---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANLN
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q9NQW6
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 41
citation_count: 41
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ANLN (human)

## Current model (mechanistic narrative)

Anillin (ANLN) is a multidomain scaffold protein that organizes the actomyosin cytokinetic contractile ring by physically coupling its core components and linking them to the underlying membrane and spindle [PMID:7559773, PMID:15496454, PMID:18158243]. Its N-terminal actin-binding domain contains three distinct actin-binding sites that crosslink filaments into parallel and antiparallel bundles, and these crosslinking activities allow anillin to autonomously generate tens-of-picoNewton contractile forces and drive ring constriction even in the absence of myosin II [PMID:28147230, PMID:34321459]. Anillin directly binds nonmuscle myosin II in a light-chain phosphorylation-dependent manner and is required for the spatial regulation of myosin contraction and successful abscission [PMID:15496454]. Membrane anchorage and equatorial targeting are achieved through a C-terminal module of three synergistic membrane-associating elements—a cryptic C2 domain, a Rhotekin-homologous Rho-binding domain, and a PH domain—that together engage GTP-RhoA and phospholipids, with the PH domain binding PI(4,5)P2 and recruiting septins to the furrow [PMID:18158243, PMID:22197245, PMID:25959226]. Through these interactions anillin acts as a kinetic scaffold that concentrates PI(4,5)P2 and prolongs the membrane dwell time of GTP-RhoA to amplify RhoA effector recruitment [PMID:31105010]. Anillin further bridges the spindle and the cortex by interacting with centralspindlin component RacGAP, the RhoGEF Ect2, the formin mDia2, and microtubules, thereby positioning contractile-ring assembly relative to the central spindle [PMID:18158242, PMID:18349071, PMID:20660154, PMID:22514687, PMID:24994938]. Its activity is tightly cell-cycle controlled: APC/C-Cdh1 targets anillin for ubiquitin-mediated degradation, counterbalanced by USP10 deubiquitylation, and mitotic phosphorylation at S635 and importin-mediated conformational and localization control restrict its membrane function to mitosis [PMID:16040610, PMID:36526897, PMID:28081137, PMID:25829492, PMID:28931593]. Beyond division, anillin localizes to epithelial cell-cell junctions where it controls junctional RhoA-GTP dynamics, perijunctional actomyosin organization, and tissue mechanics, and it links RhoG signaling to F-actin stabilization during neuronal migration [PMID:24835458, PMID:25809162, PMID:30702429, PMID:25843030]. Mutations in ANLN (R431C, G618C) cause familial focal segmental glomerulosclerosis through disrupted CD2AP binding and aberrant podocyte signaling [PMID:24676636].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0008092 cytoskeletal protein binding, GO:0008289 lipid binding, GO:0005198 structural molecule activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005886 plasma membrane, GO:0005634 nucleus, GO:0005856 cytoskeleton, GO:0005815 microtubule organizing center
- **pathway (Reactome):** R-HSA-1640170 Cell Cycle, R-HSA-162582 Signal Transduction, R-HSA-1500931 Cell-Cell communication
- **partners:** RHOA, MYH9, RACGAP1, ECT2, DIAPH3, CD2AP, USP10, SEPT9
- **complexes:** actomyosin contractile ring, midbody ring, centralspindlin-associated cortical complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1995 | High | Anillin (Drosophila) directly binds actin filaments and bundles them through a defined 244-amino-acid domain; it localizes to the nucleus during interphase and becomes enriched in the cleavage furrow with myosin II during anaphase-telophase, suggesting a role in organizing/stabilizing contractile domains of the actin cytoskeleton. | PMID:7559773 | The Journal of cell biology |
| 2004 | High | Anillin directly interacts with nonmuscle myosin II, and this interaction is regulated by myosin light chain phosphorylation; depletion of anillin in Drosophila or human cells causes cytokinesis failure with loss of spatial regulation of myosin II contraction and failure of abscission. | PMID:15496454 | Molecular biology of the cell |
| 2005 | High | Anillin is a substrate of the APC/C ubiquitin ligase activated by Cdh1; anillin contains a destruction-box, is ubiquitinated in a Cdh1-dependent manner, and its levels peak in mitosis and drop during mitotic exit. APC/C-mediated degradation controls spatial contractility of myosin during late cytokinesis. | PMID:16040610 | The Journal of biological chemistry |
| 2005 | High | Drosophila anillin (encoded by the scraps gene) is required for septin recruitment to the furrow canal and contractile ring; PH domain mutations cause defects in septin localization, membrane stabilization, and cellularization; a more N-terminal mutation blocks pole cell separation. | PMID:15930114 | Development (Cambridge, England) |
| 2005 | Medium | Human ANLN interacts with RhoA and induces actin stress fibers; PI3K/AKT activity regulates ANLN stability and nuclear localization; siRNA knockdown of ANLN in NSCLC cells causes multinucleation and cell death. | PMID:16357138 | Cancer research |
| 2007 | High | Human anillin contains a conserved C-terminal domain homologous to the RhoA-binding protein Rhotekin that directly interacts with RhoA; anillin functions as a scaffold linking RhoA to actin and myosin at the equatorial cortex; furrows can initiate without anillin but require anillin when the central spindle is also disrupted. | PMID:18158243 | Current biology : CB |
| 2007 | High | Anillin and septins promote asymmetric furrow ingression in C. elegans; anillin and septins promote coalescence of contractile ring components on one side of the ring, and disruption of this asymmetry makes cytokinesis sensitive to partial contractility inhibition. | PMID:17488632 | Developmental cell |
| 2007 | High | Drosophila RacGAP50C directly interacts with Anillin; both proteins depend on this interaction for their localization; in the absence of anillin, spindle-associated RacGAP50C loses equatorial cortex association and cytokinesis fails, establishing a direct molecular link between spindle microtubules and the actomyosin contractile ring. | PMID:18158242 | Current biology : CB |
| 2008 | High | Affinity-purification/MS of Anillin interactors in Drosophila cells identified actin, myosin, three septins, and RacGAP50C (Tum); F-actin is essential for cortical Anillin localization in prometaphase but not for furrow accumulation; septins travel along microtubules to interact with Anillin at the furrow; RacGAP50C is necessary for Anillin accumulation at the furrow and the two proteins interact in vitro. | PMID:18349071 | Journal of cell science |
| 2008 | High | Ran regulates anillin-dependent targeting of the septin Peanut to pseudocleavage furrows in Drosophila; importin-α and importin-β directly bind anillin and prevent its interaction with Peanut; RanGTP reverses this inhibition; a mutant anillin lacking the importin binding site renders furrow ingression insensitive to Ran pathway disruption. | PMID:18579688 | Molecular biology of the cell |
| 2010 | Medium | mDia2 interacts with anillin via its diaphanous-inhibitory domain (DID); anillin binding is competitive with the diaphanous autoregulatory domain (DAD) autoinhibitory interaction; both Rho GTPase-mediated activation and anillin interaction are required for mDia2 localization and function in cytokinesis. | PMID:20660154 | Molecular biology of the cell |
| 2011 | High | The PH domain of anillin directly binds PI(4,5)P2; reduction of cellular PI(4,5)P2 or PH domain mutations that disrupt PI(4,5)P2 binding impair anillin localization to the furrow; the PH domain has two functions: PI(4,5)P2-mediated furrow targeting and septin recruitment to the furrow. | PMID:22197245 | Current biology : CB |
| 2011 | Medium | Citron kinase (CIT-K) physically and functionally interacts with anillin; CIT-K is an upstream regulator (not effector) of RhoA during late cytokinesis; active RhoA and anillin are displaced from the midbody in CIT-K-depleted cells; overexpression of anillin alone delays abscission independently of RhoA. | PMID:21849473 | Molecular biology of the cell |
| 2011 | Medium | Anillin (ANI-1) promotes astral microtubule-directed cortical myosin polarization in C. elegans embryos; microtubule-directed myosin II polarization is aberrant without ANI-1; anillin interacts with microtubules providing an inhibitory mechanism to promote cell cortex polarization for cytokinesis. | PMID:21737681 | Molecular biology of the cell |
| 2012 | High | Anillin acts as a bifunctional linker coordinating midbody ring biogenesis: the N-terminus connects with the actomyosin contractile ring and supports midbody ring formation; the C-terminus (via septin Peanut) ensures stable anchoring of the plasma membrane; loss of either function prevents complete cytokinesis. | PMID:22226749 | Current biology : CB |
| 2012 | Medium | Anillin interacts with the PH domain of Ect2 (RhoGEF) in human cells; the anillin-Ect2 complex stabilizes central spindle microtubules at the cortex during cytokinesis; a PH domain mutation disrupting phospholipid association weakens the anillin-Ect2 interaction. | PMID:22514687 | PloS one |
| 2014 | High | Crystal structures of human anillin C-terminal region reveal a cryptic C2 domain and a Rho-binding domain; together with the PH domain, three membrane-associating elements (C2, RBD, PH) synergistically bind RhoA and phospholipids to anchor anillin at the cleavage furrow. | PMID:25959226 | Developmental cell |
| 2014 | High | Anillin localizes to epithelial cell-cell junctions throughout the cell cycle in Xenopus embryos and regulates junction integrity; anillin knockdown disrupts tight and adherens junctions, increases dynamic RhoA-GTP flares at junctions, and reduces junctional F-actin and myosin II accumulation. | PMID:24835458 | Current biology : CB |
| 2014 | High | Mutations in ANLN (R431C and G618C) cause familial FSGS; the R431C mutant displays reduced binding to the slit-diaphragm scaffold protein CD2AP, enhanced podocyte motility, and loss-of-function in zebrafish glomerular filtration; anillin is required for podocyte actin cytoskeleton integrity. | PMID:24676636 | Journal of the American Society of Nephrology : JASN |
| 2014 | Medium | Human anillin interacts with astral microtubules; astral and central spindle microtubules independently control contractile protein localization; RhoA-GTP binding to anillin competes with its microtubule interaction; anillin restricts myosin to the equatorial cortex and NuMA to the polar cortex. | PMID:24994938 | Journal of cell science |
| 2014 | Medium | A complex of p190RhoGAP-A and anillin modulates RhoA-GTP levels at the cytokinetic furrow; p190RhoGAP-A mutants that cannot bind anillin or inactivate RhoA fail to rescue cytokinesis defects; excess RhoA-GTP from p190RhoGAP-A depletion prevents progression to abscission. | PMID:25359885 | Journal of cell science |
| 2015 | High | Anillin (Drosophila and C. elegans) directly links RhoG/MIG-2 signaling to the actin cytoskeleton during neuronal migration and neurite growth: the active form of RhoG directly binds anillin and recruits it to the leading edge, where the anillin actin-binding domain stabilizes F-actin by antagonizing cofilin-mediated severing. | PMID:25843030 | Current biology : CB |
| 2015 | Medium | Importin-β2 targets anillin to the nucleus during interphase via a noncanonical PY-NLS; nuclear sequestration restricts anillin's membrane function to mitosis; importin-β2 binding does not regulate mitotic function but prevents cytosolic accumulation that disrupts interphase architecture. | PMID:25829492 | The Journal of biological chemistry |
| 2015 | Medium | Anillin knockdown disrupts tight and adherens junctions in human epithelial cells; this is accompanied by disorganization of the perijunctional actomyosin belt, decreased γ-adducin expression, and cytoplasmic aggregation of αII-spectrin; JNK activation mediates the junctional defects, and JNK inhibition restores junction integrity in anillin-depleted cells. | PMID:25809162 | Cellular and molecular life sciences : CMLS |
| 2015 | Medium | Active Ran/importin gradient spatially restricts anillin to the equatorial cortex; anillin contains a conserved NLS that binds importin-β; RhoA-GTP binding to anillin's RBD domain autoinhibits the NLS and nearby microtubule-binding domain; importin-β binding stabilizes a conformation favoring cortical recruitment during cytokinesis. | PMID:28931593 | Molecular biology of the cell |
| 2017 | Medium | Phosphorylation of anillin at S635 (adjacent to the AH domain) by mitotic kinases is required for efficient recruitment to the equatorial membrane at anaphase onset; a S635A mutant shows impaired cortical recruitment and cytokinesis failure; a phosphomimetic S635D partially restores localization. | PMID:28081137 | PLoS genetics |
| 2017 | High | Anillin actin-binding domain harbors three distinct actin-binding sites (ABS1–3); ABS1 and ABS3 bind F-actin in a mutually exclusive fashion; ABS2 and ABS3 are each required and together sufficient for cortical localization during cytokinesis; anillin can cross-link actin filaments in parallel and antiparallel orientations and promotes 3D F-actin bundle formation. | PMID:28147230 | Journal of molecular biology |
| 2018 | Medium | The ANLN R431C FSGS mutation causes hyperactivation of PI3K/AKT/mTOR/p70S6K/Rac1 signaling and mTOR-driven ER stress in podocytes; inhibition of mTOR, GSK-3β, Rac1, or calcineurin ameliorates R431C effects; calcineurin/NFAT pathway inhibition reduces endogenous ANLN and mTOR expression. | PMID:30002222 | Journal of the American Society of Nephrology : JASN |
| 2019 | High | Anillin directly binds GTP-RhoA and concentrates PIP2 at the cortex to promote effector recruitment; a sequential kinetic scaffolding pathway is proposed and tested where GTP-RhoA first binds anillin, is then retained at the membrane by PIP2 after disengaging from anillin, and repeated binding cycles increase GTP-RhoA dwell time to enhance effector recruitment. | PMID:31105010 | Developmental cell |
| 2019 | High | Anillin regulates medial-apical actomyosin in Xenopus epithelial cells; anillin overexpression increases mechano-sensitive vinculin recruitment to junctions (increased tension) but slows junctional recoil after laser ablation; medial-apical laser ablation reveals tensile forces stored across the apical surface that depend on anillin; anillin's effects on cellular mechanics impact tissue-wide mechanics. | PMID:30702429 | eLife |
| 2019 | Medium | ANLN knockdown in pancreatic cancer cells inhibits LASP1 expression via upregulation of miR-218-5p; ANLN-induced EZH2 upregulation suppresses miR-218-5p to maintain LASP1 levels; this ANLN→EZH2→miR-218-5p→LASP1 axis promotes pancreatic cancer cell proliferation, migration, and invasion. | PMID:31395079 | Journal of experimental & clinical cancer research : CR |
| 2020 | Medium | Importin-β binding to anillin's NLS promotes a conformation that increases accessibility of the C2 domain; active RhoA binding to the RBD initially opens the C2 domain, and subsequent importin binding stabilizes the conformation required for cortical recruitment; this reveals importin-mediated positive regulation (not just nuclear sequestration) of a cortical protein. | PMID:32238082 | Molecular biology of the cell |
| 2020 | Medium | The Rho guanine nucleotide exchange factor Bud3 and anillin-like Bud4 form a RhoGEF-anillin module essential for septin architectural remodeling from hourglass to double ring in budding yeast; Bud3 stabilizes single septin filaments and Bud4 strengthens interactions between filament types at outer zones of the transitional hourglass. | PMID:32197082 | Current biology : CB |
| 2020 | Medium | ANLN is required for cell migration, invasion, and anchorage-independent growth in breast cancer cells; ANLN knockout triggers transcriptional reprogramming suppressing stemness and inducing mesenchymal-to-epithelial trans-differentiation with upregulation of E-cadherin; E-cadherin knockdown restores migration in anillin-deficient cells. | PMID:31910867 | Breast cancer research : BCR |
| 2021 | High | Anillin, as a non-motor actin crosslinker, autonomously propels contractility of actin bundles and rings: it generates contractile forces of tens of picoNewtons to maximize overlap lengths between bundled antiparallel actin filaments; contractility is enhanced by actin disassembly and leads to ring constriction in the absence of myosin activity. | PMID:34321459 | Nature communications |
| 2021 | Medium | ANLN directly interacts with RhoA (demonstrated by Co-IP) and promotes RhoA activation; ANLN overexpression enhances expression of multidrug resistance proteins MDR1 and BCRP, promoting doxorubicin resistance; C3 transferase (RhoA inhibitor) abolishes ANLN overexpression effects on drug resistance. | PMID:33116832 | Cancer management and research |
| 2022 | High | USP10 deubiquitinase interacts with ANLN and removes K11- and K63-linked ubiquitin chains to prevent APC/C-Cdh1-mediated degradation; USP10 and Cdh1 form a non-competitive complex with ANLN to balance its protein levels; USP10-stabilized ANLN promotes contractile ring assembly and cytokinesis. | PMID:36526897 | Cell death and differentiation |
| 2022 | Medium | CIN85 interacts directly with the N-terminal region of anillin and with SEPT9; this anillin-CIN85-SEPT9 complex facilitates SEPT9-containing septin filament localization to the intercellular bridge plasma membrane during cytokinesis; the anillin PH domain separately binds septin units lacking SEPT9 but enriched in SEPT11. | PMID:36044846 | Cell reports |
| 2022 | Medium | ANLN acts as a scaffold that strengthens the interaction between RACGAP1 and PLK1; ANLN promotes PLK1-mediated RACGAP1 phosphorylation and RhoA activation to ensure cytokinesis fidelity; hepatic Anln ablation in mice enhances polyploidization and impairs c-Myc/NRAS-driven hepatocarcinogenesis. | PMID:35477750 | Oncogene |
| 2023 | Medium | Nuclear ANLN forms a transcriptional complex with SP1, which enhances KIF2C transcriptional activity to activate the mTORC1 pathway; increased RANKL and disproportionate RANKL-OPG expression in the bone microenvironment drives HCC bone metastasis; ANLN mRNA stability is enhanced via m6A modification by METTL3/YTHDF1. | PMID:36923927 | International journal of biological sciences |
| 2023 | Medium | TAZ and TEAD2 transcriptionally upregulate ANLN as a target gene to promote HCC cell proliferation; CRISPRi knockdown of ANLN in a dCas9 knock-in mouse model reduces TAZ-driven and MET/CTNNB1-driven HCC growth in vivo. | PMID:36894036 | Gastroenterology |

## Citations

- PMID:15496454
- PMID:15930114
- PMID:16040610
- PMID:16357138
- PMID:17488632
- PMID:18158242
- PMID:18158243
- PMID:18349071
- PMID:18579688
- PMID:20660154
- PMID:21737681
- PMID:21849473
- PMID:22197245
- PMID:22226749
- PMID:22514687
- PMID:24676636
- PMID:24835458
- PMID:24994938
- PMID:25359885
- PMID:25809162
- PMID:25829492
- PMID:25843030
- PMID:25959226
- PMID:28081137
- PMID:28147230
- PMID:28931593
- PMID:30002222
- PMID:30702429
- PMID:31105010
- PMID:31395079
- PMID:31910867
- PMID:32197082
- PMID:32238082
- PMID:33116832
- PMID:34321459
- PMID:35477750
- PMID:36044846
- PMID:36526897
- PMID:36894036
- PMID:36923927
- PMID:7559773
