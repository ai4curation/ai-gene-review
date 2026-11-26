# TSHR notes

- Core function: TSHR is a basolateral receptor for TSH and thyrostimulin that couples through Gs/adenylate cyclase and through PLC-linked G proteins. Keep the specific `thyroid-stimulating hormone receptor activity`, `thyroid-stimulating hormone signaling pathway`, adenylate-cyclase GPCR signaling, PLC-activating GPCR signaling, and basolateral/plasma-membrane rows.
- Correct but generic GPCR rows remain acceptable when their row evidence only reaches the receptor family level. The broad `signaling receptor activity`, `cell surface receptor signaling pathway`, `cell-cell signaling`, and `membrane` rows are less informative than the more specific rows and are reviewed accordingly.
- The two GOA rows for `GO:0005515 protein binding` with PMID:15775968 and `UniProtKB:Q14160` are true duplicate rows in the file, one from IntAct and one from UniProt. Keep both YAML entries distinct under issue #7042.
- Remove `cellular response to thyrotropin-releasing hormone`: the cited glycoprotein-hormone paper concerns TSH/thyrotropin receptor activation, whereas TRH is the hypothalamic tripeptide acting on TRHR.
- Brown-adipose thermogenesis is left non-core because it is a mouse/rat orthology-supported tissue role and not the thyroid follicular TSHR signaling mechanism.
