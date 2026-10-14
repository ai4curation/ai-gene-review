# cbh1 (Trichoderma reesei / Hypocrea jecorina, P62694) notes

## 2026-10-01 re-review after GOA refresh

GOA was refreshed from remote. The following previously reviewed IEA rows are no longer present in the
current GOA snapshot and were marked `retired: true` (reviews kept; retirement is not a biological
REMOVE judgment):

- GO:0000272 polysaccharide catabolic process | IEA | GO_REF:0000043
- GO:0009251 glucan catabolic process | IEA | GO_REF:0000117
- GO:0016787 hydrolase activity | IEA | GO_REF:0000043
- GO:0016798 hydrolase activity, acting on glycosyl bonds | IEA | GO_REF:0000043
- GO:0030245 cellulose catabolic process | IEA | GO_REF:0000043 (the term remains the core process in
  core_functions and the proposed replacement for the current GO:0005975 row)

No new GOA rows. Re-audit fixes: several `supporting_text` quotes were paraphrases (not verbatim) of the
deep-research file and PMID:9041630; replaced with verbatim substrings. Added reasons/support to the two
MODIFY rows (GO:0004553, GO:0005975) that lacked them. No action changes.
