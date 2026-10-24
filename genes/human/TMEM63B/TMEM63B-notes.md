# TMEM63B review notes

## Why this gene was selected

Flagged as a contested/newly-assigned molecular function case: is TMEM63B a mechanically
activated cation channel, a mechanically activated lipid scramblase, or genuinely both?
Unusually for this batch, GOA already carries **both** activities for TMEM63B with
experimental evidence (`GO:0140135` mechanosensitive monoatomic cation channel activity IDA;
`GO:0017128` phospholipid scramblase activity IDA + IMP x2 + IEA), so the curation question is
not "which one is right" but **whether both are core**, and how TMEM63B differs from its
paralog TMEM63A.

## Position taken

**Both activities are core for TMEM63B.** TMEM16 family proteins are the precedent for one
protein being both a channel and a scramblase, and TMEM63B belongs to the same
Transmembrane-Channel-Scramblase (TCS) superfamily fold. The channel and scramblase claims
rest on *different* assays and different constructs, and both sets are independently
replicated, so this is a genuine dual-function protein rather than a dispute in which one
side must be wrong.

## The channel assignment (long-established, uncontested)

Founding family-level demonstration that OSCA/TMEM63 proteins are mechanically activated
channels: [PMID:30382938 "Here, we show that various members of the OSCA and TMEM63 family
of proteins from plants, flies, and mammals confer mechanosensitivity to naïve cells."].

Structure + electrophysiology, establishing the monomeric architecture and the biophysics:
[PMID:37543036 "Functional analyses demonstrated that TMEM63s are bona fide mechanosensitive
ion channels, characterized by small conductance and high thresholds."] and
[PMID:37543036 "Here, we uncover an unanticipated monomeric configuration of TMEM63 proteins."].

In vivo physiological demonstration in mouse lung, with cation currents recorded during
stretch: [PMID:38127458 "we show that loss of the mechanosensitive channels TMEM63A and
TMEM63B (TMEM63A/B) resulted in atelectasis and respiratory failure in mice due to a deficit
of surfactant secretion"] and [PMID:38127458 "Activation of TMEM63A/B channels during cell
stretch facilitated the release of surfactant and ATP from LBs fused with the plasma
membrane."].

Human disease variants act on the conductance: [PMID:37421948 "demonstrated inward leak
cation currents across the mutated channel even in isotonic conditions, while the response to
hypo-osmotic challenge was impaired, as were the Ca2+ transients generated under hypo-osmotic
stimulation"].

## The scramblase assignment (new but well replicated)

Four independent groups, four different assay systems:

1. Purified protein + cryo-EM, Segawa lab: [PMID:39424995 "we show that transmembrane protein
   63B (TMEM63B) functions as a membrane structure-responsive lipid scramblase localized at
   the PM and lysosomes, activating bidirectional lipid translocation upon changes in membrane
   curvature and thickness."] with a structural pathway
   [PMID:39424995 "We determined the cryo-electron microscopy structures of TMEM63B in its open
   and closed conformations, uncovering a lipid translocation pathway formed in response to
   changes in the membrane environment."] and a cellular lipid-distribution phenotype
   [PMID:39424995 "TMEM63B deficiency alters phosphatidylcholine and sphingomyelin
   distributions in the PM."].
2. Unbiased CRISPR revival screen for phospholipid scrambling, Suzuki lab:
   [PMID:39217145 "Ca2+ stimulation-mediated PLS is suppressed by deletion of Tmem63b, while
   human disease-related Tmem63b mutants induce constitutive PLS."] — here scrambling requires
   a Tmem63b/Slc19a2 heterodimer [PMID:39217145 "we demonstrate that a protein complex,
   consisting of the ion channel Tmem63b and the thiamine transporter Slc19a2, induces PLS upon
   calcium (Ca2+) stimulation."].
3. Paralog/ortholog survey in Tmem63b-null pro-B cells: [PMID:39716028 "We expressed human
   TMEM63 paralogs, TMEM63B orthologs, and plant OSCA1.1 in Tmem63b-deficient mouse pro-B cells
   and found that vertebrate TMEM63B orthologs exhibit scramblase activity at the PM."]
4. Reconstitution into GUVs + MD, Cox/Corry labs: [PMID:41617699 "we show that phospholipids
   can be translocated through the open pores of OSCA1.1/1.2/2.2 and TMEM63A/B proteins,
   suggesting a dual ion channel and lipid scramblase function for members of this protein
   family."] with the mechanical-gating result
   [PMID:41617699 "We show that lipid scrambling in TMEM63 proteins can be activated by
   mechanical forces in the membrane, making these mechanically activated lipid scramblases."].

Mechanistic follow-up mapping an autoinhibitory C-terminal tail:
[PMID:42248451 "Functional analyses revealed that this C-terminal region is essential for
maintaining TMEM63B in an inactive state under resting conditions."], from a group that now
simply calls the protein a scramblase [PMID:42248451 "We recently identified it as a
mechanosensitive lipid scramblase activated by changes in membrane physical properties."].

## Do the two activities use the same or different constructs/assays?

They do not collapse into one another, and the 2025-2026 work shows they can be **separated**:

- Disease variants dissociate them: [PMID:42573579 "Notably, V44M and T481N convert TMEM63B
  into constitutive phospholipid scramblases without obvious effects on their MSC activity,
  revealing an unexpected channel-to-scramblase switch in these variants."], confirmed
  structurally by [PMID:40480214 "We first found that TMEM63B p.V44M and the homologous
  TMEM63A p.V53M are gain-of-function mutations that do not enhance channel activity but
  instead evoke constitutive lipid scramblase activity."].
- A third variant separates them the other way: [PMID:42573579 "Like V44M and T481N, I475del
  also enabled constitutive phospholipid scramblase activity."] but
  [PMID:42573579 "However, unlike these variants, I475del uniquely displayed further
  potentiation of scramblase activity under hypotonic osmotic stress."].
- In the MD work, ion conduction and lipid translocation have **different bottleneck residues**
  in the same groove (PMID:41617699, Fig. 3 "Separate bottleneck residues control ion
  conduction and lipid scrambling in TMEM63A").

So the two activities share a groove but are not the same measurement re-described.

## What is genuinely still open

Whether wild-type TMEM63B scrambling operates in vivo at physiological force, as opposed to in
reconstituted/over-expressed systems, is explicitly flagged as unresolved by the authors of the
structural work: [PMID:40480214 "A further question is whether the scramblase activity of
endogenous WT TMEM63 channels is associated with physiological functions."]. This uncertainty
is about the *physiological deployment*, not about whether the activity exists, so it does not
warrant demoting `GO:0017128` from core — but it is recorded in `suggested_questions`.

## Term-choice problems found in the existing annotation set

### `GO:0005227` calcium-activated cation channel activity — wrong gating stimulus

GO definition: "Enables the transmembrane transfer of an inorganic cation by a channel that
opens **when a calcium cation has been bound** by the channel complex or one of its constituent
parts." Every experimental user of this term in GOA is a genuinely Ca2+-gated channel
(KCNN4, SLO1/SLO2, TRPM4, TMEM16A/subdued). TMEM63B is gated by membrane stretch and
hypo-osmolarity and is **Ca2+-permeable**, not Ca2+-gated. The provenance of the error is
visible in two places:

- The mouse IDA that seeds the human ISS/IEA is
  [PMID:31243992 "This Ca2+-permeable channel specifically induces Ca2+ influx across the
  membrane in response to extracellular Ca2+ concentration and hyperosmolarity."] — from a
  paper titled "Overexpression of Osmosensitive Ca(2+)-Permeable Channel TMEM63B ...".
- The InterPro signature behind the IEA, IPR045122, is named "**Calcium permeable**
  stress-gated cation channel 1-like", and InterPro2GO maps it to "calcium **activated**
  cation channel activity". A permeable→activated slip.

Action: `MODIFY` on all four GO:0005227 rows (IBA, IEA, IDA, ISS) → `GO:0140135`
mechanosensitive monoatomic cation channel activity + `GO:0005262` calcium channel activity.

### `GO:0120019` phosphatidylcholine transfer activity / `GO:0140338` sphingomyelin transfer activity — wrong mechanism

GO:0120019: "**Removes** phosphatidylcholine from a membrane or a monolayer lipid particle,
**transports it through the aqueous phase while protected in a hydrophobic pocket**, and brings
it to an acceptor membrane". GO:0140338 is the same shape for sphingomyelin. These describe
soluble **intermembrane lipid-transfer proteins** (STARD/CERT-like), not polytopic membrane
scramblases. TMEM63B is an 11-TM integral membrane protein that flips PC and SM between the two
leaflets of *one* bilayer. The observation behind the annotation is real
([PMID:39424995 "TMEM63B deficiency alters phosphatidylcholine and sphingomyelin distributions
in the PM."]) but it was mapped to a transfer-protein term rather than a scramblase term.

Action: `MODIFY` both → `GO:0017128` phospholipid scramblase activity (which the gene already
carries with IDA/IMP). Note that GO has no lipid-species-specific scramblase child; a
`phosphatidylcholine scramblase activity` / `sphingomyelin scramblase activity` term is
proposed in `proposed_new_terms`.

The downstream GOC-derived `GO:0015914` phospholipid transport (derived from GO:0120019) is
correct but uninformative; `MODIFY` to `GO:0017121` plasma membrane phospholipid scrambling,
which the gene already carries and which is a descendant of GO:0015914.

## Paralog comparison (see TMEM63A-notes.md)

TMEM63B and TMEM63A are **not** interchangeable for the scramblase claim. The Segawa-lab
paralog survey found scrambling for vertebrate TMEM63B orthologs but not for the human
paralogs, and GOA records this as `NOT|enables GO:0017128` on TMEM63A (IDA, PMID:39716028).
The 2026 GUV work agrees for the cellular setting:
[PMID:41617699 "Results from our experimental scrambling assays show that WT TMEM63A
translocates lipids in GUVs but this is not the case in the cellular context."]. So the
paralog difference is real at the level of cellular scrambling; TMEM63A can scramble only
when purified and reconstituted, or when cells are actively stretched.
