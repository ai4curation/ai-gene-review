---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ABHD14B
affinage_run_date: 2026-06-09T22:02:37
uniprot_accession: Q96IU4
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 5
citation_count: 4
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ABHD14B (human)

## Current model (mechanistic narrative)

ABHD14B is a serine hydrolase that functions as a lysine deacetylase (KDAC), transferring an acetyl group from post-translationally acetylated protein lysine residues onto coenzyme A to generate acetyl-CoA while regenerating the free lysine amine [PMID:31478652]. Through this deacetylation/acetyl-transfer activity it acts as a regulator of central carbon metabolism: loss of ABHD14B reduces flux of glucose through glycolysis and the citric acid cycle in mammalian cells, and hepatic depletion in mice produces defective systemic glucose metabolism that is most pronounced during fasting [PMID:35700823]. The same KDAC activity is deployed in an antiviral context, where ABHD14B is recruited to hepatitis B virus covalently closed circular DNA (cccDNA) via the cccDNA-binding factor TFII-I and deacetylates cccDNA-associated histones to suppress HBV RNA transcription [PMID:40658808]. Sequence determinants that distinguish ABHD14B from the closely related, functionally unannotated ABHD14A have been defined, supporting its specific assignment as the KDAC-active enzyme of the pair [PMID:37974539].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0016787 hydrolase activity, GO:0016740 transferase activity
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-1430728 Metabolism, R-HSA-4839726 Chromatin organization
- **partners:** GTF2I
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2019 | High | ABHD14B was annotated as a lysine deacetylase (KDAC) that transfers an acetyl group from a post-translationally acetylated protein lysine residue to coenzyme A (CoA), yielding acetyl-CoA and regenerating the free amine on the lysine. This activity was validated by in vitro biochemical assays with recombinant human ABHD14B and by cellular knockdown experiments. A putative substrate binding site was also identified. | PMID:31478652 | Biochemistry |
| 2022 | High | Loss of ABHD14B in mammalian cells results in significantly decreased flux of glucose through glycolysis and the citric acid cycle, as determined by combined transcriptomics and metabolomics. Hepatic depletion of ABHD14B in mice additionally causes defective systemic glucose metabolism, particularly during fasting, establishing ABHD14B as a regulator of glucose metabolism in vivo. | PMID:35700823 | The Journal of biological chemistry |
| 2023 | Medium | Bioinformatics coupled with biochemical experiments identified key sequence determinants that distinguish ABHD14B from the closely related ABHD14A, enabling correct classification of each enzyme. The study mapped both enzymes on an evolutionary timescale and showed that despite high sequence similarity, ABHD14B has KDAC activity while ABHD14A remains functionally unannotated. | PMID:37974539 | Proteins |
| 2025 | Medium | ABHD14B was identified as a host protein that interacts with hepatitis B virus covalently closed circular DNA (cccDNA) via TFII-I, a protein that binds cccDNA in a sequence-dependent manner. ABHD14B decreases acetylation levels of histone proteins associated with cccDNA, thereby inhibiting HBV RNA transcription from cccDNA. Knockout of ABHD14B confirmed its suppressor role in HBV transcription. | PMID:40658808 | Hepatology communications |
| 2019 | Low | ABHD14B was originally identified as associated with the transcription initiation factor TFIID (CCG1/TAFII250-interacting factor B), and its crystal structure was determined, though its endogenous substrates remained elusive prior to the KDAC annotation in this same paper. | PMID:31478652 | Biochemistry |

## Citations

- PMID:31478652
- PMID:35700823
- PMID:37974539
- PMID:40658808
