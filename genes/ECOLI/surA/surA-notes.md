# surA (SurA) — *Escherichia coli* K-12

## 2026-08-29 carrier-holdase consistency review

The current GOA contains 30 qualifier-aware physical signatures, all represented
exactly once in `surA-ai-review.yaml`: 13 `enables`, 11 `involved_in`, five
`located_in`, and one `is_active_in`. The review also contains one author-supplied
NEW molecular-function proposal. No physical GOA row was deleted or rewritten.

### GO:0140309 decision

GO:0051082 is obsolete. The earlier review hesitated between GO:0044183 and
GO:0140309 because SurA moves within the periplasm rather than between compartments.
That is not a requirement of GO:0140309: the project records that its definition
requires escort "to an acceptor molecule or to a specific location"
[`projects/UNFOLDED_PROTEIN_BINDING.md`]. BAM/YaeT is a defined acceptor molecule
for SurA-delivered unfolded OMP clients.

The direct cached evidence supports both components of this interpretation. SurA
"prevents FhuA from misfolding by stabilizing a dynamic, unfolded state"
[PMID:26344570], and it is "responsible for the periplasmic transit of the bulk mass
of OMPs to the YaeT complex" [PMID:17908933]. These records are abstract-only, so
the review makes no claims beyond their explicit text. The three physical GO:0051082
rows are therefore MODIFY to GO:0140309, and the former author NEW GO:0044183 row is
replaced by NEW GO:0140309. GO:0044183 is not asserted as the primary MF because the
carrier-holdase term describes the observed mechanism more specifically.

### PAINT provenance

All four IBA rows in GOA cite PANTHER:PTN005352065 and include P0ABZ6 itself among
their WITH/FROM sources. Target self-seeding is legitimate because direct SurA
evidence grounds the ancestral assertion; it is not circular. Current cached PAINT
for PTHR47637 retains at PTN005352065 only GO:0006457 protein folding, GO:0003755
PPIase activity, and GO:0030288 periplasmic localization, all seeded by P0ABZ6
[`interpro/panther/PTHR47637/PTHR47637-paint.tsv`]. Those three IBAs remain ACCEPT
with `NO_FAILURE_CORE`. GO:0051082 is absent from current PAINT, so its old GOA IBA
is recorded as `SOURCE_STALE_OR_MISSING` and MODIFY to GO:0140309 using independent
direct evidence.

### Other row-level decisions

The five GO:0005515 IPI rows are true observed interactions with OmpF, BamA/YaeT,
or BamB and have no contradictory evidence. They are retained as KEEP_AS_NON_CORE
rather than removed merely because `protein binding` is uninformative. Broad parent
or supporting IEAs (isomerase activity, peptide binding, and periplasmic space)
are also retained as non-core. Protein stabilization remains ACCEPT across IEA and
direct IMP rows because direct experiments establish stabilization of OMP clients.
Direct folding, OMP assembly, PPIase, maintenance-of-unfolded-protein, and localization
annotations also remain accepted.

## PR #2732 feedback resolution

Rechecked after the carrier-holdase policy clarification was merged through PR #2733.
The project now explicitly defines GO:0140309 carrier-holdase activity as escort to
a specified location or acceptor molecule, includes delivery within one compartment
when an acceptor such as BAM/YaeT is demonstrated, and lists SurA as an example.
The gene review is consistent with that policy and contains no remaining dependency
on the older cross-compartment interpretation or the former "unfolded protein carrier
activity" label.

The NEW GO:0140309 evidence boundary is now explicit. PMID:26344570 is the IDA basis:
it directly demonstrates stabilization of a dynamic unfolded FhuA state and stepwise
β-hairpin insertion. PMID:17908933 independently corroborates the carrier endpoint by
showing periplasmic OMP transit to YaeT/BAM and direct SurA-YaeT interaction. Neither
abstract is made to support the other's experimental component. The core quote now
preserves the cached publication's Greek `β` characters verbatim.

The stale GO:0051082 IBA remains classified `SOURCE_STALE_OR_MISSING` because current
PTHR47637 PAINT lacks that node assertion. The former `SOURCE_EVIDENCE_WEAK` subtype
was removed: absence from current PAINT establishes staleness, not weakness of the
historical source evidence, and the GO:0140309 replacement rests on independent direct
SurA experiments rather than reinterpretation of that retired node claim.
