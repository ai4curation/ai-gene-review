# Pseudomonas pyoverdine periplasmic maturation — module notes

Working notes for `modules/pseudomonas_pyoverdine_periplasmic_maturation.yaml`. These record
what was searched and what the searches did and did not turn up, so that the module's four
knowledge gaps can be read as findings rather than as unexamined blanks. This is not a
deep-research file: no provider was run, and nothing here should be cited as one.

## Why the module exists

The sibling module `pseudomonas_pyoverdine_precursor_supply` is COMPLETE and explicitly scopes
out everything downstream of the two amino-acid precursor reactions — assembly, export,
periplasmic maturation, secretion, uptake. `bacterial_tonb_siderophore_import` covers
ferripyoverdine re-entry and scopes out biosynthesis. Nothing covered the periplasmic segment,
and no module covers NRPS assembly, so the two existing pyoverdine modules do not meet.

## What was searched, and what it produced

Sources in hand for this segment:

- `publications/PMID_24816606.md` — the PvdP tyrosinase paper (abstract only). Primary
  enzymology for part 1, and the source of the "small family of tyrosinases present in
  fluorescent pseudomonads" framing. **This is the only step in the module with primary
  enzymology.**
- `publications/PMID_30386787.md` — Ringel & Brüser 2018, *The biosynthesis of pyoverdines*
  (full text). A narrative review, and the source for everything in parts 2 and 3. It is where
  the oxidation steps get partitioned between PvdP and PvdO, where the pvdMNO in-frame deletion
  results are reported, and where the PvdN/PtaA branch is described.
- `publications/PMID_19787431.md`, `publications/PMID_16621825.md` — the periplasmic maturation
  and Tat-dependence papers (abstracts). Compartment evidence.
- `publications/PMID_12686626.md` — the pvd mutagenesis survey (abstract).
- UniProt records for Q9I188 (PvdP), Q9I185 (PvdO), G3XCY5 (PvdN), fetched for the gene reviews.
- `projects/REFSEQ_GO/results/PSEPK/ncbi_proteins.tsv` — NCBIfam product names for NF051454,
  NF051459 and NF051467.

Searched for and **not** found:

- **A primary paper for PtaA.** The review cites one (its ref 74) and names the enzyme, but it
  is not cached here and could not be read. A UniProt query for `gene:ptaA` in *Pseudomonas*
  returns only unreviewed TrEMBL entries whose protein names are machine-generated
  ("Pyoverdine biosynthesis transaminase PtaA (EC 2.6.1.-)"), from *P. pharyngis*,
  *P. paraglycinae* and *P. alloputida* — none of them the characterised protein. This is why
  the PtaA variant carries `preferred_term` and a description but no `term` and no
  `representative_members`: naming one of those accessions as the exemplar would be a guess.
  Grounding this variant is the single most useful thing a reader with the primary paper could
  add.
- **A primary paper for the pvdMNO in-frame deletions** in *P. fluorescens* A506 (the review's
  ref 71). Parts 2 and 3 therefore rest on a review's account of someone else's experiment,
  which is the main reason the module is DRAFT rather than COMPLETE.
- **Any assay of PvdO.** The review states that protein purified from a heterologous host had
  no detectable cofactor and was inactive. Nothing contradicts that, and nothing supersedes it.
- **A GO term for either of the two unnamed reactions.** Checked for the second chromophore
  oxidation and for the PLP-dependent decarboxylation that retains the α-amino group; neither
  exists. `GO:0016491` oxidoreductase activity is not used for PvdO — see below.
- **A reaction for PvdM.** None. This is the sharpest gap in the module: the review reports
  PvdM as the only essential gene of the pvdMNO operon, and gives it no function. The step the
  pathway cannot do without is the one step that cannot be modelled, which is why PvdM appears
  in the operon context but is not a part.

## Decisions worth recording

**Part 3 is optional; its variant set is one-or-both.** These are two separate questions and the
first draft of the module conflated them. `selection: ONE_OR_MORE` on a non-optional part
compiles to a hard requirement (`module_logic.py`: a part is an AND child unless `optional` is
set, and only `ZERO_OR_MORE` admits an empty branch), so a strain carrying neither tailoring
enzyme would have been reported unsatisfied — contradicting the module's own note, and the
review's report that removing both leaves the glutamate unaltered. Fixed by marking the part
optional and keeping the set at ONE_OR_MORE.

**PvdO gets no function term, and not `GO:0016491` either.** The temptation is real: NCBIfam
names the model's product "dihydropyoverdine dehydrogenase", which is a reaction-type name that
matches the step. But a family product name is a curated prediction, and the one measurement
anyone has reported on this protein found it inactive and without a cofactor. Asserting a
catalytic term would assert exactly what the assay failed to show. The annoton is written as an
oxidation factor instead, with substrates and products named because the transformation is
established, and the hedge in `role_description`. The schema has no "required for" relation for
an annoton, so prose is as far as this can be taken.

**The second connection carries no `connection_type`, only `chaining_status: NOT_APPLICABLE`.**
Neither relation a `connection_type` could assert holds. PvdO's product is not the tailoring
step's substrate — the tailoring acts on the position-1 glutamate, not on the chromophore —
which is what `NOT_APPLICABLE` records. And the order is not established either, since PvdN
accepts ferribactin, which sits upstream of PvdP, so the tailoring step may precede the
oxidations rather than follow them.

This took two attempts. The first version used `PRECEDES`, whose enum definition is "the source
occurs before the target" — precisely the claim the connection's own description withdrew. That
is the same defect as the part-optionality one above: a machine-readable field asserting what
the prose beside it denies, and I introduced it while fixing the first instance. The enum has no
member meaning "adjacent in the pathway, order not established", and `connection_type` is
optional, so the honest encoding is to assert neither relation. Worth noting as a pattern: when
no enum member fits, the temptation is to pick the nearest one and qualify it in prose, and a
reader of the data never sees the qualification.

The unordered edge is also a positive finding, not a shrug. The review devotes a section to it —
"Reactions of periplasmic pyoverdine biogenesis may not occur in a strict order" — and closes by
saying there is no evidence for any channeling that could impose one. Both sentences are now
quoted on the connection.

## A third pattern: encode the warrant, not just the conclusion

Round 3 of review found that `optional: true` and `selection: ONE_OR_MORE` were argued only in
this notes file and in the YAML's free-text `notes`, with no `evidence` item on either the part
or the variant set — even though `ModulePart` and `ModuleVariantSet` both have an `evidence`
slot and `modules/` uses part-level evidence over 300 times. Worse, the sentence that licenses
`optional: true` states the case outright ("Removal of both tailoring enzymes leaves the
original glutamate unaltered") and was quoted nowhere, so what the file argued from instead was
the *single*-enzyme deletion, making an inference the review renders unnecessary.

That is the same shape as the round-1 quote finding: a weaker sentence cited while the direct
one sits in the same paper. Three rounds, three variants of one mistake — the structural
decision was right every time, and every time the machine-readable justification for it was
thinner than the prose beside it. The rule to carry forward: when a structural slot is set
because of something a source says, quote that sentence in the slot's own `evidence`, not in a
note nearby.

A fourth instance turned up in the same round and is worth recording because it is the cheapest
kind to miss. The PvdO annoton was `id: pvdo_chromophore_oxidase` while its label said
"oxidation factor" and the module asserts no molecular function for it — an identifier naming an
enzyme class the module declines to claim. Renamed to `pvdo_chromophore_oxidation_factor`;
nothing outside this file referenced the old id. Identifiers are machine-readable fields too,
and this one had been contradicting the prose beside it since the module was written, through
three rounds of review of exactly that pattern.

## Open questions for a reader with more sources

1. Ground the PtaA variant from the primary paper (the review's ref 74).
2. Read the A506 in-frame deletion paper (ref 71) and promote parts 2 and 3 off review-only
   evidence, which would be most of what DRAFT is recording.
3. Is PvdM's reaction known anywhere? If so the module gains its missing middle.
4. What accepts the electrons from the two oxidations? The review says the electron transport
   pathways have not been clarified; the one lead is that adding cysteine to a growing *ccmC*
   mutant culture produced ferribactin.
