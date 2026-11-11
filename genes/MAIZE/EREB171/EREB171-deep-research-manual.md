# EREB171 (DIL1, B4FT20) - manual literature synthesis

No deep-research API was available for this session; this synthesis was assembled by hand
from cached publications and PubMed searches (queries: "(DIL1 OR dwarf & irregular leaf OR
EREB171) AND maize"; "SMOS1 rice AP2 small organ size"; "SMOS1 DLT GRAS brassinosteroid rice").

## Identity

- UniProt B4FT20 (TrEMBL, PE 2), 412 aa, gene name EREB171, GeneID 100279334, Gramene
  Zm00001eb287100. The EMBL cross-reference EU966890 (ACG39008.1) is the cDNA that Jiang et
  al. identified as the DIL1 (dwarf & irregular leaf1) gene, and the predicted 412 aa
  polypeptide matches [PMID:22649507 "Only one low copy annotated gene with corresponding EST,
  an AP2 transcription factor-like gene, was identified within this interval (GeneBank
  EU966890.1)"; "encoding a putative polypeptide of 412 amino acids"].
- Also called ZmAP2-5 [PMID:22649507 "DIL1 belongs to the AP2 subfamily (identical to
  ZmAP2-5 or Unigene ZM.83210 in [17])"].
- Domain architecture: one PROSITE AP2/ERF domain (residues 75-141) followed by a degenerate
  second AP2-like repeat (around residues 165-215, "FYRGLPKYRGLLRQLH..."); PANTHER
  PTHR32467:SF32 (AP2-LIKE ETHYLENE-RESPONSIVE TRANSCRIPTION FACTOR SMOS1), i.e. the same
  subfamily as rice SMALL ORGAN SIZE1, which is described as an AP2-type factor "with an
  imperfect AP2 domain" in the basal ANT lineage [PMID:24486766].

## Maize genetics (Jiang et al. 2012, full text read)

- Two allelic EMS semi-dwarf mutants (dil338, dil474) have shorter internodes, shorter, wider,
  wrinkled leaves and smaller leaf angles; epidermal and parenchyma cells are irregular and
  parenchyma cells smaller [PMID:22649507].
- Both alleles are intronic G-to-A changes near exon-intron junctions causing exon 3 or exons
  3+4 skipping; "Since both exons 3 and 4 are within the AP2 domain, deletions of exons 3
  and/or 4 would presumably affect the function of the AP2 protein" [PMID:22649507].
- Expression: low, constitutive; in situ hybridisation shows transcripts "accumulate in the
  leaf primordia and also the P0 region of the meristem" [PMID:22649507].
- Mechanism was unknown at the time: "The molecular mechanism of DIL1 regulation in stalk and
  leaf development is unknown." [PMID:22649507]. No protein localisation, DNA-binding or
  transactivation data are in this paper.

## Maize molecular data (Sheng et al. 2025, abstract only)

- The GRAS protein COMPACT PLANT 3 (CT3) interacts with DIL1; ct3 and dil1 act in the same
  genetic pathway for leaf angle and plant height [PMID:39928526].
- "CT3 functions as a co-regulator to enhance the DNA affinity and transcriptional activity of
  DIL1", and DIL1 binds directly to the cell-wall genes ZmEXO1 and ZmXTH14, which are
  downregulated in ct3 [PMID:39928526]. Full text (PMC11879032) was not retrievable here, so
  the assays (EMSA, ChIP, transactivation) and the binding motif could not be inspected.

## Rice SMOS1 (same PANTHER subfamily; abstracts only)

- smos1 loss of function reduces organ size via smaller cells and abnormal microtubule
  orientation; functional fluorophore-tagged SMOS1 is nuclear; SMOS1 binds the OsPHI-1
  promoter (gel shift, ChIP) [PMID:24486766].
- SMOS1 and the GRAS protein SMOS2/DLT "physically interact to cooperatively enhance
  transcriptional transactivation activity in yeast and in rice nuclei" [PMID:28069545].
- The maize DIL1-CT3 (AP2 + GRAS) pairing therefore parallels rice SMOS1-SMOS2/DLT. Whether
  DIL1 is the strict ortholog of SMOS1 was not established in the papers read; both are in
  PTHR32467:SF32.

## Implications for GO

- MF: sequence-specific DNA-binding transcription factor that binds cis-regulatory regions of
  target genes (maize direct binding, rice gel shift/ChIP); activity probably activating
  (CT3/DLT enhance transactivation; targets reduced in ct3), but direction is not shown for
  DIL1 alone in material read.
- CC: nucleus (rice SMOS1 direct; maize inferred).
- BP: regulation of DNA-templated transcription. Developmental roles (internode elongation,
  leaf shape, cell expansion) are supported by mutant phenotype only and are not proposed as
  NEW process terms.
