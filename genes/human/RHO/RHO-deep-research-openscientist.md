---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-13T01:24:04.159576'
end_time: '2026-11-13T01:36:18.883098'
duration_seconds: 734.72
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: RHO
  gene_symbol: RHO
  uniprot_accession: P08100
  protein_description: 'RecName: Full=Rhodopsin {ECO:0000303|PubMed:6589631}; AltName:
    Full=Opsin-2;'
  gene_info: Name=RHO {ECO:0000312|HGNC:HGNC:10012}; Synonyms=OPN2;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the G protein-coupled receptor 1 family. Opsin
  protein_domains: GPCR_opsins. (IPR050125); GPCR_Rhodpsn. (IPR000276); GPCR_Rhodpsn_7TM.
    (IPR017452); Opsin. (IPR001760); Retinal_BS. (IPR027430)
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
citation_count: 27
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: RHO-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: RHO-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P08100
- **Protein Description:** RecName: Full=Rhodopsin {ECO:0000303|PubMed:6589631}; AltName: Full=Opsin-2;
- **Gene Information:** Name=RHO {ECO:0000312|HGNC:HGNC:10012}; Synonyms=OPN2;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the G protein-coupled receptor 1 family. Opsin
- **Key Domains:** GPCR_opsins. (IPR050125); GPCR_Rhodpsn. (IPR000276); GPCR_Rhodpsn_7TM. (IPR017452); Opsin. (IPR001760); Retinal_BS. (IPR027430)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "RHO" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'RHO' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **RHO** (gene ID: RHO, UniProt: P08100) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of Human RHO (Rhodopsin, UniProt P08100)

## Summary

**RHO (UniProt P08100) encodes human rhodopsin, the archetypal light-activated class-A (rhodopsin-family) G protein-coupled receptor (GPCR) and the molecular light sensor of scotopic (dim-light) vision.** The gene symbol RHO (synonym OPN2) maps unambiguously to the human opsin-2 protein, a seven-transmembrane GPCR of the opsin subfamily bearing the diagnostic GPCR_Rhodpsn_7TM (IPR017452), Opsin (IPR001760) and Retinal binding site (IPR027430) domains. Literature converges on a single, well-characterised identity: rhodopsin is the light receptor of rod photoreceptors that initiates the phototransduction cascade. The identity verification required by the task is fully satisfied — all evidence describes human/vertebrate rhodopsin, not an unrelated gene of the same symbol (e.g. the GTPase RhoA, which has a distinct HGNC symbol RHOA).

**Primary function.** Rhodopsin is not an enzyme in the classical sense but a light-regulated catalytic receptor. It carries a covalently bound chromophore, **11-cis-retinal**, attached to Lys296 through a protonated Schiff base and locked in place by an electrostatic salt bridge to the Glu113 counterion. In this dark state the 11-cis-retinal behaves as an **inverse agonist**, holding the transmembrane bundle in its inactive conformation and endowing the receptor with extraordinary thermal stability — the physical basis of the rod's ability to detect single photons against negligible dark noise. Absorption of a photon isomerises 11-cis-retinal to all-trans-retinal with ~70% quantum efficiency, driving a cascade of conformational intermediates that culminates in the active signalling state **metarhodopsin II (MII / R\*)**. R\* functions as a **guanine-nucleotide exchange factor (GEF)** that catalyses GDP→GTP exchange on the rod G protein **transducin (Gt)**, launching the cGMP phototransduction cascade (transducin → PDE6 → cGMP hydrolysis → closure of CNG channels → membrane hyperpolarisation).

**Localisation and lifecycle.** Rhodopsin is abundantly and specifically expressed in rod photoreceptors, where it resides in the stacked disc membranes of the rod outer segment (ROS), a modified sensory cilium. Beyond signalling, rhodopsin plays a **structural role** in ROS disc growth and morphogenesis, and its trafficking through the connecting cilium is essential for outer-segment biogenesis. Signalling is terminated by a two-step shutoff — GRK1 (rhodopsin kinase) phosphorylation of the C-terminus followed by arrestin-1 capping — and the bleached chromophore is regenerated through the **RPE65-driven retinoid (visual) cycle**. Mutations in RHO are a leading cause of inherited retinal degeneration: misfolding alleles (e.g. P23H) cause autosomal dominant retinitis pigmentosa through ER retention and aggregation, whereas counterion-disrupting alleles (G90D, A292E, T94I) cause congenital stationary night blindness by constitutively activating transducin.

---

## Key Findings

### Finding 1 — RHO/P08100 is confirmed as human rhodopsin, the prototypical class-A GPCR

The target identity is secure on every axis required by the task. The gene symbol **RHO** (synonym **OPN2**), organism *Homo sapiens*, G protein-coupled receptor 1 (opsin) family membership, and the domain architecture (GPCR_Rhodpsn_7TM IPR017452; Opsin IPR001760; Retinal binding site IPR027430) all match the literature description of rhodopsin. Reviews describe it precisely as "a G protein-coupled receptor (GPCR) present in the rod outer segment (ROS) of photoreceptor cells that initiates the phototransduction cascade required for scotopic vision" [PMID: 37265335](https://pubmed.ncbi.nlm.nih.gov/37265335/), and as the light sensor of vertebrate scotopic vision. The historical importance of this molecule is hard to overstate: the first atomic structure of any GPCR was bovine rhodopsin, solved at 2.8 Å — "We determined the structure of rhodopsin from diffraction data extending to 2.8 angstroms resolution" [PMID: 10926528](https://pubmed.ncbi.nlm.nih.gov/10926528/). There is no ambiguity and no evidence of a confounding same-symbol gene; all retrieved literature concerns vertebrate visual rhodopsin.

### Finding 2 — Primary function: a light-activated GPCR using 11-cis-retinal as a covalently bound inverse-agonist chromophore

Rhodopsin's defining feature is its built-in ligand. **11-cis-retinal is covalently bound to Lys296 via a protonated Schiff base**, with the positive charge stabilised by the carboxylate of **Glu113**, which serves as the counterion [PMID: 8068654](https://pubmed.ncbi.nlm.nih.gov/8068654/) [PMID: 8608127](https://pubmed.ncbi.nlm.nih.gov/8608127/). In the dark, "the ground-state chromophore, 11-cis-retinal, holds the transmembrane region of the protein in the inactive conformation" [PMID: 10926528](https://pubmed.ncbi.nlm.nih.gov/10926528/) — i.e. the chromophore acts as a tethered inverse agonist, not merely a passive cofactor. Photon capture triggers 11-cis→all-trans photoisomerisation; "its chromophore isomerises upon photon absorption with 70% efficiency, enabling the activation of its G-protein, transducin, with high efficiency" [PMID: 36273969](https://pubmed.ncbi.nlm.nih.gov/36273969/). Energy is stored in sub-picosecond retinal–protein interactions and released through thermal relaxation across a series of spectrally distinct intermediates, ending in deprotonation of the Schiff base and formation of **metarhodopsin II (MII, λmax = 380 nm), the active state (R\*)** [PMID: 8068654](https://pubmed.ncbi.nlm.nih.gov/8068654/). The substrate, in enzymatic terms, is a **photon plus the isomerisation of its own chromophore**; the product is the activated receptor conformation.

### Finding 3 — Signalling role: active MII catalyses GDP/GTP exchange on transducin, triggering the cGMP cascade

In its active state rhodopsin is a catalyst. R\*/MII "catalyzes guanine nucleotide exchange in transducin, the G protein of the photoreceptor cell" [PMID: 8068654](https://pubmed.ncbi.nlm.nih.gov/8068654/) — acting as a GEF. A single activated rhodopsin molecule generates a measurable electrical response, because it catalytically activates many transducins before being shut off, providing the first stage of amplification in vision. The canonical pathway proceeds:

> R\* → activates transducin α-subunit (Gtα, GDP→GTP) → Gtα·GTP stimulates phosphodiesterase 6 (PDE6) → PDE6 hydrolyses cGMP → cytoplasmic cGMP falls → cGMP-gated (CNG) channels close → rod membrane hyperpolarises.

Cryo-electron tomography of the rod outer segment places rhodopsin, PDE6 and the guanylate cyclases within the disc architecture that organises this cascade [PMID: 36163145](https://pubmed.ncbi.nlm.nih.gov/36163145/). Rhodopsin is therefore best described as a **light-gated catalytic GEF amplifier** sitting at the apex of the phototransduction cascade.

### Finding 4 — Deactivation: C-terminal phosphorylation by GRK1 followed by arrestin-1 binding quenches signalling

Timely shutoff is essential for temporal resolution and recovery. Deactivation is a **two-step process**: removal of rhodopsin's carboxy-terminal phosphorylation sites prolonged the single-rod flash response roughly 20-fold and made it highly variable, while in arrestin-null rods final recovery was slowed more than 100-fold, demonstrating that "phosphorylation initiates rhodopsin deactivation and that arrestin binding completes the process" [PMID: 9775212](https://pubmed.ncbi.nlm.nih.gov/9775212/). The responsible kinase is **GRK1 (rhodopsin kinase)**, "a specialized G-protein-coupled receptor kinase expressed in retina… involved in quenching of light-induced signal transduction in photoreceptors"; null mutations in GRK1 cause **Oguchi disease**, with abnormal recovery kinetics but normal photoactivation [PMID: 9419375](https://pubmed.ncbi.nlm.nih.gov/9419375/). **Arrestin-1** specifically recognises the phosphorylated, photoactivated receptor and sterically blocks further transducin coupling, with the activated arrestin-1 monomer being the rhodopsin-binding species [PMID: 39880147](https://pubmed.ncbi.nlm.nih.gov/39880147/).

### Finding 5 — Localisation: rod outer-segment disc membranes; misfolding mutants are ER-retained and cause adRP

Rhodopsin is "specifically and abundantly expressed in rod photoreceptors" [PMID: 37440077](https://pubmed.ncbi.nlm.nih.gov/37440077/) and localises to **ROS disc membranes**, where phototransduction occurs [PMID: 37265335](https://pubmed.ncbi.nlm.nih.gov/37265335/). It is a multi-pass integral membrane protein — its functional compartment is the lipid bilayer of the disc. Over 150 RHO mutations cause **autosomal dominant retinitis pigmentosa (adRP)**; the most common U.S. allele, **P23H**, is misfolded, ubiquitinylated and rapidly degraded [PMID: 37440077](https://pubmed.ncbi.nlm.nih.gov/37440077/). In a P23H–RFP knock-in mouse, "outer segments formed, and wild-type (WT) rhodopsin was properly localized, but mutant P23H-Rho protein was mislocalized in the inner segments" and retained in expanded ER membranes [PMID: 35275162](https://pubmed.ncbi.nlm.nih.gov/35275162/). A broader survey of misfolding mutants (P23H, G188R, Y178C) showed ER mislocalisation and aggregation, with aggregation severity tracking the rate of retinal degeneration [PMID: 38365903](https://pubmed.ncbi.nlm.nih.gov/38365903/) [PMID: 39875362](https://pubmed.ncbi.nlm.nih.gov/39875362/). Thus correct localisation is both diagnostic of normal function and central to disease.

### Finding 6 — Chromophore supply: rhodopsin depends on the RPE65-driven retinoid (visual) cycle

Rhodopsin cannot function without continuous resupply of its chromophore. "In all known visual systems, the chromophore is 11-cis-retinal complexed with a protein, called opsin, and photoisomerization produces all-trans-retinal" [PMID: 27830507](https://pubmed.ncbi.nlm.nih.gov/27830507/). After bleaching, "with metarhodopsin II decay, all-trans-retinal is released, and opsin is reloaded with new 11-cis-retinal" [PMID: 18563085](https://pubmed.ncbi.nlm.nih.gov/18563085/). Regeneration of 11-cis-retinal occurs enzymatically in the retinal pigment epithelium via the **isomerohydrolase RPE65**; human RPE65 mutations cause **Leber congenital amaurosis** [PMID: 41135835](https://pubmed.ncbi.nlm.nih.gov/41135835/), and metabolic disruption of RPE65 (e.g. via PKM2 loss) impairs 11-cis-retinal regeneration and the visual cycle [PMID: 42321202](https://pubmed.ncbi.nlm.nih.gov/42321202/). Rhodopsin function is therefore embedded in a two-cell (photoreceptor/RPE) metabolic loop.

### Finding 7 — Structural activation mechanism: conserved E(D)RY and NPxxY microswitches and outward TM6 movement

How does chromophore isomerisation become a G-protein-coupling signal? The ligand-free **opsin** crystal structure (2.9 Å) captured the active-state rearrangements: relative to dark rhodopsin, opsin "shows prominent structural changes in the conserved E(D)RY and NPxxY(x)5,6F regions and in TM5-TM7. At the cytoplasmic side, TM6 is tilted outwards by 6-7 Å, whereas the helix structure of TM5 is more elongated and close to TM6" [PMID: 18563085](https://pubmed.ncbi.nlm.nih.gov/18563085/). These are the canonical **class-A GPCR activation microswitches**; the outward swing of TM6 opens the cytoplasmic cavity that receives the transducin C-terminal helix. The original rhodopsin structure had already identified "a set of residues that mediate interactions between the transmembrane helices and the cytoplasmic surface, where G-protein activation occurs" [PMID: 10926528](https://pubmed.ncbi.nlm.nih.gov/10926528/). Rhodopsin thus serves as the structural template for understanding activation across the entire class-A GPCR superfamily.

### Finding 8 — Extreme dark stability underlies single-photon detection

The rod's ability to signal single photons depends on rhodopsin almost never activating by accident. Single rod-outer-segment recordings revealed rare discrete dark events whose "amplitude and power spectrum… resembled those of single photon effects in the same rod, suggesting that discrete events may arise from spontaneous activation of single rhodopsin molecules," occurring at roughly 1 event per 50 s at 20 °C [PMID: 6788941](https://pubmed.ncbi.nlm.nih.gov/6788941/). The temperature dependence gave "an activation energy of 22 kcal mole-1, probably characteristic of thermal isomerization of rhodopsin" [PMID: 6788941](https://pubmed.ncbi.nlm.nih.gov/6788941/). Mechanistically, the thermal (dark) activation barrier (~80–110 kJ/mol) is roughly half the light-activation barrier (≥180 kJ/mol), implying distinct pathways; infrared/HDX work suggests dark activation is gated by transient structural fluctuations of the retinal-binding pocket rather than of the chromophore itself [PMID: 20356096](https://pubmed.ncbi.nlm.nih.gov/20356096/). The covalently locked, counterion-stabilised 11-cis-retinal is what keeps spontaneous activation vanishingly rare.

### Finding 9 — A structural role in rod outer-segment disc growth and morphogenesis

Rhodopsin is bifunctional: besides signalling, it is the most abundant ROS protein and physically builds the outer segment. In knockout mice, "without rhodopsin, small OS structures form containing aligned nascent discs," and double-knockout analysis showed that "OS morphogenesis is initiated by RDS-mediated rim formation… with subsequent disc growth mediated by rhodopsin" [PMID: 24897172](https://pubmed.ncbi.nlm.nih.gov/24897172/). Rhodopsin participates in a disc-membrane complex with peripherin-2/RDS and the CNGB1a channel subunit [PMID: 26934134](https://pubmed.ncbi.nlm.nih.gov/26934134/). Its delivery to the outer segment through the connecting cilium is a prerequisite for biogenesis — loss of the transition-zone protein TMEM138 mislocalises rhodopsin and abolishes OS morphogenesis [PMID: 35394880](https://pubmed.ncbi.nlm.nih.gov/35394880/). So rhodopsin is simultaneously the sensor and a principal building block of the organelle in which it senses.

### Finding 10 — The Glu113–Lys296 salt bridge enforces the OFF state; its disruption causes congenital stationary night blindness

The functional importance of the counterion is demonstrated by human disease. Congenital stationary night blindness (CSNB) mutants **G90D** and **A292E** "constitutively activate the G protein transducin in the absence of a chromophore," through "an electrostatic disruption of the active site salt bridge between Glu113 and Lys296 that contributes to stabilization of the protein in the inactive state" [PMID: 12590588](https://pubmed.ncbi.nlm.nih.gov/12590588/). The **T94I** mutant behaves similarly — it constitutively activates transducin, is dark-inactive only when reconstituted with 11-cis-retinal, shows reduced thermal stability and an abnormally long-lived MII [PMID: 12466267](https://pubmed.ncbi.nlm.nih.gov/12466267/). Importantly, CSNB is mechanistically distinct from adRP: "the molecular mechanism underlying this disease may not be structural misfolding, as proposed for retinitis pigmentosa mutants, but abnormal functioning of the receptor" [PMID: 12466267](https://pubmed.ncbi.nlm.nih.gov/12466267/). This pair of disease classes cleanly separates rhodopsin's folding/trafficking requirements (adRP) from its ligand-gated switching requirements (CSNB).

### Finding 11 — Effector coupling: a two-transducin coincidence switch suppresses noise at PDE6

Downstream of rhodopsin, the effector step is itself engineered for noise rejection. Membrane-bound rod PDE6 is activated by transducin α-subunits (Gα\*), but "to fully activate PDE6, it takes a second copy of Gα\* which binds with lower affinity, forming Gα\* · PDE6 · Gα\*"; the 1:1 complex "forms with high affinity but has virtually no cGMP hydrolytic activity" [PMID: 30068566](https://pubmed.ncbi.nlm.nih.gov/30068566/). This "functional asymmetry of membrane-bound PDE6 constitutes a coincidence switch and explains the lack of G protein-related noise in visual signal transduction" [PMID: 30068566](https://pubmed.ncbi.nlm.nih.gov/30068566/): the dense burst of Gα\* generated by one light-activated rhodopsin reaches the two-transducin threshold, whereas sparse, spontaneously activated Gα\* does not. Cryo-EM of PDE6 bound to activated transducin defines the architecture of this step [PMID: 31690623](https://pubmed.ncbi.nlm.nih.gov/31690623/) [PMID: 38159849](https://pubmed.ncbi.nlm.nih.gov/38159849/). Rhodopsin's extreme dark stability (Finding 8) and the PDE6 coincidence switch together produce a near-noiseless single-photon detector.

---

## Mechanistic Model / Interpretation

Rhodopsin is best understood as a **light-gated catalytic switch** whose entire design is optimised for one of the most demanding tasks in biology: reliable detection of single photons. The findings assemble into a coherent lifecycle.

### The phototransduction cascade

```
   photon
     │
     ▼
 ┌─────────────────────┐   isomerisation (11-cis → all-trans, ~70% QE)
 │  RHODOPSIN (dark)   │ ─────────────────────────────────────────►  Metarhodopsin II (R*)
 │ 11-cis-retinal OFF  │                                              (active GPCR)
 │ Glu113–Lys296 lock  │                                                   │
 └─────────────────────┘                                                   │ GEF activity
        ▲                                                                   ▼
        │ regenerate                                     Transducin (Gt):  GDP → GTP on Gtα
        │ (RPE65 visual cycle)                                              │
        │                                                                   ▼
 ┌──────┴───────┐                                   Gtα·GTP + PDE6 + Gtα·GTP  (coincidence switch)
 │  opsin +     │ ◄── all-trans-retinal released               │
 │  11-cis-ret  │                                               ▼
 └──────────────┘                                   PDE6 hydrolyses cGMP → [cGMP] falls
                                                                │
   SHUTOFF:                                                     ▼
   GRK1 phosphorylation ──► arrestin-1 capping         CNG channels CLOSE → membrane HYPERPOLARISES
                                                                │
                                                                ▼
                                                        neural signal to bipolar cells / brain
```

### Two functions in one molecule

| Role | Mechanism | Key evidence |
|------|-----------|--------------|
| **Signalling (light sensor / GEF)** | Photon isomerises bound 11-cis-retinal → MII (R\*) → catalyses GDP/GTP exchange on transducin | [PMID: 8068654](https://pubmed.ncbi.nlm.nih.gov/8068654/), [PMID: 36273969](https://pubmed.ncbi.nlm.nih.gov/36273969/) |
| **Structural (disc morphogenesis)** | Most abundant ROS protein; drives disc growth after RDS-mediated rim formation | [PMID: 24897172](https://pubmed.ncbi.nlm.nih.gov/24897172/), [PMID: 26934134](https://pubmed.ncbi.nlm.nih.gov/26934134/) |

### The ON/OFF logic and why disease maps onto it

The receptor's resting (OFF) state is actively enforced by two coupled features: the covalent Schiff-base tether at Lys296 and the Glu113 counterion salt bridge. This is what gives rhodopsin its ~22 kcal/mol thermal isomerisation barrier and makes spontaneous activation a ~once-per-minute event per rod's worth of pigment. The conversion to ON requires photochemical isomerisation that reorganises the retinal pocket and propagates — via the conserved E(D)RY and NPxxY microswitches and a 6–7 Å outward TM6 movement — to open the cytoplasmic transducin-binding cavity.

Human disease alleles dissect this logic:

| Disease class | Representative alleles | Molecular defect | Functional consequence |
|---------------|------------------------|------------------|------------------------|
| **adRP** (autosomal dominant retinitis pigmentosa) | P23H, G188R, Y178C | Misfolding → ER retention, ubiquitinylation, aggregation | Loss of functional pigment + proteotoxic photoreceptor death |
| **CSNB** (congenital stationary night blindness) | G90D, A292E, T94I | Electrostatic disruption of Glu113–Lys296 salt bridge | Constitutive transducin activation (receptor "stuck ON") |
| **Oguchi disease** (shutoff defect) | GRK1 null (effector, not RHO) | Failure to phosphorylate R\* | Prolonged, variable response; delayed dark adaptation |

The elegance is that the **same salt bridge** that keeps rhodopsin OFF for single-photon fidelity is the exact feature whose mutation flips it constitutively ON in CSNB — directly validating the functional annotation. Meanwhile the **noise-suppression theme** recurs at two independent stages: rhodopsin's dark stability at the input, and the PDE6 two-transducin coincidence switch at the output, both engineered to prevent spontaneous molecular events from masquerading as photons.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|------|-----------------|-------------------------------|
| [10926528](https://pubmed.ncbi.nlm.nih.gov/10926528/) | *Crystal structure of rhodopsin: A G protein-coupled receptor* | Landmark 2.8 Å structure; establishes GPCR identity, inverse-agonist role of 11-cis-retinal, cytoplasmic G-protein coupling residues |
| [18563085](https://pubmed.ncbi.nlm.nih.gov/18563085/) | *Crystal structure of ligand-free opsin* | Defines active-state E(D)RY/NPxxY microswitches and 6–7 Å TM6 movement; describes chromophore release/reload |
| [8068654](https://pubmed.ncbi.nlm.nih.gov/8068654/) | *Rhodopsin-transducin interaction* | Defines MII/R\* as the active state that catalyses nucleotide exchange on transducin |
| [36273969](https://pubmed.ncbi.nlm.nih.gov/36273969/) | *Rhodopsin, light-sensor of vision* | Quantifies ~70% photoisomerisation efficiency and links it to transducin activation |
| [37265335](https://pubmed.ncbi.nlm.nih.gov/37265335/) | *Rhodopsin worldview through AFM* | States protein identity, ROS localisation, and primary function |
| [9775212](https://pubmed.ncbi.nlm.nih.gov/9775212/) | *Control of rhodopsin activity in vision* | Demonstrates two-step GRK1-phosphorylation + arrestin shutoff |
| [9419375](https://pubmed.ncbi.nlm.nih.gov/9419375/) | *Null mutation in rhodopsin kinase* | Identifies GRK1 as the quenching kinase; loss → Oguchi disease |
| [37440077](https://pubmed.ncbi.nlm.nih.gov/37440077/) | *Lysine ubiquitylation drives rhodopsin turnover* | Rod-specific expression; P23H misfolding/degradation; adRP context |
| [35275162](https://pubmed.ncbi.nlm.nih.gov/35275162/) | *Subcellular localization of P23H rhodopsin* | WT traffics to OS; P23H mislocalises to inner segment / ER |
| [27830507](https://pubmed.ncbi.nlm.nih.gov/27830507/) | *Vitamin A and Vision* | Defines chromophore chemistry of the visual cycle |
| [41135835](https://pubmed.ncbi.nlm.nih.gov/41135835/) | *RPE65 knockout* | RPE65 isomerohydrolase regenerates 11-cis-retinal; mutations → Leber congenital amaurosis |
| [6788941](https://pubmed.ncbi.nlm.nih.gov/6788941/) | *Two components of electrical dark noise* | Links dark events to spontaneous rhodopsin isomerisation; 22 kcal/mol barrier |
| [20356096](https://pubmed.ncbi.nlm.nih.gov/20356096/) | *Protein fluctuations and thermal activation* | Dark vs light activation barriers; retinal-pocket fluctuation model |
| [24897172](https://pubmed.ncbi.nlm.nih.gov/24897172/) | *Initiation of disc formation requires RDS* | Assigns disc-growth step to rhodopsin after RDS rim formation |
| [26934134](https://pubmed.ncbi.nlm.nih.gov/26934134/) | *RDS and rhodopsin in Cngb1 degeneration* | Rhodopsin–RDS–CNGB1a disc-membrane complex |
| [35394880](https://pubmed.ncbi.nlm.nih.gov/35394880/) | *Tmem138 and rhodopsin localization* | Connecting-cilium trafficking of rhodopsin required for OS biogenesis |
| [12590588](https://pubmed.ncbi.nlm.nih.gov/12590588/) | *CSNB mutant T94I characterization* | Glu113–Lys296 salt bridge disruption → constitutive transducin activation (G90D, A292E) |
| [12466267](https://pubmed.ncbi.nlm.nih.gov/12466267/) | *Thermal/conformational properties of T94I* | Distinguishes CSNB (functional defect) from adRP (misfolding) |
| [30068566](https://pubmed.ncbi.nlm.nih.gov/30068566/) | *It takes two transducins to activate PDE6* | Two-transducin coincidence switch suppresses downstream noise |
| [31690623](https://pubmed.ncbi.nlm.nih.gov/31690623/), [38159849](https://pubmed.ncbi.nlm.nih.gov/38159849/) | *PDE6 with activated G protein* | Cryo-EM architecture of the effector step |
| [36163145](https://pubmed.ncbi.nlm.nih.gov/36163145/) | *Structural view of GPCR signaling in ROS* | Places rhodopsin, PDE6, guanylate cyclase in disc architecture |
| [39880147](https://pubmed.ncbi.nlm.nih.gov/39880147/) | *Structure and self-association of arrestin-1* | Activated arrestin-1 monomer binds phospho-activated rhodopsin |

The evidence base is unusually strong and internally consistent: structural biology (X-ray and cryo-EM), single-cell electrophysiology, spectroscopy, mouse genetics, and human disease genetics all converge on the same mechanistic model. Precise, low-throughput studies (single-rod recordings, defined mutant biochemistry, atomic structures) dominate the evidence, which is exactly the hierarchy the task prioritises.

---

## Limitations and Knowledge Gaps

1. **Species transfer.** Much of the highest-resolution structural and electrophysiological work was performed on **bovine** rhodopsin and **toad/mouse** rods rather than the human P08100 protein. Human rhodopsin is ~93–95% identical to bovine and functionally equivalent, so transfer is well justified, but direct human-protein structural data are comparatively sparse.

2. **Oligomerisation state in situ.** Whether rhodopsin functions as a monomer, dimer, or higher-order oligomer in native disc membranes remains debated; small-angle neutron scattering and AFM studies give differing pictures, and the physiological relevance of dimerisation to transducin activation is unresolved.

3. **Ligand-independent / non-canonical activation.** All-trans-retinal can non-covalently activate apo-opsin via a palmitoylation-dependent second binding pocket, and bleached opsin itself has low constitutive activity. The in vivo significance of these non-canonical signalling modes (e.g. for background adaptation or light damage) is not fully quantified.

4. **Structural role mechanism.** The precise biophysical mechanism by which rhodopsin "drives disc growth" (membrane curvature generation, protein crowding, lipid interactions) is inferred from knockout phenotypes rather than directly demonstrated.

5. **Genotype–phenotype complexity.** More than 150 adRP alleles span multiple biochemical classes (misfolding, trafficking, activation, endocytic defects); the knowledge base here characterises only a representative subset (P23H, G188R, Y178C, R135L, plus CSNB alleles). A unified map linking each mutation class to degeneration mechanism is incomplete.

6. **Hydration and allostery.** Emerging work frames rhodopsin activation in terms of water/osmotic effects and polymer physics; these contributions to the energetics of the MII transition are not yet integrated into the standard switch model.

---

## Proposed Follow-up Experiments / Actions

1. **Human-protein structural confirmation.** Determine cryo-EM structures of recombinant **human** rhodopsin (dark state and MII) in a native-like lipid nanodisc, to confirm that the bovine-derived activation microswitches (E(D)RY, NPxxY, TM6) and the Glu113–Lys296 geometry are identical in the human orthologue.

2. **Direct test of the counterion → disease axis.** Reconstitute human G90D, A292E and T94I in defined membranes and measure constitutive transducin GEF activity and MII lifetime side-by-side against WT, to quantify the dose–response between salt-bridge disruption and CSNB severity.

3. **Resolve the oligomerisation question.** Combine SANS/contrast-matching, AFM, and functional transducin-activation assays in the same physiologically relevant lipid system to define whether the signalling-competent unit is monomer or dimer.

4. **Dissect the structural role.** Use inducible, rod-specific rhodopsin knock-down at defined developmental stages with live imaging of disc growth to separate rhodopsin's morphogenetic contribution from its abundance as a membrane filler, and test candidate partners (RDS/peripherin-2, CNGB1a).

5. **Therapeutic chaperone screening.** Extend the partial-retinoid-agonist strategy (e.g. acyclic-retinal, 9-cis analogues) as pharmacological chaperones for P23H and other misfolding alleles, measuring rescue of ER retention, aggregation (PROTEOSTAT) and in vivo degeneration rate — a direct translational follow-on to the adRP findings.

6. **Quantify non-canonical opsin signalling in vivo.** Use palmitoylation-site (Cys322/Cys323) and counterion mutants in knock-in mice to test whether apo-opsin/all-trans-retinal signalling contributes to background adaptation or light-induced retinal damage.

---

## Conclusion

Human **RHO (P08100) encodes rhodopsin**, the light-activated class-A GPCR of rod photoreceptors and the molecular initiator of scotopic vision. Its primary function is to use a covalently bound 11-cis-retinal inverse agonist — locked OFF by the Glu113–Lys296 salt bridge for near-noiseless single-photon sensitivity — until a photon isomerises it to all-trans-retinal, forming active metarhodopsin II that catalyses GDP/GTP exchange on transducin and drives the rod cGMP phototransduction cascade (transducin → PDE6 → cGMP hydrolysis → CNG-channel closure → hyperpolarisation). It operates as an integral membrane protein in rod outer-segment disc membranes, where it additionally serves a structural role in disc morphogenesis; signalling is terminated by GRK1 phosphorylation plus arrestin-1, and its chromophore is regenerated by the RPE65 visual cycle. The functional annotation is directly validated by human disease: misfolding alleles (P23H) cause autosomal dominant retinitis pigmentosa, while counterion-disrupting alleles (G90D, A292E, T94I) cause congenital stationary night blindness through constitutive transducin activation.


## Artifacts

- [OpenScientist final report](RHO-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](RHO-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:37265335
2. PMID:10926528
3. PMID:8068654
4. PMID:8608127
5. PMID:36273969
6. PMID:36163145
7. PMID:9775212
8. PMID:9419375
9. PMID:39880147
10. PMID:37440077
11. PMID:35275162
12. PMID:38365903
13. PMID:39875362
14. PMID:27830507
15. PMID:18563085
16. PMID:41135835
17. PMID:42321202
18. PMID:6788941
19. PMID:20356096
20. PMID:24897172
21. PMID:26934134
22. PMID:35394880
23. PMID:12590588
24. PMID:12466267
25. PMID:30068566
26. PMID:31690623
27. PMID:38159849