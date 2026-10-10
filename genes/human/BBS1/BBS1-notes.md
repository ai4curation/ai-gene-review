# BBS1 (Q8NFJ9) research notes

Gene: BBS1 / "BBSome complex member BBS1" / Bardet-Biedl syndrome 1 protein. Human, HGNC:966. 593 aa, chromosome 11.

## Summary of function

BBS1 is a core subunit of the **BBSome** (GO:0034464), an octameric, coat-like protein complex
(BBS1, BBS2, BBS4, BBS5, BBS7, BBS8/TTC8, BBS9, BBIP1/BBIP10). The BBSome is structurally related
to COPI/COPII/clathrin coats and functions as a cargo adaptor that traffics specific transmembrane
proteins (notably ciliary GPCRs and Hedgehog-pathway components) into and out of the primary cilium
by coupling them to intraflagellar transport (IFT).

- BBSome is a membrane-trafficking coat that sorts membrane proteins to primary cilia
  [PMID:20603001 "the BBSome constitutes a coat complex that sorts membrane proteins to primary cilia"].
- The BBSome is the major effector of the Arf-like GTPase **ARL6/BBS3**; GTP-bound ARL6 recruits the
  BBSome to the ciliary membrane and the two colocalize at ciliary punctae in an interdependent manner
  [PMID:20603001 "The BBSome is the major effector of the Arf-like GTPase Arl6/BBS3, and the BBSome
  and GTP-bound Arl6 colocalize at ciliary punctae in an interdependent manner"].
- Cargo recognition: the ciliary targeting signal of somatostatin receptor 3 (SSTR3) is directly
  recognized by the BBSome to mediate ciliary targeting
  [PMID:20603001 "the ciliary targeting signal of somatostatin receptor 3 needs to be directly
  recognized by the BBSome in order to mediate targeting of membrane proteins to cilia"].

### BBS1 as the β-propeller / ARL6-binding subunit
- Structural work shows BBS1 contains a 7-bladed β-propeller that binds ARL6/BBS3-GTP, providing the
  membrane-targeting interface of the BBSome [PMID:25402481 "Structural basis for membrane targeting
  of the BBSome by ARL6"]. The IntAct annotation records direct BBS1–ARL6 (Q9H0F7) interaction.
  Disease-causing BBS1 M390R maps to this propeller and weakens ARL6 binding (literature).

### BBSome assembly and Rab8/ciliary membrane biogenesis
- BBS1 was identified as part of the original 7-subunit BBSome core that, together with Rab8 GEF
  (RAB3IP/Rabin8), promotes ciliary membrane biogenesis [PMID:17574030 "A core complex of BBS proteins
  cooperates with the GTPase Rab8 to promote ciliary membrane biogenesis"; UniProt: "INTERACTION WITH
  RAB3IP"]. The BBSome associates with the ciliary membrane and binds RAB3IP/Rabin8, the GEF for Rab8;
  Rab8-GTP then promotes docking/fusion of carrier vesicles at the ciliary base (UniProt FUNCTION).
- BBSome assembly is chaperonin-assisted: BBS6/BBS10/BBS12 + CCT/TRiC mediate assembly of the BBSome
  [PMID:20080638 "BBS6, BBS10, and BBS12 form a complex with CCT/TRiC family chaperonins and mediate
  BBSome assembly"; BBS1 IDA part_of BBSome from this paper]. Sequential, intrinsic PPI-driven assembly
  with the BBS7–BBS2 and chaperonin intermediates [PMID:22500027].

### Cargo / signaling roles
- **Hedgehog (SHH):** Loss of BBS genes causes accumulation of Smoothened (SMO) and Patched1 (PTCH1) in
  cilia and a decreased Shh response; BBS genes genetically interact with the IFT pathway to modulate
  SHH-related developmental phenotypes [PMID:22228099 "the loss of BBS genes in mice result in
  accumulation of Smoothened and Patched 1 in cilia and have a decreased Shh response"]. NOTE: This is a
  **genetic interaction / cilia-accumulation** study, not a direct binding assay; the "patched binding"
  and "smoothened binding" IPI annotations from this paper are over-interpretations of genetic/trafficking
  data (BBSome regulates SMO/PTCH1 ciliary levels). The IBA propagation of these MF terms is therefore weak.
- **Leptin receptor (LEPR):** BBS proteins are required for leptin receptor signaling; BBS1 interacts with
  LEPR and Bbs loss causes leptin resistance (relevant to obesity) [PMID:19150989; IntAct BBS1–Lepr
  (mouse, P48356)]. The "Golgi to plasma membrane protein transport" IMP from this paper reflects defective
  LEPR surface trafficking.
- **Polycystin-1 (PKD1/PC1):** BBS1 (and BBS3) regulate ciliary trafficking of PC1; PC1 interacts with a
  subset of BBSome subunits (BBS1/4/5/8) and only BBS1 depletion/mutation impairs PC1 ciliary trafficking
  [PMID:24939912 "the ADPKD protein polycystin-1 (PC1) interacts with BBS1, BBS4, BBS5 and BBS8... Only
  depletion or mutation of BBS1... impairs ciliary trafficking of PC1"]. Supports BBS1 as the principal
  cargo-recognition subunit.

### Regulation / interactions with NPHP/Cep290 module
- NPHP5 (IQCB1) and CEP290 regulate BBSome integrity, ciliary trafficking and cargo delivery
  [PMID:25552655; IntAct BBS1–IQCB1 Q15051]. BBSome physically/genetically interacts with CEP290 (via BBS4)
  and modifies CEP290-ciliopathy phenotypes [PMID:23943788]. BBS1 mutations modify phenotypic expression of
  CEP290-related ciliopathies — basis for the IMP "protein localization to cilium" annotation.

### Centrosome / centriolar satellites
- BBS proteins localize at/near the centrosome and centriolar satellites; BBS4 (with DISC1) recruits PCM1
  to the centrosome [PMID:18762586]. BBS1 IntAct interaction with PCM1 (Q15154) and centrosome IDA derive
  from this/related work. AZI1/CEP131 (centriolar satellite) interacts with BBS4 and regulates BBSome
  ciliary trafficking [PMID:24550735]. UniProt subcellular location: cilium membrane; cytoplasm;
  centrosome; centriolar satellite. Note the original BBSome paper found the complex is **dispensable for
  centriolar satellite function** (UniProt FUNCTION), so centriolar-satellite localization is likely a
  pool/staging location rather than a core functional site.

### Transcriptional regulation (PMID:22302990)
- This paper foregrounds **BBS7** (which has a nuclear export signal and interacts with PcG protein RNF2);
  it argues "a similar role for other BBS proteins" in transcription. The BBS1 IPI "RNA polymerase II-specific
  DNA-binding transcription factor binding" to RNF2 (Q99496) is an over-extrapolation from BBS7 data to BBS1
  and is not a core BBS1 function. Keep as non-core / mark over-annotated.

## Disease
- Bardet-Biedl syndrome 1 (BBS1, MIM:209900): pigmentary retinopathy, obesity, polydactyly, hypogenitalism,
  renal malformation, intellectual disability. BBS1 is the **most commonly mutated** BBS gene; M390R is the
  most common allele [PMID:12118255 founding paper]. Autosomal recessive; some forms show oligogenic/triallelic
  inheritance [PMID:16327777 CCDC28B modifier]. Retinal degeneration / photoreceptor maintenance defects
  [PMID:17980398].

## Interaction partners (IntAct, from GOA) — mostly BBSome subunits + cargo/regulators
- BBSome subunits: BBS2 (Q9BXC9), BBS4 (Q96RK4), BBS7 (Q8IWZ6), BBS9 (Q3SYG4). These IPI "protein binding"
  annotations simply re-establish complex membership.
- ARL6/BBS3 (Q9H0F7) — small GTPase, membrane-targeting (direct, structural).
- RAB3IP/Rabin8 (Q96QF0) — Rab8 GEF.
- Cargo/regulators: LEPR (P48356, mouse), PKD1 (Q8TAM2), IQCB1/NPHP5 (Q15051), PCM1 (Q15154).
- Possibly non-specific / interactome-screen hits: EEF1A1 (P68104), ALDOB (P05062), PARK7/DJ-1 (Q99497),
  DCTN1 (Q14203), CCDC28B (Q9BUN5). Several are from high-throughput interactome maps (PMID:27173435,
  29039417, 32814053, 33961781, 40205054) and the legacy "novel interaction partners" screen (PMID:18000879).

## Annotation review judgments (summary)
- CORE: BBSome (part_of, GO:0034464) — strongly supported, multiple IDA. ACCEPT.
- CORE: protein localization to cilium (GO:0061512) — BBSome cargo trafficking. ACCEPT (IMP/IBA).
- CORE: cilium / non-motile cilium assembly (GO:1905515 / GO:0060271) — ACCEPT IMP/IBA.
- CORE: small GTPase binding — not currently annotated as such but is the real MF (ARL6-GTP). The generic
  "protein binding" IPI annotations to ARL6 should ideally be MF small GTPase binding; propose new term.
- centrosome (GO:0005813), ciliary membrane (GO:0060170), cytosol (GO:0005829), cytoplasm (GO:0005737):
  ACCEPT as supported localizations (cilium membrane + cytoplasm + centrosome per UniProt).
- centriolar satellite (GO:0034451): KEEP_AS_NON_CORE (staging pool; complex dispensable for satellite fn).
- axoneme (GO:0005930) IBA: weakly supported — BBSome acts at ciliary membrane/base; KEEP_AS_NON_CORE.
- patched binding / smoothened binding (GO:0005113 / GO:0005119): over-annotated — derived from genetic /
  cilia-accumulation data, not direct binding. MARK_AS_OVER_ANNOTATED.
- RNA Pol II TF binding (GO:0061629): over-annotated, extrapolated from BBS7. MARK_AS_OVER_ANNOTATED.
- fat cell differentiation (GO:0045444), retina homeostasis (GO:0001895), photoreceptor cell maintenance
  (GO:0045494): downstream/physiological consequences of ciliary dysfunction; KEEP_AS_NON_CORE.
- regulation of cilium beat frequency involved in ciliary motility (GO:0060296) + motile cilium (GO:0031514):
  BBS1/BBSome act on NON-motile (primary/sensory) cilia; these motile-cilium terms are likely mis-propagated
  Ensembl IEA. MARK_AS_OVER_ANNOTATED / REMOVE candidates (IEA, not curator).
- Golgi to plasma membrane protein transport (GO:0043001) IMP: from LEPR surface-trafficking; KEEP_AS_NON_CORE.
- intracellular protein localization (GO:0008104) IEA ARBA: vague generalization of cargo trafficking; MODIFY
  to protein localization to cilium.
- signaling receptor binding (GO:0005102) IEA: defensible (BBSome binds GPCR cargo) but generic; KEEP_AS_NON_CORE.
- phosphoprotein binding (GO:0051219) IEA Ensembl: weakly supported; UNDECIDED/over-annotated.
- protein binding (GO:0005515) IPI ×many: uninformative per guidelines; the BBSome-subunit ones support
  complex membership; KEEP_AS_NON_CORE (avoid promoting "protein binding").
</content>

## 2026-09-30 — primary-evidence reassessment

Human BBS1 is Q8NFJ9, HGNC:966, NCBI Gene582. The 60 original source
assertions and all three alternative-product objects must be preserved.
Q8NFJ9-2 is named product3 (DPP3-BBS1) in the source; this is not a basis for
assigning every canonical BBS1 assay to that fusion product.

### ARL6 recruitment and receptor recognition

[PMID:25402481](https://pubmed.ncbi.nlm.nih.gov/25402481/) directly measures
binding between recombinant human BBS1 N-terminal domain and human ARL6,
with an affinity of approximately0.54 micromolar in the reported assay.
The crystal complex is algal, whereas the human biochemical experiments
are separate. The human BBS1 domain was produced in High Five cells and
ARL6 in E. coli. A one-residue construct-boundary difference between the
Results and Methods is not evidence for natural isoform specificity.
Selected affinity Results and the purification, ITC, pulldown and
cell-assay Methods were read. The first core therefore uses small GTPase
binding; it does not give BBS1 ARL6's catalytic activity.

[PMID:20603001](https://pubmed.ncbi.nlm.nih.gov/20603001/) establishes the
BBSome as an ARL6-GTP effector. Bovine retinal BBSome purification, human
RPE-cell localization and individual BBS1-domain experiments are distinct
parts of the evidence. Selected Results and main Methods through the
purification/liposome assays were inspected; some pulldown procedures
refer to supplementary methods that were not fully read. Complex-level
cargo recognition is not automatically assigned to isolated BBS1.

The old review dismissed four Smoothened/Patched binding annotations as
genetic or localization evidence only. The actual full-text Results,
Figures2–3 captions and Methods in
[PMID:22228099](https://pubmed.ncbi.nlm.nih.gov/22228099/) include human
tagged BBS constructs in293T cells, reciprocal immunoprecipitation and
receptor-tail mapping. The BBS1-associated segments include Smoothened's
cytoplasmic tail and Patched1's C-terminal region. The binding observations
are supported even though the abstract foregrounds mouse genetics and
Hedgehog signaling. They do not establish purified binary affinities. One receptor
binding core can represent this shared cargo-recognition role.

### Contextual interactions and donor evidence

[PMID:22302990](https://pubmed.ncbi.nlm.nih.gov/22302990/) has an
abstract-only local cache. Separately indexed original Results and
Figure3C explicitly include tagged BBS1 among proteins co-precipitating
RNF2. The BBS7 bait and endogenous-IP experiments are not relabeled as
BBS1 experiments. RNF2 is a ubiquitin ligase; binding that partner is
better represented by ubiquitin protein ligase binding than by binding
a sequence-specific RNA-polymerase-II transcription factor. Changes in
RNF2 abundance after BBS1 depletion do not make BBS1 a protease.

The mouse Bbs1 donor annotation supports the contextual motile-cilium and
ciliary-beat roles in
[PMID:18299575](https://pubmed.ncbi.nlm.nih.gov/18299575/). The available
cache contains an abstract and Discussion but omits the Results and
supplementary Methods despite its full-text flag. The independent
consultation inspected indexed Results/Figure6A and the official MGI
donor mapping. Direct human localization in that paper concerns BBS2
and BBS4 and must not be transferred to BBS1. A primary-cilium-only
rationale cannot dismiss the mouse Bbs1 airway findings.

[PMID:21471969](https://pubmed.ncbi.nlm.nih.gov/21471969/) provides
context for the phosphoprotein-binding transfer. Indexed original
Results, Figure1 and Methods summary distinguish mouse DISC1 S710
phosphodead/phosphomimetic constructs and phosphorylation-dependent
BBS1 association in HT22 cells. Human DISC1 S713 biochemical experiments
are a separate assay. This supports a contextual interaction and
centrosomal recruitment in mouse cortical development; BBS1 is not
the kinase. The full supplementary files were not read. Its normal
cache fetch failed once with DNS errors; the recovered normal record
is now bound to this proposal.

PMID:17980398 describes retinal imaging in human BBS1/BBS10 patients,
not a mouse experiment. An experimental annotation must not be
rejected from that abstract alone. PMID:24939912 distinguishes ciliary
PC1 targeting from plasma-membrane targeting and cilium length.
PMID:32814053 is the Haenig neurodegenerative interactome; findings
from a separate BBS1 assembly paper must not be attributed to it.

### Curation boundaries

Supported generic interactions are retained as non-core unless a
specific molecular activity is established. PAINT assertions are
not judged by donor count or by the source paper's title. No new
biological-process annotation is proposed from an isolated knockout
phenotype. Cilium assembly and physiological outcomes are retained
as context where justified; they do not require additional duplicate
core functions.

The standard Falcon invocation with perplexity-lite fallback stopped
before either provider started because the pinned client dependency
was unavailable offline. The standard publication command found all
23 original PMIDs already cached. No provider report or downloaded
source content was authored manually. Final decisions, source binding,
history and validation will be recorded after integration.

This reassessment supersedes earlier journal statements dismissing SMO/PTCH and RNF2 interactions or presuming absence of a motile-cilium role. All 60 original assertions remain:31 ACCEPT,23 KEEP_AS_NON_CORE and six MODIFY; no NEW assertion is added. Three products and two molecular cores are retained. The LEPR generic-binding row is refined to signaling receptor binding with the annotation consultant’s specific concurrence.

### Focused application checks

The exact independently reviewed proposal was applied on 2026-09-30. Focused validation passed with 14 advisories, all for supported generic protein-binding annotations retained as non-core under the supplied ActionEnum. These recommendations do not establish that the interactions are incorrect. Rendering passed; all 60 source objects and three products remain unchanged. No repository-wide validation pass is claimed. The new Codex EDIT history records this reassessment.


## 2026-09-30 — source completeness correction before publication

The earlier 60-row audit covered the legacy review groups, not every distinct WITH/FROM tuple. A normal offline seed-goa projection with title fetching disabled recovered 23 additional partner-specific rows and backfilled 43 supporting-entity lists. The immutable GOA contains 86 raw lines representing 83 distinct source tuples; three repeated projected tuples are retained once. The review now contains all 83 distinct tuples: 31 ACCEPT, 46 KEEP_AS_NON_CORE and six MODIFY. All prior 60 judgments, three alternative products, two molecular cores and 35 references are preserved.

The added rows retain source-attributed interactions separately for BBSome subunits, RAB3IP isoforms, EEF1A1, PCM1 and PARK7. They do not inherit receptor-, RNF2- or ARL6-specific refinements. The RAB3IP isoforms identify partners, not BBS1 isoforms. Abstract-only sources and uninspected supplementary pair matrices remain explicitly limited; co-complex affinity purification is not treated as purified binary binding. The BioPlex 33961781 cache contains Introduction and Discussion despite its full-text flag. Generic binding remains non-core under the supplied ActionEnum. No new quotation or autonomous molecular activity is asserted.

This correction supersedes the earlier completeness claim while preserving that history and the unexecuted 60-row native packet. No branch, commit or PR was created from the superseded packet. Independent biological review accepted the 23 supplemental judgments and exact source projection before this application.

Focused validation after the source-completeness repair passed with 37 generic-binding non-core advisories, retained under the supplied ActionEnum (58b8c6). Rendering passed (f6d9e0), and the separate Codex EDIT history passed schema validation (a71a1e). Raw/source bytes remain unchanged; no repository-wide validation claim is made. The first history scaffold command used an ambiguous actor option and stopped before creation; the corrected actor-name command generated the new record normally.


## 2026-09-30 — first review feedback: evidence placement and prose

The 83 source annotations, their actions, partner identities, three alternative products and two core activities are unchanged. The description now names the eight BBSome subunits and makes the coat and receptor-recognition roles explicit. This does not add an autonomous GTPase, universal ciliogenesis or direct receptor-activation claim.

Short primary-source anchors now accompany the experimental PTCH1 and SMO rows, the LEPR refinement, contextual mouse motile-cilium and beat phenotypes, and phosphorylation-sensitive DISC1 association. The two receptor quotations were moved from the core to their experimental rows; the receptor core retains the source citation without repeating those quotations. The ARL6 core retains its human binding anchor. The current BBSome roster includes BBIP1, identified after the foundational seven-subunit study; that older complex-identification quotation is used only with its own source annotation.

The PMID:23943788 annotation remains accepted with explicit curator deference. Its complete available cache contains the abstract, Introduction and Discussion, but omits Results and Methods. That text foregrounds BBS4/CEP290 and does not expose the BBS1-specific assay. The new row anchor is clearly labeled corroboration from the independent PC1-trafficking study PMID:24939912. The separate source experiments are not conflated. Mouse DISC1 S710 and human S713, mouse airway phenotypes and human localization, and cell-lysate association versus purified binary binding remain distinct.

Repeated policy and audit boilerplate has been replaced by partner- and study-specific biological reasons. Detailed source access and supplementary-pair limits are retained in the corresponding reference reviews. All 37 generic binding rows remain KEEP_AS_NON_CORE under the supplied ActionEnum: the recorded associations are retained, but no additional informative molecular activity is established. No interaction is declared false merely because its label is broad. The exact Q8TAM2 partner in the PMID:24939912 generic interaction row is TTC8/BBS8. Its previous PC1-focused summary conflated the paper’s cargo experiments with the distinct GOA partner; the summary is corrected without changing the source object or action. PMID/DOI and figure-label spacing in authored prose is repaired.

The evidence check counts all quoted text across the proposed YAML and this new notes appendix, including repeated occurrences; each source remains within 25 words. Existing journal entries are preserved as historical text. No source cache, raw GOA, UniProt record or generated research file was changed. This temporary proposal has not been canonically applied or fully validated.


## 2026-10-09 — authority for the campaign binding policy

The [ClinGen project's curation instructions](https://github.com/ai4curation/ai-gene-review/blob/6b4b0fccc608746b8e6efefba54954f140da00cc/projects/CLINGEN_MENDELIAN.md#curation-instructions) record the user's explicit instruction to retain a supported, biologically correct generic protein-binding annotation as KEEP_AS_NON_CORE when no evidence-backed, more specific replacement is established. They require MODIFY for a supported refinement and UNDECIDED when the relevant evidence cannot be accessed or adjudicated. The instruction is specific to this campaign and takes precedence over the annotation-reviewer skill's general informational-exclusion recommendation.

This explicit project instruction is the authority for the retained generic interactions. It supersedes the earlier journal explanations based on the ActionEnum alone. The 2026-09-30 re-review on head 969a250d4 accepted the biological judgments and restored evidence anchors; its remaining request to remove all 37 non-core generic-binding rows applied the general policy. The project instruction resolves that policy question. The source-access limitations in the reference reviews remain in force: retention does not claim that an uninspected supplementary pair matrix was independently verified or turn a co-complex association into purified binary binding.

This clarification preserves all 83 annotation decisions (31 ACCEPT, 46 KEEP_AS_NON_CORE and six MODIFY), including the four evidence-backed refinements of generic-binding rows. The 37 generic-binding advisories are expected under the campaign instruction; their presence does not invalidate the supported retention decisions.
