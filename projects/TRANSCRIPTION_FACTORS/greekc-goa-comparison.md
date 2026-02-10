# GREEKC dbTF Target Set vs GOA Comparison

Analysis comparing the GREEKC curated dbTF target set with current GOA annotations.

## Summary

| Category | Count | Notes |
|----------|-------|-------|
| **GREEKC dbTF target set** | 1,449 | Curated by GREEKC consortium |
| **GOA dbTF annotations** | 1,447 | GO:0003700 descendants, Swiss-Prot |
| **Agreement** | 1,385 | 95.6% overlap |
| **GOA-only** | 62 | Potential over-annotations |
| **GREEKC-only** | 64 | 14 isoform IDs (canonical in GOA), 50 true gaps |

## Discrepancies

### GOA-only: 62 proteins annotated as dbTF but NOT in GREEKC curated set

These may represent over-annotations in GOA. Examples:

| UniProt | Gene | Concern |
|---------|------|---------|
| O00287 | RFXAP | Regulatory factor X accessory protein - **coTF**, not dbTF |
| O14593 | RFXANK | RFX-associated ankyrin - **coTF**, not dbTF |
| O00634 | NTN3 | Netrin-3 - axon guidance molecule |
| O95631 | NTN1 | Netrin-1 - axon guidance molecule |
| P08910 | ABHD2 | Alpha/beta hydrolase - enzyme |
| P22392 | NME2 | Nucleoside diphosphate kinase - enzyme |
| P23396 | RPS3 | Ribosomal protein S3 |
| P51858 | HDGF | Hepatoma-derived growth factor |
| P56524 | HDAC4 | Histone deacetylase 4 - enzyme |
| O15173 | PGRMC2 | Progesterone receptor membrane component 2 |

**Full list**: `comparison-goa-only.txt`

**Action**: These 62 proteins warrant review. Many appear to be coTFs, enzymes, or non-TF proteins that may have been incorrectly annotated with GO:0003700 descendants.

### GREEKC-only: 50 proteins in curated set without GOA dbTF annotation

After excluding 14 isoform-specific IDs (whose canonical forms are in GOA), 50 proteins remain:

| UniProt | Gene | Notes |
|---------|------|-------|
| A6NDX5 | ZNF840P | Zinc finger pseudogene (may not need annotation) |
| A8MQ14 | ZNF850 | Zinc finger protein |
| B7Z6K7 | ZNF814 | Zinc finger protein |
| O14709 | ZNF197 | Zinc finger protein |
| O43345 | ZNF208 | Zinc finger protein |
| P17031 | ZNF26 | Zinc finger protein |
| P17038 | ZNF43 | Zinc finger protein |
| P51523 | ZNF84 | Zinc finger protein |
| ... | ... | (41 more ZNF proteins) |

**Full list**: `comparison-greekc-only.txt` (remove isoform IDs)

**Pattern**: Most GREEKC-only entries are ZNF proteins. These may be:
1. Newly characterized TFs not yet annotated in GOA
2. Proteins with DBDs but lacking experimental validation
3. Computational predictions awaiting manual curation

## Key Findings

1. **95.6% agreement** between GREEKC curated set and GOA annotations - high concordance
2. **GOA may contain over-annotations** - 62 proteins include coTFs (RFXAP, RFXANK), enzymes (HDAC4, NME2), and non-TF proteins (netrins, ribosomal proteins)
3. **GREEKC captures isoform-specific annotations** - 14 isoform IDs whose canonical forms are already in GOA
4. **ZNF proteins dominate GREEKC-only** - Many zinc finger proteins in curated set lack GOA annotations
5. **Validates GREEKC curation** - The curated set correctly excludes obvious non-dbTFs that GOA includes

## Recommendations

### For GOA annotation review
1. Review 62 GOA-only proteins for potential removal from GO:0003700
2. Prioritize: RFXAP, RFXANK, netrins, ribosomal proteins, enzymes

### For annotation completion
1. Review 50 GREEKC-only proteins for potential GOA annotation
2. Many ZNF proteins may warrant dbTF annotation based on domain evidence

## Files Generated

- `greekc-dbTF-list-final.txt` - 1,449 GREEKC dbTF target set proteins
- `greekc-dbTF-ids.txt` - Same, stripped of UniProtKB: prefix
- `comparison-both.txt` - 1,385 proteins in agreement
- `comparison-goa-only.txt` - 62 GOA-only proteins
- `comparison-greekc-only.txt` - 64 GREEKC-only proteins (14 isoforms + 50 true gaps)
- `extract_greekc_proteins.py` - Script used for extraction

## Methods

GREEKC target set extracted via QuickGO API:
```bash
python3 extract_greekc_proteins.py > greekc-dbTF-list-final.txt
```

Uses `targetSet=dbTF` parameter with pagination through 60,391 annotations.
