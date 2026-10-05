# AURKA notes

## 2026-10-05 review (PAINT, affinage)

- 154 GOA rows, reviewed with a rule-based builder (term → action) and quotes mainly from the extensively curated UniProt entry, plus row-specific papers.
- Core: S/T kinase activity, centrosome and spindle pole, mitotic spindle organization, centrosome separation and cycle, cilium disassembly at the basal body [PMID:17604723].
- Over-annotated: chromosome passenger complex (IBA, an Aurora-B complex); response to wounding and liver regeneration (transgenic overexpression phenotypes, PMID:19435814); protein heterodimerization (the GADD45A NMR contact).
- MODIFY: protein S/T/Y kinase activity → S/T (no tyrosine activity reported). UNDECIDED: molecular function activator activity (EXP, a structure paper).
- Non-core: Aurora-B-type IBA rows (kinetochore, spindle midzone, regulation of cytokinesis), nuclear and perinuclear pools, basolateral and neuron projection (by similarity), and substrate-level outputs (HURP stability, Kif18b-MCAK, FOXP1/FBXL7, RALA mitochondrial fission, p53).
- 50 GO:0005515 IPIs: the PLK1 row becomes protein kinase binding; the rest are removed (TPX2, BORA, MYCN and others).
- PMID:23792191 (a GOA IPI source, N-Myc degradation by Aurora-A inhibitors) has an erratum; it is not quoted here.

## 2026-10-05 revision (reviewer round 1)

- Row-level evidence: each row's own cached reference is now quoted, e.g. [PMID:18615013 "Here we show that in human cells PLK1 activation occurs several hours before entry into mitosis, and requires aurora A (AURKA, also known as STK6)-dependent phosphorylation of Thr 210."].
- The meiotic rows are kept as non-core on mouse oocyte evidence [PMID:31895686 "Taken together, our current data reveal a critical role for AURKA activity in regulating microtubule dynamics, spindle pole focusing, and the maintenance of oocyte aMTOC organization at assembled meiotic spindles."].
- Cytosol is now non-core and centriole is accepted. The nuclear pool has a kinase-independent hnRNP K/MYC role (PMID:26782714).
- The IKBKB and MYCN IPIs stay removed: N-Myc stabilization is carried by GO:0031647.
