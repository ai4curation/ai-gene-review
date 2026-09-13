---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AP1S2
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: P56377
self_evaluation_pairwise: tie
faith_pct: 100.0
n_discoveries: 10
citation_count: 10
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AP1S2 (human)

## Current model (mechanistic narrative)

AP1S2 encodes the σ1B subunit of the AP-1 clathrin adaptor complex and functions in endosomal protein sorting, with its most penetrant biology in the nervous system [PMID:20203623, PMID:17186471]. In hippocampal neurons the AP-1/σ1B complex mediates reformation of synaptic vesicles from early endosomes: σ1B loss reduces synaptic vesicle reformation upon stimulation and causes accumulation of large endosomal intermediates [PMID:20203623], with elevated early-endosome PI-3-P, misrouting of synaptic vesicle proteins, and accumulation of AP-2-coated vesicles, linking σ1B-mediated SV reformation to AP-2-dependent endocytosis [PMID:25128028]. Mechanistically, σ1B binds Rabex-5 directly to prevent assembly of the AP-1/σ1A–ArfGAP1–Rabex-5 complex, thereby lowering endosomal Rabex-5 and opposing Rab5/Vps34-driven multivesicular-body maturation, balancing recycling against degradation [PMID:27411398]. In adipocytes the same complex sorts sortilin to lysosomes via a DxxD-x12-DSxxxL motif; σ1B loss causes sortilin overaccumulation that stabilizes the adipogenesis inhibitor DLK1, producing lipodystrophy [PMID:24928897]. AP1S2 also acts in intestinal macrophages downstream of an MCPIP1-restrained ATF3–AP1S2 axis, where elevated AP1S2 arrests monocyte-to-macrophage maturation and promotes proinflammatory polarization [PMID:37015751]. Loss-of-function mutations in AP1S2 cause X-linked intellectual disability, including the syndromic forms historically named Fried and Pettigrew syndromes with basal ganglia calcification/iron deposition and hydrocephalus or Dandy-Walker malformation [PMID:17186471, PMID:17617514, PMID:23756445].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0008289 lipid binding
- **localization:** GO:0005768 endosome, GO:0005794 Golgi apparatus, GO:0031410 cytoplasmic vesicle
- **pathway (Reactome):** R-HSA-5653656 Vesicle-mediated transport, R-HSA-9609507 Protein localization, R-HSA-112316 Neuronal System, R-HSA-168256 Immune System
- **partners:** RABEX-5, SORT1, DLK1, ATF3
- **complexes:** AP-1 adaptor complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2010 | High | The AP-1/σ1B (AP1S2-containing) complex is required for synaptic vesicle recycling via an endosomal pathway in hippocampal neurons. σ1B-deficient mice show reduced synaptic vesicle reformation upon stimulation and accumulation of large endosomal intermediates, demonstrating that the AP-1/σ1B complex mediates protein sorting from endosomes back to synaptic vesicles. | PMID:20203623 | The EMBO journal |
| 2006 | Medium | Loss-of-function mutations (nonsense and splice-site) in AP1S2 cause X-linked mental retardation. AP1S2 encodes the sigma2 subunit of the AP-1 adaptor protein complex at the cytoplasmic face of Golgi-associated coated vesicles, where it mediates clathrin recruitment and endocytic vesicle assembly. | PMID:17186471 | American journal of human genetics |
| 2007 | Medium | AP1S2 mutations (including a splice-site mutation causing skipping of exon 3 and predicting a protein with three novel amino acids terminating at codon 64, and a nonsense mutation p.Gln66X) cause Fried syndrome (X-linked mental retardation with basal ganglia calcifications and hydrocephalus), establishing AP1S2 loss-of-function as causative for this syndromic XLMR. | PMID:17617514 | Journal of medical genetics |
| 2008 | Medium | AP1S2 (sigma1B) mutations cause loss of the sigma subunit function within the AP-1 complex. Using AP-2 (single sigma gene) as a model system, sigma subunits were shown to be essential for the stability of human AP complexes. In patient fibroblasts carrying AP1S2 mutations, no major alteration of AP-1 complex stability, subcellular localization, or function was detected, suggesting functional redundancy with sigma1A and sigma1C in peripheral tissues; the brain-specific phenotype likely reflects a subtle brain-specific defect in AP-1-dependent intracellular protein traffic. | PMID:18428203 | Human mutation |
| 2013 | Medium | AP1S2 mutations (including c.426+1 G>T causing loss of 46 amino acids in the clathrin adaptor complex small chain domain) cause Pettigrew syndrome (MRXS5), an X-linked intellectual disability syndrome with Dandy-Walker malformation, basal ganglia iron deposition, facial dysmorphism, and choreoathetosis. This establishes that all previously described syndromic XLMR phenotypes linked to Xp22 (MIM 300629, 300630, 304340) are the same AP1S2-deficiency syndrome. | PMID:23756445 | European journal of human genetics : EJHG |
| 2014 | High | The σ1B (AP1S2)-containing AP-1 complex specifically mediates sorting of sortilin in adipocytes. σ1B binds sortilin via a DxxD-x12-DSxxxL motif on sortilin. In σ1B-deficient adipocytes, sortilin is overexpressed and fails to reach lysosomes efficiently; overexpressed sortilin binds and stabilizes DLK1 (an inhibitor of adipogenesis), preventing DLK1 downregulation and thereby inhibiting adipogenesis. This σ1B-sortilin-DLK1 axis explains lipodystrophy in σ1B-deficient mice. | PMID:24928897 | Journal of cell science |
| 2016 | High | AP-1/σ1B (AP1S2) and AP-1/σ1A differentially regulate neuronal early endosome maturation into multivesicular body late endosomes via distinct mechanisms: σ1A binds ArfGAP1 (with higher affinity for brain-specific ArfGAP1), forming an AP-1/σ1A-ArfGAP1-Rabex-5 complex that increases endosomal Rabex-5 and enhances Rab5(GTP)-stimulated Vps34 PI3-kinase activity essential for MVB formation. By contrast, σ1B binds Rabex-5 directly, preventing AP-1/σ1A-ArfGAP1-Rabex-5 complex formation and reducing endosomal Rabex-5 levels, thereby opposing MVB endosome formation and coordinating SV protein recycling versus degradation. | PMID:27411398 | Scientific reports |
| 2014 | High | AP-1/σ1B (AP1S2) regulates synaptic vesicle protein recycling through early endosomes. σ1B-deficient early endosomes have increased phosphatidylinositol 3-phosphate (PI-3-P). σ1B deficiency leads to altered endosomal proteome with increased SV protein storage, misrouting of certain SV proteins (tetraspanins enriched in synaptosomes but not endosomes), altered CaMKII and CKII association with the endosome/SV pool, and accumulation of AP-2-coated vesicles with altered coat composition, indicating that AP-1/σ1B-mediated SV reformation from endosomes is coupled to AP-2-mediated endocytosis. | PMID:25128028 | Molecular neurobiology |
| 2022 | High | AP1S2 functions downstream of an ATF3-AP1S2 axis regulated by MCPIP1 in intestinal monocyte-to-macrophage maturation. In macrophage-specific Mcpip1-deficient mice, elevated Atf3 drives increased Ap1s2 expression, which arrests monocyte-to-macrophage maturation and promotes M1-like polarization with enhanced migration and proinflammatory cytokine production. In vivo blockage of Ap1s2 ameliorated DSS-induced colitis and restored macrophage maturation. | PMID:37015751 | Gut |
| 1999 | Low | The MRX59 locus (later identified as AP1S2) was mapped by linkage analysis to Xp21.2-p22.2 in a four-generation family with nonspecific X-linked mental retardation, establishing the chromosomal location of this XLMR gene. | PMID:10398241 | American journal of medical genetics |

## Citations

- PMID:10398241
- PMID:17186471
- PMID:17617514
- PMID:18428203
- PMID:20203623
- PMID:23756445
- PMID:24928897
- PMID:25128028
- PMID:27411398
- PMID:37015751
