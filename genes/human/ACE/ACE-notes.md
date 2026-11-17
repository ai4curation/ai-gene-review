# ACE curation notes

## 2026-11-15 — initialization and primary-source review

The native fetch identifies human ACE as UniProt P12821 / HGNC:2707. It seeded
144 annotation contexts from 147 GOA rows and four alternative-product records.
The annotation decisions are still pending. ACE is distinct from ACE2; the
review must distinguish the two-domain somatic enzyme, its shed ectodomain,
the alternatively spliced soluble product, and the testis-specific C-domain
isoform. The native product identifiers and sequences remain unedited.

Falcon research failed authentication; its Perplexity fallback returned HTTP
401 with an insufficient-quota response. Neither produced a research document.
Research therefore proceeds from primary publications, native UniProt evidence,
GO definitions and existing GO-CAMs. These notes are manually authored and are
not provider-generated research.

The fetch recovered full text for several papers, including PMID:15283675,
PMID:17077303 and PMID:19773553. Two existing full-text caches,
PMID:16154999 and PMID:23257181, were restored from the pinned main revision
after automatic retrieval returned only their unchanged abstract sections.
All other source changes still require final preservation and quotation checks.

### Catalytic and isoform boundaries

Both homologous domains of somatic ACE are catalytically active. Use the direct
domain experiments in [PMID:1851160, *The two homologous domains of human
angiotensin I-converting enzyme are both catalytically active*](https://pubmed.ncbi.nlm.nih.gov/1851160/)
when judging angiotensin-I cleavage; do not silently equate a synthetic-substrate
assay with an assay of the physiological substrate.

Ac-SDKP hydrolysis is N-domain-preferred rather than universally exclusive to
that domain. The older study reports that the N-active site
"hydrolyzes the peptide 50 times faster compared with the C-active site"
([PMID:7876104](https://pubmed.ncbi.nlm.nih.gov/7876104/)). A later study states:
"The selectivity of Ac-SDKP reported here for the individual domains (N-domain and C-domain) is only 2-fold."
([PMID:26403559, *Structural basis of Ac-SDKP hydrolysis by Angiotensin-I
converting enzyme*](https://pubmed.ncbi.nlm.nih.gov/26403559/)). Construct and
assay conditions matter; the description and core functions should preserve
this distinction rather than repeat a universal numerical selectivity.

The full text of [PMID:19773553](https://pubmed.ncbi.nlm.nih.gov/19773553/)
distinguishes Aβ42-to-Aβ40 conversion from degradation into other fragments.
The N-domain performs the former in the reported assays; both domains can
participate in the latter. This does not establish equivalent activities for
all ACE isoforms or an unqualified in-vivo disease mechanism.

### Process, location and ontology checks in progress

The cached GO-CAMs `6246724f00000549` and `6246724f00000632` already place ACE's
peptidyl-dipeptidase activity in angiotensin maturation and bradykinin
catabolism. These are existing modeled activities, not missing pathway terms.

The primary human ACE/BDKRB2 study
[PMID:17077303](https://pubmed.ncbi.nlm.nih.gov/17077303/) investigates physical
association and receptor responses with ACE-resistant bradykinin analogues.
Its signaling results cannot all be dismissed as consequences of reduced
bradykinin degradation. Final annotations must remain bounded by the tested
constructs, cells and readouts.

Term definitions require particular care: hydrolysis of a dipeptide, release
of a terminal dipeptide from a longer substrate, and release of a single
terminal residue are different molecular functions. Likewise, acquisition of
hematopoietic-stem-cell identity is different from regulation of stem-cell
proliferation. Experimental biological observations and possible ontology
placement problems must be adjudicated separately.

The testis-specific UniProt product is P12821-3. A RefSeq identifier described
as "isoform 2" in a proteomics table must not be mapped automatically to
UniProt P12821-2. Claims about soluble ACE must also distinguish alternative
splicing from proteolytic shedding
([PMID:9642152](https://pubmed.ncbi.nlm.nih.gov/9642152/)).

Next steps are to complete the source-specific annotation decisions, inspect
inaccessible or supplementary evidence where possible, synthesize the core
functions and validate every authored quotation and term. No completion credit
is assigned by this initialization.

## 2026-11-15 — completed draft and independent review

All 144 native annotation contexts now have explicit decisions: 67 ACCEPT,
24 KEEP_AS_NON_CORE, 23 UNDECIDED, 14 TOO_GENERAL, 10 MARK_AS_OVER_ANNOTATED
and six MODIFY. No NEW annotation was added. DRAFT records the remaining
scientific uncertainty; it does not mean the unavailable sources were guessed.
The original annotation identities, evidence codes, alternative-product records,
GOA file and UniProt record remain unchanged.

The 23 undecided contexts preserve specific limits: metadata-only historical
papers; missing dataset-specific protein tables; cytoplasmic/lysosomal assay
context; fertility versus spermatogenesis/gonad development; and the distinction
between free-dipeptide hydrolysis and terminal dipeptide release. Positive
independent evidence for a function does not authenticate every old source
context. No experimental annotation was removed because its title emphasized
another gene, species or paralog.

The principal catalytic core comprises peptidyl-dipeptidase activity in
angiotensin maturation and bradykinin catabolism. Secondary endoproteolysis is
retained as non-core. The PAINT loss check reported no IRD or IKR loss on the
ACE lineage. A human accession among IBA descendant evidence is not circular
support. The existing GO-CAMs already represent the two principal catalytic
processes, so there is no missing-process proposal here.

Independent review corrected the interpretation of
[PMID:25017399](https://pubmed.ncbi.nlm.nih.gov/25017399/): cSrc is activated and
Cx43 is depleted. These results do not establish the two transferred
gene-expression mechanisms, which are marked overannotated. The bounded
gap-junction regulatory interpretation remains non-core; neither a direct ACE
assembly function nor ACE cleavage of Cx43 is asserted. The smooth-muscle
migration reason quotes the measured migration response in
[PMID:1750504](https://pubmed.ncbi.nlm.nih.gov/1750504/), separately from the
proliferation result.

The metallocarboxypeptidase term specifies single-terminal-residue release,
whereas peptidyl-dipeptidase releases a terminal dipeptide. The
metallodipeptidase source [PMID:7961923](https://pubmed.ncbi.nlm.nih.gov/7961923/)
is abstract-only and describes Hip-His-Leu kinetics; an additional assay in
the inaccessible full text cannot be excluded. The N-terminal tripeptide
release reported in [PMID:2983326](https://pubmed.ncbi.nlm.nih.gov/2983326/)
is retained as an ontology-scope question because GO:0008240 currently inherits
a serine-peptidase mechanism. Neither observation is rewritten to fit the
enzyme's conventional name.

### Independently checked location provenance

The [NIH Urinary Exosomes table](https://esbl.nhlbi.nih.gov/UrinaryExosomes/)
lists ACE isoform 1 precursor NP_000780 with Peptide # 23 and references 1/2,
and isoform 2 precursor NP_690043 with Peptide # 12 and reference 2.
Reference 1 is PMID:15326289 and reference 2 is PMID:19056867. The column does
not assert isoform-unique peptides. These data support detection in vesicle
preparations, not vesicle biogenesis. The inspected response SHA256 was
`b15b505bbf97b6ec5bb35d7b5ca29ab43dce9d526c9b461822c2ec2af25285b3`.
The other proteomic studies' specific ACE rows remain unresolved.

Reactome [R-HSA-9614933](https://reactome.org/content/detail/R-HSA-9614933)
has input entity 2065414, ACE(30-1232), explicitly linked to P12821 and
extracellular region GO:0005576. In
[R-HSA-2022398](https://reactome.org/content/detail/R-HSA-2022398), catalyst
2022372 uses complex 9856095 containing P12821 component 508496,
ACE(30-1306), at plasma membrane GO:0005886. These entities were checked through
the Reactome ContentService API, separately from the reaction titles.

Historical article residue numbers are not silently converted to UniProt
precursor coordinates. The shed-chain identifier is PRO_0000028531; the
Somatic-2 transcript in PMID:9642152 is not treated as proof of a protein with
the same activity as that proteolytic product.

### Source preservation and companion correction

Full-text retrieval added evidence for PMID:15283675, PMID:17077303,
PMID:18077343 and PMID:19773553, and additional text for PMID:15326289.
Existing text and its bound quotations were checked before retaining these
native fetch outputs. Six other publication changes contained only whitespace,
publication-type metadata or removal of a duplicate abstract; the retained
Git versions were restored with a compact receipt.

Four existing rat Ace donor rationales were corrected in the same workstream:
unresolved actin-binding provenance, misdescribed mouse angiotensin-metabolism
papers, and two overconfident free-dipeptide activity corrections. All rat
native annotation identities and its other 133 decisions remain unchanged.
This companion correction earns no additional human locus credit.

## 2026-11-15 — PR #6395 review follow-up

The final action counts supersede the initial draft tally above: 75 ACCEPT,
24 KEEP_AS_NON_CORE, 23 UNDECIDED, eight TOO_GENERAL,
10 MARK_AS_OVER_ANNOTATED and four MODIFY; no NEW annotations.

The eight GO:0008237 metallopeptidase rows now retain the informative
metal-dependent mechanism of the core reaction. GO:0008241 describes terminal
dipeptide removal without encoding that mechanism, and the non-core
metalloendopeptidase activity does not replace the core mechanistic assertion.
This also follows the 2026-11-14 maintainer ruling on informative mechanism
classes. There are four IDA rows in this eight-row group; its other evidence
contexts remain unchanged.

The two broad GO:0006508 proteolysis rows are now TOO_GENERAL. Fresh QuickGO
inspection confirmed the accepted angiotensin-maturation ancestry:
[GO:0002003](https://www.ebi.ac.uk/QuickGO/term/GO:0002003) →
GO:0016486 → GO:0140448 → GO:0016485 → GO:0006508, all `is_a` edges.
GO:0043171 peptide catabolic process lies outside that ancestry, so the former
replacement was not the claimed refinement. Its separate native rows remain.

The load-bearing tripeptidase ancestry was independently rechecked against
[GO:0008240](https://www.ebi.ac.uk/QuickGO/term/GO:0008240),
[GO:0070008](https://www.ebi.ac.uk/QuickGO/term/GO:0070008) and
[GO:0008236](https://www.ebi.ac.uk/QuickGO/term/GO:0008236):
GO:0008240 `is_a` GO:0070008 `is_a` GO:0008236. The parent explicitly specifies
serine-catalytic chemistry. The zinc-enzyme mechanism mismatch therefore remains
an ontology-scope question, without dismissing the observed substrate cleavage.

The description now states the mouse sperm-ACE fertility requirement plainly,
supported by PMID:11723129 and PMID:12777443. The gap-junction reasons distinguish
loss of channel-forming Cx43 subunits from regulation of production of the gene
product. Source-specific UNDECIDED contexts are retained because the relevant
historical papers or source-specific assay details remain inaccessible; they
are not converted into verified original experiments by independent support
for the same biological function.
