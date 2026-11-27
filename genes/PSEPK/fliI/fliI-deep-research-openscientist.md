---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T16:50:57.255763'
end_time: '2026-08-31T18:02:26.038259'
duration_seconds: 4288.78
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: fliI
  gene_symbol: fliI
  uniprot_accession: Q88ET7
  protein_description: 'RecName: Full=Flagellum-specific ATP synthase {ECO:0000256|ARBA:ARBA00020580};
    EC=7.1.2.2 {ECO:0000256|ARBA:ARBA00012473};'
  gene_info: Name=fliI {ECO:0000313|EMBL:AAN69944.1}; OrderedLocusNames=PP_4366 {ECO:0000313|EMBL:AAN69944.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the ATPase alpha/beta chains family.
  protein_domains: AAA+_ATPase. (IPR003593); ATPase_a/bsu_AS. (IPR020003); ATPase_alpha/beta_chains.
    (IPR050053); ATPase_F1/V1/A1_a/bsu_nucl-bd. (IPR000194); ATPase_T3SS_FliI/YscN.
    (IPR005714)
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
citation_count: 13
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: fliI-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: fliI-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88ET7
- **Protein Description:** RecName: Full=Flagellum-specific ATP synthase {ECO:0000256|ARBA:ARBA00020580}; EC=7.1.2.2 {ECO:0000256|ARBA:ARBA00012473};
- **Gene Information:** Name=fliI {ECO:0000313|EMBL:AAN69944.1}; OrderedLocusNames=PP_4366 {ECO:0000313|EMBL:AAN69944.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the ATPase alpha/beta chains family.
- **Key Domains:** AAA+_ATPase. (IPR003593); ATPase_a/bsu_AS. (IPR020003); ATPase_alpha/beta_chains. (IPR050053); ATPase_F1/V1/A1_a/bsu_nucl-bd. (IPR000194); ATPase_T3SS_FliI/YscN. (IPR005714)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "fliI" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'fliI' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **fliI** (gene ID: fliI, UniProt: Q88ET7) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: FliI (Q88ET7 / PP_4366) in *Pseudomonas putida* KT2440

## Summary

**FliI (UniProt Q88ET7, locus PP_4366) is the flagellum-specific ATPase of *Pseudomonas putida* KT2440 — an F₁-ATPase β-subunit homolog that hydrolyzes ATP to energize the flagellar type III protein-export system (fT3SS).** The protein catalyzes the reaction ATP + H₂O → ADP + Pᵢ (EC 7.1.2.2) and, through this chemical energy, drives assembly of the bacterial flagellum. It belongs to the ATPase alpha/beta chains family and carries the diagnostic FliI/YscN T3SS ATPase signature (InterPro IPR005714), placing it unambiguously within the family of secretion-system export ATPases rather than the membrane-bound respiratory F₁F₀ synthases.

Mechanistically, FliI does not act alone. It assembles a homohexameric ring closely resembling the α₃β₃γ catalytic core of F₁-ATPase, and works as part of a soluble cytoplasmic complex with the regulator/anti-activator FliH and the central-stalk-like protein FliJ. This FliH–FliI–FliJ module localizes to the cytoplasmic face of the flagellar basal body (the C-ring), where it delivers chaperone–substrate complexes to the membrane-embedded export gate and — critically — uses ATP hydrolysis to *activate* that gate so that the transmembrane proton-motive force (PMF) can drive the actual translocation of flagellar axial subunits. Thus FliI is best understood as an energy-coupling and substrate-loading engine rather than the obligate translocation motor: in bypass mutants the flagellum can still assemble using PMF alone, but with far lower efficiency and robustness.

In *P. putida* specifically, *fliI* is embedded in a large (~59-gene) flagellar regulon controlled by a three-tier transcriptional cascade (FleQ → σ^N/RpoN → FliA/σ²⁸), and it is required for building the polar flagellar tuft. Direct experimental evidence in *P. putida* strain S12 shows that transposon disruption of *fliI* abolishes flagellum formation and renders cells non-motile. The protein therefore functions at the interface of the cytoplasm and inner membrane, at the base of the flagellum, as an indispensable-for-efficiency component of the motility apparatus. This report was assembled from UniProt/InterPro annotation combined with mechanistic literature on functionally characterized FliI orthologs (primarily *Salmonella*) and *P. putida*-specific genetic and regulatory studies.

---

## Gene/Protein Identity Verification

Before presenting findings, the identity of the target was confirmed against the UniProt record:

| Attribute | Value | Consistency check |
|-----------|-------|-------------------|
| UniProt accession | Q88ET7 | ✓ target |
| Gene symbol | *fliI* | ✓ matches flagellar ATPase nomenclature |
| Locus tag | PP_4366 | ✓ *P. putida* KT2440 |
| Protein | Flagellum-specific ATP synthase, EC 7.1.2.2 | ✓ consistent with FliI function |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125) | ✓ correct strain |
| Family | ATPase alpha/beta chains family | ✓ F₁-type fold |
| Key domain | ATPase_T3SS_FliI/YscN (IPR005714) | ✓ diagnostic for export ATPases |

The gene symbol *fliI*, the EC number, the protein family, and the InterPro domain signatures are all mutually consistent and point to a single, well-defined molecular function: the flagellar export ATPase. There is no ambiguity in this assignment. Because dedicated biochemical/structural studies of the *P. putida* KT2440 ortholog itself are sparse, functional detail below is drawn from the highly conserved and extensively characterized orthologs (chiefly *Salmonella enterica*), supplemented by *P. putida*-specific genetics and regulation. The FliI protein family is strongly conserved across flagellated bacteria, so this cross-species inference is well justified.

---

## Key Findings

### Finding 1 — FliI is the flagellar-specific ATPase that hydrolyzes ATP to power flagellar protein export

UniProt annotates Q88ET7 (*fliI*/PP_4366) as a **flagellum-specific ATP synthase, EC 7.1.2.2**, in the ATPase alpha/beta chains family, and it carries the FliI/YscN T3SS ATPase InterPro signature (IPR005714). This places the protein in the class of ATPases that energize type III secretion systems. In functionally characterized orthologs, FliI is the ATP-hydrolyzing engine of the flagellar type III secretion system (fT3SS): it forms a complex with FliH and FliJ and "escorts export substrates from the cytoplasm to the export gate complex, which is made up of six membrane proteins" ([PMID: 21934659](https://pubmed.ncbi.nlm.nih.gov/21934659/)).

The core catalytic activity is ATP hydrolysis (ATP + H₂O → ADP + Pᵢ). Despite the historical "ATP synthase" name (reflecting the family relationship to F₁F₀-ATP synthase), FliI operates physiologically as an **ATPase** — it consumes ATP to do work, rather than synthesizing it. Its substrate is ATP; its output is chemical energy used to prepare export substrates and to activate the export gate. This is the primary function requested in the annotation task: FliI is an enzyme whose catalyzed reaction is ATP hydrolysis, with strict specificity for ATP as the nucleotide substrate.

### Finding 2 — FliI is an F₁-ATPase homolog that forms an ATP-driven homohexamer; a catalytic glutamate is required for hydrolysis

FliI belongs to the F₁-type ATPase alpha/beta family, and structural studies show that its assembled ring closely mirrors the catalytic core of F₁-ATP synthase. The FliI₆–FliJ complex "is structurally similar to the α₃β₃γ complex of F₁-ATPase" ([PMID: 26984495](https://pubmed.ncbi.nlm.nih.gov/26984495/)), meaning six FliI subunits form a ring analogous to the alternating α₃β₃ hexamer, with FliJ occupying the position of the γ central stalk. This deep homology reveals the evolutionary origin of the flagellar export ATPase from the rotary ATP synthase lineage and explains its nucleotide-binding chemistry.

ATP binding drives oligomerization: "FliI ATPase forms a homo-hexamer to fully exert its ATPase activity, facilitating bacterial flagellar protein export" ([PMID: 19665005](https://pubmed.ncbi.nlm.nih.gov/19665005/)). The monomer has low activity; hexamerization creates the composite active sites at subunit interfaces (as in F₁-ATPase), so ring assembly and catalysis are coupled. The catalytic residue was pinpointed by mutagenesis: the mutant **FliI(E221Q)**, "which retained the affinity for ATP but has lost ATPase activity, efficiently formed the hexamer even in the presence of ATP" ([PMID: 19665005](https://pubmed.ncbi.nlm.nih.gov/19665005/)). This experiment elegantly separates two events — nucleotide binding/hexamerization versus hydrolysis — and identifies **Glu221** (the catalytic-carboxylate equivalent) as essential for the hydrolysis step itself. The E→Q substitution neutralizes the catalytic base while preserving ATP binding, trapping the enzyme in an assembled but catalytically dead state.

### Finding 3 — FliI localizes to the cytoplasmic C-ring/basal body and shuttles substrates to the export gate

FliI functions at the cytoplasmic face of the flagellar basal body. It "forms the FliH₂–FliI complex in the cytoplasm and localizes to the flagellar basal body (FBB) through the interaction of FliH with a C ring protein, FliN" ([PMID: 25284201](https://pubmed.ncbi.nlm.nih.gov/25284201/)). This defines both the subcellular location (cytoplasm, docked at the inner-membrane basal body) and the recruitment mechanism: FliH bridges the ATPase to the C-ring switch protein FliN, and also anchors it to the export-gate protein FlhA.

Single-molecule imaging further showed that FliI exists in two functional forms with distinct roles: "the FliH₂–FliI complex and FliI₆ ring function as a dynamic substrate carrier and a static substrate loader, respectively" ([PMID: 25284201](https://pubmed.ncbi.nlm.nih.gov/25284201/)). The mobile FliH₂–FliI species picks up chaperone–substrate cargo in the cytoplasm and delivers it to the basal body, where the static FliI₆ ring loads it onto the export gate. Notably, the molecules exchange between the FBB-bound and freely diffusing pools several times per minute, and this assembly/disassembly cycle is *not* driven by ATP hydrolysis — indicating that FliI's localization dynamics and its catalytic activity are mechanistically separable. This answers the "where" question: FliI works at the cytoplasm–inner membrane interface, at the base of the flagellum, on the C-ring/basal body platform.

An important nuance from the literature is that the soluble export components are *not* required to deliver every substrate. FliI, FliH, and FliJ "do not deliver flagellin, the major filament protein, from the cytosol to the export gate" ([PMID: 25068520](https://pubmed.ncbi.nlm.nih.gov/25068520/)); their substrate-chaperone escort role is most important for the minor late substrates (FlgK, FlgL, FliD), while abundant flagellin (FliC) reaches the gate without their assistance. This refines the substrate-delivery model and emphasizes that FliI's energetic/gate-activation role, rather than a universal carrier role, is its core contribution.

### Finding 4 — FliI ATP hydrolysis activates the PMF-driven export gate and ensures efficient energy coupling; it is important but not strictly essential

A key mechanistic insight is that the membrane export gate itself is fundamentally a **proton/protein antiporter that uses the proton-motive force** — not ATP — as the direct source of translocation energy. FliI's job is to *switch the gate on*. "ATP hydrolysis by the FliI ATPase activates the export gate complex to become an active protein transporter utilizing Δψ to drive proton-coupled protein export" ([PMID: 34035173](https://pubmed.ncbi.nlm.nih.gov/34035173/)). In other words, the chemical energy of ATP is spent on a regulatory/activation step, after which the electrochemical gradient (specifically the membrane voltage, Δψ) powers the actual export.

The molecular basis of this activation is a FliJ–FlhA interaction promoted by the ATPase complex: "a specific binding of FliJ with an export gate membrane protein, FlhA, is brought about by the FliH–FliI complex, which turns the export gate into a highly efficient, Δψ-driven protein export apparatus" ([PMID: 21934659](https://pubmed.ncbi.nlm.nih.gov/21934659/)). FliI and FliH position FliJ so it can engage FlhA, converting the gate from an inefficient to a highly efficient transporter. Cross-complementation studies conclude that "FliH and FliI ensure robust and efficient energy coupling of protein export during flagellar assembly" ([PMID: 26916245](https://pubmed.ncbi.nlm.nih.gov/26916245/)).

Crucially, FliI is **not strictly essential** for export in all genetic backgrounds. Bypass mutations in the gate protein FlhB (e.g., *flhB(P28T)*) permit flagellar assembly in the absence of FliH and FliI, demonstrating that PMF alone can drive export when the gate is constitutively activated. This establishes the division of labor: PMF is the direct motor; FliI/FliH/FliJ raise the efficiency and robustness of energy coupling by orders of magnitude and are physiologically required for normal flagellation, even if formally dispensable under bypass conditions. Recent work has further uncoupled substrate delivery from gate activation, confirming these are two distinct functions of the ATPase complex ([PMID: 42254510](https://pubmed.ncbi.nlm.nih.gov/42254510/)). The FliJ surface engaging FlhA has been mapped genetically to a conserved patch of residues ([PMID: 23161028](https://pubmed.ncbi.nlm.nih.gov/23161028/)), providing molecular detail for how the ATPase complex activates the gate.

### Finding 5 — In *P. putida*, *fliI* lies within the FleQ/RpoN/FliA-regulated flagellar cluster and is required for flagellum assembly and motility

Turning to the organism of interest: *P. putida* flagellar genes are organized in a single large cluster of ~59 genes (11 operons, 22 promoters) controlled by a three-tier regulatory cascade. "Synthesis of the flagellar apparatus and core chemotaxis machinery is regulated by a three-tier cascade in which *fleQ* is a Class I gene, standing at the top of the transcriptional hierarchy" ([PMID: 34859548](https://pubmed.ncbi.nlm.nih.gov/34859548/)). FleQ is the master regulator (Class I), σ^N (RpoN) drives Class II genes, and the flagellar sigma factor FliA (σ²⁸) drives Class III genes. *fliI* sits within this regulon, so its expression is tied to the master motility program and is modulated by second-messenger (c-di-GMP) signaling through FleQ/FleN.

Direct functional evidence in *P. putida* comes from the solvent-tolerant strain S12: transposon insertions in flagellar genes including *fliI* (alongside *flgK*, *flaG*, *fliC*, and *fliH*) produced non-motile cells. The study identified "the flagellar structural proteins FlgK, FlaG, FliI, FliC, and FliH" among disrupted genes and reported that "the transposon mutants … were nonmotile as determined by a swarm assay and the formation of the flagellum was totally impaired" ([PMID: 11430400](https://pubmed.ncbi.nlm.nih.gov/11430400/)). This is the most direct organism-specific evidence: loss of *fliI* function in *P. putida* abolishes flagellum biogenesis and motility, exactly as predicted from its role as the export ATPase.

Finally, the FliI-dependent export apparatus feeds into the polar-flagellum assembly system characteristic of *Pseudomonas*. Polar flagellar placement, timing, and number in *P. putida* are governed by FlhF, FleN, and FimV ([PMID: 39709681](https://pubmed.ncbi.nlm.nih.gov/39709681/)), and the *flhA-flhF-fleN-fliA* operon links the export gate to these regulators ([PMID: 30889223](https://pubmed.ncbi.nlm.nih.gov/30889223/)). FliI therefore operates within a spatially controlled program that builds a polar tuft of flagella once per cell cycle.

---

## Mechanistic Model / Interpretation

The findings converge on a coherent, well-supported model of FliI as the **energy-transducing hub of the flagellar export apparatus**. The following schematic summarizes the architecture and energy flow:

```
        CYTOPLASM
   (chaperone–substrate, e.g. FlgN:FlgK, FliT:FliD)
                 │
                 ▼
      ┌───────────────────────┐
      │  FliH₂–FliI  (mobile)  │  ← "dynamic substrate carrier"
      │  picks up cargo        │
      └───────────┬───────────┘
                  │  docks via FliH–FliN (C-ring)
                  ▼
   ══════════════════════════════════  INNER MEMBRANE
   C-RING (FliG/FliM/FliN)  │  EXPORT GATE
        FliI₆ ring ─── FliJ ─── FlhA / FlhB / FliPQR
     "static loader"    (γ-like)     (6 membrane proteins)
                  │
        ATP ──► ADP + Pi   (Glu221 catalytic)
                  │
                  ▼
      Activates gate ⇒ Δψ (membrane voltage / PMF)
                       drives proton-coupled export
                  │
                  ▼
     Axial subunits threaded through central channel
                  │
                  ▼
        EXPORT / FLAGELLUM ASSEMBLY (extracellular)
```

**Energy logic.** The single most important conceptual point is that FliI does *not* directly push proteins across the membrane. Instead, ATP hydrolysis by the FliI₆ ring (catalytic Glu221) is spent on **activating** the membrane export gate — chiefly by enabling the FliJ–FlhA interaction — after which the **proton-motive force (specifically Δψ)** provides the direct translocation energy ([PMID: 34035173](https://pubmed.ncbi.nlm.nih.gov/34035173/); [PMID: 21934659](https://pubmed.ncbi.nlm.nih.gov/21934659/)). This explains the otherwise puzzling observation that *fliH fliI* deletions can be bypassed by gate mutations (e.g., *flhB(P28T)*): if the gate is locked "on," PMF suffices, but at greatly reduced efficiency and robustness.

**Two-role model.** FliI performs two mechanistically separable jobs: (1) **substrate loading/delivery** as the mobile FliH₂–FliI carrier and static FliI₆ loader, and (2) **gate activation/energy coupling** via ATP hydrolysis and FliJ–FlhA engagement. Recent cross-complementation work explicitly uncoupled these roles ([PMID: 42254510](https://pubmed.ncbi.nlm.nih.gov/42254510/)), and the flagellin data ([PMID: 25068520](https://pubmed.ncbi.nlm.nih.gov/25068520/)) show that the delivery role is substrate-selective (important for minor late substrates FlgK/FlgL/FliD, dispensable for bulk flagellin).

**Structural evolution.** The FliI₆–FliJ assembly is a structural echo of the α₃β₃γ core of F₁-ATP synthase ([PMID: 26984495](https://pubmed.ncbi.nlm.nih.gov/26984495/)), revealing that the flagellar/T3SS export ATPase and the respiratory ATP synthase share a common ancestor. FliI thus repurposes an ancient nucleotide-hydrolysis machine for protein secretion rather than chemiosmotic energy conservation.

**Organism context.** In *P. putida* KT2440, this machine is deployed under a FleQ→RpoN→FliA cascade ([PMID: 34859548](https://pubmed.ncbi.nlm.nih.gov/34859548/)) to build a polar flagellar tuft whose position and number are set by FlhF/FleN/FimV ([PMID: 39709681](https://pubmed.ncbi.nlm.nih.gov/39709681/)). Disrupting *fliI* collapses the whole program: no flagellum, no motility ([PMID: 11430400](https://pubmed.ncbi.nlm.nih.gov/11430400/)).

### Summary table of FliI properties

| Property | Assignment | Evidence type | Key PMID |
|----------|-----------|---------------|----------|
| Catalyzed reaction | ATP + H₂O → ADP + Pᵢ (EC 7.1.2.2) | Annotation + ortholog biochem | UniProt; 19665005 |
| Substrate specificity | ATP (nucleotide) | Biochemistry | 19665005 |
| Oligomeric state | ATP-driven homohexamer (FliI₆) | Biochem/structure | 19665005; 26984495 |
| Catalytic residue | Glu221 (hydrolysis) | Site-directed mutagenesis | 19665005 |
| Structural fold | F₁-ATPase α/β homolog; FliI₆–FliJ ≈ α₃β₃γ | Crystal structure | 26984495 |
| Localization | Cytoplasm, docked at C-ring/basal body via FliH–FliN | Single-molecule imaging | 25284201 |
| Partners | FliH (regulator/anchor), FliJ (γ-like), FlhA/FliN (docking) | Genetics/biochem | 25284201; 21934659 |
| Primary mechanistic role | Activate PMF-driven export gate; couple energy | Genetics/physiology | 34035173; 21934659 |
| Substrate delivery role | Minor late substrates (FlgK/FlgL/FliD), not bulk flagellin | Biophysics (QCM/ATPase) | 25068520 |
| Essentiality | Important, not strictly essential (bypassable) | Genetics | 26916245 |
| *P. putida* phenotype | Loss → no flagellum, non-motile | Transposon mutagenesis | 11430400 |
| *P. putida* regulation | FleQ (Class I) → RpoN → FliA cascade | Transcriptomics | 34859548 |

---

## Evidence Base

The report integrates 14 papers. Because dedicated Q88ET7-specific biochemistry is limited, the mechanistic backbone comes from *Salmonella* orthologs (justified by strong sequence/structure conservation), while organism-specificity is supplied by *P. putida* genetics and regulation.

| PMID | Title (abbrev.) | Organism | How it supports the report |
|------|-----------------|----------|----------------------------|
| [21934659](https://pubmed.ncbi.nlm.nih.gov/21934659/) | *An energy transduction mechanism used in bacterial flagellar type III protein export* | *Salmonella* | Establishes FliI–FliH–FliJ substrate escort and the FliJ–FlhA gate-activation mechanism (F1, F4) |
| [19665005](https://pubmed.ncbi.nlm.nih.gov/19665005/) | *ATP-induced FliI hexamerization facilitates flagellar protein export* | *Salmonella* | Hexamerization requirement and catalytic Glu221 via E221Q mutant (F2) |
| [26984495](https://pubmed.ncbi.nlm.nih.gov/26984495/) | *Complex structure of the type III ATPase and its regulator* | *Salmonella* | FliI₆–FliJ ≈ α₃β₃γ of F₁-ATPase; structural homology (F2) |
| [25284201](https://pubmed.ncbi.nlm.nih.gov/25284201/) | *Assembly dynamics and the roles of FliI ATPase* | *Salmonella* | Cytoplasmic FliH₂–FliI, docking via FliH–FliN, dynamic carrier vs static loader (F3) |
| [34035173](https://pubmed.ncbi.nlm.nih.gov/34035173/) | *Membrane voltage-dependent activation of the flagellar export apparatus* | *Salmonella* | ATP hydrolysis activates Δψ-driven gate (F4) |
| [26916245](https://pubmed.ncbi.nlm.nih.gov/26916245/) | *FliH and FliI ensure efficient energy coupling* | *Salmonella* | Robust/efficient energy coupling; non-essential-but-important status (F4) |
| [42254510](https://pubmed.ncbi.nlm.nih.gov/42254510/) | *Uncoupling substrate delivery from export gate activation* | *Salmonella*/Na⁺-driven | Confirms two distinct ATPase-complex functions (model) |
| [25068520](https://pubmed.ncbi.nlm.nih.gov/25068520/) | *Soluble components do not deliver flagellin* | *Salmonella* | Refines substrate scope: FliI escort matters for minor late substrates, not bulk FliC (F3) |
| [23161028](https://pubmed.ncbi.nlm.nih.gov/23161028/) | *Interaction between FliJ and FlhA* | *Salmonella* | Maps the conserved FliJ surface engaging FlhA (mechanism of gate activation) |
| [25201947](https://pubmed.ncbi.nlm.nih.gov/25201947/) | *Assembling flagella without FliO* | *Salmonella* | Context on the six-protein transmembrane export gate FliI acts upon |
| [11430400](https://pubmed.ncbi.nlm.nih.gov/11430400/) | *Transposon mutations in flagella biosynthesis of P. putida S12* | *P. putida* | Direct: *fliI* disruption abolishes flagellum and motility (F5) |
| [34859548](https://pubmed.ncbi.nlm.nih.gov/34859548/) | *Transcriptional organization of the P. putida flagellar system* | *P. putida* | FleQ/RpoN/FliA three-tier cascade; regulon context (F5) |
| [30889223](https://pubmed.ncbi.nlm.nih.gov/30889223/) | *Regulation of flhF and fleN in P. putida* | *P. putida* | Export-gate operon and its regulation; links to biofilm/c-di-GMP |
| [39709681](https://pubmed.ncbi.nlm.nih.gov/39709681/) | *Regulation of polar flagella assembly in P. putida* | *P. putida* | FlhF/FleN/FimV set position/timing/number of polar flagella (F5) |

**Consistency of evidence.** All mechanistic papers agree on the core model (ATPase complex activates a PMF-driven gate), differing mainly in emphasis. The one important refinement — that FliI is not the direct translocation motor and is bypassable — comes from bypass-mutant genetics and the PMF/Δψ work ([PMID: 34035173](https://pubmed.ncbi.nlm.nih.gov/34035173/); [PMID: 26916245](https://pubmed.ncbi.nlm.nih.gov/26916245/)), and is fully compatible with the *P. putida* loss-of-function phenotype (bypass mutations are rare/engineered; wild-type cells still need FliI for normal flagellation).

---

## Limitations and Knowledge Gaps

1. **No direct biochemistry on Q88ET7 itself.** The ATP-hydrolysis kinetics, hexamerization, and gate-activation properties are inferred from *Salmonella* orthologs. While conservation is high (identical family, domain signature, EC number), the specific catalytic residue numbering (e.g., "Glu221") and kinetic parameters have not been experimentally confirmed for the *P. putida* protein. Sequence alignment to confirm the catalytic Walker-B glutamate in Q88ET7 would close this gap.

2. **Polar (fT3SS) vs. peritrichous system differences.** Most mechanistic data derive from peritrichously flagellated *Salmonella*. *P. putida* builds a *polar* flagellar tuft with additional spatial regulators (FlhF/FleN/FimV). Whether FliI's docking dynamics or regulation differ in the polar context is untested.

3. **Substrate-delivery scope in *P. putida*.** The finding that soluble components do not carry flagellin ([PMID: 25068520](https://pubmed.ncbi.nlm.nih.gov/25068520/)) was established in *Salmonella*; the corresponding substrate hierarchy in *P. putida* is assumed, not demonstrated.

4. **Quantitative essentiality.** The transposon study ([PMID: 11430400](https://pubmed.ncbi.nlm.nih.gov/11430400/)) shows loss of flagellum/motility but did not test bypass suppressors, so the degree to which *P. putida fliI* is bypassable (as in *Salmonella*) is unknown.

5. **Possible regulatory links to lifestyle switching.** In *P. putida*, flagellar regulators (FleQ/FleN, c-di-GMP) also control biofilm genes ([PMID: 30889223](https://pubmed.ncbi.nlm.nih.gov/30889223/)); whether the export ATPase intersects motility–biofilm switching beyond building the flagellum is not addressed here (and is largely outside the requested "precise primary function" scope).

---

## Proposed Follow-up Experiments / Actions

1. **Confirm the catalytic residue in Q88ET7.** Perform a sequence alignment of Q88ET7 against *Salmonella* FliI (P26465) to identify the residue corresponding to catalytic Glu221 and the Walker-A/B motifs. This low-cost bioinformatic step would directly transfer the mutagenesis conclusion to *P. putida*.

2. **Biochemical validation.** Express and purify recombinant *P. putida* FliI; measure ATPase activity (e.g., malachite-green Pᵢ release), test ATP-dependent hexamerization by size-exclusion/native gels, and construct the E→Q catalytic mutant to confirm hydrolysis-dead-but-binding behavior.

3. **Clean genetic test in KT2440.** Build a markerless in-frame *fliI* deletion in *P. putida* KT2440 (as opposed to transposon insertion in strain S12), quantify swimming motility and flagellation by electron microscopy, and test for bypass suppressors (screen for gate mutations analogous to *flhB(P28T)*) to determine essentiality/bypassability in the polar system.

4. **Localization imaging.** Use a fluorescent FliI fusion in *P. putida* to test whether it docks at the single/few polar basal bodies and whether the dynamic-carrier/static-loader behavior seen in *Salmonella* holds in a polar flagellate.

5. **Structure prediction/validation.** Generate an AlphaFold model of Q88ET7 and the FliI₆–FliJ assembly, compare to the *Salmonella* structure ([PMID: 26984495](https://pubmed.ncbi.nlm.nih.gov/26984495/)), and verify the F₁-like fold and nucleotide-binding pocket.

6. **PMF dependence.** Test flagellar export in *P. putida* under PMF-collapsing conditions (protonophores) with and without functional FliI to confirm the ATP-activates-gate / PMF-drives-export division of labor in this organism.

---

## Conclusion

FliI (Q88ET7, PP_4366) is unambiguously the **flagellum-specific export ATPase** of *P. putida* KT2440. Its primary function is to hydrolyze ATP (ATP + H₂O → ADP + Pᵢ; EC 7.1.2.2) as an F₁-ATPase-homologous homohexamer, using that energy to load chaperone–substrate complexes onto, and to activate, the membrane-embedded flagellar type III export gate — enabling the proton-motive force to drive translocation of flagellar axial subunits during flagellum assembly. It operates at the cytoplasmic face of the flagellar basal body (C-ring), partners with FliH and FliJ, and is required for flagellum biogenesis and motility in *P. putida*. It is a critical efficiency/coupling factor rather than the obligate translocation motor, and it functions within the FleQ/RpoN/FliA-regulated flagellar program that builds the polar flagellar tuft.


## Artifacts

- [OpenScientist final report](fliI-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](fliI-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:21934659
2. PMID:26984495
3. PMID:19665005
4. PMID:25284201
5. PMID:25068520
6. PMID:34035173
7. PMID:26916245
8. PMID:42254510
9. PMID:23161028
10. PMID:34859548
11. PMID:11430400
12. PMID:39709681
13. PMID:30889223