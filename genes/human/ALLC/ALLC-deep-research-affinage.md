---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ALLC
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q8N6M5
self_evaluation_pairwise: win
faith_pct: 66.66666666666667
n_discoveries: 3
citation_count: 3
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ALLC (human)

## Current model (mechanistic narrative)

ALLC encodes allantoicase, an enzyme of the purine catabolic pathway, characterized primarily through its fungal ortholog [PMID:2148685]. In Neurospora crassa the allantoicase gene is transcribed as a single ~1.2 kb mRNA whose expression is induced by uric acid and governed by the nitrogen regulatory circuit: the NIT2 zinc-finger protein acts as the direct transcriptional activator, binding a single defined site in the allantoicase promoter that contains a symmetrical 10 bp sequence flanked by TATCT/TATCG core motifs, while the nmr gene negatively regulates expression under nitrogen-replete conditions [PMID:2148685, PMID:1978237]. Amino acid substitutions in the NIT2 zinc-finger motif abolish promoter binding, establishing NIT2 as the direct regulator of allantoicase induction under nitrogen limitation [PMID:2148685]. No direct biochemical mechanism for the human ALLC protein has been characterized in the available corpus; beyond the fungal regulatory and enzymatic context, the catalytic and cellular roles of the human enzyme remain undescribed here.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0016787 hydrolase activity
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-1430728 Metabolism
- **partners:** *(none)*
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1990 | High | The Neurospora crassa alc gene (ortholog of human ALLC) encodes allantoicase, a purine catabolic enzyme of 354 amino acids with a single intron, transcribed from two initiation sites ~50 bp upstream of the translation start site. Mobility shift and DNA footprint experiments identified a single binding site for the NIT2 regulatory protein in the alc promoter, containing a 10 bp symmetrical sequence flanked by two TATCT/TATCG core binding sequences. Mutant NIT2/beta-gal fusion proteins with amino acid substitutions in a putative zinc-finger motif were completely deficient in binding to the alc promoter DNA fragment, establishing NIT2 as the direct transcriptional activator of allantoicase expression under nitrogen limitation. | PMID:2148685 | Biochemistry |
| 1990 | Medium | The Neurospora crassa alc gene encoding allantoicase is transcribed as a single ~1.2 kb mRNA. Expression requires induction by uric acid and is positively regulated by nit-2 and negatively regulated by nmr; both control genes affect alc mRNA levels and allantoicase enzyme activity under both induced and nitrogen-repressed conditions. | PMID:1978237 | Molecular & general genetics : MGG |
| 2014 | Low | In Dictyostelium discoideum, RNAi-mediated knockdown of allC (allantoicase ortholog) caused a shortened cell cycle and developmental arrest after aggregation (cells aggregate but undergo no further morphological development). Molecular analysis revealed significant downregulation of myosin II heavy chain protein and mRNA, DdCAD-1 mRNA and protein, 14-3-3 protein and mRNA, and type A von Willebrand factor domain-containing protein mRNA in allC RNAi mutants, suggesting that myosin II heavy chain downregulation contributes to the developmental interruption and that 14-3-3 and VWA-domain protein downregulation contributes to cell cycle shortening. | PMID:24938606 | Genetics and molecular research : GMR |

## Citations

- PMID:1978237
- PMID:2148685
- PMID:24938606
