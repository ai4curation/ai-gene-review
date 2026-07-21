---
title: "PSEPK UPA00539 Pyrroloquinoline quinone biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA00539: Pyrroloquinoline quinone biosynthesis

- Module seed: `pqq_biosynthesis`
- Candidate genes after pathway hole filling: 8
- Primary bucket genes: 7
- Existing review files: 8
- Curated review files: 8
- Existing OpenScientist research files: 8

## Scope

This batch covers formation of pyrroloquinoline quinone (PQQ) from the
ribosomally synthesized precursor peptide PqqA. It includes precursor supply,
PqqD-assisted PqqE cross-linking, pathway-specific proteolysis, PqqB-dependent
oxygenation, and terminal PqqC ring closure. PQQ export and its downstream use
by quinoprotein dehydrogenases are outside this module.

`pqqD1` and `pqqD2` are two PqqD-family implementations in KT2440, not two
universally required pathway steps. The module therefore represents one
PqqD-family peptide-chaperone role and uses both proteins as exemplars.
UniPathway omitted PP_0375, but the KT2440 operon paper identifies this adjacent
S9 serine peptidase as a putative `pqqG`; it was therefore added as a hole-filled
candidate. Its biochemical role is unresolved and it is not forced into the
PqqF reaction or the conserved module core.

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level OpenScientist deep research.
- [x] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Confirm all eight selected gene folders are present.
- [x] Run OpenScientist deep research for selected genes.
- [x] Review each selected gene review for pathway consistency.
- [x] Validate module and gene reviews.
- [x] Open one PR for this module/pathway: [#2197](https://github.com/ai4curation/ai-gene-review/pull/2197).
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `PP_0375` (`pqqG` candidate) | PP_0375 | Q88QV9 | orphan:domain_only_no_pathway | PRESENT | CURATED | COMPLETE | Prolyl oligopeptidase family protein |
| [x] | `pqqE` | PP_0376 | Q88QV8 | unipathway:UPA00539 | PRESENT | CURATED | COMPLETE | PqqA peptide cyclase (EC 1.21.98.4) |
| [x] | `pqqD1` | PP_0377 | Q88QV7 | unipathway:UPA00539 | PRESENT | CURATED | COMPLETE | PqqA binding protein 1 |
| [x] | `pqqC` | PP_0378 | Q88QV6 | unipathway:UPA00539 | PRESENT | CURATED | COMPLETE | Pyrroloquinoline-quinone synthase (EC 1.3.3.11) |
| [x] | `pqqB` | PP_0379 | Q88QV5 | unipathway:UPA00539 | PRESENT | CURATED | COMPLETE | Coenzyme PQQ synthesis protein B |
| [x] | `pqqA` | PP_0380 | Q88QV4 | unipathway:UPA00539 | PRESENT | CURATED | COMPLETE | Coenzyme PQQ synthesis protein A |
| [x] | `pqqF` | PP_0381 | Q88QV3 | unipathway:UPA00539 | PRESENT | CURATED | COMPLETE | Coenzyme PQQ synthesis protein F (EC 3.4.24.-) |
| [x] | `pqqD2` | PP_2681 | Q88JG8 | unipathway:UPA00539 | PRESENT | CURATED | COMPLETE | PqqA binding protein 2 |

## Notes

Generated UTC: 2026-07-09T23:18:04.620542+00:00

## 2026-07-20 curation notes

- Replaced the preservation seed with a reusable five-part module. Molecular
  functions are attached only to leaf annotons; the root carries only the PQQ
  biosynthetic-process concept.
- Used family selectors plus verified KT2440 UniProt exemplars Q88QV3-Q88QV8
  and Q88JG8. PANTHER family data were checked, but no defensible
  Pqq-specific PTN identifiers were available.
- OpenScientist generic module research:
  `modules/pqq_biosynthesis-deep-research-openscientist.md`.
- OpenScientist module + pathway + taxon research:
  `projects/P_PUTIDA/deep-research/PSEPK__pqq_biosynthesis__upa00539-deep-research-openscientist.md`.
- The direct PqqB study (PMID:30811189) supports a non-heme iron hydroxylase
  role. Its experiments used substrate analogs and explicitly leave the native
  substrate and exact pathway ordering unresolved, so the module does not
  overstate a precise PqqB reaction or a fixed PqqF-to-PqqB handoff.
- Hole filling moved PP_0375 from the domain-only orphan queue into this batch.
  PMID:27287323 names it as the KT2440 `pqqG` candidate and places it on the
  `pqqCDEG` transcript. B16 and PA1990 homolog phenotypes were measured using
  extracellular PQQ, so PP_0375 remains a follow-up candidate rather than a new
  PQQ-biosynthetic-process annotation. Its direct substrate and relationship to
  the unrelated M16B PqqG proteins remain open questions.
- The PqqF OpenScientist report imported the two-component M16B PqqF/PqqG
  architecture from *Methylorubrum extorquens* into KT2440. Q88QV3 is instead
  a single-chain M16A-like protein, while PP_0375 is an unrelated S9-family
  candidate. The review records the report as miscited for that claim and does
  not propagate the conflation into the curated model.
- The PqqD1 OpenScientist report correctly retrieves the conserved
  PqqA-chaperone role, but swaps the KT2440 pqqC and pqqE locus assignments and
  reports an alignment without retaining a reproducible artifact. The review
  records that report as miscited and leaves those claims out of the curation.
- The PqqD2 report correctly identifies the distant PP_2681 neighborhood but
  overinterprets proximity and STRING associations as Ped-system
  specialization. Without pqqD2-specific expression, genetics, or binding
  evidence, that remains a suggested experiment rather than a module claim.
- The PP_0375 report retrieves the correct S9-family and locus context but
  treats an ortholog's extracellular-PQQ phenotype as proof of a distinct
  excretion role. Its unsaved AlphaFold, STRING, and alignment measurements are
  also excluded; only independently reproduced comparisons are used.
- The PqqB report retrieves direct hydroxylase and target-structure studies but
  promotes a modeled substrate, AHQQ product, and fixed protease-to-PqqB order
  to established native chemistry. The gene review and module retain those as
  explicit knowledge gaps.
- The PqqE report is useful family-level retrieval, but its direct enzymology
  and auxiliary-cluster structures are from non-KT2440 orthologs and its
  conservation analysis was not retained. Target claims remain grounded in
  UniProt and accessible primary evidence.
- The PqqA report correctly identifies the target peptide and Glu15/Tyr19 pair.
  Its conservation artifact omits source accessions, so exact conservation
  percentages and the inferred leader boundary are not treated as verified.
- The final generic module report correctly separates single-chain M16A,
  two-component M16B, and substitute-protease implementations and recognizes
  proteolysis-versus-PqqB ordering as the main mechanistic gap. One section
  nevertheless states that excision must precede all small-molecule steps; that
  internal overstatement was not propagated into the graph.
- The PqqC report retrieves the correct terminal enzyme and ortholog structural
  work but gives an incorrect one-O2/one-H2O2 net equation. The curated
  three-O2/two-H2O2 Rhea stoichiometry is retained, and non-KT2440 structural
  and quinoprotein studies are treated as family or physiological context.
- The final pathway/taxon report correctly resolves KT2440 to the single-chain
  M16 PqqF route and distinguishes S9-family PP_0375 from the unrelated M16B
  PqqG subunit. Its proposed PqqC identifier `GO:0033735` is wrong (the reviewed
  term is `GO:0033732`), and `GO:0018189` is the pathway BP rather than a PqqE
  molecular function. Its neighborhood-based PqqD2 specialization and
  inconsistent alternative-protease status were not propagated.
