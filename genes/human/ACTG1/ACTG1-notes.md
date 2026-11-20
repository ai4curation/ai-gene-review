# ACTG1 curation notes

## 2026-11-20 — scope and evidence

ACTG1 (HGNC:144; UniProt P63261) encodes cytoplasmic gamma-actin. The native acquisition seeded 136 annotation contexts. The review preserves their source identity, partners, evidence codes and qualifiers. The [source guide](ACTG1-source-guide.md) records primary-paper access, assay context and source locators.

The biological synthesis distinguishes a polymerizing structural actin subunit and its intrinsic ATP chemistry from myosin-driven movement. Epithelial junction organization, endothelial migration and stereocilia maintenance describe contexts in which the structural protein acts. They do not establish a dedicated transcription factor, kinase, membrane transporter or motor function [PMID:20308063; PMID:20976199; PMID:22855531; PMID:25705373].

Gene depletion and protein-sequence replacement answer different questions. Mouse Actg1 deletion leads to stereocilia maintenance defects, whereas a 2025 endogenous-locus replacement that produces beta-actin preserved the tested auditory outcomes through 16 weeks. The replacement result limits gamma-sequence-specific indispensability; it does not erase gamma-actin’s normal structural participation or the older deletion phenotypes. Human depletion experiments and mouse replacement experiments retain their distinct species, culture and age limits [PMID:19497859; PMID:20976199; PMID:40109120].

PMID:28493397’s absolute abstract wording about P70L failure to incorporate into F-actin is not adopted: Figure 2D reports comparable mutant and wild-type levels in the F-actin phase despite reduced mutant G-actin, while imaging shows an incorporation defect. Association assays support the named actin-binding partners without proving purified binary affinity.

Falcon deep research failed authentication; the Perplexity-lite fallback reported insufficient quota. Primary-source research continued manually. No authored text has been presented as a provider-generated research file.

Supported generic protein binding follows the standing ClinGen instruction: retain it as non-core when a specific molecular activity has not been demonstrated. When no independent evidence settles the interaction claim, unavailable or unadjudicated pair-level evidence remains uncertain. Interaction-screen provenance does not turn every candidate into an endogenous physiological interaction.

Native acquisition refreshed shared caches. Existing canonical cache versions were restored to preserve prior quotations and retained full text. Expanded PMID:25416956 and PMID:25910212 are retained; their source-impact audit found no newly broken inherited quotations. The fetched PMID:29892012 version broke one existing ICA1 quotation, so its prior cache was restored exactly and the fetched evidence retained through `refs/recovery/clingen-actg1-20261120/PMID-29892012-fetched-v1`. No ICA1 curation was changed. Compact acquisition, source-impact and restoration receipts preserve the reconciliation trail.

The registered sparse checkout and retained Python environment are reused with one writer. Read-only helpers examine disjoint annotation ranges; they do not create checkouts or modify the curated files. Tracker 764 was delivered and verified before this review began. ACTG1 receives no completion credit until its own validated PR has been delivered and verified.

## Initial adjudication

All 136 native contexts retain their original metadata and ordering: 65 ACCEPT, 46 KEEP_AS_NON_CORE, 18 UNDECIDED, 6 TOO_GENERAL and 1 MARK_AS_OVER_ANNOTATED. There are no NEW, REMOVE or MODIFY decisions. The wound-healing annotation overstates an in vitro gap-closure assay; migration remains represented. Two core functions summarize structural actin participation and intrinsic ATP hydrolysis. The source guide records exact interaction identifiers and access limits.

## Repository-review follow-up

Five source-limited binding rows now retain the independently supported interaction claim as non-core: ACTB (PMID:21516116), HTT (PMID:25959826), and CFL1/CAP2/CFL2 (PMID:35271311). Their original source assignments are still unverified. This reconciles duplicate claims without pretending to have inspected additional source tables. HTT evidence remains bounded to the N-terminal 1–504 construct and its polyglutamine-variant context [PMID:25416956; PMID:20308063; PMID:32814053; PMID:32296183].

Current decisions across the unchanged 136 native contexts: 65 ACCEPT, 51 KEEP_AS_NON_CORE, 13 UNDECIDED, 6 TOO_GENERAL and 1 MARK_AS_OVER_ANNOTATED. No NEW, REMOVE or MODIFY decisions. The 30 native-PMID IntAct matches and two directly supported Figure 2E pairs are unchanged; five additional retained claims reuse other verified evidence.

Core locations are representative settings for the same conserved structural actin activity, not an exhaustive copy of all accepted location rows. Axon, apical part of cell and synapse make these settings explicit. The calyx of Held is a presynaptic part of a synapse, and the Schaffer collateral–CA1 synapse is a synapse subtype, so these narrower terms remain represented without repeating them in the core location list. Axonogenesis is a developmental process, myofibril evidence concerns a distinct developmental muscle context, and NuA4 is a chromatin-complex context; their non-core treatment does not require demoting ordinary structural actin locations.

No NEW ATP-binding annotation is proposed. GO:0005524 is not an ancestor or descendant of GO:0016887, but ATP binding here is already the substrate-binding step of the retained ATP-hydrolysis activity. GO manual-annotation guidance explicitly uses these two terms as an example of unnecessary substrate-binding co-annotation. A separate binding row would add no independently established ACTG1 activity; this is a curation-convention decision, not an ontology-parent redundancy claim or a denial that actin binds ATP. See [the GO manual-annotation best-practices article](https://pmc.ncbi.nlm.nih.gov/articles/PMC3706743/), Molecular Function conventions.

The phosphate-release experiment supports ATP turnover but does not isolate the hydrolysis chemical-step rate from phosphate-release kinetics. UniProt's curated CC CATALYTIC ACTIVITY explicitly states the reaction as a database assertion with ECO:0000250 from pig ACTA1 P68137. This shares the native ISS donor provenance, so it is complementary explicit curation support, not a new independent human biochemical experiment. Neither DR GO lines nor keywords are used as functional evidence.

The [GO_REF:0000024 method](https://geneontology.org/GO_REF/0000024.html) permits case-by-case paralog transfers. A beta-actin donor alone is not a source defect. Broad plasma-membrane association has independent human ACTG1 support; dense-body localization is a narrower, unresolved compartment transfer. Inaccessible tables likewise do not establish an erroneous record. No source defect or upstream report is manufactured from either access limits or donor identity.

The remaining vesicle/cargo decisions retain study-specific access limits. Their common protein-class plausibility does not resolve ACTG1-specific identifications. The disease summary is grounded in the native UniProt CC DISEASE comments, without inferring a universal mechanism for all pathogenic variants.
