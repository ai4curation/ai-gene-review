"""Compare all horse EFR3A UniProt gene models with each other and with human Q14156.

Run from the repository root:
    uv run python genes/HORSE/EFR3A/EFR3A-bioinformatics/compare_horse_models_rereview.py

Fetches (UniProt REST, Ensembl REST) every horse UniProtKB entry for gene EFR3A plus the
benchmark accession (whose record carries no gene name),
records the Ensembl gene/transcript each derives from, the exon coordinates of
each transcript, and a global alignment of each model against human Q14156.
Outputs: horse_models_rereview.json and RESULTS-rereview.md (this folder).
Nothing is hardcoded; results are computed from the fetched records.
"""

import hashlib
import json
import time
import urllib.request
from pathlib import Path

from Bio import Align, SeqIO

here = Path(__file__).resolve().parent
root = next(p for p in here.parents if (p / "pyproject.toml").exists())
BENCHMARK = "A0A9L0S4L8"


def get_json(url: str) -> dict:
    # Ensembl REST answers HTTP 500 to the default "Python-urllib" User-Agent, so send our own.
    req = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review/EFR3A-rereview"})
    with urllib.request.urlopen(req) as fh:
        return json.load(fh)


human = SeqIO.read(root / "genes/human/EFR3A/EFR3A-uniprot.txt", "swiss")
hseq = str(human.seq)

search = get_json(
    "https://rest.uniprot.org/uniprotkb/search?query=(gene:EFR3A+OR+accession:"
    f"{BENCHMARK})+AND+organism_id:9796"
    "&fields=accession,length,reviewed,sequence,xref_ensembl,xref_panther,go_id&format=json"
)

aligner = Align.PairwiseAligner(
    mode="global", match_score=2, mismatch_score=-1, open_gap_score=-10, extend_gap_score=-0.5
)

mouse_txt = urllib.request.urlopen("https://rest.uniprot.org/uniprotkb/Q8BG67.fasta").read().decode()
mseq = "".join(mouse_txt.splitlines()[1:])
# Mouse EFR3A basic-patch residues mutated in PMID:24360784 (K50E, R53A, R61E, R68E, R70E).
MOUSE_BASIC = [50, 53, 61, 68, 70]


def pair_map(a: str, b: str) -> dict[int, int]:
    al = aligner.align(a, b)[0]
    out = {}
    for (s, e), (t, u) in zip(*al.aligned):
        for i, j in zip(range(s, e), range(t, u)):
            out[int(i)] = int(j)
    return out


mouse_to_human = pair_map(mseq, hseq)
basic_human = {p: mouse_to_human.get(p - 1) for p in MOUSE_BASIC}

models = []
for entry in search["results"]:
    acc = entry["primaryAccession"]
    seq = entry["sequence"]["value"]
    ens = [x for x in entry["uniProtKBCrossReferences"] if x["database"] == "Ensembl"]
    panther = [x["id"] for x in entry["uniProtKBCrossReferences"] if x["database"] == "PANTHER"]
    go_ids = [x["id"] for x in entry["uniProtKBCrossReferences"] if x["database"] == "GO"]
    transcript = ens[0]["id"].split(".")[0]
    gene = [p["value"] for p in ens[0]["properties"] if p["key"] == "GeneId"][0]
    time.sleep(3)
    tx = get_json(
        f"https://rest.ensembl.org/lookup/id/{transcript}?content-type=application/json;expand=1"
    )
    exons = sorted((e["start"], e["end"]) for e in tx["Exon"])
    al = aligner.align(hseq, seq)[0]
    pairs = {}
    for (s, e), (t, u) in zip(*al.aligned):
        for i, j in zip(range(s, e), range(t, u)):
            pairs[int(i)] = int(j)
    ident = sum(hseq[i] == seq[j] for i, j in pairs.items())
    unpaired_human = [i + 1 for i in range(len(hseq)) if i not in pairs]
    cys_6_9 = [pairs.get(i) for i in range(5, 9)]
    basic = []
    for mp, hi in basic_human.items():
        j = pairs.get(hi) if hi is not None else None
        basic.append(f"{mseq[mp - 1]}{mp}->{seq[j] + str(j + 1) if j is not None else '-'}")
    models.append(
        {
            "accession": acc,
            "length": len(seq),
            "reviewed": entry["entryType"],
            "ensembl_gene": gene,
            "ensembl_transcript": transcript,
            "panther": panther,
            "go_ids_in_record": go_ids,
            "n_exons": len(exons),
            "first_exon": exons[0],
            "second_exon": exons[1],
            "n_terminus_30": seq[:30],
            "identity_paired_percent": round(100 * ident / len(pairs), 2),
            "paired_residues": len(pairs),
            "human_residues_unpaired": unpaired_human,
            "human_cys6_9_aligned_residues": "".join(seq[j] if j is not None else "-" for j in cys_6_9),
            "mouse_basic_patch_mapped": basic,
            "sha256": hashlib.sha256(seq.encode()).hexdigest(),
        }
    )

(here / "horse_models_rereview.json").write_text(json.dumps(models, indent=2) + "\n")


def ranges(nums: list[int]) -> str:
    if not nums:
        return "none"
    out, start, prev = [], nums[0], nums[0]
    for n in nums[1:]:
        if n != prev + 1:
            out.append(f"{start}-{prev}" if start != prev else f"{start}")
            start = n
        prev = n
    out.append(f"{start}-{prev}" if start != prev else f"{start}")
    return ",".join(out)


lines = [
    "# EFR3A (horse): comparison of all horse UniProt gene models (re-review)",
    "",
    f"Human reference: {human.id} ({len(hseq)} residues, N-terminus {hseq[:30]}).",
    "",
    "| Accession | Length | Ensembl gene | Transcript | First exon (chr9) | N-terminus | Identity to human (paired) | Human residues unpaired | Residues at human Cys6-Cys9 | Mouse basic patch (PMID:24360784) mapped | GO in record |",
    "|---|---|---|---|---|---|---|---|---|---|---|",
]
for m in sorted(models, key=lambda m: m["first_exon"][0]):
    lines.append(
        f"| {m['accession']}{' (benchmark)' if m['accession'] == BENCHMARK else ''} | {m['length']} | "
        f"{m['ensembl_gene']} | {m['ensembl_transcript']} | {m['first_exon'][0]}-{m['first_exon'][1]} | "
        f"{m['n_terminus_30']} | {m['identity_paired_percent']}% over {m['paired_residues']} | "
        f"{ranges(m['human_residues_unpaired'])} | {m['human_cys6_9_aligned_residues']} | {' '.join(m['mouse_basic_patch_mapped'])} | "
        f"{', '.join(m['go_ids_in_record']) or 'none'} |"
    )
genes = sorted({m["ensembl_gene"] for m in models})
lines += [
    "",
    f"All horse EFR3A models derive from Ensembl gene(s): {', '.join(genes)}.",
    "",
    "Alignment: Biopython PairwiseAligner global, match 2, mismatch -1, gap open -10, extend -0.5. "
    "Exon coordinates are from the Ensembl REST lookup of each transcript. Per-model details, including "
    "sequence hashes, are in `horse_models_rereview.json`.",
    "",
]
(here / "RESULTS-rereview.md").write_text("\n".join(lines))
print("\n".join(lines))
