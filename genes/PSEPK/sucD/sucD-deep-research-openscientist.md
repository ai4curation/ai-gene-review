---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T18:29:12.685318'
end_time: '2026-07-11T18:43:55.203362'
duration_seconds: 882.52
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: sucD
  gene_symbol: sucD
  uniprot_accession: Q88FB3
  protein_description: 'RecName: Full=Succinate--CoA ligase [ADP-forming] subunit
    alpha {ECO:0000256|HAMAP-Rule:MF_01988}; EC=6.2.1.5 {ECO:0000256|HAMAP-Rule:MF_01988};
    AltName: Full=Succinyl-CoA synthetase subunit alpha {ECO:0000256|HAMAP-Rule:MF_01988};
    Short=SCS-alpha {ECO:0000256|HAMAP-Rule:MF_01988};'
  gene_info: Name=sucD {ECO:0000256|HAMAP-Rule:MF_01988, ECO:0000313|EMBL:AAN69766.1};
    OrderedLocusNames=PP_4185 {ECO:0000313|EMBL:AAN69766.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the succinate/malate CoA ligase alpha subunit
  protein_domains: Cit_synth/succinyl-CoA_lig_AS. (IPR017440); Citrt_syn/SCS-alpha_CS.
    (IPR033847); CoA-bd. (IPR003781); CoA_lig_alpha. (IPR005810); NAD(P)-bd_dom_sf.
    (IPR036291)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 11
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: sucD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: sucD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88FB3
- **Protein Description:** RecName: Full=Succinate--CoA ligase [ADP-forming] subunit alpha {ECO:0000256|HAMAP-Rule:MF_01988}; EC=6.2.1.5 {ECO:0000256|HAMAP-Rule:MF_01988}; AltName: Full=Succinyl-CoA synthetase subunit alpha {ECO:0000256|HAMAP-Rule:MF_01988}; Short=SCS-alpha {ECO:0000256|HAMAP-Rule:MF_01988};
- **Gene Information:** Name=sucD {ECO:0000256|HAMAP-Rule:MF_01988, ECO:0000313|EMBL:AAN69766.1}; OrderedLocusNames=PP_4185 {ECO:0000313|EMBL:AAN69766.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the succinate/malate CoA ligase alpha subunit
- **Key Domains:** Cit_synth/succinyl-CoA_lig_AS. (IPR017440); Citrt_syn/SCS-alpha_CS. (IPR033847); CoA-bd. (IPR003781); CoA_lig_alpha. (IPR005810); NAD(P)-bd_dom_sf. (IPR036291)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "sucD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'sucD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **sucD** (gene ID: sucD, UniProt: Q88FB3) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *sucD* (Q88FB3) — Succinyl-CoA Synthetase α-Subunit of *Pseudomonas putida* KT2440

## Summary

The gene **sucD** (ordered locus **PP_4185**; UniProt **Q88FB3**) of *Pseudomonas putida* KT2440 encodes the **α-subunit of succinyl-CoA synthetase (SCS)**, also called succinate–CoA ligase [ADP-forming] (**EC 6.2.1.5**). This enzyme catalyzes the reversible conversion **succinyl-CoA + Pi + ADP ⇌ succinate + CoA + ATP** — the single **substrate-level phosphorylation** step of the tricarboxylic acid (TCA/citric acid) cycle. Gene identity is unambiguous: the UniProt record, the KEGG genome annotation, the assigned protein family ("succinate/malate CoA ligase alpha subunit"), and the diagnostic domain architecture (CoA-binding domain IPR003781; CoA_lig_alpha IPR005810) all converge on the same well-characterized enzyme, and no conflicting literature for a differently-functioned "sucD" was found for this organism.

Within the two-subunit enzyme, the **α-subunit (SucD) contributes the two catalytically essential components**: the **CoA-binding site**, located in its N-terminal Rossmann-like domain, and the **catalytic histidine** (His247 in Q88FB3) that is transiently phosphorylated during catalysis to form a phosphohistidine intermediate. The partner **β-subunit (SucC, PP_4186)** supplies the **dicarboxylate (succinate) binding site** and determines **nucleotide specificity** (ADP/ATP vs. GDP/GTP). The active enzyme assembles as a soluble, cytoplasmic **(αβ)₂ heterotetramer**. Direct sequence analysis of Q88FB3 confirms the conserved catalytic phosphohistidine motif and the N-terminal glycine-rich CoA/Rossmann motif, and a very-high-confidence AlphaFold model (mean pLDDT 96.5) supports the canonical two-domain SCS-α fold in the actual *P. putida* protein.

Functionally, SucD operates in the **cytoplasm** as part of the TCA cycle, contributing to central carbon metabolism, energy generation, and — through the succinate/succinyl-CoA node — connections to propanoate metabolism and C5-branched dibasic acid metabolism. In pseudomonads the enzyme has notably **broad NTP-synthesizing capacity** and physically couples with **nucleoside diphosphate kinase (Ndk)**, positioning it as a contributor to cellular nucleotide-triphosphate pools beyond just ATP. This report is built on a four-tier evidence base: (1) the intrinsic sequence/structure of Q88FB3, (2) KEGG genome context in *P. putida* KT2440, (3) direct biochemical work in the close relative *P. aeruginosa*, and (4) mechanistic crystallographic studies of orthologous SCS enzymes from *E. coli*, pig heart, and *Thermus aquaticus*.

---

## Key Findings

### Finding 1 — sucD encodes the α-subunit catalyzing the TCA cycle's only substrate-level phosphorylation

The gene **sucD (Q88FB3 / PP_4185)** encodes the α-subunit of succinyl-CoA synthetase, assigned **EC 6.2.1.5** (Succinate–CoA ligase [ADP-forming]). SCS catalyzes the reversible reaction:

> **succinyl-CoA + Pi + NDP ⇌ succinate + CoA + NTP**

This is the **only reaction in the citric acid cycle that provides substrate-level phosphorylation** — that is, the direct synthesis of a nucleoside triphosphate coupled to a chemical bond transformation rather than to the electron-transport chain. The **[ADP-forming]** designation (EC 6.2.1.5) means the *P. putida* enzyme generates **ATP** (from ADP), in contrast to the GTP-forming isoform (EC 6.2.1.4) that uses GDP.

This defining catalytic role is directly stated in the literature: succinyl-CoA synthetase "catalyzes the only step in the citric acid cycle that provides substrate-level phosphorylation" ([PMID: 27487822](https://pubmed.ncbi.nlm.nih.gov/27487822/)), and the enzyme "catalyses the reversible conversion of succinyl-CoA and ADP or GDP to succinate and ATP or GTP" ([PMID: 18392745](https://pubmed.ncbi.nlm.nih.gov/18392745/)). The reversibility is physiologically important: in the oxidative direction the enzyme conserves the energy of the succinyl-CoA thioester bond as a phosphoanhydride bond in NTP, while in the reverse direction it can activate succinate to succinyl-CoA.

### Finding 2 — The α-subunit carries the CoA-binding site and the transiently phosphorylated catalytic histidine

Crystallographic dissection of SCS orthologs establishes that the **α-subunit (SucD) contributes the two components most central to catalysis**:

1. **The CoA-binding site.** In *E. coli* SCS, "CoA is bound in an extended conformation to the nucleotide-binding motif in the N-terminal domain of the alpha-subunit" ([PMID: 9917402](https://pubmed.ncbi.nlm.nih.gov/9917402/)). The GTP-specific pig-heart structure confirms this: "CoA bound to the amino-terminal domain of the α-subunit, with the free thiol extending from the adenine portion into the site where the catalytic histidine residue resides" ([PMID: 26249701](https://pubmed.ncbi.nlm.nih.gov/26249701/)).

2. **The catalytic histidine (phosphohistidine intermediate).** During the reaction a histidine of the α-subunit is transiently phosphorylated, forming a covalent phospho-enzyme intermediate. This mobile histidine must **shuttle the phosphoryl group** between the CoA/succinate site and the nucleotide site — indeed "the catalytic histidine residue would have to move about 35 Å to react with the nucleotide" ([PMID: 9917402](https://pubmed.ncbi.nlm.nih.gov/9917402/)). The phosphoryl group is stabilized at the amino termini of two "power" helices, one from the C-terminal domain of the α-subunit and one from the β-subunit.

Critically, **nucleotide specificity does NOT reside in the α-subunit.** The ATP-specific and GTP-specific isoforms of pigeon SCS "incorporate the same alpha-subunit," so "the determinants of nucleotide specificity must reside within the beta-subunit" ([PMID: 9765290](https://pubmed.ncbi.nlm.nih.gov/9765290/)). This means SucD provides the invariant catalytic machinery (CoA binding + phosphohistidine), while its partner SucC (β) tunes which nucleotide is used.

### Finding 3 — Strict substrate specificity for succinate/succinyl-CoA, with the dicarboxylate site on the β-subunit

The enzyme is highly selective for its C4-dicarboxylate substrate. The SCS·succinate·Mg·CoA complex shows that "succinate binds in the carboxy-terminal domain of the β-subunit," and this "succinate-binding site is near both the active-site histidine residue that is phosphorylated in the reaction and the free thiol of CoA" ([PMID: 27487822](https://pubmed.ncbi.nlm.nih.gov/27487822/)). The architecture positions the α-subunit's CoA thiol and catalytic histidine immediately adjacent to the β-subunit's dicarboxylate pocket, allowing the thioester-forming/phosphoryl-transfer chemistry to proceed.

The specificity is strict: the structure "shows why succinyl-CoA synthetase is specific for succinate and does not react appreciably with citrate nor with the other C4-dicarboxylic acids of the citric acid cycle, fumarate and oxaloacetate, but shows some activity with L-malate" ([PMID: 27487822](https://pubmed.ncbi.nlm.nih.gov/27487822/)). Thus, although SucD supplies the universal CoA moiety, the enzyme as a whole discriminates strongly in favor of succinate over other TCA-cycle dicarboxylic acids — a property conferred largely by the β-subunit's binding pocket and its domain-closure rearrangement upon substrate binding.

### Finding 4 — Encoded in the sucCD operon; functions as a cytoplasmic (αβ)₂ tetramer coupled to Ndk with broad NTP-synthesizing capacity

In the close relative *Pseudomonas aeruginosa*, the **sucCD operon encodes the α (sucD) and β (sucC) subunits** of SCS ([PMID: 10671455](https://pubmed.ncbi.nlm.nih.gov/10671455/)). The *P. aeruginosa* enzyme displays **remarkably broad nucleotide usage**: "In the presence of inorganic orthophosphate (Pi), succinyl-CoA, and either GDP, ADP, UDP or CDP, it synthesizes GTP, ATP, UTP, or CTP" ([PMID: 10671455](https://pubmed.ncbi.nlm.nih.gov/10671455/)). Furthermore, the Pseudomonas SCS physically and functionally couples with **nucleoside diphosphate kinase (Ndk)**, modulating its NTP-synthesis specificity — positioning SCS as a broader contributor to the cellular NTP pool than the canonical ATP-only description would suggest.

Structurally, bacterial SCS assembles as a **heterotetramer of two α- and two β-subunits** — for *T. aquaticus* SCS, "the enzyme is a heterotetramer of two α-subunits and two β-subunits" ([PMID: 22751660](https://pubmed.ncbi.nlm.nih.gov/22751660/)). As a citric-acid-cycle enzyme, SCS operates in the **bacterial cytoplasm**; in eukaryotes the orthologous enzyme is a **mitochondrial matrix enzyme** ([PMID: 18392745](https://pubmed.ncbi.nlm.nih.gov/18392745/)), the compartment that houses the TCA cycle. For *P. putida*, the cytoplasm is therefore the site of SucD's function.

### Finding 5 — Q88FB3's own sequence confirms the catalytic phosphohistidine (His247) and N-terminal CoA-binding domain

Analysis of the actual *P. putida* protein sequence — rather than reliance on orthologs alone — confirms the SCS-α mechanism applies here. The UniProt Q88FB3 record (294 aa; KEGG ppu:PP_4185; EMBL AAN69766.1) annotates:

- An **active site at His247**, described as a *"Tele-phosphohistidine intermediate"* — the catalytic residue that is transiently phosphorylated. Direct sequence inspection confirms residue 247 is histidine, embedded in the conserved motif **…PAGKRMG-H247-AGAIISGG…** (the diagnostic G-H-A-G phosphohistidine signature). His247 is the positional equivalent of the experimentally characterized catalytic His246α of *E. coli* SCS.
- A **CoA-binding domain spanning residues 4–100**, with the N-terminus containing the glycine-rich CoA/Rossmann motif **G16-F-T-G-S-Q-G22** (coincident with annotated binding site 17–20), plus additional ligand-binding residues at 43, 96–98, and 159.

The protein matches the diagnostic PROSITE signatures **PS01216 (SUCCINYL_COA_LIG_1)** and **PS00399 (SUCCINYL_COA_LIG_2)** and Pfam families **PF02629 (CoA_binding)** + **PF00549 (Ligase_CoA)**. The literature confirms this catalytic residue is on the α-subunit: "During the reaction, a histidine residue of the alpha-subunit is transiently phosphorylated" ([PMID: 11781092](https://pubmed.ncbi.nlm.nih.gov/11781092/)), and the N-terminal CoA-binding motif matches the "nucleotide-binding motif in the N-terminal domain of the alpha-subunit" ([PMID: 9917402](https://pubmed.ncbi.nlm.nih.gov/9917402/)).

### Finding 6 — Genomic context: a canonical TCA gene cluster in *P. putida* KT2440

KEGG genome annotation places **PP_4185 (sucD)** — ortholog **K01902** ("succinyl-CoA synthetase alpha subunit [EC:6.2.1.5]") — **immediately adjacent to PP_4186 (sucC)**, ortholog K01903 ("succinyl-CoA synthetase beta subunit"), followed by **PP_4187 (lpdG / dihydrolipoyl dehydrogenase, K00382)**. This is a canonical TCA-cluster arrangement. sucD is assigned to **KEGG module M00011** (Citrate cycle, second carbon oxidation: 2-oxoglutarate ⇒ oxaloacetate) and to pathways:

| KEGG pathway | Description |
|---|---|
| ppu00020 | Citrate cycle (TCA cycle) |
| ppu00640 | Propanoate metabolism |
| ppu00660 | C5-branched dibasic acid metabolism |
| ppu01200 | Carbon metabolism |

Notably, the β-subunit PP_4186 additionally carries the annotation "glutaryl-CoA synthetase, beta subunit," hinting at a broader dicarboxylyl-CoA metabolic context in this organism. This directly confirms — in *P. putida* KT2440 itself — the operonic pairing of sucD/sucC and the assignment of SucD to the TCA cycle and connected pathways.

### Finding 7 — Very-high-confidence AlphaFold model supports a well-ordered two-domain fold

The AlphaFold DB model **AF-Q88FB3-F1** (294 residues) is of **very high confidence**: global pLDDT of 96.56, with per-residue analysis showing mean pLDDT 96.5, **90.8% of residues at very-high confidence (>90)**, 99.3% confident (>70), and **0% low confidence (<50)**. This strongly supports a well-ordered, canonical SCS-α architecture in the actual *P. putida* protein: an N-terminal CoA-binding Rossmann-like domain (matching the UniProt CoA-binding domain, residues 4–100) and a C-terminal domain bearing the active-site histidine (His247). The absence of disordered regions is consistent with a stable, folded metabolic enzyme.

---

## Mechanistic Model / Interpretation

### The catalytic cycle

Succinyl-CoA synthetase operates through a **three-step, ping-pong-like mechanism** involving a covalent phosphohistidine intermediate on the α-subunit:

```
Step 1:  succinyl-CoA + Pi  →  succinyl-phosphate + CoA
Step 2:  succinyl-phosphate  →  succinate + P~His (phospho-enzyme)
Step 3:  P~His + NDP (ADP)   →  His + NTP (ATP)
------------------------------------------------------------
Net:     succinyl-CoA + Pi + ADP  ⇌  succinate + CoA + ATP
```

The **catalytic His247 of the α-subunit (SucD)** is the phosphoryl carrier. Because the CoA/succinate site and the nucleotide site are ~35 Å apart, the phosphohistidine loop must **physically swing** between the two sites, shuttling the phosphoryl group. Two glutamate residues (Glu208α and Glu197β in the studied ortholog) are crucial for the phosphorylation/dephosphorylation of this active-site histidine ([PMID: 11781092](https://pubmed.ncbi.nlm.nih.gov/11781092/)).

### Division of labor between subunits

```
        ┌─────────────────────────────────────────────┐
        │           SCS  (αβ)2 heterotetramer          │
        │                                              │
   α (SucD / PP_4185)              β (SucC / PP_4186)   │
   ─────────────────              ──────────────────    │
   • N-term CoA-binding domain    • Dicarboxylate site  │
     (Rossmann-like, res 4–100)     (succinate, C-term) │
   • Catalytic His247             • Nucleotide site     │
     (phosphohistidine)             → ADP/ATP vs GDP/GTP│
   • Provides INVARIANT             specificity         │
     catalytic machinery          • Provides SPECIFICITY│
        └─────────────────────────────────────────────┘
```

This division is the key mechanistic insight: **SucD is the "engine" (CoA + phosphohistidine chemistry) while SucC is the "selector" (which dicarboxylate, which nucleotide).** The two subunits form an intimate αβ dimer, two of which assemble into the functional (αβ)₂ tetramer.

### Physiological role in *P. putida*

*P. putida* KT2440 is an aerobic soil bacterium with a strongly oxidative, TCA-centered central metabolism. In this organism the classic glycolytic pathways are notably not part of tightly-regulated "central carbon metabolism" in the textbook sense ([PMID: 24951791](https://pubmed.ncbi.nlm.nih.gov/24951791/)), placing even greater importance on the TCA cycle for energy and precursor supply. SucD/SucC sit at the succinate node of this cycle, where:

- In the **oxidative TCA direction**, they conserve the thioester-bond energy of succinyl-CoA (produced by 2-oxoglutarate dehydrogenase) as ATP, regenerating free CoA and succinate (the latter feeding succinate dehydrogenase).
- Through the enzyme's **broad NTP-synthesizing capacity and coupling to Ndk** ([PMID: 10671455](https://pubmed.ncbi.nlm.nih.gov/10671455/)), it can help balance the cellular pools of ATP, GTP, UTP, and CTP.
- The succinate/succinyl-CoA node connects to **propanoate** and **C5-branched dibasic acid** metabolism (KEGG ppu00640, ppu00660), and — given the β-subunit's "glutaryl-CoA synthetase" annotation — potentially to broader dicarboxylyl-CoA metabolism relevant to *P. putida*'s renowned catabolic versatility (e.g., aromatic-compound degradation funneling carbon into the TCA cycle; [PMID: 25617773](https://pubmed.ncbi.nlm.nih.gov/25617773/)).

---

## Evidence Base

The functional assignment rests on a **four-tier evidence hierarchy**, from most organism-specific to most mechanistically detailed:

| Tier | Evidence type | Source(s) | What it establishes |
|---|---|---|---|
| 1 | Intrinsic sequence & structure of Q88FB3 | UniProt Q88FB3; AlphaFold AF-Q88FB3-F1 | His247 phosphohistidine, N-terminal CoA domain, canonical fold in the *actual* protein |
| 2 | Genome context in *P. putida* KT2440 | KEGG ppu:PP_4185 | sucCD operon; TCA cycle + connected pathway assignment |
| 3 | Direct biochemistry in a close relative | *P. aeruginosa* SCS [PMID: 10671455] | sucCD operon; broad NTP synthesis; Ndk coupling |
| 4 | Mechanistic crystallography of orthologs | *E. coli*, pig heart, *T. aquaticus* SCS | catalytic mechanism, subunit division of labor, substrate specificity |

### Key papers

| PMID | Title (abbreviated) | How it supports the findings |
|---|---|---|
| [27487822](https://pubmed.ncbi.nlm.nih.gov/27487822/) | *Structural basis for the binding of succinate to succinyl-CoA synthetase* | Defines SCS as the sole substrate-level phosphorylation step; localizes succinate to β-subunit; documents strict specificity vs. citrate/fumarate/OAA |
| [9917402](https://pubmed.ncbi.nlm.nih.gov/9917402/) | *A detailed structural description of E. coli succinyl-CoA synthetase* | CoA binds N-terminal domain of α-subunit; catalytic His travels ~35 Å |
| [26249701](https://pubmed.ncbi.nlm.nih.gov/26249701/) | *Structure of GTP-specific succinyl-CoA synthetase in complex with CoA* | Confirms CoA + catalytic His localize to α-subunit |
| [9765290](https://pubmed.ncbi.nlm.nih.gov/9765290/) | *ATP- and GTP-specific SCS in pigeon... same alpha-subunit* | Nucleotide specificity resides in β, not α (SucD) |
| [11781092](https://pubmed.ncbi.nlm.nih.gov/11781092/) | *Two glutamate residues crucial for phosphorylation of active-site His* | Confirms α-subunit catalytic histidine; identifies Glu residues for (de)phosphorylation |
| [10671455](https://pubmed.ncbi.nlm.nih.gov/10671455/) | *Succinyl-CoA synthetase of P. aeruginosa... broad NTP specificity* | sucCD operon in Pseudomonas; broad NTP synthesis; Ndk coupling |
| [22751660](https://pubmed.ncbi.nlm.nih.gov/22751660/) | *GTP-preferring SCS from Thermus aquaticus* | (αβ)₂ heterotetramer quaternary structure |
| [18392745](https://pubmed.ncbi.nlm.nih.gov/18392745/) | *Disorders caused by deficiency of succinate-CoA ligase* | Reversible reaction; ADP/GDP-forming isoform distinction; mitochondrial matrix localization (eukaryote) |
| [24951791](https://pubmed.ncbi.nlm.nih.gov/24951791/) | *Functional structure of central carbon metabolism in P. putida KT2440* | Context for TCA-centered metabolism in the target organism |
| [25617773](https://pubmed.ncbi.nlm.nih.gov/25617773/) | *Aromatic catabolic pathway selection... in P. putida* | Aromatic degradation funnels carbon (incl. succinate) into TCA cycle |

**Consistency check:** No paper contradicted the assignment. All mechanistic studies, whether on ATP- or GTP-specific isoforms, agree that the α-subunit universally provides CoA binding and the catalytic phosphohistidine — exactly the components annotated in Q88FB3. The pig-heart/pigeon eukaryotic work and the bacterial *E. coli*/*T. aquaticus*/*P. aeruginosa* work are mutually consistent, differing only in localization (mitochondrial matrix vs. cytoplasm) and nucleotide preference (a β-subunit property).

---

## Limitations and Knowledge Gaps

1. **No *P. putida*-specific biochemical study.** There is no direct enzymatic characterization of the KT2440 SucD/SucC enzyme itself (kinetic constants, nucleotide preference, subunit stoichiometry). The functional assignment relies on (a) the intrinsic sequence/structure of Q88FB3, (b) genome annotation, and (c) inference from the close relative *P. aeruginosa* and from more distant, structurally characterized orthologs. While these lines converge strongly, the specific catalytic parameters (Km, kcat, nucleotide preference) of the *P. putida* enzyme remain experimentally undetermined.

2. **Nucleotide preference not directly measured.** The EC 6.2.1.5 [ADP-forming] annotation implies ATP formation, but the *P. aeruginosa* ortholog shows unusually broad NDP usage (ADP/GDP/UDP/CDP). Whether *P. putida* SucD/SucC is strictly ATP-forming or similarly promiscuous has not been tested directly.

3. **Structure is predicted, not experimental.** The AlphaFold model, while very high confidence (pLDDT 96.5), is a computational prediction. No experimental crystal or cryo-EM structure of the *P. putida* enzyme exists. Ligand-bound conformational states (open/closed) and the exact geometry of the His247 loop are inferred from orthologs.

4. **Physiological regulation unexplored.** How sucCD expression and SCS flux are regulated in *P. putida* under different carbon sources (e.g., during aromatic-compound catabolism) is not directly addressed. Studies in KT2440 emphasize post-transcriptional/metabolic regulation of central metabolism ([PMID: 24951791](https://pubmed.ncbi.nlm.nih.gov/24951791/)), but the specific regulation of SucD is unknown.

5. **The β-subunit "glutaryl-CoA synthetase" annotation** is intriguing but unverified for moonlighting/alternative activity in this organism.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and kinetic characterization.** Clone the *P. putida* KT2440 sucCD operon, purify the recombinant (αβ)₂ enzyme, and measure kinetic parameters (Km, kcat) for succinyl-CoA, Pi, and each NDP (ADP, GDP, UDP, CDP) to determine whether the KT2440 enzyme shares the broad NTP-synthesizing capacity documented for *P. aeruginosa*.

2. **Site-directed mutagenesis of His247.** Mutate His247→Ala (or His247→Asn) and confirm loss of catalytic activity, directly validating the phosphohistidine mechanism in the *P. putida* protein. Complement with ³²P-labeling to demonstrate transient phosphorylation of the α-subunit.

3. **Experimental structure determination.** Solve the crystal or cryo-EM structure of the *P. putida* SCS, ideally with bound CoA and/or succinate, to confirm the predicted fold and the geometry of the catalytic site relative to the AlphaFold model.

4. **Ndk interaction assay.** Test whether *P. putida* SucD/SucC physically associates with and modulates nucleoside diphosphate kinase, as observed in *P. aeruginosa*, using pull-down or co-purification approaches.

5. **Gene deletion / conditional knockdown.** Construct a ΔsucCD strain (or conditional mutant) and assess growth phenotypes on TCA-cycle-dependent carbon sources (e.g., succinate, aromatic compounds) and rescue by succinate supplementation, paralleling the succinyl-CoA-synthetase knockout approach used in *Toxoplasma* ([PMID: 18336823](https://pubmed.ncbi.nlm.nih.gov/18336823/)).

6. **Flux analysis under aromatic catabolism.** Given *P. putida*'s biotechnological importance for lignin valorization ([PMID: 25617773](https://pubmed.ncbi.nlm.nih.gov/25617773/)), quantify SCS flux and the succinate node under different aromatic feedstocks to inform metabolic-engineering strategies.

---

## Conclusion

The gene symbol **sucD is unambiguous** for this target: Q88FB3 / PP_4185 encodes the **α-subunit of succinyl-CoA synthetase (succinate–CoA ligase [ADP-forming], EC 6.2.1.5)** of *Pseudomonas putida* KT2440. It catalyzes the reversible, ATP-generating conversion of **succinyl-CoA + Pi + ADP ⇌ succinate + CoA + ATP** — the TCA cycle's sole substrate-level phosphorylation. The α-subunit specifically provides the **CoA-binding site** and the **catalytic phosphohistidine (His247)**, while the partner β-subunit (SucC/PP_4186) supplies dicarboxylate and nucleotide specificity. The enzyme functions as a **soluble, cytoplasmic (αβ)₂ heterotetramer** encoded in the **sucCD operon**, participating in the TCA cycle and connected propanoate / C5-branched-dibasic-acid metabolism, and in pseudomonads couples to nucleoside diphosphate kinase with broad NTP-synthesizing capacity. All evidence tiers — intrinsic sequence, high-confidence structure prediction, genome context, and orthologous biochemistry/crystallography — converge on this assignment without contradiction.


## Artifacts

- [OpenScientist final report](sucD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](sucD-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:27487822
2. PMID:18392745
3. PMID:9917402
4. PMID:26249701
5. PMID:9765290
6. PMID:10671455
7. PMID:22751660
8. PMID:11781092
9. PMID:24951791
10. PMID:25617773
11. PMID:18336823