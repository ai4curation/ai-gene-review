# GatA (Q9VE09; CG6007, formerly bene) review notes

## Identity
- Amidase-family GatA subunit of mitochondrial GatCAB (human QRSL1 ortholog).
  [file:DROME/GatA/GatA-uniprot.txt "This subunit probably catalyzes the hydrolysis"].
- Fly naming: [PMID:26761199 "CG5463 and CG33649 genes – we propose to name the latter two GatB and GatC, respectively"];
  pathway: [PMID:26761199 "converting Glu to Gln via a heterotrimeric Glu-tRNAGln amidotransferase (Gat)"].
- Mitochondrial: IDA from the Liao et al. screen [PMID:16849596 "each encodes a mitochondrial protein"] (abstract only cached).
- Serine hydrolase HDA (PMID:33827210, ABPP atlas): GatA not visible in cached text; amidase-signature
  enzymes use a Ser nucleophile so FP-probe labelling is expected; kept non-core.

## Decisions (module dmel_glutamyl_trna_amidotransferase, consistent across GatA/B/C)
- Complex, mitochondrion/matrix, contributes_to GO:0050567: ACCEPT.
- Obsolete GO:0070681: MODIFY -> GO:0043685 conversion of glutamyl-tRNA to glutaminyl-tRNA
  (GO obsoletion comment says annotations need review, no automatic replacement).
- Mitochondrial translation: KEEP_AS_NON_CORE (real but downstream; the step is GO:0043685).
- Generic catalytic activity -> MODIFY to glutaminase activity; glutaminase activity ACCEPT.

## Deep research (falcon)
- GatA was previously named benedict (bene); bene/gatA mutants (Genetics 2008) show growth defects in mitotic and endoreplicating tissues (not cached; cited by deep research): [file:DROME/GatA/GatA-deep-research-falcon.md "found GatA to be the only obvious fly ortholog of this amidotransferase subunit"].
