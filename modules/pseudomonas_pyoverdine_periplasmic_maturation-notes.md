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

A fifth, with the polarity reversed, and in the field a reader sees first. The top-level
`description` said PvdO "carries out the second oxidation" — the single claim the rest of the
module is organised around declining. The part label says "PvdO-dependent", the annoton label
says "oxidation factor", `function` has no `term`, `role_description` says the catalyst question
is unsettled, gap 1 makes it a knowledge gap, and this file says asserting a catalytic term
would assert what the assay failed to show. The source says "the final oxidation depends on
PvdO" and never that PvdO performs it. So the description was stronger than the evidence, the
source, and five of the module's own fields.

The first four instances were machine-readable fields overstating what the prose hedged; this
one is prose overstating what the fields hedge. The "quote it in the slot's own evidence" rule
does not catch it, because a description has no slot to hold evidence. What catches it is
reading the description against the parts it summarises and asking whether any verb in it claims
more than the part does. Worth doing before publishing any module, since the description is what
gets read without the apparatus around it.

And the check has to be run over the whole sentence, not the clause that was flagged. The first
pass fixed the PvdO clause and left the next one standing — "a PLP-dependent tailoring enzyme
converts the glutamate side chain into one of the alternative mature forms" asserts
unconditionally the step the part marks `optional: true`, and "one of" understates a set encoded
`ONE_OR_MORE` whose source reports strains making the products of both branches. Two more
overstatements, in the same sentence, found in the same round. The lesson that generalises is
less about descriptions than about fixes: a flagged instance is a sample, so when a pattern is
named, re-read the whole field for it rather than patching the line quoted in the review.

## Ferribactin is the deacylated peptide

Worth stating because two slots in this file got it wrong in opposite directions from the rest.
The review's usage is consistent: the acylated species is always named "acylated ferribactin"
("The acylated ferribactin is exported most likely by PvdE into the periplasm, where it is
deacylated by the Ntn-type hydrolase PvdQ"), and bare **ferribactin is the deacylated peptide**,
which is what PvdP then acts on ("After ferribactin is deacylated, the fluorescent
dihydroxyquinoline ring system is generated"). The module agrees everywhere else — part 1's
substrate is plain `ferribactin`, and the scope line puts PvdQ-dependent deacylation *outside*
as upstream — so by its own boundary the ferribactin PvdP consumes is already deacylated.

Two places nonetheless called it "the undeacylated precursor", giving one molecule incompatible
acylation states inside one file. Both are fixed. The consequences differed, which is the part
worth keeping:

- On the connection, only the appositive was wrong. PvdN accepting ferribactin does place the
  tailoring upstream of the oxidations, because ferribactin is PvdP's substrate — and the review
  draws exactly that conclusion, that the ring system is not really relevant to the tailoring
  enzymes.
- On PvdN's `role_description`, the wrong appositive carried a wrong inference with it: "so this
  tailoring step is not strictly ordered after deacylation". If ferribactin is already
  deacylated, accepting it says nothing about ordering relative to deacylation. The claim was
  not merely imprecisely worded; it did not follow.

Unlike the five instances above, this is not a hedging failure — the statement was wrong rather
than overconfident, and no amount of qualifying it would have helped. The check that catches it
is different too: when the same entity appears in more than one slot, make sure the slots agree
about what it is. Here part 1's `substrates`, the scope line and two prose passages were
describing one molecule, and two of the four disagreed with the other two.

## A fix can overcorrect, and taking a reviewer's reading on trust is how

Round 5 suggested that the cyclisation is "promoted" rather than catalysed, since the review's
body text says PvdP catalyses the hydroxylation and oxidation and "thereby also promotes the
cyclization". I took it as a seventh instance of the overstatement pattern and reworded
accordingly — and wrote "The verbs are the review's", which was false. The pathway-figure legend
of the same paper says "PvdP catalyzes the oxidative cyclization". The review uses both verbs;
the original wording was supported by one of them, and my replacement asserted a
promotes-versus-catalyses distinction the paper does not maintain, attributed to the paper.

Two things to carry forward.

**Check the source yourself even when the reviewer quotes it.** The quoted sentence was real and
verbatim; what I did not do was look for the paper's *other* statements about the same step. Five
rounds of being right had made the reviewer's readings feel like findings rather than claims, and
this is the one round where deferring produced a worse file than ignoring would have.

**By then I was pattern-matching rather than reading.** "Unhedged verb, source hedges it" fit the
shape of five previous findings so well that I applied the fix without asking whether the source
was consistent. A named pattern makes the next instance cheaper to fix and easier to see where it
is not.

Even that was still taking a side. The right answer, which the next round supplied, is that the
**ring-closure mechanism is unsettled**: the review presents the oxidative cyclisation cascade as
a proposal and sets a postulated intramolecular Bucherer reaction beside it, noting that the
pseudoverdin observation it rests on came from an artificial system whose product did not work in
iron acquisition. If it is not known which chemistry closes the ring, it is not known whether
PvdP catalyses the closure — so the verb question was never answerable from the text, and picking
the weaker reading was the same mistake one notch quieter. Part 1 now asserts the hydroxylation
and the oxidation, says the closure is open in both directions, and the question is knowledge
gap 5, the only one touching the step the module calls solid.

The same figure legend also says "PvdO, possibly in conjunction with other proteins, facilitates
the final oxidation", which independently supports the PvdO hedging and is now quoted on gap 1.

### Quoting inside a free-text slot is worse than paraphrasing

The verb discrepancy ended up load-bearing in three places — an `evidence[].statement`, a
`role_description` and gap 5's `gap_statement` — and each stated it with the words in quotation
marks inside the free text. `validate-quotes` reads `supporting_text` and nothing else, so none
of it was checkable: quotation marks in a prose slot promise verification the tooling cannot
give. A paraphrase would at least have been honest about being a paraphrase. Both sentences are
now `supporting_text` on gap 5, which is where the rule two sections up already said they
belonged — the rule was written and then not applied to the next thing it covered.

### "Unsourced" is a claim about the tree, and the tree changes

Round 6 removed "a di-copper centre is the canonical tyrosinase active site" as general enzymology
rather than anything the sources state. The two premises were correct — the pathway review says
only "copper-containing", and `PMID_24816606.md` is abstract-only and never mentions copper — and
the conclusion was still wrong, because neither of us checked UniProt. `genes/PSEAE/pvdP/pvdP-uniprot.txt`
carries `DR   InterPro; IPR008922; Di-copper_centre_dom_sf.`, the SUPFAM equivalent, a 2.11 Å
structure `IN COMPLEX WITH CU(2+)`, and six Cu(2+) `FT BINDING` residues — three per copper, with
structure-derived `ECO:0007829` evidence, which CLAUDE.md lists as good support.

Two separate mistakes, worth keeping apart:

- **Checking two sources and concluding "unsourced".** The claim was about the whole available
  evidence; the check covered the review and one abstract. The record was never consulted.
- **Not revisiting after the tree changed.** At the time, pvdP's record was not on `main`, so it
  genuinely could not have been cited — the same constraint that deferred the PDB 5HHA citation.
  But 5HHA was *recorded as deferred* and came back when the sibling PR merged; the copper claim
  was deleted outright, so nothing brought it back. A deletion justified by what the tree contains
  should be recorded as conditional, the way a deferral is.

The restored version is stronger than the one deleted: the deleted sentence asserted a general
fact about tyrosinases, where the record shows two copper sites resolved **on this protein**.

### The narration rule needs re-checking after every commit, not once

`e5fc71b771` stripped review narration from the module and set the rule: an `evidence[].statement`
says what the source supports, a `description` describes the biology, the editorial trail lives
here. Review confirmed the file clean. Two commits later, six statements narrated the PR again —
"removed from the module in an earlier round", "the module previously reached this", "had rested
on PMID:24816606 alone". The first of them spent five of its seven lines on the editing history
of this PR and one on the source.

Why it recurred is worth naming: each instance arrives while *explaining a fix*, which is exactly
when the editing history is uppermost and feels like the relevant context. The rule is easy to
state, easy to verify once, and easy to break the next time there is something to explain. So it
belongs in the pre-push check alongside the quote run, not in the set of things considered settled.

And the correct home for all six already existed — this file carries every one of those points,
in fuller form, which is what makes their presence in the YAML redundant as well as wrong.

### The parallel-instance miss, three times

Round 4 named it: a flagged instance is a sample, so re-read the whole field. It has still
happened three more times, each in the commit that was applying the lesson elsewhere.

- Round 8: grounding PvdO's PANTHER rationale left PvdN's identical rationale in prose.
- Round 9: grounding PvdP's `NF051454` left PvdO's `NF051459` short-name claim in prose, and
  grounding PvdN's PANTHER line left its class-V fold description ungrounded.

All now cited. The pattern is specific enough to act on: when a fix grounds a claim for one
participant, the same claim shape almost certainly exists for the other two, because the three
parts were written in parallel from the same template. **Grep the sibling descriptors before
pushing the fix**, not after the next review.

### A deleted gloss can come back under its own replacement

Round 6 removed "a di-copper centre is the canonical tyrosinase active site" as the module's
enzymology rather than a source's. Round 9 restored the di-copper *domain* with real grounding —
and carried the word "canonical" back in with it, in two places. The grounding was new and
correct; the gloss on top of it was the same unsourced claim, re-entering under cover of the
fix that had been asked for.

Now stated as the module's own inference: the record has the di-copper centre domain, tyrosinase
active sites are built on one, and the connection between those two facts is the module's to own
rather than either record's to assert. Worth watching for generally — a restored claim arrives
with its old phrasing attached, and the phrasing may have been the part that was wrong.

### Attribute to the right structure within a deposition set

The restored copper claim said UniProt records the six Cu(2+) residues "from" the 2.11 Å
structure, and `role_description` said they were "resolved in" it. They are not. Every one of the
six `FT BINDING` lines carries `/evidence="ECO:0007829|PDB:6RRP, ECO:0007829|PDB:6RRQ"` — the
2.40 Å and 2.70 Å entries — and 6RRR, the 2.11 Å one, appears in no `FT` evidence at all. The
`RP` line reports the *best* resolution in a reference that covers all three, so quoting it and
then saying the residues come from it reads one structure's resolution onto another's evidence.

Nothing substantive turned on it — one paper, one deposition set — but the module stated a
specific attribution the record contradicts, in the field grounding its best-evidenced claim.
When a reference covers several structures, the `RP` resolution and the `FT` evidence are
different facts about different members of the set.

### The grounding was inverted, and nothing in the file showed it

Round 9's sharpest observation is not about any single claim. Part 2 grounded PvdO's *single
unpublished* 2016 PDB deposition in three separate evidence items, while part 1 — the step this
module calls solid, the only one with primary enzymology — named no structure, rested its
cofactor on one adjective in a review, and reached NCBIfam through a *P. putida* ortholog's row
in a regenerable results TSV when `NF051454` sits on the *P. aeruginosa* record itself.

That shape is invisible from inside any one field. Every individual citation was defensible; what
was wrong was the distribution, and the only way to see it is to ask which claim in the module is
best supported and then check whether its grounding is the heaviest. It wasn't, by a wide margin.
Both primary papers, three structures and six copper-binding residues were available and unused,
while an unpublished deposition carried three items.

Fixed by grounding part 1 properly rather than by thinning part 2: the NCBIfam line from pvdP's
own record, PMID:31899238 for the activity and for the family's clade boundary, and the di-copper
evidence restored above.

### Prefer the subject's own record to an ortholog's derived table

The NCBIfam accession was being cited through `projects/REFSEQ_GO/results/PSEPK/ncbi_proteins.tsv`
— a regenerable file, about the *P. putida* ortholog — when the same accession is a `DR` line on
the *P. aeruginosa* record. That was the right call when pvdP's record was not on `main`, and
stopped being so the moment it was. Same lesson as the deletion-versus-deferral one above: a
citation chosen because of what the tree contained needs revisiting when the tree changes.

### One claim per evidence item

The 5HHA citation landed as a single evidence item whose `statement` said it grounded PvdO's
FGE fold *and* its calcium site as observed rather than predicted — attached to the quote
`DR   PDB; 5HHA; X-ray; 1.24 A; A/B=22-284.`, which establishes only that a structure exists at
that resolution over those residues. Of the two substantive attributes the statement claimed, the
quote carried neither; both were on other lines of the same file it already cited.

Split into three: the cross-reference for the modality, `X-RAY CRYSTALLOGRAPHY (1.24 ANGSTROMS)
OF 22-284 IN COMPLEX WITH CA(2+)` for the calcium, and the Pfam line for the fold. The
shared-authors reasoning moved onto the deposition-title item, where the naming claim it
qualifies actually lives.

The generalisation, which is the fourth variant of one idea in this file: **an
`evidence[].statement` should name one claim, and the quote beside it should carry that claim.**
When a statement needs the word "and", that is usually two items. A multi-claim statement is how
a quote ends up vouching for things it never mentions, and nothing checks it — `validate-quotes`
confirms the quote is verbatim, not that it supports what the statement says it supports.

### A position change has to be propagated to every field

Moving from "use the weaker verb" to "the closure is open" was carried into the node label and
the part role but not the top-level `description`, which still had PvdP "oxidatively cyclising"
the residues — the exact claim gap 5 had just recorded as unknown, in the field read without the
apparatus. Note that this was not a sourcing defect: the figure legend licenses that wording,
and it was fine before the module took its new position. What changed was the module, and the
check that catches it is to re-read every field that touches a claim after changing what the
module says about it, not just the fields the reviewer quoted.

## Keep review history out of published slots

By round 6 the module file had accumulated sentences like "this is the second attempt at encoding
this relation honestly", "PRECEDES was used here first", "the first version collapsed them", and
an `evidence[].statement` explaining what had been missing from the module rather than what the
source establishes. That is this file's job, and the history records', and neither belongs in a
published module that someone else will read without any of this context. An
`evidence[].statement` should say what the source supports; a `description` should describe the
biology; the editorial trail goes here. Cleaned out in `e5fc71b771` — worth watching
for, because each instance arrived as a reasonable-looking act of transparency.

## Open questions for a reader with more sources

1. Ground the PtaA variant from the primary paper (the review's ref 74).
2. Read the A506 in-frame deletion paper (ref 71) and promote parts 2 and 3 off review-only
   evidence, which would be most of what DRAFT is recording.
3. Is PvdM's reaction known anywhere? If so the module gains its missing middle.
4. What accepts the electrons from the two oxidations? The review says the electron transport
   pathways have not been clarified; the one lead is that adding cysteine to a growing *ccmC*
   mutant culture produced ferribactin.
