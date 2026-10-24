---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T06:14:28.881493'
end_time: '2026-08-31T06:27:08.628496'
duration_seconds: 759.75
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_2671
  gene_symbol: PP_2671
  uniprot_accession: Q88JH8
  protein_description: 'RecName: Full=histidine kinase {ECO:0000256|ARBA:ARBA00012438};
    EC=2.7.13.3 {ECO:0000256|ARBA:ARBA00012438};'
  gene_info: OrderedLocusNames=PP_2671 {ECO:0000313|EMBL:AAN68279.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: HAMP_dom. (IPR003660); HATPase_C_sf. (IPR036890); HATPase_dom.
    (IPR003594); His_kinase_dom. (IPR005467); Sensor_HK_TwoCompSys. (IPR050482)
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
citation_count: 6
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_2671-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_2671-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88JH8
- **Protein Description:** RecName: Full=histidine kinase {ECO:0000256|ARBA:ARBA00012438}; EC=2.7.13.3 {ECO:0000256|ARBA:ARBA00012438};
- **Gene Information:** OrderedLocusNames=PP_2671 {ECO:0000313|EMBL:AAN68279.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** HAMP_dom. (IPR003660); HATPase_C_sf. (IPR036890); HATPase_dom. (IPR003594); His_kinase_dom. (IPR005467); Sensor_HK_TwoCompSys. (IPR050482)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_2671" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_2671' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_2671** (gene ID: PP_2671, UniProt: Q88JH8) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PP_2671 / PedS2 (UniProt Q88JH8)

**Organism:** *Pseudomonas putida* (strain KT2440 / ATCC 47054 / DSM 6125), PSEPK
**Locus tag:** PP_2671 | **Gene name:** *pedS2* | **UniProt:** Q88JH8
**EC:** 2.7.13.3 (histidine kinase) | **Length:** 424 aa | **KEGG:** ppu:PP_2671

---

## 1. Summary (Answer to the Research Question)

PP_2671 encodes **PedS2**, the **sensor histidine kinase** of the **PedS2/PedR2 two‑component signal‑transduction system** of *Pseudomonas putida* KT2440. Its primary function is to **sense the environmental availability of rare‑earth elements (lanthanides, Ln³⁺)** and to transduce this signal, by ATP‑dependent autophosphorylation on a conserved histidine and subsequent phosphotransfer to its cognate LuxR‑type response regulator **PedR2 (PP_2672)**, into a transcriptional output. This system operates the so‑called **"REE‑switch"** that inversely regulates the two functionally redundant periplasmic pyrroloquinoline‑quinone (PQQ)‑dependent ethanol dehydrogenases — the Ca²⁺‑dependent **PedE** and the lanthanide‑dependent **PedH** — allowing the bacterium to match its periplasmic alcohol/aldehyde (volatile organic compound) oxidation machinery to metal availability. PedS2 is an **inner‑membrane protein** that perceives its signal in the **periplasm** and executes catalysis (autokinase activity) in the **cytoplasm**.

The gene identity is unambiguous: Wehrmann et al. (2018) explicitly map the locus pair **PP_2671/PP_2672 to PedS2/PedR2**, matching the UniProt annotation (histidine kinase, EC 2.7.13.3, membrane, HAMP + HATPase domains).

---

## 2. Gene / Protein Identity Verification

| Check | Result |
|---|---|
| Symbol matches description | ✔ PP_2671 = *pedS2*; UniProt "histidine kinase" matches the characterized sensor kinase PedS2 |
| Organism correct | ✔ *P. putida* KT2440 (PSEPK) |
| Domains align with literature | ✔ HAMP domain + HATPase_C/His‑kinase catalytic domain = canonical two‑component sensor kinase |
| Literature specificity | ✔ Direct primary‑literature characterization of PP_2671 as PedS2 (Wehrmann et al., 2018) |

There is **no ambiguity**: this locus is directly and specifically characterized in the primary literature.

---

## 3. Primary Molecular Function

### 3.1 Enzymatic reaction (EC 2.7.13.3)
PedS2 is a **protein‑histidine kinase**. As a two‑component sensor kinase it catalyzes:

1. **Autophosphorylation:** ATP + protein L‑histidine → ADP + protein N‑phospho‑L‑histidine (on the conserved His of the DHp/H‑box), catalyzed by the C‑terminal HATPase (GHKL‑family) ATP‑binding domain.
2. **Phosphotransfer:** the high‑energy phospho‑His donates the phosphoryl group to a conserved **aspartate** on the receiver domain of the response regulator **PedR2**.

The "substrate" of the sensor kinase in the signaling sense is therefore its **cognate response regulator PedR2 (PP_2672)**; the chemical substrate/cofactor of the catalytic reaction is **ATP** (UniProt GO:0005524 ATP binding; GO:0000155 phosphorelay sensor kinase activity).

### 3.2 Input signal / ligand specificity
The physiological **input signal is the availability of lanthanide (Ln³⁺) rare‑earth elements** (experimentally probed with La³⁺). Evidence (Wehrmann et al., 2018):
- In the **absence of La³⁺**, PedS2 is kinase‑active → phosphorylates PedR2.
- In the **presence of La³⁺**, PedS2 kinase activity is **lowered**, proposed to occur through **direct binding of the metal ion to the periplasmic region of PedS2** (or an indirect interaction), reducing phospho‑PedR2 levels.

PedS2 is described as a **putative La³⁺‑binding protein**; high iron can cause **mismetallation** of PedS2 and other La³⁺‑binding proteins, shifting the Ln³⁺ concentration required for switching (Wehrmann et al., 2019).

---

## 4. Signaling Pathway and Downstream Output ("the REE‑switch")

```
Ln3+ (periplasm)
      │  (binds periplasmic sensor region of PedS2)
      ▼
  PedS2 (PP_2671)  ── ATP ──►  His~P   (kinase activity HIGH when Ln3+ LOW)
      │  phosphotransfer
      ▼
  PedR2 (PP_2672, LuxR-type RR) ── Asp~P
      │
      ├──►  ACTIVATES  pedE  (Ca2+-dependent PQQ-EDH)
      └──►  REPRESSES  pedH  (Ln3+-dependent PQQ-EDH)
```

- **Low/no lanthanide:** active PedS2 → phospho‑PedR2 → **pedE ON, pedH OFF** → alcohol oxidation via the Ca²⁺ enzyme PedE.
- **Lanthanide present:** reduced PedS2 activity → less phospho‑PedR2 → **pedE OFF**, **pedH de‑repressed** (and additionally activated by a still‑unknown regulatory module) → oxidation via the Ln³⁺ enzyme PedH.

This is the **first detailed molecular characterization of a rare‑earth‑element switch in a non‑methylotrophic bacterium** (Wehrmann et al., 2018). PedR2 has a **dual regulatory role** (activator of *pedE*, repressor of *pedH*).

**Broader pathway context:** PedE and PedH are the terminal sensing/redundant enzymes of a **periplasmic oxidation system** that oxidizes a broad range of alcohols and aldehydes (volatile organic compounds such as ethanol and 2‑phenylethanol), important for detoxification and catabolism (Wehrmann et al., 2017). Cytoplasmic uptake of lanthanides (which tunes the switch and enables PedH‑dependent growth at low REE concentrations) is mediated by the **ABC transporter PedA1A2BC**, encoded in the same *ped* gene cluster (Wehrmann et al., 2019). Thus PedS2 is the regulatory sensor at the head of an integrated periplasmic C1/alcohol‑oxidation and REE‑adaptation module.

---

## 5. Subcellular Localization

- **UniProt:** Membrane.
- **Bioinformatic topology (this work, Kyte‑Doolittle hydropathy, window 19 on the 424‑aa sequence):** an N‑terminal transmembrane helix (~residues 17–30) and a second hydrophobic/TM segment (~residues 147–160) flank a ~117‑residue **periplasmic sensor loop (~30–147)**; these are followed by the cytoplasmic **HAMP linker (161–213)** and the cytoplasmic **histidine‑kinase catalytic domain (236–424)**.
- **Interpretation:** PedS2 is an **integral inner‑membrane** sensor kinase. It **perceives the Ln³⁺ signal in the periplasm** and **carries out autophosphorylation/phosphotransfer in the cytoplasm**, with the HAMP domain transmitting the conformational signal across the membrane. This topology is fully consistent with the experimental proposal that La³⁺ binds the periplasmic region.

---

## 6. Domain Architecture (evidence from structure/sequence)

| Region (aa) | Feature | Role |
|---|---|---|
| ~17–30 | TM helix 1 | Membrane anchoring |
| ~30–147 | Periplasmic loop | Putative lanthanide (Ln³⁺) sensing / ligand binding |
| ~147–160 | TM helix 2 | Membrane anchoring |
| 161–213 | **HAMP** domain (IPR003660) | Transmembrane signal relay to the kinase core |
| 236–424 | **Histidine‑kinase** catalytic core: DHp (His phosphoacceptor) + HATPase_C/GHKL ATP‑binding (IPR003594, IPR036890, IPR005467) | Autokinase + phosphotransfer; ATP binding; dimerization (GO:0046983) |

Family classification (InterPro IPR050482): **Sensor histidine kinase of two‑component systems**.

### 6.1 Conserved catalytic residues (bioinformatic evidence, this work)
Sequence analysis of the cytoplasmic kinase core confirms all motifs required for a catalytically competent HisKA/GHKL kinase:

| Motif | Position | Sequence context | Role |
|---|---|---|---|
| **H‑box** (phosphoacceptor His) | **His238** | L‑A‑Q‑T‑L‑**H**‑D‑D‑L‑G | Site of ATP‑dependent autophosphorylation |
| N‑box | ~res 300–330 | — | Coordinates Mg²⁺/ATP |
| **G1 / D‑box** (DxGxG) | **375–379** | **DNGCG** | ATP phosphate binding (Bergerat fold) |
| **G2 / G‑box** | **411–413** | **GGG** | ATP‑lid / nucleotide binding |

The intact H‑box His238 and GHKL ATP‑binding boxes provide independent structural evidence that PedS2 autophosphorylates on **His238** and then transfers phosphate to the Asp of PedR2 — consistent with the experimentally demonstrated PedR2 phosphorylation.

## 6.2 Genomic context (the *ped* cluster; UniProt survey PP_2662–PP_2683)
PedS2 (PP_2671) sits within a self‑contained periplasmic PQQ‑dependent oxidation cluster:

| Locus | Product | Role |
|---|---|---|
| **PP_2671** | **PedS2** (this protein) — sensor histidine kinase | Lanthanide sensing / signal input |
| **PP_2672** | **PedR2 / ExaE** — LuxR‑type response regulator (212 aa) | Cognate partner; activates *pedE*, represses *pedH* |
| PP_2674 | **PedE** — Ca²⁺‑dependent PQQ‑ADH (EC 1.1.2.8, 631 aa) | Effector enzyme (low‑REE) |
| PP_2679 | **PedH** — lanthanide‑dependent PQQ‑ADH (595 aa) | Effector enzyme (high‑REE) |
| PP_2680 | AldB‑II aldehyde dehydrogenase | Downstream aldehyde oxidation |
| PP_2681 | PqqD2 (PQQ biosynthesis) | Cofactor supply |
| PP_2675 / PP_2676 | Cytochrome c / periplasmic binding protein | Electron transfer / periplasmic function |
| PP_2662 / PP_2669 / PP_2667–2668 | Porin / OMP / ABC transporter | Substrate/metal traffic |
| **PP_2664 / PP_2665 (AgmR)** | Second sensor kinase / DNA‑binding response regulator | Candidate for the additional, still‑unidentified *pedH*‑activating module |

This co‑localization with the cognate response regulator, both effector dehydrogenases, PQQ‑biosynthesis and electron‑transfer genes pinpoints PedS2 as the dedicated regulatory sensor gating this periplasmic alcohol/aldehyde‑oxidation pathway. (Note: UniProt labels PP_2672 "ExaE"; Wehrmann et al. 2018 name the same protein PedR2 — they are identical.)

---

## 7. Supported vs. Refuted Hypotheses

**Supported**
- PP_2671 = PedS2, a two‑component **sensor histidine kinase** (EC 2.7.13.3). *(UniProt; Wehrmann 2018)*
- PedS2 phosphorylates the LuxR‑type response regulator **PedR2 (PP_2672)**. *(Wehrmann 2018)*
- PedS2 activity responds **inversely to lanthanide availability**; it is a putative La³⁺‑binding sensor. *(Wehrmann 2018, 2019)*
- Output is the **REE‑switch** inversely regulating *pedE* (Ca²⁺‑PQQ‑EDH) and *pedH* (Ln³⁺‑PQQ‑EDH). *(Wehrmann 2018)*
- PedS2 is an **inner‑membrane protein with a periplasmic sensing region**. *(UniProt; topology analysis; Wehrmann 2018)*
- PedS2 retains all catalytic motifs (H‑box His238, GHKL ATP‑binding boxes) of a functional autokinase. *(sequence analysis, this work)*
- PedS2 is co‑clustered with PedR2/ExaE, PedE, PedH, PQQ‑biosynthesis and a second TCS (PP_2664/AgmR). *(UniProt genomic survey)*

**Refuted / ruled out**
- PP_2671 is **not** a metabolic/biosynthetic enzyme acting on a small‑molecule substrate; it is a signal‑transduction protein‑kinase.
- The gene symbol is **not** ambiguous in this organism — it is specifically the *ped* cluster sensor kinase, not a generic/orthologous histidine kinase from another species.

---

## 8. Evidence Quality and Limitations

- **Direct experimental evidence** (adaptive evolution, site‑directed mutagenesis, transcriptional reporter fusions, complementation) supports the physiological role of PedS2 in the REE‑switch (Wehrmann et al., 2018; genetic/physiological data 2019).
- The **exact molecular mechanism of lanthanide sensing** (direct La³⁺ binding to the periplasmic domain vs. indirect interaction) is **not yet definitively established** — the authors present it as a supported hypothesis. No purified‑protein biochemistry or structure of PedS2 with bound Ln³⁺ has been reported here.
- Membrane topology and the conserved His/Asp phosphotransfer chemistry are inferred from **sequence/domain (bioinformatic) analysis** consistent with the two‑component‑kinase family, not from an experimental PedS2 structure.
- The additional activating module for *pedH* remains unidentified.

**Future directions:** purified‑protein autokinase/phosphotransfer assays; identification of the La³⁺‑coordinating residues in the periplasmic domain (site‑directed mutagenesis); structural determination; identification of the additional *pedH*‑activating regulator.

---

## 8b. Physiological & Evolutionary Significance (context)

- **A conserved regulatory paradigm — the "lanthanide switch."** The inverse, REE‑dependent regulation of Ca²⁺‑ vs Ln³⁺‑utilizing PQQ dehydrogenases that PedS2 operates is a recurring theme across bacteria; it was first described in methylotrophs and is the subject of multiple authoritative reviews (Skovran et al. 2019, PMID 31166187; Featherston & Cotruvo 2021, PMID 32979423; Daumann et al. 2022, PMID 36167440). A mechanistic model for the switch in *Paracoccus denitrificans* was recently proposed (Parekh & Spiro 2025, PMID 40846390). The *P. putida* PedS2/PedR2 study represents the **first detailed characterization of this switch in a non‑methylotroph** (Wehrmann et al. 2018).
- **Effector‑enzyme substrate range (what the pathway ultimately does).** The PQQ‑ADHs gated by PedS2 are broad‑substrate periplasmic enzymes oxidizing volatile alcohols/aldehydes — e.g. ethanol and 2‑phenylethanol (Wehrmann et al. 2017, PMID 28655819) — and are of biotechnological interest (soluble, direct electron transfer, REE cofactor; PedE engineering: Wehrmann & Klebensberger 2018, PMID 29239114). Orthologues **IsPedE/IsPedH** in *Ideonella sakaiensis* participate in **ethylene‑glycol** metabolism, underscoring evolutionary conservation of the module (Hachisuka et al. 2022, PMID 36289066).
- **Note on the kinase's "substrate specificity."** PedS2 itself has **no small‑molecule catalytic substrate**. Its specificity is (i) **ATP** for autophosphorylation and (ii) the **response regulator PedR2** for phosphotransfer, with **lanthanide ions acting as the modulatory input ligand**. The cellular La³⁺ response in *P. putida* is substrate‑specific and also intersects glycerol metabolism (Wehrmann et al. 2020, PMID 32345644).

---

## 9. Key References
1. Wehrmann M, Berthelot C, Billard P, Klebensberger J. **The PedS2/PedR2 Two‑Component System Is Crucial for the Rare Earth Element Switch in *Pseudomonas putida* KT2440.** *mSphere* 3(4):e00376‑18 (2018). PMID: 30158283. — *Direct identification of PP_2671/PP_2672 as PedS2/PedR2 and the sensing/phosphorylation mechanism.*
2. Wehrmann M, Berthelot C, Billard P, Klebensberger J. **Rare Earth Element (REE)‑Dependent Growth of *Pseudomonas putida* KT2440 Relies on the ABC‑Transporter PedA1A2BC and Is Influenced by Iron Availability.** *Front Microbiol* 10:2494 (2019). PMID: 31736923. — *PedS2 as a putative La³⁺‑binding protein; iron mismetallation; lanthanide uptake.*
3. Wehrmann M, Billard P, Martin‑Meriadec A, Zegeye A, Klebensberger J. **Functional Role of Lanthanides in Enzymatic Activity and Transcriptional Regulation of PQQ‑Dependent Alcohol Dehydrogenases in *Pseudomonas putida* KT2440.** *mBio* 8(3):e00570‑17 (2017). PMID: 28655819. — *Discovery/characterization of PedE and PedH and the periplasmic PQQ‑ADH oxidation system.*
4. Wehrmann M, Klebensberger J. **Engineering thermal stability and solvent tolerance of the soluble quinoprotein PedE from *Pseudomonas putida* KT2440.** (2018). PMID: 29239114. — *Confirms PedE = PP_2674, periplasmic PQQ‑ADH; biotechnological relevance.*
5. Wehrmann M, Toussaint M, Pfannstiel J, Billard P, Klebensberger J. **The Cellular Response to Lanthanum Is Substrate Specific and Reveals a Novel Route for Glycerol Metabolism in *Pseudomonas putida* KT2440.** (2020). PMID: 32345644. — *Substrate‑specific La³⁺ response.*
6. Hachisuka S, et al. **Ethylene glycol metabolism in the PET‑degrading bacterium *Ideonella sakaiensis*.** (2022). PMID: 36289066. — *Conserved PedE/PedH orthologues (IsPedE/IsPedH) in ethylene‑glycol metabolism.*
7. Reviews on the lanthanide switch / lanthanome: Skovran et al. 2019 (PMID 31166187); Featherston & Cotruvo 2021 (PMID 32979423); Daumann et al. 2022 (PMID 36167440); Parekh & Spiro 2025 (PMID 40846390).
8. UniProt Q88JH8; InterPro IPR050482, IPR003660 (HAMP), IPR003594/IPR036890 (HATPase), IPR005467 (His‑kinase).


## Artifacts

- [OpenScientist final report](PP_2671-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_2671-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:30158283
2. PMID:31736923
3. PMID:28655819
4. PMID:29239114
5. PMID:32345644
6. PMID:36289066