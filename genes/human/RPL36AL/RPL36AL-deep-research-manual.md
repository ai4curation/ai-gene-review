# Manual deep research: human RPL36AL

Date: 2026-07-18

## Scope and retrieval record

This synthesis addresses the molecular function, biological process, cellular
location, and paralog-specific evidence for human RPL36AL (UniProtKB Q969Q0).
It was prepared after Falcon failed with HTTP 402 and the configured
Perplexity-lite fallback failed with HTTP 401. Sources included the fetched
reviewed UniProt and GOA records; every locally cached GOA-cited publication;
additional primary papers explicitly naming RPL36AL; the open full text of the
retrocopy study; and the current QuickGO record for GO:0000049.

## Gene identity and expression

Uechi et al. identified RPL36AL as an expressed autosomal copy of X-linked
RPL36A. Its coding region lacks introns, supporting origin by retrotransposition,
and gene-specific northern blotting and PCR found broad expression
[PMID:12490704 "RPL36AL is ubiquitously expressed."]. The paper calls the
autosomal copies functional on the basis of intact coding sequence and
expression but explicitly states that their biological role was unresolved.
Accordingly, expression alone is not used as proof of ribosome incorporation.

The fetched reviewed UniProt record assigns RPL36AL to the eukaryotic eL42
family, reports direct protein sequencing and mass-spectrometric identification,
and lists the 60S cytosolic large ribosomal subunit in ComplexPortal. Direct
sequence comparison against the fetched RPL36A record showed one difference in
106 residues: RPL36AL Arg38 versus RPL36A Lys38. This comparison creates a strict
interpretive boundary. Generic eL42 experiments and mass-spectrometric data that
cannot resolve the residue-38 peptide do not establish a paralog-specific
function.

## Ribosomal placement and tRNA binding

Hountondji et al. directly studied RPL36AL in mammalian and human ribosomes. The
2012 work placed RPL36AL Lys53 next to the CCA-end of tRNA specifically in the
P/E hybrid state [PMID:22865768 "this crosslink is specific for a tRNA at the P/E
hybrid site"]. This establishes that RPL36AL is present in the large subunit and
contacts a physiological ribosomal ligand.

The 2014 full-text study extended the result in two ways. First, it measured
direct binding between purified recombinant human RPL36AL and full-length or
3-prime-truncated tRNAs by surface plasmon resonance. The measured dissociation
constants were 1.23-3.02 nM [PMID:25191528 "The KD values in the nanomolar range
reflect high tRNA-binding affinities with full length and truncated tRNA
species."]. Poly(A), poly(U), and their mixture failed to bind in the reported
controls. Second, periodate-crosslinking experiments recovered endogenous
RPL36AL next to P-site tRNA in assembled human 80S ribosomes, including
termination-state complexes containing eRF1.

These experiments justify GO:0000049 tRNA binding as a new molecular-function
annotation. They also strengthen the existing structural constituent of ribosome,
cytosolic large ribosomal subunit, and cytoplasmic translation assignments.
RPL36AL is a ubiquitously expressed autosomal eL42 paralog whose directly
demonstrated molecular activity is tRNA binding within the cytosolic 60S
ribosomal subunit.

## Boundaries on catalytic and elongation claims

The 2014 paper tested whether isolated RPL36AL hydrolyzes peptidyl-tRNA, motivated
by the protein's GGQ-containing motif. This provocative in-vitro observation is
not sufficient to assign peptidyl-tRNA hydrolase activity as a normal molecular
function of the ribosome-bound protein, and no such term is proposed.

The 2024 HEK293T mutagenesis study showed that double substitutions in a conserved
human eL42 motif reduce polysomes and impair deacylated tRNA dissociation from the
E site [PMID:37716853 "cooperative interactions implicating the eL42 residues
Q45, Q51, and K53 play a critical role"]. The abstract does not state an
accession, and all mentioned residues are shared by RPL36A and RPL36AL. The study
is useful mechanistic context but is not used to make a paralog-specific
translational-elongation annotation.

## GOA-cited high-throughput evidence

PMID:25416956 is a proteome-scale binary-interaction map. The GOA row reports
KRTAP10-7 as an RPL36AL interactor. This is retained as physical-interaction data,
but GO:0005515 protein binding is marked over-annotated because it does not encode
a defined RPL36AL activity.

PMID:25468996 used E-cadherin proximity proteomics followed by GFP-fusion
localization of selected candidates. The GOA record assigns RPL36AL to the
nucleus. The full narrative describes the localization workflow and notes that
many translation-related candidates were non-junctional, but it does not name
RPL36AL. The gene-specific result resides in a supplementary candidate table
that was not accessible during this review. Consistent with the instruction not
to overrule an experimental curator from incomplete evidence, the nucleus record
is marked UNDECIDED rather than removed.

## Literature inspected but not used for annotation transfer

- PMID:3542712 cloned a human L44-homologous cDNA before the RPL36A/RPL36AL gene
  distinction was established. It is useful history but not treated as clean
  paralog-specific functional evidence.
- PMID:37716853 defines an eL42 motif role but does not identify the paralog in
  its accessible abstract.
- Reviewed RPL36A annotations and publications were consulted only to define the
  paralog boundary; none was transferred to RPL36AL without independent support.

## Curation-ready conclusions

1. Accept the seven ribosome, translation, and cytoplasm annotations.
2. Mark the high-throughput generic protein-binding annotation as over-annotated.
3. Leave the nuclear IDA annotation undecided because its gene-specific
   supplementary evidence could not be verified.
4. Add GO:0000049 tRNA binding with IDA evidence from PMID:25191528 and
   corroboration from PMID:22865768.
5. Represent structural ribosome membership and tRNA binding as the two linked
   core molecular activities; do not infer RPL36A-specific phenotypes or a unique
   specialized-ribosome program.
