# MICU1 (Q9BPX6) — review notes

Journal for the AI review of human MICU1 (mitochondrial calcium uptake 1; originally CBARA1,
"calcium-binding atopy-related autoantigen 1"). 114 GOA rows, 26 distinct GO terms.

## 1. The standing model

MICU1 is an EF-hand Ca2+-binding protein that sits on the intermembrane-space face of the inner
mitochondrial membrane, where it associates with the MCU/EMRE pore to form the uniporter
holocomplex (uniplex) and gates Ca2+ entry into the matrix.

- Founding identification by integrative genomics
  [PMID:20693986 "RNA interference against 13 top candidates highlighted one gene, CBARA1, that we call hereafter mitochondrial calcium uptake 1 (MICU1)."]
  and already then assigned a sensing role
  [PMID:20693986 "MICU1 is associated with the mitochondrial inner membrane and has two canonical EF hands that are essential for its activity, indicating a role in calcium sensing."].
- Gatekeeping (threshold setting)
  [PMID:23101630 "MICU1 interacts with the uniporter pore-forming subunit MCU and sets a Ca(2+) threshold for Ca(2+)(m) uptake without affecting the kinetic properties of MCU-mediated Ca(2+) uptake."],
  [PMID:23101630 "Thus, MICU1 is a gatekeeper of MCU-mediated Ca(2+)(m) uptake that is essential to prevent [Ca(2+)](m) overload and associated stress."].
- Heterodimer as the Ca2+ switch
  [PMID:28615291 "We conclude that cooperative, high-affinity interaction of the MICU1-MICU2 complex with Ca2+ serves as an on-off switch, leading to a tightly controlled channel, capable of responding directly to cytosolic Ca2+ signals."],
  with MICU1 and MICU2 acting in opposite directions
  [PMID:24560927 "At low [Ca(2+)], the dominant effect of MICU2 largely shuts down MCU activity; at higher [Ca(2+)], the stimulatory effect of MICU1 allows the prompt response of mitochondria to Ca(2+) signals generated in the cytoplasm."].
- Confirmed structurally in the holocomplex
  [PMID:32494073 "Here we report cryo-electron microscopic structures of the human mitochondrial calcium uniporter holocomplex in inhibited and Ca2+-activated states."].
- Tissue-specific dimer composition is real: MICU1 homodimers operate in skeletal muscle and kidney
  [PMID:36206740 "Here, we show that skeletal-muscle and kidney uniporters also complex with a MICU1-MICU1 homodimer and that human/mouse cardiac uniporters are largely devoid of MICUs."].

### An internal dispute that GOA already carries

Occlusion vs potentiation. GOA holds three IDA annotations to GO:0019855 calcium channel inhibitor
activity (PMID:32494073, PMID:37036971, PMID:37126688), and the 2023 pair were written explicitly
to settle a "direct clash"
[PMID:37036971 "Supporting the MICU1-occlusion mechanism, patch-clamp demonstrates that purified MICU1 strongly suppresses MCU Ca2+ currents, and this inhibition is abolished by mutating the MCU-interacting K126 residue."],
[PMID:37126688 "Thus, MICU1 restricts the cation flux across the mtCU in the absence of Ca2+, but even in cells with high endogenous MICU1 expression such as HEK, some mtCU seem to lack MICU1-dependent gating."].
Both sides agree MICU1 sets the threshold; they disagree on whether the low-Ca2+ state is physical
occlusion or allosteric potentiation. The occlusion side now has direct patch-clamp support, so the
inhibitor-activity annotations are kept.

## 2. MCU-independent functions — the part that is NOT new

MICU1 already has two published uniporter-independent roles, both in GOA:

- Cristae junction stabilisation and spatial anchoring of the uniplex at the inner boundary membrane
  [PMID:31427612 "Our data show that MICU1 localizes at the inner boundary membrane (IBM) due to electrostatic interaction of its polybasic domain."],
  [PMID:31427612 "Eventually, our findings unveil an essential function of MICU1 in CJ stabilization and provide mechanistic insights of how sophistically MICU1 controls the MCU-Complex while maintaining the structural mitochondrial membrane framework."].
- MICOS-complex formation, explicitly independent of the uniporter
  [PMID:37098122 "We demonstrated that MICU1 was essential for MICOS complex formation and that MICU1 ablation resulted in altered cristae organization, mitochondrial ultrastructure, mitochondrial membrane dynamics, and cell death signaling."],
  [PMID:37098122 "Together, our results suggest that MICU1 is an intermembrane space Ca2+ sensor that modulates mitochondrial membrane dynamics independently of matrix Ca2+ uptake."].

There is also a hard genetic argument that predates all of this: Micu1 null lethality is not rescued
by removing the uniporter
[PMID:42129466 "However, the lethality caused by Micu1 deletion is not rescued by ablating mtCU function through deletion of MCU (Mcu−/− × Micu1−/−)48 or EMRE (Smdt1−/− × Micu1−/−)49, and neither EMRE (Smdt1−/−) nor MCU (Mcu−/−) deletion is lethal, suggesting that MICU1 functions independently of its role in regulating the uniporter."].

So "MICU1 does things without MCU" is established. The 2026 claim is a different and larger one.

## 3. The 2026 metabolon claim — what it actually says

Cohen et al., Nat Metab 2026 (PMID:42129466), from the Elrod lab (the same lab as the 2023 MICOS
paper).

What it demonstrates:
[PMID:42129466 "Here we demonstrate that MICU proteins, the reported gatekeepers of mtCU, function in coordination to impart calcium-dependent regulation to FADH2-dependent mitochondrial dehydrogenases through metabolon formation independently of the mtCU and [Ca2+]m."]
MICU1-specific evidence includes a co-IP with the relevant dehydrogenase
[PMID:42129466 "A. Representative co-IP of MICU1-HA and endogenous GPD2 from HEK 293 cells."].

What it *proposes*:
[PMID:42129466 "We propose that MICU-mediated mitochondrial metabolons are a fundamental system facilitating matching of mitochondrial energy production with cellular demand and is the primary physiological calcium signaling mechanism regulating homeostatic energetics, not mtCU-dependent changes in [Ca2+]m."]
Note the hedging in the body: "Our results **suggest** that this **may be** the primary physiological
calcium signaling mechanism regulating cellular energetics."

### What it does NOT say

It does **not** claim MICU1 has stopped being a gatekeeper. The paper's own framing keeps that intact:
[PMID:42129466 "MICU1 is the primary regulator of mtCU-mediated mCa2+ uptake."]
The model it displaces is the *downstream* dogma that matrix [Ca2+], delivered through the uniporter,
is what activates the matrix dehydrogenases and thereby tunes basal energetics. That dogma is not
itself a MICU1 GO annotation. So the mapping from this paper onto MICU1's annotation set is narrower
than the abstract's rhetoric suggests:

| Claim in PMID:42129466 | Effect on MICU1 GO annotations |
|---|---|
| MICU proteins scaffold a Ca2+-sensitive GPD2/SDH metabolon | **New** function; no existing GO term captures it |
| MICU heterodimerisation is mtCU-independent | Supports existing GO:0046982, no change |
| MICU1 still gates mtCU | Supports GO:0019855, GO:0061891, GO:1990246, GO:0036444 |
| Matrix Ca2+ is not the master regulator of basal metabolism | Not a MICU1 annotation; nothing to retract |

### Scepticism applied

One paper, one lab, no independent replication and no published rebuttal. I checked: a PubMed
search for `MICU metabolon` returns exactly two records, PMID:42129466 and PMID:40678212 — and the
second is the Research Square preprint of the same study, not an independent confirmation. A search
for `MICU1 GPD2` returns nothing else at all. Meanwhile the field has gone on using the gatekeeper
model after publication, e.g. an August 2026 Exp Mol Med study describes the uniporter as one that
[PMID:42557311 "forms a complex with other subunits such as mitochondrial Ca2+ uptake 1 (MICU1), MICU2 or MICU3, acting as gatekeepers and modifiers of the Ca2+ uptake properties of MCU"].
That is not a rebuttal either, but it does show the standing model is still in working use. That asymmetry means the claim is untested, not that it is
accepted. The primacy assertion ("the primary physiological calcium signaling mechanism") is a
proposal about relative importance, which is not the sort of thing a GO annotation should encode
even if it were settled. Accordingly:

- **No existing annotation is downgraded, removed or modified on the basis of this paper.**
- The metabolon scaffolding function is recorded as a `proposed_new_terms` candidate and in
  `suggested_questions`, not folded into `core_functions`.
- The gatekeeper function stays core.

If replication follows, the right GO representation is probably an MF in the enzyme-regulator branch
(regulation of GPD2/SDH activity) plus a `part_of` a named metabolon complex, neither of which exists
yet.

## 4. Legacy and mis-mapped annotations

- **GO:0006952 defense response, TAS, PMID:9806765.** MICU1/CBARA1 was one of four cDNAs pulled from
  an expression library screened with IgE from atopic dermatitis patients
  [PMID:9806765 "The fourth cDNA coded for an IgE autoantigen containing a typical calcium binding motif that occurred in histogenetically different cells and tissues (keratinocytes, muscle, brain)."].
  Being recognised by autoreactive IgE is a property of the patients' immune systems, not a function
  of MICU1. Nothing in that paper assays a defense response performed by the protein. REMOVE.
  UniProt already records this correctly, and in the right slot: `CC -!- ALLERGEN: Causes an allergic
  reaction in human. Binds to IgE from atopic dermatitis (AD) patients.` (MICU1-uniprot.txt line 690).
  An allergen/autoantigen statement is the right representation; "defense response" is not.
- **GO:1900069 regulation of cellular hyperosmotic salinity response, IMP, PMID:26975899.** MICU1 was
  one of five hits in a targeted siRNA screen whose readout was mitoflash frequency
  [PMID:26975899 "In silico analysis and targeted siRNA screening identified four mitoflash activators (MICU1, EFHD1, SLC25A23, SLC25A25) and one mitoflash inhibitor (LETM1) in terms of their ability to modulate mitoflash response to hyperosmotic stress."].
  Hyperosmotic stress was the stimulus used to evoke mitoflashes; the paper is about EFHD1, and
  "salinity" is not what was manipulated. Over-annotation rather than a wrong gene — kept as such,
  since it is an experimental annotation whose full text I did read but whose term mapping
  over-reaches.
- **GO:0072732 cellular response to calcium ion starvation, IDA, PMID:32494073.** This appears to be a
  reading of the Ca2+-free ("inhibited") cryo-EM state as a cellular response to calcium starvation.
  A conformational state of a purified complex in a low-Ca2+ buffer is not a cellular response to
  calcium ion starvation. MARK_AS_OVER_ANNOTATED.
- **GO:0031966 mitochondrial membrane** and **GO:0070509 calcium ion import** and **GO:0034704 calcium
  channel complex** are each the correct-but-general parent of a specific term the gene already
  carries (GO:0005743, GO:0036444, GO:1990246 respectively). MODIFY with the specific replacement.
- **GO:0005515 protein binding × 13.** All IPI; no functional content. MARK_AS_OVER_ANNOTATED per
  project guidance. The interactors themselves (MCU, EMRE, MICU2, MCUR1, SLC25A23, MICU3, UCP2/3)
  are better captured by the complex and heterodimerisation terms that the gene already has.

## 5. Decisions

Disease context (not itself annotated, but it constrains how essential the gene is): biallelic
loss-of-function causes myopathy with extrapyramidal signs, MPXPS, MIM:615673 — early-onset proximal
muscle weakness, raised creatine kinase, learning difficulties and progressive involuntary movement
(UniProt DISEASE block, MICU1-uniprot.txt lines 671–685).

ACCEPT: GO:0005509, GO:0005739, GO:0005743, GO:0005758, GO:0006851, GO:0019855, GO:0036444,
GO:0044284, GO:0046982, GO:0051560, GO:0051561, GO:0061891, GO:1903852, GO:1990246
KEEP_AS_NON_CORE: GO:0042802, GO:0051260, GO:0071277
MODIFY: GO:0031966 → GO:0005743; GO:0034704 → GO:1990246; GO:0070509 → GO:0036444
MARK_AS_OVER_ANNOTATED: GO:0005515, GO:0072732, GO:1900069
REMOVE: GO:0006952
