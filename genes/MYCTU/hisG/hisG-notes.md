# hisG (Rv2121c) - Mycobacterium tuberculosis H37Rv, P9WMN1 (HIS1_MYCTU)

## Provenance

- Deep research providers were unavailable for this session (no API keys); no
  `*-deep-research-<provider>.md` was generated. Sources: cached GOA references (PMID:12511575
  abstract only; PMID:18778048 full text; PMID:14532352 abstract only), plus kinetic papers found by a
  PubMed esearch ("ATP phosphoribosyltransferase" AND tuberculosis, 11 hits) and cached with
  fetch-pmid: PMID:22989207 (Pedreno et al. 2012, full text), PMID:28872824 (Moggre et al. 2017),
  PMID:28392260 (hybrid MS of histidine feedback).
- `just paint-losses MYCTU hisG`: no IRD/IKR on the lineage.

## Key evidence

- [PMID:12511575 "The N-1-(5'-phosphoribosyl)-ATP transferase catalyzes the first step of the
  histidine biosynthetic pathway and is regulated by a feedback mechanism by the product histidine."]
- [PMID:12511575 "The active enzyme exists primarily as a dimer, and the histidine-inhibited form is a
  hexamer."] versus [PMID:22989207 "MtATP-phosphoribosyltransferase is a hexamer in solution, in the
  presence or absence of l-histidine."] - oligomeric state is disputed; both are self-association.
- [PMID:12511575 "The inhibitor AMP binds in the active site cavity formed between the two catalytic
  domains."]
- [PMID:22989207 "agent EDTA, indicating that Mg2+ is essential for activity"]
- [PMID:18778048 "Inhibition activity was determined using an assay that followed the production of
  PR-ATP spectrophotometrically."]
- Long-form HisG (HAMAP MF_00079 HisG_Long) with C-terminal histidine allosteric domain.

## Judgement calls

- Plasma membrane HDA (PMID:14532352): membrane-fraction proteomics of a soluble, cytoplasmic,
  oligomeric enzyme with no TM segment; marked over-annotated rather than UNDECIDED (other MYCTU
  reviews left this row UNDECIDED).
- Bare protein binding IPI (self, P9WMN1) -> MODIFY to identical protein binding.
- No GO term for L-histidine (allosteric effector) binding was found in OLS; not proposed.
