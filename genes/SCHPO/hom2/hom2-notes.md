# hom2 (SPCC1827.06c, UniProt P78780) notes

Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11), PTHR46718:SF1.

- [UniProt:P78780 "Reaction=L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-"]; [UniProt:P78780 "FUNCTION: Catalyzes the NADPH-dependent formation of L-aspartate 4-"] (by similarity to S. cerevisiae Hom2 P13663).
- Location: [UniProt:P78780 "SUBCELLULAR LOCATION: Cytoplasm, cytosol {ECO:0000269|PubMed:16823372}."] plus nucleus (ORFeome GFP).
- S. cerevisiae: [PMID:2570346 "In Saccharomyces cerevisiae the HOM2 gene encodes aspartic semi-aldehyde"] dehydrogenase.
- Lysine: InterPro2GO maps IPR012080 to L-lysine biosynthesis (bacterial/plant DAP pathway: [PMID:11352712 "The aspartate pathway is responsible for the biosynthesis of lysine, threonine, isoleucine, and methionine in most plants and microorganisms."]). Fungi use the alpha-aminoadipate pathway (S. pombe lys4 homocitrate synthase is in PomBase GO-CAM gomodel:67c10cc400000148). REMOVE, as for S. cerevisiae HOM2.
- NAD binding (IPR000534 domain name) -> over-annotation, as in HOM2 review.

## Naming/label note
- GO:0004073 current label is "aspartate-semialdehyde dehydrogenase activity" (GOA file still says "(NADP+) activity"); used the current label in core_functions, left GOA labels untouched.
- Core = GO:0004073 / GO:0009090 / cytosol; agrees with HOM2 review and GO-CAM 678073a900003175.


## 2026-10-26 systematic fungal threonine review

Reviewed all 17 rows and the core synthesis for SCHPO/hom2. All original machine annotation fields are preserved; no rows were added or deleted. Current actions: {'ACCEPT': 10, 'KEEP_AS_NON_CORE': 2, 'MODIFY': 4, 'REMOVE': 1}.

The specific NADP-dependent ASADH chemistry is a curated inference from budding-yeast Hom2 (P13663), supported by conserved fungal family/domain architecture. Cytosol/nuclear observations from PMID:16823372 are retained; broader cytoplasm refines to cytosol without excluding the nuclear pool. General oxidoreductase/amino-acid terms refine to supported chemistry and biosynthetic branches. NADP binding is core; the generic-domain NAD assignment refines to NADP without asserting absolute exclusion of NAD.

The normally fetched full publisher source for PMID:26869335 (https://www.nature.com/articles/srep21067) establishes the fungal dimer-of-dimers organization from Trichophyton structure and mutagenesis, with Schizosaccharomyces included in sequence comparisons. The existing dimerization-domain annotation is retained as an interface/assembly inference, not a claim of an independently active native S. pombe dimer. The old summary saying ASADH simply 'is a dimer' is corrected.

Fungal lysine synthesis uses the alpha-aminoadipate route. The old generic aspartate-family review did not prove that exclusion; PMID:29959064 now supplies relevant comparative candidate-enzyme/sequence/complementation evidence (Coccidioides/Fonsecaea, not S. pombe assays). The InterPro lysine transfer is a pathway mismatch. Full PMID:31784357 is a chromatin-association discovery lead, but exact Hom2 supplementary enrichment was not verified, so the reported nucleus is retained without a new direct chromatin function.

### Access, workflow and validation

Actual per-gene Falcon research with Perplexity-lite fallback ran concurrently with normal publication caching. Both research providers failed authentication/quota checks; no provider report was fabricated. Publication caching succeeded. Logs are `.cache/module-audit-logs/threonine-SCHPO-hom2-research.log` and `threonine-SCHPO-hom2-publications.log`. Positive claims from abstract-only papers are limited to explicit results or independently publication-linked curated statements; inaccessible detailed evidence is not confidently rejected. Full new source caches and the publisher URL were obtained only through the normal fetcher.

The review and annotation-reviewer skills, independent reviewer consultation, current protein-binding policy and GO term-definition checks were applied. UniProt quotes were backfilled with record sections. Focused strict/term/source validation, rendering, helper-generated Codex histories and original-payload proof are recorded in the threonine-fungal manifests under `.cache/module-audit-logs/`. No module/tracker edits were made.
