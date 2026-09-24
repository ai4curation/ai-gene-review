# murB curation notes

Q88LM5/PP_1904 is the FAD-dependent MurB reductase in peptidoglycan precursor
synthesis
[UniProtKB:Q88LM5, "Name=FAD;"; "PATHWAY: Cell wall biogenesis; peptidoglycan
biosynthesis."].

The separate cytoplasm and cytosol IEAs are redundant. The UniProt-supported
cytoplasm term is accepted, while cytosol is marked over-annotated and omitted
from the core-function summary. The two FAD-binding IEAs are treated similarly:
one ancillary annotation is retained and the duplicate is marked
over-annotated.

## 2026-09-24 TreeGrafter re-review

The TreeGrafter cytosol row (GO:0005829) was relaxed from MARK_AS_OVER_ANNOTATED
to ACCEPT: MurB is a soluble cytoplasmic enzyme with no transmembrane segments,
so cytosol is a true descendant of the accepted cytoplasm term rather than an
over-annotation (projects/TREEGRAFTER/rereview-2026-09-24/batch-06a.yaml).
