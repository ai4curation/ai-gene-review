# CG13096 ribosomal-L1-domain family placement (2026-10-20 re-review)

Script: `l1_family_placement.py` (run with `uv run --with biopython --with requests python l1_family_placement.py`; needs `mafft` and `phmmer`).
Raw output: `l1_family_placement_out/report.txt`, alignment `l1_family_placement_out/panel.mafft.fasta`, tree `l1_family_placement_out/panel_nj.nwk`.

## Identity of the benchmark accession

H0RNN8 length 681; Q9VLK2 length 681; identical sequence: True

H0RNN8 (TrEMBL, cDNA clone FI17503 / AEW48266.1) is a redundant entry for the full-length CG13096 product. It is not a fragment, isoform or alternative gene model; the reviewed Swiss-Prot entry Q9VLK2 carries the same 681-residue sequence.

## Panel and PANTHER context

PANTHER 19.0 places CG13096 in PTHR48162:SF1 ("RIBOSOMAL L1 DOMAIN-CONTAINING PROTEIN CG13096", family PTHR48162 "YALI0A06930P"), together with Dictyostelium DDB_G0279335, Candida albicans NRI1 and varicella-zoster virus ORF11. The characterized nucleolar L1-domain ribosome-biogenesis factors (human RSL1D1, yeast UTP30, yeast/Candida CIC1) are in a different PANTHER family, PTHR23105 (subfamilies SF31/SF203). No fly protein is assigned to PTHR23105:SF31 or SF203 in PANTHER 19.0, and in UniProt CG13096 is the only fly Pfam PF00687 protein that is not a cytoplasmic (RpL10Aa/RpL10Ab) or mitochondrial (mRpL1) ribosomal protein.

## Results

phmmer (query CG13096 Q9VLK2) full-sequence hits against the panel:

- O76021 human RSL1D1: E=3.8e-25
- Q8BVY0 mouse Rsl1d1: E=4.1e-25
- Q20720 worm F53F4.11: E=2.7e-21
- P62906 human RPL10A (uL1): E=3.3e-06
- No significant full-sequence hit to the PTHR48162 co-members (Candida NRI1, Dictyostelium DDB_G0279335, VZV ORF11), to yeast UTP30/CIC1, or to mitochondrial uL1m (MRPL1, fly mRpL1).

Pairwise identity over aligned columns is low throughout (12.6-24.4%); the highest are RSL1D1 (0.244) and worm F53F4.11 (0.239); the PTHR48162 co-members are among the lowest (NRI1 0.168, DDB_G0279335 0.143, VZV ORF11 0.126).

In the neighbour-joining tree (BLOSUM62 distances, rooted on mitochondrial uL1m), CG13096 pairs with worm F53F4.11, inside the cluster of eukaryotic cytoplasmic uL1 and RSL1D1/UTP30/CIC1 sequences, and separately from the NRI1 + DDB_G0279335 + VZV ORF11 cluster. Internal branches joining the major groups are very short (about 0.01), so the deep branching order is not resolved by this small distance tree and should not be over-read.

## Interpretation

- Sequence similarity, the phmmer hits, eggNOG (KOG1685) and OrthoDB (10251727at2759) group membership shared with RSL1D1, UTP30 and CIC1 (UniProt cross-references), and four Alliance orthology methods (OrthoFinder, OrthoInspector, PhylomeDB, SonicParanoid) all place CG13096 with the RSL1D1/UTP30/CIC1 lineage of nucleolar ribosomal-L1-domain proteins, with human RSL1D1 and worm F53F4.11 as the closest metazoan relatives.
- PANTHER disagrees and separates CG13096 into PTHR48162 with proteins that fall into different eggNOG/OrthoDB groups (Candida NRI1: ENOG502QQIF, OrthoDB 4084568at2759). The PANTHER placement therefore looks like a split of a highly divergent sequence rather than evidence of a distinct conserved function; neither placement is backed by a curated PAINT node with experimental annotations.
- CG13096 is clearly not mitochondrial uL1m (fly mRpL1 is CG7494, PTHR36427) and not a cytoplasmic uL1 ribosomal protein (fly RpL10Aa/RpL10Ab).
- The alignment and tree are too divergent to support transfer of any subfamily-specific function (RSL1D1 PTEN-translation regulation, UTP30 SSU-processome role or CIC1 60S-biogenesis/proteasome-adaptor roles). At most they support a general nucleolar RNA-binding ribosome-biogenesis-factor hypothesis.
