---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ATXN10
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9UBB4
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 6
citation_count: 6
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ATXN10 (human)

## Current model (mechanistic narrative)

ATXN10 encodes a cytoplasmic protein, also detectable around the base of the cilium, that is essential for embryonic cardiac development and adult tissue homeostasis: congenital loss causes embryonic lethality with cardiac trabeculation defects, myocardium-specific deletion produces lethal cardiac malformations, and systemic postnatal deletion drives epithelial-to-mesenchymal transition in kidney and pancreas with acinar-to-ductal metaplasia and glucose homeostasis defects, though its loss does not overtly perturb cilia formation [PMID:34970537]. In neurons, ATXN10 protein expression is required for survival, as its knockdown increases apoptosis in primary cerebellar and cortical cultures [PMID:15895557]. Separately, the gene harbors an intronic (ATTCT)n.(AGAAT)n repeat that, under torsional stress, forms an unpaired DNA structure functioning as an aberrant replication origin [PMID:12589756]; expanded tracts act as length-dependent DNA unwinding elements that elevate origin activity and drive repeat expansion in patient-derived and ectopic-replicator cells [PMID:17846122]. The expanded transcript is the basis of a toxic RNA gain-of-function disease mechanism: the spliced intron-9 RNA bearing the expanded AUUCU repeat aggregates and sequesters hnRNP K, triggering PKCδ translocation to mitochondria, caspase-3 activation, and apoptosis, a pathway recapitulated in transgenic mice expressing (ATTCT)500 that develop neuronal loss, gait abnormalities, and seizure susceptibility [PMID:22065565]. The repeat RNA adopts an A-form hairpin with periodic UCU/UCU internal loops whose loop-closing pairs transiently sample single-stranded conformations, providing a structural basis for protein recruitment such as hnRNP K binding [PMID:26039897].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** *(none)*
- **localization:** GO:0005829 cytosol, GO:0005929 cilium
- **pathway (Reactome):** R-HSA-5357801 Programmed Cell Death, R-HSA-1266738 Developmental Biology
- **partners:** HNRNPK
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2003 | High | The (ATTCT)n.(AGAAT)n repeat in the ATXN10 gene forms an unpaired DNA structure under torsional stress (supercoiling), and this unpaired structure can function as an aberrant replication origin, supporting complete plasmid replication in a HeLa cell extract. | PMID:12589756 | Journal of molecular biology |
| 2007 | High | Expanded (ATTCT)n tracts at the ATX10 locus act as functional DNA unwinding elements (DUEs) and elevate replication origin activity; expanded ATX10 loci in patient-derived cells show increased origin activity compared to the wild-type locus, and ectopic chimeric c-myc replicators containing (ATTCT)27 or (ATTCT)48 (but not shorter tracts) drive length-dependent repeat expansion by ~250 population doublings. | PMID:17846122 | Molecular and cellular biology |
| 2005 | Medium | Reduced expression of ATXN10/E46L in primary cerebellar and cortical neuronal cultures by siRNA causes increased apoptosis, indicating that ATXN10 protein expression is required for neuronal survival. | PMID:15895557 | Cerebellum (London, England) |
| 2011 | High | The spliced intron-9 RNA containing the expanded AUUCU repeat aggregates in SCA10 cells and sequesters hnRNP K; hnRNP K sequestration triggers translocation of protein kinase Cδ (PKCδ) to mitochondria, leading to caspase-3 activation and apoptosis. Expression of (ATTCT)500 in the 3'UTR of a transgene in mice recapitulates this pathway and causes neuronal loss, gait abnormalities, and increased seizure susceptibility. | PMID:22065565 | Journal of neuroscience research |
| 2015 | High | r(AUUCU) repeat RNA from the ATXN10 expanded intron adopts an A-form hairpin structure with 3×3 nucleotide (5')UCU(3')/(3')UCU(5') internal loops closed by AU pairs; molecular dynamics simulations show that loop-closing pairs can transiently form single-stranded conformations, providing structural basis for protein (e.g., hnRNP K) recruitment. | PMID:26039897 | Biochemistry |
| 2021 | High | ATXN10 protein is essential for embryonic development and adult tissue homeostasis: congenital loss causes embryonic lethality (~E10.5) with pericardial effusion and cardiac trabeculation defects; myocardium-specific loss (cTnT-Cre) causes lethal cardiac malformations; systemic postnatal deletion causes rapid epithelial-to-mesenchymal transition (EMT) in kidney and pancreas, pancreatic acinar-to-ductal metaplasia, glucose homeostasis defects, and lethality within weeks. ATXN10 protein localizes around the base of the cilium and in the cytosol, but its loss does not overtly affect cilia formation or morphology. | PMID:34970537 | Frontiers in cell and developmental biology |

## Citations

- PMID:12589756
- PMID:15895557
- PMID:17846122
- PMID:22065565
- PMID:26039897
- PMID:34970537
