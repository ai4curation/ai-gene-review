---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-04T01:10:35.612546'
end_time: '2026-10-04T01:23:22.109897'
duration_seconds: 766.5
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: PIAS1
  gene_symbol: PIAS1
  uniprot_accession: O75925
  protein_description: 'RecName: Full=E3 SUMO-protein ligase PIAS1; EC=2.3.2.- {ECO:0000269|PubMed:15280358,
    ECO:0000269|PubMed:36050397}; AltName: Full=DEAD/H box-binding protein 1; AltName:
    Full=E3 SUMO-protein transferase PIAS1 {ECO:0000305}; AltName: Full=Gu-binding
    protein; Short=GBP; AltName: Full=Protein inhibitor of activated STAT protein
    1; AltName: Full=RNA helicase II-binding protein;'
  gene_info: Name=PIAS1; Synonyms=DDXBP1;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the PIAS family. .
  protein_domains: PINIT. (IPR023321); PINIT_sf. (IPR038654); SAP_dom. (IPR003034);
    SAP_dom_sf. (IPR036361); Znf_MIZ. (IPR004181)
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
citation_count: 24
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PIAS1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PIAS1-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** O75925
- **Protein Description:** RecName: Full=E3 SUMO-protein ligase PIAS1; EC=2.3.2.- {ECO:0000269|PubMed:15280358, ECO:0000269|PubMed:36050397}; AltName: Full=DEAD/H box-binding protein 1; AltName: Full=E3 SUMO-protein transferase PIAS1 {ECO:0000305}; AltName: Full=Gu-binding protein; Short=GBP; AltName: Full=Protein inhibitor of activated STAT protein 1; AltName: Full=RNA helicase II-binding protein;
- **Gene Information:** Name=PIAS1; Synonyms=DDXBP1;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the PIAS family. .
- **Key Domains:** PINIT. (IPR023321); PINIT_sf. (IPR038654); SAP_dom. (IPR003034); SAP_dom_sf. (IPR036361); Znf_MIZ. (IPR004181)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PIAS1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PIAS1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PIAS1** (gene ID: PIAS1, UniProt: O75925) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# PIAS1 (O75925): A Nuclear SUMO E3 Ligase and SUMO-Independent Gatekeeper of STAT1/NF-κB Transcription

**Gene:** PIAS1 (synonym DDXBP1) · **Protein:** E3 SUMO-protein ligase PIAS1 · **Organism:** *Homo sapiens* · **EC:** 2.3.2.-
**Family:** PIAS family · **Domains:** SAP (IPR003034), PINIT (IPR023321), SP-RING / Znf-MIZ (IPR004181), SIM motifs

## Summary

**PIAS1** (Protein Inhibitor of Activated STAT1; gene *PIAS1*, synonym *DDXBP1*; UniProt **O75925**) is a predominantly nuclear enzyme with a dual molecular personality. First, it is a *bona fide* **SUMO (Small Ubiquitin-like MOdifier) E3 ligase** (EC 2.3.2.-) belonging to the PIAS family. Using its catalytic **SP-RING/MIZ-type zinc finger** domain, it recruits the SUMO-charged E2 conjugating enzyme Ubc9 and catalyzes transfer of SUMO (chiefly SUMO1) onto lysine residues—frequently within the canonical ΨKxE consensus motif—of a diverse set of nuclear substrates including Smad4, PPARγ, HMGN2, the metabotropic glutamate receptor mGluR8b, and the Epstein-Barr virus protein EBNA1. Through this catalysis it tunes the stability, chromatin association, and transcriptional output of its targets.

Second, and in parallel with its enzymatic activity, PIAS1 functions as a **selective transcriptional repressor that does not require SUMOylation of its target**. It was originally discovered as a specific inhibitor of STAT1: it binds the tyrosine-phosphorylated STAT1 dimer and the NF-κB subunit p65, and physically blocks their ability to bind DNA at target-gene promoters. This "promoter gatekeeper" activity constrains interferon-driven and inflammatory gene programs. The repressive function is switched on during inflammation by **IKKα-mediated phosphorylation of PIAS1 on Ser90**, and has been genetically validated in *Pias1*-knockout mice, which show heightened interferon responses and elevated proinflammatory cytokines.

PIAS1 carries out these functions **in the nucleus**. Specific nuclear locations of action include **PML nuclear bodies** (where it contributes to intrinsic antiviral defense against herpes simplex virus 1) and **sites of DNA double-strand breaks** (where, together with PIAS4, it catalyzes SUMO accumulation required for assembly of repair factors such as 53BP1, BRCA1, and RNF168). In short, PIAS1 is a nuclear SUMO ligase and a SUMO-independent STAT1/NF-κB brake, integrating post-translational modification with direct control of transcription-factor DNA binding.

---

## Gene/Protein Identity Verification

Before presenting findings, the target identity was confirmed against the UniProt record:

| Attribute | Expected (UniProt O75925) | Confirmed in literature |
|-----------|---------------------------|--------------------------|
| Gene symbol | PIAS1 (synonym DDXBP1) | Yes — "Protein Inhibitor of Activated STAT1" ([PMID: 9724754](https://pubmed.ncbi.nlm.nih.gov/9724754/)) |
| Organism | *Homo sapiens* | Human cell studies confirmed; orthologs cross-referenced |
| Enzyme class | E3 SUMO-protein ligase, EC 2.3.2.- | Yes ([PMID: 42102412](https://pubmed.ncbi.nlm.nih.gov/42102412/), [PMID: 28330929](https://pubmed.ncbi.nlm.nih.gov/28330929/)) |
| Family | PIAS family | Yes |
| Key domains | PINIT, SAP, Znf-MIZ (SP-RING) | Yes — all three functionally characterized |

The alternate names in the UniProt record ("DEAD/H box-binding protein 1," "Gu-binding protein," "RNA helicase II-binding protein") derive from PIAS1's original identification as a binding partner of the nucleolar RNA helicase RH-II/Gu (DDX21). This is consistent with the historical literature ([PMID: 9631199](https://pubmed.ncbi.nlm.nih.gov/9631199/), [PMID: 10727979](https://pubmed.ncbi.nlm.nih.gov/10727979/)) but is not the primary characterized function. The identity is unambiguous and all research below pertains to the correct protein.

---

## Key Findings

### 1. PIAS1 is a SUMO E3 ligase — its primary enzymatic function

PIAS1 catalyzes the covalent attachment of SUMO to substrate proteins, the defining biochemical activity of the protein. Multiple primary and review sources identify PIAS1 as a SUMO E3 ligase (EC 2.3.2.-) within the PIAS family. The enzyme contains the **SP-RING/Znf-MIZ** catalytic zinc finger together with **PINIT** and **SAP** domains that mediate substrate engagement and positioning of the SUMO-charged E2 (Ubc9). Mechanistically, PIAS1 promotes transfer of SUMO (principally SUMO1) onto lysine residues of substrate transcription factors and other nuclear proteins, thereby altering their stability, subcellular localization, and transcriptional activity.

A 2024 cardiovascular study states directly that "Protein inhibitor of activated STAT 1 (PIAS1) functions as a SUMO E3 ligase, regulating cardiovascular diseases by promoting the SUMOylation of target proteins" ([PMID: 42102412](https://pubmed.ncbi.nlm.nih.gov/42102412/)). A dedicated review of the PIAS family notes that "the protein inhibitor of activated STAT (PIAS) E3-ligases were initially described as transcriptional coregulators" before their SUMO-ligase function was defined ([PMID: 28330929](https://pubmed.ncbi.nlm.nih.gov/28330929/)).

### 2. Catalytic mechanism: an SP-RING ligase using SIMs and a Ubc9/SUMO1 ternary complex

PIAS1 operates via its SP-RING (Znf-MIZ, InterPro IPR004181) domain, which binds the SUMO-charged Ubc9 to catalyze SUMO transfer to substrate lysines—analogous to the RING-domain mechanism used by ubiquitin E3 ligases. Biochemical and structural work established that PIAS proteins contain conserved **SUMO-interacting motifs (SIMs)**: a central SIM1 and, in PIAS1-3, a C-terminal SIM2. The study by Lussier-Price et al. showed that "the PIAS-SIM2 plays a key role in formation of a UBC9-PIAS1-SUMO1 complex" ([PMID: 32348746](https://pubmed.ncbi.nlm.nih.gov/32348746/)), identifying the molecular assembly required for catalysis. The same work confirmed that "the human PIAS proteins are small ubiquitin-like modifier (SUMO) E3 ligases that participate in important cellular functions."

Substrate engagement is modular:
- **SAP domain** (N-terminal): binds AT-rich DNA/chromatin and mediates recruitment to damage sites.
- **PINIT domain**: contributes to substrate recruitment and nuclear retention.
- **SP-RING domain**: binds Ubc9~SUMO thioester for catalysis.
- **SIM(s)**: bind non-covalent SUMO to orient the transfer reaction.

These interactions can be fine-tuned by phosphorylation of the SIM or acetylation of SUMO1, providing regulatory layers on top of the core catalytic cycle.

### 3. PIAS1 negatively regulates STAT1 by blocking DNA binding — a SUMO-independent mechanism

PIAS1 was originally isolated precisely as an inhibitor of STAT1. The founding study demonstrated that "PIAS1, but not other PIAS proteins, blocked the DNA binding activity of Stat1 and inhibited Stat1-mediated gene activation in response to interferon" ([PMID: 9724754](https://pubmed.ncbi.nlm.nih.gov/9724754/)). Importantly, the inhibitory interaction is highly specific for the activated form of STAT1: PIAS1 associates with STAT1 (but not STAT2 or STAT3) only after STAT1 is tyrosine-phosphorylated (Tyr701) and dimerized.

The structural basis was mapped by Liao et al.: a C-terminal region of PIAS1 (amino acids 392–541) directly contacts the N-terminal domain of STAT1 (amino acids 1–191), and PIAS1 "specifically interacts with the Stat1 dimer, but not tyrosine-phosphorylated or -unphosphorylated Stat1 monomer" ([PMID: 10805787](https://pubmed.ncbi.nlm.nih.gov/10805787/)). The N-terminal region of PIAS1 serves as a modulatory domain preventing premature engagement with STAT1 monomers.

Crucially, although STAT1 can itself be SUMOylated at Lys703, the transcriptional-inhibitory function does **not** require this modification. Rogers et al. showed that "inhibition of STAT1 by PIAS proteins does not require SUMO modification of STAT1 itself" ([PMID: 12764129](https://pubmed.ncbi.nlm.nih.gov/12764129/)). This cleanly separates the repressive promoter-blocking activity from the catalytic SUMO-ligase activity.

The mechanism was validated *in vivo*: in *Pias1*-knockout mice, "PIAS1 selectively regulates a subset of IFN-gamma- or IFN-beta-inducible genes by interfering with the recruitment of STAT1 to the gene promoter," and loss of PIAS1 enhances antiviral activity ([PMID: 15311277](https://pubmed.ncbi.nlm.nih.gov/15311277/)). Independent confirmation of the STAT1-PIAS1 interaction and its functional consequence comes from studies in orthologs, where "Co-IP showed that they separately inhibited the phosphorylation of STAT1 via interacting with it, which leads to the reduction of IFN1 expression" ([PMID: 34331975](https://pubmed.ncbi.nlm.nih.gov/34331975/)), and in human cells, where PIAS1 was identified as "an inhibitor of IFN-activated transcription factor STAT1" ([PMID: 29848755](https://pubmed.ncbi.nlm.nih.gov/29848755/)).

### 4. PIAS1 negatively regulates NF-κB by blocking p65 DNA binding — validated in vivo

Parallel to its action on STAT1, PIAS1 restrains the NF-κB pathway. Upon cytokine stimulation, the p65 (RelA) subunit translocates to the nucleus and interacts with PIAS1. Liu et al. demonstrated that "the binding of PIAS1 to p65 inhibits cytokine-induced NF-kappaB-dependent gene activation. PIAS1 blocks the DNA binding activity of p65 both in vitro and in vivo" ([PMID: 15657437](https://pubmed.ncbi.nlm.nih.gov/15657437/)).

Genetic evidence corroborates the biochemistry: in *Pias1*-null cells, "the binding of p65 to the promoters of NF-kappaB-regulated genes is significantly enhanced," and at the whole-animal level, "Pias1 null mice showed elevated proinflammatory cytokines" ([PMID: 15657437](https://pubmed.ncbi.nlm.nih.gov/15657437/)). Thus PIAS1 limits p65 promoter occupancy and dampens inflammatory gene output.

### 5. The repressive switch: IKKα-mediated Ser90 phosphorylation during inflammation

PIAS1's gatekeeper activity is not constitutive but inducible. Liu et al. showed that "PIAS1 becomes rapidly phosphorylated on Ser90 residue in response to various inflammatory stimuli. Mutational studies indicate that Ser90 phosphorylation is required for PIAS1 to repress transcription" ([PMID: 17540171](https://pubmed.ncbi.nlm.nih.gov/17540171/)). Upon TNF treatment, wild-type PIAS1—but not the S90A mutant—rapidly associates with NF-κB target promoters.

The upstream kinase is **IKKα** specifically: "IKKalpha, but not IKKbeta, interacts with PIAS1 in vivo and mediates PIAS1 Ser90 phosphorylation, a process that requires the SUMO ligase activity of PIAS1" ([PMID: 17540171](https://pubmed.ncbi.nlm.nih.gov/17540171/)). Remarkably, the phosphorylation event itself depends on PIAS1's own SUMO-ligase activity, linking the two arms of PIAS1 function. The same study offers a unifying statement of mechanism: PIAS1 "inhibits immune responses by selectively blocking the binding of NF-kappaB and STAT1 to gene promoters" ([PMID: 17540171](https://pubmed.ncbi.nlm.nih.gov/17540171/)).

### 6. PIAS1 is a nuclear / PML nuclear-body protein contributing to intrinsic antiviral immunity

PIAS1 localizes predominantly to the nucleus (confirmed by subcellular fractionation of PIAS1 orthologs: "The subcellular localization and nuclear cytoplasm extraction showed that CiPIAS1a and CiPIAS1b were mainly distributed in the nucleus" — [PMID: 34331975](https://pubmed.ncbi.nlm.nih.gov/34331975/)). Within the nucleus, PIAS1 is a constituent of **promyelocytic leukemia nuclear bodies (PML-NBs)**. Alandijany et al. identified "the SUMO ligase protein inhibitor of activated STAT1 (PIAS1) as a constituent PML-NB protein" recruited in a SIM-dependent manner requiring SUMOylation-competent PML ([PMID: 27099310](https://pubmed.ncbi.nlm.nih.gov/27099310/)).

Functionally, upon HSV-1 infection, "PIAS1 promotes the stable accumulation of SUMO1 at nuclear sites associated with HSV-1 genome entry" ([PMID: 27099310](https://pubmed.ncbi.nlm.nih.gov/27099310/)), cooperating with PIAS4/PML to restrict viral genomes as part of intrinsic antiviral defense. This places PIAS1's SUMO-ligase activity at a defined spatial compartment where it silences incoming viral DNA.

### 7. PIAS1 promotes DNA double-strand break repair via SUMOylation at damage sites

PIAS1 is a core SUMOylation enzyme of the DNA-damage response. Galanty et al. showed that "SUMO1, SUMO2 and SUMO3 accumulate at DSB sites in mammalian cells, with SUMO1 and SUMO2/3 accrual requiring the E3 ligase enzymes PIAS4 and PIAS1" ([PMID: 20016603](https://pubmed.ncbi.nlm.nih.gov/20016603/)). Recruitment is mediated by the SAP domain: "PIAS1 and PIAS4 are recruited to damage sites via mechanisms requiring their SAP domains, and are needed for the productive association of 53BP1, BRCA1 and RNF168 with such regions" ([PMID: 20016603](https://pubmed.ncbi.nlm.nih.gov/20016603/)). The functional consequence is clear: "PIAS1 and PIAS4 promote DSB repair and confer ionizing radiation resistance" ([PMID: 20016603](https://pubmed.ncbi.nlm.nih.gov/20016603/)). PIAS1 thus couples SUMO deposition to the ubiquitin-mediated (RNF8/RNF168/BRCA1) repair-factor assembly cascade.

### 8. PIAS1 is a chromatin-bound, gene-selective transcriptional coregulator (androgen receptor)

Beyond acting as a repressor of inflammatory factors, PIAS1 functions as a gene-selective coregulator of the **androgen receptor (AR)**. ChIP-seq in VCaP prostate cancer cells showed that "PIAS1 is a genuine chromatin-bound AR coregulator that functions in a target gene selective fashion to regulate prostate cancer cell growth" ([PMID: 25552417](https://pubmed.ncbi.nlm.nih.gov/25552417/)). Androgen exposure "increased the number of PIAS1-occupying sites, resulting in nearly complete overlap with AR chromatin binding events" ([PMID: 25552417](https://pubmed.ncbi.nlm.nih.gov/25552417/)). PIAS1 depletion redistributes AR occupancy, activates or represses distinct subsets of AR target genes, exposes new loci to AR, and attenuates proliferation. The same AR coregulatory role operates in molecular apocrine breast cancer cells, where silencing PIAS1 influences AR function "in a target-selective fashion" with an anti-apoptotic effect ([PMID: 26219822](https://pubmed.ncbi.nlm.nih.gov/26219822/)).

### 9. Substrate repertoire: diverse nuclear substrates at ΨKxE-type sites

PIAS1 SUMOylates a broad but defined set of nuclear substrates, typically at lysines within or near the canonical ΨKxE consensus:

| Substrate | SUMO/site | Functional consequence | Reference |
|-----------|-----------|------------------------|-----------|
| **Smad4** | SUMO1, Lys159 (linker) | Enhances Smad-dependent TGF-β transcription | [PMID: 14514699](https://pubmed.ncbi.nlm.nih.gov/14514699/) |
| **PPARγ** | SUMO modification | Promotes NCoR corepressor retention, NF-κB transrepression | [PMID: 30419807](https://pubmed.ncbi.nlm.nih.gov/30419807/), [PMID: 24260304](https://pubmed.ncbi.nlm.nih.gov/24260304/) |
| **HMGN2** | SUMO1, Lys17/Lys35 | Reduces nucleosome-binding affinity | [PMID: 24872413](https://pubmed.ncbi.nlm.nih.gov/24872413/) |
| **mGluR8b** | SUMO1, Lys882 (VKSE motif) | Regulates receptor SUMOylation | [PMID: 21288202](https://pubmed.ncbi.nlm.nih.gov/21288202/) |
| **EBNA1** (EBV) | Site-specific SUMO | Suppresses lytic replication, enhances episome maintenance | [PMID: 40950008](https://pubmed.ncbi.nlm.nih.gov/40950008/) |

The Smad4 finding is direct: "the PIAS family proteins, PIAS1 and PIASx beta, function as E3 ligase factors for Smad4" ([PMID: 14514699](https://pubmed.ncbi.nlm.nih.gov/14514699/)). The HMGN2 study identified that "PIAS1 is the E3 ligase responsible for SUMOylation of HMGN2" ([PMID: 24872413](https://pubmed.ncbi.nlm.nih.gov/24872413/)). And the mGluR8b work shows canonical-site specificity: "SUMO1 conjugation of Lys882, present in a bona fide consensus sequence for SUMOylation (VKSE) in the mGluR8b C-terminus, was enhanced by addition of Pias1" ([PMID: 21288202](https://pubmed.ncbi.nlm.nih.gov/21288202/)). Substrate selection is governed by the combined action of PIAS1's SAP (DNA/chromatin), PINIT (substrate), SP-RING (Ubc9) and SIM (SUMO) modules; while many target lysines lie in the ΨKxE consensus, non-consensus sites also occur.

### 10. PIAS1 SUMOylates PPARγ to restrain NF-κB-driven inflammation

A mechanistically important substrate is **PPARγ**, which links PIAS1's catalytic and anti-inflammatory functions. Xie et al. "identified PIAS1 as a specific E3 ligase for PPARγ SUMOylation" ([PMID: 30419807](https://pubmed.ncbi.nlm.nih.gov/30419807/)). In myocardial ischemia-reperfusion models, PIAS1 falls after injury; "PIAS1 deficiency aggravated apoptosis and inflammation of cardiomyocytes via activating the NF-κB pathway after I/R," whereas PIAS1 overexpression ameliorates injury by promoting PPARγ SUMOylation and repressing NF-κB ([PMID: 30419807](https://pubmed.ncbi.nlm.nih.gov/30419807/)). Independently, "knockdown of protein inhibitor of activated STAT1 (PIAS1), an indispensable small ubiquitin-like modifier (SUMO) ligase, abrogated the effects of RGL on antagonizing LPS-induced IL-8/MCP-1 overexpression and NCoR degradation" ([PMID: 24260304](https://pubmed.ncbi.nlm.nih.gov/24260304/)). Thus SUMOylation of PPARγ by PIAS1 stabilizes the NCoR corepressor complex on NF-κB target promoters, providing a *catalytic* route to NF-κB transrepression that complements the *direct* p65 DNA-binding blockade.

---

## Mechanistic Model / Interpretation

PIAS1 is best understood as a **bifunctional nuclear regulator** that integrates two distinct molecular activities operating on overlapping sets of transcription factors.

```
                         ┌─────────────────────────────────────────────┐
                         │                  PIAS1                       │
                         │  SAP ── PINIT ── SP-RING(MIZ) ── SIM1/SIM2   │
                         │  (DNA)  (substr)  (Ubc9~SUMO)   (SUMO bind)  │
                         └───────────────┬─────────────┬───────────────┘
                                         │             │
             ARM 1: SUMO E3 LIGASE       │             │   ARM 2: SUMO-INDEPENDENT
             (catalytic)                 │             │   PROMOTER GATEKEEPER
                                         │             │
      ┌──────────────────────────────────┘             └───────────────────────┐
      ▼                                                                         ▼
  Ubc9~SUMO1 ──► substrate-Lys (ΨKxE)                        Binds activated STAT1 dimer
   • Smad4-K159  → ↑ TGF-β transcription                      (via aa 392–541 ↔ STAT1 N-dom)
   • PPARγ       → ↑ NCoR retention → NF-κB transrepression   Binds NF-κB p65
   • HMGN2-K17/35→ ↓ nucleosome binding                            │
   • mGluR8b-K882                                                  ▼
   • EBNA1 (viral)→ ↓ lytic replication                   BLOCKS DNA binding at promoters
   • DSB sites   → recruit 53BP1/BRCA1/RNF168 (repair)     → selective repression of
   • PML-NBs/HSV-1 → SUMO1 deposition (antiviral)            IFN-inducible & NF-κB genes
                                                                   ▲
                                                                   │
                                            SWITCH: IKKα → PIAS1-Ser90-P
                                            (inflammation-induced; requires
                                             PIAS1 SUMO-ligase activity)
```

The two arms are mechanistically linked rather than fully independent. The clearest link is that **IKKα-mediated Ser90 phosphorylation**, which activates the direct promoter-blocking arm, *requires* PIAS1's own SUMO-ligase activity ([PMID: 17540171](https://pubmed.ncbi.nlm.nih.gov/17540171/)). A second link is seen with PPARγ: PIAS1's *catalytic* SUMOylation of PPARγ converges on the same endpoint (NF-κB repression) as its *direct* binding and blockade of p65. The net physiological effect is a coherent one—PIAS1 acts as a **brake on interferon/innate-immune and inflammatory transcriptional programs**, deployed dynamically when inflammatory signaling activates IKKα.

Spatially, PIAS1 performs all of these roles within the nucleus, and in at least two cases at defined subnuclear structures: **PML nuclear bodies** (antiviral SUMO deposition) and **chromatin DNA double-strand-break foci** (repair-factor assembly). Its SAP domain provides the DNA/chromatin-tethering capacity that targets it to these sites.

This model is consistent with PIAS1's documented physiological and disease relevance: loss of PIAS1 in knockout mice de-represses interferon and NF-κB genes, enhances antiviral immunity, and raises proinflammatory cytokines; in cancer contexts, PIAS1 acts as a target-selective AR coregulator in prostate and apocrine breast cancer cells.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|------|-----------------|--------------|
| [9724754](https://pubmed.ncbi.nlm.nih.gov/9724754/) | *Inhibition of Stat1-mediated gene activation by PIAS1* | Founding discovery: PIAS1 blocks STAT1 DNA binding |
| [10805787](https://pubmed.ncbi.nlm.nih.gov/10805787/) | *Distinct roles of N/C-terminal domains of PIAS1* | Maps STAT1-dimer-specific interaction (aa 392–541) |
| [12764129](https://pubmed.ncbi.nlm.nih.gov/12764129/) | *SUMO modification of STAT1...* | STAT1 inhibition is SUMO-independent |
| [15311277](https://pubmed.ncbi.nlm.nih.gov/15311277/) | *PIAS1 selectively inhibits interferon-inducible genes* | In vivo (KO mouse): blocks STAT1 promoter recruitment |
| [15657437](https://pubmed.ncbi.nlm.nih.gov/15657437/) | *Negative regulation of NF-κB signaling by PIAS1* | PIAS1 blocks p65 DNA binding; KO validation |
| [17540171](https://pubmed.ncbi.nlm.nih.gov/17540171/) | *IKKα-mediated phosphorylation of PIAS1* | Ser90-P switch; unifying promoter-blocking statement |
| [20016603](https://pubmed.ncbi.nlm.nih.gov/20016603/) | *PIAS1 and PIAS4 promote responses to DSBs* | SUMO at DSBs; SAP-domain recruitment; repair |
| [27099310](https://pubmed.ncbi.nlm.nih.gov/27099310/) | *PIAS1 is a constituent PML-NB protein* | Nuclear localization; antiviral SUMO deposition |
| [25552417](https://pubmed.ncbi.nlm.nih.gov/25552417/) | *PIAS1 as target-selective AR coregulator* | Chromatin-bound AR coregulator (ChIP-seq) |
| [26219822](https://pubmed.ncbi.nlm.nih.gov/26219822/) | *AR- and PIAS1-regulated genes in apocrine breast cancer* | PIAS1 AR coregulation; anti-apoptotic role |
| [32348746](https://pubmed.ncbi.nlm.nih.gov/32348746/) | *C-terminal SIM in PIAS proteins* | Ubc9-PIAS1-SUMO1 complex assembly mechanism |
| [14514699](https://pubmed.ncbi.nlm.nih.gov/14514699/) | *SUMO-1 modification of Smad4* | Smad4 as PIAS1 substrate (TGF-β) |
| [24872413](https://pubmed.ncbi.nlm.nih.gov/24872413/) | *HMGN2 SUMOylation by PIAS1* | Chromatin-protein substrate; Lys17/35 |
| [21288202](https://pubmed.ncbi.nlm.nih.gov/21288202/) | *SUMO E3 ligases in retina / mGluR8b* | Canonical VKSE-site substrate |
| [30419807](https://pubmed.ncbi.nlm.nih.gov/30419807/) | *PIAS1 protects against myocardial I/R* | PPARγ SUMOylation substrate; NF-κB restraint |
| [24260304](https://pubmed.ncbi.nlm.nih.gov/24260304/) | *SUMOylation of PPARγ by rosiglitazone* | PIAS1 required for PPARγ-NCoR-NF-κB axis |
| [42102412](https://pubmed.ncbi.nlm.nih.gov/42102412/) | *PIAS1 attenuates abdominal aortic aneurysm* | States core SUMO-E3-ligase function |
| [28330929](https://pubmed.ncbi.nlm.nih.gov/28330929/) | *Role of PIAS SUMO E3-ligases in cancer* | Review: PIAS as ligases/coregulators |
| [29848755](https://pubmed.ncbi.nlm.nih.gov/29848755/) | *p14ARF enhances IFN-γ response via PIAS1* | PIAS1 as STAT1 inhibitor; ARF-SUMO target |
| [34331975](https://pubmed.ncbi.nlm.nih.gov/34331975/) | *Grass carp PIAS1 inhibits innate immunity* | Ortholog: nuclear localization; STAT1 interaction |
| [40950008](https://pubmed.ncbi.nlm.nih.gov/40950008/) | *EBNA1 SUMOylation by PIAS1* | Viral substrate; suppresses lytic replication |

**Convergence of evidence.** The STAT1- and NF-κB-blocking functions are supported by concordant biochemical (EMSA, co-IP), structural-mapping, cell-based (ChIP), and whole-animal knockout data—an unusually complete chain of evidence for a mechanistic claim. The SUMO-ligase function is supported across multiple independent substrate studies and structural/biochemical characterization of the catalytic machinery. These two bodies of evidence are mutually reinforcing and point to a single bifunctional protein.

**Challenges / nuances.** Some disease-model studies (e.g., circPIAS1 in melanoma, [PMID: 39334380](https://pubmed.ncbi.nlm.nih.gov/39334380/)) describe PIAS-adjacent entities (a circRNA-encoded peptide) rather than canonical PIAS1 itself, and must be interpreted carefully. Context-dependence is real: PIAS1 can act as a repressor (STAT1/NF-κB) or an activator/enhancer (Smad4 SUMOylation enhancing TGF-β transcription; AR coregulation can be activating or repressive at different loci), so its net effect is substrate- and promoter-specific.

---

## Limitations and Knowledge Gaps

1. **No local experimental dataset.** This investigation was a literature- and database-driven functional annotation; no primary data were analyzed in-house. Conclusions rest entirely on published studies and their reported findings (p-values/effect sizes were not uniformly extractable from abstracts).

2. **Substrate consensus vs. real selectivity.** While many PIAS1 substrates carry ΨKxE consensus lysines, the determinants of *in vivo* substrate selectivity (why PIAS1 rather than PIAS2/3/4 modifies a given target) remain incompletely defined. The relative contributions of the SAP, PINIT, and SIM modules to selectivity for each substrate are not fully resolved.

3. **Catalytic vs. non-catalytic separation.** The clean separation between SUMO-ligase activity and direct STAT1/NF-κB DNA-binding blockade is well established for STAT1 ([PMID: 12764129](https://pubmed.ncbi.nlm.nih.gov/12764129/)), but the extent to which each arm dominates in different cell types and stimuli is not quantified. The dependence of Ser90 phosphorylation on PIAS1's own ligase activity ([PMID: 17540171](https://pubmed.ncbi.nlm.nih.gov/17540171/)) hints at crosstalk that is not fully mechanistically dissected.

4. **Structural detail.** No high-resolution structure of full-length human PIAS1 in complex with a substrate and Ubc9~SUMO was examined here. The geometry of substrate-lysine presentation to the E2~SUMO thioester is inferred from homology and partial constructs.

5. **Nucleolar/RH-II-Gu connection.** PIAS1's historical identity as a "Gu-binding protein"/RNA helicase II-binding protein ([PMID: 9631199](https://pubmed.ncbi.nlm.nih.gov/9631199/)) is not mechanistically integrated with its characterized SUMO-ligase/transcription functions and remains a loose end.

---

## Proposed Follow-up Experiments / Actions

1. **Domain-resolved substrate selectivity screen.** Use recombinant PIAS1 domain-deletion/point mutants (ΔSAP, ΔPINIT, SP-RING catalytic-dead, SIM1/SIM2 mutants) in parallel in vitro SUMOylation assays against a panel of substrates (Smad4, PPARγ, HMGN2, mGluR8b) to quantify each module's contribution to catalysis and selectivity.

2. **Separation-of-function cell/mouse models.** Engineer PIAS1 alleles that disable catalysis (SP-RING mutant) versus DNA-binding blockade (STAT1/p65-interaction mutant from the aa 392–541 region) to measure how each arm independently controls interferon and NF-κB gene programs genome-wide (RNA-seq + ChIP-seq).

3. **Ser90 phosphorylation dynamics.** Use phospho-specific antibodies and time-resolved ChIP to map how IKKα→Ser90-P recruits PIAS1 to specific promoters after TNF/LPS, and test whether a phosphomimetic (S90D) constitutively represses NF-κB targets.

4. **Structural determination.** Pursue cryo-EM or crystallography of the Ubc9–PIAS1–SUMO1–substrate quaternary complex to define the transfer geometry and validate the SIM2-dependent assembly model ([PMID: 32348746](https://pubmed.ncbi.nlm.nih.gov/32348746/)).

5. **PML-NB and DSB spatial proteomics.** Apply proximity labeling (TurboID) at PML-NBs and laser-induced DSBs to catalog the local PIAS1 interactome and SUMO substrates at each site, clarifying how the SAP domain targets PIAS1 spatially.

6. **Therapeutic targeting assessment.** Given PIAS1's role as an AR coregulator in prostate/apocrine breast cancer and as an immune brake, evaluate selective PIAS1 modulation (catalytic vs. protein-interaction inhibitors) for effects on tumor growth and anti-tumor immunity.

---

## Conclusion

PIAS1 (O75925) is a nuclear, bifunctional protein: a SUMO E3 ligase that conjugates SUMO1 to diverse nuclear substrates via its SP-RING/Ubc9 machinery, and a SUMO-independent transcriptional gatekeeper that binds activated STAT1 dimers and NF-κB p65 to block their promoter DNA binding. These activities converge to restrain interferon and inflammatory gene programs, are activated by IKKα-mediated Ser90 phosphorylation, and operate at defined nuclear sites including PML nuclear bodies and DNA double-strand breaks.


## Artifacts

- [OpenScientist final report](PIAS1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PIAS1-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:9724754
2. PMID:42102412
3. PMID:28330929
4. PMID:9631199
5. PMID:10727979
6. PMID:32348746
7. PMID:10805787
8. PMID:12764129
9. PMID:15311277
10. PMID:34331975
11. PMID:29848755
12. PMID:15657437
13. PMID:17540171
14. PMID:27099310
15. PMID:20016603
16. PMID:25552417
17. PMID:26219822
18. PMID:14514699
19. PMID:30419807
20. PMID:24260304
21. PMID:24872413
22. PMID:21288202
23. PMID:40950008
24. PMID:39334380