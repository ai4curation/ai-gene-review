# UREG (O64700, At2g34470) notes

- SIMIBI G3E GTPase, UreG subfamily [file:ARATH/UREG/UREG-uniprot.txt "Belongs to the SIMIBI class G3E GTPase family. UreG subfamily."]
- Nickel delivery: [PMID:28710280 "Urease activation occurred in all cases where UreG was exposed to nickel in vivo , even when purified proteins were combined"]; HXH motifs of plant-specific N-terminus required [PMID:28710280 "We conclude that the plant-specific N terminus of UreG not only boosts urease activation, as does UreE, but is absolutely required"]
- GTPase: not measured for Arabidopsis UREG; GTP inhibited activation in vitro [PMID:28710280 "the addition of GTP to the assay mix did not accelerate the activation of urease but, rather, inhibited it"]; soybean UreG hydrolyses GTP [PMID:28710280 "That plant UreG hydrolyzes GTP in principle was shown for the soybean enzyme ( 19 )" = PMID:22271305]; bacterial UreG GTP hydrolysis required [PMID:10500143, PMID:24115911].
- Soybean UreG (Eu3) binds Ni2+ [PMID:10652150]; recombinant soybean UreG binds Zn2+ tighter than Ni2+ [PMID:22271305].

## Decisions
- GTPase activity IEA ACCEPT (family + soybean ortholog); flagged as not directly measured in Arabidopsis.
- NEW: GO:0170061 nickel chaperone activity (IDA, PMID:28710280) – direct transfer of nickel to purified urease-URED-UREF.
- Core: GTPase activity, urease activator activity, nickel chaperone activity, nickel cation binding.

## Deep research
- `just deep-research ARATH UREG --provider perplexity` was attempted once (2026-10-23) and failed: "Provider 'perplexity' not available. Available: falcon, openscientist". No deep-research file was generated; review based on cached literature and UniProt.

## Literature status
- PMID:16244137 (Witte 2005, Plant Physiol) – abstract only; full text not retrievable via `just fetch-pmid --force` or Europe PMC. Experimental GOA rows citing it (IDA/IMP/IPI) were accepted on abstract + independent confirmation in PMID:28710280, deferring to the curator.
- PMID:28710280 (Myrach 2017, JBC) – full text cached; key source.
- PMID:23940254 refetched with full text in this session.
- Newly fetched (abstract only): PMID:22271305 (soybean UreG), PMID:11289508 (potato UreG), PMID:10652150 (soybean Eu3/UreG), PMID:20631318 (rice urease/UAPs; not cited).

