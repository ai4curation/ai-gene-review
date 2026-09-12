---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-25T17:10:33.113050'
end_time: '2026-06-25T17:26:08.144599'
duration_seconds: 935.03
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEAE
  gene_id: APRA
  gene_symbol: aprA
  uniprot_accession: Q03023
  protein_description: 'RecName: Full=Serralysin; EC=3.4.24.40; AltName: Full=Alkaline
    metalloproteinase; Short=AP; Flags: Precursor;'
  gene_info: Name=aprA; OrderedLocusNames=PA1249;
  organism_full: Pseudomonas aeruginosa (strain ATCC 15692 / DSM 22644 / CIP 104116
    / JCM 14847 / LMG 12228 / 1C / PRS 101 / PAO1).
  protein_family: Belongs to the peptidase M10B family. .
  protein_domains: Hemolysin-typ_Ca-bd_CS. (IPR018511); Hemolysn_Ca-bd. (IPR001343);
    MetalloPept_cat_dom_sf. (IPR024079); Pept_M10_metallopeptidase. (IPR001818); Pept_M10B.
    (IPR016294)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 31
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: APRA-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: APRA-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q03023
- **Protein Description:** RecName: Full=Serralysin; EC=3.4.24.40; AltName: Full=Alkaline metalloproteinase; Short=AP; Flags: Precursor;
- **Gene Information:** Name=aprA; OrderedLocusNames=PA1249;
- **Organism (full):** Pseudomonas aeruginosa (strain ATCC 15692 / DSM 22644 / CIP 104116 / JCM 14847 / LMG 12228 / 1C / PRS 101 / PAO1).
- **Protein Family:** Belongs to the peptidase M10B family. .
- **Key Domains:** Hemolysin-typ_Ca-bd_CS. (IPR018511); Hemolysn_Ca-bd. (IPR001343); MetalloPept_cat_dom_sf. (IPR024079); Pept_M10_metallopeptidase. (IPR001818); Pept_M10B. (IPR016294)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "aprA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas aeruginosa (strain ATCC 15692 / DSM 22644 / CIP 104116 / JCM 14847 / LMG 12228 / 1C / PRS 101 / PAO1).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'aprA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **aprA** (gene ID: APRA, UniProt: Q03023) in PSEAE.

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
- **UniProt Accession:** Q03023
- **Protein Description:** RecName: Full=Serralysin; EC=3.4.24.40; AltName: Full=Alkaline metalloproteinase; Short=AP; Flags: Precursor;
- **Gene Information:** Name=aprA; OrderedLocusNames=PA1249;
- **Organism (full):** Pseudomonas aeruginosa (strain ATCC 15692 / DSM 22644 / CIP 104116 / JCM 14847 / LMG 12228 / 1C / PRS 101 / PAO1).
- **Protein Family:** Belongs to the peptidase M10B family. .
- **Key Domains:** Hemolysin-typ_Ca-bd_CS. (IPR018511); Hemolysn_Ca-bd. (IPR001343); MetalloPept_cat_dom_sf. (IPR024079); Pept_M10_metallopeptidase. (IPR001818); Pept_M10B. (IPR016294)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "aprA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas aeruginosa (strain ATCC 15692 / DSM 22644 / CIP 104116 / JCM 14847 / LMG 12228 / 1C / PRS 101 / PAO1).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'aprA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **aprA** (gene ID: APRA, UniProt: Q03023) in PSEAE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: *Pseudomonas aeruginosa* AprA (Alkaline Protease / Serralysin)

**Gene:** *aprA* (PA1249) | **UniProt:** Q03023 | **Organism:** *Pseudomonas aeruginosa* PAO1

## 1. Gene and Protein Identity

The *aprA* gene (ordered locus name PA1249) of *Pseudomonas aeruginosa* strain PAO1 encodes the alkaline protease (AP), also known as aeruginolysin, a secreted zinc-dependent metalloproteinase classified as a serralysin (EC 3.4.24.40). The mature protein is approximately 50 kDa and belongs to the peptidase M10B family within the metzincin superfamily of metalloproteases (laarman2012pseudomonasaeruginosaalkaline pages 2-3, butterworth2014modulationofthe pages 1-2). AprA is recognized as a key extracellular virulence factor of *P. aeruginosa* that functions primarily as an immune-modulating protease rather than a conventional tissue-degrading enzyme (krumina2026molecularmechanismsunderlying pages 8-10).

## 2. Protein Structure and Domain Architecture

AprA is a two-domain metalloprotease precursor protein with the following architecture:

- **N-terminal catalytic domain:** Contains the canonical HEXXHXXGXXH zinc coordination motif that is the hallmark of the metzincin superfamily. The active-site zinc ion (Zn²⁺) is essential for catalytic activity and is coordinated by three histidine residues within this motif (butterworth2014modulationofthe pages 1-2). This domain shares evolutionary similarity with mammalian matrix metalloproteinases (MMP2 and MMP9) (butterworth2014modulationofthe pages 4-5).

- **C-terminal calcium-binding RTX domain:** Contains multiple RTX (Repeats-in-ToXin) nonapeptide repeats that are rich in aspartate and glycine residues. These repeats form a parallel β-roll motif upon binding calcium ions. The RTX domain is intrinsically disordered in the absence of Ca²⁺, and calcium binding at millimolar concentrations (apparent affinity of 50–60 mM) induces proper folding of the entire protein and is essential for activation of the N-terminal protease domain (butterworth2014modulationofthe pages 4-5, butterworth2014modulationofthe pages 1-2, butterworth2014modulationofthe pages 10-10). This calcium-dependent folding mechanism is a key regulatory feature of serralysin-type proteases and may also facilitate secretion, as the unfolded protein can be threaded through the type I secretion channel.

The structural and functional features of AprA are summarized below:

| Domain/Motif | Location | Function | Key Features |
|---|---|---|---|
| N-terminal catalytic domain | N-terminal region of mature AprA | Catalyzes proteolytic cleavage of host and microbial substrates as a Zn²⁺-dependent metalloprotease | Contains the conserved HEXXHXXGXXH zinc-binding motif characteristic of serralysin-type metalloproteases; the active-site Zn²⁺ is essential for catalysis; responsible for cleavage of substrates such as complement proteins and ENaC (butterworth2014modulationofthe pages 1-2) |
| C-terminal calcium-binding RTX domain | C-terminal region | Promotes folding, stabilization, and activation of the protease after Ca²⁺ binding | Contains RTX-associated Asp/Gly-rich nonapeptide repeats that form a Ca²⁺-bound parallel β-roll; intrinsically disordered or poorly folded without Ca²⁺; Ca²⁺ binding induces proper folding and enables full protease activity (butterworth2014modulationofthe pages 4-5, butterworth2014modulationofthe pages 1-2, butterworth2014modulationofthe pages 10-10) |
| Metalloprotease superfamily classification | Whole protein / family-level annotation | Places AprA within the serralysin branch of secreted bacterial metalloproteases | AprA is a serralysin-family alkaline metalloprotease belonging to peptidase family M10B within the metzincin-like metalloprotease superfamily; this classification is consistent with the Zn²⁺ catalytic motif and Ca²⁺-regulated RTX architecture (krumina2026molecularmechanismsunderlying pages 8-10, butterworth2014modulationofthe pages 1-2) |
| AprI inhibitor interaction | Functional interaction with AprA catalytic machinery | Protects the bacterium from uncontrolled AprA proteolysis and can block AprA activity extracellularly in vitro | AprI is the cognate alkaline protease inhibitor; it inhibits AprA near-stoichiometrically and blocks AprA-dependent ENaC activation; inhibitor action is linked to interaction with the Zn²⁺-containing protease active site, consistent with structural studies of the AprA-AprI system (butterworth2014modulationofthe pages 4-5, butterworth2014modulationofthe pages 7-9, butterworth2014modulationofthe pages 10-10) |


*Table: This table summarizes the major structural and functional features of Pseudomonas aeruginosa AprA, including its catalytic and RTX calcium-binding regions, family classification, and interaction with the cognate inhibitor AprI. It is useful for connecting domain organization to secretion, activation, catalysis, and regulation.*

## 3. Enzymatic Activity and Substrate Specificity

AprA catalyzes the proteolytic cleavage of peptide bonds in a Zn²⁺-dependent manner, with Ca²⁺ serving as an essential cofactor for structural integrity and enzymatic activation. Without Ca²⁺, the enzyme exhibits minimal activity (butterworth2014modulationofthe pages 4-5). The enzyme retains sustained catalytic activity in the extracellular environment, maintaining 63% activity after 24 hours at 37°C (butterworth2014modulationofthe pages 4-5).

AprA has a broad but selective substrate specificity, with a marked preference for host immune proteins rather than generic structural extracellular matrix components. The primary substrates and their biological consequences are summarized in the following table:

| Substrate | Pathway/System Affected | Biological Consequence | Key Reference |
|---|---|---|---|
| Complement C2 | Classical and lectin complement pathways | AprA cleaves C2, preventing formation of the C4b2a C3 convertase, reducing C3b opsonization, C5a generation, neutrophil recruitment, phagocytosis, and complement-mediated killing (laarman2012pseudomonasaeruginosaalkaline pages 7-8, gonzalezalsina2023pseudomonasaeruginosaand pages 10-12) | (laarman2012pseudomonasaeruginosaalkaline pages 7-8, gonzalezalsina2023pseudomonasaeruginosaand pages 10-12) |
| C1q | Classical complement pathway | Degradation of C1q impairs complement recognition/activation and contributes to immune evasion (laarman2012pseudomonasaeruginosaalkaline pages 2-3, gonzalezalsina2023pseudomonasaeruginosaand pages 10-12) | (laarman2012pseudomonasaeruginosaalkaline pages 2-3, gonzalezalsina2023pseudomonasaeruginosaand pages 10-12) |
| C1s | Classical complement pathway | Cleavage of C1s contributes to suppression of classical pathway activation, although C2 cleavage appears to be the dominant inhibitory mechanism (laarman2012pseudomonasaeruginosaalkaline pages 7-8, laarman2012pseudomonasaeruginosaalkaline pages 1-2, laarman2012pseudomonasaeruginosaalkaline pages 2-3) | (laarman2012pseudomonasaeruginosaalkaline pages 7-8, laarman2012pseudomonasaeruginosaalkaline pages 1-2, laarman2012pseudomonasaeruginosaalkaline pages 2-3) |
| C3 | Central complement cascade | At higher concentrations/longer incubation, AprA can cleave C3, further reducing opsonization and downstream complement effector functions (laarman2012pseudomonasaeruginosaalkaline pages 7-8, laarman2012pseudomonasaeruginosaalkaline pages 2-3) | (laarman2012pseudomonasaeruginosaalkaline pages 7-8, laarman2012pseudomonasaeruginosaalkaline pages 2-3) |
| IFN-γ | Host cytokine signaling / innate immunity | Degradation of IFN-γ dampens host inflammatory and antimicrobial signaling, aiding immune evasion (laarman2012pseudomonasaeruginosaalkaline pages 2-3) | (laarman2012pseudomonasaeruginosaalkaline pages 2-3) |
| TNF-α | Host cytokine signaling / inflammation | Degradation of TNF-α reduces inflammatory signaling and host defense activation (laarman2012pseudomonasaeruginosaalkaline pages 2-3, akter2026structuralandfunctional pages 2-5) | (laarman2012pseudomonasaeruginosaalkaline pages 2-3, akter2026structuralandfunctional pages 2-5) |
| Flagellin | TLR5-mediated innate immune recognition | Cleavage of monomeric flagellin prevents TLR5 activation, reducing host detection of P. aeruginosa (laarman2012pseudomonasaeruginosaalkaline pages 2-3, keim2024polymicrobialinteractionsbetween pages 30-34) | (laarman2012pseudomonasaeruginosaalkaline pages 2-3, keim2024polymicrobialinteractionsbetween pages 30-34) |
| ENaC | Airway epithelial ion transport | Proteolytic cleavage activates epithelial sodium channel activity, potentially altering airway surface physiology; activation is slower than trypsin and can be blocked by AprI (butterworth2014modulationofthe pages 4-5, butterworth2014modulationofthe pages 7-9) | (butterworth2014modulationofthe pages 4-5, butterworth2014modulationofthe pages 7-9) |
| Fibrin | Tissue/extracellular host substrate in corneal infection | Fibrin degradation contributes to tissue damage and virulence in infected corneal tissue (akter2026structuralandfunctional pages 2-5) | (akter2026structuralandfunctional pages 2-5) |
| *S. aureus* SasG | Polymicrobial aggregation / biofilm formation | AprA cleaves SasG, removing/exposing domains that promote *S. aureus* aggregation, enhancing polymicrobial biofilm formation, persistence, and antibiotic tolerance in chronic wounds (keim2024polymicrobialinteractionsbetween pages 8-10, keim2024polymicrobialinteractionsbetween pages 10-13, keim2024polymicrobialinteractionsbetween pages 13-14) | (keim2024polymicrobialinteractionsbetween pages 8-10, keim2024polymicrobialinteractionsbetween pages 10-13, keim2024polymicrobialinteractionsbetween pages 13-14) |


*Table: This table summarizes experimentally supported and review-supported AprA substrates, the host or microbial systems they affect, and the resulting biological consequences. It is useful for linking AprA's biochemical specificity to its roles in immune evasion, tissue damage, and polymicrobial biofilm biology.*

### Primary Enzymatic Function — Complement Evasion

The best-characterized enzymatic activity of AprA is its cleavage of complement component C2. AprA was identified as the first bacterial protease demonstrated to cleave C2 (laarman2012pseudomonasaeruginosaalkaline pages 7-8). At physiologically relevant concentrations (200 nM, within the range secreted by *P. aeruginosa*), AprA specifically cleaves C2 into C2a and C2b fragments. The resulting fluid-phase C2a cannot bind to surface-deposited C4b, preventing formation of the active C3 convertase (C4b2a) required for classical and lectin pathway complement activation (laarman2012pseudomonasaeruginosaalkaline pages 7-8). AprA cleaves C2 at sites similar to the natural cleavage sites of the complement proteases C1s and MASP, suggesting it targets accessible, structurally exposed regions (laarman2012pseudomonasaeruginosaalkaline pages 7-8). At higher concentrations and longer incubation times, AprA can also cleave C3 and C4 (laarman2012pseudomonasaeruginosaalkaline pages 7-8). Importantly, AprA does not inhibit the alternative complement pathway, as C2 is not involved in that route (laarman2012pseudomonasaeruginosaalkaline pages 7-8, laarman2012pseudomonasaeruginosaalkaline pages 1-2). The IC₅₀ for AprA-mediated inhibition of complement-dependent phagocytosis is approximately 100 nM (laarman2012pseudomonasaeruginosaalkaline pages 6-6). AprA also degrades C1q, C1s, and C5a, further suppressing complement recognition and downstream effector functions (laarman2012pseudomonasaeruginosaalkaline pages 2-3, gonzalezalsina2023pseudomonasaeruginosaand pages 10-12).

### Additional Host Substrates

Beyond complement proteins, AprA degrades cytokines IFN-γ and TNF-α, dampening host inflammatory and antimicrobial signaling (laarman2012pseudomonasaeruginosaalkaline pages 2-3). AprA cleaves monomeric bacterial flagellin, preventing Toll-like receptor 5 (TLR5) activation and thus reducing innate immune detection of *P. aeruginosa* (laarman2012pseudomonasaeruginosaalkaline pages 2-3). AprA also disrupts neutrophil extracellular traps (NETs), a key antimicrobial defense mechanism (krumina2026molecularmechanismsunderlying pages 8-10). Additionally, AprA proteolytically activates the epithelial sodium channel (ENaC) on the apical surface of airway epithelial cells, leading to increased sodium absorption; this activation is slower than trypsin-mediated activation (approximately 5-fold slower kinetics) and can be blocked by the cognate inhibitor AprI (butterworth2014modulationofthe pages 4-5, butterworth2014modulationofthe pages 7-9). In corneal tissue, AprA degrades fibrin and contributes to tissue necrosis (akter2026structuralandfunctional pages 2-5).

## 4. Subcellular Localization and Secretion

AprA is secreted into the extracellular milieu via the Type I Secretion System (T1SS), a one-step secretion apparatus that directly translocates substrates across both inner and outer membranes without a periplasmic intermediate (akter2026structuralandfunctional pages 2-5, krumina2026molecularmechanismsunderlying pages 8-10, sousa2021genomicandmetabolic pages 5-7). The T1SS responsible for AprA secretion is encoded by the *aprDEF* gene cluster, organized in a dedicated operon located immediately upstream of the *aprA* structural gene (krumina2026molecularmechanismsunderlying pages 8-10). This system comprises three essential components: AprD, an ABC transporter that provides energy for translocation from the inner membrane; AprE, a membrane fusion protein (MFP) that bridges the periplasm; and AprF, an outer membrane factor (OMF) (krumina2026molecularmechanismsunderlying pages 8-10, sousa2021genomicandmetabolic pages 5-7). The protein is secreted with its propeptide intact (krumina2026molecularmechanismsunderlying pages 22-23). Once released, AprA functions exclusively in the extracellular environment, where it encounters and degrades host immune molecules at sites of infection (laarman2012pseudomonasaeruginosaalkaline pages 2-3, akter2026structuralandfunctional pages 2-5).

A periplasmic inhibitor, AprI, is co-expressed with AprA and serves to protect the bacterium from unregulated protease activity during secretion. AprI inhibits AprA at near-stoichiometric concentrations and can block AprA-mediated ENaC activation in a dose-dependent manner (butterworth2014modulationofthe pages 4-5, butterworth2014modulationofthe pages 7-9).

## 5. Regulation of Expression

Expression of *aprA* is tightly regulated by multiple signaling systems:

- **Quorum sensing:** AprA expression is controlled by the LasR-LasI (Las) quorum sensing system, with additional input from the RhlI-RhlR (Rhl) system. The LasR transcriptional activator directly regulates the *apr* gene cluster, linking AprA production to bacterial population density (krumina2026molecularmechanismsunderlying pages 8-10, gonzalezalsina2023pseudomonasaeruginosaand pages 10-12). The *aprA* gene was found to be part of the approximately 61% of LasR-regulated genes that were dysregulated in stringent response mutants (pletzer2020thestringentstress pages 12-13).

- **Stringent stress response:** AprA is a downstream effector of the ppGpp-mediated stringent stress response. Under stringent response activation (e.g., serine hydroxamate induction), *aprA* is upregulated 4.1-fold, whereas in ppGpp-deficient mutants (*relA spoT* double mutant), *aprA* is downregulated 9.6-fold (pletzer2020thestringentstress pages 8-9, pletzer2020thestringentstress pages 7-8). This regulation may reflect a bacterial strategy to produce extracellular proteases for nutrient acquisition during amino acid starvation (pletzer2020thestringentstress pages 7-8).

- **Two-component regulatory systems:** AprA is also subject to regulation by two-component signal transduction systems, including indirect control through hierarchical regulators such as AlgR and GacA (pletzer2020thestringentstress pages 9-11).

## 6. Role in Virulence and Pathogenesis

### Complement Evasion and Immune Modulation

AprA is a critical immune evasion factor. By degrading C2, C1q, C1s, C3, and C5a, AprA potently inhibits complement-mediated opsonization, phagocytosis, and neutrophil killing of *P. aeruginosa* (laarman2012pseudomonasaeruginosaalkaline pages 1-2, laarman2012pseudomonasaeruginosaalkaline pages 7-8, gonzalezalsina2023pseudomonasaeruginosaand pages 10-12). This complement resistance operates as part of a redundant system in *P. aeruginosa*, alongside elastase (LasB) and Protease IV, which also degrade complement components (laarman2012pseudomonasaeruginosaalkaline pages 7-8). The cytokine-degrading and flagellin-cleaving activities further suppress innate immune activation (laarman2012pseudomonasaeruginosaalkaline pages 2-3).

### In Vivo Virulence Evidence

In a murine cutaneous infection model, deletion of *aprA* significantly enhanced mouse survival to 77% compared with only 33% survival in wild-type PAO1-infected mice after 3 days (P = 0.025), despite no differences in initial lesion sizes or bacterial counts (pletzer2020thestringentstress pages 8-9). This directly demonstrates that AprA contributes to *P. aeruginosa* virulence through its proteolytic degradation of host defense molecules. AprA has also been identified as the downstream effector responsible for the reduced cytotoxicity observed in stringent response mutants (pletzer2020thestringentstress pages 1-2).

### Polymicrobial Interactions and Biofilm Formation

Recent research has revealed a novel role for AprA in mediating polymicrobial interactions. In chronic wound co-infections of *P. aeruginosa* and *Staphylococcus aureus*, AprA cleaves the *S. aureus* surface protein SasG by removing its A domain and exposing the B domain, enabling homodimeric interactions between adjacent *S. aureus* cells (keim2024polymicrobialinteractionsbetween pages 8-10). This SasG processing induces MRSA aggregation and promotes polymicrobial biofilm formation. Heterologous expression of AprA alone in *E. coli* is sufficient to induce SasG-dependent aggregation at levels comparable to wild-type *P. aeruginosa* (keim2024polymicrobialinteractionsbetween pages 8-10, keim2024polymicrobialinteractionsbetween pages 10-13). AprA works synergistically with LasB elastase for maximal SasG processing, and the resulting aggregates display increased tolerance to vancomycin and ciprofloxacin (keim2024polymicrobialinteractionsbetween pages 13-14). AprA expression is upregulated in vivo in clinical wound specimens (keim2024polymicrobialinteractionsbetween pages 8-10). These findings indicate that AprA promotes polymicrobial coexistence, delayed wound healing, and increased antimicrobial resistance in chronic wound infections (keim2024polymicrobialinteractionsbetween pages 13-14, keim2024polymicrobialinteractionsbetween pages 14-17).

### Additional Virulence Contributions

AprA also contributes to pyocyanin production, an important virulence factor in *P. aeruginosa* (krumina2026molecularmechanismsunderlying pages 8-10, krumina2026molecularmechanismsunderlying pages 22-23). In corneal infections, AprA causes tissue necrosis, degrades fibrin, and increases bacterial attachment to corneal epithelium by exposing host cell receptors (akter2026structuralandfunctional pages 2-5).

## 7. Clinical and Epidemiological Significance

The *apr* gene is highly conserved among clinical *P. aeruginosa* isolates. In a study of Mexican clinical isolates from hospital- and community-acquired infections, the alkaline protease gene (*apr*) was detected in 99.1% of strains, underscoring its near-ubiquitous presence in pathogenic *P. aeruginosa* populations (gonzalezalsina2023pseudomonasaeruginosaand pages 10-12). AprA has been highlighted as a promising target for anti-virulence therapeutic development, particularly given that *aprA* deletion enhances host survival in infection models without affecting bacterial growth, suggesting that targeting AprA could reduce virulence without imposing strong selective pressure for resistance (pletzer2020thestringentstress pages 8-9, pletzer2020thestringentstress pages 12-13).

## 8. Summary

AprA (alkaline protease/aeruginolysin) of *P. aeruginosa* PAO1 is a secreted, calcium-activated, zinc-dependent metalloprotease of the serralysin (M10B) family. It is exported via the AprDEF type I secretion system and functions exclusively in the extracellular environment. Its primary enzymatic activity is the proteolytic cleavage of host immune proteins—most notably complement component C2, which blocks classical and lectin pathway activation. AprA also degrades complement factors C1q, C1s, C3, and C5a, cytokines IFN-γ and TNF-α, and monomeric flagellin, collectively enabling immune evasion. Expression is regulated by the Las/Rhl quorum sensing hierarchy and the ppGpp-mediated stringent stress response. Recent work has expanded its functional repertoire to include promotion of polymicrobial biofilm formation through processing of the *S. aureus* surface protein SasG. Deletion of *aprA* significantly reduces virulence in murine infection models, establishing it as a key contributor to *P. aeruginosa* pathogenesis and a potential anti-virulence therapeutic target.

References

1. (laarman2012pseudomonasaeruginosaalkaline pages 2-3): A. Laarman, B. Bardoel, M. Ruyken, Job Fernie, F. Milder, J. V. van Strijp, and S. Rooijakkers. Pseudomonas aeruginosa alkaline protease blocks complement activation via the classical and lectin pathways. The Journal of Immunology, 188:386-393, Jan 2012. URL: https://doi.org/10.4049/jimmunol.1102162, doi:10.4049/jimmunol.1102162. This article has 160 citations.

2. (butterworth2014modulationofthe pages 1-2): Michael B. Butterworth, Liang Zhang, Xiaoning Liu, Robert M. Shanks, and Patrick H. Thibodeau. Modulation of the epithelial sodium channel (enac) by bacterial metalloproteases and protease inhibitors. PLoS ONE, 9:e100313, Jun 2014. URL: https://doi.org/10.1371/journal.pone.0100313, doi:10.1371/journal.pone.0100313. This article has 36 citations and is from a peer-reviewed journal.

3. (krumina2026molecularmechanismsunderlying pages 8-10): Angelika Krūmiņa, Aigars Reinis, Agneta Jeske, Indra Zeltiņa, and Ludmila Vīksna. Molecular mechanisms underlying the pathogenicity of pseudomonas aeruginosa. Medicina, 62:462, Feb 2026. URL: https://doi.org/10.3390/medicina62030462, doi:10.3390/medicina62030462. This article has 1 citations.

4. (butterworth2014modulationofthe pages 4-5): Michael B. Butterworth, Liang Zhang, Xiaoning Liu, Robert M. Shanks, and Patrick H. Thibodeau. Modulation of the epithelial sodium channel (enac) by bacterial metalloproteases and protease inhibitors. PLoS ONE, 9:e100313, Jun 2014. URL: https://doi.org/10.1371/journal.pone.0100313, doi:10.1371/journal.pone.0100313. This article has 36 citations and is from a peer-reviewed journal.

5. (butterworth2014modulationofthe pages 10-10): Michael B. Butterworth, Liang Zhang, Xiaoning Liu, Robert M. Shanks, and Patrick H. Thibodeau. Modulation of the epithelial sodium channel (enac) by bacterial metalloproteases and protease inhibitors. PLoS ONE, 9:e100313, Jun 2014. URL: https://doi.org/10.1371/journal.pone.0100313, doi:10.1371/journal.pone.0100313. This article has 36 citations and is from a peer-reviewed journal.

6. (butterworth2014modulationofthe pages 7-9): Michael B. Butterworth, Liang Zhang, Xiaoning Liu, Robert M. Shanks, and Patrick H. Thibodeau. Modulation of the epithelial sodium channel (enac) by bacterial metalloproteases and protease inhibitors. PLoS ONE, 9:e100313, Jun 2014. URL: https://doi.org/10.1371/journal.pone.0100313, doi:10.1371/journal.pone.0100313. This article has 36 citations and is from a peer-reviewed journal.

7. (laarman2012pseudomonasaeruginosaalkaline pages 7-8): A. Laarman, B. Bardoel, M. Ruyken, Job Fernie, F. Milder, J. V. van Strijp, and S. Rooijakkers. Pseudomonas aeruginosa alkaline protease blocks complement activation via the classical and lectin pathways. The Journal of Immunology, 188:386-393, Jan 2012. URL: https://doi.org/10.4049/jimmunol.1102162, doi:10.4049/jimmunol.1102162. This article has 160 citations.

8. (gonzalezalsina2023pseudomonasaeruginosaand pages 10-12): Alex González-Alsina, Margalida Mateu-Borrás, Antonio Doménech-Sánchez, and Sebastián Albertí. Pseudomonas aeruginosa and the complement system: a review of the evasion strategies. Microorganisms, 11:664, Mar 2023. URL: https://doi.org/10.3390/microorganisms11030664, doi:10.3390/microorganisms11030664. This article has 31 citations.

9. (laarman2012pseudomonasaeruginosaalkaline pages 1-2): A. Laarman, B. Bardoel, M. Ruyken, Job Fernie, F. Milder, J. V. van Strijp, and S. Rooijakkers. Pseudomonas aeruginosa alkaline protease blocks complement activation via the classical and lectin pathways. The Journal of Immunology, 188:386-393, Jan 2012. URL: https://doi.org/10.4049/jimmunol.1102162, doi:10.4049/jimmunol.1102162. This article has 160 citations.

10. (akter2026structuralandfunctional pages 2-5): Tanzina Akter, Paula-Maree Challita, Abrar Maswood Haider, Shiful Islam, Kaniz Fatema, Fiona Stapleton, and Mark Willcox. Structural and functional insights into pseudomonas aeruginosa’s secretion systems 1–6: regulation, role in microbial keratitis and drug targets. European Journal of Clinical Microbiology &amp; Infectious Diseases, 45:79-101, Oct 2026. URL: https://doi.org/10.1007/s10096-025-05295-2, doi:10.1007/s10096-025-05295-2. This article has 3 citations and is from a peer-reviewed journal.

11. (keim2024polymicrobialinteractionsbetween pages 30-34): Klara Keim, Mohini Bhattacharya, H. A. Crosby, C. Jenul, Krista B. Mills, Michael J. Schurr, and A. Horswill. Polymicrobial interactions between staphylococcus aureus and pseudomonas aeruginosa promote biofilm formation and persistence in chronic wound infections. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.04.621402, doi:10.1101/2024.11.04.621402. This article has 18 citations.

12. (keim2024polymicrobialinteractionsbetween pages 8-10): Klara Keim, Mohini Bhattacharya, H. A. Crosby, C. Jenul, Krista B. Mills, Michael J. Schurr, and A. Horswill. Polymicrobial interactions between staphylococcus aureus and pseudomonas aeruginosa promote biofilm formation and persistence in chronic wound infections. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.04.621402, doi:10.1101/2024.11.04.621402. This article has 18 citations.

13. (keim2024polymicrobialinteractionsbetween pages 10-13): Klara Keim, Mohini Bhattacharya, H. A. Crosby, C. Jenul, Krista B. Mills, Michael J. Schurr, and A. Horswill. Polymicrobial interactions between staphylococcus aureus and pseudomonas aeruginosa promote biofilm formation and persistence in chronic wound infections. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.04.621402, doi:10.1101/2024.11.04.621402. This article has 18 citations.

14. (keim2024polymicrobialinteractionsbetween pages 13-14): Klara Keim, Mohini Bhattacharya, H. A. Crosby, C. Jenul, Krista B. Mills, Michael J. Schurr, and A. Horswill. Polymicrobial interactions between staphylococcus aureus and pseudomonas aeruginosa promote biofilm formation and persistence in chronic wound infections. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.04.621402, doi:10.1101/2024.11.04.621402. This article has 18 citations.

15. (laarman2012pseudomonasaeruginosaalkaline pages 6-6): A. Laarman, B. Bardoel, M. Ruyken, Job Fernie, F. Milder, J. V. van Strijp, and S. Rooijakkers. Pseudomonas aeruginosa alkaline protease blocks complement activation via the classical and lectin pathways. The Journal of Immunology, 188:386-393, Jan 2012. URL: https://doi.org/10.4049/jimmunol.1102162, doi:10.4049/jimmunol.1102162. This article has 160 citations.

16. (sousa2021genomicandmetabolic pages 5-7): Telma de Sousa, Michel Hébraud, Maria L. N. Enes Dapkevicius, Luís Maltez, José Eduardo Pereira, Rosa Capita, Carlos Alonso-Calleja, Gilberto Igrejas, and Patricia Poeta. Genomic and metabolic characteristics of the pathogenicity in pseudomonas aeruginosa. International Journal of Molecular Sciences, 22:12892, Nov 2021. URL: https://doi.org/10.3390/ijms222312892, doi:10.3390/ijms222312892. This article has 225 citations.

17. (krumina2026molecularmechanismsunderlying pages 22-23): Angelika Krūmiņa, Aigars Reinis, Agneta Jeske, Indra Zeltiņa, and Ludmila Vīksna. Molecular mechanisms underlying the pathogenicity of pseudomonas aeruginosa. Medicina, 62:462, Feb 2026. URL: https://doi.org/10.3390/medicina62030462, doi:10.3390/medicina62030462. This article has 1 citations.

18. (pletzer2020thestringentstress pages 12-13): Daniel Pletzer, Travis M. Blimkie, Heidi Wolfmeier, Yicong Li, Arjun Baghela, Amy H. Y. Lee, Reza Falsafi, and Robert E. W. Hancock. The stringent stress response controls proteases and global regulators under optimal growth conditions in pseudomonas aeruginosa. Aug 2020. URL: https://doi.org/10.1128/msystems.00495-20, doi:10.1128/msystems.00495-20. This article has 39 citations and is from a peer-reviewed journal.

19. (pletzer2020thestringentstress pages 8-9): Daniel Pletzer, Travis M. Blimkie, Heidi Wolfmeier, Yicong Li, Arjun Baghela, Amy H. Y. Lee, Reza Falsafi, and Robert E. W. Hancock. The stringent stress response controls proteases and global regulators under optimal growth conditions in pseudomonas aeruginosa. Aug 2020. URL: https://doi.org/10.1128/msystems.00495-20, doi:10.1128/msystems.00495-20. This article has 39 citations and is from a peer-reviewed journal.

20. (pletzer2020thestringentstress pages 7-8): Daniel Pletzer, Travis M. Blimkie, Heidi Wolfmeier, Yicong Li, Arjun Baghela, Amy H. Y. Lee, Reza Falsafi, and Robert E. W. Hancock. The stringent stress response controls proteases and global regulators under optimal growth conditions in pseudomonas aeruginosa. Aug 2020. URL: https://doi.org/10.1128/msystems.00495-20, doi:10.1128/msystems.00495-20. This article has 39 citations and is from a peer-reviewed journal.

21. (pletzer2020thestringentstress pages 9-11): Daniel Pletzer, Travis M. Blimkie, Heidi Wolfmeier, Yicong Li, Arjun Baghela, Amy H. Y. Lee, Reza Falsafi, and Robert E. W. Hancock. The stringent stress response controls proteases and global regulators under optimal growth conditions in pseudomonas aeruginosa. Aug 2020. URL: https://doi.org/10.1128/msystems.00495-20, doi:10.1128/msystems.00495-20. This article has 39 citations and is from a peer-reviewed journal.

22. (pletzer2020thestringentstress pages 1-2): Daniel Pletzer, Travis M. Blimkie, Heidi Wolfmeier, Yicong Li, Arjun Baghela, Amy H. Y. Lee, Reza Falsafi, and Robert E. W. Hancock. The stringent stress response controls proteases and global regulators under optimal growth conditions in pseudomonas aeruginosa. Aug 2020. URL: https://doi.org/10.1128/msystems.00495-20, doi:10.1128/msystems.00495-20. This article has 39 citations and is from a peer-reviewed journal.

23. (keim2024polymicrobialinteractionsbetween pages 14-17): Klara Keim, Mohini Bhattacharya, H. A. Crosby, C. Jenul, Krista B. Mills, Michael J. Schurr, and A. Horswill. Polymicrobial interactions between staphylococcus aureus and pseudomonas aeruginosa promote biofilm formation and persistence in chronic wound infections. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.04.621402, doi:10.1101/2024.11.04.621402. This article has 18 citations.

## Artifacts

- [Edison artifact artifact-00](APRA-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](APRA-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. krumina2026molecularmechanismsunderlying pages 8-10
2. butterworth2014modulationofthe pages 1-2
3. butterworth2014modulationofthe pages 4-5
4. laarman2012pseudomonasaeruginosaalkaline pages 2-3
5. akter2026structuralandfunctional pages 2-5
6. laarman2012pseudomonasaeruginosaalkaline pages 7-8
7. laarman2012pseudomonasaeruginosaalkaline pages 6-6
8. krumina2026molecularmechanismsunderlying pages 22-23
9. pletzer2020thestringentstress pages 12-13
10. pletzer2020thestringentstress pages 7-8
11. pletzer2020thestringentstress pages 9-11
12. pletzer2020thestringentstress pages 8-9
13. pletzer2020thestringentstress pages 1-2
14. keim2024polymicrobialinteractionsbetween pages 8-10
15. keim2024polymicrobialinteractionsbetween pages 13-14
16. gonzalezalsina2023pseudomonasaeruginosaand pages 10-12
17. butterworth2014modulationofthe pages 10-10
18. butterworth2014modulationofthe pages 7-9
19. laarman2012pseudomonasaeruginosaalkaline pages 1-2
20. keim2024polymicrobialinteractionsbetween pages 30-34
21. keim2024polymicrobialinteractionsbetween pages 10-13
22. sousa2021genomicandmetabolic pages 5-7
23. keim2024polymicrobialinteractionsbetween pages 14-17
24. https://doi.org/10.4049/jimmunol.1102162,
25. https://doi.org/10.1371/journal.pone.0100313,
26. https://doi.org/10.3390/medicina62030462,
27. https://doi.org/10.3390/microorganisms11030664,
28. https://doi.org/10.1007/s10096-025-05295-2,
29. https://doi.org/10.1101/2024.11.04.621402,
30. https://doi.org/10.3390/ijms222312892,
31. https://doi.org/10.1128/msystems.00495-20,