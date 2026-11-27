# SWI6 (P09959, YLR182W) — curation notes

Working journal for the GO annotation review of *Saccharomyces cerevisiae* SWI6.
Inline citations use `[PMID:NNN "verbatim text"]`; all quoted text is from the cached
`publications/PMID_*.md` files. Note that many of the older papers are abstract-only in
the cache (1465410, 16429126, 18268013, 1832338, 25112483, 2649246, 3542227, 8372350,
8423776, 8590795, 9628912, 9719633); full text is cached for 10490612, 12697814,
19823669, 20641022, 21179020, 24470217 and 37968396.

## Identity check

Budding-yeast Swi6 is the ~90 kDa ankyrin-repeat regulatory subunit of SBF and MBF. It is
**not** the *S. pombe* Swi6, which is an HP1-family heterochromatin protein; the only
GO-CAM index hits for "swi6" are the pombe HP1 models and are irrelevant here. The
deep-research file makes the same distinction.

## Synthesised picture

- **Shared subunit of two G1/S transcription factors.** SBF = Swi4-Swi6, MBF = Mbp1-Swi6
  [PMID:10490612 "Swi4 and Mbp1 are the DNA binding components of SBF and MBF,
  respectively."]; [PMID:8372350 "MBF contains Swi6 and a 120-kilodalton protein (p120)."].
- **No DNA-binding activity of its own.** [PMID:10490612 "In contrast, Swi6 has no DNA
  binding activity but is present in the SBF complex because of its interaction with Swi4
  via the carboxy-terminal regions (CTRs) of the two proteins"]; [PMID:1465410 "we propose
  that Swi4 is responsible for binding to the SCB sequence while Swi6, through its
  association with Swi4, regulates activity of the complex."].
- **But required for the complex to bind DNA.** Swi6 relieves the Swi4 C-terminal
  auto-inhibition [PMID:10490612 "The interaction of the carboxy-terminal region of Swi4
  with Swi6 alleviates this inhibition, allowing Swi4 to bind DNA."], and Swi6 TPLH-repeat
  or leucine-zipper mutants form the complex but cannot bind DNA [PMID:8423776 "Deletion of
  the lucine zipper motif in SWI6 also allows SWI4/6 complex formation, but it eliminates
  the DNA-binding ability of the SWI4/6 complex."]. This is exactly a `contributes_to`
  relationship to sequence-specific DNA binding.
- **Carries the activation regions.** [PMID:9719633 "Within the central region, a 141
  residue segment that is capable of transcriptional activation encompasses a structural
  domain of approximately 85 residues."] and a second C-terminal activator next to the
  heteromerisation sequences [PMID:9719633 "A second protease sensitive region connects the
  ANK domain to the remaining 30 kDa C-terminal portion of Swi6 which contains a second
  transcriptional activator and sequences required for heteromerisation with Swi4 or
  Mbp1."]. Kim and Levin call it "the transcriptional activation component of SBF"
  [PMID:20641022 "Additionally, Swi6 is the transcriptional activation component of SBF
  (Sedgwick et al., 1998)."].
- **G1/S.** swi4 swi6 double mutants die because CLN1/CLN2 transcription fails
  [PMID:1832338 "We show that the essential role of SWI4 and SWI6 is to ensure the activity
  of G1-specific cyclin genes."]; mbp1 swi4 double mutants are likewise inviable
  [PMID:8372350 "Strains deleted for both MBP1 and SWI4 were inviable, demonstrating that
  transcriptional activation by MBF and SBF has an important role in the transition from G1
  to S phase."].
- **Localization cycle.** Nuclear in late M/G1, cytoplasmic from late G1 to late M when
  Ser160 is phosphorylated [PMID:8590795 "Phosphorylation of serine 160 persists from late
  G1 until late M phase, and Swi6 is predominantly cytoplasmic during this time."];
  Msn5-dependent export in G2/M is needed to re-set SBF [PMID:12697814 "In conclusion,
  these results strongly suggest that the export of Swi6p to the cytoplasm by Msn5p is
  essential for SBF activity."]; Ess1 acts on the phospho-Ser-Pro NLS [PMID:24470217 "In
  contrast, Swi6-GFP fluorescence in ess1H164R mutant cells was diffuse at all stages of the
  cell cycle, with signal in both the nucleus and the cytoplasm, indicative of a defect in
  nuclear localization."]. ChIP shows nuclear Swi6 on the CLN2 promoter [PMID:12697814
  "Swi6p immunoprecipitated from wild-type cells specifically purified a DNA fragment
  corresponding to the promoter of the CLN2 gene, indicating that, as expected, Swi6p is
  bound to the DNA."].
- **Corepressor / Cln3 interface.** Sin3 (Rpd3L) at CLN2 depends on Swi6 but not Swi4, and
  Cln3 co-IPs with Swi6 in a Swi4-dependent way [PMID:19823669 "We found that Cln3
  co-immunoprecipitates with the Swi6 component of SBF, and that this co-immunoprecipitation
  depends on Swi4 (Figure 6)."].
- **Cell-wall stress (Mpk1/Slt2).** Swi4-Mpk1 binds FKS2 without Swi6, but initiation needs
  Swi6 [PMID:18268013 "This complex then recruits Swi6 to activate transcription."];
  reporters for FKS2, CHA1, YKR013w, YLR042c are induced by heat/Congo Red/CFW/Zymolyase
  and are "strictly dependent on both SWI4 and SWI6" [PMID:20641022]; heat is the strongest
  inducer [PMID:20641022 "in general, elevated growth temperature was the strongest inducer
  for all of the reporters"].
- **Meiosis.** swi6 null: reduced spore viability and recombination, reduced RAD51/RAD54
  transcripts, dosage-dependent [PMID:9628912 "These results suggest that SWI6 enhances the
  expression level of the recombination genes in meiosis in a dosage-dependent manner, which
  results in an effect on the frequency of meiotic recombination."].

## Decisions on the non-trivial rows

1. **GO:0000978 IBA (contributes_to)** — ACCEPT. The qualifier is the whole point: Swi6
   does not bind DNA but the SBF/MBF DNA-binding activity depends on it. Donors are the
   three pombe MBF subunits.
2. **GO:0001228 IBA (enables)** — MODIFY to GO:0003713 transcription coactivator activity.
   The donors (Swi4, Mbp1, pombe Res1) are all DNA-binding subunits; Swi6 is not in the WITH
   list. GO:0001228 is a *DNA-binding* TF activity, which Swi6 cannot enable. SGD's own IDA/IMP
   for Swi6 is GO:0003713 (PMID:9719633). Recorded as a TERM_SCOPING_PROBLEM / ROLE_CONFLATION
   propagation issue at the family node (mirror image of the SWI4 review, where the cytoplasm
   and MBF IBAs were the mis-scoped ones). An alternative that would also satisfy me is
   keeping GO:0001228 with `contributes_to`.
3. **GO:0005515 rows (10 of them).** Targeted studies with Swi4 or Mbp1 → MODIFY to
   GO:0046982 protein heterodimerization activity (consistent with the SWI4 review) plus
   GO:0140297 DNA-binding transcription factor binding on the two founding papers
   (10490612 for Swi4; 8372350 for Mbp1). HTP surveys (16429126, 37968396) → REMOVE as
   uninformative. Cln3 row (19823669) → REMOVE, because the co-IP is Swi4-dependent so a
   direct Swi6-Cln3 contact (which would justify cyclin binding) is not shown.
4. **Cytoplasm rows** — KEEP_AS_NON_CORE, same grading as the WHI5 review: real, regulated
   location of the exported pool; the coactivator function is nuclear. The IBA is seeded by
   Swi6 itself so it is correct for Swi6 even though the SWI4 review removes it for Swi4.
5. **GO:0006355 rows** — MODIFY to GO:0045944 (direction-neutral root; all evidence is
   activation of Pol II transcription), as in the SWI4 review.
6. **GO:0010845 meiotic recombination** — KEEP_AS_NON_CORE. Swi6 does the transcriptional
   work that sets RAD51/RAD54 levels, which is what a regulation term describes, but it is a
   meiotic, dosage-dependent side output.
7. **GO:0034605 cellular response to heat** — KEEP_AS_NON_CORE, as for SWI4 (heat is one of
   several CWI-pathway triggers).
8. **GO:0030907 MBF IBA** — ACCEPT here (Swi6 is genuinely in MBF), whereas the same IBA is
   removed on SWI4; this is the intended asymmetry.

## Core functions

Three activity units, all with MF = transcription coactivator activity (GO:0003713) and
contributes_to GO:0000978 for the two cell-cycle complexes: (1) SBF subunit at Start,
(2) MBF subunit at Start, (3) activator recruited to Swi4-Mpk1 under cell-wall stress.
Chromatin (GO:0000785) is supported by ChIP but has no GOA row, so it was left out of
`locations` rather than adding a NEW annotation.

## Not proposed (comparator-checked in spirit)

- No NEW terms. A cell-wall-integrity / fungal-type cell wall organization process term
  would be the natural home for the Mpk1-SBF branch, but SGD has chosen GO:0034605 and
  GO:0045944 for both SWI4 and SWI6, so this is raised as a question rather than asserted.
- No "cyclin binding" for Cln3 (see above) and no chromatin CC row.

## Validation

`just validate yeast SWI6` passes; the remaining warnings were removed by dropping the
chromatin location and the non-core heat term from `core_functions` and by citing the
deep-research file.

## 2026-09-29 IBA source alignment

- Rechecked the six SWI6 IBA rows against the current `PTHR24198` PAINT snapshot.
  Added PTN-level `propagation_review` blocks for the five supported transfers, and
  retained the enables-qualified `GO:0001228` DNA-binding transcription factor activity
  as a `TERM_SCOPING_PROBLEM` whose source is the broad `PTN000917496` node.
- The cytoplasm and MBF rows are intentionally asymmetric with SWI4: `GO:0005737`
  cytoplasm is valid but non-core for Swi6 because its regulated cytoplasmic pool resets
  SBF, and `GO:0030907` MBF transcription complex is core for Swi6 because Swi6 is shared
  by both SBF and MBF.
- Searched 2025-2026 PubMed and the broader web for `SWI6`/`YLR182W` papers in budding
  yeast; the hits were gene pages, older primary literature, or broad G1/S summaries and
  did not require new SWI6-specific curation changes.
