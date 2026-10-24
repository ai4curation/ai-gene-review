# vps-34 (LET-512, B0025.1; UniProt Q9TXI7) review notes

## Deep research status
`just deep-research-falcon worm vps-34 --fallback perplexity-lite` failed on 2026-10-08. Falcon was killed at its 600 s timeout, and the perplexity provider was unavailable in this environment. No deep-research file was created. The review is based on the UniProt record, cached publications and PubMed searches.

## Key findings
- Immunoprecipitated worm VPS-34 has PtdIns 3-kinase activity [PMID:11927551 "The anti- Ce VPS34 immunoprecipitate displayed a lipid kinase activity towards PtdIns, yielding PtdIns 3-P as a product."]
- The protein is concentrated at the nuclear envelope; null mutants arrest at the L3/L4 molts with an expanded perinuclear space [PMID:11927551 "our data suggest that LET-512/VPS34 is located to and acts directly at the outer nuclear membrane"]
- BEC-1 is needed for VPS-34 function in autophagy, trafficking and endocytosis [PMID:16111945 "BEC-1 is necessary for the function of the class III PI3 kinase LET-512/Vps34, an essential protein required for autophagy, membrane trafficking, and endocytosis"]
- In phagosome maturation, VPS-34 acts with the class II PI3K PIKI-1 [PMID:22272187 "PIKI-1 and VPS-34 act in sequence to provide overlapping pools of PtdIns(3)P on phagosomes."], downstream of DYN-1 [PMID:18425118].
- SORF-1/2 restrain the activity of the BEC-1/VPS-34 complex on endosomes [PMID:26783301 "the activities of BEC-1-VPS-34 complexes from sorf-1 and sorf-2 mutants are nearly two times that from N2 animals"]
- The worm complex I subunit EPG-8 (divergent Atg14) binds BEC-1 [PMID:21116129].

## Curation decisions
- Core functions: GO:0016303 in complex I (autophagosome assembly) and complex II (endocytosis, phagosome maturation).
- Generic protein binding (BEC-1 IPI) removed.
- Pleiotropic developmental and trafficking phenotypes (molting, LRP-1 secretion, nuclear envelope, endosome size, life span) kept as non-core.
- IBA peroxisome and PI-mediated signaling marked as over-annotated.
- Engulfment terms kept as non-core: the evidence points to phagosome maturation rather than engulfment [PMID:18425118 "accumulation of internalized, but undegraded, corpses"].
