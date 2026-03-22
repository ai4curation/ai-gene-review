# BioReason-Pro RL Review: skn-1 (C. elegans)

Source: skn-1-deep-research-bioreason-rl.md

- **Correctness**: 4/5
- **Completeness**: 2/5

## Analysis

BioReason correctly identifies SKN-1 as a CNC-bZIP transcription factor with DNA-binding activity and nuclear localization. The domain analysis is sound, and the core molecular function assignment is accurate. However, the analysis is shallow and misses the rich biology that makes SKN-1 one of the most studied genes in C. elegans.

### What was right

| Aspect | BioReason claim | Curated review |
|--------|----------------|----------------|
| CNC-bZIP/Nrf2-like TF | Correctly identified family | Confirmed (Nrf1/Nrf2 ortholog) |
| DNA-binding TF activity | GO:0003700 | Accepted |
| Sequence-specific DNA binding | bZIP + N-terminal arm | Confirmed (PMID:9628487 crystal structure) |
| Nuclear localization | GO:0005634 | Accepted (stress-induced nuclear translocation) |
| Regulation of transcription | GO:0006355 | Accepted |
| Maf-type bZIP domain | Correct domain identification | Confirmed |

### Key error

- BioReason states SKN-1 "dimerizes via its Maf-type zipper." This is **incorrect** for SKN-1. Unlike mammalian Nrf2 which heterodimerizes with small Maf proteins, SKN-1 **binds DNA as a monomer** using a unique mechanism (bZIP-like basic region + N-terminal arm for minor groove contacts). This is a well-established feature from the crystal structure (PMID:9628487). The curated review explicitly notes this monomeric binding. BioReason has applied mammalian Nrf2 biology to a worm protein where it does not hold -- a classic fold-bias error.

### Missing biology

1. **Isoform-specific functions**: SKN-1 has three major isoforms with distinct roles:
   - SKN-1A: ER-associated, proteasome stress response
   - SKN-1B: ASI chemosensory neurons, dietary restriction/longevity
   - SKN-1C: Intestinal, Phase II detoxification
   BioReason mentions none of this.

2. **Oxidative stress response**: SKN-1 is the master regulator of oxidative stress responses and xenobiotic detoxification. Target genes include gst-4, gst-1, gcs-1. Not mentioned.

3. **Developmental role**: SKN-1 specifies mesendoderm fate during embryogenesis (pharynx and intestine development from ventral blastomeres). This essential developmental role is completely absent.

4. **Regulatory inputs**:
   - PMK-1/p38 MAPK phosphorylation (activation, PMID:16166371)
   - WDR-23/CUL4/DDB1 ubiquitin ligase (degradation)
   - Insulin/IGF-1 signaling via AKT kinases (inhibition)
   None mentioned.

5. **Cytoplasmic-to-nuclear translocation**: SKN-1 resides in cytoplasm basally and translocates to nucleus upon stress. BioReason only mentions nuclear residence.

6. **Mitochondrial localization**: SKN-1A localizes to mitochondria (PMID:23040073). Not mentioned.

### Failure modes

- **Fold-bias (dimerization claim)**: Applying the generic bZIP dimerization model to SKN-1, which is known to bind DNA as a monomer. This is a textbook example of family-level inference failing at the species level.
- **Generic description**: The analysis reads as "CNC-bZIP transcription factor" with no C. elegans-specific content. The dual stress-response and developmental roles that make SKN-1 distinctive are entirely absent.
