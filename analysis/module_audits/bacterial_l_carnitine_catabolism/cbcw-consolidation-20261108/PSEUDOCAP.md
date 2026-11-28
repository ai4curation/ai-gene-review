# Source-record defects for PSEUDOCAP

4 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTI7 enables GO:0005275 amine transmembrane transporter activity (IDA, PMID:19919675)
- **Field:** GO_ID
- **Change:** GO:0005275 → GO:0015418 (ABC-type quaternary ammonium compound transporting activity)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/cbcW/cbcW-ai-review.yaml`

PA5377 (CbcW permease, Q9HTI7) is annotated GO:0005275 amine transmembrane transporter activity, IDA, PMID:19919675. The substrates shown in that paper (choline, glycine betaine, L-carnitine) are quaternary ammonium compounds, which GO does not class as amines. GO:0015418 ABC-type quaternary ammonium compound transporting activity (with contributes_to for a permease subunit) is the accurate term. This row co-seeds the PAINT IBD at PTN000766131.

## 2. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTI7 involved_in GO:0031457 glycine betaine catabolic process (IDA, PMID:19919675)
- **Field:** GO_ID
- **Change:** check GO:0031457 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/cbcW/cbcW-ai-review.yaml`

PA5377 (CbcW, ABC permease) is annotated involved_in GO:0031457 glycine betaine catabolic process (IDA, PMID:19919675). The evidence is that cbc transposon mutants cannot grow on betaine as sole carbon source, which reflects loss of uptake. The permease does not catalyse any catabolic step. Consider removing the row, or keeping only GO:0031460 glycine betaine transport.

## 3. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTI7 involved_in GO:0042426 choline catabolic process (IDA, PMID:19919675)
- **Field:** GO_ID
- **Change:** check GO:0042426 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/cbcW/cbcW-ai-review.yaml`

PA5377 (CbcW, ABC permease) is annotated involved_in GO:0042426 choline catabolic process (IDA, PMID:19919675 and PMID:21478341). Both papers show that Cbc is needed for growth on choline as a carbon source, which reflects choline uptake. The permease does not perform any catabolic step. GO:0015871 choline transport already captures its role. Consider removing these rows.

## 4. WRONG_REFERENCE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTI7 involved_in GO:1902603 carnitine transmembrane transport (IDA, PMID:21478341)
- **Field:** DB:Reference
- **Change:** check PMID:21478341 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/cbcW/cbcW-ai-review.yaml`

GO:1902603 carnitine transmembrane transport for PA5377 (Q9HTI7) cites PMID:21478341 (Malek et al. 2011), whose abstract deals only with choline uptake by CbcXWV, BetT1 and BetT3. The carnitine evidence for CbcWV is in PMID:19919675 (PA14 cbc mutants fail to grow on carnitine, and PAO1 CbcWV restores CaiX-dependent carnitine uptake) and PMID:29517479. If PMID:21478341 has no carnitine data, please re-key the row. It is the sole seed of the PAINT IBD at PTN000766131.

> These transposon mutants also failed to grow on L-carnitine (Fig. S2), suggesting that carnitine is an additional substrate for this transporter.
> — PMID:19919675
