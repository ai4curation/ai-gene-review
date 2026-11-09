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
