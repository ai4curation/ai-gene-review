# HNF1B (P35680) review notes

Deep research could not run because the only configured provider failed with
`claude_code: success Not logged in`; this review is grounded in the HNF1A
sibling review, the HNF1B UniProt record, the PTHR11568 PAINT node cache, and
the GOA-cited publications cached locally.

- PTHR11568 PAINT places `GO:0005634`, `GO:0000978`, `GO:0000981`, and
  `GO:0006357` on `PTN000170751`, which covers both reviewed human HNF1
  proteins. `just paint-losses human HNF1B` reported no IRD or IKR loss on the
  HNF1B lineage.
- The core molecular function is homeodomain/POU-like RNA polymerase
  II-directed transcription-factor activity. UniProt summarizes direct binding
  to the HNF1 inverted palindrome, HNF1A heterodimerization, HNF1B
  homodimerization, and PCBD1/PCBD2 coactivator interactions.
- HNF1B renal development rows are retained as direct transcriptional biology:
  human HNF1B mutations cause abnormal nephron development and Xenopus assays
  place HNF1B in the early nephrogenic transcription-factor network, including
  direct regulation of the `lhx1` promoter [PMID:10720943; PMID:21281489].
- Generic `GO:0005515` rows are removed unless the row captures a meaningful
  HNF1B partner. PCBD1 rows are refined to transcription coregulator binding,
  and HNF1A rows are refined to protein heterodimerization activity.
- InterPro/ARBA rows for insulin secretion, animal organ development, and
  system development overreach the direct HNF1B function. Pancreas and liver
  development are plausible non-core HNF1B contexts, whereas insulin secretion
  names a downstream beta-cell output rather than work that HNF1B performs.
