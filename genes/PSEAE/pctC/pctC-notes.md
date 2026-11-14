# pctC (Q9HW93, PA4307) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9HW93 --alias pctC` (accession fetch); accession Q9HW93 matches the worklist. Reviewed Swiss-Prot entry. No deep-research provider was used; literature found through the UniProt references and the PubMed MCP, and the cited papers were cached with `ai-gene-review fetch-pmid`. PMC full text could not be retrieved through the PubMed MCP for the PseudoCAP seed papers with PMC ids (empty body), so those were read as abstracts; the confidence rule is not engaged because no defect is recorded.

### Identity

- MCP with two TM helices (11-31, 280-300) around a periplasmic dCache_1 ligand binding region, cytoplasmic HAMP and MCPsignal domains (PF02743, PF00672, PF00015; PTHR32089:SF39). LBR structure 5LTV.
- Paralogue of PctA, from a pctA duplication in the ancestor of the genus Pseudomonas [PMID:31964737 "PctA has a broad ligand range and responds to most of the proteinogenic amino acids, whereas PctB and PctC have a much narrower range"].

### Literature

- Seed paper [PMID:9353923 "The pctB and pctC genes complemented the defect in chemotaxis to only seven (Ala, Arg, Glu, Lys, Met, Tyr, Gln) and two (His, Pro) L-amino acids, respectively."] (abstract only).
- Direct binding of two amino acids and GABA [PMID:23650915 "In addition, PctC-LBR recognized GABA but not any other structurally related compound."]; pctC mutant loses GABA taxis [PMID:23650915 "Bacteria were efficiently attracted to l-Gln and GABA, but mutation of pctB and pctC, respectively, abolished chemoattraction."].
- Histamine chemotaxis without histamine binding [PMID:30425146 "This chemotactic response is mediated by the concerted action of the TlpQ, PctA, and PctC chemoreceptors"]; full text: pctC in trans restored histamine chemotaxis of the deletion strain.
- Repellent role [PMID:16233808 "This result demonstrates that PctA, PctB and PctC are also involved in repellent responses to chloroform and methylthiocyanate."].

### Annotation decisions

- Same pattern as pctB (see genes/PSEAE/pctB/pctB-notes.md): chemotaxis, response to amino acid and amino acid binding rows ACCEPT; plasma membrane ACCEPT; membrane TOO_GENERAL; signal transduction MODIFY to GO:0007166; NEW GO:0004888 (IC), core MF.
- Action counts: ACCEPT 8, MODIFY 1, TOO_GENERAL 1, NEW 1.

## PseudoCAP IBA-seed assessment

Node-level assessment: see genes/PSEAE/pctB/pctB-notes.md (recorded once there); summary repeated below.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001280296 | GO:0006935 chemotaxis | 10 | 215 (22 taxa) | GO:0006935, IMP, PMID:9353923 | SOUND | Abstract states complementation of the pct deletion strain by pctC restores His and Pro chemotaxis; pctC mutant later shown to lose GABA taxis, and the LBR binds these ligands. | PctA, PctB/PctC, CtpH, CtpL, CtpM, Aer (PseudoCAP IMP); B. subtilis McpC (IDA/IMP positive chemotaxis); B. subtilis and H. salinarum HemAT (IDA aerotaxis) | Yes; independent IDA seeds (McpC, two HemATs) and six other PseudoCAP seeds |

No `source_defects` were recorded: the PseudoCAP row is sound and the IBD (shared with pctB, ctpH, ctpM, aer, ctpL, pctA) is sound; no GO_CENTRAL defect.
