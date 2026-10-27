# Curation Notes: Mycobacterium phage L5 gene 78 (gp78, Q05293)

## Summary of Evidence
- **UniProt (`Q05293` / `VG78_BPML5`)**: Encodes Gene 78 protein (Gp78), a small 45-amino-acid (5,494 Da), highly basic, intrinsically disordered polypeptide (residues 1–45) classified in Pfam family `PF26884` (`Phage_L5_Gp78`, InterPro `IPR059593`).
- **Experimental characterization as a cytotoxic early host-shut-off protein (`PMID:18667563`)**: Burger et al. (2008) showed that inducible expression of L5 `gp78` from a mycobacterial shuttle vector is toxic to *Mycobacterium smegmatis* and inhibits host growth. `gp78` is co-transcribed with `gp77` and `gp79` from an early promoter located inside `ORF83` whose activity is repressed by the phage immunity repressor `gp71`.
- **Curation Decisions**:
  - `78-goa.tsv` is empty.
  - Propose a `NEW` annotation for `GO:0044003` (`modification by symbiont of host morphology or physiology`, `IMP`, `PMID:18667563`) reflecting the experimentally demonstrated host growth inhibition (shut-off) phenotype.
  - Because the direct molecular target and biochemical mechanism of gp78 have not yet been identified, `core_functions` is left empty.
