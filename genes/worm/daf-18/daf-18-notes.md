# daf-18 (G5EE01) review notes

Deep research: falcon run failed (timeout/connection reset; perplexity fallback unavailable). Review based on cached publications, UniProt and PubMed.

## Key findings
- PTEN homolog acting as PIP3 phosphatase in vivo [PMID:10377431 "elegans, the PTEN homolog DAF-18 functions as a negative regulator of the DAF-2 and AGE-1 signaling pathway, consistent with the notion that DAF-18 acts a phosphatidylinositol 3,4,5-trisphosphate phosphatase in vivo."]
- daf-18 suppresses Daf-c of daf-2/age-1 [PMID:10377431 "we have shown that mutation in daf-18 can completely suppress the dauer-constitutive phenotype caused by inactivation of daf-2 or age-1"]
- Protein phosphatase vs VAB-1 [PMID:19853560 "We also present evidence that DAF-18 has protein phosphatase activity to antagonize VAB-1 action."]
- Localisation: cytoplasm/nucleus then plasma membrane in VPCs [PMID:22916028 "pxx stages), DAF-18::GFP became increasingly localized to the plasma membrane of the vulval cells (Figure 2C, 2D and 2D′)."]
- Blocks AKT membrane recruitment [PMID:25383666 "The PI3K and AKT pathway is negatively regulated by the lipid phosphatase DAF-18 (homologous to human Phosphatase and Tensin Homolog, PTEN), which dephosphorylates and converts PIP3 to PIP2 and blocks recruitment of AKT kinases to the plasma membrane28–31."]

## Curation decisions
- NAS "positive regulation of insulin receptor signaling pathway" (PMID:20207731) has an inverted sign: the abstract states DAF-18 "normally serves as a suppressor of DAF-2 signaling". MODIFY -> GO:0046627 negative regulation.
- IBA regulation of PI3K/PKB signalling -> negative regulation (GO:0051898).
- "protein phosphatase inhibitor complex" NAS marked over-annotated (co-complex with ARR-1/MPZ-1, no inhibitor activity shown; DAF-18 would be the target).
- Protein binding (VAB-1) -> ephrin receptor binding.
- Neuronal localisations from PMID:16950159 (abstract-only) deferred to curator.
