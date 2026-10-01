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
