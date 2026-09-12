# IBSP review notes

## Research provenance

Falcon deep research was attempted and failed with HTTP 402; the configured Perplexity-lite fallback failed with HTTP 401. No provider-named output was retained. The review instead uses the reviewed UniProt P21815 record, QuickGO annotation metadata, the local Reactome record, cached primary publications, and manual literature searches. The synthesis is recorded in IBSP-deep-research-manual.md.

## Core biology

IBSP encodes bone sialoprotein, a highly modified secreted SIBLING-family extracellular-matrix protein. It is abundant among the noncollagenous proteins of bone, binds hydroxyapatite with high affinity, and contains an RGD integrin-binding motif. Human bone-derived and recombinant BSP directly bind hydroxyapatite and support cell attachment [PMID:11459848 "The affinity for hydroxyapatite was higher for bone-derived BSP than for recombinant BSP."]. Native BSP and an internal fragment also inhibit seeded hydroxyapatite crystal growth, showing that mineral binding can influence crystal behavior rather than serving only as passive retention [PMID:9258751 "Both native BSP and a 47 kD fragment of UMR-BSP (Fragment 1 approximately 133A- approximately 265Y) are more potent inhibitors of seeded hydroxyapatite crystal growth"].

Human developmental localization places BSP in mature osteoblasts, osteocytes, osteoclasts, hypertrophic chondrocytes, and bone matrix, but not immature osteogenic precursors [PMID:1818768 "Both protein and mRNA were found in mature, bone-forming cells but not in their immature precursors."]. Mouse Ibsp knockout produces delayed primary ossification and lower cortical mineral density, supporting conserved involvement in bone formation and mineralization [PMID:24816232 "lack of BSP alters long bone growth and membranous/cortical primary bone formation and mineralization"].

## Integrin-mediated cell attachment and migration

The RGD-containing region binds alpha-V/beta-3 integrin. Peptide substitution or truncation strongly changes osteoblast-like cell attachment [PMID:24103036 "replacement of the RGD (arg-gly-asp) peptide moiety with peptide KAE (lys-ala-glu) resulted in a dramatic loss of cell-attachment activity"]. Direct cell assays show BSP supports alpha-V/beta-3-dependent adhesion and migration of osteoblastoid, endothelial, and tumor cells [PMID:10640428 "alpha(V)beta(3)-mediated migration of HUVEC or osteoblastic cells to BSP was substantially enhanced by stimulation"]. Thus integrin binding, cell adhesion, and positive regulation of cell adhesion are core; positive regulation of cell migration is a justified additional process.

In glioblastoma models, perivascular IBSP also promotes tumor-cell migration and growth [PMID:36261010 "IBSP, enhances tumor growth and promotes the migration of GTCs along the vasculature"]. This is strong context-specific biology but is not used to redefine the skeletal core function.

## Complement evasion

BSP binds complement factor H after initial attachment to alpha-V/beta-3 and protects tumor cells from complement-mediated lysis [PMID:10747989 "Recombinant OPN and BSP can protect murine erythroleukemia cells from attack by human complement"]. Negative regulation of complement-dependent cytotoxicity is proposed as a non-core experimental annotation. The generic protein-binding annotation from this paper is replaced with integrin binding; no current GO molecular-function term specifically captures factor H binding.

## High-throughput and transferred annotations

The PMID:16210410 abstract describes a membrane-enriched proteomic survey during osteoblast differentiation but does not identify IBSP or expose the gene-specific quantitative result. Because the full text was not available and the experimental curator may have seen gene-level evidence absent from the abstract, osteoblast differentiation and membrane are left UNDECIDED rather than removed.

The HuRI interactions with FAM9B and FXYD3 come from binary interaction screening and use the uninformative protein-binding term. They lack an established endogenous mechanism and are marked over-annotated.

The vesicle ISS traces through rat BSP to direct detection in isolated growth-plate matrix vesicles (PMID:18758911). The biology is plausible and conserved, but extracellular vesicle is more informative than the generic vesicle term, so the annotation is modified.

The cellular response to growth factor stimulus transfer ultimately reflects experimentally regulated mouse Ibsp expression. It is kept as non-core because it describes regulation of IBSP expression rather than the direct molecular action of the protein.

## Annotation decisions

| Annotation group | Decision |
|---|---|
| extracellular matrix organization, IBA | ACCEPT |
| bone mineralization, IBA | ACCEPT |
| ossification, IEA | MODIFY to bone mineralization |
| extracellular region, IEA | MODIFY to extracellular matrix |
| cell adhesion, IEA | MODIFY to positive regulation of cell adhesion |
| protein binding, HuRI | MARK_AS_OVER_ANNOTATED |
| non-collagenous component of interstitial matrix | ACCEPT |
| structural molecule activity | MODIFY to integrin binding |
| small molecule binding | MODIFY to hydroxyapatite binding |
| protein binding, factor H/integrin paper | MODIFY to integrin binding |
| osteoblast differentiation, HDA | UNDECIDED |
| membrane, HDA | UNDECIDED |
| integrin binding, IMP | ACCEPT |
| positive regulation of cell adhesion, IMP | ACCEPT |
| extracellular region, ISS | ACCEPT |
| cell adhesion, ISS | ACCEPT |
| extracellular matrix organization, ISS | ACCEPT |
| vesicle, ISS | MODIFY to extracellular vesicle |
| cellular response to growth factor stimulus, ISS | KEEP_AS_NON_CORE |
| extracellular region, Reactome TAS | ACCEPT |

## Open questions

- Which post-translational modifications determine whether BSP nucleates, inhibits, or merely binds hydroxyapatite under physiological conditions?
- How much of the Ibsp-null skeletal phenotype is due to direct mineral-phase control versus integrin signaling to osteoblasts and osteoclasts?
- Is extracellular-vesicle carriage of human IBSP a regulated delivery mechanism in bone, or only a transferred rodent observation?
- Does factor H recruitment by IBSP serve a normal placental or bone function, or mainly a tumor-associated complement-evasion mechanism?

