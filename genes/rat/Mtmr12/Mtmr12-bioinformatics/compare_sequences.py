#!/usr/bin/env python3
"""Map rat A0A8I5ZMD5 (Mtmr12 TrEMBL product) onto the reviewed rat product
Q5FVM6 and human MTMR12 (Q9C0I1), and check the active-myotubularin catalytic
motif positions against human MTM1 (Q13496, active site C375).

Inputs (all in this folder or the gene folder; none are predictions):
  ../Mtmr12-uniprot.txt               target sequence (UniProt flat file SQ block)
  ../Mtmr12-same-gene-reference.json  reviewed rat Q5FVM6 record (JSON)
  MTMR12_HUMAN_Q9C0I1.fasta           human MTMR12 (UniProt REST)
  MTM1_HUMAN_Q13496.fasta             human MTM1 (UniProt REST)

Run: UV_NO_SYNC=1 uv run python compare_sequences.py
Alignments describe sequence correspondence, not expression or activity.
"""
import json
from pathlib import Path

from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).resolve().parent
GENE = HERE.parent.name


def read_flatfile_seq(path: Path) -> tuple[str, str]:
    lines = path.read_text().splitlines()
    acc = lines[1].split()[1].rstrip(";")
    i = next(k for k, ln in enumerate(lines) if ln.startswith("SQ "))
    seq = "".join(ln.strip().replace(" ", "") for ln in lines[i + 1 :] if not ln.startswith("//"))
    return acc, seq


def read_fasta(path: Path) -> tuple[str, str]:
    lines = path.read_text().splitlines()
    return lines[0].split("|")[1], "".join(lines[1:])


def aligner() -> PairwiseAligner:
    a = PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    return a


def segments(aln, a: str, b: str) -> list[dict]:
    out = []
    for (x, y), (u, v) in zip(aln.aligned[0], aln.aligned[1]):
        x, y, u, v = map(int, (x, y, u, v))
        out.append({"a_start": x + 1, "a_end": y, "b_start": u + 1, "b_end": v,
                    "identical": sum(a[x + k] == b[u + k] for k in range(y - x))})
    return out


def posmap(aln) -> dict[int, int]:
    m = {}
    for (x, y), (u, v) in zip(aln.aligned[0], aln.aligned[1]):
        for k in range(int(y) - int(x)):
            m[int(x) + k + 1] = int(u) + k + 1
    return m


tacc, target = read_flatfile_seq(HERE.parent / f"{GENE}-uniprot.txt")
ref = json.loads((HERE.parent / f"{GENE}-same-gene-reference.json").read_text())["record"]
racc, rseq = ref["primaryAccession"], ref["sequence"]["value"]
hacc, hseq = read_fasta(HERE / "MTMR12_HUMAN_Q9C0I1.fasta")
macc, mseq = read_fasta(HERE / "MTM1_HUMAN_Q13496.fasta")

al = aligner()
aln_ref = al.align(rseq, target)[0]
aln_hum = al.align(hseq, target)[0]
aln_mtm1 = al.align(mseq, target)[0]

seg_ref = segments(aln_ref, rseq, target)
seg_hum = segments(aln_hum, hseq, target)
hum_ident = sum(s["identical"] for s in seg_hum)

# MTM1 catalytic loop C375-R381 (CX5R) plus D278-region not needed; check C375..R381
m2t = posmap(aln_mtm1)
cat = []
for p in range(373, 384):
    q = m2t.get(p)
    cat.append({"mtm1_pos": p, "mtm1_res": mseq[p - 1], "target_pos": q,
                "target_res": target[q - 1] if q else "-"})

ref_domain = []
r2t = posmap(aln_ref)
for f in ref.get("features", []):
    if f["type"] != "Domain":
        continue
    s, e = f["location"]["start"]["value"], f["location"]["end"]["value"]
    mapped = [(p, r2t[p]) for p in range(s, e + 1) if p in r2t]
    ref_domain.append({"description": f.get("description", ""), "start": s, "end": e,
                       "mapped": len(mapped), "identical": sum(rseq[p - 1] == target[q - 1] for p, q in mapped)})

out = {
    "target": tacc, "target_length": len(target), "target_nterm40": target[:40],
    "rat_reference": racc, "rat_reference_length": len(rseq), "rat_reference_nterm56": rseq[:56],
    "human_mtmr12": hacc, "human_length": len(hseq), "human_identical_aligned": hum_ident,
    "segments_vs_rat_reference": seg_ref, "segments_vs_human": seg_hum,
    "rat_reference_domains": ref_domain, "mtm1_catalytic_loop": cat,
    "method": "Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5",
}
(HERE / "results.json").write_text(json.dumps(out, indent=2) + "\n")

L = [f"# {GENE}: target product vs reviewed rat, human MTMR12 and human MTM1", "",
     f"Target {tacc} ({len(target)} aa) from `{GENE}-uniprot.txt`; reviewed rat {racc} ({len(rseq)} aa); "
     f"human MTMR12 {hacc} ({len(hseq)} aa); human MTM1 {macc} ({len(mseq)} aa).", "",
     out["method"] + ".", "",
     f"Target N-terminal 40 aa: `{target[:40]}`", "",
     f"Reviewed rat N-terminal 56 aa: `{rseq[:56]}`", "",
     "## Target vs reviewed rat Q5FVM6", "",
     "| Reference interval | Target interval | Identical residues |", "|---|---|---|"]
L += [f"| {s['a_start']}–{s['a_end']} | {s['b_start']}–{s['b_end']} | {s['identical']} |" for s in seg_ref]
L += ["", "| Reference domain | Interval | Mapped | Identical |", "|---|---|---|---|"]
L += [f"| {d['description']} | {d['start']}–{d['end']} | {d['mapped']} | {d['identical']} |" for d in ref_domain]
L += ["", "## Target vs human MTMR12", "",
      f"Identical aligned residues: {hum_ident} of {len(target)} target residues.", "",
      "| Human interval | Target interval | Identical residues |", "|---|---|---|"]
L += [f"| {s['a_start']}–{s['a_end']} | {s['b_start']}–{s['b_end']} | {s['identical']} |" for s in seg_hum]
L += ["", "## MTM1 catalytic loop (active-site C375, CX5R motif 375–381) mapped to target", "",
      "| MTM1 pos | MTM1 res | Target pos | Target res |", "|---|---|---|---|"]
L += [f"| {c['mtm1_pos']} | {c['mtm1_res']} | {c['target_pos']} | {c['target_res']} |" for c in cat]
L += ["", "Sequence correspondence does not establish expression, folding, localization or binding.", ""]
(HERE / "RESULTS.md").write_text("\n".join(L))
(HERE / "alignment.txt").write_text(str(aln_ref) + "\n")
