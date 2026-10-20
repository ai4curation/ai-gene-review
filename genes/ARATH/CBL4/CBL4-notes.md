# CBL4 / SOS3 (O81223, At5g24270) review notes

## Deep research status

`just deep-research ARATH CBL4` was attempted on 2026-10-20 with the falcon
(authentication failure), perplexity (provider not available) and openai
(invalid API key) providers; all failed. No deep-research file was generated.
These notes were compiled manually from cached PubMed/PMC records in
`publications/` (fetched with `ai-gene-review fetch-pmid`).

## Identity

- UniProt O81223 (CNBL4_ARATH), gene names CBL4, SOS3, At5g24270. 222 aa,
  four EF-hand domains, N-myristoylation site at Gly2, S-acylation at Cys3.
- Calcineurin B-like (CBL) family; PANTHER PTHR23056 (CALCINEURIN B).

## Literature synthesis

### Discovery and genetics
- sos3 mutant: hypersensitive to Na+ and Li+, not to general osmotic stress;
  defective on low K+; rescued by high external Ca2+
  [PMID:9405721 "Surprisingly, increased extracellular Ca2+ suppresses the growth defect of sos3 plants on low K+ or 50 mM NaCl."].
- Cloning: SOS3 resembles calcineurin B and neuronal calcium sensors
  [PMID:9632394 "SOS3 encodes a protein that shares significant sequence similarity with the calcineurin B subunit from yeast and neuronal calcium sensors from animals."].
  The original paper proposed a "calcineurin-like pathway", but later work
  showed the target is the SOS2 kinase, not a phosphatase
  [PMID:10725350 "Our results imply that plant salt tolerance may be mediated not by a calcineurin-like protein phosphatase but, rather, by the SOS3/SOS2 kinase complex."].

### Calcium binding and myristoylation
- [PMID:11006339 "Gel mobility shift and (45)Ca(2)+ overlay assays demonstrated that SOS3 is a unique calcium binding protein and that the sos3-1 mutation substantially reduced the capacity of SOS3 to bind calcium."]
- Myristoylation of Gly2 is required for complementation
  [PMID:11006339 "Expression of the myristoylated but not the nonmyristoylated SOS3 complemented the salt-hypersensitive phenotype of sos3-1 plants."].
- Crystal structure: Ca2+-induced dimerization
  [PMID:15644219 "calcium binding is responsible for the dimerization of SOS3"].
- Dual acylation: myristoylation for PM, S-acylation at Cys3 redirects to nucleus
  [PMID:34630451 "N-myristoylation at glycine-2 is essential for plasma membrane association and recruiting SOS2 to activate SOS1, whereas S-acylation at cysteine-3 redirects SOS3 toward the nucleus."];
  nuclear pool has limited role in salt tolerance
  [PMID:34630451 "The nuclear-localized SOS3 protein had limited bearing on the salt tolerance of Arabidopsis."].

### Activation of SOS2/CIPK24
- [PMID:10725350 "SOS3 activates SOS2 protein kinase activity in a Ca(2+)-dependent manner."]
- The SOS3-binding FISL/NAF motif of SOS2 is an autoinhibitory domain
  [PMID:11402167 "Removal of the regulatory domain of SOS2, including the SOS3 binding motif, resulted in constitutive activation of the protein kinase"].
- Structure of SOS3 bound to the SOS2 regulatory domain [PMID:17499048].
- Recruitment to PM and SOS1 activation in yeast
  [PMID:12070350 "We propose a model in which SOS3 activates and directs SOS2 to the plasma membrane for the stimulatory phosphorylation of the Na+ transporter SOS1."];
  [PMID:21262798 "SOS1 is relieved from auto-inhibition upon phosphorylation of the auto-inhibitory domain by SOS2-SOS3."].
- In planta PM vesicles: sos3 reduces Na+/H+ exchange
  [PMID:12034882 "These results demonstrate that SOS1 contributes to plasma membrane Na(+)/H(+) exchange and that SOS2 and SOS3 regulate SOS1 transport activity."].
- SOS3 also binds SOS1 and HKT1;1 directly (SOS2-independent)
  [PMID:38386704 "SOS3 achieves this role by direct and SOS2-independent binding to previously unrecognized functional domains of SOS1 and HKT1;1."].
- Unlike SCaBP8/CBL10, SOS3 is not phosphorylated by SOS2
  [PMID:19448033 "SOS2 phosphorylates SCaBP8 at its C terminus but does not phosphorylate SOS3."].

### Tissue specificity and relationship to CBL10
- [PMID:17449811 "We show that SOS3 acts primarily in roots under salt stress."]
- cbl4 cbl10 double mutant more sensitive than either single
  [PMID:31100786 "suggesting that CBL4 and CBL10 each directs a different salt-tolerance pathway"].

### Other partners / roles
- CBL4-CIPK6 targets the K+ channel AKT2 to the PM
  [PMID:21445098 "the calcium (Ca(2+)) sensor CBL4 together with the interacting protein kinase CIPK6 modulates the activity and plasma membrane (PM) targeting of the K(+) channel AKT2"].
- Interaction with many CIPKs in yeast two-hybrid (CIPK1 etc.) [PMID:10590166, PMID:11115898, PMID:11230129].
- sos3 roots lack salinity-induced cytosolic alkalinization [PMID:36834961].
- Actin reorganization under salt stress [PMID:23052592] (abstract only; indirect).
- PEN3/ABCG36 interaction found by protein microarray [PMID:26315018] (abstract
  only; abstract highlights CaM7, not CBL4).

## GOA issues noted
- GO:0004723 calcium-dependent protein serine/threonine phosphatase activity
  and GO:0005955 calcineurin complex (both ISS, PMID:9632394): transfer of the
  catalytic/complex identity of animal/yeast calcineurin to a calcineurin
  B-like regulatory protein. No calcineurin A homolog exists in Arabidopsis and
  CBL4's demonstrated partner is a kinase. Removed.
- GO:0042539 hypotonic salinity response (IMP, PMID:9405721): the paper tests
  increased NaCl (hypersensitivity to Na+/Li+), so the hypotonic (decrease in
  salt) term is a term-selection error; replaced with GO:0042538 hyperosmotic
  salinity response.

## Review decisions (2026-10-20)
- Core functions: (1) Ca2+-dependent activator of CIPK24/SOS2 at the plasma
  membrane (GO:0043539; calcium-mediated signaling; hyperosmotic salinity
  response); (2) EF-hand Ca2+ binding / Ca2+ detection (GO:0005509, GO:0005513).
- REMOVE: GO:0004723 and GO:0005955 (ISS calcineurin transfers); GO:0005515 IPI
  with PEN3/ABCG36 (PMID:26315018, microarray hit, no informative MF; per
  protein-binding policy).
- GO:0005515 IPI rows with SOS2 MODIFY -> GO:0043539 where the paper shows
  activation (PMID:10725350, 11006339, 11402167, 21262798), otherwise ->
  GO:0019901 protein kinase binding (CIPK1 rows; PMID:17449811, 17785451).
- GO:0019900 kinase binding (IEA) MODIFY -> GO:0019901.
- Suspected source-record error: GO:0042539 hypotonic salinity response (IMP,
  PMID:9405721, TAIR) should be GO:0042538 hyperosmotic salinity response; the
  paper tests increased NaCl/LiCl. Recorded as MODIFY (the `source_defects`
  schema slot was not yet available in this branch).
- No NEW annotations proposed.
