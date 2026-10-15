# SPRY1 (O43609) curation notes

## 2026-10-01 initial review

Context: reviewed as a paralog variant of the Sprouty/SPRED negative-feedback step on RTK-Ras-ERK
signalling (comparator: genes/human/SPRY4, which took GO:0004860 protein kinase inhibitor activity
as core MF).

### Mechanism

- After growth-factor stimulation Spry1 moves to the plasma membrane, is Tyr-phosphorylated, and binds
  GRB2, blocking GRB2-SOS recruitment to FRS2/SHP2 [PMID:12402043 "they bind to the adaptor protein
  Grb2 and inhibit the recruitment of the Grb2-Sos complex either to the fibroblast growth factor
  receptor (FGFR) docking adaptor protein FRS2 or to Shp2"]. Abstract-only.
- SPRY1 is the GRB2-binding paralog; SPRY4 binds SOS1; SPRY1-SPRY4 hetero-oligomers are the most potent
  [PMID:16339969 "Sprouty1 specifically interacts with Grb2, whereas Sprouty4 interacts with Sos1"].
- Dissent on the exact step: [PMID:11585837 "Sprouty1 and Sprouty2 do no prevent the formation of a
  SNT.Grb2.Sos complex upon fibroblast growth factor stimulation, yet block Ras activation"].
- SHP-2 inactivates SPRY1 by dephosphorylating the critical tyrosine [PMID:16481357 "a purified SHP-2
  protein dephosphorylates the critical tyrosine of Sprouty 1"].
- No SPRY1-specific direct kinase-inhibition assay found. JAK2 suppression in erythroid cells is genetic
  [PMID:22508938 "Molecular mechanisms for Spry1 suppression of Jak2 presently are speculative"].
- Decision: core MF = GO:0140311 protein sequestering activity (proposed as NEW); the IBA GO:0004860
  is kept as non-core (inherited family activity, not contradicted, not shown for SPRY1).

### Localisation

- Endogenous human SPRY1 in HUVECs: perinuclear, vesicular, plasma membrane leading edge
  [PMID:11238463 "it was found predominantly in perinuclear regions, in vesicular structures, and in the
  plasma membrane at the leading edge of the cells"]; palmitoylated [PMID:11238463 "These results
  demonstrate that both mSpry-1 and -2 are palmitoylated"].

### Processes

- ERK negative regulation, endogenous human evidence [PMID:20813052 "we observed an increased ERK1/2
  activation and a higher migration capacity in SPRY1-silenced cells"].
- FGF2/VEGF but not EGF-ERK inhibited in HUVECs [PMID:11238463 "activation of p42/44 MAP kinase was not
  affected"] -> EGFR IBA left UNDECIDED. Also the Reactome Sprouty-CBL decoy model (SPRY2 data) and
  chondrocyte overexpression [PMID:18582454 "Spry1 likely sequesters c-Cbl away from FGFR-FRS2-Grb2
  complexes"] show Sprouty can prolong RTK signalling.
- Kidney: Spry1-/- mice have supernumerary ureteric buds rescued by lowering Gdnf [PMID:15691764]; Spry1
  also brakes FGF10-FGFR2 [PMID:20084103 "When Spry1 is absent there is no brake on signaling via
  FGFR2"]. These are developmental outcomes of the feedback activity; not proposed as NEW. Note GO has
  obsoleted GO:2000734 (negative regulation of GDNF receptor signaling involved in ureteric bud
  formation), which argues against filling this as a gap.
- Senescence via Tyr53/p38 [PMID:38670941] - noted only, not annotated.

### Ortholog-derived annotations

- Lens EMT / TGFbeta (mouse ISS from rat lens explant IDA, PMID:25576668): EMT kept non-core; TGFbeta
  receptor signalling marked over-annotated (phenotype, not pathway action).
- Cardiac EMT GO:0060940 (rat IGI, PMID:23441172): SPRY1 opposes EMT (miR-21 target) -> MODIFY to
  GO:0010719.
- Rat permeability / endothelial tube formation (PMID:41714891, abstract-only, disease model): permeability
  over-annotated; tube formation has wrong polarity -> MODIFY to GO:0016525 negative regulation of
  angiogenesis [PMID:20813052 "SPRY1 is an endogenous angiogenesis inhibitor"].

### NOT annotations

None in GOA for SPRY1.

### Comparison with SPRY4

SPRY4: RAF1 binding via cysteine-rich domain and TESK1 kinase inhibition -> kinase-inhibitor MF; SOS1
association. SPRY1: GRB2 binding via phospho-Tyr53 -> sequestration MF; no kinase-inhibition evidence.
Both converge on the same process set (negative regulation of FGFR signalling, Ras signalling, ERK1/2
cascade) and cooperate as hetero-oligomers.

## 2026-10-01: OpenScientist check of the GRB2-sequestration proposal

- OpenScientist (2 iterations; `SPRY1-hypotheses/spry1-grb2-sh3-motif/openscientist.md`) scanned human, mouse and zebrafish SPRY1, SPRY2 and SPRY4 for the PxxPxR GRB2 SH3-binding motif. The only canonical C-terminal motif is SPRY2 PTVPPR (position 304); SPRY1 has none. This agrees with Lao 2006/2007 [PMID:16893902 "found exclusively on Spry2"; PMID:17255109 "An exclusive, necessary, but cryptic PXXPXR motif in the C terminus of Spry2"].
- SPRY1 keeps the N-terminal NEYTEG Tyr53, so any SPRY1-GRB2 binding would be phospho-tyrosine dependent (Hanafusa 2002, PMID:12402043, abstract only). Gross 2001 (PMID:11585837) disputes sequestration. Even for SPRY2, GRB2 binding was dispensable for ERK inhibition in one study [PMID:17689925 "These results are evidence that the Sprouty2 mechanism of ERK inhibition is independent of Grb2 binding."].
- Decision: deleted the NEW GO:0140311 protein sequestering activity proposal. A refuted or unsupported AI proposal is deleted, not set to REMOVE. Accepted the IBA GO:0004860 protein kinase inhibitor activity and made it the core MF. GRB2 sequestration is kept as a lead in the description and suggested questions.
