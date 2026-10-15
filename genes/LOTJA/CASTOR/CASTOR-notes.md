# CASTOR (Lotus japonicus, Q5H8A6) – curation notes

## Sources
- Deep research: `CASTOR-deep-research-falcon.md` (present).
- Cached: PMID:19106374 and PMID:31420535 full text; PMID:15616514, 16903357, 22706284, 27230377, 39140702 abstract only.
- DOIs resolved to PMIDs with the PubMed MCP (31420535, 22706284, 27230377, 39140702).

## Identity and localization
- Gene identified with its twin POLLUX as a common symbiosis gene [PMID:15616514 "CASTOR and POLLUX, that are indispensable for microbial admission into plant cells and act upstream of intracellular calcium spiking"].
- The plastid localization in that paper came from overexpressed fusions. Native protein is at the nuclear envelope [PMID:19106374 "Immunogold labeling localized the endogenous CASTOR protein to the nuclear envelope of Lotus root cells."]. Inner versus outer membrane could not be resolved [PMID:19106374 "we could not determine whether CASTOR resides in the inner or outer membrane of the nuclear envelope or in both"].
- CASTOR and POLLUX form separate homocomplexes [PMID:19106374 "CASTOR and POLLUX form two independent homocomplexes in planta"].

## Channel activity: the K+ vs Ca2+ debate
- Full-length CASTOR in bilayers: 260 pS, weak cation selectivity, K+ preferred [PMID:19106374 "a weak preference of CASTOR for cations such as potassium over anions"]. The authors infer K+ is the main ion in vivo and propose a counter-ion or membrane-potential role [PMID:19106374 "compensate the charge release during the calcium efflux as counter ion channels"].
- Kim et al. 2019: a truncated, plasma-membrane-targeted pore construct (CASTOR-2TM) is Ca2+-selective and Ca2+-activated [PMID:31420535 "CASTOR from Lotus japonicus is a highly selective Ca2+ channel whose activation requires cytosolic/nucleosolic Ca2+, contrary to the previous suggestion of it being a K+ channel"]. The RCK gating-ring structure and the nodulation-rescue failure of Ca2+-site mutants are solid.
- CNGC15 is the nuclear-envelope Ca2+ channel and complexes with the K+-permeable DMI1 [PMID:27230377 "the cyclic nucleotide-gated channels form a complex with the postassium-permeable channel, which modulates nuclear Ca(2+) release"].
- 2024 review: the question is still open [PMID:39140702 "important questions remain, including the exact function of the DMI1 channel"].
- Decision: MF annotated at the level of `monoatomic cation channel activity` (GO:0005261). K+ transport is kept because full-length bilayer data support it. Calcium channel activity is not asserted.

## Genetics
- castor mutants lack Ca2+ spiking but keep the initial Ca2+ flux [PMID:16903357 "castor, pollux, nup133, and sym24) defective for calcium spiking retained a calcium flux"].
- castor-2 (pore-region A264T) is defective in both symbioses [PMID:19106374 "The castor-2 mutant is defective in Ca 2+ spiking ( Figure 5 ) and both root nodule and arbuscular mycorrhiza symbioses"].
- Channel-dead Ca2+-site mutants fail to rescue nodulation [PMID:31420535 "plants expressing D442A, E493A, or E493Q mutants failed to form root nodules"].
- DMI1 alone rescues Lotus castor/pollux mutants, while Lotus needs both channels [PMID:22706284].

## NEW-term checks
- Nodulation (GO:0009877) and AM association (GO:0036377): CASTOR's channel conductance is a mechanistic step in generating nuclear Ca2+ spikes, so it participates and is not merely required. Comparator check (QuickGO, taxa 3880/34305): CNGC15A/CNGC15B (IMP), CCaMK (IMP) and CYCLOPS (IMP/IBA) carry these terms. These are proteins in the same role (nuclear Ca2+ spiking machinery or its decoders), so the term absence for CASTOR is a gap, not a convention.
- GOA has only 3 IEA rows for CASTOR (no MF, no experimental rows), so these additions are not overruling any curator.

## Project relevance (symbiosis vs defense)
- CASTOR is purely a symbiosis-pathway component. There is no evidence for a role in fungal or bacterial defense, and no defense terms are proposed.
- Medicago DMI1 (POLLUX ortholog) is reviewed separately; DMI1-specific experiments were not transferred to CASTOR.
