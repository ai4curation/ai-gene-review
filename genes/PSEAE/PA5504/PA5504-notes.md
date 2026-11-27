# PA5504 (Q9HT69) notes

PubMed search returned API errors on 2026-11-05. Johnson et al. 2008 full text
is cached.

## Literature

- Mutant phenotype [PMID:18833300 "A PA5504 knockout affected growth on L-histidine as a carbon source (Table 2), however its expression was not induced by this compound."]; Table 2 gives "L-Histidine – C+/−" (reduced, not abolished).
- Operon context [PMID:18833300 "PA5504 encodes a predicted membrane component of an ABC amino acid transporter, and is encoded in a putative two gene operon along with an ATP-binding component gene."].
- UniProt: NCBIfam metI; PANTHER PTHR30450:SF1 D-methionine transport system
  permease MetI-related; neighbour PA5503 is reviewed MetN2 (methionine import
  ATP-binding protein); PA5502 lipoprotein (MetQ-like).

## PseudoCAP IBA-seed assessment

Other seeds' experimental support queried live in QuickGO on 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000765163 | GO:0006865 amino acid transport | 2 | 8 (7 taxa) | GO:1903810, IMP, PMID:18833300 (PseudoCAP) | OVER-SPECIFIC | Partial growth defect on His in a Biolog/plate screen; no uptake assay, no induction by His; MetI-family permease. Supports amino acid transport (the node term), not His as substrate. | E. coli MetI P31547 (IMP D-Met transport PMID:12218041; EXP methionine transport and ABC-type D-Met transporter activity PMID:12169620) | Yes |

PSEUDOCAP defect: 1 SUSPECTED WRONG_TERM CHECK on GO:1903810. No GO_CENTRAL
defect. The node term itself is a sound generalization for the MetI clade.
PA5504 does not receive the GO:0006865 leaf IBA in GOA; it carries the more
specific GO:0048473 IBA from the child node PTN000765164 (MetI seed), accepted.
