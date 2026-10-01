# SOD2 notes

## 2026-09-29 IBA propagation rereview

- `GO:0005739 mitochondrion` IBA traces through `PANTHER:PTN000150076`. The current
  `interpro/panther/PTHR11404/PTHR11404-paint.tsv` has a matching mitochondrial IBD
  at that node for eukaryotic MnSOD proteins, including SGD:S000001050 as a descendant
  evidence.
- `GO:0004784 superoxide dismutase activity` and `GO:0030145 manganese ion binding`
  both trace through `PANTHER:PTN004256454` in the current PTHR11404 PAINT file.
  Direct yeast evidence from PMID:238997, PMID:15851472, and the native/Fe-substituted
  yeast SOD2 structures in PMID:22102021 supports the catalytic and Mn-binding calls.
- No IBA propagation failure was found. S. cerevisiae SOD2 is assigned to
  `PTHR11404:SF6`, the mitochondrial MnSOD subfamily, and the three propagated terms
  match its experimentally established matrix superoxide dismutase activity.
- Searched 2024-2026 PubMed and web results for SOD2/Sod2p/MnSOD papers in
  Saccharomyces and yeast. Newer SOD2 hits mostly measure oxidative-stress phenotypes
  or use `SOD2` as a panel readout; none changed the core GO decisions.
- Cached PMID:37638880, a 2023 full-text Genetics paper showing that Sod2 suppresses
  paraquat-induced nuclear chromosomal rearrangements. That result is a downstream
  consequence of mitochondrial superoxide detoxification and does not make SOD2 itself
  a DNA-repair or nuclear genome-maintenance factor.

## 2026-10-01 current GOA refresh

Refreshing current GOA retained all three SOD2 IBA terms on the same PAINT nodes:
`GO:0005739 mitochondrion` at `PANTHER:PTN000150076`, and both `GO:0004784
superoxide dismutase activity` and `GO:0030145 manganese ion binding` at
`PANTHER:PTN004256454`. The 2026-10-01 PAINT/GOA row for mitochondrial
localization replaces the old TAIR locus source with `AGI_LocusCode:AT3G10920`,
and the catalytic IBA replaces both old TAIR locus sources with
`AGI_LocusCode` identifiers; I kept these as current exact rows because the IBD
nodes and biological inferences are unchanged.

Current GOA dropped five older broad automated rows from the previous review:
keyword-derived `GO:0016209 antioxidant activity` and `GO:0016491
oxidoreductase activity`, logical-inference `GO:0019430 removal of superoxide
radicals` and `GO:0098869 cellular oxidant detoxification`, and the old
UniProt combined-IEA `GO:0046872 metal ion binding` row. I marked all five as
retired provenance. The current InterPro2GO `GO:0046872` row is still correct
but non-core, because the exact `GO:0030145 manganese ion binding` annotation
captures the active-site cofactor.

Two new `GO_REF:0000123` rows came from the YeastPathways DETOX1-PWY GO-CAM
import. The activity and process assertions for SOD2 are sound, but the paired
`GO:0005829 cytosol` location contradicts direct matrix localization in
PMID:238997 and import-dependent manganese activation in PMID:15851472, so I
removed the cytosol row while keeping the imported `GO:0004784` and
`GO:0019430` rows.
