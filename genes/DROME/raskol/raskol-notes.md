# raskol (CG42684, Q8T498) curation notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: raskol is the closest experimentally characterised relative of AEDAE/A0A6I8TLE4
(same PANTHER subfamily PTHR10194:SF60). This review deliberately ignores any ProtNLM2 output.

### Deep research
- `just deep-research-falcon DROME raskol --fallback perplexity-lite` failed: falcon
  returned HTTP 403 Forbidden, and the perplexity-lite fallback also failed. No
  deep-research file exists. The review is based on the cached full text of PMID:30763317
  and PMID:25294944, the abstract of PMID:9619631 (gap-2), the UniProt record, and the
  PTHR10194 PAINT/entries files.

### Evolutionary placement
- PANTHER PTHR10194:SF60 "RAS GTPASE-ACTIVATING PROTEIN RASKOL"
  [file:DROME/raskol/raskol-uniprot.txt "DR   PANTHER; PTHR10194:SF60; RAS GTPASE-ACTIVATING PROTEIN RASKOL; 1."].
  Other SF60 members in `interpro/panther/PTHR10194/PTHR10194-entries.csv` are
  C. elegans gap-2 (Q8MLZ5), S. cerevisiae BUD2 (P33314), C. albicans BUD2 and
  Dictyostelium ngap (Q54Y08). Human RASAL2 is in SF52
  [file:human/RASAL2/RASAL2-uniprot.txt "DR   PANTHER; PTHR10194:SF52; RAS GTPASE-ACTIVATING PROTEIN NGAP; 1."].
  The mammalian homologues named in the fly paper (DAB2IP, RASAL2) are therefore
  not in the same subfamily, and no functions specific to their subfamilies were
  transferred.
- The PAINT IBDs (GO:0005096, GO:1902531) sit at the family root node PTN008939999.
  WB:WBGene00001516 (gap-2) is among the GO:1902531 donors.
- Catalytic residues: UniProt PRU00167 places the arginine finger at Arg515 (motif
  ...TFRGNSL...), and the FLR motif (SIFLRFLCPA, residues 527-536) is intact, so the
  domain is not obviously pseudo-GAP.
- The ISS donor for GO:0046580 is gap-2 (Q8MLZ5), which is in the same subfamily.
  gap-2 complements the S. pombe gap1 mutant, and gap-2 loss suppresses let-23/let-60
  reduction-of-function lethality [PMID:9619631 "GAP-2 appears to function as a negative regulator of LET-60 Ras during larval development."].
- The substrate is not uniform within SF60: Bud2 is the GAP for the Rap-like Rsr1/Bud1.
  For that reason the MF is kept at the general GO:0005096.

### Experimental data in Drosophila (all PMID:30763317 unless noted)
- Localisation (endogenous CPTI YFP trap): apical cortex of dividing embryonic cells
  [PMID:25294944 "This line has a striking localisation at the apical cortex of dividing cells"];
  apical membrane of the epidermis; membranes of BCs and PCs; colocalisation with DE-cad at
  the PC apical surface and BC-BC contacts, at amnioserosa contacts and at the DC zippering front;
  a cytoplasmic pool that is about 2x higher in PCs than in BCs.
- RNAi (one line, slbo-GAL4 or upd-GAL4, no rescue): reduced DE-cad at BC-BC contacts, BC
  cluster dissociation (63% with upd-GAL4), migration delay, delamination defects, and
  ectopic actin protrusions around the cluster with the number of front protrusions
  unchanged.
- Not shown: GAP activity, the substrate GTPase, epistasis with Ras/Rap/Rac.

### Decisions
- GO:0005096 IBA: ACCEPT (core; inferred).
- cytoplasm EXP/IEA: KEEP_AS_NON_CORE.
- plasma membrane, apical plasma membrane, apical cortex: ACCEPT.
- GO:0046580 ISS (from gap-2, same SF60): ACCEPT, flagged as inferred.
- GO:1902531 IBA: MODIFY to GO:0046580 (the general root-node term is refined to the descendant the gene already carries).
- Not added: border follicle cell migration (GO:0007298) and cell-cell junction /
  adherens junction. BC migration rests on a single RNAi line without rescue, and the
  junction evidence is only light-microscopy colocalisation. Both are raised as questions
  rather than asserted. FlyBase/UniProt took only localisation from PMID:30763317.

### For transfer to AEDAE/A0A6I8TLE4
Experimentally established in fly: localisation only (apical cortex, apical PM, PM at
DE-cad contacts, cytoplasm), plus RNAi phenotypes in BC adhesion and protrusion polarity.
Inferred, not measured in fly: GTPase activator activity and negative regulation of Ras
signalling.
