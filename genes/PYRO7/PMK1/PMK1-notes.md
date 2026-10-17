# PMK1 (Pyricularia oryzae 70-15, G4N0Z0, MGG_09565) — curation notes

## 2026-10-02 — initial review

Sources: UniProt G4N0Z0, GOA (13 rows), falcon deep research, cached PMIDs 8946911 (abstract only),
29567712 (abstract only), 34707224 (abstract only), 11952120 (abstract only), 15749760 (full text),
38252344 (full text).

### Identity / molecular function
- Fus3/Kss1-type MAPK (CMGC; TEY activation loop). [PMID:8946911 "The PMK1 gene of M. grisea is
  homologous to the Saccharomyces cerevisiae MAP kinases FUS3/KSS1, and a GST-Pmk1 fusion protein has
  kinase activity in vitro."]
- Complements yeast fus3 kss1 mating defect [PMID:8946911 "PMK1 can rescue the mating defect in a fus3 kss1 double mutant"].
- Native substrates: Hox7 and Mst12 (Pmk1-dependent phosphorylation) [PMID:34707224 "Pmk1-dependent
  phosphorylation of the Hox7 homeobox transcription factor"; "Pmk1-dependent phosphorylation of Mst12
  then regulates gene functions involved in septin-dependent cytoskeletal re-organization, polarized
  exocytosis and effector gene expression"]; fimbrin MoFim1 Ser94 in vitro [PMID:38252344 "In the presence
  of Pmk1, MoFim1 was phosphorylated."; "S94A but not S117A lost phosphorylation"].

### Pathway
- Terminal kinase of Mst11 (MAPKKK) - Mst7 (MAPKK) - Pmk1 cascade; Mst50 adaptor. [PMID:15749760
  "These data indicate that MST11 , MST7 , and PMK1 function as a MAP kinase cascade regulating
  infection-related morphogenesis in M. grisea ."] Pmk1 TEY phosphorylation detected in appressoria and
  constitutively-active MST7 transformants.
- Acts downstream of cAMP for appressorium formation [PMID:8946911 "suggests Pmk1 acts downstream of a cAMP signal"].
- Mst12 (Ste12 homolog) downstream for penetration/invasive growth, not appressorium formation [PMID:11952120].

### Processes
- Appressorium formation: pmk1 mutants fail to form appressoria [PMID:8946911]. Core.
- Cell-to-cell invasion: analog-sensitive chemical-genetic inhibition after invasion traps fungus in first
  cell; Pmk1 controls hyphal constriction at pit fields and effector expression [PMID:29567712]. Temporally
  separable from appressorium defect, so this is a genuine Pmk1 signalling role in a fungal developmental
  process, not just a secondary consequence of failing to penetrate.
- Hyphal growth: not essential in culture [PMID:8946911 "PMK1 is nonessential for vegetative growth"], but
  Pmk1->MoFim1 phosphorylation affects hyphal-tip actin and growth [PMID:38252344]. Non-core.
- Septin ring assembly: Pmk1 is upstream (via Mst12) of septin reorganisation; it regulates rather than
  builds septin rings. Kept as non-core rather than overruling the IMP curator (full text not cached).

### Location
- No GO CC annotations. Deep research reports GFP-Pmk1 nuclear in appressoria (Bruno et al. 2004, not
  cached) -> not asserted.

### Project-relevant observations
- PMK1 is a fungal signalling kinase; GOA uses symbiont-side terms (positive regulation of appressorium
  formation; symbiont-mediated cell-to-cell migration by invasive hypha), not plant defence terms. No
  host-immunity-suppression term is annotated, even though Pmk1 controls effector gene expression - which
  is correct, since that would be indirect (effectors do the suppression).
