# IDP1 (YDL066W, P21954) notes

Evidence journal (no paid deep research run; built from UniProt and cached publications).

- Isocitrate dehydrogenase [NADP], mitochondrial, EC 1.1.1.42; homodimer; mitochondrial transit peptide 1-16 (experimentally determined, PubMed:1989987); Mg2+/Mn2+ cofactor (by similarity) [UniProt:P21954].
- Isozymes: "Three differentially compartmentalized isozymes of isocitrate dehydrogenase (mitochondrial IDP1, cytosolic IDP2, and peroxisomal IDP3) in the yeast Saccharomyces cerevisiae catalyze the NADP(+)-dependent oxidative decarboxylation of isocitrate to form alpha-ketoglutarate"; isozymes "functionally interchangeable for glutamate synthesis" [PMID:15001388].
- Not a TCA-cycle enzyme in practice: "IDP1 expression levels appear to be unresponsive to carbon source, and an IDP1 disruption mutant is not significantly impaired for growth or mitochondrial respiration. These results strongly suggest that IDP1 is incapable of participating in tricarboxylic acid cycle-based respiration despite its mitochondrial location"; "A double mutant lacking both IDP1 and IDH activities proved to be auxotrophic for glutamate during growth on glucose" [PMID:8099357].
- Kinetics: purified His-tagged IDP1 has ~7-fold lower Km for isocitrate than IDP2; "these results suggest an ancillary role for IDP1 in cellular glutamate synthesis" [PMID:15574419].
- Cofactor: "The two mitochondrial isozymes, IDH and IDP1, are NAD- and NADP-specific, respectively" [PMID:8099357].
- Mitochondrial proteomes [PMID:14576278, PMID:16823961, PMID:24769239]; mtDNA nucleoid-associated protein screen [PMID:15692048].

## Curation decisions
- Core MF GO:0004450; BP GO:0006102 isocitrate metabolic process (+ NADP+ metabolism); CC mitochondrion.
- TCA cycle IBA (PTN008982454, seeded only by M. tuberculosis Icd): REMOVE - target-specific genetic evidence that IDP1 does not contribute to TCA-cycle respiration.
- Peroxisome IBA: REMOVE - peroxisomal isozyme is the paralog IDP3; IDP1 has an experimentally defined mitochondrial presequence.
- Cytosol RCA (YeastCyc PWY3O-13): REMOVE - YeastCyc attached the cytosolic step to IDP1; the cytosolic isozyme is IDP2.
- NAD binding IEA: REMOVE - IDP1 is NADP-specific.
- L-glutamate biosynthetic process (IGI, RCA): KEEP_AS_NON_CORE - IDP1 supplies 2-oxoglutarate (ancillary), the glutamate-forming step is GDH1/GDH3/GLT1.
- Pathway observation: YeastCyc superpathway of glutamate biosynthesis assigns EC 1.1.1.42 to IDP1 (mitochondrial); the main 2-OG suppliers for glutamate are IDH (glucose) and IDP2 (non-fermentable).
