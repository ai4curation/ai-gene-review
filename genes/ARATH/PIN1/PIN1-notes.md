# PIN1 (PIN-FORMED 1, AtPIN1) — Arabidopsis thaliana — curation notes

UniProt: Q9C6B8 (PINI_ARATH); locus AT1G73590; TCDB 2.A.69.1.1 (auxin efflux carrier / AEC family).

## Core identity and molecular function

PIN1 is a plasma-membrane, polytopic (10-TM) secondary transporter that mediates
cellular **auxin efflux**. Its polar (asymmetric) localization at the plasma membrane
sets the direction of intercellular (polar) auxin transport, generating the local auxin
gradients/maxima that drive organogenesis, vascular patterning, embryo axis formation
and phyllotaxis.

- Founding identification as auxin efflux carrier component, basal localization in vascular
  cells, polar auxin transport: [PMID:9856939 "the AtPIN1 protein was detected at the basal end of auxin transport-competent cells in vascular tissue. AtPIN1 may act as a transmembrane component of the auxin efflux carrier"]. Disruption phenotype: naked, pin-shaped inflorescences.
- Direct demonstration of active auxin efflux and structural mechanism: PIN1 expressed in
  HEK293F cells mediates active IAA efflux (enhanced by D6PK), inhibited by NPA
  [PMID:35917925 "These results show that PIN1 mediates active auxin efflux when expressed in HEK293F cells, and is further activated by D6PK. This PIN1-mediated auxin efflux is inhibited by NPA"].
- Substrate recognition: binds IAA (and IBA, IPA, 4-Cl-IAA) at an intracellular pocket;
  residues V51, N112, N478, I582 coordinate IAA [PMID:35917925 "IAA is coordinated through both hydrogen bonding and hydrophobic interactions ... All interacting residues (V51, N112, N478 and I582) are highly conserved in PINs"].
- Fold: 10-TM NhaA fold, TM1–TM5 / TM6–TM10 inverted repeats; inward-facing conformation
  [PMID:35917925 "The transmembrane domain of PIN1 has ten transmembrane segments (TM1 to TM10) ... PIN1 adopts a NhaA fold"].
- Homodimer: cryo-EM shows a dimeric PIN1 (TM1, TM2, TM7 dimer interface)
  [PMID:35917925 "we determined a dimeric structure of PIN1"]. This supports the GOA
  IDA annotations GO:0042802 identical protein binding and GO:0042803 protein
  homodimerization activity.

So the appropriate, informative MF terms are:
- GO:0010329 auxin efflux transmembrane transporter activity (IDA + IMP) — ACCEPT, core.
- GO:0042803 protein homodimerization activity / GO:0042802 identical protein binding — ACCEPT (homodimer is structurally established), non-core.

## Localization

- Plasma membrane is the functional site (multiple IDA/EXP): [PMID:9856939], [PMID:20439545],
  [PMID:33705718 "PINs, MAB4/MELs, and AGC kinases interact in the same complex at the plasma membrane"].
- Polar PM domains: apical vs basal localization is phosphorylation-dependent
  [PMID:20407025 "The apical-basal polar localization of the PIN proteins that determines the direction of auxin flow is controlled by reversible phosphorylation of the PIN hydrophilic loop"].
  Basal PM localization in vascular cells [PMID:9856939]. Apical/basal domains:
  GO:0016324 apical plasma membrane, GO:0009925 basal plasma membrane, GO:0045177 apical
  part of cell — all reflect the polar PM domain (cell periphery GO:0071944).
- GO:0005737 cytoplasm (HDA, PMID:15610358): PIN1 cycles between PM and endosomal
  compartments via GNOM-dependent recycling (UniProt FUNCTION). Cytoplasmic/endosomal
  signal is real (trafficking intermediates) but not the functional compartment; keep as
  non-core.
- GO:0009506 plasmodesma (HDA, PMID:21533090, proteomics): high-throughput proteome; PIN1
  is a PM protein and plasmodesmal PM is continuous with PM; weak/peripheral, keep non-core.
- GO:0009505 plant-type cell wall (IDA, PMID:18539115): PIN1 is an integral membrane
  protein; cell-wall assignment is not biologically meaningful for an auxin efflux carrier
  and likely reflects PM/apoplast-adjacent signal; mark as over-annotated.
- GO:0010168 ER body (IDA, PMID:36398993): PMID:36398993 is a tomato BIG/rosette paper
  about calcium and wound-induced rooting; it concerns ER localization of BIG, not PIN1
  ER-body localization. ER bodies are ER-derived structures found in Brassicaceae; there is
  no strong support that PIN1 is an ER-body resident. The long PINs (incl. PIN1) are PM
  proteins; only short PINs (PIN5/PIN8) are ER [PMID:35917925 "The short PINs are typically found at the endoplasmic reticulum, whereas the long PINs are at the plasma membrane"]. Treat ER body as a dubious annotation -> REMOVE/over-annotated. Marked UNDECIDED-leaning-REMOVE; chose MARK_AS_OVER_ANNOTATED conservatively is not appropriate since it appears to be a mis-assignment; chose REMOVE with rationale.

## Regulation / interactors (the "protein binding" GO:0005515 IPI rows)

All GO:0005515 rows are uninformative bare "protein binding"; replace with specific
interactor context in reason, action MARK_AS_OVER_ANNOTATED (interaction is real but term
uninformative; per project guidance avoid bare protein binding as core).

- PMID:17237354 WITH UniProtKB:Q9LJX0 = ABCB19/PGP19 — PIN–P-glycoprotein co-action in auxin transport.
- PMID:17889649 / PMID:20080776 WITH O64682 = PID (PINOID kinase) — phosphorylates PIN1 HL, controls polarity.
- PMID:33705718 WITH Q0WL52 = NPY5/MEL1 (MAB4/MEL family) — recruited to PM by PIN1, maintains polarity.
- PMID:22715043 WITH Q9LHE7 (FYPP1) and Q9SX52 (FYPP3) — PP6 phosphatase, dephosphorylates PIN.
- PMID:36226797 WITH AT3G55880 = SUE4 — PIN1-interacting membrane protein, acropetal transport under S deficiency.
- PMID:17586653 WITH Q9LY87 — K63 ubiquitin ligase context (apical dominance).

UniProt SUBUNIT: "Homodimer. Interacts with TOPP4 ... Interacts with FYPP1 and FYPP3 ...
Component of a complex made of PINs, MAB4/MELs and AGC kinases at the plasma membrane.
Binds directly to NPY5/MEL1."

## Biological processes (mostly IMP / acts_upstream_of_or_within)

Core BP:
- GO:0009926 auxin polar transport (IMP, PMID:16601150) — CORE.
- GO:0060918 auxin transport (IEA/IMP) — CORE (parent of polar transport).
- GO:0010315 auxin export across the plasma membrane (IDA, PMID:35917925) — CORE, most precise BP for the efflux event.
- GO:0055085 transmembrane transport (IEA) — accept as broad-but-correct parent.

Downstream developmental processes (pleiotropic; PIN1 acts upstream-of-or-within via auxin
gradients) — keep as non-core:
- GO:0009908 flower development; GO:0010229 inflorescence development (PMID:20407025; pin1 = pin-shaped naked inflorescence).
- GO:0048825 cotyledon development (IGI PMID:15371311); GO:0048826 cotyledon morphogenesis; GO:0009793 embryo development (PMID:20407025).
- GO:0010358 leaf shaping (PMID:16971475); GO:0010051 xylem and phloem pattern formation (PMID:16943276).
- GO:0009630 gravitropism (PMID:16601150); GO:0009640 photomorphogenesis (TAS PMID:16141452).
- GO:0048364 root development; GO:0048367 shoot system development (PMID:9856939/PMID:11060241).
- GO:0010262 somatic embryogenesis (IMP PMID:36345646); GO:0048830 adventitious root development (IMP PMID:36398993 — tomato ro/big paper; PIN1 accumulation Ca-sensitive). The adventitious-root annotation rests on an indirect tomato study; keep as non-core but flagged.

## Summary of decisions
- ACCEPT (core MF/BP/CC): auxin efflux transmembrane transporter activity (x2), auxin export across PM, auxin polar transport, auxin transport (x2), plasma membrane (multiple), transmembrane transport.
- ACCEPT non-core / homodimer: identical protein binding, protein homodimerization activity.
- KEEP_AS_NON_CORE: polar PM subdomains (apical/basal PM, apical part of cell, cell periphery), cytoplasm, plasmodesma, and all developmental BPs.
- MARK_AS_OVER_ANNOTATED: bare protein binding rows; plant-type cell wall.
- REMOVE: ER body (mis-assignment / wrong paper context).
