# NDE1 review notes

## 2026-09-27 initial review (claude-code)

Sources: UniProt Q9NXR1, GOA (87 rows), cached publications (several newly cached:
PMID:15473967, 17682047, 20403325, 21529751, 27553190, 21394081, 25245017, 35493069).

### Molecular function
- Binds dynein IC and LC8, not the motor domain [PMID:17682047 "Surprisingly, NudE interacted not with the dynein motor domain but with both the intermediate chain IC2C and the light chain LC8."].
- Recruits LIS1 to dynein [PMID:20403325 "We find that NudE stably recruits LIS1 to the dynein holoenzyme molecule"].
- Patient truncations lose dynein binding [PMID:21529751 "We show that the patient NDE1 proteins are unstable, cannot bind cytoplasmic dynein, and do not localize properly to the centrosome."].
- RAB9 effector [PMID:34793709 "Therefore, Nde1 is a Rab9 effector that tethers Rab9-associated late endosomes to the dynein motor for their retrograde transport to the TGN."].
- Dimers/tetramers, direct NDE1-NDEL1 interaction [PMID:22843697].
- GOA has no dynein complex binding for NDE1 (or NDEL1), while LIS1, BICD2, NUMA1 carry GO:0070840 -> proposed NEW.

### Localization
- Centrosome/mother centriole, spindle, kinetochores (CENP-F dependent) [PMID:17600710 "We show that Ndel1, Nde1, and Lis1 localize to kinetochores in a Cenp-F-dependent manner."].
- Nuclear envelope in prophase via NUP133-CENP-F [PMID:21383080 "At this stage, the kinetochore constituents CENP-F, NudE, NudEL, dynein, and dynactin accumulate at the NE."] -> NEW GO:0005635.

### Processes
- Kinetochore dynein and metaphase alignment [PMID:17600710 "In addition, Nde1, but not Ndel1, is required for kinetochore localization of Dynein."].
- Apical INM in rat radial glia, NDE1-specific [PMID:27553190 "However, NDE1 inhibition alone causes a complete block of apical INM"; "RNAi against the NDE1 paralogue NDEL1 has no such effects."]; CDK1 sites T215/T243 [PMID:39167527].
- Postmitotic neuronal migration: NDE1 and NDEL1 comparable [PMID:27553190 "NDE1 and NDEL1 RNAi have comparable effects on postmitotic neuronal migration."].
- Microcephaly/microlissencephaly [PMID:21529751, PMID:21529752]; mouse Nde1-null microcephaly with spindle orientation and centrosome duplication defects [PMID:15473967].
- Cilium length restriction at mother centriole [PMID:21394081] (mouse/zebrafish) - noted in description, not added as NEW.
- Nuclear pool / heterochromatin replication [PMID:25245017] - noted as a question.

### Decisions of note
- Kinesin complex IBA -> REMOVE (NDE1 is a dynein regulator, not a kinesin subunit).
- Protein binding rows -> REMOVE, except NDEL1 (22843697) -> MODIFY to protein heterodimerization activity.
- identical protein binding -> MODIFY to protein homodimerization activity.
- Chromosome localization IMP -> MODIFY to metaphase chromosome alignment.

### Relevance to nucleokinesis module
- Module lumps NDE1/NDEL1 as one NudE unit. Data show asymmetry: NDE1 (not NDEL1) needed for apical INM in radial glia, both comparable in postmitotic migration; NDEL1 overexpression rescues INM.

### Deep research incorporated (NDE1-deep-research-falcon.md, arrived after first draft)
- Pointed to Zhao et al. 2023 [PMID:37940657 "We find that Nde1 recruits Lis1 to autoinhibited dynein and promotes Lis1-mediated assembly of dynein-dynactin adaptor complexes."] - cached and used to support NEW dynein complex binding / adaptor MF and core function.
- Confirms NDE1 (not NDEL1) requirement for apical INM; NDE1 enriched in progenitors, NDEL1 in postmitotic neurons (Tsai 2024, not cached).
- Cilium disassembly complex (Maskey 2015, Gabriel 2016) and proteasome association (Monda 2018) noted but not cached/annotated.
