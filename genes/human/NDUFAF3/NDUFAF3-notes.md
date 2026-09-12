# NDUFAF3 (C3orf60) — review notes

UniProt: Q9BU61 (NDUF3_HUMAN). HGNC:29918. Gene also known as C3orf60.
184 aa; belongs to the NDUFAF3 family. Two isoforms (a = Q9BU61-1 displayed;
b = Q9BU61-2, missing residues 1-57, VSP_041086).

## Core biology

NDUFAF3 is a nucleus-encoded, mitochondrially imported **assembly factor** for
mitochondrial respiratory chain complex I (NADH:ubiquinone oxidoreductase). It is
NOT a structural subunit of the mature holoenzyme and has NO catalytic activity.

- FUNCTION (UniProt): "Essential factor for the assembly of mitochondrial
  NADH:ubiquinone oxidoreductase complex (complex I)."
  [file:human/NDUFAF3/NDUFAF3-uniprot.txt, ECO:0000269|PubMed:19463981]
- SUBUNIT (UniProt): "Interacts with NDUFAF4, NDUFS2 and NDUFS3."
  [file:human/NDUFAF3/NDUFAF3-uniprot.txt, ECO:0000269|PubMed:19463981]
- SUBCELLULAR LOCATION (UniProt): "Nucleus {ECO:0000250}. Mitochondrion inner
  membrane {ECO:0000269|PubMed:19463981}." — note the nucleus location is
  by-similarity only (ECO:0000250), the inner membrane is experimental (IDA).
  [file:human/NDUFAF3/NDUFAF3-uniprot.txt]

## Primary reference (PMID:19463981, Saada et al. 2009, Am J Hum Genet)

Abstract-only in the local cache (full_text_available: false).
- "We found that NDUFAF3 is a genuine mitochondrial complex I assembly protein
  that interacts with complex I subunits." [PMID:19463981]
- "Furthermore, we show that NDUFAF3 tightly interacts with NDUFAF4 (C6ORF66),
  a protein previously implicated in complex I deficiency." [PMID:19463981]
- Pathogenicity assessed by NDUFAF3-GFP baculovirus complementation in
  fibroblasts; MC1DN18 variants Arg-77 (G77R) and Pro-122 (R122P). [PMID:19463981]
- Conservation analysis links NDUFAF3 to the bacterial SecF/SecD/YajC
  membrane-insertion gene cluster and to C8ORF38, connecting several complex I
  disease genes by cooperation during assembly. [PMID:19463981]

## Disease

Mitochondrial complex I deficiency, nuclear type 18 (MC1DN18, MIM:618240),
autosomal recessive. Phenotypes from fatal neonatal mitochondrial disease
(PMID:19463981) to Leigh syndrome (PMID:27986404, variant Val-165 / A165V).
[file:human/NDUFAF3/NDUFAF3-uniprot.txt]

## Where NDUFAF3 acts in assembly (Reactome "Complex I biogenesis")

- R-HSA-6799203: "IP subcomplex binds NDUFAF3, NDUFAF4, TIMMDC1 to form
  Intermediate 1." — the step in which NDUFAF3 directly participates; the IP
  subcomplex is centred on core subunits NDUFS2 and NDUFS3. [reactome/R-HSA-6799203.md]
- R-HSA-6799196: "In the last step, the MCIA complex and it is assumed all of the
  assembly factors (NDUFAF2-7, TIMMDC1) dissociate from the 980kDa complex to
  leave mature Complex I." — confirms NDUFAF3 is transient and NOT part of the
  mature holoenzyme. [reactome/R-HSA-6799196.md]

## Other supporting references (interactome / proteomics — protein-binding IPIs)

- PMID:19688755 (Wessels 2009): BN + LC-MS/MS protein correlation profiling first
  flagged "a novel candidate, C3ORF60" as involved in complex I biogenesis.
- PMID:24344204 (Guarani 2014): TIMMDC1/MCIA interaction proteomics network.
- PMID:27499296 (Floyd 2016): mitochondrial AE-MS interaction map (full text cached).
- PMID:25416956, PMID:32296183, PMID:33961781, PMID:40205054: proteome-scale binary
  / cell-map interactomes; mostly high-throughput, source of the generic
  GO:0005515 protein-binding IPIs (with NDUFAF4 = Q9P032 and various non-mito hits).
- PMID:34800366 (Morgenstern 2021): high-confidence quantitative mitochondrial
  proteome — supports HTP mitochondrion localization.

## Review decisions summary

- Core BP = mitochondrial respiratory chain complex I assembly (GO:0032981) —
  ACCEPT on IMP/IEA/IBA (all from/consistent with PMID:19463981).
- Core location = mitochondrial inner membrane (GO:0005743) — ACCEPT on IDA/IBA/
  IEA/Reactome-TAS.
- Nucleus (GO:0005634): IEA (by-similarity) KEEP_AS_NON_CORE; IDA (LIFEdb GFP
  overexpression screen) MARK_AS_OVER_ANNOTATED — no established nuclear function,
  likely a screening artifact; experimental annotation not removed per policy.
- mitochondrion (GO:0005739, HTP) KEEP_AS_NON_CORE — correct but less specific.
- All GO:0005515 "protein binding" IPIs MARK_AS_OVER_ANNOTATED — uninformative
  bare term; the meaningful NDUFAF3-NDUFAF4/NDUFS2/NDUFS3 interactions are captured
  in core_functions. (Per policy, experimental/IPI protein-binding is never REMOVEd.)

## core_functions term ids used

- directly_involved_in: GO:0032981 (mitochondrial respiratory chain complex I assembly)
- locations: GO:0005743 (mitochondrial inner membrane)

No molecular_function assigned: NDUFAF3 has no catalytic activity and no
well-supported specific MF beyond generic protein binding; per task policy the
core function is centered on the assembly BP rather than inventing an MF.
