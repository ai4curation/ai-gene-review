---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-19T08:21:24.150025'
end_time: '2026-07-19T08:42:45.934514'
duration_seconds: 1281.78
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: TFR2
  gene_symbol: TFR2
  uniprot_accession: Q9UP52
  protein_description: 'RecName: Full=Transferrin receptor protein 2; Short=TfR2;'
  gene_info: Name=TFR2;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the peptidase M28 family. M28B subfamily.
  protein_domains: PA_dom_sf. (IPR046450); PA_domain. (IPR003137); Peptidase_M28.
    (IPR007484); Peptidase_M28B. (IPR039373); TFR-like_dimer_dom_sf. (IPR036757)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: TFR2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: TFR2-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q9UP52
- **Protein Description:** RecName: Full=Transferrin receptor protein 2; Short=TfR2;
- **Gene Information:** Name=TFR2;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the peptidase M28 family. M28B subfamily.
- **Key Domains:** PA_dom_sf. (IPR046450); PA_domain. (IPR003137); Peptidase_M28. (IPR007484); Peptidase_M28B. (IPR039373); TFR-like_dimer_dom_sf. (IPR036757)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "TFR2" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'TFR2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **TFR2** (gene ID: TFR2, UniProt: Q9UP52) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of Human TFR2 (Transferrin Receptor Protein 2)

**Gene:** TFR2 · **UniProt:** Q9UP52 · **Organism:** *Homo sapiens* (human)
**Protein family (InterPro/UniProt):** Peptidase M28, subfamily M28B (a non-catalytic, "pseudo-peptidase" receptor branch); PA domain; TfR-like dimerization domain.

---

## 1. Identity verification

The gene symbol **TFR2** unambiguously matches the UniProt record Q9UP52: "Transferrin receptor protein 2 (TfR2)," human. The literature is abundant and internally consistent for exactly this protein: a **type II single-pass transmembrane receptor**, homolog of transferrin receptor 1 (TFR1/TFRC), predominantly expressed in **hepatocytes and erythroid precursors**, functioning in systemic **iron homeostasis**. The domain architecture provided (peptidase M28B + PA domain + TfR-like dimerization domain) is precisely the architecture of the transferrin-receptor family. Importantly, although TFR2 is classified in **peptidase family M28**, it is a **non-catalytic member** — no proteolytic activity has been described; the protease-like fold instead serves as a ligand-binding/receptor scaffold, exactly as for its homolog TFR1. **No gene-symbol ambiguity was encountered**, and all retrieved literature concerns the correct protein.

---

## 2. Summary answer

**TFR2 is not an enzyme or a transporter of iron in the classical sense — it is a cell-surface iron-sensing receptor.** Its primary molecular function is to **bind diferric (holo-) transferrin** and, in response, to **positively regulate expression of the iron-master-hormone hepcidin** in hepatocytes, thereby controlling systemic iron balance. In erythroid cells it has a second role: it associates with the erythropoietin receptor (EPOR) and adjusts red-cell production to iron availability. Loss of TFR2 causes **hereditary hemochromatosis type 3 (HFE3)**, a systemic iron-overload disease.

---

## 3. Primary function: molecular mechanism

### 3.1 Ligand and substrate specificity
TFR2 is a **receptor for diferric (iron-loaded) transferrin (holo-Tf)**, not a catalytic enzyme. Its specificity is for the **iron-loaded** form:
- Adding **diferric Tf** (but **not** apo-Tf and **not** non-Tf-bound iron) to hepatoma cells raises TFR2 protein in a dose- and time-dependent, reversible, hepatocyte-specific manner. The increase is **post-transcriptional**, reflecting an increased protein half-life (protein stabilization), not more mRNA [Johnson & Enns, 2004, PMID 15319290].
- Ligand binding requires an **RGD (Arg-Gly-Asp) motif**; the G679A mutant cannot bind diferric Tf and is no longer regulated by ligand [Pagani et al., 2015, PMID 25637053].
- **N-linked glycosylation** (Asn 240/339/754) is not required for surface trafficking or Tf binding but **is required for holo-Tf-induced stabilization** and thus for the iron-sensing readout [Zhao & Enns, 2013, PMID 23556518].

Thus TFR2 works as a **sensor of the diferric-transferrin concentration** in blood: as transferrin saturation rises, holo-Tf stabilizes surface TFR2 (partly by blocking its iron-dependent cleavage/shedding), converting an extracellular iron signal into a receptor-abundance signal [PMID 15319290; PMID 25637053].

### 3.2 Downstream signaling to hepcidin
Once engaged by holo-Tf, TFR2 drives transcription of **hepcidin (HAMP)** through a receptor complex and a defined kinase cascade:
- **Membrane complex:** HFE, TFR2, and the BMP co-receptor **hemojuvelin (HJV)** assemble into a multiprotein plasma-membrane complex on hepatocytes; TFR2 residues **120–139** are required to bind both HFE and HJV. TFR2 and HJV each compete with TFR1 for HFE, so the balance of these receptors sets iron sensing [D'Alessio et al., 2012, PMID 22728873].
- **Kinase cascade:** Holo-Tf activation of TFR2 stimulates **ERK1/2 (MAPK)** phosphorylation, which cross-talks with and boosts the canonical **BMP6–SMAD1/5/8** pathway; the ERK inhibitor U0126 blunts holo-Tf-induced hepcidin [Ramey et al., 2009, PMID 19454495]. TFR2/HFE also up-regulate **furin** via MAPK/ERK, and furin maturation of BMPs feeds back onto hepcidin [Poli et al., 2010, PMID 20634490].
- **Net output:** Hepcidin protein is secreted, binds the iron exporter **ferroportin (SLC40A1)** on enterocytes and macrophages, and triggers its degradation, lowering dietary iron absorption and iron recycling [Kawabata 2018, PMID 29134618].

**Interpretation:** TFR2 is the "iron-replete" arm of the hepcidin thermostat — high transferrin saturation → stabilized TFR2 → ERK+SMAD signaling → high hepcidin → less iron entering plasma. This directly explains why loss of TFR2 causes iron overload.

---

## 3a. Structure and evolution: a pseudo-peptidase receptor

Direct feature analysis of the UniProt record (Q9UP52, 801 aa) defines the architecture and provides bioinformatic evidence for the non-catalytic nature of TFR2:
- **Topology:** a **type II single-pass membrane protein** — short cytoplasmic N-terminus (residues **1–83**, including a **disordered region 16–45** and an **endocytosis-signal motif at 23–26**), a **signal-anchor transmembrane helix (84–104)**, and a large **extracellular C-terminal ectodomain (105–801)** that carries the PA (protease-associated) domain, the peptidase-M28-like domain, and the TfR-like dimerization domain.
- **N-glycosylation** at N240, N339, N540, N754 — matching experimental mapping (N240/339/754 used; N540 not) [PMID 23556518].
- **No catalytic machinery:** the record annotates **no "Active site" and no "Metal binding" (catalytic zinc) residues**. Family M28 peptidases are normally **zinc-dependent** proteases; their absence in TFR2 is direct evidence that it is a **non-catalytic "pseudo-peptidase."**

**Evolutionary interpretation:** TFR2 arose from the same transferrin-receptor lineage as TFR1 (TFRC). The ancestral zinc-peptidase (M28/PA) fold has been **repurposed as a ligand-binding receptor scaffold** for holo-transferrin rather than to hydrolyze peptide bonds — a classic case of an enzyme fold evolving into a signaling/receptor module. This reconciles the UniProt "peptidase M28B" family assignment with the complete absence of any reported proteolytic activity in the experimental literature.

## 4. Localization: where TFR2 acts

- **Subcellular:** A **type II transmembrane glycoprotein** at the **plasma membrane** of hepatocytes, where it senses extracellular holo-Tf and nucleates the HFE/HJV signaling complex [PMID 22728873; PMID 23556518]. It also generates a **soluble ectodomain** by iron-regulated cleavage/shedding [PMID 25637053]. Correct **plasma-membrane localization is functionally essential**: the hemochromatosis mutation p.G792R (and the ALD-associated p.A75V) mislocalize TFR2 and impair hepcidin induction [Joshi et al., 2015, PMID 26029709; Xie et al., 2026, PMID 41677839].
- **Tissue/cell:** Expression is highly **restricted to hepatocytes and erythroid precursors** [PMID 29969719; PMID 32054685]. Within erythroblasts (and dopaminergic neurons) TFR2 additionally supports **intracellular iron trafficking from lysosomes to mitochondria** [Kawabata 2019, PMID 29969719].

---

## 4a. Isoforms: α-TFR2 vs β-TFR2

The **TFR2 gene produces two main transcripts**: full-length **α-TFR2** and a shorter **β-TFR2**. The two partition function by tissue [Roetto et al., 2010, PMID 20179178]:
- **α-TFR2** is the classical **diferric-transferrin sensor** that modulates hepcidin in the liver; hepatic α-TFR2 loss reproduces liver iron overload with inadequate hepcidin.
- **β-TFR2**, expressed in **spleen**, appears to control **splenic iron efflux** — β-specific knock-in mice have normal transferrin saturation/hepcidin but severe spleen iron accumulation with strikingly reduced splenic **ferroportin (Fpn1)**, suggesting β-TFR2 influences Fpn1 transcription independently of the hepcidin axis.

This isoform split refines the "single receptor" picture: the hepatic hepcidin-sensing function is an **α-TFR2** property, while extrahepatic/splenic iron handling involves **β-TFR2**.

## 5. Biochemical / signaling pathways in which TFR2 participates

1. **Iron-sensing → BMP/SMAD → hepcidin axis (liver).** Core pathway: diferric-Tf → TFR2 (with HFE/HJV) → ERK1/2 + BMP6/SMAD1/5/8 → HAMP transcription → ferroportin degradation → systemic iron control [PMID 22728873; PMID 19454495; PMID 20634490; PMID 29134618]. **In vivo genetic epistasis confirms TFR2 sits within the BMP6–SMAD axis:** combined loss of Tfr2 (or Hfe) plus Bmp6 markedly worsens iron overload versus Bmp6 knockout alone, with decreased Smad5 phosphorylation, further hepcidin repression, and iron loading of liver, pancreas, heart and kidney [Latour et al., 2016, PMID 26406355].
2. **Erythroid iron-sensing → EPOR axis (bone marrow).** TFR2 associates with and stabilizes **EPOR** on erythroblasts; bone-marrow-specific Tfr2 knockout increases hemoglobin/RBC counts, lowers MCV, and reduces erythroblast apoptosis, tuning erythropoiesis to iron availability [Nai et al., 2015, PMID 25499454; PMID 29969719]. Extrahepatic Tfr2 loss increases erythroferrone/EPO and expands the erythroid compartment independently of iron overload [Wortham et al., 2020, PMID 32054685].

We de-emphasize broad pleiotropic effects; the two axes above are the precise, mechanistically supported roles.

---

## 6. Genetic / disease evidence (loss-of-function confirms the mechanism)

- **Hereditary hemochromatosis type 3 (HFE3):** biallelic TFR2 loss-of-function causes intermediate-severity systemic iron overload with low hepcidin [PMID 29134618; PMID 30360575].
- **Mutation mechanisms** map onto the model: protein truncation (Gln306*, Gln672*), impaired membrane localization (p.G792R), and splicing defects (c.1606-8A>G) all yield a **non-functional receptor and defective hepcidin signaling** [PMID 26029709]; novel homozygous p.G446E produces classic HFE3 with markedly low serum hepcidin-25 [Tamai et al., 2024, PMID 38850209].
- **Model organisms:** zebrafish *tfr2* mutants recapitulate iron overload + hepcidin suppression [PMID 29897731]; multiple mouse knockouts confirm the hepatic and erythroid roles [PMID 25499454; PMID 32054685; PMID 41662592].

---

## 6a. Downstream axis and translational relevance

The signal TFR2 helps generate converges on the **hepcidin–ferroportin axis**: secreted hepcidin binds ferroportin (SLC40A1), the only cellular iron exporter, and induces its degradation, thereby reducing iron entry into plasma [Nai et al., 2025, PMID 40603805]. Because TFR2-driven hepcidin sits upstream of this rate-limiting step, TFR2 loss (low hepcidin) causes iron overload, while pharmacological restoration of hepcidin is being pursued therapeutically for hemochromatosis and β-thalassemia [PMID 40603805]. This positions TFR2 as the **iron-replete sensor input** to a druggable hormonal axis.

## 7. Supported vs. refuted hypotheses

| Hypothesis | Verdict | Key evidence |
|---|---|---|
| TFR2 is a diferric-transferrin sensor that positively regulates hepcidin | **Supported** | PMID 41662592, 15319290, 29134618 |
| TFR2 signals via a surface HFE–TFR2–HJV complex through ERK + BMP/SMAD | **Supported** | PMID 22728873, 19454495, 20634490 |
| TFR2 has a distinct erythroid role via EPOR and intracellular iron routing | **Supported** | PMID 25499454, 32054685, 29969719 |
| TFR2 (as an M28-family member) is a catalytically active peptidase | **Refuted / no evidence** | No proteolytic activity reported; family M28B receptor branch is non-catalytic |
| TFR2 is a major route of transferrin-bound iron *uptake* (like TFR1) | **Refuted** | Only TFR1-expressing hepatocytes internalize holo-Tf; TFR2 contributes negligibly to iron uptake (PMID 41662592) |

---

## 8. Limitations and future directions

- **Structure:** No high-resolution experimental structure of full-length human TFR2 was retrieved; the non-catalytic status is inferred here from UniProt feature annotation (no active-site/zinc residues) and the absence of any reported proteolytic activity. The exact conformational change coupling holo-Tf binding to ERK/SMAD activation remains to be defined (cryo-EM of the HFE–TFR2–HJV complex would help).
- **Signaling detail:** How ERK physically converges on SMAD and how furin fits kinetically is still partly correlative.
- **Erythroid vs hepatic separation:** Distinguishing cell-autonomous erythroid effects from secondary iron effects benefits from conditional models (already begun, e.g., PMID 32054685).
- **β-TFR2:** The molecular mechanism by which β-TFR2 controls splenic ferroportin/iron efflux is not yet defined.

---

*Report compiled across Iterations 1–5. Evidence prioritizes primary hepatocyte/erythroid cell studies, targeted mutagenesis, knockout models, and direct UniProt feature analysis over high-throughput data. 26 papers reviewed; 8 findings recorded.*


## Artifacts

- [OpenScientist final report](TFR2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](TFR2-deep-research-openscientist_artifacts/final_report.pdf)