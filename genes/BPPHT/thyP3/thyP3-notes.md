# thyP3 (Bacillus phage phi3T) — Curation Notes

## Overview
- **Gene symbol**: `thyP3`
- **UniProt ID**: `P07606` (`TYSY_BPPHT`)
- **Organism**: *Bacillus* phage phi3T (`NCBITaxon:10736`)
- **Product**: Thymidylate synthase (`TS`, `thyP3`; 279 aa, ~32.7 kDa; EC `2.1.1.45`)

## Biological Function and Mechanism
- **De novo dTMP biosynthesis**: `thyP3` encodes a 279-amino-acid thymidylate synthase (`EC 2.1.1.45`) that catalyzes the reductive methylation of `2'-deoxyuridine 5'-monophosphate` (`dUMP`) by `(6R)-5,10-methylene-5,6,7,8-tetrahydrofolate` to produce `dTMP` (`thymidine 5'-monophosphate`) and `7,8-dihydrofolate` [PMID:3924741; file:BPPHT/thyP3/thyP3-uniprot.txt].
- **Homology and prophage conversion**: The phage phi3T `thyP3` gene is virtually identical to the *Bacillus subtilis* chromosomal `thyA` gene (which itself originated from lysogenic integration/recombination of a phi3T/SPbeta-like prophage) and shares strong catalytic site conservation with T4 phage and eukaryotic thymidylate synthases, including the catalytic nucleophilic cysteine (`Cys146` in `thyP3`, corresponding to `Cys198` of *L. casei* TS) that forms a covalent bond at C6 of `dUMP` [PMID:3924741; file:BPPHT/thyP3/thyP3-uniprot.txt].

## Curation Decisions
- **Existing annotations**:
  - `GO:0004799` (`thymidylate synthase activity`, IEA): `ACCEPT`. Core enzymatic activity (`EC:2.1.1.45`).
  - `GO:0006231` (`dTMP biosynthetic process`, IEA): `ACCEPT`. Direct metabolic process catalyzed by `thyP3`.
  - `GO:0006235` (`dTTP biosynthetic process`, IEA): `KEEP_AS_NON_CORE`. De novo synthesis of dTMP by thymidylate synthase is a required upstream step in the broader dTTP biosynthetic pathway (`UniPathway:UPA00575`).
  - `GO:0008168` (`methyltransferase activity`, IEA), `GO:0016740` (`transferase activity`, IEA), and `GO:0016741` (`transferase activity, transferring one-carbon groups`, IEA): `TOO_GENERAL` (all entailed by `GO:0004799`).
  - `GO:0009165` (`nucleotide biosynthetic process`, IEA): `TOO_GENERAL` (entailed by `GO:0006231`).
