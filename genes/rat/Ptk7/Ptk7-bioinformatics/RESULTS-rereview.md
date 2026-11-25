# Ptk7 re-review (2026-10-21): rat gene models and PANTHER classification

Script: `compare_rat_models_rereview.py` (PEP 723; `uv run --script compare_rat_models_rereview.py > RESULTS-rereview-raw.txt`).
Raw output: `RESULTS-rereview-raw.txt`. Sequences are fetched live from UniProt REST; the PANTHER row is read from the
official PANTHER 19.0 rat sequence-classification file.

## 1. Two rat Ptk7 TrEMBL gene-model products

| Accession | Length | N-terminal 40 residues | SignalP signal peptide (UniProt) | Ensembl transcript |
|---|---|---|---|---|
| A0A8I6ALM9 (benchmark; RGD GAF product) | 1079 | MGRAWRGALLPMPARRARVPPCKFRGKAGTPDGPTGAHSA | none called | ENSRNOT00000118183 (Ptk7-202, Ensembl canonical) |
| A0A8I6AKN3 | 1062 | MGARQLPLLRALLLPLLAGAHSAIVFIKEPSSQDALQGRR | SIGNAL 1..22 | ENSRNOT00000108486 (Ptk7-201) |
| Q8BKG3 (mouse PTK7, Swiss-Prot) | 1062 | MGARPLTLLRALLLPLLAGAQAAIVFIKEPSSQDALQGRR | SIGNAL 1..22 | - |
| Q13308 (human PTK7, Swiss-Prot) | 1070 | MGAARGSPARPRRLPLLSVLLLPLLGGTQTAIVFIKQPSS | SIGNAL 1..30 | - |

Global alignment blocks (BLOSUM62, gap open -10, extend -0.5):

- A0A8I6ALM9 36-1079 aligns to A0A8I6AKN3 19-1062 with 1044 identities (identical over the whole block).
- A0A8I6ALM9 36-1079 aligns to mouse Q8BKG3 19-1062 with 1012 identities.
- A0A8I6AKN3 1-1062 aligns to mouse Q8BKG3 1-1062 with 1028 identities.

Interpretation: A0A8I6ALM9 and A0A8I6AKN3 are products of the same rat Ptk7 gene (ENSRNOG00000039976, RGD:1310472) that
differ only at the N-terminus. A0A8I6ALM9 replaces the conserved hydrophobic signal peptide (residues 1-18 of
A0A8I6AKN3, matching mouse 1-18) with an unrelated arginine-rich 35-residue segment. Everything downstream (seven
Ig-like domains, transmembrane helix, pseudokinase domain) is identical between the two rat products. A0A8I6ALM9 is
therefore an alternative gene model whose 5' end does not encode the signal peptide that is conserved in mouse and
human PTK7 and in the other rat model; whether a signal-peptide-less product is made in vivo, and what topology it
would adopt, is not known. Neither rat entry is reviewed (Swiss-Prot).

## 2. Official PANTHER 19.0 rat classification row

```
RAT|RGD=1310472|UniProtKB=A0A8I6ALM9	A0A8I6ALM9	Ptk7	PTHR24418:SF399	TYROSINE-PROTEIN KINASE	MEGAKARYOCYTE-ASSOCIATED TYROSINE-PROTEIN KINASE
```

Column 4 assignment for A0A8I6ALM9 in PTHR19.0_rat: PTHR24418:SF399 (MEGAKARYOCYTE-ASSOCIATED TYROSINE-PROTEIN KINASE).

A0A8I6AKN3 has no row in the PANTHER 19.0 rat file.

The current UniProt record for A0A8I6ALM9 instead carries PTHR45080:SF21 (INACTIVE TYROSINE-PROTEIN KINASE 7), the
subfamily that holds human Q13308, mouse Q8BKG3 and chicken Q91048 (interpro/panther/PTHR45080/PTHR45080-entries.csv).
PTHR24418:SF399 is the MATK subfamily of the non-receptor tyrosine kinase family PTHR24418 (Csk/Src/Tec). MATK-family
proteins have an SH3-SH2-kinase architecture; the rat Ptk7 product has no SH2 or SH3 domain (no SH2/SH3 InterPro,
Pfam, SMART or PROSITE match in its UniProt record) and instead has seven Ig-like domains and a transmembrane helix.
The PANTHER 19.0 placement of rat Ptk7 in the MATK subfamily is therefore inconsistent with its domain architecture and
with the placement of its mouse and human orthologs.

Consequence for GO: the two rat IBA rows come from PTHR24418 nodes, not from the PTK7 subfamily:

- GO:0004715 non-membrane spanning protein tyrosine kinase activity, PANTHER:PTN001231168 (IBD seed FB:FBgn0262081, Drosophila Csk).
- GO:0005886 plasma membrane (is_active_in), PANTHER:PTN002521457 (seeded by Src/Tec/Csk-family kinases).

Conversely, the IBA annotations human PTK7 receives from PTHR45080 nodes (e.g. GO:0005911 cell-cell junction and
GO:0060828 regulation of canonical Wnt signaling pathway, both IBD at PANTHER:PTN000701324, taxon:32524 Amniota, in
interpro/panther/PTHR45080/PTHR45080-paint.tsv) do not reach rat Ptk7.
