---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-30T05:27:22.311493'
end_time: '2026-09-30T05:40:34.947994'
duration_seconds: 792.64
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: kuz
  gene_symbol: kuz
  uniprot_accession: Q9VJW9
  protein_description: 'RecName: Full=ADAM10 endopeptidase {ECO:0000256|ARBA:ARBA00012332};
    EC=3.4.24.81 {ECO:0000256|ARBA:ARBA00012332};'
  gene_info: Name=kuz {ECO:0000313|EMBL:AAF53318.1, ECO:0000313|FlyBase:FBgn0259984};
    Synonyms=11410 {ECO:0000313|EMBL:AAF53318.1}, 34Da {ECO:0000313|EMBL:AAF53318.1},
    ADAM10 {ECO:0000313|EMBL:AAF53318.1}, BG:DS07660.3 {ECO:0000313|EMBL:AAF53318.1},
    br38 {ECO:0000313|EMBL:AAF53318.1}, CT22079 {ECO:0000313|EMBL:AAF53318.1}, Dmel\CG7147
    {ECO:0000313|EMBL:AAF53318.1}, GS11410 {ECO:0000313|EMBL:AAF53318.1}, KUZ {ECO:0000313|EMBL:AAF53318.1},
    Kuz {ECO:0000313|EMBL:AAF53318.1}, l(2)03782 {ECO:0000313|EMBL:AAF53318.1}, l(2)34Da
    {ECO:0000313|EMBL:AAF53318.1}, l(2)br38 {ECO:0000313|EMBL:AAF53318.1}, l(2)c00136
    {ECO:0000313|EMBL:AAF53318.1}, l(2)k01403 {ECO:0000313|EMBL:AAF53318.1}, l34Da
    {ECO:0000313|EMBL:AAF53318.1}, soy nut {ECO:0000313|EMBL:AAF53318.1}; ORFNames=CG7147
    {ECO:0000313|EMBL:AAF53318.1, ECO:0000313|FlyBase:FBgn0259984}, Dmel_CG7147 {ECO:0000313|EMBL:AAF53318.1};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Not specified in UniProt
  protein_domains: ADAM10_ADAM17. (IPR034025); ADAM10_Cys-rich. (IPR049038); ADAM_Metalloproteinase.
    (IPR051489); Disintegrin_dom. (IPR001762); Disintegrin_dom_sf. (IPR036436)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 42
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: kuz-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: kuz-deep-research-falcon_artifacts/artifact-01.md
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
- **UniProt Accession:** Q9VJW9
- **Protein Description:** RecName: Full=ADAM10 endopeptidase {ECO:0000256|ARBA:ARBA00012332}; EC=3.4.24.81 {ECO:0000256|ARBA:ARBA00012332};
- **Gene Information:** Name=kuz {ECO:0000313|EMBL:AAF53318.1, ECO:0000313|FlyBase:FBgn0259984}; Synonyms=11410 {ECO:0000313|EMBL:AAF53318.1}, 34Da {ECO:0000313|EMBL:AAF53318.1}, ADAM10 {ECO:0000313|EMBL:AAF53318.1}, BG:DS07660.3 {ECO:0000313|EMBL:AAF53318.1}, br38 {ECO:0000313|EMBL:AAF53318.1}, CT22079 {ECO:0000313|EMBL:AAF53318.1}, Dmel\CG7147 {ECO:0000313|EMBL:AAF53318.1}, GS11410 {ECO:0000313|EMBL:AAF53318.1}, KUZ {ECO:0000313|EMBL:AAF53318.1}, Kuz {ECO:0000313|EMBL:AAF53318.1}, l(2)03782 {ECO:0000313|EMBL:AAF53318.1}, l(2)34Da {ECO:0000313|EMBL:AAF53318.1}, l(2)br38 {ECO:0000313|EMBL:AAF53318.1}, l(2)c00136 {ECO:0000313|EMBL:AAF53318.1}, l(2)k01403 {ECO:0000313|EMBL:AAF53318.1}, l34Da {ECO:0000313|EMBL:AAF53318.1}, soy nut {ECO:0000313|EMBL:AAF53318.1}; ORFNames=CG7147 {ECO:0000313|EMBL:AAF53318.1, ECO:0000313|FlyBase:FBgn0259984}, Dmel_CG7147 {ECO:0000313|EMBL:AAF53318.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ADAM10_ADAM17. (IPR034025); ADAM10_Cys-rich. (IPR049038); ADAM_Metalloproteinase. (IPR051489); Disintegrin_dom. (IPR001762); Disintegrin_dom_sf. (IPR036436)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "kuz" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'kuz' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **kuz** (gene ID: kuz, UniProt: Q9VJW9) in DROME.

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
- **UniProt Accession:** Q9VJW9
- **Protein Description:** RecName: Full=ADAM10 endopeptidase {ECO:0000256|ARBA:ARBA00012332}; EC=3.4.24.81 {ECO:0000256|ARBA:ARBA00012332};
- **Gene Information:** Name=kuz {ECO:0000313|EMBL:AAF53318.1, ECO:0000313|FlyBase:FBgn0259984}; Synonyms=11410 {ECO:0000313|EMBL:AAF53318.1}, 34Da {ECO:0000313|EMBL:AAF53318.1}, ADAM10 {ECO:0000313|EMBL:AAF53318.1}, BG:DS07660.3 {ECO:0000313|EMBL:AAF53318.1}, br38 {ECO:0000313|EMBL:AAF53318.1}, CT22079 {ECO:0000313|EMBL:AAF53318.1}, Dmel\CG7147 {ECO:0000313|EMBL:AAF53318.1}, GS11410 {ECO:0000313|EMBL:AAF53318.1}, KUZ {ECO:0000313|EMBL:AAF53318.1}, Kuz {ECO:0000313|EMBL:AAF53318.1}, l(2)03782 {ECO:0000313|EMBL:AAF53318.1}, l(2)34Da {ECO:0000313|EMBL:AAF53318.1}, l(2)br38 {ECO:0000313|EMBL:AAF53318.1}, l(2)c00136 {ECO:0000313|EMBL:AAF53318.1}, l(2)k01403 {ECO:0000313|EMBL:AAF53318.1}, l34Da {ECO:0000313|EMBL:AAF53318.1}, soy nut {ECO:0000313|EMBL:AAF53318.1}; ORFNames=CG7147 {ECO:0000313|EMBL:AAF53318.1, ECO:0000313|FlyBase:FBgn0259984}, Dmel_CG7147 {ECO:0000313|EMBL:AAF53318.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ADAM10_ADAM17. (IPR034025); ADAM10_Cys-rich. (IPR049038); ADAM_Metalloproteinase. (IPR051489); Disintegrin_dom. (IPR001762); Disintegrin_dom_sf. (IPR036436)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "kuz" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'kuz' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **kuz** (gene ID: kuz, UniProt: Q9VJW9) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: Kuzbanian (kuz) in *Drosophila melanogaster*

## Gene Identity and Overview

Kuzbanian (Kuz) is the sole *Drosophila melanogaster* ortholog of mammalian ADAM10 (A Disintegrin And Metalloproteinase 10), encoded by the gene *kuz* (also known as CG7147, FBgn0259984) (baker2024aninvivo pages 13-17, wang2023aconservedmechanism pages 1-4). This transmembrane metalloproteinase was first identified in genetic screens for neurogenic phenotypes in the 1990s and has since emerged as a critical regulator of developmental signaling pathways (rooke1996kuzaconserved pages 1-2, pan1997kuzbaniancontrolsproteolytic pages 1-2).

## Primary Enzymatic Function and Catalytic Mechanism

### Enzyme Classification and Reaction

Kuzbanian functions as a zinc-dependent metalloproteinase of the ADAM family that catalyzes **ectodomain shedding** through hydrolysis of peptide bonds in transmembrane protein substrates (baker2024aninvivo pages 13-17, baker2024aninvivo pages 10-13, baker2024aninvivo pages 38-40). The catalytic reaction involves water activation by the zinc ion in the metalloprotease active site to cleave specific peptide bonds in the extracellular juxtamembrane regions of substrate proteins (baker2024aninvivo pages 13-17, baker2024aninvivo pages 30-35). This proteolytic activity releases the extracellular domains of substrates while leaving membrane-associated C-terminal fragments that can undergo further processing (wang2023aconservedmechanism pages 1-4, bahrampour2020thefivefaces pages 51-53).

### Protein Structure and Domain Organization

Kuz is a type-I transmembrane protein with a multidomain architecture characteristic of ADAM family proteases (rooke1996kuzaconserved pages 3-4, pan1997kuzbaniancontrolsproteolytic pages 8-9). The protein contains an N-terminal signal peptide, a prodomain, a metalloprotease domain with zinc-binding site, a disintegrin domain, a cysteine-rich domain, a transmembrane segment near the C-terminus, and a short cytoplasmic tail (rooke1996kuzaconserved pages 3-4, pan1997kuzbaniancontrolsproteolytic pages 2-4). This topology positions the catalytic metalloprotease domain extracellularly where it can access transmembrane substrates (pan1997kuzbaniancontrolsproteolytic pages 8-9, pan1997kuzbaniancontrolsproteolytic pages 7-8).

## Substrate Specificity

Kuzbanian exhibits specificity for transmembrane proteins with accessible extracellular cleavage sites. The three best-characterized substrates in *Drosophila* are detailed below and summarized in the accompanying table.

| Substrate | Cleavage site/location | Biological function of cleavage | Evidence type | Key references |
|---|---|---|---|---|
| **Notch receptor** | Extracellular **S2 site** in the juxtamembrane negative regulatory region, approximately 12 residues outside the transmembrane domain. The exact residue of the *Drosophila* Kuz cut has not been mapped conclusively; Ala1710–Val1711 was mapped in mammalian Notch1 and should not be assigned directly to fly Notch. | Ectodomain shedding generates a membrane-tethered Notch intermediate that becomes a γ-secretase substrate. Subsequent S3 cleavage releases NICD, which enters the nucleus and activates Su(H)/Mastermind-dependent transcription. | Strong genetic and cell-biological evidence: kuz loss or dominant-negative Kuz impairs Notch processing and target-gene activation; activated intracellular Notch bypasses the kuz requirement. Recent in-vivo receptor-switch experiments also show Kuz-dependent activation. | Pan & Rubin, 1997; Klein, 2002; Pinot & Le Borgne, 2024; Baker et al., 2024 (bahrampour2020thefivefaces pages 51-53, pinot2024spatiotemporalregulationof pages 2-4, baker2024aninvivo pages 30-35, klein2002kuzbanianisrequired pages 1-2, klein2002kuzbanianisrequired pages 5-5, steinbuck2018areviewof pages 2-4, pan1997kuzbaniancontrolsproteolytic pages 7-8) |
| **Roundabout 1 (Robo1)** | Cleavage within the receptor’s extracellular domain; a precise Kuz cleavage bond is not established in the cited evidence. | Proteolytic processing regulates Robo1-mediated repulsive signaling and is required for appropriate axon guidance at the *Drosophila* CNS midline. | Genetic and receptor-processing evidence, summarized in recent Slit–Robo and proteolytic-switch literature; the functional phenotype links Kuz-dependent Robo1 cleavage to midline axon repulsion. | Coleman et al., 2010; Baker et al., 2024; Sanhueza et al., 2025 (sanhueza2025theslit–robosignalling pages 3-4, baker2024aninvivo pages 38-40) |
| **Amyloid precursor protein-like (APPL)** | **α-secretase cleavage** in the APPL ectodomain, producing soluble **sAPPLα** and a membrane-associated α-C-terminal fragment; the exact peptide bond is not specified in the cited studies. | Promotes non-amyloidogenic APPL processing. Secreted sAPPLα has been associated with neuronal-survival and neuroglial-signaling functions, while α-cleavage competes with β-secretase processing. | In-vivo genetic and biochemical evidence: Kuz overexpression increases the APPL α-CTF and decreases the β-CTF; α-secretase inhibition increases full-length APPL at the plasma membrane. | Cassar & Kretzschmar, 2016; Ramaker et al., 2016 (ramaker2016amyloidprecursorproteins pages 7-8, cassar2016analysisofamyloid pages 5-6, ramaker2016amyloidprecursorproteins pages 14-15) |


*Table: Key Drosophila Kuzbanian substrates, the location and functional outcome of their cleavage, and the strength of supporting evidence. Notch is the best-established signaling substrate, while Robo1 and APPL connect Kuz to axon guidance and α-secretase processing, respectively.*

### Notch Receptor: The Primary Substrate

The **Notch receptor** is the most extensively characterized Kuz substrate (wang2023aconservedmechanism pages 1-4, bahrampour2020thefivefaces pages 51-53, pan1997kuzbaniancontrolsproteolytic pages 1-2). Kuz performs the critical **S2 cleavage** in Notch's extracellular juxtamembrane region, approximately 12 amino acids outside the transmembrane domain (mumm2000aligandinducedextracellular pages 1-2, steinbuck2018areviewof pages 2-4). This cleavage occurs within the negative regulatory region (NRR) after ligand binding exposes the normally masked S2 site (pinot2024spatiotemporalregulationof pages 2-4, steinbuck2018areviewof pages 2-4). 

Biochemical and genetic evidence strongly supports Notch as a direct Kuz substrate: loss of *kuz* function eliminates the ~100 kDa processed Notch C-terminal fragment, while dominant-negative Kuz lacking protease activity blocks Notch processing (pan1997kuzbaniancontrolsproteolytic pages 6-7, pan1997kuzbaniancontrolsproteolytic pages 2-4). Expression of activated intracellular Notch (NICD) bypasses the Kuz requirement, placing Kuz function upstream of NICD production (klein2002kuzbanianisrequired pages 1-2, klein2002kuzbanianisrequired pages 5-5). Recent studies using chimeric receptor systems have confirmed that Kuz-mediated cleavage is necessary for most ligand-dependent and force-activated Notch receptor variants (baker2024aninvivo pages 13-17, baker2024aninvivo pages 10-13).

### Roundabout (Robo1) Receptor

The **Robo1 axon guidance receptor** is cleaved by Kuz in its extracellular domain, a process required for proper repulsive signaling at the CNS midline during axon guidance (sanhueza2025theslit–robosignalling pages 3-4, baker2024aninvivo pages 38-40). This proteolytic processing regulates Robo1-mediated responses to the Slit ligand and is essential for midline axon repulsion (sanhueza2025theslit–robosignalling pages 3-4, baker2024aninvivo pages 38-40).

### Amyloid Precursor Protein-Like (APPL)

**APPL**, the *Drosophila* homolog of mammalian APP, undergoes α-secretase cleavage by Kuzbanian (ramaker2016amyloidprecursorproteins pages 7-8, cassar2016analysisofamyloid pages 5-6). Genetic manipulation experiments demonstrate that Kuz overexpression increases the APPL α-C-terminal fragment while reducing the β-C-terminal fragment, consistent with Kuz functioning as the APPL α-secretase (ramaker2016amyloidprecursorproteins pages 7-8, cassar2016analysisofamyloid pages 5-6). This cleavage produces soluble sAPPLα, which has been implicated in neuroprotective and neuroglial signaling functions (cassar2016analysisofamyloid pages 5-6).

### Note on Delta Ligand

While early studies proposed that Kuz might cleave the Notch ligand Delta, subsequent cell-autonomous clonal analyses demonstrated that Kuz is required in Notch-receiving cells but not in Delta-expressing signal-sending cells (klein2002kuzbanianisrequired pages 1-2, klein2002kuzbanianisrequired pages 5-5, klein2002kuzbanianisrequired pages 2-5). Current evidence does not support Delta as a physiologically relevant Kuz substrate during canonical Notch signaling (vullings2025anothertailof pages 1-2, klein2002kuzbanianisrequired pages 5-5).

## Subcellular Localization and Site of Function

Kuzbanian is a **transmembrane protein localized at the cell surface** where it performs ectodomain shedding of its substrates (rooke1996kuzaconserved pages 3-4, pan1997kuzbaniancontrolsproteolytic pages 8-9, pan1997kuzbaniancontrolsproteolytic pages 7-8). The extracellular orientation of the metalloprotease domain positions the catalytic site to access the extracellular portions of transmembrane substrates (pan1997kuzbaniancontrolsproteolytic pages 8-9, pan1997kuzbaniancontrolsproteolytic pages 1-2). While the precise trafficking itinerary and steady-state distribution between plasma membrane and intracellular compartments have not been comprehensively mapped, the functional evidence indicates that proteolytic processing occurs at or near the cell surface (pan1997kuzbaniancontrolsproteolytic pages 8-9).

## Signaling Pathways and Molecular Mechanisms

### Notch Signaling Pathway: Core Molecular Function

Kuzbanian plays an **essential and specific role in canonical Notch signaling** as the protease responsible for ligand-induced receptor activation (bahrampour2020thefivefaces pages 51-53, pinot2024spatiotemporalregulationof pages 2-4, wang2023aconservedmechanism pages 1-4, wang2023aconservedmechanism pages 5-7). The molecular mechanism proceeds through the following steps:

1. **Ligand binding**: Delta or Serrate on an adjacent signal-sending cell binds to Notch on the receiving cell (pinot2024spatiotemporalregulationof pages 2-4, wang2023aconservedmechanism pages 1-4).

2. **Conformational change and endocytosis**: Ligand endocytosis generates mechanical force that exposes the S2 cleavage site in Notch's NRR (pinot2024spatiotemporalregulationof pages 2-4, baker2024aninvivo pages 30-35, vullings2025anothertailof pages 1-2).

3. **Kuz-mediated S2 cleavage**: Kuzbanian cleaves Notch at the S2 site, releasing the extracellular domain and generating a membrane-tethered NEXT (Notch Extracellular Truncation) fragment (bahrampour2020thefivefaces pages 51-53, pinot2024spatiotemporalregulationof pages 2-4, wang2023aconservedmechanism pages 1-4, mumm2000aligandinducedextracellular pages 1-2).

4. **γ-secretase S3 cleavage**: The NEXT fragment becomes a substrate for the γ-secretase complex, which cleaves within the transmembrane domain at the S3 site (bahrampour2020thefivefaces pages 51-53, pinot2024spatiotemporalregulationof pages 2-4, wang2023aconservedmechanism pages 1-4).

5. **NICD release and transcription**: The S3 cleavage releases the Notch intracellular domain (NICD), which translocates to the nucleus, associates with Suppressor of Hairless [Su(H)] and Mastermind, and activates target gene transcription including *Enhancer of split* [*E(spl)*] genes (bahrampour2020thefivefaces pages 51-53, wang2023aconservedmechanism pages 1-4, bahrampour2020thefivefaces pages 56-59).

This proteolytic cascade positions Kuz as the **rate-limiting step** that initiates Notch receptor activation (wang2023aconservedmechanism pages 1-4, wang2023aconservedmechanism pages 5-7, steinbuck2018areviewof pages 2-4). Recent studies have shown that JNK pathway activation can inhibit *kuz* expression, providing a mechanism for negative regulation of Notch signaling in certain cellular contexts such as tumors (wang2023aconservedmechanism pages 1-4, wang2023aconservedmechanism pages 5-7).

### Additional Pathway Roles

Beyond Notch, Kuzbanian participates in the **Robo/Slit axon guidance pathway** through proteolytic processing of Robo1, contributing to midline repulsion during CNS axon pathfinding (sanhueza2025theslit–robosignalling pages 3-4). The protein may also function in α-secretase processing of APPL, linking it to non-amyloidogenic APP metabolism (ramaker2016amyloidprecursorproteins pages 7-8, cassar2016analysisofamyloid pages 5-6).

## Developmental Roles and Biological Processes

Kuzbanian is required in multiple developmental contexts throughout *Drosophila* development, primarily through its role in Notch-dependent cell fate decisions. These functions are summarized in the accompanying table.

| Developmental process / tissue | Specific role of Kuzbanian | Phenotype when Kuz is disrupted | Key citation |
|---|---|---|---|
| Embryonic neurogenesis | Enables Notch-dependent lateral inhibition in signal-receiving ectodermal cells, restricting neural precursor selection and preserving epidermal fates. | Excess neural differentiation at the expense of epidermis; severe maternal-plus-zygotic loss causes widespread neuralization. | Rooke et al., 1996; Pan & Rubin, 1997 (rooke1996kuzaconserved pages 1-2, pan1997kuzbaniancontrolsproteolytic pages 1-2) |
| Sensory bristle development (notum) | Supports Notch-mediated selection and fate specification of sensory-organ precursors; acts during the distinct periods when macrochaete and microchaete precursors are selected. | Clusters or supernumerary macrochaetes after disruption during the third larval instar and extra microchaetes after early-pupal disruption; later shaft-versus-socket decisions may also be altered. | Pan & Rubin, 1997 (pan1997kuzbaniancontrolsproteolytic pages 4-5, pan1997kuzbaniancontrolsproteolytic pages 6-7) |
| Eye development | Restricts photoreceptor recruitment through lateral inhibition and contributes to orderly ommatidial differentiation. | Supernumerary photoreceptors and ELAV-positive neurons; disrupted ommatidial organization and abnormal or chimeric ommatidia. | Rooke et al., 1996; Pan & Rubin, 1997 (pan1997kuzbaniancontrolsproteolytic pages 4-5, pan1997kuzbaniancontrolsproteolytic pages 2-4, rooke1996kuzaconserved pages 1-2) |
| Wing development | Acts cell-autonomously in Notch-receiving cells at the dorsal–ventral boundary, upstream of intracellular Notch production, to maintain Notch-target *wingless* expression and wing-margin patterning. | Loss of *wingless* and Notch-reporter expression within mutant cells, producing notches or loss of tissue at the adult wing margin; activated intracellular Notch bypasses the Kuz requirement. | Klein, 2002; Pan & Rubin, 1997 (klein2002kuzbanianisrequired pages 1-2, klein2002kuzbanianisrequired pages 5-5, pan1997kuzbaniancontrolsproteolytic pages 6-7) |
| Axon guidance and CNS tract formation | Provides proteolytic activity needed for axon extension and guidance, including proper formation of longitudinal CNS pathways; receptor processing such as Robo1 cleavage offers a mechanistic link to midline repulsion. | Breaks or disorganization in longitudinal axon tracts, stalled axons, and major pathway defects after neuronal expression of protease-defective Kuz. | Pan & Rubin, 1997; Sanhueza et al., 2025 (pan1997kuzbaniancontrolsproteolytic pages 4-5, pan1997kuzbaniancontrolsproteolytic pages 2-4, sanhueza2025theslit–robosignalling pages 3-4) |


*Table: This table maps the principal Drosophila tissues and developmental processes requiring Kuzbanian to its mechanistic role and characteristic loss-of-function phenotypes. It distinguishes well-established Notch-dependent patterning functions from its additional role in axon guidance.*

### Embryonic Neurogenesis and Lateral Inhibition

Kuz is essential for **lateral inhibition**, the process by which emerging neural precursors signal to neighboring cells to prevent them from adopting neural fates (rooke1996kuzaconserved pages 1-2, pan1997kuzbaniancontrolsproteolytic pages 1-2). Loss of *kuz* function causes neural hyperplasia, with excess cells adopting neural fates at the expense of epidermal cells (pan1997kuzbaniancontrolsproteolytic pages 2-4, rooke1996kuzaconserved pages 1-2, pan1997kuzbaniancontrolsproteolytic pages 1-2). Severe maternal and zygotic *kuz* mutants show widespread neuralization of the embryo, demonstrating the fundamental requirement for Kuz in establishing the neural-epidermal cell fate balance (rooke1996kuzaconserved pages 1-2).

### Sensory Organ Development

In the **notum (thorax)**, Kuz is required for proper selection and patterning of sensory bristle precursors (pan1997kuzbaniancontrolsproteolytic pages 4-5, pan1997kuzbaniancontrolsproteolytic pages 6-7). Disruption of Kuz function produces clusters of supernumerary macrochaetes (large bristles) when perturbed during the third larval instar, and extra microchaetes (small bristles) when disrupted during early pupal development, reflecting the distinct temporal windows for these precursor selections (pan1997kuzbaniancontrolsproteolytic pages 4-5, pan1997kuzbaniancontrolsproteolytic pages 6-7, rooke1996kuzaconserved pages 1-2).

### Eye Development

In the **developing eye**, Kuz limits photoreceptor recruitment through lateral inhibition (pan1997kuzbaniancontrolsproteolytic pages 4-5, pan1997kuzbaniancontrolsproteolytic pages 2-4, rooke1996kuzaconserved pages 1-2). *kuz* mutant clones produce supernumerary photoreceptors and disrupt ommatidial organization, leading to abnormal eye morphology (pan1997kuzbaniancontrolsproteolytic pages 4-5, rooke1996kuzaconserved pages 1-2).

### Wing Development

In the **wing imaginal disc**, Kuz acts cell-autonomously in Notch-receiving cells at the dorsal-ventral boundary to maintain expression of the Notch target gene *wingless* and to pattern the wing margin (klein2002kuzbanianisrequired pages 1-2, klein2002kuzbanianisrequired pages 5-5). Loss of Kuz function causes notches in the adult wing blade and loss of *wingless* expression at the boundary (pan1997kuzbaniancontrolsproteolytic pages 6-7, klein2002kuzbanianisrequired pages 1-2, klein2002kuzbanianisrequired pages 5-5). Crucially, expression of activated NICD can rescue these defects, confirming that Kuz functions upstream of NICD generation (klein2002kuzbanianisrequired pages 1-2, klein2002kuzbanianisrequired pages 5-5).

### Axon Guidance and Growth

Beyond its role in cell fate specification, Kuz is required for **proper axon extension and guidance** in the developing nervous system (pan1997kuzbaniancontrolsproteolytic pages 4-5, pan1997kuzbaniancontrolsproteolytic pages 2-4). Expression of dominant-negative Kuz specifically in neurons causes major disruptions in CNS axon pathways, including breaks in longitudinal connectives and stalled growth cones (pan1997kuzbaniancontrolsproteolytic pages 4-5, pan1997kuzbaniancontrolsproteolytic pages 2-4). This function likely involves both Notch-dependent and Notch-independent mechanisms, including Robo1 processing (sanhueza2025theslit–robosignalling pages 3-4).

### Cell-Autonomous Function

Genetic mosaic analyses have established that Kuz functions **cell-autonomously in signal-receiving cells** rather than in ligand-producing cells (klein2002kuzbanianisrequired pages 1-2, rooke1996kuzaconserved pages 3-4, klein2002kuzbanianisrequired pages 5-5). Cells lacking Kuz cannot respond to Delta or Serrate ligands from neighboring wild-type cells, whereas Kuz-mutant cells expressing Delta can signal normally to wild-type neighbors (klein2002kuzbanianisrequired pages 1-2, klein2002kuzbanianisrequired pages 5-5). This demonstrates that Kuz acts within the responding cell to process the Notch receptor.

## Experimental Evidence and Evolutionary Conservation

The functional characterization of Kuzbanian has employed multiple experimental approaches:

- **Genetic evidence**: Loss-of-function alleles and dominant-negative constructs lacking the protease domain produce characteristic neurogenic and wing phenotypes (pan1997kuzbaniancontrolsproteolytic pages 6-7, pan1997kuzbaniancontrolsproteolytic pages 2-4, rooke1996kuzaconserved pages 1-2, pan1997kuzbaniancontrolsproteolytic pages 1-2).

- **Biochemical evidence**: Western blot analyses show that the ~100 kDa processed Notch fragment is absent in *kuz* mutant embryos and cells expressing dominant-negative Kuz (pan1997kuzbaniancontrolsproteolytic pages 6-7, pan1997kuzbaniancontrolsproteolytic pages 2-4).

- **Cell-autonomous clonal analysis**: Mosaic experiments demonstrate that Kuz is required in Notch-receiving cells (klein2002kuzbanianisrequired pages 1-2, klein2002kuzbanianisrequired pages 5-5).

- **Structure-function analysis**: Domain deletion studies confirm the requirement for the metalloprotease catalytic domain (pan1997kuzbaniancontrolsproteolytic pages 2-4, rooke1996kuzaconserved pages 1-2).

The functional role of Kuz in Notch signaling is evolutionarily conserved: mammalian ADAM10 performs the equivalent S2 cleavage of mammalian Notch receptors, and this conservation extends to vertebrate neurogenesis (pan1997kuzbaniancontrolsproteolytic pages 2-4, pan1997kuzbaniancontrolsproteolytic pages 1-2).

## Recent Developments (2023-2025)

Recent studies continue to illuminate Kuz biology:

- **Pathway regulation**: Wang et al. (2023) demonstrated that JNK pathway activation inhibits *kuz* expression in *Drosophila* tumor models, providing a conserved mechanism linking stress signaling to Notch inactivation (wang2023aconservedmechanism pages 1-4, wang2023aconservedmechanism pages 5-7).

- **Force-dependent activation**: Baker et al. (2024) used engineered receptor-switch systems to demonstrate that Kuz-mediated cleavage is necessary for force-dependent Notch activation across diverse proteolytic switch domains (baker2024aninvivo pages 13-17, baker2024aninvivo pages 10-13).

- **Temporal regulation**: Pinot and Le Borgne (2024) reviewed the spatio-temporal control of Notch activation during asymmetric cell division, highlighting the precise regulation of Kuz-dependent S2 cleavage at cytokinesis (pinot2024spatiotemporalregulationof pages 13-15, pinot2024spatiotemporalregulationof pages 2-4).

- **Pathway integration**: Sanhueza et al. (2025) discussed Kuz's role in Robo1 processing during Slit-Robo signaling in nervous system development (sanhueza2025theslit–robosignalling pages 3-4).

## Summary

Kuzbanian is a transmembrane zinc-dependent metalloproteinase that serves as the primary activating protease for Notch signaling in *Drosophila melanogaster*. Through catalytic hydrolysis of peptide bonds in the extracellular juxtamembrane regions of substrate proteins, particularly the S2 cleavage of Notch, Kuz enables critical developmental decisions including lateral inhibition during neurogenesis, sensory organ patterning, photoreceptor specification, and wing margin formation. The protein functions cell-autonomously at the plasma membrane of signal-receiving cells and is evolutionarily conserved with mammalian ADAM10. Additional substrates including Robo1 and APPL connect Kuz to axon guidance and neuroprotective pathways beyond canonical Notch signaling.

References

1. (baker2024aninvivo pages 13-17): Frederick C. Baker, Jacob Harman, Trevor Jordan, Breana Walton, Amber Ajamu-Johnson, Rama F. Alashqar, Simran Bhikot, Gary Struhl, and Paul D. Langridge. An in vivo screen for proteolytic switch domains that can mediate notch activation by force. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.10.602225, doi:10.1101/2024.07.10.602225. This article has 1 citations.

2. (wang2023aconservedmechanism pages 1-4): Cheng-Wei Wang, Marie Clémot, Takao Hashimoto, Johnny A. Diaz, Lauren M. Goins, Andrew S. Goldstein, Raghavendra Nagaraj, and Utpal Banerjee. A conserved mechanism for jnk-mediated loss of notch function in advanced prostate cancer. Science Signaling, Nov 2023. URL: https://doi.org/10.1126/scisignal.abo5213, doi:10.1126/scisignal.abo5213. This article has 3 citations and is from a domain leading peer-reviewed journal.

3. (rooke1996kuzaconserved pages 1-2): Jenny Rooke, Duojia Pan, Tian Xu, and Gerald M. Rubin. Kuz, a conserved metalloprotease-disintegrin protein with two roles in drosophila neurogenesis. Science, 273:1227-1231, Aug 1996. URL: https://doi.org/10.1126/science.273.5279.1227, doi:10.1126/science.273.5279.1227. This article has 443 citations and is from a highest quality peer-reviewed journal.

4. (pan1997kuzbaniancontrolsproteolytic pages 1-2): Duojia Pan and Gerald M Rubin. Kuzbanian controls proteolytic processing of notch and mediates lateral inhibition during drosophila and vertebrate neurogenesis. Cell, 90:271-280, Jul 1997. URL: https://doi.org/10.1016/s0092-8674(00)80335-9, doi:10.1016/s0092-8674(00)80335-9. This article has 705 citations and is from a highest quality peer-reviewed journal.

5. (baker2024aninvivo pages 10-13): Frederick C. Baker, Jacob Harman, Trevor Jordan, Breana Walton, Amber Ajamu-Johnson, Rama F. Alashqar, Simran Bhikot, Gary Struhl, and Paul D. Langridge. An in vivo screen for proteolytic switch domains that can mediate notch activation by force. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.10.602225, doi:10.1101/2024.07.10.602225. This article has 1 citations.

6. (baker2024aninvivo pages 38-40): Frederick C. Baker, Jacob Harman, Trevor Jordan, Breana Walton, Amber Ajamu-Johnson, Rama F. Alashqar, Simran Bhikot, Gary Struhl, and Paul D. Langridge. An in vivo screen for proteolytic switch domains that can mediate notch activation by force. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.10.602225, doi:10.1101/2024.07.10.602225. This article has 1 citations.

7. (baker2024aninvivo pages 30-35): Frederick C. Baker, Jacob Harman, Trevor Jordan, Breana Walton, Amber Ajamu-Johnson, Rama F. Alashqar, Simran Bhikot, Gary Struhl, and Paul D. Langridge. An in vivo screen for proteolytic switch domains that can mediate notch activation by force. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.10.602225, doi:10.1101/2024.07.10.602225. This article has 1 citations.

8. (bahrampour2020thefivefaces pages 51-53): Shahrzad Bahrampour and Stefan Thor. The five faces of notch signalling during drosophila melanogaster embryonic cns development. Advances in experimental medicine and biology, 1218:39-58, Jan 2020. URL: https://doi.org/10.1007/978-3-030-34436-8\_3, doi:10.1007/978-3-030-34436-8\_3. This article has 14 citations and is from a peer-reviewed journal.

9. (rooke1996kuzaconserved pages 3-4): Jenny Rooke, Duojia Pan, Tian Xu, and Gerald M. Rubin. Kuz, a conserved metalloprotease-disintegrin protein with two roles in drosophila neurogenesis. Science, 273:1227-1231, Aug 1996. URL: https://doi.org/10.1126/science.273.5279.1227, doi:10.1126/science.273.5279.1227. This article has 443 citations and is from a highest quality peer-reviewed journal.

10. (pan1997kuzbaniancontrolsproteolytic pages 8-9): Duojia Pan and Gerald M Rubin. Kuzbanian controls proteolytic processing of notch and mediates lateral inhibition during drosophila and vertebrate neurogenesis. Cell, 90:271-280, Jul 1997. URL: https://doi.org/10.1016/s0092-8674(00)80335-9, doi:10.1016/s0092-8674(00)80335-9. This article has 705 citations and is from a highest quality peer-reviewed journal.

11. (pan1997kuzbaniancontrolsproteolytic pages 2-4): Duojia Pan and Gerald M Rubin. Kuzbanian controls proteolytic processing of notch and mediates lateral inhibition during drosophila and vertebrate neurogenesis. Cell, 90:271-280, Jul 1997. URL: https://doi.org/10.1016/s0092-8674(00)80335-9, doi:10.1016/s0092-8674(00)80335-9. This article has 705 citations and is from a highest quality peer-reviewed journal.

12. (pan1997kuzbaniancontrolsproteolytic pages 7-8): Duojia Pan and Gerald M Rubin. Kuzbanian controls proteolytic processing of notch and mediates lateral inhibition during drosophila and vertebrate neurogenesis. Cell, 90:271-280, Jul 1997. URL: https://doi.org/10.1016/s0092-8674(00)80335-9, doi:10.1016/s0092-8674(00)80335-9. This article has 705 citations and is from a highest quality peer-reviewed journal.

13. (pinot2024spatiotemporalregulationof pages 2-4): Mathieu Pinot and Roland Le Borgne. Spatio-temporal regulation of notch activation in asymmetrically dividing sensory organ precursor cells in drosophila melanogaster epithelium. Cells, 13:1133, Jun 2024. URL: https://doi.org/10.3390/cells13131133, doi:10.3390/cells13131133. This article has 3 citations.

14. (klein2002kuzbanianisrequired pages 1-2): Thomas Klein. Kuzbanian is required cell autonomously during notch signalling in the drosophila wing. Jun 2002. URL: https://doi.org/10.1007/s00427-002-0233-4, doi:10.1007/s00427-002-0233-4. This article has 29 citations and is from a peer-reviewed journal.

15. (klein2002kuzbanianisrequired pages 5-5): Thomas Klein. Kuzbanian is required cell autonomously during notch signalling in the drosophila wing. Jun 2002. URL: https://doi.org/10.1007/s00427-002-0233-4, doi:10.1007/s00427-002-0233-4. This article has 29 citations and is from a peer-reviewed journal.

16. (steinbuck2018areviewof pages 2-4): Martin Peter Steinbuck and Susan Winandy. A review of notch processing with new insights into ligand-independent notch signaling in t-cells. Frontiers in Immunology, Jun 2018. URL: https://doi.org/10.3389/fimmu.2018.01230, doi:10.3389/fimmu.2018.01230. This article has 148 citations and is from a peer-reviewed journal.

17. (sanhueza2025theslit–robosignalling pages 3-4): Nicole Sanhueza, Evelyn C. Avilés, and Carlos Oliva. The slit–robo signalling pathway in nervous system development: a comparative perspective from vertebrates and invertebrates. Open Biology, Jul 2025. URL: https://doi.org/10.1098/rsob.250026, doi:10.1098/rsob.250026. This article has 8 citations and is from a peer-reviewed journal.

18. (ramaker2016amyloidprecursorproteins pages 7-8): Jenna M. Ramaker, Robert S. Cargill, Tracy L. Swanson, Hanil Quirindongo, Marlène Cassar, Doris Kretzschmar, and Philip F. Copenhaver. Amyloid precursor proteins are dynamically trafficked and processed during neuronal development. Frontiers in Molecular Neuroscience, Nov 2016. URL: https://doi.org/10.3389/fnmol.2016.00130, doi:10.3389/fnmol.2016.00130. This article has 28 citations.

19. (cassar2016analysisofamyloid pages 5-6): Marlène Cassar and Doris Kretzschmar. Analysis of amyloid precursor protein function in drosophila melanogaster. Frontiers in Molecular Neuroscience, Jul 2016. URL: https://doi.org/10.3389/fnmol.2016.00061, doi:10.3389/fnmol.2016.00061. This article has 48 citations.

20. (ramaker2016amyloidprecursorproteins pages 14-15): Jenna M. Ramaker, Robert S. Cargill, Tracy L. Swanson, Hanil Quirindongo, Marlène Cassar, Doris Kretzschmar, and Philip F. Copenhaver. Amyloid precursor proteins are dynamically trafficked and processed during neuronal development. Frontiers in Molecular Neuroscience, Nov 2016. URL: https://doi.org/10.3389/fnmol.2016.00130, doi:10.3389/fnmol.2016.00130. This article has 28 citations.

21. (mumm2000aligandinducedextracellular pages 1-2): Jeffrey S Mumm, Eric H Schroeter, Meera T Saxena, Adam Griesemer, Xiaolin Tian, D.J Pan, William J Ray, and Raphael Kopan. A ligand-induced extracellular cleavage regulates γ-secretase-like proteolytic activation of notch1. Molecular Cell, 5:197-206, Feb 2000. URL: https://doi.org/10.1016/s1097-2765(00)80416-5, doi:10.1016/s1097-2765(00)80416-5. This article has 1206 citations and is from a highest quality peer-reviewed journal.

22. (pan1997kuzbaniancontrolsproteolytic pages 6-7): Duojia Pan and Gerald M Rubin. Kuzbanian controls proteolytic processing of notch and mediates lateral inhibition during drosophila and vertebrate neurogenesis. Cell, 90:271-280, Jul 1997. URL: https://doi.org/10.1016/s0092-8674(00)80335-9, doi:10.1016/s0092-8674(00)80335-9. This article has 705 citations and is from a highest quality peer-reviewed journal.

23. (klein2002kuzbanianisrequired pages 2-5): Thomas Klein. Kuzbanian is required cell autonomously during notch signalling in the drosophila wing. Jun 2002. URL: https://doi.org/10.1007/s00427-002-0233-4, doi:10.1007/s00427-002-0233-4. This article has 29 citations and is from a peer-reviewed journal.

24. (vullings2025anothertailof pages 1-2): Nicole Vüllings, Alina Airich, Ekaterina Seib, Tobias Troost, and Thomas Klein. Another tail of two sites: activation of the notch ligand delta by mindbomb1. BMC biology, 23 1:71, Mar 2025. URL: https://doi.org/10.1186/s12915-025-02162-6, doi:10.1186/s12915-025-02162-6. This article has 1 citations and is from a domain leading peer-reviewed journal.

25. (wang2023aconservedmechanism pages 5-7): Cheng-Wei Wang, Marie Clémot, Takao Hashimoto, Johnny A. Diaz, Lauren M. Goins, Andrew S. Goldstein, Raghavendra Nagaraj, and Utpal Banerjee. A conserved mechanism for jnk-mediated loss of notch function in advanced prostate cancer. Science Signaling, Nov 2023. URL: https://doi.org/10.1126/scisignal.abo5213, doi:10.1126/scisignal.abo5213. This article has 3 citations and is from a domain leading peer-reviewed journal.

26. (bahrampour2020thefivefaces pages 56-59): Shahrzad Bahrampour and Stefan Thor. The five faces of notch signalling during drosophila melanogaster embryonic cns development. Advances in experimental medicine and biology, 1218:39-58, Jan 2020. URL: https://doi.org/10.1007/978-3-030-34436-8\_3, doi:10.1007/978-3-030-34436-8\_3. This article has 14 citations and is from a peer-reviewed journal.

27. (pan1997kuzbaniancontrolsproteolytic pages 4-5): Duojia Pan and Gerald M Rubin. Kuzbanian controls proteolytic processing of notch and mediates lateral inhibition during drosophila and vertebrate neurogenesis. Cell, 90:271-280, Jul 1997. URL: https://doi.org/10.1016/s0092-8674(00)80335-9, doi:10.1016/s0092-8674(00)80335-9. This article has 705 citations and is from a highest quality peer-reviewed journal.

28. (pinot2024spatiotemporalregulationof pages 13-15): Mathieu Pinot and Roland Le Borgne. Spatio-temporal regulation of notch activation in asymmetrically dividing sensory organ precursor cells in drosophila melanogaster epithelium. Cells, 13:1133, Jun 2024. URL: https://doi.org/10.3390/cells13131133, doi:10.3390/cells13131133. This article has 3 citations.

## Artifacts

- [Edison artifact artifact-00](kuz-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](kuz-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. cassar2016analysisofamyloid pages 5-6
2. pan1997kuzbaniancontrolsproteolytic pages 8-9
3. rooke1996kuzaconserved pages 1-2
4. baker2024aninvivo pages 13-17
5. wang2023aconservedmechanism pages 1-4
6. pan1997kuzbaniancontrolsproteolytic pages 1-2
7. baker2024aninvivo pages 10-13
8. baker2024aninvivo pages 38-40
9. baker2024aninvivo pages 30-35
10. bahrampour2020thefivefaces pages 51-53
11. rooke1996kuzaconserved pages 3-4
12. pan1997kuzbaniancontrolsproteolytic pages 2-4
13. pan1997kuzbaniancontrolsproteolytic pages 7-8
14. pinot2024spatiotemporalregulationof pages 2-4
15. klein2002kuzbanianisrequired pages 1-2
16. klein2002kuzbanianisrequired pages 5-5
17. steinbuck2018areviewof pages 2-4
18. ramaker2016amyloidprecursorproteins pages 7-8
19. ramaker2016amyloidprecursorproteins pages 14-15
20. mumm2000aligandinducedextracellular pages 1-2
21. pan1997kuzbaniancontrolsproteolytic pages 6-7
22. klein2002kuzbanianisrequired pages 2-5
23. vullings2025anothertailof pages 1-2
24. wang2023aconservedmechanism pages 5-7
25. bahrampour2020thefivefaces pages 56-59
26. pan1997kuzbaniancontrolsproteolytic pages 4-5
27. pinot2024spatiotemporalregulationof pages 13-15
28. Su(H)
29. *E(spl)*
30. https://doi.org/10.1101/2024.07.10.602225,
31. https://doi.org/10.1126/scisignal.abo5213,
32. https://doi.org/10.1126/science.273.5279.1227,
33. https://doi.org/10.1016/s0092-8674(00
34. https://doi.org/10.1007/978-3-030-34436-8\_3,
35. https://doi.org/10.3390/cells13131133,
36. https://doi.org/10.1007/s00427-002-0233-4,
37. https://doi.org/10.3389/fimmu.2018.01230,
38. https://doi.org/10.1098/rsob.250026,
39. https://doi.org/10.3389/fnmol.2016.00130,
40. https://doi.org/10.3389/fnmol.2016.00061,
41. https://doi.org/10.1016/s1097-2765(00
42. https://doi.org/10.1186/s12915-025-02162-6,