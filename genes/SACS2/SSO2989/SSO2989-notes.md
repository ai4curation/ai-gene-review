# SSO2989 (UniProt Q97UL5) - Saccharolobus solfataricus P2

## 2026-11-18 review notes

### Literature search

No deep-research provider was available. PubMed (NCBI E-utilities):
`Sulfolobus[tiab] AND mevalonate[tiab]` (8 hits) and `PTO1356 OR Ta0893 OR SSO2989 OR HVO_1412`
(no hit for SSO2989; papers use "S. solfataricus DMD"). Papers assaying SSO2989:
PMID:23378249 (activity, pathway; abstract only), PMID:26303832 (crystal structure, disulfide;
abstract only), PMID:28003359 (substrate complexes, Asp281 mutants; abstract only). PMC/Europe PMC
full text could not be retrieved (publisher-restricted, HTTP 403/500).

### Reaction

- Classical diphosphomevalonate decarboxylase (EC 4.1.1.33; RHEA:23732):
  (R)-5-diphosphomevalonate + ATP = isopentenyl diphosphate + ADP + CO2 + phosphate.
  [PMID:23378249 "Biochemical characterization using recombinant proteins showed that the
  orthologues of the enzymes catalyzing the late steps of the classical pathway, i.e. MVA kinase,
  PMK and DMD, are all active."]
- Two half-reactions, shown with this enzyme: Asp281 mutants become MVAPP 3-kinases.
  [PMID:28003359 "Site-directed mutagenesis on Asp-281 creates mutants that only show
  diphosphomevalonate 3-kinase activity, demonstrating that the residue is required in the
  process of phosphate elimination/decarboxylation, rather than in the preceding phosphorylation
  step."] Structures 5GMD (MVAPP + ATPgammaS) and 5GME (MVAPP + ADP).
- The organism uses the classical pathway: [PMID:23378249 "in vitro conversion of the
  intermediates in the classical and modified pathways by cell-free extract from S. solfataricus
  indicated that only the classical pathway likely works in the organism."]
- Homodimer with an intersubunit disulfide that forms in vivo and stabilises the enzyme
  [PMID:26303832 "Western blot analysis combined with nonreducing SDS-PAGE of the whole cells of
  S. solfataricus proved that the disulfide bond was predominantly formed in the cells."]
  Structures 4Z7C, 4Z7Y.

### PAINT / family

- PANTHER PTHR10977:SF3. In the PANTHER 19 tree SSO2989 (Q97UL5) is a direct leaf of
  PTN000104601 (Archaea-Eukaryota), the IBD node for GO:0004163, GO:0019287 and GO:0005829; it is
  the only archaeal leaf under that node (`../../HALVD/mvaD/mvaD-bioinformatics/RESULTS.md`).
- `just paint-losses SACS2 SSO2989`: no IRD or IKR on this lineage.
- All three IBAs judged sound for this member.
- Sulfolobales carry the eukaryote-type PMK + DMD, thought to have arrived by horizontal transfer
  [PMID:38674651 "The order Sulfolobales was considered as the sole archaeal taxon that encodes
  the eukaryote-type MVA pathway as a consequence of HGT [10]."].

### Annotation decisions

| Term | Evidence | Action |
|---|---|---|
| GO:0004163 diphosphomevalonate decarboxylase activity | IBA | ACCEPT |
| GO:0004163 diphosphomevalonate decarboxylase activity | IEA (IPR029765/RHEA/EC) | ACCEPT |
| GO:0005829 cytosol | IBA | ACCEPT |
| GO:0005829 cytosol | IEA (IPR029765) | ACCEPT |
| GO:0008299 isoprenoid biosynthetic process | IEA (IPR005935) | ACCEPT |
| GO:0016831 carboxy-lyase activity | IEA (IPR005935) | TOO_GENERAL (IPR005935 spans DMD, PMD and MBD, so row evidence cannot support MODIFY) |
| GO:0019287 IPP biosynthesis, mevalonate pathway | IBA | ACCEPT |
| GO:0019287 IPP biosynthesis, mevalonate pathway | IEA | ACCEPT |
