---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ABI3BP
affinage_run_date: 2026-06-09T22:02:37
uniprot_accession: Q7Z7G0
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 12
citation_count: 12
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ABI3BP (human)

## Current model (mechanistic narrative)

ABI3BP is a secreted extracellular matrix protein that acts as a brake on stem and progenitor cell proliferation while licensing their differentiation [PMID:23666637, PMID:25296984]. Mechanistically, ABI3BP deposited in the matrix binds integrin-β1 and drives Src association with paxillin, stabilizing focal adhesions and stress fibers; loss of ABI3BP releases this brake, increasing proliferation through cyclin-D1, ERK1/2, and Src to promote S-phase entry, and severely impairing osteogenic and adipogenic differentiation of mesenchymal stem cells [PMID:23666637]. In cardiac progenitor cells the same integrin-β1 axis signals through PKC-ζ and Akt to drive cardiomyocyte differentiation, such that genetic ablation expands the progenitor pool but worsens recovery after myocardial infarction [PMID:25296984]. ABI3BP couples this anti-proliferative role to cellular senescence: its loss inhibits proliferation and induces p53/p21-dependent growth arrest with multicentrosome formation in fibroblasts [PMID:19338757], and conversely its downregulation suppresses senescence through the Nrf2 antioxidant pathway in vascular smooth muscle cells [PMID:40889718] and through Klotho-dependent control of ferroptosis in renal tubular cells [PMID:38812032]. ABI3BP expression is epigenetically silenced by EZH2-mediated H3K27 methylation directed by the lncRNA MALAT1 [PMID:31174563]. The protein also maintains F-actin organization and type-I interferon (IRF3/TBK1) signaling against RNA virus replication [PMID:38384000], shapes mitral cell dendritic refinement in the olfactory bulb as a secreted factor [PMID:19302145], and is proteolytically cleaved by thrombin at Arg337, with recombinant ABI3BP protecting the blood-brain barrier after ischemia-reperfusion injury via PI3K/Akt survival signaling [PMID:41839242].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098631 cell adhesion mediator activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0031012 extracellular matrix, GO:0005576 extracellular region
- **pathway (Reactome):** *(none)*
- **partners:** ITGB1, SRC, PXN
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2013 | High | Abi3bp forms extracellular deposits whose expression is controlled by Akt1 and ubiquitin-mediated degradation. Abi3bp knockdown/knockout stabilized focal adhesions and promoted stress-fiber formation in mesenchymal stem cells (MSCs). Upon Abi3bp binding to integrin-β1, Src associated with paxillin, which inhibited MSC proliferation. Knockout or stable knockdown increased MSC proliferation via cyclin-D1, ERK1/2, and Src, promoting S-phase entry. MSCs from Abi3bp knockout mice displayed severe deficiencies in osteogenic and adipogenic differentiation. | PMID:23666637 | Stem cells (Dayton, Ohio) |
| 2014 | High | Abi3bp regulates cardiac progenitor cell (CPC) proliferation and differentiation via integrin-β1, protein kinase C-ζ, and Akt signaling. Genetic ablation of Abi3bp in vivo inhibited CPC differentiation while increasing CPC number and proliferative capacity, correlating with adverse recovery after myocardial infarction. In vitro, Abi3bp-deficient CPCs showed reduced expression of cardiomyocyte markers under differentiating conditions. | PMID:25296984 | Circulation research |
| 2009 | Medium | TARSH (ABI3BP) is a secreted protein that promotes reduction of mitral cell dendritic complexity in the olfactory bulb. Secreted TARSH restricts dendritic branching and outgrowth of interneurons in dissociated olfactory bulb cultures. Overexpression of TARSH in mitral cells also produced dendritic morphological changes. Its expression is restricted to pyramidal neurons along the main olfactory pathway and is not altered by odor-evoked activity blockade. | PMID:19302145 | The European journal of neuroscience |
| 2009 | Medium | Reduction of TARSH (ABI3BP) expression by shRNA in mouse embryonic fibroblasts (MEFs) inhibited proliferation and increased senescence-associated β-galactosidase activity. This growth arrest was dependent on p53, as demonstrated using p53-/- MEFs, and involved p21(Cip1) accumulation. TARSH reduction also induced multicentrosome formation, linked to chromosomal instability. | PMID:19338757 | Biochemical and biophysical research communications |
| 2005 | Medium | mTARSH (mouse ABI3BP) is induced in the early phase of mouse embryonic fibroblast (MEF) replicative senescence. Structural analysis revealed five splicing variants sharing a common reading frame, with diversity derived from the SH3-binding motif cluster in the middle of the gene. | PMID:15752759 | Biochemical and biophysical research communications |
| 2019 | Medium | MALAT1 lncRNA down-regulates ABI3BP expression in gallbladder cancer through recruitment of EZH2 to the ABI3BP promoter, leading to H3K27 methylation-mediated silencing. Silencing MALAT1 or suppression of H3K27 methylation restored ABI3BP expression, suppressed cell growth, and enhanced cell senescence. | PMID:31174563 | Journal of experimental & clinical cancer research : CR |
| 2024 | Medium | ABI3BP knockdown in human skin fibroblast BJ-5ta cells induced structural rearrangement of intracellular F-actin. ABI3BP knockdown increased VSV genome replication by 2.2–4.0-fold and significantly reduced phosphorylation of IRF3 and TBK1 after VSV infection, indicating that ABI3BP maintains type I interferon pathway integrity. | PMID:38384000 | Chinese medical sciences journal |
| 2024 | Medium | ABI3BP gene knockout in mice elevated Klotho expression and reduced ferroptosis in renal tubular epithelial cells following irradiation, thereby mitigating radiation-induced renal aging. A significant negative correlation between ABI3BP and Klotho was established. Klotho knockdown attenuated the aging inhibition caused by ABI3BP downregulation, placing ABI3BP upstream of Klotho in regulating ferroptosis and renal aging. | PMID:38812032 | Journal of translational medicine |
| 2025 | Medium | ABI3BP downregulation inhibits angiotensin II-induced vascular smooth muscle cell (VSMC) senescence by enhancing Nrf2 expression and its downstream anti-aging factors. ABI3BP knockout in mice ameliorated Ang II-induced vascular aging, reduced IL-6 and TNF-α secretion, alleviated collagen accumulation, and suppressed Ang II-induced blood pressure elevation. Silencing Nrf2 with siRNA attenuated the protective effects of ABI3BP downregulation, placing ABI3BP upstream of Nrf2. | PMID:40889718 | Mechanisms of ageing and development |
| 2025 | Low | ABI3BP overexpression in NSCLC cells inhibited cell growth, motility, and EMT, and suppressed the MAPK/ERK pathway. ABI3BP functions as a tumor suppressor in NSCLC by targeting the MAPK/ERK axis. | PMID:40092729 | Open life sciences |
| 2026 | Medium | Thrombin cleaves ABI3BP at arginine 337 in the context of cerebral ischemia-reperfusion injury (IRI), reducing endogenous ABI3BP. The thrombin inhibitor dabigatran reversed this reduction. Recombinant ABI3BP crossed the blood-brain barrier, reduced infarct volume, restored blood flow, and decreased BBB leakage by upregulating tight junction proteins ZO-1/Occludin. ABI3BP inhibited endothelial apoptosis by suppressing cleaved caspase-3 and increasing Bcl-2/Bax, p-Akt/Akt, and p-PI3K/PI3K, placing ABI3BP as an activator of PI3K/Akt survival signaling. | PMID:41839242 | Biochemical pharmacology |
| 2025 | Low | ABI3BP knockdown in chondrocytes mitigated IL-1β-induced ECM degradation and reduced senescence-associated markers (P16, P21), indicating ABI3BP promotes chondrocyte senescence and ECM catabolism in osteoarthritis. | PMID:41232761 | Journal of proteomics |

## Citations

- PMID:15752759
- PMID:19302145
- PMID:19338757
- PMID:23666637
- PMID:25296984
- PMID:31174563
- PMID:38384000
- PMID:38812032
- PMID:40092729
- PMID:40889718
- PMID:41232761
- PMID:41839242
