---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-10T08:17:22.827754'
end_time: '2026-11-10T08:31:39.772657'
duration_seconds: 856.94
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: GRIN1
  gene_symbol: GRIN1
  uniprot_accession: Q05586
  protein_description: 'RecName: Full=Glutamate receptor ionotropic, NMDA 1 {ECO:0000305};
    Short=GluN1; AltName: Full=Glutamate [NMDA] receptor subunit zeta-1 {ECO:0000305};
    AltName: Full=N-methyl-D-aspartate receptor subunit NR1; Short=NMD-R1; Short=hNR1
    {ECO:0000303|PubMed:7685113, ECO:0000303|PubMed:8406025}; Flags: Precursor;'
  gene_info: Name=GRIN1 {ECO:0000312|HGNC:HGNC:4584}; Synonyms=NMDAR1 {ECO:0000303|PubMed:7679115};
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
citation_count: 31
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: GRIN1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: GRIN1-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q05586
- **Protein Description:** RecName: Full=Glutamate receptor ionotropic, NMDA 1 {ECO:0000305}; Short=GluN1; AltName: Full=Glutamate [NMDA] receptor subunit zeta-1 {ECO:0000305}; AltName: Full=N-methyl-D-aspartate receptor subunit NR1; Short=NMD-R1; Short=hNR1 {ECO:0000303|PubMed:7685113, ECO:0000303|PubMed:8406025}; Flags: Precursor;
- **Gene Information:** Name=GRIN1 {ECO:0000312|HGNC:HGNC:4584}; Synonyms=NMDAR1 {ECO:0000303|PubMed:7679115};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the glutamate-gated ion channel (TC 1.A.10.1)
- **Key Domains:** ANF_lig-bd_rcpt. (IPR001828); Glu/Gly-bd. (IPR019594); Iono_Glu_rcpt_met. (IPR001508); Ionotropic_Glu_rcpt. (IPR015683); Iontro_rcpt_C. (IPR001320)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GRIN1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GRIN1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GRIN1** (gene ID: GRIN1, UniProt: Q05586) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# GRIN1 (GluN1 / NR1): Functional Annotation Report

**Gene:** GRIN1 (HGNC:4584) · **Protein:** Glutamate receptor ionotropic, NMDA 1 (GluN1 / NR1 / NMD-R1 / zeta-1) · **UniProt:** Q05586 · **Organism:** *Homo sapiens* (Human) · **Family:** Glutamate-gated ion channel (TC 1.A.10.1)

---

## Summary

**GRIN1 encodes GluN1 (also called NR1 or NMDAR1), the obligatory, non-redundant core subunit of the N-methyl-D-aspartate (NMDA) subtype of ionotropic glutamate receptor.** Its primary molecular function is not enzymatic but **ligand- and voltage-gated cation channel activity**. GluN1 contributes two interlocking capabilities to the receptor: (1) it supplies the binding site for the co-agonists **glycine and D-serine**, and (2) it co-assembles with glutamate-binding GluN2 subunits (or, alternatively, with GluN3 subunits) to build the Ca²⁺-permeable cation channel that mediates the slow, Ca²⁺-signaling component of excitatory synaptic transmission in the central nervous system. The canonical receptor is a heterotetramer of two GluN1 and two GluN2 subunits arranged in a **1-2-1-2** configuration. Because glycine binds GluN1 and glutamate binds GluN2, and because channel opening additionally requires membrane depolarization to relieve a voltage-dependent Mg²⁺ block of the pore, the NMDA receptor behaves as a **Hebbian coincidence detector** — opening only when presynaptic glutamate release and postsynaptic depolarization coincide. The resulting Ca²⁺ influx is the trigger for long-term potentiation (LTP), long-term depression (LTD), learning, memory, and activity-dependent neurodevelopment.

GluN1 is remarkably versatile. Beyond the classic GluN1/GluN2 NMDA receptor, GluN1 partners with GluN3 subunits to build **excitatory glycine receptors (eGlyRs)** that are gated by glycine alone, independent of glutamate. GluN1's N-terminal exon-5 splice cassette and C-terminal C1/C2 cassettes act as regulatory modules: the exon-5 insert tunes proton and neurosteroid allosteric modulation, while the C-terminal tail carries an endoplasmic-reticulum (ER) retention signal that gates surface trafficking and binds calmodulin to mediate Ca²⁺/calmodulin-dependent inactivation — a negative-feedback brake on Ca²⁺ influx. Critically, the *same* GluN1-containing receptor produces diametrically opposite cellular outcomes depending on *where* it sits: **synaptic** NMDA receptors drive pro-survival CREB signaling and plasticity, whereas **extrasynaptic** NMDA receptors drive excitotoxic cell death implicated in stroke and neurodegeneration.

The subunit's essential, non-redundant status is bracketed by genetics at both extremes. Complete genetic ablation of *Grin1* in mice abolishes all NMDA-evoked currents and Ca²⁺ influx and is neonatally lethal, while de novo human *GRIN1* variants cause a severe neurodevelopmental encephalopathy (GRIN1-related disorder) with intellectual disability, hypotonia, movement disorder, and epilepsy. Structural biology — crystal structures of the GluN1 S1S2 ligand-binding core and of the intact receptor — confirms the clamshell glycine-binding mechanism and the layered, Ca²⁺-permeable pore architecture, and evolutionary/bioinformatic analyses place GluN1 within the larger ionotropic glutamate receptor family, sharing a periplasmic-binding-protein-like ligand-binding fold with the AMPA receptor GluR2. **Gene identity is confirmed and unambiguous:** the symbol, protein description, human organism, family (TC 1.A.10.1), and domain architecture all match the primary literature.

---

## Key Findings

### Finding 1 — GluN1 is the obligatory, non-redundant subunit required for all NMDA receptor function

GluN1 is not merely one subunit among several; it is the indispensable core without which no functional NMDA receptor can form. The definitive evidence comes from in vivo genetic ablation in mice. Targeted disruption of the *Grin1* (NR1) gene abolishes the NMDA response entirely: neurons from homozygous null mutants show complete loss of NMDA-inducible increases in intracellular calcium and of NMDA-evoked membrane currents, and the animals die 8–15 hours after birth from respiratory failure ([PMID: 8060614](https://pubmed.ncbi.nlm.nih.gov/8060614/)). As the authors state, *"NR1 has a unique role, which cannot be substituted by any other subunit, in determining the activity of the endogenous NMDA receptor,"* and *"NMDA-inducible increases in intracellular calcium and membrane currents were abolished in neurons from homozygous null mutants."* GluN1 has no known functional homolog and is expressed in almost every neuronal cell type, underscoring its universal role in NMDA signaling ([PMID: 19794189](https://pubmed.ncbi.nlm.nih.gov/19794189/)): *"The NMDA receptor (NMDAR) subunit GluN1 is an obligatory component of NMDARs without a known functional homolog and is expressed in almost every neuronal cell type."* This obligatory, ubiquitous status is the central fact of GluN1 biology — every finding below concerns receptors that necessarily contain GluN1.

### Finding 2 — GluN1 harbors the glycine/D-serine co-agonist site; glutamate binds GluN2

The division of labor within the NMDA receptor is precise and structurally defined. NMDA receptors require *both* glycine (or D-serine) and glutamate to open, with the two agonists binding distinct subunits: **GluN1 forms the glycine site and GluN2 forms the glutamate site** ([PMID: 12805203](https://pubmed.ncbi.nlm.nih.gov/12805203/)): *"NMDA receptors require both glycine and glutamate for activation with NR1 and NR2 forming glycine and glutamate sites, respectively."* This assignment is proven at atomic resolution: co-crystal structures of the GluN1 (NR1) S1S2 ligand-binding core were solved in complex with the agonists glycine and D-serine, directly demonstrating that GluN1 binds these co-agonists (*"we describe the cocrystal structures of the NR1 S1S2 ligand-binding core with the agonists glycine and D-serine"*). The functional building block is the heterodimer: the **NR1–NR2A (GluN1–GluN2A) heterodimer is the functional unit** within the tetrameric receptor ([PMID: 16281028](https://pubmed.ncbi.nlm.nih.gov/16281028/)): *"the NR1-NR2A heterodimer is the functional unit in tetrameric NMDA receptors."* Thus GluN1's primary biochemical function is to serve as the glycine/D-serine co-agonist sensor of the receptor complex. The physiological co-agonist supply is set by serine racemase (producing D-serine) and by glycine transporter GlyT1, which regulates ambient glycine at the GluN1 site ([PMID: 37833512](https://pubmed.ncbi.nlm.nih.gov/37833512/), [PMID: 39059742](https://pubmed.ncbi.nlm.nih.gov/39059742/)).

### Finding 3 — The receptor is a Ca²⁺-permeable coincidence detector with 1-2-1-2 architecture

The intact receptor's architecture explains its signature physiology. X-ray crystal structures of the complete GluN1–GluN2B receptor reveal subunits arranged in a **1-2-1-2** fashion, with a layered organization of amino-terminal domains (ATD), ligand-binding domains (LBD), and transmembrane domains (TMD), and a pore lined by residues that coordinate Mg²⁺ and channel blockers ([PMID: 25008524](https://pubmed.ncbi.nlm.nih.gov/25008524/)): *"Receptor subunits are arranged in a 1-2-1-2 fashion."* Functionally, this makes the NMDA receptor a Hebbian-like coincidence detector: *"NMDA receptors are Hebbian-like coincidence detectors, requiring binding of glycine and glutamate in combination with the relief of voltage-dependent magnesium block to open an ion conductive pore across the membrane bilayer."* The convergence of three requirements — glycine on GluN1, glutamate on GluN2, and depolarization to expel Mg²⁺ — means the channel opens only when pre- and postsynaptic activity coincide, and the ensuing Ca²⁺ influx is the biochemical substrate for synaptic plasticity.

### Finding 4 — GluN1 surface trafficking is gated by an ER retention signal in its C1 cassette

Where and when GluN1-containing receptors reach the cell surface is tightly controlled by signals within GluN1's own C-terminus. A CD8–NR1 C-terminal fusion protein is retained intracellularly in both HEK293 cells and neurons because of an **ER retention signal located in the C1 cassette** ([PMID: 11640925](https://pubmed.ncbi.nlm.nih.gov/11640925/)): *"the NR1 fusion protein was retained intracellularly in both HEK293 cells and neurons because of the presence of an ER retention signal in the C1 cassette."* This retention is not absolute — it can be overridden *"either by the addition of a PDZ domain-binding motif or by mimicking phosphorylation at a site adjacent to the retention signal,"* providing regulated control of surface expression. Beyond the retention signal itself, NMDA receptors are sorted to dendrites through a specialized secretory route: NR1/NR2B complexes (with KIF17, CASK, SAP97) are *"diverted from the somatic endoplasmic reticulum into a specialized endoplasmic reticulum subcompartment that bypasses somatic Golgi"* and use dendritic Golgi outposts, a pathway distinct from that used by AMPA receptors ([PMID: 19620977](https://pubmed.ncbi.nlm.nih.gov/19620977/)). Additional ER-retention determinants in the M3 transmembrane segments ensure that only properly assembled complexes reach the surface ([PMID: 18836292](https://pubmed.ncbi.nlm.nih.gov/18836292/)). Trafficking regulation is therefore an intrinsic property of the GluN1 subunit.

### Finding 5 — De novo GRIN1 variants cause a severe NMDAR channelopathy

Human genetics confirms the subunit's essential role from the disease side. De novo *GRIN1* mutations cause a severe early-infantile neurodevelopmental encephalopathy characterized by intellectual disability, hypotonia, hyperkinetic and stereotyped movements, and epilepsy ([PMID: 28389307](https://pubmed.ncbi.nlm.nih.gov/28389307/)): *"De novo GRIN1 mutations have recently been shown to cause severe intellectual disability, hypotonia, hyperkinetic and stereotyped movements, and epilepsy."* Mechanistic characterization links genotype to channel dysfunction: a recurrent de novo variant, **GluN1-M641I**, produces gain-of-function channels showing *"enhanced agonist potency and reduced Mg²⁺"* block ([PMID: 34227748](https://pubmed.ncbi.nlm.nih.gov/34227748/)). Variants in the pre-M1 / S1-M1 linker region of GRIN1 (and the paralogous GRIN2 genes) critically alter channel gating, agonist potency, open probability, and surface expression; this helix is essentially devoid of variation in healthy populations while being a hotspot for pathogenic de novo variants ([PMID: 37000222](https://pubmed.ncbi.nlm.nih.gov/37000222/)). A conserved M4 glycine acts as a gating hinge where disease-associated mutations produce slow deactivation and high Ca²⁺ flux ([PMID: 30217972](https://pubmed.ncbi.nlm.nih.gov/30217972/)). These disease mechanisms directly corroborate GluN1's role in co-agonist binding, Mg²⁺ block, and gating.

### Finding 6 — GluN1 partners with GluN3 to form glycine-gated excitatory receptors (eGlyR)

GluN1's functional repertoire extends beyond classic NMDA receptors. When assembled with GluN3 subunits rather than GluN2, GluN1 forms receptors with fundamentally different pharmacology: unlike GluN2-containing NMDARs that require both glutamate and glycine, **GluN3-containing receptors are activated solely by glycine** ([PMID: 42665662](https://pubmed.ncbi.nlm.nih.gov/42665662/)): *"Unlike GluN2-containing NMDARs, GluN3-containing receptors are activated solely by glycine."* Native GluN3A-containing receptors are *"diheteromeric assemblies"* of GluN1 and GluN3A, and cryo-EM shows glycine opens the channel via conformational changes in GluN3A. These **excitatory glycine receptors (eGlyRs)** have a defined physiological role: discrete interneuron subsets use GluN1/GluN3A eGlyRs to regulate hippocampal network activity throughout development and evolution ([PMID: 41472680](https://pubmed.ncbi.nlm.nih.gov/41472680/)). Thus GluN1 is the common glycine-binding subunit shared between two functionally distinct receptor classes — the glutamate+glycine-gated GluN1/GluN2 NMDAR and the glycine-only-gated GluN1/GluN3 eGlyR. The same glycine-clamping module is deployed either as a co-agonist gate (with GluN2) or as the primary agonist gate (with GluN3).

### Finding 7 — Gating requires two glycine sites; the exon-5 cassette tunes allosteric modulation

Because the receptor contains two GluN1 subunits, it contains two glycine sites, and both must be occupied for the channel to open. Channel gating requires a **quadruply-liganded state** — binding of two glutamate and two glycine molecules ([PMID: 32070387](https://pubmed.ncbi.nlm.nih.gov/32070387/)): *"The quadruply-liganded state of binding of two glutamate and two glycine molecules to the receptor drives channel gating,"* enabling cation and Ca²⁺ flux. GluN1's N-terminal **exon-5 splice cassette** acts as an allosteric tuning module: the exon-5 insert of NR1-1b *"regulates the magnitude of proton-dependent PS [pregnenolone sulfate] potentiation"* and modulates tonic proton inhibition and polyamine sensitivity ([PMID: 21883211](https://pubmed.ncbi.nlm.nih.gov/21883211/)). Alternative splicing of GluN1 therefore directly controls how the receptor responds to protons (pH) and neurosteroids, adding a layer of context-dependent regulation on top of the core gating machinery.

### Finding 8 — The GluN1 C-terminal tail mediates Ca²⁺/calmodulin-dependent inactivation

GluN1 is not a passive pore — its cytoplasmic tail actively limits its own Ca²⁺ throughput. Ca²⁺ influx through NMDA channels is curtailed by a rapid **Ca²⁺/calmodulin (CaM)-dependent inactivation** that results from competitive displacement of cytoskeleton-binding proteins from the GluN1 (NR1) subunit by Ca²⁺/CaM ([PMID: 10844014](https://pubmed.ncbi.nlm.nih.gov/10844014/)): *"The influx of Ca(2+) through NMDA channels is limited by a rapid and Ca(2+)/calmodulin (CaM)-dependent inactivation that results from a competitive displacement of cytoskeleton-binding proteins from the NR1 subunit of the receptor by Ca(2+)/CaM."* The same study shows PKC phosphorylates the NR1 C-terminus, and PKC and CaM converge on steady-state current — i.e., GluN1's tail integrates kinase and Ca²⁺-sensor signals. Calmodulin binds a high-affinity site in the GluN1 **C1 exon cassette** and a lower-affinity site in the C-terminal region ([PMID: 9089692](https://pubmed.ncbi.nlm.nih.gov/9089692/)): *"NMDA receptor function can be regulated by direct binding of calmodulin to a low and high affinity (C1 exon cassette) site in the C-terminal region of the NR1 subunit."* This makes the GluN1 tail a built-in Ca²⁺ sensor providing negative feedback on channel activity — a safeguard against excessive Ca²⁺ loading.

### Finding 9 — Subcellular localization dictates opposite outcomes: synaptic survival vs. extrasynaptic death

The downstream consequence of GluN1-receptor activation depends critically on *where* the receptor is located. The cellular outcome of NMDA receptor stimulation is dictated by subcellular localization: **synaptic NMDARs promote plasticity and survival**, driving CREB activation and neuroprotective gene expression, **whereas extrasynaptic NMDARs mediate excitotoxicity** and contribute to cell death in neurodegenerative diseases ([PMID: 31924235](https://pubmed.ncbi.nlm.nih.gov/31924235/)): *"Synaptic NMDARs promote plasticity and survival whereas extrasynaptic NMDARs mediate excitotoxicity and contribute to cell death in neurodegenerative diseases."* This dichotomy holds in human neurons: in iPSC-derived brain organoids, *"glutamate-induced excitotoxic cell death is mediated primarily by extrasynaptic N-methyl-d-aspartate receptors (NMDARs),"* while synaptic NMDAR activity drives sustained CREB phosphorylation and neuroprotection ([PMID: 34958875](https://pubmed.ncbi.nlm.nih.gov/34958875/)). The same molecular machine — a GluN1-containing receptor — thus serves as both a pro-survival plasticity engine and a pro-death excitotoxicity trigger, with location as the decisive variable. This principle underlies NMDAR involvement in ischemic stroke and neurodegeneration ([PMID: 40490524](https://pubmed.ncbi.nlm.nih.gov/40490524/)).

### Finding 10 — GluN1's function is corroborated by its modular, evolutionarily derived domain architecture

Structure and evolution independently validate the functional assignments above. The GluN1 S1S2 ligand-binding core adopts a bilobed **"clamshell"** fold, characteristic of bacterial periplasmic binding proteins, that closes around glycine/D-serine and opens in the presence of antagonist ([PMID: 12805203](https://pubmed.ncbi.nlm.nih.gov/12805203/)): *"The cleft of the S1S2 'clamshell' is open in the presence of the antagonist DCKA and closed in the glycine, DS and DCS complexes."* This domain-closure mechanism is the structural basis of gating. GluN1 is evolutionarily related to the AMPA-receptor GluR2 subunit (~40% homology in the ligand-binding core), and the partial-agonist mechanism it uses is a refinement of the paradigm established for GluR2 ([PMID: 15996549](https://pubmed.ncbi.nlm.nih.gov/15996549/)): *"the NR1 subunit provides a new paradigm for partial agonist action that is distinct from that of the evolutionarily related GluR2, AMPA-sensitive receptor."* Evolutionary trace and molecular-dynamics analyses of ionotropic glutamate receptor sequences map the ligand-binding residues and show that disruption of domain closure impairs channel activation ([PMID: 15597199](https://pubmed.ncbi.nlm.nih.gov/15597199/)). The InterPro domain annotations supplied with the target (ATD ANF clamshell IPR001828; Glu/Gly-binding IPR019594; ionotropic pore module IPR001508/IPR015683/IPR001320; family TC 1.A.10.1) correspond precisely to this architecture.

---

## Mechanistic Model / Interpretation

The findings converge on a single coherent model of GluN1 as a multifunctional, obligatory receptor subunit whose domains each carry out a distinct part of the receptor's job.

### Receptor architecture and the coincidence-detection logic

```
          EXTRACELLULAR
   ┌───────────────────────────────┐
   │  ATD (ANF clamshell)  GluN1+GluN2   <- allosteric: Zn2+, protons,
   │                                        polyamines; GluN1 exon-5 tunes this
   ├───────────────────────────────┤
   │  LBD (S1S2 clamshell)               <- GluN1 binds GLYCINE / D-SERINE
   │                                        GluN2 binds GLUTAMATE
   │                                        BOTH closed => gate opens
   ├───────────────────────────────┤
   │  TMD pore  (1-2-1-2)                <- Mg2+ block (voltage-dependent)
   │  ================= MEMBRANE ======      Ca2+-permeable when open
   ├───────────────────────────────┤
   │  GluN1 C-terminal tail              <- C1: ER-retention signal (trafficking)
   │                                        CaM binding => Ca2+/CaM inactivation
   │                                        PKC phosphorylation; PDZ motif
   └───────────────────────────────┘
          INTRACELLULAR
```

**Opening the channel requires three simultaneous conditions** (coincidence detection):

| Requirement | Subunit / site | Evidence |
|---|---|---|
| Glycine / D-serine bound | GluN1 LBD (×2) | [PMID: 12805203](https://pubmed.ncbi.nlm.nih.gov/12805203/) |
| Glutamate bound | GluN2 LBD (×2) | [PMID: 12805203](https://pubmed.ncbi.nlm.nih.gov/12805203/) |
| Mg²⁺ block relieved | TMD pore (depolarization) | [PMID: 25008524](https://pubmed.ncbi.nlm.nih.gov/25008524/) |
| → Net: quadruply-liganded + depolarized | whole receptor | [PMID: 32070387](https://pubmed.ncbi.nlm.nih.gov/32070387/) |

Only when all three are met does the pore open to Ca²⁺ and other cations, converting coincident synaptic activity into a Ca²⁺ signal that drives LTP, LTD, learning, and memory.

### GluN1 as a combinatorial hub

| Partner subunit | Receptor type | Gating agonist(s) | Role | Evidence |
|---|---|---|---|---|
| GluN2 (A–D) | Classic NMDAR | Glutamate **and** glycine | Coincidence detector; plasticity, Ca²⁺ signaling | [PMID: 12805203](https://pubmed.ncbi.nlm.nih.gov/12805203/), [PMID: 16281028](https://pubmed.ncbi.nlm.nih.gov/16281028/) |
| GluN3 (A/B) | Excitatory glycine receptor (eGlyR) | Glycine **only** | Interneuron network regulation, development | [PMID: 42665662](https://pubmed.ncbi.nlm.nih.gov/42665662/), [PMID: 41472680](https://pubmed.ncbi.nlm.nih.gov/41472680/) |

In both cases GluN1 contributes the glycine-binding clamshell; the identity of the partner subunit redefines whether glutamate is also required.

### Regulatory layers intrinsic to GluN1

1. **Splicing (N-terminal exon-5):** tunes proton inhibition, polyamine, and neurosteroid (pregnenolone sulfate) modulation ([PMID: 21883211](https://pubmed.ncbi.nlm.nih.gov/21883211/)).
2. **Trafficking (C-terminal C1):** ER retention signal controls surface delivery; overridden by PDZ motif or phosphorylation; specialized dendritic secretory pathway ([PMID: 11640925](https://pubmed.ncbi.nlm.nih.gov/11640925/), [PMID: 19620977](https://pubmed.ncbi.nlm.nih.gov/19620977/)).
3. **Feedback inactivation (C-terminal tail):** Ca²⁺/calmodulin displaces cytoskeletal anchors to inactivate the channel — a self-limiting brake on Ca²⁺ influx; PKC phosphorylation modulates this ([PMID: 10844014](https://pubmed.ncbi.nlm.nih.gov/10844014/), [PMID: 9089692](https://pubmed.ncbi.nlm.nih.gov/9089692/)).

### Location determines life-or-death signaling

```
          GluN1-containing NMDAR
           /                   \
      SYNAPTIC              EXTRASYNAPTIC
   Ca2+ -> CREB ON          Ca2+ -> CREB OFF
   survival genes           excitotoxic death
   LTP / plasticity         stroke / neurodegeneration
   [PMID 31924235]          [PMID 34958875, 40490524]
```

The identical receptor complex produces opposite fates depending on subcellular localization — a central theme in the pathophysiology of ischemic stroke and neurodegenerative disease.

### Pathway context

GluN1/NMDAR sits at the heart of the glutamatergic excitatory signaling pathway: (1) presynaptic glutamate release + ambient glycine/D-serine occupy the GluN2 and GluN1 sites; (2) coincident postsynaptic depolarization (often via AMPA receptors) relieves Mg²⁺ block; (3) channel opening admits Ca²⁺ at the postsynaptic density; (4) Ca²⁺ activates downstream effectors (CaMKII, calcineurin, Ras-ERK, CREB) that execute LTP/LTD, receptor trafficking, and transcriptional programs underlying memory and development. GluN1's own contribution to pathway specificity is the **co-agonist gate** (glycine/D-serine requirement) and the **obligatory scaffolding** that determines whether any NMDAR exists at all.

### Why GluN1 is essential and disease-associated

Because GluN1 is the obligatory subunit, its complete loss abolishes all NMDA signaling and is lethal ([PMID: 8060614](https://pubmed.ncbi.nlm.nih.gov/8060614/)), while point mutations that subtly shift agonist potency, Mg²⁺ block, or gating (e.g., GluN1-M641I; pre-M1 linker variants) cause severe encephalopathy without abolishing the receptor ([PMID: 34227748](https://pubmed.ncbi.nlm.nih.gov/34227748/), [PMID: 37000222](https://pubmed.ncbi.nlm.nih.gov/37000222/), [PMID: 28389307](https://pubmed.ncbi.nlm.nih.gov/28389307/)). The genetics bracket GluN1's function from both the null and the dysfunction directions.

---

## Evidence Base

| PMID | Study (abbrev.) | Type | How it supports the findings |
|---|---|---|---|
| [8060614](https://pubmed.ncbi.nlm.nih.gov/8060614/) | *Targeted disruption of NMDA receptor 1 gene...* | In vivo genetics (mouse KO) | GluN1 obligatory & non-redundant; loss abolishes NMDA Ca²⁺/currents; neonatal lethality (F001) |
| [19794189](https://pubmed.ncbi.nlm.nih.gov/19794189/) | *Behavioral deficits... mutant NMDA receptors...* | Mouse hypomorph / review | GluN1 obligatory, no functional homolog, ubiquitous expression; coincidence detection → LTP/learning (F001) |
| [12805203](https://pubmed.ncbi.nlm.nih.gov/12805203/) | *Crystal structures of the NMDA receptor NR1 LBD core* | X-ray crystallography | GluN1 binds glycine/D-serine; clamshell closes on agonist, opens on antagonist (F002, F010) |
| [16281028](https://pubmed.ncbi.nlm.nih.gov/16281028/) | *Subunit arrangement and function in NMDA receptors* | Structure/function | GluN1–GluN2A heterodimer is the functional unit (F002) |
| [25008524](https://pubmed.ncbi.nlm.nih.gov/25008524/) | *NMDA receptor structures reveal subunit arrangement...* | X-ray (intact receptor) | 1-2-1-2 architecture; Hebbian coincidence detection; Mg²⁺ block (F003) |
| [11640925](https://pubmed.ncbi.nlm.nih.gov/11640925/) | *An ER retention signal explains surface expression...* | Cell biology | ER retention signal in GluN1 C1 cassette; overridden by PDZ/phospho (F004) |
| [19620977](https://pubmed.ncbi.nlm.nih.gov/19620977/) | *SAP97 and CASK mediate sorting of NMDARs...* | Cell biology | Dedicated dendritic secretory pathway for NMDARs (F004) |
| [18836292](https://pubmed.ncbi.nlm.nih.gov/18836292/) | *Role of the fourth membrane domain of NR2B...* | Cell biology | M3 ER-retention determinants ensure only assembled complexes surface (F004) |
| [28389307](https://pubmed.ncbi.nlm.nih.gov/28389307/) | *De novo GRIN1 mutations...encephalopathy* | Human genetics / review | Defines GRIN1-related neurodevelopmental disorder phenotype (F005) |
| [34227748](https://pubmed.ncbi.nlm.nih.gov/34227748/) | *Recurrent seizure-related GRIN1 variant...* | Functional electrophysiology | GluN1-M641I gain-of-function: ↑agonist potency, ↓Mg²⁺ block (F005) |
| [37000222](https://pubmed.ncbi.nlm.nih.gov/37000222/) | *S1-M1 linker...controls channel opening* | Functional variant screen | Pre-M1 linker variants in GRIN1 alter gating; intolerant to variation (F005) |
| [30217972](https://pubmed.ncbi.nlm.nih.gov/30217972/) | *A conserved glycine...slow deactivation, high Ca²⁺* | Electrophysiology/MD | M4 glycine gating hinge; disease mutations alter gating (F005) |
| [42665662](https://pubmed.ncbi.nlm.nih.gov/42665662/) | *Gating/allosteric modulation of GluN1-GluN3A...* | Cryo-EM / physiology | GluN1/GluN3 gated by glycine alone; diheteromeric assembly (F006) |
| [41472680](https://pubmed.ncbi.nlm.nih.gov/41472680/) | *Interneuron subsets...GluN1/GluN3A eGlyR...* | Circuit physiology | eGlyR physiological role in hippocampal networks (F006) |
| [32070387](https://pubmed.ncbi.nlm.nih.gov/32070387/) | *Tripartite signalling by NMDA receptors* | Review | Quadruply-liganded (2 glutamate + 2 glycine) state drives gating (F007) |
| [21883211](https://pubmed.ncbi.nlm.nih.gov/21883211/) | *A steroid modulatory domain in NR2A...NR1 exon-5...* | Electrophysiology | GluN1 exon-5 tunes proton/pregnenolone-sulfate modulation (F007) |
| [10844014](https://pubmed.ncbi.nlm.nih.gov/10844014/) | *PKC regulates Ca²⁺-dependent inactivation of NMDARs* | Electrophysiology | Ca²⁺/CaM inactivation via displacement from GluN1; PKC phosphorylation (F008) |
| [9089692](https://pubmed.ncbi.nlm.nih.gov/9089692/) | *Ca²⁺-dependent inactivation...CaM binding of NR1* | Biochemistry/physiology | Maps CaM sites to GluN1 C-terminus incl. C1 cassette (F008) |
| [31924235](https://pubmed.ncbi.nlm.nih.gov/31924235/) | *microRNA signature of toxic extrasynaptic NMDAR...* | Molecular/cell biology | Synaptic=survival vs extrasynaptic=excitotoxicity dichotomy (F009) |
| [34958875](https://pubmed.ncbi.nlm.nih.gov/34958875/) | *NMDAR-mediated preconditioning...iPSC organoids* | Human iPSC model | Extrasynaptic NMDARs drive excitotoxic death in human neurons (F009) |
| [15996549](https://pubmed.ncbi.nlm.nih.gov/15996549/) | *Mechanism of partial agonist action at NR1* | Crystallography | GluN1↔GluR2 evolutionary relationship; partial-agonist paradigm (F010) |
| [15597199](https://pubmed.ncbi.nlm.nih.gov/15597199/) | *Evolutionary trace analysis of iGluR sequences* | Bioinformatics/MD | Conserved ligand-binding residues; domain closure essential for gating (F010) |
| [40490524](https://pubmed.ncbi.nlm.nih.gov/40490524/) | *NMDAR pathways in ischemic stroke* | Review | Synaptic vs extrasynaptic NMDAR signaling in stroke (context for F009) |

Supporting/contextual literature also reviewed includes the role of D-serine and serine racemase as the endogenous co-agonist source ([PMID: 37833512](https://pubmed.ncbi.nlm.nih.gov/37833512/), [PMID: 36535077](https://pubmed.ncbi.nlm.nih.gov/36535077/)); GlyT1 control of ambient glycine and co-agonist site occupancy ([PMID: 39059742](https://pubmed.ncbi.nlm.nih.gov/39059742/), [PMID: 39770104](https://pubmed.ncbi.nlm.nih.gov/39770104/)); subunit-selective allosteric modulators acting via the GluN1 co-agonist site ([PMID: 41335128](https://pubmed.ncbi.nlm.nih.gov/41335128/)); triheteromeric gating/ketamine sensitivity ([PMID: 39954679](https://pubmed.ncbi.nlm.nih.gov/39954679/)); and GluN2-subunit diversity governing plasticity and disease ([PMID: 31508206](https://pubmed.ncbi.nlm.nih.gov/31508206/), [PMID: 39596430](https://pubmed.ncbi.nlm.nih.gov/39596430/)). None of these contradict the findings; they reinforce GluN1's identity as the glycine-site-bearing obligatory subunit.

**Consistency assessment:** The evidence base is unusually convergent. Genetic ablation, human disease variants, multiple independent crystal and cryo-EM structures, electrophysiology, cell-biological trafficking studies, and evolutionary/bioinformatic analyses all point to the same core conclusions, with no material contradictions among the primary sources used for the findings.

---

## Limitations and Knowledge Gaps

1. **Model-system dependence.** Much of the definitive functional and structural work (knockouts, S1S2 crystal structures, Ca²⁺/CaM inactivation) was performed in rodent or recombinant/*Xenopus* systems. While GluN1 is highly conserved and the human disease genetics align, strictly human experimental data remain comparatively sparse (the iPSC organoid study, [PMID: 34958875](https://pubmed.ncbi.nlm.nih.gov/34958875/), is a notable exception).

2. **GluN1 splice-variant diversity.** GluN1 has eight splice variants (combinations of the N-terminal exon-5 and C-terminal C1/C2/C2′ cassettes). This report documents functional consequences of exon-5 and C1, but the full functional map of all variants — their regional expression, trafficking, and modulation — is incomplete.

3. **eGlyR physiology is still emerging.** The GluN1/GluN3 excitatory glycine receptor has only recently been structurally and physiologically characterized. Its precise native stoichiometry, circuit-level roles beyond hippocampal interneurons, and contribution to human disease remain under active investigation.

4. **Mechanistic granularity of the synaptic/extrasynaptic switch.** The dichotomy is well established, but how GluN1-receptor localization is dynamically regulated, and whether GluN1 (versus the GluN2 subtype) directly determines the survival-versus-death signaling, is not fully resolved. Much of the death-signaling specificity has been attributed to the GluN2B C-terminus rather than GluN1.

5. **Quantitative affinity/kinetic parameters** (e.g., exact glycine EC₅₀, Ca²⁺ permeability ratios) vary with subunit composition and were not systematically tabulated here; they depend on the GluN2 partner.

6. **Non-neuronal / peripheral roles.** GluN1 expression and potential functions outside the CNS were not examined.

---

## Proposed Follow-up Experiments / Actions

1. **Comprehensive human splice-variant functional map.** Express all eight human GluN1 splice variants with each GluN2 subtype in a uniform human cellular background (e.g., iPSC-derived neurons) and systematically measure glycine/D-serine potency, proton/polyamine/neurosteroid modulation, surface trafficking, and Ca²⁺/CaM inactivation — resolving limitation #2.

2. **Isolate the subunit source of the survival/death switch.** Using GluN1 C-terminal mutants (ER-retention, PDZ, CaM, PKC sites) in synaptic- vs extrasynaptic-targeted contexts, dissect whether GluN1's tail contributes to the CREB-on vs CREB-off decision independently of GluN2B — addressing limitation #4.

3. **Structural characterization of GluN1 regulatory states.** Obtain cryo-EM structures of full-length GluN1-containing receptors with the Ca²⁺/CaM complex bound to the C-terminal tail, to visualize the inactivation mechanism at atomic resolution (extends F008).

4. **Deep mutational scanning of GRIN1.** Systematically assay the functional effect of all possible GRIN1 missense variants (agonist potency, Mg²⁺ block, open probability, surface expression) to build a clinical variant-interpretation resource, extending the targeted studies ([PMID: 34227748](https://pubmed.ncbi.nlm.nih.gov/34227748/), [PMID: 37000222](https://pubmed.ncbi.nlm.nih.gov/37000222/)).

5. **In vivo eGlyR physiology.** Use GluN3-conditional and GluN1-reporter mouse lines (and human tissue where feasible) to define the circuit and behavioral roles of GluN1/GluN3 excitatory glycine receptors (extends F006).

6. **Co-agonist supply in human disease.** Quantify how serine racemase / D-serine and GlyT1 set GluN1 co-agonist site occupancy in human neurons, linking the biochemical supply chain ([PMID: 37833512](https://pubmed.ncbi.nlm.nih.gov/37833512/), [PMID: 39059742](https://pubmed.ncbi.nlm.nih.gov/39059742/)) to therapeutic modulation of NMDAR hypo-/hyperfunction.

---

## Conclusion

GRIN1 encodes GluN1, the obligatory, non-redundant, glycine/D-serine-binding subunit of the NMDA receptor. Its primary molecular function is to supply the co-agonist binding site and co-assemble (two GluN1 + two GluN2, 1-2-1-2) into a ligand- and voltage-gated, Ca²⁺-permeable cation channel that acts as a Hebbian coincidence detector at the postsynaptic membrane of central neurons. The channel opens only when glutamate (on GluN2), glycine (on GluN1), and depolarization (relieving Mg²⁺ block) coincide, generating the Ca²⁺ signals that drive synaptic plasticity, learning, memory, and neurodevelopment. GluN1 additionally forms glycine-only-gated eGlyRs with GluN3, carries intrinsic regulatory modules (exon-5 allosteric tuning, C1 ER-retention trafficking control, C-terminal Ca²⁺/CaM feedback inactivation), and mediates opposite survival-versus-death outcomes depending on synaptic versus extrasynaptic localization. Its essential role is confirmed by neonatal-lethal knockouts and severe de novo human encephalopathy variants, and its mechanism by crystal/cryo-EM structures and evolutionary analysis.


## Artifacts

- [OpenScientist final report](GRIN1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](GRIN1-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:8060614
2. PMID:19794189
3. PMID:12805203
4. PMID:16281028
5. PMID:37833512
6. PMID:39059742
7. PMID:25008524
8. PMID:11640925
9. PMID:19620977
10. PMID:18836292
11. PMID:28389307
12. PMID:34227748
13. PMID:37000222
14. PMID:30217972
15. PMID:42665662
16. PMID:41472680
17. PMID:32070387
18. PMID:21883211
19. PMID:10844014
20. PMID:9089692
21. PMID:31924235
22. PMID:34958875
23. PMID:40490524
24. PMID:15996549
25. PMID:15597199
26. PMID:36535077
27. PMID:39770104
28. PMID:41335128
29. PMID:39954679
30. PMID:31508206
31. PMID:39596430