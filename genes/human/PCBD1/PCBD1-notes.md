# PCBD1 (P61457) review notes

## Identity
- HGNC:8646, UniProt P61457 (PHS_HUMAN), gene PCBD1 (synonyms DCOH, PCBD).
- 104 aa, small cytosolic/nuclear protein; homotetramer/homodimer.
- RecName: Pterin-4-alpha-carbinolamine dehydratase (PHS); EC 4.2.1.96.
- AltNames: 4-alpha-hydroxy-tetrahydropterin dehydratase; Dimerization cofactor of HNF1-alpha (DCoH / DCoH); Phenylalanine hydroxylase-stimulating protein; Pterin carbinolamine dehydratase (PCD).
- Classic bifunctional / moonlighting protein. MoonDB curated entry present in UniProt DR line.

## Function 1 — enzyme (PCD / PHS)
- Catalyzes: (4aS,6R)-4a-hydroxy-L-erythro-5,6,7,8-tetrahydrobiopterin = (6R)-L-erythro-6,7-dihydrobiopterin (quinonoid-BH2) + H2O. RHEA:11920, EC 4.2.1.96. [UniProt CATALYTIC ACTIVITY, P61457]
- 4a-hydroxy-BH4 (carbinolamine) is generated as an intermediate during aromatic amino acid hydroxylation (e.g. PAH-catalyzed Phe->Tyr). PCBD1 dehydrates it to quinonoid-BH2 which DHPR (QDPR) then reduces back to BH4 — i.e. PCBD1 is part of BH4 REGENERATION (recycling), not de novo synthesis. [UniProt FUNCTION "Involved in tetrahydrobiopterin biosynthesis ... Seems to both prevent the formation of 7-pterins and accelerate the formation of quinonoid-BH2"]
- Deficiency -> primapterinuria / mild transient neonatal hyperphenylalaninemia (HPABH4D, MIM 264070); increased excretion of 7-substituted pterins. [UniProt DISEASE]
- Substrate-binding residues 61-63 and 78-81 (ECO:0000250). [UniProt FT BINDING]

## Function 2 — DCoH transcriptional coactivator (moonlighting)
- Identified as Dimerization Cofactor of HNF-1alpha (DCoH); binds and stabilizes the HNF-1alpha homodimer, forming a stable tetrameric DCoH-HNF-1alpha complex; does not bind DNA itself and does not change HNF-1alpha DNA-binding, but enhances its transcriptional activity. Does NOT confer activation to a GAL4 DBD alone. [PMID:1763325 "A dimerization cofactor of HNF-1 alpha (DCoH) was identified that ... did not bind to DNA, but, rather, selectively stabilized HNF-1 alpha dimers. The formation of a stable tetrameric DCoH-HNF-1 alpha complex, which required the dimerization domain of HNF-1 alpha, did not change the DNA binding characteristics of HNF-1 alpha, but enhanced its transcriptional activity."]
- Also a coactivator for HNF1B: PCBD1 binds HNF1B (via HNF-p1 domain) and costimulates the FXYD2 promoter, controlling renal Mg2+ reabsorption in the distal convoluted tubule (DCT). [PMID:24204001 "Overexpression in a human kidney cell line showed that wild-type PCBD1 binds HNF1B to costimulate the FXYD2 promoter, the activity of which is instrumental in Mg(2+) reabsorption in the DCT."]
- HPABH4D late complications: hypomagnesemia w/ renal Mg2+ wasting and MODY-like diabetes, attributed to the HNF1B/HNF1A coactivator role. [PMID:24204001 abstract + Discussion]
- Recruited to the nucleus through interaction with HNF1B; monomers can passively diffuse into nucleus; PCBD1 homotetramer and PCBD1-HNF1 complex are mutually exclusive (same interface). [PMID:24204001 Discussion; UniProt SUBCELLULAR LOCATION Note]

## Subcellular location
- Cytoplasm and Nucleus (both experimentally, PMID:24204001, ECO:0000269). Nuclear recruitment via HNF1B. HPA/IDA (GO_REF:0000052) supports cytosol + nucleoplasm. IBA supports cytosol + nucleoplasm.
- Exosome (HDA) from urinary/prostatic proteomics screens — common contaminant/secreted-in-vesicle finding for abundant cytosolic proteins; keep as non-core.

## Scrutiny items
- GO:0004505 phenylalanine 4-monooxygenase activity (IEA, GO_REF:0000107 Ensembl Compara, with_from mouse Pcbd1 P61458). This is PAH's activity (L-Phe + BH4 + O2 = L-Tyr + 4a-hydroxy-BH4; def confirmed via OLS). PCBD1 does NOT hydroxylate Phe — it acts on the 4a-hydroxy-BH4 PRODUCT of that reaction. Clear over-propagation from an ortholog/compara artifact. REMOVE.
- GO:0006571 L-tyrosine biosynthetic process (IEA, GO_REF:0000108, inter-ontology link from GO:0004505). This is a downstream consequence of the erroneous 0004505 mapping. PCBD1 is not a tyrosine biosynthetic enzyme. REMOVE / over-annotated.
- GO:0006729 tetrahydrobiopterin biosynthetic process (IEA InterPro). PCBD1 regenerates BH4 (recycling) rather than de novo synthesis, but GO groups regeneration under the biosynthetic process node and this is the accepted community annotation; ACCEPT (with note it is recycling/regeneration).
- Bare protein binding (GO:0005515, many IPI from HT screens): uninformative; MARK/KEEP_AS_NON_CORE. Biologically meaningful partners captured better by DCoH coactivator MF/HNF1 process.
- identical protein binding (GO:0042802): reflects the homotetramer/homodimer (self-interaction P61457-P61457 in IntAct). ACCEPT/KEEP_AS_NON_CORE — real but supportive.

## GO term verification (OLS REST, 2026-07-05)
- GO:0008124 4-alpha-hydroxytetrahydrobiopterin dehydratase activity — current, not obsolete.
- GO:0006729 tetrahydrobiopterin biosynthetic process — current.
- GO:0003713 transcription coactivator activity — current.
- GO:0045893 positive regulation of DNA-templated transcription — current.
- GO:0004505 phenylalanine 4-monooxygenase activity — current (def = PAH reaction).
- GO:0006571 L-tyrosine biosynthetic process — current.
- GO:0005829 cytosol, GO:0005634 nucleus, GO:0005654 nucleoplasm — current.
