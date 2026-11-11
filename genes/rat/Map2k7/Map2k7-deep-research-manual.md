# Map2k7 (rat, UniProt Q4KSH7) - manual literature synthesis

No deep-research API was available; this synthesis was compiled by hand from cached
publications in `publications/` and the UniProt record. Provenance is inline.

## Identity

- Rat Map2k7 (RGD:1560043, GeneID 363855), Swiss-Prot Q4KSH7 (MP2K7_RAT), 419 aa.
- UniProt: "Belongs to the protein kinase superfamily. STE Ser/Thr protein kinase family. MAP kinase kinase subfamily."
- Domains (UniProt CC:DOMAIN): N-terminal D domain (residues 37-57) "required for the binding to MAPK substrates";
  C-terminal DVD domain (377-400) that binds upstream MAP3Ks.
- PTM: "Activated by phosphorylation on Ser-271 and Thr-275 by MAP kinase kinase kinases (MAP3Ks)" (UniProt, citing PMID:14575811).

## Molecular function: JNK-specific MAP2K

- Mouse MKK7 cloning: "MKK7 specifically activated stress-activated protein kinases (SAPKs)/c-Jun N-terminal protein
  kinases (JNKs) but not extracellular-regulated kinase or p38 kinase" [PMID:9405446].
- "In vitro protein kinase assays demonstrate that MKK7 phosphorylates and activates JNK, but not the p38 or
  extracellular signal-regulated kinase groups of MAP kinase" [PMID:9207092].
- Residue preference: "JNK is phosphorylated preferentially on Tyr by MKK4 and on Thr by MKK7" [PMID:11390361].
- Substrate docking: "MKK7 contains three JNK-docking sites that interact to selectively bind JNK and contribute to JNK
  signal transmission and specificity" [PMID:16533805].
- Isoforms and location: "these MKK7 isoforms are detected in both cytoplasmic and nuclear compartments of cultured cells.
  The presence of MKK7 in the nucleus was not, however, required for JNK activation in vivo" [PMID:9891090].

## Biological roles

- Cytokine vs stress: "disruption of the Mkk7 gene alone was sufficient to prevent JNK activation caused by
  proinflammatory cytokines" [PMID:11390361]; dominant-negative MKK7 "inhibits interleukin-1beta, lipopolysaccharide,
  and MEKK1-induced SAPK/JNK activation" [PMID:9405446].
- Stress activation (human): "MKK7 was also activated when cells were exposed to heat, UV irradiation, anisomycin,
  hyperosmolarity or the pro-inflammatory cytokine tumor necrosis factor-alpha" [PMID:9535930].

## Rat-specific experimental work

- PC12 / SCLC transfectants: "osmotic stress stimulated both HA-MKK4 and HA-MKK7", whereas UV stimulated only HA-MKK4
  in SCLC cells [PMID:10051439] (abstract only).
- Cerebellar granule neurons, low-potassium apoptosis: "MKK7, but not MKK4, was activated within the first 4-6 h";
  "These data suggest that MKK7 is responsible for activating the JNK pathway during LK-induced CGN apoptosis"
  [PMID:11849756] (abstract only).
- Hippocampal CA1 after global ischaemia: phospho-MKK7 rises 1-5 days; "the interaction of MLK3, ASK1 and phospho-JNK
  with MKK7 was increased compared with sham control, as shown by coimmunoprecipitation experiments" [PMID:14575811];
  K252a inhibits the "MLK3/MKK7/JNK3 cascade" [PMID:15680699]; estrogen/Akt1 inhibits the "MLK3-MKK4/7-JNK1/2 pathway"
  [PMID:17064355] (all abstract only).
- PC12 neurite regrowth: "the ERK1/2 kinase MEK1 and the JNK kinase MKK7 bind to MEKK1 in a competing fashion"
  [PMID:16006144] (abstract only).
- POSH scaffold: POSH-induced neuronal apoptosis "is suppressed by dominant-negative forms of MLKs, MKK4/7 and c-Jun"
  [PMID:12514131] (full text).
- Perfused rat heart (full text): endogenous MKK7 immune-complex kinase assays with GST-JNK and GST-c-Jun as substrates;
  "In control experiments in which hearts were perfused with sorbitol, we saw robust activation of all MKK isoforms
  assayed"; during ischaemia "There was no significant activation of either MKK4 or MKK7" [PMID:20550965].
- Mouse neurons: "some MKK7/MAP2K7-deficient facial motoneurons were resistant to axotomy-induced death" [PMID:25100604].

## Provenance of mouse donor annotations (QuickGO lookup, Q8CE90)

- QuickGO lists the mouse Map2k7 (Q8CE90) GO:0004707 MAP kinase activity row as a UniProt IDA citing PMID:9405446,
  a paper that describes MKK7 activating SAPK/JNK; the rat ISO row for GO:0004707 is copied from it.
- The mouse rows for GO:0009611 response to wounding and GO:2000671 regulation of motor neuron apoptotic process are
  MGI IMP rows citing PMID:25100604 (axotomy of facial motoneurons).
