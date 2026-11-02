# Smn (DROME, Q9VV74) review notes

## Session 1 (initial review)

- Fetched with `just fetch-gene DROME Smn`; UniProt Q9VV74 (SMN_DROME, Swiss-Prot,
  FlyBase FBgn0036641, GeneID 39844) confirmed. 82 GOA rows.
- No deep-research API available; literature synthesis written by hand in
  `Smn-deep-research-manual.md` from cached publications.
- Abstract-only in cache: PMID:12783845, 14605208, 14715275, 17595295, 18923150,
  19464282, 21627586, 21939654, 38944040. Experimental rows citing these were not
  overruled; actions defer to curators where the abstract is consistent.

### Key judgements

- Core: SMN complex (SMN-Gemin2 core) assembles Sm cores on snRNAs
  [PMID:18621711 "An affinity chromatography strategy has permitted us the purification
  of an assembly-active complex composed of SMN and Gemin2 only."]. Accepted
  spliceosomal snRNP assembly, SMN complex, SMN-Gemin2 complex, SmD-containing SMN-Sm
  protein complex, cytoplasm and U body.
- mRNA splicing (IMP): kept as non-core. Note PMID:22813737 is cited for this term,
  but its full text reports no appreciable minor-intron splicing defects
  [PMID:22813737 "Despite these reductions, we found no appreciable defects in the
  splicing of mRNAs containing minor-class introns."]. The term is still supported by
  PMID:23063131 (U12 intron retention in smn73Ao larvae). Flag the 22813737 row to
  FlyBase as a possible misreading.
- Protein binding (GO:0005515) rows: REMOVE per policy (Gem2/Gem3 partnership is
  captured by SMN complex / SMN-Gemin2 complex; Rpp20 and human SMN2 from Y2H).
- Identical protein binding: MODIFY to protein homodimerization activity (YG-box
  homodimer; UniProt FT REGION 159..226).
- Plasma membrane IEA (inferred from AMPA receptor clustering) REMOVE: Smn is a
  soluble cytoplasmic/nuclear protein; the inter-ontology inference is unsound.
- Phenotype-derived BP terms: mostly KEEP_AS_NON_CORE. MARK_AS_OVER_ANNOTATED for:
  positive regulation of cholinergic synaptic transmission (cholinergic transmission
  not measured; NMJ release is increased in mutants), AMPA glutamate receptor
  clustering (fly NMJ GluRIIA receptors are not AMPA-type; indirect), basal protein
  localization (Miranda mislocalization is a downstream phenotype), excitatory
  postsynaptic potential (physiological readout, not a process Smn executes), RNA
  binding IEA (InterPro mapping; Smn's Tudor domain binds methylarginine Sm tails, not
  RNA directly in fly assays).
- Tracheal lumen formation (PMID:23029159, full text read): single RNAi line,
  gas-filling readout, no rescue; kept as non-core.
- No NEW process terms proposed (NEW-term bar: phenotype data does not establish
  participation). One NEW MF row: contributes_to protein carrier chaperone
  (GO:0140597), IDA from PMID:18621711 (Smn-Gemin2 dimer loads Sm proteins and
  transfers them only to cognate snRNAs).

### Open questions

- Is the reported link between Smn and the Zpr1 pathway in tracheal terminal cells
  dependent on snRNP assembly?
- Which snRNP-independent activities (alpha-actinin / sarcomere, FGF signalling) are
  real direct functions?

## 2026-10-28 review fixes

Removed the restating manual-file quote from the NEW GO:0140597 row (PMID:18621711 covers it); cited the manual's synthesis of the conflicting minor-intron splicing reports on the PMID:22813737 splicing row instead.
