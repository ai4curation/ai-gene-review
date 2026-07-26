# ABHD8 review notes

## What the gene actually does

ABHD8 is named for a fold, and the fold is the source of nearly every problem in its GO
record. Its one characterised function is not catalytic at all — it is a scaffold that brings
an enzyme to a substrate.

The single primary paper is PMID:39225180, which shows ABHD8 binds NLRP3 and routes it into
chaperone-mediated autophagy for degradation: [PMID:39225180 "ABHD8, a member of the
α/β-hydrolase domain-containing (ABHD) family, interacts with NLRP3 and promotes its
degradation through the chaperone-mediated autophagy (CMA) pathway"]. The mechanism is
explicitly an adaptor one — the authors' own word is *scaffold*: [PMID:39225180 "ABHD8 acts as
a scaffold to recruit palmitoyltransferase ZDHHC12 to NLRP3 for its palmitoylation as well as
subsequent CMA-mediated degradation"].

Both perturbation directions are reported, which is why the `GO:1900226` IMP is solid rather
than suggestive: [PMID:39225180 "ABHD8 deficiency results in the stabilization of NLRP3
protein and promotes NLRP3 inflammasome activation"] and [PMID:39225180 "ABHD8 overexpression
ameliorates LPS- or alum-triggered NLRP3 inflammasome activation in vivo"]. Loss-of-function
plus gain-of-function on the same axis, one *in vivo*.

The axis is virally targeted: [PMID:39225180 "the nucleocapsid (N) protein of severe acute
respiratory syndrome coronavirus 2 (SARS-CoV-2) impairs the ABHD8-NLRP3 association, resulting
in an elevation in NLRP3 protein level and excessive inflammasome activation"]. UniProt
records this as a separate SUBUNIT line
[file:human/ABHD8/ABHD8-uniprot.txt "CC   -!- SUBUNIT: (Microbial infection) Interacts with SARS-CoV-2 nucleoprotein"].

Because the scaffold role is a demonstrated molecular function and no existing annotation
captured it, `GO:0140767` *enzyme-substrate adaptor activity* was added as a `NEW` IDA. That
accounts for the entry count: GOA has 15 rows and the review has 16 `existing_annotations`
entries — 15 reviewed rows plus this one proposal, which correctly has no GOA row.

## The catalytic annotations, and why none of them is removed

Five IBA rows push lipid-enzyme activities onto ABHD8 (`GO:0004620`, `GO:0052689`,
`GO:0042171`, `GO:0006654`, `GO:0055088`), plus an InterPro-derived `GO:0003824`. No reaction
or substrate has ever been reported for ABHD8. UniProt's own EC number is the maximally
uninformative one — [file:human/ABHD8/ABHD8-uniprot.txt "DE            EC=3.-.-.-;"] — which is
the signature of a protein placed in an enzyme family with nothing measured.

All six are `MARK_AS_OVER_ANNOTATED` rather than `REMOVE`, and it took a bioinformatics check
to establish that this is the right call rather than a hedge. `ABHD8-bioinformatics/`
resolves all seven distinct WITH/FROM accessions against UniProt and queries each one's own GO
evidence via QuickGO, at run time
([file:human/ABHD8/ABHD8-bioinformatics/RESULTS.md]).

**The single most important result: 6 of the 7 sources carry their own experimental evidence**
for at least one propagated term — only the PANTHER node does not. These IBAs are propagating
from genuinely characterised enzymes, not from a family-level guess. That is what makes
over-annotation the right verdict and `REMOVE` the wrong one — and it is also why the
`propagation_review` `root_cause` on every row is **`PROPAGATION_BAD`** ("the source annotation
is sound, but the term should not propagate to this target") rather than any `SOURCE_*` value.
Classifying these as weak sources would now contradict the evidence table.

**Evidence provenance and name provenance are different questions, and only one is settled for
all six.** The Drosophila source has no reviewed UniProt entry, and its FlyBase id maps to **four**
UniProt entries carrying different names — Q5U191 *"1-acylglycerol-3-phosphate O-acyltransferase
ABHD5"* and A1Z753 *"Pummelig, isoform A"* among them. Its curated GO annotations are real, but
that first name is an automatic by-similarity label. Listing it beside `LPAAT_ARATH` and `CLD1`
made an uncharacterised protein look characterised.

Two counts, at two scopes, and they must not be conflated:

| scope | sources with own experimental evidence | independently *characterised* proteins |
|---|---|---|
| all five IBA rows | 6 of 7 (only the PANTHER node lacks it) | 5 of 6 protein sources are reviewed |
| the two **hydrolase** rows (`GO:0004620`, `GO:0052689`) | 4 of 4 protein sources | **3** — the fourth is the unreviewed fly entry |

The 3 is what matters for the hydrolase rows' `MARK_AS_OVER_ANNOTATED` reasoning, since those are
the rows whose sources include the fly entry. Stated globally it would be wrong.

That ambiguity was found only because the resolver was changed to fetch more than one hit and
refuse to pick silently — and the first version of this note then said "two entries" when the
authoritative `x-total-results` count is **four**. Inferring a total from a `size=2` response is
the very error the check was added to prevent, committed one step further down. The generalisable
point: **a size-capped lookup converts an ambiguity
into a confident wrong answer**, and it did so here on the one source whose name was doing
argumentative work.

Two source identities were **misdescribed** in an earlier draft, and both errors ran the same
way — dismissing a source without resolving it:

- **`MGI:MGI:1915938` is not ABHD8's mouse ortholog.** It is Q8VD66, mouse **ABHD4**, a
  (lyso)-N-acylphosphatidylethanolamine lipase — a *paralog*. This is perfectly legitimate for
  IBA, because WITH/FROM lists experimentally-annotated **members**, not orthologs. But it means
  no ortholog-strength inference exists anywhere on these rows, and the earlier claim that this
  entry "carries the same family-level inference rather than independent experimental support"
  was wrong twice over: wrong protein, and it carries IDA.
- **`SGD:S000003342` is CLD1**, P53264, yeast mitochondrial cardiolipin-specific deacylase, with
  both IDA and IMP. It had been waved away as a distant family member — which is exactly the
  mistake already made and corrected for `SGD:S000004089`/ICT1, repeated on the row next door.

The generalisable rule: **an unresolved WITH/FROM accession cannot be dismissed, only deferred.**
Every confident sentence about a source needs the lookup behind it, and "this source is just the
same inference" is a *testable* claim about that source's own evidence codes, not a safe hedge.

The other two facts that decided the verdict:

- **`SGD:S000004089` is a real enzyme, not a mis-transfer** — ICT1_YEAST (Q12385), recommended
  name *1-acylglycerol-3-phosphate O-acyltransferase ICT1*. What is missing is a demonstration
  **in ABHD8**, not an activity in the family.
- **ABHD8 retains a complete catalytic triad.** UniProt annotates three active-site residues
  ([file:human/ABHD8/ABHD8-uniprot.txt "FT   ACT_SITE        252"], plus 370 and 398) and
  places it in MEROPS S33
  ([file:human/ABHD8/ABHD8-uniprot.txt "DR   MEROPS; S33.011; -."]). A protein with an intact
  charge relay system cannot be called a pseudoenzyme — though note those residues are
  themselves `ECO:0000250`, transferred by similarity.

The defensible position is therefore narrow and slightly unsatisfying: ABHD8's triad is
**intact and untested**. The fold-derived annotations are premature, not refuted.

### The ABHD5 analogy is wrong in both directions — a correction worth recording

My first draft argued these IBAs were fold-only propagation by analogy to ABHD5/CGI-58, "the
textbook α/β-hydrolase fold that is not a hydrolase". That argument was backwards twice over,
and the second error is the more interesting one:

1. **It cuts against my own conclusion.** ABHD5 is the fold-without-catalysis example
   *because it lacks the nucleophilic serine*. ABHD8 has the full triad. The comparison, run
   properly, is evidence that ABHD8 is **more** likely to be catalytic, not less.
2. **ABHD5 is not actually a pseudoenzyme.** The script's own output shows UniProt recording a
   demonstrated CoA-dependent lysophosphatidic acid acyltransferase activity for ABHD5, with
   substrate preferences and a primary reference — despite zero annotated active sites. So
   ABHD5 has lost the canonical hydrolase serine while retaining a different, measured
   chemistry. Invoking it as the family's dead-fold case misstates ABHD5 as well as ABHD8.

Generalising: **"protein X has fold F but no activity" is a claim about X's residues, and it
should be checked before it is used as a premise.** The fold-name-becomes-activity failure
this review is about has a mirror image — fold-name-becomes-*absence-of*-activity — and both
are shortcuts around looking at the sequence.

## Why the gene is studied at all

Worth recording because it frames the whole record: most ABHD8 literature is not about ABHD8's
activity. It is a candidate target gene of the 19p13.1 breast/ovarian cancer susceptibility
locus — [PMID:27601076 "Chromosome conformation capture identifies interactions between four
candidate SNPs and ABHD8, and luciferase assays indicate six risk alleles increased
transactivation of the ADHD8 promoter"] (the abstract's `ADHD8` is its own typo for ABHD8).

This is *cis*-regulation of ABHD8 expression, not ABHD8 protein function, so it supports no GO
annotation. But it explains the shape of the evidence: a gene with sustained genetic interest
and exactly one paper on what its protein does. That asymmetry — heavy locus-level attention,
one mechanistic study — is why the fold-derived annotations went unchallenged for so long.

## Interaction rows

`GO:0005515` appears five times. The two `PMID:32296183` rows come from HuRI, a systematic
Y2H map (full text cached), and are marked over-annotated: reproducible but uncharacterised
binary hits, with no follow-up tying either partner to ABHD8's biology. They were initially
merged into one review entry and are now split, one per GOA row, since they concern different
partners. The `PMID:39225180` rows are the NLRP3 and ZDHHC12 interactions; one is `MODIFY`
toward the adaptor MF, the other `KEEP_AS_NON_CORE`.

`GO:0070062` *extracellular exosome* (HDA, PMID:18570454) is a single neural-stem-cell exosome
proteomics dataset; the paper is abstract-only in the cache. Bulk exosome-proteome membership
is weak evidence of residence for a protein UniProt localises to cytoplasm
([file:human/ABHD8/ABHD8-uniprot.txt "CC   -!- SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:39225180}."]),
so it is over-annotated rather than accepted — but not removed, since HDA is a real
observation and I have not read the full text.

## Process notes

Recorded here rather than left in PR comments, because these recur.

- **Never write a reference `title:` from memory.** This was the third occurrence in this
  campaign; the pre-write hook hard-blocks it every time, but the wasted round is avoidable.
  Copy the title from the cached record: `grep -m1 "^title:" -A2 publications/PMID_<id>.md`.
- **`propagation_review` blocks must not be copy-pasted between rows.** `GO:0042171`'s block
  was byte-identical to `GO:0006654`'s and consequently omitted `AGI_LocusCode:AT4G24160` from
  its `source_entities`. WITH/FROM is **per row**: the five IBA rows here have 2, 3, 4, 5 and 5
  sources respectively. A copied block silently misstates what was inspected.
- **Diff the working tree against your own claims before pushing.** In round 1 I reported
  removing the ABHD5 argument from four places (it was removed from three) and splitting the
  two `PMID:32296183` rows (they were not split). Announcing a fix that did not land costs
  more reviewer trust than the original error did — the claim has to be verified against the
  tree, not against intent.
- **`file:` supporting_text is not machine-checked.** The repo validator only verifies `PMID:`
  quotes, so a broken `file:` quote passes `just validate` in silence. Every quote in this
  review was checked with a local script that applies the same whitespace normalisation
  (36 quotes, 0 problems). UniProt quotes in particular must stay inside a single physical
  line, or they pick up the `CC   ` continuation prefix and stop being verbatim.
