# XDH (human) — curation notes

UniProt: P47989 (XDH_HUMAN). HGNC:12805. Gene ID 7498. Chromosome 2. 1333 aa.

## Verified biology (from UniProt P47989 + cached publications)

XDH is **xanthine dehydrogenase/oxidase** (xanthine oxidoreductase, XOR), a large
(~146 kDa monomer) cytosolic **homodimer**. Each subunit binds a molybdopterin
(Mo-co) center, one FAD, and **two [2Fe-2S] clusters**. It catalyses the last two
steps of purine catabolism:
- hypoxanthine + NAD+ + H2O -> xanthine + NADH + H+ (EC 1.17.1.4; RHEA:24670)
- xanthine + NAD+ + H2O -> urate + NADH + H+ (EC 1.17.1.4; RHEA:16669)
The enzyme exists in an NAD+-dependent **dehydrogenase (XDH)** form that can be
converted to an O2-dependent **oxidase (XO)** form — reversibly by oxidation of
sulfhydryl groups (Cys535/Cys993, Cys509/Cys1318 disulfides in oxidase form) or
irreversibly by proteolysis. The XO form produces urate + H2O2 (EC 1.17.3.2;
RHEA:21132), a source of superoxide/H2O2 (reactive oxygen species).
[file:P47989 FUNCTION "Key enzyme in purine degradation. Catalyzes the oxidation of
hypoxanthine to xanthine. Catalyzes the oxidation of xanthine to uric acid.
Contributes to the generation of reactive oxygen species."]

Localization: cytoplasm/cytosol (primary); also reported peroxisome and secreted
(detected in milk/colostrum). [file:P47989 SUBCELLULAR LOCATION]

Disease: **Xanthinuria type I (XAN1, MIM:278300)** — isolated XDH deficiency;
excretion of large amounts of xanthine, xanthine stones, low serum/urine uric acid.
Multiple XAN1 truncating/missense variants (e.g. R149C, C150F, P1150R, and several
C-terminal truncations). [file:P47989 DISEASE]

Pharmacology: target of gout drugs **allopurinol / oxypurinol, febuxostat,
topiroxostat, tigulixostat**; also metabolizes 6-mercaptopurine and activates/handles
several prodrugs (azathioprine ADME). ChEMBL CHEMBL1929; Pharos Tclin.
(Note: combined XDH + sulfite oxidase deficiency = molybdenum cofactor deficiency, a
separate MOCS-gene disorder, NOT XDH.)

## Key experimental references (cached)

- **PMID:8670112** (Saksela & Raivio 1996, Biochem J) — cloned complete human
  XDH/XO cDNA; expressed in COS-1 cells; measured significant XDH/XO enzyme activity;
  enzyme expressed predominantly (89.8%) in the dehydrogenase form. Human. Supports
  GO:0004854 (XDH), GO:0004855 (XO), GO:0009115 (xanthine catabolic). CATALYTIC
  ACTIVITY ref in UniProt for EC 1.17.1.4. Abstract-only cache.
- **PMID:17301077** (Yamaguchi et al. 2007, J Biochem) — human XOR expressed in
  E. coli; crystal structure of E803V mutant at 2.6 Å in complex with FAD, 2Fe-2S,
  molybdopterin, salicylate, Ca. Active-site residues Glu803/Arg881 required for
  purine substrate; mutants gain aldehyde oxidase activity; not inhibited by
  allopurinol. UniProt cites for COFACTOR, CATALYTIC ACTIVITY, FUNCTION, SUBUNIT
  (homodimer). Supports cofactor-binding IDAs, XO activity, homodimerization.
  Abstract-only cache.
- **PMID:1619276** (Ichikawa et al. 1992, J Histochem Cytochem) — immunoEM of
  **rat** hepatocytes: XO labeling "clearly over the cytosol and not on cell
  organelles"; NO label over ER, Golgi, lysosomes, or peroxisomes; occasional
  mito-matrix label but no biochemical XO in mito fraction. This is the
  MGI-assigned reference for the human XDH cytosol IDA and for the array of purine
  catabolic BP IDAs (hypoxanthine/inosine/deoxyinosine/AMP/IMP catabolic, allantoin
  metabolic). Note: this study is localization only (rat); the catabolic-process
  IDAs likely derive from the enzyme's established purine-degradation role, not from
  this paper's direct assays. Abstract-only cache. NOTE: this paper's data argue
  AGAINST peroxisomal XO in rat liver — relevant to the peroxisome IEA.
- **PMID:16502470** (Palmer et al. 2006, Proteomics) — human colostrum proteomics;
  XDH identified as a minor aqueous-phase protein. Supports secreted/extracellular
  (HDA). Abstract-only.
- **PMID:32296183** (Luck et al. 2020, Nature; HuRI) — human binary interactome
  (Y2H); source of the bare "protein binding" IPI (interactor GRIP1 isoform
  Q9Y3R0-3). Full text available. Uninformative MF term.

## Curation reasoning summary

- **Core MF**: GO:0004854 (xanthine dehydrogenase activity) and GO:0004855
  (xanthine oxidase activity) — both with direct human IDA (8670112, 17301077).
  ACCEPT the IDA/IBA; IEA duplicates ACCEPT.
- **Core cofactor binding**: molybdopterin cofactor (GO:0043546), FAD (GO:0050660),
  2Fe-2S (GO:0051537) — all with human IDA from the crystal structure (17301077).
  ACCEPT. GO:0071949 FAD binding (InterPro IEA) is a valid parent/sibling — ACCEPT.
  GO:0005506 iron ion binding and GO:0046872 metal ion binding and GO:0051536
  iron-sulfur cluster binding (InterPro IEAs) are correct but generic — ACCEPT
  (broader than the specific IDA terms; harmless).
- **Core BP**: GO:0009115 (xanthine catabolic process) — human IDA. ACCEPT.
  GO:0009114 (hypoxanthine catabolic) IDA — ACCEPT as core (the hypoxanthine->xanthine
  step). The other nucleotide/nucleoside catabolic BP terms (inosine, deoxyinosine,
  AMP, IMP, adenosine, guanine, GMP, dGMP, dAMP, deoxyadenosine, deoxyguanosine
  catabolic) are pathway-context terms: XDH acts only at the terminal purine-base
  oxidation steps, not on the nucleotides/nucleosides themselves. The IDAs
  (1619276-derived) and IEAs over-attribute whole upstream catabolic pathways to XDH.
  Mark the whole-pathway nucleotide/nucleoside terms as MARK_AS_OVER_ANNOTATED or
  KEEP_AS_NON_CORE; keep hypoxanthine/xanthine as core.
- GO:0000255 allantoin metabolic process — in humans urate is the END product
  (humans lack urate oxidase); allantoin is not made. MARK_AS_OVER_ANNOTATED
  (over-propagation from lower organisms). IDA ref (1619276) does not assay allantoin.
- GO:0070674 hypoxanthine dehydrogenase / GO:0070675 hypoxanthine oxidase — these are
  the hypoxanthine->xanthine activities; real (human IDA 1619276 for dehydrogenase).
  ACCEPT (or KEEP_AS_NON_CORE as sub-activities of the two canonical MFs).
- GO:0016491 oxidoreductase activity (IEA) — correct but generic parent. ACCEPT
  (harmless broad IEA) — but not core.
- **CC**: GO:0005829 cytosol (IDA 1619276, TAS Reactome, IEA) — core, ACCEPT.
  GO:0005737 cytoplasm (IEA) — broad parent, ACCEPT non-core. GO:0005576
  extracellular region (IBA/IEA/HDA) — secreted/milk pool, real but minor;
  KEEP_AS_NON_CORE. GO:0005777 peroxisome (IEA by similarity) — contradicted by
  1619276 rat immunoEM; MARK_AS_OVER_ANNOTATED. GO:0016529 sarcoplasmic reticulum
  (Ensembl IEA) — weak/orthology; MARK_AS_OVER_ANNOTATED.
- GO:0005515 protein binding IPI (HuRI) — bare, uninformative;
  MARK_AS_OVER_ANNOTATED per curation policy (do not REMOVE experimental IPI).
- GO:0042803 protein homodimerization activity IPI (17301077) — XDH is a genuine
  homodimer; ACCEPT (informative and structurally supported).
