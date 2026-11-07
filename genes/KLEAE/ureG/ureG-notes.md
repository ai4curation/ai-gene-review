# ureG (P18319) notes -- Klebsiella aerogenes urease accessory GTPase UreG

Deep research: `just deep-research KLEAE ureC --provider perplexity` was attempted once (2026-10-23) and failed ("Provider 'perplexity' not available. Available: falcon, openscientist"). No deep-research file was generated for any KLEAE ure gene; this review relies on cached primary literature and the reviewed UniProt entry.

- Isolated UreG is monomeric and does not bind/hydrolyze GTP; P-loop K20A/T21A give inactive urease and no UreDFG-apoprotein complexes [PMID:9209019 "UreG did not bind or hydrolyze ATP or GTP"].
- GTP hydrolysis required for activation at physiological bicarbonate; nucleotide site localized to UreG [PMID:10500143 "nucleotide hydrolysis, not just binding, is required for this process"].
- Binds one Ni or Zn, Kd ~5 uM [PMID:22369361 "binds one Ni or one Zn with Kd values of about 5 μM"].
- Decisions: GTPase, nickel binding, cytoplasm, urea catabolism ACCEPT; GO:0005515 REMOVE; NEW GO:0018237 and GO:0150006. Core: GTPase activity, nickel cation binding, urease activator activity.
