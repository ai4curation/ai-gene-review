# REL review notes

## PTHR24169 context

REL encodes c-Rel, the `PTHR24169:SF4` member of the human NF-kappaB/Rel family.
It has the same N-terminal Rel-homology DNA-binding and dimerization domain as
NFKB1, NFKB2, RELA and RELB, but unlike NFKB1 and NFKB2 it is synthesized as a
transactivation-capable Rel subunit rather than as an ankyrin-repeat precursor.

## Evidence synthesis

c-Rel binds kappaB DNA motifs on its own or as a heterodimer with p50 or p65 in
the same recombinant-protein study that defined optimal p50 and p65 motifs
[PMID:1406630, "the product of the proto-oncogene c-rel can bind to similar DNA
motifs"]. The accepted core rows therefore center on RNA polymerase II
cis-regulatory DNA binding, NF-kappaB dimer complexes, chromatin/nuclear
localization, and positive regulation of RNA polymerase II transcription.

The largest block of REL GOA rows consists of BioPlex and other high-throughput
`GO:0005515` protein-binding edges. Those rows preserve the individual
`WITH/FROM` interactors but are all removed because bare protein binding is not
a curatable molecular function in this project.

REL also has experimental rows for repression of IFNB1 through YY1 after TLR3
signaling [PMID:22065573, "via induction of transcriptional repressor protein
YY1"]. This is a supported c-Rel/RelB regulatory context, but it is secondary to
the core c-Rel NF-kappaB DNA-binding transcription factor function.

## Automated research

`just deep-research human REL --provider perplexity` was not rerun after the
NFKB1 provider check failed with only `claude_code` available. No
`REL-deep-research-perplexity.md` artifact was created or filled manually.
