---
title: Human and model-organism ProtNLM challenge set
species: [human, mouse, rat, worm, ARATH, DANRE, XENLA]
tags: [EVALUATION, ML_PREDICTIONS]
autolink_gene_symbols: false
---
# Human and model-organism ProtNLM challenge set

**Twenty additional genes across seven species, selected for informative function-prediction reviews and evolutionary comparisons.** All twenty have live, exact-accession ProtNLM outputs. The set contains **20 GO predictions, 14 function paragraphs, 14 localization statements and 20 protein names**, preserved separately. Selection is complete; biological reviews and evolutionary analyses are pending.

This queue complements the [eight remaining pombe genes](pombe-remaining.md) and the [next twenty fly genes](fly-next20.md). The twenty targets here all carry GO or function output, so none is a comparison gene without a prediction. Proposed relatives used for evolutionary analysis are a separate evidence panel and are not counted as benchmark targets.

[Selection and review questions](mod-evolution-benchmark/cohort.csv) · [Exact predictions](mod-evolution-benchmark/prediction-statements.csv) · [Source manifest](mod-evolution-benchmark/manifest.json) · [Methods and frozen sources](mod-evolution-benchmark/README.md) · [Parent project](../PROTNLM_EVALUATION.md)

## Selected genes

Each accession links to its actual ProtNLM output. Gene names and MOD identifiers come from the accompanying UniProt records; they identify the intended gene, but do not establish that every property of its usual full-length product applies to the selected sequence.

| Species | Gene | Prediction accession | Review and evolutionary question |
|---|---|---|---|
| Human | UBE2F | [F8WDQ9](https://rest.uniprot.org/uniprotkb/protnlm/F8WDQ9) | Ubiquitin versus NEDD8 transfer; distinguish the intrinsic reaction from downstream ubiquitination. |
| Human | NARF | [J3KS48](https://rest.uniprot.org/uniprotkb/protnlm/J3KS48) | Hydrogenase-fold diversification and NARF versus NARFL/CIAO3 attribution of Fe-S assembly functions. |
| Human | DTD1 | [A0A2R8YCT7](https://rest.uniprot.org/uniprotkb/protnlm/A0A2R8YCT7) | Aminoacyl-tRNA substrate specificity and divergence from ATD. |
| Human | ACAD9 | [A0A7P0T7Z1](https://rest.uniprot.org/uniprotkb/protnlm/A0A7P0T7Z1) | Fatty-acid metabolism, FAD-dependent catalysis and recruitment into complex I assembly. |
| Human | RHOJ | [G3V4H1](https://rest.uniprot.org/uniprotkb/protnlm/G3V4H1) | Test the paragraph's intrinsic-GTPase inactivity and GAP-resistance claims against the relevant Rho subfamily. |
| Mouse | Spcs2 | [A0A140LHW5](https://rest.uniprot.org/uniprotkb/protnlm/A0A140LHW5) | Signal-peptidase catalysis versus a noncatalytic complex component; inspect the short product. |
| Mouse | Sdhaf2 | [A0A494B8X4](https://rest.uniprot.org/uniprotkb/protnlm/A0A494B8X4) | FAD attachment and respiratory-complex assembly; factor–client relationships across species. |
| Mouse | Vmn2r73 | [A0A3B2WCZ5](https://rest.uniprot.org/uniprotkb/protnlm/A0A3B2WCZ5) | Glutamate-receptor paragraph versus vomeronasal receptor subfamily and ligand diversification. |
| Rat | Pnkd | [B4F7D2](https://rest.uniprot.org/uniprotkb/protnlm/B4F7D2) | The specific glyoxalase-II reaction versus a related hydrolase with different substrate evidence. |
| Rat | Mtmr12 | [A0A8I5ZMD5](https://rest.uniprot.org/uniprotkb/protnlm/A0A8I5ZMD5) | An inactive-phosphatase-family comparison; assess the actual name/localization claims without inventing a catalytic prediction. |
| Rat | Ptk7 | [A0A8I6ALM9](https://rest.uniprot.org/uniprotkb/protnlm/A0A8I6ALM9) | Pseudokinase architecture and the emitted adhesion/Plexin paragraph; separate extracellular and kinase-domain evolution. |
| Worm | dpm-1 | [U4PF58](https://rest.uniprot.org/uniprotkb/protnlm/U4PF58) | A 51-residue product with a detailed mannosyltransferase paragraph; resolve the sequence before comparing enzyme/anchor organization. |
| Worm | wdr-23 | [S6FN32](https://rest.uniprot.org/uniprotkb/protnlm/S6FN32) | Translation/ribosome predictions versus the substrate-receptor paragraph; specificity within WD-repeat proteins. |
| Worm | C28G1.2 | [Q18287](https://rest.uniprot.org/uniprotkb/protnlm/Q18287) | Inhibitory-serpin claims versus collagen-chaperone function; reactive-center loop and subfamily placement. |
| Arabidopsis | FTSH12 | [A0A1P8ARD2](https://rest.uniprot.org/uniprotkb/protnlm/A0A1P8ARD2) | Protease-family diversification into the chloroplast import machinery; assess ATPase and protease functions separately. |
| Arabidopsis | DRS1 | [Q9SAI7](https://rest.uniprot.org/uniprotkb/protnlm/Q9SAI7) | Transfer of a specific 5-hydroxymethylcytosine-reader function into a plant protein. |
| Arabidopsis | AT4G38370 | [Q0WW53](https://rest.uniprot.org/uniprotkb/protnlm/Q0WW53) | Substrate specificity within the putative phosphoglycerate-mutase/histidine-phosphatase superfamily. |
| Zebrafish | dcxr | [Q567K5](https://rest.uniprot.org/uniprotkb/protnlm/Q567K5) | Dicarbonyl/L-xylulose reductase naming versus a beta-ketoacyl-ACP reductase paragraph. |
| Zebrafish | hes6 | [Q6P0J1](https://rest.uniprot.org/uniprotkb/protnlm/Q6P0J1) | DNA recognition versus dimerization and transcriptional regulation among Hes/Her proteins. |
| Xenopus laevis | uap1.S | [Q6DCZ6](https://rest.uniprot.org/uniprotkb/protnlm/Q6DCZ6) | UDP-GlcNAc versus UDP-glucose synthesis, with an explicit S/L-homeolog comparison. |

## First evolutionary investigations

These are tractable questions with experimental starting points, not predetermined prediction verdicts.

1. **Pnkd and HAGH: a substrate-specificity test.** Published biochemical work reports that PNKD does not catalyze the same reaction as glyoxalase II, while leaving other thioesterase substrates open. Compare the rat sequence with the experimentally tested mammalian proteins, then map metal-binding and substrate-pocket differences across the two branches. A negative result for one substrate does not establish universal catalytic inactivity. [Primary study](https://pmc.ncbi.nlm.nih.gov/articles/PMC3098736/).

2. **DTD1 and ATD: evolution of proofreading specificity.** ATD was experimentally characterized as a DTD-related enzyme with relaxed chiral selectivity and a different Gly-Pro conformation. A useful analysis would connect family placement, the surrounding active-site structure and tested tRNA substrates. Resolve the selected short DTD1 product first; sequence alone cannot establish proline cis/trans geometry. [Primary structural and biochemical study](https://pmc.ncbi.nlm.nih.gov/articles/PMC5802732/).

3. **FTSH12, FtsHi and Ycf2: domain-specific functional change.** The characterized chloroplast import complex supplies a framework for testing how ATPase and protease domains have diversified. Sample active FtsH proteases and the import-associated proteins, reconstruct the domains separately, and map catalytic motifs. Do not infer FTSH12 inactivity simply because its FtsHi partners are inactive proteases. [Primary import-complex study](https://pmc.ncbi.nlm.nih.gov/articles/PMC6305978/).

4. **UBE2F and other E2 enzymes: modifier specificity.** Experimental work distinguishes NEDD8 E2 pathways and cullin preferences. Compare UBE2F with UBE2M and ubiquitin E2s, mapping modifier/E1/E3 interfaces as well as the catalytic cysteine. This tests a mechanistic distinction that a shared E2 fold cannot resolve. The 101-residue target must be mapped before interpreting absent interfaces. [Primary specificity study](https://pmc.ncbi.nlm.nih.gov/articles/PMC2725360/).

5. **ACAD9 and ACADVL: catalytic activity and assembly recruitment.** Structural and biochemical work shows ECSIT-dependent deflavination of ACAD9; cellular studies also support an ACAD9 contribution to fatty-acid oxidation. Compare the catalytic core and assembly-factor interface while retaining tissue and complex-state distinctions. Use the existing human ACAD9 review and investigation as evidence leads, after checking how their tested sequence relates to this accession. [Deflavination study](https://pmc.ncbi.nlm.nih.gov/articles/PMC7986633/), [cellular fatty-acid oxidation study](https://pmc.ncbi.nlm.nih.gov/articles/PMC4424958/).

**Next tier:** NARF/NARFL is particularly interesting because the Fe-S assembly evidence needs careful paralog attribution. The mouse IOP1/NARFL knockout study is an experimental anchor, not automatic validation for NARF. The frozen same-gene search also retrieved RNF138 through its *NARF* alias; the shared-HGNC-ID check excludes it. [Primary IOP1 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC3091189/). The dcxr and uap1.S substrate questions provide additional metabolic comparisons; Mtmr12 and Ptk7 connect to the mammalian pseudoenzyme cases.

## Sequence checks before functional transfer

The [same-gene reference table](mod-evolution-benchmark/same-gene-references.csv) identifies nine reviewed comparison records using shared MOD identifiers. Eight targets are shorter than those references. Length differences alone do not distinguish alternative splicing, incomplete records or genuine domain loss.

| Gene | Target length | Reviewed same-gene reference length |
|---|---:|---:|
| UBE2F | 101 | 185 |
| NARF | 217 | 456 |
| DTD1 | 127 | 209 |
| ACAD9 | 626 | 621 |
| RHOJ | 153 | 214 |
| Spcs2 | 74 | 226 |
| Sdhaf2 | 135 | 164 |
| Mtmr12 | 732 | 748 |
| FTSH12 | 991 | 1008 |

The 51-residue dpm-1 product is another sequence-identity priority. It has no reviewed same-species reference in the frozen query. These lengths refer to current UniProt records; the ProtNLM API does not supply the original model input sequences. Historical input identity therefore remains unverified.

For each priority family, first establish the target transcript and domain coverage, then retrieve characterized relatives and suitable outgroups. Build alignments and supported gene trees, distinguish orthologs from paralogs, reconcile credible duplications with the species tree, and map catalytic or substrate-recognition changes onto the supported branches. Treat apparent motif loss in a short record as a gene-model question until sequence completeness is established. A lack of evidence for a branch assignment should remain unresolved.

Budding yeast, pombe, fly and additional vertebrates can contribute characterized comparison proteins even when their relevant accession has no ProtNLM prediction. Those proteins belong in the evidence panel, with their own source and sequence provenance.

## Evaluation scope

This is a **purposive challenge set assembled after seeing the predictions**, enriched for mechanistic distinctions and evolutionary questions. It cannot estimate general ProtNLM accuracy. Related targets and evidence-panel proteins should remain in the same family group for any later train/test split or aggregate analysis.

Reviews follow the [function-prediction review skill](https://github.com/ai4curation/ai-gene-review/blob/main/.codex/skills/review-function-prediction/SKILL.md). Evaluate the exact claims separately, use experimental and reproducible analytical evidence, and distinguish family inference from direct observation. Protein names and UniProt SL locations remain their original output types. No COR/CNN/LSP/UNC/PLI/NPI/REP outcomes are assigned by the selection tables.
