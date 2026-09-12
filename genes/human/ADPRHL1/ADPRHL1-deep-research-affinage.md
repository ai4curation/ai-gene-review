---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ADPRHL1
affinage_run_date: 2026-06-09T22:02:42
uniprot_accession: Q8NDY3
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 7
citation_count: 6
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for ADPRHL1 (human)

## Current model (mechanistic narrative)

ADPRHL1 is a catalytically inactive member of the ADP-ribosylhydrolase family whose principal characterized role is in cardiac myofibrillogenesis and ventricular chamber outgrowth [PMID:27217161]. Although it lacks the active-site residues required for ADP-ribosylhydrolase catalysis, its function depends not on catalysis but on a modified substrate-binding cleft centered on a di-arginine (Arg271-Arg272) loop; disruption of this loop abolishes ventricular myofibril assembly, and cardiac activity is concentrated in the C-terminal portion of the protein [PMID:27217161, PMID:32726316]. Consistent with a direct structural role, recombinant ADPRHL1 localizes to stripes adjacent to the Z-disc and modulates actin filament and Z-disc dynamics, with both loss and overexpression disrupting sarcomere organization [PMID:27217161]. In human stem cell-derived cardiomyocytes, ADPRHL1 maintains focal adhesion formation, calcium transients, and electrophysiological activity by suppressing the ROCK-myosin II pathway, and pharmacological ROCK or myosin II inhibition rescues these defects [PMID:37880701]. Beyond the heart, wild-type ADPRHL1 restrains cell proliferation, while a recurrent germline loss-of-function variant (p.D78V) activates PARP1 and enhances DNA damage response and prostate cancer cell survival in a manner reversible by olaparib [PMID:35816343]. Its promoter is subject to epigenetic repression through an HDAC4/MEF2/SUV39H1 axis in cardiomyocytes [PMID:34492228].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0098772 molecular function regulator activity, GO:0008092 cytoskeletal protein binding
- **localization:** GO:0005856 cytoskeleton
- **pathway (Reactome):** R-HSA-1266738 Developmental Biology, R-HSA-397014 Muscle contraction, R-HSA-1643685 Disease
- **partners:** PARP1
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2016 | High | Adprhl1 is essential for striated myofibril assembly and ventricular chamber outgrowth in Xenopus laevis; morpholino knockdown inhibits myofibrillogenesis while overexpression causes disarrayed, branching myofibrils with sarcomere division at the actin-Z-disc boundary, and recombinant Adprhl1 localizes to stripes adjacent to the Z-disc, indicating a direct role in modifying Z-disc and actin dynamics. | PMID:27217161 | Developmental biology |
| 2016 | Medium | Structural modelling indicates Adprhl1 is a pseudoenzyme lacking key catalytic residues required for ADP-ribosylhydrolase activity, classifying it as catalytically inactive despite belonging to the ADP-ribosylhydrolase protein family. | PMID:27217161 | Developmental biology |
| 2020 | High | CRISPR/Cas9 knockout targeting a di-arginine (Arg271-Arg272) peptide loop at the centre of the ancestral ADP-ribosylhydrolase binding cleft in exon 6 causes loss of ventricular myofibril assembly, demonstrating that the modified substrate-binding cleft—not catalytic activity—is required for Adprhl1 cardiac function; mice lacking exons 3-4 are normal but retain the smaller ADPRHL1 species, indicating cardiac activity is concentrated in the C-terminal protein portion. | PMID:32726316 | PloS one |
| 2023 | High | ADPRHL1 knockout in human embryonic stem cell-derived cardiomyocytes causes abnormal cell adhesion, disrupted focal adhesion formation, and perturbations in calcium transients and electrophysiological activity via excessive upregulation of the ROCK-myosin II pathway; pharmacological inhibition of ROCK or myosin II restores focal adhesions and improves electrical conduction and calcium activity. | PMID:37880701 | Stem cell research & therapy |
| 2022 | Medium | A recurrent ADPRHL1 germline loss-of-function mutation (c.A233T; p.D78V) activates PARP1, leading to increased H2O2- or cisplatin-induced DNA damage response and enhanced prostate cancer cell survival; wild-type ADPRHL1 expressed in prostate cancer cells suppresses cell proliferation and oncogenesis, and PARP1 inhibition with olaparib suppresses cell survival induced by mutant ADPRHL1. | PMID:35816343 | Molecular cancer research : MCR |
| 2021 | Medium | HDAC4 represses transcription from the Adprhl1 promoter through a mechanism requiring the methyltransferase SUV39H1; MEF2 binding sites are overrepresented in Adprhl1 promoter regions that gain activating histone marks (H3K9ac, H3K4me3) upon HDAC4 deletion, identifying the Adprhl1 promoter as a target of HDAC4/MEF2/SUV39H1-mediated epigenetic repression in cardiomyocytes. | PMID:34492228 | Journal of molecular and cellular cardiology |
| 2025 | Low | ARH2 (ADPRHL1) promotes M2 macrophage polarization and suppresses immune responses in lung adenocarcinoma by regulating the FPR2/PI3K/AKT signaling pathway; siRNA-mediated knockdown of ARH2 delivered via a nanoparticle system activates anti-tumor immune responses. | PMID:40801020 | Bioactive materials |

## Citations

- PMID:27217161
- PMID:32726316
- PMID:34492228
- PMID:35816343
- PMID:37880701
- PMID:40801020
