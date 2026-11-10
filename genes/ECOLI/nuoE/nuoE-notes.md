# nuoE (E. coli K-12, P0AFD1) notes

## 2026-10-23 / 2026-11-01 review session

Deep-research providers are unavailable in this environment (no API keys), so
literature was reviewed manually from the cached publications/ files and the
UniProt record. Most cached papers are abstract-only (exceptions: PMID:18316732,
PMID:9495756, PMID:24561554 full text).

- NuoE is the [2Fe-2S] subunit (cluster N1a) of the NADH dehydrogenase fragment
  (NuoE/F/G) of NDH-1 [PMID:15922336 "These clusters were assigned to clusters N3
  and N1a, respectively."].
- N1a is reduced by NADH via FMN very fast in E. coli complex I
  [PMID:18316732 "The major part of N1a undergoes very fast reduction with a time
  constant"], but lies on a side path [PMID:18316732 "with the exception of N1a,
  which curiously appears to be on a"]; Thermus structure: FMN within reach "of
  the distal cluster N1a, a possible antioxidant" [PMID:16469879].
- N1a ligand mutants lose NADH oxidase activity and also lose N1b on NuoG
  [PMID:28509551 "the content of binuclear cluster N1b located on a neighboring
  subunit was significantly decreased"].
- Every nuo gene is needed for a functional complex [PMID:22063474 "Thus, all
  nuo-genes are required either for the assembly or the stability of a functional
  E. coli complex I."]; NuoEFG accumulate in the cytoplasm when the membrane arm
  is missing.

Decisions:
- Subunit MF: GO:0009055 electron transfer activity (NEW, IDA PMID:18316732);
  complex MF contributes_to GO:0008137; GO:0003954 contributes_to accepted.
- FMN binding (contributes_to, IDA) marked over-annotated: FMN is on NuoF.
- Generic oxidoreductase activity (IEA) and proton transmembrane transport (IEA
  inference) marked over-annotated for this peripheral, non-catalytic subunit.
- membrane -> plasma membrane; NADH dehydrogenase complex -> respiratory chain
  complex I (MODIFY). Bare protein binding (NuoG IPI x2) removed per policy.
- No GO:0050136 (non-electrogenic) row exists for E. coli nuoE.
- PMID:9593861 (Friedrich 1998 review) has no abstract in cache; ISS row accepted
  on independent EPR/mutagenesis evidence.

Family: PANTHER PTHR10371:SF3 (same SF as P. putida Q88FH4); family review
interpro/panther/PTHR10371/PTHR10371-review.yaml.
