# ABCA8 (human) curation notes

UniProt: O94911 (ABCA8_HUMAN); HGNC:38; gene ID 10351; chromosome 17. Displayed
canonical in UniProt = isoform 3 (O94911-3). PANTHER PTHR19229:SF274 "ABC-type
organic anion transporter ABCA8". ABCA6-like subgroup of the ABCA family.

## Protein architecture
- 1621 aa, multi-pass membrane protein (~14 predicted TM helices), heavily
  N-glycosylated (16 predicted sites; Asn-84 glycosylation shown by liver
  glycoproteomics, PMID:19159218).
- Two ABC transporter domains (480-715 and 1285-1518) each with a Walker-A
  ATP-binding P-loop (BINDING 516-523 and 1323-1330) [file:human/ABCA8/ABCA8-uniprot.txt
  "ABC transporter 1"]. "Belongs to the ABC transporter superfamily. ABCA family."
- EC assigned 7.6.2.- (translocase) [ECO:0000269|PubMed:12379217].

## Function
- **Sterol/bile-acid efflux (core).** Full-length human ABCA8 (and mouse ABCA8b)
  "mediates efflux of [3H]cholesterol and [3H]taurocholate" and "functions as a
  sinusoidal efflux transporter for at least cholesterol and taurocholate in mouse
  and human liver" [PMID:29300488]. Notably it showed "no significant efflux
  activity for [3H]estrone sulfate, [3H]digoxin, [3H]vinblastine,
  [3H]para-aminohippuric acid, [3H]oleic acid, [14C]nicotine, or [3H]methotrexate"
  for the full-size transporter [PMID:29300488] — contrasting with the short-isoform
  organic-anion results below.
- **HDL regulation / ABCA1 cooperation (core).** "Overexpression of wild-type but
  not mutant ABCA8 resulted in a significant increase (1.8-fold; P=0.01) of
  cholesterol efflux to apolipoprotein AI in vitro" and "ABCA8 colocalizes and
  interacts with adenosine triphosphate-binding cassette transporter A1 and further
  potentiates adenosine triphosphate-binding cassette transporter A1-mediated
  cholesterol efflux" [PMID:28882873]. Human low-HDLc probands carry deleterious
  ABCA8 variants (P609R, IVS17-2 A>G, T741X); Abca8b-/- mice have lower HDLc.
  Conclusion: "ABCA8 facilitates cholesterol efflux and modulates HDLc levels in
  humans and mice" [PMID:28882873]. UniProt: "Interaction with ABCA1 potentiates
  cholesterol efflux to lipid-free APOA1, which regulates high-density lipoprotein
  cholesterol levels" [file:human/ABCA8/ABCA8-uniprot.txt].
- **Organic-anion/xenobiotic transport (non-core, short isoform 1).** In Xenopus
  oocytes, estradiol-beta-glucuronide, taurocholate, LTC4, PAH and ochratoxin A were
  accumulated ("para-aminohippuric acid, ochratoxin-A, were significantly
  accumulated"), "The transport of [14C]estradiol-beta-glucuronide was
  ATP-dependent", and "ABCA8 is a new member of the xenobiotic transporter
  ABC-subfamily" [PMID:12379217]. Km values 0.1-30.4 uM. Physiological relevance
  uncertain and partly contradicted for full-length protein (PMID:29300488).
- **Sphingolipid/myelin (non-core, oligodendrocyte).** "ABCA8 was able to
  significantly stimulate both sphingomyelin synthase 1 expression and sphingomyelin
  production" and the data "strongly suggest that ABCA8 regulates lipid metabolism
  in oligodendrocytes" [PMID:23560799]. This is a positive-regulatory effect on
  sphingolipid biosynthesis (SGMS1 is the catalytic enzyme), not direct biosynthesis
  by ABCA8 — hence the GO:0006686 row is modified to positive regulation of
  sphingolipid biosynthetic process (GO:0090154).

## Localization
- "Cell membrane"; "Basolateral cell membrane"; "Predominantly expressed on the
  sinusoidal plasma membrane" [file:human/ABCA8/ABCA8-uniprot.txt]. Mouse orthologue
  "predominantly distributed in sinusoidal membranes of the hepatocytes"
  [PMID:29300488]. Variant P609R affects plasma-membrane localization and abolishes
  efflux to APOA1 [PMID:28882873]. The ER IDA row (PMID:28882873) is treated as
  over-annotation: ABCA8 is a PM transporter and any ER signal in transfected
  overexpression most likely reflects biosynthetic transit (organelle-annotation
  policy: ER transit is not residence).

## Tissue expression
- Widely expressed, higher in heart, skeletal muscle and liver; highly expressed in
  superior frontal and inferior temporal white matter [file:human/ABCA8/ABCA8-uniprot.txt;
  PMID:12379217; PMID:23560799].

## Curation summary
- Core molecular function: ATP-driven (ATPase-coupled) transmembrane transport of
  sterol/lipid substrates (GO:0042626 / GO:0140359 / GO:0005319). Core processes:
  cholesterol efflux and transport (GO:0033344, GO:0030301) and regulation of
  cholesterol efflux (GO:0010874/GO:0010875).
- All four cited publications are abstract-only in the cache (full_text_available:
  false), so experimental (IDA/IMP/EXP) rows are not overruled on abstract gaps;
  claims are anchored to abstract text and the curated UniProt ECO:0000269 record.
