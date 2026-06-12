---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-06-11T21:42:13.285055'
end_time: '2026-06-11T22:18:52.184321'
duration_seconds: 2198.9
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: EMC2
  gene_symbol: EMC2
  uniprot_accession: Q15006
  protein_description: 'RecName: Full=ER membrane protein complex subunit 2 {ECO:0000305};
    AltName: Full=Tetratricopeptide repeat protein 35 {ECO:0000312|HGNC:HGNC:28963};
    Short=TPR repeat protein 35 {ECO:0000312|HGNC:HGNC:28963};'
  gene_info: Name=EMC2 {ECO:0000312|HGNC:HGNC:28963}; Synonyms=KIAA0103 {ECO:0000312|EMBL:BAA03493.1},
    TTC35 {ECO:0000312|HGNC:HGNC:28963};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the EMC2 family. .
  protein_domains: EMC2-like. (IPR039856); TPR-like_helical_dom_sf. (IPR011990); TPR_EMC2.
    (IPR055217); TPR_rpt. (IPR019734); TPR_EMC2 (PF22890)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
citation_count: 29
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q15006
- **Protein Description:** RecName: Full=ER membrane protein complex subunit 2 {ECO:0000305}; AltName: Full=Tetratricopeptide repeat protein 35 {ECO:0000312|HGNC:HGNC:28963}; Short=TPR repeat protein 35 {ECO:0000312|HGNC:HGNC:28963};
- **Gene Information:** Name=EMC2 {ECO:0000312|HGNC:HGNC:28963}; Synonyms=KIAA0103 {ECO:0000312|EMBL:BAA03493.1}, TTC35 {ECO:0000312|HGNC:HGNC:28963};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the EMC2 family. .
- **Key Domains:** EMC2-like. (IPR039856); TPR-like_helical_dom_sf. (IPR011990); TPR_EMC2. (IPR055217); TPR_rpt. (IPR019734); TPR_EMC2 (PF22890)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "EMC2" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'EMC2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **EMC2** (gene ID: EMC2, UniProt: Q15006) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# EMC2 (ER Membrane Protein Complex Subunit 2): Comprehensive Functional Annotation

## Summary

**EMC2** (UniProt Q15006; synonyms TTC35, KIAA0103) is a 297-amino acid cytoplasmic scaffold protein that serves as the organizational hub of the **ER membrane protein complex (EMC)**, an essential and evolutionarily ancient multi-subunit insertase residing at the endoplasmic reticulum (ER) membrane. EMC2 contains three tetratricopeptide repeat (TPR) motifs arranged in an α-helical solenoid fold and is classified as a peripheral membrane protein — it does not span the lipid bilayer itself but instead anchors to the cytoplasmic face of the ER through extensive interactions with the transmembrane subunits EMC3, EMC5, and the soluble partners EMC8/EMC9. Its primary molecular function is to form the cytoplasmic vestibule that captures client transmembrane domains (TMDs) from the cytosol and channels them to the membrane-embedded insertase subunit EMC3 for energy-independent membrane insertion.

The EMC inserts two major classes of substrates: (1) **tail-anchored (TA) proteins** with moderately hydrophobic C-terminal TMDs that cannot be engaged by the canonical GET/TRC40 pathway, and (2) the **first TMD of multipass membrane proteins** (including G protein-coupled receptors) in the correct N-exo/C-cyto topology, enforcing the "positive-inside rule." Through these activities, EMC2 is indirectly required for cholesterol homeostasis (via biogenesis of squalene synthase and SOAT1), GPCR signaling, rhodopsin biosynthesis and photoreceptor survival, voltage-gated ion channel assembly, and ER–mitochondria lipid transfer. EMC2 is a common essential gene in human cells, is ubiquitously expressed across more than 210 cell types, and its complex is conserved across all major eukaryotic lineages since the last eukaryotic common ancestor (LECA). Functionally, the EMC is also coupled to ER-associated degradation (ERAD) quality control and serves as a host dependency factor exploited by flaviviruses for infection.

This report synthesizes evidence from cryo-electron microscopy structural studies, site-directed mutagenesis, reconstituted biochemical assays, CRISPR genetic screens, comparative genomics, and disease genetics to provide a comprehensive functional annotation of human EMC2.

---

## 1. Gene and Protein Identity

| Property | Value |
|----------|-------|
| **Gene** | EMC2 (Ensembl: ENSG00000104412) |
| **Chromosomal location** | 8q23.1 (chr8:108,443,601–108,551,893, GRCh38, forward strand) |
| **Synonyms** | TTC35, KIAA0103 |
| **UniProt** | Q15006 |
| **Organism** | Homo sapiens |
| **Protein family** | EMC2 family (IPR039856) |
| **Protein length** | 297 amino acids |
| **Key domains** | Three TPR motifs (aa 87–120, 155–188, 192–225); EMC2-like domain (IPR055217); TPR-like helical domain superfamily (IPR011990) |
| **Gene essentiality** | Common essential gene (DepMap CRISPR screens; Chronos score ~−0.8 to −1.0) |

The gene symbol "EMC2" unambiguously refers to this ER membrane protein complex subunit in humans. The protein was originally identified as KIAA0103 in early cDNA sequencing projects and later named TTC35 based on its TPR repeats, before being renamed EMC2 following the characterization of the EMC complex.

---

## 2. The ER Membrane Protein Complex (EMC)

### 2.1 Discovery and Conservation

The EMC was first identified in a systematic yeast genetic screen for factors involved in ER protein folding. Wideman (2015) subsequently demonstrated through comprehensive homology searching that the EMC is "truly an ancient and conserved protein complex, present in every major eukaryotic lineage. Very few organisms have completely lost the EMC, and most, even over 2 billion years of eukaryote evolution, have retained a majority of the complex members" ([PMID: 26512320](https://pubmed.ncbi.nlm.nih.gov/26512320/)). The EMC was present in the last eukaryote common ancestor (LECA), underscoring its fundamental importance to eukaryotic cell biology.

### 2.2 Complex Composition and Architecture

The human EMC consists of 9–10 subunits with distinct structural and functional roles:

| Subunit | Topology | Key Role |
|---------|----------|----------|
| **EMC1** | Type I TM, large lumenal β-propeller | Lumenal client folding; disease-associated |
| **EMC2** | Peripheral/cytoplasmic (TPR scaffold) | **Cytoplasmic substrate capture and complex organization** |
| **EMC3** | Multi-TM, YidC/Oxa1-like fold | Core insertase; forms lipid-exposed membrane groove |
| **EMC4** | TM | Membrane groove, lipid transfer |
| **EMC5/MMGT1** | TM | Hydrophilic vestibule component |
| **EMC6** | TM | Gating regulation |
| **EMC7** | Type I TM | Lumenal functions |
| **EMC8** | Cytoplasmic | Binds EMC2, cytoplasmic subcomplex |
| **EMC9** | Cytoplasmic | Binds EMC2, paralog of EMC8 |
| **EMC10** | TM | Regulatory, least conserved |

Multiple cryo-EM structures of the full human EMC have been determined, including in lipid nanodiscs at 3.4 Å resolution (PDB: 6WW7; O'Donnell et al., 2020; [PMID: 32459176](https://pubmed.ncbi.nlm.nih.gov/32459176/)) and in apo and VDAC-bound states (PDB: 8J0N, 8J0O; Li et al., 2024; [PMID: 38517390](https://pubmed.ncbi.nlm.nih.gov/38517390/)). These structures reveal a tripartite architecture: a large lumenal domain (dominated by EMC1), a transmembrane region containing a lipid-exposed hydrophilic groove (centered on EMC3, which shares structural homology with the YidC/Oxa1 superfamily of membrane protein insertases; [PMID: 35850079](https://pubmed.ncbi.nlm.nih.gov/35850079/); [PMID: 32910895](https://pubmed.ncbi.nlm.nih.gov/32910895/)), and a cytoplasmic domain forming a moderately hydrophobic vestibule for substrate capture (organized by EMC2).

---

## 3. EMC2: Structural Role and Molecular Function

### 3.1 Cytoplasmic Scaffold Architecture

EMC2 is entirely cytoplasmic, classified as a peripheral membrane protein associated with the ER membrane. Its three TPR repeats create a concave α-helical solenoid structure (~20 helices with two short β-strands), as revealed by the 2.2 Å crystal structure of the EMC2–EMC9 subcomplex (PDB: 6Y4L; [PMID: 32459176](https://pubmed.ncbi.nlm.nih.gov/32459176/)).

The TPR motifs function as protein–protein interaction domains. In the context of the EMC, EMC2 serves as the central organizing hub for the cytoplasmic face of the complex, with experimentally validated interactions:

- **EMC8 interaction:** 17 experimental validations
- **EMC9 interaction:** 14 experimental validations (paralog of EMC8, competes for the same binding site)
- **EMC3 interaction:** 12 experimental validations (bridges to the membrane-embedded insertase)
- **EMC5/MMGT1 interaction:** 13 experimental validations

### 3.2 Role in Substrate TMD Capture

The cryo-EM and crosslinking studies by O'Donnell et al. (2020) revealed that "EMC's cytosolic domain contains a large, moderately hydrophobic vestibule that can bind a substrate's transmembrane domain (TMD). The cytosolic vestibule leads into a lumenally-sealed, lipid-exposed intramembrane groove large enough to accommodate a single substrate TMD" ([PMID: 32459176](https://pubmed.ncbi.nlm.nih.gov/32459176/)). EMC2 forms a substantial portion of this cytoplasmic vestibule.

Pleiner et al. (2023) mapped the substrate path in detail using site-specific crosslinking, showing that client TA proteins are first captured by methionine-rich loops on the cytoplasmic face, then threaded through a hydrophilic vestibule into the membrane. "Positively charged residues at the entrance to the vestibule function as a selectivity filter that uses charge-repulsion to reject mitochondrial TA proteins. Similarly, this selectivity filter retains the positively charged soluble domains of multipass substrates in the cytosol, thereby ensuring they adopt the correct topology and enforcing the 'positive-inside' rule" ([PMID: 37199759](https://pubmed.ncbi.nlm.nih.gov/37199759/)).

### 3.3 Functional Residue Mapping by Mutagenesis

Site-directed mutagenesis studies (catalogued in UniProt Q15006, largely from O'Donnell et al. 2020) have mapped the functional surfaces of EMC2 at single-residue resolution:

| Functional Surface | Key Residues | Effect of Mutation |
|---|---|---|
| **EMC5 binding** | 28, 156, 160, 227 | Loss of EMC5 interaction |
| **EMC8 binding** | 171, 200, 227 | Decreased/abolished EMC8 interaction |
| **EMC3 binding** | 180, 259 | Decreased EMC3 interaction |
| **Substrate TMD capture** | 189, 190, 191 | Decreased TA protein TMD binding |
| **No effect on TMD binding** | 61, 95, 122, 193, 194 | No detectable change |

The substrate-binding residues (189–191) lie in the TPR3 region, and their proximity to the EMC3-contact residue (180) provides molecular evidence that EMC2 bridges substrate capture and membrane insertion at a defined structural junction. The EMC5 and EMC8 binding sites are distributed along the TPR solenoid, consistent with EMC2 serving as a multi-armed scaffold connecting cytoplasmic and membrane subunits.

{{figure:emc2_domain_map.png|caption=EMC2 functional domain map showing TPR repeats (blue), partner binding sites for EMC3/EMC5/EMC8, substrate TMD interaction residues (189-191), and post-translational modifications. Residue-level annotations are derived from UniProt Q15006 mutagenesis data and cryo-EM structural studies (O'Donnell et al. 2020).}}

### 3.4 Post-Translational Modifications

EMC2 undergoes N-terminal acetylation at Ala2 (after initiator methionine removal) and lysine acetylation at Lys255. Lys255 is located in the C-terminal helix (residues 247–274) near the EMC3-binding residue (259), suggesting potential regulation of the EMC2–EMC3 interface, though this has not been functionally tested. The best-characterized regulatory modification is **ubiquitination of unassembled EMC2**, which leads to proteasomal degradation and is prevented by WNK1 binding ([PMID: 33964204](https://pubmed.ncbi.nlm.nih.gov/33964204/)).

### 3.5 EMC2 Assembly and Quality Control by WNK1

A surprising finding from Pleiner et al. (2021) revealed that the kinase WNK1 (with no lysine kinase 1) moonlights as an essential assembly factor for the EMC. WNK1 "uses a conserved amphipathic helix to stabilize the soluble subunit, EMC2, by binding to the EMC2-8 interface. Shielding this hydrophobic surface prevents promiscuous interactions of unassembled EMC2 and directly competes for binding of E3 ubiquitin ligases, permitting assembly" ([PMID: 33964204](https://pubmed.ncbi.nlm.nih.gov/33964204/)). Without WNK1, free EMC2 is ubiquitinated and degraded by the proteasome. Depletion of WNK1 destabilizes both the EMC and its membrane protein clients. This quality control mechanism ensures that only properly assembled EMC complexes persist, highlighting EMC2's centrality — the entire complex depends on its successful incorporation.

---

## 4. Primary Functions of the EMC (Including EMC2)

### 4.1 Post-Translational Insertion of Tail-Anchored Proteins

The landmark study by Guna et al. (2018) established the EMC as a bona fide transmembrane domain insertase. They demonstrated that "known membrane insertion pathways fail to effectively engage tail-anchored membrane proteins with moderately hydrophobic transmembrane domains. These proteins are instead shielded in the cytosol by calmodulin. Dynamic release from calmodulin allowed sampling of the endoplasmic reticulum (ER), where the conserved ER membrane protein complex (EMC) was shown to be essential for efficient insertion in vitro and in cells" ([PMID: 29242231](https://pubmed.ncbi.nlm.nih.gov/29242231/)). Critically, purified EMC in synthetic liposomes catalyzed the insertion of its substrates, proving direct insertase activity.

The EMC operates in parallel with the **GET/TRC40 pathway** but handles a distinct substrate class: TA proteins whose TMDs are **moderately hydrophobic** — too weak for the GET pathway but requiring assistance for membrane insertion. Jung & Zimmermann (2023) used quantitative proteomics to systematically characterize the client spectra of these pathways, confirming that each handles a distinct subset of membrane proteins ([PMID: 37762469](https://pubmed.ncbi.nlm.nih.gov/37762469/)). Structural comparisons reveal that both EMC and GET insertases share a conserved hydrophilic groove mechanism, suggesting divergent evolution from a common ancestor ([PMID: 35850079](https://pubmed.ncbi.nlm.nih.gov/35850079/); [PMID: 32910895](https://pubmed.ncbi.nlm.nih.gov/32910895/)).

### 4.2 Cotranslational Insertion of Multipass Membrane Proteins

Beyond TA proteins, the EMC plays a critical role in the cotranslational biogenesis of multipass membrane proteins. It mediates the insertion of the first TMD of multipass proteins in the correct N-exo topology (N-terminus in the ER lumen), enforcing the "positive-inside rule" that governs membrane protein topology ([PMID: 37199759](https://pubmed.ncbi.nlm.nih.gov/37199759/)). Miller-Vedam et al. (2020) resolved cryo-EM structures of both yeast and human EMC that "reveal conserved intricate assemblies and human-specific features associated with pathologies. Structure-based functional studies distinguish between two separable EMC activities, as an insertase regulating tail-anchored protein levels and a broader role in polytopic membrane protein biogenesis" ([PMID: 33236988](https://pubmed.ncbi.nlm.nih.gov/33236988/)).

### 4.3 Cooperation with the Multipass Translocon

Page et al. (2024) demonstrated that the EMC physically and genetically interacts with the back of Sec61 (BOS) complex, a component of the multipass translocon. They proposed "a unifying model for coordination between the EMC, the multipass translocon, and Sec61 for the biogenesis of diverse membrane proteins in human cells" ([PMID: 38076791](https://pubmed.ncbi.nlm.nih.gov/38076791/)). This places EMC2 within a larger biogenesis network where the EMC inserts the first TMD of multipass proteins and then hands off partially inserted substrates to Sec61/BOS for completion.

### 4.4 Chaperone Function for Membrane Protein Complex Assembly

The most recent work by Stanton et al. (2026) demonstrated that the EMC acts as a chaperone beyond its insertase function, "facilitating the assembly of heterotrimeric voltage-gated calcium channels" at the ER membrane ([PMID: 41648177](https://pubmed.ncbi.nlm.nih.gov/41648177/)). This extends EMC function beyond simple insertion to include holding and protecting unassembled membrane protein subunits, facilitating their stoichiometric assembly.

Additionally, Li et al. (2024) resolved cryo-EM structures of human EMC in apo and VDAC-bound states, revealing "a specific interaction between VDAC proteins and the EMC at mitochondria-ER contact sites, which is conserved from yeast to humans. Moreover, [they] identified a gating plug located inside the EMC hydrophilic vestibule, the substrate-binding pocket for client insertion" ([PMID: 38517390](https://pubmed.ncbi.nlm.nih.gov/38517390/)). This gating plug may regulate the switch between the EMC's insertase and chaperone modes.

---

## 5. Subcellular Localization

EMC2 localizes to the **cytoplasmic face of the endoplasmic reticulum membrane** (GO:0072546, EMC complex; GO:0042406, extrinsic component of ER membrane). It is not itself a transmembrane protein but is tethered to the ER membrane through its extensive interactions with the transmembrane EMC subunits (EMC3, EMC5).

Within the cell, the EMC complex is found at:

- **ER membrane:** Primary site of function (protein insertion and chaperone activity)
- **ER–mitochondria contact sites (MAMs):** The EMC interacts with VDAC at these contact sites ([PMID: 38517390](https://pubmed.ncbi.nlm.nih.gov/38517390/)), and with SLC25A46 to facilitate phospholipid transfer between the ER and mitochondria ([PMID: 27390132](https://pubmed.ncbi.nlm.nih.gov/27390132/))

EMC2 is ubiquitously expressed across human tissues, detected in more than 210 cell types and tissues (Bgee database, ENSG00000104412), consistent with its fundamental role in ER membrane protein biogenesis.

---

## 6. Physiological Roles and Client Specificity

### 6.1 Cholesterol Homeostasis

Volkmar et al. (2019) demonstrated that "insertion of the weakly hydrophobic tail-anchor (TA) of SQS into the ER membrane by the EMC ensures sufficient flux through the sterol biosynthetic pathway while biogenesis of polytopic SOAT1 promoted by the EMC provides cells with the ability to store free cholesterol as inert cholesteryl esters" ([PMID: 30578317](https://pubmed.ncbi.nlm.nih.gov/30578317/)). EMC deficiency causes diminished cell viability under both limiting and excessive extracellular cholesterol, demonstrating that the EMC is a key biogenic determinant of cellular cholesterol tolerance.

### 6.2 Rhodopsin Biosynthesis and Photoreceptor Survival

EMC subunits are essential for rhodopsin (Rh1) stabilization. Satoh et al. (2015) showed that "dPob/EMC3, EMC1, and EMC8/9, Drosophila homologs of subunits of ER membrane protein complex (EMC), are essential for stabilization of immature Rh1 in an earlier step than that at which another Rh1-specific chaperone (NinaA) acts" ([PMID: 25715730](https://pubmed.ncbi.nlm.nih.gov/25715730/)). Xiong et al. (2020) confirmed this in mammals: "Conditional knockout of the Emc3 gene in mice led to mislocalization of rhodopsin protein and death of cone and rod photoreceptor cells" ([PMID: 31263175](https://pubmed.ncbi.nlm.nih.gov/31263175/)). Hiramatsu et al. (2019) further showed that the EMC specifically facilitates insertion of late-synthesized transmembrane helices of Rh1 ([PMID: 31553680](https://pubmed.ncbi.nlm.nih.gov/31553680/)).

### 6.3 GPCR Biogenesis

GPCRs, the largest family of human membrane receptors (~800 members), are key EMC clients. The EMC inserts the first TMD of GPCRs in the correct N-exo orientation, which is essential for subsequent folding of the remaining TMDs. Page et al. (2024) showed that characteristics of a GPCR's soluble domain determine its biogenesis pathway, with the EMC, multipass translocon, and Sec61 coordinating ([PMID: 38076791](https://pubmed.ncbi.nlm.nih.gov/38076791/)).

### 6.4 Viral Membrane Protein Biogenesis

The EMC, including EMC2/TTC35, was identified as a host dependency factor for flaviviruses. Barrows et al. (2019) showed that "TTC35 and TMEM111, which we previously demonstrated to be required for yellow fever virus (YFV) infection and others subsequently showed were also required by other flaviviruses. These proteins are components of the human endoplasmic reticulum membrane protein complex (EMC)" ([PMID: 31273220](https://pubmed.ncbi.nlm.nih.gov/31273220/)). Savidis et al. (2016) independently confirmed that "both flaviviruses require the EMC for their early stages of infection" ([PMID: 27342126](https://pubmed.ncbi.nlm.nih.gov/27342126/)). Bagchi et al. (2022) further showed that EMC4 specifically promotes DENV–endosomal membrane fusion by mediating ER-to-endosome transfer of phosphatidylserine ([PMID: 35834589](https://pubmed.ncbi.nlm.nih.gov/35834589/)).

### 6.5 Functional Connection to ER-Associated Degradation (ERAD)

STRING network analysis reveals high-confidence interactions between EMC2 and ERAD components DERL2 (Derlin-2, score = 0.904) and UBAC2 (score = 0.847). A chemogenomic screen by Raj et al. (2015) found that "the set of mutants conferring sensitivity to sr7575 was strikingly narrow, affecting components of the endoplasmic reticulum-associated protein degradation (ERAD) stress response and the ER membrane protein complex (EMC). ERAD-deficient mutants were hypersensitive to sr7575 in both *S. cerevisiae* and *A. fumigatus*, indicating a conserved mechanism of growth inhibition between yeast and filamentous fungi" ([PMID: 26666917](https://pubmed.ncbi.nlm.nih.gov/26666917/)). This functional coupling likely reflects the need for coordinated biogenesis (EMC) and quality control (ERAD) of membrane proteins at the ER.

---

## 7. Mechanistic Model

The following model summarizes the role of EMC2 within the EMC insertase complex:

```
                        CYTOSOL
                          │
     ┌────────────────────┼────────────────────┐
     │                    │                    │
     │   Calmodulin ──► release of TA protein │
     │                    │                    │
     │        ┌───────────▼───────────┐        │
     │        │    EMC2 VESTIBULE     │        │
     │        │  (TPR solenoid fold)  │        │
     │        │                       │        │
     │        │  EMC8/9 ◄──► EMC2    │        │
     │        │  (soluble)   │       │        │
     │        │              │ res   │        │
     │        │     WNK1 ──► │ 189-  │        │
     │        │  (assembly   │ 191   │        │
     │        │   factor)    │ (TMD  │        │
     │        │              │ bind) │        │
     │        │              ▼       │        │
     │        │         res 180/259  │        │
     │        │         (EMC3 contact)│        │
     │        └──────────┬───────────┘        │
     │                   │                    │
═════╪═══════════════════╪════════════════════╪═══
     │    ER MEMBRANE    │                    │
     │                   ▼                    │
     │        ┌──────────────────┐            │
     │        │  EMC3 INSERTASE  │            │
     │        │ (hydrophilic     │            │
     │        │  groove, lipid-  │◄── EMC1    │
     │        │  exposed)        │    EMC5    │
     │        │                  │    EMC4    │
     │        │  Selectivity     │    EMC6    │
     │        │  filter (+charge │    EMC7    │
     │        │  repulsion)      │    EMC10   │
     │        └────────┬─────────┘            │
     │                 │                      │
     │                 ▼                      │
     │        Inserted TMD in                 │
     │        correct topology                │
     │        (N-exo, positive-inside)        │
     │                                        │
     └────────────────────────────────────────┘
                     ER LUMEN

  Clients: TA proteins (SQS, VAMP7, etc.)
           Multipass proteins (GPCRs, rhodopsin, CaV channels)
  
  Coupled pathways:
  → GET/TRC40 (parallel: handles strongly hydrophobic TA TMDs)
  → BOS/Sec61 (sequential: handles downstream TMDs of multipass proteins)
  → ERAD (quality control: degrades misfolded EMC clients)
```

**Substrate selection logic:** The EMC vestibule (formed largely by EMC2) captures TMDs from the cytosol. A charge-based selectivity filter at the vestibule entrance uses electrostatic repulsion to reject mitochondrial TA proteins (which have net negative flanking charges) while accepting ER-destined substrates and enforcing the positive-inside topology rule for multipass proteins. After capture, the TMD is handed off through the EMC2–EMC3 interface into a lipid-exposed, lumenally-sealed intramembrane groove in EMC3 for lateral release into the ER membrane.

---

## 8. Pathway Context

EMC2 is notably absent from canonical signaling pathway databases (no KEGG or Reactome pathway annotations). This reflects its role as **core biogenesis machinery** for ER membrane proteins — a "housekeeping" complex that impacts many downstream pathways indirectly:

| Pathway/Process | EMC Role | Key Clients |
|---|---|---|
| **Membrane protein insertion** | Primary insertase for moderate-hydrophobicity TMDs | TA proteins, first TMD of multipass proteins |
| **GET/TRC40 pathway** | Parallel, complementary pathway (handles strong TMDs) | TA proteins with high hydrophobicity |
| **Sec61/BOS translocon** | Sequential cooperator for multipass protein biogenesis | Downstream TMDs of GPCRs |
| **Cholesterol biosynthesis** | Biogenesis of pathway enzymes | SQS/FDFT1 (TA protein), SOAT1 (polytopic) |
| **Phototransduction** | Rhodopsin biogenesis | Rhodopsin/Rh1 |
| **Ion channel assembly** | Chaperone for complex formation | Voltage-gated Ca²⁺ channels |
| **ERAD** | Functional coupling; quality control of EMC clients | Misfolded membrane proteins |
| **ER–mitochondria communication** | Lipid transfer at contact sites | VDAC, SLC25A46 |

---

## 9. Disease Associations

### 9.1 EMC Subunit Mutations in Human Disease

While no Mendelian disease has been directly attributed to EMC2 mutations (likely reflecting embryonic lethality of homozygous loss, consistent with its essential gene classification), mutations in related EMC subunits cause severe disease:

- **EMC1 mutations** cause neurodevelopmental syndrome with global developmental delay, severe hypotonia, cerebellar atrophy, and visual impairment ([PMID: 37187958](https://pubmed.ncbi.nlm.nih.gov/37187958/); [PMID: 38784058](https://pubmed.ncbi.nlm.nih.gov/38784058/))
- **EMC3 mutations** have been identified as a candidate gene for inherited retinal dystrophies ([PMID: 37809982](https://pubmed.ncbi.nlm.nih.gov/37809982/))
- **EMC loss** causes photoreceptor degeneration in both flies and mice ([PMID: 25715730](https://pubmed.ncbi.nlm.nih.gov/25715730/); [PMID: 31263175](https://pubmed.ncbi.nlm.nih.gov/31263175/))

### 9.2 Cancer Prognostic Associations

EMC2 has been identified as a prognostic indicator in several cancer types:

- In **acute myeloid leukemia**, EMC2 was identified among significant prognostic genes, with "high transcript abundance correlating with poor outcomes" ([PMID: 39311489](https://pubmed.ncbi.nlm.nih.gov/39311489/))
- In **breast cancer**, EMC2 appears in ferroptosis-related prognostic gene signatures ([PMID: 34956895](https://pubmed.ncbi.nlm.nih.gov/34956895/); [PMID: 34059009](https://pubmed.ncbi.nlm.nih.gov/34059009/))
- **TTC35 (EMC2)** expression is significantly altered with pancreatic tumor grade ([PMID: 34711879](https://pubmed.ncbi.nlm.nih.gov/34711879/))

The mechanistic basis for these associations likely reflects EMC2's essential role in membrane protein biogenesis (including iron-handling proteins like SQS/FDFT1) rather than a direct role in ferroptosis signaling, though this remains to be directly demonstrated.

### 9.3 Viral Infection

As a flavivirus host dependency factor, the EMC (including EMC2) represents a potential target for antiviral intervention against dengue, Zika, and yellow fever viruses ([PMID: 31273220](https://pubmed.ncbi.nlm.nih.gov/31273220/); [PMID: 27342126](https://pubmed.ncbi.nlm.nih.gov/27342126/)).

---

## 10. Key Structural Evidence

| PDB ID | Method | Resolution | Contents | Reference |
|--------|--------|-----------|----------|-----------|
| 6Y4L | X-ray | 2.2 Å | EMC2–EMC9 subcomplex | O'Donnell et al. 2020 |
| 6WW7 | Cryo-EM | 3.4 Å | Full human EMC in nanodisc | O'Donnell et al. 2020 |
| 7ADO | Cryo-EM | 3.39 Å | Human EMC | Miller-Vedam et al. 2020 |
| 8J0N | Cryo-EM | 3.47 Å | Human EMC apo state | Li et al. 2024 |
| 8J0O | Cryo-EM | 3.32 Å | Human EMC + VDAC | Li et al. 2024 |

---

## 11. Evidence Base

### Structural Studies

| Study | Key Contribution | PMID |
|---|---|---|
| O'Donnell et al. 2020 | Architecture of human EMC; cytoplasmic vestibule; EMC2–EMC9 crystal structure | [32459176](https://pubmed.ncbi.nlm.nih.gov/32459176/) |
| Miller-Vedam et al. 2020 | Yeast and human EMC structures; dual insertase/chaperone activities | [33236988](https://pubmed.ncbi.nlm.nih.gov/33236988/) |
| Li et al. 2024 | Human EMC apo and VDAC-bound; gating plug mechanism | [38517390](https://pubmed.ncbi.nlm.nih.gov/38517390/) |
| McDowell et al. 2020 | GET insertase structure; structural homology with EMC | [32910895](https://pubmed.ncbi.nlm.nih.gov/32910895/) |

### Functional/Biochemical Studies

| Study | Key Finding | PMID |
|---|---|---|
| Guna et al. 2018 | EMC is a TA protein insertase for moderate-hydrophobicity TMDs | [29242231](https://pubmed.ncbi.nlm.nih.gov/29242231/) |
| Pleiner et al. 2023 | Charge-based selectivity filter; positive-inside rule enforcement | [37199759](https://pubmed.ncbi.nlm.nih.gov/37199759/) |
| Pleiner et al. 2021 | WNK1 as EMC2 assembly factor | [33964204](https://pubmed.ncbi.nlm.nih.gov/33964204/) |
| Page et al. 2024 | EMC•BOS holocomplex for GPCR biogenesis | [38076791](https://pubmed.ncbi.nlm.nih.gov/38076791/) |
| Volkmar et al. 2019 | EMC required for cholesterol homeostasis via SQS and SOAT1 | [30578317](https://pubmed.ncbi.nlm.nih.gov/30578317/) |
| Stanton et al. 2026 | EMC chaperone activity for Ca²⁺ channel assembly | [41648177](https://pubmed.ncbi.nlm.nih.gov/41648177/) |
| Jung & Zimmermann 2023 | Systematic characterization of EMC client spectrum | [37762469](https://pubmed.ncbi.nlm.nih.gov/37762469/) |

### Physiological/Disease Studies

| Study | Key Finding | PMID |
|---|---|---|
| Satoh et al. 2015 | EMC essential for rhodopsin biosynthesis in *Drosophila* | [25715730](https://pubmed.ncbi.nlm.nih.gov/25715730/) |
| Xiong et al. 2020 | Emc3 knockout causes photoreceptor death in mice | [31263175](https://pubmed.ncbi.nlm.nih.gov/31263175/) |
| Hiramatsu et al. 2019 | EMC facilitates late TMD insertions of Rh1 | [31553680](https://pubmed.ncbi.nlm.nih.gov/31553680/) |
| Barrows et al. 2019 | EMC2/TTC35 is a flavivirus host dependency factor | [31273220](https://pubmed.ncbi.nlm.nih.gov/31273220/) |
| Savidis et al. 2016 | EMC required for ZIKV/DENV infection | [27342126](https://pubmed.ncbi.nlm.nih.gov/27342126/) |
| Wideman 2015 | EMC conserved since LECA | [26512320](https://pubmed.ncbi.nlm.nih.gov/26512320/) |
| Wang et al. 2023 | EMC1 mutations cause neurodevelopmental disease | [37187958](https://pubmed.ncbi.nlm.nih.gov/37187958/) |
| Raj et al. 2015 | EMC and ERAD functional coupling in chemogenomic screen | [26666917](https://pubmed.ncbi.nlm.nih.gov/26666917/) |
| Janer et al. 2016 | SLC25A46–EMC interaction in mitochondrial lipid homeostasis | [27390132](https://pubmed.ncbi.nlm.nih.gov/27390132/) |

---

## 12. Limitations and Knowledge Gaps

1. **No direct substrate-bound structure:** No structure of EMC2 bound to a client TMD has been resolved, leaving the precise substrate capture geometry partially inferred from crosslinking and mutagenesis data.

2. **Regulation of EMC2 function is poorly understood:** The acetylation at Lys255 near the EMC3-binding interface hints at post-translational regulation, but the responsible enzyme(s) and functional consequences have not been characterized.

3. **Client specificity determinants incompletely defined:** While it is known that EMC handles moderate-hydrophobicity TMDs and the GET pathway handles strongly hydrophobic ones, the precise biophysical thresholds and how EMC2's vestibule discriminates substrates remain incompletely defined.

4. **Disease associations are largely correlative:** EMC2's appearances in ferroptosis/cancer prognostic gene signatures likely reflect its essential role in membrane protein biogenesis rather than a direct role in ferroptosis. Mechanistic studies are needed.

5. **Gating plug dynamics unresolved:** The gating plug inside the EMC hydrophilic vestibule may regulate switching between insertase and chaperone modes, but its regulation and dynamics during substrate engagement have not been captured.

6. **No EMC2-specific Mendelian disease:** This likely reflects embryonic lethality of homozygous loss, but hypomorphic alleles or mosaic states have not been systematically searched for.

---

## 13. Proposed Follow-up Experiments

1. **Characterize Lys255 acetylation:** Use acetylation-mimicking (K255Q) and acetylation-dead (K255R) mutants to test whether this modification regulates EMC2–EMC3 binding affinity and insertase activity in reconstituted assays.

2. **Resolve substrate-bound EMC structure:** Use cryo-EM with stalled substrates (e.g., dominant-negative TA proteins) to capture the EMC with a client TMD in the vestibule.

3. **Define EMC2-specific client spectrum:** Perform TMT-based quantitative proteomics comparing EMC2-depleted versus EMC3-depleted cells to determine whether EMC2 has functions independent of the insertase.

4. **Screen for EMC2 disease variants:** Mine ClinVar and gnomAD for rare EMC2 missense variants at functionally critical residues (189–191, 180, 259) and test their effects on EMC assembly and client protein levels.

5. **Test EMC2 in ferroptosis directly:** Determine whether EMC2 knockdown sensitizes cells to ferroptosis inducers and whether this is mediated through loss of specific client biogenesis.

6. **Explore antiviral potential:** Determine whether partial EMC inhibition can suppress flavivirus replication without lethal cytotoxicity, leveraging residual insertion capacity from the parallel GET pathway.

---

## References

1. Guna A, Volkmar N, Christianson JC, Hegde RS. *The ER membrane protein complex is a transmembrane domain insertase.* Science. 2018;359(6374):470–473. [PMID: 29242231](https://pubmed.ncbi.nlm.nih.gov/29242231/).
2. O'Donnell JP, Phillips BP, Yagita Y, et al. *The architecture of EMC reveals a path for membrane protein insertion.* eLife. 2020;9:e57887. [PMID: 32459176](https://pubmed.ncbi.nlm.nih.gov/32459176/).
3. Miller-Vedam LE, Brauning B, Popova KD, et al. *Structural and mechanistic basis of the EMC-dependent biogenesis of distinct transmembrane clients.* eLife. 2020;9:e62611. [PMID: 33236988](https://pubmed.ncbi.nlm.nih.gov/33236988/).
4. Pleiner T, Hazu M, Tomaleri GP, et al. *WNK1 is an assembly factor for the human ER membrane protein complex.* Mol Cell. 2021;81(13):2730–2742. [PMID: 33964204](https://pubmed.ncbi.nlm.nih.gov/33964204/).
5. Pleiner T, Hazu M, Pinton Tomaleri G, et al. *A selectivity filter in the ER membrane protein complex limits protein misinsertion at the ER.* J Cell Biol. 2023;222(6):e202212007. [PMID: 37199759](https://pubmed.ncbi.nlm.nih.gov/37199759/).
6. Volkmar N, Thezenas ML, Louie SM, et al. *The ER membrane protein complex promotes biogenesis of sterol-related enzymes maintaining cholesterol homeostasis.* J Cell Sci. 2019;132(2):jcs223453. [PMID: 30578317](https://pubmed.ncbi.nlm.nih.gov/30578317/).
7. Li Y, Zhang Y, Xu L, et al. *Structural insights into human EMC and its interaction with VDAC.* EMBO J. 2024;43:1377–1398. [PMID: 38517390](https://pubmed.ncbi.nlm.nih.gov/38517390/).
8. Wideman JG. *The ubiquitous and ancient ER membrane protein complex (EMC): tether or not?* F1000Res. 2015;4:624. [PMID: 26512320](https://pubmed.ncbi.nlm.nih.gov/26512320/).
9. Barrows NJ, Anglero-Rodriguez Y, Kim B, et al. *Dual roles for the ER membrane protein complex in flavivirus infection.* J Virol. 2019;93(22):e01010-19. [PMID: 31273220](https://pubmed.ncbi.nlm.nih.gov/31273220/).
10. Savidis G, McDougall WM, Meraner P, et al. *Identification of Zika virus and dengue virus dependency factors using functional genomics.* Cell Rep. 2016;16(1):232–246. [PMID: 27342126](https://pubmed.ncbi.nlm.nih.gov/27342126/).
11. Satoh T, Ohba A, Liu Z, Inagaki T, Bhatt VS. *dPob/EMC is essential for biosynthesis of rhodopsin and other multi-pass membrane proteins in Drosophila photoreceptors.* eLife. 2015;4:e06306. [PMID: 25715730](https://pubmed.ncbi.nlm.nih.gov/25715730/).
12. Xiong L, Zhang L, Yang Y, et al. *ER complex proteins are required for rhodopsin biosynthesis and photoreceptor survival in Drosophila and mice.* J Cell Biol. 2020;219(3):e201909094. [PMID: 31263175](https://pubmed.ncbi.nlm.nih.gov/31263175/).
13. Sinning I, McDowell MA. *Cryo-EM insights into tail-anchored membrane protein biogenesis in eukaryotes.* Curr Opin Struct Biol. 2022;75:102428. [PMID: 35850079](https://pubmed.ncbi.nlm.nih.gov/35850079/).
14. Page BM, Nguyen HT, Pleiner T, et al. *Role of a holo-insertase complex in the biogenesis of biophysically diverse ER membrane proteins.* Science. 2024;383(6684):eadj7880. [PMID: 38076791](https://pubmed.ncbi.nlm.nih.gov/38076791/).
15. Stanton AC, Singal N, Biswal M, et al. *The ER membrane protein complex acts as a chaperone to promote the biogenesis of multi-bundle membrane proteins.* 2026. [PMID: 41648177](https://pubmed.ncbi.nlm.nih.gov/41648177/).
16. Janer A, Prudent J, Paupe V, et al. *SLC25A46 is required for mitochondrial lipid homeostasis and cristae maintenance.* EMBO Mol Med. 2016;8(9):1019–1038. [PMID: 27390132](https://pubmed.ncbi.nlm.nih.gov/27390132/).
17. Jung S, Bhatt P, Zimmermann R. *Quantitative mass spectrometry characterizes client spectra of components for targeting and insertion into the ER membrane.* Int J Mol Sci. 2023;24(19):14869. [PMID: 37762469](https://pubmed.ncbi.nlm.nih.gov/37762469/).
18. Wang L, Wang Y, Gao S, Xie F. *Novel compound heterozygous variants in EMC1.* Mol Genet Genomic Med. 2023;11(7):e2177. [PMID: 37187958](https://pubmed.ncbi.nlm.nih.gov/37187958/).
19. Alzayed S, Alzuabi M, Alqusaimi N, et al. *Tribal founder EMC1 variant.* Clin Genet. 2024;106(2):194–199. [PMID: 38784058](https://pubmed.ncbi.nlm.nih.gov/38784058/).
20. Liu X, Yang J, Han R, Zhou H, Qu S, Shi Y. *ncRNA-mediated overexpression of ferroptosis-related gene EMC2.* Immun Inflamm Dis. 2021;9(4):1510–1527. [PMID: 34956895](https://pubmed.ncbi.nlm.nih.gov/34956895/).
21. Shangguan Y, Huang L, Chen Y, et al. *Prognostic assessment value of immune escape-related genes in AML.* Sci Rep. 2025;15(1):33094. [PMID: 39311489](https://pubmed.ncbi.nlm.nih.gov/39311489/).
22. Bagchi P, Speckhart K, Kennedy A, Tai AW, Bhatt VS. *A specific EMC subunit supports dengue virus infection.* PLoS Pathog. 2022;18(7):e1010717. [PMID: 35834589](https://pubmed.ncbi.nlm.nih.gov/35834589/).
23. Raj S, Krishnan K, Askew DS, et al. *The toxicity of a novel antifungal compound is modulated by ERAD components.* mBio. 2015;6(6):e01861-15. [PMID: 26666917](https://pubmed.ncbi.nlm.nih.gov/26666917/).
24. Hiramatsu N, Tago T, Satoh T, Satoh AK. *ER membrane protein complex is required for the insertions of late-synthesized transmembrane helices of Rh1 in Drosophila photoreceptors.* Mol Biol Cell. 2019;30(20):2577–2589. [PMID: 31553680](https://pubmed.ncbi.nlm.nih.gov/31553680/).
25. McDowell MA, Heimes M, Fiorentino F, et al. *Structural basis of tail-anchored membrane protein biogenesis by the GET insertase complex.* Mol Cell. 2020;80(1):72–86. [PMID: 32910895](https://pubmed.ncbi.nlm.nih.gov/32910895/).
26. Park JM, Mau CZ, Chen YC, et al. *A case-control study in Taiwanese cohort and meta-analysis of serum ferritin in pancreatic cancer.* Sci Rep. 2021;11(1):21242. [PMID: 34711879](https://pubmed.ncbi.nlm.nih.gov/34711879/).
27. Rapaport D, Herrmann JM. *Chasing the right tail: How the ER membrane complex recognizes its substrates.* J Cell Biol. 2023;222(7):e202306065. [PMID: 37436711](https://pubmed.ncbi.nlm.nih.gov/37436711/).


## Citations

1. PMID:26512320
2. PMID:32459176
3. PMID:38517390
4. PMID:35850079
5. PMID:32910895
6. PMID:37199759
7. PMID:33964204
8. PMID:29242231
9. PMID:37762469
10. PMID:33236988
11. PMID:38076791
12. PMID:41648177
13. PMID:27390132
14. PMID:30578317
15. PMID:25715730
16. PMID:31263175
17. PMID:31553680
18. PMID:31273220
19. PMID:27342126
20. PMID:35834589
21. PMID:26666917
22. PMID:37187958
23. PMID:38784058
24. PMID:37809982
25. PMID:39311489
26. PMID:34956895
27. PMID:34059009
28. PMID:34711879
29. PMID:37436711