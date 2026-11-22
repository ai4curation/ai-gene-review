# ASTN1 notes

## 2026-10-05 review (PAINT, affinage)

- Astrotactin is a neuronal ligand for glial-guided migration [PMID:8602532 "Transfection of astrotactin complementary DNA into 3T3 cells indicated that astrotactin acts as a ligand for neuron-glia binding during neuronal migration."].
- Astn1-null mice [PMID:11861479 "In vitro and in vivo cerebellar granule cell assays show a decrease in neuron-glial binding, a reduction in migration rates and abnormal development of Purkinje cells."].
- ASTN2 sets ASTN1 surface level, and endocytic trafficking releases adhesions [PMID:20573900 "Together, these findings suggest that ASTN2 regulates the levels of ASTN1 in the plasma membrane and that the release of neuronal adhesions to the glial fiber during neuronal locomotion involves the intracellular trafficking of ASTN1."].
- Human disease [PMID:41544630 "Here, we describe eighteen individuals with NDDs from twelve unrelated families with bi-allelic, ultra-rare, predicted damaging variants in ASTN1 and one individual with heterozygous variants in both ASTN1 and ASTN2 ."].
- Every GOA row is IBA or IEA, derived from mouse Astn1 experiments. All are accepted, except clathrin-coated vesicle and perikaryon, which are kept as non-core.
- GO:0007158 neuron cell-cell adhesion is defined as attachment of a neuron to "another cell", so neuron-glia binding fits.
- No MF term is proposed: the glial counter-receptor is unknown. This is recorded as an MF_DARK knowledge gap.
- Not used: the affinage-listed miR-sc3 nerve-injury (PMID:26786955) and liver-cancer overexpression (PMID:32945491) papers.

## 2026-10-05 revision (reviewer round 1)

- Added NEW GO:0098632 cell-cell adhesion mediator activity (ISO from mouse) and set it as the core MF. The 3T3 gain-of-function and knockout loss-of-binding data support the activity without the counter-receptor being known. The knowledge gap is narrowed to the counter-receptor, and its dark_aspect was dropped. GOA has no MF row for ASTN1.
- Both endosome rows (IBA is_active_in and IEA) are now non-core, consistent with the clathrin-coated vesicle row. Endosomes are trafficking compartments, and the adhesion activity is at the surface.
- PMID:20573900 was re-fetched with full text (PMC2905051). Quotes now come from its Results: RhoB-positive endosomes, clathrin light chain colocalization, and C-terminus exposure on the cell surface. The C-terminus result supports external side of plasma membrane.
- The 1996 abstract says "two fibronectin type III repeats"; current UniProt annotates one FN3 domain (1030-1145), and the description follows UniProt.
- BP specificity: GO:0021932 hindbrain radial glia guided cell migration fits the cerebellar evidence. ASTN1 is also expressed in cortex, hippocampus and olfactory bulb, and human variants cause cortical malformations, so the general neuron migration term is kept.
