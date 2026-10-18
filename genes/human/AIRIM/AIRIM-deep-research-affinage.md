---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AIRIM
affinage_run_date: 2026-06-09T22:02:42
uniprot_accession: Q9NX04
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 9
citation_count: 8
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AIRIM (human)

## Current model (mechanistic narrative)

AIRIM (C1orf109) is a structural subunit of the eumetazoan-specific 55LCC complex (SPATA5–SPATA5L1–C1orf109–CINP), where it assembles with CINP and the N-terminal domains of SPATA5 and SPATA5L1 into a funnel-like ring positioned above a hexameric AAA+ ATPase motor [PMID:38554706, PMID:40268917]. Through this complex AIRIM drives a late cytoplasmic step of human pre-60S ribosome maturation, and its loss impairs global protein synthesis [PMID:35354024]. Within the 55LCC the ATPase activity is enhanced by replication fork DNA and coupled to cysteine protease-dependent cleavage of replisome substrates, such that complex deficiency causes ubiquitin-independent proteotoxicity, replication stress, and chromosome instability [PMID:38554706]. AIRIM variants reduce ribosome levels selectively during neuroepithelial differentiation, disproportionately impairing translation of a subset of mRNAs and disrupting neural progenitor survival and fate commitment; these defects are suppressed by mTOR activation, and AIRIM variants cause a neurodevelopmental disorder [PMID:40760247]. A distinct activity of the longest isoform involves binding DHX9 and displacing PARP1 to promote R-loop accumulation and DNA damage [PMID:32761833], and C1orf109 is a CK2 substrate [PMID:22548824].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140657 ATP-dependent activity, GO:0003677 DNA binding
- **localization:** GO:0005829 cytosol, GO:0005634 nucleus
- **pathway (Reactome):** R-HSA-8953854 Metabolism of RNA, R-HSA-73894 DNA Repair
- **partners:** SPATA5, SPATA5L1, CINP, DHX9, CSNK2 (CK2)
- **complexes:** 55LCC complex (SPATA5–SPATA5L1–C1orf109–CINP)

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2022 | High | C1orf109 (AIRIM), together with SPATA5, CINP, and SPATA5L1, controls a late step of human pre-60S ribosome maturation in the cytoplasm. Loss of C1orf109 impairs global protein synthesis. | PMID:35354024 | Cell reports |
| 2012 | Medium | C1orf109 protein is phosphorylated in vivo and can be directly phosphorylated by protein kinase CK2 in vitro; it localizes mainly to the nucleus and cytoplasm, and its overexpression promotes cancer cell proliferation and colony formation with upregulation of PCNA and cyclin D1, while siRNA knockdown reduces proliferation. | PMID:22548824 | Journal of biomedical science |
| 2020 | Medium | C1orf109L (the longest isoform of C1orf109/AIRIM) binds DHX9 (identified by IP-MS and co-IP), localizes to R-loops (by DR-IP and immunofluorescence), and competitively displaces PARP1 from DHX9, thereby blocking DHX9-PARP1 function and promoting R-loop accumulation, DNA damage, and G2/M cell cycle arrest. This mechanism enhances sensitivity to the topoisomerase inhibitor camptothecin. | PMID:32761833 | Cell proliferation |
| 2023 | Medium | C1orf109 interacts and co-localizes with CK2 in liver cancer cells and activates Wnt signaling by upregulating non-phosphorylated β-catenin and downstream targets (CyclinD1, c-Myc, MMP7); CK2-specific inhibitor blocks the proliferative and invasive effects of C1orf109 overexpression. | PMID:36988773 | Journal of molecular histology |
| 2024 | High | C1orf109 (AIRIM) is part of the 55LCC complex (SPATA5–SPATA5L1–C1orf109–CINP), which has ATPase activity specifically enhanced by replication fork DNA and is coupled to cysteine protease-dependent cleavage of replisome substrates in response to replication fork damage. Deficiency in the complex causes ubiquitin-independent proteotoxicity, replication stress, and severe chromosome instability. Integrative structural biology revealed that SPATA5–SPATA5L1 N-terminal domains interact with C1orf109–CINP to form a funnel-like structure above a cylindrical ATPase motor. | PMID:38554706 | Cell |
| 2025 | High | Cryo-EM structure shows C1orf109 and CINP form an N-terminal ring with SPATA5 and SPATA5L1 NTDs within the 4:2:2:2 55LCC complex. In the pre-60S-bound state, CINP (not C1orf109 directly) mediates recognition of the pre-60S particle through interactions with GTPBP4 and ES27A—a human-specific feature absent in yeast. | PMID:40268917 | Nature communications |
| 2025 | High | AIRIM/C1orf109 variants cause neurodevelopmental disorders by reducing ribosome levels specifically during neuroepithelial differentiation. Reduced ribosome availability disproportionately impairs translation of specific transcripts, disrupting survival and cell fate commitment of transitioning neuroepithelia. Genetic and pharmacologic enhancement of mTOR activity suppresses the growth and developmental defects associated with AIRIM variants in human cerebral organoids. | PMID:40760247 | Nature cell biology |
| 2024 | Medium | AIRIM variants reduce ribosome levels specifically in neural progenitor cells and cause a transient delay in radial glia fate commitment; inappropriately low ribosome levels impair translation of a selected subset of mRNAs. mTORC1 activation (genetic and pharmacologic) suppresses AIRIM-linked phenotypes in cerebral organoids. | PMID:38260472 | bioRxiv |
| 2025 | Medium | In a protein–protein interaction screen, C1orf109 (as part of the 55LCC complex) was confirmed as essential for pre-60S maturation; acute depletion of each 55LCC component (including C1orf109) impairs pre-60S maturation. SPATA5 ATPase activity is more important than SPATA5L1's ATPase activity for complex function. Cryo-EM and X-ray crystallography defined the 55LCC architecture, and 55LCC represents a eumetazoan-specific elaboration of the yeast Drg1 ATPase. | — | bioRxiv |

## Citations

- PMID:22548824
- PMID:32761833
- PMID:35354024
- PMID:36988773
- PMID:38260472
- PMID:38554706
- PMID:40268917
- PMID:40760247
