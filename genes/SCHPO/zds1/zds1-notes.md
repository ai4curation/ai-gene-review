# zds1 (S. pombe, O14100, SPAC31F12.01) – curation notes

## Identity
- 938-aa protein; PomBase product "serine/threonine protein phosphatase PP2A regulatory
  subunit, Zds1"; synonym mug88 (meiotically upregulated). Single fission-yeast member of
  PANTHER PTHR28089 (PROTEIN ZDS1-RELATED; Zds_C domain PF08632, IPR013941), orthologous to
  S. cerevisiae ZDS1 and ZDS2 (the budding-yeast pair arose from the whole-genome duplication).
- Conservation is concentrated in the C-terminus [PMID:16322512 "the C-terminal region of Zds1
  is well conserved while the N-terminal region is less conserved"].

## Fission-yeast experimental evidence

### Yakura et al. 2006 (PMID:16322512, full text cached)
- Isolated as a multicopy suppressor of ras1delta diploid sporulation defect; acts upstream of
  Byr2 genetically [PMID:16322512 "zds1 expression did not induce sporulation in strains with
  mutations in genes participating in the downstream MAP kinase cascade"].
- Deletion phenotypes: CaCl2 sensitivity, cold sensitivity, loss of stationary-phase viability,
  round shape, zymolyase sensitivity, thicker cell wall and irregular secondary septum
  [PMID:16322512 "the zds1delta strain is round in shape and very sensitive to zymolyase, and its
  cell wall becomes thicker than that of wild type"] (abstract wording).
- Localisation of GFP fusions (overexpressed and endogenous C-terminal tag):
  [PMID:16322512 "The Zds1–GFP fusion protein localized to the cytosol, the septum, and the cell
  cortex."] Septum/cortex targeting maps to residues 682–817.
- Overexpression of the C-terminal region gives multi-septated cells and abnormal zygotes;
  N-terminal region proposed as negative regulatory region.
- The paper does NOT test PP2A binding, PP2A activity, mitotic entry timing or cell size; and it
  does not mention calcineurin. Authors speculate morphology relates to polarized growth
  [PMID:16322512 "This may be because polarized growth slows down in the stationary phase, which may
  enhance the abnormal cell morphology caused by zds1 deletion."]

### Genome-wide/large-scale data (via PomBase gene page JSON, retrieved 2026-10-10)
- Physical: Affinity Capture-MS with Paa1 (PP2A scaffold A subunit) in PMID:22119525 (SIP
  complex paper; zds1 appears only in the supplementary MS data, not in cached main text); with
  Fft3 (PMID:28218250); Affinity Capture-RNA with Zfs1 (PMID:29084823).
- A 2023 Greatwall–Endosulfine–PP2A/B55 quiescence study (PMC10723533) recovered Zds1 among
  PP2A regulators (Igo1, Zds1, Dis2, Ppe1, Ekc1) in a pull-down — a detection, not a functional
  test (read via web search summary only; not cached).
- Phenotypes (PomBase FYPO): viable; "viable vegetative cell, abnormal cell shape, normal cell
  size" (PMID:23697806, Hayles et al. 2013 deletion-collection screen; supplementary data);
  abnormal cell shape (PMID:25373780); inviable / loss of viability upon G0-to-G1 transition
  (PMID:30116786); abolished meiotic G2/MI transition and abnormal meiotic segregation in
  zds1delta/zds1delta (PMID:29259000) [PMID:29259000 "showed phenotypes indicative of defective
  conjugation (dbl2Δ), meiotic entry (cdt2Δ, zds1Δ), or asci formation (tpr1Δ, dms1Δ)"];
  various drug sensitivities/resistances (PMID:37787768).
- PomBase GO set (2026-10): MF protein phosphatase regulator activity (ISO from SGD ZDS2);
  BP establishment of cell polarity (IBA), positive regulation of G2/M transition (IBA), signal
  transduction (NAS); CC cytosol and cell division site (HDA, ORFeome PMID:16823372). The new IBA
  GO:0004864 protein phosphatase inhibitor activity (PAINT 2026-03-20) is in GOA but not yet in
  the PomBase JSON.
- I could not find any fission-yeast primary paper that directly assays Zds1 regulation of
  PP2A-Pab1 (B55/Cdc55 ortholog), its role in TORC1–Greatwall–Igo1 signalling, or its effect on
  mitotic entry; the Pab1/Etd1 cytokinesis paper (PMID:20876564) does not mention zds1.

## Budding-yeast context (seed genes of PAINT node PTN001999034)
- Zds1/Zds2 bind Cdc55-PP2A and regulate it bidirectionally [PMID:21536748 "Zds1/Zds2 promote
  Cdc55-PP2A function for mitotic entry, whereas Zds1/Zds2 inhibit Cdc55-PP2A function during
  mitotic exit"]; mechanism primarily localisation (cytoplasmic/cortical retention of Cdc55).
- Zds-family proteins are fungal-specific; Igo/ENSA proteins are the conserved B55 inhibitors
  [PMID:24800822 "Zds1-family proteins are found only in fungi but not in higher eukaryotes"].
- Zds1 localises to polarity sites in S. cerevisiae [PMID:24800822 "Zds1, which primarily
  localized to the sites of cell polarity and in the cytoplasm"].

## Assessment of PAINT PTN001999034 terms for S. pombe zds1
- GO:0005737 cytoplasm – supported directly (GFP cytosol/cortex; ORFeome cytosol). Accept.
- GO:0004864 protein phosphatase inhibitor activity – no fission-yeast evidence; even in budding
  yeast the activity is context-dependent (inhibits nuclear Cdc55-PP2A in mitotic exit, promotes
  it for mitotic entry). The neutral parent GO:0019888 protein phosphatase regulator activity
  (already annotated, ISO) captures what is known; pombe has a Paa1 AP-MS link. Recommend
  MODIFY to GO:0019888.
- GO:0010971 positive regulation of G2/M transition – no pombe evidence; zds1delta has normal
  vegetative cell size (PomBase/PMID:23697806), arguing against a significant role in mitotic
  entry timing in fission yeast, whose size control at G2/M is very sensitive. Fission-yeast
  B55 (Pab1) restrains mitotic entry and is antagonised by Greatwall–Igo1, not by Zds1 as far as
  published. Mark as over-annotated (not REMOVE; absence of phenotype could reflect redundancy).
- GO:0030010 establishment of cell polarity – consistent with pombe data: round/abnormal cell
  shape of deletion, cortical localisation; PomBase retains it. Accept (phenotypic support only;
  mechanism unknown).

## Open questions
- Does pombe Zds1 bind Pab1 (B55) directly and control its nucleocytoplasmic distribution as in
  budding yeast? Does it affect Pab1-dependent SIN/cytokinesis or cell-wall functions?
- Basis of the G0→G1 re-entry lethality and meiotic-entry defect.

## Deep research
- falcon deep-research job was launched by the orchestrator; not present at time of writing.

## Addendum: falcon deep research (arrived after the review was written)

`zds1-deep-research-falcon.md` landed after the annotation review was finished and was cross-checked
against it. It agrees with the review: Zds1 is a non-catalytic regulatory protein localized to the
cytosol, septum and cell cortex, required for cell-wall integrity, cell shape and sexual
differentiation, and linked to PP2A in fission yeast only by a nitrogen-starvation Paa1 affinity-MS
co-purification; no pombe experiment shows PP2A inhibition. It is cited on the GO:0004864 (MODIFY to
GO:0019888) row. No annotation decision changes.
