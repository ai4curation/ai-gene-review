# PSEPK methionine-cycle source assessment

Reviewed 2026-11-07. The frozen UniProt/GOA/provider/publication files were not refreshed. Official JSON snapshots alongside this file record retrieval URLs.

## PP_2698: MesD versus folate-dependent MetE

PP_2698/Q88JF1 and Acinetobacter baylyi MesD/Q6F6Z8 share 295 identical residues across 346 global-alignment columns; both proteins contain 344 residues. The independently acquired UniProt records identify adjacent PP_2699/Q88JF0 as a MesX-family protein (InterPro IPR015004; Pfam PF08908). The frozen target has the catalytic Meth_synt_2 barrel, not the canonical N-terminal folate-binding barrel. Together, sequence similarity to the experimentally characterized MesD comparator and linked MesX support a MesD assignment. Single-barrel architecture alone would not distinguish MesA, MesB, MesC, split MetE and MesD. The exact alignment and input snapshots are retained here.

PMID33534785 full cache: ACIAD3523/Q6F6Z8 and ACIAD3524 were genetically required in Acinetobacter baylyi ADP1. The new native fitness experiments and cloned complementation used Sphingomonas koreensis DSMZ15582, not KT2440. Both mesD and mesX rescued E. coli Keio ΔmetE/ΔmetF aerobically; neither gene alone did. Anaerobic complementation failed. These results do not identify the methyl donor, establish direct oxygen incorporation, or demonstrate purified KT2440 catalysis.

Exact primary excerpts:

> Growth of either ΔmetE or ΔmetF strains was rescued when both mesD and mesX were provided on a plasmid, but not when mesD or mesX were provided individually

> Overall, we found that the functional residues for binding zinc and homocysteine were conserved in all four families of core methionine synthases.

The current GO0003871 definition requires a specific methylfolate substrate. GO0008172 specifies methyl transfer to sulfur without a methyl-donor requirement. This supports a bounded generalization of the inherited electronic annotation, not a new row or a new target assay.

## MetH and the other cycle enzymes

KT2440 MetH has a complete soluble four-module methyltransferase architecture and no annotated signal peptide or transmembrane segment; cytosolic activity is an inference, not a native localization measurement. The frozen record's PIRNR000381-supported FUNCTION/CATALYTIC ACTIVITY/DOMAIN statements, NCBIfam TIGR02082 and full domain complement are independent support for its catalytic role; neither submitted names nor GOA are evidence. Current QuickGO GO0071267 includes regeneration of methionine from derivatives, and GO0008705 has a part_of link to it. This is not restricted to methylthioadenosine salvage. MetH directly converts methylfolate into tetrahydrofolate, so its pteridine and tetrahydrofolate process annotations are chemically true. Homocysteine metabolism can be refined to the methionine cycle, a current descendant, without replacing that substrate process with a disconnected product term.

MetK and AhcY retain curated HAMAP/RuleBase-supported chemistry and cofactor assignments; these are conserved-role inferences, not purified KT2440 kinetics. AhcY-bound NAD participates in internal redox chemistry and is regenerated rather than consumed stoichiometrically. Reaction assignment does not establish measured net native flux or control of the SAM:SAH ratio. Soluble architecture plus curated cytoplasmic localization supports the cytosol inference for these enzymes.

## Access and PAINT limits

PMID33534785 is full text. Newly normal-fetched PMID12832615 is abstract-only; it supports the stated MetH reaction/module mechanism, not uninspected assay details or KT2440 localization. Existing OpenScientist reports for metH/metE were read but their partial-MetE/folate-donor interpretation is superseded by the primary MesD evidence. Real default Falcon attempts for metK and ahcY failed; no provider output was manufactured. All four PAINT-loss checks report target leaf absent; this is unavailable lineage evidence, not proof of no losses. No existing IBA annotation occurs in this four-gene slice.
