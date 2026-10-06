---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ATAD3B
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q5T9A4
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 6
citation_count: 4
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ATAD3B (human)

## Current model (mechanistic narrative)

ATAD3B is a mitochondrial membrane protein that acts as a stress-responsive mitophagy receptor for selective clearance of damaged mitochondrial DNA [PMID:33665835]. Under basal conditions it hetero-oligomerizes with ATAD3A, which targets the ATAD3B C-terminus to the intermembrane space and negatively regulates ATAD3A's interaction with matrix nucleoid complexes, positioning ATAD3B as a dominant-negative modulator of ATAD3A whose loss perturbs mitochondrial morphology [PMID:33665835, PMID:22664726]. Oxidative stress-induced mtDNA damage or depletion disrupts the ATAD3B-ATAD3A hetero-oligomer, exposing the ATAD3B C-terminus at the outer mitochondrial membrane where its LIR motif directly binds LC3 to initiate mitophagy independently of PINK1 [PMID:33665835]. This pathway is functionally consequential: ATAD3B re-expression promotes clearance of pathogenic m.3243A>G mutant mtDNA [PMID:33665835]. ATAD3B is encoded as two mitochondrially localized isoforms that are early transcriptional targets of c-Myc and are required for normal cell division, with knockdown producing polynuclear cells, reduced proliferation, and apoptosis [PMID:16909202]. At mitochondria-associated membranes, the ER protein SEC62 directly binds ATAD3B and suppresses its expression, dampening mitophagy and amplifying mitochondrial ROS and inflammation [PMID:42001994].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity
- **localization:** GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-9612973 Autophagy
- **partners:** ATAD3A, MAP1LC3B, SEC62
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2021 | High | ATAD3B contains a LIR (LC3-interacting region) motif that directly binds LC3 and functions as a mitophagy receptor, promoting oxidative stress-induced mitophagy in a PINK1-independent manner to clear damaged mtDNA. | PMID:33665835 | The EMBO journal |
| 2021 | High | Under normal conditions, ATAD3B hetero-oligomerizes with ATAD3A, which promotes targeting of the ATAD3B C-terminal region to the mitochondrial intermembrane space. Oxidative stress-induced mtDNA damage or depletion reduces this ATAD3B-ATAD3A hetero-oligomerization, leading to exposure of the ATAD3B C-terminus at the mitochondrial outer membrane and subsequent LC3 recruitment for mitophagy initiation. | PMID:33665835 | The EMBO journal |
| 2012 | Medium | ATAD3B associates with ATAD3A (hetero-oligomerization), negatively regulates the interaction of ATAD3A with matrix nucleoid complexes, and contributes to a mitochondrial fragmentation phenotype. ATAD3B thus functions as a dominant negative regulator of ATAD3A. | PMID:22664726 | Mitochondrion |
| 2006 | Medium | The ATAD3B gene encodes two distinct protein isoforms (AAA-TOB3s and AAA-TOB3l) generated from distinct transcription initiation sites, both localized to mitochondria. Both isoforms are early transcriptional targets of c-Myc. Knockdown of both isoforms results in polynuclear cells, decreased proliferation, dysfunctional cell division, and increased apoptosis, indicating a required role in cell division. | PMID:16909202 | Cellular and molecular life sciences : CMLS |
| 2026 | Medium | SEC62, an ER transmembrane protein at mitochondria-associated membranes (MAMs), directly interacts with ATAD3B and suppresses ATAD3B expression, leading to defective mitophagy, increased mitochondrial ROS, and amplified inflammatory responses in MASH. | PMID:42001994 | Metabolism: clinical and experimental |
| 2021 | Medium | ATAD3B re-expression in cells with m.3243A>G mutated mtDNA promotes clearance of the mutant mtDNA, demonstrating a functional role of ATAD3B-mediated mitophagy in eliminating pathogenic mtDNA variants. | PMID:33665835 | The EMBO journal |

## Citations

- PMID:16909202
- PMID:22664726
- PMID:33665835
- PMID:42001994
