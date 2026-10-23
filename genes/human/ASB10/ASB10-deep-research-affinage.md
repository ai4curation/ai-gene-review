---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ASB10
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q8WXI3
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 11
citation_count: 4
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ASB10 (human)

## Current model (mechanistic narrative)

ASB10 is a substrate-recognition E3 ubiquitin ligase that controls the abundance of specific client proteins and thereby regulates tissue homeostasis in the eye, vasculature, and heart [PMID:34285210, PMID:40399264]. As an E3 ligase it ubiquitylates the tumor endothelial marker TEM8, targeting it for proteasomal degradation so that loss of ASB10 elevates homeostatic TEM8 levels [PMID:34285210]. In the heart, ASB10 acts in the opposite direction on a different client: it binds HSP70 and competitively blocks STUB1-mediated ubiquitination of HSP70, stabilizing HSP70 and driving inflammation and accumulation of Ser394-phosphorylated HDAC2, which together exacerbate pressure-overload cardiac hypertrophy and fibrosis [PMID:40399264]. In trabecular meshwork cells ASB10 localizes to intracellular vesicles where it physically associates with HSP70 and with proteasomal (20S α4 subunit) and autophagic-lysosomal machinery, and its vesicle dynamics track autophagic flux, while ASB10 itself is not ubiquitinated [PMID:23901248]; silencing ASB10 reduces aqueous humor outflow facility, and a splice-altering coding variant links ASB10 to primary open-angle glaucoma [PMID:22156576]. A unified enzymatic mechanism connecting substrate selection across these tissues to a single biochemical activity has not been fully resolved in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0016740 transferase activity, GO:0140096 catalytic activity, acting on a protein, GO:0098772 molecular function regulator activity
- **localization:** GO:0031410 cytoplasmic vesicle, GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-392499 Metabolism of proteins, R-HSA-9612973 Autophagy
- **partners:** HSP70, STUB1, TEM8, PSMA7
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2011 | Medium | ASB10 silencing in perfused anterior segment organ culture reduced aqueous humor outflow facility by ~50% compared with control-infected anterior segments, demonstrating a functional role for ASB10 in trabecular meshwork outflow regulation. | PMID:22156576 | Human molecular genetics |
| 2011 | Medium | ASB10 mRNA and protein are strongly expressed in trabecular meshwork, retinal ganglion cells, and ciliary body, as established by expression analysis in human ocular tissues. | PMID:22156576 | Human molecular genetics |
| 2011 | Medium | A synonymous variant c.765C>T (Thr255Thr) in ASB10 affects an exon splice enhancer site and alters mRNA splicing in lymphoblasts of affected family members with POAG. | PMID:22156576 | Human molecular genetics |
| 2013 | Medium | ASB10 localizes to intracellular vesicular structures in human trabecular meshwork (HTM) cells and co-localizes with markers of the ubiquitin-proteasomal pathway (ubiquitin, α4 subunit of 20S proteasome) and autophagic structures (LC3, p62, HDAC6, HSP70, Rab7, LAMP1), as shown by confocal and super-resolution structured illumination microscopy. | PMID:23901248 | Molecular vision |
| 2013 | Medium | ASB10 physically interacts with HSP70 and with the α4 subunit of the 20S proteasome in HTM cells, as demonstrated by co-immunoprecipitation. | PMID:23901248 | Molecular vision |
| 2013 | Medium | ASB10 itself is not ubiquitinated, despite its association with ubiquitin-mediated degradation pathway components in HTM cells. | PMID:23901248 | Molecular vision |
| 2013 | Medium | Treatment of HTM cells with the autophagy/proteasome inhibitor MG132 significantly increased the number of small ASB10-stained vesicles, while autophagy inhibitors (wortmannin, bafilomycin A1) decreased them, indicating ASB10 vesicle dynamics are coupled to autophagic flux. | PMID:23901248 | Molecular vision |
| 2021 | Medium | ASB10 functions as an E3 ubiquitin ligase that ubiquitylates TEM8 (tumor endothelial marker 8) for proteasomal degradation; ASB10 deficiency in triple-negative breast cancer results in elevated homeostatic TEM8 levels. | PMID:34285210 | Nature communications |
| 2025 | High | Asb10 binds HSP70 and competitively blocks STUB1-mediated ubiquitination and proteasomal degradation of HSP70, thereby stabilizing HSP70 protein levels and exacerbating cardiac hypertrophic growth. | PMID:40399264 | Cell death & disease |
| 2025 | High | Asb10 overexpression in vivo (AAV9-Asb10) worsens cardiac function and increases interstitial fibrosis after transverse aortic constriction (TAC), while Asb10 knockdown (AAV9-shAsb10) improves outcomes, establishing Asb10 as a pro-hypertrophic factor in pressure-overload heart failure. | PMID:40399264 | Cell death & disease |
| 2025 | Medium | The pro-hypertrophic effects of Asb10 are mediated through HSP70 stabilization leading to cardiac inflammation and activation of phospho-HDAC2 at Ser394 (pHDAC2S394). | PMID:40399264 | Cell death & disease |

## Citations

- PMID:22156576
- PMID:23901248
- PMID:34285210
- PMID:40399264
