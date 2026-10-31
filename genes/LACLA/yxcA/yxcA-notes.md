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

## KBase Dark Protein Atlas verdict

Item: https://gene-annotate-dashboard.kbase.us/review/NZ_VXKC01000008.1_19
(Lactococcus lactis, 1441 aa; part of the LBNL hackathon set, see
`projects/LBNL_HACKATHON.md`).

Dashboard call (tier A): "PlsA plasmalogen biosynthesis protein combining
activation and reduction/dehydration functions for anaerobic plasmalogen
production", with GO:0016491 oxidoreductase activity, GO:0016836 hydro-lyase
activity and GO:0008611 ether lipid biosynthetic process. Prior annotations:
eggNOG "hgdC", Pfam PF09989 (DUF2229).

**Dashboard verdict: supported.** The identification is right, and the call
correctly sets aside the eggNOG "hgdC" name, which describes the stand-alone
activator of 2-hydroxyglutaryl-CoA dehydratase (about 260 aa). The evidence is
stronger than the call knew: the 96.6%-identical L. cremoris PlsA is
sufficient for plasmalogen synthesis in E. coli (PMID:41427725). Three caveats:

- GO:0016836 hydro-lyase is an overreach. The dehydration step is only
  proposed by analogy with BCR/HAD enzymes. Not added in this review.
- GO:0016491 oxidoreductase is correct but generic. GO has no specific term,
  so I proposed one (see Annotation decisions).
- The description names the pathway and the domains, not the reaction. A
  better description: "Anaerobic plasmalogen synthase (single-chain PlsAR):
  converts the sn-1 acyl chain of diacyl glycerophospholipids into the
  1-alk-1'-enyl ether of the corresponding plasmalogen; iron-sulfur enzyme of
  the BCR/HAD family."

Do not map this protein to GO:0047159 "plasmalogen synthase activity". That
term is an acyltransferase on lysoplasmalogen (RHEA:10344), and it took the
EC 2.3.1.25 name in 2024 (go-ontology#27588). I checked all three against the
sources on 2026-10-30: the Rhea entry; the closed GO issue; and the term,
labelled "1-alkenylglycerophosphocholine O-acyltransferase activity" in GO
release 2024-01-17 and "plasmalogen synthase activity" in 2024-06-17. The
GO issues still pending are new ones: relabel the term, and add an MF term
for the anaerobic activity.

PANTHER supports the same point. Q9CDI2 is in PTHR32329:SF4, named "ACTIVATOR
OF 2-HYDROXYACYL-COA DEHYDRATASE". The family PTHR32329 is named "BIFUNCTIONAL
PROTEIN [INCLUDES 2-HYDROXYACYL-COA DEHYDRATASE (N-TER) AND ITS ACTIVATOR
DOMAIN (C_TERM)-RELATED" in PANTHER (panther.obo; yxcA-uniprot.txt). The
"Dehydratase Activator and Reductase Protein" name belongs to the integrated
InterPro entry IPR051805, and it is machine-generated and unchecked
(llm: true, checked: false in PTHR32329-metadata.yaml). All nine reviewed members of PTHR32329
(interpro/panther/PTHR32329/PTHR32329-entries.csv) are 243-438 aa proteins in
subfamily SF2. They are 2-hydroxyacyl-CoA dehydratase activators (HgdC, LcdC,
HadI, FldI), benzoyl-CoA reductase subunits (BcrA, BcrD) and three
uncharacterized proteins (E. coli YjiL, M. jannaschii MJ0004 and MJ0800).
None is in SF4. By their UniProt PANTHER cross-references (fetched in
yxcA-bioinformatics/RESULTS.md), the characterized single-chain plasmalogen
synthases S. mutans SMU_438c (Q8DVN8), E. faecalis EF1327 (Q835P9) and
M. elsdenii MeHAD (G0VRE7) are all in SF4, as are L. cremoris A2RP33 and
L. lactis yxcA. So the family names, like the eggNOG
"hgdC", describe a family relationship, not this protein's function.

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
- **Lactococcus, directly:** PMID:41427725 found plasmalogens in 4 of the
  5 L. cremoris strains tested [PMID:41427725 "Out of the 38 facultative anaerobic
  Lactobacillales strains tested, 11 were identified as plasmalogen
  producers"]. The authors cloned plsA from L. cremoris ATCC BAA-493
  (LACR_2543, 4,311 bp) [PMID:41427725 "These were named plsAK4 (4,248 bp),
  plsABAA493 (4,311 bp), and plsAsuis (4,920 bp), respectively."]. Expressing
  it in E. coli (strain PlsLc) gave plasmalogens under both aerobic and
  anaerobic conditions [PMID:41427725 "Both PlsLc and PlsBs produced
  plasmalogens, as evidenced by the detection of aldehydes in the lipid
  extracts after acid hydrolysis"]. The empty vector gave none.
- **Caveat:** the type strain JCM16167T makes no plasmalogen although it
  carries a plsA homolog, RU89_GL001778 [PMID:41427725 "Notably, of the five
  L. cremoris strains tested, only the type strain JCM16167T did not produce
  plasmalogen."]. No L. lactis subsp. lactis strain was among the 38
  tested. Non-production by one strain is most likely regulatory: a
  TetR/AcrR-like regulator sits directly upstream of pls in facultative
  anaerobes [PMID:33350306 "a TetR/AcrR-like transcriptional regulator
  (EF1326) directly upstream of the pls gene (EF1327)"]. That the enzyme
  works is shown directly by heterologous expression, so the caveat bears
  on whether L. lactis IL1403 makes plasmalogens in vivo. It does not bear
  on the function of the protein.
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
- MF: GO:0051539 4 iron, 4 sulfur cluster binding (NEW, ISS; supporting,
  not in core_functions). It is based on the conserved cysteines and the
  BCR/HAD family property. In M. elsdenii MeHAD, a combined mutant of the
  four predicted ligand cysteines is inactive [PMID:37348645 "The
  four-cysteine (Cys125, Cys164, Cys445 and Cys484) site-mutant of MeHAD,
  which were predicted binding to the [4Fe-4S] cluster, was unable to
  synthesize plasmalogens"]. In the global alignment computed in
  yxcA-bioinformatics/RESULTS.md (48.7% identity) these are Q9CDI2 C126,
  C165, C445 and C484. The PMID:37348645 record is abstract-only. The cluster itself has not been
  observed on any PlsA.
- Proposed MF term: renamed "plasmalogen-forming diacylglycerophospholipid
  reductase activity" to match the drafted GO new-term request. Its
  definition now states only the overall conversion. The ATP-dependent
  radical mechanism, which is proposed by analogy, is in the justification.
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
