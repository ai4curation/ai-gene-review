# A0A8J0SCI2 notes

## Re-review (2026-08-29)

Systematic re-review of `A0A8J0SCI2-ai-review.yaml` against the GOA tsv, UniProt
record, deep-research (falcon) file, ProtNLM predictions review, and the
OpenScientist hypothesis analysis.

### GOA coverage

All 5 GOA rows have matching `existing_annotations` entries (term id +
evidence_type + reference + qualifier):

1. GO:0005634 nucleus, IBA, GO_REF:0000033, is_active_in — ACCEPT (kept)
2. GO:0006357 regulation of transcription by RNA Pol II, IBA, GO_REF:0000033 — ACCEPT (kept)
3. GO:0000981 DNA-binding TF activity Pol II-specific, IBA, GO_REF:0000033 — ACCEPT (kept)
4. GO:0000978 Pol II cis-regulatory region sequence-specific DNA binding, IBA, GO_REF:0000033 — KEEP_AS_NON_CORE (kept; defensible: the binding activity is the mechanistic component of the core TF activity GO:0000981)
5. GO:0005634 nucleus, IEA, GO_REF:0000044, located_in — ACCEPT (kept)

No GOA rows are missing from the review. (The UniProt DR lines additionally list
GO:0008270 zinc ion binding and GO:0006351 DNA-templated transcription as
IEA:UniProtKB-KW, but these are not in the GOA tsv and were not added; zinc
binding is a structural feature of the C2H2 fold rather than an informative
function, and GO:0006351 is subsumed by GO:0006357.)

### Changes made in this re-review

1. **GO:0006357 summary** — removed the claim that the IBA was "inferred from
   characterized orthologs including Klf family members". The WITH/FROM donors
   (MGI/RGD entries and human UniProtKB accessions such as P52737, P52738,
   Q96CS4, Q96RE9, Q9HCX3) are classical C2H2/KZNF-type zinc finger proteins
   within PANTHER family PTHR24381 ("ZINC FINGER PROTEIN"); KLFs belong to a
   different PANTHER family. Replaced with neutral, verifiable wording.
2. **GO:0000981 summary** — the sentence explaining why ProtNLM2's GO:0001228
   (activator) prediction was scored NPI claimed it "was based on a phmmer hit
   to a KRAB-ZNF repressor". Neither the predictions-review file nor the
   OpenScientist analysis mentions phmmer; they attribute the error to
   over-specific transfer from KRAB-ZNF-like sequences (CATH FunFam
   assignments) for a protein that is an effector-less tandem zinc finger
   array. Reworded to match the actual documented rationale.
3. **GO:0000978 supported_by quote** — the deep-research quote omitted
   "(Zn²⁺)" present in the source text (line 192 of the falcon file), making
   it non-verbatim. Restored the verbatim wording.

Other deep-research quotes verify verbatim against the source once markdown
bold markers (`**`) are stripped; left unchanged since validation accepts them
and content is faithful.

### Checked and deliberately left unchanged

- **Description**: project-independent, no curation/workflow commentary; the
  TrEMBL/PE3 status statement is factual database context. Domain claims (8
  tandem C2H2 fingers, residues 37-260, N-terminal disordered region 1-27, no
  KRAB/SCAN/BTB) match the UniProt FT lines.
- **Actions**: all five are sound. IBA annotations sit at appropriate
  specificity (GO:0000981 neutral parent rather than activator/repressor
  child, consistent with the NPI verdict on ProtNLM2's GO:0001228).
- **core_functions**: terms are in correct branches (MF GO:0000981, BP
  GO:0006357, CC GO:0005634) and match the accepted annotations.
- **references**: GO_REF entries only; no PMIDs cited, so no reference_review
  adjudication was applicable (nothing to verify against cached publications).

Validation (`just validate XENTR A0A8J0SCI2`) passes after edits.
