# MYCTU groEL2 review — 2026-11-07

GroEL2 (Cpn60.2) is the essential housekeeping chaperonin of Mycobacterium tuberculosis. It supports ATP-dependent protein folding with GroES, while purified lower oligomers can also suppress aggregation and partially refold substrates independently of ATP or GroES. Its assembly and ATPase activity depend strongly on solution conditions. Extracellular and surface-associated GroEL2 participates in macrophage adhesion, and a proteolytically cleaved form reaches host mitochondria and modulates apoptotic responses.

Evidence and limits

- [PMID:12198306] Purification and preliminary crystallography identify a Cpn60.2 dimer in the asymmetric unit. Access: abstract only .
- [PMID:14532352] Proteomics identifies proteins in an H37Rv membrane fraction; target-specific enrichment and topology cannot be verified from the abstract alone. Access: abstract only .
- [PMID:15528667] GroEL2 is more abundant during anaerobic adaptation of strain Harlingen; this does not establish an oxygen-sensing mechanism. Access: abstract only .
- [PMID:18227252] Mycobacterial GroEL1/GroEL2 enhance HspR renaturation with DnaK; the reconstituted process depends on ATP hydrolysis. Access: abstract only .
- [PMID:19470749] Capsule and surface assays identify Cpn60.2; recombinant competition and epitope masking support macrophage adhesion. Access: abstract only .
- [PMID:20633027] Cpn60.2 mediates CD43-dependent macrophage binding. Access: abstract only .
- [PMID:20925060] GroEL2 is used as a mycobacterial phosphoacceptor substrate in a kinase coexpression assay. Access: abstract only .
- [PMID:24830429] Hip1 cleaves GroEL2 and alters macrophage inflammatory responses; the cleaved protein is released extracellularly. Access: full text inspected (cached or externally accessed) .
- [PMID:28288970] Exported GroEL2 reaches host mitochondria; cleaved protein is enriched there and association with mortalin contributes to apoptosis inhibition. Access: full text inspected (cached or externally accessed) .
- [PMID:2892795] The mycobacterial 65-kDa antigen is induced by heat. Access: abstract only .
- [PMID:15327959] Purified mycobacterial lower oligomers show weak ATPase and partial substrate refolding that can occur without ATP or cochaperonin. Access: abstract only .
- [PMID:18227175] Genetic tests distinguish essential cpn60.2/cpn10 from dispensable cpn60.1. Access: abstract only .
- [PMID:22834700] Mtb and M. smegmatis Cpn60.2 complement E. coli GroEL with cognate or E. coli cochaperonin; nucleotide/kosmotrope conditions promote oligomerization and ATPase activity. Access: abstract only .

GO0044183 expressly includes binding a protein-containing complex to assist folding; GroES can therefore retain this function without being an autonomous ATPase. Core GroES activity is chaperone binding with contribution to ATP-dependent folding. No NEW annotations were introduced. Generic protein binding, where present, follows the explicit project removal policy; specific interactions remain documented. Differences from E. coli are not used to discard target-specific experiments.

All original source annotation payloads/order and raw files are preserved against the new-cage-member baseline. The PAINT lineage check found no IRD/IKR loss and is not a fresh reconstruction of ancestral node placement. A genuine Falcon research call failed HTTP403 authentication; logs are under `.cache/module-audit-logs/groel-20261107/new-cage-consultation/`. No provider-labelled report was fabricated.


## PR6164 review follow-up, 2026-11-07

Independently reconsidered review5809803940 using original PMID12198306, biochemical lower-oligomer evidence in PMID15327959, current GO definitions and full publisher PMID12837792 Methods/Table2. [Activity evidence](../../../analysis/module_audits/bacterial_groel_groes_chaperonin_folding/round1-activity-consultation/evidence.md) records the judgment. GroEL2 self-binding is refined to identical protein binding; its broad folding-chaperone row explicitly covers the non-ATP mode. E. coli GroES metal binding is marked over-annotated because DLS assembly effects and a proposed site do not establish direct target coordination, even with a valid ancestral source. This supersedes the earlier inference that the DLS response sufficiently justified KEEP_AS_NON_CORE. Neither high calcium alone nor short donor lists is used as a refutation. Original payloads and sources are preserved.
