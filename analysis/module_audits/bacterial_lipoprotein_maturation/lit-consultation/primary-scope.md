# Lit source identity and activity review

## Selected exact exemplar

The single reviewed exemplar is Q813T3, BC_1526, Bacillus cereus ATCC14579 (BACCR; NCBITaxon226900), 218 residues. PMID28320885 identifies BC1526 in this exact strain (Methods/Table1) and connects deletion/complementation to the native PrsA lipid chemotype (Figure7). PMID34253723 Methods directly names Q813T3_BACCR as its target. The official UniProt record independently links BC_1526 to AAP08506.1/AE016877 and the same strain. This is an explicit accession bridge, not a name-only orthology inference.

PMID32471867 uses Enterococcus faecalis WMC_RS08810, traced through the discovery paper to ATCC19433. It is not a V583 experiment. That exact current UniProt accession remains unresolved: WMC_RS08810 search returned none, NCBI protein locus search returned none, and official genome searches either expanded ATCC19433 as a species synonym or yielded an unrelated title match. These responses are not identity evidence. PMC supplement requests returned a download challenge and publisher access was blocked; no supplement sequence was claimed as read. The directly studied, explicitly accession-named Bacillus alternative is therefore selected without inventing an Enterococcus accession.

## What each primary establishes

PMID28320885: native B.cereus BC1526 loss and complementation alter PrsA's N-terminal lipid structure. The same discovery paper studies Enterococcus ATCC19433. Native lipid product chemistry and locus identity are used, not a general essentiality or resistance claim.

PMID32471867: isotope-labelled Lpp substrate and Lit-containing E.coli inner-membrane fractions support intramolecular transfer for Enterococcus Lit. The enzyme source was not purified Lit. Histidine functional/topology evidence supports an extracellular-interface reaction. The acid-base route and cyclic intermediate were proposed, whereas chain relocation was measured. No source-specific numeric result is transferred to Bacillus.

PMID34253723: the exact Bacillus target was purified after heterologous expression. Synthetic lipopeptide product NMR establishes sn-2 ester-to-N-terminal-amide relocation. The structure resolves four membrane helices and an extracytoplasmic cap. Functional and structural evidence implicates H85/H153; detailed proton transfers and the eight-membered intermediate derive from a mechanistic model including computation, not a trapped native reaction intermediate. The product retains two acyl chains. Lit thus differs from Lnt's addition of a third chain. No substrate copper interaction is converted into a copper-binding enzyme annotation, and no host immune-process annotation is proposed.

## Ontology and participation

Fresh QuickGO defines GO0016867 as acyl transfer within one molecule. Its current specific descendants do not name the Lit substrate. GO0140186 instead specifies acyl-CoA donation to protein lysine N6 and does not fit this reaction. The exact activity is stated in core prose; an unsupported specific GO identifier is not invented. GO0042160 describes covalent alteration of lipid/amino-acid residues in an existing lipoprotein. Its parent chain is metabolic, not proteolytic. Lit directly catalyzes that alteration: it is neither the substrate nor merely a necessary upstream factor. GO0005886 represents the bacterial cytoplasmic membrane.

The same-role experimental comparator is ATCC19433 WMC_RS08810, whose accession query is unresolved. A current Lit-family survey independently found reviewed O67827 (Aquifex aq_2036; only plasma-membrane GOA) and A8DYQ9 (Listeria pCT0028; no GOA). These are family candidates, not newly verified experimental Lit exemplars; their absent BP coverage is not evidence of an established contrary curation convention. Q813T3 itself has zero GOA rows. Sparse annotations alone do not justify additions: the three NEW proposals instead rest on exact-target primary chemistry/structure and native product evidence. No redundant ancestor/descendant pair is added. No Q813T3, O67827 or A8DYQ9 model was found in the local GO-CAM index. Comparator GOA is only a survey record, never cited as function support.

## Source and provider access

The immutable PMID32471867 cache was abstract-only. Genuine full main-text HTML for that paper and discovery PMID28320885 was retrieved separately from PMC with `?report=xml`; hashes and URLs are in source-provenance.yaml. This query returns HTML, not XML. Normal fetching of missing28320885 cached only its abstract; normal fetching of missing34253723 supplied full text. Neither protected existing publication was refreshed. Failed HTML/challenge responses are recorded as failures, not full text. The configured Falcon attempt for BACCR BC_1526 failed with HTTP403 authentication. No provider report was fabricated. Manual evidence synthesis supplies the review.

## Family scope

Official Q813T3 cross-references identify InterPro IPR010178 (Lit), Pfam PF07314 (Lit), NCBIfam NF051877 (lptranacylLit) and TIGR01906. No PANTHER assignment is present; none is inferred. Family membership alone is not an experimentally verified substrate-specific activity claim for every member.
