# Primary identity and catalytic scope: PMID30670548

Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC6416908/?pdf=1 (complete primary HTML acquired 2026-11-07). The protected publication cache remains abstract-only. Full source bytes and extraction are in ignored cache; provenance.json records the successful acquisition hash.

## Assay identity

The paper reports cloning from S. meliloti 3D0a2 (DSMZ30135), using Rm2011 sequence designs, and states:

> The sequences were 100% identical to those from S. meliloti Rm2011

The independently acquired CP004140.1 region 2423202–2443202 contains SM2011_c01637/AGG74839.1 and SM2011_c01638/AGG74840.1. Their translations match the frozen strain 1021 Q92NF6 (300/300 residues) and Q92NF5 (496/496 residues), respectively. These are protein identity bridges, not identity of strain phenotypes. The authors sequence-verified modified pET22b expression plasmids; affinity-purified recombinant proteins were produced in E. coli. A complete expression-plasmid sequence and exact residual tag sequence were not independently compared here.

## Catalysis and domain roles

The primary section heading reads:

> Smc01638 is a trifunctional enzyme (CDH thioesterase).

Purified full-length Smc01638 performs NAD-dependent carnitine oxidation and hydrolysis of both carnitinyl-CoA and betainyl-CoA. Table 1 reports carnitine Km940µM/kcat6.2s−1, NAD Km154µM, carnitinyl-CoA Km 12µM/kcat 0.9s−1, and betainyl-CoA Km 12µM/kcat 142.3s−1. These conditions establish different rates, not absence of the slower function. Metabolomics detects carnitinyl-CoA in GBB-grown 3D0a2 cells, and the reconstructed upstream BcoAB/C/D sequence supplies it; a direct carnitine ligase is not needed. Carnitinyl-CoA hydrolysis produces carnitine upstream of the module's boundary, while oxidation and betainyl-CoA hydrolysis perform its first and last reactions. The N-terminal dehydrogenase and C-terminal hotdog assignments are supported by the curated target architecture and similarity to separately characterized Pseudomonas enzymes; the 2019 assays used the intact fusion, not isolated target domains. Proposed channeling is a hypothesis, not a measured endpoint.

BcoG/Smc01637 was kinetically assayed for dehydrocarnitine plus acetyl-CoA conversion and used to synthesize betainyl-CoA. Table 1 gives dehydrocarnitine Km13µM/kcat0.24s−1 and acetyl-CoA Km118µM. This supports the cleavage/acyl-transfer role independently of the BKACE family name. The source does not establish every substrate reaction of that diverse family for BcoG.

## Native phenotype limits and source defect

The Rm2011 mutant list in Methods and the growth experiments cover c01638, c01639, c01640 and c01641. It does not include c01637/BcoG. Accordingly the UniProt Q92NF6 disruption statement and inherited IMP proposal cannot be supported by this paper's listed mutants. BcoG participation is independently supported by catalysis, and is retained in its existing metabolic-process refinement and core synthesis; the historical IMP proposal is explicitly retired, not silently deleted.

Rm2011 and 3D0a2 grow on GBB under the reported conditions, whereas five tested Rm1021 stocks did not, despite the reported 20 kb locus identity. Catalytic identity therefore must not be presented as demonstrated native GBB growth in1021. The c01638 mutant supports BcoEF's role in the Rm2011 pathway but does not separate its three activities. No conclusion about carnitine-specific growth in1021 follows solely from the GBB-negative result. The paper also reports failure to grow KT2440 on GBB; this does not negate its downstream carnitine-catabolic chemistry.
