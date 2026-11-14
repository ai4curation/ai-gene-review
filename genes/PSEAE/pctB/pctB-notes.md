# pctB (Q9HW91, PA4310) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9HW91 --alias pctB` (accession fetch); accession Q9HW91 matches the worklist. Reviewed Swiss-Prot entry. No deep-research provider was used; literature found through the UniProt references and the PubMed MCP, and the cited papers were cached with `ai-gene-review fetch-pmid`. PMC full text could not be retrieved through the PubMed MCP for the PseudoCAP seed papers with PMC ids (empty body), so those were read as abstracts; the confidence rule is not engaged because no defect is recorded.

### Identity

- MCP with two TM helices (11-31, 277-297) around a periplasmic dCache_1 (double PDC) ligand binding region, cytoplasmic HAMP and MCPsignal domains (PF02743, PF00672, PF00015; PTHR32089:SF39). Crystal structures 5LT9/5LTO of the LBR.
- Paralogue of PctA and PctC; arose from an independent pctA duplication in the ancestor of P. aeruginosa [PMID:31964737 "PctA has a broad ligand range and responds to most of the proteinogenic amino acids, whereas PctB and PctC have a much narrower range"].

### Literature

- Seed paper [PMID:9353923 "The pctB and pctC genes complemented the defect in chemotaxis to only seven (Ala, Arg, Glu, Lys, Met, Tyr, Gln) and two (His, Pro) L-amino acids, respectively."] (abstract only). The deletion strain PCT2 lacks pctC-orf1-pctA-pctB.
- Direct binding [PMID:23650915 "We show that the recombinant ligand binding regions (LBRs) of PctA, PctB and PctC bind 17, 5 and 2 l-amino acids respectively."]; [PMID:23650915 "l-Gln, one of the three amino acids that is not recognized by PctA-LBR, was the most tightly binding ligand to PctB"]; pctB mutant loses L-Gln chemoattraction [PMID:23650915 "Bacteria were efficiently attracted to l-Gln and GABA, but mutation of pctB and pctC, respectively, abolished chemoattraction."] (abstract only).
- Repellent role [PMID:16233808 "This result demonstrates that PctA, PctB and PctC are also involved in repellent responses to chloroform and methylthiocyanate."].

### Annotation decisions

- Chemotaxis (IBA, IEA, IMP): ACCEPT, core. Response to amino acid (IMP, IEA): ACCEPT (no amino-acid chemotaxis term exists). Amino acid binding (IDA, IEA): ACCEPT.
- Plasma membrane IEA: ACCEPT; membrane IEA: TOO_GENERAL (plasma membrane is_a membrane). Signal transduction IEA: MODIFY to GO:0007166.
- NEW GO:0004888 transmembrane signaling receptor activity (IC), core MF; periplasmic LBR binding plus in vivo signalling.
- Action counts: ACCEPT 8, MODIFY 1, TOO_GENERAL 1, NEW 1.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001280296 | GO:0006935 chemotaxis | 10 | 215 (22 taxa) | GO:0006935, IMP, PMID:9353923 | SOUND | Abstract states complementation of the pct deletion strain by pctB restores chemotaxis to seven amino acids; pctB mutant later shown to lose L-Gln taxis, and the LBR binds the same ligands. | PctA, PctB/PctC, CtpH, CtpL, CtpM, Aer (PseudoCAP IMP); B. subtilis McpC (IDA/IMP positive chemotaxis); B. subtilis and H. salinarum HemAT (IDA aerotaxis) | Yes; independent IDA seeds (McpC, two HemATs) and six other PseudoCAP seeds |

No `source_defects` were recorded: the PseudoCAP row is sound and the IBD is sound.

### Node-level assessment, PTN001280296 (GO:0006935 chemotaxis)

The IBD (GO_Central, 2025-09-04) has ten WITH/FROM seeds: seven P. aeruginosa PseudoCAP seeds (PctC Q9HW93, CtpH G3XDA3, PctB Q9HW91, CtpM Q9I0I6, Aer Q9I3F6, CtpL Q9HUW6, PctA G3XD24) and three non-Pseudomonas seeds. Queried live in QuickGO on 2026-11-05, the three outside seeds carry their own experimental rows: B. subtilis McpC (P54576) GO:0050918 positive chemotaxis IDA PMID:23038252 and IMP PMID:9353924 (CACAO); B. subtilis HemAT (O07621) and H. salinarum HemAT (Q9HPR6) GO:0009454 aerotaxis IDA PMID:10676961 (UniProt). Aerotaxis and positive chemotaxis are both is_a chemotaxis (go-basic.obo), so every seed supports the node term.

All five PseudoCAP seeds reviewed in this batch are SOUND (mutant or complementation chemotaxis data for the receptor itself, several later backed by direct ligand binding). The IBD would stand without any one of them, and without all seven Pseudomonas seeds, on the B. subtilis and Halobacterium seeds. The node is a PTHR32089 MCP clade (215 leaf IBAs, 22 taxa: mostly Proteobacteria, Firmicutes, Archaea, Leptospira, Synechocystis), for which chemotaxis is the right level; no GO_CENTRAL defect is recorded. One leaf-level oddity: the Dictyostelium lysozyme-like proteins AlyL (Q54M35, F0ZEQ3; Pfam AlyA, no MCPsignal domain) are classified in PTHR32089 under this node and so inherit a chemotaxis IBA. That is a PANTHER family-placement problem for two leaves, not a fault in the IBD; it is raised as a suggested question on pctB, not as a defect.

This node-level assessment is recorded once, here on pctB; the pctC, ctpH, ctpM and aer notes cross-reference it. ctpL and pctA (the remaining PseudoCAP seeds) will be reviewed separately.
