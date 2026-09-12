# LRP5L evidence notes

## Scope and bottom line

This note evaluates source evidence for human **LRP5L** (UniProtKB A4QPB2;
NCBI Gene 91355; HGNC:25323) without assuming that the locus encodes a stable
protein. The evidence supports transcription/cDNA models and one reported
cataract-family and cell-perturbation study. It does **not** establish an intrinsic molecular
function, a native biological process, a native subcellular location, a signal
peptide, or a transmembrane topology. No LRP5- or LRP6-like receptor/Wnt function
should be transferred by name or broad-family membership.

There is a current database-model conflict. The official NCBI Datasets Gene API
labels LRP5L **`"type": "PSEUDO"`** and exposes 2 `NON_CODING` plus 16
`NON_CODING_MODEL` transcripts
[file:human/LRP5L/LRP5L-ncbi-gene.json, fetched 2026-08-19]. HGNC independently
assigns **`"locus_type": "pseudogene"`** while cross-referencing A4QPB2
[file:human/LRP5L/LRP5L-hgnc.json, fetched 2026-08-19]. In contrast, the cached
UniProtKB flat file still says **“ID   LRP5L_HUMAN             Reviewed;
252 AA.”** and
**“PE   2: Evidence at transcript level;”**
[file:human/LRP5L/LRP5L-uniprot.txt]. “Reviewed” denotes record curation; PE2 is
explicitly transcript-level rather than protein-level evidence. The two current
official gene authorities independently support the `PSEUDOGENE` product type
used in the review, while whether any stable endogenous translation nevertheless
occurs remains an empirical knowledge gap.

## UniProtKB sequence model and explicit limits

The displayed A4QPB2 sequence is 252 aa. UniProtKB annotates five consecutive
**“LDL-receptor class B”** repeats at residues 3-45, 46-88, 89-132, 133-175,
and 176-218 [file:human/LRP5L/LRP5L-uniprot.txt, exact `FT REPEAT` records]. It
also annotates residues 223-247 as **“Disordered”**, with computational evidence
**“ECO:0000256|SAM:MobiDB-lite”** [file:human/LRP5L/LRP5L-uniprot.txt].

Isoform 2 is a C-terminal variant, not evidence for a different function. The
record states **“TNPHA -> PGTAE (in isoform 2)”** for residues 220-224 and
**“Missing (in isoform 2)”** for residues 225-252
[file:human/LRP5L/LRP5L-uniprot.txt]. Thus isoform 2 changes residues 220-224
and removes the final 28 residues.

The complete cached record contains no `CC   -!- FUNCTION`, `CC   -!-
SUBCELLULAR LOCATION`, `FT   SIGNAL`, or `FT   TRANSMEM` line. The positive
keyword list is only **“Alternative splicing; Reference proteome; Repeat.”**
[file:human/LRP5L/LRP5L-uniprot.txt]. These absences are boundaries, not
positive evidence: they do not prove cytosolic localization, lack of secretion
in every possible product, or any molecular activity. They do show that the
reviewed UniProtKB record itself supplies no function/localization claim and no
annotated signal peptide or membrane span.

## Proteomics cross-reference audit

The UniProtKB record lists **MassIVE A4QPB2**, **PaxDb
9606-ENSP00000482378**, **PeptideAtlas A4QPB2**, **ProteomicsDB 689
(A4QPB2-1)**, and **ProteomicsDB 690 (A4QPB2-2)**
[file:human/LRP5L/LRP5L-uniprot.txt, exact `DR` records]. These are database
cross-references: their presence shows that the protein model or identifiers are
indexed by proteomics resources, but the flat file contains no peptide sequence,
sample, spectrum, locus-uniqueness assessment, or protein-existence upgrade tied
to them. UniProtKB still assigns **“PE   2: Evidence at transcript level;”**, so
it has not treated these links as accepted protein-level confirmation. The
conservative conclusion is not that proteomics resources lack LRP5L records, but
that the reviewed evidence does not establish a locus-unique endogenous LRP5L
polypeptide.

## Transcript and clone evidence

UniProtKB cites PMID:17974005 for large-scale mRNA sequencing of isoform 1. The
paper describes **“more than 3,800 sequence-verified entry clones representing
ORFs, cloned with and without stop codon, for about 1,700 different gene loci”**
[PMID:17974005, Abstract]. It is a general ORFeome-resource paper and does not
directly characterize LRP5L function.

UniProtKB cites PMID:15489334 for large-scale mRNA sequencing of isoforms 1 and
2. The cached abstract says the MGC was designed to generate **“a publicly
accessible cDNA resource containing a complete open reading frame (ORF) for
every human and mouse gene”** [PMID:15489334, Abstract; full text unavailable in
cache]. This supports historical transcript/cDNA-model provenance, not protein
expression or function. UniProtKB also cites the chromosome 22 genomic-sequence
paper PMID:10591208; it was not promoted to a top-level functional reference
because it establishes genomic context rather than LRP5L-specific transcript,
protein, or functional evidence.

## PANTHER family boundary

The locally fetched PANTHER table assigns A4QPB2/LRP5L to
**PTHR46513:SF43**, while human LRP5 (O75197; 1615 aa) is
**PTHR46513:SF16** and human LRP6 (O75581; 1613 aa) is
**PTHR46513:SF40**
[file:interpro/panther/PTHR46513/PTHR46513-entries.csv, exact A4QPB2, O75197,
and O75581 rows]. The broad family also contains EGF and nidogen proteins, so
membership in PTHR46513 is far too broad for function transfer. The distinct
subfamilies, the approximately 252-aa versus approximately 1,600-aa lengths,
and the absence from A4QPB2 of an annotated signal peptide/transmembrane segment
make transfer of LRP5/LRP6 receptor, Wnt-coreceptor, ligand-binding, or membrane
localization annotations unsafe.

## Direct cataract study (PMID:32789677)

The only located primary experimental paper directly centered on human LRP5L is
Sun et al. (2020). The cached abstract reports **“a novel suspected pathogenic
mutation in LRP5L (c.107C > G, p.P36R)”**, absent from **“300 normal controls
and 300 age-related cataract patients”** [PMID:32789677, Abstract; full text
unavailable]. It also states that wild-type and mutant LRP5L plasmids were
transfected into HLE B-3 cells and human anterior lens capsules, and that
LRP5L/laminin gamma-1 were knocked down with siRNA [PMID:32789677, Abstract,
**“Wild-type and mutant low-density lipoprotein receptor-related protein 5-like
(LRP5L) plasmids were constructed and transfected into human lens epithelial
cells (HLE B-3) and human anterior lens capsules.”**].

The reported result is that **“LRP5L upregulated laminin γ1 expression”** and
**“LRP5L upregulated c-MAF expression”**, with P36R inhibiting those effects
[PMID:32789677, Abstract]. This is direct perturbation evidence for expression
effects in the tested systems. It does not identify an intrinsic biochemical
activity, demonstrate a direct molecular interaction, establish native
localization/topology, or justify a receptor/Wnt annotation. The current NCBI
pseudogene classification and suppression of the exact historical coding
RefSeqs materially contest the protein-based interpretation. Because only the
abstract is cached, construct sequence/isoform identity, segregation details,
and assay controls could not be independently audited. The paper is retained as
highly relevant but its protein-causal interpretation is marked `DISPUTED`, not
dismissed.

## Curation boundary

- Supported: a transcribed human locus; historical full-ORF/cDNA models; a
  retained UniProtKB 252-aa PE2 sequence model with five LDLR class B repeats;
  a C-terminal alternative splice model; and reported P36R-associated lens-cell
  expression phenotypes.
- Not established: stable endogenous protein production, molecular function,
  direct binding partners, receptor activity, Wnt signaling, native biological
  process, subcellular location, signal peptide, or transmembrane topology.
- Unresolved evidence boundary: NCBI Gene and HGNC treat LRP5L as a pseudogene
  while UniProtKB retains a reviewed transcript-evidence protein record and
  links to proteomics aggregators. Resolving the conflict
  requires endogenous protein evidence tied unambiguously to the locus and
  re-evaluation of the 2020 constructs against current transcript models.
