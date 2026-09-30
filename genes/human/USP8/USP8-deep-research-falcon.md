---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T13:54:13.743640'
end_time: '2026-09-08T14:06:20.337197'
duration_seconds: 726.59
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: USP8
  gene_symbol: USP8
  uniprot_accession: P40818
  protein_description: 'RecName: Full=Ubiquitin carboxyl-terminal hydrolase 8 {ECO:0000305};
    EC=3.4.19.12 {ECO:0000269|PubMed:9628861}; AltName: Full=Deubiquitinating enzyme
    8; AltName: Full=Ubiquitin isopeptidase Y; Short=hUBPy; AltName: Full=Ubiquitin
    thioesterase 8; AltName: Full=Ubiquitin-specific-processing protease 8;'
  gene_info: Name=USP8 {ECO:0000312|HGNC:HGNC:12631}; Synonyms=KIAA0055, UBPY;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the peptidase C19 family. .
  protein_domains: Papain-like_cys_pep_sf. (IPR038765); Peptidase_C19_UCH. (IPR001394);
    Rhodanese-like_dom. (IPR001763); Rhodanese-like_dom_sf. (IPR036873); Ub_carboxyl-term_hydrolase.
    (IPR050185)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: USP8-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** P40818
- **Protein Description:** RecName: Full=Ubiquitin carboxyl-terminal hydrolase 8 {ECO:0000305}; EC=3.4.19.12 {ECO:0000269|PubMed:9628861}; AltName: Full=Deubiquitinating enzyme 8; AltName: Full=Ubiquitin isopeptidase Y; Short=hUBPy; AltName: Full=Ubiquitin thioesterase 8; AltName: Full=Ubiquitin-specific-processing protease 8;
- **Gene Information:** Name=USP8 {ECO:0000312|HGNC:HGNC:12631}; Synonyms=KIAA0055, UBPY;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the peptidase C19 family. .
- **Key Domains:** Papain-like_cys_pep_sf. (IPR038765); Peptidase_C19_UCH. (IPR001394); Rhodanese-like_dom. (IPR001763); Rhodanese-like_dom_sf. (IPR036873); Ub_carboxyl-term_hydrolase. (IPR050185)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "USP8" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'USP8' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **USP8** (gene ID: USP8, UniProt: P40818) in human.

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
- **UniProt Accession:** P40818
- **Protein Description:** RecName: Full=Ubiquitin carboxyl-terminal hydrolase 8 {ECO:0000305}; EC=3.4.19.12 {ECO:0000269|PubMed:9628861}; AltName: Full=Deubiquitinating enzyme 8; AltName: Full=Ubiquitin isopeptidase Y; Short=hUBPy; AltName: Full=Ubiquitin thioesterase 8; AltName: Full=Ubiquitin-specific-processing protease 8;
- **Gene Information:** Name=USP8 {ECO:0000312|HGNC:HGNC:12631}; Synonyms=KIAA0055, UBPY;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the peptidase C19 family. .
- **Key Domains:** Papain-like_cys_pep_sf. (IPR038765); Peptidase_C19_UCH. (IPR001394); Rhodanese-like_dom. (IPR001763); Rhodanese-like_dom_sf. (IPR036873); Ub_carboxyl-term_hydrolase. (IPR050185)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "USP8" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'USP8' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **USP8** (gene ID: USP8, UniProt: P40818) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Human USP8 (UniProt P40818): Functional-Annotation Research Report

## Executive summary

The requested target is unambiguously **human ubiquitin-specific peptidase 8 (USP8; UBPY; KIAA0055; UniProt P40818)**, not a similarly named protein from another organism. It is an approximately 130-kDa, 1,118-residue, multidomain **papain-like cysteine deubiquitinase** of the peptidase C19/USP family. Its architecture—MIT, rhodanese-like, WW-like regulatory, and C-terminal USP catalytic domains—matches the supplied UniProt/InterPro description. The literature reviewed here consistently concerns *Homo sapiens* USP8 or experimentally relevant mammalian orthologs; no conflicting gene identity was used. (dufner2019ubiquitinspecificprotease8 pages 1-3, caba2024autoinhibitionofubiquitinspecific pages 1-2, petukhova2024usp8mutationsassociated pages 1-2)

USP8’s primary biochemical function is hydrolysis of the bond joining ubiquitin’s C-terminal Gly76 to a substrate or another ubiquitin. Its most firmly established cellular role is control of ubiquitinated membrane proteins and trafficking machinery on the **cytosolic face of endosomes**, where it is recruited to ESCRT complexes. EGFR is a well-supported substrate, but whether USP8-mediated deubiquitination ultimately favors receptor recycling or efficient multivesicular-body/lysosomal degradation varies with cellular context. (dufner2019ubiquitinspecificprotease8 pages 3-4, kakihara2021molecularbasisof pages 1-2)

The clearest human disease mechanism is in ACTH-secreting pituitary neuroendocrine tumors causing Cushing disease. Somatic mutations near Ser718–Pro720 disable phosphorylation-dependent 14-3-3 restraint, facilitate formation of a hyperactive catalytic fragment, and sustain EGFR–ERK–POMC–ACTH signaling. A 2024 systematic review estimated USP8 variants in approximately 35% of corticotroph adenomas, although individual cohorts range from 11% to 62%. USP8 remains a **preclinical therapeutic target**; no human trial of a selective USP8 inhibitor was identified. (hashemimadani2024targetedanalysisof pages 1-2, ma2015recurrentgainoffunctionusp8 pages 1-2)

| Topic | Best-supported conclusion | Key quantitative evidence | Evidence type / limitations |
|---|---|---|---|
| Identity and domains | The target is human USP8/UBPY/KIAA0055, a USP-family cysteine deubiquitinase matching UniProt P40818. It contains an N-terminal MIT domain, rhodanese-like domain, long disordered region with SH3-binding and Ser718-centered 14-3-3 motifs, a WW-like autoinhibitory domain, and a C-terminal USP catalytic domain. (dufner2019ubiquitinspecificprotease8 pages 1-3, caba2024autoinhibitionofubiquitinspecific pages 1-2, kakihara2021molecularbasisof pages 1-2, petukhova2024usp8mutationsassociated pages 1-2) | Protein length: 1,118 aa; WW-like domain: aa 645–684; catalytic region reported around aa 778–1088. (kakihara2021molecularbasisof pages 1-2, petukhova2024usp8mutationsassociated pages 1-2) | Identity and architecture are supported by sequence annotation, interaction studies, and structural biochemistry. Exact domain boundaries vary slightly among annotations. |
| Catalytic reaction and linkage specificity | USP8 hydrolyzes ubiquitin C-terminal isopeptide, peptide, or thioester bonds, releasing ubiquitin from conjugated proteins or ubiquitin chains. Its papain-like USP domain uses a Cys–His–Asp/Asn catalytic arrangement. USP8 has broad activity toward Lys-linked chains rather than strict linkage specificity; cellular specificity is substantially determined by recruitment domains and interacting proteins. (takahashi2020ahumandub pages 5-9, kakihara2021molecularbasisof pages 1-2) | In an 88-protein human DUB array, 80 DUBs were active and 52 USPs cleaved at least one diubiquitin. USP-family enzymes other than CYLD generally showed broad linkage specificity; USP8 was not among the nine USPs with greater than 10% M1-diubiquitin cleavage. (takahashi2020ahumandub pages 5-9) | Recombinant diubiquitin assays establish intrinsic activity but do not reproduce membranes, longer chains, substrate recruitment, or cellular cofactors. Substrate-specific K6 or K63 observations should not be interpreted as an exclusive intrinsic preference. |
| Autoinhibition and 14-3-3 | The folded WW-like domain inhibits USP8 in cis by competing with ubiquitin for the catalytic S1 pocket. Ser718 phosphorylation permits 14-3-3 binding, which stabilizes autoinhibition. Disease mutations can disrupt this restraint and promote cleavage at Lys714, yielding a hyperactive approximately 40-kDa catalytic fragment. AMPK was identified in 2024 as a selective Ser718 kinase. (caba2024autoinhibitionofubiquitinspecific pages 1-2, caba2024autoinhibitionofubiquitinspecific pages 4-6, kakihara2021molecularbasisof pages 1-2) | WW-domain deletion increased catalytic efficiency about 12-fold to 215 ± 49 × 10^3 M−1 s−1; W655S increased it about eightfold to 146 ± 14 × 10^3 M−1 s−1. WW deletion improved mono-ubiquitin affinity from KD 1.48 ± 0.37 to 0.29 ± 0.016 micromolar. (caba2024autoinhibitionofubiquitinspecific pages 4-6) | Supported by purified full-length protein, kinetics, NMR, SEC-MALLS/SAXS, and mutagenesis. The precise atomic interface remains model-supported rather than resolved as a high-resolution experimental complex. |
| Endosomal EGFR role | USP8 acts mainly on the cytosolic face of endosomes, where MIT–CHMP and SH3-motif–STAM interactions connect it to ESCRT machinery. EGFR deubiquitination is well supported, but its outcome is context-dependent: studies variously indicate promotion of ESCRT/MVB degradation or rescue and recycling to the plasma membrane. (dufner2019ubiquitinspecificprotease8 pages 3-4, dufner2019ubiquitinspecificprotease8 pages 1-3, kakihara2021molecularbasisof pages 1-2) | One tumor comparison reported EGFR expression in 80% of USP8-mutant versus 50% of wild-type tumors, although subsequent cohorts were inconsistent. (dufner2019ubiquitinspecificprotease8 pages 4-6) | Endosomal association and EGFR deubiquitination are directly supported. The degradation-versus-recycling question remains unresolved because USP8 modifies both cargo and endocytic machinery, and results vary with cell type and assay design. |
| Mitophagy | USP8 can remove K6-linked ubiquitin from Parkin and facilitate Parkin recruitment to damaged mitochondria. Conversely, 2023 work showed that reducing USP8 enhances a distinct Parkin-independent basal mitophagy pathway in Drosophila brain and human neurons. USP8 also regulates p62/SQSTM1 and EPG5 in autophagic flux. (dufner2019ubiquitinspecificprotease8 pages 4-6, dufner2019ubiquitinspecificprotease8 pages 6-7, mauri2023usp8downregulationpromotes pages 17-19, mauri2023usp8downregulationpromotes pages 19-20) | DUBs-IN-1/2 were reported to inhibit USP8 at approximately 200 nM, compared with greater than 100 micromolar for USP7. (mauri2023usp8downregulationpromotes pages 17-19) | Genetic and cellular evidence is substantial, but apparently opposite effects in Parkin-dependent and Parkin-independent pathways show that USP8 inhibition cannot be assumed to enhance every form of mitophagy. No human therapeutic benefit has been demonstrated. |
| Cushing disease | Somatic gain-of-function mutations cluster in exon 14 around Ser718–Pro720 in the 14-3-3-binding motif. Loss of 14-3-3 restraint and enhanced proteolysis increase USP8 activity, EGFR recycling and EGFR–ERK signaling, thereby increasing POMC transcription and ACTH secretion. EGFR is a strong functional mediator but probably not the only relevant substrate. (theodoropoulou2015decodingthegenetic pages 8-10, ma2015recurrentgainoffunctionusp8 pages 7-8, ma2015recurrentgainoffunctionusp8 pages 1-2) | The original Chinese cohort found variants in 67/108 tumors, or 62.04%, and 0/150 other pituitary adenoma types. A 2024 systematic review estimated USP8 variants in 35% of corticotroph adenomas; 25% involved codon 720/P720R. Reported cohort frequencies span 11–62%. (hashemimadani2024targetedanalysisof pages 1-2, ma2015recurrentgainoffunctionusp8 pages 1-2) | Supported by tumor sequencing, primary-cell knockdown, EGFR blockade, and biochemical assays. Frequency and genotype–phenotype associations vary with ancestry, cohort size, sequencing method, and inclusion criteria. |
| 2023–2024 advances | Recent work identified Parkin-independent mitophagy after USP8 reduction, established a full-length structural and kinetic model of WW/14-3-3 autoinhibition, identified AMPK as a Ser718 kinase, and implicated WNT and somatostatin-receptor trafficking in mutant corticotroph tumors. Molecular-dynamics studies suggest that hotspot and selected non-hotspot variants can cause convergent conformational changes. (mauri2023usp8downregulationpromotes pages 17-19, caba2024autoinhibitionofubiquitinspecific pages 1-2, petukhova2024usp8mutationsassociated pages 1-2, nerubenko2024cushing’sdiseasemanifestation pages 1-2) | In a 2024 cohort, 18/35 tumors, or 51%, carried variants. Mutant tumors were more often microadenomas, 44% versus 29%, and recurrent, 44% versus 22%; all were SST5-positive and 73% were SST5+/SST2+. (nerubenko2024cushing’sdiseasemanifestation pages 1-2) | The autoinhibition study provides strong mechanistic biochemistry. Tumor findings come from a small observational cohort, while molecular-dynamics results require experimental validation. |
| Therapeutic and clinical status | USP8 remains a preclinical target. Candidate tools include DUBs-IN-1/2, SJB3-019A, less-selective compounds, and engineered ubiquitin variant UbV8.2. Indirect approaches include EGFR inhibitors and pasireotide in selected tumors. No relevant human trial of a selective USP8 inhibitor was identified. (dufner2019ubiquitinspecificprotease8 pages 8-10, mauri2023usp8downregulationpromotes pages 17-19, takahashi2020ahumandub pages 5-9, hashemimadani2024targetedanalysisof pages 1-2) | Reported potencies include approximately 200–280 nM for DUBs-IN-2, 4.8 nM for UbV8.2CΔ2, and 68% USP8 inhibition by SJB3-019A in a DUB-array assay. (mauri2023usp8downregulationpromotes pages 17-19, dufner2019ubiquitinspecificprotease8 pages 8-10, takahashi2020ahumandub pages 5-9) | Evidence is limited to biochemical assays, cells, primary tumor cultures, and animal models. USP8 essentiality creates toxicity concerns, and an older review's printed 0.28 mM value for DUBs-IN-2 conflicts with later approximately 200–280 nM reporting. |


*Table: Evidence hierarchy for human USP8/P40818, covering molecular function, localization, regulation, disease biology, recent findings, and therapeutic status. Quantitative findings and major uncertainties are shown alongside the supporting evidence.*

## 1. Identity verification and domain organization

### 1.1 Target identity

The literature identifies USP8 as **USP8/UBPY/KIAA0055**, a human USP-family deubiquitinase. The reported 1,118-amino-acid length and approximately 130-kDa mass agree with UniProt P40818. The supplied EC classification, **EC 3.4.19.12**, is consistent with ubiquitinyl-hydrolase activity. (dufner2019ubiquitinspecificprotease8 pages 1-3, caba2024autoinhibitionofubiquitinspecific pages 1-2, petukhova2024usp8mutationsassociated pages 1-2)

The protein is not a ubiquitin C-terminal hydrolase-family UCH enzyme in the narrow phylogenetic sense; rather, it belongs to the **ubiquitin-specific protease branch of clan CA/peptidase C19**, whose catalytic domain adopts the papain-like cysteine-protease fold. “Ubiquitin carboxyl-terminal hydrolase” in the protein name describes the reaction class.

### 1.2 Domain architecture

From N to C terminus, experimentally supported features include:

- An **MIT—microtubule-interacting and transport—domain**, which binds charged multivesicular-body proteins (CHMPs) associated with early and late endosomes.
- An adjacent **rhodanese-like domain**, reported to interact with the E3 ligase NRDP1. This is principally an interaction module in USP8, not evidence that USP8 catalyzes sulfur transfer.
- A long, largely disordered central region containing several atypical **RXXK SH3-binding motifs** that engage STAM1/2 in ESCRT-0.
- A phosphorylation-dependent **14-3-3-binding motif** centered on human Ser718.
- An atypical **WW-like domain at residues 645–684**, now experimentally established as the minimal intramolecular autoinhibitory unit.
- A C-terminal **USP catalytic domain**, approximately residues 778–1088 depending on annotation boundaries. (caba2024autoinhibitionofubiquitinspecific pages 1-2, kakihara2021molecularbasisof pages 1-2, petukhova2024usp8mutationsassociated pages 1-2)

This architecture explains how a broadly ubiquitin-reactive catalytic domain achieves cellular specificity: the noncatalytic modules recruit USP8 to defined endosomal protein complexes and substrates.

## 2. Primary enzymatic function

### 2.1 Catalyzed reaction and mechanism

USP8 catalyzes:

**ubiquitin–substrate + H₂O → free ubiquitin + deubiquitinated substrate**

or, for a ubiquitin chain:

**Ub–Ub + H₂O → ubiquitin-chain products/free ubiquitin.**

The cleaved bond is usually an **isopeptide bond** between ubiquitin Gly76 and a substrate lysine or a lysine in another ubiquitin. USP enzymes can also process suitable ubiquitin-terminal peptide or thioester bonds. The USP8 catalytic domain has the characteristic fingers, palm and thumb subdomains: the fingers bind ubiquitin’s globular body, while a Cys–His–Asp/Asn catalytic arrangement in the palm/thumb cleft performs nucleophilic hydrolysis. Ub-VME covalently labels the catalytic cysteine, experimentally confirming cysteine-protease chemistry. (kakihara2021molecularbasisof pages 1-2)

The apo catalytic domain has closed blocking loops and an inward-constricted fingers subdomain, implying that ubiquitin binding induces a catalytically competent conformation. Thus, structural plasticity and relief of autoinhibition are integral to activity rather than the catalytic site simply remaining constitutively accessible. (kakihara2021molecularbasisof pages 1-2)

### 2.2 Ubiquitin-chain and substrate specificity

USP8 should be regarded as a **broad Lys-linked-chain deubiquitinase**, not as an enzyme intrinsically specific for one linkage. In a recombinant array of 88 human DUBs tested against eight diubiquitin linkage types, 80 enzymes were active and USP-family enzymes other than CYLD generally had broad specificity. USP8 was not among the nine USPs exhibiting more than 10% cleavage of linear M1-linked diubiquitin, arguing against strong M1 activity under those assay conditions. (takahashi2020ahumandub pages 5-9)

Cellular observations of particular linkages reflect the recruited substrate and pathway and should not be mistaken for an exclusive intrinsic preference. Examples include removal of **K6-linked ubiquitin from Parkin**, K63-linked ubiquitin from EPG5, and ubiquitin from EGFR, STAM proteins, p62/SQSTM1, SHANK3, Sec31 and other reported proteins. Of these, EGFR, Parkin, EPG5 and p62 have comparatively direct biochemical or cellular deubiquitination evidence. Some larger substrate lists derive from interaction, stability or pathway assays and therefore do not always establish direct catalysis. (dufner2019ubiquitinspecificprotease8 pages 6-7, mauri2023usp8downregulationpromotes pages 19-20, kakihara2021molecularbasisof pages 1-2)

## 3. Regulation: WW-like autoinhibition, phosphorylation and proteolysis

### 3.1 WW-like domain

Kakihara et al. identified residues **645–684** as an autoinhibitory region using deletion analysis, Ub-VME labeling, pull-down, single-molecule FRET and modeling. The region forms an atypical three-stranded WW-like fold and obstructs access to the ubiquitin-binding pocket. Removing it increased deubiquitination of EGFR, Parkin and STAM1/2 without materially changing USP8’s staining pattern, indicating regulation of catalytic access rather than localization. The study was published November 2021 in *Communications Biology*; DOI: https://doi.org/10.1038/s42003-021-02802-x. (kakihara2021molecularbasisof pages 1-2)

Caba et al. substantially strengthened this model in 2024 using purified near-full-length human USP8, kinetics, SEC-MALLS, SAXS, NMR and mutagenesis. Full-length USP8 was an extended monomer; WW-domain deletion increased catalytic efficiency about **12-fold**, to `(215 ± 49) × 10³ M⁻¹s⁻¹`, while W655S disruption of WW folding increased it about eightfold, to `(146 ± 14) × 10³ M⁻¹s⁻¹`. WW deletion improved apparent mono-ubiquitin binding from `KD 1.48 ± 0.37 µM` to `0.29 ± 0.016 µM`. NMR supported direct WW–catalytic-domain interaction and competition between the WW module and ubiquitin for the catalytic S1 pocket. The inhibition required the WW domain **in cis**, emphasizing the importance of tether geometry. Published online August 28, 2024 in *Journal of Biological Chemistry*; DOI: https://doi.org/10.1016/j.jbc.2024.107727. (caba2024autoinhibitionofubiquitinspecific pages 1-2, caba2024autoinhibitionofubiquitinspecific pages 4-6)

The proposed atomic interface remains partly model-based rather than a crystallographically or cryo-EM-resolved WW–catalytic-domain complex, but the underlying autoinhibitory interaction is supported by convergent biochemical evidence.

### 3.2 Ser718–14-3-3 control

Phosphorylation of Ser718 creates a mode-I-like 14-3-3-binding site. Bound 14-3-3 stabilizes the WW-dependent autoinhibited conformation. The 2024 study identified **AMP-activated protein kinase (AMPK)** as a highly selective Ser718 modifier and showed that a phosphorylated USP8 molecule complexes with a constitutive 14-3-3γ dimer. 14-3-3 potentiated inhibition of full-length USP8 but not a WW-deleted enzyme, unifying phosphorylation-dependent and intramolecular inhibition. (caba2024autoinhibitionofubiquitinspecific pages 1-2, caba2024autoinhibitionofubiquitinspecific pages 4-6)

### 3.3 Proteolytic activation

Cushing-disease mutations that weaken 14-3-3 binding favor cleavage near **Lys714**, producing an approximately **40-kDa C-terminal catalytic fragment** that is more active than full-length USP8. Limited processing has also been reported after T-cell-receptor activation, suggesting that cleavage can be a regulated physiological mechanism as well as a pathological one. The identity and regulation of the responsible protease remain potential intervention points. (dufner2019ubiquitinspecificprotease8 pages 3-4, caba2024autoinhibitionofubiquitinspecific pages 1-2)

## 4. Cellular localization and canonical biological role

USP8 is principally a soluble cytoplasmic protein recruited to the **cytosolic surface of early and late endosomes**, rather than an integral membrane protein or secreted enzyme. Its MIT domain associates with ESCRT-III CHMP proteins, while its SH3-binding motifs interact with STAM1/2 in the HRS–STAM ESCRT-0 complex. These interactions place catalytic USP8 beside ubiquitinated membrane cargo and trafficking machinery. (dufner2019ubiquitinspecificprotease8 pages 1-3, caba2024autoinhibitionofubiquitinspecific pages 1-2)

A proposed USP8–STAM2–HD-PTP–CHMP4B checkpoint helps transfer receptor cargo from ESCRT-0 toward ESCRT-III and intraluminal vesicles. USP8 also maintains the abundance or ubiquitination state of endocytic machinery including HRS, STAM1/2, Eps15 and CHMP proteins. Retromer-dependent recycling of the cation-independent mannose-6-phosphate receptor connects USP8 to transport of lysosomal hydrolases and lysosome competence. (dufner2019ubiquitinspecificprotease8 pages 3-4, kakihara2021molecularbasisof pages 1-2)

### Important mechanistic qualification

There is a genuine literature disagreement over the final fate of EGFR. Some experiments indicate that USP8-mediated removal of ubiquitin is required for orderly ESCRT sorting and **promotes lysosomal degradation**; others indicate that it removes the sorting signal, rescues EGFR from lysosomes and **promotes recycling**. These results are not necessarily mutually exclusive: USP8 acts on both receptor cargo and the ESCRT machinery, and the net result depends on timing, compartment, expression level and cellular context. EGFR deubiquitination is established more securely than a universal degradation-versus-recycling outcome. (dufner2019ubiquitinspecificprotease8 pages 3-4, dufner2019ubiquitinspecificprotease8 pages 1-3)

## 5. Principal pathways

### 5.1 EGFR and other receptor tyrosine kinases

Following ligand activation and ubiquitination, EGFR enters endosomes. USP8 can remove receptor ubiquitin and thereby alter the balance between return to the plasma membrane and MVB/lysosomal delivery. The same endosomal logic extends to MET and other RTKs, although direct evidence is strongest for EGFR. Because receptor trafficking controls signal duration, USP8 changes downstream ERK/MAPK output without itself being a kinase. (dufner2019ubiquitinspecificprotease8 pages 3-4, theodoropoulou2015decodingthegenetic pages 8-10)

### 5.2 Autophagy and mitochondrial quality control

USP8 has pathway-specific effects on autophagy:

- It deubiquitinates **p62/SQSTM1 at Lys420** and removes K63-linked ubiquitin from **EPG5 at Lys252**, supporting EPG5–LC3 interaction and autophagic flux in relevant cells.
- It removes K6-linked ubiquitin from **Parkin**, facilitating Parkin recruitment to damaged mitochondria and supporting PINK1/Parkin-dependent mitophagy.
- Conversely, Mauri et al. reported in April 2023 that reducing USP8 increased basal **Parkin-independent mitophagy** in Drosophila brain and human neurons. DOI: https://doi.org/10.3390/cells12081143. (dufner2019ubiquitinspecificprotease8 pages 4-6, dufner2019ubiquitinspecificprotease8 pages 6-7, mauri2023usp8downregulationpromotes pages 17-19, mauri2023usp8downregulationpromotes pages 19-20)

These apparently opposite results indicate that USP8 can promote Parkin recruitment yet suppress a separate Parkin-independent pathway. They caution against the broad claim that USP8 inhibition will universally increase or decrease mitophagy.

### 5.3 Additional experimentally supported processes

USP8 has been implicated in T-cell-receptor microclusters and positive thymocyte selection; T-cell-specific deletion disrupts T-cell development and regulatory-T-cell function. Other mechanistically supported substrates/pathways include SHANK3 turnover at excitatory synapses, EPG5/p62-mediated autophagy, Sec31-dependent COPII trafficking, VAMP8-associated cytokinesis, Smoothened/Hedgehog signaling and BRIT1-associated DNA-damage responses. These are biologically important but less central than endosomal receptor sorting to USP8’s primary annotation. (dufner2019ubiquitinspecificprotease8 pages 4-6, dufner2019ubiquitinspecificprotease8 pages 6-7, dufner2019ubiquitinspecificprotease8 pages 7-8, kakihara2021molecularbasisof pages 1-2)

## 6. Cushing disease: strongest human genotype–mechanism relationship

### 6.1 Mutation spectrum and prevalence

Somatic gain-of-function mutations cluster in **exon 14**, particularly around Ser718 and Pro720 in or adjacent to the 14-3-3-binding motif. Ma et al. found variants in **67 of 108 ACTH-secreting adenomas (62.04%)**, but in **0 of 150** other pituitary-adenoma types. Published online February 13, 2015; DOI: https://doi.org/10.1038/cr.2015.20. (ma2015recurrentgainoffunctionusp8 pages 1-2)

Frequency varies substantially between populations and studies. A PRISMA-based 2024 systematic review estimated USP8 variants in **35%** of corticotroph adenomas; approximately **25%** involved codon 720/P720R. The literature range was **11–62%**. Published June 2024 in *BMC Endocrine Disorders*; DOI: https://doi.org/10.1186/s12902-024-01619-z. (hashemimadani2024targetedanalysisof pages 1-2)

### 6.2 Mechanistic chain

The most strongly supported model is:

1. A hotspot mutation reduces phosphorylation-dependent 14-3-3 binding and/or destabilizes the autoinhibited conformation.
2. USP8 undergoes enhanced proteolytic activation and has greater effective DUB activity.
3. EGFR is deubiquitinated, escapes efficient lysosomal down-regulation and is recycled or retained at the cell surface.
4. Sustained EGFR–ERK/MAPK signaling stimulates **POMC transcription**.
5. Increased POMC processing raises ACTH output, driving adrenal cortisol excess. (theodoropoulou2015decodingthegenetic pages 8-10, ma2015recurrentgainoffunctionusp8 pages 7-8, ma2015recurrentgainoffunctionusp8 pages 1-2)

This model has evidence beyond association: mutant tumors show increased POMC and often increased EGFR/ERK signaling; USP8 knockdown lowers EGFR and ACTH in primary mutant tumor cells; and gefitinib reduces ACTH secretion. In the original cohort, mutant tumors were smaller but produced more ACTH per tumor size. Nevertheless, EGFR abundance was not consistently higher in every subsequent cohort, and cytoplasmic or nuclear substrates may contribute. EGFR is therefore a strong functional mediator, not necessarily the sole disease substrate. (dufner2019ubiquitinspecificprotease8 pages 4-6, theodoropoulou2015decodingthegenetic pages 8-10, ma2015recurrentgainoffunctionusp8 pages 7-8)

## 7. Recent developments, 2023–2024

### 7.1 Full-length mechanistic biochemistry

The most important 2024 advance was the purified full-length structure–function analysis showing that USP8 is an extended monomer and that its WW-like module physically competes with ubiquitin in the S1 pocket. The same work connected AMPK phosphorylation at Ser718 to 14-3-3-dependent stabilization of autoinhibition. This moves the field from a largely inferred model to quantitative allosteric biochemistry. (caba2024autoinhibitionofubiquitinspecific pages 1-2, caba2024autoinhibitionofubiquitinspecific pages 4-6)

### 7.2 Expanded corticotroph-tumor phenotyping

A November 2024 cohort found USP8 variants in **18/35 tumors (51%)**. Mutant tumors were more frequently microadenomas (**44% versus 29%; p=0.04**) and recurrent (**44% versus 22%; p=0.0015**). All mutant adenomas were SST5-positive and **73% were SST5+/SST2+**. Transcriptomics of nine mutant and six wild-type tumors suggested altered WNT components and links among USP8, EGFR and somatostatin-receptor trafficking. Because the cohort was small and some genotype–phenotype results differ from previous studies, these observations are hypothesis-generating rather than definitive clinical predictors. DOI: https://doi.org/10.3390/ijms252312886; published November 29, 2024. (nerubenko2024cushing’sdiseasemanifestation pages 1-2)

A companion molecular-dynamics study examined eight variants and found broadly convergent conformational changes, including for selected variants outside the canonical hotspot. This supports an allosteric interpretation but remains computational and requires biochemical validation. DOI: https://doi.org/10.3390/ijms252312697; published November 26, 2024. (petukhova2024usp8mutationsassociated pages 1-2)

### 7.3 Mitophagy and neurodegeneration

The 2023 Drosophila/human-neuron work identified increased Parkin-independent mitophagy following USP8 reduction, suggesting a potential mitochondrial-quality-control strategy for neurodegenerative disease. The evidence is preclinical; no patient benefit or safe long-term therapeutic window has been demonstrated. (mauri2023usp8downregulationpromotes pages 17-19)

## 8. Applications, inhibitors and translational status

### 8.1 Current real-world use

The most immediate application is **molecular stratification of resected corticotroph tumors** by sequencing USP8 exon 14. This can clarify tumor biology and may eventually guide EGFR- or somatostatin-directed therapy, but published genotype–outcome associations remain inconsistent. Transsphenoidal surgery remains standard first-line management; USP8 testing is not itself an approved therapy. The 2024 systematic review reported initial surgical remission rates of approximately **65–85%** and emphasized the unmet need in persistent or recurrent disease. (hashemimadani2024targetedanalysisof pages 1-2)

### 8.2 Direct inhibitors and research tools

Reported compounds/tools include:

- **DUBs-IN-1 and DUBs-IN-2**, indeno-pyrazine derivatives reported near 200–280 nM biochemical potency against USP8 and greater than 100 µM against USP7 in one comparison. They have shown cellular and animal-model activity but have not established clinical safety or efficacy. (mauri2023usp8downregulationpromotes pages 17-19)
- **SJB3-019A**, which inhibited USP8 by 68% in one DUB-array assay but also inhibited multiple other USPs; it is not a selective clinical lead. (takahashi2020ahumandub pages 5-9)
- **UbV8.2/UbV8.2CΔ2**, engineered ubiquitin variants with reported low-nanomolar inhibition—4.8 nM for one construct—but protein delivery and pharmacology limit immediate therapeutic use. (dufner2019ubiquitinspecificprotease8 pages 8-10)
- Broader or less-selective candidates such as RA-9 have shown preclinical effects but cannot be considered validated USP8-specific drugs. (hashemimadani2024targetedanalysisof pages 1-2)

An older review printed DUBs-IN-2 potency as 0.28 mM, whereas later accounts report approximately 200–280 nM; the discrepancy may be typographic or assay-related and should be resolved from original assay data before medicinal-chemistry decisions. (dufner2019ubiquitinspecificprotease8 pages 8-10, mauri2023usp8downregulationpromotes pages 17-19)

### 8.3 Indirect targeting

EGFR inhibitors such as **gefitinib** and lapatinib have suppressed ACTH-related phenotypes in preclinical models or primary cultures. Pasireotide may be relevant where mutant tumors express SST5, but responses can differ among individual USP8 variants; mutation status is not yet a universally validated predictive biomarker. (theodoropoulou2015decodingthegenetic pages 8-10, hashemimadani2024targetedanalysisof pages 1-2, nerubenko2024cushing’sdiseasemanifestation pages 1-2)

No relevant human interventional trial of a selective USP8 inhibitor was found in the clinical-trial search. Direct USP8 inhibition therefore remains **preclinical**. The principal expert concern is therapeutic index: USP8 is essential in several normal tissues and regulates multiple trafficking pathways, so systemic catalytic inhibition could be toxic. Mutation-selective, allosteric, protease-directed, or tissue-targeted strategies may offer better selectivity than blocking the conserved catalytic cysteine. (dufner2019ubiquitinspecificprotease8 pages 8-10)

## 9. Evidence-based functional annotation

The most defensible concise annotation is:

> **USP8 is a cytoplasmic, endosome-recruited USP-family cysteine deubiquitinase that hydrolyzes ubiquitin C-terminal isopeptide bonds on membrane cargo and trafficking machinery. Through MIT–CHMP and SH3-motif–STAM interactions, it regulates ESCRT-dependent receptor sorting, particularly EGFR trafficking, and thereby controls receptor-signal duration. Its catalytic domain has broad Lys-linked ubiquitin-chain activity and is restrained by a cis-acting WW-like domain plus Ser718-phosphorylation-dependent 14-3-3 binding. Somatic mutations disrupting this regulatory module hyperactivate USP8 and drive a substantial subset of ACTH-secreting pituitary tumors through sustained EGFR–ERK–POMC signaling.**

## 10. Main uncertainties

1. **EGFR fate:** receptor deubiquitination is established, but whether it promotes degradation or recycling is context-dependent.
2. **Substrate hierarchy:** numerous proteins are reported as substrates, but direct catalytic evidence is uneven; interaction or stabilization alone does not prove deubiquitination.
3. **Mitophagy direction:** USP8 supports Parkin recruitment yet suppresses a separate Parkin-independent pathway.
4. **Cushing genotype–phenotype prediction:** prevalence is robust, but tumor size, recurrence and drug-response associations vary among cohorts.
5. **Therapeutic maturity:** available inhibitors are preclinical tools or leads, and essential normal functions create a substantial safety challenge.

References

1. (dufner2019ubiquitinspecificprotease8 pages 1-3): Almut Dufner and Klaus-Peter Knobeloch. Ubiquitin-specific protease 8 (usp8/ubpy): a prototypic multidomain deubiquitinating enzyme with pleiotropic functions. Biochemical Society Transactions, 47:1867-1879, Dec 2019. URL: https://doi.org/10.1042/bst20190527, doi:10.1042/bst20190527. This article has 76 citations and is from a peer-reviewed journal.

2. (caba2024autoinhibitionofubiquitinspecific pages 1-2): Cody Caba, Megan Black, Yujue Liu, Ashley A. DaDalt, Josh Mallare, Lixin Fan, Rachel J. Harding, Yun-Xing Wang, Panayiotis O. Vacratsis, Rui Huang, Zhihao Zhuang, and Yufeng Tong. Autoinhibition of ubiquitin-specific protease 8: insights into domain interactions and mechanisms of regulation. Oct 2024. URL: https://doi.org/10.1016/j.jbc.2024.107727, doi:10.1016/j.jbc.2024.107727. This article has 12 citations and is from a domain leading peer-reviewed journal.

3. (petukhova2024usp8mutationsassociated pages 1-2): Natalia Petukhova, Anastasia Poluzerova, Dmitry Bug, Elena Nerubenko, Anna Kostareva, Uliana Tsoy, and Renata Dmitrieva. Usp8 mutations associated with cushing’s disease alter protein structure dynamics. International Journal of Molecular Sciences, 25(23):12697, Nov 2024. URL: https://doi.org/10.3390/ijms252312697, doi:10.3390/ijms252312697. This article has 3 citations.

4. (dufner2019ubiquitinspecificprotease8 pages 3-4): Almut Dufner and Klaus-Peter Knobeloch. Ubiquitin-specific protease 8 (usp8/ubpy): a prototypic multidomain deubiquitinating enzyme with pleiotropic functions. Biochemical Society Transactions, 47:1867-1879, Dec 2019. URL: https://doi.org/10.1042/bst20190527, doi:10.1042/bst20190527. This article has 76 citations and is from a peer-reviewed journal.

5. (kakihara2021molecularbasisof pages 1-2): Keijun Kakihara, Kengo Asamizu, Kei Moritsugu, Masahide Kubo, Tetsuya Kitaguchi, Akinori Endo, Akinori Kidera, Mitsunori Ikeguchi, Akira Kato, Masayuki Komada, and Toshiaki Fukushima. Molecular basis of ubiquitin-specific protease 8 autoinhibition by the ww-like domain. Nov 2021. URL: https://doi.org/10.1038/s42003-021-02802-x, doi:10.1038/s42003-021-02802-x. This article has 26 citations and is from a peer-reviewed journal.

6. (hashemimadani2024targetedanalysisof pages 1-2): Nahid Hashemi-Madani, Sara Cheraghi, Zahra Emami, Ali Zare Mehrjardi, Mahmoud Reza Kaynama, and Mohammad E. Khamseh. Targeted analysis of ubiquitin-specific peptidase (usp8) in a population of iranian people with cushing’s disease and a systematic review of the literature. BMC Endocrine Disorders, Jun 2024. URL: https://doi.org/10.1186/s12902-024-01619-z, doi:10.1186/s12902-024-01619-z. This article has 4 citations and is from a peer-reviewed journal.

7. (ma2015recurrentgainoffunctionusp8 pages 1-2): Zeng-Yi Ma, Zhi-Jian Song, Jian-Hua Chen, Yong-Fei Wang, Shi-Qi Li, Liang-Fu Zhou, Ying Mao, Yi-Ming Li, Rong-Gui Hu, Zhao-Yun Zhang, Hong-Ying Ye, Ming Shen, Xue-Fei Shou, Zhi-Qiang Li, Hong Peng, Qing-Zhong Wang, Dai-Zhan Zhou, Xiao-Lan Qin, Jue Ji, Jie Zheng, Hong Chen, Yin Wang, Dao-Ying Geng, Wei-Jun Tang, Chao-Wei Fu, Zhi-Feng Shi, Yi-Chao Zhang, Zhao Ye, Wen-Qiang He, Qi-Lin Zhang, Qi-Sheng Tang, Rong Xie, Jia-Wei Shen, Zu-Jia Wen, Juan Zhou, Tao Wang, Shan Huang, Hui-Jia Qiu, Ni-Dan Qiao, Yi Zhang, Li Pan, Wei-Min Bao, Ying-Chao Liu, Chuan-Xin Huang, Yong-Yong Shi, and Yao Zhao. Recurrent gain-of-function usp8 mutations in cushing's disease. Cell Research, 25:306-317, Feb 2015. URL: https://doi.org/10.1038/cr.2015.20, doi:10.1038/cr.2015.20. This article has 408 citations and is from a domain leading peer-reviewed journal.

8. (takahashi2020ahumandub pages 5-9): Hirotaka Takahashi, Satoshi Yamanaka, Shohei Kuwada, Kana Higaki, Kohki Kido, Yusuke Sato, Shuya Fukai, Fuminori Tokunaga, and Tatsuya Sawasaki. A human dub protein array for clarification of linkage specificity of polyubiquitin chain and application to evaluation of its inhibitors. Jun 2020. URL: https://doi.org/10.3390/biomedicines8060152, doi:10.3390/biomedicines8060152. This article has 30 citations.

9. (caba2024autoinhibitionofubiquitinspecific pages 4-6): Cody Caba, Megan Black, Yujue Liu, Ashley A. DaDalt, Josh Mallare, Lixin Fan, Rachel J. Harding, Yun-Xing Wang, Panayiotis O. Vacratsis, Rui Huang, Zhihao Zhuang, and Yufeng Tong. Autoinhibition of ubiquitin-specific protease 8: insights into domain interactions and mechanisms of regulation. Oct 2024. URL: https://doi.org/10.1016/j.jbc.2024.107727, doi:10.1016/j.jbc.2024.107727. This article has 12 citations and is from a domain leading peer-reviewed journal.

10. (dufner2019ubiquitinspecificprotease8 pages 4-6): Almut Dufner and Klaus-Peter Knobeloch. Ubiquitin-specific protease 8 (usp8/ubpy): a prototypic multidomain deubiquitinating enzyme with pleiotropic functions. Biochemical Society Transactions, 47:1867-1879, Dec 2019. URL: https://doi.org/10.1042/bst20190527, doi:10.1042/bst20190527. This article has 76 citations and is from a peer-reviewed journal.

11. (dufner2019ubiquitinspecificprotease8 pages 6-7): Almut Dufner and Klaus-Peter Knobeloch. Ubiquitin-specific protease 8 (usp8/ubpy): a prototypic multidomain deubiquitinating enzyme with pleiotropic functions. Biochemical Society Transactions, 47:1867-1879, Dec 2019. URL: https://doi.org/10.1042/bst20190527, doi:10.1042/bst20190527. This article has 76 citations and is from a peer-reviewed journal.

12. (mauri2023usp8downregulationpromotes pages 17-19): Sofia Mauri, Greta Bernardo, Aitor Martinez, Mariavittoria Favaro, Marta Trevisan, Gael Cobraiville, Marianne Fillet, Federico Caicci, Alexander J. Whitworth, and Elena Ziviani. Usp8 down-regulation promotes parkin-independent mitophagy in the drosophila brain and in human neurons. Apr 2023. URL: https://doi.org/10.3390/cells12081143, doi:10.3390/cells12081143. This article has 21 citations.

13. (mauri2023usp8downregulationpromotes pages 19-20): Sofia Mauri, Greta Bernardo, Aitor Martinez, Mariavittoria Favaro, Marta Trevisan, Gael Cobraiville, Marianne Fillet, Federico Caicci, Alexander J. Whitworth, and Elena Ziviani. Usp8 down-regulation promotes parkin-independent mitophagy in the drosophila brain and in human neurons. Apr 2023. URL: https://doi.org/10.3390/cells12081143, doi:10.3390/cells12081143. This article has 21 citations.

14. (theodoropoulou2015decodingthegenetic pages 8-10): Marily Theodoropoulou, Martin Reincke, Martin Fassnacht, and Masayuki Komada. Decoding the genetic basis of cushing's disease: usp8 in the spotlight. European journal of endocrinology, 173 4:M73-83, Oct 2015. URL: https://doi.org/10.1530/eje-15-0320, doi:10.1530/eje-15-0320. This article has 65 citations and is from a highest quality peer-reviewed journal.

15. (ma2015recurrentgainoffunctionusp8 pages 7-8): Zeng-Yi Ma, Zhi-Jian Song, Jian-Hua Chen, Yong-Fei Wang, Shi-Qi Li, Liang-Fu Zhou, Ying Mao, Yi-Ming Li, Rong-Gui Hu, Zhao-Yun Zhang, Hong-Ying Ye, Ming Shen, Xue-Fei Shou, Zhi-Qiang Li, Hong Peng, Qing-Zhong Wang, Dai-Zhan Zhou, Xiao-Lan Qin, Jue Ji, Jie Zheng, Hong Chen, Yin Wang, Dao-Ying Geng, Wei-Jun Tang, Chao-Wei Fu, Zhi-Feng Shi, Yi-Chao Zhang, Zhao Ye, Wen-Qiang He, Qi-Lin Zhang, Qi-Sheng Tang, Rong Xie, Jia-Wei Shen, Zu-Jia Wen, Juan Zhou, Tao Wang, Shan Huang, Hui-Jia Qiu, Ni-Dan Qiao, Yi Zhang, Li Pan, Wei-Min Bao, Ying-Chao Liu, Chuan-Xin Huang, Yong-Yong Shi, and Yao Zhao. Recurrent gain-of-function usp8 mutations in cushing's disease. Cell Research, 25:306-317, Feb 2015. URL: https://doi.org/10.1038/cr.2015.20, doi:10.1038/cr.2015.20. This article has 408 citations and is from a domain leading peer-reviewed journal.

16. (nerubenko2024cushing’sdiseasemanifestation pages 1-2): Elena Nerubenko, Pavel Ryazanov, Natalia Kuritsyna, Artem Paltsev, Oksana Ivanova, Elena Grineva, Anna Kostareva, Renata Dmitrieva, and Uliana Tsoy. Cushing’s disease manifestation in usp8-mutated corticotropinoma may be mediated by interactions between wnt signaling and sst trafficking. International Journal of Molecular Sciences, 25(23):12886, Nov 2024. URL: https://doi.org/10.3390/ijms252312886, doi:10.3390/ijms252312886. This article has 8 citations.

17. (dufner2019ubiquitinspecificprotease8 pages 8-10): Almut Dufner and Klaus-Peter Knobeloch. Ubiquitin-specific protease 8 (usp8/ubpy): a prototypic multidomain deubiquitinating enzyme with pleiotropic functions. Biochemical Society Transactions, 47:1867-1879, Dec 2019. URL: https://doi.org/10.1042/bst20190527, doi:10.1042/bst20190527. This article has 76 citations and is from a peer-reviewed journal.

18. (dufner2019ubiquitinspecificprotease8 pages 7-8): Almut Dufner and Klaus-Peter Knobeloch. Ubiquitin-specific protease 8 (usp8/ubpy): a prototypic multidomain deubiquitinating enzyme with pleiotropic functions. Biochemical Society Transactions, 47:1867-1879, Dec 2019. URL: https://doi.org/10.1042/bst20190527, doi:10.1042/bst20190527. This article has 76 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](USP8-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. takahashi2020ahumandub pages 5-9
2. caba2024autoinhibitionofubiquitinspecific pages 4-6
3. kakihara2021molecularbasisof pages 1-2
4. hashemimadani2024targetedanalysisof pages 1-2
5. caba2024autoinhibitionofubiquitinspecific pages 1-2
6. theodoropoulou2015decodingthegenetic pages 8-10
7. https://doi.org/10.1038/s42003-021-02802-x.
8. https://doi.org/10.1016/j.jbc.2024.107727.
9. https://doi.org/10.3390/cells12081143.
10. https://doi.org/10.1038/cr.2015.20.
11. https://doi.org/10.1186/s12902-024-01619-z.
12. https://doi.org/10.3390/ijms252312886;
13. https://doi.org/10.3390/ijms252312697;
14. https://doi.org/10.1042/bst20190527,
15. https://doi.org/10.1016/j.jbc.2024.107727,
16. https://doi.org/10.3390/ijms252312697,
17. https://doi.org/10.1038/s42003-021-02802-x,
18. https://doi.org/10.1186/s12902-024-01619-z,
19. https://doi.org/10.1038/cr.2015.20,
20. https://doi.org/10.3390/biomedicines8060152,
21. https://doi.org/10.3390/cells12081143,
22. https://doi.org/10.1530/eje-15-0320,
23. https://doi.org/10.3390/ijms252312886,