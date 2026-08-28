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

Tsr4 clearly binds nascent Rps2 and promotes its solubility. However, curated
UniProt states that Tsr4 is released before Rps2 nuclear import, and current
evidence does not identify a direct acceptor, directional handoff, or escort by
Tsr4 to the nucleus. Consequently, GO:0140597 is not retained as core and
GO:0140318/GO:0140309 are not proposed. The direct GO:0140597 row and all three
obsolete GO:0051082 rows are instead MODIFY to GO:0044183, which captures the
experimentally demonstrated client-stabilizing chaperone activity without
inventing transport.

The core synthesis is therefore a cytoplasmic, Rps2-specific protein folding
chaperone whose activity supports ribosomal small-subunit biogenesis and SSU
rRNA maturation. Experiments that identify the immediate Rps2 acceptor and
demonstrate directional handoff would be needed before asserting carrier or
transporter activity.
