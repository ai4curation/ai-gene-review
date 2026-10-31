# CD3E (human, P07766) review notes

Project: ADAPTIVE_IMMUNITY (T cell receptor trunk).

## Biology summary (with provenance)

- TCR-CD3 composition: "The T cell receptor complex (TCR-CD3) is composed of TCR alpha/beta ligand binding subunits bound to the CD3 subunits responsible for signal transduction" [PMID:12110186]. Cryo-EM: "The octameric TCR-CD3 complex is assembled with 1:1:1:1 stoichiometry of TCRαβ:CD3γε:CD3δε:CD3ζζ." [PMID:31461748]
- Assembly: "The TCR/CD3 complex is assembled after a series of pairwise interactions involving the formation of dimers of CD3 epsilon with either CD3 gamma or CD3 delta." [PMID:9485181]; "the CD3-epsilon chain is central to CD3 core assembly and full complex formation" [PMID:8490660]; "CD3 epsilon is critical for the assembly of pre-TCR" [PMID:9886373].
- gamma-delta TCR: "whereas αβTCRs contain both CD3δɛ and CD3γɛ dimers, most γδTCRs were found to contain only CD3γɛ dimers" [PMID:16418397].
- ITAM/kinases: SPR, "The association rate and equilibrium binding constants for the ZAP-70 and syk SH2 domains were determined for the CD3 epsilon ITAM." [PMID:7761456]; N-terminal ITAM Tyr needed for ZAP-70 association [PMID:11855827].
- Proline-rich sequence/NCK: "ligand engagement of TCR-CD3 induces a conformational change that exposes a proline-rich sequence in CD3 epsilon and results in recruitment of the adaptor protein Nck" [PMID:12110186]; PxxDY motif shares Y166 with the ITAM, and its phosphorylation switches off SH3 binding [PMID:17617578]; structures with EPS8L1 SH3 [PMID:18644376] and NCK1 SH3.1 [PMID:18955169].
- Endocytosis: "Here we report that CD3 epsilon displays endocytosis determinants." [PMID:10384095]
- Newer regulators: ITPRIPL1 is "an inhibitory ligand of CD3ε" [PMID:38614099]; LAG-3 condensates with CD3E disrupt CD3E-Lck association [PMID:40592325].
- Disease: IMD18 (T-B+NK+ SCID) from CD3E mutations [PMID:8490660; UniProt].

## Curation decisions (106 GOA rows)

- 17 `protein binding` IPI rows: MODIFY to SH3 domain binding (NCK1/NCK2/EPS8L1 rows from PMID:17617578, 18644376, 18955169), protein tyrosine kinase binding (ZAP70/SYK from PMID:7761456, 11855827, 9698567), protein heterodimerization activity (CD3D/CD3G from PMID:9485181); REMOVE HuRI Y2H hits (PMID:32296183) and CEACAM1 (PMID:18424730).
- REMOVE: GPCR signaling pathway and RTK signaling pathway (TAS, PMID:8530500) - TCR-CD3 is neither.
- Over-annotated: integrin adhesion regulation (SKAP-55 paper, downstream of TCR), mouse neuronal development terms (dendrite/cerebellum development, phenotype-based), ARBA regulation terms, apoptosis (CD8-CD3E chimera crosslinking), T cell receptor binding (intra-complex contact; NAS from CD3G letter).
- UNDECIDED: positive/negative regulation of gene expression IMP (PMID:23817958, galectin-9 in MSCs; abstract does not mention CD3E, full text unavailable). Leaves one consistency warning vs the ARBA IEA row (MARK_AS_OVER_ANNOTATED) - intentional.
- Non-core: MHC class II receptor activity (contributes_to), positive thymic T cell selection (IBA), positive regulation of T cell proliferation, identical protein binding (in vitro oligomerization of disordered tails), neuronal locations, cell-cell junction.
- Necessity vs participation: process terms kept as core only where CD3E does part of the work (TCR signaling, TCR complex assembly). Proliferation/selection kept as non-core outcomes.

## Core functions

1. GO:0004888 transmembrane signaling receptor activity, in GO:0042105, directly in GO:0050852.
2. GO:1990782 protein tyrosine kinase binding (phospho-ITAM docking of ZAP70/SYK).
3. GO:0017124 SH3 domain binding (NCK recruitment via PRS).
4. GO:0030159 signaling receptor complex adaptor activity, in GO:0065003 protein-containing complex assembly, complex GO:0042101.

## Deep research

`just deep-research-falcon human CD3E --fallback perplexity-lite` succeeded (falcon, ~15 min; CD3E-deep-research-falcon.md). It was consistent with the review; it added the BRS-mediated LCK recruitment (cited in core function 2), the di-glycine hinge (Gly169-Gly170) and IRAP-dependent endosomal TCR signaling, none of which changed any annotation decision.

## Deep research integration (falcon)

Report: CD3E-deep-research-falcon.md. It is mostly built on reviews (Mariuzza 2020, Xu 2020, Menon 2023, Chandler 2020) and gives no PMIDs. I resolved the DOIs of the key primary papers through PubMed and cached them: PMID:28659468, 32690949, 32730808, 38779683, 32487999.

Note: core function 1 is now GO:0030159 signaling receptor complex adaptor activity, contributing to GO:0004888. This follows the CD3D/CD3E/CD3G harmonisation and replaces the older "Core functions" list above. The report has no evidence that conflicts with that change, or with the MARK_AS_OVER_ANNOTATED call on the contributes_to MHC class II receptor activity row.

### Claims adopted
- CD3E is the main LCK-recruiting CD3 chain, through ionic binding of its BRS to the LCK Unique domain [PMID:28659468 "CD3ε is the only CD3 chain that can efficiently interact with Lck"]. Added to the description, the core function 2 (GO:1990782) description and its supported_by, and the supported_by of the GO:0019901 MODIFY row. The action is unchanged.
- Ligation exposes an RK motif that binds the LCK SH3 domain [PMID:32690949, abstract only]. Added to the description and to core function 2.
- CD3E recruits LCK and NCK before ITAM phosphorylation [PMID:38779683]. Added to core function 2 supported_by.
- Mono-phosphorylated CD3E ITAMs recruit the inhibitory kinase CSK [PMID:32730808, abstract only]. Added to the description and core function 2. CSK is a tyrosine kinase, so this falls within GO:1990782 and needs no new term.

### Claims confirming the review (no change)
- Type I TM subunit; 1:1:1:1 stoichiometry; CD3E paired with CD3G and with CD3D; one ITAM; ZAP70 docking.
- BRS sequestered in the membrane at rest; NCK SH3.1 binding to the PRS; ER retention of unassembled subunits.
- Plasma membrane location; SCID (IMD18).

### Claims not acted on
- Di-glycine motif (Gly169-Gly170): the only source is a 2024 Research Square preprint with no PMID. The residues do match the precursor sequence.
- IRAP/Stx6 endosomal signalling (PMID:32487999): the paper is about the CD3 zeta pool. For CD3E it shows only proximity-ligation detection in IRAP vesicles ("IRAP vesicles contain several components of the TCR signalosome, such as ZAP-70, LAT, Lck and CD3ε"). That is too indirect for a NEW endosome CC annotation.
- CD3E BRS recruiting p85 in CAR-T cells (PMID:32730808): engineered CAR context, so no GO term was added.
- Calcium-mediated release of the cytoplasmic tail, and in situ extracellular conformation (Natarajan 2024): review-level or not specific to CD3E annotation.
- The "chaperone" phrasing for CD3E: not adopted. Assembly is already captured by GO:0030159 and GO:0065003.
- Clinical, therapeutic, CAR-T and aptamer sections: not relevant to GO.

### Report errors and inconsistencies
- It attributes NCK SH2 binding to phospho-Tyr177. The primary data put the shared SH3/SH2 switch residue at Y166, the N-terminal ITAM tyrosine in mature numbering [PMID:17617578].
- It mixes numbering schemes: precursor Y188/Y199 versus cytoplasmic-tail Y39/Y50 in Woessner 2024.
- Hartl 2020 is cited as an "Unknown journal" preprint, but it is Nat Immunol 2020 (PMID:32690949).
- It gives no PMIDs at all.

- Follow-up (coordinator): the PMID:28659468 quote on the GO:0019901 MODIFY row and two suggested questions (CSK recruitment in primary T cells; the Gly169-Gly170 hinge preprint) were added after the integration agent stopped, so the review now matches this section and the history record.

## 2026-10-05 whole reassessment of the historical human CD3E review

This entry supersedes conflicting scientific judgments in the preserved historical journal above; the earlier text, provider report and provider artifact have not been rewritten. The frozen association remains autosomal-recessive immunodeficiency 18, Definitive, with the original ClinGen assertion and date unchanged. The exact reviewed protein is human P07766, 207 amino acids. The original reviewed UniProt record declares no alternative-product block, so none is invented from cross-references or a provider summary.

The immutable GOA has 107 rows and 106 distinct full assertions. The single exact duplicate is the plasma-membrane IDA annotation from PMID:38614099 at raw indices 42 and 59; all 106 existing machine objects already preserve their qualifiers, original references and supporting entities. No provenance restoration or new assertion is needed. All decisions are reassessed individually. Of the 74 protected publication/Reactome caches found at intake, 53 belong to the historical reference list and 21 are auxiliary protections. The two historical records, raw inputs, provider outputs and all cache bytes remain unchanged. A supplementary normal cache is being prepared only for the verified mouse neural donor PMID:17502348; this does not refetch or reseed CD3E.

### Molecular mechanism and synthesis

CD3 epsilon supplies extracellular and transmembrane assembly contacts, a basic region that recruits LCK, a proline-rich motif recognized by partner SH3 domains, and an ITAM whose phosphorylated tyrosines recruit kinase SH2 domains. It supplies no intrinsic tyrosine-kinase chemistry. The original human structure establishes the assembled receptor architecture ([PMID:31461748](https://pubmed.ncbi.nlm.nih.gov/31461748/)); older CD3 gamma/epsilon and delta/epsilon dimer experiments support the interfaces without requiring their older two-TCR stoichiometric proposal ([PMID:9485181](https://pubmed.ncbi.nlm.nih.gov/9485181/)). The canonical 2019 cache is abstract-only. The original official abstract and selected external author reproduction were examined; the [2021 correction](https://www.nature.com/articles/s41586-021-03245-4) adds omitted subunit sequence/construct information. No image-pixel or complete-supplement inspection is claimed.

The LCK recruitment study combines human CD3E tail and human LCK biochemical experiments with a human receptor reconstitution, while its NMR constructs are mouse. Those contexts are distinct. Its D12N LCK control separates recruitment from basal kinase activity and localization, while CD3E basic-region mutants can also affect assembly. The kinase performs phosphorylation; epsilon recruits it ([PMID:28659468](https://pmc.ncbi.nlm.nih.gov/articles/PMC5530670/)). Selected available Results, Discussion, Methods and supplementary prose were read; the cached HTML body is not silently treated as a complete publisher PDF. The 2024 human Jurkat knockout/reconstitution and CAR-T study has surface-expression controls, but its tyrosine-to-glutamate variants are phosphomimetics rather than direct measurements of every native phosphorylation state ([PMID:38779683](https://pubmed.ncbi.nlm.nih.gov/38779683/)).

The binding refinements distinguish the sides of the interface. CD3E's proline-rich motif binds the SH3 domains of NCK1, NCK2 and EPS8L1; CD3E does not acquire an SH3 domain by binding those proteins ([PMID:17617578](https://pubmed.ncbi.nlm.nih.gov/17617578/), [PMID:18644376](https://pubmed.ncbi.nlm.nih.gov/18644376/), [PMID:18955169](https://pubmed.ncbi.nlm.nih.gov/18955169/)). Direct phospho-ITAM/tandem-SH2 measurements establish ZAP70/SYK association ([PMID:7761456](https://pubmed.ncbi.nlm.nih.gov/7761456/)). The receptor adaptor core integrates these interfaces rather than duplicating the same signaling process as several independent outcomes.

A second core captures target-specific recognition of the inhibitory ligand ITPRIPL1. The final canonical publication abstract explicitly identifies CD3 epsilon and inhibition of TCR signaling ([PMID:38614099](https://pubmed.ncbi.nlm.nih.gov/38614099/)). Earlier author-preprint passages were read separately and are not passed off as final-paper Methods. The downstream mouse/canine therapeutic observations do not define human construct-specific mechanisms. The 2025 LAG3 study supports another interaction with CD3 epsilon, but only its abstract and selected publisher summary/introductory text were inspected; no complete experimental-species inventory is claimed ([PMID:40592325](https://pubmed.ncbi.nlm.nih.gov/40592325/)).

### Binding, complex contribution and signaling terms

The standing project instruction retains supported generic protein binding as non-core unless a more informative molecular-function refinement is supported. Accordingly, historical blanket HuRI/CEACAM1 removals are superseded. Exact reviewed UniProt partner edges corroborate the six HuRI associations. NCK2 has separate direct domain evidence and is refined using that source, without claiming the original HuRI target table was re-read. The other retained pairs do not establish a domain-specific interface or signaling role just from partner identity. CEACAM1 association with the TCR/CD3 complex and SHP1 recruitment support a qualitative complex association; the exact epsilon-specific original co-IP panel and a purified binary interface were not independently recovered ([PMID:18424730](https://pubmed.ncbi.nlm.nih.gov/18424730/)).

The MHC-II receptor annotation retains its original contributes_to qualifier. Cached GO-CAM 685de18700002961 represents the activity as enabled by the alpha-beta TCR complex with CD3E as a part, not as isolated epsilon binding peptide-MHC. Its activity evidence and complex membership are explicit. This is compatible with epsilon's own assembly/signaling contribution and is not grounds for an overannotation call. The core does not give epsilon the clonotypic recognition site. The TCR-binding NAS is also retained non-core using independent physical assembly evidence; its original PMID:11186279 cache has bibliographic content only, so that particular source remains unverified. The GO definition does not restrict receptor binding to extracellular ligands.

GO:0007172 signal-complex assembly covers assembly of the signal-transducing complex and is not restricted to a free cytoplasmic adaptor complex. Epsilon's physical receptor-assembly work supports it. Broad immune-response, cellular signaling, complex-assembly and proliferation/selection terms are retained where sound but kept outside the more specific core. Receptor organization and recruitment can regulate signaling, so historical claims that a signal-transducing component cannot regulate its own pathway are not retained.

The two historical TAS assignments to PMID:8530500 require different judgments. GO:0007169 requires a receptor possessing tyrosine-kinase activity; this report describes TCR-associated kinases and G-alpha-q/11 signaling, not receptor-intrinsic kinase activity. The source-specific RTK label is over-annotated. By contrast, GO:0007186 is defined through receptor-promoted GDP/GTP exchange on an associated heterotrimeric G protein and does not explicitly require seven membrane helices. The original abstract reports nucleotide exchange and PLC-beta coupling, not merely association. Its complete Methods and detailed receptor/construct controls remain inaccessible, so the GPCR assignment remains undecided rather than rejected from CD3E topology or an unsupported claim about replication. The official term definitions were read independently of the old review.

### Resolved donor and correction boundaries

The original adhesion source was examined through an author reproduction of [PMID:12652296, DOI:10.1038/ni913](https://doi.org/10.1038/ni913), including selected Methods and Results for fibronectin binding, ICAM1 binding and T-cell/APC conjugation. Anti-CD3 2C11 stimulates mouse CD3 epsilon in T8.1 cells; the introduced human construct is SKAP55, not CD3E. Mouse primary T cells also contribute experiments. BSA, unstimulated/vector, anti-LFA1, phorbol-ester and Mg/EGTA controls distinguish the endpoints and inside-out signaling. The evidence supports the retained donor-based positive adhesion regulation without implying intrinsic integrin binding or a directly tested human CD3E construct. The [actual 2025 correction](https://www.nature.com/articles/s41590-025-02239-y) replaces an incorrect Vector image and explicitly leaves the conclusions unaffected. The replacement image pixels were not inspected.

The official dated MGI donor graph resolves the four neural transfers to [PMID:17502348](https://pmc.ncbi.nlm.nih.gov/articles/PMC1951947/). Selected original Methods and Results establish mouse Purkinje somatic/dendritic staining and altered dendritic/cerebellar phenotypes. They also describe Bergmann-glial expression. Crucially, the Cd3e knockout lacks detectable Cd3d and has reduced Cd3g; it does not isolate an epsilon-only neuronal mechanism. The transfers are retained non-core with those limitations and without inventing direct human neural evidence or an epsilon-specific rescue. The normal cache is pending in this provisional snapshot; final metadata and any cache-access claim must bind the actual imported bytes.

The [PMID:32690949 correction](https://www.nature.com/articles/s41590-020-00843-8) replaces a graph inadvertently duplicated between figure panels and corrects the associated statistical caption. The notice was read, not the corrected pixels. It is not treated as a retraction or a reason to discard all target adaptor/signaling evidence. The original mouse/human distinctions in the gamma-delta receptor study also remain explicit; murine CD3 composition is not automatically imposed on human gamma-delta receptors ([PMID:16418397](https://pubmed.ncbi.nlm.nih.gov/16418397/)).

### Remaining access limits and audit boundary

The two IMP gene-expression rows from PMID:23817958 remain undecided. The available abstract concerns human stromal-cell/galectin-9 and lymphocyte responses, but does not expose the exact CD3E perturbation or expression endpoints. It is not labeled a wrong-gene citation from its title. The separate electronic positive-expression assertion is retained using independently supported receptor-dependent signaling rather than pretending the inaccessible IMP assay was inspected.

All 36 historical PMID headers and available complete abstracts were read. The 17 Reactome event headers/summaries were read, without claiming full participant-graph reconstruction. Reference assessments distinguish available XML/HTML from actual sections inspected, partial bodies, external author copies, preprints, and uninspected interaction tables. GO_REF records describe methods, not biological experiments; exact ARBA rules and the full PAINT tree/MSA were not reconstructed. A short donor list or target self-inclusion is not a defect. The old Falcon outputs remain unchanged orientation material, with no new provider output fabricated and no provider quotation used as the sole basis of a core.

The inherited notes above contain earlier quotations and superseded decisions. They are preserved as historical provenance, not newly authored quotations. New YAML snippets and this append are audited separately, with no new verbatim quotations in this append. Literal snippets are checked against their actual source bytes and aggregated across all new YAML occurrences. The source and product projection, frozen files, GO-CAM files/index, old history and original notes prefix are checked mechanically before the final owner is sealed. Normal staged validation/status/render and independent whole scientific peer review remain required; this provisional snapshot is not canonical application or publication acceptance.


### Final synthesis and remaining source-access checkpoint

The first core now uses contributes_to GO:0032395 MHC class II receptor activity in its machine slot, matching the already accepted source row 78 and the cached GO-CAM complex role. The current official AmiGO definition describes recognition of MHC-II and signal transmission and places the activity under GO:0004888 and GO:0140375 (https://amigo.geneontology.org/amigo/term/GO%3A0032395). Model 685de18700002961 assigns the activity to an alpha-beta TCR complex containing CD3E; PMID:1323144 is its activity evidence and PMID:31461748 supports the CD3E subunit. The specific contributes_to term does not claim that isolated epsilon supplies clonotypic peptide-MHC specificity or that every CD3E-containing receptor is class-II restricted. Its exact scope is stated in the core description. The separate own-receptor GO:0004888 core concerns ITPRIPL1 recognition, a distinct ligand input; no NEW annotation is added. The additional PMID:1323144 core pointer introduces no quotation.

A further direct access attempt for PMID:23817958 failed at the original Wiley full-text endpoint (https://onlinelibrary.wiley.com/doi/full/10.1002/eji.201343335). The authors' institutional record at https://iris.unimore.it/handle/11380/972112 exposes a complete abstract but labels its deposited PDF as restricted access. It provides no new CD3E-specific perturbation or expression control. Rows 67/68 therefore remain UNDECIDED, without a wrong-gene, miscitation or antibody-artifact conclusion. The saved primary access result distinguishes this boundary from a full-paper reading.

This provisional snapshot still awaits authenticated normal-cache integration for PMID:17502348 and the final normal validation/status/render sequence. All 106 annotation actions and all source objects are unchanged from preliminary-v2.


### Source-description precision audit before final seal

A final source-by-source reread corrected four inaccurate source descriptions in the provisional draft. PMID:11368773 is the ZAP70/LAT phosphosite study, not the CD3-epsilon conformational-change report; PMID:15294938 is the CD6/TCR-CD3 coassociation and synapse study, not an extracellular CD3 structural paper; PMID:17213291 concerns FcRL6 expression/signaling, with the original CD3E surface-localization control still uninspected; and PMID:8176201 describes ZAP70/SYK expression and a Src-dependent zeta-chain assay, not an epsilon-specific reconstitution. The exact abstracts were reread. These corrections affect rows 28, 63, 81 and 98 and their reference assessments, without changing any action or machine source field. The retained location, membership and signaling assertions use the explicitly cited independent human CD3-epsilon surface, structure and recruitment evidence. PMID:17213291 remains UNVERIFIED for its exact target-specific localization claim despite checked bibliographic identity; no absence or miscitation conclusion is inferred from its abstract.

The earlier provisional snapshots remain available. The v4 YAML restores the existing width-88 serialization after the v3 synthesis build used width 100; the formatting correction has no semantic effect beyond the source-prose changes listed above. No new quotation was added.


### Informative audit anchors and source-ledger refresh

Before final source integration, a finite anchor pass replaced several short noun fragments with exact assay or interaction clauses, and supplied cache-verbatim support for the three remaining pointer-only binding refinements and the ITPRIPL1 core. The same source/partner and construct limitations remain explicit; these excerpts do not establish uninspected original screen tables. All 106 actions, machine fields, reference assessments and core terms are unchanged. The new quotes are allocated across all YAML occurrences, with no new verbatim quotation in this notes append. The inherited historical journal remains an exact prefix and is not represented as satisfying the newly authored quote budget.

The refreshed source-access ledger now derives every assessment from the current candidate, including the four corrected source descriptions and the separately disclosed expression-source access failure. The old v2-bound provisional ledger is retained as a superseded intermediate artifact. PMID:17502348 normal-cache metadata still awaits authenticated recovery and ROOT import; external primary readings remain distinctly identified.


### Authenticated donor cache and final audit-anchor integration

ROOT imported the authenticated normal PMID:17502348 cache after bounded transport recovery, source-identity assessment and protected-source checks. The reference title and access flag now follow those exact canonical bytes. The complete available header and abstract were read; the prior selected PMC Methods/Results remain separately identified as external primary access. The mouse construct, cell-context and knockout-complex caveats remain unchanged. This supersedes the pending-cache statements in earlier journal entries without rewriting their historical text.

The four PMID:7761456 anchors were first shortened too far during the finite anchor pass. PR review restored full-clause evidence for the phospho-ITAM/kinase and proline-rich/SH3 rows, restored GO:1990782 and GO:0017124 as dedicated core functions, restored class-agnostic GO:0004888 receptor activity in the receptor-adaptor core, and reverted the ARBA positive gene-expression row to MARK_AS_OVER_ANNOTATED. The five retained HuRI reasons now explicitly identify the GOA and UniProt IntAct records as the same underlying evidence, not independent experimental replication; the two related reference assessments use the same distinction. Five short literal UniProt pair anchors verify recorded identifiers only, not uninspected original constructs or controls. This clarification supersedes the ambiguous corroboration wording in the earlier journal entry. NCK2 retains its genuinely separate primary domain evidence, and the inherited historical prefix is preserved separately from the new quotation budget.
