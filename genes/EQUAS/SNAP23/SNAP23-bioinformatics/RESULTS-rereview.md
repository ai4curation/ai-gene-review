# SNAP23 (donkey) re-review: gene-model and family placement

Added 2026-10-21. Supplements `RESULTS.md` (left unchanged).

## 1. Transcript structure (Ensembl REST, queried 2026-10-21)

Reproduce from this folder:

```
uv run --script compare_transcripts_rereview.py ENSEASG00005013173 ENSEAST00005020804 ENSEAST00005020803
```

Output (`transcripts_rereview_output.txt`):

```
Gene ENSEASG00005013173 SNAP23 chr2:191091543-191106545 strand -1
ENSEAST00005020800	biotype=protein_coding	ensembl_canonical=1	exons=8	protein=ENSEASP00005019164	length=222
ENSEAST00005020803	biotype=protein_coding	ensembl_canonical=0	exons=7	protein=ENSEASP00005019167	length=211
ENSEAST00005020804	biotype=protein_coding	ensembl_canonical=0	exons=5	protein=ENSEASP00005019168	length=97
ENSEAST00005060473	biotype=protein_coding	ensembl_canonical=0	exons=6	protein=ENSEASP00005047854	length=158
ENSEAST00005081845	biotype=protein_coding	ensembl_canonical=0	exons=6	protein=ENSEASP00005061071	length=209

Exons of ENSEAST00005020804 (5'->3' on gene strand):
  191106442-191106545	shared with canonical
  191105894-191105935	shared with canonical
  191105210-191105258	shared with canonical
  191104353-191104470	shared with canonical
  191100026-191100121	NOT in canonical
```

Interpretation: the benchmark entry A0A8C4M285 (ENSEASP00005019168, 97 aa) is encoded by an
alternative transcript of the single donkey SNAP23 gene. It shares the first four exons with
the transcript of the UniProt gene-centric canonical product A0A8C4M333 (ENSEAST00005020803,
211 aa, same length as human SNAP-23a O00161-1), then ends in an alternative terminal exon
(191100026-191100121) that encodes the 8-residue tail FNIRSRAQ and the stop codon. The
benchmark product is therefore an alternative-splice (alternative terminal exon) gene model,
not a separate gene. It is not equivalent to human isoform SNAP-23b, which lacks human
residues 90..142 but retains the C-terminal SNARE motif.

The UniProt gene-centric canonical product for this gene (proteome UP000694387) is
A0A8C4M333 (queried 2026-10-21 via `rest.uniprot.org/genecentric`). No transcript-support or
expression evidence for ENSEAST00005020804 was available to this analysis.

## 2. PANTHER placement (UniProt cross-references, queried 2026-10-21)

All five donkey SNAP23 UniProt entries (A0A8C4M285, A0A8C4M333, A0A8C4M5X5, A0A9L0K6I4,
A0A9L0J3X0) are assigned to PTHR19305:SF4 (SYNAPTOSOMAL-ASSOCIATED PROTEIN 23), the subfamily
that also contains reviewed human O00161, mouse O09044 and rat O70377
(`interpro/panther/PTHR19305/PTHR19305-entries.csv`). Human SNAP25 (P60880) sits in a different subfamily,
PTHR19305:SF5, of the same entries file. The donkey TreeGrafter rows cite PANTHER:PTN000447812.
