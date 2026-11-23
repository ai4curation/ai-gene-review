"""Re-review: place the benchmark horse BCAT2 model (A0A9L0TSN4) among all horse
BCAT2 gene models (UniProt + Ensembl ENSECAG00000011310 translations) and
reviewed mammalian BCAT2 orthologs (human, mouse, rat, cow; all PTHR11825:SF39).

Questions:
  1. Where does the benchmark model begin relative to the conserved mammalian
     N terminus (human mitochondrial transit peptide 1-27)?
  2. Are the PLP Schiff-base lysine (human K229), the CXXC motif (human
     C342/C345 in precursor numbering; C315/C318 in mature numbering of
     PMID:17050531) and the curated substrate-binding residues retained?
  3. Is the N-terminal extension found in any reviewed ortholog?

Inputs (all in this folder or the repo):
  ../BCAT2-uniprot.txt                               horse A0A9L0TSN4
  ../../../human/BCAT2/BCAT2-uniprot.txt             human O15382
  horse_BCAT2_uniprot_models-rereview.fasta          UniProt horse BCAT2 entries
  horse_BCAT2_ensembl_translations-rereview.fasta    Ensembl translations of ENSECAG00000011310
  mammal_BCAT2_orthologs-rereview.fasta              rat, mouse, cow BCAT2 (Swiss-Prot)

Writes RESULTS-rereview.md and results-rereview.json.
Run from repo root:
  uv run python genes/HORSE/BCAT2/BCAT2-bioinformatics/compare_models_rereview.py
"""

from pathlib import Path
import json

from Bio import Align, SeqIO, SwissProt

here = Path(__file__).resolve().parent
with (here.parent / "BCAT2-uniprot.txt").open() as f:
    bench = SwissProt.read(f)
with (here.parents[2] / "human" / "BCAT2" / "BCAT2-uniprot.txt").open() as f:
    human = SwissProt.read(f)
H = human.sequence


def load(name):
    out = {}
    for r in SeqIO.parse(here / name, "fasta"):
        key = r.id.split("|")[1] if "|" in r.id else r.id
        out[key] = str(r.seq)
    return out


uniprot_models = load("horse_BCAT2_uniprot_models-rereview.fasta")
ensembl_models = load("horse_BCAT2_ensembl_translations-rereview.fasta")
orthologs = load("mammal_BCAT2_orthologs-rereview.fasta")
assert uniprot_models["A0A9L0TSN4"] == bench.sequence

aligner = Align.PairwiseAligner(
    mode="global",
    match_score=2,
    mismatch_score=-1,
    open_gap_score=-10,
    extend_gap_score=-0.5,
)
aligner.end_gap_score = 0

# human positions (1-based, precursor numbering) of checked residues
sites = {
    "PLP Schiff-base Lys (MOD_RES 229)": 229,
    "CXXC Cys1 (mature C315)": 315 + 27,
    "CXXC Cys2 (mature C318)": 318 + 27,
}
for ft in human.features:
    if ft.type == "BINDING":
        p = int(ft.location.start) + 1
        sites[f"substrate BINDING {p}"] = p
for name, p in sites.items():
    assert 1 <= p <= len(H), name


def compare(seq):
    al = aligner.align(H, seq)[0]
    m = {}
    for (s, e), (t, _u) in zip(*al.aligned):
        for k in range(e - s):
            m[int(s + k)] = int(t + k)
    paired = len(m)
    ident = sum(H[i] == seq[j] for i, j in m.items())
    first_h = min(m)
    first_t = m[first_h]
    # residues of target before the residue aligned to human Met1
    h1 = m.get(0)
    site_res = {
        name: (seq[m[p - 1]] if (p - 1) in m else "-") + f"/{H[p - 1]}"
        for name, p in sites.items()
    }
    missing_h = [i + 1 for i in range(len(H)) if i not in m]
    return {
        "length": len(seq),
        "paired": paired,
        "identity_pct": round(100 * ident / paired, 2),
        "human_coverage_pct": round(100 * paired / len(H), 2),
        "target_pos_of_human_Met1": None if h1 is None else h1 + 1,
        "n_terminal_extension_residues": first_t if first_h == 0 else None,
        "first_human_pos_aligned": first_h + 1,
        "human_positions_unaligned_count": len(missing_h),
        "human_unaligned_ranges": ranges(missing_h),
        "sites_target_over_human": site_res,
        "starts_with": seq[:30],
    }


def ranges(xs):
    out = []
    for x in xs:
        if out and x == out[-1][1] + 1:
            out[-1][1] = x
        else:
            out.append([x, x])
    return [f"{a}-{b}" if a != b else str(a) for a, b in out]


results = {"human": "O15382", "human_length": len(H), "models": {}}
for group, d in [
    ("uniprot_horse", uniprot_models),
    ("ensembl_horse", ensembl_models),
    ("reviewed_ortholog", orthologs),
]:
    for k, s in d.items():
        r = compare(s)
        r["group"] = group
        results["models"][k] = r

ext = bench.sequence[:59]
results["benchmark_extension"] = {
    "sequence": ext,
    "gly_count": ext.count("G"),
    "arg_count": ext.count("R"),
    "pro_count": ext.count("P"),
    "acidic_count": ext.count("D") + ext.count("E"),
    "found_in_reviewed_orthologs": [k for k, s in orthologs.items() if ext[:20] in s],
    "found_in_horse_models": [
        k for d in (uniprot_models, ensembl_models) for k, s in d.items() if ext[:20] in s
    ],
}
core = bench.sequence[59:]
results["benchmark_core_from_Met60"] = {
    "length": len(core),
    "identical_to_any_horse_model": [
        k for d in (uniprot_models, ensembl_models) for k, s in d.items() if s == core
    ],
        "C_terminal_12_benchmark": core[-12:],
    "C_terminal_12_orthologs": {k: s[-12:] for k, s in {"O15382": H, **orthologs}.items()},
}
(here / "results-rereview.json").write_text(json.dumps(results, indent=2) + "\n")

lines = [
    "# BCAT2 (horse A0A9L0TSN4): gene-model re-review",
    "",
    "Global alignments to human O15382 (392 aa; free end gaps; match 2, mismatch -1,",
    "open -10, extend -0.5). Site columns give target/human residue. Reproduce with",
    "`uv run python genes/HORSE/BCAT2/BCAT2-bioinformatics/compare_models_rereview.py`.",
    "",
    "| model | group | length | identity % | human coverage % | N-terminal residues before human Met1 | human positions unaligned |",
    "|---|---|---|---|---|---|---|",
]
for k, r in results["models"].items():
    lines.append(
        f"| {k} | {r['group']} | {r['length']} | {r['identity_pct']} | {r['human_coverage_pct']} | "
        f"{r['n_terminal_extension_residues']} | {', '.join(r['human_unaligned_ranges']) or 'none'} |"
    )
lines += ["", "## Conserved catalytic and substrate residues (target/human)", ""]
names = list(sites)
lines.append("| model | " + " | ".join(names) + " |")
lines.append("|---|" + "---|" * len(names))
for k, r in results["models"].items():
    lines.append(f"| {k} | " + " | ".join(r["sites_target_over_human"][n] for n in names) + " |")
e = results["benchmark_extension"]
lines += [
    "",
    "## Benchmark N-terminal extension",
    "",
    f"A0A9L0TSN4 residues 1-59 (upstream of Met60): `{e['sequence']}` "
    f"(Gly {e['gly_count']}, Arg {e['arg_count']}, Pro {e['pro_count']}, Asp+Glu {e['acidic_count']}).",
    f"First 20 residues found in reviewed orthologs: {e['found_in_reviewed_orthologs'] or 'none'}.",
    f"First 20 residues found in horse models: {', '.join(e['found_in_horse_models'])}.",
    "",
]
c = results["benchmark_core_from_Met60"]
lines += [
    "## Benchmark body from Met60",
    "",
    f"A0A9L0TSN4 residues 60-452 ({c['length']} aa) begin at the Met aligned to human Met1. "
    f"Identical horse models: {c['identical_to_any_horse_model'] or 'none'}. "
    f"C-terminal 12 residues: benchmark `{c['C_terminal_12_benchmark']}`; orthologs "
    + ", ".join(f"{k} `{v}`" for k, v in c["C_terminal_12_orthologs"].items())
    + ".",
    "",
]
(here / "RESULTS-rereview.md").write_text("\n".join(lines))
print("\n".join(lines))
