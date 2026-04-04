# BioReason-Pro SFT Review: wsc1 (Schizosaccharomyces pombe)

Source: wsc1-deep-research-bioreason.md

- **Correctness**: 3/5
- **Completeness**: 3/5

## Functional Summary Review

The BioReason functional summary describes Wsc1 as:

> A single-pass plasma membrane receptor in fission yeast that uses an extracellular carbohydrate-binding module to sense mechanical strain at growth sites and transmit this information across the membrane to a Rho1-centered kinase cascade. By activating a protein kinase C-MAP kinase pathway, it maintains cell wall integrity, supports polarized growth at the cell tip, and restrains stress-induced necrotic death.

This summary correctly captures the overall architecture and localization of Wsc1, including the WSC domain, single-pass topology, plasma membrane localization at cell tips, and Rho1-centered signaling. However, it contains several significant errors in the downstream pathway and one unsupported functional claim.

**Correctness issues:**

1. **The PKC-MAPK pathway assignment is incorrect for S. pombe Wsc1.** BioReason states Wsc1 activates "a protein kinase C-MAP kinase pathway" involving "Protein kinase C-like 2" and "MAP kinase kinase skh1/pek1." This conflates the Wsc1-specific signaling branch with the general CWI MAPK pathway. Cruz et al. 2013 (PMID:23907979) explicitly demonstrated that MAPK Pmk1p signaling remained active in wsc1-delta disruptants, meaning Wsc1 acts INDEPENDENTLY of the CWI MAPK cascade. The actual Wsc1 pathway is: Wsc1 -> Rgf2 (Rho-GEF) -> Rho1 -> beta-1,3-glucan synthase. The PKC pathway (Mtl2 -> Rho1 -> Pck1) is the parallel Mtl2-specific branch. This is a fundamental pathway-assignment error.

2. **"Negative regulation of necrotic cell death" (GO:0060547) is unsupported and uses an obsolete term.** GO:0060547 is listed as obsolete in the Gene Ontology. Moreover, there is no published evidence that S. pombe Wsc1 regulates necrotic cell death. While CWI pathway mutants can undergo lytic death from wall rupture, this is mechanical failure, not regulated necrotic cell death. The claim that Wsc1 "restrains stress-induced necrotic death" is an unsupported extrapolation from the general concept that maintaining wall integrity prevents lysis.

3. **GO:0004888 (transmembrane signaling receptor activity) was proposed but the existing curated term GO:0140897 (mechanoreceptor activity) is more specific and experimentally validated.** BioReason defaults to the general receptor term when the curated annotation already captures the specific type of receptor activity.

4. **The thinking trace mentions "MAP kinase kinase skh1/pek1" as a direct component of the Wsc1 pathway.** There is no evidence that Wsc1 signals through Skh1/Pek1 in S. pombe. This appears to be transferred from S. cerevisiae Wsc1 biology without recognizing the critical difference demonstrated in Cruz et al. 2013.

5. **The mention of "uncharacterized aminotransferase C6B12.04c" as an interaction partner** is not validated in the peer-reviewed literature for Wsc1 function and may come from high-throughput interaction datasets without functional validation.

**What BioReason got right:**

1. The WSC domain architecture and its role in binding cell wall polysaccharides is accurately described.
2. The single-pass type I topology with extracellular WSC domain and cytoplasmic signaling tail is correct.
3. Rho1 as the central signaling hub is correct.
4. Plasma membrane of cell tip localization is correct.
5. The general function in cell wall integrity and polarized growth is correct.

**Completeness issues:**

1. **No mention of Wsc1 force-dependent clustering.** The key mechanistic insight from Neeli-Venkata et al. 2021 (PMID:34666001) -- that Wsc1 forms micrometer-sized clusters at sites of force application through reduced lateral diffusivity -- is absent. This is the defining mechanistic feature of Wsc1 mechanosensing.

2. **No mention of the autonomous nature of Wsc1 mechanosensing.** Neeli-Venkata et al. 2021 showed clustering is independent of canonical polarity, trafficking, and downstream CW regulatory pathways. This is a distinctive property.

3. **No mention of cell wall thickness homeostasis.** Davi et al. 2018 (PMID:29689193) demonstrated that Wsc1 mediates a dynamic feedback controlling wall thickness at growing tips, and wsc1 mutants lyse from wall rupture. This directly establishes physiological function.

4. **No mention that Wsc1 and Mtl2 are functionally redundant for Rho1 activation.** The synthetic lethality of the double deletion is a key genetic finding.

5. **No mention of O-mannosylation** of the Ser/Thr-rich ectodomain, which contributes to the rod-like rigidity of the extracellular domain.

## Comparison with InterPro2GO

The InterPro annotations for Wsc1 yield:
- IPR002889 (WSC domain): No direct InterPro2GO mapping to a specific MF term
- IPR051836 (Kremen receptor family): Broad structural classification

BioReason adds substantial mechanistic context beyond raw InterPro2GO annotations by correctly inferring receptor-like signaling from the domain architecture. However, the pathway errors (PKC-MAPK attribution) and the unsupported necrotic cell death claim make portions of the BioReason output less accurate than the curated PomBase annotations.

## Notes on Thinking Trace

The thinking trace demonstrates competent domain-to-function reasoning from the WSC domain and transmembrane topology. The main weakness is the pathway assignment: the trace constructs a linear cascade (Wsc1 -> Rho1-GEF -> Rho1 -> PKC-like 2 -> MAPKK Skh1/Pek1) that merges the distinct Wsc1 and Mtl2 signaling branches documented in the literature. In S. pombe, the Wsc1-specific output is Rgf2 -> Rho1 -> glucan synthase (not PKC -> MAPK). The PKC branch is the Mtl2 pathway. This error likely stems from over-reliance on S. cerevisiae Wsc1 biology where Wsc1 does signal through PKC/MAPK, without accounting for the documented differences in S. pombe.

The GO:0060547 prediction for necrotic cell death reveals a tendency to extrapolate from indirect reasoning (wall integrity -> prevents lysis -> prevents necrotic death) without checking whether the GO term is valid or whether experimental evidence supports the claim. The term is in fact obsolete.

## GO Term Predictions Assessment

BioReason's deep-research file curiously lists empty GO term predictions under "Molecular Function," "Biological Process," and "Cellular Component" sections, despite the thinking trace discussing specific terms. The predictions are embedded only in the narrative, not in structured form, making systematic evaluation difficult.
