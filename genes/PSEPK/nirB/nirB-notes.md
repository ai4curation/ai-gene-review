# nirB curation notes

- Q88M69 is an 850-residue NirB-family nitrite reductase large subunit assigned EC 1.7.1.4. [file:PSEPK/nirB/nirB-uniprot.txt, "Nitrite reductase [NAD(P)H] large subunit"]
- UniProt assigns FAD, siroheme, 2Fe-2S, and 4Fe-4S cofactors, consistent with the complete catalytic and electron-transfer machinery of NirB. [file:PSEPK/nirB/nirB-uniprot.txt, "Binds 1 [4Fe-4S] cluster per subunit."]
- The adjacent 120-residue NirD protein is the non-catalytic accessory small subunit. Its Rieske-related fold lacks an Fe-S cluster. [PMID:22965870, "it does not contain any Fe-S cluster or other cofactors that might be involved in electron transfer"]
- KT2440 literature identifies PP_1705 and PP_1706 as the assimilatory nitrite reductase. [PMID:32523942, "nirBD (PP_1705, PP_1706)"]
- NADH-versus-NADPH preference and direct KT2440 biochemistry remain unresolved.
- The OpenScientist gene job completed without materializing a report. No provider text is claimed; this review therefore rests on GOA/UniProt, the completed PP_1703 pathway-context report, PMID:32523942, PMID:22965870, and verified PANTHER family grounding.


## 2026-10-29 resumed nitrate audit: primary evidence and scope

The annotation-reviewer audit inspected every current row and core claim, preserving all machine payloads and immutable raw files. Broad supported terms are refined with MODIFY; ordinary imported relationship labels are not grounds for rejecting valid enzyme-complex contributions. No provider report was fabricated or refreshed. The foundation logs record the failed Falcon attempt; the genuine existing reports remain unchanged.

PMID:35285712 is a primary KT2440 pooled-mutant fitness study, not merely a thesis citation. Its exact gene-specific statement is: “We were also able to identify a distinct nitrate transporter PP_2092 (−2.6).” It also states: “However, no significant phenotype could be detected for this gene in the nitrite condition, suggesting that it may be specific to nitrate.” The authors explicitly allow PP_2092 or other transporters to provide nitrite transport. Absence of a fitness defect does not exclude redundant or conditional flux.

For reductases, the same paper states: “The enzymes associated with the initial steps of the assimilatory nitrogen system in P. putida are the reductases NarB and NirDB, for which we see significant growth phenotypes”. Figure 3 was visually inspected. It labels NarB and combined NirDB rather than accession-specific individual subunits. The pooled-mutant result supports the route, but no combined NirDB score is assigned separately to NirB or NirD, and no individual PP_1703 score is inferred solely from the generic NarB label.

PMID:38000372 directly studies KT2440 NasT/c-di-GMP regulation, nirBD transcription, NirB protein, and cell-lysate nitrite-reductase activity. Exact text: “the NalA-encoding sequence (nalA) is located upstream of the nirBD operon (PP_1705-PP_1706).” It reports “the induction of nirB expression was abolished in ΔnasT, while the induction of nalA expression was not affected in ΔnasT”. Its activity assay uses “3 mM methyl viologen, 1 mM KNO2, 17 mM Na2S2O4”, so this is not a measurement of the native NADH/NADPH preference. The perturbed gene is nasT; these experiments are not direct PP_1703 enzymology or a purified NirD assembly assay. PMID:32523942 likewise provides PP_1703/nirBD locus context in its introduction while directly perturbing nasT.

The 2026 P. putida Y-9 study (PMID:41980646) is available as a normally fetched abstract only. Its explicit nirB/nirD deletion and isotope-tracing results are comparative evidence. The strain's aerobic DNRA/ANRA phenotypes are not promoted to directly measured KT2440 physiology. Existing full-text access failures are documented rather than repeatedly retried.

NirB is reviewed as a catalytic component of the NirBD complex. NirB-specific NCBIfam and cofactor/domain evidence replace circular product-name/EC and ARBA-only pathway support. Native activity measurements establish the pathway context, not pyridine-nucleotide preference. GO:0050661 means binding NADP+ or NADPH; it does not imply exclusive preference. With no direct native specificity assay, that row is UNDECIDED, not rejected because NADH is also plausible. The Pfam BFD-like domain and PIRSR 4Fe-4S sites independently support the two cluster types. Heme binding is retained for siroheme because no verified more specific siroheme-binding GO term was identified.

The inherited NEW complex-membership row remains a conserved-assembly inference from the specific family, paired native operon, and comparative NirBD evidence. No native KT2440 purified stoichiometry is claimed. The core uses contributes_to_molecular_function to state the complex context explicitly.

### 2026-10-29: qualification of the earlier NirD cofactor statement

The earlier statement that the adjacent KT2440 NirD lacks an Fe-S cluster is an inference from the NirD-specific sequence/family evidence and the characterized **M. tuberculosis** homolog, not a direct measurement of Q88M68 cofactor occupancy. PMID:22965870 states that its Mtb protein "does not contain any Fe-S cluster or other cofactors that might be involved in electron transfer." The current NirD review retains that distinction and does not present the Mtb structure as a KT2440 experiment.
