---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/XRCC2
affinage_run_date: 2026-06-11T09:02:06
uniprot_accession: O43543
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 29
citation_count: 29
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for XRCC2 (human)

## Current model (mechanistic narrative)

XRCC2 is a RecA/RAD51-family recombination-repair protein that is essential for homologous recombination (HR) repair of DNA double-strand breaks and for genome stability, with its loss causing >100-fold reduction in HR while leaving non-homologous end joining intact [PMID:9628903, PMID:9660962, PMID:10517641]. It functions as a stable subunit of the multimeric RAD51 paralog complexes: it forms a direct, ATPase-active complex with RAD51D [PMID:10871607] and is a component of the BCDX2 heterotetramer (RAD51B-RAD51C-RAD51D-XRCC2) that preferentially binds branched DNA and catalyzes strand annealing [PMID:15141025]. Cryo-EM resolves how these complexes act on RAD51 filaments: within BCDX2 the RAD51C-RAD51D-XRCC2 module mimics three RAD51 protomers to stimulate ATP-hydrolysis-dependent filament nucleation and extension on ssDNA, whereas the XRCC3-containing complex (XRCC3-RAD51C-RAD51D-XRCC2) caps 5' filament termini to promote homologous pairing [PMID:37344587, PMID:41196948]. Mechanistically, XRCC2 is required for damage-induced RAD51 focus formation and chromatin loading without itself requiring ATP binding, distinguishing its role from the ATP-dependent activity of XRCC3 [PMID:11301337, PMID:12488590, PMID:19470754]. Beyond canonical HR, XRCC2 acts late in the Fanconi anemia pathway downstream of FANCD2 monoubiquitination (designated FANCU) [PMID:27208205], restrains replication fork progression during dNTP imbalance through ATR-mediated phosphorylation at Ser247 [PMID:30566856], and is essential for mammalian meiotic recombination [PMID:30042186]. Biallelic XRCC2 mutation causes a Fanconi anemia phenotype [PMID:27208205], and a homozygous p.Leu14Pro mutation causes meiotic arrest and infertility in humans [PMID:30042186]. At the organismal level, Xrcc2 loss produces p53-dependent apoptosis of post-mitotic neurons and embryonic lethality [PMID:11118202, PMID:17116431].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0003677 DNA binding, GO:0140657 ATP-dependent activity, GO:0098772 molecular function regulator activity, GO:0140096 catalytic activity, acting on a protein
- **localization:** GO:0005634 nucleus, GO:0005694 chromosome
- **pathway (Reactome):** R-HSA-73894 DNA Repair, R-HSA-69306 DNA Replication, R-HSA-1474165 Reproduction, R-HSA-1640170 Cell Cycle
- **partners:** RAD51D, RAD51C, RAD51B, RAD51, XRCC3
- **complexes:** BCDX2 (RAD51B-RAD51C-RAD51D-XRCC2), XRCC3-RAD51C-RAD51D-XRCC2 complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1998 | High | XRCC2 is a member of the RecA/RAD51 family of recombination-repair proteins; the human XRCC2 cDNA complements the DNA cross-linking agent sensitivity and genetic instability of the hamster irs1 mutant cell line, establishing its role in recombinational repair. | PMID:9628903, PMID:9660962 | Nucleic acids research |
| 1998 | Medium | XRCC3, but not XRCC2, was shown to interact directly with HsRAD51 by direct interaction assay; XRCC2 and XRCC3 are RAD51-related proteins promoting chromosome stability and protecting against DNA cross-links. | PMID:9660962 | Molecular cell |
| 1999 | High | XRCC2 is essential for efficient repair of DNA double-strand breaks by homologous recombination between sister chromatids; XRCC2-deficient hamster cells show >100-fold decrease in HR induced by DSBs, while NHEJ remains normal, and this defect is rescued by transient XRCC2 expression. | PMID:10517641 | Nature |
| 2000 | High | XRCC2 deficiency leads to significant increases in chromosome missegregation and centrosome fragmentation during mitosis, not due to loss of the spindle checkpoint, but linked to unresolved DNA damage. | PMID:11025669 | Nature cell biology |
| 2000 | High | Xrcc2 knockout in mice causes embryonic lethality from mid-gestation, with high-frequency apoptotic death of post-mitotic neurons in the developing brain and chromosomal aberrations in embryonic cells, demonstrating a role for homologous recombination in endogenous damage repair during development. | PMID:11118202 | The EMBO journal |
| 2000 | High | RAD51L3 (RAD51D) possesses single-stranded DNA binding activity and DNA-stimulated ATPase activity, and forms a direct protein complex with XRCC2 in human cells, as demonstrated with purified proteins. | PMID:10871607 | The Journal of biological chemistry |
| 2001 | High | Ablation of XRCC2 in chicken DT40 B cells shifts immunoglobulin V gene diversification from gene conversion (templated) to somatic hypermutation (non-templated), demonstrating XRCC2's role in channeling recombination intermediates toward template-dependent repair. | PMID:11528482 | Nature |
| 2001 | High | XRCC2 localizes to the nucleus (as a GFP fusion), and is required for damage-dependent RAD51 focus formation; XRCC2 mutants with inactivated ATP-binding P-loop motifs still complement XRCC2-deficient irs1 cells, indicating XRCC2 promotes RAD51-dependent recombination repair without requiring ATP binding. | PMID:11301337 | The Journal of biological chemistry |
| 2002 | High | The purified XRCC2·RAD51D (Xrcc2·Rad51D) complex catalyzes homologous pairing between ssDNA and dsDNA in vitro, forms multimeric ring structures in the absence of DNA, and forms filamentous structures on ssDNA, similar to RAD51, RAD52, and XRCC3·RAD51C. | PMID:11834724 | The Journal of biological chemistry |
| 2002 | Medium | XRCC2 is required for the formation of RAD51 foci after both ionizing radiation and mitomycin C treatment; irs1 cells lacking XRCC2 fail to form early (type 1) and late (type 2) RAD51 foci despite normal RAD51 protein levels, and XRCC2 complementation restores focus formation. | PMID:12488590 | Journal of biomedicine & biotechnology |
| 2002 | Medium | Non-conservative substitution or deletion of amino acid 188 of XRCC2 significantly affects cellular sensitivity to DNA damage; the R188H polymorphic variant (present in 6% of chromosomes) has a weak effect on damage sensitivity. | PMID:12023985 | Human molecular genetics |
| 2003 | High | Xrcc2−/− mouse embryonic fibroblasts exhibit order-of-magnitude higher chromosomal alterations including aneuploidy and complex exchanges, a 30-fold reduction in gene conversion, and reduced RAD51 focus formation and SCE; these phenotypes resemble Brca disruptions and confirm XRCC2 as a non-redundant HR component. | PMID:14678973 | Cancer research |
| 2003 | Medium | A tumour-derived XRCC2 mutant allele (342delT) dominantly suppresses HR at stalled replication forks but not at two-ended DSBs, suggesting that XRCC2 participates in at least two mechanistically distinguishable sub-pathways of HR: replication fork-associated and DSB-associated. | PMID:14645207 | Human molecular genetics |
| 2004 | High | The BCDX2 complex (RAD51B-RAD51C-RAD51D-XRCC2) preferentially binds branched DNA structures (Y-shaped DNA and Holliday junctions) over linear or nicked duplexes, and catalyzes strand-annealing between long complementary ssDNA molecules. | PMID:15141025 | Nucleic acids research |
| 2005 | Medium | XRCC2 is required for RAD51 focus formation and chromatin association after hydroxyurea (HU)-induced replication arrest, but not after thymidine-induced arrest, indicating at least two XRCC2-dependent and -independent sub-pathways for repair at stalled replication forks. | PMID:15861395 | Journal of cellular biochemistry |
| 2006 | Medium | The naturally occurring R188H polymorphic variant of XRCC2 confers increased resistance to cisplatin-induced DNA damage compared to wild-type XRCC2, as assayed in chicken DT40 XRCC2-knockout cells complemented with human wild-type or R188H cDNAs. | PMID:17141189 | Biochemical and biophysical research communications |
| 2006 | High | Excessive apoptosis in Xrcc2−/− embryos is p53-dependent; loss of p53 restores growth capacity to Xrcc2−/− fibroblasts but cannot rescue embryonic lethality. Loss of ATM in an Xrcc2−/− background has little effect, indicating that the embryonic response to HR loss is not mediated through ATM. | PMID:17116431 | DNA repair |
| 2008 | High | HR (via XRCC2 and BRCA2) but not NHEJ protects against O6-methylguanine-triggered apoptosis, DSBs, and chromosomal aberrations; cells defective in XRCC2 are hypersensitive to temozolomide/MNNG-induced cell death and show persistent γH2AX foci, while NHEJ mutants (Ku80, DNA-PKcs) are not hypersensitive. | PMID:18840549 | DNA repair |
| 2008 | Medium | Transcription-associated recombination (TAR) depends on BRCA2 but is independent of XRCC2; XRCC2-deficient irs1 cells are also proficient in recombination induced at slowed replication forks, linking TAR mechanistically to fork-associated recombination rather than DSB repair. | PMID:19043071 | Nucleic acids research |
| 2009 | High | XRCC2 deficiency biases sister chromatid recombination toward long-tract gene conversion (LTGC); this defect is corrected by wild-type XRCC2 and by XRCC2 mutants defective in ATP binding and hydrolysis, whereas XRCC3-mediated suppression of LTGC requires ATP binding/hydrolysis. | PMID:19470754 | Molecular and cellular biology |
| 2010 | Medium | XRCC2 is important but not essential for the accumulation of RAD51 at DNA damage sites; XRCC2 colocalizes with RAD51 at damage sites; protein truncations of XRCC2 destroy its function; XRCC2 and RAD51L3 (RAD51D) interact with RAD51 in yeast two-hybrid assay. | PMID:20189471 | DNA repair |
| 2015 | Medium | ZNF281 transcriptionally activates XRCC2 expression through direct DNA binding to its promoter; ZNF281 silencing delays DNA repair after etoposide treatment; c-Myc binds the XRCC2 promoter but cannot activate its transcription or modify ZNF281 activity. | PMID:26300006 | Oncogene |
| 2016 | High | XRCC2 is a Fanconi anemia gene (FANCU); wild-type XRCC2 corrects increased MMC sensitivity, chromosome breakage, and G2-M accumulation in FA patient cells with biallelic XRCC2 mutation; XRCC2 acts late in the FA-BRCA pathway (downstream of FANCD2 monoubiquitination, which is normal in XRCC2-deficient cells); the patient's XRCC2 p.R215X mutant is unstable and reduces levels of other BCDX2 complex proteins. | PMID:27208205 | Journal of medical genetics |
| 2018 | High | XRCC2 (FANCU) and its binding partner RAD51D restrain active DNA synthesis during dNTP alterations independently of HDR; XRCC2 absence is associated with elevated RRM2 levels and high nucleotide pools, causing unrestrained fork progression and DNA damage accumulation; this function is regulated by ATR-mediated phosphorylation of XRCC2 at Ser247. | PMID:30566856 | Cell reports |
| 2018 | High | A homozygous XRCC2 missense mutation (c.41T>C/p.Leu14Pro) causes meiotic arrest, azoospermia, and infertility in humans; knockin mice with the equivalent mutation survive but exhibit meiotic arrest, azoospermia, premature ovarian failure, and infertility, establishing XRCC2 as essential for mammalian meiotic HR. | PMID:30042186 | Journal of medical genetics |
| 2019 | High | RAD51D cancer-associated mutations G96C and G107V (near/within the Walker A motif) disrupt RAD51D interaction with XRCC2 in yeast two-hybrid and Co-IP, and abolish DSB repair in a sister chromatid recombination reporter, demonstrating that the RAD51D–XRCC2 interaction is required for homologous recombination. | PMID:30836272 | DNA repair |
| 2023 | High | Cryo-EM and AlphaFold2 structural analysis of the BCDX2 complex reveals that RAD51C-RAD51D-XRCC2 mimics three RAD51 protomers aligned within a nucleoprotein filament while RAD51B is highly dynamic; biochemical and single-molecule assays show BCDX2 stimulates nucleation and extension of RAD51 filaments on ssDNA in reactions dependent on coupled ATPase activities of RAD51B and RAD51C. | PMID:37344587 | Nature |
| 2026 | High | Cryo-EM reveals two distinct heterotetrameric RAD51 paralog complexes: the RAD51B complex (RAD51B-RAD51C-RAD51D-XRCC2) promotes dynamic ATP hydrolysis-dependent RAD51 filament assembly, while the XRCC3 complex (XRCC3-RAD51C-RAD51D-XRCC2) stably caps the 5' termini of RAD51 filaments to promote homologous pairing. | PMID:41196948 | Science (New York, N.Y.) |
| 2024 | Medium | c-Myc acts as a transcriptional activator of XRCC2 in NSCLC, as shown by ChIP and luciferase reporter assays; XRCC2 augments NSCLC cell proliferation through down-regulation of FOS expression; XRCC2 knockdown impairs proliferation in vitro and in vivo. | PMID:39153434 | Biomedicine & pharmacotherapy |

## Citations

- PMID:10517641
- PMID:10871607
- PMID:11025669
- PMID:11118202
- PMID:11301337
- PMID:11528482
- PMID:11834724
- PMID:12023985
- PMID:12488590
- PMID:14645207
- PMID:14678973
- PMID:15141025
- PMID:15861395
- PMID:17116431
- PMID:17141189
- PMID:18840549
- PMID:19043071
- PMID:19470754
- PMID:20189471
- PMID:26300006
- PMID:27208205
- PMID:30042186
- PMID:30566856
- PMID:30836272
- PMID:37344587
- PMID:39153434
- PMID:41196948
- PMID:9628903
- PMID:9660962
