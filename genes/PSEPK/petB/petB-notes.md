# petB (Q88N94, PP_1318) — curation notes

Cytochrome *b* membrane core of the respiratory cytochrome bc1 complex of
*Pseudomonas putida* KT2440. See `genes/PSEPK/petA/petA-notes.md` for the operon-level
identity argument and the evidence caveats that apply to all three subunits; notes
here cover what is specific to petB.

## What UniProt gives, and what it does not

`petB-uniprot.txt` is an unreviewed TrEMBL entry at PE 3 (inferred from homology). It
supplies: the cytochrome b family assignment ("Belongs to the cytochrome b family."),
two non-covalently bound b hemes ("Note=Binds 2 heme groups non-covalently."),
multi-pass membrane topology, the `Electron transport` keyword, and PANTHER
`PTHR19271` CYTOCHROME B. It does **not** name the Qo/Qi sites, assign bL vs bH, or
specify which membrane — all of which the review asserts, so each is sourced below.

## Qo/Qi and the bL/bH relay

The bifurcating Q cycle is the conserved mechanism of the bacterial complex:
"It couples electron transfer from ubiquinol to cytochrome c with generation of proton
motive force which fuels ATP synthesis" [PMID:21996020 "It couples electron transfer
from ubiquinol to cytochrome c with generation of proton motive force which fuels ATP
synthesis."]. The structural work behind that statement found the Paracoccus complex
closely conserved precisely at cytochrome *b* [PMID:21996020 "It has high structural
homology to mitochondrial complexes and to the Rhodobacter sphaeroides complex
especially for subunits cytochrome b and ISP."] — cytochrome *b* is the most strongly
conserved subunit of the three, which is what licenses transferring the Qo/Qi and
bL/bH description to a PE 3 *P. putida* ortholog.

Both quinone sites lie within cytochrome *b*. That single structural fact drives two
review decisions:

- `GO:1902600` proton transmembrane transport is `ACCEPT`ed as a direct petB process,
  not marked non-core as on petA and petC. Quinol deprotonation releasing protons to
  the periplasm at Qo, and quinone protonation from the cytoplasm at Qi, are reactions
  that happen at petB.
- `GO:0022904` respiratory electron transport chain is the core process term: petB
  performs the committed step rather than merely being required for it.

## GO:0016491 — the earlier reason had the ontology backwards

The previous draft justified `KEEP_AS_NON_CORE` on `GO:0016491` oxidoreductase
activity with "subsumed by electron transfer activity". That is not the relationship.
Checked against the GO hierarchy (OLS `hierarchicalAncestors`):

- `GO:0009055` electron transfer activity has **no** ancestor `GO:0016491`; it sits
  directly under `GO:0003674 molecular_function`.
- `GO:0008121` quinol-cytochrome-c reductase activity **does** descend from
  `GO:0016491`, via `GO:0016679` (oxidoreductase activity, acting on diphenols and
  related substances as donors).

So `GO:0016491` is a broad ancestor of the *complex-level* reaction and is unrelated
by ancestry to petB's direct function. `KEEP_AS_NON_CORE` is still the right action —
it is correct but uninformative — and the reason text now says why correctly rather
than asserting a subsumption that does not exist.

## GO:0022900 is the parent of a term petB already carries

`GO:0022900` electron transport chain is a direct ancestor of the co-annotated
`GO:0022904` respiratory electron transport chain (same OLS check). Accepting both as
equals states one claim at two granularities. Moved to `KEEP_AS_NON_CORE`:
redundant but not incorrect, with `GO:0022904` the term that belongs in
`core_functions`. `genes/human/NDUFS4/NDUFS4-ai-review.yaml` reaches the same
judgment about the same pair, keeping the broader term with an explicit note that it
is redundant.

## Location: why GO:0005886 rather than GO:0016020

petB's own UniProt line is only the unqualified "Membrane". The refinement to
`GO:0005886 plasma membrane` is an inference from complex membership, not from petB's
own record — the co-operonic petA carries an explicit "Cell membrane"
(UniProtKB-SubCell:SL-0039), and in a Gram-negative bacterium a respiratory complex
III subunit is in the cytoplasmic (inner) membrane. `modules/bacterial_cytochrome_bc1_complex.yaml`
already asserts `GO:0005886` for this subunit, so the earlier `GO:0016020` in
`core_functions.locations` contradicted the module; the gene review has been brought
into line with the module rather than the reverse.

`MODIFY` was chosen over `REMOVE` (the action used on petA's `GO:0016020`) because
petB has no `GO:0005886` row of its own — removing the generic term outright would
leave the gene with no location at all. Whether petB warrants a plasma-membrane
assertion independent of complex membership is recorded as a `suggested_question`.

## Boilerplate removed

The previous draft gave four annotations spanning two GO aspects — `GO:0022900` (BP),
`GO:0022904` (BP), `GO:0045275` (CC) and `GO:1902600` (BP) — verbatim-identical
summary and reason text. A complex-membership term and a proton-transport term do not
share a justification, and the identical text concealed both the parent/child
redundancy in the BP pair and the fact that `GO:1902600` is petB-specific in a way it
is not for the other two subunits. Each now carries a term-specific justification and
its own supporting evidence.
