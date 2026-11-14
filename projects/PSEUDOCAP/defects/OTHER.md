# Source-record defects for OTHER

1 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** InterPro:IPR028359
- **Subject:** UniProtKB:G3XD94
- **Change:** GO:0016628 → GO:0016616 (oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/wbpA/wbpA-ai-review.yaml`

InterPro2GO: IPR028359 (UDP-ManNAc/GlcNAc dehydrogenase) maps to GO:0016628 (CH-CH group of donors). Family members (WbpA EC 1.1.1.136, WecC EC 1.1.1.336) oxidise the C6 hydroxymethyl group of the sugar, a CH-OH donor. The mapping should be GO:0016616.
