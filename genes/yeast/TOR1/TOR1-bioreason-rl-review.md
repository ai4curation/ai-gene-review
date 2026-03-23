# BioReason-Pro RL Review: TOR1 (yeast)

Source: TOR1-deep-research-bioreason-rl.md

- **Correctness**: 4/5
- **Completeness**: 3/5

## Analysis

BioReason produces a strong analysis of TOR1, correctly identifying it as a PIKK-family serine/threonine kinase with HEAT/ARM repeats, FAT domain, and FRB domain. The reasoning from domain architecture to TOR signaling is sound and well-articulated. This is the best-performing gene in this set.

### What was right

| Aspect | BioReason Claim | Curated Review Agreement |
|--------|----------------|------------------------|
| Core MF: protein Ser/Thr kinase activity | GO:0004674 | Yes -- core function confirmed by IBA, IEA, IDA, EXP |
| Core MF: ATP binding | GO:0005524 | Yes -- accepted |
| Core BP: TOR signaling | GO:0031929 | Yes -- accepted (IEA, NAS) |
| Domain: HEAT/ARM scaffold | Correctly identified | Yes |
| Domain: FRB gate (FKBP12-rapamycin binding) | Correctly identified | Yes -- InterPro IPR009076 |
| Domain: FAT domain | Correctly identified | Yes |
| Nutrient and growth control | Correctly inferred | Yes -- regulation of cell growth (GO:0001558) accepted |
| Ribosome biogenesis connection | Mentioned in trace | Yes -- GO:0042254 accepted |
| Autophagy regulation | Mentioned in trace | Yes -- GO:0010507 / GO:0016242 accepted |
| FKBP12 as interaction partner | Correctly predicted | Yes |
| LST8-like scaffold predicted | Correct | Yes -- LST8 is TORC1 component |

### What was wrong or imprecise

1. **Localization partially wrong -- cytosol alone is incomplete**: BioReason assigns GO:0005829 (cytosol) as the sole localization. The curated review documents that TOR1 localizes to multiple membrane compartments: vacuolar membrane (GO:0000329, multiple evidence types), plasma membrane (GO:0005886), endosome, Golgi, and nucleus (GO:0005634). TORC1 is a membrane-associated complex, particularly at the vacuolar membrane where amino acid sensing via EGO complex and PIB2 occurs. Calling it purely cytosolic misses the membrane biology.

2. **TORC1 complex not explicitly named**: The curated review emphasizes TORC1 complex membership (GO:0031931) with specific components (TOR1/TOR2 + KOG1 + LST8 + TCO89). BioReason mentions "adaptor-rich complexes" generically but does not name TORC1 or its defined subunits (except LST8).

3. **IPR050517 labeled as "DNA Damage Response and Repair Kinase"**: This InterPro family annotation is technically the PIKK family, but BioReason correctly interprets it as nutrient/growth signaling rather than DNA damage repair. The naming could be misleading but the functional inference is correct.

### What was missed

| Missing Function | GO Term | Evidence |
|-----------------|---------|---------|
| TORC1 complex membership | GO:0031931 | IPI, IEA |
| TORC1 signaling (specific) | GO:0038202 | IBA |
| Negative regulation of macroautophagy | GO:0016242 | IBA |
| Negative regulation of autophagy | GO:0010507 | IEA, IGI |
| Response to nitrogen starvation | GO:0006995 | IEA, IGI |
| Response to nutrient | GO:0007584 | NAS |
| Regulation of cell cycle | GO:0051726 | NAS |
| Peptidyl-serine phosphorylation | GO:0018105 | IDA |
| Vacuolar membrane localization | GO:0000329 | HDA, IEA |
| Nuclear localization | GO:0005634 | IBA |
| Specific substrates (Tap42, Sch9, Ypk3, Stm1, Pib2) | -- | Multiple IDA |
| Response to ER stress | GO:0034976 | IMP |
| Regulation of snRNA pseudouridine synthesis | GO:1905356 | IEA |

### Failure modes observed

- **Localization oversimplification**: Predicting only cytosolic localization for a vacuolar membrane-associated kinase complex misses the spatial regulation of TORC1 signaling. The vacuolar membrane is the primary site of amino acid sensing.
- **Complex biology underspecified**: While BioReason correctly infers a kinase hub, it does not name the specific complex (TORC1) or distinguish TORC1 from TORC2.
- **Substrate specificity invisible**: The curated review documents specific phosphorylation targets (Tap42, Sch9, Ypk3, Stm1, Pib2). Domain architecture cannot predict substrates, which is expected but represents a completeness gap.
- **Conditional activities missed**: Nitrogen starvation response, autophagy regulation, and cell cycle control are condition-dependent functions not derivable from structure alone.

## Overall Assessment

TOR1 is BioReason's strongest result in this set. The PIKK/mTOR domain signature is distinctive enough that the reasoning chain from domains to TOR signaling is relatively straightforward. The main gaps are in membrane localization, complex identity, and the downstream regulatory network.
