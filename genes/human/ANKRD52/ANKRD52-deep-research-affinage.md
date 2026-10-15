---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANKRD52
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q8NB46
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 5
citation_count: 5
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ANKRD52 (human)

## Current model (mechanistic narrative)

ANKRD52 is the ankyrin-repeat regulatory subunit of the protein phosphatase 6 (PP6) heterotrimer, where it assembles with the PP6 catalytic subunit and a SAPS-domain PP6R subunit to confer substrate specificity on the complex [PMID:18186651]. It was identified by mass spectrometry as a PP6 holoenzyme component, binding the C-terminal scaffold region of PP6R1, which holds separate docking sites for the catalytic and ankyrin-repeat subunits, with endogenous holoenzymes eluting as >440 kDa heterotrimers [PMID:18186651]. Functionally, the ANKRD52-PP6 complex maintains the global efficiency of miRNA-mediated silencing by dephosphorylating AGO2 at a conserved S824-S834 cluster; target engagement triggers hierarchical phosphorylation of AGO2 by CSNK1A1, and rapid dephosphorylation by ANKRD52-PPP6C resets AGO2 for productive target binding, with loss of this cycle expanding the AGO2 target repertoire and diluting the active phosphatase-reset pool per target [PMID:28114302]. The same complex dephosphorylates PAK1 to restrain cell migration, and ANKRD52 transcription is repressed by TAZ [PMID:33096142]. Through its control of miRNA silencing, ANKRD52 sustains miR-155-mediated repression of SOCS1, so its inactivation—or reintroduction of cancer patient mutations—dampens JAK-STAT/interferon-γ signaling and antigen presentation, allowing tumor cells to evade T cell-mediated cytotoxicity [PMID:34853298].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0098772 molecular function regulator activity, GO:0060090 molecular adaptor activity
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-8953854 Metabolism of RNA, R-HSA-168256 Immune System
- **partners:** PPP6C, PP6R1, PP6R3, AGO2, PAK1, CSNK1A1
- **complexes:** PP6 phosphatase heterotrimer

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2008 | High | ANKRD52 (PP6-ARS-C) is a regulatory subunit of the PP6 holoenzyme heterotrimer. It was identified by mass spectrometry as co-precipitating with FLAG-PP6R1 (a SAPS domain subunit). Tagged Ankrd28 (the closest paralog studied in detail) coprecipitated with PP6 catalytic subunit and with SAPS domain subunits PP6R1 and PP6R3. The C-terminal region of PP6R1 was sufficient to coprecipitate Ankrd28/Ankrd52-family proteins but not PP6 itself, demonstrating PP6R1 acts as a scaffold with separate binding regions for the catalytic subunit and the ankyrin repeat subunit. Endogenous PP6 holoenzymes with PP6R1 and PP6R3 eluted at >440 kDa from size-exclusion chromatography together with Ankrd28, consistent with a heterotrimer. Knockdown of PP6R1 or Ankrd28, but not PP6R3, enhanced IκBε degradation in response to TNFα, indicating functional specificity of the ankyrin repeat subunit. | PMID:18186651 | Biochemistry |
| 2017 | High | ANKRD52 is the regulatory subunit of the ANKRD52-PPP6C phosphatase complex that dephosphorylates AGO2 at a cluster of conserved residues (S824-S834). Target engagement by AGO2 triggers hierarchical multi-site phosphorylation by CSNK1A1, followed by rapid dephosphorylation by the ANKRD52-PPP6C complex. AGO2 phosphorylation at these residues inhibits target mRNA binding. Inactivation of this phosphorylation cycle globally impairs miRNA-mediated silencing. Non-phosphorylatable AGO2 shows a pronounced expansion of its transcriptome-wide target repertoire at steady-state, reducing the active AGO2 pool per target. | PMID:28114302 | Nature |
| 2020 | Medium | TAZ transcriptionally represses ANKRD52: knockdown of TAZ leads to enhanced ANKRD52 promoter activity and increased ANKRD52 mRNA levels. ANKRD52, as a subunit of the PP6 holoenzyme, interacts with PAK1 (identified by mass spectrometry). Knockdown of ANKRD52 or PP6c results in elevated PAK1 phosphorylation, while forced ANKRD52 expression attenuates cell mobility. ANKRD52 thus regulates cell migration through PP6c-mediated dephosphorylation of PAK1. | PMID:33096142 | Biochimica et biophysica acta. Molecular cell research |
| 2021 | High | Genetic inactivation of ANKRD52, or re-introduction of frequent ANKRD52 patient mutations found in cancers, dampens JAK-STAT-interferon-γ signaling and antigen presentation in cancer cells, largely by abolishing miR-155-targeted silencing of SOCS1. This was established by combining CRISPR library screens in syngeneic mouse tumor models with co-culture systems under immune pressure, demonstrating that the ANKRD52-containing miRNA machinery maintains cancer cell sensitivity to T cell-mediated cytotoxicity. | PMID:34853298 | Nature communications |
| 2024 | Low | In colorectal cancer, PP6 functions as a heterotrimer comprising PP6c, PP6R subunits (PP6R1-3), and scaffold subunits including ANKRD52. The PP6c-PP6R3 complex (not specifically ANKRD52) was identified as a key player in regulating cancer stem cell markers; PP6c knockdown decreased colony-forming ability and in vivo proliferation. This study confirms the heterotrimer model for PP6 assembly including ANKRD52 as a scaffold subunit. | PMID:39014521 | Cancer science |

## Citations

- PMID:18186651
- PMID:28114302
- PMID:33096142
- PMID:34853298
- PMID:39014521
