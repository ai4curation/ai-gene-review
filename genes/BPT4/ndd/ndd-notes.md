# Curation Notes: Bacteriophage T4 `ndd` (UniProt P15556)

## Identity and Nomenclature
- **Gene symbol:** `ndd` (synonyms: `D2b`, `ndd.6`)
- **UniProt accession:** `P15556` (`NDD_BPT4`)
- **Protein name:** Nucleoid disruption protein
- **Length:** 151 AA (16,967 Da)
- **Organism:** Enterobacteria phage T4 (`NCBITaxon:10665`)

## Summary of Experimental Evidence
- **Host Nucleoid Disruption and Relocalization:** `ndd` encodes an early T4 infection effector (`Pfam:PF06591`, `Phage_T4_Ndd`) that causes rapid disorganization of the *Escherichia coli* host nucleoid within 2-3 minutes post-infection, redistributing host chromosomal DNA from the cell center to the inner membrane periphery without cleaving or degrading the DNA (`Disorganizes the host nucleoid and inhibits replication, but without host DNA cleavage or degradation. Only the architecture of the nucleoid is affected.`; Bouet et al. 1998, PubMed 9748458; Snustad et al. 1976, PubMed 796620).
- **Double-Stranded DNA Binding and Inhibition of Host Replication:** Biochemical characterization by Bouet et al. 1998 (PubMed 9748458) demonstrated that purified Ndd binds double-stranded DNA (`Binds to dsDNA but not to ssDNA. {ECO:0000269|PubMed:9748458}.`) and that ectopic expression of Ndd in *E. coli* is sufficient to disrupt nucleoid architecture and inhibit host DNA replication (`inhibits replication, but without host DNA cleavage or degradation`).

## Review of Existing GO Annotations
1. `GO:0003677` (`DNA binding`, IEA `GO_REF:0000043`): **MODIFY** to `GO:0003690` (`double-stranded DNA binding`). Bouet et al. 1998 (PubMed 9748458) experimentally demonstrated that Ndd binds specifically to double-stranded DNA and not to single-stranded DNA.
2. `GO:0098673` (`symbiont-mediated suppression of host DNA replication`, IEA `GO_REF:0000043`): **ACCEPT**. Ndd-mediated nucleoid disruption directly halts host chromosomal replication independently of host DNA degradation by DenA/DenB.
3. `GO:0044071` (`symbiont-mediated perturbation of host cell cycle progression`, IEA `GO_REF:0000043`): **KEEP_AS_NON_CORE**. Arrest of host cell cycle progression/division upon ectopic expression or early infection is a downstream consequence of Ndd-mediated nucleoid disruption and inhibition of host chromosomal replication (`GO:0098673`).
