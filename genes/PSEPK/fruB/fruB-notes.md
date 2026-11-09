# fruB curation notes

## Boundary and evidence

FruB (Q88PQ5; PP_0793) is the soluble, fused EI-HPr-EIIA(Fru)
multiphosphoryl-transfer component of the KT2440 fructose PTS. The exact
UniProt record assigns EC 2.7.3.9 and RHEA:23880. Primary KT2440 work states
that FruA and FruB form a complete system for fructose intake and identifies
FruB as an EI-HPr-EIIA(Fru) polyprotein
[PMID:18296519 "Two of these PTS constituents (FruA and FruB) form a complete
system for fructose intake."; PMID:22708906 "FruB (i.e. the
EI-HPr-EIIA(Fru) polyprotein)"].

The literature name follows phosphate-flow order. In the Q88PQ5 primary
sequence, the domains run EIIA(Fru)-HPr-EI from the N to the C terminus.

The current GO vocabulary has no EIIA-specific protein-to-protein relay
activity. GO:0008982 and its fructose child GO:0022877 describe
transport-coupled transfer from phosphohistidine to extracellular sugar, while
GO:0090563 describes the terminal phosphocysteine-to-sugar transport reaction.
None captures the soluble HPr-to-EIIA-to-EIIB transfer, so the proposed EIIA
term remains under the conservative `GO:0016772` parent pending ontology-editor
placement
([QuickGO GO:0008982](https://www.ebi.ac.uk/QuickGO/term/GO%3A0008982);
[QuickGO GO:0022877](https://www.ebi.ac.uk/QuickGO/term/GO%3A0022877);
[QuickGO GO:0090563](https://www.ebi.ac.uk/QuickGO/term/GO%3A0090563)).

The fructose-dependent transfer of phosphate from FruB to the nitrogen-related
PTS is experimentally supported, but it is treated as a regulatory side branch
rather than the core FruB function. Broad kinase and transferase annotations
were marked over-annotated because GO:0008965 captures the direct reaction.

## 2026-11-05 — completion pass (Claude, AI-assisted)

Deep research: `just deep-research PSEPK fruB --provider perplexity` was tried
once and failed (provider not available in this environment); no
deep-research file exists for this gene.

Changes made to reach COMPLETE:

- Replaced UniProt quotes that rest only on ARBA rules (subcellular location,
  EC number) with KT2440 literature quotes and the NCBIfam/PANTHER family
  lines. Q88PQ5 is an unreviewed entry whose catalytic-activity and location
  comments are all ARBA-derived.
- GO:0008965 now cites [PMID:18296519 "FruB is a multiphosphoryl transfer
  protein consisting of a classic EI domain fused to an equally standard HPr
  module and one EIIA Fru module."] and the in vivo PtsN phosphorylation by
  FruB.
- GO:0016740 and GO:0016772: MARK_AS_OVER_ANNOTATED -> TOO_GENERAL (true,
  entailed by GO:0008965).
- GO:0016301 kinase activity: kept MARK_AS_OVER_ANNOTATED, now with the GO
  definition ("Catalysis of the transfer of a phosphate group, usually from
  ATP, to a substrate molecule.") and the observation that GO places
  GO:0008965 outside kinase activity.
- Every row now has supported_by. Actions are aligned with the new X.
  campestris FruB (P45597) review for shared terms.
