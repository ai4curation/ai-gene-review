# SGMS2 (human) — gene review notes

UniProt: Q8NHU3 (SMS2_HUMAN). Gene: SGMS2 (HGNC:28395). 365 aa multi-pass membrane protein.
RecName: Phosphatidylcholine:ceramide cholinephosphotransferase 2; AltName: Sphingomyelin synthase 2 (SMS2). EC 2.7.8.27.

## Core biology

SGMS2 is one of the two mammalian sphingomyelin synthases (paralog of SGMS1). It catalyzes the
transfer of the phosphocholine head group from **phosphatidylcholine (PC)** onto **ceramide**, producing
**sphingomyelin (SM)** and **diacylglycerol (DAG)** as by-product (EC 2.7.8.27). This is the terminal
step of de novo SM biosynthesis.

- "SM synthesis is mediated by a phosphatidylcholine:ceramide cholinephosphotransferase, or SM synthase,
  which transfers the phosphorylcholine moiety from phosphatidylcholine (PC) onto the primary hydroxyl of
  ceramide, thus generating SM and diacylglycerol (DAG)" [PMID:14685263].
- The enzyme is reversible: "the enzyme is also able to catalyse the reverse reaction, namely the
  formation of PC from SM and DAG ... it may regulate, in opposite directions, the cellular levels of the
  bioactive lipids ceramide and DAG" [PMID:14685263].
- Donor specificity: SGMS2 uses PC (not free phosphorylcholine or CDP-choline). Per UniProt FUNCTION,
  "Does not use free phosphorylcholine or CDP-choline as donors (PubMed:14685263)"
  [file:human/SGMS2/SGMS2-uniprot.txt].

**Localization.** SGMS2 is the paralog that acts mainly at the **plasma membrane** (SGMS1 at the Golgi):
"Whereas human SMS1 is localised to the Golgi, SMS2 resides primarily at the plasma membrane"
[PMID:14685263]. A small fraction is at the Golgi apparatus membrane. UniProt: "Primarily localized at
the plasma membrane with a small fraction at the Golgi apparatus" [file:human/SGMS2/SGMS2-uniprot.txt].
Plasma-membrane localization requires C-terminal palmitoylation (Cys-331/332/343/348)
[UniProt PTM; PMID:19233134 cited therein].

## Multiple in vitro activities (Sakane lab, 2024)

Purified human SMS2 in near-native (detergent-free proteoliposome) and micellar systems displays, besides
SM synthase (SMS) activity: **PC-specific phospholipase C (PC-PLC)**, PE-PLC, and **ceramide
phosphoethanolamine synthase (CPES)** activities — all D609- and Zn2+-sensitive, and all requiring the
His229/His272/Asp276 catalytic triad.

- "human SMS2, which is located in detergent-insoluble fractions of the plasma membrane, also possesses
  PC-PLC activity (approximately 41% of SMS activity), PE-PLC activity (approximately 4%), ceramide
  phosphoethanolamine synthase (CPES) activity (approximately 46%), and SMS activity" [PMID:39510177].
- "The catalytic triad (His229, His272, and Asp276) of SMS2 (Fig. S1) is crucial for all the
  DG-producing activities." [PMID:39510177].

The CPES (SM synthase → PE donor) activity was first shown by Ternes et al. 2009 (PubMed:19454763,
cited in UniProt): SMS2 displays dual activity as ceramide phosphoethanolamine synthase. UniProt CATALYTIC
ACTIVITY lists ceramide + PE → ceramide phosphoethanolamine (CPE) + DAG [file:human/SGMS2/SGMS2-uniprot.txt].

## Physiological roles

- **SM/DAG homeostasis at the plasma membrane / raft biology.** SGMS2 supplies plasma-membrane SM, a
  structural component of lipid rafts, and modulates the pro-apoptotic ceramide / mitogenic DAG balance.
  Overexpression and knockdown alter cellular SM, plasma-membrane SM, and DAG, affecting apoptosis
  [PMID:17982138]: "SMS1 and SMS2 are key factors in the control of SM and DAG levels within the cell and
  thus influence apoptosis." Pathway = sphingolipid metabolism (UniProt PATHWAY, PubMed:17982138).
- **Bone mineralization / skeletal homeostasis.** Heterozygous SGMS2 variants cause childhood-onset
  osteoporosis and calvarial doughnut lesions (CDL, MIM:126550) and, more severely, spondylometaphyseal
  dysplasia (CDLSMD). "we identified a heterozygous variant in SGMS2, a gene prominently expressed in
  cortical bone and encoding the plasma membrane-resident sphingomyelin synthase SMS2" [PMID:30779713].
  "Bone biopsies showed markedly altered bone material characteristics, including defective bone
  mineralization." [PMID:30779713]. The p.Arg50* nonsense variant "yielded a catalytically inactive
  enzyme," while p.Ile62Ser / p.Met64Arg block ER export of a functional enzyme [PMID:30779713]. Supports
  GO:0030500 regulation of bone mineralization (IMP).
- **Secretory transport (minor).** Via regulation of the Golgi DAG pool and downstream PRKD1 (UniProt
  FUNCTION, PubMed:18370930, PubMed:21980337) — non-core.

## Disease

Calvarial doughnut lesions with bone fragility (CDL, MIM:126550) and CDL + spondylometaphyseal dysplasia
(CDLSMD, MIM:126550), autosomal dominant [UniProt DISEASE; PMID:30779713].

## Reactome

- R-HSA-429786 "SGMS2 transfers phosphocholine onto ceramide" — the SM synthase reaction, PM-associated.
- R-HSA-1660661 "Sphingolipid de novo biosynthesis" — parent pathway.

## Annotation-review reasoning summary

- **Core MF:** GO:0033188 sphingomyelin synthase activity (verified current label via OLS; def = PC +
  ceramide → DAG + SM). Multiple experimental (IDA) sources: PMID:14685263, PMID:17982138, PMID:30779713,
  PMID:39510177. ACCEPT.
- **Core BP:** GO:0006686 sphingomyelin biosynthetic process (IDA PMID:14685263, PMID:17982138). ACCEPT.
- **Secondary MF:** GO:0034480 phosphatidylcholine phospholipase C activity (IDA PMID:39510177) — real in
  vitro activity, PC-PLC ~41% of SMS activity; KEEP_AS_NON_CORE. GO:0002950 ceramide phosphoethanolamine
  synthase activity (IDA PMID:39510177; IBA) — real dual activity; KEEP_AS_NON_CORE.
- **GO:0047493 ceramide cholinephosphotransferase activity** (IBA + IDA PMID:14685263): the GO def is the
  **CDP-choline** route (CDP-choline + ceramide → SM), but SGMS2 explicitly does NOT use CDP-choline; its
  donor is PC. This is a mislabel of the true PC-dependent SM synthase reaction → **MODIFY** to GO:0033188.
- **GO:0046513 ceramide biosynthetic process** (IBA): forward physiological direction consumes ceramide;
  ceramide is produced only by the reverse reaction. Phylogenetic over-inference → MARK_AS_OVER_ANNOTATED.
- **GO:0016780 phosphotransferase activity, for other substituted phosphate groups** (IEA/InterPro): the
  correct grandparent of SM synthase activity but far too general → MODIFY to GO:0033188.
- **GO:0005515 protein binding** (IPI, PMID:32296183, HuRI binary interactome; interactor ZFPL1/O95159 and
  others): high-throughput Y2H, bare "protein binding", uninformative → MARK_AS_OVER_ANNOTATED.
- **Locations:** GO:0005886 plasma membrane (primary, IDA/IBA) ACCEPT; GO:0000139 Golgi membrane and
  GO:0005794 Golgi apparatus (minor pool, IDA/IBA) KEEP_AS_NON_CORE; GO:0005789 ER membrane (IBA only,
  no experimental support for WT active enzyme in ER — mutants accumulate in ER) MARK_AS_OVER_ANNOTATED.
- **GO:0030500 regulation of bone mineralization** (IMP, PMID:30779713): well supported disease/functional
  study; KEEP_AS_NON_CORE (downstream physiological role, not molecular core).
- **GO:0030148 sphingolipid biosynthetic process** (TAS Reactome): correct parent BP; KEEP_AS_NON_CORE
  (GO:0006686 is the more precise term).
