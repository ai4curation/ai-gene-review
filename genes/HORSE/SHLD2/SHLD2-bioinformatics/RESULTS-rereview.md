# SHLD2 (horse) re-review: all equine protein models vs human SHLD2

Script: `compare_isoforms_rereview.py` (run with
`uv run --with biopython --with requests python compare_isoforms_rereview.py`).
Sequences were downloaded from the UniProt REST API on 2026-10-20 and saved to
`horse_shld2_models_rereview.fasta`; the full numeric output is in
`compare_isoforms_rereview.json`. Global alignment, BLOSUM62, gap open -10, extend -0.5,
free end gaps. "Last conserved" is the end of the last 30-column window with at least 70%
identity.

## Gene models (Ensembl gene ENSECAG00000001626, SHLD2, horse chromosome 1)

Ensembl REST lookup (2026-10-20) lists seven protein-coding transcripts. The Ensembl
canonical transcript is ENSECAT00000122467 (protein ENSECAP00000090394 = UniProt
A0A9L0TUF0, 1047 aa, 10 exons). The benchmark accession A0A9L0RGD6 is ENSECAT00000102809
(ENSECAP00000060865, 883 aa, 8 exons), a non-canonical alternative transcript model.
QuickGO (2026-10-20) shows GO annotations (IBA from PANTHER node PTN001025652 and IEA
ortholog transfers from Q86V20) only on A0A9L0TUF0; A0A9L0RGD6 has none.

| Horse model | Length | Identity to human iso-2 (904 aa) | Human iso-2 coverage | Last conserved human iso-2 residue | Horse residue there |
|---|---|---|---|---|---|
| A0A9L0RGD6 (benchmark) | 883 | 73.7% | 90.8% | 799 | 811 |
| A0A9L0TUF0 (Ensembl canonical) | 1047 | 73.9% | 100% | 904 | 948 |
| F6W5G1 | 936 | 73.9% | 100% | 904 | 916 |
| A0A3Q2HUD4 | 971 | 73.9% | 100% | 904 | 951 |
| A0A9L0RPS9 | 986 | 73.9% | 100% | 904 | 966 |
| A0A3Q2I8C2 | 1008 | 73.9% | 100% | 904 | 909 |
| A0A9L0TSK2 | 843 | 74.5% | 92.8% | 827 | 831 |

## What A0A9L0RGD6 keeps and loses

- Its N-terminus (MSGGSQVHIFWGAPIGPLKM) starts at the position equivalent to human M1, so
  the human 1-60 region that is sufficient for SHLD3 and MAD2L2 binding is present.
- It contains the 69-residue OB-fold-B segment that distinguishes the long human product
  (UniProt Q86V20-2, 904 aa) from the short one (Q86V20-1, 835 aa).
- It retains the four cysteines of the OB-fold-C zinc ribbon (CAKC at horse 772-775 and
  CFSC at 790-793, aligning with human iso-1 699-702 and 717-720).
- Conservation ends after horse residue ~811 (human iso-2 799, iso-1 730). Horse residues
  ~812-883 are an Arg/Gly/Pro-rich sequence with no counterpart in human SHLD2 or in the
  canonical horse model, which instead continues collinearly with human through the
  human C-terminus. The benchmark model therefore lacks the equivalent of the last ~105
  residues of human SHLD2 (iso-1 731-835): the remainder of OB fold C after the zinc ribbon
  and the distal half of the region mapped as mediating SHLD1 interaction (human iso-1
  652-822). Its 8-exon structure versus 10 exons for the canonical model is consistent
  with an alternative 3' exon or intron read-through; no transcript evidence was examined.

## Interpretation

A0A9L0RGD6 is an alternative (non-canonical) gene-model product of horse SHLD2, not a
separate gene. Its family placement (PTHR14495:SF2, the single SHLD2 subfamily) and the
sequence above support orthology to human SHLD2. The truncated OB fold C means the
model cannot be assumed to keep the ssDNA-binding and SHLD1-binding functions that
human end-protection requires. The recruitment and SHLD3-REV7 binding module is intact.
