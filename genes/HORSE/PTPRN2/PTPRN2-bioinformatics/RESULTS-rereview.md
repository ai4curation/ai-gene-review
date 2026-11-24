# PTPRN2 (horse): gene-model re-review, 2026-10-20

Script: `compare_horse_models_rereview.py` (run with `uv run --python 3.12 compare_horse_models_rereview.py`).
Raw output: `results-rereview.json`. The script fetches the sequences live from UniProt and Ensembl; nothing is hardcoded.

## Horse PTPRN2 gene models

Ensembl gene ENSECAG00000012762 (display name PTPRN2) has eight protein-coding models in UniProtKB/TrEMBL, all in PANTHER PTHR46106:SF5 (RECEPTOR-TYPE TYROSINE-PROTEIN PHOSPHATASE N2): A0A9L0T4W6, A0A9L0RAE3, A0A9L0R212, A0A9L0RHF7, F6S989, A0A9L0RER4, A0A9L0R2U6 and A0A9L0T2L9. None is Swiss-Prot reviewed. A0A9L0RAE3 (1054 aa, transcript ENSECAT00000125162, PTPRN2-205) is the model in the UniProt gene-centric canonical reference proteome UP000002281; the benchmark accession A0A9L0T4W6 (976 aa, ENSECAT00000094767, PTPRN2-208) is not.

## The benchmark model has a non-conserved C-terminal tail

All ten proteins (human Q92932, mouse P80560 and the eight horse models) contain the PTP signature motif HCSDGAGRSG with the catalytic cysteine (human Cys945, horse A0A9L0T4W6 Cys897). Human and mouse PTPRN2 and seven of the eight horse models have an identical 62-residue sequence after the motif, ending in ...PGMVQTKEQFEFALTAVAEEVNAILKALPQ. In A0A9L0T4W6 only the first 15 of those residues (TYVLIDMVLNKMAKG) are retained; the remaining 47 conserved residues are replaced by 56 unrelated residues ending in ...LPVRGRHCRRSHTGWKTIRVLCTSRSLLGS.

The divergence comes from the gene model: the last coding exon of ENSECAT00000094767 (ENSECAE00000523854, 184 bp, chromosome 4) is not used by the canonical transcript ENSECAT00000125162, whose coding sequence continues into two further 3' exons instead. A0A9L0T4W6 therefore uses an alternative terminal exon that is not supported by conservation with human, mouse or the other horse models.

Mapped onto human Q92932, whose PTP domain spans residues 745-1005, the replaced segment corresponds to human residues 969-1015: the final 37 residues of the phosphatase-like domain and the cytoplasmic C-terminus. The benchmark protein retains the signal peptide, the luminal IA-2 domain, the transmembrane helix and the catalytic-cysteine loop. Its PTP domain is incomplete at the C-terminal end, so whether it folds and is catalytically competent is untested.

The benchmark product is also 87 residues shorter than the canonical model upstream of the catalytic motif (Cys897 against Cys984 in A0A9L0RAE3), consistent with alternative exon use in the luminal/juxtamembrane region.

## Limits

This is a sequence and gene-model comparison, not a structure prediction or an assay. Whether the PTPRN2-208 transcript is expressed in horse tissues is not addressed here.
