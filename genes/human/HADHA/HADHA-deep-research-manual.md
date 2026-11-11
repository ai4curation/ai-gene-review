# HADHA: manual primary-source research

Date: 2026-11-11. This is manual research, not a provider-generated report.
The configured Falcon attempt returned HTTP 403 (JWT required), and the
Perplexity fallback returned HTTP 401/quota exhaustion. Neither produced a report.
This synthesis uses original articles, retained native publication records,
UniProt, current QuickGO definitions and the cached GO-CAM model.

## Catalysis and substrate range

HADHA is the alpha subunit of mitochondrial trifunctional protein. Expression of
human alpha-subunit cDNA establishes enoyl-CoA hydratase and hydroxyacyl-CoA
dehydrogenase activities; the beta-subunit cDNA establishes long-chain thiolase
activity [PMID:8135828](https://pubmed.ncbi.nlm.nih.gov/8135828/). The original
purified human mitochondrial complex was active with C6 and longer substrates,
had maximal measured dehydrogenase activity at C10-C16, and lacked C4 activity
[PMID:1550553](https://pubmed.ncbi.nlm.nih.gov/1550553/). Preference must not be
rewritten as exclusion of every chain outside C10-C16. These older retained
records are abstract-only; no complete old article inspection is claimed.

The human structural studies support the alpha2-beta2 complex at the inner
membrane and separate alpha hydratase/dehydrogenase from beta thiolase
[PMID:29915090](https://pubmed.ncbi.nlm.nih.gov/29915090/),
[PMID:30850536](https://pubmed.ncbi.nlm.nih.gov/30850536/). The retained
PMID:8651282 abstract also describes patient fibroblast expression and
gel-filtration evidence for stabilization of the assembled complex. Its previous
review note incorrectly said the cache was missing.

Current QuickGO defines [GO:0018812](https://www.ebi.ac.uk/QuickGO/term/GO:0018812)
as a specific child of [GO:0004300](https://www.ebi.ac.uk/QuickGO/term/GO:0004300).
Both definitions use dehydration equations; the hydratase parent explicitly
discusses the reverse hydration direction. The label alone therefore does not
justify replacing the dehydratase annotations. The nine broader molecular-function
rows are refined with MODIFY to the supported specific activities, including
GO:0018812 for its GO:0004300 parent. This is a specificity correction, not a
rejection of the broader chemistry. NAD+ binding, root mitochondrial location
and the informative pathway-level fatty acid metabolic process remain accepted;
the latter is distinct from an uninformative generic molecular-function class.

GO:0003985 describes the C4 acetyl-CoA/acetoacetyl-CoA reaction. The alpha/beta
activity separation and absent C4 activity support removing that assertion from
HADHA. This is not an instruction to transfer the same C4 term to HADHB.

## Cardiolipin activity and protein identity

The original full [2012 article, PMID:23152787](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0048628)
describes full-length human alphaTFP/HADHA expression using a cell-free E. coli
system, His-tag purification and a second MLCL affinity step. The purified
protein acylated MLCL with linoleoyl-, oleoyl- and palmitoyl-CoA. Figure 2 and
the reported kinetic measurements identify linoleoyl-CoA as the preferred
tested donor. This differs from the native UniProt prose assigning greatest
activity to oleoyl-CoA; the machine-fetched source is preserved and the review
follows the original experimental comparison.

Table 2 tests lysophospholipid specificity: other tested lysophospholipids did
not show detectable acyltransferase activity. The definition of
[GO:0071617](https://www.ebi.ac.uk/QuickGO/term/GO:0071617), lysophospholipid
acyltransferase activity, fits acyl-CoA-dependent MLCL reacylation. Using it for
the core function does not imply activity on all lysophospholipids. The follow-up
proposes exactly one NEW molecular-function row from this direct full-length
protein assay. No specific transferase branch is present among the 60 native
contexts; the broad catalytic-activity row is refined to the three supported
activities. Existing cardiolipin-remodeling BP rows need no new process term.

The full-length assay must be distinguished from the previously described
MLCLAT1 protein corresponding to alphaTFP without its first 227 residues.
Neither should be silently equated with current UniProt isoform 2, whose
sequence changes are different. Human engineered and patient-derived
cardiomyocyte experiments support HADHA involvement in fatty acid oxidation
and cardiolipin remodeling [PMID:31604922](https://doi.org/10.1038/s41467-019-12482-1).
The retained full article includes Results and Methods. Its loss-of-function,
lipidomic and respiratory observations do not by themselves establish every
step in the proposed tafazzin-to-HADHA remodeling model. Direct catalytic
participation is supported by the earlier recombinant-protein experiment.

## Unresolved hydrolase annotation

The [original PMID:22586271 main article](https://pmc.ncbi.nlm.nih.gov/articles/PMC3416193/)
describes recombinant THEM4/THEM5 and THEM5-mutant thioesterase experiments.
Figure 4C mentions MLCLAT1 in downstream reacylation context. That mention is
not proof of an assay of canonical HADHA. The retained cache contains only
Abstract, Introduction and Discussion despite its full-text flag. The original
main article was inspected, but the listed supplementary PDF
`MCB.00312-12_zmb999109558so1.pdf` could not be read: PMC returned a download
interstitial, Europe PMC returned HTTP 500, and the publisher endpoint failed.
No claim of complete supplementary inspection or universal absence is made.

Current GOA still asserts HADHA/P40939 GO:0052816 by IDA with this PMID.
The cached model `gocams/67b1629100002092/67b1629100002092-src.yaml`, activity
`67b1629100002145`, repeats this term/reference and specifies tetralinoleoyl
cardiolipin as output. The [GO:0052816 definition](https://www.ebi.ac.uk/QuickGO/term/GO:0052816)
instead describes fatty acyl-CoA hydrolysis to fatty acid and CoA. This is an
unresolved activity/reference/output discrepancy for curator clarification,
not a basis for confidently declaring the gene product wrong. Use UNDECIDED
and withdraw the categorical source defect. Preserve the original GOA fields
and earlier history record.

## Interaction and nucleoid evidence

The fresh native seed separates four PMID:20562859 ATG8-family partner contexts:
GABARAP, GABARAPL2, MAP1LC3B and GABARAPL1. Curated IntAct co-immunoprecipitation
and pull-down records and UniProt corroborate these associations. HADHB and
HTT contexts are also retained. Structural evidence for the alpha-beta complex
is stronger than co-complex detection alone; no adaptor or autophagy-receptor
activity is inferred from interaction data. The ten generic binding contexts
are kept as non-core under the ClinGen binding policy.

For the nucleoid annotation, the original PMID:18063578 attribution is retained,
but HADHA-specific crosslink behavior was not independently established.
Original [PMID:22453275](https://pmc.ncbi.nlm.nih.gov/articles/PMC3401451/)
Tables 1 and 2 identify HADHA in human HEK293T nucleoid purification and ATAD3B
affinity/SILAC experiments. That positive association evidence supports a
non-core location without asserting direct mtDNA binding, replication or
translation activity. The native full-text cache was already in Git and is
reused unchanged. The three proteomics references whose retained main texts
do not expose HADHA-specific supplementary entries are explicitly marked
unverified for target-specific support; their curator attributions and the
independently supported biological assertions are preserved.

## Source and scope checks

Fresh QuickGO has 60 source rows and 60 seeded contexts; one evidence-backed NEW
MF is now proposed separately; the prior 57-context
review collapsed three additional ATG8 partner contexts. All native annotation
fields and 28 inherited supporting-text occurrences are preserved. The five
PTHR43612 quotations of HADHA UniProt remain supported by the refreshed native
record. No family, module or cached GO-CAM source is edited. One independent
annotation reviewer assessed all 60 contexts and a second checked the disputed
hydrolase evidence. Canonical validation and final draft review are separate
delivery gates.
