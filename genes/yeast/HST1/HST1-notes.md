# HST1 review notes

## Identity and scope

- Target: *Saccharomyces cerevisiae* HST1 / YOL068C, UniProt P53685, a
  503-residue class-I sirtuin. This is the canonical NAD-dependent deacetylase,
  not P50111/YMR273C (Zds1), whose obsolete `HST1` synonym caused the former
  repository collision.
- OpenScientist completed a GO-focused synthesis on 2026-08-12. Its Markdown
  report and HTML/PDF artifacts are preserved in this gene directory.

## Core mechanism

- Hst1 is the catalytic subunit of a locus-specific Sum1-Rfm1-Hst1 repressor.
  Rfm1 bridges Sum1 and Hst1 and is required for their interaction
  [PMID:12612074, "Rfm1 interacts with both Sum1 and Hst1 and is required for
  the Sum1-Hst1 interaction."].
- The complex represses middle-sporulation genes during vegetative growth.
  Modern chromatin analysis shows that Sum1 and Hst1 remain associated with
  these loci and maintain deacetylation primarily at H4K5
  [PMID:29066473, "Set1 appeared to promote the association of the
  sequence-specific DNA binding protein Sum1 and the HDAC Hst1 with middle
  sporulation genes to maintain deacetylation, primarily at H4K5, and gene
  repression."].
- Hst1 also couples intracellular NAD+ to repression of de novo NAD
  biosynthesis and thiamine-biosynthesis genes. These are genuine target
  programs of the same promoter-deacetylation mechanism rather than distinct
  catalytic functions [PMID:20439498, "multiple thiamine ( THI ) genes in
  Saccharomyces cerevisiae are also regulated by the intracellular NAD +
  concentration via the NAD + -dependent histone deacetylase (HDAC) Hst1"].
- Sum1 recruits Hst1 to a subset of replication origins, where loss of Hst1
  increases H4K5 acetylation and reduces initiation efficiency
  [PMID:18990212, "We identified seven ARS elements whose initiation capacity
  depended on Sum1 and Hst1."]. This direct extra role is retained as non-core.

## Native versus conditional silencing

- Native Hst1 is not a Sir2-like regional silencing enzyme. The original HST1
  characterization reports no phenotype in Sir2-dependent HML or rDNA
  silencing [PMID:8810037, "Disruption of HST1 has shown no phenotype with
  respect to mechanisms in which SIR2 has a role, namely, regional silencing
  of HML alpha, or in rDNA recombination."]. The telomeric-region and
  subtelomeric-heterochromatin inferences are therefore removed.
- Hst1 can silence HMR when the gain-of-function Sum1-1 protein aberrantly
  recruits it. Those experimental mating-type-silencing annotations are kept
  as conditional/non-core rather than treated as Hst1's native function.
- PMID:27185881 and PMID:16051752 are abstract-only caches whose visible text
  does not expose the Hst1 experiments underlying two curated annotations.
  Those experimental calls remain `UNDECIDED`; the review does not overrule
  curators from incomplete evidence.

## Annotation synthesis

- Core molecular function: NAD-dependent histone deacetylase activity
  (GO:0017136), acting in the Sum1-Rfm1-Hst1 histone deacetylase complex.
- Core process and location: negative regulation of DNA-templated
  transcription on nuclear chromatin.
- H3K9-, H3K14-, and H4K16-specific IBA activities are marked
  over-annotated. Hst1-specific studies identify H4K5 as the predominant
  residue. Current GO has an H4K5 hydrolytic-mechanism term but no
  NAD-dependent H4K5 child of GO:0017136, so the review proposes that missing
  term while retaining the generic NAD-dependent activity as the core function.
- PMID:12972620 directly demonstrates Hst1-dependent repression of de novo NAD+
  biosynthesis genes, but GO lacks a corresponding negative-regulation term.
  The review proposes that process term rather than forcing the evidence into
  the unregulated biosynthetic-process term.
- Set3C membership is experimentally real, but Hst1 is largely dispensable for
  Set3C repression and the Sum1-Rfm1-Hst1 complex is its principal functional
  context. Set3C annotations are retained as non-core.
- Generic `protein binding` annotations are marked over-annotated; specific
  recruitment by Rfm1 and complex membership are biologically informative.
