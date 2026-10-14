---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ASPSCR1
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9BZE9
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 17
citation_count: 17
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ASPSCR1 (human)

## Current model (mechanistic narrative)

ASPSCR1 (TUG/ASPL/UBXD9) is a multifunctional tethering protein that controls insulin-regulated vesicle trafficking and that, when fused to TFE3, becomes a sarcoma-driving oncogenic transcription factor [PMID:17202135, PMID:36246906, PMID:37029109]. In fat and muscle, intact TUG traps GLUT4 storage vesicles intracellularly by binding GLUT4 through its N-terminal region and the Golgi matrix through its acetylated C-terminus, holding vesicles in perinuclear membranes until insulin acts [PMID:17202135, PMID:22610098, PMID:36246906]; its N-terminus adopts a ubiquitin-like beta-grasp fold that serves as a protein-interaction module rather than a covalent modifier [PMID:16501224]. Insulin triggers site-specific endoproteolytic cleavage of TUG by the muscle splice form of the Usp25 protease in a TC10α-dependent manner, releasing vesicles for translocation; the N-terminal TUGUL product modifies the KIF5B kinesin to load cargo onto microtubule motors, while the C-terminal product enters the nucleus to bind PPARγ/PGC-1α and drive fatty acid oxidation and thermogenesis, with its stability controlled by the ATE1 N-degron pathway [PMID:22610098, PMID:29773651, PMID:33686286]. This proteolytic switch governs coordinated translocation of both GLUT4 and IRAP and regulates systemic glucose homeostasis and energy expenditure in vivo [PMID:23744065, PMID:25944897]. Independently, TUG binds the p97/VCP AAA-ATPase N-terminal domain through an extended UBX domain and stoichiometrically disassembles p97 hexamers into p97:ASPL heterotetramers with loss of D2 ATPase activity, regulating ERAD, membrane trafficking, and Golgi reassembly [PMID:22207755, PMID:27762274]. In alveolar soft part sarcoma, the der(17)t(X;17) translocation fuses ASPSCR1 in-frame to TFE3, producing a nuclear oncoprotein that acts as a strong transactivator binding thousands of genomic loci and directly upregulating MET, CYP17A1, and other targets [PMID:11244503, PMID:23288701]; in vivo it remodels super-enhancers to drive angiogenesis via Pdgfb, Rab27a, and Sytl2, activates lysosome-autophagy programs, and induces p21-dependent senescence with SASP secretion [PMID:37029109, PMID:33846569, PMID:27673450].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity, GO:0140110 transcription regulator activity, GO:0031386 protein tag activity
- **localization:** GO:0005783 endoplasmic reticulum, GO:0005634 nucleus, GO:0005886 plasma membrane
- **pathway (Reactome):** R-HSA-382551 Transport of small molecules, R-HSA-5653656 Vesicle-mediated transport, R-HSA-74160 Gene expression (Transcription), R-HSA-1643685 Disease, R-HSA-392499 Metabolism of proteins
- **partners:** GLUT4, VCP, GOLGIN-160, ACBD3, USP25, KIF5B, SIRT2, PPARG
- **complexes:** p97/VCP:ASPL heterotetramer, GLUT4 storage vesicle tethering complex, ASPSCR1-TFE3 fusion transcription factor

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2001 | High | ASPSCR1 (ASPL) at 17q25 is fused in-frame to the TFE3 transcription factor gene at Xp11.2 via the der(17)t(X;17)(p11.2;q25) translocation in alveolar soft part sarcoma, generating ASPL-TFE3 fusion proteins (type 1 and type 2) that retain the TFE3 DNA-binding domain, implying transcriptional deregulation as the oncogenic mechanism. The ASPL protein contains a UBX-like domain in its C-terminal region. | PMID:11244503 | Oncogene |
| 2007 | High | TUG (ASPSCR1) directly binds GLUT4 via a large intracellular loop in GLUT4, retains GLUT4 in perinuclear (non-endosomal) membranes in unstimulated 3T3-L1 adipocytes, and is required for intracellular sequestration of GLUT4; siRNA-mediated depletion or dominant-negative TUG expression causes GLUT4 translocation and enhanced glucose uptake resembling insulin stimulation. | PMID:17202135 | The Journal of biological chemistry |
| 2011 | High | TUG (ASPSCR1) binds p97/VCP at its N-terminal domain via an extended sequence comprising three TUG regions (not the UBX domain alone), causes stoichiometric conversion of p97 hexamers into monomers (hexamer disassembly), and localizes to the ER-to-Golgi intermediate compartment (ERGIC) and ER exit sites. TUG overexpression accumulates ubiquitylated substrates and targets p97 to the nucleus; TUG depletion impairs Golgi reassembly after brefeldin A removal. | PMID:22207755 | The Journal of biological chemistry |
| 2012 | High | Insulin stimulates site-specific endoproteolytic cleavage of TUG (ASPSCR1) in adipocytes in a TC10α-dependent manner, separating an N-terminal GLUT4-binding fragment (generating an 18-kDa ubiquitin-like modifier called TUGUL) from a C-terminal fragment that had bound the Golgi matrix anchor. Intact TUG links GLUT4 to PIST (a TC10α effector) and to Golgin-160 via its C-terminus. A cleavage-resistant TUG mutant does not support insulin-responsive GLUT4 translocation or glucose uptake. | PMID:22610098 | The Journal of biological chemistry |
| 2013 | High | Muscle-specific transgenic expression of the TUG C-terminal UBX-Cter fragment in mice causes constitutive TUG proteolysis and GLUT4 translocation to T-tubules during fasting, decreases fasting plasma glucose and insulin, increases whole-body glucose turnover, and elevates oxygen consumption and energy expenditure by 12–13%, demonstrating that the TUG proteolytic pathway regulates systemic glucose homeostasis and energy metabolism in muscle. | PMID:23744065 | The Journal of biological chemistry |
| 2013 | High | ASPSCR1-TFE3 fusion protein localizes predominantly to the nucleus, functions as a stronger transcriptional transactivator than native TFE3, binds 2193 genomic loci genome-wide, and up-regulates direct target genes including MET, CYP17A1, and UPP1. RNAi screening identified 11 additional ASPSCR1-TFE3 target genes that contribute to cancer cell proliferation. | PMID:23288701 | The Journal of pathology |
| 2015 | High | TUG (ASPSCR1) C-terminus is acetylated; acetylation reduces binding of TUG to ACBD3 (but not Golgin-160), and mutation of acetylated residues impairs insulin-responsive GLUT4 trafficking. SIRT2 deacetylase binds TUG, deacetylates it, and its overexpression redistributes GLUT4 and IRAP to the plasma membrane. SIRT2 knockout mice show increased TUG acetylation and proteolytic processing and enhanced glucose disposal. | PMID:25561724 | The Journal of biological chemistry |
| 2015 | High | TUG proteolysis controls IRAP (insulin-regulated aminopeptidase) targeting to T-tubules in muscle as well as GLUT4 translocation; IRAP binds TUG through a short peptide previously shown critical for GLUT4 intracellular retention. Constitutive TUG proteolysis in transgenic mice increases vasopressin degradation in vivo, demonstrating that TUG controls coordinated translocation of both GLUT4 and IRAP vesicle cargoes. | PMID:25944897 | The Journal of biological chemistry |
| 2016 | High | ASPSCR1 (ASPL) contains an extended UBX domain (eUBX) that is critical for disassembly of p97 hexamers, generating stable p97:ASPL heterotetramers. Hexamer disassembly is accompanied by reorientation of the p97 D2 ATPase domain and loss of D2 ATPase activity. Overproduction of ASPL disrupts p97 hexamer function in ERAD. | PMID:27762274 | Nature communications |
| 2016 | Medium | ASPL-TFE3 fusion oncoprotein functions as an aberrant transcription factor that directly activates p21 (CDKN1A) expression in a p53-independent manner through binding to the p21 promoter, causing cell cycle arrest and cellular senescence; senescent cells secrete proinflammatory SASP cytokines. | PMID:27673450 | Neoplasia |
| 2016 | Medium | Mutant p97 (disease-causing R93C, R155H, R155C) reduces the efficiency of UBXD9/TUG (ASPSCR1)/ASPL-mediated p97 hexamer disassembly into monomers, with species- and mutation-specific differences in binding affinity (assessed by surface plasmon resonance) and ATP-dependent interactions. | PMID:27132113 | European journal of cell biology |
| 2018 | High | The muscle splice form of Usp25 (Usp25m), but not the Usp25a isoform, is the protease required for insulin-stimulated TUG cleavage and GLUT4 translocation in adipocytes. Usp25m binds TUG and GLUT4, colocalizes with TUG in unstimulated cells, and dissociates from TUG-bound vesicles after insulin. TUG cleavage generates TUGUL, which modifies the KIF5B kinesin motor, and this is required to load GLUT4 onto microtubule-based motors. TUG proteolysis and Usp25m are reduced in insulin-resistant adipose tissue. | PMID:29773651 | The Journal of biological chemistry |
| 2021 | High | Insulin-stimulated TUG (Aspscr1) cleavage in muscle releases a C-terminal cleavage product that enters the nucleus, binds PPARγ and PGC-1α, and regulates gene expression to promote lipid oxidation and thermogenesis, upregulating sarcolipin in muscle and UCP1 in adipocytes. This pathway is independent of PI3K/Akt. The PPARγ2 Pro12Ala polymorphism (associated with reduced diabetes risk) enhances TUG binding. The ATE1 arginyltransferase regulates stability of the TUG C-terminal product via an N-degron pathway. Muscle-specific Tug knockout and constitutive-cleavage mouse models confirmed regulation of insulin-stimulated glucose uptake and whole-body energy expenditure. | PMID:33686286 | Nature metabolism |
| 2022 | Medium | TUG (Aspscr1, UBXD9) proteins act as central tethers that trap GLUT4 storage vesicles at the Golgi matrix via N-terminal GLUT4-binding and C-terminal Golgi matrix-binding; insulin triggers Usp25m-mediated endoproteolytic cleavage generating the TUGUL ubiquitin-like modifier (N-terminal product) that modifies KIF5B kinesin in adipocytes, enabling microtubule-based vesicle transport to the cell surface. After cleavage, the TUG C-terminal product is extracted from the Golgi matrix by p97/VCP ATPase. In both muscle and fat, the C-terminal product enters the nucleus to bind PPARγ/PGC-1α and regulate fatty acid oxidation. Stability of the C-terminal product is regulated by Ate1-dependent N-degron pathway. | PMID:36246906 | Frontiers in endocrinology |
| 2006 | Medium | The N-terminal region of TUG (ASPSCR1; residues 10–83) adopts a ubiquitin-like (beta-grasp) fold as determined by NMR spectroscopy. This UBL1 domain lacks the C-terminal diglycine motif and canonical ubiquitin 'Ile-44 hydrophobic face', suggesting it functions as a protein-protein interaction module rather than as a covalent modifier. | PMID:16501224 | Protein science |
| 2023 | High | ASPSCR1::TFE3 fusion transcription factor is dispensable for in vitro tumor cell maintenance but is required for in vivo tumor development via angiogenesis. ASPSCR1::TFE3 associates with super-enhancers (SEs) at its DNA binding sites; its loss causes SE redistribution affecting angiogenesis pathway genes. ASPSCR1::TFE3 transcriptionally activates Pdgfb, Rab27a, Sytl2, and Vwf; Rab27a and Sytl2 promote angiogenic factor trafficking to facilitate ASPS vascular network construction. | PMID:37029109 | Nature communications |
| 2021 | Medium | ASPL-TFE3 fusion protein translocates to the nucleus in renal cell carcinoma cells and transcriptionally activates lysosome-autophagy pathway genes by binding their promoters. This autophagy activation enables energy stress evasion by promoting protein and lipid utilization. The fusion protein escapes regulation by the classic mTOR-TFE3 signaling axis and instead activates phospho-mTOR and its downstream targets. | PMID:33846569 | Oncogene |

## Citations

- PMID:11244503
- PMID:16501224
- PMID:17202135
- PMID:22207755
- PMID:22610098
- PMID:23288701
- PMID:23744065
- PMID:25561724
- PMID:25944897
- PMID:27132113
- PMID:27673450
- PMID:27762274
- PMID:29773651
- PMID:33686286
- PMID:33846569
- PMID:36246906
- PMID:37029109
