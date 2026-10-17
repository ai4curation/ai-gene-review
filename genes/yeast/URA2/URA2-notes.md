# URA2 (YJL130C, P07259) notes

Evidence journal built from UniProt and cached abstracts.

- Multifunctional CAD-like protein: GATase + CPSase (CPSase P, EC 6.3.5.5), defective DHOase-like domain, ATCase (EC 2.1.3.2) [UniProt:P07259]. "The DHOase domain is defective"; DHOase is URA4 [UniProt:P07259].
- [PMID:10446140 "The first two steps of the de novo pyrimidine biosynthetic pathway in Saccharomyces cerevisiae are catalyzed by a 240-kDa bifunctional protein encoded by the ura2 locus."]; channelling: [PMID:10446140 "the intermediate carbamoyl phosphate is channeled from the CPSase domain where it is synthesized to the ATCase domain"]; [PMID:3281587 "direct evidence for the channeling of carbamylphosphate"].
- pDHO: [PMID:10446140 "an inactive dihydroorotase homologue that bridges the two functional domains in the native molecule."]
- CPSase kinetics: UTP inhibition, XMP activation, K+ requirement [PMID:182284; PMID:237624 "Glutamine could be replaced partially by ammonium ions as nitrogen donor."].
- ATCase: in situ kinetics [PMID:6354093].
- Regulation: [PMID:5651325 "The activities of the first two enzymes, carbamoyl phosphate synthetase and aspartic transcarbamylase, are simultaneously controlled by feedback inhibition and repression."]
- Location: [PMID:11015727 "All three approaches localize the bulk of Ura2 to the cytoplasm, whereas the signals associated with the nucleus, mitochondria or vacuoles are close to or at the background level."]; some activity in membrane fractions [PMID:11921093].

## Curation decisions
- Core: GO:0004088 and GO:0004070, both in GO:0044205 de novo UMP biosynthesis, cytosol.
- Mitochondrion HDA x2 -> MARK_AS_OVER_ANNOTATED (contradicted by targeted localisation).
- protein binding (Cpr6, HTP) -> REMOVE (uninformative; no replacement MF).
- Generic RCA/IEA process terms (nucleotide biosynthetic, pyrimidine ribonucleotide biosynthetic) and pyrimidine nucleoside biosynthetic (IDA) -> MODIFY to GO:0044205; carboxyl/carbamoyltransferase -> MODIFY to ATCase.
- PMID:4550660 (IMP for ATCase/pyrimidine) abstract concerns URA5 regulation; full text not available - deferred to curator (ACCEPT).
- No arginine/citrulline-pathway annotation for URA2 exists in GOA (the YeastCyc link mentioned in the batch context was not propagated); none proposed: URA2 channels its carbamoyl phosphate to ATCase, so arginine-pathway CP comes from CPA1/CPA2.
