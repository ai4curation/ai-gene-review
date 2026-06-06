# Proteostasis Review Batch 3 — Gene Selection

Date: 2026-06-06
Branch: `claude/proteostasis-gene-review-w59I5`

## Context

The two prior batches are complete:
- `proteostasis-pr-1217` (50 human genes, merged 2026-06-02)
- `proteostasis-batch-2026-06-03` (50 human genes, alphabetical sweep AAAS..ATP6V0D1 from the PN projected candidate-additions report)

All five `priority_genes.tsv` no-local-dir targets (BTF3, HSPA12A, HSPA12B,
AARSD1, BAG6) now also have local reviews.

This batch selects **20 more genes** from the PN projected candidate-additions
report (`reports/pn_projection/pn_projected_candidate_additions.tsv`), all of
which are (a) PN-projected candidates with `ok_for_propagation_to_go` scope and
(b) had no local `*-ai-review.yaml` before this batch.

Rather than continuing the pure alphabetical sweep (which next hits a long run
of family/domain-based BTB-domain inclusions of lower individual value), this
batch is chosen to be **biologically coherent and high-value across the three
main proteostasis branches**.

## Selected genes (20)

### ALP — lysosomal acidification (V-ATPase, completing the V0 set from batch 2)
1. `ATP6V1A`  — V-ATPase V1 catalytic A subunit
2. `ATP6V1B2` — V-ATPase V1 B2 subunit
3. `ATP6V1C1` — V-ATPase V1 C1 subunit
4. `ATP6V1D`  — V-ATPase V1 D subunit
5. `ATP6V1E1` — V-ATPase V1 E1 subunit
6. `ATP6V1F`  — V-ATPase V1 F subunit
7. `ATP6V1G1` — V-ATPase V1 G1 subunit
8. `ATP6V1H`  — V-ATPase V1 H subunit
9. `ATP6V0E1` — V-ATPase V0 e1 subunit

### ALP — selective autophagy / mitophagy receptors
10. `BNIP3L` (NIX) — mitophagy receptor
11. `BCL2L13` — mammalian Atg32-like mitophagy receptor
12. `CALCOCO1` — ER-phagy / Golgiphagy receptor (CoCoA)

### ER proteostasis — folding & quality control
13. `CANX` — calnexin, ER lectin chaperone (calnexin/calreticulin cycle)
14. `CALR` — calreticulin, ER lectin chaperone
15. `CCDC47` — ER multipass membrane protein biogenesis / calnexin-associated
16. `CAMLG` — GET/TRC pathway (tail-anchored membrane protein insertion)
17. `AUP1` — ERAD / lipid-droplet ubiquitination adaptor

### Cytosolic co-chaperone & UPS regulation
18. `BAG2` — BAG-domain HSP70 co-chaperone (nucleotide exchange factor)
19. `CACYBP` (SIP) — Siah-1 interacting protein, ubiquitination adaptor
20. `CAND1` — cullin-associated/dissociation factor; CRL E3 ligase regulator

## Method

For each gene:
- `uv run ai-gene-review fetch-gene human <GENE> --output-dir .` (UniProt, GOA,
  cached publications, seeded `-ai-review.yaml`).
- Research from cached publications + UniProt + literature; notes recorded in
  `<GENE>-notes.md` with provenance.
- Each seeded GOA annotation reviewed per GO guidelines (ACCEPT /
  KEEP_AS_NON_CORE / MODIFY / MARK_AS_OVER_ANNOTATED / REMOVE / etc.) with
  `supported_by` evidence.
- `description`, `core_functions`, `suggested_questions`, `suggested_experiments`
  populated.
- Validated with `uv run ai-gene-review validate ...` / `just validate`.

## Completion summary (2026-06-06)

All 20 reviews completed and validated (schema + term + reference validators all
pass). Selected curation highlights:

- **V-ATPase subunits** (ATP6V1A/B2/C1/D/E1/F/G1/H, ATP6V0E1): core role is
  ATP-hydrolysis-driven proton transport in the V1/V0 rotary mechanism; the
  recurring over-annotations were bare `protein binding`, generic `membrane`,
  `extracellular exosome` (lysosomal-proteomics contamination), and indirect
  `regulation of macroautophagy`. Genuine secondary roles retained as non-core
  include ATP6V1H's clathrin/AP-2 adaptor role and ATP6V1D/E1 mTORC1 and
  apical-membrane functions. ATP6V1E1 had one IPI `protein binding` REMOVED
  (tristetraprolin/CCL3 mRNA paper — probable curation error).
- **ER folding/QC** (CANX, CALR, CCDC47, CAMLG, AUP1): calnexin/calreticulin
  cycle (lectin chaperone + ER Ca2+) accepted as core; CALR surface/"eat-me"
  and MHC-I peptide-loading roles kept as non-core. CCDC47 PAT-complex and
  CAMLG GET-complex membrane-protein-biogenesis roles accepted; both required
  moving complex terms into `core_functions.in_complex`.
- **Autophagy/mitophagy receptors** (BNIP3L, BCL2L13, CALCOCO1): the defining
  selective-autophagy receptor MF/BP terms are largely absent from GOA. Added
  as `proposed_new_terms` (mitophagy receptor activity for BNIP3L/BCL2L13;
  reticulophagy/Golgiphagy receptor activity for CALCOCO1). CALCOCO1's older
  transcriptional-coactivator (CoCoA) annotations kept as non-core. BNIP3L
  `defense response to virus` marked UNDECIDED (cited paper is about apoptosis;
  the real NIX-MAVS link is viral immune *evasion*, not host defense).
- **Co-chaperone / UPS regulation** (BAG2, CACYBP, CAND1): BAG2 HSP70 NEF +
  CHIP-inhibition accepted; CAND1 captured as a CRL exchange/assembly regulator
  (not a catalytic enzyme); CACYBP as a Siah1-SKP1 E3 adaptor bridging S100/
  calcium signaling to ubiquitination.

Tracking row added to `review_batches.tsv` as `proteostasis-batch-2026-06-06`.
