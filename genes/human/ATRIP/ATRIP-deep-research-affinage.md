---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ATRIP
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q8WXE1
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 29
citation_count: 29
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ATRIP (human)

## Current model (mechanistic narrative)

ATRIP is the obligate regulatory partner of the ATR kinase, and the two proteins are mutually dependent for stable expression and for mounting DNA damage checkpoint responses [PMID:11721054]. ATRIP localizes the complex to sites of genotoxic stress: its N-terminal checkpoint recruitment domain (CRD) directly binds RPA-coated ssDNA, the structure that recruits ATR-ATRIP to DNA damage and stimulates downstream checkpoint kinase activity [PMID:12791985, PMID:17339343]. RPA-ssDNA engagement is mediated by multiple, redundant interactions flanking the conserved coiled-coil, which itself drives ATRIP homo-oligomerization required for stable ATR binding and accumulation at lesions; oligomerization per se, rather than the specific coiled-coil sequence, is the essential feature [PMID:16027118, PMID:16407120]. Structurally, ATR-ATRIP assembles as a heart-shaped dimer of heterodimers in which an extended HEAT-repeat ATRIP locks the N-termini of two ATR monomers [PMID:29271416]. Once recruited, the complex is allosterically activated by TopBP1, which engages a dedicated TopBP1-interacting region in ATRIP that cooperates with the ATR PIKK regulatory domain (PRD) to switch on kinase activity, enabling phosphorylation of Chk1 and other substrates [PMID:16530042, PMID:18519640]. Distinct ATRIP domains route the complex to distinct outputs: the RPA-binding region supports FANCD2 monoubiquitination and FANCI phosphorylation in the Fanconi anemia pathway, whereas full Chk1 activation requires both the RPA- and TopBP1-binding regions [PMID:22258451]. ATRIP activity is further tuned by post-translational modifications, including CDK2-cyclin A phosphorylation at S224 controlling G2/M checkpoint maintenance, SIRT2-dependent K32 deacetylation promoting RPA-ssDNA binding, and SUMO2/3 modification at K234/K289 enabling coordinated assembly with ATR, RPA, TopBP1, and MRN [PMID:17638878, PMID:26854234, PMID:24990965], and by interacting partners that act as positive regulators (Nek1, ZFP161) or as a negative regulator (REV7, which directly binds ATRIP to inhibit ATR kinase activity) [PMID:23345434, PMID:31757956, PMID:41562258].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0003677 DNA binding, GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005634 nucleus, GO:0000228 nuclear chromosome
- **pathway (Reactome):** R-HSA-73894 DNA Repair, R-HSA-1640170 Cell Cycle, R-HSA-8953897 Cellular responses to stimuli
- **partners:** ATR, RPA70, TOPBP1, NEK1, REV7, ZFP161, BRCA1, MCM2
- **complexes:** ATR-ATRIP

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2001 | High | ATRIP is an ATR-interacting protein that is phosphorylated by ATR, regulates ATR expression, and is mutually dependent with ATR for stable expression; siRNA knockdown of ATRIP causes loss of both ATRIP and ATR protein and abolishes DNA damage checkpoint responses, establishing ATR and ATRIP as obligate partners. | PMID:11721054 | Science |
| 2003 | High | RPA-coated ssDNA is the critical structure that recruits the ATR-ATRIP complex to sites of DNA damage; ATRIP directly binds RPA-ssDNA in vitro, enabling ATR-ATRIP to associate with DNA and stimulate phosphorylation of Rad17; the yeast ATRIP ortholog Ddc2 is recruited to DSBs in an RPA-dependent manner, and the checkpoint-deficient RPA mutant rfa1-t11 is defective for recruiting Ddc2 both in vivo and in vitro. | PMID:12791985 | Science |
| 2004 | Medium | ATR exists as a monomer associated with ATRIP with moderate affinity; ATRIP stimulates ATR-mediated phosphorylation of RPA in a ssDNA-dependent manner, but both ATR alone and the ATR-ATRIP heterodimer bind naked or RPA-covered DNA with comparable affinities. | PMID:14729973 | Molecular and cellular biology |
| 2004 | Medium | ATR-ATRIP complex can bind ssDNA in two modes: a high-affinity RPA-dependent mode and a lower-affinity RPA-independent mode that requires an additional unidentified protein from HeLa nuclear extract; neither ATR nor ATRIP can bind DNA individually in this low-affinity mode. | PMID:14724280 | The Journal of biological chemistry |
| 2004 | Medium | ATR-mediated phosphorylation of ATRIP at Ser-68 and Ser-72 occurs in response to genotoxic stimuli; phosphorylated ATRIP accumulates at DNA damage foci, but this phosphorylation is dispensable for ATRIP relocalization to foci and activation of downstream effectors. | PMID:15451423 | Biochemical and biophysical research communications |
| 2004 | High | ATR-ATRIP and Claspin collaborate in a multistep process for Chk1 activation: ATR-ATRIP bound to ssDNA/dsDNA junction templates shows higher kinase activity than on ssDNA alone, and Claspin strongly stimulates phosphorylation of Chk1 by activated ATR-ATRIP. | PMID:15371427 | The Journal of biological chemistry |
| 2004 | Medium | The N-terminal domain of ATRIP contributes to intranuclear relocalization to DNA damage-induced foci in an RPA-dependent manner even without ATR association, suggesting an ATR-independent localization function for this domain. | PMID:15527801 | FEBS letters |
| 2005 | High | The N-terminal domain of ATRIP is necessary and sufficient for interaction with RPA-ssDNA and for ATRIP accumulation into damage-induced foci; however, the ATRIP-RPA-ssDNA interaction is not absolutely essential for ATR activation because Chk1 phosphorylation occurs in cells expressing an ATRIP mutant that cannot bind RPA-ssDNA; ATR association is also required for proper ATRIP localization. | PMID:15743907 | Molecular biology of the cell |
| 2005 | High | ATRIP binding to ATR is required for ATR to efficiently phosphorylate Chk1 in Xenopus egg extracts; stable DNA-binding domain and coiled-coil domain of ATRIP are dispensable for Chk1 phosphorylation on defined checkpoint-inducing templates; ATRIP adopts an oligomeric state in egg extracts dependent on binding to ATR. | PMID:16186122 | The Journal of biological chemistry |
| 2005 | High | The coiled-coil domain of ATRIP mediates ATRIP homodimerization/homo-oligomerization; this domain is essential for oligomerization, stable ATR binding, and accumulation of ATRIP at DNA lesions; replacing the coiled-coil with a heterologous dimerization domain restores stable ATR binding and localization, demonstrating that oligomerization per se (not the specific coiled-coil sequence) is required for ATR-dependent checkpoint signaling to Chk1. | PMID:16027118 | The Journal of biological chemistry |
| 2005 | Medium | The coiled-coil domain of ATRIP mediates self-dimerization in vivo and is required for stable translocation of the ATR-ATRIP complex to nuclear foci after genotoxic stress; dimerization-defective ATRIP compromises maintenance of replication forks during replication inhibitor treatment but does not impair the G2/M checkpoint after IR, revealing separable ATR-ATRIP functions. | PMID:16176973 | Molecular biology of the cell |
| 2006 | High | TopBP1 activates the ATR-ATRIP kinase complex; recombinant TopBP1 induces a large increase in ATR kinase activity in both Xenopus and human systems; the ATR-activating domain of TopBP1 is a conserved segment distinct from BRCT repeats; a point mutation inactivating this domain renders egg extracts defective in checkpoint regulation. | PMID:16530042 | Cell |
| 2006 | Medium | ATRIP associates with RPA-ssDNA through multiple interactions: two major RPA-ssDNA-interacting domains flank the conserved coiled-coil domain; one internal region of ATRIP exhibits direct affinity for ssDNA; the N-terminus associates with RPA-ssDNA in two distinct ways, indicating dynamic and redundant interactions. | PMID:16407120 | Proceedings of the National Academy of Sciences of the United States of America |
| 2007 | High | A conserved checkpoint recruitment domain (CRD) at the N-terminus of ATRIP mediates the RPA interaction; mutations in the CRD of Saccharomyces cerevisiae Ddc2 disrupt Ddc2-RPA interaction, prevent proper localization to DNA breaks, sensitize yeast to DNA-damaging agents, and partially compromise checkpoint signaling; TopBP1-mediated ATR activation can occur independently of ATRIP-RPA interaction. | PMID:17339343 | Molecular and cellular biology |
| 2007 | High | CDK2-cyclin A phosphorylates ATRIP at S224 in vitro and in cells in a cell cycle-dependent manner; mutation of S224 to alanine causes a defect in ATR-ATRIP-dependent G2/M checkpoint maintenance after IR and UV radiation. | PMID:17638878 | Cancer research |
| 2008 | High | ATRIP contains a TopBP1-interacting region required for TopBP1-ATR association and TopBP1-mediated ATR activation; ATR contains a PIKK Regulatory Domain (PRD) that is critical for activation by TopBP1 (mutations abolish activation without affecting basal kinase activity); both are required for checkpoint signaling and cellular viability after replication stress; the ATRIP TopBP1-interacting region is functionally conserved in yeast Ddc2. | PMID:18519640 | Genes & development |
| 2012 | High | ATRIP is crucial for DNA damage-induced FANCD2 monoubiquitination and FANCI phosphorylation; ATR phosphorylates recombinant FANCI in vitro, facilitated by FANCD2; the RPA-binding region of ATRIP (but not the TopBP1-binding region) is required for FANCD2 monoubiquitination, whereas Chk1 phosphorylation requires both domains. | PMID:22258451 | Cancer research |
| 2013 | High | Nek1 kinase associates with ATR-ATRIP, maintains ATRIP protein levels, and promotes ATR-ATRIP association and basal ATR kinase activity even in undamaged cells; upon DNA damage, Nek1 is required for efficient phosphorylation of ATR substrates and ATR autophosphorylation at T1989; Nek1's promotion of ATR activation requires Nek1 kinase activity and its interaction with ATR-ATRIP. | PMID:23345434 | Proceedings of the National Academy of Sciences of the United States of America |
| 2013 | Medium | The FA core complex enhances ATRIP binding and localization within damaged chromatin; in FA core complex-deficient cells, ATR-mediated phosphorylation of both ATRIP and FANCI is defective; canonical ATR activation via RAD17 and TOPBP1 is largely dispensable for FA pathway activation. | PMID:23723247 | Nucleic acids research |
| 2013 | High | The BRCA1 BRCT domains bind an ATRIP phosphopeptide (pS238-containing motif 235-PEACpSPQFG-243); crystal structures at 1.75 Å resolution reveal that pSer and Phe(+3) anchor the ATRIP peptide into the BRCT binding groove, with Gln(+2) accommodated through a conformational change of BRCA1 E1698. | PMID:24073851 | Biochemistry |
| 2014 | High | ATRIP is SUMOylated by SUMO2/3 at K234 and K289; an ATRIP SUMOylation mutant fails to localize efficiently to DNA damage sites and support ATR activation; SUMOylation promotes simultaneous interaction with multiple ATRIP partners including ATR, RPA70, TopBP1, and the MRE11-RAD50-NBS1 complex, and these partners display affinity for SUMO2 chains in vitro; fusion of a SUMO2 chain to the ATRIP SUMOylation mutant partially rescues its defects. | PMID:24990965 | Genes & development |
| 2016 | High | SIRT2 deacetylates ATRIP at lysine K32 in response to replication stress; K32 deacetylation by SIRT2 promotes ATRIP accumulation at DNA damage sites, binding to RPA-ssDNA, ATR autophosphorylation, and ATR checkpoint signaling, as well as DNA replication fork progression and recovery. | PMID:26854234 | Cell reports |
| 2017 | High | Cryo-EM structure of the human ATR-ATRIP complex at 4.7 Å overall (3.9 Å for ATR C-terminal catalytic core) reveals a hollow 'heart'-shaped dimer of heterodimers; ATRIP contains 14 HEAT repeats in an extended 'S' shape; conformational flexibility of ATR allows ATRIP to lock the N-termini of two ATR monomers; catalytic pockets face outward without inhibitory occlusion. | PMID:29271416 | Cell research |
| 2017 | High | Cryo-EM structure of yeast Mec1-Ddc2 (ATR-ATRIP ortholog) at 3.9 Å reveals the complex forms a dimer of heterodimers through Mec1 PRD/FAT domains and the Ddc2 coiled-coil domain; the PRD inhibits the Mec1 activation loop, establishing an allosteric mechanism of kinase activation; PRD and Bridge domains constitute critical regulatory sites. | PMID:29191911 | Science |
| 2019 | Medium | ZFP161 acts as a scaffolding protein that facilitates interaction between RPA and ATR/ATRIP; ZFP161 binds RPA and ATR/ATRIP through distinct regions and stabilizes the RPA-ATR-ATRIP complex at stalled replication forks, promoting ATR-Chk1 signaling. | PMID:31757956 | Nature communications |
| 2017 | Medium | ATRIP directly interacts with MCM2, MCM3, MCM6, and MCM7; downregulation of MCM2 and MCM6 significantly reduces ATRIP chromatin loading; downregulation of MCM2 decreases ATRIP phosphorylation at S224 in a dose-dependent manner. | PMID:29442041 | Die Pharmazie |
| 2023 | Medium | APE1 directly associates with ssDNA and recruits ATRIP onto ssDNA in an RPA-independent manner; the N-terminal motif of APE1 is required and sufficient for APE1-ATRIP interaction in vitro; this APE1-ATRIP interaction is required for ATRIP recruitment to ssDNA and ATR-Chk1 DDR pathway activation in Xenopus egg extracts; APE1 also directly associates with RPA70 and RPA32 via two distinct motifs. | PMID:37216274 | eLife |
| 2025 | High | REV7 directly binds ATRIP through a defined REV7-interaction motif in ATRIP; mutation of this motif abrogates the REV7-ATRIP interaction in vitro and in cells; REV7 inhibits ATR-mediated phosphorylation of substrates including p53 in vitro; disruption of the REV7-ATRIP interaction enhances CHK1 phosphorylation at Ser317 in cells, establishing REV7 as a negative regulator of ATR signaling. | PMID:41562258 | Nucleic acids research |
| 2025 | High | Cryo-EM structures of human ATR-ATRIP complex at ~3 Å overall resolution in the presence of ATR inhibitors VE-822 and RP-3500 reveal near-complete atomic model including subunit stoichiometry (dimer of heterodimers), intramolecular and intermolecular interactions, and PRD regulatory insertion; one ATR-ATRIP complex binds four VE-822 molecules (two in active site, two at ATR-ATR dimer interface); RP-3500 binding depends on two bound water molecules. | PMID:40379520 | Science bulletin |

## Citations

- PMID:11721054
- PMID:12791985
- PMID:14724280
- PMID:14729973
- PMID:15371427
- PMID:15451423
- PMID:15527801
- PMID:15743907
- PMID:16027118
- PMID:16176973
- PMID:16186122
- PMID:16407120
- PMID:16530042
- PMID:17339343
- PMID:17638878
- PMID:18519640
- PMID:22258451
- PMID:23345434
- PMID:23723247
- PMID:24073851
- PMID:24990965
- PMID:26854234
- PMID:29191911
- PMID:29271416
- PMID:29442041
- PMID:31757956
- PMID:37216274
- PMID:40379520
- PMID:41562258
