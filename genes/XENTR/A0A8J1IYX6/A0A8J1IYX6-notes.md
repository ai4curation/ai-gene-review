# A0A8J1IYX6 (LOC101732819) — notes

## Re-review 2026-08-29

### Key finding: protein misidentification in the prior review

The prior review (and the falcon deep-research report it relied on) described this
protein as a PKCdelta (PRKCD) ortholog. That identity derives solely from the
RefSeq-derived UniProt SubName "Protein kinase C delta type"
(ECO:0000313|RefSeq:XP_031749696.1), an automated name. The actual evidence
contradicts it:

- **Domain architecture** (UniProt features): 424 aa; disordered N-terminal region
  (~1-103, basic/acidic-rich), single protein kinase domain (113-366), AGC-kinase
  C-terminal domain (367-424). **No C1 (DAG-binding) or C2-like domains** — the
  regulatory domains that define PKC family kinases, including PKCdelta (~676 aa).
- **PANTHER family**: `PANTHER; PTHR24351; RIBOSOMAL PROTEIN S6 KINASE` (verified
  against `interpro/panther/panther.obo`), i.e. the RSK/MSK/S6K branch of AGC
  kinases, not the PKC family.
- **IBA WITH/FROM donors** (GOA rows, GO_REF:0000033): for GO:0004674 the donors
  include UniProtKB:Q15418 (RPS6KA1), O75582 (RPS6KA5/MSK1), O75676 (RPS6KA4/MSK2),
  P23443 (RPS6KB1/S6K1), Q9UBS0 (RPS6KB2/S6K2), SGD/PomBase/dictyBase/Arabidopsis
  S6-kinase-family genes — all from the S6-kinase family tree (nodes PTN008614469,
  PTN008614470), none from PKC.
- The falcon deep-research report itself states: "no studies were identified that
  specifically investigated LOC101732819"; all its PKCdelta content is transferred
  mammalian PRKCD literature keyed off the SubName.

Note X. tropicalis has a separate genuine prkcd gene; LOC101732819's RefSeq name
appears to be an automated naming artifact.

### Changes made in the re-review

- **description**: rewritten. Removed all PKCdelta biology (C1A/C1B, C2-like
  domain, DAG activation, caspase-3 cleavage/NLS story); now describes an
  uncharacterized AGC-group kinase of the ribosomal protein S6 kinase family,
  with the name discrepancy noted factually.
- **GO:0005634 nucleus (IBA)**: action changed KEEP_AS_NON_CORE -> ACCEPT. The
  prior non-core call rested on PKCdelta-specific reasoning (nuclear entry only
  after caspase cleavage). For this uncharacterized S6K-family kinase the PAINT
  placement (nucleus + cytoplasm, is_active_in) is the best available evidence and
  is consistent with nuclear-acting family members (RSK/MSK); no target-specific
  evidence argues against it.
- **GO:0005737 cytoplasm (IBA)**, **GO:0004674 (IBA)**: actions unchanged
  (ACCEPT), summaries/reasons rewritten to family-based rationale.
- **IEA terms** (GO:0000166, GO:0004672, GO:0016301, GO:0016740 over-annotated;
  GO:0004674 IEA ACCEPT; GO:0005524 KEEP_AS_NON_CORE): actions unchanged — those
  judgments are identity-independent and sound; wording de-PKCdelta-ized.
- **supported_by**: removed all quotes from the deep-research file (they describe
  PKCdelta, not this protein); replaced with verbatim UniProt-record quotes.
- **references**: deep-research file entry now carries a `reference_review`
  (relevance: LOW, correctness: MISCITED) documenting the identity problem;
  findings for the file references updated accordingly.
- **core_functions**: description rewritten (S6K-family kinase, substrates
  unknown); kept GO:0004674; locations now cytoplasm + nucleus (both IBA-accepted).

### Deliberately unchanged

- GOA-sourced term ids/labels/evidence rows: all 9 GOA rows have matching
  existing_annotations entries; untouched per policy.
- The falcon deep-research file itself (auto-generated, do-not-edit); flagged via
  reference_review instead.
- gene_symbol LOC101732819 (no HGNC-style symbol exists for this locus).
- No new annotations proposed: with zero gene-specific literature, anything beyond
  the PAINT/IEA inferences would be speculation.
