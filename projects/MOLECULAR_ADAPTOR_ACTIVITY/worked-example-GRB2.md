---
title: "Worked example: GRB2"
species: [human]
---

# Worked example: GRB2 (`P62993`)

Back to the [project page](../MOLECULAR_ADAPTOR_ACTIVITY.md).

GRB2 is the textbook signaling adaptor and a good first worked example because
it shows the problem this project exists to fix in a single gene: its GOA is
dominated by uninformative `protein binding`, while the function that makes
GRB2 *GRB2* — bridging an activated receptor tyrosine kinase to the Ras
exchange factor SOS — is carried by a handful of adaptor rows. GRB2 already has
a [COMPLETE review](../../genes/human/GRB2/GRB2-ai-review.yaml); this page reads
that review through the project's [decision rules](../MOLECULAR_ADAPTOR_ACTIVITY.md#decision-rules-draft)
rather than re-deciding anything.

## Starting state (GOA)

| GO term | id | rows | branch |
|---|---|---:|---|
| protein binding | GO:0005515 | **567** | (uninformative — not an adaptor term) |
| protein-macromolecule adaptor activity | GO:0030674 | 4 | core_adaptor |
| guanyl-nucleotide exchange factor adaptor activity | GO:0005091 | 2 | core_adaptor |

567 bare `protein binding` rows against 6 adaptor rows. Almost all of the 567
are `IPI` (`ECO:0000353`) interactions deposited by IntAct — one row per
partner GRB2 was seen to bind (EGFR `P00533`, SOS, SHC, CBL, GAB1, …). They
record *what GRB2 sticks to*, which is exactly the information `protein binding`
throws away: 567 partners of **one** adaptor function, not 567 functions.

The informative molecular functions are already present, with direct
experimental evidence:

- `GO:0005091` GEF adaptor activity — IDA, PMID:8386805 (the original
  GRB2–SOS–Ras coupling).
- `GO:0030674` protein-macromolecule adaptor activity — IDA, PMID:25870599
  (multivalent adaptor organising LAT signalosome clusters) and PMID:7539782.

## Applying the decision rules

**Rule 1 — bare `protein binding` → adaptor only when it is bridging.** The
existing review removed 472 of the 567 rows under the protein-binding policy and
rewrote 92 to the specific activity each interaction actually demonstrates
(`MODIFY`). The replacements are instructive:

| Replacement term | id | rows (from MODIFY) |
|---|---|---:|
| phosphotyrosine residue binding | GO:0001784 | 56 |
| proline-rich region binding | GO:0070064 | 19 |
| GEF adaptor activity | GO:0005091 | 7 |
| transmembrane receptor protein tyrosine kinase adaptor activity | GO:0005068 | 6 |
| protein-macromolecule adaptor activity | GO:0030674 | 4 |

The two biggest buckets are not adaptor terms but the **two binding activities
that mechanistically constitute** GRB2's adaptor function: the SH2 domain
reading phosphotyrosine (`GO:0001784`) and the SH3 domains reading proline-rich
`PxxP` motifs (`GO:0070064`). This is the key teaching point — an adaptor's
bridging is the sum of its individual recognition activities, and a reviewer
chooses the adaptor MF for the *bridging as a whole* and the binding MFs for the
*individual contacts*, rather than leaving either as `protein binding`.

**Rule 2 — most specific child.** GRB2 does not stop at `GO:0030674`. The review
keeps `GO:0030674` (general multivalent adaptor, well supported) but also uses
the specific children the evidence licenses: `GO:0005068` (adaptor *for* the
activated RTK) and `GO:0005091` (adaptor *for* the GEF). All three are legitimate
because GRB2 genuinely bridges at both ends.

**Rule 3 — adaptor vs scaffold/sequestering/carrier.** GRB2 is an adaptor, not a
scaffold: it is a small, transient, stoichiometric bridge (SH2 to one partner,
SH3 to another), not a platform that nucleates a condensate or holds many
clients. None of the scaffold/sequestering/carrier terms apply.

**Rule 4 — name the bridged partners (`has input`).** The adaptor MF is only
meaningful with its two ends named. For GRB2 the canonical pair is the
autophosphorylated receptor (or the LAT/SHC phosphoprotein) on the SH2 side and
SOS1/SOS2 on the SH3 side. In a GO-CAM this is `has input` the receptor +
`directly positively regulates` the SOS GEF activity (the regulatory-adaptor
pattern, not merely `provides input for`). The 567 IntAct partners are the raw
material for choosing those inputs — most are SH2 or SH3 contacts of the single
adaptor activity.

**Rule 5 — treat propagated rows as inference.** GRB2's two IEA adaptor rows
(`GO:0005091` via ARBA/ortholog, `GO:0030674` via GO_REF:0000107 from mouse
`Q60631`) sit on top of direct human IDA for the same terms, so they are
`ACCEPT`ed as consistent — not challenged, not treated as independent support.

## Outcome in the review

The four core functions the review settled on are all adaptor/recognition MFs,
with `protein binding` gone entirely:

- `GO:0005068` transmembrane receptor protein tyrosine kinase adaptor activity
- `GO:0001784` phosphotyrosine residue binding (SH2 mechanism)
- `GO:0005091` guanyl-nucleotide exchange factor adaptor activity (SOS coupling)
- `GO:0030674` protein-macromolecule adaptor activity (LAT signalosome)

Across the whole review the 567 `protein binding` rows became 472 `REMOVE` + 92
`MODIFY`; every adaptor row was `ACCEPT`ed as core.

## Lessons for the project

1. **Scale.** The payoff is concentrated — one gene turned ~95 informative
   rewrites out of 567 uninformative rows. The core_adaptor worklist genes are
   where this concentration is highest.
2. **Adaptor MF ≠ a single binding MF.** Expect to add both the adaptor term(s)
   *and* the specific domain-level binding terms (phosphotyrosine, proline-rich,
   etc.); they are complementary, not redundant.
3. **IntAct `protein binding` rows are a partner list.** Read them as candidate
   `has input` partners of one adaptor function, not as separate functions —
   this is the fastest way to pick the right adaptor child and its inputs.
4. **Specific children are usually justified for well-studied adaptors.** Do not
   stop at `GO:0030674` when the evidence names both ends of the bridge.
