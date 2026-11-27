# vreR (PA0676, O69006) — review notes

Tier-3 PseudoCAP review. `vreR` is the sigma factor regulator of the PUMA3 cell-surface
signalling system, chosen for this batch as a second instance of the architecture in which
batch 4 found annotations transposed between components.

## The system

PA0674-PA0675-PA0676 = VreA (receptor) - VreI (sigma) - VreR (regulator). `vreI` is already
merged in the corpus; `vreA` has no folder. So after this review PUMA3 is two-thirds covered,
as the Fem system is.

`[PMID:19730690 "They generally consist of a TonB-dependent outer membrane receptor, a sigma factor regulator (or anti-sigma factor) in the cytoplasmic membrane, and an extracytoplasmic function (ECF) sigma factor."]`

PUMA3 is unusual twice over. Its regulon is virulence rather than iron uptake —
`[PMID:19730690 "we have identified a novel system involved in the regulation of virulence"]`
— and its receptor is atypical:
`[PMID:19730690 "the receptor component which is considerably smaller than that of other CSS outer membrane receptors and lacks a beta-barrel domain"]`.
Neither bears on vreR's own annotations, but both are why the paper exists.

## No transposition here

The batch-4 femA/femI finding was a swap between a transducer and a sigma factor from one
paper. vreR was reviewed partly to see whether the same pattern recurs in a second system.
**It does not.** vreR has only two rows, both describing a sigma factor regulator, and both
are right for this protein: nothing from this paper has landed on the wrong component. Worth
stating as a negative result rather than leaving unsaid — the femA/femI exchange looks like a
specific accident with the three adjacent, one-letter-apart `fem` symbols, not a systematic
failure in how these systems were curated.

## The record

319 residues, FecR family, and transmembrane:

- `[file:PSEAE/vreR/vreR-uniprot.txt "DR   Pfam; PF04773; FecR; 1."]` and
  `[file:PSEAE/vreR/vreR-uniprot.txt "DR   InterPro; IPR032623; FecR_N."]` — the FecR_N/FecR
  pair is the domain architecture the merged `foxR` and `PA0471` reviews both cite as
  identifying a cell-surface-signalling anti-sigma factor.
- `[file:PSEAE/vreR/vreR-uniprot.txt "DR   InterPro; IPR012373; Ferrdict_sens_TM."]`
- `KW Transmembrane {ECO:0000256|SAM:Phobius}` — a sequence-analysis feature, which the
  project rules count as valid computational evidence, and it fits the cytoplasmic-membrane
  position the paper describes for this component.
- `PE   4: Predicted`, recorded as a limit on the rows rather than cited for an ACCEPT.

## `GO:0016989` and the house style

`GO:0016989 sigma factor antagonist activity` (IMP) is `ACCEPT`, matching the merged `foxR`
and `PA0471` reviews, which accept the same term on the same reasoning — the FecR_N/FecR
architecture of cell-surface-signalling anti-sigma factors.

`GO:0045892 negative regulation of DNA-templated transcription` (IEA, `GO_REF:0000108`,
derived from `GO:0016989`) is `MODIFY` → `GO:2000143 negative regulation of DNA-templated
transcription initiation`, again matching `foxR` and `PA0471` verbatim. Verified in OLS:
`GO:2000143` is a child of `GO:0045892`, and it is the mirror of the `GO:2000142` that the
cognate sigma-factor reviews accept.

Note the contrast with `femI`, where I used `TOO_GENERAL` on a general regulation term rather
than `MODIFY`. The two are different situations and the distinction is deliberate: femI
already carried `GO:2000142` as its own accepted row, so the specific term was asserted
elsewhere in the review and there was nothing to propose. vreR carries no `GO:2000143` row, so
the specific term has to be proposed, which is what `MODIFY` is for.

## An ontology gap: the activator half of the function

The paper's most interesting statement about this protein is that its role is **dual**:

`[PMID:19730690 "Furthermore, the sigma factor regulator both inhibits the function of the ECF sigma factor and is required for its activity."]`

`GO:0016989` captures only the inhibition. There is no GO term for the other half. Searched in
OLS: GO carries `GO:0016987` sigma factor activity, `GO:0016989` sigma factor antagonist
activity, `GO:0043856` anti-sigma factor antagonist activity (for proteins that inhibit an
anti-sigma), `GO:1903865` sigma factor antagonist complex and `GO:0045152` antisigma factor
binding — a term for every other role in these systems, and **nothing for a protein that is
required for a sigma factor's activity**.

PANTHER's own name for this family says the same thing from the other direction:
`[file:PSEAE/vreR/vreR-uniprot.txt "DR   PANTHER; PTHR30273; PERIPLASMIC SIGNAL SENSOR AND SIGMA FACTOR ACTIVATOR FECR-RELATED; 1."]`
— the family is named for the activator role that GO cannot express.

Recorded as a `proposed_new_terms` entry, which is where the project rules put an ontology
gap, with a second `core_functions` entry using `proposed_molecular_function` so the protein's
two activities are both represented. This is not a `NEW` annotation: there is no term to
annotate to, and inventing an id would be exactly the hallucination the rules warn against.

The gap is a general one, not specific to vreR. FecR itself is the paradigm, and the merged
`foxR` and `PA0471` reviews carry the same single-sided encoding without remarking on it, so
if the term is created those two would merit the same addition.
