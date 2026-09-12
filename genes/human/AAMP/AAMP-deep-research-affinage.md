---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AAMP
affinage_run_date: 2026-06-09T22:02:35
uniprot_accession: Q13685
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 10
citation_count: 10
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AAMP (human)

## Current model (mechanistic narrative)

AAMP is a WD40- and immunoglobulin-domain-containing protein, distributed both intracellularly and at the cell surface, that governs cell migration, angiogenesis, and innate immune signaling primarily by acting as a positive regulator of Rho-family GTPases and the actin cytoskeleton [PMID:8683944, PMID:26350504, PMID:39404373]. Its amino-terminal positively charged region binds heparin with high affinity and mediates heparin-sensitive, glycosaminoglycan-dependent cell binding and clustering, and anti-AAMP antibody blocks endothelial tube formation [PMID:8683944, PMID:18634104]. In vascular endothelial cells AAMP is recruited by VEGF to membrane protrusions and is required for VEGF-induced tube formation, aortic ring sprouting, actin stress fiber formation, and gel contraction through RhoA/Rho-kinase signaling [PMID:26350504]. Mechanistically, AAMP binds RhoA directly and protects it from SMURF2-mediated ubiquitination and degradation, thereby raising active RhoA levels [PMID:34901393], regulates the stability and activity of both RhoA and RhoB and colocalizes with F-actin and cortactin at membrane ruffles where it constrains endothelial barrier function [PMID:39404373], and binds CDC42 to promote its activation by impeding the ARHGAP1–CDC42 interaction [PMID:33279622]; collectively these activities drive cancer cell adhesion, growth, and invasion [PMID:23564791, PMID:33279622, PMID:34901393]. Independently of its cytoskeletal role, AAMP interacts via its WD40 domains with the NLR protein Nod2 and modulates Nod1/Nod2-driven NF-κB activation [PMID:19535145], and binds the co-stimulatory protein B7-H3 to influence T-cell proliferation [PMID:35919070].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity, GO:0008092 cytoskeletal protein binding, GO:0060090 molecular adaptor activity, GO:0008289 lipid binding
- **localization:** GO:0005829 cytosol, GO:0005886 plasma membrane, GO:0005576 extracellular region, GO:0005856 cytoskeleton
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-168256 Immune System, R-HSA-1643685 Disease
- **partners:** RHOA, RHOB, CDC42, ARHGAP1, SMURF2, NOD2, CD276, CTTN
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1996 | Medium | AAMP is a 52 kDa protein containing immunoglobulin-type domains, WD40 repeats, a large acidic region with an acid box, a potential transmembrane region, serine/threonine phosphorylation sites, and a positively charged amino-terminal region with strong heparin binding potential (Kd = 14 pmol). Anti-AAMP antibody inhibits endothelial tube formation on Matrigel under cross-linking conditions, and AAMP is distributed both intracellularly and extracellularly in endothelial cell cultures. | PMID:8683944 | Laboratory investigation |
| 1996 | Medium | AAMP shares a common epitope (ESESES) with alpha-actinin and a fast skeletal muscle 23-kDa fiber protein; the epitope is continuous in AAMP but discontinuous/assembled in alpha-actinin. Thermolysin digestion destroys anti-P189 reactivity for alpha-actinin but not recombinant AAMP, demonstrating structural differences in how the epitope is presented. | PMID:8660919 | Experimental cell research |
| 1997 | Medium | An AAMP-derived peptide (P189, from the heparin-binding amino-terminal region) in aggregated particulate form binds heparin in a saturable manner (Kd = 306 pmol) and mediates heparin-sensitive cell binding/clustering; cell surface glycosaminoglycans are implicated. Tumor cell migration is partially inhibited by the peptide. | PMID:18634104 | Biotechnology and bioengineering |
| 2009 | High | AAMP was identified as a binding partner of Nod2 (NLR family) via yeast two-hybrid screen; co-immunoprecipitation from human cells confirmed the interaction and showed that an internal peptide of AAMP spanning three WD40 domains is sufficient for binding. AAMP is predominantly cytosolic in epithelial cells. Overexpression and siRNA knockdown demonstrated that AAMP modulates Nod2- and Nod1-mediated NF-κB activation in HEK293T cells. | PMID:19535145 | Molecular immunology |
| 2013 | Medium | Knockdown of AAMP (via hammerhead ribozyme transgene) in breast cancer cell lines reduced cell adhesion and cell growth (MCF-7) and suppressed cell invasion (MDA-MB-231), establishing a direct functional role for AAMP in breast cancer cell adhesion, growth, and invasion. | PMID:23564791 | Anticancer research |
| 2015 | Medium | AAMP localizes to cytoplasm and membrane in vascular endothelial cells, and is recruited by VEGF to cell membrane protrusions. siRNA knockdown and antibody blockade of AAMP impaired VEGF-induced endothelial tube formation and aortic ring angiogenic sprouting. AAMP knockdown reduced VEGF-induced actin stress fiber formation and collagen gel contraction. RhoA/Rho kinase signaling was identified as a downstream mediator of AAMP's role in endothelial cell migration and angiogenesis. | PMID:26350504 | Annals of biomedical engineering |
| 2020 | Medium | AAMP interacts with CDC42 (confirmed by co-immunoprecipitation) and promotes CDC42 activation in NSCLC cells, resulting in formation of cellular protrusions. Mechanistically, AAMP enhances CDC42 activation by impairing the interaction between the GAP protein ARHGAP1 and CDC42, thereby preventing CDC42 inactivation. | PMID:33279622 | Cancer letters |
| 2021 | Medium | AAMP binds directly to RhoA and suppresses its SMURF2-mediated ubiquitination and degradation, thereby stabilizing RhoA and increasing the level of active RhoA. SMURF2 was shown to act as an E3 ubiquitin ligase for RhoA. This AAMP-RhoA-SMURF2 axis promotes colorectal cancer cell migration and invasion. | PMID:34901393 | Molecular therapy oncolytics |
| 2022 | Medium | AAMP was identified as a binding partner of the co-stimulatory protein B7-H3 by yeast two-hybrid and mass spectrometry screens; binding was confirmed by bimolecular fluorescence complementation (BiFC) and co-immunoprecipitation. On a functional level, AAMP modulates B7-H3-mediated effects on T-cell proliferation in a 3H-thymidine proliferation assay. | PMID:35919070 | Neuro-oncology advances |
| 2024 | Medium | Proteomics screen (following ubiquitination inhibition in primary human endothelial cells) identified AAMP as a negative regulator of endothelial barrier function whose turnover is controlled by ubiquitination. AAMP regulates the stability and activity of both RhoA and RhoB, and colocalizes with F-actin and cortactin at membrane ruffles, suggesting a role in F-actin dynamics. | PMID:39404373 | Cells |

## Citations

- PMID:18634104
- PMID:19535145
- PMID:23564791
- PMID:26350504
- PMID:33279622
- PMID:34901393
- PMID:35919070
- PMID:39404373
- PMID:8660919
- PMID:8683944
