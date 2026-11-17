# ccl1 evidence review

## 2026-11-06 cytochrome maturation audit

Persistent marker: CYTOCHROME-RHOCB-ccl1-20261106.

Normal accession-aware fetch created the pristine scaffold; its complete original payloads and raw hashes were captured before editing in `.cache/module-audit-logs/cytochrome-20261106/rhodobacter-shewanella/RHOCB-ccl1-baseline.json`. All original annotations are retained. Default Falcon research was attempted normally and failed with HTTP 403 authentication/access denial; this file records manual literature review, not a provider report.

 The frozen target is SB1003; the primary work uses tagged/truncated R. capsulatus proteins and MT1131-derived complementation backgrounds. This is a conserved-role inference, not a direct assay of an unmodified SB1003 protein; construct provenance is documented in the source analysis.

Read the shared [construct scope](../ccl2/ccl2-source-analysis/construct-scope.md) and preserved primary Table 1 for precise strain, tag, truncation and donor boundaries. PMID18753134 remains abstract-only in the normal cache; its full PMC methods were inspected separately and the short strain excerpt is recorded in that analysis. PMID28634234 and PMID21956106 have full cached text.

GO:0005886: ACCEPT. Detergent extraction and reciprocal affinity purification place CcmF in a membrane-integral CcmFHI complex. The plasma membrane is the supported refinement of generic membrane. The frozen target is SB1003; the primary work uses tagged/truncated R. capsulatus proteins and MT1131-derived complementation backgrounds. This is a conserved-role inference, not a direct assay of an unmodified SB1003 protein; construct provenance is documented in the source analysis.

GO:0015232: MARK_AS_OVER_ANNOTATED. CcmF binds heme and contributes to periplasmic ligation. These findings do not demonstrate movement of heme from one side of the membrane to the other by this target; nor do they directly exclude all such movement. The electronic transporter assignment exceeds the established molecular role. The frozen target is SB1003; the primary work uses tagged/truncated R. capsulatus proteins and MT1131-derived complementation backgrounds. This is a conserved-role inference, not a direct assay of an unmodified SB1003 protein; construct provenance is documented in the source analysis.

GO:0015886: MODIFY. The broad heme-transport label conflates heme handling with transmembrane transport; the replacement is a lateral correction to the established ligation process. R. capsulatus physical complex evidence and comparative CcmFH functional reconstruction support participation, not isolated CcmF catalysis. The frozen target is SB1003; the primary work uses tagged/truncated R. capsulatus proteins and MT1131-derived complementation backgrounds. This is a conserved-role inference, not a direct assay of an unmodified SB1003 protein; construct provenance is documented in the source analysis.

GO:0016020: MODIFY. Detergent extraction and reciprocal affinity purification place CcmF in a membrane-integral CcmFHI complex. The plasma membrane is the supported refinement of generic membrane. The frozen target is SB1003; the primary work uses tagged/truncated R. capsulatus proteins and MT1131-derived complementation backgrounds. This is a conserved-role inference, not a direct assay of an unmodified SB1003 protein; construct provenance is documented in the source analysis.

GO:0017004: MODIFY. The assembly term can be refined to its cytochrome c-heme linkage descendant. R. capsulatus physical complex evidence and comparative CcmFH functional reconstruction support participation, not isolated CcmF catalysis. The frozen target is SB1003; the primary work uses tagged/truncated R. capsulatus proteins and MT1131-derived complementation backgrounds. This is a conserved-role inference, not a direct assay of an unmodified SB1003 protein; construct provenance is documented in the source analysis.

GO:0020037: ACCEPT. The CcmF family contains a stable noncovalent heme cofactor and heme-handling architecture. Comparative CcmF biochemistry supports the target inference; no SB1003 binding constant or purified target assay is claimed. The frozen target is SB1003; the primary work uses tagged/truncated R. capsulatus proteins and MT1131-derived complementation backgrounds. This is a conserved-role inference, not a direct assay of an unmodified SB1003 protein; construct provenance is documented in the source analysis.

GO:0004408: NEW. The CcmFH functional reconstruction establishes complex-level synthase activity. R. capsulatus CcmF physically associates with CcmH and CcmI in the functional membrane machinery. The contributes_to qualifier explicitly avoids assigning the entire reaction to isolated CcmF; the reconstructed reaction is comparative E. coli evidence. The frozen target is SB1003; the primary work uses tagged/truncated R. capsulatus proteins and MT1131-derived complementation backgrounds. This is a conserved-role inference, not a direct assay of an unmodified SB1003 protein; construct provenance is documented in the source analysis.


## PR6121 round-1 evidence correction (2026-11-06)

- GO:0015886 ACCEPT: CcmF participates in intracellular heme delivery to the ligation machinery.
- Move repeated SB1003/MT1131 construct caveat to source reference assessment; preserve per-row biological rationale.

Current GO definitions were checked against the official QuickGO API. All original annotation payloads, including authored NEW rows, are preserved. Primary scope and construct limits remain explicit; no raw UniProt/GOA, provider report or publication cache was edited. Scoped comparative proof is recorded in the round-1 audit.


## PR6121 reference-finding follow-up (2026-11-06)

Narrowed the top-level finding statements for PMID:24397552, file:RHOCB/ccl2/ccl2-source-analysis/construct-scope.md to the claims established by their existing quoted passages. Annotation actions, core functions, quotes and source records are unchanged. The original 52-file handoff remains preserved and verified separately; this edit has a supplemental history and manifest.
