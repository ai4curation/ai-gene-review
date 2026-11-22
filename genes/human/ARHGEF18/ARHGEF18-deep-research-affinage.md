---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARHGEF18
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q6ZSZ5
self_evaluation_pairwise: tie
faith_pct: 100.0
n_discoveries: 15
citation_count: 14
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARHGEF18 (human)

## Current model (mechanistic narrative)

ARHGEF18 (p114RhoGEF) is a Dbl-family guanine nucleotide exchange factor that drives spatially restricted RhoA activation at epithelial and endothelial cell junctions to organize cortical actomyosin, control apicobasal polarity, and maintain barrier integrity [PMID:21258369, PMID:23698346]. Through its DH/PH catalytic module it activates RhoA (and Rac1, but not Cdc42), and a patient-derived DH-domain missense variant that weakens RHOA binding establishes this domain as essential for exchange activity [PMID:14512443, PMID:28132693]. Once active, it signals predominantly through a ROCK–myosin II axis: at cell-cell contacts it stimulates myosin light chain double phosphorylation to power collective epithelial migration and amoeboid invasion, and it acts upstream of ROCK2 and myosin IIA to control apical junction assembly, circumferential actomyosin belt formation, retinal neuroepithelial polarity, and lumen consolidation during tubulogenesis [PMID:23698346, PMID:23185572, PMID:26483385, PMID:26217016]. Its junctional recruitment and activation are governed by multiple upstream inputs, including heterotrimeric G-protein subunits Gβγ and Gα12, the FERM protein Lulu2 (antagonized by aPKC phosphorylation) with PDZ-mediated recruitment by Patj, LKB1, the CRB3A–Ehm2 polarity module, and the Wnt effectors Dishevelled and Daam1 [PMID:14512443, PMID:22006950, PMID:23648482, PMID:20810787, PMID:26217016, PMID:31051012]. Beyond epithelia, ARHGEF18 supports endothelial mechanotransduction, where shear-stress-dependent phosphorylation directs its association with tight junctions to maintain the vascular barrier, drives PKA/CREB-coupled actomyosin remodeling required for trophoblast fusion, and is activated by an isoform-specific SEPTIN9 interaction at mitochondrial fission sites to promote calcium influx and inner-membrane constriction [PMID:33842485, PMID:40920138, PMID:39977269].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity
- **localization:** GO:0005886 plasma membrane, GO:0005856 cytoskeleton, GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-1500931 Cell-Cell communication, R-HSA-1266738 Developmental Biology
- **partners:** RHOA, ROCK2, CGN, LLGL2, PATJ, STK11, CRB3, SEPTIN9
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2011 | High | p114RhoGEF (ARHGEF18) is a junction-associated protein that drives spatially restricted RhoA activation at epithelial junctions; it associates with a complex containing myosin II, ROCK II, and the junctional adaptor cingulin, and its depletion abolishes junction-associated RhoA activation while stimulating non-junctional Rho signaling and basal myosin phosphorylation. | PMID:21258369 | Nature cell biology |
| 2003 | High | Gβγ subunits of heterotrimeric G proteins directly interact with the DH/PH domain of p114RhoGEF and stimulate its guanine nucleotide exchange activity toward RhoA and Rac1 (but not Cdc42), leading to actin stress fiber formation, cell rounding, and NADPH oxidase-dependent ROS production. | PMID:14512443 | Circulation research |
| 2011 | High | Lulu2 (a FERM-domain protein) directly interacts with and activates p114RhoGEF at apical cell-cell junctions to regulate the circumferential actomyosin belt; this interaction is negatively regulated by aPKC-mediated phosphorylation of the FERM-adjacent domain of Lulu2. Additionally, Patj recruits p114RhoGEF to apical junctions via PDZ domain-mediated interaction. | PMID:22006950 | The Journal of cell biology |
| 2013 | Medium | LKB1 interacts with p114RhoGEF in a kinase-activity-independent manner and together they control RhoA activity to promote apical junction assembly in human bronchial epithelial cells. | PMID:23648482 | Molecular and cellular biology |
| 2010 | Medium | p114-RhoGEF binds to Dishevelled (Dvl) and Daam1 and is required for Wnt-3a/Dvl-induced RhoA activation and neurite retraction in neuroblastoma cells; shRNA-mediated depletion of p114-RhoGEF suppresses Dvl-induced neurite retraction and RhoA activation, and overexpression of the Dvl-binding domain of p114-RhoGEF acts as a dominant negative. | PMID:20810787 | Molecular biology of the cell |
| 2013 | High | ArhGEF18-mediated RhoA activation signals through Rock2 to maintain apicobasal polarity, tight junction localization, cortical actin organization, and control of neurogenic vs. proliferative cell divisions in the vertebrate retinal neuroepithelium; human ARHGEF18 rescues the medaka arhgef18 mutant phenotype. | PMID:23698346 | Development (Cambridge, England) |
| 2012 | Medium | p114RhoGEF drives cortical myosin activation specifically by stimulating myosin light chain double phosphorylation at cell-cell contacts, promoting collective epithelial cell migration and amoeboid-like tumor cell invasion on Matrigel; depletion reduces RhoA but increases Rac activity. | PMID:23185572 | PloS one |
| 2015 | Medium | p114RhoGEF controls later stages of tubulogenesis (lumen consolidation) through a ROCK–myosin IIA pathway; knockdown causes multiple lumens per tube, and inhibition of ROCK or myosin IIA phenocopies this, with live imaging showing that cell movement required for lumen consolidation is blocked. | PMID:26483385 | Journal of cell science |
| 2015 | Medium | CRB3A recruits p114RhoGEF and its activator Ehm2 to the cell periphery via both cytoplasmic tail motifs, increasing RhoA activation; ROCK1/2 act downstream to remodel the cytoskeleton into a circumferential actomyosin belt and change cell morphology. | PMID:26217016 | Molecular and cellular biology |
| 2016 | Medium | p114RhoGEF contains a C-terminal region that specifically binds Gα12 (but not Gα13); charge-reversal mutagenesis of conserved residues disrupts this interaction. This region is distinct from the RH domain interface used by other RhoGEFs, and Gα12 dominant-negative suppresses serum-mediated signaling to p114RhoGEF in cells. | PMID:31051012 | Journal of molecular signaling |
| 2021 | Medium | ARHGEF18/p114RhoGEF is required for syncytiotrophoblast differentiation and placenta development; it controls expression of AKAP12 (a PKA scaffold), is required for PKA-induced actomyosin remodeling, and enables CREB-driven transcription of fusogenic proteins, thereby linking actomyosin dynamics and cell-cell junctions to PKA/CREB signaling and trophoblast cell-cell fusion. | PMID:33842485 | Frontiers in cell and developmental biology |
| 2025 | Medium | SEPTIN9 is present at mitochondrial fission sites from early stages and activates ARHGEF18 through an isoform-specific N-terminal interaction; loss of SEPTIN9 impairs mitochondrial calcium influx, placing SEPTIN9–ARHGEF18 upstream of calcium flux and inner membrane constriction during early mitochondrial fission. | PMID:40920138 | The Journal of cell biology |
| 2025 | Medium | ARHGEF18 phosphorylation is modulated by shear stress magnitude in endothelial cells; when phosphorylated, ARHGEF18 interacts with tight junctions and is required for EC elongation, alignment, migration, tight junction formation, and maintenance of the endothelial barrier and vascular permeability in vivo. | PMID:39977269 | Cell reports |
| 2017 | Low | A missense variant p.Thr270Ala in the DBL homology (DH) domain of ARHGEF18 reduces its ability to interact with and activate RHOA, functionally validating the DH domain as essential for RHOA activation by ARHGEF18. | PMID:28132693 | American journal of human genetics |
| 2025 | Medium | Arhgef18 associates with the retinal outer limiting membrane (OLM) adherens junctions between Müller glia and photoreceptors; Müller glia-specific knockout causes OLM disruption, retinal rosette formation, progressive degeneration, and vascular leakage. In cultured Müller cells, p114RhoGEF depletion disrupts junctional OLM protein recruitment and activates NF-κB, β-catenin, and TBK1 signaling while reducing mitochondrial activity; TBK1 inhibition or nicotinamide rescues mitochondrial activity and suppresses these signaling pathways. | — | bioRxiv |

## Citations

- PMID:14512443
- PMID:20810787
- PMID:21258369
- PMID:22006950
- PMID:23185572
- PMID:23648482
- PMID:23698346
- PMID:26217016
- PMID:26483385
- PMID:28132693
- PMID:31051012
- PMID:33842485
- PMID:39977269
- PMID:40920138
