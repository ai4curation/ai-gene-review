# J7SF87 (sqrd-2, Y9C9A.16b) manual literature review

No deep-research API was available, so this review was assembled by hand from the cached
publications and a PubMed search ("(sqrd-2 OR sqrd-1 OR sulfide quinone oxidoreductase) AND
elegans", 5 hits), plus a sequence comparison in `J7SF87-bioinformatics/`.

## Identity

- UniProtKB J7SF87 (TrEMBL, unreviewed) is the 422-residue Y9C9A.16b product of WormBase gene
  WBGene00021183 (GeneID 189421), chromosome IV. The shorter Y9C9A.16a product is Q9N2S1 (361 aa).
- The gene was named sqrd-2 by Mikolas et al.: [PMID:23484030 "Interestingly, one of the genes
  that was increased in gei-8(ok1671) mutants (Y9C9A.16) encodes a sulfide:quinone oxidoreductase
  that we name sqrd-2."]
- It is the paralog of sqrd-1 (F02H6.5). Budde and Roth: [PMID:21840852 "The C. elegans genome is
  predicted to encode another SQRD homolog, Y9C9A.16 (sqrd-2), which was initially classified as a
  pseudogene."]
- It is expressed: [PMID:39178951 "We found that Y9C9A.16 is expressed in C. elegans, yielding an
  mRNA of the expected size according to the gene model (Fig. S2)."]

## Sequence (J7SF87-bioinformatics/RESULTS.md)

- 45.3% identical to human SQOR (Q9Y6N5); both catalytic persulfide cysteines (human Cys201 and
  Cys379) are conserved, as J7SF87 Cys169 and Cys351; the FAD-binding positions and the N-terminal
  GxGxxG motif (residue 18) are present.
- No counterpart of the human N-terminal transit peptide: the J7SF87 model starts 17 residues
  before the GxGxxG motif.
- Q9N2S1 (isoform a) lacks residues 1-61, including the FAD motif, but keeps both cysteines.
- 75.1% identical to SQRD-1 (C6KRP5).

## Genetics and physiology

- A deletion allele does not cause H2S sensitivity: [PMID:21840852 "We obtained the deletion allele
  of sqrd-2 and found that it is not sensitive to RA/H2S."]
- In liquid sulfide, sqrd-2(ok3440) recovers motility slightly earlier than wild type:
  [PMID:39178951 "In contrast to the sqrd-1 mutant strain, the recovery of sqrd-2 mutant strain
  (sqrd-2(ok3440)) was slightly earlier than that of the N2 strain"]. The authors speculate:
  [PMID:39178951 "suggesting that SQRD-2 would function as a negative regulator as part of circuit
  that controls the sulfide response"].
- Expression is not induced by H2S, unlike sqrd-1: [PMID:39178951 "Unlike the sqrd-1 gene, sqrd-2
  does not change its expression under H2S conditions according to microarray studies (16)."]
- Homology models of SQRD-2 dock ubiquinone and rhodoquinone in the quinone site (in silico only):
  [PMID:39178951 "UQ and RQ were kept in the quinone site of SQRD-1 and SQRD-2 and within a distance
  compatible with an electron transfer reaction during the simulation."]
- Expression rises 7.6-fold in gei-8 (NCoR/SMRT homologue) mutants: [PMID:23484030 "One of the
  most significantly affected genes in the gei-8(ok1671) homozygous mutants was Y9C9A.16, encoding
  a predicted mitochondrial sulfide:quinone oxidoreductase, which had an averaged 7.6-fold increase
  in expression compared to wild-type controls"]. RNAi has no phenotype in wild type
  [PMID:23484030 "We were not able to identify any specific phenotype of Y9C9A.16 knockdown in wild
  type animals."], but modifies gei-8 gonad phenotypes. The dsRNA region includes three 21U-RNA
  loci, so the phenotypes cannot be assigned to the protein.

## Ortholog biochemistry

- Human SQOR is the mitochondrial glutathione-dependent SQR (EC 1.8.5.8), whose catalytic
  cysteines are experimentally defined (UniProt Q9Y6N5 ACT_SITE 201 and 379, PubMed:30905673).

## Not found

- No enzyme assay, purified protein, localization study or structure of worm SQRD-2.
