#!/usr/bin/env python3
"""Refresh official family records without rewriting source responses."""
from pathlib import Path
import hashlib
import json
import urllib.request
from datetime import datetime, timezone
base = Path(__file__).resolve().parent
manifest = json.loads((base / "manifest.json").read_text())
for source in manifest["sources"]:
    with urllib.request.urlopen(source["url"], timeout=60) as response:
        data = response.read()
    if source["file"].endswith(".json"):
        json.loads(data)
    (base / source["file"]).write_bytes(data)
    source["sha256"] = hashlib.sha256(data).hexdigest()
manifest["retrieved"] = datetime.now(timezone.utc).isoformat()
(base / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
