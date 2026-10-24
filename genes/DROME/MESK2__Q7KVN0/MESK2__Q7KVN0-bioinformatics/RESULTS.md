# MESK2 (Q7KVN0): full-text check of the ABPP evidence

Script: `abpp_fulltext_extract.py` (fetches PMC7610703 XML from NCBI E-utilities; run with
`uv run --no-project python abpp_fulltext_extract.py`). Raw output: `abpp_fulltext_extract.out`.

The cached `publications/PMID_33827210.md` holds only the abstract. This script reads the
full text so that the HDA "serine hydrolase activity" row on Q7KVN0 can be judged on what
the paper actually reports for MESK2.

## What the paper reports for MESK2

- MESK2 appears in Table 1 ("List of SHs showing sexual dimorphism in activities in adult fly")
  in the metabolic-SH block:
  `MESK2 | Unknown hydrolase | Male | Head | Ahmed et. al., 2020`.
  The "Unknown hydrolase" label is the authors' sequence-homology category from their in
  silico SH list, not a measured activity.
- The LC-MS/MS ABPP identifies proteins by peptide counts after FP-biotin labelling and
  avidin enrichment; protein-level identification, not identification of a probe-modified
  peptide or residue.
- The heat-denatured control described in the text is for the gel-based ABPP; no
  inhibitor-competition, no-probe or heat-denatured control is described for the
  protein-level LC-MS/MS identifications, and no MESK2-specific follow-up is reported.

## Interpretation

- The data show that MESK2 is recovered by FP-biotin/avidin enrichment from adult male head
  proteome. That is consistent with probe reactivity of some MESK2 residue, but it is also
  consistent with co-enrichment, because enrichment is scored at the protein level.
- Independent sequence evidence (genes/DROME/MESK2/MESK2-bioinformatics/RESULTS-rereview.md)
  shows that Q7KVN0 has Gly152 at the nucleophile-elbow position (IGFGVGAGANI) that carries
  the catalytic serine in active alpha/beta hydrolases, matching human NDRG2, whose crystal
  structure lacks the Ser-His-Asp triad. GO:0017171 is defined by a serine nucleophile in a
  catalytic triad, so a protein lacking the nucleophile at the canonical position is not
  expected to carry this activity.
- Conclusion: the HDA row records a real high-throughput observation (probe enrichment), but
  it does not establish triad-dependent serine hydrolase catalysis by MESK2.

## PANTHER subfamily placement (PANTHER 19.0 HMM classification files, fruit fly and human)

Lines copied verbatim from the PANTHER 19.0 sequence-classification files
(`PTHR19.0_fruit_fly`, `PTHR19.0_human`; selected columns for the human rows):

```
DROME|FlyBase=FBgn0043070|UniProtKB=Q9GU50	Q9GU50	MESK2	PTHR11034:SF56	N-MYC DOWNSTREAM REGULATED	GH09802P
HUMAN|HGNC=7679|UniProtKB=Q92597	NDRG1	PTHR11034:SF18
HUMAN|HGNC=14460|UniProtKB=Q9UN36	NDRG2	PTHR11034:SF17
HUMAN|HGNC=14462|UniProtKB=Q9UGV2	NDRG3	PTHR11034:SF20
HUMAN|HGNC=14466|UniProtKB=Q9ULP0	NDRG4	PTHR11034:SF21
```

MESK2 (classified via Q9GU50, which is sequence-identical to Q7KVN0) is in subfamily SF56,
separate from each of the four human NDRG subfamilies. NDRG paralog-specific functions are
therefore not transferred; only assertions PAINT placed at a node ancestral to both
(PTN000867215, Eumetazoa) apply.
