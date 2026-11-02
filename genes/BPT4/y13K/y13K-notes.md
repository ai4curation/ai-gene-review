# Curation Notes: Bacteriophage T4 `y13K` (UniProt P39504)

## Identity and Nomenclature
- **Gene symbol:** `y13K` (synonym: `pseT.3`)
- **UniProt accession:** `P39504` (`SPAN1_BPT4`)
- **Protein name:** Spanin, inner membrane subunit (i-spanin)
- **Length:** 117 AA (13,135 Da)
- **Organism:** Enterobacteria phage T4 (`NCBITaxon:10665`)

## Summary of Experimental Evidence
- **Identification and Genetic Validation in T4 (Summer et al. 2007):** [PMID:17900620, "In the case of T4, a deletion of a non-overlapping gene pair pseT.2 and pseT.3 identified as Rz/Rz1 equivalents resulted in the same divalent cation-dependent lysis phenotype."] `y13K` (`pseT.3`) encodes the 117-amino-acid inner-membrane spanin subunit (i-spanin) of the T4 two-component spanin complex, paired with the adjacent outer-membrane lipoprotein gene `y13J` (`pseT.2`, o-spanin). Deletion of `pseT.3` and `pseT.2` in T4 produces the classical divalent cation ($Mg^{2+}$)-dependent lysis defect in which infected *E. coli* cells form spherical bodies bounded by an intact outer membrane after holin-endolysin action.
- **Topology, Subcellular Localization, and Mechanism:** `y13K` (`pseT.3`) is a single-pass type II inner membrane protein (`SUBCELLULAR LOCATION: Host cell inner membrane {ECO:0000250}; Single-pass type II membrane protein {ECO:0000250}; Periplasmic side {ECO:0000250}.`) with an N-terminal transmembrane signal-anchor helix (residues 3-23) and a periplasmic coiled-coil domain (residues 24-93; total periplasmic region 24-117). Its C-terminus binds the C-terminus of the outer-membrane o-spanin `y13J` (`pseT.2`) across the periplasm (`These proteins were named "spanins," since their protein products are predicted to span the periplasm providing a physical connection between the inner and outer membranes.` [PMID:17900620]). Following peptidoglycan degradation by T4 endolysin, the spanin complex undergoes conformational collapse to fuse the inner and outer membranes and complete host cell lysis.

## Review of Existing GO Annotations
1. `GO:0020002` (`host cell plasma membrane`, IEA `GO_REF:0000044`): **ACCEPT**. In Gram-negative bacteria (*E. coli*), the inner membrane (`UniProtKB-SubCell:SL-0373`, `Host cell inner membrane`) is the host cell plasma membrane, where Y13K is anchored via its N-terminal transmembrane helix.
2. `GO:0044659` (`viral release from host cell by cytolysis`, IGI `PMID:17900620`): **ACCEPT**. Directly supported by the $\Delta(\text{pseT.3 pseT.2})$ lysis defect in T4 [PMID:17900620].
3. `GO:0031640` (`killing of cells of another organism`, IEA `GO_REF:0000043`): **MODIFY** to `GO:0044659` (`viral release from host cell by cytolysis`), which is the specific descendant process already experimentally annotated on the gene.
