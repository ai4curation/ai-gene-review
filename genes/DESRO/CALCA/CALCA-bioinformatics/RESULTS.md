# CALCA (DESRO) vCGRP mapping — Results

## Summary
- Searched both RefSeq RNA (GCF_022682495.2 HLdesRot8A.1; 58,773 transcripts) and the TSA contig set (GABZ01; 8,786 transcripts) for the 37-aa vCGRP peptide.
- No exact matches and no matches with ≤1 mismatch were found in translated transcripts for either dataset.
- The peptide may derive from transcripts not captured in these assemblies, may be highly divergent, or may require a more sensitive search strategy.

## Checklist
- [x] Scripts avoid hardcoded inputs/outputs
- [x] Script tested on at least one other input
- [x] Analyses completed as expected
- [x] Direct results saved in `results/`
- [x] Summary includes detailed provenance and justification

## Provenance
- vCGRP peptide sequence from Kakumanu et al., Toxins 2019 (MDPI 11:26)
- DESRO RNA FASTA from NCBI RefSeq (GCF_022682495.2 HLdesRot8A.1)
- DESRO TSA FASTA from NCBI WGS/TSA project GABZ01 (GABZ01.1.fsa_nt.gz)

## Commands
- `just download`
- `just search`
- `just test`

### Runs completed
- Exact search: `python scripts/search_peptide_in_transcripts.py --rna-fasta data/desro_rna.fna.gz --peptide-fasta data/vcgrp_peptide.faa --max-mismatch 0 --out-tsv results/vcgrp_hits_exact.tsv`
- 1-mismatch search: `python scripts/search_peptide_in_transcripts.py --rna-fasta data/desro_rna.fna.gz --peptide-fasta data/vcgrp_peptide.faa --max-mismatch 1 --out-tsv results/vcgrp_hits_mm1.tsv`
- TSA exact search: `python scripts/search_peptide_in_transcripts.py --rna-fasta data/GABZ01.1.fsa_nt.gz --peptide-fasta data/vcgrp_peptide.faa --max-mismatch 0 --out-tsv results/vcgrp_hits_tsa_exact.tsv`
- TSA 1-mismatch search: `python scripts/search_peptide_in_transcripts.py --rna-fasta data/GABZ01.1.fsa_nt.gz --peptide-fasta data/vcgrp_peptide.faa --max-mismatch 1 --out-tsv results/vcgrp_hits_tsa_mm1.tsv`
- Test run: `python scripts/search_peptide_in_transcripts.py --rna-fasta data/test_transcripts.fna --peptide ACDE --max-mismatch 0 --out-tsv results/test_hits.tsv`

## Results files
- `results/vcgrp_hits_exact.tsv` (0 hits)
- `results/vcgrp_hits_mm1.tsv` (0 hits)
- `results/vcgrp_hits_tsa_exact.tsv` (0 hits)
- `results/vcgrp_hits_tsa_mm1.tsv` (0 hits)
- `results/test_hits.tsv` (1 hit)
