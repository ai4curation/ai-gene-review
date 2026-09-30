# CpxP annotation review notes

## 2026-08-29 — dedicated annotation-reviewer audit

Audited all 11 qualifier-aware physical GOA signatures in `CpxP-goa.tsv` one-for-one.
The physical set contains six `enables`, two `located_in`, two
`acts_upstream_of_or_within`, and one `is_active_in` qualifiers. Evidence codes are
five IDA, two IBA, and one each of IEA, IPI, EXP, and ISM. The review also adds two
author-supplied NEW annotations, which are not part of the 11-row GOA reconciliation.

### Mechanistic synthesis

CpxP has two directly supported core roles. First, purified CpxP reduces CpxA
phosphorylation without changing its phosphotransfer or phosphatase activities
[PMID:17259177, "Purified tagless CpxP protein reduced the phosphorylation status
of CpxA to 50% but had no effect on CpxA phosphotransfer or phosphatase activities."].
Full-text interaction experiments further show dynamic CpxP-CpxA association and
stress-dependent release [PMID:25207645, "For the first time, we demonstrate physical
interaction between CpxP and CpxA in unstressed cells"]. GO:0030547, *signaling receptor
inhibitor activity*, is a current molecular-function term and captures the functional
consequence of the two generic protein-binding rows.

Second, CpxP is a DegP substrate adaptor. The cached abstract explicitly states that
it is required for effective proteolysis of a subset of misfolded substrates
[PMID:16303867, "CpxP functions as a periplasmic adaptor protein that is required for
the effective proteolysis of a subset of misfolded substrates by the DegP protease."].
GO:0140767, *enzyme-substrate adaptor activity*, therefore provides a current and
specific molecular-function annotation. The experimental evidence code is retained
as EXP, matching the source GOA row rather than inferring a stronger assay type from
an abstract-only cache. Because loss of CpxP prevents effective degradation in the
same study, the broad GO:0030162 row is modified to GO:0045862, *positive regulation
of proteolysis*. A second NEW annotation, GO:0070298 *negative regulation of
phosphorelay signal transduction system*, records the directly demonstrated CpxA
inhibition process represented in the core-function synthesis.

### GO:0051082 and chaperone interpretation

All three GO:0051082 rows remain `MARK_AS_OVER_ANNOTATED`. GO:0051082 is obsolete,
and CpxP's demonstrated misfolded-client recognition serves DegP proteolysis. The
structure paper proposes a substrate-recognition cleft
[PMID:21239493, "an extended hydrophobic cleft on the convex surface suggests a potent
substrate recognition site for misfolded pilus subunits"], while the direct full-text
comparison reports only weak chaperone activity
[PMID:21317898, "We found that CpxP has weak chaperone activity in vitro and CpxP
overproduction causes the accumulation of Im7 in otherwise wild-type strains"].
Neither establishes general aggregation prevention. No general holdase NTR is proposed
for CpxP, and GO:0140309 is not appropriate because carrier-like escort to an acceptor
or destination has not been demonstrated. This agrees with
`projects/UNFOLDED_PROTEIN_BINDING.md`, which lists CpxP as over-annotated and points
to CpxA inhibition rather than a holdase function.

### PAINT provenance

The PTHR38102 PAINT cache was retrieved through public wrappers on 2026-08-29 during
the paired Spy family review (`just fetch-panther-family PTHR38102` and
`just fetch-panther-paint PTHR38102 --extra-uniprot P77754`). Current PAINT contains
one IBD assertion at `PANTHER:PTN002445564`: GO:0030288, with descendant evidence
from CpxP (`UniProtKB:P0AE85`) and Spy (`UniProtKB:P77754`). Thus the GO:0030288 IBA
is a valid core localization transfer; CpxP appearing in its own WITH/FROM is expected
descendant evidence, not circularity. The historical GO:0051082 node assertion is
absent from current PAINT, so its node and both listed proteins are recorded as
`SOURCE_STALE_OR_MISSING`; direct CpxP biology is evaluated separately.

### Evidence limits and decisions

PMID:9473036, PMID:16303867, PMID:17259177, PMID:21239493, and PMID:21317318 are
abstract-only in the local cache. Their experimental annotations were not removed or
second-guessed beyond what their abstracts directly establish. PMID:21317898 and
PMID:25207645 have cached full text. The homodimer IPI and broad response-to-stress IDA
are retained as `KEEP_AS_NON_CORE`: both are supported, but neither states a direct
core mechanism. Final physical action counts are ACCEPT 3, KEEP_AS_NON_CORE 2,
MODIFY 3, MARK_AS_OVER_ANNOTATED 3, with no REMOVE, UNDECIDED, or PENDING rows. Two
separate NEW annotations capture GO:0140767 DegP adaptor molecular function and
GO:0070298 Cpx phosphorelay inhibition.
