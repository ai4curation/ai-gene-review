---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANKRD9
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q96BM1
self_evaluation_pairwise: win
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

# Affinage mechanistic annotation for ANKRD9 (human)

## Current model (mechanistic narrative)

ANKRD9 is a metabolically regulated ankyrin-repeat protein that functions as the substrate-recognition subunit of a CUL5–ELOB–ELOC–RNF7 cullin-RING E3 ubiquitin ligase, targeting the purine-biosynthesis enzymes IMPDH1 and IMPDH2 for ubiquitination and proteasomal degradation [PMID:30293565]. Its control of IMPDH2 is coupled to cellular nutrient and guanosine status: under basal conditions ANKRD9 is sequestered in vesicle-like structures away from cytosolic IMPDH2, but upon nutrient limitation it relocalizes and co-assembles with IMPDH2 into rod-like filaments, a vesicle-to-rod transition and IMPDH2 binding that requires its conserved Cys109–Cys110 motif; guanosine addition reverses rod formation and restores the vesicular pattern [PMID:31337707]. Through this IMPDH2-degrading activity ANKRD9 acts as a negative regulator of skeletal myogenesis, where its overexpression suppresses myoblast proliferation and differentiation and its knockdown increases muscle mass, effects reversed by restoring IMPDH2 [PMID:41691811]. In intestinal enterocytes ANKRD9 regulates purine-biosynthesis enzymes to sustain ATP synthesis, and its loss in mice lowers intestinal ATP, alters Golgi morphology, delays ApoB/chylomicron trafficking, and produces lipid accumulation with a lean phenotype, linking purine metabolism to dietary fat absorption [PMID:41826336].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0016874 ligase activity, GO:0060090 molecular adaptor activity
- **localization:** GO:0005829 cytosol, GO:0031410 cytoplasmic vesicle
- **pathway (Reactome):** R-HSA-392499 Metabolism of proteins, R-HSA-1430728 Metabolism
- **partners:** IMPDH2, IMPDH1, CUL5, ELOB, ELOC, RNF7
- **complexes:** CUL5-ELOB-ELOC-RNF7 cullin-RING E3 ubiquitin ligase

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2018 | High | ANKRD9 functions as a substrate receptor subunit of a CUL5-based cullin-RING E3 ubiquitin ligase complex, assembling with CUL5 (not CUL2), ELOB, ELOC, and RNF7 subunits. Both isoforms of inosine monophosphate dehydrogenase (IMPDH1 and IMPDH2) are cognate substrates of this complex; ANKRD9 recognizes IMPDH isoforms and is required for their ubiquitination and proteasomal degradation. | PMID:30293565 | Biochimica et biophysica acta. Molecular basis of disease |
| 2019 | High | ANKRD9 facilitates degradation of IMPDH2 in a metabolically-controlled manner. Under basal conditions ANKRD9 is segregated from cytosolic IMPDH2 in vesicle-like structures. Upon nutrient limitation, ANKRD9 loses its vesicular pattern and co-assembles with IMPDH2 into rod-like filaments. Inhibition of IMPDH2 activity with ribavirin promotes ANKRD9 binding to IMPDH2 rods, while guanosine addition reverses rod formation and restores ANKRD9 to vesicle-like structures. The conserved Cys109-Cys110 motif in ANKRD9 is required for the vesicle-to-rod transition and for IMPDH2 binding and regulation. ANKRD9 knockdown increases IMPDH2 levels and prevents IMPDH2 rod formation upon nutrient limitation. | PMID:31337707 | The Journal of biological chemistry |
| 2009 | Medium | ANKRD9 mRNA is dramatically induced in riboflavin-deficiency-induced fatty acid oxidation disorders in chicken liver. Hepatic ANKRD9 mRNA is repressed by thyroid hormone (T3) and fasting, elevated by re-feeding after fasting, and reduced in response to apoptosis. GFP-tagged ANKRD9 localizes to the cytoplasm. | PMID:19788857 | BMB reports |
| 2026 | Medium | ANKRD9 negatively regulates skeletal myogenesis in chicken by directly binding IMPDH2 and promoting its ubiquitin-mediated proteasomal degradation without affecting IMPDH2 mRNA levels. ANKRD9 overexpression inhibits myoblast proliferation and differentiation, while knockdown enhances these processes. In vivo siRNA-mediated ANKRD9 knockdown increases muscle mass and myofiber diameter. Rescue experiments restoring IMPDH2 expression reversed the inhibitory effects of ANKRD9, confirming that IMPDH2 degradation mediates the myogenic inhibition. | PMID:41691811 | Poultry science |
| 2026 | High | ANKRD9 couples ATP synthesis and lipoprotein trafficking in intestinal enterocytes. ANKRD9 regulates enzymes within the purine biosynthesis pathway to increase ATP synthesis. Intracellular localization of ANKRD9 is lipid- and ATP-dependent. Inactivation of Ankrd9 in mice reduces intestinal ATP (despite intact mitochondrial and glycolytic function), alters Golgi morphology, delays ApoB/chylomicron trafficking, and causes lipid accumulation in enterocytes along with a lean body phenotype. | PMID:41826336 | Nature communications |
| 2026 | Low | Overexpression of ANKRD9 in chicken primary myoblasts significantly inhibits IMP metabolism, as measured by ELISA, indicating ANKRD9 plays a key role in negative regulation of IMP accumulation through the purine metabolic pathway. | PMID:41769753 | British poultry science |

## Citations

- PMID:19788857
- PMID:30293565
- PMID:31337707
- PMID:41691811
- PMID:41769753
- PMID:41826336
