# URE (Q9SR52, At1g67550) notes

- Single-chain plant urease (fused gamma-beta-alpha), dinickel enzyme; UniProt: "Urea hydrolase involved in nitrogen recycling from ureide, purine, and arginine catabolism." [file:ARATH/URE/URE-uniprot.txt]
- ure mutants defective in urease activity, cannot grow on urea [PMID:16244137 "In contrast to wild-type plants, the mutant lines were not able to support growth with urea as the sole nitrogen source."]
- Activation in E. coli needs URED+UREF+UREG [PMID:16244137 "In these bacteria, urease activity was observed only when all three plant accessory genes were coexpressed together with the plant urease gene."]
- Cytosolic urea hydrolysis in vivo [PMID:23940254 "The postulated bypass of the UAH reaction via URE was confirmed by the significantly increased urea content in the uah ure double mutant"]
- Urease-UreD-UreF-UreG complex; UreD is the only UAP binding urease directly [PMID:28710280 "a direct interaction with urease was only observed for UreD but not for UreF or UreG"]
- In vivo activation takes days after nickel supply [PMID:28710280 "in vivo the process of urease activation is rather a matter of days than of hours."]

## Decisions
- cytoplasm ISM -> MODIFY to cytosol; generic hydrolase rows TOO_GENERAL; urease activator complex (URE as client) KEEP_AS_NON_CORE.
- Core: urease activity (GO:0009039) in cytosol / urease complex; nickel cation binding (GO:0016151).

## Deep research
- `just deep-research ARATH UREG --provider perplexity` was attempted once (2026-10-23) and failed: "Provider 'perplexity' not available. Available: falcon, openscientist". No deep-research file was generated; review based on cached literature and UniProt.

## Literature status
- PMID:16244137 (Witte 2005, Plant Physiol) – abstract only; full text not retrievable via `just fetch-pmid --force` or Europe PMC. Experimental GOA rows citing it (IDA/IMP/IPI) were accepted on abstract + independent confirmation in PMID:28710280, deferring to the curator.
- PMID:28710280 (Myrach 2017, JBC) – full text cached; key source.
- PMID:23940254 refetched with full text in this session.
- Newly fetched (abstract only): PMID:22271305 (soybean UreG), PMID:11289508 (potato UreG), PMID:10652150 (soybean Eu3/UreG), PMID:20631318 (rice urease/UAPs; not cited).

