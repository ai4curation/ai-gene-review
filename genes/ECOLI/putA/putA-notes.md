# putA (Escherichia coli K-12, UniProtKB P09546) review notes

## Provenance of this review

- Provider deep research (`just deep-research`) was **not available** in this
  environment (no provider API keys). No `*-deep-research-*.md` file exists for
  this gene. These notes were compiled manually from the cached publications
  (`publications/PMID_*.md`, fetched with `just fetch-gene-pmids ECOLI putA`),
  the UniProt record (`putA-uniprot.txt`) and the PutA family review
  PMID:28712849 (full text cached).
- Literature checked: all ten PMIDs cited in GOA (1618807, 6321477, 11294639,
  12009917, 12514740, 15155740, 18586269, 19140736, 22040654, 25384482) plus
  PMID:28712849. Only PMID:22040654, PMID:19140736 and PMID:28712849 have full
  text in the cache; the rest are abstract-only.

## Domain architecture and overview

- 1320-residue trifunctional protein: N-terminal ribbon-helix-helix (RHH)
  DNA-binding domain, FAD-dependent proline dehydrogenase (PRODH) beta/alpha
  barrel, C-terminal NAD+-dependent P5C / L-glutamate gamma-semialdehyde
  dehydrogenase (GSALDH, ALDH superfamily) [PMID:22040654 "The E. coli PutA polypeptide has 1320 residues with the DNA-binding, PRODH and P5CDH domains localized at residues 1-52, 261-612, and 650-1130, respectively"].
- Oxidizes proline to glutamate in two steps [PMID:22040654 "performs the oxidation of proline to glutamate in two catalytic steps using separate proline dehydrogenase (PRODH) and Δ(1)-pyrroline-5-carboxylate (P5C) dehydrogenase domains"].
- UniProt: "Oxidizes proline to glutamate for use as a carbon and nitrogen source"; "Also functions as a transcriptional repressor of the put operon" (CC FUNCTION, ECO:0000269).

## PRODH activity and electron acceptor

- Purified PutA has both activities [PMID:1618807 "We showed copurification of proline and delta 1-pyrroline-5-carboxylate dehydrogenase activities"].
- Membrane reconstitution: soluble vs membrane forms [PMID:6321477 "Soluble and membrane associated proline dehydrogenase differ in catalytic properties"; "The membrane-associated enzyme transfers electrons from L-proline to O2 via the respiratory chain, with coupled transmembrane proton translocation"].
- Ubiquinone is the physiological acceptor [PMID:22040654 "the oxidation of proline is coupled to the reduction of ubiquinone (CoQ) by the PRODH domain"; "rapid equilibrium ping-pong mechanism with proline and ubiquinone binding at two distinct sites"].
- PutA669 (residues 1-669) has PRODH but no P5CDH activity [PMID:12009917 "PutA(669) purifies as a dimer and has a PDH specific activity that is 4-fold higher than that of PutA"; "PutA(669) lacks P5CDH activity"].
- Tyr540 mutants change proline/hydroxyproline specificity [PMID:19140736 "Mutation of Tyr540 increases the catalytic efficiency for hydroxyproline 3-fold and decreases the specificity for proline"].
- FAD redox: [PMID:11294639 "an E(m)(E--FAD/E--FADH(2)) of --0.076 V for the two-electron reduction of PutA-bound FAD"].

## Transcriptional repression

- [PMID:11294639 "PutA represses transcription of the putA and putP genes by binding to the control region DNA of the put regulon"].
- DNA-binding domain mapped to residues 1-47, RHH; PutA90/PutA47 repress in vivo [PMID:15155740 "Cell-based transcriptional assays demonstrate that PutA90 functions as a transcriptional repressor in vivo"; "These results are consistent with the ribbon-helix-helix family of transcription factors"].
- Operators: five GTTGCA sites [PMID:18586269 "Five operator sites, each containing the sequence motif 5'-GTTGCA-3', were identified using gel-shift analysis. Three of the sites are shown to be critical for repression of putA, whereas the two other sites are important for repression of putP"].

## Functional switching and localization

- [PMID:28712849 "When the flavin cofactor is oxidized, EcPutA is cytosolic and functions as a transcriptional repressor of the put regulon via the N-terminal RHH domain."]
- [PMID:28712849 "Reduction of the flavin by proline causes EcPutA to associate with the cytoplasmic membrane thereby enabling EcPutA to catalyze the proline:ubiquinone oxidoreductase reaction."]
- PutA reconstitutes onto inverted membrane vesicles (cytoplasmic face outward) [PMID:1618807 "it could be reconstituted to inverted membrane vesicles, yielding proline dehydrogenase activity"].
- Peripheral membrane protein; no TM segment [PMID:12009917 "a peripherally membrane-bound enzyme"].
- Substrate channeling between PRODH and GSALDH sites in EcPutA [PMID:28712849 "The coupled PRODH-GSALDH activity of EcPutA is best described by a mechanism that includes a substrate channeling step"].

## Oligomeric state

- Dimer [PMID:1618807 "the protein in our preparation was dimeric with a molecular mass of 293 kDa"]; domain-swapped dimer in PutA669 crystal structure [PMID:12514740 "The structure is a domain-swapped dimer"]; RHH residues 1-47 stabilize the dimer [PMID:15155740].

## Oxidative stress

- putA mutant more sensitive to oxidative stress; proline oxidation generates H2O2 that pre-adapts cells via OxyR/katG [PMID:25384482 "the putA mutant strain was significantly more sensitive to oxidative stress than the parental wild-type strain"; "Proline oxidative metabolism was shown to generate hydrogen peroxide"]. Indirect / physiological; non-core.

## Curation judgments (summary)

- GO:0055129 L-proline biosynthetic process (InterPro2GO IEA): REMOVE; PutA is catabolic (UniProt PATHWAY: L-proline degradation into L-glutamate), consistent with the P. putida PutA review.
- GO:0097054 L-glutamate biosynthetic process (IDA x2): KEEP_AS_NON_CORE. Glutamate is the literal product of the PutA reaction, and these rows appear to descend from the obsoleted GO:0010133 "L-proline catabolic process to L-glutamate"; physiologically the process is proline catabolism (GO:0006562). Same judgment as the yeast PUT2 review.
- Generic DNA binding / sequence-specific DNA binding / transcription cis-regulatory region binding: MODIFY to GO:0000987, which the gene carries by IDA.
- Plasma membrane and cytoplasmic side of membrane: MODIFY to GO:0009898 cytoplasmic side of plasma membrane (IDA on the gene).
- Identical protein binding: MODIFY to protein homodimerization activity (GO:0042803), kept as non-core.


## 2026-11-06 comparative PutA-module audit

All original annotation payloads/order and historical NEW actions retained. All rows and core functions were re-read; only evidence/role inconsistencies were changed. Refined true anion/heterocyclic binding to supported FAD/proline/NAD interactions after official GO ancestor checks; no new annotation rows. Binding need not be a separate autonomous activity. Retained both catalytic reactions without assigning a universal quinone species or channeling mechanism.

GO0097054 directly describes formation of the central product L-glutamate and does not require de novo anabolism; existing product-formation rows are ACCEPT alongside proline catabolism. Specific cofactor/self-association/inducer-binding claims central to catalysis or repression are retained as core where already present. No universal RHH repression or channeling inference is made across all PutAs. [PMID:28712849; exact catalytic reactions in the protected UniProt record.]

A genuine default Falcon attempt was run and failed with HTTP403 authentication; no provider report was fabricated. Manual review used existing primary/review caches plus explicitly scoped independent PMC captures where recorded. PAINT loss checks found no IRD/IKR on the target lineage.
