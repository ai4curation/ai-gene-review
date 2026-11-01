# P (C6G8B2) review notes

2026-10-28. Fetched with `just fetch-gene MAIZE C6G8B2 --alias P`. Confirmed
the record is C6G8B2, GN Name=P, GeneID 542272, Zm00001eb014290; GOA file has
10 rows keyed to C6G8B2 (no experimental rows; IBA + IEA only).

Literature read: PMID:22702356 (full text; UV-B, ChIP of P1 at C2 promoter),
PMID:23113982 (full text; EMSA + ChIP of P1 at Zmf3'h1), PMID:23055943 (full
text; paramutation/Ufo1 at p1 - about regulation of the gene, not the
protein), PMID:22822204 (ChIP-seq; activation and repression), abstracts of
PMID:8313474, PMID:9144964, PMID:15347654, PMID:11148280, PMID:12663550.

Decisions:
- MF: DNA-binding transcription activator activity is the core, supported by
  EMSA/ChIP plus target activation [PMID:23113982 "Using a combination of
  EMSA and ChIP experiments, we established that the Zmf3'h1 gene is a direct
  target of P1"]. DNA binding (IEA) MODIFY to sequence-specific DNA binding,
  which is already present (ARBA) and is supported by the CCT/AACC motif
  [PMID:8313474 "P encodes a Myb homolog that recognizes the sequence
  CCT/AACC"].
- BP: regulation and positive regulation of transcription accepted (binding can
  lead to activation or repression, PMID:22822204). DNA-templated
  transcription MODIFY to positive regulation (TF does not perform
  transcription). Pigment biosynthetic process MODIFY to positive regulation
  of flavonoid biosynthetic process (P1 regulates the enzyme genes; does not
  catalyse). Response to stress MARK_AS_OVER_ANNOTATED: UV-B induction is
  landrace-specific and defense is via downstream metabolites.
- CC: nucleus (IBA, IEA) accepted.
- No NEW rows. The core MF (GO:0001228) and cis-regulatory region binding
  (GO:0000976) are reached by MODIFY of the DNA binding and sequence-specific
  DNA binding rows; the BP side is covered by the accepted regulation rows and
  the pigment row MODIFY to GO:0009963.
- Upstream defects recorded: UniRule UR000400000 (GO:0006351 on a TF) and
  ARBA00027688 (pigment biosynthetic process on a TF).
- C6G8B2 vs P27898: identical over residues 1-250 (249/250), divergent
  C-terminus (P-bioinformatics/RESULTS.md); left as a suggested question.
