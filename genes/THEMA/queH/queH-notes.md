# queH review notes (Thermotoga maritima MSB8, Q9WZJ0)

Created as a representative of the QueH route in the bacterial preQ1
incorporation and queuosine maturation module.

## Provenance of this review

- No deep-research provider was available in this environment (no provider API
  keys), so no `-deep-research-<provider>.md` file exists or was fabricated.
  The review was built from the reviewed UniProt record and the cached
  publications below.
- Literature checked, both full text in the cache: PMID:34652139 (the
  structural and biochemical paper on this very protein) and PMID:28128549
  (the comparative-genomics paper that identified the family and renamed
  DUF208 to QueH).

## Function

- QueH is a nonorthologous replacement for QueG, catalysing the same final
  step without cobalamin. [file:THEMA/queH/queH-uniprot.txt "Catalyzes the
  conversion of epoxyqueuosine (oQ) to queuosine (Q), which is a hypermodified
  base found in the wobble positions of tRNA(Asp), tRNA(Asn), tRNA(His) and
  tRNA(Tyr)."]
- This gene complements an E. coli queG deletion. [PMID:34652139 "The queH gene
  (TM0731) of T. maritima was previously shown to complement a ΔqueG strain of
  E. coli by restoring functionally production of Q."]
- Genes from eight distant family members do the same. [PMID:28128549 "All the
  genes duf208 from B. pertussis, D. ethenogenes, H. somnus, S. aureus, S.
  epidermidis, S. pyogenes, T. maritima, and H. pylori allows the restoration
  of the presence of Q into the ΔqueG strain when present on a pBAD24 plasmid."]
- Protein existence level 1. [file:THEMA/queH/queH-uniprot.txt "PE   1:
  Evidence at protein level;"]

## The [4Fe-4S] ligands, and a UniProt defect

The six conserved family cysteines are 9, 10, 87, 90, 169 and 171 in this
192-residue sequence (verified against the record's own sequence; Asp13 is
present as well). The structure assigns them as follows:

- Cluster: [PMID:34652139 "A canonical [4Fe-4S] cluster is coordinated with a
  four cysteine motif: Cys87-X2-Cys90 (α4) and Cys169-X-Cys171 (located in a
  loop between α7, α8) with helix α3 helping to enclose the active site"]
- Separate mononuclear metal: [PMID:34652139 "a single metal ion was found
  coordinated with the two cysteines (Cys9, Cys10) along with Asp13 and a
  non-proteinogenic ligand"]
- The predicted redox-active disulfide is refuted. [PMID:34652139 "The two
  cysteines not coordinating the metal cluster were previously predicted to
  undergo disulfide bond chemistry through a redox cycle, similar to the
  mechanism of vitamin K epoxide reductase."]

HAMAP MF_02089 therefore misassigns both features in this entry: `FT BINDING
9, 10, 87, 90` as cluster ligands, and `FT DISULFID 169..171` as redox-active.
Both are recorded as `UNIPROT` `source_defects` on the `GO:0051539` row, at
`CONFIRMED` confidence since the structure is of this protein.

## Open questions

- No QueH family member has been shown to make queuosine in vitro: the
  purified enzyme consumes the substrate but no product was seen.
  [PMID:34652139 "With added TmQueH, the epoxyqueuosine signal disappears,
  however, a mass corresponding to queuosine was not apparent"]
- The second active-site metal is unassigned: modelled as iron from anomalous
  data, while a prediction server favoured zinc, and the coordinating Asp13 is
  a cysteine in some species. Both are recorded as `knowledge_gaps`.
