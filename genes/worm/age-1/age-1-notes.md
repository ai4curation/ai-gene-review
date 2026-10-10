# age-1 (Q94125) review notes

Deep research: `just deep-research-falcon worm age-1 --fallback perplexity-lite` failed (falcon timed out / connection reset; perplexity provider unavailable in this environment). No deep-research file was produced; the review is based on cached publications, the UniProt record and PubMed lookups.

## Key findings
- AGE-1 is the class I PI3K p110 catalytic subunit [PMID:8700226 "age-1 encodes a homologue of mammalian phosphatidylinositol-3-OH kinase (PI(3)K) catalytic subunits."]
- PIP3 depends on AGE-1 [PMID:23543623 "PIP3 is significantly reduced in first-generation age-1(mg44) homozygotes, and is below detectable limits in their second-generation progeny"]
- AGE-1 is cytoplasmic [PMID:23543623 "registered full-length enzyme as a diffuse cytoplasmic signal in virtually all cell types of wild-type C."]
- PIP3 is made at the plasma membrane by AGE-1/AAP-1 [PMID:25383666 "In the IIS pathway, the insulin receptor-like protein DAF-2 activates the PI3K complex AGE-1/AAP-118–20, leading to the generation of PIP3 on the inner leaflet of the plasma membrane."]
- Dauer, lifespan, fertility outputs via DAF-16 [PMID:9504918 "These data show that insulin signaling, mediated by DAF-2 through the AGE-1 phosphatidylinositol-3-OH kinase, regulates reproduction and embryonic development, as well as dauer diapause and life span, and that DAF-16 transduces these signals."]

## Curation decisions
- GOA has only PI->PI3P (GO:0016303) and PI4P 3-kinase (GO:0035005) MF terms; the physiological class I activity GO:0046934 (PIP2 3-kinase, the term used in the DAF-2 module) is proposed as NEW (AGE-1 itself catalyses the step).
- PI3P biosynthetic process IBA marked over-annotated (class III / VPS34 function).
- Protein binding (AAP-1) -> PI3K regulatory subunit binding.
- Salt chemotaxis / learning / NMJ / stress rows kept as non-core cell-context outputs.
- Non-motile cilium IDA (PMID:16968739) is abstract-only; deferred to curator, non-core.
