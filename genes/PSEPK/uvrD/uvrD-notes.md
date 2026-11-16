# uvrD curation notes

Q88C31 (PP_5352) has the UvrD-family architecture and exact EC 5.6.2.4
directional helicase assignment. A direct P. putida deletion study found
elevated mutation frequencies but also reported that "NER or MMR pathways are
not completely abolished in UvrD-deficient P. putida" [PMID:30292721].
The positive mutant evidence is the elevated-mutation and DNA-damage-survival
phenotype [PMID:30292721 "UvrD helicase is essential to prevent the emergence
of mutations"]; a P. aeruginosa uvrD allele independently showed defective
mismatch repair [PMID:11952911 "showing defective mismatch repair activity."].

Mismatch repair and nucleotide-excision repair were therefore added as direct
IMP-supported processes, with wording that preserves the observed redundancy.
Generic helicase, hydrolase, and nucleotide-binding parents were marked
over-annotated rather than duplicated in the core function.

## OpenScientist adjudication

The OpenScientist report corroborated the UvrD-family identity and
ATP-dependent 3'-to-5' DNA helicase assignment. It missed the direct P. putida
deletion paper already used in the review and therefore understated the
organism-specific evidence; the report is used only for conserved molecular
function support, not for process assertions.

## Completion pass (Claude, AI-assisted)

Every row now carries vetted `supported_by` quotes (UniProt family/domain
cross-references and PROSITE-ruled domain features, the PTHR11070 PAINT rows,
the E. coli ortholog literature, PMID:30292721 and PMID:11952911); the ARBA-only
UniProt EC and SIMILARITY lines are no longer cited. Actions were harmonised
with the E. coli UvrD review (P03018):

- Generic parents (DNA helicase, helicase, nucleotide binding, hydrolase) changed
  from MARK_AS_OVER_ANNOTATED to MODIFY with the specific term already on the
  gene (correct-but-general rule).
- Recombinational repair (TreeGrafter, from PTN000116141) changed from
  KEEP_AS_NON_CORE to MARK_AS_OVER_ANNOTATED: the PAINT node is seeded by RecB,
  Srs2 and Fbh1, while UvrD-subfamily helicases act mainly as anti-recombinases
  [PMID:16135232 "UvrD acts by removing RecA or a RecA-made structure, allowing
  replication fork reversal."].
- Identical protein binding (ARBA) modified to protein homodimerization activity
  [PMID:12527299 "two UvrD monomers must bind the DNA substrate in order to form
  a complex that is able to unwind short DNA substrates in vitro."].
- P. aeruginosa evidence refined: the ATP-site uvrD allele is MMR-defective but
  NER-proficient [PMID:11952911 "Interestingly, cells carrying this mutant allele
  exhibited a fully active UvrABC-mediated excision repair."], so it supports
  only the MMR row.
