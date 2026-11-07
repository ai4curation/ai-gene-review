# ccl2 evidence review

## 2026-11-06 cytochrome maturation audit

Persistent marker: CYTOCHROME-RHOCB-ccl2-20261106.

Normal accession-aware fetch created the pristine scaffold; its complete original payloads and raw hashes were captured before editing in `.cache/module-audit-logs/cytochrome-20261106/rhodobacter-shewanella/RHOCB-ccl2-baseline.json`. All original annotations are retained. Default Falcon research was attempted normally and failed with HTTP 403 authentication/access denial; this file records manual literature review, not a provider report.

 The frozen target is SB1003; the primary work uses tagged/truncated R. capsulatus proteins and MT1131-derived complementation backgrounds. This is a conserved-role inference, not a direct assay of an unmodified SB1003 protein; construct provenance is documented in the source analysis.

Read the shared [construct scope](../ccl2/ccl2-source-analysis/construct-scope.md) and preserved primary Table 1 for precise strain, tag, truncation and donor boundaries. PMID18753134 remains abstract-only in the normal cache; its full PMC methods were inspected separately and the short strain excerpt is recorded in that analysis. PMID28634234 and PMID21956106 have full cached text.

GO:0005886: ACCEPT. The conserved single C-terminal transmembrane helix and periplasmic redox domain support this location. TreeGrafter inference is consistent with target architecture; it is not evidence of heme transport. The frozen target is SB1003; the primary work uses tagged/truncated R. capsulatus proteins and MT1131-derived complementation backgrounds. This is a conserved-role inference, not a direct assay of an unmodified SB1003 protein; construct provenance is documented in the source analysis.

GO:0042597: MODIFY. The conserved single C-terminal transmembrane helix and periplasmic redox domain support this location. TreeGrafter inference is consistent with target architecture; it is not evidence of heme transport. The frozen target is SB1003; the primary work uses tagged/truncated R. capsulatus proteins and MT1131-derived complementation backgrounds. This is a conserved-role inference, not a direct assay of an unmodified SB1003 protein; construct provenance is documented in the source analysis.

GO:0015036: NEW. Purified R. capsulatus CcmH Cys variants participate in quantified thiol-disulfide exchange; this adds the missing molecular activity rather than inferring catalysis from essentiality. The stereospecific ligation sequence is a mechanistic model supported by differential reactivity, not a fully observed native intermediate pathway. The frozen target is SB1003; the primary work uses tagged/truncated R. capsulatus proteins and MT1131-derived complementation backgrounds. This is a conserved-role inference, not a direct assay of an unmodified SB1003 protein; construct provenance is documented in the source analysis.

The core/row-coverage advisory for GO:0018063 is retained: direct chemical participation is described in the core, but no extra process row is manufactured to silence the validator. The new oxidoreductase MF is independently supported. UniProt predicted covalent-heme sites at Cys42/45 are flagged for upstream review against redox-cysteine experiments.

## 2026-11-06 source packaging

Persistent marker CYTOCHROME-RHOCB-ccl2-SOURCE-PACKAGING-20261106. Moved the full acquired primary PDF and extraction to the ignored audit acquired-sources cache, preserving byte hashes. The committed source analysis now contains only scoped strain/construct table excerpts and URL/hash provenance. Gene review assertions, quotes, machine payloads, UniProt/GOA files and normal publication caches were unchanged.


## PR6121 round-1 specificity follow-up (2026-11-06)

The historical NEW GO:0015036 payload and core are unchanged. Current QuickGO definitions of GO:0015035 and GO:0015036 both express a reversible sulfide/disulfide reaction; protein substrate scope, not an assumed net direction, distinguishes them. PMID28634234 measures protein-associated thiol-disulfide exchange using CcmH variants and TNB adducts, and discusses a slower alternative involving reduced CcmH. That evidence does not justify claiming CcmH lacks reducing chemistry. A separate specificity review should distinguish the protein intermediates from assay adducts before refining the core, while preserving the exact historical NEW assertion. Parent instruction defers that non-blocking refinement.


## PR6121 reference-finding follow-up (2026-11-06)

Narrowed the top-level finding statements for file:RHOCB/ccl2/ccl2-source-analysis/construct-scope.md to the claims established by their existing quoted passages. Annotation actions, core functions, quotes and source records are unchanged. The original 52-file handoff remains preserved and verified separately; this edit has a supplemental history and manifest.
