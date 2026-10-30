# PCK1 (human, P35558) curation notes

## Deep research status

- 2026-10-16: `just deep-research human PCK1 --provider falcon` was run and FAILED.
  The Edison/falcon client could not authenticate: `HTTPStatusError: Client error
  '403 Forbidden' for url 'https://api.platform.edisonscientific.com/auth/login'`
  (a direct probe of the endpoint also returned HTTP 403 from the upstream server,
  not from the local proxy). No deep-research file was generated, and none has been
  written by hand. The review below is based on the UniProt record, the cached
  publications (mostly abstract-only), the cached Reactome entries, and the GO-CAM
  models that include PCK1.

## Identity and core biochemistry

- PCK1 = cytosolic phosphoenolpyruvate carboxykinase [GTP] (PEPCK-C), EC 4.1.1.32;
  catalyses GTP + oxaloacetate = PEP + GDP + CO2 (Rhea:10388). The mitochondrial
  paralog is PCK2 (PEPCK-M).
  [file:human/PCK1/PCK1-uniprot.txt "Cytosolic phosphoenolpyruvate carboxykinase that catalyzes the reversible decarboxylation and phosphorylation of oxaloacetate (OAA) and acts as the rate-limiting enzyme in gluconeogenesis"]
- First crystal structure of a GTP-dependent PEPCK (human PCK1); novel GTP-binding site
  with a phenylalanine-walled guanine pocket; Mn2+ cofactor (1 per subunit; monomer).
  [PMID:11851336 "These structures are the first to be determined for a GTP-dependent PEPCK, and provide the first view of a novel GTP-binding site unique to the GTP-dependent PEPCK family"]
  [file:human/PCK1/PCK1-uniprot.txt "Binds 1 Mn(2+) ion per subunit"]
- Reactome: PCK1 converts OA to PEP in the cytosol as part of gluconeogenesis.
  [Reactome:R-HSA-70241 "The transfer of a high-energy phosphate bond from GTP to oxaloacetate (OA), to form phosphoenolpyruvate (PEP), GDP, and CO2, is catalyzed by cytosolic phosphoenolpyruvate carboxykinase PCK1"]

## Cataplerosis / anaplerosis and regulation by acetylation

- Latorre-Muro et al. 2018: acetylation (p300; K91) toggles PCK1 from gluconeogenic
  (OAA->PEP) to anaplerotic (PEP->OAA) direction; SIRT1 deacetylation restores
  gluconeogenic direction; GSK3B-mediated phosphorylation affects acetylation and
  ubiquitination.
  [PMID:30193097 "Here, we describe that dynamic acetylation of PCK1 interconverts the enzyme between gluconeogenic and anaplerotic activities"]
  [PMID:30193097 "Under high glucose, p300-dependent hyperacetylation of PCK1 did not lead to protein degradation but instead increased the ability of PCK1 to perform the anaplerotic reaction, converting phosphoenolpyruvate to oxaloacetate"]
- GO:0072350 "tricarboxylic acid metabolic process" (IDA, this paper) is defined as
  metabolism of acids with three carboxyl groups; PCK1 substrates (OAA, a dicarboxylic
  acid; PEP) are not tricarboxylic acids. The curator's intent (TCA-cycle intermediate
  flux / cataplerosis-anaplerosis) is better captured by GO:0006107 oxaloacetate
  metabolic process, which PCK1 already carries.

## Human genetics

- Cytosolic PEPCK deficiency (PCKDC, MIM 261680): hypoglycemia, liver dysfunction,
  lactic acidosis, urinary TCA intermediates (fumarate).
  [PMID:26971250 "Whole exome sequencing revealed a homozygous 12-bp deletion in PCK1 (MIM 614168) encoding cytosolic phosphoenolpyruvate carboxykinase (PEPCK); enzymatic studies subsequently confirmed its pathogenic nature"]
  [PMID:28216384 "The COS-1 transfected cells showed the mutant gene to be incapable of producing a normally functioning cytosolic phosphoenolpyruvate carboxykinase (PEPCK) enzyme"]
  [PMID:24863970 "For kinetic analyses, WT and I45T PEPCK-C were assayed as previously described"]
- Promoter SNP -232C>G associated with T2D; reporter insensitive to insulin
  down-regulation. This is a cis-regulatory (promoter) observation, not a property of
  the protein.
  [PMID:14764811 "Thus, we report a promoter SNP in PCK1 that was resistant to down-regulation by insulin in vitro and was associated with type 2 DM in two independent study samples."]

## Moonlighting protein kinase activity (the key issue)

- Xu et al. 2020 (Nature), human HCC cells: AKT phosphorylates PCK1 Ser90; pS90-PCK1
  translocates to ER and uses GTP to phosphorylate INSIG1 Ser207 / INSIG2 Ser151; this
  reduces sterol binding by INSIGs and disrupts INSIG-SCAP interaction, releasing
  SCAP-SREBP to the Golgi and activating SREBPs and lipogenesis.
  [PMID:32322062 "Phosphorylated PCK1 translocates to the endoplasmic reticulum, where it uses GTP as a phosphate donor to phosphorylate INSIG1 at Ser207 and INSIG2 at Ser151"]
  [PMID:32322062 "This phosphorylation reduces the binding of sterols to INSIG1 and INSIG2 and disrupts the interaction between INSIG proteins and SCAP, leading to the translocation of the SCAP-SREBP complex to the Golgi apparatus"]
- Cached copy is abstract-only (content_type: abstract_only). The GOA IDA rows
  (GO:0106264, GO:0018105, GO:0046889, GO:0046890, GO:0005783, GO:0005829, GO:0004613,
  GO:0032869) were made by a curator who read the full text, so they are not removed.
- Only independent follow-up found: Ma et al. 2024, PRRSV infection of MARC-145 (monkey
  kidney) cells; AKT->PCK1->INSIG->SREBP axis invoked, INSIG phosphorylation reported to
  cause INSIG degradation. Not an independent biochemical reconstitution with purified
  PCK1.
  [PMID:39433189 "Activated PCK1 then phosphorylated insulin-induced genes (INSIGs), resulting in their degradation."]
- Assessment: the protein-kinase activity is a single-lab, cancer-cell-line finding, not
  reconstituted independently and not separated from PEPCK catalysis by a kinase-dead /
  PEPCK-competent mutant pair in another lab. It is kept, but as non-core.
- Direction of effect: PCK1 opposes SREBP-SCAP retention in the ER. GO-CAM
  gomodel:6205c24300000880 models PCK1 GO:0106264 part_of GO:0046889 with a negative
  causal edge onto INSIG activities that are part_of GO:0036316 (SREBP-SCAP complex
  retention in ER). The export produced acts_upstream_of_or_within GO:0036316 for PCK1,
  which was ISO-transferred to mouse Pck1 (genes/mouse/Pck1, GO_REF:0000119, with
  UniProtKB:P35558). That is an over-annotation (PCK1 is not part of the retention
  machinery; its reported effect is the opposite sign). Human PCK1 has no GO:0036316
  row and none is proposed here.

## Other localisation / process notes

- PCK1 is the cytosolic isozyme; no mitochondrial targeting. The IBA "is_active_in
  mitochondrion" (PTN000169230, donors PCK2 human/mouse) reflects the PCK2 branch.
- Glyceroneogenesis in adipose/liver (rat Pck1 evidence) generates glycerol-3-phosphate
  rather than free glycerol. GO nevertheless made GO:0006114 glycerol biosynthetic process
  the replacement for the obsolete GO:0046327 (exact synonym "glyceroneogenesis"), so
  GO:0006114 is accepted, not re-termed to GO:0046167. GO:0046166
  glyceraldehyde-3-phosphate biosynthetic process is also accepted, matching the mouse
  Pck1 review (IMP row, plus GO-CAM gomodel:6494e2e900002018). Reconciled 2026-10-16 when
  both species were reviewed together.
- Memory CD8+ T cell role (mouse, By similarity in UniProt): PCK1-derived PEP feeds
  glycogen and the pentose phosphate pathway. This is a metabolic requirement rather
  than a regulatory role in differentiation.
  [file:human/PCK1/PCK1-uniprot.txt "The resultant phosphoenolpyruvate flows to glycogen and pentose phosphate pathway, which is essential for memory CD8(+) T-cells homeostasis"]
