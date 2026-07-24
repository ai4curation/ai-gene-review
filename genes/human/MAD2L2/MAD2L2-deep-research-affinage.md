---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/MAD2L2
affinage_run_date: 2026-06-10T02:59:50
uniprot_accession: Q9UI95
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 47
citation_count: 47
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for MAD2L2 (human)

## Current model (mechanistic narrative)

MAD2L2 (REV7/MAD2B/FANCV) is a HORMA-domain adaptor that uses a multivalent 'safety-belt' surface to bind structurally diverse partners and thereby coordinates DNA damage tolerance, double-strand break (DSB) repair pathway choice, and mitotic cell-cycle control [PMID:20164194, PMID:28887307, PMID:31484720]. In translesion synthesis, REV7 is the non-catalytic subunit of DNA polymerase zeta, binding the catalytic subunit REV3L through two short sequence motifs and recruiting REV1 via a distinct interface, with REV7 dimerization tethered by the two REV3 motifs being required for assembly of a functional REV1/pol zeta complex [PMID:20164194, PMID:22859296, PMID:25567983, PMID:30111544]; this activity underlies damage-induced mutagenesis and resistance to UV and crosslinking agents [PMID:3897794, PMID:25567983], and a point mutation (C70R) that severs the REV7–REV3 interaction abolishes damage tolerance and causes germ-cell loss and infertility [PMID:24356953]. REV7 is the central subunit of the shieldin complex (with SHLD1, SHLD2/FAM35A, SHLD3), which is recruited to DSBs and telomeres through the H4K20me2–53BP1–RIF1 axis and inhibits 5' end resection to enforce NHEJ over homologous recombination; its loss restores resection in BRCA1-deficient cells and causes PARP-inhibitor resistance [PMID:25799992, PMID:25799990, PMID:30046110, PMID:30154076, PMID:29160738]. Shieldin assembly depends on SHLD2-driven REV7 dimerization and on REV7's C-terminal wrapping around SHLD3, and is reversed by TRIP13-catalyzed closed-to-open conformational switching together with p31comet, which also disassembles the REV7–REV3 complex; competing seatbelt ligands such as CHAMP1 likewise tune this balance [PMID:31796627, PMID:31915374, PMID:33051298, PMID:34521823, PMID:36044844]. Independently of shieldin, REV7 protects and restarts stalled replication forks in a REV3L/REV1-dependent manner by limiting MRE11 resection [PMID:36075897]. In mitotic control, MAD2L2 inhibits both CDH1-APC and CDC20-APC by binding the activators rather than the core APC [PMID:11459826, PMID:11459825], and biallelic inactivating REV7 mutations cause Fanconi anemia (REV7 = FANCV) [PMID:27500492].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity, GO:0003677 DNA binding
- **localization:** GO:0005634 nucleus, GO:0000228 nuclear chromosome
- **pathway (Reactome):** R-HSA-73894 DNA Repair, R-HSA-69306 DNA Replication, R-HSA-1640170 Cell Cycle, R-HSA-1643685 Disease
- **partners:** REV3L, REV1, SHLD3, SHLD2, TRIP13, RAN, CHAMP1, 53BP1
- **complexes:** DNA polymerase zeta (REV3L-REV7), shieldin (REV7-SHLD1-SHLD2-SHLD3), REV1/pol zeta TLS complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1985 | High | REV7 (yeast ortholog) is required for UV-induced mutagenesis in Saccharomyces cerevisiae and belongs to the RAD6 epistasis group for UV survival, establishing its role in damage-induced mutagenesis. | PMID:3897794 | Molecular & general genetics |
| 1994 | Medium | Yeast REV7 gene was cloned and sequenced; its function is required for DNA damage-induced mutagenesis but is not essential for viability. | PMID:7871890 | Yeast |
| 1999 | Medium | Human MAD2B (MAD2L2) gene was isolated and characterized as homologous to the spindle checkpoint gene MAD2 (MAD2L1); chromosomal localization was determined (chromosome 1p36). | PMID:10366450 | Genomics |
| 2000 | Medium | Human REV7 (hREV7) interacts with hREV3 (catalytic subunit of DNA polymerase zeta) and with hMAD2 (but not hMAD1), establishing hREV7 as a component of the human pol zeta complex; interaction domains between hREV3 and hREV7 were determined. | PMID:10660610 | The Journal of biological chemistry |
| 2001 | High | MAD2B (MAD2L2) inhibits both CDH1-APC and CDC20-APC (anaphase-promoting complex) by targeting CDH1 and CDC20 directly, not APC itself; unlike MAD2, MAD2B does not interact with MAD1, indicating it relays a distinct cellular signal. | PMID:11459826 | Genes & development |
| 2001 | High | MAD2L2 specifically binds and inhibits CDH1-APC (but not CDC20-APC in contrast to MAD2); proposed mechanism is inhibition of substrate release from APC, paralleling MAD2's effect on CDC20. | PMID:11459825 | Genes & development |
| 2001 | Medium | MAD2B interacts with PRCC (papillary renal cell carcinoma protein); the PRCCTFE3 fusion protein retains the MAD2B interaction domain but this interaction is impaired, leading to mitotic checkpoint defects in t(X;1)-positive RCCs. | PMID:11717438 | Proceedings of the National Academy of Sciences |
| 2003 | Medium | Human REV1 and REV7 proteins form a stable heterodimer in solution; however, human REV7 does not influence the stability, substrate specificity, or kinetic parameters of REV1's transferase activity (negative finding for functional stimulation in humans, contrasting with yeast Rev7 stimulating Rev3). | PMID:12529368 | The Journal of biological chemistry |
| 2005 | Medium | In yeast, Rev1 forms a stable complex with Rev7 that copurifies; the polymerase-associated domain (PAD) of Rev1 mediates its binding to Rev7, revealing a novel protein-protein interaction role for the PAD. | PMID:16227619 | Molecular and cellular biology |
| 2007 | Medium | Human Rev7/MAD2B interacts with the transcription factor Elk-1 and promotes Elk-1 phosphorylation by JNK MAP kinases, thereby upregulating Elk-1 target gene expression (e.g., egr-1) following DNA damage. | PMID:17296730 | Molecular and cellular biology |
| 2007 | High | The Shigella effector IpaB binds directly to Mad2L2 and causes unscheduled APC activation (by neutralizing Mad2L2's APC-inhibitory function), leading to G2/M cell cycle arrest dependent on IpaB/Mad2L2 interaction, which promotes bacterial colonization. | PMID:17719540 | Cell |
| 2009 | Medium | MAD2B interacts with the small GTPase RAN throughout the cell cycle; during mitosis, they co-localize at the spindle; the interaction domain of RAN maps to a C-terminal 60 amino acid moiety, and MAD2B must be full-length. | PMID:19753112 | PloS one |
| 2009 | Medium | MAD2B interacts with TCF4; this interaction abolishes TCF4's DNA-binding ability and blocks TCF4-mediated transactivation; MAD2B knockdown leads to epithelial-mesenchymal transdifferentiation by de-repressing TCF4-mediated Slug expression. | PMID:19443654 | The Journal of biological chemistry |
| 2010 | High | Crystal structure of human REV7 in complex with a REV3 fragment (residues 1847-1898) was solved; the structure reveals the mechanism of REV7-REV3 interaction and shows that the REV7-REV3 interface creates a structural platform for REV1 binding, defining REV7 as an adaptor protein recruiting pol zeta to lesion sites. | PMID:20164194 | The Journal of biological chemistry |
| 2010 | Medium | Defined short sequence motifs in REV3 are necessary and sufficient for REV7 binding; MAD2 (MAD2L1) also binds the REV7-binding sequence in REV3, but REV7 does not bind the MAD2-binding sequences in MAD1 or CDC20, establishing distinct but overlapping short motif recognition between REV7 and MAD2. | PMID:20088965 | Genes to cells |
| 2010 | Medium | MAD2B interacts with clathrin light chain A (CLTA) during G2/M phase and co-localizes with CLTA at the mitotic spindle; MAD2B depletion causes CLTA redistribution away from the spindle and increased chromosome misalignment. | PMID:21152103 | PloS one |
| 2012 | High | Crystal structure of the ternary complex of human REV1 C-terminal domain, REV7, and a REV3 fragment was solved; the REV1 CTD uses a four-helix bundle to interact with REV7 via a conserved mammalian linker region, using a distinct interface from other TLS polymerase binding sites, providing the structural basis for pol zeta recruitment and polymerase switching. | PMID:22859296 | The Journal of biological chemistry |
| 2012 | High | NMR spectroscopy demonstrates that the Rev1 C-terminal domain uses independent interaction interfaces to simultaneously bind pol eta and REV7 (subunit of pol zeta), enabling Rev1 to serve as a scaffold accommodating multiple polymerases for TLS. | PMID:22828282 | FEBS letters |
| 2012 | Medium | REV7 is required for APC/C-mediated polyubiquitination and proteasomal degradation of REV1; REV7 depletion stabilizes REV1 by preventing its polyubiquitination, while REV7 overexpression augments REV1 degradation; the N-terminal region of REV1 contains both the APC degron and an additional REV7-binding domain. | PMID:23287467 | Cell cycle |
| 2013 | High | A missense mutation (C70R) in Rev7 disrupts its interaction with REV3 (catalytic subunit of pol zeta), causing infertility, primordial germ cell loss, increased apoptosis, S-phase arrest with DNA damage accumulation after mitomycin C; Rev7 C70R does not affect the mitotic spindle assembly checkpoint. | PMID:24356953 | The Journal of biological chemistry |
| 2013 | High | Mad2l2 is essential for primordial germ cell (PGC) maintenance in mice; Mad2l2-/- PGCs fail to arrest in G2 phase and fail to transition from H3K9me2 to H3K27me3 chromatin configuration; Mad2l2 interacts with histone methyltransferases G9a and GLP (downregulating H3K9me2) and inhibits Cdk1 (causing G2 arrest), which allows Ezh2 to upregulate H3K27me3. | PMID:24009519 | PLoS genetics |
| 2013 | High | REV7 is essential for primordial germ cell (PGC) maintenance and fertility in mice; Rev7-/- mice show progressive PGC loss during migration with increased apoptosis; DNA damage accumulation and increased histone methylation were detected in Rev7-/- embryos; REV7 is required for prevention of apoptotic cell death in PGCs. | PMID:23463509 | The Journal of biological chemistry |
| 2015 | High | REV7 (MAD2L2) loss in mouse and human cells re-establishes CTIP-dependent end resection of DSBs in BRCA1-deficient cells, restoring homologous recombination and causing PARP inhibitor resistance; REV7 is recruited to DSBs via the H2AX-MDC1-RNF8-RNF168-53BP1 chromatin pathway; REV7 promotes NHEJ by blocking HR and end resection downstream of 53BP1; ATM inhibition reverses PARPi resistance caused by REV7 loss. | PMID:25799992 | Nature |
| 2015 | High | MAD2L2 accumulates at uncapped telomeres and promotes NHEJ-mediated chromosome end fusion; MAD2L2 inhibits 5' end resection at DSBs and telomeres; its activity depends on ATM, RNF8, RNF168, 53BP1, and RIF1 but not PTIP, REV1, or REV3; MAD2L2 controls DSB repair independently of its TLS role. | PMID:25799990 | Nature |
| 2015 | High | REV7 is essential for DNA damage tolerance via its interaction with two distinct REV7-binding sites in mammalian REV3L (residues 1877-1887 and 1993-2003); mutation of both binding sites eliminates REV3L-REV7 interaction and fails to prevent spontaneous chromosome breaks or confer UV and cisplatin resistance. | PMID:25567983 | Nucleic acids research |
| 2015 | Medium | Rev7/Mad2B is required for functional mitotic spindle assembly; Rev7-depleted cells accumulate monoastral and abnormal spindles with misaligned chromosomes; Rev7 physically interacts with RAN and this interaction may mediate spindle organization; Rev7 depletion does not compromise spindle assembly checkpoint activity. | PMID:26697843 | Cell cycle |
| 2016 | High | Biallelic inactivating mutations in REV7 (FANCV) cause Fanconi anemia; patient-derived cells show increased chromosome breaks and G2/M accumulation upon crosslinking agents, γH2AX and 53BP1 foci; WT REV7 expression rescues normal phenotypes; CRISPR/Cas9 inactivation of REV7 in non-FA cells produces FA phenotype; REV7 is thereby identified as FANCV. | PMID:27500492 | The Journal of clinical investigation |
| 2017 | High | Crystal structures of MAD2L2 in complex with CAMP (chromosome alignment-maintaining phosphoprotein) fragments reveal that CAMP's 'WK' motif mediates binding to MAD2L2; the MAD2L2-CAMP interaction creates a distinct interface compared to REV3 binding; one crystal form shows a dimeric MAD2L2-CAMP structure with C-terminal domain swapping, providing evidence for the dynamic nature of MAD2L2 structure. | PMID:28887307 | The Journal of biological chemistry |
| 2017 | Medium | REV7 undergoes ubiquitin/proteasome-mediated degradation upon UV irradiation; the N-terminal destruction box of REV7 acts as the degron; Cul4A/B are the putative E3 ubiquitin ligases; HR23B physically interacts with and colocalizes with REV7 in nuclear foci post-UV and protects REV7 from accelerated degradation; degradation is NER-pathway dependent (observed with UV and 4-NQO but not cisplatin). | PMID:28440919 | The FEBS journal |
| 2018 | Medium | MAD2L2 (REV7) inhibits NCOA3 through a mechanism requiring p38 activation, which phosphorylates NCOA3 leading to its ubiquitination and proteasomal degradation; MAD2L2 was identified as an NCOA3 interaction partner by IP-MS. | PMID:29360267 | Molecular oncology |
| 2018 | High | 53BP1 cooperates with REV7 to promote NHEJ during class-switch recombination (CSR) but REV7 is not required for 53BP1-dependent V(D)J recombination; shieldin (comprising REV7, SHLD1/c20orf196, SHLD2/FAM35A, SHLD3/FLJ26957) was identified as a four-subunit complex essential for REV7-dependent DNA end protection and NHEJ in CSR but dispensable for REV7-dependent ICL repair. | PMID:30046110 | Nature |
| 2018 | High | SHLD2 (FAM35A) is a REV7 interactor identified by MS-based proteomics; FAM35A accumulates at DSBs in a 53BP1-, RIF1-, and REV7-dependent manner; FAM35A, REV7, and SHLD1 form a complex promoting NHEJ and limiting HR by antagonizing DNA end resection. | PMID:30154076 | The EMBO journal |
| 2018 | Medium | FAM35A (SHLD2) associates with REV7/RIF1/53BP1; FAM35A knockdown causes sensitivity to DNA-damaging agents; in BRCA1-mutant cells, FAM35A depletion increases resistance to camptothecin by allowing more efficient DNA end processing. | PMID:29789392 | The EMBO journal |
| 2018 | Medium | H4K20 dimethylation (H4K20me2) recruits the 53BP1-RIF1-MAD2L2 complex to DSBs; replication-associated 2-fold dilution of H4K20me2 promotes release of this complex and favors BRCA1 access; MAD2L2, like 53BP1 and RIF1, suppresses DSB accumulation of BRCA1. | PMID:29160738 | Cell cycle |
| 2018 | High | Rev7 dimerization is required for assembly and function of the Rev1/pol zeta TLS complex; Rev7 forms homodimers when tethered by the two RBMs of Rev3 and heterodimerizes with Mad2 and p31comet via the canonical HORMA dimerization interface; the Rev7 dimer binds only one copy of Rev1; mutation of the Rev7 dimer interface increases cellular sensitivity to DNA damage. | PMID:30111544 | Proceedings of the National Academy of Sciences |
| 2018 | Medium | Rev7 and 53BP1/Crb2 specifically repress long-range DSB resection through the RecQ helicase-dependent pathway (not Exo1), preventing hyper-resection in S. pombe; this mechanism is linked to PARPi resistance in BRCA1-deficient cells. | PMID:29697047 | eLife |
| 2019 | High | Crystal structures of REV7 in complex with RAN and IpaB fragments were solved; both RAN and IpaB bind the 'safety belt' region of REV7 causing rearrangement of the C-terminal beta-sheet; REV7 preferentially binds GTP-bound RAN, suggesting the RAN GTP/GDP switch regulates REV7 activity in cell cycle control. | PMID:31484720 | The Journal of biological chemistry |
| 2019 | High | Crystal structures of REV7 in complex with SHLD3's REV7-binding domain (RBD) were solved at 2.2-2.3 Å; SHLD3 uses an N-terminal loop and C-terminal alpha-helix for REV7 binding; the REV7 'safety belt' region retards RBD dissociation (low-nanomolar affinity); both structural elements are indispensable for high-affinity binding. | PMID:31796627 | The Journal of biological chemistry |
| 2020 | High | TRIP13 ATPase catalyzes the conversion of REV7 from an active 'closed' conformation to an inactive 'open' conformation, dissociating REV7-Shieldin to promote HDR; TRIP13 similarly disassembles the REV7-REV3 TLS complex, inhibiting error-prone TLS; TRIP13 overexpression confers PARPi resistance in BRCA1-deficient cancers. | PMID:31915374 | Nature cell biology |
| 2020 | Medium | p31comet binds the REV7-Shieldin complex, promotes REV7 inactivation (via TRIP13), causes dissociation from SHLD3, and promotes DNA end resection and PARPi resistance; p31comet also releases REV7 from REV3 in pol zeta, counteracting TLS. | PMID:33051298 | Proceedings of the National Academy of Sciences |
| 2020 | High | REV7 is required for B cell survival upon AID-deamination independently of its roles in DSBR, G2/M transition, or REV1-mediated TLS; REV7-dependent TLS across UNG-processed apurinic/apyrimidinic (AP) sites is required for cell survival upon AID/APOBEC deamination. | PMID:32499490 | Nature communications |
| 2021 | High | MAD2L2 dimerization (mediated by SHLD2) accelerates MAD2L2-SHLD3 interaction and is required for shieldin complex assembly and NHEJ function; MAD2L2 wraps its C-terminus around SHLD3 creating a stable complex; appropriate TRIP13 levels are important for proper shieldin (dis)assembly. | PMID:34521823 | Nature communications |
| 2022 | Medium | CHAMP1 binds directly to REV7 via the REV7 seatbelt/C-terminal domain (competing with SHLD3), reduces shieldin complex levels, increases DSB end resection, and activates HR repair; CHAMP1 also interacts with POGZ in a heterochromatin complex promoting HR; CHAMP1 overexpression confers PARPi resistance. | PMID:36044844 | Cell reports |
| 2022 | High | MAD2L2 promotes replication fork protection and restart independently of shieldin; MAD2L2 loss leads to uncontrolled MRE11-dependent resection of stalled forks and ssDNA accumulation; fork protection by MAD2L2 requires REV3L and REV1 (TLS partners) but not shieldin subunits. | PMID:36075897 | Nature communications |
| 2022 | Medium | CDH1 interacts with MAD2L2 using the same C-terminal residues that REV1 uses (Rev1-like binding pattern); MAD2L2's C-terminus interface is essential for both CDH1-MAD2L2 binding and MAD2L2 homodimerization. | PMID:32811646 | Biochemical and biophysical research communications |
| 2024 | Medium | REV7 binds directly to p53 and blocks ATM-dependent p53 Ser15 phosphorylation; REV7 is also involved in p53 destabilization, revealing a novel function of REV7 in DSB-induced p53 signaling. | PMID:38557443 | Cell cycle |
| 2024 | Medium | AURKB interacts with and modulates expression of MAD2L2 in bladder cancer cells; AURKB knockdown effects (suppression of proliferation/migration, cell cycle arrest, senescence) are rescued by MAD2L2 overexpression, placing MAD2L2 downstream of AURKB in a DDR pathway affecting p53. | PMID:38515112 | Journal of translational medicine |

## Citations

- PMID:10366450
- PMID:10660610
- PMID:11459825
- PMID:11459826
- PMID:11717438
- PMID:12529368
- PMID:16227619
- PMID:17296730
- PMID:17719540
- PMID:19443654
- PMID:19753112
- PMID:20088965
- PMID:20164194
- PMID:21152103
- PMID:22828282
- PMID:22859296
- PMID:23287467
- PMID:23463509
- PMID:24009519
- PMID:24356953
- PMID:25567983
- PMID:25799990
- PMID:25799992
- PMID:26697843
- PMID:27500492
- PMID:28440919
- PMID:28887307
- PMID:29160738
- PMID:29360267
- PMID:29697047
- PMID:29789392
- PMID:30046110
- PMID:30111544
- PMID:30154076
- PMID:31484720
- PMID:31796627
- PMID:31915374
- PMID:32499490
- PMID:32811646
- PMID:33051298
- PMID:34521823
- PMID:36044844
- PMID:36075897
- PMID:38515112
- PMID:38557443
- PMID:3897794
- PMID:7871890
