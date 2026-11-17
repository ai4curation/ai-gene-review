# queH review notes (Acinetobacter baylyi ADP1, Q6FAK7)

Created as a representative of the QueH route in the bacterial preQ1
incorporation and queuosine maturation module. A. baylyi is the exemplar of an
organism that encodes both epoxyqueuosine reductase families.

## Provenance of this review

- No deep-research provider was available in this environment (no provider API
  keys), so no `-deep-research-<provider>.md` file exists or was fabricated.
  The review was built from the reviewed UniProt record and the cached
  publications below.
- Literature checked, both full text in the cache: PMID:28128549 (the
  deletion analysis in this organism, cited by UniProt for this entry's gene
  name and disruption phenotype) and PMID:34652139 (the structural paper on
  the Thermotoga family member, used here for family-level cofactor and
  mechanism context only).

## Function

- QueH catalyses the final oQ-to-Q step without cobalamin.
  [file:ACIAD/queH/queH-uniprot.txt "Catalyzes the conversion of
  epoxyqueuosine (oQ) to queuosine (Q), which is a hypermodified base found in
  the wobble positions of tRNA(Asp), tRNA(Asn), tRNA(His) and tRNA(Tyr)."]
- The two routes are redundant here: only the double mutant loses queuosine.
  [file:ACIAD/queH/queH-uniprot.txt "Queuosine is observed in queG or queH
  single mutants, but queG-queH double mutants accumulate epoxyqueuosine and
  lack queuosine."] [PMID:28128549 "Acinetobacter baylyi ADP1 is one of the few
  organisms that harbor both QueG and DUF208, and deletion of both
  corresponding  genes was required to observe the absence of Q and the
  accumulation of oQ in  tRNA."]
- The authors note the A. baylyi role could in principle be indirect; the
  family-wide complementation of an E. coli queG mutant is what makes the
  direct reading the better one.
- Protein existence level 3. [file:ACIAD/queH/queH-uniprot.txt "PE   3:
  Inferred from homology;"]

## The [4Fe-4S] ligands, and a UniProt defect

This 218-residue sequence has nine cysteines (22, 23, 26, 77, 101, 104, 142,
184, 186), verified against the record's own sequence. Six of them reproduce
the spacing of the structurally characterized Thermotoga protein: 22-23 for
Cys9-Cys10, 101-X2-104 for Cys87-X2-Cys90, and 184-X-186 for
Cys169-X-Cys171. [PMID:34652139 "Sequence analysis shows conservation of the
six cysteine residues among QueH family members; corresponding to four
cysteines coordinating to the [4Fe-4S] cluster, along with two others."]

So the cluster ligands here are Cys101, Cys104, Cys184 and Cys186, while
Cys22 and Cys23 belong to the separate mononuclear metal site. Cys26 sits
where Thermotoga has Asp13, which the paper says is expected in some species.
[PMID:34652139 "Sequence alignment shows that Asp13 is commonly replaced in
some bacteria species by a cysteine residue, suggesting possible alternative
bonding modes and/or coordinating metals."]

HAMAP MF_02089 therefore misassigns both features in this entry: `FT BINDING
22, 23, 101, 104` as cluster ligands, and `FT DISULFID 184..186` as
redox-active. Both are recorded as `UNIPROT` `source_defects` on the
`GO:0051539` row, at `PROBABLE` confidence because no structure of this protein
exists and the assignment rests on the family alignment.

## Open questions

- Why keep both QueG and QueH when either alone suffices? Differing oxygen
  sensitivity or cobalamin availability is the obvious hypothesis, and is
  recorded in `suggested_experiments`.
