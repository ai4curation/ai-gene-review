# HBA2 research and annotation review

## 2026-11-15 — locus identity and shared protein evidence

HBA2 is HGNC:4824, NCBI Gene 3040, ENSG00000188536 and transcript NM_000517.
HBA1 is a distinct locus (HGNC:4823, NCBI Gene 3039, ENSG00000206172,
NM_000558). The [official HBA2 HGNC record](https://rest.genenames.org/fetch/hgnc_id/HGNC:4824)
and [UniProt P69905](https://rest.uniprot.org/uniprotkb/P69905.json) map both loci
to one alpha-globin protein. PMID:2981252 explicitly reports that they
“encode identical alpha-globin proteins” and illustrates locus assignment of
structural variants. A protein assay therefore supports the shared product;
attribution to a particular locus requires genetic or transcript evidence.

The native fetch used the symbol HBA2 with explicit accession P69905. Using the
first primary gene name in UniProt alone would incorrectly collapse this locus
into HBA1. The resulting review has gene_symbol HBA2, while every machine-sourced
GOA field retains its original value. Its 85 annotation contexts are exactly
equal to the 85 native contexts in the independently reviewed HBA1 record
(source commit ddc7bcc0cc33bfe50d61e5026b8af7bcaf77921e). GOA and UniProt bytes
also match. No gene names, donors, qualifiers or source identifiers were rewritten.

The [ClinGen HBA2 assertions](https://search.clinicalgenome.org/kb/genes/HGNC:4824)
were checked against the campaign snapshot. HBA2-related alpha-thalassemia
spectrum is AR/Definitive (2023-06-28). Familial erythrocytosis 7 is AD/Limited
(2023-10-25); alpha-type methemoglobinemia is AD/Limited (2024-03-28); unstable
hemoglobin disease is AD/Limited (2024-02-28). These strengths are not copied
from HBA1. Variant effects on dosage, oxygen affinity, ferric-state stability or
protein stability do not change the normal protein's oxygen-carrier function.
No disease classification is converted into a new GO annotation.

### Expression is locus-specific; normal protein chemistry is shared

The accessible primary abstracts establish several useful distinctions:

- PMID:4044827 measures human reticulocyte **mRNA**, reporting “alpha 2-globin
  mRNA is present at an average 2.8-fold excess to alpha 1.” The same study
  reports deletion-associated compensation. This is not a universal protein
  output percentage or a claim that HBA1 contributes nothing.
- PMID:1571559 examines human embryonic/early fetal erythroid RNA and reports
  equal embryonic expression followed by “dominant expression of the alpha
  2-globin locus at week 8 in utero.” Its transgenic-mouse observations are
  corroborating, not a substitute for the explicitly reported human samples.
  Regulation of HBA2 expression does not make alpha-globin a transcriptional or
  developmental regulator.
- PMID:39633569, retained as full text, quantifies HBA2 and HBA1 separately by
  RT-ddPCR in perfused human resistance arteries. HBA2/HBA1 transcript ratios
  were 2.38±0.56 in arterial tissue and 1.64±0.25 in whole blood. The study
  documents blood-contamination controls. Crucially, its RNA in-situ experiment
  probes **HBA1**, not HBA2. Thus HBA2 arterial-tissue expression is established,
  while HBA2-specific endothelial in-situ localization is not claimed.

The newer human vascular study also reports alpha/beta-globin, eNOS and CYB5R3
complexes and NOS-dependent vasoreactivity. These protein and deletion results
concern shared alpha-globin and dosage, not a uniquely HBA2 biochemical activity.
Its finding that “Alpha and beta globin subunits of hemoglobin interact with eNOS
to restrict NO signaling in human resistance arteries” supports the bounded
vascular context, not directed NO transport or an extra developmental process.

### Functional synthesis and annotation decisions

All 85 native contexts were assessed using their original source references,
the shared protein literature and the locus distinctions above: 27 ACCEPT,
37 KEEP_AS_NON_CORE, 10 MODIFY, 10 UNDECIDED and one MARK_AS_OVER_ANNOTATED.
One additional NEW molecular-function context gives 86 entries in total.
Both native contributes_to qualifiers are preserved.

The core unit is heme-dependent oxygen carriage in hemoglobin heterotetramers,
with reversible N-terminal carbamation contributing directly to CO2 transport.
The alpha chain supplies this chemical carriage, rather than serving as a passive
substrate for another enzyme. PMID:11307949 supports oxygen affinity and
allosteric regulation; PMID:16765986 provides oxygen-ligand structural evidence;
Reactome R-HSA-1237325 and R-HSA-1247668 describe carbamation and gas exchange.
Carbon monoxide binding is not carbon dioxide transport, and carbonic-anhydrase
activity is not assigned to alpha-globin.

Specific alpha/beta-like assembly interactions are refined to GO:0046982.
For the ligand-focused PMIDs:10390349 and 11724557, that refinement explicitly
rests on separately cited assembly evidence (PMIDs:1552945 and 15550245), not an
assertion that the ligand experiments measured assembly kinetics. Supported
generic interactions remain non-core under the user's ClinGen exception. No
adaptor or other molecular function is invented from a screening partner name.
UniProt CC:INTERACTION and the directly checked IntAct records share a curation
lineage and are not independent experimental replications.

The six native IBA contexts match positive IBD assertions at PTN000154218 in the
retained PAINT family slice. P69905 appears with the HBA2 label in that mapping;
this neither excludes HBA1 nor establishes locus-specific expression. Human
self-inclusion is legitimate descendant experimental evidence. No inferred
loss boundary, donor-count weakness or unverified finer topology is asserted.
The retained GO-CAM index has no P69905 match. Native PANTHER evidence includes
the complete 810-member family fetch, rather than its discarded partial retry.

PMID:36302779 directly assays purified human deoxyferrous alpha-globin reducing
nitrite and forming ferrous-NO under reducing conditions. This supports NEW
GO:0098809 nitrite reductase activity as a contextual MF outside the respiratory
core. The [live term records](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0098809,GO:0050421,GO:0008942)
were verified during the shared-protein review: GO:0050421 specifies cytochrome c
in its reaction, while GO:0008942 specifies NAD(P)H/ammonium. Neither specificity
is demonstrated by the dithionite-supported alpha-globin assay. Human myoglobin
also has a direct-assay GO:0098809 annotation, supporting this established term
usage. No broader or narrower nitrite-reductase term is duplicated. Mouse
vascular knockout/exercise results are kept separate from the human protein
assay. In CYB5R3-mediated heme reduction, alpha-globin is the redox client;
that statement does not deny its distinct nitrite-reductase activity.

Peroxidase, peroxide consumption, haptoglobin binding and extracellular
scavenging remain contextual. PMID:19740759 describes peroxide chemistry with
oxidative injury; peroxidase activity alone does not establish protective
cellular oxidant detoxification, so that IEA remains over-annotated.
GO:0005576 remains current; GO:0005615 is obsolete with replacement GO:0005576,
as verified in [GO issue31545](https://github.com/geneontology/go-ontology/issues/31545)
and the linked upstream ontology commits. An older local table is not the live
ontology state.

### Preserved uncertainties and processing boundaries

Ten contexts remain UNDECIDED: the precise E7-protein interaction; two
source-linked AHSP assertions; two older binding contexts; directed NO transport;
and four membrane/vesicle proteomic assignments. Accessible abstracts or main
texts did not recover the necessary source-specific evidence. Titles about
another protein or organism do not invalidate a curator's full-text judgment.
Neither contamination nor citation error is asserted. Missing peptide tables
could resolve a shared P69905 assignment but cannot by themselves identify
HBA2 as the source of an identical wild-type protein.

The erythrocyte-development IBA remains non-core. Its corroborating human
beta-thalassemia quote reports maturation arrest and apoptosis caused by globin
imbalance; this is not proof of normal transcriptional or developmental
regulation by alpha-globin.

Structured processing separates mature alpha-globin (2–142, PRO_0000052653)
from the hemopressin segment (96–104, PRO_0000455882). PMID:18077343's rat
PVNFKFLSH differs from human PVNFKLLSH. PMID:20505104 administers the latter
sequence to rodents; PMID:22952224's human-plasma observations concern longer
pepcans. No endogenous human nine-mer occurrence, appetite/pain role or
HBA2-specific peptide source is presupposed. These uncertainties and the ten
source-level decisions justify DRAFT status.

### Research provenance

Research reused the verified shared-protein sources and added four native-fetched
locus/vascular publications. PMID:39633569 has cached full text; the other three
new papers have cached abstracts only, and their findings are restricted to
those accessible statements. Native GOA, UniProt, publications, Reactome and
PANTHER files were not hand-edited. Reused sources are pinned to retained Git
objects, without per-gene copies of runtimes or large source stores.

The recent Falcon authentication failure and Perplexity quota failure were
already established during HAMP research. No new provider request or fabricated
provider report is claimed here; the primary-source research is documented in
these notes. Schema, reference, quote, history and rendering checks follow this
completed draft, together with independent annotation and locus review.

### Completed checks

Schema/ontology validation passed with 16 expected generic-binding warnings
under the user's exception and no errors. Reference validation checked 96
snippets and 47 titles without issues; the independent quote check verified all
157 occurrences, including the non-PMID sources and reference findings, with
zero unchecked. Canonical rendering passed in memory without an HTML artifact
or graphical inspection. Independent annotation-transfer and final locus/science
reviews found no actionable concern. A final reference-review wording
clarification explicitly separates alpha-globin as a heme-reductase substrate
from its own nitrite-reductase activity; it changes no evidence quotation,
annotation decision or source field.

## PR #6374 review follow-up (2026-11-15)

The oxygen-binding and two heme-binding reasons now address their own ligands.
The oxygen row retains the human oxyhemoglobin structure and adds the native
O2 feature; the heme rows add the native heme-b feature and resolved prosthetic
heme groups from PMID:28665412. Precursor His88 is the proximal residue
(conventional mature-alpha His87); precursor His59 is the distal residue.

Four MODIFY rows now quote their own original papers. Their reasons distinguish
engineered alpha-chain fusion (PMID:10930828), assembled ferric methemoglobin
cryo-EM (PMID:28665412), beta6-mutant fiber packing (PMID:9830011), and engineered
globin disassembly/reassembly (PMID:9894000). Independent alpha-beta dimer and
assembly evidence remains the basis for the heterodimerization refinement;
structural observations are not described as wild-type assembly kinetics.

The four unresolved proteomics rows now rest only on inaccessible protein-level
evidence. Shared accession P69905 is not itself a reason to withhold an
annotation from either locus: verified shared-protein observations apply to
both identical products, without establishing which locus supplied a particular
sample. The source-specific protein tables remain unverified.

### Ontology and optional suggestions

A [live QuickGO ancestry check](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0042744/ancestors?relations=is_a,part_of)
on 2026-11-15 found GO:0008150, GO:0072593, GO:0009056, GO:0008152,
GO:0009987, GO:0042743 and GO:0042744 in the is_a/part_of closure of
GO:0042744. GO:0098869 is absent. Thus peroxide breakdown does not entail
cellular oxidant detoxification; the existing non-core/over-annotated split
remains consistent. This establishes non-descendancy, not an immediate sibling
relationship. The payload SHA256 was
`9b348828cb50570c24af233d855f2d028b473c31089358ae8fff176bca0bbd25`.

GO:0070026 nitric oxide binding is a valid possible MF for the spectroscopic
observation in PMID:8292032. This bounded follow-up retains that observation
and the existing NO-related question without adding another annotation to the
DRAFT; it does not reject the ligand-binding finding or require in-vivo evidence
for all molecular functions. The unresolved NO-transport process is unchanged.

The [GO:0072562 definition](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0072562)
specifies a cell-derived phospholipid microvesicle. Evidence for soluble
extracellular hemoglobin and haptoglobin binding does not by itself establish
residence in that compartment. The blood-microparticle row therefore remains
UNDECIDED until the source protein table or equivalent compartment-specific
evidence is available; this does not reject extracellular hemoglobin.

### Shared-accession tooling audit

Code inspection at base `c81db5dece15279feec216530b401fc4465b578e` confirms
that keeping both locus-specific folders and the genuine shared UniProt
accession is supported for ordinary export and browser display, with these
current limits:

- `src/ai_gene_review/export/annotation_export.py` appends review rows and
  preserves each gene symbol and source-path link. The browser uses array
  positions; payload compaction preserves both records. No review is replaced
  merely because its accession is P69905.
- The exported annotation ID uses accession, GO term and evidence code without
  locus, reference or full row context. These IDs can collide within and across
  reviews. External consumers must not treat that field as a unique row key.
  DuckDB redundancy calculations group by protein ID and skip equal annotation
  IDs, so their derived comparisons do not fully distinguish loci or contexts.
- Propagation export keys reviews by species/gene folder and retains distinct
  links, but its displayed target comes from native GOA SYMBOL. Both native
  alpha-globin files say HBA1; HBA2-linked rows can therefore display HBA1, and
  search does not independently include the review folder name.
- `src/ai_gene_review/etl/gocam.py` indexes model activities by their enabled_by
  protein identifier. A P69905 join is a shared-protein join, not a locus-specific
  expression assertion. `src/ai_gene_review/gocam_compartments.py` selects the
  first sorted GOA file per accession with `setdefault`; with both folders
  present it selects HBA1, so differing HBA2 location judgments would not enter
  that lookup.

A focused tooling follow-up should address unique annotation context keys,
propagation display identity and shared-accession location-review aggregation.
No source accession or native GOA symbol was rewritten to conceal these limits.

### Follow-up validation

The revised review passes schema/ontology validation with the same 16 expected
generic-binding warnings and no errors. Reference validation checks 102 snippets
and 47 titles with no issues; the separate quote checker verifies all 166 quote
occurrences, with zero unchecked or blocking. Canonical rendering passes in
memory. Independent read-only scientific review finds no actionable concern.
All 85 native contexts, the existing NEW row, decisions, propagation assessments,
core functions and prior evidence quotations are preserved.
