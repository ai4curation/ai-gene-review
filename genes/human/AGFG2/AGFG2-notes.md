# AGFG2 (O95081) — review journal

Working notes for the GO annotation review. Process history lives here rather than in
row summaries. Computed evidence and its provenance are in
`AGFG2-bioinformatics/RESULTS.md`; this file records how the review got there, what was
tried and abandoned, and what a later reader should not repeat.

## Starting position

7 GOA rows, all 8 lines of `AGFG2-goa.tsv` accounted for (7 data + header), all 7
distinct, and the `fetch-gene` stub seeded exactly 7 entries. The row-collapse hazard
documented for other genes did not occur here — worth stating, because checking and
finding nothing is a result.

The gene looked dark: five IBA rows, one InterPro IEA, one bulk-proteomics HDA, no
`GO:0005515`, no FUNCTION comment in UniProt, and `PE 1: Evidence at protein level`
resting on two mass-spectrometry surveys. That reading was wrong, and finding out how
wrong is the substance of this review.

## The paper that decides the review, and how it was found

`PMID:34369554` — *"Arf GTPase-activating proteins SMAP1 and AGFG2 regulate the size of
Weibel-Palade bodies and exocytosis of von Willebrand factor"* (Biol Open 2021). Titled
for AGFG2. Full text in PMC. It contains siRNA knockdown with an siRNA-resistant rescue,
two secretagogues, ELISA quantification, TEM, and a GAP-dead point mutant.

**The affinage record does not cite it, and `gates_passed: True`.** All four of its
citations are real and numeric, and the report is internally coherent; it simply missed
the one paper that establishes what this gene does. That is the clean form of the
campaign's recall lesson: a passing gate bounds precision and says nothing about recall.

How it was actually found: a recorded PubMed query crossing the gene synonyms
(`AGFG1 OR AGFG2 OR HRB OR HRBL OR drongo`) with ArfGAP-activity vocabulary
(`"GAP activity" OR "GTPase-activating" OR "GTP hydrolysis" OR ArfGAP`). The query was
written to test whether GAP activity had ever been *measured*; it returned the
functional paper instead. Searching the mechanism vocabulary rather than the symbol is
what surfaced it — the same shape as a paper titled for a partner holding the only
experiment on your gene.

The second-order find from that same query was `PMID:23433073` (Schlacht et al., Traffic
2013), reached because `PMID:34369554` cites it by author name in a sentence about lost
ArfGAP residues. That paper is what turned the `GO:0005096` verdict from an opinion into
a measurement.

## affinage: one table row contradicts its own narrative, and its own cited abstract

Recorded because it is a new provider failure mode for this campaign.

The affinage table row for `PMID:26701340` reads: *"AGFG2 (HRBL) knockdown increases CD4
surface levels specifically in HIV-1 Vpu-expressing cells but not in Nef-expressing
cells."*

The "but not in Nef-expressing cells" half is false three times over:

1. the cited abstract concludes HRBL *"affects the CD4 downregulation in a dual role as
   co-factor of both HIV-1 Nef and Vpu"*;
2. `PMID:25496667`, the companion paper, states *"The finding that both EPS15 and HRBL
   mediate CD4 down-regulation in a Nef-specific manner…"*;
3. **the affinage record's own narrative section gets it right**, saying AGFG2 "serves as
   a co-factor for both Nef- and Vpu-mediated CD4 downregulation".

So the provider's two summaries of the same paper disagree with each other. Nothing in
the review rests on any affinage sentence, and the CD4 evidence is quoted from the
primary sources.

`PMID:21284487`, the record's fourth citation, is real and correctly quoted but its
mammals-only conclusion does not survive contact with a dedicated phylogenetic study;
marked `LOW_QUALITY`, see below.

**Consequence for the validation warning.** `just validate` warns that no annotation
references the deep-research file. That is left standing deliberately: the record's only
gene-specific findings that reach an annotation are the two CD4 papers, whose evidence is
quoted from the primary sources instead, and one of its four table rows misstates its own
cited abstract — so quoting it as `supporting_text` anywhere would be importing a known
error. Documenting the reason is the right response to that warning, not silencing it.

## The catalytic question: I nearly got it backwards

The brief predicted a `PSEUDOENZYME_OVERANNOTATION` shape — a catalytic term propagated
from a domain name onto a protein that has lost the catalytic residues. The first pass
tested the obvious residue and would have concluded the **opposite**:

- the C4 zinc finger is intact (C47, C50, C67, C70);
- the catalytic arginine is present at **R75**;
- `PMID:34369554` says so explicitly — *"human AGFG2 conserves ArfGAP consensus sequence
  CX2CX16CX2CX4R in ArfGAP domain"* — and built an `AGFG2[R75Q]` mutant, which
  independently confirms the residue number my motif derivation produced.

Testing one residue and stopping would have yielded "catalytic machinery intact, ACCEPT".

`PMID:23433073` names a **second** residue: the aspartate that contacts the Arf catalytic
glutamine (Arf6-Q67), *"essential to hydrolysis"*, and reports it absent from 38 of 40
AGFG sequences. Transferring ASAP3 D484 by alignment gives **Thr89** in human AGFG2. The
panel then discriminates perfectly — 5/5 AGFG proteins lack it, 4/4 GAP-competent
ArfGAPs have it, including SMAP1, the *other* hit from the same siRNA screen, which is the
control that makes the comparison mean something rather than reflect panel composition.

**A refuted assumption, kept on the record.** I first placed the aspartate at a fixed
offset from the zinc finger (the second of the four residues between the fourth cysteine
and the arginine). Its own control refused it: ASAP3 came out at 466, not 484. The
residue is 15 positions C-terminal of the arginine *in ASAP3*, and indels move it between
subfamilies, so alignment transfer is the only sound method. That is why
`arfgap_domain.py` anchors on a literature-pinned residue in a real sequence rather than
on a motif offset, and why `probe_asap3.py` is committed: the number that refused to
match was the bug report.

**Why `MARK_AS_OVER_ANNOTATED` and not `REMOVE`.** The activity is *unmeasured*, not
measured-and-absent. The zinc finger and arginine are intact, the domain is a genuine
catalytic ArfGAP domain by four independent signatures, `PMID:23433073` phrases its own
conclusion as a prediction, and the single functional test (R75Q) is reported as *data not
shown* and asks whether the arginine is needed for one function, not whether the protein
has GAP activity at all. A REMOVE would have to be earned by an assay, and no assay
exists.

## What the WITH/FROM field actually says

Every IBA row on this gene is seeded from **mouse Agfg1** — the mouse orthologue of
AGFG2's *paralogue*. The finding is not that datum on its own but its negative control:

| protein | identity to human AGFG2 | PANTHER subfamily | used as a seed? |
|---|---|---|---|
| mouse **Agfg2** (Q80WC7) | **83.2 %** | PTHR46134:**SF4** (same as AGFG2) | **no** |
| mouse Agfg1 (Q8K2K6) | 46.5 % | PTHR46134:SF1 | yes, on all 5 rows |

AGFG2's own mouse orthologue exists, is Swiss-Prot reviewed, sits in the same subfamily,
and is 36 percentage points closer — and it is in none of the WITH/FROM fields. Without
that control the observation is "an IBA from a family member", which is ordinary; with it,
it is a paralogue substitution.

The reciprocal node question was the productive one. `PTN002919572`'s human reach is
**exactly {AGFG1, AGFG2}**, and what it gives them is the mouse *Agfg1* knockout phenotype
set — acrosome assembly, spermatid nucleus differentiation, intermediate filament
organization — spread across 68 gene products from lamprey and hagfish to placental
mammals (plus one tardigrade, which looks like a mis-placement worth someone's attention).

**But the same donor is scored differently on different rows, deliberately.** For
`GO:0031410 cytoplasmic vesicle` mouse Agfg1 is `SUPPORTS_TRANSFER`: it holds its own IDA
to that exact term, and AGFG2's own endothelial data corroborate it independently. For
the three developmental terms it is `SUPPORTS_SOURCE_BUT_NOT_TARGET`. A generic
subcellular compartment transfers across a 48 %-identical paralogue with the same
architecture; a mammalian spermatid-specific developmental phenotype does not. Scoring an
entity per row rather than per gene is the point of the field.

## Checks run that came back negative, recorded as negatives

- **Propagation landing above its donor** (the ACRV1 shape): no. The propagated
  `GO:0031410` is the same term the donors hold, not a broader ancestor, so no downward
  MODIFY.
- **Self-referential IBA**: none. No WITH/FROM token is AGFG2's own accession.
- **Logical-opposite citation cross-product**: nothing to intersect — no pair of the 7
  terms is a positive/negative regulation pair.
- **Retraction / erratum / expression-of-concern**, read from `CommentsCorrections` on
  each cited record rather than by a publication-type search: none flagged across all 12
  references.
- **Row collapse in the seeded stub**: none, 7 GOA rows and 7 stub entries.
- **IntAct**: 10 records total, of which 2 are miRNA–mRNA CLASH and **8 are
  protein–protein over 5 distinct partners** — AGFG1, TRIM68 and STARD7 by anti-tag
  co-IP in *both* BioPlex releases (two records each, but one platform, so not two
  methods), XPO1 by pulldown, and *Yersinia* lcrS by Y2H pooling at MI-score 0.37. That
  is **4 human partners with co-IP or pulldown support**, which is the figure quoted in
  the review's curation knowledge-gap; the fifth partner is the bacterial Y2H hit and is
  excluded from it. None of the five is in GOA and AGFG2 has zero `GO:0005515` rows, so
  no per-partner verdicts were needed. The AGFG1 co-IP is interesting — the two
  paralogues may heterodimerise — but one platform is not replication, so nothing was
  proposed on it.

## An inconsistency between two cited papers, settled

`PMID:21284487` says AGFG2 proteins are *"present in mammals only"*, from an analysis of
the first section of the coding mRNAs. `PMID:23433073`, a dedicated phylogenetic study,
places the AGFG duplication among the subfamilies that duplicated at the base of
vertebrates. A UniProt symbol census (totals from `x-total-results`, never from a page)
finds `agfg2` in 72 ray-finned fish, 23 reptiles/birds, 4 amphibians and 1 bird, with the
`agfg1` control non-zero in every clade.

A symbol census is a name-matching pipeline's output, not an orthologue count, so it
would not settle this alone — that distinction is why the census is reported as a census.
Combined with the phylogenetic result, and with `PTN002919572` reaching lamprey, hagfish
and zebrafish, the mammals-only claim is unsupported. `PMID:21284487` is marked
`LOW_QUALITY`: it says what it is cited as saying, but its method cannot support the
conclusion.

## Context read but not used for annotation

- **`PMID:18775314`** (Pryor et al.) — the molecular basis for HRB sorting the SNARE
  VAMP7 into endocytic clathrin-coated vesicles. This is AGFG1, and it is one of AGFG1's
  three `GO:0005515` IPI references. It is the best mechanistic picture of what an AGFG
  protein does, and it is *not* transferable to AGFG2 without a measurement — noted here
  so that a later reviewer does not mistake it for AGFG2 evidence.
- **`PMID:31533044`** — drongo, the *Drosophila* AGFG protein, promoting actomyosin
  contractility during collective cell migration. Abstract-only in the cache. Titled
  "The ArfGAP Drongo", i.e. the same naming assumption this review is testing.
- **`PMID:18809720`** (Kahn et al.) — the consensus nomenclature paper for the human
  ArfGAP domain-containing proteins, read for the subfamily naming used throughout.
- `PMID:10601011`, `PMID:18393921`, `PMID:19036332` were fetched while looking for a
  citable statement of ARFGAP1's catalytic arginine and are not relied on. That search
  is why the residue derivation ended up anchored on `AGFG2[R75Q]` from
  `PMID:34369554` — a literature anchor in the actual protein under review — rather than
  on a remembered ARFGAP1 residue number.

## Decisions, in one place

| row | action | one-line reason |
|---|---|---|
| GO:0005737 cytoplasm | KEEP_AS_NON_CORE | true, but the verified ancestor of GO:0031410 on the same evidence |
| GO:0031410 cytoplasmic vesicle | ACCEPT | donors hold their own experimental rows to this exact term; AGFG2's own data corroborate |
| GO:0001675 acrosome assembly | MARK_AS_OVER_ANNOTATED | paralogue transfer + tissue mismatch; unmeasured on AGFG2 |
| GO:0007289 spermatid nucleus differentiation | MARK_AS_OVER_ANNOTATED | same, on one donor IMP |
| GO:0045109 intermediate filament organization | MARK_AS_OVER_ANNOTATED | same, and the donor row reads a downstream keratin-5 deficiency as a filament function |
| GO:0005096 GTPase activator activity | MARK_AS_OVER_ANNOTATED | Arf-contacting Asp absent subfamily-wide; activity never measured; not REMOVE because unmeasured |
| GO:0016020 membrane | KEEP_AS_NON_CORE | a 1142-entity bulk import; the protein has no membrane anchor |
| GO:0045055 regulated exocytosis | **NEW** | siRNA + rescue + overexpression in HUVEC, two secretagogues |
| GO:0044794 host-mediated activation of viral process | **NEW** | shRNA in two human backgrounds, Nef and Vpu — annotated, but *not* a core function (virus-co-opted; APOE precedent) |

## Committed guard

`AGFG2-bioinformatics/audit_claims.py` — 9 checks, 18 break-tests plus 1 no-fire test.
It gates the quotes (including the `file:` quotes that CI does not check), the GOA-row
reconciliation in both directions, `source_entities` against the WITH/FROM field, a
duplicate-key-rejecting YAML load with a raw-vs-parsed count, the residue claims against
`arfgap_domain.json`, `core_functions` coverage in both directions, a hedge sweep over
every structured slot, every prose number in the YAML against the JSON it came from, and
— check I — the numbers in `RESULTS.md` itself, because that file is *cited as evidence*
and is therefore the surface least likely to be re-read as prose. Check I reads the report
through an indirection the self-test can override, so its break-test mutates the same
artifact the check reads rather than a different representation of it.

Three of its own defects were found by break-testing rather than by reading:

1. a hedge rule that forbade the literal string `located_in` whenever `GO:0033093` was
   hedged — it fired on legitimate qualifiers on unrelated rows. A guard that forbids
   legitimate practice gets worked around, not obeyed; removed in favour of the
   structured-slot sweep, which is where the claim would actually have to be asserted to
   do damage.
2. `str(n) in body` for a small number is **vacuous** — "9" occurs inside
   "PMID:9303539". The number check now requires a mandatory context suffix and asserts
   that the suffix is non-empty, so a bare digit test cannot be written by accident.
3. the number check originally missed the word form. `All six reviewed members` passes a
   digit grep silently; both forms now count as stated, and there is a no-fire test
   asserting that spelling a bound number out does **not** trip the check.

The break-test for the number check also had to be retargeted: mutating
`1142 annotations` tripped the quote check instead, because that number appears inside a
`file:` quote. It now mutates a value that occurs nowhere in a quoted span, so it
exercises the check it is meant to exercise. Red is not the same as red for the right
reason.

## Two claims that were verified only in a transcript, and are now in the repository

Caught on a self-review pass before the first review landed. Two numbers in the YAML —
`GO:0044794`'s human usage (58 annotations over 53 entities, the reason it was chosen over
`GO:0046784`) and the IntAct partner count — came from ad-hoc queries whose output existed
only in the working session. A verification a reader of the tree cannot re-run is not a
verification.

Both are now committed: the term-usage counts in `term_checks.json` (with `GO:0045055` at
369/201 as the non-zero control that makes the `GO:0046784` zero readable), and the
interaction records in `intact.py` / `intact.json`. Check H binds all three to the JSON,
and check I binds the IntAct figures in `RESULTS.md` as well.

Writing the IntAct script also corrected an over-claim: I had described the bacterial
partner lcrS as excluded from the co-IP set by a species filter. It is excluded by
**method** — two-hybrid pooling — so the by-name filter is a no-op. It is kept, and
reported as a no-op, rather than credited with work it does not do.

## Review round 1 — approved with six non-blocking suggestions, all six taken

`ai4c-reviewer` approved and raised six 🔵 suggestions. I verified each premise before
conceding, and all six were right.

1. **`arfgap_domain.py`'s docstring still described the refuted fixed-offset method** while
   the code did alignment transfer. This is the "guard defeated by its own docstring" mode,
   and it is worse here than elsewhere because the docstring is the first thing a re-runner
   reads and the PR's stated goal was to keep the refutation *visible*. Step 1 now describes
   the two methods separately, and the fixed-offset attempt is an explicit "tried and
   refused" note with the ASAP3-466-not-484 measurement that killed it.
2. **The two controls were not equivalent and the table implied they were.** The arginine is
   *derived* and reproduces a literature number. The aspartate's position is an **input
   constant** (`ASP_CONTROL = ("Q8TDY4", 484)`); what the script verifies is residue
   identity, domain containment and the alignment column. `RESULTS.md` now labels them
   `derived` and `asserted, not derived`, and `arfgap_domain.json` carries a `method` field
   on each control saying which it is.
3. **The HIV cofactor role was in `core_functions`, and the schema says "core *evolved*
   functions".** A role a virus co-opts, with no host-intrinsic counterpart demonstrated,
   does not meet that. Checked the precedent the reviewer cited: `APOE-ai-review.yaml`
   keeps `GO:0044794` as *contextual*. The `NEW GO:0044794` annotation stays — its evidence
   is unaffected — but it is out of `core_functions`, with the reason stated in the row.
4. **The `GO:0016020` reason argued for `MARK_AS_OVER_ANNOTATED` while the action was
   `KEEP_AS_NON_CORE`.** Fixed by changing the *level* of the claim rather than flipping the
   action: the objection is to the *evidence* (a 1142-entity bulk import cannot determine a
   location), not to the term (`GO:0016020`'s definition covers proteins *attached to* a
   bilayer, which a granule-fusion factor is). The reason now says that explicitly, and
   names the reviewer's alternative reading rather than leaving it unaddressed.
5. **The Rev/RRE export result yields no annotation and the reasoning was buried** inside
   another row. Now its own `knowledge_gaps` entry: the assay is overexpression in monkey
   CV-1 cells, so it shows sufficiency not requirement; and `GO:0046784`'s definition
   specifies *intronless* viral mRNA while Rev/RRE exports intron-containing transcripts.
6. **The clade labels double-counted.** "23 reptiles and birds … and 1 bird" reads as 24
   sauropsids, but Aves (8782) is a subset of Sauropsida (8457). Now a table using
   `distribution.json`'s own clade names with the subset relation marked, and the real
   asymmetry stated: 1 avian `agfg2` against 363 avian `agfg1`.

**A guard I had to widen, and how I widened it.** Fix 3 collided with check F, which
asserted that *every* ACCEPT/NEW term appears in `core_functions`. Rather than relax the
check, it now carries an enumerated exemption **with a reason per case**, plus two new
directions that stop the exemption rotting: it fires if an exempted term is not actually
ACCEPT/NEW, and if an exempted term turns out to be in `core_functions` after all. Both are
break-tested. 12 break-tests now, all firing for the right reason.

**A bug in my own patch script, of the exact class the campaign has recorded three times.**
The queued-refinement script asserted `old not in new_text` — but the anchor is a *prefix*
of the replacement, so that assertion is **unsatisfiable**: the edit succeeded and the
script reported failure, then re-ran and reported "already applied". Replaced with occurrence
arithmetic (`out.count(old) == before.count(old) * new.count(old)`). It had also written to
the installed file rather than the staging copy; that was reverted with `git checkout` and
re-applied to the staged copy, so no partial state shipped.

**Quote-count reconciliation across the two checkers.** `checkquotes.py` went 47 → 45 this
round, which needed explaining rather than accepting: removing the second `core_functions`
entry dropped 2 quotes, and the 2 quotes added to the new `knowledge_gaps` entry are in
`provenance`, which `checkquotes.py` does not walk. My own walker sees 52 = 45 + 7
provenance quotes, all verbatim, including all 10 `file:` quotes. The numbers add up exactly,
which is the only reason the 45 is trustworthy.

## Review round 2 — approved again, two more suggestions, both taken

1. **My round-1 fix cost a guard half its coverage.** Reformatting the clade census into a
   table left check I binding 4 of the table's 10 cells, because the binding was
   suffix-matching on hand-picked cells and the reformat changed the suffixes. The
   reviewer caught it and verified the other six by hand. This is worth recording as a
   *class*: a guard that matches formatted prose loses coverage silently whenever the prose
   is reformatted, and it loses it in the direction of passing.

   Fixed structurally rather than by adding six more suffixes: check I now **parses the
   emitted table** out of `RESULTS.md` and compares it to `distribution.json` cell by cell,
   reconciling the *sets* of clades so a dropped row is caught, checking each row's NCBI
   taxon id, and failing if fewer cells were compared than the JSON has. Four break-tests
   cover it — a wrong cell, a deleted row, a missing taxon id, and the residue check.

   **Two of those break-tests failed on first run, both my fixtures rather than the guard.**
   One used `replace(old, new, 1)` and left a second copy of `R75 present` standing, so the
   check correctly did not fire; the other deleted the whole clade label, which made the row
   read as *missing/extra* instead of as *missing-a-taxon-id* — a mutation coarser than the
   distinction it was supposed to certify. Both were only visible by running them.

2. **`resolution` was empty while `significance` carried resolution-shaped text.** Taken for
   both gaps where it applied, not just the one flagged: the "what would settle it" sentences
   moved into `resolution`, and `significance` now says why the gap matters. Fixing only the
   flagged instance would have left the same inconsistency one entry away.

## Review round 3 — approved again; the fix I made left the same gap one file away

1. **I closed the coverage gap on the analysis report and left it open on the review
   document.** Round 2 taught check I to parse the census table in `RESULTS.md`; the *same*
   five numbers are stated in prose in `AGFG2-ai-review.yaml`, and none of them was bound.
   So the copy a curator actually reads was the ungated one. This is the campaign's
   "fixed in N places, landed in N−1" pattern in its most instructive form: the fix was
   correct, thorough on the artifact I was looking at, and blind to the artifact next to it.
   Check H now binds all five from `distribution.json`, with a break-test on one.

2. **A coverage counter that a failure could satisfy.** `checked += 1` sat inside the
   *failure* branch of the taxon-id test while `expected_cells` counted only value cells, so
   taxon-id failures inflated the value-cell count. One deleted row (−2) plus two missing
   taxon ids (+2) landed back at parity and **suppressed the "has lost coverage" message**.
   A floor a failure can satisfy is not a floor. Value cells and taxon ids now have separate
   counters, both counting *comparisons attempted* rather than failures found, and a
   compound break-test reproduces the exact offset scenario: under the fix it reports
   "only 8 of 10 census value cells were compared", which the old accounting hid.

3. The first-token clade keying could in principle collide and silently shrink the floor.
   Not reachable with the present five labels, but a silent shrink is precisely what the
   counter exists to prevent, so it is now asserted rather than assumed.

**Stopping criterion, stated explicitly.** Rounds 2 and 3 changed no GO term, no action, no
evidence code, no quote and no reported number — every finding was about the guards, not
about what the guards compute, and the two that *were* about what they compute (an unbound
number, a foolable counter) are now fixed. I will still fix anything that could misstate a
number or misfire on another machine. I am drawing the line at findings about the harness's
own prose.

## Review round 4 — approved; the last item was above my own stated line, so I took it

`_states_number` used a plain substring test with **no left digit boundary**, so
`"4 amphibians"` matched inside `"14 amphibians"` and `"72 ray-finned fish"` inside
`"172 ray-finned fish"`. Nothing in the tree was wrong — all five values match — but binding
single-digit quantities in round 3 widened a latent hole: a stale prose value whose trailing
digits equal the true value would have passed check H.

The reviewer flagged it as arguably below the stopping criterion I had just stated, and then
noted it concerns *what the guard computes* rather than how it reads. That is the right side
of the line I drew, so I took it rather than accepting the offered pass. A criterion that
bends the first time it is inconvenient is not a criterion.

Digit matching now requires a negative lookbehind for a digit, word matching a word boundary,
and the break-test is the **smallest** mutation a boundary-less matcher cannot distinguish
from correct text: prefix one digit to a bound value (`4` → `14`) and require check H to
reject it. 18 break-tests now.

## Environment note

The pre-write hook resolves `file:` paths and the `publications/` cache against
`$CLAUDE_PROJECT_DIR`, so in this sibling worktree it reported non-existent-file errors
for every `file:` reference and not-found-as-substring errors for quotes into
publications it could not see — all for content that is present and verbatim here. (The
error list was truncated in the hook output, so no count is claimed.) Every quote was
re-checked against the files in *this* worktree by the committed audit script before any
hook error was dismissed, and `just validate` run inside the worktree reports `✓ Valid`.
A hook error is a claim to verify, not an order — complying with these would have meant
deleting correct evidence.
