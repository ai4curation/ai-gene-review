# COX14 (Cytochrome c oxidase assembly protein COX14 / C12orf62) — review notes

UniProtKB: Q96I36. Human, 57 aa, single-pass transmembrane protein (~6.6 kDa).
Gene synonym: C12orf62. HGNC:28216.

## Core biology
COX14 is a small mitochondrial **inner-membrane** assembly factor for Complex IV
(cytochrome c oxidase). It is a core component of the **MITRAC** (mitochondrial
translation regulation assembly intermediate of cytochrome c oxidase) complex and acts
**early** in COX assembly: it associates with the newly-synthesised mtDNA-encoded core
subunit MT-CO1 (COX1) and, together with COA3/CCDC56 and other MITRAC components,
**couples/regulates MT-CO1 translation with its assembly** into the growing complex. It
is **non-catalytic** (no enzymatic MF).

- MITRAC core component with COA3 [PMID:23260140 abstract; UniProt SUBUNIT].
- Couples COX1 synthesis with COX assembly; required for early steps
  [PMID:22243966 "C12orf62 is required for coordination of the early steps of COX
  assembly with the synthesis of COX I"; UniProt FUNCTION].
- Binds COX1 and acts as its translation regulator (negative translation regulation of
  COX1, conserved from yeast COX14) [PMID:22356826 full text: "We experimentally confirm
  the role of C12orf62 as a COX assembly factor binding to COX1 and acting as its
  translation regulator"; "C12orf62 overexpression ... reveals lower levels of newly
  synthesized COX1"].
- Forms an early COX1-COA3-COX14 assembly intermediate (stabilised by CMC1) before COX4
  and COX5a incorporation [PMID:28082314 "CMC1 stabilizes a COX1-COA3-COX14 complex
  before the incorporation of COX4 and COX5a subunits"].

## Localization — inner membrane, NOT outer membrane
UniProt annotates "Mitochondrion outer membrane" (SL-0172 → GO:0005741), and the
APEX/topology paper PMID:27184847 was cited for it. However the protein is a MITRAC/COX
assembly factor that engages MT-CO1 in the **inner membrane**, and Reactome places COX14
in the **mitochondrial inner membrane** (GO:0005743) for every MITRAC reaction. Topology
in UniProt (FT): TOPO_DOM 1–14 "Mitochondrial intermembrane", TRANSMEM 15–37, TOPO_DOM
38–57 "Cytoplasmic" (= matrix) — i.e. a single-pass membrane protein spanning a
mitochondrial membrane with the C-terminus in the matrix, consistent with the inner
membrane where COX assembles. Treat GO:0005743 mitochondrial inner membrane as the
correct anatomical location; the outer-membrane annotations are likely a
subcellular-localization-vocabulary artefact / mis-assignment and are marked
over-annotated rather than accepted as core.

## Disease
Biallelic COX14 mutations cause **mitochondrial complex IV deficiency, nuclear type 10
(MC4DN10; MIM:619053)** — autosomal recessive, neonatal, Leigh-like/fatal neonatal lactic
acidosis; variant M19I [PMID:22243966; UniProt DISEASE].

## MF status
GOA carries only bare "protein binding" (GO:0005515, IPI PMID:32296183, with MESD/Q14696)
and "protein folding chaperone" (GO:0044183, IDA PMID:28082314). Neither is a genuine
catalytic MF. COX14 has no informative molecular-function term; it is a scaffolding/
adaptor assembly factor. Therefore `core_functions` omits `molecular_function` and uses
`directly_involved_in` (complex IV assembly) + `located_in` (GO:0005743).

## Term guidance
- Complex IV membership: current term GO:0045277 respiratory chain complex IV
  (GO:0005751 is OBSOLETE).
- Core BP: GO:0033617 mitochondrial respiratory chain complex IV assembly (current).
- Location: GO:0005743 mitochondrial inner membrane (current).

## GO:0044183 protein folding chaperone (IDA, PMID:28082314)
The cited paper (Bourens & Barrientos 2017) shows COX14 is part of an early COX1-COA3-COX14
assembly intermediate stabilised by CMC1; it does not demonstrate a classical
protein-folding chaperone activity for COX14 itself. This looks like an over-annotation of
a scaffolding/assembly-factor role as a "chaperone" MF. The derived IEA GO:0006457 protein
folding (GO_REF:0000108, inferred from GO:0044183) inherits the same weakness.
