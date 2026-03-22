# BioReason-Pro RL Review: hsp-90 (C. elegans)

Source: hsp-90-deep-research-bioreason-rl.md

- **Correctness**: 4/5
- **Completeness**: 3/5

## Analysis

BioReason correctly identifies HSP-90 as a cytoplasmic ATP-dependent molecular chaperone with the canonical tripartite domain organization (N-terminal ATPase, middle client-regulatory domain, C-terminal dimerization platform). The core molecular function assignment of ATP binding, hydrolysis, and chaperone activity is accurate.

### What was right

| Aspect | BioReason claim | Curated review |
|--------|----------------|----------------|
| Domain architecture | N-terminal ATPase, middle domain, C-terminal dimerization | Confirmed |
| ATP hydrolysis | Core function driving conformational cycle | Accepted (PMID:19559711) |
| Cytoplasmic localization | Correctly inferred | Accepted; cytosol/perinuclear confirmed (PMID:12950278) |
| Co-chaperone interactions | Mentions Hsp70, CDC37, p23, Aha1 analogs | CDC-37, STI-1/Hop, AHA-1, PPH-5 confirmed |
| Protein folding | Core function | Accepted |

### What was wrong or imprecise

- BioReason uses the odd GO annotation `GO:0003824` (catalytic activity) as a "formal label for function" -- this is far too generic and shows confusion about GO annotation specificity.
- The GO:0006355 (regulation of transcription) is cited as the biological process label, which is bizarre for a chaperone. This appears to be a hallucinated or mismatched GO term assignment. The curated review correctly identifies protein folding (GO:0006457), cellular response to heat (GO:0034605), and protein stabilization (GO:0050821) as the relevant processes.
- No mention of the DAF-21 alias, which is the commonly used genetic name in C. elegans.

### Missing biology

- No mention of specific client proteins (myosin via UNC-45, DAF-11 guanylyl cyclase, kinases).
- No discussion of the essential role in larval development, dauer formation, or chemosensory behavior.
- Misses the transcellular chaperone signaling (TCS) function documented in PMID:29949773.
- Does not mention heat stress induction via PQM-1 or HSF-1/DAF-16 regulation.
- Plasma membrane/lipid raft association (PMID:21070894) is not discussed.
- No mention of germline-enriched expression pattern.

### Failure modes

- **Incorrect GO term assignment**: Assigning GO:0006355 (regulation of transcription) as the biological process is a significant error, likely a slot-filling artifact.
- **Generic function labels**: Using GO:0003824 (catalytic activity) as a primary function annotation is uninformative.
- **Missing organism-specific biology**: The analysis reads as a generic HSP90 textbook description rather than a C. elegans-specific review.
