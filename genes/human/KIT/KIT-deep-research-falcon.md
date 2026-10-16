---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-25T04:07:03.465579'
end_time: '2026-09-25T04:14:32.079415'
duration_seconds: 448.61
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: KIT
  gene_symbol: KIT
  uniprot_accession: P10721
  protein_description: 'RecName: Full=Mast/stem cell growth factor receptor Kit; Short=SCFR;
    EC=2.7.10.1; AltName: Full=Piebald trait protein; Short=PBT; AltName: Full=Proto-oncogene
    c-Kit; AltName: Full=Tyrosine-protein kinase Kit; AltName: Full=p145 c-kit; AltName:
    Full=v-kit Hardy-Zuckerman 4 feline sarcoma viral oncogene homolog; AltName: CD_antigen=CD117;
    Flags: Precursor;'
  gene_info: Name=KIT; Synonyms=SCFR;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the protein kinase superfamily. Tyr protein
  protein_domains: Ig-like_dom. (IPR007110); Ig-like_dom_sf. (IPR036179); Ig-like_fold.
    (IPR013783); Ig_sub. (IPR003599); Ig_sub2. (IPR003598)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 43
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: KIT-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** P10721
- **Protein Description:** RecName: Full=Mast/stem cell growth factor receptor Kit; Short=SCFR; EC=2.7.10.1; AltName: Full=Piebald trait protein; Short=PBT; AltName: Full=Proto-oncogene c-Kit; AltName: Full=Tyrosine-protein kinase Kit; AltName: Full=p145 c-kit; AltName: Full=v-kit Hardy-Zuckerman 4 feline sarcoma viral oncogene homolog; AltName: CD_antigen=CD117; Flags: Precursor;
- **Gene Information:** Name=KIT; Synonyms=SCFR;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the protein kinase superfamily. Tyr protein
- **Key Domains:** Ig-like_dom. (IPR007110); Ig-like_dom_sf. (IPR036179); Ig-like_fold. (IPR013783); Ig_sub. (IPR003599); Ig_sub2. (IPR003598)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "KIT" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'KIT' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **KIT** (gene ID: KIT, UniProt: P10721) in human.

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
- **UniProt Accession:** P10721
- **Protein Description:** RecName: Full=Mast/stem cell growth factor receptor Kit; Short=SCFR; EC=2.7.10.1; AltName: Full=Piebald trait protein; Short=PBT; AltName: Full=Proto-oncogene c-Kit; AltName: Full=Tyrosine-protein kinase Kit; AltName: Full=p145 c-kit; AltName: Full=v-kit Hardy-Zuckerman 4 feline sarcoma viral oncogene homolog; AltName: CD_antigen=CD117; Flags: Precursor;
- **Gene Information:** Name=KIT; Synonyms=SCFR;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the protein kinase superfamily. Tyr protein
- **Key Domains:** Ig-like_dom. (IPR007110); Ig-like_dom_sf. (IPR036179); Ig-like_fold. (IPR013783); Ig_sub. (IPR003599); Ig_sub2. (IPR003598)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "KIT" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'KIT' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **KIT** (gene ID: KIT, UniProt: P10721) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Human KIT (UniProt P10721): Functional-Annotation Research Report

## Executive summary

The requested target is unambiguously **human KIT** (*KIT proto-oncogene, receptor tyrosine kinase*), not another similarly named gene. The supplied identity—**UniProt P10721**, SCFR/c-KIT/CD117, a precursor glycoprotein and tyrosine-protein kinase—is consistent with the literature. Human KIT is described as a **976-amino-acid, approximately 145-kDa type III single-pass receptor tyrosine kinase** with five extracellular immunoglobulin-like domains, one transmembrane helix, an inhibitory juxtamembrane segment, and a split cytoplasmic kinase domain. This architecture agrees with the supplied InterPro Ig-like-domain and kinase-family annotations (katagiri2022mutatedkittyrosine pages 1-2, roskoski2005signalingbykit pages 2-3, cilloni2024detectionofkit pages 2-3).

Its primary function is to receive extracellular **stem cell factor (SCF/KITLG)** signals at the plasma membrane and convert them into intracellular protein-tyrosine phosphorylation. SCF-induced KIT dimerization enables reciprocal receptor phosphorylation and recruitment of effectors controlling survival, proliferation, differentiation, adhesion, chemotaxis, and migration. KIT is particularly important in hematopoietic progenitors and mast cells, melanocytes, germ cells, and gastrointestinal interstitial cells of Cajal. Loss of KIT signaling causes developmental phenotypes such as piebaldism, whereas constitutive activation drives GIST, mastocytosis, and subsets of AML and other cancers (OpenTargets Search: -KIT, krimmer2023cryoemanalysesof pages 1-2, roskoski2005signalingbykit pages 1-2, cilloni2024detectionofkit pages 3-5).

| Category | Evidence-based annotation | Key evidence/source |
|---|---|---|
| Identity, aliases, organism | **Human KIT proto-oncogene receptor tyrosine kinase**, corresponding to **UniProt P10721**; aliases include **SCFR, c-KIT, CD117**, and **p145 c-KIT**. The literature consistently identifies human KIT/CD117 as the stem-cell-factor receptor, so no symbol ambiguity was detected. | Cilloni et al., 2024, DOI: [10.3390/ijms252010885](https://doi.org/10.3390/ijms252010885); Roskoski, 2005, DOI: [10.1016/j.bbrc.2005.08.055](https://doi.org/10.1016/j.bbrc.2005.08.055) (cilloni2024detectionofkit pages 3-5, roskoski2005signalingbykit pages 2-3, cilloni2024detectionofkit pages 2-3) |
| Molecular class and architecture | A **type III single-pass receptor tyrosine kinase** and approximately **145-kDa glycoprotein** of **976 amino acids**. It contains five extracellular immunoglobulin-like domains (D1–D5), one transmembrane helix, an autoinhibitory juxtamembrane segment, and a split cytoplasmic kinase domain interrupted by a kinase insert. This agrees with the supplied Ig-like-domain and protein-tyrosine-kinase annotations. | Cilloni et al., 2024, DOI: [10.3390/ijms252010885](https://doi.org/10.3390/ijms252010885); Katagiri et al., 2022, DOI: [10.3390/ijms23094694](https://doi.org/10.3390/ijms23094694); Heldin and Lennartsson, 2013, DOI: [10.1101/cshperspect.a009100](https://doi.org/10.1101/cshperspect.a009100) (katagiri2022mutatedkittyrosine pages 1-2, cilloni2024detectionofkit pages 2-3, heldin2013structuralandfunctional pages 7-9) |
| Ligand and activation | The specific ligand is **stem cell factor (SCF/KITLG)**, which occurs in soluble and membrane-bound forms. One SCF homodimer binds two KIT molecules through D1–D3; D4–D4 and D5–D5 receptor contacts stabilize the dimer. Dimerization relieves juxtamembrane autoinhibition and enables reciprocal trans-autophosphorylation. | Heldin and Lennartsson, 2013, DOI: [10.1101/cshperspect.a009100](https://doi.org/10.1101/cshperspect.a009100); Roskoski, 2005, DOI: [10.1016/j.bbrc.2005.08.055](https://doi.org/10.1016/j.bbrc.2005.08.055); Krimmer et al., 2023, DOI: [10.1073/pnas.2300054120](https://doi.org/10.1073/pnas.2300054120) (roskoski2005signalingbykit pages 1-2, roskoski2005signalingbykit pages 2-3, krimmer2023cryoemanalysesof pages 7-8, heldin2013structuralandfunctional pages 7-9) |
| Catalytic reaction and substrate specificity | KIT catalyzes ATP-dependent transfer of the gamma phosphate of ATP to protein tyrosine residues: **ATP + protein-L-tyrosine → ADP + protein-L-tyrosine phosphate**. Initial substrates are tyrosines on the paired KIT receptor; the resulting phosphotyrosines recruit signaling proteins. Documented docking sites include Y568/Y570, Y703, Y721, Y730, Y900, and Y936. | Roskoski, 2005, DOI: [10.1016/j.bbrc.2005.08.055](https://doi.org/10.1016/j.bbrc.2005.08.055); Rönnstrand, 2004, DOI: [10.1007/s00018-004-4189-6](https://doi.org/10.1007/s00018-004-4189-6) (r�nnstrand2004signaltransductionvia pages 1-2, roskoski2005signalingbykit pages 1-2, roskoski2005signalingbykit pages 2-3) |
| Localization and trafficking | Mature KIT functions primarily at the **plasma membrane**, with its ligand-binding region extracellular and kinase region cytosolic. SCF activation promotes internalization; KIT is generally not efficiently recycled but is ubiquitinated after Cbl recruitment and routed toward lysosomal and proteasomal degradation. Mutant GIST-associated KIT can show altered localization and impaired degradation. | Le Gall et al., 2015, DOI: [10.1158/1535-7163.MCT-15-0321](https://doi.org/10.1158/1535-7163.MCT-15-0321); Zhou et al., 2024, DOI: [10.1186/s12964-023-01411-x](https://doi.org/10.1186/s12964-023-01411-x) (gall2015neutralizationofkit pages 10-11, zhou2024kitmutationsand pages 1-2) |
| Major downstream pathways | Autophosphorylated KIT activates **RAS–RAF–MEK–ERK/MAPK, PI3K–AKT, PLCγ–PKC/Ca²⁺, SRC-family kinase**, and **JAK–STAT** signaling. These pathways principally control survival, proliferation, differentiation, adhesion, chemotaxis, and migration. | Roskoski, 2005, DOI: [10.1016/j.bbrc.2005.08.055](https://doi.org/10.1016/j.bbrc.2005.08.055); Cilloni et al., 2024, DOI: [10.3390/ijms252010885](https://doi.org/10.3390/ijms252010885) (roskoski2005signalingbykit pages 1-2, katagiri2022mutatedkittyrosine pages 1-2, cilloni2024detectionofkit pages 3-5) |
| Physiological cell types and functions | KIT is prominent in hematopoietic stem/progenitor cells and remains highly expressed by mast cells; expression is also documented in germ cells, melanocytes, interstitial cells of Cajal, NK cells, and dendritic cells. KIT–SCF signaling supports early hematopoiesis, mast-cell development and survival, melanogenesis, gametogenesis, and gastrointestinal pacemaker-cell development. | Krimmer et al., 2023, DOI: [10.1073/pnas.2300054120](https://doi.org/10.1073/pnas.2300054120); Cilloni et al., 2024, DOI: [10.3390/ijms252010885](https://doi.org/10.3390/ijms252010885); Katagiri et al., 2022, DOI: [10.3390/ijms23094694](https://doi.org/10.3390/ijms23094694) (krimmer2023cryoemanalysesof pages 1-2, katagiri2022mutatedkittyrosine pages 1-2, cilloni2024detectionofkit pages 3-5, pardanani2023systemicmastocytosisin pages 1-2) |
| Loss-of-function phenotypes | Reduced KIT signaling causes **piebaldism or hypopigmentation** through impaired melanocyte development and may produce mast-cell deficiency, anemia or other hematopoietic abnormalities, and impaired fertility. Severe experimental loss of KIT or SCF is lethal, whereas partial loss produces pigmentation and germ-cell phenotypes. | Rönnstrand, 2004, DOI: [10.1007/s00018-004-4189-6](https://doi.org/10.1007/s00018-004-4189-6); Roskoski, 2005, DOI: [10.1016/j.bbrc.2005.08.055](https://doi.org/10.1016/j.bbrc.2005.08.055); Open Targets evidence (OpenTargets Search: -KIT, r�nnstrand2004signaltransductionvia pages 1-2, roskoski2005signalingbykit pages 1-2) |
| Gain-of-function diseases | Ligand-independent KIT activation drives **GIST, systemic and cutaneous mastocytosis, mast-cell leukemia, subsets of AML, seminoma or germ-cell tumors**, and some melanomas. Primary KIT mutations occur in approximately **80–90% of treatment-naive GIST**, while KIT protein is detected in approximately **95%**. More than **90% of mastocytosis** cases have somatic KIT mutations, most commonly adult D816V; pediatric skin lesions show D816V in about **30%** and extracellular-domain activating variants in about **40%**. | Zhou et al., 2024, DOI: [10.1186/s12964-023-01411-x](https://doi.org/10.1186/s12964-023-01411-x); Cilloni et al., 2024, DOI: [10.3390/ijms252010885](https://doi.org/10.3390/ijms252010885) (cilloni2024detectionofkit pages 3-5, zhou2024kitmutationsand pages 1-2) |
| Current clinical applications | KIT is used as a **CD117 diagnostic marker**, molecular diagnostic and monitoring target, and drug target. KIT/PDGFRA genotyping guides GIST therapy with imatinib and later-line TKIs such as sunitinib, regorafenib, and ripretinib. In mastocytosis, D816V is generally imatinib-resistant, whereas avapritinib and midostaurin target advanced disease. One systemic-mastocytosis series reported an imatinib response rate of **18% (4/22)**, supporting its restricted use in selected non-D816V or unknown-genotype disease. | Pardanani, 2023, DOI: [10.1002/ajh.26962](https://doi.org/10.1002/ajh.26962); Zhou et al., 2024, DOI: [10.1186/s12964-023-01411-x](https://doi.org/10.1186/s12964-023-01411-x) (zhou2024kitmutationsand pages 1-2, pardanani2023systemicmastocytosisin pages 1-2, pardanani2023systemicmastocytosisin pages 16-16) |
| 2023–2024 advances | Cryo-EM revealed an asymmetric D5 interface with buried areas of approximately **292 Å²** in wild-type KIT, **479 Å²** in ligand-sensitized DupA502/Y503 KIT, and **1,001 Å²** in ligand-independent T417I/Δ418–419 KIT. The latter mutant's D5 termini were **4.8 Å** apart without SCF versus **15.0 Å** after SCF-induced remodeling; DupA502/Y503 D5 fragments showed **10–20-fold** stronger dimerization. These results identify D4/D5 contacts as therapeutic targets. A 2024 synthesis reported that approximately **90% of imatinib resistance in GIST** is associated with secondary KIT mutations and that resistance commonly emerges after **18–24 months**. | Krimmer et al., 2023, DOI: [10.1073/pnas.2300054120](https://doi.org/10.1073/pnas.2300054120); Zhou et al., 2024, DOI: [10.1186/s12964-023-01411-x](https://doi.org/10.1186/s12964-023-01411-x) (zhou2024kitmutationsand pages 1-2, krimmer2023cryoemanalysesof pages 7-8, krimmer2023cryoemanalysesof pages 1-2, krimmer2023cryoemanalysesof pages 8-10) |


*Table: Concise evidence-based annotation of human KIT (UniProt P10721), covering molecular mechanism, localization, physiology, disease associations, clinical use, and recent structural findings. Quantitative claims are linked to the supporting literature and available evidence contexts.*

## 1. Identity verification

### 1.1 Gene, protein, and organism

The literature identifies **KIT/CD117** as the human stem-cell-factor receptor, also called **SCFR** or **c-KIT**. It is encoded by *KIT* on chromosome 4 and belongs to the type III receptor tyrosine kinase family. The reported 976-residue, approximately 145-kDa glycoprotein is concordant with UniProt P10721 and the historical name p145 c-KIT (katagiri2022mutatedkittyrosine pages 1-2, roskoski2005signalingbykit pages 2-3, cilloni2024detectionofkit pages 2-3).

No conflicting same-symbol protein was encountered. The reviewed work concerns **Homo sapiens KIT**, except where experimental model phenotypes are explicitly used as supporting evidence. The related gene **KITLG** encodes the ligand and must not be confused with the receptor itself.

### 1.2 Domain verification

KIT has five extracellular immunoglobulin-like domains, conventionally designated **D1–D5**. D1–D3 form the principal SCF-binding region, while membrane-proximal D4 and D5 provide receptor–receptor contacts that stabilize and orient the signaling dimer. These are followed by a single transmembrane helix, a cytosolic juxtamembrane regulatory segment, and an intracellular tyrosine-kinase domain interrupted by a kinase insert—hence the characteristic “split kinase” architecture of class III receptors (katagiri2022mutatedkittyrosine pages 1-2, roskoski2005signalingbykit pages 2-3, krimmer2023cryoemanalysesof pages 7-8, heldin2013structuralandfunctional pages 7-9).

## 2. Primary molecular function

### 2.1 Ligand specificity

The physiological ligand is **SCF**, encoded by *KITLG* and also known as mast-cell growth factor or steel factor. SCF exists in membrane-bound and soluble forms and is a noncovalent homodimer. One SCF dimer engages two KIT molecules principally through D1–D3, bringing them together so that D4–D4 and D5–D5 contacts can complete the active receptor assembly (roskoski2005signalingbykit pages 1-2, roskoski2005signalingbykit pages 2-3, krimmer2023cryoemanalysesof pages 7-8, heldin2013structuralandfunctional pages 7-9).

This ligand specificity distinguishes KIT from related class III receptors such as PDGFRA/B, CSF1R, and FLT3. KIT is not a transporter or structural protein; it is a cell-surface signaling enzyme.

### 2.2 Catalytic reaction and substrate specificity

KIT is an ATP-dependent protein-tyrosine kinase (EC 2.7.10.1). Its net catalytic reaction can be represented as:

**ATP + protein-L-tyrosine → ADP + protein-L-tyrosine phosphate.**

Following dimerization, each KIT kinase phosphorylates tyrosines on the opposing receptor—reciprocal **trans-autophosphorylation**—and can subsequently phosphorylate associated signaling proteins. Thus, its substrate class is protein tyrosine residues rather than free tyrosine or a small-molecule metabolite. Autophosphorylation both increases catalytic activity and creates binding sites for proteins containing SH2 or phosphotyrosine-binding domains (r�nnstrand2004signaltransductionvia pages 1-2, roskoski2005signalingbykit pages 1-2, roskoski2005signalingbykit pages 2-3).

Important receptor phosphotyrosines include Y568/Y570, which recruit Src-family kinases, SHP proteins, SHC, and APS; Y703, associated with GRB2; Y721, a major PI3K-recruitment site; Y730, associated with PLCγ; and C-terminal sites Y900 and Y936, which recruit combinations of PI3K, CRK, GRB2, GRB7, and APS. These sites make KIT a phosphorylation-dependent signaling scaffold as well as an enzyme (roskoski2005signalingbykit pages 1-2).

### 2.3 Activation and autoinhibition

In inactive KIT, the juxtamembrane segment inserts between the kinase lobes and restrains catalytic activity. SCF-mediated dimerization permits intermolecular phosphorylation of this regulatory region and other receptor sites, relieving autoinhibition and stabilizing the active state (heldin2013structuralandfunctional pages 7-9).

Recent cryo-EM work refined this model. SCF organizes interactions across D1–D3, symmetric D4 contacts, and an asymmetric D5 interface that likely constrains the transmembrane and intracellular domains in a productive orientation. Mutation of D5-interface residues F504 or F506 reduced ligand-induced autophosphorylation, and combined R381A/F506A substitution abolished it, functionally connecting the extracellular interface to kinase activation (krimmer2023cryoemanalysesof pages 7-8).

## 3. Cellular localization and trafficking

Mature KIT operates primarily at the **plasma membrane**: its glycosylated Ig-like region faces the extracellular environment, the single transmembrane helix anchors the receptor, and the kinase domain lies in the cytosol. This topology allows extracellular SCF to control cytoplasmic phosphorylation without ligand transport across the membrane (katagiri2022mutatedkittyrosine pages 1-2, cilloni2024detectionofkit pages 2-3).

After activation, KIT is internalized. Phosphorylated receptor recruits the Cbl E3 ubiquitin ligase, undergoes ubiquitination, and is directed toward lysosomal and proteasomal degradation; it is generally not efficiently recycled to the cell surface. This trafficking provides negative feedback and limits signal duration. Oncogenic KIT can exhibit altered intracellular localization or impaired degradation, potentially prolonging signaling (gall2015neutralizationofkit pages 10-11, zhou2024kitmutationsand pages 1-2).

## 4. Signaling pathways

KIT autophosphorylation initiates several interacting pathways:

* **RAS–RAF–MEK–ERK/MAPK:** promotes transcriptional programs, proliferation, and differentiation.
* **PI3K–AKT:** supports survival, metabolism, and resistance to apoptosis; Y721 is an important receptor docking site.
* **PLCγ–PKC/Ca²⁺:** links KIT to phosphoinositide hydrolysis, calcium mobilization, and context-dependent proliferation.
* **SRC-family kinases:** participate in proliferation, survival, adhesion, cytoskeletal regulation, and migration.
* **JAK–STAT:** contributes to transcriptional responses and hematopoietic differentiation in appropriate cellular contexts (roskoski2005signalingbykit pages 1-2, katagiri2022mutatedkittyrosine pages 1-2, cilloni2024detectionofkit pages 3-5).

These pathways overlap with those of other growth-factor receptors. Biological specificity therefore arises not merely from which pathways are present, but from receptor abundance, phosphosite usage, signal amplitude and duration, membrane-bound versus soluble SCF, receptor isoform, and cell-specific effector expression. The alternatively spliced GNNK-negative KIT isoform reportedly phosphorylates and internalizes more rapidly and produces stronger downstream signaling than GNNK-positive KIT (r�nnstrand2004signaltransductionvia pages 1-2, cilloni2024detectionofkit pages 2-3).

## 5. Physiological functions and biological processes

### Hematopoiesis and mast cells

KIT is strongly expressed in early hematopoietic stem and progenitor populations and contributes to survival, self-renewal, and myeloid/lymphoid differentiation. Expression usually declines during maturation, but mast cells retain high surface KIT. SCF–KIT signaling is consequently central to mast-cell proliferation, maturation, adhesion, chemotaxis, and survival (katagiri2022mutatedkittyrosine pages 1-2, cilloni2024detectionofkit pages 3-5, pardanani2023systemicmastocytosisin pages 1-2).

### Melanocytes

KIT supports melanocyte development, migration, and survival. Human loss-of-function variants are associated with **piebaldism**, making pigmentation genetics strong in-vivo evidence for the receptor’s developmental role. Open Targets independently identifies a high-confidence KIT–piebaldism association (OpenTargets Search: -KIT, r�nnstrand2004signaltransductionvia pages 1-2).

### Germ cells and fertility

KIT signaling supports germ-cell development and both spermatogenic and oogenic processes. Severe or partial disruption of the KIT–SCF axis produces germ-cell depletion or infertility in experimental genetics, while human loss-of-function syndromes can include reproductive abnormalities (r�nnstrand2004signaltransductionvia pages 1-2, roskoski2005signalingbykit pages 1-2, cilloni2024detectionofkit pages 3-5).

### Interstitial cells of Cajal

KIT is required for development and maintenance of gastrointestinal interstitial cells of Cajal, the pacemaker lineage from which most GISTs are thought to arise. The dependence of both normal Cajal cells and GIST on KIT provides a direct lineage-based explanation for KIT’s central role in this tumor type (krimmer2023cryoemanalysesof pages 1-2, zhou2024kitmutationsand pages 1-2).

## 6. Genetic and disease evidence

### 6.1 Loss of function

Partial KIT loss of function causes impaired melanocyte development and piebaldism; experimental reduction also produces mast-cell deficiency, anemia or other hematopoietic defects, and sterility. Complete loss of KIT or SCF activity is lethal in classical genetic models. These concordant phenotypes across pigment, blood, and germ-cell lineages strongly support the normal functional annotation (r�nnstrand2004signaltransductionvia pages 1-2, roskoski2005signalingbykit pages 1-2).

### 6.2 Gain of function

Activating mutations bypass the normal requirement for SCF or make the receptor hypersensitive to ligand. Mutation location matters mechanistically:

* **Extracellular-domain mutations** can strengthen receptor dimerization.
* **Juxtamembrane mutations**, frequent in GIST, weaken autoinhibition.
* **Activation-loop/kinase-domain mutations**, particularly D816V in mastocytosis, stabilize active kinase conformations and alter inhibitor sensitivity (r�nnstrand2004signaltransductionvia pages 1-2, pardanani2023systemicmastocytosisin pages 1-2, cilloni2024detectionofkit pages 3-5, krimmer2023cryoemanalysesof pages 8-10).

Recent estimates indicate primary KIT mutations in approximately **80–90% of treatment-naive GIST**, with KIT protein expression in about **95%**. More than **90% of mastocytosis** cases have somatic KIT point mutations, most often D816V in adult systemic disease. In pediatric cutaneous disease, D816V is reported in approximately 30% of biopsies and extracellular-domain activating mutations in approximately 40% (cilloni2024detectionofkit pages 3-5, zhou2024kitmutationsand pages 1-2).

KIT alterations also occur in subsets of AML—especially core-binding-factor AML—germ-cell tumors/seminoma, melanoma, and mast-cell leukemia. These associations should not be interpreted as equivalent across diseases: the mutation domain, co-mutations, lineage, and receptor localization determine biological behavior and drug sensitivity (krimmer2023cryoemanalysesof pages 1-2, katagiri2022mutatedkittyrosine pages 1-2, cilloni2024detectionofkit pages 3-5).

## 7. Current applications and real-world implementation

### Diagnostic use

KIT protein is detected clinically as **CD117** by immunohistochemistry or flow cytometry. It is widely used in the diagnostic work-up of GIST, mast-cell disease, and hematologic neoplasia, although expression alone does not demonstrate an activating mutation. Molecular testing is therefore needed to identify the relevant KIT variant and select therapy.

For mastocytosis, highly sensitive allele-specific quantitative PCR or droplet-digital PCR is important because KIT D816V variant allele fractions can be below ordinary NGS detection thresholds. Peripheral-blood testing can miss low-burden disease; one 2024 review reported that peripheral-blood ddPCR misses more than half of bone-marrow mastocytosis cases, emphasizing that a negative blood test does not exclude disease (cilloni2024detectionofkit pages 2-3).

### GIST therapy

Imatinib is foundational first-line therapy for susceptible KIT-mutant advanced GIST. Subsequent agents include sunitinib, regorafenib, and ripretinib, with selection influenced by the primary and secondary mutation spectrum. Resistance commonly emerges after approximately **18–24 months**, and a 2024 synthesis attributed about **90% of imatinib resistance** to secondary KIT mutations. Individual metastases or tumor subclones can carry different secondary mutations, explaining why later-line inhibitors often suppress only part of the disease (zhou2024kitmutationsand pages 1-2).

This is a canonical precision-oncology implementation: KIT genotyping is predictive, not merely descriptive. Juxtamembrane exon-11 mutants are often imatinib-sensitive, whereas activation-loop variants have different conformational preferences and inhibitor profiles.

### Systemic mastocytosis therapy

The common KIT D816V mutant is generally resistant to imatinib. Imatinib is therefore reserved for unusual imatinib-sensitive variants, such as selected transmembrane or juxtamembrane mutants, or advanced systemic mastocytosis lacking D816V or with unknown KIT status. In one Mayo Clinic series, only 4 of 22 evaluable patients responded—an overall response rate of **18%**—supporting this restricted role (pardanani2023systemicmastocytosisin pages 16-16).

Midostaurin and avapritinib are clinically important inhibitors for advanced systemic mastocytosis. Avapritinib can produce deep biochemical, histological, and molecular responses, although associated myeloid neoplasms containing additional driver mutations may not be fully controlled by KIT inhibition alone. Preliminary phase-2 bezuclastinib data cited in the 2023 update showed greater than 50% serum-tryptase reduction in all 11 reported patients; all eight evaluable after at least two cycles had at least 50% reduction in marrow mast-cell burden, with complete aggregate clearance in six. These early numbers require confirmation in larger and mature datasets (pardanani2023systemicmastocytosisin pages 1-2, pardanani2023systemicmastocytosisin pages 16-16).

## 8. Recent developments, 2023–2024

### 8.1 Structural oncogenic plasticity

Krimmer and colleagues’ March 2023 single-particle cryo-EM analysis examined full-length wild-type KIT and extracellular oncogenic mutants. Although the transmembrane and kinase regions were not resolved, the work directly visualized how extracellular interfaces encode activation. The ligand-sensitized DupA502/Y503 mutant expanded the D5 interface from approximately **292 Å²** in wild type to **479 Å²** and increased isolated D4–D5-fragment dimerization affinity by approximately **10–20-fold** (krimmer2023cryoemanalysesof pages 7-8, krimmer2023cryoemanalysesof pages 1-2).

The ligand-independent T417I/Δ418–419 mutant adopted a V-shaped assembly held by an approximately **1,001 Å²** D5 interface. Its membrane-proximal termini were about **4.8 Å** apart without SCF but **15.0 Å** apart after SCF binding, which restored a more wild-type-like D4/D5 organization. This demonstrates “oncogenic plasticity”: the same mutant receptor can occupy markedly different extracellular arrangements while remaining signaling competent. The authors identify the D4/D5 interface as a potential therapeutic Achilles heel for antibodies, bispecifics, or other binders (krimmer2023cryoemanalysesof pages 7-8, krimmer2023cryoemanalysesof pages 1-2, krimmer2023cryoemanalysesof pages 8-10). Publication: 27 March 2023; DOI: https://doi.org/10.1073/pnas.2300054120.

### 8.2 Resistance-focused functional annotation

The February 2024 review by Zhou and colleagues emphasizes that mutant KIT in GIST differs from wild-type KIT not only by ligand independence but also by altered localization, transcriptional regulation, processing, and degradation. High KIT expression is usually not explained by gene amplification. This broader model helps explain persistent “KIT addiction” and suggests that reducing receptor production, maturation, or stability could complement ATP-site inhibition (zhou2024kitmutationsand pages 1-2). DOI: https://doi.org/10.1186/s12964-023-01411-x.

### 8.3 Mutation detection in mastocytosis

The October 2024 review by Cilloni and colleagues highlights the clinical need for ultrasensitive D816V detection and mutation-specific interpretation. More than 90% of affected patients carry a KIT point mutation, but variant allele fractions may be too low for routine NGS. The review also underscores age-related mutation differences: adult disease is dominated by exon-17 D816V, whereas pediatric cutaneous disease more often includes extracellular mutations (cilloni2024detectionofkit pages 3-5, cilloni2024detectionofkit pages 2-3). DOI: https://doi.org/10.3390/ijms252010885.

## 9. Expert interpretation

The most precise functional description of KIT is: **an SCF-gated plasma-membrane tyrosine kinase that couples extracellular dimer assembly to intracellular phosphotyrosine signaling**. Its essential mechanistic sequence is ligand binding → receptor dimerization and D4/D5 alignment → relief of juxtamembrane inhibition → reciprocal phosphorylation → effector recruitment → pathway activation → internalization and degradation.

Three expert-level qualifications are important:

1. **KIT expression is not equivalent to KIT oncogenic activation.** CD117 positivity can reflect normal lineage biology, whereas mutation and phospho-signaling establish constitutive activation.
2. **“KIT-mutant” is not one therapeutic category.** Extracellular, juxtamembrane, ATP-pocket, and activation-loop variants differ in conformation and drug sensitivity.
3. **Resistance is structurally heterogeneous.** In GIST, multiple secondary KIT mutations can coexist across lesions, making a single ATP-site inhibitor unlikely to suppress every clone. Extracellular-interface inhibition, receptor degradation, and rational combinations are therefore attractive research directions (zhou2024kitmutationsand pages 1-2, krimmer2023cryoemanalysesof pages 7-8, krimmer2023cryoemanalysesof pages 8-10).

## 10. Confidence and limitations

Confidence is **high** for identity, domain architecture, SCF specificity, receptor activation, plasma-membrane localization, major signaling pathways, and the core developmental and disease roles; these are supported by convergent structural, biochemical, genetic, and clinical evidence. The catalytic reaction is the standard protein-tyrosine-kinase phosphotransfer reaction; KIT recognizes receptor and protein substrates in a cellular docking context rather than a single small-molecule substrate.

Clinical percentages vary by cohort, assay sensitivity, age, disease classification, and whether only treatment-naive tumors are counted. Older statements that more than 90% of GISTs harbor KIT mutations should therefore be superseded by recent estimates of approximately 80–90%, while recognizing that KIT protein expression is more frequent than mutation. Early bezuclastinib results are promising but preliminary, and the 2023 cryo-EM structures resolved extracellular—not intracellular kinase—organization.

## Selected references

* Krimmer SG et al. **Cryo-EM analyses of KIT and oncogenic mutants reveal structural oncogenic plasticity and a target for therapeutic intervention.** *PNAS*. Published March 2023. https://doi.org/10.1073/pnas.2300054120 (krimmer2023cryoemanalysesof pages 1-2, krimmer2023cryoemanalysesof pages 7-8, krimmer2023cryoemanalysesof pages 8-10)
* Zhou S et al. **KIT mutations and expression: current knowledge and new insights for overcoming imatinib resistance in GIST.** *Cell Communication and Signaling*. Published February 2024. https://doi.org/10.1186/s12964-023-01411-x (zhou2024kitmutationsand pages 1-2)
* Cilloni D et al. **Detection of KIT Mutations in Systemic Mastocytosis: How, When, and Why.** *International Journal of Molecular Sciences*. Published October 2024. https://doi.org/10.3390/ijms252010885 (cilloni2024detectionofkit pages 3-5, cilloni2024detectionofkit pages 2-3)
* Pardanani A. **Systemic mastocytosis in adults: 2023 update on diagnosis, risk stratification and management.** *American Journal of Hematology*. Published May 2023. https://doi.org/10.1002/ajh.26962 (pardanani2023systemicmastocytosisin pages 1-2, pardanani2023systemicmastocytosisin pages 16-16)
* Heldin C-H, Lennartsson J. **Structural and functional properties of platelet-derived growth factor and stem cell factor receptors.** *Cold Spring Harbor Perspectives in Biology*. Published August 2013. https://doi.org/10.1101/cshperspect.a009100 (heldin2013structuralandfunctional pages 7-9)
* Roskoski R. **Signaling by Kit protein-tyrosine kinase—the stem cell factor receptor.** *Biochemical and Biophysical Research Communications*. Published November 2005. https://doi.org/10.1016/j.bbrc.2005.08.055 (roskoski2005signalingbykit pages 1-2, roskoski2005signalingbykit pages 2-3)

References

1. (katagiri2022mutatedkittyrosine pages 1-2): Seiichiro Katagiri, SungGi Chi, Yosuke Minami, Kentaro Fukushima, Hirohiko Shibayama, Naoko Hosono, Takahiro Yamauchi, Takanobu Morishita, Takeshi Kondo, Masamitsu Yanada, Kazuhito Yamamoto, Junya Kuroda, Kensuke Usuki, Daigo Akahane, and Akihiko Gotoh. Mutated kit tyrosine kinase as a novel molecular target in acute myeloid leukemia. International Journal of Molecular Sciences, 23:4694, Apr 2022. URL: https://doi.org/10.3390/ijms23094694, doi:10.3390/ijms23094694. This article has 26 citations.

2. (roskoski2005signalingbykit pages 2-3): Robert Roskoski. Signaling by kit protein-tyrosine kinase—the stem cell factor receptor. Biochemical and Biophysical Research Communications, 337(1):1-13, Nov 2005. URL: https://doi.org/10.1016/j.bbrc.2005.08.055, doi:10.1016/j.bbrc.2005.08.055. This article has 368 citations and is from a peer-reviewed journal.

3. (cilloni2024detectionofkit pages 2-3): Daniela Cilloni, Beatrice Maffeo, Arianna Savi, Alice Costanza Danzero, Valentina Bonuomo, and Carmen Fava. Detection of kit mutations in systemic mastocytosis: how, when, and why. Oct 2024. URL: https://doi.org/10.3390/ijms252010885, doi:10.3390/ijms252010885. This article has 24 citations.

4. (OpenTargets Search: -KIT): Open Targets Query (-KIT, 35 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (krimmer2023cryoemanalysesof pages 1-2): Stefan G. Krimmer, Nicole Bertoletti, Yoshihisa Suzuki, Luka Katic, Jyotidarsini Mohanty, Sheng Shu, Sangwon Lee, Irit Lax, Wei Mi, and Joseph Schlessinger. Cryo-em analyses of kit and oncogenic mutants reveal structural oncogenic plasticity and a target for therapeutic intervention. Proceedings of the National Academy of Sciences of the United States of America, Mar 2023. URL: https://doi.org/10.1073/pnas.2300054120, doi:10.1073/pnas.2300054120. This article has 27 citations and is from a highest quality peer-reviewed journal.

6. (roskoski2005signalingbykit pages 1-2): Robert Roskoski. Signaling by kit protein-tyrosine kinase—the stem cell factor receptor. Biochemical and Biophysical Research Communications, 337(1):1-13, Nov 2005. URL: https://doi.org/10.1016/j.bbrc.2005.08.055, doi:10.1016/j.bbrc.2005.08.055. This article has 368 citations and is from a peer-reviewed journal.

7. (cilloni2024detectionofkit pages 3-5): Daniela Cilloni, Beatrice Maffeo, Arianna Savi, Alice Costanza Danzero, Valentina Bonuomo, and Carmen Fava. Detection of kit mutations in systemic mastocytosis: how, when, and why. Oct 2024. URL: https://doi.org/10.3390/ijms252010885, doi:10.3390/ijms252010885. This article has 24 citations.

8. (heldin2013structuralandfunctional pages 7-9): C.-H. Heldin and J. Lennartsson. Structural and functional properties of platelet-derived growth factor and stem cell factor receptors. Cold Spring Harbor perspectives in biology, 5 8:a009100, Aug 2013. URL: https://doi.org/10.1101/cshperspect.a009100, doi:10.1101/cshperspect.a009100. This article has 244 citations and is from a peer-reviewed journal.

9. (krimmer2023cryoemanalysesof pages 7-8): Stefan G. Krimmer, Nicole Bertoletti, Yoshihisa Suzuki, Luka Katic, Jyotidarsini Mohanty, Sheng Shu, Sangwon Lee, Irit Lax, Wei Mi, and Joseph Schlessinger. Cryo-em analyses of kit and oncogenic mutants reveal structural oncogenic plasticity and a target for therapeutic intervention. Proceedings of the National Academy of Sciences of the United States of America, Mar 2023. URL: https://doi.org/10.1073/pnas.2300054120, doi:10.1073/pnas.2300054120. This article has 27 citations and is from a highest quality peer-reviewed journal.

10. (r�nnstrand2004signaltransductionvia pages 1-2): L. R�nnstrand. Signal transduction via the stem cell factor receptor/c-kit. Cellular and Molecular Life Sciences CMLS, 61:2535-2548, Oct 2004. URL: https://doi.org/10.1007/s00018-004-4189-6, doi:10.1007/s00018-004-4189-6. This article has 643 citations.

11. (gall2015neutralizationofkit pages 10-11): Marianne Le Gall, Ronan Crépin, Madeline Neiveyans, Christian Auclair, Yongfeng Fan, Yu Zhou, James D. Marks, André Pèlegrin, and Marie-Alix Poul. Neutralization of kit oncogenic signaling in leukemia with antibodies targeting kit membrane proximal domain 5. Molecular Cancer Therapeutics, 14:2595-2605, Nov 2015. URL: https://doi.org/10.1158/1535-7163.mct-15-0321, doi:10.1158/1535-7163.mct-15-0321. This article has 11 citations and is from a peer-reviewed journal.

12. (zhou2024kitmutationsand pages 1-2): Shishan Zhou, Omar Abdihamid, Fengbo Tan, Haiyan Zhou, Heli Liu, Zhi Li, Sheng Xiao, and Bin Li. Kit mutations and expression: current knowledge and new insights for overcoming im resistance in gist. Cell Communication and Signaling : CCS, Feb 2024. URL: https://doi.org/10.1186/s12964-023-01411-x, doi:10.1186/s12964-023-01411-x. This article has 81 citations.

13. (pardanani2023systemicmastocytosisin pages 1-2): Animesh Pardanani. Systemic mastocytosis in adults: 2023 update on diagnosis, risk stratification and management. American Journal of Hematology, 98:1097-1116, May 2023. URL: https://doi.org/10.1002/ajh.26962, doi:10.1002/ajh.26962. This article has 159 citations and is from a domain leading peer-reviewed journal.

14. (pardanani2023systemicmastocytosisin pages 16-16): Animesh Pardanani. Systemic mastocytosis in adults: 2023 update on diagnosis, risk stratification and management. American Journal of Hematology, 98:1097-1116, May 2023. URL: https://doi.org/10.1002/ajh.26962, doi:10.1002/ajh.26962. This article has 159 citations and is from a domain leading peer-reviewed journal.

15. (krimmer2023cryoemanalysesof pages 8-10): Stefan G. Krimmer, Nicole Bertoletti, Yoshihisa Suzuki, Luka Katic, Jyotidarsini Mohanty, Sheng Shu, Sangwon Lee, Irit Lax, Wei Mi, and Joseph Schlessinger. Cryo-em analyses of kit and oncogenic mutants reveal structural oncogenic plasticity and a target for therapeutic intervention. Proceedings of the National Academy of Sciences of the United States of America, Mar 2023. URL: https://doi.org/10.1073/pnas.2300054120, doi:10.1073/pnas.2300054120. This article has 27 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](KIT-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. roskoski2005signalingbykit pages 1-2
2. heldin2013structuralandfunctional pages 7-9
3. krimmer2023cryoemanalysesof pages 7-8
4. cilloni2024detectionofkit pages 2-3
5. zhou2024kitmutationsand pages 1-2
6. pardanani2023systemicmastocytosisin pages 16-16
7. katagiri2022mutatedkittyrosine pages 1-2
8. roskoski2005signalingbykit pages 2-3
9. krimmer2023cryoemanalysesof pages 1-2
10. cilloni2024detectionofkit pages 3-5
11. gall2015neutralizationofkit pages 10-11
12. pardanani2023systemicmastocytosisin pages 1-2
13. krimmer2023cryoemanalysesof pages 8-10
14. 10.3390/ijms252010885
15. 10.1016/j.bbrc.2005.08.055
16. 10.3390/ijms23094694
17. 10.1101/cshperspect.a009100
18. 10.1073/pnas.2300054120
19. 10.1007/s00018-004-4189-6
20. 10.1158/1535-7163.MCT-15-0321
21. 10.1186/s12964-023-01411-x
22. 10.1002/ajh.26962
23. https://doi.org/10.3390/ijms252010885
24. https://doi.org/10.1016/j.bbrc.2005.08.055
25. https://doi.org/10.3390/ijms23094694
26. https://doi.org/10.1101/cshperspect.a009100
27. https://doi.org/10.1073/pnas.2300054120
28. https://doi.org/10.1007/s00018-004-4189-6
29. https://doi.org/10.1158/1535-7163.MCT-15-0321
30. https://doi.org/10.1186/s12964-023-01411-x
31. https://doi.org/10.1002/ajh.26962
32. https://doi.org/10.1073/pnas.2300054120.
33. https://doi.org/10.1186/s12964-023-01411-x.
34. https://doi.org/10.3390/ijms252010885.
35. https://doi.org/10.3390/ijms23094694,
36. https://doi.org/10.1016/j.bbrc.2005.08.055,
37. https://doi.org/10.3390/ijms252010885,
38. https://doi.org/10.1073/pnas.2300054120,
39. https://doi.org/10.1101/cshperspect.a009100,
40. https://doi.org/10.1007/s00018-004-4189-6,
41. https://doi.org/10.1158/1535-7163.mct-15-0321,
42. https://doi.org/10.1186/s12964-023-01411-x,
43. https://doi.org/10.1002/ajh.26962,