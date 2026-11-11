# queG review notes (E. coli K-12, P39288)

Created for the bacterial preQ1 incorporation and queuosine maturation module,
which needed reviewed exemplars outside *Pseudomonas*.

## Provenance of this review

- No deep-research provider was available in this environment (no provider API
  keys), so no `-deep-research-<provider>.md` file exists or was fabricated.
  The review was built from the reviewed UniProt record and the cached
  publication below.
- Literature checked: PMID:21502530 (abstract only in the cache), the paper
  behind both experimental rows and cited by UniProt for the disruption
  phenotype.

## Function

- QueG performs the final step, reducing and deoxygenating epoxyqueuosine at
  position 34 to queuosine. [file:ECOLI/queG/queG-uniprot.txt "Catalyzes the
  conversion of epoxyqueuosine (oQ) to queuosine (Q)"]
- It was found by screening the single-gene knockout collection, and is related
  to the B12-dependent iron-sulfur proteins of halorespiration. [PMID:21502530
  "we have screened 1,755 single gene knockouts of Escherichia coli and have
  identified the key final step in the biosynthesis of Q"] [PMID:21502530 "The
  protein is homologous to B(12)-dependent iron-sulfur proteins involved in
  halorespiration."]
- Cofactors: cob(II)alamin and two [4Fe-4S] clusters per monomer.
  [file:ECOLI/queG/queG-uniprot.txt "Binds 2 [4Fe-4S] clusters per monomer."]
  [file:ECOLI/queG/queG-uniprot.txt "Name=cob(II)alamin"]
- The knockout accumulates the substrate. [file:ECOLI/queG/queG-uniprot.txt
  "RNA from mutants accumulates epoxyqueuosine and lacks queuosine."]
- Note that the in vitro assay in PMID:21502530 used the *B. subtilis* enzyme
  (P97030); the E. coli evidence is genetic. Both proteins seed the PTHR30002
  PAINT node for `GO:0052693`.

## Curation decisions

- `GO:0031419` cobalamin binding is added as `NEW` (IC): HAMAP assigns the
  cofactor and exogenous cobalamin stimulates the characterized ortholog, but
  GOA has no metal/cofactor row for it. Same call as the P. putida ortholog.
- `GO:0051536` was refined to `GO:0051539`, since the record specifies
  [4Fe-4S] clusters and maps their ligands.
- `GO:0016491`, `GO:0006400` and `GO:0008033` were all refined to the specific
  terms the protein already carries (`GO:0052693`, `GO:0008616`).
- Cytoplasm is kept rather than refined: unlike the other three enzymes here,
  this entry has no experimental cytosol row, and the entry is protein
  existence level 3 (inferred from homology).
- QueG seeds the PTHR30002 PAINT node, so it is also the reference protein of
  `interpro/panther/PTHR30002/PTHR30002-review.yaml`.
