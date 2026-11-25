---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARFRP1
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q13795
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 15
citation_count: 15
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARFRP1 (human)

## Current model (mechanistic narrative)

ARFRP1 is a trans-Golgi/TGN-localized ARF-like GTPase that acts as a master regulator of membrane trafficking by initiating a bifurcated GTPase cascade at the TGN [PMID:16129887, PMID:31575603]. Its Golgi targeting is intrinsic and GTP-independent: an N-terminal amphipathic helix is sufficient to specify Golgi localization, requires N-terminal acetylation (mediated by hNaa30) and binding to Sys1, and when swapped onto an endosomal GTPase redirects that protein to the Golgi [PMID:28356483, PMID:32972971]. Once at the TGN, GTP-bound ARFRP1 recruits the downstream GTPases ARL1 and ARL5, which respectively recruit GRIP-domain golgins (golgin-97, golgin-245) for carrier capture and the GARP complex for SNARE-mediated tethering, coordinating retrograde delivery of cargoes such as Shiga toxin and TGN38 to the TGN [PMID:16129887, PMID:17127620, PMID:31575603]. In parallel, ARFRP1 directs anterograde export from the TGN, controlling surface delivery of VSV-G and E-cadherin and assembling with the E-cadherin/catenin adhesion complex [PMID:18662990, PMID:19224922]. Across tissues this trafficking function underlies metabolic cargo sorting: ARFRP1 governs lipid droplet growth and SNAP23/lipolytic enzyme distribution in adipocytes, intracellular sequestration of GLUT4, chylomicron and VLDL lipidation in intestine and liver via an ARL1-Golgin-245-Rab2 axis, hepatic IGF1 secretion and GLUT2 sorting, and SNAP25-dependent insulin secretion through interaction with GOPC [PMID:20038528, PMID:20230794, PMID:22505585, PMID:22927645, PMID:24186947, PMID:33359402]. No disease-causing human mutation is documented in this corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0003924 GTPase activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005794 Golgi apparatus
- **pathway (Reactome):** R-HSA-5653656 Vesicle-mediated transport, R-HSA-9609507 Protein localization, R-HSA-1430728 Metabolism
- **partners:** ARL1, ARL5, SYS1, GOPC, CDH1, NAA30, JTB
- **complexes:** E-cadherin/catenin complex, SYS1-ARFRP1 (Golgi targeting)

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2005 | High | ARFRP1 is associated mainly with the trans-Golgi compartment and TGN, and is an essential regulatory factor for targeting of ARL1 and GRIP domain-containing proteins (golgin-97 and golgin-245) onto Golgi membranes. In concert with ARL1 and GRIP proteins, ARFRP1 is implicated in Golgi-to-plasma membrane transport of VSV-G protein and in retrograde transport of TGN38 and Shiga toxin from endosomes to the TGN. | PMID:16129887 | Journal of cell science |
| 2006 | High | GTP-bound ARFRP1 (Q79L mutant) associates with Golgi membranes and co-localizes with ARL1, while the GDP-locked ARFRP1 (T31N mutant) clusters in the cytosol. ARFRP1-T31N or RNAi depletion disrupts Golgi association of ARL1 and Golgin-245 and alters distribution of TGN marker syntaxin 6, without affecting GM130 or giantin. In Arfrp1-/- embryos, ARL1 dislocates from Golgi membranes. | PMID:17127620 | Molecular membrane biology |
| 2008 | High | ARFRP1 is required for trans-Golgi to plasma membrane trafficking of E-cadherin. In Arfrp1-/- embryos and intestine-specific knockout enterocytes, E-cadherin is mistargeted to intracellular compartments. ARFRP1 co-immunoprecipitates in a complex with E-cadherin, alpha-catenin, beta-catenin, gamma-catenin, and p120ctn from MDCK cells stably expressing myc-ARFRP1. RNAi depletion of ARFRP1 in HeLa cells dislocates E-cadherin from the cell surface. | PMID:18662990 | The Journal of biological chemistry |
| 2009 | Medium | ARFRP1 and ARL1 have differential roles at the TGN: ARL1 specifically regulates retrograde transport of Shiga toxin to the TGN, while ARFRP1 specifically regulates anterograde transport of VSVG from the TGN. A SNARE complex containing Vti1a, syntaxin 6, and syntaxin 16 is involved in Shiga toxin transport downstream of ARL1. | PMID:19224922 | The Journal of biological chemistry |
| 2009 | High | ARFRP1 is essential for lipid droplet growth in adipocytes. Adipocyte-specific Arfrp1 knockout mice are lipodystrophic with smaller lipid droplets and disturbed interaction of small lipid-loaded particles with larger droplets. SNAP23 is mislocalized to the cytosol in Arfrp1-/- adipocytes (normally associated with small lipid droplets). Levels of phosphorylated HSL are elevated and ATGL association with lipid droplets is enhanced in Arfrp1-/- brown adipose tissue. Knockdown of Arfrp1 in 3T3-L1 adipocytes increases basal lipolysis. | PMID:20038528 | Molecular and cellular biology |
| 2010 | Medium | ARFRP1 is involved in sorting of GLUT4 in adipocytes. In adipocyte-specific Arfrp1 knockout mice, GLUT4 accumulates at the plasma membrane rather than being sequestered in an intracellular insulin-responsive storage compartment. siRNA-mediated knockdown of Arfrp1 in 3T3-L1 adipocytes produces similar GLUT4 missorting with elevated basal deoxyglucose uptake. Arfrp1 knockout adipocytes exhibit an abnormal trans-Golgi morphology. | PMID:20230794 | Biochemical and biophysical research communications |
| 2012 | High | ARFRP1 controls the lipidation and assembly of chylomicrons in intestinal epithelium. Intestine-specific Arfrp1 knockout enterocytes absorb fatty acids normally but secrete chylomicrons with markedly reduced triacylglycerol content. ApoA-I accumulates in Arfrp1-/- epithelium, co-localizing with Rab2. Suppression of Rab2, ARL1, and Golgin-245 reduces chylomicron release from Caco-2 cells, placing ARFRP1 upstream of ARL1-Golgin-245-Rab2 in chylomicron lipidation. | PMID:22505585 | Human molecular genetics |
| 2012 | High | Liver-specific knockout of Arfrp1 results in reduced hepatic IGF1 secretion (but not IGFBP2 secretion) and intracellular retention of GLUT2, leading to decreased hepatic glucose uptake and reduced glycogen stores. Suppression of Arfrp1 in primary hepatocytes reduces IGF1 release. ARFRP1 thus controls selective protein sorting/secretion at the trans-Golgi in hepatocytes. | PMID:22927645 | Molecular and cellular biology |
| 2013 | High | Hepatocyte-specific deletion of Arfrp1 impairs VLDL lipidation, leading to reduced plasma triglyceride levels and accumulation of ApoC3 in liver. Fractionation reveals more ApoB48 and lower triglycerides in Golgi compartments of Arfrp1-/- livers, indicating ARFRP1 is required for lipidation and assembly of proteins onto lipid particles in the Golgi during VLDL maturation. | PMID:24186947 | Journal of lipid research |
| 2017 | Medium | ARFRP1 requires N-terminal acetylation for proper membrane association and Golgi localization. Depletion of the N-terminal acetyltransferase hNaa30 causes ARFRP1 to shift from predominantly cis-Golgi/TGN localization to aberrant Golgi and non-Golgi vesicular structures, though membrane association is not completely lost. | PMID:28356483 | Bioscience reports |
| 2019 | High | ARFRP1 functions as a master regulator upstream of ARL1 and ARL5 at the TGN. ARFRP1 coordinates recruitment of two distinct tethering factors: ARL1 recruits golgins (long-distance carrier capture), while ARL5 recruits the GARP complex (SNARE assembly). This bifurcated GTPase cascade is essential for retrograde cargo delivery to the TGN. | PMID:31575603 | The Journal of cell biology |
| 2020 | High | The N-terminal amphipathic helix of ARFRP1 is sufficient to determine its Golgi localization, and is required for its binding partner Sys1. Exchanging the amphipathic helix between ARFRP1 (Golgi-localized) and Arl14 (endosome/plasma membrane-localized) switches their localizations. Residues required for N-terminal acetylation of the ARFRP1 helix are important for specific Golgi localization. ARFRP1 is recruited to Golgi independently of GTP binding. | PMID:32972971 | The Journal of biological chemistry |
| 2020 | High | ARFRP1 interacts with the Golgi-associated PDZ and coiled-coil motif-containing protein GOPC at the TGN. Both ARFRP1 and GOPC regulate plasma membrane localization of the SNARE protein SNAP25 and control first and second phase insulin secretion from pancreatic β-cells. Downregulation of GOPC or ARFRP1 in Min6 cells impairs SNAP25 plasma membrane localization and enhances SNAP25 degradation. Overexpression of SNAP25 or GOPC restores insulin secretion in β-cell-specific Arfrp1 knockout islets. | PMID:33359402 | Molecular metabolism |
| 2024 | Medium | ARFRP1 participates in an ARFRP1/AP-1-dependent pathway allowing Golgi-to-lysosome trafficking of SARS-CoV-2 Envelope protein. This pathway was identified by proximity biotinylation of tagged Envelope protein. | PMID:38569033 | Science advances |
| 2025 | Low | A complex involving SYS1, JTB, and ARFRP1 was predicted computationally and validated experimentally, suggesting JTB participates in Golgi trafficking alongside ARFRP1. | PMID:bio_10.1101_2025.09.09.675133 | bioRxiv |

## Citations

- PMID:16129887
- PMID:17127620
- PMID:18662990
- PMID:19224922
- PMID:20038528
- PMID:20230794
- PMID:22505585
- PMID:22927645
- PMID:24186947
- PMID:28356483
- PMID:31575603
- PMID:32972971
- PMID:33359402
- PMID:38569033
- PMID:bio_10.1101_2025.09.09.675133
