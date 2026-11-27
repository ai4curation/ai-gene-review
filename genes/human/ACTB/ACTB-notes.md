# ACTB source and annotation audit

## 2026-09-26 — baseline and access record (audit in progress)

Human ACTB is cytoplasmic beta-actin, UniProt P60709, HGNC:132 and NCBI Gene 60. Identity and aliases were checked against [NCBI GTR](https://www.ncbi.nlm.nih.gov/gtr/genes/60/) and the HGNC-linked [NCBI/PubChem gene record](https://pubchem.ncbi.nlm.nih.gov/gene/60). Current-main baseline was `0efff18e63a816029f64fa64bea40bef0c68c320`; all seven top-level ACTB files matched GitHub's authoritative content blobs. Review blob: `fddca5a52a4d801096af110aabd4afc87df1d5c5`. Open-PR text searches for ACTB and its BRWS1/PS1TP5BP1 aliases returned no overlap. This is a bounded text-search check, not a claim to have inspected every open PR's file list.

The prior COMPLETE document contains **247 seeded annotation rows and one earlier NEW proposal**, 171 reference entries, 117 listed PMIDs, and four core-function entries. All 117 listed publications were already cached; the normal parallel `fetch-gene-pmids` run completed 117/117. A wider citation scan also finds PMID:29581253 and PMID:18765789 (both cached but absent from the reference list), and PMID:29925947 (missing cache). A normal `ai-gene-review fetch-pmid 29925947` attempt failed DNS. This legitimate existing citation must not be silently deleted to bypass the publication requirement; absent a successful supported fetch, publication remains draft.

A genuine default Falcon launch with a 1200-second timeout and Perplexity-lite fallback was attempted using supported per-process UV tool/cache directories. Both launches failed dependency resolution at `pypi.org` before research began. Output was directed to an isolated `/tmp/ACTB-research-2026-09-26/ACTB/` directory so the three existing genuine provider reports could not be overwritten. The launch exited unsuccessfully and produced no report. Existing Falcon, Cyberian and Perplexity-lite files remain immutable background sources, not substitutes for primary evidence.

No direct P60709/ACTB entry was found in the current `gocams/index.tsv`. This is not evidence that actin lacks a process. All 247 source records, including original evidence/reference fields, will be preserved. The earlier broad ATP-dependent-activity NEW proposal requires reassessment because it duplicates existing ATP hydrolysis coverage.

## Primary-source recovery and issues under adjudication

- **PMID:25255767**: [the original Wiley article](https://febs.onlinelibrary.wiley.com/doi/10.1111/febs.13068) was read through its Results and figures using the public indexed full article. The local cache remains abstract-only. Recombinant human WT and variant beta-actins were made in Sf9 cells; the authors explicitly report 5–15% endogenous insect actin in preparations. Figure 4 separates intrinsic filament ATP turnover from Figure 6's activation of nonmuscle myosin-2A ATPase. WT filament ATP turnover was 2.1 ± 0.3 per hour; Figure 5 measures profilin-II binding. These are specific positive observations supporting intrinsic ATPase activity and functional interactions, without conflating the two ATPases. Brief external Results excerpt: “wt-β-actin, which showed a hydrolysis rate of 2.1 ± 0.3 h−1” (typographic superscript rendered as h−1).
- **PMID:18341992**: [PubMed](https://pubmed.ncbi.nlm.nih.gov/18341992/) and cached abstract identify photoactivatable GFP–beta-actin in rat CA1 hippocampal slices, with distinct dynamic and stable pools supporting spine shape and plasticity. This directly favors preserving postsynaptic structural specificity; a neuron-specific function is not invalid merely because ACTB also functions elsewhere. Full methods/construct details are still being sought.
- **PMID:17340523**: [PubMed](https://pubmed.ncbi.nlm.nih.gov/17340523/) independently confirms the cached paper is a 1985 Fumaria alkaloid separation study. It does not support the existing NAS transcription-regulation assertion. The source identifier will remain unchanged; the intended ComplexPortal citation has not been established and no replacement identifier is being guessed.
- **PMID:39321809**: the cached primary abstract specifically says luminal actin is integral to non-activated gamma-TuRC and is released during CDK5RAP2 activation. Nuclear/cytoplasmic actin is not itself a tubulin polymerase. The assembly/scaffold role and the source's activation-state qualification must be retained when interpreting microtubule-nucleation annotations.
- **PMID:16217013**: cached full text identifies actin in the purified K562 LCR-associated remodeling complex by LC-MS/MS of the 45-kDa band. It assigns sequence-specific DNA recognition to hnRNP C1/C2. Complex membership and chromatin remodeling therefore do not, by themselves, establish that isolated ACTB directly binds nucleosomal DNA.

The remaining annotation/source groups are still under review; this journal is not a final sign-off.

## Completed source adjudication

All **247 seeded annotations** have been reviewed; source terms, evidence codes, original references and any source flags remain identical to the baseline. The prior extra NEW `GO:0140657 ATP-dependent activity` proposal was withdrawn: it merely mirrored the former core and added no useful coverage beyond the existing ATP-hydrolysis assertion. No NEW annotation was introduced. Final actions are **108 ACCEPT, 63 KEEP_AS_NON_CORE, 5 MODIFY, 48 REMOVE and 23 UNDECIDED**. The five refinements concern hydrolase→ATP hydrolysis, CaMKII→protein kinase binding, NOS3→nitric-oxide synthase binding, MAL→transcription coregulator binding and myosin binding. Duplicate specific terms supported by distinct original sources are retained.

The three core functions are filament-based structural work, intrinsic ATP hydrolysis, and a **contribution to SWI/SNF chromatin remodeling**. The last uses `contributes_to_molecular_function: GO:0140658`, with SWI/SNF as `in_complex`; it does not assign the SMARCA2/SMARCA4 motor active site to ACTB. NuA4, dynactin and gamma-TuRC memberships remain reviewed separately. The former gamma-TuRC core used generic protein binding and an unverified quotation, so it was not retained as a separate molecular activity.

### Primary evidence and source distinctions

- **PMID:22855531**, cached full article, Results and Figures 1–11: human SK-CO15 and Caco-2 BBE experiments distinguish beta- and gamma-actin with isoform-specific staining, RNA interference and peptides. Beta-actin supports adherens-junction assembly and epithelial polarity. At the later calcium-repletion time point it colocalizes with ZO-1 as well as adherens-junction markers; a different steady-state knockout phenotype for gamma-actin does not refute beta-actin tight-junction localization. Both isoforms affect transepithelial resistance and dextran passage. Structural control of the junctional barrier supports the existing contextual transepithelial-transport regulation term; ACTB is not being treated as a tracer transporter.
- **PMID:19008859**, cached full Results/Methods: MAL RPEL cell pull-downs use **human FLAG-beta-actin** expressed in NIH3T3 cells. The purified crystallographic actin is rabbit skeletal actin, a separate preparation. The target-specific cell experiment supports the useful transcription-coregulator-binding refinement. Verbatim result: “RPEL1MAL and RPEL2MAL recovered exogenous wild-type β-actin and endogenous β-actin efficiently from total cell lysates”.
- **PMID:29581253**, cached full primary article and Figure 4: biochemical preparations are cytoplasmic **beta/gamma-actin mixtures** from human HAP1 control and NAA80-deficient cells. They demonstrate changes in filament elongation and depolymerization after acetylation loss. They are not pure-beta kinetic measurements, and NAA80 performs the acetyl-transfer reaction.
- **PMID:27840001**, cached abstract, independently traced through [SynGO annotation 409](https://www.syngoportal.org/annotation_409.html): mouse beta/gamma-actin knockouts were tested by synaptic capacitance/fission-pore measurements, vesicle imaging and electron microscopy. Polymerized actin supplies force for endocytic pit formation. The mouse Actb P60710/ENSMUSP00000098066 neuronal transfers therefore represent structural participation, not just an indirect knockout phenotype. The record identifies calyx and hippocampal synaptic contexts. The full source remains unavailable locally.
- **PMID:9845365**, [live PubMed primary abstract](https://pubmed.ncbi.nlm.nih.gov/9845365/): independently checked by the owner and peer consultant. Purification and peptide sequencing identify beta-actin and BAF53 in BAF; their contribution to maximal BRG1 ATPase and chromatin/matrix association is directly reported. Short excerpt: “beta-actin and BAF53 are required for maximal ATPase activity of BRG1”. PMID:12045110 is a later review, not this experiment. A normal retrieval attempt created no cache; subsequent reference validation also reports that it could not fetch the record. No specific diagnostic from the first fetch was captured. This is a second explicit cache gate.
- **PMID:29925947** was already cited in the baseline nucleus review and UniProt. UniProt maps the identifier to DOI `10.1038/s41586-018-0237-5`; the [original Nature article](https://www.nature.com/articles/s41586-018-0237-5) confirms the title and abstract. It studies Xenopus extracts and mammalian cells, showing nuclear actin/ARP2/3 recruitment and actin-dependent movement of repair domains. This supports the existing nuclear context; no new repair-process assertion was added. The normal cache fetch failed DNS and the missing source remains an explicit draft gate.
- **PMID:21423176**, cached Methods: purified HFF-1 focal adhesions were assessed by actin immunoblot; actin and fibronectin were then immunodepleted before MudPIT. These stages must not be conflated when assessing the HDA localization.
- **PMID:24415753**, cached body: PDI associates with beta-actin in MEG-01 cells, including a disulfide-linked complex and lamellipodial localization. The complex CC is valid at the source resolution. The generic MF is uninformative, and ACTB is not assigned PDI's enzyme chemistry.
- **PMID:11687588**, cached source: NDHII/DHX9-associated nuclear actin and hnRNP-C complexes support nuclear and protein-complex locations. Complex membership is not an RNA-helicase assignment to actin.
- **PMID:19190083** and **PMID:21362503**, cached full relevant Results/Discussion: actin/beta-actin is explicitly reported in characterized extracellular-vesicle preparations. These contextual detections are retained. Other extracellular proteomic rows remain UNDECIDED where the target identification table or preparation evidence was not recovered; they are not called contamination merely because ACTB is abundant.
- **PMID:23382103** has a positive `full_text_available` flag but only a partial recovered body. The exact HMP platelet-aggregation evidence was not resolved; the original annotation remains UNDECIDED rather than being rejected as an expression-only effect.
- **PMID:22926577** supplies adult substantia-nigra expression/proteomic context in the abstract. Without the underlying developmental evidence, the developmental HEP row remains UNDECIDED; this is not a claim that the curator used the wrong tissue or developmental stage.

### Nuclear source consultation

The independent annotation-reviewer consultant read rows 77–120 and the relevant complex sources. The owner separately read the cached abstracts/bodies and incorporated the following bounded conclusions:

- The 45 cached Reactome event summaries were read. Their compartment annotations are retained at source resolution. The SWI/SNF assembly events `R-HSA-9933236`, `R-HSA-9933237` and `R-HSA-9933238` explicitly place the ACTB–ACTL6 dimer between the catalytic and core modules. This is positive structural work. The cytosol events include both soluble and filamentous actin; the membrane events do not transfer dynamin GTPase, HSPA ATPase or kinase chemistry to ACTB.
- **PMID:10078207** reconstitutes a minimal BRG1/BRM remodeling system without directly assaying ACTB. That is neither proof that ACTB is the motor nor evidence against its structural contribution to the native complex.
- **PMID:12368262**, [PMC187451](https://pmc.ncbi.nlm.nih.gov/articles/PMC187451/), externally indexed Results and Figure 3A: beta-actin is detected by Western blot in purified mouse-brain and HeLa complexes. The bBAF CC is retained. The paper's proposed developmental model is distinguished from that solid membership evidence, and the exact positive-differentiation row remains UNDECIDED.
- **PMID:27153538**, [PMC4887106](https://pmc.ncbi.nlm.nih.gov/articles/PMC4887106/), external indexed Results: TIP60/MBTD1 chromatin recruitment, transcription and repair reporters support contextual transcription/HR roles. The local cache lacks important Methods/Results/figures despite its full-text flag. The particular ACTB nucleosome and cell-cycle assertions remain unresolved. Nucleosome includes associated proteins, so ACTB is not rejected simply because it is not a histone.
- **PMID:12215535**, [PMC134043](https://pmc.ncbi.nlm.nih.gov/articles/PMC134043/), externally indexed Methods/Results: the remodeling preparation is **yeast SWI/SNF**, used with six purified human excision-repair factors. The title's human excision nuclease does not make this a human ACTB assay. The source-specific transfer remains UNDECIDED.
- **PMID:23698369** directly supports BAF-mediated TOP2A recruitment and decatenation, with a G2/M checkpoint delay and anaphase bridges. The precise metaphase/anaphase regulatory term is left unresolved. **PMID:25066234** supports PBAF-dependent silencing near DNA breaks and early repair; it does not settle the separate metaphase/anaphase claim.
- Contextual complex processes are retained when the source describes real complex work: GBAF proliferation in PC3 cells, naive stem-cell transcriptional maintenance, BAF-dependent CD4 silencing, MyoD-dependent promoter remodeling, Rb/SWI/SNF cyclin repression, H2AX-associated repair and PBAF-mediated local transcriptional silencing. Lack of an ACTB-only knockout does not erase structural-subunit participation. Partner-specific DNA recognition, kinase and histone-modifying activities remain assigned to the corresponding partners.
- **PMID:14966270**, [PMC350560](https://pmc.ncbi.nlm.nih.gov/articles/PMC350560/), cached partial body plus externally recovered article introduction, composition table and Discussion, establishes conserved NuA4 and discusses DNA-damage/apoptosis functions. The earlier primary **PMID:10966108** reports impaired repair and apoptotic competence with catalytically inactive TIP60 complexes. These support contextual complex roles, distinct from ACTB being the catalytic HAT.

### Ontology and propagation checks

The following definitions were checked live in GO/GO-consortium resources:

- [GO:0098973](https://zfin.org/GO:0098973) defines contribution to structural integrity of a postsynaptic actin cytoskeleton. The neuron-specific scope is positively supported, so it is retained as NON_CORE rather than generalized.
- [GO:0098974](https://www.informatics.jax.org/vocab/gene_ontology/GO%3A0098974) concerns assembly, arrangement and disassembly of postsynaptic actin filaments and associated proteins; it is not equivalent to generic regulation of filament length.
- [GO:0001221](https://www.informatics.jax.org/vocab/gene_ontology/GO%3A0001221) is transcription coregulator binding, fitting the MAL interaction. [GO:0017022](https://zfin.org/GO%3A0017022) is myosin binding, fitting the human beta-actin/myosin assay.
- [GO:0140658](https://amigo.geneontology.org/amigo/term/GO%3A0140658) is ATP-dependent chromatin remodeler activity; the core records **contribution**, not independent ACTB motor catalysis.
- [GO:0016586](https://www.ebi.ac.uk/QuickGO/term/GO:0016586) includes mammalian PBAF/RSC-type complexes. [GO:0035060](https://www.ebi.ac.uk/QuickGO/term/GO:0035060) specifically concerns the BRM-containing assembly; it is not a synonym for every BAF complex. The consultant verified their live definitions.
- [GO:0097433](https://flybase.org/cgi-bin/cvreport.pl?id=GO%3A0097433) is an electron-dense body which may contain granules. It is not restricted to smooth muscle. The chicken P60706 donor was traced, but the source experiment was not resolved.

PAINT source blocks contain only the verified ancestral PTN nodes, with source-specific comments. Target self-evidence among descendants is legitimate, not circular. The dynactin ISO donor is **ComplexPortal:CPX-26390** for both complex membership and microtubule-based process. Replacing the latter with gamma-TuRC nucleation would change source mechanisms. Direct ComplexPortal API access failed during this session; the stored donor identity and independent UniProt dynactin description were retained without inventing donor species or subunit accessions.

### Validation and publication state

The first full `just validate human ACTB` run passed schema, source/GOA, reference and quote checks, with four nonblocking warnings: source-specific action differences for three duplicated terms and preservation of genuine provider reports without treating them as primary quotes. The final run additionally checks authored ontology terms and the two explicitly listed missing caches. Source-field equality, parsed-YAML equality after stripping trailing spaces, history validation and rendering are recorded in the final manifest. **Keep publication draft until normal machine caches for PMID:29925947 and PMID:9845365 are available and final reference validation passes.** No cache or generated provider report was hand-written or edited.

Final checks: `just validate human ACTB`, `ai-gene-review validate ... --terms`, `just validate-history` and `just render human ACTB` exited successfully. Validation retains five warnings, including both missing references. Independent coordinator inspection of all 247 reasons and all three core functions found no biological blocker. The publication remains draft for the two cache requirements.

### PR #3184 follow-up: source-bearing support and explicit draft status

This follow-up starts from published head `0f6201a1371e284dc9db890b2a81d3219909801b`. The three gene artifact hashes and the earlier history record matched the published manifest before editing. The previous session's decisions and validation totals above describe that earlier state. This section records the revised state; the published history record is untouched.

The generic `GO:0005515` row from PMID:17502619 is now **REMOVE**. The same source and IPI code already supply the retained `GO:0050998` nitric-oxide synthase binding annotation, so proposing that term again added no coverage. Actual cached results replace the title: human platelet G-actin binds NOS3, and the G-actin/NOS3/Hsp90 complex increases NOS activity. The specific NOS-binding and NOS-regulator rows remain non-core, and removing the generic annotation does not deny the interaction.

The actual file contains **12** `GO:0042802` rows, all IPI, rather than the 18 stated in the review. [The live GO definition](https://www.informatics.jax.org/vocab/gene_ontology/GO%3A0042802) describes binding to an identical protein and includes protein homopolymerization as a related synonym. These annotations remain **ACCEPT** because direct human beta-actin filament assembly establishes the biological function. Their reasons now distinguish that positive target evidence from the unresolved provenance of each original interaction assay; none claims that an original paper title establishes an ACTB–ACTB interaction.

The independent target evidence is [PMID:25255767, original publisher full text](https://febs.onlinelibrary.wiley.com/doi/10.1111/febs.13068). Results, **Actin assembly and disassembly**, and Figure 4A measure polymerization of recombinant wild-type human beta-actin alongside p.R183W and p.E364K. Wild type has a polymerization half-time of 20.6 ± 2.4 min; the mutant preparations polymerize more slowly. Figure 1 and the preceding production section confirm the human recombinant protein with an antibody that does not recognize insect actin. Preparations nevertheless contain 5–15% endogenous Sf9 actin, so the experiment does not establish an absolutely isoform-pure homopolymer. The observed wild-type filament assembly supports self-association. This is independent biological corroboration, not a claim to have recovered all twelve original ACTB pair records. The primary result excerpt is attached to the filament core; the individual rows cite this source and quote actual study context from their original papers. The local cache remains abstract-only, and the external full-text route is recorded separately.

Source-specific boundaries for the twelve rows are explicit. PMID:17404223 demonstrates CaMKII bundling of F-actin; PMID:18234857 reconstructs F-actin alone and with fimbrin; PMID:20383143 examines alpha-actinin domains on the filament. These establish filament or partner context without independently identifying the actin reagent as human ACTB in the available material. PMID:19000816's accessible abstract describes parasite profilin; the exact actin reagent and homotypic assay remain unresolved, and no wrong-gene claim is made. For the eight human interaction-screen sources (PMID:16189514, PMID:21516116, PMID:25416956, PMID:25502805, PMID:25910212, PMID:29892012, PMID:31515488, PMID:32296183), the individual ACTB–ACTB supplemental record and, where relevant, allele were not independently recovered. The original IPI fields remain unchanged. Retention follows the guideline permitting curator deference when the target function is independently established.

The title-support audit also covered the other retained and modified annotations named in the review. Seventy-eight rows had title-only support replaced by actual cached assay, result or source-scope passages. This includes the rat CA1 beta-actin photoactivation study (PMID:18341992), neuronal BAF transcription (PMID:17920018), source-specific chromatin remodeling experiments, nuclear actin/NDHII (PMID:11687588), NOS3, NET, DYRK1A, PDI, membrane/vesicle fractions and focal adhesions. The myosin-binding modification now uses the actual external Figure 6 result from PMID:25255767 instead of a title and a section heading. Complex-level results are distinguished from ACTB-specific perturbations, and the ACTB–ACTL6 structural linkage is cited from the existing cached Reactome source where it supplies that bridge. The PC3 proliferation inference explicitly identifies GLTSCR1/GLTSCR1L as the perturbed subunits; their necessity is not presented as an ACTB knockout result.

The [full original PMID:12368262 Results and Figure 3A](https://pmc.ncbi.nlm.nih.gov/articles/PMC187451/) were recovered again by indexed primary search (`"PMC187451" "Western" "β"`). They directly report beta-actin in affinity-purified mouse-brain and HeLa complexes. That result now accompanies the bBAF membership assessment with the species and preparation limits preserved. External full-text recovery does not change the incomplete local-cache flag.

The **gamma-TuRC microtubule-nucleation NAS row is UNDECIDED**. [GO:0007020](https://amigo.geneontology.org/amigo/term/GO%3A0007020) concerns the initial aggregation of alpha/beta-tubulin heterodimers into a seed, under microtubule polymerization. [PMID:39321809's primary abstract](https://pubmed.ncbi.nlm.nih.gov/39321809/) establishes luminal actin in non-activated gamma-TuRC and release during CM1-dependent activation. This establishes the complex association; it does not alone resolve which nucleation step ACTB structurally performs. Release during activation also does not prove a universal absence from active complexes. Direct Cell, DOI and ScienceDirect opens did not yield the full original Results during this follow-up, so neither a confident process acceptance nor rejection is warranted. No new assembly or regulation process is proposed.

Dynactin, gamma-TuRC and the three NuA4 membership rows are retained as **KEEP_AS_NON_CORE**, reflecting specialized structural pools outside the synthesized filament and SWI/SNF cores. Their physical membership is not rejected. The PAINT and ISO propagation blocks retain the verified node/donor and use `NO_FAILURE_NON_CORE`. BAF/PBAF/BRM/neural/GBAF membership remains **ACCEPT**: these are compositionally qualified forms of the existing SWI/SNF structural contribution, rather than separate motor activities. Three expert questions now record the wrong PMID's intended source, ACTB's activation-state-dependent gamma-TuRC role, and unresolved original self-interaction assay records.

Both required cache fetches were retried once using the normal machine fetcher and existing offline runtime: PMID:9845365 and PMID:29925947 each returned `Cached 0/1` with a DNS resolution error. No cache was manufactured or edited. Their verified primary evidence and citations are preserved, including the nuclear core's PMID:9845365 support. Merely moving its quote would not remove the repository's citation-cache requirement. The YAML status is now **DRAFT**, consistent with these two open cache gates. No provider report, source GOA, UniProt record, source annotation field or original reference identity changed.

Final action totals for this follow-up are **103 ACCEPT, 67 KEEP_AS_NON_CORE, 4 MODIFY, 49 REMOVE and 24 UNDECIDED** across the same 247 seeded annotations, with 175 references, three cores and no NEW annotation. All removals remain generic protein-binding annotations. Final validation, rendering, source-preservation evidence and exact file hashes are recorded in the follow-up manifest.


### Prepublication metadata and supporting-excerpt check

The eleven references PMID:11078522, PMID:14966270, PMID:15121898, PMID:17404223, PMID:19199708, PMID:22664934, PMID:23382103, PMID:23533145, PMID:24327345, PMID:27153538, PMID:30280653 retain `full_text_unavailable: false` because their cache metadata records available full text. Missing extracted sections or supplementary identification tables remain described in each reference review; partial extraction is not the same as no full-text access.

Reopened the primary Wiley page for PMID:25255767 (https://febs.onlinelibrary.wiley.com/doi/10.1111/febs.13068): the publisher labels it **Free Access**, with Results and Figure 4A accessible. No Creative Commons or comparable redistribution license was established from that page. Its concise wild-type polymerization excerpt is now included in all twelve same-protein-binding supporting entries as well as the core, using `supporting_text_fulltext` for publisher text not licensed for wholesale repository redistribution. The original machine cache remains abstract-only and unchanged.


## 2026-09-27 normal publication-cache recovery

The missing PMID:9845365 and PMID:29925947 records are now present as exact
normal-fetch output. The first remains abstract-only and directly describes
beta-actin/BAF53 purification and their contribution to BRG1 activity and
chromatin association. It does not assign the BRG1 motor reaction to ACTB.
The second now contains XML full text from PMC6145447. Results and Methods
separate beta-actin recruitment in Xenopus extracts, human U2OS actin-chromobody
imaging and repair-focus movement, and mouse-tail fibroblast perturbations.
Actin-chromobody imaging is not an ACTB-specific knockout experiment. The source
supports the existing nuclear localization and contextual interpretation; no
new repair-process annotation is proposed. Its full_text_unavailable flag is
false; the first source retains true. The obsolete missing-cache sentence in
the nucleus reason now states the source's nuclear-actin context.

Both records come from normal fetch Actions run 36286975328, head
5946477c8ac79ade0709264c775ea1262b108438, artifact 10920674630, verified ZIP
SHA-256 `c0ffe4a66b80278af34b44aab6a3ae354ffd5699236b3a486ca95527be5e9713`.
The per-file import receipt is
`tmp/verified-reference-records/local-import-receipt.json`. This dated entry
supersedes the earlier missing-cache status, without rewriting prior history.
All 247 source assertions and actions, three cores, 175 reference identities
and machine/provider files are preserved. Targeted validation, render, history
and exact byte checks are recorded in the closure manifest. Status COMPLETE
requires zero validation warnings; an unused-provider advisory is independent
of the closed cache gate. No cache content was edited.

## 2026-09-27 post-merge source12 assessment

The full audit merged through PR #3184 as `c7078166039c9abd5c62704489283403eb520007`.
The last approved review head was `3635743f96850ac6674e5af2983d4d4b123ee7df`.
Fresh main `587fad096c3c8a338b95465f53bf654968f06a8a` retained the exact eight
canonical ACTB files; no overlapping open ACTB PR or proposed follow-up branch
was found. This follow-up preserves all **247 annotation source objects and
actions**, all three core biological assertions, the original 175 reference
identities, and every machine/provider file. It adds assessments of nine
normally recovered publications and five genuine provider-linked sources still
awaiting a cache, plus a separately identified DOI-only publisher review. Recovery does not turn a provider's interpretation into an
independent experiment.

The nine records were imported unchanged from source12; the canonical import
receipt is `tmp/source12-canonical-import-receipt.json`, SHA-256
`111b2251162b55efec7612ebc869e75650cf6ac69cb26effda29b6e6c2038cee`.
Their exact bytes, hashes and null publication-base paths are included in this
follow-up manifest. Source13 adds no ACTB-owned record. Eight of the nine have
extracted bodies; PMID:11416185 remains abstract-only. Available XML does not
imply that every supplementary method, figure or identification table was read.

### Actual source scope

- [PMID:21900491] contains mouse whole-body/conditional Actb deletion, primary
  MEF and CD4-lineage T-cell experiments. Growth, migration and G/F-actin-pool
  changes corroborate structural participation. The proposed SRF connection
  does not demonstrate ACTB DNA recognition; beta/gamma colocalization in the
  tested MEFs also argues against a universal isoform-segregation claim.
- [PMID:11416185] is a chicken embryo fibroblast zipcode-oligonucleotide
  experiment. Its abstract distinguishes impaired directionality/net movement
  from unchanged total path length and protrusion velocity. ACTB mRNA is the
  regulated object; ACTB protein is not thereby the machinery for localizing
  its transcript. The primary authors and pages differ from the provider's
  generated bibliographic details.
- [PMID:34475390] distinguishes native mouse MEF nuclear co-immunoprecipitation
  (Figure 1A is labeled a single experiment) from NLS-tagged human beta-actin
  rescue in mouse Actb-knockout MEFs. The latter gives partial compartment
  rescue. Chromatin and Hi-C measurements are consistent with a structural
  contribution, not ACTB supplying the BRG1 motor reaction. A peer independently
  checked these construct and host distinctions.
- [PMID:34486492] combines pan-cancer expression/immune correlations with human
  SCC25/CAL33 ACTB-siRNA migration and invasion experiments. Altered NF-kappaB
  and Wnt-related transcript levels do not identify an ACTB catalytic signaling
  activity. The cohort correlations are not direct immune-function assays.
- [PMID:37228182] supplies free/capped filament-end cryo-EM Results; detailed
  reagent Methods are delegated to supplementary material. The primary
  [RCSB 8F8R deposition](https://www.rcsb.org/structure/8F8R), read on 2026-09-27,
  identifies the free-barbed-end actin as **rabbit alpha-skeletal actin P68135**
  and links this paper. It is family-level structural corroboration, not a
  human ACTB structure. [PMID:37632366] is the authors' short explanation of
  that same study, not an independent replication.
- [PMID:38750021] uses mouse marrow MSCs, with NIH3T3 cells also described.
  Actin-modifying drugs and Arp4 knockdown change chromatin accessibility;
  the nuclear-actin chromobody is an imaging probe. The provider's description
  of human MSCs is incorrect. These experiments are not a human ACTB rescue
  or an isolated ACTB remodeling-enzyme assay. The peer read agrees.
- [PMID:39769373] uses isoform-directed shRNA in human A549 cells, with
  reciprocal actin-isoform compensation, nuclear/lamina/histone changes and
  no significant cell-cycle/proliferation change in the measured 4-5-day
  interval. The histone-mark phenotypes do not make ACTB a histone-modifying
  enzyme.
- [PMID:38867273] immunizes mice with human JAM-ICR cells, identifies the 6D6
  antigen through immunoprecipitation/LC-MS, and examines cell-line/tumor
  immunoreactivity. This is antigen detection and clinical association,
  without an ACTB loss/rescue mechanism. It does not establish a receptor
  function or universal suitability as an expression-normalization control.

Primary PubMed identities, the recovered source records and relevant actual
Methods/Results were checked separately. The full-record assessments are in
`references[].reference_review`; exact machine-fetched titles are retained.
No action or core biological change is justified by these nine sources.

### External evidence attachments and access

The merged review's optional evidence-format concern was reassessed. Nineteen
`supporting_text_fulltext` attachments represented external passages absent
from the local extraction, without an established restriction on sharing the
full text. They have been removed from that special field. Each primary PMID
remains attached directly to the claim. A relevant ordinary cached quote is
retained where available; a reference-only attachment is used when the precise
assay passage is external. Notes are not substituted as the supporting source,
and no external passage is presented as a cached quote. In particular:

- For [PMID:25255767], the previously read
  [publisher Results](https://febs.onlinelibrary.wiley.com/doi/10.1111/febs.13068)
  and Figure 4A establish wild-type filament assembly; Figure 4 measures
  intrinsic ATP turnover and Figure 6 measures stimulation of myosin-2A.
  The short repeated fragment “compared with wild-type actin (20.6 ± 2.4 min)”
  lacked the polymerization-half-time context and is no longer treated as a
  self-contained quote. The quantitative context and the 5–15% insect-actin
  preparation limit remain documented above. The precise ATP/myosin results
  are absent from the local abstract; their reasons and primary reference
  assessment explicitly identify the external evidence. No licensing claim
  follows merely from the publisher's Free Access label or failure to find a
  license. This supersedes the earlier field-choice rationale without altering
  its historical access record.
- For [PMID:12368262], the prior external
  [Results/Figure 3A receipt](https://pmc.ncbi.nlm.nih.gov/articles/PMC187451/)
  records beta-actin detection in affinity-purified brain and HeLa complexes.
  The cache retains its true full-text-available metadata, but its extraction
  omits that Results passage. Its ordinary cached complex context and the
  independently cached ACTB–ACTL6 structural-module evidence remain attached.
- For [PMID:30280653], the prior external
  [junction section/Figure 2 receipt](https://pmc.ncbi.nlm.nih.gov/articles/PMC6335099/)
  describes actin-linked endothelial junctions. Its extracted Introduction
  provides barrier context, not an ACTB-specific perturbation. The ordinary
  contextual quote is labeled accordingly by the reason; the external
  cytoskeletal passage is not misrepresented as being present in the cache.

### Recursive provider census and five remaining cache requirements

The census includes all authored YAML/Markdown and all three immutable provider
reports, with HTML/URL decoding, title-only bibliography review and DOI/PMCID
matching against real metadata. The incorrect provider DOI
`10.1101/cshperspect.a018218` identifies an unrelated epidermal-barrier paper,
but its adjacent **PMC5749151** link identifies the genuine Svitkina review
[PMID:29295889], [DOI 10.1101/cshperspect.a018267](https://doi.org/10.1101/cshperspect.a018267).
Likewise, DOI `10.1016/j.isci.2022.105181` does not identify the claimed
actin-processing study, but **PMC9556930** identifies [PMID:36248738],
[DOI 10.1016/j.isci.2022.105186](https://doi.org/10.1016/j.isci.2022.105186).
Both primary identities were verified. The latter's accessible summary and
indexed Results concern actin as an aminopeptidase substrate, not an actin
processing enzyme; this follow-up did not comprehensively read all its Methods.

The third incorrect DOI `10.1016/j.tibs.2018.12.008` is excluded as an identifier
mismatch, but the adjacent exact title resolves a real review:
*Actin Post-translational Modifications: The Cinderella of Cytoskeletal Control*,
[PMID:30611609], [DOI 10.1016/j.tibs.2018.11.010](https://doi.org/10.1016/j.tibs.2018.11.010).
Primary PubMed identifies Varland, Vandekerckhove and Drazic as its authors,
not the generated provider author. Its abstract addresses regulation of actin
through modifications; it does not establish a new ACTB enzyme activity.

The provider's title-only 1954 pair also identifies real indexed sources:
[PMID:13165697], [DOI 10.1038/173971a0](https://doi.org/10.1038/173971a0), and
[PMID:13165698], [DOI 10.1038/173973a0](https://doi.org/10.1038/173973a0).
PubMed metadata and Nature bibliographic records identify the authors, titles
and pages. Neither PubMed record has an abstract and the full bodies were not
read. Historical muscle context is not recast as a human ACTB-specific assay.
Their citation identities are verified separately from their unassessed
experimental details.

The provider also mislabels the already cached *Essential nucleotide- and
protein-dependent functions of Actb/beta-actin*: its correct DOI and PMC6077724
identify **PMID:30012594**. The adjacent literal **PMID:30012616** identifies an
unrelated influenza-hemagglutinin simulation paper. That wrong literal is
retained in the immutable provider but excluded from biological support; no
additional source retrieval is needed for the correctly identified actin paper.

Falcon's title-only *Housekeeping gene and its internal control* resolves to
the 2025 Adhikari and colleagues review in *World Journal of Pharmaceutical
Research* 14(21):558-574, [DOI 10.5281/zenodo.17474289](https://doi.org/10.5281/zenodo.17474289).
The [publisher abstract](https://www.wjpr.net/abstract_show/31435) and indexed
[original PDF title page](https://wjpr.s3.ap-south-1.amazonaws.com/article_issue/3d49f662ebf270ae7477d92d27963cfe.pdf)
were checked on 2026-09-27. Its abstract concerns expression-normalization
controls and cautions that their stability depends on experimental context;
it supplies no new ACTB mechanism. No PMID was established, and the full body
was not assessed. This separate DOI-only source record is not replaced by an
invented PubMed identifier or manufactured publication cache.

Three finite normal fetches ended with exit 1 and **0/5 cached**, all DNS
failures: two PMC-resolved sources (`/tmp/ACTB-pmc-corrections-fetch.log`), the
Cinderella review (`/tmp/ACTB-cinderella-fetch.log`), and the two historical
papers (`/tmp/ACTB-historical-pair-fetch.log`). Each source was attempted once.
No source was manufactured or overwritten. This follow-up remains **DRAFT**
with five PMID cache gates: 13165697, 13165698, 29295889, 30611609 and 36248738.
These are additional to the nine recovered source12 records. The DOI-only
publisher record and three incorrect DOI mappings are explicitly separate in
the census. Provider bytes remain unchanged; erroneous bibliographic details
and species attributions are not endorsed. The manifest records the complete
finite census, terminal receipts and exact hashes.

## 2026-09-27 — Source19 evidence and PR #3302 attachment follow-up

This bounded follow-up preserves all 247 original annotation assertions and
actions, all three core functions, the biological description, raw sources,
provider reports and published history. The five normally recovered source19
records were read from the verified staging archive and then compared with
the coordinator's exact canonical import. The source12 missing-cache statement
above is historical and is superseded by that verified recovery. No new
annotation is proposed from these papers.

### Evidence attachments and public primary access

The review correctly identified two off-topic quotations. The general
endothelial-permeability sentence in [PMID:30280653] does not establish actin's
contribution to the blood-brain barrier, and the BAF53b assembly sentence in
[PMID:12368262] does not identify beta-actin. Both quotes are removed while
their primary reference attachments and annotation judgments are retained.
The exact existing Reactome R-HSA-9933238 quote naming the ACTB–ACTL6A/B module
remains attached to bBAF membership.

The actual local records are **partial full-text extractions**, not both
abstract-only: [PMID:12368262] contains the abstract and Discussion, whereas
[PMID:30280653] contains the abstract and Introduction. Neither contains the
target-specific passage at issue. Their retained availability flags report
these actual partial bodies, with the omitted evidence stated explicitly.
No cache was edited and no inference is drawn from the missing sections.

Primary access was rechecked on 2026-09-27:

- [PMC187451 Results and Figure 3A](https://pmc.ncbi.nlm.nih.gov/articles/PMC187451/)
  report beta-actin Western detection in affinity-purified mouse-brain and
  HeLa complexes. This is positive complex-membership evidence; the proposed
  developmental interpretation remains separate. The indexed primary Results
  reproduce the passage cited in the earlier external-access note.
- [PMC6335099 junction section and Figure 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC6335099/)
  describe ZO-protein coupling to actin and endothelial cytoskeletal anchoring.
  This is review-level barrier-maintenance context, not a direct human ACTB
  transport or signaling experiment.
- [The original Wiley Results, Figures 4 and 6, and Methods](https://febs.onlinelibrary.wiley.com/doi/10.1111/febs.13068)
  for [PMID:25255767] distinguish intrinsic filament ATP turnover from
  actin-stimulated human NM-2A ATPase. Human tag-free beta-actin was produced in
  Sf9 cells, with reported 5–15% endogenous insect actin. Figure 4 measures
  WT intrinsic turnover of about 2.1 per hour; Figure 6 reports approximately
  15-fold NM-2A stimulation by 30 micromolar WT filamentous beta-actin. The
  latter supports the retained specific myosin-binding refinement. These
  externally accessible assays are absent from the local abstract.
- The independently verified [PMID:3672117] abstract supplies an on-topic
  cached description of ATP hydrolysis after actin polymerization. It is now
  attached to the two ATP-hydrolysis rows as general actin-family support,
  with an explicit distinction from the human ACTB kinetic experiment. It
  is not substituted for the myosin-interaction assay.
- [RCSB 8F8R](https://www.rcsb.org/structure/8F8R) was independently reopened:
  the primary entry links [PMID:37228182] and identifies its actin entity as
  rabbit alpha-skeletal actin, UniProt P68135. This corroborates the existing
  species limitation without turning the structure into a human ACTB assay.

Public primary evidence remains attributed to the original PMID and primary
URL. The schema's `supporting_text_fulltext` field is reserved for text that
cannot be publicly shared or committed; cache absence alone does not meet
that condition. These accessible passages are therefore documented here and
in source-specific reasons, without a self-referential notes-file evidence
proxy. The myosin row retains its direct primary reference and explicit
external-access scope.

**Count reconciliation:** the preceding source12 note and published history
correctly describe removal of **nineteen actual full-text fields**, leaving
zero. Parsing the exact prior YAML finds seventeen annotation attachments and
two core attachments. The reviewer's text search counts twenty deleted lines
because it also matches a reference-review sentence mentioning the field name;
that sentence is not another field. The published history is preserved, and
this entry records the semantic count without changing any annotation.

### Five recovered records: actual access and experimental scope

| Source | Actual record and bounded assessment |
| --- | --- |
| [PMID:13165697] | Bibliographic-only; no abstract exists in PubMed despite the generated Abstract heading. A. F. Huxley and R. Niedergerke's 1954 Nature identity is verified. The original body, organism and ACTB isoform are not established by this record. |
| [PMID:13165698] | Bibliographic-only; no PubMed abstract. H. Huxley and J. Hanson's paired 1954 Nature identity is verified. This remains historical muscle background, without an invented human ACTB experiment. |
| [PMID:29295889] | Abstract-only Svitkina review of actin cytoskeleton and motility. The recovered title/DOI/PMCID identify the intended work behind the provider's correct PMC link and incorrect adjacent DOI. No new target-specific assay is claimed. |
| [PMID:30611609] | Abstract-only Varland, Vandekerckhove and Drazic review of actin modifications. Actin is the regulated substrate; the review does not assign ACTB the enzymes' reactions. The preserved provider's author/DOI mismatch remains explicitly corrected by the primary identity. |
| [PMID:36248738] | Full extracted Results, Discussion, Limitations and STAR Methods read. Mouse embryonic fibroblasts/tissues, human HAP1 cells and commercial human platelet actin are explicitly separated. The provider's adjacent wrong DOI remains unendorsed. |

In [PMID:36248738], mass spectrometry detects low-abundance N-terminal
beta-actin Asp removal; the gamma-actin processing pattern differs. Human
HAP1 DNPEP/ENPEP knockout affects processing, F-actin and cellular morphology,
but the authors caution that both peptidases have other substrates. Purified
ENPEP cleaves non-acetylated synthetic actin N-terminal peptides; DNPEP has
no detectable activity in that particular peptide assay, and neither enzyme
cleaves the acetylated peptides tested. These assays establish actin as a
substrate, not the entity performing proteolysis. Relative MS intensity is not
absolute quantification, and not every cellular phenotype can be assigned
solely to ACTB processing. No new process or molecular-function assertion is
added. External supplements were not separately read.

The recursive census retains the earlier explicit wrong-provider-identifier
exclusions and the separately identified DOI-only housekeeping-gene review.
All three provider reports remain byte-for-byte unchanged. Recovery of a
bibliographic record closes its cache-presence requirement without pretending
that an unavailable original paper was read.

The canonical import receipt `tmp/source19-canonical-import-receipt.json`
records exact normal-fetch bytes for all five sources; each was independently
compared with its staged record. The final recursive census finds all **136
required PMID records and 44 Reactome records present**. Twenty-five resolved
DOI mappings, three wrong-provider DOI mappings, the one wrong literal PMID,
and the separately assessed DOI-only review retain their explicit dispositions.
No additional source was fetched or manufactured in this follow-up.

Source preservation and all 254 cached supporting quotations pass independent
checks. The coordinator's complete semantic-delta read found no biological
blocker. Targeted validation passes with the four existing advisories: three
source-specific action differences and the unused-provider-reference advisory.
The YAML remains `DRAFT` because advisories persist; the five missing-cache
gates are closed and no longer require keeping the PR in draft. The new history
record, rendered page and exact publication manifest are validated separately.
