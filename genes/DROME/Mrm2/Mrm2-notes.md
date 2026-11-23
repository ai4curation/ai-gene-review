# Mrm2 (Q9VDT6, CG11447, FBgn0038737) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 predictions were not consulted for this re-review.

### Identity
- Q9VDT6 is the reviewed Swiss-Prot entry MRM2_DROME, 250 aa, sequence version 1, the single
  FlyBase product (FBpp0083225, CG11447-RA). It is the canonical full-length product, not an isoform,
  fragment or alternative gene model. It has a predicted 1-35 mitochondrial transit peptide
  (ECO:0000255), the FtsJ domain (PF01728), HAMAP MF_01547 and the RlmE family signature
  (IPR015507).
- Catalytic check (`Mrm2-bioinformatics/RESULTS-rereview.md`): the RlmE active-site lysine
  (E. coli K164) maps to fly K201, and all five experimentally defined RlmE SAM-binding residues
  are conserved. No sign of a pseudoenzyme.

### Evolutionary placement
- PANTHER PTHR10920:SF18 "RRNA METHYLTRANSFERASE 2, MITOCHONDRIAL". In the family inventory
  (`interpro/panther/PTHR10920/PTHR10920-entries.csv`) SF18 holds bacterial RlmE (E. coli P0C0R7,
  P. putida Q88DV0) and human MRM2 Q9UI43. Yeast TRM7 (P38238) is in SF12, a tRNA branch.
- PAINT (`PTHR10920-paint.tsv`): node PTN000100455 (taxon 2759) carries GO:0008650 (seeds
  yeast S000003104, E. coli P0C0R7, human Q9UI43), GO:0000027 (seeds include this fly gene,
  P0C0R7, Q9UI43) and GO:0031167; PTN000100456 carries GO:0005739. The fly gene in the
  GO:0000027 seed list is its own FlyBase IMP (expected, not circular).
- The PANTHER family review (`interpro/panther/PTHR10920/PTHR10920-review.yaml`) puts Mrm2 in SF18,
  and so does UniProt. No disagreement over subfamily placement.

### Literature
- The only fly experimental paper is PMID:35177605 (Rebelo-Guiomar et al. 2022, full text cached).
  Human MRM2 knockout: mtLSU assembly stalls at a late checkpoint; catalytic-dead MRM2 rescues
  assembly ("The catalytic activity of MRM2 is dispensable for mtLSU biogenesis"). Fly: ubiquitous
  RNAi (da-GAL4) gives developmental delay and late-pupal lethality, and lower respiratory-chain
  subunit levels in late pupae. Pan-neuronal knockdown is lethal; pan-muscle knockdown impairs
  climbing.
- The fly experiments did not directly measure mitoribosome assembly, rRNA methylation or
  mitochondrial translation. The FlyBase IMP for GO:1902775 therefore rests on a fly phenotype
  read together with the human mechanism. I keep it, deferring to the curator, because the
  orthology (SF18 plus the PTN000100455 node) and the reduced respiratory-chain subunits are
  consistent with it.
- The human site (Um3039 in 16S mt-rRNA in the 2022 paper's numbering; UniProt quotes Um1579)
  should not be transferred as a fly coordinate.
- PMID:25009282 (Rorbach 2014, MRM2/MRM3 in human mtLSU biogenesis) is cited by UniProt but is
  not in the publications cache, so I did not cite it.

### Decisions
- GO:0000027 IBA: MODIFY to GO:1902775 (mitochondrial LSU assembly), a term the gene already carries.
- GO:0005739 (IBA/IEA/ISS): ACCEPT. Organelle-level localisation is what the transit peptide and
  orthology support. The matrix (IC) row is also accepted as the more precise compartment.
- GO:0006364 rRNA processing ISS: MODIFY to GO:0031167 rRNA methylation. The general term is
  entailed by the specific methylation process the gene already carries. (Earlier review: ACCEPT.)
- GO:0008168 IEA: MODIFY to GO:0008650.
- GO:0008650 (IBA/IEA/ISS x2): ACCEPT. Same subfamily as the characterised enzymes, conserved
  catalytic residues.
- GO:0031167 IBA: ACCEPT.
- GO:1902775 IMP: ACCEPT (see the caveat above).
- No NEW terms. Mitochondrial translation is a downstream consequence of assembly (necessity),
  and organismal developmental phenotypes are not process participation.

### Relative
- Closest experimentally characterised relative: human MRM2 (Q9UI43), in the same PANTHER subfamily
  SF18, with seeds under the same eukaryotic PAINT node PTN000100455. No review exists in
  genes/human/. E. coli RlmE P0C0R7 is the bacterial member of SF18 and has no review either;
  P. putida rlmE (genes/PSEPK/rlmE, Q88DV0) is DRAFT.

### Modules
- No module under modules/ references Mrm2, MRM2, Q9VDT6 or Q9UI43. The only grep hits were
  unrelated deep-research artifacts.
- Related context module: `modules/dmel_mitochondrial_ribosome.yaml` (FlyBase MRP group; DRAFT).
  Mrm2 is not one of its parts. It is an assembly factor and rRNA-modifying enzyme acting on the
  mtLSU, not a ribosomal subunit, so it correctly stays outside the complex membership.
