# yxcA (Q9CDI2), Lactococcus lactis subsp. lactis IL1403: notes

## Entry and identity

- UniProtKB Q9CDI2 (unreviewed, 1436 aa). Gene name *yxcA*, locus tag
  L104115, EMBL AAK06336.1. The entry is in the L. lactis reference proteome
  (UP000002196).
- UniProt name "2-hydroxyglutaryl-CoA dehydratase" is a ProtNLM prediction
  (ECO:0008006). Its [4Fe-4S] cofactor and iron-sulfur keywords come from
  ARBA. Neither is evidence.
- GOA has no annotations for Q9CDI2 (the goa.tsv is empty), so every
  annotation in this review is NEW.
- How the review started: KBase "Dark Protein Atlas" hackathon item
  NZ_VXKC01000008.1_19 (L. lactis, eggNOG name "hgdC"). That sequence is
  UniParc UPI00072AC48C (RefSeq WP_081041604, 1441 aa). It formerly had
  TrEMBL entries A0A0V8CX59 and A0A2A5SIM0. UniProt deleted both as "Not
  part of a reference proteome". Q9CDI2 is the closest active entry, at 98.3%
  identity
  [file:LACLA/yxcA/yxcA-bioinformatics/RESULTS.md].

## Function: plasmalogen synthase PlsA

- Plasmalogens are vinyl-ether (1-alk-1'-enyl, 2-acyl) glycerophospholipids.
  In anaerobic bacteria they are made by reducing the sn-1 ester of a diacyl
  lipid. This differs from the aerobic route, which oxidizes an ether
  [PMID:33350306 "anaerobic plasmalogen biosynthesis uses the reductive
  conversion of an ester to an aldehyde equivalent"].
- In C. perfringens the pls operon encodes PlsA (Act1, Act2, Red1) and PlsR
  (Red2). Deleting the operon abolishes plasmalogens, and expressing it in
  E. coli confers them [PMID:33350306 "Heterologous expression of the C.
  perfringens pls operon in E. coli conferred the ability to produce
  plasmalogens"].
- In facultative anaerobes the four domains are fused into one chain
  [PMID:33350306 "The E. faecalis gene EF1327 encodes all activation and
  reduction/dehydration domains as a single polypeptide (PlsA)"]. EF1327
  alone is sufficient in E. coli [PMID:33350306 "we observed plasmalogen
  production in E. coli harboring the pPlsEF plasmid"].
- **Lactococcus, directly:** PMID:41427725 found plasmalogens in
  L. cremoris strains [PMID:41427725 "Out of the 38 facultative anaerobic
  Lactobacillales strains tested, 11 were identified as plasmalogen
  producers"]. The authors cloned plsA from L. cremoris ATCC BAA-493
  (LACR_2543, 4,311 bp) [PMID:41427725 "These were named plsAK4 (4,248 bp),
  plsABAA493 (4,311 bp), and plsAsuis (4,920 bp), respectively."]. Expressing
  it in E. coli (strain PlsLc) gave plasmalogens under both aerobic and
  anaerobic conditions [PMID:41427725 "Both PlsLc and PlsBs produced
  plasmalogens, as evidenced by the detection of aldehydes in the lipid
  extracts after acid hydrolysis"]. The empty vector gave none.
- Q9CDI2 is 96.6% identical over its full length to LACR_2543 (ABJ73971.1)
  and 67.3% identical to EF1327
  [file:LACLA/yxcA/yxcA-bioinformatics/RESULTS.md].
- Domains: Act1 (PF01869, 7-257), Act2 (PF01869, 322-576) and Red1
  (PF09989/DUF2229, 676-897) are detected by Pfam. Pfam's HGD-D model does
  not detect Red2, but residues 1011-1411 align to C. perfringens PlsR at
  41.3% identity, so the C-terminus is the fused Red2 domain. The protein is
  full length, not just an "HgdC-like activator".
- Mechanism (proposed, by analogy to BCR/HAD enzymes; not shown
  biochemically): ATP-driven electron transfer from the activator domains
  makes a ketyl radical at the sn-1 ester, followed by a second reduction and
  a final dehydration [PMID:33350306 "The sequence would involve an initial
  reduction of the sn-1 linked ester to a ketyl radical anion, protonation, a
  second reduction-protonation sequence, and a final dehydration"]. The
  electron donor is presumed to be ferredoxin, as in HAD/BCR. Neither the
  donor nor the in vitro activity has been shown for any PlsA.
- Iron-sulfur cluster: the Act-domain cysteines are conserved [PMID:33350306
  "Act1 and Act2 also share conserved cysteines for iron–sulfur cluster
  ligation with HAD and BCR activation domains"]. Eight of the nine
  cysteines in Q9CDI2 residues 1-620 are conserved in EF1327 and in
  C. perfringens PlsA (RESULTS.md). The cluster itself has not been observed
  experimentally.
- Oxygen: the E. faecalis enzyme works only anaerobically. The L. cremoris
  enzyme is unusually oxygen tolerant [PMID:41427725 "the PlsLc strain
  produced more than three times the amount of plasmalogen as the other
  strains, even under aerobic conditions"]. The authors attribute this to a
  C-terminal helix, using AlphaFold3 models only.
- The plasmalogen-producing E. coli strain had lower ROS and better
  tolerance of 1 M NaCl (PMID:41427725). These are effects of the lipid in a
  heterologous host, not functions of the enzyme, so I do not annotate them.

## Annotation decisions

- BP: GO:0008611 ether lipid biosynthetic process (NEW, ISS from LACR_2543).
  GO has no plasmalogen-specific biosynthesis term (the only child of
  GO:0008611 is PAF biosynthesis). The substrate-vs-participant test passes:
  this protein catalyses the vinyl-ether-forming step.
- MF: GO has no term for the reductive diacyl-to-plasmalogen conversion.
  GO:0047159 "plasmalogen synthase activity" is an acyl-CoA acyltransferase
  (EC 2.3.1.25) reaction and is WRONG for PlsA. Do not use it. I proposed a
  new term and used `proposed_molecular_function` in core_functions.
  I did not add generic GO:0016491 (oxidoreductase) or GO:0016836
  (hydro-lyase): the redox chemistry is inferred from family analogy, and the
  dehydration step is only a mechanistic proposal.
- MF: GO:0051539 4 iron, 4 sulfur cluster binding (NEW, ISS, non-core). It is
  based on the conserved cysteines plus the BCR/HAD family property. It is
  not observed on any PlsA.
- CC: no annotation. DeepTMHMM (KBase run on UPI00072AC48C) predicts a
  globular, cytoplasmic protein, yet the substrate is a membrane
  phospholipid. Whether PlsA associates with the membrane is unknown, so I
  made no CC call.
- Comparator check for the BP term (QuickGO, 2026-10-30): the enzyme that
  forms the vinyl ether by the aerobic route, Myxococcus xanthus CarF
  (Q9AE87, plasmanyl desaturase), carries GO:0008611 by IDA
  (PMID:31604315). So the term is used for the enzyme that does the
  equivalent step. EF1327 (Q835P9) and L. cremoris llmg_2516 (A2RP33) have no
  GOA annotations at all. The absence on PlsA proteins is a curation gap for
  a recently characterized family, not a convention against the term.
