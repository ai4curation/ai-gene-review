# TMEM231 (Q9H6L2) review notes

## Deep research status
- Falcon was run with `--fallback perplexity-lite` (600 s; fallback not available here), then rerun with `--timeout 2400`; the outcome is at the bottom of this file. The review rests on cached primary literature.

## Protein
- Two-pass transmembrane protein (TM 23-43, 262-282), TMEM231 family; only in ciliated organisms [PMID:25869670 "TMEM231 orthologues are not found in unciliated organisms, further suggesting that this protein has conserved roles in ciliary biology."].
- Disease: JBTS20 [PMID:23012439 "Our data suggest that mutations in TMEM231 cause JBTS"], MKS11, OFD3.

## Key findings
- Early basal body arrival [PMID:22179047 "A transmembrane component, TMEM231, localizes to the basal body before and independently of intraflagellar transport in a Septin 2 (Sept2)-regulated fashion."].
- Interdependence [PMID:22179047 "The localizations of TMEM231, B9D1 (B9 domain-containing protein 1) and CC2D2A (coiled-coil and C2 domain-containing protein 2A) at the transition zone are dependent on one another and on Sept2."].
- MKS complex [PMID:25869670 "These data reveal that Tmem231 is a biochemical component of the MKS complex."].
- Organizes the TZ [PMID:25869670 "In mice, B9d1 and Tmem231 are required for the TZ localization of each other and their interacting proteins, Tmem67 and Mks1."]. The NPHP module is independent of it [PMID:25869670 "In contrast, neither Rpgrip1l nor Nphp1 require Tmem231 or B9d1 to localize to the TZ"].
- Membrane composition [PMID:25869670 "For example, Arl13b, Adcy3, Pkd2, and Inpp5e fail to localize to cilia in Tmem231−/− MEFs"]. Not essential for ciliogenesis in MEFs [PMID:25869670 "Thus, Tmem231 and B9d1 are essential for controlling the composition of the ciliary membrane, but are not essential for ciliogenesis."]. Knockdown reduced cilia in Chih et al. [PMID:22179047 "Disruption of the complex in vitro causes a reduction in cilia formation and a loss of signalling receptors from the remaining cilia."].
- Worm: TMEM-231 TZ localization needs MKS-2 and MKS-5 but not NPHP-4 [PMID:25869670 "TMEM-231::GFP (green) is enriched at the TZ of wild-type animals, but is mislocalized in the mks-2 and mks-5 mutants, but not in the nphp-4 mutants."].

## Curation decisions
- Protein binding: HuRI Y2H (KRT31, KRT40, NOTCH2NLA) REMOVE; TMEM107 REMOVE (MKS complex covers it).
- Cilium assembly: ACCEPT, with a tissue-dependence caveat.
- Smoothened signalling: KEEP_AS_NON_CORE.
- NEW: GO:1905349 ciliary transition zone assembly (IMP, PMID:25869670). The paper's own conclusion is "organizes the ciliary transition zone". Scaffold-case participation; see the reason text for the comparator/sparse-term argument.

## HPA cilium atlas vs module role
- HPA (member_evidence.md): no cilium/centrosome call; HPA main location "Vesicles". Hansen et al. 2025 [PMID:41005307 "We found that 69% of the ciliary proteome is cell-type specific, and 78% exhibited single-cilia heterogeneity."]. The atlas did not detect TMEM231 at cilia in its three cell lines. A vesicular signal is compatible with trafficking of a membrane protein (it is septin-dependent and reaches the basal body via vesicles), but it is not evidence against TZ localization: the TZ pool is small, and the literature (mouse tissues, worms) is strong.
- Module role: MKS module component, ciliary diffusion barrier, TZ assembly. Fully consistent with the literature. TMEM231 is one of the best-supported MKS members for the TZ assembly role, and core_functions follow the module.
