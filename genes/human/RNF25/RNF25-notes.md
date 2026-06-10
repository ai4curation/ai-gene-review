# RNF25 (AO7) — research notes

UniProt: Q96BH1. RING-H2 E3 ubiquitin ligase (RING-H2_RNF25, RWD domain + RING). Cytoplasmic.

## Core function — RQC / translation quality control
RNF25 is a RING E3 ubiquitin ligase acting in the **RNF14-RNF25 translation quality control pathway**
on stalled/collided ribosomes.
- Catalyzes ubiquitination of RPS27A/eS31 in response to ribosome collisions, promoting activation of RNF14.
- Ubiquitinates other ribosomal proteins (uL... eS...) and stalled ETF1/eRF1 for degradation.
  [file:human/RNF25/RNF25-uniprot.txt "E3 ubiquitin-protein ligase that plays a key role in the RNF14-RNF25 translation quality control pathway"]
  [file:human/RNF25/RNF25-uniprot.txt "Catalyzes ubiquitination of RPS27A in response to ribosome collisions, promoting activation of RNF14"]
- [PMID:36638793 "An E3 ligase network engages GCN1 to promote the degradation of translation factors on stalled ribosomes"] — RNF14 + RNF25 required for eEF1A degradation; RNF25 ubiquitinates RPS27A/eS31 as a second signal.
- [PMID:37651229 "E3 ubiquitin ligases RNF14 and RNF25"] — drug (eRF1-trapping)-induced readthrough via RNF14/RNF25 degradation of eRF1.
- [PMID:37951216 "RNF14-dependent atypical ubiquitylation promotes translation-coupled resolution of RNA-protein crosslinks"] — RNF25 acts with RNF14 in resolving RNA-protein crosslinks (collision-coupled).
- [PMID:37951215 "K6-linked ubiquitylation marks formaldehyde-induced RNA-protein crosslinks"] — atypical K6-linked ubiquitination (GO:0085020); RNF25 IDA.
- [PMID:27863242] cryo-EM/RQC study: RNF25 K6-linked ubiquitination, cytosolic ribosome, ubiquitin protein ligase activity.

## E2 interaction / catalysis
- Interacts with UBE2D2 (UbcH5B), may interact with UBE2E1/E3. RWD domain binds E2.
  [PMID:26475854 "Insights into Ubiquitination from the Unique Clamp-like Binding of the RING E3 AO7 to the E2 UbcH5B"]

## Moonlighting / older
- Originally cloned as AO7, supports NF-kB (RELA/p65)-mediated transcription [PMID:12748188]; nuclear+cytosol IDA, NF-kB binding IPI. Keep non-core.
- Mediates ubiquitination/degradation of NKD2 (by similarity).

## Action plan
- Core MF: GO:0061630 ubiquitin protein ligase activity. Core BP: GO:0072344 rescue of stalled cytosolic ribosome; GO:0006511 ubiquitin-dependent protein catabolic process; GO:0085020 K6-linked ubiquitination; GO:0160127 protein-RNA covalent cross-linking repair.
- protein binding IPI (HT screens, E2s): keep non-core / over-annotated.
- NF-kB binding, nucleus: keep non-core (older AO7 role).
