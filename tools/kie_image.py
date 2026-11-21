#!/usr/bin/env python3
"""Generate images with KIE (GPT Image 2.6) and download the results.

The KIE API key is injected by the cloud session's network proxy; no key is read here.
Usage:
  python3 tools/kie_image.py --prompt-file p.txt --out out.png [--model sunburst] [--ratio 16:9] [--res 2K] [--quality high]
  python3 tools/kie_image.py --credits
"""
import argparse, json, sys, time, urllib.request

API = "https://api.kie.ai"

def call(method, path, body=None):
    req = urllib.request.Request(API + path, method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"Content-Type": "application/json", "Authorization": "Bearer proxy-injected"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read())

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt-file"); ap.add_argument("--out")
    ap.add_argument("--model", default="sunburst", choices=["sunburst", "flare", "economy"])
    ap.add_argument("--ratio", default="16:9"); ap.add_argument("--res", default="2K")
    ap.add_argument("--quality", default="high"); ap.add_argument("--credits", action="store_true")
    a = ap.parse_args()
    if a.credits:
        print(json.dumps(call("GET", "/api/v1/chat/credit"))); return
    prompt = open(a.prompt_file, encoding="utf-8").read().strip()
    inp = {"prompt": prompt, "aspect_ratio": a.ratio, "output_format": "png"}
    if a.model != "economy":
        inp.update({"resolution": a.res, "quality": a.quality})
    r = call("POST", "/api/v1/jobs/createTask", {"model": f"gpt-image-2-6/{a.model}-text-to-image", "input": inp})
    if r.get("code") != 200:
        sys.exit(f"createTask failed: {r}")
    tid = r["data"]["taskId"]; print("task", tid, flush=True)
    for _ in range(120):
        time.sleep(5)
        d = call("GET", f"/api/v1/jobs/recordInfo?taskId={tid}")["data"]
        if d["state"] == "success":
            url = json.loads(d["resultJson"])["resultUrls"][0]
            print("url", url, "credits", d.get("creditsConsumed"), flush=True)
            urllib.request.urlretrieve(url, a.out); print("saved", a.out); return
        if d["state"] == "fail":
            sys.exit(f"failed: {d.get('failCode')} {d.get('failMsg')}")
    sys.exit("timeout")

if __name__ == "__main__":
    main()
