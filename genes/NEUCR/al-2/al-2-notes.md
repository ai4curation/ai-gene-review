# al-2 (P37295, NCU00585) curation notes — Neurospora crassa

## Identity

- UniProt P37295, LCPS_NEUCR, "Bifunctional lycopene cyclase/phytoene synthase",
  AltName "Protein albino-2". 602 aa. Gene al-2, ORFNames B22I21.230, NCU00585.
- Two enzymatic activities are recorded by UniProt with experimental evidence:
  - Phytoene synthase, EC 2.5.1.32 [file:NEUCR/al-2/al-2-uniprot.txt "EC=2.5.1.32"]
  - Lycopene beta-cyclase, EC 5.5.1.19 [file:NEUCR/al-2/al-2-uniprot.txt "EC=5.5.1.19"]
- N-terminal region (1..241) = lycopene beta-cyclase; C-terminal region (248..602)
  = phytoene synthase [file:NEUCR/al-2/al-2-uniprot.txt "Lycopene beta-cyclase";
  "Phytoene synthase"]. Deep research independently gives ~1-244 cyclase /
  remaining 358 residues synthase [file:...deep-research-falcon.md "N-terminal
  residues 1–244 form the cyclase region"].
- Distinct from al-1 (NCU00552, phytoene desaturase) and al-3 (GGPP synthase)
  [file:...deep-research-falcon.md "al-3, geranylgeranyl-diphosphate synthase"].
  This matters because two IEA InterPro rows try to give al-2 the activities of
  neighbouring/paralogous enzymes.

## Cached evidence status

- PMID:11862485 (Arrach 2002, Mol Genet Genomics) — ABSTRACT ONLY
  (full_text_available: false). Isolated two reddish al-2 cyclase-domain mutants
  (JA26 W189R, JA28 K208E) that lose cyclase activity and neurosporaxanthin;
  concludes al-2 product is bifunctional. Source of the IDA rows for GO:0046905,
  GO:0045436, GO:0016117, GO:0016120. The catalytic-activity records in UniProt
  cite this PMID with ECO:0000269 (experimental), i.e. the curator read the full
  text; I defer to that for the enzymatic activities.
- PMID:16928467 (Sandmann 2006, BBA) — ABSTRACT ONLY. al-2 cDNA cloned, expressed,
  functionally characterized; "enzyme comprised the two catalytic activities of a
  phytoene synthase and a lycopene cyclase"; monocyclic-acting, "first CrtYB-type
  monocyclic-acting lycopene cyclase". Source of a second set of IDA rows.
- PMID:8163509 (Schmidhauser 1994, JBC) — ABSTRACT ONLY. Cloning + photoregulation
  of al-2; "segment homologous to prokaryotic and other eukaryotic phytoene
  synthases"; al-2 mRNA increased >30-fold on photoinduction. Not a GOA row but the
  UniProt ECO:0000303 basis for the phytoene synthase name; fetched for context.
- GO-CAM gocam:62f58d8800000065 (Carotenoid biosynthesis, N. crassa, production):
  al-2 (P37295) appears with GO:0046905 (activity ...066) and GO:0045436
  (activities ...115/...123/...131 for the three cyclizations to gamma-carotene,
  beta-carotene and torulene), each part_of GO:0016117, evidence ECO:0000314
  PMID:11862485. Confirms the two-function model.

## Reaction / pathway (UniProt CATALYTIC ACTIVITY + PATHWAY)

- 2 GGPP = 15-cis-phytoene + 2 diphosphate (RHEA:34475, EC 2.5.1.32)
  [file:...uniprot.txt "Reaction=2 (2E,6E,10E)-geranylgeranyl diphosphate =
  15-cis-phytoene + 2"].
- all-trans-lycopene = gamma-carotene (RHEA:32219); gamma-carotene =
  all-trans-beta-carotene (RHEA:32239); both EC 5.5.1.19
  [file:...uniprot.txt "Reaction=all-trans-lycopene = gamma-carotene";
  "Reaction=gamma-carotene = all-trans-beta-carotene"].
- Native flux: al-2 phytoene synthase -> al-1 desaturations -> al-2 cyclase forms
  torulene (from 3,4-didehydrolycopene) / gamma-carotene; cao-2 cleaves, ylo-1
  oxidizes to neurosporaxanthin [file:...uniprot.txt "Torulene is the substrate of
  the dioxidase cao-2"; deep-research pathway section]. Single cyclizations
  preferred, so monocyclic products dominate natively
  [PMID:16928467 "single cyclizations were preferentially catalyzed"].

## Annotation-by-annotation reasoning

Molecular function — TRUE activities (ACCEPT):
- GO:0046905 15-cis-phytoene synthase activity: IBA, IDA x2 (11862485, 16928467),
  IEA(RHEA:34475/EC:2.5.1.32). Core function; directly assayed and Rhea/EC-grounded.
- GO:0045436 lycopene beta cyclase activity: IDA x2 (11862485, 16928467),
  IEA(RHEA:32219). Core function; directly assayed and Rhea-grounded.

Molecular function — InterPro2GO paralog over-annotations (REMOVE, per brief and
mirroring genes/PANAN/crtB):
- GO:0004311 geranylgeranyl diphosphate synthase activity (IEA, IPR044843
  Trans_IPPS_bact-type). QuickGO def = FPP + IPP -> GGPP. al-2 CONSUMES GGPP as the
  phytoene synthase substrate; GGPP is made by the separate gene al-3. Fold-level
  trans-IPPS signature cannot discriminate chain elongation from head-to-head
  condensation. REMOVE.
- GO:0051996 squalene synthase [NAD(P)H] activity (IEA, IPR033904 Trans_IPPS_HH).
  QuickGO def = 2 FPP + NAD(P)H -> squalene. al-2 uses GGPP not FPP, makes phytoene
  not squalene, needs no NAD(P)H. IPR033904 is the head-to-head domain shared by
  phytoene and squalene synthases by construction. REMOVE.

Molecular function — over-general true-ish parents (MODIFY to the specific
directly-assayed activity):
- GO:0016765 transferase activity, transferring alkyl or aryl (other than methyl)
  groups (IEA, IPR019845 Squalene/phytoene_synthase_CS). QuickGO ancestor check:
  GO:0046905 IS a descendant of GO:0016765 (via GO:0004659 prenyltransferase). The
  family conserved-site signature only licenses the generic level; direct assay
  establishes the specific reaction. MODIFY -> GO:0046905. (Same handling as crtB.)
- GO:0016872 intramolecular lyase activity (IEA, IPR017825 Lycopene_cyclase_dom).
  IPR017825 is specifically the lycopene cyclase domain, and EC 5.5.1.19 sits in
  EC subclass 5.5 (intramolecular lyases), so the InterPro2GO mapping intent is
  "this domain performs the lycopene cyclization." al-2 holds the specific activity
  GO:0045436 by direct assay, so MODIFY -> GO:0045436. NOTE: in the current GO
  hierarchy GO:0045436 is placed under GO:0009975 cyclase activity / GO:0016860
  intramolecular oxidoreductase, NOT under GO:0016872 (verified via QuickGO
  ancestors) — so I do not claim a descendant relationship; the MODIFY is justified
  by the domain-signature intent plus the directly-assayed specific activity, not by
  ontology subsumption.

Cellular component:
- GO:0016020 membrane (IEA, UniProtKB-SubCell SL-0162). UniProt: "Membrane;
  Multi-pass membrane protein {ECO:0000255}", 7 predicted TM helices in the feature
  table. Sequence-based (no experimental localization in N. crassa
  [file:...deep-research-falcon.md "No direct study was found that localizes native
  AL-2"]), but carotenoid biosynthesis enzymes act on membrane-embedded hydrophobic
  substrates and the 7-TM prediction is strong. ACCEPT (general but correct).

Biological process:
- GO:0016117 carotenoid biosynthetic process (IBA + IDA). ACCEPT. al-2 catalyses
  two steps of this pathway.
- GO:0016120 carotene biosynthetic process (IDA x2). ACCEPT. Phytoene, gamma-,
  beta-carotene, torulene are hydrocarbon carotenes; al-2 makes them. (Per brief,
  GO:0016120 is NOT a descendant of GO:0016117 in the current ontology; both are
  legitimately held, neither is redundant. Not "fixing" this.)

## NEW annotations

None proposed. Both molecular activities and both relevant processes are already
present. Blue-light induction of al-2 (WCC target, PMID:8163509 / deep research) is
regulation OF the gene, not a function the al-2 protein performs, so it fails the
participation test and no "response to light" process term is added. beta-carotene
biosynthetic process (GO:1901812) was considered but not added: natively al-2
prefers single cyclizations toward monocyclic torulene/neurosporaxanthin rather
than bicyclic beta-carotene, so the existing carotene/carotenoid process terms are
the better-supported level; raised instead as a suggested question.

## Knowledge gaps

- No experimental subcellular localization in N. crassa (which membrane, whether
  processed) [file:...deep-research-falcon.md "No direct study was found that
  localizes native AL-2"].
- No purified-enzyme kinetics / cofactor determination for native al-2.
- Structural basis of monocyclic (single-cyclization) preference vs bicyclic
  cyclases is unknown.
