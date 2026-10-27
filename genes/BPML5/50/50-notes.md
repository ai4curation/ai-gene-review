# Curation Notes: Mycobacteriophage L5 gene 50 (Adenosylcobalamin-dependent ribonucleoside-triphosphate reductase Gp50, Q05262)

## Summary
- **Gene symbol**: `50`
- **UniProt ID**: `Q05262` (`VG50_BPML5`)
- **Organism**: Mycobacterium phage L5 (`NCBITaxon:31757`)
- **Protein length**: 682 amino acids (76,331 Da)
- **EC number**: EC 1.17.4.2 (ribonucleoside-triphosphate reductase, thioredoxin-disulfide)

## Literature & Bioinformatic Findings
- First identified in the complete genome sequence of mycobacteriophage L5 [PMID:8459766, "We describe here the complete DNA sequence of the L5 genome and initial characterization of L5 virion structure and gene expression."].
- Overexpressed in *E. coli* and biochemically characterized by Bhattacharya et al. (2008), establishing that Gp50 is a functional class II adenosylcobalamin (vitamin B12)-dependent ribonucleotide reductase (RNR) with properties resembling the *Lactobacillus leichmannii* class II RNR (which reduces ribonucleoside triphosphates directly to deoxyribonucleoside triphosphates) [PMID:18248423, "It was established that Gp50 was a class II RNR having properties similar to that of the corresponding enzyme from Lactobacillus leichmanni, whereas Gp48 was a flavin-dependent thymidylate synthase (ThyX) that resembled the Paramecium bursaria chlorella virus-1 ThyX enzyme in its properties."].
- Expressed early during lytic growth and co-immunoprecipitates with the phage-encoded flavin-dependent thymidylate synthase Gp48 (ThyX) [PMID:18248423, "Gp48 and 50 were also found to coimmunoprecipitate, which indicates the possible existence of an L5 thymidylate synthase complex."].
- Kirtania et al. (2014) demonstrated that both the phage-encoded NrdH-like redoxin Gp56 and host mycobacterial thioredoxin TrxB can reduce the active-site disulfide of Gp50 to support ribonucleotide reduction [PMID:24913246, "The abilities of Gp56 and TrxB to reduce Gp50, the L5-encoded ribonucleotide reductase, was examined. While both are capable of executing this function, the former needs more reducing equivalents in the process as compared with the latter."].

## Review of Existing GOA Annotations
- `GO:0008998` (`ribonucleoside-triphosphate reductase (thioredoxin) activity`, both IDA and IEA rows), `GO:0031419` (`cobalamin binding`), and `GO:0000166` (`nucleotide binding`) are accepted (`ACCEPT`) as core molecular functions.
- `GO:0004748` (`ribonucleoside-diphosphate reductase activity, thioredoxin disulfide as acceptor`) is modified (`MODIFY`) to `GO:0008998` (`ribonucleoside-triphosphate reductase (thioredoxin) activity`) because Gp50 is an EC 1.17.4.2 class II ribonucleoside-triphosphate reductase resembling the *L. leichmannii* enzyme rather than a ribonucleoside-diphosphate reductase (EC 1.17.4.1).
- `GO:0006260` (`DNA replication`) is modified (`MODIFY`) to `GO:0009263` (`deoxyribonucleotide biosynthetic process`) because RNR catalyzes the de novo synthesis of deoxyribonucleotide precursors rather than directly performing DNA strand polymerization.
- `GO:0016491` (`oxidoreductase activity`) is marked `TOO_GENERAL` because it is entailed by `GO:0008998`.
