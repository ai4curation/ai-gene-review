# CEP89 review notes

## 2026-10-03: sources and scope

- GOA snapshot 38 rows; UniProt Q96ST8. GOA PMIDs cached (PMID:23348840 and PMID:23575228 abstract-only; PMID:23789104 and PMID:21399614 full text).
- Additional papers: PMID:29789620, PMID:32242819 (dual CEP89 layers), PMID:39882855 (Kanie et al. 2025, CEP89 recruits NCS1), PMID:39696441 (Je and Ko 2024, mouse Cep89 and cilia disassembly; cached, not cited in the YAML).
- Deep research: `CEP89-deep-research-falcon.md` is present (falcon; the file reports `cached: true`). It was used for the NCS1 mechanism and for flagging the Kanie hierarchy preprint and the 2024 mouse disassembly study.

## Functional synthesis

- CEP89 (Cep123/CCDC123) is a distal appendage protein recruited by CEP83, but not needed for FBF1/CEP164 [PMID:23348840 "Subsequent recruitment of FBF1 and CEP164 is independent of CEP89 but mediated by SCLT1."]
- Immunogold EM places it on distal appendages, and it is required for ciliary vesicle formation and assembly (not maintenance) of primary cilia [PMID:23789104 "Here, we show that the distal appendage protein Cep123 (Cep89/CCDC123) is required for the assembly, but not the maintenance, of a primary cilium. In the absence of Cep123 ciliary vesicle formation fails, suggesting that it functions in the early stages of primary ciliogenesis."]
- It co-precipitates centriolar satellite proteins [PMID:23789104 "Cep123 interacts with the centriolar satellite proteins PCM-1, Cep290 and OFD1, all of which play a role in primary ciliogenesis."] and is at the base of motile cilia too [PMID:23789104 "Cep123 localized to the base of ependymal cilia confirming that it is a component of both motile and immotile cilia."]
- Mechanism: CEP89 directly binds and recruits NCS1 to the distal appendage; myristoylated NCS1 captures RAB34-positive preciliary vesicles [PMID:39882855 "This localization was completely abolished in CEP89 knockouts, suggesting that CEP89 recruits NCS1 to the distal appendage."]. Deep research adds that CEP89 residues 1-343 bind NCS1 and the C-terminal region targets the centrosome [file:human/CEP89/CEP89-deep-research-falcon.md "CEP89 bound NCS1 through its **N-terminal residues 1–343** and bound CEP15 independently"]. In CEP89 knockouts ciliation is delayed rather than abolished (deep research summary of Kanie et al.).
- Super-resolution shows two CEP89 layers, at distal and subdistal appendage levels [PMID:32242819 "Specifically, we find dual layers of both ODF2 and CEP89, where their localizations are differentially regulated by DAP and sDAP integrity."]
- Mitochondria: a single study reports cytosolic and intermembrane-space pools and reduced complex IV activity on knockdown, plus a patient with a homozygous deletion also covering SLC7A9 [PMID:23575228 "Immunocytochemistry and cellular fractionation experiments showed that CEP89 is present both in the cytosol and in the mitochondrial intermembrane space."]. Not replicated; treated as non-core/undecided.

## Annotation decisions

- Accept centriole, centrosome, basal body, transition fiber, cilium (motile/non-motile) and cilium assembly rows.
- Mitochondrial IMS, mitochondrion organization: non-core. Complex IV assembly IMP: UNDECIDED (single study, mechanism and directness unclear).
- Chemical synaptic transmission and synapse (IEA from fly phenotype): over-annotated.
- Spindle pole and cytosol rows: non-core. OFD1 protein binding: remove.
- NEW protein-macromolecule adaptor activity (GO:0030674) based on the CEP89-NCS1 recruitment data; used as core MF.

## HPA cilium atlas vs module role

- Module role: "distal appendage component".
- HPA v25: Primary cilium (Uncertain); Basal body (Supported); Centrosome (Supported); main location cytosol.
- Comparison: Supported basal body and centrosome calls agree with the module. The cytosolic main location matches the reported cytosolic pool. The module describes CEP89 only as a structural appendage component; the review argues for a more specific role: CEP89 is the appendage adaptor that positions NCS1 for preciliary vesicle capture, which links stage 1 to stage 2 (ciliary vesicle formation) of the module. CEP89 is also not required for FBF1/CEP164 recruitment, and the Kanie preprint (via deep research) suggests the assembly hierarchy is more interconnected than the linear CEP83 -> SCLT1/CEP89 -> FBF1/CEP164 order the module states. This is a refinement, not a contradiction.
