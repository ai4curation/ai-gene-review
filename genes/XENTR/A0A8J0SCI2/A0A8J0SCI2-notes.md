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

## Family/PTN curation pass (2026-08-31)

Second IBA-curation pass using the FamilyReview framework. Created
`interpro/panther/PTHR24381/PTHR24381-review.yaml` (family "ZINC FINGER PROTEIN",
verbatim from panther.obo; preferred name "Krueppel C2H2-type zinc-finger family")
and added structured `review.propagation_review` blocks to all four IBA rows here.

### What was inspected

All four IBA rows (GO:0005634 is_active_in, GO:0006357, GO:0000981, GO:0000978)
are backed by the single PAINT node **PANTHER:PTN001225435** (taxon:6072,
Eumetazoa, in `PTHR24381-paint.tsv`); the GOA WITH/FROM seed lists match the
paint.tsv IBD rows exactly. All four node assertions were assessed **SOUND** in
the family review:

- GO:0005634 (snapshot 20260529): 39 experimentally annotated eumetazoan seeds;
  spot-checked mouse Zfp932 (MGI:1916754 = UniProtKB:E9QAG8) IDA nucleus
  (PMID:21177534) in QuickGO.
- GO:0000978 (snapshot 20200709): single-seed IBD from Zfp932 — not weak support
  per the project's phylogenetic reading; the seed has IDA GO:0000978 from two
  papers (PMID:21177534, PMID:22391310). The family's one documented loss of
  cis-regulatory-region binding (ZNF445 clade, IRD negating GO:0000976 at
  PTN008615686) was pruned by PAINT at its own node and does not implicate this
  one.
- GO:0000981 (snapshot 20250904): seeds span both regulatory directions (ZNF300
  IDA GO:0001228; ZNF140 IDA GO:0001227), so the direction-agnostic parent at the
  node is the correct generalization — consistent with this review's NPI verdict
  on ProtNLM2's GO:0001228 prediction for this effector-less protein.
- GO:0006357 (snapshot 20260529): 13 seeds, again both directions (ZNF300 IDA
  GO:0045944; ZNF140 and Zfp932 IDA GO:0000122).

Seed identities verified against live UniProt REST / Alliance / mygene.info;
seed experimental annotations checked in QuickGO; no identity or label was
written from memory. All existing actions (ACCEPT ×3, KEEP_AS_NON_CORE for
GO:0000978) were **kept unchanged** — the family-level inspection confirms them.
Root causes: NO_FAILURE_CORE ×3, NO_FAILURE_NON_CORE for GO:0000978 (non-core
because the binding term is the mechanistic component of GO:0000981, not because
the propagation is doubted). No failure_modes. The target does not appear in any
WITH/FROM (it has no experimental annotations), so no self-source handling was
needed.

### Residue claims

`residue_claims_not_applicable` set on all four rows: every argument rests on the
intact repeated architecture of 8 tandem C2H2 fingers (residues 37-260), not on
any single anchorable position, and the family review deliberately defines no
`residue_sites` (a point-residue site for a modular zinc-finger array would
fabricate precision the biology does not have).

### Family review scope notes

Family review is deliberately scoped: only PTN001225435 assessed (of 16
PAINT-annotated nodes), only subfamily SF440 ("OOCYTE ZINC FINGER PROTEIN
XLCOF7.1-LIKE", the target's subfamily per its UniProt PANTHER xref) described.
Term assessments: GO:0005634/GO:0000981/GO:0006357 FAMILY_WIDE; GO:0000978
SUBFAMILY_ONLY with an explicitly non-exhaustive applicable list ([SF440]),
since the ZNF445-clade IRD proves it is not family-wide. Representative members
A0A8J0SCI2 and P18752 are not yet in `panther-members.tsv` (index refresh left
to the orchestrator), so `validate-families` reports two acceptable UNRESOLVED
membership lines.

### Addendum (2026-08-31): SF440 membership withdrawn after member-index refresh

After the orchestrator ran `just refresh-panther-members`, the refreshed
`interpro/panther/panther-members.tsv` (resolved live against the current PANTHER
release) reclassifies both proteins this pass had placed in PTHR24381:SF440:
**A0A8J0SCI2 -> PTHR24377:SF929** and X. laevis XlCOF7.2 **P18752 ->
PTHR23226:SF391**. The cached `A0A8J0SCI2-uniprot.txt` still carries
`PTHR24381:SF440`; this is release drift between the cached/annotation release
and current PANTHER, not a curation error on either side.

Consequences applied to `interpro/panther/PTHR24381/PTHR24381-review.yaml`:
the SF440 subfamily entry (with both representative members) was removed rather
than re-pointed ("assert no id you cannot be sure of"; re-assigning the proteins
to PTHR24377/PTHR23226 would be an evolutionary-placement judgment not made
here), and the GO:0000978 term assessment was rescoped from SUBFAMILY_ONLY
[SF440] to **UNRESOLVED**, with the drift and the still-valid facts (not
family-wide because of the ZNF445-clade IRD; sound at PTN001225435) recorded in
its scope_reason.

The four IBA rows and their propagation_review blocks here are unaffected: the
GOA WITH/FROM cites PANTHER:PTN001225435, a node in PTHR24381's cached PAINT
slice, so the annotations under review descend from PTHR24381's tree as of the
annotation release, and the node assessments stand. This gene review's text
never claimed SF440 membership, so no gene-review wording needed softening.
