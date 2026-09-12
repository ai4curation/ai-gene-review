# SSQ1 review notes

## 2026-08-12 re-review

- Identity verified as *Saccharomyces cerevisiae* SSQ1/YLR369W, UniProt Q05931,
  the mitochondrial Ssq-type Hsp70 dedicated to iron-sulfur cluster biogenesis.
- The existing Falcon report is correctly scoped to Q05931. An OpenScientist
  run was launched through `just deep-research-openscientist yeast SSQ1`; after
  extended silent polling without a returned artifact it was interrupted. No
  unreturned result was treated as evidence.
- Core mechanism: Jac1 recruits the Isu scaffold and stimulates the Ssq1 ATPase
  cycle; Mge1 promotes nucleotide exchange; Ssq1 recognizes the Isu LPPVK motif
  and drives release/handoff of the newly assembled cluster to Grx5.
- UniProt resolves the GOA IntAct partners directly: Q03020 is the physiological
  Isu1 scaffold client, whereas P15646 is the nucleolar protein Nop1. The Isu1
  rows are biologically relevant but poorly expressed by bare protein binding;
  the Nop1 rows are likely high-throughput background for a matrix protein.
- Generic family terms were narrowed where a more informative child exists:
  GO:0044183 and GO:0051082 are modified to GO:0140662, generic nucleotide and
  hydrolase parents are over-annotated, and mitochondrial matrix is the core
  location rather than its broad organelle/lumen parents.
- GO:0042026 protein refolding is an unsafe general-Hsp70 IBA transfer. Ssq1 is
  specialized for the Isu client and ISC transfer rather than broad stress
  refolding; the propagation audit records this functional divergence.
- The cytoplasm IBA is ontologically true because mitochondria are part of the
  GO cytoplasm, but it is marked over-annotated because matrix is the precise
  functional compartment. Intracellular iron homeostasis is retained as a
  genuine downstream phenotype, not a core direct function.

## 2026-08-28 completion audit

- Reconciled all 29 GOA rows by the exact machine signature (GO term, evidence
  code, reference, and qualifier); `just validate-goa yeast SSQ1` passes and no
  review remains `PENDING`.
- Audited all seven IBA rows against the current GOA `WITH/FROM` field and
  `interpro/panther/PTHR19375/PTHR19375-paint.tsv`. The actual PAINT nodes are
  PTN002321897 for cytoplasm, PTN000452554 for mitochondrion and iron-sulfur
  cluster assembly, and PTN000452648 for ATP hydrolysis, heat-shock-protein
  binding, protein-folding chaperone, and protein refolding. SSQ1 appearing
  among the experimental descendants for conserved ATPase/ISC assertions is
  expected phylogenetic grounding, not circularity.
- The core ATPase and ISC-transfer calls have direct target evidence. Jac1 and
  Isu1 stimulate Ssq1 ATPase [PMID:12756240, "Jac1 and Isu1 cooperatively
  stimulate the ATPase activity of Ssq1."], and a ferredoxin maturation assay
  established a mitochondrial Fe-S assembly requirement [PMID:11273703,
  "Ssq1 was demonstrated to be required for the FeS cluster assembly in
  mitochondria."].
- GO:0051082 is retained only as the imported legacy row and changed to
  `MODIFY` because the term is obsolete, not because the experiment is weak:
  Ssq1 directly showed ATP-regulated binding to unfolded substrates
  [PMID:11601843, "Ssq1 showed typical chaperone properties by binding to
  unfolded substrate proteins in an ATP-regulated manner."]. GO:0140662 is the
  proposed replacement already used in the core-function synthesis.
- Live-ontology recheck on 2026-08-28 confirmed this obsoletion in the official
  EBI OLS GO record (`is_obsolete: true`, label `obsolete unfolded protein
  binding`, with `consider` GO:0044183 and GO:0140309). The repository cache row
  that still says `False` is timestamped 2026-03-21, and the SSQ1 GOA/UniProt
  snapshots are dated 2026-01; all predate closure of the official GO obsoletion
  request on 2026-05-29 (geneontology/go-ontology#30962). They are stale evidence
  for current term status, not a contradiction of the live ontology.
- GO:0042026 remains marked as an over-propagated general-Hsp70 process rather
  than removed. The available literature establishes specialized ISC client
  handling but does not provide a target-specific refolding assay; this avoids
  claiming loss of all refolding capacity from incomplete evidence.
- The five protein-binding IPI rows were retained as over-annotated rather than
  removed. Isu1 is the physiological client, while the Nop1 rows are
  compartmentally discordant high-throughput observations; bare protein binding
  is uninformative in either case.
- Final curation state: 9 `ACCEPT`, 8 `KEEP_AS_NON_CORE`, 10
  `MARK_AS_OVER_ANNOTATED`, 2 `MODIFY`, 0 `PENDING`; status set to `COMPLETE`.
