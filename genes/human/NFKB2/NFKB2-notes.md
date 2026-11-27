# NFKB2 review notes

## PTHR24169 context

NFKB2 is the p100/p52 member of the reviewed human PANTHER family `PTHR24169`.
The same family also contains NFKB1, REL, RELA and RELB; RELA was already
complete on `main`, while NFKB1, NFKB2, REL and RELB are reviewed together here.

## Evidence synthesis

NFKB2 encodes the p100 precursor and the processed p52 NF-kappaB subunit. p100
uses an ankyrin-repeat C terminus as an IkappaB-like inhibitor, and noncanonical
NIK/IKKalpha signaling phosphorylates p100 for proteasomal processing to p52.
Reactome's noncanonical NF-kappaB events capture p100:RELB binding in the
cytosol, the NIK/IKKalpha phosphorylation reactions, and the resulting p52:RELB
translocation into the nucleus [Reactome:R-HSA-5607720;
Reactome:R-HSA-5607726; Reactome:R-HSA-5607741].

Early experimental rows describe NFKB2 as `lyt-10`/p100/p49 and H2TF1, including
MHC class I kappaB enhancer binding [PMID:8360178, "binds the MHC kappa B
site"] and the p49 product acting with p65 on the HIV enhancer [PMID:1876189,
"A 49K product (p49) can be generated"]. More recent rows place p100 processing
in noncanonical B-cell signaling, including NIK-dependent p100 processing and
SUMO1 modification of p100 [PMID:11239468; PMID:18617892].

The direct p52 DNA-binding and p52:RELB nuclear rows are core. BCL3-p52, p52-p65
and menin-interaction rows were kept as real partner contexts, and bare
`GO:0005515` rows were removed under the project protein-binding policy without
disputing the reported interactions.

## Automated research

`just deep-research human NFKB2 --provider perplexity` was not rerun after the
NFKB1 provider check failed with only `claude_code` available. No
`NFKB2-deep-research-perplexity.md` artifact was created or filled manually.
