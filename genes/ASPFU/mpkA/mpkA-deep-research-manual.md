# Manual deep research: ASPFU mpkA

`mpkA` / `AFUA_4G13720` encodes an Aspergillus fumigatus Af293 MAP kinase in
PANTHER family PTHR24055. The UniProt record carries the MAPK signature,
protein kinase ATP-binding signature, and protein kinase catalytic domain, and
assigns EC 2.7.11.24.

The 2008 primary study identified MpkA as the A. fumigatus MAPK most similar to
fungal cell-wall-integrity MAPKs. Deleting `mpkA` caused severe sensitivity to
cell-wall-active compounds, abnormal morphology, and altered oxidative-stress
resistance, establishing MpkA as a major cell-wall-integrity regulator.

The 2009 follow-up placed MpkA in a three-tier Bck1-Mkk2-MpkA MAPK module.
Mutants lacking any tier had severe cell-wall-drug sensitivity and abnormal
morphology, and western blots showed that Bck1 and Mkk2 activate MpkA during
vegetative growth and after cell-wall stress. That paper also connected MpkA to
pyomelanin formation.

The 2021 fumiquinazoline study provided the strongest direct substrate evidence
currently cached: MpkA physically associates with nonribosomal peptide
synthetases FmqA and FmqC, and the phosphorylated FmqC band is absent in the
`mpkA` deletion strain. MpkA therefore directly phosphorylates a biosynthetic
enzyme during conidiogenesis, in addition to its classical CWI signaling role
through RlmA.

PMID:22220813 functionally characterized upstream CWI sensors and Rho GTPases.
It is useful background for Wsc/Mid/Rho inputs to the CWI pathway, but the
cached record is abstract-only and does not itself show the `mpkA` experiments
behind the heat and alkaline-pH IMP rows.

The 2024 gliotoxin paper is the newest direct MpkA paper I found. It showed
that MpkA is essential for gliotoxin production and self-protection, that MpkA
physically interacts with GliT and GtmA, and that MpkA is needed for GliT and
GtmA accumulation and vacuolar localization under gliotoxin-producing
conditions. These findings strengthen the model that A. fumigatus MpkA has
secondary-metabolism outputs, but the core GO representation is still MAP kinase
activity in the cell-wall-integrity MAPK cascade.
