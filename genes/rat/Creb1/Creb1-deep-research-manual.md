# Creb1 (rat, P15337) - manual literature synthesis

No deep-research API was available for this session; this synthesis was assembled by hand from the
cached publications in `publications/`, the UniProt record (`Creb1-uniprot.txt`) and the existing
human CREB1 review in this repository. Most cached rat papers are abstract-only; the full-text
papers read were PMID:21367864, PMID:16207717, PMID:18193038, PMID:19365572, PMID:22952905,
PMID:24084215, PMID:27664298 and PMID:31092551.

## Identity and domain architecture

- Rat Creb1 (P15337, RGD:620218, GeneID 81646) is a 327-aa (delta isoform, displayed) bZIP protein of
  the CREB/ATF family; the alpha isoform carries a 14-residue insertion after residue 86.
  [Creb1-uniprot.txt "SIMILARITY: Belongs to the bZIP family."]
- Domains: kinase-inducible domain (KID, 8-146) and C-terminal bZIP (269-327; basic motif 270-295,
  leucine zipper 297-318). [Creb1-uniprot.txt FT DOMAIN]
- Ser-119 (Ser-133 in alpha numbering) is the activating phosphosite; S119A abolishes activation by
  CaMK4 [Creb1-uniprot.txt "S->A: Loss of activation by CaMK4."]; Ser-128 phosphorylation by CaMKII
  is inhibitory.
- Rat Creb1 was the original CREB cDNA (Gonzalez et al. 1989, PMID:2521922), cloned from rat
  PC12/brain and recognized as a cAMP-regulated nuclear factor with a phosphorylation-site cluster.

## Molecular function

- Sequence-specific binding to CRE (TGACGTCA) and CRE half-sites as a dimer, through the bZIP
  domain. In rat pineal nuclear extracts CREB is a constituent of complexes on the Rgs4 AP-1R
  (tgcgtca) CRE-half-site element and binds it constitutively day and night, while the bound CREB is
  phosphorylated at night [PMID:21367864 "indicates constitutive CREB binding to this sequence"].
- Rat CREB binding at CREs in other promoters: bradykinin B2 receptor enhancer (requirement of CREB
  DNA binding and Ser-133 phosphorylation) [PMID:15632413 "demonstrated the requirement of CREB DNA
  binding and Ser-133 phosphorylation for optimal enhancer function"]; TGF-beta3 promoter CRE
  (PMID:16891311); GIOT1 promoter CRE (PMID:12697699); TGF-beta1 promoter CRE in hepatic stellate cells
  (PMID:27279449); proenkephalin CREs in striatum (PMID:9581644).
- Transcriptional activation through phospho-KID binding to the KIX domain of CBP/p300: the NMR
  structure of the pKID-KIX complex [PMID:9413984 "The nuclear factor CREB activates transcription of
  target genes in part through direct interactions with the KIX domain of the coactivator CBP in a
  phosphorylation-dependent manner."]. CBP recruitment and histone hyperacetylation accompany CREB
  occupancy at the B2R promoter (PMID:15632413); p300 cooperates with CREB on the fibronectin promoter
  (PMID:22357921).
- Other partners: TOX3 (calcium-dependent co-activator; PMID:19196971), beta-arrestin1 (PMID:21223624),
  mitochondrial HSP70/GRP75 (PMID:16207717).

## Signalling inputs

- cAMP/PKA, Ca2+/CaMK, growth factor/ERK/RSK/MSK and PI3K/AKT pathways converge on Ser-119
  phosphorylation [Creb1-uniprot.txt PTM]. In the SCN, light/glutamate-induced phase advances need
  CRE-mediated Per1 induction (CRE-decoy oligonucleotides block it) [PMID:12409294 "Thus,
  Ca(2+)/cAMP response element-binding protein (CREB) and Per1 are integral components of the pathway
  transducing light-stimulated GLU neurotransmission into phase advance of the circadian clock."].
- NGF applied to distal axons triggers intra-axonal CREB translation and retrograde transport to the
  nucleus, needed for CRE-mediated transcription and survival (rat DRG neurons) [PMID:18193038].
- BDNF regulates CREB-DNA binding via NO / S-nitrosylation (PMID:16427017).

## Physiological roles (context-dependent, non-core)

- Neuronal plasticity and memory: dominant-negative CREB in perirhinal cortex impairs long-term
  recognition memory and LTP (PMID:16000619); siRNA knockdown in laterodorsal thalamus impairs memory
  consolidation (PMID:31092551); SUMOylation at K271/K290 by PIAS1 enhances spatial memory
  (PMID:25031400).
- Neuronal excitability: constitutively active CREB depolarizes locus coeruleus neurons
  (PMID:16641242).
- Survival/apoptosis: dominant-negative CREB induces VSMC apoptosis and lowers Bcl-2 (PMID:12939230);
  mitochondrial CREB supports complex I gene expression and neuronal survival (PMID:16207717); CREB1
  can also promote DNA-damage apoptosis in autophagy-defective cells (PMID:24189100).
- Proliferation/differentiation: fibroblast (PMID:19285017), Muller glia progenitor (PMID:19365572),
  PC12 neuronal differentiation (PMID:31678682), thyroid growth (PMID:21816899).
- Drug/xenobiotic responses (ethanol, morphine, nicotine, cocaine, antidepressants) are measured as
  changes in CREB phosphorylation or abundance (IEP-type evidence).
- Mouse genetics (ISO sources): Creb1-null lungs fail to mature (PMID:21408140); brain CREB loss causes
  pituitary hypoplasia and dwarfism via reduced GHRH (PMID:16141355).

## Caveats

- Mitochondrial CREB (PMID:16207717) relies on fractionation, proteinase K protection and a
  mito-targeted dominant negative; it is a minority pool and not the core site of action.
- Many process annotations derive from correlation of phospho-CREB with a stimulus, and are
  downstream physiology rather than CREB's own activity.
