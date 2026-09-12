# fliY (P24073) — GO Decision Table (curator leads; verify before applying)

**Focus:** Evaluate BioReason-Pro SFT prediction of **cell septum (GO:0030428, CC)**.
**Verdict:** REFUTED — over-annotation / misassignment.

| GO term | Aspect | Status of prediction / existing annot. | Recommended curation action | Support | Key evidence |
|---|---|---|---|---|---|
| **GO:0030428 cell septum** | CC | Predicted (BioReason-Pro) | **REJECT — do not add** | None | No literature/domain/interaction support; false positive |
| GO:0009425 bacterial-type flagellum basal body | CC | Existing (IEA:InterPro) | **RETAIN** (preferred CC) | Strong | PMID 23532838, 30455280; InterPro |
| GO:0005886 plasma membrane (cytoplasmic side) | CC | Existing (IEA:SubCell) | RETAIN | Strong | UniProt; peripheral, cytoplasmic side |
| GO:0004721 phosphoprotein phosphatase activity | MF | Existing (IDA:CACAO) | RETAIN; consider more specific CheY-P dephosphorylation framing | Strong | PMID 12920116, 14749334 |
| GO:0003774 cytoskeletal motor activity | MF | Existing (IEA:InterPro) | REVIEW — likely too strong (FliY is switch/phosphatase, not a motor ATPase); consider removal/refinement | Weak | Family carry-over; no motor assay for FliY |
| GO:0006935 chemotaxis | BP | Existing (IMP:CACAO) | RETAIN | Strong | PMID 1447979, 14749334 |
| GO:0044780 bacterial-type flagellum assembly | BP | Existing (IMP:CACAO) | RETAIN | Strong | PMID 1447979 (null = no flagella) |
| GO:1902021 regulation of flagellum-dependent motility | BP | Existing (IMP:CACAO) | RETAIN | Strong | PMID 12920116 |
| GO:0016311 dephosphorylation | BP | Existing (IMP:CACAO) | RETAIN | Strong | PMID 14749334 |

## Why the septum prediction likely arose (error-mode note for curator)
1. **"SpoA-like" superfamily label** (SSF101801, aa 295–376) = **S**urface **P**resentation **O**f **A**ntigens of the type-III secretion system — easily conflated with **spo**rulation/**sep**tation by a text/label-driven model.
2. **Ring-at-the-membrane analogy:** the flagellar **C-ring** and the cytokinetic **Z-ring** are both membrane-proximal oligomeric rings; a model may generalize "assembles into a ring at the membrane → division site."
3. Neither reflects biology: fliY's partners and domains are exclusively flagellar/chemotaxis.

## Provenance
- Literature: PMID 1447979, 12920116, 14749334, 23532838, 15546616, 30455280, 17675386
- Computed (this run): InterPro API domain map + STRING v12 network — see `fliY_provenance.md`
