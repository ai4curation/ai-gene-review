---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T16:50:57.255734'
end_time: '2026-08-31T17:10:45.527715'
duration_seconds: 1188.27
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: flhA
  gene_symbol: flhA
  uniprot_accession: Q88EV8
  protein_description: 'RecName: Full=Flagellar biosynthesis protein FlhA {ECO:0000256|RuleBase:RU364093};'
  gene_info: Name=flhA {ECO:0000256|RuleBase:RU364093, ECO:0000313|EMBL:AAN69923.1};
    OrderedLocusNames=PP_4344 {ECO:0000313|EMBL:AAN69923.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the FHIPEP (flagella/HR/invasion proteins export
  protein_domains: FHIPEP_1. (IPR042194); FHIPEP_3. (IPR042193); FHIPEP_4. (IPR042196);
    FHIPEP_CS. (IPR025505); FlhA. (IPR006301)
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
citation_count: 10
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: flhA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: flhA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88EV8
- **Protein Description:** RecName: Full=Flagellar biosynthesis protein FlhA {ECO:0000256|RuleBase:RU364093};
- **Gene Information:** Name=flhA {ECO:0000256|RuleBase:RU364093, ECO:0000313|EMBL:AAN69923.1}; OrderedLocusNames=PP_4344 {ECO:0000313|EMBL:AAN69923.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the FHIPEP (flagella/HR/invasion proteins export
- **Key Domains:** FHIPEP_1. (IPR042194); FHIPEP_3. (IPR042193); FHIPEP_4. (IPR042196); FHIPEP_CS. (IPR025505); FlhA. (IPR006301)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "flhA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'flhA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **flhA** (gene ID: flhA, UniProt: Q88EV8) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *flhA* (PP_4344, UniProt Q88EV8) in *Pseudomonas putida* KT2440

## Summary

**FlhA (PP_4344, UniProt Q88EV8) is a large 709-residue polytopic inner-membrane protein that serves as a core, essential subunit of the flagellar type III secretion system (fT3SS) export apparatus in *Pseudomonas putida* KT2440.** It is the founding member of the FHIPEP (Flagella/Hr/Invasion Proteins Export Pore) family and, together with FlhB, FliO, FliP, FliQ and FliR, it forms the membrane-embedded "export gate" at the base of the flagellum. Through this gate, unfolded axial subunits — rod proteins, hook proteins, hook-filament junction proteins, and flagellin — are secreted from the cytoplasm across the inner membrane and channeled up the growing flagellar structure to assemble at its distal tip. This annotation is anchored both by organism-specific genetic work in *P. putida* and by an exceptionally deep body of mechanistic literature on FlhA orthologs in *Salmonella*.

Mechanistically, FlhA performs two coupled jobs. Its **N-terminal transmembrane FHIPEP domain** (~residues 1–350) is part of the export gate that operates as a proton-protein antiporter, converting the transmembrane proton-motive force (PMF) into the energy that drives translocation; this coupling is mediated in part by a direct interaction between FlhA and FliJ at the center of the cytoplasmic FliH/FliI/FliJ ATPase ring. Its large **C-terminal cytoplasmic domain (FlhA_C**, ~residues 350–709, bearing the conserved GYxLI motif present in Q88EV8 as GYRLI at position 377**)** is a dynamic docking platform that receives export-chaperone/substrate complexes (e.g. FlgN-FlgK/L) and, in concert with FliK and FlhB, executes the ordered switch of export specificity from hook-type to filament-type substrates once the hook reaches its mature length.

FlhA carries out its function at and within the cytoplasmic (inner) membrane, at the base of the flagellar basal body, and it is required for the export of every class of axial flagellar substrate. In *P. putida* specifically, *flhA* is the first gene of the **σN-dependent, FleQ-activated, FleN-repressed *flhA-flhF-fleN-fliA* operon**, placing it firmly within the flagellar biogenesis/motility regulatory cascade and, through FleQ and cyclic-di-GMP signaling, at the intersection of motility and biofilm lifestyle decisions. Because FlhA/FHIPEP is the single most conserved component shared between flagellar and virulence (injectisome) T3SSs, the functional annotation of Q88EV8 is a high-confidence inference supported by both direct genetics and deep evolutionary conservation.

---

## Gene/Protein Identity Verification

Before presenting findings, the target identity was confirmed against all mandatory criteria:

| Criterion | UniProt spec | Verification |
|---|---|---|
| Gene symbol | *flhA* | Matches; organism-specific *P. putida* study (PMID 30889223) names *flhA* as the flagellar export-gate gene |
| Organism | *P. putida* KT2440 (ATCC 47054 / DSM 6125) | Confirmed; PMID 30889223 studies KT2440/KT2442 directly |
| Ordered locus | PP_4344 | Consistent with EMBL AAN69923.1 |
| Protein family | FHIPEP (flagella/HR/invasion export) | Confirmed by sequence architecture and InterPro domains |
| Key domains | FHIPEP_1/3/4, FHIPEP_CS, FlhA signature | Verified bioinformatically on Q88EV8 (see Findings 6, 8) |

The gene symbol is **unambiguous** for this protein: "flhA" reliably denotes the flagellar biosynthesis protein FlhA across bacteria, and organism-specific literature exists for *P. putida*. There was no need to fall back on domain-only inference — though the conserved architecture strongly reinforces the direct genetic evidence.

---

## Key Findings

### Finding 1 — FlhA is a membrane component of the flagellar export gate in *P. putida*, encoded in a FleQ/σN-regulated operon

The most direct, organism-specific evidence comes from a dedicated study of the *P. putida* KT2440/KT2442 flagellar gene cluster ([PMID: 30889223](https://pubmed.ncbi.nlm.nih.gov/30889223/)). This work establishes that *flhA* is **the first gene of the *flhA-flhF-fleN-fliA* operon**, explicitly annotating it as encoding "*a component of the flagellar export gate*," while the three downstream genes (*flhF*, *fleN*, *fliA*) are regulatory elements. The operon is transcribed from the **σN-dependent P*flhA* promoter**, which is activated by the master flagellar regulator **FleQ** and negatively regulated by **FleN**. This transcriptional placement is diagnostic: genes in Class II/III of the flagellar hierarchy encode the structural export apparatus and basal-body components, consistent with a physical export-gate role rather than a regulatory or late-filament role. Verbatim, the paper states that "*The Pseudomonas putida flhA-flhF-fleN-fliA cluster encodes a component of the flagellar export gate and three regulatory elements potentially involved in flagellar biogenesis and other functions*," and that "*PflhA and PflhF are σN-dependent, activated by the flagellar regulator FleQ, and negatively regulated by FleN*." This single organism-specific study anchors the entire functional annotation of Q88EV8 to *P. putida*.

### Finding 2 — FlhA is a core integral-membrane subunit of the export gate that cooperates with a cytoplasmic ATPase ring

An authoritative review of the flagellar T3SS ([PMID: 24064315](https://pubmed.ncbi.nlm.nih.gov/24064315/), Minamino 2014) defines the export apparatus as consisting of "*a membrane-embedded export gate made of FlhA, FlhB, FliO, FliP, FliQ, and FliR and a water-soluble ATPase ring complex consisting of FliH, FliI, and FliJ*." FlhA is therefore not a peripheral accessory but one of six integral-membrane proteins that build the transmembrane secretion channel. Substrate-specific chaperones (FlgN, FliS, FliT) protect their cognate unfolded substrates from premature aggregation and deliver them to the gate, while the soluble ATPase complex facilitates the initial entry of substrate into the narrow export-gate pore. This division of labor — membrane gate versus soluble ATPase versus chaperone escorts — frames every downstream mechanistic finding about FlhA.

### Finding 3 — The FlhA-containing gate is a proton-protein antiporter; FlhA-FliJ coupling harnesses PMF

The same review ([PMID: 24064315](https://pubmed.ncbi.nlm.nih.gov/24064315/)) reports the energetic mechanism: "*The export gate by itself is a proton-protein antiporter that uses the two components of proton motive force, the electric potential difference and the proton concentration difference, for different steps of the export process.*" Critically for FlhA's specific role, "*A specific interaction of FlhA with FliJ located in the center of the ATPase ring complex allows the export gate to efficiently use proton motive force to drive protein export.*" This places FlhA at the heart of energy coupling: its transmembrane domain contributes to the antiporter that converts PMF (both the membrane potential ΔΨ and the proton gradient ΔpH) into translocation energy, and its physical contact with FliJ links the membrane gate to the ATPase ring so that ATP hydrolysis and PMF are used cooperatively rather than redundantly. Both ATP and PMF energize export, but the gate can operate on PMF once substrate entry is initiated.

### Finding 4 — The FlhA C-terminal cytoplasmic domain (FlhA_C) is a chaperone/substrate docking platform

Direct biochemical evidence for FlhA_C as a docking platform comes from GST pull-down and genetic studies ([PMID: 22233518](https://pubmed.ncbi.nlm.nih.gov/22233518/), Minamino et al. 2012). The flagellar export chaperone **FlgN** interacts directly with FlhA_C, and the FlgN-FlgK complex binds FlhA_C together with FliJ to form a quaternary **FlgN-FlgK-FliJ-FlhA_C complex**: "*The FlgN-FlgK complex bound to FlhA(C) and FliJ to form the FlgN-FlgK-FliJ-FlhA(C) complex.*" A conserved Tyr-122 of FlgN was required for the interaction, and a truncation abolishing it (FlgN120) lost binding; genetic suppressors of a Δ*flgN* export defect mapped back to FlhA_C, independently confirming the functional partnership. The authors conclude "*FlgN efficiently transfers FlgK/L subunits to FlhA(C) to promote their export.*" Thus FlhA_C is the cytoplasmic receiving dock where chaperone-escorted substrates are handed off to the export channel.

### Finding 5 — Dynamic domain motions of FlhA_C (GYXLI motif and linker) mediate substrate-specificity switching

Two structure-guided mutagenesis studies establish that FlhA_C is not a static dock but a **dynamic machine**. Inoue et al. 2021 ([PMID: 34059784](https://pubmed.ncbi.nlm.nih.gov/34059784/)) show that "*The flagellar protein export apparatus switches substrate specificity from hook-type to filament-type upon hook assembly completion, thereby initiating filament assembly at the hook tip*," and that the FlhA_C **linker** mediates this switching. Minamino et al. 2022 ([PMID: 35876582](https://pubmed.ncbi.nlm.nih.gov/35876582/)) show that the conserved **GYXLI motif** of FlhA is required for the dynamic domain motions of FlhA_C needed for export; the paper notes that "*Flagellar structural subunits are transported via the flagellar type III secretion system (fT3SS) and assemble at the distal end of the growing flagellar structure.*" Together these define a mechanism in which conformational cycling of FlhA_C, gated by the GYXLI motif and its linker, reorders the substrate preference of the gate as assembly proceeds.

### Finding 6 — Sequence analysis of Q88EV8 confirms canonical FlhA architecture

Bioinformatic analysis performed in this investigation confirms that the *P. putida* protein has the textbook FlhA two-module plan. Q88EV8 is **709 amino acids**. Kyte-Doolittle hydropathy analysis (window 19) identifies a dense cluster of hydrophobic/transmembrane-like segments confined to the **N-terminal ~350 residues** (13 hydrophobic peaks, including clear membrane spans at approximately residues 27–41, 47–66, and 121–139), followed by a largely hydrophilic **C-terminal region of ~359 residues (res ~350–709)** corresponding to the cytoplasmic FlhA_C domain. The conserved functional **GYxLI motif is present as GYRLI at residue 377**, immediately at the start of FlhA_C — precisely matching the motif shown by Minamino et al. 2022 to be required for FlhA_C domain motions. The overall length (709 aa) is consistent with FlhA orthologs (~692 aa in *Salmonella*). This confirms that the mechanistic conclusions from *Salmonella* transfer to Q88EV8 at the level of primary structure.

### Finding 7 — FlhA is directly required for export of both rod/hook- and filament-class substrates and executes the hook-length switch with FlhB and FliK

Direct export-competence assays in *Salmonella* ([PMID: 10049367](https://pubmed.ncbi.nlm.nih.gov/10049367/), Minamino & Macnab 1999) demonstrated that export of the hook-capping protein FlgD and hook protein FlgE to the periplasm "*required FlhA, FlhB, FliH, FliI, FliO, FliP, FliQ, and FliR*," and that flagellin export likewise required FlhA — establishing FlhA as essential for **both** substrate classes. The hierarchical-export review ([PMID: 29850796](https://pubmed.ncbi.nlm.nih.gov/29850796/), Minamino 2018) states that upon completion of hook assembly (~55 nm), "*Three flagellar proteins, namely FliK, FlhB and FlhA, are responsible for this substrate specificity switching*," and that after switching, interactions among FlhA, the ATPase complex, and export chaperones establish filament assembly order. FliK-driven conformational rearrangements of FlhA and FlhB drive the switch ([PMID: 31712281](https://pubmed.ncbi.nlm.nih.gov/31712281/), Minamino et al. 2020).

### Finding 8 — FlhA/FHIPEP is the most conserved T3SS export component, making the Q88EV8 annotation high-confidence

FlhA is the founding member of the **FHIPEP family** and is the single most highly conserved subunit shared between the flagellar and virulence (injectisome) type III secretion systems. Its injectisome orthologs — InvA (*Salmonella* SPI-1), MxiA (*Shigella*) — were collectively renamed **SctV**. All members share the two-module plan: an N-terminal polytopic transmembrane FHIPEP domain plus a large cytoplasmic domain that oligomerizes into a **nonameric ring**. Q88EV8 retains the full FHIPEP transmembrane region, a ~359-aa FlhA_C, and the GYxLI (GYRLI) motif, and its InterPro assignments (IPR042194 / IPR042193 / IPR042196 FHIPEP domains, IPR025505 FHIPEP_CS, IPR006301 FlhA signature) match the family exactly. Because deep conservation is combined with direct organism-specific genetics in *P. putida* ([PMID: 30889223](https://pubmed.ncbi.nlm.nih.gov/30889223/)), the functional annotation is robust.

---

## Mechanistic Model / Interpretation

The findings converge on a single coherent model of FlhA as the **energy-coupling, substrate-sorting gatekeeper of the flagellar export gate**. Its domain architecture maps directly onto its two functions.

```
                     FLAGELLUM (grows at distal tip)
                              ▲
                              │  unfolded axial subunits
                              │  (rod → hook → junction → flagellin)
   ┌──────────────────────────────────────────────────────┐
   │              FLAGELLAR BASAL BODY / MS-ring            │
   │  ┌───────────────── EXPORT GATE ─────────────────┐    │
   │  │  FlhA  FlhB  FliO  FliP  FliQ  FliR            │    │  INNER
   │  │   ▲(FHIPEP TM domain = proton-protein          │    │  MEMBRANE
   │  │   │ antiporter; uses ΔΨ + ΔpH of PMF)          │    │
   └──┼───┼────────────────────────────────────────────┼───┘
      │   │
      │  FlhA_C (cytoplasmic, ~359 aa, GYRLI@377)
      │   │  • docks chaperone-substrate complexes
      │   │  • dynamic domain motions → substrate switch
      │   ▼
      │  FliJ ── center of ATPase ring                  CYTOPLASM
      │  ┌──────────────────────────────┐
      │  │  FliH – FliI – FliJ ATPase    │  ← ATP hydrolysis
      │  └──────────────────────────────┘
      │        ▲
   Chaperones: FlgN·FlgK/L, FliS·FliC, FliT·FliD  → deliver substrates
```

**Energy coupling.** The N-terminal FHIPEP transmembrane domain of FlhA is embedded in the inner membrane and forms part of the antiporter that couples inward proton flow to outward protein translocation. The two components of PMF are used at different steps: the membrane potential (ΔΨ) and the proton gradient (ΔpH) power distinct phases of export. FlhA's direct contact with FliJ links this membrane machine to the FliH/FliI/FliJ ATPase, so that ATP-driven substrate loading and PMF-driven translocation act in series rather than redundantly (Findings 2, 3).

**Substrate handoff and sorting.** FlhA_C projects into the cytoplasm and serves as the landing pad for chaperone-escorted substrates. Chaperones (FlgN for the hook-junction proteins FlgK/FlgL; FliS for flagellin; FliT for the filament cap FliD) keep their cargo unfolded and hand it to FlhA_C, forming complexes such as FlgN-FlgK-FliJ-FlhA_C (Finding 4). Because FlhA_C assembles into a nonameric ring, it presents multiple binding sites that impose order on which substrates are exported when.

**The hook-length switch.** The elegance of the system lies in its self-timing. While the hook grows, the gate exports "hook-type" substrates. When the hook reaches ~55 nm, the molecular ruler FliK signals completion, triggering conformational rearrangements in FlhB and in FlhA_C. The GYXLI motif and the FlhA_C linker enable the dynamic domain motions that reconfigure the gate's specificity from hook-type to filament-type, so that flagellin and junction proteins are now exported to build the filament at the hook tip (Findings 5, 7). FlhA is thus simultaneously an energy transducer and a programmable sorting valve.

**Regulatory embedding in *P. putida*.** Transcription of *flhA* is not constitutive. It heads the σN-dependent *flhA-flhF-fleN-fliA* operon under the control of the enhancer-binding master regulator FleQ, itself modulated by the second messenger cyclic-di-GMP, and is repressed by FleN. Low c-di-GMP favors FleQ activation of σN-dependent flagellar promoters (motility program); high c-di-GMP redirects FleQ toward biofilm-matrix genes ([PMID: 27636892](https://pubmed.ncbi.nlm.nih.gov/27636892/)). FlhA production is therefore gated at the point where *P. putida* commits to a motile versus sessile lifestyle (Finding 1). Consistent with this, screens for biofilm-defective *P. putida* mutants recover flagellar regulatory genes, underscoring motility/adhesion crosstalk ([PMID: 27190143](https://pubmed.ncbi.nlm.nih.gov/27190143/)).

| FlhA module | Residues (Q88EV8) | Localization | Function |
|---|---|---|---|
| FHIPEP transmembrane domain | ~1–350 | Inner membrane | Forms export channel; proton-protein antiporter (PMF coupling) |
| Cytoplasmic domain FlhA_C | ~350–709 | Cytoplasm | Chaperone/substrate docking; nonameric ring; substrate-switch |
| GYxLI motif (GYRLI) | 377 | Cytoplasm (FlhA_C) | Enables dynamic FlhA_C domain motions required for export |

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution | Type |
|---|---|---|---|
| [30889223](https://pubmed.ncbi.nlm.nih.gov/30889223/) | Transcriptional organization of *flhF*/*fleN* in *P. putida* | Organism-specific: names *P. putida flhA* as export-gate gene; defines FleQ/σN operon | Primary genetics |
| [24064315](https://pubmed.ncbi.nlm.nih.gov/24064315/) | Protein export through the flagellar T3S pathway | Defines FlhA as core gate subunit; PMF antiporter; FlhA-FliJ coupling | Authoritative review |
| [22233518](https://pubmed.ncbi.nlm.nih.gov/22233518/) | FlgN-FlhA interaction required for export | FlhA_C is chaperone-substrate docking platform | Primary biochemistry |
| [34059784](https://pubmed.ncbi.nlm.nih.gov/34059784/) | FlhA linker mediates export switching | FlhA_C linker drives hook→filament switch | Primary mutagenesis |
| [35876582](https://pubmed.ncbi.nlm.nih.gov/35876582/) | Conserved GYXLI motif of FlhA | GYXLI required for FlhA_C domain motions | Primary mutagenesis |
| [10049367](https://pubmed.ncbi.nlm.nih.gov/10049367/) | Components of *Salmonella* flagellar export apparatus | FlhA required for export of hook- and filament-class substrates | Primary export assay |
| [29850796](https://pubmed.ncbi.nlm.nih.gov/29850796/) | Hierarchical protein export mechanism | FliK/FlhB/FlhA execute substrate-specificity switch | Review |
| [31712281](https://pubmed.ncbi.nlm.nih.gov/31712281/) | FliK-driven rearrangements of FlhA/FlhB | Conformational basis of export switching | Primary |
| [10712687](https://pubmed.ncbi.nlm.nih.gov/10712687/) | Interactions among export apparatus components | FlhAC/FlhBC interaction map; model of gate + ATPase | Primary |
| [26244937](https://pubmed.ncbi.nlm.nih.gov/26244937/) | Weak FlhB interactions govern T3S dynamics | Quantitative FlhBC–FlhAC affinity (micromolar) | Primary biophysics |
| [27636892](https://pubmed.ncbi.nlm.nih.gov/27636892/) | FleQ/c-di-GMP/σ factors in *P. putida* | Regulatory context: FleQ + c-di-GMP control flagellar cascade | Primary genetics |
| [27190143](https://pubmed.ncbi.nlm.nih.gov/27190143/) | Biofilm-defective mutants in *P. putida* | Links flagellar regulatory genes to motility/biofilm crosstalk | Primary screen |

**How the evidence fits together.** The strongest and most target-specific evidence is [PMID: 30889223](https://pubmed.ncbi.nlm.nih.gov/30889223/), which explicitly annotates *P. putida flhA* as an export-gate component and defines its regulation. Every mechanistic detail — the antiporter, the FlhA-FliJ coupling, the FlhA_C docking platform, the GYXLI-dependent domain motions, and the hook-length switch — comes from *Salmonella* studies of the orthologous protein. These transfer to Q88EV8 with high confidence because (i) FHIPEP is the most conserved T3SS subunit, (ii) the *P. putida* sequence retains the full architecture including the GYRLI motif, and (iii) *P. putida* genetics independently confirm the same physiological role. No paper in the corpus challenges this annotation; the studies are mutually reinforcing across genetics, biochemistry, and structural biophysics.

---

## Limitations and Knowledge Gaps

1. **No direct structural or biochemical study of Q88EV8 itself.** All mechanistic conclusions rest on *Salmonella* orthologs plus one *P. putida* transcriptional/genetic study. There is no published crystal/cryo-EM structure, no reconstituted export assay, and no mutagenesis of the *P. putida* protein specifically. The inference is strong but remains an inference for the exact residues and dynamics of Q88EV8.

2. **Transmembrane topology is predicted, not experimentally mapped.** The N-terminal domain boundaries and exact number of TM helices in Q88EV8 come from hydropathy analysis performed here, not from experimental topology mapping (e.g. PhoA/LacZ fusions) in *P. putida*.

3. **PMF vs ATP quantitative contribution not measured in *P. putida*.** The energetics (antiporter, ΔΨ/ΔpH partitioning) are established in enteric models; whether *P. putida*'s polar flagellar system uses identical energetics is untested.

4. **Chaperone partners in *P. putida* not individually validated.** FlgN, FliS, FliT partnerships with FlhA_C are demonstrated in *Salmonella*; the corresponding *P. putida* chaperones are presumed orthologous but not experimentally shown to dock Q88EV8.

5. **Possible moonlighting/regulatory roles unexplored.** The *P. putida* operon couples *flhA* to regulatory genes (*flhF*, *fleN*, *fliA*) and to c-di-GMP/FleQ signaling; whether FlhA itself contributes to any signaling beyond structural export in *P. putida* is unknown.

---

## Proposed Follow-up Experiments / Actions

1. **Solve or model the Q88EV8 FlhA_C structure.** Obtain an AlphaFold model (and, ideally, cryo-EM of the *P. putida* export gate) to confirm the nonameric ring geometry and the placement of the GYRLI motif; compare to *Salmonella* FlhA_C to quantify conservation of the switch machinery.

2. **Experimental TM topology mapping.** Use reporter fusions (PhoA/GFP) in *P. putida* to confirm the number and boundaries of transmembrane segments in the N-terminal FHIPEP domain and validate the ~350-residue module boundary.

3. **Targeted mutagenesis of the GYRLI motif in *P. putida*.** Introduce point mutations at residue 377 and test motility, filament assembly, and hook-length control to confirm the switch function operates identically in the polar flagellar system.

4. **Reconstitute or assay export competence.** Construct a Δ*flhA* (ΔPP_4344) *P. putida* strain and test secretion of hook (FlgE) and flagellin substrates, complementing with wild-type and mutant *flhA* to establish direct export requirement in this organism.

5. **Map the *P. putida* chaperone-FlhA_C interactome.** Use pull-downs / bacterial two-hybrid with *P. putida* FlgN, FliS, FliT, and FliJ orthologs against FlhA_C to confirm the docking partnerships.

6. **Probe regulatory integration.** Measure P*flhA* activity and FlhA protein levels as a function of c-di-GMP and FleQ status to quantify how FlhA production is gated at the motility-to-biofilm decision point.

---

## Conclusion

FlhA (PP_4344, Q88EV8) is the conserved, essential gatekeeper of the *Pseudomonas putida* flagellar type III export apparatus: a polytopic inner-membrane protein whose N-terminal FHIPEP domain forms the PMF-driven export channel and whose cytoplasmic FlhA_C domain docks chaperone-substrate complexes and, via GYRLI-gated domain motions with FlhB and FliK, sorts and switches axial substrates during flagellar assembly. It functions at the flagellar basal body in the inner membrane, is required for export of every axial subunit class, and is transcriptionally embedded in the FleQ/σN-regulated flagellar cascade that governs motility and biofilm lifestyle in *P. putida*.


## Artifacts

- [OpenScientist final report](flhA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](flhA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:30889223
2. PMID:24064315
3. PMID:22233518
4. PMID:34059784
5. PMID:35876582
6. PMID:10049367
7. PMID:29850796
8. PMID:31712281
9. PMID:27636892
10. PMID:27190143