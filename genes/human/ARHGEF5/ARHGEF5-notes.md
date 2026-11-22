# ARHGEF5 (TIM / ephexin3) notes

## Biology
- RhoA GEF acting upstream of RhoA/ROCK: stress fibres, MLC phosphorylation, transformation [PMID:15601624].
- Recombinant overexpression in COS-7/NIH-3T3 produced ruffles and filopodia [PMID:14662653].
- Src-induced podosome formation: Arhgef5 binds the Src SH3 domain, is tyrosine-phosphorylated by Src, and activates RhoA [PMID:21525037].
- The ODAM C-terminus binds the ARHGEF5 SH3 domain in an integrin-ODAM-ARHGEF5-RhoA pathway in junctional epithelium [PMID:25911094].
- Reactome RHOA/B/C GTPase-cycle entries list ARHGEF5 (reactome/R-HSA-8980691, -9013023, -9013109).

## GOA calls
- **Protein binding (35 rows) → all REMOVE** under the generic-binding policy:
  - The RHOA IPI rows cite PMID:12006984 (Dbs/intersectin structures) and PMID:34591642 (HNSCC network); neither mentions ARHGEF5 in the accessible text.
  - GRB2 recurs in five interactome studies without interface mapping.
  - 14-3-3 sigma (SFN) comes from proteomics.
- **GTP binding (TAS, cloning paper) → REMOVE:** a GEF, not a GTP-binding protein.
- **ACCEPT:** GEF activity (all rows; substrate RHOA), positive regulation of Rho signal transduction, regulation of actin cytoskeleton organization, cytoplasm/cytosol.
- **IBA nodes:** PTN002656129 (ephexin) and PTN002656143 (ARHGEF5, seeded by ARHGEF5 itself).
- **Non-core:** nucleus/nucleoplasm, plasma membrane and cell periphery, podosome, general signalling parents.
- Review round (PR #4171):
  - GO:0043087 → MODIFY to GO:0090630 activation of GTPase activity (exchange-defined; follows the ARHGEF16 precedent).
  - Wang et al. 2009 [PMID:19713215] is now cited:
    - Mouse Arhgef5 substrate panel (RhoA/RhoB strong, RhoC/RhoG weak, not Rac1/RhoQ/RhoD/RhoV). This is the source of UniProt's by-similarity panel and Reactome's RHOB/RHOC entries.
    - Gbetagamma binding and stimulation.
    - Immature dendritic cell migration in knockout mice.
  - SH3 autoinhibition relieved by SH3-binding peptides [PMID:25645980]; Src-PI3K ternary complex [PMID:21525037].
  - GO:0005085 is the only GEF term because GO:0005089 was merged into it.
  - No podosome assembly process row was added. Podosome evidence is from Arhgef5 RNAi in Src-transformed cells; the podosome location row is kept non-core.
