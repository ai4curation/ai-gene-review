# CASQ1 evidence notes

CASQ1 is the skeletal calsequestrin paralog. Its core activity is high-capacity
calcium sequestration in the sarcoplasmic-reticulum terminal cisterna lumen,
supported by human skeletal CASQ1 crystal structures with calcium-binding sites
and by tubular-aggregate-myopathy mutants that disrupt calcium-dependent
aggregation, storage and SR release [PMID:22337878, PMID:28895244,
PMID:27196359].

CASQ1 and CASQ2 share the calsequestrin calcium-binding and polymerization
module, but the PAINT biological-process split is paralog-specific: CASQ1 carries
skeletal-muscle release regulation at PTN002559189 and CASQ2 carries cardiac
release regulation at PTN002559177. PTN000004019's terminal-cisterna and
SR-lumen assertions fit both paralogs; the same node's Z-disc assertion is not
accepted for CASQ1 because a luminal junctional-SR reservoir is adjacent to
sarcomeric markers without becoming a Z-disc constituent.

The two SOCE rows annotated as positive regulation need a sign correction.
Zhang et al. report that CSQ1-STIM1 interaction suppresses STIM1 aggregation and
SOCE in heterologous cells, while Barone et al. report that CASQ1 tubular
aggregate mutants lose part of the wild-type inhibitory effect on SOCE
[PMID:27185316, PMID:28895244]. Those rows are MODIFIED to negative regulation
of store-operated calcium entry; the generic CSQ1-STIM1 protein-binding row is
removed as bare GO:0005515.

The mitochondrial matrix branch is left out of the synthesized function. The
1994 calmitine paper asserted enrichment in mitochondrial matrix, and a later
human skeletal-muscle mitochondrial phosphoproteome recovered CASQ1, but the
modern P31415 record has an ER signal peptide and direct human CASQ1 disease and
STIM1 studies place the protein in ER/SR compartments [PMID:7945294,
PMID:20833797, PMID:27196359, PMID:27185316].
