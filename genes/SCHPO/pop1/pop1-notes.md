# pop1 (Ste16) — S. pombe — Review notes

UniProt: P87060 (POP1_SCHPO), 775 AA. PomBase SPBC1718.01. Synonym ste16. F-box (298-345) plus
C-terminal WD40 repeats (UniProt annotates five; the primary papers count seven or eight).
Paralogue: pop2/Sud1 (O14170). Budding yeast comparator: Cdc4 (P07834); human comparator: FBXW7
(sequence) / SKP2 (role as the CKI-degrading F-box adaptor).

Inputs used: pop1-uniprot.txt, pop1-goa.tsv, pop1-deep-research-falcon.md (Edison/Falcon synthesis of
the same primary papers plus Kawamukai 2024), and the cached publications. Only PMID:12167173 is
full-text in the cache; the other seven references are abstract-only, and this is recorded in each
`reference_review`.

## Core biology

Pop1 is one of two Cdc4/Fbw7-type F-box/WD40 substrate receptors of the fission yeast SCF. It has no
catalytic activity; it tethers itself to the Psh1 (Skp1) - Pcu1 (cullin-1) - Pip1 (Rbx1) core through
its F-box and captures phosphorylated substrates with its WD40 propeller. It forms homo-oligomers and
hetero-oligomers with Pop2 through an F-box-independent N-terminal region (Pop1 residues 228-402).
Endogenous Pop1, Pop2, Pcu1, Psh1 and Pip1 co-fractionate in a ~500 kDa SCF(Pop1/Pop2) complex that
polyubiquitylates phosphorylated Rum1 in vitro. The Pop1 F-box is essential; the Pop2 F-box is not.
Pop1-only complexes still have ubiquitin ligase activity. Pop1 is exclusively nuclear, unlike every other
subunit of the complex.

Substrates with direct evidence:
- Rum1 (CDK inhibitor): accumulates without ubiquitylated forms in pop1 mutants; half-life ~20 min ->
  >100 min in pop1 mutants; SCF(Pop1/Pop2) polyubiquitylates phospho-Rum1 in vitro.
- Cdc18 (replication initiator): accumulates in pop1 mutants independently of Rum1; Pop1 binds Cdc18 in
  vivo; Cdc18 binding to Pop2 requires Pop1.
- Cig2 (S-phase cyclin): Pop1 binds phosphorylated Cig2 through a 93-residue cyclin-box segment;
  Pop1/Pop2 are responsible for SCF-dependent Cig2 instability in G2 and M (the APC/C handles anaphase/G1).

Phenotypes: pop1 mutants are sterile and polyploid; the polyploidy needs rum1+; synthetic lethal with
cdc2-ts and cdc13-ts. As ste16, disruptants fail to arrest in G1 after nitrogen starvation, arrest in G2,
and diploidise on refeeding (fully suppressed by rum1 deletion).

## Key evidence (verbatim quotes)

- Founding paper, ploidy and substrates.
  [PMID:9203581 "By screening for sterile mutants that show increased ploidy, we have identified a new gene, pop1+, in mutants that become polyploid."]
  [PMID:9203581 "In a pop1 mutant Rum1 and Cdc18 proteins become accumulated to high levels."]
  [PMID:9203581 "The high ploidy phenotype in the pop1 mutant is dependent on the presence of the rum1+ gene, whereas the accumulation of Cdc18 is independent of Rum1."]
  [PMID:9203581 "In the pop1 mutant, however, no ubiquitinated forms of these proteins are detected."]
  [PMID:9203581 "Finally we show that Pop1 binds Cdc18 in vivo."]
  [PMID:9203581 "We propose that Pop1 functions as a recognition factor for Rum1 and Cdc18, which are subsequently ubiquitinated and targeted to the 26S proteasome for degradation."]

- ste16 = pop1; starvation G1 arrest.
  [PMID:9472077 "We isolated the sterile mutants which were defective in G1 arrest following nitrogen starvation."]
  [PMID:9472077 "The ste16 disruptant was viable, but arrested the cell cycle in the G2-phase after the nutritional down-shift."]
  [PMID:9472077 "This diploidization phenomenon was completely suppressed by the null mutation of rum1 encoding the inhibitor of Cdc2 kinase."]
  [PMID:9472077 "As the Rum1 protein level was remarkably elevated in the ste16Delta, the Ste16 protein negatively controls the Rum1 level."]

- Pop2 discovery, hetero-/homo-dimers, cullin-1.
  [PMID:9990507 "Pop1 and Pop2 form hetero-as well as homo-dimers in the cell."]
  [PMID:9990507 "By forming three distinct complexes, SCFPop1/Pop1, SCFPop1/Pop2 and SCFPop2/Pop2, SCF has evolved a sophisticated mechanism to control the level of Rum1 and Cdc18."]
  [PMID:9990507 "cullin-1 functions as a component of SCFPop1,2"]

- Pop1-Pop2 complexes and Cdc18.
  [PMID:10209119 "Pop1p and Pop2p formed heterooligomeric complexes when overexpressed, and binding of Cdc18p to Pop2p was dependent on Pop1p."]
  [PMID:10209119 "The Pop1p-Pop2p interaction was mediated by the amino-terminal domain of Pop2p which, when fused to full-length Pop1p, rescued the phenotype of a Deltapop1Deltapop2 double mutant."]

- Biochemistry of the complex (full text read).
  [PMID:12167173 "We have identified Psh1p and Pip1p, the fission yeast homologues of human SKP1 and HRT1/RBX1/ROC1, and show that both associate with Pop1p, Pop2p, and Pcu1p into a ~500 kDa SCFPop1p-Pop2p complex, which supports polyubiquitylation of Rum1p."]
  [PMID:12167173 "Only the F-box of Pop1p is required for SCFPop1p-Pop2p function, while Pop2p seems to be attracted into the complex through binding to Pop1p."]
  [PMID:12167173 "Rum1p half-life was increased from ~20 minutes in wild-type to greater than 100 minutes in pop1 or pop2 mutants"]
  [PMID:12167173 "F-box-deleted Pop1p was completely defective in rescuing the Rum1p proteolysis defect of pop1 mutants"]
  [PMID:12167173 "A further truncation mutant mapped the Pop2p binding domain to a region between residues 228 and 402 of Pop1p"]
  [PMID:12167173 "Thus Pop1p and Pop2p appear to assemble into distinct SCF complexes bearing ubiquitin ligase activity in vitro."]
  [PMID:12167173 "Since all SCFPop1p-Pop2p subunits, except for Pop1p, which is exclusively nuclear, localize to both the nucleus and the cytoplasm"]
  [PMID:12167173 "While Pip1p, Psh1p, Pcu1p, and Pop2p were present in both the cytoplasm and the nucleus, surprisingly, GFP-Pop1p was largely restricted to the nucleus"]

- Cig2.
  [PMID:14970237 "Cig2 instability during G(2) and M phase is dependent upon the SCF complex, whereas the APC/C is responsible for Cig2 destruction during anaphase and G(1)"]
  [PMID:14970237 "Two F-box/WD proteins Pop1 and Pop2, homologues of budding yeast Cdc4 and human Fbw7, are responsible for Cig2 instability."]
  [PMID:14970237 "Pop1 binds Cig2 in vivo."]
  [PMID:14970237 "Cig2 phosphorylation is also required for interaction with Pop1."]

- Skp1 co-IP survey (Pop1 one of 12 F-box proteins).
  [PMID:15147268 "In order to assess the binding properties of ts Skp1, 12 F-box proteins and Pcu1 were epitope-tagged, and co-immunoprecipitation performed."]

- ORFeome localisation (source of the HDA nucleus row).
  [PMID:16823372 "we determined the localization of 4,431 proteins, corresponding to approximately 90% of the fission yeast proteome, by tagging each ORF with the yellow fluorescent protein"]

## Curation decisions

- Nine GO:0005515 protein binding IPI rows (partners Pop2 x3, Cdc18 x3, Skp1/Psh1 x2, Cig2 x1): all
  MODIFY -> GO:1990756 ubiquitin-like ligase-substrate adaptor activity, following the CDC4 exemplar
  (Skp1 contact = the F-box tether; Cdc18/Cig2 = substrate recognition; Pop2 = the heterooligomeric
  receptor module). The three Pop2 rows also propose GO:0046982 protein heterodimerization activity.
  None removed: each is a focused mechanistic study, not a proteome-scale record.
- GO:0005634 nucleus (HDA, IEA): ACCEPT; concordant with the exclusive nuclear localisation shown by
  three methods in Seibert et al.
- GO:0005737 cytoplasm IBA (PANTHER:PTN008687761): REMOVE. Checked interpro/panther/PTHR19848/
  PTHR19848-paint.tsv: the cytoplasm IBD on this node (2025-10-29) is seeded by LIS1/PAFAH1B1
  orthologues (human P43034, S. cerevisiae PAC1 = SGD:S000005795, fly/worm/zebrafish/Dictyostelium
  entries), T. brucei Q57TT4 (G-protein beta-like) and mouse Fbxw11 (MGI:2144023). The node is a deep
  WD40-family grouping; Pop1 has direct evidence of being excluded from the cytoplasm. Argument is with
  node placement plus target-specific divergence, not donor count.
- GO:0031145 anaphase-promoting complex-dependent catabolic process IMP (PMID:14970237): MODIFY ->
  GO:0031146. The paper's own abstract assigns Pop1/Pop2 to the SCF branch of Cig2 degradation (G2/M)
  and the APC/C to anaphase/G1. Pop1 is not part of the APC/C and does no work in APC/C-dependent
  ubiquitylation. Abstract-only cache, so the possibility that the full text shows an APC/C-branch
  defect is raised in suggested_questions rather than asserted.
- GO:0031146 ISO and GO:0043224 ISO (from Cdc4): ACCEPT; both directly supported in S. pombe.
- GO:1900087 positive regulation of G1/S transition IMP (PMID:9472077): ACCEPT. Cdc4/SKP2 and the
  g1_s_transition module use GO:0000082 instead; raised as a convention question.
- GO:1990756 IEA (ARBA) and IPI (Cig2): ACCEPT; this is the core MF.
- No NEW rows. pop2 carries GO:1903467 negative regulation of mitotic DNA replication initiation for
  Cdc18; for pop1 the polyploidy epistasis is rum1-dependent, so the term is not asserted for pop1 and
  the asymmetry is left as a suggested question.

## Loose ends

- UniProt DR lines list PomBase IMP annotations to GO:0006511 (ubiquitin-dependent protein catabolic
  process) and GO:0000747 (conjugation with cellular fusion) that are absent from the QuickGO export
  used to seed this review; they were not reviewed here.
- PANTHER: UniProt cross-references place pop1 in PTHR19848:SF8 (FBXW7), whereas the local PANTHER 19.0
  classification used by modules/g1_s_transition.yaml places it in PTHR44129 (WD REPEAT-CONTAINING
  PROTEIN POP1). The cytoplasm IBA node PTN008687761 is in the PTHR19848 tree.
- No structure of Pop1 or of a Pop1-substrate complex; phosphodegron recognition is inferred from
  Rum1 Ser58/Thr62 and Cig2 phosphorylation dependence.
