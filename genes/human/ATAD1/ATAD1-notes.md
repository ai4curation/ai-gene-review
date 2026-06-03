# ATAD1 Notes

## 2026-06-03 Proteostasis PN review

Falcon deep research was attempted with the required `perplexity-lite` fallback.
Falcon timed out after 600 seconds and the fallback failed with a Perplexity API
quota error, so this review uses cached primary evidence, UniProt, Reactome, and
the local PN projection reports rather than a generated Falcon research artifact.

ATAD1 is a strong fit for the mitochondrial proteostasis batch, but the safest
core term remains the existing specific process `GO:0140570` extraction of
mislocalized protein from mitochondrial outer membrane. The direct ATAD1/Msp1
paper says human ATAD1 limits mitochondrial mislocalization of PEX26 and GOS28
and proposes ATAD1/Msp1 as mitochondrial protein quality-control factors that
promote extraction and degradation of mislocalized tail-anchored proteins
[PMID:24843043 "human ATAD1 limits the mitochondrial mislocalization of PEX26
and GOS28"; PMID:24843043 "promote the extraction and degradation of
mislocalized TA proteins"].

The PN projection report proposes `GO:0035694` mitochondrial protein catabolic
process for ATAD1 from
`Mitochondrial proteostasis|Organelle-specific protein degradation|mitoCPR
pathway`. This is a class-level propagation, and the mapping audit flags this
source as requiring manual gene-level review before changing a review. I accepted
the projected term only as a broad `NEW` candidate because PMID:24843043 supports
degradation as the downstream outcome, not because the PN source alone is
sufficient. I used TAS rather than IMP for this candidate because the cached
paper text supports a traceable degradation claim, while the explicit
protein-level knockout evidence available in the cached abstract is from mouse
tissue. It should not replace `GO:0140570`, which is the sharper mechanism.

Peroxisomal membrane localization is retained as non-core. UniProt reports
peroxisome membrane localization and Reactome lists ATAD1 as a class I
peroxisomal membrane protein bound by PEX19, but the current evidence does not
establish peroxisomal substrate extraction as ATAD1's primary function
[file:human/ATAD1/ATAD1-uniprot.txt "Peroxisome membrane";
Reactome:R-HSA-9603804 "ATAD1 (Liu et al. 2016)"].

The synaptic/behavioral block is treated conservatively. UniProt summarizes
mouse-derived AMPAR trafficking, synaptic plasticity, learning, and memory
biology by similarity, and human ATAD1 encephalopathy provides disease context
[file:human/ATAD1/ATAD1-uniprot.txt "Required for NMDA-stimulated AMPAR
internalization"; PMID:29659736 "ATAD1 encephalopathy and stiff baby syndrome"].
I kept postsynaptic/receptor-internalization terms as non-core and marked the
high-level learning/memory annotations as over-annotations.
