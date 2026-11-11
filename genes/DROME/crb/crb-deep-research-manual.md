# crb (Crumbs, P10040) - manual literature synthesis

No deep-research API was available for this session; this summary was compiled by hand from
the cached publications in `publications/` and the UniProt record `crb-uniprot.txt`.

## Identity and structure

- Drosophila melanogaster crumbs (FlyBase FBgn0259685, GeneID 42896), UniProt P10040, 2146 aa,
  single-pass type I transmembrane protein. Large extracellular domain with ~30 EGF-like repeats
  (several calcium-binding) and laminin G-like domains; a 37-aa cytoplasmic tail with a
  juxtamembrane FERM-binding motif (FBM) and a C-terminal PDZ-binding motif (ERLI)
  [PMID:2344615 "encodes an integral membrane protein with 30 EGF-like repeats in the extracellular part"].

## Localization

- Apical plasma membrane of ectodermal epithelia [PMID:2344615 "The protein is exclusively localized on the apical membranes of epithelial cells and concentrated at the borders between cells"].
- Follicle cells: apical membrane facing the germline [PMID:11076972 "Crb localizes to the apical membrane of follicle cells that is in contact with germline cells"].
- Subapical region / marginal zone, apical to the zonula adherens, as the core of the subapical complex (SAC)
  [PMID:11740560 "A core component of the SAC is the transmembrane protein Crumbs"].
- Photoreceptors: stalk membrane (the apical membrane between the zonula adherens and the rhabdomere), with residual
  rhabdomere staining [PMID:32579558 "Crumbs was concentrated to the stalk membrane with some Crumbs residual staining in the rhabdomere"];
  [PMID:22105348 "Crb still localizes to the stalk membrane in MyoV mutant tissue"]. Drosophila photoreceptors are not ciliated, so the
  stalk is not a "photoreceptor connecting cilium" even though it is analogous to the vertebrate inner segment
  [PMID:11850625 "Crumbs and CRB1 localize to corresponding subdomains of the photoreceptor apical plasma membrane: the stalk of the Drosophila photoreceptor and the inner segment of mammalian photoreceptors"].
- Early embryo: overlap with mitotic spindle microtubules [PMID:25065591 "Both Galla-1 and Crb proteins show overlapping localization with spindle microtubules during nuclear division"].

## Molecular interactions (the core mechanism)

- PDZ-binding motif binds Stardust (Sdt, PALS1 orthologue), which recruits Patj and Lin-7: the Crb-Sdt-Patj subapical complex
  [PMID:11740560 "Stardust proteins colocalize with Crumbs and bind to the carboxy-terminal amino acids of its cytoplasmic tail"];
  [PMID:11740559 "Stardust and Crumbs are mutually dependent in their stability, localization and function"];
  [PMID:18177979 "Drosophila Lin-7 ... is associated with the Crumbs complex"].
- aPKC binds and phosphorylates the Crb tail [PMID:15302858 "via direct binding of DaPKC to both Crb and Patj, and identify Crumbs as a phosphorylation target of DaPKC"].
- FBM links Crb to Moesin and beta-Heavy spectrin [PMID:12500938 "Crumbs interacts with the cortical cytoskeleton made of DMoesin and beta heavy-Spectrin"].
- FBM directly binds the FERM protein Expanded, recruiting it apically, which promotes Hippo signalling
  [PMID:20498073 "Crb directly binds to Ex through its juxtamembrane FERM-binding motif (FBM)"];
  [PMID:20362445 "These studies identify Crb as a novel SWH regulator via JM-dependent effects on Ex levels and localization"];
  Crb also promotes SCF-Slimb-mediated Ex degradation [PMID:24778256 "Crb promotes phosphorylation-dependent ubiquitin-mediated degradation of Ex"]
  and can sequester Kibra [PMID:28292426 "Crumbs promotes the ability of Expanded to activate the pathway but also sequesters Kibra"].
- Crb-Crb extracellular homophilic interactions drive self-recruitment [PMID:22658591 "Crb self-recruits via Crb-Crb extracellular domain interactions"].
- Myosin V co-IPs with the Crb complex; Crb stabilizes MyoV against proteasomal degradation and is required for Rh1 transport
  [PMID:22105348 "myosin V (MyoV) coimmunoprecipitated with the Crb complex and that loss of crb led to severe reduction in MyoV levels, which could be rescued by proteasomal inhibition"].
- Apnoia binds Crb in trachea [PMID:30645584 "Apn physically interacts with Crb to control its localization and maintenance at the apical membrane of developing airways"].
- Galla-1/2 and Xpd (CGX complex) [PMID:25065591 "Galla-1 physically interacts with the intracellular domain of Crb"].

## Biological roles

- Epithelial apical-basal polarity and zonula adherens assembly/maintenance, particularly during tissue remodelling
  [PMID:11740560 "Cells lacking crumbs or the functionally related gene stardust fail to organize a continuous ZA and to maintain cell polarity"];
  [PMID:19567473 "Crumbs has a specific, conserved function in stabilising cell polarity during tissue remodelling"].
- Apical membrane growth: salivary gland, trachea [PMID:12526813 "crb and klar mediate growth and delivery of apical membrane"];
  [PMID:30645584 "RNAi-mediated knockdown of Crb results in decreased apical surface growth of tracheal cells"].
- Photoreceptor morphogenesis (stalk, AJ positioning, rhabdomere elongation) and protection from light-induced degeneration
  [PMID:11850625 "Drosophila Crumbs is required to maintain zonula adherens integrity during the rapid apical membrane expansion that builds the rhabdomere"];
  [PMID:12361571 "mutations in Drosophila crumbs result in progressive, light-induced retinal degeneration"].
- Growth control via Hippo signalling [PMID:20498073 "Loss of Crb leads to tissue overgrowth and target gene expression characteristic of defective Hippo signaling"].
- Limits Notch signalling [PMID:16440003 "Crumbs reduces the activity of the gamma-Secretase complex"]; [PMID:20110329 "a novel function for Crb in limiting ligand-dependent transactivation of the N receptor"].
- Actomyosin regulation in amnioserosa during dorsal closure [PMID:26544546 "a novel role of Crumbs as a negative regulator of actomyosin dynamics during dorsal closure"].
