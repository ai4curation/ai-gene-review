# PA4921 / ChoE (Q9HUP2) review notes

## Literature

Search (Europe PMC REST, 2026-11-05: `TITLE:"acetylcholinesterase" AND TITLE:aeruginosa`)
returned PMID:22192836 and PMID:36753877; the PubMed search API was failing that day.

1. Sanchez et al. 2012 [PMID:22192836], abstract only. PA4921 is the gene for the
   cholinesterase (ChoE) activity of PAO1, an SGNH-hydrolase with a signal peptide
   [PMID:22192836 "this work demonstrates that the PA4921 gene of the Pseudomonas
   aeruginosa PAO1 genome is a gene responsible for cholinesterase (ChoE) activity"].
   Acetylthiocholine and propionylthiocholine are substrates; butyrylcholine inhibits;
   the purified recombinant enzyme behaves like mammalian AChE kinetically. The authors
   propose an acetylcholinesterase or propionylcholinesterase.
2. Inoue et al. 2023 [PMID:36753877], abstract only. Recombinant PAO1 AChE also catalyses
   acetyl transfer to amines and alcohols (aminolysis/alcoholysis) using acetylcholine or
   ethyl acetate as donor; a side activity of the acyl-enzyme.
3. UniProt Q9HUP2 (unreviewed): SignalP 1-18; Pfam Lipase_GDSL; PANTHER PTHR45648; 13 PDB
   structures (6UQV-6UR1, 8D8W-8D91), mature chain 21-307.

The ChoE substrate choice (AChE vs propionylcholinesterase) is unresolved, so
GO:0004104 cholinesterase activity, the term the curator used, is the right level;
GO:0003990 acetylcholinesterase activity would overstate it.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN005219546 | GO:0052689 carboxylic ester hydrolase activity | 2 | 960 (51 taxa) | GO:0004104 cholinesterase activity, IDA, PMID:22192836 (PseudoCAP) | SOUND | Purified recombinant enzyme hydrolyses acetyl- and propionylthiocholine and p-nitrophenyl esters (abstract). Cholinesterase is_a carboxylic ester hydrolase, so the seed supports the node term. | EstA (O33407, PA5112): IMP PseudoCAP and IDA UniProt carboxylesterase (PMID:20931591) | Yes; EstA's purified-enzyme esterase evidence alone supports it, and ester hydrolysis is the conserved GDSL/SGNH chemistry. Consistent with the estA review (SOUND). No GO_CENTRAL defect. |

PTN005219546 also carries a GO:0008610 lipid biosynthetic process IBD seeded only by EstA
(not by PA4921). The node-level GO_CENTRAL defect for it is recorded once in
`genes/PSEAE/estA/estA-ai-review.yaml`; not repeated here. On PA4921 the propagated row
is removed: a periplasmic/secreted cholinesterase has no role in lipid biosynthesis.

## Annotation decisions

- GO:0004104 IDA: ACCEPT; core.
- GO:0052689 IBA: TOO_GENERAL (GO:0004104, accepted, is_a GO:0052689).
- GO:0016788 IEA: TOO_GENERAL (same reason).
- GO:0008610 IBA: REMOVE (propagated from EstA's indirect rhamnolipid phenotype).
