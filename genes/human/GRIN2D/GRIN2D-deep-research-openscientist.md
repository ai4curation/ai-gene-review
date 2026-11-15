---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-14T20:26:30.772431'
end_time: '2026-11-14T20:58:33.346103'
duration_seconds: 1922.57
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: GRIN2D
  gene_symbol: GRIN2D
  uniprot_accession: O15399
  protein_description: 'RecName: Full=Glutamate receptor ionotropic, NMDA 2D {ECO:0000305};
    Short=GluN2D {ECO:0000303|PubMed:36959261}; AltName: Full=EB11; AltName: Full=Glutamate
    [NMDA] receptor subunit epsilon-4 {ECO:0000250|UniProtKB:Q03391}; AltName: Full=N-methyl
    D-aspartate receptor subtype 2D; Short=NMDAR2D {ECO:0000303|PubMed:9489750}; Short=NR2D;
    Flags: Precursor;'
  gene_info: Name=GRIN2D {ECO:0000303|PubMed:27616483, ECO:0000312|HGNC:HGNC:4588};
    Synonyms=GluN2D {ECO:0000303|PubMed:36959261}, NMDAR2D {ECO:0000303|PubMed:9489750};
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
citation_count: 18
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: GRIN2D-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: GRIN2D-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** O15399
- **Protein Description:** RecName: Full=Glutamate receptor ionotropic, NMDA 2D {ECO:0000305}; Short=GluN2D {ECO:0000303|PubMed:36959261}; AltName: Full=EB11; AltName: Full=Glutamate [NMDA] receptor subunit epsilon-4 {ECO:0000250|UniProtKB:Q03391}; AltName: Full=N-methyl D-aspartate receptor subtype 2D; Short=NMDAR2D {ECO:0000303|PubMed:9489750}; Short=NR2D; Flags: Precursor;
- **Gene Information:** Name=GRIN2D {ECO:0000303|PubMed:27616483, ECO:0000312|HGNC:HGNC:4588}; Synonyms=GluN2D {ECO:0000303|PubMed:36959261}, NMDAR2D {ECO:0000303|PubMed:9489750};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the glutamate-gated ion channel (TC 1.A.10.1)
- **Key Domains:** ANF_lig-bd_rcpt. (IPR001828); Glu/Gly-bd. (IPR019594); Iono_Glu_rcpt_met. (IPR001508); Ionotropic_Glu_rcpt. (IPR015683); Iontro_rcpt_C. (IPR001320)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GRIN2D" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GRIN2D' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GRIN2D** (gene ID: GRIN2D, UniProt: O15399) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# GRIN2D (GluN2D / NR2D) — Functional Annotation Report

**Gene:** GRIN2D (HGNC:4588) | **Protein:** Glutamate receptor ionotropic, NMDA 2D (GluN2D / NR2D / NMDAR2D / epsilon-4 / EB11)
**UniProt:** O15399 | **Organism:** *Homo sapiens* (Human)
**Protein family:** Glutamate-gated ion channel (TC 1.A.10.1)

---

## Summary

**GRIN2D encodes GluN2D (also called NR2D or NMDA receptor subunit epsilon-4), a glutamate-binding, pore-forming subunit of the N-methyl-D-aspartate (NMDA) subtype of ionotropic glutamate receptor.** GluN2D is not an enzyme or a transporter in the classical sense; it is a *ligand-and-voltage-gated cation channel subunit*. Functional NMDA receptors are obligate heterotetramers built from two glycine/D-serine-binding GluN1 subunits and two glutamate-binding GluN2 subunits (GluN2A–D). The identity of the GluN2 subunit dictates the receptor's biophysical and pharmacological personality, and GluN2D confers a highly distinctive one: ultra-slow deactivation (deactivation time constant ~3 seconds), the highest glutamate affinity of the GluN2 family, and low single-channel conductance. The gene symbol, human organism, and glutamate-gated ion channel family all match the primary literature; the identity is firmly verified with no ambiguity.

**Mechanistically, the GluN2D-containing receptor is a coincidence detector that gates Ca²⁺ influx.** The channel conducts only when three conditions are met simultaneously: glutamate is bound to GluN2D, the co-agonist glycine or D-serine is bound to GluN1, and the membrane is depolarized enough to relieve the voltage-dependent Mg²⁺ block of the pore. When these coincide, the pore opens and admits cations — predominantly Ca²⁺ — which triggers downstream signaling. GluN2D's slow kinetics and high agonist sensitivity specialize these receptors for *tonic*, *extrasynaptic* detection of ambient and spillover glutamate rather than fast point-to-point synaptic transmission. These properties are encoded by GluN2D's modular extracellular domains: the amino-terminal domain (ATD) sets high glutamate potency and tunes open probability, and a single threonine (T692) in the S2 ligand-binding segment is a major determinant of agonist potency and deactivation rate.

**Spatially and developmentally, GluN2D is highly restricted.** It is broadly expressed in the embryonic and early postnatal brain but, in the adult, becomes concentrated subcortically (thalamus, midbrain, brainstem, spinal cord) and, in forebrain, is largely confined to subpopulations of GABAergic interneurons and specific cell types such as cerebellar Purkinje and Golgi cells and dentate granule cells. It frequently assembles into triheteromeric receptors (e.g., GluN1/GluN2B/GluN2D) that are restricted to extrasynaptic sites. The physiological importance of this inhibitory-circuit role is validated by human genetics: de novo gain-of-function missense variants clustered in the M3 pore-gating helix cause severe developmental and epileptic encephalopathy (DEE), act principally through GABAergic interneurons, and are frequently responsive to the NMDAR channel blocker memantine.

---

## Key Findings

### Finding 1 — GRIN2D encodes GluN2D, a glutamate-gated subunit of the ionotropic NMDA receptor

GRIN2D (UniProt O15399) encodes the GluN2D subunit, historically named NR2D or glutamate [NMDA] receptor subunit epsilon-4. Functional NMDA receptors are heterotetrameric complexes composed of **two obligatory GluN1 subunits** (which bind the co-agonist glycine/D-serine) plus **two GluN2 subunits** (GluN2A–D, which bind the agonist glutamate). The identity of the GluN2 subunit defines the receptor's functional characteristics, so the presence of GluN2D confers a specific biophysical and pharmacological signature on the assembled receptor.

This architecture is directly supported by the recent literature: *"NMDARs are tetrameric complexes composed of two essential GluN1 subunits and two distinct GluN2 subunits (GluN2A-D) that define their functional characteristics"* ([PMID: 42427625](https://pubmed.ncbi.nlm.nih.gov/42427625/)). The division of molecular labor between subunits — GluN1 binding glycine and GluN2 binding glutamate — is confirmed structurally in the tri-heteromeric receptor: *"the tri-heteromeric receptor, comprising glycine-binding GluN1 and two types of glutamate-binding GluN2 subunits"* ([PMID: 39954679](https://pubmed.ncbi.nlm.nih.gov/39954679/)).

**Identity verification:** the gene symbol GRIN2D, the human organism, and the glutamate-gated ion channel family (TC 1.A.10.1) all match the primary literature. There is no ambiguity — this is the correct protein.

### Finding 2 — GluN2D is developmentally regulated and, in adults, restricted largely to GABAergic interneurons and extrasynaptic sites

GluN2D displays a striking spatiotemporal expression pattern. It is broadly expressed in the embryonic and early postnatal brain but becomes spatially restricted in the adult, where it is found predominantly in subpopulations of GABAergic (inhibitory) interneurons: *"GluN2D is broadly expressed during embryonic and early postnatal development, but its expression becomes more spatially restricted in the adult brain, where it is predominantly found in subpopulations of GABAergic (gamma-aminobutyric acidergic) interneurons"* ([PMID: 41765344](https://pubmed.ncbi.nlm.nih.gov/41765344/)).

Beyond interneurons, GluN2D also operates in specific excitatory cell types. In mature dentate granule cells, GluN2D-containing NMDARs are *"tonically active, primarily extrasynaptic, and facilitate GC action-potential firing"* ([PMID: 42427625](https://pubmed.ncbi.nlm.nih.gov/42427625/)), and conditional knockout of GluN2D from these cells impaired synaptic plasticity and spatial memory. This establishes two defining features of GluN2D physiology: an **extrasynaptic subcellular localization** and a role in **supporting neuronal excitability** rather than mediating fast synaptic transmission.

### Finding 3 — GluN2D confers distinctive biophysical and pharmacological properties, including in triheteromeric receptors

The GluN2D subunit imparts its signature even when co-assembled with another GluN2 subunit into a triheteromeric receptor. Functional studies of GluN1/2B/2D receptors show agonist potencies, open probability, and glutamate deactivation kinetics that are intermediate between the parent diheteromeric GluN1/2B and GluN1/2D receptors, and — critically for pharmacology — these triheteromers are *"more sensitive to channel blockade by ketamine and memantine compared to GluN1/2B receptors"* ([PMID: 31541561](https://pubmed.ncbi.nlm.nih.gov/31541561/)) in physiological Mg²⁺.

Structural work on native adult-brain receptors reinforces that GluN2D has mechanically distinct gating. Cryo-EM of the GluN1-2B-2D tri-heteromer resolved activated, inhibited, and S-(+)-ketamine-blocked states and showed that *"the inhibitor (S)-DQP-997-74 selectively decouples linker tension in GluN2D, offering insights into subtype-selective targeting"* ([PMID: 39954679](https://pubmed.ncbi.nlm.nih.gov/39954679/)). This demonstrates that GluN2D-specific gating-linker mechanics can be selectively engaged by drugs, opening a route to subtype-selective therapeutics.

### Finding 4 — GluN2D-containing NMDARs show extremely slow deactivation, high agonist affinity, and low conductance

The hallmark biophysical property of GluN2D is its extraordinarily slow kinetics. Native NR1/NR2D receptors in rat cerebellar Purkinje cells deactivate with a single-exponential time constant of approximately 3 seconds — roughly 100-fold slower than GluN2A-containing receptors: *"The averaged macroscopic current exhibited a decay time course which was well described by a single exponential function with a time constant of approximately 3 s"* ([PMID: 10835034](https://pubmed.ncbi.nlm.nih.gov/10835034/)). These receptors also have low whole-cell conductance (~750 pS) and a characteristic low (~50 pS) single-channel conductance with asymmetric main/sub-conductance transitions.

Combined with the highest agonist sensitivity of the GluN2 family, these kinetics make GluN2D ideally suited to detect low-concentration ambient and spillover glutamate: *"The receptors formed by NR2B and (especially) NR2D subunits are known to have higher agonist sensitivity and much slower deactivation kinetics than NR2A-containing receptors"* ([PMID: 15146049](https://pubmed.ncbi.nlm.nih.gov/15146049/)). This same study showed that extrasynaptic NR2D-containing receptors generate anomalously slow "superslow" afterburst excitatory postsynaptic currents via glutamate spillover in the hippocampus — a functional readout of GluN2D's role as a slow, extrasynaptic integrator.

| Property | GluN2D-containing receptor | Functional consequence |
|---|---|---|
| Deactivation time constant | ~3 s (single exponential) | Ultra-slow, prolonged Ca²⁺ signaling |
| Agonist (glutamate) sensitivity | Highest of GluN2A–D | Detects ambient/spillover glutamate |
| Single-channel conductance | Low (~50 pS) | Small unitary currents |
| Preferred location | Extrasynaptic | Tonic, non-synaptic signaling |
| Mg²⁺ block | Present (voltage-dependent) | Coincidence detection |

### Finding 5 — GluN2D's distinctive properties are encoded by its modular extracellular domains

GluN2D's unusual biophysics are not accidents of its pore but are programmed into its large extracellular domains. The GluN2 **amino-terminal domain (ATD)** controls agonist potency, deactivation time course, and open probability. Specifically, *"the ATD contributes to the low glutamate potency of NR2A-containing NMDA receptors and the high glutamate potency of NR2D-containing receptors"* ([PMID: 19793963](https://pubmed.ncbi.nlm.nih.gov/19793963/)); swapping or removing the NR2D ATD increases open probability and mean open duration, showing the ATD both sets agonist potency and tonically restrains gating.

Within the **ligand-binding domain (LBD)**, a single residue is pivotal. In the GluN2D S2 segment, threonine 692 is a key determinant of agonist action: the T692A mutation produced *"an approximately 1600-fold reduction in glutamate potency compared to wild-type NR1a/NR2D receptors"* and accelerated deactivation ~60-fold, without changing glycine potency or single-channel conductance ([PMID: 15107472](https://pubmed.ncbi.nlm.nih.gov/15107472/)). Together these studies demonstrate that GluN2D's identity-defining properties — high glutamate affinity and slow deactivation — are modular, encoded in the ATD and LBD, and are mechanistically separable from the pore and the glycine site.

### Finding 6 — GluN2D-NMDARs act as coincidence detectors gating Ca²⁺ influx and natively form extrasynaptic di- and triheteromeric channels

The core physiological function of the assembled receptor is coincidence detection. NMDARs integrate presynaptic glutamate release with postsynaptic depolarization to open the channel gate: *"integrating presynaptic glutamate release and postsynaptic membrane depolarization to open the channel gate. This allows the influx of cations (mainly calcium) into the postsynaptic neuron and triggers downstream signaling for synaptic plasticity"* ([PMID: 42265035](https://pubmed.ncbi.nlm.nih.gov/42265035/)). The Ca²⁺ that enters through the pore is the second messenger that links receptor activation to plasticity and gene-expression cascades.

GluN2D natively assembles into both diheteromeric and triheteromeric channels with cell-type specificity. In the cerebellum it co-assembles with GluN1 as low-conductance diheteromers in Purkinje cells ([PMID: 10835034](https://pubmed.ncbi.nlm.nih.gov/10835034/)), and with GluN2B to form triheteromeric channels restricted to extrasynaptic sites in Golgi cells: *"a triheteromeric assembly (NR1/NR2B/NR2D) in cells from wild-type mice"* ([PMID: 12832518](https://pubmed.ncbi.nlm.nih.gov/12832518/)). This native triheteromeric, extrasynaptic configuration is a recurring theme of GluN2D biology.

### Finding 7 — GluN2D protein shows a defined regional and developmental expression gradient, enriched in diencephalon/midbrain/brainstem and in interneurons

Protein-level mapping with an NR2D-specific antibody (recognizing an ~160-kDa N-glycosylated protein) established a clear regional gradient: NR2D is highest in the **thalamus, midbrain, medulla, and spinal cord**, intermediate in cortex and hippocampus, and low or undetectable in olfactory bulb, striatum, and cerebellum: *"NR2D was expressed at highest levels in the thalamus, midbrain, medulla, and spinal cord, whereas intermediate levels of this subunit were found in the cortex and hippocampus"* ([PMID: 8931465](https://pubmed.ncbi.nlm.nih.gov/8931465/)). Developmentally, the protein is high embryonically, peaks around postnatal day 7, then declines roughly two-fold into adulthood while remaining measurable.

At the cellular level, GluN2D is neuron-restricted and distinguishes itself from the closely related glial GluN2C: *"GluN2D subunit mRNA colocalized with neuronal and not astrocyte markers or GluN2C mRNA in the telencephalon"* ([PMID: 29651654](https://pubmed.ncbi.nlm.nih.gov/29651654/)). This establishes GluN2D as a neuronal (predominantly interneuronal) subunit, in contrast to the astrocytic distribution of its paralog GluN2C.

### Finding 8 — GRIN2D gain-of-function variants cause developmental and epileptic encephalopathy, acting principally through GABAergic interneurons

Human genetics provides the strongest validation of GluN2D's precise functional role. De novo missense variants in GRIN2D, clustered in the **M3 transmembrane gating helix** (e.g., recurrent V667I present in roughly a quarter of patients; also A675V and T674K), cause severe developmental and epileptic encephalopathy with intractable seizures, hypotonia, and neurodevelopmental delay ([PMID: 41673952](https://pubmed.ncbi.nlm.nih.gov/41673952/), [PMID: 36567197](https://pubmed.ncbi.nlm.nih.gov/36567197/), [PMID: 33397303](https://pubmed.ncbi.nlm.nih.gov/33397303/)). The variants localize to the helix that gates the pore: *"affecting one of the transmembrane domains (M3), which is essential for normal NMDAR function and harbours most of the pathogenic variants reported to date"* ([PMID: 41673952](https://pubmed.ncbi.nlm.nih.gov/41673952/)).

A knock-in mouse carrying the orthologous variant recapitulates the human disease, and crucially pinpoints the responsible cell type: *"expression of V664I in GABAergic interneurons, but not excitatory forebrain neurons, is sufficient to recapitulate the severe electroclinical phenotype"* ([PMID: 40200555](https://pubmed.ncbi.nlm.nih.gov/40200555/)). This cell-type dissection confirms that GluN2D's physiologically decisive action is within inhibitory interneurons — paradoxically, a gain of function in a depolarizing channel housed in inhibitory neurons produces a network phenotype of epilepsy. Therapeutically, the mechanism is targetable by channel block: among individuals with GRIN gain-of-function variants, *"Fourteen of 19 individuals (74%) benefited from memantine"* ([PMID: 41489401](https://pubmed.ncbi.nlm.nih.gov/41489401/)), confirming that the disease operates through excess channel activity.

### Finding 9 — GluN2D-NMDARs require glycine/D-serine co-agonism and operate within the glutamatergic excitatory signaling pathway

A GluN2D-containing receptor is an obligate coincidence device at the chemical level as well. Glycine (or D-serine) binding to GluN1 is a mandatory co-agonist that works in concert with glutamate binding to GluN2D: *"glycine (or d-serine) acts in concert with glutamate as a mandatory co-agonist to set the level of receptor activity. It also regulates the receptor's trafficking and expression independently of glutamate"* ([PMID: 34058193](https://pubmed.ncbi.nlm.nih.gov/34058193/)). Thus the receptor conducts only when glutamate occupies the GluN2D LBD, the co-agonist occupies the GluN1 LBD, and the membrane is depolarized. Beyond gating, co-agonist occupancy also acts as a quality-control signal for surface trafficking, coupling the receptor's assembly and delivery to its ligand environment.

---

## Mechanistic Model / Interpretation

GluN2D should be understood as a **specialization module** that converts the generic NMDA-receptor coincidence detector into a slow, high-sensitivity, extrasynaptic sensor of ambient glutamate, deployed selectively in inhibitory and subcortical circuits.

```
          GluN2D-containing NMDA receptor (heterotetramer)
          +---------------------------------------------+
          |  2 x GluN1 (glycine / D-serine binding)     |
          |  + GluN2D  (glutamate binding)              |
          |  +/- 2nd GluN2 (e.g. GluN2B) -> triheteromer|
          +---------------------------------------------+

  REQUIRED COINCIDENCE (all three simultaneously):
    (1) Glutamate bound to GluN2D LBD   ---+
    (2) Glycine/D-serine bound to GluN1 ---+--> channel gate (M3) opens
    (3) Membrane depolarized -> Mg2+ block relieved ---+
                              |
                              v
                 Ca2+ (and Na+/K+) influx through low-conductance pore
                              |
                              v
          Downstream Ca2+ signaling -> excitability, plasticity, gene expression

  GluN2D-SPECIFIC TUNING (domain-encoded):
    - ATD  --> high glutamate potency; restrains open probability   (PMID 19793963)
    - LBD-S2 Thr692 --> agonist potency + ~3 s slow deactivation    (PMID 15107472)
    - M3   --> gate; site of pathogenic gain-of-function variants   (PMID 41673952)

  DEPLOYMENT:
    Developmental: high embryonic -> peak ~P7 -> ~2-fold decline      (PMID 8931465)
    Regional:  thalamus/midbrain/brainstem/spinal cord > cortex/hippo (PMID 8931465)
    Cellular:  GABAergic interneurons; Purkinje & Golgi cells; DG GCs (PMID 41765344, 29651654)
    Subcellular: EXTRASYNAPTIC (di- and tri-heteromeric)              (PMID 12832518, 42427625)
```

The slow deactivation (~3 s) and high agonist affinity mean that a GluN2D receptor, once activated, keeps conducting long after a fast synaptic AMPA/NMDA current has decayed, and can be activated by low-level glutamate that has diffused ("spilled over") away from release sites. This makes GluN2D a **tonic, integrative** element rather than a fast signaling element. In GABAergic interneurons such tonic Ca²⁺ influx tunes interneuron excitability and thereby the excitatory/inhibitory balance of the network — which is why a *gain* of function in these receptors, even though they are depolarizing, can derail network dynamics into epilepsy, and why that phenotype is reproduced by driving the variant specifically in interneurons ([PMID: 40200555](https://pubmed.ncbi.nlm.nih.gov/40200555/)). The pharmacological corollary — enhanced sensitivity to open-channel blockers memantine and ketamine ([PMID: 31541561](https://pubmed.ncbi.nlm.nih.gov/31541561/)) and clinical benefit from memantine ([PMID: 41489401](https://pubmed.ncbi.nlm.nih.gov/41489401/)) — closes the loop between molecular mechanism and therapy.

### Functional annotation summary

| Annotation axis | Assignment for GRIN2D / GluN2D |
|---|---|
| **Molecular function** | Glutamate-gated, Ca²⁺-permeable cation channel subunit (glutamate-binding) of the ionotropic NMDA receptor |
| **Primary "substrate"/ligand** | L-glutamate (agonist at GluN2D); requires glycine/D-serine co-agonist at GluN1; permeant ions Ca²⁺ > Na⁺/K⁺ |
| **Reaction/activity** | Ligand- and voltage-gated transmembrane cation flux (not catalytic) |
| **Localization** | Plasma membrane; predominantly **extrasynaptic**; neuronal |
| **Pathway** | Glutamatergic excitatory neurotransmission; coincidence detection → Ca²⁺-dependent signaling, synaptic plasticity, excitability control |
| **Cellular/anatomical context** | GABAergic interneurons; cerebellar Purkinje & Golgi cells; dentate granule cells; enriched in thalamus/midbrain/brainstem/spinal cord; developmentally down-regulated |
| **Disease relevance** | De novo M3 gain-of-function variants → developmental and epileptic encephalopathy (acting via interneurons; memantine-responsive) |

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [42427625](https://pubmed.ncbi.nlm.nih.gov/42427625/) | *GluN2D-containing NMDARs support dentate granule cell excitability, plasticity, memory* | Heterotetramer architecture; GluN2 defines function; GluN2D receptors tonically active, extrasynaptic, support firing and memory |
| [39954679](https://pubmed.ncbi.nlm.nih.gov/39954679/) | *Structural basis for channel gating and blockade in tri-heteromeric GluN1-2B-2D* | Cryo-EM: GluN1 glycine-binding, GluN2 glutamate-binding; GluN2D-specific linker tension decoupled by inhibitor |
| [41765344](https://pubmed.ncbi.nlm.nih.gov/41765344/) | *GluN2D NMDA Receptors: Bridging Physiology and Pathology* | Developmental regulation; adult restriction to GABAergic interneurons |
| [31541561](https://pubmed.ncbi.nlm.nih.gov/31541561/) | *Functional and pharmacological properties of triheteromeric GluN1/2B/2D* | Intermediate properties; enhanced ketamine/memantine sensitivity |
| [10835034](https://pubmed.ncbi.nlm.nih.gov/10835034/) | *Slow deactivation kinetics of NR1/NR2D in Purkinje cells* | ~3 s deactivation; low conductance; native diheteromers |
| [15146049](https://pubmed.ncbi.nlm.nih.gov/15146049/) | *Extrasynaptic NR2B/NR2D shape 'superslow' afterburst EPSC* | High agonist sensitivity, slow kinetics, extrasynaptic spillover signaling |
| [19793963](https://pubmed.ncbi.nlm.nih.gov/19793963/) | *Control of NMDAR function by NR2 ATD* | ATD encodes high glutamate potency of NR2D and tunes gating |
| [15107472](https://pubmed.ncbi.nlm.nih.gov/15107472/) | *Threonine in S2 LBD determines potency/deactivation of NR1a/NR2D* | T692A: ~1600-fold lower glutamate potency, ~60-fold faster deactivation |
| [42265035](https://pubmed.ncbi.nlm.nih.gov/42265035/) | *Atomic insights into NMDA receptor diversity* | Coincidence detection; Ca²⁺ influx → plasticity signaling |
| [12832518](https://pubmed.ncbi.nlm.nih.gov/12832518/) | *NR2B/NR2D coassemble in Golgi cells, extrasynaptic* | Native triheteromeric GluN2D receptors restricted to extrasynaptic sites |
| [8931465](https://pubmed.ncbi.nlm.nih.gov/8931465/) | *Regional/ontogenic NR2D protein expression* | Regional gradient (thalamus/midbrain/brainstem/spinal cord high); developmental profile |
| [29651654](https://pubmed.ncbi.nlm.nih.gov/29651654/) | *GluN2C glial vs GluN2D interneuronal mRNA* | GluN2D neuronal/interneuronal, not astrocytic |
| [40200555](https://pubmed.ncbi.nlm.nih.gov/40200555/) | *Synaptic dysregulation in GRIN2D DEE mouse model* | Gain-of-function in interneurons sufficient for disease |
| [41673952](https://pubmed.ncbi.nlm.nih.gov/41673952/) | *GRIN2D-related DEE with polymorphic seizures* | Pathogenic variants cluster in M3 gating helix |
| [41489401](https://pubmed.ncbi.nlm.nih.gov/41489401/) | *Memantine in GRIN gain-of-function variants* | 74% benefited — channel-activity mechanism is drug-targetable |
| [34058193](https://pubmed.ncbi.nlm.nih.gov/34058193/) | *Glycine agonism in ionotropic glutamate receptors* | Mandatory glycine/D-serine co-agonism; trafficking role |
| [36567197](https://pubmed.ncbi.nlm.nih.gov/36567197/) | *Perampanel for GRIN2D DEE; A675V in M3* | Additional M3 pathogenic variant; treatment case |
| [33397303](https://pubmed.ncbi.nlm.nih.gov/33397303/) | *Novel GRIN2D T674K variant* | Heterotetramer composition; additional pathogenic variant |
| [40277233](https://pubmed.ncbi.nlm.nih.gov/40277233/) | *Grin2d V667I mouse recapitulates human disease* | Model validation; memantine/phenytoin partial correction |
| [39535073](https://pubmed.ncbi.nlm.nih.gov/39535073/) | *Ligand distances predict pathogenicity in NMDARs* | Variant pathogenicity/function predicted by proximity to bound ligands |

**Consistency of the evidence.** The findings form a mutually reinforcing picture across experimental modalities — electrophysiology of native and recombinant receptors (PMIDs 10835034, 15146049, 15107472, 31541561), structural biology (PMID 39954679), protein and mRNA expression mapping (PMIDs 8931465, 29651654), mouse genetics (PMID 40200555), and human clinical genetics/pharmacology (PMIDs 41673952, 41489401). No paper in the reviewed set contradicts the core annotation. One important nuance distinguishing gain-of-function from loss-of-function mechanisms is that heterozygous GRIN2D protein-truncating (null) variants appear non-pathogenic, whereas the DEE-causing variants are missense gain-of-function changes in the M3 gate — emphasizing that disease stems from excess channel activity rather than haploinsufficiency.

---

## Limitations and Knowledge Gaps

- **Species mixing.** Much of the detailed biophysical and expression data derives from rat and mouse (PMIDs 10835034, 15146049, 8931465, 40200555). While the subunit is highly conserved and human disease genetics align with rodent mechanisms, some quantitative parameters (exact deactivation constants, regional densities) may differ in human tissue.
- **Human-specific functional data are sparse.** The precise kinetics and single-channel behavior of *human* GluN2D-containing receptors in native human neurons have not been directly characterized here; inference rests on rodent native receptors and recombinant systems.
- **Triheteromeric composition in vivo.** Many physiological GluN2D receptors are triheteromers (e.g., GluN1/2B/2D), but the full catalog of native partner subunits, stoichiometries, and brain-region-specific compositions remains incompletely mapped.
- **Downstream signaling specificity.** Although GluN2D gates Ca²⁺ influx, the specific intracellular effectors and C-terminal protein interactions unique to GluN2D (as opposed to the better-studied GluN2A/2B) are not resolved in the reviewed literature, including how its extrasynaptic location couples to signaling.
- **Non-ionotropic / metabotropic signaling.** Whether GluN2D-containing receptors engage in agonist-bound but non-conducting ("metabotropic") signaling, as described for some NMDARs, was not addressed.
- **No structural validation was performed in this investigation.** The report is literature-based; no experimental data files or structures were analyzed.

---

## Proposed Follow-up Experiments / Actions

1. **Cell-type-resolved human expression atlas.** Use single-nucleus RNA-seq and spatial transcriptomics of adult human brain to precisely map GRIN2D to interneuron subclasses (e.g., PV⁺, SST⁺, VIP⁺) and subcortical nuclei, confirming the rodent-derived distribution in human tissue.
2. **Human GluN2D electrophysiology.** Characterize deactivation kinetics, open probability, and Mg²⁺/memantine sensitivity of recombinant *human* GluN1/GluN2D and GluN1/2B/2D receptors, and in human iPSC-derived interneurons (patient-derived lines exist, PMID 33482465), to establish human-specific parameters.
3. **Define the GluN2D interactome.** Pull-down/proximity-labeling of the GluN2D C-terminal domain to identify subunit-specific scaffolding and signaling partners that mediate its extrasynaptic Ca²⁺ signaling.
4. **Structure-function of pathogenic variants.** Cryo-EM and electrophysiology of M3 variants (V667I, A675V, T674K) in defined triheteromers to quantify the gain-of-function magnitude and test variant-specific blocker sensitivity, extending the ligand-distance pathogenicity framework (PMID 39535073).
5. **Circuit-level rescue.** In the Grin2d knock-in model, test interneuron-targeted memantine delivery or subtype-selective negative allosteric modulators (e.g., DQP-997-74-class compounds that decouple GluN2D linker tension, PMID 39954679) for seizure suppression, to validate GluN2D as a precision therapeutic target.
6. **Co-agonist dependence in GluN2D circuits.** Test how ambient D-serine vs glycine availability shapes tonic extrasynaptic GluN2D currents in interneurons, given the co-agonist's dual gating/trafficking role (PMID 34058193).

---

*Report compiled from 9 confirmed findings and 45 reviewed papers over 5 investigation iterations. Gene identity (GRIN2D / GluN2D / O15399, Homo sapiens) verified against primary literature; no ambiguity detected.*


## Artifacts

- [OpenScientist final report](GRIN2D-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](GRIN2D-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:42427625
2. PMID:39954679
3. PMID:41765344
4. PMID:31541561
5. PMID:10835034
6. PMID:15146049
7. PMID:19793963
8. PMID:15107472
9. PMID:42265035
10. PMID:12832518
11. PMID:8931465
12. PMID:29651654
13. PMID:41673952
14. PMID:36567197
15. PMID:33397303
16. PMID:40200555
17. PMID:41489401
18. PMID:34058193