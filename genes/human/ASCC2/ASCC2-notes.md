# ASCC2 notes

## 2026-06-03 Proteostasis PN batch review

Fetched human ASCC2 with `just fetch-gene human ASCC2`; GOA seeded 38 review
annotations from 39 GOA rows. Refreshed PMID caching successfully. Falcon deep
research was attempted with `perplexity-lite` fallback; Falcon timed out after
600 seconds and the fallback failed with a Perplexity API quota 401, so no
provider deep-research file was created. This review therefore uses the cached
primary literature, UniProt, Reactome, and the PN projection report directly.

Core synthesis: ASCC2 is a CUE-domain ubiquitin-binding subunit used in two
well-supported ASCC contexts. In the nucleus, ASCC2 recognizes K63-linked
polyubiquitin signals during alkylation damage and helps recruit ASCC repair
machinery [PMID:29144457 "Proper recruitment of the repair complex requires
recognition of K63-linked polyubiquitin by the CUE"]. Loss of ASCC2 impairs
repair kinetics [PMID:29144457 "Loss of this subunit impedes alkylation adduct
repair kinetics"].

In the proteostasis/RQC context, ASCC2 works with ASCC3 and TRIP4 as the human
RQC-trigger complex. Hashimoto et al. identify the trimeric hRQT complex
[PMID:32099016 "The hRQT complex is composed of ASCC3, ASCC2, and TRIP4"].
Juszkiewicz et al. show ASCC disassembles collided ribosomes [PMID:32579943
"disassembles the leading ribosome in an ATP-dependent reaction"]. Narita et al.
connect this to K63-polyubiquitinated uS10 and ASCC2 ubiquitin binding
[PMID:36302773 "ASCC2 specifically interacts with K63-linked polyubiquitin
chains"].

PN projection decision: the PN report projects ASCC2 to `GO:0072344 rescue of
stalled cytosolic ribosome` as already present, and to `GO:0006515 protein
quality control for misfolded or incompletely synthesized proteins` as a
candidate new-to-GOA group-level RQC annotation
[file:projects/PROTEOSTASIS/reports/pn_projection/pn_projected_annotations.tsv
"ASCC2		Translation|Cytosolic translation|Ribosome-associated QC|Ribosomal
rescue"]. I treated the projection conservatively: keep and support the specific
RQC annotations (`GO:0072344`, `GO:0032790`, `GO:1990116`, `GO:0180022`,
`GO:0070530`), but do not propose adding broad `GO:0006515` because the existing
specific GO annotations already capture ASCC2's proteostasis role.

Annotation decisions:

- `GO:0043130 ubiquitin binding`: MODIFY to `GO:0070530 K63-linked
  polyubiquitin modification-dependent protein binding`.
- `GO:0005515 protein binding`: remove or mark over-annotated depending on
  whether the interaction is high-throughput-only or mechanistically meaningful
  ASCC2-ASCC3 complex evidence.
- `GO:0006260 DNA replication`: REMOVE; the cited evidence supports DNA
  alkylation repair, not ASCC2 involvement in DNA replication.
- Transcription regulation annotations: KEEP_AS_NON_CORE; the ASC-1 complex
  evidence is real [PMID:12077347 "essential role in AP-1, SRF, and NF-kappaB
  transactivation"], but not the core PN-relevant role.
