# pvdA (Q51548, PA2386) — Pseudomonas aeruginosa PAO1

Curation notes for the review added alongside the
`modules/pseudomonas_pyoverdine_precursor_supply.yaml` module work. PAO1 PvdA was
added as the experimentally best-characterized exemplar of the module's ornithine
hydroxylation step; the KT2440 ortholog (Q88GC8, `genes/PSEPK/pvdA`) was already
reviewed, but its evidence is largely orthology-based.

## What is established

- **Reaction.** L-ornithine + NADPH + O2 = N5-hydroxy-L-ornithine + NADP+ + H2O
  (RHEA:41508, EC 1.14.13.195), curated in UniProt from PMID:17015659 and
  PMID:17900176. Purified enzyme assayed both by NADPH oxidation and by direct
  Csaky-type hydroxylation assay
  [PMID:17900176 "PvdA is dependent on FAD for activity and FMN is not an effective coenzyme."].
- **Cofactors.** Strictly FAD and NADPH; FMN and NADH do not substitute
  [PMID:17015659 "The enzyme is specific for NADPH and flavin adenine dinucleotide (FAD(+)) as cofactors, as it cannot utilize NADH and flavin mononucleotide."].
  One FAD per subunit, bound weakly (Kd in the micromolar range), with
  FAD-binding residues curated from the crystal structures
  [PMID:21757711 "PvdA has the two expected Rossmann-like dinucleotide-binding domains for FAD and NADPH and also a substrate-binding domain"].
- **Specificity.** Shortening or lengthening the side chain abolishes
  hydroxylation; L-lysine supports NADPH oxidation but yields no hydroxylated
  product, i.e. it is a non-substrate effector that uncouples the reaction
  [PMID:17900176 "By extending the side chain by one methylene group (L-lysine), NADPH oxidation occurred at 80 % of the rate of L-ornithine; however, no hydroxylated product was formed."].
  D-ornithine, 5-aminopentanoate, 1,4-diaminobutane and L-norleucine are inactive.
  This is the fact that makes the PANTHER family unusable as a grounding for the
  ornithine-specific term (see below).
- **Pathway role.** pvdA disruption gives a pyoverdine-negative strain that is
  rescued genetically and by feeding the hydroxylated precursor
  [PMID:8106324 "the pvdA mutant obtained by gene disruption also disclosed no pyoverdin synthesis, lacked L-Orn N5-oxygenase activity, was complemented by the cloned pvdA gene, and produced pyoverdin at wild-type levels when fed with the biosynthetic precursor L-N5-OH-Orn"].
  The rescue is what places PvdA upstream of NRPS assembly rather than inside it.
- **Location.** Topology analysis concluded a peripheral inner-membrane protein
  with the bulk of the chain in the cytosol and no transmembrane segment
  [PMID:18757814 "Cell fractionation and proteinase K accessibility experiments in P. aeruginosa confirmed the membrane-bound nature of PvdA, but excluded the transmembrane topology of its N-terminal hydrophobic region"];
  fluorescent fusions put PvdA among the cytoplasmic pathway enzymes while
  recovering a substantial membrane fraction and old-pole clustering
  [PMID:22498339 "fluorescent fusions with PvdA, one of the initial enzymes in the biosynthetic pathway of PVDI in the cytoplasm"].
  The review therefore accepts cytoplasm as the core location and keeps plasma
  membrane as a supported non-core row rather than choosing between them.

## Review decisions worth recording

- `GO:0006879 intracellular iron ion homeostasis` (IBA from PAINT node
  PTN001009003) → **MODIFY** to `GO:0002049`. The node placement is sound: the
  seeds are fungal siderophore ornithine monooxygenases and every descendant
  initiates hydroxamate siderophore synthesis. The objection is granularity and
  role — the term names the downstream outcome of siderophore-mediated uptake,
  not the hydroxylation, and the gene already carries the direct process term
  from experiment. Recorded as `propagation_review` with
  `root_cause: TERM_SCOPING_PROBLEM`, not as a propagation failure.
- `GO:0002049` IDA from PMID:20650894 was **ACCEPTed** even though that paper's
  title and abstract foreground the *Aspergillus fumigatus* enzyme SidA. The
  abstract states the substrate-activation effect was also observed with
  bacterial PvdA, the full text is not cached, and the pathway assignment is
  independently established — so there is no basis for a wrong-gene claim.
- `GO:0050660 flavin adenine dinucleotide binding` added as **NEW**: directly
  supported by the structures and the curated cofactor statement, and absent
  from GOA for this entry.

## Family grounding

UniProt cross-references put Q51548 in `PANTHER:PTHR42802` and its only
subfamily `PTHR42802:SF1`. That family also contains lysine N6-monooxygenases
(E. coli IucD P11295, M. tuberculosis MbtG) and putrescine N-hydroxylases
(Bordetella AlcA, Shewanella PubA, Streptococcus FbsI). Since the purified
enzymes are mutually substrate-specific, family (or subfamily) membership cannot
establish ornithine specificity, so `interpro/panther/PTHR42802/PTHR42802-review.yaml`
scopes `GO:0031172` as UNRESOLVED and the module asserts no PANTHER id on that
annoton, grounding the role on representative members instead. The family *is*
coherent for flavin-dependent omega-amino N-hydroxylation and for the
iron-homeostasis process, which is scoped FAMILY_WIDE there.

## Provider deep research

`just deep-research-perplexity PSEAE pvdA` is not available in this environment
(`Provider 'perplexity' not available. Available: falcon, openscientist`), and
`falcon` fails authentication here (`Exception: Failed to authenticate`). No
`-deep-research-*.md` file was fabricated. The review is built from the cached
publications in `publications/` (one with full text, PMID:17900176) and the
curated UniProt record; where only an abstract was available this is recorded in
`full_text_unavailable` and in each `reference_review`.
