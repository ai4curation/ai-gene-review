# lin-12 (C. elegans) curation notes

UniProt P14585 (LIN12_CAEEL), 1429 aa, single-pass type I membrane protein, "Protein lin-12" /
Notch-like protein; one of the two C. elegans Notch receptors (the other is GLP-1).

## Identity and domain architecture

- Extracellular: 13 EGF-like repeats (several Ca2+-binding EGF), 3 LIN-12/Notch repeats (LNR) and the
  NOD/NODP negative regulatory region; intracellular RAM region, ankyrin repeats.
  [PMID:3419531 "These include extensive overall sequence similarity to the Drosophila Notch protein"]
- PANTHER (from the UniProt record, verbatim): PTHR24049 (CRUMBS FAMILY MEMBER), PTHR24049:SF22
  (DROSOPHILA CRUMBS HOMOLOG). Note: this is an odd placement for a Notch receptor. APX-1 (a DSL
  ligand) is placed in the same subfamily, and the lin-12 IBA rows for Notch binding (PTN002371879) and
  negative regulation of Notch signaling (PTN001170801) are both seeded exclusively by DSL ligand
  donors (e.g. Dl, Ser, mouse DLL1/DLL3/DLL4, rat JAG1; the negative-regulation node donors are mouse DLL4 and rat DLL3). These are ligand functions and I flag them as
  mis-propagated onto a receptor (REMOVE).
- GLP-1 by contrast is in PTHR45836:SF23 (NEUROGENIC LOCUS NOTCH HOMOLOG PROTEIN 1).

## Receptor function

- Binary cell-fate switch: [PMID:6616618 "We propose that lin-12 functions as a binary switch to control
  decisions between alternative cell fates during C. elegans development."]
- Acts cell-autonomously in the signal-receiving cell (AC/VU decision):
  [PMID:2736627 "we conclude that lin-12 function is VU cell autonomous"]
- Intracellular domain has intrinsic activity; ECD regulates it:
  [PMID:8343960 "Our results indicate that the intracellular domains of Lin-12 and Notch have intrinsic
  activity and that the principal role of the extracellular domains in the intact proteins is to regulate
  this activity."]
- Ligands: LAG-2, APX-1, DSL-1 (DSL ligands) and OSM-11 (secreted DOS co-ligand) bind LIN-12 EGF
  repeats 1-6 in yeast two-hybrid [PMID:18700817 "We found that OSM-11 also interacted with LIN-12
  extracellular EGF repeats 1 through 6 (Figure 8)"].
- Redundancy with glp-1 in embryogenesis (Lag phenotype):
  [PMID:1769331 "We show here that lin-12 and glp-1 are functionally redundant during embryogenesis"]

## Nuclear function (NICD)

- NICD forms the LAG-1 (CSL) / LAG-3 (SEL-8, Mastermind) ternary complex:
  [PMID:10830967 "Here we identify LAG-3, a glutamine-rich protein that forms a ternary complex together
  with the LAG-1 DNA-binding protein and the receptor's intracellular domain."]
- Crystal structure of worm CSL-LIN-12 NICD-LAG-3 on DNA [PMID:16530045]; LIN-12 RAM peptide binds
  LAG-1 BTD [PMID:15297877; PMID:18381292 "Our binding data show that RAM and CSL form a high affinity
  complex in the presence or absence of DNA."]
- Nuclear LIN-12::GFP detectable in embryos and differentiating vm2 cells [PMID:22901814; PMID:24512688].

## Regulation / trafficking (pathway-variant relevant)

- Apical localization in VPCs; EGFR-Ras-MAPK in P6.p drives LIN-12 endocytosis and degradation
  (ALX-1, WWP-1) — a worm-specific crosstalk mode [PMID:16236769]. Lateral-signal inhibiting activity
  resides in the ECD at the apical surface [PMID:16236769].
- SEL-10 (CDC4/FBW7) complexes with LIN-12 and promotes its turnover [PMID:9389650].
- S2 cleavage by ADAM (SUP-17/ADM-4); S3 by gamma-secretase (SEL-12/HOP-1) (UniProt PTM line).

## Other roles (non-core, pleiotropic outputs of the signaling)

- Postembryonic mesoderm (M lineage) ventral fates [PMID:18036582]; vm2 muscle-arm development
  [PMID:23539368]; basement-membrane sliding [PMID:27661254]; dauer recovery [PMID:18599512]; sleep
  [PMID:29523076].


## Deep research status

The first falcon run (`just deep-research-falcon worm lin-12 --fallback perplexity-lite`) timed out at 600 s. The
perplexity fallback is unavailable in this environment. A rerun with `--timeout 2400` succeeded:
`lin-12-deep-research-falcon.md`. It is consistent with the review and is cited in core_functions. Note that
falcon reports C. elegans LIN-12/GLP-1 are tuned to lower force thresholds for activation than Drosophila
Notch (Langridge et al. 2021 bioRxiv; not in the publications cache, so not used as evidence here).
