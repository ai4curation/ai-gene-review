# ALG13 (Q9NP73) review notes

## Summary of function
ALG13 is the **catalytic (glycosyltransferase) subunit** of the bipartite
**ALG13/ALG14 UDP-N-acetylglucosamine transferase (GnTase)** that catalyses the
**second step of dolichol-linked oligosaccharide (LLO) assembly** in the ER: transfer of
the **second N-acetylglucosamine (β1,4-linked) from UDP-GlcNAc onto GlcNAc-PP-dolichol**
to form the chitobiose core **GlcNAc2-PP-dolichol** (N,N'-diacetylchitobiosyl
diphosphodolichol). EC 2.4.1.141 = GO:0004577.

- ALG13 provides the UDP-GlcNAc-binding/catalytic (GT28) domain but lacks a
  membrane-spanning region; ALG14 is the membrane anchor that recruits ALG13 to the
  **cytosolic face of the ER membrane**. ALG13 has no GnTase activity unless complexed
  with ALG14. [PMID:16100110, PMID:36200043]
- The active complex = **UDP-N-acetylglucosamine transferase complex (GO:0043541)**;
  ALG13 is a peripheral ER-membrane protein.
- Human ALG13 has 4 isoforms. Only the **short isoform 2 (165 aa)** forms a functional
  complex with ALG14 and supports GnTase/LLO synthesis; the long isoform 1 (1137 aa,
  the displayed/canonical sequence) does **not** bind ALG14 and lacks GnTase activity.
  [PMID:36200043] The GT28 catalytic region is at the N-terminus (aa ~1-125, shared by
  isoforms 1 and 2).
- The long isoform 1 additionally contains an **OTU domain** with intact catalytic
  residues, but **no deubiquitinase activity** was detected in vitro (UniProt CAUTION;
  PMID:23827681). This DUB/proteolysis annotation is not a validated function and is not
  in the GOA TSV under review.

## Disease
Pathogenic ALG13 variants cause **X-linked developmental and epileptic encephalopathy 36
(DEE36 / ALG13-CDG)** — infantile spasms / early-onset epileptic encephalopathy with
neurodevelopmental impairment. Some patients show abnormal transferrin isoelectric
focusing (CDG type I biomarker), though many ALG13-CDG variants have near-normal
transferrin. CDG variants (e.g. K94E, N107S) reduce GnTase activity in vitro.
[PMID:22492991, PMID:36200043, PMID:23934111, PMID:26138355]

## GOA annotation review decisions (genes/human/ALG13/ALG13-goa.tsv)
- GO:0004577 N-acetylglucosaminyldiphosphodolichol N-acetylglucosaminyltransferase activity
  — the exact GOA MF term (= EC 2.4.1.141). Multiple lines (IDA PMID:36200043,
  IMP PMID:22492991, IEA GO_REF:0000120). CORE. ACCEPT.
- GO:0006488 dolichol-linked oligosaccharide biosynthetic process — CORE BP. ACCEPT
  (IMP PMID:22492991; IEA InterPro).
- GO:0006487 protein N-linked glycosylation — downstream BP, acts_upstream_of_positive_effect
  IMP. KEEP_AS_NON_CORE (the direct molecular step is LLO GlcNAc2 formation; N-glycosylation
  is the pathway it feeds).
- GO:0005789 endoplasmic reticulum membrane — CORE CC (EXP PMID:16100110, TAS Reactome, IEA
  SubCell). ACCEPT.
- GO:0098554 cytoplasmic side of endoplasmic reticulum membrane — precise CC, is_active_in,
  IGI PMID:16100110. ACCEPT (more specific than ER membrane; matches biology).
- GO:0003824 catalytic activity (IEA ARBA) — root-level MF, uninformative. MARK_AS_OVER_ANNOTATED.
- GO:0016758 hexosyltransferase activity (IEA InterPro) — parent of GO:0004577; correct but
  too general given the specific term is present. MODIFY -> GO:0004577.
- GO:0005737 cytoplasm (IEA ARBA) — over-general/imprecise; the protein acts as a peripheral
  membrane protein on the cytoplasmic face of the ER (GO:0098554), not free cytoplasm.
  MARK_AS_OVER_ANNOTATED.
- GO:0005515 protein binding (IPI PMID:33961781, with SLC2A4/P14672) — bare protein binding
  from a high-throughput AP-MS interactome (BioPlex). Uninformative; not the biologically
  meaningful ALG13-ALG14 interaction. MARK_AS_OVER_ANNOTATED (per policy: do not REMOVE bare
  protein binding IPI).

## Complex membership
UniProt DR block records GO:0043541 (UDP-N-acetylglucosamine transferase complex, IDA) — used
in core_functions in_complex.

## 2026-09-27 substantive re-review

This section supersedes the earlier action list and its policy descriptions. The
original notes are retained as history. HGNC:30881 approves ALG13 (UniProt Q9NP73),
with previous symbols GLT28D1/CXorf45 and aliases MDS031, YGL047W, FLJ23018, TDRD13
and CDG1S. All five initial files matched main
`ba3ff58d7d2de76dbe3c24b16e05e12369f463fc`; parent checked the canonical and seven
alias PR searches and both local/main alias directories. No overlap was found.

The review preserves all **15 machine-seeded annotation objects**, including their
qualifiers and evidence, all four alternative products and all eleven original
reference identifiers/titles. The sixteenth row was an existing authored NEW
complex proposal, which is withdrawn after the formal scope assessment below. The
current 15 decisions are 12 ACCEPT, 2 MODIFY and 1 REMOVE, with seven explicit
source-provenance blocks (six IEA
rows and the yeast genetic-interaction partner). There are no PENDING decisions.

### Human chemistry and isoform scope

Read the complete cached Methods, Results, Figures 1–5 and Discussion of
[PMID:36200043](https://pmc.ncbi.nlm.nih.gov/articles/PMC9527342/). The investigators
co-expressed human FLAG-ALG13 isoform 2 and His-ALG14 in *E. coli*, purified the
membrane-associated complex sequentially by the two tags, and tested a chemically
prepared GlcNAc-PP-dolichol acceptor with UDP-GlcNAc. LC-MS establishes product
formation, and subsequent yeast ALG1 recognition supports the beta-1,4 chitobiose
linkage. Separately expressed proteins mixed after extraction did not give the
same activity. Human HEK293 co-IP and immunoprecipitated-protein activity assays
compare isoforms 1 and 2 directly. Short isoform 2 binds ALG14 and is active;
long isoform 1 was negative in those assays and did not rescue the yeast
complementation test with ALG14. These findings do not assay all functions of
isoforms 3 and 4. The current description and core explicitly identify the active
short isoform instead of presenting every splice product as an active enzyme.

The mutant assays use membrane extracts and normalized ALG13 abundance; their
relative conversion measurements are not measurements of enzyme activity in
patient brain. The reduced activities of tested variants and near-normal serum
transferrin results can coexist. Neither normal transferrin nor the recombinant
result alone resolves the neuronal disease mechanism. No neural-development or
seizure-process NEW is proposed from necessity/clinical association.

The exact activity GO:0004577 agrees with RHEA:23380/EC:2.4.1.141 and the human
substrates/products. Live [AmiGO](https://amigo.geneontology.org/amigo/term/GO:0004577)
confirms both the reaction and its hexosyltransferase/catalytic ancestry. The
root catalytic and hexosyltransferase rows are MODIFY to this specific term.
Their source identifiers are preserved; ARBA predicates were not reconstructed,
so those source internals remain UNRESOLVED even where independent biology
supports the annotation judgment.

### Localization, pathway and complex scope

[PMID:16100110](https://pubmed.ncbi.nlm.nih.gov/16100110/) is abstract-only locally.
The abstract explicitly distinguishes yeast Alg13/Alg14 recruitment experiments
from human-pair complementation in yeast. The original author-lab PDF route failed;
no direct human microscopy or uninspected topology experiment is claimed.
The retained location combines curator assessment, this conserved functional
recruitment and the independently read human complex/membrane-activity results
in PMID:36200043. The IGI source partner SGD:S000003015 is the preserved yeast
ALG13/YGL047W identifier. Broad cytoplasm remains ACCEPT: it includes the ER
cytoplasmic surface and does not assert an exclusively free cytosolic protein.
The earlier assertion that cytoplasm incorrectly implies free cytoplasm is
withdrawn. Human isoform-1 cytosolic localization is not asserted from yeast data.

The two cached Reactome events distinguish the normal ALG13:ALG14 reaction
(R-HSA-446207) from the defective-ALG14 variant event (R-HSA-5633241). The latter
provides normal enzyme context plus ALG14 variant effects, not a negative
wild-type ALG13 reaction or an ALG13-mutant experiment. Both support the retained
ER compartment with the primary evidence.

[GO:0006487](https://amigo.geneontology.org/amigo/term/GO:0006487) explicitly has
GO:0006488 as a **part_of** child. The prior NON_CORE characterization of the
broader N-linked-glycosylation process as merely downstream is therefore
superseded by ACCEPT. ALG13 performs a sugar-transfer step of precursor assembly;
it does not carry out the later transfer to asparagine itself. The integrated
core uses the more precise existing precursor process, without a redundant NEW
ancestor. The cached production GO-CAM `65c57c3400000687`, activity
`65c57c3400000688`, already models ALG13 GO:0004577 in GO:0006488 at GO:0098554,
using the same three primary references. No missing-process assumption was made.

The original complex NEW had an IDA label but cited the UniProt file. Direct
PMID:36200043 complex purification/co-IP/activity establishes human isoform 2
paired with ALG14. The human ALG14 comparator carries both IBA and IDA from this
paper for GO:0043541, and the ALG13 UniProt DR block already includes that term.
This records existing curator use and does not establish why the GOA snapshot
differs. Crucially, the [current term definition and parents](https://www.informatics.jax.org/vocab/gene_ontology/GO:0043541)
describe a **multienzyme** LLO-synthesis assembly, give yeast Alg7/Alg13/Alg14 as its
composition, and include phosphorus-transferase-complex ancestry. The human
paper establishes the ALG13–ALG14 dimer, **not** a DPAGT1-containing multienzyme
assembly. Existing curator usage does not resolve that evidence/definition gap.
The prior authored NEW is therefore withdrawn and the core `in_complex` identifier
omitted; no immutable experimental source annotation is removed. The demonstrated
ALG13–ALG14 partnership remains explicit in the biological description and core
prose. An ontology question asks whether the dimer and larger assembly should
be distinguished. Neither absence of a larger human complex nor native human
stoichiometry is inferred from these recombinant assays.

### Original clinical source and interaction evidence

[PMID:22492991](https://pubmed.ncbi.nlm.nih.gov/22492991/) is abstract-only in the
normal cache. The Oxford publisher record verifies its identity. The original
[author-uploaded Figure 2B caption](https://www.researchgate.net/publication/230612777_Gene_identification_in_the_congenital_disorders_of_glycosylation_type_I_by_whole-exome_sequencing)
was recovered: it identifies patient/control fibroblast microsomal extracts,
UDP-GlcNAc and radiolabeled GlcNAc1-PP-dolichol, with TLC measurement of the second
GlcNAc product. Full-text download returned 404 and complete Methods were not
read. These positive source findings plus independent 2022 human enzymology
support all three retained IMP assertions without inventing controls or exact
patient residual activity.

BioPlex PMID:33961781 and the UniProt interaction record identify an ALG13–SLC2A4
association. The pair supplement and tested isoform were not independently
recovered. REMOVE of generic GO:0005515 applies because it supplies no resolved
molecular function; it does not deny that interaction or replace its partner with
ALG14. The old notes' policy claim that bare binding must not be removed is
superseded by the current annotation-reviewer policy.

Full cached [PMID:23827681](https://pmc.ncbi.nlm.nih.gov/articles/PMC3705208/)
describes human OTU preparations. ALG13 did not react with Ub-PA, reacted with
haloalkyl probes, and was inactive against the diubiquitin panel. This is an
assay-bound negative, not evidence that every possible substrate or cellular
role of the entire long protein is absent. No DUB/proteolysis activity is added.

Historical notes citations [PMID:23934111](https://pubmed.ncbi.nlm.nih.gov/23934111/)
and [PMID:26138355](https://pubmed.ncbi.nlm.nih.gov/26138355/) were independently
verified against the primary PubMed titles/abstracts. The former reports a human
exome cohort and recurrent ALG13 mutations; the latter reports sporadic infantile
spasm probands including the p.Asn107Ser variant. They support clinical context,
not direct enzymology or a new neural function. Their complete articles were not
inspected.

### Access, provenance and remaining gates

Fresh genuine default Falcon research and fallback perplexity-lite ran concurrently
with normal GOA publication caching. Both research commands failed with exit code 2
while fetching `deep-research-client` from PyPI because DNS resolution failed,
before provider contact. There is no generated provider report, and no manual text
was labeled as provider output. The review rests on manual primary-source analysis.
Logs: `/tmp/ALG13-fresh-research.log` and `/tmp/ALG13-fetch-goa.log` (4/4 GOA
publications already cached). A separate normal fetch of PMID:23934111 and
PMID:26138355 exited 1 with 0/2 cached and terminal DNS errors; log
`/tmp/ALG13-notes-fetch.log`. Both remain missing required source caches.

All source/publication/GO-CAM/Reactome files remain unchanged. Cache-availability
flags describe the actual local record, not external reading: PMID:16100110 and
PMID:22492991 are abstract-only, while PMID:33961781, PMID:36200043 and
PMID:23827681 have cached full-text sections. The BioPlex extraction does not
resolve every pair supplement merely because its full-text flag is true.

A bounded independent consultation by annotation_aars1 confirmed the yeast-versus-human
scope of PMID:16100110 and the stronger human isoform-specific complex evidence
in PMID:36200043. The exact notes-inclusive missing PMID census is 23934111 and
26138355; both cited Reactome records are cached. Status remains DRAFT until the
required caches and any remaining validation warnings are resolved.

Parent independent review accepted the enzyme, isoform, pathway and source-scoped
localization decisions, and identified the unresolved multienzyme scope as a reason
to withdraw the prior complex proposal. That refinement was incorporated before
publication. The broad pathway acceptance remains grounded in the live part_of
relationship and the actual ALG13-catalyzed step.
