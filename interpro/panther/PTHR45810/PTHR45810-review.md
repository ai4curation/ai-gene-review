# PANTHER Family Review: PTHR45810

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR45810 |
| **Family Name** | HISTONE H3.2 (members are CENP-A / CenH3 centromeric H3 variants) |
| **InterPro Entry** | IPR000164 (Histone H3 signature) |
| **Total Proteins** | 3,924 |
| **Taxonomic Breadth** | 6,818 taxa |
| **Subfamilies** | 8 |
| **Representative Structure** | (none recorded) |

## Executive Summary

PTHR45810 carries the PANTHER name "HISTONE H3.2," but its characterized members are overwhelmingly **CENP-A / CenH3 — the centromere-specific histone H3 variant** that replaces canonical H3 in centromeric nucleosomes and epigenetically defines centromere identity. The family's subfamilies (SF1, SF14, SF17, etc.) all correspond to CENP-A/CenH3 orthologs across fungi, plants, protists and animals (human/mouse CENPA, S. cerevisiae CSE4, Arabidopsis CENH3, Drosophila cid). The shared molecular function is **structural constituent of (centromeric) chromatin / nucleosomal DNA binding**, and the shared biology is **centromere/kinetochore specification and assembly**.

The S. pombe anchor gene, **cnp1** (Q9Y812), is the fission-yeast CENP-A (CenH3), placed in subfamily **PTHR45810:SF1 (HISTONE H3-LIKE CENTROMERIC PROTEIN A)** by its UniProt cross-reference. Because the entire family is CENP-A, the core MF (chromatin structural constituent, nucleosomal DNA binding) and the CENP-A-specific BP terms (kinetochore assembly, CENP-A nucleosome / kinetochore localization) transfer well to cnp1. "Kinetochore assembly" is a CENP-A-specific function and is correct for cnp1 even though one of its seeds is in a different fine subfamily. The main caveat is heterochromatin-related process terms, which were judged over-annotations for cnp1.

## Subfamily Analysis

### PTHR45810:SF1 - HISTONE H3-LIKE CENTROMERIC PROTEIN A (ANCHOR SUBFAMILY)
**Members**: 10 proteins (largest subfamily)

This is the subfamily of the S. pombe anchor gene **cnp1 (Q9Y812)**, confirmed by `DR PANTHER; PTHR45810:SF1; HISTONE H3-LIKE CENTROMERIC PROTEIN A`.

**Key Members**:
- *S. pombe* cnp1 (Q9Y812) - anchor; CENP-A/CenH3
- *Gallus gallus* CENPA (Q6XXM1)
- *Arabidopsis thaliana* CENH3/HTR12 (Q8RVQ9); *Lilium longiflorum* gH3 (Q9MBF6)
- Fungal CSE4/CenH3: *Yarrowia lipolytica* (Q6CER9), *Millerozyma farinosa* (Q0MXD1)
- *Neurospora crassa* hH3v (Q7RXR3)
- *Tetrahymena thermophila* CNA1 (Q2N2K6); *Dictyostelium* H3v1 (Q54F38)
- *Encephalitozoon cuniculi* ECU09_0450 (Q8SQP3)

**Function**: Centromere-specific histone H3 variant; structural constituent of centromeric chromatin and epigenetic mark of centromere identity.

### PTHR45810:SF14 - CENTROMERE PROTEIN A (vertebrate CENPA)
**Members**: 4 proteins

**Key Members**: *Homo sapiens* CENPA (P49450); *Mus musculus* Cenpa (O35216); *Bos taurus* CENPA (P49449); *Cricetulus griseus* CENPA (Q8R565).

**Function**: Vertebrate CENP-A. This is the subfamily that seeds the "kinetochore assembly" IBA propagated to cnp1 (via UniProtKB:P49450) — a CENP-A-specific function shared with cnp1.

### PTHR45810:SF17 - HISTONE H3-LIKE CENTROMERIC PROTEIN A (fungal/amphibian/fish CSE4-CenH3 clade)
**Members**: 7 proteins

**Key Members**: *Xenopus* cenpa (Q28I31, Q569M3); *Danio rerio* cenpa (Q803H4); *Kluyveromyces lactis* CSE4 (Q6CTI2), *K. marxianus* CSE4 (Q0MTC0); *Candida glabrata* CSE4 (Q874J6); *C. briggsae* CBG10032 (A8XA80).

**Function**: Additional CENP-A/CSE4 orthologs; same centromeric-chromatin function.

### Unassigned / other CENP-A members
Several well-known CENP-A orthologs are present without a sampled subfamily label, including *S. cerevisiae* CSE4 (P36012), *Drosophila* cid (Q9V6Q2), and *C. elegans* cpar-1 (P34440) — all CENP-A/CenH3 proteins, underscoring that the family is functionally homogeneous (CENP-A) despite the "Histone H3.2" PANTHER label.

## IBA Annotation Assessment

Cnp1 receives the following IBA (GO_REF:0000033) annotations from several PANTHER nodes (PTN008967730, PTN008517672, PTN008320273). Seeds include canonical CENP-A orthologs (e.g. human CENPA P49450, and canonical H3 P68431/P84233/P84243 for the generic chromatin terms).

| GO ID | Label | Aspect | Flags | Our action | Assessment |
|-------|-------|--------|-------|------------|------------|
| GO:0030527 | structural constituent of chromatin | MF | (none) | ACCEPT | Correct and core. CENP-A is a structural component of centromeric nucleosomes; this is the principal molecular activity. Well-seeded. |
| GO:0031492 | nucleosomal DNA binding | MF | (none) | ACCEPT | Correct. As a histone variant, cnp1 binds nucleosomal DNA; transfers soundly. |
| GO:0051382 | kinetochore assembly | BP | CROSS_SUBFAMILY | ACCEPT | Correct despite CROSS_SUBFAMILY flag. Kinetochore assembly is a CENP-A-specific function; the seed (vertebrate CENPA, SF14, UniProtKB:P49450) is in a different fine subfamily but the same CENP-A function — cnp1 is experimentally required for inner-kinetochore assembly. Triage flag, correct verdict. |
| GO:0000776 | kinetochore | CC | LOCALIZATION; NO_UNIPROT_SEEDS | ACCEPT | Correct. CENP-A defines the kinetochore-assembly site; localization term is consistent with CENP-A biology. |
| GO:0043505 | CENP-A containing nucleosome | CC | LOCALIZATION; NO_UNIPROT_SEEDS | ACCEPT | Correct and CENP-A-specific by definition; the appropriate compartment for cnp1. |
| GO:0007080 | mitotic metaphase chromosome alignment | BP | NO_UNIPROT_SEEDS | KEEP_AS_NON_CORE | Downstream consequence of centromere function rather than a direct molecular role; retained as non-core. |
| GO:0031507 | heterochromatin formation | BP | NO_UNIPROT_SEEDS | MARK_AS_OVER_ANNOTATED | Over-annotation for cnp1. CENP-A occupies the nonrepetitive central core, not the flanking pericentromeric heterochromatin; heterochromatin formation in S. pombe is driven by H3K9 methylation/RNAi machinery, not by CENP-A. Flagged as over-annotated with a positive biological argument. |

**CROSS_SUBFAMILY assessment**: The one CROSS_SUBFAMILY-flagged term (kinetochore assembly, seeded from vertebrate CENPA in SF14) is CORRECT for cnp1 — the function is CENP-A-specific and conserved, so the flag is triage only. The localization CC terms are all CENP-A-appropriate. The only term rejected is heterochromatin formation (MARK_AS_OVER_ANNOTATED), on the biological grounds that cnp1/CENP-A acts at the central core domain and heterochromatin assembly is a separate, RNAi/H3K9me-dependent process; metaphase chromosome alignment is kept as a non-core downstream term.

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER family metadata/members, UniProt, the cnp1 gene review (genes/SCHPO/cnp1), and the PANTHER IBA propagation table.
