# SPOCK3 (Testican-3) GO Annotation Review Summary

## Gene Information
- **UniProt ID**: Q9BQ16
- **Gene Symbol**: SPOCK3
- **Protein Name**: Testican-3 (SPARC/osteonectin, CWCV, and Kazal-like domains proteoglycan 3)
- **Organism**: Homo sapiens
- **Size**: 436 amino acids
- **Localization**: Secreted, extracellular matrix

## Overview
SPOCK3 is a secreted extracellular matrix proteoglycan with experimentally validated tumor-suppressive metalloendopeptidase inhibitor activity. It was originally identified through expression cloning as an inhibitor of membrane-type matrix metalloproteinases (MT1-MMP and MT3-MMP), distinguishing it from testican-2 (SPOCK2), which lacks this inhibitory activity and instead counteracts it.

## Core Molecular Functions

### Primary Function: Metalloendopeptidase Inhibitor
- **GO:0008191** - metalloendopeptidase inhibitor activity
- Directly interacts with and inhibits MT1-MMP and MT3-MMP
- Prevents pro-MMP-2 activation
- Experimentally validated by PMID:11751414, PMID:12810672

### Supporting Functions:
- **GO:0005509** - calcium ion binding (EC calcium-binding domains)
- **GO:0005518** - collagen binding (deposited on collagen)
- **GO:0050840** - extracellular matrix binding
- **GO:0005539** - glycosaminoglycan binding (proteoglycan with GAG chains)
- **GO:0030414** - peptidase inhibitor activity (parent term)
- **GO:0004857** - enzyme inhibitor activity (parent term)

### Biological Processes:
- **GO:2000146** - negative regulation of cell motility (tumor suppression)
- **GO:0010951** - negative regulation of endopeptidase activity
- **GO:0010810** - regulation of cell-substrate adhesion

### Cellular Localization:
- **GO:0031012** - extracellular matrix (core localization)
- **GO:0005615** - extracellular space (parent term)

## Annotation Review Results

**Total Annotations Reviewed**: 14 (from GOA file)
**Additional Annotations Added**: 3 (from UniProt, missing in GOA)

### Action Summary:
- **ACCEPT**: 14/14 existing annotations (100%)
- **NEW**: 3 annotations (collagen binding, ECM binding, negative regulation of endopeptidase activity)
- **REMOVE**: 0
- **MODIFY**: 0
- **UNDECIDED**: 0

### Key Findings:

1. **All existing annotations are correct and well-supported**
   - Multiple evidence codes converge on core functions (IBA, IEA, TAS, HDA, IDA)
   - Experimental validation from key papers (PMID:11751414, PMID:12810672)
   - High-throughput proteomics support (PMID:32055794, PMID:33266304)

2. **Multiple duplicate annotations strengthen confidence**
   - GO:0031012 (extracellular matrix): 4 annotations (IBA, HDA×2)
   - GO:0008191 (metalloendopeptidase inhibitor): 3 annotations (IBA, IEA, TAS)
   - GO:0005509 (calcium ion binding): 2 annotations (IBA, IEA)

3. **Functional distinction from SPOCK2**
   - SPOCK3 HAS MMP inhibitory activity (like SPOCK1)
   - SPOCK2 LACKS this activity and counteracts inhibition by SPOCK3
   - This is a key functional difference in the testican family

4. **Missing annotations identified and added**
   - GO:0005518 (collagen binding) - present in UniProt, missing from GOA
   - GO:0050840 (ECM binding) - present in UniProt, missing from GOA
   - GO:0010951 (negative regulation of endopeptidase activity) - IDA evidence from PMID:11751414

## Key Publications

1. **PMID:11751414** - Nakada et al. (2001)
   - Original characterization of SPOCK3/N-Tes as MT-MMP inhibitor
   - Demonstrates suppression of tumor invasion
   - Expression cloning identified SPOCK3 as pro-MMP-2 activation regulator

2. **PMID:12810672** - Nakada et al. (2003)
   - Comparative analysis of testican family members
   - Shows SPOCK3 inhibits MT-MMPs (unlike SPOCK2)
   - Demonstrates N-Tes deposition on collagen and cell motility inhibition

3. **PMID:32055794** - 3D ECM mapping proteomics
   - High-throughput identification of SPOCK3 in native ECM

4. **PMID:33266304** - Matrisome characterization
   - Independent validation of SPOCK3 as ECM component

## Structural Features
- Signal peptide (1-21)
- Follistatin-like domain
- Acidic region
- EC calcium-binding domains (EF-hand motifs)
- Kazal-like protease inhibitor domain (133-185)
- Thyroglobulin type-1 domain (314-380)
- GAG attachment sites (Ser387, Ser392)

## Alternative Splicing
- 9 isoforms
- **Isoform 2 (N-Tes)**: Lacks thyroglobulin domain but retains MMP inhibitory activity
- N-Tes is resistant to testican-2 inactivation when calcium-binding domain is deleted

## Expression and Disease
- Highly expressed in normal brain
- Down-regulated in gliomas (correlates with tumor grade)
- Expression loss associated with increased tumor invasion

## Curation Confidence
**HIGH** - All core functions are experimentally validated with multiple independent lines of evidence. The annotation set is comprehensive and accurate.

## Recommendations
1. Retain all existing annotations
2. Add the three missing annotations identified from UniProt
3. No modifications needed - current annotations are at appropriate specificity
4. Consider adding disease annotations for glioma progression

---
*Review completed: 2025-01-11*
*Curator: AI-assisted systematic review*
