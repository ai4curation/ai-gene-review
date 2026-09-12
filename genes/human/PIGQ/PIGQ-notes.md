# PIGQ (GPI1) review notes

UniProtKB: Q9BRB3. HGNC:14135. Synonym GPI1. Gene on chr16p13.3.

## Function (verified from primary literature + UniProt)

PIGQ (also GPI1 / PIG-Q) is a **non-catalytic subunit of the GPI-N-acetylglucosaminyltransferase (GPI-GnT) complex**, the multi-protein ER-membrane enzyme that catalyses the **first, committed step of GPI-anchor biosynthesis**: transfer of GlcNAc from UDP-GlcNAc to phosphatidylinositol (PI) → GlcNAc-PI. The catalytic subunit is PIGA; PIGQ is a required accessory/scaffolding subunit.

- UniProt FUNCTION: "Part of the glycosylphosphatidylinositol-N-acetylglucosaminyltransferase (GPI-GnT) complex that catalyzes the transfer of N-acetylglucosamine from UDP-N-acetylglucosamine to phosphatidylinositol and participates in the first step of GPI biosynthesis." [file:human/PIGQ/PIGQ-uniprot.txt]
- UniProt SUBUNIT: complex composed at least by PIGA, PIGC, PIGH, PIGP, PIGQ, PIGY and DPM2 (PMID:16162815, PMID:9463366). Interacts with PIGA, PIGH and PIGC (PMID:9463366).
- The GOA TSV carries **no catalytic MF term**. UniProt DR has GO:0017176 (phosphatidylinositol N-acetylglucosaminyltransferase activity) as IEA:Ensembl, but this is NOT in the GOA snapshot, and PIGQ is not the catalytic subunit — so no catalytic activity is asserted here.

### Complex membership / role
- [PMID:9463366 "four mammalian gene products form a protein complex in the endoplasmic reticulum membrane. ... The protein complex had GPI-GlcNAc transferase (GPI-GnT) activity in vitro"] — first defines the PIG-A/PIG-H/PIG-C/GPI1 complex; localises it to the ER membrane; GPI-GnT activity in vitro.
- [PMID:9729469 "allow conclusions about a specific function for Gpi1p in stabilizing the enzymic complex"] — Gpi1p/GPI1 role = stabilising the GPI-GnT enzymic complex; mammalian GPI1 rescues yeast gpi1 mutants (first step of GPI biosynthesis, conserved).
- [PMID:10944123 "GPI-GnT is a uniquely complex glycosyltransferase, consisting of at least four proteins, PIG-A, PIG-H, PIG-C and GPI1"; "PIG-P ... associates with PIG-A and GPI1"; "DPM2 ... associates with GPI-GnT through interactions with PIG-A, PIG-C and GPI1"] — GPI1 interacts with PIG-P and DPM2 within the complex (IPI partners DPM2 O94777, PIGA P37287).
- [PMID:16162815 "Biosynthesis of glycosylphosphatidylinositol (GPI) is initiated by an unusually complex GPI-N-acetylglucosaminyltransferase (GPI-GnT) consisting of at least six proteins. Here, we report that human GPI-GnT requires another component, termed PIG-Y ... A complex of six components was formed without PIG-Y."] — establishes 7-component complex incl. PIGQ; the "complex of six" (PIGA/PIGC/PIGH/PIGP/PIGQ/DPM2) forms without PIG-Y. Source of the IDA GPI-GnT-complex, ER-membrane, and GPI-anchor-biosynthesis annotations.

### Location
- ER membrane. PMID:9463366 (complex in ER membrane). UniProt SUBCELLULAR LOCATION: Membrane; multi-pass membrane protein (5 predicted TM helices, residues 278-497).
- Reactome R-HSA-162730: the GlcNAc-PI-forming reaction and its catalysing multimeric enzyme are "localized to the endoplasmic reticulum membrane".

## MF: protein binding (IPI) annotations
Five IPI GO:0005515 annotations from IntAct, all to physiological GPI-GnT partners:
- PMID:10944123 → DPM2 (O94777), PIGA (P37287)
- PMID:16162815 → PIGA (P37287)
- PMID:33961781 (BioPlex) → PIGH (Q14442)
- PMID:40205054 (multimodal cell maps) → PIGH (Q14442)
- PMID:9463366 → PIGA (P37287), PIGC (Q92535), PIGH (Q14442)
Bare "protein binding" is uninformative per curation policy; the biology is better captured by part_of GPI-GnT complex (GO:0000506). Per policy, do NOT REMOVE experimental IPIs whose full text is unverified — MARK_AS_OVER_ANNOTATED. Interactions with PIGA/PIGC/PIGH/PIGP/DPM2 are all with fellow complex subunits, corroborating complex membership.

## Disease
Biallelic PIGQ loss-of-function → **Multiple congenital anomalies-hypotonia-seizures syndrome 4 (MCAHS4; MIM:618548)**, an autosomal-recessive inherited GPI-deficiency disorder (GPIBD) = a developmental and epileptic encephalopathy: refractory neonatal seizures, severe global developmental delay, dysmorphism, skeletal/renal/ophthalmic anomalies; caused cellularly by defective GPI synthesis. Refs PMID:24463883, 25558065, 27513193, 31148362. (These are disease/phenotype refs, not in GOA; noted for description only.)

## Annotation review decisions (GOA has 15 rows)
- GO:0005783 endoplasmic reticulum (IBA, GO_REF:0000033, is_active_in) → ACCEPT (core location, phylo). ER is correct; ER membrane (below) is more specific.
- GO:0006506 GPI anchor biosynthetic process (IBA, GO_REF:0000033) → ACCEPT (core BP).
- GO:0006506 GPI anchor biosynthetic process (IEA, GO_REF:0000120; InterPro IPR007720 + UniPathway) → ACCEPT.
- GO:0016020 membrane (IEA, GO_REF:0000120; SubCell SL-0162) → MODIFY → GO:0005789 ER membrane (too general; specific ER-membrane localization is known).
- GO:0005515 protein binding ×5 (IPI) → MARK_AS_OVER_ANNOTATED (uninformative; partners are complex subunits; captured by GO:0000506).
- GO:0000506 GPI-GnT complex (IPI, PMID:16162815, ComplexPortal) → ACCEPT (core CC).
- GO:0005789 ER membrane (IDA, PMID:16162815, ComplexPortal) → ACCEPT (core location).
- GO:0000506 GPI-GnT complex (IDA, PMID:16162815, UniProt) → ACCEPT (core CC).
- GO:0006506 GPI anchor biosynthetic process (IDA, PMID:16162815) → ACCEPT (core BP).
- GO:0005789 ER membrane (TAS, Reactome R-HSA-162730) → ACCEPT.
- GO:0005975 carbohydrate metabolic process (TAS, PMID:9729469) → MODIFY → GO:0006506 (too general; the specific process is GPI anchor biosynthesis / GlcNAc-PI formation).

## core_functions
No catalytic MF in GOA → omit `function`; record BP via directly_involved_in GO:0006506, location GO:0005789 (ER membrane), complex GO:0000506 (GPI-GnT complex).
