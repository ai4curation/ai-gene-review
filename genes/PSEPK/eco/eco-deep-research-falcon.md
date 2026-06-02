---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-01T08:45:21.184573'
end_time: '2026-06-01T08:54:27.960776'
duration_seconds: 546.78
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: eco
  gene_symbol: eco
  uniprot_accession: Q88IC7
  protein_description: 'RecName: Full=Ecotin {ECO:0000255|HAMAP-Rule:MF_00706}; Flags:
    Precursor;'
  gene_info: Name=eco {ECO:0000255|HAMAP-Rule:MF_00706}; OrderedLocusNames=PP_3072;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the protease inhibitor I11 (ecotin) family.
  protein_domains: Ecotin_C. (IPR027438); Ecotin_sf. (IPR036198); Prot_inh_ecotin.
    (IPR005658); Prot_inh_ecotin_gammaproteobac. (IPR023084); Ecotin (PF03974)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 33
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: eco-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88IC7
- **Protein Description:** RecName: Full=Ecotin {ECO:0000255|HAMAP-Rule:MF_00706}; Flags: Precursor;
- **Gene Information:** Name=eco {ECO:0000255|HAMAP-Rule:MF_00706}; OrderedLocusNames=PP_3072;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the protease inhibitor I11 (ecotin) family.
- **Key Domains:** Ecotin_C. (IPR027438); Ecotin_sf. (IPR036198); Prot_inh_ecotin. (IPR005658); Prot_inh_ecotin_gammaproteobac. (IPR023084); Ecotin (PF03974)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "eco" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'eco' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **eco** (gene ID: eco, UniProt: Q88IC7) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88IC7
- **Protein Description:** RecName: Full=Ecotin {ECO:0000255|HAMAP-Rule:MF_00706}; Flags: Precursor;
- **Gene Information:** Name=eco {ECO:0000255|HAMAP-Rule:MF_00706}; OrderedLocusNames=PP_3072;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the protease inhibitor I11 (ecotin) family.
- **Key Domains:** Ecotin_C. (IPR027438); Ecotin_sf. (IPR036198); Prot_inh_ecotin. (IPR005658); Prot_inh_ecotin_gammaproteobac. (IPR023084); Ecotin (PF03974)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "eco" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'eco' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **eco** (gene ID: eco, UniProt: Q88IC7) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Research report: **eco** (ecotin) — UniProt **Q88IC7** (*Pseudomonas putida* KT2440; locus **PP_3072**)

### Executive summary
The target gene **eco** (UniProt Q88IC7) in *Pseudomonas putida* KT2440 is annotated as **ecotin**, a member of the **MEROPS inhibitor family I11**, best understood as a **periplasmic, signal-peptide-directed, broad-spectrum inhibitor of trypsin-fold (S1A) serine proteases** that protects Gram-negative bacteria from **exogenous proteolytic attack**. Direct experimental work on ecotin exists primarily in *E. coli* and *Pseudomonas aeruginosa*; in the retrieved literature, *P. putida* is explicitly reported to encode ecotin at the species level, but **strain KT2440 / PP_3072 / Q88IC7 is not directly studied**. Therefore, this functional annotation for Q88IC7 is supported primarily by (i) UniProt-provided identity plus (ii) strong family-level mechanistic conservation and (iii) Pseudomonas/ecotin literature, while **KT2440-specific pathways, regulation, and phenotypes remain evidence gaps**. (eggers2004theperiplasmicserine pages 4-4, meyer2023ecotinaversatile pages 1-2, eggers2004theperiplasmicserine pages 1-2)

### 1) Gene/protein identification and verification (critical disambiguation)
**Verified target context.** The symbol **eco** can be ambiguous across organisms, but the UniProt record provided specifies *P. putida* KT2440 protein **Q88IC7** with description “Ecotin; precursor,” and membership in the **ecotin (I11) protease inhibitor family**.

**Independent literature concordance.** Ecotin is explicitly described in the literature as a **periplasmic serine protease inhibitor** with a **signal peptide** and typical ecotin properties (dimeric inhibitor; broad S1A inhibition), which matches the UniProt description and domain family context. (meyer2023ecotinaversatile pages 1-2, eggers2004theperiplasmicserine pages 1-2, eggers2004theperiplasmicserine pages 4-6)

**Organism check.** Eggers et al. report that within the genus **Pseudomonas**, ecotin is present in **Pseudomonas aeruginosa, Pseudomonas putida, and Pseudomonas fluorescens** (and absent from *P. syringae* pv. tomato DC3000). This supports that ecotin-family proteins occur in *Pseudomonas putida* and is consistent with the UniProt-provided KT2440 assignment, although it does not resolve the KT2440 locus tag in that paper. (eggers2004theperiplasmicserine pages 4-4)

### 2) Key concepts and definitions (current understanding)
#### 2.1 What is ecotin?
Ecotin is a bacterial (and more broadly microbial) **serine protease inhibitor** originally described in *E. coli* and classified as **MEROPS family I11**. It is notable for **broad inhibitory specificity** compared with many protease inhibitors that are narrow-spectrum. (meyer2023ecotinaversatile pages 1-2, kantyka2010prokaryotederivedproteininhibitors pages 14-15)

#### 2.2 Mechanism: dimeric inhibitor with two binding sites and 2:2 stoichiometry
A defining mechanistic concept is that ecotin forms a **contralateral dimer**, and this dimer binds **two protease molecules** to form a **2:2 heterotetrameric complex**; each ecotin monomer contributes a **primary and secondary binding interface** that together underlie tight binding and broad specificity. (meyer2023ecotinaversatile pages 1-2, kantyka2010prokaryotederivedproteininhibitors pages 14-15)

#### 2.3 Structural basis of broad specificity
Sequence/structure analyses emphasize ecotin’s **surface loops** that contact target proteases, including a substrate-like **“80s loop”** with a key **P1 residue** that varies among species and helps tune specificity. In addition, loop/backbone flexibility is implicated in accommodating different protease active sites (e.g., movement of 50s/80s loops in comparisons of ecotin–protease complexes). (eggers2004theperiplasmicserine pages 4-6, eggers2004theperiplasmicserine pages 10-10)

### 3) Primary function, targets, and substrate specificity
Ecotin’s **primary function** is inhibition of **trypsin-fold serine proteases** (S1A) rather than catalysis; thus “substrate specificity” for annotation purposes is best described as **target-protease range**.

#### 3.1 Host/animal protease targets (well-supported)
Across ecotin orthologs, inhibition has been shown for a range of mammalian serine proteases, including **trypsin, chymotrypsin, elastase**, and (in reviews) additional targets such as **cathepsin G**. (eggers2004theperiplasmicserine pages 1-2, meyer2023ecotinaversatile pages 1-2)

A central experimentally supported “defense” target is **human neutrophil elastase (NE)**, a potent antimicrobial protease. Eggers et al. demonstrate that ecotin protects bacteria from NE-driven killing and propose a periplasmic protection mechanism (below). (eggers2004theperiplasmicserine pages 1-2, eggers2004theperiplasmicserine pages 10-10)

#### 3.2 Complement lectin pathway targets (immune evasion concept)
Beyond direct elastase inhibition, ecotin orthologs can inhibit complement-related serine proteases. Nagy et al. report ecotin orthologs (including from *P. aeruginosa*) inhibit **MASP-1 and MASP-2** (lectin pathway activators) and also inhibit **MASP-3**, which activates factor D in resting blood, thereby modulating lectin (and at higher concentrations alternative) pathway activity. (nagy2019ecotinamicrobial pages 1-2)

A 2023 review further summarizes MASP inhibition and reports **Ki values in the ~10−5 to 10−9 M range** (depending on ecotin ortholog and target), supporting that ecotin can act as a complement-pathway protease inhibitor in host-associated contexts. (meyer2023ecotinaversatile pages 3-4)

### 4) Cellular localization and where the protein functions
#### 4.1 Core localization: periplasm (best-supported for ecotin family; applied to Q88IC7)
Ecotin is described as a **periplasmic** inhibitor and is associated with a **signal peptide** for export to the periplasm, consistent with the “precursor” concept in UniProt-style annotations. (meyer2023ecotinaversatile pages 1-2, eggers2004theperiplasmicserine pages 1-2)

#### 4.2 A Pseudomonas-specific extension: extracellular biofilm matrix association (shown in *P. aeruginosa*)
While ecotin is classically periplasmic, *Pseudomonas aeruginosa* provides a key real-world implementation of ecotin function outside the periplasm: Tseng et al. show ecotin (PA2755) is enriched in the **biofilm extracellular matrix**, accumulates in mature biofilms, and **binds the exopolysaccharide Psl**. Matrix-bound ecotin retains activity, inhibiting neutrophil elastase and protecting biofilm cells. (tseng2018abiofilmmatrixassociated pages 2-3, tseng2018abiofilmmatrixassociated pages 4-5, tseng2018abiofilmmatrixassociated pages 6-8)

A 2024 review (biofilm matrix as a catalytic environment) reiterates this mechanism and highlights that ecotin lacks canonical secretion signals, proposing that extracellular appearance may occur via **release from lysed cells during biofilm development** and subsequent retention by matrix components such as Psl. (goltermann2024microbialprimerthe pages 3-4)

**Implication for Q88IC7:** no KT2440-specific extracellular/matrix evidence was retrieved, but given genus-level conservation, ecotin in *P. putida* could plausibly contribute to extracellular/biofilm-associated defense under certain conditions; this remains **hypothesis-level** without direct KT2440 data. (goltermann2024microbialprimerthe pages 3-4, tseng2018abiofilmmatrixassociated pages 2-3)

### 5) Pathways and biological processes
Ecotin is not a metabolic enzyme in a canonical pathway; rather it participates in a **cell-envelope defense process** against exogenous proteases, which can be framed as an interface of:

1. **Envelope stress / damage context:** Exogenous proteases damage outer membrane proteins, increasing permeability.
2. **Periplasmic neutralization:** Ecotin inhibits proteases that enter the periplasm.

Eggers et al. articulate a model wherein neutrophil elastase cleaves outer membrane proteins (e.g., OmpA), increases permeability, and then translocates into the periplasm where it impairs growth/repair; ecotin inhibits this periplasmic protease activity, improving recovery. (eggers2004theperiplasmicserine pages 10-10)

In host-associated settings, complement inhibition (via MASP targets) provides an additional immune-evasion pathway-level concept, though direct *P. putida* involvement is untested in the retrieved set. (nagy2019ecotinamicrobial pages 1-2, meyer2023ecotinaversatile pages 3-4)

### 6) Recent developments (prioritizing 2023–2024)
#### 6.1 2023 dedicated review: updated “ecotin biology” synthesis
De Meyer & Carlier (Frontiers in Microbiology, **Jan 2023**) provide an updated synthesis emphasizing (i) ecotin’s **periplasmic localization** and broad inhibitory spectrum, (ii) the **2:2 binding mode** and structural basis of broad specificity, (iii) its frequent occurrence in host-associated bacteria but presence also in environmental taxa, and (iv) emerging roles in host–microbe interactions, including complement protease inhibition and biofilm-associated phenomena reported for *P. aeruginosa*. https://doi.org/10.3389/fmicb.2023.1114690 (meyer2023ecotinaversatile pages 1-2, meyer2023ecotinaversatile pages 3-4)

#### 6.2 2024 biofilm-matrix review: ecotin as a matrix-retained active factor
Goltermann et al. (Microbiology, **Aug 2024**) highlight ecotin as an example of a **matrix-associated** factor that retains biochemical activity in the biofilm matrix by binding **Psl**, inhibiting neutrophil elastase and protecting matrix components/cells; they also discuss the unresolved question of how ecotin becomes extracellular (cell lysis vs nonclassical secretion). https://doi.org/10.1099/mic.0.001497 (goltermann2024microbialprimerthe pages 3-4)

### 7) Current applications and real-world implementations
#### 7.1 Biofilm-associated immune evasion (real infection-relevant implementation in *P. aeruginosa*)
A clear “real-world” implementation is ecotin’s contribution to **biofilm tolerance against host proteases** in *P. aeruginosa*. Tseng et al. provide a mechanistic example where ecotin is retained in biofilm matrix via Psl and can inhibit neutrophil elastase, protecting both biofilm cells and matrix proteins from proteolytic attack. https://doi.org/10.1128/mBio.00543-18 (tseng2018abiofilmmatrixassociated pages 2-3, tseng2018abiofilmmatrixassociated pages 6-8)

Although this is not *P. putida*, it is a close genus-level implementation demonstrating that ecotin can function beyond the periplasm in pseudomonads.

#### 7.2 Therapeutic/biotech relevance (ecotin as an inhibitor scaffold; broader field)
Prokaryote-derived protease inhibitor reviews note ecotin’s unusual binding architecture and describe its use in **protein engineering and specificity reprogramming** efforts (e.g., mutagenesis/phage display selection to alter specificity), supporting interest in ecotin as a scaffold. (kantyka2010prokaryotederivedproteininhibitors pages 14-15)

### 8) Quantitative data and statistics (from recent and authoritative sources)
#### 8.1 Inhibition potency ranges (ortholog-dependent)
Eggers et al. report that ecotin orthologs can potently inhibit **trypsin and chymotrypsin at <10 pM**, while inhibition of blood proteases is much more variable (**5 pM to 24 μM** across tested combinations). https://doi.org/10.1042/BJ20031790 (eggers2004theperiplasmicserine pages 1-2)

For **neutrophil elastase**, Eggers et al. report *P. aeruginosa* ecotin as among the tightest inhibitors tested, with **Ki < 5 pM**. (eggers2004theperiplasmicserine pages 10-10)

#### 8.2 Matrix-bound ecotin activity and concentrations (*P. aeruginosa*)
In a cell-free matrix assay, Tseng et al. report that immunoprecipitated matrix containing ecotin inhibited neutrophil elastase activity by **52.1% ± 10.2%** and that the matrix preparation contained approximately **16.5 ± 3.2 nM** ecotin, while **100 nM** elastase was used. https://doi.org/10.1128/mBio.00543-18 (tseng2018abiofilmmatrixassociated pages 5-6)

#### 8.3 Phenotypic protection (planktonic survival; *P. aeruginosa*)
Tseng et al. quantify elastase-mediated killing in planktonic culture: wild type decreased by **0.93 ± 0.14 log10 CFU/mL**, Δeco decreased **2.47 ± 0.25 log10 CFU/mL**, and a complemented strain decreased **1.48 ± 0.47 log10 CFU/mL** after elastase exposure. (tseng2018abiofilmmatrixassociated pages 5-6)

#### 8.4 Distribution statistics across taxa
Nagy et al. describe ecotin as distributed among many microbes, stating ecotin is “identified in **more than 200 species**” and that “**more than three hundred species** express at least one ecotin homolog” (in their figure caption), with reported tallies across phyla/classes in the excerpt (e.g., Proteobacteria **158 species**, Bacteroidetes **40 species**). https://doi.org/10.1371/journal.ppat.1008232 (nagy2019ecotinamicrobial pages 17-19)

A 2023 review similarly emphasizes broad distribution and notes ecotin homologs are widespread, particularly among Gammaproteobacteria, including non-pathogenic Pseudomonas such as *P. fluorescens* and *P. protegens*. https://doi.org/10.3389/fmicb.2023.1114690 (meyer2023ecotinaversatile pages 2-3)

### 9) Expert opinions and analysis (authoritative synthesis)
A consistent expert-level interpretation across reviews and primary work is that ecotin’s biological role is most parsimoniously explained as a **defensive inhibitor** against **external proteases** encountered in host-associated or protease-rich environments; however, its presence in environmental genera such as **Pseudomonas** motivates hypotheses of additional ecological roles (e.g., interbacterial interactions, predation defense, or biofilm matrix protection), many of which remain incompletely resolved. (eggers2004theperiplasmicserine pages 4-4, meyer2023ecotinaversatile pages 1-2)

For pseudomonads specifically, ecotin’s integration into the biofilm matrix via **specific polymer binding (Psl)** provides a concrete mechanistic route by which a periplasmic inhibitor can become an extracellularly acting protective factor in multicellular communities. (tseng2018abiofilmmatrixassociated pages 2-3, goltermann2024microbialprimerthe pages 3-4)

### 10) What is known specifically for *Pseudomonas putida* KT2440 eco (Q88IC7/PP_3072)?
**Direct KT2440 experimental evidence not found in retrieved texts.** No retrieved primary paper directly characterizes **PP_3072 / Q88IC7** expression, localization, or phenotypes in KT2440.

**Species-level presence is supported.** *P. putida* is explicitly named as an ecotin-containing species in Eggers et al., supporting that *P. putida* encodes an ecotin ortholog. (eggers2004theperiplasmicserine pages 4-4)

**Most defensible KT2440 functional annotation (based on best evidence):**
- **Molecular function:** ecotin-family **serine protease inhibitor** (MEROPS I11), likely broad-spectrum against trypsin-fold serine proteases. (meyer2023ecotinaversatile pages 1-2, kantyka2010prokaryotederivedproteininhibitors pages 14-15)
- **Localization:** likely **periplasmic** (signal peptide; “precursor”). (meyer2023ecotinaversatile pages 1-2, eggers2004theperiplasmicserine pages 1-2)
- **Biological process:** defense against **exogenous proteases**; plausible roles in protecting envelope integrity and possibly biofilm communities (hypothesis based on *P. aeruginosa*). (eggers2004theperiplasmicserine pages 10-10, tseng2018abiofilmmatrixassociated pages 2-3)

### Summary evidence table
| Claim/Annotation item | What it means for Q88IC7 (KT2440) | Evidence type (primary experimental / review / inference) | Key supporting citations with publication year and URL | Quantitative data (if any) |
|---|---|---|---|---|
| Gene/protein identity and family | Q88IC7/PP_3072 is the **ecotin-family protease inhibitor I11** protein annotated as **eco** in *Pseudomonas putida* KT2440. Because the literature retrieved did not explicitly mention PP_3072 or Q88IC7, the KT2440 assignment relies on the provided UniProt record, while the functional identity is supported by species-level reports that *P. putida* contains ecotin and by strong family-level concordance with known ecotins. | Inference anchored to species-level literature + review/background evidence | Eggers et al., 2004, *Biochemical Journal*, https://doi.org/10.1042/BJ20031790; De Meyer & Carlier, 2023, *Frontiers in Microbiology*, https://doi.org/10.3389/fmicb.2023.1114690 (eggers2004theperiplasmicserine pages 4-4, meyer2023ecotinaversatile pages 1-2) | None specific for KT2440 in retrieved papers |
| Localization: signal peptide / periplasm | The most likely core localization of Q88IC7 is the **periplasm**, consistent with ecotin being synthesized with an N-terminal signal peptide and functioning as a periplasmic inhibitor that protects the cell envelope from exogenous serine proteases. This matches the UniProt “precursor” designation. | Primary experimental + review; applied to KT2440 by inference | Eggers et al., 2004, https://doi.org/10.1042/BJ20031790; De Meyer & Carlier, 2023, https://doi.org/10.3389/fmicb.2023.1114690 (eggers2004theperiplasmicserine pages 1-2, eggers2004theperiplasmicserine pages 4-6, meyer2023ecotinaversatile pages 1-2) | Ecotin described as ~16 kDa subunits; signal peptide ~20 aa in review |
| Localization: extracellular matrix in Pseudomonas biofilms | No KT2440-specific extracellular localization data were retrieved. However, in the related pseudomonad *P. aeruginosa*, ecotin can accumulate in the **extracellular biofilm matrix** by binding the exopolysaccharide **Psl**; this suggests a plausible but unproven extracellular role for Q88IC7 under some conditions. | Primary experimental in *P. aeruginosa*; inference for KT2440 | Tseng et al., 2018, *mBio*, https://doi.org/10.1128/mBio.00543-18; Goltermann et al., 2024, *Microbiology*, https://doi.org/10.1099/mic.0.001497 (tseng2018abiofilmmatrixassociated pages 2-3, tseng2018abiofilmmatrixassociated pages 4-5, tseng2018abiofilmmatrixassociated pages 1-2, goltermann2024microbialprimerthe pages 3-4) | Matrix-associated ecotin inhibited elastase by **52.1% ± 10.2%**; matrix prep contained **~16.5 ± 3.2 nM** ecotin vs **100 nM** elastase |
| Molecular function | Q88IC7 is best annotated as a **broad-spectrum serine protease inhibitor** of the **ecotin/I11 family**, acting mainly against **trypsin-fold (S1A) serine proteases**. Its primary biological role is protection from **external proteolytic attack**, not catalysis. | Primary experimental + review; applied to KT2440 by inference | Kantyka et al., 2010, https://doi.org/10.1016/j.biochi.2010.06.004; Eggers et al., 2004, https://doi.org/10.1042/BJ20031790; De Meyer & Carlier, 2023, https://doi.org/10.3389/fmicb.2023.1114690 (kantyka2010prokaryotederivedproteininhibitors pages 14-15, eggers2004theperiplasmicserine pages 1-2, meyer2023ecotinaversatile pages 1-2) | Digestive proteases can be inhibited at **<10 pM** in tested ecotins |
| Mechanism: oligomeric state and binding architecture | Q88IC7 is expected to function as a **homodimer** that forms a **2:2 ecotin:protease heterotetramer**. Each monomer contributes **primary and secondary binding sites**, a hallmark of ecotin’s broad specificity and tight binding. | Primary structural/biochemical + review; inference for KT2440 | Kantyka et al., 2010, https://doi.org/10.1016/j.biochi.2010.06.004; De Meyer & Carlier, 2023, https://doi.org/10.3389/fmicb.2023.1114690 (kantyka2010prokaryotederivedproteininhibitors pages 14-15, meyer2023ecotinaversatile pages 1-2) | Stoichiometry **2:2** |
| Mechanism: loop flexibility and specificity determinants | Q88IC7 likely uses conserved ecotin surface loops, including the **80s loop** with the key **P1 residue**, to adapt to different protease active sites. Flexibility in the 50s/80s loops is central to broad substrate recognition. | Primary structural/biochemical + review; inference for KT2440 | Eggers et al., 2004, https://doi.org/10.1042/BJ20031790; Jobichen et al., 2020, *Biochemistry*, https://doi.org/10.1021/acs.biochem.0c00493 (eggers2004theperiplasmicserine pages 4-6, eggers2004theperiplasmicserine pages 10-10) | Ecotin is **142 aa** long in cited analysis; 80s and 50s loop movement reported at **4.6 Å** in structural comparison |
| Mechanism: periplasmic protection model | The most likely biological model for Q88IC7 is that exogenous proteases such as **neutrophil elastase (NE)** damage outer-membrane components, gain access to the periplasm, and are then neutralized by ecotin, improving survival and recovery. | Primary experimental; inference for KT2440 | Eggers et al., 2004, https://doi.org/10.1042/BJ20031790 (eggers2004theperiplasmicserine pages 1-2, eggers2004theperiplasmicserine pages 10-10) | NE killing assays used **3.4 µM** NE in one experimental setup |
| Substrates/targets: neutrophil elastase (NE) | Q88IC7 most plausibly inhibits **NE**, one of the best-supported ecotin targets in pseudomonads and other Gram-negative bacteria. This is likely among the most biologically relevant targets when bacteria encounter host innate immunity. | Primary experimental + review; inference for KT2440 | Eggers et al., 2004, https://doi.org/10.1042/BJ20031790; Tseng et al., 2018, https://doi.org/10.1128/mBio.00543-18; De Meyer & Carlier, 2023, https://doi.org/10.3389/fmicb.2023.1114690 (eggers2004theperiplasmicserine pages 1-2, eggers2004theperiplasmicserine pages 10-10, tseng2018abiofilmmatrixassociated pages 5-6, tseng2018abiofilmmatrixassociated pages 1-2, meyer2023ecotinaversatile pages 3-4) | *P. aeruginosa* ecotin NE **Ki <5 pM** |
| Substrates/targets: trypsin and chymotrypsin | Q88IC7 is expected to inhibit **trypsin** and **chymotrypsin**, canonical ecotin targets and part of the original biochemical definition of ecotin activity. | Primary experimental + review; inference for KT2440 | Eggers et al., 2004, https://doi.org/10.1042/BJ20031790; De Meyer & Carlier, 2023, https://doi.org/10.3389/fmicb.2023.1114690 (eggers2004theperiplasmicserine pages 1-2, meyer2023ecotinaversatile pages 1-2) | Potent inhibition of pancreatic digestive proteases at **<10 pM** |
| Substrates/targets: CatG and other trypsin-fold proteases | Q88IC7 may also inhibit **cathepsin G (CatG)** and additional trypsin-fold host proteases, although potency varies by ecotin ortholog. | Primary experimental + review; inference for KT2440 | Eggers et al., 2004, https://doi.org/10.1042/BJ20031790; De Meyer & Carlier, 2023, https://doi.org/10.3389/fmicb.2023.1114690 (eggers2004theperiplasmicserine pages 4-6, meyer2023ecotinaversatile pages 1-2) | Broad blood-protease inhibition range reported from **5 pM to 24 µM** across orthologs |
| Substrates/targets: complement MASPs | Q88IC7 may plausibly inhibit **MASP-1, MASP-2, and MASP-3**, based on ecotin ortholog data from *E. coli*, *Y. pestis*, and *P. aeruginosa*. This suggests a potential role in resisting complement-dependent host defenses, but it has not been directly shown for KT2440 Q88IC7. | Primary experimental in other orthologs + review; inference for KT2440 | Nagy et al., 2019, *PLOS Pathogens*, https://doi.org/10.1371/journal.ppat.1008232; De Meyer & Carlier, 2023, https://doi.org/10.3389/fmicb.2023.1114690 (nagy2019ecotinamicrobial pages 1-2, meyer2023ecotinaversatile pages 3-4) | MASP inhibitory **Ki range ~10^-5 to 10^-9 M** reported in 2023 review |
| Quantitative inhibition / assay values most relevant to annotation | The strongest quantitative guidance for Q88IC7 annotation comes from orthologs: very tight inhibition of digestive proteases, picomolar NE inhibition in *P. aeruginosa*, and partial yet significant elastase inhibition when matrix-bound in biofilms. | Primary experimental + review | Eggers et al., 2004, https://doi.org/10.1042/BJ20031790; Tseng et al., 2018, https://doi.org/10.1128/mBio.00543-18; De Meyer & Carlier, 2023, https://doi.org/10.3389/fmicb.2023.1114690 (eggers2004theperiplasmicserine pages 1-2, eggers2004theperiplasmicserine pages 10-10, tseng2018abiofilmmatrixassociated pages 5-6, meyer2023ecotinaversatile pages 3-4) | **<10 pM** for digestive proteases; *P. aeruginosa* NE **Ki <5 pM**; matrix-bound ecotin **52.1% ± 10.2%** elastase inhibition; **16.5 ± 3.2 nM** ecotin in matrix prep |
| Phenotypic protection data from Pseudomonas | No KT2440 phenotype data were retrieved. In *P. aeruginosa*, ecotin protects both planktonic and biofilm cells from elastase-mediated killing, supporting the general annotation of ecotin as a defensive inhibitor in pseudomonads. | Primary experimental in related species; inference for KT2440 | Tseng et al., 2018, https://doi.org/10.1128/mBio.00543-18 (tseng2018abiofilmmatrixassociated pages 5-6, tseng2018abiofilmmatrixassociated pages 6-8) | Planktonic viability loss after elastase: WT **0.93 ± 0.14 log10 CFU/ml**, Δeco **2.47 ± 0.25 log10 CFU/ml**, complemented **1.48 ± 0.47 log10 CFU/ml** |
| Distribution across taxa and Pseudomonas | Ecotin is not unique to enteric pathogens; it is distributed broadly across bacteria and is explicitly reported in **Pseudomonas putida**, **P. aeruginosa**, and **P. fluorescens**. This supports the plausibility of an ecotin-based protective role in environmental pseudomonads such as KT2440. | Primary survey + review | Eggers et al., 2004, https://doi.org/10.1042/BJ20031790; Nagy et al., 2019, https://doi.org/10.1371/journal.ppat.1008232; De Meyer & Carlier, 2023, https://doi.org/10.3389/fmicb.2023.1114690 (eggers2004theperiplasmicserine pages 4-4, nagy2019ecotinamicrobial pages 17-19, meyer2023ecotinaversatile pages 2-3) | Species counts reported as **>200** and **>300** ecotin-containing species in different sources; one review notes **>600 homologs** overall |
| Current confidence / limitation for KT2440-specific annotation | The **primary function** of Q88IC7 can be annotated with moderate confidence as an **ecotin-family periplasmic serine protease inhibitor** protecting against exogenous serine proteases. However, **KT2440-specific substrates, phenotypes, regulation, and extracellular roles remain unverified** in the retrieved literature. | Evidence synthesis / inference | Supported collectively by ecotin literature and species-level *P. putida* presence reports (eggers2004theperiplasmicserine pages 4-4, eggers2004theperiplasmicserine pages 1-2, meyer2023ecotinaversatile pages 1-2) | No direct KT2440 quantitative measurements retrieved |


*Table: This table summarizes the available functional annotation evidence for ecotin encoded by eco (UniProt Q88IC7; PP_3072) in Pseudomonas putida KT2440. It separates direct evidence from inference and highlights where KT2440-specific data are still lacking.*

### References (URLs and publication dates)
- Eggers CT et al. **Apr 2004**. *The Biochemical Journal*. “The periplasmic serine protease inhibitor ecotin protects bacteria against neutrophil elastase.” https://doi.org/10.1042/BJ20031790 (eggers2004theperiplasmicserine pages 1-2, eggers2004theperiplasmicserine pages 4-4)
- Kantyka T et al. **Nov 2010**. *Biochimie*. “Prokaryote-derived protein inhibitors of peptidases: A sketchy occurrence and mostly unknown function.” https://doi.org/10.1016/j.biochi.2010.06.004 (kantyka2010prokaryotederivedproteininhibitors pages 14-15)
- Nagy ZA et al. **Dec 2019**. *PLOS Pathogens*. “Ecotin… blocks multiple complement dependent and independent microbicidal activities of human serum.” https://doi.org/10.1371/journal.ppat.1008232 (nagy2019ecotinamicrobial pages 1-2, nagy2019ecotinamicrobial pages 17-19)
- Jobichen C et al. **Jul 2020**. *Biochemistry*. “Structural basis for the inhibition mechanism of ecotin against neutrophil elastase…” https://doi.org/10.1021/acs.biochem.0c00493 (eggers2004theperiplasmicserine pages 10-10)
- De Meyer FD, Carlier A. **Jan 2023**. *Frontiers in Microbiology*. “Ecotin: A versatile protease inhibitor of bacteria and eukaryotes.” https://doi.org/10.3389/fmicb.2023.1114690 (meyer2023ecotinaversatile pages 1-2, meyer2023ecotinaversatile pages 3-4, meyer2023ecotinaversatile pages 2-3)
- Tseng BS et al. **May 2018**. *mBio*. “A biofilm matrix-associated protease inhibitor protects Pseudomonas aeruginosa from proteolytic attack.” https://doi.org/10.1128/mBio.00543-18 (tseng2018abiofilmmatrixassociated pages 2-3, tseng2018abiofilmmatrixassociated pages 5-6)
- Goltermann L et al. **Aug 2024**. *Microbiology*. “Microbial primer: The catalytic biofilm matrix.” https://doi.org/10.1099/mic.0.001497 (goltermann2024microbialprimerthe pages 3-4)


References

1. (eggers2004theperiplasmicserine pages 4-4): Christopher T. EGGERS, Iain A. MURRAY, Valerie A. DELMAR, Anthony G. DAY, and Charles S. CRAIK. The periplasmic serine protease inhibitor ecotin protects bacteria against neutrophil elastase. The Biochemical journal, 379 Pt 1:107-18, Apr 2004. URL: https://doi.org/10.1042/bj20031790, doi:10.1042/bj20031790. This article has 134 citations.

2. (meyer2023ecotinaversatile pages 1-2): Frédéric De Meyer and Aurélien Carlier. Ecotin: a versatile protease inhibitor of bacteria and eukaryotes. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2023.1114690, doi:10.3389/fmicb.2023.1114690. This article has 7 citations and is from a peer-reviewed journal.

3. (eggers2004theperiplasmicserine pages 1-2): Christopher T. EGGERS, Iain A. MURRAY, Valerie A. DELMAR, Anthony G. DAY, and Charles S. CRAIK. The periplasmic serine protease inhibitor ecotin protects bacteria against neutrophil elastase. The Biochemical journal, 379 Pt 1:107-18, Apr 2004. URL: https://doi.org/10.1042/bj20031790, doi:10.1042/bj20031790. This article has 134 citations.

4. (eggers2004theperiplasmicserine pages 4-6): Christopher T. EGGERS, Iain A. MURRAY, Valerie A. DELMAR, Anthony G. DAY, and Charles S. CRAIK. The periplasmic serine protease inhibitor ecotin protects bacteria against neutrophil elastase. The Biochemical journal, 379 Pt 1:107-18, Apr 2004. URL: https://doi.org/10.1042/bj20031790, doi:10.1042/bj20031790. This article has 134 citations.

5. (kantyka2010prokaryotederivedproteininhibitors pages 14-15): Tomasz Kantyka, Neil D. Rawlings, and Jan Potempa. Prokaryote-derived protein inhibitors of peptidases: a sketchy occurrence and mostly unknown function. Biochimie, 92 11:1644-56, Nov 2010. URL: https://doi.org/10.1016/j.biochi.2010.06.004, doi:10.1016/j.biochi.2010.06.004. This article has 64 citations and is from a peer-reviewed journal.

6. (eggers2004theperiplasmicserine pages 10-10): Christopher T. EGGERS, Iain A. MURRAY, Valerie A. DELMAR, Anthony G. DAY, and Charles S. CRAIK. The periplasmic serine protease inhibitor ecotin protects bacteria against neutrophil elastase. The Biochemical journal, 379 Pt 1:107-18, Apr 2004. URL: https://doi.org/10.1042/bj20031790, doi:10.1042/bj20031790. This article has 134 citations.

7. (nagy2019ecotinamicrobial pages 1-2): Zoltán Attila Nagy, Dávid Szakács, Eszter Boros, Dávid Héja, Eszter Vígh, Noémi Sándor, Mihály Józsi, Gábor Oroszlán, József Dobó, Péter Gál, and Gábor Pál. Ecotin, a microbial inhibitor of serine proteases, blocks multiple complement dependent and independent microbicidal activities of human serum. PLOS Pathogens, 15:e1008232, Dec 2019. URL: https://doi.org/10.1371/journal.ppat.1008232, doi:10.1371/journal.ppat.1008232. This article has 44 citations and is from a highest quality peer-reviewed journal.

8. (meyer2023ecotinaversatile pages 3-4): Frédéric De Meyer and Aurélien Carlier. Ecotin: a versatile protease inhibitor of bacteria and eukaryotes. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2023.1114690, doi:10.3389/fmicb.2023.1114690. This article has 7 citations and is from a peer-reviewed journal.

9. (tseng2018abiofilmmatrixassociated pages 2-3): Boo Shan Tseng, Courtney Reichhardt, Gennifer E. Merrihew, Sophia A. Araujo-Hernandez, Joe J. Harrison, Michael J. MacCoss, and Matthew R. Parsek. A biofilm matrix-associated protease inhibitor protects pseudomonas aeruginosa from proteolytic attack. mBio, May 2018. URL: https://doi.org/10.1128/mbio.00543-18, doi:10.1128/mbio.00543-18. This article has 85 citations and is from a domain leading peer-reviewed journal.

10. (tseng2018abiofilmmatrixassociated pages 4-5): Boo Shan Tseng, Courtney Reichhardt, Gennifer E. Merrihew, Sophia A. Araujo-Hernandez, Joe J. Harrison, Michael J. MacCoss, and Matthew R. Parsek. A biofilm matrix-associated protease inhibitor protects pseudomonas aeruginosa from proteolytic attack. mBio, May 2018. URL: https://doi.org/10.1128/mbio.00543-18, doi:10.1128/mbio.00543-18. This article has 85 citations and is from a domain leading peer-reviewed journal.

11. (tseng2018abiofilmmatrixassociated pages 6-8): Boo Shan Tseng, Courtney Reichhardt, Gennifer E. Merrihew, Sophia A. Araujo-Hernandez, Joe J. Harrison, Michael J. MacCoss, and Matthew R. Parsek. A biofilm matrix-associated protease inhibitor protects pseudomonas aeruginosa from proteolytic attack. mBio, May 2018. URL: https://doi.org/10.1128/mbio.00543-18, doi:10.1128/mbio.00543-18. This article has 85 citations and is from a domain leading peer-reviewed journal.

12. (goltermann2024microbialprimerthe pages 3-4): Lise Goltermann, Shahab Shahryari, Morten Rybtke, and Tim Tolker-Nielsen. Microbial primer: the catalytic biofilm matrix. Aug 2024. URL: https://doi.org/10.1099/mic.0.001497, doi:10.1099/mic.0.001497. This article has 8 citations and is from a peer-reviewed journal.

13. (tseng2018abiofilmmatrixassociated pages 5-6): Boo Shan Tseng, Courtney Reichhardt, Gennifer E. Merrihew, Sophia A. Araujo-Hernandez, Joe J. Harrison, Michael J. MacCoss, and Matthew R. Parsek. A biofilm matrix-associated protease inhibitor protects pseudomonas aeruginosa from proteolytic attack. mBio, May 2018. URL: https://doi.org/10.1128/mbio.00543-18, doi:10.1128/mbio.00543-18. This article has 85 citations and is from a domain leading peer-reviewed journal.

14. (nagy2019ecotinamicrobial pages 17-19): Zoltán Attila Nagy, Dávid Szakács, Eszter Boros, Dávid Héja, Eszter Vígh, Noémi Sándor, Mihály Józsi, Gábor Oroszlán, József Dobó, Péter Gál, and Gábor Pál. Ecotin, a microbial inhibitor of serine proteases, blocks multiple complement dependent and independent microbicidal activities of human serum. PLOS Pathogens, 15:e1008232, Dec 2019. URL: https://doi.org/10.1371/journal.ppat.1008232, doi:10.1371/journal.ppat.1008232. This article has 44 citations and is from a highest quality peer-reviewed journal.

15. (meyer2023ecotinaversatile pages 2-3): Frédéric De Meyer and Aurélien Carlier. Ecotin: a versatile protease inhibitor of bacteria and eukaryotes. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2023.1114690, doi:10.3389/fmicb.2023.1114690. This article has 7 citations and is from a peer-reviewed journal.

16. (tseng2018abiofilmmatrixassociated pages 1-2): Boo Shan Tseng, Courtney Reichhardt, Gennifer E. Merrihew, Sophia A. Araujo-Hernandez, Joe J. Harrison, Michael J. MacCoss, and Matthew R. Parsek. A biofilm matrix-associated protease inhibitor protects pseudomonas aeruginosa from proteolytic attack. mBio, May 2018. URL: https://doi.org/10.1128/mbio.00543-18, doi:10.1128/mbio.00543-18. This article has 85 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](eco-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. eggers2004theperiplasmicserine pages 4-4
2. nagy2019ecotinamicrobial pages 1-2
3. meyer2023ecotinaversatile pages 3-4
4. goltermann2024microbialprimerthe pages 3-4
5. eggers2004theperiplasmicserine pages 10-10
6. kantyka2010prokaryotederivedproteininhibitors pages 14-15
7. eggers2004theperiplasmicserine pages 1-2
8. tseng2018abiofilmmatrixassociated pages 5-6
9. nagy2019ecotinamicrobial pages 17-19
10. meyer2023ecotinaversatile pages 2-3
11. meyer2023ecotinaversatile pages 1-2
12. eggers2004theperiplasmicserine pages 4-6
13. tseng2018abiofilmmatrixassociated pages 2-3
14. tseng2018abiofilmmatrixassociated pages 4-5
15. tseng2018abiofilmmatrixassociated pages 6-8
16. tseng2018abiofilmmatrixassociated pages 1-2
17. https://doi.org/10.3389/fmicb.2023.1114690
18. https://doi.org/10.1099/mic.0.001497
19. https://doi.org/10.1128/mBio.00543-18
20. https://doi.org/10.1042/BJ20031790
21. https://doi.org/10.1371/journal.ppat.1008232
22. https://doi.org/10.1042/BJ20031790;
23. https://doi.org/10.1128/mBio.00543-18;
24. https://doi.org/10.1016/j.biochi.2010.06.004;
25. https://doi.org/10.1021/acs.biochem.0c00493
26. https://doi.org/10.1371/journal.ppat.1008232;
27. https://doi.org/10.1016/j.biochi.2010.06.004
28. https://doi.org/10.1042/bj20031790,
29. https://doi.org/10.3389/fmicb.2023.1114690,
30. https://doi.org/10.1016/j.biochi.2010.06.004,
31. https://doi.org/10.1371/journal.ppat.1008232,
32. https://doi.org/10.1128/mbio.00543-18,
33. https://doi.org/10.1099/mic.0.001497,