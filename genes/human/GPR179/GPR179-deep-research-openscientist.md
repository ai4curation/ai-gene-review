---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-16T06:52:24.523922'
end_time: '2026-11-16T07:03:08.864399'
duration_seconds: 644.34
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: GPR179
  gene_symbol: GPR179
  uniprot_accession: Q6PRD1
  protein_description: 'RecName: Full=Probable G protein-coupled receptor 179; AltName:
    Full=Probable G protein-coupled receptor 158-like 1; Short=GPR158-like; Flags:
    Precursor;'
  gene_info: Name=GPR179 {ECO:0000303|PubMed:24084093, ECO:0000312|HGNC:HGNC:31371};
    Synonyms=GPR158L, GPR158L1 {ECO:0000303|Ref.1};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the G protein-coupled receptor 3 family.
  protein_domains: GPCR_3_C. (IPR017978); GPR158/179. (IPR043458); GPR158_179_extracellular.
    (IPR054714); 7tm_3 (PF00003); GPR158_179_EC (PF22572)
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
citation_count: 14
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: GPR179-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: GPR179-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q6PRD1
- **Protein Description:** RecName: Full=Probable G protein-coupled receptor 179; AltName: Full=Probable G protein-coupled receptor 158-like 1; Short=GPR158-like; Flags: Precursor;
- **Gene Information:** Name=GPR179 {ECO:0000303|PubMed:24084093, ECO:0000312|HGNC:HGNC:31371}; Synonyms=GPR158L, GPR158L1 {ECO:0000303|Ref.1};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the G protein-coupled receptor 3 family.
- **Key Domains:** GPCR_3_C. (IPR017978); GPR158/179. (IPR043458); GPR158_179_extracellular. (IPR054714); 7tm_3 (PF00003); GPR158_179_EC (PF22572)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GPR179" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GPR179' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GPR179** (gene ID: GPR179, UniProt: Q6PRD1) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# GPR179 (Q6PRD1): The Scaffold and Transsynaptic Adhesion Organizer of the ON‑Bipolar Night‑Vision Synapse

## Gene/Protein Identity Verification

Before presenting the research, the target identity was confirmed against the supplied UniProt record. The gene symbol **GPR179**, UniProt accession **Q6PRD1**, organism **Homo sapiens**, protein family **G protein-coupled receptor 3 (class C) family**, and the characteristic domains (**GPR158/179** fold, **GPR158_179_extracellular**, **7tm_3 / PF00003**) all match the primary literature reviewed here. The literature on GPR179 is coherent, specific, and consistently refers to the human retinal class C orphan GPCR encoded at HGNC:31371, with synonyms **GPR158L / GPR158L1** reflecting its paralogy to GPR158. There is **no ambiguity**: all 24 papers reviewed describe the same molecule, and the disease gene (complete congenital stationary night blindness, cCSNB) matches the UniProt-cited reference [PMID: 24084093](https://pubmed.ncbi.nlm.nih.gov/24084093/). Research proceeded with confidence.

---

## Summary

**Human GPR179 is a retina-specific class C orphan G-protein-coupled receptor that functions primarily as a postsynaptic scaffold and transsynaptic adhesion molecule, rather than as a classical ligand-activated signaling receptor.** It is expressed at the dendritic tips of depolarizing ("ON") bipolar cells (DBCs/ON-BCs), precisely where those dendrites invaginate the photoreceptor terminal and sit juxtaposed to the presynaptic ribbon — the location of the first synapse in vision. Its defining role is the **structural organization of the mGluR6 → Gαo → TRPM1 phototransduction signalplex** that converts the light-evoked decrease in glutamate release from photoreceptors into depolarization of ON-bipolar cells.

Mechanistically, GPR179 performs three interlocking jobs. First, it is the **organizing scaffold** of the postsynaptic cascade, physically recruiting the metabotropic glutamate receptor mGluR6, the effector cation channel TRPM1, and the regulator-of-G-protein-signaling (RGS) proteins into a macromolecular complex. Second, it is the **membrane anchor for the RGS7/RGS11–Gβ5 GTPase-activating protein (GAP) complex** (together with R9AP), the machinery that rapidly inactivates Gαo and thereby shapes the kinetics and fidelity of the ON response. Third, it acts as a **transsynaptic adhesion bridge**, linking the postsynaptic apparatus to the presynaptic dystroglycan–pikachurin extracellular matrix via heparan sulfate proteoglycans, thereby aligning pre- and post-synaptic machinery across the cleft. Consistent with the GPR158/179 family, cryo-EM shows GPR179 lacks a canonical Venus-flytrap ligand-binding domain and instead adopts a noncanonical homodimer architecture suited to the highly curved dendritic-tip membrane.

The functional consequence of these roles is stark and specific: **loss of GPR179 abolishes the ON-bipolar light response** (absent electroretinogram b-wave) and causes **autosomal-recessive complete congenital stationary night blindness (cCSNB)** in humans, with a conserved requirement demonstrated from zebrafish to mouse to human. GPR179 is therefore best classified not as a signal-transducing receptor in the conventional sense, but as a **scaffold/adhesion GPCR** — a structural organizer and GAP-anchoring platform at the heart of the night-vision synapse.

---

## Key Findings

### Finding 1 — GPR179 is an orphan class C GPCR at ON-bipolar dendritic tips whose loss causes complete CSNB

GPR179 was identified as a cCSNB disease gene through whole-exome sequencing of patients who lacked mutations in previously known genes. A homozygous missense mutation (c.1807C>T [p.His603Tyr]) in a consanguineous autosomal-recessive family and a homozygous frameshift mutation (c.278delC [p.Pro93Glnfs*57]) in a simplex male patient established GPR179 loss-of-function as causal for complete CSNB ([PMID: 22325361](https://pubmed.ncbi.nlm.nih.gov/22325361/)). GPR179 is now consistently listed among the small core set of genes that encode the ON-bipolar signalplex — **NYX, GRM6 (mGluR6), TRPM1, GPR179, and LRIT3** — mutations in any of which produce the same clinical and electrophysiological picture.

Its molecular identity and location are unambiguous: GPR179 is "an orphan class C GPCR … expressed at the dendritic tips of ON-bipolar cells in the retina. It plays a pivotal role in the initial synaptic transmission of visual signals from photoreceptors, and its deficiency is known to be the cause of complete congenital stationary night blindness" ([PMID: 39333506](https://pubmed.ncbi.nlm.nih.gov/39333506/)). This single statement captures identity (orphan class C GPCR), localization (ON-bipolar dendritic tips), function (initial synaptic transmission), and disease (cCSNB).

### Finding 2 — GPR179 is the organizing scaffold of the mGluR6 postsynaptic signalplex

The central mechanistic insight is that GPR179 is not merely a passenger in the ON-bipolar cascade but its **physical organizer**. Co-immunoprecipitation and proximity-based assays in transfected cells and native mouse retina showed that "in mouse retinas, GPR179 forms physical complexes with the main components of the metabotropic cascade, recruiting mGluR6, TRPM1, and the RGS proteins" ([PMID: 24114537](https://pubmed.ncbi.nlm.nih.gov/24114537/)). Genetic dissection in the same work indicated that ablation of mGluR6 or RGS proteins (but not TRPM1) impaired GPR179 postsynaptic targeting, revealing a web of interdependent co-stabilization among signalplex members. GPR179 thus behaves as a **core nucleating scaffold** that brings the receptor (mGluR6), the effector channel (TRPM1), and the signal-termination machinery (RGS) into a single functional macromolecular complex at the dendritic tip.

### Finding 3 — GPR179 anchors the RGS7/RGS11–Gβ5 GAP complex that inactivates Gαo

A key determinant of the speed and reliability of the ON response is how quickly the Gαo cycle is reset. GPR179 provides the structural anchor for this timing machinery. Biochemical experiments showed that "RGS7 binds to a conserved site in GPR179 and that RGS11 in vivo forms a complex only with R9AP. R9AP and GPR179 are further integrated via direct protein-protein interactions involving their cytoplasmic domains. Elimination of GPR179 prevents postsynaptic accumulation of R9AP" ([PMID: 26961947](https://pubmed.ncbi.nlm.nih.gov/26961947/)). Because RGS7/RGS11–Gβ5 are the GTPase-activating proteins that accelerate hydrolysis of Gαo-GTP, GPR179 effectively positions the "off-switch" of the cascade at the correct subcellular site. Concurrent knockout of R9AP and RGS7 in that study abolished synaptic transmission, producing a night-blindness phenotype — demonstrating that the GAP module GPR179 anchors is functionally essential.

### Finding 4 — GPR179 mediates transsynaptic adhesion to the dystroglycan–pikachurin complex via heparan sulfate proteoglycans

Beyond organizing the postsynaptic cytoplasmic machinery, GPR179 reaches across the synaptic cleft. The GPR158/179 orphan receptors associate with synaptic-cleft heparan sulfate proteoglycans (HSPGs), and "the HSPG member Pikachurin, released by photoreceptors, recruits a key post-synaptic signaling complex of downstream ON-bipolar neurons in coordination with the pre-synaptic dystroglycan glycoprotein complex. We further demonstrate that this transsynaptic assembly plays an essential role in synaptic transmission of photoreceptor signals" ([PMID: 30282023](https://pubmed.ncbi.nlm.nih.gov/30282023/)). This establishes GPR179 as a **transsynaptic adhesion molecule** that bridges the presynaptic dystroglycan–pikachurin matrix to the postsynaptic signalplex, aligning the two sides of the ribbon synapse so that light signals are faithfully transmitted.

### Finding 5 — Cryo-EM reveals a noncanonical class C homodimer suited to the curved dendritic-tip membrane

The structure of GPR179 explains its unusual biology. Cryo-EM of the human GPR179 transmembrane domain showed that "the transmembrane domain (TMD) of GPR179 forms a homodimer through the TM1/7 interface with a single inter-protomer disulfide bond, adopting a noncanonical dimerization mode. Furthermore, the TMD dimer exhibits architecture well-suited for the highly curved membrane of the dendritic tip" ([PMID: 39333506](https://pubmed.ncbi.nlm.nih.gov/39333506/)). Most class C GPCRs dimerize through TM4/5/6 interfaces; GPR179's TM1/7 interface is distinctive and appears to be a structural adaptation to the extreme membrane curvature at the invaginating dendritic tip. The structure reinforces the interpretation that GPR179's function is architectural — shaping and organizing a specialized membrane microdomain — rather than classical agonist-driven signal transduction.

### Finding 6 — Ultrastructural localization to invaginating dendritic tips; loss closes/eliminates TRPM1 channels

Immuno-electron microscopy of human retina placed GPR179 with precision: "In the human retina, GPR179 is localized on the tips of ON-BC dendrites, which invaginate photoreceptors and terminate juxtaposed to the synaptic ribbon" ([PMID: 24084093](https://pubmed.ncbi.nlm.nih.gov/24084093/)). This is the exact nanometer-scale site where phototransduction output is received. The same study linked GPR179 to the downstream effector state: "The similarities of 15-Hz flicker ERGs noted in GPR179 patients and NYX or TRPM1 patients suggest that the loss of GPR179 leads to the loss or closure of TRPM1 channels." Because TRPM1 is the cation channel whose opening depolarizes the ON-bipolar cell in response to light, this places GPR179 functionally **upstream of, and required for, the correct operation of the TRPM1 effector channel**.

### Finding 7 — GPR179 is required for ON-bipolar function and conserved from zebrafish to human, colocalizing with mGluR6/GRM6

The requirement for GPR179 in ON-bipolar signaling is evolutionarily conserved and demonstrated by complementary genetic approaches. The spontaneous mouse mutant Gpr179(nob5) was identified by the absence of the ERG b-wave (the readout of depolarizing bipolar cell function); its lesion is a large transposon-like insertion in Gpr179. Immunohistochemistry confirmed the molecular partnership: "We developed an antibody against mouse GPR179, which robustly labeled DBC dendritic terminals in wild-type mice. This labeling colocalized with the expression of GRM6 and was absent in Gpr179(nob5/nob5) mutant mice" ([PMID: 22325362](https://pubmed.ncbi.nlm.nih.gov/22325362/)). Cross-species confirmation came from zebrafish, where "functional knockdown of gpr179 in zebrafish led to a marked reduction in the amplitude of the ERG b-wave," and from the identification of inactivating mutations in human cCSNB patients. The colocalization with mGluR6 (GRM6) and conservation across vertebrates underscore that GPR179 is a hard-wired, essential component of the ON-bipolar dendritic signalplex.

### Finding 8 — GPR179 belongs to the GPR158/179 family, which lacks a Venus-flytrap domain and acts as a membrane anchor/GAP platform for RGS7–Gβ5

GPR179's mechanism is best understood through its family identity. It is the paralog of GPR158 (hence the synonym GPR158L/GPR158L1), and both belong to the "GPR158/179 group of orphan receptors" that associate with synaptic HSPGs ([PMID: 30282023](https://pubmed.ncbi.nlm.nih.gov/30282023/)). For the closely related and better-characterized GPR158, cryo-EM established the family's defining features: "Among class C GPCRs, GPR158 is unique as it lacks a Venus flytrap-fold ligand-binding domain and terminates Gαi/o protein signaling through the RGS7-Gβ5 heterodimer" ([PMID: 34815401](https://pubmed.ncbi.nlm.nih.gov/34815401/)). GPR179 mirrors this: it binds RGS7 at a conserved site ([PMID: 26961947](https://pubmed.ncbi.nlm.nih.gov/26961947/)). The family-level inference is powerful — it reframes GPR179 away from the "classical agonist-binding GPCR" paradigm and toward a **membrane-anchored scaffold and RGS-GAP presentation platform** that organizes and terminates Gαo/i signaling.

---

## Mechanistic Model / Interpretation

### The first synapse of vision

Vision begins when light reduces glutamate release from rod and cone photoreceptors. ON-bipolar cells respond to this *decrease* in glutamate by *depolarizing* — a sign-inverting step achieved by a metabotropic (G-protein) cascade rather than a direct ionotropic receptor. GPR179 is the structural lynchpin that assembles and positions this cascade at the invaginating dendritic tip.

### The cascade and GPR179's place in it

```
   PHOTORECEPTOR TERMINAL (presynaptic)
   +---------------------------------------------+
   |  Ribbon  .  glutamate release (down in light)|
   |  Dystroglycan == Pikachurin (HSPG matrix)   |
   +---------------+-----------------------------+
                   |  transsynaptic adhesion (HSPG bridge)
   ================+=============== synaptic cleft ===
                   |
   +---------------v-----------------------------+
   |  ON-BIPOLAR DENDRITIC TIP (postsynaptic)    |
   |                                             |
   |     +----------  GPR179  ----------+        |
   |     | (scaffold / adhesion / anchor)|      |
   |     v            v            v              |
   |  mGluR6       RGS7/RGS11    R9AP            |
   |  (GRM6)        -Gbeta5 (GAP)                |
   |     |            |                          |
   |     v            v                          |
   |   Galpha-o -GTP-> (RGS accelerates GTP      |
   |     |             hydrolysis = OFF switch)   |
   |     v                                       |
   |   TRPM1 channel -- opens in light --> DEPOLARIZE
   +---------------------------------------------+
```

GPR179 sits at the center of this diagram as the organizer. In the dark, tonic glutamate activates mGluR6, which couples to Gαo; active Gαo keeps the TRPM1 cation channel closed. In the light, glutamate falls, mGluR6/Gαo activity drops, and TRPM1 opens, depolarizing the cell. The speed and reliability of this switching depend on rapid Gαo inactivation by the RGS7/RGS11–Gβ5 GAP complex. GPR179 performs the following non-redundant roles:

| Role | Molecular action | Evidence (PMID) |
|---|---|---|
| **Scaffold** | Physically recruits mGluR6, TRPM1, RGS proteins into one complex | 24114537 |
| **GAP anchor** | Binds RGS7 at a conserved site; integrates R9AP via cytoplasmic domains; required for postsynaptic R9AP accumulation | 26961947 |
| **Transsynaptic adhesion** | Links postsynaptic complex to presynaptic dystroglycan–pikachurin via HSPGs | 30282023 |
| **Membrane architect** | Noncanonical TM1/7 homodimer fitting the curved dendritic-tip membrane | 39333506 |
| **Effector enabler** | Loss leads to loss/closure of TRPM1 channels | 24084093 |

### Why GPR179 is a scaffold, not a classical receptor

Three independent lines of evidence converge on this reclassification. (1) **Family identity**: the GPR158/179 group lacks the Venus-flytrap ligand-binding domain universal to other class C GPCRs, and the paralog GPR158 terminates rather than initiates Gαi/o signaling via RGS7–Gβ5 ([PMID: 34815401](https://pubmed.ncbi.nlm.nih.gov/34815401/)). (2) **Structure**: the noncanonical TM1/7 dimer and curved-membrane fit indicate an architectural role ([PMID: 39333506](https://pubmed.ncbi.nlm.nih.gov/39333506/)). (3) **Interactome/genetics**: GPR179 physically assembles the signalplex and anchors the GAP machinery, and its deletion disrupts the localization of partners (R9AP, and functionally TRPM1) rather than acting as a stand-alone signal transducer ([PMID: 24114537](https://pubmed.ncbi.nlm.nih.gov/24114537/); [PMID: 26961947](https://pubmed.ncbi.nlm.nih.gov/26961947/)). The "orphan" status is therefore not a gap in knowledge awaiting a hidden agonist, but a reflection of a genuinely scaffold-centric mechanism.

### Localization: where GPR179 does its job

GPR179 carries out its function at a single, highly specialized location: the **plasma membrane of the ON-bipolar dendritic tip, within the photoreceptor invagination, juxtaposed to the synaptic ribbon** in the outer plexiform layer of the retina ([PMID: 24084093](https://pubmed.ncbi.nlm.nih.gov/24084093/)). As a precursor glycoprotein with a 7-transmembrane class C architecture, it is an integral membrane protein whose extracellular region engages the cleft HSPG matrix and whose cytoplasmic domains engage R9AP/RGS and the rest of the signalplex. This is a cell-surface, synaptic function — not cytoplasmic, nuclear, or secreted.

---

## Evidence Base

| PMID | Title (abbreviated) | Contribution |
|---|---|---|
| [22325361](https://pubmed.ncbi.nlm.nih.gov/22325361/) | WES identifies GPR179 mutations in AR cCSNB | Original human disease-gene discovery; defines loss-of-function phenotype |
| [22325362](https://pubmed.ncbi.nlm.nih.gov/22325362/) | GPR179 required for DBC function; mutated in AR cCSNB | Mouse nob5 model; colocalization with GRM6; zebrafish conservation |
| [24084093](https://pubmed.ncbi.nlm.nih.gov/24084093/) | Ultrastructural localization of GPR179 (UniProt ref.) | Immuno-EM in human retina; links loss to TRPM1 closure |
| [24114537](https://pubmed.ncbi.nlm.nih.gov/24114537/) | GPR179 macromolecular complexes in ON-BCs | Core scaffolding evidence: recruits mGluR6/TRPM1/RGS |
| [26961947](https://pubmed.ncbi.nlm.nih.gov/26961947/) | Anchoring subunits specify RGS targeting | GPR179 binds RGS7; anchors R9AP/RGS GAP complex |
| [30282023](https://pubmed.ncbi.nlm.nih.gov/30282023/) | Transsynaptic GPR179–dystroglycan–pikachurin | Transsynaptic adhesion role via HSPGs |
| [39333506](https://pubmed.ncbi.nlm.nih.gov/39333506/) | Cryo-EM of human GPR179 TMD | Noncanonical TM1/7 homodimer; curved-membrane fit |
| [34815401](https://pubmed.ncbi.nlm.nih.gov/34815401/) | Structure of GPR158–RGS7–Gβ5 | Family mechanism: no Venus-flytrap; RGS7–Gβ5 coupling |
| [34793198](https://pubmed.ncbi.nlm.nih.gov/34793198/) | Cryo-EM GPR158–RGS7–Gβ5 | Family structural organization (homodimer, Cache domain) |
| [36357076](https://pubmed.ncbi.nlm.nih.gov/36357076/) | GPR158–RGS7 cross-talk review | Family signaling framework |

Supporting context on the shared signalplex and therapy comes from the broader cCSNB literature: whole-exome identification of LRIT3 ([PMID: 23246293](https://pubmed.ncbi.nlm.nih.gov/23246293/)), the role of LRIT3 in TRPM1 targeting and cone-ON-BC organization ([PMID: 28334377](https://pubmed.ncbi.nlm.nih.gov/28334377/)), mGluR6 trafficking determinants ([PMID: 34793838](https://pubmed.ncbi.nlm.nih.gov/34793838/)), the ER-resident pool of TRPM1 ([PMID: 30027108](https://pubmed.ncbi.nlm.nih.gov/30027108/)), and gene-augmentation therapy that can restore night vision in cCSNB models ([PMID: 34401402](https://pubmed.ncbi.nlm.nih.gov/34401402/); [PMID: 40766553](https://pubmed.ncbi.nlm.nih.gov/40766553/)). These place GPR179 within an interdependent, therapeutically tractable signalplex.

**How the evidence converges:** No single paper challenges the scaffold/adhesion model; rather, independent approaches — human genetics, mouse and zebrafish models, immuno-EM, biochemistry/interactomics, and cryo-EM structure — each add an orthogonal layer that reinforces the same conclusion. The strongest claims (scaffolding, RGS anchoring, transsynaptic adhesion) each rest on direct experimental evidence, while the mechanistic reclassification (no Venus-flytrap, RGS-GAP platform) is partly inferred from the closely related paralog GPR158.

---

## Limitations and Knowledge Gaps

1. **Orphan status / ligand.** GPR179 has no established endogenous agonist. The family analogy to GPR158 strongly suggests it does not use a classical Venus-flytrap ligand mechanism, but whether GPR179 binds a small-molecule or peptide modulator remains undetermined for GPR179 specifically.

2. **Structure is partial.** The cryo-EM structure resolves the transmembrane domain homodimer ([PMID: 39333506](https://pubmed.ncbi.nlm.nih.gov/39333506/)); the full-length architecture including the large extracellular region and the exact GPR179–RGS7/R9AP interface in situ is not fully resolved.

3. **Human vs. model-organism inference.** Much of the detailed biochemistry (RGS anchoring, signalplex recruitment) was performed in mouse retina. While human genetics, human immuno-EM, and human cryo-EM corroborate the picture, some mechanistic steps are extrapolated from mouse.

4. **Directionality of co-dependence.** Signalplex members mutually stabilize one another (e.g., mGluR6/RGS loss impairs GPR179 targeting; GPR179 loss impairs R9AP accumulation). Disentangling the precise hierarchy/order of assembly during synaptogenesis is incomplete.

5. **Myopia mechanism.** cCSNB (including GPR179 cases) is associated with high myopia, but how GPR179-dependent ON-BC signaling contributes to refractive development is not mechanistically resolved and falls outside the precise primary-function focus of this report.

---

## Proposed Follow-up Experiments / Actions

1. **Full-length cryo-EM of the GPR179 signalplex.** Resolve GPR179 in complex with RGS7/RGS11–Gβ5 and R9AP, and with the extracellular HSPG/pikachurin interaction, to map the anchoring and adhesion interfaces at atomic resolution.

2. **Define the extracellular binding partners directly.** Use proximity labeling (BioID/TurboID) at the ON-BC dendritic tip and in vitro binding assays to confirm and quantify GPR179–HSPG–pikachurin–dystroglycan contacts and test whether GPR179's extracellular domain is sufficient for transsynaptic adhesion.

3. **Separation-of-function mutants.** Engineer GPR179 variants that selectively disrupt (a) RGS7 binding, (b) R9AP integration, or (c) transsynaptic adhesion, and test each in Gpr179-null retina to assign distinct phenotypic contributions to kinetics vs. assembly vs. alignment.

4. **Assembly-order time course.** Use developmental immuno-EM / live imaging in retinal organoids or mouse to determine the temporal hierarchy of signalplex assembly and GPR179's nucleating role during synaptogenesis.

5. **Therapeutic translation.** Building on gene-augmentation successes for LRIT3 and other cCSNB genes, evaluate AAV-mediated GPR179 replacement in Gpr179-null models for restoration of the ERG b-wave and visual acuity, and define the therapeutic window in the mature retina.

6. **Ligand/modulator screen.** Given family precedent, screen for small molecules or peptides that bind the GPR179 extracellular/Cache-like region, which could reveal whether any ligand-dependent modulation of its scaffolding function exists.

---

## Conclusion

GPR179 is a retina-specific **class C orphan GPCR that functions as a scaffold and transsynaptic adhesion organizer**, not as a classical ligand-driven signal transducer. At the dendritic tips of ON-bipolar cells — invaginating the photoreceptor terminal at the first synapse of vision — it assembles the mGluR6/TRPM1/RGS signalplex, anchors the RGS7/RGS11–Gβ5/R9AP GAP machinery that times Gαo inactivation, and bridges to the presynaptic dystroglycan–pikachurin matrix via heparan sulfate proteoglycans. Its structure (noncanonical TM1/7 homodimer) and family identity (GPR158/179, no Venus-flytrap domain) reinforce this architectural role. Loss of GPR179 collapses the ON response, closing/eliminating TRPM1 channels and abolishing the ERG b-wave, producing autosomal-recessive complete congenital stationary night blindness — a phenotype conserved from zebrafish to human.


## Artifacts

- [OpenScientist final report](GPR179-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](GPR179-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:24084093
2. PMID:22325361
3. PMID:39333506
4. PMID:24114537
5. PMID:26961947
6. PMID:30282023
7. PMID:22325362
8. PMID:34815401
9. PMID:23246293
10. PMID:28334377
11. PMID:34793838
12. PMID:30027108
13. PMID:34401402
14. PMID:40766553