# atg-3 (Q9N369, Y55F3AM.4) review notes

## Provenance / process
- UniProt has two TrEMBL entries for atg-3: Q9N369 (305 aa, full-length) and U4PRD2 (96 aa fragment/short isoform). Q9N369 was used (fetched with `just fetch-gene worm Q9N369 --alias atg-3`). The module does not cite an accession for ATG-3.
- Deep research failed (falcon timeout; perplexity-lite fallback killed, exit 137). No deep-research file; review based on cached publications and PubMed.

## Key evidence
- "Lipidation of LGG-1 and LGG-2 is mediated by 2 enzymes, ATG-7 and ATG-3." [PMID:27046254]
- atg-3 mutants are the autophagy-null reference in the EPG-7 paper: "levels of SQST-1 are dramatically elevated in atg-3 and epg-7 mutant embryos in an immunoblotting assay"; "Levels of EPG-7 are dramatically elevated and a large number of EPG-7 aggregates are formed in atg-3 mutants." [PMID:23530068]
- "No direct interactions were detected between EPG-7 and ATG-3, ATG-7, or ATG-5 in the pull-down assay" [PMID:23530068].

## Decisions
- ACCEPT Atg8-family conjugating enzyme activity (IBA) as core MF.
- MODIFY generic ubiquitin-like protein transferase (InterPro Atg3/Atg10, IEA) to GO:0141046.
- NEW GO:0061739 (ATG-3 catalyses the transfer to PE; comparator: yeast Atg3 GO:0006501 IDA/IMP, human ATG7 GO:0061739 IDA).
- Nucleophagy, glycophagy, mitochondrion autophagy IBAs kept as non-core.
- macroautophagy "IDA" from PMID:23530068 is really a mutant phenotype, but the term is right; accepted.
