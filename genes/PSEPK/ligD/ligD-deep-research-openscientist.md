---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T16:05:18.513278'
end_time: '2026-09-01T16:20:23.864778'
duration_seconds: 905.35
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ligD
  gene_symbol: ligD
  uniprot_accession: Q88HU3
  protein_description: 'RecName: Full=DNA ligase (ATP) {ECO:0000256|ARBA:ARBA00012727};
    EC=6.5.1.1 {ECO:0000256|ARBA:ARBA00012727}; AltName: Full=NHEJ DNA polymerase
    {ECO:0000256|ARBA:ARBA00029943};'
  gene_info: Name=ligD {ECO:0000313|EMBL:AAN68867.1}; OrderedLocusNames=PP_3260 {ECO:0000313|EMBL:AAN68867.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: DNA_ligase_ATP-dep_C. (IPR012309); DNA_ligase_ATP-dep_cent. (IPR012310);
    LigD_ligase_dom. (IPR014146); LigD_PE_domain. (IPR014144); LigD_pol_dom. (IPR014145)
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
  path: ligD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ligD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88HU3
- **Protein Description:** RecName: Full=DNA ligase (ATP) {ECO:0000256|ARBA:ARBA00012727}; EC=6.5.1.1 {ECO:0000256|ARBA:ARBA00012727}; AltName: Full=NHEJ DNA polymerase {ECO:0000256|ARBA:ARBA00029943};
- **Gene Information:** Name=ligD {ECO:0000313|EMBL:AAN68867.1}; OrderedLocusNames=PP_3260 {ECO:0000313|EMBL:AAN68867.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** DNA_ligase_ATP-dep_C. (IPR012309); DNA_ligase_ATP-dep_cent. (IPR012310); LigD_ligase_dom. (IPR014146); LigD_PE_domain. (IPR014144); LigD_pol_dom. (IPR014145)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ligD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ligD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ligD** (gene ID: ligD, UniProt: Q88HU3) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: LigD (Q88HU3, PP_3260) — *Pseudomonas putida* KT2440

## Gene/Protein Identity Verification

The gene symbol **ligD** is **unambiguous** and correctly matches the UniProt description for the target.

- **UniProt:** Q88HU3 — "DNA ligase (ATP)" (EC 6.5.1.1); AltName "NHEJ DNA polymerase"
- **Gene:** *ligD*; ordered locus **PP_3260**; organism *Pseudomonas putida* KT2440 (taxid 160488)
- **Length:** 833 aa (verified from UniProt sequence, Iteration 2)
- **Domains (InterPro):** LigD_PE_domain (IPR014144), LigD_ligase_dom (IPR014146), DNA_ligase_ATP-dep central/C (IPR012310/IPR012309), LigD_pol_dom (IPR014145)

All identifiers, the enzyme class, the domain complement, and the organism are internally consistent and match the well-characterized bacterial NHEJ **DNA ligase D** family. A study performed directly in *P. putida* (Paris et al., 2015, PMID 25942369) explicitly describes the LigD/Ku NHEJ system in this organism, and the cognate Ku gene is present in the same genome (PP_3255; see below). There is **no evidence of gene-symbol ambiguity** — this is the canonical bacterial NHEJ multifunctional ligase, not an unrelated same-symbol gene.

---

## 1. Summary (Answer to the Research Question)

**LigD is the central, multifunctional, ATP-dependent DNA ligase of the bacterial non-homologous end-joining (NHEJ) pathway.** Its primary function is to repair chromosomal DNA **double-strand breaks (DSBs)** without a homologous template, acting as the enzymatic "workhorse" downstream of the DNA-end-binding protein **Ku**. LigD is a single polypeptide carrying **three autonomous catalytic modules** that together perform every chemical step of end-joining: a **3'-phosphoesterase (PE)** domain that heals damaged 3' ends to a ligatable 3'-OH; an **ATP-dependent ligase (LIG)** domain that seals the phosphodiester backbone via a covalent ligase–AMP intermediate; and a **primase/polymerase (POL)** domain that fills gaps and adds (ribo)nucleotides across the break. The enzyme functions in the **cytoplasm on nucleoid (chromosomal) DNA**, and is physiologically most important in **non-replicating / stationary-phase / starved cells**, where homologous recombination is unavailable. NHEJ by Ku–LigD is intrinsically **error-prone**, so LigD also contributes to stress-associated (stationary-phase) mutagenesis in *P. putida*.

---

## 2. Primary Function: Reaction Catalyzed and Substrate Specificity

### 2.1 Overall pathway function
Bacterial NHEJ is a minimal **two-component system**: the homodimeric end-binding protein **Ku** plus the polyfunctional ligase **LigD** possess all the break-recognition, end-processing and ligation activities needed to rejoin a DSB (Gong et al., 2005, PMID 15778718; Pitcher, Brissett & Doherty, 2007, PMID 17506672; Amare et al., 2021, PMID 34901162). Ku binds and synapses the two broken ends and recruits/stimulates LigD, which then processes and seals the junction (Amare et al., 2021, PMID 34901162; Zhu & Shuman, 2010, PMID 20018881).

### 2.2 Domain architecture (bioinformatically verified for Q88HU3)
InterPro/Pfam mapping of the 833-aa Q88HU3 sequence gives an unambiguous N→C module order, matching the experimentally characterized *Pseudomonas aeruginosa* LigD:

| Module | Approx. residues | InterPro / Pfam | Catalytic role |
|--------|------------------|-----------------|----------------|
| **PE** (3'-phosphoesterase) | ~5–160 | IPR014144 / PF13298 | End-healing: generate 3'-OH |
| **LIG** (ATP-dependent ligase) | ~219–520 (central IPR012310/PF01068 + OB-fold C-term IPR012309/PF04679) | IPR014146 | Nick sealing |
| **POL** (primase-polymerase) | ~547–812 (PaeLigD-type IPR033651) | IPR014145 / PF21686 | Gap fill / nucleotide addition |

The POL module is explicitly of the **PaeLigD-type** subclass, i.e., the same structural class as the crystallized *P. aeruginosa* POL domain, allowing high-confidence transfer of the *P. aeruginosa* biochemistry to the *P. putida* ortholog (Iteration 2 analysis).

### 2.3 POL domain — gap-filling primase/polymerase
- **Fold/mechanism:** The 1.5-Å crystal structure of the *Pseudomonas* LigD POL domain reveals a **minimized two-metal polymerase with a fold similar to archaeal DNA primase** (archaeo-eukaryotic primase, AEP superfamily) (Zhu et al., 2006, PMID 16446439).
- **Activity/specificity:** Performs **templated and nontemplated primer extension**, is **Mn²⁺-dependent**, and shows a **preference for adding ribonucleotides to blunt DNA ends** (Zhu et al., 2006, PMID 16446439; Pitcher et al., 2006, PMID 17174332).
- **Substrate recognition:** Efficient **gap filling** requires a **5'-phosphate** on the distal strand of the gap, conferring apparent processivity; residues His-553, Arg-556, Lys-566 mediate 5'-PO₄ recognition and Phe-603 stacks on the templating base (Zhu & Shuman, 2010, PMID 20018881). A 5'-phosphate at the single-/double-strand junction is a principal signal for specific POL binding to NHEJ intermediates (Pitcher et al., 2006, PMID 17174332).
- **Physiological consequence:** POL is the **direct catalyst of mutagenic (nontemplated single-nucleotide) additions** during NHEJ in vivo (Zhu et al., 2006, PMID 16446439).

### 2.4 PE domain — 3'-end healing
The N-terminal PE module catalyzes **Mn-dependent 3'-phosphodiesterase and 3'-phosphomonoesterase** reactions at the primer-strand 3' end (Zhu & Shuman, 2006, PMID 16540477). It acts as a **3'-exoribonuclease** that resects a 3'-terminal diribonucleotide to a ribonucleoside-3'-PO₄ (strictly requiring the 2'-OH of the penultimate ribose), and its phosphomonoesterase then **converts a 3'-PO₄ (ribo- or deoxyribo-) to a ligatable 3'-OH** (Zhu & Shuman, 2006, PMID 16540477). This "heals" damaged ends and removes the ribonucleotides deposited by POL, coordinating the processing→sealing hand-off.

### 2.5 LIG domain — nick sealing (EC 6.5.1.1)
The ligase module is an **ATP-dependent DNA ligase** that performs the final sealing step. The structure of the LigD ligase domain was captured as the **covalent ligase–AMP (adenylylated-enzyme) intermediate** with a divalent metal in the active site (Akey et al., 2006, PMID 16476729), consistent with canonical two-step ligase chemistry: (i) enzyme adenylylation using ATP, (ii) AMP transfer to the DNA 5'-phosphate, (iii) phosphodiester bond formation joining 3'-OH and 5'-PO₄. Its activity is dynamically balanced against end-remodeling, which underlies NHEJ's error-prone signature (Akey et al., 2006, PMID 16476729).

**Net reaction (EC 6.5.1.1):** ATP + (5'-phospho-DNA)ₙ + (3'-hydroxy-DNA)ₘ → AMP + diphosphate + ligated DNA — carried out at DSB junctions after PE/POL end-processing.

---

## 3. Subcellular Localization

LigD is a **soluble cytoplasmic enzyme** that acts on **chromosomal (nucleoid) DNA**. There is no signal peptide, transmembrane region, or secretion signal; the protein's substrate is intracellular double-stranded DNA. Functionally it is recruited to double-strand breaks in the bacterial chromosome, where Ku first binds the DNA ends and delivers LigD (Amare et al., 2021, PMID 34901162; Zhu & Shuman, 2010, PMID 20018881). Genetic work in *P. putida* demonstrates its action on the resident chromosome under starvation (Paris et al., 2015, PMID 25942369).

---

## 4. Biological Process and Physiological Context

- **When it matters:** NHEJ is "a critical repair mechanism when DNA is not replicating" (Amare et al., 2021, PMID 34901162). It is especially important during **quiescent/stationary states** (late stationary phase, starvation, sporulation in spore-formers) when no sister chromosome is available for homologous recombination (Paris et al., 2015, PMID 25942369).
- **In *P. putida* specifically:** Genetic evidence shows **LigD and Ku participate in stationary-phase mutagenesis** in carbon-starved *P. putida*; deleting *ligD* or *ku* yields distinct mutation spectra, and **both the PE and POL domains** of LigD contribute to the mutational outcomes (Paris et al., 2015, PMID 25942369).
- **Fidelity:** NHEJ is intrinsically **mutagenic** — repair of blunt and 5'-overhang DSBs proceeds with ~50% error rate, driven by templated fill-in, nontemplated single-nucleotide additions, and nucleolytic resection (Gong et al., 2005, PMID 15778718). Genetic dissection shows POL activity mainly promotes infidelity, while efficient repair depends on the Ku protein and the LigD POL **domain** (as a structural bridging element) more than on its polymerase catalytic activity per se (Aniukwu, Glickman & Shuman, 2008, PMID 18281464).
- **Genomic context:** The cognate **Ku** (Q88HU8, gene *ku*, **PP_3255**, 273 aa) is encoded within five ORFs of *ligD* (PP_3260), confirming a complete, self-standing two-component NHEJ apparatus in KT2440 (Iteration 2 UniProt analysis).

---

## 5. Evidence Basis

- **Direct experimental (in-organism):** Genetic knockouts and mutation-spectrum analysis in *P. putida* (Paris et al., 2015, PMID 25942369).
- **Biochemical/structural (Pseudomonas orthologs, directly transferable):** Crystal structure and enzymology of the *Pseudomonas* POL domain (Zhu et al., 2006, PMID 16446439; Zhu & Shuman, 2010, PMID 20018881); PE-domain enzymology (Zhu & Shuman, 2006, PMID 16540477).
- **Structural (family):** LigD ligase-domain structure (Akey et al., 2006, PMID 16476729); *M. tuberculosis* PolDom structure (Pitcher et al., 2006, PMID 17174332); in-vivo domain contributions (Aniukwu et al., 2008, PMID 18281464); founding genetics of bacterial NHEJ (Gong et al., 2005, PMID 15778718).
- **Reviews:** Pitcher, Brissett & Doherty, 2007 (PMID 17506672); Amare et al., 2021 (PMID 34901162).
- **Bioinformatic/sequence:** UniProt Q88HU3 (833 aa) and InterPro/Pfam domain mapping confirming the PE–LIG–POL, PaeLigD-type architecture (this study, Iteration 2).

---

## 6. Supported and Refuted Hypotheses

**Supported:**
1. LigD is the multifunctional ATP-dependent DNA ligase of bacterial NHEJ (EC 6.5.1.1). ✔
2. It contains three separable catalytic modules (PE, LIG, POL) in N→C order PE–LIG–POL. ✔ (bioinformatically confirmed for Q88HU3)
3. POL is an AEP/primase-fold, Mn-dependent, ribonucleotide-preferring gap-filling polymerase that senses 5'-phosphate. ✔
4. PE is a 3'-phosphoesterase/exoribonuclease generating 3'-OH ends. ✔
5. It acts in the cytoplasm on chromosomal DNA, primarily in non-replicating/starved cells, and contributes to error-prone stationary-phase mutagenesis in *P. putida*. ✔
6. A cognate Ku partner is genomically encoded (PP_3255) — complete two-component system. ✔

**Refuted / not supported:**
- The gene-symbol-ambiguity concern is **refuted** — *ligD* unambiguously denotes the NHEJ ligase for this accession/organism.

---

## 7. Limitations and Future Directions

- Most **atomic/enzymatic** data derive from *P. aeruginosa* and *M. tuberculosis* LigD; while domain identity (PaeLigD-type) makes transfer to *P. putida* robust, KT2440-specific in-vitro kinetics and a full-length structure are not yet reported.
- No experimental wild-type full-length LigD structure exists for any species; domain arrangement in the intact protein relies on individual-domain structures and AlphaFold predictions (Amare et al., 2021, PMID 34901162).
- The precise contribution of LigD to survival after specific DSB-inducing stresses (e.g., desiccation, ionizing radiation, quinolone antibiotics) in *P. putida* has not been exhaustively quantified and is a promising direction.
- Whether LigD/Ku influence horizontal gene transfer or plasmid capture via end-joining in *P. putida* remains open.

---

*Report generated across Iterations 1–3. Citations reference PubMed IDs of the primary literature and reviews surveyed.*


## Artifacts

- [OpenScientist final report](ligD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ligD-deep-research-openscientist_artifacts/final_report.pdf)