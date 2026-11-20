# vanY (Enterococcus faecium, P37711) — curation notes

## Literature search record

No deep-research provider key exists here and there is no model organism
database description for Enterococcus. `just fetch-fitness ENTFC vanY` was not
attempted; no fitness data set exists for this organism.

Sources checked:

- `genes/ENTFC/vanY/vanY-uniprot.txt` (Swiss-Prot P37711): FUNCTION, COFACTOR,
  ACTIVITY REGULATION, SUBCELLULAR LOCATION, INDUCTION, the peptidase M15B
  family note, the single transmembrane helix at residues 7-23, the ACT_SITE at
  213 and the three zinc-binding residues (163, 170, 216).
- The GOA-cited publication PMID:1510448 (abstract-only in the cache).
- Fetched for context: PMID:8852545 (review of the mechanism), PMID:1556077
  (operon control), PMID:7873524 (VanX, the enzyme VanY works in series with).
- Context read but not edited: a glycopeptide-resistance pathway module and a
  review of the vanA-operon GO-CAM, both proposed in
  ai4curation/ai-gene-review#5904 and not part of this branch; nothing in this
  review rests on them.
- GO relations checked against the local GO build, 2026-11-04: `GO:0008233
  peptidase activity` and `GO:0008237 metallopeptidase activity` are both `is_a`
  ancestors of `GO:0009046 zinc D-Ala-D-Ala carboxypeptidase activity`;
  `GO:0006508 proteolysis` is defined over the hydrolysis of proteins and is not
  an ancestor of `GO:0000270 peptidoglycan metabolic process`.

## What VanY does

VanY is the accessory, dispensable member of the cluster: a membrane-anchored
D,D-carboxypeptidase that finishes what VanX starts, by trimming precursors that
were already assembled with D-Ala-D-Ala.

[PMID:1510448 "VanY was associated with the cell membranes and cleaved the C-terminal D-alanine residue of UDP-muramyl-pentapeptide but did not display transpeptidase or beta-lactamase activities."]
[PMID:1510448 "VanY released the C-terminal D-hydroxy acid from depsipeptides produced by the vancomycin resistance protein VanA."]
[PMID:1510448 "These results demonstrate that VanY should contribute in vivo to the hydrolysis of both the D-alanyl-D-alanine- and the depsipeptide-containing peptidoglycan precursors."]

So its specificity is the mirror image of VanX's: VanX spares the depsipeptide,
while VanY cleaves both the dipeptide- and the depsipeptide-terminated
precursor. That is also why VanY is not required for resistance and only raises
its level a little:
[PMID:8852545 "VanX is required for resistance whereas VanY only slightly increases the level of resistance mediated by VanH, VanA and VanX."]
[PMID:8852545 "These two proteins act in series to eliminate D-Ala-D-Ala-containing precursors."]
UniProt states the dispensability directly, from two papers.

It is a zinc, not a serine, carboxypeptidase. The functional evidence for that is
the inhibitor profile:
[PMID:1510448 "The DD-carboxypeptidase activity was not inhibited by beta-lactam antibiotics."]
which is what distinguishes the metallo D,D-carboxypeptidases from the
penicillin-binding serine enzymes; UniProt adds a zinc cofactor and three
zinc-coordinating residues, and places the protein in the peptidase M15B family.

## Annotation issues

Only four rows, two of them location.

- `GO:0005886 plasma membrane` is directly observed and is where the enzyme acts,
  on membrane-associated precursors; UniProt adds a single-pass transmembrane
  helix. Both the EXP and the mapped row are accepted.
- `GO:0008233 peptidase activity` is the InterPro signature's generic term and is
  far less specific than the evidence supports. `GO:0009046 zinc D-Ala-D-Ala
  carboxypeptidase activity` is an `is_a` descendant and states the measured
  reaction, the metal class and the substrate, so the row is refined to it. This
  is also the typing used in the module.
- `GO:0006508 proteolysis` has the same problem here as on vanX, but the
  replacement differs because the substrate differs: VanY does not act on a free
  peptide but on UDP-MurNAc-pentapeptide and on the corresponding depsipeptide,
  i.e. on peptidoglycan precursors. `GO:0000270 peptidoglycan metabolic process`
  is the term that fits, and UniProt's keywords for this entry already include
  peptidoglycan synthesis and cell wall biogenesis/degradation.

Nothing in GOA connects vanY to antibiotic resistance, so `GO:0046677 response to
antibiotic` is proposed as a `NEW` row. The reason given is deliberately weaker
than for the other van genes, because VanY is dispensable; what justifies it is
that VanY is vancomycin-inducible, is part of the resistance cluster, and does
perform a step that raises the resistance level rather than merely accompanying
it.
