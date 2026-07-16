# FAR2 (Fatty acyl-CoA reductase 2) — review notes

UniProt: Q96K12 (FACR2_HUMAN); gene FAR2 (HGNC:25531; synonym MLSTD1, "Male sterility
domain-containing protein 1"); human chromosome 12; 515 aa; EC 1.2.1.84.

## Core biology (grounded in UniProt Q96K12 and cited literature)

FAR2 is the paralog of FAR1. Both are peroxisomal, NADPH-dependent, alcohol-forming fatty
acyl-CoA reductases that reduce a fatty acyl-CoA to the corresponding primary fatty alcohol
with release of CoA:

- UniProt CATALYTIC ACTIVITY (RHEA:52716): "a long-chain fatty acyl-CoA + 2 NADPH + 2 H(+)
  = a long-chain primary fatty alcohol + 2 NADP(+) + CoA ... EC=1.2.1.84"
  [file:human/FAR2/FAR2-uniprot.txt]. Additional VLC and ULC chain-length reactions
  (RHEA:81751, RHEA:81755) are also listed.

Substrate preference (distinguishes FAR2 from FAR1): FAR2 prefers **saturated** C16/C18
acyl-CoA, whereas FAR1 accepts both saturated and unsaturated C16/C18.

- [PMID:15220348 "FAR1 preferred saturated and unsaturated fatty acids of 16 or 18 carbons
  as substrates, whereas FAR2 preferred saturated fatty acids of 16 or 18 carbons."]
- UniProt FUNCTION: "Catalyzes the reduction of saturated but not unsaturated C16 or C18
  fatty acyl-CoA to fatty alcohols" and "A lower activity can be observed with shorter fatty
  acyl-CoA substrates" [file:human/FAR2/FAR2-uniprot.txt].
- Later work (Otsuka et al. 2022) shows FAR2 can also produce very-long-chain and
  ultra-long-chain fatty alcohols, straight or branched: UniProt FUNCTION "Can produce very
  long-chain and ultra long-chain FAls, regardless of whether they have a straight or
  branched chain (PubMed:35238077)" [file:human/FAR2/FAR2-uniprot.txt]. This is the basis of
  the "very long-chain" MF term (GO:0080019) and the additional VLC/ULC RHEA reactions in
  UniProt. Note: PMID:35238077 full text is not cached locally; claims here are taken from
  the UniProt curated summary, which cites it.

## Product/pathway roles

Fatty alcohols made by FAR2 feed wax monoester and ether-lipid (plasmalogen) biosynthesis.

- [PMID:15220348 "The conversion of fatty acids to fatty alcohols is required for the
  synthesis of wax monoesters and ether lipids."]
- UniProt FUNCTION: "Involved in the production of ether lipids/plasmalogens and wax
  monoesters whose synthesis requires FAls as substrates" [file:human/FAR2/FAR2-uniprot.txt].
- Reactome R-HSA-9640463 (Wax biosynthesis): "FAR1 and FAR2 catalyze the reduction of fatty
  acids to fatty alcohols in the peroxisome and AWAT1 and AWAT2 catalyze the reaction of
  fatty alcohols and acyl-CoA in the cytosol to form wax esters" [reactome/R-HSA-9640463.md].

## Localization / topology

Peroxisomal membrane, single-pass (tail-anchored), with a large cytoplasmic N-terminal
catalytic region and a short peroxisomal-lumen C-terminal tail.

- UniProt SUBCELLULAR LOCATION: "Peroxisome membrane ...; Single-pass membrane protein"
  [file:human/FAR2/FAR2-uniprot.txt].
- UniProt topology: TOPO_DOM 1..464 Cytoplasmic; TRANSMEM 465..484; TOPO_DOM 485..515
  Peroxisomal [file:human/FAR2/FAR2-uniprot.txt].
- [PMID:15220348 "Confocal light microscopy indicated that FAR1 and FAR2 were localized in
  the peroxisome."]
- PMID:24108123 primarily characterizes FAR1 topogenesis (peroxisomal tail-anchored protein,
  Pex19p-dependent targeting). FAR2 appears mainly as a comparator ("Far1, but not Far2, was
  preferentially degraded in response to the cellular level of plasmalogens"); the curator's
  IDA to peroxisomal membrane for FAR2 is retained on the basis that the full text (available)
  assays both proteins. Not a plasmalogen-degradation contrast that changes FAR2's location.

## Tissue expression

FAR2 mRNA is restricted; most abundant in eyelid (meibomian glands) and present in brain.

- [PMID:15220348 "The FAR2 mRNA was more restricted in distribution and most abundant in the
  eyelid, which contains wax-laden meibomian glands. Both FAR mRNAs were present in the
  brain, a tissue rich in ether lipids."]
- Meibum relevance (dry eye) is developed in PMID:35238077 (title: "Formation of fatty
  alcohols-components of meibum lipids-by the fatty acyl-CoA reductase FAR2 is essential for
  dry eye prevention"), not cached locally.

## GO term id verification (via OLS)

- GO:0080019 alcohol-forming very long-chain fatty acyl-CoA reductase activity — MF, current.
- GO:0102965 alcohol-forming long-chain fatty acyl-CoA reductase activity — MF, current;
  matches EC 1.2.1.84 and the C16/C18 (palmitoyl/stearoyl-CoA) activity that is FAR2's
  best-characterized reaction.
- GO:1903175 fatty alcohol biosynthetic process — BP, current (candidate; not currently in GOA).
- GO:0008611 ether lipid biosynthetic process — BP, current (candidate).
- GO:0010025 wax biosynthetic process — BP, current.
- GO:0035336 long-chain fatty-acyl-CoA metabolic process — BP, current (substrate metabolism).
- GO:0005778 peroxisomal membrane; GO:0005777 peroxisome — CC, current.

## Evidence-base caveat

Direct human experimental evidence for FAR2 is thinner than for FAR1. The two anchoring
primary papers are PMID:15220348 (abstract only in cache; identifies FAR2 and its substrate
preference/localization/tissue distribution) and PMID:35238077 (not cached; meibum/dry-eye
and expanded chain-length range). PMID:24108123 is chiefly a FAR1 topogenesis study.

## Curation decisions summary

- MF (GO:0080019, GO:0102965): ACCEPT — alcohol-forming fatty acyl-CoA reductase is FAR2's
  core catalytic function; both chain-length-specific children are supported.
- CC (GO:0005778 peroxisomal membrane; GO:0005777 peroxisome): ACCEPT — core localization,
  experimentally supported.
- BP (GO:0010025 wax biosynthetic process; GO:0035336 long-chain fatty-acyl-CoA metabolic
  process): ACCEPT — downstream/substrate processes consistent with the enzymatic role.
- GO:0016491 oxidoreductase activity (TAS Reactome): MARK_AS_OVER_ANNOTATED — correct but a
  high-level parent of the specific reductase MF; the specific alcohol-forming reductase
  terms are preferred.
