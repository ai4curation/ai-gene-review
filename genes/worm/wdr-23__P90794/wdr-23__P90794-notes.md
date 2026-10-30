# wdr-23 (P90794, WDR-23A canonical; P90794-2 = WDR-23B) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: canonical Swiss-Prot product of C. elegans wdr-23 (WBGene00008419, D2030.9). The
benchmark product S6FN32 (genes/worm/wdr-23) is an N-terminally shortened gene model of the
same gene and is reviewed separately. No ProtNLM2 file or prediction-evidence folder was opened.

### Provenance / process

- `just fetch-gene worm P90794 --alias wdr-23__P90794`: 16 GOA rows seeded.
- `just deep-research-falcon ... --fallback perplexity-lite` FAILED: falcon "Failed to
  authenticate"; perplexity-lite HTTP 401 (insufficient quota). No deep-research file exists for
  this folder. The review is built from primary literature cached in `publications/`.
- Literature found by PubMed search `wdr-23[tiab] AND elegans` (23 hits) and `WDR23[ti]`.
  Cached: PMID:23555279, 31409866, 28453520, 26056713, 30166349, 24912676, 23836880.
- **Two Choe-lab MCB papers are retracted** (PubMed retraction notices PMID:26282131 and
  26282130): PMID:24912676 (direct WDR-23/SKN-1 interaction blocks DNA binding) and
  PMID:23836880 (SKN-1/WDR-23 negative-feedback loop). They are listed as references with
  `is_invalid: true` and are not used as support. PMID:19273594 (Choe et al. 2009, the GOA
  source for most rows) is not retracted (PubMed pubtype Journal Article); but its cached copy
  is abstract-only.

### Evolutionary grounding

- PANTHER PTHR19847:SF7 (DDB1- and CUL4-associated factor 11), same subfamily as human DCAF11
  (Q8TEB1). PAINT node PTN000457302 (taxon Eukaryota) carries two IBDs:
  GO:0080008 Cul4-RING E3 ubiquitin ligase complex (seeded by human DCAF11) and GO:0043161
  proteasome-mediated ubiquitin-dependent protein catabolic process (seeded by wdr-23 itself).
  No MF IBD was placed; that is read as no experimental MF on donors at the time (2017), not
  a rejection.
- `wdr-23__P90794-bioinformatics/RESULTS.md`: four WDxR motifs; R342 and R389 (mutated in the
  WDR-23(DxR) allele of Staab et al. 2013) are both WDxR arginines.

### What is experimentally established in C. elegans

- Interaction with CUL-4/DDB-1 and repression of SKN-1 protein level, nuclear accumulation and
  activity [PMID:19273594 "SKN-1 protein levels, nuclear accumulation, and activity are repressed by
  the WD40 repeat protein WDR-23, which interacts with the CUL-4/DDB-1 ubiquitin ligase to
  presumably target the transcription factor for proteasomal degradation"]. Note "presumably":
  direct ubiquitination of SKN-1 by CRL4-WDR-23 is not shown in the abstract.
- DDB-1 docking motifs are required in vivo [PMID:23555279 "expression of WDR-23(DxR) driven by
  the endogenous wdr-23 promoter fragment failed to restore wild type aldicarb responsiveness to
  wdr-23 mutants"].
- Isoform localization: WDR-23A cytoplasmic/outer mitochondrial membrane, WDR-23B nuclear
  [PMID:23555279 "WDR-23b-GFP was entirely nuclear, whereas WDR-23a-GFP adopted a ring-like
  pattern of fluorescence in the intestinal cytoplasm"; PMID:31409866 "WDR-23A in the cytoplasm
  and WDR-23B in the nucleus"]. Both isoforms rescue wdr-23 mutant neuromuscular phenotypes
  (Staab), but only WDR-23B suppresses stress resistance / gst-4 induction (Spatola).
- GEN-1 (Holliday junction resolvase) is a second substrate: Y2H, co-IP in HEK293T and in vitro
  ubiquitin modification with immunoprecipitated WDR-23 isoforms [PMID:31409866].
- Organismal phenotypes of loss (all SKN-1 dependent per PMID:26056713): increased stress
  resistance, lifespan extension, reduced growth and fecundity, Mn resistance of DA neurons
  (PMID:23721876), iodide resistance (PMID:30166349).

### What is inferred, not shown in worm

- Polyubiquitination of SKN-1 by CRL4(WDR-23) in vivo. The proteasomal turnover model is
  supported by protein-level and genetic data plus the conserved human mechanism
  (PMID:28453520: human WDR23 binds the NRF2 DIDLID motif and regulates its stability via
  DDB1-CUL4).

### Annotation decisions (summary)

- Core: GO:0080008 (ACCEPT), GO:0043161 (ACCEPT, IBA + IMP), the three GO:0005515 rows
  MODIFY -> GO:1990756 ubiquitin-like ligase-substrate adaptor activity (DDB-1 and SKN-1
  partners), GO:0061629 (ACCEPT; SKN-1 is the substrate), GO:0005634 nucleus (ACCEPT; WDR-23B).
- Non-core regulatory/organismal: GO:0000122, GO:0080135, GO:1905803, GO:0008340 x2,
  GO:0040018 (KEEP_AS_NON_CORE; consequences of SKN-1 repression).
- GO:1990748 cellular detoxification IGI: MARK_AS_OVER_ANNOTATED (WDR-23 represses the
  detoxification response; it does not perform detoxification).
- NEW: GO:0005741 mitochondrial outer membrane and GO:0005737 cytoplasm for isoform a
  (P90794-1), from Staab 2013 / Spatola 2019. UniProt's DR GO lines show WormBase already has
  IDA rows for these; they were not in the fetched GOA set for P90794 (likely isoform-keyed).
