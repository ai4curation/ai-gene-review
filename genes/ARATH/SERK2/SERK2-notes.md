# SERK2 review notes

## 2026-10-28 initial review

- fetch-gene resolved Q9XIC7 (SERK2_ARATH, TAIR AT1G34210, GeneID 840320); 31 GOA rows.
- Literature synthesis written by hand in SERK2-deep-research-manual.md (no deep-research API keys).
- Full text read: PMID:22253607 (Gou et al. 2012), PMID:16284306 (Colcombet et al. 2005),
  PMID:26320950 (Meng et al. 2015), PMID:27920157 (Li et al. 2017, EMS1 co-receptor).
  Abstract only: PMID:16284305, PMID:18667726, PMID:19616764, PMID:26308901, PMID:27229311,
  PMID:27449136, PMID:19105183.
- Key points:
  - SERK2 is a kinase-active LRR co-receptor; its in vivo role is mainly redundant with SERK1 in
    EMS1/TPD1-dependent tapetum specification [PMID:27920157 "Our results suggest that SERK1 and SERK2 may
    function redundantly as coreceptors of EMS1 during anther development in Arabidopsis."]
    and with BAK1 in ERECTA-family stomatal patterning [PMID:26320950].
  - BR signalling: SERK2 can act when overexpressed but is largely dispensable
    [PMID:22253607 "These results indicate that serk2 has an undetectable effect on BR signaling in
    Arabidopsis seedlings"]. BR rows kept as non-core.
- Decisions:
  - Generic kinase IEA rows MODIFY to GO:0004675 (verified is_a descendant of GO:0004672 and
    GO:0004674 via OLS).
  - GO:0007178 accepted as the umbrella process for its multiple peptide-receptor co-receptor roles
    (BR signalling is not under GO:0007178 in the current ontology; checked with OLS).
  - Nucleus HDA (PMID:28887381, membrane protein correlation profiling) marked over-annotated: no
    SERK2-specific nuclear evidence; SERK2 is a type I plasma membrane protein.
  - Bare protein binding rows removed per policy.
- No NEW terms proposed. Stomatal patterning (GO:0010375) and vascular / PSK / RGF signalling roles
  are supported by higher-order mutant genetics and structures, but are not proposed as NEW
  annotations here; candidates for a curator decision.
