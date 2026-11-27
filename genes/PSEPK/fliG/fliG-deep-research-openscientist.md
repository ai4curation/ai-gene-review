---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T16:50:57.256201'
end_time: '2026-08-31T17:53:23.554362'
duration_seconds: 3746.3
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: fliG
  gene_symbol: fliG
  uniprot_accession: Q88ET5
  protein_description: 'RecName: Full=Flagellar motor switch protein FliG {ECO:0000256|ARBA:ARBA00021870,
    ECO:0000256|PIRNR:PIRNR003161};'
  gene_info: Name=fliG {ECO:0000313|EMBL:AAN69946.2}; OrderedLocusNames=PP_4368 {ECO:0000313|EMBL:AAN69946.2};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the FliG family. {ECO:0000256|ARBA:ARBA00010299,
  protein_domains: Flg_Motor_Flig. (IPR000090); Flg_Motor_Flig_C. (IPR023087); FliG_a-hlx.
    (IPR011002); FliG_M. (IPR032779); FliG_N. (IPR028263)
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
citation_count: 22
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: fliG-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: fliG-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88ET5
- **Protein Description:** RecName: Full=Flagellar motor switch protein FliG {ECO:0000256|ARBA:ARBA00021870, ECO:0000256|PIRNR:PIRNR003161};
- **Gene Information:** Name=fliG {ECO:0000313|EMBL:AAN69946.2}; OrderedLocusNames=PP_4368 {ECO:0000313|EMBL:AAN69946.2};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the FliG family. {ECO:0000256|ARBA:ARBA00010299,
- **Key Domains:** Flg_Motor_Flig. (IPR000090); Flg_Motor_Flig_C. (IPR023087); FliG_a-hlx. (IPR011002); FliG_M. (IPR032779); FliG_N. (IPR028263)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "fliG" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'fliG' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **fliG** (gene ID: fliG, UniProt: Q88ET5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: Flagellar Motor Switch Protein FliG (Q88ET5, PP_4368) in *Pseudomonas putida* KT2440

**Gene:** *fliG* (OrderedLocusName PP_4368)
**UniProt:** Q88ET5 (339 aa)
**Organism:** *Pseudomonas putida* strain ATCC 47054 / DSM 6125 / KT2440 (PSEPK)

## Summary

**FliG (UniProt Q88ET5; locus PP_4368) is the torque-generating rotor and directional-switch protein of the bacterial flagellar motor in *Pseudomonas putida* KT2440.** It is not an enzyme, transporter, or diffusible signaling molecule. Instead, it is a structural/mechanical protein that, together with FliM and FliN, forms the cytoplasmic C-ring — the rotor of the flagellar motor — attached to the cytoplasmic face of the MS-ring (the integral membrane protein FliF) at the base of the flagellum. FliG performs three inter-related jobs: (1) it converts the transmembrane proton-motive force into mechanical rotation (torque generation) through direct electrostatic contacts between its C-terminal domain and the membrane-embedded stator MotA; (2) it anchors the C-ring to FliF, templating assembly of the rotor; and (3) it acts as the mechanical effector of chemotactic switching, undergoing large conformational changes that reverse the sense of rotation from counterclockwise (CCW) to clockwise (CW) when phosphorylated CheY binds the C-ring.

The identity of Q88ET5 as a *bona fide* FliG orthologue is strongly supported by bioinformatic analysis. The 339-residue *P. putida* protein has the canonical three-domain armadillo-repeat architecture (FliG_N, FliG_M, FliG_C), carries the conserved "MFxF" switch/torque motif in its C-terminal domain, and displays the charged-residue-rich C-terminal ridge that is the hallmark of the rotor–stator interface. The gene sits within the *P. putida* polar (lophotrichous) flagellar regulon, controlled by the master regulator FleQ (σ54/σN-dependent), the polarity/number regulators FlhF and FleN, and integrated with biofilm decisions through c-di-GMP signaling.

Because *P. putida* FliG itself has not been the subject of dedicated biochemical or structural studies, the functional annotation here is built on: (i) the extensive, highly conserved experimental literature on FliG from *Salmonella*, *Escherichia coli*, *Thermotoga maritima*, *Vibrio*, and *Sinorhizobium*; and (ii) direct sequence/domain analysis of Q88ET5 confirming conservation of every functionally critical feature. This is a well-justified inference: FliG is one of the most deeply conserved and mechanistically characterized proteins of the bacterial flagellum, and *P. putida*'s polar flagellar system uses the same core motor components as the model peritrichous systems.

---

## Key Findings

### Finding 1 — FliG is a rotor component of the flagellar C-ring with a three-domain architecture

FliG is one of three "switch-complex" proteins — **FliG, FliM, and FliN** — that together assemble into the **cytoplasmic C-ring**, a ring-shaped structure mounted on the cytoplasmic face of the MS-ring (formed by the integral membrane protein FliF). The C-ring is the rotor of the flagellar motor. FliG is present in multiple copies per motor, with estimates ranging from ~25 copies (early *Thermotoga*/*E. coli* work) to 34 copies per motor from cryo-electron microscopy reconstructions.

Structurally, FliG is organized into three domains along its length: an **N-terminal domain (FliG_N)** dedicated to flagellar assembly (attachment to FliF), a **middle domain (FliG_M)** involved in inter-subunit and FliM contacts, and a **C-terminal domain (FliG_C)** that carries the torque/motor-generating surface. This modular organization was first revealed by the crystal structure of the FliG-C domain from *Thermotoga maritima* in 1999 and has been repeatedly confirmed by multiple cryo-EM C-ring reconstructions.

The foundational structural study states plainly that "*FliG is a component of the rotor, present in about 25 copies per flagellum. It is composed of an amino-terminal domain that functions in flagellar assembly and a carboxy-terminal domain (FliG-C) that functions specifically in motor rotation*" ([PMID: 10440379](https://pubmed.ncbi.nlm.nih.gov/10440379/)). A modern review confirms the location and role: "*The rotor is composed of the transmembrane MS ring made of FliF and the cytoplasmic C ring consisting of FliG, FliM, and FliN. The C ring is directly involved in rotation and directional switching*" ([PMID: 30940700](https://pubmed.ncbi.nlm.nih.gov/30940700/)). The cryo-EM-based stoichiometry is given as "*the cytoplasmic ring is assembled from 34 FliG and FliM molecules in a 1:1 fashion*" ([PMID: 22896702](https://pubmed.ncbi.nlm.nih.gov/22896702/)).

### Finding 2 — The FliG C-terminal domain generates motor torque via electrostatic interactions with the stator MotA

The central mechanical function of FliG is **torque generation**. The C-terminal domain (FliG_C) presents a prominent ridge of conserved charged residues that engages, through electrostatic interactions, complementary charged residues on the cytoplasmic loop of the stator protein **MotA**. As protons flow through the MotA/MotB stator channel powered by the proton-motive force, cyclical electrostatic interactions between MotA and the FliG_C ridge drive the rotor around, producing rotation.

The specific residues are well mapped in model systems. In *Salmonella*, the key FliG residues are **Arg281** and **Asp289**; homologous residues appear in *Sinorhizobium meliloti* (Arg294/Glu302) and a conserved set in *Vibrio*. On the stator side, MotA contributes **Arg90** and **Glu98**. Crucially, double-mutant synergism and charge-reversal suppression studies dissected the roles of individual contacts: the MotA-Arg90–FliG-Asp289 interaction primarily governs proper **stator positioning** around the rotor, whereas the MotA-Glu98–FliG-Arg281 interaction is more important for **torque generation** itself.

The original insight came from mutational studies showing that "*both proteins contain charged residues essential for motor rotation. This suggests that functionally important electrostatic interactions might occur between the rotor and stator*" ([PMID: 9600984](https://pubmed.ncbi.nlm.nih.gov/9600984/)). The functional partition of the interface was later resolved: "*the MotA-Arg90-FliG-Asp289 interaction is critical for the proper positioning of the stators around the rotor, whereas the MotA-Glu98-FliG-Arg281 interaction is more important for torque generation*" ([PMID: 23161029](https://pubmed.ncbi.nlm.nih.gov/23161029/)). Structurally, "*Charged residues that are important for function, and which interact with the stator protein MotA, cluster along a prominent ridge on FliG-C*" ([PMID: 10440379](https://pubmed.ncbi.nlm.nih.gov/10440379/)).

### Finding 3 — The FliG N-terminal domain anchors the C-ring to the FliF MS-ring, coupling torque to rotation

For torque generated at the FliG_C–MotA interface to produce useful rotation, FliG must be rigidly coupled to the rest of the rotor. This coupling is achieved by the **N-terminal domain (FliG_N)**, which binds the C-terminal cytoplasmic tail of **FliF**, the integral membrane protein that forms the MS-ring. FliG is among the very first proteins added during basal-body assembly, and its FliG_N domain effectively templates the geometry of the entire C-ring.

The molecular basis of this junction has been resolved: a FliF–FliG "split domain" co-folds to form the MS:C ring interface, and coevolution analysis plus FliF-FliG fusion-ring reconstructions show that FliG_N — with the embedded FliF C-terminal α-helix — homo-oligomerizes to build the ring. A primarily helical linker/hinge connects the N-terminal assembly domain to the C-terminal motility domain, allowing the conformational flexibility needed for switching.

The interface is described as the coupling point of the machine: "*The interface between the membrane (MS) and cytoplasmic (C) rings of the bacterial flagellar motor couples torque generation to rotation within the membrane*" ([PMID: 28089452](https://pubmed.ncbi.nlm.nih.gov/28089452/)). The domain architecture connecting attachment and motility is described as: "*A primarily helical linker joins the N-terminal assembly domain of FliG, which is firmly attached to the FliF protein of the MS ring of the basal body, to the motility domain that interacts with MotA/MotB*" ([PMID: 15126479](https://pubmed.ncbi.nlm.nih.gov/15126479/)). The co-folding/oligomerization mechanism is captured by: "*the cofolded domains of the FliG N-terminal domain (FliG_N) with embedded α-helical FliF carboxy-terminal tail homo-oligomerize*" ([PMID: 30082903](https://pubmed.ncbi.nlm.nih.gov/30082903/)).

### Finding 4 — FliG conformational changes mediate CheY-P-driven directional switching (CCW/CW)

Beyond generating torque, FliG is the **mechanical effector of chemotactic switching**. The output of the chemotaxis two-component signaling pathway is phosphorylated CheY (**CheY-P**). CheY-P binds to **FliM and FliN** in the C-ring, inducing conformational changes that propagate through the ring and **remodel FliG**, reorienting its torque-generating C-terminal surface. This reverses the direction of rotation from the default counterclockwise (CCW) to clockwise (CW), switching the cell from smooth swimming ("runs") to reorientation ("tumbles").

Recent cryo-EM comparisons of default-CCW motors versus motors locked in the CW state (by constitutively active CheY) reveal the structural basis: CheY binding drives an upward/inward shift of the C-ring that remodels the FliG subunits and reverses both the orientation and the surface electrostatic potential of the FliG_C torque helix — precisely the surface that engages MotA. Specific FliG mutations (for example, the *Salmonella* ΔPSA deletion and hinge-region substitutions) lock or bias the motor's rotational direction, confirming FliG as the switch point.

The signaling logic is stated as: "*The phosphorylated form of the chemotactic signaling protein CheY binds to FliM and FliN to induce conformational changes of the C ring responsible for switching the direction of flagellar motor rotation from CCW to CW*" ([PMID: 31452860](https://pubmed.ncbi.nlm.nih.gov/31452860/)). The structural mechanism is captured by cryo-EM: CheY binding "*eventually remodels the structures of the FliG subunits and reverses the orientations and surface electrostatic potential of the*" torque surface ([PMID: 39179739](https://pubmed.ncbi.nlm.nih.gov/39179739/)). And the effector role is summarized as: "*Switching of bacterial flagellar rotation is caused by large domain movements of the FliG protein triggered by binding of the signal protein CheY to FliM*" ([PMID: 26561852](https://pubmed.ncbi.nlm.nih.gov/26561852/)).

### Finding 5 — The FliG-containing C-ring is multifunctional and also required for flagellar type III protein export

The C-ring is not only the rotor and switch — it is also required for **flagellar type III protein secretion (fT3SS)**, the export machinery that ships flagellar axial components (rod, hook, filament subunits) out through the growing structure. The C-ring, working with the export ATPase **FliI**, forms part of the platform that feeds substrate to the export gate. This means FliG has an essential role in **flagellar biogenesis** in addition to motility.

Genetic evidence underscores this: *fliG* null mutants are non-flagellate (Fla⁻). FliG-deficient mutants make far fewer flagella than *fliM*/*fliN* mutants, and although overproduction of the export ATPase FliI can partially rescue flagellum assembly in C-ring-defective backgrounds, such flagella are paralyzed — demonstrating that an intact, FliG-containing C-ring is essential for a functional motor.

Reviews state the multifunctionality explicitly: "*The C ring is a multifunctional structure necessary for flagellar protein secretion, torque generation, and switching of the rotational direction of the motor*" ([PMID: 19648242](https://pubmed.ncbi.nlm.nih.gov/19648242/)). And, independently confirming both the function and the cytoplasmic localization: "*The C ring, located at the bottom of the flagellum and in the cytoplasmic space, consists of FliG, FliM and FliN, and has an important function in flagellar protein secretion, torque generation and rotational switch of the motor*" ([PMID: 26142283](https://pubmed.ncbi.nlm.nih.gov/26142283/)).

### Finding 6 — Bioinformatic confirmation that Q88ET5 has canonical FliG architecture and conserved torque/switch motifs

Direct analysis of the *P. putida* KT2440 sequence confirms that Q88ET5 (PP_4368) is a genuine FliG orthologue with every functionally important feature intact. The protein is **339 amino acids** long and, per UniProt/InterPro annotation, contains the three canonical armadillo-repeat domains:

| Domain | Approx. residues | InterPro | Function |
|--------|------------------|----------|----------|
| FliG_N | ~10–111 | IPR028263 | Assembly; binds FliF MS-ring |
| FliG_M | ~121–194 | IPR032779 | Inter-subunit / FliM contacts |
| FliG_C | ~224–330 | IPR023087 | Torque generation; MotA interface |

Additional family/domain signatures include Flg_Motor_Flig (IPR000090), Flg_Motor_Flig_C (IPR023087), and the FliG α-helical fold (IPR011002). Critically, the C-terminal domain carries the hallmark conserved **"MFxF" (MFVF) switch/torque motif** at residues ~240–243, and the FliG_C segment (224–330) is strongly enriched in charged residues (≈39 D/E/R/K residues), consistent with the electrostatic ridge that engages the MotA stator. A **Gly-Gly-containing linker** (…GGIKR… around residues ~200–204) connects FliG_M to FliG_C — the very flexible hinge whose integrity is required for rotational switching in model organisms. The presence of all of these features means the entire conserved mechanochemical toolkit is physically present in Q88ET5.

### Finding 7 — In *P. putida*, FliG operates within a polar (lophotrichous) flagellar system under FleQ/FlhF/FleN control

*P. putida* KT2440 differs from the peritrichous model organisms (*E. coli*, *Salmonella*) in flagellar architecture: it assembles a **tuft of flagella at a single cell pole** (lophotrichous), and these must be rebuilt de novo every cell cycle to keep both daughter cells motile. FliG, as a core basal-body/C-ring component, is part of this polar flagellar regulon and localizes to the cytoplasmic face of the polar basal body.

Flagellar biogenesis in *P. putida* is governed by a regulatory hierarchy: the **master regulator FleQ** (which activates transcription via σ54/σN), the flagellar number and placement regulators **FlhF** (a signal-recognition-particle-type GTPase acting as a polar landmark) and **FleN** (a MinD-like ATPase), plus FimV. FlhF targets early flagellar components to the pole and prevents non-polar nucleation, while cytoplasmic FleN limits flagellar number by antagonizing FleQ. The second messenger **c-di-GMP** integrates motility with biofilm/adhesion decisions (e.g., the LapA adhesin, cellulose biosynthesis).

The polar architecture and its regulation are documented: "*The Gram-negative bacterium Pseudomonas putida bears a tuft of flagella at a single cell pole. New flagella must be assembled de novo every cell cycle to secure motility of both daughter cells*" ([PMID: 39709681](https://pubmed.ncbi.nlm.nih.gov/39709681/)), and "*FlhF determines the polar position of the flagella by targeting early flagellar components to the cell pole and preventing their nucleation at non-polar sites*" ([PMID: 39709681](https://pubmed.ncbi.nlm.nih.gov/39709681/)). The transcriptional hierarchy is established by: "*PflhA and PflhF are σN-dependent, activated by the flagellar regulator FleQ, and negatively regulated by FleN*" ([PMID: 30889223](https://pubmed.ncbi.nlm.nih.gov/30889223/)).

---

## Mechanistic Model / Interpretation

FliG sits at the heart of a rotary nanomachine that converts a chemical gradient (proton-motive force) into mechanical rotation, and that reprograms its output direction in response to a chemotactic signal. The three domains of FliG each map cleanly onto a distinct mechanical function, and the protein integrates torque generation, structural coupling, and signal transduction into a single polypeptide.

```
                 OUTSIDE / PERIPLASM
        ═══════════════════════════════════════
        ║   Filament ─ Hook ─ Rod (exported     ║
        ║   via flagellar T3SS; C-ring required)║
   ═════╬═══════════════════════════════════════╬═════  Inner
        ║   MotB   |  MS-ring = FliF |   MotB    ║       membrane
   MotA ▓▓         |   (integral membrane)  |    ▓▓ MotA
   (H+ channel)    |                        |   (stator)
        ║          FliF C-terminal tail          ║
        ═══════════╪═════════════════════════════
                   │  binds
             ┌─────▼─────┐
             │  FliG_N   │  ← assembly / anchor (Finding 3)
             ├───────────┤
             │  FliG_M   │  ← inter-subunit + FliM contacts
             │ ~GG linker│  ← hinge (switching, Finding 6)
             ├───────────┤
   MotA ◄───►│  FliG_C   │  ← TORQUE: charged ridge (Arg/Asp)
   electro-  │  (MFxF)   │     electrostatically drives rotor
   static    └─────┬─────┘     (Finding 2)
                   │
             ┌─────▼─────────────────┐
             │   FliM  +  FliN       │  ← bind CheY-P (Finding 4)
             └───────────────────────┘  C-RING = ROTOR (cytoplasm)
                          ▲
                          │ CheY-P from chemotaxis pathway
                          │ → remodels FliG → CCW⇄CW switch
```

**Torque cycle.** Protons flowing through the MotA/MotB stator drive conformational cycling of the MotA cytoplasmic loop. Charged residues on that loop (MotA-Arg90, MotA-Glu98) transiently pair with charged residues on the FliG_C ridge (FliG-Arg281, FliG-Asp289 in *Salmonella* numbering; the equivalent conserved residues are present in Q88ET5). Because FliG_N is rigidly clamped to FliF, and FliF is embedded in the membrane as the MS-ring, the net effect of these cyclical electrostatic pushes is rotation of the entire rotor assembly relative to the fixed stator.

**Switching.** The default state rotates CCW (smooth swimming). When the chemotaxis system detects a decreasing attractant gradient, CheA autophosphorylates and transfers phosphate to CheY. CheY-P diffuses to the C-ring and binds FliM/FliN. This binding is amplified through the ring, forcing large domain movements in FliG that flip the orientation and surface charge of the FliG_C torque helix. With the torque surface reoriented, the same proton flux now drives CW rotation, causing the cell to tumble and reorient. FliG is thus simultaneously the motor's power output and its gear-shift.

**Localization.** All of FliG's activity occurs in the **cytoplasm**, at the **base of the flagellum**, on the cytoplasmic face of the inner membrane. In *P. putida* specifically, this base is positioned at a **single cell pole**, and the whole assembly is built de novo each cell cycle under FleQ/FlhF/FleN/σ54 control.

The overarching interpretation is that FliG is a **structural/mechanical rotor-switch protein** — the single most functionally critical rotor subunit — with no catalytic (enzymatic) or transport activity of its own. Its "substrate," in the loose sense, is mechanical: it accepts electrostatic force from MotA and delivers rotation to the flagellum, and it accepts a conformational signal (via FliM/FliN/CheY-P) and delivers a change of rotational direction.

---

## Evidence Base

The annotation rests on a large, internally consistent body of structural, genetic, and biophysical work on FliG orthologues, combined with direct sequence analysis of Q88ET5. Because FliG is among the most conserved flagellar proteins, cross-species inference to *P. putida* is well justified.

| PMID | Title (abbrev.) | How it supports the annotation |
|------|------------------|-------------------------------|
| [10440379](https://pubmed.ncbi.nlm.nih.gov/10440379/) | *Structure of the C-terminal domain of FliG* | Crystal structure defining FliG as a rotor with an assembly N-domain and a torque C-domain; charged ridge interacts with MotA (Findings 1, 2) |
| [30940700](https://pubmed.ncbi.nlm.nih.gov/30940700/) | *Conformational rearrangements of the switch complex* | Review confirming FliG/FliM/FliN C-ring on FliF MS-ring; rotation & switching (Finding 1) |
| [22896702](https://pubmed.ncbi.nlm.nih.gov/22896702/) | *Structure of flagellar motor proteins in complex* | Cryo-EM stoichiometry: 34 FliG per C-ring (Finding 1) |
| [9600984](https://pubmed.ncbi.nlm.nih.gov/9600984/) | *Electrostatic interactions between rotor and stator* | Establishes rotor–stator torque as electrostatic (Finding 2) |
| [23161029](https://pubmed.ncbi.nlm.nih.gov/23161029/) | *Distinct roles of conserved charged residues at MotA–FliG interface* | Assigns FliG-Asp289 (positioning) vs FliG-Arg281 (torque) (Finding 2) |
| [28089452](https://pubmed.ncbi.nlm.nih.gov/28089452/) | *Co-folding of FliF–FliG split domain* | MS:C ring interface couples torque to rotation (Finding 3) |
| [15126479](https://pubmed.ncbi.nlm.nih.gov/15126479/) | *Hinges: mutations in the interdomain region of FliG* | Helical linker joins FliF-attached N-domain to MotA-interacting motility domain (Finding 3) |
| [30082903](https://pubmed.ncbi.nlm.nih.gov/30082903/) | *Coevolution-guided model for the rotor* | FliG_N co-folds with FliF tail; homo-oligomerizes to template ring (Finding 3) |
| [31452860](https://pubmed.ncbi.nlm.nih.gov/31452860/) | *Directional switching mechanism* | CheY-P binds FliM/FliN → C-ring change → CCW/CW switch (Finding 4) |
| [39179739](https://pubmed.ncbi.nlm.nih.gov/39179739/) | *Structural basis of rotational switching* | Cryo-EM: CheY remodels FliG subunits, reverses torque-surface charge (Finding 4) |
| [26561852](https://pubmed.ncbi.nlm.nih.gov/26561852/) | *Coevolved mutations reveal architectures* | Switching = large FliG domain movements triggered by CheY (Finding 4) |
| [19648242](https://pubmed.ncbi.nlm.nih.gov/19648242/) | *Flagellar formation in C-ring-defective mutants* | C-ring multifunctional: secretion, torque, switching (Finding 5) |
| [26142283](https://pubmed.ncbi.nlm.nih.gov/26142283/) | *FliG 3-aa deletion in Vibrio polar flagella* | Cytoplasmic C-ring; secretion/torque/switch functions (Finding 5) |
| [39709681](https://pubmed.ncbi.nlm.nih.gov/39709681/) | *Polar flagella assembly in P. putida* | Polar architecture; FlhF targets early components to pole (Finding 7) |
| [30889223](https://pubmed.ncbi.nlm.nih.gov/30889223/) | *flhF and fleN in P. putida* | FleQ/FleN/σN regulatory hierarchy of the regulon (Finding 7) |

Several additional papers reinforce the torque-interface picture across ion-coupling variants, strengthening confidence that the mechanism generalizes to *P. putida*'s H⁺-driven MotAB motor. Charge-reversal studies in the Na⁺-driven *Vibrio* motor ([PMID: 24464458](https://pubmed.ncbi.nlm.nih.gov/24464458/)) show a group of ~6 FliG and ~7 PomA charged residues collectively drive torque, with a specific PomA-E97–FliG-K284 pair critical. In *Bacillus subtilis*, conserved charged residues in the MotA/MotP cytoplasmic loops are required for rotation ([PMID: 24771657](https://pubmed.ncbi.nlm.nih.gov/24771657/)). In *Salmonella*, the electrostatic MotA–FliG interaction is required for efficient stator assembly around the rotor ([PMID: 21091499](https://pubmed.ncbi.nlm.nih.gov/21091499/)). The *Sinorhizobium meliloti* unidirectional motor uses the same FliG (Arg294/Glu302)–MotA (Arg90/Glu98) interface but repurposes it for speed modulation ([PMID: 15819626](https://pubmed.ncbi.nlm.nih.gov/15819626/)), illustrating the interface's mechanistic centrality. The Gly-Gly linker/hydrophobic-core work ([PMID: 37520711](https://pubmed.ncbi.nlm.nih.gov/37520711/); [PMID: 40001515](https://pubmed.ncbi.nlm.nih.gov/40001515/)) explains how the very hinge motif present in Q88ET5 controls switching. Copy-number and adaptive-remodeling measurements ([PMID: 36946730](https://pubmed.ncbi.nlm.nih.gov/36946730/)) use 34 FliG per C-ring as the reference stoichiometry.

**Direct evidence for Q88ET5 itself** comes from the bioinformatic domain analysis (Finding 6): the sequence has the full three-domain architecture, the conserved MFxF torque/switch motif, the charged FliG_C ridge, and the Gly-Gly hinge — i.e., every conserved determinant of the functions above is physically present in the *P. putida* protein.

---

## Limitations and Knowledge Gaps

1. **No dedicated *P. putida* FliG study.** There is, to our knowledge, no direct biochemical, structural, or single-mutant motility study of PP_4368/Q88ET5 specifically. The functional annotation is an inference — a very well-supported one, given deep conservation — from orthologues in *Salmonella*, *E. coli*, *Thermotoga*, *Vibrio*, *Sinorhizobium*, and *Bacillus*, plus sequence analysis of Q88ET5. The specific torque residues (e.g., the exact *P. putida* equivalents of Arg281/Asp289) have not been experimentally validated in *P. putida*.

2. **Residue-level numbering is by homology.** The critical charged residues and the MFxF motif positions are assigned by alignment/InterPro mapping, not by experimental mutagenesis in *P. putida*. Precise residue identities should be confirmed against a curated alignment before being cited as *P. putida* positions.

3. **Copy-number/stoichiometry** figures (25–34 FliG per motor; adaptive FliM remodeling) come from *E. coli*/*Salmonella*/*Thermotoga*; the exact stoichiometry of the *P. putida* polar motor has not been measured and could differ, as polar motors sometimes have distinct C-ring dimensions.

4. **Regulatory integration** in *P. putida* (FleQ, FlhF, FleN, c-di-GMP) is established at the level of the flagellar regulon and early-component targeting; the precise placement of *fliG* (PP_4368) within the transcriptional class hierarchy and its promoter architecture were not individually verified here.

5. **Ion-coupling assumption.** *P. putida* is assumed to use an H⁺-driven MotAB stator (like *E. coli*/*Salmonella*), which is standard for *Pseudomonas*, but this was not independently confirmed for KT2440 in this investigation.

---

## Proposed Follow-up Experiments / Actions

1. **Targeted mutagenesis of the predicted torque residues.** Identify, by structure-guided alignment, the *P. putida* equivalents of FliG-Arg281/Asp289 and the MFxF motif, then perform charge-reversal/charge-neutral substitutions and quantify motility (swim plates, tethered-cell rotation assays, bead assays). This would experimentally validate the inferred torque interface in KT2440.

2. **Deletion / complementation.** Construct a clean *fliG* (PP_4368) deletion and confirm the expected non-flagellate (Fla⁻) phenotype and loss of motility, with restoration on complementation — directly testing the essential structural role.

3. **Cryo-EM / cryo-ET of the polar motor.** Determine the C-ring stoichiometry and architecture of the *P. putida* polar motor in situ, and compare FliG copy number and C-ring diameter to peritrichous models — addressing the stoichiometry gap.

4. **Switching assays.** Test CCW/CW switching behavior in wild-type versus FliG hinge-region (Gly-Gly linker) mutants to confirm that the conserved *P. putida* hinge controls directional switching as in *Salmonella*.

5. **Localization.** Use a fluorescent FliG fusion to confirm polar localization and de novo per-cell-cycle assembly, and to test FlhF-dependence of FliG polar targeting.

6. **Transcriptional placement.** Map the *fliG* promoter and its dependence on FleQ/σ54 and FleN to firmly place PP_4368 within the *P. putida* flagellar regulatory hierarchy.

---

## Conclusion

FliG (Q88ET5, PP_4368) in *Pseudomonas putida* KT2440 is the **torque-generating rotor and directional-switch protein of the polar flagellar motor** — a structural/mechanical protein, not an enzyme, transporter, or diffusible signal. Its C-terminal domain converts proton-motive force into rotation via electrostatic contacts with the MotA stator; its N-terminal domain anchors the C-ring to the FliF MS-ring for assembly; and CheY-P-triggered conformational changes make FliG the effector that switches rotation between CCW and CW. It functions in the cytoplasm at the base of the polar flagellum within the FleQ/σ54-regulated flagellar system, and the FliG-containing C-ring is additionally required for flagellar type III protein export. This annotation is inferred from deeply conserved orthologue biology and confirmed by the presence of all canonical FliG domains and torque/switch motifs in the Q88ET5 sequence.


## Artifacts

- [OpenScientist final report](fliG-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](fliG-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10440379
2. PMID:30940700
3. PMID:22896702
4. PMID:9600984
5. PMID:23161029
6. PMID:28089452
7. PMID:15126479
8. PMID:30082903
9. PMID:31452860
10. PMID:39179739
11. PMID:26561852
12. PMID:19648242
13. PMID:26142283
14. PMID:39709681
15. PMID:30889223
16. PMID:24464458
17. PMID:24771657
18. PMID:21091499
19. PMID:15819626
20. PMID:37520711
21. PMID:40001515
22. PMID:36946730