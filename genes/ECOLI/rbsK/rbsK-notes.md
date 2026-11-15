# rbsK (Escherichia coli K-12, P0A9J6) curation notes

## 2026-11-11 initial review

- Reviewed as the E. coli exemplar of the RbsK ribokinase step in `modules/bacterial_ribose_uptake_and_entry.yaml`.
- Deep research was not run: no deep-research provider credentials were available in this environment,
  and no `-deep-research-<provider>.md` file was created. The review relies on the cached publications
  cited by GOA (`publications/PMID_*.md`, mostly abstract-only) and the curated UniProt record.
- RbsK is a soluble, homodimeric PfkB-family ribokinase. It is not a subunit of the RbsABC2 transporter,
  and GOA has no protein-binding row for it.
- Ribokinase activity is directly assayed [PMID:11563694 "the catalytic activity of E. coli ribokinase is
  also affected by PVI, increasing both the velocity and affinity of the enzyme for D-ribose"] and
  [PMID:16784868 "Besides D-ribose and 2-deoxy-D-ribose, RK was found to catalyze the 5-O-phosphorylation
  of D-arabinose, D-xylose, and D-fructose"]. D-ribose is the preferred substrate. Activity on the other
  sugars is much weaker and is not annotated.
- Refinements with MODIFY: kinase activity and phosphotransferase activity to ribokinase activity, D-ribose
  metabolic process to D-ribose catabolic process, cytoplasm to cytosol, and metal ion binding to
  potassium ion binding [PMID:11786021 "Escherichia coli ribokinase is activated by potassium with an
  apparent K(d) of 5 mM"].
- The PMID:18304323 cytosol row is supported by that paper's cytosolic-fraction proteome. RbsK appears in
  its data tables rather than in its text.
