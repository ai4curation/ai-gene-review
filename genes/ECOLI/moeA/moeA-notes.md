# moeA (P12281) notes, E. coli K-12

Deep research providers were unavailable for this session (no API keys), so no
`-deep-research-<provider>.md` file exists. The review is built from the UniProt record
and the cached publications (all abstract-only except PMID:18304323 and PMID:24561554).

## Identity

- UniProt P12281, molybdopterin molybdenumtransferase, EC 2.10.1.1; synonyms bisB, chlE,
  narE; b0827. MoeA family (PANTHER PTHR10192, Pfam MoeA_N / MoCF_biosynth / MoeA_C).
- Curated function [file:ECOLI/moeA/moeA-uniprot.txt "Catalyzes the insertion of molybdate into adenylated molybdopterin with the concomitant release of AMP."] (ECO:0000269, PMID:15632135).

## Biochemistry

- Purified MoeA ligates Mo (and less well W) to MPT; MogA stimulates with ATP/Mg
  [PMID:15632135 "MoeA is responsible for mediating molybdenum ligation to molybdopterin, whereas MogA stimulates this activity in an ATP-dependent manner"].
  The later identification of MPT-AMP as the MogA product explains the ATP dependence.
- moeA(-) and mogA(-) cells make MPT but cannot insert Mo
  [PMID:12006571 "moeA(-) and mogA(-) cells are able to synthesize molybdopterin, but both are deficient in molybdenum incorporation"].
- Structures: dimer, active site across the interface
  [PMID:11525167 "The active form of MoeA is a dimer"]; PMID:11428898 also shows a dimer and
  domain 3 resembling MogA. Mg2+ bound per subunit (UniProt COFACTOR, PMID:11428898).
- PMID:9515915 (sulfide suppression, thiomolybdate model) is historical context.

## Curation decisions

- Bare protein binding (three IPI rows) removed per policy; interactions are real
  (MogA/MobA/MobB, Moco-dependent; PMID:12372836).
- Cytoplasm IBA MODIFY to cytosol (gene has cytosol IDA and IBA). Same in PSEPK/moeA.
- GO:0032324 MODIFY to GO:0006777 (Mo-specific descendant the gene carries).
- GO:0042802 identical protein binding MODIFY to GO:0042803 (structurally defined dimer).
- No crossover rows: the E. coli MoeA GOA set carries no MogA adenylyltransferase term.
  Note the PANTHER subfamily PTHR10192:SF5 is named GEPHYRIN (the fused MogA-MoeA protein),
  which is only a family name.
