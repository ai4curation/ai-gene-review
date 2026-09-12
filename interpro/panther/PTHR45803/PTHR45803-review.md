# PANTHER Family Review: PTHR45803

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR45803 |
| **Family Name** | SOX Transcription Factors (SOX_TF) |
| **InterPro Entry** | IPR050917 |
| **Total Proteins** | 4,869 |
| **Taxonomic Breadth** | 5,029 taxa |
| **Subfamilies** | 5 |
| **Representative Structure** | (none recorded) |

## Executive Summary

PTHR45803 is a family of **HMG-box DNA-binding transcription factors of the SOX type**. Its members carry a single high-mobility-group (HMG) DNA-binding domain, bind sequence-specifically to T-rich DNA motifs, bend the DNA, and activate RNA polymerase II transcription. The metazoan members are the well-known **SoxE group (SOX8/SOX9/SOX10)** plus the insect SOX100B clade, with roles in chondrogenesis, neural-crest/glia development, sex determination and cell-fate specification.

The S. pombe anchor gene, **ste11** (P36631), is the fission-yeast **master HMG-box transcription factor of sexual differentiation**. Notably, PANTHER places ste11 in subfamily **PTHR45803:SF5 (SOX100B)** by its UniProt cross-reference, which is a *different* fine subfamily from the metazoan SoxE clades that seed most IBAs. This is a clear example of PANTHER grouping divergent HMG/SOX subfamilies into one family: ste11 is evolutionarily distant from vertebrate SOX9/10 but is **genuinely an HMG-box, sequence-specific RNA Pol II transcription factor**. Consequently, the dbTF-activity and transcription IBAs that propagate to ste11 are flagged CROSS_SUBFAMILY but are **CORRECT** and were ACCEPTed — the conserved HMG-box dbTF function transfers across these fine subfamilies even though the downstream target-gene programs differ.

## Subfamily Analysis

### PTHR45803:SF1 - TRANSCRIPTION FACTOR SOX-9
**Members**: 13 proteins (largest subfamily)

**Key Members**: *Homo sapiens* SOX9 (P48436); *Mus musculus* Sox9 (Q04887); *Rattus* Sox9 (F1LYL9); *Sus scrofa* SOX9 (O18896); *Gallus* SOX9 (P48434); *Xenopus laevis* sox9-a (B7ZR65), sox9-b (Q6DFF5); *X. tropicalis* sox9 (Q6F2E7); primate orthologs (P61753, P61754, Q9BG89, Q9BG91); *Canis* SOX9 (Q7YRJ7).

**Function**: SoxE-group HMG-box transcription factor; chondrogenesis and sex determination. This subfamily provides the strongest IBA seeds (e.g. human SOX9 P48436).

### PTHR45803:SF6 - TRANSCRIPTION FACTOR SOX-10
**Members**: 7 proteins

**Key Members**: *Homo sapiens* SOX10 (P56693); *Mus musculus* Sox10 (Q04888); *Rattus* Sox10 (O55170); *Sus scrofa* SOX10 (A5A763); *Gallus* SOX10 (Q9W757); *Xenopus* sox10 (A4IIJ8, Q8AXX8).

**Function**: SoxE-group HMG-box transcription factor; neural-crest and glial/myelination programs.

### PTHR45803:SF2 - TRANSCRIPTION FACTOR SOX-8
**Members**: 5 proteins

**Key Members**: *Homo sapiens* SOX8 (P57073); *Gallus* SOX8 (P57074); *Mus musculus* Sox8 (Q04886); *Xenopus laevis* sox8 (Q6VVD7); *Tetraodon* sox8 (Q6IZ48).

**Function**: Third SoxE-group paralog; overlapping HMG-box dbTF function with SOX9/SOX10.

### PTHR45803:SF5 - SOX100B (ANCHOR SUBFAMILY)
**Members**: 1 protein in the sampled set - the anchor itself.

This is the subfamily of the S. pombe anchor gene **ste11 (P36631)**, confirmed by `DR PANTHER; PTHR45803:SF5; SOX100B`. The "SOX100B" label is the Drosophila SoxE-related naming; ste11 is the fission-yeast representative that PANTHER co-locates here. Despite the distant placement from the vertebrate SoxE subfamilies, ste11 is a bona fide HMG-box transcription factor: it binds T-rich TR-box elements (TTCTTTGTTY), bends DNA, and activates transcription of mating/meiosis genes.

## IBA Annotation Assessment

Ste11 receives the following IBA (GO_REF:0000033, PANTHER node PTN002910095) annotations. All four were **ACCEPTed** in the ste11 review. The seeds are vertebrate SoxE factors (e.g. SOX9 P48436, mouse Sox8/9/10 MGI:98358/98370/98371) from SF1/SF2/SF6 — hence the CROSS_SUBFAMILY flag — together with PomBase:SPBC32C12.02.

| GO ID | Label | Aspect | Flags | Our action | Assessment |
|-------|-------|--------|-------|------------|------------|
| GO:0000981 | DNA-binding transcription factor activity, RNA polymerase II-specific | MF | CROSS_SUBFAMILY | ACCEPT | Correct and core. CROSS_SUBFAMILY here is triage, not a verdict: the HMG-box dbTF activity is conserved across these SOX subfamilies, and ste11 is experimentally a sequence-specific Pol II transcription factor. |
| GO:0000978 | RNA polymerase II cis-regulatory region sequence-specific DNA binding | MF | CROSS_SUBFAMILY | ACCEPT | Correct. Ste11 binds sequence-specifically to TR-box cis-regulatory elements; transfers soundly despite the fine-subfamily difference. |
| GO:0006357 | regulation of transcription by RNA polymerase II | BP | CROSS_SUBFAMILY | ACCEPT | Correct. Ste11 regulates Pol II transcription of sexual-development genes (activator). |
| GO:0005634 | nucleus | CC | CROSS_SUBFAMILY; LOCALIZATION | ACCEPT | Correct. Ste11 is a nuclear (nucleocytoplasmic-shuttling) transcription factor that accumulates in the nucleus on starvation/pheromone signaling; localization is experimentally supported. |

**CROSS_SUBFAMILY assessment**: This family is the calibration example for treating CROSS_SUBFAMILY as **triage rather than verdict**. All four ste11 IBAs are flagged CROSS_SUBFAMILY because the seeds come from the vertebrate SoxE subfamilies (SF1/SF2/SF6) while ste11 sits in SF5 (SOX100B). However, the transferred terms describe the **conserved HMG-box transcription-factor function**, which ste11 genuinely possesses — confirmed by direct S. pombe experiments (TR-box binding/bending, activation of mei2 and mating genes). These are therefore CORRECT and accepted. What is *not* shared across the subfamilies are the organism-specific target-gene programs (vertebrate chondrogenesis/neural-crest vs. fission-yeast mating/meiosis); no such process-specific term was over-transferred to ste11.

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER family metadata/members, UniProt, the ste11 gene review (genes/SCHPO/ste11), and the PANTHER IBA propagation table.
