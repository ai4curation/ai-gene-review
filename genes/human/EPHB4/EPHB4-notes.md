# EPHB4 (P54760) — curation notes

Deep-research providers are unavailable in this environment; research is from the cached
publications, the UniProt record and PubMed.

## Protein

Single-pass type I receptor tyrosine kinase. Signal peptide 1-15, extracellular
topological domain 16-539 (ligand-binding domain, cysteine-rich region, two fibronectin
type III repeats), transmembrane 540-560, cytoplasmic 561-987 with kinase and SAM
domains and active site at 740. The ligand-binding face is extracellular and
surface-accessible.
[file:human/EPHB4/EPHB4-uniprot.txt "SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|PubMed:28687708, ECO:0000269|PubMed:8188704}; Single-pass type I membrane protein"]

## Function

- Highly selective receptor for ephrin-B2; crystal structure of the complex solved.
  [PMID:16867992 "we determined the crystal structure of the ligand binding domain of EphB4 in complex with the extracellular domain of ephrinB2"]
- Forward signalling drives endothelial repulsion and segregation.
  [PMID:12734395 "EphrinB2-mediated repulsive signals are transduced by EphB4"]
  [PMID:12734395 "In turn, soluble EphB4-Fc is pro-adhesive and stimulates EC migration and sprouting angiogenesis."]
- Active kinase: autophosphorylates and phosphorylates the pseudokinase EPHB6.
  [PMID:8188704 "Purified in vitro translated Htk was enzymatically active and autophosphorylated on tyrosine in kinase assays."]
- Human genetics: loss of function causes CM-AVM2 and contributes to vein of Galen
  malformation.
  [PMID:28687708 "Germline Loss-of-Function Mutations in EPHB4 Cause a Second Form of Capillary Malformation-Arteriovenous Malformation (CM-AVM2) Deregulating RAS-MAPK Signaling."]
  [PMID:30578106 "Other VOGM probands harbored rare inherited damaging mutations in Ephrin signaling genes, including a genome-wide significant mutation burden in EPHB4."]
- Context-dependent RAS-ERK output.
  [PMID:22555806 "its activation resulted in inhibition of the Ras/ERK pathway in endothelial cells but activation of the same pathway in MCF-7 breast cancer cells"]

## Review decisions

Localization conclusion: plasma membrane, ectodomain extracellular and
antibody-accessible (agonistic ectodomain antibodies activate the receptor). The 36
plasma-membrane rows, including 31 Reactome reactions, were accepted. The Reactome
extracellular-region and cytosol rows were kept as non-core because they describe the
MMP-shed ectodomain and the gamma-secretase-released intracellular fragment.

Of ten bare protein-binding rows, the six ephrin-B2 rows were modified to ephrin
receptor activity, and the EPO, RASA1, EPHA5, EPHA6 and EPHA7 rows were removed as
uninformative (five rows; the RASA1 interaction is not disputed). `protein kinase
activity` and `protein tyrosine kinase activity` were marked TOO_GENERAL beside the
accepted transmembrane receptor protein tyrosine kinase activity. Heart morphogenesis
(mouse-derived) was kept as non-core.
