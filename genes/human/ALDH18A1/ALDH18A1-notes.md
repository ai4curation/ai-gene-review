# ALDH18A1 (P5CS) review notes

UniProt: P54886 (P5CS_HUMAN). Gene: ALDH18A1 (synonyms GSAS, P5CS, PYCS). HGNC:9722.
Taxon: Homo sapiens (NCBITaxon:9606). 795 aa. Evidence at protein level.

## Core biology

ALDH18A1 encodes delta-1-pyrroline-5-carboxylate synthase (P5CS), the mitochondrial
**bifunctional** enzyme that catalyzes the first two committed steps of proline and
ornithine biosynthesis from L-glutamate:

- N-terminal **glutamate 5-kinase (GK)** domain (residues 1-361): L-glutamate + ATP ->
  L-glutamyl 5-phosphate + ADP. EC 2.7.2.11 (Rhea:14877). GO:0004349.
- C-terminal **gamma-glutamyl phosphate reductase (GPR) / glutamate-5-semialdehyde
  dehydrogenase** domain (residues 362-795): L-glutamyl 5-phosphate + NADPH ->
  L-glutamate 5-semialdehyde (which cyclizes non-enzymatically to P5C). EC 1.2.1.41
  (Rhea:19541). GO:0004350.

[file:human/ALDH18A1/ALDH18A1-uniprot.txt REGION 1..361 "Glutamate 5-kinase"; REGION
362..795 "Gamma-glutamyl phosphate reductase"; EC=2.7.2.11 and EC=1.2.1.41 both
ECO:0000269|PubMed:26297558].

FUNCTION (UniProt): "Bifunctional enzyme that converts glutamate to glutamate 5-
semialdehyde, an intermediate in the biosynthesis of proline, ornithine and arginine"
[file:human/ALDH18A1/ALDH18A1-uniprot.txt, "an intermediate in the biosynthesis of
proline, ornithine"].

P5C sits at a metabolic branch point: it can be reduced to proline (by PYCR1/2/L) or
transaminated to ornithine (by OAT), and ornithine feeds the urea cycle
(citrulline/arginine). Hence the enzyme is upstream of proline, ornithine, arginine and
(indirectly) citrulline. [PMID:11092761 "critical step in the biosynthesis of proline,
ornithine and arginine"].

## Isoforms

Two isoforms by alternative splicing (2-aa insert at the GK active site):
- **Long** (P54886-1, displayed): expressed in multiple tissues; insensitive to ornithine
  feedback inhibition; makes proline from glutamate.
- **Short** (P54886-2; VSP_005215, Δ239-240): high in gut, participates in arginine
  biosynthesis; inhibited by L-ornithine (Ki ~0.25 mM).
[PMID:11092761 "P5CS undergoes alternative splicing to generate two isoforms";
"The short isoform has high activity in the gut, where it participates in"; UniProt
ACTIVITY REGULATION CC].

## Localization

Mitochondrion; specifically mitochondrial matrix (direct IDA). Forms rod/ring-like
(and stress-responsive filament) structures inside mitochondria.
[PMID:32770108 "P5CS localizes in mitochondria in rod- and ring-like patterns but
diffuses inside the"; UniProt SUBCELLULAR LOCATION "Mitochondrion matrix"
ECO:0000269|PubMed:32770108].
The Reactome "mitochondrial inner membrane" placements are historical (P5CS "associated
with the inner mitochondrial membrane", R-HSA-508040) or arise from ALDH18A1 being a
LONP1 protease substrate (R-HSA-9837978 / R-HSA-9838004, "LONP1 binds/degrades
mitochondrial inner membrane proteins"). Direct experimental evidence favors the matrix,
so inner-membrane calls are treated as over-annotated/non-core localization.

## Subunit / interactions

Forms homodimers/multimers; multimerization (not catalytic activity) governs its
sub-mitochondrial localization. [UniProt SUBUNIT "Can form homodimers/multimers";
PMID:32770108 "Multimerization (but not the catalytic activity) of P5CS regulates its
localization"; PMID:26320891 disease mutant "stable and able to interact with wild-type
P5CS" -> self-association / identical protein binding GO:0042802].
IntAct binary interactions (AGTRAP/Q6RW13, CMTM5/Q96DZ9, COQ9/O75208, DARS2/Q6PI48) come
from high-throughput two-hybrid interactome maps (PMID:25416956 HuRI predecessor;
PMID:32296183 HuRI) and are generic "protein binding" (GO:0005515) IPI with no
functional interpretation -> non-core.

## Moonlighting / secondary observations

- **RNA binding** (GO:0003723, HDA, PMID:22658674): identified in a HeLa mRNA-interactome
  capture screen that flagged many "RNA-binding enzymes of intermediary metabolism".
  Real observation but not an established function -> non-core.
- **Mitochondrial respiration / stress sensing** (PMID:32770108): P5CS knockout impairs
  organization of mitochondrial respiratory complexes and lipid/purine metabolism; P5CS
  redistributes under starvation/oxidative stress. [PMID:32770108 "P5CS is required for
  mitochondrial respiratory complex organization"]. Underlies the Ensembl-transferred
  "response to temperature stimulus" IEA (from rat ortholog); non-core / weak.
- **ATP-demand-driven filament formation** (PMID:39506109, Nature 2024): not in GOA/seed;
  noted for context only.

## Disease (all caused by ALDH18A1 variants; UniProt DISEASE CCs)

- Cutis laxa, autosomal recessive, 3A / ARCL3A (MIM:219150; De Barsy-like) — R84Q etc.
  [PMID:11092761, PMID:18478038, PMID:22170564, PMID:24767728].
- Cutis laxa, autosomal dominant, 3 / ADCL3 (MIM:616603) — recurrent Arg138 de novo
  [PMID:26320891].
- Spastic paraplegia 9A, autosomal dominant / SPG9A (MIM:601162) [PMID:26026163,
  PMID:26297558].
- Spastic paraplegia 9B, autosomal recessive / SPG9B (MIM:616586) [PMID:26026163].
Metabolic hallmark of P5CS deficiency: hyperammonemia with hypoornithinemia,
hypocitrullinemia, hypoargininemia and hypoprolinemia [PMID:11092761 "Their metabolic
phenotype includes hyperammonemia, hypoornithinemia,"].

## Annotation review reasoning

Two catalytic MFs are the core functions, each supported by direct human IDA
(PMID:11092761) and IMP (PMID:26297558, variant loss-of-function):
- GO:0004349 glutamate 5-kinase activity
- GO:0004350 glutamate-5-semialdehyde dehydrogenase activity

Core BP: L-proline biosynthetic process (GO:0055129) and L-ornithine biosynthetic process
(GO:0006592), both IMP. Core CC: mitochondrion (GO:0005739) / mitochondrial matrix
(GO:0005759), IDA.

Borderline:
- GO:0019240 L-citrulline biosynthetic process (IMP): P5CS acts upstream of ornithine,
  which feeds citrulline synthesis; the deficiency lowers citrulline, but ALDH18A1 does
  not itself carry out citrulline biosynthesis. Kept as non-core (indirect/downstream).
- GO:0006536 glutamate metabolic process (IMP): correct-but-broad parent (glutamate is the
  substrate). Non-core, superseded by the specific MF/BP terms.
- GO:0008652 amino acid biosynthetic process (IEA, ARBA): true but generic parent of the
  proline/ornithine BP terms. Non-core.
- GO:0003824 catalytic activity, GO:0016301 kinase activity, GO:0016491 oxidoreductase
  activity (all IEA/InterPro): correct-but-uninformative parents of the two specific
  catalytic MFs. Over-annotated relative to GO:0004349/GO:0004350.
- GO:0005737 cytoplasm (IEA/InterPro): protein is mitochondrial-matrix; cytoplasm is a
  bacterial-family-driven, overly broad/misleading localization -> over-annotated. (This
  IEA InterPro-to-GO transfer from a family that includes cytoplasmic bacterial ProB/ProA
  is arguably removable, but I mark it over-annotated to be conservative.)
- GO:0005743 mitochondrial inner membrane (TAS, Reactome x3) / GO:0031966 mitochondrial
  membrane (IEA, Ensembl): imprecise localization vs the matrix; over-annotated.
- GO:0005515 protein binding (IPI x4 in one GOA row per PMID; HuRI Y2H): bare, generic,
  non-informative -> over-annotated per policy (not removed).
- GO:0042802 identical protein binding (IDA): supported by self-association / homomultimer
  evidence; accept as non-core (structural, not the catalytic core function).
- GO:0003723 RNA binding (HDA): non-core moonlighting.
- GO:0009266 response to temperature stimulus (IEA, Ensembl from rat): weak, non-core.

Per curation policy, experimental annotations (IDA/IMP/IPI) are never REMOVEd; only clearly
wrong IEAs are candidates. I use MARK_AS_OVER_ANNOTATED for the generic-parent IEAs and the
imprecise-localization TAS/IEA, and KEEP_AS_NON_CORE for defensible secondary functions.

## 2026-09-27 source-specific audit

This section supersedes the earlier action reasoning and unsupported source attributions above. The original notes remain as the review journal. The earlier assertion that experimental annotations can never be removed is not the current policy: an uninformative generic protein-binding term can be removed without denying the interaction. Likewise, broad terms are not automatically over-annotations, cytoplasm is not synonymous with cytosol, and a matrix location does not exclude peripheral membrane association.

Baseline was the five canonical files at main `c7078166039c9abd5c62704489283403eb520007`, independently checked by the coordinator (`/tmp/ALDH18A1-root-baseline.json`). HGNC:9722 identifies approved ALDH18A1, UniProt P54886; historical names GSAS, PYCS and SPG9 and alias P5CS were checked for overlapping directories and open PRs. All 40 seeded source objects and both alternative products are preserved. The baseline was INITIALIZED despite already containing decisions. The revised totals are 27 ACCEPT, 3 MODIFY, 2 KEEP_AS_NON_CORE, 2 REMOVE, 1 MARK_AS_OVER_ANNOTATED and 5 UNDECIDED. There are two catalytic cores and no NEW assertions.

### Primary evidence and assay boundaries

- **Human catalysis and disease, PMID:11092761**: the cached primary abstract reports human R84Q expression in mammalian cells, with reduced coupled P5CS activity in both splice forms. It identifies the ATP/NADPH-dependent glutamate-to-P5C chemistry and describes amino-acid deficiencies in two affected siblings. This supports direct participation in glutamate, proline and ornithine metabolism. A coupled-activity defect does not establish that R84Q separately damages the C-terminal reductase domain. The intestinal glutamate-to-ornithine-to-citrulline route includes the chemical work performed by P5CS; being upstream of OTC does not preclude participation. The two citrulline rows remain non-core because their tissue/pathway context is narrower than the principal P5C-producing activity. [Primary abstract](https://pubmed.ncbi.nlm.nih.gov/11092761/).
- **Human versus mouse isoforms, PMID:10037775**: the [original author-institution abstract](https://pure.johnshopkins.edu/en/publications/molecular-enzymology-of-mammalian-%CE%B4sup1sup-pyrroline-5-carboxylat/) and [publisher record](https://www.sciencedirect.com/science/article/pii/S0021925819876445) identify the same primary work, DOI 10.1074/jbc.274.10.6754. Human long and short cDNAs complement yeast strains deficient in kinase/reductase activity. The CHO-K1 expression and ornithine-inhibition measurements described there use **mouse** isoforms; the approximately 0.25 mM Ki is not represented here as a directly measured human value. The full body was not recovered. This is added evidence for the prior isoform discussion, with a normal-cache gate.
- **SPG9 enzyme study, PMID:26297558**: the local file contains bibliography only. The [original publisher extract](https://academic.oup.com/brain/article/139/1/e3/2468786), DOI 10.1093/brain/awv247, explicitly identifies site-directed mutagenesis and enzyme assays using purified recombinant P5CS. Detailed kinetic and localization figures were not recovered. The former title-only finding asserting specific V243L/R252Q domain kinetics has been removed; no such result was inferred from the letter's title. The known catalytic and mitochondrial functions permit retention of the experimental annotations with curator deference, without claiming every disease variant affects both domains equally.
- **Human localization, PMID:32770108**: the cache has `full_text_available: true`, but its extracted body contains Introduction/Discussion rather than the complete Results and figures. Therefore `full_text_unavailable` remains false and this extraction limit is stated separately. Indexed original [PMC7853148](https://pmc.ncbi.nlm.nih.gov/articles/PMC7853148/) Results/Figure 1 were recovered with query `"PMC7853148" "matrix"` (also `"PMC7853148" "P5CS localizes" "matrix"` in independent consultation). The [PubMed figure captions](https://pubmed.ncbi.nlm.nih.gov/32770108/) corroborate the assays. Human HeLa C-terminal P5CS-APEX produces matrix signal; endogenous P5CS has an HSP60-like protease-protection profile. Carbonate pH 11.5 releases most P5CS, ATP5A and HSP60, unlike integral TOMM20. These are positive matrix and non-integral-topology results. They do not rule out peripheral membrane association. The starvation/oxidant experiments and respiratory phenotypes are distinct from the rat thermal-stability source below. The direct structural versus metabolic explanation of respiratory changes remains open.
- **Rat donor experiment, PMID:6131890**: [PubMed identity](https://pubmed.ncbi.nlm.nih.gov/6131890/) and the [original JBC full-paper mirror](https://www.researchgate.net/publication/17054205_Pyrroline-5-carboxylate_synthesis_from_glutamate_by_rat_intestinal_mucosa_Subcellular_localization_and_temperature_stability) were read. The original publisher route was blocked. Results/Discussion on journal pages 3874–3879 test rat intestinal mucosal preparations, mitochondrial subfractions, detergent effects and enzyme activity at different incubation temperatures. Glycerol/phosphate stabilization and protein concentration are assay conditions; the Discussion interprets the loss as heat denaturation of the enzyme or a protein–lipid complex. This is **cell-free enzyme stability**, not an experimentally demonstrated cellular temperature-response process. The study also genuinely retains P5CS activity in a particulate mitochondrial fraction and conditionally discusses the inner membrane or its inner surface. Small miniprint panels were not all legible; no complete reading of those panels is claimed. This is sufficient to revise the thermal-response scope and to retain uncertainty about transfer of precise membrane association to human P5CS.
- **Human self-association, PMID:26320891**: the cached primary abstract explicitly describes affected fibroblasts and heterologous expression, mutant–wild-type interaction, altered sub-mitochondrial distribution and reduced native-complex size. Together with the multimerization experiments in PMID:32770108, this supports self-association as a property of the core enzyme. It does not fix one obligatory native oligomer stoichiometry. [Original primary record](https://pubmed.ncbi.nlm.nih.gov/26320891/).
- **Newer assembly context, PMID:39506109**: the [primary PubMed abstract and figure captions](https://pubmed.ncbi.nlm.nih.gov/39506109/), DOI 10.1038/s41586-024-08146-w, were checked. The study describes ATP-demand-associated segregation of P5CS filaments into mitochondrial subpopulations. Many mechanistic experiments use mouse embryonic fibroblasts; human U2OS knockout/rescue, human cell imaging and human tissue observations are separately identified in the figures. This supports dynamic organization of the enzyme rather than assigning P5CS ATP-synthase chemistry or a new respiratory catalytic activity. No new process annotation is proposed from this context.
- **HDA RNA binding, PMID:22658674**: the source explicitly uses UV crosslinking and mRNA-interactome capture in human HeLa cells. The ALDH18A1-specific supplementary result was not recovered. The decision is UNDECIDED, not an allegation of contamination or an established moonlighting mechanism.
- **Protein-interaction maps, PMID:25416956 and PMID:32296183**: the cached human binary-interaction studies and curated pair identifiers were checked. The first cache is a partial full-text extraction. Removing GO:0005515 concerns the term's lack of a useful functional meaning; neither the AGTRAP/CMTM5 nor COQ9/DARS2 pairs are declared false. No specific adaptor function is manufactured from them.
- **MitoCoP, PMID:34800366**: the cached full XML describes human mitochondrial profiling, but the extracted article does not contain the target supplementary hit. The HTP mitochondrial assignment is retained with curator deference and strong independent human localization evidence, at the original organelle resolution.
- **Historical human clone, PMID:8761662**: the cached primary abstract identifies the human cDNA and attributes the two catalytic reactions to the encoded bifunctional enzyme. It supports the source TAS process; this is not described as purified-domain enzymology.

### Disease citations already present in the journal

The four uncached older disease references remain required even though they do not supply new function assertions in this revision. Their primary records were checked: [PMID:18478038](https://pubmed.ncbi.nlm.nih.gov/18478038/) describes H784Y-associated disease without the usual metabolic abnormalities and reports preserved measured fibroblast proline/ornithine flux; [PMID:22170564](https://pubmed.ncbi.nlm.nih.gov/22170564/) concerns clinical, expression and functional P5CS-deficiency analysis; [PMID:24767728](https://pubmed.ncbi.nlm.nih.gov/24767728/) is a cutis-laxa case report with literature review; [PMID:26026163](https://pubmed.ncbi.nlm.nih.gov/26026163/) concerns dominant and recessive spastic paraplegia and ornithine metabolism. In particular, the earlier universal-sounding metabolic-signature sentence is superseded: circulating amino-acid abnormalities vary among genotypes. These observations do not define a new molecular function from clinical necessity alone.

### Ontology, propagation and reaction checks

The local OAK GO SQLite snapshot was read directly for exact definitions and parent edges; the relevant live GO displays were also checked. [GO:0005737](https://flybase.org/cgi-bin/cvreport.pl?childdepth=2&cvterm=GO%3A0005737) includes organelles and therefore is compatible with mitochondrial P5CS. [GO:0009266](https://amigo.geneontology.org/amigo/term/GO%3A0009266) requires a change in a cell or organism, which is why the recovered cell-free thermal assay is insufficient for the transferred process. GO:0004350 displays the reversible reaction in the oxidative direction; its use for the physiological reductase reaction is correct. GO:0006592/GO:0019240 describe biosynthetic pathways, not only their final chemical step. Original seeded labels are preserved even when current ontology display wording differs.

InterPro root catalytic, kinase and oxidoreductase assertions are refined to the resolved chemistry. ATP binding, broad amino-acid biosynthesis, glutamate metabolism, mitochondrion and cytoplasm assertions remain valid at their source resolution. Broad true assertions are not rejected merely because the integrated core uses narrower terms.

The cached PAINT `interpro/panther/PTHR11063/PTHR11063-paint.tsv` has the IBD nodes PTN000869169 (mitochondrion) and PTN000115463 (GPR). Their reviews use the ancestral PTN nodes only; neither donor counts nor target self-evidence are treated as circularity. The GO-CAM index contains no P54886 entry. Exact ARBA rule predicates were not recovered, so their source-status limit is explicit while independent target chemistry supports the process.

The Ensembl source is rat UniProt A0A8I6AAN3 / ENSRNOP00000089847. The [MGI orthology GO graph](https://www.informatics.jax.org/homology/GOGraph/Aldh18a1) traces both the temperature-response IDA and mitochondrial-membrane IDA to PMID:6131890 / RGD:13439717. The thermal row's source scoping problem is supported by the recovered original study. The membrane row remains UNDECIDED.

All three cached Reactome records were read: R-HSA-508040 explicitly describes P5CS associated with the inner membrane during catalysis, while R-HSA-9837978/9838004 concern LONP1 substrates. Reactome's P54886 entity carries an explicit inner-membrane compartment. This is a genuine source assertion, not something inferred merely from an event title. The summaries do not resolve the human P5CS-specific localization experiment; matrix/non-integral evidence is not sufficient to refute peripheral association. All three precise IMM rows remain UNDECIDED.

### Research execution and remaining gates

Default Falcon with Perplexity-lite fallback was launched concurrently with normal GOA publication caching. The first launch inherited offline runtime settings and failed dependency discovery before provider execution. A corrected online launch used ordinary writable `UV_TOOL_DIR`, `UV_TOOL_BIN_DIR` and `UV_CACHE_DIR` under `/tmp`; both provider dependency attempts then failed DNS before either provider executed. Logs: `/tmp/ALDH18A1-deep-research.log` and `/tmp/ALDH18A1-deep-research-online.log`. No provider-generated report exists and none was authored manually. Manual primary-source work above supplies the review evidence.

GOA publication caching completed with the nine existing source PMIDs already cached (`/tmp/ALDH18A1-fetch-goa.log`). Normal fetches for the five older notes/context gaps and two newly traced sources failed DNS, terminal exit 1, with 0/5 and 0/2 cached (`/tmp/ALDH18A1-fetch-notes.log`, `/tmp/ALDH18A1-fetch-donors.log`). The exact seven gates are **18478038, 22170564, 24767728, 26026163, 39506109, 6131890 and 10037775**. These have been included in the coordinator's fixed source-recovery batch; no source bytes were manufactured or edited. The review stays DRAFT pending normal cache recovery and the documented evidence questions. External primary access is described independently from local cache availability.

The annotation-reviewer consultation is this agent's full 40-row audit; a second agent independently checked the human matrix/non-integral assays and rat thermal-study scope, agreeing that matrix evidence does not rule out peripheral association. The coordinator is separately reviewing all decisions and both cores. No shared project files or Git state were edited.

Validation completed: `just validate human ALDH18A1` passed with one aggregated reference-access warning; `just validate-history` and `just render human ALDH18A1` passed. A case-sensitive whitespace-normalized check verified all 47 cached supporting snippets; the single uncached thermal quote was independently confirmed in indexed PubMed. The source-object, original-reference-identity, isoform and protected-file checks passed. The notes-inclusive cache census remains the seven IDs above.

Coordinator review read all 40 decisions, propagation assessments, 22 original-plus-added literature/method references, both cores and questions without a biological blocker. The bounded final refinement adds the exact preserved UniProt `Mitochondrion matrix` location statement to each core (23 references total, including that source file). Live [AmiGO GO:0006592](https://amigo.geneontology.org/amigo/term/GO:0006592) names the term **L-ornithine biosynthetic process**; the local OAK cache uses the older shorter label. Only the authored core label was updated to the live official label; all trusted source fields remain intact. YAML anchors and aliases were expanded with parsed-content equality checks.

Final validation passed (exit 0) with two warning categories: missing reference caches and the local ontology snapshot retaining “ornithine biosynthetic process” for GO:0006592 while the live official AmiGO label is “L-ornithine biosynthetic process”. The authored core keeps the verified current label; source GOA terms remain unchanged. DRAFT remains for the seven notes-inclusive missing caches. The final integrity check confirms 49 case-sensitive, whitespace-normalized cached quotes, with no case-fold-only matches.


## 2026-09-27 source5 recovery follow-up

This follow-up supersedes the seven missing-cache statements above. The source5 normal-fetch artifact supplied exact machine-generated records for PMID:6131890, PMID:10037775, PMID:18478038, PMID:22170564, PMID:24767728, PMID:26026163 and PMID:39506109. Their SHA256 and Git blob hashes match the coordinator's verified import receipt `tmp/source5-canonical-import-receipt.json`; no source record was rewritten. The published review baseline is PR #3269 head `4729ad9dd1f8a32f4ef8bda79d7a30f118d45eab`, with all five canonical files independently matched by GitHub blob IDs before editing.

The six abstract-only records and the one full-text record were read. Their evidential scopes are:

- **PMID:6131890:** the normal abstract confirms rat intestinal mitochondrial fractions, retention of activity in the particulate fraction, and temperature/glycerol/detergent effects on cell-free activity. It agrees with the earlier external full-paper reading. GO:0009266 remains over-annotated from this particular thermal assay, while transfer of precise human membrane association remains unresolved.
- **PMID:10037775:** the fetched title spells **Delta1**, now preserved exactly in the reference metadata. Both human cDNAs complement deficient yeast, whereas the stable CHO ornithine-inhibition assays concern murine isoforms. The abstract's inner-membrane statement does not identify a direct human localization experiment. This recovery does not resolve the three precise inner-membrane annotations.
- **PMID:18478038:** the H784Y family has clinical disease despite unaffected measured fibroblast proline and ornithine flux. This reinforces the existing caution about variable biochemical phenotypes, rather than establishing another enzyme activity.
- **PMID:22170564:** the abstract distinguishes human patient fibroblast expression/localization observations from mutagenesis and functional assays in bacterial glutamate kinase. The structural models and clinical arginine treatment are not represented as purified human P5CS variant measurements.
- **PMID:24767728:** the case report and ten-patient review concern the variable neurocutaneous phenotype. They supply disease context, not an additional direct molecular function.
- **PMID:26026163:** the abstract reports dominant and recessive hereditary spastic paraplegia, amino-acid abnormalities in a subset of individuals, and glutamine-loading evidence for a P5CS block in two related patients' fibroblast cultures. The disease spectrum and metabolic evidence are retained without assuming that all genotypes share the same blood signature.
- **PMID:39506109:** the genuine full text was read in Results, Discussion and relevant Methods; `full_text_unavailable` is now false. Human P5CS cDNA is explicitly specified for tagged and mutant constructs. U2OS knockout/rescue and endogenous imaging, and human pancreatic ductal adenocarcinoma tissue staining, provide direct human evidence. Most fusion/fission and OPA1 experiments use mouse embryonic fibroblasts; the DRP1 experiment in 143B cells is distinguished. The study links enzyme filaments, proline synthesis and mitochondrial subpopulation organization. ATP synthase performs ATP synthesis and the fission/fusion machinery executes membrane dynamics; no new P5CS catalytic or process assertion is created from those other proteins' work.

All 40 source objects and their decisions, both alternative products, both catalytic cores, original reference identities and protected GOA/UniProt bytes remain unchanged. The only YAML changes concern three reference assessments, one fetched title and the full-text availability flag. Existing unresolved target-specific RNA-binding evidence and precise membrane localization questions remain unresolved; normal cache recovery is not itself resolution of every biological question.

A recursive citation scan covered all five gene files (the HTML is a derived duplicate), with no provider, hypothesis or other nested source artifact present. The 17 distinct normalized DOIs resolve either to a cached PMID record or to the paired PMID in the immutable UniProt bibliography. The authored review and historical notes use 16 distinct PMIDs as evidence or biological context, all now cached; the raw-only inventory below is separate. The three additional absent raw-UniProt-only records are PMID:15164054 (genomic sequencing; DOI 10.1038/nature02462), PMID:24275569 (human liver phosphoproteome; DOI 10.1016/j.jprot.2013.11.014), and PMID:25944712 (mitochondrial N-terminome; DOI 10.1002/pmic.201400617). The latter two primary PubMed identities and abstracts were checked; no target-specific supplementary hit from either is used in this review. The genomic citation is retained as UniProt provenance, not independently promoted to functional evidence. Likewise, R-HSA-8964539 is an unused raw UniProt pathway cross-reference. These four raw-only records are inventoried separately rather than expanding the reviewed evidence into unrelated citations. Current main `30a9290881824baaacab2b681d7808f572c4cef6` lacks those four and the seven newly imported source5 papers, so the seven actual recovery records are explicitly included in this follow-up's publication manifest. All Reactome entries cited by the authored review are cached.

The earlier genuine provider failures remain historical facts; there was no new provider run or fabricated provider output for this bounded cache follow-up. DRAFT is retained while the intentional live-versus-local GO:0006592 label advisory remains. The seven reference-cache gates are closed locally and will close on the PR when these exact records are published.

Follow-up checks: full gene validation passed with only the pre-existing GO:0006592 label advisory. All 50 case-sensitive, whitespace-normalized source excerpts passed; all original source objects, actions, cores and protected bytes are preserved. The regenerated HTML and new history record accompany the seven exact recovered cache files.


## 2026-09-27: ATP and membrane evidence follow-up

Reviewed PR #3269 formal review 5329874104 and comment 5854896502 against the exact published head `f0dcf402a39ca4d849f128c3a90bd3e9703ab9c8`. The independent follow-up read agrees with the nine revised evidence blocks and the corrected duplicate-row explanation. No annotation action, machine-supplied source field, alternative product, reference identity, or core function changes.

For GO:0005524, the evidence now explicitly names ATP: the cached UniProt reaction is `Reaction=L-glutamate + ATP = L-glutamyl 5-phosphate + ADP;`, and the PMID:11092761 abstract describes a bifunctional ATP- and NADPH-dependent mitochondrial enzyme. The three GO:0004349 assertions and the broad kinase refinement also cite the exact gamma-glutamyl kinase domain wording and this reaction. The human R84Q result is retained as coupled P5CS activity evidence; it is not recast as a separately measured isolated-domain kinetic assay. ATP binding remains an integral catalytic property represented by the kinase core, without a redundant third core function.

The rat mitochondrial-membrane transfer and three Reactome inner-membrane assertions now quote the actual PMID:6131890 fractionation result: the membrane fraction freed of soluble matrix and intermembrane-space enzymes retained P5C-synthesizing activity. This is positive rat biochemical evidence, not a direct human topology experiment. The four UNDECIDED decisions continue to distinguish particulate/peripheral association from integral insertion, and human matrix evidence from proof of no membrane association. The local PMID:6131890 and PMID:11092761 records remain abstract-only; these added excerpts do not claim recovery of their complete articles.

The third seeded ornithine-biosynthesis entry is explicitly identified as a duplicate of the other PMID:11092761 IMP assertion. The GOA has two corresponding process rows, while the preserved review has three; this duplicate is not independent evidence. Its source object is retained intact.

The optional action suggestions were assessed without changing the accepted biological interpretation. GO:0009266 remains MARK_AS_OVER_ANNOTATED because the inspected rat experiment measures cell-free enzyme thermal inactivation and assay stabilization; it does not establish a cellular temperature-response function. GO:0008652 remains ACCEPT: ALDH18A1 directly catalyzes steps of amino-acid biosynthesis, so this broad process is correct core participation, even when its molecular function can be refined to substrate-specific chemistry. GO:0042802 remains ACCEPT with observed self-association integrated into the existing catalytic synthesis; an additional assembly-only core would duplicate that account. These retained actions do not imply either a fixed native oligomeric stoichiometry or that every accepted supporting property needs a separate core entry.

No publication, raw UniProt/GOA, or provider artifact was modified or newly fetched. The prior source5 closure and its explicit distinction between authored citations and unused raw-record bibliography remain applicable; this follow-up introduces no new citation. DRAFT remains appropriate for the recorded live-versus-local GO:0006592 label advisory, rather than treating all abstract-only records as missing-source gates.
