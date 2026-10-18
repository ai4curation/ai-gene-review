# TMC1 review notes

## Why this gene was selected

Contested/newly-assigned molecular function. Two questions are live at once:

1. **Is TMC1 an ion channel at all, or only a component of the transduction apparatus?** This was a
   genuine long-running dispute, driven by the failure of TMC1 to reach the plasma membrane in
   heterologous cells. The 2024/2025 Neuron paper that largely settles it says so in its own abstract:
   [PMID:39674179 "However, controversy persists because the heterogeneously expressed TMC1/2 in
   cultured cells lack evidence of mechanical gating, primarily due to their absence from the plasma
   membrane."]
2. **Is TMC1 also a lipid scramblase?** Structurally the same question as TMEM63A/TMEM63B, which a
   sibling review in this batch handled, and which the TMC field itself frames the same way, because
   TMC1 was modelled on the TMEM16 fold:
   [PMID:30063209 "We generated a model of TMC1 based on X-ray and cryo-EM structures of TMEM16
   proteins, revealing the presence of a large cavity near the protein-lipid interface"]

## Position taken

**Channel: core, and no longer contested.** **Scramblase: process asserted, activity withheld.**

The asymmetry is deliberate and is the point of the review.

## The channel assignment

Genetic necessity, with normal hair-bundle structure so the phenotype is not developmental:
[PMID:22105175 "Tmc1(Δ)Tmc2(Δ) mice had profound vestibular dysfunction, deafness, and structurally
normal hair cells that lacked all mechanotransduction activity"] and rescued by either paralogue
[PMID:22105175 "Expression of either exogenous TMC1 or TMC2 rescued mechanotransduction in
Tmc1(Δ)Tmc2(Δ) mutant hair cells."]

Permeation properties tracked to TMC subunit identity:
[PMID:23871232 "Cells that expressed Tmc2 had high calcium permeability and large single-channel
currents, while cells with mutant Tmc1 had reduced calcium permeability and reduced single-channel
currents."] and [PMID:23871232 "The data demonstrate TMC1 and TMC2 are components of hair cell
transduction channels and contribute to permeation properties."]

Pore mapping by cysteine modification in hair cells:
[PMID:30138589 "The data provide compelling evidence that TMC1 is a pore-forming component of sensory
transduction channels in auditory and vestibular hair cells."]

Six pore-region deafness mutations, all altering Ca2+ permeability (PMID:36191207).

The remaining gap - mechanical gating of the human protein in a naive cell - was closed by forcing
TMC1 to the plasma membrane with a CRISPRi screen:
[PMID:39674179 "Further, whole-genome CRISPRi screening enabled wild-type human TMC1/2 localization in
the plasma membrane, where they responded robustly to poking stimuli."], with a pore-identity argument
[PMID:39674179 "Deafness-related TMC1 mutations altered the reversal potential of TMC1, indicating that
TMC1/2 are pore-forming mechanotransduction channels."] and the conclusion
[PMID:39674179 "our study provides evidence that human TMC1/2 are pore-forming, mechanically activated
ion channels, supporting their roles as mechanotransduction channels in hair cells."]

## The scramblase assignment - why it is handled differently from TMEM63B

The TMEM63B review in this batch made **both** activities core, on the grounds that four independent
peer-reviewed groups using four different assay systems reported scrambling, and that disease variants
could dissociate the two activities. That evidence base does not exist for TMC1. What exists is:

- **Peer-reviewed genetics showing necessity, not agency.**
  [PMID:40073458 "We found that expression of either TMC1 or TMC2, was essential for PS
  externalization."] and [PMID:40073458 "Tmc1/Tmc2 knockout mice and Tmie mutant mice lacked PS
  externalization completely."] The title is exact about this - "necessary for scramblase activity" -
  and the authors decline to go further:
  [PMID:40073458 "However, it remains unclear whether TMC1 and TMC2 have a direct role in lipid
  scrambling or an essential but indirect role, perhaps by providing a signal or environment that
  enables lipid scrambling."]
  Note also that the Tmie mutant result cuts both ways: hair cells that still express TMC1/TMC2 but
  mislocalise them show no PS externalisation, so the requirement is for *functional, correctly placed*
  TMCs - which is what you would expect either of a direct scramblase or of an upstream permissive role.
- **One direct translocation assay, in a preprint.**
  [PMID:40631239 "Using reconstituted proteoliposomes and molecular dynamics simulations, we demonstrate
  that both proteins facilitate phospholipid translocation across membrane bilayers, a process tuned by
  cholesterol and enhanced by deafness-causing TMC1 mutations."] and
  [PMID:40631239 "Here, we reveal that TMC1 and TMC2 are cholesterol-regulated lipid scramblases whose
  activity modulates plasma membrane asymmetry."]
  **This is bioRxiv 2025.07.03.663083 and was still a preprint when this review was written** (no journal
  version in PubMed as of September 2026). It is flagged as such in `reference_review`.

So the curation call is: assert `GO:0017121 plasma membrane phospholipid scrambling` **involved_in**
(NEW, IMP, PMID:40073458) because necessity in hair cells is established in peer-reviewed work; do
**not** assert `GO:0017128 phospholipid scramblase activity` **enables**, because the only evidence
that TMC1 performs the translocation is a preprint and the peer-reviewed authors explicitly leave the
mechanism open. "Necessary for" is not "performs". Dual function remains a legitimate possible outcome -
the TMEM16 and TMEM63/OSCA precedents show a single groove can pass both ions and lipids - it is simply
not yet established here.

A further caveat recorded in `suggested_questions`: in hair cells PS externalisation is *triggered by
blocking transduction* and by deafness alleles, so it may report hair-cell distress rather than a normal
physiological process. If so, even the BP annotation describes a disease mechanism.

## Term-choice problem found in the existing annotation set

### `GO:0005245` voltage-gated calcium channel activity - wrong gating stimulus

TMC1 carries this term twice (IBA GO_REF:0000033; IEA GO_REF:0000107 from mouse). TMC1 is gated by
tension through the PCDH15 tip link and has no voltage sensor. Tracing the propagation:

- Mouse Tmc1 (MGI:MGI:2151016 / UniProtKB:Q8R4P5) carries `enables GO:0005245` with IMP and IGI from
  **PMID:23871232**, a paper that measured **calcium permeability and single-channel conductance** of
  the mechanotransduction channel. It makes no voltage-gating claim.
- The same mouse record also carries `enables GO:0005262` calcium channel activity from the same paper,
  which is the term the data actually support.
- GO:0005245 is a child of GO:0005262 that adds a gating mechanism. So this is a `GRANULARITY_MISMATCH`
  under `TERM_SCOPING_PROBLEM`: the child overstates specificity in a way that is not just uninformative
  but factually wrong about the mechanism.

Action: `MODIFY` both rows to `GO:0140135` mechanosensitive monoatomic cation channel activity +
`GO:0005262` calcium channel activity, with structured `propagation_review` on the IBA.

This is the same shape of error the TMEM63B review found (`GO:0005227` calcium-**activated** cation
channel activity for a stretch-gated, calcium-**permeable** channel): a permeation property written
into a gating term.

### `GO:0008381` left as ACCEPT rather than tightened

`GO:0140135` (cation) would fit the mammalian MET channel better than `GO:0008381` (any ion). But the
IBA sits at a node that also spans invertebrate TMCs, and per project rules an IBA encodes a
phylogenetic curator's judgement about where a function arose; tightening the term at the human leaf
would misrepresent what the node asserts. Left as ACCEPT with the point recorded in `reason`.

### `GO:0009897` external side of plasma membrane

Orthology transfer of a mouse IDA (PMID:16455951). TMC1 is a ten-TM protein with cytoplasmic termini,
so the term sits oddly, but this is an experimental curator call whose full text was not read here, so
per project rules it is `KEEP_AS_NON_CORE`, not `REMOVE`.

### No complex term at all

Two MF rows use `contributes_to`, which presupposes a complex, yet GOA gives TMC1 no complex membership.
Added `GO:0034703` cation channel complex as a NEW `part_of` annotation (IDA, PMID:34089643, which
defines CIB2/CIB3 as MET channel auxiliary subunits), and proposed a dedicated
**mechanoelectrical transduction channel complex** term, since GO:0034703 does not distinguish this
assembly from any other cation channel.

## PMIDs verified

All PMIDs cited were checked against PubMed metadata before use. Three initial guesses were **wrong**
and were discarded rather than cited: 29804837 (a V(D)J recombination paper, not Pan et al. 2018),
25683721 (phylogenetic profiling) and 35768512 (enteric viruses). The correct Pan et al. 2018 Neuron
pore paper is **PMID:30138589**.
