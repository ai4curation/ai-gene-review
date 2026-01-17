# Notes for MYCTU cds1 (O69652)

## Gene Summary

- **UniProt**: O69652 (Reviewed Swiss-Prot)
- **Gene**: cds1 (Rv3684)
- **Protein**: L-cysteine desulfhydrase Cds1
- **EC**: 4.4.1.1
- **Organism**: Mycobacterium tuberculosis (strain ATCC 25618 / H37Rv)

## PANTHER Family

This gene belongs to PANTHER subfamily **PTHR10314:SF135** within family **PTHR10314**.

See family-level analysis: [interpro/panther/PTHR10314/PTHR10314-notes.md](../../../interpro/panther/PTHR10314/PTHR10314-notes.md)

### Key Finding: IBA Annotation Error

The IBA annotation **GO:0019344 (L-cysteine biosynthetic process)** is INCORRECT for this gene.

- **Reason**: SF135 (Cds1 subfamily) performs cysteine CATABOLISM (EC 4.4.1.1), not biosynthesis
- **Branch length**: 0.528 from root - longest branch, indicating significant functional divergence
- **Correct annotations**: GO:0019450 (cysteine catabolic process), GO:0080146 (L-cysteine desulfhydrase activity)

### Important: M. tuberculosis has multiple cysteine-related enzymes

| Gene | UniProt | Subfamily | Function |
|------|---------|-----------|----------|
| **cds1 (Rv3684)** | O69652 | SF135 | Cysteine DESULFHYDRASE (catabolism) |
| cysK1 (Rv2334) | P9WP55 | SF194 | Cysteine SYNTHASE (biosynthesis) |
| cysM (Rv1336) | P9WP53 | SF162 | Cysteine SYNTHASE (biosynthesis) |

## Gene-Specific Notes

### Experimental Evidence (PMID:34439535 - Kunota et al. 2021)

1. Identified Rv3684 (Cds1) as an **H2S-producing enzyme** in Mtb
2. Δcds1 disruption significantly reduces H2S production in all media tested
3. H2S production confirmed using lead acetate assay, BiCl3 assay, and amperometric microsensor
4. Products identified by LC-MS/MS: H2S + pyruvate (confirms desulfhydrase activity)

### Biochemical Characterization

- **Kinetics**: KM = 11.26 mM for cysteine, kcat = 78.71 sec-1
- **Cofactor**: PLP (pyridoxal 5'-phosphate) at Lys67
- **Inhibitors**: AOAA (PLP inhibitor) - YES; PAG (CGL inhibitor) - NO
- This confirms Cds1 is a true cysteine desulfhydrase, NOT a cystathionine gamma-lyase

### Physiological Role

1. **H2S stimulates respiration** via cytochrome bd
2. Modulates balance between respiration and glycolysis
3. Contributes to **redox homeostasis** (affects ergothioneine and mycothiol levels)
4. Δcds1 shows 40% reduction in basal oxygen consumption rate
5. Δcds1 cells grow poorly with 4 mM cysteine (enzyme eliminates toxic cysteine)
6. Δcds1 shows **increased survival** after clofazimine or rifampicin treatment
   - H2S may contribute to antibiotic sensitivity

### Drug Target Potential

The finding that Δcds1 shows increased antibiotic sensitivity suggests Cds1 could be a drug target for TB treatment in combination with existing antibiotics.

---
*Last updated: 2026-01-06*
