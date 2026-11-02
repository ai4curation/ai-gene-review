# Msed_1375 (A4YGI1) notes: carboxyltransferase (gamma) subunit of acetyl-CoA/propionyl-CoA carboxylase

Automated deep research was unavailable for this gene (no `-deep-research-*.md` file). These notes
come from my own literature search (Europe PMC, cached papers in `publications/`) and the UniProt
record. Session date 2026-11-01.

## Identity

- UniProt A4YGI1 (TrEMBL), 524 aa, locus Msed_1375. Name "Acetyl-CoA carboxylase carboxyltransferase
  subunit alpha / ... beta / propionyl-CoA carboxylase carboxyltransferase subunit"; keyword Transferase.
- CoA carboxyltransferase N-terminal (PS50980, 10-267) and C-terminal (PS50989, 271-506) domains; Pfam
  Carboxyl_trans (PF01039); crotonase-fold; PANTHER PTHR43842:SF2 (propionyl-CoA carboxylase beta chain).
  This is a single-chain fusion of the AccD-like and AccA-like CT halves, as in PCC beta subunits.
  [file:METS5/Msed_1375/Msed_1375-uniprot.txt]
- Encoded away from the Msed_0147-Msed_0148 pair.

## The enzyme

- Gamma subunit (57 kDa) = carboxytransferase of the purified M. sedula acetyl-CoA/propionyl-CoA
  carboxylase, which acts equally on both acyl-CoAs [PMID:12581213 "The enzyme consists of two large subunits of 57 kDa each representing biotin carboxylase (alpha) and carboxytransferase (gamma), respectively, and a small 18.6 kDa biotin carrier protein (beta)."].
- A. brierleyi ortholog: acyl-CoA and carboxybiotin binding sites in the CT subunit [PMID:12533469 "The acyl-CoA-binding site and the carboxybiotin-binding site were found in the carboxyltransferase subunit."].
  So the CT subunit determines the dual acetyl-/propionyl-CoA substrate range.
- Induced autotrophically [PMID:24532060 "especially the genes encoding acetyl-CoA/propionyl-CoA carboxylase (ACCαβγ) (Msed_0147, Msed_0148, Msed_1375; 7- to 30-fold)"].
- Part of E1 expressed in P. furiosus [PMID:23530213 "E1 (acetyl/propionyl-CoA carboxylase, encoded by Msed_0147, Msed_0148, and Msed_1375)"].

- Recombinant gamma made in E. coli was insoluble and inactive, and an earlier attempt to add
  E. coli-made gamma to the native enzyme changed nothing [PMID:27315782 "Hulger et al. expressed only the ACC-γ subunit in E. coli, and saw no change in activity when it was added to the purified native protein"].
  Active recombinant ACC (His-tag on the gamma N-terminus) was purified from P. furiosus co-expressing the
  M. sedula biotin protein ligase [PMID:27315782 "Recombinant ACC purified from MW112 cell extract (Table II) was functional"].

## Subunit-level function and GO

The CT subunit catalyses the second half-reaction: transfer of the carboxyl group from carboxybiotin-BCCP
to acetyl-CoA (EC 2.1.3.15 in the bacterial ACC nomenclature) or propionyl-CoA. GO has no specific term
for this acyl-CoA carboxytransferase half-reaction; the nearest correct parent is GO:0016743 carboxyl- or
carbamoyltransferase activity. (GO:0047154 methylmalonyl-CoA carboxytransferase activity is the
transcarboxylase reaction with pyruvate, a different reaction.)

GOA rows:
- GO:0004658 propionyl-CoA carboxylase activity (TreeGrafter, enables): the activity is real but belongs
  to the alpha-beta-gamma complex; the subunit contributes. MARK_AS_OVER_ANNOTATED. A NEW contributes_to
  row was added for GO:0003989. contributes_to GO:0004658 is recorded only in core_functions, because the
  validator treats a NEW row on a term already in GOA as a duplicate, whatever its qualifier. The TreeGrafter node also misses the acetyl-CoA activity, which in
  this archaeal enzyme is equal to the propionyl-CoA activity.
- GO:0016874 ligase activity (InterPro2GO from IPR011763): the subunit's own chemistry is a carboxyl
  transfer, not ATP-coupled ligation; ATP is consumed by the BC subunit. MODIFY to GO:0016743.
- NEW involved_in GO:0015977 carbon fixation.

## Open points

- NCBI esummary was down on 2026-11-01. The uncached PMIDs (12581213, 9973333, 12533469, 27315782)
  were cached with the repo's normal fetch pipeline, using metadata taken from efetch XML.
- I found no structure of an archaeal CT of this enzyme; the basis for the equal acetyl-/propionyl-CoA specificity is unknown.
