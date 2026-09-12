# SLC25A32 (MFT/MFTC) — review notes

UniProt: Q9H2D1 (S2532_HUMAN). Gene symbol SLC25A32; synonyms MFT, MFTC. Human, NCBI:txid9606.
315 aa, ~35.4 kDa, six-TM mitochondrial carrier with three Solcar repeats (SLC25 family, TC 2.A.29).

## Identity and family
- Member of the mitochondrial carrier (SLC25) family; three Solcar repeats and six predicted
  transmembrane helices [file:human/SLC25A32/SLC25A32-uniprot.txt "Belongs to the mitochondrial carrier (TC 2.A.29) family"; TRANSMEM 1..6; REPEAT Solcar 1/2/3].
- InterPro: IPR002067 (MCP), IPR018108 (MCP_transmembrane), IPR044712 (SLC25A32-like); PANTHER PTHR45683;
  Pfam PF00153 (Mito_carr x3). TCDB 2.A.29.10.2.

## Function — the key twist (folate vs FAD)
- **Originally identified as the mitochondrial FOLATE transporter (MFT).** Cloned by complementation of the
  glyB CHO glycine-auxotroph phenotype; restored folate accumulation in mitochondria
  [PMID:10978331 "reinstated folate accumulation in the mitochondria of transfected cells"].
- The glyB defect is a point mutation (Gly192Glu) in a predicted TM domain of the hamster mft, abolishing
  mitochondrial folate transport and creating a glycine requirement
  [PMID:15140890 "a point mutation in an inner mitochondrial membrane protein required for transport of folates into mitochondria"; "the glyB mft mutation identified a region of this mitochondrial folate carrier vital to its transport function"].
- **Later shown to function primarily as a mitochondrial FAD transporter.** MFT (SLC25A32) — but not the
  N111 candidate — complemented the yeast FLX1 (FAD carrier) mutant, identifying it as the human
  mitochondrial FAD transporter, with a proposed role in MADD-like disease
  [PMID:16165386 "only the previously described mitochondrial folate transporter (MFT) was able to functionally complement the FLX1 mutant"; "we report the identification of the human mitochondrial FAD transporter"].
- Mouse genetics decisively separated the two substrates: patient-derived knock-in and knockout mice showed
  that SLC25A32 disease mutations block mitochondrial FAD uptake, NOT folate uptake
  [PMID:35727412 "None of the Slc25a32 mutations hindered the mitochondrial uptake of folate. Instead, the mitochondrial uptake of flavin adenine dinucleotide (FAD) was specifically blocked"].
- Reduced matrix FAD impairs flavoenzymes (fatty-acid β-oxidation, amino-acid metabolism) and damages DLD
  (dihydrolipoamide dehydrogenase) of the glycine cleavage system, causing glycine accumulation, reduced
  glycine-derived formate, and downstream disruption of folate-mediated one-carbon metabolism
  [PMID:35727412 "a subunit of glycine cleavage system-dihydrolipoamide dehydrogenase damaged, resulting in glycine accumulation and glycine derived-formate reduction, which further disturbed folate-mediated one-carbon metabolism, leading to 5-methyltetrahydrofolate shortage"].
- UniProt captures this reappraisal explicitly:
  [file:human/SLC25A32/SLC25A32-uniprot.txt "Initially postulated to transport folate based on complementation evidence, but it was latter shown to rather function as a FAD transporter indirectly affecting folate levels and folate-mediated one-carbon metabolism in mitochondria"].
- UniProt FUNCTION: FAD translocation across the IMM into the matrix, "where it acts as a redox cofactor to
  assist flavoenzyme activities ... including fatty acid beta-oxidation, amino acid and choline metabolism
  as well as mitochondrial electron transportation. In particular, provides FAD to DLD dehydrogenase of the
  glycine cleavage system" [file:human/SLC25A32/SLC25A32-uniprot.txt].
- Transport reaction (NOT enzymatic catalysis): FAD(in) = FAD(out), Rhea:RHEA:76535
  [file:human/SLC25A32/SLC25A32-uniprot.txt "Reaction=FAD(in) = FAD(out); Xref=Rhea:RHEA:76535"].

## Interpretation for GO
- **Core MF = GO:0015230 FAD transmembrane transporter activity** (IMP PMID:35727412, IMP PMID:16165386,
  IBA GO_Central). This is the best-supported, most specific transporter activity.
- **Folate/folic acid transporter activity (GO:0008517, Reactome TAS)** reflects the original (now-superseded
  as *primary*) model. SLC25A32 does still influence mitochondrial folate levels — but indirectly, via FAD →
  one-carbon metabolism — and mouse data show its disease mutations do not block folate uptake itself. Keep as
  non-core (it is curator-asserted TAS; folate handling remains a real physiological association), not a REMOVE.
- **Nucleotide transport / nucleotide transmembrane transporter activity (GO:0006862, GO:0015215; IEA from
  InterPro/ARBA)** are over-general ancestors of the specific FAD (a flavin dinucleotide) activity — not the
  informative function. MARK_AS_OVER_ANNOTATED.

## Localization
- Mitochondrion inner membrane, multi-pass
  [file:human/SLC25A32/SLC25A32-uniprot.txt "Mitochondrion inner membrane"; "Multi-pass membrane protein"].
  Supported by IDA (PMID:29666258 mitochondrion; mutant retains mito localization), IGI (PMID:15140890),
  ISS, IBA, and Reactome TAS. Core CC = GO:0005743 mitochondrial inner membrane.
- Ubiquitous / low tissue specificity expression [file:human/SLC25A32/SLC25A32-uniprot.txt "Ubiquitous"].

## Disease
- **RREI — Exercise intolerance, riboflavin-responsive (MIM:616839), autosomal recessive**
  [file:human/SLC25A32/SLC25A32-uniprot.txt "Exercise intolerance, riboflavin-responsive (RREI)"].
  Variants (e.g. R147H, Y174C, K235R) reduce FAD transport / flavoenzyme (SDH, G3PDH) activity; riboflavin
  responsive [PMID:26933868 title "SLC25A32 Mutations and Riboflavin-Responsive Exercise Intolerance"; UniProt VARIANT notes].
- **NTD — Neural tube defects susceptibility (MIM:182940)** [file:human/SLC25A32/SLC25A32-uniprot.txt
  "Neural tube defects (NTD)"]. Slc25a32 knockout mice die in utero with folate-resistant cranial NTDs
  rescued by formate; a biallelic LOF human NTD case was found
  [PMID:29666258 "gene trap inactivation of Slc25a32 (Mft) in mice induces NTDs that are folate (5-methyltetrahydrofolate, 5-mTHF) resistant yet are preventable by formate supplementation"; "identified biallelic loss of function SLC25A32 variants in a cranial NTD case"].

## Annotation-specific notes
- PMID:21956163 (chronic alcohol / liver mito folate uptake): IDA mitochondrion. Abstract concerns MFT
  expression/regulation and mitochondrial folate uptake in rat liver / HepG2; supports mitochondrial
  localization and the folate-uptake association [PMID:21956163 "Transport of folate from the cytoplasm into the mitochondria is via a specific carrier-mediated process involving the mitochondrial folate transporter (MFT)"].
- PMID:34800366 HTP mitochondrion: large-scale high-confidence mitochondrial proteome; supports the
  mitochondrion location as a bulk-proteomics call (does not name substrate).
- Reactome R-HSA-200680 / R-HSA-200720 model SLC25A32 as reversible THF transporter between cytosol and
  matrix (curator TAS); folic acid transporter activity + IMM location. Historical/consensus folate model —
  keep as non-core.
