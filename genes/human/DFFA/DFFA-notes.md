# DFFA apoptosis review notes

## Core identity

- DFFA is ICAD/DFF45, the regulatory subunit of the DNA fragmentation factor.
  It binds CAD/DFFB, assists productive folding of the CAD nuclease, and keeps
  CAD inactive until executioner caspases cleave DFFA during apoptotic
  execution.
- The central molecular split is important for curation: DFFA is not the
  endonuclease. CAD/DFFB performs DNA cleavage; DFFA folds CAD and inhibits CAD
  in the inactive DFF complex. Caspase-3 cleavage of DFFA releases the nuclease
  [PMID:9108473; PMID:11371636].
- DFFA has two separable activities. PMID:19944011 explicitly supports a
  C-terminal chaperone function that is dispensable for DFF40 inhibition,
  making `GO:0044183 protein folding chaperone` a conservative missing
  molecular-function annotation alongside the existing
  `GO:0060703 deoxyribonuclease inhibitor activity`.

## Curation choices

- Accepted `GO:0060703 deoxyribonuclease inhibitor activity` and
  `GO:1902511 negative regulation of apoptotic DNA fragmentation` as the core
  ICAD/CAD inhibition terms.
- Added `NEW` rows for `GO:0044183 protein folding chaperone` and
  `GO:0006457 protein folding` for the direct CAD folding activity supported
  by PMID:11371636 and PMID:19944011.
- Accepted `GO:0006309 apoptotic DNA fragmentation` with an explicit caveat:
  DFFA participates through CAD folding and inhibition, but DFFB is the
  executing DNase.
- Modified broad `GO:0006915 apoptotic process` and
  `GO:0042981 regulation of apoptotic process` to the specific
  `GO:1902511 negative regulation of apoptotic DNA fragmentation`.
- Removed generic high-throughput `protein binding` rows for DFFB, HSPB1, and
  TSPYL4 when they added only partner edges. The focused DFF40:DFF45 structural
  and biochemical papers carry the specific inhibitor/chaperone assertions.
- Kept the generic `GO:0032991 protein-containing complex` row as non-core
  because DFFA truly belongs to the DFF complex, but no GO term for the DNA
  fragmentation factor complex is present locally.

## Localization

- Retained cytosolic, nucleoplasmic, and chromatin annotations. Liu et al.
  purified DFF from HeLa cytosol [PMID:9108473], later work showed that a
  cytosolic CAD pool can be limiting for DNA laddering [PMID:22253444], and
  DFF40:DFF45 can be found in a chromatin-enriched fraction or transfected
  chromatin-associated pool [PMID:19882353; PMID:15572351].
- Reactome places DFFA/DFF45 in cytosolic DFF40:DFF45 association, importin
  binding and nuclear import, caspase-3 cleavage, and dissociation of DFFA
  fragments from active DFF40. These are consistent pathway locations rather
  than independent DFFA activities.
