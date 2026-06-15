# SORBI_3003G204000 (C5XPJ5) — research notes

UniProt: **C5XPJ5** (`C5XPJ5_SORBI`), *Sorghum bicolor* (NCBI:txid4558), 188 aa,
PE=4 (Predicted), TrEMBL/unreviewed. Locus / ORF name **SORBI_3003G204000**
(Gramene EES00992; chromosome 3). No assigned gene symbol; "Uncharacterized
protein".

## Deep-research tooling note (RESOLVED)
Initial failure was operator error: I invoked
`src/ai_gene_review/tools/deep_research_unified.py` directly, which does not
populate the `gene_research_go_focused.md` template variables (hence
`Missing template variables: gene_id, gene_info, protein_family, ...`). The
correct entry point is the justfile target `just deep-research-falcon` ->
`scripts/deep_research_wrapper.py` -> `deep-research-client research --template
... --var ...`, which parses the UniProt file and supplies every `--var`. The
run succeeded once invoked correctly:
`uv run python scripts/deep_research_wrapper.py SORBI C5XPJ5 falcon --alias
SORBI_3003G204000 --fallback asta openscientist`, producing
`SORBI_3003G204000-deep-research-falcon.md` (+ artifacts) and
`-deep-research-asta.md`. (Env notes: `just` was not installed in this container
-- installed via `uv tool install rust-just`; `perplexity` has no API key here,
so only falcon/asta/openscientist are available and a `perplexity-lite` fallback
is unusable.)

The falcon report independently reaches the same conclusion as this review --
"the most parsimonious functional assignment is that C5XPJ5 encodes a putative
SPC24 subunit of the NDC80 outer-kinetochore complex" -- and found no paper
naming C5XPJ5/SORBI_3003G204000 (all statements are domain/orthology inference).
Additional corroborating sources it surfaced: Xie 2024 (plant kinetochore
complex / KMN network), Kozgunova 2025 (recent advances in plant kinetochores),
Ustinov 2020 (NDC80 complex structure: SPC24/SPC25 as structural adaptor). No
gene-specific PMIDs were cached (`fetch-gene-pmids` found none; the only seeded
reference is GO_REF:0000002).

## Family / domain assignment (basis of the single annotation)
- InterPro **IPR044951** "SPC24-like" → InterPro2GO maps to GO:0051983
  (this is the source of the only GOA annotation, via GO_REF:0000002 / IEA).
- PANTHER **PTHR35730** "KINETOCHORE PROTEIN SPC24 HOMOLOG-RELATED"
  (subfamily PTHR35730:SF2). The *single reviewed (Swiss-Prot) member* of this
  PANTHER family is **Q67XT3 = Arabidopsis thaliana SPC24 homolog (gene SPC24 /
  MUN)** [interpro/panther/PTHR35730/PTHR35730-entries.csv]. This makes the
  family assignment, and hence the SPC24-homolog identity, well supported.
- eggNOG ENOG502S0WN; HOGENOM CLU_156988_0_0_1. AlphaFoldDB model available.
- Short (188 aa) protein consistent with SPC24 (Arabidopsis SPC24 = 201 aa);
  SPC24 proteins have an N-terminal coiled-coil and a C-terminal RWD globular
  domain that, with SPC25, forms the kinetochore-anchoring module of NDC80.

## What SPC24 does (background, from orthologs)
- SPC24 is one of the four subunits of the **NDC80 (NDC80–NUF2–SPC24–SPC25)
  outer-kinetochore complex**, the principal microtubule-binding interface of
  the kinetochore. NDC80/NUF2 bind microtubules at one end; SPC24/SPC25 anchor
  the complex to the inner kinetochore (MIND/Mis12 complex). The complex is
  essential for end-on kinetochore–microtubule attachment, chromosome
  segregation, and spindle-assembly-checkpoint signaling.
  [WebSearch synthesis; Pharos SPC24 (Tbio)]
- **Arabidopsis SPC24 = MUN (MERISTEM UNSTRUCTURED)**: loss of function causes
  embryo arrest, stunted/disorganized meristems, low cell-division rate,
  aneuploidy and chromosome-segregation defects — i.e. a bona fide NDC80-complex
  kinetochore subunit required for proper mitotic chromosome segregation.
  [PMID:29356153 Shin et al. 2018 Plant J, "MUN (MERISTEM UNSTRUCTURED),
  encoding a SPC24 homolog of NDC80 kinetochore complex, affects development
  through cell division in Arabidopsis thaliana"]
- AtNUF2 (another NDC80-complex subunit) similarly modulates spindle
  microtubule organization and chromosome segregation in mitosis.
  [PMID:33993566]

## Assessment of the existing annotation
- **GO:0051983 "regulation of chromosome segregation" (IEA, GO_REF:0000002,
  from InterPro IPR044951)**: Direction is correct — an SPC24/NDC80-complex
  homolog is genuinely a kinetochore protein involved in chromosome segregation.
  The IEA family→term mapping is conservative and defensible (NDC80 complex
  both executes attachment and contributes to spindle-checkpoint regulation of
  the metaphase→anaphase transition). For sorghum there is no experimental
  evidence, so this electronic annotation should be kept (ACCEPT) as a
  reasonable, non-overreaching inference. Note for curators: more *direct*
  terms supported by the orthology would be the **NDC80 complex** /
  **condensed chromosome kinetochore** cellular component (GO:0031262 /
  GO:0000776), **chromosome segregation** (GO:0007059), and **microtubule
  binding** (GO:0008017) molecular function — but these are not currently in
  GOA for this entry and rest on orthology, not direct evidence, so they are
  recorded as proposed/possible rather than asserted.

## Identifiers
- GO:0051983 regulation of chromosome segregation (parents incl. GO:0033045
  regulation of sister chromatid segregation cluster) — verified via QuickGO.
- PMID:29356153 — Arabidopsis MUN/SPC24 (verified via PubMed search).
- PMID:33993566 — AtNUF2 (verified via PubMed search).
- Genome refs for the entry: PMID:19189423 (Sorghum genome, Paterson 2009),
  PMID:29161754 (Sorghum reference genome v3, McCormick 2018) — large-scale
  genome papers, not functional evidence for this locus.
