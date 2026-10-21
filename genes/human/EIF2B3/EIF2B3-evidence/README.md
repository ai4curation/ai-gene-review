# Reproducing EIF2B3 source projections

`reproduce.py` is a Python 3 standard-library program. It parses 16 saved official inputs and reconstructs the target's ancestral path, aligned sequence, literal PAINT records, ARBA condition matches, selected donor annotations, Reactome entity chains and HPA location summary. It does not make biological decisions or retrieve article bodies.

`inputs.json` lists original source URLs, input filenames, byte lengths and SHA-256 hashes. Put those exact responses in a directory, then run:

```sh
python3 reproduce.py --input-dir /path/to/saved-inputs --output reproduced.json
```

Compare the result with `source-projections.json`. The complete PAINT IBD file is required; the selected output rows alone are not used to infer absence of a loss along the path. The source snapshots are intentionally not bundled here, and current downloads may differ from the saved hashes. A newer snapshot should be reviewed separately instead of bypassing the hash checks.

The replay was run with normal and optimized Python, producing identical output. Inputs were supplied through a separate directory, and a changed UniProt input was rejected before output creation. All logical input checks remain active under optimization. The script uses no YAML or third-party parsing packages.

`original-locators.json` records the normal publication-cache hashes and the precise independently assessed original sections. These locators document access; they do not claim that an abstract-only cache contains the separately recovered original. `RESULTS.md` explains the biological interpretation and its limits. The review's zero-quotation policy is preserved.

## Obtaining the external inputs

From this evidence directory, the following standard-library command downloads each URL recorded in `inputs.json` into a new directory. It accepts a response only when both its length and SHA-256 match the recorded snapshot; HTTP failures or changed bytes stop the command. It never updates the manifest or bypasses `reproduce.py` checks.

```sh
python3 - <<'PY'
import hashlib
import json
from pathlib import Path
from urllib.request import Request, urlopen

out = Path("downloaded-inputs")
out.mkdir(exist_ok=False)
for item in json.loads(Path("inputs.json").read_text())["inputs"]:
    request = Request(item["url"], headers={"User-Agent": "EIF2B3-evidence-replay/1"})
    with urlopen(request, timeout=120) as response:
        data = response.read()
    digest = hashlib.sha256(data).hexdigest()
    if len(data) != item["bytes"] or digest != item["sha256"]:
        raise SystemExit(f"Source changed: {item['name']} ({len(data)} bytes; SHA-256 {digest})")
    with (out / item["name"]).open("xb") as handle:
        handle.write(data)
print("All source snapshots authenticated.")
PY
python3 reproduce.py --input-dir downloaded-inputs --output reproduced.json
```

These are live source endpoints, not guaranteed historical archives. If any source has changed or is unavailable, obtain the recorded responses from the evidence depositor and place them under the names in `inputs.json`; a fresh checkout alone does not contain those external bytes. Preserve a newer download as a separate version for a new assessment. Do not alter the recorded hashes merely to make the historical replay run. Full IBD input is required because selected output rows cannot reproduce the path-wide loss check. The fetch example is an acquisition recipe, not a claim that today's endpoints still return the captured versions.
