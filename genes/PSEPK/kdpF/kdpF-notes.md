# kdpF curation notes

## Evidence assessment

E. coli deletion and reconstitution experiments show that KdpF remains in the
purified Kdp complex but is dispensable for low-potassium growth and has little
effect on membrane-bound ATPase activity. Its strong stabilizing effect is seen
after detergent solubilization and can be substituted by added lipids
[PMID:10608856, "the purified detergent-solubilized enzyme complex showed a
dramatic decrease in enzymatic activity"]. This bounds the role to an in vitro
stabilization phenotype rather than an essential in vivo transport function.

## PSEPK locus verification

The late old-locus tag PP_5660 does not indicate a distant gene. In the RefSeq
NC_002947.4 feature table, kdpF is the reverse-strand CDS at
4705173..4705262, immediately adjacent to reverse-strand kdpA at
4703469..4705163. KdpB, KdpC, KdpD, and KdpE continue in the same locus. The
current feature table labels KdpF as PP_RS21615 and records PP_5660 as its old
locus tag [RefSeq:NC_002947.4, accessed 2026-08-11]. UniProt maps the 29-residue
PSEPK peptide to this RefSeq record [file:PSEPK/kdpF/kdpF-uniprot.txt].

## Curation decision (earlier draft; see re-review pass below)

KdpF is retained as a non-catalytic pump component contributing to GO:0008556.
The core-function prose is limited to the experimentally demonstrated
detergent-solubilized-complex stabilization, with transfer to PSEPK identified
as family- and locus-based inference.

## 2026-11-01 re-review pass

- Provider deep research was not run in this pass; the upgrade relies on the UniProt record
  (HAMAP/InterPro/NCBIfam family evidence) and cached E. coli ortholog publications, cited as
  orthology-based support.
- Every row now has a reason and verbatim support; correct-but-general terms changed to MODIFY
  with the specific term the gene already carries; a NEW part_of GO:0031004 (ISO from the E. coli
  ortholog) row added so the complex used in core_functions is reflected in annotations.
- Revised decision: KdpF is no longer given contributes_to GO:0008556 in core_functions; the
  GO:0008556 IEA row is MARK_AS_OVER_ANNOTATED, because KdpF has no catalytic or transport activity
  and is dispensable in vivo in E. coli [PMID:10608856 "KdpF is not essential for growth on low K(+) (0.1 mM) medium"].


## Scoped Kdp module consultation — 2026-11-07

GO0008556 and0071805 are ACCEPT for the peptide's structural contribution to its pump, now represented by contributes_to and the existing transport BP in the core. The original ISO complex NEW row is retained. PMID10608856 is explicitly E. coli: low-K growth and membrane ATPase activity tolerate deletion under tested conditions, while purified detergent-complex activity is rescued by KdpF or lipids. Those results support a stabilizing role rather than peripheral function; no KT2440 deletion or universal dispensability claim is made.

Every original annotation row and its source payload/order was reviewed and preserved. No additional annotation rows were proposed. Full provenance and assay boundaries: `analysis/module_audits/bacterial_kdp_potassium_homeostasis/psepk-consultation/primary-scope.md`; sequence checks are adjacent. No IBA rows occur in these six reviews, so no IBA loss judgment is being made. Family membership and original historical ISO donors are retained independently of donor counts.

A genuine `just deep-research PSEPK kdpF --provider falcon` request failed HTTP403 authentication. Logs remain in `.cache/module-audit-logs/kdp-20261107/psepk-consultation/`; no provider report was manufactured.


## 2026-11-07 PR6179 round-one adjudication

Reviewed the source relation, core role and source-specific limits relevant to this gene. See `analysis/module_audits/bacterial_kdp_potassium_homeostasis/round1/evidence.md` for the full evidence and disagreement record. Original ordered annotation payloads, qualifiers and historical NEW/retired flags are preserved. GO0008556 now has a relation-specific overannotation judgment and probable source correction from enables to contributes_to; structural contribution remains core. KdpF requirement is conditional on the tested detergent-solubilized preparation, not universal native essentiality. [PMID:10608856; PMID:34272288].
