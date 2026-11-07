# PRO1 (YDR300C, P32264) notes

- Glutamate 5-kinase (gamma-glutamyl kinase, EC 2.7.2.11), first step of proline biosynthesis from glutamate; AA-kinase domain + C-terminal PUA domain [UniProt:P32264 "Catalyzes the transfer of a phosphate group to glutamate to"].
- Gene-enzyme identification by complementation of E. coli proline auxotrophs [PMID:2824433 "Interspecies complementation demonstrated that the S. cerevisiae PRO1 gene encoded gamma-glutamyl kinase"].
- Enzyme activity assayed in yeast extracts; D154N allele raises gamma-GK activity, relieves proline feedback, and increases proline/freeze tolerance [PMID:12513997 "the allele of PRO1 was shown to enhance the activities of gamma-glutamyl kinase"]. Yeast GK is nearly insensitive to physiological proline [PMID:12513997 "was virtually insensitive to the physiological concentration of l -proline"]. GK and GPR (PRO2) may form a complex [PMID:12513997 "which together may form a complex in vivo"].
- Cytosolic by native-promoter GFP [PMID:25112878 "Pro1p, Pro2p, and Pro3p were expressed exclusively in the cytosol"].
- Moonlighting claim: GK activity required for ribophagy, genetic interaction with UBP3 [PMID:27442630 "indicating that GK activity is indispensable for ribophagy"]; abstract-only, mechanism unknown (may be via proline/metabolite). Kept as non-core.
- IPI with HSP82 from Hsp90 interactome screen [PMID:15766533]; uninformative protein binding.
- RNA binding IEA is InterPro2GO from the PUA domain only; no evidence of RNA binding for any ProB.

## 2026-11-02 completion pass (module bacterial_glutamate_to_p5c_biosynthesis)

- Literature search: cached publications for every GOA reference were read
  (full text where `full_text_available: true`), together with the SGD
  description (`PRO1-deep-research-sgd.md`). No other deep-research provider
  file exists and no provider API keys were available in this session.
- Cytoplasm rows reworded: the high-throughput assays resolve "cytoplasm", which
  is correct; cytosol is carried separately by the targeted GFP IDA.
- Cofactor/co-substrate binding rows (ATP binding for PRO1, NADP binding for PRO2)
  are KEEP_AS_NON_CORE, matching the E. coli and P. putida proB/proA reviews.
- PUA-derived RNA binding IEA changed to REMOVE, matching the E. coli and P. putida proB reviews [PMID:16337196 "We propose that the PUA domain modulates the function of the AAK domain"].


## 2026-11-07 bounded RNA-binding comparator correction

The earlier universal claim that no glutamate kinase binds RNA is contradicted by PMID:37511294: K-12 ProB, expressed with a C-terminal His tag, shows specific but weak RNA binding by SELEX and competition EMSA. The estimated KD is >>10 micromolar, the binding site is not mapped, and no native RNA-regulatory role is established. This experiment neither establishes nor excludes RNA binding by this yeast protein. The original InterPro RNA-binding row is therefore UNDECIDED, preserving every machine payload and all unrelated judgments. The kinase-regulatory role of an E. coli PUA domain is not evidence of absence of RNA binding. This was a bounded source-premise correction, not a complete new review of yeast biology.
