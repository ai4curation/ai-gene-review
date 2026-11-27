# apg-6 / ATG8 notes

## 2026-10-21

- Reviewed the `PTHR10969` PAINT rows for the cross-fungal ATG8 family.
  `PTN000103522` is the eukaryotic ATG8 node that propagates autophagosome
  membrane, phosphatidylethanolamine binding, autophagosome assembly, mitophagy,
  cellular response to nitrogen starvation, and autophagosome maturation to the
  Neurospora crassa member; `PTN000861115` is the Fungi-level node that
  propagates fungal-type vacuole membrane from curated SGD and PomBase seeds.
- N. crassa APG-6 is a single-copy member of the fungal ATG8 branch in the
  cached PANTHER entries table and UniProt classifies Q8WZY7 in `PTHR10969`.
  I did not find evidence that the Neurospora protein has diverged from the
  conserved ATG8 lipidation cycle.
- The direct N. crassa literature hit for `atg-8`/`NCU01545` was the Fu et al.
  deletion-library screen [PMID:21666072], which reported that `atg-8`
  mutants were among strains "apparently required for intracolonial hyphal cell
  fusion without being essential for CAT formation" and that "the phenotypes of
  the ham-4 (NCU00528), atg-8 (NCU01545), nox-1 (NCU02110), ro-11 (NCU08566),
  and ro-6 (NCU9142) mutants have been verified by complementation and RIP
  experiments". This supports an apg-6 loss phenotype but does not establish a
  direct APG-6 activity in cell fusion, so I did not add a cell-fusion GO term.
- The UniProt record also transfers by-similarity nucleophagy, ER-specific
  autophagy/survival, early secretory-pathway membrane fusion, and Atg8-PE
  tethering/hemifusion statements from S. cerevisiae. These statements were not
  promoted to new N. crassa annotations because the organism-specific evidence
  is absent and the current GOA/PAINT rows already cover the conserved
  autophagosome-membrane function.
- PubMed/open-web searches for `Neurospora crassa apg-6 Atg8 autophagy
  NCU01545` and 2024-2026 ATG8 papers found NCBI/FungiDB-style gene pages and
  papers that use NCU01545 as an ortholog in comparative figures, but no newer
  primary N. crassa APG-6 biochemical or localization study.
- Kept the mitophagy and nitrogen-starvation response IBAs as non-core:
  selective autophagy and starvation autophagy use the conserved ATG8 platform,
  but APG-6's direct activity is phosphatidylethanolamine-conjugated
  autophagosome membrane modification.
- Marked the two generic vacuolar membrane rows as too general because the
  same review accepts the fungal-type vacuole membrane IBA from the
  Fungi-level ATG8 PAINT node.
