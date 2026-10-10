# Notes for DANRE sult1st2

## 2026-05-09 review notes

- Core function is cytosolic PAPS-dependent sulfotransferase activity toward aryl/xenobiotic and estrogen substrates [file:DANRE/sult1st2/sult1st2-uniprot.txt "Sulfotransferase that utilizes 3'-phospho-5'-adenylyl sulfate"].
- Generic sulfotransferase activity was modified to aryl and estrone sulfotransferase activity because substrate testing supports those more informative terms [PMID:14726148 "activities toward two endogenous estrogens"].
- Xenobiotic metabolism is retained because hydroxychlorobiphenyl sulfation is directly described [PMID:12755695 "endogenous compounds and xenobiotics including hydroxychlorobiphenyls"].

## Re-review 2026-09-29

- GOA refresh replaced the old broad sulfotransferase-activity IEA reference (GO_REF:0000002) with a combined-IEA mapping (GO_REF:0000120, ARBA/InterPro). Removed the stale GO:0008146 IEA GO_REF:0000002 row (was flagged "not in GOA") and moved its MODIFY content onto the current GO:0008146 IEA GO_REF:0000120 row, keeping the MODIFY to the specific children aryl sulfotransferase (GO:0004062) and estrone sulfotransferase (GO:0004304).
- Resolved 2 further PENDING rows as ACCEPT, consistent with their reviewed siblings: GO:0005737 cytoplasm IBA (cytosolic SULT1), and GO:0006805 xenobiotic metabolic process IDA/involved_in (duplicate of the acts_upstream_of_or_within row).
- Both primary references are abstract-only (checked full_text_available: false). PMID:12755695 [Sugahara 2003] characterizes both zebrafish SULT1 enzymes and sult1st2 = "SULT1 ST2"; [PMID:12755695 "endogenous compounds and xenobiotics including hydroxychlorobiphenyls"] supports the sulfotransferase-activity and xenobiotic-metabolism IDA. PMID:14726148 [Ohkimoto 2004] characterizes a zebrafish estrogen-sulfating cytosolic ST strongly preferring estrone/E2 over T3/T4/DOPA/DHEA [PMID:14726148 "activities toward two endogenous estrogens"]; ZFIN attributes it to sult1st2, supporting the estrone-ST and estrogen-metabolic-process IDA (deferred to curator per the incomplete-evidence rule; noted in reference_review).
- Added reference_review (both HIGH/VERIFIED, abstract-only noted) to both PMIDs. Reduced reliance on falcon deep-research quotes for ACCEPT/MODIFY rows, anchoring supported_by on the UniProt FUNCTION/CATALYTIC line and the two primary abstracts. No REMOVE, no NEW. Validation: zero errors, zero warnings.
