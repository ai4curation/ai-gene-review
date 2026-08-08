---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ADPRH
affinage_run_date: 2026-06-09T22:02:42
uniprot_accession: P54922
self_evaluation_pairwise: tie
faith_pct: 100.0
n_discoveries: 14
citation_count: 14
gates_passed: False
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for ADPRH (human)

> ⚠️ **CAUTION — trust gate(s) tripped; review before using:**
>
> - Affinage's own head-to-head self-evaluation scored this record `pairwise = tie` (not `win`) vs the curated UniProt reference — treat the narrative with extra scepticism.

## Current model (mechanistic narrative)

ADPRH (ARH1) is a cytosolic, ubiquitously expressed enzyme that reverses arginine-specific mono-ADP-ribosylation by hydrolyzing the N-glycosidic ADP-ribose–arginine bond on modified proteins, regenerating unmodified protein and releasing free ADP-ribose [PMID:16278211, PMID:36497109]. Catalysis requires vicinal acidic active-site residues and is enhanced by Mg2+, with crystallographic analysis showing that ARH1 binds K+ as a structural ion and that its adenosine-ribose binding diverges from the related ARH3 to dictate distinct substrate specificity [PMID:16278211, PMID:19407395, PMID:30472116]. Beyond protein substrates, ARH1 hydrolyzes O-acetyl-ADP-ribose via nucleophilic attack at the C-1″ position and stereospecifically cleaves α-NAD+ but not β-NAD+, linking it to broader NAD+ metabolism [PMID:21498885, PMID:31599159]. ARH1 operates as the eraser in an ADP-ribosylation cycle whose writers are bacterial cholera toxin and the cellular transferase ARTC1/ART1: it counteracts cholera toxin-mediated ADP-ribosylation of Gαs, with ARH1-deficient mice showing greater intoxication and fluid accumulation, and it cleaves ADP-ribosylated TRIM72 in myocardium, where ARH1, ART1, and TRIM72 form co-immunoprecipitating complexes [PMID:17526733, PMID:30429362, PMID:36497109]. Loss of ARH1 produces distinct pathologies across these axes: cardiomyopathy with myocardial fibrosis, impaired membrane repair, and increased ischemia/reperfusion injury [PMID:30429362], and tumorigenesis—ARH1 acts as a tumor suppressor, with knockout/heterozygous mice developing lymphomas and adenocarcinomas, loss of heterozygosity in tumors, and tumorigenicity that scales inversely with retained hydrolase activity, placing ARTC1 as the epistatic writer counterpart in this cancer pathway [PMID:21697277, PMID:26029825, PMID:36945646].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0016787 hydrolase activity, GO:0140096 catalytic activity, acting on a protein, GO:0140098 catalytic activity, acting on RNA
- **localization:** GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-1430728 Metabolism, R-HSA-1643685 Disease
- **partners:** ART1, TRIM72, GNAS, ARTC1
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2005 | High | ARH1 (ADPRH) is a 39-kDa ADP-ribosylarginine hydrolase that cleaves the N-glycosidic bond of mono-ADP-ribosylated arginine residues on proteins, releasing free ADP-ribose and regenerating unmodified protein. Its activity is enhanced by Mg2+. Critical vicinal acidic amino acids required for catalytic activity were identified by mutagenesis. | PMID:16278211 | The Journal of biological chemistry |
| 2007 | High | ARH1 (ADPRH) counteracts cholera toxin-mediated ADP-ribosylation of the Gsα protein in vivo. ADPRH-knockout cells and mice showed greater intoxication (higher ADP-ribosylarginine content, greater Gsα modification, increased fluid accumulation in intestinal loops) than wild-type, and overexpression of wild-type ADPRH in knockout cells reduced these effects. | PMID:17526733 | Molecular and cellular biology |
| 2011 | High | ARH1 deficiency in mice leads to spontaneous development of lymphomas, adenocarcinomas, and metastases, establishing ARH1 as a tumor suppressor. ARH1-null and heterozygous mouse embryonic fibroblasts showed higher proliferation rates and formed tumors in nude mice. Loss of heterozygosity of the remaining ARH1 allele was documented in all tumors from heterozygous mice. | PMID:21697277 | Cancer research |
| 2014 | High | Comprehensive structural analysis of ARH1 and ARH3 by crystallography revealed that the two enzymes have distinct substrate requirements driven by diverged adenosine ribose moiety binding, while the active sites harboring the distal ribose closely resemble each other. Structural basis for selective inhibition of ARH3 (but not ARH1) by ADP-HPD and arginine-ADP-ribose was elucidated. | PMID:30472116 | Cell chemical biology |
| 2009 | Medium | Human ARH1 (ADPRH) was crystallized in complex with K+ and ADP, yielding diffracting crystals at 1.9 Å resolution. The presence of K+ was required for well-diffracting crystals, indicating a structural role for K+ in the enzyme. | PMID:19407395 | Acta crystallographica. Section F, Structural biology and crystallization communications |
| 2018 | High | ARH1 cleaves ADP-ribosylated TRIM72 (tripartite motif-containing protein 72) on arginine residues in the myocardium. ARH1-deficient mice developed cardiomyopathy with myocardial fibrosis, decreased myocardial function, and increased susceptibility to ischemia/reperfusion injury. ARH1, ART1 (the writing enzyme), and TRIM72 were found in multiple co-immunoprecipitated complexes from mouse heart lysates. ARH1 knockdown in C2C12 myocytes increased ADP-ribosylation of TRIM72 and delayed wound healing. | PMID:30429362 | JCI insight |
| 2015 | High | ARH1 mutations found in tumors from ARH1 heterozygous mice encode proteins with reduced enzymatic activity. MEFs transformed with ARH1 mutant genes showed altered proliferation rates, anchorage-independent colony growth, and tumorigenesis in nude mice in proportion to the degree of hydrolase activity loss, establishing a direct link between ARH1 catalytic activity and tumor suppression. | PMID:26029825 | Oncogenesis |
| 2019 | High | ARH1 hydrolyzes α-NAD+ (but not β-NAD+) in a stereospecific reaction, in addition to its established α-ADP-ribosyl-arginine hydrolase activity. This activity is shared with ARH3 and macrodomain proteins, revealing a broader role in cellular NAD+ metabolism. | PMID:31599159 | ACS chemical biology |
| 2011 | High | ARH1 hydrolyzes O-acetyl-ADP-ribose (OAADPr) and poly(ADP-ribose), in addition to ADP-ribose-arginine. Mechanistic analysis revealed that ARH1-catalyzed hydrolysis of OAADPr involves nucleophilic attack at the C-1″ position, consistent with cleavage of a 1″-O linkage. A postulated 1″-OAADPr isomer was identified at alkaline pH. | PMID:21498885 | The Journal of biological chemistry |
| 2018 | Medium | Female ARH1-knockout mice show greater sensitivity to cholera toxin than male ARH1-KO mice, with higher ADP-ribosylated Gsα protein levels and increased ADP-ribosylarginine content in intestinal epithelial cells, revealing a gender-dependent role of ARH1 in regulating cholera toxin-mediated ADP-ribosylation. | PMID:30500844 | PloS one |
| 2005 | Medium | The ADPRH (ARH1) gene spans approximately 9 kilobases with four exons and three introns. Promoter analysis identified potent stimulatory (−119 to −89) and inhibitory (−161 to −119) elements. An Sp1-binding GC-box element (−107 to −95) positively regulates ADPRH transcription, as demonstrated by Sp1/Sp3 binding (EMSA) and Sp1 trans-activation in Drosophila SL2 cells lacking endogenous Sp1. | PMID:15893437 | Gene |
| 2002 | Medium | Retroviral expression of wild-type ARH1 in transformed lymphocytes from autosomal recessive hypercholesterolemia patients restored LDL receptor internalization, as demonstrated by uptake and degradation of 125I-labeled LDL and confocal microscopy, establishing ARH1 as a functional adaptor required for LDL receptor-dependent LDL internalization in lymphocytes and macrophages. | PMID:12464675 | The Journal of clinical investigation |
| 2022 | Medium | ARH1 is a cytosolic protein ubiquitously expressed in mammalian tissues. In vivo confirmed substrates include Gαs (ADP-ribosylated by cholera toxin) and TRIM72 (ADP-ribosylated by ART1), with ARH1 cleaving the ADP-ribose-arginine bond on these proteins. ARH1 deficiency leads to increased ADP-ribosylation of TRIM72 following ischemia/reperfusion injury. | PMID:36497109 | Cells |
| 2023 | Medium | ARTC1 (the arginine-specific ADP-ribosyltransferase) and ARH1 function in the same ADP-ribosylation cycle. Artc1/Arh1 double-KO MEFs showed decreased tumorigenesis in nude mice compared to Arh1-KO MEFs, and Artc1-KO recipient mice showed decreased xenograft tumor growth with CD8+ T cell and macrophage infiltration and necroptosis, establishing ARTC1 as the writing enzyme counterpart to ARH1 in the same pathway. | PMID:36945646 | bioRxiv |

## Citations

- PMID:12464675
- PMID:15893437
- PMID:16278211
- PMID:17526733
- PMID:19407395
- PMID:21498885
- PMID:21697277
- PMID:26029825
- PMID:30429362
- PMID:30472116
- PMID:30500844
- PMID:31599159
- PMID:36497109
- PMID:36945646
