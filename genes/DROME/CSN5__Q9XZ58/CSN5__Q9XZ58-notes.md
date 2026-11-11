# CSN5 (Q9XZ58) review notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 file or prediction-evidence folder was opened or used.

**Identity and folder.** Q9XZ58 is the reviewed Swiss-Prot entry for FlyBase CSN5 (FBgn0027053, CG14884), the canonical CSN5-PA product (327 aa). `genes/DROME/CSN5` is keyed to the PB isoform entry A0A0B4KHM2, so this review sits in `genes/DROME/CSN5__Q9XZ58`. It was fetched with `just fetch-gene DROME Q9XZ58 --alias CSN5__Q9XZ58`.

**Deep research.** `just deep-research-falcon DROME Q9XZ58 --alias CSN5__Q9XZ58 --fallback perplexity-lite` failed. Falcon failed with "Exception: Failed to authenticate", and the perplexity-lite fallback failed with HTTP 401 insufficient_quota. No deep-research file was written. The review rests on the cached publications (all abstract-only except PMID:17251548, which is full text) and on the UniProt record.

**Evolutionary grounding.** `CSN5__Q9XZ58-bioinformatics/check_csn5.py` (output in `results.txt`, summary in `RESULTS.md`) confirms the following:
- The JAMM ligands His135, His137 and Asp148 are intact (motif HSHPGYGCWLSGID).
- PANTHER 19.0 places Q9XZ58 in PTHR10410:SF6 (COP9 signalosome complex subunit 5), together with human COPS5, mouse Cops5, worm csn-5, S. pombe csn5, S. cerevisiae RRI1 and Dictyostelium csn5.
- Other JAMM proteins sit in other subfamilies: PSMD14 (SF43), RPN11 (SF5), BRCC3 (SF34) and EIF3H (SF3).

The CSN5-clade PAINT node PTN000045369 propagates COP9 signalosome, deNEDDylase activity, cytoplasm and regulation of cell cycle. Q9XZ58 is a donor to that node. The metal-dependent deubiquitinase IBA comes from a deeper node, PTN000045368, whose donors are mostly in other subfamilies.

**Experimentally established in Drosophila (usable as a transfer reference):**
- COP9 signalosome membership: co-IP and gel filtration [PMID:10531038 "have shown by co-immunoprecipitation and gel-filtration analysis that these proteins are components of the Drosophila COP9 signalosome"].
- Removal of NEDD8 from Cul1 in vivo [PMID:12737805 "we show that the CSN acts during Drosophila oogenesis to remove Nedd8 from Cullin1"], with JAMM dependence shown by mutagenesis [PMID:12183637 "Metal chelators and point mutations within JAMM abolished CSN-dependent cleavage of Nedd8 from Cul1"; UniProt MUTAGEN H135A/H137A/D148N].
- Cytoplasm (IDA). Nucleus is supported by UniProt (ECO:0000305) and by a nuclear-periphery IDA.
- Substrate-specific outcomes: Cyclin E degradation (PMID:12737805) and stabilization of Rbf1/Rbf2 against the proteasome (PMID:17251548).
- Developmental requirements (IMP): R-cell differentiation, the R-cell signal for lamina glial migration, female germline stem cell self-renewal, somatic support of the male germline, and larval hemocyte homeostasis.

**Inferred only (not experimentally shown in flies):** metal-dependent deubiquitinase activity (IBA from a deep node). It is marked as over-annotated.

**Key decisions.**
- Core: metal-dependent deNEDDylase activity (IDA), protein deneddylation (IMP), COP9 signalosome, cytoplasm and nucleus.
- peptidase activity (IEA) and deNEDDylase activity (IBA) are MODIFY to GO:0140758.
- regulation of protein neddylation (NAS, from a 1999 paper that predates the deneddylase discovery) is MODIFY to GO:0000338 protein deneddylation.
- The two oocyte axis-specification rows are MARK_AS_OVER_ANNOTATED. The phenotype is suppressed by mei-41 and mei-W68 [PMID:12397113 "the CSN5 phenotype is suppressed by mutations in mei-41 or by mutations in mei-W68"], so it is an indirect checkpoint effect.
- All 7 generic protein-binding rows are REMOVE (CSN subunit interactions are covered by the complex annotation; Trc8 interaction has no specific MF).
- Other developmental and regulatory rows are KEEP_AS_NON_CORE.
- No NEW annotations. Pleiotropic developmental phenotypes were not added as process participation.
