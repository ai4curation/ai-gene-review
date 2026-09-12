---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-26T20:21:52.212306'
end_time: '2026-07-26T22:00:25.116972'
duration_seconds: 5912.9
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: hutU
  gene_symbol: hutU
  uniprot_accession: Q88CZ6
  protein_description: 'RecName: Full=Urocanate hydratase {ECO:0000255|HAMAP-Rule:MF_00577};
    Short=Urocanase {ECO:0000255|HAMAP-Rule:MF_00577}; EC=4.2.1.49 {ECO:0000255|HAMAP-Rule:MF_00577};
    AltName: Full=Imidazolonepropionate hydrolase {ECO:0000255|HAMAP-Rule:MF_00577};'
  gene_info: Name=hutU {ECO:0000255|HAMAP-Rule:MF_00577}; OrderedLocusNames=PP_5033;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the urocanase family. {ECO:0000255|HAMAP-
  protein_domains: Urocanase. (IPR055351); Urocanase-like. (IPR023637); Urocanase_C.
    (IPR035401); Urocanase_central_sf. (IPR038364); Urocanase_CS. (IPR023636)
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
citation_count: 16
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: hutU-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: hutU-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88CZ6
- **Protein Description:** RecName: Full=Urocanate hydratase {ECO:0000255|HAMAP-Rule:MF_00577}; Short=Urocanase {ECO:0000255|HAMAP-Rule:MF_00577}; EC=4.2.1.49 {ECO:0000255|HAMAP-Rule:MF_00577}; AltName: Full=Imidazolonepropionate hydrolase {ECO:0000255|HAMAP-Rule:MF_00577};
- **Gene Information:** Name=hutU {ECO:0000255|HAMAP-Rule:MF_00577}; OrderedLocusNames=PP_5033;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the urocanase family. {ECO:0000255|HAMAP-
- **Key Domains:** Urocanase. (IPR055351); Urocanase-like. (IPR023637); Urocanase_C. (IPR035401); Urocanase_central_sf. (IPR038364); Urocanase_CS. (IPR023636)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "hutU" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'hutU' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **hutU** (gene ID: hutU, UniProt: Q88CZ6) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *hutU* (Q88CZ6, PP_5033): Urocanase of *Pseudomonas putida* KT2440

## Summary

The gene **hutU** (UniProt **Q88CZ6**; ordered locus **PP_5033**) of *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) encodes **urocanase** (urocanate hydratase; systematic name 4-imidazolone-5-propanoate hydro-lyase; **EC 4.2.1.49**). This enzyme catalyzes the **second step of the histidine utilization (hut) pathway**, the hydration of *trans*-urocanate to 4(5)-imidazolone-5(4)-propionate. The gene symbol, protein family (urocanase family), and domain architecture (Urocanase/Urocanase-like/Urocanase_C domains, IPR023637/IPR035401 etc.) are fully consistent with the UniProt annotation, and the identification is supported by direct experimental characterization of the *P. putida* urocanase — including cloning of the *hutU* gene, high-resolution crystallography, and detailed enzymological mechanism studies. **This is a well-characterized enzyme, and the gene identity is unambiguous.**

Mechanistically, urocanase is remarkable among lyases in that it uses a **tightly (but non-covalently) bound NAD⁺** as an **electrophilic, non-redox prosthetic group** rather than as a hydride-accepting redox cofactor. The nicotinamide ring of NAD⁺ forms a transient covalent C–C bond to the C5′ position of the substrate's imidazole ring, activating the conjugated double-bond system for the stereospecific addition of water. This unusual chemistry was established through ¹³C-NMR of specifically labelled NAD⁺, deuterium isotope-effect studies, and mutational analysis identifying a single essential catalytic cysteine. The enzyme is a **cytoplasmic, soluble homodimer** of 2 × 557 residues; its 1.14 Å crystal structure (from *P. putida*) reveals an NAD-binding Rossmann domain inserted into a larger core domain that forms the dimer interface and sequesters the substrate and cofactor in a closed cavity.

Physiologically, urocanase enables *P. putida* KT2440 to use **L-histidine as a carbon, nitrogen, and energy source**. Histidine is imported by the transporter **HutT** and degraded intracellularly: histidase (HutH) converts histidine to urocanate, urocanase (HutU) hydrates urocanate to imidazolone-propionate, and downstream enzymes (HutI, then HutG/HutF) channel the product toward **L-glutamate**. The *hutU* gene lies in the urocanate-inducible **hutUHIG operon**, controlled by the local repressor **HutC** (with urocanate as the physiological inducer) and integrated into global carbon/nitrogen regulation via the **CbrAB/σ⁵⁴** and **NtrBC/σ⁷⁰** systems. Notably, urocanate — the substrate consumed by urocanase — doubles as a **signaling molecule** through which bacteria recognize eukaryotic hosts, linking this central metabolic enzyme to environmental sensing and, in pathogens, virulence.

---

## Gene / Protein Identity Verification

| Field | Value |
|---|---|
| UniProt accession | Q88CZ6 |
| Gene symbol | *hutU* |
| Ordered locus | PP_5033 |
| Protein | Urocanate hydratase (urocanase) |
| EC number | 4.2.1.49 |
| Alt. name | Imidazolonepropionate hydrolase |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) |
| Family | Urocanase family |
| Length / MW | 557 residues / ≈ 60.7 kDa |
| Cofactor | 1 NAD⁺ per subunit (tightly, non-covalently bound) |
| Localization | Cytoplasm |
| Pathway | L-histidine degradation to L-glutamate, step 2/3 |

**Verification result:** All literature located for *hutU* refers to bacterial urocanase in the histidine utilization pathway; no conflicting gene of the same symbol was found. The protein family and domain assignments align across all sources, and the *P. putida* enzyme has been directly characterized. The gene identity is secure.

---

## Key Findings

### Finding 1 — *hutU* encodes urocanase, the second enzyme of histidine degradation

The *hutU* gene of *Pseudomonas putida* was directly demonstrated to encode a catalytically active urocanase. Lenz & Rétey (1993) isolated the *hutU* gene from a genomic library of *P. putida* nicII, subcloned it into a T7 expression vector, and expressed it in *E. coli*, where the recombinant enzyme accumulated to roughly **30% of soluble cellular protein** and was catalytically active ([PMID: 7901006](https://pubmed.ncbi.nlm.nih.gov/7901006/)). The reaction catalyzed — hydration of urocanate to 4(5)-imidazolone-5(4)-propionate — and the enzyme identity (EC 4.2.1.49, NAD-dependent urocanate hydro-lyase) had earlier been established for the *P. putida* enzyme by Egan, Matherly & Phillips (1981) ([PMID: 6110440](https://pubmed.ncbi.nlm.nih.gov/6110440/)).

The target protein Q88CZ6 is the KT2440 ortholog of this characterized enzyme. It belongs to the same species (*P. putida*), carries the same gene symbol, and occupies the analogous position in the *hut* pathway. Its curated reaction — *trans*-urocanate + H₂O → 4-imidazolone-5-propanoate (Rhea:13101; EC 4.2.1.49) — matches the experimentally verified chemistry exactly.

**Reaction catalyzed:**

```
                    urocanase (HutU, EC 4.2.1.49)
   trans-urocanate  +  H2O  ───────────────────────►  4(5)-imidazolone-5(4)-propionate
   (imidazol-4-yl-acrylate)      NAD+ (bound cofactor)
```

### Finding 2 — Urocanase uses a tightly bound NAD⁺ as a non-redox electrophilic prosthetic group

Urocanase is mechanistically distinctive: although it requires **NAD⁺**, it does not use it for a net oxidation–reduction. Egan, Matherly & Phillips (1981) used deuterium isotope effects and labeling patterns to show that the reaction proceeds by **water addition across the conjugated double-bond system of urocanate**, "rather than an internal oxidation–reduction process, yet NAD⁺ is required" ([PMID: 6110440](https://pubmed.ncbi.nlm.nih.gov/6110440/)).

The role of NAD⁺ was clarified by ¹³C-NMR work of Klepp, Rétey and colleagues (1990), who grew the enzyme on [4-¹³C]nicotinate to specifically label the prosthetic NAD⁺. This revealed a **covalent C–C bond between C4 of the nicotinamide ring and C5′ of the imidazole ring** of the substrate/inhibitor adduct — direct evidence for the electrophilic addition of enzyme-bound NAD⁺ to the substrate that activates it toward hydration ([PMID: 1976515](https://pubmed.ncbi.nlm.nih.gov/1976515/)). A complementary inhibition study with 2-methylurocanate proposed the same crucial first step: electrophilic addition of enzyme-bound NAD to the 2-position of the imidazole nucleus ([PMID: 2885981](https://pubmed.ncbi.nlm.nih.gov/2885981/)).

Mutational analysis pinpointed the catalytic machinery: of the enzyme's cysteines, **only Cys410 was essential for catalysis**, and NAD is **not covalently bound** to the protein ([PMID: 7901006](https://pubmed.ncbi.nlm.nih.gov/7901006/)). Together these results define urocanase as an enzyme in which NAD⁺ functions as a tightly bound electrophilic catalyst — a rare, non-canonical role for this classic redox cofactor.

### Finding 3 — Urocanase is a cytoplasmic homodimer with an NAD-binding domain inserted into a novel core domain

The three-dimensional architecture was solved to atomic resolution. Kessler, Rétey & Schulz (2004) determined the **1.14 Å crystal structure** of *P. putida* urocanase, revealing a **symmetric homodimer of 2 × 557 amino acid residues with tightly bound NAD⁺ cofactors** ([PMID: 15313616](https://pubmed.ncbi.nlm.nih.gov/15313616/)). Each subunit comprises a **typical NAD-binding (Rossmann-type) domain inserted into a larger core domain** that forms the dimer interface and binds urocanate in a surface depression.

Critically for the mechanism, the structure showed that **substrate, nicotinamide, and five water molecules are completely sequestered in a closed cavity** ([PMID: 15313616](https://pubmed.ncbi.nlm.nih.gov/15313616/)). This supports the water-addition mechanism (the five ordered waters are positioned for the hydration chemistry) and implies that the NAD-binding domain acts as a mobile lid that must lift to admit substrate and release product. The soluble, cytoplasmic nature of the enzyme is consistent with its role in intracellular amino-acid catabolism.

### Finding 4 — *hutU* is part of the urocanate-induced *hutUHIG* operon under global carbon/nitrogen control

In *P. putida*, the *hut* genes are contiguous, with the gene order determined as **hutG–hutI–hutH–hutU–hutC–hutF**, organized into three transcriptional units; *hutU* (with *hutHIG*) forms an operon that possesses its own operator–promoter and is **induced by urocanate** via the HutC repressor (Hu & Phillips, 1988) ([PMID: 2842309](https://pubmed.ncbi.nlm.nih.gov/2842309/)). That same study showed that expression of *hutF* and *hutU* (urocanase) is induced by urocanate.

Regulation is layered onto global carbon/nitrogen homeostasis. Work in the closely related *P. fluorescens* SBW25 (Zhang & Rainey, 2007/2008) established that the *hutU* operon is transcribed from a **σ⁵⁴ promoter requiring CbrB** when histidine is the sole carbon source, and from a **σ⁷⁰ promoter requiring NtrC** (or CbrB) when histidine is the sole nitrogen source ([PMID: 18202367](https://pubmed.ncbi.nlm.nih.gov/18202367/)). The three *hut* operons are **negatively regulated by the HutC repressor with urocanate as the physiological inducer** ([PMID: 17717196](https://pubmed.ncbi.nlm.nih.gov/17717196/)). This dual regulatory logic ensures urocanase is produced only when its substrate is available and when histidine catabolism is nutritionally advantageous.

### Finding 5 — Q88CZ6 (KT2440) sequence directly matches the characterized *P. putida* urocanase, with conserved catalytic residues

Sequence-level analysis confirms that the target protein is the enzyme described above. The UniProt Q88CZ6 sequence is **exactly 557 residues** (MW ≈ 60.7 kDa), identical in length to the crystallized *P. putida* urocanase subunit (2 × 557 residues) ([PMID: 15313616](https://pubmed.ncbi.nlm.nih.gov/15313616/)). It contains 7 cysteines (positions 64, 192, 198, 355, 411, 508, 544); the **essential catalytic cysteine** identified in the biochemically characterized nicII enzyme (Cys410 in that numbering) ([PMID: 7901006](https://pubmed.ncbi.nlm.nih.gov/7901006/)) is **conserved at position 411** of Q88CZ6.

UniProt's curated annotations for Q88CZ6 are internally consistent with all experimental evidence: reaction = 4-imidazolone-5-propanoate ⇌ *trans*-urocanate + H₂O (Rhea:13101, EC 4.2.1.49); cofactor = "Binds 1 NAD⁺ per subunit"; subcellular location = **Cytoplasm**; and pathway = "L-histidine degradation into L-glutamate … step 2/3." The high similarity of urocanase across bacterial species (including psychrotrophic and mesophilic *Pseudomonas*) further supports transfer of the detailed *P. putida* characterization to the KT2440 ortholog ([PMID: 11772602](https://pubmed.ncbi.nlm.nih.gov/11772602/)).

### Finding 6 — Histidine is imported by HutT and degraded intracellularly; urocanate is both substrate and host-recognition signal

In *P. putida* KT2440, the **APC-family high-affinity histidine:H⁺ symporter HutT** (encoded within the *hut* operon) is the major histidine uptake system; deletion of *hutT* **severely impairs growth on histidine**, indicating that histidine is imported before being catabolized intracellularly ([PMID: 34245008](https://pubmed.ncbi.nlm.nih.gov/34245008/)). Once inside, histidase produces urocanate, which urocanase then hydrates — all in the cytoplasm.

Beyond its metabolic role, **urocanate is a signaling molecule**. Zhang, Ritchie & Rainey (2014) showed that urocanate — an intermediate of the histidine degradation pathway — **accumulates in host tissues such as skin and acts as a molecule that promotes bacterial infection through interaction with the bacterial regulatory protein HutC** ([PMID: 24305948](https://pubmed.ncbi.nlm.nih.gov/24305948/)). Because urocanase directly consumes urocanate, it sits at the junction between metabolism and this host-recognition/virulence signaling axis: the enzyme's activity modulates the intracellular pool of the very metabolite that serves as the HutC inducer and, in pathogens, a host-derived infection cue.

---

## Mechanistic Model / Interpretation

### Position in the histidine utilization pathway

Urocanase catalyzes step 2 of a conserved multi-step route that converts L-histidine to L-glutamate, feeding carbon and nitrogen into central metabolism:

```
  L-histidine
     │  HutH (histidase / histidine ammonia-lyase)   — releases NH3
     ▼
  trans-urocanate  ◄──────────── physiological inducer of HutC; host-recognition signal
     │  HutU (UROCANASE, EC 4.2.1.49)   ← Q88CZ6 / PP_5033   [+ H2O; bound NAD+]
     ▼
  4-imidazolone-5-propionate
     │  HutI (imidazolonepropionase)   — + H2O
     ▼
  N-formimino-L-glutamate
     │  HutG / HutF (branch-dependent)
     ▼
  L-glutamate  ──►  central C/N metabolism
```

All of these reactions occur in the **cytoplasm**, after histidine is transported into the cell by **HutT**. UniProt places urocanase at "step 2/3" of "L-histidine degradation into L-glutamate," matching this scheme.

### Catalytic mechanism

The core innovation of urocanase is the use of NAD⁺ as an **electrophile, not an oxidant**:

| Feature | Evidence | Reference |
|---|---|---|
| NAD⁺ required, but no net redox | Deuterium isotope effects; water addition, not oxidation–reduction | [PMID: 6110440](https://pubmed.ncbi.nlm.nih.gov/6110440/) |
| Covalent C4(nicotinamide)–C5′(imidazole) adduct | ¹³C-NMR of [4-¹³C]nicotinate-labelled NAD⁺ | [PMID: 1976515](https://pubmed.ncbi.nlm.nih.gov/1976515/) |
| Electrophilic addition to imidazole is first step | Inhibition by 2-methylurocanate | [PMID: 2885981](https://pubmed.ncbi.nlm.nih.gov/2885981/) |
| Single essential Cys; NAD non-covalently bound | Site-directed mutagenesis (Cys410 essential) | [PMID: 7901006](https://pubmed.ncbi.nlm.nih.gov/7901006/) |
| Substrate + nicotinamide + 5 waters sequestered | 1.14 Å crystal structure | [PMID: 15313616](https://pubmed.ncbi.nlm.nih.gov/15313616/) |

In outline: the nicotinamide ring adds electrophilically to the imidazole of urocanate, forming a covalent adduct that dearomatizes/activates the conjugated acrylate–imidazole system. This allows stereospecific addition of water (delivered by the ordered active-site waters) across the double bond, after which the adduct collapses to release 4-imidazolone-5-propionate and regenerate NAD⁺. Cys410/411 participates in catalysis, and the whole cycle takes place in a closed cavity formed as the Rossmann NAD-domain lid seals over the core domain.

### Structural summary

```
  Urocanase subunit (557 aa, ~60.7 kDa)
  ┌─────────────────────────────────────────────┐
  │  CORE domain (dimer interface, urocanate site)│
  │        ┌───────────────────────┐             │
  │        │  NAD-binding domain    │  ← Rossmann fold, "lid"
  │        │  (inserted into core)  │     tightly binds 1 NAD+/subunit
  │        └───────────────────────┘             │
  └─────────────────────────────────────────────┘
        × 2  →  symmetric homodimer, cytoplasmic, soluble
```

### Regulatory and ecological integration

Urocanase expression is gated by substrate availability and nutritional context. The *hutUHIG* operon is de-repressed by HutC when **urocanate** accumulates, and its promoters are activated through **CbrAB/σ⁵⁴** (carbon-source mode) or **NtrBC/σ⁷⁰** (nitrogen-source mode). This makes urocanase production responsive to whether histidine is being used primarily as a carbon or nitrogen source. The dual identity of urocanate — catabolic intermediate *and* host-recognition/virulence signal via HutC — means that flux through urocanase influences not just energy metabolism but also the intracellular signaling pool that couples histidine catabolism to environmental/host sensing.

---

## Evidence Base

| PMID | Study (paraphrased) | How it supports the annotation |
|---|---|---|
| [7901006](https://pubmed.ncbi.nlm.nih.gov/7901006/) | *Cloning, expression and mutational analysis of hutU from P. putida* | Directly proves *hutU* encodes active urocanase; identifies essential Cys410; NAD non-covalent |
| [6110440](https://pubmed.ncbi.nlm.nih.gov/6110440/) | *Mechanism of urocanase by deuterium isotope effects and labeling* | Establishes EC 4.2.1.49 identity and water-addition (non-redox) mechanism in *P. putida* |
| [1976515](https://pubmed.ncbi.nlm.nih.gov/1976515/) | *Specific ¹³C-labelling of prosthetic NAD⁺; revised adduct structure* | Demonstrates covalent NAD–substrate C–C adduct central to electrophilic mechanism |
| [2885981](https://pubmed.ncbi.nlm.nih.gov/2885981/) | *Inhibition by 2-methylurocanate; proposed mechanism* | Supports electrophilic addition of NAD to imidazole as the first catalytic step |
| [15313616](https://pubmed.ncbi.nlm.nih.gov/15313616/) | *Structure and action of urocanase (1.14 Å)* | Defines homodimer (2×557), domain organization, sequestered active site with 5 waters |
| [2842309](https://pubmed.ncbi.nlm.nih.gov/2842309/) | *Organization and regulation of hut genes in P. putida* | Establishes *hutG-hutI-hutH-hutU-hutC-hutF* order and urocanate induction of *hutU* |
| [17717196](https://pubmed.ncbi.nlm.nih.gov/17717196/) | *Genetic analysis of hut in P. fluorescens SBW25* | HutC/urocanate negative regulation of the *hutU*-containing operon |
| [18202367](https://pubmed.ncbi.nlm.nih.gov/18202367/) | *Dual CbrAB/NtrBC regulation of hut* | σ⁵⁴/CbrB (carbon) vs σ⁷⁰/NtrC (nitrogen) control of the *hutU* operon |
| [34245008](https://pubmed.ncbi.nlm.nih.gov/34245008/) | *HutT is the major L-histidine transporter in KT2440* | Establishes histidine import route feeding intracellular urocanase |
| [24305948](https://pubmed.ncbi.nlm.nih.gov/24305948/) | *Urocanate as a host-recognition signal* | Shows urocanate (urocanase substrate) is a HutC-acting signaling molecule |
| [11772602](https://pubmed.ncbi.nlm.nih.gov/11772602/) | *Cold-inducible hutU from P. syringae* | Confirms high urocanase sequence conservation and Rossmann/NAD motif across *Pseudomonas* |

Supporting/contextual literature includes the demonstration that the *hut* operon is upregulated at low temperature in antarctic *Pseudomonas* ([PMID: 9561727](https://pubmed.ncbi.nlm.nih.gov/9561727/)), the branched *hut* pathway topology and horizontal acquisition of *hutE* in *P. aeruginosa* PAO1 ([PMID: 22225844](https://pubmed.ncbi.nlm.nih.gov/22225844/)), CbrA's dual role in histidine uptake and signaling ([PMID: 26148710](https://pubmed.ncbi.nlm.nih.gov/26148710/)), HutC governance of NtrBC carbon/nitrogen homeostasis ([PMID: 33675669](https://pubmed.ncbi.nlm.nih.gov/33675669/)), and the identification of urocanase homology within the *Bacillus subtilis hut* operon ([PMID: 7704263](https://pubmed.ncbi.nlm.nih.gov/7704263/)).

**Consistency check:** No literature was found describing a *different* gene with the symbol *hutU*. In every reference, *hutU* refers to bacterial urocanase in the histidine utilization pathway, and the protein family/domain assignments (urocanase family; Rossmann NAD-binding fold; conserved active-site cysteine) align across all sources. The gene identity is therefore secure.

---

## Limitations and Knowledge Gaps

1. **Direct characterization is of *P. putida* strains other than KT2440.** The definitive enzymology, mutagenesis, and 1.14 Å structure were performed on *P. putida* (nicII / the strain used for crystallography), not on KT2440 itself. The inference to Q88CZ6 rests on identical species, identical protein length (557 aa), conserved catalytic cysteine (position 411), and shared gene symbol/operon context — very strong, but formally by orthology rather than direct KT2440 assay.

2. **Catalytic-residue numbering.** The "Cys410" essential cysteine of the nicII enzyme corresponds to position 411 in Q88CZ6; a full residue-by-residue alignment confirming all active-site residues (beyond the catalytic Cys) was not exhaustively documented here.

3. **Kinetic parameters for the KT2440 enzyme** (kcat, Km for urocanate, substrate-specificity profile against related imidazole-acrylates) are not reported in the reviewed literature for Q88CZ6 specifically.

4. **Substrate specificity breadth.** Urocanase is understood to be highly specific for *trans*-urocanate, but quantitative specificity data (e.g., activity toward analogues beyond the 2-methylurocanate inhibitor) were not systematically compiled.

5. **In-vivo flux and physiological knockout data in KT2440.** While *hutT* deletion phenotypes are documented, a clean *hutU*-specific deletion phenotype in KT2440 (growth on histidine, urocanate accumulation) was not directly cited.

6. **Localization** is annotated as cytoplasmic (UniProt) and inferred from the soluble homodimeric structure; no experimental fractionation study specific to KT2440 was reviewed.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant KT2440 urocanase characterization.** Express Q88CZ6 (PP_5033) in *E. coli*, purify, and measure steady-state kinetics (kcat, Km for *trans*-urocanate), NAD⁺ stoichiometry, and thermal stability to confirm transfer of the nicII/crystallography data to the exact target sequence.

2. **Active-site alignment and mutagenesis.** Perform a structure-guided alignment of Q88CZ6 against the 1.14 Å structure ([PMID: 15313616](https://pubmed.ncbi.nlm.nih.gov/15313616/)); verify conservation of all substrate- and NAD-contacting residues, and validate Cys411 as the catalytic cysteine by C411A/S mutagenesis.

3. **KT2440 *hutU* deletion phenotype.** Construct a markerless ΔhutU mutant; assay growth on histidine as sole C/N source, and measure intracellular urocanate accumulation (expected to rise) and its effect on HutC-dependent gene expression.

4. **Metabolomic confirmation of product.** Use LC-MS/NMR to confirm 4-imidazolone-5-propionate as the *in vivo* product and to trace flux toward L-glutamate through HutI/HutG/HutF.

5. **Regulatory dissection in KT2440.** Test σ⁵⁴/CbrB vs σ⁷⁰/NtrC promoter usage of the *hutU* operon directly in KT2440 under carbon- vs nitrogen-limited histidine growth, mirroring the SBW25 studies.

6. **Signaling link.** Quantify how urocanase activity modulates the intracellular urocanate pool and downstream HutC-controlled/virulence-associated gene expression, to test the metabolism–signaling coupling suggested by [PMID: 24305948](https://pubmed.ncbi.nlm.nih.gov/24305948/).

---

## Conclusion

*hutU* (Q88CZ6, PP_5033) of *Pseudomonas putida* KT2440 encodes **urocanase (EC 4.2.1.49)**, the second enzyme of the histidine utilization pathway, which hydrates *trans*-urocanate to 4-imidazolone-5-propionate using a tightly bound, non-covalent NAD⁺ acting as an electrophilic (non-redox) catalyst. It is a soluble, cytoplasmic homodimer (2 × 557 residues) with a fully solved atomic-resolution structure, and it functions to let the bacterium exploit histidine (imported by HutT) as a carbon, nitrogen, and energy source by routing it to L-glutamate. Its expression is urocanate-induced through the HutC repressor and integrated into global C/N regulation via CbrAB/σ⁵⁴ and NtrBC/σ⁷⁰. The gene identity is unambiguous and strongly supported by direct experimental evidence in *P. putida*.


## Artifacts

- [OpenScientist final report](hutU-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](hutU-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:7901006
2. PMID:6110440
3. PMID:1976515
4. PMID:2885981
5. PMID:15313616
6. PMID:2842309
7. PMID:18202367
8. PMID:17717196
9. PMID:11772602
10. PMID:34245008
11. PMID:24305948
12. PMID:9561727
13. PMID:22225844
14. PMID:26148710
15. PMID:33675669
16. PMID:7704263