# EARS2 evidence notes

## Mitochondrial tRNA charging

EARS2 uses ATP to attach glutamate to both mitochondrial tRNA-Glu and mitochondrial tRNA-Gln. The two substrates therefore lead to different charged-tRNA products. Glutamyl-tRNA-Glu supplies glutamate for mitochondrial protein synthesis. Glutamyl-tRNA-Gln instead requires the separate GatCAB amidotransferase to convert its tRNA-bound glutamate to glutamine; EARS2 does not catalyze that amidation (PMID:19805282).

The direct enzyme experiments used transit-sequence-deleted, His-tagged human EARS2 expressed in bacteria with native bovine and human placental mitochondrial tRNAs. In a separate reconstitution, human GatCAB converted the mischarged intermediate: [PMID:19805282 "Gln-tRNA Gln was clearly formed in the presence of hGatCAB"]. The associated HeLa knockdown experiments targeted GatCAB subunits, not EARS2. Full-length human EARS2 with a C-terminal EGFP tag was used separately to assess mitochondrial targeting (PMID:19805282).

## Localization and mitochondrial proteomics

Matrix localization is supported by the curated experimental EXP/ECO:0000269 assertion and the UniProt SL-0170 mapping. The available main text of PMID:19805282 establishes mitochondrial targeting. Its detailed supplementary Methods were unavailable, and the specific matrix assay was not independently reconstructed. This access limit is not negative evidence against the curator's positive finding. The broad mitochondrial annotations are refined using that target-level matrix support; the whole-organelle measurements are not described as matrix-specific assays.

Human MitoCoP proteomics identifies EARS2 group 6714 in Table S1(A), row 333, and S1(B), row 301. The group contains Q5JPH6, H3BTB7 and Q5JPH6-2 and has measured mitochondrial enrichment, spatial clustering and import dependence. These are not separate measurements of each natural product. The matrix GO flag imports prior annotation. The peripheral carbonate/sonication category is operational: approximately 86.43% membrane-associated and 18.01% integral. It does not identify a membrane face or exclude matrix-side association (PMID:34800366).

## Conserved chemistry and unresolved zinc binding

The [reproducible analysis](EARS2-bioinformatics/RESULTS.md) reconstructs all three PAINT IBD joins on the exact 523-residue target lineage. Donor records retain their evidence codes, and the target's own experimental annotation is legitimate grounding for its inherited annotation. Rhea 23540 and 64612 distinguish the two tRNA substrates; 18397 is the broader Glx reaction. ARBA00026962 outputs mitochondrion, although its precise current FunFam trigger was not independently reconstructed. That trace limit does not overturn separate target evidence. Each GO_REF is assessed as a methodological reference with LOW biological relevance rather than a primary experiment.

The zinc-binding inference comes from an IPR033910 match. In the family alignment, E. coli Zn ligands C98/C100/C125/H127 correspond to human C140/C142/C167/N169. Three cysteines are retained and the fourth site differs. Neither this correspondence nor the absence of a target metal feature establishes loss of binding. No direct human occupancy measurement was recovered, so zinc binding remains unresolved and is not included in the core activities.

## Natural products and disease context

The two UniProt products have 523 and 534 residues and differ at the C terminus. The NP_001077083.1 reference parent named in the biochemical study exactly matches Q5JPH6-1, but sequencing of the complete expressed insert is not established. Shared upstream sequence does not prove equivalent natural-product activity or localization.

Biallelic EARS2 variants are associated with infantile leukoencephalopathy involving the thalamus and brainstem and elevated lactate, with differing disease severity. The clinical abstract supports this disease context, not an additional mechanistic pathway or tissue-development annotation (PMID:22492562).

## Annotation choices and evidence access

The 2026-10-18 review preserves all 22 imported source records: ten ACCEPT, eleven MODIFY and one UNDECIDED zinc-binding annotation. The two catalytic activities are represented separately, with a shared mitochondrial tRNA-charging process. Broad nucleotide binding is refined to ATP binding. Current GO marks glutamyl-tRNA aminoacylation GO:0006424 obsolete; its three imported IDs remain intact, with GO:0070127 proposed in their reviews. This ontology change does not contradict the biochemical observations. No new process assertion is inferred from disease necessity.

The assessment uses the main Results, Discussion and Methods of PMID:19805282, selected mitochondrial-proteomics Methods and source tables from PMID:34800366, and the clinical abstract of PMID:22492562. Detailed supplementary Methods for PMID:19805282 and full clinical Methods/Results for PMID:22492562 were unavailable. Figures were not independently assessed. The [source evidence guide](EARS2-source-evidence.yaml) distinguishes primary assays, curated assertions and calculations from the underlying records. The short excerpts in the review and these notes each occur once; other source descriptions are paraphrases.

Automated literature research through Falcon and Perplexity-lite failed because authentication was denied and the quota was exhausted, respectively. The assessment therefore uses manual examination of the cited sources and the reproducible analysis. The downloaded publication and database records are retained without alteration.
