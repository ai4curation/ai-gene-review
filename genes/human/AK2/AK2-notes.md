# AK2 review notes

## 2026-09-27 — source3 baseline and research

HGNC:362 is the approved human symbol AK2; the archived official HGNC subset
has no previous or alias symbols. UniProt P54819 also lists ADK2. Fresh direct
GitHub API checks at main `30a9290881824baaacab2b681d7808f572c4cef6`
found the canonical five gene paths and task branch absent, with no open
canonical-title PR. Separate ADK2 path/title checks found no alias directory or
open PR. All three exact source3 seed hashes match the import receipt; no
reviewer-authored baseline existed. The 30 seeded assertions, 14 original
references and six alternative products are preserved for audit. Publication
base `d35dcc30b44924f79c0510b281ae824aa536848a` also lacks the gene paths.

Default Falcon research with `--fallback perplexity-lite --timeout 1200` and
normal `fetch-gene-pmids` were launched concurrently. Both provider commands
failed before contacting a provider because uvx could not resolve PyPI to
install deep-research-client; each returned 2, and the wrapper returned 1.
No provider report was produced. The cache command returned 0 and found all
five seeded PMID records already cached; it did not refresh or modify them.
Logs: `/tmp/AK2-provider.log` and `/tmp/AK2-seed-fetch.log`. Research proceeds
through cached primary sources and separately documented primary web access.

## Evidence and annotation decisions

The 30 original assertions were reviewed individually. Their source objects,
qualifiers, supporting entities and six alternative products remain unchanged.
Eight generic protein-binding rows are removed as uninformative; this does not
reject their reported interactions. Three broad electronic function/process
rows are refined to measured AMP kinase activity or adenylate interconversion.
Two sperm locations are retained as contextual ortholog inferences. Exosomal
localization remains unresolved because its target-specific supplement was not
recovered. One new molecular-function proposal is described below.

### Catalysis, isoforms and compartment

PMID:6182143 was verified against PubMed, and its original JBC full article was
read through the author-uploaded text on [ResearchGate publication 17011438](https://www.researchgate.net/publication/17011438_Adenosine_triphosphate-adenosine-5%27-monophosphate_phosphotransferase_from_normal_human_liver_mitochondria_Isolation_chemical_properties_and_immunochemical_comparison_with_Duchenne_dystrophic_serum_abe)
on 2026-09-27 (DOI 10.1016/S0021-9258(18)33631-7). Methods identify human
liver and separate coupled assays for both directions; Results and Table III
support adenine-nucleotide phosphate transfer by purified mitochondrial enzyme.
The local cache is metadata-only and was not modified. PMID:9504408 independently
reports active purified recombinant human AK2A and AK2B, not all six products.

The exact Reactome:R-HSA-110144 and Reactome:R-HSA-110145 summaries separate
human enzymology from rat-derived intermembrane-space inference. UniProt agrees
with that compartment. The human MitoCoP study (PMID:34800366, cached full text)
is retained at its original broad mitochondrion resolution, with curator
deference because the AK2-specific supplement was not re-extracted. It does not
supply an independent intermembrane-space assay. GO:0005737 is cytoplasm,
including cytoplasmic organelles, rather than cytosol; the inherited broad
location is therefore appropriate. Apoptotic release reported in PMID:10218571
is a contextual mammalian observation, not the basis for constitutive cytosol
as a core location.

Live AmiGO definitions were checked for GO:0004017, GO:0005737, GO:0006172,
GO:0015949, GO:0055086 and GO:0072542. ADP formation is direct chemical work by
AK2, not synthesis of the adenine/ribose backbone. AMP and ATP metabolism are
also direct substrate/product participation. The one integrated metabolic core
retains those scopes without manufacturing a differentiation or ATP-hydrolysis
annotation.

### Propagation and contextual locations

The cached `interpro/panther/PTHR23359/paint.tsv` includes the exact IBD assertions
at PTN000599576 (kinase and cytoplasm), PTN000599693 (ADP biosynthesis), and
PTN001916109 (mitochondrion). Only the PTNs are entered as IBA source entities.
Human AK2 among the kinase descendants is valid experimental grounding, not
circular support. The family tree/MSA and all loss events were not reconstructed.
InterPro signature membership was checked against the immutable UniProt record;
RHEA:12973 and EC:2.7.4.3 match the direct reaction. ARBA/UniRule condition
internals remain unresolved independently of the supported target functions.

[MGI's comparative Ak2 graph](https://www.informatics.jax.org/homology/GOGraph/Ak2)
(snapshot 2023-03-10) traces both sperm-compartment donor terms to mouse IDA
PMID:16790685. The primary abstract specifically identifies AK2 in the sperm
midpiece mitochondrial sheath, distinct from AK1 elsewhere in the flagellum.
Mouse Q9WTP6/ENSMUSP00000030583 is the donor; no direct human sperm assay was
claimed. Conserved mitochondrial targeting makes a contextual transfer
plausible. Full source was not recovered, so an axonemal structural or motility
mechanism is not inferred.

PMID:20458337 has an abstract-only cache. The original [author-uploaded main
article](https://www.researchgate.net/publication/44588150_MHC_class_II-associated_proteins_in_B-cell_exosomes_and_potential_functional_implications_for_exosome_biogenesis)
was inspected, but its AK2-specific supplementary peptide row was not recovered.
Its total exosome proteome and MHC-II co-immunoprecipitated subset are different
assays. The annotation remains UNDECIDED; no claim of contamination or false
localization follows from the dominant mitochondrial pool.

### Binding records and the DUSP26 activity proposal

The original PMID:32814053 [institutional full PDF](https://edoc.mdc-berlin.de/id/eprint/19322/1/19322oa.pdf)
was read. It describes repeated human Y2H screens and integration with other
interaction evidence. The eight exact partners are also listed in the immutable
UniProt record. No AK2-specific functional mechanism for those partners was
established from the main paper, and pair-level supplements were not reanalyzed.
REMOVE implements generic-binding policy, not a finding that these pairs do
not bind. DUSP26 is not substituted for one of these unrelated pairs.

PMID:24548998 was independently verified at [PubMed](https://pubmed.ncbi.nlm.nih.gov/24548998/),
with full primary Methods/Results read through the [Nature PDF](https://www.nature.com/articles/ncomms4351.pdf)
and indexed PMC3948464 (DOI 10.1038/ncomms4351). Figures 3–4 directly test
recombinant human AK2 binding and activation of DUSP26. The phosphatase acts on
pNPP and Plk-phosphorylated FADD; kinase-defective AK2 K28E retains activation.
AK2 alone has no measured phosphatase activity, and AK3/FADD controls do not
stimulate DUSP26. Tagged proteins and gel-filtration fractions do not establish
fixed endogenous complex stoichiometry. Independent annotation_a4galt reading
confirmed these assay boundaries and found no blocker for the activator MF.

NEW checks: AK2 performs activation, DUSP26 performs dephosphorylation.
GO:0072542 requires binding and increased protein-phosphatase activity; its
parents GO:0019211/GO:0019888 are regulator terms. Its narrower tyrosine-specific
child is not appropriate for the FADD phosphoserine assay. Neither this term
nor its ancestors/descendants occur in the seeded AK2 set. Local AMBRA1 and
CALM1 GOA files contain experimental GO:0072542 annotations, establishing
comparable noncatalytic phosphatase-activator usage. These database rows are a
term-usage check, not substituted experimental evidence for AK2. An exact
P54819/AK2 search of `gocams/index.tsv` found no target activity. The proposal
is kept distinct from the dominant metabolic core because its general tissue
importance is unresolved. No new cell-proliferation, apoptosis or differentiation
process is proposed. PMID:17952061's primary abstract is retained as signaling
context, with full construct/control details unresolved.

### Mendelian context and source access

The cached PMID:19043417 human genetics/zebrafish abstract, primary
[PMID:19043416 abstract and Figure 3](https://pubmed.ncbi.nlm.nih.gov/19043416/),
and [PMID:39378586](https://pubmed.ncbi.nlm.nih.gov/39378586/) with indexed full
PMC11830988 establish disease context. Human patient rescue and progenitor
perturbations link nucleotide imbalance and stage-specific metabolic control to
reticular dysgenesis. They establish AK2 necessity; no direct developmental
process is manufactured solely from loss/rescue phenotypes. The latter paper's
DOI is 10.1182/blood.2024024123. Human disease and zebrafish experiments are not
interchanged.

One normal six-ID cache request completed with exit 1 and 0/6 records recovered:
PMID:16790685, PMID:19043416, PMID:39378586, PMID:17952061, PMID:10218571,
PMID:24548998. Every failure was DNS resolution; log `/tmp/AK2-extra-fetch.log`.
External primary access does not create a synthetic cache or change local
`full_text_unavailable` flags. These six remain publication gates. The genuine
provider attempts produced no artifact, so there are no provider-only sources.
The final census includes authored YAML/notes and their decoded DOI/URL
citations, while immutable raw UniProt bibliography is distinguished from
reviewer-cited evidence. No raw data, publication, Reactome or provider bytes
were edited.

## Final independent review and verification

The coordinator independently read all 31 decision objects, propagation
assessments, 22 reference assessments, the integrated core and questions, and
checked the primary DUSP26 activation controls and live term definition.
Biological review passed. A requested Reactome quote-boundary cleanup was
applied without changing its meaning or any decision.

Final `just validate human AK2` passed with one grouped warning covering the
six missing records above; status remains DRAFT. An earlier run found the
singular `failure_mode` spelling, corrected to the schema's `failure_modes`
list before the final full rerun. History validation and rendering passed.
Independent preservation checks confirmed all original source objects,
reference IDs/titles and alternative products; 35 cached quote occurrences
match their immutable sources. The one new DUSP26 excerpt was verified against
the primary PubMed abstract but cannot be checked against a local cache yet.
The recursive authored citation census is 12 PMIDs and three Reactome records;
all DOI occurrences map to those same records, and no provider artifact exists.
Exact hashes, existing-base reuse and five missing-base immutable source3
publication/Reactome dependencies are listed in the frozen manifest.
