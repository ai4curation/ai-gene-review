# GCV3 notes (YAL044C, P39726)

- H-protein of GCS, lipoyl carrier (Lys-102) [PMID:9020168 "is shown to code for the H-protein subunit of the multienzyme glycine cleavage system"]; needed for glycine as N source [PMID:9020168 "it is essential when glycine serves as the sole nitrogen source"].
- Moonlighting role in protein lipoylation: [PMID:19570983 "GCV3, encoding the H protein target of lipoylation, is itself absolutely required for lipoylation of Lat1 and Kgd2"]; K102 mutants abolish Lat1/Kgd2 lipoylation [PMID:19570983 "suggesting that the lipoylated form of Gcv3 is required for lipoylation of the E2 subunits, Lat1 and Kgd2"].
- Lipoylated in vivo [PMID:32974306 "Lipoyl-Gcv3p is the lipoic acid bound subunit of glycine cleavage system (GCV)."].

## Curation observations
- No GCS-specific GO MF term for the lipoyl/aminomethyl swinging-arm carrier; GO:0031405 lipoic acid
  binding used as the closest, while GO:0140104 molecular carrier activity may be an appropriate parent.
- protein lipoylation (IMP) accepted: Gcv3 is the first lipoylated intermediate in the relay, not just a substrate (same logic as Bacillus GcvH).

## 2026-11-10 glycine cleavage module completion pass (Claude, AI-assisted)

- Every row now carries a verbatim supporting quote; truncated UniProt quotes were completed to the end of the claim.
- Broad parent rows shared across the module's P/H/T/L reviews were harmonized: glycine metabolic/catabolic process (and amino acid metabolic process) -> MODIFY to GO:0019464; for the L proteins 2-oxoglutarate metabolic process and tricarboxylic acid cycle -> MODIFY to GO:0120551, generic oxidoreductase parents -> MODIFY to GO:0004148, FAD binding ACCEPT.
