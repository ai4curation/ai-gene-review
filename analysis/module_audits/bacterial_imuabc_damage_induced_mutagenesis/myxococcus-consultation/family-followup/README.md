# PTHR45900 follow-up after ImuA identity resolution

The current UniProt record classifies Q1D5A2/MXAN_3991 in PTHR45900:SF1.
The primary sequence bridge in the frozen parent consultation establishes that
this protein is experimentally studied M. xanthus ImuA. The earlier family
review's inventory covered reviewed UniProt members; it did not justify universal
claims over current family membership including this unreviewed entry.

## Judgments

- GO:0140664 changes from FAMILY_WIDE to UNRESOLVED. Its definition requires
  recognition of toxic DNA structures and initiation of ATP-driven signaling.
  Canonical RecA sensing remains supported. ImuA DNA binding, ATP hydrolysis and
  inhibition of RecA1 do not establish ImuA LexA co-protease signaling. They also
  do not establish that this activity is absent, so a negative member exception
  would overstate the evidence.
- Explicit UNRESOLVED family-scope assessments for strand exchange and
  recombinational repair prevent an unsupported universal grant. This retains
  positive canonical RecA evidence and does not deny ImuA an unassayed activity.
- Family coherence changes to MOSTLY_COHERENT and SF1 includes the identified
  accessory protein alongside its canonical representatives. ImuA has positive
  DNA-binding and ATPase evidence; it is not described as globally inactive.
- All five existing PAINT node identifiers, seeds, assertions and verdicts are
  unchanged. Their reasoning is bounded to the existing tree. The Q1D5A2 leaf is
  absent from the cached tree, so no PTN placement, loss event or pruning is invented.
- The pre-existing Pol V and endonuclease term assessments remain unchanged.

`baseline.json` freezes the original family review and source hashes and retains
the exact 18-file gene consultation manifest. `preserve.py` checks those files,
source bytes, original references, canonical subfamilies, original representative
members, PAINT node assertions/verdicts, and the two unchanged term assessments.
It does not judge scientific truth. The cited primary literature and frozen
identity analysis provide the biological basis.

The family/gene cross-check has zero conflicts but also zero consistent claims
to count after removal of an unsupported family-wide grant. It is not an
independent assay-coverage test. The representative membership validator initially
reports the new accession as not indexed; its current UniProt PANTHER cross-reference
is quoted as independent classification evidence. No reassignment was made to
resolve an indexing limitation.
