# kdpE curation notes

## Evidence assessment

KdpE combines two separable activities: phosphorelay response-regulator activity
and sequence-specific regulatory DNA binding. In the E. coli system, KdpE with
an intact phosphorylation site is required for kdpFABC expression, and
phosphorylated KdpE binds the cognate DNA site [PMID:14534307, "kdpFABC
expression requires the corresponding response regulator KdpE with an intact
phosphorylation site"]. PSEPK Q88FE0 has the conserved receiver and DNA-binding
architecture [file:PSEPK/kdpE/kdpE-uniprot.txt].

## Curation decision

Two core-function entries represent the receiver/phosphorelay role and the
DNA-binding transcriptional-activation role independently. Generic DNA binding
and self-binding terms remain non-core or over-annotated where more informative
terms are present.

## 2026-11-01 re-review

- Provider deep research was not run in this pass; no deep-research file exists.
- GO:0000976 and GO:0003677 -> MODIFY to GO:0000987; GO:0005737 -> MODIFY to GO:0005829;
  GO:0006355 -> MODIFY to GO:0045893; GO:0042802 -> MODIFY to GO:0042803 (orthology with
  E. coli KdpE receiver-domain dimer, PMID:16322582).
- E. coli KdpE papers cited as orthology-based support (shared PTHR48111:SF50, receiver and
  OmpR/PhoB DNA-binding domains). The two KdpE core functions (GO:0000156, GO:0000987) remain
  separate.


## Scoped Kdp module consultation — 2026-11-07

The receiver and OmpR/PhoB DNA-binding activities remain distinct core entries with homolog assay scope explicit. Asp55 is present in the frozen target sequence. Protein-DNA complex membership is ACCEPT because DNA-bound transcriptional control is central, not peripheral merely because complex membership follows from binding. Full E. coli22291906 assays establish promoter DNA binding;16322582 receiver-domain structures support the existing homodimerization refinement, not a target-specific oligomerization assay.

Every original annotation row and its source payload/order was reviewed and preserved. No additional annotation rows were proposed. Full provenance and assay boundaries: `analysis/module_audits/bacterial_kdp_potassium_homeostasis/psepk-consultation/primary-scope.md`; sequence checks are adjacent. No IBA rows occur in these six reviews, so no IBA loss judgment is being made. Family membership and original historical ISO donors are retained independently of donor counts.

A genuine `just deep-research PSEPK kdpE --provider falcon` request failed HTTP403 authentication. Logs remain in `.cache/module-audit-logs/kdp-20261107/psepk-consultation/`; no provider report was manufactured.


## 2026-11-07 PR6179 round-one adjudication

Reviewed the source relation, core role and source-specific limits relevant to this gene. See `analysis/module_audits/bacterial_kdp_potassium_homeostasis/round1/evidence.md` for the full evidence and disagreement record. Original ordered annotation payloads, qualifiers and historical NEW/retired flags are preserved. The integrated promoter-output core is GO0001216; cis-regulatory DNA-binding annotations remain distinct and unchanged. CAUVN uses direct promoter data, while KT2440 retains explicit comparative inference [PMID:39133005; PMID:1630316].
