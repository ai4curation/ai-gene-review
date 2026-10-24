---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANAPC15
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: P60006
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 9
citation_count: 9
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ANAPC15 (human)

## Current model (mechanistic narrative)

ANAPC15 (APC15) is a structural subunit of the anaphase-promoting complex/cyclosome (APC/C) platform that governs spindle assembly checkpoint (SAC) silencing by driving turnover of the mitotic checkpoint complex (MCC) on the APC/C [PMID:21926987, PMID:23007861]. Located near the APC/C's MCC binding site, APC15 is specifically required for APC/C(MCC)-dependent autoubiquitylation and degradation of the co-activator CDC20, which disassembles the inhibitory MCC and licenses cyclin B1 ubiquitylation and anaphase onset; in its absence MCC and ubiquitylated CDC20 remain locked onto the APC/C, blocking checkpoint silencing [PMID:21926987, PMID:23007861]. This activity is selective: APC15 is dispensable for the core catalytic ubiquitylation of canonical substrates by APC/C(CDC20) and APC/C(CDH1) [PMID:23007861]. The role is conserved, with the yeast ortholog Mnd2/Apc15 likewise required for SAC-dependent Cdc20 autoubiquitination during checkpoint inactivation [PMID:22940250]. APC15-driven MCC turnover operates in parallel with UBE2C-dependent ubiquitination and with the AAA+ ATPase TRIP13, such that complete MCC disassembly and timely mitotic exit require both routes [PMID:27591192, PMID:30341343]. APC15 is also required for SAC inactivation and the metaphase-to-anaphase transition in mouse oocyte meiosis [PMID:40153087].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0005198 structural molecule activity, GO:0140096 catalytic activity, acting on a protein
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-1640170 Cell Cycle, R-HSA-392499 Metabolism of proteins
- **partners:** CDC20, TRIP13, UBE2C
- **complexes:** APC/C

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2011 | High | APC15 is required for the turnover of the APC/C co-activator CDC20 and release of mitotic checkpoint complexes (MCCs) during SAC signalling. In the absence of APC15, MCCs and ubiquitylated CDC20 remain locked onto the APC/C, preventing ubiquitylation and degradation of cyclin B1 when the SAC is satisfied. APC15 is dispensable for APC/C catalytic activity per se. | PMID:21926987 | Nature cell biology |
| 2012 | High | APC15 (related to yeast Mnd2) is located near the APC/C's MCC binding site and is required for APC/C(MCC)-dependent CDC20 autoubiquitylation and degradation, which promotes MCC disassembly and timely anaphase initiation. APC15 is dispensable for substrate ubiquitylation by APC/C(CDC20) and APC/C(CDH1). | PMID:23007861 | Nature structural & molecular biology |
| 2012 | High | In budding yeast, the Mnd2/Apc15 subunit of the APC/C is required for SAC-dependent Cdc20 autoubiquitination. Reconstitution with purified components showed that Mad3-Bub3 synergizes with Mad2 to lock Cdc20 on the APC/C and stimulate Cdc20 autoubiquitination while inhibiting substrate ubiquitination; this SAC-dependent autoubiquitination requires Mnd2/Apc15. Deletion of Mnd2 delays but does not abolish SAC release, indicating Cdc20 ubiquitination is required for SAC inactivation. | PMID:22940250 | Molecular cell |
| 2016 | Medium | APC15 is a component of the APC/C platform subcomplex. Cryo-EM of an APC/C-Cdh1 complex lacking Apc1(WD40) showed that Apc15 density is not visible in this mutant, and the complex is locked in an inactive conformation, suggesting Apc15's structural position within the APC/C depends on the Apc1 WD40-mediated conformational state. | PMID:27601667 | Proceedings of the National Academy of Sciences of the United States of America |
| 2016 | Medium | In HCT116 cells lacking UBE2C (CRISPR/Cas9 knockout), depletion of APC15 causes a strong synergistic inhibition of mitotic progression by stabilizing MCC on the APC/C, suggesting that APC15-driven MCC turnover and UBE2C-dependent ubiquitination act in parallel pathways for SAC silencing. | PMID:27591192 | Biology open |
| 2017 | Medium | In fission yeast, deletion of Apc15 reduces association between MCC and APC/C, causes defective poly-ubiquitination of Cdc20, and results in checkpoint defects. In vitro and in vivo co-immunoprecipitation data support the existence of APC/C-bound complexes containing two molecules of Cdc20 (MCC-Cdc20 and APC/C-bound Cdc20); Apc15 deletion leads to accumulation of complexes containing both Cdc20 molecules. | PMID:28366744 | Current biology : CB |
| 2017 | Medium | In fission yeast, deletion of Apc15 mimics mutations in the Mad3 ABBA-KEN2-ABBA motif that mediates MCC binding to the APC/C and MCC disassembly, revealing that Apc15 shares a function with this motif in APC/C-MCC association and checkpoint disassembly. This function may be masked in human cells by independent mediators. | PMID:28366743 | Current biology : CB |
| 2018 | High | TRIP13 and APC15 act through parallel pathways to disassemble MCC and drive mitotic exit. Combining rapid TRIP13 depletion (degron tagging) with elimination of APC15-dependent Cdc20 ubiquitination/degradation results in a complete inability to exit mitosis even when MCC assembly at unattached kinetochores is prevented, demonstrating that both interphase-produced and mitosis-produced MCC must be disassembled for mitotic exit. | PMID:30341343 | Nature communications |
| 2025 | Medium | During mouse oocyte meiosis, APC15 localizes dynamically throughout meiotic progression (observed by immunofluorescence/confocal microscopy). siRNA knockdown of APC15 does not affect spindle organization but causes meiotic arrest at metaphase I and impairs removal of BUB3 from kinetochores, indicating APC15 is required for SAC inactivation and the metaphase-to-anaphase transition in oocytes. | PMID:40153087 | Journal of molecular histology |

## Citations

- PMID:21926987
- PMID:22940250
- PMID:23007861
- PMID:27591192
- PMID:27601667
- PMID:28366743
- PMID:28366744
- PMID:30341343
- PMID:40153087
