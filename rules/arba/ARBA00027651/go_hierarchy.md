# GO Term Hierarchy for Phosphatases

## Current Annotation: GO:0004721 (phosphoprotein phosphatase activity)

GO:0004721 is a parent term in the GO molecular function hierarchy. More specific child terms are available and should be used instead:

### Recommended Child Terms:

**GO:0004722 (protein serine/threonine phosphatase activity)**
- Definition: Catalysis of the reaction: protein serine/threonine phosphate + H2O = protein serine/threonine + phosphate
- Should be used for: PP1, PP2A, PP2B, PP2C families and related Ser/Thr phosphatases

**GO:0004725 (protein tyrosine phosphatase activity)**  
- Definition: Catalysis of the reaction: protein tyrosine phosphate + H2O = protein tyrosine + phosphate
- Should be used for: Receptor and non-receptor type protein tyrosine phosphatases

**GO:0008138 (protein tyrosine/serine/threonine phosphatase activity)**
- Definition: Catalysis of the reaction: protein tyrosine/serine/threonine phosphate + H2O = protein tyrosine/serine/threonine + phosphate
- Should be used for: Dual-specificity phosphatases (DSPs) like MAP kinase phosphatases

## Impact of Using Parent Term

Using GO:0004721 instead of these specific terms:
1. Loses important mechanistic information
2. Reduces utility for pathway analysis
3. Makes it difficult to distinguish different phosphatase types in annotations
4. Violates GO annotation guidelines that recommend using the most specific term available

## Conclusion

ARBA00027651 should be split into separate rules using the appropriate specific GO terms rather than the overly broad parent term.