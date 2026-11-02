# TSR4 annotation re-review notes

## 2026-08-28 dedicated re-review

TSR4 (P25040; SGD:S000005382) encodes a cytoplasmic dedicated chaperone
for ribosomal protein Rps2/uS5. Two independent 2019 studies identify the same
client relationship. Rössler et al. report direct Tsr4-Rps2 binding and in-vitro
solubility promotion [PMID:31062022, "We report the identification of Nap1 and
Tsr4 as direct binding partners of Rps6 and Rps2, respectively. Both factors
promote the solubility of their r-protein clients in vitro."]. Black et al.
independently report cotranslational association and the Rps2 N-terminal
determinant [PMID:31182640, "Here, we report that Tsr4 cotranslationally
associates with Rps2. Rps2 harbors a eukaryote-specific N-terminal extension
that is critical for its interaction with Tsr4."]. Both cached publications are
abstract-only, so the review uses only claims stated in those abstracts or in
the curated UniProt record and does not invent inaccessible assay details.

### GOA reconciliation

The cached GOA has 15 physical rows and 15 distinct qualifier-aware signatures
(qualifier + GO term + evidence code + reference). All are positive relation
qualifiers (`enables`, `involved_in`, or `located_in`); there are no NOT or
isoform-specific rows. The IGI small-subunit-biogenesis row has WITH/FROM
`SGD:S000003091` (RPS2), matching the experimentally defined client. The single
IBA row has WITH/FROM `PANTHER:PTN000958897|SGD:S000005382`.

### PAINT provenance

The sole IBA is GO:0030490 maturation of SSU-rRNA at
`PANTHER:PTN000958897`. The current local PAINT snapshot contains neither a
PTHR47524 family directory/table nor a record for PTN000958897, although the
official PANTHER ontology resolves PTHR47524 as "20S RRNA ACCUMULATION PROTEIN
4." The propagation review therefore records `SOURCE_STALE_OR_MISSING` for the
unrecoverable current node assertion. This is not a biological rejection of the
IBA: the target itself is the experimental seed, which is valid rather than
circular, and direct target evidence supports SSU-rRNA maturation
[PMID:19806183, "We experimentally evaluated >100 candidate yeast genes in a
battery of assays, confirming involvement of at least 15 new genes, including
previously uncharacterized genes (YDL063C, YIL091C, YOR287C, YOR006C/TSR3,
YOL022C/TSR4)."].

### Chaperone versus carrier semantics

Live QuickGO definitions were checked on 2026-08-28:

- GO:0051082 is obsolete.
- GO:0044183 protein folding chaperone means binding a protein or complex to
  assist protein folding.
- GO:0140597 is now labelled protein carrier activity and requires delivery to
  an acceptor molecule or specific location.
- GO:0140318 protein transporter activity specifically requires delivery to a
  cellular location.
- GO:0140309 unfolded protein holdase activity additionally requires an unfolded
  client to be escorted to an acceptor or location.

Tsr4 clearly binds nascent Rps2 and promotes its solubility. GO:0140597 is
retained as the core activity because it is a recent, directly curated IDA and
the abstract-only cache is insufficient to overrule the curator's full-text
assessment. This is also consistent with NAP1 and the dedicated ribosomal-
protein-chaperone cohort. GO:0140318/GO:0140309 were not newly proposed in the
initial 2026-08 review. The three obsolete GO:0051082 rows were initially marked
MODIFY to GO:0044183 to preserve their client-stabilizing, anti-aggregation facet
alongside the separately curated GO:0140597 carrier annotation; the 2026-10 PR
follow-up below revisits that choice in light of the YAR1 precedent and the new
Pse1 handoff paper.

The core synthesis is therefore a cytoplasmic, Rps2-specific protein carrier
chaperone whose activity directly supports ribosomal small-subunit biogenesis;
SSU-rRNA maturation is retained as a downstream annotated consequence.

## 2026-10-01 current GOA and PAINT refresh

- Forced a fresh GOA/UniProt pull for TSR4. Current GOA has 14 live rows; exact row
  parity required retiring the stale GO_REF:0000043 ribosome-biogenesis IEA row and the
  three obsolete `GO:0051082 unfolded protein binding` rows, then accepting the two new
  SGD IPI rows to `GO:0044183 protein folding chaperone` and the derived
  `GO:0006457 protein folding` IEA row.
- Added GOA's explicit qualifiers and `WITH/FROM` support entities to the live rows. The
  only IBA row still traces to `PANTHER:PTN000958897|SGD:S000005382`, and the
  target's own SGD seed remains valid descendant evidence rather than a circular support.
- Refetched the PTHR47524 family and PAINT cache. Unlike the August 28 review, the local
  cache now resolves `PANTHER:PTN000958897` and confirms the `GO:0030490 maturation of
  SSU-rRNA` IBD seeded by TSR4 itself, so the IBA propagation source is now classified as
  `SUPPORTS_TRANSFER` rather than `SOURCE_STALE_OR_MISSING`.
- Searched for 2023-2026 TSR4/Rps2/uS5 literature. PMID:37509163 was already covered by
  the Falcon report; PMID:42641886 is a new 2026 primary paper showing that the Rps2
  N-terminal extension integrates Tsr4 binding, Pse1 importin recognition, and arginine
  methylation. It reinforces the carrier-chaperone model and narrows the remaining
  handoff question, but it does not require a new GO action.

## PR #3804 holdase/foldase follow-up

- Re-checked the GO:0044183 and GO:0006457 decisions against the project's
  YAR1 precedent and the UPB carrier-holdase rules. Tsr4's cached abstracts
  support cotranslational Rps2 binding and solubility, and PMID:42641886 adds
  Pse1 as a defined competitor for the same Rps2 N-terminal extension, but no
  accessible evidence shows that Tsr4 actively folds Rps2.
- Changed the two live SGD GO:0044183 IPI rows from ACCEPT to MODIFY with
  `GO:0140309 unfolded protein holdase activity` as the replacement, and
  changed the three retired GO:0051082 rows to the same replacement.
- Removed the GO_REF:0000108 `GO:0006457 protein folding` row because it is a
  logical consequence of the broad GO:0044183 edge; TSR4's process context is
  Rps2 handoff into nuclear import and 40S biogenesis rather than a demonstrated
  direct protein-folding step.
- Tightened the core molecular function from parent `GO:0140597 protein carrier
  activity` to child `GO:0140309 unfolded protein holdase activity`.
