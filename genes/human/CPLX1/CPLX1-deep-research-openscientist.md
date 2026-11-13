---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-12T23:59:32.916916'
end_time: '2026-11-13T00:11:14.874307'
duration_seconds: 701.96
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: CPLX1
  gene_symbol: CPLX1
  uniprot_accession: O14810
  protein_description: 'RecName: Full=Complexin-1; AltName: Full=Complexin I; Short=CPX
    I; AltName: Full=Synaphin-2;'
  gene_info: Name=CPLX1;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the complexin/synaphin family. .
  protein_domains: Synaphin. (IPR008849); Synaphin (PF05835)
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
citation_count: 28
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: CPLX1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: CPLX1-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** O14810
- **Protein Description:** RecName: Full=Complexin-1; AltName: Full=Complexin I; Short=CPX I; AltName: Full=Synaphin-2;
- **Gene Information:** Name=CPLX1;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the complexin/synaphin family. .
- **Key Domains:** Synaphin. (IPR008849); Synaphin (PF05835)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CPLX1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CPLX1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CPLX1** (gene ID: CPLX1, UniProt: O14810) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# CPLX1 (Complexin-1, UniProt O14810): A Presynaptic SNARE-Complex Clamp and Activator of Ca²⁺-Triggered Neurotransmitter Release

## Gene/Protein Identity Verification

Before presenting findings, the target identity was explicitly verified against the UniProt record and the primary literature:

| Attribute | Value (verified) |
|-----------|------------------|
| **Gene symbol** | CPLX1 |
| **Protein** | Complexin-1 (Complexin I; CPX I; Synaphin-2) |
| **UniProt accession** | O14810 |
| **Organism** | *Homo sapiens* (Human) |
| **Length** | 134 amino acids |
| **Family** | Complexin/synaphin family |
| **Domain** | Synaphin (IPR008849 / PF05835) |
| **Class** | Cytosolic presynaptic regulatory protein (NOT an enzyme or transporter) |

The gene symbol, organism, protein family (complexin/synaphin), and the Synaphin domain all align consistently across the UniProt record and the primary neuroscience literature. The term "complexin" and the alternate name "synaphin" are used interchangeably in the literature, and papers using either name describe the same presynaptic SNARE-binding protein. **No ambiguity was encountered** — the literature is extensive and specific to this protein. This report proceeds with full confidence that CPLX1/Complexin-1 is correctly identified.

---

## Summary

**CPLX1 encodes Complexin-1, a small (~134-residue), soluble, neuron-enriched cytosolic protein that is not an enzyme or transporter but a regulatory adapter/clamp of the neuronal membrane-fusion machinery.** Its primary molecular function is to bind the assembled neuronal SNARE complex — the four-helix bundle formed by syntaxin-1, SNAP-25, and the vesicle protein VAMP2/synaptobrevin-2 — and thereby to control the timing of Ca²⁺-triggered synaptic vesicle fusion at the presynaptic terminal. Complexin-1 binds the SNARE bundle through a central α-helix that inserts in an antiparallel orientation into the groove between syntaxin and synaptobrevin (residues ~48–70 are the core interaction region), competing with α-SNAP for the same surface.

Complexin-1 performs a characteristic **dual function**. Through its accessory α-helix and intrinsically disordered, membrane-curvature-sensing C-terminal domain, it "**clamps**" partially assembled SNAREs into a cross-linked zig-zag topology that is geometrically incompatible with fusion — preventing premature or spontaneous vesicle release. Simultaneously, through its N-terminal domain, it "**activates**" fast, synchronous release by cooperating with the Ca²⁺ sensor synaptotagmin-1 so that, upon an action potential and Ca²⁺ influx, the clamp is released and fusion proceeds rapidly and in synchrony. This combination of fusion restraint plus facilitation is the functional signature that distinguishes complexin from other SNARE-regulatory proteins.

Spatially, Complexin-1 acts in the **cytosol at the presynaptic active zone and on synaptic vesicles**, where it is targeted by its C-terminal curvature-sensing domain. In human hippocampus and cerebellum it is preferentially associated with **inhibitory synapses** (whereas the paralog Complexin-2 predominates at excitatory synapses). It also contributes to **glucose-induced insulin secretion** by pancreatic β-cells, reflecting the conserved role of the SNARE/complexin machinery in regulated exocytosis beyond neurons. The physiological importance of the gene is underscored by human genetics: biallelic loss-of-function CPLX1 variants cause autosomal-recessive **developmental and epileptic encephalopathy 63 (DEE63)**, and Cplx1-knockout mice show the earliest-onset ataxia of any mouse model.

---

## Key Findings

### Finding 1 — Complexin-1 is a cytosolic presynaptic regulator that binds the assembled neuronal SNARE complex

Complexin-1 is a small (~134 aa) soluble neuronal protein of the complexin/synaphin family (UniProt O14810; Synaphin domain PF05835). It is not catalytic; its defining biochemical activity is high-affinity binding to the fully assembled ternary neuronal SNARE complex composed of syntaxin-1, SNAP-25, and VAMP2/synaptobrevin-2. Binding occurs through complexin's central α-helix, which inserts in an antiparallel orientation into the groove between the syntaxin and synaptobrevin helices of the four-helix SNARE bundle.

Importantly, complexin occupies a surface that overlaps with the binding site of α-SNAP, so the two proteins compete — a finding that first suggested complexin modulates the neurotransmitter-release process rather than catalyzing a reaction ([PMID: 10383625](https://pubmed.ncbi.nlm.nih.gov/10383625/)). The central α-helix is **necessary but not sufficient** for complexin's role in release: SNARE binding alone does not reproduce full function, implying that additional domains flanking the central helix carry out the regulatory work ([PMID: 17828276](https://pubmed.ncbi.nlm.nih.gov/17828276/)).

> "We show here that SNARE complex binding of complexin I (CplxI) via its central alpha-helix is necessary but, unexpectedly, not sufficient for its key function in promoting neurotransmitter release." ([PMID: 17828276](https://pubmed.ncbi.nlm.nih.gov/17828276/))

> "complexins compete with alpha-SNAP for binding to the complex, suggesting that complexins may modulate neurotransmitter release process" ([PMID: 10383625](https://pubmed.ncbi.nlm.nih.gov/10383625/))

### Finding 2 — Complexin has a dual clamp/activator function mediated by distinct, modular domains

Systematic domain dissection reveals that complexin-1 is organized into functionally separable modules arrayed around the central SNARE-binding helix:

| Domain | Approx. residues | Function |
|--------|------------------|----------|
| N-terminal domain (NTD) | 1–26/27 | Facilitates Ca²⁺-triggered (evoked) release |
| Accessory α-helix | ~27–48 | Inhibitory "clamp"; arrests SNARE zippering/assembly |
| Central α-helix | ~48–70 | Binds assembled SNARE complex (antiparallel) |
| C-terminal domain (CTD) | ~71–134 | Membrane-curvature sensing; clamps premature fusion |

The accessory α-helix (N-terminal to the central helix) inhibits fast synaptic exocytosis, while the sequences N-terminally adjacent to it facilitate Ca²⁺-triggered release — even in the absence of synaptotagmin-1 ([PMID: 17828276](https://pubmed.ncbi.nlm.nih.gov/17828276/)). Biophysically, the accessory helix arrests assembly of the SNARE complex ([PMID: 32698012](https://pubmed.ncbi.nlm.nih.gov/32698012/)), and it can locally displace the VAMP2 C-terminus in the quaternary complexin–SNARE assembly ([PMID: 20026076](https://pubmed.ncbi.nlm.nih.gov/20026076/)). The far C-terminal domain independently interferes with SNARE assembly to arrest tonic (spontaneous) exocytosis ([PMID: 30044227](https://pubmed.ncbi.nlm.nih.gov/30044227/)).

> "An accessory alpha-helix on the N-terminal side of the SNARE complex-binding region has an inhibitory effect on fast synaptic exocytosis, whereas sequences N-terminally adjacent to this helix facilitate Ca2+-triggered release even in the absence of the Ca2+ sensor synaptotagmin-1." ([PMID: 17828276](https://pubmed.ncbi.nlm.nih.gov/17828276/))

> "the accessory helix of complexin arrests assembly of the soluble N-ethylmaleimide-sensitive factor attachment protein receptor (SNARE) complex" ([PMID: 32698012](https://pubmed.ncbi.nlm.nih.gov/32698012/))

> "the far C-terminal domain (CTD) of CpxII interferes with SNARE assembly, thereby arresting tonic exocytosis" ([PMID: 30044227](https://pubmed.ncbi.nlm.nih.gov/30044227/))

### Finding 3 — Complexin-1 cooperates with synaptotagmin-1 and localizes to the active zone, preferentially at inhibitory synapses

Complexin-1 is a presynaptic cytosolic protein concentrated at the active zone. In human brain it is preferentially associated with **inhibitory synapses**, whereas Complexin-2 is associated with excitatory synapses ([PMID: 16814428](https://pubmed.ncbi.nlm.nih.gov/16814428/)). Functionally, the N-terminal domain of complexin specifically cooperates with **synaptotagmin-1** (but not synaptotagmin-VII) to enable synchronous fusion; the two proteins act synergistically as a fusion clamp that is released upon Ca²⁺ influx ([PMID: 39585326](https://pubmed.ncbi.nlm.nih.gov/39585326/), [PMID: 32401194](https://pubmed.ncbi.nlm.nih.gov/32401194/), [PMID: 42990368](https://pubmed.ncbi.nlm.nih.gov/42990368/)).

Native-synapse genetics confirm the dual role: at the mouse calyx of Held, Cplx1 ablation reduces both evoked and spontaneous release yet produces **excessive asynchronous release** after stimulation — exactly the phenotype expected if complexin both facilitates synchronous fusion and clamps premature fusion ([PMID: 26019341](https://pubmed.ncbi.nlm.nih.gov/26019341/)).

> "Complexin I is a presynaptic protein localised to inhibitory synapses." ([PMID: 16814428](https://pubmed.ncbi.nlm.nih.gov/16814428/))

> "the N-terminal domain (NTD) of CpxII (amino acids 1-27) specifically cooperates with synaptotagmin I (SytI), but not with synaptotagmin VII" ([PMID: 39585326](https://pubmed.ncbi.nlm.nih.gov/39585326/))

> "a developmentally exacerbating phenotype of reduced spontaneous and evoked transmission but excessive asynchronous release after stimulation, compatible with combined facilitating and clamping functions of Cplx1" ([PMID: 26019341](https://pubmed.ncbi.nlm.nih.gov/26019341/))

### Finding 4 — Structural basis: antiparallel central-helix binding and a primed tripartite complex with synaptotagmin-1

Crystallography and single-molecule FRET establish the structural mechanism. Complexin's central α-helix binds the SNARE core complex in an **antiparallel orientation via residues 48–70**, with the positively charged residues 71–77 also required for binding ([PMID: 17454299](https://pubmed.ncbi.nlm.nih.gov/17454299/), [PMID: 15821166](https://pubmed.ncbi.nlm.nih.gov/15821166/)). Crystal structures of the primed pre-fusion **SNARE–complexin–synaptotagmin-1** complex reveal an unexpected tripartite interface in which synaptotagmin-1 contacts both the SNARE complex and complexin, with a second synaptotagmin-1 at the "primary" interface; mutating either interface impairs evoked synchronous release ([PMID: 28813412](https://pubmed.ncbi.nlm.nih.gov/28813412/)).

A **conformational switch** in complexin — the accessory helix transitioning from an "open" to a "closed" state — is required for synaptotagmin-1/Ca²⁺ to trigger fusion; in the open state the accessory helix clamps a neighboring SNAREpin ([PMID: 21785412](https://pubmed.ncbi.nlm.nih.gov/21785412/)). An alternative model attributes accessory-helix inhibition to electrostatic/steric repulsion between the vesicle and plasma membranes rather than insertion into the SNARE complex ([PMID: 24842998](https://pubmed.ncbi.nlm.nih.gov/24842998/)), reflecting ongoing debate about the precise clamping geometry.

> "Here we determine crystal structures of the primed pre-fusion SNARE-complexin-synaptotagmin-1 complex. These structures reveal an unexpected tripartite interface between synaptotagmin-1 and both the SNARE complex and complexin." ([PMID: 28813412](https://pubmed.ncbi.nlm.nih.gov/28813412/))

> "complexin binds to SNARE core complex in an anti-parallel conformation with its residues 48 - 70" ([PMID: 17454299](https://pubmed.ncbi.nlm.nih.gov/17454299/))

> "the conformational switch from open to closed in complexin is needed for synaptotagmin-Ca(2+) to trigger fusion" ([PMID: 21785412](https://pubmed.ncbi.nlm.nih.gov/21785412/))

### Finding 5 — The disordered C-terminal domain senses membrane curvature and targets complexin to synaptic vesicles for its clamp function

The complexin C-terminal domain (CTD) is intrinsically disordered and binds membranes through tandem motifs, including a curvature-sensing amphipathic helix that folds only on highly curved surfaces (sensing lipid-packing defects on small, high-curvature synaptic vesicles) ([PMID: 25229806](https://pubmed.ncbi.nlm.nih.gov/25229806/), [PMID: 28596722](https://pubmed.ncbi.nlm.nih.gov/28596722/)). Mutations that block helix formation without disrupting membrane binding selectively compromise complexin's inhibitory (clamp) function *in vivo*, directly linking the curvature-dependent conformational change to clamping ([PMID: 25229806](https://pubmed.ncbi.nlm.nih.gov/25229806/)).

The CTD thus serves a dual purpose: it **localizes** complexin to synaptic vesicles, giving it effective access to assembling SNAREs ([PMID: 40321081](https://pubmed.ncbi.nlm.nih.gov/40321081/), [PMID: 35931110](https://pubmed.ncbi.nlm.nih.gov/35931110/)), and it adopts distinct membrane-bound structural signatures that modulate inhibitory function ([PMID: 35777466](https://pubmed.ncbi.nlm.nih.gov/35777466/)).

> "complexin's CTD is highly sensitive to membrane curvature, which it senses via tandem motifs" ([PMID: 25229806](https://pubmed.ncbi.nlm.nih.gov/25229806/))

> "Mutations that disrupt helix formation without disrupting membrane binding compromise complexin's inhibitory function in vivo" ([PMID: 25229806](https://pubmed.ncbi.nlm.nih.gov/25229806/))

> "Complexin gains effective access to the assembling SNAREs via its membrane-binding C-terminal domain" ([PMID: 40321081](https://pubmed.ncbi.nlm.nih.gov/40321081/))

### Finding 6 — Biallelic loss-of-function CPLX1 variants cause human developmental and epileptic encephalopathy (DEE63)

Human genetics confirm that CPLX1 is essential for normal brain function. Homozygous CPLX1 variants were identified in patients from unrelated families presenting with intellectual disability, marked developmental delay, and severe/migrating infantile myoclonic epilepsy (one with a cerebellar cleft); a homozygous truncating variant causes migrating epilepsy with structural brain abnormalities ([PMID: 28422131](https://pubmed.ncbi.nlm.nih.gov/28422131/)). A homozygous CPLX1 mutation underlies a Dravet-syndrome presentation modeled with patient iPSC lines ([PMID: 38110787](https://pubmed.ncbi.nlm.nih.gov/38110787/)). CPLX1 lies within the Wolf-Hirschhorn syndrome seizure-susceptibility region (4p16.3) and is implicated in WHS-related seizures ([PMID: 35278209](https://pubmed.ncbi.nlm.nih.gov/35278209/)). In mice, homozygous Cplx1 knockout produces the earliest-onset ataxia of any known mouse model ([PMID: 28422131](https://pubmed.ncbi.nlm.nih.gov/28422131/)).

> "All displayed marked developmental delay and migrating myoclonic epilepsy, and one showed a cerebellar cleft in addition." ([PMID: 28422131](https://pubmed.ncbi.nlm.nih.gov/28422131/))

> "homozygous Cplx1 knockout mice have the earliest known onset of ataxia seen in a mouse model" ([PMID: 28422131](https://pubmed.ncbi.nlm.nih.gov/28422131/))

### Finding 7 — Single-molecule force measurements confirm complexin-1 as a SNARE-assembly chaperone with domain-segregated functions

Dual-trap optical-tweezers experiments on single SNARE complexes under mechanical force reconstituted both complexin-1 functions directly: the **N-terminal domain dominates facilitation** (promoting SNARE assembly) while the **C-terminal domain mediates clamping** (inhibiting assembly). A mixture of CpxI(1-83) plus the isolated CTD reproduces full-length inhibition, demonstrating that complexin-1 acts as a chaperone controlling the dynamic folding of the SNARE complex ([PMID: 36750663](https://pubmed.ncbi.nlm.nih.gov/36750663/)). This is consistent with the biochemical mapping in which the CTD amphipathic helix hydrophobic face binds fusion-promoting SNAREs to arrest the pre-fusion intermediate while the NTD cooperates with synaptotagmin-1 for synchronous fusion ([PMID: 39585326](https://pubmed.ncbi.nlm.nih.gov/39585326/)).

> "while the N-terminal domain (NTD) plays a dominant role of the facilitate function, CTD is mainly related to clamping" ([PMID: 36750663](https://pubmed.ncbi.nlm.nih.gov/36750663/))

> "Our observation identifies the important chaperone role of the CpxI molecule in the dynamic assembly of SNARE complex under mechanical tension" ([PMID: 36750663](https://pubmed.ncbi.nlm.nih.gov/36750663/))

### Finding 8 — UniProt-verified architecture and annotations (O14810)

The UniProt record for O14810, retrieved programmatically, confirms the picture built from the primary literature: a 134-residue protein; a defined "Interaction with the SNARE complex" region at residues 48–70 with a central coiled-coil/helix (~29–70); disordered N-terminal (1–60) and C-terminal (74–113) regions; and a basic-and-acidic compositional bias (15–60). The annotated function states that complexin-1 "organizes the SNAREs into a cross-linked zigzag topology that, when interposed between the vesicle and plasma membranes, is incompatible with fusion, thereby preventing SNAREs from releasing neurotransmitters until an action potential arrives" (based on [PMID: 21785414](https://pubmed.ncbi.nlm.nih.gov/21785414/)). It is additionally "involved in glucose-induced secretion of insulin by pancreatic beta-cells."

Subcellular location is annotated as Cytoplasm/cytosol, Perikaryon, and Presynapse, enriched at synaptic releasing sites. Tissue specificity is the nervous system; in hippocampus and cerebellum it is expressed mainly by inhibitory neurons, and it is overexpressed in Parkinson-disease substantia nigra. Natural variants (residues 105–134, 108–134, and 128) are annotated as causing DEE63. Keywords include Exocytosis, Neurotransmitter transport, Synapse, Cytoplasm, Coiled coil, and Epilepsy.

---

## Mechanistic Model / Interpretation

Complexin-1 is best understood as a **molecular timer and safety catch** acting on the SNARE fusion machine. The neuronal SNARE proteins (syntaxin-1 and SNAP-25 on the plasma membrane; VAMP2 on the vesicle) progressively "zipper" from their N- to C-termini, drawing the two membranes together and ultimately driving fusion. Complexin-1 intercepts this process at a partially zippered, pre-fusion stage.

```
        SYNAPTIC VESICLE (high curvature)
   ┌───────────────────────────────────────┐
   │   VAMP2        Complexin-1 CTD ────────┼── curvature-sensing
   │     \          (amphipathic helix)     │    amphipathic helix
   │      \                                 │    folds on vesicle
   │   ┌───╫───────────────┐  accessory     │
   │   │ 4-helix SNARE     │  helix clamps  │
   │   │ bundle (zippering)│  C-term zipper │
   │   └───╫───────────────┘                │
   │      /   central helix (aa 48-70)      │
   │     /    binds antiparallel            │
   │  SNAP-25 / Syntaxin-1                  │
   └───────────────────────────────────────┘
        PLASMA MEMBRANE / ACTIVE ZONE

   N-terminal domain (aa 1-26) -- cooperates with Synaptotagmin-1
                                  -> ACTIVATES fast evoked fusion

   -- Resting state: zig-zag cross-linked SNAREs = CLAMPED (no fusion)
   -- Ca2+ influx -> Synaptotagmin-1 engages -> conformational switch
      (accessory helix open->closed) -> clamp released -> FAST FUSION
```

The **clamp** arises from two cooperating elements. The accessory α-helix competes with the VAMP2 C-terminus, locally displacing it and arresting further zippering, holding the SNAREs in a fusion-incompatible "zig-zag" topology. The intrinsically disordered CTD reinforces this by binding the highly curved synaptic-vesicle membrane via its curvature-sensing amphipathic helix, both **localizing** complexin to vesicles and contributing an independent arrest of spontaneous (tonic) fusion. This explains why loss of complexin unleashes excessive spontaneous and asynchronous release.

The **activator** function resides in the N-terminal domain, which cooperates specifically with synaptotagmin-1. The crystallographic "primed" tripartite SNARE–complexin–synaptotagmin-1 complex shows how these components are pre-organized so that Ca²⁺ binding to synaptotagmin-1 can act rapidly. Ca²⁺ influx drives a conformational switch in complexin (accessory helix open→closed) that releases the clamp and permits synchronous completion of zippering and fusion. Complexin therefore couples **restraint** (preventing wasteful or mistimed release) with **readiness** (poising vesicles for instantaneous, synchronous release), which is precisely the control required for high-fidelity synaptic transmission.

Single-molecule optical-tweezers experiments crystallize this model into a clean domain map: the NTD facilitates assembly, the CTD clamps, and complexin-1 overall behaves as a **chaperone of SNARE folding**. The preferential localization of Complexin-1 to inhibitory synapses in human hippocampus and cerebellum, combined with the severe epileptic phenotype of loss-of-function, suggests that in humans a major physiological role is to guarantee properly timed inhibitory neurotransmission — failure of which produces the excitatory/inhibitory imbalance that manifests as epileptic encephalopathy and ataxia.

Beyond neurons, the same machinery operates in pancreatic β-cells, where complexin-1 participates in glucose-induced insulin secretion — a reminder that complexin is a general regulator of **regulated, Ca²⁺-triggered exocytosis**, not a neuron-exclusive factor.

---

## Evidence Base

| PMID | Topic | How it supports the model |
|------|-------|---------------------------|
| [10383625](https://pubmed.ncbi.nlm.nih.gov/10383625/) | Complexin vs α-SNAP | SNARE-complex binding; competition with α-SNAP |
| [17828276](https://pubmed.ncbi.nlm.nih.gov/17828276/) | Domains of complexin I | Central helix necessary-not-sufficient; accessory inhibits, NTD facilitates |
| [20026076](https://pubmed.ncbi.nlm.nih.gov/20026076/) | Accessory helix EPR | Accessory helix displaces VAMP2 C-terminus (clamp mechanism) |
| [32698012](https://pubmed.ncbi.nlm.nih.gov/32698012/) | Capturing VAMP2/SNAP25 | Accessory helix arrests SNARE assembly |
| [30044227](https://pubmed.ncbi.nlm.nih.gov/30044227/) | C-terminus arrest | CTD interferes with SNARE assembly, arrests tonic exocytosis |
| [16814428](https://pubmed.ncbi.nlm.nih.gov/16814428/) | Synaptic proteins | Complexin I localized to inhibitory synapses |
| [39585326](https://pubmed.ncbi.nlm.nih.gov/39585326/) | Dual clamp/activator | NTD cooperates with synaptotagmin-1; CTD clamps |
| [32401194](https://pubmed.ncbi.nlm.nih.gov/32401194/) | Synergistic Syt1 + Cpx | Synergistic fusion clamp |
| [42990368](https://pubmed.ncbi.nlm.nih.gov/42990368/) | Evolutionary tuning | Conserved complexin–synaptotagmin fusion clamp |
| [26019341](https://pubmed.ncbi.nlm.nih.gov/26019341/) | Calyx of Held | Native-synapse dual facilitation + clamping phenotype |
| [28813412](https://pubmed.ncbi.nlm.nih.gov/28813412/) | Primed complex | Crystal structure of SNARE–complexin–Syt1 tripartite complex |
| [17454299](https://pubmed.ncbi.nlm.nih.gov/17454299/) | Residues 71–77 | Antiparallel central-helix binding (48–70); 71–77 required |
| [15821166](https://pubmed.ncbi.nlm.nih.gov/15821166/) | Single-molecule FRET | Structural/kinetic validation of complexin–SNARE binding |
| [21785412](https://pubmed.ncbi.nlm.nih.gov/21785412/) | Conformational switch | Open→closed switch gates Syt1/Ca²⁺ triggering |
| [24842998](https://pubmed.ncbi.nlm.nih.gov/24842998/) | Re-examining inhibition | Alternative electrostatic/steric clamp model (challenges insertion model) |
| [25229806](https://pubmed.ncbi.nlm.nih.gov/25229806/) | Curvature sensing | CTD senses curvature; curvature-dependent clamp |
| [28596722](https://pubmed.ncbi.nlm.nih.gov/28596722/) | CTD motifs | Amphipathic motif required for inhibition |
| [35777466](https://pubmed.ncbi.nlm.nih.gov/35777466/) | Membrane-bound CTD | Distinct membrane-bound CTD structures |
| [40321081](https://pubmed.ncbi.nlm.nih.gov/40321081/) | CTD access | CTD provides access/localization to assembling SNAREs |
| [35931110](https://pubmed.ncbi.nlm.nih.gov/35931110/) | Membrane interactions | CTD role in localization and synapse evolution |
| [36750663](https://pubmed.ncbi.nlm.nih.gov/36750663/) | Optical tweezers | NTD facilitates, CTD clamps; complexin is a SNARE chaperone |
| [28422131](https://pubmed.ncbi.nlm.nih.gov/28422131/) | CPLX1 variants | Human DEE63; mouse early-onset ataxia |
| [38110787](https://pubmed.ncbi.nlm.nih.gov/38110787/) | Dravet iPSC | Homozygous CPLX1 mutation, Dravet phenotype |
| [35278209](https://pubmed.ncbi.nlm.nih.gov/35278209/) | Wolf-Hirschhorn | CPLX1 in 4p16.3 seizure-susceptibility region |

**Points of consensus:** The central-helix antiparallel binding mode, the modular dual clamp/activator architecture, the NTD–synaptotagmin-1 cooperation, the CTD curvature-sensing clamp, and the human DEE63 phenotype are all supported by multiple independent structural, biophysical, genetic, and single-molecule studies.

**Points of ongoing debate:** The precise molecular geometry of the accessory-helix clamp remains contested — the "insertion" model ([PMID: 21785412](https://pubmed.ncbi.nlm.nih.gov/21785412/)) versus an "electrostatic/steric repulsion" model ([PMID: 24842998](https://pubmed.ncbi.nlm.nih.gov/24842998/)). Related isothermal titration calorimetry work ([PMID: 28880148](https://pubmed.ncbi.nlm.nih.gov/28880148/)) and reviews on the difficulty of measuring these weak interactions ([PMID: 35986639](https://pubmed.ncbi.nlm.nih.gov/35986639/)) emphasize that the clamping interface is a genuinely weak, transient interaction, which accounts for discrepancies across laboratories. There is also species-level variation in complexin/synaptotagmin behavior that reflects tuning of a conserved mechanism rather than fundamentally different roles ([PMID: 42990368](https://pubmed.ncbi.nlm.nih.gov/42990368/)).

---

## Limitations and Knowledge Gaps

1. **Clamp geometry unresolved.** Whether the accessory helix physically inserts into/near the SNARE bundle or acts primarily through membrane-level electrostatic/steric repulsion remains unsettled. The interactions involved are weak and transient, making them technically difficult to measure, and different laboratories have reported discrepant ITC results.

2. **Human-specific data are limited.** Much mechanistic detail derives from mouse (CpxI/II), *Drosophila*, and *C. elegans* complexins, or from reconstituted systems. Human CPLX1-specific structural and electrophysiological data are sparser, though the high sequence conservation and human genetics support extrapolation.

3. **Paralog division of labor.** Humans express four complexins (CPLX1–4). The precise functional distinctions — e.g., why Complexin-1 prefers inhibitory synapses while Complexin-2 prefers excitatory synapses, and the lipid-anchored behavior of Complexin-3/4 — are not fully explained at the mechanistic level for the human proteins.

4. **Insulin-secretion role is thinly characterized.** The β-cell/insulin-secretion function is annotated but mechanistically underexplored relative to the neuronal role.

5. **Post-translational regulation.** Complexin is subject to regulation such as S-nitrosylation and farnesylation that modulates its clamping ability ([PMID: 29630591](https://pubmed.ncbi.nlm.nih.gov/29630591/)), but the physiological scope of these modifications on human CPLX1 specifically is not established.

6. **Genotype–phenotype correlation in DEE63** is based on a small number of families; the full variant spectrum and mechanism (loss of clamp vs. loss of activation) are not comprehensively mapped.

---

## Proposed Follow-up Experiments / Actions

1. **Resolve the clamp geometry with human CPLX1.** Use cryo-EM or integrative structural biology on reconstituted human SNARE–CPLX1–synaptotagmin-1 assemblies on membrane templates of defined curvature to directly visualize the accessory helix relative to the SNARE bundle and the two membranes, discriminating the insertion vs. repulsion models.

2. **Patient iPSC-derived neuron electrophysiology.** Use DEE63 patient-derived iPSC neurons ([PMID: 38110787](https://pubmed.ncbi.nlm.nih.gov/38110787/)) to quantify spontaneous vs. evoked release, asynchronous release, and inhibitory/excitatory balance, correlating specific CTD-truncating variants (105–134, 108–134, 128) with loss of clamp vs. loss of activation.

3. **Structure-guided variant mapping.** Introduce each annotated DEE63 variant into reconstituted single-molecule optical-tweezers assays ([PMID: 36750663](https://pubmed.ncbi.nlm.nih.gov/36750663/)) to assign each to the facilitation (NTD) or clamping (CTD) axis.

4. **Dissect the β-cell role.** Knock down/out CPLX1 in human β-cell models and measure glucose-stimulated insulin secretion kinetics to define whether the clamp/activator duality operates identically in endocrine exocytosis.

5. **Map paralog-specific synapse targeting.** Use synapse-type-resolved proteomics/imaging in human tissue to determine the molecular determinants that route Complexin-1 to inhibitory synapses versus Complexin-2 to excitatory synapses.

6. **Characterize PTM regulation in human neurons.** Test whether S-nitrosylation/farnesylation ([PMID: 29630591](https://pubmed.ncbi.nlm.nih.gov/29630591/)) tunes human CPLX1 clamping in an activity-dependent manner.

---

## Conclusion

CPLX1/Complexin-1 is a small cytosolic presynaptic adapter — not an enzyme or transporter — whose primary function is to bind the assembled neuronal SNARE complex and govern the timing of Ca²⁺-triggered synaptic vesicle fusion. It simultaneously **clamps** premature/spontaneous fusion (via its accessory helix and membrane-curvature-sensing C-terminal domain, organizing SNAREs into a fusion-incompatible zig-zag topology) and **activates** fast synchronous release (via its N-terminal cooperation with synaptotagmin-1). It functions in the cytosol at the presynaptic active zone and on synaptic vesicles, preferentially at inhibitory synapses in human hippocampus and cerebellum, and additionally supports glucose-induced insulin secretion. Biallelic loss of function causes human developmental and epileptic encephalopathy (DEE63), confirming that this timing-control function is essential for normal neural circuit operation.


## Artifacts

- [OpenScientist final report](CPLX1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](CPLX1-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10383625
2. PMID:17828276
3. PMID:32698012
4. PMID:20026076
5. PMID:30044227
6. PMID:16814428
7. PMID:39585326
8. PMID:32401194
9. PMID:42990368
10. PMID:26019341
11. PMID:17454299
12. PMID:15821166
13. PMID:28813412
14. PMID:21785412
15. PMID:24842998
16. PMID:25229806
17. PMID:28596722
18. PMID:40321081
19. PMID:35931110
20. PMID:35777466
21. PMID:28422131
22. PMID:38110787
23. PMID:35278209
24. PMID:36750663
25. PMID:21785414
26. PMID:28880148
27. PMID:35986639
28. PMID:29630591