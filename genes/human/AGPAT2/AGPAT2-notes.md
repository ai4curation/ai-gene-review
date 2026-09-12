# AGPAT2 (LPAAT-beta) review notes

UniProt: O15120 (PLCB_HUMAN, "1-acyl-sn-glycerol-3-phosphate acyltransferase beta"),
gene symbol AGPAT2, HGNC:325, human (NCBITaxon:9606), 278 aa precursor.

## Core biology

AGPAT2 (also LPAAT-beta, 1-AGPAT 2) is an endoplasmic-reticulum multi-pass membrane
enzyme that catalyzes the second committed step of the glycerol-phosphate pathway of
glycerolipid biosynthesis: acylation of the sn-2 position of 1-acyl-sn-glycerol-3-phosphate
(lysophosphatidic acid, LPA) using a long-chain acyl-CoA to give 1,2-diacyl-sn-glycerol-3-phosphate
(phosphatidic acid, PA) plus CoA (EC 2.3.1.51).

- FUNCTION (UniProt): "Converts 1-acyl-sn-glycerol-3-phosphate (lysophosphatidic acid or LPA) into 1,2-diacyl-sn-glycerol-3-phosphate (phosphatidic acid or PA) by incorporating an acyl moiety at the sn-2 position of the glycerol backbone." [file:human/AGPAT2/AGPAT2-uniprot.txt]
- CATALYTIC ACTIVITY (UniProt, RHEA:19709, EC 2.3.1.51): "a 1-acyl-sn-glycero-3-phosphate + an acyl-CoA = a 1,2-diacyl-sn-glycero-3-phosphate + CoA". Evidence ECO:0000269 from PubMed:15629135, 19075029, 21873652, 9242711. [file:human/AGPAT2/AGPAT2-uniprot.txt]
- PATHWAY (UniProt): "Phospholipid metabolism; CDP-diacylglycerol biosynthesis; CDP-diacylglycerol from sn-glycerol 3-phosphate: step 2/3." PA is also the branch-point precursor for CDP-DAG, phospholipids (via de novo route), and diacylglycerol/triacylglycerol. [file:human/AGPAT2/AGPAT2-uniprot.txt]
- SUBCELLULAR LOCATION (UniProt): "Endoplasmic reticulum membrane {ECO:0000269|PubMed:21873652}; Multi-pass membrane protein". Two TRANSMEM helices (30-50, 122-142). [file:human/AGPAT2/AGPAT2-uniprot.txt]
- TISSUE SPECIFICITY (UniProt): "Expressed predominantly in adipose tissue, pancreas and liver." (major adipose LPAAT isoform). [file:human/AGPAT2/AGPAT2-uniprot.txt]
- Family (UniProt SIMILARITY): "Belongs to the 1-acyl-sn-glycerol-3-phosphate acyltransferase family." HXXXXD (98-103) catalytic motif and EGTR motif (172-175). [file:human/AGPAT2/AGPAT2-uniprot.txt]

## Disease

Biallelic loss-of-function AGPAT2 mutations cause congenital generalized lipodystrophy type 1
(CGL1 / Berardinelli-Seip), MIM:608594: "A form of congenital generalized lipodystrophy...
near complete absence of adipose tissue, extreme insulin resistance, hypertriglyceridemia,
hepatic steatosis and early onset of diabetes. Inheritance is autosomal recessive."
[file:human/AGPAT2/AGPAT2-uniprot.txt]. Disease gene established in PMID:11967537 (Agarwal et al.
Nat Genet 2002); CGL mutants have reduced enzyme activity (PMID:15629135).

## Key experimental evidence for catalytic activity / localization

- PMID:9242711 (Eberhardt et al., JBC 1997): cloning of human LPAAT; "Recombinant protein produced in COS 7 cells exhibited LPAAT activity with a preference for LPA as the acceptor phosphoglycerol and arachidonyl coenzyme A as the acyl donor." [PMID:9242711]. (This paper's expression-highest-in-liver-and-pancreas Northern is the historical basis; UniProt later says predominant in adipose/pancreas/liver.)
- PMID:9212163 (West et al., DNA Cell Biol 1997): cloned two human LPAAT cDNAs (LPAAT-alpha, LPAAT-beta = AGPAT2); "Expression of these two cDNAs in an Escherichia coli strain with a mutated LPAAT gene (plsC) complements its growth defect and shifts the equilibrium of cellular lipid content from LPA to PA". Also reports that overexpression correlated with enhanced TNF-alpha/IL-6 upon IL-1beta stimulation: "This increase in LPAAT activity correlates with enhancement of transcription and synthesis of tumor necrosis factor-alpha and interleukin-6 from cells upon stimulation with interleukin-1beta, suggesting LPAAT overexpression may amplify cellular signaling responses from cytokines." [PMID:9212163]. NOTE: this cytokine link is an overexpression correlation (indirect, speculative) -> basis for the BHF-UCL positive-regulation-of-cytokine annotations, which are over-annotations of a lipid enzyme.
- PMID:15629135 (Haque et al., BBRC 2005): CGL mutant enzymology; "The AGPATs catalyze acylation of lysophosphatidic acid (LPA) to phosphatidic acid (PA) during the biosynthesis of glycerophospholipids and triglycerides from glycerol-3-phosphate." Measured "conversion of [(3)H]LPA to [(3)H]PA in the presence of oleoyl-coenzyme A"; CGL mutants (G136R, 140delF, L228P) retained 15-40% activity, A239V ~90%. [PMID:15629135].
- PMID:19075029 (Zhao et al., JLR 2009): ALCAT1-focused study; abstract does not describe AGPAT2 assays explicitly (title/abstract about ALCAT1). GOA has AGPAT2 IDA GO:0003841 from this paper (curator read full text). Abstract-only cache -> cannot verify the AGPAT2-specific assay; ACCEPT (defer to curator, function is correct core MF).
- PMID:21873652 (Agarwal et al., JBC 2011): biochemical characterization of human AGPAT1/2 + ER localization; "When co-expressed, both isoforms co-localize to the endoplasmic reticulum." [PMID:21873652]. Also KM/Vmax kinetics in UniProt BIOPHYSICOCHEMICAL PROPERTIES. EXP source for GO:0005789 ER membrane and IDA GO:0003841.
- PMID:9461603 (Aguado & Campbell, JBC 1998): characterizes hLPAATalpha (the MHC class-III / chromosome 6 paralog AGPAT1, "G15"), NOT AGPAT2. "The amino acid sequence of the MHC-encoded human LPAAT (hLPAATalpha) is 48% identical to the recently described hLPAAT". GOA uses this as NAS for AGPAT2 MF/phospholipid-metabolism (family-level assertion). Correctly cited paper but describes the paralog -> keep NAS but note relevance; MF is correct at family level.

## Annotation review summary

Core, well-supported:
- GO:0003841 1-acylglycerol-3-phosphate O-acyltransferase activity (MF) - multiple IDA/IMP/IBA/IEA/TAS/NAS; ACCEPT experimental ones, ACCEPT redundant IEA/IBA (own core function).
- GO:0006654 phosphatidic acid biosynthetic process (BP) - IBA/IGI/TAS; ACCEPT.
- GO:0005789 endoplasmic reticulum membrane (CC) - EXP PMID:21873652 + TAS/IEA; ACCEPT. GO:0005783 ER (parent) IDA/IBA/ISS/IEA - ACCEPT/KEEP_AS_NON_CORE (membrane is more precise).
- GO:0016024 CDP-diacylglycerol biosynthetic process (BP) - IEA UniPathway; matches UniProt PATHWAY; KEEP_AS_NON_CORE (downstream branch role).
- GO:0008654 phospholipid biosynthetic process (BP) IEA InterPro; GO:0006644 phospholipid metabolic process NAS - correct but general parents; KEEP_AS_NON_CORE.
- GO:0016746 acyltransferase activity IEA InterPro - correct general parent of core MF; KEEP_AS_NON_CORE.
- GO:0016020 membrane IEA InterPro - correct general parent of ER membrane; KEEP_AS_NON_CORE.

Over-annotations / mislocalizations:
- GO:0001819 positive regulation of cytokine production (IMP PMID:9212163) - MARK_AS_OVER_ANNOTATED (experimental, keep; indirect overexpression correlation, not core lipid function).
- GO:0001961 positive regulation of cytokine-mediated signaling pathway (IC PMID:9212163) - MARK_AS_OVER_ANNOTATED (same basis).
- GO:0008544 epidermis development (IEA Ensembl, from rat ortholog) - MARK_AS_OVER_ANNOTATED (not a core AGPAT2 function; ortholog-transfer).
- GO:0009410 response to xenobiotic stimulus (IEA Ensembl, from rat ortholog) - MARK_AS_OVER_ANNOTATED.
- GO:0005886 plasma membrane (TAS Reactome R-HSA-6799350) - MARK_AS_OVER_ANNOTATED (neutrophil-degranulation pathway propagation; enzyme is ER).
- GO:0035579 specific granule membrane (TAS Reactome R-HSA-6799350) - MARK_AS_OVER_ANNOTATED (same neutrophil-degranulation propagation).

## Core functions selected
- MF: GO:0003841 1-acylglycerol-3-phosphate O-acyltransferase activity
- BP: GO:0006654 phosphatidic acid biosynthetic process
- CC (location): GO:0005789 endoplasmic reticulum membrane
</content>
</invoke>
