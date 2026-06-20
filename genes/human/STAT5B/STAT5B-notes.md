# STAT5B (P51692) — Gene Review Notes

Journal of research and provenance for the AI review of human STAT5B (HGNC:11367).

## Overview / identity

- UniProt P51692, "Signal transducer and activator of transcription 5B" (STA5B_HUMAN), 787 aa, chr17q21.2.
- Member of the STAT family of transcription factors. Domain architecture (from UniProt + PMID:29844444): N-terminal domain (ND), 4-alpha-helix coiled-coil domain (CCD), DNA-binding domain (DBD), linker, SH2 domain (aa 589–686), C-terminal transactivation domain (TAD).
- Paralog: STAT5A (P42229), ~90% identical, differing mainly in the C-terminal TAD. Largely overlapping but non-redundant functions.

## Core mechanism (latent cytoplasmic TF → activated nuclear TF)

STAT5B is a latent cytoplasmic transcription factor. Cytokine/hormone receptor engagement activates receptor-associated JAK kinases, which phosphorylate STAT5B on Tyr-699; phospho-STAT5B dimerizes (via reciprocal SH2–pTyr interactions), translocates to the nucleus, binds GAS (gamma-activated sequence) DNA elements, and activates transcription of target genes.

- Activating tyrosine: Tyr-699. [UniProt P51692 FT MOD_RES 699 "Phosphotyrosine; by HCK, JAK and PTK6"]; [PMID:8631883 "human Stat5 activation is also dependent on Tyr-694 in Stat5A and Tyr-699 in Stat5B, indicating that these tyrosines are required for dimerization"].
- Subcellular location: Cytoplasm and Nucleus; "Translocated into the nucleus in response to phosphorylation." [UniProt P51692 SUBCELLULAR LOCATION, ECO:0000269|PubMed:29844444].
- Homodimerization on activation: [PMID:29844444 "Co-immunoprecipitation (co-IP) experiments, furthermore, supported homo-dimerization capabilities for each variant"]; UniProt SUBUNIT "Upon activation, forms homodimers (PubMed:29844444)".
- DNA binding to canonical STAT5B response element (GHRE/GAS): [PMID:29844444 "WT STAT5B readily bound and gel-shifted the STAT5B-specific DNA probe (GHRE) only under GH-stimulated conditions"] and luciferase reporter transactivation [PMID:29844444 "STAT5B-mediated luciferase reporter assays"].

## Upstream activators (cytokines/hormones → JAKs)

STAT5B is activated downstream of many cytokine and hormone receptors:
- Common gamma-chain cytokines: IL-2, IL-7, IL-9, IL-15, IL-21 (via JAK1/JAK3). IL-2: [PMID:8631883 "both Stat5A and Stat5B are activated by interleukin-2 (IL-2) in peripheral blood lymphocytes, natural killer-like YT leukemia cells"]; reconstitution required "coexpression of Jak3 along with the IL-2 receptor beta chain and the common cytokine receptor gamma-chain" [PMID:8631883].
- Growth hormone (GH): the "key signal transducer for GH" [PMID:29844444 "Autosomal-recessive mutations in signal transducer and activator of transcription (STAT5B), the key signal transducer for GH"]; GH → JAK2 → STAT5B → IGF1 induction. GHISID1/2 phenotypes (below).
- Prolactin (PRL): UniProt FUNCTION "Binds to the GAS element and activates PRL-induced transcription."
- Erythropoietin (EPO) via JAK2: [PMID:9657743 "erythropoietin induces tyrosine phosphorylation of Jak2, STAT5A, and STAT5B"; "Tyrosine phosphorylation of STAT5 is accompanied by the translocation of activated STAT5 to the nucleus"].
- Oncostatin-M via type II OSM receptor (OSMR/IL6ST): UniProt FUNCTION (PubMed:9188471).
- Also GM-CSF/IL-3/IL-5, thrombopoietin, G-CSF, KIT (SCF), FLT3, FGFR1 fusions (Reactome pathways in UniProt DR lines; many in oncogenic context).

## Biological roles

- Growth / IGF1 axis: STAT5B loss-of-function causes growth hormone insensitivity syndrome with immune dysregulation (GHISID1, AR; GHISID2, AD). [PMID:29844444 "STAT5B deficiency (MIM 245590), a rare cause of GHIS with immunodeficiency"]. Dominant-negative missense variants in CCD (Q177P, abrogated nuclear import) and DBD (Q474R, A478V, loss of DNA binding) disrupt WT STAT5B by heterodimerizing with it [PMID:29844444 "each variant retains the ability to dimerize with wild-type STAT5B, disrupting the normal transcriptional functions of wild-type STAT5B"].
- Lymphocyte development / immunity: gamma-chain cytokine signaling drives T-cell (esp. Treg via Foxp3) and NK development; STAT5B deficiency → immune dysregulation, T-lymphopenia. General "defense response" / immunity role (IBA). Note STAT5B can form STAT heterodimers (e.g., STAT3/STAT5B, STAT5A/STAT5B) [PMID:24058793 review of STAT heterodimers in immunity].
- Hematopoiesis / erythropoiesis: positively regulates erythroid differentiation; STAT5B level controlled post-transcriptionally by ZFP36L1 [PMID:20702587 "ZFP36L1 negatively regulates erythroid differentiation ... by directly binding the 3' untranslated region of Stat5b encoding mRNA"; "Stat5b down-regulation ... results ... in a drastic decrease of erythroid colonies formation"].
- Oncogenesis: recurrent somatic activating mutations (e.g., SH2-domain N642H) in T/NK leukemias and lymphomas. [PMID:29844444 "Recurrent somatic activating heterozygous missense STAT5B mutations in the SH2 or TAD domains ... were recently identified and reported to be causal of lymphomas"]; structural/functional study of N642H driver mutation [PMID:31175292 "Structural and functional consequences of the STAT5B(N642H) driver mutation"].

## Protein interactions (GO:0005515 IPI sources)

- NMI (Q13287): identified via yeast two-hybrid with the STAT5b coiled-coil region; augments STAT5/STAT1 transcription by enhancing CBP/p300 recruitment [PMID:9989503 "Using the coiled-coil region of Stat5b as the bait in a yeast two-hybrid screen, we identified the association of Nmi"; "Nmi enhances the association of CBP/p300 coactivator proteins with Stat1 and Stat5"].
- hTid1 / DNAJA3 (Q96EY1): DnaJ tumor suppressor binding the STAT5b TAD; negative regulator [PMID:21106534 "hTid1 interacts specifically with STAT5b but not with STAT5a"; "hTid1 negatively regulates the expression and transcriptional activity of STAT5b"].
- ABL1 (P00519): IntAct (PMID:31175292), UniProt INTERACTION block.
- High-throughput binary/affinity interactome partners (PMID:32296183 HuRI; PMID:33961781 BioPlex): HNRNPA2B1, USP2, CDKN1A, PIK3R3, RBBP4, CHAF1A, LMO4, MED25, MRPS6, STAC, SUOX, TSSK3, ZNF410, LGALS14 — mostly generic/HT, not core function.
- NR3C1 / glucocorticoid receptor (P04150): GO:0035259 nuclear glucocorticoid receptor binding (IPI, PMID:12552091). Note: PMID:12552091 itself is an estrogen/SOCS-2/GH-signaling paper (see caveat below).

## Caveats / citation notes

- PMID:12552091 (Leung et al., PNAS 2003) is titled/abstracted as "Estrogen inhibits GH signaling by suppressing GH-induced JAK2 phosphorylation, an effect mediated by SOCS-2." The abstract reports GH-stimulated STAT5 reporter activity in 293GHR/HuH7/T-47D cells. It is the original_reference for four annotations: GO:0060397 (GH receptor signaling via JAK-STAT, IDA), GO:0032355 (response to estradiol, IDA), GO:0032870 (cellular response to hormone stimulus, IDA), and GO:0035259 (nuclear glucocorticoid receptor binding, IPI). The GR-binding annotation is curator (BHF-UCL) judgment from full text; abstract is consistent with GH/STAT5 + estradiol but does not itself mention GR binding in the cached abstract. Full text not cached (full_text_available: false) — defer to curator where evidence is experimental (do not REMOVE).
- PMID:8631883, PMID:9657743, PMID:9989503, PMID:12552091 are abstract-only in cache.
- PMID:11773439 (TC-PTP/PTPN2 regulation of STAT5) was RETRACTED (PMID:24319783). Not in GOA annotation set here; noted for completeness.
- GO:0019530 taurine metabolic process (ISS, acts_upstream_of_positive_effect, from mouse P42232) is a narrow, indirectly-transferred annotation; flagged as over-annotation / non-core.

## Core function summary

1. Sequence-specific RNA Pol II DNA-binding transcription (activator) factor binding GAS elements (GO:0000981 / GO:0001228).
2. Cytokine/JAK-STAT signal transducer (GO:0007259 / GO:0019221), including GH receptor signaling (GO:0060397) and EPO signaling (GO:0038162).
3. Activation-dependent homo/heterodimerization (GO:0042803).
Outputs: regulation of growth (IGF1 axis), lymphocyte/Treg/NK development & immunity, and erythroid/hematopoietic differentiation.
