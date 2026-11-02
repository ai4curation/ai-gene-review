# nirD curation notes

- Q88M68 is a 120-residue NirD-family protein with a Rieske-related fold, but characterized NirD lacks an Fe-S cluster or other electron-transfer cofactor. [PMID:22965870, "it does not contain any Fe-S cluster or other cofactors that might be involved in electron transfer"]
- NirD lacks the siroheme catalytic machinery and pyridine-nucleotide-binding domains of NirB, so it contributes to complex activity rather than independently enabling nitrite reduction.
- The nirB-nirD adjacency and family assignments support a two-subunit assimilatory nitrite reductase in KT2440.
- KT2440 literature explicitly identifies PP_1705 and PP_1706 as the assimilatory nitrite reductase. [PMID:32523942, "nirBD (PP_1705, PP_1706)"]
- The OpenScientist gene job completed without materializing a report. No provider text is claimed; the structural interpretation is grounded directly in PMID:22965870, the exact Q88M68 UniProt record, locus context, and verified PANTHER family membership.


## 2026-10-29 resumed nitrate audit: primary evidence and scope

The annotation-reviewer audit inspected every current row and core claim, preserving all machine payloads and immutable raw files. Broad supported terms are refined with MODIFY; ordinary imported relationship labels are not grounds for rejecting valid enzyme-complex contributions. No provider report was fabricated or refreshed. The foundation logs record the failed Falcon attempt; the genuine existing reports remain unchanged.

PMID:35285712 is a primary KT2440 pooled-mutant fitness study, not merely a thesis citation. Its exact gene-specific statement is: “We were also able to identify a distinct nitrate transporter PP_2092 (−2.6).” It also states: “However, no significant phenotype could be detected for this gene in the nitrite condition, suggesting that it may be specific to nitrate.” The authors explicitly allow PP_2092 or other transporters to provide nitrite transport. Absence of a fitness defect does not exclude redundant or conditional flux.

For reductases, the same paper states: “The enzymes associated with the initial steps of the assimilatory nitrogen system in P. putida are the reductases NarB and NirDB, for which we see significant growth phenotypes”. Figure 3 was visually inspected. It labels NarB and combined NirDB rather than accession-specific individual subunits. The pooled-mutant result supports the route, but no combined NirDB score is assigned separately to NirB or NirD, and no individual PP_1703 score is inferred solely from the generic NarB label.

PMID:38000372 directly studies KT2440 NasT/c-di-GMP regulation, nirBD transcription, NirB protein, and cell-lysate nitrite-reductase activity. Exact text: “the NalA-encoding sequence (nalA) is located upstream of the nirBD operon (PP_1705-PP_1706).” It reports “the induction of nirB expression was abolished in ΔnasT, while the induction of nalA expression was not affected in ΔnasT”. Its activity assay uses “3 mM methyl viologen, 1 mM KNO2, 17 mM Na2S2O4”, so this is not a measurement of the native NADH/NADPH preference. The perturbed gene is nasT; these experiments are not direct PP_1703 enzymology or a purified NirD assembly assay. PMID:32523942 likewise provides PP_1703/nirBD locus context in its introduction while directly perturbing nasT.

The 2026 P. putida Y-9 study (PMID:41980646) is available as a normally fetched abstract only. Its explicit nirB/nirD deletion and isotope-tracing results are comparative evidence. The strain's aerobic DNRA/ANRA phenotypes are not promoted to directly measured KT2440 physiology. Existing full-text access failures are documented rather than repeatedly retried.

The original machine GO:0008942 row is ACCEPT as a complex contribution. Its ordinary enables label is inert and cannot justify rejection. The inherited duplicate authored NEW GO:0008942 row was retired and preserved in full, with original ordinal 3, in nirD-source-analysis/retired-proposals.yaml; no machine row was removed.

The reproducible sequence analysis finds Cys18, Cys95 and His87 only. The canonical Rieske two-Cys/two-His ligand set is impossible in that sequence. Together with NirD-specific family membership and the explicitly cofactor-free Mycobacterium tuberculosis NirD structure in the PMID:22965870 abstract, this supports rejecting the fold-derived 2Fe-2S mapping. Full publisher access was blocked; the explicit abstract conclusion is used comparatively, not presented as a KT2440 structure. No native direct metal assay or universal exclusion of every noncanonical cofactor is claimed.

The inherited process and complex NEW proposals are retained on a structural enzyme-component role, not generic growth necessity or absence-based completeness. The target-specific structural role and requirement in reconstituted KT2440 NirBD remain open; NirD is not presumed to carry an electron-transfer cofactor.
