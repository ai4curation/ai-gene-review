---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T18:51:53.332617'
end_time: '2026-07-20T20:11:23.673576'
duration_seconds: 4770.34
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Pyrroloquinoline quinone biosynthesis
  module_summary: Pyrroloquinoline quinone (PQQ) is made from conserved glutamate
    and tyrosine residues in the short ribosomally synthesized precursor peptide PqqA.
    A PqqD-family peptide chaperone presents PqqA to the radical-SAM enzyme PqqE,
    which forms the defining carbon-carbon cross-link. Proteolytic processing and
    PqqB-dependent oxygenation both contribute to formation of a late small-molecule
    precursor, although their relative order is unresolved. PqqC completes oxidative
    ring closure to mature PQQ. PQQ export and use by quinoprotein dehydrogenases
    are downstream of this module.
  module_outline: "- Pyrroloquinoline quinone biosynthesis\n  - 1. PqqA precursor-peptide\
    \ supply\n  - PqqA precursor-peptide supply\n    - PqqA precursor-peptide role\
    \ (molecular player: PqqA precursor-peptide family)\n  - 2. PqqD-assisted radical-SAM\
    \ cross-link formation\n  - PqqD-assisted PqqE cross-linking\n    - PqqD peptide-chaperone\
    \ role (molecular player: PqqD peptide-chaperone family)\n    - PqqE PqqA peptide\
    \ cyclase activity (molecular player: PqqE radical-SAM peptide cyclase family;\
    \ activity or role: cyclase activity)\n  - Proteolytic release of a PqqA-derived\
    \ intermediate\n  - PqqA-derived precursor proteolysis\n    - Alternative versions\
    \ by protease repertoire: PQQ precursor-proteolysis implementation\n      - Single-chain\
    \ PqqF/M16A-like protease route\n        - Single-chain PqqF metalloendopeptidase\
    \ activity (molecular player: single-chain PqqF M16 peptidase family; activity\
    \ or role: metalloendopeptidase activity)\n      - Two-component PqqF/PqqG M16B\
    \ protease route\n        - PqqF/PqqG M16B metalloendopeptidase complex (molecular\
    \ player: PqqF/PqqG M16B protease complex; activity or role: metalloendopeptidase\
    \ activity)\n      - Alternative cellular-protease route\n        - Alternative\
    \ PqqA-pathway peptidase activity (molecular player: peptidase activity; activity\
    \ or role: peptidase activity)\n  - PqqB-dependent oxygenation\n  - PqqB-dependent\
    \ precursor oxygenation\n    - PqqB oxygen-incorporating oxidoreductase activity\
    \ (molecular player: PqqB family; activity or role: oxidoreductase activity, acting\
    \ on paired donors, with incorporation or reduction of molecular oxygen)\n  -\
    \ 5. Terminal oxidative ring closure\n  - PqqC terminal PQQ formation\n    - Pyrroloquinoline-quinone\
    \ synthase activity (molecular player: PqqC-like family; activity or role: pyrroloquinoline-quinone\
    \ synthase activity)"
  module_connections: '- PqqA precursor-peptide supply feeds into PqqD-assisted PqqE
    cross-linking: PqqA supplies the precursor peptide bound by PqqD and modified
    by PqqE.

    - PqqD-assisted PqqE cross-linking feeds into PqqA-derived precursor proteolysis:
    A PqqA-derived precursor undergoes pathway-associated proteolytic processing.

    - PqqD-assisted PqqE cross-linking feeds into PqqB-dependent precursor oxygenation:
    PqqB acts on an intermediate derived from cross-linked PqqA.

    - PqqA-derived precursor proteolysis feeds into PqqC terminal PQQ formation: Proteolysis
    is required to generate the small-molecule precursor used late in the pathway.

    - PqqB-dependent precursor oxygenation feeds into PqqC terminal PQQ formation:
    PqqB-dependent oxygenation contributes to formation of the late PqqC substrate.'
  pathway_query: UPA00539
  pathway_id: UPA00539
  pathway_name: UniPathway UPA00539
  pathway_source: UniPathway
  pathway_context: 'Resolved local bucket unipathway:UPA00539 with 7 primary genes;
    module area: unipathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '7'
  candidate_genes: '- pqqE: PP_0376 | Q88QV8 | PqqA peptide cyclase (EC 1.21.98.4)
    (Coenzyme PQQ synthesis protein E) (Pyrroloquinoline quinone biosynthesis protein
    E) (EC 1.21.98.4; primary bucket unipathway:UPA00539)

    - pqqD1: PP_0377 | Q88QV7 | PqqA binding protein 1 (Coenzyme PQQ synthesis protein
    D 1) (Pyrroloquinoline quinone biosynthesis protein D 1) (primary bucket unipathway:UPA00539)

    - pqqC: PP_0378 | Q88QV6 | Pyrroloquinoline-quinone synthase (EC 1.3.3.11) (Coenzyme
    PQQ synthesis protein C) (Pyrroloquinoline quinone biosynthesis protein C) (EC
    1.3.3.11; primary bucket unipathway:UPA00539)

    - pqqB: PP_0379 | Q88QV5 | Coenzyme PQQ synthesis protein B (Pyrroloquinoline
    quinone biosynthesis protein B) (primary bucket unipathway:UPA00539)

    - pqqA: PP_0380 | Q88QV4 | Coenzyme PQQ synthesis protein A (Pyrroloquinoline
    quinone biosynthesis protein A) (primary bucket unipathway:UPA00539)

    - pqqF: PP_0381 | Q88QV3 | Coenzyme PQQ synthesis protein F (EC 3.4.24.-) (Pyrroloquinoline
    quinone biosynthesis protein F) (EC 3.4.24.-; primary bucket unipathway:UPA00539)

    - pqqD2: PP_2681 | Q88JG8 | PqqA binding protein 2 (Coenzyme PQQ synthesis protein
    D 2) (Pyrroloquinoline quinone biosynthesis protein D 2) (primary bucket unipathway:UPA00539)'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 2
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__pqq_biosynthesis__upa00539-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__pqq_biosynthesis__upa00539-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Pyrroloquinoline quinone biosynthesis in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: UPA00539
- Resolved ID: UPA00539
- Resolved name: UniPathway UPA00539
- Source: UniPathway

Resolved local bucket unipathway:UPA00539 with 7 primary genes; module area: unipathway.

## Candidate Genes From Local Metadata

Candidate gene count: 7

- pqqE: PP_0376 | Q88QV8 | PqqA peptide cyclase (EC 1.21.98.4) (Coenzyme PQQ synthesis protein E) (Pyrroloquinoline quinone biosynthesis protein E) (EC 1.21.98.4; primary bucket unipathway:UPA00539)
- pqqD1: PP_0377 | Q88QV7 | PqqA binding protein 1 (Coenzyme PQQ synthesis protein D 1) (Pyrroloquinoline quinone biosynthesis protein D 1) (primary bucket unipathway:UPA00539)
- pqqC: PP_0378 | Q88QV6 | Pyrroloquinoline-quinone synthase (EC 1.3.3.11) (Coenzyme PQQ synthesis protein C) (Pyrroloquinoline quinone biosynthesis protein C) (EC 1.3.3.11; primary bucket unipathway:UPA00539)
- pqqB: PP_0379 | Q88QV5 | Coenzyme PQQ synthesis protein B (Pyrroloquinoline quinone biosynthesis protein B) (primary bucket unipathway:UPA00539)
- pqqA: PP_0380 | Q88QV4 | Coenzyme PQQ synthesis protein A (Pyrroloquinoline quinone biosynthesis protein A) (primary bucket unipathway:UPA00539)
- pqqF: PP_0381 | Q88QV3 | Coenzyme PQQ synthesis protein F (EC 3.4.24.-) (Pyrroloquinoline quinone biosynthesis protein F) (EC 3.4.24.-; primary bucket unipathway:UPA00539)
- pqqD2: PP_2681 | Q88JG8 | PqqA binding protein 2 (Coenzyme PQQ synthesis protein D 2) (Pyrroloquinoline quinone biosynthesis protein D 2) (primary bucket unipathway:UPA00539)

## Generic Module Context

### Working Scope

Pyrroloquinoline quinone (PQQ) is made from conserved glutamate and tyrosine residues in the short ribosomally synthesized precursor peptide PqqA. A PqqD-family peptide chaperone presents PqqA to the radical-SAM enzyme PqqE, which forms the defining carbon-carbon cross-link. Proteolytic processing and PqqB-dependent oxygenation both contribute to formation of a late small-molecule precursor, although their relative order is unresolved. PqqC completes oxidative ring closure to mature PQQ. PQQ export and use by quinoprotein dehydrogenases are downstream of this module.

### Provisional Biological Outline

- Pyrroloquinoline quinone biosynthesis
  - 1. PqqA precursor-peptide supply
  - PqqA precursor-peptide supply
    - PqqA precursor-peptide role (molecular player: PqqA precursor-peptide family)
  - 2. PqqD-assisted radical-SAM cross-link formation
  - PqqD-assisted PqqE cross-linking
    - PqqD peptide-chaperone role (molecular player: PqqD peptide-chaperone family)
    - PqqE PqqA peptide cyclase activity (molecular player: PqqE radical-SAM peptide cyclase family; activity or role: cyclase activity)
  - Proteolytic release of a PqqA-derived intermediate
  - PqqA-derived precursor proteolysis
    - Alternative versions by protease repertoire: PQQ precursor-proteolysis implementation
      - Single-chain PqqF/M16A-like protease route
        - Single-chain PqqF metalloendopeptidase activity (molecular player: single-chain PqqF M16 peptidase family; activity or role: metalloendopeptidase activity)
      - Two-component PqqF/PqqG M16B protease route
        - PqqF/PqqG M16B metalloendopeptidase complex (molecular player: PqqF/PqqG M16B protease complex; activity or role: metalloendopeptidase activity)
      - Alternative cellular-protease route
        - Alternative PqqA-pathway peptidase activity (molecular player: peptidase activity; activity or role: peptidase activity)
  - PqqB-dependent oxygenation
  - PqqB-dependent precursor oxygenation
    - PqqB oxygen-incorporating oxidoreductase activity (molecular player: PqqB family; activity or role: oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen)
  - 5. Terminal oxidative ring closure
  - PqqC terminal PQQ formation
    - Pyrroloquinoline-quinone synthase activity (molecular player: PqqC-like family; activity or role: pyrroloquinoline-quinone synthase activity)

### Known Relationships Among Steps

- PqqA precursor-peptide supply feeds into PqqD-assisted PqqE cross-linking: PqqA supplies the precursor peptide bound by PqqD and modified by PqqE.
- PqqD-assisted PqqE cross-linking feeds into PqqA-derived precursor proteolysis: A PqqA-derived precursor undergoes pathway-associated proteolytic processing.
- PqqD-assisted PqqE cross-linking feeds into PqqB-dependent precursor oxygenation: PqqB acts on an intermediate derived from cross-linked PqqA.
- PqqA-derived precursor proteolysis feeds into PqqC terminal PQQ formation: Proteolysis is required to generate the small-molecule precursor used late in the pathway.
- PqqB-dependent precursor oxygenation feeds into PqqC terminal PQQ formation: PqqB-dependent oxygenation contributes to formation of the late PqqC substrate.

## Assignment

Write a species-aware review of this module/pathway in the target organism. The
goal is not a generic pathway essay; the goal is to support manual module
satisfiability and gene annotation curation.

Treat the candidate gene list as a starting point, not ground truth. Use the
literature and authoritative resources to decide whether each expected pathway
step is present, absent, ambiguous, replaced by a lineage-specific alternative,
or represented by a likely over-propagated annotation.

Prioritize direct evidence from the target species/strain. When using evidence
from related organisms, state the organism and explain whether transfer to the
target taxon is strong, weak, or uncertain. Distinguish *Pseudomonas putida*
KT2440 evidence from broader *Pseudomonas* or generic bacterial evidence.

## Questions To Address

1. **Pathway boundaries**
   - What exact biochemical or cellular process is included?
   - Which neighboring pathways or broad overview maps should be kept separate?
   - Are there alternate names or database-specific definitions for this pathway?

2. **Satisfiability in the target taxon**
   - Which expected steps are encoded by candidate genes?
   - Which steps are missing from the metadata but likely present under a
     different gene name, paralog, or enzyme family?
   - Which steps are probably not expected in this organism?

3. **Candidate gene assessment**
   - For each high-confidence gene, summarize the likely role, evidence type,
     and any curation-relevant caveats.
   - Identify paralog ambiguity, broad EC/GO mappings, and likely annotation
     over-propagation.
   - Note genes that should be promoted to full `fetch-gene` review.

4. **Module implications**
   - What module steps should be marked covered, candidate_uncertain, gap,
     not_expected_in_target_taxon, or module_needs_revision?
   - Are existing generic module boundaries wrong for this organism?
   - Are new module documents or GO term requests likely needed?

5. **Evidence and open questions**
   - Which conclusions are supported by direct experiments?
   - Which are inferred from homology, pathway databases, or neighboring genes?
   - What experiments or expert questions would resolve the important gaps?

## Output Format

Use concise review sections:

1. Executive summary
2. Target-organism pathway definition
3. Expected step model
4. Candidate genes and evidence
5. Gaps, ambiguities, and likely over-annotations
6. Module and GO-curation recommendations
7. Genes to promote to full review
8. Key references

Include citations for major claims, preferably PMIDs or DOIs. Be explicit about
uncertainty, species transfer, and whether evidence is direct for the target
organism.

## Output

# Species-Aware Review: Pyrroloquinoline Quinone (PQQ) Biosynthesis in *Pseudomonas putida* KT2440

**Taxon:** *Pseudomonas putida* KT2440 (PSEPK, NCBI:txid160488, proteome UP000000556)
**Module / bucket:** UniPathway UPA00539 (pyrroloquinoline quinone biosynthesis)
**Date:** 2026-07-21

---

## 1. Executive summary

The UPA00539 PQQ-biosynthesis module is **fully satisfiable** in *P. putida* KT2440. All five conserved catalytic steps map to a compact chromosomal cluster, **PP_0376–PP_0381** (`pqqE-pqqD1-pqqC-pqqB-pqqA-pqqF`, i.e. the *pqqFABCDE* operon read 5'→3'): precursor-peptide supply (PqqA), PqqD-assisted radical-SAM cross-linking (PqqD1 + PqqE), PqqB oxygenation, PqqF proteolysis, and PqqC terminal ring closure. PQQ production is functionally confirmed — KT2440 depends on PQQ as the cofactor for its periplasmic glucose dehydrogenase (Gcd) (PMID 27287323).

Two curation caveats dominate:
1. **Proteolysis route.** KT2440 encodes a **single-chain M16 PqqF** (PP_0381, 766 aa, InterPro IPR011844). The generic module's "two-component PqqF/PqqG M16B protease" alternative derives from the α-proteobacterium *Methylobacterium extorquens* (PMID 31427437) and **does not apply** here. A gene sometimes labelled *pqqG* in KT2440 (**PP_0375**) is a **Peptidase S9 / prolyl-oligopeptidase**, not an M16B partner — a naming collision that should not be curated as the two-component route.
2. **Paralog ambiguity.** **PqqD2 (PP_2681)** is a standalone PqqD-family paralog embedded among quinoprotein dehydrogenase genes; its assignment to UPA00539 is **candidate_uncertain** and may be over-propagated. The operon-embedded **PqqD1 (PP_0377)** is the high-confidence chaperone.

---

## 2. Target-organism pathway definition

**Included process.** Conversion of the ribosomally synthesized precursor peptide **PqqA** into the mature small-molecule redox cofactor **PQQ**. This is a RiPP (ribosomally synthesized and post-translationally modified peptide) pathway comprising: (i) a C–C cross-link between a specific Glu and Tyr in PqqA by the radical-SAM enzyme PqqE, presented by the PqqD RiPP-recognition element (RRE); (ii) proteolytic excision of the cross-linked di-amino-acid intermediate; (iii) PqqB-dependent oxygenation/hydroxylation; and (iv) an eight-electron/eight-proton oxidative ring closure by PqqC yielding PQQ (PMID 32731194).

**Keep separate (neighboring processes, downstream or unrelated).**
- **PQQ *utilization*** by quinoprotein dehydrogenases — glucose dehydrogenase *gcd* (PP_1444), PQQ-dependent alcohol dehydrogenases (e.g. *pedH/exaA*-type) — is downstream and should not be folded into UPA00539.
- **PQQ export/secretion** and the **PedS2/PedR2** and **AgmR** regulatory systems (PMIDs 30158283, 11954793) are regulatory/transport, not biosynthetic.
- Adjacent operon genes **PP_0382 (davA)** and **PP_0383 (davB, tryptophan 2-monooxygenase)** belong to lysine/amino-acid catabolism, not PQQ synthesis, despite chromosomal proximity.
- Broad overview maps ("cofactor biosynthesis", "metabolic pathways") should not substitute for the specific module.

**Alternate names / DB definitions.** UniPathway UPA00539; KEGG module for PQQ biosynthesis; "coenzyme PQQ synthesis" (Uni­Prot Pqq nomenclature, letters A–F). Enzyme names: PqqE = "PqqA peptide cyclase" (EC 1.21.98.4); PqqC = "pyrroloquinoline-quinone synthase" (EC 1.3.3.11).

---

## 3. Expected step model (generic → KT2440 status)

| # | Generic step | Enzyme/player | KT2440 gene | Status |
|---|--------------|---------------|-------------|--------|
| 1 | PqqA precursor supply | PqqA precursor peptide | **PP_0380 pqqA** | **covered** |
| 2 | PqqD-assisted PqqE cross-link | PqqD RRE + PqqE radical-SAM | **PP_0377 pqqD1 + PP_0376 pqqE** | **covered** |
| 3 | Proteolytic release of intermediate | protease (M16 single-chain *or* M16B two-component *or* other) | **PP_0381 pqqF (single-chain M16)** | **covered (single-chain route)** |
| 4 | PqqB-dependent oxygenation | PqqB dual hydroxylase | **PP_0379 pqqB** | **covered** |
| 5 | Terminal oxidative ring closure | PqqC synthase | **PP_0378 pqqC** | **covered** |

The two alternative proteolysis sub-versions not used here (M16B two-component; generic cellular protease) should be marked **not_expected_in_target_taxon** for KT2440.

---

## 4. Candidate genes and evidence

| Gene | Locus | Acc | Length | Role / signature | Evidence class | Curation note |
|------|-------|-----|--------|------------------|----------------|---------------|
| **pqqA** | PP_0380 | Q88QV4 | 23 aa | Precursor peptide; PqqA family (Pfam PF08042). Sequence `MWTKPAYTDLRIGFEVTMYFANR` carries the conserved **E15-x-x-x-Y19** cross-link motif | Homology + motif; operon context; strong | High confidence. Short ORF — verify it is retained in gene models. |
| **pqqD1** | PP_0377 | Q88QV7 | 91 aa | PqqD/RRE chaperone that presents PqqA to PqqE | Homology; strong structural precedent (PMIDs 28481092, 38435514) | High-confidence operon chaperone. |
| **pqqE** | PP_0376 | Q88QV8 | 376 aa | Radical-SAM PqqA peptide cyclase, EC 1.21.98.4; forms the defining C–C cross-link | Homology to well-characterized PqqE (PMID 38435514); strong | High confidence; **promote to fetch-gene** as the module-defining catalytic step. |
| **pqqB** | PP_0379 | Q88QV5 | 303 aa | Metallo-hydrolase/β-lactamase fold (InterPro IPR001279) dual hydroxylase/oxygenase | Homology (PMID 32731194); strong for step, but **UniProt annotation is outdated** | High confidence structurally, but UniProt FUNCTION still reads "may be involved in transport of PQQ… to the periplasm" (keyword *Transport*) — a **legacy annotation** superseded by the oxygenase role. Update to O2-incorporating oxidoreductase; drop *Transport*. |
| **pqqC** | PP_0378 | Q88QV6 | 251 aa | Pyrroloquinoline-quinone synthase, EC 1.3.3.11; terminal 8e⁻/8H⁺ ring closure | Homology; well-defined EC; strong | High confidence; cofactor-independent oxidase. |
| **pqqF** | PP_0381 | Q88QV3 | 766 aa | Single-chain M16 peptidase; InterPro IPR011844 (PQQ_synth_PqqF) + fused C-terminal domains; EC 3.4.24.- (by similarity) | Homology + dedicated PqqF signature; KT2440 expression tracks PQQ (PMID 27287323); moderate-strong | Broad EC 3.4.24.-; exact cleavage in KT2440 not experimentally demonstrated. **Promote to fetch-gene.** |
| **pqqD2** | PP_2681 | Q88JG8 | 90 aa | Second PqqD paralog; located far from operon, flanked by *aldB-II* (PP_2680) and *yiaY* alcohol DH (PP_2682) | Homology only; **candidate_uncertain** | UniProt FUNCTION/SIMILARITY text and InterPro set are **byte-identical to PqqD1** — an unmodified by-similarity copy, i.e. over-propagation, not PqqD2-specific evidence. Likely quinoprotein-associated/accessory. **Promote to fetch-gene** to decide. |

**Direct target-strain evidence:** An & Moe (PMID 27287323) mapped the *pqqFABCDEG* operon in KT2440, showed ≥2 independent transcripts, and found *pqqF* and *pqqB* transcript levels mirror PQQ output — the strongest species-specific data. A 2026 study (PMID 41705821, Puiggené & Nikel) addresses the "functional organization and regulatory logic" of this cluster and should be consulted directly for updated wiring (abstract not yet indexed).

---

## 5. Gaps, ambiguities, and likely over-annotations

1. **"pqqG" = PP_0375 (Q88QV9) is an S9 prolyl-oligopeptidase, not an M16B PqqG.** Historic operon nomenclature (*pqqFABCDEG*, An & Moe) attached the *pqqG* label to PP_0375, but its family (Pfam PF00326 Peptidase_S9; InterPro IPR001375) is unrelated to the *Methylobacterium* M16B PqqG. **Do not** curate KT2440 as using a two-component PqqF/PqqG protease. PP_0375's role in PQQ synthesis is unproven; treat as accessory/uncertain and, if anything, a candidate for the "alternative cellular-protease" sub-step rather than the M16B route.
2. **PqqD2 (PP_2681) over-propagation risk.** Two PqqD paralogs are annotated to the module; only PqqD1 is operon-embedded. PqqD2's genomic neighborhood argues for a quinoprotein-linked role. Mark candidate_uncertain.
3. **Broad/loose mappings.** PqqF EC 3.4.24.- is family-level (not reaction-specific); PqqE/PqqC have precise ECs. PqqB carries no EC and, more importantly, an **outdated UniProt FUNCTION** ("transport of PQQ… to the periplasm", keyword *Transport*) that predates its reclassification as a dual hydroxylase/oxygenase (metallo-β-lactamase fold, IPR001279; PMID 32731194). Its GO should be O2-incorporating oxidoreductase, and the *Transport* keyword removed. The historical "PqqB = PQQ transporter" view should not be propagated.
4. **PqqD2 = unmodified copy of PqqD1.** PqqD2 (PP_2681) inherits byte-identical by-similarity FUNCTION/SIMILARITY text and the same InterPro triad as PqqD1 — direct evidence that its UPA00539 membership is annotation transfer, not paralog-specific data.
5. **Order of proteolysis vs. oxygenation** (PqqF vs PqqB) remains biochemically unresolved even in model organisms (PMID 32731194); this is a pathway-biology gap, not a KT2440 gene gap.
6. **Species transfer.** Mechanistic detail (HDX-MS ternary complexes, PqqD NMR, two-component protease) comes from *Methylobacterium extorquens* and in-vitro systems — **strong for conserved catalytic logic**, **weak for the protease architecture** (α- vs γ-proteobacterial divergence). KT2440-specific evidence is essentially the operon mapping/expression study plus functional PQQ dependence.

---

## 6. Module and GO-curation recommendations

| Step | Recommended status |
|------|--------------------|
| PqqA precursor supply | **covered** (PP_0380) |
| PqqD-assisted PqqE cross-link | **covered** (PP_0377 + PP_0376) |
| Proteolysis — single-chain PqqF/M16 route | **covered** (PP_0381) |
| Proteolysis — two-component PqqF/PqqG M16B route | **not_expected_in_target_taxon** |
| Proteolysis — alternative cellular protease | **gap/uncertain** (only PP_0375 S9 peptidase as a weak, unproven candidate) |
| PqqB oxygenation | **covered** (PP_0379) |
| PqqC terminal ring closure | **covered** (PP_0378) |

**Module boundary edits.**
- Constrain the proteolysis step in the KT2440 module instance to the single-chain PqqF alternative; suppress the M16B two-component alternative for this taxon.
- Move PqqD2 (PP_2681) to a **candidate_uncertain / accessory** slot, not a required core step.
- Explicitly exclude PQQ-utilizing quinoprotein dehydrogenases, transport, and the PedS2/PedR2–AgmR regulators from the biosynthetic module.

**Annotation-quality fixes (in addition to boundaries).**
- **PqqB (PP_0379):** replace the legacy "PQQ transport to periplasm" FUNCTION and remove the *Transport* keyword; annotate as O2-incorporating oxidoreductase/hydroxylase (metallo-β-lactamase fold, IPR001279). Step stays **covered**.
- **PqqD2 (PP_2681):** demote from primary UPA00539 member to candidate_uncertain; its annotation is an unmodified copy of PqqD1.

**GO term needs.** Existing terms suffice: PqqE GO:0018189-type peptide-cyclase (EC 1.21.98.4); PqqC GO:0033735 (pyrroloquinoline-quinone synthase, EC 1.3.3.11); PqqB GO oxidoreductase (paired donors, O2 incorporation). No new GO request appears necessary; if PP_0375 is investigated, a dedicated peptidase term already exists. Recommend a curator note distinguishing "PqqG (S9, KT2440)" from "PqqG (M16B, *Methylobacterium*)" to prevent future over-propagation.

---

## 7. Genes to promote to full `fetch-gene` review

1. **pqqE / PP_0376** — module-defining radical-SAM step; confirm SPASM/radical-SAM Cys motifs and Fe-S cluster residues.
2. **pqqF / PP_0381** — proteolysis assignment; confirm single-chain M16 architecture, catalytic HxxEH Zn motif, and that no M16B partner is required.
3. **pqqD2 / PP_2681** — resolve whether it is a bona fide PQQ-biosynthesis chaperone or a quinoprotein-associated accessory (decides candidate_uncertain vs remove).
4. **PP_0375 (Q88QV9, "pqqG")** — clarify family (S9 peptidase) and whether it has any genuine PQQ-pathway role; prevent M16B mis-annotation.

---

## 8. Key references

- An R, Moe LA. *Regulation of PQQ-dependent glucose dehydrogenase activity in P. putida KT2440.* Appl Environ Microbiol. 2016. **PMID 27287323** — *direct KT2440 operon (pqqFABCDEG) mapping and expression.*
- Zhu W, Klinman JP. *Biogenesis of the peptide-derived redox cofactor pyrroloquinoline quinone.* 2020. **PMID 32731194** — *mechanistic review of PqqE, PqqF/G, PqqB.*
- Martins AM, et al. *A two-component protease in Methylobacterium extorquens* (M16B PqqF/PqqG). 2019. **PMID 31427437** — *establishes α-proteobacterial two-component route (weak transfer to KT2440).*
- Zhu W, Iavarone AT, Klinman JP. *HDX-MS of the multicomponent radical-SAM enzyme PqqE (PqqA/PqqD/PqqE/SAM complexes).* 2024. **PMID 38435514.**
- Evans RL, et al. *NMR structure and binding studies of PqqD (RRE).* 2017. **PMID 28481092.**
- Puiggené O, Nikel PI. *Functional organization and regulatory logic of the [pqq cluster].* 2026. **PMID 41705821** — *consult directly for updated KT2440 wiring.*
- Wehrmann M, et al. *PedS2/PedR2 two-component system, rare-earth-element switch, P. putida KT2440.* 2018. **PMID 30158283** — *regulatory, downstream.*
- Vrionis HC, et al. *AgmR regulator and alcohol utilization in P. putida.* 2002. **PMID 11954793** — *regulatory, downstream.*

*Uncertainty flags:* PqqF cleavage specificity and PP_0375/PqqD2 roles are inferred from homology/genomic context, not KT2440 biochemistry. Core catalytic assignments (PqqA/D1/E/B/C) are high-confidence homology with functional PQQ-dependence confirmed in-strain.


## Artifacts

- [OpenScientist final report](PSEPK__pqq_biosynthesis__upa00539-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__pqq_biosynthesis__upa00539-deep-research-openscientist_artifacts/final_report.pdf)