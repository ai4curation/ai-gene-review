# A0A8B6GS20 (Mytilus galloprovincialis, ORF MGAL_10B089004) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted.

### Identity: partial/fused gene model
- 607 aa TrEMBL entry, PE 3, from a WGS assembly (EMBL VDI68180.1). Only residues 362-588
  align to human MTMR9 Q96QG7 (residues 313-542; 41% of MTMR9, 60.4% identity). The PH-GRAM
  domain and the N-terminal half of the phosphatase-like domain are missing.
  [file:MYTGA/A0A8B6GS20/A0A8B6GS20-bioinformatics/RESULTS-rereview.md "A0A8B6GS20 (ORF MGAL_10B089004) is a partial MTMR9 gene model."]
- Residues 1-361 are three D8C_UMOD-type repeats (starting at 2, 174 and 272; Pfam
  PF23283 x2), an extracellular-protein module unrelated to myotubularins. This looks like a
  gene-model fusion.
- Active site: VHGSEGFDTT aligns to MTMR6 VHCSDGWDRT, giving Gly at the catalytic Cys
  position and Thr at the Arg position. Human MTMR9 (IHGTEGTDST) and worm MTM-9 (IHGGDGLDST)
  have the same kind of change, so this is an MTMR9-type pseudophosphatase.
- The same genome has full-length MTMR9-type models from ORF MGAL_10B079678 (A0A8B6ENJ7,
  A0A8B6EPV9, A0A8B6EME1, A0A8B6ELH7). Each covers 98.7% of human MTMR9 and is 97.2%
  identical to the target's C-terminal 246 residues. That fits a haplotig or partial
  duplicate. None of these entries is reviewed, so there is no canonical Swiss-Prot product
  for the same gene.

### Phylogenetic placement
- PANTHER PTHR10807:SF73 (LD06050P). The only experimentally characterised member in the
  family review entries is C. elegans mtm-9 (Q965W9). Human, mouse and bovine MTMR9 are in
  SF56. The closest characterised relative by subfamily is therefore worm MTM-9.
- PAINT: the MTMR9 clade node PTN000086907 carries IRD (loss) of GO:0004438 and
  GO:0106018, with the active ancestor PTN008506586 as seed. The process GO:0046856 is
  retained (IBA from PTN008506586). Protein phosphatase binding and negative regulation of
  autophagy come from PTN002246859, seeded by human MTMR9 alone. Phosphatase activator
  activity (human EXP) was not propagated, and that omission is treated as deliberate.

### Literature
- Human: MTMR9 dimerises with MTMR6/7/8, increases their activity and sets substrate
  preference; the MTMR8/R9 complex inhibits autophagy [PMID:22647598 "Complex formation between the
  active myotubularins and MTMR9 increases their catalytic activity and alters
  their substrate specificity"]. MTMR9 also stabilises MTMR6 [PMID:19038970].
- Worm: [PMID:14565969 "We demonstrate that MTM-6 and MTM-9 function as part of a complex to
  regulate an endocytic pathway that involves the Arf6 GTPase"]; [PMID:21076391 "MTM-6 and MTM-9
  are myotubularin lipid phosphatases that function as a complex to
  dephosphorylate phosphatidylinositol-3-phosphate"].

### Decisions (changes from the earlier draft)
- cytoplasm: ACCEPT (unchanged), with a gene-model caveat.
- negative regulation of autophagy: MARK_AS_OVER_ANNOTATED changed to KEEP_AS_NON_CORE.
  The PAINT node is legitimate. The evidence comes from vertebrate MTMR8/R9 only and is a
  downstream regulatory outcome; the invertebrate work concerns endocytic traffic.
- protein phosphatase binding: ACCEPT changed to MODIFY, with GO:0019902 phosphatase binding as
  the replacement. The partners are lipid phosphatases, not phosphoprotein phosphatases. This is
  consistent with the human MTMR9 review, which left the partner-class question UNDECIDED.
- phosphatidylinositol dephosphorylation: MODIFY (to regulation of) changed to ACCEPT. MTMR9 is
  the noncatalytic regulatory subunit of the phosphatase complex (scaffold-type participation),
  and PAINT deliberately kept the process while negating the activities. This is consistent
  with the human MTMR9 review, which ACCEPTs the same IBA.
- The description was rewritten to state the fusion/partial-model identity. The earlier
  Golgi/ERGIC recruitment claims were dropped because they are not supported by the cited
  primary papers.

### Relative to review next
- C. elegans mtm-9 (Q965W9): same PANTHER subfamily SF73 and experimentally characterised.
  The repo has no review for it.
- Family review interpro/panther/PTHR10807: its SF73 entry lists only this mussel protein
  as representative. It should add worm mtm-9 Q965W9, which PANTHER also places in SF73.
  Its open question about the "mussel target's catalytic-site status" is resolved: the
  MTMR9-type inactive motif is present. There is no disagreement on subfamily placement.
- modules/: no myotubularin or MTMR9 module exists.
