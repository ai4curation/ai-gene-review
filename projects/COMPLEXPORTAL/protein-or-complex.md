---
title: "Does a Function Belong to the Protein or the Complex?"
autolink_gene_symbols: false
---

# Does a function belong to the protein or the complex?

[Back to the Complex Portal project](../COMPLEXPORTAL.md)

**Bottom line:** GO, Complex Portal (CP) and GO-CAM give three answers to the same
question. CP puts the molecular function (MF) on the complex entity. GO puts it on
gene products, with `enables` and `contributes_to` the only ways to say "this chain
is part of a unit that does X". GO-CAM can say "this complex does X" but exports
back to gene products. Several projects in this repo have run into the question
separately. This page draws them together into one working framework and measures
how the three representations line up. In the first measurement, 877 pairs of a CP
complex and one of its MF terms have every subunit reviewed here. For 255 of them GOA gives
the activity `enables` on every subunit, and our reviews do so for only 70. GOA
leaves 178 with no subunit annotated to the activity, and our reviews leave 349.
At subunit level, 492 rows that are `enables` in GOA are `contributes_to` in the
review's `core_functions`. They come mostly from rotary ATPases, Cys-loop channels,
complex I and RNA polymerases. These counts describe disagreement, not error. Where
the line between protein and complex should fall is the open question this page
sets up.

## The question

When the evidence for an activity comes from a complex, there are four places the
function could be recorded:

1. **On one chain**, the one that has the active site, binding site or pore
   (`enables` on that gene product).
2. **On every chain that does part of the work** (`contributes_to` on each).
3. **On the complex as an entity** (CP's `ComplexPortal:CPX-*` gene product, or a
   GO-CAM complex node), with no claim about which chain does what.
4. **Nowhere on a chain**: the subunit is annotated only to membership
   (`part_of` the GO complex term) or to the assembly, regulation or stability of
   the complex.

These are not interchangeable, and the choice changes what downstream users get.
In gene-set enrichment, a protease term on every proteasome alpha subunit inflates
the protease gene set. Variant interpretation relies on the catalytic chain, and a
`contributes_to` row hides it. ML benchmarks learn "subunit of X implies activity
X" from `enables` rows on structural chains. Orthology propagation copies whichever
answer was chosen to every species.

## How each resource answers it

| Resource | Where the MF goes | What a subunit gets | Source |
|---|---|---|---|
| GO annotation guidance | On gene products | `enables` for an activity the gene product executes; `contributes_to` for an activity of a complex that "cannot be ascribed to an individual subunit", given only to "the complex subunits required for the Molecular Function" | [GO annotation docs](https://geneontology.org/docs/go-annotations/), fetched 2026-11-22; go-annotation 6414 (SDH) |
| Complex Portal | On the CPX entity (`enables`, NAS) | No MF; BP and CC are rolled down to every subunit | [COMPLEXPORTAL](../COMPLEXPORTAL.md#two-annotation-layers) |
| GO-CAM | On a complex node or a single gene product | Export currently turns `has member` into `contributes_to` for all members; a split into active and accessory members is proposed | [PROTEIN_COMPLEX_FUNCTIONS](../PROTEIN_COMPLEX_FUNCTIONS.md#go-cam-and-export-position) |
| PAINT / IBA | On gene products, per node | Whatever qualifier the IBD carried; complex subunits in one family can inherit the full activity | [IBA_REVIEW](../IBA_REVIEW.md), [PSEUDOCAP](../PSEUDOCAP.md) |
| Genome-scale metabolic models | On the reaction | Every subunit is in the GPR (`A and B and C`); each is necessary, none is singled out | [METABOLIC_MODEL_ANALYSIS](../METABOLIC_MODEL_ANALYSIS.md) |
| This repo's schema | `core_functions.molecular_function` or `contributes_to_molecular_function`, plus `in_complex` | Reviewer chooses; `COMPLEX_ACTIVITY_TRANSFER` is the prediction-error type for the wrong choice | `src/ai_gene_review/schema/gene_review.yaml` |

GO's definition has two tests. The activity must not be ascribable to one
subunit, and only subunits "required for" it qualify. "Required" is where the
trouble starts. It is the same necessity-versus-participation problem that
CLAUDE.md sets out for process terms ("Do not add what curators deliberately
declined to add"). A subunit can be required because it does part of the work,
or because without it the complex never assembles. A knockout cannot tell the two
apart, and GAF rows record both the same way. The first test is also often
skipped: when one chain carries the whole active site, GO's own definition points
to `enables` on that chain, not `contributes_to` on every chain.

## What the sibling projects already found

| Project | What it contributes to this question |
|---|---|
| [PROTEIN_COMPLEX_FUNCTIONS](../PROTEIN_COMPLEX_FUNCTIONS.md) | The attribution spectrum (executor, subcomplex, whole complex, structural, regulatory, assembly), a review rubric, and the GO-CAM proposal for `has active member` versus `has accessory/structural member`. Structure prediction did not settle any interface. |
| [SDH_GP2TERM_CONTRIBUTES_TO](../SDH_GP2TERM_CONTRIBUTES_TO.md) | One upstream ruling: GO agreed that all four complex II subunits take `contributes_to` for succinate dehydrogenase (ubiquinone) activity, even SDHA, which carries the FAD site. The argument was that no single subunit does the whole reaction. |
| [OXPHOS](../OXPHOS.md) | 36 reviews applying one policy: core catalytic subunits `contributes_to` the complex activity, supernumerary subunits get membership and assembly terms, and assembly factors get no complex activity. |
| [BGC](../BGC.md) | Obligate heterodimers in natural-product clusters (KSα/KSβ-CLF, PqsB/PqsC), where the activity is assigned to the wrong partner. Here the activity sits at an interface. |
| [FUNCTION_REQUIREMENT_RULES](../FUNCTION_REQUIREMENT_RULES.md) | "Lacks the catalytic domain" flags turned out to be mostly `enables` that should be `contributes_to`. The rules therefore cover `enables` rows only, and exempt the peripheral catalytic subunits of primary active transporters, which GO itself gives `enables`. |
| [PSEUDOCAP](../PSEUDOCAP.md) | PAINT nodes that give the Sha/Mrp antiporter activity `enables` to subunits that were never mutated, including an assembly subunit. |
| [PROTEIN_DIMERIZATION_TERMS](../PROTEIN_DIMERIZATION_TERMS.md) | Rough consensus that "homodimerization activity" describes composition, not activity: the same confusion at its smallest scale. |
| [MOLECULAR_ADAPTOR_ACTIVITY](../MOLECULAR_ADAPTOR_ACTIVITY.md) | A scaffold or adaptor subunit has an activity of its own (bridging), which is the right replacement for both protein binding and a borrowed catalytic term. |
| [RNAP_II_HOLOENZYME_OBSOLETION](../RNAP_II_HOLOENZYME_OBSOLETION.md), [CHROMATIN_SILENCING_COMPLEX_OBSOLETION](../CHROMATIN_SILENCING_COMPLEX_OBSOLETION.md) | When a "complex" is really a purification or a grouping, it has no stable membership to attribute anything to. |
| [COMPLEXPORTAL](../COMPLEXPORTAL.md) | CP's BP and CC roll-down. Its most common errors are attribution errors: regulation terms on the regulated subunit, a partner's activity in BP form (MBL2 "proteolysis") and a promiscuous subunit (actin) inheriting every complex's processes. |

## Working framework

These are hypotheses to test against cases, not rules yet.

**A. The activity belongs to a chain** (record `enables` on it) when the chain does
the activity on its own when isolated, or carries every residue the chemistry needs
while the partners only position, stabilise or regulate it. Examples: the
proteasome β5 chain for the chymotrypsin-like protease, gpi8/PIGK for GPI
transamidase.

**B. The activity belongs to the complex, with named contributors**
(`contributes_to` on each), when the active site, pore or electron path spans
chains. Examples: the subunits lining a heteropentameric channel pore, the complex
II redox chain, a rotary ATPase stator and rotor.

**C. The chain is a member, not a contributor** (`part_of` only, plus its own
activity if it has one: adaptor, inhibitor, assembly). Examples: supernumerary
OXPHOS subunits, proteasome α subunits for the protease, scaffold subunits.

**D. The complex is not a stable unit** (variable composition, a purification or
a grouping). Attribute nothing beyond membership until the unit is defined.

Questions that separate the cases:

1. Was the activity shown for an isolated chain, a reconstituted subcomplex, the
   holocomplex, or only inferred from loss of function?
2. Where are the active site, cofactor, pore or binding surface, and do they span
   chains?
3. Does losing the chain stop the activity by removing part of the mechanism, or
   by preventing the complex from assembling?
4. Is the activity the same thing at the chain and complex level? A ligand-binding
   chain of a receptor complex enables binding. Only the assembled receptor has
   receptor activity.

Question 4 is why many disagreements are not really about qualifiers. The
complex term (`GABA-A receptor activity`) and the chain term (`GABA binding`,
`chloride channel activity`) can be different GO terms. In that case, giving every
chain the complex term is a term choice to fix, not a choice between `enables` and
`contributes_to`.

## First measurement: CP complex MF versus subunit annotation

Script: [`scripts/cp_mf_attribution.py`](scripts/cp_mf_attribution.py). Output:
[`data/cp_mf_attribution.yaml`](data/cp_mf_attribution.yaml). Inputs: CP
`complextab` files for ten species (curated complexes only, downloaded
2026-11-22), GO `go-basic.obo` release 2026-07-26, and the cached GOA and review
files in `genes/`. For each CP complex with an MF term, each subunit is classified
twice:

- by its GOA rows for that term or a descendant (`enables`, `contributes_to` or
  none);
- by its review's `core_functions` (as `molecular_function`, as
  `contributes_to_molecular_function` or absent).

Of the 5,210 curated complexes loaded, 4,298 carry at least one MF term. 3,643
complex-MF pairs have at least one subunit reviewed here: 260 are homomeric and
3,383 heteromeric. In 877 heteromeric pairs every subunit is reviewed, and only
those give a complete picture.

**How the activity is spread over the subunits (877 fully reviewed heteromeric
pairs):**

| Pattern | GOA | Review `core_functions` |
|---|---|---|
| One subunit `enables`, the rest have no MF row | 353 | 239 |
| Every subunit `enables` | 255 | 70 |
| No subunit annotated to the activity | 178 | 349 |
| Mix of `enables` and `contributes_to` | 36 | 109 |
| Every subunit `contributes_to` | 7 | 79 |
| Several `enables`, the rest none | 45 | 14 |
| Some `contributes_to`, the rest none | 3 | 17 |

**Subunit level (all heteromeric pairs, reviewed subunits only):**

| GOA | Review core | Subunits |
|---|---|---|
| none | none | 3,476 |
| `enables` | `enables` | 1,358 |
| `enables` | none | 1,015 |
| `enables` | `contributes_to` | 492 |
| none | `contributes_to` | 393 |
| `contributes_to` | `contributes_to` | 118 |
| `contributes_to` | none | 66 |
| none | `enables` | 56 |
| `contributes_to` | `enables` | 14 |

**What this shows so far:**

- **GOA makes "every subunit `enables`" common for heteromers (255 of 877).** The
  terms behind it are mostly channels and receptors (Cys-loop acetylcholine and
  GABA-A receptors, NMDA receptors, voltage-gated calcium channels) and
  transcription-factor heterodimers. Our reviews mostly turn these into
  `contributes_to` or leave the activity out of `core_functions`. The 492
  `enables` to `contributes_to` subunits are led by rotary ATPases (61), chloride
  channels (60), acetylcholine-gated channels (48), complex I (32) and RNA
  polymerases (19).
- **"Nobody" is frequent and mostly not an error.** In GOA, the leading
  complex-level MF terms with no subunit annotation are generic binding terms
  (calcium ion, ATP and single-stranded DNA binding; "ubiquitin binding" alone accounts
  for 55 pairs). CP asserts these on the complex, and chain-level curation does not
  repeat them. In reviews, "nobody" also includes subunits whose `core_functions`
  describe a different, more specific activity. The descendant-only match counts
  those as absent.
- **The reverse disagreement is rare but informative (14 subunits).** Here GOA
  says `contributes_to` and the review says `enables`. Two leads to check:
  - **SCHPO/gaa1**: the review's prose calls gaa1 a structural and recognition
    subunit that "contributes the complex-level GPI-anchor transamidase activity",
    but the slot it uses is `molecular_function`, not
    `contributes_to_molecular_function`. PomBase's row is `contributes_to`. A
    check that compares core-function prose with the slot would catch this.
  - **human EMC subunits** (EMC1, EMC3, EMC4, EMC6, EMC7, MMGT1): the reviews give
    `enables` membrane insertase activity to subunits that are not the
    EMC3/EMC6 insertase core.
- **Homomers are the control.** For the 260 homomeric pairs, GOA never uses
  `contributes_to`, as expected. In three homomeric pairs the review's `core_functions`
  do use it. These need a look, because for a homomer `contributes_to` is a
  slot error unless the activity really needs a heteromeric partner that CP left
  out.

**Limitations.** Matching is by term and descendants only, so a review that gives
a chain a different but correct activity counts as "none". CP complexes overlap,
with paralog variants and sub-complexes, so the pairs are not independent: the same
CHRNA1 rows count once for every nAChR variant. Paralog sets in CP participant
lists are expanded to all members. The review verdicts are AI reviews and do not
form a gold standard. Most of the disagreement is a convention question, which
this page is meant to settle; it is not a count of errors.

## Next steps

- [ ] Hand-adjudicate a stratified sample of the 492 `enables` to `contributes_to`
      subunits, per complex class (channels, rotary ATPases, polymerases,
      transcription-factor dimers), against the framework above. Decide which
      class each belongs to and whether the fix is the qualifier or the term.
- [ ] Ask GO for the current convention on heteromeric ion channels. The
      transporter exemption in FUNCTION_REQUIREMENT_RULES and the SDH ruling point
      in different directions.
- [ ] Add a review check: `core_functions` prose saying "contributes" or
      "subunit of" while `molecular_function` is set, and `contributes_to` on a
      chain whose CP complex is homomeric.
- [ ] Re-review SCHPO/gaa1 and the EMC set (separate content PRs).
- [ ] Compare with GO-CAM complex nodes in `gocams/`: which models use a complex
      node for the activity, and what does the export give each member?
- [ ] Join the CP `Complex assembly` and ECO fields, to test whether
      ortholog-templated complexes are more likely to have no chain-level
      attribution.
- [ ] Write the framework into a short guidance section for gene-review authors
      once the adjudicated sample supports it.

## Reproduce

```bash
D=projects/COMPLEXPORTAL
mkdir -p /path/to/complextab && cd /path/to/complextab
for t in 9606 10090 10116 559292 284812 6239 7227 83333 3702 208964; do
  curl -sO https://ftp.ebi.ac.uk/pub/databases/intact/complex/current/complextab/$t.tsv
done
curl -sLO http://purl.obolibrary.org/obo/go/go-basic.obo
cd -
uv run python $D/scripts/cp_mf_attribution.py /path/to/complextab /path/to/complextab/go-basic.obo $D/data/cp_mf_attribution.yaml
```

The downloads are not committed. The output reflects the CP release current on
the download date and the GOA snapshot cached in `genes/`.
