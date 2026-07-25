---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T04:40:47.248446'
end_time: '2026-07-17T05:01:39.957589'
duration_seconds: 1252.71
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: hisZ
  gene_symbol: hisZ
  uniprot_accession: Q88DD7
  protein_description: 'RecName: Full=ATP phosphoribosyltransferase regulatory subunit
    {ECO:0000255|HAMAP-Rule:MF_00125};'
  gene_info: Name=hisZ {ECO:0000255|HAMAP-Rule:MF_00125}; OrderedLocusNames=PP_4890;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the class-II aminoacyl-tRNA synthetase family.
  protein_domains: aa-tRNA-synth_II/BPL/LPL. (IPR045864); HisRS-like_core. (IPR041715);
    HisRS/HisZ. (IPR004516); HisZ. (IPR004517); tRNA-synt_His (PF13393)
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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: hisZ-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: hisZ-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88DD7
- **Protein Description:** RecName: Full=ATP phosphoribosyltransferase regulatory subunit {ECO:0000255|HAMAP-Rule:MF_00125};
- **Gene Information:** Name=hisZ {ECO:0000255|HAMAP-Rule:MF_00125}; OrderedLocusNames=PP_4890;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the class-II aminoacyl-tRNA synthetase family.
- **Key Domains:** aa-tRNA-synth_II/BPL/LPL. (IPR045864); HisRS-like_core. (IPR041715); HisRS/HisZ. (IPR004516); HisZ. (IPR004517); tRNA-synt_His (PF13393)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "hisZ" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'hisZ' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **hisZ** (gene ID: hisZ, UniProt: Q88DD7) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *hisZ* (Q88DD7 / PP_4890) in *Pseudomonas putida* KT2440

## Identity Verification

- **UniProt accession:** Q88DD7
- **Gene / locus:** *hisZ* / PP_4890
- **Organism:** *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125), abbreviation **PSEPK**
- **Protein:** ATP phosphoribosyltransferase **regulatory subunit** (HisZ) — HAMAP rule MF_00125
- **Family / domains:** class-II aminoacyl-tRNA-synthetase fold (IPR045864); HisRS-like core (IPR041715); HisRS/HisZ (IPR004516); HisZ (IPR004517); Pfam PF13393 (tRNA-synt_His)

**Outcome:** The gene symbol *hisZ* is consistent across all evidence. The UniProt description ("ATP phosphoribosyltransferase regulatory subunit"), the HisRS-like/HisZ domain architecture, and the HAMAP MF_00125 rule all coincide with the well-defined **HisZ** protein family. There is no symbol collision — "hisZ" is used uniformly for this regulatory subunit throughout the histidine-biosynthesis literature. Direct primary studies of the *P. putida* KT2440 protein itself are limited, so the functional description is built from (i) curated UniProt/HAMAP/InterPro annotation of Q88DD7, (ii) organism-specific sequence and comparative-genomics evidence generated in this investigation, and (iii) precise mechanistic/structural studies of orthologous HisZ proteins (*Lactococcus lactis*, *Thermotoga maritima*, *Psychrobacter arcticus*), whose mechanism is strongly conserved across the family.

---

## Summary

**hisZ** (UniProt **Q88DD7**, ordered locus **PP_4890**) of *Pseudomonas putida* KT2440 encodes **HisZ, the regulatory subunit of ATP phosphoribosyltransferase (ATP-PRT, EC 2.4.2.17)**, the enzyme catalyzing the first and committed step of L-histidine biosynthesis. HisZ is a **catalytically inactive paralog of the class-II histidyl-tRNA synthetase (HisRS)**: it retains the HisRS catalytic core fold but has lost aminoacylation activity and has instead been evolutionarily repurposed as an obligatory, non-catalytic partner of the catalytic subunit HisG. HisZ does not itself carry out the chemistry of the reaction; rather, it is required for that chemistry to occur and for its physiological regulation.

The functional unit is a **hetero-octameric complex** of four catalytic **HisG_S** subunits (the "short-form" catalytic subunit) and four regulatory **HisZ** subunits (~220 kDa total, 4:4 stoichiometry). Only the complete octamer is catalytically active — isolated short-form HisG has little activity on its own. HisZ activates catalysis allosterically by making new contacts with the HisG_S dimer interface that restructure the active site and recruit conserved residues to activate the pyrophosphate leaving group. HisZ additionally builds the allosteric sites, located at the HisG_S–HisZ subunit interfaces, through which the pathway end-product **L-histidine** feedback-inhibits the enzyme (and through which AMP reports cellular energy charge).

In *P. putida*, comparative genomics provides an organism-specific diagnostic signature confirming this arrangement: the catalytic subunit HisG (PP_0965, Q88P87) is only **211 amino acids** — the short catalytic form (HisG_S) that lacks the C-terminal allosteric domain of long-form ATP-PRTs — and therefore requires a separate HisZ subunit for both activation and feedback regulation. The reaction catalyzed is the Mg²⁺-dependent condensation of **ATP + 5-phospho-α-D-ribosyl-1-pyrophosphate (PRPP) → N'-5'-phosphoribosyl-ATP (PR-ATP) + pyrophosphate (PPi)** — step 1 of 9 in the pathway from PRPP to L-histidine. The protein functions in the **cytoplasm**.

---

## Key Findings

### Finding 1 — HisZ is the regulatory subunit of ATP-PRT, a catalytically dead HisRS paralog essential for histidine biosynthesis

HisZ proteins are built on the catalytic core of **class-II histidyl-tRNA synthetase (HisRS)** but lack the aminoacylation activity of a true synthetase. Instead they serve an essential role in the first enzyme of histidine biosynthesis. This was established in the founding study by Sissler and colleagues in *Lactococcus lactis*, where HisZ was shown to be required for histidine prototrophy: complementation of an in-frame *hisG* deletion in *E. coli* required **both** the *L. lactis* HisG **and** HisZ proteins; HisG and HisZ co-eluted during affinity chromatography, demonstrating a **direct physical interaction**; and both subunits were required for catalysis of the ATP-PRT reaction ([PMID: 10430882](https://pubmed.ncbi.nlm.nih.gov/10430882/)).

The identity of Q88DD7 as this regulatory subunit is reinforced by curated, rule-based annotation. UniProt Q88DD7 is annotated by **HAMAP rule MF_00125** as the ATP phosphoribosyltransferase regulatory subunit HisZ, and its domain complement — **PF13393 (tRNA-synt_His)** with InterPro signatures **IPR004516 (HisRS/HisZ)** and **IPR004517 (HisZ)** — places it unambiguously in the HisRS/HisZ family. Two verbatim conclusions from the founding paper capture the function:

> "members lack aminoacylation activity but are instead essential components of the first enzyme in histidine biosynthesis ATP phosphoribosyltransferase (HisG)" ([PMID: 10430882](https://pubmed.ncbi.nlm.nih.gov/10430882/))

> "Both HisG and HisZ are required for catalysis of the ATP phosphoribosyltransferase reaction" ([PMID: 10430882](https://pubmed.ncbi.nlm.nih.gov/10430882/))

HisZ is therefore not an enzyme in its own right in this pathway (it does not aminoacylate tRNA) but is an indispensable component of the ATP-PRT holoenzyme.

### Finding 2 — HisZ forms a hetero-octameric ATP-PRT (4 HisG_S + 4 HisZ) and allosterically activates catalysis via subunit-interface rearrangement

The active enzyme is a **~220 kDa hetero-octameric complex** of four catalytic HisG_S subunits (adopting a periplasmic-binding-protein / type-II PBP fold) and four regulatory HisZ subunits. This architecture was defined crystallographically and biochemically in *Thermotoga maritima* (Vega et al. 2005) and *Lactococcus lactis* (Champagne et al. 2005). Critically, **kinetics show that only the complete octameric complex is catalytically active** — HisZ is a prerequisite for turnover, not a mere modulator.

The structural mechanism of activation is understood in detail. Crystallography of the PRPP-bound *L. lactis* complex revealed **new contacts between the HisZ motif-2 loop and the HisG_S dimer interface** in the activated state. These contacts "restructure the interface to recruit conserved residues to the active site, where they activate pyrophosphate to promote catalysis" (Champagne et al. 2005). HisZ thus acts allosterically across a subunit interface to remodel the HisG active site into a catalytically competent geometry. Consistent with this, in the short-form *Psychrobacter arcticus* enzyme, HisZ binding **shifts the rate-limiting step**, the kinetic hallmark of genuine allosteric activation (Fisher et al. 2018).

> "220 kDa hetero-octameric complex comprising four catalytic subunits (HisGS) and four regulatory subunits (HisZ)" ([PMID: 15660995](https://pubmed.ncbi.nlm.nih.gov/15660995/))

> "only the complete octameric complex is active" ([PMID: 15660995](https://pubmed.ncbi.nlm.nih.gov/15660995/))

> "new contacts between the HisZ motif 2 loop and the HisG(S) dimer interface. These contacts restructure the interface to recruit conserved residues to the active site, where they activate pyrophosphate to promote catalysis" ([PMID: 16051603](https://pubmed.ncbi.nlm.nih.gov/16051603/))

### Finding 3 — The complex catalyzes the committed first step of histidine biosynthesis, and HisZ mediates histidine feedback inhibition

The reaction catalyzed is the joining of **ATP and PRPP to form N'-5'-phosphoribosyl-ATP (PR-ATP) + PPi** — the **first, committed, and rate-controlling step** of histidine biosynthesis. Steady-state kinetics for the *L. lactis* hetero-octamer give **Km(PRPP) = 18.4 ± 3.5 µM** and **kcat = 2.7 ± 0.3 s⁻¹** (Champagne et al. 2006). The enzyme is regulated by two physiologically important ligands: the pathway end-product **L-histidine is a noncompetitive inhibitor (Ki = 81 µM)**, providing classic negative feedback, while **AMP is a competitive inhibitor (Ki = 1.44 mM)**, coupling flux into the energetically expensive histidine pathway to cellular energy charge.

HisZ is directly implicated in feedback control: the *T. maritima* complex has **eight histidine-binding sites located within the four HisG_S–HisZ subunit interfaces**, and the complex is non-competitively inhibited by histidine (Vega et al. 2005). The allosteric inhibition of short-form ATP-PRTs by histidine has since been dissected structurally in *P. arcticus* (Thomson et al. 2019; Read et al. 2022). HisZ therefore contributes not only to activation but also provides the molecular surface on which end-product inhibition is built — the ancestral HisRS histidine-binding pocket has been repurposed to sense histidine rather than to charge tRNA^His.

> "Histidine and AMP were determined to be noncompetitive (Ki = 81.1 microM) and competitive (Ki = 1.44 mM) inhibitors" ([PMID: 17154531](https://pubmed.ncbi.nlm.nih.gov/17154531/))

> "eight histidine binding sites that are located within each of the four HisGS-HisZ subunit interfaces" ([PMID: 15660995](https://pubmed.ncbi.nlm.nih.gov/15660995/))

### Finding 4 — *P. putida* encodes a short-form HisG (PP_0965, 211 aa) plus HisZ (PP_4890, 395 aa), confirming a HisZ-dependent hetero-octameric ATP-PRT

The organism-specific evidence in *P. putida* is decisive. UniProt Q88DD7 (395 aa) is annotated: **FUNCTION** "Required for the first step of histidine biosynthesis. May allow the feedback regulation of ATP phosphoribosyltransferase activity by histidine"; **PATHWAY** "L-histidine biosynthesis; L-histidine from 5-phospho-alpha-D-ribose 1-diphosphate: step 1/9"; **SUBUNIT** "Heteromultimer composed of HisG and HisZ subunits"; **SUBCELLULAR LOCATION** "Cytoplasm"; **SIMILARITY** "class-II aminoacyl-tRNA synthetase family, HisZ subfamily."

The critical comparative-genomics signature is the length of the co-encoded catalytic subunit. In *P. putida*, HisG (Q88P87, PP_0965) is only **211 amino acids** — the **short catalytic form (HisG_S)** that lacks the C-terminal allosteric/regulatory domain found in long-form (single-subunit, ~290–300 aa) HisG proteins. Sissler et al. showed by comparative genomics that HisZ co-occurs precisely with short HisG polypeptides. The presence of a 211-aa HisG plus a HisZ in *P. putida* therefore diagnoses a **HisZ-dependent hetero-octameric ATP-PRT** in this organism, rather than relying on ortholog inference alone. Notably, *hisG* (PP_0965) and *hisZ* (PP_4890) map to **distant, non-adjacent loci**, indicating the two subunits are independently transcribed yet must co-assemble into the hetero-octamer — the *his* genes are dispersed across the genome rather than in a single contiguous operon.

> "comparative genomics, a technique that revealed a link between the presence or the absence of HisZ and a systematic variation in the length of the HisG polypeptide" ([PMID: 10430882](https://pubmed.ncbi.nlm.nih.gov/10430882/))

### Finding 5 — Bioinformatic confirmation: *P. putida* HisZ is a bona fide HisRS-fold paralog with no signal peptide, consistent with a cytoplasmic, repurposed protein

Independent, organism-specific sequence analysis confirms the annotation. A **Smith–Waterman local alignment** (BLOSUM62, gap penalty −8) of *P. putida* HisZ (Q88DD7, 395 aa) against *E. coli* histidyl-tRNA synthetase HisS (P60906, 424 aa) yields a **best score of 100**, versus shuffled-sequence controls of **32–41** (~2.6-fold over random). This demonstrates statistically clear homology to the class-II HisRS catalytic core and confirms Q88DD7 is a genuine HisRS-fold paralog (HAMAP HisZ subfamily), consistent with InterPro IPR004516/IPR004517 and Pfam PF13393.

The N-terminus (`MATVDRWLLPDGIEE...`) begins with a cytoplasmic-type Met-Ala start and contains **no cleavable signal peptide or N-terminal transmembrane segment**, consistent with the curated **cytoplasmic** localization. The protein therefore carries out its function in the cytoplasm, the compartment where histidine biosynthesis takes place, as a soluble component of the ATP-PRT complex.

---

## Mechanistic Model / Interpretation

The findings converge on a single, well-supported model. *P. putida* KT2440 uses the **"short-form" ATP phosphoribosyltransferase** solution — one of the two evolutionary strategies bacteria employ to build and regulate the first enzyme of histidine biosynthesis. In long-form ATP-PRTs, a single ~290–300 aa HisG polypeptide carries both the catalytic domain and a C-terminal allosteric ferredoxin-like domain that binds histidine. In the short-form solution used by *P. putida*, HisG is truncated to ~211 aa (catalysis only), and the missing regulatory function is supplied *in trans* by a separate protein — **HisZ** — that evolved from a duplicated histidyl-tRNA synthetase.

```
                Histidine biosynthesis — committed step 1/9
                =============================================

   ATP  +  PRPP  ───────────────────────────────►  PR-ATP  +  PPi
                          ▲
                          │ catalysis requires the ASSEMBLED complex
                          │
        ┌─────────────────────────────────────────────┐
        │        HETERO-OCTAMER  (~220 kDa)            │
        │                                              │
        │   4 × HisG_S  (PP_0965, 211 aa, catalytic)   │
        │        +                                     │
        │   4 × HisZ    (PP_4890, 395 aa, regulatory)  │
        │                                              │
        │   • HisZ = catalytically-dead HisRS paralog  │
        │   • HisZ motif-2 loop contacts HisG_S dimer  │
        │     interface → restructures active site →   │
        │     activates PPi leaving group (ACTIVATION) │
        │   • 8 histidine sites at HisG_S–HisZ         │
        │     interfaces → feedback inhibition         │
        │   • AMP competitive inhibitor (energy charge)│
        └─────────────────────────────────────────────┘
                          │
                          ▼
              subcellular location: CYTOPLASM
```

HisZ has a **dual regulatory role**:

1. **Positive (activation).** HisZ is obligatory for catalysis. Its motif-2 loop docks onto the HisG_S dimer interface and remodels the active site, recruiting conserved residues that activate the pyrophosphate leaving group. Isolated HisG_S is essentially inactive; the complete octamer is active. In psychrophilic *P. arcticus*, HisZ binding shifts the rate-limiting step, the kinetic signature of allosteric activation.

2. **Negative (feedback inhibition).** The eight histidine-binding sites reside at the four HisG_S–HisZ interfaces. When intracellular histidine is abundant, it binds these interfacial sites and non-competitively inhibits the enzyme, throttling flux into the pathway. AMP additionally inhibits competitively, linking histidine production (an ATP-expensive process) to the cell's energy status.

The following table places the *P. putida* enzyme in the context of the model systems that established the mechanism:

| Feature | *P. putida* KT2440 (this target) | *L. lactis* | *T. maritima* | *P. arcticus* |
|---|---|---|---|---|
| Catalytic subunit (HisG_S) | PP_0965, 211 aa | short-form | short-form | short-form (HisG_S) |
| Regulatory subunit (HisZ) | **PP_4890 / Q88DD7, 395 aa** | present | present | present |
| Holoenzyme | hetero-octamer (inferred) | hetero-octamer | 4×HisG_S + 4×HisZ, ~220 kDa | hetero-octamer |
| Key kinetics | (inferred by orthology) | Km(PRPP)=18.4 µM; kcat=2.7 s⁻¹ | — | rate-limiting-step shift on activation |
| His feedback | at HisG_S–HisZ interface (inferred) | Ki=81 µM (noncompetitive) | 8 interfacial sites, noncompetitive | structurally mapped |
| Localization | Cytoplasm | Cytoplasm | Cytoplasm | Cytoplasm |

The *P. putida* enzyme has not itself been crystallized or kinetically characterized, so its specific properties are **inferred by strong orthology** from these characterized systems, combined with the definitive local evidence (211-aa HisG + genuine HisZ paralog + cytoplasmic sequence features). This inference is robust because the diagnostic short-HisG/HisZ pairing is exactly the situation the founding comparative-genomics work established as requiring a HisZ-dependent hetero-octamer.

---

## Evidence Base

| PMID | Study (organism) | How it supports the annotation |
|---|---|---|
| [10430882](https://pubmed.ncbi.nlm.nih.gov/10430882/) | *An aminoacyl-tRNA synthetase paralog with a catalytic role in histidine biosynthesis* (*L. lactis*) | **Founding paper.** Defines HisZ as a HisRS paralog lacking aminoacylation, essential to ATP-PRT; both HisG and HisZ required for catalysis; comparative genomics links HisZ presence to short HisG — the exact *P. putida* signature. |
| [15660995](https://pubmed.ncbi.nlm.nih.gov/15660995/) | *Regulation of the hetero-octameric ATP-PRT from Thermotoga maritima by a tRNA synthetase-like subunit* | Establishes 4:4 HisG_S:HisZ ~220 kDa hetero-octamer; only the octamer is active; eight histidine sites at HisG_S–HisZ interfaces mediate noncompetitive feedback inhibition. |
| [16051603](https://pubmed.ncbi.nlm.nih.gov/16051603/) | *Activation of the hetero-octameric ATP-PRT through subunit interface rearrangement by a tRNA synthetase paralog* (*L. lactis*) | Structural mechanism of activation: HisZ motif-2 loop contacts HisG_S dimer interface, restructuring the active site to activate pyrophosphate. |
| [17154531](https://pubmed.ncbi.nlm.nih.gov/17154531/) | *Substrate recognition by the hetero-octameric ATP-PRT from Lactococcus lactis* | Steady-state kinetics (Km PRPP=18.4 µM, kcat=2.7 s⁻¹); histidine noncompetitive (Ki=81 µM), AMP competitive (Ki=1.44 mM). |
| [29940105](https://pubmed.ncbi.nlm.nih.gov/29940105/) | *Allosteric Activation Shifts the Rate-Limiting Step in a Short-Form ATP-PRT* (*P. arcticus*) | Shows HisZ binding allosterically activates HisG_S by shifting the rate-limiting step. |
| [31251578](https://pubmed.ncbi.nlm.nih.gov/31251578/) | *Mapping the Structural Path for Allosteric Inhibition of a Short-Form ATP-PRT by Histidine* | Structural dissection of histidine feedback inhibition in a short-form (HisG_S/HisZ) enzyme. |
| [34928596](https://pubmed.ncbi.nlm.nih.gov/34928596/) | *Allosteric Inhibition of ATPPRT* | Further structural/mechanistic detail on histidine allosteric inhibition of short-form ATP-PRT. |
| [38150593](https://pubmed.ncbi.nlm.nih.gov/38150593/) | *Crystal Structure, Steady-State, and Pre-Steady-State Kinetics of ...* (first step of histidine biosynthesis) | Additional structural/kinetic characterization of the ATP-PRT first-step enzyme. |

**Evidence quality note.** All mechanistic citations above are **precise, low-throughput studies** (X-ray crystallography, steady-state and pre-steady-state enzyme kinetics, targeted mutagenesis, and defined genetic complementation), not high-throughput screens. A dedicated PubMed search for *P. putida* KT2440-specific functional or essentiality data on *hisZ* returned no results, so the organism-specific assignment relies on (i) curated UniProt/HAMAP annotation of Q88DD7, (ii) sequence-level evidence generated in this investigation (short-form HisG PP_0965; significant HisRS homology; no signal peptide), and (iii) high-confidence orthology to the biochemically/structurally characterized HisZ proteins of *L. lactis*, *T. maritima*, and *P. arcticus*.

**Own bioinformatic analysis:** Smith–Waterman alignment of Q88DD7 vs *E. coli* HisRS (P60906) scored 100 vs 32–41 for shuffled controls, confirming genuine HisRS-fold homology; N-terminal sequence analysis found no signal peptide/TM segment, supporting cytoplasmic localization.

Note: several papers returned during literature searches (on two-component histidine-kinase signaling, histamine/microbiota biology, palmitoyltransferases, and pterin deaminases) are **not** relevant to this target. They surfaced because of the shared token "histidine"/"His" but concern unrelated proteins and were correctly excluded.

---

## Supported and Refuted Hypotheses

**Supported:**
- HisZ is the regulatory (non-catalytic) subunit of ATP-PRT — **supported** (annotation + orthologous genetics/biochemistry).
- HisZ is required for HisG activity / histidine biosynthesis — **supported** (Sissler 1999; Vega 2005).
- HisZ mediates end-product (histidine) allosteric feedback inhibition — **supported** (Vega 2005; Champagne 2006).
- HisZ localizes to the cytoplasm — **supported** (HAMAP annotation; soluble complex; no signal peptide).

**Refuted / ruled out:**
- HisZ retains histidyl-tRNA aminoacylation activity — **refuted** (the HisZ family lacks aminoacylation activity; Sissler 1999).
- HisZ is the catalytic phosphoribosyltransferase subunit — **refuted** (catalysis is by HisG_S; HisZ is regulatory/activating).

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of the *P. putida* enzyme.** There is no published crystal structure, kinetic dataset, or in vitro reconstitution specifically for PP_4890/PP_0965. All mechanistic and kinetic detail is inferred from orthologs. The inference is strong but not a substitute for direct measurement.
2. **Holoenzyme stoichiometry inferred, not measured.** The 4:4 hetero-octamer is established for orthologs; the *P. putida* complex is assumed to follow the same architecture but has not been assembled or imaged.
3. **Kinetic parameters are orthologous estimates.** Km, kcat, and inhibition constants (histidine Ki, AMP Ki) for the *P. putida* enzyme are unknown; the cited values are from *L. lactis*.
4. **Dispersed genome context.** *hisG* (PP_0965) and *hisZ* (PP_4890) are at distant loci, so their co-regulation and expression coordination in *P. putida* are not directly established.
5. **Localization is sequence-inferred.** Cytoplasmic localization rests on curated annotation plus absence of signal/TM features, not on experimental fractionation or imaging in *P. putida*.

---

## Proposed Follow-up Experiments / Actions

1. **Reconstitute the *P. putida* ATP-PRT in vitro.** Co-express PP_0965 (HisG_S) and PP_4890 (HisZ), purify, and confirm hetero-octamer formation by SEC-MALS or native mass spectrometry (target ~220 kDa, 4:4 stoichiometry).
2. **Direct kinetic characterization.** Measure Km(ATP), Km(PRPP), and kcat for the assembled complex vs isolated HisG_S to confirm HisZ-dependent activation; determine histidine and AMP inhibition constants (Ki) and modality.
3. **Structural determination.** Solve a cryo-EM or crystal structure of the *P. putida* holoenzyme with PRPP and with histidine bound, to confirm the motif-2-loop activation mechanism and the interfacial histidine sites predicted from *T. maritima*/*L. lactis*.
4. **Genetic validation in KT2440.** Construct clean *hisZ* (PP_4890) and *hisG* (PP_0965) deletions and test for histidine auxotrophy; complement with wild-type and motif-2-loop mutants to confirm the activation mechanism in vivo.
5. **Regulatory analysis.** Map the promoters of the dispersed *his* genes and test whether histidine availability modulates their expression, complementing the post-translational feedback inhibition operating at the protein level.
6. **Confirm cytoplasmic localization experimentally** via subcellular fractionation or a fluorescent-fusion reporter in *P. putida*.

---

## References

- Sissler M, et al. *An aminoacyl-tRNA synthetase paralog with a catalytic role in histidine biosynthesis.* PNAS 1999. [PMID: 10430882](https://pubmed.ncbi.nlm.nih.gov/10430882/)
- Vega MC, et al. *Regulation of the hetero-octameric ATP phosphoribosyl transferase complex from Thermotoga maritima by a tRNA synthetase-like subunit.* 2005. [PMID: 15660995](https://pubmed.ncbi.nlm.nih.gov/15660995/)
- Champagne KS, Sissler M, Larrabee Y, Doublié S, Francklyn CS. *Activation of the hetero-octameric ATP phosphoribosyl transferase through subunit interface rearrangement by a tRNA synthetase paralog.* 2005. [PMID: 16051603](https://pubmed.ncbi.nlm.nih.gov/16051603/)
- Champagne KS, Piscitelli E, Francklyn CS. *Substrate recognition by the hetero-octameric ATP phosphoribosyltransferase from Lactococcus lactis.* Biochemistry 2006. [PMID: 17154531](https://pubmed.ncbi.nlm.nih.gov/17154531/)
- Fisher G, et al. *Allosteric Activation Shifts the Rate-Limiting Step in a Short-Form ATP Phosphoribosyltransferase.* 2018. [PMID: 29940105](https://pubmed.ncbi.nlm.nih.gov/29940105/)
- Thomson CM, Alphey MS, Fisher G, da Silva RG. *Mapping the Structural Path for Allosteric Inhibition of a Short-Form ATP Phosphoribosyltransferase by Histidine.* 2019. [PMID: 31251578](https://pubmed.ncbi.nlm.nih.gov/31251578/)
- Read BJ, et al. *Allosteric Inhibition of [short-form ATP phosphoribosyltransferase].* 2022. [PMID: 34928596](https://pubmed.ncbi.nlm.nih.gov/34928596/)
- *Crystal Structure, Steady-State, and Pre-Steady-State Kinetics of [the first step of histidine biosynthesis].* [PMID: 38150593](https://pubmed.ncbi.nlm.nih.gov/38150593/)
- UniProt Q88DD7 (HAMAP MF_00125); InterPro IPR004516/IPR004517/IPR041715/IPR045864; Pfam PF13393.


## Artifacts

- [OpenScientist final report](hisZ-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](hisZ-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10430882
2. PMID:15660995
3. PMID:16051603
4. PMID:17154531
5. PMID:29940105
6. PMID:31251578
7. PMID:34928596
8. PMID:38150593