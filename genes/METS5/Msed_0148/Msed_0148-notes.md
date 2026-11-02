# Msed_0148 (A4YD23) notes: biotin carboxyl carrier protein (beta) subunit of acetyl-CoA/propionyl-CoA carboxylase

Automated deep research was unavailable for this gene (no `-deep-research-*.md` file). These notes
come from my own literature search (Europe PMC, cached papers in `publications/`) and the UniProt
record. Session date 2026-11-01.

## Identity

- UniProt A4YD23 (TrEMBL), 167 aa, "Biotin carboxyl carrier protein", locus Msed_0148, keyword Biotin.
- C-terminal biotinyl/lipoyl domain (PS50968, 83-167; CDD cd06850 biotinyl_domain; Pfam Biotin_lipoyl).
  PANTHER PTHR45266:SF3 (named after oxaloacetate decarboxylase alpha chain; the family groups
  biotin-carrier domains generally). [file:METS5/Msed_0148/Msed_0148-uniprot.txt]
- My own sequence inspection: the biotin-acceptor lysine is predicted at K133 in ...SIEAMKSETIV...
  (A-M-K-S instead of the canonical A-M-K-M). This matches the published observation that Sulfolobales
  BCCPs have serine after the biotinylated lysine [PMID:27315782 "While similar biotinylated proteins in both E. coli and P. furiosus have a methionine immediately C-terminal to the biotinylated lysine residue, S. tokodaii, M. sedula and the other Sulfolobales have a serine (Li et al. 2006) (Figure 2)."].
- GOA has no rows for this protein.

## The enzyme

- Beta subunit (18.6 kDa) of the M. sedula acetyl-CoA/propionyl-CoA carboxylase
  [PMID:12581213 "The enzyme consists of two large subunits of 57 kDa each representing biotin carboxylase (alpha) and carboxytransferase (gamma), respectively, and a small 18.6 kDa biotin carrier protein (beta)."].
- Autotrophic Sulfolobales contain large amounts of a small biotin-carrying protein
  [PMID:9973333 "They contained large amounts of a small biotin-carrying protein, which is most likely part of the acetyl-CoA and propionyl-CoA carboxylases."].
- A. brierleyi ortholog: biotin-binding site on the 20 kDa BCCP subunit [PMID:12533469 "the conserved biotin-binding site was located on the biotin carboxyl carrier protein"].
- M. sedula biotin protein ligase Msed_2010 biotinylates this subunit in vitro, and co-expressing it
  improved 3HP production in engineered P. furiosus [PMID:27315782 "M. sedula BPL (Msed_2010) was shown to biotinylate the β-subunit (biotin carboxyl carrier protein) of the ACC in vitro."].
- Recombinant ACC-beta made in E. coli was poorly biotinylated; with Msed_2010 co-expressed in
  P. furiosus the purified recombinant ACC was active [PMID:27315782 "Recombinant ACC purified from MW112 cell extract (Table II) was functional, although less active than the native enzyme with a specific activity of 0.65 µmol/min/mg compared to 3.2 µmol/min/mg for the native-purified enzyme (Hügler et al. 2003)."].
- Gene induced 7-30-fold autotrophically together with Msed_0147 and Msed_1375 [PMID:24532060 "especially the genes encoding acetyl-CoA/propionyl-CoA carboxylase (ACCαβγ) (Msed_0147, Msed_0148, Msed_1375; 7- to 30-fold)"].
- Expressed as part of E1 in P. furiosus (coupled E1αβ, Msed_0147-Msed_0148) [PMID:23530213].

## Subunit-level function and GO

BCCP carries the covalently bound biotin. BC carboxylates it, and the carboxybiotin arm moves to the
CT site, where the carboxyl group is transferred to acetyl-CoA or propionyl-CoA. BCCP thus supplies the
cofactor the reaction depends on: it does part of the work (the "cofactor" case in CLAUDE.md), so
`contributes_to` the overall activities and involvement in carbon fixation pass the participation test.

GO has no molecular-function term for "carboxyl carrier activity"; GO:0009374 biotin binding describes
non-covalent binding of free biotin and is not used for a covalently attached prosthetic group.
E. coli AccB is annotated `enables` GO:0003989 (IMP, IBA) and part_of GO:0009317. Here I use
`contributes_to` GO:0003989 and GO:0004658 (NEW, IDA from the purified complex, PMID:12581213) and
involved_in GO:0015977 carbon fixation. No CC term (see Msed_0147 notes on GO:0009317).

## Open points

- No direct experiment (mass spectrometry or mutagenesis) has located the biotinylated lysine in
  M. sedula BCCP; K133 is a sequence-based prediction.
- NCBI esummary was down on 2026-11-01. PMID:12581213, PMID:9973333, PMID:12533469 and PMID:27315782 were
  cached with the repo's normal fetch pipeline, using metadata taken from efetch XML.
