# HOM2 notes (YDR158W, P13663)

- Aspartate-semialdehyde dehydrogenase, EC 1.2.1.11, NADPH-dependent, homotetramer, step 2 of aspartate -> homoserine [UniProt:P13663 "FUNCTION: Catalyzes the NADPH-dependent formation of L-aspartate 4-"]; [UniProt:P13663 "KM=36 uM for NADP(+) (at pH 8.5 and at 30 degrees Celsius)"].
- Biochemistry: [PMID:4145650 "Purification and characterization of aspartic -semialdehyde dehydrogenase from yeast"] (no abstract cached).
- Genetics: hom2 mutants need Thr + Met [PMID:4380684 "Genetic and biochemical studies of genes controlling the synthesis of threonine and methionine in Saccharomyces."] (no abstract cached; curator-read).
- Localisation: cytosol + nucleus by GFP [UniProt:P13663 "SUBCELLULAR LOCATION: Cytoplasm, cytosol {ECO:0000269|PubMed:14562095}."].

## Curation observations
- GO:0009085 L-lysine biosynthetic process (InterPro IPR012080) REMOVED: yeast makes lysine via the alpha-aminoadipate pathway, not the DAP pathway that uses ASA.
- NAD binding IEA marked over-annotated: InterPro domain name, enzyme is NADP-specific.
- Plasma membrane HDA (PMID:16622836) marked over-annotated (soluble abundant enzyme in membrane-fraction proteome).


## 2026-10-26 systematic fungal threonine review

Reviewed all 38 rows and the core synthesis for yeast/HOM2. All original machine annotation fields are preserved; no rows were added or deleted. Current actions: {'MODIFY': 7, 'ACCEPT': 27, 'KEEP_AS_NON_CORE': 2, 'UNDECIDED': 1, 'REMOVE': 1}.

Hom2 catalyzes NADPH-dependent reductive dephosphorylation, producing aspartate semialdehyde. The original PMID:4145650 record lacks an abstract/full text after the normal retry, but its experimentally curated UniProt FUNCTION, kinetic and catalytic statements independently support the established reaction. Do not claim to have read that paper's full kinetic comparison. GO:0051287 was checked against QuickGO: NAD(H) differs from NADP(H). The electronic NAD claim is corrected to independently supported NADP binding; this does not assert that NAD can never bind. Integral nucleotide binding is core.

The 2016 fungal structure paper (PMID:26869335; normally cached publisher URL https://www.nature.com/articles/srep21067 after two PMID-fetch HTTP429 failures) directly establishes a Trichophyton functional tetramer with dimer-of-dimers interfaces. It cites the original yeast tetramer work and compares fungal sequences, including Saccharomyces/Schizosaccharomyces. Thus the dimerization-domain inference is compatible with a tetramer; an isolated active yeast dimer is not claimed. This is comparative structural support, not new native yeast structural measurement.

The broad InterPro lysine mapping is rejected for the fungal AAA route. PMID:29959064 explicitly assayed alleged DHDPS proteins in Coccidioides and Fonsecaea and found alternative activity/failed complementation; its abstract is sufficient for those stated comparisons but is not relabeled a yeast assay. The old pan-microbial review quotation did not itself establish the negative fungal assertion and is replaced by relevant evidence.

Nuclear localization is retained. Full PMID:26936955 screens Hom2/Hom6 but mechanistic Gdh1 results are not transferred. Full PMID:39349514 shows threonine-rescuable hom2 rDNA-silencing defects, supporting metabolic mediation rather than an invented chromatin MF. The HDA plasma-membrane row from PMID:16622836 is UNDECIDED: normal force-fetch and publisher access attempts did not yield target-level results/supplement. A soluble enzyme can have a peripheral membrane pool; 'likely contaminant' was not established.

### Access, workflow and validation

Actual per-gene Falcon research with Perplexity-lite fallback ran concurrently with normal publication caching. Both research providers failed authentication/quota checks; no provider report was fabricated. Publication caching succeeded. Logs are `.cache/module-audit-logs/threonine-yeast-HOM2-research.log` and `threonine-yeast-HOM2-publications.log`. Positive claims from abstract-only papers are limited to explicit results or independently publication-linked curated statements; inaccessible detailed evidence is not confidently rejected. Full new source caches and the publisher URL were obtained only through the normal fetcher.

The review and annotation-reviewer skills, independent reviewer consultation, current protein-binding policy and GO term-definition checks were applied. UniProt quotes were backfilled with record sections. Focused strict/term/source validation, rendering, helper-generated Codex histories and original-payload proof are recorded in the threonine-fungal manifests under `.cache/module-audit-logs/`. No module/tracker edits were made.
