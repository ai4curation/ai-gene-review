---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-14T05:47:31.723602'
end_time: '2026-11-14T05:59:12.825028'
duration_seconds: 701.1
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: TRPM1
  gene_symbol: TRPM1
  uniprot_accession: Q7Z4N2
  protein_description: 'RecName: Full=Transient receptor potential cation channel
    subfamily M member 1; AltName: Full=Long transient receptor potential channel
    1; Short=LTrpC1; AltName: Full=Melastatin-1;'
  gene_info: Name=TRPM1 {ECO:0000312|HGNC:HGNC:7146}; Synonyms=LTRPC1, MLSN {ECO:0000303|PubMed:11535825},
    MLSN1 {ECO:0000312|EMBL:BAC80203.1};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the transient receptor (TC 1.A.4) family. LTrpC
  protein_domains: Ion_trans_dom. (IPR005821); TRPM. (IPR050927); TRPM-like. (IPR057366);
    TRPM_SLOG. (IPR041491); TRPM_tetra. (IPR032415)
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
citation_count: 20
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: TRPM1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: TRPM1-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q7Z4N2
- **Protein Description:** RecName: Full=Transient receptor potential cation channel subfamily M member 1; AltName: Full=Long transient receptor potential channel 1; Short=LTrpC1; AltName: Full=Melastatin-1;
- **Gene Information:** Name=TRPM1 {ECO:0000312|HGNC:HGNC:7146}; Synonyms=LTRPC1, MLSN {ECO:0000303|PubMed:11535825}, MLSN1 {ECO:0000312|EMBL:BAC80203.1};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the transient receptor (TC 1.A.4) family. LTrpC
- **Key Domains:** Ion_trans_dom. (IPR005821); TRPM. (IPR050927); TRPM-like. (IPR057366); TRPM_SLOG. (IPR041491); TRPM_tetra. (IPR032415)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "TRPM1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'TRPM1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **TRPM1** (gene ID: TRPM1, UniProt: Q7Z4N2) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# TRPM1 (Transient Receptor Potential Cation Channel Subfamily M Member 1): A Functional Annotation Report

**Gene:** TRPM1 (synonyms: LTRPC1, MLSN, MLSN1, melastatin-1, LTrpC1)
**Protein:** Transient receptor potential cation channel subfamily M member 1
**UniProt:** Q7Z4N2 · **Organism:** *Homo sapiens* (Human) · **HGNC:** 7146
**Family:** TRP superfamily, melastatin (TRPM) subfamily — TRPM1 is the founding member

---

## Summary

**Human TRPM1 is a tetrameric, Ca²⁺-permeable, non-selective cation channel of the melastatin (TRPM) subfamily that performs no enzymatic catalysis — its molecular activity is the gated, passive transport of cations down their electrochemical gradient.** Its primary and best-characterized function is to serve as the **effector ("transduction") channel of retinal ON (depolarizing) bipolar cells**, the final element of the metabotropic glutamate signaling cascade that initiates the ON visual pathway responsible for dim-light (scotopic) vision.

The gating logic is distinctive and sign-inverting. TRPM1 is **constitutively open** — intrinsically conductive without any ligand. In the dark, photoreceptors tonically release glutamate, which activates the postsynaptic metabotropic glutamate receptor mGluR6 (GRM6) at the dendritic tips of ON-bipolar cells. mGluR6 signals through the heterotrimeric G-protein Go (Gαo1/Gβ3/Gγ13), and **both the Gαo and the Gβγ subunits bind TRPM1 and cooperatively force it closed**, hyperpolarizing the cell. At light onset, glutamate release falls; a dedicated R7-RGS/Gβ5 GTPase-activating complex (RGS7/RGS11 with adaptors R9AP and GPR179) accelerates Gαo-GTP hydrolysis, relieving the inhibition and allowing TRPM1 to open. The resulting cation influx depolarizes the ON-bipolar cell and generates the electroretinogram (ERG) b-wave. TRPM1 operates within a tightly organized "signalplex" scaffolded by nyctalopin (NYX) and transsynaptically assembled by the presynaptic adhesion protein LRIT3, with a large reserve pool held in the endoplasmic reticulum.

Clinical and biological corollaries confirm this function. Loss-of-function TRPM1 mutations are a principal cause of autosomal-recessive **complete congenital stationary night blindness (cCSNB)**, defined by an electronegative ERG (preserved a-wave, reduced b-wave). Autoantibodies against TRPM1 produce the same phenotype in **melanoma-associated retinopathy (MAR)**. TRPM1 was originally discovered as "melastatin" (MLSN1), a **melanoma differentiation/metastasis-suppressor marker**, and in melanocytes it contributes to Ca²⁺ homeostasis and melanogenesis — a secondary role that reinforces its core identity as a Ca²⁺-conducting channel.

---

## Identity Verification

The mandatory identification check converges on a single, unambiguous target:

| Verification Step | Result |
|---|---|
| Gene symbol matches protein description | ✅ "TRPM1" / melastatin-1 / LTRPC1 used consistently across literature |
| Organism correct | ✅ Human (Q7Z4N2); mechanism heavily studied and conserved in mouse models |
| Protein family/domains align | ✅ TRPM subfamily; six-TM cation channel; TRPM_SLOG (IPR041491) N-terminal homology region; TRPM_tetra (IPR032415) C-terminal coiled-coil |
| Conflicting same-symbol literature | ✅ None — "TRPM1" literature is internally consistent |

The gene symbol is **not ambiguous**; literature is abundant and specific. Research proceeded on the correct target.

---

## Key Findings

### Finding 1 — TRPM1 is the effector cation channel of the ON-bipolar light response, gated by the mGluR6–Gαo cascade

TRPM1 is the transduction channel that converts a chemical synaptic signal into an electrical response in retinal ON (depolarizing) bipolar cells. The circuit logic is counterintuitive. In darkness, photoreceptors are depolarized and continuously release glutamate, which activates **mGluR6**, a Group III metabotropic glutamate receptor at the dendritic tips of ON-bipolar cells. mGluR6 couples to the G-protein **Go**, and active Go holds TRPM1 **closed**, keeping the cell hyperpolarized. When light strikes the retina, photoreceptors hyperpolarize and *reduce* glutamate release; mGluR6 activity falls, Go is deactivated, **TRPM1 opens**, and the ON-bipolar cell depolarizes — producing the ERG b-wave. Trpm1-knockout mice entirely lack the ON-bipolar light response.

The mechanism is stated directly: *"In retinal ON bipolar cells, Go couples the metabotropic receptor mGluR6 to the TRPM1 channel and closes it in the dark, thus hyperpolarizing the cell. Light, via GTPase-activating proteins, deactivates Go, opens TRPM1 and depolarizes the cell"* [PMID: 27037829](https://pubmed.ncbi.nlm.nih.gov/27037829/). TRPM1 is explicitly *"the visual transduction channel downstream of metabotropic glutamate receptor 6 (mGluR6) on retinal ON bipolar cells"* [PMID: 29854741](https://pubmed.ncbi.nlm.nih.gov/29854741/), and the cascade is one in which *"synaptic transmission is initiated by the metabotropic glutamate receptor, mGluR6, that signals via the G-protein Go to control opening of the effector ion channel, TRPM1"* [PMID: 26961947](https://pubmed.ncbi.nlm.nih.gov/26961947/). This is the central, primary function of the gene product.

### Finding 2 — TRPM1 is a Ca²⁺-permeable, non-selective cation channel of the melastatin subfamily

TRPM1 (melastatin-1, LTRPC1) is the **founding member** of the eight-member TRPM subfamily. TRPM proteins possess six transmembrane domains with intracellular N- and C-termini and assemble as tetramers to form *"monovalent-permeable cation channels with variable selectivity for Ca²⁺, Mg²⁺ and other divalent cations"* [PMID: 15895246](https://pubmed.ncbi.nlm.nih.gov/15895246/). Functional evidence for Ca²⁺ conduction comes from melanocytes: *"lentiviral short hairpin RNA (shRNA)-mediated knockdown of TRPM1 results in reduced intracellular Ca²⁺ and decreased Ca²⁺ uptake suggesting a role for TRPM1 in Ca²⁺ homeostasis"* [PMID: 19587221](https://pubmed.ncbi.nlm.nih.gov/19587221/).

Recent (2026) cryo-EM work resolves a long-standing debate about whether TRPM1 conducts current independently: the channel adopts *"a non-canonical architecture with an inverted transmembrane domain,"* in which *"the VSLD and PD are arranged with an opposite handedness compared to other related channels. This inverted transmembrane domain allows the formation of a large pore-like structure that supports the role of TRPM1 as an ion channel"* [PMID: 41857038](https://pubmed.ncbi.nlm.nih.gov/41857038/). The channel's substrate, therefore, is **cations (notably Ca²⁺ and monovalent cations)** — not any chemical reactant.

### Finding 3 — TRPM1 localizes to ON-bipolar dendritic tips within a nyctalopin-scaffolded signalplex, with a large ER reserve pool

TRPM1's site of action is the **plasma membrane at the dendritic tips of ON-bipolar cells** — the postsynaptic site invaginating photoreceptor terminals — where it is assembled into a multiprotein signaling ensemble. A proteomic search identified the leucine-rich-repeat protein **nyctalopin (NYX)** as TRPM1's binding partner and scaffold: *"We have conducted a proteomic search for proteins associated with nyctalopin in the mouse retina and identified TRPM1 as the binding partner. We further demonstrate that nyctalopin additionally interacts with mGluR6 receptor. Disruption of mGluR6 prevented targeting of TRPM1 to the postsynaptic compartment of ON-bipolar neurons"* [PMID: 21832182](https://pubmed.ncbi.nlm.nih.gov/21832182/).

Assembly of the signalplex is organized transsynaptically by the presynaptic adhesion protein **LRIT3** in photoreceptors: *"the absence of LRIT3 expression leads to the disassembly of the postsynaptic glutamate signaling complex (signalplex) expressed on depolarizing bipolar cell (DBC) dendrites"* [PMID: 31189098](https://pubmed.ncbi.nlm.nih.gov/31189098/).

Notably, only a minority of cellular TRPM1 sits at the dendritic tips at any moment; the majority is held as an intracellular reserve: *"the majority of TRPM1 is present in the ER, from which it can potentially be transported to the dendritic tips as needed for ON light response"* [PMID: 30027108](https://pubmed.ncbi.nlm.nih.gov/30027108/). This endoplasmic-reticulum pool (distinguished from Golgi by marker colocalization) likely acts as a trafficking buffer supplying functional channels to the synapse on demand.

### Finding 4 — Loss-of-function mutations cause complete congenital stationary night blindness; autoantibodies cause melanoma-associated retinopathy

The clinical genetics confirm TRPM1's role as the obligatory ON-pathway transduction channel. Human TRPM1 mutations are one of the principal causes of autosomal-recessive **complete congenital stationary night blindness (cCSNB)** — a non-progressive disorder with night blindness, myopia, nystagmus and a diagnostic **electronegative ERG** (reduced b-wave, preserved a-wave), reflecting selective loss of ON-bipolar transmission without photoreceptor degeneration. TRPM1 is one member of an interdependent signalplex: cCSNB is *"caused by mutations in one of several genes that are part of a large, interdependent depolarizing bipolar cell (DBC) signalplex required for normal synaptic signaling with photoreceptors. These genes include NYX, GRM6, TRPM1, GPR179, and LRIT3"* [PMID: 42471459](https://pubmed.ncbi.nlm.nih.gov/42471459/).

An independent, acquired route to the same phenotype is autoimmune. In some melanoma patients, circulating autoantibodies target TRPM1: *"MAR is caused by autoantibodies targeting TRPM1, an ion channel found in melanocytes and retinal ON-bipolar cells (ON-BCs). The visual symptoms arise when TRPM1 autoantibodies enter ON-BCs and block the function of TRPM1"* [PMID: 38946992](https://pubmed.ncbi.nlm.nih.gov/38946992/). Detection of anti-TRPM1 autoantibodies, combined with an electronegative ERG, is a diagnostic criterion for MAR. That a single channel's loss — whether genetic or autoimmune — abolishes ON-bipolar signaling is powerful functional proof that TRPM1 *is* the transduction channel.

### Finding 5 — In melanocytes, TRPM1 (melastatin-1) supports Ca²⁺ homeostasis/melanogenesis and is a melanoma differentiation/metastasis marker

TRPM1 was originally discovered in melanocytes as **"melastatin" (MLSN1)** — a gene whose expression correlates with terminal melanocytic differentiation and inversely with melanoma aggressiveness. *"mRNA expression of its founding member, TRPM1 (melastatin), correlates with terminal melanocytic differentiation and loss of its expression has been identified as an important diagnostic and prognostic marker for primary cutaneous melanoma"* [PMID: 22897572](https://pubmed.ncbi.nlm.nih.gov/22897572/). Earlier work showed melastatin transcripts are undetectable in melanoma metastases and that expression inversely tracks tumor thickness [PMID: 9537257](https://pubmed.ncbi.nlm.nih.gov/9537257/).

Functionally, TRPM1 knockdown in normal human melanocytes *"resulted in a decrease in tyrosinase activity and intracellular melanin pigment"* [PMID: 19587221](https://pubmed.ncbi.nlm.nih.gov/19587221/), linking TRPM1-mediated Ca²⁺ entry to melanin synthesis. The locus is also a dual-product gene: *"TRPM1 gene codes two transcripts: TRPM1 channel protein in its exons and miR-211 in one of its introns"* [PMID: 22897572](https://pubmed.ncbi.nlm.nih.gov/22897572/). The intronic microRNA **miR-211** (within intron 6) is co-processed with the mRNA and is itself implicated in the invasion-suppressor phenotype. This melanocyte role, while secondary to the retinal function, reinforces the core molecular identity: TRPM1 is a Ca²⁺-conducting channel whose activity shapes intracellular Ca²⁺.

### Finding 6 — TRPM1 is constitutively open and is closed by cooperative binding of both Gαo and Gβγ

A defining, unusual property of TRPM1 is that it is **intrinsically/constitutively active** — its resting state is *open*, and signaling acts to *close* it, inverting the usual expectation that a receptor cascade opens an effector channel. Dialysis experiments in mouse rod bipolar cells demonstrated the constitutive conductance and dissected the closing mechanism: a constitutively active Gαo mutant closes the channel, while reagents that sequester Gβγ (phosducin, or inactive Gαo) open it — indicating that *both* G-protein subunits participate. Co-immunoprecipitation showed TRPM1 interacts with Gβ3 and with both active and inactive Gαo; BRET mapping localized Gαo binding to both the N- and C-termini of TRPM1 and Gβγ binding to the N-terminus.

The authors state the problem and conclusion plainly: *"TRPM1 is thought to be constitutively open, but the mechanism that leads to its closure is unclear"* and *"Our physiological and biochemical results suggest that both Gαo and Gβγ bind TRPM1 channels and cooperate to close them"* [PMID: 26883481](https://pubmed.ncbi.nlm.nih.gov/26883481/). Recent single-channel recordings of purified human TRPM1 independently confirm ligand-independent activity: *"Our single-channel recordings reveal constitutive activity consistent with the conductive state captured"* [PMID: 42702620](https://pubmed.ncbi.nlm.nih.gov/42702620/). The dark-closed state is therefore an *actively imposed* block on an intrinsically conductive channel.

### Finding 7 — TRPM1 is a non-enzymatic "pure channel" — its molecular activity is cation transport, not catalysis

The question "what reaction does it catalyze?" has a definitive answer for TRPM1: **none**. Within the TRPM subfamily, enzymatic ("chanzyme") capability is confined to specific members. TRPM6 and TRPM7 uniquely bear C-terminal α-kinase domains. TRPM2 carries a C-terminal NUDT9-homology (NUDT9H) domain that senses ADP-ribose — but in vertebrates, including humans, this domain is **catalytically dead**: *"Thus, TRPM2 is not a 'chanzyme'"* [PMID: 27383051](https://pubmed.ncbi.nlm.nih.gov/27383051/), and *"TRPM2 Nudix motifs are canonical in all invertebrates but vestigial in vertebrates"* [PMID: 30938679](https://pubmed.ncbi.nlm.nih.gov/30938679/).

TRPM1 — together with TRPM3 and TRPM8 — carries **no enzymatic domain at all**. Its N-terminus contains the TRPM homology region / TRPM_SLOG domain (IPR041491), and its C-terminus bears a TRP helix and a coiled-coil tetramerization domain (IPR032415). These are structural/regulatory modules, not catalytic ones. TRPM1 should therefore be annotated functionally as a **transporter/ion channel**, with its molecular activity being the facilitated diffusion of cations — not as an enzyme.

### Finding 8 — The RGS7/RGS11–Gβ5 GAP complex sets the kinetics of TRPM1 opening by deactivating Gαo

The *timing* of TRPM1 opening — and therefore the speed and shape of the light response — is controlled by a dedicated GTPase-activating protein (GAP) module. The R7-family RGS proteins **RGS7 and RGS11**, together with obligate partner **Gβ5** and membrane adaptors **R9AP** and **GPR179**, accelerate hydrolysis of Gαo-GTP. When light lowers glutamate, this GAP complex rapidly deactivates Go, relieving inhibition on TRPM1 and permitting opening. Genetic ablation proves the requirement: in RGS7/RGS11 double-knockout mice, *"Gβ5S expression in the retinal outer plexiform layer is eliminated, as is the ERG b-wave"* [PMID: 22371490](https://pubmed.ncbi.nlm.nih.gov/22371490/).

The response is further tuned by additional dendritic-tip components. Protein kinase C alpha (PKCα) modulates kinetics: *"Protein kinase C alpha plays an important modulatory role in RBCs, regulating both the peak amplitude and temporal properties"* [PMID: 26230760](https://pubmed.ncbi.nlm.nih.gov/26230760/). A second metabotropic glutamate receptor, mGluR5, co-localizes with TRPM1/mGluR6 and provides a retrograde modulatory signal back to photoreceptors [PMID: 41371955](https://pubmed.ncbi.nlm.nih.gov/41371955/).

---

## Mechanistic Model / Interpretation

TRPM1 sits at the terminus of a G-protein signaling cascade whose remarkable features are **sign inversion plus constitutive channel activity**. The following diagram captures the complete transduction logic:

```
                    DARK                                      LIGHT
       (photoreceptor depolarized)              (photoreceptor hyperpolarized)
                     │                                          │
        high glutamate release                      low glutamate release
                     │                                          │
                     ▼                                          ▼
        ┌──────────────────────┐                   ┌──────────────────────┐
        │   mGluR6 (GRM6)      │ ACTIVE            │   mGluR6 (GRM6)      │ inactive
        └──────────┬───────────┘                   └──────────┬───────────┘
                   │                                          │
                   ▼                                          ▼
        Gαo-GTP + Gβ3γ13  (active Go)              RGS7/RGS11–Gβ5–R9AP–GPR179
                   │                                   GAP accelerates GTP hydrolysis
        Gαo AND Gβγ bind TRPM1                                 │
        and COOPERATIVELY CLOSE it                            ▼
                   │                                   Gαo-GDP (Go deactivated)
                   ▼                                          │
        ┌──────────────────────┐                             ▼
        │  TRPM1  = CLOSED     │                   ┌──────────────────────┐
        │  (intrinsically open │                   │  TRPM1  = OPEN       │
        │   but held shut)     │                   │  cation influx (Ca²⁺)│
        └──────────┬───────────┘                   └──────────┬───────────┘
                   ▼                                          ▼
        ON-bipolar HYPERPOLARIZED                  ON-bipolar DEPOLARIZED
                   │                                          │
                   ▼                                          ▼
           no b-wave                              ►►► ERG b-wave ◄◄◄
                                                   ON visual pathway active
```

The entire module is physically organized at the dendritic tip by a **signalplex**: nyctalopin (NYX) scaffolds TRPM1 and mGluR6; GPR179 anchors the RGS GAP complex; and presynaptic LRIT3 (in the photoreceptor terminal) transsynaptically instructs assembly of the postsynaptic ensemble. A large ER reserve pool feeds functional channel to the synapse.

**Comparative placement within the TRPM family:**

| Member | Catalytic domain | Enzyme activity | Signature function |
|---|---|---|---|
| **TRPM1** | **None** | **None (pure channel)** | **mGluR6-gated ON-bipolar transduction channel; melanocyte Ca²⁺** |
| TRPM2 | NUDT9H (ADPR) | Vestigial/absent in vertebrates | Oxidative-stress/ADPR-gated channel |
| TRPM3 | None | None | Thermo/steroid-sensitive channel |
| TRPM6/7 | α-kinase | Active kinase | Mg²⁺ homeostasis (chanzymes) |
| TRPM8 | None | None | Cold/menthol sensor |

The two tissue contexts of TRPM1 — retina and melanocyte — are unified by a single molecular job: **conducting Ca²⁺ (and other cations) across the plasma membrane under regulatory control**. In the retina the regulator is the mGluR6/Go cascade; in the melanocyte the Ca²⁺ influx feeds pigment-synthesis pathways (tyrosinase activity, melanin production) and differentiation state. In both cases the channel is non-enzymatic; its output is ionic, not chemical.

---

## Evidence Base

| PMID | Topic | How it supports the findings |
|---|---|---|
| [27037829](https://pubmed.ncbi.nlm.nih.gov/27037829/) | mGluR6 cascade | Core gating: Go closes TRPM1 in dark; light deactivates Go, opens TRPM1 (F1) |
| [29854741](https://pubmed.ncbi.nlm.nih.gov/29854741/) | TRPM1/mGluR6 KO | TRPM1 is the mGluR6-downstream transduction channel (F1) |
| [26961947](https://pubmed.ncbi.nlm.nih.gov/26961947/) | RGS anchoring | mGluR6-Go control of effector channel TRPM1; GAP role (F1, F8) |
| [15895246](https://pubmed.ncbi.nlm.nih.gov/15895246/) | TRPM overview | Channel topology and cation permeability of the subfamily (F2) |
| [19587221](https://pubmed.ncbi.nlm.nih.gov/19587221/) | Melanocyte Ca²⁺ | TRPM1 conducts Ca²⁺; links to tyrosinase/melanin (F2, F5) |
| [41857038](https://pubmed.ncbi.nlm.nih.gov/41857038/) | Cryo-EM | Non-canonical inverted TM domain; large pore; ion-channel architecture (F2) |
| [21832182](https://pubmed.ncbi.nlm.nih.gov/21832182/) | TRPM1–nyctalopin | TRPM1 binds NYX; mGluR6-dependent postsynaptic targeting (F3) |
| [30027108](https://pubmed.ncbi.nlm.nih.gov/30027108/) | ER pool | Large intracellular ER reserve pool (F3) |
| [31189098](https://pubmed.ncbi.nlm.nih.gov/31189098/) | LRIT3 | Transsynaptic assembly of TRPM1-containing signalplex (F3) |
| [42471459](https://pubmed.ncbi.nlm.nih.gov/42471459/) | cCSNB gene therapy | TRPM1 among cCSNB signalplex genes (F4) |
| [38946992](https://pubmed.ncbi.nlm.nih.gov/38946992/) | MAR | Anti-TRPM1 autoantibody mechanism of MAR (F4) |
| [9537257](https://pubmed.ncbi.nlm.nih.gov/9537257/) | Melastatin/metastasis | Melastatin/MLSN1 inversely tracks melanoma aggressiveness (F5) |
| [22897572](https://pubmed.ncbi.nlm.nih.gov/22897572/) | TRPM in melanoma | Differentiation/prognostic marker; miR-211 dual product (F5) |
| [26883481](https://pubmed.ncbi.nlm.nih.gov/26883481/) | Gα/Gβγ gating | Constitutively open; closed cooperatively by Gαo and Gβγ (F6) |
| [42702620](https://pubmed.ncbi.nlm.nih.gov/42702620/) | Constitutive gating | Single-channel constitutive activity of human TRPM1 (F6) |
| [27383051](https://pubmed.ncbi.nlm.nih.gov/27383051/) | TRPM2 chanzyme | TRPM channels are channels, not enzymes (F7) |
| [30938679](https://pubmed.ncbi.nlm.nih.gov/30938679/) | TRPM2 evolution | Enzymatic capacity vestigial/absent in vertebrate TRPM (F7) |
| [22371490](https://pubmed.ncbi.nlm.nih.gov/22371490/) | RGS7/RGS11 KO | R7-RGS/Gβ5 GAP complex essential for TRPM1-mediated b-wave (F8) |
| [26230760](https://pubmed.ncbi.nlm.nih.gov/26230760/) | PKCα | PKCα modulates TRPM1-dependent response kinetics (F8) |
| [41371955](https://pubmed.ncbi.nlm.nih.gov/41371955/) | mGluR5 | mGluR5 co-localizes with TRPM1; retrograde modulation (F8) |

**Convergence of evidence.** The identification of TRPM1 as the ON-bipolar transduction channel rests on independent lines: (1) genetic knockout abolishing the ON response; (2) human loss-of-function mutations causing cCSNB with an electronegative ERG; (3) autoantibody-mediated blockade producing the identical phenotype (MAR); (4) direct electrophysiology of its constitutive activity and G-protein gating; and (5) recent cryo-EM structural confirmation of its channel architecture. The non-enzymatic conclusion is supported by domain-level comparative analysis across the TRPM family. This is a robust, multi-pronged evidence base.

---

## Limitations and Knowledge Gaps

- **Species of mechanistic studies.** Much of the detailed gating, localization, and signalplex biology was established in **mouse** retina. The core identity is confirmed in human (human mutations cause cCSNB; human single-channel and cryo-EM data exist), but fine kinetic parameters are largely inferred from rodent models.
- **Molecular basis of constitutive gating and Go-imposed closure.** Although both Gαo and Gβγ are shown to bind and cooperatively close TRPM1, the structural transition translating G-protein binding into pore closure — and what makes the channel intrinsically open — is not fully resolved. A complete open↔closed structural trajectory with bound Go is still lacking.
- **Permeation/selectivity in situ.** Exact single-channel conductance, Ca²⁺-vs-monovalent selectivity, and divalent block in native ON-bipolar membranes remain incompletely quantified; purified human TRPM1 has historically shown challenging biochemical behavior.
- **ER reserve pool dynamics.** The signals and machinery that mobilize the large ER-resident pool to the dendritic tips (and whether this is light-history dependent) are unknown.
- **Melanocyte pathway details.** Downstream coupling from TRPM1 Ca²⁺ entry to tyrosinase/melanogenesis, and the mechanistic relationship between the channel protein and intronic miR-211 in tumor suppression, remain correlative.
- **Homomer vs. heteromer.** Whether TRPM1 functions purely as a homomer or heteromerizes with TRPM3 in vivo is unresolved.

---

## Proposed Follow-up Experiments / Actions

1. **Structure of the gated channel.** Solve cryo-EM structures of human TRPM1 bound to active Gαo and to Gβγ to visualize the closed state and define the cooperative closure mechanism; include a nucleotide/modulator series to capture open↔closed intermediates.
2. **Quantitative native electrophysiology.** Measure single-channel conductance, Ca²⁺/monovalent permeability ratios, and divalent block directly in human/primate ON-bipolar dendrites or a faithful reconstituted signalplex, to establish the physiological permeation profile.
3. **ER pool mobilization.** Use live-cell imaging of tagged TRPM1 in retinal explants to test whether light/dark history dynamically traffics the ER reserve to dendritic tips, and identify the trafficking machinery.
4. **Dissect Gα vs. Gβγ contributions in vivo.** Use subunit-selective perturbations (guided by the BRET-mapped N- vs. C-terminal binding sites) in mouse retina to quantify each subunit's contribution to closure kinetics and b-wave shape.
5. **Melanocyte Ca²⁺–melanogenesis coupling.** Combine TRPM1 knockdown/rescue with real-time Ca²⁺ imaging and tyrosinase assays to establish the causal chain from channel flux to pigment synthesis, separating channel-protein effects from intronic miR-211 effects.
6. **Therapeutic translation.** Build on existing gene-augmentation proof-of-concept in cCSNB models [PMID: 42471459](https://pubmed.ncbi.nlm.nih.gov/42471459/) by optimizing ON-bipolar-targeted TRPM1 delivery, and explore immunomodulatory/blood-retinal-barrier strategies for anti-TRPM1 autoantibody-mediated MAR.

---

## Conclusion

Human **TRPM1 (Q7Z4N2)** is a tetrameric, Ca²⁺-permeable, non-selective cation channel of the TRPM (melastatin) subfamily that **catalyzes no reaction** — its molecular activity is regulated passive cation transport. Its **primary function** is to serve as the **effector transduction channel of retinal ON-bipolar cells**: a constitutively open channel held closed in the dark by Gαo/Gβγ downstream of glutamate-activated mGluR6, and opened at light onset when the RGS7/RGS11–Gβ5–R9AP–GPR179 GAP complex deactivates Go — depolarizing the cell, generating the ERG b-wave, and driving the ON visual pathway for dim-light vision. It acts at the **postsynaptic dendritic-tip plasma membrane** within a nyctalopin/mGluR6/LRIT3/GPR179 signalplex, backed by a large ER reserve pool. Its loss (by mutation) causes complete congenital stationary night blindness, and autoantibodies against it cause melanoma-associated retinopathy. A **secondary role** in melanocytes supports Ca²⁺ homeostasis and melanogenesis, where the gene — first known as "melastatin" — is a melanoma differentiation/metastasis marker.


## Artifacts

- [OpenScientist final report](TRPM1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](TRPM1-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:27037829
2. PMID:29854741
3. PMID:26961947
4. PMID:15895246
5. PMID:19587221
6. PMID:41857038
7. PMID:21832182
8. PMID:31189098
9. PMID:30027108
10. PMID:42471459
11. PMID:38946992
12. PMID:22897572
13. PMID:9537257
14. PMID:26883481
15. PMID:42702620
16. PMID:27383051
17. PMID:30938679
18. PMID:22371490
19. PMID:26230760
20. PMID:41371955