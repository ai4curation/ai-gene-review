# AIRIM / C1orf109 (Q9NX04) — review notes

2026-09-26. PAINT no-IBA backlog. Deep research provider: affinage.

## Shape of the problem

188 GOA rows, but only **10 distinct GO terms**. 174 of the rows are `GO:0005515 protein binding`
IPI, one per interaction partner (148 distinct partners after the seeder's known WITH/FROM
collapse merged a duplicate CINP row). Where they come from:

| Source | Rows | What it is |
|---|---|---|
| PMID:32296183 | 121 | HuRI, all-by-all binary interactome |
| PMID:25416956 | 43 | HI-II-14, proteome-scale binary map |
| PMID:35354024 | 4 | the 55LCC ribosome paper |
| PMID:38554706 | 4 | the 55LCC structural paper |
| PMID:21516116 | 3 | high-throughput Y2H methods paper |
| PMID:28514442, PMID:33961781 | 1 each | BioPlex 2.0 / 3.0 |

So ~164 rows come from three systematic screens that were not studies of AIRIM at all.

## How the protein-binding mass was handled

Project policy (CLAUDE.md + the annotation-reviewer skill) is explicit and I followed it rather
than inventing a scheme: GO:0005515 is **not** `MARK_AS_OVER_ANNOTATED` — its defect is that it
conveys no functional information, not that it overclaims. `MODIFY` where a more informative
evidence-backed term exists, otherwise `REMOVE`, and removal does not assert the interaction is
false.

That split fell out cleanly on the **partner**, not the reference:

- **8 rows MODIFY → GO:1904949 ATPase complex.** Partner is CINP, AFG2A or AFG2B — genuine 55LCC
  subunits. Complex membership is the informative statement these rows were groping toward.
  Notably this includes the two BioPlex rows, whose single partner each is CINP, so an AP-MS
  screen row was treated differently from a Y2H screen row purely on who the partner is.
- **166 rows REMOVE**, each naming its own partner (resolved via the UniProt API, including 20
  isoform accessions mapped to their base entries — not written from memory).

## The real biology

AIRIM is a **structural subunit of the 55LCC complex** (AFG2A/SPATA5 + AFG2B/SPATA5L1 + CINP +
AIRIM):

> [PMID:38554706 "Here, we identify replisome factor interactions with a protein complex composed of AAA+ ATPases SPATA5-SPATA5L1 together with heterodimeric partners C1orf109-CINP (55LCC)."]
> [PMID:38554706 "An integrative structural biology approach revealed a molecular architecture of SPATA5-SPATA5L1 N-terminal domains interacting with C1orf109-CINP to form a funnel-like structure above a cylindrically shaped ATPase motor."]

One structural role, two settings:

- **Cytoplasmic pre-60S maturation** — [PMID:35354024 "We provide evidence that these factors, together with CINP and SPATA5L1, control a late step of human pre-60S maturation in the cytoplasm."], with [PMID:35354024 "Loss of either C1orf109 or SPATA5 impairs global protein synthesis."]
- **Chromatin replisome proteostasis** — [PMID:38554706 "55LCC showed ATPase activity that was specifically enhanced by replication fork DNA and was coupled to cysteine protease-dependent cleavage of replisome substrates in response to replication fork damage."]

## The MF gap, and how I filled it without over-reaching

Stripping 166 protein-binding rows would have left the gene with **zero molecular function
annotations** — which misrepresents a protein whose role is structurally resolved. Added one
`NEW`: **GO:0005198 structural molecule activity** ("the action of a molecule that contributes to
the structural integrity of a complex"), which is exactly what the funnel architecture shows.

Critically, AIRIM is *not* the ATPase — that is the AFG2A/AFG2B motor. The schema anticipates
this case, so the ATPase activity goes in `contributes_to_molecular_function` (GO:0016887), not
`molecular_function`. A term for substrate gating at the funnel would be better if one existed;
raised in suggested_questions instead of forced.

## Two gotchas worth recording

1. **`GO:1904949 ATPase complex` is rejected in `locations`.** I had put it in both `locations`
   and `in_complex`; `GOCellularLocationEnum` excludes it. Belongs only in `in_complex`.
2. **The `--terms` validator failure is silent through the wrapper.** `just validate` printed
   `✗ Invalid` with *no error line at all*. Running `linkml-term-validator validate-data`
   directly gave the actual message immediately. Worth remembering: an "Invalid with no errors
   shown" result means drop to the underlying tool.

## The IBA rows are fine

Both IBA rows carry `UniProtKB:Q9NX04` — AIRIM itself — in their own WITH/FROM. Per the skill's
guidance this is **expected and correct**, marking that the node has experimental grounding on
this very gene. Not labelled circular.

## One demotion

`GO:0005730 nucleolus` (IDA) → `KEEP_AS_NON_CORE`. Plausible for a ribosome factor and a real
observation, but the demonstrated AIRIM step is *late and cytoplasmic*, and the replisome role is
nucleoplasmic. Neither characterised activity happens in the nucleolus.

## affinage assessment

Accurate and well framed this time — correctly names the 55LCC complex, calls AIRIM's role
structural, separates the two activities, and surfaced three papers absent from GOA
(PMID:40268917, PMID:40760247, PMID:32761833). A useful contrast with ADIG (missed the decisive
paper) and ADM5 (right papers, wrong framing) earlier in the same session.

## Outcome

189 rows: 166 REMOVE, 13 ACCEPT, 8 MODIFY, 1 KEEP_AS_NON_CORE, 1 NEW.
`just validate human AIRIM` → ✓ Valid, no warnings.
17 distinct supporting_text quotes (358 instances) verified as substrings, including the 2
`file:` ones CI does not check.

## Round 2 (review feedback)

Two blocking items, both fair, and the first is a pattern I have now hit **three times in one
session**.

### Three AIRIM-specific papers were in my own diff and uncited

`PMID:40268917`, `PMID:40760247` and `PMID:32761833` — 37, 73 and 105 AIRIM mentions
respectively — were cached by this PR and cited nowhere. Worse, the description asserted that
hypomorphic AIRIM variants cause a neurodevelopmental disorder **on the strength of nothing**,
while the source sat in the same diff:

> [PMID:40760247 "Here we describe variants in the ribosome biogenesis factor AIRIM/C1orf109 that are primarily associated with neurodevelopmental disorders."]

Same shape as the ADIG cold-tolerance claim and the ADM5 heart-failure diuresis claim earlier
today. The common cause is that I cache papers while researching, use them to form the picture,
then write the picture without going back to cite what formed it. The three-time recurrence means
it is a process failure, not a slip.

### "Substrate presentation" was wrong

I wrote that AIRIM's contribution is "structural integrity and substrate presentation". The
higher-resolution structure says the opposite:

> [PMID:40268917 "CINP contributes to both the interfaces between the SPATA5 complex and the pre-60S particle, while C1orf109 does not interact with the pre-60S particle directly"]
> [PMID:40268917 "the recognition of the pre-60S particle is mediated by human-specific factor CINP, through two distinct sets of interactions: one with GTPBP4 and the other with ES27A."]

AIRIM makes **no direct pre-60S contact**. The structural-integrity half stands and `GO:0005198`
is unaffected — the N-terminal ring supports it — but the substrate half is removed, and the
`suggested_questions` entry that speculated about AIRIM *gating* access to the motor is recast to
say explicitly that gating is ruled out.

### Stoichiometry

> [PMID:40268917 "Here we reveal that SPATA5 forms a 4:2:2:2 complex with SPATA5L1, C1orf109, and CINP."]
> [PMID:40268917 "This complex features an N-terminal ring made of C1orf109, CINP and NTDs of SPATA5/SPATA5L1, and two hexameric AAA+ ATPase rings."]

"Heterohexameric" (which I took from UniProt and PMID:38554706) describes the **SPATA5–SPATA5L1
motor**, not the 4:2:2:2 assembly. Replaced everywhere it described the whole complex; the three
surviving occurrences are the sentences explaining the distinction. "Funnel" is likewise replaced
by "N-terminal ring", which is what the structure paper calls it.

### Isoform caveat recorded

`PMID:32761833` is about the **long isoform C1orf109L** binding DHX9 and promoting R-loop
dependent DNA damage. Recorded as a flagged caveat rather than folded in: it is a different
activity from the 55LCC roles, no GO annotation on this gene covers it, and it should not be
assumed to hold for the canonical product.

### Not changed

The six MODIFY rows still propose `GO:1904949`, which the gene already carries. That is
deliberate — the point of the MODIFY is that these protein-binding rows should *become* the
complex-membership statement, and duplicates to the same term are explicitly fine per the
annotation-reviewer guidance. Also unchanged: the NEW row's `file:` evidence leg is skipped by
the supporting-text validator, which is true of every `file:` quote in this repo; I verify them
by hand and say so.

Final: 189 rows, 166 REMOVE / 13 ACCEPT / 8 MODIFY / 1 KEEP_AS_NON_CORE / 1 NEW.
25 distinct quotes (366 instances) verified.
