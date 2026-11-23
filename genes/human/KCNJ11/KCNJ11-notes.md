# KCNJ11 (Kir6.2) review notes

UniProt Q14654; HGNC:6257. Pore-forming subunit of the ATP-sensitive K+ (KATP) channel.

## Core biology

- Kir6.2 forms the K+ pore; four Kir6.2 + four SUR subunits make the KATP channel
  [PMID:7502040 "these pancreatic beta cell potassium channels are a complex composed of at least two subunits--BIR, a member of the inward rectifier potassium channel family, and SUR"].
- Human SUR1/Kir6.2 cryo-EM structure with ATP in the Kir6.2 inhibitory site
  [PMID:29286281 "human pancreatic KATP channel, containing the ABC transporter SUR1 and the inward-rectifier K+ channel Kir6.2"].
- ATP binding residues R50, K185, R201 in Kir6.2 mediate ATP closure
  [PMID:12860923 "mutation of three positively charged residues, R50, K185 and R201, impairs the ability of ATP to close the channel"].
- Beta-cell coupling: [PMID:8923010 "Closure of ATP-sensitive potassium channels in pancreatic islet beta-cells initiates a cascade of events that leads to insulin secretion."]
- Physiological current is K+ efflux (falcon deep research, citing Tinker 2018): "In a pancreatic β-cell, an open channel permits K⁺ efflux down the prevailing electrochemical gradient, holding the plasma membrane relatively hyperpolarized."

## Disease

- Loss of function: congenital hyperinsulinism (HHF2) [PMID:8923010 "Kir6.2 is necessary, although not sufficient, for normal regulation of insulin release"].
- Gain of function (reduced ATP block): neonatal diabetes / DEND
  [PMID:15583126 "All mutations increased resting whole-cell K(ATP) currents by reducing channel inhibition by ATP"].

## Annotation decisions (summary)

- Core MF: GO:0015272 (ATP-sensitive inward rectifier channel; definition covers ATP inhibition despite the "ATP-activated" label). Core BP: potassium ion transmembrane transport, regulation of membrane potential, regulation of insulin secretion.
- MODIFY voltage-gated K+ channel and SynGO "voltage-gated ... presynaptic membrane potential" rows to GO:0015272: Kir6.2 has no voltage sensor; PMID:18945825 is a pig urethral smooth-muscle study, not presynaptic.
- MODIFY "potassium ion import across plasma membrane" (incl. IBA) to GO:0071805: KATP physiological current is outward. Same choice as the ABCC8 review.
- MODIFY "glucose metabolic process" IMPs to glucose homeostasis (channel affects insulin secretion, not glucose metabolism).
- REMOVE ATPase-coupled cation transporter ISS (Kir6.2 has no ATPase; ATP is an inhibitory ligand) and bare protein binding rows.

## Provenance

- Stub fetched with `just fetch-gene human KCNJ11` (2026-10-10). Falcon deep research first timed out at the
  default 600 s; re-run with `--timeout 3600` succeeded (KCNJ11-deep-research-falcon.md).
- Aligned with dismech `Congenital_Isolated_Hyperinsulinism` and `Hyperinsulinemic_Hypoglycemia`, whose K-ATP
  loss-of-function nodes now carry GO:0015272 DECREASED.
