# Cupriavidus necator Gbd (Q59104)

## 2026-10-26 source-based review

Q59104 is the exact accession named in the biochemical study, not a Pseudomonas candidate. Current UniProt uses species-level CUPNE/taxon 106590 and records the original H16/SK4040 sequence source. The current H16_A1553/Q0KBD6 genome sequence is identical at all 382 positions; no redundant genome-paralog review was introduced. The normal UniProt and GOA files remain unchanged.

PMID:31981617 explicitly studies the recombinant Q59104 fusion and forward NAD-dependent 4-hydroxybutyrate oxidation. Its abstract reports product-inhibition analysis, reverse-reaction behavior, and loss of activity after substitution of the four proposed iron ligands. Thus both existing GO0047577 rows are accepted, three broad activity rows refine to that already represented activity, and metal binding refines to iron binding. The ligand mutations corroborate conserved coordination chemistry; they are not described as direct measurement of iron occupancy. No NEW annotation is needed.

PMID:7851418 distinguishes the parental H16/HF39 strains, which did not grow on 4HB, from selected HF39-derived SK4040, which did. Cloned DNA conferred 4HB growth on H16. The physiological role is therefore grounded in selected/expression-dependent strains; the gene summary and module must not imply constitutive wild-type growth. Enzymic and isotope observations support oxidation through succinate semialdehyde to succinate.

Nudix activation in PMID:31981617 uses purified Bacillus methanolicus ACT and Escherichia coli NudF. It is informative enzyme regulation, but neither activator is imported as a native Cupriavidus pathway member or obligatory step. Reverse chemistry is measured; the pathway's oxidative direction follows the physiological context rather than an assumed irreversible reaction.

Normal PMID retrieval, the repository full-text provider chain, and ordinary publisher HTML/PDF attempts did not recover the complete 1995/2020 papers. The accessible abstract explicitly supports the quoted conclusions. No full Methods, exact native regulatory partner, or unreported substrate specificity is claimed. An initially mistyped publisher PII URL returned no content and was discarded; the verified DOI/PII was subsequently tried normally and also returned no cached full text. It supplies no evidence.

Actual Falcon research and perplexity-lite fallback failed authentication; no provider report was fabricated. FEBA retrieval was attempted and failed because no mapped/reachable CUPNE source was available. Original six annotations are preserved in order with their complete non-review payloads. The audit baseline and acquisition logs are recorded in `.cache/module-audit-logs/hydroxybutyrate-panel-baseline.json` and the per-target acquisition reports. History records document the completed review separately.


## PR #5591 source and cofactor follow-up — 2026-10-26

Replaced the downstream SSADH quotation attached to both GO:0047577 rows and the Gbd core with the actual PMID:7851418 sentence linking the structural gene, enzymic analysis, recombinant E. coli and five of six 4HB-negative transposon mutants. Added the corresponding reference finding. This remains the selected-strain genetic/enzymic context, not an invented purified-enzyme kinetic assay. The standalone summary now describes biology without review framing. All original annotation payloads, qualifiers, actions and raw UniProt/GOA bytes are preserved. No NEW annotation was added. Independent bounded consultation agreed that NAD capacity does not imply NADP exclusion. Focused validation, source checks, renders and preservation checks are recorded in the PR #5591 follow-up report.
