---
title: "Matrisome → GO mapping & ECM annotation gaps"
---

# Matrisome → GO mapping & ECM annotation gaps

Supporting material relating the [Matrisome project](https://sites.google.com/uic.edu/matrisome)
(Naba/Hynes; [MatrisomeDB](https://matrisomedb.org)) to GO annotation review. The matrisome is a
**curated membership list** — a lookup table, not a classifier — that assigns each ECM /
ECM-associated gene to one of six families under two categories:

| category | families |
|---|---|
| **Core matrisome** | Collagens, ECM Glycoproteins, Proteoglycans |
| **Matrisome-associated** | ECM-affiliated Proteins, ECM Regulators, Secreted Factors |

**MatrisomeDB does not deposit GO annotations.** ECM `GO:0031012` annotations in GOA are made
independently by GO curators (e.g. GO_Central, BHF-UCL) citing the underlying proteomics papers
(HDA). This project treats the matrisome as one of our membership-based propagation sources (like
InterPro2GO / PANTHER-IBA), used to *find candidate annotations*, never to auto-assert.

## The mapping (family → GO)

- `matrisome2go.sssom.yaml` — **canonical** SSSOM mapping set (source of truth). Only the three
  **core** families map to the ECM cellular-component term `GO:0031012` (`located in`). The three
  **associated** families are deliberately recorded as `sssom:NoTermFound` gap rows: their members
  (proteases, cross-linkers, secreted cytokines/growth factors) are not reliably ECM-localized, so
  propagating `GO:0031012` would manufacture over-annotations.
- `matrisome2go.terms.yaml` — **generated** nested term-tuple form (do not edit) for GO label
  validation.
- `sssom_to_terms.py` — regenerates `.terms.yaml` from `.sssom.yaml`.

> **Note on `GO:0062023`.** "Collagen-containing extracellular matrix" was **obsoleted** and merged
> back into `GO:0031012` (`replaced_by GO:0031012`; go-ontology#29475, *"not clearly defined and
> usage has been inconsistent"*). The earlier GO push to reannotate metazoan ECM annotations to
> `GO:0062023` has therefore been reversed; `GO:0031012` is the current term for all core families.

```bash
just validate-matrisome-mappings   # SSSOM structure + GO term/label validation
```

## Path 2 — candidate missing ECM annotations (higher priority)

`missing_annotation_report.py` scans every reviewed gene (`genes/<species>/<gene>/<gene>-goa.tsv`),
looks it up in the masterlist (species-aware, by UniProt accession or symbol), and — for **core**
matrisome genes — flags those whose GOA lacks `GO:0031012`. Subsumption-aware filtering suppresses a
gene that already carries a more specific (is_a descendant) ECM term. Output:

- `MISSING_ANNOTATIONS.md` — human-readable summary + candidate table.
- `data/candidate_missing_annotations.tsv` — one row per (gene, candidate GO term).

```bash
just matrisome-missing
```

These are **leads for a curator, not assertions** — e.g. GAS6/IGFBP3 are matrisome ECM glycoproteins
that a curator should evaluate before any GO:0031012 annotation.

## Path 1 — quotable MatrisomeDB evidence for existing annotations (lower priority, not yet built)

Intended to let a review cite a MatrisomeDB export line as `supporting_text` evidence for an existing
ECM annotation (mirroring how publication quotes are verbatim-checked). Requires a MatrisomeDB
per-protein export format; deferred.

## Data

`data/matrisome_*.csv` — the matrisome masterlists (gene/category/family), one file per species
(human, mouse, zebrafish, drosophila, c.elegans).

Source: [`Matrisome/MatrisomeAnalyzeR`](https://github.com/Matrisome/MatrisomeAnalyzeR) @ `d8aec6d`
(`data/matrisome.list.rda`), licensed GPL (≥3). Each gene appears as multiple rows — one per
identifier namespace (symbol, alias, UniProt, RefSeq, Ensembl, NCBI GeneID) — so any identifier
resolves to its family. The canonical human matrisome is ~1,027 genes (the NCBI-GeneID row count).
