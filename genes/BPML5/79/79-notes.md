# Curation Notes: Mycobacterium phage L5 gene 79 (gp79, Q05294)

## Summary of Evidence
- **UniProt (`Q05294` / `VG79_BPML5`)**: Encodes Gene 79 protein (Gp79), a 72-amino-acid (7,876 Da) early phage protein classified in Pfam family `PF17463` (`GP79`, InterPro `IPR035353`).
- **Experimental characterization as a cytotoxic early protein affecting host cell division (`PMID:18667563`)**: Burger et al. (2008) demonstrated that inducible expression of L5 `gp79` in *Mycobacterium smegmatis* is toxic and inhibits host growth, and reported evidence that host cell division is affected by `gp79` (filamentation/septation defect). Transcription of `gp79` (along with `gp78` and `gp77`) is driven by an early promoter located inside `ORF83` and repressed by the phage immunity repressor `gp71`.
- **Curation Decisions**:
  - `79-goa.tsv` is empty.
  - Propose a `NEW` annotation for `GO:0044003` (`modification by symbiont of host morphology or physiology`, `IMP`, `PMID:18667563`) capturing the experimentally demonstrated host growth and cell-division perturbation.
  - Because the direct molecular binding partner of gp79 in the mycobacterial division apparatus (e.g. FtsZ or divisome components) has not yet been biochemically identified in the cached L5 literature, `core_functions` is left empty.
