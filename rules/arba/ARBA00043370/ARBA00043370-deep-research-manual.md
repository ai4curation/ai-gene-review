# Deep Research for ARBA00043370: Export across plasma membrane rule

## Research Summary

ARBA00043370 is a UniProt annotation rule that assigns GO:0140115 "export across plasma membrane" to proteins matching specific structural and taxonomic criteria. This rule has 12 complex condition sets covering various transporter families.

## GO Curator Concerns (GitHub Issue #6140)

The primary concern raised by GO curators in issue #6140 is:

> "We don't know (and can't infer) the location, substrate or direction of these transporters"

This indicates that the rule is making overly specific locational and directional assumptions about transporter function without sufficient evidence.

## Rule Analysis

The rule covers:
- Sugar transporters (IPR005829 + IPR020846 + PTHR23502)
- ABC transporters in various taxa
- MFS (Major Facilitator Superfamily) transporters 
- P-type ATPases
- Na+/H+ antiporters
- Sodium/potassium-transporting ATPases

## Key Problems Identified

1. **Over-specificity**: The term "export across plasma membrane" implies:
   - Specific cellular location (plasma membrane)
   - Specific direction (export, not import)
   - These assumptions may not be justified for all covered transporters

2. **Taxonomic Scope Issues**: The rule has 12 different condition sets with different taxonomic restrictions, suggesting potential biological incoherence

3. **Functional Diversity**: The covered transporter families have diverse functions - some may import, others export, and many can do both

## Biological Assessment

Many transporters in the covered families (MFS, ABC, P-type ATPases) are known to:
- Function bidirectionally
- Localize to various cellular membranes (not just plasma membrane)  
- Transport different substrates in different organisms

The blanket assignment of "export across plasma membrane" appears biologically inappropriate for this diverse set of transporters.

## Recommendations

Based on the curator concerns and rule analysis:
1. **DEPRECATE** - This rule should be deprecated due to over-annotation
2. The covered transporters should be annotated with more general, appropriate terms
3. Individual transporter families may warrant separate, more specific rules with proper evidence

## References

- GO annotation issue #6140: https://github.com/geneontology/go-annotation/issues/6140
- UniProt rule data: ARBA00043370.enriched.json