# Bacterial 23S rRNA U747/U1939 C5 methylation audit

## 2026-10-26 — boundary and source survey

The original document was a single E. coli RlmC reaction. The curated boundary will cover the paired U747/U1939 methylation program, retaining this existing module identifier. E. coli uses dedicated RlmC and RlmD activities; Bacillus subtilis and Streptococcus pneumoniae use a dual-specific RlmCD protein. Each taxon-specific implementation will expose both chemical roles. These are distinct substrate modifications, not a claimed sequential pathway: no catalytic precedence or mutual requirement follows from co-occurrence. TrmA is an independently reviewed specificity comparator outside the module, not a U747 enzyme. The survey found no separate U1939 module to duplicate.

The Bacteria root is an envelope for these three characterized implementations, not a universality claim. PMID:32290235 reports no U747 modification in the surveyed mollicutes despite variable U1939 modification. The U1939-only folate/FAD RlmFO route is outside this paired-site boundary. Broad Gram-positive/Gram-negative descriptions in reviews are not sufficient to generalize the variants to entire phyla.

### Literature retrieval and assessment

Searches included “RlmC RlmCD review ribosomal RNA m5U747 methylation review”, “Streptococcus pneumoniae RlmCD U747 U1939 methylation structure”, “ribosomal RNA modifications bacterial methyltransferase review”, and “Mollicutes Modify 23S RlmFO”. PubMed identifiers were cross-checked through Europe PMC, then the repository normal fetcher cached PMID:28601226, PMID:32290235 and PMID:42517620 with full text. Initial concurrent PMID requests hit HTTP 429; a later batched normal retry succeeded. PMID:21051506 was normally warmed to full text.

- PMID:42517620, Compendium of RNA modifications for bacterial stress adaptation (2026), provides the current bacterial overview and links U747 methylation to the separate G748 modification context. Its Gram-stain generalization is bounded by the primary species evidence. The heading N5-methyluridine is chemically incorrect for m5U, whose methyl group is attached to C5. Its RlmC iron-sulfur statement requires checking its cited primary protein before use.
- PMID:28601226, The Evolution of Substrate Specificity by tRNA Modification Enzymes (2017), explains RNA fold recognition and discrimination between RlmD and TrmA; a shared catalytic family does not establish a shared substrate.
- PMID:32290235, Reductive Evolution and Diversification of C5-Uracil Methylation in the Nucleic Acids of Mollicutes (2020), is primary comparative evidence for the absence boundary, not a review.
- PMID:12907714 directly distinguishes E. coli RlmC in-vivo assignment from recombinant RlmD biochemistry. The authors discuss loss of recombinant RlmC activity during preparation. Inactivity does not establish an obligatory ribosome-assembly intermediate.
- PMID:21824914 establishes native B. subtilis dual-site modification plus separately identified heterologous E. coli rescue.
- PMID:26365244 gives native S. pneumoniae TIGR4 SP_1029 disruption chemistry at both sites. Its G748/TEL context is conditional and outside this module; U747 methylation increases RlmAII efficiency rather than being an absolute prerequisite.
- PMID:28949991 and PMID:30388185 provide successive structural and biochemical studies. The later paper explicitly treats the earlier 18-nt complex as physiologically irrelevant crystal packing; only the newer substrate complexes support the detailed recognition model. Truncated/catalytic-trap constructs are not native-state structures.

### Family and exemplar boundary

Current raw UniProt records classify RlmC P75817, B. subtilis RlmCD O31503 and S. pneumoniae SP_1029 Q97R12 in PANTHER:PTHR11061, whose official name is RNA M5U METHYLTRANSFERASE. The recorded SF30 name is tRNA-specific despite containing these rRNA enzymes; it is not evidence for the wrong RNA substrate. Use the verified broad family with explicit role restrictions, rather than invent a narrow PANTHER node or infer substrate specificity from the family label. E. coli RlmD P55135 is reviewed as the other native paired-site enzyme; TrmA P23003 is the negative substrate comparator.

### Provider attempts

The module Falcon command ran and failed Edison authentication (HTTP 403). A separately executed Perplexity-lite fallback failed quota (HTTP 401). No provider report was created or authored manually. An initial attempt to pass the gene-workflow --fallback flag to the module wrapper failed argument parsing; the actual provider calls were subsequently made separately. Manual research is recorded here.

### Outstanding checks

Complete all five gene reviews; reconcile the site-specific module draft with their core functions; validate sources, family membership, taxa and route logic; render and create appended history; obtain independent scientific QA; run full validation before creating the module-specific PR.

## 2026-10-26 — paired-site draft and bounded checks

The paired-site draft now has three native alternatives, six independently evidenced site activities and nine assessed literature sources. The broader boundary makes RlmD a core E. coli participant; TrmA remains a specificity comparator. Twelve route cases pass. The normal UniProt API resolves all four representatives to PTHR11061 (RlmD SF49, the other three SF30), confirming the broad family without transferring substrate specificity. Review PMID:42517620 reference 185 was checked: it is the RlmD/RumA redox paper PMID:15181002, not a direct RlmC assay. The reference assessment records that miscitation. No GO-CAM index rows matched the four module proteins.

Independent QA identified that FAMILY selectors would permit broader substitution despite prose limits. All six leaves now select exact GENE_PRODUCTs and retain their verified family descriptors as classification. Representative members are not treated as the limits of a broad family. The route predicate uses only the selected protein.

QA confirmed the paired-site chemistry and recommended a stronger overall E. coli quotation. Both the module and variant now quote the YbjF loss result together with the full recombinant YgcA/U1939 sentence. Current TrmA P23003 belongs to PTHR47790, not the PTHR11061 classification of the four rRNA participants; historical biochemical homology does not justify asserting the same current PANTHER placement.
