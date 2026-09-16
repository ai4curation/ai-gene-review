# loqs ProtNLM2 function-description review

## Original prediction

> Required for formation of the RNA induced silencing complex (RISC). Component of the RISC loading complex (RLC), also known as the micro-RNA (miRNA) loading complex (miRLC), which is composed of DICER1, AGO2 and TARBP2. Within the RLC/miRLC, DICER1 and TARBP2 are required to process precursor miRNAs (pre-miRNAs) to mature miRNAs and then load them onto AGO2. AGO2 bound to the mature miRNA constitutes the minimal RISC and may subsequently dissociate from DICER1 and TARBP2. May also play a role in the production of short interfering RNAs (siRNAs) from double-stranded RNA (dsRNA) by DICER1

Original wording and all model/source metadata are retained in [loqs-protnlm-source.json](loqs-protnlm-source.json).

## Assessment

**Mixed: supported small-RNA cofactor function; incorrect literal mammalian complex and Dicer allocation.** X2J5X6 is loqs-PF, a PB-like fly isoform, not human TARBP2. All three PB domains are retained ([sequence analysis](loqs-bioinformatics/RESULTS.md)). Fly miRNA processing uses Dcr-1, Loqs and AGO1; the predicted DICER1/AGO2/TARBP2 complex reproduces mammalian nomenclature and composition rather than the fly machinery. The fly Dcr-2/Loqs-PD pathway produces siRNAs, so the final DICER1 statement cannot be transferred literally to this PF isoform. This is a pathway/paralog allocation error within an otherwise meaningful homolog-based account, not proof of absent gene-expression regulation.

Evidence: [PMID:15918769](https://pubmed.ncbi.nlm.nih.gov/15918769/) describes the Dcr-1/Loqs complex and AGO1-associated processing; [PMID:19635780](https://pubmed.ncbi.nlm.nih.gov/19635780/) separates PB/Dcr-1 miRNA from PD/Dcr-2 endo-siRNA biogenesis. Both publications are cached. The exact function paragraph and donor Q15633 metadata remain in the source JSON.

## Claim-level decisions

| Claim | Assessment | Evidence |
|---|---|---|
| Required for RISC formation | NPI | Loqs-null extracts support miRISC assembly; Loqs is largely dispensable for this step (PMID:17928574). |
| Dicer-associated pre-miRNA processing cofactor | CNN | Established Loqs activity; PF retains the PB processing architecture (PMID:15918769, PMID:17666393). |
| Literal DICER1/AGO2/TARBP2 miRLC composition in this fly protein | NPI | The fly miRNA complex uses Dcr-1/Loqs/AGO1, while AGO2 chiefly serves the Dcr-2 siRNA pathway (PMID:15918769, PMID:19635780). |
| Loading-mediated complex dissociation as described for the mammalian complex | UNC | No experiment establishes this exact transition for the PF isoform. |
| siRNA production by DICER1 with this PF protein | NPI for the stated Dicer allocation; UNC for any independent PF siRNA contribution | Fly endo-siRNA processing uses Dcr-2 with PD, not the PB-like Dcr-1 arrangement (PMID:19635780). |

[PMID:17928574](https://pubmed.ncbi.nlm.nih.gov/17928574/) states: “Loqs plays a prominent role in miRNA biogenesis, but is largely dispensable for miRISC assembly.” The cached abstract supports the requirement distinction without claiming that Loqs never associates with a processing/loading complex.
