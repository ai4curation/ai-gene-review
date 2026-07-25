---
title: "Taxon-absent-component detector (genome-content satisfiability for IBA QC)"
---

# Taxon-absent-component detector

A small, runnable prototype that turns one recurring IBA over-annotation pattern
into an automatable screen. It is the **signaling-domain, genome-content**
special case of the [Pathway satisfiability](../../PATHWAY_SATISFIABILITY.md)
engine (which resolves *metabolic* modules against an expression oracle).

[parent project ← Pathway satisfiability](../../PATHWAY_SATISFIABILITY.md) ·
[origin ← IBA Annotation Quality](../../IBA_REVIEW.md)

## The pattern

Some process/pathway GO terms **entail an obligate component**. `GO:0007259`
"signaling via **JAK**-STAT" entails a Janus kinase. Read as a boolean formula
over required components under a *genome-content oracle*, the annotation is
**unsatisfiable** in a genome that encodes no such component — so an IBA that
transferred it (from metazoan seeds, say) is a candidate
`LINEAGE_OR_TAXON_MISMATCH` over-propagation.

This came out of the *Dictyostelium* development review: Dd-STATa/c were
annotated JAK-STAT, but *Dictyostelium* has **no JAK** (the STATs are activated
by the TKL kinases Pyk2/Pyk3), so the term was rescoped to the JAK-independent
parent `GO:0097696`.

## Two oracles — and why PANTHER is primary

The naïve version of this check asks whether the target genome has an **InterPro
domain signature** for the component. That has a serious failure mode:
**signature-absence ≠ genome-absence for divergent lineages** — a real ortholog
that has diverged past its metazoan domain signature scores zero.

The fix is the **PANTHER family (`PTHR…`) membership** oracle. IBA is itself
propagated *along the PANTHER tree*, so the very orthologs an IBA touches are, by
construction, placed in the PANTHER family — even when their domains have
diverged. `detect.py` therefore queries **both** and lets PANTHER decide:

| Status | Rule |
|--------|------|
| `COMPONENT_PRESENT` | PANTHER family has a target member → satisfiable; not flagged |
| `ABSENT` | PANTHER target 0, control >0 → candidate unsatisfiable (confidence **HIGH** when InterPro agrees, **MEDIUM** otherwise) |
| `INCONCLUSIVE` | PANTHER control 0 (bad family id) or an API error |
| *divergence flag* | present by PANTHER **but** InterPro domain screen scores 0 — a domain-only screen would have wrongly called it absent |

Counts are fetched **live** from UniProt REST and never hard-coded; a failed
fetch yields `INCONCLUSIVE`, not a made-up number.

## Live results (this is the whole point)

Current [RESULTS.md](RESULTS.md), *D. discoideum* (44689) vs human (9606):

| Case | Component | PANTHER ctrl/tgt | InterPro ctrl/tgt | Verdict |
|------|-----------|:----------------:|:-----------------:|---------|
| **jak_stat** | JAK | 56 / **0** | 56 / 0 | **ABSENT (HIGH)** — true positive; both oracles agree |
| stat_control | STAT | 128 / **4** | 100 / 0 | **PRESENT** + ⚠divergence flag |
| **gpcr_purinergic** | P2Y (GPCR) | 21 / **0** | 3 / 0 | **ABSENT (HIGH)** — P2Y GPCR truly absent |
| p2x_control | P2X | 47 / **5** | 26 / 0 | **PRESENT** + ⚠divergence flag |

The two divergence controls are the payoff: an **InterPro-only** screen calls
STAT and P2X *absent* in *Dictyostelium* (both score 0) — but they are present
(the 4 Dd-STATs; ~5 divergent P2X receptors, matching Fountain et al. 2007,
*Nature* 448:200). **PANTHER recovers both**, so the dual-oracle detector does
not flag them, while still correctly flagging the genuine JAK and P2Y-GPCR
absences. The `PTHR` node is the divergence-robust handle the domain screen
lacked.

## Run it

```bash
cd projects/PATHWAY_SATISFIABILITY/taxon_absent_component
uv run python detect.py --write RESULTS.md          # DICDI vs human
uv run python detect.py --target 44689 --control 9606
```

## Still a triage screen, not an oracle

PANTHER sharply cuts the false-positive rate but does not eliminate uncertainty:
a genome could carry a member PANTHER has not classified, and family membership
alone does not prove the specific sub-activity is retained. So an `ABSENT`
verdict — even at HIGH confidence — is a **strong lead for review**, not an
automatic `REMOVE`. The deciding evidence stays in `corroboration` (for JAK: the
documented JAK-independence of *Dictyostelium* STAT activation).

## Possible extensions

- Profile-HMM / structure search for the residual cases PANTHER also misses.
- Drive the target taxon and candidate terms straight from a review's
  `LINEAGE_OR_TAXON_MISMATCH` `propagation_review` rows (whose `WITH/FROM`
  already carries the `PANTHER:PTN…` node), closing the loop with the
  [IBA project](../../IBA_REVIEW.md).
- Query the exact IBA source **`PTN` node** (not just the family) so the check
  is against the precise ancestral node the annotation was propagated from.
