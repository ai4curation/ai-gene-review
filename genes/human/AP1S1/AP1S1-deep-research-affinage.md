---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AP1S1
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: P61966
self_evaluation_pairwise: tie
faith_pct: 83.33333333333333
n_discoveries: 9
citation_count: 9
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AP1S1 (human)

## Current model (mechanistic narrative)

AP1S1 encodes sigma1A, the smallest polypeptide subunit of the Golgi-localized AP-1 clathrin-associated adaptor complex that drives clathrin-coated vesicle assembly and cargo sorting [PMID:2040623]. Sigma1A recognizes [DE]XXXL[LI] dileucine sorting motifs and must assemble into the AP-1 complex to do so; the disease-associated L90P variant fails both to incorporate into AP-1 and to bind these motifs, defining the molecular basis of AP-1 loss of function [PMID:39269494]. Through this sorting activity AP1S1 governs trafficking of multiple cargoes: it directs the copper-transporting ATPases ATP7A and ATP7B to maintain copper homeostasis [PMID:24754424], maintains tight-junction protein (ZO-1, claudin-3) localization and intestinal epithelial barrier integrity [PMID:32306098], and controls the balance between EGFR recycling and lysosomal degradation [PMID:37659097]. In neurons, sigma1A nucleates an AP-1/sigma1A–ArfGAP1–Rabex-5 complex that raises endosomal Rabex-5 and enhances Rab5(GTP)-stimulated Vps34 PI3-kinase activity, promoting early-to-late endosome maturation and synaptic vesicle protein degradation [PMID:27411398]. Loss-of-function mutations in AP1S1 cause the multisystem MEDNIK/IDEDNIK syndrome, with defects in skin, pigmentation, and neural development [PMID:19057675, PMID:39269494]. AP1S1 depletion also induces cellular senescence and Golgi dispersal and sensitizes neuronal cells to oxidative and amyloid-beta stress [PMID:40954504].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0038024 cargo receptor activity
- **localization:** GO:0005794 Golgi apparatus, GO:0031410 cytoplasmic vesicle, GO:0005768 endosome
- **pathway (Reactome):** R-HSA-5653656 Vesicle-mediated transport, R-HSA-9609507 Protein localization, R-HSA-1643685 Disease
- **partners:** ARFGAP1, RABEX-5, ATP7A, ATP7B
- **complexes:** AP-1 adaptor complex, AP-1/sigma1A–ArfGAP1–Rabex-5 complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2008 | High | AP1S1 encodes the sigma1A small subunit of the AP-1 adaptor protein complex; loss-of-function (splice mutation causing premature stop codon) disrupts skin formation, pigmentation, and spinal cord neural network development in zebrafish, and wild-type but not truncated AP1S1 mRNA rescues these defects, demonstrating AP1S1 is required for AP-1-dependent vesicular trafficking in skin and neural tissue. | PMID:19057675 | PLoS genetics |
| 2014 | Medium | AP1S1 (sigma1A subunit of AP-1) directs intracellular trafficking of the copper-transporting ATPases ATP7A and ATP7B; loss of AP1S1 function disrupts copper homeostasis, producing combined features of Menkes and Wilson's diseases (copper deficiency in serum alongside liver copper overload). | PMID:24754424 | Annals of the New York Academy of Sciences |
| 1991 | Medium | AP19 (AP1S1) is the smallest polypeptide chain of the AP-1 clathrin-associated protein complex localized to the Golgi apparatus; its cDNA predicts a 158-amino-acid protein (Mr 18,733) that is homologous to AP17 (AP-2 small chain) and to a yeast homolog (Yap17p), establishing it as a conserved component of clathrin-coated vesicle assembly machinery. | PMID:2040623 | The Journal of biological chemistry |
| 2016 | High | AP-1/sigma1A (AP1S1-containing complex) binds ArfGAP1 (and with higher affinity brain-specific ArfGAP1), which in turn binds Rabex-5; formation of the AP-1/sigma1A–ArfGAP1–Rabex-5 complex increases endosomal Rabex-5 levels and enhances Rab5(GTP)-stimulated Vps34 PI3-kinase activity, thereby promoting early endosome maturation into multivesicular body late endosomes and controlling synaptic vesicle protein degradation. | PMID:27411398 | Scientific reports |
| 2020 | High | Loss of AP1S1 function in intestinal epithelial cells (CaCo2 knockout) causes mislocalization of tight-junction proteins ZO-1 and claudin-3, decreased transepithelial electrical resistance, increased dextran permeability, and abnormal lumen formation in 3D culture; re-expression of wild-type AP1S1 reverses these defects whereas missense variants (L90P, E116K) do not, indicating AP1S1 maintains intestinal epithelial barrier integrity via tight-junction regulation. | PMID:32306098 | Human genetics |
| 2023 | Medium | AP1S1 regulates EGFR intracellular trafficking; knockout of AP1S1 in non-small cell lung cancer cells causes lysosomal degradation of EGFR rather than recycling, leading to suppressed EGF-induced ALK phosphorylation and increased erlotinib sensitivity in otherwise TKI-resistant H1975 cells. | PMID:37659097 | Journal of cellular physiology |
| 2024 | High | The AP1S1 missense variant sigma1A L90P is largely unable to assemble into the AP-1 complex and fails to bind [DE]XXXL[LI] dileucine sorting motifs, resulting in AP-1 loss-of-function and full MEDNIK syndrome. | PMID:39269494 | Journal of molecular medicine (Berlin, Germany) |
| 2025 | Medium | AP1S1 knockdown in neuronal cells (N2a) induces cellular senescence and Golgi dispersal without directly impairing viability, but exacerbates neuronal vulnerability to oxidative stress (H2O2) and amyloid-beta toxicity; proteomic profiling after AP1S1 depletion implicates dysregulation of rRNA modifications and Golgi-associated vesicle biogenesis. | PMID:40954504 | Alzheimer's research & therapy |
| 2025 | Medium | A splicing mutation in AP1S1 (c.430-1G>A) causes a single-base deletion in exon 5 mRNA, producing a frameshift (p.Glu144ArgfsTer83), as confirmed by in vitro mRNA splicing assay, altering protein structure and function. | PMID:40901618 | International journal of genomics |

## Citations

- PMID:19057675
- PMID:2040623
- PMID:24754424
- PMID:27411398
- PMID:32306098
- PMID:37659097
- PMID:39269494
- PMID:40901618
- PMID:40954504
