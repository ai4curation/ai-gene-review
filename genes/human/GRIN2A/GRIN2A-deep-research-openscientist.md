---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-14T20:27:08.912651'
end_time: '2026-11-14T20:47:59.257744'
duration_seconds: 1250.35
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: GRIN2A
  gene_symbol: GRIN2A
  uniprot_accession: Q12879
  protein_description: 'RecName: Full=Glutamate receptor ionotropic, NMDA 2A {ECO:0000305};
    Short=GluN2A; AltName: Full=Glutamate [NMDA] receptor subunit epsilon-1; AltName:
    Full=N-methyl D-aspartate receptor subtype 2A; Short=NMDAR2A {ECO:0000303|PubMed:8768735};
    Short=NR2A; Short=hNR2A {ECO:0000303|PubMed:8061049}; Flags: Precursor;'
  gene_info: Name=GRIN2A {ECO:0000312|HGNC:HGNC:4585}; Synonyms=NMDAR2A;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the glutamate-gated ion channel (TC 1.A.10.1)
  protein_domains: ANF_lig-bd_rcpt. (IPR001828); Glu/Gly-bd. (IPR019594); Iono_Glu_rcpt_met.
    (IPR001508); Ionotropic_Glu_rcpt. (IPR015683); Iontro_rcpt_C. (IPR001320)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 17
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: GRIN2A-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: GRIN2A-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q12879
- **Protein Description:** RecName: Full=Glutamate receptor ionotropic, NMDA 2A {ECO:0000305}; Short=GluN2A; AltName: Full=Glutamate [NMDA] receptor subunit epsilon-1; AltName: Full=N-methyl D-aspartate receptor subtype 2A; Short=NMDAR2A {ECO:0000303|PubMed:8768735}; Short=NR2A; Short=hNR2A {ECO:0000303|PubMed:8061049}; Flags: Precursor;
- **Gene Information:** Name=GRIN2A {ECO:0000312|HGNC:HGNC:4585}; Synonyms=NMDAR2A;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the glutamate-gated ion channel (TC 1.A.10.1)
- **Key Domains:** ANF_lig-bd_rcpt. (IPR001828); Glu/Gly-bd. (IPR019594); Iono_Glu_rcpt_met. (IPR001508); Ionotropic_Glu_rcpt. (IPR015683); Iontro_rcpt_C. (IPR001320)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GRIN2A" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GRIN2A' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GRIN2A** (gene ID: GRIN2A, UniProt: Q12879) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# GRIN2A (GluN2A / NR2A) — Functional Annotation Report

**Gene:** GRIN2A (HGNC:4585) · **Synonyms:** NMDAR2A · **Protein:** Glutamate receptor ionotropic, NMDA 2A (GluN2A / NR2A / epsilon-1 subunit) · **UniProt:** Q12879 · **Organism:** *Homo sapiens* · **Family:** Glutamate-gated ion channel (TC 1.A.10.1)

---

## Summary

**GRIN2A encodes GluN2A (also called NR2A or the glutamate receptor ε1 subunit), the principal glutamate-binding regulatory subunit of the N-methyl-D-aspartate (NMDA) subtype of ionotropic glutamate receptor.** GluN2A does not function alone: it co-assembles with the obligatory GluN1 subunit (which binds the co-agonist glycine/D-serine) to build a heterotetrameric, glutamate-gated cation channel. The primary molecular activity of the receptor is **ligand-gated ion conduction** — specifically, it forms a non-selective cation channel that is highly permeable to Ca²⁺ and is subject to a voltage-dependent Mg²⁺ block. Because the channel opens only when glutamate binds *and* the postsynaptic membrane is depolarized (relieving the Mg²⁺ block), the GluN2A-containing NMDA receptor acts as a molecular **coincidence detector** at excitatory synapses. GluN2A is a ligand-gated ion channel subunit and signaling molecule — **not an enzyme or a solute transporter**; the "substrate" it conducts is Ca²⁺/Na⁺/K⁺, gated by the agonist glutamate. The gene symbol, organism, protein family, and domain architecture (ANF_lig-bd_rcpt, Glu/Gly-bd, Ionotropic_Glu_rcpt) all match the UniProt Q12879 target precisely; literature identity is unambiguous.

The gene product carries out its function at the **postsynaptic density (PSD) of mature excitatory (glutamatergic) synapses** in the central nervous system, with the extracellular N-terminal half of the protein facing the synaptic cleft and the C-terminal tail projecting into the postsynaptic cytoplasm, where it organizes downstream signaling. During development, cortical and hippocampal synapses undergo an activity- and experience-driven switch from GluN2B- to GluN2A-containing receptors, making GluN2A the hallmark subunit of the mature synapse. Functionally, Ca²⁺ entering through GluN2A-NMDARs is the trigger for the **CaMKII → CREB signaling cascade** that drives AMPA-receptor trafficking, spine enlargement, and long-term potentiation (LTP) — the cellular substrate of learning and memory — and it biases neural circuits toward stability rather than plasticity.

Clinically, GRIN2A is the **glutamate-receptor gene most frequently mutated in human neurologic disease** and the leading monogenic cause of the **epilepsy-aphasia spectrum**. Its variants produce either gain- or loss-of-function of the NMDA receptor in a domain-dependent manner, which directly validates the structure-function map of the protein: mutations in the glutamate-binding and amino-terminal regulatory domains tend to reduce receptor function, while mutations in the channel-gating transmembrane/linker regions tend to increase it.

### Identity verification

The gene symbol, protein name, organism, family, and domain set given by UniProt are fully consistent with the published literature. The InterPro domains map one-to-one onto the experimentally defined NMDA-receptor architecture: **ANF_lig-bd_rcpt (IPR001828)** = extracellular amino-terminal domain (ATD); **Glu/Gly-bd (IPR019594)** = ligand-binding/agonist-binding domain (LBD/ABD); **Ionotropic_Glu_rcpt / Iono_Glu_rcpt_met (IPR015683, IPR001508)** = transmembrane ion-channel module; **Iontro_rcpt_C (IPR001320)** = intracellular C-terminal domain. There is **no ambiguity**: GRIN2A/Q12879 unambiguously denotes the human GluN2A subunit of the NMDA-type glutamate receptor. (A distinct body of work on *GRIN2A* somatic mutations in melanoma refers to the **same** gene/protein, not a homonym.)

---

## Key Findings

### Finding 1 — GluN2A is the glutamate-binding subunit of the NMDA receptor

GRIN2A encodes GluN2A, the regulatory subunit that binds the principal agonist, glutamate, within the NMDA-type ionotropic glutamate receptor. The receptor is an obligate heteromer: GluN2A must assemble with the GluN1 subunit (typically 2×GluN1 + 2×GluN2), and in the assembled receptor the two subunits bind different ligands — **GluN2A binds glutamate, while GluN1 binds the co-agonist glycine (or D-serine)**; both must be occupied for activation. The decisive experimental evidence localizing the glutamate site to GluN2A comes from disease-mutation electrophysiology: the **D731N mutation, located in the GluN2A agonist-binding domain (ABD) glutamate pocket, decreases glutamate potency by more than 3,000-fold** ([PMID: 28182669](https://pubmed.ncbi.nlm.nih.gov/28182669/)). A single residue substitution in the GluN2A ABD selectively crippling glutamate sensitivity is direct proof that this subunit houses the glutamate-binding pocket. A foundational description confirms the identity: *"GRIN2A encodes the regulatory GluN2A subunit of the glutamate-gated N-methyl-d-aspartate receptor (NMDAR)"* ([PMID: 24455489](https://pubmed.ncbi.nlm.nih.gov/24455489/)). This is fully consistent with the UniProt Q12879 domain set — ANF_lig-bd_rcpt (IPR001828) and the Glu/Gly-binding domain (IPR019594) — confirming the correct protein.

GluN2A is **not an enzyme or transporter in the classical sense**: it is a ligand-gated ion channel subunit. The assembled NMDAR is a non-selective cation channel that is **highly permeable to Ca²⁺** (in addition to Na⁺/K⁺) and shows a hallmark **voltage-dependent Mg²⁺ block** relieved by depolarization.

### Finding 2 — GRIN2A is a major monogenic locus for the epilepsy-aphasia spectrum, with domain-dependent gain- vs. loss-of-function

GRIN2A is the glutamate-receptor gene most often affected by neurologic-disease mutations, and seizure disorders constitute the largest category of affected patients ([PMID: 25904555](https://pubmed.ncbi.nlm.nih.gov/25904555/): *"the GRIN2A gene encoding the GluN2A N-methyl-d-aspartate receptor subunit being most often affected"*). In a cohort of **248 individuals**, pathogenic GRIN2A variants produced a clinical spectrum ranging from mild epilepsy with speech delay to severe developmental and epileptic encephalopathy — strongly within the **epilepsy-aphasia spectrum**. Critically, the phenotype tracked with **both the domain location of the mutation and its functional consequence**: missense variants in the **transmembrane and linker domains (misTMD+Linker)** produced severe phenotypes and predominantly NMDAR **gain-of-function**, whereas missense variants in the **amino-terminal and ligand-binding domains (misATD+LBD)** and null variants caused less severe phenotypes and **loss-of-function** (discovery P = 1×10⁻⁶; validation P = 0.0003) ([PMID: 30544257](https://pubmed.ncbi.nlm.nih.gov/30544257/): *"misTMD+Linker predominantly led to NMDAR gain-of-function, while misATD+LBD exclusively caused NMDAR loss-of-function"*).

This genotype–function–phenotype correlation is itself a powerful structure-function readout: it indicates that the transmembrane/linker region controls channel gating (so mutations there open the channel too easily), whereas the ATD and LBD regulate and bind ligand (so mutations there weaken the response). It also rationalizes divergent precision therapies — NMDAR antagonists (e.g., memantine) for gain-of-function and co-agonist supplementation (L-serine) for loss-of-function ([PMID: 36516565](https://pubmed.ncbi.nlm.nih.gov/36516565/)).

### Finding 3 — GluN2A-NMDARs reside in the postsynaptic density and predominate at mature synapses after a developmental GluN2B→GluN2A switch

GluN2A (NR2A)-containing NMDARs are concentrated at the **postsynaptic density (PSD)** of excitatory synapses — the electron-dense scaffold directly beneath the postsynaptic membrane. Their abundance there is actively maintained: the auxiliary CUB-domain protein **Neto1** is required to keep NR2A-NMDARs at the PSD, and Neto1-null mice shift LTP subunit-dependency away from NR2A-NMDARs and show depressed hippocampal LTP, learning, and memory ([PMID: 19243221](https://pubmed.ncbi.nlm.nih.gov/19243221/): *"a novel component of the NMDAR complex critical for maintaining the abundance of NR2A-containing NMDARs in the postsynaptic density"*).

GluN2A is the signature subunit of the **mature** synapse. During cortical and hippocampal development there is an **activity- and sensory-experience-driven switch from NR2B- to NR2A-containing NMDARs** ([PMID: 21521618](https://pubmed.ncbi.nlm.nih.gov/21521618/): *"In cerebral cortex there is a developmental switch from NR2B- to NR2A-containing NMDA receptors (NMDARs) driven by activity and sensory experience."*). This switch requires joint NMDAR + mGluR5 activation signaling through the PLC/IP3R-Ca²⁺-release/PKC pathway, and is deficient in mGluR5-knockout mice in vivo (in both CA1 and visual cortex). Independent biochemical evidence from in situ photoaffinity labeling shows the adult NR2A-type (175 kDa) NMDAR labeling pattern emerges around postnatal day 10, confirming NR2A as a structural marker of receptor maturation ([PMID: 8378316](https://pubmed.ncbi.nlm.nih.gov/8378316/)).

### Finding 4 — Ca²⁺ permeability and voltage-dependent Mg²⁺ block make GluN2A-NMDARs molecular coincidence detectors required for circuit refinement

The defining biophysical property of the NMDA receptor is that it is a non-selective cation channel that is **highly permeable to Ca²⁺** and subject to a **voltage-dependent Mg²⁺ block** that is relieved by postsynaptic depolarization. Consequently, channel opening requires the simultaneous occurrence of two events: **presynaptic glutamate release AND postsynaptic depolarization** — the biophysical definition of coincidence detection. The causal importance of these properties was shown genetically: an NR1 N598R mutation that renders NMDARs Mg²⁺-insensitive and Ca²⁺-impermeable **prevents whisker-related somatotopic ("barrelette") pattern formation** in the mouse brainstem despite normal receptor expression ([PMID: 12657691](https://pubmed.ncbi.nlm.nih.gov/12657691/): *"coincidence-dependent calcium signaling by NMDA receptors (NMDARs) under control of the voltage-dependent Mg2+ block might play a special role"*; and *"This leads to the expression of functional NMDARs that are Mg2+ insensitive and Ca2+ impermeable."*). This demonstrates that coincidence-gated Ca²⁺ signaling by NMDARs is **necessary for activity-dependent synaptic map refinement**, not merely correlated with it.

### Finding 5 — GluN2A-NMDAR Ca²⁺ influx triggers the CaMKII → AMPAR-trafficking cascade underlying LTP and memory

Ca²⁺ admitted through postsynaptic NMDARs is the trigger for the central plasticity cascade. At mature synapses this Ca²⁺ **primarily activates Ca²⁺/calmodulin-dependent protein kinase II (CaMKII)** and drives its autophosphorylation, which renders the kinase calcium-independent so that its signaling **outlasts the brief NMDAR Ca²⁺ transient** ([PMID: 34051268](https://pubmed.ncbi.nlm.nih.gov/34051268/): *"the elevated calcium levels activate primarily calcium/calmodulin-dependent kinase II (CaMKII) and cause its autophophorylation"*). Sustained CaMKII activity then drives the **trafficking of AMPA-type glutamate receptors into the postsynaptic density** and structural enlargement of the spine ([PMID: 34375719](https://pubmed.ncbi.nlm.nih.gov/34375719/): *"Activation of postsynaptic NMDA type glutamate receptor (NMDA-R) induces trafficking of AMPA type glutamate receptors (AMPA-R) and other proteins to the synapse in sequential fashion."*). This is the molecular basis of **long-term potentiation (LTP)**, the cellular correlate of learning and memory. The reverse manipulation confirms the direction of causality: NMDAR hypofunction downregulates the CaMKII → ERK1/2 → CREB cascade and impairs LTP and recognition memory ([PMID: 36417808](https://pubmed.ncbi.nlm.nih.gov/36417808/); [PMID: 33882624](https://pubmed.ncbi.nlm.nih.gov/33882624/)).

### Finding 6 — The GluN2A-specific intracellular C-terminal domain couples NMDARs to CaMKII/CREB signaling and promotes mature-circuit stability

GluN2A and GluN2B are most divergent in their long intracellular **C-terminal tails**, which recruit distinct sets of signaling proteins; this is the structural basis for their different downstream effects. NR1/NR2A receptors are mainly expressed in mature neurons and **induce circuit stability**, whereas NR1/NR2B receptors predominate in immature neurons and promote plasticity and dendritogenesis ([PMID: 28160495](https://pubmed.ncbi.nlm.nih.gov/28160495/): *"NR1NR2B receptors are predominantly expressed in immature neurons and promote plasticity, NR1NR2A receptors are mainly expressed in mature neurons and induce circuit stability"*; and *"this is likely related to the presence of their distinct C-terminal sequences that couple different signaling proteins"*). Mechanistically, CaMKII is recruited to the GluN2 C-terminal domain, and engineering a GluN2A construct with increased CaMKII interaction (NR2AΔIN) reactivates dendritogenesis in mature hippocampal neurons both in vitro and in vivo — demonstrating that the GluN2A C-tail's CaMKII coupling, acting through CREB phosphorylation and the histone mark H3K27ac, controls the transcriptional program that governs the plasticity-versus-stability transition. GluN2A-NMDARs also interact with the PSD-95/MAGUK scaffold and are regulated by calmodulin and α-actinin at the PSD.

### Finding 7 — GluN1/GluN2A NMDARs are modular heterotetramers allosterically gated via the GluN2A amino-terminal domain (high-affinity Zn²⁺ / proton inhibition)

Cryo-EM and crystal structures of the GluN1/GluN2A NMDA receptor reveal a **layered, modular heterotetramer** with four structural tiers, each corresponding to UniProt-annotated domains:

1. an extracellular **amino-terminal domain (ATD)** — the ANF_lig-bd_rcpt / IPR001828 region;
2. a **ligand-binding domain (LBD/ABD)** — the Glu/Gly-bd / IPR019594 region, where GluN2A binds glutamate and GluN1 binds glycine;
3. a **transmembrane ion-channel domain** forming the Ca²⁺-permeable pore and Mg²⁺-block site;
4. an intracellular **C-terminal domain**.

A subtype-defining feature of GluN2A-containing receptors is **allosteric inhibition by nanomolar zinc and by low pH**. Zinc binds a high-affinity site in the cleft of the GluN2A ATD bi-lobe; this binding elicits structural changes transduced through the LBD that constrict the channel gate and lower open probability ([PMID: 30500536](https://pubmed.ncbi.nlm.nih.gov/30500536/): *"zinc binding to the amino terminal domain elicits structural changes that are transduced though the ligand-binding domain and result in constriction of the ion channel gate"*; [PMID: 27916457](https://pubmed.ncbi.nlm.nih.gov/27916457/): *"their ion channel activity is allosterically inhibited by a nano-molar concentration of zinc that binds to an extracellular domain called an amino-terminal domain (ATD)"*). This ATD-based allosteric mechanism is evolutionarily conserved — the conformational closure induced by zinc on GluN2A is structurally analogous to that induced by ifenprodil on GluN2B ([PMID: 26170175](https://pubmed.ncbi.nlm.nih.gov/26170175/)).

---

## Mechanistic Model / Interpretation

The findings integrate into a single coherent picture of GluN2A as the **glutamate-sensing, Ca²⁺-conducting, plasticity-gating subunit of the mature excitatory synapse.**

### Receptor architecture and ligand logic

```
   SYNAPTIC CLEFT (extracellular)
   ┌───────────────────────────────────────────────────────┐
   │  ATD layer   [GluN2A ATD]  ← Zn2+ (nM), H+ (low pH)   ← allosteric brake
   │              [GluN1 ATD ]
   │  ─────────────────────────────────────────────────────
   │  LBD layer   [GluN2A ABD] ← GLUTAMATE (agonist)
   │              [GluN1 ABD ] ← GLYCINE / D-SERINE (co-agonist)
   ├───────────────────────────────────────────────────────┤
   │  TMD / PORE  voltage-dependent Mg2+ block;  Ca2+-permeable
   └───────────────────────────────────────────────────────┘
   POSTSYNAPTIC CYTOPLASM
      [GluN2A C-terminal tail] → recruits CaMKII → CREB / H3K27ac
```

**Gating requires a logical AND of three conditions:** (1) glutamate bound at the GluN2A ABD, (2) glycine/D-serine bound at the GluN1 ABD, and (3) membrane depolarization to expel Mg²⁺ from the pore. Only then does the Ca²⁺-permeable channel open. The GluN2A ATD superimposes a tunable allosteric brake — nanomolar Zn²⁺ and protons close the ATD bi-lobe and dampen the channel — allowing the local chemical environment to set receptor sensitivity.

### From ion flux to memory

```
Glutamate (presynaptic release) + postsynaptic depolarization
        │
        ▼
GluN2A/GluN1 NMDAR opens  ──►  Ca2+ influx into spine
        │
        ▼
Ca2+/calmodulin  ──►  CaMKII activation + autophosphorylation (Ca2+-independent)
        │                         (signal outlasts the Ca2+ transient)
        ▼
AMPAR trafficking into PSD  +  spine enlargement   ──►  LTP (learning & memory)
        │
        └──►  CaMKII → ERK1/2 → CREB → H3K27ac  ──►  transcriptional stabilization
```

### Developmental and functional role

The receptor's coincidence-detection property makes it the molecular arbiter of **activity-dependent circuit refinement**: only coincident, correlated pre- and post-synaptic activity opens the channel and admits the Ca²⁺ needed to strengthen a synapse ("cells that fire together, wire together"). Early in development GluN2B dominates, favoring plasticity; sensory experience and activity then drive a **GluN2B→GluN2A switch**, after which the GluN2A C-terminal tail reconfigures downstream signaling to **stabilize** mature circuits. This explains why GluN2A is the hallmark of the mature synapse and why its loss derails both learning and the normal maturation of language and cortical networks.

### Disease logic as a structure-function validation

| Mutated domain | Effect on channel | Typical phenotype |
|---|---|---|
| ATD + LBD (misATD+LBD), null variants | **Loss-of-function** (weakened ligand response / regulation) | Milder; epilepsy-aphasia, speech delay |
| TMD + Linker (misTMD+Linker) | **Gain-of-function** (channel opens too readily) | More severe; developmental & epileptic encephalopathy |

This clean split (P = 1×10⁻⁶ discovery; P = 0.0003 validation) is an independent, human-genetics confirmation of the modular model: ligand-binding/regulatory domains set the "go/no-go" and sensitivity of the receptor, while transmembrane/linker elements execute gating.

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the findings |
|---|---|---|
| [24455489](https://pubmed.ncbi.nlm.nih.gov/24455489/) | Evidence that GRIN2A mutations in melanoma correlate with decreased survival | States GluN2A is the regulatory subunit of the glutamate-gated NMDAR (identity) — F1 |
| [28182669](https://pubmed.ncbi.nlm.nih.gov/28182669/) | De novo loss-of-function GRIN2A mutation in childhood focal epilepsy/aphasia | D731N in GluN2A ABD cuts glutamate potency >3,000-fold → localizes glutamate pocket to GluN2A — F1 |
| [25904555](https://pubmed.ncbi.nlm.nih.gov/25904555/) | Ionotropic GABA/Glutamate receptor mutations and human neurologic disease | GRIN2A most frequently mutated glutamate-receptor gene in neurologic disease — F2 |
| [30544257](https://pubmed.ncbi.nlm.nih.gov/30544257/) | GRIN2A-related disorders: genotype & functional consequence predict phenotype | 248-patient cohort; domain-dependent gain- vs loss-of-function — F2 |
| [36516565](https://pubmed.ncbi.nlm.nih.gov/36516565/) | GRIN2A-related epilepsy and speech disorders (review) | Primary monogenic cause of epilepsy-aphasia; precision-therapy rationale — F2 |
| [19243221](https://pubmed.ncbi.nlm.nih.gov/19243221/) | Neto1 is a CUB-domain NMDAR-interacting protein | NR2A-NMDARs localized to PSD; Neto1 maintains their abundance — F3 |
| [21521618](https://pubmed.ncbi.nlm.nih.gov/21521618/) | mGluR5 and NMDARs drive the NR2B→NR2A switch | Activity/experience-driven developmental subunit switch — F3 |
| [8378316](https://pubmed.ncbi.nlm.nih.gov/8378316/) | Photoaffinity ligand labeling of NMDAR subtypes | Adult NR2A-type (175 kDa) pattern emerges ~P10 → maturation marker — F3 |
| [12657691](https://pubmed.ncbi.nlm.nih.gov/12657691/) | Absence of whisker pattern in mice with NMDARs lacking coincidence detection | Ca²⁺ permeability + Mg²⁺ block necessary for circuit refinement — F4 |
| [34051268](https://pubmed.ncbi.nlm.nih.gov/34051268/) | CaMKII autophosphorylation for NMDAR-dependent potentiation | Ca²⁺ influx primarily activates CaMKII with autophosphorylation — F5 |
| [34375719](https://pubmed.ncbi.nlm.nih.gov/34375719/) | Molecular mechanism of hippocampal LTP | NMDAR activation triggers AMPAR trafficking underlying LTP — F5 |
| [36417808](https://pubmed.ncbi.nlm.nih.gov/36417808/) | GluN1 antibody causes deficits via CaMKIIβ signaling | NMDAR hypofunction downregulates CaMKII→ERK→CREB, impairs memory — F5 |
| [33882624](https://pubmed.ncbi.nlm.nih.gov/33882624/) | Fisetin reverses impaired plasticity in schizophrenia model | Links NMDAR function to CaMKII/CREB/ERK and AMPAR GluA1 — F5 |
| [28160495](https://pubmed.ncbi.nlm.nih.gov/28160495/) | NMDAR subunit composition controls dendritogenesis via CaMKII/CREB/H3K27ac | GluN2A C-tail couples CaMKII/CREB; NR2A→stability, NR2B→plasticity — F6 |
| [30500536](https://pubmed.ncbi.nlm.nih.gov/30500536/) | Mechanisms for zinc and proton inhibition of GluN1/GluN2A | ATD zinc binding transduced through LBD constricts channel gate — F7 |
| [27916457](https://pubmed.ncbi.nlm.nih.gov/27916457/) | Molecular basis for high-affinity zinc inhibition in GluN2A ATD | Nanomolar zinc inhibition at GluN2A ATD is subtype-defining — F7 |
| [26170175](https://pubmed.ncbi.nlm.nih.gov/26170175/) | Conserved structural mechanism: ifenprodil vs zinc | ATD allosteric inhibition conserved (zinc/GluN2A ↔ ifenprodil/GluN2B) — F7 |

**Supported hypotheses:** H1 GluN2A is the glutamate-binding subunit ✅; H2 PSD localization / mature-synapse marker ✅; H3 coincidence detection drives refinement ✅; H4 Ca²⁺→CaMKII→AMPAR/CREB underlies LTP ✅; H5 C-tail biases toward circuit stability ✅; H6 modular ATD Zn²⁺/proton allostery ✅; H7 leading epilepsy-aphasia locus with domain-dependent GoF/LoF ✅.

**Refuted / ruled out:** GluN2A is **not** an enzyme catalyzing a metabolic reaction and **not** a solute transporter — it is a ligand-gated ion channel subunit. The gene symbol is **not ambiguous** for this organism.

---

## Limitations and Knowledge Gaps

- **Literature-based conclusions.** No primary dataset was provided; all conclusions rest on published experimental and structural evidence.
- **Species of evidence.** Several mechanistic studies (barrelette coincidence-detection, Neto1, NR2B→NR2A switch, dendritogenesis) are rodent/in vitro. The core biochemistry (ligand binding, Ca²⁺ permeability, zinc allostery, CaMKII coupling) is highly conserved and corroborated by human structural and genetic data, but some fine details are inferred for human by homology.
- **Triheteromeric receptors.** Many native adult NMDARs are **triheteromeric** (GluN1/GluN2A/GluN2B), with intermediate kinetics. This report treats the diheteromeric GluN1/GluN2A receptor as canonical; native mixed-receptor behavior in vivo is less completely characterized.
- **C-terminal interactome.** The full PSD interactome of the GluN2A C-tail (PSD-95/MAGUK, phosphatases, additional kinases) and how specific disease mutations perturb it is not exhaustively mapped here.
- **Non-neuronal roles.** Functional NMDARs outside the CNS (e.g., vascular/immune cells, melanoma) are emerging but mechanistically less precise and were treated as secondary to the core synaptic function.
- **Variant-level functional data.** Although the domain-level gain/loss split is statistically robust, functional annotation of individual rare human variants remains incomplete, limiting precision-therapy decisions.

---

## Proposed Follow-up Experiments / Actions

1. **Systematic deep-mutational / electrophysiological scan of GRIN2A variants** across ATD, LBD, TMD-linker, and CTD, measuring glutamate EC₅₀, open probability, Ca²⁺ flux, and zinc/proton sensitivity — to convert the domain-level gain/loss rule into residue-level functional calls that guide precision therapy (memantine for gain-of-function; D-serine/co-agonists for loss-of-function).
2. **Human-neuron (iPSC) validation** of the GluN2B→GluN2A developmental switch and its dependence on mGluR5/PLC/IP3R signaling, to confirm rodent mechanisms in human synapses and define the maturation timeline.
3. **Structure-guided mapping of the GluN2A C-terminal CaMKII docking site** by cryo-EM/cross-linking MS of the full-length receptor–CaMKII complex, testing how disease-associated CTD variants alter CaMKII/CREB coupling.
4. **In vivo Ca²⁺ imaging in GRIN2A gain- vs loss-of-function knock-in mice** to directly link altered coincidence detection to circuit-refinement, language, and seizure phenotypes.
5. **Triheteromeric receptor characterization** using subunit-tethered constructs to quantify how GluN2A dosage tunes Ca²⁺ signaling and plasticity thresholds in native-like receptors.

---

*Report generated from 7 confirmed findings and 31 reviewed papers across 5 investigation iterations. All claims are attributed to the cited primary literature and verified citation snippets.*


## Artifacts

- [OpenScientist final report](GRIN2A-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](GRIN2A-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:28182669
2. PMID:24455489
3. PMID:25904555
4. PMID:30544257
5. PMID:36516565
6. PMID:19243221
7. PMID:21521618
8. PMID:8378316
9. PMID:12657691
10. PMID:34051268
11. PMID:34375719
12. PMID:36417808
13. PMID:33882624
14. PMID:28160495
15. PMID:30500536
16. PMID:27916457
17. PMID:26170175