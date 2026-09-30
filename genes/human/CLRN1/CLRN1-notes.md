# CLRN1 (clarin-1, USH3A; UniProt P58418) — review notes

## Identity and architecture
- Human clarin-1, 232 aa, four-transmembrane (tetraspanin-like) glycoprotein of the clarin family (paralogs CLRN2, CLRN3). Single N-linked glycosylation site at Asn48 (first extracellular loop). UniProt P58418; TCDB 9.A.46.1.1 "the clarin (CLRN) family"; InterPro IPR026748; PANTHER PTHR31548:SF4.
- Biallelic loss-of-function variants cause autosomal-recessive Usher syndrome type 3A (USH3A): post-lingual, progressive sensorineural hearing loss, variable vestibular dysfunction, and rod–cone retinal degeneration (retinitis pigmentosa). Some CLRN1 variants also cause non-syndromic RP61 [UniProt P58418; PMID:21310491].

## Core wild-type function (framing per requester: hair-bundle F-actin organization + trafficking, NOT a member of the USH1 tip-link or USH2 ankle-link complexes)
- Clarin-1 acts as a plasma-membrane-associated organizer of the F-actin cytoskeleton in sensory hair cells, required for stereocilia hair-bundle integrity and efficient mechanotransduction, and (basolaterally) for inner-hair-cell ribbon-synapse maturation.
- Heterologous (HEK293) study: "When expressed in HEK293 cells, clarin-1 localized to the plasma membrane and concentrated in low density compartments distinct from lipid rafts. Clarin-1 reorganized actin filament structures and induced lamellipodia." [PMID:19423712]
- In vivo support that the actin role is physiological: "Consistent with the hypothesized role of clarin-1 in actin organization, F-actin-enriched stereocilia of auditory hair cells evidenced structural disorganization in Clrn1 −/− mice." [PMID:19423712]
- The N48K USH3A mutant (loss of glycosylation) fails the actin-reorganizing function and is degraded/mislocalized: "This actin-reorganizing function was absent in the modified protein encoded by the most prevalent North American Usher syndrome III mutation, the N48K form of clarin-1 deficient in N-linked glycosylation." [PMID:19423712]

### Caveat on the HEK293 readouts
The lamellipodium induction, cell motility, and microvillus enrichment in PMID:19423712 are heterologous-overexpression phenotypes in a non-sensory immortalized cell line. They report an underlying actin-organizing activity but are not the wild-type in-vivo function of clarin-1 (hair cells are not motile and do not make lamellipodia). "These results suggest that wild-type CLRN1 locally activates cellular spreading and an increase in the number of cellular protrusions." [PMID:19423712] Treated here as over-annotations of the core actin-organization function.

## Localization
- Cell/plasma membrane, multi-pass membrane protein [UniProt; PMID:21310491 EXP; PMID:19423712 IDA].
- Stereocilium (hair-bundle) localization — well supported (mouse ortholog; disorganized stereocilia in Clrn1-/-). Core location.
- Basolateral/ribbon-synapse (basal part of cell) localization in inner hair cells [deep-research: Dulon 2018, JCI94351 — mouse].
- Passes through Golgi (Endo H-resistant, PNGase F-sensitive glycan): "Resistance to Endo H f suggests that the N-linked glycan moiety on CLRN1 was processed by Golgi-mannosidase II and passed through the protein quality control mechanism of the Golgi apparatus." [PMID:19423712] — consistent with trans-Golgi trafficking transit (non-core).
- Microtubule cytoskeleton (IEA, Ensembl from mouse ortholog): no biological support; clarin-1 associates with F-actin, not microtubules. Treated as over-annotation.

## Hearing / balance
- Sensory perception of sound: core. USH3A = progressive hearing loss; IMP from Finnish USH3 patients [PMID:15650299]; IBA across clarin family.
- Equilibrioception (vestibular): genuine hair-cell function; variable vestibular dysfunction in USH3A [IMP PMID:15521980; IBA].

## Retina
- Retinal degeneration in USH3A is real, but recent evidence localizes CLRN1 predominantly to Müller glia rather than photoreceptors, implying a non-cell-autonomous, structural/homeostatic support of photoreceptors [deep-research: Xu 2020 J Pathol path.5360; Nonarath 2025 PLoS Genet pgen.1011205]. Photoreceptor-maintenance / light-perception BP annotations (IMP from patient RP phenotype, PMID:15521980) are accepted as non-core.

## Protein interactions
- 27 "protein binding" (GO:0005515) IPI annotations all derive from a single systematic yeast-two-hybrid screen: "A reference map of the human binary protein interactome" (HuRI/HI-III-20) [PMID:32296183]. "yeast two-hybrid (Y2H) represents the only binary PPI assay that can be operated at sufficient throughput to systematically screen the human proteome for binary PPIs." The recovered partners (ALG8, MGST3, SEC22B, ITGAM, various TMEMs, claudin-19, etc.) are largely ER/membrane proteins and do not correspond to the physiologically meaningful partners (harmonin/USH1C, CACNB2/CaV1.3). Bare "protein binding" is uninformative — marked as over-annotated.

## Action summary
- ACCEPT (core): sensory perception of sound (IBA, IEA/ARBA, IMP); equilibrioception (IBA, IMP); actin filament organization (IDA); stereocilium; plasma membrane (IEA, EXP, IDA); basal part of cell.
- KEEP_AS_NON_CORE: photoreceptor cell maintenance; sensory perception of light stimulus; trans-Golgi network transport vesicle.
- MARK_AS_OVER_ANNOTATED: protein binding (x27, HuRI Y2H); microvillus, lamellipodium, positive regulation of lamellipodium assembly, cell motility (HEK293 overexpression); microtubule cytoskeleton (unsupported IEA).
