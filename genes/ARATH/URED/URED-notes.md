# URED notes

- Required for urease activation; mutant lacks urease activity [PMID:16244137 "Plants bearing T-DNA or Ds element insertions in either the structural gene for urease or in any of the three putative urease accessory genes AtureD, AtureF, and AtureG lacked the corresponding mRNAs and were defective in urease activity."]
- Interaction map [PMID:28710280 "In the absence of urease, direct binding of UreD to UreF was observed"; "a direct interaction with urease was only observed for UreD but not for UreF or UreG"; "Co-purification of urease with tagged UreF was only possible in the presence of UreD"]
- Nickel binding (InterPro2GO) marked over-annotated: no plant data; bacterial UreD binds Ni weakly with Zn competition [PMID:20207756]; bacterial UreF is a fidelity gatekeeper coupling UreG GTPase [PMID:22369361]; nickel carrier in plants is UREG [PMID:28710280].

## Decisions
- Core: urease activator activity (GO:0018237), directly_involved_in urea catabolic process (GO:0043419; GO relates the urease activator complex GO:0150006 to it by "capable of part of"), the same core process used for every urease accessory protein in the urease module; protein maturation (GO:0051604) is kept as non-core, in urease activator complex (GO:0150006), cytoplasm.
- urea catabolic process (IDA) KEEP_AS_NON_CORE (acts upstream of hydrolysis); IBA urea metabolic process TOO_GENERAL.
- GO:0110147 "protein maturation by nickel ion transfer" is obsolete; its GO record gives `replaced_by` GO:0051604 (go-ontology issue 29105), so protein maturation is the most precise available term.

## Deep research
- `just deep-research ARATH UREG --provider perplexity` was attempted once (2026-10-23) and failed: "Provider 'perplexity' not available. Available: falcon, openscientist". No deep-research file was generated; review based on cached literature and UniProt.

## Literature status
- PMID:16244137 (Witte 2005, Plant Physiol) – abstract only; full text not retrievable via `just fetch-pmid --force` or Europe PMC. Experimental GOA rows citing it (IDA/IMP/IPI) were accepted on abstract + independent confirmation in PMID:28710280, deferring to the curator.
- PMID:28710280 (Myrach 2017, JBC) – full text cached; key source.
- PMID:23940254 refetched with full text in this session.
- Newly fetched (abstract only): PMID:22271305 (soybean UreG), PMID:11289508 (potato UreG), PMID:10652150 (soybean Eu3/UreG), PMID:20631318 (rice urease/UAPs; not cited).

