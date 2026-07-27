# ADCK5 (Q3MIX3) — is the "protein serine/threonine kinase" assignment supported?

Four reproducible analyses, all runnable from this directory with no arguments:

```bash
python3 ubib_motif_analysis.py              # diagnostic residue columns
python3 ubib_motif_analysis.py --self-test  # break-tests its guards, both directions
python3 family_annotation_census.py         # human UbiB family GO/EC census
python3 partner_localisation.py             # IntAct partners: topology and assay independence
python3 audit_adck5_claims.py               # prose surfaces must not drift from the JSON
python3 audit_adck5_claims.py --self-test   # break-tests the audit, both directions
```

Outputs: `results.json`, `family_census.json`, `partner_localisation.json`,
`ubib_family.fasta`, `ubib_family.aln.fasta`. Deleting the `.json`/`.fasta` files and
re-running reproduces them byte-for-byte.

All four scripts are **stdlib-only** (plus `mafft` on `PATH` for the alignment), so the bare
`python3` invocations above work on a clean interpreter. That is deliberate: an interim
version of the audit imported PyYAML, which would have made the documented command fail for
anyone without it while working fine on the author's machine — a documentation defect that
only shows up on someone else's.

`audit_adck5_claims.py` re-reads the three JSON outputs and asserts that every residue call,
census number and withdrawn phrasing is consistent across `RESULTS.md`, `ADCK5-notes.md` and
`ADCK5-ai-review.yaml` — the "fixed in N places, landed in N−1" failure. It earned its keep, twice:
after the PR reviewer pointed out that the compartment argument assumed a membrane sidedness
this review elsewhere declines to assert, the first "fix" softened **one** of four
occurrences. Widening the scan to the whole gene folder found two more — a second YAML field
and a *script docstring* — which is why the scan is not limited to the prose files. The
**fourth** survived even that, in this very file, because the paragraph *paraphrased* the
withdrawn conclusion instead of repeating the pinned literal. Scope had been widened;
vocabulary had not.

That is a limit of literal matching, not a gap in the phrase list, so adding more literals
would not have closed it. The compartment claim is now guarded **structurally**: any
paragraph that states NOTCH2NLA's own localisation — the contrast the argument is built from
— must carry a statement that ADCK5's sidedness is unmeasured, in that paragraph or the next.
The trigger is the topic, so rewording the conclusion cannot evade it.

A file-level version of that invariant was written first, tested against the actual text that
shipped, and **passed** — the historical file hedged in a different section. Hence
paragraph-locality, and hence `--self-test` replays that real paragraph rather than a
synthetic mutation.

**Then the paragraph-local version turned out to be file-level too, on the surface that
mattered most.** `_paragraphs()` split on blank lines, and `ADCK5-ai-review.yaml` contains
**zero** blank lines — so the whole 550-line file came back as one paragraph, and a hedge in
the `GO:0016020` row was silently satisfying the check for an unhedged claim in a *different
annotation*. Found by the PR reviewer, and it is the fifth instance in this PR of one shape:
**a check whose unit of analysis is coarser than the unit the claim lives in.** The splitter
now divides a YAML surface at every mapping key, so each `summary`, `reason` and
`gap_statement` is its own unit — **233 units, not 1** — while markdown keeps blank-line
paragraphs, and the one-paragraph lookahead applies only to markdown, since an adjacent YAML
field is usually an unrelated key. Fixing it immediately caught the row-3 summary, which had
been asserting the argument flatly under a renamed label.

The split is a line scan rather than a YAML parse, for a reason worth stating: a parse needs
a failure branch, and the only obvious fallback — treat the file as one blob — silently
restores exactly the file-level behaviour this function exists to abolish. There is no parse
and therefore no fallback, and a YAML surface that yields fewer than two units is a hard
error naming the pattern to check.

Residual limit, stated rather than hidden: in markdown a hedge more than one paragraph away
still evades this, so withdrawing a claim still needs a human re-read.

Two further hardening points from the same review. The historical paragraph was originally
read by `git show` from a branch-local SHA — which would not exist in a fresh clone after
squash-merge, so **the strongest test in the suite would have broken the moment this PR
landed**. It is now frozen as
`fixtures/historical_unhedged_compartment_paragraph.md`, and a self-test asserts that fixture
is *excluded* from the live scan, since it preserves the bad text on purpose. And
`expect_flag` takes a `match=` naming the guard under test, on **all 19** call sites:
replaying the historical paragraph fires **two** messages, only one of which is the
compartment guard, so without `match=` that test could have passed on an unrelated check.
Asserting that *something* failed is not asserting that the thing you were testing failed.

Writing the audit exposed four defects in the audit itself, every one found by running the
break-tests and none by reading it:

1. a residue check that reported a conflict between K147 and K228, both correct — it **failed
   on perfect agreement**, i.e. the happy path was the untested path;
2. a withdrawn-phrase matcher that fired on this file's own explanation of the correction it
   was policing;
3. a keyword-argument mismatch that aborted the suite halfway while the earlier checks still
   printed as passes;
4. the widened scan matching **its own definition list** — the registry of withdrawn phrasings
   necessarily contains all of them. Fixed by excluding exactly one file, this script, by
   resolved path rather than by extension; a self-test plants a phrase in a *sibling* script
   and requires a catch, so the exclusion cannot silently widen.

### The class that kept recurring, and the invariant that closes it

Four review items in this PR were one thing: **a claim about a paralog's database record,
asserted in prose with nothing in the repo to check it against.** The parity framing
(blocking), the supplied-vs-corroborated split (blocking), the MitoCoP row (blocking), and
ADCK2's SubCell provenance (raised as a suggestion) — the MitoCoP row being the other half of
the very sentence whose first half was fixed the round before. (For the record, since this
paragraph names the same paralogs: their SL-0173 rests on `PubMed:33988507`, an assay ADCK5
was never in.) Fixing these one at a time was losing to the rate of discovery.

So `check_cross_gene_claims` closes the class. Every cross-gene *record* claim must be
**covered**: the fact lives in `family_census.json` and is re-asserted against the committed
JSON, or against the committed PAINT table — **ten dimensions**: IBA rows, the MitoCoP
`GO:0005739` HTP row, EC numbers, the Ser/Thr keyword, `SUBCELLULAR LOCATION`, `NOT|` rows,
the screen-provenance partition, the exact per-gene tag sets pinned by the table in the
localisation section below, the PAINT node's terms and seed, and the exact kinase-row sets
(term, evidence, qualifier and reference) for COQ8A and COQ8B. The PAINT table is **shared
repo state this review does not own**: if another branch re-fetches the family, this gene's
audit will fail, and that failure should be read as "the upstream table moved", not "the
review drifted".

**Routing is per sentence, not per unit — and that mattered.** The first version routed per
*unit*, so one covered token gave a blanket pass to every other record claim in the same unit.
The reviewer-predicted fifth instance was already in the tree because of it: the sentence
stating that GOA carries both a negated and a positive `GO:0004672` IDA row for COQ8B tripped
the gate, resolved to the `negated` dimension via its `NOT|` token, and passed — while the
positive row and both PMIDs were asserted nowhere. The self-test had "proved" the catch only
because its probe was appended as a standalone paragraph carrying no covered token. Both are
fixed: routing is per sentence (paralog and record token must occur in the *same* sentence),
and the `kinase_rows` dimension asserts the **exact** kinase-row set, with references, for
COQ8A and COQ8B.

**Residual limits, stated rather than papered over.** Two of them, and the second is the
larger:

1. Routing is per sentence, not per *claim*. A sentence mixing a covered record claim with an
   uncovered one still passes, because a sentence's tokens are unioned into one decision.
2. **A record claim whose subject is an antecedent in a neighbouring sentence is not gated at
   all** — "…carried by ADCK1 and ADCK2." followed by "The HTP row…". Carrying the last-named
   paralog forward across sentences was implemented and then *withdrawn*: with the colon no
   longer splitting, both in-tree claims this gate exists for already sit in one sentence
   each, so it bought nothing and produced three false positives on sentences about ADCK5's
   **own** evidence codes. Anaphora across a sentence boundary is therefore a known hole, not
   a covered case.

Regex cannot do better than this honestly, and pretending otherwise is exactly how the
per-unit version came to claim more than it did.

**What makes it close the class rather than enumerate it** is that the *trigger* is generic.
Any **sentence** naming a paralog alongside a **record-shaped token** — a GO evidence code
(the full vocabulary, not a sample), `GO_REF:`,
`ECO:` id, SubCell id, EC number or PANTHER node id — must route to a covered dimension, and
fails if it does not. A bare `GO:xxxxxxx` is deliberately excluded: it names a *term*, and
terms are discussed throughout the literature prose. An earlier version keyed the trigger on
the token→dimension map itself, whose keys mapped one-to-one onto the covered dimensions, so
the uncovered branch was **unreachable for any real prose** — it closed the enumerated
dimensions while claiming to close the class. The self-test proves the difference by running the two
failures a reviewer *predicted* would be the fifth instance — a claim about which evidence
code backs a paralog's positive kinase row, and a claim about a paralog's annotation and
experimental counts — and requiring both to fail **without any token being added first**. The
probe strings live in the audit script rather than here, since writing a hypothetical false
claim into a scanned surface would trip the very guard being described.

Literature claims about paralogs stay out of scope, and that exclusion is narrow and stated:
those are anchored by `supporting_text` and already checked verbatim against the cached
publications. **There is no exemption list**: one was added for a unit whose record token was
ADCK5's own `IPI`, then found *unreachable* once routing moved to sentence level — described
here as an active escape while no input could reach it. Restricting `.py` surfaces to comments
and docstrings removed the only case that motivated it, so the mechanism is gone rather than
kept as decoration.

Every guard is exercised in the direction it exists to catch **and** in the happy
direction, plus invariants about the harness itself; `--self-test` reports the count
rather than this file hardcoding it, because that number drifted three times while the
suite grew and a hand-written figure that has to track a computed one is exactly the
drift this whole file argues against. Two replay **real** defects from this
PR's own history, frozen as fixtures: the unhedged compartment paragraph and the
pre-retraction parity units.

## Question

UniProt names ADCK5 "Uncharacterized aarF domain-containing protein kinase 5", assigns it
`EC 2.7.11.-`, gives it the `Serine/threonine-protein kinase` keyword, and therefore emits
`DR GO; GO:0004674; F:protein serine/threonine kinase activity; IEA:UniProtKB-KW`. In the
same entry it states that "The function of this protein is not yet clear."

ADCK5 belongs to the UbiB family. For the two human members whose activity was actually
measured, the answer to "is this a protein kinase?" turned out to be largely no: Stefely
et al. showed "neither catalyzes canonical protein kinase activity" in trans
(PMID:27499294). So the question is whether ADCK5's kinase label is a real activity call or
a fold name propagated into an activity.

## Analysis 1 — diagnostic residue columns

MAFFT `--auto` alignment of the five human UbiB proteins plus yeast Coq8p, *E. coli* UbiB
and a canonical protein kinase negative control (PKA Cα, P17612). Motif columns are located
from a reference sequence whose residue numbering is **published**, and every published
residue is asserted against the downloaded sequence before any column is read.

Percent identity to ADCK5 over co-aligned columns:

| sequence | identity |
|---|---|
| ADCK1 | 39.9% |
| Coq8p (yeast) | 24.2% |
| UbiB (*E. coli*) | 24.1% |
| COQ8B | 22.4% |
| COQ8A | 21.4% |
| ADCK2 | 20.3% |
| PKA Cα | 15.6% |

| column | reference | UbiB expects | PKA has | **ADCK5 has** | discriminates? | other UbiB |
|---|---|---|---|---|---|---|
| KxGQ lysine | COQ8A:276 | K | *gap* | **K147** | yes | 6/6 |
| A-rich loop | COQ8A:339 | A | G | **A209** | yes | 5/6 |
| G-rich loop 2nd Gly | PKA:53 | A | G | **A209** | yes | 5/6 |
| catalytic-loop Asp | COQ8A:488 | D | D | **D360** | no | 6/6 |
| DFG Asp | COQ8A:507 | D | D | **D382** | no | 6/6 |
| β3 (VAIK) Lys | PKA:73 | K | K | **K228** | no | 6/6 |
| αC Glu | PKA:92 | E | E | **E281** | no | 6/6 |
| catalytic-loop Asn | PKA:172 | N | N | **N365** | no | 6/6 |

Two independent anchors — COQ8A's A-rich loop A339 and PKA's G-rich loop G53 — resolve to
**the same alignment column (391)**, which is the correspondence Stefely et al. assert
("the analogous A-rich loop of ADCK3"). The script asserts this rather than assuming it; if
MAFFT separated them, the A-rich claim would not be supported by this alignment and the run
aborts.

### What this shows

**ADCK5 is built like a UbiB protein, not like a canonical protein kinase.** It retains
both features that Stefely et al. identified as positioned to *inhibit* protein kinase
activity:

* the invariant **KxGQ** motif (K147) — the motif whose domain "occludes the canonical
  peptide substrate pocket" (PMID:27499294), and which is absent altogether from PKA
  (the column is a gap);
* the **A-rich loop** alanine (A209, third residue of an `AAAS` at 207–210, exactly as
  COQ8A's A339 is the third residue of an `AAAS` at 337–340) in place of the canonical
  glycine. This is the residue whose A→G mutation in COQ8A/Coq8p flips nucleotide
  selectivity and *enables* autophosphorylation.

**ADCK5 is not a dead pseudokinase either.** The catalytic and nucleotide-positioning
machinery is fully intact: β3 lysine, αC glutamate, catalytic-loop aspartate and
asparagine, and the DFG aspartate are all present. Those five columns do not discriminate
(PKA has them too) and are reported as non-discriminating rather than counted as evidence
either way.

### One incidental per-gene difference, relevant to the sibling reviews

At the A-rich-loop column, **ADCK2 alone among the seven UbiB proteins carries a glycine**,
the same residue PKA has. Every other member — ADCK5, ADCK1, COQ8A, COQ8B, Coq8p, *E. coli*
UbiB — has alanine. In COQ8A and Coq8p this exact A→G change is the engineered mutation
that reverses ADP-over-ATP selectivity. Whether ADCK2 is therefore natively ATP-preferring
is untested; flagged for the ADCK2 reviewer rather than concluded here.

## Analysis 2 — human UbiB family GO/EC census

Complete (non-truncated) QuickGO and UniProt queries for all five human UbiB genes.

| gene | EC | Ser/Thr kinase KW | annotations | IBA | experimental | IBA node | NOT| rows |
|---|---|---|---|---|---|---|---|
| **ADCK5** | **2.7.11.-** | **yes** | 4 | **0** | 3 | **none** | 0 |
| ADCK1 | 2.7.-.- | yes | 8 | 3 | 4 | PTN005148758 | 0 |
| ADCK2 | 2.7.11.- | yes | 8 | 1 | 5 | PTN000059786 | 0 |
| COQ8A | 2.7.-.- | no | 87 | 1 | 83 | PTN000059692 | 2 |
| COQ8B | 2.7.-.- | no | 19 | 1 | 12 | PTN000059692 | 2 |

Two findings, both asserted by the script so they fail loudly if the databases move:

1. **ADCK5 is the only human UbiB gene with no IBA annotation at all.** UniProt states this
   independently: "PAN-GO; Q3MIX3; 0 GO annotations based on evolutionary models."
2. **The EC downgrade tracks whether the activity was measured.** COQ8A and COQ8B, the two
   members actually assayed, were moved to the generic `EC 2.7.-.-` and lost the Ser/Thr
   kinase keyword, and both carry `NOT|enables GO:0004672` plus `NOT|involved_in GO:0006468`
   (IDA, PMID:27499294). ADCK5 and ADCK2, never assayed, still carry `EC 2.7.11.-` and the
   keyword. ADCK1 is intermediate: `EC 2.7.-.-` but the keyword retained.

### Why ADCK1 and ADCK2 get a mitochondrial UniProt annotation and ADCK5 does not
#### (they were in an imaging screen, PubMed:33988507, whose library did not contain ADCK5)

Worth stating precisely, because the obvious reading is wrong. All three genes carry the same
MitoCoP HTP row (`PMID:34800366`), so it looks as though UniProt is treating identical evidence
differently. It is not: `ADCK1-uniprot.txt:117` reads
`SUBCELLULAR LOCATION: Mitochondrion {ECO:0000269|PubMed:33988507}` and ADCK2's entry carries
the same evidence tag, while MitoCoP is **not cited in either entry**. Both paralogs have a
dedicated *experimental* localisation from the subcellular kinome atlas that ADCK5 lacks.

**But ADCK5 lacks it because it was never assayed**, not because it was assayed and found
elsewhere. That paper says so: *"ADCK5 and OBSCN were absent from the library"*. QuickGO returns
**0** annotations for Q3MIX3 from `PMID:33988507`, consistent with absence of testing.

The passage supports a slightly stronger reading than a bare absence. It is reconciling the
screen's 22 mitochondrial kinases against the MitoCarta2.0 mitochondrial proteome, and it lists
two kinds of exception: ADCK5 and OBSCN, *absent from the library*; and FASTK and PAK5, which
were in the library and which the authors tested and called non-mitochondrial. ADCK5 is in the
first group — a mitochondrial candidate the assay never reached, not one it examined and
rejected. `family_census.json` also records what that screen did for each paralog's UniProt
localisation, and the two cases are not the same — `mitochondrial_localisation_provenance`
partitions them:

| gene | `ECO:0000269` tags on its mitochondrial location | role of the screen |
|---|---|---|
| ADCK1 | `PubMed:33988507` | **sole** evidence — supplied it |
| ADCK2 | `PubMed:33988507` | **sole** evidence — supplied it |
| COQ8A | `PubMed:11888884` (2002), `PubMed:25498144`, `PubMed:33988507` | one of three, and the latest — **corroborated** it |
| COQ8B | `PubMed:24270420` (2013), `PubMed:33988507` | one of two, and the later — **corroborated** it |
| **ADCK5** | *none* | **absent from the library** |

An earlier draft said the screen "supplied" the localisation for all four, which the JSON in
the same commit refuted. The load-bearing conclusion is unaffected and is what the partition
asserts: all four paralogs were in the library and **ADCK5 is the only member it could not
assess.** The script fails if that partition changes.

The evidence tags behind this are now computed into `family_census.json` by
`family_annotation_census.py` rather than described in prose, and the script asserts the
corrected claim: if ADCK1 or ADCK2 ever loses its experimental mitochondrial location, or if
ADCK5 gains one, the run fails and the correction request must be revised. A cross-gene claim
has to be checkable from the repository, not from a live query someone once ran — which is the
defect that let the original parity claim stand for four surfaces.

So the UniProt correction request in the review is posed on ADCK5's own evidence — its MitoCoP
membership, 17 of 25 mitochondrial interactome partners, and the family's exclusively
mitochondrial distribution — and not on a parity with its paralogs that does not hold. An
earlier draft made the parity claim on three surfaces, including in text addressed to UniProt
curators who would have checked it.

### An unflagged contradiction in a neighbouring gene, visible in this census

`family_census.json` records COQ8B holding **both** of these, from the same aspect and the
same evidence code:

```
GO:0004672 IDA NOT|enables      (PMID:27499294)
GO:0004672 IDA enables          (PMID:38425362)
```

Read as GO terms alone, that asserts and negates protein kinase activity for the same gene
simultaneously.

**This is an ontology-expressivity gap, not a curation defect.** The merged COQ8B review
`ACCEPT`s both rows *and reconciles them explicitly* — its NOT row records that the negation
"refers to general in-trans kinase behaviour; it does not contradict the later, specific
ATP-dependent COQ3 phosphorylation by COQ8B (PMID:38425362)". The curator got it right. What
they could not do is express it **in terms**: GO offers no way to say "no activity in trans
toward general substrates, but yes toward this one specific substrate", so the reconciliation
lives in free text while the term-level record stays self-contradictory to any consumer
reading terms.

That is the same gap recorded in ADCK5's second `knowledge_gaps` entry, and COQ8B shows its
cost on a **characterised** member rather than a dark one — arguably the better illustration,
since there the biology is known and the ontology still cannot carry it.

*(An earlier draft of this section claimed the COQ8B review had missed the conflict. It had
not. The claim came from reading the structured fields — term, evidence, negated, action —
and not the summaries. Checking `action:` values is not checking a review.)*

## Analysis 3 — PAINT node placement (`just fetch-panther-paint`)

ADCK5 is `PTHR43173:SF28`; ADCK1 is `PTHR43173:SF19`; ADCK2 is `PTHR45890:SF1`; COQ8A/COQ8B
are `PTHR43851:SF1`/`SF4`. Three different PANTHER families for five paralogs.

| family | node | terms | seeds |
|---|---|---|---|
| PTHR43173 | PTN005148758 | GO:0005743 mitochondrial inner membrane; GO:0007005 mitochondrion organization; GO:0055088 lipid homeostasis | `SGD:S000004243` (yeast MCP2) |
| PTHR43851 | PTN000059692 | GO:0006744 ubiquinone biosynthetic process | 8 entities incl. COQ8A, COQ8B |

`PTHR43173` — ADCK5's own family — has exactly **one** annotated node, seeded by a single
yeast protein (MCP2, itself `PTHR43173:SF19`). ADCK1 receives all three of its terms;
**ADCK5 receives none**, because the node sits in the SF19 clade and does not reach SF28.

A reach scan of the three node terms was run but hit a page cap for GO:0005743 (2,500 of
10,019) and GO:0007005 (2,500 of 9,097), so those entity lists are **floors and are not
reported as complete**. The load-bearing claim does not depend on them: the per-gene QuickGO
query for Q3MIX3 returned all 4 of 4 annotations, none IBA, and UniProt's PAN-GO line agrees.
The GO:0006744 scan was complete (1,920 of 1,920) and contains no ADCK5.

## Analysis 4 — the `GO:0005515` partner, and the interaction record

All 54 IntAct interaction records for Q3MIX3 (complete; `len(rows) == totalElements`
asserted):

| reference | method | n | partners |
|---|---|---|---|
| PMID:27499296 | anti tag coip | 40 | 25 distinct partners, **17 of 25 UniProt-annotated to the mitochondrion** (ATP5F1B, C1QBP, CHCHD2, CHCHD3, ECH1, ETFA, HARS2, HOGA1, HSPA9, IMMT, MRPL2, NDUFAB1, PMPCB, POLDIP2, SHMT2, SSBP1, STOML2) |
| PMID:25416956 | **two hybrid array + two hybrid prey pooling approach + validated two hybrid** | 3 | **NOTCH2NLA** |
| PMID:31515488 | two hybrid array | 1 | **NOTCH2NLA** |
| PMID:33961781 | anti tag coip | 2 | TMEM160, ZMPSTE24 |
| others | various | 8 | singletons |

The two GOA `GO:0005515` rows both name **NOTCH2NLA (Q7Z3S9)**. UniProt records
`Q3MIX3; Q7Z3S9: NOTCH2NLA; NbExp=4;` — but the four experiments are **three sub-method
labels of one Rolland/CCSB Y2H screen** plus one further Y2H from the same resource
lineage. MI score 0.67 on every row; no orthogonal assay anywhere in IntAct. This is the
third gene in this campaign where `NbExp` counts sub-methods of a single screen (after
ACRV1 and ADAMTSL5).

Compartment (a supporting consideration, **not** a conclusion): NOTCH2NLA (Q7Z3S9, reviewed,
236 aa) is annotated `Secreted` and `Cytoplasm` and is a human-specific regulator of neural
progenitor proliferation. ADCK5 is a mitochondrial protein — in eukaryotes "UbiB homologs are
found exclusively in mitochondria" — and its only large interaction dataset (PMID:27499296,
the mitochondrial interactome) returns 25 partners of which 17 are annotated to the
mitochondrion. Y2H places both proteins in the yeast nucleus, removing whatever targeting
constraint applies in vivo.

**How far that argument actually goes.** It requires ADCK5's kinase-like domain to face the
matrix, as COQ8A's C-terminus is measured to do. **ADCK5's own sidedness has never been
measured** — the single transmembrane segment is a prediction, and an outer-membrane anchor
presenting the domain to the cytosol is not excluded. That is precisely the uncertainty that
stops this review proposing `GO:0031966`, so the compartment point is stated here as an
assumption and nothing rests on it. The `MARK_AS_OVER_ANNOTATED` verdict rests on the
method-replication argument, which stands alone.

Every number above is computed by `partner_localisation.py`, not typed: it re-pulls all 54
IntAct records (asserting `len(rows) == totalElements`), resolves every partner by **UniProt
accession** rather than gene symbol, and emits `17 of 25`,
`orthogonal_assay_for_goa_partners: {Q7Z3S9: false}`, `mi_scores: [0.67]` (one distinct score
across every row — itself evidence the rows are not independent observations) and
`methods_by_pmid`, which is what shows `25416956` contributing three sub-method labels and
`31515488` one. `audit_adck5_claims.py` then holds this
file, the notes and the review YAML to those values, and fails if an orthogonal assay ever
appears for Q7Z3S9 — which would make the `MARK_AS_OVER_ANNOTATED` verdict stale.

(A first draft of this file claimed all 25 partners were mitochondrial and the measurement
refused it. Resolving by accession also removes a real ambiguity: the symbols `HARS2` and
`MRPL2` each match two reviewed Swiss-Prot entries, so a symbol-keyed lookup would have
silently picked one.)

**Negative results from this check, recorded so the next reviewer knows it was run:**
NOTCH2NLA resolves to a *reviewed, canonical, full-length* Swiss-Prot entry — no TrEMBL or
partial-ORFeome substitution of the kind found on ACRV1. And the mitochondrion HTP row's
reference (PMID:34800366) is a proteome-wide localisation census, not a complex-to-subunit
projection: it carries no functional or phenotype term that could spread across a complex,
so the ACTR8 projection failure mode does not apply.

## Conclusion

The kinase label on ADCK5 is a **fold-derived name, not a measured activity** — UniProt says
so itself. But the correct inference is narrower than "UbiB proteins are not protein
kinases": COQ8B *does* phosphorylate a specific protein substrate, COQ3
(PMID:38425362, "COQ3, but not COQ6, is phosphorylated by COQ8B at multiple sites"), and
that took direct assay to establish. So ADCK5's intact catalytic core plus intact
autoinhibitory KxGQ and A-rich features are consistent with a nucleotide-dependent,
substrate-restricted activity of an as-yet unknown kind — and are **not** consistent with
the generic `protein serine/threonine kinase activity` that its keyword asserts.

Crucially, **there is nothing in ADCK5's GOA to act on**: GOA carries no `GO:0004674`,
`GO:0004672` or `GO:0006468` row for Q3MIX3 (QuickGO returns 0 hits for GO:0004674 with
`goUsage=descendants`). The unsupported claim survives only in UniProt's keyword/EC layer,
which GOA no longer imports. The actionable item is therefore a **UniProt correction
request**, not a GO annotation change.
