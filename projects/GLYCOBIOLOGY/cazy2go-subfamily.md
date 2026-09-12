# Subfamily resolution of the poly-specific cazy2go families

The poly-specific CAZy families (one family → many GO MF terms) cannot be propagated safely at the
family level. This resolves them to **subfamily granularity** so each specific activity is attributed
to the right sub-group.

## Method (InterPro co-occurrence — dbCAN-sub was inaccessible)

The canonical route is dbCAN-sub's subfamily→EC table, but its server does not serve the data files
from this environment (every candidate URL returns an error page). So subfamilies are resolved from
data we already have: each reviewed UniProt member of a CAZy family carries **both** its EC(s) **and**
its InterPro signature(s). Within a poly-specific family `F`, for each specific GO MF term `G`
reachable from members' ECs, [`subfamily_resolve.py`](subfamily_resolve.py) finds InterPro
signatures `S` that co-occur with `G` at high precision:

```
precision(S→G | F) = |members of F with S and G| / |members of F with S|   (≥ 0.8)
support            = |members of F with S|                                  (≥ 2)
sig_family_spread  = # distinct CAZy families S appears in   (≤ 2 ⇒ "family-specific")
```

A **family-specific** (`spread ≤ 2`), high-precision `S` is a sub-family marker for `G` — a safe,
signature-level attribution of the activity the unsafe family-level term lumped. Each `S→G` is checked
against `interpro2go`. Full table: [`cazy2go.subfamily.tsv`](cazy2go.subfamily.tsv).

## Results

90 poly-specific (non-CBM) families; **66 resolved** to ≥1 signature→GO; **490 signature→GO rows**:

| status vs interpro2go | rows | meaning |
|-----------------------|-----:|---------|
| **CONFIRMS** | **71** | `interpro2go` already maps `S`→`G` (or a descendant) — **validates the method** |
| PROPOSED_new | 250 | `interpro2go` silent on `S` → candidate addition |
| PROPOSED_specific | 61 | `interpro2go` gives only an ancestor of `G` → specificity refinement |
| PROPOSED_other | 108 | `interpro2go` gives an unrelated term → flag/inspect |

Filtering proposals to **family-specific signatures** (spread ≤ 2, dropping broad superfamily entries
like the GH10 TIM-barrel `IPR017853` that are precise within a family but too broad to propagate)
leaves **210 trustworthy proposals across 56 families** — signature-level, safe-to-propagate
`interpro2go` candidates. Examples (all precision ≈1.0, spread=1):

- **GH28 `IPR050434` → polygalacturonase activity** (32 members)
- **GT4 `IPR056736/IPR056735` → sucrose synthase activity** (24)
- **GH2 `IPR050347` → β-galactosidase**, **GH3 `IPR050288` → β-glucosidase**
- **GH47 `IPR050749` → mannosyl-oligosaccharide 1,2-α-mannosidase** (20)
- **GH20 `IPR029019` → β-N-acetylhexosaminidase**, **GH38 `IPR041147` → α-mannosidase**
- **GH13 `IPR044143` → 1,4-α-glucan branching enzyme** (a GH13 subfamily, the canonical poly-specific
  amylase family resolved to its branching-enzyme sub-group)

## Interpretation

- The **71 CONFIRMS** are the headline validation: an entirely independent signal (InterPro
  co-occurrence within reviewed members) re-derives mappings curators already put in `interpro2go`.
- The resolution **fixes the poly-specific safety problem**: where family→GO was unsafe (GH13 → 27
  terms), signature→GO attributes each activity to its sub-group (e.g. branching enzyme vs
  cyclomaltodextrin glucanotransferase via distinct `IPR`s).
- The 210 family-specific proposals are the actionable, subfamily-resolved `interpro2go` addition
  candidates.

## Caveats

- This is **InterPro-signature subfamily resolution**, a proxy for the CAZy/dbCAN-sub subfamily
  namespace (which was not fetchable here).
- Precision/support are computed over **reviewed** members only — small N for niche families.
- `spread ≤ 2` is a heuristic; a few legitimate subfamily signatures span 2–3 related families.
- CONFIRMS validate; **PROPOSED rows are candidates requiring a human GO/InterPro2GO curator** to
  confirm the signature universally implies the activity before any submission.
