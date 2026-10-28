#!/usr/bin/env python3
"""Upload all site files then create a production deployment."""
import base64, hashlib, json, os, subprocess, sys

SITE = os.path.dirname(os.path.abspath(__file__))
TEAM = "team_qOib2mCJBDzOmQxpCTYvIOAu"
VERCEL = "/opt/hatch/bin/vercel"

TEXT_FILES = [
    "index.html", "certificate-services.html", "energy-rebates.html", "sales.html",
    "energy-audits.html", "aggregation.html", "it-support.html", "billing-facility.html",
    "how-it-works.html", "faq.html", "contact.html",
    "styles.css", "site.js",
]
BINARY_FILES = [
    "logo.png", "logo-header.png", "favicon.ico", "favicon-32.png",
    "favicon-16.png", "apple-touch-icon.png",
    "img/solar-field.webp", "img/solar-sunset.webp", "img/solar-aerial.webp",
    "img/electrician.webp", "img/engineer.webp", "img/team.webp",
    "img/it-team.webp", "img/ev-charging.webp", "img/battery.gif",
]

def call(name, args):
    cmd = [VERCEL, "call-tool", "--name", name, "--arguments-json", json.dumps(args)]
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if p.returncode != 0:
        print("CALL FAILED:", name, p.stderr[:400] or p.stdout[:400])
        sys.exit(1)
    out = json.loads(p.stdout)
    return out["result"]["content"][0]["text"]

def sha1(path):
    h = hashlib.sha1()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

def main():
    skip_upload = "--skip-upload" in sys.argv
    # 1. upload binaries (or reuse already-uploaded content-addressed blobs)
    files = []
    for rel in BINARY_FILES:
        path = os.path.join(SITE, rel)
        data = open(path, "rb").read()
        digest = sha1(path)
        if not skip_upload:
            args = {
                "teamId": TEAM,
                "xVercelDigest": digest,
                "contentLength": len(data),
                "requestBody": base64.b64encode(data).decode(),
            }
            resp = call("upload_file", args)
            print("uploaded", rel, len(data) // 1024, "KB", digest[:12])
        files.append({"file": rel, "sha": digest, "size": len(data)})
    # 2. inline text files
    for rel in TEXT_FILES:
        path = os.path.join(SITE, rel)
        data = open(path, "r", encoding="utf-8").read()
        files.append({"file": rel, "data": data, "encoding": "utf-8"})
        print("inline", rel, len(data) // 1024, "KB")
    # 3. create deployment
    body = {"name": "it-green-consulting", "project": "it-green-consulting", "target": "production", "files": files}
    resp = call("create_deployment", {"teamId": TEAM, "forceNew": "1", "requestBody": body})
    print(resp[:2500])

if __name__ == "__main__":
    main()
