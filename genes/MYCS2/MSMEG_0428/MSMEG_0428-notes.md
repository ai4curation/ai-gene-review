# MSMEG_0428 evidence review

## 2026-10-29: complex contribution and fold-to-cofactor transfer

Both original annotation payloads and raw records are unchanged. The ordered locus is retained as the symbol supplied by the target record; no alternate gene symbol was invented. Failed Falcon authentication is documented in the foundation log.

NirD-specific NCBIfam and PROSITE signatures support a small-subunit contribution to the NirB enzyme. [file:MYCS2/MSMEG_0428/MSMEG_0428-uniprot.txt "NCBIfam; TIGR02378; nirD_assim_sml; 1."] Native GlnR response data identify the paired nirBD system; mc2 155 and SMR5/MH1 experiments are distinguished. No independent small-subunit catalysis is asserted.

[PMID:22965870 "it does not contain any Fe-S cluster or other cofactors that might be involved in electron transfer."] This is the M. tuberculosis homolog, not a native M. smegmatis cofactor measurement. It shows why a Rieske-like fold is insufficient for the original electronic two-iron-binding claim. MARK_AS_OVER_ANNOTATED preserves that uncertainty; the target is not declared experimentally cofactor-free. No NEW rows were added to silence core-process coverage advisories.


## 2026-10-29: PR #5740 follow-up

An IC NEW GO:0042128 proposal now makes the existing core-process inference explicit. Specific NirD component classification plus native paired nirBD expression under nitrogen limitation supports participation as an enzyme component, not as a consumed substrate or unrelated necessary regulator. It remains weaker than a target-specific small-subunit perturbation/assembly assay, and no such experiment is claimed. Exact-term annotations are absent on PSEPK NirD Q88M68, ECOLI NirD P0A9I8 and BACSU NasE P42436; those negative comparators prevent an 'obvious omission' argument but do not negate the independent mechanistic evidence. Positive process annotation of the NasB electron-transfer component shows that enzyme-component participation is compatible with the term. The nitrate-assimilation parents do not exclude structural components, GO:0008942 does not entail that process, and no redundant process or A0QPK3 GO-CAM index hit occurs.

The extended ligand analysis finds Cys22/79/98 and His15/54. These totals permit, but do not establish, a canonical two-Cys/two-His set. Thus the target-specific impossibility argument used for PSEPK NirD does not transfer here; MARK_AS_OVER_ANNOTATED remains appropriate pending site/structure or occupancy evidence. Reproduction and results are in the PSEPK NirD source-analysis directory; the M. tuberculosis cofactor result remains comparative.
