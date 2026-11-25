# helX evidence review

## 2026-11-06 cytochrome maturation audit

Persistent marker: CYTOCHROME-RHOCB-helX-20261106.

Normal accession-aware fetch created the pristine scaffold; its complete original payloads and raw hashes were captured before editing in `.cache/module-audit-logs/cytochrome-20261106/rhodobacter-shewanella/RHOCB-helX-baseline.json`. All original annotations are retained. Default Falcon research was attempted normally and failed with HTTP 403 authentication/access denial; this file records manual literature review, not a provider report.

 The frozen target is SB1003; the primary work uses tagged/truncated R. capsulatus proteins and MT1131-derived complementation backgrounds. This is a conserved-role inference, not a direct assay of an unmodified SB1003 protein; construct provenance is documented in the source analysis.

Read the shared [construct scope](../ccl2/ccl2-source-analysis/construct-scope.md) and preserved primary Table 1 for precise strain, tag, truncation and donor boundaries. PMID18753134 remains abstract-only in the normal cache; its full PMC methods were inspected separately and the short strain excerpt is recorded in that analysis. PMID28634234 and PMID21956106 have full cached text.

GO:0015036: ACCEPT. Direct R. capsulatus biochemical assays support the reversible disulfide oxidoreductase class, with reduction of apocytochrome and CcmH-linked substrates as the biologically relevant direction. The frozen target is SB1003; the primary work uses tagged/truncated R. capsulatus proteins and MT1131-derived complementation backgrounds. This is a conserved-role inference, not a direct assay of an unmodified SB1003 protein; construct provenance is documented in the source analysis.

GO:0016491: MODIFY. The broad catalytic class is true; GO:0015036, already present, specifies the measured reaction rather than a different redox chemistry. The frozen target is SB1003; the primary work uses tagged/truncated R. capsulatus proteins and MT1131-derived complementation backgrounds. This is a conserved-role inference, not a direct assay of an unmodified SB1003 protein; construct provenance is documented in the source analysis.

GO:0017004: MODIFY. Reduction is a direct chemical contribution to cytochrome c-heme linkage, the supported descendant process. HelX is not assigned a stable CcmFHI complex membership merely from this role. The frozen target is SB1003; the primary work uses tagged/truncated R. capsulatus proteins and MT1131-derived complementation backgrounds. This is a conserved-role inference, not a direct assay of an unmodified SB1003 protein; construct provenance is documented in the source analysis.

GO:0030288: ACCEPT. The periplasmic catalytic domain is membrane tethered. The envelope supports the outer membrane-bounded periplasmic compartment; this does not assert that the entire protein is freely soluble. The frozen target is SB1003; the primary work uses tagged/truncated R. capsulatus proteins and MT1131-derived complementation backgrounds. This is a conserved-role inference, not a direct assay of an unmodified SB1003 protein; construct provenance is documented in the source analysis.

GO:0042597: MODIFY. The periplasmic catalytic domain is membrane tethered. The envelope supports the outer membrane-bounded periplasmic compartment; this does not assert that the entire protein is freely soluble. The frozen target is SB1003; the primary work uses tagged/truncated R. capsulatus proteins and MT1131-derived complementation backgrounds. This is a conserved-role inference, not a direct assay of an unmodified SB1003 protein; construct provenance is documented in the source analysis.

PMID18786143 full primary text adds a thiol-independent apocytochrome-holding role: cysteine-less CcmG* made from pCS1554 binds apocytochrome in vitro and supports cytochrome production in mutant backgrounds. Methods use E. coli expression and CcmG*-enriched extracts, not a purified native SB1003 flux assay. This specific chaperone role is represented by a proposed MF, without inventing a generic refolding annotation. The DsbA-null bypass shows the redox branch is not universally obligatory under every genetic condition.

## 2026-11-06 protein-substrate specificity follow-up

Persistent marker CYTOCHROME-RHOCB-HELX-PROTEIN-SPECIFICITY-20261106. Live QuickGO GO:0015035 specifies protein substrates, whereas GO:0015036 permits generic disulfide substrates; both definitions are reversible. PMID28634234 protein-thiol and mixed-disulfide assays justify the more specific MF. Refined the core and both original generic MF review decisions to GO:0015035, preserving every original annotation payload and construct/strain caveat. This corrects biological granularity independently of module capacity checking.
