# K9IIP0 Research Notes

## Key findings
- UniProt names this protein Tumor necrosis factor-inducible gene 6 protein [file:DESRO/K9IIP0/K9IIP0-uniprot.txt "RecName: Full=Tumor necrosis factor-inducible gene 6 protein"].
- Deep research identifies K9IIP0 as TNFAIP6/TSG-6 with Link and CUB domains [file:DESRO/K9IIP0/K9IIP0-deep-research-falcon.md "UniProt accession K9IIP0 corresponds to tumor necrosis factor alpha-induced protein 6 (TNFAIP6/TSG-6) from Desmodus rotundus (vampire bat), with hallmark Link and CUB domains and hyaluronan-binding/link module and CUB superfamily annotations."].
- Deep research notes TSG-6 is secreted and inflammation-inducible [file:DESRO/K9IIP0/K9IIP0-deep-research-falcon.md "TNFAIP6/TSG-6 is a secreted, inflammation-inducible glycoprotein"]

## 2026-07-31 compliance review

**The UniProt CAUTION was being over-read.** The previous version used
[file:DESRO/K9IIP0/K9IIP0-uniprot.txt "CAUTION: Lacks conserved residue(s)
required for the propagation of"] to justify UNDECIDED on hyaluronan binding and
on secretion, and REMOVE on the anti-inflammatory term. But the caution is
scoped to `PROSITE-ProRule:PRU00059`, and PRU00059 is the **CUB** rule (it maps
to PROSITE PS01180; confirmed at prosite.expasy.org/unirule/PRU00059). The Link
module features in the same record cite a different rule, PRU00323. So the
caution constrains CUB-derived transfer only — not the Link module, not
secretion, not hyaluronan binding. Same pattern as K9IWX5, where the caution was
scoped to the ShKT rule.

Cross-checked every call against human TNFAIP6 (P98066) in QuickGO:

| Term | Human evidence | Old call | New call |
|---|---|---|---|
| `GO:0005540` HA binding | IDA ×2 (26468290, 26823460) | UNDECIDED | ACCEPT |
| `GO:0005615` extracellular space | `GO:0005576` IDA (1730767) | UNDECIDED | ACCEPT |
| `GO:0050728` neg. reg. inflammatory response | **IDA** (21569482) + IBA | REMOVE | ACCEPT |
| `GO:0016787` hydrolase activity | `GO:0106435` **IDA ×2** | REMOVE | MODIFY → `GO:0106435` |
| `GO:0007155` cell adhesion | IEA only, no experiment in any species | OVER_ANNOTATED | OVER_ANNOTATED (kept) |

**The hydrolase reversal is the substantive one.** The old reason was "No
evidence of hydrolase activity; annotation is keyword-based and unreliable."
That is factually wrong: TSG-6 catalyses covalent transfer of
inter-alpha-inhibitor heavy chains onto hyaluronan through an ester
intermediate. The UniProt record *for this protein* says so —
[file:DESRO/K9IIP0/K9IIP0-uniprot.txt "is required for transesterification of
the HC to hyaluronan."] — the deep research independently lists
[file:DESRO/K9IIP0/K9IIP0-deep-research-falcon.md "enzymatic transesterase
activity transferring I"]αI heavy chains among TSG-6's activities, and human
TNFAIP6 carries `GO:0106435` carboxylesterase activity from two direct assays
(PMID:16873769, PMID:20463016). `GO:0106435` is a descendant of `GO:0016787`
(verified via OLS ancestors), so the right move is MODIFY, not REMOVE.

Added `GO:0030212` hyaluronan metabolic process as NEW (ISS) — the BP
counterpart of that catalytic step, IDA-supported in human, and absent from the
DESRO GOA record.

The Vampirome study (PMID:23411029, cached) is the source of the EMBL record
(JAA46157.1) and confirms the protein in the gland proteome [PMID:23411029 "Of
note, expression of TSG-6 was confirmed by the proteome of the PS gland (Figure
2A)."] — 101 ions, third most abundant family. Worth following up: TSG-6
[PMID:23411029 "TSG-6 has been found to potentiate the antiplasmin activity of
inter"]-α-inhibitor, while the best-characterised vampire bat salivary protein
is a **plasminogen activator**. Whether those two are functionally coupled is
recorded as a knowledge gap.
