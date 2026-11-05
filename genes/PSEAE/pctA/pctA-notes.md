# pctA (PA4309, G3XD24) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE G3XD24 --alias pctA` (accession fetch). Accession
G3XD24 matches the worklist. No deep-research keys available; literature from cached
publications (PMID:9353923, PMID:23650915, PMID:16233808 abstract-only) and the UniProt
record.

## Identity

- Major amino acid chemoreceptor MCP, PTHR32089 (UniProt lists subfamily SF39). Two TM
  helices (11-31, 277-297) around a periplasmic dCache_1 (double PDC) ligand binding
  region (36-259), then HAMP and MCPsignal domains. Crystal structures of the LBR with
  bound amino acids (5LTX, 5T65, 5T7M, 9KOO). Paralog of PctB and PctC.

## Literature

- Major amino acid receptor. The pct deletion strain PCT2 shows no taxis to any of the
  20 L-amino acids; cloned pctA restores taxis to 18
  [PMID:9353923 "A null mutant strain PCT2, which contained a deletion in the entire pctC, orf1, pctA and pctB genes, did not show chemotaxis towards all 20 commonly occurring L-amino acids."];
  [PMID:9353923 "The pctA gene restored the ability of strain PCT2 to respond to 18 L-amino acids, suggesting that PctA plays a major role in detecting L-amino acids in P. aeruginosa."].
- Direct binding of 17 L-amino acids to the recombinant LBR
  [PMID:23650915 "We show that the recombinant ligand binding regions (LBRs) of PctA, PctB and PctC bind 17, 5 and 2 l-amino acids respectively."].
- Repellent responses to TCE/chloroform/methylthiocyanate [PMID:16233808]. UniProt also
  records histamine (indirect) and AI-2 chemotaxis.

## Annotation decisions

- Chemotaxis (IBA, IEA, IMP), response to amino acid (IEA, IMP): ACCEPT core.
  Amino acid binding (IDA, IEA): ACCEPT. Transmembrane signaling receptor activity (IEA):
  ACCEPT core MF. Plasma membrane (IEA): ACCEPT. Signal transduction (IEA): MODIFY to
  GO:0007166. Membrane (IEA): TOO_GENERAL.
- Action counts: ACCEPT 8, MODIFY 1, TOO_GENERAL 1.
- No source defects; the PseudoCAP seed row is sound.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001280296 | GO:0006935 chemotaxis | 10 | 215 (22 taxa) | GO:0006935, IMP, PMID:9353923 | SOUND | Deletion abolishes amino acid taxis; cloned pctA restores taxis to 18 amino acids; the LBR binds 17 amino acids directly. PctA performs the sensing step itself. | PctB, PctC, CtpH, CtpL, CtpM, Aer (PseudoCAP IMP); B. subtilis McpC (IDA/IMP positive chemotaxis); B. subtilis and H. salinarum HemAT (IDA aerotaxis) | Yes; independent IDA seeds and six other PseudoCAP seeds |

Node-level assessment of PTN001280296 is recorded once in `pctB-notes.md`; pctA is
consistent with it (SOUND, no GO_CENTRAL defect).
