# TMEM216 (Q9P0N5) review notes

## Deep research status
- Falcon was run with `--fallback perplexity-lite` (600 s default; fallback not available here), then rerun with `--timeout 2400`. The first 2400 s attempt exited with code 137 (killed), so it was retried; the outcome is at the bottom of this file. The review rests on cached primary literature.

## Protein
- Small (148 aa) tetraspan membrane protein (Transmemb_17 / IPR019184). Worm ortholog MKS-2.
- Disease: JBTS2 [PMID:20036350 "we identified a homozygous mutation, R12L, in the TMEM216 gene, in all affected individuals"], MKS2, OFD VI, RP98.

## Location
- Ciliary base [PMID:22282472 "Immunostaining of endogenous TMEM138 with a marker (Arl13b) of the ciliary axoneme and transition zone demonstrated closely adjacent localization with TMEM216 at the base of cilia"]; [PMID:20512146 "TMEM216 antibody also reacted strongly to the base of cilia in organs like kidney containing ciliated cells"].
- Vesicles/Golgi [PMID:22282472 "It is noteworthy that TMEM216 localized to post-Golgi vesicles along microtubules, as well as the Golgi apparatus surrounding the base of cilium"].
- Mouse TZ/basal body [PMID:21725307 "Tmem216 occasionally localized to the transition zone, but more typically localized to the basal body or axoneme."].
- MKS components between axoneme and membrane [PMID:28401750 "MKS complex components (Tectonic, MKS1, TMEM216, B9D1 and B9D2) localized between the axonemal MTs and the ciliary membrane"].

## Complex
- [PMID:21725307 "we have identified a complex containing Tctn1, Tctn3 and seven MKS proteins (Mks1, Tmem216, Tmem67, Cep290, Cc2d2a, B9d1 and Tctn2)"]. Possibly peripheral [PMID:21725307 "Thus, Cep290, Tmem67 and Tmem216 may be substoichiometric or peripheral components of the Tectonic complex."].
- With meckelin [PMID:20512146 "Both assays detected a complex between TMEM216 and Meckelin."].
- Worm: core, mutually dependent MKS proteins [PMID:26982032 "Since MKS-1/MKSR-1/MKSR-2/MKS-2/TMEM-231 all depend on each other for their TZ localisation"].

## Function
- Ciliogenesis [PMID:20512146 "Tmem216 knockdown prevented ciliogenesis in polarized cells, and blocked correct docking of centrosomes at the apical cell surface"]; [PMID:22282472 "suggesting that both TMEM138 and TMEM216 are required for ciliogenesis"].
- Dvl1/RhoA, possible non-canonical Wnt co-receptor with meckelin [PMID:20512146 "We therefore speculate that TMEM216, a novel tetraspan protein, forms a non-canonical Wnt receptor-coreceptor complex with Meckelin."]. Speculative; not annotated.

## Curation decisions
- Cytosol (Reactome TAS, x3): REMOVE. It is a multi-pass membrane protein.
- Protein binding (TMEM107): REMOVE (uninformative; MKS complex covers it).
- Positive regulation of cilium assembly (IEA/ISS): MODIFY to cilium assembly. The evidence is a requirement, not modulation.
- Photoreceptor morphogenesis/maintenance, positive regulation of Smo signalling (ISS/IEA): KEEP_AS_NON_CORE.
- No NEW TZ-assembly annotation. Unlike TCTN2/TMEM231, there is no direct mammalian data showing TMEM216 loss removes other TZ components or TZ structure, so I did not add GO:1905349. The worm MKS-2 mutual-dependence data support protein localization to TZ.

## HPA cilium atlas vs module role
- HPA (member_evidence.md): no cilium/centrosome call; "not in HPA" (no HPA v25 subcellular data). The Hansen et al. 2025 cilium atlas [PMID:41005307 "We employed antibody-based spatial proteomics to expand the Human Protein Atlas to primary cilia."] therefore gives no evidence either way. A small tetraspan protein may lack a validated antibody.
- Module role: MKS module component (diffusion barrier; TZ assembly). Literature supports MKS module membership and TZ/ciliary-base localization. Direct evidence that TMEM216 itself builds the TZ is weaker than for TMEM231/TCTN2. core_functions therefore list MKS complex, TZ location, protein localization to TZ and cilium assembly, but not TZ assembly itself. This is a mild divergence from the module, which assigns TZ assembly to the whole MKS complex. Holding it at the complex level is fine.
