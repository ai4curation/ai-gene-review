"""Build AlphaFold Server job files for a multi-seed re-run of Ghs2-Bgs3.

AF3 cannot run in this repository's environment (no GPU, and the AF3 weights are
licensed per user), so this script writes job JSON for the public AlphaFold
Server (https://alphafoldserver.com), in the same format as the authors'
deposited job request (Mendeley doi:10.17632/8j46dhsyxr.1). Sequences are
fetched from UniProt and, for Ghs2/Bgs3, checked against the deposited request.

Jobs:
  * Ghs2 + Bgs3 with the Methods seed (361330275) and 9 further fixed seeds
  * Ghs2 + Bgs4 (O74475), 3 seeds: co-IP negative in PMID:42786154
  * Ghs2 + Bgs1 (Q10287), 3 seeds: Ghs2 localization does not depend on Bgs1

Output: af_server_jobs/<batch>.json (each a list of jobs, uploadable to the
server's "Upload JSON" option), plus one file per job.
Run:  uv run python make_af_server_jobs.py
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "af_server_jobs"
ACC = {"Ghs2": "O13789", "Bgs3": "Q9P377", "Bgs4": "O74475", "Bgs1": "Q10287"}
METHODS_SEED = "361330275"  # seed stated in the paper's Methods for Ghs2-Bgs3
# Fixed, arbitrary extra seeds so the run is reproducible.
EXTRA_SEEDS = ["11", "23", "101", "2024", "31337", "424242", "7777777", "123456789", "987654321"]
CONTROL_SEEDS = ["11", "101", "2024"]


def fasta(acc: str) -> str:
    txt = subprocess.run(
        ["curl", "-sS", "--fail", f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"],
        check=True, capture_output=True, text=True).stdout
    return "".join(l.strip() for l in txt.splitlines() if not l.startswith(">"))


def job(name: str, seed: str, seqs: list[str]) -> dict:
    return {
        "name": name,
        "modelSeeds": [seed],
        "sequences": [{"proteinChain": {"sequence": s, "count": 1, "useStructureTemplate": True}}
                      for s in seqs],
        "dialect": "alphafoldserver",
        "version": 1,
    }


def main() -> None:
    seq = {k: fasta(v) for k, v in ACC.items()}
    dep = HERE / "data" / "fold_ghs2_bgs3_job_request.json"
    if dep.exists():
        d = json.loads(dep.read_text()); d = d[0] if isinstance(d, list) else d
        dep_seqs = [s["proteinChain"]["sequence"] for s in d["sequences"]]
        for name, s in zip(["Ghs2", "Bgs3"], dep_seqs):
            print(f"{name}: UniProt {ACC[name]} len {len(seq[name])} "
                  f"{'== ' if s == seq[name] else '!= '}deposited len {len(s)}")
    else:
        print("deposited job request not found; run af3_interface_analysis.py first to compare")

    batches = {
        "ghs2_bgs3_multiseed": [job(f"Ghs2_Bgs3_s{s}", s, [seq["Ghs2"], seq["Bgs3"]])
                                for s in [METHODS_SEED] + EXTRA_SEEDS],
        "ghs2_controls": [job(f"Ghs2_{p}_s{s}", s, [seq["Ghs2"], seq[p]])
                          for p in ("Bgs4", "Bgs1") for s in CONTROL_SEEDS],
    }
    OUT.mkdir(exist_ok=True)
    for b, jobs in batches.items():
        (OUT / f"{b}.json").write_text(json.dumps(jobs, indent=1))
        for j in jobs:
            (OUT / f"{j['name']}.json").write_text(json.dumps([j], indent=1))
        print(f"{b}: {len(jobs)} jobs -> {OUT / (b + '.json')}")


if __name__ == "__main__":
    main()
