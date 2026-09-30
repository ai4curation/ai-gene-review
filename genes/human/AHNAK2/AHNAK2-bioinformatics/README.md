# AHNAK2 bioinformatics

Reproducible checks behind the human AHNAK2 GO review. Everything is fetched
live from UniProt, QuickGO, InterPro/ARBA and IntAct; `cache/` is disposable.

```bash
uv run python resolve_withfrom.py        # who are the IBA donors, and what do THEY hold?
uv run python check_multihit.py          # every candidate behind each multi-hit MOD id
uv run python subcell_provenance.py      # what evidence backs each SUBCELLULAR LOCATION?
uv run python paralogue_architecture.py  # is the AHNAK2/AHNAK paralogy functionally informative?
uv run python gap_homodimer.py           # did PDB 4CN0 produce any GO annotation anywhere?
uv run python gap_by_reference.py        # per-paper GO coverage for AHNAK2
uv run python node_reach.py              # which node's reach is exactly my gene set?
uv run python arba_rules.py              # which ARBA condition set fires on AHNAK2?
uv run python intact_partners.py         # is AHNAK2's interactome one screen or many?
uv run python retraction_check.py        # retraction/erratum/correction on every cited PMID
uv run python check_terms.py             # definitions + ancestry of every term argued about
uv run python reconcile_goa.py           # gate: every GOA row reviewed exactly once
uv run python audit_claims.py            # gate: the review's claims still match the data
uv run python audit_claims.py --self-test  # prove the guards fire
```

`paralogue_architecture.md` is written by `paralogue_architecture.py`. Do not
hand-edit it — a fresh run overwrites it.

`RESULTS.md` is prose written by the reviewer; every number in it names the
script that produces it, and `audit_claims.py` re-derives the load-bearing ones
from the committed TSVs and fails if they drift.
