# nuoF (E. coli K-12, P31979) notes

## 2026-10-23 / 2026-11-01 review session

Deep-research providers are unavailable in this environment (no API keys), so
literature was reviewed manually from the cached publications/ files and the
UniProt record. Full text available for PMID:18316732 and PMID:9495756; others
abstract-only.

- NuoF holds the NADH site and FMN and cluster N3 [PMID:15922336 "The NuoF
  subunit, which harbors NADH-binding site"; "we identified that cluster N3 is
  ligated to the 351Cx2Cx2Cx40C398 motif"].
- Glu95 in the catalytic site: E95Q lowers NADH oxidation 2.5-4.8x, changes Ki for
  NAD+ / ADP-ribose and shifts FMN Em from -350 to -310 mV [PMID:19061856].
- nuo mutants (incl. polar nuoF::miniTn10Cm) are complex I deficient and cannot
  "use acetate effectively as a sole carbon source" [PMID:9495756].
- Electron entry: "two electrons move via the FMN cofactor to the iron"
  [PMID:18316732].

Decisions:
- Core MF GO:0003954 NADH dehydrogenase activity (module leaf function);
  contributes_to GO:0008137; process GO:0022904; complex GO:0045271; location
  GO:0005886.
- GO:0045333 cellular respiration (IBA) MODIFY -> GO:0022904 (granularity); node
  PTN000207323 judged sound.
- GO:1902600 proton transmembrane transport kept as non-core (NuoF supplies the
  electrons that drive pumping but does not translocate protons).
- membrane -> plasma membrane; NADH dehydrogenase complex -> complex I.
- No GO:0050136 row exists for E. coli nuoF.

PANTHER placement disagreement: UniProt/InterPro put P31979 in PTHR43578:SF3
(with HoxF/HndC hydrogenase subunits), while PANTHER 19.0's own classification
file (.cache/panther/PTHR19.0_e_coli) puts nuoF in PTHR11780:SF10 with
mitochondrial NDUFV1; PAINT node PTN000207323 (source of the IBAs) is in the
PTHR11780 tree. Recorded in interpro/panther/PTHR43578/PTHR43578-review.yaml.
