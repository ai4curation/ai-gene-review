# AMD2 (YDR242W) — research notes

UniProt: P22580 (AMDY_YEAST) · SGD: S000002650 · Systematic: YDR242W · 549 aa · EC 3.5.1.4 (probable).
Status: **dark / understudied gene** — no direct biochemical or genetic characterization of the physiological reaction.

## Summary: KNOWN vs NOT-known

### KNOWN (well supported)
- AMD2 is a member of the **amidase signature (AS) family** (Pfam PF01425 "Amidase"; InterPro IPR023631
  Amidase_dom, IPR020556 Amidase_CS, IPR036928 AS_sf; PROSITE PS00571 AMIDASES; Gene3D 3.90.1300.10;
  SUPFAM SSF75304; PIRSF001221 "Amidase_fungi"). It is inferred from homology (UniProt PE 3).
- The protein carries the **conserved AS-family Ser–cisSer–Lys catalytic triad**: UniProt annotates
  ACT_SITE at positions 132 and 209 ("Charge relay system") and 233 ("Acyl-ester intermediate"),
  all by similarity (ECO:0000250). Presence of an intact triad is consistent with a catalytically
  competent amidase rather than a pseudoenzyme.
- The UniProt CATALYTIC ACTIVITY block records the generic AS-family reaction
  (Rhea:RHEA:12020; EC 3.5.1.4): "a monocarboxylic acid amide + H2O = a monocarboxylate + NH4(+)".
  This is exactly the definition of GO:0004040 amidase activity
  ("Catalysis of the reaction: a monocarboxylic acid amide + H2O = a monocarboxylate + NH4+.", OLS/GO).
- AMD2 is non-essential. High-throughput phenotype data in SGD report that the null mutant has
  **decreased resistance to nutrient deprivation** and **decreased resistance to the antifungal
  miconazole** (SGD locus S000002650; https://www.yeastgenome.org/locus/S000002650). These are
  chemogenomic/HTP-screen phenotypes, not a defined biochemical role.
- The gene was first identified as a *putative* amidase from genomic sequence by Chang & Abelson 1990
  [PMID:2263500 "Identification of a putative amidase gene in yeast Saccharomyces cerevisiae."] — a
  one-page sequence note; abstract-only in cache; no enzymatic assay reported.

### NOT known (knowledge gaps — the primary deliverable)
- **Physiological substrate / exact reaction is unknown.** EC 3.5.1.4 "amidase" and Rhea:12020 are
  generic parent activities covering "a monocarboxylic acid amide"; the specific amide substrate
  hydrolysed by AMD2 in vivo has never been determined experimentally.
- **In-vivo biological process is unknown.** No pathway placement; GOA carries only an ND
  (No biological Data) root annotation for BP.
- **Subcellular localization is unknown.** No experimental localization; GOA carries only an ND root
  annotation for CC. (UniProt gives no SUBCELLULAR LOCATION; there is no predicted signal peptide,
  transit peptide or transmembrane segment in the record.)
- **Direction of the observed phenotypes is mechanistically unexplained** — why loss of a putative
  amidase would decrease resistance to nutrient starvation or to miconazole is not established.

## Inline domain reasoning (from the UniProt record)

The AS (amidase signature) family (Pfam PF01425) is a large, functionally diverse enzyme family whose
members hydrolyse a wide range of carboxamide substrates. They share the Ser-cisSer-Lys catalytic triad
in the conserved "GGSS(G/S)GS" signature region. In P22580 the sequence around residue 209 is
`...GGSSGGEGS...` (see SQ, "SGGSSGGEGSLIGAHG"), the canonical AS signature block, and the annotated
active-site residues (Ser132, Ser209, Lys — annotated as 233 "acyl-ester intermediate") map onto the
expected triad geometry. This strongly supports assignment to the family and a **generic amidase
(carboxamide hydrolase, EC 3.5.1.4)** activity, but the AS fold is notoriously substrate-promiscuous
across the family, so fold membership alone does NOT license a specific-substrate MF term.

### Subfamily / orthology context (from fetched PANTHER PTHR46072)
- AMD2 belongs to PANTHER family **PTHR46072 "Amidase"**, subfamily **PTHR46072:SF11 "AMIDASE-RELATED"**.
- Its co-members in SF11 include the *S. pombe* uncharacterized amidase **Q8TFF9 (SPBPB8B6.03)** — i.e.
  AMD2's closest annotated relatives are themselves uncharacterized ("putative amidase").
- The best-characterized members of the broader PTHR46072 family are the fungal **acetamidases**
  (*A. nidulans* amdS P08158; *A. oryzae* amdS Q12559), but these sit in a *different* subfamily
  (PTHR46072:SF9 "ACETAMIDASE"), so AMD2 should NOT be assumed to be an acetamidase. Other family
  members are involved in cyclic-peptide (KK-1) biosynthesis and benzoxazolinone detoxification in
  filamentous fungi (PANTHER family description), again outside AMD2's subfamily.
- eggNOG KOG1212 (Eukaryota); no vertebrate 1:1 ortholog implied. S. cerevisiae has no obvious
  paralog assigned to this family in the record (single AS-family gene in this PANTHER subfamily).

Conclusion of domain reasoning: a **generic "amidase activity" (GO:0004040)** MF assignment is
domain-defensible (intact triad + AS fold + Rhea/EC). A **specific-substrate** amidase term would be
over-annotation and is not supported.

## GOA annotations to review (4)
1. GO:0004040 amidase activity — IEA (GO_REF:0000120, from RHEA:12020|EC:3.5.1.4). Domain-defensible
   at the generic level → ACCEPT (this is the one substantive, defensible function).
2. GO:0003674 molecular_function — ND (GO_REF:0000015, SGD). Root placeholder. Now superseded by the
   IEA amidase MF → this is the standard "no experimental data" stub. Keep as non-core / note it is a
   root placeholder (do not treat as informative).
3. GO:0005575 cellular_component — ND (GO_REF:0000015, SGD). Root placeholder; localization unknown.
4. GO:0008150 biological_process — ND (GO_REF:0000015, SGD). Root placeholder; process unknown.

Note: UniProt DR GO also lists GO:0043605 (amide catabolic process, IBA) but this is NOT in the GOA
TSV and the term is **OBSOLETE** ("unnecessary grouping term"), so it is not reviewed here.

## Other data
- BioGRID lists physical/genetic interactions (e.g. NAM7/UPF1, YRA2) from HTP screens; none establishes
  a molecular function and none is used as annotation support here.

## Falcon deep-research (2026-07-05, genuine late file) — key take-aways and caveats

The falcon/Edison report (`AMD2-deep-research-falcon.md`, 1668 s runtime) reinforces the honest
"dark enzyme, substrate unknown" framing. Load-bearing, independently verified point it surfaced:

- **AMD2 is not a classical acetamidase.** Wild-type S. cerevisiae S288C does not grow on acetamide
  as a nitrogen source and requires a heterologous acetamidase (A. nidulans amdS or Y. lipolytica
  YlAMD1). Verified directly in Hamilton et al. 2020 (PMC full text)
  [PMID:32024536 "Control transformations failed to form colonies while YlAMD1-transformed cells gave
  rise to well-defined colonies on acetamide plates"] and
  [PMID:32024536 "amdS can be recycled through counterselection with fluoroacetamide"]. S288C is the
  exact strain used, and it is described in that paper's Table 1 as
  "Mat-alpha ... ATCC 204508 strain S288C" — the reference proteome strain that carries AMD2. So the
  native genome (with AMD2) does not confer acetamidase activity. This matches the PANTHER-subfamily
  reasoning above (AMD2 in SF11, acetamidases in SF9) and is now cited in the review as MEDIUM-relevance
  supporting evidence for the MF knowledge gap.

Caveats / errors in the falcon report I deliberately did NOT propagate:
- It states AMD2 is **598 aa** — WRONG; UniProt P22580 is **549 aa**. Not used.
- It asserts a paralog **"AMD1 (YCR025C)"** — unverified (YCR025C is itself a dubious/uncharacterized
  ORF); not asserted in the review.
- It cites cytoplasmic localization from Huh et al. 2003 GFP study — plausible but the paper is not in
  cache and I did not verify a usable verbatim quote, so I kept CC as an open knowledge gap (ND retained,
  not replaced by a specific CC term). This is the conservative choice for a dark gene.

All AS-family biochemistry statements (Ser-cisSer-Lys triad, generic R-CO-NH2 + H2O -> R-COOH + NH3
reaction, family substrate diversity: FAAH/NAE, plant AMI1/IAM, malonamidase E2, peptide amidase) are
consistent with the UniProt/InterPro record and general enzymology; they are used only as framing, with
the concrete review anchored to UniProt + GOA + PMID:2263500 + PMID:32024536.
