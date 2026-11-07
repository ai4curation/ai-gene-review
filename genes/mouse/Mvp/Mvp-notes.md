# Mvp (mouse, Q9EQK5) review notes

## Deep research

Deep-research providers (falcon, perplexity) have no API keys in this environment, so
no `-deep-research-*.md` file was generated. The literature search was done by hand
with PubMed E-utilities (esearch/esummary), and relevant hits were cached with
`ai-gene-review fetch-pmid`. The human MVP review (`genes/human/MVP/`) was the
starting point; its literature and decisions were reused where they apply.

Queries (PubMed, title/abstract):

- `"major vault protein"[tiab] AND (mice[tiab] OR mouse[tiab] OR knockout[tiab] OR deficient[tiab])` (45 hits)
- `"major vault protein"[tiab] AND (osteoclast*[tiab] OR bone[tiab])` (11 hits)
- `"major vault protein"[tiab] AND (dendritic[tiab] OR influenza[tiab])` (7 hits)
- `"major vault protein"[tiab] AND (vascular[tiab] OR mitophagy[tiab] OR hepatic[tiab] OR liver[tiab])` (30 hits)

Newly cached: PMID:12941141, 34158848, 37704623, 37267856, 35387478, 35246039,
29540554, 39069011, 26843330, 37192622, 19779459, 11149928, 41782382. No mouse
paper on vascular remodelling or mitophagy specifically involving Mvp turned up in
these searches.

## Mouse-specific evidence

- Structure: the 2.1 A structure of the first seven MVP repeats used mouse MVP cDNA
  [PMID:19779459 "together with the 2.1-A structure of the seven N-terminal domains
  (R1-R7) of MVP, reveal the interactions governing vault association"].
- Composition: vaults purified from mouse liver; TEP1 needed for vRNA association
  [PMID:11149928 "we have uncovered a novel role for TEP1 in vivo as an integral vault
  protein important for the stabilization and recruitment of the vault RNA to the vault
  particle"].
- Knockout: viable and healthy [PMID:12499273 "The MVP(-/-) mice are viable, healthy, and
  show no obvious abnormalities"]; dendritic cells normal [PMID:12941141 "In conclusion,
  vaults are not required for primary DC functions"].
- Myeloid phenotypes (Nanjing groups): obesity/atherosclerosis via TRAF6/NF-kappaB
  [PMID:30996248 "MVP interacts with TRAF6 preventing its recruitment to IRAK1 and
  subsequent oligomerization and ubiquitination"]; plaque instability via ASK1-JNK
  [PMID:35387478]; osteoclastogenesis via calcineurin-NFATc1 [PMID:34158848 "MVP
  negatively regulates osteoclast differentiation and bone resorption via inhibition of
  calcineurin-NFATc1 signaling"]; osteoclast apoptosis via Fas [PMID:37704623]; fracture
  repair / M2 polarisation [PMID:37267856].
- Antiviral: IL-6/IL-8 induction and influenza susceptibility [PMID:26843330]; antibody
  and germinal centre responses [PMID:39069011]; ferroptosis [PMID:41782382].
- Neuro: Mvp+/- visual cortical plasticity, STAT1 [PMID:29540554].
- Vault turnover by p62/NBR1 selective autophagy, including mouse tissues [PMID:37192622].

## Curation decisions

- All 28 GOA rows reviewed; actions kept consistent with human MVP.
- GO:0072376 protein activation cascade (mouse IMP, PMID:15133037): REMOVE plus
  source defect (WRONG_TERM, UNIPROT, DELETE_ROW), as for the human projection. The
  term definition (each product catalyses the next activation step) does not fit an
  effect on Ras/ERK/Elk-1 signalling; judged from the definition despite the
  abstract-only cache.
- GO:0008283 cell population proliferation (mouse IMP): MARK_AS_OVER_ANNOTATED, not
  REMOVE, out of deference to the full-text curator.
- NEW: GO:0005198 structural molecule activity (IDA, PMID:19779459, mouse protein) and
  GO:1990904 ribonucleoprotein complex (IDA, PMID:11149928, mouse liver vaults; mouse
  has no RNP row, unlike human's NAS row).
- No NEW process terms from the knockout phenotypes (NF-kappaB, osteoclast
  differentiation, antiviral responses): they are modulatory, partly overexpression-based,
  and mechanistically heterogeneous; raised as a suggested question instead, matching
  the human review, which also did not add them.
