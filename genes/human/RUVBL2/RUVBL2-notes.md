# RUVBL2 curation notes

## Deep research

Automated deep research was not available for this family workstream, so this review was completed from the seeded UniProt/GOA records, cached primary publications, and the existing INO80, SRCAP and TIP60/p400 module reviews. No manual `RUVBL2-deep-research-<provider>.md` file was created.

## Curation synthesis

RUVBL2 is best treated as the beta half of the alternating RUVBL1-RUVBL2 AAA+ ATPase ring. That ring appears in three chromatin-remodeling contexts already modeled by this repository: INO80, SRCAP/SWR1, and TIP60/p400. PMID:21303910 places Tip49a/RUVBL1 and Tip49b/RUVBL2 with IES2, IES6 and ARP5 on the INO80 Snf2 ATPase-domain module, and PMID:30337683 resolves the SRCAP complex as a ten-subunit assembly whose head is a RUVBL1-RUVBL2 heterohexamer. The same ATPase ring is also the core of R2TP and the PAQosome: PMID:29662061 reconstitutes human R2TP from RUVBL1-RUVBL2 plus RPAP3-PIH1D1 and maps RPAP3 binding to the RUVBL2 ATPase face, while PMID:33367824 shows the NOPCHAP1 adaptor bridging NOP58 to RUVBL1/2 during box C/D snoRNP assembly.

The strongest molecular-function annotation is `GO:0016887` ATP hydrolysis activity. PMID:17157868 is pivotal because it reproduced robust ATPase activity of an equimolar human TIP48/TIP49 complex but found no DNA helicase or branch-migration activity, so the older DNA helicase claim from PMID:10428817 was downgraded to `MARK_AS_OVER_ANNOTATED` rather than used as a core activity. PMID:33205750 further supports RUVBL2-specific nucleotide regulation by showing that DHX34 binding changes RUVBL2 N termini and suppresses RUVBL1-RUVBL2 ATP hydrolysis.

Most process annotations on RUVBL2 are outputs of the complexes that use the ring, not RUVBL2-specific jobs. Chromatin remodeling, INO80/SRCAP/TIP60 complex membership and box C/D snoRNP assembly were accepted as direct enough; replication stress recovery, homologous recombination, DNA repair, cell-cycle regulation, estrogen-responsive transcription and Wnt/beta-catenin signaling were kept as non-core or marked as over-annotated where the row was a distal perturbation endpoint. All bare `GO:0005515` protein-binding rows were removed by the project policy: they record many true interactions but not curatable molecular functions.
