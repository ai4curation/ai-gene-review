---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ABRA
affinage_run_date: 2026-06-09T22:02:37
uniprot_accession: Q8N0Z2
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

# Affinage mechanistic annotation for ABRA (human)

## Current model (mechanistic narrative)

ABRA (STARS) is a striated-muscle-enriched actin-binding protein that couples sarcomeric actin dynamics to the transcriptional program governing muscle growth and adaptation [PMID:11983702]. It localizes to the sarcomeric Z disc/I-band, binds actin filaments, and activates Rho-GTPase signaling, which in turn drives nuclear translocation of the MRTF-A/MRTF-B co-activators to stimulate SRF-dependent transcription of muscle structural and growth genes [PMID:11983702, PMID:17415416]. Its actin-cytoskeleton-regulating activity is conserved through the C-terminal Costars domain, whose function in actin organization and motility is preserved across species [PMID:20940261]. The STARS→RhoA→MRTF→SRF axis operates as a feed-forward autoregulatory loop, since SRF binds the STARS proximal promoter and ABRA is itself required for cardiac development, with loss of zebrafish STARS causing severe cardiac dysfunction rescuable by SRF [PMID:22815879]. Beyond the heart, ABRA mediates fluid-shear-stress-induced arteriogenesis through NO-dependent Rho signaling in vascular smooth muscle [PMID:19778941] and tracks coordinately with skeletal muscle hypertrophy and atrophy [PMID:19255118]. ABRA transcription is induced by MEF2 and by PGC-1α/ERRα, repressed by GATA4, and its protein is suppressed post-transcriptionally by miR-628-5p with aging [PMID:17415416, PMID:21486805, PMID:22431517, PMID:27739650]. Its physical partners include the actin-binding ABLIM-2 and ABLIM-3 proteins, which synergistically enhance STARS-dependent SRF activation [PMID:17194709].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0008092 cytoskeletal protein binding, GO:0098772 molecular function regulator activity, GO:0140110 transcription regulator activity
- **localization:** GO:0005856 cytoskeleton, GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-74160 Gene expression (Transcription), R-HSA-1266738 Developmental Biology, R-HSA-397014 Muscle contraction
- **partners:** ABLIM2, ABLIM3, ACTIN, MRTFA, MRTFB, SRF
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2002 | High | STARS (ABRA) is a novel actin-binding protein specifically expressed in cardiac and skeletal muscle that binds to the I-band of the sarcomere and to actin filaments in transfected cells, activates Rho-signaling events, and stimulates SRF transcriptional activity through a mechanism requiring actin binding and Rho GTPase activation. | PMID:11983702 | The Journal of biological chemistry |
| 2007 | High | STARS is localized to the Z disc of the sarcomere and activates SRF-dependent transcription by inducing nuclear translocation of MRTF-A and MRTF-B. STARS expression is upregulated by MEF2 (via a conserved MEF2 binding site in the STARS promoter) in cardiac hypertrophy, and forced cardiac overexpression of STARS exaggerates pressure overload- and calcineurin-induced deterioration in cardiac function. | PMID:17415416 | The Journal of clinical investigation |
| 2006 | High | STARS interacts with two novel members of the ABLIM protein family, ABLIM-2 and ABLIM-3, identified by yeast two-hybrid screening of a skeletal muscle cDNA library. ABLIM-2 and -3 directly bind F-actin, localize to actin stress fibers, and synergistically enhance STARS-dependent SRF activation. siRNA knockdown of endogenous ABLIM significantly blunts SRF-dependent transcription in C2C12 cells. | PMID:17194709 | The Journal of biological chemistry |
| 2009 | High | ABRA (STARS) expression is highly upregulated in growing collateral vessels in response to fluid shear stress (FSS); this upregulation is NO-dependent (blocked by L-NAME). Adenoviral overexpression of Abra in collateral vessels improved collateral conductance by 60%, while targeted deletion of Abra in mice impaired arteriogenesis. Cell culture studies showed Abra-triggered smooth muscle cell proliferation requires Rho signaling. | PMID:19778941 | Arteriosclerosis, thrombosis, and vascular biology |
| 2009 | Medium | The STARS signaling pathway (STARS → RhoA → MRTF-A/B → SRF) is upregulated at the mRNA and protein level in human quadriceps muscle after resistance training (hypertrophy) and downregulated after de-training (atrophy), with nuclear SRF protein and SRF target genes (alpha-actin, MHCIIa, IGF-1) showing coordinated changes. | PMID:19255118 | The Journal of physiology |
| 2011 | High | STARS is a transcriptional target of PGC-1α/ERRα in skeletal muscle: adenoviral overexpression of PGC-1α in C2C12 myotubes induced a 3-fold increase in Stars mRNA, abolished by ERRα suppression. STARS is also upregulated in human skeletal muscle after endurance cycling exercise, accompanied by increased MRTF-A and nuclear SRF protein. Suppression of endogenous STARS reduced CPT-1β levels and inhibited PGC-1α-induced CPT-1β upregulation, suggesting STARS mediates PGC-1α-driven fat oxidative gene expression. | PMID:21486805 | The Journal of physiology |
| 2012 | High | STARS is essential for cardiac development and function in zebrafish: morpholino-induced knockdown of zSTARS causes altered atrial/ventricular dimensions, decreased ventricular fractional shortening, pericardial edema, and absent circulation in 77% of injected embryos. Co-injection of SRF mRNA rescues the cardiac phenotype, establishing a STARS-SRF pathway in vivo. SRF binds the STARS proximal promoter (demonstrated by ChIP), and STARS overexpression in vitro activates this promoter, revealing a feed-forward autoregulatory loop. | PMID:22815879 | PloS one |
| 2012 | High | GATA4 represses ms1/STARS expression in embryonic, neonatal, and adult hearts via two evolutionarily conserved cis-regulatory modules (ECRs α and DINA) in the STARS promoter. Loss of GATA4 (as in type 1/type 2 diabetic models) results in upregulation of ms1/STARS and thereby alters MRTF-SRF signaling in cardiac disease. | PMID:22431517 | Molecular and cellular biology |
| 2013 | Medium | Resistance exercise acutely stimulates the STARS signaling pathway in a contraction-mode dependent manner: a single bout of eccentric (ECC) exercise produces enhanced STARS and SRF mRNA responses compared to concentric (CONC) exercise, while STARS protein increase is specific to CONC exercise. Whey protein supplementation has no effect on STARS pathway regulation. | PMID:23753523 | The Journal of physiology |
| 2016 | Medium | STARS overexpression in C2C12 skeletal muscle cells enhances differentiation but not proliferation, associated with increased mRNA of myogenic markers (Ckm, Ckmt2, Myh4), the differentiation factor Igf2, and myogenic regulatory factors Myf5 and Myf6. The MRTF-A/SRF inhibitor CCG-1423 did not affect differentiation rate, indicating STARS promotes differentiation via an MRTF-A-independent mechanism. | PMID:26903873 | Frontiers in physiology |
| 2016 | Medium | STARS protein is significantly downregulated in skeletal muscle of older (60–75 years) compared to young (18–30 years) humans. miR-628-5p, a miRNA regulated by age and exercise, directly binds the STARS 3'UTR to downregulate STARS transcription. | PMID:27739650 | Acta physiologica (Oxford, England) |
| 2010 | Medium | Costars, a Dictyostelium protein homologous to the C-terminal domain of STARS (ABRA), regulates the actin cytoskeleton and cell motility. cosA-null cells show reduced chemotactic migration speed, aberrant F-actin distribution, increased cytoskeleton-associated actin, and excessive pseudopod formation. Expression of human mCostars rescues these phenotypes, demonstrating functional conservation of this domain. | PMID:20940261 | Journal of cell science |

## Citations

- PMID:11983702
- PMID:17194709
- PMID:17415416
- PMID:19255118
- PMID:19778941
- PMID:20940261
- PMID:21486805
- PMID:22431517
- PMID:22815879
- PMID:23753523
- PMID:26903873
- PMID:27739650
