# hscA (P0A6Z1, E. coli K-12) notes

Provider deep research could not run: `just deep-research-falcon` failed with Edison API 403 (auth), 2026-10-23. These notes are from the cached publications and the UniProt record.

## Function
- Specialized Hsp70 (Hsc66). ATP hydrolysis is rate-limiting [PMID:10713091 "These results indicate that ATP hydrolysis is the rate-limiting step under steady-state conditions and is >10(3)-fold slower than the rate of ADP/ATP exchange."]
- IscU is its substrate, recognized through the LPPVK motif [PMID:12871959 "Hsc66 interacts with peptides corresponding to a discrete region of IscU including residues 99-103 (LPPVK)"]; [PMID:15485839 "IscU behaves as a substrate for HscA, and HscB enhances the binding of IscU to HscA."]
- Catalyzes ATP-dependent cluster transfer [PMID:18986169 "HscA-mediated acceleration of [2Fe2S] cluster transfer exhibited an absolute requirement for both HscB and ATP."]
- Binds BioB and improves its in vivo cluster assembly [PMID:19821612 "In this work, we show that in Escherichia coli, HscA significantly improves the efficiency of the in vivo assembly of the [2Fe-2S](2+) cluster on BioB under conditions of low to moderate iron."]
- Cold-induced [PMID:7665466 "Expression of hscA was not induced upon heat shock but was induced approximately 11-fold 3 h after a shift from 37 to 10 degrees C."]

## Curation decisions
- Core MF is GO:0140662, in GO:0016226. This matches the module. The GO:0044183 IBA is changed to GO:0140662. GO:0016887 is kept as a second core MF.
- Generic protein folding, protein refolding and membrane are marked as over-annotated.
- Suspected source defect: the PMID:11983079 IPI WITH/FROM UniProtKB:P0A9R9 resolves to FtsE. The paper reports HscA with Fdx/IscA, so P0A9R4 (Fdx) was probably intended. Recorded under source_defects with confidence SUSPECTED.
- Open question: GO:0140662 says "folding", but HscA's output is remodelling of the cluster-loaded scaffold.


## 2026-11-07 ISC whole-gene re-review

Replaced unsupported core ATP-dependent folding precision with the measured ATP-hydrolysis/cluster-transfer activity. PMID22782893 shows disordered-IscU stabilization and slower D-to-S conversion, consistent with holdase behavior; GO0044183 explicitly distinguishes a holdase from folding assistance. Existing folding/refolding assertions remain UNDECIDED, not rejected merely because HscA is specialized. PMID9852006 abstract establishes suppression of selected-model-protein aggregation; indexed PMC full text was read, but local acquisition returned a checkpoint and no full-text artifact is claimed. PMID9707441 abstract distinguishes DnaK stress refolding from HscA. Peripheral membrane association remains possible despite cytosolic activity/no TM segment. The prior suspected partner correction was withdrawn pending the original interaction records; the intact payload is unchanged. Cold-induced expression is retained as an observation, without asserting a demonstrated adaptation mechanism.

All original ordered annotation payloads and historical NEW actions were preserved. Existing raw/provider/publication files were not refreshed. A genuine new default Falcon attempt returned HTTP 403; no provider report was fabricated. Manual source review is recorded here and in `analysis/module_audits/bacterial_isc_iron_sulfur_cluster_assembly/ecoli-consultation/`. The normal PAINT lineage-loss check found no IRD or IKR; donor-list length and target self-inclusion were not used as evidence against the ancestral assertion. Focused validation, render, and append-only helper-history results are recorded in the final handoff.


## 2026-11-07 PR6175 evidence-specific follow-up

Reviewed the disputed folding, oligomerization and sulfur-transport interpretations against fresh official GO definitions and primary assay context. See `analysis/module_audits/bacterial_isc_iron_sulfur_cluster_assembly/round1/ecoli-psepk-consultation/evidence.md` and source-provenance.json for exact access limits and the newly read full9852006 negative luciferase assay. Original ordered source payloads, all historical NEW rows and immutable sources are preserved. E. coli negative folding assays are not relabeled as KT2440 experiments; HscB structured-state stabilization remains distinct from HscA holdase behavior. The PSEPK HscA retired proposal lifecycle is deliberately untouched pending parent adjudication. No new annotation is added.
