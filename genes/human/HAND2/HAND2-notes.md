# HAND2 (dHAND) notes

Automated deep research was unavailable for this review (falcon 402, OpenAI 401), so these notes
were compiled manually from cached PubMed abstracts/full texts, the UniProt record (P61296) and
QuickGO annotations of the mouse ortholog (Q61039).

## Identity and molecular mechanism

- Twist-family class B bHLH transcription factor (bHLH domain aa 99-151; Pfam PF00010). Human gene
  cloned and strongly expressed in heart [PMID:9878849 "Northern analysis indicates that the HAND2 transcript is 2.3 kb in length and strongly expressed in the human heart"].
- Heterodimerizes with E-proteins (E12/E47, TCF4, TCF12) and binds a subset of E-boxes; N-terminal
  activation domain [PMID:11812799 "HAND2 contains a strong transcriptional activation domain in the amino-terminal third of the protein"; "HAND2 functions as a transcription activator by binding a subset of E-boxes as a heterodimer with E-proteins"]. Homodimers form in vitro but not robustly in cells
  [PMID:11812799 "HAND2 fails to homodimerize in a mammalian two-hybrid assay but demonstrates robust HAND2/E12 interaction"].
- Dimer partner choice with TWIST1 is regulated by PKA/PP2A phosphorylation of helix I
  [PMID:15735646 "Dimerization partner choice by Twist1 and Hand2 can be modulated by protein kinase A- and protein phosphatase 2A-regulated phosphorylation of conserved helix I residues"].
- DNA-binding-independent activity: limb digit duplication needs only the HLH
  [PMID:12070084 "digit duplication by dHAND requires neither the transcriptional activation domain nor the basic region, but only the HLH motif"];
  ANF activation independent of E-boxes [PMID:12392994 "mutations in these three sites suggest HAND2 activity is DNA-binding independent"].
- Partner TFs: GATA4 (bHLH-zinc finger interaction, p300 recruitment)
  [PMID:11994297 "the bHLH domain of dHAND physically interacted with the C-terminal zinc finger domain of GATA4 forming a higher order complex"; "the bHLH domain of dHAND directly interacted with the CH3 domain of p300"];
  MEF2C [PMID:15486975 "full-length MEF2C protein is able to interact with dHAND in vitro and in vivo"];
  NKX2-5 synergy on ANF [PMID:12392994]; PHOX2A [PMID:16280598 "dHAND causes an eightfold increase in the affinity of Phox2a for its recognition sites on the DBH promoter region"].
- p300/CBP dependence in autonomic neuron induction [PMID:16145670 "this function is dependent on its interaction with the histone acetyltransferase p300/CBP"].

## Biological roles (mostly from mouse)

- Heart: right ventricle and aortic arch arteries [PMID:9171826 "the first demonstration of a single gene controlling the formation of the mesodermally derived right ventricle and the neural crest-derived aortic arches"];
  with Nkx2-5 for the entire ventricular segment [PMID:11784028 "Complete ventricular dysgenesis was observed in Nkx2.5(-/-)dHAND(-/-) mutants"],
  role in survival/expansion, not specification [PMID:11784028 "a role of HAND genes in survival and expansion of the ventricular segment, but not in specification of ventricular cardiomyocytes"].
  Cardiac neural crest: OFT alignment, SHF proliferation non-autonomously [PMID:19008477].
- Adult heart disease: re-expressed in failing myocardium; drives pathological hypertrophy [PMID:24161931].
- Limb: upstream of Shh in the ZPA [PMID:10804186 "identify dHAND as an upstream activator of Shh expression"].
- Sympathetic/noradrenergic neurons [PMID:18501887; PMID:16145670]; enteric neurons [PMID:17075884].
- Branchial arches downstream of endothelin-1 (PMID:9671575, cached).
- Uterus: progesterone-induced stromal Hand2 suppresses FGFs to block epithelial proliferation; required for implantation
  [PMID:21330545 "Hand2 operates downstream of P to regulate the production of FGFs"].

## Curation notes

- Module (cardiac_specification_network) annoton GO:0000981 in heart development is consistent with
  the review. Note that a subset of HAND2 activity is DNA-binding independent (co-activator-like via
  GATA4/p300), so GO:0061629 is also a core MF.
- GO:0003680 (AT-rich minor groove binding) from PMID:15486975 likely reflects the MEF2C A/T site in a
  MEF2C-HAND2 complex rather than HAND2 activity.
