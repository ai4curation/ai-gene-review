---
title: "Cytoplasm"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
index_group: CROSS_CUTTING
description: Is GO:0005737 cytoplasm ever informative? In eukaryotes it is never a core location; in prokaryotes it keeps the normal rules.
---

# Cytoplasm

**Bottom line:** this page sets how reviews treat `GO:0005737` cytoplasm. In a
**eukaryote** the term includes every organelle, so it says little more than "not
nuclear, not extracellular". It is never a core location: never `ACCEPT`, and
never in `core_functions.locations`. A cytoplasm row is `TOO_GENERAL` when the
review asserts a more specific location that GO places under cytoplasm (cytosol,
an organelle, a granule). It is `MODIFY` when the row's own evidence resolves
where the protein is, and `KEEP_AS_NON_CORE` otherwise. In a **prokaryote**
cytoplasm is the main localisation contrast (with membrane, periplasm and the
outside), so it is informative and keeps the normal rules. `just validate` warns
on the eukaryotic `ACCEPT`, `NEW` and core-location cases
(`check_type: cytoplasm_policy`), and `just cytoplasm-audit` lists every row the
policy would change. Proposed 2026-11-26.

## The question

> Is it ever useful to project eg iba iss iea to cytoplasm? Cytoplasm has always
> seemed a useless term to me. For experimental we should at least know cytosol
> unless it's an experiment that is too broad for GO.

## What the term says

GO defines the two terms as:

- `GO:0005737` cytoplasm: "The contents of a cell excluding the plasma membrane
  and nucleus, but including other subcellular structures."
- `GO:0005829` cytosol: "The part of the cytoplasm that does not contain
  organelles but which does contain other particulate matter, such as protein
  complexes."

So in a eukaryote a mitochondrial-matrix or ER-lumen protein is, by definition,
in the cytoplasm. The term is true of almost every protein that is neither
nuclear, secreted nor confined to the plasma membrane. It is also what a naive
predictor outputs for a protein with no signal peptide or transmembrane segment
(the `LOCALIZATION_DEFAULT` error type in prediction reviews).

There is also a translation problem. When an author writes "cytoplasmic" they
usually mean diffuse and non-nuclear, which in practice is cytosol. A curator who
maps the word literally to `GO:0005737` records a weaker claim than the one the
paper made.

**What GO places under cytoplasm.** The `TOO_GENERAL` test uses GO's own is_a and
part_of closure. In the GO snapshot the validator uses, these are under cytoplasm:
cytosol, mitochondrion and its parts, the ER and its lumen, Golgi, lysosome,
cytoplasmic vesicle, cell cortex, perinuclear region of cytoplasm, cytoplasmic
stress granule, P-body and chloroplast. These are **not**: cytoskeleton,
microtubule, centrosome, ribosome, nucleoid, nucleus and cytoplasmic side of
plasma membrane. Microtubules and centrosomes also occur in or at the nucleus, so
a microtubule row does not make a cytoplasm row redundant. The integration test
`tests/test_cytoplasm_policy.py` pins the cases the check relies on.

## Where the rows come from

Most electronic cytoplasm rows restate a UniProt subcellular location of
"Cytoplasm" with no finer sub-location. Counts of IEA `GO:0005737` rows by
reference, across the corpus's cached `*-goa.tsv` files on 2026-11-25:

| Reference | Source | IEA rows |
|---|---|---:|
| `GO_REF:0000044` | UniProtKB subcellular location mapping | 1,615 |
| `GO_REF:0000120` | combined automated annotation (multiple IEA methods) | 1,022 |
| `GO_REF:0000117` | ARBA | 242 |
| `GO_REF:0000107` | Ensembl Compara orthology projection | 166 |
| `GO_REF:0000118` | TreeGrafter | 92 |
| `GO_REF:0000002` | InterPro2GO | 85 |

```bash
awk -F'\t' 'FNR>1 && $5=="GO:0005737" && $9=="IEA" {c[$10]++}
  END {for (r in c) print c[r] "\t" r}' genes/*/*/*-goa.tsv | sort -rn
```

An IBA row on cytoplasm says something only when the family has nuclear members,
so that the PAINT node marks a real split. Otherwise it passes the default down
the tree. An ISS, ISO or Ensembl Compara row copies an ortholog's cytoplasm row.
In every one of these cases the row's evidence stops at cytoplasm by
construction.

## Policy

### Eukaryotes

1. **Never `ACCEPT`, never a core location.** `ACCEPT` marks a term as
   representing the core function, and in a eukaryote cytoplasm never says where a
   core activity happens. This is an exception to "if the general term is as
   precise as the evidence allows, keep it (`ACCEPT` if core)". As with the
   protein-binding policy, the problem is lack of information, not a false claim.
   In `core_functions.locations`, name the compartment where the activity is shown
   to happen, or omit the location.
2. **`TOO_GENERAL` when the review asserts something GO places under cytoplasm.**
   Cytoplasm is the cytoplasmic counterpart of `GO:0016020` membrane, the example
   in the 2026-11-14 ruling: imprecise on its own ("which part of the
   cytoplasm?"). This holds whatever the row's evidence code. It judges the term,
   not the evidence.
3. **`MODIFY` only on the row's own evidence.** A propagated row (IBA, IEA, ISS,
   ISO, ISA, ISM, IGC, RCA) cannot support a deeper term, because its source is
   itself a cytoplasm annotation, keyword or mapping. Use `TOO_GENERAL` if a
   specific location is asserted elsewhere. Otherwise use `KEEP_AS_NON_CORE`, and
   add a `NEW` row for the specific location only on evidence of its own. For an
   experimental row, read what the assay could resolve (table below).
4. **Otherwise `KEEP_AS_NON_CORE`.** This is the honest action when the evidence
   separates only nucleus from the rest. Consider whether the gene needs a `NEW`
   cytosol or organelle row on independent evidence.
5. **No `NEW` cytoplasm rows.** Propose the specific location the evidence
   supports, or nothing.
6. **Generality is not a reason to `REMOVE`.** A cytoplasm row on a
   mitochondrial-matrix protein is true by definition and is `TOO_GENERAL`.
   `REMOVE` or `MARK_AS_OVER_ANNOTATED` is for a claim that is wrong, such as a
   default prediction for a protein that is nuclear, secreted or in the plasma
   membrane.

| What the assay resolves | Example | Action on the cytoplasm row |
|---|---|---|
| The soluble cytoplasm | diffuse immunofluorescence or GFP throughout the cytoplasm (which the Human Protein Atlas scores as "Cytosol"); a high-speed supernatant; release by digitonin | `MODIFY` to `GO:0005829` cytosol |
| A named structure | co-localisation with an organelle, granule or cortex marker | `MODIFY` to that structure |
| Nucleus versus the rest | nuclear/cytoplasmic fractionation kits, whose "cytoplasmic fraction" carries membranes and organelles; "cytoplasmic and nuclear" staining at low resolution | `KEEP_AS_NON_CORE` |
| An unidentified structure | punctate or perinuclear staining with no marker | `KEEP_AS_NON_CORE`; do not refine to cytosol |
| A fraction of unknown purity | proteomics of a "cytoplasmic" fraction (HDA) | usually `KEEP_AS_NON_CORE` |

**Shuttling proteins.** For a protein that moves between nucleus and cytoplasm,
the information is the partition and its regulation, which a static location
term cannot carry. Do not use `GO:0042994` cytoplasmic sequestering of
transcription factor or `GO:0051220` cytoplasmic sequestering of protein: both are
obsolete, because GO judged that they describe a molecular function, not a
process. A process term such as `GO:0042308` negative regulation of protein import
into nucleus belongs to the protein that does the retaining, not to its cargo
(the participation test in `CLAUDE.md`).

### Prokaryotes

Bacteria and archaea have no organelles, so cytoplasm is close to cytosol, and the
localisation question is cytoplasm versus inner membrane, periplasm, outer
membrane or outside. A cytoplasm row there makes a real claim, including a
propagated one. Apply the normal rules, and treat cytoplasm like a root organelle
term (`projects/ORGANELLES.md`): informative, so never `TOO_GENERAL`. A `MODIFY`
to cytosol is allowed when the row's own evidence supports it, but adds little and
is not required.

### Out of scope

- **Viruses.** A viral protein in the host cell has its own term,
  `GO:0030430` host cell cytoplasm. Whether GOA's `GO:0005737` rows on viral
  proteins should move there is an open question.
- **`NOT` rows.** "Not in the cytoplasm" is a negative claim and carries
  information.
- **Entries whose lineage cannot be read** from the UniProt record beside the
  review.

## Worked example: ARATH/NPR1

`genes/ARATH/NPR1` has six cytoplasm rows (IBA, IEA from `GO_REF:0000120`, IDA
from PMID:26269953 and PMID:10662863, EXP from PMID:11148282 and PMID:12837250),
all `ACCEPT`ed, and no cytosol row. The IBA and IEA rows quote PMID:12615947:

> NPR1 modulates cross-talk between salicylate- and jasmonate-dependent defense
> pathways through a novel function in the cytosol.

So the review's own evidence names the cytosol, but the review records only the
weaker term, as core. Under this policy:

1. Add a `NEW` `GO:0005829` cytosol row on PMID:12615947, with that quote. The
   IBA and IEA rows cannot be `MODIFY`, because their evidence stops at cytoplasm
   (rule 3).
2. With the cytosol row in place, the IBA and IEA rows are `TOO_GENERAL` (rule 2).
   Without it they would be `KEEP_AS_NON_CORE` (rule 4).
3. Each IDA and EXP row is `MODIFY` to cytosol only if its own paper shows the
   cytosol. Otherwise it is `TOO_GENERAL` as well.

NPR1 moves between nucleus and cytoplasm, and so do several of the other genes in
the hard residue the audit finds (EMENI/veA, EMENI/velB, CANAL/HOG1).

## Corpus census (2026-11-26)

`just cytoplasm-audit` over 12,487 reviews. Non-`NOT` `GO:0005737` rows by
lineage and action:

| Action | Eukaryota | Bacteria | Archaea | Viruses |
|---|---:|---:|---:|---:|
| `ACCEPT` | 4,618 | 509 | 20 | 0 |
| `KEEP_AS_NON_CORE` | 1,345 | 81 | 0 | 0 |
| `MODIFY` | 865 | 320 | 0 | 0 |
| `TOO_GENERAL` | 235 | 39 | 0 | 0 |
| `MARK_AS_OVER_ANNOTATED` | 176 | 8 | 0 | 0 |
| `UNDECIDED` | 43 | 6 | 0 | 0 |
| `REMOVE` | 24 | 7 | 0 | 0 |
| `NEW` | 19 | 49 | 11 | 1 |

What the policy would change:

| Category | Findings | Warned by `just validate` | Fix |
|---|---:|:-:|---|
| `EUK_ACCEPT` | 4,618 | yes | `TOO_GENERAL` for 3,865 (3,236 of them entailed by cytosol); rule 3 or 4 for the other 753 |
| `EUK_CORE_LOCATION` | 989 | yes | name the compartment, in 763 reviews |
| `EUK_MODIFY_PROPAGATED` | 596 | no | `TOO_GENERAL` for 585; `KEEP_AS_NON_CORE` plus a `NEW` row for 11 |
| `PROK_TOO_GENERAL` | 39 | no | back to `ACCEPT` or `KEEP_AS_NON_CORE` |
| `EUK_NEW` | 19 | yes | the specific location, or drop |
| `EUK_TOO_GENERAL_UNENTAILED` | 0 | no | |

The warned categories fall in 1,980 review files. Of the 753 `EUK_ACCEPT` rows
that nothing more specific entails, 275 are IEA, 177 IBA, 141 IDA, 50 EXP and 39
HDA. A sample of twelve experimental ones included four proteins known to shuttle
between nucleus and cytoplasm. Their assays have not been checked row by row.

## Enforcement

`src/ai_gene_review/validation/cytoplasm_policy.py`:

- **`just validate`** warns (`cytoplasm_policy`) on eukaryotic `ACCEPT` and `NEW`
  cytoplasm rows and on cytoplasm in `core_functions.locations`. The lineage is the
  first `OC` line of the UniProt record beside the review. With the ontology
  loaded, the warning names any asserted location that makes the row
  `TOO_GENERAL`.
- **`just cytoplasm-audit`** writes every finding to
  `reports/cytoplasm-policy.tsv` (git-ignored), with the entailing terms, and
  prints the tallies above.

Severity is WARNING, as for the protein-binding policy. The policy applies to new
and revisited reviews. Reviews merged before it are not retroactively defective,
and migrating them is a separate sweep, not a condition of any content PR.

## Open questions

- **Bulk migration.** The 3,865 entailed `EUK_ACCEPT` rows and 585 entailed
  `EUK_MODIFY_PROPAGATED` rows could be relabelled `TOO_GENERAL` mechanically. The
  753 unentailed rows need a reviewer.
- **Warn on `EUK_MODIFY_PROPAGATED`?** It follows from the 2026-11-14 ruling, but it
  is audit-only for now.
- **Upstream.** Should UniProt's plain "Cytoplasm" sub-location be raised where its
  own evidence names the cytosol, as in the NPR1 example?
- **Other near-root terms.** The same reasoning may apply to `GO:0005622`
  intracellular anatomical structure and, in part, to cell periphery
  (`projects/CELL_PERIPHERY_DEFINITIONS.md`).
