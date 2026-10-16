# twist1 (Xenopus laevis, P13903) — review notes

Project: NEURAL_CREST_ORIGINS (Tier 1, neural crest specifier candidate).

## Identity
- Swiss-Prot TWIST_XENLA, 166 aa, X-twi / Xtwi; bHLH (IPR011598, IPR047093 TWIST1_bHLH); C-terminal WR
  domain (Twist box, aa 143-166 per Lander 2013). PANTHER PTHR23349 (bHLH Twist family).
- UniProt: "Efficient DNA binding requires dimerization with another bHLH protein. Homodimer." Nucleus.

## Expression (where/when)
- Cloned as Xtwi; mesoderm (notochord, lateral plate, not myotome) from early gastrula, then neural crest
  [PMID:2590945 "Xtwi is also activated a few hours later in the early"] [PMID:2590945 "Xtwi expression therefore marks the subdivision"].
- Low maternal/pre-gastrula RNA [PMID:9727830 "X-twi RNA can be weakly detected at stages prior to"]; function of
  early RNA unknown.
- In NC: first detectable at stage 14, later than snai1/2, sox9, foxd3; restricted to cranial crest
  (mandibular -> hyoid -> branchial), maintained in migrating and post-migratory arch crest
  [PMID:23443570 "Twist expression is first detectable in NC precursor cells at stage 14, considerably later than several other NC specifiers, including Snail1, Snail2, Sox9 and Foxd3, indicating that it is unlikely to be a regulatory input into the initial expression of these factors"]
  [PMID:23443570 "Twist is distinguished from other NC specifiers by the restriction of its expression to cranial regions"].

## Upstream inputs (network position)
- Immediate-early Pax3 target in animal caps (cycloheximide-resistant), Pax3-dependent in vivo; not Zic1
  [PMID:24360906 "Twist1 was neither activated by Zic1 alone, nor downregulated by Zic1 knock-down in vivo, suggesting that twist is regulated by Pax3 only."]
  [PMID:24360906 "were highly and reproducibly activated either by Pax3 (snail2, twist1) or by Zic1 (snail1) in the presence of cycloheximide"].
  Pax3 occupancy of a twist1 enhancer not shown.

## Molecular activity
- bHLH; E-box binding and homo-/heterodimerization with E12/E47 (family-level, cited in Lander intro)
  [PMID:23443570 "domain that mediates homodimerization or dimerization with E12/E47"]. No Xenopus-specific
  DNA-binding / ChIP data found; no direct targets defined in frog.
- WR domain binds Snail1/Snail2 directly and inhibits Snail2 (reduces its chromatin recruitment; blocks
  Snail2-induced ectopic NC); regulated by GSK3-beta phosphorylation of S148
  [PMID:23443570 "Glutathione S-transferase (GST)-pulldown assays indicate that the interaction between Twist and Snail2 is direct"]
  [PMID:23443570 "Twist diminishes recruitment of Snail2 to chromatin"]
  [PMID:23443570 "Snail2 expression induces ectopic NC formation in this assay, and while TwistS148D potently blocked its effects, TwistS148A did not"]
  [PMID:23443570 "Collectively, our data suggested a model in which Twist binds to and inhibits the activity of Snail proteins"].
  -> candidate NEW MF GO:0140416 transcription regulator inhibitor activity (IDA).

## Loss/gain of function (Xenopus)
- NC-targeted MO (one cell, 8-cell stage, avoids mesoderm): reduced snai1/2 (mildly), sox10 (strongly);
  zic1 domain expanded (cells stalled in border state); no apoptosis/proliferation change; rescued by
  MO-resistant Twist [PMID:23443570 "Importantly, the effects of Twist depletion can be rescued by a form of Twist that cannot be targeted by the MO"]
  [PMID:23443570 "strongly suggesting that the loss of gene expression reflects altered cell specification as opposed to the death of specific cell populations"].
- Fate diversification: MO -> reduced Sox9 in arches, cartilage defects; increased Foxd3 (cranial glia).
  GOF -> opposite (more Sox9, less Foxd3) [PMID:23443570 "suggesting that in the absence of Twist, cranial NC cells that would normally give rise to cartilage might instead adopt glial fates"].
- GOF does NOT generate ectopic NC in frog; both gain and loss disrupt NC (stoichiometry-dependent).

## Layer placement
- Not a border specifier (downstream of Pax3; its loss expands zic1). Not a pluripotency/competence factor.
- A late-onset, cranial-restricted NC specifier whose main distinctive output is ectomesenchymal
  (chondrogenic) fate of cranial crest. Its GRN-"specifier" status is Xenopus/anamniote-specific:
  [PMID:23443570 "although it does not appear to have this role in amniotes"]
  [PMID:23443570 "its early NC expression appears to have been lost in the mouse"].
  Mouse null still has cranial NC/branchial arch defects [PMID:23443570 "mice have severe defects in cephalic neural tube closure and malformed branchial arches and facial primordium"].
- GO: GO:0014029 neural crest formation (definition = formation of border ectoderm region) fits the border
  layer better; sibling reviews (XENLA/sox10) moved specifier rows to GO:0014036 neural crest cell fate
  specification. Applied the same here for consistency.
- Cranial skeleton: GO:0048701 embryonic cranial skeleton morphogenesis (mouse Twist1 carries it) — Twist
  acts in cranial crest to bias toward cartilage; proposed as NEW (IMP, PMID:23443570).

## Mesoderm (non-core in frog)
- Mesodermal expression since 1989 is the "ancestral" Twist role (Drosophila twist mesoderm). No Xenopus
  functional data for mesoderm found -> no NEW mesoderm term.

## Evolution
- Ciona: Twist (twist-like 2) only in mesoderm-derived mesenchyme; misexpression in a9.49 pigment lineage
  makes migrating ectomesenchyme
  [PMID:23135395 "In Ciona, Twist is expressed solely in mesoderm-derived mesenchyme"]
  [PMID:23135395 "Thus, the misexpression of Twist appears to be sufficient, in part, to reprogram the a9.49 lineage into ectomesenchyme"].
  Supports co-option of a mesodermal mesenchyme determinant into the cranial crest as a vertebrate innovation.
- Amphioxus: many specifier genes absent from the neural plate border
  [PMID:18562679 "many neural crest specifier genes are not expressed at the amphioxus neural plate/tube border, raising the intriguing possibility that this level of the network was co-opted during vertebrate evolution"].
- Tetrapods: only cephalic crest expresses Twist and makes ectomesenchyme
  [PMID:23135395 "In tetrapods, it appears that only the cephalic neural crest expresses Twist and produces ectomesenchyme"].

## TAS PMID:15242799
- Id2/cardiac NC ablation paper (chick, Xenopus), abstract-only cached; abstract does not mention Twist;
  presumably Twist used as NC marker in full text. Weak support but term biologically sound -> MODIFY to the
  more precise GO:0014036 (consistent with sox10) rather than remove.
