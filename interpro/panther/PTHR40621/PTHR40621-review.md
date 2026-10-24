# PANTHER Family Review: PTHR40621

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR40621 |
| **Official PANTHER Name** | TRANSCRIPTION FACTOR KAPC-RELATED |
| **InterPro Entry** | IPR050936 |
| **Cached InterPro counters** | 11,010 protein matches; 3,258 taxon records |
| **Cached InterPro subfamily counter** | 6 |
| **Representative Structure** | 1gd2 (Crystal structure of bZIP transcription factor Pap1 bound to DNA) |

## Executive Summary

PTHR40621 is a broad bZIP transcription-factor family. It must not be summarized as a
uniformly fungal, redox-regulated YAP family: the cached PAINT root node PTN000894784 is
taxonomically eukaryotic and is seeded by metazoan AP-1 factors, whereas pap1's three IBAs
come from the shallower fungal node PTN008082960. The cached InterPro metadata description
is explicitly LLM-generated and unchecked, so it is not used as evidence for family-wide
biological claims.

The *S. pombe* anchor gene **pap1** (Q01663) is a structurally characterized member (PDB
1gd2) of **PTHR40621:SF6 (AP-1-LIKE TRANSCRIPTION FACTOR YAP1-RELATED)**. The reviewed-entry
cache places *S. cerevisiae* Yap proteins, Candida Cap1/AP1, and several filamentous-fungal
Yap1-like proteins in the same subfamily. This supports transfer of general DNA-binding
transcription-activator functions at PTN008082960. It does not establish that every family
member shares pap1's peroxide relay, Crm1-regulated localization, target genes, or specific
stress-response program.

## Subfamily Analysis

### PTHR40621:SF6 - AP-1-LIKE TRANSCRIPTION FACTOR YAP1-RELATED (ANCHOR SUBFAMILY)

**Reviewed representatives in the cache**: 16 proteins. This is not a complete subfamily
membership count.

This is the subfamily containing the S. pombe anchor gene **pap1 (Q01663)**, confirmed by its UniProt cross-reference `DR PANTHER; PTHR40621:SF6`.

**Key Members**:
- *S. pombe* pap1 (Q01663) - anchor; redox-regulated oxidative-stress / MDR activator
- *S. cerevisiae* YAP1 (P19880), CAD1/YAP2 (P24813), CIN5/YAP4 (P40917), YAP5 (P40574), YAP6 (Q03935), YAP7 (Q08182), ARR1/YAP8 (Q06596)
- *K. lactis* YAP1 (P56095)
- *Candida albicans* CAP1 (Q5AJU7); *Candida glabrata* AP1 (Q6FRZ8)
- *Aspergillus* spp. yap1 (B8NNN3, Q2UMT9, Q4WMH0); *A. nidulans* napA (Q5AW17)
- *Cryptococcus neoformans* yap1 (J9VEC2)

**Function supported for pap1 and close characterized representatives**: Sequence-specific
AP-1/TRE-like DNA-binding transcription-factor activity. The reviewed slice aggregates a
budding-yeast YAP paralog set with distinct stress and metal-regulatory programs, so redox
control and specific regulons must not be projected across all descendants.

### PTHR40621:SF11 - TRANSCRIPTION FACTOR KAPC-RELATED

**Reviewed representatives in the cache**: 7 proteins.

**Taxonomy**: Aspergillus / Eurotiomycete filamentous fungi.

**Key Members**: *A. clavatus* kapC (A1C9M5), *Neosartorya fischeri* kapC (A1D9Z7), *A. niger* kapC (A2R346).

**Function**: bZIP transcription factors; this clade lends the family its overall PANTHER name component. Functional details are less characterized than the Yap1/Pap1 clade.

### PTHR40621:SF8 - AP-1-LIKE TRANSCRIPTION FACTOR YAP3

**Reviewed representatives in the cache**: 2 proteins.

**Function**: A YAP3-type AP-1-like clade; bZIP transcription factor.

### PTHR40621:SF7 - BZIP DOMAIN-CONTAINING PROTEIN (includes hapX-like members)

**Reviewed representatives in the cache**: 2 proteins.

**Key Members**: *Arthroderma benhamiae* hapX (D4AQY2). HapX-type bZIP factors are iron-responsive regulators in fungi, illustrating subfunctionalization within the broader family toward metal/iron homeostasis.

## IBA Annotation Assessment

Pap1 receives the following IBA (GO_REF:0000033, PANTHER node PTN008082960) annotations. All three were **ACCEPTed** in the pap1 review.

| GO ID | Label | Aspect | Flags | Our action | Assessment |
|-------|-------|--------|-------|------------|------------|
| GO:0000976 | transcription cis-regulatory region binding | MF | NO_UNIPROT_SEEDS | ACCEPT | Correct. Pap1 binds AP-1/TRE-like cis-regulatory elements (TTACGTAA) experimentally. A more specific term (GO:0000978) better captures the activity, but the IBA is not wrong. |
| GO:0001228 | DNA-binding transcription activator activity, RNA polymerase II-specific | MF | NO_UNIPROT_SEEDS | ACCEPT | Correct and core. Pap1 is a sequence-specific Pol II transcriptional activator; this is the defining molecular function of the YAP subfamily and transfers soundly across SF6. |
| GO:0090575 | RNA polymerase II transcription regulator complex | CC | LOCALIZATION; NO_UNIPROT_SEEDS | ACCEPT | Acceptable. As an activator, Pap1 acts within the Pol II transcription regulator machinery; this is a localization-type term but is biologically consistent with the well-supported MF. |

**CROSS_SUBFAMILY risk**: None of pap1's IBAs are flagged CROSS_SUBFAMILY; all three descend
from fungal node PTN008082960. The `NO_UNIPROT_SEEDS` flag reflects that the supporting
descendant evidence is represented by PomBase/SGD/CGD identifiers (including pap1 itself),
not that the PAINT judgment lacks experimental grounding. The target's appearance among the
IBD descendants is expected and is not circular.

**Paralog caveat (curatorial note)**: Within the reviewed fungal SF6 slice, general dbTF /
cis-regulatory-binding terms are shared, but *paralog-specific biological processes* and
specific target/stress programs do not transfer cleanly — e.g. iron regulation (Yap5/Yap7),
arsenic resistance (Arr1/Yap8), or pap1's particular oxidative-stress and
multidrug-resistance regulons. IBA propagation of such process-specific terms beyond the
actual PTN008082960 node should be scrutinized; no corresponding claim is made for all of
PTHR40621.

## Review Status

- **Date**: 2026-09-01
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER family metadata/members, UniProt, the pap1 gene review (genes/SCHPO/pap1), and the PANTHER IBA propagation table.
