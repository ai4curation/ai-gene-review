# ERP27 (C12orf46, ERp27) research notes

UniProt Q96DN0. ER-lumenal, non-catalytic PDI-family member. 273 aa, ER-retention motif (KVEL/270-273).

## Core function
- NON-CATALYTIC: lacks CXXC active-site motif -> redox-inactive PDI-family member.
  - [file:human/ERP27/ERP27-uniprot.txt "Does not contain a CXXC active site motif indicating that it is a catalytically redox-inactive member of the protein disulfide isomerase family."]
- Binds unfolded proteins via a hydrophobic pocket in its C-terminal (b'-like) domain, distinguishing folded vs unfolded.
  - [file "Specifically binds unfolded proteins and may recruit protein disulfide isomerase PDIA3 to unfolded substrates"]
  - [PMID:23192347 "ERp27 is able to distinguish between folded and unfolded substrates, only interacting with the latter. ERp27 is up-regulated during ER stress, thus presumably allowing it to bind accumulating misfolded substrates and present them to ERp57 for catalysis."]
- Recruits/presents substrates to PDIA3/ERp57 (catalytic partner). PDIA3-binding site = residues 230-233 (E231/W232/D233 critical).
  - [PMID:16940051 "ERp27, a new non-catalytic endoplasmic reticulum-located human protein disulfide isomerase family member, interacts with ERp57."]
- Homologous to non-catalytic b and b' domains of PDI; binds Delta-somatostatin (PDI test peptide).
- ER stress-induced. Pancreas-enriched (HPA tissue enriched pancreas).

## Localization
- ER lumen [file "SUBCELLULAR LOCATION: Endoplasmic reticulum lumen"].

## Action plan
- protein folding (GO:0006457) IBA - KEEP_AS_NON_CORE (assists folding as chaperone/substrate-presenter, not a foldase; downstream).
- NOT|protein disulfide isomerase activity (GO:0003756) IBA negated - ACCEPT (correct, lacks CXXC).
- ER lumen (GO:0005788) IEA + EXP - ACCEPT.
- protein binding (many IPI) - the FUNCTIONAL one (substrate/unfolded-protein binding, PDIA3 recruitment) is core but these GOA protein binding entries are mostly HT interactome (SGTA/EEF1D/UBQLN/HTT etc), not PDIA3. KEEP_AS_NON_CORE. Note PDIA3 interaction itself is NOT in GOA protein-binding rows (those are HT partners). Core MF captured as unfolded protein binding (GO:0051082) and protein-folding chaperone binding.
- Core MF proposals: unfolded protein binding (GO:0051082); chaperone role presenting substrates to ERp57.
