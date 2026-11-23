2026-11-23: fetched PCK2 with `just fetch-gene human PCK2`; QuickGO returned 42 rows, so
`PCK2-goa.tsv` is not a failed header-only fetch.

`just deep-research human PCK2 --provider perplexity` failed because this checkout only had
`claude_code` configured. I used a manual review instead, centered on the fetched GOA rows, the
PCK2 UniProt record, the full-text kinetic paper PMID:28955899, the PCK2 cloning/expression
abstract PMID:8645161, the gene-structure/tissue-expression abstract PMID:9657976, and the 2024
ACSL4/ferroptosis study PMID:38720107.

Core PCK2 biology:

- PCK2 is the mitochondrial GTP-dependent PEPCK isozyme. Modaressi et al. cloned a human liver
  cDNA and showed that expression raised mitochondrial, not cytosolic, PCK activity in HEK293
  cells and rat hepatocytes.
- The 1998 follow-up mapped the human PCK2 gene and found expression in liver, kidney, pancreas,
  intestine and fibroblasts, fitting a mitochondrial isozyme that is broader than purely hepatic
  gluconeogenesis.
- Direct enzymology of human PCK2 established GTP-dependent conversion between oxaloacetate and
  phosphoenolpyruvate, with the oxaloacetate-to-PEP direction favored in vivo, and an absolute
  Mn2+ requirement.
- HEK293T PCK2 overexpression increased glucose and lipid production, supporting roles in both
  gluconeogenesis and glyceroneogenesis.

Non-core or over-annotated contexts:

- PCK2 has weak pyruvate-kinase-like activity in vitro, but this is not a physiological pyruvate
  biosynthetic process because the same kinetic study found the normal oxaloacetate-to-PEP
  reaction strongly favored.
- Ortholog transfers to beta-cell glucose response and insulin secretion are plausible but
  indirect for human; kept as non-core rather than core.
- PCK2 is not PCK1: PAINT terms for insulin stimulus, dexamethasone stimulus and hepatocyte
  differentiation sit on a node that covers both vertebrate PCK1 and PCK2, but the evidence is
  driven by cytosolic PCK hormone regulation and developmental-expression contexts, so these are
  over-annotated on PCK2.
- Li et al. reported a GTP-dependent, noncanonical PCK2 kinase function on ACSL4 Thr679 in
  tumor-cell ferroptosis models. I retained both the protein serine/threonine kinase row and the
  ferroptosis row as conditional/non-core.

PANTHER PTHR11561:

- The root node `PANTHER:PTN000169226` correctly carries the conserved PEPCK(GTP) activity, Mn2+
  binding, gluconeogenesis and oxaloacetate metabolism for both human paralogs.
- Human PCK1 leaf `PTN002480248` is in the vertebrate cytosolic PCK1 branch `PTN008520420`.
- Human PCK2 leaf `PTN002480250` is in the vertebrate mitochondrial PCK2 branch `PTN008520418`.
- `PTN008520418` is the right PCK2-only node for the mitochondrial matrix IBD and for the cytosol
  IRD that prevents cytosolic localization from propagating into vertebrate PCK2.
- `PTN000169230` propagates mitochondrion to both PCK1 and PCK2; the location is sound for PCK2
  but needs an IRD at `PTN008520420` to block the cytosolic PCK1 branch.
