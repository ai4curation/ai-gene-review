# Archived DsbB identity and assay scope

A8FLS4 is the archived 81116 DsbB record, not a current live UniProtKB entry. Official UniSave version 50 identifies gene dsbB, locus C8J_0812, CAMJ8, NCBITaxon:407148 and strain 81116 / NCTC11828. Its 260-residue sequence matches ENA CP000814.1 translation ABV52411.1 and UniParc UPI00015D00EB exactly. The sequence SHA256 is `17efc48df7e7f539143ff67bf2281f647f9cc5fe189c0ed9c78a18d1b4b49ad0`. All 50 versions in the official history carry sequence version 1. This is an exact archived native-strain record, not transfer from NCTC11168.

The adjacent `A8FLS4-unisave-v50-uniprot.txt` is the byte-identical official archived response, SHA256 `ca6094e8a57bc78de2c90284127aabd15cf07066e31097a5ed00d9e57a124d20`. It is explicitly distinct from the canonical empty live dsbB-uniprot.txt. The normal canonical fetch seeded the correct taxon through CAMJ8 mnemonic resolution and obtained a genuine header-only GOA snapshot, with zero annotations. Every reviewed annotation is therefore authored NEW; none was manufactured as an archived GAF row.

Official source endpoints:
- https://rest.uniprot.org/unisave/A8FLS4?format=txt&versions=50
- https://rest.uniprot.org/unisave/A8FLS4?format=json
- https://www.ebi.ac.uk/ena/browser/api/embl/CP000814.1?download=false
- https://rest.uniprot.org/uniparc/UPI00015D00EB

The archive records IPR003752, IPR023380 and PF02600. It contains no PANTHER cross-reference; no family or ancestral node is guessed. The historical GO cross-references are GO0016021, GO0005886 and GO0015035 with their 2015 labels and IEA sources. Those fields describe that release, not present-day annotations or experimental evidence. The archival record and its evidence tags are retained unchanged.

PMID34948248 section5.2.3 identifies native 81116 CP000814 as the PCR donor and describes the NheI-HindIII insert in pET24a/pUWM1469 with a C-terminal polyhistidine tag. The authors state that the construct was verified by sequencing. The exact tag junction and complete recombinant sequence were not independently reconstructed here; the native donor sequence is exact, while the assayed protein is tagged. The approximate 0.75-kb description is not substituted for the verified 260-aa native translation.

The partially purified, detergent-solubilized DsbB preparation reoxidized both recombinant DsbA1 and DsbA2 at 1/2-hour AMS endpoints with exogenous UQ/MK7. The authors explicitly omitted a no-DsbB control. These data support the proposed partner reaction when combined with native DsbA1 redox-state changes and DsbA2 abundance loss in the dsbB mutant. They do not independently quantify quinone reduction, establish equal binding affinities or identify the physiological quinone. The paper states that neither assay quinone occurs naturally in C. jejuni. Accordingly GO0015035 is proposed by IC, but the more acceptor-specific GO0016672 is not asserted for this target.

Native 81116 client assays in PMID25181355 found AstA activity at 8% and PhoX activity at 53% of wild type in the dsbB mutant. These support the functional system but do not prove direct oxidation of AstA/PhoX by DsbB: the DsbA proteins perform the substrate-oxidation step and DsbB recycles them. PMID32203539 also reports altered C8J_1298 redox state in several dsb mutants, including dsbB. That network effect is not a purified direct DsbB-C8J_1298 reaction or evidence for DsbB isomerase activity. The later paper corrects the old DsbA1 motility attribution to background mutation; no motility function is added here.

Protein-folding BP participation is supported by DsbB performing oxidoreductase regeneration, not by being a substrate or merely being required for a phenotype. Same-role QuickGO convention checks found GO0006457 on E. coli P0A6M2 and P. aeruginosa PAO1 P21482/P57701 (eight rows, including IMP on the PAO1 records). Those annotation observations are not used as supported_by evidence and do not substitute PAO1 for the 81116 target. The BP is under protein metabolic process/cellular process, does not duplicate the MF or plasma-membrane location, and no target entry was found in gocams/index.tsv.
