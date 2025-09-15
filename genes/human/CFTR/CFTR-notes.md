# CFTR Gene Review Notes

## 2025-01-14 - Obsolete Term Label Fix

**Issue**: Validation failure due to 2 GO terms having obsolete labels.

**Root Cause**: Two GO terms in the review had labels prefixed with "obsolete" which no longer match the current ontology:
- GO:0098660: had "obsolete inorganic ion transmembrane transport" → corrected to "inorganic ion transmembrane transport"
- GO:0043225: had "obsolete ATPase-coupled inorganic anion transmembrane transporter activity" → corrected to "ATPase-coupled inorganic anion transmembrane transporter activity"

**Action Taken**: Updated the term labels to remove the "obsolete" prefixes to match the current GO ontology.

**Validation Status**: After fixing the obsolete labels, the gene now passes validation with only warnings about PENDING annotations.

**Note**: These terms were likely marked as obsolete at some point but have since been reinstated in the GO ontology, requiring the label correction. CFTR is the cystic fibrosis transmembrane conductance regulator, a chloride channel whose dysfunction causes cystic fibrosis.