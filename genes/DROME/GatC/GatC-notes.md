# GatC (Q86BL4; CG33649) review notes

## Identity
- Small non-catalytic GatC subunit of mitochondrial GatCAB (human GATC ortholog).
  [file:DROME/GatC/GatC-uniprot.txt "This subunit probably forms a belt"].
- Named in [PMID:26761199 "CG5463 and CG33649 genes – we propose to name the latter two GatB and GatC, respectively"].
- No fly experimental data.

## Decisions
- Complex, mitochondrion, matrix (IC) accepted; obsolete GO:0070681 -> GO:0043685;
  mitochondrial translation non-core.
- Regulation of translational fidelity (InterPro): over-annotation; GatCAB is biosynthetic.
- ND root MF: kept non-core; no contributes_to MF proposed because human GATC carries none
  (comparator check via QuickGO), so the core function lists complex + process only.

## Deep research (falcon)
- GatC is the predicted non-catalytic assembly subunit: [file:DROME/GatC/GatC-deep-research-falcon.md "rather than an independently acting glutaminyl-tRNA synthetase"].
