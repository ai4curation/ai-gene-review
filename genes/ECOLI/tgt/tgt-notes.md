# tgt review notes (E. coli K-12, P0A847)

Created for the bacterial preQ1 incorporation and queuosine maturation module,
which needed reviewed exemplars outside *Pseudomonas*.

## Provenance of this review

- No deep-research provider was available in this environment (no provider API
  keys), so no `-deep-research-<provider>.md` file exists or was fabricated.
  The review was built from the reviewed UniProt record and the cached
  publications below.
- Literature checked, all abstract-only in the cache except the proteome paper:
  PMID:8323579 (purification and base exchange, the IDA activity row),
  PMID:7893665 (zinc content and ligands, the IDA zinc row), PMID:6804468 (the
  tgt mutant lacking queuosine, both IMP rows), PMID:18304323 (cytosol
  proteome, full text cached; Tgt is not named in the parsed text).

## Function

- Tgt exchanges guanine 34 for preQ1 in GUN-anticodon tRNAs through a
  double-displacement mechanism. [file:ECOLI/tgt/tgt-uniprot.txt "Catalyzes the
  base-exchange of a guanine (G) residue with the queuine precursor
  7-aminomethyl-7-deazaguanine (PreQ1) at position 34 (anticodon wobble
  position) in tRNAs with GU(N) anticodons"]
- The purified enzyme performs that exchange. [PMID:8323579 "TGT-catalyzed base
  exchange of guanosine-34 with preQ1 (7-aminomethyl-7-deazaguanine)"]
- One structural zinc per subunit, needed for oligomerization and tRNA
  binding. [PMID:7893665 "wild-type TGT contains ca. 0.8 mol of zinc/mol of
  subunit, determined by atomic emission spectrometry"] [PMID:7893665
  "cysteines 302, 304, and 307 and histidine 317 are the ligands to the zinc"]
  Current UniProt maps the fourth ligand to residue 333 instead, from
  structure; the cofactor claim is unaffected either way.
- Loss of Tgt abolishes queuosine without a growth defect, but costs viability
  under unfavourable conditions. [PMID:6804468 "indicating that the enzyme is
  actually involved in the biosynthesis of queuosine in tRNA"] [PMID:6804468
  "marked reduction of viability when the cells are kept under unsuitable
  conditions for growth"]

## Curation decisions

- `GO:0008479` is retained although its definition (RHEA:16633) describes
  free-queuine insertion, which is the eukaryotic QTRT1/QTRT2 reaction. GOC
  applies the term to bacterial preQ1-inserting Tgt through InterPro2GO
  (IPR004803) and UniRule, and no preQ1-specific term exists, so the
  established mapping is kept and a dedicated bacterial term is proposed in
  `proposed_new_terms`. Same call as the P. putida ortholog.
- `GO:0006400` was refined to `GO:0002099`, and `GO:0005737` to `GO:0005829`;
  both refinements point at terms this protein already carries.
- The zinc row is `KEEP_AS_NON_CORE`: as precise as warranted, but a structural
  cofactor rather than the catalytic function.
- Tgt seeds the bacterial PTHR46499 PAINT nodes, so it is also the reference
  protein of `interpro/panther/PTHR46499/PTHR46499-review.yaml`. That family is
  heterogeneous: SF1 also holds archaeal tRNA-guanine(15) transglycosylases and
  SF2 holds archaeosine synthases, so the family review scopes `GO:0008479` to
  the bacterial Tgt members.
