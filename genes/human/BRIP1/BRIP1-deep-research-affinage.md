---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/BRIP1
affinage_run_date: 2026-06-09T22:02:45
uniprot_accession: Q9BX63
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 38
citation_count: 40
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for BRIP1 (human)

## Current model (mechanistic narrative)

BRIP1 (BACH1/FANCJ) is a 5′-to-3′ DEAH-box ATP-dependent DNA helicase that maintains genome stability during DNA replication and repair, and its loss defines Fanconi anemia complementation group J [PMID:16153896, PMID:16116423, PMID:16116424, PMID:16116421]. Catalytic activity depends on an N-terminal iron–sulfur cluster coordinated by three conserved cysteines—mutated in Fanconi anemia and cancer—and on Q-motif (Q25)-dependent dimerization, with the dimer showing enhanced ATPase, helicase, and DNA-binding activity [PMID:16973432, PMID:22582397, PMID:32542039]. The enzyme unwinds duplex DNA, dissociates G-quadruplex (G4) structures, disrupts triplex DNA and protein–DNA complexes, and inhibits RAD51 strand exchange, contacting both translocating and non-translocating strands during unwinding [PMID:18426915, PMID:18978354, PMID:19150983, PMID:17145708]. A central physiological role is resolving G4 obstacles during replication: FANCJ counteracts fork stalling at G4 structures—a function it performs in cell-free Xenopus extracts independently of the canonical FA pathway—and engages G4s through a dedicated AKKQ recognition motif that also mediates MLH1 binding, while a PIP-like region recruits REV1 to assemble a G4 repair complex [PMID:23530069, PMID:25193968, PMID:27342280, PMID:31861576]. FANCJ operates in interstrand crosslink repair downstream of FANCD2 monoubiquitination, where its helicase activity and direct MLH1 (MutLα) interaction—rather than its BRCA1 interaction—are required to correct ICL sensitivity [PMID:16116421, PMID:17581638]. FANCJ directly binds and stabilizes FANCD2/FANCI and is reciprocally required for FANCD2 chromatin loading and focus formation [PMID:25070891, PMID:26336824, PMID:20676667]. In homologous recombination, CDK-dependent S990 phosphorylation drives both BRCA1 interaction and K1249 acetylation, the latter recruiting CtIP to promote DNA end resection [PMID:32251466, PMID:22792074]. FANCJ couples to checkpoint and replication-stress responses via phospho-Thr1133-dependent binding to the TopBP1 BRCT7/8 domains, supporting ATR signaling and RPA chromatin loading, and cooperates with RPA on damaged and G4 substrates [PMID:20159562, PMID:21127055, PMID:17596542]. Genetically, FANCJ helicase function suppresses spontaneous and replication-stress-induced microsatellite instability independently of FANCD2, with Fancj-null mice predisposed to lymphoma [PMID:26637282, PMID:27179029]. Beyond replication and repair, FANCJ unfolds protein adducts in DNA–protein crosslink repair to enable SPRTN cleavage and translesion synthesis [PMID:36608669], and contributes to S-phase PARP1 activity through its MLH1 interaction, explaining its requirement for PARP inhibitor efficacy in BRCA1-deficient cells [PMID:38521768].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0140657 ATP-dependent activity, GO:0140097 catalytic activity, acting on DNA, GO:0003677 DNA binding, GO:0016787 hydrolase activity, GO:0060090 molecular adaptor activity
- **localization:** GO:0005634 nucleus, GO:0000228 nuclear chromosome
- **pathway (Reactome):** R-HSA-73894 DNA Repair, R-HSA-69306 DNA Replication, R-HSA-8953897 Cellular responses to stimuli
- **partners:** BRCA1, MLH1, FANCD2, RPA1, TOPBP1, CTIP, REV1, FANCI
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2005 | High | BRIP1/BACH1 (FANCJ) is a DEAH-box DNA helicase that physically interacts with the BRCT domain of BRCA1 and is defective in Fanconi anemia complementation group J (FA-J); mutation of BACH1 in an FA-J patient-derived cell line was confirmed by western blot, and re-expression of wild-type BACH1 reduced the G2/M accumulation characteristic of FA cells after crosslinker treatment, establishing BACH1 as FANCJ. | PMID:16153896, PMID:16116423, PMID:16116424 | Cancer cell |
| 2005 | High | BRIP1 helicase function in the Fanconi anemia pathway is independent of its interaction with BRCA1: chicken DT40 brip1 knockout cells are proficient for FANCD2 ubiquitination but hypersensitive to cisplatin and arrested in late S-G2; expression of human BRIP1 lacking the BRCT-interaction domain rescued these defects, placing BRIP1 downstream of FANCD2 activation in the FA pathway. | PMID:16116421 | Nature genetics |
| 2006 | High | FANCJ (and the related helicase XPD/Rad3) contain a conserved iron-sulfur (Fe-S) cluster domain near the N-terminus coordinated by three absolutely conserved cysteines; the Fe-S cluster is essential for helicase activity, and clinically relevant Fanconi anemia mutations in FANCJ disrupt this cluster and abolish helicase activity. | PMID:16973432 | Molecular cell |
| 2007 | High | FANCJ physically interacts with the mismatch repair complex MutLα (MLH1/PMS2); FANCJ binds MLH1 directly through its helicase domain independently of BRCA1. Genetic studies showed that FANCJ helicase activity and MLH1 binding—but not BRCA1 binding—are essential to correct the ICL-induced 4N DNA accumulation and ICL sensitivity of FA-J cells. | PMID:17581638 | The EMBO journal |
| 2007 | Medium | FANCJ co-immunoprecipitates with the RPA70 subunit of Replication Protein A (RPA); FANCJ colocalizes with RPA in nuclear foci after DNA damage in a BRCA1-dependent manner; RPA stimulates FANCJ helicase activity on duplex DNA substrates. | PMID:17596542 | Blood |
| 2008 | High | FANCJ unwinds G-quadruplex (G4) DNA substrates in an ATPase-dependent manner with 5′-to-3′ polarity; this activity is specific (RECQ1 failed to unwind all G4 substrates tested); RPA stimulates FANCJ G4 unwinding while MSH2/MSH6 inhibits it; FANCJ-depleted cells treated with the G4-interactive compound telomestatin show impaired proliferation, elevated apoptosis, and increased DNA damage, implicating G4 DNA as a physiological substrate. | PMID:18426915 | Molecular and cellular biology |
| 2008 | High | FANCJ is a structure-specific DNA helicase that dissociates G4 DNA with 5′-to-3′ polarity in vitro; loss of FANCJ G4 unwinding in the FA-J cell line EUFA0030 correlates with accumulation of large genomic deletions near G4 DNA signature sequences, supporting G4 resolution as a physiological function. | PMID:18978354 | The Journal of biological chemistry |
| 2009 | High | FANCJ uses its motor ATPase to: (1) destabilize protein-DNA complexes, (2) unwind triplex (triple helix) DNA structures, and (3) inhibit RAD51 strand exchange in vitro, suggesting roles in controlling homologous recombination and resolving DNA structural obstacles. | PMID:19150983 | The Journal of biological chemistry |
| 2009 | High | FANCJ helicase is uniquely inhibited by a single thymine glycol lesion in either strand of a duplex substrate (unlike other helicases tested which show strand-specific inhibition); RPA (but not E. coli SSB) relieves FANCJ inhibition when the lesion is in the non-translocating strand, suggesting a strand-specific functional interaction between RPA and FANCJ on damaged DNA. | PMID:19419957 | The Journal of biological chemistry |
| 2010 | High | FANCJ/BACH1 interacts with TopBP1 through S-phase-specific phosphorylation of BACH1 at Thr1133, which is recognized by the C-terminal tandem BRCT7/8 domains of TopBP1. Both TopBP1 and BACH1 are required for ATR-dependent phosphorylation events and for RPA loading onto chromatin following replication stress, placing BACH1 early in replication checkpoint control. | PMID:20159562 | Molecular cell |
| 2010 | High | Crystal structure of TopBP1 BRCT7/8 domains free and in complex with a phospho-Thr1133 BACH1/FANCJ peptide reveals a dramatic conformational change upon binding: the two BRCT repeats pivot about the BRCT-BRCT interface to form an extensive peptide-binding cleft; Thr(P) recognition mechanism is distinct from canonical BRCT-phosphopeptide interactions. Systematic mutagenesis confirmed key contact residues. | PMID:21127055 | The Journal of biological chemistry |
| 2010 | Medium | FANCJ binding to BRCA1 (dependent on FANCJ phosphorylation at Ser990) regulates DNA repair pathway choice: a FANCJ mutant unable to bind BRCA1 inhibits homologous recombination and promotes Polη-dependent bypass; this bypass is dependent on FANCJ's direct interaction with MLH1. | PMID:20173781 | Oncogene |
| 2011 | Medium | FANCJ coordinates two independent mechanisms to maintain epigenetic stability near G4 DNA motifs: one dependent on REV1 translesion polymerase and one dependent on WRN and BLM helicases. Loss of FANCJ leads to G4 motif-associated epigenetic instability (loss of transcriptional states) measurable at the single-cell level. | PMID:22021381 | Nucleic acids research |
| 2011 | Medium | Oncogenic RAS downregulates BRIP1 expression, causing BRCA1 dissociation from chromatin and accumulation of DNA damage as part of RAS-induced senescence. Ectopic BRIP1 rescues BRCA1 chromatin association and suppresses RAS-induced senescence and DNA damage response, identifying BRIP1 as a physiological partner required for BRCA1 chromatin retention. | PMID:22137763 | Developmental cell |
| 2012 | Medium | FANCJ is acetylated at lysine 1249; acetylation at K1249 facilitates DNA end processing required for repair and checkpoint signaling (RPA foci formation, RPA phosphorylation, and RAD51 foci formation in response to camptothecin). Both preventing and mimicking FANCJ acetylation disrupts checkpoint maintenance; FANCJ acetylation is dispensable for ICL survival but shifts the mechanism toward recombination-dependent repair. | PMID:22792074 | PLoS genetics |
| 2012 | Medium | FOXM1 transcription factor directly binds the BRIP1 promoter and drives BRIP1 expression; depletion of FOXM1 downregulates BRIP1 at mRNA and protein levels; FOXM1's requirement for homologous recombination-based DSB repair can be circumvented by reintroduction of BRIP1, placing BRIP1 downstream of FOXM1 in DSB repair. | PMID:23108394 | Oncogene |
| 2013 | Medium | FANCJ promotes DNA replication in trans by counteracting fork stalling at G4 quadruplex structures; in ΔFANCJ cells, G4 stabilization restricts fork movement, uncouples leading- and lagging-strand synthesis, and generates single-stranded DNA gaps behind the fork. FANCJ also suppresses heterochromatin spreading by coupling fork movement through replication barriers with maintenance of chromatin structure. | PMID:23530069 | The Journal of cell biology |
| 2013 | Medium | FANCJ localization to UV-induced damage sites requires its direct interaction with the MMR protein MLH1 (not BRCA1); FANCJ, its MLH1 interaction, and MSH2 function in a common pathway in response to UV irradiation to promote RPA phosphorylation and arrest of DNA synthesis; FANCJ-deficient cells show elevated mutation frequency after UV despite no increased UV killing. | PMID:24351291 | Cancer research |
| 2014 | High | Depletion of FANCJ helicase from Xenopus egg extracts causes persistent replication stalling at G-quadruplex structures; nascent strand synthesis stalls 1–2 nucleotides from the G4, and after transient stalling G4s are normally resolved. FANCJ performs this G4 replication function independently of the classical Fanconi anemia pathway. | PMID:25193968 | The EMBO journal |
| 2014 | High | FANCD2 and FANCJ directly interact in vitro and in vivo (reciprocal co-IP, gel filtration, and baculoviral co-expression); non-ubiquitinated FANCD2 (K561R mutant) constitutively interacts with FANCJ and impedes proper FANCJ chromatin localization; FANCJ is necessary for efficient FANCD2 chromatin loading and focus formation after mitomycin C, showing mutual regulation. | PMID:25070891 | The Journal of biological chemistry |
| 2015 | Medium | FANCJ-deficient mice (Fancj GT/GT) show increased MLH1 focus frequency during meiotic prophase I and increased chiasmata, indicating increased crossovers; this increase in crossovers correlates with increased BLM helicase localization, suggesting BLM compensates for FANCJ loss to facilitate crossing over. FANCJ interacts with MLH1 and BRCA1 in the meiotic context. | PMID:26490168 | Chromosoma |
| 2015 | High | Fancj helicase-deficient mice exhibit high levels of spontaneous microsatellite instability (MSI) that is exacerbated by replication inhibitors; MSI is not observed in Fancd2-deficient mice, demonstrating that FANCJ's role in MSI suppression is functionally distinct from its role in the canonical FA ubiquitination pathway. Fancj-null mice are also predisposed to lymphoma. | PMID:26637282 | Genes & development |
| 2015 | Medium | FANCJ promotes stabilization of FANCD2 and FANCI proteins: depletion of FANCJ causes proteasome- and caspase-3-dependent degradation of FANCD2 and FANCI. FANCJ can complex with and stabilize FANCD2 even without a functional helicase domain, indicating this stabilization function is independent of helicase catalytic activity. | PMID:26336824 | Oncotarget |
| 2015 | Medium | FANCD2, FANCJ, and BRCA2 cooperate to promote replication fork restart after aphidicolin stalling independently of FA core complex-mediated monoubiquitination; non-ubiquitinated FANCD2 is sufficient for fork recovery together with FANCJ and BRCA2, supporting a non-linear FA pathway model at stalled forks. | PMID:25659033 | Cell cycle |
| 2016 | High | Single-molecule and ensemble biochemical analysis reveals FANCJ possesses a G4-specific recognition site (AKKQ motif) distinct from its helicase core; through this site FANCJ undergoes repeated rounds of stepwise G4-unfolding and refolding, partially stabilizing the G-quadruplex. The G4-recognition residues also participate in MLH1 interaction, suggesting FANCJ activity in G4 replication and ICL repair are mutually exclusive. | PMID:27342280 | Nucleic acids research |
| 2016 | Medium | The Fe-S cluster of FANCJ is indispensable for DNA unwinding in vitro and for cellular resistance to ICL-inducing agents; cancer-associated FeS domain mutations abolish helicase activity and impair G4 unfolding on DNA templates in a primer extension assay with polymerase delta. FeS-cluster-deficient FANCJ variants retain partial ability to suppress replisome-associated G4 structures but sensitize cells to G4-stabilizing agents. | PMID:32542039 | PLoS genetics |
| 2016 | Medium | FANCJ is essential for maintaining microsatellite structure genome-wide during replication stress: hydroxyurea or aphidicolin treatment of FANCJ-depleted cells causes loss of diverse microsatellite PCR signals and chromosome recombination at ectopic hairpin-forming CTG/CAG repeats; this phenotype is specific to FANCJ and is distinct from the intact FA pathway. | PMID:27179029 | Nucleic acids research |
| 2017 | Medium | FANCJ controls the balance between short-tract and long-tract gene conversions (STGC and LTGC) at chromosomal DSBs; FANCJ-deficient cells show reduced overall gene conversions biased toward LTGC. This regulation requires the FANCJ-BRCA1 interaction, and helicase activity is essential for controlling overall HR and terminating extended repair synthesis during sister chromatid recombination. | PMID:28911102 | Nucleic acids research |
| 2018 | Medium | FANCJ knockout cells show aberrant accumulation of the fork remodeling factor HLTF at replication forks; HLTF contributes to fork degradation in FANCJ-KO cells. FANCJ-dependent unrestrained DNA synthesis in HLTF-deficient cells correlates with S1-nuclease sensitivity and fork degradation, indicating FANCJ and HLTF counteract each other to maintain fork remodeling/elongation balance. | PMID:30232006 | Cell reports |
| 2020 | Medium | FANCJ promotes DNA end resection by recruiting CtIP to DSB sites; this recruitment depends on FANCJ K1249 acetylation, which in turn requires CDK-mediated phosphorylation of FANCJ at S990. CDK phosphorylation of FANCJ at S990 also independently facilitates BRCA1 interaction at damage sites. ATP-hydrolysis-deficient FANCJ partially supports end resection, indicating both scaffolding and helicase activity contribute. | PMID:32251466 | PLoS genetics |
| 2019 | Medium | FANCJ is tethered to the core promoter of REG3A via an RNA-DNA triplex formed by lncRNA REG1CP; once at the promoter, FANCJ unwinds double-stranded DNA to facilitate a permissive state for glucocorticoid receptor α (GRα)-mediated REG3A transcription, identifying a transcriptional regulatory role for FANCJ. | PMID:31767869 | Nature communications |
| 2019 | Medium | FANCJ AKKQ peptide binds tightly to a TTA loop of G4 structures and is sequestered away from 8-oxoguanine damage in the G4; a FANCJ PIP-like region recruits REV1 polymerase preferentially over PCNA, suggesting FANCJ assembles a G4 repair complex by engaging both G4 recognition (via AKKQ) and REV1 recruitment (via PIP). | PMID:31861576 | Genes |
| 2023 | High | FANCJ helicase plays a direct role in DNA-protein crosslink (DPC) repair: FANCJ binds ssDNA downstream of a DPC and uses its ATPase activity to unfold the protein adduct, exposing the underlying DNA for SPRTN protease cleavage. FANCJ is also essential for SPRTN activation after CMG bypass of a DPC, and FANCJ-dependent DPC unfolding enables translesion DNA synthesis past DPCs that cannot be degraded by SPRTN. | PMID:36608669 | Molecular cell |
| 2024 | Medium | MutSβ, an MLH1-PMS1 heterodimer (MutLβ), and FANCJ are required for MUS81-initiated restart of DNA replication stalled at transcription-replication conflict (TRC)-associated G4/R-loops; MutSβ recruits FANCJ to G4s via its G4-binding activity, and the process depends on FANCJ helicase activity and FANCJ-MLH1 interaction. | PMID:38324687 | Science advances |
| 2024 | Medium | FANCJ promotes PARP1 activity during S-phase DNA replication; in FANCJ-deficient cells, G-quadruplex structures sequester PARP1 and MSH2, reducing PARP1 activity. Loss of the FANCJ-MLH1 interaction also diminishes PARP1 activity. In BRCA1-deficient cells, FANCJ loss mirrors PARP1 loss in reducing S-phase PARP1 activity, explaining FANCJ's requirement for PARP inhibitor effectiveness in BRCA1-deficient contexts. | PMID:38521768 | Nature communications |
| 2006 | Medium | BACH1 helicase requires contacts with both the translocating and non-translocating strands for efficient DNA unwinding; an increased motor ATPase variant (M299I) enables BACH1 to overcome backbone discontinuities, and increasing the 5′ tail length of the substrate allows loading and unwinding of backbone-modified substrates. | PMID:17145708 | Nucleic acids research |
| 2012 | High | The Q motif of FANCJ (invariant Q25) is essential for dimerization: wild-type FANCJ exists as both monomer and dimer by size exclusion chromatography and sedimentation velocity; the dimeric form has higher specific ATPase and helicase activities and greater DNA binding. The Q25A mutation prevents dimerization, abolishes helicase and ATPase activity, impairs DNA binding, and fails to complement fancj-null cell sensitivity to cisplatin or telomestatin. | PMID:22582397 | The Journal of biological chemistry |
| 2010 | Medium | FANCJ nuclear foci assemble during S phase and are induced by various stresses; FANCJ helicase activity and BRCA1-binding capacity are both required for FANCJ nuclear focus formation; FANCJ and FANCD2 substantially co-localize in foci, and FANCJ promotes assembly of FANCD2 nuclear foci, linking FANCJ to FANCD2 chromatin recruitment. | PMID:20676667 | Chromosoma |

## Citations

- PMID:16116421
- PMID:16116423
- PMID:16116424
- PMID:16153896
- PMID:16973432
- PMID:17145708
- PMID:17581638
- PMID:17596542
- PMID:18426915
- PMID:18978354
- PMID:19150983
- PMID:19419957
- PMID:20159562
- PMID:20173781
- PMID:20676667
- PMID:21127055
- PMID:22021381
- PMID:22137763
- PMID:22582397
- PMID:22792074
- PMID:23108394
- PMID:23530069
- PMID:24351291
- PMID:25070891
- PMID:25193968
- PMID:25659033
- PMID:26336824
- PMID:26490168
- PMID:26637282
- PMID:27179029
- PMID:27342280
- PMID:28911102
- PMID:30232006
- PMID:31767869
- PMID:31861576
- PMID:32251466
- PMID:32542039
- PMID:36608669
- PMID:38324687
- PMID:38521768
