---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-12T23:44:59.540605'
end_time: '2026-05-12T23:54:18.328251'
duration_seconds: 558.79
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 27
---

## Question

Concise GO annotation research for human BRAF / UniProt P15056. Focus only on GO-relevant evidence: core molecular function as a RAF-family serine/threonine protein kinase and MAP kinase kinase kinase in the RAS-RAF-MEK-ERK cascade; ATP binding, kinase activation mechanisms, RAS-GTP recruitment, dimerization, phosphorylation/regulatory sites, and direct MEK1/MEK2 substrate phosphorylation. Cover core biological processes such as MAPK cascade, ERK1/ERK2 cascade, Ras protein signal transduction, and regulation of cell proliferation/differentiation only where directly supported. Evaluate cellular localization evidence including cytosol, plasma membrane recruitment, nucleus if any, endomembrane, mitochondrion, and protein complexes. Distinguish wild-type BRAF core function from oncogenic BRAF mutants (especially V600E), cancer phenotypes, apoptosis, development, vascular/angiogenesis phenotypes, transcription, immune/metabolic downstream outcomes, and overexpression/pathway-membership inferences. Evaluate generic protein binding versus more informative MF terms. Include PMID/DOI citations and keep under 1500 words.

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

Concise GO annotation research for human BRAF / UniProt P15056. Focus only on GO-relevant evidence: core molecular function as a RAF-family serine/threonine protein kinase and MAP kinase kinase kinase in the RAS-RAF-MEK-ERK cascade; ATP binding, kinase activation mechanisms, RAS-GTP recruitment, dimerization, phosphorylation/regulatory sites, and direct MEK1/MEK2 substrate phosphorylation. Cover core biological processes such as MAPK cascade, ERK1/ERK2 cascade, Ras protein signal transduction, and regulation of cell proliferation/differentiation only where directly supported. Evaluate cellular localization evidence including cytosol, plasma membrane recruitment, nucleus if any, endomembrane, mitochondrion, and protein complexes. Distinguish wild-type BRAF core function from oncogenic BRAF mutants (especially V600E), cancer phenotypes, apoptosis, development, vascular/angiogenesis phenotypes, transcription, immune/metabolic downstream outcomes, and overexpression/pathway-membership inferences. Evaluate generic protein binding versus more informative MF terms. Include PMID/DOI citations and keep under 1500 words.

## GO-focused annotation research report: Human **BRAF** (UniProt **P15056**)

### Executive summary (GO-relevant)
BRAF is a RAF-family **serine/threonine protein kinase** that functions as the MAP3K tier in the canonical **RAS–RAF–MEK1/2–ERK1/2** cascade. GO-relevant evidence supports: **ATP binding and kinase catalysis**, **RAS-GTP-dependent recruitment to the plasma membrane via the RAS-binding domain (RBD) and cysteine-rich domain (CRD)**, release of **14-3-3-mediated autoinhibition** through regulatory phosphosites **pS365/pS729**, **kinase-domain dimerization** as a key activation step (for wild-type), and **direct phosphorylation/activation of MEK1/MEK2** (including MEK1 S218/S222). Evidence in this corpus supports **cytosolic autoinhibited complexes** and **plasma-membrane-associated active dimers**, but does **not** provide direct support for nuclear, Golgi/endomembrane, or mitochondrial localization for BRAF. (martinvega2023navigatingtheerk12 pages 2-4, bahar2023targetingtherasrafmapk pages 5-6, liu2024reconstitutionandcharacterization pages 1-2, liu2024reconstitutionandcharacterization pages 7-9)

| Annotation theme | Suggested GO term(s) | Key mechanistic evidence | Best supporting citations |
|---|---|---|---|
| ATP binding / kinase motifs | ATP binding; protein serine/threonine kinase activity | BRAF CR3 contains canonical kinase motifs; K578 contacts ATP γ-phosphate, and DFG/activation-segment conformations regulate active vs inactive states; ATP pocket remains accessible in autoinhibited structures. | (imani2024theevolutionof pages 6-7, fiesco2022structuralinsightsinto pages 4-5) |
| Core catalytic activity | protein serine/threonine kinase activity | BRAF is a RAF-family Ser/Thr kinase with catalytic CR3; active BRAF phosphorylates downstream MAP2Ks rather than generic substrates. | (bonsor2024rasandshoc2 pages 1-3, bahar2023targetingtherasrafmapk pages 5-6) |
| MAP3K role | MAP kinase kinase kinase activity | RAF is the MAP3K tier immediately downstream of RAS; BRAF is the direct upstream kinase for MEK1/MEK2 in the ERK pathway. | (martinvega2023navigatingtheerk12 pages 2-4, bahar2023targetingtherasrafmapk pages 5-6) |
| RAS-GTP recruitment to membrane | Ras GTPase binding; plasma membrane recruitment during Ras protein signal transduction | Exposed RBD basic residues bind activated RAS; CRD contributes membrane/phospholipid engagement, promoting recruitment from cytosol to plasma membrane. | (fiesco2022structuralinsightsinto pages 1-2, fiesco2022structuralinsightsinto pages 5-7, bonsor2024rasandshoc2 pages 4-6) |
| 14-3-3 binding via regulatory phosphosites | 14-3-3 protein binding | 14-3-3 dimer binds BRAF pS365 and pS729, stabilizing autoinhibition and controlling transition to active states. | (bonsor2024rasandshoc2 pages 1-3, liu2024reconstitutionandcharacterization pages 1-2, fiesco2022structuralinsightsinto pages 4-5) |
| Dimerization and activation | protein homodimerization activity; protein heterodimerization activity; activation of protein kinase activity | RAS engagement and loss of CR2-site restraint promote exposure of the dimer interface; 14-3-3 can bridge C-terminal pS729 sites across protomers to stabilize active dimers. | (fiesco2022structuralinsightsinto pages 1-2, fiesco2022structuralinsightsinto pages 2-4, bonsor2024rasandshoc2 pages 1-3) |
| Direct MEK1/MEK2 phosphorylation | MAP kinase kinase activity; protein serine/threonine kinase activity | Active BRAF directly phosphorylates MEK1/2; retrieved sources explicitly note MEK1 Ser218/Ser222 phosphorylation downstream of RAF/BRAF. | (imani2024theevolutionof pages 6-7, patel2023investigatingtherole pages 42-45, liu2024reconstitutionandcharacterization pages 9-10) |
| MAPK / ERK cascade | MAPK cascade; ERK1 and ERK2 cascade | BRAF functions in the RAS-RAF-MEK-ERK module as the MAP3K tier that activates MEK, which then activates ERK1/2. | (martinvega2023navigatingtheerk12 pages 2-4, bahar2023targetingtherasrafmapk pages 5-6) |
| Ras protein signal transduction | Ras protein signal transduction | BRAF is a direct RAS effector; GTP-bound RAS engages the BRAF RBD and initiates the conformational and localization changes needed for signaling. | (bonsor2024rasandshoc2 pages 1-3, fiesco2022structuralinsightsinto pages 1-2, fiesco2022structuralinsightsinto pages 5-7) |
| Cytosol autoinhibited state | cytosol; protein-containing complex | Wild-type BRAF resides as a cytosolic, monomeric autoinhibited complex with 14-3-3, with CRD and dimer interface occluded. | (liu2024reconstitutionandcharacterization pages 1-2, bonsor2024rasandshoc2 pages 1-3, mozzarelli2024functionalandstructural pages 6-7) |
| Plasma membrane active state | plasma membrane; plasma membrane protein-containing complex | Activated RAS recruits BRAF to membrane; membrane engagement plus dimerization generates the active signaling form. | (liu2024reconstitutionandcharacterization pages 1-2, bonsor2024rasandshoc2 pages 6-8, liu2024reconstitutionandcharacterization pages 7-9) |
| Complex with MEK and 14-3-3 | protein-containing complex | Cryo-EM/reconstitution studies identify autoinhibited BRAF-MEK-14-3-3 assemblies and related BRAF:14-3-3 complexes central to regulation. | (bonsor2024rasandshoc2 pages 1-3, fiesco2022structuralinsightsinto pages 1-2) |
| Other localization claims | no direct support for nucleus; no direct support for Golgi/endomembrane; no direct support for mitochondrion | In the retrieved GO-relevant sources, direct evidence supports cytosol, plasma membrane recruitment, and signaling complexes, but not nuclear, Golgi/endomembrane, or mitochondrial localization for BRAF. | (liu2024reconstitutionandcharacterization pages 2-4, mozzarelli2024functionalandstructural pages 6-7, liu2024reconstitutionandcharacterization pages 7-9) |


*Table: This table maps core GO-relevant annotation themes for human BRAF to suggested term labels, concise mechanistic evidence, and the strongest supporting context IDs. It is useful as a compact evidence matrix for curating BRAF molecular function, biological process, and cellular component annotations.*

---

### 1) Key concepts and definitions (current understanding)

#### Core molecular function (MF): RAF-family Ser/Thr kinase; MAP3K in ERK cascade
BRAF is a RAF-family kinase whose primary role in the ERK pathway is to act as a **MAP kinase kinase kinase (MAP3K)** that phosphorylates and activates **MEK1/MEK2**. This places BRAF immediately downstream of RAS and upstream of ERK1/2 signaling. (martinvega2023navigatingtheerk12 pages 2-4, bahar2023targetingtherasrafmapk pages 5-6)

**ATP binding/kinase motifs.** Structural descriptions identify canonical kinase features in BRAF, including residues involved in ATP coordination (e.g., K578 contacting ATP’s γ-phosphate) and activation-segment/DFG conformational control of active vs inactive states; cryo-EM structures indicate the ATP-binding pocket can remain accessible even in an autoinhibited monomer. (imani2024theevolutionof pages 6-7, fiesco2022structuralinsightsinto pages 4-5)

#### Informative binding MF terms vs generic “protein binding”
Generic “protein binding” is weakly informative for GO; the evidence supports specific binding functions that are mechanistically decisive:
* **Ras GTPase binding** via the BRAF **RBD** with exposed basic residues positioned to engage RAS switch regions. (fiesco2022structuralinsightsinto pages 5-7)
* **14-3-3 protein binding** via two phosphoserine sites flanking/near the kinase domain (**S365 and S729**), central to autoinhibition and activation. (bonsor2024rasandshoc2 pages 1-3, fiesco2022structuralinsightsinto pages 4-5)
* **Dimerization-associated protein binding** (homo-/heterodimers) as an activation mechanism for wild-type RAF proteins. (bahar2023targetingtherasrafmapk pages 5-6, fiesco2022structuralinsightsinto pages 2-4)

---

### 2) Recent developments and latest research (prioritizing 2023–2024)

#### Plasma-membrane recruitment and membrane context (2024 nanodisc reconstitution)
A 2024 mechanistic study reconstituted full-length BRAF with **14-3-3** and **membrane-tethered KRAS4B** on lipid nanodiscs and showed **GTP-dependent assembly**, directly linking **RAS-GTP + membrane** to formation of an active BRAF signaling complex. (Liu et al., *Protein Science*, May 2024, DOI:10.1002/pro.5016, URL https://doi.org/10.1002/pro.5016) (liu2024reconstitutionandcharacterization pages 1-2, liu2024reconstitutionandcharacterization pages 2-4)

Key GO-relevant findings include:
* BRAF exists as an **autoinhibited monomeric cytosolic complex** and an **active dimeric complex** with distinct SEC-resolved species (supporting CC: cytosol vs membrane-associated signaling states). (liu2024reconstitutionandcharacterization pages 2-4, liu2024reconstitutionandcharacterization pages 1-2)
* **Membrane lipid composition (e.g., anionic lipids)** and **RAS surface density** modulate BRAF binding kinetics/affinity, supporting a mechanistic basis for “plasma membrane recruitment” annotations rather than generic “membrane association.” (liu2024reconstitutionandcharacterization pages 7-9)
* The reconstituted BRAF complex is used in **MEK phosphorylation assays** in a membrane context, reinforcing BRAF’s MAP3K role. (liu2024reconstitutionandcharacterization pages 9-10)

#### Structural mechanism for RAS-mediated release of autoinhibition (2022 cryo-EM; still central in 2023–2024 syntheses)
High-resolution cryo-EM structures of autoinhibited BRAF complexes (with 14-3-3 and ±MEK) resolve the BRAF **RBD** and show that, despite autoinhibition, **key basic RBD residues are exposed and required for KRAS binding** (supported by binding assays and mutational disruption). (Martinez Fiesco et al., *Nature Communications*, Jan 2022, DOI:10.1038/s41467-022-28084-3, URL https://doi.org/10.1038/s41467-022-28084-3) (fiesco2022structuralinsightsinto pages 5-7)

The same study links RAS binding to activation-relevant conformational steps:
* Autoinhibition is stabilized by a **14-3-3 dimer** binding **pS365 and pS729**, occluding the CRD membrane-binding region and kinase dimer interface. (fiesco2022structuralinsightsinto pages 1-2, fiesco2022structuralinsightsinto pages 4-5)
* Superposition/modeling suggests that full RAS:RBD engagement would sterically/electrostatically perturb the adjacent 14-3-3 protomer, promoting **release from pS365** and enabling the CRD to engage membrane and support subsequent **kinase-domain dimerization**. (fiesco2022structuralinsightsinto pages 8-9, fiesco2022structuralinsightsinto pages 2-4)

#### Expert synthesis (2023–2024)
Recent authoritative reviews emphasize a conserved activation logic: **cytosolic autoinhibited monomer → RAS-GTP membrane recruitment → relief of 14-3-3/CR2-site inhibition (often via SHOC2–MRAS–PP1C) → active RAF dimer stabilized by 14-3-3 at C-terminal sites**. (Bonsor & Simanshu, *Annu Rev Cancer Biol*, Jun 2024, DOI:10.1146/annurev-cancerbio-062822-030450, URL https://doi.org/10.1146/annurev-cancerbio-062822-030450) (bonsor2024rasandshoc2 pages 6-8, bonsor2024rasandshoc2 pages 1-3)

A 2024 Molecular Cell review of RAS effector proteins similarly highlights **RAF dimerization at the plasma membrane** as culminating in full activation, placing BRAF among the best structurally characterized RAS effectors. (Mozzarelli et al., *Molecular Cell*, Aug 2024, DOI:10.1016/j.molcel.2024.06.027, URL https://doi.org/10.1016/j.molcel.2024.06.027) (mozzarelli2024functionalandstructural pages 6-7)

---

### 3) GO-relevant biological processes (BP) supported by direct evidence

* **MAPK cascade / ERK1/2 cascade.** RAF kinases are the MAP3K tier directly downstream of RAS; BRAF activates MEK1/2, which activates ERK1/2. (Martín-Vega & Cobb, *Biomolecules*, Oct 2023, DOI:10.3390/biom13101555, URL https://doi.org/10.3390/biom13101555) (martinvega2023navigatingtheerk12 pages 2-4)
* **Ras protein signal transduction.** BRAF is a direct RAS effector: its RBD binds activated RAS and drives membrane recruitment and activation. (fiesco2022structuralinsightsinto pages 1-2, fiesco2022structuralinsightsinto pages 5-7)

**Restriction on proliferation/differentiation claims.** While ERK signaling is widely linked to proliferation/differentiation, within this evidence set the strongest GO-relevant support is for BRAF’s placement and biochemical role in the ERK cascade rather than specific downstream phenotypes. (martinvega2023navigatingtheerk12 pages 2-4, bahar2023targetingtherasrafmapk pages 5-6)

---

### 4) Cellular component and protein-complex evidence (CC)

#### Cytosolic autoinhibited complexes
Multiple sources support that RAF proteins (including BRAF) reside in a **cytosolic autoinhibited monomeric state** stabilized by **14-3-3** binding to regulatory phosphosites (BRAF **S365** and **S729**) and often in complex with **MEK1**. (liu2024reconstitutionandcharacterization pages 1-2, bonsor2024rasandshoc2 pages 1-3, fiesco2022structuralinsightsinto pages 1-2)

#### Plasma membrane recruitment and active dimers
Upon RAS activation (GTP loading), BRAF is **recruited to the plasma membrane**, enabling CRD membrane engagement, exposure of the kinase dimer interface, and formation of **active RAF dimers** (homo- or heterodimers). (bonsor2024rasandshoc2 pages 6-8, mozzarelli2024functionalandstructural pages 6-7, liu2024reconstitutionandcharacterization pages 7-9)

#### Nucleus / endomembranes / mitochondria
In the retrieved GO-relevant corpus, there is **no direct experimental evidence** supporting BRAF localization to the **nucleus**, **Golgi/endomembrane compartments**, or **mitochondria**; therefore, these CC terms are not supported here and should not be inferred from downstream pathway membership. (liu2024reconstitutionandcharacterization pages 2-4, mozzarelli2024functionalandstructural pages 6-7, liu2024reconstitutionandcharacterization pages 7-9)

---

### 5) Wild-type BRAF vs oncogenic mutants (GO-relevant mechanistic distinctions)

#### Wild-type BRAF (regulated activation)
Wild-type BRAF is described as autoinhibited by 14-3-3 binding (pS365/pS729) and activated through **RAS-GTP-dependent membrane recruitment** followed by **dimerization** and conformational rearrangements. (martinvega2023navigatingtheerk12 pages 2-4, bonsor2024rasandshoc2 pages 1-3)

#### BRAFV600E and other oncogenic classes
Evidence supports distinct mechanistic behaviors relevant to GO annotation:
* **Class I (V600E)**: predominant oncogenic allele; can **signal as a monomer** and shows **constitutively high kinase activity** that is **not further increased by membrane-tethered RAS** in the reconstituted system; V600E is described as active regardless of oligomerization status. (martinvega2023navigatingtheerk12 pages 4-5, liu2024reconstitutionandcharacterization pages 7-9)
* **Class II mutants/fusions**: signal as **RAS-independent dimers** with increased activity (but generally less than V600E). (martinvega2023navigatingtheerk12 pages 4-5)
* **Class III mutants**: show **impaired kinase activity** and are described as not directly phosphorylating MEK while retaining RAS binding and ability to heterodimerize (implying a noncanonical/scaffold-like contribution rather than the core catalytic MF). (martinvega2023navigatingtheerk12 pages 4-5)

These distinctions should be captured in mutant-specific annotations and not conflated with wild-type function. (martinvega2023navigatingtheerk12 pages 4-5, liu2024reconstitutionandcharacterization pages 7-9)

---

### 6) Current applications and real-world implementations (GO-adjacent)
Although not GO terms per se, the mechanistic features above directly inform real-world implementations:
* **BRAF/MEK targeting** leverages the restricted substrate relationship (RAF→MEK→ERK). A 2023 high-citation review summarizes the pathway logic underpinning RAF/MEK inhibitor strategies and highlights dimerization-dependent activation as central to drug response/resistance mechanisms (relevant to how mutations shift BRAF’s GO-relevant catalytic state). (Bahar et al., *Signal Transduction and Targeted Therapy*, Dec 2023, DOI:10.1038/s41392-023-01705-z, URL https://doi.org/10.1038/s41392-023-01705-z) (bahar2023targetingtherasrafmapk pages 5-6)

---

### 7) Statistics and quantitative data (from retrieved studies)
* **RAS binding affinity (structural study):** Purified autoinhibited BRAF:14-3-3 (±MEK) complexes showed **nanomolar-range KRAS binding** in fluorescence polarization/pull-down assays, and mutating key basic RBD residues disrupts binding—quantitative support for “Ras GTPase binding” MF and RAS-dependent recruitment models. (fiesco2022structuralinsightsinto pages 5-7)
* **Membrane-dependent assembly/activity (nanodisc study):** BRAF:14-3-3:KRAS4B assembly was **GTP-dependent**, and lipid composition (e.g., anionic lipids) measurably altered on/off rates and KD in BLI assays; SEC resolved monomeric vs dimeric BRAF:14-3-3 complexes consistent with distinct inactive/active states. (liu2024reconstitutionandcharacterization pages 2-4, liu2024reconstitutionandcharacterization pages 7-9)

---

### 8) Curatorial cautions (avoid over-annotation)
* Avoid annotating generic “protein binding” when specific binding functions are supported (RAS-GTP binding; 14-3-3 binding; dimerization-related interactions). (fiesco2022structuralinsightsinto pages 5-7, fiesco2022structuralinsightsinto pages 4-5)
* Avoid inferring nuclear/endomembrane/mitochondrial localization or downstream phenotypes (apoptosis, immune, metabolic, transcriptional outcomes) from pathway membership in the absence of direct BRAF evidence in this corpus. (liu2024reconstitutionandcharacterization pages 2-4, liu2024reconstitutionandcharacterization pages 7-9)

---

### Key sources (URLs and dates)
* Liu NF et al. *Protein Science* (May 2024). “Reconstitution and characterization of BRAF in complex with 14-3-3 and KRAS4B on nanodiscs.” https://doi.org/10.1002/pro.5016 (liu2024reconstitutionandcharacterization pages 1-2)
* Bonsor DA, Simanshu DK. *Annual Review of Cancer Biology* (Jun 2024). “RAS and SHOC2 Roles in RAF Activation and Therapeutic Considerations.” https://doi.org/10.1146/annurev-cancerbio-062822-030450 (bonsor2024rasandshoc2 pages 1-3)
* Mozzarelli AM et al. *Molecular Cell* (Aug 2024). “Functional and structural insights into RAS effector proteins.” https://doi.org/10.1016/j.molcel.2024.06.027 (mozzarelli2024functionalandstructural pages 6-7)
* Martín-Vega A, Cobb MH. *Biomolecules* (Oct 2023). “Navigating the ERK1/2 MAPK Cascade.” https://doi.org/10.3390/biom13101555 (martinvega2023navigatingtheerk12 pages 2-4)
* Bahar ME et al. *Signal Transduction and Targeted Therapy* (Dec 2023). “Targeting the RAS/RAF/MAPK pathway for cancer therapy: from mechanism to clinical studies.” https://doi.org/10.1038/s41392-023-01705-z (bahar2023targetingtherasrafmapk pages 5-6)
* Martinez Fiesco JA et al. *Nature Communications* (Jan 2022). “Structural insights into the BRAF monomer-to-dimer transition mediated by RAS binding.” https://doi.org/10.1038/s41467-022-28084-3 (fiesco2022structuralinsightsinto pages 1-2)


References

1. (martinvega2023navigatingtheerk12 pages 2-4): Ana Martín-Vega and Melanie H. Cobb. Navigating the erk1/2 mapk cascade. Biomolecules, 13:1555, Oct 2023. URL: https://doi.org/10.3390/biom13101555, doi:10.3390/biom13101555. This article has 103 citations.

2. (bahar2023targetingtherasrafmapk pages 5-6): Md Entaz Bahar, Hyun Joon Kim, and D. Kim. Targeting the ras/raf/mapk pathway for cancer therapy: from mechanism to clinical studies. Signal Transduction and Targeted Therapy, Dec 2023. URL: https://doi.org/10.1038/s41392-023-01705-z, doi:10.1038/s41392-023-01705-z. This article has 938 citations and is from a peer-reviewed journal.

3. (liu2024reconstitutionandcharacterization pages 1-2): Ningdi F. Liu, Masahiro Enomoto, Christopher B. Marshall, and Mitsuhiko Ikura. Reconstitution and characterization of braf in complex with 14‐3‐3 and kras4b on nanodiscs. Protein Science : A Publication of the Protein Society, May 2024. URL: https://doi.org/10.1002/pro.5016, doi:10.1002/pro.5016. This article has 5 citations.

4. (liu2024reconstitutionandcharacterization pages 7-9): Ningdi F. Liu, Masahiro Enomoto, Christopher B. Marshall, and Mitsuhiko Ikura. Reconstitution and characterization of braf in complex with 14‐3‐3 and kras4b on nanodiscs. Protein Science : A Publication of the Protein Society, May 2024. URL: https://doi.org/10.1002/pro.5016, doi:10.1002/pro.5016. This article has 5 citations.

5. (imani2024theevolutionof pages 6-7): Saber Imani, Ghazaal Roozitalab, Mahdieh Emadi, Atefeh Moradi, Payam Behzadi, and Parham Jabbarzadeh Kaboli. The evolution of braf-targeted therapies in melanoma: overcoming hurdles and unleashing novel strategies. Frontiers in Oncology, Nov 2024. URL: https://doi.org/10.3389/fonc.2024.1504142, doi:10.3389/fonc.2024.1504142. This article has 51 citations.

6. (fiesco2022structuralinsightsinto pages 4-5): Juliana A. Martinez Fiesco, David E. Durrant, Deborah K. Morrison, and Ping Zhang. Structural insights into the braf monomer-to-dimer transition mediated by ras binding. Nature Communications, Jan 2022. URL: https://doi.org/10.1038/s41467-022-28084-3, doi:10.1038/s41467-022-28084-3. This article has 129 citations and is from a highest quality peer-reviewed journal.

7. (bonsor2024rasandshoc2 pages 1-3): Daniel A. Bonsor and Dhirendra K. Simanshu. Ras and shoc2 roles in raf activation and therapeutic considerations. Annual Review of Cancer Biology, 8:97-113, Jun 2024. URL: https://doi.org/10.1146/annurev-cancerbio-062822-030450, doi:10.1146/annurev-cancerbio-062822-030450. This article has 13 citations and is from a peer-reviewed journal.

8. (fiesco2022structuralinsightsinto pages 1-2): Juliana A. Martinez Fiesco, David E. Durrant, Deborah K. Morrison, and Ping Zhang. Structural insights into the braf monomer-to-dimer transition mediated by ras binding. Nature Communications, Jan 2022. URL: https://doi.org/10.1038/s41467-022-28084-3, doi:10.1038/s41467-022-28084-3. This article has 129 citations and is from a highest quality peer-reviewed journal.

9. (fiesco2022structuralinsightsinto pages 5-7): Juliana A. Martinez Fiesco, David E. Durrant, Deborah K. Morrison, and Ping Zhang. Structural insights into the braf monomer-to-dimer transition mediated by ras binding. Nature Communications, Jan 2022. URL: https://doi.org/10.1038/s41467-022-28084-3, doi:10.1038/s41467-022-28084-3. This article has 129 citations and is from a highest quality peer-reviewed journal.

10. (bonsor2024rasandshoc2 pages 4-6): Daniel A. Bonsor and Dhirendra K. Simanshu. Ras and shoc2 roles in raf activation and therapeutic considerations. Annual Review of Cancer Biology, 8:97-113, Jun 2024. URL: https://doi.org/10.1146/annurev-cancerbio-062822-030450, doi:10.1146/annurev-cancerbio-062822-030450. This article has 13 citations and is from a peer-reviewed journal.

11. (fiesco2022structuralinsightsinto pages 2-4): Juliana A. Martinez Fiesco, David E. Durrant, Deborah K. Morrison, and Ping Zhang. Structural insights into the braf monomer-to-dimer transition mediated by ras binding. Nature Communications, Jan 2022. URL: https://doi.org/10.1038/s41467-022-28084-3, doi:10.1038/s41467-022-28084-3. This article has 129 citations and is from a highest quality peer-reviewed journal.

12. (patel2023investigatingtherole pages 42-45): Khushali Patel. Investigating the role of oncogenic kras g12 mutations in cell signalling. Dissertation, Mar 2023. URL: https://doi.org/10.17863/cam.95441, doi:10.17863/cam.95441. This article has 0 citations.

13. (liu2024reconstitutionandcharacterization pages 9-10): Ningdi F. Liu, Masahiro Enomoto, Christopher B. Marshall, and Mitsuhiko Ikura. Reconstitution and characterization of braf in complex with 14‐3‐3 and kras4b on nanodiscs. Protein Science : A Publication of the Protein Society, May 2024. URL: https://doi.org/10.1002/pro.5016, doi:10.1002/pro.5016. This article has 5 citations.

14. (mozzarelli2024functionalandstructural pages 6-7): Alessandro M. Mozzarelli, Dhirendra K. Simanshu, and Pau Castel. Functional and structural insights into ras effector proteins. Molecular Cell, 84:2807-2821, Aug 2024. URL: https://doi.org/10.1016/j.molcel.2024.06.027, doi:10.1016/j.molcel.2024.06.027. This article has 35 citations and is from a highest quality peer-reviewed journal.

15. (bonsor2024rasandshoc2 pages 6-8): Daniel A. Bonsor and Dhirendra K. Simanshu. Ras and shoc2 roles in raf activation and therapeutic considerations. Annual Review of Cancer Biology, 8:97-113, Jun 2024. URL: https://doi.org/10.1146/annurev-cancerbio-062822-030450, doi:10.1146/annurev-cancerbio-062822-030450. This article has 13 citations and is from a peer-reviewed journal.

16. (liu2024reconstitutionandcharacterization pages 2-4): Ningdi F. Liu, Masahiro Enomoto, Christopher B. Marshall, and Mitsuhiko Ikura. Reconstitution and characterization of braf in complex with 14‐3‐3 and kras4b on nanodiscs. Protein Science : A Publication of the Protein Society, May 2024. URL: https://doi.org/10.1002/pro.5016, doi:10.1002/pro.5016. This article has 5 citations.

17. (fiesco2022structuralinsightsinto pages 8-9): Juliana A. Martinez Fiesco, David E. Durrant, Deborah K. Morrison, and Ping Zhang. Structural insights into the braf monomer-to-dimer transition mediated by ras binding. Nature Communications, Jan 2022. URL: https://doi.org/10.1038/s41467-022-28084-3, doi:10.1038/s41467-022-28084-3. This article has 129 citations and is from a highest quality peer-reviewed journal.

18. (martinvega2023navigatingtheerk12 pages 4-5): Ana Martín-Vega and Melanie H. Cobb. Navigating the erk1/2 mapk cascade. Biomolecules, 13:1555, Oct 2023. URL: https://doi.org/10.3390/biom13101555, doi:10.3390/biom13101555. This article has 103 citations.

## Citations

1. fiesco2022structuralinsightsinto pages 5-7
2. liu2024reconstitutionandcharacterization pages 7-9
3. liu2024reconstitutionandcharacterization pages 9-10
4. mozzarelli2024functionalandstructural pages 6-7
5. bahar2023targetingtherasrafmapk pages 5-6
6. liu2024reconstitutionandcharacterization pages 1-2
7. fiesco2022structuralinsightsinto pages 1-2
8. imani2024theevolutionof pages 6-7
9. fiesco2022structuralinsightsinto pages 4-5
10. fiesco2022structuralinsightsinto pages 2-4
11. patel2023investigatingtherole pages 42-45
12. liu2024reconstitutionandcharacterization pages 2-4
13. fiesco2022structuralinsightsinto pages 8-9
14. https://doi.org/10.1002/pro.5016
15. https://doi.org/10.1038/s41467-022-28084-3
16. https://doi.org/10.1146/annurev-cancerbio-062822-030450
17. https://doi.org/10.1016/j.molcel.2024.06.027
18. https://doi.org/10.3390/biom13101555
19. https://doi.org/10.1038/s41392-023-01705-z
20. https://doi.org/10.3390/biom13101555,
21. https://doi.org/10.1038/s41392-023-01705-z,
22. https://doi.org/10.1002/pro.5016,
23. https://doi.org/10.3389/fonc.2024.1504142,
24. https://doi.org/10.1038/s41467-022-28084-3,
25. https://doi.org/10.1146/annurev-cancerbio-062822-030450,
26. https://doi.org/10.17863/cam.95441,
27. https://doi.org/10.1016/j.molcel.2024.06.027,