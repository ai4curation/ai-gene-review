# CALM1 — biological evidence notes

## Calcium sensing and distinct target activities

Human CALM1, CALM2 and CALM3 share the canonical calmodulin protein sequence. Experiments on that protein establish biochemical capabilities but do not by themselves identify which gene supplies it in a cell. Calmodulin binds calcium through EF-hand sites; the KCNQ-associated structure reports [PMID:27564677 "four Ca(2+) ions are bound"]. Calcium sensing enables several distinct target-regulatory activities rather than making calmodulin the target enzyme or channel pore.

The CaMKII structural study explains activation through the regulatory segment and active-site configuration: [PMID:20668654 "mechanism of CaMKII activation by calmodulin"]. Its complete available Results and Methods were read; experimental construct numbering is not evidence for an additional human product. Calmodulin activates the kinase, which performs phosphate transfer. A separate human-calmodulin disulfide-mutant study reports [PMID:8631777 "loss of ability to activate 
target enzymes, phosphodiesterase and calcineurin"]; reduction restores regulatory activity. That abstract supports phosphatase activation without assigning calcineurin's dephosphorylation chemistry to calmodulin.

Channel regulation is target dependent. The CaV1.2 study reports [PMID:26969752 "dominant loss of inactivation in CaV1.2"] for disease-associated variants. RyR2 studies independently support modulation of cardiac calcium release, whereas the complete human Reactome R-HSA-9865670 narrative describes TRPV4 potentiation. These results support a broad calcium-channel-regulator activity, not universal channel inhibition. The three functional units remain kinase activation, phosphatase activation and channel regulation, with calcium binding as their enabling sensing mechanism.

## Nuclear location and reaction-specific uncertainty

The complete cached human Reactome R-HSA-2730867 and R-HSA-4551465 records explicitly name CaM-containing calcineurin:NFAT complexes translocating to the nucleus. They corroborate a nucleoplasmic calmodulin pool. All six existing nucleoplasm assertions are therefore retained as ACCEPT. The three CaMKK-linked records require separate caveats: R-HSA-442749 leaves the kinase reaction compartment unresolved; R-NUL-9618916 combines mouse Camkk1 with human calmodulin; R-NUL-9619177 combines rat Camkk2 with human CAMK4 and assumes recombinant-calmodulin species identity from sequence conservation. Those experiments do not independently locate the particular reaction in a human nucleus. Their uncertainty does not negate the independently supported target-location assertion. The underlying primary localization experiments and structured Reactome participant graphs were not inspected.

## Gene-specific disease attribution and residue numbering

The CALM1 arrhythmia study directly reports [PMID:23040497 "Both CALM1 substitutions demonstrated compromised calcium 
binding"]. Its N53I/N97S names use mature-protein numbering. UniProt P0DP23 records initiator-methionine removal from the 149-residue precursor and a chain spanning residues 2–149, so the corresponding precursor names are N54I/N98S. Three paralog genes must not be interpreted as three CALM1 alternative products.

The later calmodulinopathy report explicitly separates [PMID:31454269 "CALM3-E141K in 2 
cases; CALM1-E141V"]. CALM1-E141V must be distinguished from CALM3-E141K and CALM3-D130G; the two mosaic pedigrees concern CALM3. Its cardiomyocyte experiments overexpress mutant or wild-type calmodulin, and detailed Methods reside in an unavailable supplement. The CALM3-A103V study (PMID:27516456) also compares known CALM1 variants, so its title alone does not invalidate CALM1 biochemical evidence. The PMID:26969752 abstract and cached author narrative give differing cohort counts; no prevalence or cohort-size claim is made here.

## Contextual functions and limits of the available evidence

Anthrax edema factor is a real calmodulin-activated target: calmodulin [PMID:11807546 "stabilizes a 
disordered loop and leads to enzyme activation"]. This pathogen context does not establish a mammalian GPCR-linked cyclase core. The mu-opioid-receptor work supplies a separate GPCR regulatory context. CP110 binding-defective experiments and bacterial OspC/CaMKII signaling experiments support their specific cellular contexts without establishing universal cell-cycle or CALM1-gene-specific mechanisms.

Supported generic interactions are retained as non-core when no finer activity is justified. Directly supported refinements include IDH1 enzyme binding, KIF1A kinesin binding, EPB41 cytoskeletal binding and channel/transporter binding. Association alone does not transfer a partner's catalysis or establish its activation. LYST and tau target-interaction assertions remain unresolved because the relevant original target evidence was not recovered; the tau abstract is truncated. Other remaining uncertainties concern G2/M transition, sperm midpiece, calyx of Held, presynaptic endocytosis, calcium export and substantia nigra development.

The primary reading comprises complete cached abstracts and the specifically identified available Methods, Results or narrative sections. A full-text metadata flag does not establish that target tables, images or supplements are present. The PMID:19855925 erratum corrects Figure 5 panels and an axis unit; correction prose, not images, was inspected. PAINT node evidence supports conserved activities, without a claim to have reanalyzed every donor or the complete alignment. These access boundaries remain recorded per reference.

## Current follow-up assessment

The focused follow-up changes only the three nucleoplasm decisions and the question that distinguished their reaction compartments: 106 ACCEPT, 48 KEEP_AS_NON_CORE, 14 MODIFY and 8 UNDECIDED across the same 176 source assertions. All references, source fields, existing evidence quotations and three functional cores remain unchanged; no new annotation or product is introduced. The original dated journal below is preserved verbatim as historical provenance. Its earlier action counts and nuclear uncertainty classification are superseded by this section.

<details>
<summary>Original dated journal — historical assessment and provenance</summary>

# CALM1 scientific review — 2026-10-04

This review distinguishes CALM1 gene-specific evidence from experiments on the canonical calmodulin sequence shared by human CALM1, CALM2 and CALM3. The primary accession is UniProt P0DP23, human taxon 9606, HGNC:1442. The record describes a 149-residue precursor with the initiator methionine removed and a chain spanning residues 2–149. The N53I/N97S names in PMID:23040497 use mature-protein numbering; the corresponding UniProt precursor names are N54I/N98S. Three paralog genes are not three alternative products of CALM1. No alternative-product slot or unverified product inventory was added.

## Source restoration and review scope

The prior review had 171 annotation objects, while its immutable GOA file contains 179 records. Normal reseeding in an isolated TMP directory produces 176 distinct assertions: two byte-identical duplicate records and one date-only duplicate collapse without losing a distinct biological claim. The normal projection restores five partner-specific assertions: two myelin-basic-protein partners from PMID:19855925, IQGAP3 from PMID:21299499, KCNQ3 from PMID:27564677 and CAMK2D from PMID:20668654. These are existing source assertions, not five NEW annotations. All 179 raw records were joined exactly once to the 176 assertions, with qualifiers, original term/reference/evidence, literal supporting entities and negation preserved. ROOT independently checked that projection.

All 176 assertions are assessed: 103 ACCEPT, 48 KEEP_AS_NON_CORE, 14 MODIFY and 11 UNDECIDED; no REMOVE, MARK_AS_OVER_ANNOTATED or NEW is proposed. All 91 original reference IDs and titles are retained, and UniProt:P0DP23 is added for explicit target-specific curated evidence. There are three core units. The review remains DRAFT because the remaining uncertainties and validation advisories are explicit rather than resolved by bookkeeping.

The existing provider-authored Falcon deep-research file was read as orientation. Its original bytes and the other existing Falcon files are preserved. It is not treated as primary proof, and no new provider output or invented provider file was created. The notes and source assessments document the manual review. No source fetch, cache rewrite, canonical authored edit or historical-record rewrite forms part of this TMP proposal.

## Molecular functions and synthesis

Calcium sensing is the mechanism that enables target regulation, rather than a redundant fourth core. The first core is calmodulin's own protein serine/threonine kinase activator activity. The human CaMKII study (PMID:20668654) explains displacement of the inhibitory segment, rearrangement of the catalytic site and the active regulatory configuration. Independent binding/phosphorylation/autophosphorylation comparisons (PMID:14722083) corroborate the biochemical regulatory role. Calmodulin is not assigned the kinase's phosphate-transfer activity. The Methods construct named calmodulin 1–152 is reported as experimental construct numbering; it does not establish a new human product.

The second core is calmodulin's own protein phosphatase activator activity. Human calmodulin disulfide mutants lose calcineurin activation and recover regulatory activity after reduction (PMID:8631777). The cached calcineurin/NFAT events place the regulatory assembly in cytosolic and nuclear signaling contexts. Calcineurin, not calmodulin, performs dephosphorylation.

The third core is target-dependent calcium-channel regulation. CaV1.2 inactivation and RyR2-mediated release control connect calmodulin sensing to cardiac electrical and contractile regulation (PMID:26969752, PMID:26164367, PMID:23040497, PMID:22067155). The broad regulator MF remains useful because calmodulin can potentiate other calcium channels: the complete cached Reactome R-HSA-9865670 narrative explicitly describes TRPV4 potentiation. The core does not claim universal channel inhibition or channel-pore activity. The existing source-specific inhibitor annotations remain appropriate for their own targets. The sarcomere assertions (zero-based rows 19 and 154) are ACCEPT, consistent with the core's cardiac location and independent RyR2-directed FRET/Z-line evidence; this is not an assertion of structural sarcomere work. The broad sarcoplasmic-release parent is subsumed by the existing cardiac-contraction child rather than duplicated in the core.

Anthrax edema-factor activation is real but contextual (PMID:11807546). It does not support the former mammalian GPCR-linked adenylate-cyclase core. The mu-opioid-receptor study independently supports a distinct GPCR regulatory context (PMID:10899953). CP110 binding and the binding-defective CP110 mutant provide functional evidence beyond generic depletion (PMID:16760425), but are retained as contextual cytokinesis regulation, without converting that experiment into G2/M-transition evidence or a universal fourth core. The bacterial OspC study contains real host CaM/CaMKII/JAK-STAT experiments (PMID:35568036), but is not the sole foundation of the general kinase-activator core and is not interpreted as CALM1-specific gene deletion.

## Binding and source-specific uncertainty

The standing user instruction in projects/CLINGEN_MENDELIAN.md retains supported generic binding as KEEP_AS_NON_CORE when no justified finer MF is available. It takes precedence over the generic validator suggestion to remove all bare binding. This affects ten retained generic-binding assertions. Biological reasons describe the experiment and limits; they do not substitute policy discussion for evidence.

The bounded binding consultation examined all 21 assigned source objects and recommends 10 NC, 9 MODIFY and 2 UNDECIDED. The original handoff is preserved. Two wording corrections were agreed during integration: the IDH1 abstract supports quantitative Kd measurements, not an asserted calorimetry method; the truncated S100b/melittin abstract does not expose microtubule-assembly effects. The actions and source objects are unchanged by those corrections. Directly supported refinements include IDH1 enzyme binding, edema-factor adenylate-cyclase activation, KIF1A kinesin binding, EPB41 cytoskeletal binding, channel/NHE1 transmembrane-transporter binding and USP6 protease binding. The old IQSEC2 clathrin-binding and IDH1 enzyme-activation rationales are not retained. Neither partner enzyme catalysis nor a stronger regulator function is inferred from mere association.

Rows 54 and 81 remain UNDECIDED because the relevant LYST and tau target evidence was not recovered; a paper title is not used to call either an experimental misattribution. Other uncertainties are the specific G2/M-transition, calyx-of-Held, sperm-midpiece, presynaptic-endocytosis, negative calcium-export and substantia-nigra-development assertions, plus three mixed-species nuclear CaMKK contexts. Positive independent target evidence is distinguished from failure to inspect the exact original experiment. No donor count, target-self circularity argument or unverified wrong-paralog claim is used.

## Propagation and pathway reading

Eight exact calmodulin IBD assertions were read in the cached PTHR23048 PAINT export, including PTN000549682 calcium binding and the relevant PTN008588804/806/809 localization, calcium detection, calcineurin and sarcoplasmic-release assertions. The full phylogenetic tree, multiple alignment and every donor experiment were not reanalyzed. A target appearing among experimental descendants is legitimate grounding. Literal source identities and source-specific corroboration are retained; no new family IDs or ancestral claims were invented.

The separate Reactome consultation read all 48 complete cached event narratives for 54 assigned localization rows. These are cached narratives, not a new inspection of structured participant graphs or all linked publications. It retains 50 ACCEPT and one extracellular KEEP_AS_NON_CORE, with three UNDECIDED nuclear contexts. Platelet-release wording explicitly includes lysis and therefore does not establish active calmodulin secretion. Mixed rat/mouse/porcine/human R-NUL events are not relabeled as human-only experiments. Calcineurin translocation and other explicit cytosolic events support some localizations, while distinct CaMKK nuclear claims remain uncertain. This source-specific difference explains the validator's nucleoplasm action warning; equal GO IDs do not erase differing reference support.

## Disease attribution and access limits

ROOT independently reviewed PMID:23040497, PMID:26969752, PMID:27516456 and PMID:31454269. CALM1-E141V is distinguished from CALM3-E141K and CALM3-D130G; the two mosaic pedigrees in PMID:31454269 are CALM3. Its cardiomyocyte experiments involve overexpression, and the missing supplement contains detailed Methods. PMID:27516456 reports CALM3-A103V clinically but explicitly compares known CALM1 variants, so the CALM1 annotation is not rejected merely from the CALM3 title. PMID:26969752 has a version discrepancy between 38/5 and 39/6 cohort counts; neither prevalence nor cohort size is used in the biological synthesis.

All 36 cached primary abstracts were read; PMID:3111527 is intrinsically truncated. Eighteen caches advertise full-text availability, but that metadata does not establish completeness. The actual reading is recorded per reference in the YAML. Selected cached full-text narratives omit central Methods, Results, target tables or supplements in several cases. No uninspected figure, target edge or complete paper is claimed. The complete unique CaMKII Results/Methods and the relevant OspC Results/selected Methods were read. The CP110 cache, calcineurin abstract, channel narratives and peer source readings supply the specific limits described above.

The official PMID:19855925 erratum at https://link.springer.com/article/10.1007/s00726-010-0583-6 corrects Figure 5 panels and an axis unit. Correction prose was inspected, not the images; no affected quantitative circular-dichroism conclusion is used. The canonical PMID:28890335 cache and its remote metadata variant are both preserved: remote adds full_text_attempted metadata, with the other bytes matching. No source cache was overwritten to simplify validation.

## Evidence anchors and checks

Eleven short exact primary anchors are attached to load-bearing reviews or cores. Each is a literal substring of its immutable local cache. The aggregate maximum is 13 quoted words per primary source; this notes file adds no quoted source text. All other support objects are reference-only. The quote ledger records every occurrence rather than counting only unique snippets.

The bounded core consultation found no synthesis defect. Its historical candidate pin is preserved; a later description wording improvement says the three human genes share the canonical calmodulin sequence, avoiding an implication that their wider transcript/product inventories are identical. Two existing sarcomere review actions were aligned with the channel core as described above. Full normal candidate validation and exact source-projection checks are recorded in the accompanying proposal packet; canonical application and publication require ROOT's distinct whole-science peer.

Normal candidate validation completed successfully with 12 warnings: ten standing-policy generic-binding advisories, the source-specific nucleoplasm action difference, and the optional unused provider-file support advisory. Schema, authored term validation and reference validation passed. Initial runs stopped because the sandbox could not write the default uv cache; the final run used the installed environment without synchronization and an isolated writable uv cache. An intermediate propagation-root-cause enum typo introduced while aligning the sarcomere row was corrected to the defined NO_FAILURE_CORE value. Those failed results are retained. No validator rule was weakened and no source bytes were changed to obtain the passing result.

</details>
