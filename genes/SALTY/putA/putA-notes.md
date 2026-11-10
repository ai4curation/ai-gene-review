# putA (Salmonella typhimurium LT2, UniProtKB P10503) - curation notes

## Provenance of this research

Provider deep research (perplexity/openai/falcon etc.) was unavailable in this
environment (no provider API keys), so no `putA-deep-research-*.md` file exists.
These notes were compiled manually from the cached PubMed records in
`publications/` (all Salmonella primary papers are abstract-only in the cache;
PMC full text for PMID:1987118, PMID:8483946 and PMID:9098084 could not be
retrieved, HTTP 403 / publisher restriction), the UniProt record
(`putA-uniprot.txt`) and the family-level review PMID:28712849 (full text).

Literature checked: PMID:6270100, PMID:1987118, PMID:8483946, PMID:7730362,
PMID:9098084, PMID:2851701, PMID:8479928, PMID:28712849.

## Gene product

- 1320-aa trifunctional (class 1C) PutA. N-terminal RHH DNA-binding region
  (UniProt REGION 1..52 by similarity to E. coli P09546), proline dehydrogenase
  region 228..574, aldehyde dehydrogenase (GSALDH) region 653..1119.
  No transmembrane segment in the UniProt features; membrane association is peripheral.
- UniProt: [file:SALTY/putA/putA-uniprot.txt "Oxidizes proline to glutamate for use as a carbon and nitrogen source (PubMed:6270100). Also functions as a transcriptional repressor of the put operon (PubMed:1987118)."]

## Enzymology (Menzel & Roth 1981)

- [PMID:6270100 "catalyze both the proline oxidase and the pyrroline-5-carboxylic acid dehydrogenase activities necessary for the oxidation of proline to glutamic acid"]
- Purification starts from membranes: [PMID:6270100 "The purification involves the preparation of a crude membrane pellet, detergent solubilization"]
- [PMID:6270100 "The purified protein is a dimer composed of identical 132,000-dalton subunits."]
- Genetic link: [PMID:6270100 "Analysis of mutants defective for proline utilization demonstrate that the bifunctional enzyme is the putA gene product."]
- Family review: the S. typhimurium PRODH was kinetically characterised [PMID:28712849 "Early kinetic analysis of the class 1C PutA from Salmonella typhimurium suggested a ping-pong mechanism for the PRODH activity"].

## Autoregulation (Maloy lab)

- Divergent operon: [PMID:2851701 "Extensive genetic evidence suggests that transcription of the put operon is autoregulated by the putA gene product, a membrane-associated dehydrogenase."]
- Operator candidate: [PMID:2851701 "A 27 bp palindrome located between the two promoters may be the operator for autoregulation by the PutA protein."]
- Direct DNA binding: [PMID:1987118 "Purified PutA protein bound specifically to several nonoverlapping fragments of control region DNA"]; deletions of operator sites [PMID:1987118 "increased expression of the put genes but were still induced by proline, indicating that multiple cis elements are involved in repression"].
- Redox switch: [PMID:8483946 "The proline utilization (put) operon of Salmonella typhimurium is transcriptionally repressed by PutA protein in the absence of proline."]; [PMID:8483946 "Catabolism of proline requires PutA to associate with the membrane because reoxidation of the FAD cofactor in PutA needs the presence of an electron acceptor."]; [PMID:8483946 "Repression of the put operon requires PutA to bind to the put control-region DNA in the cytoplasm."]
- PRODH activity needed for induction: [PMID:7730362 "the results indicate that the proline dehydrogenase activity of PutA is essential for induction of the put operon by proline"]; single proline site [PMID:7730362 "a single proline-binding site is involved in both proline dehydrogenase activity and induction of the expression of the put operon"].
- Mutually exclusive membrane vs DNA binding: [PMID:9098084 "The results indicate that wild-type PutA does not simultaneously associate with DNA and membranes."]; shuttling model [PMID:9098084 "the PutA protein shuttles between the membrane (where it acts as an enzyme but lacks access to DNA-binding sites) and the cytoplasm (where it binds DNA and acts as a transcriptional repressor)"].

## Curation judgements

- L-proline biosynthetic process (GO:0055129, InterPro IPR005933 mapping): REMOVE,
  directionally wrong; PutA oxidises proline to glutamate (as in the P. putida review).
- L-glutamate biosynthetic process (GO:0097054, IDA PMID:6270100): glutamate is
  literally formed, but the term sits under amino acid biosynthesis (anabolic
  glutamate pathways: GDH/GOGAT, MetaCyc GLUTSYN-PWY etc.). It looks like a
  decomposition of the obsoleted precomposed GO:0010133 "L-proline catabolic
  process to L-glutamate", whose replaced_by is GO:0006562. Marked as
  over-annotated by the first pass; harmonized to KEEP_AS_NON_CORE by the
  module curator to match the E. coli PutA and yeast PUT2 reviews. The product-side context is better carried by GO:0006562 plus
  GO:0003842 or a GO-CAM.
- Membrane location: plasma membrane / cytoplasmic side of membrane rows MODIFY to
  GO:0009898 cytoplasmic side of plasma membrane (peripheral, no TM segment,
  quinone-dependent FAD reoxidation at the inner membrane).
- Not added: cytosol (the DNA-bound repressor state is cytoplasmic per PMID:8483946);
  left as a possible NEW for a later pass.
