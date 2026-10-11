"""Render the dismech<->AIGR alignment audit as a markdown project page."""
import sys

import yaml

_loaded = yaml.safe_load(open(sys.argv[1]))
# The report gained a provenance block; accept either shape.
if isinstance(_loaded, dict):
    PROV = _loaded.get("provenance") or {}
    rep = _loaded.get("entries") or []
else:
    PROV, rep = {}, _loaded
out = sys.argv[2]

# Recorded justifications for flags that are deliberate, keyed (entry, gene) or (entry, None).
NOTES = {
    ("Inborn_Disorder_of_Bile_Acid_Synthesis", None): "Grouping-like entry; genes are carried by its subtypes.",
    ("Triglyceride_Storage_Disease_Type_1", None): "Historical OMIM:190420 phenotype; no gene has been reported (ABHD5 content lives in Dorfman_Chanarin_Disease).",
    ("Vitamin_D-Dependent_Rickets_Type_2B", None): "Genetic basis unknown; HNRNPC is modelled as a mechanism actor, not a causal gene.",
}
# Keyed by gene symbol. Every principal row carrying a module flag must appear here, or
# the run fails: the page claims each such gene has a stated reason, so that claim is
# enforced rather than asserted. A key may name several genes separated by " / ".
MODULE_REASONS = {
    "TRMT10C": "RNase P partners (HSD17B10, PRORP, ELAC2) lack completed reviews.",
    "ANGPTL3": "No LPL / plasma triglyceride clearance module; LPL review still DRAFT.",
    "CTNS": "Lysosomal cystine export is a single step.",
    "SLC26A1": "Epithelial oxalate/sulfate transport has no coherent multi-part module yet; SLC26A1's oxalate role is contested.",
    "SLC26A6": "As SLC26A1; a two-part oxalate-transport module is possible later.",
    "DMP1": "No module contains DMP1 as a part. It is named in the notes of fgf23_klotho_phosphate_homeostasis as regulatory context, which this audit deliberately does not count as membership, and its mechanism is undefined.",
    "SLC10A7": "Single gene with unknown transported substrate.",
    "DNAJC30": "Complex I N-module repair is not assembly; no repair module exists.",
    "LCT": "Brush-border disaccharide digestion: only LCT has a completed review (SI, MGAM, TREH missing).",
    "HNF1A / HNF4A": "Transcription factors whose hyperinsulinism and MODY roles act through many target genes; no beta-cell transcriptional-network module exists yet.",
    "SLC16A1": "Disease mechanism is ectopic beta-cell expression of a transporter whose normal role (lactate/pyruvate transport) belongs to no beta-cell pathway; a monocarboxylate-transport module would not include the disease mechanism.",
    "SIM1": "Transcription factor needed for paraventricular hypothalamic neuron development and function; it acts on, rather than within, the leptin_melanocortin_signaling module, whose parts are the ligand, processing and receptor steps.",
    "MT-TL1 / MT-TQ / MT-TH / MT-TK / MT-TC / MT-TS1 / MT-TS2 / MT-TV / MT-TW / MT-TM": "No mitochondrial translation module exists; in mitochondrial_trna_charging_and_initiator_formylation a tRNA would appear only as a synthetase substrate, which the substrate guidance excludes, and module parts are UniProt proteins.",
    "UCP2": "Causal role disputed (relationship DISPUTED); its transported substrate is itself contested.",
    "AIFM1": "The aligned function is the mitochondrial disulfide relay (CHCHD4 anchoring); no module covers the relay. AIFM1 is a part of apoptotic_execution_phase, whose AIFM1 annoton carries DNA binding, nucleus and positive regulation of apoptotic process: a different AIFM1 activity, and not the encephalomyopathy mechanism.",
    "APOB": "The aligned term is GO:0034379 very-low-density lipoprotein particle assembly, and there is no VLDL-assembly module. APOB is a part of chylomicron_assembly_secretion, whose scope is GO:0034378 chylomicron assembly, and of ldl_receptor_mediated_endocytosis, which is about the receptor taking the particle up. GO:0034378 and GO:0034379 are siblings, not one inside the other, so the hepatic VLDL step is genuinely unmodelled. APOB's other row, the LDL-receptor-binding one, is covered.",
    "NUBPL": "The aligned term is GO:0016226 iron-sulfur cluster assembly. NUBPL is a part of complex_i_assembly_factors, whose scope is GO:0032981 mitochondrial respiratory chain complex I assembly: NUBPL delivers an Fe-S cluster to the assembling complex, and the cluster's own assembly is a different process that no module covers.",
    "NDUFA1": "A limitation of the coverage test rather than a modelling gap, and left flagged rather than waived. The dismech node binds the molecular function GO:0008137 NADH dehydrogenase (ubiquinone) activity, while complex_i_accessory_subunits declares its scope as the biological process GO:0006120 mitochondrial electron transport, NADH to ubiquinone. Those are the same chemistry in two GO aspects, and is_a/part_of ancestry does not cross between molecular function and biological process, so no amount of ontology walking will relate them. The module is the right one.",
}
MODULE_FLAGS = ("NO_MODULE_MEMBERSHIP", "MODULE_NOT_COVERING")
SOFT = MODULE_FLAGS + ("ALIGNED_NONCORE", "ALIGNED_PROPOSED")

lines = [
    "---",
    "title: dismech metabolic disorders aligned with ai-gene-review",
    "maturity: IN_PROGRESS",
    "description: Per-entry check that dismech metabolic disease mechanisms agree with ai-gene-review core functions and modules",
    "species: [human]",
]

from collections import Counter

# Whitelist, so a renamed or new dismech relationship value does not silently become
# principal and inflate the clean count.
PRINCIPAL_RELATIONSHIPS = (None, "CAUSATIVE")
principal = lambda g: g.get("relationship") in PRINCIPAL_RELATIONSHIPS

all_genes = sorted({g["gene"] for e in rep for g in e.get("genes", [])})
lines += [
    "genes: [" + ", ".join(all_genes) + "]",
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
    "ai-gene-review core functions. The audit script (`align_audit.py`), the page generator",
    "(`make_page.py`), the entry list (`scope.yaml`) and the committed report of the run behind this",
    "table (`report.yaml`) are in the `projects/DISMECH_METABOLIC_ALIGNMENT/` directory of the",
    "repository.",
    "",
    "**What \"aligned\" does and does not claim.** Two properties of the test make it a weak check,",
    "and either can turn a row green that a curator would not:",
    "",
    "- The relation is **symmetric** and **unbounded in distance**. A node term counts as aligned",
    "  when either it or the core term is an is_a/part_of ancestor of the other, at any depth. So a",
    "  dismech node bound to something broad aligns with a specific core function, and the reverse,",
    "  and two terms many levels apart still align. The table therefore prints the core term each",
    "  node term matched (`node->core`, or the term alone where the two are identical), so the",
    "  distance behind a match is visible per row. `DMP1 | GO:0005509` (calcium ion binding) is the",
    "  clearest row where the verdict carries little information; reading a row as agreement means",
    "  reading its pair.",
    "- Module **membership** is not module **coverage**. Membership says the gene is a part of some",
    "  module; coverage says a module is about the function the row aligned on, which is a different",
    "  and stronger claim. They are flagged separately: `NO_MODULE_MEMBERSHIP` means no module",
    "  contains the gene, and `MODULE_NOT_COVERING` means one does but none of that gene's annotons",
    "  in any of them carries a GO term related to the aligned terms. Such a module is marked",
    "  `(not covering)` in the Modules column. AIFM1 is the row this flag exists to catch: it sits",
    "  in `apoptotic_execution_phase`, whose AIFM1 annoton carries DNA binding, nucleus and",
    "  positive regulation of apoptotic process, while the aligned function is the mitochondrial",
    "  disulfide relay. No module covers the relay.",
    "",
    "Coverage reads the module's declared `concepts`, at module level and per node, as well as its",
    "annotons' terms: a module states its scope as processes while its annotons carry the molecular",
    "functions of individual parts, so annotons alone miss what the module is about. One limitation",
    "survives that and is left visible rather than waived: is_a/part_of ancestry does not cross",
    "between molecular function and biological process, so a dismech node bound to an activity and",
    "a module scoped to the corresponding process cannot be related, however plainly they are the",
    "same chemistry. NDUFA1 is that row.",
    "",
    "Membership is read from the module structure (`parts[].node.annotons[]`, following the",
    "participant whichever selector it uses, including a `FAMILY` participant's",
    "`representative_members` and a protein complex's active units and components), and following",
    "nested parts and variant sets, so a gene named only in a module's notes or evidence does not",
    "count as a part. Reading the files as text instead finds 3,707 accessions against 3,659 real",
    "parts; the 48 extra are mentions rather than parts.",
    "",
    "Flags: `UNTYPED`/`NO_ORIGIN` (genetic record lacks relationship type / variant origin),",
    "`NO_GO_ON_GENE_NODES` (no node naming the gene carries a GO term), `NO_AIGR_REVIEW`,",
    "`AIGR_NOT_COMPLETE`, `NO_CORE_FUNCTION_TERMS` (the review has no core-function GO term to",
    "compare against), `NO_GO_ALIGNMENT` (no node term matches a core function, an annotation the",
    "review keeps, or a term it proposes), `ALIGNED_NONCORE` (node terms match only annotations the",
    "review keeps as non-core), `ALIGNED_PROPOSED` (node terms match only terms the review proposes",
    "as NEW, which are not yet annotations), `NO_MODULE_MEMBERSHIP`, `MODULE_NOT_COVERING`. The last",
    "four are informational, not defects.",
    "",
]
if PROV:
    lines += [
        "**Provenance of this run.** The table is generated, so it is only as current as the inputs it",
        "was generated from, and those inputs live in two repositories.",
        "",
        f"- run date: `{PROV.get('run_date') or 'unrecorded'}`",
        f"- dismech revision: `{PROV.get('dismech_revision') or 'unrecorded'}`"
        + (f" ({PROV['dismech_describe']})" if PROV.get("dismech_describe") else ""),
        f"- ai-gene-review revision: `{PROV.get('aigr_revision') or 'unrecorded'}`"
        + (f" (branch `{PROV['aigr_branch']}`)" if PROV.get("aigr_branch") else ""),
        f"- GO release: `{PROV.get('go_version') or 'unrecorded'}`, adapter `{PROV.get('go_adapter') or 'unrecorded'}`",
        "",
        "Many of the gene reviews and modules this table asserts `COMPLETE` for are added by the ten",
        "themed PRs split out of #4690, so on a branch without those merged the audit cannot be",
        "re-run to reproduce these rows. `report.yaml` is committed as the record of the run above.",
        "",
    ]


def aligned_cell(g):
    """Node term with the core term it matched, so an unbounded match is visible."""
    pairs = g.get("aligned_pairs") or {}
    terms = g.get("aligned_terms") or []
    if not terms:
        return "-"
    cells = []
    for t in terms:
        c = pairs.get(t)
        if isinstance(c, list):
            c = c[0]
        cells.append(t if (c is None or c == t) else f"{t}&rarr;{c}")
    return " ".join(cells)


def modules_cell(g):
    """Modules, marking those whose own GO terms do not cover the aligned function."""
    mods = g.get("modules") or []
    if not mods:
        return "-"
    cov = g.get("covering_modules")
    if cov is None:
        return " ".join(mods)
    return " ".join(m if m in cov else f"{m} (not covering)" for m in mods)


c = Counter(f for e in rep for g in e.get("genes", []) if principal(g) for f in g["flags"])
n_rows = sum(1 for e in rep for g in e.get("genes", []) if principal(g))
n_clean = sum(1 for e in rep for g in e.get("genes", [])
              if principal(g) and not [f for f in g["flags"] if f not in SOFT])
lines += [
    f"**Summary.** {len(rep)} entries; {n_rows} principal gene rows (causative and untyped);",
    f"{n_clean} carry no flag other than a module flag, `ALIGNED_NONCORE` or `ALIGNED_PROPOSED`."
    + (" Flag counts on principal rows: " + ", ".join(f"`{k}` {v}" for k, v in sorted(c.items())) + "."
       if c else " No principal row carries a flag."),
    "",
    "Polygenic entries (Type I diabetes) and modifier/susceptibility genes are",
    "listed but were not required to align: their genes are risk loci or modifiers, not the",
    "normal-function owners of a single pathway step.",
    "",
    "| Entry | Gene | Relationship | AIGR | Aligned GO terms (node&rarr;core) | Modules | Flags |",
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
            f"{aligned_cell(g)} | {modules_cell(g)} | {flags} |"
        )
lines += [
    "",
    "## Notes on remaining flags",
    "",
    "- Every causative gene row is free of flags other than the two module flags. The other flags",
    "  fall on modifier, susceptibility and disputed genes, none of which were required to align.",
    "- **MELAS mtDNA genes**: MT-ND1, MT-ND5 and MT-ND6 have reviews and are parts of",
    "  mitochondrial_complex_i_core, aligning with the dismech complex I node (NADH:ubiquinone",
    "  oxidoreductase activity, DECREASED). The ten mt-tRNA genes (MT-TL1, MT-TQ, MT-TH, MT-TK,",
    "  MT-TC, MT-TS1, MT-TS2, MT-TV, MT-TW, MT-TM) have ncRNA reviews (RNAcentral ids) whose core",
    "  function, triplet codon-amino acid adaptor activity in mitochondrial translation, matches",
    "  the dismech translation-defect nodes.",
    "- **UCP2** (DISPUTED): dismech binds regulation of insulin secretion (GO:0050796), which",
    "  is the parent of a UCP2 annotation the review keeps as non-core (GO:0061179), so the row",
    "  is `ALIGNED_NONCORE`. dismech deliberately binds no UCP2",
    "  activity, because its causal role in hyperinsulinism and its transported substrate",
    "  are both disputed.",
    "- **TMEM251** is the dismech/HGNC-build label for the gene now named LYSET; it is matched to",
    "  the LYSET review.",
    "- **Type I diabetes risk loci** (PTPN22, IL2RA, CTLA4, IFIH1, BACH2, TNFAIP3, EGR2, IRF4, IKZF1,",
    "  TYK2) are SUSCEPTIBILITY records with no single pathway step; several ai-gene-review entries",
    "  for them are still drafts from other projects.",
]
lines += ["", "## Causative genes without a covering module, and why", ""]
for k, v in MODULE_REASONS.items():
    lines.append(f"- **{k}**: {v}")

# Enforce the claim above: every principal row carrying a module flag must have a reason.
covered = {g.strip() for key in MODULE_REASONS for g in key.split("/")}
missing = sorted({g["gene"] for e in rep for g in e.get("genes", [])
                  if principal(g) and [f for f in g["flags"] if f in MODULE_FLAGS]} - covered)
if missing:
    sys.exit("MODULE_REASONS has no entry for principal rows flagged "
             f"{'/'.join(MODULE_FLAGS)}: {', '.join(missing)}")
unused = sorted(covered - {g["gene"] for e in rep for g in e.get("genes", [])})
if unused:
    print("warning: MODULE_REASONS names genes absent from the report:", ", ".join(unused))

open(out, "w").write("\n".join(lines) + "\n")
print("wrote", out, n_rows, n_clean)
