# PTHR11801 (STAT) tree and domain checks

Script: `tree_and_domain_checks.py` (run `python3 tree_and_domain_checks.py`; needs network
access to pantherdb.org and rest.uniprot.org). Data: PANTHER 19 treeinfo for PTHR11801 and
PTHR45807, and UniProt InterPro cross-references. Run date 2026-10-04.

## Findings

1. PTN000927860, which carries the GO:0007259 (JAK-STAT), GO:0006952 and GO:0042127 IBDs,
   is the Unikonts node: its descendants include the Dictyostelium STATs (SF65, SF50 and
   dstD in SF43) and all nematode STATs (SF49, SF68, and sta-1 in SF43), not only the
   bilaterian JAK-bearing lineages.
2. PTN000210448, which carries the nucleus, cytoplasm, GO:0000981, GO:0000978 and GO:0006357
   IBDs, is the Eukaryota root; its descendants include the Viridiplantae clade
   (Arabidopsis SHA and SHB, in SF43).
3. The PANTHER JAK family PTHR45807 (root PTN001975446, Eumetazoa) has no members in
   C. elegans, C. briggsae, P. pacificus, Dictyostelium discoideum, Arabidopsis or
   Nematostella. It does have members in Drosophila, Daphnia, sea urchin, Ciona,
   Branchiostoma, all vertebrates sampled and Trichoplax.
4. Arabidopsis SHA (B5X561) and SHB (Q56XZ1) carry no STAT DNA-binding-domain InterPro entry
   (IPR008967, IPR013801, IPR012345 or IPR037059). All other members checked, including the
   four Dictyostelium STATs and both C. elegans STATs, carry at least one.

## Raw output

```
== PTHR11801 PAINT nodes in the PANTHER tree
PTN000210448	taxon=Eukaryota	event=SPECIATION	node_SF=PTHR11801:SF43	leaves=225
   descendant SFs: {'PTHR11801:SF18': 22, 'PTHR11801:SF19': 17, 'PTHR11801:SF2': 27, 'PTHR11801:SF39': 25, 'PTHR11801:SF41': 20, 'PTHR11801:SF43': 66, 'PTHR11801:SF47': 12, 'PTHR11801:SF48': 18, 'PTHR11801:SF49': 3, 'PTHR11801:SF50': 2, 'PTHR11801:SF65': 6, 'PTHR11801:SF66': 2, 'PTHR11801:SF67': 3, 'PTHR11801:SF68': 2}
   has Dictyostelium: True | has Caenorhabditis: True | has plants (Arabidopsis): True
PTN000210451	taxon=Chordata	event=SPECIATION	node_SF=PTHR11801:SF43	leaves=147
   descendant SFs: {'PTHR11801:SF18': 22, 'PTHR11801:SF19': 17, 'PTHR11801:SF2': 27, 'PTHR11801:SF39': 25, 'PTHR11801:SF41': 20, 'PTHR11801:SF43': 4, 'PTHR11801:SF47': 12, 'PTHR11801:SF48': 18, 'PTHR11801:SF66': 2}
   has Dictyostelium: False | has Caenorhabditis: False | has plants (Arabidopsis): False
PTN000210452	taxon=None	event=DUPLICATION	node_SF=PTHR11801:SF43	leaves=143
   descendant SFs: {'PTHR11801:SF18': 22, 'PTHR11801:SF19': 17, 'PTHR11801:SF2': 27, 'PTHR11801:SF39': 25, 'PTHR11801:SF41': 20, 'PTHR11801:SF47': 12, 'PTHR11801:SF48': 18, 'PTHR11801:SF66': 2}
   has Dictyostelium: False | has Caenorhabditis: False | has plants (Arabidopsis): False
PTN000210582	taxon=Eutheria	event=SPECIATION	node_SF=PTHR11801:SF47	leaves=12
   descendant SFs: {'PTHR11801:SF47': 12}
   has Dictyostelium: False | has Caenorhabditis: False | has plants (Arabidopsis): False
PTN000927860	taxon=Unikonts	event=SPECIATION	node_SF=PTHR11801:SF43	leaves=180
   descendant SFs: {'PTHR11801:SF18': 22, 'PTHR11801:SF19': 17, 'PTHR11801:SF2': 27, 'PTHR11801:SF39': 25, 'PTHR11801:SF41': 20, 'PTHR11801:SF43': 24, 'PTHR11801:SF47': 12, 'PTHR11801:SF48': 18, 'PTHR11801:SF49': 3, 'PTHR11801:SF50': 2, 'PTHR11801:SF65': 6, 'PTHR11801:SF66': 2, 'PTHR11801:SF68': 2}
   has Dictyostelium: True | has Caenorhabditis: True | has plants (Arabidopsis): False
PTN002623821	taxon=Euteleostomi	event=SPECIATION	node_SF=PTHR11801:SF41	leaves=20
   descendant SFs: {'PTHR11801:SF41': 20}
   has Dictyostelium: False | has Caenorhabditis: False | has plants (Arabidopsis): False
PTN002623830	taxon=Euteleostomi	event=SPECIATION	node_SF=PTHR11801:SF18	leaves=22
   descendant SFs: {'PTHR11801:SF18': 22}
   has Dictyostelium: False | has Caenorhabditis: False | has plants (Arabidopsis): False
PTN002623841	taxon=Euteleostomi	event=SPECIATION	node_SF=PTHR11801:SF2	leaves=27
   descendant SFs: {'PTHR11801:SF2': 27}
   has Dictyostelium: False | has Caenorhabditis: False | has plants (Arabidopsis): False
PTN002623856	taxon=Euteleostomi	event=SPECIATION	node_SF=PTHR11801:SF39	leaves=57
   descendant SFs: {'PTHR11801:SF39': 25, 'PTHR11801:SF47': 12, 'PTHR11801:SF48': 18, 'PTHR11801:SF66': 2}
   has Dictyostelium: False | has Caenorhabditis: False | has plants (Arabidopsis): False

== PTHR45807 (JAK) organisms represented; root PTN001975446 (Eumetazoa)
   3	Anolis carolinensis
   4	Bos taurus
   1	Branchiostoma floridae
   4	Canis lupus familiaris
   2	Ciona intestinalis
   5	Danio rerio
   1	Daphnia pulex
   1	Drosophila melanogaster
   4	Equus caballus
   4	Felis catus
   5	Gallus gallus
   4	Gorilla gorilla gorilla
   4	Homo sapiens
   5	Macaca mulatta
   3	Monodelphis domestica
   4	Mus musculus
   4	Ornithorhynchus anatinus
   5	Oryzias latipes
   4	Pan troglodytes
   4	Rattus norvegicus
   1	Strongylocentrotus purpuratus
   4	Sus scrofa
   1	Trichoplax adhaerens
   6	Xenopus laevis
   4	Xenopus tropicalis
   4	lepisosteus oculatus
   JAK members in Caenorhabditis elegans: 0
   JAK members in Caenorhabditis briggsae: 0
   JAK members in Pristionchus pacificus: 0
   JAK members in Dictyostelium discoideum: 0
   JAK members in Arabidopsis thaliana: 0
   JAK members in Nematostella vectensis: 0

== InterPro cross-references (STAT DNA-binding-domain entries marked *)
P40763	STAT3	DNA-binding domain entry: True
   IPR008967* p53-like_TF_DNA-bd_sf; IPR000980 SH2; IPR036860 SH2_dom_sf; IPR001217 STAT; IPR035855 STAT3_SH2; IPR048988 STAT_linker; IPR036535 STAT_N_sf; IPR013800 STAT_TF_alpha; IPR015988 STAT_TF_CC; IPR013801* STAT_TF_DNA-bd; IPR012345* STAT_TF_DNA-bd_N; IPR013799 STAT_TF_prot_interaction
P42224	STAT1	DNA-binding domain entry: True
   IPR008967* p53-like_TF_DNA-bd_sf; IPR000980 SH2; IPR036860 SH2_dom_sf; IPR001217 STAT; IPR038295 STAT1_C_sf; IPR035859 STAT1_SH2; IPR022752 STAT1_TAZ2-bd_C; IPR048988 STAT_linker; IPR036535 STAT_N_sf; IPR013800 STAT_TF_alpha; IPR015988 STAT_TF_CC; IPR013801* STAT_TF_DNA-bd; IPR012345* STAT_TF_DNA-bd_N; IPR013799 STAT_TF_prot_interaction
Q24151	Stat92E	DNA-binding domain entry: True
   IPR008967* p53-like_TF_DNA-bd_sf; IPR000980 SH2; IPR036860 SH2_dom_sf; IPR001217 STAT; IPR048988 STAT_linker; IPR036535 STAT_N_sf; IPR013800 STAT_TF_alpha; IPR015988 STAT_TF_CC; IPR013801* STAT_TF_DNA-bd; IPR012345* STAT_TF_DNA-bd_N; IPR013799 STAT_TF_prot_interaction
Q9NAD6	sta-1	DNA-binding domain entry: True
   IPR008967* p53-like_TF_DNA-bd_sf; IPR000980 SH2; IPR036860 SH2_dom_sf; IPR001217 STAT; IPR048988 STAT_linker; IPR013800 STAT_TF_alpha; IPR015988 STAT_TF_CC; IPR013801* STAT_TF_DNA-bd; IPR012345* STAT_TF_DNA-bd_N
Q20977	sta-2	DNA-binding domain entry: True
   IPR008967* p53-like_TF_DNA-bd_sf; IPR000980 SH2; IPR036860 SH2_dom_sf; IPR001217 STAT; IPR012345* STAT_TF_DNA-bd_N; IPR057515 STATB_N
O00910	dstA	DNA-binding domain entry: True
   IPR041604 EF-hand_12; IPR008967* p53-like_TF_DNA-bd_sf; IPR037059* RHD_DNA_bind_dom_sf; IPR000980 SH2; IPR036860 SH2_dom_sf; IPR001217 STAT; IPR015988 STAT_TF_CC; IPR015347 STAT_TF_homologue_CC; IPR041410 STATa_Ig
Q54BD4	dstC	DNA-binding domain entry: True
   IPR041604 EF-hand_12; IPR008967* p53-like_TF_DNA-bd_sf; IPR037059* RHD_DNA_bind_dom_sf; IPR000980 SH2; IPR036860 SH2_dom_sf; IPR001217 STAT; IPR015988 STAT_TF_CC; IPR015347 STAT_TF_homologue_CC; IPR041410 STATa_Ig
Q70GP4	dstB	DNA-binding domain entry: True
   IPR041604 EF-hand_12; IPR008967* p53-like_TF_DNA-bd_sf; IPR037059* RHD_DNA_bind_dom_sf; IPR000980 SH2; IPR036860 SH2_dom_sf; IPR001217 STAT; IPR015988 STAT_TF_CC; IPR015347 STAT_TF_homologue_CC; IPR041410 STATa_Ig
Q86I20	dstD	DNA-binding domain entry: True
   IPR041604 EF-hand_12; IPR008967* p53-like_TF_DNA-bd_sf; IPR037059* RHD_DNA_bind_dom_sf; IPR000980 SH2; IPR036860 SH2_dom_sf; IPR001217 STAT; IPR015988 STAT_TF_CC; IPR041410 STATa_Ig
B5X561	SHA	DNA-binding domain entry: False
   IPR013320 ConA-like_dom_sf; IPR060320 DG1062/SHA-B_N; IPR000980 SH2; IPR036860 SH2_dom_sf; IPR001217 STAT
Q56XZ1	SHB	DNA-binding domain entry: False
   IPR013320 ConA-like_dom_sf; IPR060320 DG1062/SHA-B_N; IPR000980 SH2; IPR036860 SH2_dom_sf; IPR001217 STAT
```
