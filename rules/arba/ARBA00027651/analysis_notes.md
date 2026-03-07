# ARBA00027651 Analysis Notes

## Phosphoprotein Phosphatase Mechanisms

Phosphoprotein phosphatases comprise mechanistically distinct families:

### Protein Tyrosine Phosphatases (PTPs)
- Use a cysteine-based nucleophilic attack mechanism
- Characterized by the signature motif HC(X)5R 
- Include both receptor-type and non-receptor type phosphatases
- Representative domains: IPR000242 (Tyrosine-specific protein phosphatase, PTPase domain)

### Serine/Threonine Phosphatases
- Use metal-dependent mechanisms (Mg2+/Mn2+ or Fe2+/Zn2+)
- Include PP1, PP2A, PP2B (calcineurin), PP2C families
- Different metal requirements and regulatory mechanisms
- Representative domains: IPR001932 (PPM-type phosphatase-like domain), IPR006186 (Serine/threonine-specific protein phosphatase)

### Dual-Specificity Phosphatases (DSPs)
- Can dephosphorylate both tyrosine and serine/threonine residues
- Mechanistically related to PTPs (cysteine-based)
- Often target MAP kinases and cell cycle proteins
- Representative domains: IPR000340 (Dual specificity phosphatase, catalytic domain)

## Functional Distinctions Lost in ARBA00027651

The rule's use of the broad GO term GO:0004721 (phosphoprotein phosphatase activity) fails to capture these important mechanistic and functional distinctions. Each family should be annotated with more specific GO terms:

- GO:0004725 (protein tyrosine phosphatase activity) for PTPs
- GO:0004722 (protein serine/threonine phosphatase activity) for PSPs  
- GO:0008138 (protein tyrosine/serine/threonine phosphatase activity) for DSPs

This specificity is critical for understanding cellular signaling networks and drug targeting.