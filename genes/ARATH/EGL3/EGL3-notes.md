# EGL3 (ENHANCER OF GLABRA3; AtbHLH2; At1g63650; UniProt Q9CAD0) curation notes

## Identity
- UniProt Q9CAD0 is named "Transcription factor EGL1" (gene BHLH2; synonyms EGL1, EGL3, EN30, MYC146), locus AT1G63650. Verified as the intended EGL3 protein (subgroup IIIf bHLH, paralog of GL3/At5g41315 and TT8/At4g09820).

## Key findings (with provenance)
- egl3 single mutants are near wild type; gl3 egl3 is glabrous and ttg1-like [PMID:12917293 "When mutated, egl3 gives totally glabrous plants only in the gl3 mutant background."; "The double bHLH mutant, gl3 egl3, has a pleiotropic phenotype like ttg1 having defective anthocyanin production, seed coat mucilage production, and position-dependent root hair spacing."]
- Partners: TTG1, GL1, PAP1/2, CPC, TRY, GL3 heterodimer [PMID:12917293 "EGL3, like GL3, interacts with TTG1, the myb proteins GL1, PAP1 and 2, CPC and TRY, and it will form heterodimers with GL3."]
- Root: GL3/EGL3 specify non-hair fate, needed for GL2 and CPC transcription, bind WER and CPC [PMID:14627722 "Plants homozygous for mutations in both genes fail to specify the non-hair cell type"]; WER acts with GL3/EGL3 to induce GL2 and competes with CPC [PMID:21914815 "WER acts together with GL3/EGL3 to induce GL2 expression"].
- Direct targets shared with GL3 (ChIP) [PMID:17885086 "we show that EGL3 shares some direct targets with GL3"].
- Hormonal inputs (non-core): JAZ repressors bind EGL3; gl3 egl3 lacks JA-induced trichome initiation [PMID:21551388 "the JA-induced trichome initiation was disrupted in gl1 and the gl3 egl3 double mutant"]; DELLAs bind EGL3/GL3/GL1 [PMID:24659329]; BIN2 phosphorylates EGL3 (T399, T209/T213) and relocalizes it in root H cells [PMID:24771765].
- R3 MYB inhibitors compete with R2R3 MYBs for GL3/EGL3 binding [PMID:18766177 "These inhibitors can compete with the R2R3 MYB factor for binding to GL3/EGL3 in yeast three-hybrid assays"].

## Curation decisions
- DNA-binding TF activity (ISS x3) and cis-regulatory region binding (IBA) accepted: bHLH domain intact; shared direct targets with GL3.
- protein binding rows with MYB partners -> MODIFY to GO:0140297 DNA-binding transcription factor binding (repo policy disallows MARK_AS_OVER_ANNOTATED for GO:0005515).
- protein binding rows with DELLA (RGA, RGL2) and BIN2 -> REMOVE (regulatory inputs; interaction not disputed).
- JA signaling (IBA/IEA/IMP) kept as non-core hormonal input.
- Falcon deep research (EGL3-deep-research-falcon.md) generated 2026-10-05; used for the GL2-promoter ChIP point.

## 2026-10-06 PR #4395 review follow-up
- The three GO:0005515 IPI rows with CPC (UniProtKB:O22059) as partner (PMID:12917293, PMID:14627722, PMID:15361138) changed from MODIFY to GO:0140297 DNA-binding transcription factor binding to REMOVE. GO:0140297 would assert CPC is a DNA-binding TF, contradicting the CPC review (no demonstrated CPC DNA binding; GO:0003700 replaced, GO:0000976 over-annotated). As with the DELLA/BIN2 rows, CPC binding is a repressive regulatory input on EGL3; the informative term is on CPC (GO:0140416). PAP1/PAP2/WER rows stay on GO:0140297 (genuine R2R3 MYBs).
- PMID:15361138 rows now quote the abstract's statement of the conserved R3 signature "as the structural basis for interaction between MYB and R/B-like BHLH proteins" instead of a motif tally; the cache is abstract-only, so per-pair data are deferred to the curator.
