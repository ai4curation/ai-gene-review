# ATAD3B notes

## 2026-10-05 review (PAINT, affinage)

- Mitophagy receptor [PMID:33665835 "ATAD3B contains a LIR motif that binds to LC3 and promotes oxidative stress-induced mitophagy in a PINK1-independent manner, thus promoting the clearance of damaged mtDNA induced by oxidative stress."]. This source is abstract-only. I added NEW GO:0140580 (IDA) and GO:0000423 (IMP). Comparators: BNIP3 carries both (IDA/IMP), FUNDC1 carries mitophagy (IGI).
- Topology switch [PMID:33665835 "Under normal conditions, ATAD3B hetero-oligomerizes with ATAD3A, thus promoting the targeting of the C-terminal region of ATAD3B to the mitochondrial intermembrane space."].
- Dominant-negative modulator of ATAD3A [PMID:22664726 "Using loss- and gain-of-function approaches, we show that ATAD3B associates with the ubiquitous ATAD3A species, negatively regulates the interaction of ATAD3A with matrix nucleoid complexes and contributes to a mitochondria fragmentation phenotype."]. Mitochondrion organization (IBA) is therefore kept as non-core.
- Walker A (352-359) is present (UniProt BINDING). No ATPase assay is reported in the cited sources, so ATP hydrolysis (IEA) is kept as non-core.
- The four Reactome neutrophil-degranulation rows (plasma membrane, secretory granule membrane, ficolin-1-rich granule membrane) are proteomics-derived, and the cached Reactome text does not name ATAD3B. Marked as over-annotated: ATAD3B is an inner-membrane mitochondrial protein, and ATAD3A peptides are near-identical.
- Not used: the 2026 SEC62/MASH paper (PMID:42001994), which is uncached.

## 2026-10-05 revision (reviewer round 1)

- Added NEW mitochondrial outer membrane (IDA, PMID:33665835) and made it the location of the mitophagy-receptor core function. The LC3-recruiting activity occurs where the C-terminus is exposed on the OMM under stress, not in the inner membrane. BNIP3L carries GO:0005741 (IMP).
- Added a second core function for the basal ATAD3A-modulator role, located in the inner membrane.
- Dropped the uninformative "Reactome text does not name ATAD3B" clause: cached Reactome files carry no participant lists. Also noted that ATAD3A carries none of those Reactome rows (QuickGO).
- The HTP row no longer quotes boilerplate. The MitoCoP per-protein data are in supplementary tables I have not checked.
- Walker A is noted as a UniProt prediction (ECO:0000255).
