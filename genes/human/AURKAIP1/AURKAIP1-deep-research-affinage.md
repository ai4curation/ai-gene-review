---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AURKAIP1
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9NWT8
self_evaluation_pairwise: win
faith_pct: 100.0
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

# Affinage mechanistic annotation for AURKAIP1 (human)

## Current model (mechanistic narrative)

AURKAIP1 is a multifunctional protein whose best-supported role is as a bona fide protein component of the mammalian mitochondrial ribosome small subunit (designated MRPS38/mS38), essential for mitochondrial protein synthesis [PMID:23908630]. Work in the yeast ortholog (Cox24p/mS38) establishes that it functions as an intrinsic ribosomal regulator of mRNA-specific translation, being required for efficient mitoribogenesis and preferentially needed for translation initiation of the cytochrome c oxidase subunit mRNAs COX1, COX2, and COX3, with an additional role in COX1 pre-mRNA intron processing [PMID:16339141, PMID:30968120]. Independently of its mitoribosomal function, AURKAIP1 acts as a negative regulator of Aurora-A kinase: it forms a ternary complex with antizyme1 (Az1) and Aurora-A, enhances Az1 binding to Aurora-A, and drives proteasome-dependent but ubiquitin-independent degradation of Aurora-A [PMID:17125467, PMID:17452972]. AURKAIP1 also scaffolds the PKA catalytic subunit (PKAc) to the NF-κB p65 subunit in the cytosol, controlling the rate of TNFα-stimulated p65 nuclear translocation through PKAc-dependent phosphorylation of p65-Ser276 [PMID:21556136]. In triple-negative breast cancer cells it stabilizes DDX5 by blocking its ubiquitination, thereby supporting Wnt/β-catenin signaling and proliferation [PMID:38040691].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0005198 structural molecule activity, GO:0045182 translation regulator activity, GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005739 mitochondrion, GO:0005840 ribosome, GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-8953854 Metabolism of RNA, R-HSA-392499 Metabolism of proteins, R-HSA-162582 Signal Transduction
- **partners:** AURKA, OAZ1, PRKACA, RELA, DDX5
- **complexes:** mitochondrial ribosome small subunit (MRPS38/mS38)

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2007 | High | AURKAIP1 promotes Aurora-A degradation through a proteasome-dependent but ubiquitin-independent mechanism. AURKAIP1 inhibits polyubiquitination of Aurora-A, and a non-interactive AURKAIP1 mutant that cannot destabilize Aurora-A restores ubiquitination. Degradation persists in cells lacking E1 ubiquitin-activating enzyme (ts-20 CHO cells at restrictive temperature), confirming ubiquitin-independence. | PMID:17125467 | The Biochemical journal |
| 2007 | High | Antizyme1 (Az1) mediates AURKAIP1-dependent degradation of Aurora-A. AURKAIP1, Az1, and Aurora-A form a ternary complex, and AURKAIP1 enhances the binding affinity of Az1 to Aurora-A, promoting proteasome-dependent but ubiquitin-independent Aurora-A degradation. Az inhibitor (AzI) abrogates AURKAIP1-mediated degradation, and an Aurora-A mutant defective in Az1 interaction cannot be degraded by AURKAIP1. | PMID:17452972 | Oncogene |
| 2013 | High | AURKAIP1 (designated MRPS38) is a bona fide protein component of the mammalian mitochondrial ribosome small subunit, identified by mass spectrometry of purified mitoribosome fractions. siRNA knockdown of AURKAIP1 significantly reduces expression of mitochondrially encoded proteins, demonstrating an essential role in mitochondrial protein synthesis. | PMID:23908630 | Frontiers in physiology |
| 2011 | High | AKIP1 (AURKAIP1) simultaneously binds PKAc and the p65 subunit of NF-κB in resting cells, scaffolding PKAc to NF-κB in the cytosol. This interaction regulates the rate of p65 nuclear translocation: AKIP1 overexpression enhances TNFα-stimulated nuclear accumulation of p65, correlating with decreased phosphorylation of p65-Ser276 by PKAc. Disruption of AKIP1–PKAc interaction (by a competing peptide CAT 1-29) also accelerates p65 nuclear translocation. | PMID:21556136 | PloS one |
| 2005 | Medium | The yeast ortholog of AURKAIP1, Cox24p (ORF YLR204W), is required for processing of COX1 pre-mRNA introns aI2 and aI3 in Saccharomyces cerevisiae mitochondria. Northern blot analyses of cox24 null mutants show a block in processing of these introns. The growth defect is partially rescued in intronless mitochondrial DNA strains. Cox24-cox14 double mutant analysis indicates Cox24p also has a function related to COX1 mRNA translation. | PMID:16339141 | The Journal of biological chemistry |
| 2019 | Medium | In yeast, the mitoribosome small subunit protein mS38 (Cox24/AURKAIP1 ortholog) is required for efficient mitoribogenesis and is preferentially needed for translation initiation of COX1, COX2, and COX3 mRNAs. Deletion of mS38 causes ~2-fold compensatory increase in mitoribosome abundance but still reduces overall mitochondrial protein synthesis rate. mRNA-specific translational activator levels are unaffected, placing mS38 as an intrinsic ribosomal regulator of mRNA-specific translation. | PMID:30968120 | Nucleic acids research |
| 2023 | Medium | AURKAIP1 directly interacts with and stabilizes DDX5 protein in triple-negative breast cancer cells by preventing DDX5 ubiquitination and proteasomal degradation. Knockdown of AURKAIP1 reduces DDX5 protein levels; DDX5 overexpression rescues the proliferation inhibition caused by AURKAIP1 knockdown. AURKAIP1 silencing suppresses Wnt/β-catenin signaling in a DDX5-dependent manner. | PMID:38040691 | Cell death & disease |
| 2025 | Medium | CYFIP1 collaborates with the m7G methyltransferase RNMT to induce m7G methylation of AURKAIP1 mRNA, increasing its mRNA stability and translation. Elevated AURKAIP1 protein (as a mitochondrial small ribosomal subunit protein) dysregulates mitochondrial translation, increasing FDX1 expression and triggering cuproptosis in osteosarcoma cells. | PMID:39984834 | Molecular medicine (Cambridge, Mass.) |
| 2018 | Low | BCA3/AKIP1 (AURKAIP1) is incorporated into HIV-1 particles and requires its C-terminus for packaging. The C-terminus of BCA3 is the binding site for the catalytic subunit of PKA (PKAc), and BCA3 incorporation into HIV-1 particles is mediated by its interaction with PKAc (which is itself packaged into HIV-1). However, incorporated BCA3 has no detectable effect on HIV-1 infectivity (negative result). | PMID:29677171 | Viruses |

## Citations

- PMID:16339141
- PMID:17125467
- PMID:17452972
- PMID:21556136
- PMID:23908630
- PMID:29677171
- PMID:30968120
- PMID:38040691
- PMID:39984834
