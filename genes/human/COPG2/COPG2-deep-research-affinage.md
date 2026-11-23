---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/COPG2
affinage_run_date: 2026-06-09T22:57:19
uniprot_accession: Q9UBF2
self_evaluation_pairwise: loss
faith_pct: 100.0
n_discoveries: 4
citation_count: 4
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for COPG2 (human)

## Current model (mechanistic narrative)

COPG2 encodes a coatomer (COPI) complex subunit (gamma2-COP) whose locus is a model for tissue- and species-specific allelic regulation rather than for vesicle-trafficking mechanism per se in the available corpus [PMID:22053079]. In mouse, Copg2 is subject to allele-biased expression driven by its genomic neighbor Mest: tissue-specific alternative polyadenylation at Mest generates extended antisense MestXL transcripts that read >10 kb into Copg2, and this transcriptional interference produces maternal-allele-biased Copg2 expression in CNS tissues while non-CNS tissues remain biallelic; truncating Mest to abolish MestXL also abolishes the Copg2 allelic bias, establishing MestXL-mediated transcriptional interference as the causal mechanism [PMID:22053079]. A paternal-specific differentially methylated region at the Copg2 promoter CpG island is associated with the locus but is insufficient on its own to silence Copg2, since in an interspecific hybrid the methylation occurs without monoallelic expression [PMID:12879359]. The locus is further marked by reciprocally imprinted antisense transcripts (Copg2AS, Copg2AS2, and human CIT1), and human COPG2 itself escapes imprinting and is biallelically expressed while the antisense transcript alone shows allelic asymmetry [PMID:12879359, PMID:10995575]. The molecular and cellular function of the COPG2 protein in COPI coat assembly or trafficking has not been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** *(none)*
- **localization:** *(none)*
- **pathway (Reactome):** *(none)*
- **partners:** *(none)*
- **complexes:** COPI coatomer

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2011 | Medium | Tissue-specific alternative polyadenylation at the Mest locus produces longer RNA variants (MestXL) that extend >10 kb into the antisense gene Copg2; in CNS tissues where MestXL is expressed, transcriptional interference from MestXL causes preferential (maternal-allele-biased) expression of Copg2, whereas in non-CNS tissues Copg2 is biallelically expressed. A targeted truncation allele at Mest that abolishes MestXL formation also abolishes the allelic bias at Copg2, establishing MestXL-mediated transcriptional interference as the mechanistic basis for tissue-specific allelic regulation of Copg2. | PMID:22053079 | Nucleic acids research |
| 2003 | Medium | A differentially methylated region (DMR) with paternal-specific methylation exists at the promoter-associated CpG island of mouse Copg2; however, in the interspecific F1 hybrid (C57BL/6 × M. spretus), this paternal-specific methylation is not accompanied by allele-specific (monoallelic) expression of Copg2, demonstrating that promoter CpG island methylation alone is not sufficient to silence Copg2 expression. A novel antisense transcript (Copg2AS2) originating at the Copg2 promoter region is expressed monoallelically and correlates with the differential methylation. | PMID:12879359 | Mammalian genome |
| 2000 | Low | Mouse Copg2 is paternally imprinted (preferentially expressed from the maternal allele) in embryos, neonates, and adult brain, with partial imprinting in other tissues; an antisense transcript Copg2AS overlapping the 3'-UTRs of Copg2 and Peg1/Mest is maternally imprinted, indicating a reciprocal imprinting relationship between the sense and antisense transcripts at this locus. | PMID:10788617 | FEBS letters |
| 2000 | Low | Human COPG2 (gamma2-COP) on chromosome 7q32 escapes genomic imprinting and is biallelically expressed in all fetal tissues and adult blood lymphocytes examined; an antisense transcript CIT1 within intron 20 of COPG2 is paternally expressed (monoallelic) in fetal tissues, establishing allelic asymmetry only at the non-coding antisense transcript and not the COPG2 protein-coding gene itself. | PMID:10995575 | Genomics |

## Citations

- PMID:10788617
- PMID:10995575
- PMID:12879359
- PMID:22053079
