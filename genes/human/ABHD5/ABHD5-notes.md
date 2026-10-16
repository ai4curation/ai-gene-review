# ABHD5 review notes

## 2026-09-27 — full ClinGen campaign audit

The source3 normal fetch supplied an INITIALIZED review with 44 PENDING assertions,
including one **NOT** triacylglycerol-lipase assertion, and 11 reference identities.
All source objects, qualifiers, partner isoforms, original identifiers and titles are
preserved. There was no prior notes file or genuine provider report.

The archived official HGNC subset identifies HGNC:21396, approved ABHD5, aliases
CGI-58 and NCIE2, with no previous symbol. UniProt Q8WTS1 is the human protein.
Root verified the five canonical paths absent on current main `3f6abf56` at 07:02 UTC;
the earlier exact base is `ba3ff58d7d2de76dbe3c24b16e05e12369f463fc`. Canonical and
separate NCIE2/CGI-58/CGI58 open-PR searches were empty; alias directories were absent.
The three imported source-file hashes match `/tmp/ABHD5-root-baseline.json` and the
source3 import receipt. Raw seed snapshots are in `/tmp/ABHD5-initial/`.

### Research and source access

The required Falcon request with `--fallback perplexity-lite --timeout 1200` and
initial publication-caching recipe ran concurrently. Both ended with exit 1 during
project build-dependency resolution: PyPI/hatchling DNS failed before the provider
or fetcher started. Logs: `/tmp/ABHD5-provider.log` and
`/tmp/ABHD5-initial-cache-fetch.log`. Neither provider was contacted; no provider
artifact was generated or authored. All five original PMID records were already
present from the normal source3 retrieval.

Normal installed-CLI fetches then attempted PMID:40818613, PMID:30361410,
PMID:37087101 and PMID:31742248 (`/tmp/ABHD5-additional-fetch.log`, terminal exit 1,
0/4), and PMID:25315780 plus PMID:26745266
(`/tmp/ABHD5-conflict-fetch.log`, terminal exit 1, 1/2 already cached). The five
missing records all failed DNS; PMID:26745266 was already a genuine full-text cache
and was not refreshed. PMID:24879803 was also already full cached. No publication
bytes were edited. External indexed primary text is recorded below as such; it was
not converted into a fabricated cached publication. Missing-cache flags remain true
even when primary full text was read externally.

### Intrinsic LPAAT versus enzyme regulation

[PMID:18606822](https://pubmed.ncbi.nlm.nih.gov/18606822/), DOI
10.1074/jbc.M801783200, has an abstract-only local record. The indexed full original
[PMC3259832](https://pmc.ncbi.nlm.nih.gov/articles/PMC3259832/) supplied Methods and
Results despite direct PMC opens showing a browser challenge. It used human
His-tagged ABHD5 expressed in BL21(DE3), nickel affinity purification, radiolabeled
LPA/PA assays and yeast overexpression. The positive product identification and
extract measurements are real observations. The mouse white-adipose fractionation
is a separate experiment. The original also reports negative human triolein,
phospholipase and lysophospholipase tests; these are not inferred from its title.

[PMID:24879803](https://pubmed.ncbi.nlm.nih.gov/24879803/) is fully cached, with
Methods and Results/Figures 2–6 read. Most bacterial purification tests concern
mouse protein. Empty-vector eluates carry LPAAT; PlsC-defective bacteria do not
recover that activity unless PlsC is added; membrane removal and stricter washes
remove LPAAT while preserving ATGL coactivation. Figure 6 separately tests human
Protein-A-ABHD5 in wild-type and ict1-deleted yeast: expression is confirmed, but
extract LPAAT does not increase. This directly addresses both premises of the
2008 assignment. The review records its intrinsic-LPAAT finding as DISPUTED with
the counterpaper attached, and removes six LPAAT/direct-PA-synthesis assertions.
It does not erase localization or all phospholipid phenotypes from the original.

[PMID:25315780](https://pubmed.ncbi.nlm.nih.gov/25315780/), indexed full
[PMC4239649](https://pmc.ncbi.nlm.nih.gov/articles/PMC4239649/), is relevant
countervailing context. Figure 1 measures LPAAT in human-ABHD5-overexpressing 293T
homogenates; the affinity-purified Sf9 preparation is used for LPGAT. These assays
are not bacterial preparations, so bacterial contamination cannot simply be
asserted for them. However, the homogenate experiment does not isolate intrinsic
human LPAAT from altered endogenous activities, and LPG is a different substrate.
No retraction or fabricated result is alleged.

[PMID:26745266](https://pubmed.ncbi.nlm.nih.gov/26745266/) is a full genuine cache.
Its plant/mouse controls do not reproduce LPAAT/LPGAT, and the plant phospholipid
and triglyceride hydrolysis assays are negative. Plant-dependent bacterial PG
depletion and S199/H379 mutation sensitivity remain interesting unresolved
mechanistic observations. They do not prove identical human chemistry. Thus the
homeostatic role can be conserved while an ancestral catalytic assignment fails.

The two inherited lipid-hydrolase assertions are rejected on the combined human
negative assays and mammalian canonical lipase-site divergence. This is not a
claim that an alpha/beta fold cannot catalyze other reactions. In particular,
peptide proteolysis is chemically different from carboxylic-ester hydrolysis.
The seeded NOT triglyceride-lipase assertion is accepted, not accidentally reversed.

### Established regulatory roles and localization

[PMID:16679289](https://pubmed.ncbi.nlm.nih.gov/16679289/) has a cached primary
abstract. It reports ABHD5–ATGL interaction, stimulation of hydrolysis, impaired
activation by human disease variants, and rescue in CDS fibroblasts. COS-7 and
mouse 3T3-L1 experiments are separately identified. Every detailed recombinant
construct in the full original was not recovered. Together with the later
purification/coactivation controls, this supports the lipase-activator MF and
positive regulation of triglyceride catabolism. The broader lipid-catabolism
row is refined to that specific process. This is ABHD5 performing regulatory work,
not assigning it ATGL's hydrolysis reaction.

The [PMID:18832586 primary full page](https://pmc.ncbi.nlm.nih.gov/articles/PMC2570125/)
was recovered through indexed Results: Figure 2H,I describes human hepatocyte and
neuronal cytoplasmic staining, and immunoelectron microscopy separately locates
protein in keratinocyte lamellar granules. The local record remains abstract-only.
The [PMID:21498505 full Results](https://pmc.ncbi.nlm.nih.gov/articles/PMC3122193/)
describe A431 lipid-droplet proteomics and CGI-58 abundance alongside the main LPCAT
targets. The supplementary peptide list was not independently inspected, and
LPCAT-specific imaging/topology panels are not attributed to ABHD5. These details
support retaining the curator's broad cytoplasm and droplet annotations. Cytosol
also remains accepted under curator deference; the precise HPA image was not
retrieved and tissue cytoplasmic labeling is not called a cytosol-specific assay.

### PNPLA1 and the epidermal lipid barrier

[PMID:30361410](https://pubmed.ncbi.nlm.nih.gov/30361410/), full indexed
[PMC6277169](https://pmc.ncbi.nlm.nih.gov/articles/PMC6277169/), distinguishes murine
co-IP/localization/Figure 4 assays from human constructs and disease variants.
The Methods explicitly name both; human cell host alone does not establish human
ABHD5. The study supports recruitment and enhanced acylceramide formation, not
intrinsic ABHD5 transacylase activity.

[PMID:37087101](https://pubmed.ncbi.nlm.nih.gov/37087101/), full indexed
[PMC10209018](https://pmc.ncbi.nlm.nih.gov/articles/PMC10209018/), uses human CGI-58,
truncated human PNPLA1 and truncated **mouse** ATGL. CGI-58 enhances lipolysis but
does not enhance the measured transacylation in that preparation. Its negative
result is retained rather than suppressed; the authors explicitly discuss missing
localization/context as a possibility, not an established explanation.

[PMID:40818613](https://pubmed.ncbi.nlm.nih.gov/40818613/), full indexed
[PMC12465037](https://pmc.ncbi.nlm.nih.gov/articles/PMC12465037/), explicitly clones
full-length human ABHD5 NM_016006.6 and human PNPLA1/PLIN2/PLIN3. HEK293T lipid assays,
COS-7 localization and cell-free proteoliposome experiments separate binding defects
from droplet-targeting defects. Forced membrane co-localization rescues the tested
mutants; direct binding is therefore not asserted as the sole stimulation mechanism.
The PNPLA1 core describes spatial/regulatory work, with the precise optional MF
omitted rather than guessing an intrinsic enzyme or adaptor term. No new process
annotation is needed to preserve the biological finding.

### Contextual peptide proteolysis and interaction policy

[PMID:31742248](https://pubmed.ncbi.nlm.nih.gov/31742248/), full indexed
[PMC6861130](https://pmc.ncbi.nlm.nih.gov/articles/PMC6861130/), reports recombinant
human ABHD5-dependent HDAC4 cleavage, dose response, AEBSF inhibition and mutant
controls with thermal-stability measurements; cellular and mouse experiments are
separate evidence. This supports describing a reported contextual protease
activity and motivates a question about endogenous generality. It does not rescue
the lipid-esterase annotations or imply that all ABHD5 chemistry is inactive. No
speculative NEW proteolysis process or additional core is added.

The full cached [PMID:32296183](https://pubmed.ncbi.nlm.nih.gov/32296183/) HuRI paper
is a binary-interaction map. All 20 seeded ABHD5 partners, including partner
isoform suffixes, match the immutable UniProt IntAct list. The generic binding
terms are removed as functionally uninformative, without alleging nonbinding or
misattribution. Independent perilipin biology does not justify inventing a specific
MF from each high-throughput pair.

### Ontology and propagation audit

Live primary AmiGO definitions/parents were checked for
[GO:0003841](https://amigo.geneontology.org/amigo/term/GO:0003841),
[GO:0042171](https://amigo.geneontology.org/amigo/term/GO:0042171),
[GO:0004620](https://amigo.geneontology.org/amigo/term/GO:0004620),
[GO:0060229](https://amigo.geneontology.org/amigo/term/GO:0060229),
[GO:0010898](https://amigo.geneontology.org/amigo/term/GO:0010898), and
[GO:0055088](https://amigo.geneontology.org/amigo/term/GO:0055088).
Some direct requests timed out; indexed AmiGO supplied the same formal definitions.
[ZFIN GO:0052689](https://zfin.org/GO:0052689) explicitly defines carboxylic-ester
hydrolysis, distinct from peptide cleavage. No source GO identifier was rewritten.

The local GO-CAM index has no Q8WTS1 hit. No NEW annotation was proposed, so no
absence-based comparator argument was used. PAINT source_entities contain only
the seeded PTNs. Full node/MSA evidence was not retrieved; this limitation is
explicit even where independent target experiments resolve the action. A target
in its own WITH/FROM is valid descendant evidence, and a single listed plant seed
is not counted as weak support. MGI/NCBI identify MGI:1915938 as mouse **Abhd4**,
not Abhd5. This matters for divergence, not because cross-paralog inheritance is
automatically invalid. UniProt Q9DBL9 is mouse Abhd5; NCBI rat Gene 316122 links
Q6QA69 with ENSRNOP00000000239. Exact donor experimental chains and ARBA rule
internals remain unresolved where not independently recovered.

### Current review state

All 44 source assertions have decisions: 15 ACCEPT, 28 REMOVE and 1 MODIFY.
The source NOT flag and partner isoforms remain unchanged; no NEW is added.
The two core units describe ATGL activation and PNPLA1 spatial/regulatory support.
The broad lipid-homeostasis term remains supported without assigning a shared
intrinsic catalytic mechanism across the family. Independent reviewer consultation
confirmed the old human LPAAT methods and the species-specific counterexperiments.
Root is independently reading the stable draft.

The recursive review/notes census currently contains 12 PMIDs, five still missing:
PMID:25315780, PMID:30361410, PMID:31742248, PMID:37087101 and PMID:40818613.
There are no provider artifacts, hidden provider bibliography, Reactome citations
or negative-test fixture citations. Immutable UniProt bibliographic links are
source metadata rather than additional manually cited review evidence. Status
remains DRAFT pending normal recovery of the five required records. Full validation,
history validation, source preservation and rendering results will be appended.

### Final independent review and checks, 2026-09-27

Root independently read every annotation rationale, all 19 reference assessments,
both cores and the questions, then checked the primary contaminant controls,
LPAAT/LPGAT substrate distinction, the 2025 human PNPLA1 construct/reconstitution
methods and the HDAC4 mutant controls. Biological review passed without a
requested action change. The PMID:37087101 source note was further narrowed to
human CGI-58 and PNPLA1 versus mouse ATGL, consistent with the inspected Methods.

`just validate human ABHD5` completed with exit 0 and all validations passed.
Its sole grouped reference warning identifies the five already declared missing
PMIDs; no additional source gate appeared. The final local integrity check
preserves all 44 complete source objects, the NOT qualifier, partner isoform
suffixes, all 11 seeded reference id/title pairs and exact UniProt/GOA bytes.
It verifies 89 cached supporting-text occurrences and seven cached publication
titles. One ordinary supporting-text quote from the externally read primary
PMID:40818613 remains cache-dependent; it is not presented as a recovered local
record. The recursive YAML/notes/provider census remains 12 PMIDs with five
missing records, no Reactome IDs and no provider artifact. The checked review
stays DRAFT. Logs and the explicit publication manifest preserve these limits.

### PR 3287 evidence and term-scope follow-up, 2026-09-27

The exact reviewed head was `afd87b03e1c37589d03d084a942c5a84b5ad1411`.
All 44 source assertions, their actions, all 19 reference identities and both
core units are preserved. The changes address the full reviewer comment
[5854544244](https://github.com/ai4curation/ai-gene-review/issues/3287#issuecomment-5854544244).

The five missing records remain normal-cache requirements. Their VERIFIED
assessments mean that the intended primary identities and relevant content were
independently inspected; they do not claim that a local cache exists. Direct PMC
opens intermittently returned browser challenges during this follow-up, while
indexed original PMC pages supplied the relevant text. The rechecked routes are
PMID:25315780 / [PMC4239649](https://pmc.ncbi.nlm.nih.gov/articles/PMC4239649/),
PMID:30361410 / [PMC6277169](https://pmc.ncbi.nlm.nih.gov/articles/PMC6277169/),
PMID:31742248 / [PMC6861130](https://pmc.ncbi.nlm.nih.gov/articles/PMC6861130/),
PMID:37087101 / [PMC10209018](https://pmc.ncbi.nlm.nih.gov/articles/PMC10209018/),
and PMID:40818613 / [PMC12465037](https://pmc.ncbi.nlm.nih.gov/articles/PMC12465037/).
The last paper's existing ordinary supporting-text quote about restoring mutant
co-localization is verbatim in the primary abstract, also reproduced in PubMed.
Its Methods explicitly specify human ABHD5 NM_016006.6 and human PNPLA1 constructs.
The quote remains an ordinary cache-dependent quote; it was not moved into a
different field to avoid the missing-source check. No unchanged normal-fetch
failure was repeated. The already dispatched source10 recovery must be verified
and imported before these five gates can close.

The PNPLA1 unit now has an explicit curator question about the molecular-function
term. Live [GO:0060229](https://amigo.geneontology.org/amigo/term/GO:0060229)
specifies activation of lipid hydrolysis, whereas the PNPLA1 assay measures
transacylation. Live [GO:0008047](https://amigo.geneontology.org/amigo/term/GO:0008047)
defines an increase in catalytic activity and its comment requires direct enzyme
interaction without covalent modification. It is also the parent of the existing
lipase-activator term. Wild-type association, droplet targeting and restoration
of activity by forced co-localization of binding-defective mutants are distinct
results. They justify retaining the biological PNPLA1 unit while leaving its
most suitable GO MF as an explicit curator question. No NEW row, redundant
ancestor or unverified mechanism is added.

The cytoplasm row no longer uses a tissue-expression fragment as localization
support. It retains the correct UniProt localization statement and a short exact
external primary localization excerpt with its PMC2570125 route and human
Figure 2 context. Local PMID:18832586 remains abstract-only. The description now
states the bounded recombinant-human HDAC4 cleavage result directly; the LPAAT
controversy and its assay controls remain in these notes and the relevant rows.

SOURCE_BAD on the Rhea/EC propagation block concerns the challenged assignment
of ABHD5 to those reactions, not the existence or correctness of the reaction
identifiers. Those comments already make this distinction. Direct biochemical
counterexperiments support the source-assignment judgment, so replacing it with
a weak-source label would lose that distinction. A future upstream UniProt
curation report should include the original positive study, the controlled
counterexperiments and the different LPGAT preparation; no external ticket was
sent by this follow-up.

### Source10 import and recovered-text assessment, 2026-09-27

The five required normal-fetch records were imported without overwrites under
`tmp/source10-canonical-import-receipt.json` (SHA256
`18d517caec871b4306b21283bb89204639ecc0b25f6f495802bd664d072c8359`).
All five exact canonical byte hashes match that receipt. PMID:25315780 remains
abstract-only; PMID:30361410, PMID:31742248, PMID:37087101 and PMID:40818613 now
contain full-text extractions. Reference access flags now reflect those actual
caches rather than the earlier failed local fetches. The five normal publication
cache gates are closed; the earlier failure notes remain historical provenance.

Rereading the recovered Methods, Results and captions preserves the two lipid
regulatory cores and every annotation action. PMID:30361410 Figure 4 uses murine
proteins, while Figure 5 explicitly tests human ABHD5 variants with human PNPLA1.
PMID:37087101 uses human CGI-58 and PNPLA1 with mouse ATGL and preserves the
preparation-specific absence of enhanced transacylation. PMID:40818613 Figure 7
and the human-construct Methods confirm the forced proteoliposome co-localization
rescue, including the two variants with reduced PNPLA1 binding. Its existing
abstract quote is now verifiable directly against the normal cache.

The fuller PMID:31742248 Methods reveal a source-label limitation: human HDAC4 is
explicit, but the ABHD5 expression plasmid is named
`6XHis-smt3-TEV-mABHD5`. The Results compare mouse Ser239 and human Ser237 and
use Ser237 mutant numbering. The precise sequence behind that construct name was
not independently resolved here. Therefore the current description and reference
assessment avoid the earlier unqualified attribution to recombinant human ABHD5.
This is an explicit narrowing of assay provenance, not evidence of wrong-gene
curation. The dose response, inhibitor, mutant and thermal-stability assays still
support reported ABHD5-dependent peptide cleavage; human-cell and mouse results
remain separate. No protease annotation or core is added.

The 2015 notice linked by PMID:25315780 was independently read on the indexed
original [PMC4281727](https://pmc.ncbi.nlm.nih.gov/articles/PMC4281727/),
[DOI:10.1074/jbc.A114.573857](https://doi.org/10.1074/jbc.A114.573857).
It corrects author-affiliation symbols only; it contains no assay or data
correction. PubMed's original record lists the erratum bibliographically and the
PMC notice displays no PMID. Targeted primary PubMed/DOI searches did not confirm
a separate PMID; the identifier-conversion API was inaccessible. This is recorded
as an externally inspected DOI/PMC-only notice with no normal local cache, not
silently mapped to the original paper or to an invented PMID. It does not alter
the biological source judgment. There are no provider artifacts or new PMID
citations in this follow-up.

Final targeted validation passed with exit 0 and zero curation warnings. The
review status is COMPLETE; all 12 cited PMIDs are normally cached, and the
separate externally verified DOI-only affiliation notice remains explicit.
Final schema, history, rendering, immutable-field and literal-quote checks are
recorded in the follow-up manifest. Completion of this local review does not
claim PR approval, publication or merge.
