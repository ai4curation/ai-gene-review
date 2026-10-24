# SSZ1 review notes

## 2026-08-12 re-review

- Identity verified as *Saccharomyces cerevisiae* SSZ1/YHR064C (PDR13),
  UniProt P38788, the atypical Hsp70-like subunit of the ribosome-associated
  complex (RAC), not the mitochondrial Fe-S chaperone Ssq1.
- Existing Falcon and targeted OpenScientist reports are correctly scoped. The
  OpenScientist report independently supports removing both family-derived
  GO:0016887 ATP hydrolysis annotations while retaining real ATP binding.
- Ssz1 forms stable RAC with Zuo1 at the cytoplasmic ribosomal tunnel exit. Its
  principal molecular contribution is to enable Zuo1 to stimulate the ATPase of
  the canonical nascent-chain Hsp70 Ssb1/2; neither Ssz1 ATP binding nor
  hydrolysis is required for this role.
- GO:0044183 is retained as the project's pragmatic co-chaperone MF for Ssz1's
  regulatory contribution to the RAC-Ssb folding system; unlike GO:0140662, it
  does not assert Ssz1 ATP hydrolysis. GO:0042026 remains an unsafe family-level
  transfer because classical post-translational refolding is not supported.
- The IMP unfolded-protein-binding annotation is marked over-annotated rather
  than removed: the peptide-binding domain is dispensable and classical Hsp70
  substrate binding is unsupported, but transient nascent-chain contacts within
  RAC cannot be excluded from the available evidence.
- Nuclear and plasma-membrane localizations are unsupported for Ssz1. Cytoplasm
  and cytosol remain consistent with RAC at the cytoplasmic ribosome.

## 2026-08-28 completion audit

- Reconciled the review against all 75 GOA rows, which collapse to 30 unique
  term/evidence/reference/qualifier signatures in the YAML; every non-NEW row now
  records its GOA qualifier explicitly.
- Audited all eight IBA rows against the current PTHR45639 PAINT snapshot. The
  active nodes are PTN002321897 (cytoplasm), PTN002500132 (nucleus/cytosol), and
  PTN000452648 (ATP hydrolysis, heat-shock-protein binding, protein-folding
  chaperone, and protein refolding).
- Corrected the localization interpretation. Plasma membrane remains REMOVE, but
  its root cause is `SOURCE_STALE_OR_MISSING`: the pinned GOA row points to
  PTN002500132, while the current PAINT snapshot has no plasma-membrane assertion
  at that node. Nucleus remains REMOVE with `PROPAGATION_BAD`: PMID:20368619
  directly localizes Jjj1/Zuo1 and discusses Ssb nuclear cycling, whereas its only
  Ssz1-specific result is 27S rRNA precursor accumulation in an SSZ1 deletion.
  That phenotype supports GO:0006364 rRNA processing, not `is_active_in nucleus`.
  [PMID:20368619 "When compared with WT cells, we observed a strong accumulation
  of the 27S rRNA precursor in Δjjj1 and Δzuo1 strains as well as in Δssz1 and
  Δssb1/2"]
- Retained the refolding IBA as `MARK_AS_OVER_ANNOTATED`. Its supported related
  biology is already represented by two accepted GO:0051083 de novo
  cotranslational-folding rows, so a redundant MODIFY replacement would weaken
  the explicit record of the canonical-Hsp70 transfer error.
- Added a NEW GO:0022626 `cytosolic ribosome` annotation and the same location to
  `core_functions`, directly supported by the original RAC study. [PMID:11274393
  "Zuotin and Ssz1p form a ribosome-associated complex (RAC) that is bound to the
  ribosome via the zuotin subunit."]
- RAC membership is captured explicitly in the core-function description and
  evidence, but no `in_complex` GO identifier was asserted: the review found no
  RAC-specific GO cellular-component term, and using generic `ribosome` as a
  complex would falsely imply that Ssz1 is a structural ribosomal subunit. The
  earlier protein-binding wording was corrected so it no longer claims a
  nonexistent RAC complex annotation.
- PAINT `source_label` values now use each exact bare machine identifier
  (`PANTHER:PTN...`) rather than an invented descriptive node label.
- The review is now COMPLETE: ATP binding is retained, ATP hydrolysis remains
  removed as a lost Hsp70 subactivity, generic protein-binding rows remain
  over-annotated, and the experimentally supported cotranslational-folding,
  translational-fidelity, frameshifting, and ribosome-biogenesis annotations are
  retained at core or non-core scope as appropriate. Cytosol is retained as the
  broad core compartment, while all still-broader cytoplasm rows are consistently
  non-core.


## Full annotation re-review — 2026-09-20

Re-read all 31 annotation rows, primary sources and the Falcon report, and critically incorporated the complete existing ATPase OpenScientist investigation. Newly cached PMID:17901048 directly states "We now find that Ssz1 is not an ATPase in vitro". This supports rejecting inherited ATPase activity at PTN000452648 while retaining ATP binding. Dispensability for growth is not proof that an activity is absent; the report's suggestions based on that inference are not adopted.

Newly cached full primary PMID:32198371 directly demonstrates short nascent-chain contacts in Saccharomyces cerevisiae and describes "Ssz1 is an active chaperone optimized for transient, low-affinity substrate binding". The chaperone review, obsolete unfolded-binding replacement, description and core function now include this relay mechanism. The ATPase report identified this lead but did not independently adjudicate refolding or secondary nucleus/plasma-membrane localization.

The old refolding IBA is generalized to protein folding because current PAINT explicitly places a NOT/IRD at fungal PTN001065099 below PTN000452648 and current SSZ1 leaf PTN000453341 carries generalized GO:0006457 through these nodes. This curation revision is not proof of universal absent refolding capacity. Nucleus/plasma-membrane rows are UNDECIDED rather than removed merely because RAC primarily functions on cytosolic ribosomes. The coordinated new focused report will independently evaluate these questions; it has not yet been incorporated here.

## 2026-09-29 IBA follow-up

- Rechecked all eight IBA rows against the current
  `interpro/panther/PTHR45639/PTHR45639-paint.tsv` snapshot. PTN000452648
  still carries the broad ATPase, HSP-binding, chaperone and refolding
  ancestral assertions; PTN002321897 still carries cytoplasm; PTN002500132
  still carries cytosol and nucleus but not plasma membrane.
- Removed the pinned GO:0005886 plasma-membrane IBA as stale: it points to
  PTN002500132, and the current PAINT snapshot has no GO:0005886 assertion at
  that node. The pinned Candida, mouse and rat extant donors are likewise absent
  from any current PTHR45639 GO:0005886 row. This is separate from the still-live
  nucleus IBA, which remains `UNDECIDED` because target cytosolic localization
  does not exclude every secondary pool.
- Kept the ATPase IBA at `REMOVE` for Ssz1-specific subactivity loss, the HSP
  binding and protein-folding-chaperone IBAs as supported by RAC evidence, and
  the protein-refolding IBA as `MODIFY` to GO:0006457 by the fungal
  PTN001065099 NOT/IRD revision.
- Exact 2025+ PubMed search for `(SSZ1 OR Ssz1 OR YHR064C) AND
  "Saccharomyces cerevisiae"` returned PMID:39863615, PMID:40156734 and
  PMID:41078542. PMID:39863615 is a *Candida glabrata* Ipi1 paper with
  *S. cerevisiae* PDR context only. PMID:40156734 directly tests ssz1∆ in a
  prion/Hsp104 background and was added as a medium-relevance downstream
  proteostasis reference. PMID:41078542 directly assays SSB1/2 and mentions
  Ssz1/PDR context; it was cached but did not change SSZ1 annotation decisions.

## 2026-10-01 focused report incorporation

- Read and incorporated
  `SSZ1-hypotheses/refolding-and-secondary-compartments/openscientist.md`. The
  report supports the existing stale `GO:0005886` plasma-membrane removal and
  resolves `GO:0005634` nucleus from `UNDECIDED` to `REMOVE`: current
  PTN002500132 nucleus propagation is live, but it is seeded by canonical
  cytosolic Hsp70s and remains unsupported for specialized ribosome-associated
  Ssz1.
- Kept `GO:0042026` protein refolding at `MODIFY` to `GO:0006457`. The report
  independently agrees that autonomous Ssz1 refolding is not supported, but its
  live-QuickGO statement that no `GO:0042026` NOT exists in the family is stale
  relative to the local PTHR45639 snapshot, where PTN001065099 already carries a
  2026-06-16 NOT/IRD and generalized protein-folding assertion.
- Reviewed the 45 current high-throughput `GO:0005515` rows added by the fresh
  GOA seed. Newly seeded Zuo1-backed rows from PMIDs 16429126, 16554755,
  19536198 and 37968396 were converted to `GO:0031072` heat shock protein
  binding, matching the existing direct RAC partner rows; all other newly seeded
  rows were removed as generic proteomics-derived `protein binding`. SSB2-backed
  rows were kept at `REMOVE` with row-specific reasons because Ssb2 is the
  cognate Hsp70, but these high-throughput co-purifications do not establish a
  direct binary Ssz1-Ssb2 contact distinct from ribosome- and Zuo1-bridged
  RAC/Ssb coupling.
