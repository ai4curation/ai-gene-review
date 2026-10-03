# PDE6D (O43924) research notes

Retinal rod rhodopsin-sensitive cGMP 3',5'-cyclic phosphodiesterase subunit delta (PDEdelta, PrBP/delta), human. A prenyl-binding, GDI-like carrier.

## Deep research status
DEEP_RESEARCH_STATUS_PLACEHOLDER

## Summary of function
- Original description: [PMID:9570951 "A novel subunit, termed PDE delta (HGMW-approved symbol, PDE6D; MW 17 kDa), is able to detach PDE partially from bovine rod outer segment membranes under physiological conditions."]
- Carrier of prenylated proteins, regulated by Arl2-GTP: [PMID:11980706 "PDE delta is structurally closely related to RhoGDI and contains a deep empty hydrophobic pocket."; "We suggest PDE delta to be a specific soluble transport factor for certain prenylated proteins and Arl2-GTP a regulator of PDE delta-mediated transport."]
- Farnesyl binding and Arl2/Arl3 release: [PMID:22002721 "Here we report the structure of fully modified farnesylated Rheb-GDP in complex with PDEδ."; "We demonstrate that the G proteins Arl2 and Arl3 act in a GTP-dependent manner as allosteric release factors for farnesylated cargo."]
- RAS (non-ciliary): [PMID:23698361 "Correct localization and signalling by farnesylated KRAS is regulated by the prenyl-binding protein PDEδ, which sustains the spatial organization of KRAS by facilitating its diffusion in the cytoplasm."] Also Rap1 in retina (PMID:30257685).
- Cilia: INPP5E targeting, Joubert syndrome. [PMID:24166846 "depletion of PDE6D with two independent siRNAs led to a virtually complete loss of ciliary INPP5E, suggesting that PDE6D is indispensible for proper INPP5E ciliary targeting"]. Not required for ciliogenesis [PMID:24166846 "indicating that PDE6D is not involved in ciliary biogenesis"].
- Photoreceptors: [PMID:17496142 "Thus the absence of PrBP/delta in retina impairs transport of prenylated proteins, particularly GRK1 and cone PDE, to rod and cone outer segments"]
- RPGR scaffold: [PMID:23559067 "we propose a model where RPGR is acting as a scaffold protein recruiting cargo-loaded PDEδ and Arl3 to release lipidated cargo into cilia."]
- Rab13: [PMID:9712853 "Purified recombinant delta-PDE had the capacity to dissociate Rab13 from cellular membranes."]

## Key curation decisions
- Core MF: molecular carrier activity (GO:0140104; IEA/ISS accepted). NEW: farnesylated protein binding (GO:0001918, verified in OLS), IDA from PMID:22002721. This is the cargo-recognition MF and is directly supported by structure and by binding of KRAS, RHEB and INPP5E.
- Protein binding rows: ARL2/ARL3/ARL15/ARL16 changed (MODIFY) to small GTPase binding. HRAS and RHEB changed to farnesylated protein binding. RAB13 changed to small GTPase binding. RPGR rows, tir (EHEC), OTP: REMOVE (generic). The RPGR scaffold relationship is noted in the description and a suggested question.
- GTPase inhibitor activity (IEA/ISS): KEEP_AS_NON_CORE. It is a consequence of binding ARL2/3-GTP, not the evolved function.
- Cilium (Reactome TAS): KEEP_AS_NON_CORE. PDE6D is mainly cytosolic and hands off cargo at the transition zone and proximal cilium.
- No NEW process term for Ras plasma-membrane localization. It is raised as a suggested question, with RhoGDI/UNC119 comparators to be checked first, per CLAUDE.md's bar for NEW process terms.

## HPA cilium atlas vs module role
- Module stage 5: "Lipidated cargo carriers" (PDE6D with UNC119B); "Carry lipidated proteins to the cilium for ARL3-dependent release"; process protein localization to cilium.
- HPA v25: no cilium, basal body or centrosome call; main location Vesicles. This is consistent with PDE6D being a soluble cytosolic carrier, enriched only transiently near the transition zone (PMID:24166846). It is not a resident ciliary protein, so no HPA ciliary call is expected.
- Assessment: core_functions agrees with the module's ciliary-carrier role, framed as cytosolic carrier activity plus protein localization to cilium. It adds a separate, cilium-independent core function: solubilization of farnesylated Ras-family GTPases (KRAS, HRAS, RHEB). The module's stage-5 placement is a correct but partial view of PDE6D. It should not be read as PDE6D being a cilium-specific protein.
