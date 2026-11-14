# SSTR2 notes

Deep research (`just deep-research-falcon human SSTR2 --fallback perplexity-lite`) failed in this
environment (no provider API keys: "Provider 'perplexity' not available"). Notes below are
compiled directly from the UniProt record (P30874) and cached publications.

## Identity and topology
- Somatostatin receptor type 2, class A rhodopsin-like GPCR, 7 TM helices; N-terminus extracellular
  (UniProt TOPO_DOM 1..43 Extracellular), C-terminal tail cytoplasmic.
- UniProt: "Cell membrane; Multi-pass membrane protein. Cytoplasm. Note=Located mainly at the cell
  surface under basal conditions. Agonist stimulation results in internalization to the cytoplasm."
  The "cytoplasm" refers to internalized (endocytic vesicle) receptor, not a soluble pool.
- [PMID:22651821 "in basal conditions, SSTR2 and SSTR3 colocalize at the plasma membrane"]; agonist
  reduces cell-surface pool with increased intracellular colocalization.
- [PMID:18653781 "Activation of SSTR2 results in the recruitment and stable association of beta-arrestin, followed by receptor internalization and intracellular receptor pooling"]

## Function
- UniProt FUNCTION (ECO:0000269): "Receptor for somatostatin-14 and -28. This receptor is coupled via
  pertussis toxin sensitive G proteins to inhibition of adenylyl cyclase."
- [PMID:7914078 "somatostatin-14 inhibits the adenylyl cyclase in a dose dependent and pertussis toxin-sensitive manner when human SSTR2 is co-expressed with Gi alpha 1 in CHO cells"]
- Reactome R-HSA-374758: the 5 SSTRs "couple with pertussis toxin-sensitive G proteins to inhibit adenylate cyclase after ligand binding".
- Antiproliferative (cytostatic) signaling: [PMID:9892014] SSTR1,2,4,5 induce Rb hypophosphorylation and G1 arrest; efficacy hSSTR5 > hSSTR2.
- PI3K inhibition: [PMID:16917505 "Somatostatin, acting through sst2, inhibits PI3K activity by disrupting a pre-existing complex comprising the sst2 receptor and the p85 PI3K regulatory subunit"] (pY71 in ICL1 binds p85 C-SH2).
- Heterodimers with SSTR5 (PMID:18653781) and SSTR3 (PMID:22651821); C-terminal PDZ ligand binds SHANK1 (SSTRIP) PDZ domain (PMID:10551867).
- Clinical: principal target of octreotide/lanreotide and of SSTR-targeted PET imaging/PRRT in neuroendocrine tumours (general knowledge; not used as evidence for annotations).

## Localization conclusion
Plasma membrane, 7TM with extracellular N-terminus and ECLs exposed at cell surface; agonist-induced
endocytosis to intracellular vesicles. Cytosol (HPA IF) is not credible for a multi-pass receptor.
