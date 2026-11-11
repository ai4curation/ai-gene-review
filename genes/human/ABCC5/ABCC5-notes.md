# ABCC5 (MRP5) curation notes

UniProt: O15440 (MRP5_HUMAN). Gene: ABCC5 (HGNC:56), synonym MRP5; also historically
MOAT-C, SMRP, pABC11. Taxon: Homo sapiens (NCBITaxon:9606). 1437 aa, EC 7.6.2.2 / 7.6.2.-.

## Summary of function

ABCC5/MRP5 is a plasma-membrane ATP-binding-cassette (ABC) efflux transporter of the
ABCC/MRP ("multispecific organic anion transporter") subfamily. It is a primary active
transporter: two nucleotide-binding domains hydrolyse ATP to pump substrates out of the
cytosol against a concentration gradient. Its characterized substrates are predominantly
small organic anions, particularly:

- **Cyclic nucleotides**: 3',5'-cyclic GMP and 3',5'-cyclic AMP. First described as an
  "ATP-dependent export pump for cyclic nucleotides" [PMID:10893247 "Thus, cyclic nucleotides
  are physiological substrates for MRP5"]; cGMP K_m 2.1 µM, cAMP K_m 379 µM in vesicles
  [PMID:10893247]. Other labs found much lower affinity from intact cells and concluded MRP5
  is a low-affinity "overflow" cyclic-nucleotide pump [PMID:12637526 "MRP4 and MRP5 are low
  affinity cyclic nucleotide transporters"; PMID:12695538]. UniProt flags this caution
  (MISCELLANEOUS). The activity is genuine and reproducible; its quantitative physiological
  weight is debated.
- **Nucleotide/nucleoside-monophosphate analog drugs**: confers resistance to thiopurines
  (6-MP → thioinosine monophosphate tIMP, thioxanthosine monophosphate) and the acyclic
  nucleoside phosphonate PMEA [PMID:10840050 "MRP5 is a multispecific organic anion pump able
  to transport nucleotide analogs"; PMID:12435799 "all major thiopurine monophosphates...are
  transported by MRP4 and MRP5"; PMID:12695538].
- **Glutathione and GSH conjugates**: transports DNP-GS and GSH basolaterally in MDCKII cells
  [PMID:10840050 "transport of DNP-GS to the basal compartment"].
- **Folates / antifolates**: transports folic acid and methotrexate (MTX), KM ~1 mM; confers
  antifolate resistance [PMID:15899835 "MRP5/ABCC5 is also an antifolate and folate exporter"].
- **Glutamate conjugates / N-acetylated amino-acid derivatives**: NAAG, N-acetylaspartate,
  N-lactoyl-amino acids, beta-citrylglutamate, kainate, domoate (UniProt CATALYTIC ACTIVITY,
  PMID:26515061, PMID:25964343 — not in the GOA set under review but corroborates the
  "broad glutamate-conjugate / organic-anion exporter" picture).

A distinct, evolutionarily conserved role is **heme export**: MRP-5/ABCC5 acts as a heme
exporter translocating cytosolic heme toward the secretory pathway; mrp-5 is essential for
C. elegans development and zebrafish hemoglobinization [PMID:24836561 "the multidrug resistance
protein MRP-5/ABCC5 likely acts as a heme exporter"; "MRP5 resides on the plasma membrane and
endosomal compartments and regulates export of cytosolic heme"; "targeted depletion of mrp-5 in
the intestine causes embryonic lethality"]. This explains the endosome-membrane and Golgi
localizations.

## Localization

UniProt: basolateral cell membrane; apical cell membrane; Golgi apparatus lumen; endosome
membrane; cytoplasmic granule (by similarity). "In most cells, routes to the basolateral plasma
membrane, but in the brain capillary endothelial cells that form the blood-brain barrier,
resides in the apical membrane" (UniProt SUBCELLULAR LOCATION note; PMID:15501592, PMID:24836561).

- Basolateral in polarized MDCKII [PMID:10840050 "MRP5 is routed to the basolateral membrane"].
- Apical/luminal in human brain capillary endothelium, plus pyramidal neurons [PMID:15501592
  "...localized by confocal laser scanning microscopy to the luminal side of brain capillary
  endothelial cells"; "MRP5 protein was present in pyramidal neurons"].
- RPE: present on both apical and basolateral surfaces of human fetal RPE [PMID:28112518;
  PMID:31791063 "Most drug transporters showed similar abundance on both RPE surfaces"].
- Rat BBB study found Mrp5 NOT on the microvessel luminal surface, but in ependymal cells
  [PMID:18619525 "...Mrp5 (Abcc5) were not detected on the luminal surface using either method";
  "Mrp5...detected in the ependymal cells lining the ventricle"]. Localization is thus
  context/species dependent; the shared truth is plasma-membrane residence.

Structure: multi-pass membrane protein, 13 TM helices (UniProt FT), two ABC transmembrane
domains + two NBDs with Walker A/B ATP-binding motifs [PMID:9325169 "...had two ABCs with walker
A and B motifs"]. Cryo-EM structures: PDB 8KCI, 8WI0-8WI5. PANTHER PTHR24223:SF196.

## Points affecting the review

- **Hyaluronan**: HA export by ABCC5 rests on a single-lab inhibitor study [PMID:15345330] and
  mouse ortholog propagation; it is contested — HA synthases (HAS1/2/3) are now thought to
  extrude their own product, and Reactome itself hedges [Reactome:R-HSA-2142859 "there is
  evidence that silencing of the ABC transporter C5 (ABCC5)...affects HA export" but "HA is
  produced by HA synthases (HAS) 1,2,3 in a combined process of synthesis and membrane
  translocation"]. The two `GO:0030213 hyaluronan biosynthetic process` rows are marked
  MARK_AS_OVER_ANNOTATED (a pure transporter does no biosynthesis); the HA-transport term
  `GO:1901264 carbohydrate derivative transport` (Reactome TAS) is kept KEEP_AS_NON_CORE.
- **Generic membrane rows** (`GO:0016020`) are MODIFIED to `GO:0005886 plasma membrane` per
  the ABC-transporter surfaceome convention. `GO:0016020` IDA cites PMID:15297306 whose title
  foregrounds MRP4/ABCC4; per the don't-overrule rule this is treated as a generic→specific
  refinement, not a mis-attribution.
- **General transporter-activity terms** entailed by the specific accepted activities are
  marked TOO_GENERAL: `GO:0140359 ABC-type transporter activity`, `GO:0042626 ATPase-coupled
  transmembrane transporter activity`, `GO:0022857 transmembrane transporter activity`,
  and the BP root `GO:0055085 transmembrane transport`. Ontology ancestry confirmed via OLS
  (GO:0008559 and GO:1905948 are descendants of GO:0140359 → GO:0042626 → GO:0022857).
- **Blood-brain-barrier** (`GO:0150104`, NAS) is KEEP_AS_NON_CORE: the two NAS references
  (PMID:26590417, PMID:30280653) are general BBB reviews that do not mention ABCC5, but ABCC5's
  luminal localization in human brain capillary endothelium (PMID:15501592) supports a role.
- All catalytic activity is transport; ABCC5 performs no biosynthetic chemistry, so metabolic/
  biosynthetic process terms (`GO:0006805 xenobiotic metabolic process`) are refined to the
  matching transport term the gene carries (`GO:0042908 xenobiotic transport`).
