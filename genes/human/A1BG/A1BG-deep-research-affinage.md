---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/A1BG
affinage_run_date: 2026-06-09T22:02:35
uniprot_accession: P04217
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 6
citation_count: 6
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for A1BG (human)

## Current model (mechanistic narrative)

A1BG is a secreted immunoglobulin-like domain plasma glycoprotein that functions through protein–protein interactions to regulate the activity and stability of partner proteins across diverse physiological contexts [PMID:39433128, PMID:40560034]. Its third of five repeated immunoglobulin-like domains binds CAP-superfamily proteins such as CRISP2 in a magnesium-dependent manner, and this interaction inhibits CRISP2 sterol-binding in vitro and abolishes its sterol export function in yeast [PMID:39433128]. In a distinct context, adipocyte-secreted A1BG binds and stabilizes NAMPT, raising NAD+ production to enhance PARP1/ATM-mediated DNA repair and thereby drive cisplatin resistance in osteosarcoma [PMID:40560034]. A1BG also has a sex-specific cardiac role: cardiomyocyte-specific deletion causes dilated cardiomyopathy with disrupted intercalated disc architecture and altered glucose-6-phosphate and acetyl-CoA metabolism in female but not male mice, consistent with sex-specific cardiac interactomes [PMID:40270023]. Beyond these interaction-based roles, the broader signaling and regulatory logic linking A1BG's partners across tissues has not been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity
- **localization:** GO:0005576 extracellular region
- **pathway (Reactome):** *(none)*
- **partners:** CRISP2, NAMPT
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2024 | High | A1BG directly interacts with CRISP2 (and related CAP superfamily members), and this interaction inhibits sterol-binding by CRISP2 in vitro and abolishes sterol export function in yeast. The interaction is mapped to the third of five repeated immunoglobulin-like domains within A1BG and requires magnesium, implicating coordination of Mg2+ by conserved tetrad residues in the CAP domain as essential for stable complex formation. | PMID:39433128 | The Journal of biological chemistry |
| 2025 | High | Adipocyte-secreted A1BG directly interacts with NAMPT, stabilizing NAMPT protein and increasing NAD+ production, which in turn enhances PARP1 activity and DNA repair via the PARP1/ATM pathway, thereby promoting cisplatin resistance in osteosarcoma cells. A1BG depletion in adipocytes restored cisplatin sensitivity, and recombinant A1BG recapitulated resistance. | PMID:40560034 | Advanced science (Weinheim, Baden-Wurttemberg, Germany) |
| 2025 | High | Loss of A1BG specifically in cardiomyocytes (conditional knockout) causes dilated cardiomyopathy in female but not male mice, with left ventricular dilation, wall thinning, and disruption of intercalated disc architecture. Transcriptomic analysis revealed A1BG regulates metabolic pathways (glucose-6-phosphate and acetyl-CoA metabolism) in female cardiomyocytes. Mass spectrometry identified sex-specific A1BG cardiac interactomes. | PMID:40270023 | Biology of sex differences |
| 2024 | Medium | Loss of A1BG in cardiomyocytes leads to dilated cardiomyopathy in female but not male mice (preprint version of the peer-reviewed finding above), with sex-specific A1BG cardiac interactomes identified by mass spectrometry and sex-specific disruption of intercalated discs. | PMID:39070637 | Research square (preprint) |
| 2019 | Low | Bioinformatic analysis attributed A1BG to the leukocyte receptor cluster (LRC) of eutherian mammals, placing it among immunoglobulin-like domain-containing receptors that evolved from ancestral LRC genes through exon shuffling and sequence divergence. | PMID:31106814 | Genome biology and evolution |
| 1989 | Medium | Genetic linkage analysis assigned the A1BG locus to human chromosome 19, linked to the Lutheran (LU) blood group system. | PMID:2591067 | Clinical genetics |

## Citations

- PMID:2591067
- PMID:31106814
- PMID:39070637
- PMID:39433128
- PMID:40270023
- PMID:40560034
