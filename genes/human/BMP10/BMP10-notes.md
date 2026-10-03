# BMP10 provisional scientific review — 2026-10-01

This TMP v5 candidate preserves all 119 seeded assertions and contains 24 ACCEPT, 86 KEEP_AS_NON_CORE, 2 MODIFY and 7 UNDECIDED decisions. There are no NEW or REMOVE annotations. Sources103 and104 have been integrated from authenticated normal outputs; canonical application, final peer, validation, history and rendering remain outstanding.

## Core activity

The single core function is extracellular growth-factor activity (GO:0008083), initiating BMP signaling (GO:0030509), in the extracellular region (GO:0005576). BMP10 supplies the ligand; receptor kinases perform phosphorylation. The original assertions already contain these terms. The two binding refinements use seeded receptor serine/threonine kinase binding and telethonin binding. Processing of the precursor does not create a splice isoform. No alternative-product or protein-product object is introduced.

## Resolved existing evidence

The 54 HuRI IPI assertions are retained as non-core. Each existing GOA partner was matched to UniProt, and the primary HuRI screening methods were read. These curated records can share provenance; they are not two independent experiments. Individual constructs, supplementary records and orthogonal validation were not independently audited. Neither a physiological interaction nor a signaling role is inferred. This treats existing experimental assertions with curator deference while recording their limits.

Selected [fibrillin study Table 3 and Discussion](https://pmc.ncbi.nlm.nih.gov/articles/PMC2376219/) support BMP10 prodomain binding to the FBN2 fragment rF86. Both fibrillin interactions remain non-core; the local cache is abstract-only.

The [PMID:17921333 author manuscript](https://www.researchgate.net/publication/5924396_Interaction_of_BMP10_with_Tcap_may_modulate_the_course_of_hypertensive_cardiac_hypertrophy) supports cytoplasmic staining and conditioned-medium sarcomeric maturation. Selected text and captions were read; no image audit is claimed. Four previously unresolved rows are retained as non-core with experimental limits. The contraction claim remains unresolved.

The [PMID:17068149 publisher caption](https://ashpublications.org/blood/article/109/5/1953/23209/Identification-of-BMP9-and-BMP10-as-functional) describes WST-1 viable-cell abundance. [GO cell growth](https://amigo.geneontology.org/amigo/term/GO:0016049?relation=isa_partof) concerns enlargement of an individual cell. The negative-cell-growth assertion is therefore UNDECIDED; no proliferation replacement is manufactured from WST-1 alone.

## Remaining uncertainties

Seven rows remain UNDECIDED: two adult-heart and two atrial-development transfers, one contraction assertion, one cartilage-development transfer and the cell-growth assertion above. Fourteen existing transfers now have independent functional corroboration; the exact original donor-reference edges are still unverified. Expression alone does not establish a developmental function, and opposing hypertrophic responses in different experimental contexts need not conflict.

The existing activin receptor pathway and hormone assertions were checked against official GO definitions. They do not require an activin-named ligand, SMAD2/3 or a specified circulation route. BMP10 is neither a receptor kinase nor a DNA-binding transcription factor. ClinGen Limited disease associations remain Limited.

## Reading and provenance

All 119 source objects and decisions were assessed by the independent reviewer. Six normal Seed58 publication abstracts, both Reactome records, selected HuRI methods, selected primary external passages and official GO definitions were used. Normal publication cache bytes were not edited or replaced with manually authored full text. The repository cache availability flags remain accurate. No provider-labelled research output was authored.

Independent findings: `tmp/BMP10-provisional-peer/independent-findings-v2.json`; v3 applies those bounded existing-source findings. The final candidate must incorporate available source recovery outcomes, preserve all machine-sourced fields, and pass a distinct final scientific peer before canonical publication.

## Additional mechanism evidence

[PMID:35504921](https://pubmed.ncbi.nlm.nih.gov/35504921/) resolves binary BMP10–BMPRII and ternary ALK1–BMP10–BMPRII structures. The selected Results support the existing receptor-binding and growth-factor interpretation; BMP10 is the ligand, and the receptors are kinases. The paper’s BMPR2 genetics do not establish a BMP10 disease association.

[PMID:21737454](https://pubmed.ncbi.nlm.nih.gov/21737454/) measures BMP10 binding to human and mouse endoglin extracellular domains and inhibition of BMP10 Smad-reporter responses by soluble endoglin constructs. Its receptor-competition mapping used BMP9. These experiments provide receptor-context evidence without a new annotation or a transfer of BMP9-specific measurements to BMP10.

[PMID:39921464](https://pubmed.ncbi.nlm.nih.gov/39921464/) sections3.1–3.2 compare processed and unprocessed recombinant BMP10 and section3.8 examines fibrillin-1 targeting. Processed BMP10 activates SMAD responses; only the processed complex bound the tested fibrillin fragment. Convertases perform the cleavage, so this study supplies no BMP10 proteolysis activity/process annotation. Modeled conformational masking is kept distinct from the directly measured binding and signaling results.

[PMID:38322548](https://pubmed.ncbi.nlm.nih.gov/38322548/) reports a Glu83* variant in one family and loss of reporter activation in HeLa cells. Its normal cache is abstract-only. Reporter activation does not make BMP10 a DNA-binding transcription factor. The source ClinGen Limited classifications remain unchanged.

Only abstracts and the explicitly named Results/caption excerpts were read; no complete-paper, image or supplementary audit is claimed. Source103 normal bytes were verified against the staged artifact before use; their canonical import is a separate step. Four references and supporting explanations were added, with no action changes or NEW annotations. The ordinary falcon/perplexity-lite research command failed before provider execution because the required offline dependency was unavailable; no provider-labelled research file was created.

## Developmental evidence integrated on 2026-10-01

[PMID:15073151](https://pubmed.ncbi.nlm.nih.gov/15073151/) supplies mouse knockout, histological and rescue evidence. Selected Figures 3-4 and Results distinguish impaired ventricular/trabecular growth from preserved primitive trabecular initiation. Figure 7 and Results connect BMP10 exposure to cardiomyocyte proliferation. This resolves existing developmental signaling assertions without making BMP10 part of the division machinery.

[PMID:16798733](https://pubmed.ncbi.nlm.nih.gov/16798733/) examines myocardial BMP10 overexpression after birth. Cardiomyocyte enlargement is reduced, but exercise and beta-adrenergic hypertrophic responses remain intact. These context-dependent results need not contradict the positive hypertrophic responses reported in PMID:17921333.

Both newly retrieved caches contain abstracts only. Selected primary indexed Results and caption text supplied additional context; images, supplements and entire papers were not audited. No manually reconstructed publication cache, new annotation, clinical reclassification or substitute donor provenance is introduced. The single extracellular growth-factor core remains unchanged. Fourteen decisions move from UNDECIDED to KEEP_AS_NON_CORE; seven remain unresolved.


## Canonical review completed — 2026-10-01

This entry supersedes the provisional status above. The distinct final scientific review, focused schema/term/reference/GOA validation, new history record and HTML rendering passed. All 56 validation advisories concern retained generic physical interactions under the requested project policy. The rendered YAML equals the canonical review. All 119 distinct source assertions, fetched UniProt/GOA and 15 publication/Reactome source files remain preserved; seven decisions retain their explicit evidence limits. No alternative-product or protein-product object was introduced. Remote publication and approval remain separate steps.

## Research reassessment after the first PR review — 2026-10-01

This entry supersedes the earlier HuRI retention rationale and action counts. The single core remains BMP10's extracellular growth-factor activity. The revised decisions are 24 ACCEPT, 28 KEEP_AS_NON_CORE, 6 MODIFY and 61 UNDECIDED across the same 119 source assertions. No assertion or partner is deleted, and no new annotation is proposed. The four existing supporting quotations are unchanged; the evidence discussion below uses paraphrases.

### Binding specificity and the HuRI evidence boundary

The fibrillin experiments support a specific refinement. The BMP10 prodomain binds the N-terminal region of fibrillin-1 and the fibrillin-2 fragment rF86 in recombinant binding experiments ([PMID:18339631, Table 3 and Discussion](https://pmc.ncbi.nlm.nih.gov/articles/PMC2376219/)). [GO:0050840 extracellular matrix binding](https://amigo.geneontology.org/amigo/term/GO:0050840) describes binding to these matrix components. Both generic binding assertions become MODIFY. This does not assert binding to an assembled microfibril or add another core signaling function. Processing matters: the processed BMP10 complex, but not the unprocessed precursor, bound the tested fibrillin-1 fragment in the later study ([PMID:39921464, section 3.8](https://pubmed.ncbi.nlm.nih.gov/39921464/)). Its structural modeling is distinct from measured binding and does not establish a universal in-vivo latent state.

The 54 HuRI assertions become UNDECIDED because the particular constructs and validation records have not been independently adjudicated. The existing partner accessions remain intact, and all 54 names were matched to the fetched BMP10 UniProt interaction list. The GOA and UniProt records can share the same experimental provenance. HuRI's binary screening, retesting and sequence-confirmation methods support taking those records seriously; dataset-level orthogonal validation does not demonstrate that every BMP10 pair received that validation ([PMID:32296183](https://pubmed.ncbi.nlm.nih.gov/32296183/)). The methods and discussion also identify limitations of expressing proteins in yeast, including processing and isoform coverage, and caution against rejecting all pairs without known colocalization. Neither generic wording nor an assumed compartment mismatch establishes a false interaction.

The topology concern is heterogeneous. The fetched [COQ9 record](https://www.uniprot.org/uniprotkb/O75208/entry) annotates mitochondrial localization, which is a substantial concern for physiological contact with secreted BMP10. In contrast, [KIR2DL3 P43628](https://www.uniprot.org/uniprotkb/P43628/entry) has an annotated extracellular domain: membrane localization alone cannot exclude access by an extracellular ligand. For FFAR2 and KLRC1, the receptor label does not identify the assayed binding surface. For BSCL2 and MGST3, the relevant question is the actual membrane face and BMP10 species, rather than merely whether an ER/microsomal label appears. MRPS18B and MTIF3 warrant scrutiny of the mitochondrial-compartment concern, without claiming their particular HuRI results have been experimentally disproved. The source names TMPRSS2 **O15393-2** and SLC35C2 **Q9NQQ7-3** specifically; canonical sequences cannot silently replace these isoforms.

Only the COQ9 cached localization and the indexed KIR2DL3 topology were independently established in this focused topology check. A current bulk UniProt retrieval failed, and several entry pages exposed only access-fallback text; these limitations were not converted into invented topology assignments. The remaining partner names come from the unchanged BMP10 record, not an independent functional audit of 54 proteins. For every pair, the unresolved link is between the exact assay construct, BMP10's precursor/prodomain/processed growth-factor forms, and any verified interaction in an appropriate cellular context. The change to UNDECIDED reflects that evidence gap and does not assert that all HuRI interactions are artifacts. It does not depend on a generic-binding exception adopted for a different gene.

### Receptor signaling and endothelial endpoints

BMP10-specific ActRIIA support comes from the shRNA experiment in MC3T3 cells in [PMID:16049014](https://pubmed.ncbi.nlm.nih.gov/16049014/). The second GO:0032924 assertion therefore remains ACCEPT with this additional reference. [PMID:17068149](https://ashpublications.org/blood/article/109/5/1953/23209/Identification-of-BMP9-and-BMP10-as-functional) establishes BMP10 activation of ALK1, but its BMPRII/ActRIIA depletion experiment concerns BMP9. ALK1's historical name and a discussion hypothesis cannot substitute for the BMP10 experiment. The original annotation's reference field is preserved.

The same paper's BMP10 experiments measure distinct endpoints. Figure 6D follows endothelial wound closure in low serum, supporting the authors' migration interpretation, although closure can also depend on cell abundance. The generic migration assertion is refined to the already represented endothelial-specific GO:0010596. Figure 6E uses WST-1 after 24 and 48 hours, reported as viable-cell abundance. The authors describe growth inhibition; that observation is preserved. It does not directly measure enlargement of an individual cell or distinguish division from survival and metabolic changes. GO:0030308 remains UNDECIDED rather than being assigned [GO:0001937 negative regulation of endothelial cell proliferation](https://amigo.geneontology.org/amigo/term/GO:0001937) on this endpoint alone. This is uncertainty about the appropriate biological interpretation, not an assertion that the inspected caption was inaccessible or that BMP10 cannot affect proliferation.

### Cardiac responses and developmental mechanism

The near-root GO:0051240 assertion is refined to the existing GO:0010613 positive regulation of cardiac muscle hypertrophy. This follows the conditioned-medium response in neonatal rat cardiomyocytes reported in [PMID:17921333](https://pubmed.ncbi.nlm.nih.gov/17921333/). It does not establish the ARBA rule's original training provenance or a universal response to BMP10: postnatal myocardial overexpression produced reduced cardiomyocyte enlargement in [PMID:16798733](https://pubmed.ncbi.nlm.nih.gov/16798733/). The earlier author-manuscript reading remains limited to selected text and captions; no publisher full-text retrieval or image audit is newly claimed.

In embryonic mouse myocardium, loss of BMP10 is associated with ectopic/elevated CDKN1C/p57KIP2 and impaired maintenance of NKX2-5 and MEF2C expression, alongside reduced cardiomyocyte proliferation; conditioned medium rescues deficient hearts ([PMID:15073151](https://pubmed.ncbi.nlm.nih.gov/15073151/)). These observations give the existing developmental-process reasons a mechanistic context. They do not make BMP10 a DNA-binding transcription factor or establish that one expression change alone explains the entire phenotype. The PMID:16049014 transcription row retains its original reporter evidence; the PMID:17068149 row already describes endogenous endothelial gene expression. The developmental paper adds corroboration without rewriting either original experiment or resolving the exact donor-reference edges.

Four suggested questions now make the remaining gaps explicit: HuRI constructs and validation; endothelial division versus viability/metabolism; direct contraction measurements; and the specific donor experiments behind adult-heart, atrial and cartilage transfers. The review remains DRAFT. Primary reading is limited to the cached abstracts/full text and the specifically named external Results/caption passages. Publication availability flags and all source-cache bytes remain unchanged.


## Follow-up verification

Independent scientific review approved this follow-up and its explicit reading limits. Focused schema, ontology-term, reference, GOA and best-practice validation passed on the exact candidate YAML now applied, with no repository advisories; it was not rerun on identical bytes. History validation passed, and the rendered page reproduces the review YAML. All 119 source assertions and four supporting quotations are preserved. The review contains 24 ACCEPT, 28 KEEP_AS_NON_CORE, 6 MODIFY and 61 UNDECIDED decisions, one unchanged core and no new assertion. All source caches and previous history are unchanged.
