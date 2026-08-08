# CYP46A1 (Cholesterol 24-hydroxylase) — review notes

UniProt: Q9Y6A2 (CP46A_HUMAN). HGNC:2641. Gene on chromosome 14q32.1.
Source of most quotes below: `file:human/CYP46A1/CYP46A1-uniprot.txt` and cached publications.

## Identity and core function

- RecName: "Cholesterol 24-hydroxylase"; Short "CH24H"; EC 1.14.14.25. AltNames:
  Cholesterol 24-monooxygenase, Cholesterol 24S-hydroxylase, Cytochrome P450 46A1.
  [file:human/CYP46A1/CYP46A1-uniprot.txt "RecName: Full=Cholesterol 24-hydroxylase"]
- Member of the cytochrome P450 family (heme-thiolate monooxygenase).
  [file:human/CYP46A1/CYP46A1-uniprot.txt "Belongs to the cytochrome P450 family"]
- FUNCTION: "P450 monooxygenase that plays a major role in cholesterol homeostasis in
  the brain. Primarily catalyzes the hydroxylation (with S stereochemistry) at C-24 of
  cholesterol side chain, triggering cholesterol diffusion out of neurons and its
  further degradation" (PubMed:10377398, 14640697, 18621681, 25017465).
  [file:human/CYP46A1/CYP46A1-uniprot.txt "Primarily catalyzes the hydroxylation (with S"]
- Primary catalytic activity (RHEA:22716, EC 1.14.14.25): cholesterol + reduced
  [NADPH--hemoprotein reductase] + O2 = (24S)-hydroxycholesterol + oxidized reductase
  + H2O + H(+). [file:human/CYP46A1/CYP46A1-uniprot.txt "(24S)-hydroxycholesterol + oxidized [NADPH--hemoprotein reductase]"]

## Biological role: CNS cholesterol elimination

- CYP46A1 is the principal, rate-limiting route for eliminating cholesterol from the
  brain. 24S-hydroxycholesterol (24S-HC), unlike cholesterol, can cross membranes and
  the blood-brain barrier, is exported to plasma/liver and enters the bile-acid pathway.
  [PMID:10377398 "The turnover of cholesterol in the brain is thought to occur via
  conversion of excess cholesterol into 24S-hydroxycholesterol, an oxysterol that is
  readily secreted from the central nervous system into the plasma."]
- The reaction is also the first step in enzymatic degradation of brain cholesterol.
  [PMID:14640697 "This reaction produces biologically active oxysterol,
  24(S)-hydroxycholesterol, and is also the first step in enzymatic degradation of
  cholesterol in the brain."]
- Expressed predominantly in the brain; localized to neurons.
  [PMID:10377398 "Cholesterol 24-hydroxylase is expressed predominantly in the brain as
  judged by RNA and protein blotting."] and [PMID:10377398 "immunohistochemistry
  localize the expression of this P450 to neurons in multiple subregions of the brain."]
- 24S-HC is exported to the liver and converted to bile acids/salts; only a minor bile
  acid source but critical for disposing of excess brain cholesterol.
  [Reactome:R-HSA-193775 "24-hydroxycholesterol is synthesized in the brain, exported to
  the liver, and converted there to bile acids and bile salts. This pathway is only a
  minor source of bile acids and bile salts, but appears to be critical for the disposal
  of excess cholesterol from the brain"]

## Cellular localization

- SUBCELLULAR LOCATION: "Endoplasmic reticulum membrane ... Single-pass membrane
  protein. Microsome membrane ... Postsynapse ... Presynapse ... Cell projection,
  dendrite." All by similarity to mouse ortholog Q9WVK8.
  [file:human/CYP46A1/CYP46A1-uniprot.txt "Endoplasmic reticulum membrane"]
- One N-terminal transmembrane helix (residues 3-23), consistent with single-pass ER
  membrane anchoring. Original cloning localized both mouse and human enzymes to the ER.
  [PMID:10377398 "both proteins are localized to the endoplasmic reticulum"]
- N.B. the synaptic (pre-/postsynapse) and dendrite locations are ISS transferred from
  the mouse ortholog (Q9WVK8), not directly demonstrated for the human protein.

## Cofactor / structure

- Cofactor: heme (ChEBI:30413), experimentally established by crystallography
  (PubMed:18621681, 20667828, 23288837). Axial Fe ligand is Cys437 (heme-thiolate).
  [file:human/CYP46A1/CYP46A1-uniprot.txt "Name=heme; Xref=ChEBI:CHEBI:30413"]
- Multiple X-ray structures determined (2Q9F substrate-bound with cholesterol 3-sulfate;
  substrate-free 2Q9G; plus many drug/inhibitor co-complexes).
  [PMID:18621681 "the 1.9-A structure of CYP46A1 complexed with a high-affinity substrate
  cholesterol 3-sulfate"]

## Broad / secondary substrate specificity (in vitro; mostly non-core)

- Broad substrate specificity beyond cholesterol: further metabolizes
  24(S)-hydroxycholesterol to 24,25- and 24,27-dihydroxycholesterols; side-chain
  hydroxylation of 7alpha-hydroxycholesterol and cholestanol; ring hydroxylation of the
  C21-steroid hormones progesterone and testosterone; and xenobiotic metabolism.
  [PMID:14640697 "P450 46A1 was able to carry out side chain hydroxylations of two
  endogenous C27-steroids ... and introduce a hydroxyl group on the steroid nucleus of
  the C21-steroid hormones with the C4-C5 double bond (progesterone and testosterone)."]
  [PMID:14640697 "P450 46A1 was found to metabolize xenobiotics carrying out
  dextromethorphan O- and N-demethylations, diclofenac 4'-hydroxylation, and phenacetin
  O-deethylation."]
- Progesterone metabolism (progesterone -> 17alpha-hydroxyprogesterone; underlies the
  GO:0004508 steroid 17-alpha-monooxygenase RHEA IEA and GO:0042448 progesterone
  metabolic process IDA). [file:human/CYP46A1/CYP46A1-uniprot.txt "Reaction=progesterone
  + reduced [NADPH--hemoprotein reductase] + O2 ="]
- Testosterone hydroxylations at 6beta, 16beta, and 2-positions (underlie GO:0050649 and
  GO:0062184 RHEA/EXP). [file:human/CYP46A1/CYP46A1-uniprot.txt "16beta,17beta-dihydroxyandrost-4-en-3-one"]
- Oxidizes cholesterol precursors 7-dehydrocholesterol (to 24- and 25-hydroxy products)
  and desmosterol (epoxidation to (24S),25-epoxycholesterol and 27-hydroxylation);
  potentially relevant to Smith-Lemli-Opitz syndrome and desmosterolosis.
  [PMID:25017465 "P450 46A1 oxidizes 7-dehydrocholesterol to
  24-hydroxy-7-dehydrocholesterol and 25-hydroxy-7-dehydrocholesterol"]
  [PMID:25017465 "In the case of desmosterol, epoxidation to 24S,25-epoxycholesterol and
  27-hydroxylation was observed"]
- Metabolizes 4beta-hydroxycholesterol (further 24S-hydroxylation). The cited paper
  PMID:12077124 is primarily about CYP3A4-derived 4beta-hydroxycholesterol turnover; the
  CYP46A1 4beta-OH-cholesterol activity is captured in the UniProt catalytic-activity
  block (RHEA:46392, ECO:0000269|PubMed:12077124).
  [file:human/CYP46A1/CYP46A1-uniprot.txt "Reaction=4beta-hydroxycholesterol + reduced"]
- Clotrimazole is a substrate (basis of GO:0006805 xenobiotic metabolic process IDA
  from PMID:20667828). [PMID:20667828 "We show here that clotrimazole is also a substrate
  for CYP46A1."]

## Drug target / disease relevance (context; supports "non-core" framing of synaptic/LTP)

- CYP46A1 controls brain cholesterol turnover and is a drug target; several marketed
  drugs (voriconazole, tranylcypromine, etc.) inhibit it, and its structures underpin
  drug design. [PMID:20667828 "CYP46A1 initiates the major pathway of cholesterol
  elimination from the brain and thereby controls cholesterol turnover in this organ."]
- Loss of Cyp46a1 in mice reduces cerebral cholesterol turnover and impairs learning /
  hippocampal LTP (basis of the ISS/IEA regulation-of-LTP annotation, transferred from
  the mouse ortholog). [PMID:20667828 "CYP46A1 is important for memory and learning ...
  reduces cerebral cholesterol turnover and the production of the biosynthetic
  intermediate geranylgeraniol necessary for normal learning and hippocampal plasticity"]

## Review reasoning summary

- Core MF: cholesterol 24-hydroxylase activity (GO:0033781) — multiple EXP/IDA lines;
  the defining activity. heme binding (GO:0020037) and iron ion binding (GO:0005506) are
  core cofactor functions of this P450.
- Core BP: cholesterol catabolic process (GO:0006707) — IDA-supported "first step in
  cholesterol degradation in the brain".
- Core CC: endoplasmic reticulum membrane (GO:0005789) — single-pass ER membrane P450.
- steroid hydroxylase activity (GO:0008395, IDA) is a correct but broader parent of the
  physiological activity; retained but noted as a generalization.
- Promiscuous/in-vitro activities (testosterone 6beta/16beta-hydroxylase, steroid
  17-alpha-monooxygenase, progesterone/xenobiotic/C21-steroid processes) are real but
  non-core / over-annotations of a promiscuous P450 relative to its physiological role.
- Synaptic component (pre-/postsynapse, dendrite) and regulation-of-LTP annotations are
  ISS/IEA transferred from the mouse ortholog and kept as non-core.
- protein localization to membrane raft (GO:1903044, acts_upstream_of_negative_effect,
  ISS): indirect downstream effect of altered membrane cholesterol; kept as non-core.
</content>
</invoke>
