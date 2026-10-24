# pvdH (Q9I168, PA2413) — Pseudomonas aeruginosa PAO1

Curation notes for the review added alongside the
`modules/pseudomonas_pyoverdine_precursor_supply.yaml` module work. PAO1 PvdH is
the exemplar whose enzymology and mutant phenotype ground the module's
L-2,4-diaminobutyrate step; the KT2440 ortholog (Q88F75, `genes/PSEPK/pvdH`) was
already reviewed from orthology plus this same paper.

## What is established

- **Reaction.** Interconversion of L-aspartate beta-semialdehyde and
  L-2,4-diaminobutyrate by a PLP-dependent transamination, on protein
  hyperexpressed and purified from PAO1
  [PMID:15317763 "PvdH was found to catalyze an aminotransferase reaction, interconverting aspartate beta-semialdehyde and l-2,4-diaminobutyrate."].
  Highest specificity for alpha-ketoglutarate, 41-fold lower for pyruvate,
  negligible for other keto acids, with a ping-pong mechanism
  [PMID:15317763 "Steady-state kinetic analysis with a novel coupled assay established that the enzyme adopts a ping-pong kinetic mechanism and has the highest specificity for alpha-ketoglutarate."]
  — i.e. EC 2.6.1.76, `GO:0045303`.
- **Pathway role.** The pyoverdine chromophore is a condensation product of
  D-tyrosine and L-2,4-diaminobutyrate, and both pvdH and asd mutants are
  pyoverdine-negative unless the diamino acid is supplied
  [PMID:15317763 "Both pvdH and asd (encoding aspartate beta-semialdehyde dehydrogenase) knockout mutants of Pseudomonas aeruginosa PAO1 were unable to synthesize pyoverdine under iron-limiting conditions in the absence of l-2,4-diaminobutyrate in the culture media."].
  Independent mutant-phenotype support comes from the PAO1 pyoverdine gene
  screen [PMID:12686626 "The candidate genes were mutated and the effects of the mutations on pyoverdine production were determined. Eight new pvd genes were identified."].
- **Conservation.** PvdH homologues sit inside the pyoverdine loci of other
  pseudomonads [PMID:15317763 "These homologues were found in the DNA loci of the corresponding genomes that contain other pyoverdine synthesis genes."],
  which is what makes the module's genus-level scope defensible while keeping the
  exemplars to PAO1 and KT2440.
- **Classification.** Class-III PLP-dependent aminotransferase: Pfam
  Aminotran_3, PROSITE AA_TRANSFER_CLASS_3, InterPro IPR004637 (Dat), NCBIfam
  TIGR00709 (dat), PIRSF Transaminase_4ab_Lys_Orn. The entry is unreviewed
  (TrEMBL) and `PE 3: Inferred from homology`, so its free-text cofactor note
  carries only ARBA evidence and is not cited as support; the curated domain
  signatures are.

## Review decisions worth recording

- All three `GO:0008483 transaminase activity` rows (IBA, IDA, IEA) →
  **MODIFY** to `GO:0045303`. Same term, same claim, consistent actions: the
  broad parent is true but the assayed reaction is the specific child. Added
  `GO:0045303` as a **NEW** row since GOA carries only the parent here, although
  the KT2440 ortholog already has the specific term.
- The IBA's `WITH/FROM` contains `UniProtKB:Q9I168` itself, i.e. the gene appears
  among the seeds of the PAINT node it later receives. Per the repo's IBA policy
  this is expected and is a marker that experimental grounding exists on the
  target — explicitly *not* `CIRCULAR_OR_REDUNDANT`. Recorded in
  `propagation_review` with `root_cause: TERM_SCOPING_PROBLEM` and
  `source_status: SUPPORTS_TRANSFER`.
- `GO:0030170 pyridoxal phosphate binding` kept as **KEEP_AS_NON_CORE**:
  genuinely supported by the class-III signatures and consistent with the
  ping-pong mechanism, but a cofactor property rather than the catalytic role.
  This matches the KT2440 review's treatment of the same term.

## Family grounding

`PANTHER:PTHR43552` is a clean family-level grounding, unlike the PvdA case: both
of its subfamilies (SF1 Dat/PvdH/RhbA, SF2 EctB) perform the same EC 2.6.1.76
transamination and differ only in which pathway consumes the product, so
`interpro/panther/PTHR43552/PTHR43552-review.yaml` scopes `GO:0045303` as
FAMILY_WIDE and the module uses the family id on this annoton. What family
membership does *not* say is that a member serves pyoverdine — that comes from
the pyoverdine locus context.

## Provider deep research

`just deep-research-perplexity PSEAE pvdH` is unavailable in this environment
(`Provider 'perplexity' not available. Available: falcon, openscientist`), the
`falcon` provider fails authentication here, and an `openscientist` run started
for the sibling gene pvdA produced no output before hitting a 15-minute limit,
so no provider route was usable. No `-deep-research-*.md` file was fabricated. The review rests on the cached publications (both abstract-only, as
recorded in `full_text_unavailable`) and on the curated domain/family
cross-references in the UniProt record.
