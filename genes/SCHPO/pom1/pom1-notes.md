# pom1 (SPAC2F7.03c, Q09690) review notes

S. pombe DYRK-family dual-specificity protein kinase. Forms polar cortical gradients from cell tips; spatial cell-end marker coupling cell geometry to mitotic entry timing (cell-size control) and division-plane positioning, plus polarized (bipolar) growth.

## Molecular function / catalysis
- DYRK / MNB-DYRK subfamily, CMGC group; kinase domain 699-995, ATP binding 705-713 + K728, active site D825. EC 2.7.12.1 (dual specificity). [UniProt Q09690]
- Dual-specificity: autophosphorylates on Tyr; phosphorylates substrates on Ser/Thr. [PMID:22174761 "DYRKs share a kinase domain capable of catalyzing autophosphorylation on tyrosine and exogenous phosphorylation on serine/threonine residues"]
- Pom1 kinase activity demonstrated; catalytic-domain point mutations cause asymmetry. [PMID:11230130 "Point mutations in the catalytic domain lead to asymmetry during both cell growth and division"]
- Direct in vitro phosphorylation of substrates. [PMID:25720772 "Purified Pom1 phosphorylated these cell polarity targets in vitro, confirming that they are direct substrates of Pom1 kinase activity"]
- Pom1 phosphorylates Cdr2 C-terminal domain reducing Cdr2-T166 activating phosphorylation by Ssp1. [PMID:24508166 "Pom1 phosophorylated the C-terminal domain of Cdr2, and this modification reduced Cdr2-T166 phosphorylation by Ssp1"]

## Cell-size control / mitotic entry (G2/M)
- Pom1 gradient measures cell length and controls mitotic entry; dose-dependent G2-M inhibitor; negatively regulates Cdr1/Cdr2 (Wee1 inhibitors). [PMID:19474792 "an intracellular gradient of the dual-specificity tyrosine-phosphorylation regulated kinase (DYRK) Pom1, which emanates from the ends of rod-shaped Schizosaccharomyces pombe cells, serves to measure cell length and control mitotic entry"; "Pom1 is also a dose-dependent G2-M inhibitor. Genetic analyses indicate that Pom1 negatively regulates Cdr1 and Cdr2"]
- Pom1 forms polar gradient, dose-dependent inhibitor of mitotic entry via Cdr2 pathway; as cells elongate Pom1 decreases at middle leading to mitotic entry. [PMID:19474789 "Pom1 forms a polar gradient extending from the cell ends towards the cell middle and acts as a dose-dependent inhibitor of mitotic entry, working through the Cdr2 pathway"]
- Distinct Pom1 thresholds set timing vs positioning of division; Pom1 inhibits Cdr2 for mitotic commitment independently of regulating its localization. [PMID:24316795 "Pom1 inhibits Cdr2 for mitotic commitment independently of regulating its localization or cortical levels"]
- Pom1 prevents activation of Cdr2 by CaMKK Ssp1. [PMID:24508166 "Pom1 acts to prevent activation of Cdr2 kinase activity by the CaMKK Ssp1"]
- Pom1 suppresses Wee1 node bursts in small cells. [PMID:29514920 "Size-dependent signaling was caused in part by the Cdr2 inhibitor Pom1, which suppressed Wee1 node bursts in small cells"]
- Caveat: pom1Δ and nif1Δ have WT size homeostasis -> Pom1 is not the direct cell-size sensor. [PMID:24047646 "Cells deleted for either of these 2 genes show wild-type size homeostasis ... This indicates that these genes do not have a critical role as direct cell size sensors"]

## Division plane positioning / Mid1 / cytokinesis
- pom1 mutants misplace/misorient septa -> asymmetric division. [PMID:9573052 "many cells misplace and/or misorient their septa, leading to asymmetric cell division"]
- Pom1 required for proper placement of Mid1p ring; acts in pathway distinct from Plo1/Mid1. [PMID:9852154 "Pom1p is required for proper placement of the Mid1p ring"]
- Pom1 kinase prevents septation at cell tips even without Mid1; phosphorylates F-BAR Cdc15 to disrupt membrane/paxillin binding -> ensures medial division. [PMID:32101481 "Pom1's kinase activity prevents septation at cell tips even if Mid1 is absent or mislocalized"; "inhibition of Cdc15-scaffolded septum formation at cell poles is a key Pom1 mechanism that ensures medial division"]
- Multiple polarity kinases (incl. Pom1) phosphorylate Cdc15 IDR, inhibit phase separation/condensation, antagonize CR assembly. [PMID:36749320 "a threshold of Cdc15 phosphorylation by assorted kinases prevents Cdc15 condensation on the PM and antagonizes CR assembly"]
- Pom1 localizes at cortex of cell tip during cytokinesis; contributes to preventing tip septation. [PMID:37746062 "preventing tip septation in Schizosaccharomyces pombe"]
- Pom1 detected in contractile ring intermediate layer (super-res map). [PMID:28914606 "An intermediate layer (80-160 nm) consists of a network of cytokinesis accessory proteins as well as multiple signaling components which influence cell division"]

## Polarized / bipolar growth (NETO), Cdc42, Rga4
- pom1 provides positional info for both growth and division; mutants fail to switch to bipolar growth. [PMID:9573052 "most cells never switch to bipolar growth but instead grow exclusively at the randomly chosen end"]
- Pom1 interacts with Rga4 (Cdc42 GAP); needed to remove Rga4 from nongrowing end -> bipolar GTP-Cdc42. [PMID:18328707 "Pom1 kinase physically interacts with Rga4"; "Pom1 kinase recruited to cell ends ... is essential for proper localization of a GAP for Cdc42, Rga4, which ensures bipolar localization of GTP-bound, active Cdc42"; deltapom1 brings about monopolar growth]
- Tea1-Tea4-Pom1 axis counteracts inappropriate Gef1 activity by regulating Rga4 localization. [PMID:29930085 "Microtubules and the Tea1-Tea4-Pom1 axis counteract inappropriate Gef1 activity by regulating the localization of the Cdc42 GTPase-activating protein Rga4"]
- Pom1 contributes to cell-end determination; pom1Δ has defective growth pattern/actin relocalization. [PMID:14663827 "Pom1Delta, in combination with Tea1Delta or Tea3Delta, has the greatest difficulty in relocalizing actin to the cell ends following actin depolymerization and generates the most defective growth pattern"]

## Cell integrity MAPK (Pmk1)
- Pom1 is a negative regulator of the Pmk1 (cell integrity) pathway, via regulating Rga4 localization/phosphorylation (not via Rga4 Rho2-GAP). [PMID:20164182 "The DYRK-type protein kinase Pom1, which regulates both the localization and phosphorylation state of Rga4, is also a negative regulator of the Pmk1 pathway"]

## Localization / gradient mechanism
- Cell tip / cell cortex of cell tip / site of polarized growth / cell division site. [PMID:11230130; PMID:9573052; PMID:24047646]
- Tea4 recruits Pom1 to cortex; Pom1 binds PM via basic region (direct lipid interaction), diffuses laterally, autophosphorylates to release. [PMID:21703453 "Pom1 then moves laterally at the plasma membrane, which it binds through a basic region exhibiting direct lipid interaction. Pom1 autophosphorylates in this region to lower lipid affinity and promote membrane release"]
- Interacts with Tea4; triggers PM association via Dis2-dependent dephosphorylation. [PMID:21703453 "Tea4 triggers Pom1 plasma membrane association by promoting its dephosphorylation through the protein phosphatase 1 Dis2"]
- PIP binding: Pom1 binds plasma membrane lipids via basic region (phosphatidylinositol phosphate binding, IDA). [PMID:21703453, "direct lipid interaction"]
- Intermolecular autophosphorylation buffers gradient robustness. [PMID:26150232 "Pom1 auto-phosphorylates intermolecularly, both in vitro and in vivo, which confers robustness to the gradient"]
- Under glucose limitation Pom1 re-localizes to cell sides (lateral cell cortex) via MT destabilization/PKA-CLASP. [PMID:26443240 "Pom1 re-localizes to cell sides upon environmental glucose limitation, where it strongly delays mitosis"]

## Notes on specific annotations
- GO:0005515 protein binding (IPI to cdr2, tea4, rga4): uninformative MF; the underlying interactions are real but better captured by kinase MF + specific BP. Mark over-annotated / non-core.
- GO:0005856 cytoskeleton (IBA): Pom1 is cortical/PM, not a cytoskeletal component; over-annotation from phylo.
- GO:0005737 cytoplasm (IBA): broad; Pom1 acts at cortex/PM. Keep non-core.
- PMID:12206652 (Mac1) and PMID:20870879 (invasive filaments) and PMID:22174761 (Pom2): pom1 localization references, supportive of cell tip/division site CC.
- PMID:11950884 not cached locally; cell tip localization corroborated by many other refs.
