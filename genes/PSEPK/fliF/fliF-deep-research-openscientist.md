---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T16:43:33.793287'
end_time: '2026-08-31T16:58:44.782837'
duration_seconds: 910.99
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: fliF
  gene_symbol: fliF
  uniprot_accession: Q88ET4
  protein_description: 'RecName: Full=Flagellar M-ring protein {ECO:0000256|ARBA:ARBA00017949,
    ECO:0000256|PIRNR:PIRNR004862};'
  gene_info: Name=fliF {ECO:0000313|EMBL:AAN69947.1}; OrderedLocusNames=PP_4369 {ECO:0000313|EMBL:AAN69947.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the FliF family. {ECO:0000256|ARBA:ARBA00007971,
  protein_domains: AMP-bd_C_sf. (IPR045851); Flag_M-ring_C. (IPR013556); FlgMring_FliF.
    (IPR000067); FliF_N_dom. (IPR006182); YscJ/FliF. (IPR043427)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 21
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: fliF-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: fliF-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88ET4
- **Protein Description:** RecName: Full=Flagellar M-ring protein {ECO:0000256|ARBA:ARBA00017949, ECO:0000256|PIRNR:PIRNR004862};
- **Gene Information:** Name=fliF {ECO:0000313|EMBL:AAN69947.1}; OrderedLocusNames=PP_4369 {ECO:0000313|EMBL:AAN69947.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the FliF family. {ECO:0000256|ARBA:ARBA00007971,
- **Key Domains:** AMP-bd_C_sf. (IPR045851); Flag_M-ring_C. (IPR013556); FlgMring_FliF. (IPR000067); FliF_N_dom. (IPR006182); YscJ/FliF. (IPR043427)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "fliF" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'fliF' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **fliF** (gene ID: fliF, UniProt: Q88ET4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# FliF (Q88ET4, PP_4369) — Flagellar M-ring Protein of *Pseudomonas putida* KT2440

## Functional Annotation Research Report

---

## Summary

**FliF (UniProt Q88ET4; ordered locus PP_4369) is the flagellar M-ring/MS-ring protein of *Pseudomonas putida* KT2440 — a non-catalytic structural protein that forms the transmembrane structural core, assembly template, and rotor base of the bacterial flagellar motor.** It is *not* an enzyme, a transporter, or a signaling molecule. Its "substrate" is not a small molecule but rather the flagellar machine itself: FliF self-assembles into a ring that serves as the physical foundation upon which the entire flagellum is built. The gene symbol *fliF* is unambiguous here and matches the UniProt description, the FliF family (IPR000067) domain complement, and the *P. putida* KT2440 organism assignment exactly — no gene-identity conflict was encountered.

Architecturally, the *P. putida* protein is a 592-residue integral inner-membrane protein with exactly two transmembrane helices (residues ~40–59 and ~494–512) that flank a large (~430-residue) periplasmic region containing the ring-building motifs, together with a cytoplasmic N-terminus and a cytoplasmic C-terminal tail. Roughly 34 copies of FliF oligomerize within the cytoplasmic (inner) membrane to build the **MS-ring**, the earliest-formed component of the flagellar basal body. This topology, established experimentally in *Salmonella*, is fully conserved in the *P. putida* ortholog based on direct sequence and hydropathy analysis of the Q88ET4 record, justifying orthology-based functional transfer.

Functionally, the MS-ring performs three interlocking roles. **(1)** Its central pore houses the flagellar type III secretion system (fT3SS) export gate (FlhA, FlhB, FliO, FliP, FliQ, FliR), the machine that secretes the axial subunits (rod, hook, filament) that build the rest of the flagellum. **(2)** FliF's C-terminal cytoplasmic tail co-folds with the rotor protein FliG to create the MS-ring:C-ring interface, forming the motor rotor and coupling stator-generated torque to flagellar rotation and CW/CCW switching. **(3)** As the founding scaffold laid down at the earliest stage of assembly, FliF is essential for motility and acts as an assembly checkpoint that gates expression of late flagellar genes. In *Pseudomonas*, *fliF* is a **Class II** gene in a four-tiered transcriptional hierarchy driven by the master regulator FleQ together with RpoN (σ54), and its product is targeted to the cell pole by FlhF/FimV to generate the characteristic polar (unipolar) flagellation of *P. putida*.

---

## Key Findings

### Finding 1 — FliF is the flagellar M-ring/MS-ring protein: the structural core and assembly template of the basal body

FliF is a **single-domain structural protein** whose function is architectural rather than catalytic. It possesses two transmembrane helices flanking a large periplasmic region that contains three ring-building motifs (RBM/D1–D2–D3), which are homologous to the ring-building motifs of the injectisome proteins PrgK and PrgH — reflecting the deep evolutionary kinship between the flagellar basal body and the virulence-associated type III injectisome. FliF self-assembles into the transmembrane **MS-ring**, embedded in the cytoplasmic (inner) membrane.

Cryo-electron microscopy of native basal bodies from *Salmonella* establishes that the ring is built from **34 FliF subunits**, organized into the periplasmic S-ring and the M-ring. Remarkably, the 34 subunits adopt two distinct conformations that generate different rotational subsymmetries within a single ring — a 23-fold inner symmetry and an 11-fold middle symmetry — reconciling long-standing observations of symmetry mismatch in the motor ([PMID: 34244518](https://pubmed.ncbi.nlm.nih.gov/34244518/); [PMID: 33653894](https://pubmed.ncbi.nlm.nih.gov/33653894/)). As stated directly: *"The bacterial flagellar MS ring is a transmembrane complex acting as the core of the flagellar motor and template for flagellar assembly"* and *"the native MS ring is formed by 34 FliF subunits"* ([PMID: 34244518](https://pubmed.ncbi.nlm.nih.gov/34244518/)).

The MS-ring forms at the **earliest stage of flagellar assembly** and serves as the template/base upon which all downstream axial structures (rod, hook, filament) are constructed, as well as the housing for the flagellar protein export gate. As described in the literature: *"The MS-ring is embedded in the cytoplasmic membrane and is formed at the earliest stage of flagellar formation to serve as the base for flagellar assembly as well as a housing for the flagellar protein export gate complex. The MS-ring is formed by FliF, which has two transmembrane helices and a large periplasmic region"* ([PMID: 33653894](https://pubmed.ncbi.nlm.nih.gov/33653894/)).

The *P. putida* protein PP_4369 belongs to the FliF family (IPR000067) and carries the FliF N-terminal domain (IPR006182) and the Flagellar M-ring C-terminal domain (IPR013556), matching this architecture precisely.

### Finding 2 — The MS-ring central pore houses the flagellar type III secretion (export) gate

The MS-ring is not merely a passive scaffold; its central pore is the physical housing for the membrane-embedded flagellar type III secretion system (fT3SS) export apparatus, comprising **FlhA, FlhB, FliO, FliP, FliQ, and FliR**. This export gate secretes the thousands of axial protein subunits (rod, hook, filament) needed to build the flagellum beyond the membrane. As reported: *"The membrane-embedded part of the export apparatus, which consists of FlhA, FlhB, FliO, FliP, FliQ and FliR, is located in the central pore of the MS ring formed by 26 copies of FliF"* ([PMID: 24450479](https://pubmed.ncbi.nlm.nih.gov/24450479/)).

Structural work shows that the geometry of the ring is precisely matched to this cargo: *"The internal core of the M ring, formed by 23 subunits, forms a hole of the right size to accommodate the protein export gate"* ([PMID: 34244518](https://pubmed.ncbi.nlm.nih.gov/34244518/)). FliF interacts directly with FlhA, and roughly nine FlhA molecules assemble into the export gate coordinately with MS-ring formation.

Genetic evidence corroborates a direct, functionally meaningful FliF–FlhA interaction: intergenic suppression studies in *Salmonella* show that a defect in the FliF periplasmic domain (loss of Ala-174/Ser-175) can be suppressed by compensating mutations in the membrane domain of FlhA. *"FliF-FlhA intergenic suppression is a fairly rare event. FlhA is a component of the flagellar protein export apparatus"* ([PMID: 11160096](https://pubmed.ncbi.nlm.nih.gov/11160096/)). Rare intergenic suppression of this kind is a classic signature of a specific, direct physical contact between two proteins.

### Finding 3 — FliF forms the motor rotor by co-folding with FliG, coupling torque to rotation

Below the membrane, FliF builds the **rotor** in partnership with the C-ring protein FliG. The C-terminal cytoplasmic tail of FliF **co-folds** with the N-terminal domain of FliG, forming a "split" or shared domain at the MS-ring:C-ring interface. This interface is the mechanical junction at which stator-generated torque is converted into rotation: *"The interface between the membrane (MS) and cytoplasmic (C) rings of the bacterial flagellar motor couples torque generation to rotation within the membrane"* ([PMID: 28089452](https://pubmed.ncbi.nlm.nih.gov/28089452/)).

The intimacy of the FliF–FliG partnership is demonstrated by engineering experiments: *"A full-frame fusion of FliF with the rotor protein FliG assembles rings in non-motile expression hosts"* ([PMID: 30082903](https://pubmed.ncbi.nlm.nih.gov/30082903/)), and coevolution-guided modelling supports FliF providing a periplasmic hub platform on which the FliG ring self-assembles. Localization studies in *Salmonella* show that FliF-YFP forms puncta only when FliG is present (and independently of FliM, FliN, FlhA, FlhB, FliO/P/Q/R), identifying FliG as FliF's immediate downstream assembly partner.

Together, the transmembrane MS-ring (FliF) plus the cytoplasmic C-ring (FliG, FliM, FliN) constitute the motor rotor: *"The rotor is composed of the transmembrane MS ring made of FliF and the cytoplasmic C ring consisting of FliG, FliM, and FliN"* ([PMID: 30940700](https://pubmed.ncbi.nlm.nih.gov/30940700/)). This assembly transmits torque from the ion-driven stator units to flagellar rotation and mediates the directional (clockwise/counter-clockwise) switching that underlies chemotaxis.

### Finding 4 — *fliF* is an early (Class II) flagellar gene essential for motility and acts as an assembly checkpoint

MS-ring assembly is one of the very first events of flagellar biogenesis. In vivo assembly studies in *E. coli* show that *"motor self-assembly is initiated by oligomerization of the membrane export apparatus protein FlhA, which is followed by the recruitment of the MS ring component FliF and by the ordered association of other motor proteins"* ([PMID: 21244534](https://pubmed.ncbi.nlm.nih.gov/21244534/)). FliF is thus placed at the foundation of the ordered assembly cascade.

Because it is foundational, loss of FliF is catastrophic for motility. Deletion or mutation of *fliF* abolishes both motility and flagellum production in diverse bacteria, including *Helicobacter pylori* ([PMID: 10960117](https://pubmed.ncbi.nlm.nih.gov/10960117/)) and *Listeria monocytogenes* ([PMID: 16113269](https://pubmed.ncbi.nlm.nih.gov/16113269/)). Critically, *fliF* loss also feeds back onto the flagellar gene-regulatory hierarchy: *"The MS ring (encoded by fliF) is one of the earliest flagellar structures assembled. Deletion of fliF resulted in the elimination of RpoN-dependent transcripts"* ([PMID: 25825427](https://pubmed.ncbi.nlm.nih.gov/25825427/)). Completion of the FliF/FliG basal body plus the export apparatus is required for efficient secretion of the anti-σ factor FlgM, which in turn de-represses the late (σ28/FliA) flagellar genes — the mechanism by which assembly progress is coupled to gene expression ([PMID: 25313396](https://pubmed.ncbi.nlm.nih.gov/25313396/)).

In *P. putida* — a polar-flagellated organism — *fliF* is an early flagellar component whose spatial targeting to the cell pole is directed by FlhF (and the polar landmark FimV): *"FlhF determines the polar position of the flagella by targeting early flagellar components to the cell pole and preventing their nucleation at non-polar sites"* ([PMID: 39709681](https://pubmed.ncbi.nlm.nih.gov/39709681/)). Correct positioning of the FliF MS-ring therefore underlies the unipolar flagellar placement characteristic of this species.

### Finding 5 — The *P. putida* ortholog has the canonical bitopic-to-M-ring architecture

Direct analysis of the Q88ET4 UniProt record confirms that the *P. putida* protein is a **592-residue integral membrane protein with exactly two transmembrane helices** (residues 40–59 and 494–512). An independent Kyte–Doolittle hydropathy scan reproduced these assignments (hydrophobic windows at ~34–61, max KD = 2.58; and ~485–517, max KD = 2.72), providing bioinformatic corroboration of the annotation.

The two TM helices flank a large (~430-residue) **periplasmic region** containing the two annotated ring-building domains — the Flagellar M-ring N-terminal domain (residues ~61–237) and the Flagellar M-ring C-terminal domain (residues ~270–468) — plus a disordered linker (~292–391). The N-terminus (residues 1–39) and the C-terminal ~80 residues (513–592) reside in the cytoplasm; the C-terminal cytoplasmic tail is the FliG-binding segment (see Finding 3).

UniProt subcellular localization is given as *"Bacterial flagellum basal body"* and *"Cell membrane; Multi-pass membrane protein"*, with keywords including Flagellum, Cell membrane, and Transmembrane. This topology matches the experimentally established *Salmonella* FliF topology exactly, validating orthology-based functional transfer to the *P. putida* protein.

```
 Periplasm   [ N-domain (RBM) ]---[ linker ]---[ C-domain (RBM) ]
                |                                        |
 Membrane   ===[TM1: 40–59]==============[TM2: 494–512]===
                |                                        |
 Cytoplasm   N-term (1–39)                    C-term tail (513–592) → binds FliG
```

### Finding 6 — In *Pseudomonas*, *fliF* sits in the Class II tier of a four-tiered flagellar transcriptional hierarchy

Flagellar biogenesis in *Pseudomonas* is governed by a **four-tiered (Class I–IV) transcriptional circuit**, established by whole-genome transcriptional profiling of *fleQ*, *fleR*, *fliA*, and *rpoN* mutants in the closely related *P. aeruginosa*: *"Analysis of the transcriptomes generated for each of these mutants indicates a four-tiered (Classes I-IV) hierarchy of transcriptional regulation. Class I genes are constitutively expressed and include the transcriptional regulator fleQ and the alternative sig[ma factor]"* ([PMID: 14617143](https://pubmed.ncbi.nlm.nih.gov/14617143/)).

The circuit is driven by a dedicated regulatory set: *"Dedicated flagellar genes fleQ, fleS, fleR, fliA, flgM and fleN encode proteins that participate in the regulation of the flagellar transcriptional circuit"* ([PMID: 14617143](https://pubmed.ncbi.nlm.nih.gov/14617143/)). Class I is constitutive (master regulator FleQ, and RpoN/σ54). The basal-body/MS-ring genes, including *fliF*, are expressed early as **Class II** genes, activated by the enhancer-binding master regulator FleQ together with RpoN (σ54); FleN (a MinD-like ATPase) modulates FleQ activity to control flagellar number. This placement is fully consistent with the assembly-hierarchy role of *fliF* (Finding 4) and with the *P. putida* data (PMID 39709681) showing FlhF targets early flagellar components — including the MS-ring — to the pole and indirectly stimulates Class III promoters via FlgM secretion. Additional *Pseudomonas*-specific regulation is layered on top of this circuit; for example, the membrane regulator MorA controls the timing of flagellar development in *P. putida* ([PMID: 15489433](https://pubmed.ncbi.nlm.nih.gov/15489433/)).

---

## Mechanistic Model / Interpretation

FliF can be understood as the **keystone of the flagellar basal body** — the first brick laid, the anchor point, the pore-former, and the rotor base, all in one non-catalytic polypeptide. The following integrated model synthesizes the six findings.

**Spatial and temporal logic of assembly:**

```
  TIME →

  (1) FlhA oligomerizes in inner membrane
        │
  (2) ~34 FliF subunits recruited → self-assemble into MS-RING  ◄── EARLIEST STRUCTURE
        │        (in P. putida: targeted to the CELL POLE by FlhF/FimV)
        ├──► central pore HOUSES the fT3SS export gate (FlhA/B, FliO/P/Q/R)
        │
  (3) FliF C-terminal tail CO-FOLDS with FliG → MS:C-ring interface
        │        C-ring = FliG + FliM + FliN  →  ROTOR
        │
  (4) Export gate secretes rod → hook → (HBB complete)
        │
  (5) HBB completion → FlgM secreted out → σ28/FliA freed
        │
  (6) Late (Class IV) genes expressed → filament (flagellin) assembled
```

**Three roles in one protein.** The single MS-ring simultaneously provides: (a) a *scaffold/template* that nucleates and geometrically organizes the entire basal body; (b) a *housing/pore* that cradles the type III export gate through which all downstream axial proteins are secreted; and (c) a *rotor base* that, through FliF–FliG co-folding, mechanically couples the ion-motive-force-driven stators to rotation. The dual-conformation, symmetry-mismatched architecture (23-fold inner / 11-fold middle within a 34-mer) is what allows one protein to satisfy the differing geometric requirements of the export gate (inner core) and the rod/rotor connections (outer regions) at once.

**Regulatory coupling.** FliF is not only a structural piece but a **checkpoint**. Because late-gene expression depends on FlgM secretion, and FlgM secretion depends on a completed FliF/FliG basal body plus export apparatus, the cell only commits to making expensive filament (flagellin) once the foundation is verifiably in place. This is why *fliF* deletion collapses the RpoN- and σ28-dependent tiers of the hierarchy.

**Localization summary table:**

| Region of FliF | Compartment | Structural role |
|---|---|---|
| N-terminus (1–39) | Cytoplasm | Membrane anchoring / assembly |
| TM1 (40–59) | Inner membrane | Membrane insertion |
| N-domain + linker + C-domain (61–468) | Periplasm | Ring-building motifs (RBM); S-ring/M-ring body |
| TM2 (494–512) | Inner membrane | Membrane insertion |
| C-terminal tail (513–592) | Cytoplasm | Co-folds with FliG → rotor / torque coupling |

**Answer to the specific questions posed:**
- *Enzyme? Reaction/substrate?* — **No.** FliF is a structural protein with no catalytic activity. Its functional "substrate" is the flagellar machine it templates.
- *Transporter?* — **No,** but it *houses* the type III export gate that transports axial flagellar subunits.
- *Structural/adapter role?* — **Yes.** It is the founding scaffold of the basal body and the rotor base; it adapts the membrane MS-ring to the cytoplasmic C-ring via FliG co-folding.
- *Localization?* — Inner (cytoplasmic) membrane, at the flagellar basal body, positioned at the cell pole in *P. putida*.
- *Pathway?* — Flagellar biogenesis and bacterial motility/chemotaxis; a Class II gene in the FleQ/σ54-driven *Pseudomonas* flagellar transcriptional circuit.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|---|---|---|
| [34244518](https://pubmed.ncbi.nlm.nih.gov/34244518/) | *Native flagellar MS ring is formed by 34 subunits with 23-fold and 11-fold subsymmetries* | Cryo-EM: MS-ring is the transmembrane core and assembly template; 34 FliF subunits; inner 23-subunit core forms a pore sized for the export gate (Findings 1, 2) |
| [33653894](https://pubmed.ncbi.nlm.nih.gov/33653894/) | *Two Distinct Conformations in 34 FliF Subunits...* | Defines FliF domain architecture, membrane localization, earliest-assembly and export-gate-housing roles (Findings 1, 5) |
| [24450479](https://pubmed.ncbi.nlm.nih.gov/24450479/) | *Assembly and stoichiometry of FliF and FlhA...* | Places the fT3SS export apparatus (FlhA/B, FliO/P/Q/R) in the FliF central pore (Finding 2) |
| [11160096](https://pubmed.ncbi.nlm.nih.gov/11160096/) | *Intergenic suppression between FliF and FlhA* | Genetic evidence for a direct FliF–FlhA functional interaction (Finding 2) |
| [28089452](https://pubmed.ncbi.nlm.nih.gov/28089452/) | *Co-Folding of a FliF-FliG Split Domain...* | The MS:C-ring interface couples torque to rotation via FliF–FliG co-folding (Finding 3) |
| [30082903](https://pubmed.ncbi.nlm.nih.gov/30082903/) | *A coevolution-guided model for the rotor...* | FliF–FliG fusion assembles rings; FliF is the rotor's periplasmic hub (Finding 3) |
| [30940700](https://pubmed.ncbi.nlm.nih.gov/30940700/) | *Novel Insights into...the Flagellar Switch Complex* | States rotor = MS-ring (FliF) + C-ring (FliG/FliM/FliN) (Finding 3) |
| [21244534](https://pubmed.ncbi.nlm.nih.gov/21244534/) | *Assembly and stability of flagellar motor in E. coli* | FliF recruited at earliest ordered assembly step, after FlhA (Finding 4) |
| [25825427](https://pubmed.ncbi.nlm.nih.gov/25825427/) | *Basal Body Structures...RpoN- and FliA-Dependent Genes in H. pylori* | *fliF* is early; its deletion eliminates RpoN-dependent transcripts (Finding 4) |
| [39709681](https://pubmed.ncbi.nlm.nih.gov/39709681/) | *Spatial, temporal and numerical regulation of polar flagella in P. putida* | FlhF targets early flagellar components (MS-ring) to the pole in *P. putida* (Findings 4, 6) |
| [14617143](https://pubmed.ncbi.nlm.nih.gov/14617143/) | *Four-tiered transcriptional regulatory circuit...P. aeruginosa* | Establishes the four-tiered *Pseudomonas* flagellar hierarchy and its regulators; places *fliF* as a Class II target (Finding 6) |
| [16113269](https://pubmed.ncbi.nlm.nih.gov/16113269/) | *Role of FliF and FliI of L. monocytogenes...* | ΔfliF abolishes motility and flagella production (supports essentiality, Finding 4) |
| [10960117](https://pubmed.ncbi.nlm.nih.gov/10960117/) | *Mutational analysis of early flagellar genes of H. pylori* | *fliF* mutation → nonmotile, nonflagellate; reduced flaA transcription (assembly checkpoint, Finding 4) |
| [25313396](https://pubmed.ncbi.nlm.nih.gov/25313396/) | *FlgM is secreted by the flagellar export apparatus in B. subtilis* | FlgM secretion requires FliF/FliG basal body + export apparatus, linking assembly to late-gene expression (Finding 4) |

**Supporting context papers** (mechanism of the machine FliF anchors): reviews and studies on flagellar type III export ([PMID: 18931786](https://pubmed.ncbi.nlm.nih.gov/18931786/), [PMID: 15170399](https://pubmed.ncbi.nlm.nih.gov/15170399/), [PMID: 31172377](https://pubmed.ncbi.nlm.nih.gov/31172377/), [PMID: 35602071](https://pubmed.ncbi.nlm.nih.gov/35602071/)), the flagellar motor ([PMID: 18848888](https://pubmed.ncbi.nlm.nih.gov/18848888/)), the FliO chaperone role in export-gate assembly ([PMID: 28771474](https://pubmed.ncbi.nlm.nih.gov/28771474/)), and *Pseudomonas*-specific flagellar regulation ([PMID: 15489433](https://pubmed.ncbi.nlm.nih.gov/15489433/), on MorA controlling flagellar timing in *P. putida*).

**Convergence and consistency.** The evidence is highly convergent. The structural (cryo-EM), genetic (intergenic suppression, deletion phenotypes), biochemical (co-folding, fusion assembly), and localization (FliF-YFP puncta) lines of evidence independently support the same model. No cited study contradicts the FliF-as-MS-ring assignment. The main caveat is that most *mechanistic* detail derives from model enterobacteria (*Salmonella*, *E. coli*) and other species (*H. pylori*, *B. subtilis*, *Listeria*, *Vibrio*), with *P. putida*-specific data limited to regulatory/localization studies.

---

## Limitations and Knowledge Gaps

1. **Orthology-based functional transfer.** The detailed mechanistic roles of FliF (34-subunit stoichiometry, dual conformations, export-gate housing, FliG co-folding, FlhA suppression) are established in *Salmonella*, *E. coli*, and other model organisms — **not directly in *P. putida***. The functional assignment for Q88ET4 rests on strong sequence/topology conservation (Finding 5) plus the general universality of the flagellar basal body, but no *P. putida*-specific cryo-EM structure or FliF–FliG interaction study was found.

2. **Exact stoichiometry in *P. putida* is unknown.** Reported FliF copy numbers vary in the literature (e.g., 26 in one export-gate study, 34 in native cryo-EM). Whether the *P. putida* MS-ring is a 34-mer has not been measured directly.

3. **No *P. putida* ΔfliF phenotype in the reviewed literature.** Essentiality for motility is inferred from *H. pylori*, *Listeria*, and general assembly logic; a targeted *P. putida* KT2440 *fliF* knockout characterization was not located, though the *P. putida* polar-flagella regulation study (PMID 39709681) situates the MS-ring in the pathway.

4. **Species-specific regulatory wiring.** The four-tiered hierarchy (Finding 6) was defined in *P. aeruginosa*. *P. putida* is expected to share this architecture, but the precise promoter architecture and FleQ/σ54 dependence of the *P. putida fliF* promoter has not been experimentally mapped in the reviewed set.

5. **Interpretation of the AMP-bd_C_sf (IPR045851) domain annotation.** This InterPro superfamily signature appears in the target's domain list but is best interpreted as a structural-fold homology (the AMP-binding C-terminal-like fold) rather than an indication of AMP-binding catalytic activity; there is no evidence FliF binds AMP or catalyzes a reaction. This should be flagged as a potentially misleading automated annotation.

---

## Proposed Follow-up Experiments / Actions

1. **Direct *P. putida* KT2440 Δ*fliF* knockout.** Construct a clean deletion and assay swimming/swarming motility, flagellar staining/EM, and flagellin (FliC) secretion to confirm essentiality and checkpoint behavior in this organism specifically.

2. **Cryo-EM / cryo-ET of the native *P. putida* polar basal body.** Determine the actual FliF stoichiometry and confirm the S-ring/M-ring dual-conformation architecture in a polar-flagellate context.

3. **FliF–FliG interaction validation in *P. putida*.** Test co-folding/interaction of the Q88ET4 C-terminal tail with the *P. putida* FliG N-terminal domain (e.g., bacterial two-hybrid, co-purification, or a FliF–FliG fusion complementation assay) to confirm the rotor interface.

4. **Map the *fliF* (PP_4369) promoter.** Use RNA-seq/primer extension in *fleQ*, *rpoN*, and *fliA* mutant backgrounds to confirm Class II assignment and FleQ/σ54 dependence in *P. putida*.

5. **Polar-targeting dependency test.** Localize a fluorescent FliF fusion in wild-type vs. Δ*flhF* / Δ*fimV* backgrounds to confirm that FliF MS-ring positioning drives unipolar flagellation in *P. putida* (extending PMID 39709681).

6. **Correct the AMP-binding annotation.** Recommend that downstream annotation pipelines treat IPR045851 in this protein as a fold-level signature, not evidence of enzymatic AMP binding, to avoid propagating a spurious catalytic annotation.

---

## Conclusion

FliF (Q88ET4, PP_4369) is unambiguously the **flagellar M-ring/MS-ring protein** of *Pseudomonas putida* KT2440 — a non-catalytic, integral inner-membrane structural protein that self-assembles into the transmembrane MS-ring, the earliest-formed and foundational component of the flagellar basal body. It serves simultaneously as the assembly template for the whole flagellum, the housing for the type III secretion export gate, and the rotor base that couples torque to rotation via co-folding with FliG. It functions at the base of the polar flagellum in the inner membrane, is targeted to the cell pole by FlhF, is essential for motility, and is expressed early as a Class II gene in the FleQ/σ54-driven *Pseudomonas* flagellar regulatory hierarchy. The gene identity, organism, family, and domains all match the UniProt record, and the functional assignment is supported by convergent structural, genetic, biochemical, and bioinformatic evidence.


## Artifacts

- [OpenScientist final report](fliF-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](fliF-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:34244518
2. PMID:33653894
3. PMID:24450479
4. PMID:11160096
5. PMID:28089452
6. PMID:30082903
7. PMID:30940700
8. PMID:21244534
9. PMID:10960117
10. PMID:16113269
11. PMID:25825427
12. PMID:25313396
13. PMID:39709681
14. PMID:14617143
15. PMID:15489433
16. PMID:18931786
17. PMID:15170399
18. PMID:31172377
19. PMID:35602071
20. PMID:18848888
21. PMID:28771474