# ubiC (PP_5317, Q88C66) - Pseudomonas putida KT2440 - curation notes

## 2026-11-11 audit (ubiquinone_biosynthesis module)

Sources: no Perplexity/Falcon/OpenAI deep research was available (no provider keys in this
environment); an OpenScientist report exists (`ubiC-deep-research-openscientist.md`) and was
read critically. Evidence otherwise comes from the reviewed UniProt entry (HAMAP MF_01632)
and E. coli UbiC literature. No experimental study of the KT2440 protein exists.

- Reaction: UniProt "Reaction=chorismate = 4-hydroxybenzoate + pyruvate" (RHEA:16505,
  EC 4.1.3.40), exactly the GO:0008813 definition.
- E. coli exemplar: [PMID:1644758 "In Escherichia coli, chorismate lyase catalyzes the first
  step in ubiquinone biosynthesis, the conversion of chorismate to 4-hydroxybenzoate."];
  [PMID:8012607 "The enzyme activity did not require metal cofactors."];
  [PMID:8012607 "A feeding experiment with [1,7-13C2]shikimate confirmed the chorismate
  pyruvate-lyase as the sole enzymic source of 4-hydroxybenzoate in vivo."]
- Product retention / hand-off to UbiA: [PMID:11825618 "may involve a mechanism of directed
  delivery to the membrane-bound enzyme that follows CL in the ubiquinone pathway."]
- PAINT: PTHR38683 IBD node PTN002214686 (Gammaproteobacteria, seed E. coli P26602) carries
  GO:0005829, GO:0008813 and GO:0006744. KT2440 has no IBA rows in GOA; the TreeGrafter
  cytosol row (PTN002446048) inherits from that node.
- Location decisions: cytosol ACCEPT (core); UniRule cytoplasm MODIFY to cytosol (correct but
  general, specific term already carried).
- Pyruvate biosynthetic process (UniRule GO_REF:0000104): coproduct, MARK_AS_OVER_ANNOTATED.
- Deep-research caveat: the report treats the KT2440 4HB-biosensor engineering study
  (PMID:30861344) as evidence about PP_5317, but by its own description that study used a
  "heterologously expressed UbiC"; not used as evidence.

Module agreement: matches the `chorismate_lyase_activity` annoton (GO:0008813).
