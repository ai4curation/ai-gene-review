# CEP83 review notes

## 2026-10-03: sources and scope

- `just fetch-gene human CEP83` produced the GOA snapshot (26 rows) and UniProt record Q9Y592; `just fetch-gene-pmids human CEP83` cached the two GOA PMIDs (both abstract-only).
- Additional primary papers cached with `just fetch-pmid`: PMID:29789620 (DAP super-resolution architecture), PMID:31455668 (CEP83 is a TTBK2 substrate), PMID:32238932 (mouse Cep83 and centrosome anchoring), PMID:24882706 (CEP83 mutations in NPHP18).
- Deep research: `just deep-research-falcon human CEP83 --fallback perplexity-lite` timed out at 600 s; the rerun with `--timeout 2400` succeeded (`CEP83-deep-research-falcon.md`).

## Functional synthesis

- CEP83 (CCDC41) is one of five distal appendage (DAP) components and the root of their assembly hierarchy [PMID:23348840 "CEP83 recruits both SCLT1 and CEP89 to centrioles. Subsequent recruitment of FBF1 and CEP164 is independent of CEP89 but mediated by SCLT1."]
- Loss of CEP83 specifically blocks docking of the mother centriole to membranes, and undocked centrioles do not recruit TTBK2 or lose CP110 [PMID:23348840 "All five DAP components are essential for ciliogenesis; loss of CEP83 specifically blocks centriole-to-membrane docking."]
- Super-resolution places CEP83 at the root of the appendage blades [PMID:29789620 "CEP83, CEP89, SCLT1, and CEP164 form the backbone of pinwheel blades, with CEP83 confined at the root and CEP164 extending to the tip near the membrane-docking site."]
- CEP83 is needed for ciliary vesicle docking and interacts with CEP164; a minor pool co-localizes with IFT20 at the Golgi [PMID:23530209 "a pool of CCDC41 colocalizes with intraflagellar transport protein 20 (IFT20) subunit of the intraflagellar transport particle at the Golgi complex."] and [PMID:23530209 "depletion of CCDC41 or IFT20 inhibits ciliogenesis at the ciliary vesicle docking step"]
- CEP83 is a substrate of TTBK2 once TTBK2 has been recruited by CEP164 [PMID:31455668 "TTBK2-dependent CEP83 phosphorylation is important for early ciliogenesis steps, including ciliary vesicle docking and CP110 removal."]
- In mouse radial glia, CEP83-dependent appendages anchor the centrosome to the apical membrane [PMID:32238932 "Selective removal of centrosomal protein 83 (CEP83) eliminates these distal appendages and disrupts the anchorage of the centrosome to the apical membrane"]
- Disease: biallelic variants cause infantile nephronophthisis (NPHP18) with altered DAP composition in patient cells [PMID:24882706 "Fibroblasts and tubular renal cells from affected individuals showed an altered DAP composition and ciliary defects."]

- Deep research adds: CEP83 is itself recruited by a distal-centriole CEP90-MNR-OFD1 complex [file:human/CEP83/CEP83-deep-research-falcon.md "a distal-centriolar complex containing CEP90, MNR and OFD1 recruits CEP83 before the CEP83-dependent appendage hierarchy"], so it is the root of the appendage hierarchy, not the first protein at the centriole; the Kanie knockout preprint suggests CEP83 and SCLT1 are interdependent; TTBK2 phosphosites on CEP83 (S29, T292, T527, S698) regulate a step after scaffold assembly (Lo 2019); CEP83-knockout iPSC nephron progenitors ciliate poorly (Mansour 2022); and retinal dystrophy without childhood kidney disease has been reported (Veldman 2021). These extra papers were not cached or annotated.

## Annotation decisions

- Accept centriole, centrosome, ciliary transition fiber, cilium assembly and protein localization to centrosome rows.
- Golgi apparatus (IBA, IDA): keep as non-core (minor IFT20-associated pool).
- Establishment of centrosome localization (IBA from mouse): keep as non-core; anchoring is a consequence of appendage loss.
- Two bare protein binding rows (IFT20, CEP164): remove per policy.
- Seven Reactome cytosol TAS rows: keep as non-core (Reactome compartment convention for centrosomal reactions).
- NEW: structural molecule activity (GO:0005198), from the blade-backbone super-resolution data; used as the core MF. Note: GO:0097539 ciliary transition fiber is classified in GO as a protein-containing complex, so it is used as `in_complex` and centriole as the location.

## HPA cilium atlas vs module role

- Module (`modules/primary_cilium_life_cycle.yaml`, stage 1): "distal appendage root component".
- HPA v25 (member_evidence.md): Primary cilium (Uncertain); Primary cilium transition zone (Uncertain); main locations Golgi apparatus, primary cilium, transition zone, vesicles. No centrosome or basal body call. The HPA cilium atlas paper (PMID:41005307) is abstract-only in the cache and gives no gene-level detail.
- Comparison: the Golgi/vesicle signal agrees with the reported IFT20-associated Golgi pool, and a transition-zone-level signal is compatible with transition fibers at the ciliary base, but both calls are graded Uncertain and HPA does not resolve the distal appendage. The literature (several independent groups, super-resolution, EM, patient cells) robustly supports the module role, and core_functions are consistent with it. Minor refinements: CEP83 is downstream of the CEP90-MNR-OFD1 distal complex (which matches the C2CD3/OFD1 Reactome step), and CEP83-SCLT1 may be interdependent rather than strictly ordered. No substantive disagreement with the module.
