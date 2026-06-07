# CSNK1D (Casein kinase I isoform delta, CK1δ) review notes

UniProt: P48730 (KC1D_HUMAN). 415 aa. EC 2.7.11.1 (protein Ser/Thr kinase) and EC 2.7.11.26 (tau-protein kinase). HGNC: CSNK1D. Chr 17q25.3.

## Summary of biology

CK1δ is a constitutively active, monomeric (PubMed:22168824, PubMed:23106386) serine/threonine
protein kinase of the casein kinase 1 (CK1) family. It uses ATP and is magnesium-dependent
(catalytic mechanism shared by the CK1 family). It is a "casein kinase" operationally defined by
preferential phosphorylation of acidic substrates, and characteristically performs both primed
(phospho-directed) and unprimed phosphorylation. Activity is autoinhibited by C-terminal
autophosphorylation (a "futile cycle") and reactivated by phosphatases (PP1) [UniProt PTM;
PMID:9632646].

### Core molecular function
- **Protein-serine/threonine kinase activity (ATP binding)**. Directly demonstrated in vitro for
  many substrates [PMID:10606744 p53/TP53 Thr18; PMID:20041275 p53 S20; PMID:12270943 connexin-43/GJA1;
  PMID:14761950 + PMID:17562708 MAPT/tau; PMID:19043076 TOP2A Ser-1106; PMID:20637175 DCK Ser-74;
  PMID:20699359 HIF-1α Ser247; PMID:21084295 eIF6 Ser174/175; PMID:21422228 DVL2/DVL3;
  PMID:17962809 PKD2 Ser244; PMID:20048001 YAP1 phosphodegron; PMID:23636092 PER2 peptide]. This is
  the unambiguous core function and is supported by EXP/IDA evidence and abundant structural data
  (>30 PDB entries).
- Tau-protein kinase activity (GO:0050321) is a valid, more specific MF directly shown
  [PMID:14761950 "Casein kinase 1 delta phosphorylates tau"; PMID:17562708 novel tau sites].

### Core biological processes
- **Circadian rhythm / regulation of circadian rhythm (GO:0042752; GO:0032922 circadian regulation
  of gene expression)**. CK1δ phosphorylates PER1/PER2, controlling their stability, nuclear entry
  and thus the clock period. FASPS2 (familial advanced sleep phase) and familial migraine are caused
  by CSNK1D missense variants (T44A, H46R) that reduce kinase activity [PMID:23636092; PMID:15800623].
  This is a hallmark, well-established physiological role. Interacts directly with PER1/PER2
  [PubMed:11165242].
- **Wnt signaling (regulation of Wnt signaling pathway; canonical Wnt)**. CK1δ phosphorylates DVL2/DVL3
  to mediate Wnt-3a-dependent neurite outgrowth [PMID:21422228]. Hippo-Wnt crosstalk: TAZ inhibits
  CK1δ/ε-mediated DVL phosphorylation [PMID:20412773 — note this is a Hippo→Wnt paper where CK1δ acts
  on DVL]. CK1 family broadly phosphorylates LRP6, APC, β-catenin in canonical Wnt (family-level,
  largely from orthologs/IBA).
- **Centrosome / ciliogenesis / Golgi / microtubules**. CK1δ localizes to the centrosome (anchored via
  AKAP9/AKAP450 [PubMed:12270714]) and Golgi; required for primary (non-motile) ciliogenesis, Golgi-derived
  microtubule nucleation and Golgi organization [PMID:24648492 IMP for GO:0007020 microtubule nucleation,
  GO:0034067 protein localization to Golgi, GO:0007030 Golgi organization, GO:0061512 protein localization
  to cilium, GO:0071539 protein localization to centrosome, GO:1905515 non-motile cilium assembly].
  Localizes to spindle/spindle microtubules upon DNA damage; involved in mitotic spindle formation in
  trophoblasts [PMID:10826492; PMID:16027726].

### Substrate-driven roles (real but mostly non-core / downstream of kinase activity)
Many BP annotations are transferred from individual substrate phosphorylation events:
- p53/MDM2: phosphorylates p53 Thr18/S20 and promotes MDM2 turnover via SCF(β-TRCP) [PMID:10606744;
  PMID:20041275; PMID:20708156]. Linked to GO:0032436 positive regulation of proteasomal ubiquitin-
  dependent protein catabolic process (YAP1, MDM2 degron priming).
- HIF-1α regulation [PMID:20699359]; TOP2A/DNA cleavage [PMID:19043076]; DCK activation (in vitro only,
  CAUTION: probably not in vivo per UniProt) [PMID:20637175]; eIF6 nucleo-cytoplasmic shuttling
  [PMID:21084295]; PKD2 nuclear localization [PMID:17962809]; YAP1 stability/Hippo [PMID:20048001];
  connexin-43 gap junction assembly [PMID:12270943].

### Subcellular location
Cytoplasm, nucleus, centrosome (MOC), perinuclear region, cell/plasma membrane, spindle/spindle
microtubule, Golgi apparatus, cytosol, ciliary basal body (GO:0036064 IDA PMID:29257953), ERGIC
membrane (Reactome). Correct localization requires kinase activity [PubMed:11161704].

## Annotation-review reasoning highlights

- **protein binding (GO:0005515, IPI x many)**: bare "protein binding" is uninformative →
  MARK_AS_OVER_ANNOTATED. Several partners are biologically meaningful (PER2 O15055; DVL3/Q92997;
  MDM2 Q00987; YWHAE/14-3-3ε P62258) but the term itself conveys no function. Real binding functions
  (PER, DVL) are captured better elsewhere via the kinase/circadian/Wnt annotations.
- **cadherin binding (GO:0045296, HDA PMID:25468996)**: high-throughput E-cadherin interactome
  proximity dataset; CK1δ is not an established cadherin-binding adaptor → MARK_AS_OVER_ANNOTATED.
- **Many GO:0005829 cytosol TAS Reactome** annotations point at numerous centrosome/ciliogenesis
  reactions; cytosol localization is correct but each is a separate Reactome reaction citation →
  ACCEPT location (cytosol is a true location) but redundant; keep representative as ACCEPT.
- **COPII vesicle coat assembly (GO:0048208 TAS Reactome R-HSA-204005) / CSNK1D phosphorylates SEC23
  (R-HSA-5694441)**: CK1δ phosphorylates SEC23A in COPII vesicle formation (Reactome). Real but a
  narrow substrate-driven role → KEEP_AS_NON_CORE.
- **endocytosis (GO:0006897 IBA)**: transferred from yeast CK1 orthologs (Yck1/Yck2, SGD) — these
  yeast paralogs regulate endocytosis, but human CK1δ has no direct experimental support for endocytosis
  → MARK_AS_OVER_ANNOTATED (over-transfer from distant paralogs).
- **midbrain dopaminergic neuron differentiation (GO:1904948 ISS) / positive regulation of non-canonical
  Wnt (GO:2000052 ISS)**: ISS from mouse ortholog Q9DC28 (ParkinsonsUK-UCL). Plausible developmental/
  pleiotropic roles but not core → KEEP_AS_NON_CORE.
- **DCK** (PMID:20637175): UniProt CAUTION says in vitro only, probably not in vivo. Still supports the
  MF (protein serine kinase activity) since phosphorylation was directly demonstrated → ACCEPT for MF.

## Provenance for key claims
- Monomer, constitutively active: PubMed:22168824, PubMed:23106386; UniProt SUBUNIT.
- FASPS2 disease & migraine, reduced kinase activity of T44A/H46R: [PMID:23636092 "Casein kinase iδ
  mutations in familial migraine and advanced sleep phase"], [PMID:15800623 FASPS2 A44].
- Autoinhibition by autophosphorylation: UniProt PTM; PMID:9632646.
- Ciliogenesis mechanism: [PMID:24648492 "CK1δ was required for microtubule nucleation at the Golgi and
  maintenance of Golgi integrity ... mediates primary ciliogenesis by multiple mechanisms"].

## Caveat on PMID:25500533 (GO:0004674 IDA)
PMID:25500533 (Chia et al.) is primarily about **CK1α/CSNK1A1**, identified by a kinome siRNA screen as
the kinase responsible for constitutive LRRK2 phosphorylation at S910/S935. For CK1δ specifically, the
paper reports only that "CK1δ/ε and CK1γ isoforms could moderately phosphorylate S955 and S935 in vitro"
[PMID:25500533, Suppl. Fig. 5c,d]. So this paper does support that CK1δ has protein Ser/Thr kinase
activity in vitro, but the headline physiological LRRK2-Golgi finding is a CK1α function, not CK1δ. The
GO:0004674 IDA annotation on CSNK1D from this reference is therefore retained as ACCEPT for the generic
MF (it does show in-vitro Ser/Thr kinase activity of CK1δ) but is weak; the LRRK2-specific biology should
not be over-transferred to CK1δ.

## Reactome cytosol/centrosome reactions (GO:0005829 TAS x many)
The ~25 GO:0005829 cytosol TAS annotations each cite a distinct Reactome reaction (centrosome maturation,
ciliogenesis, rRNA processing, AURKA/PLK1 cascades). Cytosol is a genuine CK1δ location, so the location
term is correct, but the long list is redundant Reactome pathway-membership inflation. Keep one
representative as ACCEPT (core cytosolic kinase); mark the remainder ACCEPT as well since the CC term
itself is not wrong (they differ only by reference, not by term).
