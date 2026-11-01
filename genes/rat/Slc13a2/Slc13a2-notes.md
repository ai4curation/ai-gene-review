# Slc13a2 notes

## Re-review 2026-10-10

GOA refresh changes:
- 3 new rows seeded, all ISO (GO_REF:0000121) with human SLC13A2 (UniProtKB:Q13183) as donor, duplicating existing mouse-sourced (MGI:MGI:1276558) ISO rows: GO:0015141 succinate transmembrane transporter activity, GO:0017153 sodium:dicarboxylate symporter activity, GO:0071422 succinate transmembrane transport.
- No rows retired.

Decisions:
- All three Q13183 donor-split rows ACCEPT, consistent with their mouse-sourced siblings and with rat IDA evidence [PMID:9694847 "When expressed in Xenopus oocytes, SDCT1 mediated electrogenic, sodium-dependent transport of most Krebs cycle intermediates (Km = 20-60 microM), including citrate, succinate, alpha-ketoglutarate, and oxaloacetate."].
- No existing actions changed. Re-audit confirmed: specific transporter/transport terms ACCEPT; generic parents (GO:0015370, GO:0022857, GO:0055085) MODIFY to the specific symporter/transport terms; localization terms KEEP_AS_NON_CORE; GO:0071285 cellular response to lithium ion (IBA, IEA, ISO, IDA) kept MARK_AS_OVER_ANNOTATED because Li+ acts as a competitive cation in transport assays [UniProtKB:P70545 "ACTIVITY REGULATION: Li(+) decreases succinate transport in the presence of Na(+), by competing at one of the three cation binding sites"]; it is a property of the transporter, not a cellular response executed by it. The lithium rows previously cited only paper titles; the UniProt ACTIVITY REGULATION line was added.
- 33 stale UniProt quotes (an older FUNCTION paraphrase) replaced with verbatim current FUNCTION, CATALYTIC ACTIVITY (per substrate) or SUBCELLULAR LOCATION lines.
- Description rewritten to remove review commentary.

Open questions:
- The IDA for cellular response to lithium ion cites PMID:9691021, whose abstract does not mention Li+ (the Li+ data in UniProt are attributed to PMID:9694847). A curator with the full text could confirm which paper reports the Li+ effect.

Review follow-up 2026-10-17: In response to PR #4622 review, five IDA rows citing PMID:9691021 now quote the abstract instead of the title [PMID:9691021 "rNaDC-1 mediated sodium-dependent uptake of di- and tricarboxylates"; "succinate, alpha-ketoglutarate, and glutarate were relatively high-affinity substrates, and citrate was a low-affinity substrate of rNaDC-1"; "rNaDC-1 is localized exclusively in the luminal membrane of S2 and S3"]. The cached abstract never mentions fumarate, so the two fumarate IDA rows say so and lean on the UniProt fumarate Rhea reaction; ACCEPT kept (curator's full text not cached). Apical plasma membrane added as the core-function location and the three GO:0016324 rows moved KEEP_AS_NON_CORE -> ACCEPT, consistent with Slc5a1. Suggested questions (Li+ source paper, fumarate substrate) and experiments added.
