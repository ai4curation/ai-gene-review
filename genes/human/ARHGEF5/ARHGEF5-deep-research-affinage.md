---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARHGEF5
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q12774
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

# Affinage mechanistic annotation for ARHGEF5 (human)

## Current model (mechanistic narrative)

ARHGEF5 (TIM) is a Dbl-family Rho guanine nucleotide exchange factor that drives actin cytoskeletal remodeling, cell migration, and invasion by activating Rho-family GTPases [PMID:19713215, PMID:21525037]. In vitro GEF assays establish that it strongly activates RhoA and RhoB and more weakly RhoC and RhoG, but not Rac1 or other Rho proteins [PMID:19713215]. Its exchange activity is restrained by an intramolecular autoinhibitory mechanism in which the C-terminal SH3 domain engages a poly-proline sequence adjacent to the DH domain; disrupting this SH3–poly-proline interaction with designed peptide or peptoid ligands directly relieves autoinhibition and stimulates RhoA exchange in a manner that scales with ligand affinity [PMID:25645980, PMID:31197859]. ARHGEF5 integrates multiple upstream inputs: it binds the Src SH3 domain, is tyrosine-phosphorylated by Src, reciprocally promotes Src activity, and forms a Src–ARHGEF5–PI3K ternary complex required for RhoA/Cdc42-dependent podosome formation, a function dependent on its PH domain [PMID:21525037]; it is also activated by Gβγ to stimulate RhoA, supporting chemokine-driven dendritic-cell migration [PMID:19713215], and it operates within an integrin–ODAM–ARHGEF5–RhoA axis controlling junctional epithelium adhesion [PMID:25911094]. ARHGEF5 is upregulated during TGF-β-induced EMT and promotes migration through Rho-ROCK signaling and tumor growth and metastasis through PI3K–Akt activation [PMID:27617642]. In neurons, ARHGEF5 binds Drebrin E and facilitates its CDK5-mediated phosphorylation, and ARHGEF5 loss reduces α-tubulin acetylation; an acetylation-mimetic α-tubulin K40Q mutant rescues dendrite and neuronal migration defects, placing ARHGEF5 upstream of microtubule stability [PMID:38932934].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0098772 molecular function regulator activity
- **localization:** GO:0005856 cytoskeleton, GO:0005886 plasma membrane
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-1643685 Disease
- **partners:** SRC, PIK3CA, ODAM, DBN1, CDK5
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2011 | High | ARHGEF5 was identified as a Src SH3 domain-binding protein; Src tyrosine-phosphorylates ARHGEF5, and ARHGEF5 in turn positively regulates Src activity. ARHGEF5 is required for Src-induced podosome formation, acts through activation of RhoA and Cdc42, and forms a ternary complex with Src and PI3K when Src and/or ARHGEF5 are upregulated. The PH domain of ARHGEF5 is required for podosome formation. | PMID:21525037 | Journal of cell science |
| 2009 | High | ARHGEF5 strongly activates RhoA and RhoB, and weakly activates RhoC and RhoG, but not Rac1, RhoQ, RhoD, or RhoV, in transfected HEK293 cells. Gβγ interacts with ARHGEF5 and stimulates ARHGEF5-mediated RhoA activation in an in vitro assay. In vivo, ARHGEF5 deficiency abrogates MIP1α-induced chemotaxis of immature dendritic cells and impairs DC migration from skin to lymph node. | PMID:19713215 | The Journal of biological chemistry |
| 2015 | Medium | ODAM interacts with ARHGEF5 to activate RhoA signaling (inducing ROCK expression and actin filament rearrangement) in the junctional epithelium. Integrin β3 and β6 are upstream of ODAM-ARHGEF5-RhoA, establishing a fibronectin/laminin-integrin-ODAM-ARHGEF5-RhoA signaling axis for junctional epithelium adhesion. | PMID:25911094 | The Journal of biological chemistry |
| 2003 | Low | Expression of recombinant ARHGEF5/TIM protein in COS-7 and NIH-3T3 cells caused loss of actin stress fibers and formation of membrane ruffles and filopodia, a morphological pattern consistent with activation of Rac1, Cdc42, or RhoG rather than RhoA. | PMID:14662653 | Human molecular genetics |
| 2016 | Medium | ARHGEF5 is upregulated during TGF-β-induced EMT in MCF10A cells and promotes cell migration via the Rho-ROCK pathway. In mesenchymal-like colorectal cancer cells, ARHGEF5 activates Akt via PI3K to support tumor growth; this dependence on ARHGEF5 is induced by EMT (TNF-α or Slug expression in HCT116 cells). ARHGEF5 is required for in vivo metastatic activity of HCT116 cells. | PMID:27617642 | Oncogenesis |
| 2015 | Medium | ARHGEF5/TIM contains an auto-inhibitory mechanism: a putative helix N-terminal to the DH domain is stabilized by intramolecular interaction of the C-terminal SH3 domain with a poly-proline sequence between the helix and DH domain. Disrupting the SH3–poly-proline interaction with rationally designed peptide aptamers both binds the SH3 domain and activates TIM-catalyzed RhoA GEF exchange activity, with a positive correlation between peptide affinity and exchange activity. | PMID:25645980 | Biochimie |
| 2019 | Medium | The auto-inhibitory state of ARHGEF5/TIM can be relieved by displacing the intramolecular SH3–poly-proline (SSP) interaction with peptoid ligands targeting the SH3 domain; higher SH3-peptoid affinity correlates exponentially with increased TIM-catalyzed RhoA exchange activity. | PMID:31197859 | Proteins |
| 2024 | Medium | ARHGEF5 binds Drebrin E and facilitates the interaction between Drebrin E and CDK5, which phosphorylates Drebrin E. ARHGEF5 deficiency reduces acetylated α-tubulin levels; expression of an α-tubulin K40Q acetylation-mimetic mutant rescues dendrite development defects and neuronal migration defects, placing ARHGEF5 upstream of microtubule stability. ARHGEF5 also influences Golgi positioning in leading processes of migrating cortical neurons. | PMID:38932934 | Frontiers in molecular neuroscience |

## Citations

- PMID:14662653
- PMID:19713215
- PMID:21525037
- PMID:25645980
- PMID:25911094
- PMID:27617642
- PMID:31197859
- PMID:38932934
