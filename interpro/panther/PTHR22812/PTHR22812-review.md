# PANTHER Family Review: PTHR22812

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR22812 |
| **Family Name** | Heterochromatin-associated chromo domain-containing protein (CHROMOBOX PROTEIN) |
| **InterPro Entry** | IPR051219 |
| **Total Proteins** | 14,304 |
| **Taxonomic Breadth** | 8,079 taxa |
| **Subfamilies** | 13 |
| **Representative Structure** | 6mha (Drosophila HP1 chromodomain bound to H3K9me3 peptide) |

## Executive Summary

PTHR22812 is the **HP1 (Heterochromatin Protein 1) / chromobox family of heterochromatin-associated chromodomain proteins**. The canonical architecture is an **N-terminal chromodomain** that reads methylated histone H3 Lys9 (H3K9me2/me3) joined by a flexible hinge to a **C-terminal chromoshadow domain** that homodimerizes and forms a protein-protein interaction platform. By binding H3K9me nucleosomes and oligomerizing, these proteins compact chromatin and recruit downstream effectors, mediating **transcriptional gene silencing and heterochromatin formation/spreading** at centromeres, telomeres, silent mating-type loci and other repressed domains.

The **conserved core function across the family is H3K9-methyl chromatin binding (chromodomain reader) coupled to heterochromatin formation**. Family members include the mammalian HP1 isoforms (CBX1/HP1β, CBX3/HP1γ, CBX5/HP1α), *Drosophila* HP1a/Su(var)205, and the fission-yeast HP1 proteins Swi6 and Chp2. The family also contains chromodomain proteins that have **subfunctionalized** away from the canonical HP1 role - notably *S. pombe* Chp1 (the chromodomain subunit of the RITS RNAi-silencing complex) and the *Drosophila* Rhino (piRNA-pathway HP1 variant) and *C. elegans* chromobox/cec proteins.

The fission yeast anchor **swi6 (P40381)** is the principal *S. pombe* HP1 ortholog and the central H3K9me reader/effector of heterochromatin.

## Subfamily Analysis

**Note on subfamily assignment**: In the curated reference set for PTHR22812, the `subfamily` / `subfamily_name` columns are not populated for any of the 18 reference proteins, and the *S. pombe* swi6 UniProt record carries only the family-level `DR PANTHER; PTHR22812; CHROMOBOX PROTEIN` annotation **without an :SFn subfamily**. The iba_propagation analysis accordingly flags swi6 as `GENE_NO_SUBFAMILY`. Members below are therefore grouped by orthology/function; the anchor's "subfamily" is the family node itself (PTN000517042).

### HP1 / chromobox core group (incl. ANCHOR)
**Key Members**:
- ***S. pombe* swi6 (P40381) - the anchor gene** (HP1 ortholog)
- *S. pombe* chp2 (O42934, Chromo domain-containing protein 2; the second fission-yeast HP1)
- Human CBX5/HP1α (P45973), CBX1/HP1β (P83916), CBX3/HP1γ (Q13185)
- Mouse Cbx1 (P83917), Cbx3 (P23198), Cbx5 (Q61686); Orangutan CBX3 (Q5R6X7)
- *Drosophila* HP1/Su(var)205 (P05205), *D. virilis* HP1A (P29227)
- *Cryptococcus* SWI6 (J9VQZ0)
- *C. elegans* hpl-1 (G5EET5), hpl-2 (G5EDE2)

**Function**: Canonical HP1 - chromodomain reads H3K9me; chromoshadow domain dimerizes and recruits effectors; drives heterochromatin formation, spreading and silencing.

### Specialized / subfunctionalized chromodomain members
**Key Members**:
- *S. pombe* chp1 (Q10103, 960 aa) - chromodomain subunit of the **RITS** RNAi complex (much larger, RNAi-pathway-specialized)
- *Drosophila* Rhino (Q7JXA8) - HP1 variant of the **piRNA** pathway
- *C. elegans* cec-1 (P34618), cec-3 (P45968) - chromodomain proteins

**Function**: Chromodomain readers diverged from the core HP1 silencing role into RNAi/piRNA and other chromatin pathways - a clear case of **paralog subfunctionalization** within the family.

**Caveat (paralog awareness)**: Per review guidance, swi6 is an HP1-family chromodomain protein with *S. pombe* paralogs. Within **this** PANTHER family the relevant paralogs are **chp2** (also a canonical HP1, shares heterochromatin functions) and **chp1** (RNAi/RITS-specialized). The H3K9-methyltransferase **Clr4** is **not** a member of PTHR22812 (it is an enzyme in a different family), so there is no risk of methyltransferase functions being propagated here. The IBA terms assessed below are generic HP1-reader/heterochromatin functions, conserved between swi6, chp2 and metazoan HP1 - not chp1-specific RNAi functions - so paralog-specific mis-transfer is not occurring.

## Functional Diversity Assessment

### Neo-functionalization: MODERATE
The chromodomain H3K9me-reading and heterochromatin-association core is conserved across the canonical HP1 members (swi6, chp2, CBX1/3/5, HP1a). Divergence is seen in the specialized members (chp1→RITS/RNAi; Rhino→piRNA), which retain the chromodomain fold but act in distinct chromatin pathways. swi6 itself is firmly within the canonical HP1 group.

## IBA Annotation Assessment

IBA annotations (GO_REF:0000033, node PTN000517042) propagated to swi6 (P40381). All carry `GENE_NO_SUBFAMILY` (swi6 has no :SFn assignment; propagation is from the family node).

| GO ID | Label | Aspect | Flags | Assessment |
|-------|-------|--------|-------|------------|
| GO:0031507 | heterochromatin formation | BP | GENE_NO_SUBFAMILY | **APPROPRIATE.** Defining, conserved HP1-family function and swi6's curated core role (assembly/spreading of heterochromatin). Seeded by 2 in-family proteins. |
| GO:0003682 | chromatin binding | MF | GENE_NO_SUBFAMILY; NO_UNIPROT_SEEDS | **APPROPRIATE but non-informative.** swi6 binds H3K9me chromatin via its chromodomain; "chromatin binding" is correct but general. The project marks this KEEP_AS_NON_CORE in favor of the more specific methyl-H3K9 reader description. Not an error - just low specificity. |
| GO:0005721 | pericentric heterochromatin | CC | LOCALIZATION; GENE_NO_SUBFAMILY; NO_UNIPROT_SEEDS | **APPROPRIATE.** swi6 localizes to pericentromeric heterochromatin (where it enriches cohesin for chromosome segregation); the localization transfer is consistent with established *S. pombe* biology. No conflict. |

**Summary**: All three propagations are biologically appropriate for swi6 and match its curated function/localization. They are exactly the generic HP1-reader and heterochromatin terms shared across the canonical HP1 members (swi6, chp2, metazoan CBX/HP1) - **not** chp1-specific RNAi/RITS functions, so the paralog caveat does not require any down-ranking. The `GENE_NO_SUBFAMILY` flag reflects missing fine-grained subfamily structure rather than an error. Following the do-not-overrule principle, all IBA propagations to swi6 are endorsed.

## Key Literature

| PMID | Key Finding |
|------|-------------|
| PMID:11242054 | HP1 chromodomain binds H3K9me with high affinity (the methyl-lysine reader). |
| PMID:10801440 | Chromoshadow-domain dimerization creates a protein-interaction "pit". |
| PMID:23485968 | Swi6 binding to methylated nucleosomes switches it from auto-inhibited to spreading-competent. |
| PMID:11780129 | Cohesin subunit Psc3 interacts with Swi6/HP1. |
| PMID:16762840 | Epe1 recruited to heterochromatin by Swi6/HP1. |

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER PTHR22812 metadata/entries, UniProt (P40381), swi6 ai-review, GOA IBA annotations, iba_propagation.tsv
