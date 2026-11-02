---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARMS2
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: P0C7Q2
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

# Affinage mechanistic annotation for ARMS2 (human)

## Current model (mechanistic narrative)

ARMS2 is a primate-specific small protein implicated in complement-mediated clearance of cellular debris and in the pathogenesis of age-related macular degeneration (AMD) [PMID:28086806, PMID:22133792]. Although it lacks a classical signal sequence, ARMS2 is secreted through an unconventional Golgi-bypass route: it recruits the lectin chaperones calnexin and calreticulin from the cytosol and traffics through GRASP65-positive structures, and secretion is insensitive to brefeldin A but abolished by mutation of the calnexin/calreticulin-binding residues [PMID:27270414]. Once extracellular, ARMS2 behaves as an extracellular matrix-associated protein that interacts with fibulin-6 (hemicentin-1) and localizes to choroidal pillars at sites of drusen formation [PMID:19696174]. Functionally, ARMS2 binds apoptotic and necrotic cell surfaces and recruits the complement activator properdin to augment C3b opsonization for phagocytosis [PMID:28086806], and it positively regulates the proinflammatory output of retinal pigment epithelium cells, including C3, C5, IL-6, IL-8, and TNF-α [PMID:23959158]. The AMD risk haplotype acts at two levels: a 3'-UTR del443ins54 polymorphism destabilizes ARMS2 mRNA and abolishes protein expression in risk homozygotes [PMID:18511946, PMID:21252205], while the coding A69S variant alters proliferation, attachment, and migration and elevates oxidative stress in retinal cells [PMID:23326481, PMID:37126685]. Earlier reports of mitochondrial outer-membrane localization [PMID:17884985] were superseded by evidence for a cytosolic/secreted distribution [PMID:19255159, PMID:19696174].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity, GO:0005198 structural molecule activity
- **localization:** GO:0005576 extracellular region, GO:0031012 extracellular matrix, GO:0005829 cytosol, GO:0005783 endoplasmic reticulum
- **pathway (Reactome):** R-HSA-168256 Immune System, R-HSA-9609507 Protein localization
- **partners:** PROPERDIN, FIBULIN-6, CALNEXIN, CALRETICULIN
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2007 | Medium | LOC387715/ARMS2 mRNA is expressed in human retina and various cell lines and encodes a 12-kDa protein that localizes to the mitochondrial outer membrane when expressed in mammalian cells. | PMID:17884985 | Proceedings of the National Academy of Sciences of the United States of America |
| 2008 | Medium | A deletion-insertion polymorphism in the ARMS2 3'-UTR (del443ins54) removes the polyadenylation signal and inserts a 54-bp AU-rich element that mediates rapid mRNA turnover, resulting in undetectable ARMS2 expression in homozygous risk-allele carriers. The normal ARMS2 protein associates with the mitochondrial ellipsoid region of photoreceptors. | PMID:18511946 | Nature genetics |
| 2009 | Medium | Contrary to the mitochondrial localization report, both endogenous and exogenously expressed ARMS2 protein are distributed predominantly in the cytosol, not on the mitochondrial outer membrane. The A69S variant is more likely to associate with the cytoskeleton compared with wild-type ARMS2. | PMID:19255159 | Investigative ophthalmology & visual science |
| 2009 | Medium | ARMS2 is a secreted extracellular matrix protein (not mitochondrial) that directly interacts with fibulin-6 (hemicentin-1) and several other extracellular matrix proteins. Although ARMS2 lacks a classical N-terminal signal sequence, it is translocated to the endoplasmic reticulum in cultured cells before secretion. In human eyes, ARMS2 is localized predominantly to choroidal pillars, a region corresponding to drusen formation sites. | PMID:19696174 | Investigative ophthalmology & visual science |
| 2016 | Medium | ARMS2 is secreted via an unconventional (Golgi-bypass) pathway: it recruits lectin chaperones calnexin/calreticulin from the cytosol, co-localizes with calnexin-positive vesicle-like structures, and co-localizes with GRASP65 (a marker of unconventional secretion). Brefeldin A (ER-to-Golgi blocker) does not inhibit ARMS2 secretion. Site-directed mutagenesis of residues required for calnexin/calreticulin interaction abolishes secretion. | PMID:27270414 | Human molecular genetics |
| 2017 | High | Recombinant ARMS2 binds to apoptotic and necrotic cell surfaces and recruits the complement activator properdin, forming ARMS2-properdin complexes that augment C3b surface opsonization for phagocytosis. ARMS2 protein is absent in monocytes and microglia derived from patients homozygous for the AMD risk variant (rs10490924), and ARMS2 is expressed in human monocytes (especially under oxidative stress) and in retinal microglia. | PMID:28086806 | Journal of neuroinflammation |
| 2013 | Medium | siRNA knockdown of ARMS2 in ARPE-19 cells reduces secreted levels of complement components C3 and C5 and proinflammatory cytokines IL-6, IL-8, and TNF-α by ~30–37%, indicating that ARMS2 positively regulates expression of these proinflammatory mediators. | PMID:23959158 | Graefe's archive for clinical and experimental ophthalmology |
| 2013 | Medium | Overexpression of wild-type ARMS2 and the A69S mutant (rs10490924) in RF/6A and RPE cells showed that the A69S mutation significantly increases cell proliferation and attachment but inhibits cell migration compared with wild-type ARMS2; neither form affected tube formation (neovascularization in vitro). | PMID:23326481 | PloS one |
| 2011 | Medium | In AMD patients, the ARMS2 risk genotype (rs10490924) is independently associated with elevated systemic complement activation markers (C3d/C3 ratio, C5a), even in the absence of CFH risk alleles, placing ARMS2 in the alternative complement pathway relevant to AMD pathogenesis. | PMID:22133792 | Ophthalmology |
| 2023 | Medium | CRISPR editing of the rs10490924 (A69S) variant in iPSC-derived retinal cells from AMD patients demonstrates that this specific SNV raises oxidative stress; sodium phenylbutyrate preferentially reverses cell death caused by ARMS2 rs10490924 but not by HTRA1 rs11200638. | PMID:37126685 | Proceedings of the National Academy of Sciences of the United States of America |
| 2011 | Medium | Heterologous expression of genomic ARMS2 constructs carrying risk-haplotype alleles produces significantly reduced ARMS2 mRNA levels compared with non-risk isoforms, an effect specifically attributable to the 3'-UTR del443ins54 insertion/deletion polymorphism. Analysis of post-mortem retina/RPE samples heterozygous for the risk haplotype confirmed that the risk haplotype reduces ARMS2 (but not HTRA1) mRNA expression in vivo. | PMID:21252205 | Human molecular genetics |
| 2021 | Medium | Two Gtf2i-β/δ transcription factor isoforms bind a cis-element (5'-ATTAATAACC-3') within the ARMS2/HTRA1 indel sequence (identified by EMSA and LC-MS/MS), leading to enhanced transcription of HTRA1 in transfected cells and AMD patient iPSCs. This mechanism was validated in mice where CAG-promoter overexpression of Htra1 elevated blood Htra1, upregulated VEGF, and produced a CNV-like phenotype. | PMID:33636181 | The Journal of biological chemistry |

## Citations

- PMID:17884985
- PMID:18511946
- PMID:19255159
- PMID:19696174
- PMID:21252205
- PMID:22133792
- PMID:23326481
- PMID:23959158
- PMID:27270414
- PMID:28086806
- PMID:33636181
- PMID:37126685
