# PANTHER Family Review: PTHR10574

## Family overview

PANTHER's official name for PTHR10574 is **NETRIN/LAMININ-RELATED** (`panther.obo`). The cached InterPro metadata uses the display name “Laminin/Netrin Extracellular Matrix” and links IPR050440. Its counts (31,327 proteins, 4,860 taxa, 37 subfamilies) describe the 2026-02-05 snapshot, not a current census. The metadata description is explicitly marked `llm: true` and `checked: false`; it is orientation, not independent evidence.

The cached member table includes laminin chains and netrins. Human NTN1 (O95631) is assigned to PTHR10574:SF378, **NETRIN-1**, and NTN3 (O00634) to PTHR10574:SF292, **NETRIN-3**. Laminins contribute to basement-membrane structure; netrins can act as receptor ligands in guidance, adhesion and survival. Those distinct roles do not justify assigning every function to every member.

## Netrin biology and its limits

Full-length NTN1 is a secreted ligand whose DCC/UNC5-family interactions control axon responses. Human variants impair secretion and cause congenital mirror movements ([PMID:28945198](https://pubmed.ncbi.nlm.nih.gov/28945198/)). Extracellular matrix association and secretion are compatible: a secreted cue may act as a local adhesive substrate rather than only as a freely diffusible gradient ([PMID:28780049](https://pubmed.ncbi.nlm.nih.gov/28780049/)).

Primary extracellular localization is not exclusivity. Some human cancer cells express an N-terminally truncated NTN1 form from an internal promoter. This form localizes to the nucleolus and associates with ribosomal-gene promoters ([PMID:22871610](https://pubmed.ncbi.nlm.nih.gov/22871610/)). This finding invalidates the previous blanket prohibition on nuclear annotations. Its ribosome-biogenesis context does not establish RNA-polymerase-II-specific transcription-factor activity or sequence recognition.

Human NTN3 was initially characterized as NTN2L by cloning and transcript analysis ([PMID:9143507](https://pubmed.ncbi.nlm.nih.gov/9143507/)). The distinct mouse ortholog study demonstrated binding to DCC, neogenin and UNC5H1/H2/H3, lower affinity for DCC than for the other tested receptors, and axon-outgrowth activity ([PMID:10366627](https://pubmed.ncbi.nlm.nih.gov/10366627/)). The mouse study supports conserved netrin-receptor ligand function; it should not be misidentified as the original human paper or used to claim identical expression in all tissues or species.

NTN1 and NTN3 have laminin N-terminal, laminin EGF-like and NTR-domain architecture, rather than the POU-specific DNA-binding architecture of the transcription-factor seeds below. The previous domain table reused one InterPro identifier for three different domains and is withdrawn. The generated member and metadata files are preserved unchanged.

## Disputed POU-seeded annotations

The historical GOA rows for NTN1/NTN3 cite PTN000180816 and experimentally characterized POU transcription factors. The current cached `PTHR10574-paint.tsv` also contains the POU-seeded IBD rows. Thus, the export contains a real provenance discrepancy that must be traced through the underlying family tree; this review does not establish whether it originated in tree placement, identifier mapping, or export assembly. A short donor list would not weaken an IBD, and donor identity alone is not a biological verdict.

| GO term | Current NTN1/NTN3 assessment | Reason |
|---|---|---|
| GO:0000981 DNA-binding transcription factor activity, RNA polymerase II-specific | REMOVE | The specific sequence-recognition activity does not follow from the target netrin architecture or an established functional relationship to the POU seeds. |
| GO:0000978 RNA polymerase II cis-regulatory region sequence-specific DNA binding | REMOVE | The POU-derived DNA-recognition assertion is unsupported for the target netrins; NTN1 ribosomal-promoter association does not establish this Pol II-specific MF. |
| GO:0006357 regulation of transcription by RNA polymerase II | UNDECIDED | This broader process can involve signaling proteins. Neither the defective trace nor secretion establishes that netrin-specific regulation is impossible. |

POU5F1 (Q01860) is independently indexed in `panther-members.tsv` under PTHR11636:SF86. That confirms a mismatch for one named source, while the current IBD export still requires upstream inspection. No family assignment is inferred for the other sources from memory.

The target-specific MF removals are curation recommendations, not experimental NOT annotations. No negative experiment has been supplied that would justify manufacturing a NOT annotation. Likewise, no family-wide “never nuclear” rule is justified.

## Evidence and citation corrections

| Reference | Verified title and relevant scope |
|---|---|
| [PMID:28945198](https://pubmed.ncbi.nlm.nih.gov/28945198/) | *Mutations in the netrin-1 gene cause congenital mirror movements.* Primary human variant/secretion evidence. |
| [PMID:26190107](https://pubmed.ncbi.nlm.nih.gov/26190107/) | *A Floor-Plate Extracellular Protein-Protein Interaction Screen Identifies Draxin as a Secreted Netrin-1 Antagonist.* Interaction-network evidence. |
| [PMID:9143507](https://pubmed.ncbi.nlm.nih.gov/9143507/) | *The NTN2L gene encoding a novel human netrin maps to the autosomal dominant polycystic kidney disease region on chromosome 16p13.3.* Human gene characterization. |
| [PMID:10366627](https://pubmed.ncbi.nlm.nih.gov/10366627/) | *Netrin-3, a mouse homolog of human NTN2L, is highly expressed in sensory ganglia and shows differential binding to netrin receptors.* Mouse ortholog binding/function study. |
| [PMID:22871610](https://pubmed.ncbi.nlm.nih.gov/22871610/) | *Nucleolar localization of a netrin-1 isoform enhances tumor cell proliferation.* Context-specific intracellular form. |
| [PMID:28780049](https://pubmed.ncbi.nlm.nih.gov/28780049/) | *Netrin1 establishes multiple boundaries for axon growth in the developing spinal cord.* Local substrate-guidance mechanism. |

The previous generic-review titles attached to the first three PMIDs were incorrect. They have been replaced with the cached primary records. Unverified broad review-title suggestions were removed.

## Review status

- Date: 2026-09-20
- Reviewer: Codex, AI-assisted evidence re-review
- Status: DRAFT; specific Pol II regulation and upstream PAINT provenance remain unresolved
- Gene decisions: [NTN1](../../../genes/human/NTN1/NTN1-ai-review.yaml), [NTN3](../../../genes/human/NTN3/NTN3-ai-review.yaml)
- Evidence audit: [context-transfer.yaml](../../../projects/IBA_REVIEW/rereview-2026-09-20/context-transfer.yaml)
