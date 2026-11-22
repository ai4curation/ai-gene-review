# CADM1 (human, Q9BY67) review notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: human CADM1 is the experimentally characterised ortholog used as the
reference for HORSE/CADM1 (A0A5F5PGJ5). No ProtNLM2 output was consulted.

### Deep research

`just deep-research-falcon human CADM1 --fallback perplexity-lite` failed:
falcon returned "Exception: Failed to authenticate" and the perplexity-lite
fallback returned HTTP 401 (insufficient quota). No deep-research file exists.
The review is built from the cached publications and the UniProt record.

### Evolutionary grounding

- UniProt Q9BY67 is in PANTHER PTHR45889:SF2 "CELL ADHESION MOLECULE 1",
  the same subfamily as mouse Cadm1 (Q8R5M8) and rat Cadm1 (Q6AYP5). Transfer
  of mouse/rat experimental data to human (ISS/IEA Ensembl Compara rows) is
  therefore within one orthologous subfamily, not a paralog transfer. PTHR45889
  has sister subfamilies named for CADM2, CADM3 and CADM4 (SF1, SF5, SF3);
  their functions are not transferred here.
- IBA rows come from two PAINT nodes: PTN002913382 (donors mouse Cadm1
  MGI:1889272, rat Cadm1 RGD:1310999 and human CADM1 itself) supplies signaling
  receptor binding, plasma membrane, cell recognition, susceptibility to NK cell
  mediated cytotoxicity, neuron projection, synapse and detection of stimulus.
  A deeper node PTN001910345 (donors mouse Cadm1 and MGI:2137858) supplies
  homophilic cell-cell adhesion, i.e. PAINT placed homophilic adhesion as a
  family-wide property and the CRTAM-ligand terms at the CADM1 node.
- PAINT did not propagate the CADM1-specific IDA terms "positive regulation of
  cytokine production" or "positive regulation of NK cell mediated
  cytotoxicity"; those stay as human experimental claims only.

### Experimental findings in human (direct evidence)

- Homophilic Ca2+-independent adhesion and cis homodimers (TSLC1-GFP in MDCK)
  [PMID:12050160 "it forms homodimers through cis interaction within the plane of the cell membranes"].
- Human mast cells: CADM1 is the sole receptor for homotypic mast cell
  aggregation [PMID:22438059 "CADM1 downregulation abolished homotypic adhesion, indicating that CADM1 is the sole receptor mediating mast cell aggregation"].
- CRTAM ligand: [PMID:15811952 "CRTAM-Necl-2 interactions promote cytotoxicity of NK cells and interferon gamma (IFN-gamma) secretion of CD8+ T cells in vitro"];
  structure of the CADM1-CRTAM complex [PMID:23871486 "Necl-2 occupies the CRTAM homodimer interface, making homodimerization impossible"];
  also [PMID:15781451 "We further show that Necl2 binds Class-I-restricted T-cell-associated molecule (CRTAM)"].
- Cytoplasmic tail: PDZ-binding-motif dependent binding to MPP3
  [PMID:13679854 "This interaction was dependent on the presence of a PDZ-binding motif at the carboxyl terminus of TSLC1"],
  MPP3-Dlg-p85 complex and PI3K activation downstream of trans-homophilic
  binding [PMID:24503895]; 4.1B/DAL-1 FERM binding [PMID:12234973, PMID:21131357].
- Tumour suppressor in NSCLC [PMID:11279526]; this is a cancer phenotype, not a
  GO process.

### Rodent (orthologous, SF2) findings

- Synaptic adhesion and synapse induction: [PMID:12202822 "functions as a homophilic cell adhesion molecule at the synapse"].
- Heterophilic adhesion with Necl-1/CADM3 and nectin-3, basolateral
  localisation in gall bladder epithelium [PMID:12826663].
- Mast cell-nerve attachment (mouse BMMC) [PMID:15905536].

### Reference problem found

- The UniProt-assigned IPI "protein binding" row with MPP3 (Q13368) cites
  PMID:29099056, an ammonia/ADMA astrocyte paper whose full text never
  mentions CADM1, TSLC1, SynCAM or MPP3. The UniProt SUBUNIT note attributes
  the MPP3 interaction to PubMed:13679854 and PubMed:24503895, so this looks
  like a mis-keyed reference. Recorded as a source_defect (WRONG_REFERENCE,
  CHECK).

### Decisions worth flagging

- "detection of stimulus" (IDA + IBA + ISS + IEA): CADM1 is the ligand that
  CRTAM-bearing lymphocytes detect; it is the stimulus, not the detector.
  Marked as over-annotated on all four rows rather than removed, because
  PAINT deliberately placed it at the CADM1 node and the curator read the full
  text of PMID:15811952.
- "positive regulation of cytokine production" (IDA) -> MODIFY to
  "positive regulation of type II interferon production" (IFN-gamma).
- Generic protein binding: MODIFY where the partner gives an informative
  activity (CRTAM -> signaling receptor binding; CADM2 -> cell adhesion
  molecule binding; MPP3 -> PDZ domain binding), otherwise REMOVE.
- "synaptic vesicle" (IEA from mouse): CADM1 is a single-pass plasma membrane
  adhesion protein; marked over-annotated.
