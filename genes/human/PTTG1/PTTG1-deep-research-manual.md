# Manual deep research: human PTTG1 (securin)

This manual synthesis was prepared from the reviewed UniProt record, the 30
current GOA rows, the cached GOA-linked publications, and three additional
primary studies. It was created because the first OpenScientist request timed
out without producing a report; a second request was attempted independently.

## Core molecular role

PTTG1 is the human securin protein and forms a stoichiometric regulatory complex
with ESPL1/separase. Before anaphase, PTTG1 acts as a pseudosubstrate inhibitor:
its motifs occupy the separase catalytic site and adjacent substrate-docking
surfaces. This directly supports cysteine-type endopeptidase inhibitor activity
and separase-securin complex membership.

- [PMID:12194817 "Securin prevents the access of substrate analogs to the active
  site of separase."]
- [PMID:34290405 "As in Caenorhabditis elegans and yeast, human securin contains
  its own pseudosubstrate motifs."]
- [PMID:34290405 "Studies of truncated securin mutants revealed that this
  hydrophobic stretch is required for high-affinity securin-separase binding and
  inhibition of separase activity."]

PTTG1 is not only an inhibitor. Human knockout cells have defective separase
activation, and domain-dissection experiments distinguish separase-inhibitory
and separase-activating regions of PTTG1. The most specific supported activator
term is GO:0140608, cysteine-type endopeptidase activator activity.

- [PMID:11371342 "human cells without an hSecurin gene lose chromosomes at a
  high frequency"] and [PMID:11371342 "The abnormal mitoses were associated
  with biochemical defects in the activation of separin"].
- [PMID:23798554 "Although PTTG2 lacks securin function, its differences from
  PTTG1 provide evidence of independent inhibitory and activating functions of
  PTTG1 on separase."]

## Cell-cycle process

PTTG1 prevents premature cohesin cleavage and thereby maintains sister-chromatid
cohesion until the metaphase-to-anaphase transition. APC/C recognizes PTTG1's
destruction motifs, polyubiquitinates it, and targets it for proteasomal
destruction. Separase is then released to cleave cohesin and permit chromatid
separation.

- [PMID:10411507 "The vSecurin protein bound to a vertebrate homolog of yeast
  separins Esp1p and Cut1p and was degraded by proteolysis mediated by an
  anaphase-promoting complex in a manner dependent on a destruction motif."]
- [PMID:24781523 "Separase is activated at the metaphase-to-anaphase transition
  when both securin and cyclin B1 are degraded via the ubiquitin-proteasome
  pathway."]
- [Reactome:R-HSA-174202 "Following ubiquitination, securin is degraded by the
  26S proteasome."]

## Cellular distribution and secondary contexts

Human PTTG1 occupies both cytosolic and nuclear pools. It is highly expressed in
adult testis, and rat spermatocyte/spermatid expression plus interaction studies
suggest a role in spermatogenesis, but those data do not define a second core
molecular activity.

- [PMID:9811450 "Subcellular fractionation studies show that, although hPTTG is
  mainly a cytosolic protein, it is partially localized in the nucleus."]
- [PMID:9915854 "PTTG mRNA is expressed stage-specifically in spermatocytes and
  spermatids during rat spermatogenic cycle."]
- [PMID:9915854 "These results suggest that PTTG may play a role in
  spermatogenesis."]

## Evidence limitations

The cached versions of PMID:12194817, PMID:20360068, PMID:26496610,
PMID:9811450, PMID:9915854, and PMID:15929994 are abstract-only. No experimental
annotation was removed on the basis of missing full text. The three
proteome-scale interaction papers establish the design of their interaction
surveys in accessible text, while the exact PTTG1-ESPL1 pairs are represented
in GOA/IntAct; those rows are conservatively refined only from generic protein
binding to protease binding.
