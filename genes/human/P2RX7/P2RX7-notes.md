# P2RX7 review notes

## Why this gene was selected, and where the exposure actually is

P2X7 is usually described as a "contested" protein. It is important to be precise about what is
contested, because the GOA exposure follows from it.

**Not contested:** the molecular function. P2X7 is a homotrimeric, ATP-gated non-selective cation
channel. This was established at the cloning of the human receptor
[PMID:9038151 "Brief applications (1-3 s) of ATP and 2', 3'-(4-benzoyl)-benzoyl-ATP elicited
cation-selective currents."], confirmed by single-channel analysis, and shown structurally
[PMID:31587896 "P2X receptors are trimeric, non-selective cation channels activated by extracellular
ATP."]. Even the 2026 review that catalogues the controversy opens by taking the receptor's identity
for granted and disputes only where it is found.

**Contested:** which cells express it.
[PMID:41672132 "Its expression has been clearly demonstrated in microglia, where it regulates numerous
cellular processes, including cell activation, cytokine release, and calcium signaling."] but
[PMID:41672132 "The most controversial, however, is the presence and role of P2X7R in neurons."] The
review frames the problem as methodological:
[PMID:41672132 "We revisit the pharmacological regimen required to confirm the functional expression of
the receptor and the mouse models that have aided in the investigation of neuronal P2X7R."]

So **the curation exposure is in CC and BP, not MF.** No MF controversy was manufactured; every
molecular-function row was reviewed on its own merits and the ATP-gated cation channel term is core.

## The other side of the neuronal argument

The 2026 literature is not uniform. Two 2026 papers proceed as if neuronal P2rx7 were settled:
[PMID:41935187 "Mechanistically, we identify the purinergic receptor gene P2rx7 as a direct target of
SETDB1."] and [PMID:41935187 "We characterize a novel enhancer in the P2rx7 first intron that is
epigenetically silenced by SETDB1; loss of SETDB1 results in increased chromatin accessibility and
aberrant P2rx7 overexpression."] - with the conditional Setdb1 deletion restricted to excitatory
neurons; and [PMID:41881298 "In line with these findings, we found that selective genetic P2X7R
depletion or, unexpectedly, TNAP heterozygosity prevented the reduction of neuronal CTCF expression in
P301S mice."]

The strongest positive evidence is the cell-type-specific seizure study:
[PMID:38777288 "Mice with deleted P2rx7 in microglia displayed less severe acute seizures and developed
a milder form of epilepsy, and microglia displayed an anti-inflammatory molecular profile."] versus
[PMID:38777288 "In contrast, mice lacking P2rx7 in neurons showed a more severe seizure phenotype when
compared to epileptic wild-type mice."] with human data
[PMID:38777288 "Analysis of single-cell expression data revealed that human P2RX7 expression is elevated
in the hippocampus of patients with temporal lobe epilepsy in excitatory and inhibitory neurons."]

**Opposite-direction phenotypes from two cell-type-restricted deletions are hard to explain by
antibody artefact**, which is why the neuronal annotations are kept rather than removed.

### The corrigendum, PMID:40713463 - what could not be retrieved

That seizure study has a 2025 corrigendum. **I could not retrieve what was corrected.** Specifically:

- The PubMed record (PMID:40713463) is an `Published Erratum` type with author list and affiliations but
  **no abstract and no correction text**. It states only `Erratum for Brain Behav Immun. 2024
  Aug;120:121-140. doi: 10.1016/j.bbi.2024.05.023`.
- Europe PMC returns the record with an empty `abstractText` and `isOpenAccess: N`, listing only
  "Subscription required" via DOI.
- `https://doi.org/10.1016/j.bbi.2025.07.009` redirects to linkinghub.elsevier.com, which served only a
  "Redirecting" stub; the ScienceDirect article page returned HTTP 403.

So: the corrigendum exists (Brain Behav Immun 2025;129:1040, doi 10.1016/j.bbi.2025.07.009), it applies
to the paper that is the single strongest support for functional neuronal P2X7, and **its content is
unknown to this review**. That is recorded verbatim in `reference_review` for PMID:40713463 and raised
in `suggested_questions`, because a curator leaning on PMID:38777288 needs to read it first. Note also
that the corrigendum author list differs slightly from the original in the rendering of several author
names (e.g. "Arribas Blázquez M" becomes "Blázquez MA", "Menéndez Méndez A" becomes "Méndez AM"),
which is consistent with - but not proof of - an authorship/name correction rather than a data
correction. I am not asserting that; it is an observation about the two PubMed records.

## Curation positions taken on the neuronal annotations

The neuronal terms split into **two groups that deserve different treatment**, and this is the main
finding of the review:

### Group 1 - derived mechanically from the molecular function: `MARK_AS_OVER_ANNOTATED`

- `GO:0060079` excitatory postsynaptic potential is `IEA GO_REF:0000108` (inter-ontology logical
  inference) with **`GO:0004931` in the WITH/FROM field**.
- `GO:0098794` postsynapse is `IEA GO_REF:0000108` with **`GO:0060079` in the WITH/FROM field**.

The chain is therefore: *P2X7 is an ATP-gated cation channel → it could generate an EPSP → it is
postsynaptic.* No neuron was involved at any step, and every P2X receptor inherits the same chain. For
a protein whose neuronal expression is the contested question, deriving a synaptic compartment from its
molecular function is the one inference that must not be allowed to stand in as evidence. Both marked
over-annotated, with the derivation spelled out in `reason`.

This was checked directly against the WITH/FROM column of `P2RX7-goa.tsv`, not assumed.

### Group 2 - orthology transfers of experimental mouse localisations: `KEEP_AS_NON_CORE`

`GO:0043025` neuronal cell body, `GO:0045202` synapse, `GO:0031594` neuromuscular junction (and
`GO:0009897`, `GO:0005911`) are `IEA GO_REF:0000107` from mouse P2rx7, and the mouse records carry
experimental evidence behind each: GO:0043025 from PMID:15964665 and PMID:15978588, GO:0045202 from
PMID:18082965, GO:0031594 from PMID:15713258. These are precisely the antibody-based studies the 2026
review questions, but per project rules an experimental curator call is not overruled from an abstract.
Kept, demoted to non-core, with the full controversy recorded in `reason` on each.

`GO:0019233` sensory perception of pain got the same treatment - well supported as an organismal
phenotype, but mechanistically attributed largely to microglial P2X7, so it sits inside the cell-type
question rather than outside it.

## A second, independent dispute found inside the GOA itself

**Does the P2X7 pore dilate?** GOA carries `GO:0046931` pore complex assembly three times (ARBA IEA,
IMP PMID:25651887, IDA PMID:9038151). The permeabilisation is real:
[PMID:9038151 "Longer applications of agonists permeabilized the cells, as evidenced by uptake of the
propidium dye YO-PRO1, but this was less marked than for cells expressing the rat P2X7 receptor."]

But single-channel analysis of the human receptor argues against dilation of the P2X7 pore itself:
[PMID:17483156 "Single-channel kinetics and permeation properties remained unchanged during receptor
activation by up to 1 mM ATP(4-) for >1 min, arguing against a molecular correlate of pore dilation at
the single P2X(7) channel level."]

and the dye-uptake pathway was assigned to a different protein:
[PMID:17036048 "Here, we identify pannexin-1, a recently described mammalian protein that functions as a
hemichannel when ectopically expressed, as this dye-uptake pathway and show that signalling through
pannexin-1 is required for processing of caspase-1 and release of mature IL-1beta induced by P2X(7)
receptor activation."]

So the phenotype is P2X7-dependent while the pore may not be P2X7. `KEEP_AS_NON_CORE`, with both sides
cited in `supported_by` on the annotation itself - the same treatment TMEM175's proton-channel terms got
in this project. This is also why `GO:0015748` organophosphate ester transport (ARBA) is marked
over-annotated: it reads a transport activity off the ligand.

## Scrambling: P2X7 is the trigger, ANO6 is the scramblase

`GO:0017121` plasma membrane phospholipid scrambling is IDA on P2X7 from
[PMID:25651887 "Here we demonstrate that the stimulation of P2X7 receptors activates anoctamin 6 (ANO6,
TMEM16F), a protein that functions as Ca(2+) dependent phospholipid scramblase and Ca(2+)-activated
Cl(-) channel."] with the decisive control
[PMID:25651887 "Inhibition or knockdown of ANO6 attenuates ATP-induced cell shrinkage, cell migration
and phospholipid scrambling."]

P2X7 supplies the calcium; ANO6 flips the lipids. `KEEP_AS_NON_CORE`, and
**`positive regulation of plasma membrane phospholipid scrambling` is proposed as a new term**, because
GO has no regulation child under `GO:0017121` and so annotates trigger and executor identically. This
is the same distinction that had to be drawn for TMC1 in this batch ("necessary for" vs "performs"),
approached from the opposite direction.

## Other findings

- **`GO:0001530` lipopolysaccharide binding** (IEA + ISS): `MARK_AS_OVER_ANNOTATED`. It traces to a
  putative LPS-binding motif in the rodent C-terminal tail, a region the full-length structures assign
  to the C-cys anchor and the cytoplasmic ballast. Biologically it collapses a two-signal pathway:
  TLR4 is the LPS receptor (signal 1), P2X7 is the ATP sensor (signal 2).
- **`GO:0005267` potassium channel activity and `GO:0005272` sodium channel activity** (both IDA,
  PMID:17483156): `MODIFY` to `GO:0004931`. The recordings are real - the study substituted the charge
  carrier systematically - but the terms name *selective* channels and P2X7 is non-selective. The fluxes
  themselves remain recorded as `GO:0071805` and `GO:0035725`.
- **`GO:0005524` ATP binding**: kept non-core, not removed. Literally true, but the site is
  extracellular and the protein neither hydrolyses nor uses ATP, so on a surface receptor the term
  invites the wrong reading. Complicated by the structures, which found a genuine cytoplasmic
  *guanosine* nucleotide site [PMID:31587896 "They show a second cytoplasmic element with a unique fold,
  the cytoplasmic ballast, which unexpectedly contains a zinc ion complex and a guanosine nucleotide
  binding site."].
- **`GO:0042802` identical protein binding** was `ACCEPT`ed, not swept up with bare protein binding:
  for an obligate homotrimer, self-association is a real and mechanistically loaded statement.
- **`GO:0002931` response to ischemia** (NAS, PMID:12849743): the weakest evidence code in the set, and
  the cited abstract is about P2X2 and P2X4 [PMID:12849743 "In particular, P2X2 and P2X4 proteins became
  significantly up-regulated, although to different extent and in different cellular phenotypes."].
  Flagged `MARK_AS_OVER_ANNOTATED` and `MISCITED` rather than removed, because the full text was not
  available.
- **`Reactome:R-HSA-139855`** is titled "P2X1-mediated entry of Ca++ from plasma" and is used as a TAS
  source for a P2RX7 plasma-membrane annotation. The localisation is right; the event is about a
  different subtype. Recorded as `WRONG_IDENTIFIER` in `reference_review`.
- **`PMID:17299767`** ("Involvement of P2X4 and P2Y12 receptors in ATP-induced microglial chemotaxis")
  is likewise used only for a plasma-membrane TAS on P2RX7 - harmless, but a poor reference choice.
- Nine bare `GO:0005515` protein binding rows: `MARK_AS_OVER_ANNOTATED` per project guidance.
- **`GO:0005737` cytoplasm** (ISS): `MARK_AS_OVER_ANNOTATED`. A two-transmembrane surface receptor.

## Qualifier note

No `NOT|` qualifiers appear anywhere in `P2RX7-goa.tsv` - checked directly. All 106 GOA rows are
positive assertions.

## PMID verification

Every PMID cited was checked against PubMed metadata or the cached record before use.
