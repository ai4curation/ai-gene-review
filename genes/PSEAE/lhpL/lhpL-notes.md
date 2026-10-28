# lhpL (PA1255, Q9I489) notes

## 2026-10-28 review (PseudoCAP IBA-seed worklist, rank 86)

No deep-research provider keys were available; literature gathered by PubMed
search and from the cached publications. Sister genes in the same hydroxyproline
cluster are not yet reviewed.

### Identity

- UniProt Q9I489 (Swiss-Prot, PE 1), 344 aa, RecName "Bifunctional
  trans-3-hydroxy-L-proline dehydratase/2-epimerase", gene `lhpL` /
  OrderedLocusNames PA1255 [file:PSEAE/lhpL/lhpL-uniprot.txt].
- Proline racemase family (Pfam PF05544 Pro_racemase, PIRSF029792,
  SFLDS00028 Proline_Racemase, NCBIfam NF047722 T3LHypDht, PANTHER
  PTHR33442:SF5). Catalytic Cys-Cys pair architecture of that family; UniProt
  places the proton acceptor at residue 90 by similarity to B9K4G4
  [file:PSEAE/lhpL/lhpL-uniprot.txt].
- Two distinct enzymes must be kept apart in PAO1:
  - **PA1268 (Q9I476)** is the genuine *4-hydroxyproline 2-epimerase*
    (4HypE/PaHyPRE, EC 5.1.1.8).
  - **PA1255 (Q9I489, this gene)** acts on the *3*-hydroxy isomer.
  PseudoCAP annotated GO:0047580 (4-hydroxyproline epimerase activity) to both
  from PMID:27145750 (QuickGO, reference PMID:27145750).

### Activity

- Watanabe et al. 2016 assign the 3-hydroxy activity to this gene
  [PMID:27929065 "We herein demonstrated that PaLhpL gene (PA1255; Fig. 1d) in
  the L-hydroxyproline gene cluster encodes a bifunctional dehydratase and
  2-epimerase toward trans-3-hydroxy-L-proline as the leading candidate"]. That
  paper's own subject is the aconitase-X-family dehydratase PaLhpI, which acts
  on *cis*-3-hydroxy-L-proline; PaLhpL is the companion enzyme for the *trans*
  isomer.
- UniProt records both reactions with experimental evidence
  (`ECO:0000269|PubMed:27929065`): dehydration of trans-3-hydroxy-L-proline to
  Delta(1)-pyrroline-2-carboxylate (EC 4.2.1.77, KM 23 mM, kcat 28.7 min-1) and
  2-epimerization of trans-3-hydroxy-L-proline to cis-3-hydroxy-D-proline
  (EC 5.1.1.-) [file:PSEAE/lhpL/lhpL-uniprot.txt].
- The substrates it does **not** accept are also curated experimentally:
  "No dehydratase activity with L-proline, trans-4-hydroxy-L-" proline,
  "cis-4-hydroxy-L-proline (c4LHyp), D-proline" and so on, and, decisively for
  the seed under review, "Displays neither t4LHyp epimerase nor proline
  racemase activity (PubMed:17849014)"
  [file:PSEAE/lhpL/lhpL-uniprot.txt]. Goytia et al. assayed *P. aeruginosa*
  proline-racemase-family proteins directly and found that the ones with
  substituted catalytic couples gave neither activity
  [PMID:17849014 "aeruginosa sequences that present ‘Cys-Thr’ or ‘Ser-Cys’
  couple replacements respectively did not show neither PRAC nor HyPRE
  enzymatic activities"], while the genuine hydroxyproline epimerase they
  characterised (PaHyPRE) came from a different gene
  [PMID:17849014 "B. pseudomallei and P. aeruginosa recombinant proteins
  presented no measurable PRAC activity but demonstrated strong epimerization
  of OH-L/D-Pro behaving as genuine OH-Pro epimerases"].
- Zhao et al. 2014 is the genome-neighbourhood study that predicted t3HypD
  activities in this family; Q9I489 is among the sequences it treats
  [PMID:24980702 "The reactions catalyzed by proline racemase (ProR),
  4R-hydroxyproline 2-epimerase (4HypE), and trans-3-hydroxy-L-proline
  dehydratase (t3HypD) and the metabolic pathways in which they participate."],
  and it is the source of the UniProt INDUCTION statement that lhpL is
  up-regulated on trans-4- or trans-3-hydroxy-L-proline as sole carbon source.

### What PMID:27145750 (the seed reference) shows

- Li & Lu characterised the AraC-family regulator LhpR and the two hydroxyproline
  loci. In their nomenclature the gene at PA1255 is *lhpK*
  [PMID:27145750 "the second locus codes for a putative ABC transporter
  (LhpPMNO), a protein of unknown function (LhpH), Hyp/Pro racemase (LhpK) and
  two enzymes in l-Hyp catabolism (LhpC and LhpG)"]; `Hyp/Pro racemase` is a
  sequence-based name, not an assay.
- The genetic result that PseudoCAP used is an *induction* phenotype of a double
  mutant [PMID:27145750 "Induction of the lhpA promoter by d-Hyp was completely
  abolished in the lhpA lhpK double mutant devoid of two epimerases, while the
  induction effect of l-Hyp remained unchanged"]. That shows the two genes
  together are needed for D-Hyp-dependent promoter induction; it does not show
  which reaction either protein catalyses, and it cannot distinguish the 4- from
  the 3-hydroxy isomer.
- So the seed annotation is a phenotype-to-molecular-function step onto a term
  (GO:0047580: trans-4-hydroxy-L-proline = cis-4-hydroxy-D-proline) whose
  reaction has been directly tested on this protein and found absent.

### PAINT node (lhpL-bioinformatics/RESULTS.md)

PTN002433936 is an internal DUPLICATION node of PTHR33442 (family root
PTN002530875, 48 leaves): 9 leaves in 7 organisms, sole-seeded by
UniProtKB:Q9I489 (PAINT snapshot 20180110). Leaves are proline-racemase-family
proteins of *Korarchaeum*, *Chloroflexus*, three *Bacillus cereus* paralogues,
*Streptomyces coelicolor*, *Clostridium botulinum* PrdF and *Nematostella*,
plus lhpL; one of the *B. cereus* leaves is itself named
"Trans-3-hydroxy-L-proline dehydratase". GOA currently holds 35 GO:0047580 rows
with this node in with/from (9 GO_Central reference leaves, 24 TreeGrafter,
2 UniProt), so the term the node carries is propagated well beyond the
reference proteome.

### Annotation decisions

- GO:0047580 (IBA, IEA/ARBA, IMP): all three MODIFY to GO:0050346. The protein
  does have a hydroxyproline-acting epimerase/dehydratase activity, but on the
  3-hydroxy isomer; the 4-hydroxy reaction is experimentally excluded. The
  ARBA row's rule was almost certainly learnt from the same mis-assignment.
- GO:0050346 (EXP, IEA from RHEA/EC): ACCEPT, core.
- PSEUDOCAP `WRONG_TERM` defect on the IMP row, GO_CENTRAL `WRONG_TERM` defect
  on PTN002433936.
- The 2-epimerase half of the activity (trans-3-hydroxy-L-proline =
  cis-3-hydroxy-D-proline) has no GO term; recorded in `proposed_new_terms`.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002433936 | GO:0047580 4-hydroxyproline epimerase activity | 1 (sole) | 9 GO_Central (35 GOA rows incl. TreeGrafter) | GO:0047580, IMP, PMID:27145750 | WRONG | The seed is an induction phenotype of an *lhpA lhpK* double mutant, and the term's reaction (trans-4-hydroxy-L-proline = cis-4-hydroxy-D-proline) has been assayed on this protein and is absent (UniProt `CC:FUNCTION`, ECO:0000269 PubMed:17849014). The protein is a trans-**3**-hydroxy-L-proline dehydratase/2-epimerase (PMID:27929065), and PAO1's real 4-hydroxyproline 2-epimerase is a different gene (PA1268, Q9I476), which carries its own GO:0047580 IMP from the same paper. The node itself is a reasonable clade (proline-racemase family, one leaf already named a t3LHyp dehydratase) but it should carry GO:0050346 trans-L-3-hydroxyproline dehydratase activity, not GO:0047580. |
