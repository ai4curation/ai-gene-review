# NT5C1A (Cytosolic 5'-nucleotidase 1A / cN-IA) review notes

UniProt: Q9BXI3 (5NT1A_HUMAN). HGNC:17819. Gene ID 84618. Chromosome 1. 368 aa.

## Identity and family

- RecName: Cytosolic 5'-nucleotidase 1A; short cN1A / cN-IA / cN-I
  [file:human/NT5C1A/NT5C1A-uniprot.txt "RecName: Full=Cytosolic 5'-nucleotidase 1A"].
- Belongs to the 5'-nucleotidase type 3 family (haloacid dehalogenase-like phosphatase fold)
  [file:human/NT5C1A/NT5C1A-uniprot.txt "Belongs to the 5'-nucleotidase type 3 family."].
- Active-site nucleophile at residue 211 (by similarity; ACT_SITE 211 "Nucleophile" in UniProt FT).
- Pfam PF06189 (5-nucleotidase), InterPro IPR010394, PANTHER PTHR31367:SF2
  "CYTOSOLIC 5'-NUCLEOTIDASE 1A".

## Enzymatic function

- Catalyzes hydrolysis of ribonucleotide and deoxyribonucleotide 5'-monophosphates,
  releasing inorganic phosphate + the corresponding nucleoside
  [file:human/NT5C1A/NT5C1A-uniprot.txt "FUNCTION: Catalyzes the hydrolysis of ribonucleotide and"].
- AMP is the major/preferred substrate; also hydrolyzes dCMP and IMP
  [file:human/NT5C1A/NT5C1A-uniprot.txt "AMP is the major substrate but can"].
- EC 3.1.3.5 (5'-nucleotidase), EC 3.1.3.89 (5'-deoxynucleotidase), EC 3.1.3.99 (IMP-specific).
- Recombinant human enzyme: "high affinity toward dCMP and lower affinity toward AMP and IMP.
  ADP was necessary for maximal catalytic activity."
  [PMID:11133996 "The recombinant cN-I showed high affinity toward dCMP and lower affinity toward AMP and IMP. ADP was necessary for maximal catalytic activity."].
- Note on substrate preference: kinetic parameters differ between the recombinant-enzyme study
  (Hunsucker 2001; high affinity for dCMP) and the tissue/heart studies (Tavenier 1995,
  Skladanowski 1996) which characterize an "AMP-preferring" (N-I) activity in myocardium
  [PMID:8967393 "the AMP-preferring one (N-I, 107 +/- 61 mU/g,"]. The UniProt consensus is that
  AMP is the major substrate. cN-IA (N-I) is AMP-preferring while cN-II (N-II) is IMP-preferring
  [PMID:8967393 "Cytoplasmic IMP-preferring 5'-nucleotidase"].
- Cofactor: Mg(2+) [file:human/NT5C1A/NT5C1A-uniprot.txt "Name=Mg(2+); Xref=ChEBI:CHEBI:18420;"],
  measured biochemically in human heart enzyme (Skladanowski 1996, IDA GO:0000287).
- Allosterically activated by ADP
  [file:human/NT5C1A/NT5C1A-uniprot.txt "Activated by ADP."],
  [PMID:11133996 "ADP was necessary for maximal catalytic activity."].
- pH optimum 7.0 (Skladanowski 1996, UniProt BIOPHYSICOCHEMICAL PROPERTIES).

## Biological role

- Regulates adenosine production during AMP catabolism / ATP breakdown, prominently in
  skeletal muscle and heart. In ischemic heart, intracellular AMP hydrolysis by cytosolic
  5'-nucleotidase generates physiologically relevant adenosine
  [PMID:8967393 "Intracellular AMP hydrolysis probably produces sufficient adenosine in ischemic"],
  [PMID:8967393 "cytosolic 5'-nucleotidase activity in human heart can easily account for adenosine"].
- Comparative kinetics of purine-degradation / salvage enzymes (including AMP- and IMP-specific
  5'-nucleotidases) in human vs rat myocardium
  [PMID:7599155 "AMP- and IMP-specific 5'-nucleotidases, adenosine"],
  [PMID:7599155 "Pathways producing and converting adenosine have hardly been investigated in"].
- Central role in regulating the purine nucleotide pool in skeletal muscle, preferentially
  converting AMP to adenosine
  [PMID:34814800 "plays a central role in the regulation of"],
  [PMID:34814800 "preferentially converting adenosine monophosphate to adenosine."].
- Also implicated in physiological pyrimidine nucleotide pool regulation and in nucleoside-analog
  (chemotherapy) resistance via dephosphorylation of drug monophosphates
  [PMID:11133996 "may play an important role in the regulation of physiological pyrimidine"],
  [PMID:11133996 "conferred resistance to"].

## Tissue distribution

- Highly expressed in skeletal muscle; intermediate in heart, brain, kidney, pancreas
  [file:human/NT5C1A/NT5C1A-uniprot.txt "Highly expressed in skeletal muscle."],
  [PMID:11133996 "It is expressed at a high level in skeletal and heart muscle,"].
- HPA: group enriched (skeletal muscle, tongue) (UniProt DR HPA line).

## Localization

- Cytoplasm / cytosol
  [file:human/NT5C1A/NT5C1A-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:7599155}."].
  UniProt attributes the location call to PubMed:7599155 (Tavenier 1995, ECO:0000305).

## Disease / autoantigen

- cN-IA is a prominent autoantibody target (anti-NT5C1A / anti-cN1A) in sporadic inclusion body
  myositis (sIBM). The Jedrzejewska 2022 paper studies it as an autoantigen and serum-activity
  biomarker in breast-cancer-associated muscle inflammation
  [PMID:34814800 "cN-IA can act as an autoantigen in muscle"]. (sIBM autoantigen role is
  established in the broader literature; the cached paper covers the paraneoplastic/BC context.)

## Protein interactions (high-throughput only)

- IntAct/interactome screens report binary interactions with NTAQ1 (Q96HA8) and CDC37 (Q16543):
  - PMID:25416956 (Rolland 2014, proteome-scale binary interactome) — NTAQ1
  - PMID:31515488 (Fragoza 2019, SNV interaction perturbation) — NTAQ1
  - PMID:32296183 (Luck 2020, HuRI reference binary interactome) — CDC37, NTAQ1
- These are systematic Y2H/binary-map "protein binding" (GO:0005515, IPI) annotations with no
  gene-specific functional characterization of NT5C1A; treated as uninformative for core function.
  UniProt INTERACTION also lists CDC37 (Q16543) and NTAQ1 (Q96HA8).

## Citation issue found

- GOA seeds several IDA/TAS annotations against `PMID:599155`, but PMID:599155 is a 1977
  J Biochem paper on Ehrlich-ascites acyltransferases (Waku & Nakazawa) — unrelated to NT5C1A.
  This is a transcription error for `PMID:7599155` (Tavenier 1995, "Kinetics of adenylate
  metabolism in human and rat myocardium"), the paper UniProt actually cites for 5'-nucleotidase
  activity and cytoplasmic location. The verbatim reference title check would fail against the
  wrong-paper title, so the review flags PMID:599155 as WRONG_IDENTIFIER and the affected
  annotations are UNDECIDED / handled via the correctly-attributed PMID:7599155 annotations.

## Core function synthesis

- MF: 5'-nucleotidase activity (GO:0008253) — AMP-preferring cytosolic 5'-nucleotidase; no more
  specific "AMP 5'-nucleotidase" MF term exists in GO (verified via OLS). Mg2+ cofactor
  (GO:0000287). 5'-deoxynucleotidase activity (GO:0002953) is a genuine measured secondary
  activity (dCMP/dNMP hydrolysis).
- BP: AMP catabolic process (GO:0006196), adenosine metabolic process (GO:0046085), and the
  broader purine/pyrimidine nucleotide catabolism (IMP/dAMP/dGMP catabolic processes).
- CC: cytosol (GO:0005829) / cytoplasm (GO:0005737).
</content>
</invoke>
