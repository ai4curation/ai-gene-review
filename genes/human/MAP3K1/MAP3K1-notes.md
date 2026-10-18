# MAP3K1 (MEKK1) curation notes

UniProt Q13233; 1512 aa; STE Ser/Thr kinase family, MAP3K subfamily. Kinase domain 1243-1508
(active site D1369); SWIM zinc finger 338-366; RING/PHD zinc finger 443-492; TOG domain ~542-888;
caspase-3 site at Asp878 separating the N-terminal regulatory half from the C-terminal kinase.

## Kinase function (core)

- Phosphorylates MKK4/SEK1/JNKK1 to activate SAPK/JNK:
  [PMID:7997270 "We find that MEKK regulates a new signalling cascade by phosphorylating an SAPK activator, SEK1 which in turn phosphorylates and activates SAPK."]
- MKK4 is the preferred substrate in vitro, with a stable direct MEKK1:MKK4 complex:
  [PMID:9808624 "Figure 2 B shows that JNKK1 is the preferred substrate for MEKK1."]
  [PMID:9808624 "As purified recombinant MEKK1 and JNKK1 also form a stable complex, the interaction between the two proteins is direct."]
- MKK7 is a weaker substrate; MKK3/MKK6 (p38 arm) also activated:
  [PMID:9639556 "MEKK1 activates SKK1/MKK4 more efficiently than MLK2, but barely activates SKK4/MKK7."]
  [PMID:9639556 "MLK2 and MEKK1 also activated SKK2/MKK3 and SKK3/MKK6, the direct upstream activators of SAPK2a/p38."]
- ERK arm (MKK1) is context dependent; low-level expression favours JNK:
  [PMID:9808624 "These results confirmed that MEKK1 preferentially activates JNK1 and to a lesser extent p38α, but is ineffective in ERK2 activation."]
  [PMID:12456688 "MEKK1 phosphorylates and activates MKK1 and MKK4, leading to ERK1/2 and JNK activation."]
- IKK activation (NF-kB) — Reactome R-HSA-933530: "MEKK1 phosphorylates Ser-176 and Ser-180 in IKKA and Ser-177 and Ser-181 in IKKB activation loop"
  (TAS; the underlying primary papers are not cached here). IKKs are not MAP2Ks, so this output is not strictly
  "MAP kinase kinase kinase activity", but the term remains correct for the gene.
- Activation mechanism: oligomerisation-induced autophosphorylation, promoted by GCK (MAP4K2) and TRAF2:
  [PMID:11784851 "Autophosphorylation within the MEKK1 kinase domain activation loop is required for activation."]
  [PMID:11784851 "Here we show that endogenous GCK and MEKK1 associate in vivo."]
- Negative regulation by STK38 via direct interaction with the catalytic domain:
  [PMID:17906693 "STK38 negatively regulates the activation of MEKK1/2 by direct interaction with the catalytic domain of MEKK1/2"]
- Kinase-dead MEKK1 blocks TNF- and EGF-induced JNK activation (receptor-coupled signalling):
  [PMID:9808624 "the activation of HA–JNK2 by TNF or epidermal growth factor (EGF) was inhibited almost completely by coexpression of catalytically inactive ΔMEKK1(KM)."]

## E3 ubiquitin ligase function (core, unusual among MAP3Ks)

- PHD/RING domain ubiquitinates ERK2 [PMID:12049732 "The PHD domain of MEKK1, a RING finger-like structure, exhibited E3 ubiquitin ligase activity toward ERK2 in vitro and in vivo."]
- c-Jun ubiquitination/degradation under osmotic stress [PMID:17101801 "ubiquitination-dependent degradation by the PHD/RING finger domain of MEKK1, which exhibited E3 ubiquitin ligase activity toward c-Jun in vitro and in vivo."]
- Self-ubiquitylation inhibits kinase output [PMID:12456688 "MEKK1 ubiquitylation is inhibited by mutation of cysteine 441 to alanine (C441A) within the PHD."]
- K63 chains on TAB1 with UBE2N (mouse ES cells, abstract only) [PMID:25260751 "The MEKK1 PHD binds and mediates the transfer of Lys63-linked poly-Ub, using the conjugating enzyme UBE2N, onto TAB1 to regulate TAK1 and MAPK activation by TGF-β and EGF."]

## TOG domain / tubulin binding

- [PMID:32817551 "Here we show that MEKK1 contains a previously unidentified tumor overexpressed gene (TOG) domain."]
- ITC: 1:1 binding to free tubulin, KD 0.63 uM; no binding to taxol-stabilised microtubules
  [PMID:32817551 "clearly shows 1:1 stoichiometric binding with a calculated dissociation constant KD = 0.63 μM"].
  Not currently in GOA -> proposed as NEW GO:0015631 tubulin binding.

## Localization

- Cytosolic signalling protein (IBA, Reactome TAS). Partial recruitment to tight junctions by MarvelD3:
  [PMID:24567356 "MarvelD3 recruited MEKK1 to junctions, leading to down-regulation of JNK phosphorylation"] —
  a regulatory sequestration site, kept as non-core.

## Scaffolds / interactors (protein binding IPI rows)

- MAP2K4 (PMID:9808624) -> direct, functional; MODIFY to GO:0031434 MAPKK binding.
- MAP4K2/GCK (PMID:11784851) -> direct in vitro binding of kinases; MODIFY to GO:0019901 protein kinase binding.
- DCAF7/Han11 (PMID:20940704, PMID:14743216) and FLNB (PMID:19270716) are scaffolds that bind MEKK1; the
  informative function belongs to the scaffold, not MEKK1 -> REMOVE generic protein binding.
- BRAF (PMID:16810323, PMID:16888650): cached full texts do not mention MEKK1 at all (probably IntAct
  large-scale/supplementary data) -> REMOVE generic protein binding (does not mean interaction is false).

## Odd annotation

- GO:0071260 cellular response to mechanical stimulus, IEP, PMID:19593445 (BAD / prostate cancer paper).
  Cached full text does not mention MEKK1/MAP3K1 or mechanical stimulation; the same PMID supports the
  same IEP term on FAS, GADD45A, MAP2K4, MAP3K2, MAPK8, TNFRSF1A, suggesting a batch UniProt annotation
  whose basis is not visible to us -> UNDECIDED.

## Disease

- 46,XY DSD (SRXY6), gain-of-function-like alleles altering p38/ERK phosphorylation and RHOA binding
  [PMID:21129722 "these mutations altered the phosphorylation of the downstream targets, p38 and ERK1/2, and enhanced binding of RHOA to the MAP3K1 complex."]
- Frequent truncating mutations in luminal breast cancer (deep research, falcon).
