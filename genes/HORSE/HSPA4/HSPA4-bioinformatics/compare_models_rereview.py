"""Re-review: place the benchmark horse HSPA4 model (A0A9L0S5Z5, 800 aa) relative to
the other horse HSPA4 gene models, the Ensembl canonical transcript, human HSPA4 (P34932)
and other PTHR45639:SF6 orthologs, and test whether the segment it lacks is conserved.

Inputs (fetched from UniProt / Ensembl REST and cached in this folder):
  horse_HSPA4_all_models-rereview.fasta   all four horse HSPA4 UniProt entries
  hspa4_sf6_and_paralogs-rereview.fasta   human/mouse/rat/dog HSPA4 (SF6), human HSPA4L (SF5), human HSPH1
  ensembl_gene-rereview.json              Ensembl lookup of ENSECAG00000020813 (expand=1)

Writes RESULTS-rereview.md and results-rereview.json.
Run from repo root:
  uv run python genes/HORSE/HSPA4/HSPA4-bioinformatics/compare_models_rereview.py
"""

import json
from pathlib import Path

from Bio import Align, SeqIO

here = Path(__file__).resolve().parent
TARGET = "A0A9L0S5Z5"
HUMAN = "P34932"

horse = {r.id.split("|")[1]: str(r.seq) for r in SeqIO.parse(here / "horse_HSPA4_all_models-rereview.fasta", "fasta")}
others = {r.id.split("|")[1]: (r.id.split("|")[2], str(r.seq)) for r in SeqIO.parse(here / "hspa4_sf6_and_paralogs-rereview.fasta", "fasta")}
human = others[HUMAN][1]
gene = json.loads((here / "ensembl_gene-rereview.json").read_text())

aligner = Align.PairwiseAligner()
aligner.mode = "global"
aligner.match_score = 2
aligner.mismatch_score = -1
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.end_gap_score = 0


def compare(ref: str, other: str) -> dict:
    """Identity over paired columns and the ref segments (1-based) unpaired in `other`."""
    aln = aligner.align(ref, other)[0]
    x, y = str(aln[0]), str(aln[1])
    pairs = same = 0
    i = 0
    gaps: list[list[int]] = []
    for u, v in zip(x, y):
        if u != "-":
            i += 1
        if u != "-" and v != "-":
            pairs += 1
            same += u == v
        elif u != "-" and v == "-":
            if gaps and gaps[-1][1] == i - 1:
                gaps[-1][1] = i
            else:
                gaps.append([i, i])
    return {"len_ref": len(ref), "len_other": len(other), "paired": pairs, "identity": round(same / pairs, 4), "ref_segments_missing": gaps}


def exon_keys(tr: dict) -> set:
    return {(e["start"], e["end"]) for e in tr["Exon"]}


transcripts = {t["Translation"]["id"]: t for t in gene["Transcript"] if "Translation" in t}
canonical = next(t for t in gene["Transcript"] if t.get("is_canonical"))
canon_exons = exon_keys(canonical)

results: dict = {"gene": gene["id"], "canonical_transcript": canonical["id"], "horse_models": {}, "segment_conservation": {}}
for acc, seq in horse.items():
    results["horse_models"][acc] = compare(human, seq)

target_vs_human = results["horse_models"][TARGET]
# Exon comparison between the target transcript and the canonical transcript
target_tr = next(t for t in gene["Transcript"] if t["id"] == "ENSECAT00000106098")
results["target_transcript"] = target_tr["id"]
results["canonical_exons_absent_from_target"] = sorted(canon_exons - exon_keys(target_tr))
results["target_exons_absent_from_canonical"] = sorted(exon_keys(target_tr) - canon_exons)

# Conservation of the segment missing from the target, across SF6 orthologs and paralogs
for seg in target_vs_human["ref_segments_missing"]:
    s, e = seg
    key = f"human_{s}-{e}"
    human_seg = human[s - 1 : e]
    results["segment_conservation"][key] = {"human": human_seg}
    for acc, (name, seq) in others.items():
        if acc == HUMAN:
            continue
        aln = aligner.align(human, seq)[0]
        x, y = str(aln[0]), str(aln[1])
        i = 0
        out = []
        for u, v in zip(x, y):
            if u != "-":
                i += 1
            if s <= i <= e and u != "-":
                out.append(v)
        mapped = "".join(out)
        ident = sum(a == b for a, b in zip(human_seg, mapped)) / len(human_seg)
        results["segment_conservation"][key][f"{acc} {name}"] = {"aligned": mapped, "identity_to_human_segment": round(ident, 3)}

(here / "results-rereview.json").write_text(json.dumps(results, indent=2))

lines = ["# HSPA4 horse gene-model re-review", ""]
lines.append(f"Ensembl gene {results['gene']}; canonical transcript {results['canonical_transcript']}.")
lines.append("")
lines.append("| horse accession | length | paired with human P34932 | identity | human segments missing |")
lines.append("|---|---|---|---|---|")
for acc, r in results["horse_models"].items():
    lines.append(f"| {acc} | {r['len_other']} | {r['paired']} | {r['identity']} | {r['ref_segments_missing']} |")
lines.append("")
lines.append(f"Target transcript {results['target_transcript']}: canonical exons absent from target = {results['canonical_exons_absent_from_target']}; target exons absent from canonical = {results['target_exons_absent_from_canonical']}.")
lines.append("")
for key, d in results["segment_conservation"].items():
    lines.append(f"## Conservation of {key} (missing from {TARGET})")
    lines.append("")
    lines.append(f"Human: `{d['human']}`")
    lines.append("")
    for k, v in d.items():
        if k == "human":
            continue
        lines.append(f"- {k}: `{v['aligned']}` (identity {v['identity_to_human_segment']})")
    lines.append("")
(here / "RESULTS-rereview.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
