# SLC3A1 review notes

## Research provenance

Falcon deep research was attempted and failed with HTTP 402. The configured
Perplexity-lite fallback was then attempted and failed with HTTP 401 because the
API quota was unavailable. No provider-named output was retained. The review
therefore uses the reviewed UniProt Q07837 record, the complete local GOA seed,
official QuickGO term definitions, the three Reactome records in the seed, nine
cached primary publications, and the manual synthesis in
`SLC3A1-deep-research-manual.md`.

The six publications fetched from the GOA seed were all inspected. Three
additional primary papers were cached and read because they resolve the key
curation boundary: PMID:10588648 identifies SLC7A9 as the catalytic subunit,
PMID:16825196 establishes rBAT-dependent oligomerization, and PMID:9987991 is
the rat source underlying the vacuolar-membrane transfer.

## Core biological interpretation

SLC3A1 encodes rBAT, the type II glycoprotein heavy chain of an apical
heteromeric amino-acid transporter. It forms a disulfide-linked heterodimer with
SLC7A9. Native human kidney brush-border membranes contain the complex
[PMID:12167606 "rBAT and b(0,+)AT were solely expressed as heterodimers of identical size"],
and the complex accounts for essentially all apical cystine reabsorption in the
studied proximal-tubule context [PMID:12167606 "responsible for virtually all apical cystine reabsorption"].

The heavy/light-chain distinction is decisive for reviewing the old transporter
molecular-function annotations. SLC7A9 is the catalytic subunit
[PMID:10588648 "b(0,+)AT as the catalytic subunit that associates by a disulfide bond with rBAT"].
The heavy chain instead supports trafficking and maturation
[PMID:32817565 "The light chain constitutes the transport subunit whereas the heavy chain mediates trafficking to the plasma membrane"].
SLC3A1 is therefore involved in cystine and dibasic-amino-acid transport and
renal absorption, but it does not independently enable the amino-acid
transmembrane transporter activity. The review represents the direct function
as transporter activator activity and the complex-level transporter function as
`contributes_to_molecular_function`.

## Complex architecture and the extracellular domain

The rBAT-SLC7A9 heterodimer is the minimal functional unit, while rBAT-rBAT
contacts assemble two heterodimers into a heterotetramer. The title and abstract
of PMID:16825196 explicitly state that the heavy chain dictates oligomerization
and that "a single heterodimer is the functional unit." Cryo-EM independently
resolves rBAT-mediated dimerization [PMID:32494597 "rBAT mediates the dimerization of HATs"].

The large extracellular rBAT region has an alpha-amylase-like fold, which drives
an InterPro annotation to carbohydrate metabolic process. That inference is
experimentally contradicted: the purified complex had no detectable
alpha-glucosidase activity [PMID:32494597 "The results showed that the complex has no α-glucosidase activity"].
The carbohydrate-process IEA is therefore removed rather than merely downgraded.

## Localization boundaries

Brush-border, apical-plasma-membrane, plasma-membrane, and membrane annotations
all agree with the established epithelial site and are accepted. Urinary-exosome
detection comes from a large proteomic survey whose local abstract does not expose
the SLC3A1 peptide result [PMID:19056867 "analysis identified 1132 proteins unambiguously"].
It is left undecided rather than treated as a verified functional exosome assignment.

The vacuolar-membrane transfer traces to rat forebrain immunoelectron microscopy
[PMID:9987991 "immunogold labeling for NBAT was distributed along plasmalemmal and vacuolar membranes"].
Because the source-side experiment is explicit, the human IEA is kept as non-core;
its relevance to endogenous human neuronal biology remains unresolved.

## Annotation decisions

| Annotation group | Decision |
|---|---|
| brush border membrane (4 evidence groups) | ACCEPT |
| amino acid transport (3 evidence groups) | ACCEPT |
| amino acid transmembrane transport | ACCEPT as a process contribution |
| plasma membrane (7 evidence groups) | ACCEPT |
| carbohydrate metabolic process | REMOVE |
| membrane (2 evidence groups) | ACCEPT |
| apical plasma membrane (2 evidence groups) | ACCEPT |
| basic amino acid transmembrane transport | ACCEPT as a process contribution |
| protein binding (2 evidence groups) | MODIFY to protein heterodimerization activity |
| vacuolar membrane | KEEP_AS_NON_CORE |
| protein-containing complex binding | MODIFY to protein heterodimerization activity |
| transmembrane transporter complex | MODIFY to amino acid transport complex |
| protein heterodimerization activity | ACCEPT |
| extracellular exosome | UNDECIDED |
| amino acid transmembrane transporter activity | MODIFY to transporter activator activity |
| basic amino acid transmembrane transporter activity | MODIFY to transporter activator activity |
| L-cystine transmembrane transporter activity | MODIFY to transporter activator activity |
| basic amino acid transport | ACCEPT |
| L-cystine transport | ACCEPT |
| renal amino acid absorption | NEW |

Duplicate GO terms use consistent actions. No generic protein-binding annotation
is retained, and no experimental annotation is removed on the basis of missing
full text.

## Open questions

- What are the relative human proximal-tubule contributions of SLC7A9 and SLC7A13 as SLC3A1 partners?
- Do any noncanonical SLC3A1 isoforms form stable surface complexes?
- Does endogenous human neuronal SLC3A1 occupy vacuolar membranes?
- Which nonenzymatic properties of the extracellular glycosidase-like domain control folding, oligomerization, or trafficking?
