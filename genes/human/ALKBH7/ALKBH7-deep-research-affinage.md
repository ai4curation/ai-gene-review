---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ALKBH7
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q9BT30
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 12
citation_count: 12
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ALKBH7 (human)

## Current model (mechanistic narrative)

ALKBH7 is a mitochondrial matrix-localized α-ketoglutarate–dependent dioxygenase that links mitochondrial RNA metabolism to cell-death and metabolic programs [PMID:34253897, PMID:23572141, PMID:25122757]. Crystallographic analysis defines a double-stranded β-helix fold coordinating a catalytic iron through a conserved HX(D/E)…H motif, with observed self-hydroxylation of Leu-110 confirming hydroxylase activity, and a solvent-exposed active site lacking the nucleotide-recognition lid of other AlkB members [PMID:25122757]. Functionally, ALKBH7 acts as an RNA demethylase that site-specifically removes m2,2G from mitochondrial Ile pre-tRNA and m1A from Leu1 pre-tRNA regions within nascent polycistronic transcripts; its loss accelerates polycistronic RNA processing, lowers steady-state mitochondrial tRNA levels, and reduces mitochondrial translation and activity [PMID:34253897]. Independently, ALKBH7 is required for alkylation- and oxidation-induced programmed necrosis downstream of PARP hyperactivation, where it triggers collapse of mitochondrial membrane potential and NAD/ATP depletion without affecting apoptosis [PMID:23666923], a phenotype that is tissue- and sex-specific in vivo [PMID:28726787]. ALKBH7 also governs mitochondrial fatty acid and dialdehyde metabolism: its genetic deletion impairs short-chain fatty acid utilization and increases adiposity [PMID:23572141], elevates glyoxalase I and methylglyoxal adducts, and confers cardiac protection against ischemia-reperfusion injury through a GLO-1–dependent route [PMID:32795389]. Its expression is transcriptionally downregulated by HIF-1α binding to the ALKBH7 promoter, and ALKBH7 loss provokes mitochondrial damage and cGAS-STING activation via downregulation of UQCRC2 [PMID:40140527].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140098 catalytic activity, acting on RNA, GO:0016491 oxidoreductase activity, GO:0140096 catalytic activity, acting on a protein
- **localization:** GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-8953854 Metabolism of RNA, R-HSA-5357801 Programmed Cell Death, R-HSA-1430728 Metabolism
- **partners:** HIF1A
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2021 | High | ALKBH7 is an RNA demethylase that site-specifically demethylates m2,2G within mitochondrial Ile pre-tRNA and m1A within mitochondrial Leu1 pre-tRNA regions in nascent polycistronic mitochondrial RNA. ALKBH7 depletion leads to increased polycistronic mitochondrial RNA processing, reduced steady-state mitochondria-encoded tRNA levels, reduced mitochondrial protein translation, and decreased mitochondrial activity. | PMID:34253897 | Nature cell biology |
| 2013 | High | ALKBH7 is required for alkylation- and oxidation-induced programmed necrosis. After severe DNA damage and PARP hyperactivation, ALKBH7 triggers collapse of mitochondrial membrane potential and large-scale loss of mitochondrial function leading to energy (NAD/ATP) depletion and cell death. ALKBH7-depleted cells undergo PARP hyperactivation and NAD depletion but rapidly recover NAD and ATP, maintain mitochondrial membrane potential, plasma membrane integrity, and viability. ALKBH7 has no effect on apoptotic cell death. | PMID:23666923 | Genes & development |
| 2013 | High | Mouse ALKBH7 localizes to the mitochondrial matrix, and genetic deletion of Alkbh7 dramatically increases body weight and fat mass. Alkbh7-/- mice show impaired utilization of short-chain fatty acids, implicating ALKBH7 in mitochondrial fatty acid metabolism. | PMID:23572141 | Journal of molecular cell biology |
| 2014 | High | Crystal structures of human ALKBH7 in complex with Mn(II) and α-ketoglutarate (1.35 Å) or N-oxalylglycine (2.0 Å) reveal a conserved double-stranded β-helix fold coordinating a catalytic iron via a conserved HX(D/E)…Xn…H motif. Self-hydroxylation of Leu-110 was observed, indicating ALKBH7 can catalyze hydroxylation. ALKBH7 lacks the 'nucleotide recognition lid' present in other AlkB members, resulting in a solvent-exposed active site and a negatively charged groove, suggesting it acts on protein rather than nucleic acid substrates. | PMID:25122757 | The Journal of biological chemistry |
| 2020 | Medium | ALKBH7 regulates dialdehyde (glyoxal) metabolism in mitochondria. Alkbh7-/- mice have elevated glyoxalase I (GLO-1) levels and rewired methylglyoxal (MGO) metabolic pathways with elevated MGO protein adducts. Multi-omics analysis found no evidence that ALKBH7 functions as a prolyl-hydroxylase. Hearts from Alkbh7-/- mice are protected against ischemia-reperfusion injury in a manner blocked by GLO-1 inhibition, placing ALKBH7 upstream of GLO-1 in dialdehyde metabolism and necrosis signaling. | PMID:32795389 | eLife |
| 2017 | Medium | ALKBH7 modulates alkylation-induced necrosis in a tissue- and sex-specific manner in vivo. ALKBH7-deficient mice are more resistant to MMS-induced toxicity in males but not females. ALKBH7 deficiency protects retinal photoreceptors and cerebellar granule cells (cell types that undergo necrosis via BER pathway and PARP1/ARTD1 hyperactivation) against alkylation-induced death, with cerebellar protection specific to male mice. | PMID:28726787 | Cell death & disease |
| 2017 | Medium | A prostate cancer-associated SNP in ALKBH7 (rs7540) causes a structural change that reduces ALKBH7's ability to bind its cosubstrate (α-ketoglutarate). Experimental spectroscopy with purified wild-type and variant proteins validated molecular dynamics simulation predictions of impaired cosubstrate binding. | PMID:28231280 | PLoS computational biology |
| 2019 | Low | IP-MS/MS identified ALKBH7 interactors in mitochondria. ALKBH7 knockdown leads to upregulation of UQCRH and HMGN1 protein levels, while overexpression produces the opposite pattern, placing ALKBH7 as a regulator of these proteins involved in protein homeostasis, lipid metabolism, and programmed necrosis. | PMID:31889914 | Proteome science |
| 2025 | Medium | HIF-1α directly binds the ALKBH7 promoter (chromosome 19 region 6372400–6372578, motif ACCGTGGC) to transcriptionally downregulate ALKBH7 expression. ALKBH7 knockdown induces mitochondrial damage and activates cGAS-STING signaling by downregulating UQCRC2. Overexpression of ALKBH7 resists hypoxia-induced mitochondrial damage and fibroblast-like synoviocyte (FLS) activation. | PMID:40140527 | Acta pharmacologica Sinica |
| 2025 | Medium | Bismuth drugs specifically bind ALKBH7 (a mitochondrial iron-binding protein) and deplete it in kidney tissue. ALKBH7 gene knockout or silencing increases cell survival upon excessive cisplatin exposure, and bismuth treatment prevents cisplatin-induced acute kidney injury in mice by targeting ALKBH7. | PMID:40484038 | Biochemical pharmacology |
| 2025 | Medium | NMR backbone resonance assignment of full-length human ALKBH7 shows that the active site and C-terminal regions are dynamic on an intermediate exchange timescale (NMR-invisible), consistent with the previously reported X-ray structure. This establishes that ALKBH7 has conformational dynamics at its active site relevant to substrate recognition and enzyme regulation. | PMID:39881053 | Biomolecular NMR assignments |
| 2025 | Low | In Drosophila, overexpression of Alkbh7 (the ortholog of human ALKBH7) increases resistance to octanoic acid (a short-chain fatty acid), consistent with ALKBH7's established role in mitochondrial fatty acid metabolism. Alkbh7 shows elevated expression in OA-resistant fly populations and mutation of Alkbh7 in D. sechellia reduces OA tolerance. | PMID:bio_10.1101_2025.07.23.666417 | bioRxiv |

## Citations

- PMID:23572141
- PMID:23666923
- PMID:25122757
- PMID:28231280
- PMID:28726787
- PMID:31889914
- PMID:32795389
- PMID:34253897
- PMID:39881053
- PMID:40140527
- PMID:40484038
- PMID:bio_10.1101_2025.07.23.666417
