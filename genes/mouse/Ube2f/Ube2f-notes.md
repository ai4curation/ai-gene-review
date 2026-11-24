# Ube2f (mouse, Q9CY34) review notes

## 2026-10-20 session

### Deep research
- `just deep-research-falcon mouse Ube2f --fallback perplexity-lite` failed: Edison (falcon)
  returned "Failed to authenticate" (403) and the perplexity-lite fallback also failed
  (JWT token required). No deep-research file exists; the review is built from the cached
  primary literature and the UniProt record.
- Re-fetched PMID:19250909 with `cache_publication(force=True)`; the cache now holds the
  PMC full text (it was abstract-only before), which is essential because the mouse
  experiments are in the body text.

### Evolutionary grounding
- PANTHER: UBE2F subfamily `PTHR24068:SF129` "NEDD8-CONJUGATING ENZYME UBE2F" in the local
  panther.obo; the UniProt cross-reference uses the older family id PTHR24067 (release skew,
  discussed in `interpro/panther/PTHR24068/PTHR24068-review.yaml`).
- PAINT node `PTN000630367` (NEDD8-conjugating clade, UBC12/UBE2M + UBE2F) carries IBD
  GO:0019788 NEDD8 transferase activity and GO:0045116 protein neddylation, seeded by
  human UBE2M (P61081), human UBE2F (Q969M7), mouse Ube2f (MGI:1915171 - this gene), yeast
  UBC12 and a fly member. The same node carries IRDs that remove GO:0061631 ubiquitin
  conjugating enzyme activity and GO:0000209 protein polyubiquitination inherited from the
  ubiquitin-E2 ancestor: a deliberate curator decision that this clade conjugates NEDD8,
  not ubiquitin. Cytosol (GO:0005829) IBD at the same node is seeded by a trypanosome
  member (Q57TW2).
- The mouse protein is 185 aa, UBC core 32-185, catalytic Cys116 (UniProt ACT_SITE), N-terminal
  UBA3-binding region 1-29. Huang et al. state human UBE2F is 97% identical to mouse
  [PMID:19250909 "Human UBE2F and UBE2M, which have 97% and 100% identical protein sequences as their mouse counterparts"].

### What is experimental IN MOUSE
- PMID:19250909 (Huang et al. 2009, Mol Cell; full text). In vitro biochemistry (E1 charging,
  thioester formation, 32P-NEDD8 transfer to CUL5 with RBX2) used human UBE2F. The mouse
  experiments: shRNA knockdown of Ube2f in NIH 3T3 cells (and primary MEFs, data not shown)
  "virtually eliminated the presence of Nedd8ylated Cul5, and had no effect on the levels of
  Nedd8-modified Cullins 1–4"; rescued by human UBE2F-HF but not by UBE2M-HF. Ube2f
  knockdown cells "appeared normal" (no proliferation/apoptosis defect), unlike Ube2m.
  Rbx1/Rbx2 double knockdowns in NIH 3T3 show UBE2F pairs with RBX2 for Cul5.
  => Mouse-experimental: protein (cullin-5) neddylation, E2 required for Cul5 neddylation.
  The MF (NEDD8 E2 activity) is inferred for the mouse protein from human biochemistry plus
  in-cell rescue; EXP/IMP MF rows are reasonable but rest partly on the human protein.
- PMID:38574733 (Chang et al. 2024, Dev Cell; abstract only). Mouse KrasG12D PDAC model:
  Ube2f deletion suppresses cerulein pancreatitis/ADM/PanIN; mechanism via loss of
  CRL5-Asb11-mediated Diras2 ubiquitylation. MGI made an IDA for NEDD8 transferase activity
  and UniProt cites it for CUL5 neddylation with RBX2. Full text not read; defer to curator.
  The tumour phenotypes are organismal and are NOT annotated as processes.

### Inferred only (human Q969M7)
- Interaction with DCUN1D1-5 via acetylated N-terminus (PMID:23201271, human), CUL9
  neddylation (by similarity) - not transferred as annotations here.
- HIV Vif hijacking of CRL5: UBE2F is required for Vif-mediated APOBEC3G degradation
  [PMID:23300442 "conjugation of NEDD8 to Cullin-5 by the NEDD8-conjugating enzyme UBE2F is required for HIV Vif-mediated degradation of the host restriction factor APOBEC3G (A3G)"].
  This is the likely origin of the ISO rows for innate immune response / defense response to
  virus; it is a pro-viral role (the virus uses UBE2F to defeat a restriction factor), and
  the current human Q969M7 GOA set (QuickGO, 2026-10-20) no longer carries
  GO:0045087, GO:0051607 or GO:0043161, so these ISO rows are stale projections.

### Decisions
- MF: GO:0061654 NEDD8 conjugating enzyme activity (E2 thioester transthiolation) ACCEPT;
  GO:0019788 NEDD8 transferase activity ACCEPT too - it is broader but also covers the final
  NEDD8 transfer from the E2 thioester to the cullin lysine (isopeptide), which
  GO:0061654's thioester-to-thioester definition does not.
- BP: protein neddylation ACCEPT (mouse IMP is the strongest evidence).
- innate immune response / defense response to virus ISO: REMOVE.
- proteasome-mediated ubiquitin-dependent protein catabolic process ISO (acts upstream):
  KEEP_AS_NON_CORE - neddylation activates CRL5, which ubiquitylates substrates such as
  Diras2 for degradation; upstream, indirect.
