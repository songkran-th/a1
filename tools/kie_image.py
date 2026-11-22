#!/usr/bin/env python3
"""Generate images with KIE (GPT Image 2.6) and download the results.

API key: in the cloud environment "a1" the network proxy injects it (nothing to set).
On a PC set the environment variable KIE_API_KEY (never commit the key).

Single image:
  python3 tools/kie_image.py --prompt-file p.txt --out out.png [--ref ref1.jpg --ref ref2.jpg] [--model sunburst]
Batch (JSON list of {"name","prompt","refs":[paths]} ; runs in parallel, writes <outdir>/<name>.png/.jpg):
  python3 tools/kie_image.py --batch jobs.json --outdir dir [--workers 6]
Credits:
  python3 tools/kie_image.py --credits
Every finished task is appended to <outdir or out's dir>/kie_log.jsonl (name, taskId, url, credits).
"""
import argparse, json, os, sys, time, threading, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor

API = "https://api.kie.ai"
UPLOAD = "https://kieai.redpandaai.co/api/file-stream-upload"
_lock = threading.Lock()
_uploaded = {}
AUTH = "Bearer " + os.environ.get("KIE_API_KEY", "proxy-injected")

def call(method, path, body=None):
    req = urllib.request.Request(API + path, method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"Content-Type": "application/json", "Authorization": AUTH})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read())

def upload(path):
    """Upload a local reference image to KIE temp storage (kept 24h); returns its URL."""
    with _lock:
        if path in _uploaded: return _uploaded[path]
    b = uuid.uuid4().hex
    name = os.path.basename(path)
    ctype = "image/png" if name.lower().endswith(".png") else "image/jpeg"
    parts = []
    for k, v in (("uploadPath", "phijuk/refs"), ("fileName", name)):
        parts.append(f'--{b}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode())
    parts.append(f'--{b}\r\nContent-Disposition: form-data; name="file"; filename="{name}"\r\nContent-Type: {ctype}\r\n\r\n'.encode()
                 + open(path, "rb").read() + b"\r\n")
    parts.append(f"--{b}--\r\n".encode())
    req = urllib.request.Request(UPLOAD, data=b"".join(parts), method="POST",
        headers={"Content-Type": f"multipart/form-data; boundary={b}", "Authorization": AUTH})
    with urllib.request.urlopen(req, timeout=300) as r:
        url = json.loads(r.read())["data"]["downloadUrl"]
    with _lock: _uploaded[path] = url
    return url

def generate(prompt, out, refs=(), model="sunburst", ratio="16:9", res="2K", quality="high", name=None):
    inp = {"prompt": prompt, "aspect_ratio": ratio, "output_format": "png"}
    if model != "economy": inp.update({"resolution": res, "quality": quality})
    mode = "text-to-image"
    if refs:
        inp["input_urls"] = [upload(p) for p in refs]; mode = "image-to-image"
    r = call("POST", "/api/v1/jobs/createTask", {"model": f"gpt-image-2-6/{model}-{mode}", "input": inp})
    if r.get("code") != 200: raise RuntimeError(f"createTask failed: {r}")
    tid = r["data"]["taskId"]
    for _ in range(180):
        time.sleep(5)
        d = call("GET", f"/api/v1/jobs/recordInfo?taskId={tid}")["data"]
        if d["state"] == "success":
            url = json.loads(d["resultJson"])["resultUrls"][0]
            urllib.request.urlretrieve(url, out)
            try:
                from PIL import Image
                Image.open(out).convert("RGB").save(os.path.splitext(out)[0] + ".jpg", quality=95, subsampling=0)
            except ImportError: pass
            rec = {"name": name or os.path.basename(out), "taskId": tid, "url": url, "credits": d.get("creditsConsumed"), "refs": list(refs)}
            with _lock, open(os.path.join(os.path.dirname(os.path.abspath(out)), "kie_log.jsonl"), "a") as f:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            return rec
        if d["state"] == "fail": raise RuntimeError(f"task {tid} failed: {d.get('failCode')} {d.get('failMsg')}")
    raise RuntimeError(f"task {tid} timeout")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt-file"); ap.add_argument("--out"); ap.add_argument("--ref", action="append", default=[])
    ap.add_argument("--batch"); ap.add_argument("--outdir"); ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--model", default="sunburst", choices=["sunburst", "flare", "economy"])
    ap.add_argument("--ratio", default="16:9"); ap.add_argument("--res", default="2K")
    ap.add_argument("--quality", default="high"); ap.add_argument("--credits", action="store_true")
    a = ap.parse_args()
    kw = dict(model=a.model, ratio=a.ratio, res=a.res, quality=a.quality)
    if a.credits:
        print(json.dumps(call("GET", "/api/v1/chat/credit"))); return
    if a.batch:
        jobs = json.load(open(a.batch, encoding="utf-8")); os.makedirs(a.outdir, exist_ok=True)
        def run(j):
            try:
                r = generate(j["prompt"], os.path.join(a.outdir, j["name"] + ".png"), j.get("refs", []), name=j["name"], **kw)
                print("OK", j["name"], r["credits"], flush=True)
            except Exception as e:
                print("FAIL", j["name"], e, flush=True)
        with ThreadPoolExecutor(a.workers) as ex: list(ex.map(run, jobs))
        print("DONE", flush=True); return
    prompt = open(a.prompt_file, encoding="utf-8").read().strip()
    r = generate(prompt, a.out, a.ref, **kw)
    print("url", r["url"], "credits", r["credits"]); print("saved", a.out)

if __name__ == "__main__":
    main()
