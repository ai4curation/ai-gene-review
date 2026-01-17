# STAT3 GO Annotation Review Summary

## Overview
Completed comprehensive systematic review of 456 existing GO annotations for human STAT3 (UniProt P40763).

## Gene Function Summary
STAT3 (Signal transducer and activator of transcription 3) is a latent cytoplasmic transcription factor that is activated by tyrosine phosphorylation (Tyr705) in response to cytokines and growth factors. Upon phosphorylation by JAK kinases, STAT3 forms dimers via reciprocal SH2 domain-phosphotyrosine interactions, translocates to the nucleus, binds DNA at GAS elements, and regulates transcription of target genes.

## Curation Actions Applied

### Summary Statistics
- **Total annotations reviewed**: 456
- **ACCEPT**: 364 (79.8%)
- **KEEP_AS_NON_CORE**: 26 (5.7%)
- **REMOVE**: 66 (14.5%)

### Key Decisions

#### ACCEPTED (364 annotations)
Core functions representing STAT3's essential role as a JAK-STAT transcription factor:

**Molecular Functions:**
- DNA-binding transcription factor activity (GO:0000981, GO:0003700)
- RNA polymerase II cis-regulatory region sequence-specific DNA binding (GO:0000978)
- DNA binding (GO:0003677)
- Transcription activator activity (GO:0001228)
- Protein homodimerization activity (GO:0042803) - essential SH2-mediated dimerization
- Heterodimerization activity (GO:0046983) - with other STAT family members

**Biological Processes:**
- Cell surface receptor signaling pathway via JAK-STAT (GO:0007259) - core pathway
- Cytokine-mediated signaling pathway (GO:0019221) - canonical activation
- Interleukin-6-mediated signaling pathway (GO:0070106) - canonical IL-6/JAK/STAT3 axis
- Regulation of transcription by RNA polymerase II (GO:0006357, GO:0045944)
- Astrocyte differentiation (GO:0048708) - **relevant to NEURON_DEVELOPMENT project**
- Glial cell differentiation (GO:0014013)

**Cellular Components:**
- Nucleus (GO:0005634) - localization after activation
- Cytoplasm (GO:0005737) - localization of latent STAT3
- Cytosol (GO:0005829) - latent form
- Nucleoplasm (GO:0005654) - activated dimers
- Mitochondrion (GO:0005739) - mitoSTAT3 non-canonical functions

#### KEPT AS NON-CORE (26 annotations)
Valid but peripheral to core transcription factor function:

**Pleiotropic Effects:**
- Defense response (GO:0006952)
- Immune response (GO:0006955)
- Cell proliferation regulation (GO:0042127) - downstream effect of target genes

**Specific Pathways (not defining):**
- Leptin-mediated signaling pathway (GO:0033210)
- Growth hormone receptor signaling via JAK-STAT (GO:0060397)
- Response to peptide hormone (GO:0043434)

**Downstream Organismal Effects:**
- Positive regulation of multicellular organismal process (GO:0051240)
- Angiogenesis (GO:0001525) - via VEGF target gene
- Wound healing (GO:0042060)

**Immune Cell Differentiation:**
- T-helper 17 cell lineage commitment (GO:0072540)

#### REMOVED (66 annotations)
**All instances of generic "protein binding" (GO:0005515)**
- Rationale: Uninformative generic term per GO curation guidelines
- STAT3 has specific protein interactions better represented by:
  - Homodimerization (GO:0042803)
  - Heterodimerization (GO:0046983)
  - Kinase binding (GO:0019904)
- Removed from all 66 IPI annotations with various PMIDs

## Core Functions Defined

1. **DNA-binding transcription factor activity** (GO:0000981)
   - Binds GAS elements in target gene promoters

2. **Protein homodimerization activity** (GO:0042803)
   - SH2-pY705 reciprocal interactions essential for activation

3. **JAK-STAT signaling pathway** (GO:0007259)
   - Activated by JAK kinases downstream of cytokine receptors

4. **IL-6-mediated signaling pathway** (GO:0070106)
   - Canonical STAT3-activating pathway
   - IL-6 → IL-6Rα/gp130 → JAKs → pY705-STAT3 → dimerization → nucleus → transcription

5. **Astrocyte differentiation** (GO:0048708)
   - Promotes gliogenesis during neural development
   - Relevant to NEURON_DEVELOPMENT project

## Key Supporting Evidence
All annotations reference: `file:human/STAT3/STAT3-deep-research-falcon.md`

Key findings from deep research:
- Canonical IL-6–JAK–STAT3 pathway well-established
- Y705 phosphorylation essential for dimerization and nuclear translocation
- S727 phosphorylation modulates transcriptional activity and mitochondrial functions (mitoSTAT3)
- SH2 domain mediates critical protein-protein interactions
- Target genes include MYC, CCND1, BCL-XL, BCL2, MCL1, VEGFA
- Negative feedback via SOCS3 and phosphatases (PTP1B, SHP-1/2)

## Localization Context
Both cytoplasm and nucleus localizations are CORRECT:
- **Cytoplasm**: Latent unphosphorylated STAT3 before activation
- **Nucleus**: Activated phosphorylated STAT3 dimers for transcription
- **Mitochondrion**: mitoSTAT3 for non-canonical metabolic functions

## Notes on Evidence Codes
- **IBA annotations**: Generally well-curated phylogenetic inferences, mostly accepted
- **IEA annotations**: Computational predictions, reviewed for specificity
- **IPI annotations** for protein binding: All removed (generic term)
- **IDA/IMP/IGI annotations**: Experimental evidence, accepted
- **ISS annotations**: Sequence/structure similarity inferences, accepted for conserved functions

## Review Status
**COMPLETE** - All 456 annotations systematically reviewed with specific rationales and supporting references.

## Files Updated
- `/Users/cjm/repos/ai-gene-review/genes/human/STAT3/STAT3-ai-review.yaml` (5140 lines)
- Status: COMPLETE
- Aliases added: APRF, Acute-phase response factor
- Core functions section added (5 entries)
