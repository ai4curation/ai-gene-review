# C6F010 bioinformatics results

Script: `rboh_identity.py` (run with `uv run --project <repo root> python rboh_identity.py`);
raw output in `results.tsv`.

## Method

Global pairwise alignment (Biopython PairwiseAligner, BLOSUM62, gap open -10,
extend -0.5) of C6F010 (932 aa) against all reviewed Arabidopsis RBOH entries
retrieved live from the UniProt REST API. Percent identity is reported over
aligned columns and over the query length.

## Results

- The closest Arabidopsis homologue of C6F010 is RBOHD (Q9FIJ0), at 67.4%
  identity over aligned columns (65.1% over the query length), followed by
  RBOHC (65.2%) and RBOHA/RBOHB (63.8%).
- The four PIRSR-predicted heme-iron axial ligand positions of C6F010 (461, 475,
  564, 577) are all histidine, so both bis-histidine heme sites of the
  gp91phox-type ferric-reductase domain are intact.

## Interpretation

C6F010 is an RBOHD-clade plant NADPH oxidase with intact catalytic heme
ligands. The Nat Genet 2024 study (PMID:38238629) calls its ZmRBOH4 "the most
closely related to AtRBOHD with 63.3% sequence identity"; our result is
consistent with C6F010 being ZmRBOH4 (NCBI GeneID 100136880 also carries the
designation "respiratory burst oxidase4"), but the paper's cached text gives no
gene identifier, so this identity remains probable rather than confirmed. The
identity values depend on alignment method and are not directly comparable to
the paper's 63.3%.
