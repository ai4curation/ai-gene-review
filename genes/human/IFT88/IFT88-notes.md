# IFT88 notes (human, Q13099)

## Deep research status
DRSTATUS

## Summary
IFT88 (Tg737/polaris) is a TPR-repeat IFT-B1 core subunit. Discovery: Chlamydomonas IFT88 mutant lacks flagella [PMID:11062270 "The phenotype of this mutant is normal except for the complete absence of flagella."]; mouse Tg737 mutants have short kidney cilia and PKD [PMID:11062270 "We show that the primary cilia in the kidney of Tg737 mutant mice are shorter than normal."]

- Localization: base + within cilia in RPE1 [PMID:28428259 "In the majority of control RPE1 cells, IFT88 is found within cilia as well as at the ciliary base (Figure 5J; also see Figure 5O)."]; colocalizes with RABL2B at ciliary base [PMID:28625565 "SIM revealed that IFT88 almost perfectly colocalized with RABL2B at the ciliary base (Fig."]; centrosome pool [PMID:25564561 "To test this, we showed that CENP-F colocalised with IFT88 and KIF3B at the centrosome of asynchronous NIH 3T3 fibroblasts (figure 5A, B) and along the ciliary axonemes of ATDC5 cells (chondrocytes) (figure 5C)"]
- Anterograde role: [PMID:30388400 "IFT88 RNAi (targeting an essential protein for anterograde IFT)"]
- Interactors (ENTR1/SDCCAG3, CENPF, LRRC56, HuRI Y2H hits) are recorded as generic protein binding; removed as uninformative.

## Key curation decisions
- ACCEPT: IFT-B complex, cilium/basal body/ciliary tip/non-motile cilium, intraciliary (anterograde) transport, cilium assembly.
- REMOVE: protein binding (11 rows), IFT-A IDA (PMID:26980730), response to silicon dioxide (IEA from rat IEP).
- MODIFY: positive regulation of cilium assembly (IMP PMID:17604723) and regulation of cilium assembly (IEA/ISS) -> cilium assembly; IFT88 is a structural IFT-B subunit, not a regulator.
- KEEP_AS_NON_CORE: centrosome/centriole, cytosol (incl. Reactome aggrephagy events, where IFT88 is depicted as a misfolded ciliary substrate), sperm structures, kidney development, inner-ear stereocilium organization, autophagosome assembly regulation, kinesin binding (IBA; kinesin-2 contacts mapped mainly to IFT-B2).

## HPA cilium atlas vs module role
HPA v25 (projects/HUMAN_PROTEIN_ATLAS/cilium_life_cycle/member_evidence.md): Primary cilium (Supported), Basal body (Supported), Centriolar satellite (Approved); main locations End piece, Microtubules, Primary cilium. The atlas [PMID:41005307 "We employed antibody-based spatial proteomics to expand the Human Protein Atlas to primary cilia."] thus places IFT88 exactly where an anterograde IFT-B subunit is expected (ciliary base + shaft), and the GO_REF:0000052 rows (cilium, ciliary basal body) are accepted. The centriolar satellite call is a minor, non-core pool. The sperm "end piece" main location is consistent with IFT in flagella.
Module (stage 4, axoneme extension by IFT) assigns IFT88 as an IFT-B subunit with complex function "IFT cargo adaptor", processes intraciliary anterograde transport + cilium assembly. Core functions agree on process, location and complex. Mild disagreement: no cargo-binding activity is established for IFT88 itself (it is a scaffold within IFT-B1), so the review asserts no MF; the "cargo adaptor" label is a property of the complex, best grounded on IFT81/IFT74 (tubulin) and other cargo-binding subunits.

## Shared IFT background

- IFT particles are built from two biochemically distinct complexes, IFT-A and IFT-B [PMID:15955805 "IFT particles contain multiple copies of two distinct protein complexes, A and B, which contain at least 6 and 11 protein subunits, respectively."]
- Motors: kinesin-2 drives anterograde and dynein-2 drives retrograde movement [PMID:15955805 "Anterograde movement of particles away from the cell body is mediated by kinesin-2, whereas retrograde movement away from the flagellar tip is powered by cytoplasmic dynein 1b/2."]
- IFT-B core vs peripheral: high-salt core contains IFT88, IFT81, IFT74/72, IFT52, IFT46, IFT27 [PMID:15955805 "revealing a 500-kDa core that contains IFT88, IFT81, IFT74/72, IFT52, IFT46, and IFT27."]; IFT172 is peripheral [PMID:15955805 "This result demonstrates that the complex B subunits, IFT172, IFT80, IFT57, and IFT20 are not required for the core subunits to stay associated."]
- Human IFT-B architecture by VIP: 10 core + 6 peripheral subunits [PMID:26980730 "we determined the overall architecture of the IFT-B complex, which can be divided into core and peripheral subcomplexes composed of 10 and 6 subunits, respectively."]
- IFT-B is the train backbone [PMID:36354106 "The IFT-B complex constitutes the backbone of polymeric IFT trains carrying cargo between the cilium and the cell body."]; IFT-B1 carries cargo sites, IFT-B2 binds inactive dynein-2 [PMID:36354106 "The IFT-B complex organizes into IFT-B1 and IFT-B2 parts with binding sites for ciliary cargo and the inactive IFT dynein motor, respectively."]
- Directionality: [PMID:27932497 "Intraflagellar transport (IFT)-A and -B complexes mediate retrograde and anterograde ciliary protein trafficking, respectively."] — but IFT-A also mediates ciliary entry of GPCRs [PMID:27932497 "Thus the data presented here demonstrate that the IFT-A complex mediates not only retrograde trafficking but also entry into cilia of GPCRs."]

## GOA curation issue common to all IFT-B subunits

Every IFT-B subunit annotated from PMID:26980730 (Katoh et al. 2016, an IFT-B architecture paper) carries an IDA to GO:0030991 *intraciliary transport particle A*. This contradicts the paper's own content (which supports the GO:0030992 IFT-B IPI rows from the same paper) and the established biochemistry. Marked REMOVE as a genuinely contradicted claim (likely batch term-selection error), not as second-guessing assay data.
