---
title: "Yeast Genes Re-Review: REMOVE actions"
species: [yeast]
autolink_exclude: [RCA, old, COX10]
---

# Re-review of REMOVE actions in yeast gene reviews

Back to the [human REMOVE re-review](REMOVE_RE_REVIEW.md), of which this is
the yeast counterpart. The mouse and rat reviews had the same pass in
[ai4curation/ai-gene-review#6513](https://github.com/ai4curation/ai-gene-review/pull/6513).
Tracked in [#4097](https://github.com/ai4curation/ai-gene-review/issues/4097).

**Bottom line:** every annotation row with `action: REMOVE` in `genes/yeast`
was read again against the current review rules (read on 18 November 2026,
applied on 20 November at commit `9496534c1` of main). There were 3,068 such
rows in the 905 review files. 2,440 are bare `protein binding` rows, which the
protein-binding policy removes as uninformative; they were audited by script
and none changed action. The other 628 rows, in 342 reviews, were read one at
a time.
**38 of them (6%) no longer say REMOVE**, 590 stand, and 5 errors in source
records were written down as structured `source_defects`. 27 review files
were edited. No row was changed to REMOVE.

The row-level record is in
[`yeast_remove_rereview_changes.yaml`](yeast_remove_rereview_changes.yaml):
every changed row with its old and new action and the rule applied, the
REMOVE rows that were examined closely and kept, and the rows outside this
pass that it shows to need another look.

## Why so few rows changed

In the human and in the mouse and rat reviews, 23% of the substantive REMOVE
rows changed. In yeast it is 6%, because most yeast REMOVE rows rest on a
stated biological argument:

- **Half are pathway-derived rows.** 327 of the 628 rows are `RCA` rows that
  SGD derives from the YeastPathways GO-CAMs. They were removed for the
  systematic errors of that conversion, which
  [YeastPathways to Modules](../YEAST_PATHWAYS.md) describes: the cytosol as
  default compartment for enzymes that work elsewhere (209 rows), the process
  of a superpathway given to all its members (`bifid shunt` on 28 glycolytic
  and fermentative enzymes, `chorismate metabolic process` on 15 enzymes), and
  reactions assigned to the wrong enzyme. Four of the 327 changed.
- **The phylogenetic rows argue with the tree.** 119 of the 121 `IBA` rows
  carry a propagation review that names the node and a ground specific to the
  target: a paralog with another substrate or compartment, a pseudoenzyme, a
  pathway that yeast lacks. Two changed.
- **The no-data rows were settled before.** All 14 are stale under the no-data
  policy (the [no-data project](../NO_DATA.md) had swept them), so none
  changed.

The changes are concentrated where the human pass also found them:
high-throughput locations removed as contamination, rows removed although
the same term is kept on another row, and curated rows removed on the
strength of an abstract that in fact supports them.

## Method

- **Triage by script.** For every REMOVE row the triage recorded the other
  rows of the same term in the review with their qualifiers, kept terms below
  it in the ontology, the evidence and reference, whether the cited paper is
  in the cache as full text, and whether GOA still carries the row.
- **Rows read one at a time**, by category: same term kept in the review,
  ancestor of a kept term, no-data rows, root organelle rows, experimental
  rows, curator statements, pathway-derived rows and phylogenetic rows.
- **Rules as in the human pass.** A REMOVE that rests on a biological argument
  was left alone, also where another action would have been defensible.
- **Two rulings made since the human pass were applied.** A correct but general
  term is `MODIFY` only where the row's own evidence supports the specific
  term, and `TOO_GENERAL` is kept for terms that are imprecise on their own.
  A wrong-gene or wrong-reference claim is confident only where the unread
  part of the paper could not overturn it; how a resource annotated a paper is
  a lead, not a proof, and is recorded as a query.
- **Reference-level checks.** For each wrong-gene claim that the pass kept or
  recorded, every annotation made from the paper was listed in QuickGO. One
  paper that the cache holds as an abstract only (SAS3) was read in full on
  its PMC page.

## Results

| | Yeast |
|---|---|
| Review files | 905 |
| REMOVE rows at start | 3,068 |
| Bare protein binding (unchanged) | 2,440 |
| Substantive rows read | 628 |
| Reviews with substantive rows | 342 |
| Rows that no longer say REMOVE | 38 |
| REMOVE rows at end | 3,030 |
| Review files edited | 27 |

**By evidence code**

| Evidence | Rows read | Changed |
|---|---|---|
| RCA (YeastPathways) | 327 | 4 |
| IBA | 121 | 2 |
| IEA | 92 | 10 |
| IDA | 16 | 2 |
| HDA | 15 | 12 |
| ND | 14 | 0 |
| TAS (Reactome) | 10 | 0 |
| IPI (not bare protein binding) | 8 | 4 |
| IMP | 7 | 1 |
| NAS | 7 | 2 |
| ISS | 5 | 0 |
| IGI, EXP | 4 | 0 |
| ISA, ISO | 2 | 1 |

**By new action**

| New action | Rows |
|---|---|
| `MARK_AS_OVER_ANNOTATED` | 17 |
| `KEEP_AS_NON_CORE` | 15 |
| `MODIFY` | 2 |
| `ACCEPT` | 2 |
| `TOO_GENERAL` | 1 |
| `UNDECIDED` | 1 |

**What was wrong with the 38 rows**

| Pattern | Rows | What was done |
|---|---|---|
| The same term treated differently on another row of the review | 14 | Action of the sibling row |
| A location from an organelle or membrane proteome or screen, removed as probable contamination | 12 | `KEEP_AS_NON_CORE` (11), `MARK_AS_OVER_ANNOTATED` (1) |
| The row's own paper or curated record supports the claim | 4 | `KEEP_AS_NON_CORE` |
| Identical protein binding removed as uninformative, where the contact may be indirect | 4 | `MARK_AS_OVER_ANNOTATED` |
| Ancestor of a kept term | 1 | `TOO_GENERAL` |
| A real observation in a term that names more than was shown | 1 | `MARK_AS_OVER_ANNOTATED` |
| The gene product represses the process | 1 | `MODIFY` to the fitting term |
| The paper behind the row could not be examined | 1 | `UNDECIDED` |

## Rows changed

Every row is in the row-level record with its index. Gene symbols link to the
reviews.

### Same term on another row of the review (14)

| Review | Term (rows) | Evidence | Now | Basis |
|---|---|---|---|---|
| ACO2 | cytosol (3) | RCA | `MARK_AS_OVER_ANNOTATED` | Marked on the IBA row. The pathway-default compartment adds no evidence, and the cytosolic pool of yeast aconitase is that of Aco1p. |
| THI3 | cytosol (1) | RCA | `MARK_AS_OVER_ANNOTATED` | Marked on the IBA row. The row places in the cytosol a decarboxylation that Thi3p does not catalyse. |
| GCY1 | arabinose catabolic process; D-xylose catabolic process (2) | IEA | `MARK_AS_OVER_ANNOTATED` | Marked on the direct-assay rows: reduction of a pentose by a promiscuous reductase is not catabolism of the sugar. |
| HXK1, HXK2 | D-glucose import across plasma membrane; fructose import across plasma membrane (4) | IEA | `MARK_AS_OVER_ANNOTATED` | Marked on the genetic-interaction rows: low-Km uptake depends on the kinases, which do not transport the sugar. |
| MET8 | protoporphyrin ferrochelatase activity (1) | IEA | `MODIFY` → sirohydrochlorin ferrochelatase activity | Redirected on the direct-assay row; the mapping has the right kind of enzyme and the wrong substrate. |
| LRO1 | phospholipid:diacylglycerol acyltransferase activity (1) | ISO | `ACCEPT` | Accepted on seven rows. The transfer names mouse LCAT, which does not have the activity (source defect). |
| TOM22 | protein transmembrane transporter activity (1) | IBA | `ACCEPT` | Accepted on the mutant-phenotype row with the same `contributes_to` qualifier. The PAINT node no longer carries the term, which the propagation review records. |
| SIR3 | DNA replication origin binding (1) | IBA | `MARK_AS_OVER_ANNOTATED` | Marked on the direct-assay row (see "Other changes"). |

### Organelle and membrane proteome hits (12)

Rule 2 of the [organelle policy](../ORGANELLES.md) keeps a location that a
direct assay observed: the row says what the experiment showed. These rows
had been removed as probable contamination, with no study that refutes the
detection. Eleven are now kept as non-core, because the location is
peripheral to what is known of the protein. The twelfth, a hit for San1 in a
screen with over-produced proteins, is marked as an over-annotation, since
over-production can mislocalise a protein. Of the 489 high-throughput
`mitochondrion` rows in yeast reviews, 431 are accepted or kept and 46 are
marked; the nine below were the only ones removed.

| Review | Term (rows) | Evidence | Now | Source |
|---|---|---|---|---|
| ATG7, CHD1, ESP1, SIR3 | mitochondrion (8) | HDA | `KEEP_AS_NON_CORE` | Two proteomes of purified mitochondria (PMID:14576278, PMID:16823961). |
| YPT7 | mitochondrion (1) | HDA | `KEEP_AS_NON_CORE` | Quantitative mitochondrial proteome (PMID:24769239). Ypt7 is at the contact site between vacuole and mitochondrion, which the review keeps. |
| YPT7, GSF2 | mitochondrial outer membrane (2) | HDA | `KEEP_AS_NON_CORE` | Proteome of outer membrane vesicles from mitochondria that were free of ER markers (PMID:16407407). The authors count Ypt7 among the GTP-binding proteins of the outer membrane; Gsf2 is otherwise known as an ER membrane protein. |
| SAN1 | peroxisome (1) | HDA | `MARK_AS_OVER_ANNOTATED` | Screen with over-produced proteins (PMID:35563734). San1 is a nuclear ubiquitin ligase. |

### The row's own paper or record supports the claim (4)

| Review | Term | Evidence | Now | What the source says |
|---|---|---|---|---|
| DEG1 | mitochondrion | IMP | `KEEP_AS_NON_CORE` | Mitochondrial tRNAs of the disrupted strain lack pseudouridine 38 and 39, and the authors conclude a common origin of the activity in both compartments (PMID:9430663). The row had been removed because the protein was seen only in nucleus and cytoplasm. |
| RPD3 | cytoplasm | IEA | `KEEP_AS_NON_CORE` | The UniProt location is tied to the genome-wide GFP study. The row had been called an artefact of automatic annotation. |
| RPD3 | nucleosome assembly | NAS | `KEEP_AS_NON_CORE` | The paper reports a chaperone function of the Rpd3 core complex that promotes histone deposition onto DNA (PMID:22177115). |
| RPD3 | response to oxidative stress | NAS | `KEEP_AS_NON_CORE` | Cells that lack Rpd3 are resistant to hydrogen peroxide, and Snt2 and Ecm5 recruit Rpd3 to promoters (PMID:23878396). |

### Identical protein binding (4)

The protein-binding policy removes bare `protein binding` only, and the term
asserts no more than a self-interaction; the rows are marked, not kept,
because the recorded contact may be indirect. Yeast reviews
keep or accept 97 of 118 `identical protein binding` rows with physical
interaction evidence; six had been removed "like protein binding".

| Review | Rows | Now | Basis |
|---|---|---|---|
| FUS3 | 2 (IPI) | `MARK_AS_OVER_ANNOTATED` | A two-hybrid self-interaction, which endogenous Ste5 can bridge, and an interaction record from a study of autophosphorylation; no direct assay of a Fus3 homodimer. |
| SPT16 | 2 (IPI, retired) | `MARK_AS_OVER_ANNOTATED` | Recovered with itself in two interactome studies, where shared chromatin or partners can bring two copies down together; the functional form is the Spt16-Pob3 heterodimer. |

The two SWI4 rows stay REMOVE: the cited paper shows that full-length Swi4 is
monomeric and that the fragment contact is intramolecular.

### Other changes (4)

| Review | Term | Evidence | Now | Basis |
|---|---|---|---|---|
| MDH2 | intracellular organelle lumen | IEA | `TOO_GENERAL` | Entailed by nuclear periphery, which the review keeps as a non-core location; the term names no organelle. `MARK_AS_OVER_ANNOTATED` is the near alternative, since the entailing row is a hit of a localisation screen under stress. |
| SIR3 | DNA replication origin binding | IDA | `MARK_AS_OVER_ANNOTATED` | Sir3 was detected at replication origins by chromatin immunoprecipitation, on the adjacent nucleosomes (PMID:29795547). The association is real; binding of origin DNA is the work of ORC. |
| SIR4 | DNA-templated transcription | IEA | `MODIFY` → heterochromatin formation | Sir4 silences transcription and takes no part in it. The same keyword row is redirected in the reviews of Sir3, Hst2 and Hst3. |
| EPS1 | protein-disulfide reductase (glutathione) activity | IDA | `UNDECIDED` | The abstract reports undetectable oxidative refolding activity, a different assay from the one the term names; the full text could not be obtained. |

## REMOVE rows kept, with a corrected record (5)

| Review | Row | What changed |
|---|---|---|
| ARO7 | nucleus (IDA) | Reason written. Source defect `WRONG_TERM`: the cited paper shows the functional fusion protein exclusively in the cytoplasm. |
| COX17 | protein farnesylation (IDA) | Source defect `WRONG_GENE_PRODUCT`: the paper is on COX10 and was published two years before COX17 was cloned. |
| MBP1 | maintenance of translational fidelity (IMP) | Source defect `WRONG_GENE_PRODUCT`: the paper is about MBF1. |
| SAS3 | subtelomeric heterochromatin formation (IMP) | Source defect `WRONG_GENE_PRODUCT`: the paper has no sas3 mutant, and the phenotypes are those of SAS2 mutants. |
| ERG10 | vacuole (NAS) | Reason written: the removal rests on the primary localisation data, not on the absence of a sentence in the cached article. |

## Source defects

| Review | Defect | Resource | Confidence | Depth |
|---|---|---|---|---|
| MBP1 | `WRONG_GENE_PRODUCT`: MBF1 mis-keyed as MBP1 | SGD | CONFIRMED | Full text; SGD made the same row on the same day for the two partners of Mbf1 that the paper studies. |
| COX17 | `WRONG_GENE_PRODUCT`: yeast COX10 recorded under the accession of COX17 | MGI | CONFIRMED | Title, abstract and annotation records; the paper predates the cloning of COX17. |
| ARO7 | `WRONG_TERM`: nucleus from a paper that shows cytoplasm | UniProt | CONFIRMED | Full text. |
| LRO1 | `WRONG_WITH_FROM`: mouse LCAT as the source of a PDAT transfer | CACAO | PROBABLE | Abstract, UniProt and QuickGO records. |
| SAS3 | `WRONG_GENE_PRODUCT`: two mutant-phenotype rows of SAS2 keyed to SAS3 | SGD | CONFIRMED | Full text, read on the PMC page of the article (not in the cache), and annotation records. |

## Protein binding audit

The 2,440 bare `protein binding` REMOVE rows (347 reviews) are all `IPI`
rows and none is negated; 325 are retired. Two text screens looked for rows
that are not what the policy covers. They flagged 35 rows whose text has words
such as "non-specific" or "spurious" and 18 rows whose text names a GO term
that the review does not assert. The distinct cases were read: the texts call
the term non-specific, not the interaction, and the GO terms are complex
terms or terms the text argues against. No action changed. 261 rows have no
`reason`; each has a summary, and the policy is the reason.

## What REMOVE means in the yeast set now

The 590 substantive rows that stand:

- **Errors of the YeastPathways conversion** (323 rows): the cytosol as default
  compartment, superpathway terms, reactions and catalysts that do not fit
  the enzyme.
- **Phylogenetic rows with a ground specific to the target** (119 rows):
  compartment-specific and substrate-specific paralogs (Idp1, Idp2 and Idp3;
  Odc1 and Odc2; Spe3 and Spe4), pseudoenzymes (Kdx1, Dug2, Thi3, Oca6), and
  functions of a branch the target does not belong to (Acl4, Cdc4, Yar1).
- **Wrong electronic mappings** (88 rows of `IEA`, `ISS` and `ISA`): a term for
  another substrate or cofactor, an activity of a domain the protein lacks, an
  inference from a row that is itself removed.
- **Experimental rows that are contradicted** (31 rows): by their own paper
  (Pfk1 ribosome binding, Nte1 lipid droplet, Swi4 self-binding), by later
  work on the same protein (Kgd4 as a ribosomal protein, Coq8 as a protein
  kinase, Mmm1 in the outer membrane), or because the row is on the wrong
  gene (Mbp1, Cox17).
- **Statements of a source that the biology contradicts** (15 rows): Reactome
  import intermediates recorded as locations of matrix proteins, and the
  vacuole and mitochondrion statements of one review article on the
  ergosterol pathway.
- **No-data rows that literature has overtaken** (14 rows).

The row-level record lists 16 notes on rows that stand, several of which
cover more than one row; five are marked as close calls.

## Follow-ups

- **ERG19 and MVD1 are two folders for one protein** (P32377), and they
  disagree: the vacuole statement of the ergosterol review article is marked
  in one and removed in the other. One folder should be retired.
- **The same statement, two actions.** The location statements of that review
  article (PMID:28904410) are REMOVE in the reviews of ERG8, ERG10, ERG13 and
  MVD1 and `MARK_AS_OVER_ANNOTATED` in those of ERG19, ERG20 and IDI1.
- **Rows kept beside the ones settled here.** ARO7 nucleus from the GFP screen
  (marked, although the targeted study found the protein exclusively in the
  cytoplasm); the second rows from the mis-keyed papers on SAS3 and COX17,
  which the reviews keep because the claims are true on other evidence; the
  IBA cytosol rows of ACO2 and THI3, with which the pathway-derived rows were
  harmonised.
- **Marked rows that might be removed instead.** The sugar import rows of
  HXK1 and HXK2 and the pentose catabolism rows of GCY1 were harmonised with
  experimental rows that the reviews mark. The reasons describe a failure of
  participation, so removal of all rows for these claims would also be
  defensible, and the experimental rows may be the ones in the wrong tier.
- **Marked proteome rows elsewhere.** 46 high-throughput mitochondrion rows in
  other yeast reviews are marked as over-annotations. Under rule 2 of the
  organelle policy they would be kept as non-core, as the proteome rows
  changed here now are. They were not REMOVE rows and were not touched.
- **A transfer of rows that changed here.** A sweep over every changed row
  looked for rows in other reviews that name the yeast protein as their
  source. One differs from its changed source: the Candida review
  CANAL/CEK2 removes a transfer of the Fus3 self-interaction, which is now
  marked. That removal is defensible as it stands, because a transfer to
  another species has no observation behind it.
- **Full text needed.** PMID:16002399 (EPS1).
- **Source defects beyond this pass.** The errors of the YeastPathways
  conversion are described in the project page and not recorded row by row.
  Other REMOVE rows describe an error in a source record without a structured
  defect, for example HAP4 (a transcription factor as part of the respiratory
  chain complex, CACAO), HMG2 (a degradation substrate as part of the
  proteasome complex, SGD) and the three CAF-1 subunits (part of the
  nucleosome, Complex Portal).
- **Other organisms.** The worm, fly, fission yeast and other reviews were not
  touched.
