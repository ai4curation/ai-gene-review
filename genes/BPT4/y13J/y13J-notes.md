# Curation Notes: Bacteriophage T4 `y13J` (UniProt P39503)

## Identity and Nomenclature
- **Gene symbol:** `y13J` (synonym: `pseT.2`)
- **UniProt accession:** `P39503` (`SPAN2_BPT4`)
- **Protein name:** Spanin, outer lipoprotein subunit (o-spanin)
- **Length:** 99 AA precursor (signal peptide 1-16; mature lipoprotein chain 17-99, lipidated at Cys17)
- **Organism:** Enterobacteria phage T4 (`NCBITaxon:10665`)

## Summary of Experimental Evidence
- **Identification and Genetic Validation in T4 (Summer et al. 2007):** [PMID:17900620, "In the case of T4, a deletion of a non-overlapping gene pair pseT.2 and pseT.3 identified as Rz/Rz1 equivalents resulted in the same divalent cation-dependent lysis phenotype."] `y13J` (`pseT.2`) encodes the outer-membrane lipoprotein subunit (o-spanin) of the T4 two-component spanin complex, paired in a separated head-to-tail gene architecture with `y13K` (`pseT.3`), which encodes the inner-membrane subunit (i-spanin). Deletion of `pseT.2`/`pseT.3` in T4 causes a divalent cation ($Mg^{2+}$)-dependent lysis defect in which infected *E. coli* cells become spherical after holin and endolysin action because the outer membrane fails to disrupt.
- **Subcellular Localization and Mechanism:** Synthesized as a 99-AA precursor with an N-terminal signal peptidase II lipobox (`SIGNAL 1..16`), `y13J` (`pseT.2`) is lipidated on Cys17 (`N-palmitoyl cysteine`, `S-diacylglycerol cysteine`) and sorted to the periplasmic leaflet of the host cell outer membrane (`SUBCELLULAR LOCATION: Host cell outer membrane {ECO:0000250}; Lipid-anchor {ECO:0000250}; Periplasmic side {ECO:0000250}.`). Its C-terminal periplasmic domain interacts with the C-terminus of the i-spanin `y13K` (`pseT.3`) to form a periplasm-spanning complex (`These proteins were named "spanins," since their protein products are predicted to span the periplasm providing a physical connection between the inner and outer membranes.` [PMID:17900620]). After endolysin degrades the peptidoglycan meshwork, the spanin complex drives fusion of the inner and outer membranes to disrupt the outer membrane barrier and complete host cell lysis.

## Review of Existing GO Annotations
1. `GO:0044659` (`viral release from host cell by cytolysis`, IGI `PMID:17900620`): **ACCEPT**. Directly supported by the $\Delta(\text{pseT.2 pseT.3})$ lysis defect in T4 [PMID:17900620].
2. `GO:0031640` (`killing of cells of another organism`, IEA `GO_REF:0000043`): **MODIFY** to `GO:0044659` (`viral release from host cell by cytolysis`), which is the specific descendant process already experimentally annotated on the gene.
3. `GO:0020002` (`host cell plasma membrane`, IEA `GO_REF:0000044`): **MODIFY** to `GO:0033644` (`host cell membrane`). In Gram-negative bacteria (*E. coli*), the plasma membrane is the inner membrane (where the partner i-spanin `y13K` resides), whereas `y13J` (`pseT.2`) is an outer-membrane lipoprotein anchored in the `Host cell outer membrane` (`UniProtKB-SubCell:SL-0376`). Because `GO_REF:0000044` conservatively mapped `SL-0376` to `GO:0020002`, replacing `GO:0020002` with `GO:0033644` (`host cell membrane`) avoids misplacing the outer-membrane lipoprotein subunit in the inner (plasma) membrane.
