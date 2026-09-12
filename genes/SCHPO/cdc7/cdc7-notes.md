# cdc7 (SPBC21.06c, P41892) — S. pombe SIN initiating kinase — review notes

## CRITICAL identity caveat
S. pombe **cdc7 is the SIN (Septation Initiation Network) protein kinase**, NOT the
DDK/Dbf4-dependent replication kinase. The replication initiation kinase in fission yeast
(the true Cdc7/CDC7 ortholog of budding yeast Cdc7 and human CDC7) is **Hsk1**. Therefore
no DNA-replication / origin-firing / DDK function should be imported onto pombe cdc7.

## Core function
Cdc7 is the most upstream protein Ser/Thr kinase of the SIN. It is recruited to the
spindle pole body (SPB) by GTP-bound Spg1 (on the Cdc11–Sid4 scaffold), and acts at the
top of the SIN kinase cascade (Cdc7 -> Sid1–Cdc14 -> Sid2–Mob1) to trigger contractile-ring
constriction and septum formation (cytokinesis). It localizes asymmetrically to one SPB
(the new/daughter SPB) in late anaphase, which is important for SIN regulation.

## Key evidence

- Cdc7 is a protein kinase essential for cell division; loss prevents septum formation and
  cytokinesis; overexpression drives multiple rounds of septation; multi-septation requires
  kinase activity and depends on cdc11.
  [PMID:8039497 "We have cloned the cdc7 gene and show that it encodes a protein kinase which is essential for cell division. In the absence of cdc7 function, spore germination, DNA synthesis and mitosis are unaffected, but cells are unable to initiate formation of the division septum."]
  [PMID:8039497 "Overexpression of p120cdc7 causes cell cycle arrest; cells complete mitosis and then undergo multiple rounds of septum formation without cell cleavage. This phenotype ... requires the kinase activity of p120cdc7."]
  [PMID:8039497 "the p120cdc7 protein kinase plays a key role in initiation of septum formation and cytokinesis in fission yeast and suggest that p120cdc7 interacts with the cdc11 protein in the control of septation."]
  Note: DNA synthesis and mitosis are explicitly UNAFFECTED in cdc7 loss — confirms this is NOT a replication kinase.

- Cdc7 interacts with the Spg1 GTPase; Spg1 activity is needed for Cdc7 SPB localization
  (not for its in vitro kinase activity). Cdc7 is on both SPBs early in mitosis then on only
  one pole during anaphase B (asymmetric segregation).
  [PMID:9420333 "early in mitosis it associates with both spindle pole bodies and, as the spindle extends, is seen on only one pole of the spindle during anaphase B. Spg1p activity is required for localization of Cdc7p in vivo but not for its kinase activity in vitro."]
  [PMID:9420333 "asymmetric distribution of Cdc7p may be mediated by inactivation of Spg1p on one spindle pole."]

- Spg1-GTP binds Cdc7 and recruits it to SPB; SPB-localized Cdc7 promotes activation of
  Sid2 kinase, which moves to the division site to trigger cytokinesis.
  [PMID:19736319 "Once activated, Spg1-GTP binds the Cdc7 kinase and recruits it to the spindle pole body (SPB; Sohrmann et al., 1998). SPB-localized Cdc7 then promotes activation of the Sid2 protein kinase (Sparks et al., 1999). Active Sid2 translocates from the SPB to the cell division site to trigger cytokinesis."]
  Cdc7 fluorescence at single SPB increases ~2.5-fold in late anaphase (Etd1/Spg1 hyperactivation reporter).
  [PMID:19736319 "In wild-type cells, Cdc7-GFP localizes to both SPBs in early mitosis and then to just one SPB in anaphase and telophase"]

- Cdc7 kinase activity is required for mitotic hyperphosphorylation of the SIN scaffold
  Cdc11; cdc11 is a Cdc7 substrate/target in vivo.
  [PMID:12546793 "We demonstrate that mitotic hyperphosphorylation of cdc11p requires the activity of cdc7p ... We conclude that cdc11p hyperphosphorylation correlates with activation of the SIN and that this may be mediated primarily by cdc7p in vivo."]
  Supports both protein Ser/Thr kinase activity (EXP) and septation initiation signaling.

- Cdc11 + Sid4 form the SPB scaffold that anchors all SIN proteins (including Cdc7) at SPB.
  [PMID:11676915 "cdc11p is required for the localization of all the known SIN components, except sid4p, to the SPB."]

- Asymmetric Spg1/Cdc7 segregation: Byr4–Cdc16 GAP localizes to the SPB lacking Cdc7; in
  byr4- mutants Cdc7 localizes symmetrically.
  [PMID:10381387 "One of the roles of the spg1p GTPase is to localise the cdc7p protein kinase to the poles of the mitotic spindle, from where the onset of septation is thought to be signalled at the end of mitosis. ... cdc7p is located on both spindle pole bodies early in mitosis, but only on one during the later stages of anaphase."]
  [PMID:10799520 "Spg1 accumulates in an active, GTP-bound form and binds the Cdc7 protein kinase to cause Cdc7 translocation to SPBs. Cdc7 disappears from one SPB in mid-anaphase and from the second SPB in late mitosis. ... Byr4 was localized to SPBs that did not contain Cdc7. In byr4(-) mutants, Cdc7 localized to interphase SPBs and only symmetrically localized to mitotic SPBs."]

- SIP/PP2A (Csc1) complex dephosphorylates Cdc11 and propagates SIN asymmetry; Cdc7 and
  Sid1 localize asymmetrically to the newly duplicated SPB in late anaphase.
  [PMID:22119525 "Two of the SIN kinases, Cdc7p and Sid1p, localize asymmetrically to the newly duplicated SPB in late anaphase."]

- SIN (including Cdc7) is required for spore formation in meiosis; Cdc7 and Sid1 associate
  with the meiotic SPB in meiosis II when forespore membrane deposition begins.
  [PMID:16787941 "The protein kinases Sid1p and Cdc7p do not associate with the spindle pole body until meiosis II, when forespore membrane deposition begins. These data indicate a role for the SIN in regulating spore formation during meiosis."]
  Supports meiotic SPB localization (GO:0035974).

- Dma1-dependent degradation of Cdc7 (and Cdc11, Sid4) after meiosis II; Cdc7 localization to
  meiotic SPB; in meiosis GTP-Spg1 is not the main determinant of Cdc7 SPB timing.
  [PMID:24838944 "there is stage-specific degradation of SIN components in meiosis; Byr4p is degraded after meiosis I, whereas the degradation of Cdc7p, Cdc11p and Sid4p occurs after the second meiotic division and depends upon the ubiquitin ligase Dma1p."]
  Supports meiotic SPB localization (GO:0035974).

- Etd1 links SIN to cytokinesis; Cdc7-GFP at SPB used as readout of Spg1 activity.
  [PMID:15933715 "The protein kinase Cdc7p is asymmetrically recruited to the SPB that maintains the activated form of Spg1p (Sohrmann et al, 1998) and Sid1p-Cdc14p binds to this activated SPB."]
  Supports old/new mitotic SPB localization.

- SIN activity (Cdc7-GFP at SPB used as marker) disperses Cdr2/Mid1 type-1 nodes.
  [PMID:25501814 "Activating the SIN in interphase cells dispersed Cdr2p and anillin Mid1p from type 1 nodes a few min after the SIN kinase Cdc7p-GFP accumulated at spindle pole bodies."]
  Supports mitotic SPB localization (IDA via Cdc7-GFP marker).

- Pcp1 / Pmo25 papers use Cdc7-GFP as the established asymmetric daughter-SPB marker.
  [PMID:19942852 "we exploited asymmetric SPB localisation of Cdc7, one of the SIN kinases (Sohrmann et al, 1998). Cdc7 localises to both SPBs in early mitosis, but remains only on the daughter SPB in late anaphase"]
  [PMID:16325501 "Pmo25p shows no distinct localization during interphase, but it is recruited to one of the two spindle pole bodies during anaphase ... The septation initiation network (SIN) regulates the localization of Pmo25p"]
  These support new mitotic SPB (GO:0071958) localization of Cdc7 (IDA, Cdc7-GFP imaged directly).

## UniProt notes
- EC 2.7.11.1 (non-specific Ser/Thr kinase). Protein kinase domain 9-259, ATP binding 15-23, 38;
  Mg2+ cofactor; active site 131.
- SUBUNIT: Interacts with spg1; seems to interact with cdc11 [PMID:9203579 — INTERACTION WITH SPG1; not cached].
- Family: protein kinase superfamily, Ser/Thr protein kinase family, CDC7 subfamily.

## Annotation-by-annotation judgments
- MF kinase activities (GO:0004674 serine/threonine, GO:0106310 serine, GO:0004672 protein kinase,
  GO:0005524 ATP binding): all ACCEPT. EXP/IMP evidence for Ser/Thr kinase activity is direct (8039497,
  9420333, 12546793). IEA from RHEA/InterPro/EC consistent. ATP binding consistent with kinase domain.
- GO:0000165 MAPK cascade (IBA): scrutinize. pombe cdc7 is a SIN kinase cascade kinase, NOT a MAPK
  cascade component. MAPK cascade is a defined three-tiered MAP3K->MAP2K->MAPK module; SIN is a distinct
  GTPase-regulated kinase cascade. IBA from PANTHER groups cdc7 with budding yeast CDC15 (MEN kinase) /
  STE20-like kinases. This IBA over-propagates "MAPK cascade" onto a non-MAPK kinase. Mark as
  MARK_AS_OVER_ANNOTATED / NOT a core MAPK function. No experimental support for cdc7 in a MAPK cascade.
  Better: septation initiation signaling (already separately annotated). Action: REMOVE (over-propagated
  IBA, no evidence cdc7 acts in a MAPK cascade in pombe).
- Septation initiation signaling GO:0031028 (EXP x2, IMP): ACCEPT — core.
- GO:0140281 positive regulation of mitotic division septum assembly (IMP, 8039497): ACCEPT — core.
- SPB CC terms (GO:0044732 mitotic SPB; GO:0071957 old mitotic SPB; GO:0071958 new mitotic SPB;
  GO:0035974 meiotic SPB): all ACCEPT, direct IDA via Cdc7 antibody/Cdc7-GFP imaging. Asymmetry to
  new/daughter SPB is well established.
