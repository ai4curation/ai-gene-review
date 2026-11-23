# aroB (P07639, Escherichia coli K-12) review notes

## Provenance of this notes file

Provider deep research was unavailable for this review (no deep-research provider key in
the session), so no `aroB-deep-research-*.md` file exists. These notes were compiled by the
reviewer from the cached publications in `publications/`, the UniProt record
(`aroB-uniprot.txt`) and the PTHR43622 family review
(`interpro/panther/PTHR43622/PTHR43622-review.yaml`, for which AroB is the reference
protein).

Family: PANTHER PTHR43622 (3-DEHYDROQUINATE SYNTHASE), subfamily PTHR43622:SF7, the
canonical DHQS clade under PAINT node PTN000472619; InterPro IPR016037/IPR030963, Pfam
PF01761 and PF24621, NCBIfam TIGR01357, HAMAP MF_00110. No PAINT IRD/IKR loss on the AroB
lineage (`just paint-losses ECOLI aroB`).

## Function

- 3-Dehydroquinate synthase (DHQS, EC 4.2.3.4), step 2 of the shikimate pathway:
  DAHP = 3-dehydroquinate + phosphate (RHEA:21968).
  [UniProt P07639 CC FUNCTION "Catalyzes the conversion of 3-deoxy-D-arabino-heptulosonate 7-phosphate (DAHP) to dehydroquinate (DHQ)."]
- Gene-enzyme link and purification: [PMID:6386050 "Dehydroquinate synthase has been purified 9000-fold from Escherichia coli K-12 (strain MM294)."]
  [PMID:6386050 "The synthase is encoded by the aroB gene"]
  Overexpression from the cloned gene raised activity: [PMID:6386050 "Subcloning of the aroB gene behind a tac promoter results in E. coli transformants that produce 1000 times more enzyme than MM294"]
- Mechanism: an oxidation at C-5 by tightly bound NAD+, then phosphate elimination,
  reduction, ring opening and intramolecular aldol cyclisation.
  [PMID:353051 "The presence of 3H in the formate corresponding to 15% of the enzyme was interpreted as indicating a 5-dehydro derivative of the substrate as an intermediate of the reaction."]
- Cofactors: [PMID:2514789 "The homogeneous enzyme, purified from the overproducing strain RB791 (pJB14), is a monomeric metalloenzyme of Mr = 39,000 that contains 1 mol of tightly bound Co(II) according to atomic absorption analysis."]
  [PMID:2514789 "Reconstitution of the apoenzyme with Zn(II) (which is probably the functioning metal in vivo) restores activity to 53% of the level observed with the Co(II)-holoenzyme."]
  [PMID:2514789 "Dehydroquinate synthase also binds 1 mol of NAD+, the presence of which is essential for catalytic activity."]
  Km for NAD+ 80 nM; Km for DAHP 0.6-5.5 uM (UniProt, from PMID:2514789).
- Quaternary structure: monomer (PMID:6386050, PMID:2514789). Maitra and Sprinson's
  earlier Mr of about 57,000 (PMID:353051) is out of line with the 362-residue sequence
  (about 39 kDa).

## Localization

- Soluble cytoplasmic (cytosolic) enzyme: [PMID:6386050 "the synthase constitutes 5% of the soluble protein of the cell."]
  No signal peptide or transmembrane segment in the UniProt record.

## Interactions

- A yeast two-hybrid screen (PMID:24561554) reported AroB with FixX (P68646, a
  ferredoxin-like protein; UniProt INTERACTION NbExp=2). No functional consequence is known;
  the interaction is not named in the cached text.

## Pathway context

- Chorismate biosynthesis step 2/7 (UniProt PATHWAY, HAMAP MF_00110). Chorismate is the
  precursor of phenylalanine, tyrosine and tryptophan, and of folate, ubiquinone,
  menaquinone and enterobactin, so DHQS is upstream of all of them.
