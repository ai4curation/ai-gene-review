# CG5565 evidence notes

## Identity and evidence

Q9VQ04 is the single 240-residue CG5565-PA product in the current FlyBase record. The complete HAD-family architecture is compatible with the manually transferred PUDP activity; it is not a truncated native isoform.

[PMID:20722631](https://pubmed.ncbi.nlm.nih.gov/20722631/) characterized human HDHD1/PUDP Q08623: purified enzyme hydrolyzed pseudouridine 5′-phosphate with Km 0.3 μM and at least 1000-fold greater catalytic efficiency than the other tested phosphate esters. GOA specifically records manual ortholog transfer from that experimentally characterized protein. The proposed core function is a qualified inference rather than a direct fly assay.

The current PTHR18901 PAINT export places pseudouridine 5′-phosphatase activity at PTN000431252, seeded by human PUDP and corroborated through the UniProt cross-reference for yeast YKL033W-A, while the broad GO:0016791 phosphatase IBA in the CG5565 GOA snapshot cites PTN000431251. Re-fetching PTHR18901 with Q9VQ04 explicitly included did not put PTN000431251 into the local slice, so the slice is insufficient to call that GOA source stale. The GOA seed union is instead consistent with a legitimate broad phosphatase placement above the plant GPP and human/yeast PUDP branches. The broad IBA remains less granular than the existing FlyBase ISS to human PUDP, but direct Drosophila kinetics and PAINT descent from PTN000431252 remain unestablished.

The ProtNLM structural donor Q9V1B3 is a Pyrococcus protein; its glyceraldehyde-3-phosphate statement is itself by similarity to Q58832. Shared structure does not determine substrate specificity. Conversely the existence of a better-supported physiological substrate cannot refute the explicitly in vitro side-activity claim, which remains UNC. The source is a function paragraph only, with no original GO predictions.

## Research assessment and sequence check

The Falcon report was inspected. Its discussion of HAD substrate ambiguity is relevant, but its “no specific reaction without biochemical testing” recommendation misses the current FlyBase PUDP ortholog transfer to experimentally characterized human Q08623. A full-length comparison with that human protein retains both catalytic Asp positions and covers 226 of 228 human residues; the original archaeal structural donor is substantially less similar in sequence. This supports accepting the qualified PUDP transfer while keeping the separate in vitro substrate claim unresolved. The comparison alone does not establish orthology or prove a particular substrate. Inputs, script, alignments, controls and [RESULTS.md](CG5565-bioinformatics/RESULTS.md) are retained.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Identity: Q9VQ04 is the canonical (only) FlyBase product CG5565-PA, 240 aa, full-length HAD-IA fold with the DxD catalytic motif (Asp16/Asp18) intact. It is not a fragment, isoform or alternative gene model.

Evolutionary grounding (new analysis, `CG5565-bioinformatics/panther_tree_rereview.py`, results in `CG5565-bioinformatics/RESULTS-rereview.md`): a walk of the PANTHER 19 PTHR18901 tree shows that CG5565 descends from PTN000431252 (Unikonts). That node carries the PAINT IBD for GO:1990738 pseudouridine 5'-phosphatase activity, seeded by human PUDP (Q08623, IDA PMID:20722631) and yeast YKL033W-A. This answers the open question in the earlier notes: CG5565 is inside the PTN000431252 clade. That IBD (dated 20260729) has not reached GOA yet, and even human PUDP has only the PTN000431251 GO:0016791 IBA in QuickGO, so its absence from the CG5565 GOA snapshot is lag, not a curator decision to exclude it.

The fly has a dipteran-specific duplication (PTN000431298) giving five paralogs: CG5565, Gs1l, CG5561, CG5556 and CG5564 (CG31924). CG5565 is therefore a co-ortholog of human PUDP. The UniProt subfamily mismatch (fly SF38, human PUDP SF43) comes from a recent Catarrhini duplication; mouse Pudp is SF38. So it does not show that CG5565 sits outside the characterised clade. The plant GPP glycerol-3-phosphatase IBD (GO:0043136) is placed in the bikont/plant lineage (PTN008360158) and is not inherited, so it is not proposed.

FlyBase: testis specificity index 4.86; protein detected in the sperm proteome (Dorus et al. 2006, via FlyBase); the only phenotype is from an RNAi screen (abnormal pain response with elav-GAL4), which is not used as a process annotation.

Actions: both GO:0016791 rows (IBA, IEA) MODIFY → GO:1990738 (correct but too general; the specific term is already on the gene). GO:1990738 ISS ACCEPT, now supported by the tree placement as well as the human kinetics. Core function unchanged. Added a suggested question and experiments on paralog subfunctionalisation. No NEW annotations: the fly protein has no localisation or process evidence.

Relative to review next: human PUDP (Q08623), the experimentally characterised co-ortholog in the same PTN000431252 clade; it has no review in the repo. The PANTHER family review `interpro/panther/PTHR18901/PTHR18901-review.yaml` lists CG5565 under SF38, which agrees with the UniProt subfamily. Its summary says CG5565 "remains a phosphatase-family protein with unresolved physiological substrate", which is more conservative than the tree supports. The tree supports pseudouridine 5'-phosphatase activity, inherited but not assayed. I have not edited the family review. The deep-research (falcon) file was read previously; its "no specific reaction without biochemical testing" stance is superseded by the PAINT placement.
