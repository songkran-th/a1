#!/usr/bin/env python3
"""Image-to-video with KIE (Grok Imagine or MiniMax H3). Keys are injected by the cloud proxy (environment "a1").

Batch file: JSON list of {"name","model":"grok"|"h3","image":local_path,"prompt","duration":int}
  python3 tools/kie_video.py --batch jobs.json --outdir dir [--workers 4] [--res 720p|1080p (grok) / 768P|2K (h3)]
Writes <outdir>/<name>.mp4 and appends to <outdir>/kie_log.jsonl. Both models also generate an audio track (mute it in the edit).
"""
import argparse, json, os, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.dirname(__file__))
from kie_image import call, upload, _lock

def generate(j, outdir, res_grok="720p", res_h3="768P"):
    url = upload(j["image"])
    if j["model"] == "grok":
        body = {"model": "grok-imagine/image-to-video",
                "input": {"image_urls": [url], "prompt": j["prompt"], "mode": "normal",
                          "duration": int(j.get("duration", 10)), "resolution": res_grok}}
    else:
        body = {"model": "minimax-h3/image-to-video",
                "input": {"first_frame_url": url, "prompt": j["prompt"],
                          "duration": int(j.get("duration", 10)), "resolution": res_h3}}
    r = call("POST", "/api/v1/jobs/createTask", body)
    if r.get("code") != 200: raise RuntimeError(f"createTask failed: {r}")
    tid = r["data"]["taskId"]
    for _ in range(360):
        time.sleep(10)
        d = call("GET", f"/api/v1/jobs/recordInfo?taskId={tid}")["data"]
        if d["state"] == "success":
            vurl = json.loads(d["resultJson"])["resultUrls"][0]
            out = os.path.join(outdir, j["name"] + ".mp4")
            urllib.request.urlretrieve(vurl, out)
            rec = {"name": j["name"], "model": j["model"], "taskId": tid, "url": vurl, "credits": d.get("creditsConsumed")}
            with _lock, open(os.path.join(outdir, "kie_log.jsonl"), "a") as f: f.write(json.dumps(rec) + "\n")
            return rec
        if d["state"] == "fail": raise RuntimeError(f"task {tid} failed: {d.get('failCode')} {d.get('failMsg')}")
    raise RuntimeError(f"task {tid} timeout")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", required=True); ap.add_argument("--outdir", required=True)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--res-grok", default="720p"); ap.add_argument("--res-h3", default="768P")
    a = ap.parse_args(); os.makedirs(a.outdir, exist_ok=True)
    jobs = json.load(open(a.batch, encoding="utf-8"))
    def run(j):
        try:
            r = generate(j, a.outdir, a.res_grok, a.res_h3); print("OK", j["name"], r["credits"], flush=True)
        except Exception as e:
            print("FAIL", j["name"], e, flush=True)
    with ThreadPoolExecutor(a.workers) as ex: list(ex.map(run, jobs))
    print("DONE", flush=True)

if __name__ == "__main__":
    main()
