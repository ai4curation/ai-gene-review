# Notes for VIBCH cds1 (Q9KT44)

## Gene Summary

- **UniProt**: Q9KT44
- **Gene**: cds1 (VC_1061)
- **Protein**: L-cysteine desulfhydrase Cds1
- **EC**: 4.4.1.1
- **Organism**: Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961)

## PANTHER Family

This gene belongs to PANTHER subfamily **PTHR10314:SF135** within family **PTHR10314**.

See family-level analysis: [interpro/panther/PTHR10314/PTHR10314-notes.md](../../../interpro/panther/PTHR10314/PTHR10314-notes.md)

### Key Finding: IBA Annotation Error

The IBA annotation **GO:0019344 (L-cysteine biosynthetic process)** is INCORRECT for this gene.

- **Reason**: SF135 (Cds1 subfamily) performs cysteine CATABOLISM (EC 4.4.1.1), not biosynthesis
- **Tree position**: in the PANTHER 19.0 tree the IBA's node (PTN000034104) is the family root, a
  duplication with five branches. All 19 seeds of the row sit in three of the other four branches and
  none in the Cds1 branch (PTN008304321), so every seed is a paralog of cds1 (`cds1-phylo.yaml`,
  from `just phylo VIBCH cds1`).
  *Correction 2026-11-10: this line used to read "Branch length: 0.528 from root - longest branch,
  indicating significant functional divergence". The five root branches are 0.412, 0.528, 0.659, 0.458
  and 0.402, so the Cds1 branch is the second longest (the threonine synthase branch is the longest),
  and branch length was not the evidence in any case.*
- **Correct annotations**: GO:0019450 (cysteine catabolic process), GO:0080146 (L-cysteine desulfhydrase activity)

## Gene-Specific Notes

### Experimental Evidence (PMID:34283874 - Ma et al. 2021)

1. VC1061 (cds1) is the **principal determinant** of cysteine-derived H2S in V. cholerae
2. Genetic deletion (Δvc1061) drastically reduces H2S production from cysteine
3. CBS-derived H2S protects V. cholerae from oxidative stress (H2O2)
4. Δcbs shows ~10-fold lower viability under intense H2O2
5. H2S enhances catalase (KatB) activity at post-translational level
6. In adult mouse models, cbs mutant is outcompeted by WT under high-ROS conditions

### Physiological Role

- Primary function: Produce H2S from cysteine degradation
- Secondary function: Protect against oxidative stress via H2S-mediated catalase enhancement
- Virulence factor: Required for host colonization under high-ROS conditions

---
*Last updated: 2026-01-06*
