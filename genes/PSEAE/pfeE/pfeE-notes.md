# pfeE (PA2689, Q9I0F2) notes

Periplasmic ferric-enterobactin esterase (esterase D family). No deep-research provider was
available; literature checked by hand (PMID:30086222 abstract only; UniProt curated text from
the same paper; QuickGO for the other node seeds and for E. coli Fes P13039). The pfeS review
covers the regulator of the pfe locus.

## Literature

- Perraud et al. 2018 (PMID:30086222, abstract): ["Purified PfeE hydrolyzed ferri-ENT into three
  molecules of 2,3-DHBS (2,3-dihydroxybenzoylserine) still complexed with ferric iron"]; iron
  release needs a reductant too; crystal structures with ferri-ENT define the site and catalytic
  triad; ["cell fractionation and fluorescence microscopy showed periplasmic localization of PfeE
  in P. aeruginosa cells"]. UniProt adds: monomer, induced by enterobactin, deletion strongly
  inhibits Fe uptake via enterobactin, also hydrolyses salmochelin S4, EC 3.1.1.108.
- Other PTN002868704 seeds: A. fumigatus SidJ Q4WF29 (AspGD IMP GO:0016788, PMID:17586718;
  fusarinine C esterase); A. nidulans EstB Q5AV79 (UniProt EXP GO:0008849, PMID:30070018).
- Comparators for a process term: E. coli Fes (P13039) carries GO:0033214 only as
  acts_upstream_of_or_within (IMP); SidJ likewise. So no NEW process term was added.
- GO:0008849 enterochelin esterase is defined on iron-free enterobactin; no GO term for ferric
  enterobactin esterase (EC 3.1.1.108); proposed as a new term.

## Review decisions

- GO:0016788 IDA and IBA: MODIFY to GO:0052689 carboxylic ester hydrolase activity (the lactone
  bonds of enterobactin are carboxylic esters); new term proposed for EC 3.1.1.108.
- GO:0042597 periplasmic space EXP and IEA: MODIFY to GO:0030288 (Gram-negative periplasm).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002868704 | GO:0016788 hydrolase activity, acting on ester bonds | 3 | 9 (8 taxa) | GO:0016788, IDA, PMID:30086222 (PseudoCAP) | SOUND | Abstract states purified PfeE hydrolyses ferric enterobactin. The term is correct but general for PfeE (row MODIFY to GO:0052689); the broad node term is appropriate for a clade of esterases on different siderophores. | A. fumigatus SidJ Q4WF29 (IMP); A. nidulans EstB Q5AV79 (EXP GO:0008849) | Yes, on the two Aspergillus seeds |

No PSEUDOCAP or GO_CENTRAL defect.
