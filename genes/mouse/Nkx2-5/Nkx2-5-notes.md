# Nkx2-5 (mouse, P42582, NKX25_MOUSE) — curation notes

## Provenance note

Automated deep research could not be run for this gene (falcon provider returned
HTTP 402, OpenAI provider returned HTTP 401). No `-deep-research-<provider>.md`
file exists. These notes were assembled manually from the cached publications in
`publications/` (most are abstract-only; full text available for PMIDs 11390666,
17350578, 18689573, 18722343, 19035347, 19166829, 19479054, 19546853, 19578358,
21379568, 21640717, 21931855, 22192413, 22560297, 23028370) and the UniProt record
`Nkx2-5-uniprot.txt`.

## Identity and domain architecture

- NK-2 class homeodomain transcription factor (also called Csx / Csx1), vertebrate
  ortholog of Drosophila *tinman*; belongs to PANTHER PTHR24340:SF28 (HOMEOBOX PROTEIN
  NKX-2.5) per UniProt cross-reference.
- Homeodomain binds NK2 elements (NKEs; e.g. TNAAGTG/TCCACTTTCC-type sites) in target
  promoters/enhancers; additional conserved motifs include the TN domain, the NK2-specific
  domain and a tyrosine-rich domain (YRD) required in vivo
  [PMID:16510504 "the YRD was absolutely essential for the function of Nkx2-5 in cardiogenesis during ES cell differentiation and in the developing embryo"].
- Binds DNA as monomer and homodimer
  [PMID:11042197 "the HD of Csx/Nkx2.5 binds as a monomer as well as a dimer to its DNA binding sites in the promoter of the atrial natriuretic factor (ANF) gene"].
- Nuclear; SUMOylation enhances activity
  [PMID:21931855 "we confirm that SUMOylation strongly enhances Nkx2-5 transcriptional activity"].

## Molecular function: cardiac transcription factor, activator and repressor

- Activator of cardiac structural/regulatory genes (Nppa/ANF, cardiac alpha-actin,
  Cx40, myocardin, Mef2c, Id2, miR-143/145), usually in combination with partner TFs:
  - GATA4 [PMID:9584153 "Coexpression of Csx and GATA4 synergistically activates ANF reporter gene expression"]
  - SRF [PMID:8887666 "SRF recruited Nkx-2.5 to the alpha-actin promoter"]
  - TBX5 [PMID:11572777 "Direct and cooperative transactivation of the ANF and cx40 promoters by Tbx5 and the homeodomain transcription factor Nkx2-5 was also demonstrated"]
  - TBX20 [PMID:14550786 "Tbx20 physically interacted with cardiac transcription factors Nkx2-5, GATA4, and GATA5, collaborating to synergistically activate cardiac gene expression"]
  - MEF2C [PMID:19035347 "Co-immunoprecipitation and mammalian two-hybrid experiments revealed a direct molecular interaction between Nkx2.5 and Mef2c"]
  - HAND2 [PMID:12392994 "HAND2 and the homeobox factor Nkx2.5 exhibit transcriptional synergy in the regulation of ANP"]
  - FOXH1 [PMID:15363409 "Mef2c is a direct target of Foxh1, which physically and functionally interacts with Nkx2-5 to mediate strong Smad-dependent activation of a TGFbeta response element in the Mef2c gene"]
  - Direct targets: myocardin [PMID:14645532 "Transient-cotransfection analysis showed that Nkx2.5 transactivates the myocardin promoter"]; miR-143/145 [PMID:19578358 "miR-145 and miR-143 were direct transcriptional targets of serum response factor, myocardin and Nkx2-5"]; Id2 [PMID:17604724 "A 1.2 kb fragment of the Id2 promoter proved sufficient for cooperative regulation by Nkx2-5 and Tbx5 in vitro"].
- Repressor functions (context-dependent): with TBX2 represses Nppa in the AV canal
  [PMID:12023302 "Tbx2 formed a complex with Nkx2.5 on the ANF TBE-NKE, and was able to repress ANF promoter activity"];
  represses the pacemaker program (Hcn4, Tbx3) at the atrium/SAN border
  [PMID:17234970 "Nkx2-5 suppresses pacemaker channel gene Hcn4 and T-box transcription factor gene Tbx3"];
  feedback repression of Bmp2/Smad1 in the second heart field
  [PMID:17350578 "feedback repression of Bmp2/Smad1 signaling by Nkx2-5 critically regulates SHF proliferation and outflow tract (OFT) morphology"].
- Coregulators: HIPK corepressors [PMID:9748262 "HIPKs localize to nuclear speckles and potentiate the repressor activities of NK homeoproteins"];
  JARID2/JMJ [PMID:15542826 "JMJ represses ANF gene expression by inhibiting transcriptional activities of Nkx2.5 and GATA4"];
  CAMTA2 coactivator [PMID:16678093 "activates the ANF gene, at least in part, by associating with the cardiac homeodomain protein Nkx2-5"];
  WHSC1/NSD2 H3K36 methyltransferase [PMID:19483677 "Nkx2-5 in embryonic hearts, regulating the expression of their target genes"];
  UTX/UTY [PMID:22192413 "UTX is recruited to cardiac-specific enhancers by associating with core cardiac transcription factors"].
- Genome-wide binding in cardiomyocytes [PMID:21379568 "We present a systems biology study integrating mRNA profiles with DNA-binding events of key cardiac transcription factors (Gata4, Mef2a, Nkx2.5, and Srf)"].

## Biological roles (mouse genetics)

- Null embryos: heart tube forms but looping is not initiated, death ~E9-10, loss of
  Mlc2v (ventricular differentiation marker)
  [PMID:7628699 "looping morphogenesis, a critical determinant of heart form, was not initiated at the linear heart tube stage"]
  [PMID:7628699 "the myosin light-chain 2V gene (MLC2V) was not expressed in mutant hearts"];
  commitment to cardiac lineage itself is not lost
  [PMID:7628699 "Commitment to the cardiac muscle lineage, expression of most myofilament genes and myofibrillogenesis were not compromised"].
- Required for later cardiomyocyte differentiation (ES chimeras)
  [PMID:10021345 "Csx/Nkx2.5 is required for later differentiation of cardiac myocytes"].
- Yolk sac vascular and hematopoietic defects in nulls
  [PMID:10021345 "Moreover, there were severe defects in vascular formation and hematopoiesis in the mutant yolk sac"]
  — most likely secondary to cardiac failure (Nkx2-5 is not a yolk sac vascular/blood regulator).
- Ventricle formation with Hand2 and Mef2c (double mutants lack ventricle)
  [PMID:11784028 "Complete ventricular dysgenesis was observed in Nkx2.5(-/-)dHAND(-/-) mutants"]
  [PMID:19035347 "ventricular hypoplasia is the result of defective ventricular cell differentiation"].
- Second heart field: Nkx2-5/Bmp2/Smad1 negative feedback
  [PMID:17350578 "Smad1 deletion in Nkx2-5 mutants rescued SHF proliferation and OFT development"].
- Left/right asymmetric eHand expression
  [PMID:9192865 "In hearts of embryos lacking the homeobox gene Nkx2-5, which do not loop, left-sided eHand expression was abolished"].
- Conduction system: dosage-dependent; AV node primordium absent in nulls; Purkinje
  fibre formation requires Nkx2-5 cell-autonomously; Tbx5/Nkx2-5/Id2 pathway
  [PMID:15085192 "We show in KO mice that the number of cells in the cardiac conduction system is directly related to Nkx2-5 gene dosage"]
  [PMID:17250822 "the formation of the peripheral conduction system is time- and dose-dependent on the transcription factor Nkx2.5 that is cell-autonomously required for the postnatal differentiation of Purkinje fibers"]
  [PMID:17604724 "compound haploinsufficiency of Tbx5 and Nkx2-5 or Tbx5 and Id2 prevented embryonic specification of the ventricular conduction system"].
- Ventricular-restricted KO: AV block, trabecular overgrowth (Bmp10)
  [PMID:15109497 "At birth, mutant mice display a hypoplastic atrioventricular (AV) node and then develop selective dropout of these conduction cells"].
- Perinatal/postnatal requirement: Scn5a (Nav1.5), Ryr2 expression, conduction and
  contraction [PMID:18689573 "Nkx2-5 function is critical not only during cardiac development but also in perinatal hearts, by regulating expression of several important gene products involved in conduction and contraction"]
  [PMID:19546853 "Nkx2-5 is necessary for proper conduction and contraction after 2 weeks of age"].
- Adult cardiomyocyte survival [PMID:11889119 "expression of wild type Csx/Nkx2-5 protected cardiomyocytes from doxorubicin-induced apoptotic death"].
- SAN: Nkx2-5 must be excluded from SAN (Shox2 represses it)
  [PMID:21640717 "tissue specific overexpression of Nkx2.5 in the heart leads to severe hypoplasia of the SAN and the venous valves"].
- Pulmonary myocardium identity [PMID:17823370 "When Nkx2-5 protein level was lowered in a hypomorphic model, the pulmonary myocardium switched to a Cx40-negative, Hcn4-positive phenotype"].
- Proepicardium [PMID:18722343 "Nkx2-5 knockout resulted in abnormal proepicardial development and decreased expression of Wt1"].
- Cardiomyocyte proliferation [PMID:20713518 "transgenic overexpression of Nkx2.5 leads to increased cardiomyocyte proliferation and increased ventricular mass"].

## Extracardiac roles

- Spleen (Pbx1/Nkx2-5/p15 module; Nkx2-5 marks splenic mesenchymal progenitors; Tlx1
  is a parallel spleen regulator)
  [PMID:22560297 "This study establishes that a Pbx/Nkx2-5/p15 regulatory module is essential for spleen development"].
- Pharynx (redundant with Nkx2-6)
  [PMID:11390666 "These results demonstrated a critical role of the NK-2 homeobox genes in the differentiation, proliferation, and survival of pharyngeal endodermal cells"].
- Thyroid bud [PMID:16418214 "Our results indicate that Nkx2-5(-/-) embryos exhibit thyroid bud hypoplasia, providing evidence that NKX2-5 plays a role in thyroid organogenesis"].
- Overexpression in C2C12 myoblasts inhibits myotube formation and induces neuron-like
  cells [PMID:15653675 "overexpression of NKX2.5 in C2C12 cells and primary cultures of human fetal myoblasts led to differentiation of myoblasts into neuron-like cells"]
  — artificial gain-of-function, not a physiological role.

## Curation decisions summary

- Core: sequence-specific RNA pol II TF activity (GO:0000981 / GO:0000978), positive and
  negative regulation of Pol II transcription, nucleus; heart development (looping,
  ventricle formation, cardiomyocyte differentiation, conduction system) and spleen development.
- Generic terms (DNA binding, sequence-specific DNA binding, chromatin binding,
  GO:0003700, GO:0001216, positive regulation of DNA-templated transcription) modified to
  the Pol II-specific children.
- `protein binding` IPI rows modified to TF binding (GO:0061629) or coregulator binding
  (GO:0001221/GO:0001222/GO:0001223) depending on the partner.
- Marked as over-annotated: vasculogenesis, hemopoiesis (yolk sac secondary to heart
  failure), apoptotic process involved in heart morphogenesis, tongue development (expression
  only), skeletal myotube/neuron differentiation (C2C12 overexpression), positive regulation of
  sodium ion transport and negative regulation of canonical Wnt signaling (indirect expression
  effects), cytosol, protein-containing complex, tissue development.
- No GO-CAM model in `gocams/index.tsv` includes Nkx2-5 (P42582).
