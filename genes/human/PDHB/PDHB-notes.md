# PDHB (human) review notes

UniProtKB:P11177 — Pyruvate dehydrogenase E1 component subunit beta, mitochondrial (ODPB_HUMAN).
Gene HGNC:8808 (PDHB; synonym PHE1B). EC 1.2.4.1.

Deep research: `PDHB-deep-research-falcon.md` did not appear within the 8-min poll window;
review grounded in the UniProtKB entry, the seeded GOA TSV, the PDC-deficiency disorder KB
(`~/repos/dismech/kb/disorders/Pyruvate_Dehydrogenase_Deficiency.yaml`), and the cached
`publications/PMID_*.md`. NEVER fabricated a `-deep-research-*.md`.

## Verified biology

- PDHB is the **E1 beta** subunit. Together with PDHA1 (E1alpha) it forms the
  heterotetrameric (alpha2-beta2) E1 component of the mitochondrial pyruvate dehydrogenase
  complex (PDC). [UniProt FUNCTION: "Together with PDHA1 forms the heterotetrameric E1 subunit
  of the pyruvate dehydrogenase (PDH) complex"; SUBUNIT: "Heterotetramer of two PDHA1 and two
  PDHB subunits"].
- E1 catalyses the TPP (thiamine diphosphate)-dependent oxidative decarboxylation of pyruvate
  and the reductive acetylation of the E2 lipoyl group. EC 1.2.4.1; Rhea:19189.
  [PMID:19081061 full text: "The E1p component catalyzes the ThDP-mediated decarboxylation of
  pyruvate ... and the reductive acetylation of a lipoyl group"].
- Structure: alpha2beta2 heterotetramer; TPP-dependent; K+ structural sites in E1beta.
  [PMID:12651851 abstract: "In alpha2beta2-heterotetrameric human pyruvate dehydrogenase, this
  cofactor is used to cleave the Calpha-C(=O) bond of pyruvate followed by reductive acetyl
  transfer to lipoyl-dihydrolipoamide acetyltransferase"; crystal structure 1.95 A holo-form].
- Subcellular location: mitochondrial matrix. [UniProt SUBCELLULAR LOCATION: Mitochondrion
  matrix]. E1 heterotetramer binds the E2 (DLAT) core.
- The whole PDC links glycolysis to the TCA cycle (gateway/committed step, pyruvate ->
  acetyl-CoA + CO2). [PMID:19081061: "the gate-keeper enzyme that strategically links
  glycolysis to the Krebs cycle and lipogenic pathways"].

## Disease

- PDHB variants cause **pyruvate dehydrogenase E1-beta deficiency (PDHBD, MIM 614111;
  MONDO:0013580; ORPHA:255138)**, an autosomal-recessive PDC-deficiency subtype (~10% as
  frequent as PDHA1) presenting with primary lactic acidosis, developmental delay, hypotonia.
  [PMID:18164639 abstract: "We have found four cases of PDHB mutations among 83 analyzed cases
  of PDC deficiency ... All cases were diagnosed by low PDC activity, with normal E2 and E3
  activities"]. Disorder KB: PDHB → MONDO:0013580, autosomal recessive.

## Annotation notes / decisions

- **Core MF**: GO:0004739 pyruvate dehydrogenase (acetyl-transferring) activity — verified
  (EC 1.2.4.1; Rhea:19189; UniProt CATALYTIC ACTIVITY from PubMed:19081061). Note the
  `contributes_to` qualifier on IDA lines (18164639, 19081061) is correct: E1 activity is a
  property of the alpha2beta2 heterotetramer, to which PDHB contributes; TAS line (2376596)
  uses `enables`.
- **Core BP**: GO:0006086 pyruvate decarboxylation to acetyl-CoA — verified (multiple IDA/IBA).
- **Core CC**: GO:0045254 pyruvate dehydrogenase complex (part_of) and GO:0005759
  mitochondrial matrix — verified.
- **GO:0006099 tricarboxylic acid cycle (TAS, PMID:2376596)**: PDC feeds the TCA cycle but is
  not itself part of the TCA cycle; keep as non-core (PDC is the entry gateway, upstream of the
  cycle proper). The cited paper is about E1beta cDNA and TCA-cycle-deficient fibroblasts.
- **GO:0005515 protein binding (IPI x4)**: bare `protein binding` — do NOT remove experimental
  IPIs (policy). WITH/FROM shows biologically meaningful partners: PDHA1 (P08559; the E1
  heterotetramer partner) in 12651851, 29128334, 33961781; DLAT (P10515; the E2 core) in
  18206651 and 33961781. Mark as over-annotated (uninformative term) but note the real
  interactions are captured by the complex/heterotetramer terms and core_functions.
- **GO:0005634 nucleus (HDA, PMID:21630459)**: single sperm-nucleus proteomics hit; a
  mitochondrial matrix enzyme. Contaminant/over-annotation of a large-scale dataset — MARK_AS_OVER_ANNOTATED.
- **GO:0005739 mitochondrion (multiple)**: correct but less specific than mitochondrial matrix;
  keep, non-core / accept the broader localization.
- Reactome TAS mitochondrial-matrix lines (R-HSA-*): correct localization; several are generic
  matrix-protein degradation reactions (LONP1/CLPXP) rather than PDC function — accept as
  location evidence, non-core for the degradation-reaction ones.
