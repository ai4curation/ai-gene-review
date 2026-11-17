# aer (Q9I3F6, PA1561) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I3F6 --alias aer` (accession fetch); accession Q9I3F6 matches the worklist. Reviewed Swiss-Prot entry. No deep-research provider was used; literature found through the UniProt references and the PubMed MCP, and the cited papers were cached with `ai-gene-review fetch-pmid`. PMC full text could not be retrieved through the PubMed MCP for the PseudoCAP seed papers with PMC ids (empty body), so those were read as abstracts; the confidence rule is not engaged because no defect is recorded.

### Identity

- Formerly TlpC. N-terminal PAS domain (21-76; PF08447 PAS_3), two TM helices (147-169, 174-193) separated by a four-residue loop, cytoplasmic MCPsignal domain (249-485); PTHR32089:SF74. No periplasmic sensor domain: the PAS domain is cytoplasmic, so the membrane segment is an anchor, as in E. coli Aer.

### Literature

- Seed paper [PMID:14987771 "Mutant strains which contained deletions in the methyl-accepting chemotaxis protein-like genes tlpC and tlpG showed decreased aerotaxis."]; [PMID:14987771 "A double mutant deficient in tlpC and tlpG was negative for aerotaxis."]; [PMID:14987771 "TlpC has 45% amino acid identity with the Escherichia coli aerotactic transducer Aer."] (abstract only).
- Regulation [PMID:16233612 "The anr mutation eliminated Aer-mediated aerotaxis, but not Aer-2-mediated aerotaxis."].
- Energy taxis [PMID:17933940 "We found that a robust energy taxis response mediated by the Aer receptor can sometimes mask chemotaxis mediated by other methyl-accepting chemotaxis proteins (MCPs)"].

### Annotation decisions

- Positive aerotaxis (IMP CACAO, IEA ARBA): ACCEPT, core. Aerotaxis IMP (PseudoCAP seed) and chemotaxis IBA/IEA: TOO_GENERAL (positive aerotaxis is_a aerotaxis is_a chemotaxis).
- GO:0004888 transmembrane signaling receptor activity (InterPro2GO): MODIFY to GO:0038023 signaling receptor activity; sensing and output are both cytoplasmic. No source defect recorded, since the schema has no InterPro resource; the mapping question is raised in suggested_questions.
- Signal transduction IEA: ACCEPT (cell surface receptor signalling does not apply). Plasma membrane ACCEPT; membrane TOO_GENERAL.
- Action counts: ACCEPT 4, MODIFY 1, TOO_GENERAL 4.

## PseudoCAP IBA-seed assessment

Node-level assessment: see genes/PSEAE/pctB/pctB-notes.md (recorded once there); summary repeated below.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001280296 | GO:0006935 chemotaxis | 10 | 215 (22 taxa) | GO:0009454 aerotaxis, IMP, PMID:14987771 (PseudoCAP); GO:0052131 positive aerotaxis, IMP, same PMID (CACAO) | SOUND | Abstract states the aer (tlpC) deletion decreases aerotaxis and the aer aer-2 double mutant is aerotaxis-negative; aerotaxis is_a chemotaxis, so the seed supports the node term. | PctA, PctB/PctC, CtpH, CtpL, CtpM, Aer (PseudoCAP IMP); B. subtilis McpC (IDA/IMP positive chemotaxis); B. subtilis and H. salinarum HemAT (IDA aerotaxis) | Yes; independent IDA seeds (McpC, two HemATs) and six other PseudoCAP seeds |

No `source_defects` were recorded; no GO_CENTRAL defect for the shared node.
