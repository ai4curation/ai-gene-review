# GRID1 (GluD1, glutamate receptor ionotropic delta-1) — review notes

UniProt: Q9ULK0. Human, 1009 aa, 3 TM segments + re-entrant pore loop, ATD + LBD
(S1/S2) + TMD + long CTD — the canonical iGluR architecture. UniProt places it in
the "glutamate-gated ion channel (TC 1.A.10.1) family, GRID1 subfamily".

## The contested question: is GluD1 an ion channel, and what is the agonist?

This is the whole review. GluD1 has the *architecture* of an ionotropic glutamate
receptor but does not behave like one, and the field currently holds several
mutually incompatible positions at once. GOA has annotated most of them.

### Position 1 — it is not a canonical ligand-gated channel; it is a scaffold/transducer

* Dai et al. 2021 Nature showed that GluD1's synaptic job is done without using the
  pore at all. Presynaptic neurexin–cerebellin complexes bind the GluD1 ATD and the
  signal is relayed through short CTD motifs:
  [PMID:34135511 "binding of presynaptic neurexin-cerebellin complexes to postsynaptic
  GluD1 controls glutamate receptor activity without affecting synapse numbers"].
  The killer experiment is the chimera:
  [PMID:34135511 "minimal GluD1 and GluD2 constructs containing only their N-terminal
  cerebellin-binding and C-terminal cytoplasmic domains, joined by an unrelated
  transmembrane region, fully control the levels of NMDA and AMPA receptors"].
  Conclusion: [PMID:34135511 "Thus, GluDs are signalling molecules that regulate NMDA
  and AMPA receptors by an unexpected transduction mechanism that bypasses their
  ionotropic receptor architecture and directly converts extracellular
  neurexin-cerebellin signals into postsynaptic receptor responses."]
* Itoh, Piot et al. 2024 PNAS is the direct refutation of the glycine/D-serine gating
  claim, with the controls the original work lacked (naive HEK cells and GluD2-null
  Purkinje neurons gave the same currents):
  [PMID:39052831 "these results cast doubt on the previously proposed hypothesis that
  extracellular ligands directly gate wild-type GluD channels"].
  UniProt carries this as an explicit CAUTION on Q9ULK0.
* The 2026 Acta Pharmacol Sin review takes this line:
  [PMID:41345253 "primarily due to its lack of classical ion channel activity. Recent
  advancements have redefined GluD1 as a multifunctional synaptic organizer, essential
  for the development, plasticity, and behavioral regulation of both excitatory and
  inhibitory circuits."]

### Position 2 — the pore is real and carries current in native neurons, but it is gated indirectly

* Gantz et al. 2020 eLife: in dorsal raphe serotonin neurons the alpha-1 adrenergic
  excitatory drive is carried by GluD1:
  [PMID:32234214 "mediated by the ionotropic glutamate receptor homolog cation channel,
  delta glutamate receptor 1 (GluD1). GluD1R-channels are constitutively active under
  basal conditions carrying tonic inward current"], and synaptic activation of
  alpha-1 adrenergic receptors augments that current.
* Copeland et al. 2023 EMBO Rep: the tonic component is not GPCR-driven at all:
  [PMID:37154294 "GluD1R carries a G-protein-independent tonic current that contributes
  to subthreshold neuronal excitation in the dorsal raphe nucleus."]
* Dadak et al. 2017 (GluD2, cerebellum/HEK): the current is opened downstream of a
  *different* receptor's Gq cascade:
  [PMID:27276689 "the activation of GluD2 channels via DHPG-induced mGlu1 stimulation is
  Gαq-dependent"] and [PMID:27276689 "the opening of the GluD2 channel by mGlu1 receptor
  mobilizes the canonical Gq-PLC-PKC pathway"].
  **Important for curation**: the GPCR here is mGlu1, not GluD. GOA nonetheless carries
  `GO:0099530 G protein-coupled receptor activity ...` as `enables` on GRID1 from this
  paper. GluD1 is a 3-TM tetrameric channel subunit; it is not a 7-TM GPCR. This is a
  role conflation (effector annotated as the agent), and the paper's own data are on
  GluD2.
* Kain et al. 2026 (**bioRxiv PREPRINT, not peer reviewed**): uses the same
  alpha-1-adrenergic route to evoke the current and finds proton block:
  [PMID:42427720 "GluD1R current is inhibited by physiological drops in extracellular pH.
  Unlike other iGluRs, protons inhibited GluD1R current via a voltage-independent decrease
  in unitary current."]
* Vinnakota & Kumar 2026 Commun Biol (a Comment, mostly about GluD2) offers a
  reconciliation — the channel is silent at room temperature because of a high energetic
  barrier: [PMID:41741709 "they resembled ion channels structurally but appeared
  functionally silent in standard room-temperature electrophysiological assays"].

### Position 3 — the agonist is GABA (2023), or acetylcholine (2026)

* Piot et al. 2023 Science: GluD1 binds GABA in its LBD. Crucially the authors are
  explicit that the downstream effect is **not** ionotropic:
  [PMID:38060673 "we demonstrate that GluD1 binds GABA, a previously unknown feature of
  iGluRs. GluD1 activation produces long-lasting enhancement of GABAergic synaptic
  currents in the adult mouse hippocampus through a non-ionotropic mechanism that is
  dependent on trans-synaptic anchoring."]
  So GO:0016917 *GABA receptor activity* is defensible on its GO definition ("Combining
  with gamma-aminobutyric acid (GABA), and transmitting the signal from one side of the
  membrane to the other to initiate a change in cell activity") — that definition does
  not require a current. GO:0004890 GABA-A (ionotropic) receptor activity would not be.
* Chettiar et al. 2026 Mol Psychiatry (abstract only in cache): GluD1 at cholinergic
  synapses, with ACh-evoked NASPM-sensitive currents:
  [PMID:42270762 "produced current responses in medium spiny neurons (MSNs) that were
  sensitive to the GluD1-channel blocker NASPM. These responses were absent in GluD1 KO
  and overexpression of GluD1 on KO background rescued Ach puff-induced currents
  suggesting potential conductance via GluD1."]
  Note the authors' own hedge ("suggesting potential conductance"), and that ligand
  binding was assessed only indirectly, via a GluD1–Cbln1 interaction/conformational
  assay. Same group's review (PMID:41345253) simultaneously says GluD1 lacks classical
  channel activity — the two 2026 papers from the same lab are not easy to reconcile.

### My position

1. **Core = trans-synaptic organizer / signal transducer.** This is the only role with
   converging, independently replicated, mechanism-level evidence (Dai 2021 chimeras;
   Piot 2023 requirement for trans-synaptic anchoring; Ryu 2011 presynaptic
   differentiation; Liu 2020 thalamostriatal circuit). Family membership is not function.
2. **Core = GABA receptor, non-ionotropic.** Direct structural + functional evidence
   (Piot 2023), and the GO term's definition fits.
3. **Non-core, but real = a cation conductance in native neurons** (Gantz 2020, Copeland
   2023), tonic and/or augmented by Gq-coupled receptors. Not directly transmitter-gated.
4. **Unresolved = direct transmitter gating** (`GO:1904315`). One 2026 report (ACh)
   supports it; the standing literature (PNAS 2024) and the GABA paper itself argue
   against it. `UNDECIDED` is the honest action.
5. **Wrong = the AMPA-receptor annotations.** GluD1 does not bind glutamate at all
   (UniProt: "does not bind glutamate as a primary ligand"), so `GO:0004971 AMPA glutamate
   receptor activity` (definition: "exhibits fast gating by glutamate") and
   `GO:0032281 AMPA glutamate receptor complex` are simply false, and the
   inter-ontology-inferred `GO:0035235 ionotropic glutamate receptor signaling pathway`
   falls with them.

## Why the AMPA IBAs are a propagation failure (not just a quibble)

`GO:0004971` and `GO:0032281` on GRID1 both come from PANTHER node
**PTN000438081**. Every donor in the WITH/FROM is an AMPA receptor subunit
(UniProtKB:P42261 = human GRIA1, P42263 = GRIA3, P48058 = GRIA4, MGI:95808 = mouse
Gria1, plus the rat Gria orthologues RGD:61862/61863/621531/70958). No delta-receptor
donor appears. The IBD was therefore placed on the AMPA-receptor clade, and GRID1 —
a member of the *delta* branch, which diverged before the AMPA/kainate/NMDA split —
should not be inside it. The same node also seeded `GO:0043197 dendritic spine`, which
happens to be true of GluD1 for independent reasons and so is harmless.

Contrast `GO:1904315`, which comes from the much broader node **PTN001826301** whose
donors span AMPA, kainate, NMDA *and* delta (UniProtKB:O43424 = human GRID2). That node
placement is a defensible judgement about the ancestral iGluR; the question there is
whether the delta branch retained direct transmitter gating, which is exactly the open
question. Hence REMOVE for the first pair, UNDECIDED for the second.

## The GOA incoherence, itemised

GOA currently asserts that one protein is, simultaneously:
* a GABA receptor (`GO:0016917`, IDA, PMID:38060673) — defensible, non-ionotropic;
* an AMPA glutamate receptor (`GO:0004971`, IBA) — false, mis-propagated;
* a G-protein-coupled receptor (`GO:0099530`, IDA, PMID:27276689) — structurally
  impossible; the GPCR in that paper is mGlu1;
* a transmitter-gated ion channel (`GO:1904315`, IBA/IEA/ISS) — unresolved;
* a generic ligand-gated ion channel (`GO:0015276`, IEA from InterPro) — the specific
  claim refuted by PMID:39052831;
* a signaling receptor regulator (`GO:0030545`, IDA, PMID:34135511) — correct, and the
  best single MF summary of what GluD1 actually does.

`GO:0099538 synaptic signaling via neuropeptide` (IDA from PMID:27276689, plus ISS and
IEA rows) is a third oddity: no neuropeptide appears anywhere in the GluD1 literature.
The GO *definition* ("Cell-cell signaling to or from a synapse, mediated by a peptide")
is loose enough that a curator could have reached it for cerebellin-mediated signalling,
but `GO:0099557` says that precisely and is already on the gene, so these rows are
re-pointed rather than kept.

`GO:0005515 protein binding` rests on two IntAct/BioPlex rows whose sole partner is
UniProtKB:P68871 = **haemoglobin subunit beta**, a textbook affinity-purification
contaminant and not a plausible partner for a postsynaptic receptor.
`GO:0070062 extracellular exosome` is HDA from a **urinary** exosome proteome
(PMID:19056867) — GluD1 is a brain protein.

## Non-core biology worth keeping

* Behaviour: Grid1 KO/conditional-KO mice show altered social behaviour and impaired
  behavioural flexibility — [PMID:31945419 "selective ablation of GluD1 from the dorsal
  striatum impairs behavioral flexibility in a water T-maze task"], with loss of
  thalamostriatal terminals. Supports `GO:0035176 social behavior` as non-core.
* GluD1 organises both excitatory and inhibitory presynaptic terminals, which is why the
  GABAergic-synapse localisation is not an error:
  [PMID:22138648 "GluD1 induced presynaptic differentiation of not only glutamatergic
  presynaptic terminals but also GABAergic ones"].

## Validation / provenance housekeeping

* All PMIDs cited here were fetched with `ai-gene-review fetch-pmid` and the titles,
  journals and years above come from the cached `publications/PMID_*.md` frontmatter.
* PMID:42270762 (Mol Psychiatry 2026) is **abstract-only** in the cache
  (`full_text_available: false`).
* PMID:42427720 is a **bioRxiv preprint** (`publication_type: PREPRINT`) and is flagged
  as such in `reference_review`.
