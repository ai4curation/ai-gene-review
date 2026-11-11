# PDIA4 (human, P13667) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: human PDIA4 is the experimentally characterised reference for the HORSE40
ProtNLM2 cohort gene HORSE/PDIA4 (A0A3Q2IEH6). This review is of human PDIA4 in its own
right; no ProtNLM2 file or prediction evidence was opened or used.

### Deep research

`just deep-research-falcon human PDIA4 --fallback perplexity-lite` failed: falcon
returned "Exception: Failed to authenticate" and the perplexity-lite fallback returned
HTTP 401 (insufficient quota). No deep-research file exists. The review is based on the
UniProt record, GOA rows, PAINT data in `interpro/panther/PTHR18929/` and cached
publications read directly (abstracts, and full text where available).

### Evolutionary grounding

- UniProt DR: PANTHER PTHR18929:SF210 "PROTEIN DISULFIDE-ISOMERASE A4"; InterPro
  IPR017068 Protein_diS-isomerase_A4 and IPR041866 PDIA4_PDI_b (subfamily-specific
  signatures). Mouse Pdia4 (P08003) and rat Pdia4 (P38659), the ISS donors, are
  one-to-one orthologs in the same subfamily, so transfer of their experimental
  isomerase/folding data is warranted.
- PAINT (`PTHR18929-paint.tsv`): PTN000432607 (deep PDI-family node) carries IBD for
  GO:0003756, GO:0005783, GO:0006457, GO:0034976. Human PDIA4 itself is a seed only
  for GO:0005783 at that node; the GO:0003756 seeds include mouse Pdia4 (MGI:104864,
  whose IDA is from PMID:28576878) and other PDI-family members. PTN001448731
  (taxon 6072, Eumetazoa) carries GO:0009986 cell surface seeded by MGI:104864 and
  human P13667 (PMID:19995400).
- PAINT did not propagate mouse Pdia4's IMP platelet-aggregation /
  blood-coagulation terms (acts_upstream_of_or_within, PMID:28576878) or its integrin
  binding IPI. Treated as a deliberate decision: no NEW process terms added for
  thrombosis.

### Literature findings (human unless stated)

- Domain architecture: a0-a-b-b'-a', three CGHC active sites, C-terminal KEEL ER
  retention [PMID:2295602 "ERp72 appears to be a newly described member of the family
  of CGHC-containing proteins"; PMID:19446521 (rat ERp72 structure) "define the relative
  positions of the five thioredoxin-like domains of ERp72"].
- Enzyme activity: recombinant human ERp72 has peptide thiol-disulfide oxidase
  activity similar to PDI [PMID:16677074]. Insulin-reduction assay shows all three
  thioredoxin domains contribute to catalysis [PMID:16333982; organism of construct not
  stated in abstract].
- Oxidative folding in cells: in human hepatoma cells ERp72 depletion alone had minimal
  impact but showed overlap with PDI for albumin oxidation; narrow substrate
  specificity [PMID:20660153].
- Misfolded-substrate engagement: ERp72 co-precipitates with misfolded mutant
  matrilin-3 A-domains, not wild type [PMID:16287128]; substrate-trapping mutant forms
  mixed disulphides with mutant matrilin-3 in mouse MED models [PMID:23956175].
- ER quality control: ERp72 mediates ER retention of cholera toxin, opposing PDI
  [PMID:16785320].
- Partners: ERp72-cyclophilin B complex enhances IgG folding [PMID:22665516]; ERp72 does
  not bind calnexin [PMID:19446521].
- Extracellular/cell surface: released from human platelets and relocates to the
  platelet surface after activation [PMID:19995400]; mouse conditional KO shows role in
  platelet function and thrombosis via a and a' CGHC motifs, and recombinant ERp72
  potentiates human platelet aggregation [PMID:28576878].
- Viral entry: PDIA4 binds HAstV-1/-8 spikes and is involved in genome uncoating
  [PMID:33396308].

### Decisions summary

- Core: protein disulfide isomerase activity / thiol-disulfide oxidoreductase activity in
  the ER lumen, protein folding in ER (MODIFY protein folding -> GO:0034975).
- MATN3 IPI rows -> MODIFY to misfolded protein binding (GO:0051787).
- Other protein binding IPI rows removed per protein-binding policy.
- RNA binding (HeLa interactome capture) marked over-annotated: luminal protein.
- Protein secretion TAS removed: the paper assayed ERp72's own KEEL-dependent retention.
- Melanosome, extracellular region, cell surface, response to ER stress kept as non-core.
