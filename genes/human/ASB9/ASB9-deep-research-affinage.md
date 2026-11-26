---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ASB9
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q96DX5
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 15
citation_count: 14
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ASB9 (human)

## Current model (mechanistic narrative)

ASB9 is the substrate-recognition subunit of an ECS-type Cullin 5 RING E3 ubiquitin ligase that selects diverse substrates through its ankyrin repeat domain and recruits the catalytic core via its SOCS box, thereby controlling the proteasomal turnover of metabolic, transcriptional, and chromatin-associated targets [PMID:17148442, PMID:23837592]. The ankyrin repeats engage substrates such as cytosolic creatine kinase B (CKB) and ubiquitous mitochondrial creatine kinase (uMtCK) in a SOCS box-independent manner, while the SOCS box drives substrate degradation; full-length ASB9 ubiquitylates uMtCK, disrupts mitochondrial structure, lowers membrane potential, and reduces creatine kinase activity [PMID:17148442, PMID:20302626]. ASB9 is unstable alone but forms a stable ternary complex with Elongin B/C that binds selectively to the Cullin 5 N-terminal domain, assembling the ASB9–EloBC–CUL5–RBX2 ligase [PMID:23837592]. Structural and HDX-MS studies show that ASB9 binds creatine kinase with very high affinity and that ASB9 and CUL5 behave as rigid rods joined by an EloB/C hinge, transmitting long-range allosteric signals from the bound substrate to the RBX2 E2-recruiting region to enable dynamic ubiquitin transfer across the complex [PMID:25654263, PMID:32513959]. The ligase polyubiquitylates free histones H3 and H4 — but not H2A/H2B, nucleosomal histones, or Asf1-bound histones — generating K48 and K63 chains, and does so without requiring an ARIH2 RBR helper ligase, distinguishing it from other CUL5 complexes [PMID:41260500]. Physiologically, ASB9 suppresses ovarian granulosa cell proliferation and apoptosis through MAPK signaling and is itself transcriptionally induced by CLOCK [PMID:34476862, PMID:37280645], restrains spermatogonial stem cell proliferation by degrading HIF1AN [PMID:36683111], and assembles a testis-specific TNP2-targeting CRL whose loss causes TNP2 retention, failed histone-to-protamine transition, and male infertility in mice and humans [PMID:41915740].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0016874 ligase activity, GO:0140096 catalytic activity, acting on a protein, GO:0060089 molecular transducer activity, GO:0042393 histone binding, GO:0098772 molecular function regulator activity
- **localization:** GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-392499 Metabolism of proteins, R-HSA-1474165 Reproduction
- **partners:** CKB, CKMT2, ELOB, ELOC, CUL5, HIF1AN, TNP2
- **complexes:** ASB9–ElonginB/C–CUL5–RBX2 CRL, TNP2–ASB9–ElonginB/C–CUL5–RBX1 testis CRL

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2006 | High | ASB9 ankyrin repeat domain binds creatine kinase B (CKB) in a SOCS box-independent manner; the interaction promotes polyubiquitylation of CKB and decreases total CKB protein levels, with CKB degradation being primarily SOCS box-dependent, establishing ASB9 as a substrate receptor of an E3 ubiquitin ligase targeting CKB for proteasomal degradation. | PMID:17148442 | The Journal of biological chemistry |
| 2010 | High | ASB9 interacts with ubiquitous mitochondrial creatine kinase (uMtCK) via its ankyrin repeat domain in a SOCS box-independent manner and co-localizes with uMtCK in mitochondria. Full-length ASB9 (but not the naturally occurring SOCS box-deleted variant ASB9ΔSOCS) induces ubiquitination of uMtCK, causes abnormal mitochondrial structure, decreases mitochondrial membrane potential, reduces creatine kinase activity, and reduces cell growth. | PMID:20302626 | BMC biology |
| 2012 | High | Crystal structure of the ASB9-2 isoform (containing one ankyrin repeat domain) at 2.2-Å resolution revealed an arch shape with L-shaped cross-section. Mutagenesis (His103, Phe107) and truncation analysis showed that the first six ankyrin repeats plus the N-terminal region are essential for CKB binding. | PMID:22418839 | The protein journal |
| 2013 | High | ASB9 is unstable alone but forms a stable ternary complex with Elongin B and Elongin C (EloBC), which then binds with high affinity to the Cullin 5 N-terminal domain (Cul5NTD) but not to Cul2NTD, establishing selective Cullin 5 recruitment for the ECS-type CRL complex. | PMID:23837592 | Biochemistry |
| 2015 | High | One ASB9 molecule binds to a CK dimer with extremely tight affinity; the N-terminal disordered region and first ankyrin repeat of ASB9 are protected upon binding. ASB9 protects CK residues 182–203 (one side of the active site), and ASB9 N-terminal residues may occupy one CK active site, partially inhibiting CK enzymatic activity. | PMID:25654263 | Biochemistry |
| 2016 | Medium | Integrative structural modeling combined with small-angle X-ray scattering (SAXS) defined the ASB9–CK interface and constructed an atomic model of the full CK-targeting CRL. Dominant modes of motion in the correctly docked complex permit close approach of ubiquitin to the CK substrate, suggesting a dynamic mechanism for ubiquitin transfer over ~60 Å. | PMID:27396830 | Structure |
| 2019 | Medium | Yeast two-hybrid screening of ovarian granulosa cell cDNA library identified PAR1, TAOK1, and TNFAIP6/TSG6 as ASB9 binding partners in granulosa cells. Notably, no interaction was found between ASB9 and CKB in these granulosa cells, in contrast to other cell types. | PMID:30811458 | PloS one |
| 2019 | Medium | CRISPR/Cas9-mediated inhibition of ASB9 in ovarian granulosa cells led to increased granulosa cell proliferation and modulated expression of target genes (PAR1, TAOK1, TNFAIP6), establishing a functional role for ASB9 in suppressing GC proliferation. | PMID:30811458 | PloS one |
| 2020 | High | Cryo-EM structures of the substrate CKB bound to ASB9-ELOB/C and of full-length CUL5 bound to RBX2 revealed that ASB9 and CUL5 behave as rigid rods connected through an ELOB/C hinge. HDX-MS mapped onto the full structural model showed long-range allosteric communication from the substrate through CUL5 to the RBX2 flexible linker, proposing a revised allosteric mechanism for CUL-E3 ligase function. | PMID:32513959 | Nature communications |
| 2021 | Medium | CRISPR/Cas9-mediated inhibition of ASB9 in ovarian granulosa cells increased GC number, decreased caspase-3/7 activity, CASP3 expression, and BAX/BCL2 ratio (reduced apoptosis), and increased pMAPK3/1 phosphorylation; conversely, ASB9 induction post-hCG was concomitant with decreased pMAPK3/1 levels, placing ASB9 upstream as a negative regulator of MAPK signaling in GCs. | PMID:34476862 | Molecular reproduction and development |
| 2023 | Medium | ASB9 interacts with hypoxia-inducible factor 1-alpha inhibitor (HIF1AN) in human spermatogonial stem cells (SSC line), as confirmed by protein immunoprecipitation. ASB9 overexpression inhibited SSC proliferation and increased apoptosis; re-expression of HIF1AN reversed these effects, establishing HIF1AN as the functional target of ASB9 in SSCs. CKB was tested but did not show direct interaction with ASB9 in this cell type. | PMID:36683111 | Biological research |
| 2023 | Medium | CLOCK transcription factor binds to the E-box element in the ASB9 promoter and increases ASB9 expression, which in turn inhibits porcine granulosa cell proliferation, placing CLOCK upstream of ASB9 in a transcriptional regulatory pathway. | PMID:37280645 | Journal of animal science and biotechnology |
| 2025 | High | The ASB9-CUL5 E3 ligase polyubiquitylates free histones H3 and H4 (but not H2A/H2B, or histones in nucleosomes or complexed with chaperone Asf1), generating K48 and K63 polyubiquitin chains. The ligase-histone interaction is highly electrostatic; neddylated ASB9-CRL5 binds with highest affinity. Crucially, this ubiquitylation does not require the ring-between-ring ligase ARIH2, representing the first example of CUL5-mediated ubiquitylation without a RBR helper ligase. | PMID:41260500 | Molecular & cellular proteomics |
| 2025 | Medium | ASB9-CUL5 E3 ligase polyubiquitylates free histones H3 and H4 with substrate specificity (H2A and H2B are not polyubiquitylated); histones in nucleosomes or bound by chaperone Asf1 are not ubiquitylated. This represents the first CUL5-mediated ubiquitylation not requiring an ARIH2 RBR helper ligase. (Preprint version of the same study as PMID:41260500.) | PMID:40501794 | bioRxiv |
| 2026 | High | ASB9 assembles a testis-specific CRL complex (TNP2-ASB9-ELOB/C-CUL5-RBX1) that mediates ubiquitin-dependent degradation of transition protein TNP2 during spermiogenesis. ASB9 deficiency in humans and mice causes TNP2 retention, failure of the histone-to-protamine transition, sperm head malformation, and male infertility. | PMID:41915740 | Proceedings of the National Academy of Sciences of the United States of America |

## Citations

- PMID:17148442
- PMID:20302626
- PMID:22418839
- PMID:23837592
- PMID:25654263
- PMID:27396830
- PMID:30811458
- PMID:32513959
- PMID:34476862
- PMID:36683111
- PMID:37280645
- PMID:40501794
- PMID:41260500
- PMID:41915740
