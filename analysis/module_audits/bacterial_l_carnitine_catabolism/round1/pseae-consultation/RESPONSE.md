# PR6182 finding 3: CbcV and CbcW evidence mapping

Addressed across all 27 CbcV and 25 CbcW rows. Each cargo claim now cites its actual
uptake evidence; transporter-composition text is limited to component/complex
roles and supplemented with functional reconstitution. The original 52 ordered
payloads, actions, qualifiers and proposal lifecycle are unchanged. No NEW rows,
retirements, publication refreshes or other source changes were needed.

- Choline and glycine betaine: PMID19919675 measures accumulation in E. coli
  MKH13 expressing PAO1 cbcXWV, with empty-vector controls. BetX/core
  reconstitution provides independent betaine-specific recognition evidence.
- Carnitine: core-plus-CaiX reconstitution is distinguished from CbcX transport
  and core-only controls. The tested Table 5 partner includes B728a CaiX; the
  PAO1 core is not relabeled as a fully native PAO1 transporter experiment.
- COS: the full PMID23763788 Results/Figure 5 explicitly compares pNCbcWV,
  pNCbcXWV and empty pN in B728a binding-protein mutants. Core-dependent,
  CosX-dependent QAC-uidA induction supports conditional cellular entry. The
  PAO1 origin of the plasmid core is established by PMID19919675. Thus the
  sulfur-cargo NON_CORE verdict remains justified, with reporter-based evidence
  distinguished from purified flux and native PAO1 physiology. Free sulfate
  specificity remains corrected, not silently equated with a sulfate ester.
- Osmotic response: PMID21478341 PA14 comparisons support condition-dependent
  nutritional uptake; they do not settle a native PAO1 CbcV stress role. The
  UNDECIDED verdict is retained with the relevant osmolarity experiment.
- ATP binding/hydrolysis and membrane location: source-specific sites,
  signatures and curated RuleBase topology support the subunit mechanism.
  No isolated target ATPase kinetics or native fractionation is invented.
- Nearby description suggestion: removed CbcV's negative sulfate/degradation
  commentary from the standalone biological description.

PMID19919675 is available as preserved full cached primary text. PMID21478341
and PMID23763788 were re-read at the full publisher URLs; their abstract-only
publication caches were intentionally not overwritten. Short excerpts and
controls are in primary-evidence.md. No new publication was fetched.

Both focused gene validations, both reference checks, both renders and both
helper histories pass. Four existing structured-propagation advisories remain
(two per review, IBA MODIFY rows); no new PAINT judgment is claimed in this
bounded evidence repair. Record-section backfill reports no additions or
mismatches. The preservation checker proves all 52 ordered payloads/actions and
all 63 parent-baseline protected files unchanged. No module logic/core activity
or family selector changes are required from these repairs.
