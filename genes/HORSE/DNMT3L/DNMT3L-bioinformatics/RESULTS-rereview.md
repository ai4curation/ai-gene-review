# DNMT3L re-review: horse gene models versus human and mouse DNMT3L

Script: `compare_models_rereview.py` (run with `uv run --with biopython --with requests python compare_models_rereview.py`); raw output and full alignments in `results-rereview.json`. Sequences are fetched live from UniProt; global alignment, BLOSUM62, gap open -10, extend -0.5, free end gaps.

## Horse gene models

Ensembl gene ENSECAG00000009690 (DNMT3L) has two protein-coding transcripts: ENSECAT00000080350 (Ensembl canonical; ENSECAP00000084444, 426 aa = UniProt A0A9L0T837, the benchmark accession) and ENSECAT00000010000 (ENSECAP00000007680, 403 aa = UniProt F6YVL8). No reviewed (Swiss-Prot) horse DNMT3L entry exists.

A0A9L0T837 and F6YVL8 are identical over their shared N-terminal 351 residues. F6YVL8 lacks four residues (RRDV, A0A9L0T837 268-271) and diverges after A0A9L0T837 residue 399, losing the conserved C-terminal tail (KNCFLPLREYFKYFSTEFTSSL) that A0A9L0T837 shares with human DNMT3L. A0A9L0T837 is therefore the more complete of the two horse models.

## Horse A0A9L0T837 versus human Q9UJW3

- 386 paired residues, 300 identical (77.7%); covers 100% of human DNMT3L and 90.6% of the horse protein.
- The unpaired horse residues are an N-terminal extension of 40 residues (horse 1-40) before the position aligned to human Met1. Mouse Q9CWR8 (421 aa) has a comparable extension (first residue paired to human: mouse 38), so the extension is shared with rodents and is not a horse-specific artefact.
- All cysteines in the human ADD domain (human 41-173) are conserved in horse (human C53, C55, C56, C73, C76, C96, C99, C100, C108, C113, C116, C118, C121, C142, C145 map to horse cysteines), as are H62 and H65. Human H135 aligns to horse Q175 (mouse has N at this position), so it is not a conserved ligand.
- Human Phe261, whose substitution F261A abolishes binding to DNMT3A (UniProt Q9UJW3 MUTAGEN, PMID:17713477), aligns to horse Phe301.
- Identity over human residues 300-386 (C-terminal part of the methyltransferase-like domain) is 69.0%, lower than the whole-protein figure but without gaps.

## Interpretation

A0A9L0T837 is a full-length product of the horse DNMT3L gene, not a fragment. It retains the ADD (cysteine-rich, H3-tail binding) domain and the DNMT3A-interface phenylalanine. It is in PANTHER subfamily PTHR23068:SF13 with human DNMT3L, so the human and mouse DNMT3L experimental findings transfer within the same subfamily. Like human DNMT3L, the horse protein is a methyltransferase-like domain without the catalytic motifs; this analysis does not test catalytic residues directly. Sequence conservation does not demonstrate horse-specific activity; no horse functional assay was found.
