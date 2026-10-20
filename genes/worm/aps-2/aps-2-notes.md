# aps-2 — AP-2 complex subunit sigma (Q19123, TrEMBL) — curation notes

## Identity
- `aps-2` (F02E8.3) encodes the sigma2 (AP17) small subunit of the AP-2 clathrin adaptor complex [PMID:10588660 "elegans proteins representing probable CCP components: clathrin heavy chain (T20G5.1), α-adaptin (T20B5.1), β-adaptin (Y71H2_389.E), μ2 (R160.1), and ς2 (F02E8.3)."]. Shim & Lee (2000; abstract only) determined the genomic structure and reported expression in most cells during embryogenesis and mainly in neurons and some hypodermal cells after hatching [PMID:10901169 "the two genes are expressed primarily in neurons and some hypodermal cells following hatching through adulthood"].

## Molecular role
- Sigma2 is tightly bound to alpha-adaptin and forms with it one hemicomplex of AP-2; it is unstable (~10% of wild type) in apa-2 mutants but remains at the nerve ring (40%) in mu2 mutants [PMID:23482940 "On the other hand, the small σ2 subunit, which is normally tightly bound to α-adaptin, is unstable in apa-2 mutants."] [PMID:23482940 "Tagged σ2-adaptin is still localized to the nerve ring (Figure 6A) and is reduced to 40% as assayed by fluorescence (Figure 6, Table 1)."].
- The sigma2 surface forms the dileucine-motif binding pocket, latched in the closed conformation by the beta N-terminus; fcho-1 bypass suppressors map to this latch [PMID:25303366 "In the unlatched state, the N-terminus of the beta subunit disconnects from the alpha and sigma2 subunits and exposes the dileucine-motif binding pocket (Kelly et al., 2008)."] [PMID:25303366 "(B) Mutations in the latching mechanism formed by the N-terminus of beta and the di-leucine motif binding-pocket of sigma2."].
- Clathrin is recruited to AP-2 by the beta subunit, not by sigma2 [PMID:23482940 "Although clathrin is largely recruited to AP2 by the β subunit, even in the absence of β, it could still be recruited indirectly to the complex via AP180"].

## Phenotypes
- aps-2 deletion mutants are viable and show the jowls phenotype shared by apa-2, apm-2 and fcho-1 [PMID:25303366 "Deletion of the sigma subunit (aps-2) produces a similar ‘jowls’ phenotype (Figure 1A and Figure 1—figure supplement 1B), while the beta subunit is shared by both AP1 and AP2 in C."].
- RNAi of sigma2 gives severely dumpy progeny but does not reduce yolk uptake [PMID:10588660 "All progeny of Ce- μ2(RNAi) and Ce- ς2(RNAi) mothers were severely dumpy (Dpy)."] [PMID:10588660 "Unlike the other CCP components we tested, Ce- μ2(RNAi) and Ce- ς2(RNAi) did not result in an apparent reduction in YP170::GFP uptake into the oocyte."]. Shim & Lee reported embryonic and larval lethality after RNAi (abstract only) [PMID:10901169 "RNA interference experiments showed that the reduction of either apm-2 or aps-2 gene function causes embryonic lethality, larval lethality at various stages of development, and other morphological defects in the larval stages."], which sits uneasily with the viability of deletion alleles.
- aps-2 RNAi did not increase germ-cell corpses, unlike apa-2, apb-1 and dpy-23 RNAi [PMID:23696751 "germ cell corpses increased significantly in an age-dependent manner in animals with RNAi of apa-2, apb-1, and dpy-23, but not aps-2, which encodes the σ2 subunit of the AP2 complex"].

## Curation decisions
- Clathrin binding (ISS, PMID:10901169) is removed: sigma2 lacks a clathrin-binding element; clathrin recruitment is a beta-subunit function.
- Embryo/larval development rows are marked over-annotated because deletion mutants are viable; body morphogenesis (Dpy) is kept as non-core.

## Additional literature surfaced by deep research (not in GOA; see aps-2-deep-research-falcon.md)
- APS-2::GFP nerve-ring fluorescence falls to 11% in apa-2 and 39% in apm-2 mutants [file:worm/aps-2/aps-2-deep-research-falcon.md "Nerve-ring fluorescence: wild type **3543 ± 169 (100%)**; *apa-2/α* mutant **389 ± 28 (11%)**; *apm-2/μ2* mutant **1391 ± 51 (39%)**; comparisons **p < 0.0001**."].
- aps-2(tm2912) is a 194-bp coding deletion with temperature-dependent growth and locomotion defects that enhance neuronal alpha-synuclein toxicity (Kuwahara et al. 2008, DOI 10.1093/hmg/ddn198); aps-2 mutants also reduce GLR-1 abundance at ventral-cord synapses (Garafalo et al. 2015, DOI 10.1091/mbc.e14-06-1048).
