# pchB (Q51507, PA4230) notes

## Review session 2026-10-28 (PseudoCAP IBA-seed protocol, worklist rank 66)

No deep-research provider was available; these notes are my own reading of the Swiss-Prot record and the
cached papers. Only PMID:21751784 has full text in the cache; PMID:7500944, 11937513, 16248620 and
19432488 are abstract-only.

## Identity

- *P. aeruginosa* PAO1 PA4230, Swiss-Prot Q51507, 101 aa, AroQ-class chorismate-mutase fold
  (Pfam PF01817 CM_2; InterPro IPR008241 Isochorismate_pyruvate-lyase; PIRSF029775; PANTHER PTHR38041:SF1).
- Intertwined three-helix homodimer; structures 2H9C/2H9D/3HGW/3HGX/3REM/3RET.
- First gene of the iron-repressed *pchBA* operon (salicylate), upstream of the pyochelin NRPS genes.

## Literature

- Genetics: *pchBA* are necessary for salicylate formation [PMID:7500944 "two adjacent genes, designated
  pchB and pchA, which are necessary for salicylate formation"]. pchB alone converts isochorismate to
  salicylate in an *E. coli entB* background [PMID:7500944 "an entB mutant of E. coli blocked in the
  conversion of isochorismate to 2,3-dihydro-2,3-dihydroxybenzoate formed salicylate when transformed with a
  pchB expression construct"]. Crude-extract reconstitution [PMID:7500944 "Salicylate formation could also be
  demonstrated in vitro when chorismate was incubated with a crude extract of P. aeruginosa containing
  overproduced PchA and PchB proteins"]. Pathway conclusion [PMID:7500944 "Our results are consistent with a
  pathway leading from chorismate to isochorismate and then to salicylate plus pyruvate, catalyzed
  consecutively by the iron-repressible PchA and PchB proteins in P. aeruginosa."]. Salicylate is a pyochelin
  precursor [PMID:7500944 "Salicylate is a precursor of pyochelin in Pseudomonas aeruginosa"].
- Purified enzyme: IPL, no cofactors [PMID:11937513 "In the reaction catalyzed by this enzyme, isochorismate
  --> salicylate + pyruvate, no cofactors appear to be required."]; "second enzyme of pyochelin
  biosynthesis" [PMID:11937513 "Isochorismate pyruvate-lyase (IPL), the second enzyme of pyochelin
  biosynthesis and the product of the pchB gene, was purified to homogeneity from Pseudomonas aeruginosa."].
  Secondary CM activity [PMID:11937513 "Chorismate was shown to be converted to prephenate by purified PchB in
  vitro"] and complementation of an *E. coli* CM-deficient mutant [PMID:11937513 "a CM-deficient Escherichia
  coli mutant, which is auxotrophic for phenylalanine and tyrosine, was functionally complemented by the
  cloned P. aeruginosa pchB gene"].
- Mechanism: pericyclic hydrogen transfer [PMID:16248620 "the label is quantitatively transferred from C2 to
  C9"]; the two activities are not covariant [PMID:19432488 "the mutational effects on k(cat) provide evidence
  that the two activities of PchB are not covariant"].
- The CM activity is non-physiological [PMID:21751784 "has non-physiological chorismate mutase activity,
  albeit with considerably lower catalytic efficiency than for the lyase activity"]; the physiological role
  is salicylate for pyochelin [PMID:21751784 "The physiological function of the isochorismate-pyruvate lyase
  (PchB) from Pseudomonas aeruginosa is to convert isochorismate to salicylate and pyruvate"].

## Annotation decisions

- GO:0043904 isochorismate pyruvate lyase activity (EXP x4, IEA): ACCEPT, core MF.
- GO:0016835 carbon-oxygen lyase activity (IDA x2, IEA): MODIFY to GO:0043904 (its is_a descendant,
  already carried).
- GO:0004106 chorismate mutase activity (EXP, IDA x2, IBA, IEA): KEEP_AS_NON_CORE; real in vitro and in
  heterologous complementation, but adventitious (kcat/Km much lower than for IPL).
- GO:0046417 chorismate metabolic process (IBA, IEA): KEEP_AS_NON_CORE; follows from the adventitious CM
  activity; the physiological substrate is isochorismate.
- GO:0009697 salicylic acid biosynthetic process (IDA PseudoCAP, IBA, IEA): ACCEPT, core BP. PchB catalyses
  the final step (isochorismate -> salicylate + pyruvate).
- GO:0042864 pyochelin biosynthetic process (IDA, UniProt): ACCEPT; salicylate is incorporated into
  pyochelin and PchB is the second enzyme of the pathway. In GO the two process terms are not linked
  (GO:0009697 is not part_of GO:0042864), so both are kept.

## The node PTN002211012

QuickGO (2026-10-28) lists 17 leaves with the GO:0009697 IBA from PTN002211012, and the same 17 with the
GO:0004106 chorismate mutase IBA from the same node. They are the AroQ-class chorismate-mutase family as a
whole: *Methanocaldococcus jannaschii* AroQ (Q57696, the classic MjCM), *Halobacterium* VNG_1244C (Q9HQB1),
*Methanosarcina* MA_1377 (Q8TR07), *M. tuberculosis* Rv1885c (P9WIB9, secreted CM) and Rv0948c (P9WIC1,
intracellular CM), *P. aeruginosa* AroQ (Q9HU05), *Yersinia* PheA2 (Q7CHH5), *Xanthomonas* PheA (Q8PCZ3),
*Salmonella* STM1269, *Coxiella*, *Geobacter*, *Streptococcus pneumoniae*, *Streptomyces* SCO2019, and the
secreted CM effectors of the fungi *Sclerotinia sclerotiorum* (A7F9N9) and *Puccinia graminis* (E3LB91).
PchB is the only member with IPL activity. The chorismate mutase IBD at this node is well seeded (Mtb,
MjCM, PA AroQ, Yersinia); the salicylate IBD rests on PchB alone and transfers a pathway that the
comparators do not perform (mycobacteria and *Yersinia* make salicylate with a salicylate synthase,
MbtI/Irp9, not via CM-fold proteins). The node term is right for PchB and wrong for the clade.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002211012 | GO:0009697 salicylic acid biosynthetic process | 1 (sole) | 17 (15 taxa) | GO:0009697, IDA, PMID:7500944 (PseudoCAP) | OVER-SPECIFIC | The seed is sound for PchB: pchB alone converts isochorismate to salicylate in an *E. coli entB* strain, and the purified enzyme is an IPL (PMID:11937513). But the IBD sits at the root of the AroQ chorismate-mutase family, whose other 16 leaves (archaeal, mycobacterial, enterobacterial, fungal CMs) are chorismate mutases with no IPL activity. Withdraw the IBD or move it to a node confined to PchB-type IPLs. |
