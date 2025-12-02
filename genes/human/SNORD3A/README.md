# SNORD3A Gene Review

## Gene Type: Non-Coding RNA (snoRNA)

**IMPORTANT**: SNORD3A is a **non-coding RNA** (specifically, a C/D box small nucleolar RNA), not a protein-coding gene.

## Why Standard Files Don't Apply

### Missing Files Explained:

1. **SNORD3A-uniprot.txt** - ❌ Not applicable
   - UniProt only contains protein sequences
   - snoRNAs do not have UniProt entries
   - **Equivalent**: `SNORD3A-rnacentral.json` (115KB) contains ncRNA-specific annotation from RNAcentral database

2. **SNORD3A-goa.tsv** - ❌ Not applicable
   - GOA (Gene Ontology Annotation) files from QuickGO are generated primarily for proteins
   - ncRNAs typically lack pre-existing GO annotations in standard GOA datasets
   - **Alternative**: GO annotations are curated de novo in the `existing_annotations` section of the YAML file with action: NEW

### What We Have Instead:

| Standard File | ncRNA Equivalent | Status |
|--------------|------------------|--------|
| `*-uniprot.txt` | `SNORD3A-rnacentral.json` | ✅ Present (115KB) |
| `*-goa.tsv` | `existing_annotations` in YAML | ✅ Present (4 annotations) |
| `*-deep-research-*.md` | `SNORD3A-deep-research-perplexity.md` | ✅ Present (8.0KB) |

## Review Completeness

This review is **100% complete** for an ncRNA gene:

### Files Present:
- ✅ `SNORD3A-ai-review.yaml` - Complete gene review (6.0KB)
- ✅ `SNORD3A-deep-research-perplexity.md` - Comprehensive literature research (8.0KB)
- ✅ `SNORD3A-notes.md` - Curated research notes (4.5KB)
- ✅ `SNORD3A-rnacentral.json` - RNAcentral database entry (115KB)
- ✅ `README.md` - This documentation

### Review Contents:
- ✅ 4 aliases documented
- ✅ 4 GO annotations curated (all marked as NEW)
- ✅ 2 core functions defined
- ✅ 4 literature references (2 PMIDs + 2 local files)
- ✅ 2 suggested experiments
- ✅ 3 suggested questions for experts
- ✅ Status: COMPLETE
- ✅ Validation: PASSES

## Gene Function Summary

**SNORD3A (U3 snoRNA)** is essential for ribosome biogenesis. Unlike typical C/D box snoRNAs that guide 2'-O-methylation, U3 guides site-specific cleavage of pre-rRNA through base-pairing interactions. It is a critical component of the SSU-processome complex that directs maturation of 18S rRNA and assembly of the 40S small ribosomal subunit.

### Key GO Annotations:

**Molecular Functions:**
- GO:0042134 (rRNA primary transcript binding)
- GO:0070181 (small ribosomal subunit rRNA binding)

**Biological Processes:**
- GO:0030490 (maturation of SSU-rRNA)
- GO:0006364 (rRNA processing)

## Curation Notes

The standard `just fetch-gene` command fails for SNORD3A because it expects Swiss-Prot UniProt IDs, which only exist for protein-coding genes. This is expected behavior and does not indicate an incomplete review.

For ncRNA genes, manual curation of GO annotations based on literature is the appropriate approach, which has been completed for this gene.
