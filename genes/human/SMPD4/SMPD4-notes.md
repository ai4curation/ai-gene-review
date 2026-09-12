# SMPD4 (nSMase3 / neutral sphingomyelinase 3) — review notes

UniProt: Q9NXE4 (NSMA3_HUMAN). Gene: SMPD4 (HGNC:32949). Synonyms: KIAA1418, SKNY, NET13.
866 aa; MW ~97.8 kDa. EC 3.1.4.12.

## Identity / family
- Sphingomyelin phosphodiesterase 4 = neutral sphingomyelinase 3 (nSMase3/nSMase-3).
  [file:human/SMPD4/SMPD4-uniprot.txt "RecName: Full=Sphingomyelin phosphodiesterase 4"; "AltName: Full=Neutral sphingomyelinase 3"]
- NOT a member of the SMPD2/SMPD3 (nSMase1/nSMase2) extended-calcineurin-like family; distinct
  fold, "shows only a little homology to nSMase1 and -2."
  [PMID:16517606 "a novel human sphingomyelinase, nSMase3, that shows only a little homology to nSMase1 and -2"]
  Magini review: "although nSMase-3 ... has no significant sequence homology with other sphingomyelinases".
  [PMID:31495489 "has no significant sequence homology with other sphingomyelinases"]
- InterPro IPR024129 (Sphingomy_SMPD4); Pfam PF14724 (mit_SMPDase); PANTHER PTHR12988.
  [file:human/SMPD4/SMPD4-uniprot.txt "InterPro; IPR024129; Sphingomy_SMPD4"]

## Molecular function (core)
- Catalyzes hydrolysis of sphingomyelin → phosphocholine + ceramide (EC 3.1.4.12).
  [file:human/SMPD4/SMPD4-uniprot.txt "Catalyzes the hydrolysis of membrane sphingomyelin to form phosphorylcholine and ceramide"]
  Reaction (Rhea:19253): "a sphingomyelin + H2O = phosphocholine + an N-acylsphing-4-enine + H(+)"; EC=3.1.4.12.
  [file:human/SMPD4/SMPD4-uniprot.txt "Reaction=a sphingomyelin + H2O = phosphocholine"]
- Mg2+-dependent, pH optimum 7.0; activated by phosphatidylserine and TNF; inhibited by scyphostatin.
  [PMID:16517606 "nSMase3 is Mg2+-dependent and shows optimal activity at pH 7, which is enhanced in the presence of phosphatidylserine and inhibited by scyphostatin"]
  Cofactor Mg(2+). [file:human/SMPD4/SMPD4-uniprot.txt "Name=Mg(2+)"]
- Enzyme activity independently confirmed in skeletal muscle: constitutive Mg2+-dependent nSMase
  activity; nSMase3a (88 kD, full length) is catalytically active.
  [PMID:25180167 "We demonstrate constitutive nSMase activity in skeletal muscles of"; "GFPnSMase3a is functionally active"]

### CAUTION — GO:0050290 is the WRONG MF term for SMPD4
- GOA carries many `GO:0050290 sphingomyelin phosphodiesterase D activity` annotations (IBA, IEA-InterPro,
  IEA-GO_REF:2, IDA PMID:25180167, IDA PMID:16517606). GO:0050290 = EC 3.1.4.41, SMase **D**, reaction
  "sphingomyelin = ceramide 1-phosphate + choline" (a phospholipase-D-type cleavage found in venom/bacteria).
- SMPD4 is a type-**C** sphingomyelinase (EC 3.1.4.12), reaction "sphingomyelin = ceramide + phosphocholine".
  UniProt states EC=3.1.4.12 explicitly. [file:human/SMPD4/SMPD4-uniprot.txt "EC=3.1.4.12"]
- The correct GO MF term is **GO:0004767 sphingomyelin phosphodiesterase activity** (EC:3.1.4.12; verified in go.db).
- Therefore GO:0050290 annotations are MODIFY → GO:0004767. The experimental (IDA/EXP) ones are not removed
  (they demonstrate the real phosphocholine-releasing activity); the term label is just wrong.
- This is a known family-wide GO curation artifact: nSMases are recurrently mis-mapped to the SMase-D term.

## Subcellular location
- ER membrane (single-pass / C-tail-anchored), Golgi apparatus membrane.
  [PMID:16517606 "Cellular localization studies with hemagglutinin-tagged nSMase3 demonstrated colocalization with markers of the endoplasmic reticulum as well as with Golgi markers"]
  [file:human/SMPD4/SMPD4-uniprot.txt "Endoplasmic reticulum membrane"; "Golgi apparatus membrane"; "Single-pass membrane protein"]
- C-tail-anchored: TM helix 822-842, close to C-terminus, no N-terminal signal peptide.
  [PMID:16517606 "contains a 23-amino-acid transmembrane domain close to the C terminus, which is indicative for the family of C-tail-anchored integral membrane proteins"]
- Outer nuclear envelope / ER; interacts with nuclear pore complex proteins (identified as NET13).
  [PMID:31495489 "Overexpression of human Myc-tagged SMPD4 showed localization both to the outer nuclear envelope and the ER and additionally revealed interactions with several nuclear pore complex proteins by proteomics analysis"]
  [PMID:31495489 "SMPD4 was identified as nuclear envelope transmembrane protein-13, NET13"]
- ER localization confirmed in cancer cells; C-terminal TM/ER-targeting deletion partly alters ER
  compartmentalization. [PMID:18505924 "reveals nSMase3 to localize to the endoplasmic reticulum (ER)"]
- In skeletal muscle also at internal and sarcolemmal membranes (mouse/human muscle).
  [PMID:25180167 "By immunofluorescence microscopy, nSMase3 resides in both internal and sarcolemmal membranes"]
  Sarcolemma annotation in GOA is ISS from mouse ortholog Q6ZPR5; UniProt: "Cell membrane, sarcolemma {ECO:0000250|UniProtKB:Q6ZPR5}".
- NOTE: neither nSMase3 variant is detected in the cytosol. [PMID:25180167 "neither variant is detected in the cytosol"]

## Biological process
- Sphingomyelin catabolism → ceramide biosynthesis (salvage/turnover); membrane sphingolipid homeostasis.
  [file:human/SMPD4/SMPD4-uniprot.txt "has a relevant role in the homeostasis of membrane sphingolipids"]
- ER organization / ER–nuclear-envelope crosstalk; loss causes ER cisternae abnormalities, ER stress,
  autophagy, and delayed cell-cycle (mitotic) progression.
  [PMID:31495489 "Fibroblasts from affected individuals showed ER cisternae abnormalities, suspected for increased autophagy, and were more susceptible to apoptosis under stress conditions, while treatment with siSMPD4 caused delayed cell cycle progression"]
  [PMID:31495489 "SMPD4 links homeostasis of membrane sphingolipids to cell fate by regulating the cross-talk between the ER and the outer nuclear envelope"]
- Stress response: expression induced by DNA damage (Adriamycin) and by TNF; sensitizes cells to
  DNA-damage-induced apoptosis (proapoptotic).
  [PMID:18505924 "Treatment with genotoxic Adriamycin and nongenotoxic tumor necrosis factor-alpha up-regulates endogenous nSMase3 expression"]
  [PMID:18505924 "Overexpression of exogenous nSMase3 sensitizes cells to Adriamycin-induced cell killing"]
- Cellular response to TNF: TNF stimulates rapid nSMase3 activation (peak ~1.5 min in MCF7).
  [PMID:16517606 "Tumor necrosis factor stimulates rapid activation of nSMase3 in MCF7 cells with peak activity at 1.5 min"]
- Skeletal-muscle redox signaling: nSMase3 is required for TNF-stimulated cytosolic oxidant production
  (nSMase3a sufficient). By similarity in human UniProt FUNCTION ("mediates TNF-stimulated oxidant production").
  [PMID:25180167 "nSMase3 acts as a signaling nSMase in skeletal muscle that is essential for TNF-stimulated oxidant activity"]

### On "glycerophospholipid catabolic process" (GO:0046475)
- Sphingomyelin is a phosphosphingolipid, NOT a glycerophospholipid (its backbone is sphingosine, not glycerol).
  SMPD4's substrate is sphingomyelin; there is no evidence it hydrolyzes glycerophospholipids.
- GO:0046475 is an IDA (PMID:16517606, BHF-UCL) and an IBA. It is an over-annotation / mis-classification of
  the sphingomyelinase reaction under the wrong lipid class. Mark as over-annotated (do not remove the IDA per policy).

## Disease
- NEDMABA: Neurodevelopmental disorder with microcephaly, arthrogryposis, and structural brain anomalies
  (MIM:618622); autosomal recessive, bi-allelic loss-of-function SMPD4 variants.
  [file:human/SMPD4/SMPD4-uniprot.txt "Neurodevelopmental disorder with microcephaly, arthrogryposis, and structural brain anomalies (NEDMABA)"]
  [PMID:31495489 "Genomic analysis revealed bi-allelic loss-of-function variants in SMPD4"]

## Tissue / expression
- Widely expressed; highest in heart and skeletal muscle. [file:human/SMPD4/SMPD4-uniprot.txt "highest levels in heart and skeletal muscle"]
- nSMase3 mRNA most abundant nSMase in diaphragm. [PMID:25180167 "nSMase3 (Smpd4 gene) mRNA is highly expressed in muscle"]

## Isoforms
- 10 isoforms by alternative splicing. Isoform 1 = nSMase3a (full length, exon 11 retained, 88 kD, active);
  isoform 2 = nSMase3b (lacks exon 11, 85 kD). [file:human/SMPD4/SMPD4-uniprot.txt "Name=1; Synonyms=nSMase3a"; "Name=2; Synonyms=nSMase3b"]
  [PMID:25180167 "the 88 kD protein is nSMase3a and the 85 kD protein is nSMase3b"]

## Annotation action summary (rationale)
- Core MF: GO:0004767 sphingomyelin phosphodiesterase activity (EC 3.1.4.12) + GO:0046872 metal ion binding (Mg2+, KW/cofactor).
- GO:0050290 (SMase D) → MODIFY to GO:0004767 (wrong reaction/EC; see caution above).
- Core BP: GO:0006685 sphingomyelin catabolic process; GO:0046513 ceramide biosynthetic process (paired products of one reaction).
- Core CC: ER membrane (GO:0005789), Golgi membrane/apparatus, nuclear envelope / outer nuclear membrane.
- GO:0046475 glycerophospholipid catabolic process → MARK_AS_OVER_ANNOTATED (sphingomyelin is not a glycerophospholipid).
- GO:0007029 ER organization (IMP) and GO:0071356 cellular response to TNF (IDA) → ACCEPT (non-core/regulatory but experimentally supported).
- trans-Golgi network (GO:0005802): IDA from overexpression; keep as non-core (steady-state ER/Golgi more central).
