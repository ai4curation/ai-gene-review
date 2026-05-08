# Deep Research: ARBA00088072 and TRM1/Trm1 Dimethyltransferase Specificity

## Overview of the Issue

Based on GitHub issue #5782, ARBA rule ARBA00088072 was allegedly propagating annotations to GO:0160103 "tRNA (guanine(26)-N2/guanine(27)-N2)-dimethyltransferase activity" for TRM1/Trm1 enzymes. However, this rule appears to be deprecated or non-existent in the current UniProt ARBA database.

## Key Problems Identified

1. **Rule Non-existence**: ARBA00088072 cannot be found in UniProt's current ARBA database
2. **GO Term Specificity**: Confusion between GO:0160103 (G26/G27 activity) and GO:0160104 (G26-only activity) 
3. **Literature Evidence**: The cited literature (PMID:9801306) doesn't support G27 methylation
4. **ARBA Thresholds**: Questions about whether sufficient experimental evidence exists for rule creation

## Literature Analysis: PMID:9801306

**Title**: "Point and deletion mutations eliminate one or both methyl group transfers catalysed by the yeast TRM1 encoded tRNA (m22G26)dimethyltransferase"

**Key Findings**:
- Yeast TRM1 encodes a tRNA (m22G26)dimethyltransferase
- The enzyme catalyzes **specifically G26 dimethylation** 
- Paper title explicitly mentions "m22G26" (dimethylguanosine at position 26)
- No mention of G27 methylation activity
- Abstract states: "Guanosine at position 26 in eukaryotic tRNAs is usually modified to N2,N2-dimethylguanosine (m22G26)"

**Critical Issue**: This paper provides evidence for G26-specific activity only, NOT G26/G27 dual activity.

## TRM1/Trm1 Enzyme Specificity Analysis

### Canonical Activity
- **Primary Function**: G26-specific dimethyltransferase
- **Taxonomic Distribution**: Conserved across eukaryotes
- **Well-characterized organisms**: S. cerevisiae, S. pombe, humans (TRMT1)

### G27 Methylation Evidence
- **Eukaryotic systems**: No strong evidence for G27 methylation by TRM1/Trm1
- **Bacterial/archaeal systems**: Some reports suggest possible G27 activity, but less characterized
- **Literature consensus**: TRM1/Trm1 is primarily/exclusively G26-specific in eukaryotes

## GO Term Analysis

### GO:0160103 vs GO:0160104

**GO:0160103**: "tRNA (guanine(26)-N2/guanine(27)-N2)-dimethyltransferase activity"
- EC: 2.1.1.215
- Dual specificity for both G26 AND G27
- Reaction: Uses 4 S-adenosyl-L-methionine molecules

**GO:0160104**: "tRNA (guanine(26)-N2)-dimethyltransferase activity"  
- EC: 2.1.1.216
- G26-specific only
- Reaction: Uses 2 S-adenosyl-L-methionine molecules
- More accurate for canonical TRM1/Trm1 activity

### Experimental Annotations
From the GitHub issue:
- Only 3 experimental annotations exist for GO:0160103
- 2 SGD annotations from PMID:9801306 (which doesn't support G27 activity)
- Insufficient evidence base for broad ARBA propagation

## Curation Issues Identified

1. **Over-annotation**: TRM1/Trm1 enzymes being annotated with dual G26/G27 specificity when literature supports only G26
2. **Inappropriate GO Term**: GO:0160103 should likely be restricted or have taxon constraints
3. **Evidence Threshold**: ARBA rule creation with insufficient experimental support
4. **Propagation Impact**: Incorrect annotations spreading to well-characterized genes

## Taxonomic Considerations

### Eukaryotic TRM1/Trm1
- Strong evidence for G26-only specificity
- Should be annotated to GO:0160104, not GO:0160103

### Prokaryotic/Archaeal Systems
- May have different specificities
- Limited characterization
- If G26/G27 dual activity exists, it may be lineage-specific

## Related GitHub Issues

Issue #26257 mentioned in comments discusses the history of these GO terms, suggesting ongoing curation challenges with tRNA methyltransferase annotations.

## Conclusions

1. ARBA00088072 appears to be deprecated/non-existent
2. The biological evidence strongly favors G26-only specificity for eukaryotic TRM1/Trm1
3. GO:0160103 may be inappropriately broad for most characterized systems
4. Current annotations may represent significant over-annotation

## Recommendations

1. **Verify rule status**: Confirm ARBA00088072 deprecation
2. **Review existing annotations**: Audit proteins annotated with GO:0160103
3. **Consider taxon restrictions**: If GO:0160103 is valid, restrict to appropriate taxonomic groups
4. **Literature re-evaluation**: Reassess experimental evidence supporting G26/G27 dual activity