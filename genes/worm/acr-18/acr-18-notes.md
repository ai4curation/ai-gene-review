# acr-18 review notes

## Session 1 (2026-10-28)

- `just fetch-gene worm acr-18` resolved G5EG72 (WormBase F28F8.1,
  WBGene00000057, GeneID 191604); 18 GOA rows, all IBA/IEA. No experimental
  GO rows exist for this gene.
- `just fetch-gene-pmids` found no PMIDs in GOA. Cached PMID:23577128
  (Sherlekar et al. 2013, full text) by hand; plus PMID:14696039 (abstract only)
  and PMID:17503100 (family nomenclature). PubMed searches found no other
  primary acr-18 paper. No deep-research API keys; literature summary in
  `acr-18-deep-research-manual.md`.
- Sequence: Cys-loop pair C155/C169 and vicinal C219-C220 (loop C) so an
  alpha-type subunit [file:worm/acr-18/acr-18-uniprot.txt sequence].
- Function: ACR-18-containing receptor in AVA mediates cholinergic
  PVY/PVX -> AVA transmission that drives male reversal during mating; rescue
  from the nmr-1 promoter [PMID:23577128 "These data suggest that PVY+PVX-induced
  reversal depends on an ACR-18-containing cholinergic receptor that functions in
  nmr-1-expressing cells"].
- Ligand caveat: ACR-18 is a DEG-3-group subunit [PMID:23577128 "acr-18, which
  encodes a DEG-3 type acetylcholine receptor"]; agonist never measured. Kept
  the IBA contributes_to GO:0022848 (the cholinergic genetics support it) and
  refined the generic channel IEA rows to it, but raised the ligand as a
  suggested question.
- Decisions: MF IEA rows -> MODIFY to GO:0022848; generic transport rows ->
  GO:0098655 monoatomic cation transmembrane transport; regulation of membrane
  potential and regulation of postsynaptic membrane potential -> GO:0060079
  (verified with OAK that GO:0060079 is_a GO:0060078 is_a GO:0042391);
  membrane -> plasma membrane; synapse -> postsynapse (OAK: GO:0098794 is_a
  GO:0045202). Calcium ion transport IBA left UNDECIDED (no Ca2+ permeability
  data for ACR-18 or verified for the DEG-3 group).
- No NEW terms proposed. The mating-behaviour phenotype (male reversal) is
  necessity evidence for a behaviour; the receptor's own work is captured by
  cholinergic synaptic transmission.
