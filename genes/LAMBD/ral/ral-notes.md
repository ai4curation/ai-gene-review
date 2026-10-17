# ral (P03703) - Curation Notes

## Overview
- **Gene symbol**: `ral`
- **UniProt ID**: `P03703` (`RAL_LAMBD`)
- **Protein name**: Restriction inhibitor protein ral (Restriction alleviation protein, 66 AA)
- **Organism**: Escherichia phage lambda (`NCBITaxon:2681611`)

## Function & Biological Context
- **Modulator of host Type I restriction-modification (EcoKI / HsdRMS)**: The lambda `ral` gene (66 AA) is expressed early from the `PL` operon (located between `N` and `cIII`) and counteracts the *Escherichia coli* K-12 Type I restriction-modification system (`EcoKI`, encoded by `hsdR`, `hsdM`, and `hsdS`) by two complementary activities: alleviating restriction cleavage of unmodified phage DNA and strongly enhancing *de novo* methylation (modification) of unmethylated target sites (`m*` enhancement / bi-functional modulation) [PMID:3023633, "The product of the lambda ral gene alleviates restriction and enhances modification by the Escherichia coli K-12 restriction and modification system."].
- **Direct interaction with HsdM/HsdS subunits of EcoKI**: Genetic and biochemical evidence indicates that Ral interacts with the methyltransferase/specificity core (`HsdM` or `HsdS` polypeptides) of the EcoKI holoenzyme, inducing a conformational switch from the restriction mode (which normally cleaves unmethylated DNA and only methylates hemimethylated DNA efficiently) into a modification mode that rapidly methylates completely unmethylated target sites on progeny phage DNA [PMID:3023633, "Our data support a model in which, as a consequence of the interaction of Ral with either the hsdM or the hsdS polypeptide, the conformation of the enzyme is changed and the efficiency of methylation of unmodified target sites is enhanced."].

## Review of Existing GO Annotations
- `GO:0052031` (symbiont-mediated perturbation of host defense response, IEA, `GO_REF:0000043`): **MODIFY** to `GO:0099018` (symbiont-mediated evasion of host restriction-modification system), which is a direct specific descendant already annotated on `ral`.
- `GO:0052170` (symbiont-mediated suppression of host innate immune response, IEA, `GO_REF:0000043`): **MODIFY** to `GO:0099018` (symbiont-mediated evasion of host restriction-modification system), which is the specific descendant describing anti-restriction activity in bacteria.
- `GO:0099018` (symbiont-mediated evasion of host restriction-modification system, IEA, `GO_REF:0000043`): **ACCEPT**. Directly captures Ral's core biological role in alleviating restriction and stimulating methylation by the host Type I restriction-modification system.
