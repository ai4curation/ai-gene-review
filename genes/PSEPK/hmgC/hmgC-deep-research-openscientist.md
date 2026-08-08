---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T13:37:24.596096'
end_time: '2026-07-23T13:48:34.514246'
duration_seconds: 669.92
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: hmgC
  gene_symbol: hmgC
  uniprot_accession: Q88E49
  protein_description: 'SubName: Full=Maleylacetoacetate isomerase {ECO:0000313|EMBL:AAN70192.1};
    EC=5.2.1.2 {ECO:0000313|EMBL:AAN70192.1};'
  gene_info: Name=hmgC {ECO:0000313|EMBL:AAN70192.1}; OrderedLocusNames=PP_4619 {ECO:0000313|EMBL:AAN70192.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the GST superfamily. Zeta family.
  protein_domains: Glutathione-S-Trfase_C-like. (IPR010987); Glutathione-S-Trfase_C_sf.
    (IPR036282); Glutathione_S-Trfase. (IPR040079); Glutathione_S-Trfase_N. (IPR004045);
    GST_Zeta. (IPR005955)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 11
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: hmgC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: hmgC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88E49
- **Protein Description:** SubName: Full=Maleylacetoacetate isomerase {ECO:0000313|EMBL:AAN70192.1}; EC=5.2.1.2 {ECO:0000313|EMBL:AAN70192.1};
- **Gene Information:** Name=hmgC {ECO:0000313|EMBL:AAN70192.1}; OrderedLocusNames=PP_4619 {ECO:0000313|EMBL:AAN70192.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the GST superfamily. Zeta family.
- **Key Domains:** Glutathione-S-Trfase_C-like. (IPR010987); Glutathione-S-Trfase_C_sf. (IPR036282); Glutathione_S-Trfase. (IPR040079); Glutathione_S-Trfase_N. (IPR004045); GST_Zeta. (IPR005955)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "hmgC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'hmgC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **hmgC** (gene ID: hmgC, UniProt: Q88E49) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *hmgC* (Q88E49, PP_4619) in *Pseudomonas putida* KT2440

**Gene:** hmgC (OrderedLocusName PP_4619) · **UniProt:** Q88E49 · **EC:** 5.2.1.2
**Protein:** Maleylacetoacetate isomerase (MAAI / HmgC)
**Organism:** *Pseudomonas putida* strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440 (PSEPK)
**Family:** Glutathione S-transferase (GST) superfamily, Zeta class
**Domains:** GST N-terminal thioredoxin-like (IPR004045); GST C-terminal / C-terminal-like (IPR036282, IPR010987); GST_Zeta signature (IPR005955); Glutathione_S-Trfase (IPR040079)

---

## Summary

**hmgC** (UniProt **Q88E49**; ordered locus **PP_4619**) of *Pseudomonas putida* KT2440 encodes **maleylacetoacetate isomerase (MAAI; HmgC; EC 5.2.1.2)**, the third enzyme of the central **homogentisate ring-cleavage pathway**. Its primary function is the **glutathione-dependent *cis*→*trans* isomerization of 4-maleylacetoacetate to 4-fumarylacetoacetate** — the penultimate biochemical step that channels the carbon skeletons of aromatic amino acids into central metabolism. The enzyme belongs to the **Zeta class of the glutathione S-transferase superfamily** and is the bacterial counterpart of the well-characterized eukaryotic **GSTZ1/MAAI** enzyme. It uses reduced glutathione (GSH) as an **essential catalytic cofactor** that is regenerated each cycle rather than consumed.

In *P. putida*, HmgC operates within a defined, experimentally validated catabolic module. The aromatic substrates **L-phenylalanine, L-tyrosine, and 3-hydroxyphenylacetate** all converge on the intermediate **homogentisate**, which is processed by three enzymes encoded in a single operon: **homogentisate 1,2-dioxygenase (HmgA)** cleaves the aromatic ring; **HmgC** isomerizes the resulting maleylacetoacetate; and **fumarylacetoacetate hydrolase (HmgB)** hydrolyzes fumarylacetoacetate to **fumarate and acetoacetate**, which feed the TCA cycle and acetyl-CoA pool. The isomerization is obligatory, because only the *trans* (fumaryl) isomer is a substrate for HmgB — HmgC therefore gates flux through the pathway's terminal step.

The gene product is a **soluble, cytoplasmic** homodimeric enzyme, consistent both with its role in the cytosolic aromatic-catabolic pathway and with the predominantly cytosolic distribution documented for GSTZ/MAAI enzymes across species. The *hmgABC* genes form a single transcriptional unit that is de-repressed by homogentisate acting through the IclR-type repressor **HmgR**. All of the core conclusions — reaction, substrate, cofactor requirement, structural fold, subcellular location, and transcriptional regulation — are supported by a combination of direct experimental characterization in *P. putida* and detailed biochemical/structural work on the conserved GSTZ/MAAI family.

---

## Gene/Protein Identity Verification

The gene symbol, organism, family, and domains provided by UniProt are internally consistent and confirmed by primary literature:

- The symbol **hmgC** is used in *P. putida* precisely for **maleylacetoacetate isomerase**, one of the three enzymes of the homogentisate pathway (HmgA/B/C) ([PMID: 15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/)).
- **Maleylacetoacetate isomerase is identical to the Zeta-class GST (GSTZ1)** ([PMID: 16399379](https://pubmed.ncbi.nlm.nih.gov/16399379/); [PMID: 21303221](https://pubmed.ncbi.nlm.nih.gov/21303221/)), matching the UniProt "GST superfamily, Zeta family" assignment and the IPR005955 GST_Zeta domain.
- The EC number (**5.2.1.2**, a *cis-trans* isomerase) matches the reaction defined below.

No conflicting-gene ambiguity was encountered. Importantly, most *mechanistic and structural* studies of this enzyme were performed on the human/mammalian orthologue GSTZ1; the *pathway role and gene assignment* are established experimentally and directly in *P. putida*, while the strong family/domain conservation makes the mechanistic conclusions applicable to the bacterial enzyme by homology. The extensive human GSTZ1 disease literature (hepatocellular carcinoma, dichloroacetate pharmacology, NRF2/KEAP1 and Wnt signaling) describes the *ortholog's* biology and is **not** attributed to the bacterial protein here.

---

## Key Findings

### Finding 1 — HmgC (PP_4619) is the maleylacetoacetate isomerase of the homogentisate central catabolic pathway

The primary functional assignment of *hmgC* is firmly established by direct experimental characterization of the homogentisate pathway in *Pseudomonas putida*. This pathway is a **central catabolic route** that degrades three aromatic substrates — L-phenylalanine, L-tyrosine, and 3-hydroxyphenylacetate — that all funnel into the common intermediate **homogentisate (2,5-dihydroxyphenylacetate)**. Homogentisate is then processed by three enzymes acting in series, of which HmgC is the **maleylacetoacetate isomerase**.

As stated directly in the primary study of this pathway: *"Homogentisate is then catabolized by a central catabolic pathway that involves three enzymes, homogentisate dioxygenase (HmgA), fumarylacetoacetate hydrolase (HmgB), and maleylacetoacetate isomerase (HmgC), finally yielding fumarate and acetoacetate."* ([PMID: 15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/)). This single statement assigns the enzymatic identity of HmgC, places it relative to HmgA and HmgB, and defines the pathway's ultimate products. HmgC carries **EC 5.2.1.2**, the classification for maleylacetoacetate *cis*-*trans* isomerase.

The biological significance is that HmgC sits at a metabolic bottleneck. After the aromatic ring of homogentisate is oxidatively opened by HmgA to yield maleylacetoacetate (a *cis*-configured molecule), the downstream hydrolase HmgB requires the *trans* (fumaryl) isomer. HmgC provides the obligatory isomerization that connects these two reactions. Without HmgC activity, maleylacetoacetate cannot be productively hydrolyzed and flux through the pathway stalls — making HmgC essential for the complete degradation of aromatic amino acids by this route.

### Finding 2 — HmgC is a Zeta-class glutathione transferase (GSTZ1/MAAI family) catalyzing a glutathione-dependent isomerization

HmgC belongs to the **Zeta family of the glutathione S-transferase superfamily**, indicated by its domain architecture (IPR005955 GST_Zeta; IPR004045 GST N-terminal thioredoxin-like; IPR010987/IPR036282 GST C-terminal-like). In eukaryotes the equivalent enzyme is **GSTZ1**, which is biochemically **identical to maleylacetoacetate isomerase (MAAI)** — the two names denote the same protein. This family identity provides deep mechanistic insight into how HmgC works, because the eukaryotic orthologue has been studied in extensive structural and kinetic detail.

The hallmark reactions of the Zeta-class GST/MAAI family are twofold: *"GSTZ was found to catalyze the oxygenation of dichloroacetic acid (DCA) to glyoxylic acid and the cis-trans isomerization of maleylacetoacetate to fumarylacetoacetate"* ([PMID: 16399379](https://pubmed.ncbi.nlm.nih.gov/16399379/)). The second reaction — the **isomerization of maleylacetoacetate to fumarylacetoacetate** — is exactly the physiological reaction catalyzed by HmgC in *P. putida*. The first (dehalogenation of DCA) reflects the catalytic promiscuity of the active site and is medically important in the eukaryotic enzyme, but it is a xenobiotic side-reaction rather than the primary physiological function.

The structural basis was resolved by the **1.9 Å crystal structure of human MAAI in complex with glutathione**: *"Here we report the crystal structure of human MAAI at 1.9 A resolution in complex with glutathione and a sulfate ion which mimics substrate binding."* ([PMID: 11327815](https://pubmed.ncbi.nlm.nih.gov/11327815/)). This structure demonstrates the **canonical GST fold** — an N-terminal thioredoxin-like domain forming the glutathione "G-site" and a C-terminal all-α-helical domain forming the hydrophobic substrate "H-site." The title of that work — *"Crystal structure of maleylacetoacetate isomerase/glutathione transferase zeta reveals the molecular basis for its remarkable catalytic promiscuity"* — captures the central insight that one active-site architecture supports isomerization, oxygenation, dehalogenation, and peroxidation.

Critically, **glutathione functions as a cofactor, not a co-substrate, in the isomerization**: it is required for activity but is regenerated at the end of each catalytic cycle and is not net-consumed. Mechanistically, the GSH thiolate is thought to add reversibly to the maleyl double bond, converting it to a freely rotatable single bond, permit rotation, then be eliminated to yield the *trans* (fumaryl) product — a glutathione-mediated addition-rotation-elimination isomerization. Kinetic and mutagenesis studies of the family identify a reactive active-site cysteine (Cys16 in the human enzyme) as central to GSH binding and catalysis, and an active-site arginine (Arg42) as governing substrate access/product release ([PMID: 15173170](https://pubmed.ncbi.nlm.nih.gov/15173170/); [PMID: 11692075](https://pubmed.ncbi.nlm.nih.gov/11692075/)).

### Finding 3 — *hmgC* lies in the homogentisate-inducible *hmgABC* operon and its product acts in the cytoplasm

The *hmgC* gene is not an isolated cistron but part of a **co-regulated catabolic operon**. In *P. putida*, *"the hmgABC genes appear to form a single transcriptional unit"* ([PMID: 15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/)), meaning HmgA, HmgB, and HmgC are transcribed together and coordinately controlled — a logical arrangement for three enzymes acting sequentially on a shared intermediate.

Expression is under **substrate-inducible negative control**. The divergently transcribed regulatory gene *hmgR* encodes an **IclR-type transcriptional repressor**: *"hmgR encodes a specific repressor that controls the inducible expression of the divergently transcribed hmgABC catabolic genes, and homogentisate is the inducer molecule"* ([PMID: 15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/)). In the absence of substrate, HmgR binds a 17-bp palindromic operator in the divergent *Phmg* promoter and blocks transcription. When homogentisate accumulates, it binds HmgR, relieves repression, and switches on the pathway. This demand-driven logic ensures HmgC and its partner enzymes are produced only when substrate is present.

The gene product carries out its function in the **cytoplasm**. HmgC is a soluble homodimeric enzyme with no signal peptide or transmembrane segment, consistent with the intracellular, cytosolic nature of the homogentisate pathway. This cytosolic localization is further supported by the documented distribution of the orthologous GSTZ/MAAI enzyme: *"GSTZ1 is most abundant in rodent and human liver, with its concentration several fold higher in cytoplasm than in mitochondria"* ([PMID: 37742772](https://pubmed.ncbi.nlm.nih.gov/37742772/)). Across the family the enzyme is predominantly cytoplasmic, and there is no evidence for a distinct localization of the bacterial orthologue.

---

## Mechanistic Model / Interpretation

### The homogentisate pathway and HmgC's position within it

HmgC is the isomerase at the heart of the homogentisate central catabolic pathway. The pathway is a funnel: multiple aromatic substrates are converted (by peripheral pathways) into a single common intermediate, homogentisate, which is then ring-cleaved and processed to central-metabolism products.

```
   L-Phenylalanine    L-Tyrosine    3-Hydroxyphenylacetate
          \               |                /
           \              |               /
            +-------------+--------------+
                          |   (peripheral pathways: PhhAB, TyrB, Hpd ...)
                          v
                   HOMOGENTISATE  (2,5-dihydroxyphenylacetate)
                          |
                          |   HmgA  (homogentisate 1,2-dioxygenase)
                          |   ring cleavage; O2 incorporation
                          v
                  4-MALEYLACETOACETATE   (cis isomer)
                          |
                          |   >>> HmgC  (maleylacetoacetate isomerase, PP_4619) <<<
                          |   glutathione-dependent cis -> trans isomerization
                          |   EC 5.2.1.2 ; GSH = catalytic cofactor (not consumed)
                          v
                 4-FUMARYLACETOACETATE   (trans isomer)
                          |
                          |   HmgB  (fumarylacetoacetate hydrolase)
                          |   hydrolysis
                          v
                 FUMARATE  +  ACETOACETATE
                    |               |
              (TCA cycle)    (ketone body / acetyl-CoA)
```

**Table 1. The three enzymes of the *P. putida* homogentisate pathway.**

| Gene | Enzyme | Reaction | EC | Role relative to HmgC |
|------|--------|----------|----|-----------------------|
| *hmgA* | Homogentisate 1,2-dioxygenase | Homogentisate + O₂ → maleylacetoacetate | 1.13.11.5 | Acts **before** HmgC; produces its substrate |
| ***hmgC*** (PP_4619) | **Maleylacetoacetate isomerase** | Maleylacetoacetate → fumarylacetoacetate | **5.2.1.2** | **This gene** |
| *hmgB* | Fumarylacetoacetate hydrolase | Fumarylacetoacetate → fumarate + acetoacetate | 3.7.1.2 | Acts **after** HmgC; consumes its product |

### Why the isomerization step is required

HmgA opens the aromatic ring to generate maleylacetoacetate, in which the newly formed backbone is in the *cis* (maleyl) configuration. The downstream hydrolase HmgB is specific for the *trans* (fumaryl) isomer. HmgC bridges this stereochemical mismatch. Because *cis*→*trans* isomerization across a C=C double bond is thermodynamically favorable but kinetically slow, the cell employs a glutathione-based catalytic strategy: the GSH thiolate adds reversibly to the double bond, rotation occurs, and GSH is eliminated to release the *trans* product. This chemistry is why the enzyme is a member of the GST superfamily even though its physiological reaction is an isomerization rather than a conjugation.

### Regulatory logic

```
   No aromatic substrate                Aromatic substrate present
   ---------------------                ---------------------------
   HmgR (IclR repressor)                Homogentisate binds HmgR
   bound to Phmg operator      --->     Repressor released
   hmgABC transcription OFF             hmgABC transcription ON
                                        HmgA + HmgC + HmgB produced
```

This demand-driven induction means HmgC is synthesized specifically under conditions where its substrate is being generated — an efficient allocation of biosynthetic resources.

### Evolutionary and functional context

Bacterial HmgC and eukaryotic GSTZ1/MAAI are orthologues performing the identical physiological reaction — the penultimate step of tyrosine/phenylalanine catabolism. This deep conservation from bacteria to humans underscores the fundamental importance of the homogentisate pathway. In eukaryotes, loss of GSTZ1/MAAI makes phenylalanine toxic and leads to accumulation of tyrosine intermediates ([PMID: 21303221](https://pubmed.ncbi.nlm.nih.gov/21303221/)), and the enzyme additionally metabolizes the drug dichloroacetate. While the human disease literature does not describe the *P. putida* protein, it provides robust, transferable insight into the **catalytic mechanism, glutathione dependence, fold, and substrate chemistry** of the conserved MAAI reaction that HmgC performs.

---

## Evidence Base

**Table 2. Key literature and how each source supports the annotation of HmgC.**

| PMID | Focus | Contribution to this annotation |
|------|-------|--------------------------------|
| [15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/) | Homogentisate pathway in *P. putida* | **Primary, direct evidence.** Assigns HmgC as maleylacetoacetate isomerase; defines substrates (L-Phe, L-Tyr, 3-hydroxyphenylacetate) and products (fumarate, acetoacetate); establishes the *hmgABC* operon and HmgR/homogentisate regulation. |
| [11327815](https://pubmed.ncbi.nlm.nih.gov/11327815/) | Crystal structure of MAAI/GSTZ | Establishes the canonical GST fold, glutathione binding, and the structural basis of the isomerase reaction and catalytic promiscuity for the family. |
| [16399379](https://pubmed.ncbi.nlm.nih.gov/16399379/) | Human glutathione transferase zeta | Defines the two hallmark GSTZ/MAAI reactions (MAA→FAA isomerization; DCA→glyoxylate), confirming the primary isomerase function and substrate. |
| [37742772](https://pubmed.ncbi.nlm.nih.gov/37742772/) | Clinical physiology/pharmacology of GSTZ1/MAAI | Supports predominantly cytosolic localization of the MAAI/GSTZ family enzyme. |
| [21303221](https://pubmed.ncbi.nlm.nih.gov/21303221/) | Discovery, catalysis, and *Gstz1⁻/⁻* mice | Confirms the identity GSTZ1 = MAAI, the GSH-dependent chemistry, and that loss of the enzyme makes phenylalanine toxic — underscoring the pathway role. |
| [15173170](https://pubmed.ncbi.nlm.nih.gov/15173170/) | Binding/kinetic mechanism of Zeta-class GST | Details GSH binding and the catalytic role of active-site Cys16 in the family. |
| [11692075](https://pubmed.ncbi.nlm.nih.gov/11692075/) | GSTZ1d allele; MAAI catalysis | Confirms Zeta-class GSTs isomerize maleylacetoacetate to fumarylacetoacetate and maps active-site residues (e.g., Arg42) affecting catalysis. |

### A note on citation scope

The human GSTZ1 papers concerning **hepatocellular carcinoma, DCA pharmacokinetics, NRF2/KEAP1 signaling, ferroptosis, and Wnt/β-catenin regulation** (e.g., [PMID: 31782257](https://pubmed.ncbi.nlm.nih.gov/31782257/), [PMID: 31666108](https://pubmed.ncbi.nlm.nih.gov/31666108/), [PMID: 33931597](https://pubmed.ncbi.nlm.nih.gov/33931597/), [PMID: 35562974](https://pubmed.ncbi.nlm.nih.gov/35562974/)) describe **human disease biology of the orthologue** and are **not** claims about the *P. putida* protein. They are noted only to document the conserved enzymatic identity (GSTZ1 = MAAI) and catalytic chemistry, which transfer to HmgC by orthology. The core functional annotation of HmgC rests on the direct *P. putida* study ([PMID: 15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/)) plus structural/mechanistic work on the conserved family.

---

## Supported and Refuted Hypotheses

**Supported:**

- **H1 — hmgC = maleylacetoacetate isomerase, the third enzyme of the homogentisate pathway.** Supported by direct experimental evidence in *P. putida* ([PMID: 15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/)).
- **H2 — The enzyme is a Zeta-class GST that uses glutathione as a catalytic cofactor for a *cis-trans* isomerization.** Supported by family identity, biochemistry, and structure ([PMID: 16399379](https://pubmed.ncbi.nlm.nih.gov/16399379/); [PMID: 11327815](https://pubmed.ncbi.nlm.nih.gov/11327815/)).
- **H3 — The product is soluble/cytoplasmic and co-regulated with hmgA/hmgB via homogentisate-responsive HmgR.** Supported ([PMID: 15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/); [PMID: 37742772](https://pubmed.ncbi.nlm.nih.gov/37742772/)).

**Refuted / not supported:**

- The gene is **not** a transporter, structural protein, or signaling molecule; no evidence supports such roles. Broad pleiotropic and disease-biomarker associations reported for the human orthologue GSTZ1 (cancer metabolism, DCA pharmacology) are not part of the bacterial enzyme's primary catabolic function and are excluded as off-target to this annotation.

---

## Limitations and Knowledge Gaps

1. **No dedicated biochemical study of the *P. putida* HmgC protein itself.** The assignment rests on (a) direct genetic/pathway characterization in *P. putida* ([PMID: 15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/)) and (b) enzymology of the conserved eukaryotic orthologue. No purified-enzyme kinetic characterization (kcat, Km for maleylacetoacetate, GSH dependence) for Q88E49/PP_4619 was located; kinetic parameters are inferred, not measured, for this exact protein.

2. **No experimental structure of HmgC.** The GST fold, glutathione-binding mode, and catalytic residues (reactive Cys, active-site Arg) are inferred from the human MAAI crystal structure ([PMID: 11327815](https://pubmed.ncbi.nlm.nih.gov/11327815/)) and InterPro domain assignments rather than confirmed in the bacterial enzyme.

3. **UniProt annotation provenance.** The EC number and enzyme name in the Q88E49 record carry an ECO:0000313 (imported/automatic from EMBL) evidence code, indicating derivation from sequence/database inference rather than direct assay of this protein — though this is strongly corroborated by the independent experimental pathway study in the same organism.

4. **Substrate-specificity breadth is unquantified for HmgC.** The eukaryotic enzyme is catalytically promiscuous (isomerase, dehalogenase, peroxidase). Whether the *P. putida* enzyme retains side activities (e.g., toward α-haloacids such as DCA) has not been tested; only the physiological isomerase reaction is documented.

5. **Regulatory fine detail.** While the *hmgABC* operon and HmgR-mediated homogentisate induction are established, operator occupancy, HmgR–homogentisate binding affinity, and possible global inputs (e.g., carbon catabolite control) for *hmgC* specifically were not examined.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant enzyme characterization.** Overexpress and purify PP_4619 (His-tagged) and measure steady-state kinetics of the maleylacetoacetate → fumarylacetoacetate isomerization (using maleylacetone as a convenient surrogate substrate, as done for human GSTZ1), quantifying kcat, Km, and the absolute glutathione requirement — converting orthology-based inference into direct evidence for the bacterial protein.

2. **Structural determination / prediction validation.** Solve a crystal structure or analyze an AlphaFold model of HmgC, superpose it on human MAAI ([PMID: 11327815](https://pubmed.ncbi.nlm.nih.gov/11327815/)), and confirm conservation of the G-site GSH-binding residues, the catalytic cysteine, and the H-site geometry accommodating the acetoacetate moiety.

3. **Gene knockout / complementation.** Construct a *P. putida* KT2440 Δ*hmgC* mutant and test growth on L-tyrosine, L-phenylalanine, and 3-hydroxyphenylacetate as sole carbon sources. Predicted outcome: a growth defect (and accumulation of maleylacetoacetate/pigmented homogentisate-derived products) rescued by plasmid-borne *hmgC*, directly demonstrating physiological essentiality.

4. **Metabolite profiling.** Use LC-MS to detect accumulation of maleylacetoacetate (and homogentisate autoxidation pigments) in the Δ*hmgC* strain versus wild type upon aromatic-substrate feeding, confirming the metabolic block occurs at the isomerization step.

5. **Promoter/regulation assay.** Fuse the *Phmg* promoter to a reporter and confirm homogentisate-dependent, HmgR-mediated induction of *hmgABC*, quantifying induction ratio and testing which aromatic intermediates act as inducers.

6. **Substrate-promiscuity screen.** Test whether purified HmgC dehalogenates dichloroacetate to glyoxylate (the diagnostic GSTZ side reaction), establishing the degree of functional conservation with the eukaryotic enzyme and any potential utility in bioremediation of haloacid pollutants.

---

## Conclusion

The evidence robustly supports annotation of **hmgC (Q88E49, PP_4619)** as **maleylacetoacetate isomerase (EC 5.2.1.2)**, a soluble cytoplasmic **Zeta-class glutathione S-transferase** that catalyzes the **glutathione-dependent *cis*→*trans* isomerization of maleylacetoacetate to fumarylacetoacetate**. It is the third enzyme of the *P. putida* homogentisate central catabolic pathway, acting between the ring-cleaving dioxygenase HmgA and the hydrolase HmgB, thereby enabling complete degradation of L-phenylalanine, L-tyrosine, and 3-hydroxyphenylacetate to fumarate and acetoacetate. Its gene is co-transcribed in the homogentisate-inducible *hmgABC* operon under IclR-type (HmgR) repressor control. This assignment is anchored by direct experimental study of the pathway in *P. putida* and reinforced by extensive structural and mechanistic characterization of the conserved GSTZ1/MAAI orthologues.


## Artifacts

- [OpenScientist final report](hmgC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](hmgC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:15262943
2. PMID:16399379
3. PMID:21303221
4. PMID:11327815
5. PMID:15173170
6. PMID:11692075
7. PMID:37742772
8. PMID:31782257
9. PMID:31666108
10. PMID:33931597
11. PMID:35562974