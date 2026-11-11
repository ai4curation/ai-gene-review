# phaZ Gene Review Notes

## Identifier Mapping

- In KT2440, the literature gene name `phaZ` maps to locus `PP_5004` and UniProt `Q88D24`, even though the UniProt gene line currently says `Name=phaB`. [file:PSEPK/phaZ/phaZ-uniprot.txt, "SubName: Full=Poly(3-hydroxyalkanoate) depolymerase"; "GN   Name=phaB"; "GN   OrderedLocusNames=PP_5004"; "DR   ESTHER; psepu-PHAZ; PHA_depolymerase_arom."]

## Core Function

- PhaZ is the intracellular granule-associated depolymerase that mobilizes stored medium-chain-length PHA in KT2440. [JBC 2007 PDF, "first formal biochemical evidence that PhaZ is certainly an intracellular mcl-PHA depolymerase"; https://pdfs.semanticscholar.org/ae3e/1d24baa56e7222a02f12b2b3b75ee84cee02.pdf]
- Biochemical work on the highly similar KT2442 ortholog showed that 3-hydroxyoctanoate monomer is the main hydrolysis product and classified PhaZ as an endo/exo-mcl-PHA depolymerase. [JBC 2007 PDF, "the monomer of HO was identified as the main product of PhaZ hydrolysis"; "classify PhaZ as an endo/exo-mcl-PHA depolymerase"; https://pdfs.semanticscholar.org/ae3e/1d24baa56e7222a02f12b2b3b75ee84cee02.pdf]
- The best current molecular-function term is GO:0050527 poly(3-hydroxyoctanoate) depolymerase activity rather than triacylglycerol lipase activity. [AmiGO GO:0050527, "poly(3-hydroxyoctanoate) depolymerase activity"; https://amigo.geneontology.org/amigo/term/GO%3A0050527]

## Physiological Role

- Deletion of phaZ increases and stabilizes PHA accumulation, showing that PP_5004 participates in poly(3-hydroxyalkanoate) metabolic process in vivo. [PMC3918157, "the Delta phaZ knockout phenotype suggests that the PhaZ depolymerase is a major determinant of PHA accumulation and maintenance in the cell"; https://pmc.ncbi.nlm.nih.gov/articles/PMC3918157/]
- PhaZ is associated with polyhydroxyalkanoate granules rather than glycerolipid catabolism. [JBC 2007 PDF, "Identification of PhaZ as granule-associated protein"; PMC6922519, "the gene encoding the PHA depolymerase (phaZ; PP_5004) was deleted"; https://pdfs.semanticscholar.org/ae3e/1d24baa56e7222a02f12b2b3b75ee84cee02.pdf; https://pmc.ncbi.nlm.nih.gov/articles/PMC6922519/]

## GO Review Implications

- GO:0004806 triacylglycerol lipase activity is a substrate-misassigned automated annotation and should be replaced by GO:0050527. [file:PSEPK/phaZ/phaZ-uniprot.txt, "SubName: Full=Poly(3-hydroxyalkanoate) depolymerase"; AmiGO GO:0050527, "poly(3-hydroxyoctanoate) depolymerase activity"; https://amigo.geneontology.org/amigo/term/GO%3A0050527]
- GO:0046503 glycerolipid catabolic process is misleading because intracellular PHA mobilization is not glycerolipid catabolism; GO:0042620 poly(3-hydroxyalkanoate) metabolic process is closer, but GO currently lacks a direct poly(3-hydroxyalkanoate) catabolic process term for intracellular PHA mobilization. [AmiGO term graph, "GO:0042620 poly(3-hydroxyalkanoate) metabolic process"; JBC 2007 PDF; https://amigo.geneontology.org/amigo/term/GO%3A0008152; https://pdfs.semanticscholar.org/ae3e/1d24baa56e7222a02f12b2b3b75ee84cee02.pdf]


## 2026-11-07 comparative source audit

Completed all existing annotations for phaZ; preserved ordered source payloads and provider artifacts. Genuine existing provider reports were read as leads, with primary evidence and exact strain boundaries prioritized. Evidence, ontology snapshots, PAINT limits and supplementary provenance are under analysis/module_audits/bacterial_mcl_pha_synthesis_and_mobilization/psepk-consultation/. No new GO row added. PAINT target-leaf unavailable is not evidence of absence of evolutionary loss.

Full17170116 distinguishes KT2442 recombinant/native-granule assays from KT2440. Weak overnight tributyrin hydrolysis is retained as peripheral MF; native glycerolipid-catabolic flux is not inferred. The historical granule NEW/IDA proposal is retired in place with root authorization for unsupported target-direct provenance, not rejection of localization. Original row archived in retired-phaZ-proposal.yaml. Core location remains qualified, corroborated by native fraction detection without selective-enrichment claim. Native31468725 found no titre/yield improvement after phaZ deletion under its tested accumulation conditions, superseding unconditional older notes.


## PR6194 follow-up — 2026-11-07

GO0004806 changed to MARK_AS_OVER_ANNOTATED under the measured-activity/relevance-unknown enzyme-specificity tier. Positive overnight KT2442 tributyrin chemistry is retained. Full PMID17170116 Fig6 directly resolves HO monomer/dimer products from HO-rich copolymer, now stated with strain and copolymer limitations in core evidence. The proposed broader depolymerase has GO0016788 as immediate genus. Historical NEW granule row remains unchanged and retired.

Exact evidence, before/after payload audit and source hashes: analysis/module_audits/bacterial_mcl_pha_synthesis_and_mobilization/review-followup/implementation/.

## 2026-11-07 — PR6194 second review follow-up

Clarify that the supported C8-specific GO0050527 inference and broader mcl-PHA proposal can coexist: broader substrate acceptance does not falsify the narrower reaction. Product-resolved LC-MS is attributed to PMID17170116 through its documented external full-text reading, not to PMID41055782. Exact strain/construct and pure-polymer limitations remain.


## 2026-11-08 — PR #6194 evidence and scope follow-up

Add an explicitly inferred depolymerase MF proposal with KT2442 biochemical and target-context limits. See review-followup-20261108 for the prior review and change receipt. Original source annotation payloads are unchanged; authored proposal code changes and new rows are explicit.


## 2026-11-11 — withhold exact cross-strain GO transfer

The authored GO:0050527 IC proposal is withdrawn: the evidence is a cross-strain biochemical inference, not inference from another annotation of the same protein. ISS would require a verified donor; no stable KT2442 pPAZ3 accession or complete sequence bridge has been established. Preserve the qualified broader intracellular mcl-PHA role through the existing proposed activity, and request the missing donor sequence explicitly. The 2007 methods identify the KT2442 construct, and the 2025 title does not override its KT2442 methods. All pre-audit source annotation rows remain intact.


## 2026-11-11 — consistent close-strain inference across aspects

The KT2442 derivative evidence supports qualified KT2440 core molecular function, process and location at the same confidence. Restore GO:0050527 in core_functions for the HO-rich substrate/product component; keep the broader mcl-PHA proposed function as additive coverage of aliphatic/aromatic substrates. Do not manufacture a donor accession, an experimental KT2440 annotation, or an accession-free ISS row. Full-text Table 1/methods were re-read at https://www.researchgate.net/publication/6630171_Biochemical_Evidence_That_phaZ_Gene_Encodes_a_Specific_Intracellular_Medium_Chain_Length_Polyhydroxyalkanoate_Depolymerase_in_Pseudomonas_putida_KT2442_CHARACTERIZATION_OF_A_PARADIGMATIC_ENZYME ; KT2442 is explicitly a derivative of KT2440, while pPAZ3 uses KT2442 DNA. The earlier reasoning that withheld only MF while accepting BP/CC was inconsistent and is superseded.


## 2026-11-11 — explicit target-specific molecular-function gap

Retain the supported GO:0050527 core inference and all existing annotation payloads/actions. The purified, product-resolved enzyme is KT2442-derived, so no KT2440 IDA row or accession-free ISS row is manufactured. The specific core now carries a BIOLOGY/CURATION MF_DARK gap for the unmeasured target-matched substrate/product profile and unresolved construct identity, with the positive close-strain evidence stated as its boundary. The broader proposed activity and immutable capacity fixtures remain unchanged. Restore three missing PAINT citations in PTHR43798 and correct the module gap that erroneously denied the retained core claim.
