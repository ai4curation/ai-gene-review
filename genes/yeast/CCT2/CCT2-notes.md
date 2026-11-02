# CCT2 review notes

## 2026-10-01 current-GOA refresh

- Refreshed CCT2 with current UniProt/GOA. Live GOA now has 16 rows; the refresh added a current InterPro `GO:0005524` ATP binding row and a `PMID:21701561` ComplexPortal `GO:0005832` structural row, and it backfilled qualifiers and supporting entities on the rows still present in GOA.
- Current PTHR11353 retains the CCT/TRiC protein-folding IBA on PTN004253040 and CCT-beta complex membership at PTN000144135. The older `GO:0051082` IBA has disappeared from the local PAINT snapshot, consistent with replacing it by the more specific CCT/TRiC ATP-dependent foldase activity rather than keeping unfolded protein binding as a standalone molecular function.
- Searched PubMed/Web for 2025-2026 yeast `CCT2`/`Cct2`/`YIL142W` papers. PMID:42647820 reports heat-shock-induced, vacuole-dependent Cct2 turnover outside canonical macroautophagy or microautophagy ["heat stress induces the turnover of the aggrephagy receptor Cct2"; "mediated autonomously of canonical autophagy pathways"]. This is relevant to monomeric Cct2/aggrephagy biology but does not change the CCT/TRiC GOA row reviews because the cached abstract does not define the delivery mechanism or support a precise new Cct2 GO process.
