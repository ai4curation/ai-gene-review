---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/APOO
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9BUR5
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 12
citation_count: 10
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for APOO (human)

## Current model (mechanistic narrative)

APOO (MIC26) encodes a 22 kDa integral inner mitochondrial membrane protein that functions as a subunit of the MICOS complex governing crista junction formation and mitochondrial ultrastructure [PMID:25764979, PMID:26217776]. It is incorporated into MICOS through physical interactions with MIC60, MIC27, and MIC10, and its depletion reduces crista junction number and distorts cristae architecture [PMID:25764979, PMID:26217776]. Within the complex MIC26 acts antagonistically to its paralog MIC27 (APOOL): it destabilizes the MIC10 oligomeric scaffold that MIC27 stabilizes, and the two proteins reciprocally regulate each other's levels [PMID:25764979, PMID:26217776, PMID:29733859]. MIC26 and MIC27 assemble late into MICOS and are dispensable for integration of the remaining subunits, but together they are required for cardiolipin homeostasis and for the integrity of respiratory chain supercomplexes and F1Fo-ATP synthase, with cardiolipin synthase overexpression rescuing supercomplex stability in double-knockout cells [PMID:32788226]. Through this role MIC26 shapes mitochondrial bioenergetics and physiology: adipocyte-specific loss impairs oxidative phosphorylation and shifts metabolism toward glycolysis [PMID:37088120], and macrophage-specific loss enhances efferocytosis by lowering OPA1 levels to drive mitochondrial fission [PMID:37995600]. Pathogenic APOO mutations—a missense I117T that impairs import and membrane insertion, and a C-terminal-truncating nonsense E178* that destabilizes the protein—disrupt MICOS assembly and cristae architecture, causing X-linked mitochondrial disease [PMID:32439808, PMID:37649161]. An earlier model of APOO as a secreted glycoprotein acting in cholesterol efflux [PMID:16956892] was shown to reflect non-specific signal rather than a genuine protein isoform; MIC26 is exclusively mitochondrial [PMID:37279200].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0005198 structural molecule activity
- **localization:** GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-1852241 Organelle biogenesis and maintenance, R-HSA-1430728 Metabolism
- **partners:** MIC60, MIC27, MIC10
- **complexes:** MICOS complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2006 | Medium | ApoO (APOO) is a secreted glycoprotein that belongs to the proteoglycan family (contains chondroitin sulfate chains), co-localizes with perilipins at lipid droplets, promotes cholesterol efflux from macrophages, and requires microsomal triglyceride transfer protein (MTP) activity for secretion. | PMID:16956892 | The Journal of biological chemistry |
| 2015 | High | The non-glycosylated 22 kDa mitochondrial isoform of MIC26 (APOO) spans the mitochondrial inner membrane, physically interacts with MICOS complex subunits MIC60, MIC27, and MIC10, and is required for crista junction formation; its depletion reduces crista junction number and alters mitochondrial ultrastructure. | PMID:25764979, PMID:26217776 | Biochimica et biophysica acta |
| 2015 | Medium | MIC26 and MIC27 (APOOL) regulate each other's protein levels in an antagonistic manner; overexpression of MIC26 increases MIC10 levels while depletion of MIC26 increases MIC27 levels. Both proteins are positively correlated with tafazzin levels, linking MIC26 to cardiolipin remodeling. | PMID:25764979, PMID:26217776 | Biochimica et biophysica acta |
| 2015 | Medium | Overexpression of MIC26 induces mitochondrial fragmentation, promotes ROS formation, and impairs mitochondrial respiration; knockdown of MIC26 decreases mitochondrial oxygen consumption. | PMID:25764979 | Biochimica et biophysica acta |
| 2018 | High | MIC26 destabilizes Mic10 oligomers in an antagonistic manner to MIC27 (which stabilizes Mic10 oligomers), demonstrating that MIC26 negatively regulates the oligomeric scaffold formed by the core MICOS subunit Mic10. | PMID:29733859 | Journal of molecular biology |
| 2020 | High | MIC26 and MIC27 together are required for integrity of respiratory chain (super)complexes and F1Fo-ATP synthase (including integration of F1 subunits), and cooperatively regulate cardiolipin levels; restoring cardiolipin by overexpression of cardiolipin synthase in double knockout cells rescues respiratory chain supercomplex stability. | PMID:32788226 | Life science alliance |
| 2020 | Medium | MIC26 and MIC27 are dispensable for stability and integration of the remaining MICOS subunits into the complex, indicating they assemble late into MICOS. | PMID:32788226 | Life science alliance |
| 2020 | High | A missense mutation (I117T) in APOO impairs MIC26 import processing and insertion into the inner mitochondrial membrane, causing altered MICOS assembly and crista junction disruption; corresponding mutations in yeast and Drosophila models confirmed MIC26 involvement in MICOS assembly and mitochondrial function. | PMID:32439808 | Journal of medical genetics |
| 2023 | Medium | A nonsense mutation (E178*) in APOO/MIC26 producing a truncated protein lacking 20 C-terminal amino acids results in a highly unstable protein; remaining mutant MIC26 correctly localizes to mitochondria and physically interacts with other MICOS subunits, but cannot restore normal cristae architecture in MIC26 KO cells. | PMID:37649161 | Clinical genetics |
| 2023 | High | MIC26 and MIC27 are exclusively mitochondrial proteins (22 kDa and 30 kDa respectively); the previously reported 55 kDa glycosylated secreted MIC26 isoform is a non-specific signal, not a genuine MIC26 protein form, as confirmed by knockout lines, four independent antibodies, epitope-tagged constructs, glycosylation site mutagenesis, and mass spectrometry. | PMID:37279200 | PloS one |
| 2023 | Medium | Adipocyte-specific APOO knockout mice show disrupted mitochondrial structure in brown adipocytes, impaired oxidative phosphorylation, shift from oxidative to glycolytic metabolism, increased lipogenic enzyme levels, reduced long-chain fatty acid oxidation, and disturbed peroxisomal biogenesis and very-long-chain fatty acid oxidation via PPARα. | PMID:37088120 | Metabolism: clinical and experimental |
| 2023 | Medium | Macrophage-specific MIC26 (APOO) deletion increases efferocytosis by reducing mitochondrial OPA1 protein levels (causing increased mitochondrial fission and reduced membrane potential); OPA1 silencing phenocopied the efferocytosis increase, and OPA1 overexpression abolished the efferocytosis enhancement caused by MIC26 deficiency. | PMID:37995600 | Atherosclerosis |

## Citations

- PMID:16956892
- PMID:25764979
- PMID:26217776
- PMID:29733859
- PMID:32439808
- PMID:32788226
- PMID:37088120
- PMID:37279200
- PMID:37649161
- PMID:37995600
