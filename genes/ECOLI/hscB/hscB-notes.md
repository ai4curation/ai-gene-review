# hscB (P0A6L9, E. coli K-12) notes

Provider deep research could not run: `just deep-research-falcon` failed with Edison API 403 (auth), 2026-10-23. These notes are from the cached publications and the UniProt record.

## Function
- J-type co-chaperone (Hsc20) for HscA. It binds IscU and HscA and synergistically stimulates HscA ATPase [PMID:10869428 "Addition of both Hsc20 and IscU to Hsc66 resulted in a dramatic stimulation, increasing the ATPase activity of Hsc66 ≈100-fold over the level observed in the presence of Hsc20 or IscU alone and >400-fold over the basal intrinsic activity."]
- HscB has no intrinsic chaperone activity [PMID:10869428 "In contrast to DnaJ, however, Hsc20 does not display intrinsic chaperone activity and lacks the C-terminal domains necessary for Hsp40 interactions with unfolded polypeptides"]
- The C-domain conserved patch is the IscU binding site [PMID:18702525 "We propose that the conserved patch in the C-domain of HscB is the principal binding site for IscU."]
- Weak IscS interaction [PMID:27730125 "We document a previously undetected weak interaction between the chaperone HscB and the desulfurase IscS, one of the two main players of the machine."]

## Curation decisions
- Core MF is GO:0001671 ATPase activator activity, in GO:0044571 [2Fe-2S] cluster assembly, part of GO:1990230. This matches the module.
- GO:0051087 is changed to GO:0030544 Hsp70 protein binding. GO:0006457 is marked as over-annotated. GO:0051259 is removed (the HscB C-terminal "oligomerisation" domain is the IscU-binding module).
- Protein-binding rows: one is changed to Hsp70 protein binding (the HscA partner); the others are removed per the protein-binding policy.
- P15288 (PepD) comes from a high-throughput pull-down only.


## 2026-11-07 ISC whole-gene re-review

Specialization and monomeric structure do not disprove generic folding or heterooligomer assembly. PMID22782893 shows structured-IscU stabilization, but a folding/recovery endpoint is unresolved; GO0051259 includes heteromers, and complex membership does not by itself show assembly promotion. Both broad processes remain UNDECIDED. Direct HscA activation and targeting/cluster-transfer activity are retained. Current QuickGO confirms Hsp70 binding is a descendant of both chaperone binding and heat-shock-protein binding.

All original ordered annotation payloads and historical NEW actions were preserved. Existing raw/provider/publication files were not refreshed. A genuine new default Falcon attempt returned HTTP 403; no provider report was fabricated. Manual source review is recorded here and in `analysis/module_audits/bacterial_isc_iron_sulfur_cluster_assembly/ecoli-consultation/`. The normal PAINT lineage-loss check found no IRD or IKR; donor-list length and target self-inclusion were not used as evidence against the ancestral assertion. Focused validation, render, and append-only helper-history results are recorded in the final handoff.
