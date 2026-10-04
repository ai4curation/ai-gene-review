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
