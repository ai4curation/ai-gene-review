# CLRN1 (clarin-1, USH3A; UniProt P58418) — review notes

## Identity and architecture
- Human clarin-1, 232 aa, four-transmembrane (tetraspanin-like) glycoprotein of the clarin family (paralogs CLRN2, CLRN3). Single N-linked glycosylation site at Asn48 (first extracellular loop). UniProt P58418; TCDB 9.A.46.1.1 "the clarin (CLRN) family"; InterPro IPR026748; PANTHER PTHR31548:SF4.
- Biallelic loss-of-function variants cause autosomal-recessive Usher syndrome type 3A (USH3A): post-lingual, progressive sensorineural hearing loss, variable vestibular dysfunction, and rod–cone retinal degeneration (retinitis pigmentosa). Some CLRN1 variants also cause non-syndromic RP61 [UniProt P58418; PMID:21310491].

## Core wild-type function (hair-bundle F-actin organization + trafficking, NOT a member of the USH1 tip-link or USH2 ankle-link complexes)
- Clarin-1 acts as a plasma-membrane-associated organizer of the F-actin cytoskeleton in sensory hair cells, required for stereocilia hair-bundle integrity and efficient mechanotransduction, and (basolaterally) for inner-hair-cell ribbon-synapse maturation.
- Heterologous (HEK293) study: Human clarin-1 expressed in HEK293 cells occupied surface membrane domains distinct from conventional lipid rafts and changed actin-rich cellular protrusions. [PMID:19423712]
- In vivo support that the actin role is physiological: Mouse Clrn1 loss disrupted the arrangement of actin-rich auditory hair bundles, providing an in-vivo counterpart to the cell-expression phenotype. [PMID:19423712]
- The N48K USH3A mutant (loss of glycosylation) fails the actin-reorganizing function and is degraded/mislocalized: The N48K variant failed to produce the same cellular remodeling and also had glycosylation, folding and abundance defects. [PMID:19423712]

### Caveat on the HEK293 readouts
The lamellipodium induction, cell motility, and microvillus enrichment in PMID:19423712 are heterologous-overexpression phenotypes in a non-sensory immortalized cell line. They report an underlying actin-organizing activity but are not the wild-type in-vivo function of clarin-1 (hair cells are not motile and do not make lamellipodia). Wild-type expression promoted local spreading and protrusion formation in the assayed cells. [PMID:19423712] Treated here as over-annotations of the core actin-organization function.

## Localization
- Cell/plasma membrane, multi-pass membrane protein [UniProt; PMID:21310491 EXP; PMID:19423712 IDA].
- Stereocilium (hair-bundle) localization — well supported (mouse ortholog; disorganized stereocilia in Clrn1-/-). Core location.
- Basolateral/ribbon-synapse (basal part of cell) localization in inner hair cells [deep-research: Dulon 2018, JCI94351 — mouse].
- Passes through Golgi (Endo H-resistant, PNGase F-sensitive glycan): The observed glycan sensitivity pattern supports passage through Golgi processing. [PMID:19423712] — consistent with trans-Golgi trafficking transit (non-core).
- Microtubule cytoskeleton (IEA, Ensembl from mouse ortholog): no biological support; clarin-1 associates with F-actin, not microtubules. Treated as over-annotation.

## Hearing / balance
- Sensory perception of sound: core. USH3A = progressive hearing loss; IMP from Finnish USH3 patients [PMID:15650299]; IBA across clarin family.
- Equilibrioception (vestibular): genuine hair-cell function; variable vestibular dysfunction in USH3A [IMP PMID:15521980; IBA].

## Retina
- Retinal degeneration in USH3A is real, but recent evidence localizes CLRN1 predominantly to Müller glia rather than photoreceptors, implying a non-cell-autonomous, structural/homeostatic support of photoreceptors [deep-research: Xu 2020 J Pathol path.5360; Nonarath 2025 PLoS Genet pgen.1011205]. Photoreceptor-maintenance / light-perception BP annotations (IMP from patient RP phenotype, PMID:15521980) are accepted as non-core.

## Protein interactions
- 27 "protein binding" (GO:0005515) IPI annotations all derive from a single systematic yeast-two-hybrid screen: "A reference map of the human binary protein interactome" (HuRI/HI-III-20) [PMID:32296183]. The study used scalable yeast two-hybrid assays to map binary human protein interactions. The recovered partners (ALG8, MGST3, SEC22B, ITGAM, various TMEMs, claudin-19, etc.) are largely ER/membrane proteins and do not correspond to the physiologically meaningful partners (harmonin/USH1C, CACNB2/CaV1.3). Bare "protein binding" is uninformative — marked as over-annotated.

## Action summary
- ACCEPT (core): sensory perception of sound (IBA, IEA/ARBA, IMP); equilibrioception (IBA, IMP); actin filament organization (IDA); stereocilium; plasma membrane (IEA, EXP, IDA); basal part of cell.
- KEEP_AS_NON_CORE: photoreceptor cell maintenance; sensory perception of light stimulus; trans-Golgi network transport vesicle.
- MARK_AS_OVER_ANNOTATED: protein binding (x27, HuRI Y2H); microvillus, lamellipodium, positive regulation of lamellipodium assembly, cell motility (HEK293 overexpression); microtubule cytoskeleton (unsupported IEA).

## Evidence-based update and supersession (2026-10-11)

The following assessment supersedes the earlier over-annotation judgments and molecular interpretations without erasing the earlier findings.

Positive binding observations are retained at assay-specific, non-core scope. Twenty-six partner-specific HuRI rows have three exact positive IntAct records each; their assay roles, fragments and isoform identifiers are preserved. Twelve rows are refined to an established partner class, without claiming a native physiological mechanism or transferring catalytic/transport activity to clarin-1. The unscoped historical binding assertion remains non-core. The selected HuRI text contains Results and assay/validation legends; target-level traceability comes from the literal interaction records. [PMID:32296183]

The earlier claim that microtubule localization had no experimental support is superseded. Mouse UB/OC-1 cells show controlled tubulin colocalization and nocodazole-dependent redistribution. The original study also uses tyrphostin A8 and brefeldin A comparisons to interpret a post-Golgi trafficking pool. These observations support the donor annotations with model-specific limits; they do not establish direct microtubule binding or an intrinsic transport activity. Its developing-hair-cell antibody and immunogold data independently support stereociliary and basal localization. [PMID:19539019]

The human HEK293 microvillus, lamellipodium, protrusion-induction and spreading observations are positive source-specific results. Heterologous expression limits physiological extrapolation but is not evidence against the observed activities or compartments. They are now non-core rather than over-annotated. Three independent clones, membrane-impermeant biotinylation and cytoskeletal imaging support the primary cellular findings. N48K changes protein abundance, folding and delivery as well as the phenotype, so its comparison does not isolate a catalytic mechanism. The paper leaves direct actin partners unresolved. [PMID:19423712]

A single core now integrates apical bundle and basolateral synaptic organization. Mouse conditional deletion and postnatal rescue demonstrate that the two cellular contexts can be separated. The original synaptic binding supplement identifies mouse CLRN1 NP_700434.1 and rat channel constructs; CaVβ2 mediates association of CLRN1 with the alpha1 interaction domain. These data do not establish CLRN1 itself as a bridging adaptor, and the study reports unsuccessful native auditory-organ immunodetection. No new scaffold, channel, enzyme or process term is inferred. [PMID:29985171]

The displayed human product is P58418-3 (232 residues); P58418-1 and P58418-4 have distinct authenticated sequence changes. Current product labels are preserved exactly. Historical mouse isoform 2 naming does not identify human P58418-1. The human 2009 construct is explicitly NM_174878, and the 2015 human fluorescent transgene is separately distinguished from endogenous zebrafish protein; no all-product assay claim follows. Exact current alternative sequences and the three isoform-specific HuRI partners were reconstructed from official sequence features and matched to fetched FASTAs. [PMID:19423712; PMID:26180195]

Hearing and vestibular roles have positive human clinical and measured animal support. The original human clinical articles remain abstract-only; their detailed family-level tests were not invented. Mouse ABR, DPOAE and vestibular evoked potentials and zebrafish behavioral/electrophysiological experiments supply independent functional context. Normal balance in particular animals or models reflects penetrance and assay context, not a universal absence of vestibular function. Historical PAINT node placement remains unresolved despite this biological corroboration. [PMID:15521980; PMID:15650299; PMID:19414487; PMID:26180195]

Retinal evidence favors a Müller-glial contribution to photoreceptor support. Human and animal transcript data establish cellular expression, whereas failed specific native retinal staining limits subcellular protein claims. Zebrafish low-level glial rescue restores apical structures and protects against light stress; rod/cone expression does not provide the same protection, and excess glial expression can be harmful. The rabbit model supplies independent late retinal disease context, but its proposed CTNNA2 pathway remains an interpretation rather than a demonstrated direct regulatory reaction. These studies strengthen the existing non-core maintenance and vision annotations without generating new process assertions. [PMID:31625146; PMID:40067805; PMID:42390169]

## Cellular evidence and molecular limits (2026-10-11)

The human HEK293 study provides positive membrane, microvillus and lamellipodium localization and expression-dependent actin-rich protrusions in three independent clones. These results remain valid at their assayed scope. Its four-day colony endpoint does not establish controlled self-propelled cell translocation, so the cell-motility assertion alone is marked over-annotated. Neither the cell line nor the immobility of a different native cell type is the basis for this correction. The N48K experiment remains confounded by folding, abundance and delivery changes. [PMID:19423712]

The mouse UB/OC-1 study uses endogenous clarin-1 immunostaining for the actin/tubulin comparison; a separately expressed mouse isoform-2 GFP fusion serves antibody controls. The reported "distinct non-overlapping staining" of clarin-1 and phalloidin is retained alongside positive tubulin overlap and nocodazole-dependent loss of filamentous staining. They measure localization in a different species and cellular model from the human HEK293 expression experiment. Neither paper tests the other's exact result, so the reference findings are CURRENT with a model-specific reconciliation, rather than labeling a valid observation DISPUTED. Mouse auditory deletion and rescue independently support the actin-network role without proving direct actin binding. [PMID:19539019; PMID:19423712; PMID:29985171]

A literature-grounded knowledge gap now records the unresolved molecular operation. The existing process/location core remains, without inventing a scaffold, catalytic activity or direct actin-binding MF. The calcium-channel experiment supports partner association but identifies CaVβ2 as the bridge to the alpha1 interaction domain. [PMID:19423712; PMID:29985171]

The cellular observations above supersede the earlier cell-motility interpretation.

The HuRI authors state that the "function of most individual PPIs remains to be elucidated". The positive pair records therefore establish assay-scoped binding, with physiological roles left open. [PMID:32296183]

All twelve challenged partner-class refinements are retained after checking the exact positive records and official class definitions. Six enzyme partners (MGST3, TMEM86B, CANT1, ZDHHC15, ALG8 and FUT9) have experimentally attributed function or reaction entries in their authenticated UniProt records. SEC22B is a SNARE, ITGAM an integrin subunit, and SLC61A1/SLC34A3 are assigned transmembrane uptake activities. These are class descriptions of the bound protein; no CLRN1 catalytic, transport, recruitment or regulatory activity is inferred. TMPPE has a domain/family and similarity-based cofactor assignment without a comparable experimental FUNCTION or reaction assignment, explaining its conservative generic retention. The underlying individual activity papers were not newly read; their evidence codes are provenance of the official records, not additional primary experiments claimed here.

CCL4L1 and TMPRSS4 retain chemokine- and protease-binding specificity for the mapped protein constructs. Processing, activation, exact clone sequence and contact with the mature functional region remain unresolved. Neither an unsuffixed accession nor an absent fragment feature establishes those properties. Three positive curated records per pair refer to array, pooling and validated Y2H assays, not three independent publications or pair-specific MAPPIT/GPCA tests. The latter were population-level validation in the source. Native colocalization and physiological function remain unestablished for these screen interactions; none creates another core. [PMID:32296183]

## Explicit retirement and public source locators, 2026-10-12

This entry supersedes earlier counting language. The 54 preserved review objects contain **45 active annotations and nine retired representations**. Here, historical means an earlier authored review representation; this does not establish another GOA snapshot. Eight retired rows lack supporting entities that are preserved in their active counterparts. The ninth is an unscoped HuRI aggregate, represented by 26 active named interactions. Retirement changes representation status, not the biological judgment or the positive evidence. No source identifiers, supporting entities, qualifiers, products, references, actions or replacement terms have been merged, deleted or rewritten.

| Retired row (zero-based) | Active successor | Basis |
|---|---|---|
| 0 | 47 | Sound perception IBA; exact source list retained |
| 1 | 53 | Equilibrioception IBA; exact source list retained |
| 2 | 46 | Plasma-membrane electronic mapping |
| 3 | 48 | Sound perception electronic rule |
| 4 | 20–45 | Unscoped binding aggregate; 26 distinct positive pairs |
| 5 | 49 | Microtubule-cytoskeleton donor record |
| 6 | 50 | Trans-Golgi vesicle donor record |
| 7 | 51 | Stereocilium donor record |
| 8 | 52 | Basal-cell donor record |

Each active annotation corresponds to one GOA record, including its supporting entities. The source index records the mapping. The 54 retained objects therefore represent 45 current independent assertions.

The following public source locators identify the experiments underlying the preceding biological summaries.

| Claim in the earlier notes | Public source locator and boundary |
|---|---|
| Human HEK293 surface/actin localization | [PMID:19423712 cache](../../../publications/PMID_19423712.md), full-text Abstract and Results Figure 1 paragraph (line 135); exact short anchors also occur in YAML rows 11/12. |
| Mouse-null hair-bundle disorganization | Same cache, complete full-text Abstract (line 79); this is the mouse in-vivo observation, separate from the human expression experiment. |
| N48K loss of remodeling | Same cache, Results Figure 2 paragraph (line 137) and Figure 5 discussion (lines 157/159); folding, delivery and abundance are confounders, not an isolated catalytic test. |
| Local spreading versus cell motility | Same cache, Results Figure 2 paragraph (line 137), explicitly describing the four-day colony endpoint. The existing motility overannotation judgment remains. |
| Golgi glycan processing | Same cache, enzyme-treatment Methods (line 113) and Results Figure 5A paragraph (line 155); Golgi passage is inferred from the glycan sensitivity pattern. |
| HuRI screen scale and validation | [PMID:32296183 cache](../../../publications/PMID_32296183.md), Results mapping paragraph (line 265); the exact short verification anchor remains in YAML row 4. Study-wide orthogonal validation does not establish pair-specific MAPPIT/GPCA retesting. |

The twelve supported binding-class refinements remain unchanged. They describe the positive tested partner class without asserting a native physiological mechanism or transferring enzyme, transport or regulatory activity to clarin-1.
