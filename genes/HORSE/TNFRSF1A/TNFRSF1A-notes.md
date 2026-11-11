# TNFRSF1A (horse, A0A5F5Q204) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

New folder; no prior review existed for this accession. ProtNLM2 output was not
opened or used.

### Data and literature state

- `just fetch-gene HORSE A0A5F5Q204 --alias TNFRSF1A` created the UniProt, GOA (40 rows)
  and stub files; the stub id is A0A5F5Q204.
- Deep research failed: falcon gave "Failed to authenticate", and the perplexity-lite
  fallback gave HTTP 401 insufficient_quota. No deep-research file was written.
  Literature support therefore comes from the cached human TNFR1 primary papers already
  used in `genes/human/TNFRSF1A` (COMPLETE review), quoted from `publications/`.
- No horse experimental GO annotation exists. Every row is IEA (Ensembl Compara
  ortholog transfer from human P19438 / mouse P25118, InterPro2GO, ARBA, combined
  pipelines) or IBA from PAINT node PTN002930098.

### Identity of the benchmark accession

- Horse has three unreviewed TNFRSF1A entries, all from Ensembl gene
  ENSECAG00000016330: A0A5F5Q204 (475 aa, this one), F6YIE3 (413 aa) and A0A5F5PQM0
  (410 aa). There is no reviewed (Swiss-Prot) horse TNFR1, so UniProt has not
  designated a canonical product.
- Pairwise analysis (`TNFRSF1A-bioinformatics/RESULTS.md`) shows that A0A5F5Q204 is the
  only model with a complete ectodomain: it keeps all 24 cysteines of CRD1-4 (CRD1 holds
  the PLAD), the TM helix and the death domain (87% identical to human). It differs from
  human only before the mature chain. A 22-residue segment (horse residues about 8-29) sits
  ahead of the conserved hydrophobic signal core `ALLALLVEIYPSG`, and this segment is absent
  from A0A5F5PQM0, which has the human-like start `MGLPAVPGLLPP...`. A0A5F5Q204 is therefore
  best described as an alternative gene model (transcript ENSECAT00000066645) with an
  unusual N-terminal extension. Its mature receptor is full length. UniProt flags the
  PROSITE TNFR-Cys prediction as lacking conserved residues and calls only 2 of the 4
  CRDs, but the alignment shows all 4 CRDs with all cysteines present.
- The sibling models are truncated in CRD1/CRD2 (F6YIE3 also lacks the signal peptide).

### Evolutionary grounding

- PANTHER PTHR46861:SF1 for all three horse models, human P19438 and mouse P25118, so
  the receptor is a 1:1 ortholog in the same subfamily.
- PAINT node PTN002930098 (taxon 117571, Euteleostomi) propagates only five terms:
  GO:0005031 TNF receptor activity, GO:0043120 TNF binding, GO:0043235 signaling receptor
  complex, GO:0045121 membrane raft and GO:0006954 inflammatory response. The curators did
  not place NF-kappaB, apoptosis or the many mouse phenotype-derived processes at that node.
  Core signalling processes (TNF-mediated signalling, NF-kappaB, extrinsic apoptosis via
  the death domain) are accepted here on 1:1 orthology plus conservation of the death
  domain. The mouse phenotype-derived processes (valve development, cardiac hypertrophy,
  blood-brain barrier, morphogenesis apoptosis) are treated as over-annotations.
- The PANTHER family review `interpro/panther/PTHR46861/PTHR46861-review.md` (DRAFT)
  describes PTHR46861 as a narrow TNFR1 ortholog family and does not disagree with the
  subfamily placement.

### Modules

modules/tnf_signaling.yaml, modules/nfkb_canonical_signaling.yaml,
modules/death_receptor_apoptotic_signaling.yaml all include TNFRSF1A (human).

### Relative

The canonical-product rule does not apply, because no reviewed horse canonical entry
exists and A0A5F5Q204 itself carries the full receptor. The closest characterised
relative is the human ortholog P19438 (same PANTHER subfamily SF1, same PAINT node). Its
review `genes/human/TNFRSF1A/TNFRSF1A-ai-review.yaml` is status COMPLETE. Mouse Tnfrsf1a
(P25118) also has a folder.
