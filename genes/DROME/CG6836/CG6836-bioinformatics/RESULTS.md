# CG6836 (Q9VVV2) family placement analysis

Date: 2026-10-21. Script: `fetch_and_tree.py` (run with `uv run --with biopython python fetch_and_tree.py`).
Raw output: `run_output.txt`; alignment `family.aln.fasta` (MAFFT L-INS-i); tree `tree.nwk`.

## Question

PTHR23423 (ORGANIC SOLUTE TRANSPORTER-RELATED) mixes OST-alpha/SLC51A transporters, TMEM184 proteins
and fungal Hfl1-like proteins. UniProt places Q9VVV2 only at the family level (no subfamily), and the
PANTHER 19.0 fruit-fly classification file lists the two other fly members (Tmep, SF17; CG5850, SF10)
but has no row for FBgn0036834/Q9VVV2. So no PANTHER subfamily or PAINT node is available for CG6836,
and its placement relative to SLC51A versus TMEM184 had to be checked directly.

## Method

Fifteen PTHR23423 members were fetched from UniProt (subfamily labels from the PANTHER 19.0
classification files): CG6836, fly Tmep and CG5850, human/mouse SLC51A, zebrafish slc51a,
human TMEM184A/B/C, worm osta-1/2/3 and F40E10.6, yeast YKR051W and Dictyostelium tmem184B.
They were aligned with MAFFT L-INS-i. A neighbour-joining tree was built from Biopython identity
distances and midpoint-rooted. No bootstrap was run.

## Results

- CG6836 is the 328-residue canonical Swiss-Prot product. Its length matches vertebrate OSTalpha
  (326-340 aa), and UniProt predicts seven transmembrane helices. It is not a fragment or an isoform.
- In the NJ tree CG6836 is sister to the vertebrate SLC51A clade (human, mouse, zebrafish). That group
  then joins the worm osta-1/2/3 clade. The TMEM184A/B, Tmep/F40E10.6, TMEM184C, yeast and
  Dictyostelium proteins all fall outside this OSTalpha-like clade.
- Ungapped pairwise identity of CG6836 to the other members is low throughout (15-21%). It is highest to
  human SLC51A (21.1%), mouse Slc51a (19.7%) and worm osta-2 (19.7%), and lowest to the fly paralogs
  Tmep (16.2%) and CG5850 (15.1%).

## Interpretation and limits

The tree places CG6836 in the OSTalpha (SLC51A) lineage, not with TMEM184 or Hfl1. This agrees with the
Ensembl Compara ortholog list cited by Dawson et al. 2010 (PMID:20538072), which names FBgn0036834 as a
putative OSTalpha ortholog. Because identity is low and the NJ tree has no bootstrap support, the
placement is moderate rather than decisive. It does not establish substrate, partner requirement or
transport activity. Vertebrate OSTalpha needs OSTbeta (SLC51B) to reach the plasma membrane and to
transport, and no fly OSTbeta has been identified.
