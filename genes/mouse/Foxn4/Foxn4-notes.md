# Foxn4 (mouse, Q8K3Q3) curation notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: Foxn4 is being reviewed as the experimentally characterised reference relative of
the fly gene jumu (Q9XTP7). No ProtNLM2 output was opened or used. This is a de-novo review.

### Deep research

`just deep-research-falcon mouse Foxn4 --fallback perplexity-lite` FAILED: falcon raised
"Failed to authenticate" and the perplexity-lite fallback returned HTTP 401 (insufficient
quota). No deep-research file exists; the review is written from primary literature cached
in `publications/` (PubMed esearch for Foxn4[tiab] used to find the mouse primary papers).

### Evolutionary grounding

- PANTHER 19.0 classification files (`PTHR19.0_mouse`, `_human`, `_zebrafish`,
  `_fruit_fly`; build cache under `.cache/panther/`) place mouse Foxn4 (Q8K3Q3), human FOXN4
  (Q96NZ1), zebrafish foxn4 (A2BGM5, the slipjig gene) and fly jumu (Q9XTP7) together in
  **PTHR13962:SF17 FORKHEAD BOX PROTEIN N4**. FOXN2 (P32314, SF19) and FOXN3 (O00409, SF20)
  are sister subfamilies in PTHR13962. FOXN1 (O15353/Q61575) sits in a separate family,
  PTHR46721:SF1.
- Caveat: the current UniProt record carries `PANTHER; PTHR46721:SF2; FORKHEAD BOX PROTEIN N4`
  for Foxn4, and jumu's UniProt record carries `PTHR46721:SF3` (FORKHEAD BOX N1). The newer
  PANTHER release used by UniProt therefore moves FOXN4 next to FOXN1 and does not put jumu in
  the same subfamily as Foxn4. The family review `interpro/panther/PTHR46721/PTHR46721-review.yaml`
  already notes that mouse/zebrafish Foxn4 and Jumu have differing observed parents. I did not
  try to resolve which placement is right; for transfer to jumu, the PANTHER 19.0 SF17 grouping
  and the PAINT node (below) are the relevant evidence, and FOXN4-lineage-specific programmes
  (retina, V2 spinal interneurons, lung, AV canal) should not be transferred.
- PAINT node PTN000216159 (GO_REF:0000033) is the source of every Foxn4 IBA. Its experimental
  donors span mouse Foxn4, zebrafish foxn4, human FOXN3 (O00409), human FOXN2 (P32314) and fly
  jumu (FBgn0015396), so the node sits above the FOXN2/FOXN3/FOXN4 split. PAINT propagated
  only: DNA-binding transcription factor activity (GO:0003700), cis-regulatory region
  sequence-specific DNA binding (GO:0000987), nucleus (GO:0005634, is_active_in) and regulation
  of DNA-templated transcription (GO:0006355). None of Foxn4's experimental developmental
  process terms (amacrine cell differentiation, V2 interneuron fate commitment, retina layer
  formation) and none of the zebrafish heart terms was propagated. I treat those omissions as
  deliberate: the processes are lineage-specific uses of a shared transcription-factor activity.

### What is established experimentally in mouse

- **Sequence-specific DNA binding / transcription activation.** Foxn4 activates the Dll4 5'
  enhancer CR1 through a cluster of four ACGC motifs; mutating them abolishes activation, and
  anti-Foxn4 ChIP precipitates the ACGC-containing CR1 region from E14.5–E17.5 mouse retina
  chromatin (and from human Y79 cells)
  [PMID:22323600 "anti-Foxn4 antibody specifically precipitated CR1 fragments containing the ACGC cluster"].
  Foxn4 binds ACGC-containing probes (F1, F2) from a Ptf1a enhancer in EMSA and activates the
  Ptf1a enhancer 5.1-fold alone and >=90-fold with RORβ1
  [PMID:23652001 "probes containing the conserved ACGC sequences in F1 and F2 each bound Foxn4 protein in EMSA"].
- **Activation domain.** A C-terminal region (aa 402–455) homologous to the FOXN1 activation
  domain is required for Foxn4 transcriptional activity in vitro and in retinal explants
  [PMID:21701787 "the domain between amino acids 402 and 455 is necessary for Foxn4 transcriptional activity"].
- **Nucleus.** UniProt curated nuclear location with ECO:0000269 to PMID:22323600.
- **Retina.** Foxn4 is expressed in a subset of mitotic retinal progenitors; knockout largely
  eliminates amacrine cells and abolishes horizontal cells; overexpression promotes amacrine
  fate [PMID:15363391, abstract only]. Foxn4 is required for Ptf1a, Neurod1/Neurod4 expression
  and directly activates Dll4 to limit photoreceptor production [PMID:22323600]. Later work
  frames Foxn4 as a temporal identity factor for mid/late-early retinal competence
  [PMID:32071204]. RGC axon patterning defects in Foxn4-/- mice are attributed to the loss of
  amacrine cells (Foxn4 is not expressed in RGCs) [PMID:21334440]; that is non-cell-autonomous
  and is not a Foxn4 process.
- **Spinal cord V2 interneurons.** Foxn4 is expressed in p2 progenitors; loss eliminates Mash1
  expression and V2b neurons with a fate switch to V2a [PMID:16020526]; Foxn4 induces Dll4 and
  Mash1 [PMID:17728344]; Foxn4 and Ascl1 bind a conserved Dll4 enhancer [PMID:24257627]; V2c
  (Sox1+) interneurons are absent in Foxn4 mutants [PMID:20844123].
- **Lung.** Foxn4 is expressed in postmitotic proximal-airway epithelial cells; knockout gives
  alveolar defects with reduced PDGFA, proposed to be non-cell-autonomous [PMID:21438071].
  I do not propose a lung process term: the authors themselves frame the role as indirect.

### What is NOT established in mouse

- Heart / AV canal. The AV-canal role comes from the zebrafish slipjig/foxn4 mutant, where
  Foxn4 binds a conserved tbx2 enhancer [PMID:18347092]. The same paper notes that the mouse
  question is open: "Foxn4 -null mutant mice die perinatally, but their cause of death is
  unclear". The three ISS heart rows (heart looping, regulation of heart contraction, AV canal
  development) are therefore inferred only. Heart looping and contraction defects are
  downstream organ phenotypes of the AV-canal failure in fish and are marked over-annotated;
  AV canal development is left UNDECIDED for mouse.
- Thymus: FOXN4 can partly substitute for FOXN1 in a knock-in experiment [PMID:25131198,
  abstract only]; that shows capacity, not a normal physiological role, so no annotation.
- Multiciliated cells: the Foxn4–Foxj1 multiciliogenesis role is Xenopus [PMID:27864379];
  not tested in mouse, not transferred.

### Ontology gap

There is no GO term for retinal horizontal cell differentiation (only GO:0035852 horizontal
cell localization). Recorded as a proposed new term, since horizontal cells are completely
absent in Foxn4 null retinas.

### Notes on the human FOXN4 (Q96NZ1) papers

Two human breast-cancer papers on FOXN4 (PMID:31430519, PMID:32021256) were retracted
(retraction notices PMID:33208228, PMID:33235463). Neither is used here. Human Q96NZ1's
GO:0000987 IDA is from PMID:22323600 (Y79 ChIP), which is the same mouse paper; that is the
source of the mouse ISO/IEA GO:0000987 rows, so they add no independent evidence but are
consistent.
