# AHCY (human) — curation notes

UniProt: P23526 (SAHH_HUMAN). Gene: AHCY / SAHH. HGNC:343. 432 aa. EC 3.13.2.1.

## Core biology

AHCY is **adenosylhomocysteinase** (S-adenosyl-L-homocysteine hydrolase, SAHH / AdoHcyase),
the NAD+-dependent enzyme that reversibly hydrolyses **S-adenosyl-L-homocysteine (SAH/AdoHcy)
to L-homocysteine + adenosine** [file:human/AHCY/AHCY-uniprot.txt "Reaction=S-adenosyl-L-homocysteine + H2O = L-homocysteine + adenosine"; RHEA:21708; EC=3.13.2.1].

Function is experimentally established: [PMID:10933798] provides FUNCTION and CATALYTIC ACTIVITY
evidence (ECO:0000269) and is the IDA basis for GO:0004013.

Because SAH is a potent product inhibitor of essentially every SAM-dependent methyltransferase,
AHCY clears SAH and thereby sustains cellular transmethylation, coupling the SAM/methionine cycle
to homocysteine metabolism. Reactome frames this explicitly: "Adenosylhomocysteinase (AHCY) is a
tetrameric, NAD+-bound, cytosolic protein that regulates all adenosylmethionine-(AdoMet) dependent
transmethylations by hydrolysing the feedback inhibitor adenosylhomocysteine (AdoHcy) to homocysteine
(HCYS) and adenosine (Ade-Rib)" [Reactome:R-HSA-174401].

- **Cofactor:** binds 1 NAD(+) per subunit [file:UniProt PubMed:12590576, PubMed:9586999].
- **Quaternary structure:** homotetramer [file:UniProt SUBUNIT "Homotetramer"; PMID:19177456; PMID:28647132; PMID:9586999].
- **Pathway:** L-homocysteine biosynthesis; L-homocysteine from S-adenosyl-L-homocysteine, step 1/1 (UniPathway UPA00314; UER00076). Maps to GO:0071269 L-homocysteine biosynthetic process.
- **Localization:** primarily cytosolic (IDA:HPA GO:0005829; Reactome TAS). Also reported in nucleus and ER by GFP-tagging [PMID:28647132], and in melanosome fractions [PubMed:17081065, IEA-SubCell]. Nuclear pool is thought to act at sites of AdoMet-dependent methylation [PMID:28647132 abstract].

## Disease

Deficiency causes **Hypermethioninemia with S-adenosylhomocysteine hydrolase deficiency (HMAHCHD;
MIM:613752)** — elevated SAH/SAM/methionine, failure to thrive, psychomotor/developmental delay,
facial dysmorphism, myopathy/myocardiopathy, hepatopathy [file:UniProt DISEASE; Reactome:R-HSA-5579084;
PMID:15024124]. Numerous loss-of-function missense variants (R49C, G71S, D86G, A89V, Y143C, Y328D,
W112* truncation) reduce catalytic activity and/or perturb tetramerization and nucleocytoplasmic
distribution [file:UniProt VARIANT features; PMID:19177456; PMID:28647132].

## GOA annotation review summary (P23526-goa.tsv, 31 lines)

Molecular function
- GO:0004013 adenosylhomocysteinase activity — IBA, IEA, IDA (PMID:10933798), TAS (PMID:2596825): ACCEPT (core MF). IDA is the strongest.
- GO:0005515 protein binding — IPI x13 rows from large-scale interactome / OpenCell screens (PMID:25416956, 25910212, 28514442, 31515488, 32296183, 33961781, 35271311): uninformative bare "protein binding". Per policy, MARK_AS_OVER_ANNOTATED (do NOT REMOVE experimental IPIs). The biologically meaningful interaction (AHCYL1 homolog, homotetramer) is captured elsewhere; the IntAct partners (ANKRD40 Q6AI12, C1orf50 Q9BV19, APPBP2 Q92624) are not functionally interpreted.

Biological process
- GO:0033353 L-methionine cycle — IBA: ACCEPT (core; methionine/SAM cycle context). (UniProt DR still shows the older label "S-adenosylmethionine cycle" for GO:0033353; current ontology label is "L-methionine cycle".)

Cellular component
- GO:0005829 cytosol — IBA + IDA(HPA) + TAS(Reactome x2): ACCEPT (core location). Multiple independent lines.
- GO:0005737 cytoplasm — IEA SubCell: ACCEPT (broader parent of cytosol; consistent, less specific).
- GO:0005634 nucleus — IEA SubCell + EXP (PMID:28647132): KEEP_AS_NON_CORE. Real but minor/secondary pool shown by GFP tagging; not the principal site of catalysis.
- GO:0005783 endoplasmic reticulum — IEA SubCell + EXP (PMID:28647132): KEEP_AS_NON_CORE. Same GFP-tagging study; secondary distribution, not a known ER function.
- GO:0042470 melanosome — IEA SubCell (from melanosome-fraction MS PubMed:17081065): MARK_AS_OVER_ANNOTATED. High-throughput organelle proteomics co-purification; not an established site of AHCY function.
- GO:0070062 extracellular exosome — HDA x3 (PMID:23533145, 19056867, 20458337): MARK_AS_OVER_ANNOTATED. Abundant cytosolic protein routinely detected in exosome/secretome MS; not a functional secreted location.

## Notes on evidence access
- No deep-research file (falcon out of credits, HTTP 402). Grounded in UniProt, GOA, cached publications, Reactome.
- Interactome/exosome papers are large-scale MS/Y2H studies; AHCY appears in supplementary lists, not named in abstracts, so PMID verbatim quotes for the specific AHCY finding are not available in the cache. Location/exosome supporting_text drawn from file:UniProt where possible.
