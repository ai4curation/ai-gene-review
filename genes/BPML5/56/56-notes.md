# Curation Notes: Mycobacterium phage L5 Gene 56 (gp56, Q05266)

## Overview
- **UniProt ID:** Q05266 (`VG56_BPML5`)
- **Gene Symbol:** `56`
- **Length:** 103 amino acids (11.7 kDa)
- **Genomic Context:** Encoded on the leftwards-transcribed right arm of the Mycobacterium phage L5 genome [PMID:8459766], located in the early lytic replication/metabolism cluster near the phage-encoded class II ribonucleotide reductase (`gp50`) and replication proteins (`gp57`–`gp65`).

## Literature & Biochemical Evidence
- **Primary characterization ([PMID:24913246]):**
  - Datta et al. (2014) purified and biochemically characterized L5 gp56 as a novel member of the NrdH family of redoxins [PMID:24913246].
  - Sequence and phylogenetic analysis show that gp56 contains a glutaredoxin fold (residues 9–103, `PF00462` / `IPR011911` / `cd02976` / `PTHR34386:SF1`) with a conserved active-site CXXC motif (`CPPC`, residues 19–22) and a non-catalytic third cysteine (`Cys80`) near the C-terminus [PMID:24913246].
  - Reduced gp56 catalyzes the reduction of protein disulfide bonds in vitro (insulin disulfide reduction assay) [PMID:24913246].
  - Like bacterial NrdH proteins, gp56 is reduced by NADPH via mycobacterial thioredoxin reductase (TrxR), although less efficiently than host thioredoxin TrxB [PMID:24913246].
  - Both reduced gp56 and host TrxB are capable of reducing L5 gp50, the phage-encoded class II ribonucleotide reductase, to support dNTP synthesis, although gp56 requires more reducing equivalents than TrxB [PMID:24913246].
  - Under oxidizing conditions, Cys80 forms inter-subunit disulfide linkages leading to higher-order oligomers; thus gp56 functions optimally in a reducing intracellular environment [PMID:24913246].

## Domain & Family Architecture
- **CDD:** `cd02976` (`NrdH`, E-value)
- **InterPro:** `IPR011911` (`GlrX_YruB`), `IPR002109` (`Glutaredoxin`), `IPR046372` (`Glutaredoxin_CS`), `IPR036249` (`Thioredoxin-like_sf`)
- **PANTHER:** `PTHR34386:SF1` (`GLUTAREDOXIN-LIKE PROTEIN NRDH`)
- **Pfam:** `PF00462` (`Glutaredoxin`)
- **PROSITE:** `PS51354` (`GLRX_2`, Glutaredoxin domain profile, residues 9–103)

## GO Annotation Decisions
- Currently no GOA annotations exist for `Q05266`.
- Propose `NEW` experimental annotations from [PMID:24913246]:
  - `GO:0015035` (`protein-disulfide reductase activity`, IDA, `PMID:24913246`): directly demonstrated by insulin disulfide reduction and gp50 reduction assays.
  - `GO:0045454` (`cell redox homeostasis`, IDA, `PMID:24913246`): standard biological process for NrdH/thioredoxin-like protein disulfide oxidoreductases.
  - `GO:0009263` (`deoxyribonucleotide biosynthetic process`, IDA, `PMID:24913246`): serves as the physiological electron donor for the phage-encoded ribonucleotide reductase gp50.
