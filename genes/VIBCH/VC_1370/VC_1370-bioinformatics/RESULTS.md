# VC_1370 (Q9KS89) bioinformatics: GGDEF catalytic and I-site motifs

Run: `projects/hackathon/runs/20261030T213647Z-vc1370-ggdef-motifs` (beril run). The script is
`analyze.py`, run as `analyze.py VC_1370-uniprot.txt NZ_AFOM01000014.1_606.fasta <outdir>`. The
numbers below are copied from `results.json`.

## Question

The dashboard called this protein a "c-di-GMP-binding protein containing HAMP and GGDEF
signaling domains" and did not call it a diguanylate cyclase. Is the GGDEF domain catalytically
competent, or is it degenerate? Is there an I-site?

## Results

- **Identity.** The dashboard sequence NZ_AFOM01000014.1_606 is identical to UniProt Q9KS89
  (N16961 VC_1370): 443/443 positions.
- **A-site.** The GGDEF domain carries an intact canonical A-site motif: GGDEF at residues 349-353,
  in the context RLGGDEF.
- **Other conserved catalytic residues.** These are also present:
  - the beta1 metal-binding DxD as DLD at 308-310 (the PleD D327-equivalent region);
  - the guanine/GTP-binding N-x3-GH-x2-GD stretch as NDTKGHEVGD at 316-325.
- **Primary I-site.** The RxxD I-site is present as RESD at 340-343. Its Asp (D343) is 6
  residues before the first Gly of GGDEF (G349), so 5 residues lie between them. This is the
  same spacing as PleD R359xxD362 / G368GEEF, so the I-site lies in the canonical position.
- **Hydrophobic segments.** Kyte-Doolittle 19-residue windows with mean >= 1.6 find two
  segments: 5-32 and 165-193. This matches the dashboard's DeepTMHMM call of 2 helices and the
  UniProt Phobius TM at 165-189.
- **Domain order.** The protein reads: TM1, a ~130-residue periplasmic region, TM2, HAMP
  (190-243), a coiled coil, then GGDEF (Pfam 272-426). That is the topology of an inner-membrane
  sensor DGC.

## Interpretation

- **Not degenerate.** The GGDEF domain has every sequence hallmark of an active diguanylate
  cyclase: GGDEF, DxD, the GTP-binding stretch, and an I-site in the canonical position.
- **What the I-site means.** In DGCs, I-site binding of c-di-GMP is allosteric product
  inhibition. That makes the observed c-di-GMP binding a regulatory property of a cyclase, not
  evidence that the protein is a non-catalytic receptor.
- **Caveat.** No in vitro assay of purified VC1370 has been published, so catalysis is inferred,
  not measured.
