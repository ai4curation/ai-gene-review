---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-26T23:53:25.903136'
end_time: '2026-09-27T00:01:59.526901'
duration_seconds: 513.62
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: MAP2K1
  gene_symbol: MAP2K1
  uniprot_accession: Q02750
  protein_description: 'RecName: Full=Dual specificity mitogen-activated protein kinase
    kinase 1 {ECO:0000305}; Short=MAP kinase kinase 1; Short=MAPKK 1; Short=MKK1;
    EC=2.7.12.2; AltName: Full=ERK activator kinase 1; AltName: Full=MAPK/ERK kinase
    1; Short=MEK 1;'
  gene_info: Name=MAP2K1 {ECO:0000312|HGNC:HGNC:6840}; Synonyms=MEK1, PRKMK1;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the protein kinase superfamily. STE Ser/Thr
  protein_domains: Kinase-like_dom_sf. (IPR011009); MAP_kinase_kinase. (IPR050915);
    Prot_kinase_dom. (IPR000719); Protein_kinase_ATP_BS. (IPR017441); Ser/Thr_kinase_AS.
    (IPR008271)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 21
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: MAP2K1-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q02750
- **Protein Description:** RecName: Full=Dual specificity mitogen-activated protein kinase kinase 1 {ECO:0000305}; Short=MAP kinase kinase 1; Short=MAPKK 1; Short=MKK1; EC=2.7.12.2; AltName: Full=ERK activator kinase 1; AltName: Full=MAPK/ERK kinase 1; Short=MEK 1;
- **Gene Information:** Name=MAP2K1 {ECO:0000312|HGNC:HGNC:6840}; Synonyms=MEK1, PRKMK1;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the protein kinase superfamily. STE Ser/Thr
- **Key Domains:** Kinase-like_dom_sf. (IPR011009); MAP_kinase_kinase. (IPR050915); Prot_kinase_dom. (IPR000719); Protein_kinase_ATP_BS. (IPR017441); Ser/Thr_kinase_AS. (IPR008271)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MAP2K1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MAP2K1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MAP2K1** (gene ID: MAP2K1, UniProt: Q02750) in human.

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
- **UniProt Accession:** Q02750
- **Protein Description:** RecName: Full=Dual specificity mitogen-activated protein kinase kinase 1 {ECO:0000305}; Short=MAP kinase kinase 1; Short=MAPKK 1; Short=MKK1; EC=2.7.12.2; AltName: Full=ERK activator kinase 1; AltName: Full=MAPK/ERK kinase 1; Short=MEK 1;
- **Gene Information:** Name=MAP2K1 {ECO:0000312|HGNC:HGNC:6840}; Synonyms=MEK1, PRKMK1;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the protein kinase superfamily. STE Ser/Thr
- **Key Domains:** Kinase-like_dom_sf. (IPR011009); MAP_kinase_kinase. (IPR050915); Prot_kinase_dom. (IPR000719); Protein_kinase_ATP_BS. (IPR017441); Ser/Thr_kinase_AS. (IPR008271)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MAP2K1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MAP2K1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MAP2K1** (gene ID: MAP2K1, UniProt: Q02750) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# MAP2K1/MEK1 (human; UniProt Q02750): Functional-Annotation Research Report

## Executive summary

**Identity is verified.** The requested target is human **MAP2K1**, encoding **MEK1** (MAP kinase kinase 1; UniProt **Q02750**), not its paralog MAP2K2/MEK2 or another MAP2K-family kinase. The literature consistently identifies MAP2K1 as MEK1, an approximately 44-kDa ERK-specific MAPK kinase. Its protein-kinase fold, ATP-binding machinery, MAPK-kinase role, and dual-specificity activity agree with the supplied InterPro annotations. Searches that returned MAP2K7 concerned a different human kinase and were excluded. (barbosa2021themekerknetwork pages 5-8, martinvega2023navigatingtheerk12 pages 4-5, barbosa2021themekerknetwork pages 1-5)

MEK1 is the central kinase relay between RAF and ERK in the canonical receptor–RAS–RAF–MEK–ERK pathway. Its principal enzymatic function is ATP-dependent phosphorylation of ERK1/MAPK3 and ERK2/MAPK1 on both threonine and tyrosine in their activation-loop TEY motifs. Despite being “dual-specificity,” MEK1 has unusually narrow protein-substrate specificity: ERK1 and ERK2 are its established physiological downstream substrates. (velsen2026molecularbasisof pages 1-3, gao2018allelespecificmechanismsof pages 15-18, barbosa2021themekerknetwork pages 1-5)

| Topic | Current conclusion | Key exact details/numbers | Evidence type and caveat |
|---|---|---|---|
| Identity and paralog distinction | Target is **human MAP2K1/MEK1**, UniProt **Q02750**, not MAP2K2/MEK2 or another MAP2K-family member. | Canonical name: dual-specificity mitogen-activated protein kinase kinase 1; approximately **44 kDa**. MEK1 and MEK2 are distinct ERK-specific MAP2Ks. (martinvega2023navigatingtheerk12 pages 4-5, barbosa2021themekerknetwork pages 1-5) | Accession and organism are from the supplied UniProt identity; literature independently confirms the MAP2K1–MEK1 naming and biochemical role, although the cited excerpts do not reproduce Q02750. |
| Enzyme reaction and substrate residues | MEK1 is an ATP-dependent dual-specificity kinase that transfers phosphate to threonine and tyrosine in the ERK activation-loop **TEY** motif. | Net reaction: ATP + ERK1/2-OH → ADP + phospho-ERK1/2. Full activation involves ERK1 **Thr202/Tyr204** and ERK2 **Thr185/Tyr187**; recombinant assays used ATP and inactive ERK2. (barbosa2021themekerknetwork pages 5-8, gao2018allelespecificmechanismsof pages 15-18, barbosa2021themekerknetwork pages 1-5) | Exact phosphosites and ATP-dependent kinase assays provide biochemical evidence. The net equation is the standard kinase reaction inferred from these data. |
| Substrate specificity | MEK1 has unusually narrow protein-substrate specificity: its established physiological downstream substrates are **ERK1/MAPK3 and ERK2/MAPK1**. | MEK1 modifies both residues of the ERK TEY motif, whereas activated ERK1/2 subsequently act on hundreds of cytoplasmic and nuclear targets. (velsen2026molecularbasisof pages 1-3, barbosa2021themekerknetwork pages 1-5) | Supported by mechanistic reviews and biochemical assays; proposed noncanonical substrates should not be equated with the established ERK1/2 relationship. |
| Activation and feedback | RAF activates MEK1 by phosphorylating its activation segment; ERK provides direct negative feedback. | RAF sites: **Ser218 and Ser222**. ERK feedback site: **Thr292**, a MEK1-specific modification that promotes phosphatase access and dephosphorylation of Ser218/Ser222. (barbosa2021themekerknetwork pages 5-8, martinvega2023navigatingtheerk12 pages 4-5) | Site-specific mechanistic evidence is strong. RAF is canonical, although other upstream kinases can activate MEK in particular contexts. |
| Structure and domains | MAP2K1 has the expected STE-family protein-kinase fold and regulatory elements, consistent with the supplied kinase-like, MAP kinase kinase, ATP-binding, and Ser/Thr-kinase annotations. | Features include N- and C-terminal kinase lobes, ATP-binding cleft, glycine-rich loop, αC helix, DFG and APE/SPE motifs, catalytic/regulatory spines, N-terminal ERK-binding region, nuclear-export sequence, regulatory αA helix, and C-terminal proline-rich insert. (barbosa2021themekerknetwork pages 5-8) | Structural and sequence evidence aligns with the supplied InterPro domains. Dual specificity denotes ERK threonine/tyrosine phosphorylation, not broad substrate promiscuity. |
| Subcellular localization | MEK1 acts predominantly in the **cytoplasm**, including signaling complexes recruited to the plasma membrane, while dynamically shuttling through the nucleus. | Its nuclear-export sequence favors cytosolic localization. MEK1 anchors ERK in the cytoplasm and supports XPO1/CRM1-dependent ERK nuclear export; RAF–MEK complexes reach the plasma membrane after RAS activation. (martinvega2023navigatingtheerk12 pages 4-5, barbosa2021themekerknetwork pages 1-5, barbosa2021themekerknetwork pages 11-14) | Localization is stimulus- and scaffold-dependent rather than exclusive to one compartment; MEK1 is not a transmembrane protein. |
| Pathway role | MEK1 is the middle kinase tier of the canonical **receptor → RAS → RAF → MEK1/2 → ERK1/2** cascade. | Activated ERK controls proliferation, differentiation, survival, and cell-cycle programs. MEK1 also serves as an ERK-binding and trafficking factor. (martinvega2023navigatingtheerk12 pages 4-5, barbosa2021themekerknetwork pages 1-5, barbosa2021themekerknetwork pages 11-14) | Biological output depends on signal amplitude, duration, localization, cell type, and feedback. |
| Oncogenic mutation classes | Activating MAP2K1 alleles fall into three mechanistic classes defined by RAF dependence and structural behavior. | **Class 1:** RAF-dependent amplifiers. **Class 2:** RAF-regulated, with variable RAF-independent activity. **Class 3:** RAF-independent, often β3–αC-loop deletions around residues **98–104**, strongly active and relatively resistant to approved allosteric MEK inhibitors. (gao2018allelespecificmechanismsof pages 9-12, dankner2024clinicalactivityof pages 6-10) | Classification derives from selected cancer alleles. Drug response is allele- and regimen-dependent, so class alone is not a complete clinical biomarker. |
| Human disease associations | MAP2K1 dysregulation is implicated in cancer, developmental RASopathy, and mosaic disease. | Evidence supports associations with **cancer, melanoma, cardio-facio-cutaneous syndrome/CFC3, and melorheostosis**. Germline activating variants cause CFC syndrome; somatic variants occur in tumors and mosaic disorders. (OpenTargets Search: -MAP2K1, gao2018allelespecificmechanismsof pages 9-12) | Germline, mosaic, and tumor-acquired variants have distinct phenotypic and therapeutic implications. |
| Approved MEK-directed inhibitors | Four established allosteric inhibitors target MEK1, usually together with MEK2; approvals are indication-specific rather than uniformly based on MAP2K1 mutation. | **Trametinib:** MEK1/2 IC50 **2 nM**, FDA approval **2013**. **Cobimetinib:** MEK1 IC50 **4.2 nM**, **2015**. **Binimetinib:** MEK1/2 IC50 **12 nM**, **2018**. **Selumetinib:** MEK1 IC50 **14 nM**, **2020**. (martinvega2023navigatingtheerk12 pages 21-22) | Potencies come from representative biochemical assays and are not directly interchangeable across assay systems. |
| 2024 MAP2K1-mutant cancer evidence | A 2024 systematic review/meta-analysis suggested modest overall MAPK-inhibitor activity, with potentially greater durability in Class 2 tumors. | AACR GENIE: **Class 2, 63%; Class 1, 24%; Class 3, 13%**. Among **46** treated patients: response rate **28%** and median PFS **3.9 months**. Class 2 versus other classes: PFS **5.0 vs 3.5 months** (*P*=0.04); response duration **23.8 vs 4.2 months** (*P*=0.02). (dankner2024clinicalactivityof pages 1-6, dankner2024clinicalactivityof pages 14-18) | The 2024 medRxiv report was non-peer-reviewed and based on small, heterogeneous published cases; a 2025 peer-reviewed publication reported the same principal estimates. (dankner2025clinicalactivityof pages 1-2) |
| Recent analytical development | Whole-protein mass spectrometry can directly measure complex MEK1 phosphoproteoform distributions in drug-resistant melanoma models. | Individual-ion mass spectrometry resolved MEK1 populations bearing **0–4 phosphorylations**. | This is an analytical advance rather than a clinically validated biomarker; prospective validation remains necessary. |


*Table: Compact evidence table for human MAP2K1/MEK1 (UniProt Q02750), covering identity, enzymology, regulation, localization, disease mechanisms, inhibitors, and recent clinical data. Caveats distinguish established functional annotation from emerging translational evidence.*

## 1. Target verification and nomenclature

The supplied identity—**MAP2K1; synonyms MEK1 and PRKMK1; Homo sapiens; UniProt Q02750**—is internally and externally consistent. Authoritative pathway literature distinguishes two ERK-directed MAP2Ks, MEK1/MAP2K1 and MEK2/MAP2K2, and identifies MEK1 as a 44-kDa kinase downstream of RAF. Thus, reports using *MEK1*, *MAP2K1*, or “MAP kinase kinase 1” concern the requested protein when the human context is explicit. (martinvega2023navigatingtheerk12 pages 4-5, barbosa2021themekerknetwork pages 1-5)

The family/domain assignment also matches the evidence. MEK1 has the bilobal protein-kinase architecture, ATP-binding catalytic cleft, glycine-rich loop, αC helix, DFG and APE/SPE motifs, and catalytic and regulatory spines expected of a STE-family MAP2K. These structural features align with the supplied kinase-like, MAP-kinase-kinase, protein-kinase, ATP-binding, and Ser/Thr-kinase domain annotations. (barbosa2021themekerknetwork pages 5-8)

## 2. Primary biochemical function

### 2.1 Catalyzed reaction

MEK1 catalyzes the conventional kinase reaction:

**ATP + ERK1/2–OH → ADP + phosphorylated ERK1/2.**

It transfers the ATP γ-phosphate to both residues of the ERK activation-loop **Thr-Glu-Tyr (TEY)** motif. The relevant sites are **Thr202 and Tyr204 in ERK1** and **Thr185 and Tyr187 in ERK2**. Dual phosphorylation is required for full ERK activation. Recombinant MEK1 assays employing ATP and inactive ERK2 directly support this kinase–substrate relationship. (barbosa2021themekerknetwork pages 5-8, gao2018allelespecificmechanismsof pages 15-18, barbosa2021themekerknetwork pages 1-5)

The term **dual-specificity** refers to MEK1’s ability to phosphorylate both threonine and tyrosine—not to broad protein-substrate promiscuity. MEK1/2 have exceptionally restricted downstream specificity, with ERK1/2 described as their only established physiological targets. Activated ERK1/2, by contrast, phosphorylate a much broader set of cytoplasmic and nuclear proteins. (barbosa2021themekerknetwork pages 1-5)

### 2.2 Substrate recognition

Specificity is produced by more than recognition of the TEY sequence. MEK1 has an N-terminal ERK-binding or kinase-interaction region, while ERK provides a common-docking surface. These docking contacts position the ERK activation loop for catalysis. Structural work also identifies MEK1’s N-terminal regulatory αA helix and a C-terminal proline-rich insert as modulators of ERK interaction and phosphorylation. (barbosa2021themekerknetwork pages 5-8, velsen2026molecularbasisof pages 1-3)

The most detailed MEK1–ERK2 structural model retrieved was a January 2026 cryo-EM preprint, later than the requested priority window and not peer reviewed. It supports a model in which ERK docking destabilizes the regulatory αA helix and releases MEK1’s catalytic machinery; it also suggests ERK2 need not dissociate for nucleotide exchange, potentially permitting processive dual phosphorylation. This is an important emerging mechanism but should not yet outweigh established biochemical evidence. DOI: https://doi.org/10.64898/2026.01.19.700303. (velsen2026molecularbasisof pages 1-3)

## 3. Activation, feedback, and structural regulation

Canonical activation occurs when RAF phosphorylates MEK1 at **Ser218 and Ser222** in its activation segment. Once activated, MEK1 phosphorylates ERK1/2. ERK then feeds back on MEK1 by phosphorylating **Thr292**, a MEK1-specific event that promotes phosphatase access and dephosphorylation of Ser218/Ser222. This negative feedback helps limit signal amplitude and duration. (barbosa2021themekerknetwork pages 5-8, martinvega2023navigatingtheerk12 pages 4-5)

The N-terminal αA helix and the β3–αC-loop region stabilize autoinhibitory conformations. Disease-associated substitutions, helix-breaking changes, or deletions can shift MEK1 toward an active conformation. Deletions around residues **98–104** are particularly important in strongly RAF-independent mutants. (barbosa2021themekerknetwork pages 5-8, gao2018allelespecificmechanismsof pages 9-12)

MEK1 regulation is therefore not a simple binary switch. Its output integrates RAF phosphorylation, autoinhibitory conformation, ERK-mediated feedback, phosphatase action, dimerization, docking, and scaffold-dependent localization. The exact in-vivo architecture of RAF–MEK dimers and transient higher-order complexes remains incompletely resolved. (martinvega2023navigatingtheerk12 pages 4-5, barbosa2021themekerknetwork pages 11-14)

## 4. Subcellular localization and site of action

MEK1 functions predominantly in the **cytoplasm**, where it binds ERK and acts as a cytoplasmic anchor. Its N-terminal nuclear-export sequence favors cytosolic accumulation. MEK1 nevertheless shuttles between nucleus and cytoplasm and contributes to XPO1/CRM1-dependent export of ERK from the nucleus. Thus, “cytoplasmic” is the dominant steady-state description, not an absolute compartmental restriction. (martinvega2023navigatingtheerk12 pages 4-5, barbosa2021themekerknetwork pages 11-14)

Spatially, the pathway begins at activated cell-surface receptors. RAS recruits and activates RAF at the inner plasma membrane; RAF–MEK complexes are consequently recruited to membrane-proximal signaling assemblies, where MEK1 receives activating phosphorylation. Activated MEK1 then acts on ERK in cytoplasmic complexes. ERK dissociates and can enter the nucleus to regulate transcription, while MEK1 contributes to its subsequent nuclear export and cytoplasmic retention. MEK1 itself is a soluble intracellular kinase, not a transmembrane protein and not a secreted enzyme. (barbosa2021themekerknetwork pages 1-5, barbosa2021themekerknetwork pages 11-14)

## 5. Pathway role and biological interpretation

The core pathway is:

**growth factor/other extracellular signal → receptor → RAS-GTP → RAF → MEK1/MEK2 → ERK1/ERK2 → cytoplasmic and nuclear effectors.**

MEK1’s precise function is signal transmission and control at the MAP2K tier. It converts RAF activity into ERK activation while also organizing ERK localization. ERK then controls context-dependent programs involving proliferation, cell-cycle progression, differentiation, survival, migration, metabolism, and development. These broad outcomes should be viewed as consequences of MEK1-mediated ERK activation rather than independent catalytic functions of MEK1. (martinvega2023navigatingtheerk12 pages 4-5, barbosa2021themekerknetwork pages 1-5, barbosa2021themekerknetwork pages 11-14)

Signal outcome depends on amplitude, duration, pulsatility, subcellular location, scaffold composition, and feedback. The 2023 review by Martín-Vega and Cobb emphasizes this localization and interaction logic rather than treating the pathway as a simple linear chain. Published October 2023; DOI: https://doi.org/10.3390/biom13101555. (martinvega2023navigatingtheerk12 pages 4-5)

## 6. Disease mechanisms

### 6.1 Somatic cancer mutations

Oncogenic MAP2K1 alleles can be divided mechanistically into three classes:

- **Class 1—RAF-dependent:** weak oncogenes that require RAF phosphorylation at Ser218/Ser222, remain sensitive to ERK feedback, and commonly coexist with upstream RAS, RAF, or NF1 alterations.
- **Class 2—RAF-regulated:** possess variable basal RAF-independent activity but can be further activated by RAF; these alleles can mediate acquired resistance to RAF-directed therapy.
- **Class 3—RAF-independent:** frequently contain β3–αC-loop deletions, can signal autonomously, and may be poorly inhibited by approved allosteric MEK inhibitors because the altered structure impairs inhibitor engagement. (gao2018allelespecificmechanismsof pages 9-12, dankner2024clinicalactivityof pages 6-10)

This classification is functionally more useful than labeling every MAP2K1 variant as equivalent. In experimental work, Class 1 and 2 mutants generally responded to allosteric MEK inhibition, whereas Class 3 mutants were resistant but remained susceptible to the ATP-competitive research inhibitor MAP855. (gao2018allelespecificmechanismsof pages 9-12)

MAP2K1 alterations have been linked to melanoma, lung and colorectal cancers, histiocytic neoplasms, and other tumors. Open Targets integrates genetic, somatic, literature, and therapeutic evidence linking MAP2K1 to cancer and melanoma, while also recording associations with cardio-facio-cutaneous syndrome and melorheostosis. Database association scores are useful evidence summaries, not prevalence estimates or proof that every variant is causal. (OpenTargets Search: -MAP2K1)

### 6.2 Germline and mosaic disease

Heterozygous germline activating variants in MAP2K1 cause **cardio-facio-cutaneous syndrome**, a developmental RASopathy. The molecular principle is excessive RAS–MAPK signaling during development; clinical consequences can involve craniofacial, cardiac, ectodermal, growth, and neurological abnormalities. Treatment remains primarily supportive, and repurposing of MEK inhibitors is investigational rather than established disease-modifying care. The authoritative disease association is independently captured by Open Targets. (OpenTargets Search: -MAP2K1)

Post-zygotic activating MAP2K1 mutations cause mosaic disorders including **melorheostosis**, in which affected tissue has elevated ERK activation. The localization of variants to affected rather than unaffected tissue and the downstream phospho-ERK phenotype provide a mechanistic link from mutation to disease. (OpenTargets Search: -MAP2K1)

## 7. Current applications and real-world implementation

### 7.1 Pharmacological inhibition

Four established allosteric MEK inhibitors target MEK1, generally together with MEK2:

- **Trametinib:** representative MEK1/2 IC50 2 nM; FDA approval in 2013.
- **Cobimetinib:** MEK1 IC50 4.2 nM; approval in 2015.
- **Binimetinib:** MEK1/2 IC50 12 nM; approval in 2018.
- **Selumetinib:** MEK1 IC50 14 nM; approval in 2020. (martinvega2023navigatingtheerk12 pages 21-22)

These potency values come from particular biochemical systems and should not be compared as though they directly predict clinical dose or efficacy. The drugs are deployed in indication-specific regimens, frequently combined with RAF inhibitors to deepen pathway suppression and delay adaptive reactivation. Their clinical approvals usually reflect pathway dependence—such as BRAF-driven disease—not necessarily the presence of a MAP2K1 mutation itself. (martinvega2023navigatingtheerk12 pages 21-22)

### 7.2 MAP2K1 mutation as a biomarker

The most informative recent quantitative analysis was posted in March 2024 and subsequently peer reviewed in January 2025. In AACR GENIE v13, **63%** of classified MAP2K1 mutations were Class 2, **24%** Class 1, and **13%** Class 3. A systematic review found 46 MAP2K1-mutant patients treated with MAPK-pathway inhibitors: overall response rate was **28%**, and median progression-free survival was **3.9 months**. Class 2 cases had longer median PFS than the combined other classes—**5.0 versus 3.5 months** (*P*=0.04)—and markedly longer response duration—**23.8 versus 4.2 months** (*P*=0.02). (dankner2024clinicalactivityof pages 1-6, dankner2025clinicalactivityof pages 1-2)

These data support Class 2 MAP2K1 as a candidate predictive biomarker, but the evidence is not definitive. The cohort was small and assembled from heterogeneous published cases, therapies, and tumor types. The response rate did not significantly differ by class or cancer type, and both Class 3 cases in the 2024 analysis progressed on targeted therapy. Prospective, class-stratified studies are needed. Preprint DOI: https://doi.org/10.1101/2024.03.23.24304779; peer-reviewed publication, January 27, 2025: https://doi.org/10.1200/PO.24.00199. (dankner2024clinicalactivityof pages 1-6, dankner2025clinicalactivityof pages 1-2, dankner2024clinicalactivityof pages 14-18)

The same analysis found that **4 of 6 colorectal cancers** acquired MAP2K1 mutations after sotorasib resistance, illustrating a second real-world use: MAP2K1 alterations can be markers of pathway-reactivating resistance rather than original tumor drivers. Treatment selection must therefore account for mutation class, clonality, timing, co-mutations, and prior therapy. (dankner2024clinicalactivityof pages 14-18)

## 8. Recent research developments, 2023–2024

1. **Updated pathway framework (2023).** Martín-Vega and Cobb synthesized current understanding of ERK-cascade structure, feedback, compartmentalization, mutation classes, and therapeutic targeting. The expert interpretation is that scaffold and localization biology are central determinants of MEK–ERK output, not secondary details. Published October 2023; https://doi.org/10.3390/biom13101555. (martinvega2023navigatingtheerk12 pages 4-5, martinvega2023navigatingtheerk12 pages 21-22)

2. **Mutation-class clinical evidence (2024).** The 46-patient systematic analysis supplied quantitative evidence that Class 2 MAP2K1 tumors may experience more durable benefit from MAPK inhibitors, while emphasizing the need for prospective validation. Posted March 24, 2024; https://doi.org/10.1101/2024.03.23.24304779. (dankner2024clinicalactivityof pages 1-6, dankner2024clinicalactivityof pages 14-18)

3. **Proteoform-resolved measurement (2024).** Individual-ion mass spectrometry was applied to MEK1 in a drug-resistant metastatic-melanoma model and resolved proteoforms carrying zero to four phosphorylations. This is important because bulk phospho-MEK assays collapse multiple regulatory states into one measurement. The method is presently an analytical research tool, not a clinically validated biomarker.

4. **Continuing structural interpretation.** Molecular and structural studies increasingly frame MEK1 activation as release of autoinhibitory elements coupled to substrate docking. Computational work can generate mechanistic hypotheses, but predictions about inhibitor ranking require biochemical and clinical validation; simulation alone does not establish therapeutic efficacy.

## 9. Evidence assessment and expert interpretation

The strongest functional annotation is the narrow MEK1→ERK1/2 relationship: site-specific biochemical assays, structural work, phosphosite mapping, and decades of pathway genetics converge on it. The strongest localization model is that MEK1 is predominantly cytoplasmic but dynamically scaffolded and shuttling, operating in membrane-proximal RAF complexes and cytoplasmic MEK–ERK complexes while controlling ERK nuclear export. (barbosa2021themekerknetwork pages 5-8, martinvega2023navigatingtheerk12 pages 4-5, gao2018allelespecificmechanismsof pages 15-18, barbosa2021themekerknetwork pages 11-14)

The most important translational caution is that **MEK1 inhibition and MAP2K1-mutant precision therapy are not synonymous**. Approved inhibitors commonly target both MEK1 and MEK2 and are often used because an upstream lesion makes the pathway dependent on MEK. Conversely, activating MAP2K1 variants differ substantially in RAF dependence, feedback control, and allosteric-inhibitor sensitivity. Variant-level functional interpretation is therefore essential. (gao2018allelespecificmechanismsof pages 9-12, martinvega2023navigatingtheerk12 pages 21-22, dankner2024clinicalactivityof pages 6-10)

## Conclusion

Human MAP2K1/Q02750 encodes MEK1, a soluble STE-family dual-specificity kinase whose primary function is ATP-dependent dual phosphorylation and activation of ERK1/2. It operates mainly in cytoplasmic and membrane-proximal signaling complexes, also controlling ERK trafficking between cytoplasm and nucleus. RAF phosphorylation at Ser218/Ser222 activates MEK1, while ERK phosphorylation at Thr292 contributes negative feedback. Germline, mosaic, and somatic activating variants produce distinct developmental, skeletal, and neoplastic phenotypes. MEK1 is a validated drug target, but therapeutic response depends on pathway context and mutant class; recent clinical synthesis suggests Class 2 MAP2K1-mutant tumors may derive the most durable benefit, although current evidence remains limited and retrospective.

References

1. (barbosa2021themekerknetwork pages 5-8): Renee Barbosa, Lucila A. Acevedo, and Ronen Marmorstein. The mek/erk network as a therapeutic target in human cancer. Molecular Cancer Research, 19:361-374, Mar 2021. URL: https://doi.org/10.1158/1541-7786.mcr-20-0687, doi:10.1158/1541-7786.mcr-20-0687. This article has 254 citations and is from a peer-reviewed journal.

2. (martinvega2023navigatingtheerk12 pages 4-5): Ana Martín-Vega and Melanie H. Cobb. Navigating the erk1/2 mapk cascade. Biomolecules, 13:1555, Oct 2023. URL: https://doi.org/10.3390/biom13101555, doi:10.3390/biom13101555. This article has 144 citations.

3. (barbosa2021themekerknetwork pages 1-5): Renee Barbosa, Lucila A. Acevedo, and Ronen Marmorstein. The mek/erk network as a therapeutic target in human cancer. Molecular Cancer Research, 19:361-374, Mar 2021. URL: https://doi.org/10.1158/1541-7786.mcr-20-0687, doi:10.1158/1541-7786.mcr-20-0687. This article has 254 citations and is from a peer-reviewed journal.

4. (velsen2026molecularbasisof pages 1-3): Jill von Velsen, Pauline Juyoux, Nicola Piasentin, Hayden Fisher, Karine Lapouge, Oscar Vadas, Francesco Luigi Gervasio, and Matthew W. Bowler. Molecular basis of mitogen-activated protein kinase erk2 activation by its upstream kinase mek1. bioRxiv, Jan 2026. URL: https://doi.org/10.64898/2026.01.19.700303, doi:10.64898/2026.01.19.700303. This article has 0 citations.

5. (gao2018allelespecificmechanismsof pages 15-18): Yijun Gao, Matthew T. Chang, Daniel McKay, Na Na, Bing Zhou, Rona Yaeger, Neilawattie M. Torres, Keven Muniz, Matthias Drosten, Mariano Barbacid, Giordano Caponigro, Darrin Stuart, Henrik Moebitz, David B. Solit, Omar Abdel-Wahab, Barry S. Taylor, Zhan Yao, and Neal Rosen. Allele-specific mechanisms of activation of mek1 mutants determine their properties. Cancer discovery, 8 5:648-661, May 2018. URL: https://doi.org/10.1158/2159-8290.cd-17-1452, doi:10.1158/2159-8290.cd-17-1452. This article has 168 citations and is from a highest quality peer-reviewed journal.

6. (barbosa2021themekerknetwork pages 11-14): Renee Barbosa, Lucila A. Acevedo, and Ronen Marmorstein. The mek/erk network as a therapeutic target in human cancer. Molecular Cancer Research, 19:361-374, Mar 2021. URL: https://doi.org/10.1158/1541-7786.mcr-20-0687, doi:10.1158/1541-7786.mcr-20-0687. This article has 254 citations and is from a peer-reviewed journal.

7. (gao2018allelespecificmechanismsof pages 9-12): Yijun Gao, Matthew T. Chang, Daniel McKay, Na Na, Bing Zhou, Rona Yaeger, Neilawattie M. Torres, Keven Muniz, Matthias Drosten, Mariano Barbacid, Giordano Caponigro, Darrin Stuart, Henrik Moebitz, David B. Solit, Omar Abdel-Wahab, Barry S. Taylor, Zhan Yao, and Neal Rosen. Allele-specific mechanisms of activation of mek1 mutants determine their properties. Cancer discovery, 8 5:648-661, May 2018. URL: https://doi.org/10.1158/2159-8290.cd-17-1452, doi:10.1158/2159-8290.cd-17-1452. This article has 168 citations and is from a highest quality peer-reviewed journal.

8. (dankner2024clinicalactivityof pages 6-10): Matthew Dankner, Emmanuelle Rousselle, Sarah Petrecca, François Fabi, Alexander Nowakowski, Anna-Maria Lazaratos, Charles Vincent Rajadurai, Andrew J. B. Stein, David Bian, Peter Tai, Alicia Belaiche, Meredith Li, Andrea Quaiattini, Nicola Normanno, Maria Arcila, Arielle Elkrief, Douglas B. Johnson, Marc Ladanyi, and April A. N. Rose. Clinical activity of mitogen-activated protein kinase (mapk) inhibitors in patients with map2k1 (mek1)-mutated metastatic cancers. MedRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.23.24304779, doi:10.1101/2024.03.23.24304779. This article has 1 citations.

9. (OpenTargets Search: -MAP2K1): Open Targets Query (-MAP2K1, 10 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

10. (martinvega2023navigatingtheerk12 pages 21-22): Ana Martín-Vega and Melanie H. Cobb. Navigating the erk1/2 mapk cascade. Biomolecules, 13:1555, Oct 2023. URL: https://doi.org/10.3390/biom13101555, doi:10.3390/biom13101555. This article has 144 citations.

11. (dankner2024clinicalactivityof pages 1-6): Matthew Dankner, Emmanuelle Rousselle, Sarah Petrecca, François Fabi, Alexander Nowakowski, Anna-Maria Lazaratos, Charles Vincent Rajadurai, Andrew J. B. Stein, David Bian, Peter Tai, Alicia Belaiche, Meredith Li, Andrea Quaiattini, Nicola Normanno, Maria Arcila, Arielle Elkrief, Douglas B. Johnson, Marc Ladanyi, and April A. N. Rose. Clinical activity of mitogen-activated protein kinase (mapk) inhibitors in patients with map2k1 (mek1)-mutated metastatic cancers. MedRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.23.24304779, doi:10.1101/2024.03.23.24304779. This article has 1 citations.

12. (dankner2024clinicalactivityof pages 14-18): Matthew Dankner, Emmanuelle Rousselle, Sarah Petrecca, François Fabi, Alexander Nowakowski, Anna-Maria Lazaratos, Charles Vincent Rajadurai, Andrew J. B. Stein, David Bian, Peter Tai, Alicia Belaiche, Meredith Li, Andrea Quaiattini, Nicola Normanno, Maria Arcila, Arielle Elkrief, Douglas B. Johnson, Marc Ladanyi, and April A. N. Rose. Clinical activity of mitogen-activated protein kinase (mapk) inhibitors in patients with map2k1 (mek1)-mutated metastatic cancers. MedRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.23.24304779, doi:10.1101/2024.03.23.24304779. This article has 1 citations.

13. (dankner2025clinicalactivityof pages 1-2): Matthew Dankner, Emmanuelle Rousselle, Sarah Petrecca, François Fabi, Alexander Nowakowski, Anna-Maria Lazaratos, Charles Vincent Rajadurai, Andrew J.B. Stein, David Bian, Peter Tai, Alicia Belaiche, Meredith Li, Andrea Quaiattini, Nicola Normanno, Maria Arcila, Arielle Elkrief, Douglas B. Johnson, Marc Ladanyi, and April A.N. Rose. Clinical activity of mitogen-activated protein kinase inhibitors in patients with map2k1 (mek1)-mutated metastatic cancers. Jan 2025. URL: https://doi.org/10.1200/po.24.00199, doi:10.1200/po.24.00199. This article has 9 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](MAP2K1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. barbosa2021themekerknetwork pages 5-8
2. dankner2025clinicalactivityof pages 1-2
3. barbosa2021themekerknetwork pages 1-5
4. velsen2026molecularbasisof pages 1-3
5. gao2018allelespecificmechanismsof pages 9-12
6. dankner2024clinicalactivityof pages 14-18
7. gao2018allelespecificmechanismsof pages 15-18
8. barbosa2021themekerknetwork pages 11-14
9. dankner2024clinicalactivityof pages 6-10
10. dankner2024clinicalactivityof pages 1-6
11. https://doi.org/10.64898/2026.01.19.700303.
12. https://doi.org/10.3390/biom13101555.
13. https://doi.org/10.1101/2024.03.23.24304779;
14. https://doi.org/10.1200/PO.24.00199.
15. https://doi.org/10.1101/2024.03.23.24304779.
16. https://doi.org/10.1158/1541-7786.mcr-20-0687,
17. https://doi.org/10.3390/biom13101555,
18. https://doi.org/10.64898/2026.01.19.700303,
19. https://doi.org/10.1158/2159-8290.cd-17-1452,
20. https://doi.org/10.1101/2024.03.23.24304779,
21. https://doi.org/10.1200/po.24.00199,