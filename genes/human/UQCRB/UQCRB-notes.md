# UQCRB (P14927) review notes

Gene: UQCRB / UQBP; "Cytochrome b-c1 complex subunit 7" (QCR7); AltNames: Complex III subunit 7 / VII, QP-C,
"Ubiquinol-cytochrome c reductase complex 14 kDa protein". Human, taxon 9606. 111 aa, ~13.5 kDa.

## Deep research status
Falcon deep research is OUT OF CREDITS (HTTP 402) — no `-deep-research-falcon.md`. Review grounded in the cached
UniProt record (`UQCRB-uniprot.txt`), the seeded GOA (`UQCRB-goa.tsv`), cached `publications/PMID_*.md`, cached
Reactome entries, and OLS term lookups.

## Core biology (verified)
- UQCRB is a small, **non-catalytic structural subunit** of mitochondrial respiratory **Complex III** (cytochrome
  b-c1 complex / ubiquinol-cytochrome c oxidoreductase; CIII). The redox catalysis is carried by cytochrome b, the
  Rieske Fe-S protein (UQCRFS1) and cytochrome c1; UQCRB is one of the six low-molecular-weight subunits
  [UniProt SUBUNIT: "6 low-molecular weight protein subunits UQCRH/QCR6, UQCRB/QCR7, ..."].
- Complex III is an obligate dimer embedded in the mitochondrial inner membrane; it is a peripheral inner-membrane
  protein on the matrix side [UniProt SUBCELLULAR LOCATION]. It forms supercomplexes/megacomplexes with CI and CIV
  [PMID:28844695].
- CIII catalyzes transfer of electrons from ubiquinol to cytochrome c coupled to proton translocation (Q cycle)
  [Reactome R-HSA-164651; UniProt FUNCTION]. UQCRB participates in this process as a structural component.
- UQCRB was **originally thought to be the ubiquinone-binding protein (QP-C)** [PMID:3056408 title/abstract], but
  UniProt now flags this as CAUTION: "Was originally thought to be the ubiquinone-binding protein (QP-C)." So do
  NOT assert a ubiquinone-binding molecular function.
- Nuclear-encoded; imported without a cleavable presequence [PMID:3056408].

## Disease
- Biallelic/deletion variants cause **Mitochondrial complex III deficiency, nuclear type 3 (MC3DN3; MIM:615158)**;
  a QP-C gene deletion caused CIII deficiency with hypoglycaemia and lactic acidosis [PMID:12709789, cited in
  UniProt DISEASE + reference 8]. (PMID_12709789 is not cached, so not used as supporting_text.)

## MF decision (important)
GOA carries NO informative MF for UQCRB — the only MF term is GO:0005515 "protein binding" (IPI, from large-scale
interactome screens). Per project policy `protein binding` is uninformative and these IPIs are marked
MARK_AS_OVER_ANNOTATED (not REMOVE — they are experimental IntAct records whose full text I cannot verify).

For `core_functions`, the appropriate subunit-specific MF is **structural molecule activity (GO:0005198)** — this is
the schema-prescribed MF for a non-catalytic structural subunit ("contributes to the structural integrity of a
complex"), NOT an invented catalytic activity. It `contributes_to` the complex-level MF **quinol-cytochrome-c
reductase activity (GO:0008121)** enabled by the whole CIII.

## Complex CC term
Task prompt mentioned GO:0005750 for Complex III, but OLS confirms **GO:0005750 is OBSOLETE** ("obsolete
mitochondrial respiratory chain complex III"). The current, GOA-present complex term is **GO:0045275 "respiratory
chain complex III"** — used for `in_complex`. (GOA does not carry GO:0005750.)

## GOA annotation inventory (41 data lines -> 25 unique annotation rows after collapsing duplicate PMID IPIs)
- CC:
  - GO:0045275 respiratory chain complex III — IBA (GO_REF:0000033), IEA (InterPro), IPI (PMID:28844695
    ComplexPortal) -> ACCEPT (core; complex membership)
  - GO:0005743 mitochondrial inner membrane — IEA(SubCell), ISS(P00128), IDA(PMID:28844695 ComplexPortal),
    TAS x3 (Reactome) -> ACCEPT (core location)
  - GO:0016020 membrane — IEA(ARBA) -> MARK_AS_OVER_ANNOTATED (too general; inner membrane is the specific term)
  - GO:0005739 mitochondrion — HTP(PMID:34800366) -> ACCEPT (correct but less specific than inner membrane;
    keep, high-throughput mito proteome)
  - GO:0098803 respiratory chain complex — TAS(PMID:3056408) -> ACCEPT (correct but parent of GO:0045275)
- BP:
  - GO:0006122 mitochondrial electron transport, ubiquinol to cytochrome c — IBA, IEA(InterPro), NAS(ComplexPortal)
    -> ACCEPT (core process)
  - GO:0045333 cellular respiration — NAS(ComplexPortal) -> ACCEPT (broader; keep non-core)
  - GO:0006119 oxidative phosphorylation — TAS(PMID:3056408) -> ACCEPT (CIII drives OXPHOS)
  - GO:0009060 aerobic respiration — TAS(PMID:3056408) -> KEEP_AS_NON_CORE (broad)
- MF:
  - GO:0005515 protein binding — IPI x many (interactome screens) -> MARK_AS_OVER_ANNOTATED
</content>
</invoke>
