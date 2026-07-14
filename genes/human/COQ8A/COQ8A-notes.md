# COQ8A (ADCK3 / CABC1) — gene review notes

UniProt: Q8NI60 (COQ8A_HUMAN). HGNC:16812. Synonyms: ADCK3, CABC1, COQ8, ORFNames PP265.
647 aa precursor; mitochondrial transit peptide 1–162; mature chain 163–647.

## Summary of biology

COQ8A is a mitochondrial member of the **ancient UbiB atypical protein-kinase-like (PKL)
family** required for biosynthesis of **coenzyme Q (ubiquinone, CoQ10)**. It is the human
co-ortholog (with COQ8B/ADCK4) of yeast Coq8p. It localizes to the **matrix face of the
inner mitochondrial membrane** as a single-pass membrane protein, and its mature form is
N-terminally truncated by ~162 residues.

### The atypical-kinase vs ATPase question (central nuance)

- COQ8A **adopts a protein-kinase-like fold** but carries UbiB-specific features that
  **suppress canonical protein-kinase activity**: a KxGQ-domain / N-terminal extension that
  occludes the substrate-binding cleft, and an alanine-rich (A-rich, AAAS) loop replacing
  the canonical glycine-rich loop, which limits ATP binding and gives an unusual selectivity
  for **ADP over ATP** [PMID:25498144 "unusual selectivity for binding ADP over ATP"].
- The Stefely 2016 paper explicitly demonstrated that COQ8 **lacks canonical protein kinase
  activity in trans**; instead it **has ATPase activity and interacts with lipid CoQ
  intermediates** [PMID:27499294 abstract "Instead, COQ8 has ATPase activity" / "interacts
  with lipid CoQ intermediates"]. The ATPase activity is enhanced by the KxGQ motif
  [PMID:27499294 "Coq8p ATPase activity is enhanced by the UbiB-specific KxGQ motif"] and the
  K134H (KxGQ) mutation that abolishes ATPase eliminates CoQ production in vivo
  [PMID:27499294 "the K134H mutation eliminates CoQ production in vivo"], tying the ATPase/
  small-molecule-kinase activity (not autophosphorylation) to the endogenous function.
- Only an engineered A-to-G (A339G) mutation of the A-rich loop flips coenzyme selectivity
  toward ATP and enables **autophosphorylation in vitro**, and that same mutation **inhibits
  CoQ biosynthesis in vivo** [PMID:25498144 "A single alanine-to-glycine mutation of this loop
  flips" ... "inhibits coenzyme Q biosynthesis in vivo"]. So canonical kinase-type
  phosphotransfer is antithetical to the native CoQ role.
- GOA carries an explicit **NOT** annotation for GO:0004672 protein kinase activity and NOT
  for GO:0006468 protein phosphorylation (both IDA, PMID:27499294) — consistent with the
  "lacks canonical protein kinase activity in trans" finding.

Consequence for MF curation: the best-supported molecular functions are **ATP binding
(GO:0005524)**, **ADP binding (GO:0043531, IDA)**, and an **ATPase / ATP hydrolysis activity
(GO:0016887)** — not canonical protein-serine/threonine-kinase activity. The generic
"kinase activity" (GO:0016301) IDA annotations reflect the measured ATPase ("water kinase")
and are defensible but non-core / general.

### Role in CoQ biosynthesis / complex Q (COQ synthome)

COQ8A stabilizes the multi-subunit **COQ enzyme complex ("complex Q" / COQ synthome)** that
carries out CoQ head-group modification steps. UniProt: "Interacts with the multi-subunit COQ
enzyme complex, composed of at least COQ3, COQ4, COQ5, COQ6, COQ7 and COQ9"
[file:human/COQ8A/COQ8A-uniprot.txt]. Loss of COQ8A/Coq8p causes specific deficiency of complex
Q subunits [PMID:27499294 "Coq8p and COQ8A specifically maintain complex Q"], and its
active-site mutations remodel the complex. The in-vitro reconstituted metabolon paper shows
COQ8 "increases and streamlines coenzyme Q production" [PMID:38425362].

Direct experimental interactors captured in GOA include COQ9 (O75208) and the COQ metabolon
(via PMID:27499294 / PMID:27499296 mito-interactome mapping). Many other GOA "protein binding"
IPI entries come from high-throughput binary/Y2H interactome screens (HuRI, BioPlex-type,
Luck 2020, Vo 2016, Sahni 2015, Huttlin) and are non-core.

### Disease

Biallelic COQ8A variants cause **primary coenzyme Q10 deficiency-4 (COQ10D4, MIM:612016)**,
i.e. **autosomal-recessive cerebellar ataxia (ARCA2 / SCAR9)** with cerebellar atrophy,
exercise intolerance, and variable seizures [file:human/COQ8A/COQ8A-uniprot.txt DISEASE block;
PMID:18319072; PMID:18319074; PMID:27499294 mouse Coq8a−/− recapitulates ARCA2].

### Localization / topology

- Mitochondrion membrane (inner), single-pass; matrix-facing catalytic domain
  [file:human/COQ8A/COQ8A-uniprot.txt "Mitochondrion membrane" / "Single-pass membrane protein";
  PMID:27499294 "localize to the matrix face of the inner mitochondrial membrane"].
- Homodimerizes via its transmembrane region (Gly-zipper) [PMID:25216398, via UniProt SUBUNIT].
- Induced by p53/TP53 [file:human/COQ8A/COQ8A-uniprot.txt "By p53/TP53."].

## Annotation-review disposition (summary)

- Core BP: **ubiquinone biosynthetic process (GO:0006744)** — supported by multiple IMP/IDA
  (PMID:25498144, PMID:27499294, PMID:38425362) + IBA. ACCEPT the experimental ones; keep IBA;
  IEA (UniPathway) redundant but acceptable.
- Core MF: **ATP binding** (from ATP-binding structural/biochemical data) and **ADP binding
  (GO:0043531 IDA)**; the demonstrated catalytic activity is **ATPase**. Canonical protein
  kinase activity is explicitly negated (NOT annotations kept as-is).
- CC: mitochondrion / mitochondrial membrane (inner, matrix face). Multiple EXP/IDA/HTP —
  accept; keep one as core, others non-core/redundant.
- GO:0004672 protein kinase activity **ISS** (GO_REF:0000024, from Q96D53=COQ8B) — MODIFY:
  the ISS-transferred "protein kinase activity" is contradicted by the experimental NOT
  annotation and the "lacks canonical protein kinase activity in trans" finding; recommend
  replacing with ATP binding / ATP hydrolysis activity.
- The ~65 bare "protein binding" (GO:0005515) IPI rows collapse to 8 GOA annotations (one per
  PMID). COQ9 (PMID:27499296) and complex-Q interactions are biologically meaningful but the
  bare term is uninformative → MARK_AS_OVER_ANNOTATED (never REMOVE an IPI per policy);
  high-throughput interactome ones likewise over-annotated / non-core.

## Key references

- PMID:11888884 Iiizumi 2002 — isolation of CABC1; mitochondrial; p53-inducible (abstract-only cache).
- PMID:25498144 Stefely 2015 Mol Cell — crystal structure; atypical PKL fold; ADP>ATP selectivity;
  A-rich loop; CoQ-biosynthesis structure-function. FULL TEXT.
- PMID:27499294 Stefely 2016 Mol Cell — COQ8A lacks canonical PK activity in trans; has ATPase;
  binds lipid CoQ intermediates; stabilizes complex Q; Coq8a−/− mouse = ARCA2. FULL TEXT.
- PMID:27499296 Floyd 2016 Mol Cell — mito protein interaction mapping; complex Q. FULL TEXT.
- PMID:38425362 Nicoll 2024 Nat Catal — in-vitro COQ metabolon; COQ8 streamlines CoQ production. FULL TEXT.
- PMID:33988507 Zhang 2021 eLife — subcellular kinome map (COQ8A not named in cached body text).
- PMID:34800366 — high-confidence mitochondrial proteome (HTP mitochondrion localization).
- Interactome screens (16189514, 25416956, 25910212, 31515488, 32296183, 32814053) — bare protein binding.
</content>
</invoke>
