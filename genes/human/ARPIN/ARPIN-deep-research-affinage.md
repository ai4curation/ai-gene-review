---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARPIN
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q7Z6K5
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

# Affinage mechanistic annotation for ARPIN (human)

## Current model (mechanistic narrative)

Arpin is a steric inhibitor of the Arp2/3 actin-nucleating complex that acts within a Rac-driven negative feedback loop to limit the persistence of lamellipodial protrusion and directional cell migration [PMID:26235381]. It engages Arp2/3 through a VCA-related acidic C-terminal tail that mimics WASP-family nucleation-promoting factors, but occupies only the single binding site on Arp3 and, via a C-helix at the Arp3 barbed end, induces an open, nucleation-inactive conformation rather than activating the complex [PMID:35110533, PMID:27939292]. The acidic tail extends as a linear, readily accessible peptide from a globular core that adopts a fold distinct from other Arp2/3-binding factors, and Arpin homodimerizes through a conserved interface to cooperatively enhance Arp2/3 inhibition [PMID:26774128, PMID:bio_10.1101_2025.06.24.661301]. The same acidic tail binds Tankyrase 1/2 at an overlapping site, defining a second pathway: only mutations disrupting both Arp2/3 and Tankyrase binding fully abolish Arpin's control of migration persistence [PMID:33923443]. Beyond cytoplasmic actin regulation, Arpin acts in the nucleus to suppress homology-directed DNA repair by inactivating nuclear Arp2/3 [PMID:39118570], is required for F-actin phagocytic cup completion in macrophages where it is targeted by human rhinovirus 16 [PMID:31721415], and stabilizes epithelial and endothelial junctional barriers, the latter through an Arp2/3-independent ROCK1/ZIPK actomyosin pathway [PMID:34012961, PMID:39298260].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity, GO:0008092 cytoskeletal protein binding
- **localization:** GO:0005856 cytoskeleton, GO:0005634 nucleus, GO:0005886 plasma membrane
- **pathway (Reactome):** *(none)*
- **partners:** ACTR3, TNKS, TNKS2, CDH1, OCLN, CLDN1
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2022 | High | Cryo-EM structure of Arpin bound to Arp2/3 complex at 3.24-Å resolution revealed that Arpin binds Arp2/3 complex similarly to WASP-family nucleation-promoting factors (NPFs), but only occupies the single site on Arp3 (not the Arp2-ArpC1 site). Arpin possesses a C-helix that binds at the barbed end of Arp3, and mutagenesis of sequence differences within the C-helix defined the molecular basis for inhibition by Arpin vs. activation by NPFs. | PMID:35110533 | Nature communications |
| 2016 | High | Single-particle electron microscopy showed that Arpin, using VCA-related acidic (A) motifs to interact with Arp2/3 complex, induces the 'open' nucleation-inactive conformation of Arp2/3 complex, with two new masses appearing near Arp2 and Arp3. Arpin showed additive inhibitory effects on Arp2/3 complex with Coronin and GMF. | PMID:27939292 | Journal of molecular biology |
| 2016 | High | Hybrid structural analysis (synchrotron SAXS of full-length Arpin; X-ray crystallography of the acidic tail in complex with an ankyrin repeats domain) revealed that Arpin's acidic tail extends from the globular core as a linear peptide forming a primary binding epitope that is readily accessible in unbound Arpin and sufficient to tether Arpin to interacting proteins with high affinity. | PMID:26774128 | Structure |
| 2021 | High | Arpin interacts with both Tankyrase 1 and 2 (TNKS) through a C-terminal binding site on its acidic tail that overlaps with the Arp2/3-binding site, identified by yeast two-hybrid screening and confirmed by co-immunoprecipitation. Arpin was found to dissolve the liquid-liquid phase separation of TNKS upon overexpression. Point mutations impairing interaction with either Arp2/3 or TNKS alone were insufficient to abolish Arpin's control of migration persistence; only a mutation affecting both interactions rendered Arpin completely inactive, indicating two independent pathways. | PMID:33923443 | International journal of molecular sciences |
| 2015 | Medium | Arpin is activated by the small GTPase Rac downstream of Rac-driven lamellipodium formation, closing a negative feedback loop that renders protrusions unstable. Mechanistic trajectory analysis showed that Arpin acts by inducing more frequent pausing of cell migration, during which cells are more likely to change direction, thereby controlling directional persistence. | PMID:26235381 | Cytoskeleton (Hoboken, N.J.) |
| 2019 | Medium | Arpin is recruited to sites of membrane extension and phagosome closure in macrophages. Arpin depletion results in stalled phagocytic cups with accumulated F-actin and defective internalization; re-expression of Arpin rescues phagocytosis, demonstrating Arpin is required for efficient F-actin cup formation and phagosome completion. Human rhinovirus 16 downregulates Arpin expression to impair phagocytosis. | PMID:31721415 | EMBO reports |
| 2021 | Medium | Arpin depletion in intestinal epithelial cells alters architecture of adherens junctions and tight junctions, increases actin filament content and actomyosin contractility, and significantly increases epithelial permeability. Arpin co-precipitates with TJ proteins occludin and claudin-1 and AJ protein E-cadherin, indicating physical association with junctional complexes. | PMID:34012961 | Frontiers in cell and developmental biology |
| 2024 | Medium | Arpin depletion in endothelial cells causes formation of actomyosin stress fibers and increased vascular permeability through an Arp2/3-independent mechanism. Instead, ROCK1 and ZIPK kinase inhibitors normalize the loss-of-arpin effects on actin filaments and permeability. Arpin-deficient mice show vascular phenotypes including edema, microhemorrhage, vascular congestion, increased F-actin, and increased permeability. | PMID:39298260 | eLife |
| 2024 | Medium | Arpin depletion in cells increases homology-directed DNA repair (HDR) efficiency two-fold, as measured by a specific HDR assay, through its ability to inactivate the Arp2/3 complex in the nucleus. Arpin-null cells display enhanced clustering of DNA double-strand breaks (DSBs) upon DNA damage treatment, consistent with Arp2/3 complex promoting DSB clustering for HDR. | PMID:39118570 | Biology of the cell |
| 2017 | Low | Arpin overexpression inhibited phosphorylation of Akt in breast cancer cells, and co-expression of a constitutively active form of Akt blunted the suppression of cell proliferation and invasion by Arpin, placing Arpin upstream of Akt signaling in breast cancer cell context. | PMID:28531800 | Biomedicine & pharmacotherapy |
| 2017 | Medium | Arpin-depleted tumour cells and Arpin-knockout Dictyostelium amoeba showed no obvious defect in chemotaxis, demonstrating that Arpin is dispensable for chemotaxis (negative result for a proposed function). | PMID:28186323 | Biology of the cell |
| 2025 | Medium | Crystal structure of Arpin's N-terminal globular domain at 1.65-Å resolution revealed a unique structural fold distinct from all known Arp2/3-binding factors. Biophysical analyses demonstrated that Arpin forms homodimers via a conserved interface, and homodimerization is essential for cooperative (positive synergy) inhibition of Arp2/3-dependent actin polymerization. | PMID:bio_10.1101_2025.06.24.661301 | bioRxiv |

## Citations

- PMID:26235381
- PMID:26774128
- PMID:27939292
- PMID:28186323
- PMID:28531800
- PMID:31721415
- PMID:33923443
- PMID:34012961
- PMID:35110533
- PMID:39118570
- PMID:39298260
- PMID:bio_10.1101_2025.06.24.661301
