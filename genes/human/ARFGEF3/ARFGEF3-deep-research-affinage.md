---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARFGEF3
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q5TH69
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 14
citation_count: 14
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARFGEF3 (human)

## Current model (mechanistic narrative)

ARFGEF3 (BIG3) is a multifunctional scaffold protein that controls the subcellular localization and activity of its principal partner PHB2/REA across several tissue contexts [PMID:19496786, PMID:28555617]. Despite carrying a Sec7 domain, BIG3 lacks the conserved catalytic glutamate required for guanine nucleotide exchange and instead functions through an armadillo-type alpha-helical repeat that mediates its PHB2 interaction [PMID:24997568]. In ERα-positive breast cancer cells, cytoplasmic BIG3 sequesters PHB2, blocking its estrogen-dependent binding to karyopherin-alpha import factors (KPNA1, KPNA5, KPNA6) and thereby preventing PHB2 nuclear translocation and its suppression of ERα [PMID:19496786, PMID:26052702]. Mechanistically, BIG3 acts as an A-kinase anchoring protein that simultaneously binds PKA and the phosphatase catalytic subunit PP1Cα; E2-induced PKA phosphorylation of BIG3 stimulates PP1Cα-mediated dephosphorylation of PHB2-S39, inactivating PHB2 and sustaining estrogen-dependent growth [PMID:28555617]. Disrupting the BIG3-PHB2 complex with the cell-permeable ERAP peptide releases PHB2 to inhibit genomic and non-genomic ERα signalling and ERα/growth-factor-receptor crosstalk, overcoming tamoxifen resistance [PMID:24051437, PMID:25736224]. Independently of this cancer role, BIG3 localizes to the trans-Golgi network in pancreatic beta- and alpha-cells where it negatively regulates secretory-granule biogenesis, limiting insulin and glucagon content and secretion without altering individual granule exocytotic kinetics [PMID:24711543, PMID:25139048, PMID:25737957]. A mitochondrial pool of the BIG3-PHB2 complex regulates inner mitochondrial membrane function and suppresses PARP-1/AIF-dependent apoptosis in osteosarcoma cells, and Arfgef3 loss is protective against ischemia-reperfusion kidney injury via improved mitochondrial function [PMID:34363714, PMID:41087303].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0140313 molecular sequestering activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005829 cytosol, GO:0005794 Golgi apparatus, GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-5653656 Vesicle-mediated transport, R-HSA-5357801 Programmed Cell Death
- **partners:** PHB2, PRKACA, PPP1CA, KPNA1, KPNA5, KPNA6
- **complexes:** BIG3-PHB2 complex, BIG3-PKA-PP1Cα (AKAP) complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2009 | High | BIG3 (ARFGEF3) binds PHB2/REA in the cytoplasm and inhibits its estrogen-dependent nuclear translocation. When BIG3 is absent, estradiol stimulation causes PHB2 to translocate to the nucleus, interact with ERα, and suppress ERα transcriptional activity. When BIG3 is present, it traps PHB2 in the cytoplasm, thereby enhancing ERα transcriptional activity. | PMID:19496786 | Cancer science |
| 2013 | High | A cell-permeable peptide inhibitor (ERAP) derived from BIG3 disrupts the BIG3-PHB2 interaction, releasing PHB2 to bind directly to nuclear- and membrane-associated ERα, thereby suppressing multiple ERα-signalling pathways (genomic, non-genomic ERα activation and ERα phosphorylation) and overcoming tamoxifen resistance in ERα-positive breast cancer cells. | PMID:24051437 | Nature communications |
| 2014 | High | BIG3 (ARFGEF3) is predominantly localized to insulin- and clathrin-positive trans-Golgi network (TGN) compartments in insulin-secreting cells. BIG3 deficiency increases insulin content, granule number, insulin secretion upon stimulation, and accelerates proinsulin-to-insulin processing, demonstrating that BIG3 negatively modulates insulin granule biogenesis and maturation. | PMID:24711543 | EMBO reports |
| 2014 | High | BIG3 negatively regulates insulin granule exocytosis by restricting insulin granule biogenesis without affecting the release kinetics of individual granules at final exocytotic steps. BKO β-cells have >60% more insulin granules but an unaltered number of morphologically docked granules, indicating BIG3 acts at the biogenesis stage rather than the docking/fusion stage. | PMID:25139048 | American journal of physiology. Endocrinology and metabolism |
| 2014 | Medium | Bioinformatic structural analysis reveals that BIG3's Sec7 domain lacks the conserved critical glutamate residue required for GEF activity, suggesting BIG3 has no guanine nucleotide-exchange factor activity. BIG3 is predicted to adopt an armadillo (ARM)-type α-helical repeat structure that mediates interaction with PHB2, and this interaction site was subsequently verified experimentally. | PMID:24997568 | BMC research notes |
| 2015 | Medium | BIG3 blocks the estrogen-dependent nuclear import of PHB2 by interfering with PHB2 binding to karyopherin-alpha family members (KPNA1, KPNA5, KPNA6). PHB2 interacts with KPNA1, KPNA5, and KPNA6 to enable E2-dependent nuclear translocation, and siRNA knockdown of each KPNA inhibits PHB2 translocation even in BIG3-depleted cells. | PMID:26052702 | PloS one |
| 2015 | Medium | PHB2 released from BIG3 by ERAP disrupts interactions between membrane-associated ERα and growth factor receptors (IGF-1Rβ, EGFR, PI3K, HER2), inhibiting their activation and reducing Akt, MAPK, and ERα phosphorylation, thereby suppressing crosstalk between estrogen and growth factor signaling associated with tamoxifen resistance. | PMID:25736224 | Cancer science |
| 2015 | Medium | BIG3 is highly expressed in pancreatic alpha-cells in addition to beta-cells. Depletion of BIG3 in alpha-cells leads to elevated glucagon production and secretion, and BIG3-knockout mice display increased glucagon release under hypoglycemic conditions, indicating a conserved role for BIG3 in negatively regulating hormone secretory granule biogenesis in both alpha and beta cells. | PMID:25737957 | Molecular metabolism |
| 2017 | High | BIG3 functions as an A-kinase anchoring protein (AKAP) that simultaneously binds PKA and the alpha isoform of the catalytic subunit of PP1 (PP1Cα). E2-induced PKA-mediated phosphorylation of BIG3-S305 and BIG3-S1208 enhances PP1Cα activity, which dephosphorylates PHB2-S39, inactivating PHB2 and thereby activating E2/ERα signaling in breast cancer cells. | PMID:28555617 | Nature communications |
| 2019 | Medium | Biophysical characterization shows that a non-conserved loop region unique to BIG3 (not present in BIG1/BIG2 paralogs) significantly affects the colloidal and thermodynamic stability of BIG3 protein and the thermodynamic and kinetic profile of its interaction with PHB2. | PMID:31421830 | Biochemical and biophysical research communications |
| 2021 | Medium | In osteosarcoma (OS) cells, the BIG3-PHB2 complex localizes predominantly to mitochondria (distinct from its cytoplasmic localization in breast cancer cells). Disruption of the BIG3-PHB2 complex causes G2/M-phase arrest and induces apoptosis via PARP-1/AIF pathway activation, and downregulates inner mitochondrial membrane protein complex activity. | PMID:34363714 | Cancer science |
| 2003 | Medium | BIG3/BIG-3 (ARFGEF3) protein levels increase during chondrocyte differentiation and in response to BMP-2 treatment. Stable expression of BIG-3 in ATDC5 cells accelerates matrix proteoglycan synthesis, increases alkaline phosphatase and osteopontin mRNA, and promotes mineralized matrix formation, demonstrating a functional role in chondrocyte differentiation. | PMID:14657013 | Endocrinology |
| 2004 | Medium | BIG-3 (ARFGEF3) accelerates osteoblast differentiation in MC3T3-E1 cells by inducing phosphorylation and nuclear translocation of Smad1 independently of endogenously produced BMPs. Noggin treatment (BMP inhibition) inhibited differentiation markers in control cells but not in BIG-3-overexpressing cells, and BIG-3 expression prevented noggin-induced reduction in phosphoSmad1 nuclear localization. | PMID:15707593 | Experimental cell research |
| 2025 | Medium | Arfgef3 knockout in mice ameliorates ischemia-reperfusion-induced acute kidney injury by improving mitochondrial function, reducing mitochondrial biogenesis marker dysregulation, restoring ATP production capacity, and attenuating renal inflammation, oxidative stress, and apoptosis. | PMID:41087303 | Renal failure |

## Citations

- PMID:14657013
- PMID:15707593
- PMID:19496786
- PMID:24051437
- PMID:24711543
- PMID:24997568
- PMID:25139048
- PMID:25736224
- PMID:25737957
- PMID:26052702
- PMID:28555617
- PMID:31421830
- PMID:34363714
- PMID:41087303
