# phzC1 (PA4212 / PA1901, Q7DC82) notes

## 2026-10-28 review (PseudoCAP IBA-seed worklist, rank 103)

No deep-research provider keys were available; literature gathered by PubMed
search and from the cached publications. The completed phzM and phzS reviews in
this repository were read for pathway context.

### Identity

- UniProt Q7DC82 (unreviewed, PE 3), 405 aa, "Phospho-2-dehydro-3-deoxyheptonate
  aldolase" (DAHP synthase, EC 2.5.1.54), class-II DAHP synthase family, Pfam
  PF01474 DAHP_synth_2, PANTHER PTHR21337:SF0
  [file:PSEAE/phzC1/phzC1-uniprot.txt].
- The entry covers both copies of the duplicated phenazine operon: gene names
  `phzC1` and `phzC2`, ordered locus names PA1901 and PA4212
  [file:PSEAE/phzC1/phzC1-uniprot.txt]. The two proteins are identical, so GOA
  rows and the PANTHER leaf (phzC1 = PA1901) refer to the same sequence.
- PAO1 also has non-phenazine DAHP synthases, including PA2843 (Q9I000), which
  matters for the propagation analysis below.
- The enzyme catalyses the first step of the shikimate pathway: D-erythrose
  4-phosphate + phosphoenolpyruvate -> 3-deoxy-D-arabino-heptulosonate
  7-phosphate [file:PSEAE/phzC1/phzC1-uniprot.txt]. In the phz operon it
  increases flux towards chorismate, the substrate of PhzE.

### What PMID:11591691 (the seed reference) shows

- Mavrodi et al. cloned both operons [PMID:11591691 "Two seven-gene phenazine
  biosynthetic loci were cloned from Pseudomonas aeruginosa PAO1"] and showed
  that each is sufficient in a heterologous host
  [PMID:11591691 "Functional studies of phenazine-nonproducing strains of
  fluorescent pseudomonads indicated that each of the biosynthetic operons from
  P. aeruginosa is sufficient for production of a single compound,
  phenazine-1-carboxylic acid (PCA)"].
- The evidence is therefore at the level of the operon: PseudoCAP applied the
  same IDA row to phzA1, phzB1, phzC1, phzE1, phzF1, phzG1 and the phzA2/B2/G2
  copies (QuickGO, reference PMID:11591691). Only the abstract is cached (PMC
  has no usable full text for this article), so the individual-gene
  contributions cannot be read off the paper. The conclusion that PhzC belongs
  to the pathway does not rest on this paper alone, however.

### Independent support for PhzC's role

- The PAO1 phz-cluster DAH7PS has been purified and crystallised. It is kinetically
  competent (KM 17 and 16 microM for PEP and E4P) and, unlike the housekeeping
  enzyme, is not feedback-inhibited [PMID:30242059 "Consistent with this is the
  observation made during functional characterisation that PaeDAH7PSPA1901 is
  insensitive to allosteric regulation by aromatic amino acids, confirming that
  PaeDAH7PSPA1901 functions primarily within secondary metabolism"]. The same
  work contrasts it explicitly with the housekeeping paralogue PA2843
  [PMID:30242059 "A primary structure alignment among type II DAH7PSs
  (Supplementary Figure S1) indicates that PaeDAH7PSPA1901 appears to lack much
  of the sequence that corresponds to the alpha2a and alpha2b helices of
  PaeDAH7PSPA2843, MtuDAH7PS or CglDAH7PS"].
- In the close relative P. chlororaphis, deleting the orthologous phzC collapses
  phenazine output and complementation restores it
  [PMID:35053084 "As shown in Figure 4, no morphological difference was found,
  whereas phzC mutant strain HT66DphzC displayed a reduction in PCN
  production."; PMID:35053084 "After the complementation of gene phzC in the
  corresponding DAHP synthase-deficient strain, the production of PCN was
  significantly restored."], while the housekeeping aroF/aroG/aroH deletions
  barely affect it.

So, unlike several other seeds in this worklist, the seed claim itself is right:
PhzC performs a step - the committed entry into the shikimate pathway - whose
product is consumed by phenazine biosynthesis, and the enzyme is dedicated to
that role rather than to primary metabolism.

### Where the propagation goes wrong

PTN000481936 is a Proteobacteria node of PTHR21337 with five leaves:
*Helicobacter pylori* HP_0134, *Bradyrhizobium diazoefficiens* blr3778,
*Xanthomonas campestris* dhs1, *P. aeruginosa* phzC1 (PA1901) and
*P. aeruginosa* PA2843. The GO:0002047 IBD at this node is sole-seeded by
Q7DC82, and all five leaves now carry phenazine biosynthetic process by IBA.
Four of them are housekeeping DAHP synthases of organisms, or of a paralogous
locus, with no phenazine pathway: *H. pylori*, *Xanthomonas* and
*Bradyrhizobium* are not phenazine producers, and PA2843 is the *P. aeruginosa*
primary-metabolism enzyme that the structural work above distinguishes from the
phz-cluster one. The DAHP synthase activity itself is asserted, correctly, at
the family root PTN000481914 (two seeds), so nothing is lost by removing the
phenazine IBD from the Proteobacteria node.

### Annotation decisions

- GO:0002047 (IDA, IBA): ACCEPT for this gene (core), because PhzC supplies the
  pathway's own shikimate flux and the gene is part of the phenazine operon;
  but a GO_CENTRAL defect is filed against the node, whose other four leaves
  should not inherit the term. The IDA code is operon-level evidence, noted in
  the review but not treated as a defect.
- GO:0003849 (IBA from the family root, IEA from EC): ACCEPT, core activity.
- GO:0009073 aromatic amino acid family biosynthetic process (IEA from
  InterPro): MARK_AS_OVER_ANNOTATED - this paralogue is the secondary-metabolism
  enzyme and is not feedback-regulated by aromatic amino acids; the primary
  metabolism role belongs to PA2843 and the aro genes.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000481936 | GO:0002047 phenazine biosynthetic process | 1 (sole) | 5 GO_Central (5 GOA rows; no TreeGrafter) | GO:0002047, IDA, PMID:11591691 | SOUND seed, WRONG node | The seed is right: PhzC is the phz-operon DAH7PS, it is kinetically characterised and allosterically unregulated, which marks it as a secondary-metabolism enzyme, and deleting the orthologue in P. chlororaphis collapses phenazine production. The caveat on the evidence code is that Mavrodi et al. tested whole operons, so the IDA is operon-level. The node, however, is a generic Proteobacteria DAHP synthase clade: besides phzC1 it contains Helicobacter pylori HP_0134, Xanthomonas dhs1, Bradyrhizobium blr3778 and - revealingly - P. aeruginosa's own housekeeping DAHP synthase PA2843, which structural work explicitly contrasts with the phz enzyme. All four now carry phenazine biosynthetic process by IBA. The term should sit on the phz-cluster enzymes only, not on this node. |
