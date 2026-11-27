# Wdr82 (Q9VLN1, FBgn0032030, CG17293) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: Wdr82 is reviewed as the experimentally characterised reference for its fly
paralog CG3515 (Q9VQD1). No ProtNLM2 output was opened or used.

### Provenance / process
- `just fetch-gene DROME Wdr82` created uniprot, goa (15 rows) and the review stub.
- `just deep-research-falcon DROME Wdr82 --fallback perplexity-lite` FAILED: the
  Edison API returned `403 Forbidden` at `/auth/login`, and the perplexity-lite fallback
  also failed. No deep-research file exists; the review is built from the cached primary
  literature below, all read directly.
- Cached: PMID:21694722 (abstract only), PMID:21875999 (full text), PMID:26577379
  (full text), PMID:39417277 (full text), PMID:23295261 (full text, fetched this session),
  PMID:18838538 (human WDR82, abstract only), PMID:15024081 (yeast Swd2, full text).

### Evolutionary grounding
- UniProt: `PANTHER; PTHR19861:SF0; WD REPEAT-CONTAINING PROTEIN 82` and InterPro
  IPR037867 Swd2/WDR82; "Belongs to the WD repeat SWD2 family". The same subfamily
  contains human WDR82 (Q6UXN9), mouse Wdr82, yeast Swd2, S. pombe Swd2 and fly CG3515.
- PAINT node PTN000458398 propagates only two terms to this clade: Set1C/COMPASS complex
  (GO:0048188; donors include FB:FBgn0032030 = this gene, plus SGD, PomBase, human,
  dictyBase) and chromatin binding (GO:0003682; donor MGI:1924555). PAINT did NOT
  propagate transcription-termination, RNA-surveillance or methyltransferase terms to
  the node; treat that as a deliberate decision, so those functions in fly rest on the
  fly experiments only.
- Wdr82 itself is an experimental donor for the Set1C IBA, so its own appearance in
  WITH/FROM is expected, not circular.

### Experimental findings in Drosophila (this gene)
- Set1/COMPASS membership: FLAG-Wdr82 MudPIT from S2 nuclear extracts recovers dSet1,
  dCXXC1, dDpy30, dRbbp5, Ash2 and Wds [PMID:21875999 "MudPIT analysis of dWdr82-FLAG
  eluate showed the presence of all the homologous components of yeast COMPASS and human
  COMPASS, namely, dSet1, dCXXC1, dDpy30, dRbbp5, Ash2, and Wds"]. Purified complexes
  methylate H3K4 in vitro [PMID:21875999 "all three complexes, like their mammalian
  counterparts, were capable of implementing methylation of H3K4"].
- Wdr82 RNAi reduces H3K4me3 but not H3K4me2 [PMID:21875999 "we observed a significant
  reduction only in the levels of H3K4 trimethylation, but not of dimethylation"].
- Ardehali 2011 (abstract only in cache) identified Set1 as the major H3K4me3
  methyltransferase in a conserved complex; UniProt credits it with Wdr82 identification
  in the SET1 complex and nuclear localisation (ECO:0000269|PubMed:21694722).
- Heart RNAi (Hand-Gal4) causes eclosion lethality and cardiac structural/functional
  defects and reduced H3K4me2 in cardiomyocyte nuclei [PMID:39417277 "Wdr82-RNAi did not
  change H3K4me1 levels, but significantly reduced H3K4me2"]. Note: tissue and readout
  differ from Mohan 2011 (H3K4me3 only). The heart phenotype is a pleiotropic
  consequence of losing a general Set1C subunit, not a heart-specific activity.
- Su(s)-Wdr82: Wdr82 co-purifies with Su(s) (reciprocal pulldowns) and, like Su(s),
  blocks Pol II elongation through Hsp70-alpha-beta repeat elements and down-regulates
  their unstable RNAs [PMID:26577379 "These results demonstrate that Su(s) and Wdr82 block
  elongation into the downstream region of Hsp70-αβ."]. Authors note it is unclear
  whether the complex acts on termination, RNA degradation or both.
- ChIP-MS: Wdr82 pulldowns recover MSL complex components [PMID:23295261 "we observed
  recovery of all MSL components and JIL-1 with both Wdr82 and CG4747"]. Interaction
  only; no functional consequence for Wdr82 shown; no annotation proposed.

### Orthology-based context (not transferred unless also shown in fly)
- Human WDR82 is SET1A/B-specific and associates with chromatin in an H2Bub-dependent
  manner [PMID:18838538]. Yeast Swd2 has dual roles in termination and H3K4 methylation
  [PMID:15024081].

### Decisions
- MODIFY histone methyltransferase complex -> Set1C/COMPASS complex (descendant,
  already carried by the gene).
- REMOVE bare protein binding (Su(s)) per GO:0005515 policy; interaction is real.
- KEEP_AS_NON_CORE heart development (pleiotropic).
- No NEW annotations. A `contributes_to` H3K4 trimethyltransferase activity would be
  supportable from PMID:21875999 but neither FlyBase nor PAINT asserted it; raised as a
  suggested question rather than added.
- For CG3515 transfer: only Set1C/COMPASS membership and chromatin binding are
  PAINT-grounded subfamily properties; the Su(s)-termination role and H3K4me3 effect are
  fly-Wdr82 experimental findings and should not be assumed for the fast-evolving paralog.
