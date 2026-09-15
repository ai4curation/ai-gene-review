---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T13:55:47.241371'
end_time: '2026-09-08T14:06:16.271625'
duration_seconds: 629.03
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: GHSR
  gene_symbol: GHSR
  uniprot_accession: F6QF00
  protein_description: 'RecName: Full=Growth hormone secretagogue receptor type 1
    {ECO:0000256|ARBA:ARBA00018726}; AltName: Full=GH-releasing peptide receptor {ECO:0000256|ARBA:ARBA00033151};
    AltName: Full=Ghrelin receptor {ECO:0000256|ARBA:ARBA00032291};'
  gene_info: Name=GHSR {ECO:0000313|VGNC:VGNC:18336};
  organism_full: Equus caballus (Horse).
  protein_family: Belongs to the G protein-coupled receptor 1 family.
  protein_domains: GHS-R/MTLR. (IPR003905); GPCR_Rhodpsn. (IPR000276); GPCR_Rhodpsn_7TM.
    (IPR017452); 7tm_1 (PF00001)
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
  path: GHSR-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** F6QF00
- **Protein Description:** RecName: Full=Growth hormone secretagogue receptor type 1 {ECO:0000256|ARBA:ARBA00018726}; AltName: Full=GH-releasing peptide receptor {ECO:0000256|ARBA:ARBA00033151}; AltName: Full=Ghrelin receptor {ECO:0000256|ARBA:ARBA00032291};
- **Gene Information:** Name=GHSR {ECO:0000313|VGNC:VGNC:18336};
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Belongs to the G protein-coupled receptor 1 family.
- **Key Domains:** GHS-R/MTLR. (IPR003905); GPCR_Rhodpsn. (IPR000276); GPCR_Rhodpsn_7TM. (IPR017452); 7tm_1 (PF00001)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GHSR" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GHSR' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GHSR** (gene ID: GHSR, UniProt: F6QF00) in HORSE.

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
- **UniProt Accession:** F6QF00
- **Protein Description:** RecName: Full=Growth hormone secretagogue receptor type 1 {ECO:0000256|ARBA:ARBA00018726}; AltName: Full=GH-releasing peptide receptor {ECO:0000256|ARBA:ARBA00033151}; AltName: Full=Ghrelin receptor {ECO:0000256|ARBA:ARBA00032291};
- **Gene Information:** Name=GHSR {ECO:0000313|VGNC:VGNC:18336};
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Belongs to the G protein-coupled receptor 1 family.
- **Key Domains:** GHS-R/MTLR. (IPR003905); GPCR_Rhodpsn. (IPR000276); GPCR_Rhodpsn_7TM. (IPR017452); 7tm_1 (PF00001)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GHSR" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GHSR' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GHSR** (gene ID: GHSR, UniProt: F6QF00) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional Annotation Report: Equine GHSR (UniProt F6QF00)

## Executive summary

**Identity verification passed.** The supplied UniProt record identifies F6QF00 as *Equus caballus* **GHSR**, the growth hormone secretagogue receptor type 1, also called the ghrelin receptor or GH-releasing peptide receptor. The supplied GHS-R/MTLR, rhodopsin-like GPCR, and seven-transmembrane annotations are mutually consistent with mammalian GHSR1a. No conflicting horse gene with the symbol **GHSR** was found. Equine GHSR1a RT-PCR products from pituitary and adrenal medulla have additionally been sequence-verified against the horse reference genome, supporting the ortholog assignment independently of the supplied UniProt annotation (andrews2026preliminaryinvestigationof pages 1-2, andrews2026preliminaryinvestigationof pages 2-5).

The most defensible primary annotation is: **a plasma-membrane, class-A/rhodopsin-like seven-transmembrane signaling receptor activated by acylated ghrelin, which couples principally to Gαq/11 and transduces nutritional-state signals into neuroendocrine responses, especially pituitary growth-hormone secretion and hypothalamic appetite circuitry.** LEAP2 is the counter-regulatory endogenous antagonist/inverse agonist in other mammals. The molecular mechanism is strongly established for mammalian GHSR1a but has not yet been measured directly using recombinant horse F6QF00 (giorgioni2022advancesinthe pages 1-2, polishchuk2025beyondhungerthe pages 21-23).

Horse-specific evidence remains limited. Direct findings support GHSR1a transcript in pituitary and adrenal medulla, provisional expression in several peripheral tissues, and GHS-R1a-immunoreactive protein with receptor-associated pharmacology in cultured equine chondrocytes. Tissue-resolved cell-surface localization, ligand affinity, G-protein selectivity, constitutive activity, LEAP2 pharmacology, and receptor trafficking have not been demonstrated for F6QF00 itself (andrews2026preliminaryinvestigationof pages 5-6, andrews2026preliminaryinvestigationof pages 2-5, ceriotti2018theghrelinparadox pages 9-13).

## 1. Identity and nomenclature

The gene symbol **GHSR** matches the supplied protein description. In mammalian nomenclature, **GHSR1a** denotes the full-length, signaling-competent receptor, whereas **GHSR1b** is a truncated splice product. The authoritative pharmacology synthesis describes mammalian GHSR1a as a 366-amino-acid GPCR with high basal activity; it also notes that GHSR1b can associate with GHSR1a but is not itself the canonical signaling receptor (giorgioni2022advancesinthe pages 1-2).

The horse study published by Andrews and colleagues in July 2026 used isoform-targeted RT-PCR. Expected-size GHSR1a products from pituitary and adrenal medulla were sequenced and matched the equine reference sequence in NCBI assembly GCF_002863925.1. Bands of the expected size for GHSR1b occurred in some tissues, but low product yield prevented sequence confirmation; consequently, the existence and tissue distribution of an equine GHSR1b transcript remain provisional (andrews2026preliminaryinvestigationof pages 5-6, andrews2026preliminaryinvestigationof pages 2-5). Source: Andrews et al., *BMC Veterinary Research* 22:450, July 2026, https://doi.org/10.1186/s12917-026-05700-8.

**Important date qualification:** the 2026 study is later than the requested 2023–2024 priority window, but it is the newest and most directly relevant horse-specific receptor-expression study located. The 2023–2024 literature retrieved was dominated by non-equine mechanistic or physiological work; it does not replace direct characterization of F6QF00.

## 2. Protein class, topology, and cellular location

F6QF00 belongs to the G-protein-coupled receptor 1/class-A rhodopsin-like family. Its GHS-R/MTLR, GPCR_Rhodopsn, GPCR_Rhodopsn_7TM, and Pfam 7tm_1 annotations predict an integral membrane receptor with seven α-helical transmembrane segments, an extracellular ligand-accessible pocket, and cytoplasmic surfaces that engage heterotrimeric G proteins and arrestins. This architecture agrees with structural and pharmacological descriptions of mammalian GHSR1a as a seven-transmembrane receptor (giorgioni2022advancesinthe pages 1-2, polishchuk2025beyondhungerthe pages 21-23).

The principal functional location is therefore the **plasma membrane**. Following agonist activation, mammalian GHSR1a can recruit β-arrestin and internalize into intracellular compartments; β-arrestin also scaffolds ERK1/2 and AKT signaling. This trafficking model is a strong orthology-based inference for horse F6QF00, not a horse-specific observation (polishchuk2025beyondhungerthe pages 21-23).

In horses, available experiments establish transcript or immunoreactive protein production but generally do not resolve the receptor to particular cell types or demonstrate surface localization. Sequence-confirmed transcript was found in pituitary and adrenal medulla. GHSR1a-sized PCR products were also observed in duodenum, ileum, kidney, digital lamellae, liver, and pancreas, but most peripheral products were not sequence-confirmed; stomach-pylorus and adrenal-cortex findings were inconsistent (andrews2026preliminaryinvestigationof pages 2-5). Thus, pituitary and adrenal medulla have the strongest tissue-level transcript evidence, while the broader peripheral distribution should be treated as preliminary.

## 3. Primary molecular function and ligand specificity

### 3.1 Agonist

GHSR is a signaling receptor rather than an enzyme or transporter. Its endogenous agonist is **acylated ghrelin**. In the canonical mammalian pathway, ghrelin O-acyltransferase modifies ghrelin at Ser3; only the acylated form efficiently activates classical GHSR1a. Des-acyl ghrelin can have biological effects, but those effects should not automatically be assigned to GHSR1a (andrews2026preliminaryinvestigationof pages 1-2, giorgioni2022advancesinthe pages 1-2).

The acyl group is part of the receptor-recognition determinant. Structural/pharmacological synthesis indicates that the N-terminal ghrelin segment containing acyl-Ser3 is sufficient for receptor activation and that ligand contacts occupy a bifurcated GHSR binding pocket. Acylation position and chain properties influence activity (polishchuk2025beyondhungerthe pages 19-21, polishchuk2025beyondhungerthe pages 21-23).

A potentially important equine distinction is that horse ghrelin has been reported to carry predominantly a **C4 acyl modification**, rather than the canonical C8 modification emphasized in human and rodent work. This may affect immunoassay recognition and could alter equine receptor pharmacology; however, no direct affinity or efficacy comparison of C4- versus C8-ghrelin at recombinant F6QF00 was found (andrews2026preliminaryinvestigationof pages 6-8).

### 3.2 Endogenous inhibitor

In other mammals, **LEAP2** acts both as an endogenous GHSR antagonist and as an inverse agonist that reduces ligand-independent receptor activity. LEAP2 and its N-terminal region inhibit ghrelin-evoked Ca²⁺ and inositol-phosphate signaling, and LEAP2 administration suppresses ghrelin-induced feeding in rodent models (giorgioni2022advancesinthe pages 1-2). No equine LEAP2–F6QF00 binding or functional assay was located; assigning this regulation to horse GHSR is therefore a strong conserved-mechanism hypothesis, not direct species-specific evidence.

### 3.3 Constitutive activity

Mammalian GHSR1a has unusually high ligand-independent activity—approximately **50% of the maximal ghrelin response** in commonly used signaling assays. This makes the distinction among neutral antagonists, inverse agonists, and agonists biologically important (giorgioni2022advancesinthe pages 1-2). Direct constitutive-activity measurements for horse F6QF00 are absent.

## 4. Signaling mechanism and pathways

The best-supported canonical sequence is:

1. Acyl-ghrelin binds plasma-membrane GHSR1a.
2. GHSR1a principally activates **Gαq/11**.
3. Gαq/11 activates phospholipase C, generating IP3 and diacylglycerol.
4. IP3 mobilizes intracellular Ca²⁺, while downstream signaling engages PKC, CaMKII, AMPK, and cell-specific secretory or transcriptional responses.
5. GHSR1a can additionally recruit **Gαi/o, Gα13, and β-arrestin**, producing context-dependent PI3K–AKT, ERK1/2, ion-channel, cytoskeletal, and trafficking outputs (giorgioni2022advancesinthe pages 1-2, polishchuk2025beyondhungerthe pages 21-23).

Ghrelin recruits Gαq, Gαi/o, and β-arrestin in mammalian systems, but not Gαs in the canonical receptor configuration. Ligand concentration, exposure time, cell background, receptor abundance, and heteromeric partners can alter the apparent signaling profile. Consequently, pathway assignments from heterologous overexpression systems cannot be transferred quantitatively to horse pituitary, adrenal, or cartilage cells without validation (gonzalez2020dopaminereceptortype pages 19-21, polishchuk2025beyondhungerthe pages 21-23).

Mammalian GHSR1a also forms homo- and heteromeric complexes. Reported partners include GHSR1b, dopamine D1 and D2 receptors, 5-HT2C, somatostatin SST5, orexin OX1, melanocortin MC3, and cannabinoid CB2 receptors. Such interactions can change trafficking or pathway selection, but none has been established for endogenous equine F6QF00 (giorgioni2022advancesinthe pages 1-2). A D2R–GHSR study confirmed interaction and altered CaV2.2 regulation in engineered cellular/neuronal systems, while also illustrating the interpretive limitation that receptor expression depends strongly on transfected DNA dosage (gonzalez2020dopaminereceptortype pages 19-21).

## 5. Biological processes

### Growth-hormone axis

The receptor’s defining endocrine function is to transduce acyl-ghrelin and synthetic GH-secretagogue signals in pituitary somatotrophs, promoting growth-hormone release. Sequence-confirmed GHSR1a transcript in horse pituitary makes this the strongest functional annotation for F6QF00, although direct experiments linking equine receptor occupancy to GH release were not found in the retrieved full-text evidence (andrews2026preliminaryinvestigationof pages 1-2, andrews2026preliminaryinvestigationof pages 5-6, giorgioni2022advancesinthe pages 1-2).

### Appetite and energy-state signaling

In mammals, ghrelin activates GHSR1a on arcuate hypothalamic NPY/AgRP neurons, increasing neuronal activity and food seeking. LEAP2 counter-regulates this axis. GHSR activity also contributes to reward-related feeding through mesolimbic circuitry. These are authoritative mammalian functions, but receptor localization to equine hypothalamic appetite neurons has not yet been demonstrated (giorgioni2022advancesinthe pages 1-2).

Horse circulating-ligand data are directionally compatible with a nutritional-state signal. In 35 metabolically healthy horses and ponies, median active ghrelin decreased from **13.9 pg/mL before feeding to 12.2 pg/mL two hours afterward**, a **19% reduction** (p=0.001); pre- and post-prandial values correlated at r=0.56 (p<0.001). Welsh ponies had higher pre-prandial concentrations than other breed groups (p=0.0003), while bodyweight, height, and body-condition score were not associated with active ghrelin in this cohort (andrews2026preliminaryinvestigationof pages 1-2, andrews2026preliminaryinvestigationof pages 2-5). These measurements characterize ligand availability, not receptor activation or appetite causality.

### Peripheral and cellular functions

The clearest direct peripheral functional evidence comes from primary equine chondrocytes. GHS-R1a-immunoreactive protein was detected by Western blot across early culture passages. After challenge with 100 ng/mL lipopolysaccharide, **10⁻⁷ M acyl-ghrelin** reduced cytotoxicity, and the protection was abolished by **10⁻⁶ M D-Lys3-GHRP-6**, used as a GHS-R1a antagonist. In contrast, **10⁻¹¹ M ghrelin** worsened injury, and des-acyl ghrelin did not protect. The study used cartilage from six joints of six adult horses (ceriotti2018theghrelinparadox pages 9-13, ceriotti2018theghrelinparadox pages 1-6, ceriotti2018theghrelinparadox pages 6-9). Source: Ceriotti et al., *Peptides* 103:1–9, May 2018, https://doi.org/10.1016/j.peptides.2018.03.003.

This experiment supports receptor-associated, concentration-dependent signaling in equine cartilage cells, but it does not identify the downstream pathway. Interpretation should remain cautious because antibody specificity and the pharmacological selectivity of D-Lys3-GHRP-6 are less definitive than receptor knockout, sequence-verified proteomics, or rescue with recombinant equine GHSR.

## 6. Recent developments, 2023–2024

The major 2023–2024 advances found were in the broader mammalian ghrelin–GHSR system rather than horse F6QF00.

* A 2023 mouse study linked prolonged ghrelin elevation to enhanced GHSR internalization, β-arrestin-associated desensitization, and hippocampal ghrelin resistance in an Alzheimer-related model. This reinforces that chronic agonist exposure can reduce receptor responsiveness rather than simply increase signaling; it is not evidence of the same process in horses.
* A 2024 rodent study found that LEAP2 reduced bodyweight and adiposity and increased energy expenditure and adipose thermogenic programs under some conditions, but effects were not maintained under high-fat feeding or thermoneutrality and were only partial in aged animals. This context dependence argues against treating GHSR antagonism as a universally effective metabolic intervention.
* A 2024 rat study reported that intracerebroventricular LEAP2 at 1–3 nmol suppressed ghrelin-induced feeding under freely fed conditions but not under time-restricted feeding, again emphasizing dependence on nutritional context.

These developments refine the current model: GHSR output depends on the balance among acyl-ghrelin, LEAP2, constitutive receptor activity, exposure history, and physiological state. They do not establish equine potency, dosage, safety, or clinical utility.

## 7. Applications and real-world relevance

### Equine research and veterinary relevance

Potential applications include investigation of appetite regulation, growth-hormone physiology, insulin dysregulation/equine metabolic syndrome, critical-illness metabolism, gastrointestinal function, and cartilage inflammation. At present, these are research directions rather than validated GHSR-targeted equine treatments. The preliminary finding of breed- and age-associated differences in active ghrelin requires replication in larger, prospectively phenotyped cohorts before use as a biomarker (andrews2026preliminaryinvestigationof pages 1-2, andrews2026preliminaryinvestigationof pages 2-5).

The chondrocyte findings suggest that receptor agonism might modulate inflammatory cartilage injury, but the biphasic concentration response—protection at 10⁻⁷ M and harm at 10⁻¹¹ M—argues against straightforward therapeutic extrapolation (ceriotti2018theghrelinparadox pages 9-13, ceriotti2018theghrelinparadox pages 1-6).

### Translational pharmacology

GHSR is pharmacologically tractable. Development programs include peptide and nonpeptide agonists, antagonists, inverse agonists, biased ligands, and imaging ligands. Proposed indications include cachexia, impaired gastric motility, obesity, binge eating, metabolic disease, and alcohol-use disorder. The 2022 medicinal-chemistry perspective emphasizes that structural information and signaling bias may allow desired effects to be separated from adverse pathway activation (giorgioni2022advancesinthe pages 1-2, giorgioni2022advancesinthe pages 16-17). Source: Giorgioni et al., *Journal of Medicinal Chemistry* 65:3098–3118, published February 14, 2022, https://doi.org/10.1021/acs.jmedchem.1c02191.

These human/rodent applications should not be represented as real-world implementations in horses. No approved equine GHSR-targeted drug, validated dosing regimen, or controlled equine clinical trial was identified in the retrieved evidence.

## 8. Evidence grading

The following table separates direct horse observations from conserved mammalian inference.

| Claim/domain | Horse-specific evidence | Conserved mammalian inference | Confidence |
|---|---|---|---|
| **Identity and architecture** | UniProt **F6QF00** is supplied as *Equus caballus* **GHSR**, the growth hormone secretagogue/ghrelin receptor type 1. Its GHS-R/MTLR and rhodopsin-like 7TM domain annotations are internally consistent with this identity. | Mammalian GHSR1a is a 366-aa, class-A/rhodopsin-like seven-transmembrane GPCR, strongly supporting the supplied horse annotation (giorgioni2022advancesinthe pages 1-2, polishchuk2025beyondhungerthe pages 21-23). | **High** for ortholog identity and topology; direct characterization of F6QF00 is limited. |
| **Pituitary and adrenal expression** | Equine GHSR1a RT-PCR products from pituitary and adrenal medulla had the expected size and were sequence-confirmed against the horse reference genome (andrews2026preliminaryinvestigationof pages 1-2, andrews2026preliminaryinvestigationof pages 2-5). This July 2026 study falls beyond the requested 2023–2024 priority window but is the latest species-specific source located. | Pituitary expression accords with the conserved role of GHSR1a in ghrelin-stimulated growth-hormone release (giorgioni2022advancesinthe pages 1-2). | **High** for transcript presence; **moderate** for functional protein because cell type and signaling were not tested. |
| **Peripheral tissue distribution** | GHSR1a-sized products were detected in duodenum, ileum, kidney, digital lamellae, liver and pancreas; stomach pylorus and adrenal-cortex results were inconsistent. Most peripheral products were not sequence-confirmed because RNA or product yields were low (andrews2026preliminaryinvestigationof pages 2-5). | Mammalian GHSR is reported in several peripheral tissues, although expression may be low and heterogeneous (giorgioni2022advancesinthe pages 1-2). | **Low–moderate**; provisional transcript evidence. |
| **Possible GHSR1b splice form** | Expected-size GHSR1b bands appeared inconsistently in pituitary, adrenal medulla, adrenal cortex and ileum, but low yield prevented sequence confirmation (andrews2026preliminaryinvestigationof pages 5-6, andrews2026preliminaryinvestigationof pages 2-5). | Mammalian GHSR1b is a truncated, signaling-inactive splice product that can heteromerize with GHSR1a (giorgioni2022advancesinthe pages 1-2). | **Low** for equine GHSR1b identity and function. |
| **Equine chondrocyte protein and activity** | Western blot detected GHS-R1a-immunoreactive protein in primary equine chondrocytes. Acyl-ghrelin at 10^-7 M protected cells against 100 ng/mL LPS injury, and 10^-6 M D-Lys3-GHRP-6 abolished protection; 10^-11 M ghrelin worsened injury. Cartilage came from six adult horses (ceriotti2018theghrelinparadox pages 9-13, ceriotti2018theghrelinparadox pages 1-6, ceriotti2018theghrelinparadox pages 6-9). | The results are compatible with concentration-dependent GHSR signaling, although antibody specificity and antagonist selectivity constrain interpretation. | **Moderate** for receptor-associated activity; **low–moderate** for the precise mechanism. |
| **Ligand specificity** | Equine chondrocyte experiments found no protection from des-acyl ghrelin. Equine ghrelin may predominantly carry a C4 rather than canonical C8 acyl group, creating assay and species-pharmacology questions (andrews2026preliminaryinvestigationof pages 6-8, ceriotti2018theghrelinparadox pages 9-13, andrews2026preliminaryinvestigationof pages 1-2). | Mammalian ghrelin requires Ser3 acylation by GOAT to activate GHSR1a; des-acyl ghrelin does not activate classical GHSR1a (giorgioni2022advancesinthe pages 1-2, polishchuk2025beyondhungerthe pages 21-23). | **High** for general acylation dependence; **moderate** for exact equine acyl-chain specificity. |
| **Post-prandial active ghrelin** | In 35 metabolically healthy horses and ponies, median active ghrelin declined from **13.9 pg/mL** before feeding to **12.2 pg/mL** two hours later, a **19% reduction** (p = 0.001). Paired values correlated at r = 0.56 (p < 0.001), and Welsh ponies had higher baseline concentrations (p = 0.0003) (andrews2026preliminaryinvestigationof pages 1-2, andrews2026preliminaryinvestigationof pages 2-5). This evidence was published in 2026, beyond the requested priority window. | Post-prandial suppression is consistent with ghrelin functioning as a nutritional-state signal, but circulating ligand levels do not prove receptor activation in a particular tissue. | **High** for the studied cohort; **low–moderate** for generalization or causal GHSR physiology. |
| **Primary molecular mechanism** | Direct signaling measurements have not been reported for horse F6QF00. | Mammalian GHSR1a primarily couples to Gαq/11–PLC–IP3–intracellular Ca2+, with PKC, CaMKII and AMPK outputs. It can also recruit Gαi/o, Gα13 and β-arrestin, supporting ERK/AKT signaling and receptor internalization (giorgioni2022advancesinthe pages 1-2, polishchuk2025beyondhungerthe pages 21-23). | **High** as a conserved mammalian mechanism; **moderate** when transferred to horse F6QF00. |
| **Constitutive signaling and LEAP2** | No direct horse assay of ligand-independent activity, LEAP2 pharmacology, desensitization or internalization was located. | Mammalian GHSR1a has high basal activity, approximately **50% of the maximal ghrelin response**. LEAP2 is an endogenous antagonist and inverse agonist that suppresses ghrelin-evoked and constitutive signaling (giorgioni2022advancesinthe pages 1-2). | **High** for mammalian GHSR1a; **unverified in horse**. |
| **Cellular localization** | Transcript or protein evidence supports receptor production in pituitary, adrenal medulla and cultured chondrocytes, but no horse study directly mapped GHSR1a to specific cell types or demonstrated surface localization (andrews2026preliminaryinvestigationof pages 5-6, ceriotti2018theghrelinparadox pages 9-13). | Seven-transmembrane architecture and mammalian evidence imply principal action at the **plasma membrane**, followed by β-arrestin-associated internalization after activation (polishchuk2025beyondhungerthe pages 21-23). | **High** for membrane-receptor inference; **low–moderate** for tissue-resolved equine localization. |
| **Primary functional annotation** | Horse evidence supports a ghrelin-responsive receptor in endocrine and peripheral tissues, but direct equine appetite-neuron, growth-hormone-release or knockout evidence is absent. | Best-supported annotation: an acyl-ghrelin-activated signaling GPCR that transduces nutritional-state information to pituitary growth-hormone secretion and hypothalamic NPY/AgRP appetite circuits, with LEAP2 providing counter-regulation (giorgioni2022advancesinthe pages 1-2). | **Moderate–high** by orthology; **moderate** as an experimentally demonstrated horse function. |
| **Major gaps** | No recombinant F6QF00 ligand-binding assay, sequence-resolved isoform analysis, equine G-protein coupling profile, surface-localization microscopy, LEAP2 assay, constitutive-activity measurement, receptor knockout or rigorous tissue-wide protein atlas was found. Most horse evidence predates 2023 or derives from the later 2026 preliminary study (andrews2026preliminaryinvestigationof pages 5-6, andrews2026preliminaryinvestigationof pages 8-9, ceriotti2018theghrelinparadox pages 9-13). | Mammalian pharmacology provides a strong hypothesis framework but cannot establish horse-specific potency, signaling bias, acyl-chain preference, heteromerization or physiological effect size. | **High** confidence that these are unresolved evidence gaps. |


*Table: Evidence-grading summary for functional annotation of equine GHSR/F6QF00, separating direct horse findings from conserved mammalian inference. It highlights the latest species-specific evidence, its date limitations, and major unresolved questions.*

## 9. Recommended annotation and research priorities

### Recommended functional annotation

> **Equine GHSR/F6QF00 is a predicted class-A, rhodopsin-like seven-transmembrane plasma-membrane GPCR and ortholog of mammalian GHSR1a. It is expected to bind acylated ghrelin and activate predominantly Gαq/11-dependent PLC–IP3–Ca²⁺ signaling, thereby regulating pituitary growth-hormone release and hypothalamic appetite/energy-state pathways. Mammalian evidence further predicts high constitutive activity, inhibition by LEAP2, β-arrestin-dependent internalization, and context-dependent coupling to Gi/o, G13, ERK, and AKT pathways. In horses, GHSR1a transcript has been sequence-confirmed in pituitary and adrenal medulla, while receptor-associated responses have been reported in cultured chondrocytes; detailed F6QF00 pharmacology remains unverified.**

### Highest-priority experiments

1. Express sequence-verified F6QF00 in a controlled cell system and compare equine C4-acyl ghrelin, canonical C8-ghrelin, des-acyl ghrelin, LEAP2, and synthetic secretagogues in binding, Ca²⁺, IP1, G-protein, and β-arrestin assays.
2. Quantify ligand-independent activity and distinguish neutral antagonism from inverse agonism.
3. Confirm endogenous protein by targeted mass spectrometry and validated antibodies, followed by cell-type-resolved localization in pituitary, hypothalamus, adrenal medulla, intestine, pancreas, digital lamellae, and cartilage.
4. Sequence and functionally test the putative equine GHSR1b splice form.
5. Link receptor activation to GH secretion in primary equine pituitary cells and to appetite/metabolic outcomes in controlled in-vivo studies.
6. Test whether observed cartilage effects survive receptor knockdown or CRISPR disruption, which would be more decisive than antagonist blockade alone.

## Conclusion

The symbol **GHSR**, organism **horse**, protein description, and rhodopsin-like 7TM domains all align; there is no indication that F6QF00 represents a different same-symbol protein. The strongest annotation is an acyl-ghrelin-responsive neuroendocrine GPCR acting at the cell surface. Nevertheless, the precise ligand preference, signaling bias, constitutive activity, LEAP2 sensitivity, and trafficking of horse F6QF00 remain inferred from mammalian orthologs. Direct equine evidence presently supports pituitary and adrenal-medulla transcription, provisional wider tissue expression, and receptor-associated signaling in chondrocytes—not a complete molecular characterization.

References

1. (andrews2026preliminaryinvestigationof pages 1-2): Kate E. Andrews, Hayden L. Smith, Robert J. Spence, Martin N. Sillence, and Melody A. de Laat. Preliminary investigation of ghrelin in horses and ponies: receptor expression and associations with prandial state, morphometry and signalment. Jul 2026. URL: https://doi.org/10.1186/s12917-026-05700-8, doi:10.1186/s12917-026-05700-8. This article has 0 citations and is from a peer-reviewed journal.

2. (andrews2026preliminaryinvestigationof pages 2-5): Kate E. Andrews, Hayden L. Smith, Robert J. Spence, Martin N. Sillence, and Melody A. de Laat. Preliminary investigation of ghrelin in horses and ponies: receptor expression and associations with prandial state, morphometry and signalment. Jul 2026. URL: https://doi.org/10.1186/s12917-026-05700-8, doi:10.1186/s12917-026-05700-8. This article has 0 citations and is from a peer-reviewed journal.

3. (giorgioni2022advancesinthe pages 1-2): Gianfabio Giorgioni, Fabio Del Bello, Wilma Quaglia, Luca Botticelli, Carlo Cifani, E. Micioni Di Bonaventura, M. V. Micioni Di Bonaventura, and Alessandro Piergentili. Advances in the development of nonpeptide small molecules targeting ghrelin receptor. Journal of Medicinal Chemistry, 65:3098-3118, Feb 2022. URL: https://doi.org/10.1021/acs.jmedchem.1c02191, doi:10.1021/acs.jmedchem.1c02191. This article has 29 citations and is from a highest quality peer-reviewed journal.

4. (polishchuk2025beyondhungerthe pages 21-23): Hlafira Polishchuk, Krzysztof Guzik, and Tomasz Kantyka. Beyond hunger: the structure, signaling, and systemic roles of ghrelin. International Journal of Molecular Sciences, Nov 2025. URL: https://doi.org/10.3390/ijms262210996, doi:10.3390/ijms262210996. This article has 12 citations.

5. (andrews2026preliminaryinvestigationof pages 5-6): Kate E. Andrews, Hayden L. Smith, Robert J. Spence, Martin N. Sillence, and Melody A. de Laat. Preliminary investigation of ghrelin in horses and ponies: receptor expression and associations with prandial state, morphometry and signalment. Jul 2026. URL: https://doi.org/10.1186/s12917-026-05700-8, doi:10.1186/s12917-026-05700-8. This article has 0 citations and is from a peer-reviewed journal.

6. (ceriotti2018theghrelinparadox pages 9-13): Serena Ceriotti, Anna Lange Consiglio, Lavinia Casati, Fausto Cremonesi, Valeria Sibilia, and Francesco Ferrucci. The ghrelin paradox in the control of equine chondrocyte function: the good and the bad. Peptides, 103:1-9, May 2018. URL: https://doi.org/10.1016/j.peptides.2018.03.003, doi:10.1016/j.peptides.2018.03.003. This article has 7 citations and is from a peer-reviewed journal.

7. (polishchuk2025beyondhungerthe pages 19-21): Hlafira Polishchuk, Krzysztof Guzik, and Tomasz Kantyka. Beyond hunger: the structure, signaling, and systemic roles of ghrelin. International Journal of Molecular Sciences, Nov 2025. URL: https://doi.org/10.3390/ijms262210996, doi:10.3390/ijms262210996. This article has 12 citations.

8. (andrews2026preliminaryinvestigationof pages 6-8): Kate E. Andrews, Hayden L. Smith, Robert J. Spence, Martin N. Sillence, and Melody A. de Laat. Preliminary investigation of ghrelin in horses and ponies: receptor expression and associations with prandial state, morphometry and signalment. Jul 2026. URL: https://doi.org/10.1186/s12917-026-05700-8, doi:10.1186/s12917-026-05700-8. This article has 0 citations and is from a peer-reviewed journal.

9. (gonzalez2020dopaminereceptortype pages 19-21): Santiago Cordisco Gonzalez, Emilio Román Mustafá, Silvia S. Rodriguez, Mario Perello, and Jesica Raingo. Dopamine receptor type 2 and ghrelin receptor coexpression alters ca<sub>v</sub>2.2 modulation by g protein signaling cascades. ACS Chemical Neuroscience, 11(1):3-13, Dec 2020. URL: https://doi.org/10.1021/acschemneuro.9b00426, doi:10.1021/acschemneuro.9b00426. This article has 24 citations and is from a peer-reviewed journal.

10. (ceriotti2018theghrelinparadox pages 1-6): Serena Ceriotti, Anna Lange Consiglio, Lavinia Casati, Fausto Cremonesi, Valeria Sibilia, and Francesco Ferrucci. The ghrelin paradox in the control of equine chondrocyte function: the good and the bad. Peptides, 103:1-9, May 2018. URL: https://doi.org/10.1016/j.peptides.2018.03.003, doi:10.1016/j.peptides.2018.03.003. This article has 7 citations and is from a peer-reviewed journal.

11. (ceriotti2018theghrelinparadox pages 6-9): Serena Ceriotti, Anna Lange Consiglio, Lavinia Casati, Fausto Cremonesi, Valeria Sibilia, and Francesco Ferrucci. The ghrelin paradox in the control of equine chondrocyte function: the good and the bad. Peptides, 103:1-9, May 2018. URL: https://doi.org/10.1016/j.peptides.2018.03.003, doi:10.1016/j.peptides.2018.03.003. This article has 7 citations and is from a peer-reviewed journal.

12. (giorgioni2022advancesinthe pages 16-17): Gianfabio Giorgioni, Fabio Del Bello, Wilma Quaglia, Luca Botticelli, Carlo Cifani, E. Micioni Di Bonaventura, M. V. Micioni Di Bonaventura, and Alessandro Piergentili. Advances in the development of nonpeptide small molecules targeting ghrelin receptor. Journal of Medicinal Chemistry, 65:3098-3118, Feb 2022. URL: https://doi.org/10.1021/acs.jmedchem.1c02191, doi:10.1021/acs.jmedchem.1c02191. This article has 29 citations and is from a highest quality peer-reviewed journal.

13. (andrews2026preliminaryinvestigationof pages 8-9): Kate E. Andrews, Hayden L. Smith, Robert J. Spence, Martin N. Sillence, and Melody A. de Laat. Preliminary investigation of ghrelin in horses and ponies: receptor expression and associations with prandial state, morphometry and signalment. Jul 2026. URL: https://doi.org/10.1186/s12917-026-05700-8, doi:10.1186/s12917-026-05700-8. This article has 0 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](GHSR-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. giorgioni2022advancesinthe pages 1-2
2. polishchuk2025beyondhungerthe pages 21-23
3. andrews2026preliminaryinvestigationof pages 2-5
4. andrews2026preliminaryinvestigationof pages 6-8
5. gonzalez2020dopaminereceptortype pages 19-21
6. andrews2026preliminaryinvestigationof pages 1-2
7. andrews2026preliminaryinvestigationof pages 5-6
8. ceriotti2018theghrelinparadox pages 9-13
9. polishchuk2025beyondhungerthe pages 19-21
10. ceriotti2018theghrelinparadox pages 1-6
11. ceriotti2018theghrelinparadox pages 6-9
12. giorgioni2022advancesinthe pages 16-17
13. andrews2026preliminaryinvestigationof pages 8-9
14. https://doi.org/10.1186/s12917-026-05700-8.
15. https://doi.org/10.1016/j.peptides.2018.03.003.
16. https://doi.org/10.1021/acs.jmedchem.1c02191.
17. https://doi.org/10.1186/s12917-026-05700-8,
18. https://doi.org/10.1021/acs.jmedchem.1c02191,
19. https://doi.org/10.3390/ijms262210996,
20. https://doi.org/10.1016/j.peptides.2018.03.003,
21. https://doi.org/10.1021/acschemneuro.9b00426,