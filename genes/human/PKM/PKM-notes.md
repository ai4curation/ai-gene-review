# PKM (Pyruvate Kinase M) Notes - ISOFORMS Project

## Key Isoform Biology

PKM encodes pyruvate kinase isoforms with **fundamentally different metabolic properties** - the M1/M2 switch is a hallmark of the Warburg effect in cancer.

### Critical Isoforms: M1 vs M2

| Isoform | UniProt ID | Synonym | Activity | Regulation | Expression |
|---------|------------|---------|----------|------------|------------|
| **PKM1** | P14618-2 | M1-PK | HIGH constitutive | Not allosteric | **ADULT muscle, brain, heart** |
| **PKM2** | P14618-1 | M2-PK | LOW basal, activatable | Allosteric (FBP) | **EMBRYONIC, proliferating, CANCER** |

### The M1/M2 Splice Switch

Alternative splicing of mutually exclusive exons 9 and 10:
- **Exon 9** → PKM1 (adult)
- **Exon 10** → PKM2 (embryonic/cancer)

Controlled by hnRNP splicing factors (hnRNPA1, hnRNPA2, PTB).

### Functional Differences

**PKM1 (isoform 2):**
- Constitutively active homotetramer
- High pyruvate kinase activity
- Efficient ATP generation via glycolysis
- Normal oxidative metabolism

**PKM2 (isoform 1):**
- Allosterically regulated by fructose-1,6-bisphosphate (FBP)
- Can exist as inactive monomer/dimer or active tetramer
- LOW activity allows glycolytic intermediates to accumulate
- Supports biosynthetic pathways (nucleotides, amino acids, lipids)
- **Nuclear translocation**: Can act as transcription coactivator

### The Warburg Effect

Cancer cells switch from PKM1 to PKM2:
- LOW PKM2 activity → glycolytic intermediates diverted to biosynthesis
- Supports rapid proliferation
- PKM2 is nearly universal in cancer

### PKM2 Non-Metabolic Functions

PKM2 has functions ABSENT from PKM1:
- **Protein kinase activity** - phosphorylates histones (H3Y11)
- **Transcription coactivation** - interacts with HIF-1α
- **Nuclear functions** - regulates gene expression

## GOA Annotation Status

- **88 annotations fetched, 79 seeded**
- UniProt has extensive isoform-specific functional annotations

## Expected Annotation Issues

1. **"Pyruvate kinase activity"** - TRUE for both but M1 >> M2 activity
2. **"Protein kinase activity"** - PKM2 ONLY, not PKM1
3. **"Nucleus"** localization - PKM2 ONLY
4. **"Transcription coactivator activity"** - PKM2 ONLY
5. **"Glycolytic process"** - both, but different flux
6. Any Warburg effect annotations should be PKM2-specific

## Key References

- PMID:17308100 - M2-PK in cancer
- PMID:22056988 - PKM2 phosphorylates histone H3
- UniProt P14618 has extensive isoform-specific annotations
