# TtgB Notes

## Gene Overview

TtgB (PP_1385, Q88N31) is the inner membrane RND (Resistance-Nodulation-Division) transporter component of the TtgABC tripartite efflux pump in *Pseudomonas putida* KT2440. It is a 1050 AA protein with 12 predicted transmembrane helices, belonging to the acriflavine resistance protein family (IPR001036) and specifically the MdtF-like subfamily (IPR004764). It is homologous to AcrB in *E. coli* and MexB in *P. aeruginosa*.

## TtgABC System Architecture

The TtgABC efflux pump is a tripartite system typical of RND family transporters:
- **TtgA** (PP_1384): Membrane fusion protein (MFP/periplasmic adaptor)
- **TtgB** (PP_1385): Inner membrane RND transporter (proton-dependent substrate extrusion)
- **TtgC** (PP_1386): Outer membrane factor (OMF/channel)

The three genes form an operon, transcribed from a single promoter upstream of ttgA. Expression is constitutive but regulated by the TtgR repressor (PP_1387), which is transcribed divergently from ttgA [PMID:11251828 "TtgR represses expression from the ttgA promoter... expression from the ttgA promoter increased about 20-fold in TtgR-deficient background"].

## Substrate Specificity and Function

### Organic Solvents
In DOT-T1E strain, TtgABC extrudes toluene, styrene, m-xylene, ethylbenzene, and propylbenzene [PMID:11395460 "TtgABC and TtgGHI pumps extruded toluene, styrene, m-xylene, ethylbenzene, and propylbenzene"]. However, in KT2440 this operon may not function primarily in toluene efflux [UniProt CAUTION: "In KT2400 this operon does not seem to function in toluene efflux"].

### Antibiotics
TtgABC confers resistance to multiple antibiotics in KT2440:
- Chloramphenicol: TtgABC knockout is compromised [PMID:22143519 "survival of a knockout mutant in the TtgABC RND efflux pump... were compromised in the presence of chloramphenicol"]
- Fluoroquinolones and beta-lactams: Overexpression of TtgABC via TtgR mutations leads to increased resistance [PMID:32840000 "Mutants of the first type were more resistant to fluoroquinolones and β-lactams except imipenem, and overproduced the efflux system TtgABC"]
- Also quinolones, sulfonamides [PMID:24907323]
- Indole induces ttgABC expression contributing to ampicillin resistance [PMID:28352264]

### Plant Antimicrobials and Bipyridyls
- TtgR binds phloretin and other plant antimicrobials, releasing TtgABC expression [PMID:17466326]
- TtgABC is required for detoxification of bipyridyl compounds (e.g., caerulomycin A) [PMID:32973714 "deletion of ttgB made the strain susceptible to 2,2'-bipyridyl and natural bipyridyl derivatives such as caerulomycin A"]
- Also involved in resistance to bile salts and deoxycholate [PMID:32973714]

### Multidrug Binding
TtgB itself has been shown to possess multidrug-binding capacity [PMID:17498746 "TtgR and the TtgB efflux pump proteins possess multidrug-binding capacity, and their concerted action is responsible for the multidrug resistance phenotype"].

## Additional Roles Beyond Efflux

### Biofilm Formation
Knockout of ECF-10 sigma factor leads to upregulation of ttgABC and enhanced biofilm formation, suggesting TtgABC plays a role in biofilm development [PMID:24907323 "indicating a new role for this efflux pump beyond simple antibiotic resistance in P. putida KT2440"].

### Ion Homeostasis
In the absence of TtgABC, bipyridyl compounds interfere with metal ion homeostasis, affecting copper availability and pyoverdine (siderophore) production [PMID:32973714 "the addition of copper restores the growth of the ttgB mutant and the production of pyoverdine"].

## Regulatory Context

- **TtgR**: Adjacent repressor, binds pseudo-palindromic operator overlapping ttgR/ttgA promoters. Released by effectors including antibiotics and plant antimicrobials [PMID:11251828, PMID:17466326, PMID:20435893]
- **ECF-10 (PP4553)**: Knockout leads to ttgABC upregulation [PMID:24907323]
- **PpeRS**: Two-component system positively controls TtgABC expression [PMID:32840000]
- **Lrp-like**: Global regulator involved in solvent-tolerant response [PMID:11251828]

## Key Distinction: KT2440 vs DOT-T1E

The UniProt entry is for KT2440. The caution note indicates that while the homologous system in DOT-T1E functions in solvent efflux, in KT2440 it primarily functions in antibiotic resistance, bipyridyl detoxification, and potentially biofilm formation. The proteins are highly similar but expression levels and ecological context differ.

## Homologous Systems
- **MepABC** (P. putida KT2442-TOL): Solvent and antibiotic efflux
- **ArpABC** (P. putida S12): Antibiotic efflux only, not solvent tolerance [PMID:11160799]
- **SrpABC** (P. putida B6-2): PAH degradation support [PMID:29030440]
- **AcrAB-TolC** (E. coli): Canonical RND efflux system
- **MexAB-OprM** (P. aeruginosa): Major multidrug efflux

## Energy Coupling
Proton-dependent, operates via proton motive force. Energy transfer may involve the TonB system [PMID:12142492].

## References
- PMID:9642183 - Original identification of TtgABC efflux pump in DOT-T1E (Ramos et al. 1998)
- PMID:10648517 - Second efflux system TtgDEF (Mosqueda & Ramos 2000)
- PMID:11160799 - ArpABC in S12 multidrug resistance (Kieboom & de Bont 2001)
- PMID:11251828 - TtgR regulation of TtgABC (Duque et al. 2001)
- PMID:11395460 - Three efflux pumps for toluene tolerance (Rojas et al. 2001)
- PMID:12142492 - Review of solvent tolerance mechanisms (Ramos et al. 2002)
- PMID:12534463 - KT2440 genome sequence (Nelson et al. 2002)
- PMID:12743835 - Comparative genomics of solvent extrusion pumps (Segura et al. 2003)
- PMID:16109935 - Proteomics of toluene response (Segura et al. 2005)
- PMID:17466326 - TtgR crystal structures with antibiotics/plant antimicrobials (Alguel et al. 2007)
- PMID:17498746 - TtgR operator binding cooperativity (Krell et al. 2007)
- PMID:17986203 - Cross-regulation of TtgV and TtgT (Teran et al. 2007)
- PMID:20435893 - TtgR domain cross-talk (Daniels et al. 2010)
- PMID:22143519 - Chloramphenicol resistance in KT2440 (Fernandez et al. 2011)
- PMID:24907323 - ECF-10 affects TtgABC, biofilm formation (Tettmann et al. 2014)
- PMID:28352264 - Indole-induced TtgABC and ampicillin resistance (Kim et al. 2017)
- PMID:29030440 - SrpABC/TtgABC in PAH degradation (Yao et al. 2017)
- PMID:32840000 - ParXY/TtgABC multidrug resistance (Puja et al. 2020)
- PMID:32973714 - TtgABC bipyridyl resistance in KT2440 (Henriquez et al. 2020)
