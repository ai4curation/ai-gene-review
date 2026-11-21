---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-14T20:27:10.919065'
end_time: '2026-11-14T20:49:03.340859'
duration_seconds: 1312.42
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: GRIN2B
  gene_symbol: GRIN2B
  uniprot_accession: Q13224
  protein_description: 'RecName: Full=Glutamate receptor ionotropic, NMDA 2B {ECO:0000305};
    Short=GluN2B {ECO:0000303|PubMed:26912815}; AltName: Full=Glutamate [NMDA] receptor
    subunit epsilon-2; AltName: Full=N-methyl D-aspartate receptor subtype 2B; Short=NMDAR2B
    {ECO:0000303|PubMed:7959773}; Short=NR2B; AltName: Full=N-methyl-D-aspartate receptor
    subunit 3; Short=NR3; Short=hNR3 {ECO:0000303|PubMed:7999784}; Flags: Precursor;'
  gene_info: Name=GRIN2B {ECO:0000303|Ref.3, ECO:0000312|HGNC:HGNC:4586}; Synonyms=NMDAR2B
    {ECO:0000303|PubMed:7959773};
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
citation_count: 25
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: GRIN2B-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: GRIN2B-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q13224
- **Protein Description:** RecName: Full=Glutamate receptor ionotropic, NMDA 2B {ECO:0000305}; Short=GluN2B {ECO:0000303|PubMed:26912815}; AltName: Full=Glutamate [NMDA] receptor subunit epsilon-2; AltName: Full=N-methyl D-aspartate receptor subtype 2B; Short=NMDAR2B {ECO:0000303|PubMed:7959773}; Short=NR2B; AltName: Full=N-methyl-D-aspartate receptor subunit 3; Short=NR3; Short=hNR3 {ECO:0000303|PubMed:7999784}; Flags: Precursor;
- **Gene Information:** Name=GRIN2B {ECO:0000303|Ref.3, ECO:0000312|HGNC:HGNC:4586}; Synonyms=NMDAR2B {ECO:0000303|PubMed:7959773};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the glutamate-gated ion channel (TC 1.A.10.1)
- **Key Domains:** ANF_lig-bd_rcpt. (IPR001828); Glu/Gly-bd. (IPR019594); Iono_Glu_rcpt_met. (IPR001508); Ionotropic_Glu_rcpt. (IPR015683); Iontro_rcpt_C. (IPR001320)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GRIN2B" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GRIN2B' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GRIN2B** (gene ID: GRIN2B, UniProt: Q13224) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# GRIN2B (GluN2B / NR2B): Functional Annotation Report

**UniProt:** Q13224 | **Gene:** GRIN2B (HGNC:4586) | **Organism:** *Homo sapiens* (Human)
**Protein family:** Glutamate-gated ion channel (TC 1.A.10.1)
**Protein:** Glutamate receptor ionotropic, NMDA 2B (GluN2B; NR2B; NMDAR2B; ε2 subunit)

---

## Summary

**GRIN2B encodes GluN2B (also called NR2B, NMDAR2B, or glutamate receptor subunit epsilon-2), a glutamate-binding, pore-forming subunit of the N-methyl-D-aspartate (NMDA) subtype of ionotropic glutamate receptor.** Its primary molecular function is neither enzymatic nor transport of a metabolite in the classical sense: GluN2B is a **ligand-gated cation channel subunit**. It co-assembles with the obligatory glycine-binding GluN1 subunit to build a heterotetrameric receptor (a dimer of GluN1–GluN2B heterodimers) that opens a Ca²⁺-permeable, voltage-dependently Mg²⁺-blocked cation pore when it simultaneously binds the neurotransmitter **L-glutamate** (on GluN2B) and a co-agonist, **glycine or D-serine** (on GluN1), while the membrane is depolarized. This dual requirement makes the receptor a molecular **coincidence detector** that converts correlated pre- and post-synaptic activity into a Ca²⁺ signal.

The receptor operates at the **neuronal plasma membrane**, where GluN2B protein is enriched in the forebrain — most intensely in hippocampal CA pyramidal neurons and cortical pyramidal neurons of layers II/III and V. Subcellularly it sits predominantly at **postsynaptic densities** of glutamatergic synapses, but is also found at **extrasynaptic** membrane sites and, rarely, presynaptically. The Ca²⁺ influx it conducts triggers downstream signaling that is physically organized by GluN2B's own domains: the extracellular **amino-terminal domain (ATD)** carries a GluN2B-selective allosteric control site (the ifenprodil/radiprodil pocket at the GluN1–GluN2B interface), and the intracellular **C-terminal domain (CTD)** acts as a scaffolding/signaling adapter that binds CaMKII and, via a PDZ ligand, the MAGUK scaffolds PSD-95 and SAP102. Through these interactions GluN2B gates the threshold for synaptic plasticity (LTP/LTD) and links receptor activation both to pro-survival CREB/BDNF signaling (synaptic pool) and to excitotoxic cell death (extrasynaptic/excess activation).

GluN2B is the dominant NMDAR subunit early in development and is progressively replaced by GluN2A (the "NR2B-to-NR2A switch"), which accelerates receptor kinetics. Its functional properties — high glutamate affinity, slow deactivation, Mg²⁺ block, ifenprodil sensitivity — are intrinsic to the subunit and evolutionarily conserved from teleost fish to mammals. Clinically, **de novo GRIN2B variants cause a primary Mendelian disorder of glutamatergic neurotransmission** (intellectual disability, autism spectrum disorder, epilepsy, and movement/language disorders) by producing NMDAR gain- or loss-of-function.

---

## Gene/Protein Identity Verification

All literature retrieved in this investigation is consistent with the UniProt target. The gene symbol **GRIN2B** unambiguously corresponds to the human NMDA receptor subunit GluN2B/NR2B. The protein family (glutamate-gated ion channel) and signature domains (ANF ligand-binding receptor / IPR001828; Glu/Gly-binding / IPR019594; ionotropic glutamate receptor metabotropic-like / IPR001508 & IPR015683; ionotropic receptor C-terminal / IPR001320) match the three-layer NMDAR architecture (ATD, ligand-binding domain [LBD], transmembrane domain [TMD]) resolved crystallographically ([PMID: 24876489](https://pubmed.ncbi.nlm.nih.gov/24876489/)). No evidence of a conflicting same-symbol gene in another organism was encountered. **Identity confirmed — research proceeds on the correct target.**

---

## Key Findings

### 1. GluN2B is a glutamate-binding subunit of the heterotetrameric NMDA receptor ion channel

The defining structural fact about GRIN2B is that its product does not function alone — it is one building block of a four-subunit (heterotetrameric) ligand-gated ion channel. The 4 Å crystal structure of the intact GluN1–GluN2B receptor revealed that the receptor is arranged as **a dimer of GluN1–GluN2B heterodimers**, with a layered architecture comprising the amino-terminal domain (ATD), the ligand-binding domain (LBD), and the transmembrane domain (TMD) that forms the ion-conducting pore ([PMID: 24876489](https://pubmed.ncbi.nlm.nih.gov/24876489/)). Within this assembly, GluN2B supplies the **L-glutamate-binding site**, while GluN1 binds the co-agonist glycine/D-serine. This is the structural basis for the receptor's obligate heteromeric nature and for the subunit-specific pharmacology described below.

### 2. GluN2B-containing NMDARs are Ca²⁺-permeable and voltage-dependently Mg²⁺-blocked, requiring glutamate plus a co-agonist

The functional signature of the NMDA receptor is a triple requirement: agonist (glutamate), co-agonist (glycine or D-serine), and membrane depolarization to relieve a voltage-dependent Mg²⁺ block of the pore. NMDARs "bind the neurotransmitter glutamate and a co-agonist, either glycine or D-serine" ([PMID: 41278716](https://pubmed.ncbi.nlm.nih.gov/41278716/)). The receptor's Ca²⁺ permeability and Mg²⁺ sensitivity are determined at the molecular level by specific residues at the tip of the pore (re-entrant M2) loop: "Both Mg²⁺ sensitivity and Ca²⁺ permeability are critically dependent on the amino acids at the N and N+1 positions" ([PMID: 20958962](https://pubmed.ncbi.nlm.nih.gov/20958962/)). The functional consequence is that the receptor conducts a significant Ca²⁺ current only when glutamate release coincides with postsynaptic depolarization — the physical embodiment of **coincidence detection** that underlies activity-dependent plasticity.

### 3. The ATD carries a GluN2B-selective allosteric (ifenprodil) modulatory site at the GluN1–GluN2B interface

GluN2B is pharmacologically distinguished from other GluN2 subunits by a selective allosteric site. Structural work mapped "the binding mode of multiple diaryl GluN2B-selective negative allosteric modulators at the interface between the GluN1 and GluN2B amino-terminal domains" ([PMID: 22596351](https://pubmed.ncbi.nlm.nih.gov/22596351/)). Mechanistically, "the allosteric modulatory pathway starts at the ifenprodil binding pocket in the amino terminal domain and immobilizes the connecting α5-helix to the ligand binding domain, resulting in inhibition" ([PMID: 37542648](https://pubmed.ncbi.nlm.nih.gov/37542648/)). This ATD pocket is the target of the classic GluN2B-selective antagonist ifenprodil and clinical candidates such as radiprodil, and it is the structural reason GluN2B can be probed and drugged independently of GluN2A-containing receptors.

### 4. The cytoplasmic C-terminal domain controls postsynaptic targeting and trafficking via a PDZ ligand and CaMKII site

Beyond gating ions, GluN2B's long intracellular CTD is a signaling/scaffolding hub. Casein kinase II phosphorylates Ser1480, located within the C-terminal PDZ ligand (sequence -IESDV): "Phosphorylation of Ser1480 disrupts the interaction of NR2B with the PDZ domains of PSD-95 and SAP102 and decreases surface NR2B expression in neurons" ([PMID: 15537897](https://pubmed.ncbi.nlm.nih.gov/15537897/)). The CTD also biases receptor trafficking itineraries: a subunit-specific trafficking assay revealed "a dominant role for NR2B in receptor recycling," with "NR2B preferentially trafficking through the recycling pathway" ([PMID: 20427279](https://pubmed.ncbi.nlm.nih.gov/20427279/)). Thus the CTD couples receptor surface expression and synaptic anchoring to activity (via CKII/CaMKII) and determines the dynamic pool of GluN2B available at the synapse.

### 5. GluN2B predominates early in development and is progressively replaced by GluN2A

NMDAR subunit composition is developmentally regulated. "During development, GluN2A becomes incorporated into previously GluN2B-dominated NMDARs" ([PMID: 30355491](https://pubmed.ncbi.nlm.nih.gov/30355491/)). Functionally, this switch "[produces] a speeding of the NMDAR EPSC decay, accompanied by a decrease in sensitivity to ifenprodil (selective NR2B-antagonist)" ([PMID: 10934236](https://pubmed.ncbi.nlm.nih.gov/10934236/)). GluN2B's hallmark is therefore **slow deactivation kinetics**, which lengthen the excitatory postsynaptic current and the window for Ca²⁺ entry — a property well-suited to the high plasticity of the immature and newly-forming synapse. Importantly, the switch is driven predominantly by GluN2A expression levels rather than by GluN2-subtype-specific C-terminal sequences ([PMID: 30355491](https://pubmed.ncbi.nlm.nih.gov/30355491/)).

### 6. GluN2B operates at synaptic and extrasynaptic sites and strongly influences CREB-dependent survival vs. excitotoxicity

GluN2B contributes to NMDAR function at both synaptic and extrasynaptic membrane locations, and this location dictates downstream signaling valence. In a direct comparison, "compared with suppression of GluN2A, suppression of GluN2B resulted in more reduction of NMDA- and oxygen glucose deprivation-induced excitotoxicity" ([PMID: 23839940](https://pubmed.ncbi.nlm.nih.gov/23839940/)); GluN2B suppression also attenuated CREB–BDNF regulation more than GluN2A suppression, and GluN2B overexpression exaggerated excitotoxicity and CREB down-regulation. This places GluN2B at the pivot between the pro-survival (synaptic, CREB/BDNF-promoting) and pro-death (excessive/extrasynaptic, excitotoxic) arms of NMDAR Ca²⁺ signaling.

### 7. GluN2B gates the threshold for synaptic plasticity and enhances learning and memory in vivo

Causal genetic evidence links GluN2B levels directly to plasticity and cognition. Forebrain overexpression of NR2B "leads to enhanced activation of NMDA receptors, facilitating synaptic potentiation in response to stimulation at 10–100 Hz. These mice exhibit superior ability in learning and memory" ([PMID: 10485705](https://pubmed.ncbi.nlm.nih.gov/10485705/) — the classic "Doogie" mouse). A later study confirmed subunit specificity in prefrontal cortex: "The enhanced LTP was completely abolished by a NR2B subunit selective antagonist, Ro25-6981, indicating that overexpression of NR2B subunit is responsible for enhanced LTP," accompanied by improved working memory ([PMID: 21655294](https://pubmed.ncbi.nlm.nih.gov/21655294/)). GluN2B is therefore not merely correlated with plasticity — it is a rate-limiting, causal determinant of the LTP threshold.

### 8. GluN2B's defining functional properties are evolutionarily conserved and intrinsic to the subunit

Cross-species comparison demonstrates that GluN2B's biophysical identity is encoded within the subunit itself. Comparing teleost (apteronotid fish) and murine receptors, "the agonist binding sites on the apteronotid receptor are highly conserved, with nearly identical agonist affinities to those of the murine NR1/NR2B receptor. The kinetic responses of the fish receptor were also highly conserved, with deactivation rates for the AptNR2B receptor matching those of the murine NR2B containing receptor" ([PMID: 12574460](https://pubmed.ncbi.nlm.nih.gov/12574460/)). The conservation of glutamate affinity and slow deactivation over hundreds of millions of years of vertebrate evolution confirms these are intrinsic, subunit-conferred properties and not artifacts of a particular cellular context.

### 9. GluN2B carries the orthosteric L-glutamate agonist-binding site; GluN1 binds glycine

The division of agonist labor across subunits is well established structurally and pharmacologically. "Most NMDA receptors comprise two glycine-binding GluN1 and two glutamate-binding GluN2 subunits (GluN2A–D)" ([PMID: 28760974](https://pubmed.ncbi.nlm.nih.gov/28760974/)). The GluN2 clamshell LBD binds L-glutamate; the lack, for a time, of antagonist-bound GluN2 structures was explicitly noted as a "complete lack of antagonist-bound structures for the L-glutamate-binding GluN2 subunits" ([PMID: 24462099](https://pubmed.ncbi.nlm.nih.gov/24462099/)). Agonist binding closes the bilobed LBD "clamshell," and this closure is mechanically coupled through the linkers to opening of the TMD gate — the elementary gating transition of the receptor.

### 10. De novo GRIN2B missense variants cause a primary disorder of glutamatergic neurotransmission

GRIN2B is a confirmed human disease gene whose pathology precisely reflects its normal function. "A large number of de novo variants have been identified in the GRIN gene family in patients with various neurological and neuropsychiatric conditions, including autism, intellectual disability, epilepsy, language disorders and movement disorders" ([PMID: 40994429](https://pubmed.ncbi.nlm.nih.gov/40994429/)). These variants "[alter] the N-methyl D-aspartate receptor (NMDAR) function, with a genotype-phenotype relationship" ([PMID: 40024627](https://pubmed.ncbi.nlm.nih.gov/40024627/)), and critically "[missense] variants in these genes can result in gain or loss of the NMDAR function, requiring opposite therapeutic treatments" ([PMID: 39535073](https://pubmed.ncbi.nlm.nih.gov/39535073/)). The bidirectional (gain- or loss-of-function) nature of pathogenicity, and its dependence on proximity to ligand-binding/gating sites, directly corroborates that GluN2B's essential role is ligand-gated channel function. The GluN2B-selective positive modulator spermine/spermidine can rescue loss-of-function currents ([PMID: 40024627](https://pubmed.ncbi.nlm.nih.gov/40024627/)), and radiprodil inhibits gain-of-function variants ([PMID: 40994429](https://pubmed.ncbi.nlm.nih.gov/40994429/)).

### 11. GluN2B protein is forebrain-enriched and localized to postsynaptic, extrasynaptic, and rare presynaptic membranes

Immunohistochemistry and electron microscopy of adult rat telencephalon localize the subunit with ultrastructural precision. "[The] hippocampus represented the most intensively immunolabeled region. Here, predominantly the CA pyramidal neurons were heavily stained. Intense immunoreactivity (IR) was also detected in cortical neurons, in particular in pyramidal-like ones of layers II/III and V" ([PMID: 9878886](https://pubmed.ncbi.nlm.nih.gov/9878886/)). At the ultrastructural level, "the NR2B subunit was present not only in synaptic complexes where it usually was present in postsynaptic sites but in addition could be located at extrasynaptic sites. Furthermore, preliminary evidence indicates a presynaptic location of NR2B in some rare cases" ([PMID: 9878886](https://pubmed.ncbi.nlm.nih.gov/9878886/)). This pins the physical site of GluN2B function to the forebrain glutamatergic synapse and its immediate extrasynaptic surround.

---

## Mechanistic Model / Interpretation

GluN2B's function can be understood as a four-domain modular device embedded in the postsynaptic membrane, converting coincident chemical and electrical signals into an intracellular Ca²⁺-dependent program.

```
        EXTRACELLULAR
   ┌─────────────────────────┐
   │   ATD (amino-terminal)  │  ← GluN2B-selective allosteric site
   │   GluN1 ── GluN2B iface │    (ifenprodil / radiprodil / Zn2+ / H+ / polyamines)
   │   → tunes open prob.    │    [F003, F008]
   ├─────────────────────────┤
   │   LBD (clamshell)       │  GluN2B binds L-GLUTAMATE
   │   GluN1 binds GLYCINE   │  clamshell closure → gate opening
   │                         │    [F001, F010]
   ├───────╥─────────╥───────┤  ← PLASMA MEMBRANE
   │   TMD pore (M1-M3,M2loop)│  Ca2+-permeable; Mg2+ block (N/N+1 residues)
   │   voltage-dependent gate │    [F002]
   ├─────────────────────────┤
   │   CTD (cytoplasmic)     │  Ser1480 PDZ ligand (-IESDV)
   │   → PSD-95 / SAP102      │  CaMKII docking; recycling trafficking
   │   → CaMKII, signaling    │    [F004, F006]
   └─────────────────────────┘
        INTRACELLULAR / PSD
```

**The gating logic (coincidence detection).** At resting potential the pore is plugged by extracellular Mg²⁺. Presynaptic glutamate release loads the GluN2B LBD, and ambient glycine/D-serine occupies the GluN1 LBD, but no current flows until postsynaptic depolarization (e.g., from AMPA receptor activity or a back-propagating action potential) expels Mg²⁺ from the pore. Only when **glutamate + co-agonist + depolarization coincide** does the channel conduct — and because of the N/N+1 pore residues, the current carries substantial Ca²⁺ (F002). This is the biophysical substrate of Hebbian plasticity.

**Kinetics set the plasticity window.** GluN2B confers slow deactivation (F005, F008). A longer-lived current integrates more Ca²⁺ per event and widens the temporal window for coincidence, biasing synapses toward potentiation — directly explaining why elevating GluN2B lowers the LTP threshold and enhances learning (F007).

**Compartmentalized Ca²⁺ signaling.** Where the Ca²⁺ enters matters. Synaptic GluN2B-NMDARs, anchored by PSD-95/SAP102 via the CTD, couple to CaMKII and pro-survival CREB/BDNF transcription; excessive or extrasynaptic activation drives excitotoxic Ca²⁺ overload and CREB shut-off (F006). The same CTD that scaffolds the pro-plasticity machinery thus also sits at the fulcrum of the survival/death decision. Activity-dependent phosphorylation of the CTD PDZ ligand (Ser1480) dynamically tunes how many receptors are retained at the PSD (F004).

**Developmental and evolutionary framing.** GluN2B is the "default" early-life subunit, later diluted by faster GluN2A (F005); its core properties are conserved across vertebrates (F008), underscoring that the subunit itself — not its milieu — encodes high glutamate affinity, slow kinetics, and ifenprodil sensitivity.

**Disease as a readout of function.** Because channel gating is GluN2B's job, variants that perturb ligand binding or gating produce disease, and their directionality (gain vs. loss) predicts opposite therapeutic needs (F009) — a clean, clinically actionable corollary of the mechanistic model.

### Summary table of GluN2B functional modules

| Domain | Location | Primary role | Key ligand / partner | Finding |
|---|---|---|---|---|
| ATD | Extracellular, distal | Allosteric gating control; subunit-selective pharmacology | Ifenprodil, radiprodil, Zn²⁺, H⁺, polyamines | F003, F008 |
| LBD | Extracellular, membrane-proximal | **L-glutamate binding → gate opening** | L-glutamate (GluN2B); glycine/D-serine (GluN1) | F001, F010 |
| TMD | Transmembrane | Ca²⁺-permeable pore; voltage-dependent Mg²⁺ block | Ca²⁺, Mg²⁺ (N/N+1 residues) | F002 |
| CTD | Intracellular (PSD) | Trafficking, synaptic anchoring, signal scaffolding | PSD-95, SAP102 (PDZ); CaMKII; CKII (Ser1480) | F004, F006 |

### Localization summary

| Property | Finding |
|---|---|
| Tissue/cell enrichment | Forebrain; hippocampal CA pyramidal neurons; cortical pyramidal neurons layers II/III & V ([PMID: 9878886](https://pubmed.ncbi.nlm.nih.gov/9878886/)) |
| Primary subcellular site | Postsynaptic density of glutamatergic synapses |
| Secondary sites | Extrasynaptic plasma membrane; rare presynaptic |
| Membrane topology | Type I single-pass precursor; large extracellular ATD+LBD, re-entrant pore loop, intracellular CTD |

---

## Evidence Base

| PMID | Contribution | Finding(s) supported |
|---|---|---|
| [24876489](https://pubmed.ncbi.nlm.nih.gov/24876489/) | Crystal structure of intact GluN1–GluN2B heterotetramer; dimer-of-heterodimers, 3-layer architecture | F001 |
| [41278716](https://pubmed.ncbi.nlm.nih.gov/41278716/) | Co-agonist (glycine/D-serine) requirement; Ca²⁺/Mg²⁺ paradigm review | F002 |
| [20958962](https://pubmed.ncbi.nlm.nih.gov/20958962/) | Pore N/N+1 residues govern Ca²⁺ permeability and Mg²⁺ block | F002 |
| [22596351](https://pubmed.ncbi.nlm.nih.gov/22596351/) | Maps GluN2B-selective NAM binding to GluN1–GluN2B ATD interface | F003 |
| [37542648](https://pubmed.ncbi.nlm.nih.gov/37542648/) | Allosteric transduction from ifenprodil pocket via α5-helix to LBD | F003 |
| [15537897](https://pubmed.ncbi.nlm.nih.gov/15537897/) | Ser1480 phosphorylation disrupts PSD-95/SAP102 binding, lowers surface NR2B | F004 |
| [20427279](https://pubmed.ncbi.nlm.nih.gov/20427279/) | Dominant NR2B role in receptor recycling | F004 |
| [30355491](https://pubmed.ncbi.nlm.nih.gov/30355491/) | Developmental GluN2B→GluN2A switch driven by GluN2A levels | F005 |
| [10934236](https://pubmed.ncbi.nlm.nih.gov/10934236/) | Switch speeds EPSC decay, reduces ifenprodil sensitivity | F005 |
| [23839940](https://pubmed.ncbi.nlm.nih.gov/23839940/) | GluN2B dominates excitotoxicity and CREB/BDNF regulation | F006 |
| [10485705](https://pubmed.ncbi.nlm.nih.gov/10485705/) | NR2B overexpression enhances LTP and learning (Doogie mouse) | F007 |
| [21655294](https://pubmed.ncbi.nlm.nih.gov/21655294/) | PFC LTP enhancement is GluN2B-specific (Ro25-6981-sensitive) | F007 |
| [12574460](https://pubmed.ncbi.nlm.nih.gov/12574460/) | Fish/mouse conservation of agonist affinity and deactivation | F008 |
| [28760974](https://pubmed.ncbi.nlm.nih.gov/28760974/) | GluN2 = glutamate-binding, GluN1 = glycine-binding | F010 |
| [24462099](https://pubmed.ncbi.nlm.nih.gov/24462099/) | GluN2 identified as the L-glutamate-binding subunit | F010 |
| [40994429](https://pubmed.ncbi.nlm.nih.gov/40994429/) | De novo GRIN variants in ID/ASD/epilepsy; radiprodil inhibition | F009 |
| [40024627](https://pubmed.ncbi.nlm.nih.gov/40024627/) | Genotype–phenotype relation; spermidine rescues LoF | F009 |
| [39535073](https://pubmed.ncbi.nlm.nih.gov/39535073/) | Bidirectional (GoF/LoF) variant effects; ligand-distance predicts pathogenicity | F009 |
| [9878886](https://pubmed.ncbi.nlm.nih.gov/9878886/) | Ultrastructural postsynaptic/extrasynaptic/presynaptic localization; forebrain enrichment | F011 |

**Supporting but secondary literature.** Several additional papers reviewed reinforce specific themes: triheteromeric GluN1/GluN2A/GluN2B receptors and their partial ifenprodil sensitivity ([PMID: 28594440](https://pubmed.ncbi.nlm.nih.gov/28594440/)); NR3A association with NR1–NR2A/B in adult human CNS ([PMID: 17997397](https://pubmed.ncbi.nlm.nih.gov/17997397/)); precision-therapeutics framing of GRIN disorders ([PMID: 35110392](https://pubmed.ncbi.nlm.nih.gov/35110392/)); and the α2δ-1–NR2B interaction as a modulatory partner relevant to synaptic plasticity and depression models ([PMID: 41740819](https://pubmed.ncbi.nlm.nih.gov/41740819/)). Numerous rodent studies (e.g., [PMID: 12626441](https://pubmed.ncbi.nlm.nih.gov/12626441/), [PMID: 19306263](https://pubmed.ncbi.nlm.nih.gov/19306263/)) corroborate the developmental and plasticity roles but are high-throughput/correlative and were weighted below the primary structural, electrophysiological, and genetic evidence above.

---

## Limitations and Knowledge Gaps

1. **Rodent/non-human structural and localization data.** The gold-standard ultrastructural localization ([PMID: 9878886](https://pubmed.ncbi.nlm.nih.gov/9878886/)) and much electrophysiology derive from rat/mouse (and some teleost) tissue. Human GluN2B is highly conserved and the inferences are strong, but direct human ultrastructural localization data were not catalogued here.

2. **Triheteromeric receptors underexplored.** Native forebrain NMDARs are frequently GluN1/GluN2A/GluN2B triheteromers with intermediate kinetics and only partial GluN2B pharmacology ([PMID: 28594440](https://pubmed.ncbi.nlm.nih.gov/28594440/)). Much of the cited data derive from recombinant GluN1/GluN2B diheteromers; the precise in vivo stoichiometry-dependent behavior of GluN2B is incompletely resolved.

3. **CTD interactome breadth.** This report focused on PSD-95/SAP102 and CaMKII. The GluN2B CTD interacts with many additional partners (e.g., RasGRF1, SynGAP, DAPK1), which were not systematically surveyed and could refine the signaling model.

4. **Variant-level mechanism heterogeneity.** While the gain/loss dichotomy is established ([PMID: 39535073](https://pubmed.ncbi.nlm.nih.gov/39535073/)), the quantitative mapping of individual GRIN2B variants to channel biophysics (agonist potency, Mg²⁺ block, open probability, surface expression) remains an active, incomplete effort.

5. **No primary data analysis performed.** This investigation was literature- and database-driven (annotation task); no experimental datasets were analyzed, so all conclusions rest on published evidence rather than de novo statistics.

---

## Proposed Follow-up Experiments / Actions

1. **Human synaptic localization.** Apply expansion/immuno-EM or super-resolution microscopy to human cortical/hippocampal tissue to directly confirm the postsynaptic/extrasynaptic GluN2B distribution inferred from rodent EM ([PMID: 9878886](https://pubmed.ncbi.nlm.nih.gov/9878886/)).

2. **Systematic variant functionalization.** Build a saturation-mutagenesis / deep-mutational-scanning map of GRIN2B measuring glutamate EC₅₀, Mg²⁺ IC₅₀, Ca²⁺ permeability, open probability, and surface trafficking, to operationalize the ligand-distance pathogenicity predictor ([PMID: 39535073](https://pubmed.ncbi.nlm.nih.gov/39535073/)) for clinical variant interpretation.

3. **Precision pharmacology trials.** Match GluN2B-selective positive modulators (spermidine-class; [PMID: 40024627](https://pubmed.ncbi.nlm.nih.gov/40024627/)) to loss-of-function variants and negative modulators (radiprodil; [PMID: 40994429](https://pubmed.ncbi.nlm.nih.gov/40994429/)) to gain-of-function variants in patient-derived neurons, testing the "opposite therapeutics" hypothesis.

4. **Triheteromer-specific analysis.** Use fixed-stoichiometry tandem constructs to isolate GluN1/GluN2A/GluN2B triheteromer kinetics and pharmacology, clarifying GluN2B's contribution in the physiologically dominant native assembly.

5. **CTD interactome map in human neurons.** Proximity-labeling (BioID/TurboID) of the GluN2B CTD in human iPSC-derived neurons to comprehensively define the signaling scaffold and identify druggable synaptic vs. extrasynaptic signaling nodes relevant to the survival/excitotoxicity switch ([PMID: 23839940](https://pubmed.ncbi.nlm.nih.gov/23839940/)).

---

*Report compiled from 11 confirmed findings and 42 reviewed papers over 5 investigation iterations. All claims are attributed to verified primary structural, electrophysiological, genetic, and immunohistochemical literature.*


## Artifacts

- [OpenScientist final report](GRIN2B-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](GRIN2B-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:24876489
2. PMID:41278716
3. PMID:20958962
4. PMID:22596351
5. PMID:37542648
6. PMID:15537897
7. PMID:20427279
8. PMID:30355491
9. PMID:10934236
10. PMID:23839940
11. PMID:10485705
12. PMID:21655294
13. PMID:12574460
14. PMID:28760974
15. PMID:24462099
16. PMID:40994429
17. PMID:40024627
18. PMID:39535073
19. PMID:9878886
20. PMID:28594440
21. PMID:17997397
22. PMID:35110392
23. PMID:41740819
24. PMID:12626441
25. PMID:19306263