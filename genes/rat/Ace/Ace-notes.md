# Ace (rat) review notes

## Session 2026-10-28

- `just fetch-gene rat Ace` resolved UniProt P47820 (ACE_RAT); 137 GOA rows.
- `just fetch-gene-pmids rat Ace` cached 36 PMIDs; PMID:19307186 cached with full text.
  All other GOA PMIDs are abstract-only except PMID:20122169.
- No deep-research provider available; literature synthesis is in
  `Ace-deep-research-manual.md` (manual, with inline provenance).

### Key decisions

- Core: peptidyl-dipeptidase activity (GO:0008241) on the cell-surface and soluble
  enzyme; angiotensin maturation (GO:0002003); bradykinin catabolic process
  (GO:0010815); RAS regulation of systemic arterial blood pressure (GO:0003081,
  GO:0003084). Rat-specific support: PMID:2172462 (CSF ACE converts Ang I and
  degrades bradykinin), PMID:20487892 (Met-enk-Arg-Phe cleavage), PMID:11299220
  (ACE is the main plasma kininase), PMID:10506486 (antisense lowers BP in SHR).
- GO:0008241 is_a exopeptidase activity only; it is not under metallopeptidase
  activity (checked in OLS), so GO:0008237 metallopeptidase activity is kept as
  ACCEPT (the metallo axis), not MODIFIED.
- GO:0004181 metallocarboxypeptidase activity (ISO from mouse IDA PMID:18158355,
  PMID:27649628): ACE is EC 3.4.15.1, not a single-residue carboxypeptidase; donor
  papers not read, so UNDECIDED rather than REMOVE.
- GO:0003779 actin binding (ISO from human P12821-1): no current human ACE
  annotation to actin binding found in QuickGO (query 2026-10-28), so the donor
  is stale; MARK_AS_OVER_ANNOTATED.
- Human donor sources (QuickGO): MAPKK/MAPK binding IPI PMID:14615289 (MKK7/JNK,
  outside-in signalling); bradykinin receptor binding IPI and arachidonate
  secretion IDA PMID:17077303; lysosome IDA PMID:11076943; endosome IDA
  PMID:17077303; tripeptidyl-peptidase IDA PMID:2983326 (GnRH); external side of
  plasma membrane IDA PMID:9449382.
- Mouse donor sources (QuickGO): heart contraction / conduction / gap junction /
  gene expression rows all from PMID:25017399 (cardiac ACE overexpression model,
  BHF-UCL) and PMID:16585392; HSC proliferation PMID:20116413; neutrophil immunity
  PMID:17082641 (ACE overexpression in myeloid cells); spermatogenesis and kidney
  development PMID:17135368; synaptic plasticity IDA PMID:35201898.
- Inhibitor-pharmacology IMP rows (captopril/enalapril/perindopril/ramipril with
  downstream readouts) are MARK_AS_OVER_ANNOTATED: they show consequences of
  Ang II/kinin balance, not processes ACE executes. Exceptions: blood-pressure terms
  (direct consequence of ACE catalysis, kept or refined).
- IEP "response to X" rows show regulation of Ace expression, not a response
  executed by Ace: MARK_AS_OVER_ANNOTATED.
- PMID:17977916 (female pregnancy IEP): abstract only mentions ACE2; full text not
  available, so UNDECIDED rather than claiming mis-attribution.
- PMID:7620708 heterocyclic compound binding (IDA): synthetic inhibitor (cFP /
  lisinopril derivative) displacement; grouping term with no functional content;
  REMOVE (flagged for expert check).
- No NEW terms proposed. AcSDKP degradation and Ang-(1-7) degradation have no
  specific GO process terms; covered by peptide catabolic process.

## 2026-10-28 correction: extracellular space is obsolete

- GO:0005615 extracellular space is obsolete in the current GO release. The GO:0005576
  extracellular region rows that had been MODIFIED to it are now ACCEPT (the extracellular
  location is correct and core), and core_functions locations use GO:0005576 extracellular region.

## 2026-11-15 — bounded donor-source corrections during human ACE review

This follow-up supersedes the earlier actin-binding and metallocarboxypeptidase
source statements above. Four contexts were corrected; all 137 native
annotation identities and the other 133 decisions were retained.

- The human UniProt record retains an IDA actin-binding cross-reference even
  though the exact human row was not recovered from QuickGO. That discrepancy
  leaves the donor experiment unresolved; a short cytoplasmic tail does not
  disprove binding. The rat transfer is now UNDECIDED.
- PMID:18158355 studies C-domain-inactivated mice and angiotensin metabolism;
  its abstract was inspected. PMID:27649628 has accessible full text on renal
  angiotensin metabolism, with ACE-inhibitor controls alongside NEP/ACE2
  experiments. They are not antigen-peptide-trimming studies. The evidence for
  a single-C-terminal-residue reaction remains unresolved, so GO:0004181
  remains UNDECIDED with corrected source descriptions.
- The two GO:0070573 transfers trace to human IDA PMID:7961923. Its abstract
  describes Hip-His-Leu kinetics; that supports terminal dipeptide release but
  does not expose every assay in the inaccessible full text. Both transfers
  are now UNDECIDED, with the automatic replacement terms removed.

The human UniProt GO cross-reference is quoted only to document source
provenance, not as independent experimental evidence for actin binding.
No new annotation or additional human-locus completion credit is claimed.

## 2026-11-15 — provenance presentation follow-up

The human UniProt actin-binding cross-reference remains described in the
reference finding and annotation reason, but its `DR GO` line is no longer
used as `supporting_text`. This supersedes the quotation statement immediately
above and avoids presenting a restated database annotation in an evidence-quote
field. All 137 rat annotation decisions are unchanged from the published
PR #6395 draft.
