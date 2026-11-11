# BTBD3 (chicken, UniProt F1NI11) — curation notes

Falcon deep research could not be run for this gene (authentication failure), so
these notes are a manual literature review built from PubMed searches, the cached
publications and QuickGO/OLS queries made on 2026-10-19.

## Entry identity

`F1NI11_CHICK` is an unreviewed (TrEMBL, PE 4 "Predicted") Ensembl-derived entry,
520 aa, gene name BTBD3, GeneID 427688, chromosome 3. Domain content is the
canonical BTBD1/2/3/6 architecture: BTB/POZ (IPR000210, PF00651), BACK
(IPR011705, PF07707) and PHR (IPR012983, PF08005); PANTHER PTHR45774:SF2
"BTB_POZ DOMAIN-CONTAINING PROTEIN 3"; CDD cd18348 BTB_POZ_BTBD3 and cd18524
BACK_BTBD3. The only subcellular location statement (Cytoplasm) rests on an
ARBA rule (ECO:0000256|ARBA:ARBA00004496), i.e. an unvetted prediction.

No chicken- or bird-specific BTBD3 study exists: a PubMed search for
`(BTBD3 OR Btbd3) AND (chicken OR avian OR bird OR zebra finch OR Gallus)`
returned 0 hits (2026-10-19). Everything known about function comes from mouse
(and ferret).

## Function in mammals

- Mouse Btbd3 orients primary dendrites of layer 4 neurons in the developing
  barrel cortex toward active thalamocortical axons:
  [PMID:24179155 "In developing mouse somatosensory cortex, endogenous Btbd3 translocated to the cell nucleus in response to neuronal activity and oriented primary dendrites toward active axons in the barrel hollow."]
- The function is cross-species/cross-area within mammals:
  [PMID:24179155 "Btbd3 also directed dendrites toward active axon terminals when ectopically expressed in mouse visual cortex or normally expressed in ferret visual cortex."]
  The cached record is abstract only.
- Mouse UniProt P58545 (Swiss-Prot) curates, from PMID:24179155: "Acts as a key
  regulator of dendritic field orientation during development of sensory cortex"
  and location "Cytoplasm, cytosol ... Nucleus ... Translocates from the cytosol to
  the nucleus in response to neuronal activity"; expression in spiny stellate
  neurons during barrel formation, plus olfactory bulb, piriform cortex and
  hippocampus (UniProt REST, fetched 2026-10-19; not cached in repo).
- Btbd3 knockout mice: compulsive-like behaviour and reduced exploration, but only
  modest dendritic changes outside sensory cortex:
  [PMID:31501410 "Surprisingly, Btbd3 knockout mice only showed modest increases in spine density in the anterior cingulate, while dendritic morphology was unaltered elsewhere."]
  and [PMID:31501410 "BTBD3 was found to orient dendrites toward active axon terminals and regulate activity-dependent dendritic pruning in primary sensory cortex during neonatal development, thus facilitating neural circuit formation"].
  The same paper calls it [PMID:31501410 "a putative transcription factor"]; no DNA-binding or
  transcriptional activity has been demonstrated.
- A colorectal-cancer study calls BTBD3 an E3 ligase that ubiquitinates
  beta-catenin [PMID:39227913 "BTBD3 bound and ubiquitinated β-catenin and led to β-catenin degradation"].
  BTB proteins typically act as CUL3 substrate adaptors rather than ligases
  themselves; this single cancer-cell-line study is not treated as establishing a
  molecular function, and it is not relevant to the chicken neural annotations.
- Human BTBD3 self-interaction (homodimer) was detected in the HuRI binary
  interactome (PMID:32296183, IntAct IPI GO:0042802 on Q9Y2F9), which is the
  source of the chicken Ensembl IEA "identical protein binding" row. BTB domains
  generally dimerize, so this is plausible but mechanistically uninformative.

Molecular function: not established. No GO MF term is justified beyond the
inherited self-association.

## The cerebral cortex question (RAR_MISANNOTATION / Wei et al. 2020)

### What the GO term says and what constrains it

- GO:0021987 cerebral cortex development, definition (QuickGO, 2026-10-19):
  "The cerebral cortex is the outer layered region of the telencephalon."
  Synonyms: corticogenesis (narrow), neocortex development (related).
- It is `part_of` GO:0021543 pallium development ("The pallium is the roof
  region of the telencephalon"), itself `part_of` GO:0021537 telencephalon
  development.
- Taxon constraint on GO:0021987: only `only_in_taxon Bilateria` (inherited);
  nothing excludes birds or fish. GO:0021543 carries the same Bilateria constraint.
- UBERON:0000956 cerebral cortex is defined as "The thin layer of gray matter on
  the surface of the cerebral hemisphere ... It consists of the neocortex (6
  layered cortex or isocortex), the hippocampal formation and the olfactory
  cortex", `part_of` UBERON:0000203 pallium. No never_in_taxon Aves (OLS, 2026-10-19).

### How the term is used in birds

- QuickGO, GO:0021987 exact, Aves (taxon 8782 and descendants): 1759 annotations,
  essentially all IEA (TreeGrafter GO_REF:0000118, Ensembl Compara GO_REF:0000107);
  only 2 are IBA (chicken BTBD3 and KIF14).
- Chicken (9031): 25 rows — 22 Ensembl IEA, NTRK2 ISS, and IBA for BTBD3 and KIF14.
- GO:0021543 pallium development, Aves: 0 annotations.
- Zebrafish: 3 rows (2 IBA, 1 ISS). So the term is propagated to non-mammals,
  including those whose pallium is everted and has no layered cortex, purely by
  homology inference; none of it is experimentally grounded outside mammals.

### The PAINT node

- PTN002908884 is the vertebrate BTBD3 orthology node: QuickGO rows citing it
  span lamprey (7757), cartilaginous and bony fishes (btbd3a/btbd3b), Xenopus,
  reptiles, chicken and mammals. The only experimental donor is MGI:2385155
  (mouse Btbd3, IMP/IDA from PMID:24179155). Node placement for the *gene
  function* (dendrite morphogenesis) is reasonable; there is no evidence of loss
  or divergence in birds.
- PTN001229949 (source of neurogenesis and cytosol) is a deeper metazoan node
  covering BTBD1, BTBD2, BTBD3 and BTBD6 and invertebrate homologues (fly
  donor FB:FBgn0262871).

### Avian pallium vs mammalian cortex

- Birds lack a layered neocortex:
  [PMID:33574185 "Birds display advanced behaviors, including vocal learning and problem-solving, yet lack a layered neocortex"].
- Cell-type homology hypothesis: the layer 4 input and layer 5 output cell types
  are shared across amniotes but are arranged as nuclei in birds:
  [PMID:23027930 "Our findings establish that the layer 4 input and the layer 5 output cell types are conserved across the amniotes, but are organized into very different architectures, forming nuclei in birds, cortical areas in reptiles, and cortical layers in mammals."]
- The general framing: [PMID:26154980 "The neocortex is found only in mammals"],
  and avian nuclear organisation "could hardly be more dissimilar in appearance"
  from six-layered neocortex.
- The 2005 nomenclature revision recognises pallial homology and
  [PMID:15685220 "the neocortex-like cognitive functions of the avian pallium"]
  but renamed avian regions with pallial, not cortical, names.
- Developmental counter-evidence (chick, gecko, mouse): sensory-circuit neurons
  are generated at different times and places and their transcriptomic
  trajectories diverge early, pointing to convergence:
  [PMID:39946453 "suggesting the convergence of high-order sensory processing across amniote lineages"].
- Songbird vocal-circuit neurons resemble neocortical projection neurons
  transcriptionally but have distinct developmental origins
  [PMID:33574185 "These data suggest that songbird vocal circuits and the mammalian neocortex have distinct developmental origins yet contain transcriptionally similar neurons."]

### Assessment

- What BTBD3 does in mouse is orient dendrites of layer 4 stellate neurons, a
  cell type that might be homologous to the avian L4-like input neurons
  (Dugas-Ford 2012), but the avian homologues sit in nuclei
  (entopallium, field L, nucleus basorostralis), not in a layered
  "outer region". Whether chicken BTBD3 orients dendrites in those nuclei is
  untested.
- "Pallium" is the field-homology level everyone agrees on (dorsal
  telencephalon of all vertebrates); "cerebral cortex" as GO defines it (outer
  layered region) is not an accurate description of most of the avian pallium,
  and the developmental homology of avian pallial sectors to neocortex is
  contested (PMID:23027930 vs PMID:39946453).
- Conclusion: the IBA is not wrong about the *gene* (vertebrate-wide BTBD3
  function in dorsal telencephalic neuron development is a reasonable
  inference) but is mis-scoped about the *anatomy* for a bird. The defensible
  claim for chicken is GO:0021543 pallium development, of which cerebral cortex
  development is a `part_of` child. Action: MODIFY to GO:0021543. The Wei et al.
  flag therefore holds in a weakened form: an anatomy-scope over-specification
  arising from a term with no taxon constraint below Bilateria, not a
  wrong-function misannotation. It is systemic (1759 bird rows, almost all
  TreeGrafter/Ensembl IEA), so it is best raised with GO as an ontology/
  taxon-constraint question rather than fixed gene by gene.
