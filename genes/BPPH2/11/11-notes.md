# Curation Notes: Bacillus phage phi29 Gene 11 (Proximal tail tube / lower collar protein gp11, P68930)

## Summary of Gene Function
- **Product**: Tail tube protein gp11 (also known as the lower collar protein p11; UniProt `P68930`, 293 aa, ~33.6 kDa).
- **Function & Assembly**: Forms the dodecameric (12-subunit) proximal part of the phi29 short non-contractile tail tube (the lower collar) immediately distal to the dodecameric portal/upper collar connector (`gp10`). It attaches to the connector after viral DNA packaging is complete, stabilizes the packaged genome within the head, serves as the attachment hub from which the 12 trimeric pre-neck appendages (`gp12*`) hang, and forms the proximal segment of the tail channel through which viral dsDNA is ejected into the *Bacillus subtilis* host cell ([PMID:6096227](file:///Users/cjm/orca/workspaces/ai-gene-review/aigr-agy-phages/publications/PMID_6096227.md), [PMID:11562162](file:///Users/cjm/orca/workspaces/ai-gene-review/aigr-agy-phages/publications/PMID_11562162.md), [11-uniprot.txt](file:///Users/cjm/.gemini/antigravity-cli/brain/4b846598-3920-4c66-ba84-db24d924c2d1/scratch/prd1_phi29/genes/BPPH2/11/11-uniprot.txt)).
- **Subcellular / Virion Location**: Virion tail tube (`GO:0098026`), forming the proximal dodecameric lower collar ring.

## Review of Existing GO Annotations
1. `GO:0046718` (`symbiont entry into host cell`, IEA, `GO_REF:0000043`): **TOO_GENERAL** — Entailed by the more specific annotation `GO:0099002` (`symbiont genome ejection through host cell envelope, short tail mechanism`) present on this record.
2. `GO:0098015` (`virus tail`, IEA, `GO_REF:0000043`): **TOO_GENERAL** — Entailed by the more specific tail sub-structure term `GO:0098026` (`virus tail, tube`) present on this record.
3. `GO:0098026` (`virus tail, tube`, IDA `PMID:6096227` and IEA `GO_REF:0000043`): **ACCEPT** — Directly reflects gp11 forming the proximal part of the phi29 tail tube (lower collar).
4. `GO:0099002` (`symbiont genome ejection through host cell envelope, short tail mechanism`, IEA, `GO_REF:0000043`): **ACCEPT** — Core biological process in which the gp11 tail tube forms the proximal conduit for dsDNA genome ejection across the host envelope.
