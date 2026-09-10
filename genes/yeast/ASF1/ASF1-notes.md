# ASF1 curation notes

## 2026-09-02 Update: audit fix — erroneous proposed_replacement_terms entry

While auditing the existing review, found that the `GO:0005515 protein binding` IPI
annotation (original_reference_id: PMID:11404324, documenting the ASF1–Cac2/CAF-1
interaction) carried a bogus `proposed_replacement_terms` entry — id `GO:0030515` paired
with the label `"positive regulation of cation transport"` — alongside the correct
`GO:0042393 histone binding`.

The id and the label did not go together. `GO:0030515` is in fact **`snoRNA binding`**
("Binding to a small nucleolar RNA"), confirmed against the committed ontology cache
(`cache/ontologies/go.tsv` → `GO:0030515<TAB>snoRNA binding`) and against OLS. The string
"positive regulation of cation transport" does not occur anywhere in the ontology cache
either — though that cache is deliberately sparse (`go.meta.json`: 6820 terms, "Only terms
used in annotations"), so its absence there does not by itself establish that no such GO
label exists anywhere in the ontology. What is established is the part that matters: it is
not the label of `GO:0030515`. So the entry was a mismatched id+label pair, not a
copy/paste of a real term from another review — precisely the failure mode CLAUDE.md warns
about, where a plausible-looking label conceals a wrong id. Note that
`src/ai_gene_review/tools/fix_labels.py` deliberately skips `proposed_replacement_terms`
(they "may contain hallucinated GO IDs"), so no automated label check would have caught
this.

The removal stands either way: snoRNA binding is as unrelated to ASF1's
histone-chaperone / chromatin-assembly biology as ion transport would have been. ASF1 has
no documented snoRNA-binding or ion-transport role in any of the cited literature, the
deep-research reports, or UniProt (P32447). Removed the erroneous term; kept the
`GO:0042393 histone binding` replacement suggestion, which is well supported by ASF1's
defining H3-H4 histone-binding activity documented throughout this review (e.g.
[PMID:15840725 "Structural basis for the interaction of Asf1 with histone H3 and its
functional implications."]).

Left open (flagged as non-blocking by review, needs curator judgment rather than a
mechanical edit): the retained `GO:0042393 histone binding` replacement does not match
that particular IPI's own evidence, which is an ASF1–Cac2/CAF-1 protein interaction, and
the sibling protein-binding IPIs carry no replacement terms at all; the `supporting_text`
on that annotation is also the paper title rather than substantive evidence.

No other changes made — the rest of the review (annotation actions, core_functions,
description) is well-supported by the cited evidence and deep-research reports.

## 2026-09-07 Update: resolved the retained histone-binding replacement, and corrected two misidentified interactors

Follow-up to the review's blocking item on the section above. Two things were wrong, and
they turn out to be the same mistake.

**1. The interactors were misidentified.** Both the 2026-09-02 note and the review's own
summaries described the WITH/FROM accessions on these IPI rows as CAF-1 subunits
("Cac2", "Cac1"). Checked both against UniProt directly:

- `UniProtKB:P32479` is **HIR1_YEAST / Hir1** (YBL008W), a subunit of the **HIR complex**,
  not CAF-1. UniProt's own SUBUNIT annotation cites the very reference on this row: "The
  HIR complex interacts with ASF1 (PubMed:11404324, PubMed:11412995)."
- `UniProtKB:Q04003` is **SAS4_YEAST / Sas4** (YDR181C), a subunit of the **SAS
  (something-about-silencing) complex**, not Cac1. UniProt records "Interacts with ASF1",
  consistent with [PMID:11731480 "The silencing complex SAS-I links histone acetylation to
  the assembly of repressed chromatin by CAF-I and Asf1 in Saccharomyces cerevisiae."] —
  the paper title names CAF-I, but the accession actually recorded in WITH/FROM is the
  SAS-I subunit.

Neither the ASF1–Hir1 nor the ASF1–Sas4 interaction is a CAF-1 interaction. Corrected both
summaries (`PMID:11404324` and `PMID:11731480` rows) accordingly. The genuine ASF1–Cac2
CAF-1 link is real and is discussed elsewhere in the review (IBA row for
replication-coupled nucleosome assembly); it is simply not what these two IPI rows record.

**2. The retained `GO:0042393 histone binding` replacement was therefore unsupportable.**
`proposed_replacement_terms` is a machine-readable instruction attached to a specific
annotation row, so retaining it would have turned an ASF1–Hir1/Sas4 complex-subunit
interaction into a histone-binding IPI. Hir1 and Sas4 are chromatin-regulatory complex
subunits, not histones. Removed the entry. Nothing is lost by doing so: ASF1's histone
binding is independently annotated (IEA from GO_REF:0000002, and IBA), and the sibling
`GO:0005515` IPI rows carry no replacement terms either, so the row is now consistent with
them. The `reason` text on the row stands on its own and now states why no replacement is
proposed.

Also softened the ontology-cache claim in the section above: `cache/ontologies/go.tsv` is
restricted to terms used in annotations (6820 terms per `go.meta.json`), so a string's
absence from it cannot show the string is "not a GO label at all". The conclusion that
matters — that it is not the label of `GO:0030515` — is unaffected.

Still open (pre-existing, non-blocking): the `supporting_text` on the `PMID:11404324` row
is the paper title rather than substantive evidence. The cached publication is
abstract-only, so a substantive verbatim quote establishing the Hir1 interaction is not
available from the cache; left as-is rather than paraphrasing, since `supporting_text` must
be verbatim.

## 2026-09-08 Update: removed unsupported telomere-maintenance replacement; parity + quote fixes

Follow-up to the review's remaining blocking item. The `GO:0006282 regulation of DNA
repair` NAS row (PMID:27222517) was the file's only surviving `proposed_replacement_terms`,
and it proposed `GO:0000723 telomere maintenance` — a real, non-obsolete id
(`cache/ontologies/go.tsv` → `GO:0000723<TAB>telomere maintenance`) but unsupported by the
row's own evidence. The row's `reason` and `supporting_text` are entirely about Rad53
dephosphorylation and DNA-damage-checkpoint recovery; `grep -ci telomere` over the full
text of `publications/PMID_27222517.md` (`full_text_available: true`) returns 0. This is
the same artifact class removed earlier in this PR — a plausible id attached to a row whose
evidence does not support it. Removed the replacement; the checkpoint-recovery biology is
already captured by the sibling `GO:2000002` (negative regulation of DNA damage checkpoint)
annotation from the same reference, which is ACCEPTed. Also replaced that row's
`supporting_text` (previously the paper title) with a substantive verbatim quote from the
full text about the Rad53 dephosphorylation role.

Also (non-blocking parity fix): the `PMID:11731480` IPI summary now names both GOA
WITH/FROM accessions — `UniProtKB:P40963` (Sas2, confirmed via `genes/yeast/SAS2/SAS2-uniprot.txt`
`AC P40963` / `GN Name=SAS2`) and `UniProtKB:Q04003` (Sas4) — both SAS-I complex subunits,
rather than Sas4 alone.

Note: the 2026-09-02 "Left open" paragraph above (referring to "ASF1–Cac2/CAF-1") is
superseded by the 2026-09-07 interactor correction — those accessions are Hir1 and Sas4,
not CAF-1 subunits.

## 2026-09-10 Update: removed fabricated `GO:0016585` label from free-text reason

The 2026-09-08 review found one more instance of the artifact class this PR was opened to
remove — a wrong GO id carried by a plausible-sounding label — this time in a free-text
`reason` rather than in `proposed_replacement_terms`, which is why neither the term
validator (which hard-checks only `core_functions`) nor the label-fixing tooling surfaced
it.

The `GO:0006351 DNA-templated transcription` IEA row (GO_REF:0000043) closed its `reason`
by suggesting three more specific terms: "GO:0006357, GO:0032968, GO:0016585 polymerase II
elongation". The first two are correct, but `GO:0016585` is not an elongation term at all:
it is **obsolete**, and its label is "chromatin remodeling complex"
(`cache/ontologies/go.tsv` → `GO:0016585<TAB>obsolete chromatin remodeling complex`;
independently confirmed via OLS, which reports `is_obsolete: true` and the obsoletion
reason "its definition no longer reflects and cannot be modified to be consistent with the
current state of knowledge"). Beyond being obsolete, it is a **cellular-component** term
being offered as a more specific alternative for a **biological-process** annotation.

The fix is a deletion rather than a substitution. `GO:0032968` (positive regulation of
transcription elongation by RNA polymerase II) is already named in the same sentence and is
already annotated on this gene with IDA evidence, so the elongation point is covered;
proposing a guessed replacement id would repeat the original mistake.

Also in this pass (non-blocking items from the same review):

- Documented here for the first time the `PMID:16554755` softening made on 2026-09-08 but
  omitted from that day's journal entry: the IPI summary previously asserted interactions
  with histones "H3, H4, H2A, H2B", but no H2A or H2B accession appears among the twelve
  GOA WITH/FROM accessions for that reference, so the summary now says "histone proteins"
  without enumerating types. That summary has additionally been rewritten to describe the
  annotation itself rather than narrating what the review declines to assert.
- The `GO:0006282` NAS row's `reason` no longer argues against telomere maintenance. That
  argument was written to justify removing the `GO:0000723` replacement term on 2026-09-08;
  with the term gone from the file, the rebuttal had no referent for a reader. The
  substantive point that survives — that the checkpoint-recovery biology is captured by the
  sibling `GO:2000002` annotation from the same reference — is retained.
- `status` flipped `IN_PROGRESS` → `COMPLETE`. This is not a judgement call: no annotation
  is `PENDING` (28 ACCEPT, 18 KEEP_AS_NON_CORE, 1 MARK_AS_OVER_ANNOTATED) and validation is
  warning-free, which is the schema's definition of `COMPLETE`. The repo's own
  `status_manager.compute_status_from_file` independently returns `COMPLETE` for this file.

## 2026-09-10 — IPI summaries realigned to their own WITH/FROM accessions

Review round of 2026-09-10 flagged two IPI rows whose summaries named interactors that are
not the accessions recorded on those rows — the same defect class as the `P32479`
"Cac2"→Hir1 and `Q04003` "Cac1"→Sas4 corrections of 2026-09-07, and with the same origin:
the paper's title supplied a protein name where the accession should have. Both are
`KEEP_AS_NON_CORE` on a generic `GO:0005515`, so the actions are unaffected; only the
identity claims were wrong.

**`PMID:15755447` — "MCM2 helicase" → Rad53.** The row's only WITH/FROM is
`UniProtKB:P22216` [`ASF1-goa.tsv`, ECO:0000353]. ASF1's own UniProt IntAct block names that
accession RAD53 with `NbExp=11` [`ASF1-uniprot.txt:560`], and the block's seven partners
(Hhf2, Hht2, Hir1, Rad53, Rtt106, Sas2, Sas4) include no MCM subunit at all
[`ASF1-uniprot.txt:557-563`]. The previous `reason` had built a mechanism on the misreading
("functionally relevant for histone delivery at replication forks"), which pointed the row
at the wrong pathway: ASF1–Rad53 is real, but it is checkpoint biology, already handled by
the `GO:2000002` and `GO:0006282` rows from `PMID:27222517`. The paper's title
("…regulation of MCM helicase by Tof1/Mrc1/Csm3…") is the likely source of the error.

**`PMID:16429126` — "DNA polymerase, MCM, and CAF-1 subunits" matched none of the three
accessions.** The rows carry `P11484`, `P22216` and `P47171`. `P11484` is Ssb1, a
ribosome-associated Hsp70 [`genes/yeast/SSB1/SSB1-uniprot.txt`]; `P22216` is Rad53, as
above. **`P47171` is not identifiable from any record committed to this repository**, so the
summary now names the accessions and asserts no identity for it — per CLAUDE.md, an omitted
identification says "not established" where a guessed one would say something false.

Non-blocking items from the same review, addressed in this pass:

- **`PMID:19536198` — "multiple histone chaperone partners" was one Hsp70.** The single
  WITH/FROM on that row is `P11484` (Ssb1), so the description overstated both the number
  of partners and their nature. ASF1's histone binding is annotated independently and never
  rested on this row.
- **`GO:0005634` nucleus IDA — mismatched `supporting_text` replaced.** The quote attached was
  about Rad53 dephosphorylation, which is checkpoint biology rather than localization
  evidence. It now reads "Asf1 associates with the histone H3–H4 heterodimer"
  [`publications/PMID_27222517.md:124`] — the chromatin complex that this Complex Portal IDA
  actually records. Worth noting for future auditors: `grep -niE 'nuclear|nucleus|localiz'`
  over that cache returns **nothing** despite `full_text_available: true`, so no direct
  localization quote is extractable from this paper at all. `ACCEPT` stands regardless — the
  Complex Portal curator worked from the full record, and GOA carries two further independent
  nucleus IDAs (`PMID:11404324`, `PMID:22932476`). Deleting `supported_by` outright was tried
  first and rejected: it raises a best-practice warning that flips the computed status back to
  `DRAFT`, which would have been a worse outcome than the nit it fixed.
- **`GO:0032968` — "directly demonstrates" softened.** `publications/PMID_22308335.md` is
  abstract-only and `grep -ci asf1` returns 0, so that phrasing claimed more than is visible
  here. Per CLAUDE.md the experimental annotation is not second-guessed on that basis;
  `ACCEPT` is unchanged and only the phrasing was overstated.
