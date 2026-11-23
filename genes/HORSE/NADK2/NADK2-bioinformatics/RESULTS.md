# NADK2 (horse, A0A3Q2GYY5) gene-model comparison

Script: `compare_gene_models.py` (PEP 723; `uv run --script compare_gene_models.py`).
Raw output: `compare_gene_models.out`. Sequences fetched live from UniProt REST
(2026-10-21). Global alignment, BLOSUM62, gap open -10, extend -0.5, against
reviewed human NADK2 Q4G0N4 (442 aa, isoform 1).

## Horse NADK2 TrEMBL entries (UniProt query gene:NADK2 organism_id:9796)

| Accession | Length | Ensembl transcript | vs human Q4G0N4 |
|---|---|---|---|
| A0A3Q2GYY5 (benchmark) | 560 | ENSECAT00000031483.2 | 96-aa N-terminal extension + 22-aa internal insertion after human pos 287 |
| F7DCV0 | 538 | ENSECAT00000021219.3 | 96-aa N-terminal extension only |
| A0A3Q2H586 | 411 | ENSECAT00000036795.3 | starts at the human start Met; lacks human 288..319 (the human isoform-2 exon) |
| A0A3Q2GS26 | 510 | ENSECAT00000039783.3 | named "NAD(+) kinase" (not aligned here) |

No reviewed (Swiss-Prot) horse NADK2 entry exists.

## Benchmark A0A3Q2GYY5

- Identity to human over the aligned 442 columns: 428/442 (96.8%).
- The human start motif `MTCYRGF` begins at horse residue 97; residues 1..96
  (`METGTQ...APATPM`) have no counterpart in human or mouse NADK2 and overlap
  the MobiDB-lite disordered, polar/low-complexity regions annotated on the
  entry. This looks like an upstream in-frame start in the Ensembl model. If it
  were used, the predicted mitochondrial transit peptide (human 1..62) would no
  longer be N-terminal, so the extension is not presumed to be the native
  N-terminus.
- The 22-aa insertion `MSYSWAVAVDNLRRSIPTLKGL` after human position 287 matches
  the 22-aa segment `MPYCWAVAVDNLRRDIPNLKGL` present in canonical mouse NADK2
  (Q8C5H8), so it is a conserved alternative exon, not an artefact.
- Catalytic motifs are present: GGDG motif (`AAGGDGT`) at horse 253 (human 157);
  NE/D short motif (`ALNEVF`) at horse 370 (human 274). The residues that replace
  the Ppnk NAD-site Asp/Thr/Tyr in NADK2 (human Ser-306, Lys-317, Trp-319,
  PMID:23212377) map to horse Ser-424, Lys-435 and Trp-437, all conserved.

## Conclusion

A0A3Q2GYY5 is one of several Ensembl transcript models of the single horse
NADK2 gene. It carries the complete NAD kinase catalytic domain with every
motif identified for human NADK2, so it is not a fragment. It differs from the
human canonical product by a probably non-native N-terminal extension and a
mouse-type alternative exon.
