# AKR1D1 (P51857) review notes

## Identity
- Human AKR1D1 = aldo-keto reductase family 1 member D1; a.k.a. 3-oxo-5-beta-steroid
  4-dehydrogenase; Delta(4)-3-ketosteroid 5-beta-reductase; Delta(4)-3-oxosteroid
  5-beta-reductase; gene synonym SRD5B1. EC 1.3.1.3.
- 326 aa, cytosolic (SUBCELLULAR LOCATION: Cytoplasm ECO:0000269|PubMed:7508385).
- Highly expressed in liver; also testis, weakly colon [file:human/AKR1D1/AKR1D1-uniprot.txt
  "Highly expressed in liver. Expressed in testis and"].

## Core molecular function
- NADPH-dependent stereospecific reduction of the C4-C5 (Delta4) double bond of
  3-oxo-Delta4 steroids to the 5-beta configuration, producing the A/B cis-ring
  junction characteristic of bile acids.
  [file:human/AKR1D1/AKR1D1-uniprot.txt "Catalyzes the stereospecific NADPH-dependent reduction of the"
   ... "C4-C5 double bond of bile acid intermediates and steroid hormones"]
- The specific, informative MF term is **GO:0047787 Delta4-3-oxosteroid 5beta-reductase
  activity** (present in GOA as IEA GO_REF:0000120 via EC:1.3.1.3 + RHEA). This is the
  CORE MF. The GOA also carries family-level GO:0004032 aldose reductase (NADPH) activity
  (IBA) — this is an over-annotation / less-informative parent-family activity; human
  AKR1D1 has only 50% identity to aldose reductase and is a 5-beta-reductase, not an
  aldose reductase [PMID:7508385 abstract: "50% overall identity with ... human aldose reductase"].
- Broad steroid substrate range C18–C27: bile acid intermediates (7alpha-hydroxy- and
  7alpha,12alpha-dihydroxy-cholest-4-en-3-one), and steroid hormones (testosterone,
  cortisol, cortisone, progesterone, androstenedione, aldosterone, corticosterone).
  UniProt lists many Rhea catalytic-activity reactions all EC 1.3.1.3.

## Biological process
- Bile acid biosynthesis (GO:0006699): reduces the CYP7A1/CYP8B1 products
  7alpha-hydroxy-4-cholesten-3-one and 7alpha,12alpha-dihydroxy-4-cholesten-3-one to the
  5beta-cholestan-3-one intermediates, giving bile acids their 5beta (cis) A/B ring.
  [PMID:7508385 "high activity toward the bile acid intermediates 7 alpha,12 alpha-dihydroxy-4-cholesten-3-one and 7 alpha-hydroxy-4-cholesten-3-one"; "more important for bile acid biosynthesis than for metabolism of steroid hormones"]
  Reactome models 6 5beta-reduction steps in bile acid synthesis (R-HSA-192033, -192067,
  -193746, -193755, -193821, -193824) plus 3 pathway-level nodes (R-HSA-193368, -193775,
  -193807).
- Steroid hormone metabolism (androgen/C21 steroid) — secondary; the human enzyme has a
  narrower steroid-hormone activity than rat [PMID:7508385 "substrate specificity of the
  human enzyme is considerably narrower than that of the rat enzyme"].

## Disease
- Congenital bile acid synthesis defect type 2 (CBAS2, MIM:235555; AKR1D1 deficiency):
  neonatal jaundice, intrahepatic cholestasis, hepatic failure; low chenodeoxycholic and
  cholic acid. [file:human/AKR1D1/AKR1D1-uniprot.txt "A condition characterized by jaundice, intrahepatic cholestasis and"]

## Annotation decisions summary
- KEEP AS CORE: GO:0047787 (Delta4-3-oxosteroid 5beta-reductase activity, the specific MF);
  GO:0006699 bile acid biosynthetic process (IDA PMID:7508385, Reactome TAS, InterPro IEA);
  GO:0005829 cytosol (IDA HPA, IDA PMID:7508385, Reactome TAS); GO:0016229 steroid
  dehydrogenase activity (IBA — reasonable parent, but keep specific MF as core).
- MODIFY: GO:0004032 aldose reductase (NADPH) activity (family-level IBA) → replace with
  GO:0047787. GO:0016491 oxidoreductase (too general) → GO:0047787.
- MARK_AS_OVER_ANNOTATED: GO:0047086 ketosteroid monooxygenase (IBA family term; AKR1D1 is
  a reductase not a monooxygenase); GO:0008106 alcohol dehydrogenase (NADP+) (Reactome/ARBA
  mechanistic label for the reduction reactions — the reaction reduces a C=C double bond,
  not an alcohol/aldehyde; less informative than 5beta-reductase); GO:0072582
  17beta-HSD(NADP+); GO:0005515 protein binding (2 IPI, BioPlex AP-MS, AKR1C1) — bare,
  uninformative; GO:0008202 steroid metabolic / GO:0042445 hormone metabolic /
  GO:0032787 monocarboxylic acid metabolic (ARBA broad BP); GO:0008207 C21-steroid,
  GO:0008209 androgen metabolic (human enzyme steroid-hormone activity minor vs bile acids);
  GO:0006707 cholesterol catabolic (bile acid synthesis is downstream of cholesterol but
  AKR1D1 does not act on cholesterol itself); GO:0007586 digestion (too indirect/downstream).
- KEEP_AS_NON_CORE: GO:0005737 cytoplasm (broader CC, redundant with cytosol; keep).

## Provenance
- No falcon deep-research file (provider out of credits). Grounded in
  AKR1D1-uniprot.txt, AKR1D1-goa.tsv, cached PMID_7508385 (abstract only),
  PMID_28514442/PMID_33961781 (BioPlex AP-MS), and cached Reactome R-HSA-* nodes.
</content>
</invoke>

## 2026-09-20 full-gene re-review

Read every source annotation and relevant evidence, including primary full texts for disputed reactions and the exact PAINT target path. See [AKR1D1-primary-source-checks.md](AKR1D1-primary-source-checks.md) for assay context, access limits, short exact excerpts, and pending focused adjudication. All original source fields are preserved; no NEW annotation is added. Broad true chemistry and localization are retained separately from exact substrate/reaction conflicts.

## 2026-09-27 ClinGen Mendelian substantive audit

This entry supersedes earlier functional judgments where they differ, including the early broad-process over-annotation claims, the description of aldose reduction as merely a less-specific synonym of steroid reduction, and the earlier provider-access description. Historical notes, the September 20 source audit, PAINT lineage and genuine OpenScientist artifacts remain unchanged as provenance.

Identity: the authoritative HGNC snapshot has approved AKR1D1, HGNC:388, previous symbol SRD5B1. The live [UniProt P51857 record](https://www.uniprot.org/uniprotkb/P51857/entry) confirms the human protein and synonym. Canonical/historical directories and open PR searches found no overlap. Parent verified all 11 gene files against main `c7078166039c9abd5c62704489283403eb520007`; an older local HTML rendering was backed up and restored to exact main before authoring. The baseline was INITIALIZED, with 41 reviewed source rows, 25 references and three isoforms. Every original annotation source object and reference identity/title is preserved, including the unresolved Reactome title placeholder. No NEW annotation is added.

### Primary evidence and reaction boundaries

Cached full human studies PMID:21255593 and PMID:18407998 were independently read. The kinetic study uses purified human recombinant enzyme, TLC product comparison with authentic standards, cofactor fluorescence titration, substrate kinetics and inhibition assays. It directly identifies 5beta products for the tested C18-C27 substrates except aldosterone; aldosterone turnover is observed but its product is inferred because an authentic standard was unavailable. Substrate inhibition varies by structure, and the authors discuss how single-concentration/cell preparations contributed to older discrepancies. These results support direct participation in androgen and C21 hormone metabolism alongside bile acid synthesis, without measuring each substrate's share of flux in vivo. [PMID:21255593](https://pmc.ncbi.nlm.nih.gov/articles/PMC3056882/). Product formation was demonstrated across the tested steroid panel apart from aldosterone; this does not establish every derivative in those carbon-number ranges.

PMID:18407998 structures resolve NADP+/steroid complexes and the Tyr58/Glu120 environment; mutant assays use testosterone reduction. Steroid binding is retained as integral substrate recognition. These experiments explain double-bond reduction while retaining the 3-oxo group, not a universal negative result for every sugar or alcohol-forming substrate. [PMID:18407998](https://pmc.ncbi.nlm.nih.gov/articles/PMC2423251/), "Each steroid carbonyl accepts hydrogen bonds from catalytic residues Tyr 58 and Glu 120 ."

The original human cDNA/COS-cell study [PMID:7508385](https://pubmed.ncbi.nlm.nih.gov/7508385/) remains abstract-only and its full assays were not recovered. Positive bile-acid-intermediate, cortisol and testosterone reactions are retained, while its progesterone/androstenedione negatives are explicitly preparation/condition-specific. Original localization assertions retain curator deference plus independent UniProt, HPA and Reactome corroboration; no fractionation/imaging method is invented from the abstract. Digestion remains UNDECIDED: GO:0007586 concerns breakdown of ingested nutrients, whereas the exposed assay measures bile-acid-precursor reduction. The complete source could provide additional context.

The [PMID:11342103 primary abstract](https://pubmed.ncbi.nlm.nih.gov/11342103/) explicitly uses human AKR1D1 stably expressed in HEK293 cells. UniProt maps RHEA:53484, androst-4-ene-3,11,17-trione to the C17-hydroxy product, to this paper. Exact product/controls were not exposed in the abstract and the original full body could not be recovered. Both this 17beta-HSD mapping and the ARBA alcohol-dehydrogenase assertion remain UNDECIDED. A possible endogenous cell-enzyme contribution is a question, not an established contaminant or refutation. Citation identity and the study's positive broad scope are VERIFIED; the particular side reaction remains unresolved.

The [PMID:21232532 primary abstract](https://pubmed.ncbi.nlm.nih.gov/21232532/) describes expression/IHC of progesterone-metabolizing enzymes, explicitly including AKR1D1. Its title/low expression finding cannot establish an absent monooxygenase assay elsewhere in the full paper. Publisher/full-source recovery failed. The monooxygenase IBA remains UNDECIDED, as does ancestral aldose reduction. A bounded independent annotation_aars1 consultation checked both abstracts/UniProt and attempted full-source recovery, supporting these access-qualified judgments.

### Reactome, propagation and synthesis

Eight existing Reactome caches were read, separating pathway summaries from reaction equations. Five cached reduction events retain a 3-oxo steroid carbonyl and therefore support GO:0047787 rather than GO:0008106. A new indexed primary retrieval recovered the sixth **human** record [Reactome:R-HSA-193755](https://reactome.org/content/detail/R-HSA-193755), including the complete triol-steroid equation, NADPH, AKR1D1 catalyst, cytosol and PMID:7508385. It is likewise C4-C5 reduction, so the sixth MF row now receives the same source-specific MODIFY. Direct web retrieval returned 404 and the standard cache function failed DNS; the indexed human record supplies positive evidence without inventing a replacement identifier or cache. Raw evidence: `/tmp/AKR1D1-193755-primary-evidence.json`. The original title placeholder remains pending normal machine cache recovery.

GO definitions/parents were checked through local OAK. GO:0016229 means steroid-substrate redox chemistry and is retained as an informative family-level assertion, without requiring carbonyl/alcohol conversion. Generic GO:0016491 is refined to the experimentally resolved double-bond reductase. Broad cytoplasmic localization is retained at source resolution. GO:0006707 and monocarboxylic-acid metabolism encompass pathways in which AKR1D1 directly performs an intermediate step; it need not consume cholesterol or a free acid itself. Live AmiGO requests timed out; no unverified label/obsoletion change is claimed.

The preserved PAINT lineage was read in full: PTN000198921 grounds aldose reduction/cytosol; PTN000199026 grounds steroid dehydrogenase/monooxygenase; PTN000199134 grounds androgen metabolism. The target P51857 path and IBD rows are explicit. Its own androgen/cytosol experiments are legitimate descendant grounding, not circularity. No new tree/MSA reconstruction or target-specific loss is claimed. Propagation blocks trace all IBA/IEA proximate sources; unread ARBA predicates remain UNRESOLVED even where independent human biology supports the annotation. UniProt Rhea equations were checked individually, including physiological reduction when a reaction is written in reverse. No matching AKR1D1 GO-CAM index entry was found.

BioPlex PMID:28514442 and PMID:33961781 were read at cached methods/full-section scope. The seeded partner is Q04828/AKR1C1; the exact pair supplement was not independently extracted. Generic binding is removed because no informative specific MF is established, without asserting noninteraction. The latter cache has partial full-text sections despite a true availability flag, which does not imply all tables/results were examined.

Two prior activity-identical cores are consolidated into one cytosolic NADPH-dependent steroid 5beta-reductase core covering bile-acid synthesis, cholesterol breakdown and hormone metabolism. Steroid recognition is incorporated in its description. No extra process, cofactor-binding annotation, isoform specificity, transport function or redundant NEW is manufactured.

### Research provenance and publication gates

The genuine prior OpenScientist report and PDF/HTML/citation artifacts were read and preserved. Its conclusion that steroid specialization excludes other chemistry is stronger than its acknowledged lack of direct negative assays/full donor papers, and is not adopted. Its sequence alignment was not independently rerun. A fresh normal Falcon request and perplexity-lite fallback used isolated `/tmp/AKR1D1-fresh-research/AKR1D1/` output. A launcher import typo failed before any invocation and was corrected. Both genuine provider commands then exited 2 during uvx dependency retrieval because PyPI DNS failed; no provider ran and no new report exists (`/tmp/AKR1D1-fresh-research.log`).

Parallel normal caching found all seven existing review PMIDs cached. Six missing records in preserved provider artifacts were requested normally: PMID:26418565, PMID:30254413, PMID:31337596, PMID:36739965, PMID:38034430 and PMID:41387259. All six attempts failed DNS and produced no cache (`/tmp/AKR1D1-fetch-provider-citations.log`). Several identities were independently verified through primary PubMed; these clinical/mutant leads are not substituted for the decisive substrate assays. Reactome:R-HSA-193755 remains absent after standard `cache_reactome_pathway` retrieval (`/tmp/AKR1D1-fetch-reactome.log`). DRAFT is retained for these notes/provider-inclusive source gates. Local full-text flags reflect cache metadata/content, not external reading. Final checks and independent review are recorded in the handoff manifest.

Final independent parent review read all 41 decisions, 25 reference assessments, the integrated core, questions and saved human Reactome equation; no biological change was requested. Targeted validation, history validation and rendering pass. The sole advisory reflects the deliberate GO:0008106 distinction between six resolved Reactome mapping corrections and the unresolved independent ARBA side activity. All 57 supporting snippets match their cached sources exactly after case-sensitive whitespace normalization. All source objects, three isoforms, reference identities and eight protected artifacts are unchanged. The final citation census separates the six notes/provider gaps from unused bibliography-only entries in the immutable UniProt record.


## 2026-09-27 — source5 recovery and PR #3266 follow-up

The live PR remained draft at `4e543bbf4191a0a39ee6edfccd2d042ad1c6f6dd` before
editing. All 11 canonical gene/artifact files and the published history matched
that exact head. The 41 source assertions, three isoforms, original reference
identities, all action decisions and the single core are preserved. Seven
reference assessments are added: six previously cited provider records and the
reviewer's already-cached mechanistic source, PMID:20522910.

The [normal source5 recovery run](https://github.com/ai4curation/ai-gene-review/actions/runs/36295820535)
ran at `60c5e96f8317dd1e7d8325242d8037b81e272c59`. Artifact 10926007634 has ZIP
SHA256 `cd022c3e045b00798f8e29ff86904be885a4ed9e8b539ba11d44f6b954149400`.
The independently verified import copied these records unchanged:

- PMID:26418565: SHA256 `736edb02fc30da0e99d9100edf54a014ebe0c64d5eb41d08ab45ef212bf6dc81`.
- PMID:30254413: SHA256 `e0277829914bf18588b0e7db2953dac76696540a2a59ca3760e1a404ecd575dd`.
- PMID:31337596: SHA256 `ef5c0c8295e51bb7d45637a47bbddae5e2769e69ad198e2cdb40813efd153594`.
- PMID:36739965: SHA256 `17dc234a6a4ba2fcb89f459ecc52c35e1a62544f2f3c5e41573b7de40ccef74c`.
- PMID:38034430: SHA256 `171a5fed7afadd595fa550d1e580c25ab375d33f05c0087531d149f83187d28e`.
- PMID:41387259: SHA256 `27012c7018585e3c846c00dbbdc4f00cfb73cbc4b73e487449fd8d71d85d076a`.

### Recovered evidence and limits

PMID:26418565 has extracted full Methods, Results and Discussion. Human WT and
P133R proteins were expressed in E. coli and purified using affinity plus Blue
chromatography. Cortisone and 7alpha-hydroxycholest-4-en-3-one assays, cofactor
fluorescence/chase measurements and steroid-binding titrations show diminished
P133R chemistry and cofactor affinity. The numerical effects depend on buffer,
substrate and cofactor occupancy. This source explicitly corrects the earlier
PMID:20522910 conclusion of unchanged cofactor affinity: substantial bound
NADP+ in the older WT preparation obscured the comparison. The later cofactor-
free preparations reveal the affinity difference. The narrow historical finding
is now machine-readably OVERTURNED with exact later-source support. The older
study still supports reduced mutant protein/activity; purified P133R results
are not generalized to every mutant. Neither study resolves the aldose,
monooxygenase or C17-side-activity source gaps.

PMID:30254413 has extracted full clinical case/discussion text. Genetic findings
and urinary profiles support disease context, but the R307C structural model
is predictive and the first urine profile was obtained after treatment. It
provides no purified variant-specific catalytic measurement. PMID:38034430 has
full case-series Methods/Results/Discussion: three of five patients lacked liver
dysfunction despite variants/atypical bile acids. The proposed MRP3 compensation
is explicitly a hypothesis; short follow-up and absent follow-up biopsy limit
clinical conclusions. Neither observation negates AKR1D1's established reaction.

The other three recovered records are abstract-only. PMID:31337596 distinguishes
three AKR1D1 cases from three CYP7B1 cases; the CYP7B1 allele-frequency and CDCA
response results are not assigned to AKR1D1. PMID:36739965 supports an RNA/splicing
mechanism from liver RNA and a minigene experiment, not a purified catalytic
assay. PMID:41387259 reports one fatal infant case with biochemical/genetic
support; its screening suggestion is an author proposal. The three full-body
records have `full_text_unavailable: false`; these three abstracts and the
existing abstract-only PMID:20522910 have `full_text_unavailable: true`.

### Current review suggestions

[Review comment 5853621026](https://github.com/ai4curation/ai-gene-review/pull/3266#issuecomment-5853621026)
approved the biology and offered optional refinements. PMID:20522910 is now
explicitly assessed, with the later cofactor correction recorded rather than
repeated as a current fact. The aldose reason explicitly acknowledges the
C5-oriented hydride-transfer geometry in full PMID:18407998. That positive
structural explanation supports steroid specialization but does not replace a
substrate-specific negative assay or resolve the inherited donor evidence.
Likewise, the known NADPH reductase mechanism does not independently adjudicate
the unread oxygen-insertion experiment. UNDECIDED is retained for those rows.

The steroid-dehydrogenase IBA retains its informative ancestral steroid-substrate
class; the generic oxidoreductase signature lacks that substrate restriction.
The exact 5beta reaction remains separately represented. Monocarboxylic-acid
metabolism remains core pathway participation: AKR1D1 performs a chemical step
in making monocarboxylic bile acids, and its immediate substrate need not already
carry the product's acid group. The number of non-core decisions in other gene
reviews is not biological evidence for changing this process judgment.

### Remaining source gate and recursive census

Reactome:R-HSA-193755 was not recovered: the local attempt failed DNS, and the
hosted source5 normal call returned 1 without an output record. A direct page
404 does not prove that the event never existed or establish a replacement ID.
The original GOA identifier and machine-fetched title placeholder are retained.
The earlier indexed primary **human** page explicitly identifies the reaction
of 4-cholesten-7alpha,12alpha,24(S)-triol-3-one with NADPH to yield the corresponding
5beta steroid and NADP+, and identifies AKR1D1 in cytosol. This retained-carbonyl
equation supports the existing reaction-specific MODIFY; its indexed primary
verification is separate from cache availability. The absent cache remains a
draft gate. No authored Reactome substitute is created.

The recursive census includes YAML, both source-note files, PAINT JSON and all
unchanged OpenScientist Markdown/citation/HTML/PDF artifacts. URL/HTML decoding,
Markdown escape normalization and PDF text extraction find no additional
DOI-only work in those retained artifacts. With PMID:20522910, all 14 cited
PMIDs are cached; eight of the nine Reactome records are cached, leaving only
R-HSA-193755. The immutable UniProt bibliography is distinguished from the
review/provider citations. The preserved hypothesis report's stronger chemical
exclusions are not adopted, and none of its sequence analysis is represented
as newly rerun.

Final checks for this follow-up passed: targeted validation exited 0 with the
existing evidence-specific GO:0008106 action advisory; history validation and
rendering passed. The independent integrity check confirms all 41 source
objects/actions, three isoforms, the core, 25 original reference identities,
eight protected artifacts and both published history records unchanged. All
60 quoted snippets match actual cached text after case-sensitive whitespace
normalization. The PDF census additionally examines all 33 annotation URI
links and both pypdf and pdftotext extraction, and the HTML scan includes raw
link targets. Exact current-main cache metadata and blob checks distinguish
the six new source5 records from already published sources. These checks do
not resolve the remaining Reactome cache gate or the source-specific biological
uncertainties retained in the annotations.


## 2026-10-03 — AKR1C1 association evidence

The BioPlex 2.0 and 3.0 experimental annotations report AKR1D1 association with
AKR1C1 (UniProt Q04828; PMID:28514442 and PMID:33961781). Both associations are
retained as non-core. BioPlex 2.0 used tagged human proteins and affinity-purification
mass spectrometry in HEK293T cells; BioPlex 3.0 profiled 293T and HCT116 networks.
The latter study's general two-cell-line design does not establish that the exact
AKR1D1 pair was observed in both lines.

The experimental GOA partner and UniProt interaction record corroborate the pair.
The assay framework was inspected, but the individual supplementary target records
were not independently inspected. These data support co-complex association without
establishing purified binary affinity, a native liver interaction or a specific
effect on steroid metabolism. They provide no basis for assigning AKR1C1 catalytic
activity to AKR1D1. The earlier removal rationale addressed only the annotation's
breadth; it did not identify evidence contradicting the association.

This correction changes only the two association judgments and their accompanying
reference explanations. The steroid-reductase core, the remaining source-specific
uncertainties and the missing R-HSA-193755 cache remain as previously recorded.
The separately planned normal-fetch diagnostic has no outcome incorporated here.

## 2026-10-03 — Reactome diagnostic outcome (20:16 UTC)

The previously pending diagnostic is now complete. One invocation of the unchanged
normal Reactome fetcher requested
[R-HSA-193755](https://reactome.org/ContentService/data/query/R-HSA-193755)
at 20:16:04–05 UTC. The request returned HTTP 404 without redirects. Its complete
180-byte JSON response reports that the requested identifier was not found. The
normal fetch failed and produced no Reactome cache file; no substitute source was
created. The diagnostic is recorded in the
[source run](https://github.com/ai4curation/ai-gene-review/actions/runs/37149949648).

The indexed official [human reaction page](https://reactome.org/content/detail/R-HSA-193755)
still describes AKR1D1-catalyzed reduction of the steroid double bond. Current direct
access to that detail page returned 404, and access to its schema-browser page
returned 403. These access results do not establish that the event was retired,
renamed or biologically incorrect. The existing reaction-specific assessment is
unchanged; the required normal-cache source remains unavailable and campaign
completion remains pending. No further fetch was attempted.


## 2026-10-03 — Association evidence and current source access

The two experimental BioPlex annotations remain non-core associations with AKR1C1
(Q04828). Each raw GOA row records IPI evidence and that partner; the UniProt IntAct
entry lists the same pair with three experiments. The revised rationales put these
positive observations first. Short, complete primary excerpts now anchor the
coassociation result in PMID:28514442 and the AP-MS interaction-network context in
PMID:33961781. Neither excerpt is presented as a read of the exact pair's
supplementary record. That record remains uninspected, and no observation in both
cell lines, direct binary affinity, native liver association or specific steroid
metabolic consequence is asserted.

The [ClinGen curation instructions](https://github.com/ai4curation/ai-gene-review/blob/main/projects/CLINGEN_MENDELIAN.md#curation-instructions)
record the user's explicit direction to retain supported generic binding as
KEEP_AS_NON_CORE when an evidence-backed finer term is unavailable. That instruction
takes precedence for this task over the annotation-reviewer skill's general
informational-exclusion recommendation. It does not turn an uninspected target
table into verified evidence or authorize a new molecular activity. The two
decisions rely on the experimental curator records and the corroborating UniProt
association, with the primary assay context and access limits stated above.

The Reactome reference assessment is now UNVERIFIED. Earlier wording about the
reaction came from an indexed official snippet, not successful access to the
current complete event. The already recorded single normal-fetch diagnostic
returned HTTP 404 and no cache; direct page and schema-browser access returned 404
and 403. No identifier replacement or retirement is established. The normal-cache
source gate remains unresolved, and this follow-up does not complete AKR1D1 in the
campaign. No additional fetch was performed. All annotation actions, machine
source fields, products and the steroid-reductase core remain unchanged.

## 2026-10-05 - OpenScientist redox follow-up

Evaluated `AKR1D1-hypotheses/aldose-monooxygenase-and-alcohol-reduction-specificity/openscientist.md`.
The focused report usefully highlighted residue-level specialization and AKR
reaction-class constraints, but its broad removal posture still goes beyond
directly checked target evidence for weak side activities.

PMID:22437839 was fetched and registered as target-specific support that the
Glu120/His120 switch distinguishes AKR1D1 5-beta-reductase chemistry from the
AKR1C hydroxysteroid dehydrogenase reaction geometry. GO:0047086 was removed
because AKR1D1 transfers hydride to the C4-C5 double bond and offers no
oxygen-insertion mechanism for ketosteroid monooxygenase activity, even though
the exact AKR1C1/C2/C3 donor assays from PMID:21232532 still need full-text
review. Ancestral aldose reduction remains unresolved because purified AKR1D1
negative aldose assays were not located.


## 2026-10-09 — R-HSA-193755 recovered from an official historical release

The missing event is now available as authentic historical source material. The
complete [Reactome release 89 human SBML archive](https://download.reactome.org/89/homo_sapiens.3.1.sbml.tgz)
contains reaction `reaction_193755` in pathway member `R-HSA-193775.sbml`.
Its exact title, input/output entities, AKR1D1 catalyst mapped to UniProt P51857,
cytosol compartment, and literature links were read directly from the XML.
The [unaltered source member](../../../reactome/R-HSA-193755-source/Reactome-v89-R-HSA-193775.sbml)
and [machine-generated extraction/provenance](../../../reactome/R-HSA-193755-source/provenance.json)
are retained alongside the [generated cache](../../../reactome/R-HSA-193755.md).
The archive SHA256 is `d3c99ec42c7fcf5a582b67d6a4a4dcdadbe5e448d5c6b2c4fe81338e763bca61`;
the member SHA256 is `4eda3a450b1b457917234329d64bf2feaf29addbc0716e569b2aa738866369fd`.
The XML identifies itself as release 89, generated in June 2024. The cache uses
the existing Reactome formatter with machine-extracted stable ID, title and
summary. No current API success is implied: the release-97 ContentService and
detail page still return 404 for this event, and no deletion or replacement
history has been recovered.

The archived equation's input is a Delta4 steroid and its output is the saturated
5beta steroid while the 3-one remains. This supports the existing refinement to
[GO:0047787](https://www.ebi.ac.uk/QuickGO/term/GO:0047787), rather than the alcohol/ketone
chemistry of [GO:0008106](https://www.ebi.ac.uk/QuickGO/term/GO:0008106).
Historical labels drifted: release 89 exports GO:0004033 and EC 1.1.1, whereas
the later indexed event labels GO:0008106. The original GOA term, qualifier,
TAS evidence and Reactome ID remain untouched. The source summary itself uses
cholesten inconsistently in one product sentence; the title and explicit output
entity identify the saturated cholestan product. The cache preserves that source
text rather than silently repairing it.

The event links [PMID:7508385](https://pubmed.ncbi.nlm.nih.gov/7508385/) and
[PMID:12543708](https://pubmed.ncbi.nlm.nih.gov/12543708/). The former was inspected
as an abstract: human cDNA expressed in COS cells supports reduction of related
7alpha-hydroxy and 7alpha,12alpha-dihydroxy bile acid precursors. The latter is a
broad 2003 review, accessed only as an abstract. Neither access scope establishes
an independently inspected primary assay of this exact 24(S)-hydroxylated triol.
Selected full Methods and Results of [PMID:21255593](https://pubmed.ncbi.nlm.nih.gov/21255593/)
support the molecular-function class using purified human AKR1D1, NADPH, product
comparison and substrate-dependent kinetics; their general substrate-range
result is not substituted for an exact-substrate assay. Historical reaction
identity and human enzyme activity are therefore supported, with the exact
substrate assay limitation retained.

The archived AKR1D1 species is located in cytosol (GO:0005829). Its steroid
input starts in the ER membrane; this does not locate the enzyme there or
establish transport by AKR1D1. The source explicitly leaves the translocation
mechanism unresolved. Both affected annotation actions remain unchanged:
MODIFY for the enzyme-class mapping and ACCEPT for cytosol. No NEW function,
other annotation change, or current-event replacement is proposed.

This entry supersedes the earlier search-only provenance description. It
provides the durable, machine-derived event evidence requested by the prior
review. The archived cache and original SBML address that historical source
gate; successful retrieval of the current API is not claimed or required to
verify this archived event. DRAFT remains the status calculated by the normal
validation workflow. Campaign completion still requires this follow-up to
receive review approval and merge. No further repeated live retrieval is
necessary to assess the historical event supplied here.

## 2026-10-09 — focused citation follow-up to PR #4465

The recovered [Reactome reaction](../../../reactome/R-HSA-193755.md) now has
a brief direct localization excerpt on its cytosol annotation. The same source
already supplies the reaction-catalyst excerpt on the molecular-function
refinement. Both passages were checked against the unchanged historical cache.

The molecular-function refinement also now quotes the specific double-bond
reduction chemistry described in the abstract of
[PMID:21255593](https://pubmed.ncbi.nlm.nih.gov/21255593/). The core-function
evidence retains the single product-identification excerpt from that study.
Repeated copies of that product-range excerpt elsewhere in the YAML were
consolidated, while their citations and all biological reasons remain. The
notes' duplicate was paraphrased above. This keeps the two complementary
anchors available without repeating the same quotation throughout the review;
it does not imply that the historical 24(S)-triol was directly assayed in that
paper. The exact-substrate limitation remains in the affected reason.

This is a bounded citation edit: all original source fields, products, reference
identities, actions, reasons, replacement terms and core-function terms remain
unchanged. No publication cache, Reactome cache, archive member or provenance
record was edited. The two edited sources' excerpts were counted across YAML
and notes; unrelated inherited excerpts were outside this consolidation. The
archival source directory remains a companion to the flat Reactome cache,
containing the unaltered enclosing pathway member and machine-extracted
provenance, with their hashes retained for integrity checks.
