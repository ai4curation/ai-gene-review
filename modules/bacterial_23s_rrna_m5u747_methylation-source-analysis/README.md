# Paired rRNA-site specificity audit

The module compares three native implementations of two rRNA C5 methylations. E. coli requires two named enzymes to cover both sites; one experimentally dual-specific RlmCD covers both in each of the other two implementations. These are coverage requirements, not an assertion that the two reactions occur sequentially, use two copies of RlmCD, or depend on each other. The original module identifier is preserved. The paired-site scope excludes U1939-only mollicute RlmFO, the tRNA TrmA comparator, and downstream G748/telithromycin biology.

## Reproduce bounded checks

```sh
uv run python modules/bacterial_23s_rrna_m5u747_methylation-source-analysis/check_families.py
uv run python modules/bacterial_23s_rrna_m5u747_methylation-source-analysis/check_routes.py
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/bacterial_23s_rrna_m5u747_methylation.yaml
uv run python -m ai_gene_review.validation.module_validator modules/bacterial_23s_rrna_m5u747_methylation.yaml
just render-module modules/bacterial_23s_rrna_m5u747_methylation.yaml
```

`check_families.py` obtains the four module representatives through the repository’s normal UniProt PANTHER lookup. PTHR11061 is the verified broad family, with its official label from `interpro/panther/panther.obo`. Exact GENE_PRODUCT selectors restrict the modeled participants; the broad family is retained as classification. No specific-substrate PAINT ancestor is asserted. The gene UniProt records retain the original family cross-references; the validation cache is ignored and is not evidence. The checker seeds an absent cache but preserves any existing corpus index and its alternate assignments.

`check_routes.py` exercises twelve biologically distinct coverage cases. It accepts the E. coli pair and each dual-specific enzyme, rejects either dedicated enzyme alone, rejects TrmA substitution, and rejects incomplete or mixed-species activity combinations. The compiler uses alternatives as an OR; it does not prove exclusivity, taxonomic conservation, reaction kinetics, active expression, or physiological sufficiency. Taxa and site-specific chemistry require the independently curated evidence.

## Source and panel coverage

Nine manually assessed module references include two full review articles and primary genetics, mass spectrometry, structures and comparative absence evidence. Six site-specific annotons each cite direct experimental evidence. There are no causal edges because none is justified between these two site reactions. All four native representatives and E. coli TrmA, the specificity comparator, receive full individual annotation reviews.

The initial GO-CAM index search found no entries for P75817, P55135, O31503 or Q97R12; no GO-CAM association is invented. Mollicute absence is explicitly limited to the surveyed organisms and the authors’ reported mass-spectrometric observations. The newer structural study corrects the interpretation of the earlier 18-nt packing arrangement. The 2026 review’s RlmC iron-sulfur assertion miscites an RlmD experiment and is not used as direct RlmC evidence.
