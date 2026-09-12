---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T17:58:07.117892'
end_time: '2026-09-08T18:04:53.044538'
duration_seconds: 405.93
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: Hmt-1
  gene_symbol: Hmt-1
  uniprot_accession: Q9VF20
  protein_description: 'RecName: Full=ATP-binding cassette sub-family B member 6 {ECO:0000256|ARBA:ARBA00024439};
    EC=7.6.2.5 {ECO:0000256|ARBA:ARBA00024385}; AltName: Full=ABC-type heme transporter
    ABCB6 {ECO:0000256|ARBA:ARBA00031413};'
  gene_info: Name=Hmt-1 {ECO:0000313|EMBL:AAF55241.1, ECO:0000313|FlyBase:FBgn0038376};
    Synonyms=ABCB6 {ECO:0000313|EMBL:AAF55241.1}, DmCG4225 {ECO:0000313|EMBL:AAF55241.1},
    Dmel\CG4225 {ECO:0000313|EMBL:AAF55241.1}, EP(3)3387 {ECO:0000313|EMBL:AAF55241.1},
    HMT-1 {ECO:0000313|EMBL:AAF55241.1}, hmt-1 {ECO:0000313|EMBL:AAF55241.1}; ORFNames=CG4225
    {ECO:0000313|EMBL:AAF55241.1, ECO:0000313|FlyBase:FBgn0038376}, Dmel_CG4225 {ECO:0000313|EMBL:AAF55241.1};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the ABC transporter superfamily. ABCB family.
  protein_domains: AAA+_ATPase. (IPR003593); ABC1_TM_dom. (IPR011527); ABC1_TM_sf.
    (IPR036640); ABC_transporter-like_ATP-bd. (IPR003439); ABC_transporter-like_CS.
    (IPR017871)
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
  path: Hmt-1-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q9VF20
- **Protein Description:** RecName: Full=ATP-binding cassette sub-family B member 6 {ECO:0000256|ARBA:ARBA00024439}; EC=7.6.2.5 {ECO:0000256|ARBA:ARBA00024385}; AltName: Full=ABC-type heme transporter ABCB6 {ECO:0000256|ARBA:ARBA00031413};
- **Gene Information:** Name=Hmt-1 {ECO:0000313|EMBL:AAF55241.1, ECO:0000313|FlyBase:FBgn0038376}; Synonyms=ABCB6 {ECO:0000313|EMBL:AAF55241.1}, DmCG4225 {ECO:0000313|EMBL:AAF55241.1}, Dmel\CG4225 {ECO:0000313|EMBL:AAF55241.1}, EP(3)3387 {ECO:0000313|EMBL:AAF55241.1}, HMT-1 {ECO:0000313|EMBL:AAF55241.1}, hmt-1 {ECO:0000313|EMBL:AAF55241.1}; ORFNames=CG4225 {ECO:0000313|EMBL:AAF55241.1, ECO:0000313|FlyBase:FBgn0038376}, Dmel_CG4225 {ECO:0000313|EMBL:AAF55241.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the ABC transporter superfamily. ABCB family.
- **Key Domains:** AAA+_ATPase. (IPR003593); ABC1_TM_dom. (IPR011527); ABC1_TM_sf. (IPR036640); ABC_transporter-like_ATP-bd. (IPR003439); ABC_transporter-like_CS. (IPR017871)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Hmt-1" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Hmt-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Hmt-1** (gene ID: Hmt-1, UniProt: Q9VF20) in DROME.

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
- **UniProt Accession:** Q9VF20
- **Protein Description:** RecName: Full=ATP-binding cassette sub-family B member 6 {ECO:0000256|ARBA:ARBA00024439}; EC=7.6.2.5 {ECO:0000256|ARBA:ARBA00024385}; AltName: Full=ABC-type heme transporter ABCB6 {ECO:0000256|ARBA:ARBA00031413};
- **Gene Information:** Name=Hmt-1 {ECO:0000313|EMBL:AAF55241.1, ECO:0000313|FlyBase:FBgn0038376}; Synonyms=ABCB6 {ECO:0000313|EMBL:AAF55241.1}, DmCG4225 {ECO:0000313|EMBL:AAF55241.1}, Dmel\CG4225 {ECO:0000313|EMBL:AAF55241.1}, EP(3)3387 {ECO:0000313|EMBL:AAF55241.1}, HMT-1 {ECO:0000313|EMBL:AAF55241.1}, hmt-1 {ECO:0000313|EMBL:AAF55241.1}; ORFNames=CG4225 {ECO:0000313|EMBL:AAF55241.1, ECO:0000313|FlyBase:FBgn0038376}, Dmel_CG4225 {ECO:0000313|EMBL:AAF55241.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the ABC transporter superfamily. ABCB family.
- **Key Domains:** AAA+_ATPase. (IPR003593); ABC1_TM_dom. (IPR011527); ABC1_TM_sf. (IPR036640); ABC_transporter-like_ATP-bd. (IPR003439); ABC_transporter-like_CS. (IPR017871)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Hmt-1" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Hmt-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Hmt-1** (gene ID: Hmt-1, UniProt: Q9VF20) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Research report: *Drosophila melanogaster* **Hmt-1** / CG4225 (UniProt Q9VF20)

## Executive conclusion

The identity is verified: the requested protein is **DmHMT-1**, encoded by *D. melanogaster* **CG4225/Hmt-1**, not the same-named HMT-1 proteins of *Caenorhabditis elegans* or *Schizosaccharomyces pombe*. Comparative genomic literature identifies CG4225 as the fly homolog of human **ABCB6** and classifies it as an **ABCB half-transporter**. This agrees with the supplied UniProt Q9VF20 description and its ABC transmembrane and ATP-binding domains. (jeong2014genomewideidentificationof pages 4-7, wu2019insectatpbindingcassette pages 5-7)

The most defensible primary functional annotation is:

> **DmHMT-1 is an ATP-coupled membrane ABCB half-transporter that promotes cadmium detoxification/tolerance. The exact transported chemical species and endogenous subcellular membrane in fly cells have not been established.**

Cadmium tolerance is supported by DmHMT-1-specific experiments, whereas “heme transporter,” mitochondrial porphyrin transport, obligatory phytochelatin transport, and native vacuolar localization are not directly established for the fly protein. Recent human ABCB6 structures make thiol-coordinated cadmium—especially Cd:GSH or Cd:phytochelatin complexes—a plausible substrate hypothesis, but this remains comparative rather than direct Drosophila evidence. (li2020transcriptionalresponseof pages 13-15, wu2019insectatpbindingcassette pages 14-16, choi2024cryoemstructureof pages 2-3, choi2024cryoemstructureof pages 1-2)

## 1. Identity and ambiguity control

**Verified identifiers** are UniProt **Q9VF20**, gene **Hmt-1**, locus **CG4225**, synonyms **DmHMT-1/ABCB6**, and organism ***Drosophila melanogaster***. A 2019 authoritative review explicitly states that CG4225 is the *D. melanogaster* homolog of human ABCB6 and is also known as DmHMT-1; independent arthropod comparative genomics places CG4225 with ABCB6-type half-transporters. (jeong2014genomewideidentificationof pages 4-7, wu2019insectatpbindingcassette pages 5-7)

The symbol is nevertheless biologically ambiguous across species. *C. elegans* HMT-1 and *S. pombe* SpHMT-1 are homologous proteins, not the target gene. Results from those organisms are used below only to explain conserved architecture or generate mechanistic hypotheses. In particular, direct oligomerization experiments discussed in the literature concern *C. elegans* HMT-1, not DmHMT-1. (kim2010thenterminalextension pages 1-2, kim2010thenterminalextension pages 2-4)

## 2. Protein class, domains, and transport mechanism

HMT-family proteins belong to the B branch of the ABC superfamily and have an unusual **half-molecule architecture**: one core transmembrane domain (TMD), one cytosolic nucleotide-binding domain (NBD/AAA+-type ATPase), and an N-terminal hydrophobic extension. Comparative topology models divide that extension into an accessory TMD0 and linker, followed by a six-span core TMD and the NBD. This architecture is explicitly described as conserved in proteins from fungi, worms, flies, rodents, and humans. (kim2010thenterminalextension pages 1-2, kim2010thenterminalextension pages 2-4)

The TMD is expected to recognize and translocate substrate, while the NBD binds and hydrolyzes ATP to power alternating-access transport. Because one HMT-1 polypeptide supplies only one TMD–NBD unit, a functional transporter should require homo- or hetero-oligomerization to create the canonical two-TMD/two-NBD assembly. *C. elegans* HMT-1 directly forms a protein complex and at least homodimerizes in heterologous assays; its N-terminal extension is required for oligomerization and cadmium-detoxification activity. These findings strongly motivate, but do not prove, an equivalent assembly for DmHMT-1. (kim2010thenterminalextension pages 1-2, kim2010thenterminalextension pages 2-4)

No purified DmHMT-1 ATPase or reconstituted-transport experiment was identified. Accordingly, **ATP coupling is strongly supported by conserved domains and ABC mechanism, but has not been measured directly for Q9VF20**.

## 3. Primary function and substrate specificity

### Directly supported function: cadmium tolerance

The pivotal Drosophila study is Sooksa-Nguan *et al.*, “Drosophila ABC transporter, DmHMT-1, confers tolerance to cadmium,” *Journal of Biological Chemistry* **284**, 354–362 (2009). Later reviews consistently identify it as the principal CG4225-specific functional study and conclude that DmHMT-1 confers cadmium resistance/tolerance. (wu2019insectatpbindingcassette pages 5-7, li2020transcriptionalresponseof pages 13-15, wu2019insectatpbindingcassette pages 14-16)

The available synthesis further reports **metal-selective phenotypes under the tested conditions**: DmHMT-1 provided tolerance to cadmium but not mercury or arsenite. This is narrower than *C. elegans* HMT-1, which has reported activity against cadmium, copper, and arsenite. The result should not be interpreted as proof that cadmium is DmHMT-1’s sole physiological substrate, because assay organism, expression level, metal speciation, and thiol availability can alter transporter phenotypes. (choi2024cryoemstructureof pages 1-2)

### What is physically transported?

The direct fly evidence establishes a detoxification phenotype, not molecular substrate identity. Plausible alternatives include free Cd²⁺, Cd–glutathione complexes, Cd–phytochelatin complexes, or another cadmium-containing conjugate. The 2009 work found that DmHMT-1 and SpHMT-1 were **not essential for vacuolar phytochelatin sequestration**, arguing against annotation as an obligatorily phytochelatin-dependent transporter. It does not exclude transport of selected Cd–thiol complexes under particular conditions. (li2020transcriptionalresponseof pages 13-15, wu2019insectatpbindingcassette pages 14-16)

Thus, “cadmium transporter” is a reasonable functional shorthand, but the more exact statement is **a transporter required or sufficient for cadmium detoxification whose transported cadmium species remains unresolved**.

## 4. Subcellular localization

DmHMT-1 is necessarily an integral membrane protein based on its multiple transmembrane segments. The important unresolved question is **which membrane it occupies endogenously in Drosophila**.

The primary study is reported to have observed DmHMT-1 at the **vacuolar membrane after heterologous expression in yeast**, where it suppressed cadmium hypersensitivity of an *S. pombe hmt-1* mutant. This supports membrane insertion and functional complementation, but it does not establish localization to a native fly organelle. No convincing endogenous Drosophila microscopy, biochemical fractionation, or organelle-proteomics validation was recovered. (li2020transcriptionalresponseof pages 13-15, wu2019insectatpbindingcassette pages 14-16)

Accordingly:

- **Supported:** integral membrane localization and heterologous targeting to the yeast vacuolar membrane.
- **Not established:** endogenous localization to fly lysosome-related organelles, mitochondria, plasma membrane, endoplasmic reticulum, or another compartment.
- **Interpretive model:** if DmHMT-1 resides on an acidic endolysosomal membrane, it could sequester cadmium away from the cytosol; if plasma-membrane localized, it could export cadmium. These alternatives require direct testing.

Human ABCB6 itself has had conflicting mitochondrial versus endolysosomal/plasma-membrane localization reports, reinforcing why localization should not be transferred to the fly ortholog solely by homology. (choi2024cryoemstructureof pages 1-2)

## 5. Biological pathway

The best-supported pathway is **cellular heavy-metal detoxification**, especially protection from cadmium toxicity. A mechanistic pathway model is:

1. Cytosolic cadmium associates with cellular thiols such as glutathione or related peptides.
2. DmHMT-1 recognizes cadmium or a cadmium-containing complex through its transmembrane cavity.
3. ATP binding and hydrolysis at the NBD drive conformational cycling.
4. Cadmium is moved across an organellar or cellular membrane, lowering its toxic cytosolic availability.

Steps 2–4 are mechanistically consistent with ABCB/HMT proteins, but direct transport direction, endogenous membrane, and substrate composition remain unmeasured for DmHMT-1. The finding that HMT proteins need not be essential for vacuolar phytochelatin sequestration indicates that cadmium tolerance and the canonical fungal phytochelatin-vacuole pathway are separable. (li2020transcriptionalresponseof pages 13-15, kim2010thenterminalextension pages 1-2)

### Heme and porphyrin metabolism

UniProt’s “ABC-type heme transporter ABCB6” wording should be treated as **family/orthology-based annotation**. Human ABCB6 was initially characterized in mitochondrial porphyrin transport and heme biosynthesis, although its localization and physiological roles remain complex. No direct evidence recovered here shows that DmHMT-1 transports heme, coproporphyrin III, or another porphyrin, or that its disruption alters fly heme biosynthesis. (choi2024cryoemstructureof pages 1-2)

Therefore, heme/porphyrin transport is a valuable experimental hypothesis—not the present primary functional assignment for Q9VF20.

## 6. Recent development: 2024 human ABCB6 mechanism

The most relevant recent advance is the May 2024 *Communications Biology* study by Choi *et al.*, DOI [10.1038/s42003-024-06377-1](https://doi.org/10.1038/s42003-024-06377-1). It resolved human ABCB6-core bound to Cd²⁺ plus glutathione at **3.2 Å** and Cd²⁺ plus phytochelatin-2 at **3.1 Å**. Two GSH molecules symmetrically coordinated Cd²⁺; in the PC2 complex, cysteines formed a tetrathiolate coordination environment. Both structures were inward-facing. (choi2024cryoemstructureof pages 2-3, choi2024cryoemstructureof pages 3-4, choi2024cryoemstructureof pages 1-2)

Functionally, Cd²⁺ alone and GSH alone did not stimulate human ABCB6-core ATPase activity, whereas Cd²⁺ in the presence of GSH produced an approximately **2.4-fold increase**, from **22 to 53 nmol·mg⁻¹·min⁻¹** at 800 μM Cd²⁺. The apparent Km for Cd:GSH was **108 ± 28 μM**, and measured binding Kd was **0.49 ± 0.05 mM**. A catalytically inactive E752Q variant lost Cd:GSH-stimulated ATPase activity. Overexpressed wild-type ABCB6-core also protected insect Sf9 cells: approximately **40% viability** remained at 50 μM Cd²⁺, whereas cells expressing E752Q showed substantial toxicity above 15 μM. (choi2024cryoemstructureof pages 2-3)

These data provide a compelling atomic mechanism by which an ABCB6-family protein can recognize thiol-coordinated cadmium and couple recognition to ATP hydrolysis. They do **not** demonstrate that DmHMT-1 transports Cd:GSH or Cd:PC2, because the experiments used human ABCB6-core. The appropriate current expert interpretation is that thiol-coordinated Cd is now the leading testable substrate class for purified DmHMT-1.

| Annotation question | Best conclusion | Evidence type/organism | Confidence/caveat |
|---|---|---|---|
| Identity | **Hmt-1 = CG4225 = DmHMT-1**, a *Drosophila melanogaster* homolog of human ABCB6; consistent with UniProt Q9VF20. | Comparative annotation and insect ABC-transporter review (wu2019insectatpbindingcassette pages 5-7) | **High.** Do not confuse it with HMT-1 genes studied in *C. elegans* or *S. pombe*. |
| Transporter architecture | An **ABCB half-transporter** with one core transmembrane domain, one nucleotide-binding domain, and an HMT-family N-terminal membrane extension; functional transport therefore likely requires oligomerization. | HMT-family architecture, explicitly including *Drosophila* (kim2010thenterminalextension pages 1-2, kim2010thenterminalextension pages 2-4) | **Moderate–high.** The domain assignment is strong, but DmHMT-1 topology and assembly have not been structurally resolved. |
| ATP coupling | Transport is expected to be driven by **ATP binding and hydrolysis** at the conserved ABC nucleotide-binding domain. | ABC/HMT-family mechanism and human ABCB6 biochemical evidence (kim2010thenterminalextension pages 1-2, choi2024cryoemstructureof pages 1-2, choi2024cryoemstructureof pages 2-3) | **Moderate.** Mechanistically compelling, but no purified DmHMT-1 ATPase or transport assay was identified. |
| Primary substrate/function | The best-supported function is **cadmium detoxification and tolerance**. Whether the transported species is free Cd²⁺ or a Cd–thiol complex remains unresolved. | Direct DmHMT-1 phenotype summarized from the 2009 primary study (wu2019insectatpbindingcassette pages 5-7, li2020transcriptionalresponseof pages 13-15, wu2019insectatpbindingcassette pages 14-16) | **High for cadmium tolerance; low–moderate for molecular substrate identity.** Tolerance alone does not prove direct Cd transport. |
| Metal specificity | DmHMT-1 reportedly provides tolerance to **cadmium**, but not **mercury or arsenite**, under the tested conditions. | DmHMT-1-specific experimental result summarized in a 2024 ABCB6 study (choi2024cryoemstructureof pages 1-2) | **Moderate.** This reflects the tested metals and assay conditions; it does not prove that Cd is the only physiological substrate. |
| Subcellular localization | **Native localization in fly cells remains unresolved.** Vacuolar-membrane localization was reported after expression in yeast, but this does not establish the endogenous fly compartment. | Heterologous yeast localization and complementation; no native-fly localization recovered (li2020transcriptionalresponseof pages 13-15, wu2019insectatpbindingcassette pages 14-16) | **Low–moderate.** Mitochondrial or lysosome-related localization should not be asserted without direct fly-cell evidence. |
| Phytochelatin relationship | DmHMT-1 and *S. pombe* HMT-1 were found **not to be essential for vacuolar phytochelatin sequestration**; an obligatory Cd–phytochelatin transport model is therefore unsupported for DmHMT-1. | Comparative functional conclusion from the 2009 study (li2020transcriptionalresponseof pages 13-15, wu2019insectatpbindingcassette pages 14-16) | **High for non-essentiality; unresolved for possible transport of particular thiol–Cd complexes.** |
| Oligomerization | DmHMT-1 probably functions as a **homo- or hetero-oligomer**, as expected for an ABC half-transporter. Related *C. elegans* HMT-1 forms a protein complex and can homodimerize. | Architecture-based inference plus direct *C. elegans* HMT-1 evidence (kim2010thenterminalextension pages 1-2, kim2010thenterminalextension pages 2-4) | **Moderate as family inference; low for the exact DmHMT-1 partner and stoichiometry.** No direct fly-protein oligomerization experiment was identified. |
| Porphyrin/heme role | **Porphyrin transport or a role in heme biosynthesis is unproven for DmHMT-1.** The hypothesis derives from homology to human ABCB6. | Human ABCB6 evidence, not direct fly evidence (choi2024cryoemstructureof pages 1-2) | **Low for DmHMT-1.** The UniProt “ABC-type heme transporter” description should be treated as family-based annotation rather than demonstrated fly function. |
| 2024 Cd–thiol structural mechanism | Human ABCB6 structures captured Cd²⁺ coordinated by **two GSH molecules at 3.2 Å** or **two PC2 molecules at 3.1 Å**. Cd:GSH increased ABCB6-core ATPase activity approximately **2.4-fold** at 800 μM Cd²⁺; apparent *K*ₘ was **108 ± 28 μM**. | Direct human ABCB6 cryo-EM and biochemical evidence, published May 2024 (choi2024cryoemstructureof pages 2-3, choi2024cryoemstructureof pages 1-2, choi2024cryoemstructureof pages 3-4) | **High for human ABCB6; comparative only for DmHMT-1.** It supports thiol-coordinated Cd as a testable fly-protein substrate but does not demonstrate DmHMT-1 transport of Cd:GSH or Cd:PC2. |


*Table: This table separates direct Drosophila findings from heterologous and ortholog-based inferences. It identifies cadmium detoxification as the strongest assignment while highlighting unresolved substrate chemistry, localization, oligomerization, and heme-related function.*

## 7. Current applications and real-world relevance

There is no established clinical, industrial, or agricultural deployment of DmHMT-1 itself. Its current value is chiefly as:

- a genetically tractable model of eukaryotic cadmium detoxification;
- a comparative system for understanding human ABCB6 substrate recognition and disease-associated function;
- a candidate biomarker or mechanistic component in insect heavy-metal toxicology;
- a potential tool for testing how membrane sequestration or efflux changes cadmium burden.

Broader insect ABC transporters are actively studied in xenobiotic detoxification and pesticide resistance, but those roles should not be assigned to DmHMT-1 without gene-specific experiments. The insect review identifies CG4225 specifically with cadmium resistance, while discussing pesticide transport largely for other ABC proteins. (wu2019insectatpbindingcassette pages 5-7)

## 8. Evidence-weighted annotation and research priorities

### Recommended functional annotation

**ATP-dependent ABCB half-transporter involved in cadmium detoxification; confers cadmium tolerance.** Likely functions as an oligomeric membrane transporter. The native fly compartment, transport direction, and precise substrate—free Cd²⁺ versus a Cd–thiol complex—are unknown.

### Confidence assessment

- **Gene/protein identity and ABCB-family membership:** high.
- **Cadmium-tolerance function:** high.
- **Direct cadmium translocation by DmHMT-1:** moderate; inferred from phenotype and family mechanism.
- **ATP dependence:** moderate-to-high mechanistically, but not directly assayed for purified fly protein.
- **Cd:GSH or Cd:phytochelatin as substrate:** plausible but unproven.
- **Native Drosophila localization:** unresolved.
- **Heme/porphyrin transport in Drosophila:** low-confidence orthology hypothesis.
- **Direct oligomerization of DmHMT-1:** probable but untested.

The decisive next experiments would be endogenous knock-in fluorescence plus organelle markers; tissue-specific loss-of-function under controlled Cd exposure; purification and proteoliposome transport assays comparing free Cd²⁺, Cd:GSH, Cd:PC2, heme, and coproporphyrin III; ATPase measurements with catalytic mutants; and direct determination of oligomeric state. These studies would convert the present phenotype-centered annotation into a substrate- and compartment-resolved mechanism.

## Key sources

1. **Sooksa-Nguan et al.** “Drosophila ABC transporter, DmHMT-1, confers tolerance to cadmium: DmHMT-1 and its yeast homolog, SpHMT-1, are not essential for vacuolar phytochelatin sequestration.” *Journal of Biological Chemistry* 284:354–362 (2009). Primary DmHMT-1 functional study, as identified by subsequent reviews. (li2020transcriptionalresponseof pages 13-15, wu2019insectatpbindingcassette pages 14-16)
2. **Kim, Selote & Vatamaniuk.** “The N-Terminal Extension Domain of the C. elegans Half-Molecule ABC Transporter, HMT-1, Is Required for Protein-Protein Interactions and Function.” Published September 23, 2010. [https://doi.org/10.1371/journal.pone.0012938](https://doi.org/10.1371/journal.pone.0012938). Comparative HMT architecture and oligomerization—not direct Drosophila evidence. (kim2010thenterminalextension pages 1-2, kim2010thenterminalextension pages 2-4)
3. **Wu et al.** “Insect ATP-Binding Cassette (ABC) Transporters: Roles in Xenobiotic Detoxification and Bt Insecticidal Activity.” Published June 2019. [https://doi.org/10.3390/ijms20112829](https://doi.org/10.3390/ijms20112829). Confirms CG4225/DmHMT-1 identity, ABCB context, and cadmium-resistance annotation. (wu2019insectatpbindingcassette pages 5-7)
4. **Choi et al.** “Cryo-EM structure of cadmium-bound human ABCB6.” Published May 2024. [https://doi.org/10.1038/s42003-024-06377-1](https://doi.org/10.1038/s42003-024-06377-1). Current structural and biochemical evidence for thiol-coordinated cadmium recognition by the human ortholog. (choi2024cryoemstructureof pages 2-3, choi2024cryoemstructureof pages 1-2)

No 2023–2024 DmHMT-1-specific primary study was identified in the retrieved literature; the 2024 advance pertains to human ABCB6 and is therefore used only as comparative mechanistic evidence.

References

1. (jeong2014genomewideidentificationof pages 4-7): Chang-Bum Jeong, Bo-Mi Kim, Jae-Seong Lee, and Jae-Sung Rhee. Genome-wide identification of whole atp-binding cassette (abc) transporters in the intertidal copepod tigriopus japonicus. BMC Genomics, Aug 2014. URL: https://doi.org/10.1186/1471-2164-15-651, doi:10.1186/1471-2164-15-651. This article has 51 citations and is from a peer-reviewed journal.

2. (wu2019insectatpbindingcassette pages 5-7): Chao Wu, Swapan Chakrabarty, Minghui Jin, Kaiyu Liu, and Yutao Xiao. Insect atp-binding cassette (abc) transporters: roles in xenobiotic detoxification and bt insecticidal activity. Jun 2019. URL: https://doi.org/10.3390/ijms20112829, doi:10.3390/ijms20112829. This article has 227 citations.

3. (li2020transcriptionalresponseof pages 13-15): Zhao Li, Tingwei Cai, Yao Qin, Yunhua Zhang, Ruoheng Jin, Kaikai Mao, Xun Liao, Hu Wan, and Jianhong Li. Transcriptional response of atp-binding cassette (abc) transporters to insecticide in the brown planthopper, nilaparvata lugens (stål). May 2020. URL: https://doi.org/10.3390/insects11050280, doi:10.3390/insects11050280. This article has 56 citations.

4. (wu2019insectatpbindingcassette pages 14-16): Chao Wu, Swapan Chakrabarty, Minghui Jin, Kaiyu Liu, and Yutao Xiao. Insect atp-binding cassette (abc) transporters: roles in xenobiotic detoxification and bt insecticidal activity. Jun 2019. URL: https://doi.org/10.3390/ijms20112829, doi:10.3390/ijms20112829. This article has 227 citations.

5. (choi2024cryoemstructureof pages 2-3): Seung Hun Choi, Sang Soo Lee, Hyeon You Lee, Subin Kim, Ji Won Kim, and Mi Sun Jin. Cryo-em structure of cadmium-bound human abcb6. Communications Biology, May 2024. URL: https://doi.org/10.1038/s42003-024-06377-1, doi:10.1038/s42003-024-06377-1. This article has 7 citations and is from a peer-reviewed journal.

6. (choi2024cryoemstructureof pages 1-2): Seung Hun Choi, Sang Soo Lee, Hyeon You Lee, Subin Kim, Ji Won Kim, and Mi Sun Jin. Cryo-em structure of cadmium-bound human abcb6. Communications Biology, May 2024. URL: https://doi.org/10.1038/s42003-024-06377-1, doi:10.1038/s42003-024-06377-1. This article has 7 citations and is from a peer-reviewed journal.

7. (kim2010thenterminalextension pages 1-2): Sungjin Kim, Devarshi S. Selote, and Olena K. Vatamaniuk. The n-terminal extension domain of the c. elegans half-molecule abc transporter, hmt-1, is required for protein-protein interactions and function. PLoS ONE, 5:e12938, Sep 2010. URL: https://doi.org/10.1371/journal.pone.0012938, doi:10.1371/journal.pone.0012938. This article has 20 citations and is from a peer-reviewed journal.

8. (kim2010thenterminalextension pages 2-4): Sungjin Kim, Devarshi S. Selote, and Olena K. Vatamaniuk. The n-terminal extension domain of the c. elegans half-molecule abc transporter, hmt-1, is required for protein-protein interactions and function. PLoS ONE, 5:e12938, Sep 2010. URL: https://doi.org/10.1371/journal.pone.0012938, doi:10.1371/journal.pone.0012938. This article has 20 citations and is from a peer-reviewed journal.

9. (choi2024cryoemstructureof pages 3-4): Seung Hun Choi, Sang Soo Lee, Hyeon You Lee, Subin Kim, Ji Won Kim, and Mi Sun Jin. Cryo-em structure of cadmium-bound human abcb6. Communications Biology, May 2024. URL: https://doi.org/10.1038/s42003-024-06377-1, doi:10.1038/s42003-024-06377-1. This article has 7 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Hmt-1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. choi2024cryoemstructureof pages 1-2
2. choi2024cryoemstructureof pages 2-3
3. wu2019insectatpbindingcassette pages 5-7
4. jeong2014genomewideidentificationof pages 4-7
5. li2020transcriptionalresponseof pages 13-15
6. wu2019insectatpbindingcassette pages 14-16
7. kim2010thenterminalextension pages 1-2
8. kim2010thenterminalextension pages 2-4
9. choi2024cryoemstructureof pages 3-4
10. 10.1038/s42003-024-06377-1
11. https://doi.org/10.1371/journal.pone.0012938
12. https://doi.org/10.3390/ijms20112829
13. https://doi.org/10.1038/s42003-024-06377-1
14. https://doi.org/10.1371/journal.pone.0012938](https://doi.org/10.1371/journal.pone.0012938
15. https://doi.org/10.3390/ijms20112829](https://doi.org/10.3390/ijms20112829
16. https://doi.org/10.1038/s42003-024-06377-1](https://doi.org/10.1038/s42003-024-06377-1
17. https://doi.org/10.1186/1471-2164-15-651,
18. https://doi.org/10.3390/ijms20112829,
19. https://doi.org/10.3390/insects11050280,
20. https://doi.org/10.1038/s42003-024-06377-1,
21. https://doi.org/10.1371/journal.pone.0012938,