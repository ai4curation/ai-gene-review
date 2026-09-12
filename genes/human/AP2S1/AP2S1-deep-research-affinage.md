---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AP2S1
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: P53680
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 7
citation_count: 7
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AP2S1 (human)

## Current model (mechanistic narrative)

AP2S1 encodes the σ2 (AP17) subunit of the heterotetrameric AP2 clathrin adaptor complex, which links clathrin to the plasma membrane and recognizes tyrosine- and dileucine-based sorting motifs of cargo proteins during clathrin-mediated endocytosis [PMID:23222959, PMID:9040778]. Within the assembled complex, Arg15 of AP2σ2 contacts the dileucine motif of cargo, and missense mutations at this residue impair both AP2σ2 association with the other AP2 subunits (AP2α, AP2β2, AP2μ2) and its interaction with the calcium-sensing receptor (CaSR), reducing CaSR endocytosis and CaSR-mediated calcium signaling [PMID:23222959, PMID:33729479]. These loss-of-function mutations cause familial hypocalciuric hypercalcemia type 3, recapitulated in Arg15Leu knock-in mice that display hypercalcaemia, hypermagnesaemia, and hypophosphataemia [PMID:33729479]. The cargo-adaptor role extends beyond Arg15: variants at Arg10, Lys18, and Arg61 likewise disrupt AP2 complex formation and reduce general clathrin-mediated endocytosis [PMID:bio_10.1101_2024.07.22.24310683]. Independent of its endocytic function, AP2S1 also restrains amyloid precursor protein (APP) degradation by limiting RAB9-positive late endosome-to-LAMP1-positive lysosome fusion via VPS41, such that its depletion lowers APP and Aβ levels [PMID:36412210]. AP2σ2 is essential for development, as homozygous Ap2s1 loss is embryonic lethal while heterozygotes are haplosufficient [PMID:29479578].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0038024 cargo receptor activity
- **localization:** GO:0005886 plasma membrane, GO:0005768 endosome, GO:0005764 lysosome
- **pathway (Reactome):** R-HSA-5653656 Vesicle-mediated transport, R-HSA-1643685 Disease
- **partners:** AP2A1, AP2B1, AP2M1, CASR, VPS41, ITSN1
- **complexes:** AP2 adaptor complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2012 | High | AP2S1 encodes the σ2 subunit of the AP2 heterotetramer (α, β, μ, σ), which links clathrin to vesicle membranes and binds tyrosine- and dileucine-based motifs of membrane-associated cargo proteins during clathrin-mediated endocytosis. Missense mutations at Arg15 of AP2σ2, which forms key contacts with dileucine-based motifs of CCV cargo proteins, impair CaSR endocytosis, reduce CaSR-mediated intracellular signaling, and decrease sensitivity of CaSR-expressing cells to extracellular calcium, likely through loss of interaction with a C-terminal CaSR dileucine-based motif. | PMID:23222959 | Nature genetics |
| 1996 | Medium | The human AP2S1 gene (symbol CLAPS2) encodes AP17, the small (sigma) chain of the clathrin-associated AP-2 complex, and maps to chromosome 19q13.2→q13.3. | PMID:9040778 | Cytogenetics and cell genetics |
| 1998 | Medium | AP2S1 (CLAPS2) undergoes alternative splicing to produce a variant transcript encoding AP17Δ, a 142 aa protein lacking 38 aa of the canonical AP17; both transcripts are expressed in leukocytes and leukemia cells. | PMID:9767099 | Gene |
| 2017 | High | ENU-induced deletion of 17 evolutionarily conserved amino acids forming part of the AP2σ α1-helix, α1-β3 loop, and β3 strand (del17 splice-site variant) results in a non-functional AP2σ. Homozygous Ap2s1 knockout mice are non-viable and die between embryonic days 3.5 and 9.5, demonstrating that AP2σ is essential for embryonic patterning and organogenesis. Heterozygous mice are haplosufficient with normal calcium homeostasis. | PMID:29479578 | JBMR plus |
| 2021 | High | The AP2S1 p.Arg15Leu mutation impairs protein-protein interactions between AP2σ2 and the other AP2 complex subunits (AP2α, AP2β2, AP2μ2), and also reduces the AP2σ2–CaSR interaction, as demonstrated by co-immunoprecipitation. CRISPR/Cas9 knock-in mice harboring p.Arg15Leu recapitulate FHH3 with hypercalcaemia, hypermagnesaemia, and hypophosphataemia; cinacalcet reduced plasma calcium and PTH in these mice but did not restore the diminished AP2σ2–CaSR interaction in vitro. | PMID:33729479 | Human molecular genetics |
| 2022 | High | AP2S1 regulates the degradation of amyloid precursor protein (APP) through a mechanism involving late endosome (LE)-to-lysosome fusion rather than endocytosis per se. Knockdown of AP2S1 promoted translocation of APP from RAB9-positive late endosomes to LAMP1-positive lysosomes and enhanced LE-lysosome fusion; this was prevented by silencing VPS41, a component required for LE-lysosome fusion. AAV-mediated AP2S1 knockdown in hippocampus of APP/PS1 mice reduced APP and Aβ levels and improved cognitive function. | PMID:36412210 | Traffic (Copenhagen, Denmark) |
| 2024 | Medium | Five AP2S1 variants at residues other than Arg15 (p.Arg10Trp, p.Arg10Gln, p.Lys18Glu, p.Lys18Asn, p.Arg61His) decrease cell viability, reduce clathrin-mediated endocytosis (transferrin uptake assay), and disrupt interactions between AP2σ2 and other AP2 complex subunits, thereby impairing AP2 complex formation. The p.Arg10Trp variant additionally shows reduced interactions with 44 human proteins including intersectin-1, a component required for clathrin-coated pit formation and synaptic vesicle dynamics. | PMID:bio_10.1101_2024.07.22.24310683 | bioRxiv |

## Citations

- PMID:23222959
- PMID:29479578
- PMID:33729479
- PMID:36412210
- PMID:9040778
- PMID:9767099
- PMID:bio_10.1101_2024.07.22.24310683
