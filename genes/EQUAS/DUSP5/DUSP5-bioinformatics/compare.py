"""Compare the donkey UniProt protein with its human reviewed ortholog record.

Run from the repository root:
    uv run python genes/EQUAS/<GENE>/<GENE>-bioinformatics/compare.py
Inputs: the donkey flat file in the gene folder, the human UniProt flat file and
the QuickGO annotation download (human-*-quickgo-annotations.tsv) in this folder.
Outputs: alignment.json and RESULTS.md (regenerated; nothing is hardcoded).
Global alignment, Biopython PairwiseAligner, BLOSUM62, gap open -10, extend -0.5.
Pairwise similarity alone does not establish orthology or function.
"""
import csv, json
from pathlib import Path
from Bio import Align, SeqIO
from Bio.Align import substitution_matrices

here = Path(__file__).resolve().parent
gene = here.parent.name
donkey_file = here.parent / f"{gene}-uniprot.txt"
human_file = next(here.glob("human-*-uniprot.txt"))
goa_file = next(here.glob("human-*-quickgo-annotations.tsv"))
hr, dr = SeqIO.read(human_file, "swiss"), SeqIO.read(donkey_file, "swiss")
al = Align.PairwiseAligner(mode="global")
al.substitution_matrix = substitution_matrices.load("BLOSUM62")
al.open_gap_score, al.extend_gap_score = -10, -0.5
best = al.align(hr.seq, dr.seq)[0]
h2d = {}
for (s, e), (t, u) in zip(*best.aligned):
    for i, j in zip(range(s, e), range(t, u)):
        h2d[i] = j
hs, ds = str(hr.seq), str(dr.seq)
paired = len(h2d)
ident = sum(hs[i] == ds[j] for i, j in h2d.items())
mapped_donkey = set(h2d.values())

def runs(positions):
    out = []
    for p in sorted(positions):
        if out and p == out[-1][1] + 1:
            out[-1][1] = p
        else:
            out.append([p, p])
    return out

donkey_unpaired = [r for r in runs(j + 1 for j in range(len(ds)) if j not in mapped_donkey) if r[1] - r[0] >= 4]
human_unpaired = [r for r in runs(i + 1 for i in range(len(hs)) if i not in h2d) if r[1] - r[0] >= 4]
feats = []
for f in hr.features:
    if f.type not in {"ACT_SITE", "DISULFID", "MOTIF", "TRANSMEM", "SIGNAL", "DOMAIN", "SITE"}:
        continue
    s, e = int(f.location.start), int(f.location.end)
    pts = [s, e - 1] if f.type in {"DISULFID"} else ([s] if e - s == 1 else [s, e - 1])
    note = f.qualifiers.get("note", "")
    if isinstance(note, list):
        note = note[0]
    hres = "".join(hs[p] for p in pts)
    dpos = [h2d.get(p) for p in pts]
    dres = "".join(ds[p] if p is not None else "-" for p in dpos)
    rng = range(s, e)
    npair = sum(1 for p in rng if p in h2d)
    nid = sum(1 for p in rng if p in h2d and hs[p] == ds[h2d[p]])
    feats.append(dict(type=f.type, note=note, human=[p + 1 for p in pts], human_res=hres,
                      donkey=[p + 1 if p is not None else None for p in dpos], donkey_res=dres,
                      span_len=e - s, span_paired=npair, span_identical=nid))
rows = []
with open(goa_file) as fh:
    for r in csv.DictReader(fh, delimiter="\t"):
        if r["GO EVIDENCE CODE"] in {"IEA"}:
            continue
        rows.append(r)
res = dict(human=hr.id, donkey=dr.id, human_length=len(hs), donkey_length=len(ds), paired=paired,
           identical=ident, identity_pct=round(100 * ident / paired, 2),
           human_coverage_pct=round(100 * paired / len(hs), 2), donkey_coverage_pct=round(100 * paired / len(ds), 2),
           donkey_ranges_without_human_partner=donkey_unpaired, human_ranges_without_donkey_partner=human_unpaired,
           features=feats, alignment=str(best))
(here / "alignment.json").write_text(json.dumps(res, indent=2) + "\n")
L = [f"# {gene}: donkey-human comparison", "",
     f"Donkey {dr.id} ({len(ds)} aa) aligned globally to human {hr.id} ({len(hs)} aa): {res['identity_pct']}% identity over {paired} paired residues; paired coverage {res['human_coverage_pct']}% of human and {res['donkey_coverage_pct']}% of donkey.",
     "", f"Donkey ranges (>=5 aa) without a human partner: {donkey_unpaired if donkey_unpaired else 'none'}.",
     f"Human ranges (>=5 aa) without a donkey partner: {human_unpaired if human_unpaired else 'none'}.", "",
     "Method: Biopython PairwiseAligner, global, BLOSUM62, gap open -10, extend -0.5. Regenerate with `uv run python " + str(here.relative_to(here.parents[3])) + "/compare.py`. Pairwise similarity does not by itself establish orthology or function.",
     "", "## Human UniProt features mapped onto the donkey sequence", ""]
for x in feats:
    L.append(f"- {x['type']} {x['note']}: human {x['human']} {x['human_res']} -> donkey {x['donkey']} {x['donkey_res']}; {x['span_identical']} of {x['span_len']} human residues in this span are identical in the aligned donkey sequence ({x['span_paired']} paired; aligned donkey span length {(x['donkey'][-1] or 0) - (x['donkey'][0] or 0) + 1})")
L += ["", f"## Human non-IEA GO annotations ({goa_file.name}, QuickGO download)", ""]
seen = set()
for r in rows:
    key = (r["QUALIFIER"], r["GO TERM"], r["GO EVIDENCE CODE"], r["REFERENCE"])
    if key in seen:
        continue
    seen.add(key)
    L.append(f"- {r['QUALIFIER']} {r['GO TERM']} [{r['GO EVIDENCE CODE']} {r['REFERENCE']}]")
(here / "RESULTS.md").write_text("\n".join(L) + "\n")
print("\n".join(L[:8]))
