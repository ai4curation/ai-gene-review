# GPR158 review notes

Gene: human GPR158 (UniProt Q5T848), class C orphan-derived GPCR, HGNC:23689.
Reviewed as part of a contested-function batch (see also GPR75, GPR25).

## Why this gene is contested

Three competing models of what GPR158 "is" coexist in the 2017-2026 literature:

1. **Osteocalcin (OCN) receptor** — the bone-brain axis model.
2. **Metabotropic glycine receptor (mGlyR)** — the 2023 deorphanization.
3. **Ligand-independent RGS7-Gβ5 anchor / synaptic organizer** — the oldest and,
   by structural standards, the best-established role.

Crucially these are not mutually exclusive: the mGlyR model *is* built on the RGS7
model, because glycine binding is read out as inhibition of the receptor-bound
RGS7-Gβ5 complex, not as Gα activation.

## Model 3 (RGS7-Gβ5 anchoring) — the structural backbone

GPR158 was first characterised as an RGS-anchoring receptor:
[PMID:22689652 "We show that GPR158/179 recruited RGS complexes to the plasma membrane
and augmented their ability to regulate GPCR signaling."]

and then as an allosteric enhancer of RGS7 catalytic activity:
[PMID:25792749 "The results of this study establish GPR158 as an essential regulator of
RGS7 in the native nervous system with a critical role in controlling its expression,
membrane localization, and catalytic activity."]

Two independent 2021 cryo-EM structures nailed the architecture and the GPR158-RGS7
interface:
[PMID:34793198 "We further demonstrate the structural basis of GPR158 coupling to
RGS7-Gβ5."] and
[PMID:34815401 "Among class C GPCRs, GPR158 is unique as it lacks a Venus
flytrap-fold ligand-binding domain and terminates Gαi/o protein signaling through the
RGS7-Gβ5 heterodimer."]

The same 2019 study that provides the GOA `enzyme activator activity` IDA explicitly
reports that GPR158 does **not** behave as a canonical G-protein-activating GPCR:
[PMID:31189666 "no constitutive activity of GPR158 could be detected through the
measurement of various G-protein-mediated downstream responses"] and
[PMID:31189666 "We observed that GPR158 interacted with and stabilized the amount of
RGS7-β5 through a 50-residue region downstream of its transmembrane domain and upstream
of the VCPWE motifs."]

This is the most reproducible, most mechanistically resolved thing GPR158 does, and it
is the reason `GO:0008047` enzyme activator activity (IDA, two independent papers) is
treated here as **core**.

## Model 2 (metabotropic glycine receptor) — the 2023 deorphanization

[PMID:36996198 "We identified an orphan G protein-coupled receptor, GPR158, as a
metabotropic glycine receptor (mGlyR)."] with a defined binding site and a defined
effector:
[PMID:36996198 "Glycine and a related modulator, taurine, directly bind to a Cache
domain of GPR158, and this event inhibits the activity of the intracellular signaling
complex regulator of G protein signaling 7-G protein β5 (RGS7-Gβ5), which is associated
with the receptor."] and
[PMID:36996198 "Glycine signals through mGlyR to inhibit production of the second
messenger adenosine 3',5'-monophosphate."], with a cellular readout
[PMID:36996198 "We further show that glycine, but not taurine, acts through mGlyR to
regulate neuronal excitability in cortical neurons."]

This has **independent functional replication in a different laboratory and a different
brain region** (Aceto et al., Università Cattolica del Sacro Cuore, nucleus accumbens):
[PMID:38884814 "we found that glycine-dependent activation of GPR158 increased the
firing rate of NAc medium spiny neurons (MSNs)"]

A 2026 hippocampal study reports functional metabotropic glycine responses in CA3
pyramidal cells, Gi/o-dependent, though it does not itself manipulate GPR158:
[PMID:42347714 "These results indicate that there are functional mGlyRs in the
hippocampus and that they mediate their effects via Gi/o signaling."]

A contemporaneous commentary frames the deorphanization as accepted in the field:
[PMID:37321907 "Recent work by Laboute et al. deorphanized GPR158 as a metabotropic
glycine receptor (mGlyR)"]

UniProt has adopted it as the recommended protein name ("Metabotropic glycine receptor").
Position taken: `GO:0160079` is **core**, and the direction of residual doubt is about
whether glycine is the *only* or *dominant* physiological input, not about whether the
binding/response is real.

## Model 1 (osteocalcin receptor) — real signal, weaker molecular grounding

The OCN model rests on mouse genetics and electrophysiology rather than on direct
high-affinity binding to a defined pocket:
[PMID:28851741 "Genetic, electrophysiological, molecular, and behavioral assays identify
Gpr158, an orphan G protein-coupled receptor"] (Gpr158 mediates osteocalcin's regulation
of cognition, J Exp Med 2017).

Reviews continue to state it flatly:
[PMID:40337551 "As a critical receptor for OCN, G protein-coupled receptor 158 (GPR158)
facilitates the proliferation, differentiation, and survival of neural cells"]

But UniProt itself hedges this one ("may also act as a receptor for osteocalcin ...
By similarity"), and no GO term for osteocalcin binding/receptor activity is carried in
GOA for this gene. No new term is proposed here: the claim is a *candidate* second
ligand, and asserting it in a machine-readable slot would overstate the evidence.
It is recorded in `suggested_questions` instead.

## The 2025 ligand-independent module (Dev Cell)

[PMID:40393451 "Here, we identify a postsynaptic signaling complex comprising the G
protein-coupled receptor (GPCR)- GPR158 and a constitutively active phospholipase C (PLC)
family member, PLC X-domain containing 2 (PLCXD2), that controls SA abundance."] and
[PMID:40393451 "Together, our findings uncover a direct GPCR-like receptor-to-PLC
signaling pathway that bypasses canonical PLC regulation via G proteins."]

This is a *third* effector arm (RGS7-Gβ5, and now PLCXD2), and no ligand is invoked.
It does not contradict the glycine model; it reinforces the general picture that GPR158
is an atypical receptor that works by holding and gating intracellular effectors rather
than by activating Gα. It is the main reason GPR158's synapse-organisation annotations
(`GO:0050807`) are kept as genuine rather than demoted.

## The nucleus annotations (GO:0005634)

Two EXP annotations (PMID:23451275, PMID:30855200) from one group, in trabecular
meshwork / ocular cells:
[PMID:23451275 "Both endogenous and overexpressed GPR158 show an unusual subcellular
localization pattern, being found almost entirely in the nucleus."]

UniProt records the location but flags it as mechanistically unexplained: "Trafficks
between the nucleus and the cell membrane; it is unclear how a multi-pass membrane
protein can traffick between the nucleus and the cell membrane (PubMed:23451275)."

Per project rules an experimental annotation is not removed from an abstract reading.
Action taken: `KEEP_AS_NON_CORE` on all three `GO:0005634` rows (one IEA from the
SubCell mapping plus the two EXP rows), with the caveat recorded, because it is
cell-type-restricted, unreplicated outside this group, and irreconcilable with the
dimeric 7TM postsynaptic architecture that the structural work established.

## Curation position taken

- `GO:0008047` enzyme activator activity (IDA ×2, PMID:36996198 and PMID:31189666) →
  **ACCEPT, core**. Allosteric activation of RGS7-Gβ5 GAP activity. Best-supported MF.
- `GO:0160079` G protein-coupled glycine receptor activity (IDA) → **ACCEPT, core**.
  Independent replication exists; the reason field records that the ligand assignment
  is one of three competing models.
- `GO:0004930` GPCR activity and `GO:0004888` transmembrane signaling receptor activity
  → **MODIFY** to `GO:0160079`. Correct in kind but under-specific, and the canonical
  "activates an associated G protein" mechanism these terms imply is explicitly *not*
  what GPR158 does (PMID:31189666).
- `GO:0007186` GPCR signaling pathway → **MODIFY** to `GO:0008277` regulation of GPCR
  signaling pathway, which is what GPR158 actually does via RGS7-Gβ5.
- `GO:0008277`, `GO:0072659` (recruiting RGS7-Gβ5 to the membrane), `GO:0050807` →
  **ACCEPT**.
- `GO:0005886`, `GO:0045211`, `GO:0098839`, `GO:0016020` → **ACCEPT** (locations).
- `GO:0042734` presynaptic membrane → **KEEP_AS_NON_CORE** (UniProt: "Mainly localizes
  to the postsynaptic membrane, with a small portion to the presynaptic membrane").
- `GO:0005634` nucleus → **KEEP_AS_NON_CORE** (see above).
- `GO:0001956`, `GO:0007420`, `GO:0050890` → **KEEP_AS_NON_CORE** (organismal/distal
  phenotypes, not what the protein does).

## Unresolved

- Is osteocalcin a direct GPR158 ligand, or does GPR158 sit downstream of OCN action
  by another route? No direct-binding structure exists.
- Does glycine occupancy of the Cache domain account for the synaptic-organiser and
  PLCXD2 phenotypes, or are those genuinely ligand-independent?
- The nuclear pool: artefact of overexpression/antibody, a proteolytic fragment, or real?
