---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T06:14:28.881495'
end_time: '2026-08-31T06:26:08.103980'
duration_seconds: 699.22
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: exaE
  gene_symbol: exaE
  uniprot_accession: Q88JH7
  protein_description: 'SubName: Full=Transcriptional activator protein ExaE {ECO:0000313|EMBL:AAN68280.1};'
  gene_info: Name=exaE {ECO:0000313|EMBL:AAN68280.1}; OrderedLocusNames=PP_2672 {ECO:0000313|EMBL:AAN68280.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: CheY-like_superfamily. (IPR011006); NreC/VraR/RcsB-like_REC. (IPR058245);
    Sig_transdc_resp-reg_C-effctor. (IPR016032); Sig_transdc_resp-reg_receiver. (IPR001789);
    Tscrpt_reg_LuxR_C. (IPR000792)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: exaE-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: exaE-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88JH7
- **Protein Description:** SubName: Full=Transcriptional activator protein ExaE {ECO:0000313|EMBL:AAN68280.1};
- **Gene Information:** Name=exaE {ECO:0000313|EMBL:AAN68280.1}; OrderedLocusNames=PP_2672 {ECO:0000313|EMBL:AAN68280.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** CheY-like_superfamily. (IPR011006); NreC/VraR/RcsB-like_REC. (IPR058245); Sig_transdc_resp-reg_C-effctor. (IPR016032); Sig_transdc_resp-reg_receiver. (IPR001789); Tscrpt_reg_LuxR_C. (IPR000792)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "exaE" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'exaE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **exaE** (gene ID: exaE, UniProt: Q88JH7) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of ExaE (PedR2) — *Pseudomonas putida* KT2440
**Gene:** `exaE` (synonym **`pedR2`**) · **Locus:** `PP_2672` · **UniProt:** Q88JH7 · **Length:** 212 aa

---

## 1. Summary (Answer to the Research Question)

**ExaE is not an enzyme, transporter, or structural protein — it is a DNA-binding signal-transduction protein.** Specifically, it is the **response-regulator (output) component of a bacterial two-component regulatory system**, belonging to the **LuxR/NarL (FixJ) subfamily** of response regulators. In *Pseudomonas putida* KT2440 the gene annotated `exaE` (PP_2672) has been **directly characterized experimentally as `pedR2`**, the response regulator that, together with its cognate membrane sensor histidine kinase **PedS2 (PP_2671)**, forms the **PedS2/PedR2 two-component system** (Wehrmann et al., 2018, PMID 30158283).

Its **primary molecular function** is to work as a **phosphorylation-controlled transcription factor**. When phosphorylated on a conserved receiver-domain aspartate (Asp53) by PedS2, ExaE/PedR2 **binds promoter DNA in the cytoplasm** and exerts **dual, opposite regulatory effects**: it **activates transcription of `pedE`** (PP_2674, a Ca²⁺-dependent periplasmic PQQ-alcohol dehydrogenase) and **represses transcription of `pedH`** (PP_2679, a lanthanide-dependent PQQ-alcohol dehydrogenase). This dual output implements the **"rare-earth-element (REE) switch"** that lets the cell choose which of two functionally redundant periplasmic alcohol dehydrogenases to deploy, depending on lanthanide availability. The pathway ultimately drives **periplasmic oxidation of a broad range of volatile alcohols and aldehydes** used as carbon/energy sources.

---

## 2. Protein Identity and Verification

The target was rigorously verified as the intended protein:

| Property | Value | Source |
|---|---|---|
| UniProt accession | Q88JH7 | UniProtKB |
| Gene name | `exaE` (= `pedR2`) | UniProt / EMBL AAN68280.1; PMID 30158283 |
| Locus tag | PP_2672 | UniProt |
| Organism | *Pseudomonas putida* KT2440 (taxid 160488) | UniProt |
| Length | 212 aa | UniProt |
| Architecture | N-terminal REC receiver domain + C-terminal LuxR-type HTH | UniProt / InterPro / Pfam |

**Identity is unambiguous and confirmed by experiment.** The gene symbol `exaE` derives from orthology to the *P. aeruginosa* ethanol-oxidation regulator ExaE/EraR. However, the *P. putida* locus PP_2672 has itself been studied directly and is referred to in that primary literature as **PedR2** (Wehrmann et al., 2018, PMID 30158283). Both names refer to the same protein; there is no cross-organism gene-symbol confusion — the domain architecture, genomic context, and experimental data all agree.

### Domain architecture (structural/bioinformatic evidence)
From UniProtKB (Q88JH7) and InterPro/Pfam:
- **Residues 2–118 — Response-regulator receiver (REC) domain** (Pfam **PF00072** `Response_reg`; CheY-like superfamily IPR011006; NreC/VraR/RcsB-like REC IPR058245). Contains the **phospho-acceptor site Asp53** (annotated "4-aspartylphosphate"), the canonical residue that receives the phosphoryl group in two-component signalling.
- **Residues 141–206 — LuxR-type helix-turn-helix (HTH) DNA-binding effector domain** (Pfam **PF00196** `GerE`; IPR000792 `Tscrpt_reg_LuxR_C`; IPR016032 signal-transduction response-regulator C-terminal effector).
- **GO annotations:** DNA binding; transcription cis-regulatory region binding (GO:0000976); phosphorelay signal transduction system (GO:0000160); regulation of DNA-templated transcription (GO:0006355).
- **No transmembrane segments** — ExaE/PedR2 is a soluble, two-domain cytoplasmic protein.

This two-domain "receiver + LuxR-HTH" layout is the textbook architecture of a **NarL/FixJ-family DNA-binding response regulator**, and the literature independently classifies ExaE/PedR2 as a member of the **LuxR family** (Mern et al., 2010, PMID 20093290; Wehrmann et al., 2018, PMID 30158283).

---

## 3. Genomic Context (Evidence for Function by Synteny)

Direct UniProt neighborhood analysis (organism taxid 160488) places PP_2672 in the **`ped` alcohol-oxidation gene cluster**:

| Locus | UniProt | Length | Product | Role |
|---|---|---|---|---|
| PP_2671 | Q88JH8 | 424 aa | **Sensor histidine kinase (PedS2 / "ExaD")** — HAMP (161–213) + His-kinase (236–424) domains, membrane-anchored with periplasmic sensor | Cognate kinase of ExaE |
| **PP_2672** | **Q88JH7** | **212 aa** | **Response regulator ExaE / PedR2** (this study) | **DNA-binding transcription factor** |
| PP_2673 | Q88JH6 | 219 aa | Pentapeptide-repeat protein | — |
| PP_2674 | Q88JH5 | 631 aa | **Quinoprotein (PQQ) alcohol dehydrogenase PedE** | Regulatory target (activated) |
| PP_2679 | — | — | **Lanthanide-dependent PQQ-ADH PedH** | Regulatory target (repressed) |

The immediate adjacency of the **cognate kinase (PP_2671)**, the **regulator (PP_2672)**, and the **structural enzyme gene `pedE` (PP_2674)** mirrors the syntenic `exaD–exaE–exaA` arrangement in *P. aeruginosa*, providing strong structural/evolutionary support for the regulator→dehydrogenase relationship.

---

## 4. Primary Function — Mechanistic Detail

### 4.1 ExaE/PedR2 is the output of the PedS2/PedR2 two-component system
Two-component systems couple a **sensor histidine kinase** to a **response regulator** via His→Asp phosphotransfer. Here:
- **PedS2 (PP_2671)** is a **membrane-bound sensor kinase** (HAMP + kinase domains) that senses **lanthanide (rare-earth-element, La³⁺) availability**, most likely by direct La³⁺ binding at its **periplasmic region** (Wehrmann et al., 2018, PMID 30158283).
- **PedR2 (PP_2672 = ExaE)** is the **cognate LuxR-type response regulator**. Phosphotransfer to its **Asp53** switches it into the active, DNA-binding state.

### 4.2 Dual transcriptional output — the "REE switch"
The defining experimental result (adaptive evolution, site-directed mutants, transcriptional `lacZ`/reporter fusions, complementation; Wehrmann et al., 2018, PMID 30158283):

- **In the absence of La³⁺:** PedS2 is kinase-active → **phospho-PedR2 accumulates** → **activates `pedE`** (Ca²⁺-dependent PQQ-ADH) **and represses `pedH`** (Ln³⁺-dependent PQQ-ADH). The cell uses **PedE**.
- **In the presence of La³⁺:** La³⁺ binding lowers PedS2 kinase activity → **less phospho-PedR2** → `pedE` activation falls and `pedH` repression is relieved; combined with activation of `pedH` by a second, still-undefined regulatory module, the cell **switches to PedH**.

Thus **ExaE/PedR2 is a dual-function transcription factor — a positive regulator of `pedE` and a negative regulator of `pedH`** — and its phosphorylation status is the molecular variable that selects between the two enzymes. This "inverse regulation" of two functionally redundant enzymes is an adaptive strategy to optimize growth on volatile alcohols according to environmental lanthanide supply (Wehrmann et al., 2017, PMID 28655819).

### 4.3 What the pathway accomplishes (the enzymes ExaE controls)
The downstream enzymes are **periplasmic PQQ-dependent alcohol dehydrogenases (PQQ-ADHs / PQQ-EDHs)**:
- **PedE (PP_2674):** Ca²⁺-dependent PQQ-ADH.
- **PedH (PP_2679):** Ln³⁺-dependent PQQ-ADH.
Both oxidize a **broad and overlapping substrate range — linear and aromatic primary and secondary alcohols, as well as aldehydes** — and are **crucial for efficient growth on volatile alcohols** (Wehrmann et al., 2017, PMID 28655819). These type-II quinoprotein ADHs are **soluble periplasmic enzymes** that pass electrons to a periplasmic cytochrome *c* (Toyama et al., 2004, PMID 15234265). ExaE/PedR2's biological "job" is therefore to **switch on the correct periplasmic alcohol-oxidation machinery** for carbon/energy acquisition and detoxification of volatile organic compounds.

### 4.4 Evolutionary/ortholog context
ExaE/PedR2 is the ortholog of the *P. aeruginosa* response regulator **ExaE (renamed EraR)** of the **EraSR (formerly ExaDE)** two-component system, which activates transcription of the quinoprotein ethanol dehydrogenase gene `exaA` (QEDH) during aerobic ethanol oxidation (Schobert & Görisch, 2001, PMID 11158353; Görisch, 2003, PMID 12686116; Mern et al., 2010, PMID 20093290). In *P. aeruginosa* the cognate kinase ExaD/EraS is **soluble/cytoplasmic**, whereas in *P. putida* PedS2 is **membrane-bound with a periplasmic La³⁺ sensor** — a mechanistic divergence, though the regulator's core role (LuxR-type activator of a PQQ-alcohol dehydrogenase gene) is conserved.

---

## 5. Localization — Where ExaE Acts

- **ExaE/PedR2 acts in the cytoplasm** as a DNA-binding transcription factor (soluble two-domain protein, no transmembrane segments; C-terminal LuxR-HTH binds promoter DNA).
- **Signal reception occurs at the membrane/periplasm:** the cognate kinase PedS2 senses lanthanides at its periplasmic region and relays the signal across the membrane via His→Asp phosphotransfer.
- **The catabolic output occurs in the periplasm:** the PedE/PedH PQQ-ADHs are soluble periplasmic enzymes (Toyama et al., 2004, PMID 15234265; Wehrmann et al., 2017/2018).

There is thus a clean spatial division of labour: **periplasmic sensing (PedS2) → cytoplasmic transcriptional decision (ExaE/PedR2) → periplasmic enzymatic oxidation (PedE/PedH).**

---

## 6. Supported and Refuted Hypotheses

**Supported:**
- ✅ ExaE is a **LuxR/NarL-family DNA-binding response regulator** (domain architecture + literature).
- ✅ ExaE = **PedR2**, the response regulator of the **PedS2/PedR2 TCS** (direct experiment; PMID 30158283).
- ✅ ExaE is a **dual regulator**: **activates `pedE`, represses `pedH`** (PMID 30158283).
- ✅ The system mediates the **lanthanide-dependent "REE switch"** between two periplasmic PQQ-ADHs (PMID 30158283, 28655819).
- ✅ ExaE acts as a **cytoplasmic transcription factor**; downstream enzymes are **periplasmic** (PMID 15234265, 28655819).

**Refuted / corrected:**
- ❌ Initial (orthology-based) assumption that the cognate kinase is soluble/cytoplasmic. **Corrected:** in *P. putida* the cognate kinase **PedS2 is membrane-bound with a periplasmic La³⁺-sensing region** (PMID 30158283). (The soluble-kinase description is true for the *P. aeruginosa* ortholog ExaD, not for *P. putida* PedS2.)
- ❌ That ExaE is an enzyme/transporter (its function is purely regulatory/DNA-binding).

---

## 7. Limitations and Future Directions

- **Direct DNA-binding evidence:** the exact `pedE`/`pedH` operator sequences bound by phospho-PedR2 have not been mapped by footprinting/EMSA in the primary abstracts reviewed; the activation/repression roles are inferred from genetics and reporter fusions. In-vitro binding-site definition would strengthen the mechanism.
- **`pedH` activation module:** a second, "yet unknown" regulator that positively controls `pedH` in the presence of La³⁺ remains unidentified (PMID 30158283).
- **Phospho-Asp53 requirement:** Asp53 is the predicted/annotated phospho-acceptor; a D53A/D53E mutant phenotype would formally confirm phosphorylation-dependence in *P. putida*.
- **Additional regulon members:** whether phospho-PedR2 controls genes beyond `pedE`/`pedH` (e.g., PQQ biosynthesis, cytochrome, downstream aldehyde dehydrogenases) is not fully defined.

---

## 8. Key References
1. Wehrmann M, Berthelot C, Billard P, Klebensberger J. **The PedS2/PedR2 Two-Component System Is Crucial for the Rare Earth Element Switch in *Pseudomonas putida* KT2440.** *mSphere* 3:e00376-18 (2018). PMID **30158283**. *(Direct characterization of PP_2671/PP_2672 = PedS2/PedR2; dual activation of pedE and repression of pedH.)*
2. Wehrmann M, Billard P, Martin-Meriadec A, Zegeye A, Klebensberger J. **Functional Role of Lanthanides in Enzymatic Activity and Transcriptional Regulation of PQQ-Dependent Alcohol Dehydrogenases in *P. putida* KT2440.** *mBio* 8:e00570-17 (2017). PMID **28655819**. *(PedE = PP_2674 Ca²⁺-dependent, PedH = PP_2679 Ln³⁺-dependent; broad alcohol/aldehyde substrate range; periplasmic; inverse regulation.)*
3. Wehrmann M, Toussaint M, Pfannstiel J, Billard P, Klebensberger J. **The Cellular Response to Lanthanum Is Substrate Specific...** *mBio* 11:e00516-20 (2020). PMID **32345644**.
4. Mern DS, Ha SW, Khodaverdi V, Gliese N, Görisch H. **A complex regulatory network controls aerobic ethanol oxidation in *P. aeruginosa*...** *Microbiology* 156:1505–1516 (2010). PMID **20093290**. *(ExaE renamed EraR; LuxR family; EraSR = ExaDE cognate pair.)*
5. Görisch H. **The ethanol oxidation system and its regulation in *P. aeruginosa*.** *Biochim Biophys Acta* 1647:98–102 (2003). PMID **12686116**. *(ExaD/ExaE controls exaA/QEDH transcription.)*
6. Schobert M, Görisch H. **A soluble two-component regulatory system controls expression of QEDH...** *Microbiology* 147:363–372 (2001). PMID **11158353**. *(Identification of the ExaD/ExaE TCS controlling exaA promoter.)*
7. Toyama H, Mathews FS, Adachi O, Matsushita K. **Quinohemoprotein alcohol dehydrogenases: structure, function, and physiology.** *Arch Biochem Biophys* 428:10–21 (2004). PMID **15234265**. *(Type-II PQQ-ADHs are soluble periplasmic enzymes.)*


## Artifacts

- [OpenScientist final report](exaE-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](exaE-deep-research-openscientist_artifacts/final_report.pdf)