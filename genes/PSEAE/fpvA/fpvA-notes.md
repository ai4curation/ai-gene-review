# fpvA (PA2398, P48632) — review notes

Tier-3 PseudoCAP review. `fpvA` is a Swiss-Prot **reviewed** entry (FPVA_PSEAE, 815 aa,
`Flags: Precursor`) and the best-characterised TonB-dependent transducer in this organism. It
was included in batch 5 as a third instance of the architecture examined in `femA` and
`femI`, and because it was a verified donor in `femA`'s IBA node.

## Bifunctional, and the two functions are separable

`[PMID:15968062 "The FpvA protein of Pseudomonas aeruginosa strain PAO1 mediates uptake of a siderophore, ferripyoverdine."]`
`[PMID:15968062 "It is also a component of a signal transduction pathway that controls production of an exotoxin, a protease, pyoverdine, and FpvA itself."]`
`[PMID:15968062 "Signaling involves an N-terminal domain of FpvA, and it was shown that this domain is probably located in the periplasm"]`

Linker-insertion mutagenesis separated them: `[PMID:15968062 "the remaining mutations eliminated either the transport or signaling function of"]`
FpvA. So the review gives this gene two core functions, transport and signalling, as `femA`
got — but here the separation is experimentally demonstrated rather than inferred from domain
content. The periplasmic signalling domain is the STN region on the record
(`[file:PSEAE/fpvA/fpvA-uniprot.txt "DR   Pfam; PF07660; STN; 1."]`).

The `GO:0038023` rows are consequently the best-supported in this batch: an IDA
(PMID:18641139), an IEA, and two IMPs, with PMID:15968062 titled for the signal-transducing
function itself. All four `ACCEPT`.

## `GO:0002049` is a regulatory effect annotated as participation

The one substantive correction. `GO:0002049 pyoverdine biosynthetic process` is annotated
`involved_in` by IMP from PMID:12029043, whose title reads "FpvA receptor involvement in
pyoverdine biosynthesis". The full text is cached, and it states the mechanism:

`[PMID:12029043 "Deletion of fpvA from the chromosome of P. aeruginosa reduced pyoverdine production in this organism, as a result of a decline in expression of genes (e.g., pvdD) associated with the biosynthesis of the pyoverdine peptide moiety."]`

So fpvA's effect on pyoverdine runs through **expression of the biosynthetic genes**, not
through any step of the chemistry. The synthetases do the work — `pvdL`, `pvdD` and `pvdJ`,
all reviewed in this corpus. FpvA signals. PMID:15968062 says the same thing independently:
the signal transduction pathway "controls production of ... pyoverdine".

The same paper also shows the two roles come apart in exactly the way that settles this:
`[PMID:12029043 "The truncated receptor was, however, functional in pyoverdine-mediated iron uptake"]`
— the N-terminally truncated receptor still transports but no longer supports pyoverdine
production. Transport is intact while the biosynthesis effect is lost, which is only
intelligible if the biosynthesis effect is signalling.

`MODIFY` → **`GO:1900706 positive regulation of siderophore biosynthetic process`**, found in
OLS (with `GO:1900704` the neutral parent and `GO:1900705` the negative sibling). Positive is
the right sign: deleting fpvA *reduced* production. This is a lateral correction rather than a
refinement — `GO:1900706` is not a descendant of `GO:0002049` — which the project rules
sanction as a long-standing use of `MODIFY`, and the row's own evidence supports the
replacement directly, which is what the 2026-11-14 ruling requires.

A granularity note, recorded and not acted on: GO has no "regulation of pyoverdine
biosynthetic process", so the replacement trades substance-specificity (pyoverdine →
siderophore) for correctness of relation. That is the right trade, and proposing a
pyoverdine-specific child would be term churn for no gain, so no `proposed_new_terms` entry is
made.

## A reference that supports a different term than the row it sits on

`GO:0038023 signaling receptor activity` has an IMP from **PMID:1903349** (Poole, Neshat &
Heinrichs 1991). That paper is about transport, not signalling:

`[PMID:1903349 "Reduced expression of an iron-regulated outer membrane protein (IROMP) of approximate molecular mass 90,000"]`
`[PMID:1903349 "a mutant lacking the 90 kDa protein transported barely detectable levels of ferri-pyoverdine"]`

It identifies the 90 kDa IROMP and shows the mutant fails to transport ferripyoverdine. The
abstract says nothing about signal transduction, and cell-surface signalling by TonB-dependent
transducers was not described until a decade later, so the concept postdates the paper.

The row is **kept** — the term is right for this gene, established by IDA and by a paper
titled for the signal-transducing function — but the citation is recorded as a
`WRONG_REFERENCE` at `PROBABLE` with `requested_change: CHECK`. The evidence this paper
supplies belongs to the transporter rows (`GO:0015344`, `GO:0033214`, `GO:0015891`), and the
signalling rows already carry the two references that do support them. `PROBABLE` and `CHECK`
rather than confident: the cache is abstract-only, and "the abstract does not mention it" is
the weaker of the project's two wrong-reference categories, so this is a query to the resource
rather than an assertion.

## Routine calls, consistent with femA

- `GO:0009279 cell outer membrane` — three rows (IBA, IDA, IEA) all `ACCEPT`. The IDA from the
  crystal-structure paper is the strongest localisation evidence in the batch.
- `GO:0019867 outer membrane` → `TOO_GENERAL`, as on femA: it does not say which outer
  membrane and `GO:0009279` is its child.
- `GO:0016020 membrane` (IDA, same paper as the `GO:0009279` IDA) → `TOO_GENERAL`. Same
  evidence, two granularities; the specific one is accepted.
- `GO:0015343` kept rather than marked general, exactly as on femA: it names substrate and
  mechanism and `GO:0015344` adds only direction.
- `GO:0015891` and `GO:0033214` both kept; neither is an ancestor of the other.

## The self-donor in `WITH/FROM` is expected

The `GO:0009279` IBA lists `UniProtKB:P48632` — this gene — among its donors. Per the project's
IBA guidance that is correct and expected, not circular: fpvA has its own experimental
annotation for the term (the IDA above), so it was one of the descendant evidences the PAINT
curator used to place the IBD, and the IBA then adds that the location is inherited rather
than lineage-specific. Recorded explicitly because marking it `CIRCULAR_OR_REDUNDANT` is the
error the rules single out.
