# ACTN2 curation notes

## 2026-11-27: source acquisition and scope

Human ACTN2 is HGNC:164 and UniProt P35609. Native `just fetch-gene human ACTN2`
created the UniProt record, a 209-row GOA table and 208 annotation contexts. Two
PMID:9501083 titin-binding source rows share the native seeding key; all raw TSV
rows are retained. The two
UniProt alternative products are retained without interpreting every assay as
isoform-specific. Each native context, including its supporting entity, is
reviewed separately; repeated term/evidence/reference combinations are not
automatically duplicates.

The ClinGen project lists ACTN2-related cardiac and skeletal myopathy as an
autosomal-dominant definitive association. Disease membership sets the review
scope; it does not establish a molecular activity or justify a new GO process
annotation.

Falcon research failed authentication. Its Perplexity-lite fallback failed with
an insufficient-quota response. No provider-generated research report is claimed.
This is a manual synthesis of primary literature, the native sources and
independent annotation reviews. Publication caching succeeded for all 46 native
PMIDs. Additional papers were cached with the native publication fetcher.

## Structural function and regulation

ACTN2 forms an antiparallel dimer with actin-binding domains at its ends, a rod of
spectrin repeats, and a C-terminal calmodulin-like region. Its principal muscle
function is structural: crosslinking actin and linking the actin/titin system at
the Z-disc. The human protein structure and associated biochemical experiments
support this model directly [PMID:25433700, *The structure and regulation of human
muscle α-actinin*; "a complete high-resolution structure of the
200 kDa α-actinin-2 dimer from striated muscle"].

The EF-hand-like domains are not sufficient evidence that ACTN2 binds calcium.
Muscle α-actinin-2 is calcium-insensitive; the original human cloning study
predicted disrupted calcium-binding capacity, and structural work describes
phosphoinositide regulation instead [PMID:1339456; PMID:25433700]. PIP2 and titin
Z-repeat binding modulate a closed/open conformational equilibrium involving an
intramolecular neck pseudoligand. This is not evidence that ACTN2 hydrolyses
phosphoinositides or catalyses an angiotensin signaling reaction
[PMID:11101506; PMID:25433700].

Human ACTN2 actin-binding-domain variants have been examined with purified
proteins and in cardiomyocytes [PMID:27287556]. A later tension-sensor study uses
human induced pluripotent stem cell-derived cardiomyocytes to investigate force
transmission through engineered ACTN2 constructs [PMID:41695113]. Neither
disease association nor a sensor experiment makes ACTN2 a motor or an ATPase.

## Neuronal and channel-associated roles

The neuronal structural function is supported by rat hippocampal knockdown and
human ACTN2 rescue experiments: α-actinin-2 organizes spine actin and promotes postsynaptic
density assembly. Calcium sensitivity and paralog choice matter in that rescue
system [PMID:25007055]. The human construct is assayed in rodent neurons;
necessity in human neurons is not established. A separate primary study investigates
ACTN2–CaMKII binding and spine structural plasticity [PMID:37489746]. Its
kinase-binding result should not be mistaken for kinase activity of ACTN2.

Channel-associated evidence is assessed in its own experimental context.
Kv1.5, SK2 and NaV1.5 studies examine different effects on coupling, current and
surface localization [PMID:10812072; PMID:17110593; PMID:19815520;
PMID:19943616]. An interaction does not establish intrinsic ion transport by
ACTN2, and a current phenotype does not automatically establish direct gating.

## Source and ontology checks

The GO-CAM index in the intake revision contains no ACTN2/P35609 match. The
cached PANTHER 19.0 tree and PAINT snapshot dated 2026-08-28 report no IRD/IKR
loss on the ACTN2 lineage. This is a check of the retained snapshot, not a claim
of fresh verification of the complete upstream PAINT release.

Live UniProt identity checks identify the electronic-annotation donors Q9JI91
as mouse Actn2 and A0A8I6ARF4 as rat Actn2. Identifying the donor does not by
itself adjudicate every transferred function.

Live Reactome participant queries include P35609 in all seven cited events:
R-HSA-390593, R-HSA-390595, R-HSA-390597, R-HSA-390598, R-HSA-432164,
R-HSA-481007 and R-HSA-5672965. These include modeled complexes and sets.
Absence of ACTN2 from an event's short prose summary is not evidence of a wrong
gene annotation. Presence in a participant list does not transfer the catalytic
activity of myosin, a calcium channel or a RAS exchange factor to ACTN2.

A further entity-level check resolves the platelet localization: event 481007
links input 481003 through DefinedSet 349780 to ACTN2 entity 349727 in
GO:0031093 platelet alpha granule lumen. Its output 481033 links through
DefinedSet 349778 to ACTN2 entity 349725 in GO:0005576 extracellular region.
Both terminal entities identify human P35609. Thus ACTN2 is specifically modeled
as cargo, not merely found in an undifferentiated participant list. This supports
retaining the localizations as non-core; it does not verify ACTN2-specific peptides
in the original experiments or establish conventional secretion as its main role.

Core-function term definitions were checked against the live QuickGO service,
including GO:7770064 actin-filament cross-linking activity, GO:0045214 sarcomere
organization and GO:0098973 structural constituent of postsynaptic actin
cytoskeleton. Author-supplied terms will also undergo native term validation.

Supported generic protein binding follows the ClinGen project policy:
KEEP_AS_NON_CORE when a specific molecular function cannot be justified;
UNDECIDED for inaccessible or unadjudicated evidence. An abstract mentioning
another paralog is not grounds to remove an experimental annotation. Formal
review status will reflect retained warnings and unresolved evidence.

## Source preservation and execution

One registered sparse Orca checkout and its retained runtime are reused, with
ROOT as the sole curated-file writer. Read-only helpers return evidence and
annotation proposals. Native fetch refreshed ten inherited publications and a
PANTHER metadata record. The fetched versions were retained under the Git
recovery ref `refs/recovery/clingen-actn2-20261127/native-cache-v1`, and the
inherited files were restored before annotation review. In particular, the
inherited PMID:24550280 text is fuller than the new fetch. No inherited cache
change is part of this gene review.

The public project remains at checkpoint 766 until ACTN2 is reviewed, validated
and delivered through its own PR. This work does not yet earn completion credit.

## Validation and review outcome

All 208 native annotation contexts are adjudicated: 41 ACCEPT, 143
KEEP_AS_NON_CORE, 22 UNDECIDED, one TOO_GENERAL and one REMOVE. The source
identities, evidence codes, qualifiers and supporting entities are preserved.
No NEW annotation contexts are proposed. The two core functions summarize
Z-disc crosslinking and postsynaptic actin organization; they do not convert
disease phenotypes or channel-binding results into additional process claims.

Native gene validation and history validation pass. The quote checker verifies
all 40 supporting-text occurrences, with no missing, unmatched or unchecked
sources. The native status calculation retains DRAFT. Remaining advisories
cover the 113 supported generic-binding contexts retained under project policy,
the crosslinking core term not mirrored as a NEW annotation, and the retained
Python runtime's version warning. The runtime was used without synchronization;
no local environment was created and the lockfile is unchanged.

Independent biological QA found no blocking issue after examining the two core
functions, all non-generic-binding rationales, and the identities and assay
limits across the generic-binding contexts. It independently checked the
four-EF-hand calcium-coordination passage, the human-construct/rat-neuron
rescue evidence, and the unresolved internalization-versus-recycling mechanism.
This does not replace the stated limits on inaccessible supplements or
unverified source-specific results.
