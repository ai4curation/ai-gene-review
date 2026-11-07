# CCT2 review notes

## 2026-10-01 current-GOA refresh

- Refreshed CCT2 with current UniProt/GOA. Live GOA now has 16 rows; the refresh added a current InterPro `GO:0005524` ATP binding row and a `PMID:21701561` ComplexPortal `GO:0005832` structural row, and it backfilled qualifiers and supporting entities on the rows still present in GOA.
- Current PTHR11353 retains the CCT/TRiC protein-folding IBA on PTN004253040 and CCT-beta complex membership at PTN000144135. The older `GO:0051082` IBA has disappeared from the local PAINT snapshot, consistent with replacing it by the more specific CCT/TRiC ATP-dependent foldase activity rather than keeping unfolded protein binding as a standalone molecular function.
- Searched PubMed/Web for 2025-2026 yeast `CCT2`/`Cct2`/`YIL142W` papers. PMID:42647820 reports heat-shock-induced, vacuole-dependent Cct2 turnover outside canonical macroautophagy or microautophagy ["heat stress induces the turnover of the aggrephagy receptor Cct2"; "mediated autonomously of canonical autophagy pathways"]. This is relevant to monomeric Cct2/aggrephagy biology but does not change the CCT/TRiC GOA row reviews because the cached abstract does not define the delivery mechanism or support a precise new Cct2 GO process.

## 2026-10-01 IBA alignment refresh

- Rebased from `origin/main` and reran `just fetch-gene yeast CCT2 --force`;
  the current 16-row GOA import matched the review.
- Fetched current PTHR11353 PAINT; CCT2 still receives `GO:0006457` protein
  folding from `PTN004253040` and `GO:0005832` chaperonin-containing T-complex
  from the CCT2/beta-subunit node `PTN000144135`. Added structured
  `propagation_review` blocks that evaluate these PAINT nodes, not raw
  `WITH/FROM` donor counts.
- Rechecked 2025-2026 web search results and the cached 2026
  `PMID:42647820` abstract. The heat-shock Cct2 turnover finding is direct
  and useful context but still does not support a new canonical-autophagy
  process annotation for Cct2.
