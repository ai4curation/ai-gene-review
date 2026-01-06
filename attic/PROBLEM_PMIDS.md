# Problematic Publication Files - FIXED

## Issue Found and Resolved

**Bug**: The publication fetcher was incorrectly using `pubmed_pmc_refs` (papers that cite the original) instead of `pubmed_pmc` (the PMC version of the paper itself) when looking up PMC IDs via NCBI's elink API.

**Fix Applied**: Updated `src/ai_gene_review/etl/publication.py` line 363 to check for `LinkName == "pubmed_pmc"` to ensure we only use the actual PMC version of articles, not papers that cite them.

## Previously Problematic PMIDs (Now Fixed)

All 9 files have been re-fetched and now correctly show only abstracts since these papers don't have PMC versions available:

| PMID | Paper | Status |
|------|-------|--------|
| PMID_10094049 | TAK1, IL-1 signaling, NIK, NF-kappaB (Nature 1999) | ✅ Fixed - abstract only |
| PMID_10892653 | Drosophila Dscam axon guidance receptor (Cell 2000) | ✅ Fixed - abstract only |
| PMID_11856530 | Drosophila Dscam and axon bifurcation (Neuron 2002) | ✅ Fixed - abstract only |
| PMID_12419249 | BRCA1 and XIST RNA (Cell 2002) | ✅ Fixed - abstract only |
| PMID_12546818 | Drosophila ORN axonal targeting (Neuron 2003) | ✅ Fixed - abstract only |
| PMID_15339648 | Dscam transmembrane domains (Cell 2004) | ✅ Fixed - abstract only |
| PMID_15339649 | Dscam diversity in mushroom body (Cell 2004) | ✅ Fixed - abstract only |
| PMID_16474389 | Dscam dendritic patterning (Nat Neurosci 2006) | ✅ Fixed - abstract only |
| PMID_16890528 | Drosophila DPM neurons and memory (Curr Biol 2006) | ✅ Fixed - abstract only |

## Technical Details

The bug occurred because the NCBI elink API returns multiple LinkSets:
- `pubmed_pmc`: The actual PMC version of the article (if it exists)
- `pubmed_pmc_refs`: PMC articles that cite this paper

The code was incorrectly taking the first PMC link it found without checking the LinkName, leading to citation papers being downloaded instead of the original papers. These older papers from major journals (Cell, Nature, Neuron) typically don't have PMC versions available, which is why they should only show abstracts.