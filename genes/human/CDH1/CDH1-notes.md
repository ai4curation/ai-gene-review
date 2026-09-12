# CDH1 (E-cadherin) — curation notes

## 2026-06-22 — manual PubMed curation of IBA support

Applied the proven manual-PubMed support-finding workflow (asta deprecated, see issue #1599) to the
14 IBA annotations that lacked independent PMID/DOI support. Several already had a `supported_by`
entry pointing at the falcon deep-research file (`file:...`), which is why they were flagged
unsupported — I appended foundational primary PMIDs (verified verbatim against the fetched abstract).

Added independent PMID support to **8 of 14** IBA annotations:

| Term | GO | Reference |
|---|---|---|
| beta-catenin binding | GO:0008013 | PMID:7806582 (β-catenin interacts with E-cadherin) |
| catenin complex | GO:0016342 | PMID:2349235 (uvomorulin/E-cadherin associates with catenins α/β/γ) |
| cadherin binding | GO:0045296 | PMID:20190754 (classical-cadherin strand-swap homophilic binding) |
| cell-cell adhesion mediated by cadherin | GO:0044331 | PMID:3498123 (Nagafuchi/Takeichi 1987) |
| calcium-dependent cell-cell adhesion | GO:0016339 | PMID:3498123 ("Ca2+-dependent intercellular adhesion between epithelial cells") |
| adherens junction | GO:0005912 | PMID:7806582 (E-cadherin in adherens junctions of epithelia) |
| adherens junction organization | GO:0034332 | PMID:3498123 (anti-E-cadherin disperses compact cell colonies) |
| apical junction complex | GO:0043296 | PMID:23643492 (E-cadherin at the epithelial zonula adherens) |

**Left unsupported (6) — honest:**

- **GO:0007043 cell-cell junction assembly** — core E-cadherin function, but I did not locate a clean
  cached *primary* statement specifically about junction *assembly* in a quick search (Adams/Vasioukhin
  live-imaging papers would fit; not fetched). Distinct from the organization term above.
- **GO:0016477 cell migration** — real but context-dependent (E-cadherin suppresses single-cell
  invasion yet enables collective migration); a single IBA "cell migration" is too coarse to anchor
  cleanly to one primary paper.
- **GO:0000902 cell morphogenesis** — broad developmental term; better captured by specific
  morphogenesis processes than a general primary citation.
- **GO:0005737 cytoplasm** — E-cadherin is a plasma-membrane protein with a cytoplasmic *domain*;
  a blanket "cytoplasm" CC is arguably an over-annotation and was not given primary support.
- **GO:0007416 synapse assembly** — the synaptic classical cadherin is largely N-cadherin (CDH2);
  this looks like a phylogenetic over-propagation to CDH1 and was not supported.
- **GO:0016600 flotillin complex** — obscure CC; no clean primary support surfaced; likely
  over-propagated.

Note: unlike the LGALS3 asta run, CDH1's foundational literature (Nagafuchi/Takeichi 1987, the
Ozawa/Kemler catenin papers, Harrison 2010 structure) was trivially recovered by direct PubMed
search — again reinforcing that targeted manual search beats the retrieval-only provider.