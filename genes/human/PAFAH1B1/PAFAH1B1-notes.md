# PAFAH1B1 (LIS1) review notes

## 2026-09-27 initial review (claude-code)

Sources: UniProt P43034, cached GOA-cited publications, plus newly cached PMID:20403325 and PMID:22956769 (both verified via PubMed esummary). No Falcon deep-research file was present at review time.

Two separable roles:

1. **Dynein-1 regulator (core).** LIS1 binds the dynein motor domain in the pre-powerstroke state and induces a persistent-force state [PMID:20403325 "LIS1 alone or with NudE induces a persistent-force dynein state that improves ensemble function of multiple dyneins for transport under high-load conditions"]. Human cryo-EM defines the LIS1-dynein interface [PMID:36692009 "Here, we report cryo-EM structures of human dynein-LIS1 complexes"]. LIS1 also contacts dynactin p150 during complex assembly [PMID:38547289 "Unexpectedly, LIS1 binds dynactin's p150 subunit, tethering it along the length of dynein."]. In migrating neurons it couples the nucleus to the centrosome [PMID:15173193 "Lis1 and Dcx function with dynein to mediate N-C coupling during migration"], and knockdown in rat progenitors abolishes interkinetic nuclear oscillations [PMID:16144905 "interkinetic nuclear oscillations in the radial glial progenitors were also abolished"].
   - MF chosen: GO:0140659 cytoskeletal motor regulator activity (added as NEW; matches the nucleokinesis module). GO:0140660 activator was not used because LIS1 both promotes assembly and restrains motility depending on context.
2. **PAF-AH (I) beta subunit (non-catalytic).** UniProt: "The catalytic activity of the enzyme resides in the alpha1 (PAFAH1B3) and alpha2 (PAFAH1B2) subunits, whereas the beta subunit (PAFAH1B1) has regulatory activity". Crystal structure [PMID:15572112 "One LIS1 homodimer binds symmetrically to one alpha2/alpha2 homodimer via the highly conserved top faces of the LIS1 beta propellers"]. Captured with complex GO:0008247 (ACCEPT) and NEW GO:0030234 enzyme regulator activity; PAF metabolic/catabolic process kept as non-core (LIS1 does not catalyse).

Decisions of note:
- 21 protein-binding rows: 2 MODIFY (DYNC1H1 structural papers -> dynein heavy chain binding; + dynactin binding for PMID:38547289); rest REMOVE as uninformative.
- Behavioural/synaptic IMP/ISS rows from patient-mutation and Lis1+/- mouse papers marked over-annotated (indirect consequences of migration defects).
- Heparin binding (ISS from bovine IDA, PMID:8028668): UNDECIDED; abstract silent, likely purification behaviour.
- nuclear migration IEA: MODIFY to nuclear migration along microtubule + interkinetic nuclear migration.
