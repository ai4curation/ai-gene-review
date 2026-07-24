---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/RFWD3
affinage_run_date: 2026-06-10T06:43:36
uniprot_accession: Q6PCD5
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 17
citation_count: 17
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for RFWD3 (human)

## Current model (mechanistic narrative)

RFWD3 is a RING-finger/WD40 E3 ubiquitin ligase that governs the resolution and restart of stalled and damaged DNA replication forks by remodeling the protein composition of single-stranded DNA at sites of replication stress [PMID:26474068, PMID:33321094]. It is recruited to damaged chromatin and stalled forks through a direct interaction between its C-terminal coiled-coil/WD40 region and the RPA2 subunit of RPA, an interaction required for ATR-dependent Chk1 activation and for localization to interstrand crosslink (ICL)-stalled forks [PMID:21558276, PMID:21504906, PMID:28575657]. At ongoing forks RFWD3 also associates with PCNA via a PIP motif, an interaction that stabilizes the ligase and supports normal fork progression [PMID:30530694]. RFWD3 catalyzes multi-site polyubiquitination of the RPA complex and of RAD51, modifications that depend on ATR/ATM phosphorylation of RFWD3 and drive VCP/p97-mediated extraction of these factors from DNA, enabling late-phase homologous recombination, fork restart, and ICL repair [PMID:26474068, PMID:28575658]. By promoting PCNA ubiquitination, RFWD3 licenses translesion synthesis and recruits the DNA translocase ZRANB3 to catalyze fork reversal [PMID:33321094, PMID:37036693]. Biallelic RFWD3 mutations that disrupt RPA binding and chromatin recruitment cause Fanconi anemia complementation group W, with affected cells showing defective HR, ICL hypersensitivity, and chromosomal breakage [PMID:28575657, PMID:28691929]. Beyond the replication-stress core, RFWD3 cooperates with Mdm2 to stabilize p53 in the late DNA-damage response [PMID:20173098], and is itself controlled by UHRF1-mediated ubiquitination in a negative-feedback circuit with RAD51 [PMID:40940676].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0016874 ligase activity, GO:0140096 catalytic activity, acting on a protein
- **localization:** GO:0005634 nucleus, GO:0000228 nuclear chromosome
- **pathway (Reactome):** R-HSA-73894 DNA Repair, R-HSA-69306 DNA Replication, R-HSA-1643685 Disease, R-HSA-392499 Metabolism of proteins
- **partners:** RPA2, RAD51, PCNA, MDM2, ZRANB3, UHRF1, TREX1
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2010 | Medium | RFWD3 forms a complex with Mdm2 and p53, synergistically ubiquitinates p53 in vitro, and is required to stabilize p53 in the late response to DNA damage. RFWD3-Mdm2 complex restricts polyubiquitination of p53 by Mdm2 alone. RFWD3 is phosphorylated by ATM/ATR kinases, and phosphorylation mutants fail to stimulate p53 ubiquitination. | PMID:20173098 | Proceedings of the National Academy of Sciences of the United States of America |
| 2011 | Medium | RFWD3 directly interacts with RPA (specifically RPA2 subunit) and is recruited to sites of DNA damage in a RPA-dependent manner. The C-terminus of RFWD3 (coiled-coil and WD40 domains) is necessary for RPA binding. Loss of RFWD3 results in persistent γH2AX and RAD51 foci in damaged cells. | PMID:21558276 | The Journal of biological chemistry |
| 2011 | Medium | RFWD3 directly interacts with RPA2 using purified proteins, is recruited to stalled replication forks, co-localizes with RPA2 under replication stress, and is required for ATR-dependent Chk1 activation. Deletion of the RPA2-binding region on RFWD3 impairs its localization to stalled forks and decreases Chk1 activation. | PMID:21504906 | The Journal of biological chemistry |
| 2015 | High | RFWD3 mediates multi-site ubiquitination of the entire RPA complex upon replication fork stalling. Ubiquitination occurs on chromatin at sites outside the DNA binding channel, does not cause proteasomal degradation, and increases under fork collapse conditions. RFWD3 is necessary for replication fork restart, normal repair kinetics during replication stress, and homologous recombination at stalled replication forks. | PMID:26474068 | Molecular cell |
| 2017 | High | RFWD3 mutations cause Fanconi anemia (FANCW). An I639K substitution in the WD40 repeats abolishes interaction of RFWD3 with RPA, preventing RFWD3 recruitment to ICL-stalled replication forks. Single point mutations in RPA32 that abolish RFWD3 interaction also inhibit ICL repair. Unloading of RPA from ICL-induced sites is perturbed in RFWD3-deficient cells. | PMID:28575657 | Molecular cell |
| 2017 | High | RFWD3 is the FA gene FANCW. Patient-derived mutations in RFWD3 impair its relocation to chromatin and physical interaction with RPA. RFWD3-mutant cells show defective HR, increased ICL sensitivity, G2 arrest, and chromosomal breakage. Rfwd3 knockout mice show increased embryonic lethality, subfertility, and gonadal atrophy. | PMID:28691929 | The Journal of clinical investigation |
| 2017 | High | RFWD3 polyubiquitinates both RPA and RAD51 in vitro and in vivo. Phosphorylation by ATR and ATM is required for this ubiquitination activity in vivo. RFWD3 promotes VCP/p97-mediated protein dynamics and subsequent degradation of both RPA and RAD51, thereby removing them from DNA damage sites. MMC-induced chromatin loading of MCM8 and RAD54 is defective in RFWD3-inactivated cells or cells expressing ubiquitination-deficient RAD51, indicating RAD51 ubiquitination is needed for late-phase HR. | PMID:28575658 | Molecular cell |
| 2018 | High | RFWD3 localizes at replication forks in unperturbed cells and associates with PCNA via a PIP motif. PCNA association is critical for RFWD3 stability. Cells lacking RFWD3 show slower fork progression, prolonged S phase, and increased loading of replication fork components. The S-phase defect is rescued by WT RFWD3 but not by a PIP mutant. RFWD3-PCNA interaction enables polyubiquitination of RPA for proper DNA replication. | PMID:30530694 | Proceedings of the National Academy of Sciences of the United States of America |
| 2020 | High | RFWD3 promotes ubiquitylation of proteins on ssDNA at stalled forks, which is required for PCNA ubiquitylation. Absence of RFWD3 leads to defective recruitment of key repair and signaling factors to damaged chromatin, inhibits PCNA ubiquitylation, and drastically impairs translesion DNA synthesis (TLS) across different DNA lesions. | PMID:33321094 | Molecular cell |
| 2020 | Medium | In BRCA2-deficient cells, stalled forks accumulate phosphorylated and ubiquitinated RPA (ubq-pRPA); the ubiquitination is mediated by RFWD3 and depends on SMARCAL1-dependent fork reversal. Co-depletion of RFWD3 rescues fork degradation, collapse, and cell sensitivity in BRCA2-deficient cells. | PMID:32391871 | The Journal of cell biology |
| 2020 | Low | The E3 ligase activity of RFWD3 is required for stabilization of the Origin Recognition Complex (ORC) and ORC-Associated protein (ORCA/LRWD1) in cells expressing wild-type p53. RFWD3 associates with ORC/ORCA (Co-IP), and depletion of RFWD3 reduces ORC/ORCA protein levels. Overexpression of ORC/ORCA leads to stabilization of RFWD3. | PMID:33044890 | Cell cycle (Georgetown, Tex.) |
| 2020 | Medium | The Drosophila ortholog of RFWD3 (Mus302) functions independently of RAD51 during DNA repair, and evidence does not support a role for Mus302 in repair of collapsed replication forks or DSBs through HR — in contrast to the human protein. The N-terminal third of RFWD3 is present only in mammals, suggesting this domain underlies the acquisition of HR-related functions in mammals. | PMID:31900333 | G3 (Bethesda, Md.) |
| 2022 | Medium | RFWD3 contributes to PCNA modification-dependent DNA damage tolerance independently of both the Fanconi anemia pathway and DNA polymerase η. RFWD3's role in cellular survival after UV irradiation is dependent on PCNA modifications at K164. | PMID:35905994 | Life science alliance |
| 2023 | High | RFWD3 promotes recruitment of the DNA translocase ZRANB3 to stalled replication forks and ubiquitinated sites of DNA damage. RFWD3 stimulates fork remodeling (reversal) in a ZRANB3-epistatic manner. RFWD3 promotes PCNA ubiquitination and interaction with ZRANB3, providing the mechanism for ZRANB3 recruitment. Inactivation of RFWD3 in BRCA2-deficient cells rescues fork degradation analogously to ZRANB3 inactivation. | PMID:37036693 | The Journal of cell biology |
| 2025 | Medium | UHRF1 acts as an E3 ubiquitin ligase for RFWD3, ubiquitinating and destabilizing it to prevent premature RAD51 removal during HR. RAD51 in turn protects RFWD3 from UHRF1, establishing a negative feedback circuit. Phosphorylation of UHRF1 (regulated by phosphatase PP4) controls its E3 activity toward RFWD3. | PMID:40940676 | Advanced science (Weinheim, Baden-Wurttemberg, Germany) |
| 2025 | Medium | RFWD3 competes with E3 ligase TRIM24 to stabilize TREX1 (a cytosolic dsDNA degrader) by sequestering it from TRIM24-mediated proteasomal degradation. RFWD3 inhibition increases intracellular dsDNA, activates STING-IFN signaling, decreases MDSCs, and enhances PD-L1 blockade efficacy. RFWD3 was identified as a TREX1-interacting protein by mass spectrometry. | PMID:41117130 | Advanced science (Weinheim, Baden-Wurttemberg, Germany) |
| 2025 | Medium | SLFN11 antagonizes the RFWD3-PRIMPOL fork restart pathway by disrupting recruitment of both RFWD3 and PRIMPOL to stalled forks. In the absence of SLFN11, fork restart proceeds via RFWD3 and PRIMPOL to facilitate gapped DNA synthesis. SLFN11's suppression of RFWD3/PRIMPOL recruitment requires a functional ATPase domain and persistent fork localization, but not tRNA hydrolysis or ssDNA binding. | PMID:41372167 | Nature communications |

## Citations

- PMID:20173098
- PMID:21504906
- PMID:21558276
- PMID:26474068
- PMID:28575657
- PMID:28575658
- PMID:28691929
- PMID:30530694
- PMID:31900333
- PMID:32391871
- PMID:33044890
- PMID:33321094
- PMID:35905994
- PMID:37036693
- PMID:40940676
- PMID:41117130
- PMID:41372167
