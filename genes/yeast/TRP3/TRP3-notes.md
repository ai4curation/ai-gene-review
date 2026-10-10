# TRP3 (YKL211C, P00937) notes

Pathway context: TRPSYN-PWY-1 step 1 (anthranilate synthase component II, GATase; contributes to EC 4.1.3.27) and step 4 (IGPS, EC 4.1.1.48).

- Bifunctional: [PMID:3881257 "The smaller polypeptide carries both glutamine amidotransferase activity and indole-3-glycerolphosphate synthase activity."]
- TrpG and TrpC homology, 11-residue connector: [PMID:6323449 "establish the bifunctional structure of TRP3 protein"]
- Complex with Trp2: [PMID:3881257 "consists of two different subunits, the TRP2 gene product with Mr = 64 000 and the TRP3 gene product with Mr = 58 000"]
- trp3 mutants are 5-FAA resistant: [PMID:10790693 "trp1, trp3, trp4 or trp5 strains, which lack enzymes required for the conversion of anthranilic acid to tryptophan, are resistant to 5-fluoroanthranilic acid"]
- Induced by tryptophan starvation [UniProt:P00937].
- Curation decisions: core MFs = IGPS (enables) + anthranilate synthase (contributes_to). The IEA row 'enables GO:0004049' kept non-core (qualifier overstates). Protein binding rows (Trp2) MARK_AS_OVER_ANNOTATED. chorismate metabolic process kept non-core (GATase does contribute to a chorismate-consuming reaction), unlike downstream TRP enzymes.
- Ontology note: there is no GO MF for "anthranilate synthase glutamine amidotransferase (component II)" activity; the subunit-specific MF is left unset.
