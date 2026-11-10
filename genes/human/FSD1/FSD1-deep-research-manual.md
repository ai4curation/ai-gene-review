# FSD1 (Q9BTV5) - manual literature synthesis

No deep-research API was available; this synthesis was assembled by hand from cached
publications (publications/PMID_*.md) and PubMed searches (FSD1, GLFND, MIR1) on 2026-10-28.

## Identity and domains
- FSD1 (fibronectin type III and SPRY domain containing 1; aliases MIR1, GLFND), 496 aa,
  chromosome 19. N-terminal coiled coil/B-box C-terminal (BBC) and COS box, a fibronectin
  type III domain, and a C-terminal B30.2/SPRY domain. Distant relative of the TRIM/MID1
  family but lacks the RING and B-box zinc fingers, so no E3 ligase activity is predicted.
  [PMID:11267680 "FSD1 has a BBC, FN3 and SPRY domain, it is distantly related to the midline 1 gene and is expressed only in the brain"]
- Expression: brain-enriched (UniProt TISSUE SPECIFICITY, PMID:11267680, PMID:12154070).

## Microtubule association
- Stein et al. 2002 (MIR1): [PMID:12154070 "We have identified a novel mammalian protein, MIR1, with microtubule-binding activity"];
  [PMID:12154070 "In tissue culture cells, MIR1 is enriched at the centrosome"];
  [PMID:12154070 "When overexpressed during interphase, MIR1 binds along microtubule filaments, which become stabilized, bundled and detached from the centrosome"];
  oligomerization and cdk-site phosphorylation control binding
  [PMID:12154070 "Tight binding to microtubules in interphase appears to require an oligomeric state of MIR1, and phosphorylation in mitosis at predicted cyclin-dependent kinase (cdk) sites weakens the interaction"].
  Mitotic effect on spindle poles is an overexpression phenotype
  [PMID:12154070 "In mitosis, overexpressed MIR1 dissociates from microtubules but still affects the normally focused localization of gamma-tubulin in spindle poles"].
- Manabe et al. 2002 (GLFND): [PMID:12445389 "localizes to a subpopulation of microtubules that are acetylated, and protects microtubules from depolymerization with nocodazole"];
  [PMID:12445389 "GLFND dissociates from microtubules at the beginning of mitosis and then reassociates at cytokinesis"];
  cytokinesis effect is from ectopic expression only
  [PMID:12445389 "ectopic expression of GLFND inhibits cell division and cytokinesis in CHO cells"].
- Tu et al. 2018 (full text): direct binding via SPRY domain, centrosome targeting via
  coiled coil, MT-aster anchoring at the mother centriole, required for ciliogenesis.
  [PMID:30538248 "recombinant FSD1-CC and ΔSPRY (1–268 aa) had no MT-binding activity (Fig. 6g) indicating that FSD1 directly binds to MTs through its SPRY domain"];
  [PMID:30538248 "the FSD1-CC domain (1–172 aa) was sufficient to localize to the centrosome"];
  [PMID:30538248 "We found that FSD1 localizes to the middle region of mother centrioles, directly binds to MTs, and anchors MT asters at centrosomes"];
  [PMID:30538248 "Thus, these results suggest that FSD1 promotes the anchoring of MT asters at centrosomes by directly binding MTs"].
  Knockdown in RPE-1 cells and zebrafish morphants impairs ciliogenesis, which the authors
  attribute to Cep290 mislocalization from centriolar satellites (an indirect consequence of
  lost MT asters).
- Xiao et al. 2025 (abstract only): FSD1 binds HDAC6 and restrains alpha-tubulin
  deacetylation in glioblastoma cells; CDK5 phosphorylation at Ser317/Ser324 releases FSD1
  from microtubules [PMID:39808222 "FSD1 directly interacts with histone deacetylase 6 (HDAC6) at its second catalytic domain, thereby impeding its deacetylase activity on α-tubulin"].

## Name collisions in the literature
- "FSD1" also names Arabidopsis iron superoxide dismutase (PMID:35360337, PMID:32974958,
  PMID:41408657) and the designed mini-protein FSD-1 (PMID:22417236 etc.): unrelated.
- "MIR1" alias collides with microRNA miR-1. PMID:21690310 (Tinman/Nkx2-5, miR-1, Cdc42 in
  heart) concerns miR-1 and does not mention FSD1 in its abstract or PMC full text; it is
  not evidence about FSD1.

## Localisation not supported by the literature read
- None of the FSD1 studies read here (PMID:12154070, PMID:12445389, PMID:30538248, PMID:39808222 abstract) reports a nuclear pool or nuclear function for FSD1; the UniProt "Nucleus" location has no evidence tag.
