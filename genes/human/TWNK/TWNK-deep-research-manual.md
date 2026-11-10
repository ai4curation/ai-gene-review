# TWNK (Twinkle mtDNA helicase) - manual literature synthesis

No deep-research API was available for this session; this file is a manual synthesis
from cached publications in `publications/` and PubMed searches. Every claim carries
inline provenance.

## Identity and family

- Human TWNK (C10orf2, PEO1; UniProt Q96RR1, 684 aa) encodes Twinkle, the replicative
  DNA helicase of mitochondria. It is a superfamily 4 (SF4), DnaB-like ring helicase
  related to bacteriophage T7 gene 4 primase-helicase [PMID:17324440 "Our findings place
  the mitochondrial DNA helicase firmly in the DnaB-like family of replicative DNA
  helicases."].
- Domain architecture: N-terminal zinc-binding-like domain (ZBD) and RNA-polymerase-like
  domain (RPD; primase-like, catalytically inactive), linker, and C-terminal RecA-like
  helicase/hexamerization domain [PMID:25824949 "an N-terminal zinc-binding domain (ZBD),
  an intermediate RNA polymerase domain (RPD) and a RecA-like hexamerization C-terminal
  domain (CTD)"]. The primase-like domain has lost primase activity [PMID:18039713
  "TWINKLE is not an active primase in vitro"].

## Molecular function

- 5'->3' DNA helicase driven by NTP hydrolysis (UTP optimal) [PMID:12975372 "TWINKLE is a
  DNA helicase with 5' to 3' directionality and distinct substrate requirements"; "The
  helicase activity has an absolute requirement for hydrolysis of a nucleoside
  5'-triphosphate, with UTP being the optimal substrate."].
- Unwinding stimulated by mtSSB (SSBP1) [PMID:12975372 "DNA unwinding by TWINKLE is
  specifically stimulated by the mitochondrial single-stranded DNA-binding protein."].
- Binds ssDNA (N-terminal region required) and also dsDNA [PMID:18039713 "the N-terminal
  part of TWINKLE is required for efficient binding to single-stranded DNA"; "In contrast
  to the phage protein, TWINKLE binds to double-stranded DNA."].
- Also has strand-annealing activity [PMID:22383523 "TWINKLE, although a helicase, has an
  antagonistic activity of annealing two complementary ssDNAs"], D-loop dissociation and
  branch migration [PMID:27226550 "Twinkle branch-migrates an open-ended mobile
  three-stranded DNA structure with a strong 5' to 3' directionality preference"].
- Oligomeric state: hexamers (and heptamers/higher oligomers) formed without nucleotide
  [PMID:18039713 "TWINKLE forms stable hexamers even in the absence of Mg(2+) or NTPs"];
  [PMID:22383523 "The recombinant TWINKLE assembles into hexamers and higher oligomers"].
- Membrane association: full-length human Twinkle and its RPD bind cardiolipin-containing
  liposomes; ATPase is stimulated by liposomes [PMID:34950192 "ATPase activity of the human
  replicative mtDNA helicase is enhanced by binding to liposomes."].

## Biological process

- Replicative helicase of the mtDNA replisome with POLG and mtSSB; in vitro reconstitution
  [PMID:15167897 "In combination, POLgamma and TWINKLE form a processive replication
  machinery, which can use dsDNA as template to synthesize single-stranded DNA (ssDNA)
  molecules of about 2 kb."].
- Mouse conditional knockout: TWINKLE is the only replicative helicase in mammalian
  mitochondria and is required for nascent D-loop H-strand synthesis [PMID:23393161
  "TWINKLE is essential for mouse embryonic development and thus is the only replicative
  DNA helicase in mammalian mitochondria"].
- In cells, dominant adPEO mutants cause replication stalling and mtDNA depletion
  [PMID:18971204 "We show that expression of dominant Twinkle mutations results in the
  accumulation of mtDNA replication intermediates in cell culture."]. A reduction in
  mitochondrial transcripts was also seen, but this is a downstream consequence, not
  evidence that Twinkle participates in transcription [PMID:18971204 "our results in cell
  culture pointed to a problem of transcription that preceded the mtDNA depletion
  phenotype"].
- Loading of TWINKLE at the D-loop 3' end (coreTAS) by ChIP [PMID:26253742 "we demonstrate
  that the loading of the helicase TWINKLE at coreTAS is reversible"].
- Drosophila models of the orthologous helicase: dominant-negative active-site and adPEO
  mutations deplete mtDNA, cause OXPHOS defects and secondary apoptosis [PMID:22952820
  "The mitochondrial impairment caused by these mutations promotes apoptosis"]. Apoptosis
  is an indirect consequence, not a Twinkle function.

## Location

- Mitochondrial nucleoids (co-localizes with mtDNA) [PMID:18971204 "While wild-type Twinkle
  co-localized with mtDNA in punctate nucleoids within mitochondria"]; co-fractionates with
  mtDNA [PMID:23275553 "The majority of the signal from proteins known to be involved in
  mtDNA metabolism, such as TWINKLE, TFAM, SSBP1 and POLG1, resolved in the same fractions
  as mtDNA"]; nucleoids associate with the inner membrane [PMID:34950192 "endogenous human
  mtDNA helicase is attached firmly to the MIM even in the absence of mtDNA"].

## Interactions

- Co-IP with LONP1 [PMID:14739292 "Co-immunoprecipitation experiments show that Lon
  interacts with mtDNA polymerase gamma and the Twinkle helicase"]; Twinkle is a LONP1
  substrate according to Reactome R-HSA-9838081.
- High-throughput Y2H hits (LGALS3BP) from HuRI/BioPlex-type screens (PMID:28514442,
  PMID:33961781) have no functional follow-up.

## Disease

- adPEO with multiple mtDNA deletions (PEOA3), MTDPS7 (infantile-onset spinocerebellar
  ataxia / hepatocerebral), Perrault syndrome 5 (UniProt Q96RR1 DISEASE).

## Isoforms

- Isoform 2 (Twinky) lacks ATPase/unwinding and DNA binding and is monomeric (UniProt
  Q96RR1 FUNCTION [Isoform 2], citing PMID:18039713).
