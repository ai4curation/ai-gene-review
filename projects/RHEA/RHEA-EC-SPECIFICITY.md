---
title: "RHEA vs EC: Masking, Specificity, and Mapping Gaps"
---

# RHEA vs EC: Masking, Specificity, and Mapping Gaps

**Parent project:** [RHEA.md](../RHEA.md) · **Methodology:** [RHEA-METHODOLOGY.md](RHEA-METHODOLOGY.md)

This page answers three questions that the first scoping pass deferred: how much
of RHEA's GO contribution is **masked by EC**, what happens to reaction
**specificity** on the way to GO, and what concrete **mapping gaps** exist. All
numbers are computed live by [`rhea_ec_specificity.py`](rhea_ec_specificity.py)
from three public sources — `rhea2go` and `ec2go` (GOA external2go) and RHEA→EC
(RHEA REST API) — at GO release `2026-05-19`. Nothing here is hardcoded.

The single most important caveat from the methodology carries over: GO-term
*identity* and GO-term *set membership* are exact-match. Where it matters
(specificity, true gaps) a closure-aware follow-up is still required; the
exact-match figures are bounds, and I say so each time.

## 1. RHEA is mostly masked by EC

UniProt enzymes almost always carry **both** an EC number and a RHEA reaction.
EC reaches GO via `ec2go` (`GO_REF:0000003`); RHEA reaches GO via `rhea2go`
(`GO_REF:0000116`). So before crediting RHEA with a contribution, we must ask
whether EC2GO already delivered the same term.

**At the GO-term level:**

| Quantity | Count | Note |
|---|---:|---|
| GO MF terms reachable via `rhea2go` | 4,744 | RHEA's whole target vocabulary |
| GO MF terms reachable via `ec2go` | 4,657 | EC's whole target vocabulary |
| **Shared** (RHEA term also an EC term) | **3,972** | **84% of RHEA's terms are maskable by EC** |
| **RHEA-only** (EC cannot deliver) | **772** | RHEA's genuinely unique term vocabulary |
| EC-only | 685 | EC's unique vocabulary; RHEA leaves these to EC |

**At the reaction level** (the 4,904 RHEA reactions that carry both a `rhea2go`
term and an EC number):

| Outcome | Count | Interpretation |
|---|---:|---|
| EC has an `ec2go` term, and **RHEA's term == an EC term** | **4,324 (88%)** | **Fully masked** — EC2GO already supplies exactly this GO term |
| EC has an `ec2go` term, but RHEA's term **differs** | 118 (2%) | RHEA adds a distinct (often cofactor-resolved) term |
| EC has **no** `ec2go` term | 462 (9%) | RHEA is the **only** EC-adjacent route to GO here |

**Takeaway.** For ~88% of enzymatic reactions, the `GO_REF:0000116` annotation
RHEA contributes is the *same term* EC2GO already contributes — RHEA is
redundant at the GO layer and its row would be dropped by the closure-filtered
uniqueness query (it is masked by an EC sibling). RHEA's real, *unmasked* value
is concentrated in four pockets:

1. the **772 RHEA-only GO terms** EC2GO cannot produce,
2. the **462 reactions whose EC has no `ec2go` line** (RHEA fills an EC2GO gap),
3. the **118 differing-term reactions** where RHEA resolves a distinction EC's
   own GO term blurs, and
4. the **reverse-propagation gap** (UniProt RHEA annotations that reach *neither*
   EC2GO nor RHEA2GO in GOA — see [RHEA.md](../RHEA.md) pilot).

This is the concrete form of "RHEA contributions may be masked by EC": at the
term level most are, so a RHEA audit should be driven by the four unmasked
pockets, not by raw `GO_REF:0000116` volume.

## 2. Specificity cuts both ways

RHEA is finer-grained than EC: one EC number routinely spans many RHEA reactions
(different substrates, cofactors, or directions). The question is whether that
fineness *survives* the mapping to GO.

### 2a. EC → RHEA → GO: specificity is usually flattened, sometimes kept

Of the 4,235 ECs that map to ≥1 `rhea2go` reaction, **435 map to more than one**:

| Of those 435 multi-reaction ECs… | Count | Meaning |
|---|---:|---|
| all reactions **collapse to one** GO term | **323 (74%)** | GO cannot tell the reactions apart — specificity **lost** |
| reactions **spread across multiple** GO terms | **112 (26%)** | GO keeps a split the **bare EC number lumps** — RHEA+GO **adds** specificity over EC |

The 112 "spread" cases are where RHEA is most valuable: a single EC hides a
distinction that RHEA, and the GO terms it maps to, preserve. The cleanest
example is a **cofactor split**:

> **EC:1.1.1.256** → two RHEA reactions →
> `GO:0004090 carbonyl reductase (NADPH) activity` **and**
> `GO:0004022 alcohol dehydrogenase (NAD+) activity`

Here the single EC number is ambiguous about cofactor/substrate, but the two
RHEA reactions land on two distinct, more informative GO terms. For a protein
where UniProt asserts the specific RHEA, RHEA→GO yields a *better* MF term than
EC→GO would. (Other examples the script prints: EC:1.1.1.94 →
NADP+-specific glycerol-3-phosphate dehydrogenase; EC:3.1.3.56 → a specific
inositol-polyphosphate phosphatase.)

### 2b. RHEA → GO: many reactions collapse onto one generic term

The flip side. **679 GO terms are each backed by more than one RHEA reaction**,
and the top "absorbers" swallow dozens of distinct reactions:

| RHEA reactions | GO MF term |
|---:|---|
| 67 | GO:0004022 alcohol dehydrogenase (NAD+) activity |
| 65 | GO:0015020 glucuronosyltransferase activity |
| 53 | GO:0018812 3-hydroxyacyl-CoA dehydratase activity |
| 47 | GO:0003988 acetyl-CoA C-acyltransferase activity |
| 46 | GO:0080023 (2E)-enoyl-CoA hydratase activity |
| 45 | GO:0004090 carbonyl reductase (NADPH) activity |

These are reactions that differ by substrate (which alcohol, which acyl-chain
length, which acceptor sugar) but for which GO has **no substrate-specific
child** — so 67 distinct RHEA reactions all flatten to one
`alcohol dehydrogenase (NAD+) activity` term. The specificity RHEA encodes is
discarded at the GO layer not because of a mapping error but because the GO MF
branch lacks the granularity. These are the natural candidates for
`proposed_new_terms` if substrate-specific MF resolution is ever wanted.

**Net specificity picture.** Going *into* RHEA you gain resolution over EC;
going *out* to GO you usually lose it again (74% collapse), except for the 26%
of multi-reaction ECs where GO happens to carry the cofactor/substrate split.
RHEA→GO is therefore a specificity *bottleneck*, occasionally a specificity
*rescue*.

## 3. Mapping gaps found

| # | Gap | Size | What it is |
|---|-----|------|-----------|
| G1 | **EC-masking redundancy** | 4,324 reactions (88% of EC-carrying reactions with a GO term) | RHEA's `GO_REF:0000116` term duplicates a term EC2GO already supplies → low marginal value; would be dropped by closure-filtered uniqueness. |
| G2 | **RHEA-only GO terms** | 772 GO terms | Reachable via `rhea2go` but not `ec2go` — RHEA's unique term contribution; the priority set for the *forward* contribution audit. |
| G3 | **EC-without-`ec2go`** | 462 reactions | The reaction's EC has no `ec2go` line, so RHEA is the only EC-adjacent GO route — RHEA fills an EC2GO gap. |
| G4 | **No-`rhea2go` enzymatic reactions** | **2,731 of 7,635 (36%)** EC-carrying reactions | A genuine enzymatic reaction with **no GO MF target at all**. Of these, 2,445 (across 1,888 ECs) have no `rhea2go`-covered sibling reaction either (EC-level gap); 286 are specific-reaction-only gaps where a sibling reaction *is* GO-covered. (EC2GO may still cover some of the 1,888 ECs — this is a `rhea2go` coverage gap, not necessarily a total-GO gap.) |
| G5 | **Specificity-collapse** | 679 GO terms, up to 67:1 | GO MF granularity gap: many distinct reactions share one generic activity term; candidate `proposed_new_terms`. |
| G6 | **Reverse-propagation gap** | see [RHEA.md](../RHEA.md) pilot | UniProt entries carrying a RHEA whose mapped GO term never reaches GOA (closure-filtering required to confirm). |

### How the gaps interact

G1 (masking) and G4 (no-target) are mirror images: where EC and RHEA agree, RHEA
is redundant; where RHEA has no GO term, EC often still carries the protein via
its coarser EC-level term — so the enzyme is rarely left with *no* GO MF
annotation, it is left with a *less specific* one. The curation-relevant gaps are
therefore mostly **specificity** gaps (G4/G5 — the right activity exists in
biochemistry but GO represents it only coarsely) rather than **coverage** gaps
(the enzyme has no MF term at all), with G2/G3/G6 being the places RHEA genuinely
adds something EC does not.

## Reproduce

```bash
uv run python rhea_ec_specificity.py     # all section-1/2/3 numbers
uv run python rhea_go_gap_probe.py --gap-sample   # the reverse-propagation pilot
```

`ftp.expasy.org` (the usual RHEA bulk-download host) is blocked by the web
container's network policy; the script uses the RHEA REST API
(`https://www.rhea-db.org/rhea?columns=rhea-id,ec`) instead, which is reachable.
