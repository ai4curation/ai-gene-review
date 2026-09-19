# sdhE (Q88MZ4, PP_1424) — Pseudomonas putida KT2440

FAD assembly factor SdhE. 84 aa, Swiss-Prot reviewed (`SDHE_PSEPK`).

## Summary

SdhE is a small, soluble cytoplasmic chaperone that binds FAD and delivers/licenses its
covalent attachment to the SdhA flavoprotein subunit of respiratory complex II. It is an
assembly factor, not a stoichiometric SdhABCD subunit, and it has no catalytic activity on
succinate itself. Loss of SdhE therefore abolishes succinate oxidation indirectly, by leaving
SdhA unflavinylated.

## What the P. putida record itself asserts

The PSEPK entry carries no primary experimental evidence for this protein. Both the function
and the localization are by-similarity transfers from the same source ortholog,
`UniProtKB:G4V4G2`:

- `CC -!- FUNCTION: An FAD assembly protein, which accelerates covalent attachment of the
  cofactor into other proteins. ... Required for flavinylation (covalent attachment of FAD) of
  the flavoprotein subunit SdhA of SDH and other flavinylated proteins as well.
  {ECO:0000250|UniProtKB:G4V4G2}` [file:PSEPK/sdhE/sdhE-uniprot.txt]
- `CC -!- SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250|UniProtKB:G4V4G2}`
  [file:PSEPK/sdhE/sdhE-uniprot.txt]
- `KW Chaperone; Cytoplasm; Reference proteome.` [file:PSEPK/sdhE/sdhE-uniprot.txt]

Family assignment is unambiguous: `PANTHER; PTHR39585; FAD ASSEMBLY FACTOR SDHE`,
`Pfam; PF03937; Sdh5`, `InterPro; IPR050531; SdhE_FAD_assembly_factor`
[file:PSEPK/sdhE/sdhE-uniprot.txt]. Pfam `Sdh5` is the same domain family as the eukaryotic
SDHAF2/Sdh5 assembly factor, which is why this review's core function mirrors the repo's
`genes/human/SDHAF2` treatment (`GO:0044183` protein folding chaperone + `GO:0018293`
protein-FAD linkage).

## Primary literature

The characterised bacterial ortholog is Serratia/E. coli SdhE
[PMID:22474332 "SdhE is a conserved protein required for flavinylation of succinate
dehydrogenase in bacteria"]. Full text is cached. Key points:

- Direct FAD binding, SdhA interaction and flavinylation dependence, all in one experiment
  series: [PMID:22474332 "SdhE interacted with the flavoprotein SdhA, directly bound the
  flavin adenine dinucleotide co-factor, and was required for the flavinylation of SdhA."]
- The phenotype is loss of *function*, not loss of *assembly* — which is what makes SdhE a
  cofactor-maturation factor rather than an assembly chaperone in the structural sense:
  [PMID:22474332 "SdhE was required for growth on succinate as a sole carbon source and for
  the function, but not stability, of succinate dehydrogenase"]. The discussion is explicit
  that this differs from yeast, where `sdh5` mutants destabilise SDH: [PMID:22474332 "The
  absence of FAD, however, did not prevent correct assembly of SDH."]
- This overturned the prior autocatalytic-flavinylation model: [PMID:22474332 "Our results
  contradict this autocatalytic flavinylation model and show that SdhE proteins are required
  for the incorporation of FAD into SdhA."]
- Soluble monomer, consistent with the cytoplasm annotations: [PMID:22474332 "The bacterial
  SdhE is a soluble monomer that interacted weakly and/or transiently with SdhA."]
- The UniProt phrase "and other flavinylated proteins as well" traces to the pleiotropy of the
  deletion, and the authors state it as a hypothesis rather than a demonstrated fact:
  [PMID:22474332 "SdhE might have co-factor chaperone-like functions to assist FAD
  incorporation into other flavoproteins."] It is *not* established for P. putida.

Flavinylation is not absolutely required for SdhA to acquire FAD — the PSEPK sdhA record notes
residual autocatalytic loading: `Note=Flavinylated by SdhE, about 5% flavinylation occurs in
the absence of SdhE.` [file:PSEPK/sdhA/sdhA-uniprot.txt]

## Annotation decisions

Three GOA rows [file:PSEPK/sdhE/sdhE-goa.tsv]:

| term | evidence | ref | action |
|---|---|---|---|
| `GO:0005737` cytoplasm | IEA | `GO_REF:0000044` | ACCEPT |
| `GO:0006105` succinate metabolic process | IEA | `GO_REF:0000118` (PANTHER:PTN002446823) | KEEP_AS_NON_CORE |
| `GO:0005737` cytoplasm | ISS | `GO_REF:0000024` (UniProtKB:G4V4G2) | ACCEPT |

Notes on two of these:

- **The two cytoplasm rows are not independent.** `GO_REF:0000044` maps the UniProt
  SUBCELLULAR LOCATION line, and that line is itself `ECO:0000250|UniProtKB:G4V4G2` — the same
  transfer that produced the ISS row. So the IEA adds no separate support. It is still
  *correct*, which is why it is ACCEPTed rather than REMOVEd; per the schema, `REMOVE` is for
  annotations unlikely to be correct, and redundancy between two GOA rows asserting the same
  true localization is a GOA housekeeping matter.
- **`GO:0006105` is downstream, not direct.** SdhE does not act on succinate; it acts on SdhA.
  Succinate metabolism fails in its absence because SdhA is left unflavinylated. This is
  exactly the necessity-vs-participation distinction in CLAUDE.md, so the term is retained as
  true-but-non-core and the core function records the step SdhE actually performs
  (`GO:0018293` protein-FAD linkage) rather than the pathway it enables.

## Open questions

- Has P. putida SdhE been shown to flavinylate any substrate other than SdhA? The UniProt
  "other flavinylated proteins" clause is a by-similarity transfer of a hypothesis, not a
  result.
- How large is the residual SdhE-independent SdhA flavinylation in KT2440, and is it enough to
  support any growth on succinate?
