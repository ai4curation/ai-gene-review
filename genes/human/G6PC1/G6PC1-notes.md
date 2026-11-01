# G6PC1 evidence notes

## 2026-11-01: catalytic function and source-specific reassessment

G6PC1 hydrolyzes glucose 6-phosphate on the luminal face of the ER membrane. Human cloning and expression, active-site mutagenesis and the recent human structures support one catalytic core that completes glucose production and contributes to glucose homeostasis [PMID:8211187; PMID:12093795; PMID:39847333]. The transporter SLC37A4 supplies substrate to the luminal compartment; this does not assign transporter activity to G6PC1. The earlier phrase “committed step” is replaced with “terminal step” because the same hydrolysis receives substrate from gluconeogenesis and glycogen breakdown.

The native products must remain distinct. Current UniProt specifies a 357-residue canonical sequence and a 176-residue alternative product; the latter was checked against the literal sequence variation and its own official FASTA. The 2025 substrate-trapping structure uses engineered H176A and a terminal ALFA substitution, not the natural short product. The canonical human family-book sequence is exact, but neither that match nor the structure establishes equivalent activity of the alternative product [PMID:39847333; UniProtKB:P35575].

The inherited categorical removal of phosphotransferase activity is not supported by the actual donor experiment. The literal human transfer points to mouse P35576/ENSMUSP00000019469, whose curated IDA annotation cites PMID:8407995. The original mouse study measures transfer from carbamyl phosphate to glucose in disrupted microsomes from transfected COS1 cells and adult mouse liver, with a mock-vector control. This is compatible with a phosphatase also catalyzing phosphotransfer under assay conditions. Retention as a non-core measured capability does not assert physiological reverse glucose flux or a direct human assay. Numerical units are not copied from ambiguous OCR [PMID:8407995].

Hormonal, nutritional and drug-response terms require their actual donor context. The rat annotations were traced to eight original publications. Fructose and high-protein feeding studies expose G6pc expression responses [PMID:14988444; PMID:17158265]. The insulin/metformin promoter study distinguishes basal and dexamethasone/cAMP conditions [PMID:19579180]. In the insulin-treated STZ-diabetic rat study, adjunct resveratrol lowers G6pc expression relative to insulin alone; insulin-treated rats have higher expression than the nondiabetic group, so the paper is not evidence for unconditional insulin repression [PMID:27366200]. GO response definitions permit changes in gene expression. Experimental drug treatment alone is therefore not grounds for rejecting an existing response annotation.

Two abstract-only donor reports leave narrower questions open. The gossypol/high-fat/STZ abstract does not expose the precise carbohydrate stimulus behind the curated carbohydrate-response annotation [PMID:26883980]. The suckling/weaning fasting abstract does not expose a G6pc-specific measurement [PMID:25943649]. Neither limitation proves misattribution. The broad nutrient and insulin terms can be assessed alongside independently supported narrower response terms, while retaining the original donor records. Rat hepatic overexpression supports a secondary lipid-homeostasis effect rather than a lipid-catalytic core [PMID:9813078].

Selected original Methods and Results in the 2002 human study identify a covalent His176 phosphoenzyme [PMID:12093795]. That result must not silently become an independent demonstration of noncovalent free-phosphate binding. The distinction remains an explicit question for the phosphate-ion-binding annotation; neither a title nor an abstract-only comparison is grounds to reject experimental curation.

The four IBA assertions have been joined to actual family-tree placement and literal donor records. All originate at PTHR12591 node AN0/PTN000971890; human P35575 is descendant AN15/PTN002488968. Every literal donor is represented below the asserted node. A human self-donor is legitimate experimental grounding for an ancestral inference, not circularity. Main PAINT and the retained IBD records contain the same donor sets, with three ordering-only differences preserved. This does not claim that every historical donor experiment was independently read.

Reactome's defective-G6PC event describes disease variants relative to the normal hydrolysis reaction. Its TCF19:NuRD event distinguishes the nucleoplasmic gene input from the ER-membrane protein output. Neither event gives G6PC1 a chromatin-regulatory activity. Source-specific experimental annotations are not removed merely because a cached abstract foregrounds SLC37A4 or G6PC3 [PMID:10318794; PMID:15661744].

The inherited source export contains 40 contexts, while the inherited review stores 39 because two interaction contexts were combined. Current annotation dates differ in 16 records; original machine fields are preserved and any current native reconciliation must account for all 40. The original 42 supporting-text associations remain available as historical provenance. Only two short inherited core excerpts are retained in this draft; no replacement quotation is invented. Full-text access and selected-reading limits are recorded separately for every source assessment.

## Retained earlier journal

The following is the complete earlier notes file, retained as historical text. Its old activity-removal rationale and embedded tool-markup fragment are not current conclusions.

<details>
<summary>Earlier G6PC1 notes, verbatim</summary>

```text
# G6PC1 (Glucose-6-phosphatase catalytic subunit 1) — review notes

UniProt: P35575 (G6PC1_HUMAN); formerly G6PC / G6PC1; EC 3.1.3.9.
HGNC:4056. 357 aa. Chromosome 17.

## Core biology

G6PC1 is the liver/kidney/intestine catalytic subunit of glucose-6-phosphatase, a
multi-pass integral endoplasmic reticulum (ER) membrane protein (nine transmembrane
helices) whose catalytic active site faces the ER lumen. It hydrolyzes
D-glucose-6-phosphate + H2O -> D-glucose + phosphate (Rhea:16689), the terminal,
committed step shared by gluconeogenesis and glycogenolysis, thereby enabling
hepatic/renal glucose output into blood. It functions together with the ER
glucose-6-phosphate transporter SLC37A4/G6PT, which supplies luminal G6P.

Key UniProt FUNCTION line:
"Hydrolyzes glucose-6-phosphate to glucose in the endoplasmic reticulum. Forms with
the glucose-6-phosphate transporter (SLC37A4/G6PT) the complex responsible for glucose
production in the terminal step of glycogenolysis and gluconeogenesis. Hence, it is the
key enzyme in homeostatic regulation of blood glucose levels."
(ECO:0000269|PubMed:10960498, 12093795, 15542400, 9332655, 9497333)

## Structure / topology / active site (PMID:9497333, PMID:12093795)

- Nine transmembrane helices; N terminus lumenal, C terminus cytoplasmic (odd number of
  TM helices). Active-site residues Arg-83, His-119, His-176 reside on the luminal side.
- His-176 is the nucleophile that forms the phosphohistidine-enzyme intermediate;
  His-119 is the proton donor (ACT_SITE 119 proton donor, 176 nucleophile in UniProt FT).
- PAP2 phosphatase superfamily fold (InterPro IPR016275 Glucose-6-phosphatase;
  IPR000326 PAP2/HPO). N-glycosylated at Asn-96 (PMID:9705299, 19159218).

## Disease: Glycogen storage disease type Ia (GSD1A / von Gierke disease, MIM:232200)

Autosomal recessive; deficiency of G6Pase impairs the terminal steps of glycogenolysis
and gluconeogenesis. Fasting hypoglycemia, severe hepatomegaly (glycogen accumulation),
kidney enlargement, growth retardation, lactic acidemia, hyperlipidemia, hyperuricemia.
Dozens of loss-of-function missense variants characterized (e.g. R83C prevalent in
Ashkenazi Jews; V166G, T16R, Y209C, G188R, K76N, R170Q — several show complete loss of
enzyme activity in expression assays). GSD1b (a distinct entity) is caused by SLC37A4/G6PT
transporter defects, not G6PC1.

## Existing-annotation notes / provenance issues

- PMID:10318794 ("Transmembrane topology of human glucose 6-phosphate transporter")
  is primarily about the G6P transporter (SLC37A4/G6PT). GOA carries three P35575
  annotations citing it (GO:0004346 IDA, GO:0016020 IDA, GO:0005789 TAS). Per curation
  policy I do NOT REMOVE experimental annotations on the basis of the abstract
  foregrounding the transporter; the MF/location are correct for G6PC1. Marked
  MF-IDA as ACCEPT; the generic GO:0016020 membrane IDA marked as over-annotated in favor
  of the specific ER membrane term.
- PMID:15661744 ("Brain contains a functional glucose-6-phosphatase complex...") abstract
  foregrounds glucose-6-phosphatase-beta (G6PC3), but MGI assigned an IDA GO:0004346 to
  P35575. Function is correct for the gene; ACCEPT (defer to curator; do not REMOVE on
  abstract alone).
- GO:0042301 phosphate ion binding (IMP, PMID:12093795): the paper shows His-176 is the
  covalent phosphate acceptor (phosphohistidine intermediate) and Arg-83 positions the
  phosphate; "phosphate ion binding" is a mechanistic sub-aspect of catalysis rather than
  a standalone core MF. Kept as non-core.
- IEA GO:1904638 response to resveratrol, GO:0032094 response to food, GO:0009743 response
  to carbohydrate, GO:0032868/GO:0032869 response to insulin, GO:0031667 response to
  nutrient levels: all Ensembl-projected from rat P43428. These reflect transcriptional
  regulation of the gene (G6PC1 is a canonical insulin/gluconeogenic transcriptional
  target), not molecular functions of the protein; kept as non-core.
- GO:0005515 protein binding (IPI, PMID:32814053; partners WFS1/O76024 and RNF11/Q9Y3C5
  via IntAct Y2H): uninformative bare protein-binding; MARK_AS_OVER_ANNOTATED per policy.

## Core functions

- MF: GO:0004346 glucose-6-phosphatase activity (EC 3.1.3.9)
- BP: GO:0006094 gluconeogenesis; GO:0042593 glucose homeostasis
- CC: GO:0005789 endoplasmic reticulum membrane (active site luminal)
</content>
</invoke>
```

</details>

## Completed interaction and organelle checks

The original Haenig network table has separate G6PC1–WFS1 and G6PC1–RNF11 contexts, supported by positive human-protein yeast two-hybrid records. Exact construct boundaries and mammalian validation remain unresolved; neither screening association supplies a new catalytic core [PMID:32814053]. The ER IBA and IEA assertions are retained after actual lineage and source/topology checks; the root organelle remains informative alongside the ER-membrane annotation. Generic membrane is a separate granularity issue.

All 40 current source contexts have manual decisions. The earlier stored review combined the two Haenig contexts, so it contains 39 rows; the retained original source export has 40. The completed native stage reconciled the genuine parser output and preserved both partner contexts without creating a new seed. The full inherited review and journal remain historical provenance.

## Native reconciliation — 2026-11-01

The same working lane was reused for a genuine no-seed target fetch. The original 39-row review, provider artifacts and existing sources remained unchanged. The first native stage stopped after target acquisition because the genuine UniProt record also listed R-HSA-9940951. Its exact missing path was qualified before a remaining-phase continuation acquired only the 35 absent sources; target acquisition was not repeated. The final source union is 56 objects (21 immutable existing and 35 acquired). All 40 original/export/parser contexts, all 16 export columns, literal donor order, and both declared 357/176-residue products reconcile. No activity is inferred for the short product.

All 28 accepted reference titles already match native records; no title correction or additional scientific assessment was needed. Both active inherited core snippets pass exact native-cache substring checks. The other 40 inherited quotation associations and the complete old review remain historical-only evidence. No quotation, NEW annotation or provider output was added. Native full text is available for PMID16625196, PMID27366200 and PMID39847333; other publication access limits remain explicit in the source guide. Actual publication/Reactome acquisition outputs were read, including failed full-text fallbacks and the existing package deprecation warning.

The accepted transfer has been applied and the scoped local checks completed; publication and remote review remain pending.

## Applied review and local checks — 2026-11-01

Target default validation passed with three advisories: two supported generic-binding rows and the unused inherited falcon file. Strict GOA matching passed for all 40 contexts. Native EDIT history validation, DRAFT status audit, private rendering, scoped whitespace, source preservation and retained-state conservation passed. The existing pkg_resources deprecation warning is retained separately from the three curation advisories. No source, ontology cache, scientific judgment, quotation or provider output was changed during application.

The native EDIT record is `history/genes/human/G6PC1/2026-11-01T131323Z-codex-49cefb.yaml`. Actions remain 26 ACCEPT, seven KEEP_AS_NON_CORE, five TOO_GENERAL and two UNDECIDED. All 28 manual reference assessments, the catalytic core, 357/176-residue product declarations and two active excerpts remain exactly as approved. The complete old journal above is historical text; its earlier actions and assertions do not supersede these current judgments.
