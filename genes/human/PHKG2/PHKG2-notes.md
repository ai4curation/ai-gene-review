# PHKG2 (Homo sapiens) — review notes

UniProtKB:P15735. HGNC:8931. Gene: PHKG2. 406 aa. Chromosome 16.

## Identity / core biology

PHKG2 = "Phosphorylase b kinase gamma catalytic chain, liver/testis isoform"
(PHK-gamma-LT / PHK-gamma-T / PSK-C3 / phosphorylase kinase subunit gamma-2).
EC 2.7.11.19.

- It is the **catalytic (gamma) subunit** of phosphorylase kinase (PhK). PhK is a
  huge (~1.3 MDa) hexadecamer, (alpha-beta-gamma-delta)4. Gamma carries all catalytic
  activity; alpha (PHKA1/PHKA2) and beta (PHKB) are regulatory, delta is calmodulin.
  [PMID:10487978 "It has one catalytic (gamma) subunit and three different regulatory
  (alpha, beta, and delta) subunits... The three regulatory subunits inhibit the
  phosphotransferase activity of the gamma subunit."]
- Function: activates glycogenolysis by phosphorylating and thereby activating glycogen
  phosphorylase (converts phosphorylase b -> a). Couples Ca2+ (via calmodulin/delta) and
  cAMP/PKA (phosphorylation of alpha/beta) signalling to glycogen breakdown.
  [PMID:10487978 "phosphorylase b kinase (Phk), which phosphorylates and thereby
  activates glycogen phosphorylase"; "Ca2+ relieves inhibition via the delta subunit...
  Phosphorylation of the alpha and beta subunits by the ... (cAMP)-dependent protein
  kinase (PKA) also relieves inhibition of the gamma subunit and thereby activates the
  enzyme."]
- UniProt FUNCTION: "Catalytic subunit of the phosphorylase b kinase (PHK), which
  mediates the neural and hormonal regulation of glycogen breakdown (glycogenolysis) by
  phosphorylating and thereby activating glycogen phosphorylase. May regulate
  glycogeneolysis in the testis. In vitro, phosphorylates PYGM (PubMed:35549678)."
- PHKG2 is the predominant catalytic-gamma isoform in liver, testis, erythrocytes (and
  possibly other non-muscle tissues), whereas PHKG1 is the muscle isoform.
  [PMID:8896567 "the PHKG2 gene product is the predominant isoform of the catalytic
  gamma subunit of Phk not only in testis but also in liver, erythrocytes and, possibly,
  other non-muscle tissues."]

## Structure / features (UniProt)
- Protein kinase domain 24..291; active site (proton acceptor) at 153; ATP binding 30..38
  and 53. CAMK Ser/Thr protein kinase family.
- Two calmodulin-binding regions: 306..330 (domain-N) and 346..370 (domain-C).
- Crystal structure 2Y7J (residues 6-293, kinase domain).
- Catalytic activity: 2 ATP + phosphorylase b = 2 ADP + phosphorylase a (EC 2.7.11.19),
  ECO experimental from PMID:35549678.

## Disease
- Glycogen storage disease type IXc (GSD9C / GSD-IXc, OMIM 613027): autosomal recessive
  liver PhK deficiency. Infantile hepatomegaly, growth retardation, hypotonia, liver
  dysfunction, elevated aminotransferases and lipids; can progress to hepatic
  fibrosis/cirrhosis (more severe than the X-linked PHKA2 form).
  [PMID:8896567; PMID:12930917; PMID:35549678; PMID:9245685]
- PHKG2 GSD9C variants (V106E, G189E, E157K, D215N, F233S, H89fs, R320DfsX5, etc.)
  reduce PhK enzyme activity. Functional assays: D215N and F233S markedly decrease PhK
  activity; S253G polymorphism has no impact. [PMID:35549678; PMID:12930917; PMID:8896567]

## GO annotation review decisions (summary)

Core, accept:
- GO:0004689 phosphorylase kinase activity (MF) — this IS the gene's function. Multiple
  EXP (Reactome PMID:12930917, PMID:7847371, UniProt PMID:35549678), TAS, IBA, IEA.
  ACCEPT the IBA/EXP(35549678); the others accepted/kept.
- GO:0005964 phosphorylase kinase complex (CC part_of) — subunit of the holoenzyme. IBA +
  TAS + IEA. ACCEPT.
- GO:0005829 cytosol (CC) — IDA (HPA) + Reactome TAS. ACCEPT. (glycogenolysis is cytosolic)
- GO:0005980 glycogen catabolic process (BP) — TAS Reactome + IEA. This is the specific
  process; accept as the core BP.
- GO:0045819 positive regulation of glycogen catabolic process (BP) — kinase activation of
  phosphorylase = positive regulation of glycogen catabolism. ACCEPT (TAS + IEA).
- GO:0005516 calmodulin binding (MF) — gamma subunit has 2 CaM-binding regions; delta =
  CaM; IEA. ACCEPT (supported by UniProt features + PMID:10487978 regulation).
- GO:0005524 ATP binding (MF) — kinase; ATP-binding P-loop 30..38. ACCEPT.

Generalize / less-specific (MODIFY or ACCEPT-as-broad-parent):
- GO:0005737 cytoplasm (IBA is_active_in) — correct but cytosol (0005829) is more specific
  and separately annotated. KEEP (IBA, is_active_in) but note cytosol is more precise.
- GO:0004672 protein kinase activity (IEA InterPro) — true but generic parent of 0004689.
  ACCEPT as broader IEA (allowed to be broader).
- GO:0004674 protein serine/threonine kinase activity (TAS) — true (CAMK Ser/Thr family)
  but parent of phosphorylase kinase activity. ACCEPT (broader, correct branch).
- GO:0006468 protein phosphorylation (BP TAS PMID:2948189) — generic; the specific act is
  phosphorylating glycogen phosphorylase within glycogenolysis. KEEP (correct but generic).
- GO:0005977 glycogen metabolic process (BP) — parent of glycogen catabolic process; the
  activity drives catabolism specifically. ACCEPT as broader (IBA/TAS/IEA).

Non-core / peripheral:
- GO:0007165 signal transduction (BP IBA) — PhK is a node coupling Ca2+/cAMP signals to
  glycogenolysis, so "signal transduction" is defensible but broad and not the core MF.
  KEEP_AS_NON_CORE.
- GO:0006091 generation of precursor metabolites and energy (BP TAS PMID:8896567) — broad
  metabolic role (glycogenolysis yields glucose/energy). KEEP_AS_NON_CORE.
- GO:0050321 tau-protein kinase activity (MF TAS PMID:8999860) — PMID:8999860 shows RABBIT
  SKELETAL MUSCLE PhK (i.e. PHKG1 holoenzyme) phosphorylates tau in vitro; it is not about
  the liver/testis PHKG2 gamma-2 isoform, and is an in-vitro promiscuous activity, not the
  physiological function of PHKG2. MARK_AS_OVER_ANNOTATED (in-vitro, wrong isoform/tissue,
  not core). Do NOT remove (experimental TAS; defer but flag as over-annotation).

Protein binding IPIs (GO:0005515, 8 rows): all bare `protein binding`. With/from is mostly
PHKA2 (P46019, the alpha regulatory subunit — a genuine PhK partner) and one MAGEA2B
(P43356). Per policy, bare protein binding is uninformative; MARK_AS_OVER_ANNOTATED, note
the informative interaction (PHKA2 = holoenzyme assembly, captured by 0005964). Do not
REMOVE (IPI experimental). Supporting evidence = UniProt INTERACTION section.

GO:0019899 enzyme binding (IEA Ensembl, ortholog rat P31325) — generic; the meaningful
partner is glycogen phosphorylase (substrate) / PHKA2. MARK_AS_OVER_ANNOTATED (generic,
uninformative parent of protein binding).

## References about the ALPHA subunit (note)
- PMID:7847371 (van den Berg 1995): about the PhK **alpha** (alphaL/PHKA2) subunit, X-linked
  liver PhK deficiency. Reactome uses it as one evidence for PhK-holoenzyme phosphorylase
  kinase activity (R-HSA-71588). It supports the holoenzyme activity, not PHKG2 catalysis
  specifically. Keep the annotation (EXP on holoenzyme activity) but relevance to PHKG2
  gene function is MEDIUM.
- PMID:2948189 (Hanks 1987): homology cloning; identified a Ser/Thr kinase 72% identical to
  rabbit muscle phosphorylase kinase gamma — this is the original PSK-C3/PHKG2 cDNA
  identification. Supports Ser/Thr kinase + phosphorylase kinase identity.

## core_functions
- MF GO:0004689 phosphorylase kinase activity; directly_involved_in GO:0005980 glycogen
  catabolic process (and its positive regulation, GO:0045819); location GO:0005829 cytosol;
  in_complex GO:0005964 phosphorylase kinase complex.
</content>
</invoke>
