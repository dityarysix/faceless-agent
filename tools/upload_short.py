#!/usr/bin/env python3
# Unggah short dari content/shorts/upload_meta.json sebagai private (resumable upload).
# Kredensial hanya dari variabel lingkungan: YT_CLIENT_ID, YT_CLIENT_SECRET, YT_REFRESH_TOKEN.
# Pemakaian: python3 tools/upload_short.py
import json, os, sys, urllib.parse, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
META = os.path.join(ROOT, "content", "shorts", "upload_meta.json")

def env(name):
    v = os.environ.get(name, "")
    if not v:
        sys.exit(f"Variabel lingkungan {name} belum diset")
    return v

def access_token():
    data = urllib.parse.urlencode({
        "client_id": env("YT_CLIENT_ID"),
        "client_secret": env("YT_CLIENT_SECRET"),
        "refresh_token": env("YT_REFRESH_TOKEN"),
        "grant_type": "refresh_token",
    }).encode()
    with urllib.request.urlopen("https://oauth2.googleapis.com/token", data=data) as r:
        tok = json.load(r).get("access_token", "")
    if not tok:
        sys.exit("Gagal mendapatkan access token")
    return tok

def upload(token, meta):
    path = os.path.join(ROOT, meta["file"])
    size = os.path.getsize(path)
    body = json.dumps({
        "snippet": {"title": meta["title"], "description": meta["description"]},
        "status": {"privacyStatus": "private", "selfDeclaredMadeForKids": False,
                   "containsSyntheticMedia": True},
    }).encode()
    init = urllib.request.Request(
        "https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status",
        data=body, method="POST",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json",
                 "X-Upload-Content-Type": "video/mp4", "X-Upload-Content-Length": str(size)})
    with urllib.request.urlopen(init) as r:
        location = r.headers.get("Location")
    if not location:
        sys.exit(f"Hari {meta['day']}: tidak ada URL unggah")
    with open(path, "rb") as f:
        put = urllib.request.Request(location, data=f.read(), method="PUT",
                                     headers={"Authorization": f"Bearer {token}",
                                              "Content-Type": "video/mp4"})
        with urllib.request.urlopen(put) as r:
            res = json.load(r)
    print(f"Hari {meta['day']} | videoId: {res.get('id', 'n/a')} | "
          f"privacyStatus: {res.get('status', {}).get('privacyStatus', 'n/a')} | "
          f"uploadStatus: {res.get('status', {}).get('uploadStatus', 'n/a')}")

def main():
    with open(META, encoding="utf-8") as f:
        meta = json.load(f)
    token = access_token()
    for v in meta["videos"]:
        try:
            upload(token, v)
        except urllib.error.HTTPError as e:
            print(f"Hari {v['day']}: gagal, HTTP {e.code}")

if __name__ == "__main__":
    main()
