# MAPK7 (ERK5 / BMK1) curation notes

UniProt Q13164, human, 816 aa. CMGC Ser/Thr kinase, MAP kinase subfamily (PANTHER PTHR24055).

## Identity and architecture

- Cloned independently as BMK1 and ERK5 in 1995. BMK1 "has the dual phosphorylation site of MAP
  kinases characterized by the TEY sequence found in ERK1 and ERK2, it has a distinct C-terminal and
  loop-12 structure" [PMID:7646528 "Although BMK1 has the dual phosphorylation site of MAP kinases characterized by the TEY sequence found in ERK1 and ERK2"].
- ERK5 was found as a specific two-hybrid partner of MEK5 and does not bind MEK1/2
  [PMID:7759517 "ERK5 did not interact with MEK1 or MEK2"].
- UniProt features: kinase domain 55-347, TXY motif 219-221, MAP2K5-binding region 78-139,
  NLS 505-539, long disordered C-terminal tail (406-806). UniProt SUBUNIT: interacts with MAP2K5,
  MEF2A/C/D, SGK1, PML, HSP90AB1-CDC37, STUB1 [file:human/MAPK7/MAPK7-uniprot.txt].

## Molecular function

- MAP kinase activity: MEK5 is the dedicated MAP2K; activated ERK5 phosphorylates MEF2C Ser387
  [PMID:9384584 "BMK1 dramatically enhances the transactivation activity of MEF2C by phosphorylating a serine residue at amino acid position 387 in this transcription factor"],
  SGK1 Ser78 [PMID:11254654 "BMK1 activates SGK by phosphorylation at serine 78"], and PML
  [PMID:20832753 "inhibited its tumor-suppressor function through phosphorylation"].
- Transcriptional coactivator: the C-terminal tail contains a MEF2-interacting domain and a potent
  transcriptional activation domain required for MEF2D coactivation
  [PMID:11046135 "the C-terminal region of ERK5 contains a MEF2-interacting domain and, surprisingly, also a potent transcriptional activation domain"].
  Lochhead 2020 describes ERK5 as a "dual protein kinase-transcription factor"; kinase inhibitors
  paradoxically activate the TAD [PMID:32170057].
  -> Candidate NEW MF: GO:0003713 transcription coactivator activity. Participation test: ERK5 itself
  supplies the activation domain (it does the work), and binds MEF2 directly (MADS/MEF2 domain;
  [PMID:9753748]). Comparator: other coactivators binding MEF2 (e.g. EP300, NCOA2) carry
  GO:0003713; kinases are not annotated with it by default, but ERK5 is unusual in having a TAD.
- MEF2 binding: direct binding to MEF2 MADS/MEF2 domain [PMID:9753748 "The interacting domain of MEF2 was mapped to the N-terminus which contains the highly conserved MADS and MEF2 domains"].
  -> DNA-binding transcription factor binding (GO:0140297) as replacement for bare protein binding with MEF2A.

## Localization

- Cytoplasmic in resting cells bound to HSP90-CDC37; activation causes Hsp90 dissociation and nuclear
  translocation [PMID:23428871 "activation of cellular ERK5 induces Hsp90 dissociation from the ERK5-Cdc37 complex, leading to ERK5 nuclear translocation and activation of transcription"].
- Activated BMK1 colocalizes with PML in PML nuclear bodies [PMID:20832753 "activated BMK1 is colocalized with PML in the PML-NBs"].

## Pathway / processes

- ERK5 cascade (GO:0070375): MEKK2/3 -> MEK5 -> ERK5. EGF activates Bmk1 Ras-independently via MEK5
  [PMID:9790194 "EGF-mediated activation of Bmk1 occurs independently of Ras and requires the MAP-kinase kinase Mek5"].
  GOA human MAPK7 lacks GO:0070375 (rat Mapk7 has it by IMP, PMID:11782488); the ISS "MAPK cascade"
  annotation transferred from rat P0C865 should be refined to ERK5 cascade.
- Endothelial integrity/survival: global Erk5 KO lethal E9.5-10.5 with vascular and cardiac defects
  [PMID:12093914 "Inactivation of the erk5 gene resulted in defective blood-vessel and cardiac development leading to embryonic lethality around embryonic days 9.5-10.5"];
  adult deletion causes leaky vessels and endothelial apoptosis, endothelial-specific KO phenocopies
  global KO [PMID:15085193 "the data provide direct genetic evidence that the BMK1 pathway is critical for endothelial function and for maintaining blood vessel integrity"].
- Shear stress: laminar flow activates ERK5 -> Nrf2 [PMID:23043106]; MEK5D-driven Erk5 activation
  induces KLF4 and a vasoprotective (anti-apoptotic, anti-inflammatory) endothelial phenotype
  [PMID:20551324 "We identify KLF4 as a novel Erk5 target and demonstrate a critical role of this transcription factor downstream of Erk5"].
- Cardiomyocyte survival via STUB1/CHIP-mediated ICER degradation [PMID:20724525] (mouse/rat).
- PML/p53: activated BMK1 disrupts PML-MDM2 interaction [PMID:22869143].
- TGF-beta activates ERK5 in renal PTEC (ALK5 dependent) [PMID:18588859].
- mAKAP complex (rat cardiomyocytes): ERK5 recruited via PDE4D3, phosphorylates and suppresses PDE4D3;
  cAMP/Epac1/Rap1 attenuates ERK5 [PMID:16177794]. Note: this is kinase-mediated inhibition, not
  "enzyme inhibitor activity"; ERK5 is regulated by cAMP but is not a component of Gs-coupled GPCR
  signalling.

## Judgement calls

- GO:0051019 MAPK binding (IPI, PMID:23043106) has WITH = NFE2L2 (Q16236), which is not a MAPK. The
  interaction ERK5-Nrf2 is real (abstract: "Molecular interaction between ERK5 and Nrf2 was further
  induced by laminar flow"), so MODIFY to DNA-binding transcription factor binding rather than REMOVE.
- Protein binding: MAP2K5 partners -> MAPKK binding (GO:0031434) as in MAPK14/MAPK1; HSP90AB1/CDC37 ->
  Hsp90 protein binding (GO:0051879); MEF2A -> GO:0140297; PML (a substrate) and HT-only partners
  (BAG2, UBE2C, ZKSCAN1, CCDC6, BRAF) -> REMOVE (uninformative; the interaction is not claimed false).
- Enzyme inhibitor activity (NAS) -> REMOVE; AC-activating GPCR signalling (NAS) -> REMOVE.
