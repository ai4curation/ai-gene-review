# pop2 (Sud1) — S. pombe — Review notes

UniProt: O14170 (POP2_SCHPO), 703 AA. PomBase SPAC4D7.03. Synonym sud1 ("proteolysis factor sud1").
F-box domain (UniProt 236-283) plus C-terminal WD40 repeats (UniProt lists six repeats spanning 389-654;
the primary papers describe a seven-bladed propeller). Paralogue: pop1/Ste16 (P87060). Budding yeast
comparator: Cdc4 (P07834); human comparators: FBXW7 (sequence) and SKP2 (role as the CKI-degrading
F-box adaptor). Do not confuse with the CCR4-NOT deadenylase Pop2/Caf1 of S. cerevisiae (S. pombe
caf1), which shares only the name.

Inputs used: pop2-uniprot.txt, pop2-goa.tsv, pop2-deep-research-falcon.md (Edison/Falcon synthesis of the
same primary papers plus Uchiyama 2015 on Rev1, which is not in the publication cache and was not used),
and the cached publications. Full text is cached for PMID:9653157, PMID:12167173 and PMID:17016471;
PMID:9990507, PMID:10209119, PMID:14970237 and PMID:15147268 are abstract-only, which is recorded in
each `reference_review`.

## Core biology

Pop2 is the second Cdc4/Fbw7-type F-box/WD40 substrate receptor of the fission yeast SCF ubiquitin
ligase. It has no catalytic activity of its own. Its N-terminal region (residues 1-241) mediates
heterooligomerisation with Pop1 and homooligomerisation, its F-box binds Psh1 (Skp1), and its WD40
propeller is the presumed phosphodegron-reading surface. At endogenous levels Pop2 co-purifies with
Pop1, Pcu1 (cullin-1), Psh1 and Pip1 (Rbx1) in a ~500 kDa SCF(Pop1-Pop2) complex, and it also forms a
Pop1-independent SCF(Pop2) complex that carries ubiquitin ligase activity in vitro. The two paralogues are
not interchangeable: they fail to cross-complement, Cdc18 binding to Pop2 needs Pop1, Pop2 alone does not
bind Rum1, and within the heteromer the Pop1 F-box is essential while the Pop2 F-box is dispensable, so
Pop2 is thought to be tethered to the SCF core largely through Pop1.

Substrates with direct evidence:
- Cdc18 (replication initiator, Cdc6 orthologue): sud1/pop2 deletion hyperaccumulates Cdc18; Sud1 binds
  Cdc18 in vivo only after CDK phosphorylation at consensus sites; Cdc18 binding to Pop2 requires Pop1.
- Rum1 (CDK inhibitor): accumulates in pop2 mutants (half-life ~20 min -> >100 min); the immunopurified
  Pop1-Pop2 complex binds CDK-phosphorylated Rum1 and polyubiquitylates it with E1, UBC3, ATP and
  ubiquitin; Pip1 complexes from pop2-deleted lysate have no Rum1 ubiquitylation activity.
- Cig2 (S-phase cyclin): Pop1 and Pop2 are responsible for SCF-dependent Cig2 instability in G2 and M
  (the abstract reports Pop1 binding Cig2; the PomBase IPI for Pop2 rests on the full text).

Phenotypes: pop2/sud1 deletants are viable but undergo spontaneous re-replication and diploidise;
hyperaccumulated Rum1 contributes to the re-replication but does not explain the Cdc18 proteolysis defect.
The phenotype is milder than that of pop1 deletion. Pop2 lacks the N-terminal NLS of Pop1 and is found
in both the nucleus and the cytoplasm; the complete SCF(Pop1-Pop2) complex is nuclear, where the
substrates are, and the cytoplasmic pool has been proposed to act on unidentified substrates.

## Key evidence (verbatim quotes)

- Founding sud1 paper: CDC4 homology, phospho-Cdc18 binding, re-replication (full text cached).
  [PMID:9653157 "The sud1 + gene was identified in a tblastn search with the Saccharomyces cerevisiae CDC4 protein sequence"]
  [PMID:9653157 "sud1 + shares homology with the budding yeast CDC4 gene and is required to prevent spontaneous re-replication in fission yeast."]
  [PMID:9653157 "Cells lacking sud1(+) accumulate high levels of Cdc18 and the CDK inhibitor Rum1, because they cannot degrade these two key cell cycle regulators"]
  [PMID:9653157 "Sud1-Cdc18 binding requires prior phosphorylation of the Cdc18 polypeptide at CDK consensus sites"]
  [PMID:9653157 "Sud1 interacts with ubiquitinated proteins in fission yeast and binds the Cdc18 polypeptide in a phosphorylation-dependent manner"]
  [PMID:9653157 "hyperaccumulation of Rum1 contributes to re-replication in Deltasud1 cells, but is not the cause of the defect in Cdc18 proteolysis"]
  [PMID:9653157 "Cdc18 is degraded by the ubiquitin-proteasome pathway and have identified one of the cellular factors responsible for this process, which is encoded by the fission yeast sud1 + gene."]
  [PMID:9653157 "Through genetic analysis we demonstrated that sud1 + stops unwanted diploidization and ensures stable maintenance of normal chromosomal DNA content in fission yeast."]

- Cloning of pop2; hetero-/homo-dimers; cullin-1 (abstract-only).
  [PMID:9990507 "Pop2 plays a role which overlaps with Pop1 in the degradation of Rum1 and Cdc18"]
  [PMID:9990507 "Pop1 and Pop2 form hetero-as well as homo-dimers in the cell"]
  [PMID:9990507 "By forming three distinct complexes, SCFPop1/Pop1, SCFPop1/Pop2 and SCFPop2/Pop2, SCF has evolved a sophisticated mechanism to control the level of Rum1 and Cdc18"]
  [PMID:9990507 "cullin-1 functions as a component of SCFPop1,2"]

- Pop1-Pop2 heteromer and Cdc18 capture (abstract-only; source of the PomBase IDA for GO:1990756).
  [PMID:10209119 "Pop1p and Pop2p formed heterooligomeric complexes when overexpressed"]
  [PMID:10209119 "binding of Cdc18p to Pop2p was dependent on Pop1p"]
  [PMID:10209119 "The Pop1p-Pop2p interaction was mediated by the amino-terminal domain of Pop2p which, when fused to full-length Pop1p, rescued the phenotype of a Deltapop1Deltapop2 double mutant."]
  [PMID:10209119 "the pop1 and pop2 genes fail to complement each other's deletion phenotypes, indicating that they perform non-redundant, but potentially interdependent, functions in proteolysis"]
  [PMID:10209119 "close physical proximity of two distinct F-box/WD-repeat proteins directs proteolysis mediated by the SCFPop ubiquitin ligase complex"]

- Endogenous SCF(Pop1-Pop2) complex, in vitro ligase activity, F-box requirement, localisation (full text
  cached; the principal biochemical source).
  [PMID:12167173 "co-elution of Pip1p with Pop1p, Pop2p, Pcu1p, and Psh1p in a high molecular weight complex of approximately 500 kDa"]
  [PMID:12167173 "Pip1p, Pop1p, and Pop2p antisera co-precipitated all five proteins from wild-type cell lysate"]
  [PMID:12167173 "A heterooligomeric SCFPop1p-Pop2p complex mediates polyubiquitylation of phosphorylated Rum1p"]
  [PMID:12167173 "Pop1p-Pop2p complexes specifically bound phosphorylated Rum1p"]
  [PMID:12167173 "His-Myc-Pop1p and His-Myc-Pop2p individually purified upon overexpression in pop1 pop2 double mutants exhibited no Rum1p binding above background"]
  [PMID:12167173 "Rum1p ubiquitylation was not obtained with Pip1p complexes prepared from cell lysate of pop2 deletion strains, proving the F-box protein dependency of this reaction"]
  [PMID:12167173 "Rum1p half-life was increased from ~20 minutes in wild-type to greater than 100 minutes in pop1 or pop2 mutants"]
  [PMID:12167173 "the Pop1p-Pop2p interaction occurs independently of the F-boxes of both Pop1p and Pop2p"]
  [PMID:12167173 "Only the F-box of Pop1p is required for SCFPop1p-Pop2p function, while Pop2p seems to be attracted into the complex through binding to Pop1p"]
  [PMID:12167173 "While F-box deleted Pop2p expressed from plasmids reduced Rum1p half-life to ~20 minutes in pop2 mutants, F-box-deleted Pop1p was completely defective in rescuing the Rum1p proteolysis defect of pop1 mutants"]
  [PMID:12167173 "both F-box proteins, in the absence of their respective heterooligomerization partner, could individually bind to Pip1p in complexes that also contained Psh1p and Pcu1p"]
  [PMID:12167173 "Pop1p and Pop2p each associate with polyubiquitylation activity even in the absence of their respective heterooligomerizing F-box proteins"]
  [PMID:12167173 "Pop1p is predominantly localized to cell nuclei, whereas Pop2p is expressed in both the cytoplasm and the nucleus"]
  [PMID:12167173 "Pop1p was detected mostly in nuclear fractions, while Pop2p was apparent in both nuclear and cytoplasmic fractions"]
  [PMID:12167173 "all five SCFPop1p-Pop2p subunits appear to coexist in the nucleus, although all but Pop1p are also present in the cytoplasm"]
  [PMID:12167173 "Pop1p, but not Pop2p, has a functional NLS in its N-terminus"]
  [PMID:12167173 "the cytoplasmic localization of Pop2p suggests an activity of SCFPop2p directed toward unknown cytoplasmic substrates"]

- Cig2 as an SCF(Pop1/Pop2) substrate (abstract-only).
  [PMID:14970237 "Two F-box/WD proteins Pop1 and Pop2, homologues of budding yeast Cdc4 and human Fbw7, are responsible for Cig2 instability"]
  [PMID:14970237 "Cig2 instability during G(2) and M phase is dependent upon the SCF complex"]
  [PMID:14970237 "Pop1 binds Cig2 in vivo"]

- Skp1 survey (abstract-only) and Pof14 paper (full text cached, no mention of Pop2 in the retained text).
  [PMID:15147268 "12 F-box proteins and Pcu1 were epitope-tagged, and co-immunoprecipitation performed"]
  [PMID:15147268 "It forms an adapter bridge between Cullin-1 and the substrate-determining component, the F-box protein"]
  [PMID:17016471 "provide substrate specificity to the SCF (Skp1, Cullin, F-box protein) E3 ubiquitin ligases by interacting with the core component Skp1 through their F-box motif"]

## Decision table (19 GOA rows; 20 in the TSV, the two PMID:15147268 Skp1 rows collapse to one)

| GO term | Evidence / reference / with | Action | One-line reason |
|---|---|---|---|
| GO:0005515 protein binding | IPI PMID:10209119 / Cdc18 (P41411) | MODIFY -> GO:1990756 | Substrate capture by the Pop1-Pop2 receptor; same paper as the IDA adaptor-activity annotation |
| GO:0005515 protein binding | IPI PMID:10209119 / Pop1 (P87060) | MODIFY -> GO:1990756 | Heterooligomerisation is how Pop2 is built into the substrate receptor; N-terminus fusion rescues the double deletion |
| GO:0005515 protein binding | IPI PMID:12167173 / Pcu1 (O13790) | MODIFY -> GO:1990756 | Endogenous cullin association within an active, pop2-dependent ligase; complex membership kept under GO:0019005/GO:0043224 |
| GO:0005515 protein binding | IPI PMID:12167173 / Pop1 (P87060) | MODIFY -> GO:1990756 | Heteromer, not either protein alone, binds phospho-Rum1; Pop2 F-box dispensable, so the Pop1 contact is the mechanism |
| GO:0005515 protein binding | IPI PMID:12167173 / Psh1 (Q9Y709) | MODIFY -> GO:1990756 | Canonical F-box/Skp1 attachment demonstrated at endogenous levels in a reconstituted ligase |
| GO:0005515 protein binding | IPI PMID:15147268 / Psh1 (Q9Y709) | REMOVE | Twelve-F-box survey of Skp1; adds nothing to the focused SCF(Pop) evidence; interaction not disputed |
| GO:0005515 protein binding | IPI PMID:17016471 / Psh1 (Q9Y709) | REMOVE | Pof14/ergosterol paper; Pop2 only a reference F-box; cached full text does not mention Pop2 |
| GO:0005515 protein binding | IPI PMID:9653157 / Cdc18 (P41411) | MODIFY -> GO:1990756 | Founding demonstration of phosphorylation-dependent substrate recognition (full text) |
| GO:0005515 protein binding | IPI PMID:9990507 / Pcu1 (O13790) | REMOVE | Same paper and partner underlie the GO:0019005 IPI; the binding row is a duplicate without function |
| GO:0005515 protein binding | IPI PMID:9990507 / Pop1 (P87060) | MODIFY -> GO:1990756 | Hetero-/homo-dimers are the substrate-receptor units controlling Rum1 and Cdc18 |
| GO:0005634 nucleus | IEA GO_REF:0000044 | ACCEPT | Endogenous-tag immunofluorescence and fractionation; the nuclear SCF acts on nuclear Cdc18/Rum1 |
| GO:0005737 cytoplasm | IEA GO_REF:0000044 | ACCEPT | Experimentally solid, distinguishes Pop2 from nuclear-restricted Pop1; substrates of the cytoplasmic pool unknown |
| GO:0019005 SCF ubiquitin ligase complex | IPI PMID:9990507 / cul1 | ACCEPT | Core CC; five-subunit ~500 kDa complex confirmed at endogenous levels with ligase activity |
| GO:0031146 SCF-dependent proteasomal ubiquitin-dependent protein catabolic process | ISO GO_REF:0000024 / CDC4 | ACCEPT | Core BP; transfer from Cdc4 fully corroborated by S. pombe genetics and in vitro ubiquitylation |
| GO:0043224 nuclear SCF ubiquitin ligase complex | ISO GO_REF:0000024 / CDC4 | ACCEPT | Transfer from Cdc4 corroborated by nuclear coexistence of all five SCF(Pop) subunits |
| GO:1903467 negative regulation of mitotic DNA replication initiation | IMP PMID:9653157 | ACCEPT | Core BP; Pop2 performs the phospho-Cdc18 recognition step; specific, correctly signed term |
| GO:1990756 ubiquitin-like ligase-substrate adaptor activity | IDA PMID:10209119 | ACCEPT | Core MF, correctly typed for a non-catalytic F-box receptor |
| GO:1990756 ubiquitin-like ligase-substrate adaptor activity | IEA GO_REF:0000117 / ARBA | ACCEPT | Electronic inference lands exactly on the experimentally established MF |
| GO:1990756 ubiquitin-like ligase-substrate adaptor activity | IPI PMID:14970237 / Cig2 | ACCEPT | Extends substrate range to Cig2; abstract reports Pop1 binding, deferring to the curator who read the full text |

Action counts: ACCEPT 9, MODIFY 7, REMOVE 3 (no UNDECIDED, no NEW).

## Notable curation decisions

1. Protein binding rows were split by information content rather than treated uniformly. The seven
   rows whose partner is a substrate (Cdc18) or the co-receptor Pop1, or that come from the paper
   demonstrating an active endogenous ligase (PMID:12167173), are MODIFY to GO:1990756 because each
   interaction is a step of the adaptor function. The three rows that duplicate a complex annotation
   from the same paper (cullin-1 in PMID:9990507) or come from surveys whose subject is another protein
   (Skp1 in PMID:15147268; Pof14 in PMID:17016471) are REMOVE as uninformative, with the explicit note
   that the interactions themselves are not disputed. This matches the pop1 review, where every
   protein-binding row was MODIFY to GO:1990756; the only divergence is that pop2 also carries survey-
   and duplicate-type rows that pop1 does not, and those are removed here.
2. Both localisation IEAs (nucleus and cytoplasm) are ACCEPT with core status. The cytoplasm row is
   kept as core because PMID:12167173 shows a Pop1-independent SCF(Pop2) complex with ligase activity
   and Pop2 lacks Pop1's NLS; this is modelled as a second core function with an explicit knowledge gap
   (no cytoplasmic substrate identified; the in vitro activity was a substrate-independent assay).
   The pop1 review removed the pop1 cytoplasm IBA because Pop1 is exclusively nuclear, so the two
   paralogues are deliberately treated differently on this term.
3. The two ISO transfers from S. cerevisiae Cdc4 (GO:0031146, GO:0043224) are ACCEPT with
   `propagation_review.root_cause: NO_FAILURE_CORE`, on the grounds that the fission yeast evidence
   independently establishes each claim.
4. GO:1903467 (IMP, PMID:9653157) passes the participation test: Pop2 itself performs the
   phospho-Cdc18 recognition step, so it is a core BP rather than a necessity-only phenotype term.
5. The Cig2 IPI for GO:1990756 (PMID:14970237) is ACCEPT despite the abstract naming Pop1, not Pop2,
   as the Cig2-binding protein, following the "do not overrule curators from incomplete evidence" rule.
6. No NEW terms were proposed. In particular GO:1900087 (positive regulation of G1/S transition), which
   pop1 carries by IMP, was not added to pop2 even though Rum1 half-life rises >5-fold in pop2 mutants;
   the omission is raised as a suggested question rather than filled in.
7. The deep-research Rev1 claim (Uchiyama 2015, PLoS One) was not used: the paper is not in the
   publication cache and no GOA row cites it.

## Open questions

- Is the absence of a G1/S-transition BP term on pop2 (present on pop1 by IMP) a deliberate reflection
  of the milder pop2 phenotype, or a curation gap?
- Does the Pop2 WD40 propeller contact phospho-Cdc18/phospho-Rum1 directly, or is the degron read by
  Pop1 with Pop2 acting to dimerise and stabilise the receptor? No Pop2 WD40 point mutant has been tested.
- What are the substrates of the cytoplasmic, Pop1-independent SCF(Pop2) complex?
- Should the SCF(Pop1-Pop2) heteromer and SCF(Pop2) homomer be represented as distinct complexes, with
  Cdc18/Rum1/Cig2 as `has_input` on the adaptor activity in a GO-CAM rather than as protein-binding rows?

## Housekeeping

- `just validate SCHPO pop2` passes (only warnings, if any, concern core-function terms not present in
  existing_annotations).
- The `references` list contains the deep-research file entry twice (identical content); harmless to
  validation, could be deduplicated in a later pass.
- PANTHER 19.0 places pop2 in a different family than the UniProt cross-references suggest (see
  modules/g1_s_transition.yaml); no PANTHER id is asserted in this review.
