# gpr-1 (C. elegans, UniProt Q95QJ7) - manual literature research

No deep-research API was available for this review; this file was compiled manually
from cached publications (`publications/PMID_*.md`) and PubMed searches. Every claim
carries its source.

## Identity and paralogy

- GPR-1 (F22B7.13, 525 aa) is a TPR-like / GoLoco (GPR) motif protein, homologous to
  mammalian AGS3 / LGN (GPSM1/GPSM2) and Drosophila Pins. UniProt Q95QJ7 annotates a
  single GoLoco motif at residues 424-445 and an N-terminal TPR-like helical domain
  (InterPro IPR011990).
- GPR-1 and GPR-2 are "two closely related proteins" [PMID:12730122 "we describe two
  closely related proteins, GPR-1 and GPR-2 (G protein regulator)"]. Their coding
  sequences are so similar that RNAi and antibodies do not distinguish them, so almost all
  functional data are reported for "GPR-1/2" [PMID:16247027 "We used a dsRNA that depletes
  two highly homologous G-protein regulators, GPR-1 and GPR-2"].

## Molecular function: GoLoco GDI for G-alpha(i/o)

- The GoLoco/GPR motif binds GDP-bound Galpha(i/o) [PMID:12730122 "GPR-1/GPR-2 contain a
  GoLoco/GPR motif that mediates interaction with GDP-bound Galpha(i/o)"];
  [PMID:12750478 "GPR-1/2 interacted with guanosine diphosphate-bound GOA-1"].
- GDI activity on GOA-1 [PMID:12814548 "the GPR domain of GPR-1 and GPR-2 behaves as a GDP
  dissociation inhibitor for GOA-1"] and on GPA-16 [PMID:16162648 "GPR-1/2 acts as a guanine
  nucleotide dissociation inhibitor (GDI) for GPA-16, as it does for GOA-1"].
- A GoLoco-insensitive GOA-1(N150I) mutant loses GPR-1 GoLoco binding and GDI sensitivity,
  confirming that the GDI activity depends on direct GoLoco-Galpha contact [PMID:18984596
  "abrogated interaction between the Caenorhabditis elegans Galpha subunit GOA-1 and the GPR-1
  GoLoco motif"; "we verified that GOA-1(N150I) is indeed resistant to GoLoco motif-mediated
  GDI activity"]. The GDI assays used a GPR-1/2 peptide (aa 423-461).
- RIC-8 (GEF) acts upstream; GPR-1/2 then engages free Galpha [PMID:15479639 "RIC-8
  favors generation of Galpha free from Gbetagamma and enables GPR-1/2 to mediate asymmetric
  cell division"].

## Complex and cortical force generator

- GPR-1/2 associate with the NuMA-related coiled-coil protein LIN-5 and depend on it for
  localization [PMID:12730122 "which associate with LIN-5 in vivo and in vitro and depend on
  LIN-5 for localization to the spindle and cell cortex"]; [PMID:12814548 "LIN-5, a coiled-coil
  protein also required for spindle positioning, binds to and is required for cortical
  association of the GPR protein(s)"].
- Galpha-GPR-1/2-LIN-5 forms the ternary complex that anchors dynein at the cortex
  [PMID:25548889 "a ternary complex comprised of Gα (GOA-1/GPA-16), GPR-1/GPR-2, and LIN-5 is
  essential for anchoring the motor protein dynein to the cell cortex"]; GPR-1/2 and LIN-5
  interact with LIS-1 and promote cortical dynein [PMID:17922003 "the LIN-5, GPR-1/2 and the G
  alpha proteins promote the presence of the dynein complex at the cell cortex"].
- LIN-5-Galpha co-IP requires GPR-1/2 [PMID:18234174 "LIN-5 immunoprecipitates with Gα in
  vivo , and association is GPR-1/2 dependent"].

## Localization

- Cell cortex, posteriorly enriched during anaphase of the one-cell embryo in a PAR-dependent
  manner [PMID:12750478 "were enriched on the posterior cortex in a par-3- and par-2-dependent
  manner"]; [PMID:14534135 "the asymmetry of GPR-1/2 localization depends on PAR-3 and its
  downstream intermediate LET-99"]. Anterior cortical enrichment during centration/rotation
  [PMID:18234174]. LET-99 inhibits lateral GPR-1/2 to give a bipolar pattern [PMID:20421425].
  CSNK-1/PPK-1 (PIP2) control cortical levels [PMID:18694560 "asymmetric generation of PIP(2)
  by PPK-1 directs the posterior enrichment of GPR-1/2 and LIN-5"].
- Spindle / asters as well as cortex [PMID:12730122]; UniProt subcellular location.
- In EMS/P2, enriched at the P2-EMS contact; asymmetric only in P2 [PMID:21903670, abstract only,
  not cached].

## Biological processes

- Generation of cortical pulling forces on astral microtubules that position the spindle
  asymmetrically in P-lineage divisions [PMID:12750478 "were essential for generation of proper
  pulling forces"]; [PMID:12814548].
- Anaphase spindle elongation / posterior displacement [PMID:14534135 "generate asymmetric
  spindle pole elongation during divisions in the P lineage"].
- Pronuclear centration and rotation rates [PMID:18234174 "The depletion of LIN-5 or GPR-1/2
  results in decreased centration and rotation rates, indicating a role in force generation at
  this stage"].
- Not required for meiotic spindle rotation [PMID:19219036 abstract: "Spindle rotation during
  maternal meiosis is independent of GPR-1/2 and Galpha"].
- Signalling is receptor-independent [PMID:12814548 "the Galpha subunits are regulated by a
  receptor-independent mechanism"].

## Open points

- The relative contributions of GPR-1 vs GPR-2 are unresolved because reagents target both.
- Whether the active force-generating species is Galpha-GDP-GPR-1/2 (GDI model) or Galpha-GTP
  generated by RIC-8 remains debated [PMID:18984596 discussion of the two competing models].
