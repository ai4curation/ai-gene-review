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
a COMPLETE review (its review page is linked from the gene symbol GRB2); this
page reads that review through the project's
[decision rules](../MOLECULAR_ADAPTOR_ACTIVITY.md#decision-rules-draft) rather
than re-deciding anything.

## Starting state (GOA)

The table below is the **experimental-only** view (the sidecar filters to
`ECO:0000269` descendants); the full `GRB2-goa.tsv` also carries an IEA adaptor
row, so there are **7 adaptor rows, not 6** — see Rule 5.

| GO term | id | rows | evidence |
|---|---|---:|---|
| protein binding | GO:0005515 | **567** | IPI (uninformative — not an adaptor term) |
| protein-macromolecule adaptor activity | GO:0030674 | 4 | IDA ×3 + IEA |
| guanyl-nucleotide exchange factor adaptor activity | GO:0005091 | 2 | IDA + IEA |
| transmembrane receptor protein tyrosine kinase adaptor activity | GO:0005068 | 1 | **IEA only** (mouse `Q60631`) |

567 bare `protein binding` rows against the adaptor rows. Almost all of the 567
are `IPI` (`ECO:0000353`) interactions deposited by IntAct — one row per
partner GRB2 was seen to bind (EGFR `P00533`, SOS, SHC, CBL, GAB1, …). They
record *what GRB2 sticks to*, which is exactly the information `protein binding`
throws away: 567 partners of **one** adaptor function, not 567 functions.

The informative molecular functions are already present, with direct
experimental evidence:

- `GO:0005091` GEF adaptor activity — IDA, PMID:8386805 (the original
  GRB2–SOS–Ras coupling).
- `GO:0030674` protein-macromolecule adaptor activity — IDA, PMID:25870599
  (multivalent adaptor organising LAT signalosome clusters) and PMID:7539782
  (the review flags PMID:7539782 as showing association rather than bridging).

## Applying the decision rules

**Rule 1 — bare `protein binding` → adaptor only when it is bridging.** The
existing review removed 472 of the 567 rows under the protein-binding policy and
rewrote 92 to the specific activity each interaction actually demonstrates
(`MODIFY`). The replacements are instructive:

| Replacement term | id | rows (from MODIFY) |
|---|---|---:|
| phosphotyrosine residue binding | GO:0001784 | 56 |
| proline-rich region binding | GO:0070064 | 20 |
| GEF adaptor activity | GO:0005091 | 7 |
| transmembrane receptor protein tyrosine kinase adaptor activity | GO:0005068 | 6 |
| protein-macromolecule adaptor activity | GO:0030674 | 4 |

(Replacement-term frequency; a few rows carry two replacement terms, so the
column sums slightly above the 92 MODIFY rows. The 567 GOA rows collapse to 564
distinct reference+partner pairs in the review — nothing is missing.)

The two biggest buckets are not adaptor terms but the **two binding activities
that mechanistically constitute** GRB2's adaptor function: the SH2 domain
reading phosphotyrosine (`GO:0001784`) and the SH3 domains reading proline-rich
`PxxP` motifs (`GO:0070064`). This is the key teaching point — an adaptor's
bridging is the sum of its individual recognition activities, and a reviewer
chooses the adaptor MF for the *bridging as a whole* and the binding MFs for the
*individual contacts*, rather than leaving either as `protein binding`.

**Rule 2 — most specific descendant.** GRB2 uses the specific children the
evidence licenses: `GO:0005068` (adaptor *for* the activated RTK) and `GO:0005091`
(adaptor *for* the GEF). It also keeps the **parent** `GO:0030674` — but, per
decision rule 5, *not* as a redundant general term beside its own descendants.
The review keeps it for a **distinct bridging event the children do not cover**:
GRB2's organisation of LAT microclusters and recruitment of PLCγ1 at the immune
synapse (PMID:25870599, `directly_involved_in` GO:0050852 T cell receptor
signaling). Without that distinct event, a parent sitting beside its children is
`TOO_GENERAL`; the condition is what makes all three legitimate.

**Rule 3 — adaptor vs scaffold/sequestering/carrier.** GRB2 is an adaptor, not a
scaffold: it is a small, transient, stoichiometric bridge (SH2 to one partner,
SH3 to another), not a platform that nucleates a condensate or holds many
clients. None of the scaffold/sequestering/carrier terms apply.

**Rule 4 — name the bridged partners (`has input`).** The adaptor MF is only
meaningful with its two ends named. For GRB2 the canonical pair is the
autophosphorylated receptor (or the LAT/SHC phosphoprotein) on the SH2 side and
SOS1/SOS2 on the SH3 side; these are its `has input` molecules.

*The hard call* (and the one the project exists to settle) is the MF-to-MF
relation to the SOS GEF activity in a GO-CAM. The project page's gloss makes
`provides input for` the default for "brings an enzyme to its substrate", which
fits GRB2 recruiting SOS to membrane Ras. The case for the stronger
`directly positively regulates` is specific: SOS is **autoinhibited** in the
cytosol, and GRB2-mediated recruitment to the membrane (plus allosteric Ras-GTP
binding) **relieves that autoinhibition** — i.e. the adaptor does not merely
deliver SOS to Ras, it raises SOS's exchange activity. That is a genuine
activation, so `directly positively regulates` is defensible here — but it is a
judgement that needs stating, not a default; a reviewer who cannot show the
activation step should use `provides input for`.

**Rule 5 — treat propagated rows as inference.** GRB2 has **three** IEA adaptor
rows, and they split two ways. `GO:0005091` and `GO:0030674` sit on top of direct
human IDA for the same terms, so they are `ACCEPT`ed as consistent — not
independent support. `GO:0005068`, by contrast, has **no human experimental row
at all**: it is IEA-only (from mouse `Q60631`) yet is `ACCEPT`ed as a core
function on converging small-scale evidence (with PMID:11533253 as an additional
reference). That is the most instructive rule-5 case in the gene — an IEA-only
term kept because the biology converges, not because an IDA already carries it.

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

1. **Scale.** The payoff is concentrated — one gene turned 92 `protein binding`
   rows into informative MF rewrites (plus 472 removed). The core_adaptor
   worklist genes are where this concentration is highest.
2. **Adaptor MF ≠ a single binding MF.** Expect to add both the adaptor term(s)
   *and* the specific domain-level binding terms (phosphotyrosine, proline-rich,
   etc.); they are complementary, not redundant.
3. **IntAct `protein binding` rows are a partner list.** Read them as candidate
   `has input` partners of one adaptor function, not as separate functions —
   this is the fastest way to pick the right adaptor child and its inputs.
4. **Specific children are usually justified for well-studied adaptors.** Do not
   stop at `GO:0030674` when the evidence names both ends of the bridge.
