---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANAPC5
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q9UJX4
self_evaluation_pairwise: win
faith_pct: 85.71428571428571
n_discoveries: 23
citation_count: 23
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ANAPC5 (human)

## Current model (mechanistic narrative)

ANAPC5 (APC5) is a core scaffolding subunit of the anaphase-promoting complex/cyclosome (APC/C), the multisubunit E3 ubiquitin ligase that targets cell-cycle regulators for proteasomal degradation [PMID:9469815]. Together with APC1 and APC4, APC5 builds the platform subcomplex that bridges the catalytic module (APC2/APC11/APC10) to the TPR co-activator-binding subunits; this subcomplex assembles polyubiquitin chains but cannot itself bind CDH1 or ubiquitinate substrates, marking its role as structural rather than catalytic [PMID:12956947, PMID:21307936]. Structural work resolved the APC5 N-terminal α-helical fold and its contacts with APC4, and showed that the platform supports the coactivator-induced allosteric change required for UbcH10-dependent ubiquitination [PMID:26343760, PMID:27601667]. Within the complex, APC5 directly binds substrates such as E2F1, mediating its K11-linked ubiquitination and degradation after S phase [PMID:22580462], and genetic studies across organisms reveal substrate-selective contributions: Drosophila IDA/APC5 is required for cyclin B degradation but not sister-chromatid separation [PMID:11870214], and C. elegans SUCH-1/APC5 governs SAC-dependent mitotic timing with a redundant paralog acting in meiosis [PMID:20944014, PMID:20944012]. Beyond the APC/C, APC5 engages CBP/p300 to stimulate their acetyltransferase activity and transcription and to suppress E1A-mediated transformation [PMID:16319895], binds poly(A)-binding protein to repress IRES-mediated translation [PMID:15082755], and negatively regulates IL-17 signaling through association with IL-17 receptors and the deubiquitinase A20 [PMID:23922952]. APC5 is also a target of viral subversion: HCMV pUL21a binds the APC/C and drives proteasomal degradation of APC5 (and APC4/APC1) to inactivate the complex [PMID:20686030, PMID:22792066]. More recent work implicates ANAPC5-mediated ubiquitination of GPAA1 and EGFR in tumor immune evasion and macrophage polarization [PMID:41512182, PMID:40834712].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0060090 molecular adaptor activity, GO:0005198 structural molecule activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005840 ribosome, GO:0005634 nucleus
- **pathway (Reactome):** R-HSA-1640170 Cell Cycle, R-HSA-392499 Metabolism of proteins, R-HSA-168256 Immune System, R-HSA-74160 Gene expression (Transcription)
- **partners:** ANAPC1, ANAPC4, ANAPC7, E2F1, CREBBP, EP300, PABP, TNFAIP3
- **complexes:** APC/C (anaphase-promoting complex/cyclosome)

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1998 | High | ANAPC5 (APC5) was identified as one of four previously uncharacterized human APC subunits (alongside APC2, APC4, APC7) and shown to be a core component of the anaphase-promoting complex, an eight-subunit E3 ubiquitin ligase responsible for targeting cell cycle regulators for degradation. | PMID:9469815 | Science |
| 2003 | High | APC5, together with APC1 and APC4, forms a subcomplex that can assemble multiubiquitin chains but cannot bind CDH1 or ubiquitinate substrates. APC5 likely acts as a scaffold connecting the catalytic module (APC2/APC11) with the TPR subunits that recruit co-activators. | PMID:12956947 | Current Biology |
| 2011 | High | Cryo-EM and mass spectrometry structural analysis of the APC/C places APC5 (along with APC1 and APC4) as a scaffolding subunit that coordinates the juxtaposition of the catalytic module (APC2, APC11, APC10) and TPR subunits, providing a pseudo-atomic model for APC/C organization. | PMID:21307936 | Nature |
| 2015 | High | Crystal structures of Apc4 and the N-terminal domain of Apc5 (Apc5N) were determined; Apc5N adopts an α-helical fold, and in the context of the APC/C, shows small conformational changes and contacts Apc4 to order regions disordered in the crystal. | PMID:26343760 | Journal of Molecular Biology |
| 2016 | High | APC5 (as part of the APC/C platform with APC1, APC4, and APC15) supports the coactivator-induced allosteric conformational change required for UbcH10-dependent ubiquitination; the platform structurally coordinates the catalytic and substrate-recognition modules. | PMID:27601667 | PNAS |
| 2005 | High | APC5 and APC7 directly interact with transcriptional coactivators CBP and p300 through protein-protein interaction domains evolutionarily conserved in adenovirus E1A; this interaction stimulates intrinsic CBP/p300 acetyltransferase activity and potentiates CBP/p300-dependent transcription. | PMID:16319895 | Nature |
| 2005 | Medium | APC5 and APC7 suppress E1A-mediated cellular transformation in a CBP/p300-dependent manner, indicating these subunits are functionally targeted during cellular transformation. | PMID:16319895 | Nature |
| 2004 | Medium | Apc5 binds poly(A) binding protein (PABP) and represses IRES-mediated translation of PDGF-2 mRNA; overexpression of Apc5 counteracts PABP-enhanced IRES activity, and Apc5 co-sediments with the ribosomal fraction, indicating a role outside the APC/C in translational regulation. | PMID:15082755 | Molecular and Cellular Biology |
| 2012 | Medium | APC5 binds E2F1 directly (confirmed by in vivo and in vitro Co-IP/GST pulldown) and is essential for E2F1 ubiquitination by APC/C-Cdh1, which targets E2F1 for K11-linked ubiquitin chain-mediated proteasomal degradation after S phase. | PMID:22580462 | Cell Cycle |
| 2013 | Medium | ANAPC5 binds IL-17RA and IL-17RC and associates with the deubiquitinase A20 (TNFAIP3); siRNA-mediated knockdown of ANAPC5 enhances IL-17-induced gene expression, demonstrating that ANAPC5 acts as a negative regulator of IL-17 signaling. | PMID:23922952 | PLoS ONE |
| 2010 | Medium | During HCMV infection, APC5 and APC4 subunits undergo proteasome-dependent degradation, which is temporally associated with disassembly of the APC/C core complex and requires viral early gene expression (not immediate early genes alone), leading to APC/C inactivation. | PMID:20686030 | Journal of Virology |
| 2012 | High | HCMV protein pUL21a physically binds the APC/C and is necessary and sufficient to induce proteasome-dependent degradation of APC5 and APC4, thereby disrupting APC/C integrity; residues P109-R110 of pUL21a are critical for APC binding and APC5/APC4 degradation. | PMID:22792066 | PLoS Pathogens |
| 2015 | Medium | HCMV protein UL21a also targets APC1 for degradation (in addition to APC4 and APC5); furthermore, depletion of any single platform subunit (APC1, APC4, or APC5) or APC8 triggers coordinated co-degradation of all three platform subunits, revealing a cellular mechanism for platform subunit co-regulation. | PMID:25903336 | Journal of Virology |
| 2002 | Medium | In Drosophila, IDA (the APC5 homolog) is required for APC/C-dependent degradation of cyclin B but not for degradation of substrates controlling sister-chromatid separation; ida mutants display high mitotic index with aneuploid, overcondensed chromosomes, defining a subfunction-specific role for APC5 within the APC/C. | PMID:11870214 | Journal of Cell Science |
| 2003 | Medium | Yeast Apc5 physically interacts with Cdc23 and Apc1 in co-expression in vitro transcription/translation; yeast two-hybrid and co-purification experiments confirmed Mnd2 and Swm1 interact with Apc5 and Cdc23 as core APC subunits. | PMID:12609981 | Journal of Biological Chemistry |
| 2002 | Medium | In yeast, APC5 (RMC1) is required for in vitro chromatin assembly; apc5 mutants display UV sensitivity, plasmid loss, G2/M accumulation, and genetic interactions with apc9Δ, apc10Δ, and cdc26Δ, linking APC5 function to chromatin metabolism and APC complex integrity. | PMID:12399376 | Genetics |
| 2013 | Medium | The APC (via Apc5) targets Fob1 for degradation specifically in G1; Fob1 is unstable in G1, stabilized in apc5(CA) and proteasome mutants, and Fob1 deletion suppresses apc5(CA) cell cycle and rDNA recombination defects, placing APC5-dependent Fob1 degradation in a pathway linking APC to replicative longevity and genomic stability. | PMID:24361936 | Genetics |
| 2009 | High | Fission yeast Atf1 physically binds the APC/C in vivo; purified Atf1 stimulates ubiquitylation of cyclin B and securin by the APC/C in a cell-free system, independent of Atf1's DNA-binding (bZIP) domain; atf1+ is a dose-dependent suppressor of apc5-1 mitotic arrest. | PMID:19584054 | Journal of Biological Chemistry |
| 2010 | Medium | In C. elegans, SUCH-1/APC5 is required for normal mitotic timing; a novel such-1(t1668) allele causes prolonged mitosis in embryos with monopolar spindles, and this delay is SAC-dependent (rescued by mdf-1/MAD1 or mdf-2/MAD2 inactivation), suggesting the APC/C negatively regulates the SAC. | PMID:20944014 | Genetics |
| 2010 | Medium | C. elegans has two APC5 paralogs (such-1 and gfi-3) that are coexpressed in the germline; co-depletion (but not individual depletion) causes meiotic arrest, demonstrating functionally redundant roles for APC5 paralogs in meiosis. | PMID:20944012 | Genetics |
| 2024 | Medium | Co-depletion of ANAPC5 in cell lines exacerbates KIF18A-depletion-induced mitotic arrest, whereas co-depletion of ANAPC7 partially rescues this arrest, indicating opposing roles for ANAPC5 and ANAPC7 in modulating mitotic progression downstream of KIF18A. | PMID:39677807, PMID:40596695 | Scientific Reports / bioRxiv |
| 2026 | Medium | Radiation inhibits the APC/C complex, reducing ANAPC5-mediated ubiquitination of GPAA1 (a catalytic subunit of GPI transamidase); the resulting accumulation of GPAA1 enhances GPI anchoring and CD24 membrane localization, promoting phagocytosis resistance and immune evasion in irradiated tumor cells. | PMID:41512182 | Cancer Research |
| 2025 | Medium | ANAPC5 overexpression in macrophages induces ubiquitination and suppression of EGFR, thereby promoting M2 macrophage polarization over M1; this effect is mediated through the EGFR/CD24 axis, and ANAPC5 overexpression reduces lung inflammation in an LPS-induced ALI mouse model. | PMID:40834712 | Cellular Immunology |

## Citations

- PMID:11870214
- PMID:12399376
- PMID:12609981
- PMID:12956947
- PMID:15082755
- PMID:16319895
- PMID:19584054
- PMID:20686030
- PMID:20944012
- PMID:20944014
- PMID:21307936
- PMID:22580462
- PMID:22792066
- PMID:23922952
- PMID:24361936
- PMID:25903336
- PMID:26343760
- PMID:27601667
- PMID:39677807
- PMID:40596695
- PMID:40834712
- PMID:41512182
- PMID:9469815
