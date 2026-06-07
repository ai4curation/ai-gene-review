# Proteostasis Review Batch 4 — Gene Selection

Date: 2026-06-07
Branch: `claude/proteostasis-network-genes-BVKRp`

## Context

The three prior batches are complete:
- `proteostasis-pr-1217` (50 human genes, merged 2026-06-02)
- `proteostasis-batch-2026-06-03` (50 human genes, alphabetical sweep AAAS..ATP6V0D1)
- `proteostasis-batch-2026-06-06` (20 human genes; V-ATPase core, ER folding/QC,
  autophagy/mitophagy receptors, co-chaperone/UPS regulation)

This batch selects **30 more genes** from the PN projected candidate-additions
report (`reports/pn_projection/pn_projected_candidate_additions.tsv`), all of
which are PN-projected candidates with `ok_for_propagation_to_go` scope and had
no local `*-ai-review.yaml` before this batch.

Rather than continuing the pure alphabetical sweep (which next hits a long run of
family/domain-based BTB-domain inclusions of lower individual value), this batch
is chosen to be biologically coherent and high-value across the proteostasis
branches.

## Selected genes (30)

### ALP — lysosomal acidification (complete tissue-specific V-ATPase isoforms + Cl/H antiporter)
1. `ATP6V0E2` — V-ATPase V0 e2 subunit
2. `ATP6V1B1` — V-ATPase V1 B1 subunit (kidney/inner-ear isoform)
3. `ATP6V1C2` — V-ATPase V1 C2 subunit (lung/kidney isoform)
4. `ATP6V1E2` — V-ATPase V1 E2 subunit (testis isoform)
5. `ATP6V1G2` — V-ATPase V1 G2 subunit (neuronal isoform)
6. `ATP6V1G3` — V-ATPase V1 G3 subunit (kidney isoform)
7. `CLCN7` — lysosomal Cl-/H+ antiporter (ClC-7), partners V-ATPase in acidification

### Mitochondrial proteostasis
8. `CLPX` — mitochondrial ClpXP AAA+ unfoldase/protease subunit

### Cytosolic chaperone / co-chaperone
9. `CDC37L1` — Cdc37-like HSP90 co-chaperone (Cdc37 paralog)

### ER proteostasis — folding, lectin chaperones, PPIases, collagen biogenesis
10. `CLGN` — calmegin, testis-specific calnexin paralog (ER lectin chaperone)
11. `CALR3` — calreticulin-3, testis ER chaperone (calreticulin paralog)
12. `CNPY3` — canopy-3, ER co-chaperone for Toll-like receptor folding
13. `CRTAP` — cartilage-associated protein, prolyl 3-hydroxylase complex chaperone
14. `CYB5R4` — NADH-cytochrome b5 reductase 4 (cyb5/heme; ER redox)
15. `COLGALT1` — collagen beta(1-O)galactosyltransferase 1 (ER, collagen glycosylation)
16. `COLGALT2` — collagen beta(1-O)galactosyltransferase 2
17. `CWC27` — spliceosome-associated cyclophilin/PPIase (proline isomerase)

### Cytonuclear / nuclear proteostasis — histone chaperones
18. `CHAF1A` — CAF-1 large subunit (histone H3-H4 chaperone)
19. `CHAF1B` — CAF-1 p60 subunit (histone H3-H4 chaperone)

### Ubiquitin-proteasome system — CRL substrate receptors, adaptors, E3s
20. `CRBN` — cereblon, CRL4 substrate receptor (thalidomide/IMiD target)
21. `COP1` (RFWD2) — RING E3 ubiquitin ligase
22. `DCAF10` — DDB1/CUL4-associated factor 10 (CRL4 substrate receptor)
23. `DCAF11` — DDB1/CUL4-associated factor 11 (CRL4 substrate receptor)
24. `CACUL1` — CDK2-associated cullin domain 1 (cullin regulator)
25. `CDK5RAP3` — CDK5RAP3 / C53, UFMylation pathway, ribosome/ER quality control
26. `CGRRF1` — cell growth regulator with RING finger 1 (ER membrane E3, ERAD)
27. `CNOT4` — CCR4-NOT complex RING E3 ligase (translation/RQC-linked)
28. `CHIC2` — cysteine-rich hydrophobic domain 2 (vesicle/UPS-adjacent)
29. `CSNK2B` — casein kinase 2 beta regulatory subunit (PN regulation)
30. `CSNK1D` — casein kinase 1 delta (PN regulation)

## Method

For each gene:
- `uv run ai-gene-review fetch-gene human <GENE>` (UniProt, GOA, cached
  publications, seeded `-ai-review.yaml`).
- Research from cached publications + UniProt + literature; notes recorded in
  `<GENE>-notes.md` with provenance.
- Each seeded GOA annotation reviewed per GO guidelines (ACCEPT /
  KEEP_AS_NON_CORE / MODIFY / MARK_AS_OVER_ANNOTATED / REMOVE / UNDECIDED) with
  `supported_by` evidence.
- `description`, `core_functions`, `suggested_questions`, `suggested_experiments`
  populated.
- Validated with `uv run ai-gene-review validate ...`.
