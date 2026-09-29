# ATP2B2 notes

## Calcium export and splice-dependent targeting

PMCA2 performs ATP-driven calcium export at the plasma membrane. Human splice constructs expressed in Sf9 cells retain calcium-dependent ATPase activity and form a phosphoenzyme intermediate [PMID:7929331](https://pubmed.ncbi.nlm.nih.gov/7929331/). Recombinant PMCA2 variants and mutants alter calcium-transient clearance in CHO cells [PMID:17234811](https://pmc.ncbi.nlm.nih.gov/articles/PMC1785272/). ATP is a P2Y-receptor agonist in the latter calcium-transient assay; that readout must not be described as a direct ATP-turnover measurement. The two studies therefore supply complementary evidence for one calcium-pump core.

Splicing changes where the pump acts. In polarized MDCK cells, w/a and w/b constructs reach the apical domain, whereas x/b, z/b and z/a are restricted to the basolateral membrane [PMID:12624087](https://pubmed.ncbi.nlm.nih.gov/12624087/). The PDZ-binding tail alone does not explain apical targeting in that model. All eight UniProt alternative products are preserved, including its caution that not every combinatorial product has been individually characterized. Existing GOA rows are not assigned invented isoform identifiers.

## Hearing and cellular context

Human-family genetics, recombinant CHO-cell measurements and mouse hair-cell physiology are distinct evidence in PMID:17234811. Mutant-dependent impairment of calcium clearance supports an auditory role without making PMCA2 the mechanotransduction channel. Donor species for every recombinant parental construct is not established by the Methods paragraph alone. PMID:15829536 describes a hypofunctional PMCA2 variant modifying hearing loss in particular genetic contexts; it does not establish a uniform mechanism or penetrance for every ATP2B2 allele. That record mentions an erratum whose text has not been inspected.

Native human corneal epithelium shows cytoplasmic PMCA2 immunoreactivity [PMID:15765049](https://pubmed.ncbi.nlm.nih.gov/15765049/). This is retained as contextual distribution without inventing soluble cytosolic pump activity. General neuronal and synaptic locations remain distinct from precise neurotransmitter-class and postsynaptic claims that require the original SynGO evidence dossier.

## Unresolved source-specific assertions

The exact P01258 partner is CALCA/calcitonin in UniProt, while the accessible PMID:17689535 abstract concerns calcineurin. Preserve the original machine-supplied partner and mark the exact association unresolved; incomplete full-text access cannot establish that the source is wrong. The ATP2B2-SCRIB target peptide in PMID:30126976 and the exosome proteomics hit in PMID:18570454 likewise require their target-level records. The larger staged PMID:30126976 source was inspected only for selected main-text sections; its supplemental target row was not verified, and the existing abstract-only canonical cache remains unchanged.

PMID:11259493 reports PMCA expression changes during IMR-32 differentiation and faster calcium clearance. This does not by itself establish that ATP2B2 executes neuronal differentiation. Mouse donor assays for ER/cilium/retinal-ribbon localization and cochlear development, and ATP2B2-specific cardiac-conduction evidence, also remain open. No experimental assertion is removed on the basis of an incomplete abstract or a paper's emphasis on another protein.

## Review scope and reading limits

All 58 seeded assertions and eight products are preserved: 27 ACCEPT, nine KEEP_AS_NON_CORE and 22 UNDECIDED. One calcium-export core is retained and no NEW assertion is proposed. The raw 61-row GOA projects to 58 source objects through three fine-ECO pairs; that is recorded by the normal importer, not a claim of identical raw duplicates. PAINT self-support is legitimate descendant evidence and no phylogenetic placement is challenged without a tree-level argument. The local GO-CAM index has no Q01814 match; this is not a claim of global model absence.

Falcon and its configured fallback could not start because the pinned client was absent from the offline cache. No provider report was produced. The synthesis uses manual primary-source reading and an independent all-row annotation/core consultation. Canonical sources retain their original availability flags; selected external text does not manufacture a local full-text cache.

- **PMID:11259493**: Complete staged abstract/frontmatter only.
- **PMID:12624087**: Complete staged and official PubMed abstracts; deposited human construct metadata and immutable UniProt isoform locations. Full paper Methods not accessed.
- **PMID:1313367**: Complete staged abstract/frontmatter.
- **PMID:15765049**: Complete staged abstract/frontmatter.
- **PMID:15829536**: Complete staged abstract/frontmatter; original full NEJM Methods unavailable.
- **PMID:17234811**: Complete cached abstract, Results and Discussion text, and Methods from genetic screening through electrophysiology. Figures/plots not visually inspected.
- **PMID:17689535**: Complete canonical and staged abstracts; official UniProt partner identity; original publisher body requests blocked.
- **PMID:18570454**: Complete canonical and staged abstracts; target table unread.
- **PMID:30126976**: Complete canonical/staged abstracts and targeted staged original introduction/Results library design and selections. Canonical is abstract-only; larger quarantined XML alternative is full-text. Main-text searches for ATP2B2/Q01814/PMCA2 returned no hit; supplementary target tables not inspected.
- **PMID:7929331**: Complete staged/official abstracts and original author-deposited paper text: expression-vector/Sf9 Methods, ATPase/calmodulin-overlay Methods, recombinant-expression and phosphoenzyme Results/Figures2–3 captions. No visual figure inspection or complete remaining paper read.

Root separately read complete PMID:17234811 Methods and selected Results/Discussion; the independent consultation read additional Results/Discussion. No figure-pixel or supplemental-table audit is claimed. Validation results will be appended after they run.

## Validation — 2026-09-29

Focused `just validate human ATP2B2` passed with no gene-review advisories. The HTML render succeeded and the scaffolded curation history validated. These checks cover the present review and its references; no new repository-wide validation PASS is claimed. The independent final consistency check preserved all 58 source objects and eight products and verified all six literal quotations against their normal source caches.


## First PR feedback: primary-source follow-up (2026-09-29)

The two action changes are cilium row 18 to ACCEPT and neuronal
differentiation row 29 to MARK_AS_OVER_ANNOTATED. Mouse olfactory cilia evidence
is distinct from hair-cell stereocilia. Complete original differentiation Methods
and selected Results establish upregulation after chemical induction; they do not
establish PMCA2 as the driver of neuronal differentiation. Existing source tuples
and eight alternative products are preserved. The single pump core now names
stereocilia-to-endolymph export, and the biological description includes DFNA82.
The human monogenic deafness paper adds corroboration to the existing non-core
hearing annotations; it does not turn disease into a separate molecular core.

Cardiac-conduction rows 54/55 remain unresolved. Tissue-expression evidence is
relevant, but low heart transcript abundance does not disprove a cardiac role.
PMID8245032 has a linked erratum (PMID7989379); its body was not inspected, so
precise tissue quantities are not asserted. Generic-binding pairs 8/9 remain
unresolved because their exact supporting evidence has not been verified.
User-provided annotation actions require UNDECIDED in that situation. A generic
label alone does not establish that either experimental interaction is false.
The exosome row 40 likewise remains unresolved: membrane topology is compatible
with vesicle incorporation, and the target proteomics row is still unread.

Each review summary now states the evidence separately from the action reason.
No NEW annotation, replacement term or added core is proposed. The previously
recorded normal research-provider failure is retained; no repeat is claimed.

Source reading: original PMID11259493 complete Methods 427–797 and selected
Results 890–1277/1566–1940, Figure4 caption, selected Discussion 1942–2006/2226–2355;
PMID16855061 complete Methods 245–414, Results 421–480, Discussion and Conclusion,
but no figure pixels. PMID30535804 official complete abstract and selected indexed
original genetic Results were inspected; original complete Methods were not.
PMID8245032 identity/abstract was independently checked; the cardiac abundance
wording is attributed to the immutable UniProt record. No complete-paper claim
is inferred from an abstract-only normal cache.

Primary sources:
- https://www.researchgate.net/publication/247659906_Differentiation_induces_up-regulation_of_plasma_membrane_Ca2ATPase_and_concomitant_increase_in_Ca2_efflux_in_human_neuroblastoma_cell_line_IMR32_PMCA_up-regulation_during_differentiation
- https://www.researchgate.net/publication/6930862_Plasma_Membrane_Calcium_Pumps_in_Mouse_Olfactory_Sensory_Neurons
- https://pubmed.ncbi.nlm.nih.gov/30535804/
- https://pubmed.ncbi.nlm.nih.gov/8245032/

The normal records for PMID:16855061, PMID:30535804 and PMID:8245032 are now
available and match their recovered and staged bytes exactly. The first and
third are abstract-only; PMID:30535804 has an XML body. Complete normal headers
and abstracts were read at closure. The earlier external primary-source reading
scopes remain distinct from cache availability; the recovered XML body was not
reread in full, and the PMID:7989379 erratum remains uninspected.

This follow-up supersedes the initial review's cilium and neuronal-differentiation
uncertainty and its 27 ACCEPT / 9 non-core / 22 UNDECIDED tally. The current
decisions are 28 ACCEPT, 9 KEEP_AS_NON_CORE, 20 UNDECIDED and 1
MARK_AS_OVER_ANNOTATED across the same 58 source assertions and eight products.
Historical validation observations above describe the initial version; validation
of this follow-up will be recorded after application.

Follow-up validation: focused `just validate human ATP2B2` passed without
annotation advisories, and `just render human ATP2B2` succeeded. The scaffolded
session history records the two action changes and source-access limits. No new
repository-wide validation pass is claimed.


## Second PR feedback: calcineurin interaction (2026-09-29)

The complete normal and official PubMed abstract of PMID:17689535 positively
reports an endogenous human PMCA2-calcineurin association. That target-specific
evidence resolves the broad binding function independently of the unresolved
machine-supplied P01258 partner. Row 8 is therefore refined to protein phosphatase
binding (GO:0019903), rather than treating a metadata discrepancy as absence of
all biological support. This is a contextual interaction outside the single
calcium-export core. No signaling-process annotation is introduced.

P01258 remains CALCA/calcitonin in the unchanged source assertion. Neither a
calcineurin subunit accession nor a corrected database interaction is guessed.
The existing question about the exact P01258 mapping is retained. Full original
Methods and interaction-record details were not accessed; the abstract does not
justify describing this as a purified direct-binding measurement. The reference
is verified only for its official identity and explicit abstract-supported claim.
The normal cache remains abstract-only. This entry supersedes the earlier notes'
uncertainty about the entire function in row 8, while retaining their unresolved
partner-mapping qualification. The SCRIB row remains UNDECIDED.

The official AmiGO parent definition and hierarchy support GO:0019903. A more
specific child, GO:0030346 protein phosphatase 2B binding, is listed in that
hierarchy and the local ontology label cache, but its complete official definition
could not be retrieved during this bounded check. The present proposal uses the
verified parent without adding the child as a duplicate assertion.

All 58 machine source objects, eight alternative products, the single core and
existing questions are unchanged. The proposed counts are 28 ACCEPT, nine
KEEP_AS_NON_CORE, 19 UNDECIDED, one MARK_AS_OVER_ANNOTATED and one MODIFY.
One 13-word literal abstract anchor is added to the affected row; no duplicate
quotation is added to reference findings. This is a prospective proposal; its
focused validation/render/history will follow only after canonical application.

Sources checked:
- https://pubmed.ncbi.nlm.nih.gov/17689535/
- https://amigo.geneontology.org/amigo/term/GO:0019903
- https://www.uniprot.org/entry/P06881 (explicit cross-reference to P01258)
- https://www.ncbi.nlm.nih.gov/protein/1476413357

Focused validation after applying this follow-up passed (`just validate human ATP2B2`, actual e0146a); gene rendering passed (2b0526). The new EDIT history record `2026-09-29T200440Z-codex-582807.yaml` passed history validation (1f3081). The earlier validation 07adfd ran before the follow-up was applied and is not evidence for this revision. All source assertions and alternative products remain unchanged.
