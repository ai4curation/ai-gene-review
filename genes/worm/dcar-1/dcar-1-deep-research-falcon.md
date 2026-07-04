---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-04T16:19:38.653679'
end_time: '2026-07-04T16:36:23.457277'
duration_seconds: 1004.8
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: worm
  gene_id: dcar-1
  gene_symbol: dcar-1
  uniprot_accession: G5EDI0
  protein_description: 'SubName: Full=G-protein coupled receptors family 1 profile
    domain-containing protein {ECO:0000313|EMBL:CAB62778.2};'
  gene_info: Name=dcar-1 {ECO:0000313|EMBL:CAB62778.2, ECO:0000313|WormBase:C06H5.7};
    ORFNames=C06H5.7 {ECO:0000313|WormBase:C06H5.7}, CELE_C06H5.7 {ECO:0000313|EMBL:CAB62778.2};
  organism_full: Caenorhabditis elegans.
  protein_family: Not specified in UniProt
  protein_domains: GPCR_Rhodpsn_7TM. (IPR017452)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 19
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: dcar-1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: dcar-1-deep-research-falcon_artifacts/artifact-01.md
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
- **UniProt Accession:** G5EDI0
- **Protein Description:** SubName: Full=G-protein coupled receptors family 1 profile domain-containing protein {ECO:0000313|EMBL:CAB62778.2};
- **Gene Information:** Name=dcar-1 {ECO:0000313|EMBL:CAB62778.2, ECO:0000313|WormBase:C06H5.7}; ORFNames=C06H5.7 {ECO:0000313|WormBase:C06H5.7}, CELE_C06H5.7 {ECO:0000313|EMBL:CAB62778.2};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Not specified in UniProt
- **Key Domains:** GPCR_Rhodpsn_7TM. (IPR017452)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "dcar-1" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'dcar-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **dcar-1** (gene ID: dcar-1, UniProt: G5EDI0) in worm.

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
- **UniProt Accession:** G5EDI0
- **Protein Description:** SubName: Full=G-protein coupled receptors family 1 profile domain-containing protein {ECO:0000313|EMBL:CAB62778.2};
- **Gene Information:** Name=dcar-1 {ECO:0000313|EMBL:CAB62778.2, ECO:0000313|WormBase:C06H5.7}; ORFNames=C06H5.7 {ECO:0000313|WormBase:C06H5.7}, CELE_C06H5.7 {ECO:0000313|EMBL:CAB62778.2};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Not specified in UniProt
- **Key Domains:** GPCR_Rhodpsn_7TM. (IPR017452)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "dcar-1" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'dcar-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **dcar-1** (gene ID: dcar-1, UniProt: G5EDI0) in worm.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: DCAR-1 (C06H5.7) in *Caenorhabditis elegans*

## 1. Gene and Protein Identity

DCAR-1 (DihydroCaffeic Acid Receptor-1) is a G-protein coupled receptor (GPCR) encoded by the gene *dcar-1* (systematic name C06H5.7) in *Caenorhabditis elegans* (UniProt accession G5EDI0). The protein belongs to the rhodopsin-like family of seven-transmembrane receptors (domain: GPCR_Rhodpsn_7TM, InterPro IPR017452) (venkatesh2021gproteincoupledreceptors pages 2-4, taffoni2015mechanismsofinnate pages 5-6). DCAR-1 is notable as the only GPCR identified to date that functions as a damage-associated molecular pattern (DAMP) sensor in *C. elegans* (venkatesh2021gproteincoupledreceptors pages 2-4, garciasanchez2021ubiquitinrelatedprocessesand pages 9-10).

The following table summarizes the key identity and functional features of DCAR-1:

| Feature | Value |
|---|---|
| Gene Symbol | dcar-1 |
| Full Name | DihydroCaffeic Acid Receptor-1 |
| Systematic Name | C06H5.7 |
| UniProt ID | G5EDI0 |
| Organism | *Caenorhabditis elegans* |
| Protein Type | G-protein coupled receptor (GPCR), predicted 7-transmembrane receptor; consistent with rhodopsin-like 7TM annotation in UniProt (venkatesh2021gproteincoupledreceptors pages 2-4) |
| Domain | GPCR_Rhodpsn_7TM / IPR017452; literature describes DCAR-1 as a GPCR/7TM receptor (venkatesh2021gproteincoupledreceptors pages 2-4, taffoni2015mechanismsofinnate pages 5-6) |
| Endogenous Ligand | 4-hydroxyphenyllactic acid (HPLA), a tyrosine-derived damage-associated molecular pattern (DAMP) that accumulates after infection or injury (venkatesh2021gproteincoupledreceptors pages 2-4, taffoni2015mechanismsofinnate pages 5-6) |
| Tissue Expression | Epidermis/hypodermis, especially the apical epidermal syncytium; also reported in sensory neurons, although immune function is epidermis-specific (taffoni2015mechanismsofinnate pages 5-6, venkatesh2021gproteincoupledreceptors pages 2-4) |
| Functional Localization | Cell surface receptor localized to the apical part of the epidermal syncytium hyp7 (taffoni2015mechanismsofinnate pages 5-6, taffoni2015mechanismsofinnate pages 4-5) |
| Primary Function | DAMP-sensing GPCR that activates epidermal innate immunity in response to fungal infection and wounding (venkatesh2021gproteincoupledreceptors pages 2-4, garciasanchez2021ubiquitinrelatedprocessesand pages 9-10, kim2018signalinginthe pages 14-16) |
| Key Biological Processes | Antifungal defense against *Drechmeria coniospora*, wound response, and induction of antimicrobial peptide genes including *nlp* family targets such as *nlp-29* (venkatesh2021gproteincoupledreceptors pages 2-4, taffoni2015mechanismsofinnate pages 5-6) |
| Initial Characterization | Initially characterized behaviorally as a seven-transmembrane receptor mediating avoidance to dihydrocaffeic acid (Aoki et al. 2011; identified in retrieved literature but full text unavailable in tool search). Subsequently established as an innate immune receptor activated by endogenous HPLA to trigger AMP expression during epidermal damage/infection (summarized in later reviews citing the 2014 primary work) (taffoni2015mechanismsofinnate pages 5-6, kim2018signalinginthe pages 14-16) |


*Table: This table summarizes the verified identity, ligand, localization, and core biological role of the C. elegans GPCR DCAR-1. It is useful as a quick reference to distinguish this receptor from similarly named genes and to anchor interpretation of the downstream immune signaling literature.*

## 2. Primary Function: DAMP-Sensing Receptor for Epidermal Innate Immunity

DCAR-1 serves as a pattern recognition receptor that detects tissue damage in the *C. elegans* epidermis (hypodermis) and activates innate immune defenses. Unlike mammalian Toll-like receptors that primarily detect pathogen-associated molecular patterns (PAMPs), DCAR-1 functions by sensing a host-derived endogenous ligand that accumulates when epidermal integrity is compromised (venkatesh2021gproteincoupledreceptors pages 2-4, kim2018signalinginthe pages 14-16).

### 2.1 Endogenous Ligand: 4-Hydroxyphenyllactic Acid (HPLA)

The endogenous ligand of DCAR-1 is 4-hydroxyphenyllactic acid (HPLA), a product of tyrosine degradation in the hypodermis (taffoni2015mechanismsofinnate pages 5-6, venkatesh2021gproteincoupledreceptors pages 2-4). HPLA levels increase under conditions of epidermal damage, including physical wounding, infection by the natural fungal pathogen *Drechmeria coniospora*, and in cuticle-defective mutants such as *dpy-9* and *dpy-10* (kim2018signalinginthe pages 14-16). The accumulation of HPLA thus functions as a danger signal, providing a mechanism by which the epidermis can detect tissue disruption and mount a defensive response. This identification of HPLA as the cognate ligand was a landmark finding that established DCAR-1 as the first deorphanized GPCR in the *C. elegans* innate immune system (venkatesh2021gproteincoupledreceptors pages 2-4, zhang2021antagonisticfungalenterotoxins pages 10-12).

The gene was initially named for its response to dihydrocaffeic acid, a water-soluble repellent that elicits avoidance behavior in *C. elegans* via sensory neurons (Aoki et al., 2011, as cited in multiple reviews) (venkatesh2021gproteincoupledreceptors pages 2-4). However, the immune-regulatory function of DCAR-1 is distinct from and independent of this neuronal chemosensory role.

### 2.2 Biological Roles

DCAR-1 plays critical roles in two primary contexts of epidermal defense:

**Antifungal immunity:** During infection by *D. coniospora*, a natural endoparasitic fungal pathogen of *C. elegans* that adheres to the cuticle via specialized adhesive knobs and can kill worms within 48 hours, DCAR-1 is essential for the rapid transcriptional upregulation of antimicrobial peptide (AMP) genes in the epidermis (taffoni2015mechanismsofinnate pages 5-6, taffoni2015mechanismsofinnate pages 4-5). The primary transcriptional targets include neuropeptide-like protein genes, particularly *nlp-29*, as well as caenacin (*cnc*) genes (taffoni2015mechanismsofinnate pages 5-6, dierking2016antimicrobialeffectorsin pages 4-5).

**Wound response:** Physical injury to the epidermis similarly triggers DCAR-1-dependent AMP gene induction, demonstrating that this receptor integrates signals from both pathogenic and sterile damage (taffoni2015mechanismsofinnate pages 4-5, taffoni2015mechanismsofinnate pages 5-6).

## 3. Tissue and Subcellular Localization

DCAR-1 is expressed in the epidermis (hypodermis) and in sensory neurons. However, its immune-regulatory function is epidermis-specific and cell-autonomous (taffoni2015mechanismsofinnate pages 5-6, venkatesh2021gproteincoupledreceptors pages 2-4). Within the epidermis, DCAR-1 localizes to the apical part of the epidermal syncytium hyp7, positioning it at the cell surface facing the cuticle—the barrier tissue most directly exposed to environmental pathogens and physical insults (taffoni2015mechanismsofinnate pages 5-6, taffoni2015mechanismsofinnate pages 4-5). This apical localization is functionally significant because it places the receptor at the interface where damage signals (HPLA) would first accumulate following cuticle compromise or pathogen attachment.

## 4. Signaling Pathway

The DCAR-1 signaling pathway in the epidermis has been extensively characterized through forward genetic screens, genome-wide RNAi screens, and epistasis analysis. The pathway proceeds as follows:

| Component | Type/Function | Position in Pathway | Role |
|---|---|---|---|
| DCAR-1 | GPCR; DAMP receptor activated by HPLA | Receptor / pathway entry point | Binds the endogenous tyrosine-metabolite ligand 4-hydroxyphenyllactic acid (HPLA) generated during epidermal damage, fungal infection, or wounding; initiates epidermal innate immune signaling to AMP genes (venkatesh2021gproteincoupledreceptors pages 2-4, taffoni2015mechanismsofinnate pages 5-6) |
| GPA-12 | Gα signaling subunit | Immediately downstream of DCAR-1 | Transduces the activated GPCR signal toward PKC-dependent immune signaling required for AMP induction after fungal infection or wounding (taffoni2015mechanismsofinnate pages 5-6, dierking2016antimicrobialeffectorsin pages 4-5, zhang2021antagonisticfungalenterotoxins pages 10-12) |
| RACK-1 | Gβ-associated signaling component / scaffold | Parallel to GPA-12 downstream of DCAR-1 | Cooperates with GPA-12 in GPCR signaling upstream of TPA-1 to promote epidermal antimicrobial gene expression (taffoni2015mechanismsofinnate pages 5-6) |
| EGL-8/PLC-3 | Phospholipase C enzymes | Upstream of DAG production | Convert PIP2 into DAG, providing the second messenger input needed to activate TPA-1/PKC in the epidermal immune pathway (taffoni2015mechanismsofinnate pages 5-6) |
| DAG | Lipid second messenger | Between PLCs and TPA-1 | Activates TPA-1, coupling upstream GPCR/G-protein signaling to the kinase cascade that drives AMP expression (taffoni2015mechanismsofinnate pages 5-6, kim2018signalinginthe pages 9-12) |
| TPA-1 | Protein kinase C (PKC) | Downstream of GPA-12/RACK-1 and DAG | Central kinase transmitting the DCAR-1 signal toward TIR-1 and the p38 MAPK cascade in response to epidermal infection or injury (taffoni2015mechanismsofinnate pages 5-6, kim2018signalinginthe pages 9-12) |
| TIR-1 | TIR-domain adaptor / scaffold | Upstream of MAP3K NSY-1 | Links PKC-dependent signaling to the conserved p38 MAPK module that controls antimicrobial peptide induction (taffoni2015mechanismsofinnate pages 5-6, dierking2016antimicrobialeffectorsin pages 4-5, kim2018signalinginthe pages 14-16) |
| NSY-1 | MAP kinase kinase kinase (MAP3K) | First kinase in p38 MAPK cascade | Receives input from TIR-1 and activates downstream SEK-1 as part of the canonical epidermal innate immune cascade (taffoni2015mechanismsofinnate pages 5-6) |
| SEK-1 | MAP kinase kinase (MAP2K) | Middle kinase in p38 MAPK cascade | Relays the signal from NSY-1 to PMK-1 to support transcriptional activation of AMP genes (taffoni2015mechanismsofinnate pages 5-6) |
| PMK-1 | p38 MAP kinase | Terminal kinase in core MAPK cascade | Executes the p38 MAPK immune response downstream of DCAR-1, promoting AMP induction and antifungal defense in the epidermis (venkatesh2021gproteincoupledreceptors pages 2-4, taffoni2015mechanismsofinnate pages 5-6) |
| STA-2 | STAT-like transcription factor | Downstream nuclear effector of PMK-1 pathway | Required for transcriptional activation of nlp genes and contributes to AMP expression after fungal infection, wounding, and damage sensing (garciasanchez2021ubiquitinrelatedprocessesand pages 9-10, taffoni2015mechanismsofinnate pages 5-6, kim2018signalinginthe pages 9-12, zhu2023c.eleganshemidesmosomes pages 1-2) |
| ELT-3 | GATA transcription factor | Co-regulator with STA-2 downstream of signaling cascade | Works with STA-2 to promote epidermal AMP gene transcription in response to DCAR-1 pathway activation (taffoni2015mechanismsofinnate pages 5-6) |
| nlp-29/cnc (target genes) | Antimicrobial peptide genes / transcriptional outputs | Terminal output | Encode epidermally induced antimicrobial effectors. nlp-29 is a canonical DCAR-1–p38 MAPK target; cnc genes can also be induced in related epidermal defense programs, with some regulation occurring through a non-canonical DBL-1/TGF-β branch depending on stimulus context (taffoni2015mechanismsofinnate pages 4-5, taffoni2015mechanismsofinnate pages 5-6, dierking2016antimicrobialeffectorsin pages 4-5) |


*Table: This table summarizes the experimentally supported DCAR-1 epidermal signaling pathway in C. elegans, from HPLA sensing at the receptor to antimicrobial peptide gene induction. It is useful for tracing how damage-associated signaling is converted into antifungal and wound-response outputs.*

### 4.1 Detailed Pathway Description

Upon activation by HPLA, DCAR-1 couples to the heterotrimeric G protein subunits GPA-12 (Gα) and RACK-1 (Gβ), which are required for downstream signal transduction to antimicrobial peptide gene expression (taffoni2015mechanismsofinnate pages 5-6, venkatesh2021gproteincoupledreceptors pages 2-4). The G-protein signaling activates phospholipase C enzymes EGL-8 and PLC-3, which hydrolyze phosphatidylinositol 4,5-bisphosphate (PIP2) to produce diacylglycerol (DAG), a lipid second messenger (taffoni2015mechanismsofinnate pages 5-6). DAG in turn activates the serine/threonine protein kinase C TPA-1 (taffoni2015mechanismsofinnate pages 5-6, kim2018signalinginthe pages 9-12).

TPA-1 acts upstream of TIR-1, a TIR-domain adaptor protein homologous to mammalian SARM1, which serves as a scaffold linking PKC-dependent signaling to the core p38 MAPK cascade (taffoni2015mechanismsofinnate pages 5-6, dierking2016antimicrobialeffectorsin pages 4-5). The MAPK module consists of the MAP3K NSY-1, the MAP2K SEK-1, and the p38 MAPK PMK-1, which constitutes the terminal kinase in the cascade (taffoni2015mechanismsofinnate pages 5-6, kim2018signalinginthe pages 9-12).

PMK-1 activates the STAT-like transcription factor STA-2 and the GATA transcription factor ELT-3, which together drive transcription of *nlp* antimicrobial peptide genes, including the canonical target *nlp-29* (taffoni2015mechanismsofinnate pages 5-6, kim2018signalinginthe pages 9-12, dierking2016antimicrobialeffectorsin pages 4-5). The caenacin (*cnc*) AMP gene family is also regulated through this pathway, although *cnc* gene induction shows additional complexity: after wounding, *cnc* induction is p38 MAPK-dependent, but after fungal infection, *cnc* expression is regulated through a non-canonical DBL-1/TGF-β pathway that operates independently of p38 MAPK (taffoni2015mechanismsofinnate pages 5-6, dierking2016antimicrobialeffectorsin pages 4-5).

### 4.2 Relationship to Broader Immune Signaling

The TIR-1/NSY-1/SEK-1/PMK-1 p38 MAPK cascade is a highly conserved signaling module that also functions in the *C. elegans* intestine to regulate resistance to bacterial pathogens (kim2018signalinginthe pages 9-12). In the epidermis, this cascade is specifically wired downstream of the DCAR-1 GPCR pathway, whereas in the intestine, different upstream activators engage the same MAPK module (kim2018signalinginthe pages 9-12). This tissue-specific utilization of a shared signaling core highlights how *C. elegans* achieves distinct immune responses in different tissues using modular signaling architecture.

## 5. Recent Developments (2023–2025)

### 5.1 DCAR-1-Independent Damage Sensing via Hemidesmosomes

A 2023 study by Zhu et al. revealed an important nuance in epidermal damage sensing. Through systematic analysis of collagen-encoding genes, the authors demonstrated that certain types of collagen damage (specifically damage to DPY-7 collagen) can induce *nlp-29* expression independently of DCAR-1 and PMK-1, via a hemidesmosome-based damage-sensing mechanism (zhu2023c.eleganshemidesmosomes pages 10-12). In this alternative pathway, disruption of DPY collagen substructures causes the separation of collagen BLI-1 from the hemidesmosome receptor MUP-4, leading to release of STA-2 from hemidesmosomes and direct induction of AMP gene expression (zhu2023c.eleganshemidesmosomes pages 1-2, zhu2023c.eleganshemidesmosomes pages 10-12). This finding demonstrates that while DCAR-1 is a major DAMP sensor, the epidermis employs multiple, partially overlapping damage-sensing mechanisms, and DCAR-1 only partially accounts for collagen damage-induced immune responses (zhu2023c.eleganshemidesmosomes pages 1-2).

### 5.2 DCAR-1 Pathway and Cisplatin Resistance

Raj et al. (2023) identified the p38 MAPK pathway—in which DCAR-1 functions as the upstream DAMP receptor in the epidermis—as a critical determinant of cisplatin toxicity resistance in post-mitotic *C. elegans* adults (raj2023cisplatintoxicityis pages 10-13, raj2023cisplatintoxicityis pages 13-13). The study demonstrated that cisplatin exposure activates the p38 MAPK/ATF-7 immune signaling axis, and mutations in pathway components including *dcar-1* increased sensitivity to cisplatin-induced necrotic damage (raj2023cisplatintoxicityis pages 10-13, raj2023cisplatintoxicityis pages 13-14). This work extended the functional significance of the DCAR-1 pathway beyond pathogen defense to xenobiotic stress responses.

### 5.3 Pathogen Virulence Strategies Targeting the DCAR-1 Pathway

Zhang et al. (2021) demonstrated that the fungal pathogen *D. coniospora* produces enterotoxins (DcEntA and DcEntB) that can interfere with the DCAR-1-initiated immune cascade at multiple levels, including blocking STA-2 nuclear translocation and disrupting vesicle trafficking in the epidermis (zhang2021antagonisticfungalenterotoxins pages 10-12). This illustrates the co-evolutionary arms race between host damage sensing and pathogen immune evasion strategies.

## 6. Evolutionary and Comparative Significance

DCAR-1 represents a noncanonical pattern recognition receptor in *C. elegans* innate immunity (venkatesh2021gproteincoupledreceptors pages 2-4). Unlike mammals, where TLRs, NLRs, and other canonical PRRs directly detect pathogen-derived molecules, *C. elegans* appears to primarily rely on sensing the damage caused by pathogens rather than pathogen molecules themselves (venkatesh2021gproteincoupledreceptors pages 2-4, kim2018signalinginthe pages 14-16). DCAR-1's function as a DAMP sensor—detecting an endogenous tyrosine metabolite that accumulates upon tissue damage—exemplifies this "guard" or damage-sensing strategy of immune activation (venkatesh2021gproteincoupledreceptors pages 2-4, kim2018signalinginthe pages 14-16). The unique worm TOL-1 (TLR homolog) is not essential for most pathogen defenses, making GPCR-based sensing through receptors like DCAR-1 a particularly important immune detection mechanism in this organism (venkatesh2021gproteincoupledreceptors pages 2-4).

## 7. Summary

DCAR-1 is a rhodopsin-family GPCR that functions as the primary damage-associated molecular pattern sensor in the *C. elegans* epidermis. Localized to the apical surface of the hyp7 epidermal syncytium, it detects the endogenous ligand HPLA—a tyrosine metabolite that accumulates upon cuticle disruption, fungal infection, or wounding. Ligand binding activates a well-characterized signaling cascade through G-proteins (GPA-12/RACK-1), phospholipase C, DAG, PKC (TPA-1), the TIR-1 adaptor, and the p38 MAPK module (NSY-1/SEK-1/PMK-1), culminating in STA-2- and ELT-3-dependent transcription of antimicrobial peptide genes including *nlp-29*. Recent work has revealed additional DCAR-1-independent damage-sensing mechanisms in the epidermis and extended the functional relevance of the DCAR-1/p38 MAPK pathway to xenobiotic stress resistance. DCAR-1 remains the only well-documented GPCR functioning as an innate immune DAMP receptor in *C. elegans*, providing a paradigmatic example of how metazoans can employ GPCRs for immune surveillance at epithelial barriers.

References

1. (venkatesh2021gproteincoupledreceptors pages 2-4): Siddharth R. Venkatesh and Varsha Singh. G protein-coupled receptors: the choreographers of innate immunity in caenorhabditis elegans. PLOS Pathogens, 17:e1009151, Jan 2021. URL: https://doi.org/10.1371/journal.ppat.1009151, doi:10.1371/journal.ppat.1009151. This article has 17 citations and is from a highest quality peer-reviewed journal.

2. (taffoni2015mechanismsofinnate pages 5-6): Clara Taffoni and Nathalie Pujol. Mechanisms of innate immunity in c. elegans epidermis. Tissue Barriers, 3:e1078432, Oct 2015. URL: https://doi.org/10.1080/21688370.2015.1078432, doi:10.1080/21688370.2015.1078432. This article has 75 citations and is from a peer-reviewed journal.

3. (garciasanchez2021ubiquitinrelatedprocessesand pages 9-10): Juan A. Garcia-Sanchez, Jonathan J. Ewbank, and Orane Visvikis. Ubiquitin-related processes and innate immunity in c. elegans. Cellular and Molecular Life Sciences, 78:4305-4333, Feb 2021. URL: https://doi.org/10.1007/s00018-021-03787-w, doi:10.1007/s00018-021-03787-w. This article has 15 citations and is from a domain leading peer-reviewed journal.

4. (taffoni2015mechanismsofinnate pages 4-5): Clara Taffoni and Nathalie Pujol. Mechanisms of innate immunity in c. elegans epidermis. Tissue Barriers, 3:e1078432, Oct 2015. URL: https://doi.org/10.1080/21688370.2015.1078432, doi:10.1080/21688370.2015.1078432. This article has 75 citations and is from a peer-reviewed journal.

5. (kim2018signalinginthe pages 14-16): Dennis H. Kim and J. Ewbank. Signaling in the innate immune response. WormBook, pages 1-35, Aug 2018. URL: https://doi.org/10.1895/wormbook.1.83.2, doi:10.1895/wormbook.1.83.2. This article has 181 citations.

6. (zhang2021antagonisticfungalenterotoxins pages 10-12): Xing Zhang, Benjamin W. Harding, Dina Aggad, Damien Courtine, Jia-Xuan Chen, Nathalie Pujol, and Jonathan J. Ewbank. Antagonistic fungal enterotoxins intersect at multiple levels with host innate immune defences. Jun 2021. URL: https://doi.org/10.1371/journal.pgen.1009600, doi:10.1371/journal.pgen.1009600. This article has 21 citations and is from a domain leading peer-reviewed journal.

7. (dierking2016antimicrobialeffectorsin pages 4-5): Katja Dierking, Wentao Yang, and Hinrich Schulenburg. Antimicrobial effectors in the nematode caenorhabditis elegans: an outgroup to the arthropoda. Philosophical Transactions of the Royal Society B: Biological Sciences, 371:20150299, May 2016. URL: https://doi.org/10.1098/rstb.2015.0299, doi:10.1098/rstb.2015.0299. This article has 107 citations and is from a domain leading peer-reviewed journal.

8. (kim2018signalinginthe pages 9-12): Dennis H. Kim and J. Ewbank. Signaling in the innate immune response. WormBook, pages 1-35, Aug 2018. URL: https://doi.org/10.1895/wormbook.1.83.2, doi:10.1895/wormbook.1.83.2. This article has 181 citations.

9. (zhu2023c.eleganshemidesmosomes pages 1-2): Yi Zhu, Wenna Li, Yifang Dong, Chujie Xia, and Rong Fu. C. elegans hemidesmosomes sense collagen damage to trigger innate immune response in the epidermis. Cells, 12:2223, Sep 2023. URL: https://doi.org/10.3390/cells12182223, doi:10.3390/cells12182223. This article has 13 citations.

10. (zhu2023c.eleganshemidesmosomes pages 10-12): Yi Zhu, Wenna Li, Yifang Dong, Chujie Xia, and Rong Fu. C. elegans hemidesmosomes sense collagen damage to trigger innate immune response in the epidermis. Cells, 12:2223, Sep 2023. URL: https://doi.org/10.3390/cells12182223, doi:10.3390/cells12182223. This article has 13 citations.

11. (raj2023cisplatintoxicityis pages 10-13): Dorota Raj, Bashar Kraish, Jari Martikainen, Agnieszka Podraza-Farhanieh, Gautam Kao, and Peter Naredi. Cisplatin toxicity is counteracted by the activation of the p38/atf-7 signaling pathway in post-mitotic c. elegans. Nature Communications, May 2023. URL: https://doi.org/10.1038/s41467-023-38568-5, doi:10.1038/s41467-023-38568-5. This article has 13 citations and is from a highest quality peer-reviewed journal.

12. (raj2023cisplatintoxicityis pages 13-13): Dorota Raj, Bashar Kraish, Jari Martikainen, Agnieszka Podraza-Farhanieh, Gautam Kao, and Peter Naredi. Cisplatin toxicity is counteracted by the activation of the p38/atf-7 signaling pathway in post-mitotic c. elegans. Nature Communications, May 2023. URL: https://doi.org/10.1038/s41467-023-38568-5, doi:10.1038/s41467-023-38568-5. This article has 13 citations and is from a highest quality peer-reviewed journal.

13. (raj2023cisplatintoxicityis pages 13-14): Dorota Raj, Bashar Kraish, Jari Martikainen, Agnieszka Podraza-Farhanieh, Gautam Kao, and Peter Naredi. Cisplatin toxicity is counteracted by the activation of the p38/atf-7 signaling pathway in post-mitotic c. elegans. Nature Communications, May 2023. URL: https://doi.org/10.1038/s41467-023-38568-5, doi:10.1038/s41467-023-38568-5. This article has 13 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](dcar-1-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](dcar-1-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. venkatesh2021gproteincoupledreceptors pages 2-4
2. kim2018signalinginthe pages 14-16
3. taffoni2015mechanismsofinnate pages 5-6
4. kim2018signalinginthe pages 9-12
5. zhang2021antagonisticfungalenterotoxins pages 10-12
6. garciasanchez2021ubiquitinrelatedprocessesand pages 9-10
7. taffoni2015mechanismsofinnate pages 4-5
8. dierking2016antimicrobialeffectorsin pages 4-5
9. raj2023cisplatintoxicityis pages 10-13
10. raj2023cisplatintoxicityis pages 13-13
11. raj2023cisplatintoxicityis pages 13-14
12. https://doi.org/10.1371/journal.ppat.1009151,
13. https://doi.org/10.1080/21688370.2015.1078432,
14. https://doi.org/10.1007/s00018-021-03787-w,
15. https://doi.org/10.1895/wormbook.1.83.2,
16. https://doi.org/10.1371/journal.pgen.1009600,
17. https://doi.org/10.1098/rstb.2015.0299,
18. https://doi.org/10.3390/cells12182223,
19. https://doi.org/10.1038/s41467-023-38568-5,