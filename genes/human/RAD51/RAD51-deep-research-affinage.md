---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/RAD51
affinage_run_date: 2026-06-10T06:43:36
uniprot_accession: Q06609
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 45
citation_count: 45
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for RAD51 (human)

## Current model (mechanistic narrative)

RAD51 is the central eukaryotic recombinase that assembles as an ATP-dependent nucleoprotein filament on single-stranded DNA and catalyzes homology search and DNA strand exchange, the core reaction of homologous recombination [PMID:9012806]. Filament assembly on RPA-coated ssDNA is rate-limited by nucleation, which BRCA2 overcomes by chaperoning a preassembled RAD51 nucleus onto ssDNA, displacing RPA and stabilizing the filament against ATP hydrolysis [PMID:20729832, PMID:36976771]; a C-terminal BRCA2 TR2 motif braces adjacent protomers across the filament interface, while the BRC repeats engage distinct RAD51 surfaces [PMID:37919288, PMID:15937124]. The filament's recombinase activity is intrinsically coupled to ATP hydrolysis and to an inter-subunit ATP cap that tunes turnover versus strand-exchange efficiency [PMID:9012806, PMID:22275364], and Loop2 residues impose strict mismatch intolerance that distinguishes RAD51 from its meiotic counterpart DMC1 [PMID:34871438]. A broad network of mediators governs the filament: RAD52 targets RAD51 to RPA-ssDNA and channels lesions between strand invasion and annealing [PMID:9450760, PMID:9450758, PMID:18337252], Rad54 stimulates homologous pairing and branch migration and drives ATPase-dependent filament turnover from duplex DNA [PMID:9590697, PMID:17567608, PMID:18617519], the RAD51 paralogs assemble into complexes that remodel and stabilize presynaptic filaments [PMID:10749867, PMID:26186187, PMID:23810717], and HOP2-MND1 and FANCD2/FANCI further stimulate or stabilize the filament [PMID:24943459, PMID:27694619, PMID:37526271]. Filament abundance at replication forks is set antagonistically by RADX, which competes for ssDNA, stimulates RAD51 ATPase, and destabilizes filaments in opposition to BRCA2 [PMID:30021152, PMID:33453169, PMID:32621611]. Chromatin loading is controlled by post-translational modification, including TOPBP1/PLK1-dependent Ser14 phosphorylation, Mec1-dependent phosphorylation of the yeast enzyme, and TOPORS-dependent SUMOylation [PMID:26811421, PMID:21738226, PMID:35061896]. Beyond canonical double-strand break repair and break-induced replication [PMID:14993274], RAD51 protects stalled and nascent replication forks—catalyzing fork reversal while bypassing the bound CMG helicase, shielding abasic sites and nascent strands from MRE11/DNA2/EXO1 nucleases, and suppressing transcription-replication conflicts [PMID:37104614, PMID:39178838, PMID:37526271, PMID:36002000]; in its absence, MRE11-driven degradation of unprotected nascent DNA releases cytosolic fragments that activate STING-mediated innate immunity [PMID:28334891]. RAD51 also promotes mitotic DNA synthesis and centromere integrity [PMID:34508092, PMID:36702125] and forms TERRA R-loops at telomeres [PMID:33057192].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0003677 DNA binding, GO:0140657 ATP-dependent activity, GO:0140097 catalytic activity, acting on DNA, GO:0003723 RNA binding
- **localization:** GO:0005634 nucleus, GO:0000228 nuclear chromosome
- **pathway (Reactome):** R-HSA-73894 DNA Repair, R-HSA-69306 DNA Replication, R-HSA-1640170 Cell Cycle, R-HSA-168256 Immune System
- **partners:** BRCA2, RAD52, RAD54, RADX, FANCD2, HELQ, RAD51C, DMC1
- **complexes:** RAD51-ssDNA presynaptic nucleoprotein filament, RAD51 paralog complex (RAD51B-RAD51C)

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2010 | High | Purified full-length human BRCA2 promotes assembly of RAD51 onto single-stranded DNA (ssDNA) by targeting RAD51 to ssDNA over double-stranded DNA, enabling RAD51 to displace RPA from ssDNA, and stabilizing RAD51-ssDNA filaments by blocking ATP hydrolysis. BRCA2 does not mediate ssDNA annealing. | PMID:20729832 | Nature |
| 1998 | High | Yeast Rad52 protein stimulates DNA strand exchange by Rad51 by targeting Rad51 to RPA-coated ssDNA, overcoming the inhibitory effect of RPA on presynaptic filament formation; stimulation requires concerted action of Rad51, Rad52, and RPA via specific protein-protein interactions. | PMID:9450760, PMID:9450758 | Nature |
| 1998 | High | Yeast Rad54 protein physically interacts with Rad51 and strongly stimulates the rate of homologous DNA pairing between ssDNA and dsDNA catalyzed by Rad51; Rad54 possesses a dsDNA-dependent ATPase activity. | PMID:9590697 | Nature |
| 1997 | High | Purified human RAD51 (HsRad51) catalyzes ATP-dependent homologous pairing and DNA strand exchange in vitro; rates of ATP hydrolysis, homologous pairing, and strand exchange by HsRad51 are less than 1/10 those of RecA. In the presence of ATP-γS, HsRad51 forms stable presynaptic complexes and promotes renaturation but does not catalyze strand exchange or homologous pairing with duplex DNA, suggesting that homologous pairing and strand exchange by HsRad51 are more closely linked to ATP hydrolysis than in RecA. | PMID:9012806 | Proceedings of the National Academy of Sciences of the United States of America |
| 1998 | High | Human Rad52 stimulates homologous pairing by human Rad51; hRad52 binds ssDNA and is involved in an early stage of Rad51-mediated recombination. | PMID:9450758 | Nature |
| 2005 | High | BRCA2 BRC repeats (BRC3 and BRC4) bind RAD51-DNA nucleoprotein filaments at lower molar ratios and only disrupt filaments at high concentrations. BRC3 contacts the N-terminal domain of RAD51 and BRC4 contacts the nucleotide-binding core, showing that BRC repeats are non-equivalent in their mode of interaction with RAD51 filaments. | PMID:15937124 | Proceedings of the National Academy of Sciences of the United States of America |
| 2000 | Medium | Human Rad51 redistributes to selectively UV-damaged, halogenated-thymidine-labeled chromatin after UV microirradiation, with recruitment occurring from pre-existing S-phase nuclear foci. Rad51 foci associate preferentially with postreplicative rather than replicating chromatin, supporting a role in recombinational repair of damage in postreplicative chromatin. | PMID:10908572 | The Journal of cell biology |
| 2004 | Medium | RAD51 is required for more than 95% of break-induced replication (BIR) events at unique chromosomal sequences in yeast, demonstrating a genetic requirement for RAD51 in strand invasion during BIR. | PMID:14993274 | Molecular and cellular biology |
| 2000 | Medium | Human RAD51 paralogs (XRCC2, XRCC3, RAD51B, RAD51C, RAD51D) form simultaneous protein interactions with each other and with HsRAD51; three-hybrid and baculovirus co-purification experiments show that some interactions (e.g., RAD51B-RAD51D) require a third paralog (RAD51C) to occur, suggesting they may form multi-protein complexes. | PMID:10749867 | The Journal of biological chemistry |
| 1999 | Medium | The C-terminal region of HsRad51 contains amino acid residues required for binding to HsRad52; mutations in this region (not the N-terminal domain) impair HsRad52 binding. The HsRad51 F259V mutation, which abrogates HsRad52 binding, reduces the stimulation of homologous pairing that occurs with both proteins together without affecting HsRad51-only pairing, establishing that the HsRad51-HsRad52 interaction is important for cooperative homologous pairing. | PMID:10448035 | Journal of molecular biology |
| 2007 | Medium | Efficient turnover of Rad51 from dsDNA after strand exchange requires both the Rad51 ATPase activity and the Rad54 ATPase activity; the catalytic efficiency of Rad54's ATPase is stimulated by Rad51 partial filaments on dsDNA. The Rad51-K191R ATPase-dead mutant forms filaments with significantly increased stability on DNA. | PMID:17567608 | Nucleic acids research |
| 2008 | High | Rad51 inhibits Rad52-mediated annealing of complementary ssDNA in an ATP-dependent manner through specific protein-protein interaction; the Rad51 nucleoprotein filament is more inhibitory than free Rad51. Rad59 partially restores Rad52 annealing in the presence of Rad51, suggesting coordinated channeling of processed DSBs to either strand invasion or annealing pathways. | PMID:18337252 | The Journal of biological chemistry |
| 2008 | Medium | Human Rad51 specifically stimulates the branch migration activity of human Rad54 through protein-protein interactions; the active conformation of the hRad51 filament is more stimulatory than the inactive form. This stimulation is evolutionarily conserved (also observed with yeast proteins). | PMID:18617519 | The Journal of biological chemistry |
| 2009 | Medium | Human PSF directly interacts with RAD51 through its N-terminal region and modulates RAD51-mediated homologous pairing and strand exchange in a concentration-dependent biphasic manner: stimulating at low RAD51 concentrations and inhibiting at optimal RAD51 concentrations. | PMID:19447914 | Nucleic acids research |
| 2015 | High | The C. elegans RAD51 paralog complex RFS-1/RIP-1 binds pre-synaptic RAD51 filaments and remodels them to a stabilized, 'open,' and flexible conformation in which ssDNA is more accessible and RAD51 dissociation rate is reduced. Walker box mutations in RFS-1 that abolish filament remodeling also abolish stimulation of RAD51 strand exchange, demonstrating that remodeling activity is essential for function. | PMID:26186187 | Cell |
| 2016 | Medium | TOPBP1 promotes PLK1 kinase-mediated phosphorylation of RAD51 at serine 14, which is required for RAD51 recruitment to chromatin (chromatin loading and foci formation) during homologous recombination repair; TOPBP1 BRCT domains 7/8 are essential for RAD51 foci formation. | PMID:26811421 | The Journal of cell biology |
| 2018 | Medium | RADX antagonizes RAD51 by competing with RAD51 for binding to ssDNA, modulating the amount of RAD51 at stalled replication forks. Loss of RADX restores fork protection in BRCA1-, BRCA2-, FANCA-, FANCD2-, or BOD1L-deficient cells; overexpression of RADX causes fork degradation dependent on MRE11 and DNA2 nucleases and fork reversal. | PMID:30021152 | Cell reports |
| 2021 | High | RADX directly and selectively interacts with ATP-bound RAD51, stimulates RAD51 ATP hydrolysis, and destabilizes RAD51 nucleofilaments, thereby inhibiting RAD51 strand exchange and D-loop formation. BRCA2 can overcome RADX-dependent RAD51 inhibition, placing RADX in functional opposition to BRCA2 in regulating RAD51 nucleofilament stability during DNA replication. | PMID:33453169 | Molecular cell |
| 2020 | High | RADX condenses ssDNA filaments (including RPA-coated ssDNA) via higher-order assemblies, blocks RPA displacement by RAD51, and prevents RAD51 loading onto ssDNA, functioning as a negative regulator of RAD51 filament formation. | PMID:32621611 | Nucleic acids research |
| 2023 | Medium | RAD51 uses its strand exchange activity to bypass the CMG replicative helicase (which remains bound to a stalled fork) during replication fork reversal. If the helicase is unloaded, RAD51 is no longer required for fork reversal. Thus RAD51 creates a parental DNA duplex behind the helicase that DNA translocases use for branch migration to generate the reversed fork structure. | PMID:37104614 | Science (New York, N.Y.) |
| 2017 | Medium | RAD51 deficiency leads to accumulation of self-DNA in the cytoplasm, triggering a STING-mediated innate immune response; the unprotected nascent genome in RAD51-deficient cells is degraded by MRE11 exonuclease, and the resulting fragmented nascent DNA accumulates in the cytosol to initiate innate immune signaling. | PMID:28334891 | Nucleic acids research |
| 2016 | Medium | FANCI-FANCD2 (I-D) complex directly binds RAD51 and stabilizes the RAD51-DNA filament in a manner requiring the DNA-binding activity of FANCI; the stabilized filament protects the 5'-DNA end from FAN1 nucleolytic degradation. The RAD51 mutant from FANCR patient cells fails to achieve this protection. | PMID:27694619 | Nucleic acids research |
| 2014 | High | HOP2-MND1 heterodimer stimulates RAD51 DNA strand exchange by inducing conformational changes in RAD51 that enhance interaction with nucleotide cofactors, modify DNA-binding specificity, facilitate RAD51 loading onto ssDNA, and promote dsDNA binding during the homology search; HOP2-MND1 enables strand exchange in the absence of divalent metal ions and offsets the K133A ATP-binding mutation. | PMID:24943459 | Nature communications |
| 2012 | High | The conserved aspartate at the inter-subunit ATP cap (Asp-316 in human RAD51) forms a salt bridge with the ATP γ-phosphate in the nucleoprotein filament, enhancing filament turnover at the expense of recombinase activity; substitution of Asp-316 with lysine (HsRAD51-D316K) decreases NPF turnover and markedly improves strand exchange activity in the absence of salt. | PMID:22275364 | The Journal of biological chemistry |
| 2011 | Medium | Yeast Rad51 is phosphorylated on Ser192 in a DNA-damage-responsive manner primarily mediated by the Mec1 kinase; Ser192 Ala and Glu mutations confer hypersensitivity to DNA damage and homologous recombination defects. Ser192 is required for Rad51 ATPase activity and DNA-binding activity in vitro but not for multimer formation. | PMID:21738226 | EMBO reports |
| 2013 | Medium | The HsRAD51B-HsRAD51C heterodimer forms a stable complex on ssDNA and partially stabilizes HsRAD51 nucleoprotein filaments against BLM helicase anti-recombinogenic activity; HsRAD51B-HsRAD51C also stimulates HsRAD51-mediated D-loop formation in the presence of RPA but does not facilitate RAD51 nucleation on RPA-coated ssDNA. | PMID:23810717 | DNA repair |
| 2022 | Medium | TOPORS acts as a SUMO E3 ligase that SUMOylates RAD51 at lysine residues 57 and 70 in response to DNA damage; TOPORS SUMOylation is facilitated by ATM-induced phosphorylation of TOPORS at Thr515. SUMOylation of RAD51 is required for its chromatin recruitment and homologous recombination repair; SUMOylation-deficient RAD51 has reduced association with BRCA2. | PMID:35061896 | Nucleic acids research |
| 2021 | Medium | RAD51 protects under-replicated DNA in mitotic cells and promotes mitotic DNA synthesis (MiDAS) and successful chromosome segregation; MiDAS requires de novo RAD51 recruitment to ssDNA supported by Polo-like kinase 1 (PLK1)-mediated phosphorylation of RAD51. Acute inhibition of MiDAS delays anaphase onset and induces centromere fragility. | PMID:34508092 | Nature communications |
| 2023 | High | BRCA2's C-terminal TR2 motif binds across the protomer interface in the RAD51 nucleoprotein filament, acting as a brace for adjacent RAD51 molecules by targeting an acidic-patch motif on RAD51; structure-guided mutagenesis validated the functional importance of this interaction for filament stabilization. | PMID:37919288 | Nature communications |
| 2023 | High | BRCA2 accelerates nucleation of RAD51 onto RPA-coated ssDNA to a rate approaching RAD51 association with naked ssDNA, eliminating the rate-limiting nucleation step by chaperoning a short preassembled RAD51 filament onto the ssDNA; a RAD51 dimer is the minimal unit required for spontaneous nucleation but growth self-terminates below the diffraction limit in the absence of BRCA2. | PMID:36976771 | Proceedings of the National Academy of Sciences of the United States of America |
| 2024 | High | RAD51 nucleofilaments specifically recognize and protect abasic sites in ssDNA; abasic sites increase the RAD51 association rate to DNA. In the absence of BRCA2 or RAD51, abasic sites accumulate and induce abasic ssDNA gaps that make replicating DNA fibers sensitive to APE1. RAD51 assembled on abasic DNA prevents cleavage by the MRE11-RAD50 complex, suppressing replication fork breakage. | PMID:39178838 | Molecular cell |
| 2021 | Medium | RAD51 physically interacts with TERRA lncRNA and catalyzes R-loop formation with TERRA in vitro, directly promoting TERRA recruitment to telomeres by strand invasion in trans; this process is counteracted by RNaseH1 and TRF1. | PMID:33057192 | Nature |
| 2021 | Medium | RAD51 helicase HELQ is strongly stimulated by RAD51 during DNA unwinding via direct complex formation; conversely, RPA inhibits HELQ DNA unwinding but stimulates its DNA strand annealing activity. | PMID:34937945 | Nature |
| 2021 | Medium | FANCD2, independent of FANCI dimerization, stabilizes RAD51 filaments to inhibit DNA2, MRE11, and EXO1 nucleases at stalled replication forks; additionally, FANCD2 acts as a RAD51 mediator to stimulate RAD51 strand exchange activity, providing a mechanistic link between FANCD2 and BRCA2 in the FA/BRCA fork protection pathway. | PMID:37526271 | Nucleic acids research |
| 1998 | Medium | HsRad51 is proteolytically cleaved during apoptosis in human T-lymphocyte cell lines with similar kinetics to PARP cleavage; cleavage is blocked by the caspase inhibitor Ac-DEVD-CHO, implicating a DEVD-specific caspase, though purified caspases 2, 3, or 6-10 could not individually cleave HsRad51 in vitro. | PMID:9607320 | FEBS letters |
| 2001 | Medium | Depletion of HsRad51 from human cell-free extracts diminishes triplex-induced recombination, and supplementation with purified HsRad51 restores it, establishing that HsRad51 is required for triplex-induced intermolecular recombination in human cell extracts. | PMID:11278954 | The Journal of biological chemistry |
| 2022 | Medium | RAD51 Cys319 is a functionally significant redox-regulated site; oxidation of Cys319 disrupts DNA binding (molecular dynamics simulations show DNA dissociation from oxidized Cys319 RAD51 filament). Peroxiredoxin 1 (PRDX1) maintains Cys319 in a reduced state, and loss of PRDX1 leads to increased sulfenylation of RAD51 Cys319, impaired RAD51 foci formation, and decreased homologous recombination. | PMID:36058112 | Redox biology |
| 2023 | Medium | Centromeric DNA breaks in quiescent human cells are resolved enzymatically by RAD51 recombinase, which safeguards the specification of functional centromeres. | PMID:36702125 | Molecular cell |
| 2021 | Medium | RAD51 protects replication forks from transcription-replication conflicts (TRCs); RAD51-deficient regions enriched for early-S-phase replication and transcription show increased fork breakage, and inhibiting early S-phase transcription ameliorates many adverse effects of RAD51 depletion. | PMID:36002000 | Molecular cell |
| 2021 | High | Cryo-EM structures of human RAD51-DNA complexes reveal that Loop2 residues V273 and D274 in RAD51 (vs. P274 and G275 in DMC1) are key determinants of mismatch intolerance during strand exchange; these differences in Loop2 that contact both ssDNA and the complementary strand explain why RAD51 does not permit HR in the presence of mismatches whereas DMC1 does. | PMID:34871438 | Nucleic acids research |
| 2023 | High | In vivo, Rad51-ssDNA nucleoprotein filaments in budding yeast span the entire nucleus following DSB induction, adopting diverse shapes not seen in vitro; the filaments undergo cycles of compaction and extension modulated by Rad54 (promotes extension) and Srs2 (promotes compaction), and this compaction-extension dynamic constitutes a robust nuclear homology search strategy. | PMID:37605042 | Nature structural & molecular biology |
| 2020 | Medium | Rad51 facilitates Dmc1 nucleoprotein filament assembly during meiosis through direct physical interaction; Dmc1 nucleation is stimulated by short Rad51 patches on DNA, and pull-down assays confirm a physical interaction between ScDmc1 and ScRad51 but not between ScDmc1 and EcRecA. | PMID:32404423 | Proceedings of the National Academy of Sciences of the United States of America |
| 2018 | Medium | Rad51 and Dmc1 have an intrinsic ability to self-segregate within mixed presynaptic filaments in vitro, without any accessory proteins; Dmc1 stabilizes adjacent Rad51 filament segments, suggesting cross-talk between the two recombinases. | PMID:29382724 | The Journal of biological chemistry |
| 2017 | Medium | Human RAD52 binds tightly to RPA-ssDNA and imposes an inhibitory effect on RPA turnover; during RAD51 presynaptic complex assembly, most RPA and RAD52 are displaced but some RAD52-RPA-ssDNA clusters persist interspersed within RAD51 filaments; once RAD51 filament assembles, it restricts new RAD52 binding events but RAD52 re-binds after RAD51 dissociation. | PMID:28551686 | The Journal of biological chemistry |
| 1998 | Medium | BRCA2 gene product forms in vivo complexes with both RAD51 and p53 in human cells; BRCA2 is a nuclear phosphoprotein, and exogenous BRCA2 expression inhibits p53's transcriptional activity with RAD51 coexpression enhancing this inhibitory effect. | PMID:9811893 | Proceedings of the National Academy of Sciences of the United States of America |

## Citations

- PMID:10448035
- PMID:10749867
- PMID:10908572
- PMID:11278954
- PMID:14993274
- PMID:15937124
- PMID:17567608
- PMID:18337252
- PMID:18617519
- PMID:19447914
- PMID:20729832
- PMID:21738226
- PMID:22275364
- PMID:23810717
- PMID:24943459
- PMID:26186187
- PMID:26811421
- PMID:27694619
- PMID:28334891
- PMID:28551686
- PMID:29382724
- PMID:30021152
- PMID:32404423
- PMID:32621611
- PMID:33057192
- PMID:33453169
- PMID:34508092
- PMID:34871438
- PMID:34937945
- PMID:35061896
- PMID:36002000
- PMID:36058112
- PMID:36702125
- PMID:36976771
- PMID:37104614
- PMID:37526271
- PMID:37605042
- PMID:37919288
- PMID:39178838
- PMID:9012806
- PMID:9450758
- PMID:9450760
- PMID:9590697
- PMID:9607320
- PMID:9811893
