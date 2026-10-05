---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AP3S2
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: P59780
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 3
citation_count: 2
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AP3S2 (human)

## Current model (mechanistic narrative)

AP3S2 (sigma3B) is a small-chain subunit of the AP-3 adaptor-like complex, an assembly that also contains ~47, ~140, and ~160 kDa chains and localizes to the trans-Golgi network region and peripheral endosomal structures marked by the transferrin receptor [PMID:9118953]. Within this complex, AP-3 engages tyrosine-based sorting signals such as the YQRL motif of TGN38 through its p47A medium chain, placing AP3S2 in the machinery that recognizes sorting determinants for intracellular protein trafficking [PMID:9118953]. Beyond its role as an AP-3 subunit, no further mechanistic detail of AP3S2's own activity has been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity
- **localization:** GO:0005794 Golgi apparatus, GO:0005768 endosome
- **pathway (Reactome):** R-HSA-5653656 Vesicle-mediated transport
- **partners:** NTRK3
- **complexes:** AP-3 adaptor complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1997 | High | AP3S2 (sigma3B) is a small chain component of the AP-3 adaptor-like complex, which also contains proteins of ~47, ~140, and ~160 kDa. The AP-3 complex localizes to the TGN region and peripheral structures containing the transferrin receptor, as determined by immunofluorescence microscopy. | PMID:9118953 | The EMBO journal |
| 1997 | Medium | The AP-3 complex containing AP3S2 (sigma3B) is involved in recognition of tyrosine-based sorting signals (YQRL from TGN38), mediated through the p47A medium chain subunit of the complex. | PMID:9118953 | The EMBO journal |
| 2024 | Low | AP3S2 was identified as a fusion partner with NTRK3 (AP3S2-NTRK3 fusion) in a patient with malignant melanoma, creating an oncogenic driver that was clinically responsive to a TRK inhibitor (BPI-28592). | PMID:39256512 | NPJ precision oncology |

## Citations

- PMID:39256512
- PMID:9118953
