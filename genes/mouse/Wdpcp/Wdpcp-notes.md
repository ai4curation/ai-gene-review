# Wdpcp (mouse, Q8C456) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 output was consulted. This is the first review of the mouse gene; it is the experimental
reference ortholog for human WDPCP (O95876).

### Setup
- `just fetch-gene mouse Wdpcp` (54 GOA rows); `just fetch-gene-pmids` cached PMID:24302887, 27158779, 35427153 (all full text).
- Deep research FAILED: `just deep-research-falcon mouse Wdpcp --fallback perplexity-lite` — Edison API
  "Failed to authenticate" (403), and the perplexity-lite fallback also failed. Review is based on the
  cached full-text papers, UniProt, and PAINT data.

### Evolutionary grounding
- PANTHER PTHR13667:SF5 (same subfamily as human WDPCP and Xenopus Fritz Q32NR9).
- PAINT IBDs at PTN001007408 (taxon:6072): axonemal basal plate (seed MGI Wdpcp), nervous system
  development (fly fritz + mouse), cilium organization (mouse + Xenopus), establishment of protein
  localization (mouse). PAINT did not propagate PI binding, actin/migration or PCP terms; treated as a
  deliberate decision (those rest on mouse experimental rows only).
- ISS rows (GO_REF:0000024) come from Xenopus Fritz Q32NR9, same subfamily [PMID:20671153].

### Experimentally established in mouse
- Localization of endogenous Wdpcp to the ciliary transition zone and axoneme [PMID:24302887 "Wdpcp is
  localized to the ciliary axoneme and in a ring-like structure at the base of the cilia in IMCD3 cells"],
  independent of Mks1.
- Required for ciliogenesis and for Sept2/Nphp1/Mks1 at the transition zone [PMID:24302887 "These results
  show Wdpcp is required for recruitment of Mks1 and Nphp1 to the ciliary transition zone."].
- IFT88 unaffected [PMID:24302887 "Ift88 distribution in the ciliary axoneme and basal body was unchanged in
  WdpcpCys40 mutant MEFs"] — so intraciliary transport row marked over-annotated.
- Sept2 co-IP and Sept2 loss from actin; focal adhesion, ruffling, Golgi orientation, directional migration
  defects in MEFs [PMID:24302887].
- Recombinant mouse Wdpcp binds PIPs (PI(3)P > PI(5)P > PI(4)P) via last 60 residues [PMID:35427153].
- CPLANE (Intu/Fuz/Wdpcp) structure from mouse proteins [PMID:35427153]; IFT-A recruitment by CPLANE shown
  mainly in Xenopus with mouse IMCD3 proteomics [PMID:27158779].

### Decisions
- 2x protein binding REMOVE (policy; no septin-binding MF term in GO).
- Organ-level IMP/IGI rows (kidney, eye, palate, tongue, digit, gut, heart, respiratory, nervous system,
  Smo/Ptch1 epistasis) KEEP_AS_NON_CORE: downstream ciliopathy phenotypes.
- Podocyte cell migration UNDECIDED: not described in main text (possibly supplementary).
- NEW: ciliary transition zone (GO:0035869), IDA PMID:24302887. GO places axonemal basal plate under
  axoneme, not transition zone; the basal-plate rows were accepted in deference.
