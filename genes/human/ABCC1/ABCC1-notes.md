# ABCC1 (MRP1) curation notes

UniProt: P33527 (MRP1_HUMAN). HGNC:51. 1531 aa, 17 transmembrane helices, two cytoplasmic
nucleotide-binding domains (NBD1, NBD2). Belongs to the ABC transporter superfamily, ABCC
family, conjugate transporter (TC 3.A.1.208) subfamily. EC 7.6.2.- (7.6.2.2, 7.6.2.3).

## Core biochemistry

ABCC1/MRP1 is a primary-active (ATP-hydrolysis-driven) efflux pump for organic anions. It was
cloned from the doxorubicin-selected multidrug-resistant lung-cancer line H69AR as an
overexpressed ABC transporter [PMID:1360704 "member of the ATP-binding cassette transmembrane transporter superfamily"].
The prototypical, highest-affinity endogenous substrate is the glutathione S-conjugate
leukotriene C4 (Km ~97 nM) [PMID:7961706 "The endogenous glutathione conjugate LTC4 had the highest affinity for this"].
ATP-dependent vesicular transport was demonstrated for LTC4, LTD4, LTE4 and
S-(2,4-dinitrophenyl)glutathione [PMID:7961706 "ATP-dependent primary-active transport into the vesicles was demonstrated for"].

UniProt summarizes the activity as an ATP-dependent transporter that
"hydrolyzes ATP to enable the active transport of organic" anions conjugated with glutathione,
glucuronate or sulfate (file:human/ABCC1/ABCC1-uniprot.txt, CC FUNCTION). Documented catalytic
activities (RHEA, with experimental PubMed evidence) include S-substituted glutathione export
(EC 7.6.2.3, RHEA:19121), LTC4/LTD4/LTE4, glutathione and glutathione disulfide (GSH/GSSG),
estradiol-17-glucuronide, bilirubin mono/bis-glucuronides, taurolithocholate-3-sulfate,
prostaglandin A2-glutathione diastereomers, 2'3'-cGAMP, sphingosine-1-phosphate, daunorubicin
and vincristine.

Substrate breadth / physiological substrates
[PMID:9426231 "The human multidrug resistance protein MRP1 mediates transport of organic" substrates conjugated to glutathione, glucuronide, or sulfate]:
glutathione-, glucuronide- and sulfate-conjugates. Basolateral export of GSH-prostaglandin A
conjugates shown in polarized MDCKII cells, consistent with
[PMID:9426231 "the lateral localization of human MRP1 in these cells"].

## Multidrug resistance (drug efflux)

MRP1 confers resistance to a structurally diverse range of drugs. In transfected HEK cells,
[PMID:9281595 "human MRP has also been shown to be a primary active transporter of a" structurally diverse range of organic anionic conjugates];
mouse and human orthologs
[PMID:9281595 "mrp and MRP conferred similar drug resistance profiles, with the" exception that only MRP conferred resistance to the anthracyclines tested].
Many unmodified drugs (vincristine) are co-transported only in the presence of GSH. EC 7.6.2.2
(ABC-type xenobiotic transporter).

## Additional (physiologically important but secondary) substrates

- Glutathione / GSSG export: main pathway for GSH release from astrocytes; upregulated by
  monomeric amyloid-beta [PMID:26200696 "the transporter ABCC1 (also referred to as MRP1) that is the main pathway for GSH release"],
  [PMID:26200696 "cortical ABCC1 was significantly increased in temporal register with the surge of" Abeta levels].
  UniProt: MRP1 can "export both GSH and its oxidized form GSSG in a protective mechanism"
  "that limits cellular damage especially during oxidative stress" (CC FUNCTION). → redox
  homeostasis / cytoprotection.
- Sphingosine-1-phosphate (S1P) export from mast cells, independent of degranulation
  [PMID:17050692 "S1P is exported from mast cells independently of their degranulation"],
  MK571-sensitive; siRNA knockdown reduced surface expression and S1P export; S1P transport
  [PMID:17050692 "Transport of S1P by ABCC1 influenced migration of mast cells toward antigen but not degranulation"].
- 2'3'-cGAMP export: direct ATP-dependent exporter limiting cGAS-STING signaling
  [PMID:36070769 "we identifed ABCC1 as a direct, ATP-dependent cGAMP exporter in mouse and human cells"],
  [PMID:36070769 "loss of ABCC1 reduced cGAMP export and potentiated STING signaling"]. (Note: source
  contains the typo "identifed".)
- Cobalamin (vitamin B12) export: proposed cellular cobalamin exporter (Beedholm-Ebsen 2010,
  the paper commented on in [PMID:21511966]); reviewed in [PMID:22547309] as part of the B12
  trafficking pathway; modelled by Reactome (RCbl export). Treated here as a documented but
  non-core / peripheral substrate; primary transport assays are not in the local cache.

## Localization

Multi-pass plasma-membrane protein (extracytosolic N-terminus). In polarized epithelia MRP1 is
predominantly basolateral:
- Sertoli cells (blood-testis barrier): [PMID:24130369 "MRP1 was restricted to the basolateral membrane of Sertoli cells"] (IDA, full text, rat/macaque/human).
- Choroid plexus / blood-CSF barrier: [PMID:25986174 "confirmed basolateral expression of ABCC1"]; functional efflux shown ([PMID:25986174 "Functionality of ABCC1, ABCC4, ABCB1" and ABCG2 could be shown in uptake assays]).
- Rat BBB: [PMID:18619525 "Mrp1 (Abcc1) appeared primarily abluminal by immunofluorescence"] (i.e. basal/abluminal), and basal-lateral in choroid plexus.
- Retinal pigment epithelium: present on both surfaces [PMID:31791063 "Most drug transporters showed similar abundance on both RPE surfaces"] (apical + basolateral + lateral IDA).
- Membrane/plasma-membrane proteomics: NK-cell membrane proteome (HDA, [PMID:19946888]), hCMEC/D3 ([PMID:23137377 "MRP1 and ATA1 were found only in hCMEC/D3 cells"]), RPE plasma membranes ([PMID:28112518 "MRP1, MRP5, GLUT1, 4F2hc, TAUT, CAT1,"]).
- DFNA77 hearing-loss variant p.Asn590Ser mislocalizes; [PMID:31273342 "wild type was shown only in cytomembrane"].

Over-annotations / context terms judged non-core or over-annotated:
- extracellular exosome (HDA, [PMID:20458337]): single large exosome proteome; non-core.
- cell junction (immunofluorescence GO_REF:0000052): likely lateral-membrane staining read as
  junction; MRP1 is not a junction protein → over-annotation.
- sphingolipid biosynthetic process (Reactome TAS): MRP1 exports the end-product S1P, it does
  not perform a biosynthetic step → over-annotation (participation test fails).
- heme catabolic process (Reactome TAS): MRP1 exports bilirubin-glucuronide catabolites
  (elimination step); kept non-core.

## Disease

Autosomal dominant non-syndromic hearing loss DFNA77 (MIM:618915); variant p.Asn590Ser causes
unstable mRNA and decreased efflux capacity [PMID:31273342].

## Review decisions summary

Core functions (synthesized): (1) ATP-dependent export of glutathione S-conjugates / LTC4 /
organic anions (GO:0015431); (2) ATP-dependent drug/xenobiotic efflux → multidrug resistance
(GO:0008559); (3) GSH/GSSG export → redox homeostasis (GO:0034634); (4) 2'3'-cGAMP export →
STING regulation (GO:0140359, substrate cGAMP); (5) S1P export → mast-cell signaling
(GO:0034040). Localization: basolateral plasma membrane (GO:0016323).
</content>
</invoke>
