---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-26T22:37:53.634554'
end_time: '2026-09-26T22:45:20.823312'
duration_seconds: 447.19
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: NEUCR
  gene_id: al-2
  gene_symbol: al-2
  uniprot_accession: P37295
  protein_description: 'RecName: Full=Bifunctional lycopene cyclase/phytoene synthase
    {ECO:0000303|PubMed:11862485}; AltName: Full=Protein albino-2; Includes: RecName:
    Full=Lycopene beta-cyclase {ECO:0000303|PubMed:11862485}; EC=5.5.1.19 {ECO:0000269|PubMed:11862485,
    ECO:0000269|PubMed:16928467}; AltName: Full=Carotene cyclase {ECO:0000303|PubMed:11862485};
    AltName: Full=Lycopene cyclase {ECO:0000303|PubMed:11862485}; Includes: RecName:
    Full=Phytoene synthase {ECO:0000303|PubMed:8163509}; EC=2.5.1.32 {ECO:0000269|PubMed:11862485,
    ECO:0000269|PubMed:16928467};'
  gene_info: Name=al-2 {ECO:0000303|PubMed:8163509}; ORFNames=B22I21.230, NCU00585;
  organism_full: Neurospora crassa (strain ATCC 24698 / 74-OR23-1A / CBS 708.71 /
    DSM 1257 / FGSC 987).
  protein_family: In the C-terminal section; belongs to the phytoene/squalene
  protein_domains: Isoprenoid_synthase_dom_sf. (IPR008949); Lycopene_cyclase_dom.
    (IPR017825); Squ/phyt_synthse. (IPR002060); Squalene/phytoene_synthase_CS. (IPR019845);
    Trans_IPPS_bact-type. (IPR044843)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 28
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: al-2-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** P37295
- **Protein Description:** RecName: Full=Bifunctional lycopene cyclase/phytoene synthase {ECO:0000303|PubMed:11862485}; AltName: Full=Protein albino-2; Includes: RecName: Full=Lycopene beta-cyclase {ECO:0000303|PubMed:11862485}; EC=5.5.1.19 {ECO:0000269|PubMed:11862485, ECO:0000269|PubMed:16928467}; AltName: Full=Carotene cyclase {ECO:0000303|PubMed:11862485}; AltName: Full=Lycopene cyclase {ECO:0000303|PubMed:11862485}; Includes: RecName: Full=Phytoene synthase {ECO:0000303|PubMed:8163509}; EC=2.5.1.32 {ECO:0000269|PubMed:11862485, ECO:0000269|PubMed:16928467};
- **Gene Information:** Name=al-2 {ECO:0000303|PubMed:8163509}; ORFNames=B22I21.230, NCU00585;
- **Organism (full):** Neurospora crassa (strain ATCC 24698 / 74-OR23-1A / CBS 708.71 / DSM 1257 / FGSC 987).
- **Protein Family:** In the C-terminal section; belongs to the phytoene/squalene
- **Key Domains:** Isoprenoid_synthase_dom_sf. (IPR008949); Lycopene_cyclase_dom. (IPR017825); Squ/phyt_synthse. (IPR002060); Squalene/phytoene_synthase_CS. (IPR019845); Trans_IPPS_bact-type. (IPR044843)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "al-2" matches the protein description above**
2. **Verify the organism is correct:** Neurospora crassa (strain ATCC 24698 / 74-OR23-1A / CBS 708.71 / DSM 1257 / FGSC 987).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'al-2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **al-2** (gene ID: al-2, UniProt: P37295) in NEUCR.

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
- **UniProt Accession:** P37295
- **Protein Description:** RecName: Full=Bifunctional lycopene cyclase/phytoene synthase {ECO:0000303|PubMed:11862485}; AltName: Full=Protein albino-2; Includes: RecName: Full=Lycopene beta-cyclase {ECO:0000303|PubMed:11862485}; EC=5.5.1.19 {ECO:0000269|PubMed:11862485, ECO:0000269|PubMed:16928467}; AltName: Full=Carotene cyclase {ECO:0000303|PubMed:11862485}; AltName: Full=Lycopene cyclase {ECO:0000303|PubMed:11862485}; Includes: RecName: Full=Phytoene synthase {ECO:0000303|PubMed:8163509}; EC=2.5.1.32 {ECO:0000269|PubMed:11862485, ECO:0000269|PubMed:16928467};
- **Gene Information:** Name=al-2 {ECO:0000303|PubMed:8163509}; ORFNames=B22I21.230, NCU00585;
- **Organism (full):** Neurospora crassa (strain ATCC 24698 / 74-OR23-1A / CBS 708.71 / DSM 1257 / FGSC 987).
- **Protein Family:** In the C-terminal section; belongs to the phytoene/squalene
- **Key Domains:** Isoprenoid_synthase_dom_sf. (IPR008949); Lycopene_cyclase_dom. (IPR017825); Squ/phyt_synthse. (IPR002060); Squalene/phytoene_synthase_CS. (IPR019845); Trans_IPPS_bact-type. (IPR044843)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "al-2" matches the protein description above**
2. **Verify the organism is correct:** Neurospora crassa (strain ATCC 24698 / 74-OR23-1A / CBS 708.71 / DSM 1257 / FGSC 987).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'al-2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **al-2** (gene ID: al-2, UniProt: P37295) in NEUCR.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Neurospora crassa* **al-2** / AL-2

## Executive conclusion

The target is correctly identified as ***Neurospora crassa* al-2**, locus **NCU00585**, encoding UniProt **P37295**, a **bifunctional phytoene synthase/lycopene β-cyclase** in fungal carotenoid biosynthesis. It is not *al-1*: *al-1*/NCU00552 encodes the distinct phytoene desaturase. This distinction is supported by primary genetics, biochemical assays, and modern reviews; publications or database-derived text reversing those assignments should be treated as annotation errors. The organism specified by the supplied UniProt record—*N. crassa* strain ATCC 24698/74-OR23-1A/CBS 708.71/DSM 1257/FGSC 987—is therefore consistent with the requested target, although most experimental papers identify the species or FGSC mutant strains rather than restating every reference-strain synonym. (diazsanchez2011analysisofal2 pages 10-11, strobel2009carotenoidsandcarotenogenic pages 1-2, sandmann2022carotenoidsandtheir pages 2-4, smith2010transcriptionfactorsin pages 4-5)

AL-2 performs two pathway-defining reactions: its C-terminal phytoene-synthase region condenses two geranylgeranyl diphosphate molecules into phytoene, while its N-terminal cyclase region introduces β-ionone rings into desaturated carotenoids. Direct heterologous assays demonstrated conversion of lycopene into γ-carotene and β-carotene. In native *Neurospora*, the enzyme helps direct flux through torulene and related intermediates toward the orange C35 apocarotenoid neurosporaxanthin. (diazsanchez2011analysisofal2 pages 1-2, diazsanchez2011analysisofal2 pages 6-8, sandmann2022carotenoidsandtheir pages 2-4)

| Topic | Conclusion | Evidence type / strength | Key source with DOI / date |
|---|---|---|---|
| Identity and disambiguation | **AL-2 = al-2 = NCU00585 = UniProt P37295**, the bifunctional phytoene synthase/lycopene cyclase of *Neurospora crassa*. It is not AL-1: **al-1/NCU00552 encodes phytoene desaturase**. Reports reversing these assignments are annotation errors. | **High:** consistent locus mapping, primary genetics, and biochemical literature | Díaz-Sánchez et al., DOI [10.1371/journal.pone.0021948](https://doi.org/10.1371/journal.pone.0021948), 19 Jul 2011; Strobel et al., DOI [10.1007/s00294-009-0235-0](https://doi.org/10.1007/s00294-009-0235-0), 10 Mar 2009 (diazsanchez2011analysisofal2 pages 1-2, diazsanchez2011analysisofal2 pages 10-11, strobel2009carotenoidsandcarotenogenic pages 1-2, smith2010transcriptionfactorsin pages 4-5) |
| Phytoene-synthase reaction | The C-terminal activity condenses **2 geranylgeranyl diphosphate (GGPP; C20)** molecules to the C40 carotene **15-cis-phytoene**, releasing diphosphate; conserved regions implicated in substrate–Mg²⁺ binding occur in the synthase domain. | **High for substrate/product and genetic assignment; moderate for AL-2-specific cofactor mechanism:** direct pathway genetics plus conserved catalytic-site analysis | Díaz-Sánchez et al., DOI [10.1371/journal.pone.0021948](https://doi.org/10.1371/journal.pone.0021948), 19 Jul 2011; Sandmann, DOI [10.3390/molecules27041431](https://doi.org/10.3390/molecules27041431), Feb 2022 (diazsanchez2011analysisofal2 pages 1-2, diazsanchez2011analysisofal2 pages 5-6, sandmann2022carotenoidsandtheir pages 2-4) |
| Lycopene β-cyclase reaction | The N-terminal activity cyclizes a ψ-end of **lycopene** to a β-ionone ring. In a lycopene-producing *E. coli* assay, wild-type AL-2 formed **γ-carotene** (one ring) and **β-carotene** (two rings), directly demonstrating cyclase activity. In the native pathway it also cyclizes 3,4-didehydrolycopene to torulene and can act on apo-4′-lycopenoid intermediates, although the broader substrate range is less completely quantified. | **High for lycopene → γ-/β-carotene:** heterologous functional assay; **moderate for native alternative substrates:** metabolite/genetic pathway evidence | Díaz-Sánchez et al., DOI [10.1371/journal.pone.0021948](https://doi.org/10.1371/journal.pone.0021948), 19 Jul 2011; Sandmann, DOI [10.3390/molecules27041431](https://doi.org/10.3390/molecules27041431), Feb 2022 (diazsanchez2011analysisofal2 pages 6-8, sandmann2022carotenoidsandtheir pages 2-4) |
| Domain architecture | The 2011 study models a **602-aa** bifunctional polypeptide: hydrophobic **N-terminal residues 1–244** form the cyclase region, while the **remaining 358 residues** form the more hydrophilic C-terminal phytoene-synthase region. Conserved synthase catalytic residues span approximately residues 297–556. | **High:** sequence analysis supported by domain-specific mutations and functional assays | Díaz-Sánchez et al., DOI [10.1371/journal.pone.0021948](https://doi.org/10.1371/journal.pone.0021948), 19 Jul 2011 (diazsanchez2011analysisofal2 pages 2-4, diazsanchez2011analysisofal2 pages 4-5, diazsanchez2011analysisofal2 pages 5-6) |
| Pathway role | AL-2 performs two early/branch-forming reactions in the light-inducible carotenoid pathway: **GGPP → phytoene**, followed after AL-1-mediated desaturation by cyclization toward γ-carotene/torulene. CAO-2 then cleaves carotenoids and YLO-1 oxidizes the resulting aldehyde to the orange C35 apocarotenoid **neurosporaxanthin**. | **High:** pathway mutants, metabolite identification, and functional enzyme assays | Díaz-Sánchez et al., DOI [10.1371/journal.pone.0021948](https://doi.org/10.1371/journal.pone.0021948), 19 Jul 2011; Sandmann, DOI [10.3390/molecules27041431](https://doi.org/10.3390/molecules27041431), Feb 2022 (diazsanchez2011analysisofal2 pages 1-2, sandmann2022carotenoidsandtheir pages 2-4, sandmann2022carotenoidsandtheir pages 4-6) |
| Direct light regulation | Light-activated **White Collar Complex (WC-1/WC-2)** binds near the NCU00584/NCU00585 promoter region. WCC ChIP-seq detected a peak with **200 reads and z = 10.72** after 8 min of light; prior array data reported **5.1-fold al-2 induction after 45 min**, supporting direct phototranscriptional control. | **High:** direct ChIP-seq occupancy plus light-responsive transcript data | Smith et al., DOI [10.1128/EC.00154-10](https://doi.org/10.1128/EC.00154-10), published online 30 Jul 2010 / issue Oct 2010 (smith2010transcriptionfactorsin pages 4-5, smith2010transcriptionfactorsin pages 1-2) |
| Mutant evidence | Nine classical al-2 alleles separated the two functions: eight albino alleles mainly damaged the synthase region, whereas reddish mutant **#2666** disrupted cyclization and accumulated apo-4′-lycopenoic acid. #2666 retained about **30% of wild-type carotenoids at 8°C and 60% at 30°C**; leaky alleles produced roughly **5–13 mg carotenoid g⁻¹ dry weight**. Some C-terminal truncations also altered cyclase activity, indicating interdomain coupling. | **High:** allele sequencing, pigmentation, HPLC/absorption spectra, expression assays, and heterologous complementation | Díaz-Sánchez et al., DOI [10.1371/journal.pone.0021948](https://doi.org/10.1371/journal.pone.0021948), 19 Jul 2011 (diazsanchez2011analysisofal2 pages 2-4, diazsanchez2011analysisofal2 pages 4-5, diazsanchez2011analysisofal2 pages 6-8, diazsanchez2011analysisofal2 pages 5-6) |
| Native subcellular localization | **No direct native AL-2 localization study was identified**: the available work reports neither tagged-protein microscopy nor Neurospora cell fractionation. The hydrophobic N-terminal cyclase region suggests membrane association, but this is an inference—not proof of a particular membrane or organelle in *N. crassa*. | **Unresolved / low:** sequence-based inference only | Díaz-Sánchez et al., DOI [10.1371/journal.pone.0021948](https://doi.org/10.1371/journal.pone.0021948), 19 Jul 2011 (diazsanchez2011analysisofal2 pages 6-8, diazsanchez2011analysisofal2 pages 4-5, diazsanchez2011analysisofal2 pages 2-4, diazsanchez2011analysisofal2 pages 8-9) |
| Comparative localization evidence | In *Blakeslea trispora*, homologous fungal phytoene-synthase and cyclase regions were detected as a soluble synthase and membrane-bound cyclase, possibly after post-translational cleavage. This is useful comparative context but **must not be presented as direct localization or cleavage evidence for Neurospora AL-2**. | **Comparative only:** evidence from a different fungal protein/system | Sandmann, DOI [10.3390/molecules27041431](https://doi.org/10.3390/molecules27041431), Feb 2022 (sandmann2022carotenoidsandtheir pages 2-4) |
| Developmental expression | Transcriptome integration assigned NCU00585 to predicted secondary-metabolic cluster 1. During conidial germination on Bird medium at 25°C and 37°C, most cluster genes were downregulated before germ-tube emergence and slightly upregulated during extension; al-2 and al-3 knockouts showed asexual-growth/conidiation phenotypes. | **Moderate:** multi-experiment transcriptomic reanalysis and knockout-phenotype integration, not direct catalytic analysis | Wang et al., DOI [10.1128/msystems.00232-22](https://doi.org/10.1128/msystems.00232-22), published 31 May 2022 (wang2022secondarymetabolismgene pages 8-10, wang2022secondarymetabolismgene pages 1-2) |
| Biotechnology applications | AL-2-type bifunctional enzymes provide compact two-activity modules for carotenoid engineering. Direct use of *N. crassa* al-2 in *Podospora anserina* pathway engineering contributed to up to **eightfold** higher carotenoid production, and every al-2-overexpressing transformant examined showed mycelial lifespan extension of up to **31%**. More broadly, fungal **crtYB homologs** have enabled engineered β-carotene production, but those yields are comparative—not direct AL-2 performance data. | **Moderate-to-high for Podospora application; comparative for other CrtYB cell factories** | Strobel et al., DOI [10.1007/s00294-009-0235-0](https://doi.org/10.1007/s00294-009-0235-0), 10 Mar 2009; Sandmann, DOI [10.3390/molecules27041431](https://doi.org/10.3390/molecules27041431), Feb 2022 (strobel2009carotenoidsandcarotenogenic pages 1-2, sandmann2022carotenoidsandtheir pages 10-11) |


*Table: Evidence-graded annotation of AL-2 identity, catalytic activities, pathway placement, regulation, localization limits, developmental expression, and engineering relevance. Direct Neurospora findings are distinguished from comparative results obtained with fungal homologs.*

## 1. Identity and domain-family verification

The historical designation “albino-2” reflects the pale or albino phenotype of many loss-of-function mutants. The strongest mapping is:

- **Gene:** *al-2*
- **Genome locus:** NCU00585
- **Protein:** AL-2, bifunctional lycopene cyclase/phytoene synthase
- **UniProt accession:** P37295
- **Organism:** *Neurospora crassa*
- **Distinct neighboring pathway genes:** *al-1*/NCU00552, phytoene desaturase; *al-3*, geranylgeranyl-diphosphate synthase. (diazsanchez2011analysisofal2 pages 10-11, strobel2009carotenoidsandcarotenogenic pages 1-2, wang2022secondarymetabolismgene pages 8-10, smith2010transcriptionfactorsin pages 4-5)

The 2011 sequence and mutational analysis described AL-2 as a 602-residue polypeptide with an N-terminal cyclase region spanning approximately residues 1–244 and a C-terminal phytoene-synthase region comprising the remaining 358 residues. Conserved synthase catalytic residues lie broadly within residues 297–556, including motifs implicated in substrate–Mg²⁺ interactions. This experimentally supported organization agrees with the supplied InterPro-type assignments: Lycopene_cyclase_dom at the N terminus and squalene/phytoene-synthase or isoprenoid-synthase-related domains toward the C terminus. (diazsanchez2011analysisofal2 pages 4-5, diazsanchez2011analysisofal2 pages 5-6)

The architecture is characteristic of fungal AL-2/CrtYB/CarRA proteins. It fuses two activities that are commonly encoded by separate enzymes in bacteria and plants. The cyclase region is comparatively hydrophobic; the synthase region is more hydrophilic. Mutations or truncations in one region can affect the other activity, indicating that the domains are chemically distinguishable but not always structurally independent. (diazsanchez2011analysisofal2 pages 2-4, diazsanchez2011analysisofal2 pages 6-8)

## 2. Primary biochemical function

### 2.1 Phytoene synthase activity

AL-2 catalyzes condensation of two C20 geranylgeranyl diphosphate molecules to produce the C40 carotenoid precursor phytoene:

**2 GGPP → phytoene + diphosphate products**

This is the committed carotenoid-forming step downstream of the general isoprenoid pathway. In *N. crassa*, GGPP is supplied by AL-3. The literature directly establishes the substrate and phytoene product through genetic assignment, pathway metabolites, conserved catalytic motifs, and mutant phenotypes. Conserved Mg²⁺-binding regions support a divalent-cation-assisted prenyl-condensation mechanism, although a purified-enzyme kinetic characterization of native AL-2 was not identified in the retrieved literature. (diazsanchez2011analysisofal2 pages 1-2, diazsanchez2011analysisofal2 pages 5-6, sandmann2022carotenoidsandtheir pages 2-4)

### 2.2 Lycopene β-cyclase activity and substrate specificity

The N-terminal activity cyclizes the ψ-end of lycopene to form a β-ionone ring. In engineered lycopene-producing *Escherichia coli*, wild-type AL-2 generated both **γ-carotene**, representing one cyclization, and **β-carotene**, representing cyclization at both ends. This is direct functional evidence that AL-2 itself possesses lycopene β-cyclase activity rather than merely regulating another cyclase. (diazsanchez2011analysisofal2 pages 6-8)

Its native physiological chemistry is more branched than the simple lycopene-to-β-carotene assay. *N. crassa* AL-1 can introduce a fifth desaturation at one end of lycopene, producing 3,4-didehydrolycopene; that modified end cannot undergo ordinary β-cyclization, so AL-2 cyclization of the other end produces monocyclic torulene. Metabolite evidence further indicates cyclization of apo-4′-lycopenoid intermediates in alternative late routes to neurosporaxanthin. These native alternative substrates are supported by mutant metabolite profiles, but their relative catalytic efficiencies and a complete purified-enzyme substrate panel remain unavailable. (sandmann2022carotenoidsandtheir pages 2-4, sandmann2022carotenoidsandtheir pages 4-6, diazsanchez2011analysisofal2 pages 4-5)

The available evidence also suggests selectivity against structurally different C30 carotenoids: diapolycopene detected at trace levels in AL-2-null backgrounds was proposed not to be recognized by the AL-2 cyclase. This is a pathway inference rather than a direct kinetic specificity measurement. (diazsanchez2011analysisofal2 pages 4-5)

## 3. Position in neurosporaxanthin biosynthesis

The best-supported pathway sequence is:

1. **AL-3:** generates GGPP.
2. **AL-2 phytoene-synthase domain:** 2 GGPP → phytoene.
3. **AL-1:** performs multiple desaturations, producing lycopene and, through a fifth desaturation, 3,4-didehydrolycopene.
4. **AL-2 cyclase domain:** cyclizes suitable ψ-ends, producing γ-/β-carotene in the standard assay and torulene in the native monocyclic branch.
5. **CAO-2:** oxidatively cleaves torulene or related substrates to C35 apocarotenals.
6. **YLO-1:** oxidizes the aldehyde to **neurosporaxanthin**, chemically 4′-apo-β,ψ-caroten-4′-oate. (diazsanchez2011analysisofal2 pages 1-2, strobel2009carotenoidsandcarotenogenic pages 1-2, sandmann2022carotenoidsandtheir pages 2-4)

Current expert interpretation allows parallel orders for the late reactions. In one route, 3,4-didehydrolycopene is cleaved and the apo-4′-lycopenoid is subsequently cyclized; in another, AL-2 first forms torulene, which is then cleaved. Both routes can converge on neurosporaxanthin after aldehyde oxidation. Thus, AL-2 is not merely an entry-point synthase: its cyclase activity also controls the topology and identity of downstream colored carotenoids. (sandmann2022carotenoidsandtheir pages 2-4, sandmann2022carotenoidsandtheir pages 4-6)

## 4. Experimental genetic and biochemical evidence

The most precise allele study examined nine classical *al-2* mutants. Eight albino strains carried lesions predominantly affecting the phytoene-synthase region, consistent with failure at the pathway’s first carotenoid-specific step. The reddish mutant #2666 carried a cyclase-region defect and accumulated apo-4′-lycopenoic acid, demonstrating that synthase/desaturation chemistry could continue while cyclization was impaired. (diazsanchez2011analysisofal2 pages 2-4, diazsanchez2011analysisofal2 pages 1-2)

Quantitatively, #2666 retained approximately **30% of wild-type carotenoid production at 8°C and 60% at 30°C**. Several leaky pale alleles retained approximately **5–13 mg carotenoid per gram dry weight** under the reported assay conditions. Wild type produced more carotenoid at 8°C than at 30°C, with neurosporaxanthin dominating at low temperature. These results demonstrate both residual allele-specific activity and strong environmental modulation of pathway output. (diazsanchez2011analysisofal2 pages 2-4)

Domain interdependence was also evident. One protein retaining only about 20% of its synthase region still showed substantial cyclase activity, whereas another C-terminally altered protein lost detectable cyclase activity despite retaining an apparently intact N-terminal cyclase region. Cyclase-domain substitutions likewise differed in their effects on phytoene synthesis. The fused architecture may therefore promote stability, folding, or metabolic coupling rather than behaving as two completely autonomous modules. (diazsanchez2011analysisofal2 pages 1-2, diazsanchez2011analysisofal2 pages 6-8, diazsanchez2011analysisofal2 pages 5-6)

## 5. Localization: what is known and what remains unresolved

No direct study was found that localizes native AL-2 in *N. crassa* by fluorescent tagging, immunomicroscopy, membrane fractionation, or organelle purification. A precise statement such as “ER-localized,” “mitochondrial,” or “cytosolic” would therefore exceed the evidence. (diazsanchez2011analysisofal2 pages 6-8, diazsanchez2011analysisofal2 pages 4-5, diazsanchez2011analysisofal2 pages 8-9)

The hydrophobic N-terminal cyclase region makes membrane association plausible, whereas the C-terminal synthase region is more hydrophilic. In another fungus, *Blakeslea trispora*, homologous activities were detected as a soluble synthase and membrane-bound cyclase, potentially following proteolytic processing. This is useful comparative evidence for how fungal fusion proteins may be organized, but it is not evidence that *N. crassa* AL-2 is cleaved or occupies the same compartment. The conservative annotation is therefore: **intracellular carotenoid-pathway enzyme, likely associated at least transiently with lipid/membrane environments, but native subcellular compartment unverified**. (sandmann2022carotenoidsandtheir pages 2-4, diazsanchez2011analysisofal2 pages 2-4)

## 6. Regulation and signaling context

### Blue-light control

AL-2 operates in one of the canonical outputs of *Neurospora* blue-light signaling. WC-1 and WC-2 form the White Collar Complex (WCC), which combines photoreceptor and transcription-factor functions. Genome-wide ChIP-seq detected WCC occupancy near the NCU00584/NCU00585 promoter region after 8 minutes of illumination: the reported peak contained **200 reads with z = 10.72**. Corresponding array data reported approximately **5.1-fold induction of *al-2* after 45 minutes**. This combination of promoter occupancy and transcript induction strongly supports direct WCC regulation rather than an exclusively indirect response. (smith2010transcriptionfactorsin pages 4-5, smith2010transcriptionfactorsin pages 1-2)

Mutant analysis found that *al-2* photoinduction itself was reduced approximately two- to fourfold in several *al-2* mutants, whereas *al-1* induction was largely unaffected. Proposed explanations included altered mutant-mRNA stability or feedback associated with AL-2 activity; neither mechanism was conclusively demonstrated. (diazsanchez2011analysisofal2 pages 6-8)

### Developmental and environmental expression

A 2022 analysis integrated nine transcriptomic experiments and identified 20 predicted secondary-metabolic clusters containing 177 genes. NCU00585 was placed in cluster 1 with nearby genes including *ncw-6* and *os-5*. During conidial germination on Bird medium at 25°C and 37°C, most genes in this region were downregulated before germ-tube emergence and then slightly upregulated during extension. Among 126 cluster genes assessed for knockout phenotypes, *al-2* and *al-3* showed phenotypes related to asexual growth and conidiation. This does not redefine AL-2 as a signaling protein; rather, it shows that carotenoid metabolism is integrated with developmental and environmental programs. (wang2022secondarymetabolismgene pages 8-10, wang2022secondarymetabolismgene pages 1-2)

A targeted 2023–2024 search identified emerging work on CRZ-1 regulation of carotenoid-gene promoters and use of a reconstructed *Neurospora* carotenoid pathway in plants. However, full-text evidence for those papers was not available in the retrieved corpus, so detailed mechanistic or quantitative claims from them are not used here. The core functional annotation remains based on direct AL-2 genetics, metabolite analyses, heterologous assays, WCC ChIP-seq, and the 2022 synthesis of fungal carotenoid biochemistry.

## 7. Biological role

The immediate role of AL-2 is biosynthetic: it establishes the carotenoid backbone and then determines ring formation. The visible orange pigmentation of wild-type *N. crassa* and albino/reddish colors of pathway mutants are direct phenotypic readouts. Fungal carotenoids are generally interpreted as photoprotective and antioxidant secondary metabolites, but for AL-2 specifically the strongest evidence concerns pigment synthesis rather than a quantified survival advantage under a defined oxidative stress. Its developmental phenotypes likely reflect carotenoid loss, pathway regulation, or linked developmental programs and should not be interpreted as proof that AL-2 itself is a structural conidiation factor. (diazsanchez2011analysisofal2 pages 2-4, wang2022secondarymetabolismgene pages 1-2)

## 8. Applications and real-world implementation

The fusion of two activities into one protein makes AL-2-type enzymes attractive metabolic-engineering modules. In *Podospora anserina*, manipulation of homologous carotenoid genes corresponding to *N. crassa al-1*, *al-2*, and *al-3* increased carotenoid production by as much as **eightfold**. Every examined transformant overexpressing *al-2* showed mycelial lifespan extension, reaching **up to 31%**. This connects pathway engineering to a measurable physiological outcome, although it was obtained in *P. anserina*, not in the reference *N. crassa* strain. (strobel2009carotenoidsandcarotenogenic pages 1-2)

More broadly, fungal CrtYB homologs are used in engineered yeasts to produce β-carotene and downstream xanthophylls. A 2022 review reported, for example, 12.5 mg/g dry weight β-carotene from an engineered *Yarrowia lipolytica* pathway containing a bifunctional *crtYB*, while optimized fermentation systems reached substantially higher β-carotene concentrations through additional pathway and storage engineering. These figures demonstrate the industrial relevance of the enzyme class, not the isolated productivity of P37295 itself. (sandmann2022carotenoidsandtheir pages 10-11)

The principal application opportunities for AL-2 are therefore:

- compact construction of fungal or heterologous carotenoid pathways;
- control of monocyclic versus bicyclic carotenoid output through cyclase/desaturase balance;
- production of neurosporaxanthin or specialized apo-/keto-/hydroxy-carotenoid precursors;
- use of pigmentation as a visible reporter for pathway activity or genetic manipulation.

## 9. Evidence-based annotation and remaining gaps

A defensible current annotation is:

> **AL-2 (P37295; NCU00585) is a 602-aa fungal bifunctional carotenoid enzyme whose C-terminal phytoene-synthase domain condenses two GGPP molecules to phytoene and whose hydrophobic N-terminal lycopene β-cyclase domain cyclizes desaturated carotenoid ψ-ends. It functions in the light-inducible pathway leading through torulene and apocarotenals to neurosporaxanthin.**

Confidence is **high** for identity, the two catalytic activities, domain orientation, pathway position, and direct WCC-dependent light regulation. Confidence is **moderate** for the complete native substrate range and interdomain mechanism. Native subcellular localization, oligomeric state, purified kinetic constants, exact cofactor requirements beyond conserved Mg²⁺-binding features, and possible proteolytic processing remain unresolved.

## Key sources

1. Díaz-Sánchez V. et al. “Analysis of *al-2* Mutations in *Neurospora*.” *PLoS ONE* 6:e21948. Published **19 July 2011**. DOI/URL: https://doi.org/10.1371/journal.pone.0021948. (diazsanchez2011analysisofal2 pages 1-2)
2. Sandmann G. “Carotenoids and Their Biosynthesis in Fungi.” *Molecules* 27:1431. Published **February 2022**. DOI/URL: https://doi.org/10.3390/molecules27041431. (sandmann2022carotenoidsandtheir pages 2-4)
3. Smith K.M. et al. “Transcription Factors in Light and Circadian Clock Signaling Networks Revealed by Genomewide Mapping of Direct Targets for Neurospora White Collar Complex.” *Eukaryotic Cell* 9:1549–1556. Published online **30 July 2010**; issue date October 2010. DOI/URL: https://doi.org/10.1128/EC.00154-10. (smith2010transcriptionfactorsin pages 4-5, smith2010transcriptionfactorsin pages 1-2)
4. Wang Z. et al. “Secondary Metabolism Gene Clusters Exhibit Increasingly Dynamic and Differential Expression during Asexual Growth, Conidiation, and Sexual Development in *Neurospora crassa*.” *mSystems* 7. Published **31 May 2022**. DOI/URL: https://doi.org/10.1128/msystems.00232-22. (wang2022secondarymetabolismgene pages 8-10, wang2022secondarymetabolismgene pages 1-2)
5. Strobel I. et al. “Carotenoids and carotenogenic genes in *Podospora anserina*: engineering of the carotenoid composition extends the life span of the mycelium.” *Current Genetics* 55:175–184. Published online **10 March 2009**. DOI/URL: https://doi.org/10.1007/s00294-009-0235-0. (strobel2009carotenoidsandcarotenogenic pages 1-2)

References

1. (diazsanchez2011analysisofal2 pages 10-11): Violeta Díaz-Sánchez, Alejandro F. Estrada, Danika Trautmann, M. Carmen Limón, Salim Al-Babili, and Javier Avalos. Analysis of al-2 mutations in neurospora. PLoS ONE, 6:e21948, Jul 2011. URL: https://doi.org/10.1371/journal.pone.0021948, doi:10.1371/journal.pone.0021948. This article has 35 citations and is from a peer-reviewed journal.

2. (strobel2009carotenoidsandcarotenogenic pages 1-2): Ingmar Strobel, Jürgen Breitenbach, Christian Q. Scheckhuber, Heinz D. Osiewacz, and Gerhard Sandmann. Carotenoids and carotenogenic genes in podospora anserina: engineering of the carotenoid composition extends the life span of the mycelium. Current Genetics, 55:175-184, Mar 2009. URL: https://doi.org/10.1007/s00294-009-0235-0, doi:10.1007/s00294-009-0235-0. This article has 38 citations and is from a peer-reviewed journal.

3. (sandmann2022carotenoidsandtheir pages 2-4): Gerhard Sandmann. Carotenoids and their biosynthesis in fungi. Molecules, 27:1431, Feb 2022. URL: https://doi.org/10.3390/molecules27041431, doi:10.3390/molecules27041431. This article has 121 citations.

4. (smith2010transcriptionfactorsin pages 4-5): Kristina M. Smith, Gencer Sancar, Rigzin Dekhang, Christopher M. Sullivan, Shaojie Li, Andrew G. Tag, Cigdem Sancar, Erin L. Bredeweg, Henry D. Priest, Ryan F. McCormick, Terry L. Thomas, James C. Carrington, Jason E. Stajich, Deborah Bell-Pedersen, Michael Brunner, and Michael Freitag. Transcription factors in light and circadian clock signaling networks revealed by genomewide mapping of direct targets for neurospora white collar complex. Oct 2010. URL: https://doi.org/10.1128/ec.00154-10, doi:10.1128/ec.00154-10. This article has 275 citations and is from a peer-reviewed journal.

5. (diazsanchez2011analysisofal2 pages 1-2): Violeta Díaz-Sánchez, Alejandro F. Estrada, Danika Trautmann, M. Carmen Limón, Salim Al-Babili, and Javier Avalos. Analysis of al-2 mutations in neurospora. PLoS ONE, 6:e21948, Jul 2011. URL: https://doi.org/10.1371/journal.pone.0021948, doi:10.1371/journal.pone.0021948. This article has 35 citations and is from a peer-reviewed journal.

6. (diazsanchez2011analysisofal2 pages 6-8): Violeta Díaz-Sánchez, Alejandro F. Estrada, Danika Trautmann, M. Carmen Limón, Salim Al-Babili, and Javier Avalos. Analysis of al-2 mutations in neurospora. PLoS ONE, 6:e21948, Jul 2011. URL: https://doi.org/10.1371/journal.pone.0021948, doi:10.1371/journal.pone.0021948. This article has 35 citations and is from a peer-reviewed journal.

7. (diazsanchez2011analysisofal2 pages 5-6): Violeta Díaz-Sánchez, Alejandro F. Estrada, Danika Trautmann, M. Carmen Limón, Salim Al-Babili, and Javier Avalos. Analysis of al-2 mutations in neurospora. PLoS ONE, 6:e21948, Jul 2011. URL: https://doi.org/10.1371/journal.pone.0021948, doi:10.1371/journal.pone.0021948. This article has 35 citations and is from a peer-reviewed journal.

8. (diazsanchez2011analysisofal2 pages 2-4): Violeta Díaz-Sánchez, Alejandro F. Estrada, Danika Trautmann, M. Carmen Limón, Salim Al-Babili, and Javier Avalos. Analysis of al-2 mutations in neurospora. PLoS ONE, 6:e21948, Jul 2011. URL: https://doi.org/10.1371/journal.pone.0021948, doi:10.1371/journal.pone.0021948. This article has 35 citations and is from a peer-reviewed journal.

9. (diazsanchez2011analysisofal2 pages 4-5): Violeta Díaz-Sánchez, Alejandro F. Estrada, Danika Trautmann, M. Carmen Limón, Salim Al-Babili, and Javier Avalos. Analysis of al-2 mutations in neurospora. PLoS ONE, 6:e21948, Jul 2011. URL: https://doi.org/10.1371/journal.pone.0021948, doi:10.1371/journal.pone.0021948. This article has 35 citations and is from a peer-reviewed journal.

10. (sandmann2022carotenoidsandtheir pages 4-6): Gerhard Sandmann. Carotenoids and their biosynthesis in fungi. Molecules, 27:1431, Feb 2022. URL: https://doi.org/10.3390/molecules27041431, doi:10.3390/molecules27041431. This article has 121 citations.

11. (smith2010transcriptionfactorsin pages 1-2): Kristina M. Smith, Gencer Sancar, Rigzin Dekhang, Christopher M. Sullivan, Shaojie Li, Andrew G. Tag, Cigdem Sancar, Erin L. Bredeweg, Henry D. Priest, Ryan F. McCormick, Terry L. Thomas, James C. Carrington, Jason E. Stajich, Deborah Bell-Pedersen, Michael Brunner, and Michael Freitag. Transcription factors in light and circadian clock signaling networks revealed by genomewide mapping of direct targets for neurospora white collar complex. Oct 2010. URL: https://doi.org/10.1128/ec.00154-10, doi:10.1128/ec.00154-10. This article has 275 citations and is from a peer-reviewed journal.

12. (diazsanchez2011analysisofal2 pages 8-9): Violeta Díaz-Sánchez, Alejandro F. Estrada, Danika Trautmann, M. Carmen Limón, Salim Al-Babili, and Javier Avalos. Analysis of al-2 mutations in neurospora. PLoS ONE, 6:e21948, Jul 2011. URL: https://doi.org/10.1371/journal.pone.0021948, doi:10.1371/journal.pone.0021948. This article has 35 citations and is from a peer-reviewed journal.

13. (wang2022secondarymetabolismgene pages 8-10): Zheng Wang, Francesc Lopez-Giraldez, Jason Slot, Oded Yarden, Frances Trail, and Jeffrey P. Townsend. Secondary metabolism gene clusters exhibit increasingly dynamic and differential expression during asexual growth, conidiation, and sexual development in neurospora crassa. Jun 2022. URL: https://doi.org/10.1128/msystems.00232-22, doi:10.1128/msystems.00232-22. This article has 19 citations and is from a peer-reviewed journal.

14. (wang2022secondarymetabolismgene pages 1-2): Zheng Wang, Francesc Lopez-Giraldez, Jason Slot, Oded Yarden, Frances Trail, and Jeffrey P. Townsend. Secondary metabolism gene clusters exhibit increasingly dynamic and differential expression during asexual growth, conidiation, and sexual development in neurospora crassa. Jun 2022. URL: https://doi.org/10.1128/msystems.00232-22, doi:10.1128/msystems.00232-22. This article has 19 citations and is from a peer-reviewed journal.

15. (sandmann2022carotenoidsandtheir pages 10-11): Gerhard Sandmann. Carotenoids and their biosynthesis in fungi. Molecules, 27:1431, Feb 2022. URL: https://doi.org/10.3390/molecules27041431, doi:10.3390/molecules27041431. This article has 121 citations.

## Artifacts

- [Edison artifact artifact-00](al-2-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. sandmann2022carotenoidsandtheir pages 2-4
2. strobel2009carotenoidsandcarotenogenic pages 1-2
3. sandmann2022carotenoidsandtheir pages 10-11
4. smith2010transcriptionfactorsin pages 4-5
5. sandmann2022carotenoidsandtheir pages 4-6
6. smith2010transcriptionfactorsin pages 1-2
7. wang2022secondarymetabolismgene pages 8-10
8. wang2022secondarymetabolismgene pages 1-2
9. 10.1371/journal.pone.0021948
10. 10.1007/s00294-009-0235-0
11. 10.3390/molecules27041431
12. 10.1128/EC.00154-10
13. 10.1128/msystems.00232-22
14. https://doi.org/10.1371/journal.pone.0021948
15. https://doi.org/10.1007/s00294-009-0235-0
16. https://doi.org/10.3390/molecules27041431
17. https://doi.org/10.1128/EC.00154-10
18. https://doi.org/10.1128/msystems.00232-22
19. https://doi.org/10.1371/journal.pone.0021948.
20. https://doi.org/10.3390/molecules27041431.
21. https://doi.org/10.1128/EC.00154-10.
22. https://doi.org/10.1128/msystems.00232-22.
23. https://doi.org/10.1007/s00294-009-0235-0.
24. https://doi.org/10.1371/journal.pone.0021948,
25. https://doi.org/10.1007/s00294-009-0235-0,
26. https://doi.org/10.3390/molecules27041431,
27. https://doi.org/10.1128/ec.00154-10,
28. https://doi.org/10.1128/msystems.00232-22,