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

## 2026-09-27 full campaign audit

The canonical human symbol is **AHCY, HGNC:343**, Approved in the archived
HGNC primary-source subset `projects/CLINGEN_MENDELIAN/hgnc-symbols.json`.
SAHH and AdoHcyase are aliases; neither has a separate human gene directory.
The coordinator independently searched open PRs for all three names and found
no overlap. All five canonical files matched main
`9541f70405e9e9bef718106c32ec1a54a8051bda` byte-for-byte before authoring;
`/tmp/AHCY-base/baseline.json` records the source blobs and SHA-256 hashes.
The baseline has **25 seeded assertions plus one pre-existing NEW proposal**,
not 26 independently seeded assertions. Original term, evidence, reference,
qualifier and isoform fields remain unchanged, including the retained prior NEW.
The earlier notes' raw GOA counts describe repeated partner records; the review
has seven aggregated generic-binding rows, and all seven were reassessed.

### Research and source access

The required Falcon command with a 1200-second timeout and perplexity-lite
fallback was launched concurrently with normal publication caching. Initial
offline tool resolution failed because the required deep-research-client build
was unavailable in the local tool cache. One normal online attempt then failed
PyPI DNS resolution before either provider could run (both provider client exits
2; wrapper exit 1). This was not a fresh provider credit or scientific-response
failure. No provider artifact was generated or authored manually. The normal
publication command found all 13 originally declared PMID records already
cached and left them unchanged.

Normal additional fetches for PMID:12590576, PMID:9586999, PMID:19177456,
PMID:15024124 and PMID:33328229 returned `Cached 0/5` with DNS errors. A separate
normal attempt for PMID:41549122 returned `Cached 0/1` for the same reason.
The existing notes already cite the first four structural/disease sources;
the two later studies were identified during this audit. These six absent
records remain explicit publication gates. PMID:17081065 was already cached
and is now included in the reference list as the actual melanosome source.
No publication cache or machine source was edited. Reference availability
flags follow actual local metadata, with supplementary and extraction limits
stated separately; verified identity is not downgraded solely for a failed fetch.

### Catalytic participation, propagation and core synthesis

The original abstract of PMID:10933798 reports substrate-driven closure of the
catalytic and NAD-binding domains; it is not a verbatim account of a complete
human steady-state hydrolysis assay. The established human IDA is retained with
curator deference and independent curated/structural corroboration. The human
structure records [RCSB 1A7A](https://www.rcsb.org/structure/1A7A) and
[RCSB 1LI4](https://www.rcsb.org/structure/1LI4) were checked as primary deposited
structural evidence. They support the tetrameric cofactor-bound architecture;
the latter explicitly describes four reduced cofactors in the trapped
intermediate-analogue complex. NAD is a bound catalytic cofactor, not a net
substrate in the overall hydrolysis equation. The 1989 cDNA abstract,
PMID:2596825, supports enzyme identity and the 432-residue human sequence;
it is not presented as a kinetic experiment.

The local PTHR23420 PAINT table records all three IBD assertions at
**PTN000602759**, and its member file includes human P23526. The family also
contains an IKR at a different node, PTN001158976; no claim about that node's
exact descendants is made without the full tree. Human AHCY has direct catalytic
evidence, so the other-node negative assertion is not transferred to it. The
PAINT table's later methionine-cycle seed snapshot contains an additional
zebrafish seed compared with the original GOA; the original GOA is preserved.
Human self-evidence for activity/localization is legitimate descendant grounding,
not circularity. Source blocks use the ancestral node, not repeated extant seeds.
RHEA:21708 and EC:3.13.2.1 are supported by the exact human catalytic record;
ARBA:ARBA00087412 internals remain UNRESOLVED.

The prior homocysteine-production NEW was reassessed rather than retained merely
to align the core table. AHCY itself performs the SAH hydrolysis that releases
L-homocysteine. The [live L-methionine-cycle definition and parent relations](https://amigo.geneontology.org/amigo/term/GO:0033353) explicitly include this
interconversion. The [homocysteine-metabolism parent page](https://amigo.geneontology.org/amigo/term/GO:0050667) places GO:0071269 and
GO:0033353 as separate children; the sulfur-amino-acid and L-amino-acid
biosynthesis parent pages independently show GO:0071269 beneath them. Direct
child-page requests failed, so no claim of an exhaustive live relationship
export is made. The [curated HAMAP AdoHcyase rule](https://hamap.expasy.org/rule/MF_00563) explicitly maps SAH hydrolysis to
GO:0071269. The local Pseudomonas `ahcY` source has that HAMAP assignment;
yeast MET17 in the primary GO-CAM browser and HSU1 in the indexed UniProt
record provide other direct homocysteine-forming enzyme comparators. This is
positive annotation practice for the performer role, not a proposed gap based
on absent annotations. The local GO-CAM index contains no human P23526 activity.
The proposal describes L-homocysteine formation, not human de novo methionine
biosynthesis. The two earlier cores are merged into one catalytic unit with
two process contexts, rather than presenting the same MF twice.

### Localization and interaction evidence

PMID:28647132 explicitly states endogenous nuclear and cytoplasmic localization.
Its abstract does not quantify a universal minor nuclear fraction. Both nuclear
rows are now ACCEPT as an established compartment of the enzyme, and the single
core includes nucleus and cytosol. The ER claim has explicit UniProt provenance
to the same paper, but its relevant experiment is outside the accessible abstract;
both ER rows remain UNDECIDED pending that result. This does not assert absence.
The broad cytoplasm and cytosol source assertions remain at their stated resolution.

The melanosome source is PMID:17081065; its stage-resolved fraction-MS abstract
names selected validation targets but does not expose AHCY's peptide record.
Likewise, PMID:19056867 (human urinary exosomes), PMID:20458337 (B-cell exosomes)
and PMID:23533145 (expressed-prostatic-secretion urinary exosomes) establish
sample-level proteomics without exposing the AHCY-specific identification in the
available extraction. These four annotations are UNDECIDED. The previous
categorical contamination/co-isolation explanations are withdrawn: cytosolic
abundance does not disprove an extracellular or organellar pool, and a separate
compartment-specific catalytic function is not required for localization.

Seven generic GO:0005515 rows now use REMOVE under the explicit binding policy,
without rejecting any interaction. Their source-specific partners are traced:
ANKRD40/Q6AI12, APPBP2/Q92624 and C1orf50/Q9BV19 in the 2014 binary map; the
first and third in the 2015 variant screen, 2017 BioPlex map, 2019 variant map
and 2021 BioPlex maps; C1orf50 alone in HuRI; ANKRD40 in OpenCell. Source
methods and accessible Results were checked, but individual AHCY pair/allele
supplementary rows remain uninspected. No adapter, inhibitor or partner-specific
function is invented from these records. The separately studied AHCYL1 and FTO
interactions are not substituted as if those were the partners in these sources.

### Additional primary mechanistic context

[PMID:33328229](https://pubmed.ncbi.nlm.nih.gov/33328229/) was verified through
PubMed abstract/figure captions and indexed original PMC7744083 Results. Nuclear
fractionation, endogenous BMAL1 association and chromatin recruitment primarily
use mouse liver/MEFs. Human U2OS depletion affects reporter amplitude; 293T
transfection supports co-IP. This strengthens the functional nuclear context
without assigning methyltransferase activity or proposing circadian-process NEW.

[PMID:41549122](https://pubmed.ncbi.nlm.nih.gov/41549122/) was checked against
PubMed, indexed original PMC12848013 Results and the
[publisher PDF](https://www.nature.com/articles/s41422-025-01213-5.pdf).
Recombinant binding and hydrolase-retaining separation mutants support a distinct
adenosine-dependent AHCY/FTO mechanism in tumor models. The authors exclude
intrinsic methyltransferase activity. The publisher records replacement of
incorrect supplementary Figures S4 and S7 on **2026-09-10**; the corrected panels
were not independently compared. This is a correction, not a retraction. The
mechanism is acknowledged in prose and an expert question; it does not replace
the catalytic core or create a new universal role. Broader physiological and
assembly-state scope remains a question.

The standalone biological summary no longer labels nuclear AHCY universally
minor or conflates all methylation effects with SAH turnover. Disease context
remains enzyme-deficiency biology, not treatment advice. Final validation,
independent review, notes-inclusive source gates and exact publication manifest
are recorded after the draft is stable.

### Final source recovery and independent review, 2026-09-27

The later primary-source recovery below supersedes the earlier same-session ER
and urinary-exosome uncertainty. Independent reviewer annotation_a4galt recovered
the author manuscript of [PMID:28647132](https://www.researchgate.net/publication/316917659),
which I also opened and checked. Results/Figure 6F show mCherry-AHCY colocalization
with GFP-calreticulin 1 in HEK293T cells. Both ER assertions are now NON_CORE,
scoped to ectopic expression without membrane-topology or lumen claims. Figure 1A
provides endogenous U2OS nuclear/cytoplasmic localization.

Both reviewers independently recovered indexed original
[PMC2637050 Table 1, PMID:19056867](https://pmc.ncbi.nlm.nih.gov/articles/PMC2637050/):
AHCY has 10 unique peptides and 28 spectra (the Pep and ID columns). This supports
the corresponding urinary-exosome HDA as NON_CORE at the preparation's resolution,
without claiming extracellular catalytic activity or exosome biogenesis.
The author retains the cached abstract quote as sample context; numerical target
evidence is explicitly attributed to the external primary table. Local cache
full-text flags for both papers remain unavailable.

The independent reviewer also read the melanosome
[coauthor-hosted main PDF](https://proteininformationresource.org/pirwww/about/doc/J_proteome_res_Chi2006.pdf)
and [B-cell exosome author manuscript](https://www.researchgate.net/publication/44588150).
The latter describes centrifugation, sucrose flotation and anti-MHCII purification,
with at least two unique peptides in two of three experiments for the protein list.
AHCY's supplementary rows were not recovered for either source or PMID:23533145.
These three source-specific uncertainties remain; no contamination claim is made.

The prior authored NEW GO:0071269 is retained with **IC**, not IDA. The explicit
supporting entity is GO:0004013, the established human IDA catalytic annotation
whose original PMID:10933798 is retained. The human curated reaction establishes
that AHCY performs the product-forming step. This is an inference from an existing
experimentally supported MF, not a claim that I read a new direct human hydrolysis
assay in the conformational-study abstract. The [official GO IC guidance](https://geneontology.org/GO_REF/0000036)
permits reuse of the supporting annotation's primary reference for a single-source
inference; its special multiple-source GO_REF is not assigned here.
The schema's supporting_entities records GO:0004013. The comparator, performer,
parent and local GO-CAM checks above remain the basis for the process scope.
All 25 machine-seeded assertions are unchanged; only the prior authored NEW's
evidence code and supporting entity are revised outside review objects.

Root independently read all 26 decisions, all 23 reference assessments and the
integrated core; it accepted the IC correction and recovered source-scoped
ER/exosome refinements. Final action counts are 12 ACCEPT, 3 KEEP_AS_NON_CORE,
7 REMOVE, 3 UNDECIDED and 1 NEW. The independent consultation involved no edits.

Final targeted validation passed with two warning groups: uncached YAML citations
PMID:33328229 and PMID:41549122, plus differing exosome actions across sources.
The latter is intentional: one target identification was recovered while two
remain unresolved. History validation and HTML rendering passed. The explicit notes-inclusive audit additionally retains
PMID:9586999, PMID:12590576, PMID:15024124 and PMID:19177456 as missing-source
gates: six total. No cache was fabricated or rewritten. Status remains DRAFT.
All 25 seeded source objects, 20 original reference id/title pairs, UniProt and
GOA bytes passed preservation checks; this notes file retains its original
content as an unchanged prefix. All five baseline blobs also match current main
`d2d8c9043b082a62378eff620ec0122d4118173b`. The final four-file publication manifest
is `/tmp/AHCY-local-manifest.json`; no Git or remote mutation was performed.
