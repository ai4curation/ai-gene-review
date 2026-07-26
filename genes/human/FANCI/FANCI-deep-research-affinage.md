---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/FANCI
affinage_run_date: 2026-06-09T23:54:43
uniprot_accession: Q9NVI1
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 43
citation_count: 43
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for FANCI (human)

## Current model (mechanistic narrative)

FANCI is a central effector of the Fanconi anemia DNA interstrand crosslink (ICL) repair pathway, functioning as the obligate partner of FANCD2 in a heterodimeric (ID2) clamp that recognizes and processes damaged replication forks [PMID:17412408, PMID:17460694]. The complex acts as a sliding clamp that diffuses on dsDNA and stalls specifically at single-strand/double-strand junctions characteristic of stalled forks, then encircles the DNA through a closed conformation [PMID:39085614, PMID:32066963]. Activation proceeds through ordered post-translational regulation: ATR phosphorylates conserved S/TQ motifs (notably S556, S559, S565), priming the complex by destabilizing its open state, stabilizing DNA and FANCD2 association, and protecting the eventual ubiquitin marks from USP1:UAF1 [PMID:18931676, PMID:32117957, PMID:36050501], and PP2A dephosphorylates an inhibitory FANCD2 cluster to license chromatin loading [PMID:39535917]. The UBE2T-FANCL E2-E3 pair then monoubiquitinates FANCD2 (K561) and FANCI (K523), a reaction strongly stimulated by FANCI's DNA binding and required for clamping the heterodimer on dsDNA [PMID:19111657, PMID:19589784, PMID:22287633, PMID:32167469]; FANCI's own ubiquitin reciprocally protects FANCD2's ubiquitin from USP1-UAF1 deubiquitination and enables re-ubiquitination, establishing an interdependent ubiquitin lock [PMID:32510829, PMID:36385258]. The activated clamp recruits the downstream nuclease FAN1 and directly stabilizes RAD51-DNA filaments to protect fork ends [PMID:20671156, PMID:27694619]. Beyond canonical repair, FANCI carries out FANCD2-independent functions: it restrains dormant origin firing under replication stress [PMID:25843623], localizes to the nucleolus to support pre-rRNA transcription and large-subunit processing in its deubiquitinated state [PMID:30692263], stimulates homologous recombination D-loop formation and is essential for meiosis and spermatogenesis [PMID:31219578, PMID:34373449], and can switch from FANCD2 partnering to PIDD1 binding to drive caspase-2/PIDDosome-dependent apoptosis when ICL repair fails [PMID:34256011]. Patient-derived mutations affecting the C-terminal NLS/EDGE region and the Tower domain disrupt these activities, linking FANCI to the Fanconi anemia phenotype [PMID:20971953, PMID:27405460].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0003677 DNA binding, GO:0003723 RNA binding, GO:0140096 catalytic activity, acting on a protein, GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005634 nucleus, GO:0000228 nuclear chromosome, GO:0005730 nucleolus
- **pathway (Reactome):** R-HSA-73894 DNA Repair, R-HSA-69306 DNA Replication, R-HSA-392499 Metabolism of proteins, R-HSA-5357801 Programmed Cell Death, R-HSA-8953854 Metabolism of RNA, R-HSA-1474165 Reproduction
- **partners:** FANCD2, FANCL, UBE2T, FAN1, RAD51, USP1, PIDD1, PHLPP1
- **complexes:** FANCI-FANCD2 (ID2) complex, FA core complex, PIDDosome (PIDD1-RAIDD-caspase-2)

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2007 | High | FANCI is monoubiquitinated (on K523) and forms the FANCI-FANCD2 (ID) complex that localizes to chromatin in response to DNA damage; ubiquitination of each protein is required for maintenance of ubiquitin on the other, indicating a dual ubiquitin-locking mechanism. | PMID:17412408, PMID:17460694 | Cell |
| 2007 | High | FANCI is an ATM/ATR kinase substrate required for resistance to mitomycin C-induced DNA interstrand crosslinks; it is a paralog of FANCD2 likely evolving from a common ancestral gene. | PMID:17412408 | Cell |
| 2008 | High | Multiple phosphorylation of conserved Ser/Thr-Gln (S/TQ) motifs in FANCI acts as a molecular switch to activate the FA pathway: alanine substitutions at six clustered S/TQ sites abrogate monoubiquitination and focus formation of both FANCI and FANCD2, while phosphomimetic mutations constitutively activate monoubiquitination and confer crosslink resistance. | PMID:18931676 | Nature structural & molecular biology |
| 2008 | High | FANCI enhances FANCD2 monoubiquitination by Ube2t-FANCL in vitro and restricts ubiquitination to the correct in vivo lysine residue on FANCD2. | PMID:19111657 | Molecular cell |
| 2009 | High | FANCI directly binds DNA with a preference for branched structures; the DNA-binding domain spans approximately residues 200–1000; the FANCI-FANCD2 complex shows enhanced and preferential binding to branched DNA substrates compared to either protein alone; FANCI interacts with FANCD2 through its C-terminal region (residues 1001–1328). | PMID:19561358, PMID:19589784 | The Journal of biological chemistry |
| 2009 | High | FANCI is monoubiquitinated specifically on Lys-523 by the UBE2T-FANCL E2-E3 pair in vitro. | PMID:19589784 | The Journal of biological chemistry |
| 2010 | High | The monoubiquitinated FANCI-FANCD2 (ID) complex recruits the downstream nuclease FAN1 to sites of DNA damage to facilitate ICL repair; FAN1 accumulation is strictly dependent on ID complex monoubiquitination. | PMID:20671156 | Science |
| 2011 | High | Crystal structure of the ~300 kDa FANCI-FANCD2 (ID) complex at 3.4 Å reveals that monoubiquitination and regulatory phosphorylation sites map to the I-D interface; electron density maps of FANCI-DNA crystals show binding sites for both single- and double-stranded DNA, suggesting the ID complex recognizes DNA structures formed at replication fork-ICL encounters. | PMID:21764741 | Science |
| 2012 | Medium | FANCI stimulates FANCD2-mediated nucleosome assembly (histone chaperone activity) in vitro, although FANCI alone lacks nucleosome-assembly activity; this activity is required for DNA crosslink repair. | PMID:22828868 | The EMBO journal |
| 2012 | High | Various forms of DNA (ssDNA, dsDNA, branched DNA) robustly stimulate FANCD2 monoubiquitination in vitro in a manner strictly requiring FANCI; a FANCI mutant defective in DNA binding is also defective in stimulating FANCD2 monoubiquitination. | PMID:22287633 | Nucleic acids research |
| 2012 | Medium | FANCI phosphorylation (at S/TQ sites) is the molecular trigger for FANCD2-FANCI dissociation: phosphodead FANCI fails to dissociate from FANCD2, while phosphomimetic FANCI cannot interact with FANCD2; FANCD2-FANCI complex represents the inactive form and dissociates upon DNA damage-induced FA pathway activation. | PMID:22753026 | Nucleic acids research |
| 2014 | High | FANCI DNA-binding activity is required for DNA-stimulated FANCD2 monoubiquitination within the ID2 complex; duplex or branched DNA strongly stimulates FANCD2 monoubiquitination in the ID2 complex via FANCL interaction, but in the absence of FANCD2, DNA stimulates FANCI monoubiquitination in a FANCL-independent manner. | PMID:24623813 | Nucleic acids research |
| 2015 | High | ATR-mediated phosphorylation of FANCI inhibits dormant origin firing while promoting replication fork restart/DNA repair; FANCI co-localizes with MCM-bound chromatin under replication stress; cells lacking FANCI have reduced origins and increased inter-origin distances. | PMID:25843623 | Molecular cell |
| 2015 | Medium | FANCI, but not its partner FANCD2, is required for efficient FA core complex recruitment to sites of DNA damage (nuclear foci formation); FANCI deubiquitination by USP1 is required for this function; monoubiquitination and ATR-dependent phosphorylation of FANCI are not required for core complex recruitment. | PMID:26430909 | PLoS genetics |
| 2016 | High | The FANCI-FANCD2 (I-D) complex directly binds RAD51 and stabilizes RAD51-DNA filaments; DNA binding activity of FANCI (but not FANCD2) is required for this stabilization; the stabilized RAD51 filament protects DNA ends from FAN1 nucleolytic degradation. | PMID:27694619 | Nucleic acids research |
| 2016 | Medium | The FA core complex contains a homo-dimeric catalytic module (FANCB-FANCL-FAAP100 dimer of trimers) with two FANCL molecules positioned to ubiquitinate both FANCI and FANCD2; FANCC-FANCE-FANCF bridges the catalytic module to FANCI-FANCD2 and stabilizes the dimerization interface. | PMID:27986592 | Cell reports |
| 2016 | Medium | FANCI acts as a negative regulator of Akt activation: depletion of FANCI (but not FANCD2 or USP1) results in increased Akt phosphorylation/activation due to reduced PHLPP1-Akt interaction; FANCI forms a complex with Akt, PHLPP1, PHLPP2, FANCD2, USP1, and UAF1. | PMID:27097374 | Cell cycle |
| 2016 | High | Cryo-EM structure of the human FANCD2-FANCI complex reveals an inner cavity large enough to accommodate dsDNA and a protruding Tower domain; the complex is recruited to a stalled replication fork before monoubiquitination, and this recruitment triggers the activating monoubiquitination event; disease-causing mutations in the Tower domain impair this function. | PMID:27405460 | Nature communications |
| 2017 | Medium | FANCI phosphorylation at S/TQ sites occurs in two temporally distinct phases: serine 556 is phosphorylated upstream of monoubiquitination (ubiquitination-independent), while serines 559 and 565 are phosphorylated downstream (ubiquitination-linked); ubiquitination-linked phosphorylation inhibits FANCD2 deubiquitination by USP1 and is required for effective ICL repair. | PMID:28636932 | Cell reports |
| 2017 | Medium | FANCI and FANCD2 associate with spliceosomal protein SF3B1 (U2 snRNP); replication stress induces ATR-dependent release of SF3B1 from nuclear speckles requiring FANCI; chromatin-bound FANCI and FANCD2 prevent accumulation of post-catalytic intron lariats and contribute to eviction of splicing factors. | PMID:29030393 | The Journal of cell biology |
| 2019 | Medium | FANCI localizes to the nucleolus and functions in pre-rRNA transcription and large ribosomal subunit pre-rRNA processing independently of FANCD2; in the nucleolus FANCI is predominantly in the deubiquitinated state, requiring both nucleoplasmic deubiquitinase USP1 and nucleolar deubiquitinase USP36. | PMID:30692263 | Proceedings of the National Academy of Sciences |
| 2019 | High | Purified human FANCI-FANCD2 (ID2) complex binds single-stranded RNA (ssRNA) and R-loop substrates with high affinity, preferring guanine-rich sequences; R-loop binding is via the displaced ssDNA and ssRNA but not the RNA:DNA hybrid; RNA and R-loop substrates strongly stimulate ID2 monoubiquitination in vitro. | PMID:30650351 | Cell reports |
| 2020 | High | Cryo-EM structures show that monoubiquitinated FANCD2-FANCI adopts a closed conformation that encircles dsDNA; ubiquitin at the FANCD2-FANCI interface acts as a covalent molecular pin to trap the complex on DNA; unmodified isolated FANCD2 forms a homodimer unable to bind DNA, suggesting an autoinhibitory mechanism. | PMID:32066963 | Nature structural & molecular biology |
| 2020 | High | Monoubiquitination of FANCI:FANCD2 clamps the heterodimer onto dsDNA, forming filament-like arrays on long dsDNA; clamping requires monoubiquitination of only the FANCD2 subunit; monoubiquitination does not promote specific exogenous protein-protein interactions. | PMID:32167469 | eLife |
| 2020 | High | Ubiquitination of FANCD2 promotes a large-scale conformational change in the ID2 complex that increases affinity for dsDNA by forming a secondary 'Arm' interface that encircles DNA; ubiquitination of FANCI protects the ubiquitin on FANCD2 from USP1-UAF1 deubiquitination via key hydrophobic residues on FANCI's ubiquitin. | PMID:32510829 | EMBO reports |
| 2020 | High | ATR directly phosphorylates FANCI on serines 556, 559, and 565 to stabilize its association with DNA and FANCD2; this phosphorylation stimulates ubiquitin conjugation to both FANCI and FANCD2 and inhibits deubiquitination by USP1:UAF1; S559 and S565 are particularly important for protecting the complex from USP1:UAF1. | PMID:32117957 | Frontiers in cell and developmental biology |
| 2021 | High | FANCI switches between two mutually exclusive binding partners depending on ICL repair status: it binds FANCD2 for repair, or alternatively binds PIDD1 to enable PIDDosome (PIDD1-RAIDD-caspase-2) formation and apoptosis when ICL repair fails; monoubiquitination and deubiquitination at K523 regulate interactor selection. | PMID:34256011 | Developmental cell |
| 2021 | Medium | FANCI is essential for spermatogenesis in mice: FANCI deletion causes massive germ cell apoptosis, loss of undifferentiated spermatogonia, and impairs FANCD2 foci formation; FANCI is required for H3K4 and H3K9 methylation on meiotic sex chromosomes. | PMID:34373449 | Cell death & disease |
| 2019 | Medium | FANCI interacts with RAD51 and stimulates D-loop formation (homologous recombination) independently of FANCD2; FANCI co-localizes with RPA along meiotic chromosomes; Fanci knockout mice display severe hypogonadism and meiotic phenotype. | PMID:31219578 | Nucleic acids research |
| 2022 | High | Cryo-EM structures of phosphomimetic FANCI-FANCD2 show that phosphorylation destabilizes the open state of the complex and promotes closure around DNA independent of the FA core complex; phosphomimetic mutations do not substantially alter DNA binding affinity but alter conformational dynamics to prime the complex for ubiquitination. | PMID:36050501 | Nature structural & molecular biology |
| 2022 | High | Cryo-EM structure of the FANCI-ubiquitinated/FANCD2-unmodified (IUbD2) complex shows the complex in the closed DNA-clamping conformation; FANCD2 target lysine K561 becomes fully exposed (primed for ubiquitination) in IUbD2-DNA, while FANCI's K523 is primed for ubiquitination in ID2Ub-DNA; FANCI ubiquitination maintains FANCD2 ubiquitination by preventing its deubiquitination and enabling re-ubiquitination. | PMID:36385258 | The EMBO journal |
| 2024 | High | FANCD2-FANCI is a sliding clamp that diffuses on dsDNA and stalls at ss-dsDNA junctions (structures formed at stalled replication forks); cryo-EM structures show that stalled D2-I makes specific contacts with the ss-dsDNA junction distinct from those of sliding D2-I, providing a unified mechanism for surveillance and recognition of stalled replication forks. | PMID:39085614 | Nature |
| 2024 | High | PP2A phosphatase complex dephosphorylates an inhibitory cluster in FANCD2, licensing FANCD2/FANCI complex loading onto chromosomes and enabling monoubiquitination; this was reconstituted in vitro as a coupled dephosphorylation-ubiquitination reaction. | PMID:39535917 | Cell reports |
| 2024 | Medium | SRSF1 physically interacts with FANCD2 and acts together to suppress R-loop formation via mRNA export regulation; SRSF1 stimulates FANCD2 monoubiquitination in an RNA-dependent fashion; FANCD2 monoubiquitination is required for assembly of the SRSF1-NXF1 nuclear export complex and mRNA export. | PMID:38165804 | Cell reports |
| 2024 | Medium | The FANCD2-FANCI heterodimer dynamically interacts with open chromatin regions including DSB-induced open chromatin; loaded FANCD2-FANCI stabilizes open chromatin and promotes DNA resection and RPA loading through increased BRCA1 and BLM association; chromatin-loaded FANCD2-FANCI promotes G2 cell cycle arrest via the ATR-CHK1-WEE1 axis. | PMID:41505257 | Cell reports |
| 2010 | Medium | In C. elegans, FANCI homolog is required for FANCD2 focus formation and ubiquitination after DNA crosslinking; FANCM, FANCI, and checkpoint proteins RPA, ATR, and CHK1 are all required for FANCD2 activation, demonstrating conservation of the FANCD2 activation pathway involving FANCI. | PMID:20075016 | DNA repair |
| 2011 | Medium | RAD18 E3 ubiquitin ligase binds FANCD2 and is required for efficient monoubiquitination and chromatin localization of both FANCD2 and FANCI; mutation of the RAD18 RING domain ablates interaction with and chromatin loading of FANCD2; FANCD2 ubiquitination is normal in cells with ubiquitination-resistant PCNA. | PMID:21355096 | Blood |
| 2013 | Medium | FANCI is dispensable for FANCD2-dependent BLM complex regulation: FANCD2 (but not FANCI) maintains BLM stability, is required for complete BLMcx assembly, recruits BLMcx to replicating chromatin, and mediates BLMcx phosphorylation in response to DNA damage, demonstrating functional separation of the two ID complex partners. | PMID:23658231 | Nucleic acids research |
| 2010 | Medium | The C-terminus of FANCI (last 30 residues) contains two separable functional elements: a nuclear localization signal required for nuclear import of FANCI and robust FANCD2 monoubiquitination, and an EDGE motif important for DNA crosslink repair; the patient-derived R1299X mutation deletes both elements causing protein mislocalization. | PMID:20971953 | Blood |
| 2019 | Low | FANCI directly binds IMPDH2 and prevents its degradation; this interaction activates MEK/ERK/MMP signaling in lung adenocarcinoma cells; FANCI knockdown inhibits proliferation, migration, and invasion which can be reversed by IMPDH2 overexpression. | PMID:32021289 | OncoTargets and therapy |
| 2019 | Medium | CTDP1 interacts with FANCI (via CTDP1's BRCT domain) and regulates FANCI chromatin localization, γ-H2AX interaction, and S/TQ motif phosphorylations; CTDP1 expression promotes FANCA and FANCD2 foci formation and enhances homologous recombination repair efficiency. | PMID:31240132 | Cell death discovery |
| 2018 | Medium | BRMS1 directly interacts with FANCI (via its linker region between two coiled-coil motifs) and is required for efficient monoubiquitination of both FANCI and FANCD2 in response to ICL damage; BRMS1-deficient cells show suppressed FANCD2 foci formation and ICL hypersensitivity. | PMID:30365131 | Oncology reports |
| 2024 | Low | FANCI interacts with PARP1 and suppresses its nuclear localization and functionality; FANCI inhibition sensitizes breast cancer cells to PARP inhibitor talazoparib in the absence of BRCA mutations. | PMID:39037758 | Cancer research |

## Citations

- PMID:17412408
- PMID:17460694
- PMID:18931676
- PMID:19111657
- PMID:19561358
- PMID:19589784
- PMID:20075016
- PMID:20671156
- PMID:20971953
- PMID:21355096
- PMID:21764741
- PMID:22287633
- PMID:22753026
- PMID:22828868
- PMID:23658231
- PMID:24623813
- PMID:25843623
- PMID:26430909
- PMID:27097374
- PMID:27405460
- PMID:27694619
- PMID:27986592
- PMID:28636932
- PMID:29030393
- PMID:30365131
- PMID:30650351
- PMID:30692263
- PMID:31219578
- PMID:31240132
- PMID:32021289
- PMID:32066963
- PMID:32117957
- PMID:32167469
- PMID:32510829
- PMID:34256011
- PMID:34373449
- PMID:36050501
- PMID:36385258
- PMID:38165804
- PMID:39037758
- PMID:39085614
- PMID:39535917
- PMID:41505257
