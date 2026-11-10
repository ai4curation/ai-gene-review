# Curation Notes: Variovorax paradoxus `iadK3` (`A0A0H2LZ84`, `VPARA_32100`)

## Summary
- **Gene symbol**: `iadK3` (locus tag `VPARA_32100`, 381 aa; orthologous to *V. paradoxus* CL14 IMG `2643613661`).
- **Operon context**: Second subcluster B-III periplasmic solute-binding protein (SBP) encoded immediately adjacent to `iadK2` (`VPARA_32110`) in the *Variovorax* `iad` auxin-catabolism operon (`PMID:37459330`).
- **Experimental findings (`PMID:37459330`)**:
  - Shares ~70% sequence identity with `IadK2`, but diverges at key binding-pocket residues (`Trp172`, `Ser104`, `Thr125`, `Asn126` in `IadK2`) and exhibits no detectable binding to IAA or tested auxin analogs (4-Cl-IAA, IBA, IPA, NAA, 2,4-D, PAA) [PMID:37459330, "Structural comparison revealed several residues located in the binding pocket in IadK2 are not conserved in IadK3, such as Trp172, Ser104, Thr125, and Asn126 in IadK2 (S3A, S3B and S3E Fig)."].
  - Weakly associates with 2-oxindole-3-acetic acid (`oxIAA`), the oxidized product of `IadD/IadE-IadC` [PMID:37459330, "IadK3 however show no binding with these auxin analogs. Interestingly, we found IadK3 could weakly associate with oxIAA. The detailed roles of IadK3 and IadK2 in the Variovorax auxin degradation pathway, however, remain to be further characterized and defined."].
- **Annotation review**:
  - `REMOVE` `GO:0006865` (`amino acid transport`, `IEA` from `InterPro:IPR000709`), which is a broad superfamily signature over-projection onto a subcluster B-III aromatic carboxylic acid SBP.
  - `NEW` `GO:0031406` (`carboxylic acid binding`, `IDA`, `PMID:37459330`) and `GO:0042597` (`periplasmic space`, `IC`, `PMID:37459330`).
