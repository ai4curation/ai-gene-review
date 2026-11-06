# eutC (P19636, E. coli K-12) notes

## Sources and literature search
- No deep-research file was generated for this gene (no provider was run in this session). The review rests on
  the UniProt record (`eutC-uniprot.txt`), the cached publications below, the PTHR39330 PAINT file, and the
  shell inventory in `genes/PSEPK/eutC/eutC-bioinformatics/RESULTS.md` (E. coli used as positive control).
- Literature checked (abstract-only in cache): PMID:15466038, PMID:19762342, PMID:20519496, PMID:21142024,
  PMID:29797764, PMID:6376700, PMID:2197274, PMID:23585538, PMID:27450681.

## Biology
- EutC is the small (beta) subunit of AdoCbl-dependent ethanolamine ammonia-lyase
  [PMID:19762342 "The eutB and eutC genes in the eut operon encoded the large and small subunits of the enzyme, respectively. The enzyme existed as the heterododecamer alpha(6)beta(6)."]
- It has no active site of its own; it covers the lower face of the interfacial cobalamin
  [PMID:20519496 "The active site is in the (beta/alpha)(8) barrel of the alpha-subunit; the beta-subunit covers the lower part of the cobalamin that is bound in the interface of the alpha- and beta-subunits."]
- UniProt FT BINDING: adenosylcobalamin contacts at EutC 207, 228, 258 (ECO:0000269 PMID:20519496/21142024 + PDB),
  so EutC binds cobalamin directly (as does EutB at 194, 246, 295, 401).
- The N-terminal ~28-43 residues are dispensable for catalysis (UniProt DOMAIN; PMID:19762342 limited trypsinolysis);
  in Salmonella the EutC 1-19 peptide is a microcompartment targeting signal
  [PMID:27450681 "the signal sequence EutC1-19 targets cargo to the interior of nanocompartments via a hydrophobic interaction with a helix on shell protein EutS"].
- Counterview: [PMID:23585538 "The model predicts that EutBC (ethanolamine-ammonia lyase) lies outside the compartment"].

## Decisions (orchestrator convention, applied across E. coli and KT2440 eutB/eutC)
- GO:0008851 on EutC: the activity term is correct but EutC lacks the active site, so the relation is
  `contributes_to`. All three `enables` rows (two UniProt EXP, one UniProt IEA) -> ACCEPT the term with a
  `source_defects` WRONG_QUALIFIER (enables -> contributes_to), following genes/rat/Kcnj16 and genes/CANAL/VMA8.
  The same treatment is used for the KT2440 eutC IEA row. No NEW contributes_to row is added.
- GO:0031419 cobalamin binding `enables` -> ACCEPT (experimental cobalamin-contact residues in EutC).
- GO:0006520 -> REMOVE; GO:0009350, GO:0046336 -> ACCEPT.
- GO:0031471 KEEP_AS_NON_CORE (E. coli encodes the shell; targeting peptide on EutC; contested);
  GO:0031469 -> MODIFY to GO:0031471.
- Core: contributes_to GO:0008851, in complex GO:0009350, process GO:0046336.

## 2026-11-06 localization and subunit follow-up

This entry supersedes the earlier localization counterview and qualifier certainty above. The 2013 Salmonella external-EutBC statement is a model prediction, not an established E. coli location. PMID:35785499 reports native LT2 immunogold compartment association; PMID:41032589 reports native LT2 cargo/shell imaging and EutQ-mediated encapsulation. Neither is a native E. coli assay. PMID:27450681 explicitly used Salmonella LT2 proteins in a heterologous E. coli host. E. coli MC4100 cytosol proteomics (PMID:18304323, EutB) supports the inherited location annotation through curator-reviewed tables not independently recovered here, but fractionation does not identify the site of ethanolamine-induced catalytic flux. Thus no E. coli compartment flux location is imposed on the core. The specific BMC row remains a conditional inferred non-core location; the broad BMC row remains refined to it.

EutB retains catalytic-subunit enables within the holoenzyme, without implying autonomous turnover. EutC contributes_to in the core reflects its cofactor-interface role. Its three source-specific enables concerns are PROBABLE, not CONFIRMED: the source convention must be checked, and neither isolated inactivity nor an active-site barrel in its partner automatically determines the qualifier. The original payloads, including enables, are preserved. Exact structural support remains PMID:20519496: “The active site is in the (beta/alpha)(8) barrel of the alpha-subunit; the beta-subunit covers the lower part of the cobalamin that is bound in the interface of the alpha- and beta-subunits.” No NEW annotations or action changes were made. Existing source caches were not refreshed.
