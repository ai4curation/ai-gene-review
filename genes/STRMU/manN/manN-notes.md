# manN review notes — 2026-11-07

Reviewed all 4 seeded annotations and synthesized the core function. No source payloads, qualifiers or ordering were changed; no NEW rows were created.

Identity: Q8DSC2 is the UA159 locus corresponding to the paper name manN. The current UniProt alias may differ (manL=ptnA/SMU_1877; manM=ptnC/SMU_1878; manN=SMU_1879). The frozen literature-consultation identity-proof.json and primary12902269 Fig1/17951382 establish the bridge. This is a locus/strain mapping, not a claim that an experimental construct was newly sequenced.

Primary12902269 was read in full: native ManL-dependent PTS assays support uptake participation but the mutant can grow faster on mannose, consistent with another inducible route. Full24928869 shows amino-sugar uptake dominated by ManLMN using complete-manLMN deletion in PEP-dependent uptake assays, alongside ManL deletion/partial complementation and identifies ManO modulation. It does not separately assay purified UA159 ManM or ManN. Its discussion describes substantial ManM/ManN sequence divergence between two S. mutans lineages; other strains are not interchangeable with UA159.

The membrane pair is inferred from exact domain/operon identity and native-system function, with structural context from E. coli31209249. The comparative structure is a trimer of ManYZ pairs, not proof of a UA159 stoichiometry or direct UA159 sugar-contact map. ManL retains catalytic relay chemistry; core contributes_to0022870 avoids asserting autonomous whole-transporter activity. Fresh QuickGO definitions confirm both8982 and22870 include coupled transport.

UniProt ARBA function/EC names are not independent support. Domain signatures, locus and sequence are used as such. ManM PRU00429 feature-caution wording is not a demonstrated activity-loss assay. No donor-count or circularity argument is used. PAINT-loss tools report the exact targets absent from the cached trees: lineage losses were not checked, despite the generic terminal no-loss sentence. No PTN is invented.

Actual configured Falcon research was attempted for this gene and terminated with403 authentication failure; log: .cache/module-audit-logs/mannose-pts-20261107/ua159-consultation/manN-falcon.log. No provider report was authored or fabricated. Manual source findings are in the frozen literature-consultation package.

All primary caches and machine-generated source files remain immutable. Supporting texts cite the actual externally read source excerpts where the normal publication cache is abstract-only. Focused validation, rendering, generated history and preservation proof are recorded in ua159-consultation/handoff.json.

Focused validation passed. Coverage advisories (one for ManL; two each for ManM/ManN) concern the inferred core complex and mannose process not having separate seeded rows. No extra NEW rows were manufactured to silence them; specific reaction replacements already imply the transport context.

Final refinement: whole-operon24928869 Fig2 directly supports the apparatus in GlcNAc uptake. Broad MF rows refine to all supported mannose/glucose/GlcNAc specific PTS activities, while the core emphasizes the shared mannose reaction. Stable full-operon complementation was not obtained; no complete rescue is claimed.


## PR6193 source-specific follow-up (2026-11-07)

Replaced recycled growth anchors with native UA159 PEP-dependent activity evidence, target domain/topology inference and the full-primary manLMN amino-sugar deletion result. No isolated-subunit flux or direct GlcNAc product assay is claimed. Membrane localization is supported by target-specific PROSITE-ProRule topology, not growth. Original ordered payloads and qualifiers are unchanged. Additive evidence and preservation proof: `analysis/module_audits/bacterial_mannose_pts/review-followup`; earlier releases remain historical and unchanged.
