---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T18:14:21.394881'
end_time: '2026-09-08T18:23:58.944562'
duration_seconds: 577.55
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: CSN5
  gene_symbol: CSN5
  uniprot_accession: A0A0B4KHM2
  protein_description: 'RecName: Full=COP9 signalosome complex subunit 5 {ECO:0000256|ARBA:ARBA00014880};'
  gene_info: Name=CSN5 {ECO:0000313|EMBL:AGB96019.1, ECO:0000313|FlyBase:FBgn0027053};
    Synonyms=BcDNA.LD14392 {ECO:0000313|EMBL:AGB96019.1}, BcDNA:LD14392 {ECO:0000313|EMBL:AGB96019.1},
    CH5 {ECO:0000313|EMBL:AGB96019.1}, CSN-5 {ECO:0000313|EMBL:AGB96019.1}, Csn5 {ECO:0000313|EMBL:AGB96019.1},
    csn5 {ECO:0000313|EMBL:AGB96019.1}, DCH5 {ECO:0000313|EMBL:AGB96019.1}, Dch5 {ECO:0000313|EMBL:AGB96019.1},
    dch5 {ECO:0000313|EMBL:AGB96019.1}, Dmel\CG14884 {ECO:0000313|EMBL:AGB96019.1},
    JAB1 {ECO:0000313|EMBL:AGB96019.1}, Jab1 {ECO:0000313|EMBL:AGB96019.1}, JAB1/CSN5
    {ECO:0000313|EMBL:AGB96019.1}, jab1/csn5 {ECO:0000313|EMBL:AGB96019.1}, JadBp
    {ECO:0000313|EMBL:AGB96019.1}, l(3)89Cf {ECO:0000313|EMBL:AGB96019.1}, l(3)L4032
    {ECO:0000313|EMBL:AGB96019.1}, l(3)M203 {ECO:0000313|EMBL:AGB96019.1}, Q9XZ58
    {ECO:0000313|EMBL:AGB96019.1}, quo {ECO:0000313|EMBL:AGB96019.1}; ORFNames=CG14884
    {ECO:0000313|EMBL:AGB96019.1, ECO:0000313|FlyBase:FBgn0027053}, Dmel_CG14884 {ECO:0000313|EMBL:AGB96019.1};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the peptidase M67A family. CSN5 subfamily.
  protein_domains: CSN5_C. (IPR040961); JAMM/MPN+_dom. (IPR000555); JAMM_MPN+_peptidase_M67A.
    (IPR050242); MPN. (IPR037518); CSN5_C (PF18323)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 16
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: CSN5-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** A0A0B4KHM2
- **Protein Description:** RecName: Full=COP9 signalosome complex subunit 5 {ECO:0000256|ARBA:ARBA00014880};
- **Gene Information:** Name=CSN5 {ECO:0000313|EMBL:AGB96019.1, ECO:0000313|FlyBase:FBgn0027053}; Synonyms=BcDNA.LD14392 {ECO:0000313|EMBL:AGB96019.1}, BcDNA:LD14392 {ECO:0000313|EMBL:AGB96019.1}, CH5 {ECO:0000313|EMBL:AGB96019.1}, CSN-5 {ECO:0000313|EMBL:AGB96019.1}, Csn5 {ECO:0000313|EMBL:AGB96019.1}, csn5 {ECO:0000313|EMBL:AGB96019.1}, DCH5 {ECO:0000313|EMBL:AGB96019.1}, Dch5 {ECO:0000313|EMBL:AGB96019.1}, dch5 {ECO:0000313|EMBL:AGB96019.1}, Dmel\CG14884 {ECO:0000313|EMBL:AGB96019.1}, JAB1 {ECO:0000313|EMBL:AGB96019.1}, Jab1 {ECO:0000313|EMBL:AGB96019.1}, JAB1/CSN5 {ECO:0000313|EMBL:AGB96019.1}, jab1/csn5 {ECO:0000313|EMBL:AGB96019.1}, JadBp {ECO:0000313|EMBL:AGB96019.1}, l(3)89Cf {ECO:0000313|EMBL:AGB96019.1}, l(3)L4032 {ECO:0000313|EMBL:AGB96019.1}, l(3)M203 {ECO:0000313|EMBL:AGB96019.1}, Q9XZ58 {ECO:0000313|EMBL:AGB96019.1}, quo {ECO:0000313|EMBL:AGB96019.1}; ORFNames=CG14884 {ECO:0000313|EMBL:AGB96019.1, ECO:0000313|FlyBase:FBgn0027053}, Dmel_CG14884 {ECO:0000313|EMBL:AGB96019.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the peptidase M67A family. CSN5 subfamily.
- **Key Domains:** CSN5_C. (IPR040961); JAMM/MPN+_dom. (IPR000555); JAMM_MPN+_peptidase_M67A. (IPR050242); MPN. (IPR037518); CSN5_C (PF18323)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CSN5" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CSN5' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CSN5** (gene ID: CSN5, UniProt: A0A0B4KHM2) in DROME.

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
- **UniProt Accession:** A0A0B4KHM2
- **Protein Description:** RecName: Full=COP9 signalosome complex subunit 5 {ECO:0000256|ARBA:ARBA00014880};
- **Gene Information:** Name=CSN5 {ECO:0000313|EMBL:AGB96019.1, ECO:0000313|FlyBase:FBgn0027053}; Synonyms=BcDNA.LD14392 {ECO:0000313|EMBL:AGB96019.1}, BcDNA:LD14392 {ECO:0000313|EMBL:AGB96019.1}, CH5 {ECO:0000313|EMBL:AGB96019.1}, CSN-5 {ECO:0000313|EMBL:AGB96019.1}, Csn5 {ECO:0000313|EMBL:AGB96019.1}, csn5 {ECO:0000313|EMBL:AGB96019.1}, DCH5 {ECO:0000313|EMBL:AGB96019.1}, Dch5 {ECO:0000313|EMBL:AGB96019.1}, dch5 {ECO:0000313|EMBL:AGB96019.1}, Dmel\CG14884 {ECO:0000313|EMBL:AGB96019.1}, JAB1 {ECO:0000313|EMBL:AGB96019.1}, Jab1 {ECO:0000313|EMBL:AGB96019.1}, JAB1/CSN5 {ECO:0000313|EMBL:AGB96019.1}, jab1/csn5 {ECO:0000313|EMBL:AGB96019.1}, JadBp {ECO:0000313|EMBL:AGB96019.1}, l(3)89Cf {ECO:0000313|EMBL:AGB96019.1}, l(3)L4032 {ECO:0000313|EMBL:AGB96019.1}, l(3)M203 {ECO:0000313|EMBL:AGB96019.1}, Q9XZ58 {ECO:0000313|EMBL:AGB96019.1}, quo {ECO:0000313|EMBL:AGB96019.1}; ORFNames=CG14884 {ECO:0000313|EMBL:AGB96019.1, ECO:0000313|FlyBase:FBgn0027053}, Dmel_CG14884 {ECO:0000313|EMBL:AGB96019.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the peptidase M67A family. CSN5 subfamily.
- **Key Domains:** CSN5_C. (IPR040961); JAMM/MPN+_dom. (IPR000555); JAMM_MPN+_peptidase_M67A. (IPR050242); MPN. (IPR037518); CSN5_C (PF18323)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CSN5" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CSN5' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CSN5** (gene ID: CSN5, UniProt: A0A0B4KHM2) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Drosophila melanogaster* CSN5

## Executive conclusion

The requested protein is correctly identified as *Drosophila melanogaster* COP9 signalosome subunit 5—CSN5/JAB1, encoded by **CG14884** and represented by UniProt **A0A0B4KHM2**. The accession-to-CG14884 mapping comes from the supplied UniProt record; the literature independently identifies fly CSN5/JAB1 as the catalytic CSN subunit. No conflicting *Drosophila* protein bearing this symbol was found. Its peptidase-M67A, MPN/JAMM+, and CSN5_C annotations are mechanistically coherent with the literature’s identification of CSN5 as a zinc-dependent JAMM isopeptidase (cope2003cop9signalosomea pages 2-3).

The primary molecular function is **deneddylation of cullins within cullin–RING ubiquitin ligases (CRLs)**. CSN5 hydrolyzes the isopeptide linkage between the ubiquitin-like modifier NEDD8 and a conserved lysine on a cullin:

**NEDD8–cullin + H₂O → NEDD8 + cullin.**

This reaction is not degradation of the cullin and is not ordinary deubiquitylation. Rather, it resets and protects CRL complexes, coordinating their assembly, substrate-receptor exchange, and ubiquitination cycles. In flies, a JAMM-mutant *csn5* cDNA fails to rescue lethality and photoreceptor differentiation, directly showing that the conserved catalytic center is biologically indispensable, although purified A0A0B4KHM2 itself has not been biochemically characterized in the retrieved literature (cope2003cop9signalosomea pages 2-3).

| Annotation dimension | Best-supported conclusion | Evidence type/species | Confidence and limitations |
|---|---|---|---|
| Identity | UniProt A0A0B4KHM2 corresponds to *Drosophila melanogaster* CSN5/JAB1, gene/ORF **CG14884**, the subunit-5 ortholog of the COP9 signalosome; literature independently identifies fly CSN5/JAB1 as a JAMM/MPN-domain COP9 component (harari‐steinberg2007cop9signalosomesubunit pages 1-2, cope2003cop9signalosomea pages 2-3) | Supplied UniProt mapping; *D. melanogaster* genetic and biochemical literature | **High.** Papers often use CSN5/JAB1 without printing the accession or CG identifier; no conflicting fly protein was found. |
| Catalytic reaction | In the COP9 complex, CSN5 is the zinc-dependent JAMM/MPN+ isopeptidase that hydrolyzes the bond joining NEDD8 to a conserved cullin lysine: NEDD8–cullin + H₂O → NEDD8 + cullin. JAMM-mutant fly CSN5 fails to rescue viability and photoreceptor differentiation (cope2003cop9signalosomea pages 2-3) | Direct fly catalytic-site rescue genetics; reaction chemistry established principally in other eukaryotes | **High for conserved function; moderate for fly-specific biochemistry.** The reaction was not demonstrated with purified A0A0B4KHM2 in the retrieved sources. |
| Substrate specificity | Physiological substrates are **NEDD8-modified cullins in cullin–RING ligases**, with CUL1/SCF the canonical example. CSN5 is not established as a broad deubiquitinase or as a protease directly cleaving downstream CRL substrates (cope2003cop9signalosomea pages 2-3, li2017rolesofmultifunctional pages 4-6, choo2011characterizationofthe pages 1-2) | Conserved biochemical mechanism; fly genetics supports JAMM dependence | **High for neddylated-cullin preference.** The relative efficiencies toward individual fly cullins have not been defined. |
| COP9-complex role | CSN5 supplies the catalytic center of the conserved eight-subunit COP9 signalosome, controlling CRL neddylation cycles and ubiquitin-dependent turnover. Fly **csn5-null** mutants retain an assembled residual CSN, indicating that CSN5 is crucial for function but not absolutely required for complex assembly (harari‐steinberg2007cop9signalosomesubunit pages 1-2) | Direct fly mutant analysis plus conserved CSN biochemistry | **High.** Free or low-molecular-weight CSN5 forms occur, but independent catalytic functions in flies remain insufficiently established. |
| Localization | In wild-type larvae, CSN5 is enriched in **plasmatocyte nuclei**, and immune challenge does not detectably alter that distribution. Functional effects also occur in larval fat body and peripheral neurons (harari‐steinberg2007cop9signalosomesubunit pages 4-6, djagaeva2009cop9limitsdendritic pages 2-4) | Direct fly immunolocalization and tissue-specific genetics | **High for plasmatocyte nuclear enrichment; moderate elsewhere.** This is not a comprehensive endogenous localization atlas. |
| Immunity and hematopoiesis | CSN5 restrains hemocyte proliferation and lamellocyte differentiation and regulates steady-state Cactus–Dorsal abundance/localization. Null larvae had about **2.14-fold more circulating hemocytes**, with lamellocytes comprising about **10%** of cells (899/8,307 across 11 larvae); bacterial challenge caused **40% mortality**. Signal-induced Cactus degradation and antimicrobial transcription remained possible (harari‐steinberg2007cop9signalosomesubunit pages 1-2, harari‐steinberg2007cop9signalosomesubunit pages 4-6, harari‐steinberg2007cop9signalosomesubunit pages 7-9) | Direct fly null-mutant, microscopy, cell-counting, infection, and transcriptional assays | **High for pathway phenotype.** Cactus and Dorsal are regulated downstream proteins, not demonstrated direct CSN5 enzymatic substrates; the responsible CRL was unresolved. |
| Neuronal Cullin3–Kelch pathway | In larval dendritic-arborization neurons, CSN/Cullin3 activity limits excessive branching by promoting turnover of the actin-crosslinking BTB protein Kelch. Kelch accumulates in **CSN5-mutant neurons**; Kelch overexpression increases branch ends by about **30%**, whereas kelch loss reduces ddaC dendritic area to approximately **82%** of wild type (djagaeva2009cop9limitsdendritic pages 2-4, djagaeva2009cop9limitsdendritic pages 4-6) | Direct fly mosaic genetics, immunostaining, interaction, overexpression, and epistasis | **Moderate-to-high.** Evidence connects CSN5 to Kelch abundance and CUL3 signaling, but CSN5 does not directly cleave Kelch; Kelch is a CRL ubiquitination/degradation target. |
| Recent-research gap | No 2023–2024 study directly recharacterizing A0A0B4KHM2/CG14884 was identified. A 2024 mouse embryonic-stem-cell study links CSN modulation to replication-fork protection, but does not establish that pathway in flies (xu2024smc56promotesreplication pages 1-2) | Recent comparative, non-fly research | **Low applicability to fly annotation.** Recent cross-species findings are hypothesis-generating; the most precise direct fly evidence remains older. |


*Table: Compact functional-annotation evidence for A0A0B4KHM2/CG14884, separating direct Drosophila experiments from conserved cross-species mechanisms. Confidence statements identify unresolved substrates, localization gaps, and the scarcity of recent fly-specific research.*

## 1. Identity and domain verification

The supplied record identifies A0A0B4KHM2 as *D. melanogaster* CSN5, with synonyms JAB1, CSN-5, DCH5, and ORF CG14884. This agrees with primary fly literature referring to the protein as CSN5/Jab1 and placing it in the conserved, eight-subunit COP9 signalosome. Fly *csn5*-null mutants retain a residual assembled CSN, indicating that CSN5 is not essential for the physical assembly of the remaining complex, but it supplies the complex’s catalytic deneddylase activity (harari‐steinberg2007cop9signalosomesubunit pages 1-2).

The listed **MPN**, **JAMM/MPN+**, and peptidase-M67A annotations are mutually consistent. The conserved JAMM motif contains histidine and aspartate residues that coordinate catalytic zinc; mutation of these residues abolishes deneddylation in biochemical model systems. Metal-chelator sensitivity further supports metallohydrolase chemistry. Importantly, the fly JAMM-mutant rescue failure connects that conserved chemistry to CSN5-dependent viability and neural differentiation in *Drosophila* (cope2003cop9signalosomea pages 2-3).

## 2. Primary biochemical function and substrate specificity

### Catalytic activity

CSN5 is the catalytic subunit of the COP9 signalosome’s NEDD8 isopeptidase. NEDD8 is attached through its C-terminal carboxyl group to the ε-amino group of a conserved cullin lysine. Cullin neddylation promotes the active CRL conformation and increases ubiquitin-transfer activity; CSN5 reverses that modification. Purified CSN cleaves NEDD8 from CUL1, and CSN-deficient fission yeast shift from a normal pool of approximately 10–40% neddylated CUL1 to essentially 100% neddylated CUL1, establishing that CSN is the dominant cullin deneddylase in vivo (cope2003cop9signalosomea pages 2-3).

### Physiological substrates

The defensible substrate annotation is **NEDD8-conjugated cullins assembled in CRLs**, canonically NEDD8–CUL1 in SCF ligases. The broader conserved substrate class includes CRLs based on other cullins, but relative catalytic efficiencies toward individual *Drosophila* cullins have not been measured in the retrieved studies. The evidence does not support annotating fly CSN5 as a broad deubiquitinase or as an enzyme that directly proteolyzes Cactus, Dorsal, Cyclin E, or Kelch. Those proteins are downstream CRL-regulated proteins, whereas CSN5’s direct chemical substrate is the NEDD8–cullin conjugate (li2017rolesofmultifunctional pages 4-6, choo2011characterizationofthe pages 1-2, cope2003cop9signalosomea pages 2-3).

### Requirement for the COP9 complex

The best-supported model is that productive deneddylation occurs in the holo-CSN context. The fly literature states that CSN5’s cullin-directed activity is expressed within the complex, even though CSN5 also occurs in smaller complexes or monomeric pools. Consequently, proposed “moonlighting” activities of free CSN5 should not be incorporated into the core annotation without direct fly evidence (harari‐steinberg2007cop9signalosomesubunit pages 1-2).

## 3. Cellular role: control of cullin–RING ubiquitin ligases

CRLs ubiquitinate selected regulatory proteins for proteasomal degradation. CSN5 does not simply turn these ligases off. Current mechanistic interpretation is that cycles of cullin neddylation and CSN-dependent deneddylation permit CRL remodeling, protect substrate receptors from autoubiquitylation, and allow ligase complexes to be reused or reconfigured. CSN preferentially engages active, neddylated CRL conformations; deneddylation then helps advance the ligase through its regulatory cycle (li2017rolesofmultifunctional pages 4-6, choo2011characterizationofthe pages 1-2).

This explains why loss of CSN5 can paradoxically cause accumulation rather than accelerated destruction of selected CRL substrates: constitutive cullin neddylation can destabilize CRL substrate receptors or prevent orderly ligase recycling. Thus, CSN5 is best regarded as a **CRL-cycle regulator and catalytic reset factor**, not merely a negative regulator of ubiquitination.

## 4. Subcellular and tissue localization

Direct localization evidence is tissue-dependent rather than a complete whole-animal atlas. In wild-type larval plasmatocytes, CSN5 and CSN7 are enriched in nuclei; bacterial immune challenge did not detectably change this distribution. Functional genetic evidence additionally places CSN5 action in larval fat body, circulating hemocytes, photoreceptor neurons, and peripheral dendritic-arborization neurons (harari‐steinberg2007cop9signalosomesubunit pages 4-6, djagaeva2009cop9limitsdendritic pages 2-4).

In fat-body cells, loss of CSN5 causes Cactus and Dorsal to accumulate together in nuclei, rather than demonstrating that CSN5 itself is exclusively nuclear there. In photoreceptors, reduced CSN5 activity impairs migration of glia into the lamina, consistent with a requirement in photoreceptor growth cones for production or presentation of a glial guidance signal; the precise molecular cue remains unresolved (harari‐steinberg2007cop9signalosomesubunit pages 7-9, cope2003cop9signalosomea pages 6-7).

## 5. Experimentally established pathways in *Drosophila*

### Toll–Cactus–Dorsal immunity and hematopoiesis

The most detailed fly-specific pathway study was published in February 2007: Harari-Steinberg et al., *Genes to Cells*, DOI [10.1111/j.1365-2443.2007.01049.x](https://doi.org/10.1111/j.1365-2443.2007.01049.x). In *csn5*-null larvae, Cactus protein was elevated without a corresponding increase in transcript and accumulated with Dorsal in nuclei. Nevertheless, Dorsal-dependent transcription remained repressed in unchallenged animals, showing that nuclear localization can be uncoupled from transcriptional activation. Following infection, Cactus could still be degraded and Drosomycin induced, indicating that CSN5 is not essential for the acute signal-triggered Toll response (harari‐steinberg2007cop9signalosomesubunit pages 1-2, harari‐steinberg2007cop9signalosomesubunit pages 4-6).

CSN5 instead controls the **steady-state abundance and compartmentalization** of Cactus–Dorsal and strongly restrains cellular immune development. Null larvae had approximately **2.14-fold more circulating hemocytes** than wild type; lamellocytes constituted about **10%** of circulating cells—899 of 8,307 cells counted from 11 larvae—despite being rare in unchallenged wild-type animals. Mutants developed massive melanotic capsules, failed to pupariate, and died as 10–13-day-old larvae. Bacterial challenge caused **40% mortality** under conditions that did not reduce wild-type survival (harari‐steinberg2007cop9signalosomesubunit pages 1-2, harari‐steinberg2007cop9signalosomesubunit pages 4-6).

These data support roles in hemocyte proliferation, lamellocyte differentiation, and cellular immunity. They do **not** establish Cactus or Dorsal as direct CSN5 enzymatic substrates, nor identify the relevant CRL with certainty.

### Cullin3–Kelch control of dendritic morphogenesis

A second precise pathway was reported in October 2009: Djagaeva and Doronkin, *PLoS ONE*, DOI [10.1371/journal.pone.0007598](https://doi.org/10.1371/journal.pone.0007598). In larval peripheral nervous-system neurons, COP9 signaling has dual cullin-dependent effects: a CUL1 arm promotes branching, whereas a CUL3 arm prevents excessive arborization. The CUL3 pathway controls the abundance of Kelch, an actin-crosslinking BTB-domain protein. Kelch accumulated strongly in *cul3*-mutant neurons and specifically in CSN5-mutant neurons while remaining nearly undetectable in adjacent non-mutant cells (djagaeva2009cop9limitsdendritic pages 2-4, djagaeva2009cop9limitsdendritic pages 4-6).

Kelch overexpression increased dendritic branch ends by approximately **30%** and mimicked *cul3* loss; *kelch* loss reduced ddaC dendritic area to about **82% of wild type**. Double-mutant and overexpression experiments supported Kelch as a major CUL3-regulated determinant of arbor complexity. For example, ddaF terminal ends rose from 189.7 ± 39.7 in wild type to 274 ± 54.6 after *cul3* loss, 284 ± 47.6 with Kelch overexpression, and 589.7 ± 305.4 when the perturbations were combined (djagaeva2009cop9limitsdendritic pages 4-6, djagaeva2009cop9limitsdendritic pages 6-8, djagaeva2009cop9limitsdendritic pages 8-10).

The mechanistic interpretation is indirect: CSN5 deneddylates and regulates CUL3 ligase cycling; the CUL3 machinery ubiquitinates Kelch or controls its turnover; Kelch then changes actin organization and dendritic branching. CSN5 does not directly cleave Kelch.

### Development, oogenesis, and photoreceptor differentiation

Fly *csn5*-null animals are larval-lethal and show oogenesis and photoreceptor-neuron differentiation defects. Oogenesis phenotypes include activation of a DNA-double-strand-break-dependent meiotic checkpoint and failure of normal oocyte patterning. Accumulation of SCF substrates such as Cyclin E has been proposed as a contributing mechanism, but the precise ligase/substrate chain was not fully resolved in the retrieved evidence (cope2003cop9signalosomea pages 6-7, cope2003cop9signalosomea pages 1-2).

## 6. Recent developments, 2023–2024

No 2023–2024 primary publication directly recharacterizing A0A0B4KHM2/CG14884 was identified. Therefore, older fly genetics remains more authoritative for this specific annotation than newer work in other organisms.

A January 12, 2024 mouse embryonic-stem-cell study showed that SMC5/6 negatively modulates CSN to preserve CRL activity and recruitment of replication-fork protection factors during fork restart: Xu and Jordan, *International Journal of Molecular Sciences*, DOI [10.3390/ijms25020952](https://doi.org/10.3390/ijms25020952). This expands current understanding of how CSN activity can be locally tuned, but it does not establish a replication-fork function for fly CSN5 (xu2024smc56promotesreplication pages 1-2).

A March 2024 *C. elegans* study reported that CSN-5 stabilizes FBF-1 and FBF-2 PUF proteins through a combination of COP9-dependent and partly COP9-independent mechanisms: Osterli et al., *Genetics*, DOI [10.1093/genetics/iyae033](https://doi.org/10.1093/genetics/iyae033). This supports the possibility of conserved noncanonical CSN5 interactions, but FBF proteins must not be annotated as substrates or partners of *Drosophila* CSN5 without fly experiments.

## 7. Current applications and real-world implementation

For *Drosophila* research, CSN5 is an experimentally useful node for manipulating the neddylation–CRL axis in vivo. Mosaic loss-of-function and tissue-specific perturbation permit analysis of cell-autonomous CRL regulation in neurons, blood cells, fat body, and developing visual circuits. Readouts already validated in flies include Kelch accumulation and dendritic architecture, Cactus/Dorsal localization, hemocyte abundance and identity, melanotic-capsule formation, infection survival, oogenesis, and photoreceptor/glial development (harari‐steinberg2007cop9signalosomesubunit pages 4-6, cope2003cop9signalosomea pages 6-7, djagaeva2009cop9limitsdendritic pages 2-4).

In translational systems, CSN5 is pharmacologically tractable because its JAMM active site can be inhibited, making CSN5 inhibitors useful probes of CRL dynamics and candidate anticancer agents. That application concerns mammalian CSN5 and should not be interpreted as a validated therapeutic use of the fly protein. The fly system’s practical value is chiefly as a genetically accessible model for assessing organismal consequences and tissue selectivity of CSN/CRL perturbation.

## 8. Expert assessment and annotation confidence

The strongest annotation is:

> **Catalytic COP9 signalosome subunit and JAMM-family zinc isopeptidase that removes NEDD8 from cullins, thereby regulating cullin–RING ubiquitin-ligase cycling and downstream proteasomal turnover.**

Confidence is **high** for identity, COP9 membership, JAMM dependence, essential developmental function, and regulation of cullin-based proteolysis. Confidence is **moderate-to-high** for the fly CUL3–Kelch pathway because genetics, accumulation, physical interaction, and epistasis converge, although the complete neuronal CRL composition is unresolved. Confidence is **high** for nuclear enrichment in plasmatocytes but only **moderate** for generalized cellular localization because comprehensive endogenous mapping is lacking. Proposed free-CSN5 signaling functions, individual fly-cullin preferences, and recent non-fly pathways should remain unannotated or explicitly labeled as comparative inference.

Overall, A0A0B4KHM2 is not an ambiguous alternative “CSN5”: all available organism, nomenclature, domain, and functional evidence aligns with *D. melanogaster* CG14884/CSN5/JAB1.

References

1. (cope2003cop9signalosomea pages 2-3): Gregory A Cope and Raymond J Deshaies. Cop9 signalosome a multifunctional regulator of scf and other cullin-based ubiquitin ligases. Cell, 114:663-671, Sep 2003. URL: https://doi.org/10.1016/s0092-8674(03)00722-0, doi:10.1016/s0092-8674(03)00722-0. This article has 528 citations and is from a highest quality peer-reviewed journal.

2. (harari‐steinberg2007cop9signalosomesubunit pages 1-2): Orit Harari‐Steinberg, Rafael Cantera, Simona Denti, Elisabetta Bianchi, Efrat Oron, Daniel Segal, and Daniel A Chamovitz. Cop9 signalosome subunit 5 (csn5/jab1) regulates the development of the drosophila immune system: effects on cactus, dorsal and hematopoiesis. Genes to Cells, 12:183-195, Feb 2007. URL: https://doi.org/10.1111/j.1365-2443.2007.01049.x, doi:10.1111/j.1365-2443.2007.01049.x. This article has 40 citations and is from a peer-reviewed journal.

3. (li2017rolesofmultifunctional pages 4-6): Ping Li, Longxiang Xie, Yinzhong Gu, Jiang Li, and Jianping Xie. Roles of multifunctional cop9 signalosome complex in cell fate and implications for drug discovery. Journal of Cellular Physiology, 232:1246-1253, Jun 2017. URL: https://doi.org/10.1002/jcp.25696, doi:10.1002/jcp.25696. This article has 20 citations and is from a peer-reviewed journal.

4. (choo2011characterizationofthe pages 1-2): Yin Yin Choo, Boon Kim Boh, Jessica Jie Wei Lou, Jolane Eng, Yee Chin Leck, Benjamin Anders, Peter G. Smith, and Thilo Hagen. Characterization of the role of cop9 signalosome in regulating cullin e3 ubiquitin ligase activity. Molecular Biology of the Cell, 22:4706-4715, Dec 2011. URL: https://doi.org/10.1091/mbc.e11-03-0251, doi:10.1091/mbc.e11-03-0251. This article has 23 citations and is from a domain leading peer-reviewed journal.

5. (harari‐steinberg2007cop9signalosomesubunit pages 4-6): Orit Harari‐Steinberg, Rafael Cantera, Simona Denti, Elisabetta Bianchi, Efrat Oron, Daniel Segal, and Daniel A Chamovitz. Cop9 signalosome subunit 5 (csn5/jab1) regulates the development of the drosophila immune system: effects on cactus, dorsal and hematopoiesis. Genes to Cells, 12:183-195, Feb 2007. URL: https://doi.org/10.1111/j.1365-2443.2007.01049.x, doi:10.1111/j.1365-2443.2007.01049.x. This article has 40 citations and is from a peer-reviewed journal.

6. (djagaeva2009cop9limitsdendritic pages 2-4): Inna Djagaeva and Sergey Doronkin. Cop9 limits dendritic branching via cullin3-dependent degradation of the actin-crosslinking btb-domain protein kelch. PLoS ONE, 4:e7598, Oct 2009. URL: https://doi.org/10.1371/journal.pone.0007598, doi:10.1371/journal.pone.0007598. This article has 38 citations and is from a peer-reviewed journal.

7. (harari‐steinberg2007cop9signalosomesubunit pages 7-9): Orit Harari‐Steinberg, Rafael Cantera, Simona Denti, Elisabetta Bianchi, Efrat Oron, Daniel Segal, and Daniel A Chamovitz. Cop9 signalosome subunit 5 (csn5/jab1) regulates the development of the drosophila immune system: effects on cactus, dorsal and hematopoiesis. Genes to Cells, 12:183-195, Feb 2007. URL: https://doi.org/10.1111/j.1365-2443.2007.01049.x, doi:10.1111/j.1365-2443.2007.01049.x. This article has 40 citations and is from a peer-reviewed journal.

8. (djagaeva2009cop9limitsdendritic pages 4-6): Inna Djagaeva and Sergey Doronkin. Cop9 limits dendritic branching via cullin3-dependent degradation of the actin-crosslinking btb-domain protein kelch. PLoS ONE, 4:e7598, Oct 2009. URL: https://doi.org/10.1371/journal.pone.0007598, doi:10.1371/journal.pone.0007598. This article has 38 citations and is from a peer-reviewed journal.

9. (xu2024smc56promotesreplication pages 1-2): Michelle J. Xu and Philip W. Jordan. Smc5/6 promotes replication fork stability via negative regulation of the cop9 signalosome. Jan 2024. URL: https://doi.org/10.3390/ijms25020952, doi:10.3390/ijms25020952. This article has 6 citations.

10. (cope2003cop9signalosomea pages 6-7): Gregory A Cope and Raymond J Deshaies. Cop9 signalosome a multifunctional regulator of scf and other cullin-based ubiquitin ligases. Cell, 114:663-671, Sep 2003. URL: https://doi.org/10.1016/s0092-8674(03)00722-0, doi:10.1016/s0092-8674(03)00722-0. This article has 528 citations and is from a highest quality peer-reviewed journal.

11. (djagaeva2009cop9limitsdendritic pages 6-8): Inna Djagaeva and Sergey Doronkin. Cop9 limits dendritic branching via cullin3-dependent degradation of the actin-crosslinking btb-domain protein kelch. PLoS ONE, 4:e7598, Oct 2009. URL: https://doi.org/10.1371/journal.pone.0007598, doi:10.1371/journal.pone.0007598. This article has 38 citations and is from a peer-reviewed journal.

12. (djagaeva2009cop9limitsdendritic pages 8-10): Inna Djagaeva and Sergey Doronkin. Cop9 limits dendritic branching via cullin3-dependent degradation of the actin-crosslinking btb-domain protein kelch. PLoS ONE, 4:e7598, Oct 2009. URL: https://doi.org/10.1371/journal.pone.0007598, doi:10.1371/journal.pone.0007598. This article has 38 citations and is from a peer-reviewed journal.

13. (cope2003cop9signalosomea pages 1-2): Gregory A Cope and Raymond J Deshaies. Cop9 signalosome a multifunctional regulator of scf and other cullin-based ubiquitin ligases. Cell, 114:663-671, Sep 2003. URL: https://doi.org/10.1016/s0092-8674(03)00722-0, doi:10.1016/s0092-8674(03)00722-0. This article has 528 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](CSN5-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. li2017rolesofmultifunctional pages 4-6
2. choo2011characterizationofthe pages 1-2
3. 10.1111/j.1365-2443.2007.01049.x
4. 10.1371/journal.pone.0007598
5. 10.3390/ijms25020952
6. 10.1093/genetics/iyae033
7. https://doi.org/10.1111/j.1365-2443.2007.01049.x
8. https://doi.org/10.1371/journal.pone.0007598
9. https://doi.org/10.3390/ijms25020952
10. https://doi.org/10.1093/genetics/iyae033
11. https://doi.org/10.1016/s0092-8674(03
12. https://doi.org/10.1111/j.1365-2443.2007.01049.x,
13. https://doi.org/10.1002/jcp.25696,
14. https://doi.org/10.1091/mbc.e11-03-0251,
15. https://doi.org/10.1371/journal.pone.0007598,
16. https://doi.org/10.3390/ijms25020952,