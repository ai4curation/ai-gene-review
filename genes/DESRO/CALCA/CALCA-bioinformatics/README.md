# CALCA (DESRO) vCGRP mapping

## Objective
Locate a vampire bat CGRP-like peptide (vCGRP) sequence in Desmodus rotundus
transcripts by translating RNA sequences and scanning for peptide matches.

## Inputs
- vCGRP peptide sequence (from Kakumanu et al., Toxins 2019; MDPI 11:26)
- Desmodus rotundus RefSeq RNA FASTA

## Data sources
- NCBI TSA project: GABZ01 (Desmodus rotundus transcriptome shotgun assembly)
  - FASTA: https://sra-download.ncbi.nlm.nih.gov/traces/wgs03/wgs_aux/GA/BZ/GABZ01/GABZ01.1.fsa_nt.gz
- NCBI RefSeq assembly: GCF_022682495.2 (HLdesRot8A.1)
  - RNA FASTA: https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/022/682/495/GCF_022682495.2_HLdesRot8A.1/GCF_022682495.2_HLdesRot8A.1_rna.fna.gz

## Workflow
- `just download` — fetch RefSeq RNA FASTA
- `just download-tsa` — fetch TSA FASTA (GABZ01)
- `just search` — translate and scan RefSeq RNA for vCGRP peptide (exact or 1 mismatch)
- `just search-tsa` — translate and scan TSA contigs for vCGRP peptide
- `just test` — sanity check on a small synthetic transcript

## Outputs
- `results/vcgrp_hits.tsv` — candidate transcript hits
- `results/test_hits.tsv` — test run output
