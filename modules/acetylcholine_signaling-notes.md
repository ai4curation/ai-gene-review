# Acetylcholine module audit

## 2026-10-26: scope and preserved starting material

The starting module contains 35 direct human products and a referenced VAChT
interface. Normal fetching and identity checks established a 36-product foundation.
Eight informative additions bring the review panel to 44: human GNB5; mouse
Chrm2, Rgs6 and Gnb5; rat Chrna9/Chrna10; and chicken CHRNA9/CHRNA10. All 2,786
original annotation rows were captured before review. Seven preexisting reviews
survived fetching unchanged. Original qualifiers and annotation payloads are
preserved; the member reviewers are assessing every row.

The required pathway is a concrete human transmission implementation, not a
universal vertebrate circuit. Generic exocytosis and PLC/cAMP effector modules
remain explicit interfaces. Their entire general-purpose protein inventories
are outside this audit; SLC18A3 itself is in scope. Receptor clustering through
AGRN/LRP4/MUSK/DOK7/RAPSN remains a separate module. Rat/chicken receptor segments
are optional comparisons and cannot replace the required human pathway.

Actual module Falcon and fallback research attempts failed. All 44 gene provider
jobs also attempted the configured services and failed; no provider-named report
was manufactured. Literature assessment uses normally fetched publication caches,
live authoritative identity checks, the cached GO-CAMs and manually assessed
source passages. Provider failure is not evidence of a biological knowledge gap.

## Receptor assemblies and literature findings

The original beta2-containing complex listed six different subunit types as one
pentamer, and the muscle complex required both gamma and epsilon. These are now
separate receptor alternatives. Human fetal and adult single-channel experiments
support gamma versus epsilon alternatives [PMID:8788941]. The source's abstract
also distinguishes the canonical functional alpha1 splice form from alpha-plus;
no functional assembly claim is transferred to alpha-plus.

Both alpha4/beta2 stoichiometries are explicit, as is the alpha5 accessory
alternative. The human alpha4/beta2 crystal study [PMID:27698419] isolated the
beta-rich form using engineered intracellular-domain deletions. The structural
review [PMID:32272141] explains composition-dependent interfaces and limited
subunit combinations. Full methods of [PMID:20881005] identify human cDNAs, a
linked beta2-alpha4-beta2-alpha4 construct plus alpha5, and electrophysiology in
oocytes. Alpha5's effect depends on receptor composition; its presence in one
alternative does not make it obligatory in all alpha4/beta2 channels.

Human alpha2/beta2 and alpha7 capacity is directly supported by heterologous
expression [PMID:8906617]. Alpha7 is represented as five identical active units
of a complex, not a monomeric pore. Human alpha3/beta4 channels with and without
alpha5 are separately supported by [PMID:8663494]. The human alpha6-containing
alternatives include beta3, with or without alpha4, and are grounded in defined
concatamer experiments [PMID:20923852]. That source remains abstract-only in the
normal PMID cache. Native mouse composition evidence [PMID:12944511] is
comparative, not a direct measurement of human native stoichiometry. Unlinked
alpha6 plus beta2 alone is not asserted to suffice.

Human alpha9/alpha10 coexpression is directly supported by [PMID:11752216].
The hair-cell review [PMID:34867208] separates cation entry from recruitment of
potassium conductance and net inhibition. Rat/chicken experiments
[PMID:22371598] directly compare channel calcium permeability and native hair-cell
physiology. Differences in the contribution of intracellular calcium stores
are condition dependent; identical channel names do not establish identical
downstream physiology. Modern canonical accessions identify the sampled
orthologs without claiming every historical plasmid is sequence-identical.
Phylogeny, synteny and intron evidence [PMID:30700248] also establishes that the
human 16-subunit repertoire cannot stand in for the whole vertebrate repertoire.

Concrete receptor subunits retain their exact UniProt identities. Attached
PANTHER descriptors use the official PTHR18945 label, verified against the
committed PANTHER ontology, and membership is independently checked in each
normally fetched UniProt record. This broad family contains other ligand-gated
channels: the descriptor does not imply universal ACh specificity or free
substitution between its members. No PAINT ancestral-node claim is invented.

## Muscarinic and regulator source assessment

The current Concise Guide [PMID:41461581] uses preferred coupling language for
M1/M3/M5–Gq/11 and M2/M4–Gi/o. Neither exclusive coupling nor interchangeable
GRK/RGS pairing follows. Direct BRET evidence [PMID:38671143] supports M1/M3
activation of G14 in specific ligand/expression contexts; the older negative
PLC assay [PMID:9875470] cannot alone justify declaring this coupling absent.

The cached human CHRM2 GO-CAM has a GNAO1-to-ADCY6 inhibitory edge with no
edge-specific evidence. M2–Go structural coupling [PMID:31073061] does not by
itself establish direct inhibition of a particular adenylyl cyclase.
[PMID:7961880] reports M4/Go-associated suppression of a cAMP-dependent reporter
in transfected JEG-3 cells. This prevents a blanket assertion that Go cannot
inhibit cAMP signaling, but does not establish an isolated direct Go–ADCY6
interaction. The full publisher text for GPR97–Go [PMID:33408414] was normally
recovered as a URL cache; its GPR97/cAMP assays must retain their receptor,
construct and readout context.

RGS6 is not interchangeable with monomeric RGS4. Purified RGS6–Gbeta5 complexes
have Go-directed GAP activity [PMID:10521509], while native mouse studies
[PMID:20884879, PMID:24318880] establish cardiac signaling regulation and
dependence on the partner. The native cardiac results do not specify every
G-alpha molecular target. GNB5 can also form other complexes under particular
experimental conditions; the dominant R7 complex role does not justify denying
all heterotrimer assembly. The module now has separate human RGS4 and RGS6–GNB5 activities and an optional native mouse Rgs6–Gnb5 cardiac segment.

## Verification and work remaining

The receptor structure has passed schema validation and 18 focused assembly
cases, including incomplete complexes and cross-species mixed pairs. The
reproducible checker is
`acetylcholine_signaling-source-analysis/check_receptor_assemblies.py`.
It verifies 20 exact receptor members and source quotations. The generic module
compiler treats a complex activity as one atom, so these assembly checks
explicitly inspect `active_units`; they are not a claim that protein presence
proves native assembly or sufficient transmission.

The module curation is complete, with 38 family-grounded activities, 38 assessed references and source evidence on every connection. All 44 member reviews have completed annotation decisions and focused validation; source-specific UNDECIDED rows remain explicit. Independent scientific QA led to corrections in VAChT ontology scope, alpha7 immune/channel wording, exact muscarinic/G-alpha selectors and regulator alternatives. Whole-repository validation and the dedicated PR are the remaining integration gates; this is not a claim of reviewed, merged project completion.


## 2026-10-26 edge and construct audit

All retained connections now distinguish direct experimental results from
biochemical synthesis. CHT1 and CHAT share choline as transported substrate;
CHAT and VAChT share acetylcholine; ACHE-generated choline returns to the
extracellular uptake pool. These are chemical relationships, not claims that
the enzymes and transporters physically bind. Human CHT1 uptake is supported
by PMID:11027560; its rate-limiting role is physiological-context dependent
and its expression is not declared universally neuron-exclusive.

The G14 segment records the direct carbachol/M1/M3 BRET activation result
(PMID:38671143), separately from Gq/11-to-PLC effector signaling. Its human
construct assignment comes from the linked platform/supplier provenance, not
a 2024 sequence declaration. M1/Gq/PLC-beta1 reconstitution (PMID:8626481)
establishes agonist- and GTP-dependent PLC activation; the abstract does not
establish that every purified construct is human.

RCSB entity-level provenance is retained with a reproducible retrieval script.
The M2 complex contains engineered human GoA, while the M1 complex uses a
Gi1/G11 chimera; neither structural assay establishes a specific cyclase
effector. The native presynaptic GRK5/M2/M4 feedback evidence is mouse, and
human receptor sequestration is an expression-system endpoint distinct from
direct receptor phosphorylation.

Independent nicotinic QA confirmed all original 16 human receptor subunits
and four rat/chicken exemplars are covered by the explicit alternatives.
Its one biological wording issue was corrected: the alpha7 channel variant
no longer equates macrophage signaling with obligatory homopentamer conduction.
Non-ionotropic immune signaling remains distinct.


Direct kinase evidence now limits explicit GRK2/GRK5 substrate targets to M2.
PMID:8798423 tests purified human M2 phosphorylation by GRK2 with charged
phospholipid dependence; the abstract does not establish kinase species.
PMID:8288567 establishes purified GRK5 phosphorylation of M2, with construct
species likewise left unresolved at abstract level. Human M2–M5 sequestration
(PMID:9495886) and native mouse M2/M4 internalization (PMID:19478075) remain
separate endpoints, not evidence of every direct kinase/subtype pair.
PMID:17065363 strengthens the human M2 inhibitory-cAMP branch while retaining
its additional condition-dependent Gs/Gq coupling. Independent supply and
muscarinic scope QA found no blocking contradiction with the member reviews.


## Final structural and member QA

All grouped muscarinic/G-alpha participants now use explicit gene-product
alternatives. Family representatives are examples, not an exhaustive allowlist,
so a broad PANTHER FAMILY selector could otherwise admit Gs, Go or G14 into
the wrong branch. Each exact selected product keeps its verified family or
subfamily descriptor. The optional regulation segment is ONE_OR_MORE of five
mechanisms; it no longer requires every GRK/RGS together. RGS6 and GNB5 remain
required partners inside their complex alternative. Twenty-one compiled
member/regulator cases verify these distinctions, alongside eighteen nicotinic
assembly cases. These are structural checks, not proof of native coexpression
or physiological sufficiency.

Independent member QA corrected VAChT molecular-function replacements that
incorrectly named cellular components, then distinguished entry into a cell
from vesicular/proteoliposome transport. The documented human VAChT serotonin
transport assay remains non-core with its construct and compartment limits.
A panel-wide is_a-only GO branch check finds no cross-aspect replacements
among 672 authored replacement terms. Twelve inherited status fields were
updated separately to COMPLETE without changing annotation content.
