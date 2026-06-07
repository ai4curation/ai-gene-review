# PYR1 (Abscisic acid receptor PYR1 / RCAR11) — curation notes

UniProt: O49686 (PYR1_ARATH); locus AT4G17870; 191 aa; PE 1 (protein level).
Family: PYR/PYL/RCAR intracellular ABA receptor family; START/Bet v1-like (helix-grip) fold.

## Core biology

PYR1 is the founding member of the PYR/PYL/RCAR family of intracellular abscisic
acid (ABA) receptors. It is a soluble cytosolic/nuclear protein that, upon binding
ABA, binds to and inhibits clade-A type-2C protein phosphatases (PP2Cs; ABI1, ABI2,
HAB1, AHG3/PP2CA), which are negative regulators of ABA signaling. Inhibition of the
PP2Cs releases SnRK2 kinases (e.g. OST1/SnRK2.6) from inhibition, allowing downstream
ABA responses such as stomatal closure, germination inhibition and drought tolerance.

- ABA receptor / direct ABA binding: [PMID:19407142 "we show that ABA binds to PYR1, which in turn binds to and inhibits PP2Cs"]; ABA binds within a large internal cavity [PMID:19898494 "the crystal structure of Arabidopsis thaliana PYR1, which consists of a dimer in which one of the subunits is bound to ABA"]; [PMID:19933100 "ABA binds directly to PYR1 within a large internal water-filled cavity"].
- PP2C inhibition (MF): [PMID:19407142 "PYR/PYLs are ABA receptors functioning at the apex of a negative regulatory pathway that controls ABA signaling by inhibiting PP2Cs"]; in vitro inhibition IC50 ~125 nM [PMID:19407142 "(+)-ABA acts as a potent saturable inhibitor of phosphatase activity in the presence of PYR1 (IC50 = 125 nM)"]; [PMID:23844015 "dimeric PYLs ... then bound and inhibited the group A protein phosphatases type 2Cs (PP2C)"].
- Dual stereoisomer binding: [PMID:23844015 "Steric hindrance and hydrophobic interaction are the two key factors in determining the stereospecificity"]; PYR1 can be activated by both (-)-ABA and (+)-ABA (UniProt FUNCTION, ECO:0000269|PubMed:23844015).
- Homodimer: [PMID:19933100 "The crystallographic structure reveals an alpha/beta helix-grip fold and homodimeric assembly, verified in vivo by coimmunoprecipitation"]; [PMID:19898494 "consists of a dimer in which one of the subunits is bound to ABA"]. Monomerizes upon CARK-mediated phosphorylation (UniProt SUBUNIT; [PMID:35388459]).
- Receptor activity / signaling pathway: [PMID:19624469 "PYL5 is a cytosolic and nuclear ABA receptor that activates ABA signaling through direct inhibition of clade A PP2Cs"] (PYL5; mechanism shared by PYR1).
- Drought tolerance: [PMID:29970817] RCAR11 (=PYR1) overexpression increases drought tolerance.

## Mechanism / structure

- Gate-latch-lock mechanism: [PMID:19898420 "A gate-latch-lock mechanism for hormone signalling by abscisic acid receptors"]; ABA-induced loop closure (Pro-Cap "gate", Leu-Lock "latch") creates the PP2C-docking surface. UniProt MOTIF: gate loop 85-89, latch loop 115-117. SITE 88 and 152 involved in PP2C interaction.
- Thermodynamic switch / monomer-dimer modulates ABA sensitivity: [PMID:21847091]. ComplexPortal CPX-1620 "PYR1 ABA receptor complex" -> GO:0062049 protein phosphatase inhibitor complex.

## Subcellular location

PYR1 is fundamentally cytosolic/nuclear; membrane/vacuole localizations are transient
and tied to regulatory degradation, not the catalytic site of action.
- Cytoplasm/cytosol: UniProt SUBCELLULAR LOCATION Cytoplasm (PMID:35388459), cytosol (PMID:29928509). [PMID:19624469 "PYL5 is a cytosolic and nuclear ABA receptor"].
- Nucleus: UniProt (ECO:0000269|PubMed:25465408); binds CARs both at plasma membrane and in nucleus.
- Plasma membrane: transient/CAR- and RSL1-dependent. [PMID:25465408] CAR proteins mediate Ca2+-dependent recruitment of PYR/PYLs to the PM; [PMID:25330042 "the RSL1-PYL4 and RSL1-PYR1 interaction is localized to plasma membrane"].
- Vacuole / plant-type vacuole membrane: transient, RSL1/FREE1-mediated degradation route. [PMID:27495812] FREE1 delivers ubiquitylated receptors to the vacuolar degradation pathway; UniProt Note "Localized transiently in the vacuole when in complex with RSL1".

## Protein interactions (the basis of "protein binding" IPI annotations)

These are functionally meaningful but the bare GO:0005515 term is uninformative; the
specific functions are better captured by other MF terms already annotated:
- PP2Cs ABI1/ABI2/HAB1/AHG3 (P49597, O04719, Q9CAJ0, ...): PMID:19407142, 19874541, 19898420, 19898494, 20729862, 25652827, 32612234 -> GO:0004864 protein phosphatase inhibitor activity / GO:0019207 kinase regulator activity.
- AIP1 (Q9LNW3, HONSU PP2C): PMID:32612234 -> PP2C inhibition.
- TCP19 (Q9LT89): PMID:32612234 (hormone signal-integration network).
- CARs / CAR1, CAR4 (Q9FHP6, Q9LVH4): PMID:25465408, 26719420 -> PM recruitment.
- CARK1/CARK6 and CARK2/4/5/7/11 (Q9LUT0, Q9ZW72, B9DFG5, F4HWU0, P93749, Q8H1G6, Q9M1Q2): PMID:29928509, 30967269, 35388459 -> kinase-mediated phosphorylation of PYR1 (PYR1 is the substrate). T78 phosphorylation by CARK1 stabilizes PYR1 and enhances inhibition of ABI1 [PMID:29928509].
- RSL1 E3 ligase (F4ITM1): PMID:25330042 -> GO:0044389 ubiquitin-like protein ligase binding (already a separate, more informative annotation).
- FREE1/FYVE1 (Q9ASS2): PMID:27495812 -> vacuolar degradation route.
- PYR1 self (O49686): PMID:19898494, 21847091 -> GO:0042802 identical protein binding / GO:0042803 homodimerization.

## Curation decisions summary

- Core MF: ABA binding (GO:0010427), protein phosphatase inhibitor activity (GO:0004864),
  signaling receptor activity (GO:0038023), protein homodimerization (GO:0042803).
- Core BP: abscisic acid-activated signaling pathway (GO:0009738).
- GO:0019207 kinase regulator activity (IDA, PMID:19407142): this is an indirect/downstream
  effect (PYR1 inhibits PP2Cs, which de-represses SnRK2 kinases). Kept but as non-core /
  better captured by PP2C inhibitor activity; the TAIR IDA actually measured PP2C inhibition.
- "protein binding" GO:0005515 (many IPI): REMOVE per project guidance (uninformative);
  the underlying interactions are captured by specific MF terms above.
- Locations nucleus/cytoplasm/cytosol: ACCEPT (core). plasma membrane / vacuole / plant-type
  vacuole membrane: KEEP_AS_NON_CORE (transient regulatory localizations).
- GO:0062049 protein phosphatase inhibitor complex (part_of): ACCEPT — PYR1-ABA-PP2C complex.
- GO:0044389 ubiquitin-like protein ligase binding (RSL1): KEEP_AS_NON_CORE (regulatory turnover).
- GO:1902584 positive regulation of response to water deprivation (IMP, PMID:29970817): ACCEPT as non-core downstream physiology.
- IEA nucleus GO_REF:0000044 and ISM/ISS nucleus: ACCEPT (consistent with experimental nucleus).

## Deep research synthesis (Falcon / Edison Scientific)

The Falcon deep-research report (file:ARATH/PYR1/PYR1-deep-research-falcon.md) corroborates
the existing review without changing any curation decision. Key points used to strengthen
`supported_by` evidence:

- Primary function is restated as PYR1 being an "intracellular ABA receptor** that binds
  ABA and inhibits clade A PP2C phosphatases", and PYR1 "is best understood as a
  **ligand-gated PP2C inhibitor** that converts ABA concentration into a change in
  phosphatase activity" — supports GO:0004864 (protein phosphatase inhibitor activity) and
  GO:0038023 (signaling receptor activity).
- Direct ABA binding confirmed by NMR ("to PYR1 observed by NMR chemical shift perturbations
  upon ABA addition") — supports GO:0010427 (ABA binding).
- Double-negative core circuit PYR/PYL/RCAR —| PP2C —| SnRK2, "allowing activation of
  SnRK2-driven phosphorylation cascades and ABA-responsive transcription" — supports the
  GO:0009738 BP placement and the signaling-receptor core function.
- PYR1 "forms a **homodimer** in apo and solution states; ABA induces a more compact
  closed-lid conformation" — supports GO:0042803 (homodimerization).
- RSL1 (plasma-membrane RING E3 ligase) "interacts with **PYR1** and promotes its
  degradation" — supports GO:0044389 (ubiquitin-like protein ligase binding), kept non-core
  as a regulatory turnover route.

No new GO terms with verifiable IDs were introduced. The report adds context on receptor
turnover (Bueso 2014 RSL1; García-León 2019 ALIX/ESCRT), Ca2+ feedback via CBL1/9–CIPK1
(You 2023), and chemical-genetics modulation of the dimer interface (DBSA; Wang 2024), but
these concern regulation/chemistry rather than new core PYR1 functions, so no new
`existing_annotations` were created. No `UNDECIDED` actions were present to resolve.
