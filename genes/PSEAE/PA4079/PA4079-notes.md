# PA4079 (Q9HWU9) notes

## Review session 2026-10-28 (PseudoCAP IBA-seed protocol, worklist rank 38)

No deep-research provider was available. A PubMed search for "PA4079 Pseudomonas aeruginosa" returns a
single paper (PMID:28524228), which is abstract-only in the cache and has no PMC copy.

## Identity

- *P. aeruginosa* PAO1 locus PA4079, UniProt Q9HWU9 (unreviewed, PE 1), 229 aa; submitted name "Probable
  dehydrogenase" (ECO:0000313, not evidence).
- Classical short-chain dehydrogenase/reductase (SDR): Pfam PF00106 (adh_short), InterPro IPR002347
  (SDR_fam), IPR036291 (NAD(P)-binding domain), Gene3D 3.40.50.720 Rossmann fold; PANTHER PTHR45458:SF1.
- Four crystal structures (PDB 5WQM, 5WQN apo; 5WQO, 5WQP with NADP). UniProt BINDING features for NADP(+)
  at 13 residues are structure-derived (ECO:0007829|PDB:5WQO, PDB:5WQP).

## Literature

- Li et al. 2017 solved the structure and assayed activity [PMID:28524228 "we determined its crystal
  structure and confirmed it to be a NAD(P)-dependent short-chain dehydrogenase/reductase"]; the activity
  spectrum indicates a carbonyl reductase [PMID:28524228 "Structural similarity and activity for a broad
  range of substrates indicate that PA4079 functions as a carbonyl reductase."]. NADP binding orders the
  substrate-specificity loop [PMID:28524228 "NADP stabilizes the active site specificity loop"]. Expression
  stays high under antibiotic exposure [PMID:28524228 "pa4079 maintains high expression levels during
  antibiotic exposure"], and the authors only speculate about drug reduction [PMID:28524228 "its possible
  reduction of antimicrobial drugs"].
- The physiological substrate is unknown; no mutant phenotype has been reported. I therefore propose no
  biological process term.

## Annotation decisions

- GO:0004090 carbonyl reductase (NADPH) activity (IDA PseudoCAP): ACCEPT. Activity on a broad range of
  carbonyl substrates was measured with the purified protein; the NADP-bound structures support the NADPH
  cofactor. GO:0004090 is_a GO:0008106 alcohol dehydrogenase (NADP+) activity is_a GO:0016616 (OLS).
- GO:0016616 oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor (IBA):
  MODIFY to GO:0004090 for this gene; the node term itself is a sound, cautious choice.
- NEW GO:0050661 NADP binding (IDA PMID:28524228), from the NADP-bound crystal structures.

## PseudoCAP IBA-seed assessment

QuickGO (2026-10-28, withFrom=PANTHER:PTN002388087) returns 369 GO:0016616 IBA rows (the worklist, from an
older PAINT release, has 27 leaves in 14 taxa). Leaves span diverse bacteria (several
annotated "csgA", the Myxococcus C-signal SDR homolog), fungi, green algae (Chlamydomonas), diatoms,
oomycetes and a few arthropods (from the first 200 rows inspected); PA4079 is the only seed.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002388087 | GO:0016616 oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor | 1 (sole) | 27 (14 taxa) in worklist; 369 in QuickGO | GO:0004090 carbonyl reductase (NADPH) activity, IDA, PMID:28524228 (PseudoCAP) | SOUND | Purified-enzyme activity on a broad range of carbonyl substrates plus NADP-bound structures: direct biochemistry, not a phenotype. Propagating the generic NAD(P)-dependent CH-OH oxidoreductase parent rather than "carbonyl reductase" is an appropriately cautious choice for a large cross-kingdom SDR clade with one characterised member; it is true of essentially every classical SDR with the conserved catalytic tetrad and Rossmann NAD(P) site. |
