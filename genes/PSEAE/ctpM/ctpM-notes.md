# ctpM (Q9I0I6, PA2652) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I0I6 --alias ctpM` (accession fetch); accession Q9I0I6 matches the worklist. Reviewed Swiss-Prot entry. No deep-research provider was used; literature found through the UniProt references and the PubMed MCP, and the cited papers were cached with `ai-gene-review fetch-pmid`. PMC full text could not be retrieved through the PubMed MCP for the PseudoCAP seed papers with PMC ids (empty body), so those were read as abstracts; the confidence rule is not engaged because no defect is recorded.

### Identity

- MCP with two TM helices (12-32, 206-226) around a periplasmic sCache_2 ligand binding domain (PF17200), cytoplasmic HAMP and MCPsignal domains (PTHR32089:SF119).

### Literature

- Seed paper [PMID:17933940 "We identified PA2652 as a chemoreceptor for malate by screening aer mcp double mutants by using swarm plate assays."] (abstract only; PMC body not returned).
- Follow-up, full text read [PMID:29391435 "the ligand binding domain (LBD) of the chemoreceptor PA2652 directly recognizes five C4-dicarboxylic acids"]; [PMID:29391435 "Quantitative chemotaxis assays of the mutant strain toward 10 mM ligand solutions showed a dramatic reduction in chemotaxis for all ligands"]; [PMID:29391435 "The study that reported its initial identification showed that a mutant in this gene did not respond to malate"]; [PMID:29391435 "we found that only the che pathway is involved in PA2652-mediated taxis"].

### Annotation decisions

- GO:0004888 IEA: ACCEPT, core MF. Positive chemotaxis IMP: ACCEPT, core.
- Chemotaxis IBA, IEA and IMP: TOO_GENERAL (positive chemotaxis is_a chemotaxis, accepted here), following the tier-2 is_a convention.
- Plasma membrane ACCEPT; membrane TOO_GENERAL; signal transduction MODIFY to GO:0007166.
- No GO term for malate or C4-dicarboxylate binding; raised as a suggested question rather than a NEW row.
- Action counts: ACCEPT 3, MODIFY 1, TOO_GENERAL 4.

## PseudoCAP IBA-seed assessment

Node-level assessment: see genes/PSEAE/pctB/pctB-notes.md (recorded once there); summary repeated below.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001280296 | GO:0006935 chemotaxis | 10 | 215 (22 taxa) | GO:0006935 and GO:0050918, IMP, PMID:17933940 | SOUND | Abstract names PA2652 as the malate chemoreceptor from mutant screening; the 2018 paper confirms loss of malate taxis in the mutant and direct malate binding by the LBD. | PctA, PctB/PctC, CtpH, CtpL, CtpM, Aer (PseudoCAP IMP); B. subtilis McpC (IDA/IMP positive chemotaxis); B. subtilis and H. salinarum HemAT (IDA aerotaxis) | Yes; independent IDA seeds (McpC, two HemATs) and six other PseudoCAP seeds |

No `source_defects` were recorded; no GO_CENTRAL defect for the shared node.
