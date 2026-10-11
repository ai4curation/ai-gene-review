# FGFR1 (human, P11362) curation notes

## 2026-09-30 — initial review (claude-code)

Context: reviewed as part of the FGFR signaling module (`modules/fgfr_signaling.yaml`), which
models FGFR1-4 as paralog variants of one receptor tyrosine kinase step.

### Core biology (with provenance)

- Receptor tyrosine kinase for FGFs: "Tyrosine-protein kinase that acts as a cell-surface receptor
  for fibroblast growth factors" [file:human/FGFR1/FGFR1-uniprot.txt].
- Ligand + HSPG induce dimerization and autophosphorylation: [PMID:15863030 "The binding of FGF and
  HSPG to the extracellular ligand domain of FGFR induces receptor dimerization, activation and
  autophosphorylation of multiple tyrosine residues in the cytoplasmic domain of the receptor molecule."]
- Ordered trans-autophosphorylation; activation loop first: [PMID:19224897 "First-stage
  autophosphorylation of an activation loop tyrosine leads to 50- to 100-fold stimulation of kinase
  activity"]; asymmetric kinase dimer [PMID:20133753 "formation of an asymmetric dimer between
  activated FGFR1 kinase domains is required for transphosphorylation of FGFR1 in FGF-stimulated cells"].
- Y653/Y654 required for kinase activation [PMID:8622701 "autophosphorylation on tyrosines 653 and 654
  is important for activation of tyrosine kinase activity of FGFR1"].
- pY766 docks PLC-gamma1 [PMID:1656221 "Tyr-766 and its flanking sequences represent a major binding
  site in FGFR for PLC-gamma"]; Y766F abolishes PtdIns hydrolysis but not mitogenesis [PMID:1379697].
- FRS2 binds juxtamembrane region constitutively (non-pY motif) [PMID:9660748 "A juxtamembrane segment
  of FGFR-1 and the phosphotyrosine-binding domain of SNTs are both necessary and sufficient for
  interaction"].
- Heparin: 2:2:2 FGF:FGFR:heparin complex [PMID:11030354].
- Ligand specificity by splice variant: [PMID:8663044 "FGF 1 is the only FGF that can activate all
  FGF receptor splice variants"].
- Signal termination: ubiquitination and lysosomal sorting [PMID:18480409]; NEDD4-1 [PMID:21765395].

### Paralog-specific points relevant to the module

- **FGF23 (endocrine) via FGFR1c + alpha-Klotho**: [PMID:19966287 "Fibroblast growth factor (FGF) 23
  inhibits renal phosphate reabsorption by activating FGF receptor (FGFR) 1c in a Klotho-dependent
  fashion."; "the soluble ectodomains of FGFR1c and Klotho are sufficient to form a ternary complex with
  FGF23 in vitro."]. This supports the module's FGFR1c/Klotho FGF23 variant note.
- **FGF21 via FGFR1c + beta-Klotho** (adipose): [PMID:17623664 "Both FGF19 and FGF21 can signal
  through FGFR1-3 bound by betaKlotho and increase glucose uptake in adipocytes expressing FGFR1."].
  Note this paper shows FGF19/21 can signal via FGFR1-3 with beta-Klotho, so FGF21 is not strictly
  FGFR1-exclusive at the biochemical level; FGFR1c predominance is a tissue-expression effect.
  Only FGF19 (not FGF21) signals efficiently through FGFR4.
- **GnRH neuron development / Kallmann (KAL2)**: FGFR1-specific in humans [PMID:12627230 "loss-of-function
  mutations in FGFR1 underlie KAL2"]; anosmin-1 (ANOS1/KAL1) binds FGFR1 with high affinity but FGFR2IIIc
  weakly and FGFR3IIIc negligibly [PMID:19696444].
- Pfeiffer P252R (FGFR1) is the paralogous counterpart of Apert P253R (FGFR2) and Muenke P250R (FGFR3),
  but ligand-specificity effects differ between paralogs [PMID:14613973].

### Key curation decisions

- 45 `protein binding` IPI rows: FGF-ligand-only rows MODIFY -> GO:0017134 fibroblast growth factor
  binding; PLCG1-only rows MODIFY -> GO:0043274 phospholipase binding; everything else REMOVE as
  uninformative (HT AP-MS/BioID/PLA, HSP90 client, co-IP with cadherin/catenin, 5-HT1A, NOSTRIN, FRS2,
  NEDD4, anosmin-1, FOP-FGFR1 fusion).
- PMID:8753773 (IPI with CD24): abstract only describes CD24 with c-fgr (FGR) and lyn; possible
  FGR/FGFR1 confusion, not verifiable without full text. Removed on uninformative-term grounds only.
- MAPK cascade (TAS) and positive regulation of MAP kinase activity (IDA) -> MODIFY to GO:0043410
  positive regulation of MAPK cascade (receptor initiates, does not execute, the phosphorelay).
- identical protein binding -> MODIFY to protein homodimerization activity; homodimerization kept
  non-core (mechanistic sub-step of receptor activation).
- PMID:23382219 (signaling receptor complex, IDA): cached text is a PX-FERM cargo screen and does not
  mention FGFR1 explicitly; accepted deferring to curator since FGFR1 complex membership is well
  established.
- Developmental, endothelial (miRNA papers), EMT and 5-HT1A heteroreceptor annotations kept as non-core.
- No NEW annotations proposed. GnRH neuron development (GO:0021888) was considered but not added:
  human genetic evidence is necessity evidence and the in vivo cell-autonomous mechanism was not
  verified from cached sources.
