---
title: "Mouse and Rat Genes Re-Review: REMOVE actions"
species: [mouse, rat]
autolink_exclude: [III, old, HSP60, SIR2]
---

# Re-review of REMOVE actions in mouse and rat gene reviews

Back to the [project page](../MOUSE_GENES_RE_REVIEW.md). This is the mouse and
rat counterpart of the
[human REMOVE re-review](../HUMAN_GENES_RE_REVIEW/REMOVE_RE_REVIEW.md), tracked in
[#4097](https://github.com/ai4curation/ai-gene-review/issues/4097).

**Bottom line:** every annotation row with `action: REMOVE` in `genes/mouse`
and `genes/rat` was read again against the current review rules (14 November
2026, at commit `70e3fa209` of main). There were 1,098 such rows in the 452 review files (232 mouse, 220
rat). 629 are bare `protein binding` rows, which the protein-binding policy
removes as uninformative; they were audited by script and none changed
action. The other 469 rows, in 163 reviews, were read one at a time.
**110 of them (23%) no longer say REMOVE**, 359 stand, and 16 errors in
source records were written down as structured `source_defects`. 48 review
files were edited (36 mouse, 12 rat). No row was changed to REMOVE.

The row-level record is in
[`remove_rereview_changes.yaml`](remove_rereview_changes.yaml): every changed
row with its old and new action and the rule applied, the REMOVE rows that
were examined closely and kept, and the rows outside this pass that it shows
to need another look.

## Why this pass

The human pass found that about a quarter of REMOVE rows removed a claim that
was true, kept elsewhere in the same review, or supported by an experiment
that the reviewer had not looked at. The same rules apply to mouse and rat
reviews, and two things make these reviews different:

- **Most rows are transfers.** A mouse or rat annotation is often an
  orthology transfer (ISO, IEA from Ensembl Compara, ISS) of an experimental
  annotation on the human or the other rodent protein. A transfer was often
  removed as "electronic" or "unsupported in mouse" without a look at the
  experiment behind it.
- **The donor often has its own review.** Where the human or the other rodent
  review keeps the source row, removing the transfer makes the two reviews
  disagree about one claim.

## Method

- **Triage by script.** For every REMOVE row the triage recorded the other
  rows of the same term in the review, kept terms below it in the ontology,
  the WITH/FROM donor, the donor's current annotations in QuickGO, and what
  the review of the human ortholog does with the same term.
- **Rows read one at a time**, by category: same term kept in the review,
  ancestor of a kept term, no-data rows, root organelle rows, rows whose human
  counterpart is kept, experimental rows, and transfers with an experimental
  donor.
- **Donor papers checked.** Where a transfer had been removed with no ground
  specific to the term, the abstract of the donor paper was read; 13 papers
  were added to `publications/` so that the new reasons can quote them.
- **Rules as in the human pass**, with one addition (below). A REMOVE that
  rests on a biological argument was left alone, also where another action
  would have been defensible.
- **Main was merged before the edits were applied**, so the pass covers the six
  reviews added after the triage (13 further REMOVE rows) and leaves out one
  row that another change had already settled.

### The added rule: a transfer is judged like its source row

If the review of the donor ortholog keeps the source annotation (as core,
non-core, an over-annotation or a redirected term), the transfer takes the
same action unless something specific to the target argues otherwise.
Target-specific arguments were respected: the IL-8 gene is absent from mouse,
angiogenin-related protein is a non-angiogenic paralog of angiogenin, the
CXCR3-B isoform has no mouse counterpart, and mouse knockout data show that
the effect of Hsp60 does not depend on MyD88.

## Results

| | Mouse | Rat | Total |
|---|---|---|---|
| Review files | 232 | 220 | 452 |
| REMOVE rows at start | 759 | 339 | 1,098 |
| Bare protein binding (unchanged) | 431 | 198 | 629 |
| Substantive rows read | 328 | 141 | 469 |
| Reviews with substantive rows | 96 | 67 | 163 |
| Rows that no longer say REMOVE | 84 | 26 | 110 |
| REMOVE rows at end | 675 | 313 | 988 |
| Review files edited | 36 | 12 | 48 |

**Retired rows.** 27 of the REMOVE rows, all in rat reviews, are marked
`retired`: GOA no longer carries the annotation, and the review keeps the row
as a record. They were read like the others and are included in the counts.
Twelve are substantive rows, and eleven of those changed, all in rat/Prkaa2.

| New action | Mouse | Rat | Total |
|---|---|---|---|
| `MARK_AS_OVER_ANNOTATED` | 32 | 8 | 40 |
| `KEEP_AS_NON_CORE` | 32 | 0 | 32 |
| `MODIFY` | 6 | 14 | 20 |
| `ACCEPT` | 4 | 3 | 7 |
| `UNDECIDED` | 7 | 0 | 7 |
| `TOO_GENERAL` | 3 | 1 | 4 |

What was wrong with the 110 rows:

| Pattern | Rows | What was done |
|---|---|---|
| A transfer removed although its source row is kept in the donor's review | 31 | Same action as the source row |
| A transfer removed although the donor experiment shows the claim | 6 | `KEEP_AS_NON_CORE` |
| A transfer of a real observation that is over-read, or of unknown relevance for the target | 17 | `MARK_AS_OVER_ANNOTATED` |
| The same term treated differently on another row of the review | 19 | Action of the sibling row |
| The gene product regulates the process, or the sign or substrate class is wrong | 12 | `MODIFY` to the fitting term |
| An experimental row that records a real observation as participation in a process | 14 | `MARK_AS_OVER_ANNOTATED` |
| Ancestor of a kept term | 4 | `TOO_GENERAL` |
| The reason conceded that the claim is true | 2 | Kept or refined |
| A no-data row removed because inferred rows cover the aspect | 2 | `ACCEPT` |
| The paper behind the row, or behind its source row, could not be examined | 3 | `UNDECIDED` |

## Rows changed

Evidence codes are those of the rows; where a term has several rows they are
listed together. The reason of every row states the basis in full.

### Transfers judged like their source row (31)

| Review | Term (rows) | Evidence | Now | Basis |
|---|---|---|---|---|
| mouse/Ctnnb1 | epidermal growth factor receptor signaling pathway (2) | IEA, ISO | `KEEP_AS_NON_CORE` | Human CTNNB1 keeps the direct-assay row: EGF releases beta-catenin from adherens junctions and sends it to the nucleus (PMID:18356165). |
| mouse/Ctnnb1 | cellular response to indole-3-methanol (3) | IEA, ISO, ISS | `MARK_AS_OVER_ANNOTATED` | Human CTNNB1 marks the direct-assay row: indole-3-carbinol raised the abundance of the catenins, an expression change. |
| mouse/Hsp90aa1 | UTP, CTP, GTP and dATP binding (8) | IEA, ISO | `KEEP_AS_NON_CORE` | Human HSP90AA1 keeps them: Hsp90 has a second, unspecific nucleotide-binding site at the C-terminus (PMID:12755697). |
| mouse/Notch1 | acrosomal vesicle (2) | IEA, ISO | `KEEP_AS_NON_CORE` | Rat donor: Notch 1 was seen by electron microscopy in the acrosome of elongated spermatids (PMID:11700865); human NOTCH1 keeps the term. |
| mouse/Pias1 | protein domain specific binding (2) | IEA, ISO | `KEEP_AS_NON_CORE` | Human PIAS1 keeps it; UniProt records a domain-mapped interaction of mouse PIAS1 with MSX1. |
| mouse/Tert | template-free RNA nucleotidyltransferase activity (2) | IEA, ISO | `KEEP_AS_NON_CORE` | The human review (human/TERT) keeps the direct-assay row for this non-canonical activity (PMID:19701182). |
| mouse/Tnfrsf1a | cell surface receptor signaling pathway via JAK-STAT (2) | IEA, ISO | `KEEP_AS_NON_CORE` | The human review (human/TNFRSF1A) keeps the row: Jak1/2 signalling was inhibited by an antibody against TNFR1 (PMID:21410936). |
| mouse/Trp53 | ATP-dependent DNA/DNA annealing activity (2) | IEA, ISS | `KEEP_AS_NON_CORE` | Human TP53 accepts the direct-assay row: p53 directs DNA strand reassociation (PMID:8183576). |
| mouse/Ghr | receptor internalization; regulation of response to nutrient levels; neuronal cell body (3) | ISO | `KEEP_AS_NON_CORE` | The rat review keeps all three, two of them on experimental rat rows (PMID:17258692); UniProt states that mouse GHR is internalized on hormone binding. |
| mouse/Pax6 | blood vessel development (2) | IEA, ISO | `MARK_AS_OVER_ANNOTATED` | Human PAX6 marks the mutant-phenotype row: vascular findings follow from eye malformation. |
| mouse/Myc | identical protein binding (1) | ISO | `MARK_AS_OVER_ANNOTATED` | Human MYC marks both source rows: self-association is observed, but no function is assigned to a MYC homodimer. |
| mouse/Txn1 | protein-disulfide reductase [NAD(P)H] activity (1) | IEA | `MODIFY` → protein-disulfide reductase activity | As in human TXN: thioredoxin reductase, not thioredoxin, uses NADPH. |
| mouse/Cftr | isomerase activity (1) | IEA | `MODIFY` → ATP hydrolysis activity | As in human CFTR: the keyword follows from EC 5.6.1.6, and the measured activity is ATP hydrolysis. |

### Transfers whose donor experiment shows the claim (6)

| Review | Term (rows) | Evidence | Now | Basis |
|---|---|---|---|---|
| mouse/Agtr1a | D1 dopamine receptor binding (2) | IEA, ISO | `KEEP_AS_NON_CORE` | Rat donor: AT1 and D1 receptors form heterodimers (PMID:22193384). |
| mouse/Cyp1a1 | positive regulation of G1/S transition of mitotic cell cycle (2) | IEA, ISO | `KEEP_AS_NON_CORE` | Rat donor: P4501A1 promotes G1 progression by removing the agonist of the aryl hydrocarbon receptor (PMID:14742689). |
| mouse/Sox2 | nitric-oxide synthase binding (1) | ISO | `KEEP_AS_NON_CORE` | Rat donor: a specific interaction of nNOS and Sox2 in neurons (PMID:26607632). |
| mouse/Tnfrsf1a | axon (1) | ISO | `KEEP_AS_NON_CORE` | Rat donor: TNF receptors co-localised with a TNF-alpha tracer along the sciatic nerve (PMID:11240015). |

### Transfers of a real observation, marked instead of removed (17)

| Review | Term (rows) | Evidence | Basis |
|---|---|---|---|
| mouse/Agtr1a | organelle outer membrane (2) | IEA, ISO | Rat donor: intracellular immunogold label in dendrites (PMID:15590154); receptor in transit, and the term names no organelle. |
| mouse/Agtr1a | dopamine biosynthetic process (2) | IEA, ISO | Rat donor: an AT1 antagonist lowered dopamine synthesis (PMID:20097214); the receptor influences the pathway and performs no step of it. |
| mouse/Agtr1a | symbiont entry into host cell (1) | ISO | Human donor: a complex of soluble ACE2 and the SARS-CoV-2 spike protein entered cells through AT1 receptors (PMID:33713620); not tested for the mouse receptor. |
| mouse/Cyp1a1 | porphyrin-containing compound metabolic process (2) | IEA, ISO | Rat donor: oxidation of bilirubin and uroporphyrinogen in vitro, only with polyhalogenated biphenyls added (PMID:12907239). |
| mouse/Epo | cell surface (2) | IEA, ISO | Human donor: erythropoietin binds to erythrocytes (PMID:14569084); the hormone at its receptor, not a location of the secreted protein. |
| mouse/Fmo3 | amino acid binding (1) | ISO | Rat donor: seleno-L-methionine is a substrate of FMO3 (PMID:17173378); substrate binding is implied by the activity. |
| mouse/Ghr | lipid binding; insulin-like growth factor receptor signaling pathway (2) | ISO | Human donors: lipid binding by the isolated intracellular domain in vitro (PMID:25846210); GHR acts upstream of IGF-1 receptor signalling (PMID:7565946). As in the rat review. |
| mouse/Ifi204 | nuclear speck (1) | ISO | Human IFI16 accepts the source row; whether the location carries over to p204 is not shown. |
| mouse/Mtor | protein tyrosine kinase activity; non-membrane spanning protein tyrosine kinase activity (4) | IEA, ISO, ISS | Human donor: tyrosine kinase activity of mTOR measured directly in one study (PMID:26584640); UniProt records it as something mTOR may do. |

### Same term on another row of the review (19)

| Review | Term (rows) | Evidence | Now | Basis |
|---|---|---|---|---|
| mouse/Ang2 | three immune response terms (3) | ISO | `KEEP_AS_NON_CORE` | Kept as non-core on the IBA rows. |
| mouse/Ang2 | defense response to Gram-positive bacterium (1) | ISO | `MARK_AS_OVER_ANNOTATED` | Marked on the IBA row. |
| mouse/Ccnb1 | nucleus (1) | ISO | `ACCEPT` | Accepted on the IBA and IEA rows; the row's reference could not be examined. |
| mouse/Cdk5r1 | cyclin-dependent protein serine/threonine kinase activator activity (1) | TAS | `ACCEPT` | Accepted on two other rows; the row's reference is a paper on Leishmania (source defect). |
| mouse/Pld4 | single-stranded DNA 5'-3' DNA exonuclease activity (1) | IMP | `ACCEPT` | Accepted on the IEA row; the row cites the wrong paper (source defect). |
| rat/Prkaa2 | protein serine kinase activity (1) | IEA | `ACCEPT` | Accepted on the experimental rows. |
| mouse/Abhd14b, rat/Abhd14b | protein-lysine-acetyltransferase activity (2) | IEA | `MODIFY` → acetyltransferase activity | Redirected on the ISS row; the Rhea mapping reads the reaction in the wrong direction. |
| mouse/Pcbd1, mouse/Pcbd2 | phenylalanine 4-monooxygenase activity (2) | IEA | `MODIFY` → 4-alpha-hydroxytetrahydrobiopterin dehydratase activity | Redirected on the direct-assay row. |
| rat/Pgam2 | ooplasm (1) | IEA | `MODIFY` → cytosol | Redirected on the direct-assay row. |
| mouse/Agtr1a | drinking behavior (2) | IEA, ISO | `UNDECIDED` | The experimental rows for the term are undecided. |
| mouse/Dnajb11 | nucleus; mRNA modification (2) | ISO | `UNDECIDED` | The experimental rows for the terms are undecided. |
| mouse/Agtr1a | inflammatory response (1) | IGI | `MARK_AS_OVER_ANNOTATED` | Marked on the IBA row; the row's own paper reports an effect that is independent of AT1 receptors (source defect). |
| mouse/Abi3 | defense response to tumor cell (1) | IDA | `MARK_AS_OVER_ANNOTATED` | Marked on the IEA and ISO rows; the experiment used human ABI3 (source defect already recorded). |

### Role, sign or substrate class corrected (12)

All in rat/Prkaa2, the catalytic subunit of AMPK. The review already
redirected its TORC1 signaling row to negative regulation of TORC1 signaling;
the other rows of the same kind had been removed, most of them without a
stated reason.

| Term (rows) | Evidence | `MODIFY` to |
|---|---|---|
| fatty acid biosynthetic process (1) | IEA | negative regulation of fatty acid biosynthetic process |
| cholesterol, sterol and steroid biosynthetic process (3) | IEA | negative regulation of cholesterol biosynthetic process |
| lipid biosynthetic process (3) | ISO, ISS | negative regulation of lipid biosynthetic process |
| autophagy (1) | IEA | positive regulation of autophagy |
| rhythmic process (1) | IEA | regulation of circadian rhythm |
| positive regulation of TORC1 signaling (1) | ISO | negative regulation of TORC1 signaling |
| protein serine/threonine/tyrosine kinase activity (2) | ISO | protein serine/threonine kinase activity |

### Experimental rows that record a real observation (14)

All are now `MARK_AS_OVER_ANNOTATED`. An experimental annotation that records
what was measured is not removed as false.

| Review | Term | Evidence | What was observed |
|---|---|---|---|
| rat/Arsb | response to pH | IDA | Dependence of enzyme activity on pH. |
| rat/Arsb | response to methylmercury | IDA | Inhibition of the enzyme by methylmercury. |
| rat/Sqle | response to biphenyl | IDA | Inhibition of the recombinant enzyme by biphenyl compounds. |
| rat/Slc10a1 | response to nutrient levels, to estrogen, to ethanol; cellular response to xenobiotic stimulus | IEP | Changes in Ntcp expression. |
| rat/Cfd | Notch signaling pathway | IMP | Changed adipsin expression after a gamma-secretase inhibitor. |
| mouse/Dnmt3a | cellular response to bisphenol A | IDA | Raised Dnmt3a mRNA after exposure. |
| mouse/Dnmt3a | post-embryonic development | IDA | Lethality after ectopic expression. |
| mouse/Dnmt3l | male meiosis I | IMP | Meiotic failure in cells that do not express Dnmt3L. |
| mouse/Gpam | positive regulation of multicellular organism growth | IMP | Lower body weight from reduced fat mass. |
| mouse/App | protein phosphorylation | IMP | Dephosphorylation of an NMDA receptor subunit downstream of amyloid-beta. |
| mouse/Mpo | mitochondrion | HDA | One hit in a mitochondrial proteome survey of vascularised tissues. |

### Other changes (11)

| Review | Term (rows) | Evidence | Now | Basis |
|---|---|---|---|---|
| mouse/Dll3 | negative regulation of neurogenesis (2) | IDA, IEA | `TOO_GENERAL` | Entailed by negative regulation of astrocyte differentiation, which the review keeps; the reading about neurons is contested (PMID:16144902). |
| mouse/Ghr | endocytosis (1) | IEA | `TOO_GENERAL` | Entailed by receptor internalization. |
| rat/Prkaa2 | steroid metabolic process (1) | IEA | `TOO_GENERAL` | Entailed by cholesterol metabolic process. |
| mouse/Dnajb11 | positive regulation of ATP-dependent activity (1) | ISO | `ACCEPT` | ERdj3 stimulates the ATPase activity of BiP; the row had been removed because a function term covers the same biology. |
| mouse/Ghr | growth factor binding (1) | ISO | `MODIFY` → peptide hormone binding | The receptor binds growth hormone; the review accepts the specific term. |
| rat/Actl7a, rat/Aph1a | biological_process (2) | ND | `ACCEPT`, `nd_case: INFERABLE` | No study of the rat protein identifies a process; the process rows are transfers from orthologs. |
| mouse/Trp53 | receptor tyrosine kinase binding; protein heterodimerization activity (2) | IEA | `UNDECIDED` | Transfers of human physical-interaction rows; the cached abstracts do not describe the interactions. |
| mouse/Hsp90aa1 | positive regulation of cytotoxic T cell differentiation (1) | TAS | `UNDECIDED` | An author statement may stand anywhere in the full text, so the row is not removed on the strength of the abstract, which speaks of the cytotoxic action of nitric oxide and not of T cells (suspected source defect). |

## REMOVE rows kept, with a corrected record (24)

| Review | Rows | What changed |
|---|---|---|
| mouse/Ang2 | 9 experimental rows from three papers on angiotensin II | Source defect `WRONG_GENE_PRODUCT`: MGI matched the symbol Ang2 to the peptide Ang II, a product of Agt. |
| mouse/Efr3a | 3 transfers from human corneodesmosin | Source defect `WRONG_GENE_PRODUCT`: the rows appear to belong to mouse Cdsn. |
| mouse/Mtor | 6 rows for RNA polymerase III promoter DNA binding | Reason rewritten: the donor is a chromatin immunoprecipitation result (PMID:20233713), and occupancy is not sequence-specific DNA binding. The rows had been called electronic mis-assignments. |
| rat/Casp3, rat/Ptk7 | 4 rows with no stated reason | Reason written. |
| mouse/Pax6 | nervous system process | Reason no longer says that the human review removes the term; it records it as too general. |
| rat/Pik3c2a | biological_process (ND) | `nd_case: STALE` recorded; a study in rat insulinoma cells identifies a process. |

## Source defects

16 were recorded, all on experimental or curator-made rows.

| Review | Rows | Defect | Resource | Confidence |
|---|---|---|---|---|
| mouse/Ang2 | 9 | `WRONG_GENE_PRODUCT` (Ang II is angiotensin II) | MGI | PROBABLE |
| mouse/Efr3a | 3 | `WRONG_GENE_PRODUCT` (donor is corneodesmosin) | MGI | PROBABLE |
| mouse/Cdk5r1 | 1 | `WRONG_REFERENCE` (a paper on Leishmania) | MGI | PROBABLE |
| mouse/Pld4 | 1 | `WRONG_REFERENCE` (PMID:22102906 for PMID:30111894) | UniProt | PROBABLE |
| mouse/Agtr1a | 1 | `MISSING_NEGATION` (the effect is independent of AT1 receptors) | MGI | SUSPECTED |
| mouse/Hsp90aa1 | 1 | `WRONG_TERM` (cytotoxic action of nitric oxide read as T cell differentiation) | UniProt | SUSPECTED |

## Protein binding audit

All 629 bare `protein binding` REMOVE rows (431 mouse, 198 rat) have a stated
reason and none is a negated row, so each conforms to the protein-binding
policy. None changed action.

## What REMOVE means in the mouse and rat sets now

The 359 substantive rows that stand rest on a biological argument. The common
ones:

- **A target-specific argument against a transfer:** a divergent paralog
  (mouse Ang2, 41 rows), a gene or isoform absent from the species, a
  pseudoenzyme that has lost the activity (Irak3, Ptk7, Lalba, Serpinh1).
- **The donor annotation is itself wrong:** the paper is about another gene
  product (the angiotensin II rows, Efr3a, one rat Tardbp row), or the full
  text contradicts the row.
- **The gene product is the substrate, the cargo or the target** of the
  process (Cdkn1b, Ctnnb1 and Ghr turnover, Npc1 glycosylation).
- **An expression pattern of a rodent ortholog projected as a function**
  (Ghsr, Pax4).
- **A wrong mapping:** a domain-based term on a protein that lacks the
  activity, an EC number of the wrong enzyme class, an obsolete term.

20 of the rows that stand are listed with a note in the row-level record;
eight of them are marked as close calls.

## Follow-ups

- **Human rows that this pass puts in question.** Eleven places where a
  mouse or rat review and the human review treat the same claim differently,
  often because the mouse or rat review holds an argument from the full text:
  PAX6, GRIA1, SLC16A1, TARDBP, ITPR1, VEGFA, SOX2, TP53, SERPINH1, NOTCH1 and
  PTK7. The row-level record lists each with the index and the argument. They
  were not changed here, because this pass covers mouse and rat REMOVE rows.
- **Rat rows kept beside the ones changed.** rat/Akt1 keeps translation on two
  experimental rows while the same review removes gene expression because a
  kinase performs no step of it. rat/Ghr keeps or marks three transfers whose
  human source rows are no longer in QuickGO.
- **Full text needed.** PMID:23027130 and PMID:10837489 (mouse Trp53),
  PMID:11584023 (mouse Dnajb11), PMID:12855682 (mouse Hsp90aa1) and
  PMID:12887892 (Sirt2).
- **Changes on main after the pass.** Before this pass was merged, main
  changed five of the rows it had left as REMOVE (mouse Lamp1, mouse and rat
  Map2k4, two rat Tardbp rows) and added 13 mouse and rat reviews. Those are
  not counted here.
- **Source defects beyond this pass.** Only the cases established here were
  structured; other REMOVE rows describe an error in a source record in their
  reason without a structured defect.

## Also changed with this pass

Three items carried over from the review of the follow-up to the human pass:

- **mouse/Sirt2:** the three transfers of negative regulation of striated
  muscle tissue development are `UNDECIDED`, like the human source row, which
  rests on a study of Sir2 that is probably about SIRT1.
- **Human SIRT2, cell differentiation:** `KEEP_AS_NON_CORE` with the reason
  "very broad term" becomes `MODIFY` to negative regulation of fat cell
  differentiation, which the review keeps on two rows.
- **Human SIRT2, protein binding:** a quote about p300 that did not bear on the
  row was dropped.
