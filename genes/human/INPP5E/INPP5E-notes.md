# INPP5E (Q9NRR6) curation notes

## Deep research status
DR_STATUS_PLACEHOLDER

## Summary of function
- Type IV 5-phosphatase specific for lipid substrates [PMID:10764818 "This enzyme hydrolyzes only lipid substrates, phosphatidylinositol 3,4,5-trisphosphate and phosphatidylinositol 4,5-bisphosphate."] with the highest PI(3,4,5)P3 affinity of known 5-phosphatases (Km 0.65 uM).
- UniProt also lists PI(3,5)P2 (by similarity) and low-affinity Ins(1,4,5)P3 hydrolysis (PMID:40969890; cached abstract is about synaptojanin-1 and does not mention INPP5E).
- Joubert syndrome mutations impair activity [PMID:19668216 "Mutations clustered in the phosphatase domain and impaired 5-phosphatase activity, resulting in altered cellular PtdIns ratios."]; INPP5E localizes to cilia [PMID:19668216 "INPP5E localized to cilia in major organs affected by Joubert syndrome"].
- Mouse: axonemal localization; loss destabilizes pre-formed cilia but not assembly [PMID:19668215 "Inpp5e inactivation did not impair ciliary assembly but altered the stability of pre-established cilia after serum addition."]
- Sets ciliary lipid identity [PMID:26305592 "Thus, Inpp5e limits ciliary PI(4,5)P2 and generates ciliary PI(4)P, consistent with a role in converting PI(4,5)P2 to PI(4)P within cilia."; PMID:26190144 "Upon INPP5E inactivation, PI(4,5)P2 accumulates at the ciliary tip whereas PI4P is depleted."], restricting TULP3/GPR161 [PMID:26305592 "Inpp5e limits the ciliary levels of inhibitors of Hh signaling, including Gpr161 and the PI(4,5)P2-binding protein Tulp3."]
- Delivered to cilia as farnesylated PDE6D cargo [PMID:24166846 "these results indicate that PDE6D is required for INPP5E ciliary targeting"].

## Key decisions
- Core MF: GO:0004439 (PI(4,5)P2 5-phosphatase) and GO:0034485 (PI(3,4,5)P3 5-phosphatase); process GO:0046856.
- GO:0004445 (compound soluble inositol-polyphosphate term) MODIFY -> lipid 5-phosphatase terms.
- REMOVE: PI(3,4,5)P3 3-phosphatase (wrong position), negative regulation of translation (no basis), 14-3-3 protein binding rows.
- Reactome PI biosynthetic process MODIFY -> phosphatidylinositol dephosphorylation.
- NEW: ciliary membrane (GO:0060170), ISS from mouse data (PMID:26305592).

## HPA cilium atlas vs module role
- Module (stage 5): ciliary PI(4,5)P2 5-phosphatase (GO:0004439) located in ciliary membrane.
- HPA v25: no cilium/basal body call; main location Golgi apparatus. No HPA-sourced GOA rows.
- Interpretation: the Golgi call agrees with the documented Golgi-stack pool (UniProt, by similarity). The absence of an HPA primary-cilium call conflicts with robust ciliary localization of INPP5E in human and mouse literature; it may reflect antibody performance in the HPA cell lines or cell-type heterogeneity of the ciliary proteome reported by the atlas [PMID:41005307 "We found that 69% of the ciliary proteome is cell-type specific, and 78% exhibited single-cilia heterogeneity."]. core_functions agree with the module (PI(4,5)P2 5-phosphatase in the ciliary membrane), adding PI(3,4,5)P3 5-phosphatase activity.
