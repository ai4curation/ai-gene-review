# CHRM1 (human, UniProt P11229) - curation notes

**Provenance note:** Provider deep research for this gene FAILED (Falcon returned
HTTP 402 Payment Required; Perplexity is not configured). No `*-deep-research-*.md`
file exists. The synthesis below replaces it and was written manually from the
UniProt record (`CHRM1-uniprot.txt`), the cached publications in `publications/`,
cached Reactome entries in `reactome/`, and PubMed E-utilities searches used only to
identify PMIDs, which were then cached with `just fetch-gene-pmids human CHRM1`.

## Identity and family

- CHRM1 encodes the M1 muscarinic acetylcholine receptor, a class A (rhodopsin-like)
  seven-transmembrane GPCR; UniProt: "Belongs to the G protein-coupled receptor 1
  family. Muscarinic acetylcholine receptor subfamily. CHRM1 sub-subfamily."
- Human M1 cloned alongside M2-M4 [PMID:3443095 "we have isolated the genes encoding the
  human M1 and M2 muscarinic receptors (mAChR) as well as two previously undiscovered
  mAChR subtypes, designated HM3 and HM4"]; "seven, highly conserved transmembrane
  segments and a large intracellular region unique to each subtype".
- Crystal structure with tiotropium [PMID:26958838 "Here we report the crystal structures of
  the M1 and M4 muscarinic receptors bound to the inverse agonist, tiotropium."]

## Molecular function: acetylcholine-activated GPCR (Gq/11-coupled)

- Subtype coupling: [PMID:31073061 "M1R, M3R, and M5R couple to the Gq/ 11 family, whereas M2R
  and M4R couple to the Gi/o family."] and [PMID:31073061 "By contrast, M1R, M3R, and M5R
  predominantly couple to Gq/11 proteins (Gq and G11), leading to the activation of
  phospholipase C and the increase of cytosolic Ca2+"]. Cryo-EM structure of active M1R
  bound to heterotrimeric G11.
- Human M1 expressed in CHO activates both Gq and G11 [PMID:8508928 "the HM1 receptor interacts
  with the activates both Gq alpha and G11 alpha equivalently and non-selectively"].
- Agonist binding/activation (xanomeline, carbachol) drives PI hydrolysis [PMID:9614217
  "Functional assays, using both M1 mAChR-mediated phosphoinositide hydrolysis and activation
  of neuronal nitric oxide synthase"].
- Reactome: [Reactome:R-HSA-390649 "All of these three receptors couple with Gq/11 protein which
  use the upregulation of phospholipase C and therefore inositol trisphosphate and
  intracellular calcium as a signaling mechanism"].
- UniProt FUNCTION text is family-generic ("inhibition of adenylate cyclase, breakdown of
  phosphoinositides and modulation of potassium channels"), but says "Primary transducing
  effect is Pi turnover." Adenylate cyclase inhibition is the Gi-coupled M2/M4 property.
- The receptor itself is NOT a phospholipase: PIP2 hydrolysis is catalysed by PLC-beta
  downstream of Gq/11 [PMID:8139539 "m1R stimulation of phospholipase C beta and the marked
  rise in intracellular calcium stimulated cyclic AMP (cAMP) synthesis"]. Annotations of
  GO:0004435 to CHRM1 are therefore mis-assignments of a downstream enzyme activity.
- Secondary cAMP effect is stimulatory (Ca2+-sensitive adenylyl cyclase), not inhibitory
  [PMID:8139539].

## Downstream signaling outputs (cell-model studies)

- EGR transcription factor induction via PKC [PMID:9603968 "mRNA levels of Egr-1, Egr-2, and
  Egr-3 increased readily after m1AChR stimulation"].
- Inhibition of growth-factor activation of Raf via PKA [PMID:8139539].
- Stimulated secretion of APP derivatives (sAPPalpha) in transfected HEK293 cells
  [PMID:1411529 "Stimulation of m1 and m3 receptor subtypes with carbachol increased the basal
  release of APP derivatives within minutes of treatment"].
- Mitogenic effect in cells expressing PI-coupled subtypes [PMID:2739737].
- Agonist-induced internalization/down-regulation with Gq/G11 [PMID:7925360].
- Used as a PLC/Ca2+ driver to activate TRPM5 in HEK-293 M1 cells [PMID:14657398 "The M1
  muscarinic ACh receptor expressed by these cells couples to PLC"].

## Physiology (mouse knockouts)

- M-current suppression in sympathetic neurons requires M1; KO mice resist pilocarpine
  seizures [PMID:9371842 "the m1 receptor subtype mediates M current modulation in sympathetic
  neurons and induction of seizure activity in the pilocarpine model of epilepsy"].
- Pilocarpine salivation does not require M1 [PMID:9371842 "salivation, eye watering,
  myoclonic jerks, and tremors, which thus do not require the m1 subtype"].
- Cognition: [PMID:12483218 "M1 null mutant mice showed normal or enhanced memory for tasks
  that involved matching-to-sample problems, but they were severely impaired in
  non-matching-to-sample working memory as well as consolidation."]; reduced theta-burst LTP.
- M1 is the most abundant mAChR in hippocampus and forebrain [PMID:12483218 "the M1 receptor,
  the most densely distributed muscarinic receptor in the hippocampus and forebrain"].
- Review of mAChR KO phenotypes [PMID:14744253].

## Localization

- Plasma membrane / postsynaptic membrane (UniProt). Hippocampal CA1/CA3 and dentate
  immunoreactivity absent in KO [PMID:9371842]. Agonist drives transfer from plasma membrane
  to light vesicles [PMID:7925360].

## Curation decisions summary

- Core: GO:0016907 G protein-coupled acetylcholine receptor activity; GO:0007207
  PLC-activating GPCR acetylcholine receptor signaling pathway; plasma membrane /
  postsynaptic membrane.
- REMOVE GO:0004435 (PLC activity belongs to PLCB), GO:0007197 (Gi/AC-inhibition is M2/M4),
  protein binding (uninformative; TMEM147 interaction is not disputed).
- Developmental/proliferation TAS rows judged over-annotation.
