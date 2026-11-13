"""Test whether PP_5147 has the hallmarks of a HAD-family histidinol-phosphate phosphatase.

Two independent checks, each run on PP_5147 (Q88CN3) and on two controls: the
characterized HolPase PA0335 (Q9I6F6) and the characterized phosphoserine phosphatase
SerB of Methanocaldococcus jannaschii (Q58989), the PSPase reference used by Kinateder
et al. 2024.

1. Specificity fingerprint (Kinateder et al. 2024, PMID:38284491). An alanine scan of
   PA0335 showed D16, D18 and Y47 decide HolPase over PSPase activity, with Y57 and T113
   supporting. Each query is aligned globally to PA0335 (BLOSUM62) and the residues at
   those positions are read. Identity = identical aligned positions / PA0335 length.
2. NCBIfam family models with curated trusted (TC) and noise (NC) cutoffs, for the two
   HolPase models that carry EC 3.1.3.15 and the two SerB-type PSPase models that carry
   EC 3.1.3.3. A hit passes only if the full-sequence and best-domain scores both reach
   TC (HMMER --cut_tc semantics).

Run from the repository root:

    uv run python genes/PSEPK/PP_5147/PP_5147-bioinformatics/run_holpase_checks.py

Writes results.yaml and RESULTS.md next to this script. Network access to UniProt and
the NCBI HMM FTP site is required; downloads are cached under .cache/.
"""

from __future__ import annotations

import urllib.request
from pathlib import Path

import pyhmmer
import yaml
from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).parent
CACHE = Path(".cache/pp5147_holpase")
NCBIFAM = "https://ftp.ncbi.nlm.nih.gov/hmm/current"

PROTEINS = {
    "Q88CN3": "PP_5147, P. putida KT2440 (query)",
    "Q9I6F6": "PA0335 (paHisN), P. aeruginosa; characterized HolPase",
    "Q58989": "SerB (MJ1594), M. jannaschii; characterized PSPase",
}
REFERENCE = "Q9I6F6"
FINGERPRINT = {16: ("D", "required"), 18: ("D", "required"), 47: ("Y", "required"), 57: ("Y", "supporting"), 113: ("T", "supporting")}
MODELS = {
    "NF052360.1": "histidinol-phosphatase (EC 3.1.3.15)",
    "NF052359.1": "histidinol-phosphatase (EC 3.1.3.15)",
    "TIGR00338.1": "phosphoserine phosphatase SerB (EC 3.1.3.3)",
    "NF008350.0": "phosphoserine phosphatase (EC 3.1.3.3)",
}


def fetch(url: str, path: Path) -> Path:
    """Download once into the cache."""
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        req = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review"})
        with urllib.request.urlopen(req, timeout=120) as fh:
            path.write_bytes(fh.read())
    return path


def sequence(acc: str) -> str:
    fasta = fetch(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", CACHE / f"{acc}.fasta").read_text()
    return "".join(fasta.splitlines()[1:])


def fingerprint(reference: str, query: str) -> dict:
    """Residues of the query at the PA0335 fingerprint positions."""
    aligner = Align.PairwiseAligner(
        mode="global",
        substitution_matrix=substitution_matrices.load("BLOSUM62"),
        open_gap_score=-10,
        extend_gap_score=-0.5,
        end_gap_score=0,
    )
    aln = aligner.align(reference, query)[0]
    mapping = {}
    for (rs, re_), (qs, _qe) in zip(*aln.aligned):
        for i in range(int(re_ - rs)):
            mapping[int(rs) + i + 1] = int(qs) + i + 1
    identity = sum(reference[r - 1] == query[q - 1] for r, q in mapping.items()) / len(reference)
    residues = {}
    for pos, (aa, role) in FINGERPRINT.items():
        q = mapping.get(pos)
        residues[pos] = {"expected": aa, "role": role, "query_position": q, "query_residue": query[q - 1] if q else None}
    required = [r for r in residues.values() if r["role"] == "required"]
    return {
        "identity_to_PA0335": round(identity, 3),
        "required_present": sum(r["query_residue"] == r["expected"] for r in required),
        "required_total": len(required),
        "residues": residues,
    }


def score(model: str, query: str, name: str) -> dict:
    """Score one sequence against one NCBIfam model, with no reporting threshold."""
    with pyhmmer.plan7.HMMFile(fetch(f"{NCBIFAM}/hmm_PGAP.HMM/{model}.HMM", CACHE / f"{model}.HMM")) as fh:
        hmm = fh.read()
    alphabet = pyhmmer.easel.Alphabet.amino()
    seq = pyhmmer.easel.TextSequence(name=name.encode(), sequence=query).digitize(alphabet)
    block = pyhmmer.easel.DigitalSequenceBlock(alphabet, [seq])
    hits = next(pyhmmer.hmmsearch([hmm], block, E=1e6, domE=1e6, Z=1))
    seq_score = dom_score = None
    for hit in hits:
        seq_score, dom_score = hit.score, max(d.score for d in hit.domains)
    tc, nc = hmm.cutoffs.trusted, hmm.cutoffs.noise
    if seq_score is None:
        status = "NO_HIT"
    elif seq_score >= tc[0] and dom_score >= tc[1]:
        status = "ABOVE_TC"
    elif seq_score >= nc[0] and dom_score >= nc[1]:
        status = "BETWEEN_NC_TC"
    else:
        status = "BELOW_NC"
    return {
        "model": model,
        "description": MODELS[model],
        "seq_score": None if seq_score is None else round(seq_score, 1),
        "trusted_cutoff": round(tc[0], 1),
        "noise_cutoff": round(nc[0], 1),
        "status": status,
    }


def release() -> str:
    notes = fetch(f"{NCBIFAM}/RELEASE_NOTES.txt", CACHE / "RELEASE_NOTES.txt").read_text()
    return next(line.split(":", 1)[1].strip() for line in notes.splitlines() if "Release number" in line)


def render(results: dict) -> str:
    """RESULTS.md, built only from the computed results."""
    lines = [
        "# PP_5147 histidinol-phosphate phosphatase checks",
        "",
        "Generated by `run_holpase_checks.py`; do not edit by hand. Raw output: `results.yaml`.",
        f"NCBIfam release: {results['ncbifam_release']}.",
        "",
        "## Specificity fingerprint (Kinateder et al. 2024, PMID:38284491)",
        "",
        "Positions are PA0335 numbering; required residues D16, D18, Y47; supporting Y57, T113.",
        "",
        "| Protein | Identity to PA0335 | Required present | 16 | 18 | 47 | 57 | 113 |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for acc, r in results["proteins"].items():
        fp = r["fingerprint"]
        res = " | ".join(fp["residues"][p]["query_residue"] or "-" for p in FINGERPRINT)
        lines.append(
            f"| {acc} {r['label']} | {fp['identity_to_PA0335']:.1%} | "
            f"{fp['required_present']}/{fp['required_total']} | {res} |"
        )
    lines += [
        "",
        "## NCBIfam family models (score / trusted cutoff)",
        "",
        "| Protein | " + " | ".join(f"{m} {MODELS[m]}" for m in MODELS) + " |",
        "|---" * (len(MODELS) + 1) + "|",
    ]
    for acc, r in results["proteins"].items():
        cells = [
            f"{s['seq_score'] if s['seq_score'] is not None else 'no hit'} / {s['trusted_cutoff']} ({s['status']})"
            for s in r["models"]
        ]
        lines.append(f"| {acc} | " + " | ".join(cells) + " |")
    lines += [
        "",
        "The fingerprint is only trusted for proteins close to PA0335: the paper's similarity",
        "network separated the HolPase cluster at a 45.8% identity threshold. Residues read",
        "from an alignment far below that (as for the distant SerB control) are not meaningful.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    reference = sequence(REFERENCE)
    results = {"ncbifam_release": release(), "proteins": {}}
    for acc, label in PROTEINS.items():
        query = sequence(acc)
        results["proteins"][acc] = {
            "label": label,
            "length": len(query),
            "fingerprint": fingerprint(reference, query),
            "models": [score(m, query, acc) for m in MODELS],
        }
    (HERE / "results.yaml").write_text(yaml.safe_dump(results, sort_keys=False, width=120))
    (HERE / "RESULTS.md").write_text(render(results))
    print(render(results))


if __name__ == "__main__":
    main()
