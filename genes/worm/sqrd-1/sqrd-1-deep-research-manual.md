# sqrd-1 (C. elegans): manual literature review

No deep-research API was available for this session. This file was written by hand from
PubMed searches (query "sqrd-1 elegans", which returns four papers: PMID:21840852,
PMID:26677221, PMID:24100226, PMID:39178951), from PMID:23484030 (supplied as a key paper),
from human SQOR biochemistry (PMID:25225291), and from the UniProt records of the sqrd-1
isoforms. Every claim carries its source.

## Identity

- Gene: sqrd-1 (F02H6.5, WBGene00008538, NCBI GeneID 178374), chromosome IV.
- UniProt: six unreviewed TrEMBL entries share the gene (C6KRP5 422 aa, isoform b;
  O62133 471 aa; A0A061ADY3 410 aa, isoform f; C6KRP6 361 aa; M1ZJU1; M1ZJZ0). GOA rows are
  keyed to C6KRP5, which this review uses as the representative entry.
- Family: SQRD family, PANTHER PTHR10632:SF2 "SULFIDE:QUINONE OXIDOREDUCTASE, MITOCHONDRIAL";
  InterPro IPR015904 (sulphide quinone reductase); Pfam PF07992 (Pyr_redox_2) FAD/NAD(P)-binding
  domain (C6KRP5 residues 13-127) [file:worm/sqrd-1/sqrd-1-uniprot.txt].
- The gene was named in a forward screen for H2S-sensitive mutants: "Analysis of the region revealed a
  gene, F02H6.5, encoding an apparent homolog of the protein sulfide:quinone reductase dehydrogenase
  (SQRD), which we have named sqrd-1 to reflect this homology" [PMID:21840852]. It is a group II SQR
  ("The C. elegans gene sqrd-1 encodes a member of the group II SQRD enzymes, which also includes human,
  mouse, and Drosophila homologs") [PMID:21840852].
- Paralog: sqrd-2 (Y9C9A.16). Both have about 45% identity to human SQOR [PMID:39178951 "C. elegans
  possesses two SQRD/SQOR genes, both with approximately 45% identity to human SQOR"].

## Isoforms (sequence comparison done in this session, UniProt FASTA)

- C6KRP5 (isoform b) and O62133 begin `MRTSTVVYGKHFKLLVVGGGAGG`; the dinucleotide-binding GxGxxG
  motif sits at residues 18-23. Neither predicted product carries an obvious N-terminal
  mitochondrial presequence comparable to the ~40-residue extension of human SQOR; the gene model
  may start downstream of a targeting exon, or targeting may be internal. This is unresolved.
- A0A061ADY3 (isoform f) and C6KRP6 begin at `MSLEANRG...` and lack the N-terminal GxGxxG FAD motif.
- O62133 and A0A061ADY3 carry an internal insertion (`VRFLLCWDIINHG...`), consistent with
  the report that three isoforms "possess a 48-amino acid insertion that, according to modeling, would
  form an external loop" [PMID:39178951]. The same paper states that "the FAD-binding domain and the
  sulfide binding are absent in SQRD-1d and SQRD-1e isoforms" [PMID:39178951].

## Molecular function

- No purified-enzyme assay of C. elegans SQRD-1 has been published (no hits in PubMed). The activity
  is inferred from orthology and from genetics.
- Human SQOR uses glutathione as its sulfane-sulfur acceptor: "Human SQR uses glutathione as an acceptor
  forming glutathione persulfide (GSSH), which is preferentially converted to thiosulfate by human
  rhodanese" [PMID:25225291]. This is the reaction described by GO:0106436 / EC 1.8.5.8.
- Budde and Roth describe the worm enzyme as "an oxidoreductase, oxidizing H2S to polysulfide and
  reducing ubiquinone" [PMID:21840852], citing the bacterial literature.
- Quinone specificity (modelling only): docking and molecular dynamics of homology models suggest
  SQRD-1 can bind both ubiquinone and rhodoquinone ("Both quinones bind similarly to C. elegans
  SQRD-1 and SQRD-2") [PMID:39178951]; the abstract concludes "sqrd-1 uses both benzoquinones"
  [PMID:39178951]. This is in-silico; no enzyme assay was done.

## Biological process: mitochondrial sulfide oxidation

- sqrd-1 mutants (point alleles from the screen and the tm3378 deletion) cannot survive low H2S;
  "The available deletion allele of sqrd-1 (tm3378) phenocopies and fails to complement these
  mutants" [PMID:21840852].
- ethe-1 (persulfide dioxygenase) mutants share the phenotype: "Similar to sqrd-1 (tm3378), ethe-1
  (tm4101) is sensitive to RA/H2S, which suggests that sqrd-1 confers resistance to H2S through the
  sulfur-oxidation pathway" (PMID:21840852; the original uses an en dash in "sulfur–oxidation").
- Model: "SQRD-1 catalyzes the first step in the H2S-oxidation pathway, ultimately resulting in
  production of sulfate and thiosulfate" [PMID:21840852].
- Sulfide sensitivity of sqrd-1(tm3378) was confirmed in liquid: "The sqrd-1 mutant strain
  (sqrd-1(tm3378)) is more sensitive to sulfide than the wild-type N2 strain" [PMID:39178951].

## Regulation

- HIF-1 induces sqrd-1: "Figure 6A shows that sqrd-1 and cysl-2 mRNA levels increase during RA/H2S and
  RA/HCN exposure" and "hif-1(ia04) mutant animals fail to increase sqrd-1 and cysl-2 mRNA levels
  during RA/H2S exposure" [PMID:21840852]. SQRD-1 protein is constitutively high in egl-9 mutants
  [PMID:21840852].
- CYSL-1 binds EGL-9 to activate HIF-1, which upregulates sulfide/cyanide detoxification genes
  [PMID:24100226, abstract only].

## Expression and localization

- A fosmid-based SQRD-1::GFP is undetectable in room air and induced by 50 ppm H2S, brightest in
  hypodermis and muscle dense bodies: "Confocal microscopy at ×40 magnification shows that the
  expression is brightest in the muscle dense bodies (tailed arrows) and the hypodermis" [PMID:21840852].
  The paper does not report a mitochondrial co-stain.
- Horsman and Miller state "SQRD-1 localizes to mitochondria" citing Budde and Roth [PMID:26677221], but
  the cited paper shows no mitochondrial marker. Mitochondrial localization therefore rests on
  orthology with human SQOR and on the quinone-dependent activity, not on a worm experiment.

## Downstream physiology (necessity evidence, not process participation)

- Proteostasis: "In sqrd-1 mutant animals, exposure to H2S leads to phosphorylation of eIF2α and
  inhibition of protein synthesis" and "Both ER and mitochondrial stress responses are activated in
  sqrd-1 mutant animals exposed to H2S, but not in wild-type animals" [PMID:26677221]. These are
  consequences of failing to remove H2S; SQRD-1 is not a component of the integrated stress response.
- Germline development: in a gei-8(ok1671) corepressor-mutant background, RNAi against sqrd-1 coding
  regions that also contain 21U-RNAs "resulted in changes in gonad arm migrations and an accumulation of
  germline cells (4.5% affected, n = 198)" [PMID:23484030]. No phenotype in wild type is reported for
  sqrd-1 RNAi, the dsRNA also targets embedded 21U-RNA loci, and the effect is weak; this does not
  support a developmental process annotation.

## Gaps

- No direct enzyme assay, no acceptor specificity (glutathione vs sulfite) and no localization assay
  for the worm protein.
- Which isoforms are catalytic and how they are targeted to mitochondria is unknown.
