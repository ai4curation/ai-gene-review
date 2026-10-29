# EBF1 (At2g25490, Q9SKK0) curation notes

## 2026-10-05 session (ethylene_signaling module)

- Deep research (falcon) failed (exit code 1); review based on cached literature and UniProt.
- F-box/SCF: [PMID:15090654 "two F-box proteins, EBF1 and -2, that work coordinately in SCF complexes to repress ethylene action"; "EBF1 and -2 interact directly with ethylene insensitive 3 (EIN3)"].
- EIN3 degradation: [PMID:14675532 "In the absence of ethylene, EIN3 is quickly degraded through a ubiquitin/proteasome pathway mediated by two F box proteins, EBF1 and EBF2."]
- Genetics: [PMID:14675533 "plants carrying the ebf1 and ebf2 mutations display a constitutive ethylene response and accumulate the EIN3 protein in the absence of the hormone"].
- Paralog roles: [PMID:17307926 "the SCF EBF1 and SCF EBF2 E3 complexes work in concert to fine-tune the abundance of EIN3/EIL1 in response to ambient hormone levels"].
- Ethylene downregulates EBF1/2 protein [PMID:20647342] and EIN2 represses EBF1/2 translation via 3' UTR [PMID:26496607 "EIN2 imposes the translational repression of EBF1 and EBF2 mRNA"]; EBF2 translational control [PMID:26496608].
- Localization: nucleus and cytoplasm [PMID:23166809].
- Protein binding: 33 IPI rows. EIN3 and ASK/CUL1 partners -> MODIFY to GO:1990756 ubiquitin-like ligase-substrate adaptor activity; high-throughput interactome partners (PMID:32612234) -> REMOVE.
- Possible identifier issue: IPI with P43291 (SRK2A/SnRK2.4, synonym "ASK1") from PMID:14675532/14675533 likely intended SKP1A/ASK1 (Q39255); flagged, removed as uninformative protein binding.
