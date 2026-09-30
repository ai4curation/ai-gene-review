---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-30T05:14:52.908335'
end_time: '2026-09-30T05:29:10.557612'
duration_seconds: 857.65
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: mib1
  gene_symbol: mib1
  uniprot_accession: Q9VUX2
  protein_description: 'RecName: Full=E3 ubiquitin-protein ligase mind-bomb {ECO:0000305};
    EC=2.3.2.27; AltName: Full=Mind bomb homolog {ECO:0000303|PubMed:15829515}; Short=D-mib
    {ECO:0000303|PubMed:15829515}; AltName: Full=Protein mind bob 1 {ECO:0000312|FlyBase:FBgn0263601};
    AltName: Full=RING-type E3 ubiquitin transferase mind-bomb {ECO:0000305};'
  gene_info: Name=mib1 {ECO:0000312|FlyBase:FBgn0263601}; ORFNames=CG5841 {ECO:0000312|FlyBase:FBgn0263601};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Not specified in UniProt
  protein_domains: Ankyrin_rpt. (IPR002110); Ankyrin_rpt-contain_sf. (IPR036770);
    MIB1/2_ZZ. (IPR042056); Mib_Herc2. (IPR010606); Mib_Herc2_sf. (IPR037252)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 35
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: mib1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: mib1-deep-research-falcon_artifacts/artifact-01.md
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
- **UniProt Accession:** Q9VUX2
- **Protein Description:** RecName: Full=E3 ubiquitin-protein ligase mind-bomb {ECO:0000305}; EC=2.3.2.27; AltName: Full=Mind bomb homolog {ECO:0000303|PubMed:15829515}; Short=D-mib {ECO:0000303|PubMed:15829515}; AltName: Full=Protein mind bob 1 {ECO:0000312|FlyBase:FBgn0263601}; AltName: Full=RING-type E3 ubiquitin transferase mind-bomb {ECO:0000305};
- **Gene Information:** Name=mib1 {ECO:0000312|FlyBase:FBgn0263601}; ORFNames=CG5841 {ECO:0000312|FlyBase:FBgn0263601};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Ankyrin_rpt. (IPR002110); Ankyrin_rpt-contain_sf. (IPR036770); MIB1/2_ZZ. (IPR042056); Mib_Herc2. (IPR010606); Mib_Herc2_sf. (IPR037252)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "mib1" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'mib1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **mib1** (gene ID: mib1, UniProt: Q9VUX2) in DROME.

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
- **UniProt Accession:** Q9VUX2
- **Protein Description:** RecName: Full=E3 ubiquitin-protein ligase mind-bomb {ECO:0000305}; EC=2.3.2.27; AltName: Full=Mind bomb homolog {ECO:0000303|PubMed:15829515}; Short=D-mib {ECO:0000303|PubMed:15829515}; AltName: Full=Protein mind bob 1 {ECO:0000312|FlyBase:FBgn0263601}; AltName: Full=RING-type E3 ubiquitin transferase mind-bomb {ECO:0000305};
- **Gene Information:** Name=mib1 {ECO:0000312|FlyBase:FBgn0263601}; ORFNames=CG5841 {ECO:0000312|FlyBase:FBgn0263601};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Ankyrin_rpt. (IPR002110); Ankyrin_rpt-contain_sf. (IPR036770); MIB1/2_ZZ. (IPR042056); Mib_Herc2. (IPR010606); Mib_Herc2_sf. (IPR037252)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "mib1" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'mib1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **mib1** (gene ID: mib1, UniProt: Q9VUX2) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: Drosophila mib1 (mind-bomb) Gene

## Gene Identity Verification

The gene mib1 (CG5841, UniProt Q9VUX2) in *Drosophila melanogaster* encodes Mind bomb 1 (Mib1), an E3 ubiquitin-protein ligase (EC 2.3.2.27) that is essential for Notch signaling activation (vullings2025anothertailof pages 1-2). The protein contains characteristic ankyrin repeats (IPR002110) and MIB/HERC2 domains (IPR010606) as specified in the UniProt entry, confirming the correct gene identity.

## Molecular Function and Enzymatic Activity

### Primary Enzymatic Function

Mib1 functions as a RING-type E3 ubiquitin ligase that catalyzes the transfer of ubiquitin from E2 ubiquitin-conjugating enzymes to lysine residues in substrate proteins (seib2021theroleof pages 8-9). The protein is approximately 1200 amino acids in length and contains three C-terminal RING finger domains, of which the terminal RING3 domain is essential for catalytic activity (seib2021theroleof pages 8-9, dho2019proximityinteractionsof pages 1-2). The RING domains bind ubiquitin-charged E2 enzymes and facilitate ubiquitin transfer to substrate lysines, while N-terminal MZM (MIB/HERC2 domains surrounding a ZZ-type zinc finger) and REP (MIB repeat) regions mediate substrate recognition (seib2021theroleof pages 8-9, dho2019proximityinteractionsof pages 1-2).

### Substrate Specificity

The primary physiological substrates of Drosophila Mib1 are the Notch ligands **Delta (Dl)** and **Serrate (Ser)**, both members of the DSL (Delta/Serrate/Lag-2) family of transmembrane proteins (vullings2025anothertailof pages 1-2).

**For Delta:** Mib1 recognizes Delta through a bipartite binding mechanism in which the MZM domain binds the N-box (also called ICD2) and the REP domain binds the C-box (also called ICD3) of Delta's intracellular domain (vullings2025anothertailof pages 1-2). Recent work by Vüllings et al. (2025) demonstrated that full Mib1-dependent activation of Delta requires a combination of six intracellular lysine residues, with **lysine 742 (K742)** being the most important single residue (vullings2025anothertailof pages 1-2). Loss or mutation of these lysines reduces Delta signaling activity and increases cis-inhibition, in which ligand and receptor on the same cell interfere with productive trans-signaling (vullings2025anothertailof pages 1-2). Importantly, Delta retains weak signaling activity even when all intracellular lysines are replaced by arginine (DlK2R variant), indicating that ubiquitination enhances but is not absolutely required for Delta function (troost2023themeaningof pages 1-2).

**For Serrate:** In contrast to Delta, Serrate is more strictly dependent on Mib1-mediated ubiquitination (seib2025theintracellulardomains pages 2-3, seib2025theintracellulardomains pages 1-2). Loss of Mib1 nearly abolishes Serrate endocytosis and signaling, causing Serrate to accumulate at the plasma membrane (seib2025theintracellulardomains pages 1-2). At least five conserved intracellular lysines are required for Mib1-mediated Serrate activation, with approximately six lysines needed for complete signaling and trafficking behavior (seib2025theintracellulardomains pages 2-3, seib2025theintracellulardomains pages 1-2). The five most conserved lysines preferentially support the signaling-relevant endocytic route, while an additional lysine helps restore bulk endocytosis (seib2025theintracellulardomains pages 2-3). Unlike Delta, a lysine-deficient Serrate variant cannot support development, highlighting Serrate's absolute dependence on ubiquitination (seib2025theintracellulardomains pages 2-3, seib2025theintracellulardomains pages 1-2).

| Substrate or feature | Ubiquitination sites | Functional requirement | Key findings |
| --- | --- | --- | --- |
| **Delta (Dl)** | Six intracellular lysines collectively support full Mib1-dependent activity; **K742** is the most important identified residue. | Ubiquitination is required for maximal Mib1-dependent signaling and productive endocytosis, but a lysine-less Delta variant retains weak activity. | MZM binds the Delta N-box in ICD2, while REP binds the C-box in ICD3. Loss of relevant lysines reduces trans-activation and increases cis-inhibition. (vullings2025anothertailof pages 1-2, troost2023themeaningof pages 1-2, vullings2025anothertailof pages 2-4) |
| **Serrate (Ser)** | At least **five conserved intracellular lysines** support signaling; approximately **six lysines** are needed for complete signaling and trafficking behavior. | Serrate is more strictly dependent than Delta on Mib1-mediated ubiquitination. Loss of intracellular lysines or Mib1 nearly abolishes Serrate endocytosis and signaling. | Five conserved lysines preferentially support signaling-relevant endocytosis; an additional lysine helps restore bulk endocytosis. Ubiquitination also regulates degradation and cis-inhibition. (seib2025theintracellulardomains pages 2-3, seib2025theintracellulardomains pages 1-2, seib2021theroleof pages 8-9) |
| **Catalytic RING region** | Not an acceptor substrate; recruits an E2–ubiquitin conjugate for transfer of ubiquitin to ligand lysines. | Mib1 contains three C-terminal RING fingers; the terminal **RING3** is required for demonstrated catalytic activity. | RING-defective variants fail to ubiquitinate substrates. The resulting ubiquitination commonly regulates trafficking rather than proteasomal degradation. (seib2021theroleof pages 8-9, dho2019proximityinteractionsof pages 1-2, dho2019proximityinteractionsof pages 2-4) |
| **MZM recognition region** | Not an acceptor-site class; recognizes ligand-tail motifs before ubiquitin transfer. | Required for productive substrate recognition; it binds the Delta N-box in ICD2. | MZM contains MIB/HERC-related elements surrounding a ZZ-type zinc finger. Deleting MZM while retaining REP can produce dominant-negative Notch defects. (seib2021theroleof pages 8-9, dho2019proximityinteractionsof pages 1-2, vullings2025anothertailof pages 8-10) |
| **REP recognition region** | Not an acceptor-site class; recognizes a second ligand-tail determinant. | Cooperates with MZM in bipartite substrate recognition; it binds the Delta C-box in ICD3. | REP helps position the ligand intracellular domain for ubiquitination and contributes to interfering interactions when MZM is absent. (vullings2025anothertailof pages 1-2, dho2019proximityinteractionsof pages 1-2, vullings2025anothertailof pages 8-10) |
| **Overall specificity** | The best-supported direct Drosophila targets are lysines in the cytoplasmic tails of Delta and Serrate. | Mib1-dependent ubiquitination selects ligands for signaling-competent, Epsin-associated endocytosis rather than controlling all bulk uptake. | The primary outcome is non-proteolytic activation and trafficking of Notch ligands in signal-sending cells. Delta retains alternative activity, whereas Serrate is strongly Mib1- and lysine-dependent. (troost2023themeaningof pages 1-2, seib2021theroleof pages 9-11, seib2021theroleof pages 6-8, seib2025theintracellulardomains pages 2-3) |


*Table: Summary of the experimentally supported Drosophila Mib1 substrates, lysine requirements, and functional domains. It highlights the stronger dependence of Serrate than Delta on Mib1-mediated ubiquitination.*

## Subcellular Localization

Mib1 functions primarily at the **plasma membrane** and in **endocytic compartments** of signal-sending cells (dho2019proximityinteractionsof pages 2-4, dho2019proximityinteractionsof pages 9-12). Studies in mammalian epithelial cells show that MIB1 localizes to the lateral membrane and tight junctions, where it colocalizes with epithelial polarity proteins including CRB1, CRB3, and ZO1 (dho2019proximityinteractionsof pages 9-12). The protein also associates with centrosomal and pericentriolar satellite structures (dho2019proximityinteractionsof pages 2-4, dho2019proximityinteractionsof pages 9-12). Functionally, Mib1 is associated with clathrin-coated pits and endocytic machinery components including Epsin, EPS15, and FCHO2 (dho2019proximityinteractionsof pages 2-4, dho2019proximityinteractionsof pages 4-5). The ligase ubiquitinates ligands at or near the plasma membrane to initiate their internalization through clathrin-mediated endocytosis (seib2021theroleof pages 9-11, seib2021theroleof pages 6-8).

## Role in Notch Signaling Pathway

### Mechanism of Notch Activation

Mib1 plays a central role in activating the Notch signaling pathway through a sophisticated mechanotransduction mechanism (vullings2025anothertailof pages 1-2, seib2021theroleof pages 3-4, sprinzak2021biophysicsofnotch pages 1-3). The pathway operates as follows:

1. **Ligand Ubiquitination:** In the signal-sending cell, Mib1 ubiquitinates the intracellular domains of Delta and Serrate ligands at the plasma membrane (vullings2025anothertailof pages 1-2, troost2023themeaningof pages 1-2).

2. **Epsin Recruitment:** Ubiquitinated ligands are recognized by the endocytic adaptor protein Epsin (Liquid facets in *Drosophila*) through its ubiquitin-interacting motifs (troost2023themeaningof pages 1-2, seib2021theroleof pages 9-11, seib2021theroleof pages 6-8). This coupling to Epsin is crucial because it directs ligands into a specialized, signaling-competent endocytic pathway distinct from bulk endocytosis (seib2021theroleof pages 9-11, seib2021theroleof pages 6-8).

3. **Force Generation:** When the ligand binds to Notch receptors on an adjacent signal-receiving cell (trans-interaction), ligand endocytosis generates a mechanical pulling force that is transmitted through the ligand-receptor bond (seib2021theroleof pages 3-4, sprinzak2021biophysicsofnotch pages 1-3, lv2024evolutionandfunction pages 2-4, sprinzak2021biophysicsofnotch pages 11-13). This force has been estimated at 2–5 pN based on measurements of Dll1 endocytosis stalling forces, which is below the ~19 pN rupture force of the Notch1–Dll1 bond, allowing pulling without breaking the interaction (sprinzak2021biophysicsofnotch pages 11-13).

4. **Mechanotransduction:** The pulling force induces conformational changes in Notch's negative regulatory region (NRR), which normally shields the S2 cleavage site (seib2021theroleof pages 3-4, sprinzak2021biophysicsofnotch pages 1-3, lv2024evolutionandfunction pages 2-4, seib2021theroleof pages 1-3). Force-dependent opening of the NRR exposes this previously inaccessible site.

5. **Proteolytic Processing:** Once exposed, the metalloprotease ADAM10 (Kuzbanian in *Drosophila*) cleaves Notch at the S2 site, generating the membrane-tethered NEXT fragment (sprinzak2021biophysicsofnotch pages 1-3, lv2024evolutionandfunction pages 2-4, seib2021theroleof pages 1-3). The γ-secretase complex then performs intramembrane cleavage at S3, releasing the Notch intracellular domain (NICD) (sprinzak2021biophysicsofnotch pages 1-3, lv2024evolutionandfunction pages 2-4).

6. **Transcriptional Activation:** NICD enters the nucleus and forms a transcriptional activation complex with RBPJ/CSL and Mastermind family cofactors (MAML), activating expression of Notch target genes (lv2024evolutionandfunction pages 2-4, sprinzak2021biophysicsofnotch pages 1-3).

The endocytic machinery, including clathrin-coated pit formation, actin polymerization coordinated through WASP/ARP2/3, and dynamin-mediated scission, collectively generate the mechanical forces required for this activation mechanism (seib2021theroleof pages 13-14, seib2021theroleof pages 11-13).

### Regulation of Cis-Inhibition

Mib1-mediated endocytosis also plays an important role in reducing cis-inhibition, whereby ligands and receptors on the same cell form non-productive interactions that suppress signaling (vullings2025anothertailof pages 8-10, seib2025theintracellulardomains pages 2-3). By promoting ligand internalization and potentially recycling ligands back to the surface in a modified state, Mib1 helps separate cis-interacting pairs and enhance productive trans-signaling to neighboring cells (vullings2025anothertailof pages 8-10, seib2021theroleof pages 11-13).

## Relationship with Neuralized (Neur)

In *Drosophila*, Mib1 functions alongside another E3 ubiquitin ligase called Neuralized (Neur), and the two proteins have complementary but distinct roles in activating Notch ligands (kalodimou2023separablerolesfor pages 14-15, troost2023themeaningof pages 1-2, kalodimou2023separablerolesfor pages 17-19, vullings2025anothertailof pages 1-2).

### Molecular Distinctions

The two ligases differ in their substrate recognition mechanisms and functional modes:

- **Substrate Binding:** Mib1 binds Delta through N-box (ICD2) and C-box (ICD3) motifs via its MZM and REP domains, whereas Neur recognizes an NxxN "Neur-box" motif (NEQN in Delta) in ICD1 through its NHR1 domain (kalodimou2023separablerolesfor pages 17-19, seib2021theroleof pages 8-9).

- **Functional Mode:** Mib1 acts primarily as a transient catalytic ubiquitin ligase requiring Delta lysines for robust signaling (kalodimou2023separablerolesfor pages 17-19, troost2023themeaningof pages 1-2). Neur, in contrast, has dual functionality: it can both ubiquitinate Delta and serve as an endocytic co-adaptor forming a stable Delta–Neur complex (kalodimou2023separablerolesfor pages 14-15, kalodimou2023separablerolesfor pages 17-19). Consequently, Neur can activate lysine-deficient Delta variants, whereas Mib1 activity is more strictly ubiquitination-dependent (kalodimou2023separablerolesfor pages 14-15, troost2023themeaningof pages 1-2).

### Developmental Context

The two ligases show distinct expression patterns and developmental deployment:

- **Mib1** is expressed ubiquitously in wing imaginal discs and is the dominant Delta-activating ligase in wing patterning, including dorsal-ventral boundary specification (vullings2025anothertailof pages 1-2, vullings2025anothertailof pages 2-4).

- **Neuralized** is restricted primarily to late-arising sensory organ precursor cells in the peripheral nervous system and is the predominant ligase in embryonic neuroblast selection and CNS ganglion mother cell (GMC) sibling specification (kalodimou2023separablerolesfor pages 14-15, kalodimou2023separablerolesfor pages 5-7, kalodimou2023separablerolesfor pages 15-17).

Loss of Neur causes strong neurogenic phenotypes with neural hyperplasia, whereas loss of Mib1 alone does not produce the same defect in embryonic neuroblast selection, demonstrating context-specific requirements (kalodimou2023separablerolesfor pages 15-17).

| Feature | Mib1 (Mind bomb 1) | Neuralized (Neur) |
|---|---|---|
| Protein class and architecture | Large RING-type E3 ubiquitin ligase with N-terminal MZM and REP substrate-recognition regions, eight ankyrin repeats, and three C-terminal RING fingers; the terminal RING finger is essential for catalytic activity. (seib2021theroleof pages 8-9, dho2019proximityinteractionsof pages 1-2) | RING-type E3 ubiquitin ligase containing NHR1 and NHR2 regions plus a catalytic RING domain; NHR1 recognizes ligand, while NHR2 contributes to oligomerization and full E3 activity. (seib2021theroleof pages 8-9) |
| Delta-binding determinants | MZM and REP recognize Delta intracellular N-box/ICD2 and C-box/ICD3 regions, respectively, forming a bipartite interaction. (vullings2025anothertailof pages 1-2) | NHR1 binds an NxxN “Neur-box” motif—NEQN in Delta—located principally in ICD1; weaker interaction with ICD2 has also been reported. (kalodimou2023separablerolesfor pages 17-19, seib2021theroleof pages 8-9) |
| Primary biochemical mode | Transfers ubiquitin to multiple lysines in the Delta intracellular domain; full Mib1-dependent signaling requires a combination of six lysines, with K742 contributing most strongly. (vullings2025anothertailof pages 1-2) | Can ubiquitinate Delta but also acts as an endocytic co-adaptor in a stable Delta–Neur complex; consequently, some Neur-dependent signaling persists when Delta lysines or the Neur RING domain are compromised. (kalodimou2023separablerolesfor pages 14-15, kalodimou2023separablerolesfor pages 17-19) |
| Dependence on Delta ubiquitination | Strongly ubiquitination-dependent: intracellular Delta lysines are needed for robust ligand activation and productive endocytosis in Mib1-dependent contexts. (troost2023themeaningof pages 1-2) | Not strictly dependent on ubiquitination of Delta itself; Neur can activate lysine-deficient Delta, although ubiquitination of another complex component may enhance signaling. (kalodimou2023separablerolesfor pages 17-19, kalodimou2023separablerolesfor pages 14-15) |
| Interaction with endocytosis | Mib1-mediated ligand ubiquitination promotes recognition by Epsin/Liquid facets and entry into signaling-relevant endocytosis that generates force for Notch activation. (seib2021theroleof pages 9-11, seib2021theroleof pages 6-8) | Neur can participate directly in a dynamin-dependent endocytic complex; in some CNS lineage signaling, this mode is reported to be Epsin-independent. (kalodimou2023separablerolesfor pages 17-19) |
| Expression pattern in the wing disc | Broadly or ubiquitously expressed in the wing imaginal disc, making it the principal Delta-activating ligase in most of the wing pouch. (vullings2025anothertailof pages 1-2, vullings2025anothertailof pages 2-4) | Restricted mainly to late-arising sensory-organ precursor cells rather than broadly expressed throughout the wing pouch. (vullings2025anothertailof pages 1-2) |
| Predominant developmental contexts | Dominant in wing-disc Notch signaling, including dorsal–ventral boundary specification, where Delta lysines are important and Neur is absent from most of the wing pouch. (kalodimou2023separablerolesfor pages 14-15, vullings2025anothertailof pages 2-4) | Predominant in sensory-organ precursor selection, embryonic neuroblast selection, and ganglion-mother-cell sibling specification in the CNS. (kalodimou2023separablerolesfor pages 5-7, kalodimou2023separablerolesfor pages 15-17) |
| Functional relationship | Overlaps with Neur but primarily behaves as a transient catalytic modifier of Delta; it can provide backup activity in some Neur-dominated contexts. (kalodimou2023separablerolesfor pages 17-19, kalodimou2023separablerolesfor pages 5-7) | Overlaps with Mib1 but combines catalytic and adaptor functions, allowing stronger or mechanistically distinct Delta activation in selected neural contexts. (kalodimou2023separablerolesfor pages 14-15, kalodimou2023separablerolesfor pages 17-19) |
| Best-supported distinction | Broadly deployed, substrate-ubiquitination-dependent ligand activator. | Developmentally restricted ligand activator that can couple Delta to endocytosis independently of ubiquitinating Delta itself. |


*Table: Comparison of the domain architecture, Delta-recognition mechanisms, ubiquitination requirements, expression patterns, and developmental deployment of the two Drosophila Notch-ligand E3 ligases.*

## Biological Processes and Developmental Roles

Mib1 is essential for numerous Notch-dependent developmental processes in *Drosophila* (vullings2025anothertailof pages 8-10, troost2023themeaningof pages 1-2). In wing imaginal discs, Mib1 is required for full Delta signaling activity, and loss of Mib1 strongly suppresses Delta-dependent Notch activation (vullings2025anothertailof pages 8-10). Expression of Mib1 under the tubulin promoter can restore Notch pathway activation in mib1 mutant contexts (vullings2025anothertailof pages 8-10).

Mib1 variants lacking the MZM domain while retaining REP produce dominant-negative effects, causing severe Notch-related developmental defects, near sterility, and reduced survival (vullings2025anothertailof pages 8-10). This suggests that the REP domain can mediate interfering interactions when MZM is absent, highlighting the importance of balanced domain function (vullings2025anothertailof pages 8-10).

Interestingly, a Delta variant lacking all intracellular lysines (DlK2R) can provide sufficient activity to support complete development of *Drosophila* when present as a single genomic copy, although ubiquitination is required for full signaling strength (troost2023themeaningof pages 1-2). This indicates that while Mib1-dependent ubiquitination is important for robust Notch signaling, alternative activation mechanisms (particularly through Neuralized) can compensate under physiological conditions (troost2023themeaningof pages 1-2).

## Notch-Independent Functions

While Mib1's best-characterized role in *Drosophila* is in Notch ligand activation, studies in vertebrate systems have revealed Notch-independent functions that may be conserved. In zebrafish, Mib1 regulates planar cell polarity (PCP)-dependent convergent extension movements during gastrulation independently of Notch signaling (saraswathy2022thee3ubiquitin pages 1-2, saraswathy2021thee3ubiquitin pages 4-7, saraswathy2021thee3ubiquitin pages 9-11). This function involves Mib1-mediated ubiquitination and endocytosis of the PCP component Ryk, a receptor-like tyrosine kinase (saraswathy2022thee3ubiquitin pages 1-2, saraswathy2021thee3ubiquitin pages 9-11). Loss of zebrafish mib1 impairs convergent extension, and this defect can be rescued by the PCP effector RhoA or by Ryk, but not by constitutively active Notch (NICD), demonstrating that the function is Notch-independent (saraswathy2022thee3ubiquitin pages 1-2, saraswathy2021thee3ubiquitin pages 4-7). Whether similar PCP-related functions exist for Drosophila Mib1 requires further investigation, though current literature on *Drosophila* mib1 focuses primarily on its Notch-related roles (vullings2025anothertailof pages 8-10, troost2023themeaningof pages 1-2, vullings2025anothertailof pages 1-2).

## Domain Structure and Functional Regions

Mib1 is organized into several functionally distinct regions (seib2021theroleof pages 8-9, dho2019proximityinteractionsof pages 1-2):

1. **N-terminal MZM region:** Contains two MIB/HERC2 homology domains flanking a ZZ-type zinc finger. This region binds the N-box/ICD2 of Delta and is essential for substrate recognition (seib2021theroleof pages 8-9, dho2019proximityinteractionsof pages 1-2).

2. **REP region:** Contains two adjacent MIB homology repeats that bind the C-box/ICD3 of Delta, completing the bipartite substrate interaction (seib2021theroleof pages 8-9, dho2019proximityinteractionsof pages 1-2).

3. **Ankyrin repeats:** Eight central ankyrin repeats contribute to the protein's structural organization (seib2021theroleof pages 8-9).

4. **Three C-terminal RING fingers:** These provide E3 ubiquitin ligase activity, with RING3 being the only RING domain demonstrated as essential for ubiquitination of characterized substrates (seib2021theroleof pages 8-9, dho2019proximityinteractionsof pages 1-2, dho2019proximityinteractionsof pages 2-4). A coiled-coil region is located between RING2 and RING3 (dho2019proximityinteractionsof pages 1-2).

Deletion or mutation studies confirm that the RING domains are required for catalytic activity—RING-defective mutants cannot ubiquitinate substrates—while the MZM/REP regions are required for substrate binding and proper ligand activation (dho2019proximityinteractionsof pages 8-9, dho2019proximityinteractionsof pages 4-5, dho2019proximityinteractionsof pages 2-4).

## Current Understanding and Recent Developments (2023–2025)

Recent studies have significantly advanced our understanding of Mib1 function:

1. **Bipartite Binding Mechanism (Vüllings et al., 2025):** The most recent work demonstrates that Drosophila Mib1 activates Delta through a bipartite binding mechanism similar to mammalian MIB1-JAG1 interactions, with both N-box and C-box interactions required for full activity (vullings2025anothertailof pages 1-2). This study identified K742 as the most important among six critical lysines in Delta's intracellular domain (vullings2025anothertailof pages 1-2).

2. **Ligand-Specific Requirements (Seib et al., 2025):** Work published in late 2024/early 2025 revealed that Serrate is more strictly dependent on Mib1-mediated ubiquitination than Delta, with at least five conserved lysines required for signaling (seib2025theintracellulardomains pages 2-3, seib2025theintracellulardomains pages 1-2). This contrasts with Delta, which retains residual activity without ubiquitination (seib2025theintracellulardomains pages 2-3).

3. **Ubiquitination-Independent Signaling Modes (Troost et al., 2023; Kalodimou et al., 2023):** These studies demonstrated that Delta can signal through multiple modes—some ubiquitination-dependent (Mib1-mediated) and some ubiquitination-independent (primarily Neur-mediated)—and that these modes have different developmental requirements (troost2023themeaningof pages 1-2, kalodimou2023separablerolesfor pages 17-19).

4. **Mechanotransduction Models (Sprinzak & Blacklow, 2021; Seib & Klein, 2021):** Comprehensive reviews have clarified the mechanotransduction mechanism by which ligand endocytosis generates force to activate Notch, with quantitative estimates of forces involved (seib2021theroleof pages 3-4, sprinzak2021biophysicsofnotch pages 1-3, sprinzak2021biophysicsofnotch pages 11-13, seib2021theroleof pages 1-3).

## Conclusions

Drosophila Mib1 is a RING-type E3 ubiquitin ligase that serves as a critical regulator of Notch signaling by ubiquitinating the intracellular domains of Notch ligands Delta and Serrate. Its primary molecular function is to catalyze ubiquitin transfer to specific lysine residues in these ligands (K742 and five others in Delta; at least five conserved lysines in Serrate), thereby promoting their recognition by the endocytic adaptor Epsin and entry into a specialized endocytic pathway. This ubiquitination-dependent endocytosis generates mechanical force that pulls on Notch receptors in adjacent cells, inducing the conformational changes required for proteolytic activation and downstream signaling.

Mib1 functions at the plasma membrane and in endocytic compartments of signal-sending cells, where it collaborates with clathrin-mediated endocytic machinery. It works complementarily with Neuralized, another E3 ligase, with the two proteins showing different binding mechanisms, expression patterns, and developmental contexts. While Mib1 is broadly expressed and dominates in wing disc patterning, Neuralized is restricted to neural contexts and can activate Delta through ubiquitination-independent mechanisms.

The protein's approximately 1200-amino-acid structure includes N-terminal MZM and REP substrate-recognition domains that mediate bipartite binding to ligand intracellular motifs, central ankyrin repeats, and three C-terminal RING fingers that provide catalytic activity. Recent structural and functional studies (2023–2025) have revealed ligand-specific differences in ubiquitination requirements, with Serrate being more strictly dependent on Mib1 than Delta, and have clarified the mechanotransduction mechanism underlying force-dependent Notch activation.

References

1. (vullings2025anothertailof pages 1-2): Nicole Vüllings, Alina Airich, Ekaterina Seib, Tobias Troost, and Thomas Klein. Another tail of two sites: activation of the notch ligand delta by mindbomb1. BMC biology, 23 1:71, Mar 2025. URL: https://doi.org/10.1186/s12915-025-02162-6, doi:10.1186/s12915-025-02162-6. This article has 1 citations and is from a domain leading peer-reviewed journal.

2. (seib2021theroleof pages 8-9): Ekaterina Seib and Thomas Klein. The role of ligand endocytosis in notch signalling. Biology of the Cell, 113:401-418, Jun 2021. URL: https://doi.org/10.1111/boc.202100009, doi:10.1111/boc.202100009. This article has 44 citations and is from a peer-reviewed journal.

3. (dho2019proximityinteractionsof pages 1-2): Sascha E. Dho, Nancy Silva-Gagliardi, Fabio Morgese, Etienne Coyaud, Emily Lamoureux, Donna M. Berry, Brian Raught, and C. Jane McGlade. Proximity interactions of the ubiquitin ligase mind bomb 1 reveal a role in regulation of epithelial polarity complex proteins. Scientific Reports, Aug 2019. URL: https://doi.org/10.1038/s41598-019-48902-x, doi:10.1038/s41598-019-48902-x. This article has 41 citations and is from a peer-reviewed journal.

4. (troost2023themeaningof pages 1-2): Tobias Troost, Ekaterina Seib, Alina Airich, Nicole Vüllings, Aleksandar Necakov, Stefano De Renzis, and Thomas Klein. The meaning of ubiquitylation of the dsl ligand delta for the development of drosophila. BMC Biology, Nov 2023. URL: https://doi.org/10.1186/s12915-023-01759-z, doi:10.1186/s12915-023-01759-z. This article has 9 citations and is from a domain leading peer-reviewed journal.

5. (seib2025theintracellulardomains pages 2-3): Ekaterina Seib, Maya Schmid, Hideyuki Shimizu, Tobias Troost, Sunday Faith Oyelere, Biswajit Chakraborty, Martin Baron, and Thomas Klein. The intracellular domains of the dsl ligands serrate and delta provide different activities. Cell Communication and Signaling, Oct 2025. URL: https://doi.org/10.1186/s12964-025-02472-w, doi:10.1186/s12964-025-02472-w. This article has 0 citations and is from a peer-reviewed journal.

6. (seib2025theintracellulardomains pages 1-2): Ekaterina Seib, Maya Schmid, Hideyuki Shimizu, Tobias Troost, Sunday Faith Oyelere, Biswajit Chakraborty, Martin Baron, and Thomas Klein. The intracellular domains of the dsl ligands serrate and delta provide different activities. Cell Communication and Signaling, Oct 2025. URL: https://doi.org/10.1186/s12964-025-02472-w, doi:10.1186/s12964-025-02472-w. This article has 0 citations and is from a peer-reviewed journal.

7. (vullings2025anothertailof pages 2-4): Nicole Vüllings, Alina Airich, Ekaterina Seib, Tobias Troost, and Thomas Klein. Another tail of two sites: activation of the notch ligand delta by mindbomb1. BMC biology, 23 1:71, Mar 2025. URL: https://doi.org/10.1186/s12915-025-02162-6, doi:10.1186/s12915-025-02162-6. This article has 1 citations and is from a domain leading peer-reviewed journal.

8. (dho2019proximityinteractionsof pages 2-4): Sascha E. Dho, Nancy Silva-Gagliardi, Fabio Morgese, Etienne Coyaud, Emily Lamoureux, Donna M. Berry, Brian Raught, and C. Jane McGlade. Proximity interactions of the ubiquitin ligase mind bomb 1 reveal a role in regulation of epithelial polarity complex proteins. Scientific Reports, Aug 2019. URL: https://doi.org/10.1038/s41598-019-48902-x, doi:10.1038/s41598-019-48902-x. This article has 41 citations and is from a peer-reviewed journal.

9. (vullings2025anothertailof pages 8-10): Nicole Vüllings, Alina Airich, Ekaterina Seib, Tobias Troost, and Thomas Klein. Another tail of two sites: activation of the notch ligand delta by mindbomb1. BMC biology, 23 1:71, Mar 2025. URL: https://doi.org/10.1186/s12915-025-02162-6, doi:10.1186/s12915-025-02162-6. This article has 1 citations and is from a domain leading peer-reviewed journal.

10. (seib2021theroleof pages 9-11): Ekaterina Seib and Thomas Klein. The role of ligand endocytosis in notch signalling. Biology of the Cell, 113:401-418, Jun 2021. URL: https://doi.org/10.1111/boc.202100009, doi:10.1111/boc.202100009. This article has 44 citations and is from a peer-reviewed journal.

11. (seib2021theroleof pages 6-8): Ekaterina Seib and Thomas Klein. The role of ligand endocytosis in notch signalling. Biology of the Cell, 113:401-418, Jun 2021. URL: https://doi.org/10.1111/boc.202100009, doi:10.1111/boc.202100009. This article has 44 citations and is from a peer-reviewed journal.

12. (dho2019proximityinteractionsof pages 9-12): Sascha E. Dho, Nancy Silva-Gagliardi, Fabio Morgese, Etienne Coyaud, Emily Lamoureux, Donna M. Berry, Brian Raught, and C. Jane McGlade. Proximity interactions of the ubiquitin ligase mind bomb 1 reveal a role in regulation of epithelial polarity complex proteins. Scientific Reports, Aug 2019. URL: https://doi.org/10.1038/s41598-019-48902-x, doi:10.1038/s41598-019-48902-x. This article has 41 citations and is from a peer-reviewed journal.

13. (dho2019proximityinteractionsof pages 4-5): Sascha E. Dho, Nancy Silva-Gagliardi, Fabio Morgese, Etienne Coyaud, Emily Lamoureux, Donna M. Berry, Brian Raught, and C. Jane McGlade. Proximity interactions of the ubiquitin ligase mind bomb 1 reveal a role in regulation of epithelial polarity complex proteins. Scientific Reports, Aug 2019. URL: https://doi.org/10.1038/s41598-019-48902-x, doi:10.1038/s41598-019-48902-x. This article has 41 citations and is from a peer-reviewed journal.

14. (seib2021theroleof pages 3-4): Ekaterina Seib and Thomas Klein. The role of ligand endocytosis in notch signalling. Biology of the Cell, 113:401-418, Jun 2021. URL: https://doi.org/10.1111/boc.202100009, doi:10.1111/boc.202100009. This article has 44 citations and is from a peer-reviewed journal.

15. (sprinzak2021biophysicsofnotch pages 1-3): David Sprinzak and Stephen C. Blacklow. Biophysics of notch signaling. Annual Review of Biophysics, 50:157-189, May 2021. URL: https://doi.org/10.1146/annurev-biophys-101920-082204, doi:10.1146/annurev-biophys-101920-082204. This article has 280 citations and is from a domain leading peer-reviewed journal.

16. (lv2024evolutionandfunction pages 2-4): Yan Lv, Xuan Pang, Zhonghong Cao, Changping Song, Baohua Liu, Weiwei Wu, and Qiuxiang Pang. Evolution and function of the notch signaling pathway: an invertebrate perspective. International Journal of Molecular Sciences, 25:3322, Mar 2024. URL: https://doi.org/10.3390/ijms25063322, doi:10.3390/ijms25063322. This article has 36 citations.

17. (sprinzak2021biophysicsofnotch pages 11-13): David Sprinzak and Stephen C. Blacklow. Biophysics of notch signaling. Annual Review of Biophysics, 50:157-189, May 2021. URL: https://doi.org/10.1146/annurev-biophys-101920-082204, doi:10.1146/annurev-biophys-101920-082204. This article has 280 citations and is from a domain leading peer-reviewed journal.

18. (seib2021theroleof pages 1-3): Ekaterina Seib and Thomas Klein. The role of ligand endocytosis in notch signalling. Biology of the Cell, 113:401-418, Jun 2021. URL: https://doi.org/10.1111/boc.202100009, doi:10.1111/boc.202100009. This article has 44 citations and is from a peer-reviewed journal.

19. (seib2021theroleof pages 13-14): Ekaterina Seib and Thomas Klein. The role of ligand endocytosis in notch signalling. Biology of the Cell, 113:401-418, Jun 2021. URL: https://doi.org/10.1111/boc.202100009, doi:10.1111/boc.202100009. This article has 44 citations and is from a peer-reviewed journal.

20. (seib2021theroleof pages 11-13): Ekaterina Seib and Thomas Klein. The role of ligand endocytosis in notch signalling. Biology of the Cell, 113:401-418, Jun 2021. URL: https://doi.org/10.1111/boc.202100009, doi:10.1111/boc.202100009. This article has 44 citations and is from a peer-reviewed journal.

21. (kalodimou2023separablerolesfor pages 14-15): Konstantina Kalodimou, Margarita Stapountzi, Nicole Vüllings, Ekaterina Seib, Thomas Klein, and Christos Delidakis. Separable roles for neur and ubiquitin in delta signalling in the drosophila cns lineages. Cells, 12:2833, Dec 2023. URL: https://doi.org/10.3390/cells12242833, doi:10.3390/cells12242833. This article has 4 citations.

22. (kalodimou2023separablerolesfor pages 17-19): Konstantina Kalodimou, Margarita Stapountzi, Nicole Vüllings, Ekaterina Seib, Thomas Klein, and Christos Delidakis. Separable roles for neur and ubiquitin in delta signalling in the drosophila cns lineages. Cells, 12:2833, Dec 2023. URL: https://doi.org/10.3390/cells12242833, doi:10.3390/cells12242833. This article has 4 citations.

23. (kalodimou2023separablerolesfor pages 5-7): Konstantina Kalodimou, Margarita Stapountzi, Nicole Vüllings, Ekaterina Seib, Thomas Klein, and Christos Delidakis. Separable roles for neur and ubiquitin in delta signalling in the drosophila cns lineages. Cells, 12:2833, Dec 2023. URL: https://doi.org/10.3390/cells12242833, doi:10.3390/cells12242833. This article has 4 citations.

24. (kalodimou2023separablerolesfor pages 15-17): Konstantina Kalodimou, Margarita Stapountzi, Nicole Vüllings, Ekaterina Seib, Thomas Klein, and Christos Delidakis. Separable roles for neur and ubiquitin in delta signalling in the drosophila cns lineages. Cells, 12:2833, Dec 2023. URL: https://doi.org/10.3390/cells12242833, doi:10.3390/cells12242833. This article has 4 citations.

25. (saraswathy2022thee3ubiquitin pages 1-2): Vishnu Muraleedharan Saraswathy, Akshai Janardhana Kurup, Priyanka Sharma, Sophie Polès, Morgane Poulain, and Maximilian Fürthauer. The e3 ubiquitin ligase mindbomb1 controls planar cell polarity-dependent convergent extension movements during zebrafish gastrulation. eLife, Feb 2022. URL: https://doi.org/10.7554/elife.71928, doi:10.7554/elife.71928. This article has 8 citations and is from a domain leading peer-reviewed journal.

26. (saraswathy2021thee3ubiquitin pages 4-7): Vishnu Muraleedharan Saraswathy, Priyanka Sharma, Akshai Janardhana Kurup, Sophie Polès, Morgane Poulain, and Maximilian Fürthauer. The e3 ubiquitin ligase mindbomb1 controls zebrafish planar cell polarity. bioRxiv, Jul 2021. URL: https://doi.org/10.1101/2021.07.05.451064, doi:10.1101/2021.07.05.451064. This article has 0 citations.

27. (saraswathy2021thee3ubiquitin pages 9-11): Vishnu Muraleedharan Saraswathy, Priyanka Sharma, Akshai Janardhana Kurup, Sophie Polès, Morgane Poulain, and Maximilian Fürthauer. The e3 ubiquitin ligase mindbomb1 controls zebrafish planar cell polarity. bioRxiv, Jul 2021. URL: https://doi.org/10.1101/2021.07.05.451064, doi:10.1101/2021.07.05.451064. This article has 0 citations.

28. (dho2019proximityinteractionsof pages 8-9): Sascha E. Dho, Nancy Silva-Gagliardi, Fabio Morgese, Etienne Coyaud, Emily Lamoureux, Donna M. Berry, Brian Raught, and C. Jane McGlade. Proximity interactions of the ubiquitin ligase mind bomb 1 reveal a role in regulation of epithelial polarity complex proteins. Scientific Reports, Aug 2019. URL: https://doi.org/10.1038/s41598-019-48902-x, doi:10.1038/s41598-019-48902-x. This article has 41 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](mib1-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](mib1-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. vullings2025anothertailof pages 1-2
2. seib2021theroleof pages 8-9
3. troost2023themeaningof pages 1-2
4. seib2025theintracellulardomains pages 1-2
5. seib2025theintracellulardomains pages 2-3
6. dho2019proximityinteractionsof pages 9-12
7. sprinzak2021biophysicsofnotch pages 11-13
8. kalodimou2023separablerolesfor pages 15-17
9. kalodimou2023separablerolesfor pages 17-19
10. vullings2025anothertailof pages 8-10
11. dho2019proximityinteractionsof pages 1-2
12. vullings2025anothertailof pages 2-4
13. dho2019proximityinteractionsof pages 2-4
14. seib2021theroleof pages 9-11
15. seib2021theroleof pages 6-8
16. dho2019proximityinteractionsof pages 4-5
17. seib2021theroleof pages 3-4
18. sprinzak2021biophysicsofnotch pages 1-3
19. lv2024evolutionandfunction pages 2-4
20. seib2021theroleof pages 1-3
21. seib2021theroleof pages 13-14
22. seib2021theroleof pages 11-13
23. kalodimou2023separablerolesfor pages 14-15
24. kalodimou2023separablerolesfor pages 5-7
25. dho2019proximityinteractionsof pages 8-9
26. https://doi.org/10.1186/s12915-025-02162-6,
27. https://doi.org/10.1111/boc.202100009,
28. https://doi.org/10.1038/s41598-019-48902-x,
29. https://doi.org/10.1186/s12915-023-01759-z,
30. https://doi.org/10.1186/s12964-025-02472-w,
31. https://doi.org/10.1146/annurev-biophys-101920-082204,
32. https://doi.org/10.3390/ijms25063322,
33. https://doi.org/10.3390/cells12242833,
34. https://doi.org/10.7554/elife.71928,
35. https://doi.org/10.1101/2021.07.05.451064,