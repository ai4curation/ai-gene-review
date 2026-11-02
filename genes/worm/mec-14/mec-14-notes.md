# mec-14 (Q20127, F37C12.12) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: mec-14 is the closest experimentally studied relative of fly CG18547 in PTHR42686:SF1. This review is done on mec-14's own evidence; no ProtNLM2 output was consulted.

### Deep research

`just deep-research-falcon worm mec-14 --fallback perplexity-lite` failed: falcon returned "Edison API request failed: Failed to authenticate" (HTTP 403) and the perplexity-lite fallback also failed. No deep-research file exists. Literature was gathered directly from PubMed, Europe PMC full-text search and the Alliance/WormBase gene record.

### Literature

- PubMed title/abstract search `mec-14[tiab] AND elegans` returns only PMID:8692859.
- Europe PMC full-text search ("mec-14" AND elegans) returns 15 hits; most are passing mentions (strain lists, touch-gene lists).
- PMID:2646709 (Chalfie & Au 1989): the saturation screen for touch-insensitive mutants that defined 18 touch genes; the 15 genes downstream of mec-3 give "nonfunctioning, yet differentiated, touch cells" [PMID:2646709 "The remaining 15 genes are likely targets of mec-3 action; mutants defective in these genes have nonfunctioning, yet differentiated, touch cells."]. The abstract does not name mec-14 individually (abstract only).
- PMID:8692859 (Gu, Caldwell & Chalfie 1996): mec-14 is among the genes needed for gentle-touch response [PMID:8692859 "At least 13 genes (mec-1, mec-2, mec-4-10, mec-12, mec-14, mec-15, and mec-18) are needed for the response to gentle touch by 6 touch receptor neurons"]. Recessive alleles of some touch genes act as dominant enhancers of ts alleles of mec-4, mec-5, mec-6, mec-12 and mec-15. Abstract only in our cache; PMC full text is publisher-restricted. The WormBase IGI annotations (partners mec-4, mec-12, mec-15, mec-5, mec-6) come from this paper's full text; the specific mec-14 interactions cannot be read here, so I defer to the curators on which interactions were shown.
- PMID:34875684 (Liang et al. 2022): touch-neuron FACS RNA-seq; mec-14 is among genes "known to be specific to (or highly enriched in) touch neurons based on existing single-gene analyses".
- WormBase curated gene description (via Alliance API, MOD_provided_gene_description): similarity to Kv beta subunits (AKR superfamily); required for gentle-touch response; "likely functions to regulate activity of the MEC-4 and MEC-10 degenerin channels"; expression solely in touch receptor neurons and mec-3-dependent; localisation in TRNs dependent on MEC-12. I could not find the primary publication for the expression, mec-3 dependence or MEC-12-dependent localisation statements (possibly unpublished Chalfie-lab data or a WormBase personal communication); these are therefore not used as cited evidence.

### Phylogeny (see mec-14-bioinformatics/RESULTS.md)

- PANTHER 19: PTHR42686:SF1; Ecdysozoa node PTN000199440 joins mec-14 with fly CG12224, CG3397, CG18547 (co-ortholog); Opisthokont node PTN000199433 adds yeast ARA2; Eukaryota node PTN000199432 adds Arabidopsis LGALDH. No human/vertebrate member, so the WormBase "ortholog of KCNAB1" claim is a superfamily-level similarity, not orthology in PANTHER; Kv beta proteins are in a different AKR family.
- PAINT: specific activities only at the fungal (D-arabinose DH, PTN000920371) and land-plant (L-galactose DH, PTN000920391) nodes; generic oxidoreductase activity at PTN002448388. mec-14 inherits only GO:0016491. Treat the omission as deliberate.
- Catalytic tetrad D132/Y137/K163/H206 conserved. Likely an active AKR, substrate unknown.

### Decisions

- Oxidoreductase activity (IBA, IEA): ACCEPT; as specific as the evidence allows.
- L-galactose dehydrogenase activity (IEA, InterPro IPR044479): REMOVE. The L-galactose activity belongs to the plant ascorbate pathway; PAINT deliberately confined it to land plants; the opisthokont sister ARA2 uses D-arabinose instead, and SF1 includes enzymes for several different substrates. No evidence for L-galactose as a substrate or for an L-galactose pathway in C. elegans.
- detection of mechanical stimulus involved in sensory perception of touch (IGI x3): ACCEPT, the best-supported process in this species; the molecular role in the transduction apparatus is unknown.
- mechanosensory behavior (IGI x3): KEEP_AS_NON_CORE, organismal readout of TRN function.
- positive regulation of detection of mechanical stimulus... / positive regulation of mechanosensory behavior (IGI with mec-5, mec-6): KEEP_AS_NON_CORE, curator framing of enhancer interactions; consistent with a modulatory role but not distinguishable from participation from the abstract.
- What is established experimentally in C. elegans: only genetic requirement for touch sensitivity and genetic interactions with other mec genes. No biochemical, localisation (published) or structural data. Enzyme activity is inferred only.
