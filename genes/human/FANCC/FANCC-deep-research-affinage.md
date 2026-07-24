---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/FANCC
affinage_run_date: 2026-06-09T23:54:43
uniprot_accession: Q00597
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 34
citation_count: 34
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for FANCC (human)

## Current model (mechanistic narrative)

FANCC encodes a ~60-kDa protein with dual roles in genome maintenance and cytoprotection, originally defined as a Fanconi anemia gene required for cellular resistance to DNA interstrand cross-linking agents [PMID:8499901, PMID:7517562]. As part of a nuclear FA core complex, FANCC assembles with FANCA, FANCG, FANCF, and FANCE in a series of interdependent interactions: FANCA-FANCC binding [PMID:9398857], FANCG-bridged complex formation [PMID:10373536], FANCF incorporation [PMID:11063725], and FANCE-mediated linkage of FANCC to the substrate FANCD2 [PMID:16127171]; phosphorylation-dependent nuclear accumulation of this complex defines a common pathway disrupted across multiple FA complementation groups [PMID:9789045]. This assembly is required for FANCD2 monoubiquitination, and its loss abrogates that modification, elevates spontaneous chromosomal breakage, and confers selective sensitivity to cross-linking agents [PMID:16762635]. Downstream, FANCC promotes homologous recombination and error-prone repair of abasic sites, suppresses sister chromatid exchange, and acts in concert with BLM helicase to maintain genome stability [PMID:15327776, PMID:15616572], operating in parallel pathways with BRCA2 and HELQ [PMID:16687415, PMID:24005041]. Independently of the core complex, cytoplasmic FANCC exerts anti-apoptotic functions essential for hematopoietic progenitor survival [PMID:8621788, PMID:8977247]: it binds Hsp70 to form a ternary complex that inhibits the pro-apoptotic kinase PKR [PMID:11500375, PMID:12397061], binds non-phosphorylated STAT1 to facilitate its docking and activation at the IFN-gamma receptor [PMID:10848598], and attenuates NADPH cytochrome P450 reductase activity [PMID:9787138]. Patient-derived mutant FANCC (L554P) loses both core-complex (FANCA, cdc2) and signaling (STAT1) interactions [PMID:9398857, PMID:9242535, PMID:10848598].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity, GO:0003677 DNA binding
- **localization:** GO:0005829 cytosol, GO:0005634 nucleus
- **pathway (Reactome):** R-HSA-73894 DNA Repair, R-HSA-5357801 Programmed Cell Death, R-HSA-162582 Signal Transduction, R-HSA-9612973 Autophagy, R-HSA-1474165 Reproduction
- **partners:** FANCA, FANCG, FANCF, FANCE, HSPA1A, STAT1, EIF2AK2, POR
- **complexes:** Fanconi anemia core complex (FANCA-FANCC-FANCE-FANCF-FANCG), FANCC-FANCE-FANCD2 ternary complex, FANCC-Hsp70-PKR ternary complex, FANCC-FANCE-FANCF anti-crossover subcomplex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1994 | High | The FACC polypeptide localizes predominantly to the cytoplasm, as determined by cell fractionation and immunofluorescence; it is a 60-kDa protein, and FA group C cell lines express full-length, truncated, or no detectable FACC polypeptide. Two FACC-related proteins (FRP-50 and FRP-150) were also co-immunoprecipitated. | PMID:7517562 | Proceedings of the National Academy of Sciences of the United States of America |
| 1996 | High | Cytoplasmic localization of the FAC protein is essential for its functional activity: cytoplasmic isoforms of FAC corrected both the DNA cross-linking defect and enhanced cytotoxicity in FA group C cells, whereas a nucleus-targeted isoform did not correct these phenotypes. | PMID:8621788 | The Journal of clinical investigation |
| 1997 | High | FAA (FANCA) and FAC (FANCC) proteins bind each other and form a complex. While unbound FAA and FAC are predominantly cytoplasmic, the FAA-FAC complex is found in both cytoplasm and nucleus. A patient-derived mutant FAC (L554P) fails to bind FAA. | PMID:9398857 | Nature genetics |
| 1997 | Medium | The FAC protein coimmunoprecipitates with the cyclin-dependent kinase cdc2. FAC expression increases during S phase, peaks at G2/M transition, and declines during M phase. The L554P patient-derived mutant FAC fails to bind cdc2, and the cdc2-binding region maps to the carboxyl-terminal 50 amino acids of FAC. | PMID:9242535 | Blood |
| 1997 | Medium | FA-C lymphoblasts treated with low-dose MMC exhibit prolonged G2/M arrest associated with sustained inactivation of the cyclin B1/cdc2 kinase complex (sustained cyclin B1 accumulation and cdc2 tyrosine phosphorylation), whereas FAC-corrected cells show only transient inactivation. This implicates FAC in a cross-link damage avoidance pathway that signals to the cyclin B/cdc2 kinase. | PMID:9187128 | Cancer research |
| 1998 | Medium | FAC protein binds to NADPH cytochrome P450 reductase (RED) in COS-1 and murine liver cells. This interaction requires the amino-terminal region of FAC and the cytosolic FMN-binding domain of RED. FAC expression suppresses RED-mediated reduction of cytochrome c, indicating FAC attenuates RED enzymatic activity. | PMID:9787138 | Blood |
| 1998 | High | Functional activity of FANCA requires both FAC binding and nuclear localization. Mutation/deletion of the FANCA NLS abolishes FAC binding and nuclear localization; wild-type FAC promotes nuclear accumulation of FAA, and FAA promotes nuclear accumulation of FAC. Mutant FAA forms that fail to bind FAC also fail to support nuclear FAC accumulation. | PMID:9742112 | Molecular and cellular biology |
| 1998 | Medium | FAA and FAC protect against cross-linker cytotoxicity from different subcellular compartments: nuclear localization of FAA is necessary and sufficient to correct MMC sensitivity in FA-A cells, whereas cytoplasmic FAC is required for its activity. No interaction between FAA and FAC was detected either in vivo or in vitro in this study. | PMID:9746759 | Blood |
| 1998 | Medium | The FAA/FAC protein complex undergoes nuclear accumulation in a phosphorylation-dependent manner. FA cells from complementation groups A, B, C, E, F, G, and H are all defective in FAA/FAC complex formation, FAA phosphorylation, and nuclear accumulation of the complex, defining a common FA signaling pathway. | PMID:9789045 | Proceedings of the National Academy of Sciences of the United States of America |
| 1999 | High | FANCG/XRCC9 is required for binding of FANCA and FANCC proteins. FANCG is a component of the nuclear FANCA-FANCC complex. The amino-terminal region of FANCA is required for FANCG binding, FANCC binding, nuclear localization, and functional activity. Disruption of this tripartite complex results in the FA cellular phenotype. | PMID:10373536 | Molecular and cellular biology |
| 1999 | Medium | Human alpha spectrin II (alphaSpIISigma*) forms a nuclear complex with FANCA and FANCC. Levels of alphaSpIISigma* are reduced in FA-A, FA-B, FA-C, and FA-D cells, suggesting FA proteins contribute to its stability/expression in the nucleus. | PMID:10551855 | The Journal of biological chemistry |
| 2000 | High | FANCF forms a nuclear complex with FANCA, FANCC, and FANCG in human lymphoblasts. FANCF is predominantly nuclear. These interactions require each of the FA proteins (A, C, F, G) except FANCD. Loss of any single FA protein (except D) disrupts the nuclear complex. | PMID:11063725 | Human molecular genetics |
| 2000 | High | FANCC binds STAT1 (preferentially non-phosphorylated STAT1) and facilitates its docking at the IFN-gamma receptor alpha chain, enabling STAT1 phosphorylation. GST-fusion FANCC, but not mutant FANCC (L554P), binds STAT1 in cell lysates. Loss of FANCC results in defective STAT1 docking at the IFN-gammaR, corrected by FANCC transduction. | PMID:10848598 | Molecular and cellular biology |
| 2000 | Medium | FANCC protein expression is regulated posttranscriptionally in a cell cycle-dependent manner: FANCC protein is lowest at G1/S and highest in M phase, while mRNA levels are constant throughout the cell cycle. This regulation is proteasome-dependent and is encoded within the FANCC coding sequence. | PMID:10845936 | Blood |
| 2001 | High | FANCC interacts with the molecular chaperone Hsp70 via the ATPase domain of Hsp70 and the central 320 residues of FANCC; both Hsp40 and ATP/ADP are required. This FANCC-Hsp70 interaction protects hematopoietic cells from IFN-gamma/TNF-alpha-induced cytotoxicity. Alanine mutations in the Hsp70-interacting domain of FANCC block both Hsp70 binding and cytoprotection. | PMID:11500375 | The EMBO journal |
| 2001 | Medium | FANCA, FANCC, and FANCG proteins bind to DNA containing psoralen interstrand cross-links, as shown by DNA affinity chromatography from HeLa cell nuclear extracts. | PMID:11401546 | Biochemistry |
| 2002 | High | FANCC inhibits PKR (double-stranded RNA-dependent protein kinase) activity both in vivo and in vitro; this requires a physical interaction between FANCC and Hsp70, but not interactions with other Fanconi proteins. FANCC, Hsp70, and PKR form a ternary complex in lymphoblasts and in yeast expressing PKR. FANCC can exert this anti-apoptotic function independently of the FA multiprotein complex. | PMID:12397061 | The Journal of biological chemistry |
| 2002 | High | FANCE promotes nuclear accumulation of FANCC and is required for FANCA-FANCC complex formation, FANCD2 monoubiquitination, and FANCD2 nuclear foci formation. HA-tagged FANCE coimmunoprecipitates with FANCA, FANCC, and FANCG but not FANCD2 in normal cells. | PMID:12239156 | Blood |
| 2004 | High | FANCC promotes homologous recombination (HR) repair and also facilitates error-prone repair of endogenously generated abasic sites (via translesion synthesis/mutagenic repair). Efficient repair of cross-links in DT40 cells requires combined functions of FANCC, translesion synthesis, and HR. Loss of FANCC elevates spontaneous sister chromatid exchange (SCE) approximately 2-fold. | PMID:15327776 | Molecular cell |
| 2004 | High | FANCC deficiency in DT40 cells elevates spontaneous SCE ~2-fold, requiring XRCC3 (HR factor). FANCC loss combined with RAD18 loss (TLS) yields more SCE than either single mutant (non-epistatic). FANCC is functionally linked to BLM helicase: the fancc/blm double mutant has similar SCE to blm alone, and MMC-induced BLM nuclear foci formation is severely reduced in fancc or fancd2 cells. | PMID:15616572 | The EMBO journal |
| 2005 | High | FANCC, FANCE, and FANCD2 form a ternary complex: FANCE mediates the interaction between FANCC and FANCD2. FANCE mutants that interact with FANCC but not FANCD2 abrogate FANCD2 monoubiquitination and fail to complement FA-E cells. FANCE also mediates the interaction between FANCC and FANCF within the core complex. | PMID:16127171 | The Journal of biological chemistry |
| 2006 | Medium | FANCC disruption abrogates FANCD2 monoubiquitination, confirming impaired FA pathway function. FANCC-deficient cancer cells show increased G2/M arrest and clastogenic damage in response to DNA interstrand cross-linking agents, but not gemcitabine, etoposide, or hydrogen peroxide. FANCC disruption also increases spontaneous chromosomal breakage. | PMID:16762635 | Gastroenterology |
| 2006 | Medium | FANCE nuclear accumulation depends specifically on FANCC: other FA proteins are not involved in FANCE nuclear localization. The FANCE region interacting with FANCC is distinct from the region binding FANCD2, supporting a model where FANCE recruits FANCD2 to the core complex independently of FANCC binding. | PMID:16513431 | DNA repair |
| 2006 | Medium | Epistasis analysis in DT40 cells shows FANCC (FA core complex) and BRCA2 CTD are epistatic for X-ray sensitivity, but FANCC and BRCA2 CTD act in parallel pathways for interstrand cross-link repair. BRCA2-dependent Rad51 chromatin loading after MMC is not compromised by loss of FANCC or FANCD2. | PMID:16687415 | The Journal of biological chemistry |
| 2009 | Medium | FANCC suppresses telomere sister chromatid exchange (T-SCE) specifically when telomeres are short: Fancc deficiency increases T-SCE incidence in mice crossed into a short-telomere background (Tert+/- or Tert-/-), but not in mice with long telomeres. Fancc deficiency also accelerates telomere attrition during high-turnover hematopoietic cell transplantation. | PMID:20022886 | Human molecular genetics |
| 2013 | Medium | HELQ operates in parallel to (non-epistatic with) FANCC for suppression of spontaneous chromosome instability: Helq/Fancc double mutant mice show substantially worse phenotypes (micronuclei, 53BP1 nuclear bodies) than either single mutant. Unlike Fancc-/- cells, Helq mutant cells retain intact FANCD2 monoubiquitination and focus formation. | PMID:24005041 | Nucleic acids research |
| 2014 | Medium | Combined loss of dormant replication origins (Mcm4chaos3) and FANCC results in synergistic increases in stalled/collapsed replication fork markers and genome instability beyond either single mutant, identifying an important functional overlap between dormant origins and the FA pathway in maintaining fork progression. | PMID:24589582 | Nucleic acids research |
| 2020 | Medium | ZIKV downregulates FANCC (via suppression of transcription factor E2F4) to evade selective autophagy and enhance viral replication. FANCC is essential for selective autophagy and acts as a negative regulator of ZIKV replication; Fancc KO mice show increased ZIKV infection. | PMID:33073500 | EMBO reports |
| 2022 | Medium | FANCC deficiency promotes microglial pyroptosis via the p38/NLRP3 pathway, leading to secondary neuronal apoptosis in spinal cord injury. Overexpression of FANCC suppresses microglial pyroptosis and neuronal apoptosis; knockdown worsens both outcomes. | PMID:35659106 | Cell & bioscience |
| 2023 | Medium | The FANCC-FANCE-FANCF subcomplex is evolutionarily conserved from vertebrates to plants and functions as an anti-crossover factor during meiotic recombination. Loss of FANCC, FANCE, or FANCF partially rescues CO-defective mutants; FANCC/FANCE/FANCF mutations cause synthetic meiotic catastrophe with the pro-CO factor MUS81. | PMID:36652992 | Nucleic acids research |
| 1996 | Medium | FAC protein expression suppresses apoptosis induced by growth factor withdrawal in hematopoietic factor-dependent progenitor cell lines (32D and MO7e), promoting increased viability rather than proliferation, consistent with an anti-apoptotic function analogous to Bcl-2. | PMID:8977247 | Blood |
| 1996 | Medium | Antisense oligonucleotide-mediated repression of FACC gene expression in normal human bone marrow cells inhibits clonal growth of erythroid and granulocyte-macrophage progenitors in a sequence-specific fashion, establishing a direct role for FACC in hematopoietic progenitor cell growth/survival. | PMID:7518843 | The Journal of clinical investigation |
| 2004 | Medium | Type I IFN-induced activation of STAT1, STAT3, and STAT5, as well as TYK2 and JAK1 phosphorylation, is impaired in FA-C cells bearing FANCC-inactivating mutations. This is accompanied by reduced Th1 (IFN-gamma-producing CD4+) differentiation in Fancc null mice. | PMID:15356134 | Journal of immunology |
| 1993 | Medium | A leucine-to-proline substitution at codon 554 (L554P) completely abolishes FACC protein functional complementing activity, confirming that FACC encodes a ~60 kDa protein required for resistance to DNA cross-linking agents. | PMID:8499901 | Human molecular genetics |

## Citations

- PMID:10373536
- PMID:10551855
- PMID:10845936
- PMID:10848598
- PMID:11063725
- PMID:11401546
- PMID:11500375
- PMID:12239156
- PMID:12397061
- PMID:15327776
- PMID:15356134
- PMID:15616572
- PMID:16127171
- PMID:16513431
- PMID:16687415
- PMID:16762635
- PMID:20022886
- PMID:24005041
- PMID:24589582
- PMID:33073500
- PMID:35659106
- PMID:36652992
- PMID:7517562
- PMID:7518843
- PMID:8499901
- PMID:8621788
- PMID:8977247
- PMID:9187128
- PMID:9242535
- PMID:9398857
- PMID:9742112
- PMID:9746759
- PMID:9787138
- PMID:9789045
