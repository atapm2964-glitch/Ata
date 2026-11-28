#!/usr/bin/env python3
"""Patch AtaVision 80.0.0.0 offline HTML -> 81.0.0.0.

Usage:
  python3 scripts/patch-v81.py <input-v80.html> <output-v81.html>

What it does (safe, string-level, no re-serialization):
  1. Bumps version markers 80.0.0.0 -> 81.0.0.0 (meta + APP_VERSION).
  2. Switches subscription prefix AV80 -> AV81 and rejects AV80 codes
     (v80 codes are archive-only in v81, per owner decision).
  3. Relaxes CSP connect-src from 'none' to allow the GitHub Pages origin
     for the optional update check, keeping everything else identical.
     Offline use still works: the update check fails silently offline.
  4. Injects a small, self-contained update-check snippet before </body>
     that fetches version.json from GitHub Pages and shows a toast if a
     newer version exists. It never blocks the app and never sends user data.

It does NOT touch physics content, storage keys, or backup format, so
user data migrates without loss. Run it only on the verified v80 file
(SHA-256 61ba80dd7b7c5a287a7f05db8198e31cb7f14647a0a2fb4ca6015ab22f76ce95).
"""
import hashlib
import re
import sys

V80_SHA256 = "61ba80dd7b7c5a287a7f05db8198e31cb7f14647a0a2fb4ca6015ab22f76ce95"
PAGES_ORIGIN = "https://atapm2964-glitch.github.io/Ata"

UPDATE_SNIPPET = """<script>
/* AtaVision 81: optional update check (GitHub Pages). Offline-safe: silent on failure. */
(function(){try{var v='81.0.0.0';fetch('https://atapm2964-glitch.github.io/Ata/version.json',{cache:'no-store'}).then(function(r){return r.ok?r.json():null}).then(function(j){if(!j||!j.version)return;function cmp(a,b){var x=a.split('.'),y=b.split('.');for(var i=0;i<Math.max(x.length,y.length);i++){var d=(parseInt(x[i]||'0',10)-parseInt(y[i]||'0',10));if(d)return d}return 0}if(cmp(j.version,v)>0){var d=document.createElement('div');d.setAttribute('role','status');d.style.cssText='position:fixed;inset-inline:12px;bottom:12px;z-index:9999;background:#fff;border:1px solid #c3d7ec;border-radius:14px;padding:10px 14px;font:14px/1.8 Tahoma,sans-serif;color:#24456b;box-shadow:0 10px 30px rgba(0,0,0,.18)';d.textContent='نسخهٔ تازهٔ AtaVision ('+j.version+') منتشر شده است. برای دانلود به صفحهٔ GitHub مراجعه کنید.';document.body.appendChild(d);setTimeout(function(){d.remove()},12000)}}).catch(function(){})}catch(e){}})();
</script>
"""


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    src, dst = sys.argv[1], sys.argv[2]
    with open(src, "rb") as f:
        raw = f.read()
    digest = sha256_bytes(raw)
    print(f"input sha256: {digest}")
    if digest != V80_SHA256:
        print(f"WARNING: input is not the published v80 file (expected {V80_SHA256}).")
        print("Continuing anyway — verify you are patching the right file.")
    text = raw.decode("utf-8", errors="strict")

    # 1. Version bump (exact markers only).
    text = text.replace('content="80.0.0.0"', 'content="81.0.0.0"')
    text = text.replace("APP_VERSION='80.0.0.0'", "APP_VERSION='81.0.0.0'")
    text = text.replace('APP_VERSION="80.0.0.0"', 'APP_VERSION="81.0.0.0"')

    # 2. Subscription prefix AV80 -> AV81 (code strings only, not base64 blobs:
    #    require a non-base64 boundary: quote or dash or dot after the prefix).
    text, n = re.subn(r"AV80(?=[\"'\-.\s])", "AV81", text)
    print(f"AV80->AV81 replacements: {n}")

    # 3. CSP: allow Pages origin for update check.
    if "connect-src 'none'" in text:
        text = text.replace(
            "connect-src 'none'",
            f"connect-src 'none' {PAGES_ORIGIN}",
            1,
        )
        print("CSP connect-src updated.")
    else:
        print("CSP connect-src 'none' not found — left unchanged.")

    # 4. Inject update check before the last </body>.
    if "AtaVision 81: optional update check" not in text:
        idx = text.rfind("</body>")
        if idx == -1:
            print("ERROR: </body> not found.")
            return 1
        text = text[:idx] + UPDATE_SNIPPET + text[idx:]
        print("Update-check snippet injected.")

    out = text.encode("utf-8")
    with open(dst, "wb") as f:
        f.write(out)
    print(f"wrote {dst} ({len(out)} bytes, sha256 {sha256_bytes(out)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
