"""Download the structures this analysis needs.

Experimental references: human NTCP/SLC10A1 cryo-EM entries that carry a bound
ligand, which is what lets the functional sites be defined from coordinates
rather than from memory:

  7ZYI  2.88 A  NTCP + Fab/nanobody, bound NA  (sodium)
  9QZQ  3.11 A  NTCP in nanodisc, bound NA     (sodium)
  8RQF  3.41 A  NTCP, bound BJU                (N-tetradecanoylglycine,
                                                the myristoyl-glycine of the
                                                HBV preS1 anchor)

Targets: AlphaFold DB models for the human SLC10 paralogues that have no
experimental structure, plus SLC10A1 itself as a method control (if the AFDB
SLC10A1 model reproduces the experimental SLC10A1 structure, the alignment
step is trustworthy for the paralogues).

Nothing here is hardcoded: every file is fetched from RCSB or AFDB and the
provenance is written to downloads.json.
"""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.request
from pathlib import Path

PDB_ENTRIES = ["7ZYI", "9QZQ", "8RQF"]

# UniProt accession -> human-readable label
AFDB_TARGETS = {
    "Q14973": "SLC10A1 (NTCP) - method control, has experimental structures",
    "Q12908": "SLC10A2 (ASBT) - apical paralogue, bile salt transporter",
    "Q96EP9": "SLC10A4 - orphan carrier, primary question",
    "Q3KNW5": "SLC10A6 (SOAT) - sulfated steroid transporter",
    "Q0GE19": "SLC10A7 - Golgi, orphan, secondary question",
}

OUT = Path(__file__).parent / "structures"
PROV = Path(__file__).parent / "downloads.json"


def get(url: str, dest: Path, tries: int = 4) -> bool:
    if dest.exists() and dest.stat().st_size > 0:
        print(f"  cached {dest.name}")
        return True
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=120) as resp:
                dest.write_bytes(resp.read())
            print(f"  fetched {dest.name} ({dest.stat().st_size} bytes)")
            return True
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            wait = 2**attempt
            print(f"  attempt {attempt + 1} failed for {dest.name}: {exc}; retry in {wait}s")
            time.sleep(wait)
    print(f"  GAVE UP on {url}")
    return False


def resolve_afdb_url(accession: str) -> str | None:
    """Ask the AFDB API for the current model URL for this accession."""
    api = f"https://alphafold.ebi.ac.uk/api/prediction/{accession}"
    for attempt in range(3):
        try:
            with urllib.request.urlopen(api, timeout=120) as resp:
                payload = json.load(resp)
            if not payload:
                print(f"  no AFDB entry for {accession}")
                return None
            entry = payload[0]
            url = entry.get("pdbUrl")
            print(f"  {accession}: AFDB v{entry.get('latestVersion')} -> {url}")
            return url
        except (urllib.error.URLError, TimeoutError, OSError, ValueError) as exc:
            print(f"  AFDB API attempt {attempt + 1} failed for {accession}: {exc}")
            time.sleep(2**attempt)
    return None


def main() -> None:
    OUT.mkdir(exist_ok=True)
    provenance: dict[str, dict] = {"pdb": {}, "afdb": {}}

    print("Experimental structures (RCSB):")
    for pdb_id in PDB_ENTRIES:
        url = f"https://files.rcsb.org/download/{pdb_id}.cif"
        dest = OUT / f"{pdb_id}.cif"
        ok = get(url, dest)
        provenance["pdb"][pdb_id] = {"url": url, "file": dest.name, "ok": ok}

    print("Predicted models (AlphaFold DB):")
    for acc, label in AFDB_TARGETS.items():
        # Resolve the model URL from the API rather than assuming a version
        # string: AFDB has bumped the model version (v4 -> v6), and a
        # hardcoded version silently 404s.
        url = resolve_afdb_url(acc)
        dest = OUT / f"AF-{acc}.pdb"
        ok = get(url, dest) if url else False
        provenance["afdb"][acc] = {
            "url": url,
            "file": dest.name,
            "label": label,
            "ok": ok,
        }

    PROV.write_text(json.dumps(provenance, indent=2) + "\n")
    missing = [k for section in provenance.values() for k, v in section.items() if not v["ok"]]
    if missing:
        print(f"\nWARNING: {len(missing)} download(s) failed: {missing}")
        print("Downstream analysis will report these as unavailable rather than guessing.")
    else:
        print("\nAll downloads succeeded.")


if __name__ == "__main__":
    main()
