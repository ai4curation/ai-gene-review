# unc-13 (C. elegans Munc13, UniProt P27715) - curation notes

## Identity
- Swiss-Prot UNC13_CAEEL, P27715, 2155 aa, ORF ZK524.2; sole worm Munc13 ortholog (vertebrates:
  UNC13A/B/C). Multiple transcripts from alternative splicing and promoters share the C-terminal
  release machinery (C1, C2B, MUN, C2C) but differ N-terminally (UNC-13L carries C2A)
  [PMID:11029047 "These transcripts encode proteins that are identical in their C-terminal regions but that vary in their N-terminal"].
- The null allele deleting all products hatches but dies as a paralyzed L1
  [PMID:11029047 "animals homozygous for this null allele are able to complete embryogenesis and hatch, but they die as paralyzed first-stage larvae"].

## Core biology: active-zone priming factor that makes docked vesicles fusion-competent
- Electrophysiology of unc-13 nulls: normal nervous-system architecture, normal synapse and
  postsynaptic receptor densities, a two- to threefold accumulation of synaptic vesicles, and
  near-complete loss of evoked release at both cholinergic and GABAergic synapses
  [PMID:10526333 "Mutants of unc-13 had normal nervous system architecture"; "evoked release at both GABAergic and cholinergic synapses was almost absent in unc-13 null alleles"].
- Crucially, vesicles still dock morphologically but are not release-competent, assayed by
  calcium-free spontaneous release and hyperosmotic challenge, placing UNC-13 at priming/fusion
  rather than docking
  [PMID:10526333 "Although mutant synapses had morphologically docked vesicles, these vesicles were not competent for release"].
- Independent EM work confirms the reciprocal relationship to UNC-18: unc-13 mutants accumulate
  tethered vesicles while losing docked ones, so priming (UNC-13) is separable from
  UNC-18-dependent tethering
  [PMID:21423527 "In contrast, priming defective unc-13 mutants accumulate tethered vesicles, while docked vesicles are greatly reduced"].
- Localization: the most abundant UNC-13 form is present at most or all synapses
  [PMID:11029047 "The most abundant protein form is localized to most or all synapses."], and UNC-13
  is an active-zone protein whose targeting is independent of ELKS-1
  [PMID:15976086 "ELKS is not required for the localization of UNC-13, another C. elegans active zone protein"].
- Molecular function: the family acts through syntaxin engagement; a WormBase production GO-CAM
  models the worm activity as syntaxin-1 binding at the presynaptic active zone, part of synaptic
  vesicle exocytosis [file:gocams/5b528b1100000489/5b528b1100000489-src.yaml].
- Domain-level regulation: C1 (DAG/phorbol ester), C2B (Ca2+/phospholipid) and a calmodulin-binding
  region make UNC-13 the integration point for second messengers controlling release probability
  [file:worm/unc-13/unc-13-deep-research-falcon.md].

## Dense-core vesicles and secondary/behavioural roles
- UNC-13 also augments dense-core vesicle exocytosis, in a UNC-31/CAPS-dependent manner
  [PMID:18031683 "We also demonstrate that UNC-31 is required for UNC-13-mediated augmentation of DCV exocytosis."].
- unc-13 mutants were used to show that small clear vesicle release is required for the
  cell-nonautonomous longevity signal downstream of neuronal XBP-1s
  [PMID:23791175 "Reduction of small clear vesicle (SCV) release blocked nonautonomous signaling downstream of xbp-1s"].
- unc-13 interacts genetically with egl-30/Galphaq in the control of egg laying and pharyngeal
  pumping, which are behavioural outputs of DAG-regulated release
  [PMID:14704167 "PLCbeta-mediated signaling is likely downstream of EGL-30 with respect to pharyngeal-pumping behavior"].

## Annotations traceable to a linked marker mutation
- GO:0007283 spermatogenesis and GO:0060282 positive regulation of oocyte development (both IGI,
  PMID:25261697) cite fog-3 and rnp-1 as interactors. In that paper unc-13(e1091) appears only as the
  cis-linked LGI marker used to follow fog-3
  [PMID:25261697 "fog-3(q470) unc-13(e1091); rnp-1(ok1549) animals lack sperm but can make tiny underdeveloped oocytes"];
  the germline phenotypes are attributed to fog-3 and rnp-1, and no unc-13 germline experiment is
  reported. These two rows are therefore removed.

## GO decisions (summary)
- Core: syntaxin-1 binding (GO:0017075) at the presynaptic active zone (GO:0048786), driving
  synaptic vesicle priming (GO:0016082) within synaptic vesicle exocytosis (GO:0016079).
- Non-core: dense-core granule priming, calmodulin binding, behavioural (pumping, egg-laying)
  and glutamatergic-transmission terms.
- Synaptic vesicle membrane (IBA) over-annotates the location: worm UNC-13 acts from the
  presynaptic membrane/active zone, not from the vesicle surface.
