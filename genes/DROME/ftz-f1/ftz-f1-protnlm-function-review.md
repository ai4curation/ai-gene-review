# ftz-f1: ProtNLM function-text review

**PLI (score 0) for high-affinity thyroid-hormone receptor specificity.** The nuclear-receptor family and transcriptional activation/repression clauses are supported. The 803-aa target is exactly identical to the reviewed FTZ-F1 isoform P33244-2; this is not an anonymous receptor fragment.

## Original prediction

[ProtNLM M9NFK2](https://www.uniprot.org/uniprotkb/M9NFK2/entry#prot-nlm), frozen API snapshot 2026-09-08:

> Nuclear hormone receptor that can act as a repressor or activator of transcription. High affinity receptor for thyroid hormones, including triiodothyronine and thyroxine

## Atomic assessment

| Claim | Assessment | Evidence |
|---|---|---|
| Nuclear hormone receptor | Supported as protein-family terminology | The target is the FTZ-F1 NR5A protein, with shared DNA-binding and regulatory domains; the phrase does not itself establish hormone binding. |
| Activates transcription | Supported | Regulatory-site mutagenesis, target transcription, and FTZ-F1/cofactor studies establish activation. |
| Represses transcription | Supported at the beta FTZ-F1 product level | The developmental isoform represses its own transcription; this need not be direct repression at every target. |
| High-affinity receptor for triiodothyronine and thyroxine | **PLI; PARALOG_OVERANNOTATION** | FTZ-F1 belongs to NR5A, whereas the recorded function-text phmmer match is an NR1A thyroid receptor. FTZ-F1-specific structural and functional studies support a distinct regulatory mechanism, not T3/T4 receptor specificity. |

## A traceable receptor-subfamily mismatch

The [raw prediction](ftz-f1-isoform-records/M9NFK2-protnlm.json) records `phmmer_accession: Q91279` and `phmmer_score: 98.6` for the function paragraph (`model_score: 0.08`). [Q91279](https://www.uniprot.org/uniprotkb/Q91279/entry) is Japanese flounder thyroid hormone receptor beta, NR1A2. Its [snapshotted function paragraph](ftz-f1-isoform-records/Q91279.json) is identical to the ProtNLM paragraph. The separately predicted protein name, “Nuclear receptor subfamily 5 group A member 2,” records the chicken NR5A2/LRH-1 accession [O42101](https://www.uniprot.org/uniprotkb/O42101/entry) with phmmer score 375.0.

Thus the prediction combines an NR5-related protein name with NR1 thyroid-receptor specificity. The recorded match and exact text establish a concrete attribution clue; they do not reconstruct the model's complete generation process or training history. The wrong-specificity assessment rests on the target's identity and FTZ-F1 experiments, rather than treating either donor's database prose as biological proof.

## FTZ-F1 biology and its limits

Purified FTZ-F1 recognizes regulatory DNA, and mutations that disrupt its recognition site reduce reporter expression in embryos ([PMID:2113881](https://pubmed.ncbi.nlm.nih.gov/2113881/), DOI [10.1101/gad.4.4.624](https://doi.org/10.1101/gad.4.4.624)). BetaFTZ-F1 supplies competence for stage-specific ecdysone responses and represses its own expression ([PMID:7954827](https://pubmed.ncbi.nlm.nih.gov/7954827/), DOI [10.1016/0092-8674(94)90546-0](https://doi.org/10.1016/0092-8674(94)90546-0)). Participation in the ecdysone-response cascade does not identify FTZ-F1 as the hormone-binding receptor.

The FTZ-F1/cofactor crystal structure places helix 6 inside the canonical ligand pocket and supports activity without added ligand ([PMID:21775434](https://pubmed.ncbi.nlm.nih.gov/21775434/), DOI [10.1074/jbc.M111.252916](https://doi.org/10.1074/jbc.M111.252916)). This is evidence for a different receptor mechanism, **not proof of universal ligand incapacity**. The solution NMR follow-up demonstrates pocket dynamics and in-vitro phospholipid binding ([PMID:29547262](https://pubmed.ncbi.nlm.nih.gov/29547262/), DOI [10.1021/acs.biochem.8b00069](https://doi.org/10.1021/acs.biochem.8b00069)). That experiment qualifies the closed-pocket interpretation, but supplies no T3/T4 binding affinity or thyroid-dependent transcriptional response. No claim of a direct negative T3/T4-binding experiment is made here.

## Accession and annotation scope

[Sequence comparison and snapshots](ftz-f1-isoform-records/README.md) show that M9NFK2 and P33244-2 are identical over all 803 amino acids. UniProt names this product **isoform A**; its alternative N terminus is associated with the developmental beta FTZ-F1 isoform through the reviewed sequence evidence from [PMID:8096644](https://pubmed.ncbi.nlm.nih.gov/8096644/). Database A/B product labels must not be read as Greek alpha/beta names. The longer reviewed product shares the complete DNA-binding and C-terminal regulatory domains, permitting transfer of their biochemical properties without indiscriminately transferring the longer product's embryonic expression pattern.

The main review separately evaluates all 12 GOA rows on this exact accession. Its electronic “nuclear receptor activity” assignment requires particular care: [GO:0004879](https://www.ebi.ac.uk/QuickGO/term/GO:0004879) explicitly requires ligand-regulated transcription. Protein-family membership and in-vitro lipid binding alone do not demonstrate that regulatory mechanism. The main review proposes the established RNA polymerase II transcription factor activity instead. No GO identifiers are invented or assigned to the original free-text prediction, and this narrative is excluded from GO-prediction denominators.
