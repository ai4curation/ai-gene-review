# KIF1A review notes

## 2026-09-27 initial review (claude-code)

Sources: UniProt Q12756, cached GOA publications, plus newly cached PMID:9548721, PMID:33880452 and PMID:25265257 (verified via PubMed esummary). No Falcon deep-research file was present at review time.

- Core MF: plus-end-directed microtubule motor activity (GO:0008574). Human KAND variant biophysics: [PMID:33880452 "reduced MT binding, reduced velocity and processivity, and increased non-motile rigor MT binding"].
- Synaptic vesicle precursor transport: Kif1a-null mice [PMID:9548721 "In the nervous systems of these mutants, the transport of synaptic vesicle precursors showed a specific and significant decrease"]. Added NEW GO:0048490.
- Dense core vesicle transport (rat): [PMID:30021165 "We showed that calcium, acting via CaM, enhances KIF1A binding to DCVs and increases vesicle motility"].
- Interkinetic nuclear migration: [PMID:21037580 "An RNAi screen of kinesin genes identified Kif1a, a member of the kinesin-3 family, as the motor for basally directed nuclear movement"]; rescued by human KIF1A. Rat Kif1a (F1M4A4) carries GO:0022027 IMP from this paper; human lacked it, so added NEW (ISS). KIF1A performs the step, so the participation test is met.
- All six PMID:32814053 protein-binding rows REMOVE (HTP interactome, uninformative).
- Retrograde DCV transport (IBA/ISS) kept as non-core: KIF1A is a plus-end motor.
