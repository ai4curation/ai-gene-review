# HPR / HPR1 (At1g68010, Q9C9W5) curation notes

**Deep research could not be run** in this environment (no provider API keys). These notes are a
literature summary built only from cached publications (`publications/PMID_*.md`) and the UniProt
record (`HPR-uniprot.txt`). No `*-deep-research-*.md` file exists for this gene.

## Identity and family

- HPR1 (UniProt gene name HPR) is the peroxisomal NADH-dependent hydroxypyruvate reductase (glycerate
  dehydrogenase, EC 1.1.1.29), a member of the D-isomer specific 2-hydroxyacid dehydrogenase family
  (PANTHER PTHR10996:SF257; Pfam PF00389/PF02826). It has a C-terminal microbody targeting signal
  [PMID:9177031 "Deduced amino acid sequences revealed that HPR in Arabidopsis contained the
  carboxy-terminal targeting signal to microbodies."]. Encoded by a single gene that, unlike in pumpkin,
  is not alternatively spliced into a cytosolic form [PMID:9177031 "the structure of the genomic DNA
  indicated that the Arabidopsis HPR gene did not undergo alternative splicing"]. UniProt nevertheless
  lists a second isoform differing by one residue (K264 -> KV), which does not affect the PTS1.

## Activity

- Catalyses NADH-dependent reduction of hydroxypyruvate to glycerate [PMID:22303256 "In Arabidopsis,
  the peroxisomal reaction is catalyzed by HPR1 (At1g68010) using NADH as a co-factor"].
- Recombinant HPR1 was assayed alongside HPR2 with several substrate/cofactor combinations; both show
  relaxed specificity [PMID:18952776 "This broad-range effect was to be expected due to the relaxed
  substrate and cofactor specificities of HPR1 and, even more so, of HPR2"]. The cached text lacks the
  Table 1 values, so the glyoxylate and NADPH rates of HPR1 cannot be checked here.
- hpr1 knockouts retain only ~5% of leaf NADH-HPR activity [PMID:18952776 "initial measurements
  indicated very low (∼5% of wild-type levels) NADH-dependent hydroxypyruvate reductase activity in
  leaf extracts of both lines."].

## Localization

- Immuno-EM: exclusively peroxisomal in green leaves [PMID:9177031 "Immunoelectron microscopy revealed
  that Arabidopsis HPR protein was exclusively localized in leaf peroxisomes in green leaves."];
  leaf peroxisome proteomics (PMID:12154131, PMID:17951448).
- Proteomic hits in chloroplast, mitochondrion, apoplast and crude cytosol fractions treated as
  contamination (projects/ARATH/organelle-audit.md rule 3).

## Physiological role

- Photorespiration: HPR1 performs the main peroxisomal reduction of hydroxypyruvate; hpr1 single mutants
  are only mildly air-sensitive because cytosolic HPR2 (At1g79870) and plastid HPR3 (At1g12550) provide
  bypasses; hpr1 hpr2 doubles are air-sensitive [PMID:18952776 "The combined deletion of both HPR1 and
  HPR2, however, results in distinct air-sensitivity and a dramatic reduction in photosynthetic
  performance."; "showing that HPR1 plays the dominant role in photorespiration"]
  [PMID:21205613 "most of which is subsequently reduced to glycerate by the NADH-dependent peroxisomal
  enzyme HP reductase (HPR1)"].
- hpr1 increases the CO2 compensation point and non-respiratory CO2 release per oxygenation (PMID:21567290,
  abstract only).
- Seed germination: HPR1 reoxidizes peroxisomal NADH for beta-oxidation only when peroxisomal MDH is
  absent [PMID:19812894 "These results indicate that HPR can oxidise NADH at sufficient rate in the
  absence of PMDH to support beta-oxidation and hence seed germination."]. Conditional, so not added as
  a new annotation.
- Expression: shoot-specific, induced by light and mildly by drought [PMID:19529821 "This suggests the
  AtHPR expression is up-regulated by drought"].

## Annotation-specific notes

- glyoxylate reductase (NADPH) IBA (PTN000107947; donors HPR2, HPR3, E. coli GhrA/GhrB, human GRHPR):
  HPR1 is NADH-preferring; no cached data on HPR1 NADPH-glyoxylate activity -> UNDECIDED.
- cytosol: HDA (crude cytosolic fraction) and IBA (bacterial/cytosolic donors) on a PTS1 protein that
  immuno-EM places exclusively in peroxisomes. One action for the term group (organelle-audit rule 6):
  MARK_AS_OVER_ANNOTATED for both.
- poly(U) RNA binding IDA (PMID:17511964, abstract-only): poly(U)-affinity enrichment explicitly aimed at
  nucleotide-binding motifs; an NAD-binding Rossmann-fold dehydrogenase is expected to be retained.
  Marked over-annotated.

## Module comparison (modules/photorespiration_c2_cycle.yaml, peroxisomal_hpr1_variant)

Module asserts GO:0008465 / GO:0009853 / GO:0005777 for HPR1. This review agrees on all three. The
review also accepts the more specific GO:0009854 (oxidative photosynthetic carbon pathway, is_a
photorespiration), which is supported by IMP.
