# ssb curation notes

## 2026-08-08 pathway pass

The Q88QK5 HAMAP record states that SSB binds ssDNA and recruits partner proteins
during replication, recombination, and repair [file:PSEPK/ssb/ssb-uniprot.txt,
"Binds to ssDNA and to an array of partner proteins to recruit"]. Direct homolog
work shows RecO acting on SSB-coated ssDNA during RecA loading
[PMID:32297860, "facilitates the loading of RecA onto drSSB-coated ssDNA"]. SSB
is therefore a required but broadly shared substrate-protection component of the
RecFOR module.

## Annotation-reviewer pass (2026-09-01)

Consulted the annotation-reviewer workflow against all 5 current GOA rows and reviewed UniProt Q88QK5. Accepted single-stranded DNA binding, DNA replication, and nucleoid localization. Kept DNA repair and recombination as genuine non-core uses of the same SSB activity outside this module boundary. No GOA row remains pending.

## 2026-09-26 merge reconciliation

The 2026-09-01 annotation-reviewer pass reached `main` through the bacterial DNA
replication curation (#2918) while this RecFOR branch was open, and the two
passes disagree on scope rather than on biology. Both accept `GO:0003697` and
`GO:0006260`; they differ on whether `GO:0006281` and `GO:0006310` are core
(RecFOR pass: ACCEPT) or non-core uses of the same ssDNA-binding activity
(replication pass: KEEP_AS_NON_CORE), and correspondingly on whether `GO:0009295`
nucleoid is a core location. The merge defers to the later pass already on
`main`, so no merged verdict is reverted here, and keeps the RecFOR pass's
additive material: verbatim `supported_by` quotes on every row, the
PMID:32297860 single-molecule RecO/SSB reference, the `PP_0485` alias, the module
reference, and the suggested question and experiment. Whether SSB's repair and
recombination roles should be core for this broadly-used protein rather than
scoped per module is a curation-policy question flagged on #2419 for a
maintainer, not settled by this merge.
