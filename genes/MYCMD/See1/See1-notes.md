# See1 (UMAG_02239; UniProt A0A0D1C8C8) - curation notes

## Sources
- Primary (and essentially only) experimental paper: Redkar et al. 2015 Plant Cell, PMID:25888589 (full text cached).
- Falcon deep research (See1-deep-research-falcon.md): confirms identity (um02239 = see1) and that no newer
  primary See1 mechanism has been published; Sts2/UMAG_05318 (2023) is a distinct effector.

## Identity / features
- 157-aa precursor with N-terminal secretion signal (residues 1-21; constructs use See1 22-157)
  [PMID:25888589 "See1 lacking the signal peptide was expressed from pGBKT7-See1 22–157"].
- No catalytic domain or conserved family established (deep research).

## Localization
- Fungal-delivered See1-3xHA (immunogold TEM): [PMID:25888589 "See1-3xHA was detected in the fungal hyphae, at the
  biotrophic interface, in plant cytoplasm, and prominently inside plant cell nuclei"];
  [PMID:25888589 "Only See1-3xHA was quantitatively detected inside host cells, with ∼20% of particles localizing to maize nuclei"].
- Secreted mCherry control stayed at the interface - argues translocation is See1-specific.
- Bombardment: [PMID:25888589 "See1 22–157 -mCherry localized to both the maize cytoplasm and nuclei"]; cell-to-cell
  spread seen only in overexpression, [PMID:25888589 "Movement of See1 to the neighboring cells was not observed in the TEM immunogold assay."]
- Conclusion: all three GOA CC terms (extracellular region, host cell cytoplasm, host cell nucleus) are supported.
  Extracellular region is the transit compartment (biotrophic interface); site of action is host cytoplasm/nucleus.

## Function / process
- Organ-specific: required for seedling-leaf tumours, not tassel tumours
  [PMID:25888589 "See1 does not affect tumor formation in immature tassel floral tissues"].
- DNA synthesis reactivation: [PMID:25888589 "See1 is required for the reactivation of plant DNA synthesis, which is crucial for tumor progression in leaf cells."]
  EdU: 67.5% (SG200) vs 7.3% (Δsee1) of colonized cells at 4 dpi; Δtin3 (another small-tumour mutant) retained ~44%,
  so the defect is not a trivial consequence of small tumours.
- GO:0141017 "effector-mediated induction of cell cycle reactivation in host" - definition (QuickGO): symbiont process
  in which a secreted molecule reactivates the host cell cycle, resulting in DNA synthesis and host cell division,
  contributing to vegetative tumour formation. Essentially tailored to this paper; correct symbiont-side term. ACCEPT.
- Mechanism: interacts with ZmSGT1 (Y2H, in planta co-IP, BiFC in cytoplasm and nucleus)
  [PMID:25888589 "The interaction of See1 and SGT1 was confirmed independently by in planta coimmunoprecipitation."];
  [PMID:25888589 "See1 interferes with the MAPK-triggered phosphorylation of maize SGT1 at a monocot-specific phosphorylation site."]
  Downstream steps unresolved [PMID:25888589 "The precise steps following the interference of See1 with the posttranslational modification of SGT1, resulting in the reactivation of maize DNA synthesis and ultimately in tumor formation, remain to be elucidated biochemically."]
- Immune modulation is only proposed ("Hijacking of SGT1 may contribute to the deactivation of immune responses.") -
  not sufficient for a NEW suppression-of-host-immunity term.

## MF
- No GO MF term fits: the only known activity is binding SGT1 and blocking its phosphorylation. "protein binding" is
  excluded by policy; no evidence of kinase-inhibitor activity on the MAPK itself (direct inhibition not shown), so
  "protein kinase inhibitor activity" / "molecular function inhibitor" would over-interpret. Leave MF unset in
  core_functions.

## Project curation question 1 (symbiont-side terms)
- See1's single BP annotation already uses a symbiont-side effector term (GO:0141017), backed by IDA on the effector
  itself (knockout + complementation + EdU), not IEA. No plant-side defense terms present. CC annotations use
  host-* terms correctly. Comparable to CMU1 (symbiont-side GO:0140502).
