# ATP1B4 notes

## 2026-10-05 review (PAINT, affinage)

- Co-option [PMID:17592128 "In placental mammals beta m-proteins lost their ancestral functions, accumulate in nuclear membrane of perinatal myocytes, and associate with transcriptional coregulator Ski-interacting protein (SKIP)."].
- Removed the ancestral pump rows: Na,K-ATPase complex, K+ and Na+ transport, and transmembrane transport (IEA); transmembrane transporter activity and plasma membrane (TAS, 1999). Human BetaM does not coimmunoprecipitate with alpha-subunits, and a curated NOT transmembrane transport IDA row already exists. The 1999 paper's inference is recorded with finding_review OVERTURNED, superseded by PMID:17592128.
- The SKIP (SNW1) IPI was changed to transcription coregulator binding (GO:0001221). Seven HuRI IPIs were removed.
- MyoD/BRG1 [PMID:36836771 "BetaM binds to the distal regulatory region (DRR) of MyoD, promotes epigenetic changes associated with activation of transcription, and recruits the SWI/SNF chromatin remodeling subunit, BRG1."]. GO:0045944 was not added, because it is a descendant of the GO:0006355 the gene already carries; see the revisions below for the GO:0003712 NEW row.

## 2026-10-05 revision (reviewer round 1)

- Fixed a UniProt quote truncated at a line wrap. "function as a Na,K-ATPase beta-subunit." dropped the preceding "Has lost its ancestral" and so read as the opposite. It is replaced by the SUBUNIT line "does not associate with known Na,K-ATPase alpha-subunits."
- Added NEW GO:0003712 transcription coregulator activity (ISO from mouse Q99ME6, PMID:36836771) and set it as the core MF. Comparator: SNW1/SKIP carries coactivator and corepressor activity by IDA.

## 2026-10-05 revision (reviewer round 2)

- The GO:0003712 row was wrongly coded ISO from mouse Q99ME6. PMID:36836771 expressed *human* BetaM (the constructs from PMID:17592128) in mouse C2C12 cells, which have no endogenous BetaM, and its in vivo ChIP and EMSA used *rat* neonatal muscle. Changed to IDA with no supporting_entities, and corrected the species in the reference_review. Also removed an unsupported "no DNA-binding domain" phrase.
