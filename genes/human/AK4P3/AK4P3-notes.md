# AK4P3 (A0A8I5KW96) — review notes

2026-09-26. PAINT no-IBA backlog. affinage has **no record** for this locus; falcon used.

## The setup

19 GO annotations describing a working mitochondrial adenylate kinase — AMP kinase activity, EC
2.7.4.10 and 2.7.4.6, mitochondrial matrix, ATP/GTP metabolic process. **All 19 are IEA or IBA**,
applied by automatic pipelines (chiefly HAMAP-Rule MF_03170, plus InterPro2GO, UniRule, ARBA and
PANTHER) on similarity to genuine human AK4 (P27144).

And HGNC names the locus **"adenylate kinase 4 pseudogene 3"**, `locus_type: pseudogene`.

That looked like a clean over-annotation story. It isn't.

## Why the obvious story is wrong

`AK4P3-bioinformatics/` compares the ORF to AK4:

> [file:genes/human/AK4P3/AK4P3-bioinformatics/RESULTS.md "| Identity to AK4 | **221/223 (99.1%)** |"]
> [file:genes/human/AK4P3/AK4P3-bioinformatics/RESULTS.md "| Catalytic P-loop (Walker A) | `GPPGSGK` at position 12 - **intact in both** |"]

Two conservative substitutions (M53V, V177A), full-length ORF, catalytic machinery intact. So
**the pipelines are not misfiring on a decayed relic** the way they would on a frameshifted
remnant. There is no biochemical argument for removing anything.

## The decisive paper, which no GO annotation cites

Falcon surfaced **PMID:33971925** (*Long-read cDNA sequencing identifies functional pseudogenes in
the human transcriptome*), 13 AK4P3 mentions, full text:

> [PMID:33971925 "we amplified the 5' exons and coding sequence of four spliced pseudogenes with intact ORFs (HMGB1P1, AK4P3, IFITM3P2 and RPL13AP20) and cloned them into a vector with a C-terminus 3XHA tag"]
> [PMID:33971925 "Transfection into HEK293T cells resulted in clear translation of the HMGB1P1 and AK4P3 transcripts"]

So the locus is **genuinely transcribed** (recovered from human RNA) and its ORF is
**translation-competent**. That moves it decisively off "predicted ORF".

**What is still not shown**: endogenous protein production, and any assay of this protein's
activity. The translation was from a transfected construct.

## Outcome: 19 ACCEPT

Unusual for this campaign, and it is the honest answer. Every term is appropriate to the
sequence; the pipelines behaved correctly; and the locus is transcribed with a translatable ORF.
There is no biochemical, phylogenetic or evidential ground to remove or demote any row.

The caveat belongs on the rows rather than in the actions, so each catalytic row carries an
explicit note that **no AK4P3 protein has ever been assayed** and the activity is inherited from
AK4 rather than measured.

Two rows do get separated out:

- **GO:0005524 ATP binding** is the best-supported MF row — the binding determinant is a
  structural motif and it is demonstrably intact. It is what I put in
  `core_functions.molecular_function`, with AMP kinase activity under
  `contributes_to_molecular_function`, deliberately: binding is observable in the sequence,
  catalysis is a claim about a protein nobody has tested.
- **GO:0005737 cytoplasm (IBA)** comes from a much deeper node (PTN000599576, 37 donors across
  plants, yeast, fly, fish) than the mitochondrial matrix row (PTN008598552). Not wrong —
  mitochondrion is part of cytoplasm — but it is the least informative location on the gene and
  does *not* corroborate the matrix rows.

## A suspicion I checked and dropped

I thought `GO:0050145` was mapped from EC 2.7.4.4, an EC number absent from the entry — a real
defect if true. It isn't: EC 2.7.4.4 *is* in the catalytic-activity block (I had only grepped the
`DE` lines), and genuine AK4 carries `GO:0050145` too. Recorded in the row so the next reader does
not re-run the same false lead.

## The real curation question

**Should a locus HGNC calls a pseudogene carry 19 enzyme annotations in GOA?** Nothing is wrong on
the sequence, but a curator scanning GOA sees a mitochondrial adenylate kinase with no indication
that the gene is named a pseudogene or that no protein from it has been assayed. GO has no slot
for that. Raised in `suggested_questions` rather than acted on unilaterally.

There is also a cheap decisive experiment, which the bioinformatics identified: **two fully
tryptic peptides are unique to AK4P3** (`ASTEVGEVAK`, `DAAKPVIELYK`), and both substitutions are
mass-distinguishable. So UniProt's PE=1 *is* attributable in principle — targeted MS for those two
peptides would settle it either way.

## Provider note

affinage returned **no record at all** for AK4P3, consistent with its gene set excluding
pseudogenes. Falcon handled the nomenclature trap well: it separated AK4P3 from canonical
AK4/AK3L1 explicitly, warned that the AK4 literature cannot be reassigned, and found the one
AK4P3-specific paper.

## Verification

10 distinct supporting_text quotes (83 instances), all verified, 63 of the instances being `file:`
ones CI does not check. Ran my cached-PMIDs-vs-`references[]` guard over the staged diff: clean.

## Round 2 (review feedback)

### I used a schema slot to mean something it doesn't mean

I put AMP kinase activity in `contributes_to_molecular_function` to signal "unmeasured". That
slot means **"contributes to as part of a complex"** — it is for accessory and structural subunits
(Complex I, ATP synthase, the ribosome), and repo-wide usage across 414 files matches that.
AK3/AK4-family adenylate kinases are **monomeric**, so what I wrote asserted, machine-readably,
that AK4P3 is an accessory subunit of something. That is a different and false claim.

Worse, it was inconsistent with itself: if catalysis were too unmeasured for `molecular_function`,
then `directly_involved_in: GO:0046033` and `locations: GO:0005759` had no business being there
either, since both entail it.

Fixed the way the schema intends:

- `molecular_function: GO:0004017` AMP kinase activity, asserted at the same confidence as the
  process and location — the entry is now internally consistent, everything projected from AK4.
- The hedge moved to **`knowledge_gaps`**, which is the purpose-built slot and was empty despite
  this being close to the textbook case. Two gaps recorded: one `BIOLOGY`/`MF_DARK` (is the
  protein made, and does it work — with the boundary stating what *is* established, so the gap is
  sharply delimited), and one `CURATION`/`MF_DARK` (is PE=1 attributable — resolvable from
  existing PeptideAtlas data rather than new experiments).

The general lesson: **a hedge belongs in the slot built for hedging, not smuggled into a slot
that means something else.** Putting it in the wrong slot does not merely fail to communicate the
caveat — it emits a positive false claim.

### Four process rows carried a molecular-function caveat

`GO:0006172`, `GO:0009142`, `GO:0046034` and `GO:0046039` are process terms but got the boilerplate
sentence "This row asserts a specific catalytic activity". I had already written the correct
process-row wording on the `GO:0046033` IBA row and simply failed to apply it. Now there is a
separate `PROCESS` variant saying these presuppose the catalysis asserted elsewhere and inherit
its caveat.

That is the shared-preamble hazard again, in its other form: not a false fact this time, but the
wrong template applied to a third of the rows.

### Two non-blocking notes, both taken

- **The P-loop `file:` quote transliterated an em dash to a hyphen**, so it was not byte-verbatim.
  Nothing catches this — `file:` refs are existence-checked only (`validator.py:458`). I added a
  **byte-verbatim** check to my own verification pass rather than the normalized one I had been
  using, and it immediately found a second instance: the Troskie quote had `5'` where the source
  has a prime character `5′`. Both fixed; all 10 distinct quotes are now byte-exact.
- The 1,500-character preamble repeated 19 times does bury the row-specific sentence. Flagged for
  the third time across this campaign. Left as is here because each row must read standalone, but
  the accumulating evidence says the shared-context pattern needs rethinking rather than
  re-defending — noted for the next gene rather than refactored mid-review.

### Agreed and unchanged

The reviewer independently verified the biology and the 19 ACCEPT judgment, and checked the
nearest repo precedent: **LPAL2** went `MARK_AS_OVER_ANNOTATED`, but on a PE=5 entry with a
frameshift and premature stops — a genuinely decayed relic, unlike this one. So the precedent
does not cut against ACCEPT here.
