---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ATP1B4
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9UN42
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 8
citation_count: 8
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ATP1B4 (human)

## Current model (mechanistic narrative)

ATP1B4 encodes BetaM, a protein that in placental mammals has been functionally repurposed from its ancestral Na,K-ATPase β-subunit role into a muscle-specific gene-regulatory factor of the inner nuclear membrane [PMID:14656723, PMID:17592128]. In perinatal skeletal myocytes BetaM accumulates at the nuclear envelope rather than the plasma membrane and does not associate with Na,K-ATPase α-subunits; its transmembrane domain is required for this nuclear envelope targeting [PMID:14656723]. From this location BetaM acts on muscle transcriptional programs through two routes: it binds the transcriptional co-regulator SKIP via nucleoplasmic residues 72–98 to control TGF-β-responsive transcription and upregulate the inhibitory Smad7 [PMID:17592128, PMID:26939788], and it independently occupies the distal regulatory region of the MyoD gene, drives activating epigenetic changes, and recruits the SWI/SNF remodeler BRG1 to stimulate MyoD expression [PMID:36836771]. Beyond development, BetaM is an ongoing metabolic regulator: ablation of Atp1b4 in adult mice raises energy expenditure, fat oxidation, and skeletal-muscle β-oxidation while improving glucose and insulin tolerance [PMID:40724605]. In a diabetic sarcopenia model, ATP1B4 overexpression acts upstream to suppress PI3K/AKT/mTOR signaling and activate mitophagy markers, exacerbating muscle atrophy [PMID:41022280].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140110 transcription regulator activity, GO:0003677 DNA binding
- **localization:** GO:0005635 nuclear envelope, GO:0000228 nuclear chromosome
- **pathway (Reactome):** R-HSA-74160 Gene expression (Transcription), R-HSA-4839726 Chromatin organization, R-HSA-1430728 Metabolism
- **partners:** SKIP, BRG1
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2007 | High | In placental mammals, BetaM (encoded by ATP1B4) localizes to the nuclear membrane of perinatal myocytes and directly interacts with the transcriptional co-regulator SKIP (SKI-interacting protein). Through this interaction, eutherian BetaM regulates TGF-β-responsive reporters and augments mRNA levels of Smad7, an inhibitor of TGF-β signaling, demonstrating a gene-regulatory function entirely distinct from its ancestral Na,K-ATPase β-subunit role. | PMID:17592128 | Proceedings of the National Academy of Sciences of the United States of America |
| 2003 | High | BetaM (ATP1B4) localizes specifically to nuclear envelopes of perinatal skeletal myocytes, not in plasma membrane association with Na,K-ATPase α-subunits. The transmembrane domain is required for nuclear envelope targeting; deletion of the transmembrane domain causes redistribution to cytoplasm and nucleoplasm. No Na,K-ATPase α-subunit was detected in myonuclear membranes, confirming BetaM does not associate with Na,K-ATPase in this context. | PMID:14656723 | American journal of physiology. Cell physiology |
| 2016 | Medium | Expanded yeast two-hybrid and split-ubiquitin screening identified the eutherian BetaM interactome, including lamina-associated protein LAP-1, nuclear envelope protein Syne1, heme oxidases HMOX1 and HMOX2, transcription factor LZIP/CREB3, ERGIC3, PHF3, reticulocalbin-3, β-sarcoglycan, and BetaM itself (self-interaction). Residues 72–98 in the nucleoplasmic domain (adjacent to the transmembrane segment) are required for interaction with SKIP. No new interactions were found for chicken BetaM or human Na,K-ATPase β1, β2, β3 isoforms, indicating these interactions are unique to eutherian BetaM. | PMID:26939788 | Scientific reports |
| 2011 | High | Native eutherian BetaM protein isolated from pig neonatal skeletal muscle corresponds to splice variant B (351 amino acids) and carries N-glycans of the high-mannose type with a carbohydrate moiety of ~5.9 kDa. The protein is highly sensitive to endogenous proteases, distinguishing it structurally from other Na,K-ATPase β-subunits. | PMID:21855530 | Biochemical and biophysical research communications |
| 2023 | Medium | Eutherian BetaM binds to the distal regulatory region (DRR) of the MyoD gene independently of SKIP, promotes epigenetic changes associated with transcriptional activation, and recruits the SWI/SNF chromatin remodeling subunit BRG1, thereby stimulating MyoD expression in neonatal skeletal muscle and C2C12 myoblasts. | PMID:36836771 | Life (Basel, Switzerland) |
| 2025 | High | Ablation of Atp1b4 (Atp1b4-/Y male mice) results in lower body weight and adiposity, higher energy expenditure (heat production, oxygen consumption), greater locomotor activity, lower respiratory exchange ratio indicating increased fat oxidation, enhanced β-oxidation in skeletal muscle, and improved glucose and insulin tolerance, demonstrating that eutherian BetaM regulates adult mouse metabolism. | PMID:40724605 | Life (Basel, Switzerland) |
| 2025 | Medium | Ablation of Atp1b4 in mice leads to lower body weight, lower adiposity, lower fasting blood glucose, enhanced insulin sensitivity, improved glucose tolerance, higher heat production, elevated oxygen consumption, higher locomotor activity, and lower respiratory exchange ratio, confirming a role for eutherian BetaM in regulating adult mouse energy and fat metabolism. | PMID:bio_10.1101_2025.02.26.640446 | bioRxiv |
| 2025 | Medium | In a rat model of diabetic sarcopenia, ATP1B4 overexpression suppresses PI3K/AKT/mTOR signaling and activates mitophagy markers (LC3-II, DRP1, ATG9), exacerbating muscle atrophy, collagen accumulation, and glycogen deposition; knockdown reverses these effects. ATP1B4 expression remained unchanged following PI3K/AKT/mTOR pathway modulation, supporting an upstream (unidirectional) regulatory role of ATP1B4 over this pathway. Co-overexpression of ATP1B4 abolished the protective effects of PI3K pathway activation. | PMID:41022280 | The international journal of biochemistry & cell biology |

## Citations

- PMID:14656723
- PMID:17592128
- PMID:21855530
- PMID:26939788
- PMID:36836771
- PMID:40724605
- PMID:41022280
- PMID:bio_10.1101_2025.02.26.640446
