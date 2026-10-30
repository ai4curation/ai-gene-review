# statC notes

## 2026-09-20 focused report incorporation

Read the complete OpenScientist proliferation/defense report, verified new PMID:26927887 and PMID:20159963 leads, and rechecked primary PMID:14701681/17673666/12771188/11336701/24587195 and the current PAINT node. The report's strongest positive findings are legitimate: STATb has a subtle competitive-growth phenotype; TirA and NADPH oxidases support antibacterial sentinel-cell function; STATc uses noncanonical kinase/phosphatase signaling and regulates stress/developmental transcription. These do not establish loss of the two broad inherited processes in STATc.

The report expressly admits: "The gap is not that statC was tested and found negative for proliferation" and "Its role (if any) in defense is untested rather than experimentally excluded". Its REFUTED/NOT recommendations therefore exceed its evidence. Live GO:0042127 requires modulation of proliferation, not cytokine/JAK signaling; GO:0006952 requires restriction of damage after foreign-body exposure or injury, not metazoan interferon signaling. The source STATb growth phenotype with noncanonical activation itself disproves the claim that a Dictyostelium STAT cannot regulate growth without JAK. Positive defense effectors are not an exhaustive inventory excluding transcription factors.

PTHR11801 places both processes at PTN000927860, while detailed cytokine terms are separately placed at metazoan nodes. An IBA reflects ancestral-node placement, not a pairwise transfer that becomes erroneous merely because a paralog supplies evidence. Both disputed rows are restored to KEEP_AS_NON_CORE, with exact report caveats and source excerpts. This does not claim a target-specific growth or defense experiment. Oxidative stress is not equated with defense, and differentiation timing is not equated with proliferation. The report is recorded as DISPUTED; no NOT annotation or new process term is manufactured. No duplicate report is needed.


## Recovery PR evidence follow-up (2026-09-22)

Anchor the retained STAT defense inference to the actual PAINT IBD row, or remove the unsupported negative ACG/SDF-1 assertion from supporting evidence; keep the report assessment in the reason.

## Literature review integration (2026-10-04)

- Liongue & Ward 2013 (PMID:24058787) and Wang & Levy 2012 (PMID:24058748) added to the GO:0007259 -> GO:0097696 MODIFY.
  JAK is a metazoan innovation [PMID:24058787 "The first bona fide JAK-like protein is represented in the basal metazoan porifera lineage"],
  and the pathway was assembled in bilateria [PMID:24058787 "the interaction of these proteins to form an active pathway, which occurred in bilateria"].
  Dictyostelium STAT signaling lies outside the Metazoa [PMID:24058748 "The discovery of STAT signaling in Dictyostelium extended this intercellular phosphotyrosine pathway beyond the Metazoa"].
- Implication for PAINT: the GO:0007259 IBD sits at PTN000927860, which includes the Dictyostelium STATs.
  On Liongue's timeline the JAK-dependent pathway arose in bilateria, so that IBD is placed deeper than the
  pathway's origin. The node placement is the root cause, not just term scoping. The propagation_review
  root_cause (TERM_SCOPING_PROBLEM) was left unchanged.
- Slime mold STATs lack the transactivation and N-terminal domains [PMID:24058748 "However, they lack the N-terminal and transactivation domains characteristic of STAT proteins from higher organisms"].
- Kawata 2011 (PMID:21534947) was not added. Its abstract makes no STATc-specific statement.
- No actions changed.

Cross-gene briefing for GO editors and PAINT curators: https://claude.ai/artifact/4MLfbbbWWnLchDvspwdPuM
