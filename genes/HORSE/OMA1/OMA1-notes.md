# OMA1: paired evidence notes

Human reference: https://www.uniprot.org/uniprotkb/Q96E52/entry

Primary source: [PMID:20038677 Inducible proteolytic inactivation of OPA1 mediated by the OMA1 protease in mammalian cells.](https://pubmed.ncbi.nlm.nih.gov/20038677/).

> In this study, we show that this inducible cleavage is
> mediated by a zinc metalloprotease called OMA1. We find that OMA1 small
> interfering RNA inhibits inducible cleavage, helps retain fusion competence, and
> slows the onset of apoptosis, showing that OMA1 controls OPA1 cleavage and
> function.

The horse sequence comparison is in [OMA1-bioinformatics/RESULTS.md](OMA1-bioinformatics/RESULTS.md). Transfer is assessed for this exact accession; human biochemical evidence is not equine experimental validation.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

### Deep research
- `just deep-research-falcon HORSE OMA1 --fallback perplexity-lite` failed: Edison/falcon returned "Failed to authenticate" and the perplexity-lite fallback also failed. No deep-research file was written. The review uses cached primary literature and the human OMA1 deep research (`genes/human/OMA1/OMA1-deep-research-falcon.md`) as background only.

### Identity of A0A9L0R9P8 (gene model)
- New analysis: `OMA1-bioinformatics/compare_horse_models_rereview.py` writes `RESULTS-rereview.md` and `results-rereview.json`. It compares all horse OMA1 UniProt products with human Q96E52 and mouse Q9D8H7 (control). The Ensembl REST service returned HTTP 500 on 2026-10-20, so transcript structure comes from the UniProt Ensembl cross-references only.
- Horse gene ENSECAG00000009131 has at least 8 TrEMBL products (none reviewed). The UniProt gene-centric canonical for the horse reference proteome is A0A9L0R9P8 itself (513 aa, ENSECAT00000099022). F6YE56 (491 aa) carries the VGNC OMA1 gene name.
- A0A9L0R9P8 keeps human-equivalent residues 1-~400 (76.5% identity over human 1-404). That segment covers the transit/propeptide region, the TM helix (Phobius 187-205, matching human 196-216) and all zinc ligands plus the catalytic Glu (H319/E320/H323/E384, matching human H327/E328/H331/E392).
- From the position after the "LQLAAK" motif (about human 401), the target has about 80 residues with no OMA1 similarity (IRRLGTKQVKCFVQEH...). It therefore lacks the conserved exon that F6YE56 and A0A3Q2KVR1 retain (ACVDVRASSVFWQQMEF...STHPSHGHRAERLDRLIPQ), which corresponds to human ~401-456 and contains disulfide Cys407 and the C-terminal autocatalytic region 447-456. Identity over human 405-524 is 18.3%.
- The target's last ~30 residues (RLSKLERSVIAHHFLDQTLDYYSNSV) are the same as the F6YE56 C-terminus. Both horse models therefore end in a C-terminal exon that differs from the human isoform-1 one (human isoform 2 also has a different C-terminus, VSP_027958). The target looks like an alternative or mispredicted splice model that swaps the conserved penultimate exon for unrelated sequence.
- Conclusion: the target is the canonical gene-centric entry for horse OMA1, but its gene model is atypical. Gene-level annotations are retained; whether this product is active is unknown (suggested question and experiment added).

### Evolutionary grounding
- PANTHER PTHR22726:SF1 (METALLOENDOPEPTIDASE OMA1, MITOCHONDRIAL) contains horse, human Q96E52 and mouse Q9D8H7.
- IBA metalloendopeptidase comes from PTN000506393, a deep node that includes bacterial P66948. Inner membrane and protein quality control come from PTN000506394, the eukaryotic OMA1 node (SGD Oma1, AT5G51740, MGI, human). Horse is inside both nodes.
- Human experimental terms that PAINT did not propagate (OPA1-related fusion regulation, ISR, apoptosis, cristae) reach horse only by Ensembl Compara one-to-one ortholog IEA. They are judged on the human evidence and kept at their curated precision, mostly as non-core context terms.
- The interpro/panther/PTHR22726 family review lists A0A9L0R9P8 and Q96E52 as SF1 representatives, which agrees with this placement. Its subfamily description is copy-pasted from the family coherence text (it mentions bacterial YggG/LoiP, which are not in SF1). This is a description defect, not a placement disagreement.

### Annotation decisions (re-review)
- ACCEPT: GO:0004222 (IBA, IEA), GO:0005743 (IBA, IEA), GO:0005758 is_active_in, GO:0006515 (IBA, IEA), GO:0010637, GO:0034982, GO:0140467.
- MODIFY: GO:0006508 -> GO:0034982; GO:0031966 -> GO:0005743; GO:0033554 -> GO:0140467. In each case the replacement is a descendant the gene already carries.
- KEEP_AS_NON_CORE: GO:0043065 positive regulation of apoptotic process, GO:0140468 HRI-mediated signaling (OMA1 acts upstream of HRI) and GO:1903850 regulation of cristae formation.
- The previous version quoted the same long human UniProt FUNCTION block for every row. Rows now quote the primary papers: [PMID:20038677 "wild-type OMA1 was able to compensate for OMA1 siRNA by restoring CCCP-induced cleavage of OPA1, whereas OMA1(H331A) did not restore cleavage"], [PMID:12963738 "These results identify Oma1 as a novel component of the quality control system in the inner membrane of mitochondria."], [PMID:32132706 "stress-induced activation of OMA1 causes DELE1 to be cleaved into a short form that accumulates in the cytosol"], [PMID:25275009 "Activated OMA1 cleaved the dynamin-like GTPase, optical nerve atrophy 1"].
- PMID:12963738 (Käser 2003, yeast Oma1) was newly cached (abstract only).

### Relative
- Human OMA1 Q96E52 (same subfamily SF1, a donor of both PAINT nodes, and the most extensively characterized). `genes/human/OMA1/OMA1-ai-review.yaml` exists but has status IN_PROGRESS. Its rows reuse one templated UniProt FUNCTION quote and it has a single generic core function, so it would benefit from a full re-review.
- Module: `modules/mitochondrial_upr.yaml` (mammalian OMA1-DELE1-HRI route, grounded on Q96E52).
