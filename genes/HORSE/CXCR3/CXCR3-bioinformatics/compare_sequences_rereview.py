"""Re-review: place horse CXCR3 (A0A9L0T1D1) among CXCR3 orthologs and paralogous
chemokine receptors, compare it with the other horse model of the same Ensembl gene
(F6U4S6), and check receptor motifs mapped from human P49682.

Inputs are UniProt flat files / FASTA cached in this folder (fetched from rest.uniprot.org
on 2026-10-20). Writes RESULTS-rereview.md and results-rereview.json.

Run from repo root:
  uv run --with biopython python genes/HORSE/CXCR3/CXCR3-bioinformatics/compare_sequences_rereview.py
"""

from pathlib import Path
import json

from Bio import Align, SeqIO, SwissProt
from Bio.Phylo import write as phylo_write
from Bio.Phylo.TreeConstruction import DistanceMatrix, DistanceTreeConstructor

here = Path(__file__).resolve().parent
genes = here.parents[1]

flat = {
    "A0A9L0T1D1": genes / "CXCR3" / "CXCR3-uniprot.txt",
    "P49682": genes.parent / "human" / "CXCR3" / "CXCR3-uniprot.txt",
}
for acc in ["F6U4S6", "O88410", "Q5KSK8", "Q5MD61", "P25024", "P25025", "P61073",
            "P51681", "E9QJ73"]:
    flat[acc] = here / f"{acc}-uniprot-rereview.txt"

recs = {}
for acc, p in flat.items():
    with p.open() as f:
        r = SwissProt.read(f)
    panther = [x[1] for x in r.cross_references if x[0] == "PANTHER" and ":SF" in x[1]]
    recs[acc] = {"name": r.entry_name, "seq": r.sequence, "panther_sf": panther}

iso = {rec.id.split("|")[1]: str(rec.seq)
       for rec in SeqIO.parse(here / "P49682-isoforms-rereview.fasta", "fasta")}
recs["P49682-2"] = {"name": "CXCR3_HUMAN isoform 2 (CXCR3-B)", "seq": iso["P49682-2"],
                    "panther_sf": recs["P49682"]["panther_sf"]}

aligner = Align.PairwiseAligner()
aligner.substitution_matrix = Align.substitution_matrices.load("BLOSUM62")
aligner.mode = "global"
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5


def compare(a: str, b: str) -> dict:
    aln = aligner.align(recs[a]["seq"], recs[b]["seq"])[0]
    x, y = str(aln[0]), str(aln[1])
    pairs = [(u, v) for u, v in zip(x, y) if u != "-" and v != "-"]
    ident = sum(u == v for u, v in pairs)
    return {"a": a, "b": b, "len_a": len(recs[a]["seq"]), "len_b": len(recs[b]["seq"]),
            "paired": len(pairs), "identical": ident,
            "identity": round(ident / len(pairs), 4), "x": x, "y": y}


def map_pos(a: str, b: str, positions: list[int]) -> dict:
    """Map 1-based positions in b onto a through the global alignment."""
    c = compare(a, b)
    out, pa, pb = {}, 0, 0
    for u, v in zip(c["x"], c["y"]):
        if u != "-":
            pa += 1
        if v != "-":
            pb += 1
        if v != "-" and pb in positions:
            out[pb] = {"ref_res": v, "target_pos": pa if u != "-" else None,
                       "target_res": u if u != "-" else None}
    return out


target = "A0A9L0T1D1"
others = [k for k in recs if k != target]
pairwise = []
for o in others:
    c = compare(target, o)
    pairwise.append({k: c[k] for k in ("b", "len_a", "len_b", "paired", "identical",
                                       "identity")} | {"name": recs[o]["name"],
                                                       "panther_sf": recs[o]["panther_sf"]})
pairwise.sort(key=lambda d: -d["identity"])

# Human P49682 features: sulfotyrosines Y27/Y29 (ECO:0000269), N-glycosylation N22/N32,
# disulfide C124-C203, and the DRY motif at the end of TM3.
human = recs["P49682"]["seq"]
dry = human.find("DRY") + 1
sites = [22, 27, 29, 32, 124, 203, dry, dry + 1, dry + 2]
site_map = map_pos(target, "P49682", sites)

# Horse F6U4S6 vs benchmark model
model_cmp = compare(target, "F6U4S6")
ext = len(recs["F6U4S6"]["seq"]) - len(recs[target]["seq"])
f6_suffix_match = recs["F6U4S6"]["seq"].endswith(recs[target]["seq"][7:])
human_b_cmp = compare("F6U4S6", "P49682-2")
nterm_ext = recs["F6U4S6"]["seq"][:ext + 7]
human_b_ext = recs["P49682-2"]["seq"][:52]
ext_aln = aligner.align(nterm_ext, human_b_ext)[0]
ex, ey = str(ext_aln[0]), str(ext_aln[1])
ext_pairs = [(u, v) for u, v in zip(ex, ey) if u != "-" and v != "-"]
ext_ident = sum(u == v for u, v in ext_pairs)

# Distance tree (1 - identity), NJ; full-length receptors only (exclude horse F6U4S6 and
# human isoform 2 which duplicate other entries).
tree_ids = [k for k in recs if k not in ("F6U4S6", "P49682-2")]
mat = []
for i, a in enumerate(tree_ids):
    row = []
    for b in tree_ids[: i + 1]:
        row.append(0.0 if a == b else 1 - compare(a, b)["identity"])
    mat.append(row)
names = [f"{k}_{recs[k]['name']}" for k in tree_ids]
dm = DistanceMatrix(names, mat)
tree = DistanceTreeConstructor().nj(dm)
tree.root_with_outgroup(f"P61073_{recs['P61073']['name']}")
phylo_write(tree, here / "rereview_tree.nwk", "newick")

# Sister of horse in the NJ tree
horse_clade = next(c for c in tree.get_terminals() if c.name.startswith(target))
parent = tree.get_path(horse_clade)[-2] if len(tree.get_path(horse_clade)) > 1 else tree.root
sisters = [t.name for t in parent.get_terminals() if t.name != horse_clade.name]

results = {
    "target": target,
    "target_length": len(recs[target]["seq"]),
    "target_panther_sf": recs[target]["panther_sf"],
    "pairwise_vs_target": pairwise,
    "human_sites_mapped_to_target": {str(k): v for k, v in site_map.items()},
    "human_dry_position": dry,
    "F6U4S6_vs_target": {"identity": model_cmp["identity"], "paired": model_cmp["paired"],
                         "extra_N_terminal_residues": ext,
                         "F6U4S6_starts_with_Met": recs["F6U4S6"]["seq"].startswith("M"),
                         "F6U4S6_ends_with_target_from_res8": f6_suffix_match},
    "F6U4S6_Nterm_vs_human_CXCR3B_Nterm": {"paired": len(ext_pairs), "identical": ext_ident,
                                          "identity": round(ext_ident / len(ext_pairs), 4)},
    "F6U4S6_vs_P49682-2_identity": human_b_cmp["identity"],
    "nj_tree_newick": "rereview_tree.nwk",
    "nj_sister_group_of_target": sisters,
}
(here / "results-rereview.json").write_text(json.dumps(results, indent=2))

lines = ["# CXCR3 (horse A0A9L0T1D1) re-review sequence analysis", "",
         "Generated by `compare_sequences_rereview.py` (BLOSUM62 global alignments, NJ tree on "
         "1 - identity). UniProt records fetched 2026-10-20.", "",
         f"Target A0A9L0T1D1 length {len(recs[target]['seq'])} aa; PANTHER subfamily "
         f"{', '.join(recs[target]['panther_sf'])}.", "",
         "## Pairwise identity of A0A9L0T1D1 to comparators", "",
         "| accession | entry | length | PANTHER subfamily | identity | paired |",
         "|---|---|---|---|---|---|"]
for d in pairwise:
    lines.append(f"| {d['b']} | {d['name']} | {d['len_b']} | {', '.join(d['panther_sf'])} | "
                 f"{d['identity']:.3f} | {d['paired']} |")
lines += ["", "## Human P49682 sites mapped to horse A0A9L0T1D1", "",
          "| human pos | human res | horse pos | horse res |", "|---|---|---|---|"]
for k, v in sorted(site_map.items()):
    lines.append(f"| {k} | {v['ref_res']} | {v['target_pos']} | {v['target_res']} |")
lines += ["", f"Human DRY motif starts at position {dry}.", "",
          "## Other horse gene model (same Ensembl gene ENSECAG00000023587)", "",
          f"F6U4S6 ({len(recs['F6U4S6']['seq'])} aa) vs A0A9L0T1D1: identity "
          f"{model_cmp['identity']:.3f} over {model_cmp['paired']} paired residues; F6U4S6 has "
          f"{ext} extra N-terminal residues, starts with Met: "
          f"{recs['F6U4S6']['seq'].startswith('M')}; F6U4S6 ends with the A0A9L0T1D1 sequence "
          f"from residue 8 onward: {f6_suffix_match}.",
          "",
          f"F6U4S6 N-terminal segment vs human CXCR3-B (P49682-2) N-terminal 52 residues: "
          f"identity {ext_ident / len(ext_pairs):.3f} over {len(ext_pairs)} paired residues.",
          "",
          "## NJ tree", "",
          f"Sister group of A0A9L0T1D1 in the NJ tree: {', '.join(sisters)}.", "",
          "Newick: `rereview_tree.nwk`. A distance tree on a handful of sequences is only a "
          "sanity check of the PANTHER SF671 placement, not an independent phylogeny.", ""]
(here / "RESULTS-rereview.md").write_text("\n".join(lines))
print("\n".join(lines))
