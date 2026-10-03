# NPHP1 (nephrocystin-1, O15259) review notes

## Deep research status
- Falcon was run with `--fallback perplexity-lite` (600 s; fallback not available here), then rerun with `--timeout 2400`; the outcome is at the bottom of this file. The review rests on cached primary literature.

## Protein
- Coiled-coil, SH3 and nephrocystin homology domain (NHD) [PMID:12006559 "revealed three distinct conserved domains including Src homology 3 and coil-coil domains in the N-terminal region, as well as a large highly conserved C-terminal region"].
- Adaptor [PMID:15661758 "Nephrocystin is an adaptor protein that is able to associate with signaling molecules involved in cell adhesion and actin cytoskeleton organization, such as p130Cas, Pyk2, tensin and filamins."].
- The SH3 domain binds polyproline motifs (PKD1, ADAM15) [PMID:20856870 "Here, we report that the C-terminus of PC-1 contains at least one polyproline domain that is able to mediate an interaction with Src-homology 3 domains (SH3)."].

## Transition zone
- [PMID:16885411 "Here, it is shown that nephrocystin specifically localizes at the ciliary base to the transition zone of renal and respiratory cilia and to photoreceptor connecting cilia."]
- Not needed for cilia formation [PMID:16885411 "Cilia formation is not altered in primary nephrocystin-deficient respiratory cells"]; [PMID:21565611 "normal numbers of cilia were observed in cells depleted of Nphp1, Nphp4, Nphp8"].
- NPHP1-4-8 module [PMID:21565611 "The first module consists of NPHP1, NPHP4 and NPHP8, localized to cell-cell contacts and to the ciliary transition zone."]; NPHP4 is the bridge [PMID:21565611 "We find that NPHP4 directly binds both NPHP1 and NPHP8 in vitro, and can bridge the interaction between NPHP1 and NPHP8"].
- Hierarchy: NPHP1 depends on NPHP4 [PMID:26982032 "NPHP-1 requires NPHP-4 for assembly at the TZ"]; [PMID:21357692 "NPHP4 acts upstream of NPHP1 and regulates the localization of NPHP1 at the ciliary base."]. NPHP1 does not depend on the MKS module [PMID:25869670 "neither Rpgrip1l nor Nphp1 require Tmem231 or B9d1 to localize to the TZ"].
- Redundancy with the MKS module [PMID:28401750 "However, combining the disruption of a MKS complex component with the disruption of NPHP1 or NPHP4 severely disrupted ciliogenesis, and ciliary functions"].

## Junctions
- [PMID:19755384 "nephrocystins-1 and -4 are required for the proper timing of tight junctional establishment"].

## Curation decisions (51 rows)
- 22 protein binding rows: 4 MODIFY to GO:0070064 proline-rich region binding (SH3-polyproline interactions with PKD1 and ADAM15); the rest REMOVE (uninformative; NPHP4 interaction covered by NPHP complex).
- Structural molecule activity NAS: MODIFY to protein-macromolecule adaptor activity (the paper's own "docking protein" claim).
- Visual behavior NAS (cites the NPHP4 paper): REMOVE. Signal transduction, membrane, cell-cell adhesion NAS: MARK_AS_OVER_ANNOTATED.
- Junction, cytoplasm, development (retina/spermatid) rows: KEEP_AS_NON_CORE.
- No NEW. NPHP1 is downstream in the NPHP module, and direct evidence that it builds TZ structure is lacking, so I did not add GO:1905349.

## HPA cilium atlas vs module role
- HPA (member_evidence.md): no cilium/centrosome call; "not in HPA" (no subcellular data). The Hansen et al. 2025 atlas [PMID:41005307 "Our analysis identified the subciliary locations of 715 proteins across three cell lines, examining 128,156 individual cilia."] gives no information on NPHP1.
- Module role: NPHP module component; module function "transition zone scaffold", process ciliary transition zone assembly. The literature supports NPHP module membership and TZ localization. It does not show that NPHP1 is a scaffold: within the module NPHP4 is the bridging scaffold and RPGRIP1L/MKS5 the foundational assembly factor, with NPHP1 recruited downstream. NPHP1 is also dispensable for ciliogenesis on its own. I therefore **argue against assigning the scaffold/TZ-assembly role to NPHP1 individually**: core_functions give it NPHP-complex membership, TZ location and protein localization to TZ, but not GO:1905349. At the complex level the module statement is fine.
