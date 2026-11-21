# HADH manual primary-source research — 2026-11-11

This is a manual research record. The native Falcon call returned HTTP 403
(missing JWT); its Perplexity fallback returned HTTP 401 (quota exhausted).
Neither provider produced a report. The source and annotation checks below use
the current native UniProt/QuickGO fetch, original articles or bibliographic
abstracts, and the retained publication cache. An abstract or an incomplete
article extraction is not described as a complete full-text review.

## Identity, reaction and localization

Human HADH is Q16836, HGNC:4799. Its canonical precursor is 314 residues, with
a 12-residue mitochondrial transit peptide and a mature chain at 13–314.
The original human cloning study establishes this identity and targeting
sequence ([PMID:8687463](https://pubmed.ncbi.nlm.nih.gov/8687463/)). UniProt
assigns mitochondrial matrix localization and a homodimeric enzyme that
performs the NAD+-dependent third reaction of fatty-acid beta-oxidation.

The human enzyme was expressed, purified, assayed and crystallized with NAD+
in [PMID:10231530](https://pubmed.ncbi.nlm.nih.gov/10231530/). Substrate placement
in that paper was modeled; the actual substrate/ternary structures belong to
[PMID:10840044](https://pubmed.ncbi.nlm.nih.gov/10840044/). Their retained abstracts
support those distinctions. The inspected evidence establishes a homodimer,
without independently demonstrating that dimerization is obligatory.

The paper's His158/Glu170 use mature-chain numbering, corresponding to
precursor His170/Glu182. Likewise, D45G/Y214H in
[PMID:16725361](https://pubmed.ncbi.nlm.nih.gov/16725361/) correspond to precursor
D57G/Y226H. P258L in [PMID:11489939](https://pubmed.ncbi.nlm.nih.gov/11489939/)
already uses precursor numbering and must not be shifted. Original quotations
are retained unchanged; explanatory statements distinguish these conventions.
The standalone biological description avoids ambiguous residue numbers.

GO:0005737 cytoplasm includes organelles. Its current QuickGO definition is
compatible with mitochondrial matrix localization and does not assert a
cytosolic pool. The former claim of a LIFEdb fusion/import artifact was
unsupported. The original LIFEdb experiment has not been independently
re-examined; accepting the broad compartment does not require inventing an
artifact or a separate cytosolic function.

## Substrate breadth

Human UniProt assigns the C16 reaction RHEA:31159 by similarity to pig P00348.
The pig record cites [PMID:2817332](https://pubmed.ncbi.nlm.nih.gov/2817332/),
whose abstract reports assays with different chain lengths and medium-chain
preference alongside long-chain activity. GO:0016509 covers substrates with
13–22 carbons. The C16 mapping is therefore not refuted by short/medium-chain
preference. The biochemical activity is credible, but the updated review marks the human
long-chain functional assignment as over-annotated because its physiological
relevance is unresolved. Similar Km values do not establish comparable catalytic
efficiency. This does not deny the pig activity, assert assay noise or establish
a wrong-paralog transfer; HADHA supplies the dedicated long-chain pathway step.
The full 1989 methods and tables were not independently inspected.

## Regulatory function and differing islet observations

[PMID:20670938](https://pubmed.ncbi.nlm.nih.gov/20670938/) reports mouse Hadh
knockout, protein association and islet enzyme-kinetic evidence supporting
inhibitory regulation of GDH. The original abstract and retained discussion
were read. The cached record is marked full text, but its extracted body does
not include the methods/results sections. The PMC page returned a browser
challenge and the Europe PMC full-text endpoint returned HTTP 500; no claim
of having inspected those missing sections is made.

That study reports amino-acid-sensitive insulin hypersecretion with normal
glucose responses, including with added octanoate or palmitate. In contrast,
[PMID:21990309](https://pubmed.ncbi.nlm.nih.gov/21990309/) reports increased
glucose and glucose-plus-palmitate responses in its mouse knockout islets.
These observations are preserved separately, without inventing a resolution.
The latter study also supports cold-tolerance/body-weight phenotypes; its
abstract and retained source were consulted. Such physiological consequences
are retained as non-core processes.

Human clinical and expressed-variant studies support the HADH disease link
and enzyme function (PMIDs 11489939 and 16725361). They do not by themselves
constitute a direct human HADH–GLUD1 inhibitory assay. The additional
regulatory core function and its insulin-secretion annotations consistently
state the principally mouse mechanistic evidence and human orthology inference.

## Traceable rodent response annotations

Current QuickGO rat Q9WVK7 annotations identify the original RGD sources:

| Human term | Rat evidence / reference | Observation in the inspected abstract |
|---|---|---|
| GO:0009410 response to xenobiotic stimulus | IDA, [PMID:12176671](https://pubmed.ncbi.nlm.nih.gov/12176671/) | Fenofibrate increased skeletal-muscle HADH activity. |
| GO:0009725 response to hormone | IEP, [PMID:18191600](https://pubmed.ncbi.nlm.nih.gov/18191600/) | Low-dose growth hormone increased myocardial hydroxyacyl-CoA dehydrogenase in rats with heart failure. |
| GO:0014823 response to activity | IDA, [PMID:8231758](https://pubmed.ncbi.nlm.nih.gov/8231758/) | Exercise training increased HADH activity in rat gastrocnemius and soleus. |
| GO:0032868 response to insulin | IEP, [PMID:7050060](https://pubmed.ncbi.nlm.nih.gov/7050060/) | Insulin normalized the elevated HADH activity of diabetic rat diaphragm. |

The first three identities/abstracts were checked through PubMed; the final
record was retrieved through Europe PMC's MED core-record endpoint and agrees
with the RGD/QuickGO attribution. Native publication fetching produced the five
new caches, including PMID2817332, without editing their contents. The rat
response evidence supports contextual non-core retention; it does not establish
direct human responses, hormone receptor activity, or insulin secretion itself.
The inspected abstracts do not supply substrate/isozyme-selectivity methods, so
they do not independently resolve HADH from HADHA or other enzyme contributors.
The retained gene attribution is RGD's; it is not independently verified here.

## Proteomics and source limits

[PMID:34800366](https://pubmed.ncbi.nlm.nih.gov/34800366/) describes the human
mitochondrial proteome resource cited by GOA. Its title is not gene-specific
evidence, and no HADH/HCDH/hydroxyacyl match was found in the retained article
text. The relevant supplementary row was not independently inspected. The
candidate retains curated GOA attribution plus independent mitochondrial
localization evidence; it does not allege that the curator made an error.

## Scope and provenance

The native source refresh contains 41 rows and 41 review contexts, all canonical
Q16836, with no NOT flags or annotation extensions. Native seeding retained all
41 inherited judgments and added 21 source-entity links before curation. No NEW
GO assertion is proposed. Broad molecular-function ancestors are refined to the
experimentally supported GO:0003857 with MODIFY; pathway-level metabolism and
valid compartment assertions remain accepted. Genericity is not a non-core role.

Open PR search hits #6203, #6122 and #5076 had no direct HADH gene/history/cache
file overlap in their full paginated filename lists. #5076 does edit the
beta-oxidation module and #6203 has a separate HADH HMM benchmark; neither is
changed here. Exact inbound `human/HADH/` references were absent from the
inspected gene, family, module and GO-CAM review sources at main 0ca78c07.
Canonical application was submitted in PR #6312. The subsequent review follow-up
refines molecular-function granularity and evidence limits; remote checks and
verified merged delivery remain pending.
