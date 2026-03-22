# BioReason-Pro RL Review: HSP104 (yeast)

Source: HSP104-deep-research-bioreason-rl.md

- **Correctness**: 4/5
- **Completeness**: 3/5

## Analysis

BioReason delivers a strong structural and mechanistic analysis of HSP104 as an AAA+ ClpB-type disaggregase. The domain architecture dissection is thorough and accurate, correctly identifying the Clp N-terminal domain, tandem AAA+ ATPase modules, lid domain, and C-terminal assembly region.

### What was right

- Excellent domain architecture analysis identifying all key AAA+ modules
- Correct identification as a hexameric ring-forming ATPase disaggregase (not a protease)
- Accurate molecular function: ATP binding, ATPase activity, unfolded protein binding
- Correct biological process: protein folding/quality control
- Correct localization to cytoplasm
- Correct identification of Hsp70/Hsp40 cooperation for substrate refolding
- Appropriately rejected the UniProt "probable ATP-dependent non-specific protease" summary, correctly arguing the architecture indicates chaperone/unfoldase activity rather than proteolysis

### What was wrong or missing

| Aspect | BioReason Prediction | Curated Review |
|--------|---------------------|----------------|
| **Core MF** | ATPase activity + unfolded protein binding | GO:0140545 ATP-dependent protein disaggregase activity (the specific term) |
| **Thermotolerance** | Not mentioned | Cellular heat acclimation (GO:0070370) -- the defining phenotype |
| **Prion biology** | Not mentioned | Prion fibril fragmentation and propagation of [PSI+], [URE3], [PIN+] |
| **Stress granules** | Not mentioned | Stress granule disassembly during heat recovery (PMID:24291094) |
| **Nuclear localization** | Not mentioned | Shuttles between cytoplasm and nucleus (PMID:10467108) |
| **TA protein targeting** | Not mentioned | Role in TRC complex for tail-anchored protein targeting (PMID:20850366) |

### Failure modes

1. **Missing the defining biological phenotype**: HSP104 was originally identified through its essential role in induced thermotolerance (PMID:2188365). BioReason discusses "stress" generically but never identifies heat acclimation as the core biological function.

2. **Missing specific disaggregase term**: The curated review correctly proposes replacing GO:0051082 (unfolded protein binding) with GO:0140545 (ATP-dependent protein disaggregase activity) as the specific MF term. BioReason describes the disaggregation mechanism accurately but stops at generic terms.

3. **Missing prion biology**: One of HSP104's most distinctive and biologically significant roles is in yeast prion propagation -- it fragments prion fibrils into transmissible seeds. This is entirely absent from the BioReason analysis. This cannot be predicted from domain architecture alone, but represents a major gap in biological completeness.

4. **Missing stress granule disassembly**: HSP104 drives disassembly of heat stress granules and restoration of translation during recovery. Not captured.

5. **Protein folding in ER**: BioReason includes GO:0034975 (protein folding in endoplasmic reticulum) in its GO term list. The curated review marks organelle lumen localization as over-annotated since HSP104 is cytosolic/nuclear and any ER effects are indirect.

6. **Overinclusion of generic terms**: The BioReason GO list includes many extremely general terms (GO:0009987 cellular process, GO:0008152 metabolic process, etc.) that add no information.
