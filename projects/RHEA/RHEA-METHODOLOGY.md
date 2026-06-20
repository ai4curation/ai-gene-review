---
title: "RHEA -> GO Methodology Notes"
---

# RHEA → GO Methodology Notes

**Parent project:** [RHEA.md](../RHEA.md)

## Two directions, one mapping

Everything in this project hangs off a single public file, the GOA/UniProt
**rhea2go** external mapping:

```bash
# distinct RHEA reactions -> GO molecular-function terms
curl -sL https://current.geneontology.org/ontology/external2go/rhea2go -o rhea2go.txt
# header records the GO release the mapping was generated from
```

Each line maps one RHEA reaction to one GO molecular-function term, e.g.:

```
RHEA:10596 > GO:protein tyrosine kinase activity ; GO:0004713
```

We use this mapping in **both directions**:

| Direction | Question | Source of truth | Analog |
|-----------|----------|-----------------|--------|
| **Forward (contribution)** | Which GO MF annotations exist *because* RHEA mapped them, and are they uniquely informative? | GOA rows with `GO_REF:0000116` / `assigned_by=RHEA` | SPKW (`GO_REF:0000043`), UniPathway (`GO_REF:0000041`) |
| **Reverse (gap)** | Which UniProtKB RHEA annotations *should* have produced a GO MF term but did not? | UniProtKB catalytic-activity (RHEA) xrefs vs. GOA | (new — the "falls through the cracks" question) |

`GO_REF:0000116` is the RHEA pipeline reference: in GOA these rows are
`assigned_by=RHEA`, aspect `molecular_function`, evidence `IEA`. It is the
direct RHEA counterpart of the SPKW keyword pipeline (`GO_REF:0000043`) and the
EC2GO pipeline (`GO_REF:0000003`).

## Direction 1 — Forward contribution (SPKW-style closure-filtered uniqueness)

This reuses the exact closure-filtered uniqueness logic from
[SPKW](../SPKW/SPKW-METHODOLOGY.md) and [UniPathway](../UNIPATHWAY.md), swapping
the reference id. A RHEA-derived MF row is **TRUE unique** only when no
non-RHEA source already supports the same gene→term pair, and no non-RHEA
source supports a more specific descendant term for the same gene.

```sql
-- Requires the go-db DuckDB databases under ~/repos/go-db/db/ (not bundled in
-- the web container). Mirrors UNIPATHWAY.md's closure query.
WITH rhea AS (
    SELECT internal_id, db_object_id, db_object_symbol, ontology_class_ref, aspect
    FROM gaf_association
    WHERE supporting_references = 'GO_REF:0000116'
      AND is_negation = false
),
true_unique AS (
    SELECT r.*
    FROM rhea r
    WHERE NOT EXISTS (
        SELECT 1 FROM gaf_association o
        WHERE o.db_object_id = r.db_object_id
          AND o.ontology_class_ref = r.ontology_class_ref
          AND o.supporting_references != 'GO_REF:0000116'
          AND o.is_negation = false
    )
    AND NOT EXISTS (
        SELECT 1
        FROM isa_partof_closure ipc
        JOIN gaf_association o
          ON o.db_object_id = r.db_object_id
         AND o.ontology_class_ref = ipc.subject
         AND o.supporting_references != 'GO_REF:0000116'
         AND o.is_negation = false
        WHERE ipc.object = r.ontology_class_ref
    )
)
SELECT count(*) AS annotations,
       count(DISTINCT db_object_id) AS genes,
       count(DISTINCT ontology_class_ref) AS terms
FROM true_unique;
```

Because RHEA is a **molecular-function** source, the expected pattern differs
from SPKW/UniPathway (which are dominated by broad eukaryotic *process*
conflation): RHEA-unique rows should be *enzyme activity* terms, and the
relevant failure modes are (a) **wrong-paralog / wrong-substrate** specificity,
and (b) the same **parent-vs-child altitude** problem RHEA already creates in
the reverse direction (see below).

## Direction 2 — Reverse gap ("falls through the cracks")

A UniProtKB entry can carry a catalytic activity with a RHEA cross-reference
(`CC -!- CATALYTIC ACTIVITY ... Xref=Rhea:RHEA-nnnnn`) and yet **not** carry the
GO molecular-function term that `rhea2go` maps that reaction to. The reverse
probe quantifies this directly from the UniProt REST API — no go-db required:

```bash
# entries carrying RHEA:10596, with their GO ids
curl -sL 'https://rest.uniprot.org/uniprotkb/search?query=rhea:10596+AND+reviewed:true&fields=accession,go_id&format=tsv&size=500'
```

`rhea_go_gap_probe.py` automates this: for each reaction it pulls the UniProt
entries carrying the RHEA and counts how many lack the mapped GO term.

```bash
uv run python rhea_go_gap_probe.py --stats        # characterise rhea2go
uv run python rhea_go_gap_probe.py --gap-sample   # pilot reactions
uv run python rhea_go_gap_probe.py --gap RHEA:21248
```

### Why a row falls through the cracks

1. **No GO term exists for the reaction.** ~some RHEA reactions have no
   `rhea2go` line at all (e.g. `RHEA:46608` in the pilot). The activity simply
   cannot propagate — a candidate for a *new* GO MF term (`proposed_new_terms`).
2. **Direction / master-id mismatch.** RHEA ids come in quartets (an undirected
   master plus three directional children). `rhea2go` keys on one id; if a
   UniProt entry's annotation or the GOA pipeline keys on a sibling id, the join
   can miss.
3. **Reviewed-vs-unreviewed / pipeline timing.** TrEMBL entries and recently
   added catalytic-activity annotations may not yet have propagated to the GAF
   snapshot.
4. **Altitude mismatch (the big confounder — NOT a real gap).** `rhea2go` may
   map a reaction to a *generic* parent term (e.g. `GO:0004713 protein tyrosine
   kinase activity`) while the curated entry carries a *more specific child*
   (e.g. a receptor tyrosine kinase term). Exact-match counts this as "missing"
   even though closure says it is covered.

### The closure caveat is mandatory

The pilot probe in [RHEA.md](../RHEA.md) is **exact-term match**, so its
`pct_missing` is an **upper bound** on the real gap. A reaction showing a high
exact-match gap is a *candidate*, not a confirmed gap. The honest next step is
the same closure filter used in direction 1: subtract entries that carry **any
descendant** of the mapped GO term before calling the annotation a true gap.
This needs the `isa_partof_closure` table (go-db), which is why the full audit
is staged for an environment that has the DuckDBs.

This is the identical lesson the SPKW and UniPathway projects learned: **naive
counts overstate the signal; closure filtering is the default, not an
optional refinement.**

## Limitations in the web container

- The `~/repos/go-db/db/*.ddb` DuckDBs (used for the forward closure-filtered
  cross-organism counts) are **not present** in the Claude-on-the-web container,
  so the UNIPATHWAY-style cross-organism contribution table is staged, not yet
  populated. The `GO_REF:0000116` identification and the `rhea2go`
  characterisation are computed live; the reverse gap probe runs live against
  the UniProt API.
- The reverse probe is capped at the UniProt page `size` (default 500). Rows
  flagged `capped_at_size` undercount the denominator; raise `--size` or page
  for an exact denominator.
