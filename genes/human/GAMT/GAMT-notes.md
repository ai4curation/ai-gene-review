# GAMT (human) — review notes

UniProt: Q14353 (GAMT_HUMAN). Gene: GAMT (HGNC:4136), chr 19p13.3. EC 2.1.1.2.
236 aa, ~26 kDa. Class I-like SAM-binding methyltransferase superfamily, RMT2 family.

## Core molecular function

GAMT is guanidinoacetate N-methyltransferase, the second and terminal enzyme of
endogenous creatine biosynthesis. It transfers a methyl group from
S-adenosyl-L-methionine (SAM/AdoMet) to guanidinoacetate (GAA), yielding creatine
and S-adenosyl-L-homocysteine (SAH).

- UniProt FUNCTION/CATALYTIC ACTIVITY [UniProtKB:Q14353]:
  "Converts guanidinoacetate to creatine, using S-adenosylmethionine as the methyl donor"
  Reaction: guanidinoacetate + S-adenosyl-L-methionine = creatine + S-adenosyl-L-homocysteine + H(+);
  Rhea:RHEA:10656; EC=2.1.1.2.
- PATHWAY [UniProtKB:Q14353]: "Amine and polyamine biosynthesis; creatine biosynthesis;
  creatine from L-arginine and glycine: step 2/2." (AGAT/GATM makes GAA in step 1; GAMT methylates it in step 2.)
- Substrate binding residues (UniProt features): SAM at residues 20, 50, 69-74, 90-92, 117-118, 135;
  guanidinoacetate at 42, 46, 135, 171-172. Confirmed by human crystal structure with SAH
  (PDB 3ORH; SGC) and rat ternary-complex structures.
- The reaction obligatorily consumes SAM and releases SAH (a coproduct that is itself a
  product-inhibitor of methyltransferases), so the activity is also an S-adenosylmethionine
  catabolic / SAH-producing process.

## Quantitative role as a SAM methyl-group consumer

Creatine synthesis is one of the largest single consumers of methyl groups in the body.
[ScienceDirect topic overview, web] "Creatine biosynthesis consumes 40% of methyl groups
produced as S-adenosylmethionine" — the GAMT step is the methylation event, making GAMT a
major sink for SAM-derived methyl groups and a node linking creatine metabolism to
one-carbon / methionine metabolism.

## Localization

GAMT is a soluble cytosolic enzyme. Rat liver subcellular fractionation localizes GAMT
activity to the cytosolic fraction; human Reactome places the reaction in the cytosol
(GO:0005829). The IBA pan-ancestor "nucleus" call (GO:0005634) has no direct experimental
support for GAMT and is best treated as an over-annotation; GAMT is a soluble metabolic
enzyme with no described nuclear function. "cytoplasm" (GO:0005737) is supportable but is a
broad localization rather than the defining function.

## Tissue expression

- UniProt TISSUE SPECIFICITY [UniProtKB:Q14353, PMID:8651275]: "Expressed in liver."
- Human Protein Atlas: "Tissue enhanced (liver, skeletal muscle, tongue)."
- Liver is a central organ of creatine synthesis: GAA produced largely by kidney (AGAT) is
  released into circulation and methylated to creatine in liver. Brain (astrocytes,
  oligodendrocytes) also expresses GAMT for local CNS creatine synthesis.

## Disease: GAMT deficiency / Cerebral creatine deficiency syndrome 2 (CCDS2, MIM:612736)

Autosomal recessive. GAMT deficiency was the first described inborn error of creatine
metabolism.
- [PMID:8651275 "In two children with an accumulation of guanidinoacetate in brain and a
  deficiency of creatine in blood, a severe deficiency of guanidinoacetate methyltransferase
  (GAMT) activity was detected in the liver."]
- [PMID:8651275 "It causes a severe developmental delay and extrapyramidal symptoms in early
  infancy and is treatable by oral substitution with creatine."]
- UniProt DISEASE: "developmental delay and regression, intellectual disability, severe
  disturbance of expressive and cognitive speech, intractable seizures, movement
  disturbances, severe depletion of creatine and phosphocreatine in the brain, and
  accumulation of guanidinoacetic acid in brain and body fluids."
- Many disease-causing missense variants abolish enzymatic activity in functional assays
  (e.g. W45R, M50L, H51P, A54P, L159P, L166P, L197P, R208P; characterized in PMID:24415674,
  PMID:26003046, PMID:26319512), confirming that loss of GAMT catalytic activity is the
  molecular basis of disease. UniProt FUNCTION also notes "Important in nervous system
  development (PubMed:24415674)" — this is a downstream organismal consequence of creatine
  deficiency rather than a distinct direct molecular role.

## Annotation-relevant judgments

- MF: guanidinoacetate N-methyltransferase activity (GO:0030731) — core; well supported
  (IMP from PMID:8651275 enzyme-deficiency demonstration; IBA; IEA from EC/Rhea/InterPro).
- MF: methyltransferase activity (GO:0008168, Reactome TAS) — correct but a generic parent of
  GO:0030731; over-general, mark as over-annotated.
- BP: creatine biosynthetic process (GO:0006601) — core (IDA PMID:8651275; IBA; IEA; TAS).
- BP: creatine metabolic process (GO:0006600, Reactome TAS) — correct but parent of the more
  specific biosynthetic term; keep as non-core.
- BP: muscle contraction (GO:0006936, TAS PMID:8547310) — GAMT is not part of the muscle
  contraction machinery; this is a distal physiological consequence of creatine availability,
  not a direct GAMT process. Over-annotation.
- CC: cytosol (GO:0005829, Reactome TAS) — supported localization; keep as non-core.
- CC: cytoplasm (GO:0005737, IBA) — broad, supportable; keep as non-core.
- CC: nucleus (GO:0005634, IBA) — unsupported pan-ancestor localization; over-annotation.
- MF: protein binding (GO:0005515) — three IPI annotations from high-throughput interactome
  screens (PMID:28514442, PMID:32296183, PMID:33961781; partners include FARS2/O95363,
  RAB24/Q969Q5, TRIM39/Q9HCM9-2 per UniProt IntAct). Bare "protein binding" is uninformative
  and no functional consequence is established; over-annotation per curation guidelines.
  The interactions are real (IPI) so REMOVE is not appropriate; MARK_AS_OVER_ANNOTATED.

## Interaction-paper PMIDs (cached, abstract-level high-throughput screens)
- PMID:28514442 Huttlin et al., BioPlex "Architecture of the human interactome..."
- PMID:32296183 Luck et al., HuRI "A reference map of the human binary protein interactome."
- PMID:33961781 Huttlin et al., BioPlex 3.0 "Dual proteome-scale networks..."
None characterize a specific GAMT binding function.

## Sources
- UniProtKB:Q14353 (cached uniprot.txt)
- PMID:8651275 (cached; abstract)
- Web: ScienceDirect "Guanidinoacetate Methyltransferase" overview (40% SAM methyl groups);
  GATM/GAMT local creatine synthesis (ScienceDirect S0006899321004844).
</content>
</invoke>


## 2026-11-02 — Reaction, phylogeny and source reassessment

The preceding journal is retained verbatim as historical work. Its confident rejection of nuclear localization, muscle-contraction attribution and generic-binding removal policy is superseded by the source-specific assessment below. Earlier unsupported quantitative methyl-group statements are not carried into the current biological summary.

### Human catalytic evidence and process scope

The original scanned pages 915–917 of PMID:8651275 were visually read, including Methods, Table 1 and Results. Fractionated and dialysed human liver extracts transferred radiolabeled methyl groups from SAM to guanidinoacetate; chromatography identified creatine. Substrate-free blanks, reference enzymes, electrocautery effects and mixing controls were considered. This is direct reaction/product evidence, separate from clinical loss-of-function necessity. The normal cache remains abstract-only; the inspected original images are retained separately. The mislabeled PDF endpoint returned HTML and is not counted as an original PDF. [Original article](https://pmc.ncbi.nlm.nih.gov/articles/PMC1914613/)

The official human Reactome reaction and catalyst specify SAM plus guanidinoacetate conversion to SAH plus creatine and a proton, with Q14353 in cytosol. GAMT performs the creatine-biosynthesis step, rather than the later transport or creatine-kinase reactions. The inherited core-only SAM-catabolism facet is retained: exact-term comparators include rat/mouse Gamt and other methyltransferases, and the actual typed hierarchy does not make it redundant with creatine biosynthesis. No separate NEW or quantitative homeostasis claim is proposed. [Reaction](https://reactome.org/content/detail/R-HSA-71286); [human participant](https://reactome.org/content/detail/R-HSA-71276)

### Phylogeny and products

The exact displayed 236-residue human sequence matches the PTHR32379 alignment and target AN17/PTN002529431. All four IBA assertion nodes lie on its lineage, with unchanged literal/current/main donors. The nuclear and cytoplasmic assertions have genuine experimental fungal donor contexts. The accessible Rmt2 abstract describes both compartments; donor full-text images were not read. Chemical specialization alone is not evidence of localization loss, and the verified cytosolic reaction does not require an exclusive location. No human nuclear assay is invented.

Both natural UniProt products are preserved: Q14353-1 is 236 residues and Q14353-2 is 269 residues, with the latter independently matching the VSP_042722 reconstruction and direct FASTA. The processed chain 2–236 is distinct. The inspected liver assay does not establish equivalent activity for the longer natural product, and disease transcripts are not normal splice products. [UniProt](https://www.uniprot.org/uniprotkb/Q14353/entry)

### Interaction and unresolved contraction claims

The original BioPlex tables support the Q14353–O95363 co-association. Exact HuRI rows support Q14353-1–Q969Q5 and Q14353-1–Q9HCM9-2 in human-ORF yeast two-hybrid assays. The partner suffix and clone scope remain explicit; the overlapping screen records are not treated as independent functional mechanisms. Four generic protein-binding annotations are removed as uninformative under the current policy, while their positive biological observations are preserved. No replacement activity is invented. [PMID:28514442](https://pubmed.ncbi.nlm.nih.gov/28514442/); [PMID:32296183](https://pubmed.ncbi.nlm.nih.gov/32296183/); [PMID:33961781](https://pubmed.ncbi.nlm.nih.gov/33961781/)

The muscle-contraction TAS is UNDECIDED. PMID:8547310's full experiments were not recovered; its cloning/clinical abstract cannot settle a direct role in the GO-defined contractile step. The rat probe does not make the cloned human record a wrong-organism citation. PMID:9325156's authentic abstract supports the established reaction and human gene mapping, while its negative jittery-mouse mutation finding does not negate human enzymatic activity. [PMID:8547310](https://pubmed.ncbi.nlm.nih.gov/8547310/); [PMID:9325156](https://pubmed.ncbi.nlm.nih.gov/9325156/)

### Conservation and current stage

The private proposal covers eighteen literal current contexts: nine ACCEPT, four MODIFY, four REMOVE and one UNDECIDED; no NEW is added. One core retains the specific catalytic activity, creatine biosynthesis, SAM catabolism and cytosol. Eleven inherited references receive manual assessments. All seventeen old rows and fourteen original quote associations remain available through immutable Git and private original files, with exact historical locators in the compact public evidence record. The old single HuRI row lacks partner identity and is not silently assigned to one current partner.

Three short current anchors are exact cached substrings, with source hashes and byte offsets recorded separately. Both inherited reference finding statements are restored with explicit manual assessments. Their short exact anchors contain 13 words from PMID:8651275 and 4 words from UniProt, alongside the 6-word Reactome core anchor. Each appears once; twelve other inherited quotation associations remain historical-only. No excerpt is repeated here. Genuine native acquisition and private seed reconciliation now match all eighteen original rows and the actual 16-column export. Sixteen main sources are reused unchanged, thirteen missing sources are acquired without force, and all three exact snippets pass native-byte checks. Both product records and the two restored finding statements remain intact. Default validation passed with one advisory for the deliberately retained core-only SAM-catabolism facet; it does not require manufacturing a NEW annotation. Strict GOA matched all 18 rows, native history and DRAFT status checks passed, and private rendering/link and whitespace checks passed. The muscle-contraction judgment remains UNDECIDED. Source text and original annotation contexts were not manually edited.

The broad cytoplasm IBA is refined to cytosol using the verified direct GO:0005829 part_of GO:0005737 relationship and the human Reactome catalyst. The PAINT node and donors remain valid; no ancestry defect or nuclear exclusion is inferred.


## 2026-11-04 — Native source reconciliation

The genuine no-seed refresh preserved the inherited review and journal before transfer. All 18 current contexts and their four IBA placements match the actual export; both natural-product records match the native UniProt record. All 29 source bytes and eleven reference titles were checked, with selected original reading kept distinct from normal-cache availability. The two inherited finding statements remain current at their stated scope. The exact native source snippets occur once each, with no added quotation in this journal. A native EDIT history records the completed transfer. Default validation passed with one advisory for the deliberately retained core-only SAM-catabolism facet; it does not require manufacturing a NEW annotation. Strict GOA matched all 18 rows, native history and DRAFT status checks passed, and private rendering/link and whitespace checks passed. The muscle-contraction judgment remains UNDECIDED.

## 2026-11-04 — Functional variant evidence and compartment scope

Human GAMT-deficient fibroblast assays provide additional functional evidence for the enzyme: selected missense alleles restore activity, whereas others do not. These experiments corroborate the reaction established by the original human-liver assay. Their clinical findings also explain why GAMT matters for neurological health, without identifying an additional developmental step performed by the protein ([PMID:24415674](https://pubmed.ncbi.nlm.nih.gov/24415674/), [PMID:26319512](https://pubmed.ncbi.nlm.nih.gov/26319512/)).

The longer annotated product requires a distinction between sequence and demonstrated protein function. UniProt maps Q14353-2 to NM_138924.3/NP_620279.1. The [PMID:26003046](https://pubmed.ncbi.nlm.nih.gov/26003046/) abstract reports no measurable wild-type transcript-2 activity, while the official [NCBI Gene 2593](https://www.ncbi.nlm.nih.gov/gene/2593) description reports no detected GFP-fusion protein in that study. The result therefore does not establish intrinsic inactivity of purified 269-residue GAMT. Original Methods were not accessed. Both declared products remain recorded, and the proposed experiment first controls expression and stability.

The verified nuclear PAINT placement remains positive phylogenetic support, now classified as non-core because a central human nuclear biochemical role is not established. This does not assert localization loss from fungal-to-metazoan substrate specialization or exclusivity of the cytosolic pool. The historical muscle-contraction TAS remains uncertain: its accessible cloning/clinical abstract does not resolve the exact support, and an article title cannot exclude unseen experiments.

The core again records guanidinoacetate and SAM as structured substrates. SAM catabolism remains a supported facet of the same methyl-transfer reaction, with positive ortholog/comparator and human reaction evidence; no NEW annotation is manufactured to remove an advisory. The biological question separating guanidinoacetate toxicity from creatine depletion is restored. Earlier journal text remains historical. Current source assessments and exact excerpts are in the review, with public locators in the [source guide](GAMT-source-guide.md).

Target validation passed with one advisory for the deliberately retained SAM-catabolism core facet; strict GOA matched all 18 originals. Native codex EDIT history, DRAFT status audit, private 18-row/one-core/14-reference rendering and whitespace checks passed. One source-specific UNDECIDED judgment remains; all 29 scientific sources are unchanged.
