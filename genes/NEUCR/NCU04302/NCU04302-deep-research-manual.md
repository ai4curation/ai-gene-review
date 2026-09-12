# Manual research synthesis: NCU04302 (Q1K772)

This report was researched manually on 2026-09-09 after provider failure. It is not a Falcon or Perplexity report. Sources inspected include the complete current UniProt sequence/features, the seeded GO annotations, the preserved prediction/donor records where applicable, and the primary publications cited below.

## Biological synthesis

NCU04302 encodes a 157-residue Ubc9-family SUMO-conjugating E2 enzyme. Its conserved UBC catalytic domain and phylogenetic placement support transfer of activated SUMO to protein substrates, predominantly in the nucleus. SUMO modification provides a mechanism for regulating nuclear proteins; target-specific substrates and the distribution among nuclear subcompartments remain incompletely characterized.

## Direct and comparative evidence

- file:NEUCR/NCU04302/NCU04302-uniprot.txt: “DR   InterPro; IPR000608; UBC.”
- PMID:9435231: “Moreover, recombinant yeast and mammalian UBC9 enzymes were found to form thioester complexes with SMT3 and SUMO-1, respectively.”

## Modifier specificity and donor

The PAINT SUMO-E2 node is PANTHER:PTN000629675. The UBC catalytic fold alone is insufficient to discriminate ubiquitin from SUMO. A direct comparative sequence analysis in NCU04302-bioinformatics therefore checks the target against reviewed human/fission-yeast Ubc9 and the recorded Arabidopsis ubiquitin-E2 donor P42745. PMID:9435231 demonstrates Ubc9 SUMO thioesters; PMID:16339806 reports Arabidopsis ubiquitin E2s and includes UBC1–6 activity. The donor’s reviewed function string exactly matches the paragraph. This records sequence/text provenance, not a claim about the model’s internal reasoning. QuickGO definitions cached in NCU04302-go-definitions.json distinguish isoenergetic SUMO and ubiquitin E2 transfer from the ATP-coupled ligase definition; E1 activation is a separate reaction step.

## Annotation implications

- GO:0061656: ACCEPT. The UBC catalytic domain and PAINT placement at PTN000629675 support the Ubc9 SUMO-E2 subfamily. Biochemical work on yeast and mammalian Ubc9 establishes SUMO thioester formation, making SUMO conjugation a well-grounded conserved function.
- GO:0016925: ACCEPT. The UBC catalytic domain and PAINT placement at PTN000629675 support the Ubc9 SUMO-E2 subfamily. Biochemical work on yeast and mammalian Ubc9 establishes SUMO thioester formation, making SUMO conjugation a well-grounded conserved function.
- GO:0005634: ACCEPT. Nuclear localization is supported by the conserved Ubc9 phylogenetic annotation at PTN000629675 and the nuclear SUMO-conjugation pathway. This is a family-based localization inference rather than direct imaging of NCU04302.
- GO:0000792: UNDECIDED. The ortholog transfer from fission-yeast P40984 specifies heterochromatin. Nuclear SUMO conjugation is established at family level, but conserved residence in this particular chromatin compartment has not been verified for Neurospora.
- GO:0005694: UNDECIDED. Chromosome residence is more specific than the supported nuclear SUMO pathway. The ARBA chromosome assignment does not establish stable or regulated chromosome association of this protein, and target-specific localization evidence was not recovered.
- GO:0006281: KEEP_AS_NON_CORE. Ubc9-mediated SUMO conjugation can support genome maintenance through modification of repair proteins. The fission-yeast ortholog transfer is biologically coherent, but DNA repair is one substrate-dependent role of a general SUMO E2 rather than its defining biochemical function.
- GO:0016874: MODIFY. Ubc9 catalyzes transfer of activated SUMO through a thioester intermediate; ATP-dependent modifier activation belongs to the E1 step. The more specific SUMO conjugating enzyme activity identifies the E2 chemistry and avoids the generic ATP-coupled ligase assignment.
- GO:0019789: ACCEPT. SUMO transferase activity is a valid broad description of Ubc9-mediated covalent SUMO transfer. The conserved SUMO-E2 placement and Ubc9 biochemistry provide the biological support independently of this row’s electronic source.
- GO:0061631: MODIFY. This EC:2.3.2.23 mapping specifies transfer of ubiquitin, whereas PAINT places NCU04302 in the SUMO-conjugating Ubc9 lineage. The substrate distinction is mechanistic: the characterized Ubc9 homologs form SUMO thioesters. Replace the ubiquitin-specific activity with SUMO conjugating enzyme activity.
- GO:0106068: ACCEPT. Conserved Ubc9 association with SUMO-conjugation partners supports the broad complex definition; neither permanent residence nor a specific Neurospora E3 partner is asserted.

## Ubc9-specific evidence and complex definition

Exact sequence-classification excerpts: “DR   CDD; cd23798; UBCc_UBE2I; 1.” and “DR   FunFam; 3.10.110.10:FF:000035; SUMO-conjugating enzyme ubc9; 1.” The independent full-length reference comparison and all parameters are in NCU04302-bioinformatics/RESULTS.md. PMID:12597774 supplies direct SUMO-conjugation experiments on the 75%-identical fission-yeast Ubc9 reference. GO:0106068 was checked in QuickGO and includes a SUMO-protein transferase with specificity-associated proteins; stable residence is not required. PMID:17466333 describes the conserved SUMO E2 interactions with substrate and E3 ligase during conjugation, supporting broad SUMO ligase-complex membership.
