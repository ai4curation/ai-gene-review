# HSP10 re-review notes

## 2026-10-01 IBA alignment and current-GOA refresh

HSP10/YOR020C encodes the essential mitochondrial GroES/Cpn10 cochaperonin that
caps the Hsp60 chamber in the matrix. The existing review correctly centers
Hsp10's Hsp60-binding cochaperonin function, mitochondrial-matrix localization,
and role in folding/refolding imported mitochondrial proteins.

Forced a fresh GOA/UniProt fetch. The live feed now has 19 source rows. The
older IBA and IDA `GO:0051082` unfolded-protein-binding rows have disappeared
after GO:0051082 obsoletion; the review therefore drops both stale rows. The
current PAINT table for PTHR10772 still carries the `GO:0046872` metal ion
binding IBA at PTN000080668, seeded only by *Mycobacterium tuberculosis*
GroES/Cpn10, so the existing REMOVE decision remains appropriate for yeast Hsp10.

Checked `interpro/panther/PTHR10772/PTHR10772-paint.tsv` and added explicit
PAINT-node `propagation_review` blocks for all four accepted live IBAs:
`GO:0006457` protein folding and `GO:0051087` protein-folding chaperone binding
at PTN000080668, `GO:0005739` mitochondrion at PTN000080670, and `GO:0005759`
mitochondrial matrix at PTN000080672.

Literature freshness checks found recent human/in situ mitochondrial
Hsp60-Hsp10 structural studies, including 2024-2025 cryo-EM/cryo-ET analyses of
the mitochondrial Hsp60-Hsp10 chamber. Those reinforce the conserved Hsp10
cochaperonin model but do not supersede the yeast-specific HSP10 annotations or
change the curation calls here.
