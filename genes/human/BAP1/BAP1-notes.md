# BAP1 review notes

## 2026-09-30 — scope and decisions

Human BAP1 is UniProt Q92560, HGNC:950. The review preserves all 96 source annotation objects, including evidence, references, supporting entities and the source term label on the parkin-localization row. Decisions comprise 44 ACCEPT, 47 KEEP_AS_NON_CORE, four MODIFY and one UNDECIDED. No NEW annotation is proposed. Two core functions distinguish histone from nonhistone deubiquitination.

The generic protein-binding assertions are retained as non-core when the partner relationship is supported. Co-purification is not described as proof of an isolated binary interaction. The BAP1–BRAF assertion from PMID:35512704 remains undecided because its exact construct, variant and pair-level assay were not resolved. This is an evidence-access limit, not a claim that the curator assigned the wrong gene. The P38398-5 supporting entity on the original BRCA1 interaction is a partner isoform, not a BAP1 isoform.

The four refinements specify cysteine-type deubiquitinase activity instead of generic peptidase activity, transcriptional regulation instead of two broad expression terms, and protein deubiquitination instead of protein modification. The InterPro-derived ubiquitin-dependent protein-catabolism assertion is retained as non-core. UCH-family membership alone does not establish target-protein breakdown, but HCFC1 accumulation after BAP1 depletion supports a contextual turnover role. The authors' proposed connection to proteasomal degradation remains tentative. One supported context can justify a process annotation; BAP1 need not execute degradation generally. This evidence-based retention supersedes the preliminary over-annotation proposal.

## Catalysis, chromatin and transcription

The original PR-DUB study directly reconstituted both human BAP1–ASXL1 and fly Calypso–Asx. Its human enzyme removes nucleosomal H2A ubiquitin, while the Hox-repression genetics are fly experiments. A paper centered on a fly complex therefore provides valid human catalytic evidence. [PMID:20436459](https://pubmed.ncbi.nlm.nih.gov/20436459/)

Purified human BAP1 is stimulated by ASXL DEUBAD domains. Nucleosomal H2AK119 ubiquitin is distinguished from H2AK13/15 ubiquitin; isolated peptide assays do not preserve all nucleosome specificity. Earlier recruitment and oligomerization measurements should not be generalized beyond their constructs and conditions. [PMID:26739236](https://pubmed.ncbi.nlm.nih.gov/26739236/)

The later human BAP1–ASXL1 substrate-bound structure resolves DNA, histone and ubiquitin contacts. The structural substrate contains Xenopus histones, while the enzyme is human; separate biochemical assays test cleavable substrates. The resolved 1:1 assembly is not imposed as the universal stoichiometry of every native complex. The earlier bidentate study contains a fly structure and direct human biochemical assays, with the human oligomer modeled rather than structurally resolved. [PMID:37556531](https://pubmed.ncbi.nlm.nih.gov/37556531/), [PMID:30258054](https://pubmed.ncbi.nlm.nih.gov/30258054/)

BAP1-mediated H2A deubiquitination has context-dependent transcriptional outcomes. Human HAP1 knockout and catalytic rescue support protection of active genes from PRC1-dependent silencing. Tagged interaction profiling in that study used HeLa cells; the HAP1 genetic and chromatography experiments are distinct. FOXK2-target studies separately support repression and phosphorylation-dependent recruitment. These observations motivate a direction-neutral transcription-regulation core. [PMID:30664650](https://pubmed.ncbi.nlm.nih.gov/30664650/), [PMID:25451922](https://pubmed.ncbi.nlm.nih.gov/25451922/), [PMID:24748658](https://pubmed.ncbi.nlm.nih.gov/24748658/)

Local PAINT data contain positive ancestral assertions for BAP1-family catalytic activity and heterochromatin formation. The latter is retained as non-core; the complete family topology/MSA was not reconstructed. Calypso grounding and a short donor list are not reasons to reject an IBA. Human BAP1 appearing among experimental descendants is valid grounding, not circular evidence.

## Nonhistone substrates and localization

HCFC1 is an established BAP1 partner and substrate. The HCF-binding motif and HCFC1-N/Kelch experiments must be distinguished from assays of HCFC1-C in another study. WT versus C91A and linkage-restricted ubiquitin support K48-linked substrate deubiquitination in human cells; they do not establish unrestricted cleavage of every free K48 chain. Substrate stabilization is not a universal consequence. [PMID:19815555](https://pubmed.ncbi.nlm.nih.gov/19815555/), [PMID:19188440](https://pubmed.ncbi.nlm.nih.gov/19188440/)

An ER-associated BAP1 pool binds and deubiquitinates ITPR3, supporting receptor abundance and calcium-dependent cell-death responses. The original work includes primary human fibroblasts/mesothelial cells and transfected HEK293 assays. Its biochemical reaction uses immunopurified proteins; minimal isolated binary sufficiency is not claimed. BAP1 is neither the calcium channel nor an integral ER membrane protein. The nonhistone core's nuclear location concerns HCFC1, while its ER-membrane location concerns ITPR3. [PMID:28614305](https://pubmed.ncbi.nlm.nih.gov/28614305/)

Wild-type BAP1 is principally nuclear with a regulated cytoplasmic pool. Localization-signal mutants, UBE2O-dependent monoubiquitination, BAP1 autodeubiquitination and TNPO1-dependent import help distinguish catalytic competence from substrate access. BAP1 is import cargo, not the transport receptor. [PMID:18757409](https://pubmed.ncbi.nlm.nih.gov/18757409/), [PMID:24703950](https://pubmed.ncbi.nlm.nih.gov/24703950/), [PMID:35446349](https://pubmed.ncbi.nlm.nih.gov/35446349/)

BRCA1/BARD1 interaction and inhibition of its ligase activity are distinct from deubiquitination of either component. The newer Reactome disruption event explicitly records catalytic-independent inhibition; the broader chain-removal statement in the older event is not used to invent a substrate assignment. All eight source Reactome summaries were read; their nucleoplasmic source annotations agree with direct localization evidence. [PMID:19117993](https://pubmed.ncbi.nlm.nih.gov/19117993/), [Reactome R-HSA-9700998](https://reactome.org/content/detail/R-HSA-9700998)

## Physiological outcomes and read limits

Mouse Bap1 loss supports embryonic and hematopoietic phenotypes. Orthology-derived lineage, proliferation and homeostasis annotations remain contextual, rather than separate human catalytic functions. The correct identity is PMID:22878500, DOI **10.1126/science.1221711**, PMCID PMC5201002; an earlier scratch fetch receipt mistyped the DOI suffix. Official PubMed and PMC agree on the corrected identity. The indexed abstract and Figures 1–4 captions were read. [PMID:22878500](https://pubmed.ncbi.nlm.nih.gov/22878500/)

The parkin-recruitment screen includes BAP1 among reconfirmed candidates in publisher Extended Data Figure 5. This supports the retained recruitment phenotype without making BAP1 a mitochondrial import factor. The source GO identifier and obsolete-labeled term were preserved; no replacement was guessed. Germline neurodevelopmental evidence likewise does not directly establish every developmental GO process transferred from mouse. [PMID:24270810](https://pubmed.ncbi.nlm.nih.gov/24270810/), [PMID:35051358](https://pubmed.ncbi.nlm.nih.gov/35051358/)

Several caches are abstract-only. Existing PMID:33961781 and PMID:35512704 caches contain incomplete article sections despite their full-text flags; neither flag was equated with a complete-paper read. Pair-level supplementary interaction tables were not independently inspected. Reference reviews in the YAML record source-specific boundaries. Primary Results/Methods and figure captions were read selectively where needed; no raw sequencing, microscopy images, cryo-EM maps or entire supplement reanalysis is claimed.

The normal source-fetch attempt failed before writing gene files. Verified recovery supplied the original machine-generated sources. The default Falcon research attempt and configured perplexity-lite fallback could not start because the required offline dependency was unavailable; neither produced a research report. This document records manual research, and no provider-labeled report was manufactured. An independent annotation reviewer assessed 30 rows and checked the remaining 66 plus the two-core plan. Source files and existing publication caches were preserved.

## First review follow-up: functional specificity and source scope — 2026-09-30

The BRCA1–BARD1 interaction experiments support ubiquitin ligase inhibitor
activity (GO:1990948). PMID:19117993 reports inhibition of ligase-dependent
ubiquitination even with catalytic-mutant BAP1. Its indexed publisher Methods
and Discussion were read separately from the normal abstract-only cache; the
complete paper, figures and supplements were not inspected. Three generic
binding rows with canonical BRCA1 or BARD1 are refined using that evidence,
including the older PMID:9528852 BRCA1 interaction with the later paper as an
additional reference. The BRCA1-5 partner row remains non-core because the
particular partner isoform was not established in those inhibition assays.
Other supported generic interactions retain their non-core classifications.

The nonhistone catalytic core now uses endoplasmic reticulum (GO:0005783).
PMID:28614305 reports fractionation, immunofluorescence and immunogold evidence
for an ER-associated pool, and an artificially ER-targeted BAP1 construct.
Those selected Results and Methods support the organelle assignment; they do
not require assigning endogenous BAP1 to the ER lipid bilayer. Lack of integral
membrane topology alone would not exclude peripheral membrane association.

The HCFC1 details in the protein-turnover and K48-deubiquitination reasons were
checked against original indexed Results, Figure 5 caption and Discussion in
[PMID:19188440](https://pmc.ncbi.nlm.nih.gov/articles/PMC2663315/), with relevant
Methods also inspected. The K48-restricted ubiquitin/WT-versus-C91A experiment
and precursor/processed-HCFC1 accumulation are present in those passages.
Proteasomal turnover remains the authors' interpretation, not a universal
mechanism demonstrated for all BAP1 substrates. The normal cache remains
abstract-only; article images and supplements were not read.

The gene-expression replacement is a reassignment to a regulatory process,
not a purported is_a refinement. The original source IDs are unchanged.

The official GO mature-cell differentiation pattern maps GO:0043363 to
CL:0000562, nucleate erythrocyte. This is a resulting mature cell identity, not
merely a nucleated intermediate. The adult-mouse hematology Results and
relevant Methods in the normal full-text cache of PMID:22878500 describe
anemia and erythroid dysplasia, including increased nucleated erythroid cells.
That evidence supports generalizing the electronic annotation to erythrocyte
differentiation (GO:0030218). It does not establish production of the mature
nucleate cell type or a direct human differentiation mechanism. The primary
identity is DOI 10.1126/science.1221711, PMCID PMC5201002. The complete paper
and supplements were not re-read for this bounded follow-up.

The parkin-recruitment phenotype remains non-core; the source's obsolete-
labelled GO:1903749 identifier and label are preserved. No new process or
molecular-function assertion is added. The proposal preserves all 96 source
objects and all 39 references, with 44 ACCEPT, 43 non-core, eight MODIFY and
one UNDECIDED; the two catalytic cores remain distinct.

## Second review follow-up: retained interaction context — 2026-09-30

The 15 remaining generic protein-binding annotations are deliberately retained
as KEEP_AS_NON_CORE under the user-supplied ActionEnum. That instruction
reserves REMOVE for an annotation unlikely to be correct on the combined
evidence; it permits KEEP_AS_NON_CORE for a supported annotation that does not
represent a core function. This takes precedence over the general review
recommendation to remove uninformative protein-binding terms. These rows
retain evidence-supported interaction context, not an additional core
molecular function or a claim of isolated binary binding from every assay.

A supported, more specific replacement has not been established for each
remaining exact assay, partner and partner-isoform assertion. Assigning an
adaptor or inhibitor activity solely from a physical association would add a
functional claim the experiment does not establish. In contrast, three
canonical BRCA1/BARD1 binding rows were already changed to MODIFY because
independent inhibition experiments support GO:1990948. The BRCA1-5 partner
row retains its explicit isoform-assay limit. The unresolved BRAF assertion
remains UNDECIDED and is separate from these 15 retained interactions. The
remaining generic-binding advisories are therefore acknowledged consequences
of this deliberate instruction precedence, rather than unreviewed rows.

The earlier notes sentence assigning the nonhistone core an ER-membrane
location is superseded by the first follow-up and this clarification. The
current core uses endoplasmic reticulum (GO:0005783), reflecting the
ER-associated BAP1 pool without requiring localization to the lipid bilayer.
This notes-only clarification changes no annotation, core function, reference,
source object or prior history record.
