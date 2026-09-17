# Scn9a (NaV1.7) — *Heterocephalus glaber* (naked mole-rat), UniProt G9DCX3

Research journal for the GO annotation review. Every assertion carries provenance.

## 0. What this accession is

G9DCX3 is the TrEMBL entry for the SCN9A mRNA (EMBL JF912494, protein AEV53348.1)
submitted by Smith, Omerbasic, Anirudhan, Lechner, Lapatsina and Lewin — the authors of
the Science paper that established naked mole-rat acid insensitivity. The UniProt record
cites that paper as its only literature reference, so this is the sequence physically tied
to the acid-block literature rather than a genome-pipeline model.

The record is **not** a complete protein. It carries
[file:HETGA/Scn9a/Scn9a-uniprot.txt "Flags: Fragment;"] with `NON_TER` at both residue 1
and residue 1884.

My own alignment (see `Scn9a-bioinformatics/RESULTS.md`) places the fragment at
**human Q15858 residues ~23-1901**, i.e. missing 22 residues of the N-terminal cytoplasmic
head and 87 residues of the distal cytoplasmic C-terminal tail, at 92.1% identity within
matched blocks. Everything structurally required for channel function is present: the
UniProt feature table lists four complete Pfam PF00520 ion-transport (S1-S6) domains
(105-390, 724-955, 1171-1446, 1495-1750), the PF11933 cytoplasmic domain (515-674), the
PF06512 sodium-ion-transport-associated domain (962-1167), 20 transmembrane helices, and
the PF24609 SCN5A-like C-terminal IQ motif (1862-1883).

**Curation consequence.** The fragment status does not undermine any molecular-function or
cellular-component claim about the channel core — the pore, all four voltage sensors and the
inactivation-gate region are in the entry. It would undermine a claim about the distal
C-terminal tail (e.g. specific C-terminal protein-interaction or trafficking motifs), and
none is annotated. The UniProt `CAUTION` line ("Lacks conserved residue(s) required for the
propagation of") is a UniRule feature-propagation notice and should be read against this
truncation, not as a statement that the channel core is defective.

Family assignment is unambiguous:
[file:HETGA/Scn9a/Scn9a-uniprot.txt "PANTHER; PTHR10037:SF221; SODIUM CHANNEL PROTEIN TYPE 9 SUBUNIT ALPHA; 1."]
and [file:HETGA/Scn9a/Scn9a-uniprot.txt "Belongs to the sodium channel (TC 1.A.1.10) family."]

## 1. The conserved function: this is a real voltage-gated sodium channel

UniProt's rule-based function statement is the standard NaV alpha-subunit description:
[file:HETGA/Scn9a/Scn9a-uniprot.txt "Mediates the voltage-dependent sodium ion permeability of"]
excitable membranes, with catalytic activity
[file:HETGA/Scn9a/Scn9a-uniprot.txt "Reaction=Na(+)(in) = Na(+)(out)"] and
[file:HETGA/Scn9a/Scn9a-uniprot.txt "SUBCELLULAR LOCATION: Cell membrane"]
[file:HETGA/Scn9a/Scn9a-uniprot.txt "Multi-pass membrane protein"].

Crucially, the naked-mole-rat literature treats this protein as a *functional* channel
whose gating is altered, not as a dead or pseudo-channel. Smith et al. cloned it and
measured proton block of the expressed channel
[PMID:22174253 "We describe a species-specific variant of the nociceptor sodium channel Na(V)1.7, which is potently blocked by protons and can account for acid insensitivity in this species."].
A channel that can be blocked is a channel that conducts. The naked mole-rat also shows
[PMID:34476892 "Normal nocifensive responses were reported for noxious heat and mechanical stimuli."],
which requires normal nociceptor action-potential initiation and hence a working NaV1.7.

The general statement that this class of channel is what fires action potentials is stated
plainly in the full-text review:
[PMID:32206859 "Voltage-gated sodium channels are necessary for action potential initiation and propagation"]
and, for this subunit specifically,
[PMID:32206859 "The NaV1.7 subunit is particularly important for action potential initiation and the naked mole-rat gene encodes amino acid variations that when mutated into the human protein considerably enhance proton block of NaV1.7 channels at certain pH values that excite nociceptors"].

So the projected core annotations (voltage-gated sodium channel activity; sodium ion
transmembrane transport; membrane depolarization during action potential; neuronal action
potential; plasma membrane; voltage-gated sodium channel complex) are not merely transferred
from mouse — they are positively confirmed by naked-mole-rat work on this very protein.

## 2. The species-specific adaptation: enhanced proton block

The organismal phenotype and the mechanism:

- [PMID:22174253 "Acid inhibition of voltage-gated sodium currents is more profound in naked mole-rat nociceptors than in mouse nociceptors, however, which effectively prevents acid-induced action potential initiation."]
- [PMID:22174253 "Thus, evolutionary pressure has selected for an Na(V)1.7 gene variant that tips the balance from proton-induced excitation to inhibition of action potential initiation to abolish acid nociception."]
- [PMID:34476892 "The gene variant in question renders the NaV1.7 channel more susceptible to inhibition by acid, thus shutting down action potential firing in nociceptor fibres."]
- [PMID:31992138 "This acid insensitivity is a function of altered ASIC responses compared to mouse19 and a variation in NMR NaV1.7, which renders the channel hypersensitive to proton-mediated block and therefore prevents acid-driven action potential initiation from the skin."]

Note the inversion of the usual logic. In every other vertebrate examined, acid excites
nociceptors through proton-*gated* channels
[PMID:22174253 "acid sensors are proton-gated ion channels that depolarize neurons"];
naked-mole-rat ASICs and TRPV1 behave normally, and the change is downstream, in the
channel that would have to fire the action potential.

### The motif — verified, not recalled

The abstract-only primary papers (PMID:22174253, PMID:31147513) do not give residue
numbers. The full-text review does describe the motif, in words rather than coordinates:
[PMID:32206859 "In our recent study we found that the acid-insensitive Cape mole-rat was the only species that has the identical amino acid motif in domain IV of the NaV1.7 channel as the naked mole-rat (EKE and not the more common EKD sequence)."]
and
[PMID:32206859 "It should be noted that EKE variant has been shown experimentally to increase the proton block of the NaV1.7 channel."]
The review states that the ancestral trio is KKV (positively charged) in mouse and human and
becomes EKD or EKE in subterranean African mole-rats.

Harms et al., who tested the motif experimentally, locate it precisely:
[PMID:28939386 "the suggested negatively-charged motif in the ANMrNav1.7 domain IV P-loop"].

Rather than assert residue numbers from memory, I checked the sequences directly
(`Scn9a-bioinformatics/div_ploop_motif.py`, results in
`Scn9a-bioinformatics/RESULTS.md`). Anchoring on the invariant flanking residues of the
domain IV extracellular P-loop (`D[CS][DN]P...HPG`):

| species | accession | triplet | position |
|---|---|---|---|
| naked mole-rat | G9DCX3 | **EKE** | 1698-1700 |
| human | Q15858 | KKV | 1718-1720 |
| mouse | Q62205 | KKV | 1716-1718 |
| rat | O08562 | KKV | 1716-1718 |
| rabbit | Q28644 | KKV | 1715-1717 |
| guinea pig | H0VMS3 | HKV | 1716-1718 |
| 13-lined ground squirrel | I3M736 | KKV | 1706-1708 |

[file:HETGA/Scn9a/Scn9a-bioinformatics/RESULTS.md "The naked mole-rat NaV1.7 sequence G9DCX3 carries EKE at fragment positions 1698-1700, where human Q15858 carries KKV at 1718-1720, in the domain IV extracellular P-loop."]

This reproduces the published motif exactly, in the sequence this review is about, and
locates it in the topology: taking the UniProt feature table at face value, domain IV S5
ends at 1641 and S6 begins at 1717, so 1698-1700 sits in the distal half of the
extracellular P-loop between them. Guinea pig — the closest sampled hystricomorph
relative — retains KV with only a conservative K→H at the first position, so EKE is not a
hystricomorph-wide feature. The one hibernator I sampled retains KKV; I did not attempt to
reproduce the broad hibernator survey of
[PMID:24352952 "Our analyses revealed a functional convergence of amino acid sequences, which occurred at least six times independently in mammals that hibernate."],
which reports the convergence, and which independently confirms that
[PMID:24352952 "In the naked mole-rat, acid insensitivity has been shown to be conferred by the functional motif of the sodium ion channel NaV1.7."]

### The motif is a sequence correlate; the physical mechanism is still open

I initially wrote that a +2 to -2 swap next to the pore is "exactly the kind of change
expected to raise local proton affinity". That is a just-so story, and the one paper that
actually tested it says otherwise. Harms et al. put the naked-mole-rat motif into the human
channel and confirmed the effect —
[PMID:28939386 "The insertion of the negatively charged motif (EKE) of ANMrNav1.7 into human Nav1.7 results in an increased proton-evoked tonic inhibition, but also in a reduced channel function."]
and
[PMID:28939386 "Our data confirms that a negative charge of a postulated proton-motif encodes for a high proton-sensitivity when inserted into hNav1.7."] —
but they also found that the simple electrostatic account does not generalise:
[PMID:28939386 "Overall, a correlation between proton-evoked inhibition and motif charge was not evident."],
[PMID:28939386 "Accordingly, a homology model of hNav1.7 shows that the EKE motif residues do not contribute to the pore lumen."],
and
[PMID:28939386 "Given the distance of the proton-motif from the pore mouth it seems unlikely that a blocking mechanism involving direct obstruction of the pore underlies the observed proton-evoked channel inhibition."]

Two consequences for this review. First, the wording throughout describes EKE as the
**sequence correlate** of enhanced proton block, not as a pore-occluding site. Second, the
Harms observation that the EKE substitution also *reduces* channel function in the human
chimera is a caution against reading "the naked mole-rat channel behaves normally except
for pH" too literally; the in-vivo argument for retained function rests on the animal's
normal heat and mechanical nociception, not on the chimera's biophysics.

The convergent-evolution framing is repeated in the multi-species rodent screen:
[PMID:31147513 "Using RNA sequencing, we traced the emergence of sequence variants in transduction channels, like transient receptor potential channel TRPA1 and voltage-gated sodium channel Nav1.7, that accompany algogen insensitivity."]

## 3. Does the acid-block property justify an extra GO annotation?

This was the substantive question for this review. I searched properly rather than assuming.

Terms checked (QuickGO `/ontology/go/terms/<id>/complete`, plus keyword search):

- **GO:0160128 pH-gated monoatomic ion channel activity** and its sodium child
  **GO:0160125 pH-gated sodium channel activity**. Definition of GO:0160125: *"A gated
  channel activity that enables the transmembrane transfer of a sodium ion by a channel that
  opens in response to a change in pH."* These describe a channel that **opens** on
  acidification — that is the ASIC/TRPV1 behaviour naked-mole-rat NaV1.7 does **not** have.
  Using them here would assert the opposite of the published mechanism. GO:0160128 replaces
  the older GO:0044736; no relevant secondary id.
- **GO:1905150 regulation of voltage-gated sodium channel activity** (BP) — its only child is
  GO:1905152 (positive regulation). **GO:1905151 "negative regulation of voltage-gated sodium
  channel activity" is obsolete** (obsoleted 2025-04-08, comment: *"This term was obsoleted
  because it represents a molecular function"*), with no `replaced_by` and no `consider`
  term. In any case a regulation term describes the *regulator*; the regulator here is a
  proton, not a gene product.
- **GO:0016248 channel inhibitor activity** / **GO:0019871 sodium channel inhibitor
  activity** — defined as *"Binds to and stops, prevents, or reduces the activity of a
  sodium channel"*, i.e. the property of the inhibitor, not of the inhibited channel.
- **GO:1901691 proton binding** — GO explicitly comments on GO:0160128 that pH effects on
  transporters work *"by protonation of specific residues in the protein, and not by H+
  binding"*, so proton binding is the wrong model and is discouraged for exactly this case.
- BP alternatives (**GO:0010447 response to acidic pH**, **GO:0071468**) describe a cell's or
  organism's response process; they do not capture a property of the channel, and asserting
  `involved_in response to acidic pH` for a channel whose contribution is to *fail* to fire
  would be misleading without a `NOT`/negative-regulation framing GO cannot currently express.

**Conclusion: there is a genuine ontology gap**, and the obsoletion note on GO:1905151
("represents a molecular function") shows GO itself moved the concept to the MF branch
without creating the MF term. I have therefore filed it under `proposed_new_terms` rather
than forcing an existing term. I did not add a speculative annotation.

## 4. The falcon deep-research report

A falcon report (`Scn9a-deep-research-falcon.md`, Edison Scientific Literature, 15
citations) was generated while this review was in progress. It is naked-mole-rat-specific,
unlike the affinage record, and it agrees with the conclusions I had already reached
independently, which is a useful check rather than a source of them:

- It reaches the same identity and fragment caveat:
  [file:HETGA/Scn9a/Scn9a-deep-research-falcon.md "However, **G9DCX3 is explicitly a sequence fragment**, and no retrieved study directly characterized that exact deposited fragment as a complete channel."]
- It reaches the same molecular function and location:
  [file:HETGA/Scn9a/Scn9a-deep-research-falcon.md "NaV1.7 is not an enzyme. It is an **electrogenic ion channel** whose transported substrate is principally **Na+**."]
  and
  [file:HETGA/Scn9a/Scn9a-deep-research-falcon.md "NaV1.7 performs its transport function in the **plasma membrane**."]
- It independently confirms the localisation gap I had flagged:
  [file:HETGA/Scn9a/Scn9a-deep-research-falcon.md "the retrieved literature did not provide a dedicated naked-mole-rat immunolocalization or spatial-transcriptomic study uniquely mapping G9DCX3"]
- It rules out the alternatives I did not annotate:
  [file:HETGA/Scn9a/Scn9a-deep-research-falcon.md "The retrieved evidence does not establish that G9DCX3 has unique catalytic activity, unusual ion substrate specificity, or a structural scaffolding role."]

**Its one genuinely new contribution was Harms et al. 2017 (PMID:28939386)**, which neither
the affinage record nor my own reading of the cached naked-mole-rat corpus had surfaced.
That paper was not in `publications/` and I fetched it (abstract only; no PMC record). It is
the study that tested the EKE motif experimentally, and it is also the study that qualifies
the mechanism — see section 3. Finding it changed the wording of this review, so this is a
real recall win for falcon over affinage on this gene.

Falcon's own recommended annotation set matches what this review concluded, with one
difference: it suggests "regulation of membrane potential" as a process term, which I did
not add, because for a channel that carries the depolarizing current itself GO:0086010
(membrane depolarization during action potential) is already annotated and is more precise.

## 5. What I could not resolve

- **Where the protein is expressed in the naked mole-rat, at subcellular resolution.** The
  literature speaks of "naked mole-rat nociceptors" and cutaneous C-fibres, but I found no
  naked-mole-rat immunolocalisation of NaV1.7 to axons, nerve terminals or nodes of Ranvier.
  Human data exist [PMID:30795902 "NaV1.7 could be seen localized to >90% of nodes of Ranvier in myelinated axons"],
  but I have deliberately not projected those sub-plasma-membrane CC terms onto this species;
  `plasma membrane` is as specific as the naked-mole-rat evidence supports.
- **The domain III variants.** PMID:32206859 reports that a functionally equivalent part of
  domain III also carries variants unique to acid-insensitive African mole-rats and states
  their functional importance remains to be tested. I did not attempt to localise or
  interpret them; nothing in this review depends on them.
- **Visceral vs cutaneous.** PMID:31992138 is about colonic afferents and must not be read as
  a claim about cutaneous acid insensitivity. Its own authors point out that
  [PMID:31992138 "We have shown previously that pharmacological inhibition or genetic ablation of NaV1.7 in mouse does not impair colonic afferent firing or alter pain behaviours."],
  consistent with [PMID:32206859 "NaV1.7 is far more important in somatic pain than visceral pain"].
  I cite it only as independent corroboration of the mechanism, not as evidence about gut
  physiology.

## 6. What the affinage human-ortholog record missed

The `Scn9a-deep-research-affinage-human-ortholog.md` file is an affinage record for **human**
SCN9A (Q15858), retrieved as a conserved-mechanism baseline. It is a rich account of human
NaV1.7: channelopathies, CRMP2 SUMOylation and Nedd4-2 trafficking, endogenous opioid tone in
NaV1.7-null animals, ProTx2/acylsulfonamide structural pharmacology, olfaction.

What it does **not** contain, and what this review turns on:

1. **Nothing about the naked mole-rat, or about proton block of NaV1.7 at all.** Its 42
   citation-anchored findings include no naked-mole-rat paper and no pH/proton-block finding.
   PMID:22174253, PMID:24352952, PMID:31147513 and PMID:32206859 — the entire evidence base
   for the species-specific function — are absent. This is expected (affinage is human-only)
   but it means the record could not have driven this review's central call.
2. **Its GO grounding collapses to uninformative parents.** Its `mechanism_profile` gives
   molecular_activity as **GO:0005215 transporter activity** — three levels above
   GO:0005248 and not even channel-specific — for a protein whose defining activity is
   voltage-gated sodium channel activity. Following the brief, none of its GO ids were
   imported; every term in this review was re-grounded from GOA, QuickGO and the literature.
3. **Its own self-evaluation is a `tie`, not a `win`.** The file's frontmatter records
   `self_evaluation_pairwise: tie` against the curated UniProt reference. That is recorded in
   `references[].reference_review.correctness: LOW_QUALITY` with an explanatory note, rather
   than `VERIFIED`.

It was nonetheless useful for one thing: confirming that the conserved (human) NaV1.7 is a
threshold-setting nociceptor channel, which is the background against which the naked-mole-rat
change is a *modulation* of an intact function rather than a loss of function. No sentence
from it is quoted as evidence anywhere in the review.

## 7. Review decisions, in one place

All 12 GOA rows are electronic (`GO_REF:0000002` InterPro2GO, `GO_REF:0000118`
TreeGrafter/PANTHER PTN000004433, `GO_REF:0000120` combined InterPro + PANTHER + UniRule).
There is no experimental GO annotation for this protein and none for any naked-mole-rat gene
relevant here.

| GO term | action | why |
|---|---|---|
| GO:0001518 voltage-gated sodium channel complex | ACCEPT | pore-forming alpha subunit; all four domains present in the fragment |
| GO:0005216 monoatomic ion channel activity | MODIFY → GO:0005248 | correct but uninformative; the specific child is independently annotated and literature-confirmed |
| GO:0005248 voltage-gated sodium channel activity | ACCEPT | core; confirmed on the naked-mole-rat protein itself |
| GO:0005261 monoatomic cation channel activity | MODIFY → GO:0005248 | correct but uninformative |
| GO:0005886 plasma membrane | ACCEPT | UniProt SubCell; required by the mechanism |
| GO:0006811 monoatomic ion transport | MODIFY → GO:0035725 | strict ancestor of an already-annotated term |
| GO:0006814 sodium ion transport | MODIFY → GO:0035725 | strict ancestor of an already-annotated term |
| GO:0016020 membrane | MODIFY → GO:0005886 | strict ancestor of an already-annotated term |
| GO:0019228 neuronal action potential | ACCEPT | naked-mole-rat nociceptors fire normally to heat and mechanical stimuli |
| GO:0035725 sodium ion transmembrane transport | ACCEPT | core |
| GO:0055085 transmembrane transport | MODIFY → GO:0035725 | strict ancestor of an already-annotated term |
| GO:0086010 membrane depolarization during action potential | ACCEPT | the mechanistic BP of a NaV alpha subunit |
| GO:0019233 sensory perception of pain | NEW (ISS) | the naked-mole-rat literature is entirely about this protein's role in this species' pain phenotype |

No `REMOVE`: every projected term describes a function the naked-mole-rat evidence positively
supports. The species-specific difference here is a *quantitative modulation of gating*
(greatly enhanced proton block), which refines the channel's behaviour rather than abolishing
any annotated function — exactly the case the brief warns against over-reading.

No `UNDECIDED`: unusually for a naked-mole-rat gene, this protein has a dedicated primary
literature, so nothing was left unresolved among the existing rows.
