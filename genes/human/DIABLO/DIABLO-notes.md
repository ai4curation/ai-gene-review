# DIABLO / SMAC manual curation notes

## 2026-09-30

- Completed a manual DIABLO/SMAC review from GOA, UniProt, cached PubMed
  records, Reactome events, the PTHR32247 PANTHER family, and annotation-reviewer
  follow-up.
- Canonical DIABLO is a mitochondrial IAP antagonist rather than a caspase or
  ubiquitin-ligase enzyme. The founding SMAC and DIABLO papers identify a
  mitochondrial protein that is released to the cytosol during apoptosis and
  promotes caspase activation by binding IAPs and removing their inhibitory
  activity [PMID:10929711, "Smac promotes caspase-9 activation by binding to
  inhibitor of apoptosis proteins"; PMID:10929712, "DIABLO may promote
  apoptosis by binding to IAPs and preventing them from inhibiting caspases"].
- The molecular surface is the processed N terminus. Structural work showed
  that the SMAC AVPI motif engages IAP BIR grooves and that SMAC dimerization is
  required for strong apoptotic activity [PMID:10972280, "the amino-terminal
  four residues of Smac/DIABLO are indispensable for its function"]. PARL
  cleavage in mitochondria generates the mature N-terminal IAP-binding motif;
  loss of PARL maturation leaves SMAC unable to bind XIAP, while cytosolic
  cleaved SMAC rescues apoptosis in PARL-deficient cells [PMID:28288130].
- GO currently lacks a narrow "IAP antagonist activity" term. Direct XIAP,
  cIAP1/BIRC2, ML-IAP/BIRC7, and BIRC6 rows were therefore narrowed from
  `GO:0005515 protein binding` to broad `GO:0140678 molecular function
  inhibitor activity`; less mechanistic survivin, ARTS-context, PRKCD, AREL1,
  and high-throughput binary interactome rows were removed as generic partner
  edges.
- BIRC6/BRUCE is both a SMAC antagonist and a SMAC substrate context. Bartke et
  al. showed that BRUCE inhibits caspase activity and apoptosis and functions
  as a chimeric E2/E3 ubiquitin ligase with SMAC as a substrate
  [PMID:15200957]. Three recent BIRC6 structures support the inverse side:
  SMAC binds BIRC6 multivalently and competitively displaces caspases or other
  clients from the BIRC6 cavity [PMID:36758104; PMID:36758105; PMID:36758106].
- Ubiquitination rows should stay on the IAP-family E3s. Livin/BIRC7 promotes
  SMAC degradation [PMID:16729033] and AREL1 ubiquitinates cytosolic IAP
  antagonists including SMAC, HtrA2, and ARTS [PMID:23479728], but in both
  settings DIABLO is the bound substrate or client, not the enzyme.
- The apoptosis rows were tightened toward `GO:0097193 intrinsic apoptotic
  signaling pathway`. Broad `GO:0006915 apoptotic process`,
  `GO:0043065 positive regulation of apoptotic process`, and
  `GO:0097190 apoptotic signaling pathway` obscure the same mitochondrial IAP
  antagonist step. The death-receptor row is retained only as a non-core
  downstream sensitization context, because cytosolic SMAC can potentiate TRAIL
  apoptosis at the effector-caspase/IAP checkpoint [PMID:10950947].
- Removed the mouse-transferred CD40 receptor complex and cytoplasmic side of
  plasma membrane rows. That association is separate from canonical
  mitochondrion-to-cytosol SMAC biology and is not supported by the local human
  DIABLO evidence.
- The SMAC3 splice variant has a potentially distinct XIAP-destabilizing
  activity: Smac3 binds XIAP BIR2/BIR3, disrupts processed caspase-9 binding,
  promotes caspase-3 activation, and accelerates XIAP autoubiquitination and
  destruction; unlike canonical SMAC, it lacks exon 4 and therefore residues
  62-105 of the full-length sequence [PMID:14523016].

## 2026-10-03

- Replaced the local `inhibitor-of-apoptosis protein antagonist activity` NTR
  with `GO:1990525 BIR domain binding` after the Drosophila overannotation
  reviews landed on the same branch and exposed the exact same BIR-surface
  antagonism already using `GO:1990525` in `hid` and `grim`.
