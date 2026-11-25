# Thermotoga maritima MSB8 consultation

Both reviews are COMPLETE. All 14 seeded annotation payloads remain in their original order; there are no new, removed or retired rows. Four immutable raw files are preserved.

MtaD/Q9X034 is the 406-residue TM0936 protein, independently matched to the complete 2PLM polymer in the frozen literature identity proof. The original 2007 primary demonstrates SAH/MTA deamination. The author-hosted full 2013 primary (PMID23968233) explicitly assays Tm0936 as sg8 and adds measured 5′-deoxyadenosine activity. Table 1 catalytic efficiencies, not docking ranks, support the target substrate profile. The four specific deaminase activities refine general ancestors; only SAH/MTA are presented as core functions. Different quantitative assays are not silently pooled.

AhcY/O51933 corresponds to TM0172 and hydrolyzes both SAH and SIH approximately equally in PMID17603473. A review's broader preference statement does not supersede this primary target result. Existing GO0004013 remains, with a source-supported proposed SIH hydrolase core activity under GO0046508; no fabricated GO identifier or extra annotation row is introduced. Paired enzymatic capacity is established; native flux through the MtaD–SIH route remains unconfirmed.

Fresh QuickGO definitions/ancestry and the actual author PDF/text are durable inputs here. The cached abstract-only PMID23968233 was not overwritten. The two genuine Falcon requests failed with HTTP403 authentication errors; no provider report was fabricated. PAINT-loss checks found no applicable loss; refinement of the MtaD IBA concerns term specificity, not rejection of its ancestral placement.

Run `uv run python analysis/module_audits/bacterial_methionine_cycle/thema-consultation/check_preservation.py`. Focused gene validation, render and generated-history validation logs are included. `preservation.json` reports source and action accounting; `handoff.json` freezes all released paths. The builder records the reproducible curation transformation but should not be rerun against a frozen release.
