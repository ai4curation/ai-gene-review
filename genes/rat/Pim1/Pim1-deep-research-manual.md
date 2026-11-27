# Pim1 (rat, UniProt P26794) - manual literature research

No deep-research API provider was available for this session. This file was written
by hand from cached publications (`publications/PMID_*.md`), PubMed searches, and the
UniProt records for rat (P26794), human (P11309) and mouse (P06803) PIM1.

## Identity and family

- Rat Pim1 (RGD:3330) encodes the 313-aa serine/threonine-protein kinase pim-1
  (P26794). UniProt: "Belongs to the protein kinase superfamily. CAMK Ser/Thr protein
  kinase family. PIM subfamily." InterPro IPR017348 (PIM1/2/3), PIRSF037993
  (STPK_Pim-1), PANTHER PTHR22984:SF29.
- Catalytic residues are predicted from PROSITE ProRule PRU00159: ATP-binding loop
  44-52, Lys67, proton-acceptor Asp167. Mg2+ cofactor is annotated by similarity to
  human PIM1 (human: experimental, PMID:15525646, 15657054, 15808862 as cited by UniProt).
- PIM kinases are constitutively active, lacking a regulatory domain; activity is set
  by transcription (JAK/STAT cytokine signalling), translation and protein turnover
  (HSP90 stabilization, ubiquitin-proteasome degradation).
- The rat entry lists only the 313-aa (33 kDa, AUG-initiated) form. Mouse (P06803) and
  human (P11309) entries also carry a longer CUG-initiated isoform 2 (44 kDa) that is
  membrane-associated; in mouse [UniProt P06803, citing PMID:1825810 "The pim-1 oncogene
  encodes two related protein-serine/threonine kinases by alternative initiation at AUG
  and CUG."]. Whether rat expresses the CUG isoform is not recorded in UniProt, although
  PMID:20203306 refers to "Endogenous Pim-1 (44 kDa)" in heart lysates (mouse hearts).

## Rat-specific literature

- PMID:1620615 (Wingett et al. 1992, NAR) - cloning of rat pim-1 cDNA from testis:
  "The pim-1 proto-oncogene encodes a serine/threonine protein kinase and is expressed
  in cells of hematolymphoid origin and in the germ cell lineages." A testis-specific
  2.3 kb transcript arises by alternative polyadenylation and lacks the 3' AU-rich
  element, making it more stable. Expression only.
- PMID:10373478 (Mochizuki et al. 1999, JBC; abstract only in cache) - UniProt cites it
  on the rat entry for "FUNCTION IN PHOSPHORYLATION OF CDC25A, AND INTERACTION WITH
  CDC25A": "Pim-1 physically interacts with Cdc25A both in vitro and in vivo and
  phosphorylates Cdc25A." and "Pim-1-mediated phosphorylation of Cdc25A increases its
  phosphatase activity." Kinase-inactive Pim-1 did not enhance Cdc25A-mediated
  transformation. The species of the Pim-1 construct is not stated in the abstract.
- PMID:20097747 (Lionetti et al. 2010, JBC; full text) - a hyaluronan mixed ester of
  butyric and retinoic acid (HBR) given to infarcted rat hearts. In rat cardiomyocytes
  and Stro-1 cells, "HBR enhanced the transcription of vascular endothelial growth
  factor, hepatocyte growth factor, kdr, akt, and pim-1." Nuclear run-off showed
  increased pim-1 transcription rate; induction was biphasic ("Increased pim-1 mRNA was
  detected within 24 h after HBR stimulation and then declined toward basal values after
  3 days."). The paper measures Pim1 expression only; it does not test Pim1 function.
  The authors note "Cardiac control of Pim-1 gene expression is still poorly
  understood". This is expression/regulation evidence and cannot support any
  process annotation for Pim1 (it is not in GOA).
- PMID:20203306 (Borillo et al. 2010, Circ Res) - mainly mouse hearts plus neonatal
  rat cardiomyocytes (NRCM) infected with adenoviral GFP-Pim-1: "Pim-1 protein level
  increases in the mitochondrial fraction with a corresponding decrease in the cytosolic
  fraction of myocardial lysates from hearts subjected to 30 minutes of ischemia
  followed by 30 minutes of reperfusion." Pim-1 overexpression preserved mitochondrial
  membrane potential and inhibited tBid-induced cytochrome c release.
- PMID:30257237 (Zhu et al. 2018; abstract) - in NRVMs "Pim1 overexpression enhanced
  autophagy and decreased apoptosis" after hypoxia/H2O2.
- PMID:29544221 (Zhu et al. 2018) - recombinant/human Pim-1 phosphorylates cardiac
  troponin I at Ser23/24 and Ser150; experiments used recombinant active Pim-1 and
  "Myc-tagged human Pim-1" in HEK293T, with rat cardiomyocytes for IGF-1 induction.

## Orthologue-derived functions (UniProt, by similarity)

From the rat UniProt FUNCTION text (ECO:0000250 from human P11309 and mouse P06803):
phosphorylates and inhibits pro-apoptotic BAD, MAP3K5 and FOXO3; phosphorylates MYC,
increasing its stability; phosphorylates CDC25A, CDC25C (G1/S and G2/M), CDKN1A and
CDKN1B; phosphorylates CBX3; acts in CXCL12-CXCR4 bone marrow cell homing; positive
regulator of mTORC1 via DEPDC5 phosphorylation; negative regulator of innate immunity
via GBP1 phosphorylation; phosphorylates ABCG2 (human isoform 2, PMID:18056989
according to UniProt P11309); promotes brown adipocyte differentiation (mouse).

## Basis of specific orthologous GO annotations (from P11309/P06803 DR GO lines)

- manganese ion binding: IDA in both human and mouse; but the curated cofactor is Mg2+.
- protein tyrosine kinase activator activity: human IMP; isoform 2 binds BMX
  ("Isoform 2, but not isoform 1, binds BMX.", P11309).
- xenobiotic detoxification by export: human IMP, isoform 2 with ABCG2.
- vitamin D receptor signaling pathway: human IMP (CACAO), from PMID:22720752
  (Maier et al. 2012): "the C-terminus of human PIM-1 kinase isoform2 (amino acid
  residues 135-313) ... directly interacts with VDR through the receptor's DNA-binding
  domain" and "PIM-1 modulates calcitriol signaling in HaCaT keratinocytes by enhancing
  both endogenous calcitriol response gene transcription (osteopontin) and an
  extrachromosomal DR3 reporter response."
- cardioblast proliferation: human IDA (BHF-UCL).
- cellular response to type II interferon: human IDA; human PIM1 is induced by IFNG
  (PMID:37797010 per UniProt).
- brown fat cell differentiation, positive regulation of transcription: mouse IMP;
  protein stabilization: mouse IDA; HSC proliferation: mouse IDA (CACAO).
