# SIR4 curation notes

## 2026-09-02 Update

Audited existing_annotations for oversights (this is a companion fix to the same
issue found and fixed in SIR2 and SIR3).

- **GO:0006303 (double-strand break repair via nonhomologous end joining), IMP,
  PMID:9501103**: was marked `MARK_AS_OVER_ANNOTATED` ("SIR4 is not a direct
  participant in the NHEJ catalytic machinery... this is an indirect function...
  overstates SIR4's role"). But the cited paper's abstract reports a direct
  functional assay, not an inference: "using an in vivo plasmid rejoining assay,
  we demonstrate that SIR2, SIR3 and SIR4, three genes shown previously to
  function in TPE, are essential for Ku-dependent DSB repair" [PMID:9501103
  "SIR2, SIR3 and SIR4, three genes shown previously to function in TPE, are
  essential for Ku-dependent DSB repair"]. SIR4 is not core NHEJ catalytic
  machinery, so the function remains secondary/non-core, but `MARK_AS_OVER_ANNOTATED`
  mischaracterizes directly-demonstrated genetic evidence as likely spurious
  over-annotation. Changed action to `KEEP_AS_NON_CORE`, consistent with the same
  fix applied to SIR2 and SIR3 for the identical annotation/reference.
- All other annotations reviewed; no other genuine, evidence-backed oversights
  found.

## 2026-09-05 Update — corrects the 2026-09-02 entry above

Review feedback on PR #2946 correctly pointed out that the 2026-09-02 rationale
conflated a **direct assay** with a **direct role**, and that two claims in it
were wrong. Both are corrected here.

**1. The role is indirect, and the follow-up literature says so explicitly.**
Boulton & Jackson's assay is direct, but the `sir` end-joining defect is largely
a consequence of mating-type derepression, not of SIR4 acting at the break. In
`sir` mutants HML/HMR are expressed, the cell adopts an a/alpha pseudo-diploid
identity, and a1/alpha2 represses the haploid-specific NHEJ factor `NEJ1`
[PMID:10421582 "the effect of deleting SIR genes is largely attributable to
derepression of silent mating-type genes, although Sir proteins do play a minor
role in end-joining"] [PMID:11676923 "The NEJ1 promoter contained a consensus
binding site for the a1/alpha2 repressor, explaining the cell type-specific
expression."]. The residual direct contribution is small: with haploid identity
held constant, `sir` deletions reduce chromosomal NHEJ only two- to threefold and
leave plasmid end-joining unaffected [PMID:10421582 "sir Delta mutants reduced
the frequency of NHEJ by twofold or threefold, although plasmid end-joining was
not affected"].

The decisive experiment is Kegel et al.'s rescue, whose `sir` panel explicitly
includes Sir4p: constitutive Nej1p expression "completely rescued the defect in
NHEJ, thus showing that Sir proteins per se were dispensable for NHEJ"
[PMID:11676923]. So SIR4 is not a participant in end-joining at all — it acts
permissively upstream, silencing HML/HMR so that `NEJ1` stays expressed.

Action therefore changed from `KEEP_AS_NON_CORE` to **`MODIFY`**, proposing
GO:2001032 *regulation of double-strand break repair via nonhomologous end
joining* (verified via OLS; not obsolete). The general regulation term is used
rather than the directional GO:2001034 because the role is permissive rather
than actively modulating. `KEEP_AS_NON_CORE` was rejected because it retains the
*participant* term GO:0006303, which the Kegel rescue contradicts.

**2. The "already fixed in SIR2/SIR3" claim was not true when written.** At the
time of the 2026-09-02 entry both PRs were still open. Current state on `main`:
SIR3 (#2944) **merged 2026-09-05** with exactly the `MODIFY` → GO:2001032
adjudication adopted here; SIR2 (#2942) is **still open** and still carries
`REMOVE`. The merged SIR3 entry explicitly flags SIR4 and SIR2 as needing
reconciliation with its rationale — this update does that for SIR4. SIR2 remains
outstanding.

**Deliberate divergence from the review's two suggested options.** The review
offered (1) keep `KEEP_AS_NON_CORE` with a corrected reason, or (2) keep
`MARK_AS_OVER_ANNOTATED` with the correct mechanism. Neither was taken, because
the review was written on 2026-09-02, three days before SIR3 merged, and the
merged SIR3 decision settles the identical annotation/evidence/reference triple
on `MODIFY` → GO:2001032. Adopting the same outcome keeps the three Sir entries
consistent rather than introducing a third adjudication of one experiment.

**Not changed (out of shepherd scope):** `SIR4-ANNOTATION-ACTIONS.tsv` and
`SIR4-CURATION-SUMMARY.md` still record the old action and the repudiated
telomere-stabilization rationale, as the review's 🔵 item noted. These are
hand-maintained companion artifacts outside the curation file set, and are left
for a curator to update or delete.
