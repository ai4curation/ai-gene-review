# PGL-1 PAINT lineage and catalytic-scope check (2026-09-20)

The actual PTHR47958 treeinfo POST response places Q9TZQ3 / WBGene00003992 / pgl-1
at leaf PTN002773363. `pgl-1-paint-lineage.json` preserves the full extracted path,
original IBD/IBA lines, nearby accession-mapped leaves, raw-response byte count
(33300148) and SHA-256 (6ad49ddf2142613056a69f66e28863b9f401b48efe6961569674ef8cbd06cfff).

The target descends from PTN002776867 (mRNA binding), PTN002774595 (RNA helicase),
and PTN002776405 (spliceosomal splicing and mRNA export). The helicase IRD losses
at PTN002774495 and PTN002773962 are outside its actual lineage. Nearby leaves include
C. elegans HEL-1/DDX39B Q18212 and Drosophila Hel25E Q27268. This is a real positive
ancestry, not an off-clade target or a missing-source failure.

The biological conflict is the experimentally characterized PGL scaffold and novel
alpha-helical RNase dimerization domain (PMID:26787882) versus placement among
DDX39-like helicases. The solved domain is part of the protein, so its structure
alone does not experimentally disprove every possible helicase mechanism. A neutral
focused adjudication is gated by the parent review. Splicing/export must be judged
independently of helicase catalysis; cytoplasmic/perinuclear localization does not
exclude a process contribution.

QuickGO definitions/children were retrieved on 2026-09-20 and stored in
`pgl-1-go-term-check.json`. GO:0046589 ribonuclease T1 activity is a lyase and RNA
endonuclease term; hydrolase is not entailed by this ancestry. However, the actual
UniProt record explicitly assigns a reaction consuming H2O and producing a
3′-phosphate RNA fragment. This supports the broad hydrolytic property independently
of GO ancestry and is compatible with a cyclizing intermediate and lyase EC class.
The primary PGL study establishes G-specific cleavage and leaves its novel catalytic
mechanism unresolved; lack of a separate product-mechanism assay is not a basis to
reject the broader curated reaction assignment.

GO:0043066 ancestors were separately retrieved into
`pgl-1-apoptosis-term-ancestors.json`; none duplicates a parent or child in the
existing PGL-1 process rows. The retained authored apoptosis proposal is supported
by PGL-dependent CED-4 protein regulation and gain/loss experiments, without an
asserted direct RNA target or SIR-2.1 sequestration mechanism.
