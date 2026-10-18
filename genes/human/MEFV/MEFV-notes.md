# MEFV (Pyrin / Marenostrin / TRIM20) — review notes

UniProt: O15553. Gene: MEFV. Protein: Pyrin (also marenostrin, TRIM20). Human.

## Domain architecture
- N-terminal PYRIN (PYD/DAPIN) domain (~1-92) — mediates homotypic interaction with ASC/PYCARD PYD for inflammasome assembly.
- bZIP-like / central region; B-box-type zinc finger (ZN_FING 370-412).
- Coiled-coil (COILED 413-442) — oligomerization.
- C-terminal B30.2/SPRY (PRY-SPRY) domain (~580-775) — substrate/interaction module; many FMF mutations cluster here.
- Member of the TRIM (tripartite motif) family: RING-like/B-box/coiled-coil; pyrin lacks a canonical RING but is classed as TRIM20.
[file:human/MEFV/MEFV-uniprot.txt FT DOMAIN/ZN_FING/COILED records]

## Core function (synthesized)
Pyrin is an innate-immune inflammasome sensor. It detects perturbation of RhoA GTPase activity (caused by bacterial toxins/effectors that inactivate RhoA) indirectly, via loss of PKN1/PKN2-mediated phosphorylation at Ser208/Ser242 and consequent release of inhibitory 14-3-3 proteins, leading to pyrin inflammasome assembly: pyrin nucleates PYCARD/ASC speck (pyroptosome) formation, activating caspase-1, driving IL-1beta/IL-18 maturation and pyroptosis.
[file:human/MEFV/MEFV-uniprot.txt "innate immune sensor that triggers PYCARD/ASC specks formation, caspase-1 activation, and IL1B and IL18 production (PubMed:16037825, PubMed:27030597, PubMed:28835462)"]
[PMID:27030597 "Familial autoinflammation with neutrophilic dermatosis reveals a regulatory mechanism of pyrin activation" — PKN/14-3-3 phosphoregulation; FMF/PAAND mutations]
[PMID:16037825 "Cryopyrin and pyrin activate caspase-1, but not NF-kappaB, via ASC oligomerization"]

## Microtubule dependence
Pyrin inflammasome activation requires microtubules in WT; FMF mutations lift the obligatory microtubule requirement.
[PMID:27911804 "Familial Mediterranean fever mutations lift the obligatory requirement for microtubules in Pyrin inflammasome activation"]

## Autophagy / negative-regulatory role (TRIM20 precision autophagy)
Pyrin (TRIM20) also acts as a selective-autophagy receptor that targets inflammasome components NLRP3, NLRP1 and pro-caspase-1 for autophagic degradation, serving as a platform that assembles ULK1, Beclin-1/BECN1, ATG16L1 and ATG8/LC3 family members ("precision autophagy"). This restrains excessive IL-1beta/IL-18. FMF mutations impair this autophagic function.
[PMID:26347139 "TRIM20 targets the inflammasome components, including NLRP3, NLRP1, and pro-caspase 1, for autophagic degradation ... The autophagic function of TRIM20 is affected by mutations associated with familial Mediterranean fever."]
[file:human/MEFV/MEFV-uniprot.txt "Acts as an autophagy receptor for the degradation of several inflammasome components, including CASP1, NLRP1 and NLRP3, hence preventing excessive IL1B- and IL18-mediated inflammation"]
[PMID:25127057 "TRIM proteins regulate autophagy and can target autophagic substrates by direct recognition"]

## Interactions
- PYCARD/ASC (Q9ULZ3) via PYD — inflammasome assembly. [PMID:11498534; PMID:25006247; PMID:16037825]
- PSTPIP1 (O43586) via B-box — recruits PSTPIP1; PSTPIP1 mutants (PAPA syndrome) engage pyrin to activate ASC pyroptosome. [PMID:17964261; PMID:19584923]
- CASP1 (P29466) via B30.2 — modulates IL-1beta. [PMID:16785446]
- 14-3-3 proteins (P27348, P31946, P61981, P62258, P63104, Q04917) — bind phospho-pyrin, hold it inactive. [PMID:27030597]
- Homotrimer / identical protein binding. [PMID:17964261; PMID:25006247; PMID:22829933]

## Localization
Cytoplasm/cytoskeleton (associates with microtubules and actin), perinuclear filaments and lamellar ruffles/lamellipodium; colocalizes with ASC specks; autophagosome (during precision autophagy). Isoform 2 (lacking exon 2) translocates to the nucleus.
[file:human/MEFV/MEFV-uniprot.txt SUBCELLULAR LOCATION]
[PMID:11468188 "associates with microtubules and colocalizes with actin filaments"]
[PMID:11115844 nuclear translocation of an alternatively spliced isoform]

## Disease
Recessive gain-of-function MEFV mutations (mostly B30.2/SPRY) cause Familial Mediterranean Fever (FMF). Specific Ser-site mutations (S242R, E244K) cause autosomal-dominant Pyrin-Associated Autoinflammation with Neutrophilic Dermatosis (PAAND). [PMID:27030597]

## Annotation review judgments
- Core (ACCEPT): inflammasome sensor / ASC speck (pyroptosome) assembly (GO:1904270, GO:0061702), positive regulation of IL-1beta production (GO:0032731 IDA), regulation of IL-1beta production (GO:0032651 IMP), pyroptotic inflammatory response (GO:0070269), pattern recognition receptor signaling (GO:0002221), innate immune response (GO:0045087), cytoplasm/cytosol localization.
- KEEP_AS_NON_CORE: autophagy receptor role (GO:0010508 positive regulation of autophagy; negative regulation of IL-1beta/NLRP3 assembly GO:0032691, GO:1900226, GO:1900016) — real but the secondary/regulatory arm; response to type II interferon (GO:0034341); actin binding, microtubule/cytoskeleton localizations; nucleus (isoform-specific); ruffle/lamellipodium; plasma membrane (HPA IDA); zinc ion binding (B-box); FMF clinical-correlate negative-regulation terms (PMID:20041150, PMID:16403826).
- MARK_AS_OVER_ANNOTATED / REMOVE: ubiquitin protein ligase activity (GO:0061630 IBA) — pyrin lacks a canonical functional RING and is not established as an active ubiquitin ligase; this is a TRIM-family phylogenetic over-propagation. Mark over-annotated (defer rather than hard REMOVE, since TRIM27 paper PMID:22829933 in refs concerns a paralog and family E3 activity is debated). regulation of gene expression (GO:0010468 IBA) — generic TRIM-family propagation, not a core pyrin function -> MARK_AS_OVER_ANNOTATED.
- protein binding (GO:0005515) — KEEP_AS_NON_CORE (uninformative bare term, but records real interactions).
- response to other organism (GO:0051707 IEA/ARBA) — KEEP_AS_NON_CORE (consistent with sensing of bacterial toxin effects).

## 2026 update: CDC42 as a direct pyrin ligand

Added during the contested-functions pass
(`projects/FUNCTION_KNOWLEDGE_GAPS/contested-functions-2025-2026.md`). The review as it stood was
built entirely on the canonical indirect model — RhoA inactivation removes PKN1/2-mediated
phosphorylation, 14-3-3 is released, pyrin activates — and contained no mention of CDC42.

Three simultaneous *Sci Immunol* papers (2026-08-07) plus a commentary report a direct
protein-protein interaction instead:

[PMID:42566498 "We demonstrate that the region surrounding residue T43 of CDC42 interacts with the
carboxyl-terminal B30.2 domain of pyrin and regulates its localization and activation."] and
[PMID:42566498 "These findings identify CDC42 as a pyrin ligand and provide critical insights into
the role of the pyrin B30.2 domain in inflammasome activation, suggesting dual regulation of pyrin
by two RHO family GTPases, RHOA and CDC42."]

A genotype-first screen of 265 missense MEFV variants adds an important qualification — the
mechanism is not universal:
[PMID:42566500 "We found that classical familial Mediterranean fever (FMF)-related variants bind
tightly to CDC42 to induce pyrin hyperactivation, whereas certain non-FMF variants induce pyrin
hyperactivation independently of CDC42, indicating involvement of multiple pathways in pyrin
activation."]

Companion papers: PMID:42566497 (CDC42 M45L variant), PMID:42566502 (commentary, "Misfirin' pyrin").

### What was changed
- **NEW** `GO:0031267` small GTPase binding (IDA). GO has no CDC42- or Rho-specific binding MF term,
  so this is the most specific applicable term — worth noting as a minor ontology gap.
- **NEW** `GO:0141087` positive regulation of inflammasome-mediated signaling pathway (IDA), to carry
  the direction of effect that the generic regulation term cannot.
- A third `core_functions` entry for the CDC42-binding function, explicitly stating it sits
  *alongside* rather than replacing the RhoA/PKN route.
- `description` extended with the dual-GTPase mechanism.

### Ontology gap proposed
GO has dedicated complex terms for the NLRP1 (GO:0072558), NLRP3 (GO:0072559), NLRP6 (GO:0140738),
CARD8 (GO:0140634), AIM2 (GO:0097169) and IPAF (GO:0072557) inflammasomes but **none for the pyrin
inflammasome**, so MEFV can only be annotated to regulation of *other* inflammasomes. Added a
`proposed_new_terms` entry for "pyrin inflammasome complex" under GO:0061702.

### Open question
Whether CDC42 binding is an additional input alongside the RhoA/PKN1/2/14-3-3 route or supersedes
part of it, and by what route the non-FMF variants hyperactivate pyrin CDC42-independently.
