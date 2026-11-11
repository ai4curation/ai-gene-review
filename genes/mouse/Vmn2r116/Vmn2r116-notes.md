# Vmn2r116 (V2Rp5, E9Q6I0) review notes

## 2026-10-20 session

### Deep research
- `just deep-research-falcon mouse Vmn2r116 --fallback perplexity-lite` failed: falcon returned
  "Edison API request failed: Failed to authenticate" (HTTP 403) and the perplexity-lite fallback
  also failed. No deep-research file exists; the review is built from the UniProt record and the
  cached primary literature below.

### Literature read
- PMID:20596023 (Haga et al. 2010, Nature) — abstract only in cache. Identifies V2Rp5 (= Vmn2r116)
  as the receptor for the male tear peptide ESP1 [PMID:20596023 "ESP1 is recognized by a specific
  vomeronasal receptor, V2Rp5"]; knockout abolishes neural and behavioural responses
  [PMID:20596023 "In V2Rp5-deficient mice, ESP1 induces neither neural activation nor sexual
  behaviour."]. Source of both MGI IGI annotations (with Esp1, MGI:3645915).
- PMID:23576433 (Yoshinaga et al. 2013, JBC) — full text. Direct, specific binding of ESP1 to the
  recombinant extracellular region (aa 19-584) of V2Rp5; not to ESP4; salt-sensitive, i.e.
  charge-charge driven [PMID:23576433 "These results indicate that ESP1 specifically binds to the
  extracellular region of V2Rp5."]. Homology model on mGluR1 places ESP1 in the VFT cleft.
- PMID:25073926 (Haga-Yamanaka et al. 2014, eLife) — about V1R receptors for female cues; cites the
  ESP1-V2rp5 pair as a single-receptor labelled line. Background only.

### Evolutionary placement
- UniProt: PANTHER PTHR24061 (calcium-sensing receptor-related, class C GPCR) subfamily
  PTHR24061:SF398 "VOMERONASAL 2, RECEPTOR 111-RELATED"; InterPro IPR004073 (V2R),
  CDD cd15283 7tmC_V2R_pheromone.
- GOA has two IBA rows (GPCR activity; plasma membrane, is_active_in) from PANTHER:PTN002373557, a
  deep class C node whose donors include CASR (P41180). So, contrary to the campaign brief, a PAINT
  node does cover this product, but only for family-wide class C GPCR properties. No PAINT node
  propagates any pheromone- or ligand-specific term; ligand identity (ESP1) is established only by
  experiments on this protein itself.
- ESP1 specificity is a property of this receptor (single receptor out of hundreds; ESP4 does not
  bind). It should not be transferred to other SF398 members or to other subfamilies (e.g. SF413,
  Vmn2r66-79).

### Decisions
- GO:0016503 pheromone receptor activity (IGI): ACCEPT, core.
- GO:0004930 GPCR activity (IBA, IEA): MODIFY to GO:0016503 (is_a descendant, already carried).
- GO:0005886 plasma membrane: ACCEPT. GO:0016020 membrane: MODIFY -> GO:0005886.
- GO:0007186 GPCR signaling pathway (IEA): KEEP_AS_NON_CORE (true; generic).
- GO:0045925 positive regulation of female receptivity (IGI, acts_upstream_of_or_within):
  KEEP_AS_NON_CORE — organismal behavioural outcome downstream of pheromone detection.
- Considered NEW GO:0043695 detection of pheromone. Comparator check: QuickGO returns 0
  annotations to this term in mouse, rat or human (vomeronasal receptors carry the MF
  GO:0016503 instead). Not added; raised as a question.
