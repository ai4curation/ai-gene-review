# PARD3B (human, Q8TEW8) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: reviewed as the experimentally characterised relative (same PANTHER
subfamily PTHR16484:SF4) of donkey PARD3B (A0A9L0JEY6). No ProtNLM2 output was
consulted.

Deep research: `just deep-research-falcon human PARD3B --fallback perplexity-lite`
failed (Edison/falcon auth 403; perplexity-lite fallback timed out after 600 s).
No deep-research file exists; the review is built from cached primary literature
and the Swiss-Prot entry.

### Evolutionary grounding
- Q8TEW8 and mouse Q9CSB4 are both PTHR16484:SF4 (interpro/panther/PTHR16484/PTHR16484-entries.csv).
- All IBA rows come from PTN001046835, the PAR3 family root that also contains
  PARD3, Bazooka and PAR-3. Hence IBA terms reflect family-level functions;
  aPKC-dependent ones need care because PARD3B lost the FXR/KR aPKC-binding motifs
  [PMID:33565714 "In the case of vertebrate PARD3B, both the FXR and KR motifs are mutated"].

### Experimentally established in human
- Tight-junction localization [PMID:12459187 "Nevertheless PAR3beta, expressed intrinsically or extrinsically, localizes to the tight junctions"].
- No PAR6/aPKC binding [PMID:12459187 "PAR3beta is incapable of binding to any isotypes of PAR6 or aPKC"]; but Gao 2002 reports isoform-differential Par6 binding [PMID:12234671]; Caco-2 co-IP negative [PMID:34815476].
- INSC binding [PMID:16458856].
- 14-3-3 binding via pSer-746 [PMID:15721295 "Here we show that Par3beta as well as Par3alpha interacts with 14-3-3 proteins in a phosphorylation-dependent manner."].
- Required for single-lumen Caco-2 cyst formation [PMID:34815476].
- LKB1 binding mapped with full-length human Par3L constructs; CRC cells [PMID:24859006, PMID:27908725].

### Established in mouse only
- Mammary stem cell maintenance; LKB1 suppression rescue [PMID:24859006].
- Knockout tumours, aberrant spindles [PMID:41274508] — phenotypes, not annotated as process participation.

### Decisions
- All 32 GO:0005515 rows REMOVE per protein-binding policy (INSC interaction kept in prose).
- NEW: GO:0019901 protein kinase binding (LKB1); GO:0071889 14-3-3 protein binding.
- Did NOT propose protein kinase inhibitor activity / negative regulation of protein kinase
  activity: inhibition was inferred from cellular pAMPK only, and MGI annotated the mouse
  paper only as protein binding. Raised as a suggested question/experiment.
- GO:0008104 intracellular protein localization IBA marked over-annotated (aPKC-dependent family function).
- GO:0070161 anchoring junction MODIFY -> adherens junction.
