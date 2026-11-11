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

## Second IBA-curation pass (family/PTN framework) 2026-08-31

### Family review created

`interpro/panther/PTHR24351/PTHR24351-review.yaml` (FamilyReview schema, DRAFT),
deliberately scoped to the PAINT nodes backing this gene's three IBA rows:

- **PTN008614469 / GO:0004674** (paint snapshot 20241120): assessed **SOUND**.
  Ser/Thr kinase activity is the defining function of the whole AGC/S6-kinase
  clade; the node is seeded by many experimentally characterized active kinases
  (human S6K1/S6K2/RSK1/MSK1/MSK2, rodent, fly, fungal, Dictyostelium,
  Plasmodium, plant). No pseudokinase among the seeds, nothing to prune.
- **PTN008614470 / GO:0005737** (snapshot 20260828, taxon Eukaryota): **SOUND**.
  Cytoplasm is the default compartment for these soluble kinases; target has no
  targeting features that contradict it.
- **PTN008614470 / GO:0005634** (snapshot 20260828): **UNRESOLVED** — nuclear
  activity is genuine for shuttling members (RSK/MSK) and the fungal seeds, but
  it is the least conserved of the propagated properties and there is no
  target-specific confirmation; retained for lack of counter-evidence, not
  positively established. This does not change the gene-level ACCEPT.

### Residue verification (all positions checked against real sequences)

Family residue site `PANTHER:PTHR24351#catalytic_core`, anchored on human S6K1
(UniProtKB:P23443, sequence version 2), from its live UniProt feature table:
VAIK beta-3 Lys **K123** (BINDING 123, ATP) and HRD catalytic Asp **D218**
(ACT_SITE 218, proton acceptor). Positive controls: S6K1 K123; RSK1 (Q15418)
N-terminal-domain HRD Asp D187 (ACT_SITE 187). No negative controls exist —
no documented pseudokinase in this family — so the site's `required_for`
strength is recorded as CONTRIBUTES (the validator requires a negative control
for REQUIRED, and inventing one would be fabrication).

Target A0A8J1IYX6 (sequence version 1) **retains the full catalytic
machinery**: Gly-rich loop GEGTGGKV at 120-127; VAIK **K142** (its own UniProt
BINDING 142 ATP feature; motif VAIKIV at 139); HRD catalytic Asp **D235**
(IHRDLKPDN at 232); DFG Asp **D253** (ICDFG at 251). The DFG position is not
part of the machine-checked site (not an explicit UniProt feature on the S6K1
anchor) but is recorded here and in the family-review notes.

### Gene review changes

- Added structured `review.propagation_review` to all three IBA rows:
  - GO:0004674: `root_cause: NO_FAILURE_CORE`; sources = node PTN008614469 +
    inspected seeds P23443/Q15418/O75582/Q8I4W3, all SUPPORTS_TRANSFER; two
    RETAINED `residue_claims` citing `PANTHER:PTHR24351#catalytic_core`
    (K123→K142 via UNIPROT_FEATURE on both records; D218→D235 via
    motif-anchored MSA). The target is not in its own WITH/FROM (it is
    uncharacterized), so no self-source question arises.
  - GO:0005634, GO:0005737: `root_cause: NO_FAILURE_NON_CORE`; node + seed
    sources SUPPORTS_TRANSFER; `residue_claims_not_applicable` (localization is
    not a point-residue question).
- Actions unchanged (all three IBAs remain ACCEPT); the GO:0004674 reason now
  cites the family-level inspection and retained catalytic residues.
- Seed identities verified against live UniProt: Q582V7 = T. brucei putative
  Ser/Thr kinase; Q8I4W3 = P. falciparum "RAC-beta" (Akt-like) kinase;
  G9BWQ1 = pig AKT1 (appears in the GOA WITH/FROM for the two CC rows but not
  in the cached paint.tsv seed lists, which postdate it; family review copies
  seeds from paint.tsv as the source of record).

### Omitted as unestablishable

- No PANTHER subfamily (:SF) placement for the target — its UniProt record
  carries only the family-level xref (`DR PANTHER; PTHR24351; ...; 1.` with no
  SF line), so the family review asserts no subfamilies rather than guessing.
- GO:0005634 could not be scoped to named subfamilies for the same reason
  (term_assessment scope UNRESOLVED).
- `interpro/panther/panther-members.tsv` not refreshed (shared file; orchestrator
  runs it once) — a missing-member warning for P23443/Q15418 is expected.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 files were not opened. New analysis: `A0A8J1IYX6-bioinformatics/`
(`compare_agc_rereview.py`, `tree_agc_rereview.py`, `RESULTS-rereview.md` and
captured outputs). No existing files in that folder were overwritten; the folder
is new.

### Identity

- Complete 424-aa product (UniProt sequence version 1, not flagged as a fragment).
  It is not an isoform, fragment or alternative model of another gene.
  X. tropicalis has separate prkcd (A0A6I8SIW5, 683 aa) and prkcq (A0A8J0S8T2,
  699 aa) genes. Over the catalytic region the target is about 41% identical to
  each, while frog prkcd vs human PRKCD is 88.5%.
- **Correction to the 2026-08-29 entry:** PANTHER PTHR24351 is *not* "the S6K
  branch outside PKC". Its member list (`PTHR24351-entries.csv`) includes every
  human PKC (PRKCA/B/G/D/E/H/Q/I/Z), PKN1-3, AKT1-3 and SGK1-3 as well as the
  S6K/RSK/MSK kinases. The family name is only a label. The InterPro API
  confirms PTHR24351 (42-416, E=1e-110) with no :SF subfamily.
- The kinase domain is PKC-like. Best pairwise matches are PRKCQ 42.7% and PRKCD
  41.0%, followed by the other PKCs (36-38%); FunFam calls it "Protein kinase C".
  In an NJ tree (RSKR excluded) the target branches at the base of the PKC + PKN
  clade, outside the delta/theta ortholog clades. With RSKR included, the two
  long branches pair. RSKR is in PTHR24355, so this is read as long-branch
  attraction.
- So the RefSeq "PKC delta" name is half right: the kinase domain is PKC-like,
  but the protein is not PKC delta and has no C1/C2 domains. The conclusion that
  PRKCD biology must not be transferred still stands.
- Residues: K142, D235 and D253 are retained. The PKCdelta activation-loop T507
  aligns to **G269**, so the PDK1 phospho-acceptor is lost. No hydrophobic motif
  is recognisable in the C-terminal tail. Activity and regulation are untested.

### Changes

- description rewritten (PKC-like AGC kinase, correct PANTHER scope, lost
  activation-loop Thr, separate prkcd/prkcq genes).
- GO:0005634 nucleus IBA: ACCEPT -> KEEP_AS_NON_CORE. The node assessment is
  UNRESOLVED in the family review, nuclear activity is branch-specific in
  PTHR24351, and the target is not in the RSK/MSK or fungal lineages that
  supply the nuclear evidence. It is no longer in core_functions locations.
- GO:0005737 cytoplasm IBA: ACCEPT (rationale rewritten).
- GO:0004674 IBA + IEA: ACCEPT. The note about the activation-loop G269 was
  added to the reason. Keyword quotes ("Serine/threonine-protein kinase", a KW
  label) were replaced with PROSITE signature quotes and a quote from
  RESULTS-rereview.md.
- GO:0000166, GO:0004672, GO:0016301, GO:0016740: MARK_AS_OVER_ANNOTATED ->
  TOO_GENERAL. These terms are true but entailed by GO:0004674 or GO:0005524,
  which is what TOO_GENERAL means.
- GO:0005524 ATP binding: KEEP_AS_NON_CORE (the "ATP-binding" keyword quote was
  dropped).
- References: GO_REF:0000033 and the deep-research and UniProt findings were
  corrected for PANTHER scope. A reference_review was added to the UniProt file,
  and RESULTS-rereview.md was added as a reference. No reference was removed.
  The deep-research file is kept but no longer cited as support.
- Added suggested_questions and suggested_experiments. No NEW annotations were
  added, because nothing gene-specific supports any process term.

### Relative and family

- No characterized ortholog exists. By the tree, the nearest characterized
  relatives are the PKC/PKN clade, and the closest by identity within it are the
  novel PKCs. Nominated relative: human PRKCQ (Q04759), family_member, with
  PRKCD (Q05655) essentially tied. Neither has a review in the repo (only
  `genes/human/PRKCH__C0HM02`).
- Family review disagreement: `interpro/panther/PTHR24351/PTHR24351-review.yaml`
  describes the family as the S6K/RSK/MSK/Akt/SGK/Sch9 clade and omits the PKC
  and PKN members. Its notes reject the codex framing of "PKC-delta-related
  kinase architecture", relying on the 2026-08-29 gene-review claim of
  "S6K-family placement". That claim is wrong for the kinase domain; the
  rejection should be revisited. The family review was not edited, because it
  is shared.
- Modules: none apply. `gpcr_plc_calcium_pkc_signaling.yaml` concerns
  DAG/Ca2+-activated PKCs, and this protein lacks C1/C2.
  `insulin_receptor_signaling.yaml` uses PTHR24351 only for AKT.
