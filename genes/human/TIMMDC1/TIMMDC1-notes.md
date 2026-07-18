# TIMMDC1 (Q9NPL8) review notes

## Identity
- Gene: TIMMDC1 (TIM17 domain-containing protein 1; synonyms C3orf1, M5-14, UNQ247/PRO284). HGNC:1321.
- Protein: "Complex I assembly factor TIMMDC1, mitochondrial"; 285 aa; multi-pass inner-membrane protein.
  [file:human/TIMMDC1/TIMMDC1-uniprot.txt "RecName: Full=Complex I assembly factor TIMMDC1, mitochondrial"]
- Belongs to the Tim17/Tim22/Tim23 (preprotein-translocase / membrane-insertase-like) family.
  [file:human/TIMMDC1/TIMMDC1-uniprot.txt "Belongs to the Tim17/Tim22/Tim23 family."]
- Four predicted TRANSMEM helices (80-100, 137-159, 165-185, 189-209); Pfam PF02466 (Tim17); InterPro IPR055299.
  [file:human/TIMMDC1/TIMMDC1-uniprot.txt]

## Function (core)
- Chaperone/assembly factor for mitochondrial NADH:ubiquinone oxidoreductase (Complex I); builds the membrane arm.
  [file:human/TIMMDC1/TIMMDC1-uniprot.txt "Chaperone protein involved in the assembly of the mitochondrial NADH:ubiquinone oxidoreductase complex (complex I). Participates in constructing the membrane arm of complex I."]
- Andrews et al. 2013 (PMID:24191001, PNAS, DOI:10.1073/pnas.1319247110): C3orf1 (=TIMMDC1), a hydrophobic
  protein, associates with the 550 and 815 kDa CI subcomplexes that accumulate on NDUFA11 knockdown; its
  characteristics, together with TMEM126B and NDUFA11, "suggest that they all participate in constructing the
  membrane arm of complex I." (source of the UniProt FUNCTION statement; verified via PubMed metadata — abstract
  only in cache-less state, no verbatim quote stored). This is the SUBUNIT source: "Associates with the
  intermediate 315 kDa subcomplex of incompletely assembled complex I."
  [file:human/TIMMDC1/TIMMDC1-uniprot.txt "Associates with the intermediate 315 kDa subcomplex of incompletely assembled complex I."]

## Molecular function — deliberately conservative
- TIMMDC1 is a TIM17/22/23-family membrane-insertase-like protein and a plausible scaffold/insertase for the
  membrane-arm (ND) subunits, BUT no direct evidence in the local files demonstrates catalytic "membrane
  insertase activity" (GO:0032977) or "protein transporter activity". Whether it is a true insertase vs. a
  scaffold is unresolved. It is NOT a stable structural subunit of the CI holoenzyme (it is a transient assembly
  factor that dissociates — Reactome R-HSA-6799196: "The MCIA complex, NDUFAF2-7 all dissociate from the 980kDa
  complex, resulting in Complex I"). Therefore no NADH-dehydrogenase MF (GO:0008137) and no structural-constituent
  MF is asserted. The core function is captured as the BP (GO:0032981) with a chaperone/scaffold description; MF
  is flagged as a knowledge gap.

## Localization
- Mitochondrion membrane; multi-pass membrane protein (inner membrane by Reactome TAS).
  [file:human/TIMMDC1/TIMMDC1-uniprot.txt "SUBCELLULAR LOCATION: Mitochondrion membrane"]
  [file:human/TIMMDC1/TIMMDC1-uniprot.txt "Multi-pass membrane protein"]
- GOA has IBA/IDA/HTP mitochondrion, IEA mitochondrial membrane, TAS mitochondrial inner membrane (Reactome).
- GOA also has one IDA nucleoplasm (HPA GO_REF:0000052). This contradicts all other evidence (mitochondrial
  inner-membrane multipass protein) and is almost certainly antibody cross-reactivity / non-specific HPA staining.
  Kept as non-core rather than removed (IDA, not to be REMOVEd per policy).

## Interactions / MCIA context
- Interacts with TMEM70 (PMID:33753518, Carroll et al. 2021, PNAS, DOI:10.1073/pnas.2100558118, full text cached):
  "TMEM70-t was found in association with ACAD9, NDUFAF1, and also with an additional assembly factor for complex
  I, the translocase of IMM domain-containing protein 1, or TIMMDC1". The GOA IPI GO:0005515 with WITH/FROM
  UniProtKB:Q9BUB7 (TMEM70) is supported by this paper. TMEM70/TMEM242 interact with the MCIA complex that
  supports assembly of the CI membrane arm.
  [file:human/TIMMDC1/TIMMDC1-uniprot.txt "Interacts with TMEM70 (PubMed:33753518)."]
- Large-scale binary/AP-MS interactome papers give generic GO:0005515 "protein binding" IPI:
  - PMID:25416956 (Rolland et al. 2014, Cell, DOI:10.1016/j.cell.2014.10.050) — HuRI/CCSB binary map; WITH/FROM Q969F0 (FATE1).
  - PMID:31515488 (Fragoza et al. 2019, Nat Commun, DOI:10.1038/s41467-019-11959-3) — variant interaction perturbation; WITH/FROM Q969F0 (FATE1).
  - PMID:32296183 (Luck et al. 2020, Nature, DOI:10.1038/s41586-020-2188-x) — HuRI reference binary interactome; many WITH/FROM partners (SCD, STX6, FAM20B, YIF1A, SERF1B, ...), mostly non-mitochondrial (Y2H-derived).
  - PMID:33961781 (Huttlin et al. 2021, Cell, DOI:10.1016/j.cell.2021.04.011) — BioPlex 3.0 AP-MS; WITH/FROM Q9NX14 (NDUFB11, a CI membrane-arm subunit — biologically meaningful).
  These are uninformative at the MF level (bare "protein binding"); most Y2H partners are membrane proteins from
  the ORFeome and look like sticky-membrane-protein noise. The NDUFB11 hit (BioPlex) is consistent with CI
  membrane-arm engagement. Marked over-annotated (not removed; experimental IPI per policy).

## Disease
- Mitochondrial complex I deficiency, nuclear type 31 (MC1DN31; MIM:618251); autosomal recessive.
  [file:human/TIMMDC1/TIMMDC1-uniprot.txt "Mitochondrial complex I deficiency, nuclear type 31 (MC1DN31)"]
- Established by Kremer et al. 2017 (PMID:28604674, Nat Commun, DOI:10.1038/ncomms15824): an intronic cryptic
  splice event in TIMMDC1 "establishing a novel disease-associated gene" (RNA-seq diagnosis of mitochondriopathy).
  [file:human/TIMMDC1/TIMMDC1-uniprot.txt "INVOLVEMENT IN MC1DN31"]

## Tissue / phosphorylation
- Enhanced expression in heart and skeletal muscle. [file:human/TIMMDC1/TIMMDC1-uniprot.txt "Generalized expression enhanced in heart and skeletal muscle."]
- Phosphoserine at Ser-277 (large-scale, PMID:24275569).

## Reactome (Complex I biogenesis, R-HSA-6799198)
- R-HSA-6799203: "IP subcomplex binds NDUFAF3, NDUFAF4, TIMMDC1 to form Intermediate 1" — TIMMDC1 joins the
  315 kDa IP-subcomplex-derived Intermediate 1.
- TAS mitochondrial inner-membrane location annotations (R-HSA-6799178/179/191/196/197/202/203) are all steps in
  this CI biogenesis pathway; location (inner membrane) is well supported and consistent with UniProt.

## Curation decisions summary
- BP GO:0032981 (CI assembly): ACCEPT (core), even though IEA — strongly corroborated by UniProt FUNCTION
  (PMID:24191001), Reactome, and disease.
- Mitochondrion / mitochondrial membrane / mitochondrial inner membrane locations: ACCEPT (core location) for the
  best-supported ones; inner membrane is the precise term.
- nucleoplasm IDA: KEEP_AS_NON_CORE (contradicts mito localization; likely HPA artefact; not removing an IDA).
- protein binding IPIs: MARK_AS_OVER_ANNOTATED (bare GO:0005515; keep, don't remove per policy). The TMEM70 one
  (PMID:33753518) and the NDUFB11 one (PMID:33961781) are biologically meaningful but still uninformative MF.
