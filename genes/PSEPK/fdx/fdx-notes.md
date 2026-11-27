# fdx curation notes

- Q88PK3 is an Isc-associated [2Fe-2S] ferredoxin encoded in the KT2440 isc locus. Its core role is electron transfer during cluster assembly.
- Reconstituted *E. coli* ISC machinery directly assigns Fdx a reductive step after IscS-dependent persulfide insertion [PMID:39870763 "the persulfide is cleaved into sulfide by the ferredoxin Fdx, leading to a [1Fe-1S] precursor"].
- Eukaryotic structural work independently supports close engagement of ferredoxin with the core ISC assembly site for electron transfer, but it is ortholog context rather than direct evidence for Q88PK3 [PMID:39632806 "facilitating the movement of the [2Fe-2S] cluster of FDX2 closer to the ISCU2 FeS cluster assembly site for rapid electron transfer"].


## Isc comparative-evidence audit (2026-11-07)

Fdx (PP_0847) is the Isc-associated 2Fe-2S ferredoxin of Pseudomonas putida KT2440. Its specific ferredoxin family supports electron transfer during iron-sulfur cluster assembly. In reconstituted bacterial homolog systems, reduced Fdx supplies electrons for sulfur reduction at the assembly machinery; the physiological reductase partner and dependence on this particular ferredoxin remain unresolved in KT2440.

The target remains KT2440; no purified target assay is claimed. Specific curated HAMAP/RuleBase statements or independent NCBIfam/InterPro signatures ground the target inference. ARBA names are not used as proof. All original ordered source payloads are retained. The rows are IEA or historical NEW, not IBA; no donor-count argument, PAINT loss or new evolutionary node placement is asserted.

A genuine Falcon request failed with HTTP 403 authentication/access failure. Existing OpenScientist reports, where present, were preserved; no provider-branded replacement was fabricated. The log is `.cache/module-audit-logs/isc-20261107/psepk-consultation/falcon-fdx.log`.

### Evidence and biological limits

- [PMID:39870763] E. coli Fdx supplies electrons for persulfide reduction in a reconstituted cluster-assembly system. Quoted support: “the persulfide is cleaved into sulfide by the ferredoxin Fdx”.
- [PMID:39632806] Mitochondrial ferredoxin-2 binding illustrates a related electron-delivery system, but does not establish the bacterial target interaction network.
- [PMID:34781750] The bacterial ISC electron-delivery relay includes Fdx and reductase-mediated regeneration. Quoted support: “Fdx interacts with IscS, and reduced Fdx provides an electron to the IscS complex for sulfane (S0) reduction”.

### Decisions

- GO:0005829 cytosol: ACCEPT. The specific Isc ferredoxin family and intracellular cluster-assembly role support the existing cytosolic location. This is a conserved functional inference, not a target fractionation result; inferred location is not peripheral merely because direct imaging is absent.
- GO:0009055 electron transfer activity: ACCEPT. Independent Fdx_isc NCBIfam/InterPro classification supports an electron carrier. E. coli reconstitution provides positive mechanistic support for persulfide reduction, whereas mitochondrial FDX2 work concerns a distinct system and is not treated as a target assay.
- GO:0022900 electron transport chain: ACCEPT. GO0022900 is not restricted to respiratory membranes: it describes a series of electron carriers transferring electrons to terminal acceptors. The specific Isc ferredoxin assignment and reconstituted bacterial reductase-ferrodoxin sulfur-reduction relay support this broad inherited process by homolog inference. Exact native KT2440 reductase identity is unresolved; no respiratory or P450 terminal acceptor is asserted.
- GO:0051536 iron-sulfur cluster binding: MODIFY. Correct but general; the [2Fe-2S] cofactor of the Isc ferredoxin family is captured by the specific child term GO:0051537, which this gene already carries.
- GO:0051537 2 iron, 2 sulfur cluster binding: ACCEPT. The independently recognized ferredoxin fold and Fdx_isc family support cluster binding without relying on the ARBA cofactor label. No additional cluster stoichiometry or ligand geometry is claimed from target experiments.
- GO:0140647 P450-containing electron transport chain: REMOVE. The adrenodoxin-like fold includes distinct terminal-partner specificities. Q88PK3 has the independently recognized Fdx_isc signature and Isc sulfur-reduction role, whereas no independent evidence connects this protein to a P450-containing relay. The generic fold does not justify importing the P450-specific process from related ferredoxins. This rejects that mapping, not all conceivable promiscuous electron transfer or the broader electron-transport-chain claim.
- GO:0016226 iron-sulfur cluster assembly: NEW. The original ISS/file payload is preserved. Independent Isc-specific family assignment plus direct E. coli reconstitution support the mechanistic inference beyond operon adjacency. The source experiment is not native KT2440 evidence and does not prove this target is the only possible electron donor.

Current QuickGO GO:0022900 includes nonrespiratory electron-carrier relays. The retained parent and removed P450-specific child therefore differ for biological specificity, not because soluble proteins cannot participate in electron transport.

Additional primary scope check [25688831]: E. coli FNR and Fdx support NADPH-driven cluster assembly in reconstitution; native KT2440 donor identity remains untested. Quoted support: “using electron transfer between NADPH and ferredoxin-NADP-reductase to reduce ferredoxin”. The E. coli assay does not establish a native KT2440 kinetic pathway.
