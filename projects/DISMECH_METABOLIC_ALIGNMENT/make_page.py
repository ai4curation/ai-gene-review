"""Render the dismech<->AIGR alignment audit as a markdown project page."""
import sys
import yaml

rep = yaml.safe_load(open(sys.argv[1]))
out = sys.argv[2]

# Recorded justifications for flags that are deliberate, keyed (entry, gene) or (entry, None).
NOTES = {
    ("Inborn_Disorder_of_Bile_Acid_Synthesis", None): "Grouping-like entry; genes are carried by its subtypes.",
    ("Triglyceride_Storage_Disease_Type_1", None): "Historical OMIM:190420 phenotype; no gene has been reported (ABHD5 content lives in Dorfman_Chanarin_Disease).",
    ("Vitamin_D-Dependent_Rickets_Type_2B", None): "Genetic basis unknown; HNRNPC is modelled as a mechanism actor, not a causal gene.",
}
FLAG_NOTES = {
    "NO_MODULE": "no module (see reasons below)",
}
MODULE_REASONS = {
    "TRMT10C": "RNase P partners (HSD17B10, PRORP, ELAC2) lack completed reviews.",
    "ANGPTL3": "No LPL / plasma triglyceride clearance module; LPL review still DRAFT.",
    "CTNS": "Lysosomal cystine export is a single step.",
    "SLC26A1": "Epithelial oxalate/sulfate transport has no coherent multi-part module yet; SLC26A1's oxalate role is contested.",
    "SLC26A6": "As SLC26A1; a two-part oxalate-transport module is possible later.",
    "DMP1": "Recorded as regulatory context in fgf23_klotho_phosphate_homeostasis; mechanism undefined.",
    "SLC10A7": "Single gene with unknown transported substrate.",
    "DNAJC30": "Complex I N-module repair is not assembly; no repair module exists.",
    "LCT": "Brush-border disaccharide digestion: only LCT has a completed review (SI, MGAM, TREH missing).",
    "HNF1A / HNF4A": "Transcription factors whose hyperinsulinism and MODY roles act through many target genes; no beta-cell transcriptional-network module exists yet.",
    "SLC16A1": "Disease mechanism is ectopic beta-cell expression of a transporter whose normal role (lactate/pyruvate transport) belongs to no beta-cell pathway; a monocarboxylate-transport module would not include the disease mechanism.",
    "SIM1": "Transcription factor needed for paraventricular hypothalamic neuron development and function; it acts on, rather than within, the leptin_melanocortin_signaling module, whose parts are the ligand, processing and receptor steps.",
    "UCP2": "Causal role disputed (relationship DISPUTED); its transported substrate is itself contested.",
}

lines = [
    "---",
    "title: dismech metabolic disorders aligned with ai-gene-review",
    "maturity: IN_PROGRESS",
    "description: Per-entry check that dismech metabolic disease mechanisms agree with ai-gene-review core functions and modules",
    "species: [human]",
    "---",
    "",
    "# dismech metabolic disorders aligned with ai-gene-review",
    "",
    "This page records, for every dismech metabolic disorder in scope, whether the causal gene's",
    "dysfunction as modelled in the dismech pathograph agrees with the gene's normal function in its",
    "ai-gene-review review, and whether the gene sits in an ai-gene-review module.",
    "",
    "**Scope.** dismech entries with Harrison's chapter `ENDOCRINOLOGY_METABOLISM` or a metabolic",
    "`category`, excluding primarily endocrine-gland, autoimmune, complex, neoplastic and gynecologic",
    "conditions, plus two entries created in this work (Mitchell syndrome, SLC26A1-related hypersulfaturia).",
    "",
    "**Method.** For each gene bound in an entry's `genetic` records, the GO molecular functions and",
    "biological processes on the pathograph nodes naming that gene are compared with the gene's",
    "ai-gene-review core functions. A match is the same term or one related through is_a/part_of",
    "ancestry. Modules are matched by UniProt accession. The audit script, page generator and entry",
    "list are in [DISMECH_METABOLIC_ALIGNMENT/](DISMECH_METABOLIC_ALIGNMENT/).",
    "",
    "Flags: `UNTYPED`/`NO_ORIGIN` (genetic record lacks relationship type / variant origin),",
    "`NO_GO_ON_GENE_NODES` (no node naming the gene carries a GO term), `NO_AIGR_REVIEW`,",
    "`AIGR_NOT_COMPLETE`, `NO_GO_ALIGNMENT` (no node term matches a core function), `NO_MODULE`.",
    "",
]
from collections import Counter
principal = lambda g: g.get("relationship") not in ("MODIFIER", "SUSCEPTIBILITY", "DISPUTED", "RISK_FACTOR")
c = Counter(f for e in rep for g in e.get("genes", []) if principal(g) for f in g["flags"])
n_rows = sum(1 for e in rep for g in e.get("genes", []) if principal(g))
n_clean = sum(1 for e in rep for g in e.get("genes", []) if principal(g) and not [f for f in g["flags"] if f != "NO_MODULE"])
lines += [
    f"**Summary.** {len(rep)} entries; {n_rows} principal gene rows (causative and untyped);",
    f"{n_clean} have no flag other than `NO_MODULE`. Flag counts on principal rows: "
    + ", ".join(f"`{k}` {v}" for k, v in sorted(c.items())) + ".",
    "",
    "Polygenic entries (Type I diabetes, the MELAS mtDNA genes) and modifier/susceptibility genes are",
    "listed but were not required to align: their genes are risk loci or mtDNA tRNAs, not the",
    "normal-function owners of a single pathway step.",
    "",
    "| Entry | Gene | Relationship | AIGR | Aligned GO terms | Modules | Flags |",
    "|---|---|---|---|---|---|---|",
]
for e in rep:
    if not e.get("genes"):
        lines.append(f"| {e['entry']} | - | - | - | - | - | {e.get('problem','')}: {NOTES.get((e['entry'], None), '')} |")
        continue
    for g in e["genes"]:
        flags = ", ".join(g["flags"]) or "ok"
        lines.append(
            f"| {e['entry']} | {g['gene']} | {g.get('relationship') or '-'} | {g.get('aigr_status') or '-'} | "
            f"{' '.join(g.get('aligned_terms') or []) or '-'} | {' '.join(g.get('modules') or []) or '-'} | {flags} |"
        )
lines += [
    "",
    "## Notes on remaining flags",
    "",
    "- Every causative nuclear-gene row is free of flags other than `NO_MODULE`. The other flags fall on",
    "  the MELAS mtDNA genes and on modifier, susceptibility and disputed genes, none of which were",
    "  required to align.",
    "- **MELAS mtDNA genes** (MT-TL1, MT-ND1/5/6 and the other tRNA genes): ai-gene-review has no",
    "  reviews for mitochondrially encoded tRNA or complex I subunit genes, and the dismech record",
    "  types them by relationship but not by variant origin (heteroplasmic mtDNA variants fit",
    "  neither GERMLINE nor SOMATIC cleanly).",
    "- **TMEM251** is the dismech/HGNC-build label for the gene now named LYSET; it is matched to",
    "  the LYSET review.",
    "- **Type I diabetes risk loci** (PTPN22, IL2RA, CTLA4, IFIH1, BACH2, TNFAIP3, EGR2, IRF4, IKZF1,",
    "  TYK2) are SUSCEPTIBILITY records with no single pathway step; several ai-gene-review entries",
    "  for them are still drafts from other projects.",
]
lines += ["", "## Causative genes without a module, and why", ""]
for k, v in MODULE_REASONS.items():
    lines.append(f"- **{k}**: {v}")
open(out, "w").write("\n".join(lines) + "\n")
print("wrote", out, n_rows, n_clean)
