# CF-9 (Q40235) curation notes

Solanum pimpinellifolium Cf-9 (Hcr9-9C), receptor-like protein recognising the
Fulvia fulva (Cladosporium fulvum) effector AVR9 (partner of genes/FULFL/AVR9).

## Sources used
- UniProt Q40235, GOA (10 rows), CF-9-deep-research-falcon.md, cached PMIDs.
- Newly cached: PMID:10758503, 11226184, 26765243, 15131698 (retracted), 31310343 (retraction notice).

## Key findings
- Gene identity and resistance: [PMID:7973631 "The tomato Cf-9 gene confers resistance to infection by races of the fungus Cladosporium fulvum that carry the avirulence gene Avr9."]
- Plasma membrane, glycosylated: [PMID:10758503 "c-myc : Cf-9 was enriched in these fractions, indicating that Cf-9 is a plasma membrane protein."]
- Specificity in central LRRs: [PMID:11226184 "Therefore, important sequence determinants of Cf-9 function are located in LRRs 10 to 18."]
- Ectodomain structure-function (66 mutants): [PMID:15722474 "A total of 66 site-directed mutants of Cf-9 were analyzed for activity in Avr9 recognition and for protein stability"]
- Cytosolic tail: [PMID:26315781 "the membrane-proximal region of the cytosolic domain of Cf-9 plays an important role in Cf-9-mediated necrosis"]
- Co-receptor: [PMID:26765243 "after elicitation with matching effector ligands Avr4 and Avr9, BRI1-ASSOCIATED KINASE 1/SOMATIC EMBRYOGENESIS RECEPTOR KINASE 3 (BAK1/SERK3) associates with Cf-4 and Cf-9."] SOBIR1 association data (PMID:23716655) were mainly shown for Cf-4/Ve1; not asserted for Cf-9 here.
- Direct binding unresolved: [PMID:12239406 "Binding kinetics and binding capacity were similar for membranes of the MM-Cf0 and MM-Cf9 genotypes."]
- Natural variation: [PMID:11517316 "All AVR9-responsive plants contained either Cf-9 or 9DC"]

## CITRX caution
The IPI protein-binding row (CITRX, Q9LKW0; PMID:26315781, Y2H) traces back to
PMID:15131698, retracted 2019: [PMID:31310343 "the thioredoxin that interacts in yeast 2-hybrid with the Cf-9 C-terminus is in fact localized in the chloroplast, rendering a role in Cf-9 signalling unlikely"].
The falcon deep-research file still presents CITRX as a negative regulator; disregarded.

## Decisions
- protein binding (IPI) -> REMOVE (uninformative; partner chloroplastic).
- defense response to fungus x7 -> ACCEPT (Cf-9 is the receptor initiating the defence; participation, not just necessity).
- plasma membrane IEA -> ACCEPT. response to molecule of fungal origin IEP -> KEEP_AS_NON_CORE.
- NEW: GO:0140376 innate immune receptor activity and GO:0002768 immune response-regulating
  cell surface receptor signaling pathway. Comparator: Cf-4 (O50025) carries both in GOA (EXP).
  GO:0140376 chosen over pattern recognition receptor activity / binding terms because
  AVR9 is a race-specific effector, not a PAMP, and direct binding is unproven.

## Project curation question 3 (necessity vs participation)
Unlike MLO/PEN-type genes, Cf-9's defence-to-fungus rows are justified: the protein
performs the perception step. The mechanistic term (cell-surface receptor signalling)
was added as NEW and placed in core_functions.
