# CD79A review notes

## Intake and preservation — 2026-10-09

Human CD79A (P11912) was absent from GitHub main at the initial check (main `d763bc99e4aee5c0df05fd45468e96c1da033ef9`); an open-PR search for CD79A returned no matches. The normal `fetch-gene human CD79A` command ran against an isolated copy of the current, unmodified repository code and produced a fresh UniProt record, GOA table and seed with 206 assertions, two alternative products and 23 references. The original normal outputs are preserved in the working archive.

For publications and Reactome, existing canonical bytes were selected where available. Freshly downloaded variants were preserved separately rather than replacing canonical caches. No source publication, GOA or UniProt content was edited. Normal family-data outputs remain in the intake archive and are not used to assert a new PANTHER family classification. Research and source selection were performed in an isolated working directory before publication.

The genuine Falcon attempt timed out after 90 seconds. The explicit perplexity-lite fallback then failed after repeated dependency-download attempts; no provider report was produced. Manual primary research continued. The normal publication-caching command reused all seven original PMID caches. Four additional references were obtained through the normal fetch command: PMIDs 10525050, 7643857, 8617796 and 10900006.

## Biological synthesis

CD79A is the Ig-alpha component of the CD79A/CD79B signaling heterodimer. The human IgM-BCR structure directly places this heterodimer alongside the membrane immunoglobulin heavy and light chains. The heterodimer contributes assembly and signal transmission; immunoglobulin provides antigen recognition. CD79A's cytoplasmic ITAM is phosphorylated by kinases and supplies docking sites for signaling proteins, rather than performing kinase chemistry itself. [PMID:35981043](https://pubmed.ncbi.nlm.nih.gov/35981043/), [Reactome:R-HSA-983700](https://reactome.org/content/detail/R-HSA-983700).

Human surface-expression experiments support the requirement for intact receptor assembly. The study includes tonsillar B cells and lymphoma cell lines; loss of CD79A or CD79B removes surface IgM, while consequences for fitness differ among models. Its surface-staining methods were accessible beyond the abstract. This should not become a universal claim that every CD79A-deficient cell dies immediately. [PMID:36426942](https://pubmed.ncbi.nlm.nih.gov/36426942/).

The human agammaglobulinemia study identifies a splice defect disrupting the membrane receptor subunit and a block at the pro-B to pre-B transition. It explicitly distinguishes this checkpoint from immunoglobulin gene rearrangement. Thus, the existing differentiation annotations fit CD79A's receptor role; no recombinase function is inferred. [PMID:10525050](https://pubmed.ncbi.nlm.nih.gov/10525050/).

Cytoplasmic-tail experiments support cooperative signaling by Ig-alpha/Ig-beta, but their assay context matters: PMID:8617796 uses PDGFR-tail chimeras in a murine B-cell line. The phosphorylation-regulation study supplies additional mechanistic background, without establishing every residue-specific event in endogenous human B cells. [PMID:8617796](https://pubmed.ncbi.nlm.nih.gov/8617796/), [PMID:10900006](https://pubmed.ncbi.nlm.nih.gov/10900006/).

These are one coherent core unit: a signaling and assembly subunit contributing to transmembrane receptor activity in the BCR complex. The source IBA and ISS receptor rows already use `contributes_to`. The IEA row has `enables`; that machine field is preserved, while its reason and the core synthesis explicitly state the complex-subunit interpretation. No separate autonomous antigen-receptor or enzymatic activity is assigned.

## Alternative products

Both source products are preserved: P11912-1 (long) and P11912-2 (short). The UniProt source maps the short product to an extracellular sequence alteration, and the original splice study detects variant transcripts in human B cells. The accessible study does not establish that the short product is a stable functional receptor subunit. Retaining the two source records therefore does not imply equivalent surface assembly, signaling or physiological abundance. [PMID:7643857](https://pubmed.ncbi.nlm.nih.gov/7643857/).

No residue-specific function was inferred for the short product merely from retention of the cytoplasmic tail. The proposed experiment first establishes protein expression and then compares assembly and signaling in a controlled human B-cell setting.

## Existing annotations

All 206 source assertions retain their original term, qualifier, evidence, reference and partner/product fields. Decisions are 33 ACCEPT, 172 KEEP_AS_NON_CORE and one MODIFY. There are no NEW, REMOVE, UNDECIDED or PENDING decisions. The single MODIFY refines the general cell-surface signaling pathway to B-cell receptor signaling. No new process is proposed.

Plasma-membrane and receptor-complex assignments are supported by human structure and surface-expression evidence. The external-side IBA uses `is_active_in`: extracellular CD79A contacts membrane immunoglobulin and contributes to receptor assembly there, while ITAM signaling occurs on the cytoplasmic side. This structural contribution does not assign autonomous antigen binding to CD79A. The broad membrane term and conditional raft/endocytic locations are retained as non-core. The multivesicular-body and raft annotations preserve their orthology provenance; this review does not claim newly inspected human imaging experiments for those transfers. Signal transmission is not restricted to rafts.

The isolated Ig-alpha cytoplasmic domain can oligomerize in vitro according to the original abstract. The identical-protein-binding annotation is therefore retained as non-core; this does not replace the physiological CD79A/CD79B heterodimer with a CD79A homodimer. The title foregrounding T-cell receptor zeta is not a reason to reject explicitly reported Ig-alpha assays. [PMID:14967045](https://pubmed.ncbi.nlm.nih.gov/14967045/).

The Fc-mu-receptor structural paper discusses IgM-BCR context, but its abstract does not enumerate every BCR subunit. The exact CD79A inclusion in that paper was not independently inspected. The IgM-complex annotation remains accepted because it is directly established by the independent human BCR structure; no misattribution claim is made from the Fc-mu-receptor-focused title. [PMID:36949194](https://pubmed.ncbi.nlm.nih.gov/36949194/), [PMID:35981043](https://pubmed.ncbi.nlm.nih.gov/35981043/).

PAINT assertions are evaluated against inherited receptor biology, not donor counts. CD79A's presence among descendant evidence for the BCR complex is legitimate and is not treated as circular. The ancestral node placement and complete electronic/orthology chains were not independently rebuilt.

## Independent screen-binding consultation

A separate reviewer checked all 166 source screen assertions against exact source-specific target records. The evidence and limitations are summarized below. The public [IntAct target query](https://www.ebi.ac.uk/Tools/webservices/psicquic/intact/webservices/current/search/query/id:P11912?format=tab27) and [author U2OS network](https://www.ndexbio.org/viewer/networks/95bc75d5-d1d1-11ee-8a40-005056ae23aa) identify the underlying records.

- All 164 HuRI rows join to precise publication-linked IntAct target records. Seventeen partner accessions include isoform suffixes, and those suffixes were matched without stripping them. The 498 matching pooling, array and validated Y2H records represent related assays within the study, not 498 independent physiological replications. Original construct sequences and every raw supplementary control were not reanalysed. [PMID:32296183](https://pubmed.ncbi.nlm.nih.gov/32296183/).
- The 2014 Q969F0/FATE1 row joins to exact CD79A pair records from pooling, array and validated Y2H assays. Partner identity is independently consistent with UniProt. This does not establish a FATE1-associated anti-apoptotic or organelle-contact role for CD79A. [PMID:25416956](https://pubmed.ncbi.nlm.nih.gov/25416956/).
- The 2025 Q92843/BCL2L2 row is present in the author-deposited U2OS AP-MS network as edge 578338. The portal identifies the queried network, and the accession-to-gene mapping was checked independently. This is a gene-level association in the assay context, not necessarily a direct interface or a native B-cell mechanism. The absence of that recent pair from the current IntAct response is not contrary evidence. [PMID:40205054](https://pubmed.ncbi.nlm.nih.gov/40205054/), [author data portal](https://musicmaps.ai/u2os-cellmap-data/).

All these interactions remain KEEP_AS_NON_CORE under the project's explicit instruction to retain supported correct generic binding when a more informative activity is not established. No screened partner's biochemical function is transferred to CD79A. The 166 resulting generic-binding warnings are understood and intentional. Partner isoform identifiers describe the curated/tested product and do not, by themselves, establish isoform-exclusive binding.

## Source access and limitations

All eleven publication abstracts were read. The human disease paper's accessible PMC HTML includes the methods, patient/mutation results, differentiation data and discussion inspected here. The structural and splice papers, domain-oligomerization paper and tail-function papers remain abstract-only for this review. For PMID:36426942, selected accessible main text through the methods supplemented its immutable abstract-only cache; a subsequent web retrieval returned a browser challenge, and an independent Europe PMC XML request returned HTTP 500. No complete main-text or figure-pixel read is claimed.

The screen reports were assessed through their accessible abstracts, relevant method context and the independent exact-target consultation. Cached HTML being flagged available does not establish that a complete original paper or every supplementary table was inspected. Reference assessments distinguish positive identity/record checks from such limitations. No unavailable source was silently replaced by a generated provider narrative.

All ten existing Reactome summaries were read. They locate the BCR-associated assembly and assign catalysis to the appropriate named kinases, phosphatase or phospholipase. No drug-target, therapeutic or catalytic activity is inherited by CD79A merely from participation in those cached events. No new process is inferred from the absence of CD79A/P11912 in the cached GO-CAM index search.

## Verification

Normal schema/reference/GO-term validation, status checking and rendering use unmodified repository code and authentic source caches in the isolated workspace. The 166 warnings concern the supported generic-binding rows retained by explicit policy. DRAFT is the normal derived status in the presence of these warnings; it does not mean any source assertion remains PENDING.

Structural comparison confirms preservation of all 206 original assertions outside their review blocks and both alternative products. Two short verbatim anchors appear once each in the YAML; these notes include no source quotations. The audit verifies exact cache substrings and aggregate per-source word counts including repetitions. Independent review checked the annotation decisions, exact interaction evidence and selected primary disease and structural results before publication. Source caches remain unchanged; curation history accompanies the review.
