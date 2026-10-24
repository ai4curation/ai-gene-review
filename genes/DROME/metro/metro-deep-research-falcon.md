---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T17:50:54.620846'
end_time: '2026-09-08T17:57:14.306733'
duration_seconds: 379.69
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: metro
  gene_symbol: metro
  uniprot_accession: A1Z8G0
  protein_description: 'SubName: Full=Menage a trois, isoform A {ECO:0000313|EMBL:AAF58707.3};'
  gene_info: Name=metro {ECO:0000313|EMBL:AAF58707.3, ECO:0000313|FlyBase:FBgn0050021};
    Synonyms=CG13219 {ECO:0000313|EMBL:AAF58707.3}, CG18338 {ECO:0000313|EMBL:AAF58707.3},
    Dmel\CG30021 {ECO:0000313|EMBL:AAF58707.3}, FBgn0050021 {ECO:0000313|EMBL:AAF58707.3},
    met {ECO:0000313|EMBL:AAF58707.3}, Metro {ECO:0000313|EMBL:AAF58707.3}; ORFNames=CG30021
    {ECO:0000313|EMBL:AAF58707.3, ECO:0000313|FlyBase:FBgn0050021}, Dmel_CG30021 {ECO:0000313|EMBL:AAF58707.3};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the MAGUK family.
  protein_domains: GK/Ca_channel_bsu. (IPR008145); Guanylate_kin-like_dom. (IPR008144);
    Guanylate_kinase_CS. (IPR020590); L27_C. (IPR014775); L27_dom. (IPR004172)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 3
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: metro-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** A1Z8G0
- **Protein Description:** SubName: Full=Menage a trois, isoform A {ECO:0000313|EMBL:AAF58707.3};
- **Gene Information:** Name=metro {ECO:0000313|EMBL:AAF58707.3, ECO:0000313|FlyBase:FBgn0050021}; Synonyms=CG13219 {ECO:0000313|EMBL:AAF58707.3}, CG18338 {ECO:0000313|EMBL:AAF58707.3}, Dmel\CG30021 {ECO:0000313|EMBL:AAF58707.3}, FBgn0050021 {ECO:0000313|EMBL:AAF58707.3}, met {ECO:0000313|EMBL:AAF58707.3}, Metro {ECO:0000313|EMBL:AAF58707.3}; ORFNames=CG30021 {ECO:0000313|EMBL:AAF58707.3, ECO:0000313|FlyBase:FBgn0050021}, Dmel_CG30021 {ECO:0000313|EMBL:AAF58707.3};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the MAGUK family.
- **Key Domains:** GK/Ca_channel_bsu. (IPR008145); Guanylate_kin-like_dom. (IPR008144); Guanylate_kinase_CS. (IPR020590); L27_C. (IPR014775); L27_dom. (IPR004172)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "metro" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'metro' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **metro** (gene ID: metro, UniProt: A1Z8G0) in DROME.

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
- **UniProt Accession:** A1Z8G0
- **Protein Description:** SubName: Full=Menage a trois, isoform A {ECO:0000313|EMBL:AAF58707.3};
- **Gene Information:** Name=metro {ECO:0000313|EMBL:AAF58707.3, ECO:0000313|FlyBase:FBgn0050021}; Synonyms=CG13219 {ECO:0000313|EMBL:AAF58707.3}, CG18338 {ECO:0000313|EMBL:AAF58707.3}, Dmel\CG30021 {ECO:0000313|EMBL:AAF58707.3}, FBgn0050021 {ECO:0000313|EMBL:AAF58707.3}, met {ECO:0000313|EMBL:AAF58707.3}, Metro {ECO:0000313|EMBL:AAF58707.3}; ORFNames=CG30021 {ECO:0000313|EMBL:AAF58707.3, ECO:0000313|FlyBase:FBgn0050021}, Dmel_CG30021 {ECO:0000313|EMBL:AAF58707.3};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the MAGUK family.
- **Key Domains:** GK/Ca_channel_bsu. (IPR008145); Guanylate_kin-like_dom. (IPR008144); Guanylate_kinase_CS. (IPR020590); L27_C. (IPR014775); L27_dom. (IPR004172)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "metro" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'metro' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **metro** (gene ID: metro, UniProt: A1Z8G0) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Drosophila melanogaster metro*

## Executive summary

The requested protein is correctly identified as **Metro/Ménage à trois**, encoded by ***Drosophila melanogaster metro*** (**CG30021; FBgn0050021; UniProt A1Z8G0**). This is not the unrelated juvenile-hormone receptor gene **Methoprene-tolerant (Met)** or a similarly named gene from another organism. The experimentally studied CG30021 product is an **MPP/p55-like membrane-associated guanylate kinase (MAGUK)** with tandem L27 domains and PDZ–SH3/HOOK–guanylate-kinase-like architecture, matching the supplied UniProt family/domain description. Its closest sequence similarities were reported to vertebrate MPP3, MPP4, and MPP7. (bachmann2010aperisynapticménage pages 4-6, bachmann2010aperisynapticménage pages 2-4)

Metro’s best-supported primary function is **not enzymatic catalysis**. It is a **postsynaptic/perisynaptic molecular scaffold** at larval glutamatergic neuromuscular junctions (NMJs). Through L27-domain interactions, Metro connects the neuronal Dlg isoform **DlgS97** to the adaptor **DLin-7**, stabilizing and positioning this complex in the muscle subsynaptic reticulum. The complex constrains synaptic-bouton architecture and organizes the dimensions and partitioning of postsynaptic glutamate-receptor fields. (bachmann2010aperisynapticménage pages 4-6, bachmann2010aperisynapticménage pages 1-2)

The evidence base is unusually narrow: the detailed mechanistic annotation derives predominantly from Bachmann *et al.*, published **28 April 2010** in *The Journal of Neuroscience* (DOI/URL: https://doi.org/10.1523/JNEUROSCI.0778-10.2010). Targeted searches did not identify a Metro-specific mechanistic study from 2023–2024. Accordingly, the current annotation should emphasize this strong but largely single-study evidence and should not extrapolate Dlg- or MPP-family findings automatically to Metro.

## 1. Identity verification and molecular classification

### 1.1 Correct gene and organism

The primary paper explicitly names **CG30021** as **Metro** and studies it genetically and biochemically in ***D. melanogaster*** larvae. CG30021 was identified in a search for proteins containing two L27 domains that could link DlgS97 with DLin-7. This correspondence supports the supplied mapping of metro/CG30021/FBgn0050021 to UniProt **A1Z8G0**. (bachmann2010aperisynapticménage pages 2-2, bachmann2010aperisynapticménage pages 2-4)

The short alias **met** is potentially hazardous because it can be confused with other genes. No findings concerning unrelated “MET” receptor tyrosine kinases, mammalian *MET*, or the fly Methoprene-tolerant pathway should be transferred to A1Z8G0.

### 1.2 Domain organization and isoforms

All predicted Metro variants in the foundational analysis contained **two L27 domains, one PDZ domain, an SH3/HOOK region, and a C-terminal guanylate-kinase-like (GUK) domain**. This agrees with the supplied InterPro annotations for L27 and guanylate-kinase-like domains and establishes Metro as an MPP/p55-like MAGUK. (bachmann2010aperisynapticménage pages 4-6, bachmann2010aperisynapticménage pages 2-4)

Northern blotting detected an approximately **3-kb transcript**. RT-PCR from third-instar larval body walls repeatedly recovered a predominant **556-amino-acid Metro-B** muscle isoform. The supplied UniProt description names isoform A, whereas the NMJ experiments principally characterized Metro-B; the functional evidence therefore should not be assumed to resolve every isoform-specific property of A1Z8G0. (bachmann2010aperisynapticménage pages 4-6)

### 1.3 Enzyme-versus-scaffold distinction

Despite the “guanylate kinase” family terminology, no nucleotide substrate, catalytic reaction, turnover measurement, or substrate specificity has been demonstrated for Metro. The direct study instead establishes protein–protein interactions and architectural phenotypes. The defensible annotation is therefore **MAGUK adaptor/scaffold**, not guanylate-kinase enzyme. The GUK-like domain may contribute to intramolecular or intermolecular organization, but its precise Metro-specific ligand and catalytic competence remain untested. (bachmann2010aperisynapticménage pages 4-6, bachmann2010aperisynapticménage pages 9-10)

## 2. Primary molecular function

Metro forms the middle component of a **DlgS97–Metro–DLin-7 scaffold**. GST pull-down experiments showed that Metro’s L27 region binds the N-terminal region of DlgS97 and that Metro also binds the L27 domain of DLin-7. Full-length Metro bound GST-DlgS97N, while immunoprecipitation of DLin-7 from larval body-wall extracts recovered an approximately **70-kDa Metro protein**, supporting formation of the complex in tissue as well as in vitro. (bachmann2010aperisynapticménage pages 4-6, bachmann2010aperisynapticménage pages 2-4)

Genetic dependence supports the same model. Loss of Metro or muscle-specific metro RNAi nearly eliminated junctional DLin-7, and muscle expression of Metro-B restored DLin-7. Conversely, DLin-7 loss left metro transcript detectable but eliminated Metro protein; raising Metro-B abundance without DLin-7 did not restore correct NMJ localization. Thus DLin-7 controls Metro stability/localization post-transcriptionally, while Metro is the direct molecular bridge connecting DLin-7 to DlgS97. (bachmann2010aperisynapticménage pages 4-6, bachmann2010aperisynapticménage pages 9-10)

Metro loss reduced junctional DlgS97 by **43%**, whereas Metro-B expression restored DlgS97 to **90.3% of wild-type levels**. These results support a reciprocal stabilization mechanism rather than a simple linear signaling cascade. The authors proposed that DLin-7 binding could enhance Metro–DlgS97 association allosterically, but that specific conformational mechanism remains inferential. (bachmann2010aperisynapticménage pages 9-10)

## 3. Cellular and subcellular localization

Immunofluorescence localized Metro prominently to **type-Ib boutons** and more weakly to type-Is boutons at third-instar larval NMJs. It is principally **postsynaptic**, within the muscle’s perisynaptic **subsynaptic reticulum (SSR)**, where it colocalizes with Dlg and DLin-7. Dlg-rich SSR membrane surrounds, rather than exactly coincides with, the glutamate-receptor-containing postsynaptic densities. Metro is therefore best understood as a perisynaptic organizer adjacent to receptor fields, not as a receptor subunit or extracellular ligand. (bachmann2010aperisynapticménage pages 4-6, bachmann2010aperisynapticménage pages 1-2)

Metro transcript was also detected in the developing central nervous system, and earlier expression evidence placed protein in muscle. Nevertheless, the strongest subcellular functional evidence concerns larval body-wall muscle NMJs. Adult-brain localization, epithelial functions, and organism-wide isoform distributions remain insufficiently characterized. (bachmann2010aperisynapticménage pages 2-2, bachmann2010aperisynapticménage pages 2-4)

## 4. Biological process and pathway context

The relevant pathway is best described as **synaptic-junction assembly and structural stabilization through an L27-domain MAGUK complex**, rather than a conventional kinase or second-messenger pathway. DlgS97 acts upstream in recruiting/stabilizing the Metro–DLin-7 module, while Metro provides the exclusive direct link between DlgS97 and DLin-7 at the tested NMJs. Spectrin-associated cytoskeletal structures may provide partial residual anchoring when DlgS97 is absent. (bachmann2010aperisynapticménage pages 10-11)

This complex regulates three related processes:

1. **Perisynaptic scaffold stability:** reciprocal stabilization and junctional targeting of DlgS97, Metro, and DLin-7.
2. **Bouton growth and morphology:** constraint of bouton size and prevention of irregular structural elaborations.
3. **Postsynaptic receptor-field organization:** control of glutamate-receptor-field size and separation without major disruption of basal neurotransmission. (bachmann2010aperisynapticménage pages 1-2, bachmann2010aperisynapticménage pages 7-9)

The absence of an enhanced phenotype in *dlgS97; metro* double mutants relative to the respective single mutants supports operation in a shared functional pathway, although genetic nonadditivity alone does not establish every molecular step. (bachmann2010aperisynapticménage pages 9-10)

## 5. Functional and quantitative evidence

### 5.1 Bouton morphology

Loss of Metro increased the projected area of type-Ib boutons by approximately **55%** relative to a wild-type mean of **4.14 µm²**. Mutant boutons were enlarged and irregular and exhibited corpuscular or synaptopod-like HRP staining. Ubiquitous Metro-B expression partially corrected bouton size and dispersion, supporting causality while indicating that rescue was incomplete. (bachmann2010aperisynapticménage pages 7-9)

### 5.2 Glutamate-receptor fields

Three-dimensional segmentation of GluRIID staining yielded mean receptor-field areas of **1.301 ± 0.114 µm²** in controls, **1.888 ± 0.160 µm²** in homozygous *metro* mutants (n=13), and **1.973 ± 0.462 µm²** in hemizygotes (n=12). Metro-B rescue reduced the value to **1.545 ± 0.154 µm²** (n=12). Some apparently enlarged fields were closely apposed receptor assemblies, suggesting that Metro contributes to field partitioning as well as gross size limitation. (bachmann2010aperisynapticménage pages 9-10, bachmann2010aperisynapticménage pages 7-9)

### 5.3 Active zones and ultrastructure

Bruchpilot-positive synaptic contacts were broadly preserved: **1,548 ± 96 versus 1,472 ± 132 contacts per 100,000 µm²** in the reported comparison. Electron microscopy found largely normal membrane contacts, electron densities, T-bars, and approximately **400–800-nm dense zones**, although abnormally juxtaposed zones occurred. Metro therefore has a stronger demonstrated role in postsynaptic/perisynaptic organization than in determining presynaptic active-zone abundance. (bachmann2010aperisynapticménage pages 9-10, bachmann2010aperisynapticménage pages 7-9)

### 5.4 Synaptic transmission

Structural abnormalities did not produce a major basal transmission defect under the conditions tested. Miniature-event frequencies were **1.25 ± 0.31 versus 1.19 ± 0.10 Hz**, and amplitudes were **0.91 ± 0.05 versus 0.83 ± 0.03 nA**. Evoked responses and quantal content were comparable; low-frequency increases in evoked current did not reach significance. This indicates that receptor-field enlargement can coexist with preserved local receptor density/composition and quantal transmission. It does not exclude defects under sustained activity, specialized plasticity paradigms, aging, or adult neural conditions. (bachmann2010aperisynapticménage pages 7-9)

The evidence and its limitations are summarized below.

| Annotation claim | Evidence/method | Quantitative result where available | Interpretation | Confidence/limitation |
|---|---|---|---|---|
| Correct identity and architecture | *Drosophila melanogaster* Metro was explicitly identified as CG30021 by BLAST screening for tandem-L27 proteins; sequence analysis found two L27 domains, one PDZ domain, an SH3/HOOK region, and a C-terminal guanylate-kinase-like domain. The predominant larval body-wall transcript encoded the 556-aa Metro-B isoform. (bachmann2010aperisynapticménage pages 4-6, bachmann2010aperisynapticménage pages 2-4) | Northern blot: one approximately 3-kb transcript; RT-PCR repeatedly recovered a 556-aa muscle isoform. | Matches metro/CG30021/FBgn0050021 and the supplied UniProt A1Z8G0 MAGUK annotation; supports classification as an MPP/p55-like scaffold. | High for CG30021 identity and domain organization. Exact correspondence of every reported isoform to UniProt isoform A was not independently resolved. |
| L27-mediated binding to DlgS97 and DLin-7 | GST pull-downs showed Metro’s L27 region binding the DlgS97 N terminus and DLin-7 L27 domain; full-length Metro bound GST-DlgS97N. DLin-7 immunoprecipitation from larval body-wall extracts recovered Metro. (bachmann2010aperisynapticménage pages 4-6, bachmann2010aperisynapticménage pages 2-4) | Co-immunoprecipitation detected an approximately 70-kDa Metro species. | Metro is the physical linker in a DlgS97–Metro–DLin-7 scaffold assembled through L27-domain interactions. | High: supported by in-vitro binding and tissue co-immunoprecipitation; complex stoichiometry and atomic structure remain unknown. |
| Postsynaptic/perisynaptic localization | Immunofluorescence detected Metro prominently at type-Ib and more weakly at type-Is larval NMJ boutons, postsynaptically within the perisynaptic subsynaptic reticulum, colocalizing with Dlg and DLin-7. (bachmann2010aperisynapticménage pages 4-6, bachmann2010aperisynapticménage pages 1-2) | No absolute concentration reported. | Metro acts on the muscle side of larval glutamatergic NMJs, primarily in the perisynaptic scaffold rather than as a core receptor-channel component. | High for larval NMJs; tissue-wide and adult localization remain poorly characterized. |
| Interdependent complex stabilization | metro null mutation or muscle-specific RNAi nearly abolished junctional DLin-7; Metro-B expression restored it. Metro loss reduced DlgS97, whereas DLin-7 loss eliminated detectable Metro protein despite retained metro transcript. Metro overexpression restored protein abundance but not junctional targeting without DLin-7. (bachmann2010aperisynapticménage pages 4-6, bachmann2010aperisynapticménage pages 9-10) | Junctional DlgS97 fell by 43% in metro mutants; Metro-B rescue restored it to 90.3% of wild type. | Metro, DLin-7, and DlgS97 mutually stabilize and localize a higher-order perisynaptic scaffold. | High: null/RNAi, biochemical, localization, and rescue evidence agree. Proposed allosteric enhancement remains an inference. |
| Bouton architecture | Confocal three-dimensional analysis of metro mutants found enlarged, irregular type-Ib boutons and corpuscular or synaptopod-like HRP staining; ubiquitous Metro-B partially rescued size and dispersion. (bachmann2010aperisynapticménage pages 7-9) | Mean type-Ib bouton projected area increased by 55% from a wild-type mean of 4.14 µm². | Metro constrains bouton size and supports orderly synaptic-junction morphology. | Moderate-to-high: direct mutant and rescue evidence, but rescue was partial. |
| Glutamate-receptor-field partitioning | Three-dimensional segmentation of GluRIID immunostaining showed enlarged or closely apposed receptor fields in metro mutants; Metro-B rescue reduced field size, and dlgS97;metro double mutants were not more severe than single mutants. (bachmann2010aperisynapticménage pages 9-10, bachmann2010aperisynapticménage pages 7-9) | Wild type: 1.301 ± 0.114 µm²; metro homozygote: 1.888 ± 0.160 µm², n=13; metro hemizygote: 1.973 ± 0.462 µm², n=12; rescue: 1.545 ± 0.154 µm², n=12. | The DlgS97–Metro–DLin-7 complex limits receptor-field dimensions and helps partition adjacent postsynaptic assemblies. | High for field enlargement. Incomplete Metro-B rescue suggests dosage effects or contributions from other isoforms. |
| Active-zone abundance broadly preserved | Bruchpilot-positive contacts were quantified by whole-NMJ three-dimensional reconstruction and spot detection; electron microscopy showed largely normal electron density, T-bars, and dense-zone dimensions despite occasional abnormal juxtaposition. (bachmann2010aperisynapticménage pages 9-10, bachmann2010aperisynapticménage pages 7-9) | Brp-positive contacts: 1,548 ± 96 versus 1,472 ± 132 per 100,000 µm²; dense zones were approximately 400–800 nm. | Metro primarily organizes postsynaptic/perisynaptic architecture rather than determining active-zone number. | Moderate-to-high; subtle nanoscale or activity-dependent presynaptic defects were not excluded. |
| Basal synaptic transmission largely preserved | Electrophysiological recordings found unchanged spontaneous-event frequency and amplitude and comparable evoked responses and quantal content; low-frequency EJC increases were nonsignificant. (bachmann2010aperisynapticménage pages 9-10, bachmann2010aperisynapticménage pages 7-9) | Mini frequency: 1.25 ± 0.31 versus 1.19 ± 0.10 Hz; mini amplitude: 0.91 ± 0.05 versus 0.83 ± 0.03 nA. | Structural receptor-field enlargement does not substantially alter basal quantal transmission under the tested conditions. | Moderate-to-high for larval NMJs; specialized plasticity paradigms and adult synapses were not comprehensively tested. |
| No demonstrated catalytic guanylate-kinase reaction | Metro contains a guanylate-kinase-like domain, but the direct study tested scaffold interactions and phenotypes rather than nucleotide turnover; no substrate, reaction, or catalytic assay was reported. (bachmann2010aperisynapticménage pages 4-6, bachmann2010aperisynapticménage pages 9-10) | None. | Metro should be annotated as a MAGUK adaptor/scaffold, not as a proven metabolic guanylate kinase. | High confidence that catalytic activity is unproven; absence of evidence does not formally exclude all catalytic capacity. |
| No identified 2023–2024 Metro-specific mechanistic update | Targeted searches centered on Metro/CG30021, DlgS97, DLin-7, MAGUK/MPP, and the Drosophila NMJ returned the foundational 2010 study rather than a recent Metro-focused primary study. | One directly relevant mechanistic primary study underpins most functional annotation. | Current understanding remains dominated by foundational larval-NMJ work; claims of newer Metro-specific functions would be premature. | Literature-availability limitation rather than biological evidence; indexing may miss work using unrecognized aliases. |


*Table: Evidence supporting annotation of Drosophila Metro as a postsynaptic/perisynaptic MAGUK scaffold linking DlgS97 and DLin-7. The table distinguishes direct biochemical, genetic, imaging, and electrophysiological results from inference and unresolved evidence gaps.*

## 6. Current applications and real-world relevance

Metro is presently a **research tool and model-system component**, not a clinical or biotechnological target with an established real-world deployment. Its practical value lies in using the genetically accessible larval NMJ to study:

- assembly of higher-order MAGUK scaffolds;
- L27-domain-mediated adaptor complexes;
- coupling between perisynaptic architecture and receptor-field organization;
- structural robustness of glutamatergic synapses despite preserved basal transmission.

Because Metro resembles vertebrate MPP-family proteins, the fly complex offers a comparative model for conserved DLG–MPP–LIN7 assemblies. However, the original sequence analysis found similarity to several MPP proteins, and functional equivalence to any single human paralog should not be asserted without orthology and rescue experiments. (bachmann2010aperisynapticménage pages 4-6)

## 7. Recent research status, expert interpretation, and evidence gaps

No directly relevant Metro/CG30021-focused mechanistic publication from **2023–2024** was identified in the targeted searches. The latest defensible interpretation therefore remains the foundational model: Metro is a junctional MPP-like scaffold whose L27 interactions stabilize a DlgS97–Metro–DLin-7 complex and organize larval NMJ morphology. The scarcity of independent follow-up is an important limitation, not evidence that the proposed function is incorrect.

Priority unresolved questions include:

- whether UniProt isoform A has the same localization and rescue capacity as experimentally emphasized Metro-B;
- the ligand and structural role of Metro’s PDZ and GUK-like domains;
- whether the GUK-like domain has any residual nucleotide-binding or catalytic activity;
- adult nervous-system, epithelial, and developmental functions;
- activity-dependent plasticity phenotypes not apparent in basal recordings;
- direct vertebrate orthology and functional conservation;
- endogenous complex stoichiometry and nanoscale arrangement.

## Conclusion

**Recommended primary annotation:** *Metro is a Drosophila MPP/p55-family MAGUK scaffold that localizes postsynaptically and perisynaptically in the larval neuromuscular-junction subsynaptic reticulum. Through tandem L27-domain interactions it links DlgS97 to DLin-7, stabilizing the junctional scaffold and constraining bouton morphology and postsynaptic glutamate-receptor-field organization.* (bachmann2010aperisynapticménage pages 4-6, bachmann2010aperisynapticménage pages 9-10, bachmann2010aperisynapticménage pages 7-9)

There is **no established catalytic reaction or substrate specificity** for Metro. Basal active-zone number and synaptic transmission remain largely intact after Metro loss, indicating that its clearest role is architectural organization and structural stabilization rather than direct neurotransmitter release or receptor conductance. (bachmann2010aperisynapticménage pages 9-10, bachmann2010aperisynapticménage pages 7-9)

## Principal source

Bachmann A, Kobler O, Kittel RJ, *et al.* **A Perisynaptic Ménage à Trois between Dlg, DLin-7, and Metro Controls Proper Organization of Drosophila Synaptic Junctions.** *Journal of Neuroscience*. Published **28 April 2010**;30(17):5811–5824. https://doi.org/10.1523/JNEUROSCI.0778-10.2010. (bachmann2010aperisynapticménage pages 1-2)

References

1. (bachmann2010aperisynapticménage pages 4-6): André Bachmann, Oliver Kobler, Robert J. Kittel, Carolin Wichmann, Jimena Sierralta, Stephan J. Sigrist, Eckart D. Gundelfinger, Elisabeth Knust, and Ulrich Thomas. A perisynaptic ménage à trois between dlg, dlin-7, and metro controls proper organization of drosophila synaptic junctions. The Journal of Neuroscience, 30:5811-5824, Apr 2010. URL: https://doi.org/10.1523/jneurosci.0778-10.2010, doi:10.1523/jneurosci.0778-10.2010. This article has 34 citations.

2. (bachmann2010aperisynapticménage pages 2-4): André Bachmann, Oliver Kobler, Robert J. Kittel, Carolin Wichmann, Jimena Sierralta, Stephan J. Sigrist, Eckart D. Gundelfinger, Elisabeth Knust, and Ulrich Thomas. A perisynaptic ménage à trois between dlg, dlin-7, and metro controls proper organization of drosophila synaptic junctions. The Journal of Neuroscience, 30:5811-5824, Apr 2010. URL: https://doi.org/10.1523/jneurosci.0778-10.2010, doi:10.1523/jneurosci.0778-10.2010. This article has 34 citations.

3. (bachmann2010aperisynapticménage pages 1-2): André Bachmann, Oliver Kobler, Robert J. Kittel, Carolin Wichmann, Jimena Sierralta, Stephan J. Sigrist, Eckart D. Gundelfinger, Elisabeth Knust, and Ulrich Thomas. A perisynaptic ménage à trois between dlg, dlin-7, and metro controls proper organization of drosophila synaptic junctions. The Journal of Neuroscience, 30:5811-5824, Apr 2010. URL: https://doi.org/10.1523/jneurosci.0778-10.2010, doi:10.1523/jneurosci.0778-10.2010. This article has 34 citations.

4. (bachmann2010aperisynapticménage pages 2-2): André Bachmann, Oliver Kobler, Robert J. Kittel, Carolin Wichmann, Jimena Sierralta, Stephan J. Sigrist, Eckart D. Gundelfinger, Elisabeth Knust, and Ulrich Thomas. A perisynaptic ménage à trois between dlg, dlin-7, and metro controls proper organization of drosophila synaptic junctions. The Journal of Neuroscience, 30:5811-5824, Apr 2010. URL: https://doi.org/10.1523/jneurosci.0778-10.2010, doi:10.1523/jneurosci.0778-10.2010. This article has 34 citations.

5. (bachmann2010aperisynapticménage pages 9-10): André Bachmann, Oliver Kobler, Robert J. Kittel, Carolin Wichmann, Jimena Sierralta, Stephan J. Sigrist, Eckart D. Gundelfinger, Elisabeth Knust, and Ulrich Thomas. A perisynaptic ménage à trois between dlg, dlin-7, and metro controls proper organization of drosophila synaptic junctions. The Journal of Neuroscience, 30:5811-5824, Apr 2010. URL: https://doi.org/10.1523/jneurosci.0778-10.2010, doi:10.1523/jneurosci.0778-10.2010. This article has 34 citations.

6. (bachmann2010aperisynapticménage pages 10-11): André Bachmann, Oliver Kobler, Robert J. Kittel, Carolin Wichmann, Jimena Sierralta, Stephan J. Sigrist, Eckart D. Gundelfinger, Elisabeth Knust, and Ulrich Thomas. A perisynaptic ménage à trois between dlg, dlin-7, and metro controls proper organization of drosophila synaptic junctions. The Journal of Neuroscience, 30:5811-5824, Apr 2010. URL: https://doi.org/10.1523/jneurosci.0778-10.2010, doi:10.1523/jneurosci.0778-10.2010. This article has 34 citations.

7. (bachmann2010aperisynapticménage pages 7-9): André Bachmann, Oliver Kobler, Robert J. Kittel, Carolin Wichmann, Jimena Sierralta, Stephan J. Sigrist, Eckart D. Gundelfinger, Elisabeth Knust, and Ulrich Thomas. A perisynaptic ménage à trois between dlg, dlin-7, and metro controls proper organization of drosophila synaptic junctions. The Journal of Neuroscience, 30:5811-5824, Apr 2010. URL: https://doi.org/10.1523/jneurosci.0778-10.2010, doi:10.1523/jneurosci.0778-10.2010. This article has 34 citations.

## Artifacts

- [Edison artifact artifact-00](metro-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. https://doi.org/10.1523/JNEUROSCI.0778-10.2010
2. https://doi.org/10.1523/JNEUROSCI.0778-10.2010.
3. https://doi.org/10.1523/jneurosci.0778-10.2010,