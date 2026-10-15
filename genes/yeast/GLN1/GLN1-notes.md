# GLN1 (YPR035W, P32288) notes

Evidence journal (no paid deep research run; built from UniProt and cached publications).

- Glutamine synthetase, EC 6.3.1.2 (glutamate--ammonia ligase), homooctamer (UniProt; older estimate 10-12 subunits), glutamine synthetase family (type II, eukaryotic) [UniProt:P32288].
- Purified enzyme: "We have purified glutamine synthetase over 130-fold from Saccharomyces cerevisiae. The enzyme exhibits a Km for glutamate of 6.3 mM and a Km for ATP of 1.3 mM in the biosynthetic reaction" [PMID:6129248]. Earlier biochemical study of baker's yeast GS [PMID:4156034, title only in cache].
- Gene: "The GLN1 gene, encoding glutamine synthetase in Saccharomyces cerevisiae, was sequenced"; transcription increased on glutamate vs glutamine via a nitrogen UAS, and by purine starvation [PMID:1347768].
- Location: cytoplasm (GFP, Huh 2003; UniProt). Under MMS stress a subset of Gln1 foci are nuclear and co-localise with Cmr1 in INQ: "MMS-induced Hsp104, Mkt1, Ylr126C and Gln1 foci have been annotated as cytosolic in the previous study13, although we find that a subset of these foci are in fact nuclear and co-localize with Cmr1" [PMID:25817432].
- Partners in nitrogen assimilation: GS + GOGAT (GLT1) form an ammonia-assimilating cycle; in yeast this route is ancillary to GDH1 for glutamate [PMID:9287019, PMID:9657994].

## Curation decisions
- Core MF GO:0004356; BP GO:1901704; CC cytosol.
- L-glutamate biosynthetic process (RCA, superpathway PWY3O-13): MARK_AS_OVER_ANNOTATED; GS consumes glutamate and makes glutamine; glutamate is made by GLT1 in the GS/GOGAT route.
- Nucleus HDA / nuclear periphery IDA: KEEP_AS_NON_CORE (stress-induced foci).
