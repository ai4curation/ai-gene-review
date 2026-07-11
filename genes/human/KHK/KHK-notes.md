# KHK (Ketohexokinase / Fructokinase) — review notes

UniProt: P50053 (KHK_HUMAN). HGNC:6315. EC 2.7.1.3. Human, NCBITaxon:9606.

## Core biology

KHK (ketohexokinase, a.k.a. hepatic fructokinase) catalyzes the **committed first step of
dietary fructose catabolism (fructolysis)**: fructose + ATP -> fructose-1-phosphate + ADP.

- UniProt FUNCTION: "Catalyzes the phosphorylation of the ketose sugar fructose to
  fructose-1-phosphate." [file:P50053 CC FUNCTION, ECO:0000269|PubMed:12941785]
- Catalytic activity: "beta-D-fructose + ATP = beta-D-fructose 1-phosphate + ADP + H(+)";
  Rhea:RHEA:18145; EC=2.7.1.3. [file:P50053 CC CATALYTIC ACTIVITY]
- Pathway: "Carbohydrate metabolism; fructose metabolism." [file:P50053 CC PATHWAY;
  UniPathway:UPA00202]
- Requires potassium; inhibited by ADP. [file:P50053 CC ACTIVITY REGULATION]
- KM=0.8 mM for D-fructose (KHK-C, isoform C displayed); KM=0.15 mM for Mg-ATP; kcat 7.6/s.
  Isoform A: KM=7 mM for D-fructose (much lower affinity). [file:P50053 CC BIOPHYSICOCHEMICAL,
  CC MISCELLANEOUS Isoform A]

## Isoforms (alternative splicing of two adjacent 135-bp exons)

- **KHK-C** (P50053-1, "central"; hepatic/renal/intestinal): high-affinity fructose enzyme,
  the physiologically dominant hepatic isoform.
- **KHK-A** (P50053-2, "peripheral"): widely distributed, low expression, poorer fructose
  affinity, more thermostable; no defined physiological function.
- [PMID:12941785 abstract, "Alternative splicing of the ketohexokinase (fructokinase) gene
  generates a 'central' predominantly hepatic isoform (ketohexokinase-C) and a more widely
  distributed ketohexokinase-A. Only the abundant hepatic isoform is known to possess
  activity ... Here we show that both ketohexokinase isoforms are indeed active.
  Ketohexokinase-A has much poorer substrate affinity than ketohexokinase-C for fructose but
  is considerably more thermostable."]
- [PMID:19237742 full text, "Fructose catabolism is initiated by its phosphorylation to
  fructose 1-phosphate, which is performed by ketohexokinase (KHK)."]

## Structure / mechanism

- pfkB family of carbohydrate kinases (ribokinase-like fold). InterPro IPR034093 (KHK),
  IPR011611 (PfkB_dom), IPR029056 (Ribokinase-like). Pfam PF00294. [file:P50053 DR / CC SIMILARITY
  "Belongs to the carbohydrate kinase PfkB family."]
- Functions as a **homodimer**; dimer interface formed by extended four-stranded beta-sheets.
  [PMID:19237742 full text, "Gel filtration and nondenaturing polyacrylamide gel electrophoresis
  ... have demonstrated that KHK is a dimer in solution."; "The KHK-A ternary-complex structure
  reveals the presence of one active site per subunit"]
- Ternary complex (KHK-A + fructose + AMP-PNP): fructose almost completely buried, all five
  hydroxyls H-bond to Asp15/Gly41/Asn42/Asn45/Asp258; AMP-PNP at opposite end of cleft; gamma-
  phosphate tightly bound to GAGD motif (255-258). [PMID:19237742 full text]
- Cytosolic. [Reactome R-HSA-70333 "Cytosolic ketohexokinase (KHK, also known as fructokinase)
  catalyzes the reaction of D-fructose (Fru) and ATP to form D-fructose 1-phosphate (Fru 1-P) and
  ADP."]

## Disease

- **Essential fructosuria** (FRUCT, MIM:229800): benign inborn error caused by recessive KHK
  deficiency; persistent rise in blood fructose and urinary fructose excretion after fructose/
  sucrose/sorbitol. Disease alleles G40R (null, insoluble) and A43T (thermolabile).
  [PMID:7833921 abstract; PMID:12941785 abstract; file:P50053 CC DISEASE; Reactome R-HSA-5656459]
- Distinct from Hereditary Fructose Intolerance (HFI), which is ALDOB deficiency **downstream**
  of KHK — HFI is where the Fru-1-P produced by KHK accumulates because aldolase B cannot cleave
  it. [~/repos/dismech/kb/disorders/Hereditary_Fructose_Intolerance.yaml]
- Note: fructose entering via KHK bypasses the phosphofructokinase (PFK-1) regulatory step of
  glycolysis, so KHK-driven fructolysis is essentially unregulated — relevant to fructose-driven
  metabolic disease (lipogenesis, hyperuricemia). [PMID:19237742 full text background:
  "the greatly increased fructose load in Western diets ... has been implicated in the development
  of adverse metabolic states, namely glucose intolerance, hyperlipidaemia, obesity, insulin
  resistance, diabetes and gout"]

## Localization

- Cytosol/cytoplasm (TAS Reactome, IBA, IDA LIFEdb). Consistent with a soluble cytosolic kinase.
- Extracellular exosome (HDA, PMID:19056867 urinary exosome proteomics): a high-throughput MS
  detection in urinary exosomes; KHK is renal/intestinal too. Not the site of catalytic function;
  KEEP_AS_NON_CORE (proteomic detection, not functional localization).

## GOA annotation notes (actions)

- GO:0004454 ketohexokinase activity — core MF. IBA/IEA/IDA(PMID:12941785)/TAS(PMID:7833921) all
  ACCEPT (multiple orthogonal lines; EC 2.7.1.3 / RHEA:18145).
- GO:0006000 fructose metabolic process — core BP (IBA/IEA/IDA). ACCEPT. (Could be modified to the
  more precise GO:0006001 fructose catabolic process; captured in core_functions.)
- GO:0005524 ATP binding — MF, IDA PMID:19237742 (AMP-PNP co-crystal). ACCEPT.
- GO:0070061 fructose binding — MF, IDA PMID:19237742 (fructose co-crystal). ACCEPT.
- GO:0042802 identical protein binding + GO:0042803 protein homodimerization activity — IDA
  PMID:19237742 (KHK is a homodimer). ACCEPT (homodimerization is real and structurally
  characterized); homodimerization is not the *core* function but is well-supported.
- GO:0005515 protein binding — IPI PMID:25416956 (LHX9, high-throughput Y2H interactome). Bare
  "protein binding" is uninformative per curation policy -> MARK_AS_OVER_ANNOTATED (not REMOVE;
  it is an experimental IPI).
- GO:0005979 regulation of glycogen biosynthetic process — IBA GO_REF:0000033 (PAN-GO). KHK
  produces Fru-1-P feeding hepatic carbohydrate/glycogen metabolism, but KHK is not a regulator of
  glycogen synthesis; this is a broad/indirect PAN-GO propagation -> MARK_AS_OVER_ANNOTATED /
  KEEP_AS_NON_CORE. (UniProt DR shows the current PAN-GO term as GO:0070873 regulation of glycogen
  metabolic process + GO:0032868 response to insulin.)
- GO:0005737 cytoplasm (IBA, IDA) and GO:0005829 cytosol (TAS Reactome x2) — ACCEPT (cytosolic).
- GO:0070062 extracellular exosome — HDA PMID:19056867 -> KEEP_AS_NON_CORE (proteomic detection).

## References cited
- PMID:7833921 — cloning + essential fructosuria mutational basis (abstract-only cache).
- PMID:12941785 — recombinant WT/mutant KHK properties, both isoforms active (abstract-only cache).
- PMID:19237742 — crystal structures of KHK-A and KHK-C; full text available.
- PMID:19056867 — urinary exosome proteomics (abstract-only cache).
- PMID:25416956 — human interactome map (LHX9 interaction; full text available but does not quote KHK).
- Reactome R-HSA-70333 (reaction), R-HSA-5656459 (defective KHK), UniPathway UPA00202.
</content>
