## FBXL22

- **UniProt:** Q6P050 (FBXL22) · **batch:** proteostasis-batch-2026-06-13 (Falcon DR) · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|LRR` ; **PN-node mapping:** group `Cul1 substrate receptor`=`mapped`/ok_for_propagation→GO:1990756; F-box/LRR subtype+type=`no_mapping`; class=`context_only`/too_broad→GO:0061630.
- **Consistency:** Fully consistent. Falcon DR (cardiac Z-disc adaptor; ACTN2/FLNC substrates; zebrafish contractility; denervation atrogene), review YAML, the PN F-box LRR receptor placement, and the GO:1990756 group mapping all converge. No contradictions.
- **PN story / NEW pressure:** PN projects GO:1990756 (verified real) as new_to_goa. Review does not add it as NEW but reaches the same endpoint via **`action: MODIFY` of the existing GO:0061630 ubiquitin protein ligase activity (IDA, PMID:22972877) → proposed_replacement GO:1990756** — the canonical F-box correction (catalysis is in RBX1, not the receptor). Net effect = adaptor MF present, matching PN. Conclude: already addressed by review via MODIFY; concordant with PN projection.
- **Mapping strategy:** Gene supports the node. KEY PATTERN exemplary: review explicitly demotes the catalytic ligase MF (the MGI IDA "ligase activity," which over-attributes RBX1 chemistry to the receptor) to the GO:1990756 adaptor term. PN class-level GO:0061630 correctly flagged too_broad. No broader/narrower mismatch.
- **Evidence alignment:** PN reference is only "15340381 / rev"; review anchors on the gene-defining PMID:22972877 (HIGH/VERIFIED — Z-disc, ACTN2/FLNC, SKP1/CUL1, in vivo contractility) plus FBXL review PMID:33234069 and Falcon DR. Divergence benign — PN generic family review vs review's primary cardiac study.
- **Verdict:** Consistent; adaptor MF (GO:1990756) supplied via MODIFY of the mis-attributed catalytic term, matching PN. No over-reach.
- **Recommended edits:** none to FBXL22-ai-review.yaml; PN mappings sound as-is.
