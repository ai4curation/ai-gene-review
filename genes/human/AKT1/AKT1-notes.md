# AKT1 notes

## PN proteostasis review - 2026-06-03

Falcon deep research was already present and used for the re-review. It supports the core AKT1
function as a PI3K-regulated serine/threonine kinase rather than a proteostasis-specific protein
[file:human/AKT1/AKT1-deep-research-falcon.md "AKT1 is a **serine/threonine protein kinase** (PKB)"].

The Proteostasis PN projection places AKT1 under chaperone-mediated autophagy regulation and maps it
to `GO:1904715 negative regulation of chaperone-mediated autophagy` as more specific than the
existing broad GOA annotation to `GO:0010507 negative regulation of autophagy`
[file:projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv "AKT1 GO:1904715 negative regulation of chaperone-mediated autophagy more_specific_than_existing_goa"].
The parent PN type is mapped to the directional GO term because it records inhibitory CMA roles
[file:projects/PROTEOSTASIS/mappings/autophagy_lysosome_pathway.yaml "This PN type explicitly records inhibitory roles for CMA"].
The narrower "Modulator of LAMP2A multimerization" subtype is useful triage context but has no direct
GO mapping by itself, so I did not create a LAMP2A-specific GO assertion
[file:projects/PROTEOSTASIS/mappings/autophagy_lysosome_pathway.yaml "curation_status: no_mapping"].

The CMA projection is supported by Arias et al. 2015. The paper identifies a lysosomal
mTORC2/PHLPP1/Akt axis in which Akt1 inhibits CMA; Akt inhibition or Akt1 loss increases CMA reporter
activity and LAMP-2A translocation-complex assembly [PMID:26118642 "Overall, these results support an inhibitory effect of Akt1 on CMA"].
Mechanistically, the authors connect Akt activity to GFAP phosphorylation and LAMP-2A complex
dynamics, which supports a regulation term rather than direct CMA substrate delivery machinery
[PMID:26118642 "Inhibition of Akt activity in isolated lysosomes lead to a similar dose-dependent increase"].

Existing GOA already has broad autophagy/proteolysis annotations. The older reporter assay supports
AKT1 as an autophagy inhibitor because AKT1 knockdown increased LC3 reporter release
[PMID:18387192 "Knockdown of AKT1 resulted in an increase of dNGLUC release"].
Macroautophagy evidence remains non-core and context dependent; in mammary epithelial detachment,
PI3K-AKT-MTORC1 activation was not enough to suppress autophagy
[PMID:23778976 "not sufficient to suppress detachment-induced autophagy in MECs"].

Other proteostasis-adjacent AKT1 annotations are substrate or stress contexts, not core functions.
AKT phosphorylation of Rac1 supports FBXL19-mediated ubiquitination and degradation
[PMID:23512198 "Protein kinase AKT-mediated phosphorylation of Rac1 at serine(71) was essential"].
AKT/CHIP/tau work supports a substrate-specific negative regulation of protein ubiquitination
[PMID:18292230 "Akt also prevents CHIP-induced tau ubiquitination"].
The heat response annotation is also non-core: Akt suppression increases thermosensitivity, but the
paper attributes acquired thermotolerance primarily to Hsp72/JNK regulation
[PMID:10958679 "Suppression of Akt or ERK1 and -2 kinases increased cell thermosensitivity"].

Curation decision: retain AKT1 core functions as PI3K-regulated kinase activity and PH-domain
phosphoinositide binding. Add `GO:1904715 negative regulation of chaperone-mediated autophagy` as a
`NEW` non-core proposed annotation supported by PMID:26118642 and the PN projection. Do not make AKT1
a core proteostasis or direct CMA machinery gene, and do not add a new ontology term.
# AKT1 source audit — 2026-09-27 (initial pass)

The starting review contains 445 seeded annotations, one previous NEW proposal,
233 references and two core entries. The current-main baseline was independently
confirmed before editing: review Git blob
`2da14e5e9b3cabfd00b96dcf5f924c39f9be8ce6`, notes
`b5fa9cab0b5eaa035e54ab5ce3e31d61213276c8`, and HTML
`4ffd4adb26ea99aceb1783a9148e353aa8d63e6e`. The parent coordinator found no overlapping
open PR under AKT1, PKBalpha or RACPKalpha. The cached UniProt record is P31749,
with symbols AKT1 and synonyms PKB/RAC; the human nomenclature identifier is
HGNC:391. Machine sources and generated PN notes remain unchanged.

The genuine pre-existing Falcon report (2026-05-02, 486.15 seconds) is retained
as background. It mostly synthesizes reviews and drug-development literature;
its prose is not a replacement for source-specific primary evidence. The first
pass has read the 144 cached PMID abstracts or available source summaries.
Seventy-eight Reactome references are present, of which 24 have local caches and
54 require external source access. All cited PMID paths initially exist, but
PMID:36126419 is only a metadata placeholder and is not a usable abstract cache.
The review is DRAFT while this substantive audit continues.

Scheduling scope correction: the coordinator confirmed that AKT1's strongest
ClinGen association in this campaign is Limited (Cowden syndrome 6), rather than
Definitive. This review was already underway and continues as an explicitly
recorded scheduling exception; the evidence standards are unchanged. The
coordinator owns the corresponding shared-project table and log correction.

The next pass read all 78 referenced Reactome event/pathway records (77 live
event pages, plus the cached CD28 pathway summary and its live Cot-phosphorylation
constituent after the parent page failed). The 136 associated rows now have
source-specific reasons in place of a repeated Falcon sentence. The audit keeps
AKT's kinase activity distinct from its substrates' enzymes and from upstream
kinases acting on AKT. E17K-specific predicted events remain explicitly modeled
inferences; their retention at the general kinase/location level does not claim
that each mutant-specific substrate reaction was experimentally tested.

Five cytosol rows require source-specific plasma-membrane replacements:
R-HSA-1497784, R-HSA-1497796, R-HSA-1497810, R-HSA-202111 and R-HSA-202127.
Their Participants sections place the AKT-containing NOS3/CaM/HSP90 complex at
the plasma membrane; the cytosolic participants are metabolites. By contrast,
R-HSA-202137 genuinely recruits cytosolic AKT into the membrane complex and
supports both locations. R-HSA-377186 currently places the AKT catalyst in the
cytosol and its mTORC1 substrate at the lysosomal membrane, so its old plasma-
membrane row is refined to cytosol. These are source-specific updates, not claims
that AKT lacks either cellular pool. Each live source is linked in its reference
assessment as `https://reactome.org/content/detail/<stable_id>`.

Reactome R-HSA-199863 explicitly discusses a dispute over the physiological
NR4A1 kinase (AKT versus RSK/MSK). This caveat also affects the predicted E17K
counterpart R-HSA-2399988. It does not negate AKT's independently established
serine/threonine kinase activity or nuclear pool. Several shear-flow event pages
contain inconsistent residue prose; the modeled participants identify AKT
Thr308/Ser473 and NOS3 Ser1177. Original machine-fetched titles remain unchanged.

Initial adjudication replaces 21 legacy generic-protein-binding OVER judgments
with source-specific REMOVE reasons. These remove uninformative molecular-function
assertions without claiming the measured interactions are false. Substrate,
upstream regulator, chaperone-client and scaffold roles are kept distinct. Where an
abstract does not identify the individual curated pair, that limit is explicit.
Other generic-binding rows and all remaining annotation groups are still under
review; existing untouched actions are not yet final audit conclusions.

External primary-source checks completed during this pass:

- [PMID:11438723, full original PMC35401](https://pmc.ncbi.nlm.nih.gov/articles/PMC35401/):
  Methods describe full-length PKB constructs and DHFR-fragment complementation;
  the study maps interactions and their responses to signaling perturbations.
  This establishes the assay context without inventing an AKT1 adaptor function.
- [PMID:18786403, full original PMC2597217](https://pmc.ncbi.nlm.nih.gov/articles/PMC2597217/):
  the Results subsection on Akt/CDK phosphorylation and the Akt Phosphorylation
  Methods explicitly use Akt1/PKBalpha to phosphorylate FOXO1 Ser256. Figure 5
  distinguishes phosphorylation from a change in FOXO1 DNA affinity. The direct
  page opened successfully; after an intermittent browser check, indexed primary
  queries for `"PMC2597217" "Akt" "phosphorylation"` exposed the same Results and
  Methods. The local publication remains abstract-only.
- [PMID:19197339, full original PMC2658556](https://pmc.ncbi.nlm.nih.gov/articles/PMC2658556/):
  indexed full primary Results recovered with `"PMC2658556" "Akt"` describe PEBP4
  coimmunoprecipitation with transfected and endogenous Akt, increasing during
  myoblast differentiation (supplementary Fig. S8A). The paper distinguishes this
  positive association from an unsupported PEBP4 adaptor explanation of RAF
  inhibition. The local publication remains abstract-only.
- [PMID:35512704, full original PMC9597701](https://pmc.ncbi.nlm.nih.gov/articles/PMC9597701/):
  indexed Results and Methods show a WT-versus-mutant BRET screen, including AKT1
  E17K, and follow-up experiments in MCF7 cells. The exact homotypic pair and its
  WT-versus-mutant status remain to be checked before adjudicating the separate
  identical-protein-binding row.
- [PMID:36126419, official PubMed](https://pubmed.ncbi.nlm.nih.gov/36126419/):
  identity, abstract and figure captions are externally accessible. The abstract
  reports an MPST–AKT interaction in an intestinal inflammation study, despite
  the local metadata-only cache. That file has not been hand-filled or treated
  as a recovered primary-text cache.

The existing CMA NEW proposal also requires reconciliation with the current
nonredundancy rule. The [live GO parent page](https://amigo.geneontology.org/amigo/term/GO%3A0010507?relation=isa_partof)
places GO:1904715 beneath the already annotated GO:0010507. PMID:26118642 supplies
positive evidence for lysosomal Akt control of CMA; the final decision must
preserve that biology while avoiding a redundant new assertion. No CMA action
has been changed in this initial pass.


## Completed source audit — 2026-09-27

This completed pass supersedes the initial-pass action statements above and the
older June proposal to retain a CMA NEW row. All 445 seeded assertions, including
their evidence codes, reference identifiers, qualifiers and isoform flags, are
preserved. The one previous NEW descendant proposal is withdrawn, leaving 445
reviewed rows: 204 ACCEPT, 112 KEEP_AS_NON_CORE, 82 REMOVE, 31 UNDECIDED,
15 MODIFY and one MARK_AS_OVER_ANNOTATED. No new assertions were added.
All 233 original reference id/title pairs remain in order; 17 already-cached
donor studies were added, giving 250 assessed references. The two core entries
now cite primary kinetic/activation and lipid-binding evidence instead of a
generated report. The genuine Falcon file and all machine sources are unchanged.

The annotation-reviewer consultation was performed in this lane. A separate
read-only peer consultation independently checked the unusual molecular-function
assertions: Ser/Thr/Tyr kinase, kinase inhibition, self-association and nitric-oxide
synthase regulation. Its source checks and the owner's subsequent reads agree
with the final bounded judgments. The coordinator is independently reviewing the
stable biological draft before publication.

### Chemistry and meaningful regulatory activities

[PMID:16540465](https://pubmed.ncbi.nlm.nih.gov/16540465/) directly compares the
three AKT enzymes and identifies ordered ATP/peptide catalysis for AKT1. The
primary insulin/IGF1 experiments in PMID:8978681 test PKBalpha Thr308 and Ser473
mutants and support the central receptor-response mechanism. Phosphoinositide
binding and recruitment are supported by the original
[PMID:19203586 abstract](https://pubmed.ncbi.nlm.nih.gov/19203586/), the existing
PIP3/PI(3,4)P2 IDA assertions, and the immutable UniProt domain description.
The original Cell full text was blocked; no full lipid-overlay assay is claimed
as newly recovered from that paper.

The live [GO:0004712 definition](https://amigo.geneontology.org/amigo/term/GO%3A0004712)
requires phosphorylation of serine/threonine **and tyrosine**. Therefore the two
source-specific replacements by GO:0004674 are chemistry corrections, not a
simple move to a more specific descendant. The RGC-32 source PMID:19162005 tests
Ser45/Ser47 mutants, and the full ZNRF2 source PMID:22797923 maps PKBalpha-dependent
Ser19 by HPLC/Edman sequencing. Neither assay demonstrates target Tyr chemistry;
this does not assert that AKT1 can never show such chemistry in another context.
PMID:23431171 instead directly resolves MOZ Thr369, supporting replacement of
the source's serine-only assertion by Ser/Thr kinase activity.

The literal [GO:0030291 definition](https://amigo.geneontology.org/amigo/term/GO%3A0030291)
requires binding and reduced Ser/Thr kinase activity; it does not impose a
noncatalytic or stoichiometric mechanism. The rat Akt1 accession P47196 carries
IPI evidence to GSK3alpha/beta from PMID:8524413. That primary abstract identifies
PKB as the GSK3-inactivating kinase, and PMID:9373175 directly reports PKBalpha,
GSK3beta Ser9, Ser9A resistance and phosphatase reversal. The full binding assay
was not independently recovered, but the traced donor and conserved human
chemistry support transfer. A pre-existing rat hypothesis report adds a
noncatalytic restriction absent from the GO definition; that inference is not
independent biological contradiction. Rat files were not edited in this scope.

Similarly, [GO:0030235](https://amigo.geneontology.org/amigo/term/GO%3A0030235)
does not exclude catalytic NOS regulation. PMID:10376603 establishes Akt-dependent
eNOS Ser1177 phosphorylation and activation. These regulatory activities are
retained as contextual, non-core functions. Self-association is also retained
with PMID:7891724 and the TCL1 study PMID:10983986; the latter's TCL1 trimers are
not interpreted as an Akt trimer or proof of obligate native Akt dimers.

### Full primary experiments and compartment boundaries

The following primary routes were read in addition to the first-pass sources.
Indexed PMC queries recovered Results/Methods when direct pages intermittently
returned a browser challenge. They are evidence-access routes, not fabricated
machine caches. Local flags follow actual cache metadata: abstract-only remains
`full_text_unavailable: true`, whereas a partial retrieved body remains false
with extraction limits stated in the reference assessment.

- [PMID:19162005, PMC2699899](https://pmc.ncbi.nlm.nih.gov/articles/PMC2699899/),
  cached full Methods/Results and Figure 5: purified Akt phosphorylates human
  RGC-32 Ser45/Ser47. C5b-9 was assembled from terminal complement components.
  The [GO:0002430 definition](https://amigo.geneontology.org/amigo/term/GO%3A0002430)
  instead specifies complement-component binding to a receptor. The single OVER
  judgment concerns this receptor-specific subtype, not the positive C5b-9/Akt
  signaling result.
- [PMID:21954288, PMC3752779](https://pmc.ncbi.nlm.nih.gov/articles/PMC3752779/),
  cached full experiments: Akt1/2 phosphorylate PERK Thr799, and the mutant and
  stress experiments support negative PERK regulation.
- [PMID:23684622, PMC3690479](https://pmc.ncbi.nlm.nih.gov/articles/PMC3690479/),
  cached full kinase and SIN1 Thr86 mutant/rescue experiments: Akt performs a
  positive-feedback phosphorylation step in mTORC2 regulation.
- [PMID:26844834, PMC4743039](https://pmc.ncbi.nlm.nih.gov/articles/PMC4743039/),
  cached full mouse nucleus-accumbens experiments: synaptoneurosomal Akt signaling
  and dominant-negative Akt effects on Rap1b-associated spine morphology provide
  the bounded synaptic transfer context.
- [PMID:30504268, PMC6331721](https://pmc.ncbi.nlm.nih.gov/articles/PMC6331721/):
  indexed query `"Akt-mediated phosphorylation of MICU1" "rapamycin"` recovered
  Results/Figure 2. Rapamycin-responsive Akt accumulation, protease protection,
  and MICU1 Ser124 processing experiments support a predominantly mitochondrial
  intermembrane-space pool. Broad mitochondrial donor rows retain their original
  resolution rather than being upgraded automatically.
- [PMID:16792529, PMC1570162](https://pmc.ncbi.nlm.nih.gov/articles/PMC1570162/):
  query `"PMC1570162" "Akt" "co-localized"` recovered Results/Figure 6 using
  ProF-mediated recruitment of engineered m/p-Akt1 to vesicles in COS7 cells. This is a real
  experimental location, with the construct limit retained.
- [PMID:19126672, PMC2724728](https://pmc.ncbi.nlm.nih.gov/articles/PMC2724728/):
  query `"Spontaneous phosphoinositide" "AktPH"` recovered NIH3T3 TIRF experiments
  with an EGFP-AktPH lipid reporter. Exact full-length AKT1 cortex/lamellipodium
  and migration assertions remain unresolved rather than being declared false.
- [PMID:21177249, PMC3044975](https://pmc.ncbi.nlm.nih.gov/articles/PMC3044975/):
  queries `"A new cytosolic pathway" PINK1 "Akt" rictor interaction` and
  `"PMC3044975" "Akt" "migration" "inhibitor"` recovered Figures 2, 3, 5 and 6.
  Akt is the mTORC2 kinase substrate, with survival/migration pathway experiments;
  PINK1-rictor/SIN1 coimmunoprecipitation does not settle a separate Akt physical
  pair without its actual assay.
- [PMID:22869525, PMC3457336](https://pmc.ncbi.nlm.nih.gov/articles/PMC3457336/):
  query `"PMC3457336" "MC3T3" "RESULTS"` recovers relevant preosteoblast PTEN/Akt
  experiments, but the precise differentiation endpoint remains unresolved.
- [PMID:40285646, PMC12279241](https://pmc.ncbi.nlm.nih.gov/articles/PMC12279241/):
  query `"PMC12279241" "AKT" "phosphorylation" "TMCO3"` recovered Results 2.4-2.7
  and Figures 4-6. TMCO3 binding promotes AKT membrane recruitment and PIP3 binding;
  this does not itself settle the separate AKT-positive-feedback assertion.
- PMID:29104511, cached full Figure 3C and Methods: anti-calmodulin
  coimmunoprecipitation detects Akt in HUVECs. This is positive association evidence,
  distinct from the W7 inhibitor experiments.
- PMID:19850054 and PMID:20011604, cached full primary vascular studies: retain
  source-specific proliferation/migration participation with pharmacology limits.
  In the former, the named compound is LY294002 despite being labeled an Akt
  inhibitor; it is not an AKT1-specific genetic perturbation.
- PMID:33505021, full cached primary Methods and electrophysiology: human AKT1,
  catalytic mutants and recombinant protein establish kinase-independent
  TMEM175 activation. This meaningful secondary molecular function remains
  NON_CORE and is not recast as phosphorylation of the channel.
- [PMID:21711983, PMC3244494](https://pmc.ncbi.nlm.nih.gov/articles/PMC3244494/):
  the indexed full review now exposes beta-arrestin2/PP2A/Akt and neurotransmitter
  signaling discussion. The exact Akt1-specific excitatory-potential experiment
  remains unresolved; recovery of review prose does not settle every NAS detail.

### PAINT, GO-CAM and nonredundancy

The member index places P31749 in PTHR24356:SF171. The conserved PAINT assertions
were inspected at PTN000682363, PTN000683254 and PTN001219338, using PTN-only
structured source entities. Shared ancestral nodes can occur across AGC family
files; a target's appearance among experimental descendants is expected, not
circular. Donor count is not used as an evidence-strength proxy.

All 29 AKT1 activity records in the cached GO-CAM index were read with their
source-bearing enabled-by, location, process, input and causal edges. They retain
AKT1 as a kinase, with downstream substrates and regulators modeled separately.
Two edge-specific limits are material: cGAS model `62b4ffe300003321` cites
PMID:12172553 on the process edge but PMID:26440888 on substrate/negative-regulation
edges; `65692e7e00001822` combines an RNF115 input with review-derived postsynaptic
potential context. Such combinations prompt source-specific uncertainty rather
than invented assay details. The MICU1 and PERK models preserve their actual MGI
inference routes, independently corroborated by the primary experiments above.

The existing negative-autophagy term covers the earlier proposed CMA child term.
The full PMID:26118642 experiments, including isolated lysosomal Akt/GFAP kinase
assays and LAMP2A complex dynamics, remain positive findings. Withdrawal of the
redundant NEW proposal does not reject this mechanism or add a new process on
necessity evidence alone.

### Corrections and source-access gates

- [PMID:36423325, HBx corrigendum](https://doi.org/10.1111/febs.16684): the original
  publisher corrects a duplicated colony-formation image in Figure 5A for two
  HBxS31A conditions and states the conclusions are unchanged.
- [PMID:35267011, ZNRF2 publisher note](https://discovery.dundee.ac.uk/en/publications/publishers-note-znrf2-is-released-from-membranes-by-growth-factor/):
  duplicated GST control blots in Figure 2B lack the original LICOR data; alternate
  controls from the experiment were oversaturated. The separate Ser19 mapping is
  retained with a DISPUTED reference-integrity caveat, not described as retracted.
- [PMID:33790472, TMEM175 author correction](https://www.nature.com/articles/s41586-021-03438-x.pdf):
  Figure 3b lane labels for K336A and T338D were reversed and corrected.
- [Niban disclosure notice](https://pmc.ncbi.nlm.nih.gov/articles/PMC4198044/),
  DOI:10.15252/embr.201439354: indexed full notice discloses an omitted financial
  interest in the antibody supplier. It does not report retraction or replacement
  of the catalytic experiment in PMID:22510990.

Normal `fetch-pmid` attempts for all three correction PMIDs failed with DNS
`nodename nor servname provided`. PMID:36126419 exists only as a 436-byte metadata
placeholder: a normal fetch skipped that existing file, and a supported
temporary-output fetch failed with the same DNS error. No cache was hand-edited
or manufactured. Fifty-four of 78 Reactome sources also lack local machine
caches, despite the verified external event content described above. These
access gates keep status DRAFT; validation success alone does not waive them.

Targeted validation passed with seven nonblocking warnings: six intentional
source-specific action differences (plasma membrane, cytosol, serine kinase,
cGAS regulation, glycogen biosynthesis and glucose import), and the informational
warning that no annotation uses the generated Falcon report as primary support.
This is appropriate: the generated report is retained as background, while
source-specific primary evidence supports the decisions. Final source-preservation,
history validation and rendering are recorded in the handoff manifest.


## 2026-09-27 verified source-recovery follow-up

This entry supersedes the earlier missing-Reactome and metadata-only source
statements. The canonical review, notes, HTML, machine files and prior history
were byte-checked against published PR #3242 head
`25067bbc3c0641b650867b75f3d2dac333b84431` before editing.
All 445 source assertions and actions, 250 reference identities, two cores and
existing history are preserved. Only the MPST-source evidence prose/availability
and its reference assessment change; no new annotation is proposed.

All 54 previously absent Reactome records now have normal-fetch caches. Their
stable IDs, nonempty summaries and exact bytes match the verified source2 import
receipt. The summaries corroborate the event-level interpretations already read
on the live Reactome pages; they are not substitutes for the fuller participant
and compartment records previously inspected. In particular, AKT is the substrate
in its activating/deactivating reactions, many E17K substrate events explicitly
remain predictions, and the NR4A1 event retains its disputed physiological-kinase
assignment. The R-HSA-9860759 residue-name inconsistency remains documented in its
reference assessment; the machine title and cached record are preserved.

The normal-fetch candidate for [PMID:36126419](https://pubmed.ncbi.nlm.nih.gov/36126419/)
was checked against the [original PMC article](https://pmc.ncbi.nlm.nih.gov/articles/PMC9486620/):
PMID, title, author list, PMCID PMC9486620 and DOI 10.1016/j.redox.2022.102469
match. The old canonical file was a 436-byte metadata placeholder (Git blob
`36895e1bd940255b25be03e16fdaa6e81b2744c3`). It is replaced by the exact,
unaltered 166524-byte normal-fetch candidate with SHA256
`ae05feaf20dcf1275ccc9f87119e4337c7505ecb0d73830dc5020bcec06d8292`.
No cache text or metadata was hand-edited.

The recovered Methods 2.13 describe tagged MPST/AKT transfection and
immunoprecipitation in HEK293T cells, plus an assay of recombinant His-MPST and
GST-AKT. Results 3.8/Figure 9 provide the positive interaction and C-terminal
AKT deletion-mapping results. The text generally names AKT, without accession
information resolving every construct or endogenous isoform. The interaction is
retained as evidence while its generic protein-binding annotation remains REMOVE
under the uninformative-term policy. It is not a false-interaction judgment.

A newly visible internal wording inconsistency is retained explicitly. The
abstract says MPST reduces AKT phosphorylation, whereas Results/Figure 8 report
reduced Ser473 phosphorylation after MPST loss and Results 3.8 describe MPST
sustaining AKT phosphorylation. This does not negate the independent Figure 9
interaction experiments. No kinase-inhibitor or other new molecular function is
inferred from that contradictory abstract sentence. The XML extraction repeats
some sections, but includes actual Methods, Results and figure captions; both
review availability flags for this source are now false.

The normal output came from Actions source run 36289953066 at head
`fecff1befb769b1753300fa1bc2e3442813e9dd2`, transport run 36292331362,
artifact 10923045788. Verified artifact SHA256:
`0876942c72b2e537e858e8af7cd3c79d34b97c2169490e3d883c6f00884e2965`.
The source2 import receipt records all per-file hashes; the MPST file was held
as a candidate until this identity/content review. GitHub subtree queries confirm
that all 54 Reactome paths are absent from the published baseline and the old
MPST metadata blob is exactly the one replaced.

The three required correction records PMID:33790472, PMID:35267011 and
PMID:36423325 remain pending the coordinated source3 recovery. Their citations
and existing assessments remain intact. This is partial cache closure; the review
remains DRAFT. Final validation, quote/source preservation and rendering results
are recorded in the follow-up manifest.

Follow-up `just validate human AKT1` passed with the same seven explained
source-specific/action and provider-quotation advisories. A separate check finds
94/94 ordinary supporting-text occurrences in their exact local sources using
case-sensitive whitespace-only normalization; no full-text escape fields or
missing quoted sources are present. The notes-inclusive correction-cache gate
remains separate from this successful validator result.
