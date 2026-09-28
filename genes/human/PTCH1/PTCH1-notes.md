# PTCH1 (human, UniProt Q13635) — curation notes

Working journal for the GO annotation review. Append-only; newest sections at the bottom.

## 1. What the protein is

PTCH1 is a 1447-residue polytopic membrane protein with **12 transmembrane helices and two
large extracellular domains (ECD1, ECD2)**, plus a long cytoplasmic C-terminal tail. The
UniProt feature table lists TM1 at 100..117 and a second cluster of eleven helices from 438
onward, with the sterol-sensing domain annotated at 438..598. The cryo-EM work says the same
thing independently: [PMID:29954986 "Ptch1 comprises two interacting extracellular domains,
ECD1 and ECD2, and 12 transmembrane segments (TMs), with TMs 2 to 6 constituting the
sterol-sensing domain (SSD)."]

It belongs to the RND-permease superfamily (patched family; UniProt `SIMILARITY: Belongs to
the patched family`) and is the vertebrate orthologue of *Drosophila* `ptc`. Human has a
paralogue, PTCH2 (Q9Y6C5), in the same PANTHER family; the module review
(`modules/hedgehog_signaling.yaml`) groups Drosophila ptc, human PTCH1 and human PTCH2 in the
receptor tier under PANTHER:PTHR46022.

Four alternative-promoter/splice isoforms are recorded (Q13635-1 "L", -2 "L'", -3 "M", -4
"S"). Nothing in the GOA set is isoform-scoped, and I found no evidence that the reviewed
functions are isoform-specific, so no `isoform:` fields were added.

## 2. The two molecular functions that matter

### 2.1 Hedgehog ligand binding

PTCH1 is the high-affinity receptor for all three mammalian Hedgehog ligands. The original
biochemistry is unambiguous and covers the whole ligand family at once:
[PMID:9811851 "Biochemical analysis of PTCH and PTCH2 shows that they both bind to all
hedgehog family members with similar affinity and that they can form a complex with SMO."]
That single sentence is the evidential basis for three of the GOA rows (the three
`GO:0097108 hedgehog family protein binding` IPIs against mouse Shh/Ihh/Dhh) and for the two
`GO:0005119 smoothened binding` IPIs.

The structures then explain *how*. The dominant contact is not protein–protein at all but
lipid-in-pocket: [PMID:29995851 "The palmitoylated N terminus of SHH-N inserts into a cavity
between the extracellular domains of PTCH1 and dominates the PTCH1-SHH-N interface"]. The
second lipid does the same on the other end — [PMID:31548691 "Shh inactivates PTCH1 by
grasping its extracellular domain with two lipidic pincers, the N-terminal palmitate and the
C-terminal cholesterol, which are both inserted into the PTCH1 protein core."]

Stoichiometry is **two receptors per ligand**, through two chemically distinct epitopes:
[PMID:30139912 "one SHH-N molecule engages both epitopes to bind two PTCH1 receptors in an
asymmetric manner"], and at higher order [PMID:31127104 "The structure shows that four Ptch1
protomers are organized as a loose dimer of dimers."] This matters for the review because it
is the one defensible reading of the orthology-transferred `GO:0005113 patched binding` row
(see §5.1): PTCH1 genuinely engages another PTCH1.

### 2.2 Sterol movement — the actual mechanism of SMO inhibition

The modern model is that PTCH1 is not a classical signal-transducing receptor but a
**transporter that keeps cholesterol away from SMO**, and that ligand binding switches the
transporter off. UniProt states it directly: `In absence of hedgehog, acts as an inhibitor of
smoothened protein (SMO) by preventing SMO access to cholesterol`, with a catalytic activity
line `Reaction=cholesterol(in) = cholesterol(out)`.

Evidence chain:

- Direct sterol binding and transport-like behaviour in a heterologous system:
  [PMID:21931618 "we demonstrate that purified Patched binds to cholesterol, and that the
  interaction of Shh with Patched inhibits the binding of Patched to cholesterol."] and
  [PMID:21931618 "We also show that over-expression of human Patched in the yeast S.
  cerevisiae results in a significant boost of BODIPY-cholesterol efflux."] Note the authors
  themselves hedge the cellular interpretation — [PMID:21931618 "Our results suggest that
  Patched may contribute to cholesterol efflux from cells, and to modulation of the
  intracellular cholesterol concentration."]
- Sterols are resolved all around the transmembrane domain and a translocation route is
  visible: [PMID:31555730 "The membrane-embedded part of PTCH1 is surrounded by 10 sterol
  molecules at the inner and outer lipid bilayer portion of the protein."] and
  [PMID:31555730 "The structure reveals a possible route for sterol translocation across the
  lipid bilayer by PTCH1 and homologous transporters."]
- Ligand binding closes the conduit: [PMID:31548691 "Molecular dynamics simulations show that
  this interaction leads to the closure of a tunnel through PTCH1 that serves as the putative
  conduit for sterol transport."]
- Energetics and ion coupling: [PMID:37611095 "we find an energetic barrier of ~15 to 20
  kilojoule per mole for cholesterol export"], with the framing
  [PMID:37611095 "PTCH1 inhibits the G protein-coupled receptor Smoothened (SMO) via a debated
  mechanism involving modulating ciliary cholesterol accessibility."]
- Independent restatement in a 2025 paper: [PMID:40128518 "Several studies showed that PTCH1
  functions as a cholesterol transporter to maintain the low concentration of cholesterol in
  cilia"].

This is exactly what `modules/hedgehog_signaling.yaml` encodes for the `patched_receptor`
annoton (MF `GO:0140303 intramembrane lipid carrier activity`, process
`GO:0045879 negative regulation of smoothened signaling pathway`, location plasma membrane),
and what the GO-CAM models record: `gocams/index.tsv` gives PTCH1 the same MF/BP pair with
location `GO:0098804 non-motile cilium membrane` in five human models
(696022cd00000812, 696022cd00000908, 696022cd00001146, 696022cd00001204, 696022cd00001246,
696022cd00001370). **No conflict with the module or the family reviews was found.**

One genuine tension worth recording: the 1998/2001 co-immunoprecipitation evidence that PTCH1
and SMO form a complex ([PMID:9811851] above; [PMID:11278759]) sits awkwardly with the
catalytic/sub-stoichiometric model, in which PTCH1 acts on the sterol pool rather than on SMO
directly. I did not remove the `smoothened binding` rows on that basis — they are experimental
IPIs and the observation stands — but they are marked non-core, because the core molecular
function is the sterol transport, and that is also how the module and every GO-CAM model
render the PTCH1→SMO relationship (causal inhibition, not binding).

## 3. Where it acts

Plasma membrane and, functionally, the **membrane of the non-motile primary cilium**. UniProt:
`Cell membrane ... Multi-pass membrane protein` and `Cell projection, cilium membrane`, with
the note that PTCH1 localises to the primary cilium and prevents SMO from getting there. The
caveolar/raft subpool is real but came from one 2001 study:
[PMID:11278759 "In this study, we demonstrate that both Smoothened and Patched are in
caveolin-1-enriched/raft microdomains."]

Ligand binding triggers internalisation and degradation — UniProt `PTM` records ITCH
ubiquitination at Lys-1426 in the unliganded state and SMURF1/2 ubiquitination in response to
SHH, `degradation is essential for PTCH1 clearance from the primary cilium and smoothened
pathway activation`. Reactome R-HSA-5632677 ("PTCH is internalized") is the source of the
`GO:0030666 endocytic vesicle membrane` row; this is a transit compartment on the way to
degradation rather than a site of function, hence non-core.

## 4. Disease and organismal roles

Germline loss of function causes nevoid basal cell carcinoma (Gorlin) syndrome
[PMID:8681379 "We propose that a reduction in expression of the patched gene can lead to the
developmental abnormalities observed in the syndrome and that complete loss of patched
function contributes to transformation of certain cell types."], with truncating mutations
predominating [PMID:8981943 "The preponderance of truncation mutants in the germ line of NBCCS
patients suggests that the developmental defects associated with the disorder are most likely
due to haploinsufficiency."] A nice period detail that anticipates the transport model:
[PMID:8981943 "Two missense mutations have been identified, and their location within
transmembrane domains supports the notion that PTCH may have a transport function."]

UniProt also lists basal cell carcinoma (MIM:605462) and holoprosencephaly 7 (MIM:610828).
The human-genetics IMPs in GOA (neural tube patterning, limb morphogenesis, pharyngeal system
development, somite development) all trace to the Gorlin phenotype and were kept as
**non-core**: they are genuine consequences of losing Hedgehog repression, but they are
downstream developmental outcomes, not the protein's own activity.

## 5. Annotation-by-annotation issues that needed digging

### 5.1 The PMID:10500113 cluster (reached human PTCH1 only as IEA)

Four human rows come by Ensembl-Compara transfer from mouse Ptch1 (Q61115) annotations whose
source is PMID:10500113, "Sonic hedgehog protein signals not as a hydrolytic enzyme but as an
apparent ligand for patched" (checked on PubMed). In mouse those rows are
`GO:0005113 patched binding` (IDA), `GO:0008201 heparin binding` (IDA),
`GO:0001841 neural tube formation` (IDA) and `GO:0007165 signal transduction` (IDA).

- **heparin binding** — there is no reported heparin-binding activity of human PTCH1, and the
  protein has no extracellular heparin-binding motif of the kind the Hedgehog ligands carry.
  Transferred electronically, it is an over-propagated IEA and I removed it. (I am *not*
  second-guessing the mouse experimental row, which I have not read in full; the removal is of
  the human electronic transfer, on the biology.)
- **patched binding** — read literally on Patched itself this is self-referential. The one
  reading that is both true and informative is homo-oligomerisation, which the structures
  establish directly, so this was modified to `GO:0042802 identical protein binding` rather
  than deleted.
- **neural tube formation** — the process is right for PTCH1 regardless of that row's
  provenance (mouse Ptch1 nulls have open neural tube; GOA also carries
  `GO:0001843 neural tube closure` IMP in mouse). Kept, non-core.
- **signal transduction** — correct but maximally general when `GO:0045879` is directly
  annotated seven times over; modified to the specific term.

### 5.2 The rat expression cluster

Twelve human IEA rows carry rat Ptch1 (Q6UY90 / ENSRNOP00000026287) in WITH/FROM. Tracing
them through the GO API, the rat originals split cleanly:

| rat term | evidence | rat source |
|---|---|---|
| spermatid development, prostate gland development, liver regeneration, response to xenobiotic stimulus / mechanical stimulus / estradiol / retinoic acid / alkaloid | **IEP** | 8 separate expression studies |
| dendritic growth cone, axonal growth cone, postsynaptic membrane | IDA | PMID:21618238 (subcellular localisation of Patched and Smoothened in hippocampal neurons) |
| commissural neuron axon guidance | IMP | PMID:19946319 |

The IEP block is the weakest material in the whole GOA set: PTCH1 is the canonical
transcriptional readout of Hedgehog pathway activity, so its mRNA moves in essentially any
tissue where the pathway is engaged. "Responds to X" derived from that is a statement about
pathway activity, not about PTCH1's function, and it was transferred to human with no human
evidence at all. All eight marked over-annotated. The three IDA localisations and the axon
guidance IMP rest on real perturbation/imaging experiments and were kept as non-core.

### 5.3 PMID:16229683 (Rahnama et al.) — the SMO-independent arm

Two human IMPs come from this paper. The abstract carries the transcription claim
[PMID:16229683 "We show that gene activation by GLI1, the transcriptional effector of the
pathway, can be down-regulated by PTCH1 without involvement of the canonical cascade of HH
signalling events."] and the full text carries the differentiation assay — figure legend
[PMID:16229683 "Inhibition of GLI1-induced osteogenic differentiation by PTCH1."] with the
text stating that PTCH1 significantly inhibited GLI1-induced AP staining in C3H10T1/2 cells.
Both rows are supported, but both are transfection/overexpression readouts of a non-canonical
arm, and PTCH1 is not itself a transcriptional regulator, so both are non-core.

### 5.4 PMID:17850284 (Jenkins et al.) — descriptive human IHC

Source of one IDA (`GO:0045177 apical part of cell`) and two IEPs (`GO:0048745 smooth muscle
tissue development`, `GO:0072205 metanephric collecting duct development`). The IDA is direct
and quotable [PMID:17850284 "Exploiting the polar distribution of PTCH at the apical surface
of collecting duct cells"]. The two IEPs are expression correlations in fixed human tissue,
and the authors say so themselves [PMID:17850284 "Collectively, these descriptive results
generate new hypotheses regarding SHH signal transduction in human urinary tract development
and help to explain the varied urinary tract malformation phenotypes noted in individuals with
mutations in the SHH pathway."] — hypothesis-generating, hence over-annotated.

### 5.5 Generic `GO:0005515 protein binding` (7 rows)

Per CLAUDE.md, only MODIFY / REMOVE / UNDECIDED are available. Partner identities were taken
from the UniProt `INTERACTION` block and each accession checked against UniProt:

- P14635 = CCNB1 (human) via PMID:19502428 → modified to `GO:0030332 cyclin binding`, which
  the same paper supports [PMID:19502428 "Interaction of GRK2, K220R, and BP with PTCH1
  reduces the association of PTCH1 with cyclin B1 and disrupts PTCH1-mediated inhibition of
  cyclin B1 nuclear translocation, whereas the PTCH1-binding deficient GRK2 mutant
  (Delta312-379) does not."]
- P25098 = GRK2 (human) and P21146 = GRK2 (bovine), same paper → modified to
  `GO:0019901 protein kinase binding`; GRK2 is a kinase and the interaction is the paper's
  central claim [PMID:19502428 "A physical interaction between GRK2 and cyclin B1 regulator
  patched homolog 1 (PTCH1), stimulated by Hedgehog (Hh), rather than GRK2-mediated
  phosphorylation of downstream targets, appears as the underlying mechanism."]
- Q15465 = SHH (human) via PMID:19561609 → modified to
  `GO:0097108 hedgehog family protein binding`.
- Q4KMG0 = CDON (human) and O35158 = Cdon (rat) via PMID:21802063 → removed. The interaction
  is real [PMID:21802063 "In contrast, wild-type CDON associates with PTCH1 and GAS1, but the
  variants do so inefficiently, in a manner that parallels their activity in cell-based
  assays."] but no GO molecular function describes receptor–co-receptor association any more
  informatively than the bare term does; the functional consequence already sits on CDON as
  `GO:0140597 protein carrier activity` in GO-CAM 696022cd00000908.
- P46937 = YAP1 via PMID:25283809 → removed; a WW-domain/PPxY biophysics study with no
  connection to an established PTCH1 molecular function.

Removal here never means the interaction is false — only that the bare term records nothing
about what PTCH1 does.

### 5.6 `GO:0016485 protein processing` (ISS from mouse)

The mouse source is an IMP in PMID:16061793 ("Cilia and Hedgehog responsiveness in the
mouse"), qualified `acts_upstream_of_or_within` — i.e. GLI processing changes when Ptch1 is
perturbed. The human row asserts `involved_in`. PTCH1 has no proteolytic activity and cleaves
nothing; the GLI3 processing effect is a downstream consequence of pathway repression that
`GO:0045879` already captures. Removed on the participation test.

### 5.7 `GO:0010875 positive regulation of cholesterol efflux` (IDA, PMID:21931618)

Kept in substance but retermed. The paper's own data have Patched *performing* the movement
(purified protein binds cholesterol; heterologous expression in yeast boosts efflux), not
regulating someone else's transporter, and the direction/destination ("out of the cell") is
precisely the part that later work reframed as leaflet-level accessibility. Modified to
`GO:0034204 lipid translocation`, which is what the structures and simulations support and
which GOA already carries here as an inter-ontology IEA from `GO:0140303`.

### 5.8 `GO:0072659 protein localization to plasma membrane` (IDA, PMID:11278759)

The supporting observation is [PMID:11278759 "Immunocytochemistry data and fractionation
studies also show that Patched seems to be required for transport of Smoothened to the
membrane."] — note the authors' own "seems to be". The direction of PTCH1's effect on SMO
localisation is now understood the other way round (PTCH1 restricts SMO accumulation at the
ciliary membrane; UniProt: `prevents cilium localization of SMO`). Marked over-annotated
rather than removed, since PTCH1 does control SMO's membrane distribution — just not by
delivering it there. The companion general term `GO:0032880 regulation of protein
localization` was modified to `GO:1903565 negative regulation of protein localization to
cilium`, which states the established direction.

## 6. NEW terms: none proposed

Checked against the participation and comparator tests. The module's PTCH1 annoton
(`GO:0140303` / `GO:0045879` / plasma membrane) and all six GO-CAM activities in
`gocams/index.tsv` use terms that are **already present** in the GOA set, including
`GO:0098804 non-motile cilium membrane`. The candidate I did consider,
`GO:1903565 negative regulation of protein localization to cilium`, is introduced as a
MODIFY replacement for an existing row rather than as a new assertion, so nothing is added
that a curator has not already been in a position to add.

## 7. Open questions carried into the review

- Direction and stoichiometry of the transported sterol. UniProt calls the mechanism unclear
  and offers outer→inner leaflet exchange for K+/Na+; [PMID:37611095] models export coupled to
  one to three Na+ or two to three K+. Nobody has measured it on a native ciliary membrane.
- Whether the PTCH1–SMO complex seen by co-IP has any role, given that inhibition is
  sub-stoichiometric and lipid-mediated.
- Whether the cyclin B1 / GRK2 arm operates at endogenous expression levels in human tissue,
  or is a property of overexpression.
