# ALG5: ProtNLM function-text review

**PLI (score 0): the paragraph assigns dolichyl-phosphate mannose synthesis to an ALG5-family protein.**

## Original prediction

[ProtNLM A0A5F5PM72](https://www.uniprot.org/uniprotkb/A0A5F5PM72/entry#prot-nlm), frozen API snapshot 2026-09-08.

> Transfers mannose from GDP-mannose to dolichol monophosphate to form dolichol phosphate mannose (Dol-P-Man) which is the mannosyl donor in pathways leading to N-glycosylation, glycosyl phosphatidylinositol membrane anchoring, and O-mannosylation of proteins; catalytic subunit of the dolichol-phosphate mannose (DPM) synthase complex

## Atomic claims

| Claim | Assessment | Evidence |
|---|---|---|
| Transfers mannose from GDP-mannose to dolichol phosphate | PLI | Human ALG5 is the UDP-glucose-dependent dolichyl-phosphate glucosyltransferase; exact horse sequence belongs to this family. |
| Catalytic subunit of DPM synthase | PLI | This assigns a different dolichol-sugar synthase identity; no DPM-complex membership or GDP-mannose chemistry is supported for ALG5. |
| Product supplies N-glycosylation, GPI anchoring and O-mannosylation | Mixed | N-glycosylation is relevant to ALG5 through Dol-P-Glc, but the predicted Dol-P-Man product and downstream GPI/O-mannosylation routes do not follow. |

Human [PMID:10359825](https://pubmed.ncbi.nlm.nih.gov/10359825/), DOI [10.1073/pnas.96.12.6982](https://doi.org/10.1073/pnas.96.12.6982), functionally complements the yeast alg5 defect with human ALG5. The curated human [UniProtQ9Y673](https://www.uniprot.org/uniprotkb/Q9Y673/entry) reaction uses UDP-glucose and its experimentally grounded description states “glucose donor substrate used sequentially by ALG6, ALG8 and ALG10”. Those observations establish the relevant substrate/pathway distinction.

The [horse alignment](ALG5-bioinformatics/RESULTS.md) preserves the membrane anchor and 94.6% identity across 294 paired residues, but reveals an internal 30 aa deletion (human 95–124). Therefore, an active horse glucosyltransferase is **not** asserted as experimentally established, and the main horse activity annotation remains uncertain. This uncertainty does not supply positive evidence for conversion to GDP-mannose specificity or DPM-complex membership. The exact training donor is unknown; **PARALOG_OVERANNOTATION** describes the inappropriate transfer between distinct dolichol-sugar synthase functions, not a recovered model provenance chain.
