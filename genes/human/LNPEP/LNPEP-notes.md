# LNPEP review notes

## Research provenance

- Review target: human **LNPEP**, HGNC:6656, reviewed UniProt Q9UIQ6 (`LCAP_HUMAN`). The current approved name is leucyl and cystinyl aminopeptidase; historical names include IRAP, oxytocinase, and placental leucine aminopeptidase.
- Automated deep-research attempts were not usable: Edison/Falcon returned HTTP 402 and Perplexity returned HTTP 401. No provider-labelled deep-research file was fabricated. This review therefore uses cached primary publications, reviewed UniProt, Reactome records, and live QuickGO/GO definitions.
- Live QuickGO returned 64 rows. The local TSV matched the live export exactly. Normalization produced 40 source annotations: 38 singleton tuples, one three-partner PMID:25416956 IPI tuple, and one 23-partner PMID:32296183 IPI tuple tested on Q9UIQ6-2. All 76 ordered WITH/FROM identifiers were restored. The only live extension is plasma membrane `part_of UBERON:0002421` from rat P97629. There are no NOT rows.

## Protein architecture, products, and topology

- The displayed product is 1025 aa. UniProt records a cytosolic segment 1-110, signal-anchor/TM 111-131, and extracellular (or endosomal-lumen-facing) catalytic region 132-1025. The primary sequence paper independently describes the same topology: [PMID:9177475, "Oxytocinase is a type II integral membrane protein of 1025 amino acid residues, consisting of an acidic intracellular region of 110 amino acids followed by a hydrophobic transmembrane segment of 22 residues and 893 extracellular residues containing the characteristic Zn2+ coordination sequence element His-Glu-Xaa-Xaa-His-(18 residues)-Glu found in gluzincins."]
- Isoform 2 lacks residues 1-14 and isoform 3 lacks residues 1-19; both deletions are confined to the N-terminal cytosolic tail, upstream of the TM and catalytic domain. The 23 HuRI edges identify the tested construct Q9UIQ6-2 but do not establish isoform-specific biology.
- UniProt records proteolytic cleavage between residues 154-155, producing the pregnancy-serum chain 155-1025. This is a processed product, not a splice isoform. The extracellular GO annotation applies to this soluble product and must not be used to call intact LNPEP soluble.
- UniProt states “Homodimer,” but the record does not attach a primary evidence code to that sentence. No specific GO protein-containing complex term is warranted; the review records no stable complex assignment.

## Core catalytic activity and peptide substrates

- Purified human placental enzyme provides the strongest direct biochemical anchor: [PMID:1731608, "We also examined the hydrolytic activity of P-LAP using naturally occurring peptide hormones and found that the enzyme hydrolyzed oxytocin, vasopressin, and angiotensin III."]
- LNPEP is therefore a zinc M1 metalloaminopeptidase, not merely a generic metallopeptidase. GO:0070006 is the core MF; GO:0004177 is correct but broader, and GO:0008237 should be refined.
- Human neuronal evidence broadens the substrate set: [PMID:11389728, "P-LAP was shown to degrade several bioactive neuropeptides such as Met-enkephalin and dynorphin A (1-8)."] This directly supports neuropeptide catabolism.
- LNPEP is also the high-affinity angiotensin-IV binding site and its ligands inhibit catalysis: [PMID:11707427, "We also show that AT(4) receptor ligands dose-dependently inhibit the catalytic activity of IRAP."] The historical “AT4 receptor” label should not be represented as a canonical GPCR/receptor activity.

## Localization and regulated trafficking

- Human endothelial cells show regulated surface recruitment: [PMID:11108258, "In summary, our findings provide clear evidence that OT triggers directly OTase translocation in human umbilical vascular endothelial cells via a protein kinase C-dependent pathway coupled to OTR."]
- Human adipocytes directly support the missing insulin-responsive compartment location: [PMID:11701721, "Therefore, we studied subcellular localization of GLUT4 and insulin-regulated aminopeptidase (IRAP; also referred to as vp165 or gp160), which is a constituent of GLUT4 vesicles and also translocates to PM in response to insulin."]
- In mouse 3T3-L1 adipocytes, LNPEP/IRAP is not merely cargo. Knockdown and rescue show that its cytosolic/transmembrane portion controls sorting/retention of GLUT4: [PMID:20410133, "This increased exocytosis was rescued by reexpression of either full-length IRAP or IRAP-TR (Figure 3A)."] This noncatalytic trafficking role is mechanistically strong but currently model-organism evidence for human LNPEP; retain as a gap/context rather than assert a human core GO BP.
- Tankyrase interaction is specific and real: [PMID:12080061, "Herein we describe a novel RXXPDG motif shared by IRAP, TAB182, and human TRF1 that mediates their binding to tankyrases."] There is no current tankyrase-binding GO term. Generic protein binding remains over-annotated.

## Endosomal antigen processing

- Human dendritic cells directly place LNPEP in a Rab14-positive endosomal compartment with MHC-I molecules: [PMID:19498108, "In human dendritic cells, IRAP was localized to a Rab14+ endosomal storage compartment in which it interacted with MHC class I molecules."]
- The demonstrated pathway is proteasome dependent: [PMID:19498108, "We propose the existence of two pathways for proteasome-dependent cross-presentation in which final peptide trimming involves IRAP in endosomes and involves the related aminopeptidases in the endoplasmic reticulum."] Therefore Reactome's TAP-independent/vacuolar term is too specific; use the unsigned broader exogenous-peptide MHC-I process.
- The mechanism is context dependent. In mouse models, IRAP is dispensable for steady-state CD8-positive dendritic cells but required in inflammatory monocyte-derived dendritic cells: [PMID:19918052, "However, cross-presentation was impaired in moDC deficient in IRAP or MR, confirming the role of these two molecules in inflammatory DC."]
- Full-length LNPEP is an early-endosome **membrane** protein with a lumen-facing catalytic domain; GO:0031905 early endosome lumen misclassifies the whole integral protein.

## Source/reference problems found

- PMID:11062501 explicitly purified puromycin-sensitive aminopeptidase and bleomycin hydrolase, not LNPEP. The corresponding LNPEP EXP row is a wrong-entity Reactome mapping.
- PMID:9668046 identifies an IFN-gamma-induced cytosolic LAP in soluble HeLa extracts, not membrane LNPEP.
- PMID:15691326 is about ERAP2/L-RAP promoter regulation and explicitly treats P-LAP as a related, separate gene.
- Reactome R-HSA-983162 carries the same historical “LAP” name collision into a cytosolic aminopeptidase set; R-HSA-983168 then over-propagates LNPEP into protein polyubiquitination. Both source rows should be removed.
- The PMID:17897319 lysosomal-membrane HDA and PMID:19946888 membrane HDA are plausible, but their abstract-only caches do not expose the individual Q9UIQ6 rows; curator/table provenance is retained with appropriate confidence boundaries.

## Synthesis and open questions

1. Core catalytic unit: membrane-bound GO:0070006 activity at cytoplasmic vesicle and plasma membranes, directly involved in peptide/neuropeptide catabolism; substrates include oxytocin, vasopressin, angiotensin III, Met-enkephalin, and dynorphin.
2. Core immune-context unit: the same lumen-facing activity at early-endosome membrane trims exogenous antigenic peptide precursors during MHC-I cross-presentation.
3. Processed-product unit: soluble pregnancy-serum LNPEP retains GO:0070006 activity extracellularly and modulates circulating peptide hormones.
4. Major gap: determine whether the cytosolic-tail-dependent GLUT4-sorting role demonstrated in mouse adipocytes is conserved in normal human adipocytes and which human binding partner executes it.
5. Major gap: define the peptide repertoire and TAP requirement of LNPEP-dependent cross-presentation across human dendritic-cell states.
6. Isoform experiment: compare Q9UIQ6-1, -2, and -3 for trafficking, tankyrase binding, and catalytic activity without assuming that the HuRI-tested isoform 2 has unique function.
