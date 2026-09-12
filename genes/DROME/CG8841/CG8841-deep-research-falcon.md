---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-10T14:37:16.589073'
end_time: '2026-09-10T14:44:20.909286'
duration_seconds: 424.32
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: CG8841
  gene_symbol: Dmc1
  uniprot_accession: Q0E9B5
  protein_description: 'RecName: Full=Protein HID1 {ECO:0008006|Google:ProtNLM};'
  gene_info: Name=Dmc1 {ECO:0000313|EMBL:AAF58533.1}; Synonyms=Dmel\CG8841 {ECO:0000313|EMBL:AAF58533.1};
    ORFNames=CG8841 {ECO:0000313|EMBL:AAF58533.1, ECO:0000313|FlyBase:FBgn0033713},
    Dmel_CG8841 {ECO:0000313|EMBL:AAF58533.1};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the hid-1 family.
  protein_domains: HID1/Ecm30. (IPR026705); Hid1 (PF12722)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 8
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: CG8841-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q0E9B5
- **Protein Description:** RecName: Full=Protein HID1 {ECO:0008006|Google:ProtNLM};
- **Gene Information:** Name=Dmc1 {ECO:0000313|EMBL:AAF58533.1}; Synonyms=Dmel\CG8841 {ECO:0000313|EMBL:AAF58533.1}; ORFNames=CG8841 {ECO:0000313|EMBL:AAF58533.1, ECO:0000313|FlyBase:FBgn0033713}, Dmel_CG8841 {ECO:0000313|EMBL:AAF58533.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the hid-1 family.
- **Key Domains:** HID1/Ecm30. (IPR026705); Hid1 (PF12722)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Dmc1" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Dmc1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Dmc1** (gene ID: CG8841, UniProt: Q0E9B5) in DROME.

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
- **UniProt Accession:** Q0E9B5
- **Protein Description:** RecName: Full=Protein HID1 {ECO:0008006|Google:ProtNLM};
- **Gene Information:** Name=Dmc1 {ECO:0000313|EMBL:AAF58533.1}; Synonyms=Dmel\CG8841 {ECO:0000313|EMBL:AAF58533.1}; ORFNames=CG8841 {ECO:0000313|EMBL:AAF58533.1, ECO:0000313|FlyBase:FBgn0033713}, Dmel_CG8841 {ECO:0000313|EMBL:AAF58533.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the hid-1 family.
- **Key Domains:** HID1/Ecm30. (IPR026705); Hid1 (PF12722)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Dmc1" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Dmc1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Dmc1** (gene ID: CG8841, UniProt: Q0E9B5) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional-annotation report: *Drosophila melanogaster* CG8841/Q0E9B5

## Executive conclusion

The gene symbol **“Dmc1” is ambiguous and the literature is limited for this specific protein**. For the target defined here—UniProt **Q0E9B5**, *D. melanogaster* **CG8841/FBgn0033713**—the supplied UniProt annotation identifies a **HID-1-family protein** containing HID1/Ecm30 (InterPro IPR026705) and Hid1 (Pfam PF12722). It must not be confused with the well-known **DMC1 meiotic recombinase**. Exact searches for Q0E9B5, CG8841, and FBgn0033713 yielded no primary study directly testing this fly protein; consequently, recombinase literature was excluded.

The most defensible annotation is therefore **orthology-based**: CG8841 probably encodes a nonenzymatic, membrane-associated regulator of the regulated secretory pathway, acting at the Golgi/trans-Golgi network (TGN) and immature dense-core vesicles to support lumenal acidification, cargo sorting/storage, and secretory-granule maturation. Its precise function, localization, cargo dependence, and phenotype have not been demonstrated directly in *Drosophila*.

| Annotation category | Finding for Q0E9B5/CG8841 | Evidence basis | Confidence |
|---|---|---|---|
| Identity | *Drosophila melanogaster* protein Q0E9B5; gene **CG8841** (FBgn0033713), with **Dmc1** supplied as a synonym. This is a HID-1-family protein, **not** the unrelated DMC1 meiotic recombinase. | User-supplied UniProt annotation; exact-identifier literature searches found no direct CG8841 publication. | High for database identity; low for use of the ambiguous symbol *Dmc1* |
| Protein class/domain | Non-enzymatic-appearing HID-1-family protein containing HID1/Ecm30 (InterPro IPR026705) and Hid1 (Pfam PF12722). HID-1 orthologs are conserved membrane-associated proteins; their detailed domain organization remains unresolved. | Family/domain assignment is user-supplied UniProt information. Conservation and limited domain knowledge come from ortholog studies (du2016hid1isrequired pages 1-2, bartsch2022hid1asa pages 119-122). | High for family/domain assignment; moderate for functional class |
| Primary function | Most defensible annotation: a putative regulator of dense-core secretory-vesicle biogenesis and maturation, likely affecting cargo sorting or retention and organelle acidification rather than final exocytotic membrane fusion. This is an **orthology-based inference for CG8841**, not direct fly validation. | Rat neuroendocrine-cell HID-1 knockout disrupted TGN acidification, cargo sorting, and large dense-core-vesicle formation; mouse β-cell knockout blocked immature-granule homotypic fusion (hummer2017hid1controlsformation pages 1-2, du2016hid1isrequired pages 1-2). | Moderate by conserved-family inference; unvalidated directly in *Drosophila* |
| Cellular localization | Predicted functional site: cytosolic face of the Golgi/trans-Golgi network and membranes of immature dense-core vesicles or their precursors. Direct localization of CG8841 in fly cells has not been demonstrated in the retrieved literature. | C. elegans HID-1 is membrane-associated and requires its N-terminal glycine for targeting; mammalian HID-1 is enriched at the TGN and also occurs in cytosolic/membrane pools (mesa2011hid1anew pages 6-7, mesa2011hid1anew pages 17-21, bartsch2022hid1asa pages 80-84). | Moderate for orthologs; low-to-moderate for CG8841 |
| Pathway | Putative regulated secretory pathway: TGN cargo sorting → dense-core-vesicle budding/biogenesis → immature-granule fusion and maturation → storage and stimulus-dependent release of neuropeptides, peptide hormones, or monoamines. | Direct C. elegans peptidergic-signaling evidence and mammalian secretory-granule experiments (mesa2011hid1anew pages 1-2, du2016hid1isrequired pages 1-2, hummer2017hid1controlsformation pages 1-2). | Moderate for conserved pathway placement |
| Catalytic/substrate status | No catalytic reaction, active site, transported substrate, or ligand specificity has been established. HID-1 is best treated as a membrane-associated trafficking/assembly regulator—not an enzyme or transporter. Proposed effects include retention/localization of ATP6V0A2 and sorting of soluble and membrane cargo, but a direct biochemical interaction is not firmly established (bartsch2022hid1asa pages 124-127, bartsch2022hid1asa pages 117-119). | Absence of demonstrated catalysis plus ortholog cell-biological studies; ATP6V0A2 anchoring remains a mechanistic model. | High that no reaction is currently established; low-to-moderate for the anchoring mechanism |
| Direct *Drosophila* evidence | No CG8841/Q0E9B5-specific primary paper, localization experiment, loss-of-function phenotype, rescue test, or biochemical assay was identified. The supplied family/domain annotation is therefore the only target-specific basis used here. | Exact searches for Q0E9B5, FBgn0033713, and CG8841 returned no direct study; retrieved experimental papers examined orthologs. | High confidence that the present report must distinguish inference from direct fly evidence |
| Key ortholog evidence | In C. elegans, loss of HID-1 alters neuropeptide abundance/secretion; membrane targeting depends on an N-terminal glycine, and punctate axonal HID-1 rises approximately **80%** in *unc-31* and **160%** in *unc-13* mutants. In rat neuroendocrine cells, knockout impairs LDCV formation and reduces SGII to about **40%** of wild type. Mouse β-cell knockout causes immature-granule accumulation, defective proinsulin processing, and glucose intolerance. Human-cell models report SGII at approximately **13–46%** of wild type and substantial loss of candidate protein interactions (mesa2011hid1anew pages 7-9, bartsch2022hid1asa pages 25-27, du2016hid1isrequired pages 1-2, bartsch2022hid1asa pages 124-127, bartsch2022hid1asa pages 119-122). | Direct experiments in C. elegans, rat, mouse, and cultured human cells—not direct evidence in *Drosophila*. | High for the reported ortholog experiments; moderate for transfer to CG8841 |
| Overall confidence | **High**: Q0E9B5/CG8841 is assigned to the HID-1 family and should not be confused with meiotic DMC1. **Moderate**: it probably supports regulated dense-core-vesicle biogenesis at the Golgi/TGN. **Low**: exact fly tissues, cargoes, interactors, phenotypes, and molecular mechanism remain unknown. | Integrated database identity and conserved-family evidence, with explicit organism-specific boundaries. | Moderate functional-annotation confidence overall |


*Table: This table separates target-specific database annotation from experiments on HID-1 orthologs and labels the resulting confidence. It highlights that the proposed secretory-vesicle function and Golgi localization remain orthology-based for Drosophila CG8841.*

## 1. Identity and nomenclature verification

The specified organism is **fruit fly, *Drosophila melanogaster***, and the stable target identifiers are **Q0E9B5**, **CG8841**, and **FBgn0033713**. The supplied family/domain assignments—HID-1 family, HID1/Ecm30, and Pfam Hid1—are internally consistent with the retrieved HID-1 literature. HID-1 is described as conserved among *C. elegans*, *Drosophila*, mouse, and human, although the papers retrieved did not explicitly map the fly homolog to CG8841; that final mapping rests on the supplied UniProt record (du2016hid1isrequired pages 1-2).

The label **Dmc1 should not be used alone in literature searches or functional summaries**, because it ordinarily retrieves an unrelated RecA-family meiotic DNA recombinase. Nothing retrieved for HID-1 supports ATP-dependent strand exchange, meiotic recombination, DNA binding, or another DMC1-recombinase function.

## 2. Protein class and primary molecular function

HID-1 is best classified as a **peripheral membrane trafficking/assembly regulator**, not an enzyme, transporter, receptor, or secreted cargo. No catalytic reaction, active site, transported substrate, or ligand specificity has been established. Earlier work described HID-1 as lacking recognizable conventional homology domains, notwithstanding its defining HID1-family region, and suggested reversible partitioning between membrane and cytosol (du2016hid1isrequired pages 1-2).

Across experimentally studied orthologs, HID-1 acts early in dense-core-vesicle formation rather than as an essential component of the final calcium-triggered plasma-membrane fusion machinery. In rat neuroendocrine cells, HID-1 loss reduced vesicle abundance, altered morphology and dense-core formation, impaired storage of peptide hormones and monoamines, and disrupted sorting of soluble and transmembrane regulated-secretory cargo. Calcium responsiveness and normalized exocytotic competence were comparatively preserved, pointing to deficient cargo availability and vesicle biogenesis rather than a general exocytosis block (hummer2017hid1controlsformation pages 1-2, bartsch2022hid1asa pages 25-27, bartsch2022hid1asa pages 122-124).

A proposed mechanism is that Golgi-associated HID-1 helps retain or position the V-ATPase a2 subunit ATP6V0A2, thereby sustaining the acidic TGN lumen required for cargo aggregation and sorting. HID-1 knockout caused strong ATP6V0A2 redistribution without a major reduction in total protein. This is a plausible cell-biological model, but a direct physical interaction and the description of HID-1 as an ATP6V0A2 “anchor” remain incompletely proven (bartsch2022hid1asa pages 124-127, bartsch2022hid1asa pages 117-119).

A complementary mouse β-cell study placed HID-1 in **homotypic fusion of immature secretory granules**. Conditional loss caused accumulation of immature granules, defective proinsulin processing, an elevated serum proinsulin/insulin ratio, insufficient insulin release, and glucose intolerance. Thus, the literature supports several connected early-stage activities—TGN cargo sorting and acidification, granule budding/formation, and immature-granule fusion—rather than one demonstrated catalytic step (du2016hid1isrequired pages 1-2).

### Functional annotation proposed for CG8841

> **Putative regulator of dense-core secretory-vesicle biogenesis and maturation at the Golgi/TGN; likely promotes appropriate organelle acidification, regulated-secretory cargo sorting/storage, and maturation of immature granules.**

This annotation has **moderate confidence by conserved-family inference**, but it remains unvalidated in fruit fly.

## 3. Cellular localization

The predicted functional site is the **cytosolic face of the medial/trans-Golgi and TGN**, with possible association with immature dense-core-vesicle or precursor membranes.

In *C. elegans*, neuronal HID-1–GFP was membrane-associated and appeared in puncta in the nerve ring and dorsal cord. Its delivery toward synaptic regions required the UNC-104 kinesin. Substitution of the conserved second-position glycine with asparagine produced diffuse/mislocalized protein, shifted part of it into the soluble fraction, and abolished functional rescue, supporting N-terminal glycine-dependent—probably myristoylation-dependent—membrane attachment (mesa2011hid1anew pages 6-7, mesa2011hid1anew pages 7-9, mesa2011hid1anew pages 1-2).

In PC12 cells, murine HID-1 was enriched near the TGN and partially colocalized with Syntaxin-6 and CI-M6PR, with little association with cis/medial Golgi, early endosomes, or lysosomes. Partial overlap with Rab27, synaptotagmin I, and perinuclear neuropeptide Y was also observed (mesa2011hid1anew pages 17-21). Later human-cell work found endogenous HID1 mainly in cytosolic fractions, with smaller membrane/cytoskeletal pools and only faint nuclear signal; imperfect fraction purity and model-dependent localization limit fine compartment assignments (bartsch2022hid1asa pages 80-84).

Accordingly, CG8841 should **not yet receive an experimentally verified fly Golgi annotation**. Golgi/TGN and secretory-vesicle localization are predictions transferred from orthologs.

## 4. Biological process and pathway placement

The inferred pathway is:

**TGN acidification and cargo aggregation → regulated-secretory cargo sorting/retention → dense-core-vesicle budding/biogenesis → homotypic fusion and maturation of immature granules → storage and stimulus-dependent secretion of neuropeptides, peptide hormones, and monoamines.**

Direct *C. elegans* genetics place HID-1 in peptidergic signaling. Null mutants had reduced endogenous neuropeptide levels and altered secretion of neuronal and intestinal dense-core-vesicle cargo, with neuromuscular, defecation, and dauer-related phenotypes. Genetic relationships with peptide-processing pathways and parallel behavior relative to RAB-3/RAB-27 further support action in neurosecretory trafficking rather than classical synaptic-vesicle transmission alone (mesa2011hid1anew pages 7-9, mesa2011hid1anew pages 6-7, mesa2011hid1anew pages 1-2).

This pathway assignment does not establish which fly neuropeptides or endocrine tissues depend on CG8841. Those are important unresolved questions.

## 5. Quantitative evidence from ortholog systems

* In *C. elegans*, axonal HID-1–GFP punctate fluorescence increased approximately **80% in unc-31/CAPS mutants** and **160% in unc-13 mutants**, consistent with accumulation on exocytic vesicles or precursors when priming/secretion is disrupted (mesa2011hid1anew pages 7-9).
* In HID-1-deficient PC12 cells, secretogranin II was reduced to approximately **40% of wild-type**, despite no corresponding decrease in *Scg2* transcription; lysosomal degradation accounted for part of the loss (bartsch2022hid1asa pages 25-27).
* Human SH-SY5Y HID1-edited lines showed SGII protein at approximately **13 ± 3.3% to 46 ± 15% of wild-type**, accompanied by loss of dispersed CHGA-positive puncta and perinuclear retention (bartsch2022hid1asa pages 124-127).
* Human-cell affinity proteomics identified at least **66 candidate wild-type HID1 interactors**; **63** were not enriched with the p.G320Rfs*3 truncation model, while three were shared. These are candidate complex associations, not necessarily direct binding partners (bartsch2022hid1asa pages 119-122).
* During SH-SY5Y differentiation, HID1 mRNA approximately doubled and protein increased about **fivefold**. HID1-deficient lines had impaired neurite morphology, abnormal differentiation-marker responses, and clone-dependent apoptosis (bartsch2022hid1asa pages 127-129).

These values demonstrate conserved biological importance but cannot be reported as measurements of fly CG8841.

## 6. Recent developments and current research status

No substantive **2023–2024 primary publication directly addressing CG8841/Q0E9B5** was identified. A 2024 Drosophila secretory-granule thesis was retrieved, but the available material did not provide direct CG8841 evidence. Thus, the request to prioritize 2023–2024 evidence cannot be met without substituting unrelated genes or overinterpreting general secretory-granule work.

The most recent detailed HID1 investigation retrieved was a **2022 doctoral study** using human SH-SY5Y and HeLa models. It expanded the candidate interactome, modeled a pathogenic p.G320Rfs*3 allele, and linked HID1 loss to defective neuronal differentiation and secretory-vesicle phenotypes. The premature-stop transcript underwent nonsense-mediated decay in edited SH-SY5Y cells; candidate interactors included VGF, TM9SF3, dynein-related machinery, ARF proteins, and VPS35, but direct interactions and their physiological relevance remain unresolved (bartsch2022hid1asa pages 131-134, bartsch2022hid1asa pages 119-122, bartsch2022hid1asa pages 117-119).

The field’s current expert-level interpretation is therefore cautious: HID1 is convincingly connected to Golgi/dense-core-vesicle biology, but whether its primary biochemical role is V-ATPase positioning, cargo selection, vesicle budding, transport coupling, immature-granule fusion, or coordination of several of these processes remains unsettled.

## 7. Applications and real-world relevance

There is no current fly-specific biotechnology, therapeutic, diagnostic, or agricultural implementation for CG8841. Its principal application is as a **comparative model candidate** for studying regulated secretion.

Ortholog research shows relevance to pancreatic β-cell biology, because mouse HID-1 loss disrupts proinsulin processing and glucose homeostasis (du2016hid1isrequired pages 1-2). Human loss-of-function studies connect HID1 to severe early-onset neurodevelopmental disease and motivate cellular assays of neuronal differentiation, survival, and dense-core-vesicle trafficking; however, these disease findings concern human HID1 and should not be directly assigned as CG8841 phenotypes (bartsch2022hid1asa pages 106-114, bartsch2022hid1asa pages 131-134).

## 8. Evidence gaps and recommended validation

The following experiments would convert the annotation from inference to direct fly evidence:

1. Endogenous CG8841 tagging and colocalization with cis-/trans-Golgi, TGN, and dense-core-vesicle markers.
2. CG8841-null or tissue-specific knockdown experiments in peptidergic neurons and endocrine cells, accompanied by genomic rescue.
3. Quantification of TGN pH, V-ATPase localization, secretory-granule number and morphology, and stimulus-dependent neuropeptide release.
4. Mutation of the predicted N-terminal membrane-targeting glycine to test whether fly CG8841 uses the conserved myristoylation mechanism.
5. Proximity labeling or affinity purification to test ATP6V0A2, ARF-family, dynein, VGF-like cargo, and granule-maturation machinery, followed by direct-binding validation.
6. Structural and biochemical work to determine whether the HID1/Ecm30 region is a scaffold, lipid-binding module, or regulator of another membrane protein.

## 9. Overall assessment

**High confidence:** Q0E9B5/CG8841 is the intended *D. melanogaster* HID-1-family protein and is not the canonical DMC1 meiotic recombinase.

**Moderate confidence:** conserved-family evidence predicts a role at the Golgi/TGN in dense-core-vesicle biogenesis, cargo handling, acidification, and maturation.

**Low confidence/unresolved:** exact fly localization, tissues, cargoes, interaction partners, organismal phenotypes, and molecular mechanism. No catalytic reaction or substrate specificity is currently established.

### Key literature

* Mesa R. et al. **“HID-1, a New Component of the Peptidergic Signaling Pathway.”** *Genetics* 187, 467–483. Published February 2011. https://doi.org/10.1534/genetics.110.121996 (mesa2011hid1anew pages 1-2)
* Du W. et al. **“HID-1 is required for homotypic fusion of immature secretory granules during maturation.”** *eLife* 5. Published October 2016. https://doi.org/10.7554/eLife.18134 (du2016hid1isrequired pages 1-2)
* Hummer B.H. et al. **“HID-1 controls formation of large dense core vesicles by influencing cargo sorting and trans-Golgi network acidification.”** *Molecular Biology of the Cell* 28, 3870–3880. Published December 2017. https://doi.org/10.1091/mbc.e17-08-0491 (hummer2017hid1controlsformation pages 1-2)
* Bartsch L.M. **“HID1 as a novel disease-causing gene in early onset neurological disorders: molecular, functional and phenotypic studies.”** Doctoral dissertation. Published 2022. https://doi.org/10.53846/goediss-9438 (bartsch2022hid1asa pages 80-84)

References

1. (du2016hid1isrequired pages 1-2): Wen Du, Maoge Zhou, Wei Zhao, Dongwan Cheng, Lifen Wang, Jingze Lu, Eli Song, Wei Feng, Yanhong Xue, Pingyong Xu, and Tao Xu. Hid-1 is required for homotypic fusion of immature secretory granules during maturation. eLife, Oct 2016. URL: https://doi.org/10.7554/elife.18134, doi:10.7554/elife.18134. This article has 55 citations and is from a domain leading peer-reviewed journal.

2. (bartsch2022hid1asa pages 119-122): Lydia Maximiliane Bartsch. Hid1 as a novel disease-causing gene in early onset neurological disorders: molecular, functional and phenotypic studies. ArXiv, 2022. URL: https://doi.org/10.53846/goediss-9438, doi:10.53846/goediss-9438. This article has 1 citations.

3. (hummer2017hid1controlsformation pages 1-2): Blake H. Hummer, Noah F. de Leeuw, Christian Burns, Lan Chen, Matthew S. Joens, Bethany Hosford, James A. J. Fitzpatrick, and Cedric S. Asensio. Hid-1 controls formation of large dense core vesicles by influencing cargo sorting and trans-golgi network acidification. Molecular Biology of the Cell, 28:3870-3880, Dec 2017. URL: https://doi.org/10.1091/mbc.e17-08-0491, doi:10.1091/mbc.e17-08-0491. This article has 49 citations and is from a domain leading peer-reviewed journal.

4. (mesa2011hid1anew pages 6-7): Rosana Mesa, Shuo Luo, Christopher M Hoover, Kenneth Miller, Alicia Minniti, Nibaldo Inestrosa, and Michael L Nonet. Hid-1, a new component of the peptidergic signaling pathway. Genetics, 187:467-483, Feb 2011. URL: https://doi.org/10.1534/genetics.110.121996, doi:10.1534/genetics.110.121996. This article has 36 citations and is from a domain leading peer-reviewed journal.

5. (mesa2011hid1anew pages 17-21): Rosana Mesa, Shuo Luo, Christopher M Hoover, Kenneth Miller, Alicia Minniti, Nibaldo Inestrosa, and Michael L Nonet. Hid-1, a new component of the peptidergic signaling pathway. Genetics, 187:467-483, Feb 2011. URL: https://doi.org/10.1534/genetics.110.121996, doi:10.1534/genetics.110.121996. This article has 36 citations and is from a domain leading peer-reviewed journal.

6. (bartsch2022hid1asa pages 80-84): Lydia Maximiliane Bartsch. Hid1 as a novel disease-causing gene in early onset neurological disorders: molecular, functional and phenotypic studies. ArXiv, 2022. URL: https://doi.org/10.53846/goediss-9438, doi:10.53846/goediss-9438. This article has 1 citations.

7. (mesa2011hid1anew pages 1-2): Rosana Mesa, Shuo Luo, Christopher M Hoover, Kenneth Miller, Alicia Minniti, Nibaldo Inestrosa, and Michael L Nonet. Hid-1, a new component of the peptidergic signaling pathway. Genetics, 187:467-483, Feb 2011. URL: https://doi.org/10.1534/genetics.110.121996, doi:10.1534/genetics.110.121996. This article has 36 citations and is from a domain leading peer-reviewed journal.

8. (bartsch2022hid1asa pages 124-127): Lydia Maximiliane Bartsch. Hid1 as a novel disease-causing gene in early onset neurological disorders: molecular, functional and phenotypic studies. ArXiv, 2022. URL: https://doi.org/10.53846/goediss-9438, doi:10.53846/goediss-9438. This article has 1 citations.

9. (bartsch2022hid1asa pages 117-119): Lydia Maximiliane Bartsch. Hid1 as a novel disease-causing gene in early onset neurological disorders: molecular, functional and phenotypic studies. ArXiv, 2022. URL: https://doi.org/10.53846/goediss-9438, doi:10.53846/goediss-9438. This article has 1 citations.

10. (mesa2011hid1anew pages 7-9): Rosana Mesa, Shuo Luo, Christopher M Hoover, Kenneth Miller, Alicia Minniti, Nibaldo Inestrosa, and Michael L Nonet. Hid-1, a new component of the peptidergic signaling pathway. Genetics, 187:467-483, Feb 2011. URL: https://doi.org/10.1534/genetics.110.121996, doi:10.1534/genetics.110.121996. This article has 36 citations and is from a domain leading peer-reviewed journal.

11. (bartsch2022hid1asa pages 25-27): Lydia Maximiliane Bartsch. Hid1 as a novel disease-causing gene in early onset neurological disorders: molecular, functional and phenotypic studies. ArXiv, 2022. URL: https://doi.org/10.53846/goediss-9438, doi:10.53846/goediss-9438. This article has 1 citations.

12. (bartsch2022hid1asa pages 122-124): Lydia Maximiliane Bartsch. Hid1 as a novel disease-causing gene in early onset neurological disorders: molecular, functional and phenotypic studies. ArXiv, 2022. URL: https://doi.org/10.53846/goediss-9438, doi:10.53846/goediss-9438. This article has 1 citations.

13. (bartsch2022hid1asa pages 127-129): Lydia Maximiliane Bartsch. Hid1 as a novel disease-causing gene in early onset neurological disorders: molecular, functional and phenotypic studies. ArXiv, 2022. URL: https://doi.org/10.53846/goediss-9438, doi:10.53846/goediss-9438. This article has 1 citations.

14. (bartsch2022hid1asa pages 131-134): Lydia Maximiliane Bartsch. Hid1 as a novel disease-causing gene in early onset neurological disorders: molecular, functional and phenotypic studies. ArXiv, 2022. URL: https://doi.org/10.53846/goediss-9438, doi:10.53846/goediss-9438. This article has 1 citations.

15. (bartsch2022hid1asa pages 106-114): Lydia Maximiliane Bartsch. Hid1 as a novel disease-causing gene in early onset neurological disorders: molecular, functional and phenotypic studies. ArXiv, 2022. URL: https://doi.org/10.53846/goediss-9438, doi:10.53846/goediss-9438. This article has 1 citations.

## Artifacts

- [Edison artifact artifact-00](CG8841-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. https://doi.org/10.1534/genetics.110.121996
2. https://doi.org/10.7554/eLife.18134
3. https://doi.org/10.1091/mbc.e17-08-0491
4. https://doi.org/10.53846/goediss-9438
5. https://doi.org/10.7554/elife.18134,
6. https://doi.org/10.53846/goediss-9438,
7. https://doi.org/10.1091/mbc.e17-08-0491,
8. https://doi.org/10.1534/genetics.110.121996,