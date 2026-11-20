# ctpH (G3XDA3, PA2561) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE G3XDA3 --alias ctpH` (accession fetch); accession G3XDA3 matches the worklist. Reviewed Swiss-Prot entry. No deep-research provider was used; literature found through the UniProt references and the PubMed MCP, and the cited papers were cached with `ai-gene-review fetch-pmid`. PMC full text could not be retrieved through the PubMed MCP for the PseudoCAP seed papers with PMC ids (empty body), so those were read as abstracts; the confidence rule is not engaged because no defect is recorded.

### Identity

- MCP with two TM helices (40-60, 217-237) around a periplasmic ligand binding domain, cytoplasmic HAMP and MCPsignal domains (PF00672, PF00015; PTHR32089:SF120). Constitutively expressed; not in the Pho regulon, unlike CtpL.

### Literature

- Seed paper [PMID:10852870 "Computer-assisted capillary assays showed that the ctpH single mutant failed to exhibit P(i) taxis when the concentration of P(i) in the capillary was higher than 5 mM."]; [PMID:10852870 "The ctpH ctpL double mutant was defective in P(i) taxis at any concentration ranging from 0.01 to 10 mM."] (abstract only; PMC body not returned).
- Direct binding, full text read [PMID:27353565 "We demonstrate that the ligand binding domain (LBD) of CtpH but not CtpL binds Pi directly."]; [PMID:27353565 "Data analysis revealed that the binding of CtpH-LBD with Pi has a KD of 22 μM (Table 1)."].

### Annotation decisions

- GO:0004888 IEA: ACCEPT, core MF. Chemotaxis (IBA, IEA, IMP): ACCEPT. Detection of phosphate ion IMP: ACCEPT (the receptor binds Pi itself).
- Plasma membrane ACCEPT; membrane TOO_GENERAL; signal transduction MODIFY to GO:0007166.
- NEW GO:0042301 phosphate ion binding (IDA, PMID:27353565).
- Action counts: ACCEPT 6, MODIFY 1, TOO_GENERAL 1, NEW 1.

## PseudoCAP IBA-seed assessment

Node-level assessment: see genes/PSEAE/pctB/pctB-notes.md (recorded once there); summary repeated below.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001280296 | GO:0006935 chemotaxis | 10 | 215 (22 taxa) | GO:0006935, IMP, PMID:10852870 | SOUND | Abstract states the ctpH mutant loses Pi taxis at high Pi and the ctpH ctpL double mutant at all Pi levels; CtpH-LBD binds Pi directly (PMID:27353565). | PctA, PctB/PctC, CtpH, CtpL, CtpM, Aer (PseudoCAP IMP); B. subtilis McpC (IDA/IMP positive chemotaxis); B. subtilis and H. salinarum HemAT (IDA aerotaxis) | Yes; independent IDA seeds (McpC, two HemATs) and six other PseudoCAP seeds |

No `source_defects` were recorded; no GO_CENTRAL defect for the shared node.
