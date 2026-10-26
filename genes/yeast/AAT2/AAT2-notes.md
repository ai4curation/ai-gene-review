# AAT2 notes (YLR027C, P23542; ASP5)

- Cytosolic AspAT, EC 2.6.1.1 [UniProt:P23542]. Purified/sequenced: [PMID:1859361 "The single (cytosolic) aspartate aminotransferase was purified in high yield from baker's yeast (Saccharomyces cerevisiae)."]
- Cytosolic in glucose, peroxisomal in oleate: [PMID:9288922 "Whereas virtually all cellular AAT activity was peroxisomal in oleate-grown cells, we found that in glucose-grown cells most of the AAT activity resided in the cytosol."]; [PMID:9288922 "We demonstrate that the gene AAT2 codes for the cytosolic and peroxisomal AAT activities."]; not required for beta-oxidation [PMID:9288922 "These results indicate that AAT2 is not essential for the peroxisomal NAD(H) redox shuttle."]
- Major aspartate synthase: [PMID:33397945 "suggesting that Aat2p is the major enzyme for aspartate synthesis under nitrogen starvation"]; [PMID:35621265 "Non-catalytic AAT2 mutants are auxotrophic for aspartate and well expressed."]
- Moonlighting (full text read): [PMID:35621265 "EDTA treatment to separate the ribosomal subunits further indicated that Aat2 predominantly binds to 60S (large) subunits"]; [PMID:35621265 "Loss of Aat2 caused aberrantly high activation of the ISR via enhanced eIF2α phosphorylation and GCN4 activation."] Aat2 thus restrains translational repression; the GOA term "negative regulation of translation in response to oxidative stress" with acts_upstream_of_or_within is direction-agnostic and kept as non-core.

## Curation observations
- Same YeastCyc precursor-supply BP inheritance as AAT1 (asparagine, homoserine, threonine) -> MARK_AS_OVER_ANNOTATED.


## 2026-10-26 comparative annotation audit

Reviewed all 44 existing rows and the core-function synthesis for yeast/AAT2; no rows were added or dropped. Original GO terms, evidence codes, source identifiers and all other machine fields are preserved. Actions: {'MODIFY': 8, 'ACCEPT': 31, 'KEEP_AS_NON_CORE': 5}.

PMID:33397945 full tracing results establish Aat2 dominance in newly synthesized aspartate under the tested nitrogen-starvation conditions; “almost completely abolished” is not absolute abolition in every environment. PMID:9288922 explicitly reports: “We demonstrate that the gene AAT2 codes for the cytosolic and peroxisomal AAT activities.” Peroxisomal localization is therefore retained as a core enzyme location under oleate growth, with a separate contextual core and no assertion of obligatory beta-oxidation/redox-shuttle function. Cytosolic and peroxisomal flux are not equated.

PMID:35621265 full results/figures 4, 5 and 7 show stronger peroxide-induced ribosome runoff and Gcn2/eIF2alpha activation in the deletion strain, while untreated translation is similar. Catalytic-dead Aat2 retains ribosome binding and restores normal restraint. GO:0032938 names *negative* regulation of translation; its definition was checked through live QuickGO. The existing row is MODIFY to GO:0045727 positive regulation of translation, explicitly limited to restraint of excessive repression during peroxide stress. This decision does not use the machine relationship qualifier or assert universal basal translation activation. The ribosomal-large-subunit binding row remains a specific non-core moonlighting activity. Independent annotation-reviewer consultation agreed with the direction correction.

As with AAT1, actual downstream aspartate transamination participates in asparagine catabolism without binding Asn directly (PMID:36040324). Existing Asn/homoserine biosynthetic routes include substrate formation by AspAT and are retained as secondary contributions; broad threonine metabolism refines to biosynthesis. No new downstream process is proposed. Cofactor binding and glutamate/2-oxoglutarate chemistry are core, not peripheral merely because they are components of one enzyme reaction.

### Research access and provenance

An actual per-gene Falcon attempt with Perplexity-lite fallback ran in parallel with normal publication caching. Falcon returned HTTP403 authentication failure; Perplexity returned HTTP401 insufficient quota. No provider report was fabricated. Manual evidence review is recorded here; research and publication logs are `.cache/module-audit-logs/aspartate-yeast-AAT2-research.log` and `aspartate-yeast-AAT2-publications.log`. Normal publication fetching succeeded. Cached abstracts are used only for explicit reported findings; unverified target-specific experiments are not confidently rejected.

The annotation-reviewer workflow and current bare-protein-binding policy were applied. No GOA file is used as evidence. Existing sound source quotations were preserved, new quotations were checked against cached source text, and UniProt record sections were backfilled by the helper. Gene summaries are standalone biology. Histories use the helper with explicit Codex actor/tool; focused strict/term/source validation and HTML rendering are logged under `.cache/module-audit-logs/aspartate-yeast-AAT2-*`. Final results and machine-payload proof are in the panel validation/payload manifests.
