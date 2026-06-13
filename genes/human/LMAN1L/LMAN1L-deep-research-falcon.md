---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-12T04:04:14.094768'
end_time: '2026-06-12T04:18:55.911842'
duration_seconds: 881.82
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: LMAN1L
  gene_symbol: LMAN1L
  uniprot_accession: Q9HAT1
  protein_description: 'RecName: Full=Protein ERGIC-53-like; AltName: Full=ERGIC53-like
    protein; AltName: Full=Lectin mannose-binding 1-like; Short=LMAN1-like protein;
    Flags: Precursor;'
  gene_info: Name=LMAN1L; Synonyms=ERGL; ORFNames=UNQ2784/PRO7174;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: ConA-like_dom_sf. (IPR013320); Intracellular_Lectin-GPT. (IPR051136);
    Lectin_leg. (IPR005052); Lectin_leg-like (PF03388)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 16
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 2
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: LMAN1L-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: LMAN1L-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: image-1.png
  path: LMAN1L-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: '## Context ID: pqac-00000009 The overall architecture and domain organization
    of the full-length ERGIC-53 tetramer in complex with MCFD2 is shown in this cryo-E'
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9HAT1
- **Protein Description:** RecName: Full=Protein ERGIC-53-like; AltName: Full=ERGIC53-like protein; AltName: Full=Lectin mannose-binding 1-like; Short=LMAN1-like protein; Flags: Precursor;
- **Gene Information:** Name=LMAN1L; Synonyms=ERGL; ORFNames=UNQ2784/PRO7174;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ConA-like_dom_sf. (IPR013320); Intracellular_Lectin-GPT. (IPR051136); Lectin_leg. (IPR005052); Lectin_leg-like (PF03388)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "LMAN1L" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'LMAN1L' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **LMAN1L** (gene ID: LMAN1L, UniProt: Q9HAT1) in human.

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
- **UniProt Accession:** Q9HAT1
- **Protein Description:** RecName: Full=Protein ERGIC-53-like; AltName: Full=ERGIC53-like protein; AltName: Full=Lectin mannose-binding 1-like; Short=LMAN1-like protein; Flags: Precursor;
- **Gene Information:** Name=LMAN1L; Synonyms=ERGL; ORFNames=UNQ2784/PRO7174;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ConA-like_dom_sf. (IPR013320); Intracellular_Lectin-GPT. (IPR051136); Lectin_leg. (IPR005052); Lectin_leg-like (PF03388)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "LMAN1L" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'LMAN1L' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **LMAN1L** (gene ID: LMAN1L, UniProt: Q9HAT1) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Research report: Human **LMAN1L** (UniProt **Q9HAT1**; gene **LMAN1L**, synonym **ERGL**) — functional annotation with evidence grading

### 0) Executive summary (evidence-graded)
* **High-confidence identity:** LMAN1L is a distinct human gene/protein (Ensembl ENSG00000140506; “lectin, mannose binding 1 like”) and is explicitly named as a member of the **animal L‑type lectin** family (LMAN1/ERGIC‑53, LMAN1L, LMAN2/VIP36, LMAN2L/VIPL). (OpenTargets Search: -LMAN1L, baines2007receptormediatedproteintransport pages 4-6)
* **Direct functional data gap:** Within the retrieved full-text corpus, **no primary study directly characterizes** LMAN1L’s cargo, binding partners, or subcellular localization. Therefore, most mechanistic statements below are **explicitly labeled as inference** from the closest, well-studied paralog **LMAN1/ERGIC‑53** and general cargo-receptor biology. (baines2007receptormediatedproteintransport pages 4-6, zhang2023mammaliancargoreceptors pages 4-5)
* **Most likely function (inference):** By family membership and domain annotation supplied in the prompt (legume/ConA‑like lectin domain), LMAN1L is most plausibly an **early secretory pathway lectin/cargo receptor or lectin-like chaperone**, acting in **ER↔ERGIC↔cis-Golgi** trafficking and binding selected glycoprotein cargoes via **high‑mannose N‑glycans** in a **Ca2+/pH‑sensitive** manner. This inference is grounded in mechanistic and structural work on LMAN1. (zhang2023mammaliancargoreceptors pages 4-5, zhang2023mammaliancargoreceptors pages 3-3, ergicUnknownyearvaijayantidas pages 31-37, das2012structuralbasisofa pages 25-31)
* **Recent structural advance (2024, paralog evidence):** Cryo‑EM resolved full-length **ERGIC‑53/LMAN1** in complex with **MCFD2**, defining a tetrameric architecture with a clover-like head and long coiled-coil stalk—useful as a structural analog for LMAN1L. (watanabe2024structureoffulllength media 33178de8)
* **Human genetics/traits (database-level association):** OpenTargets aggregates evidence linking LMAN1L to complex traits including hypertension, alcohol drinking, and osteoarthritis; these are **association signals** rather than mechanism-resolving functional studies. (OpenTargets Search: -LMAN1L)

### 1) Key concepts and definitions (current understanding)
#### 1.1 ER-to-Golgi cargo receptors and the ERGIC
Proteins entering the secretory pathway are synthesized in the ER, packaged into COPII vesicles, and delivered to the **ER–Golgi intermediate compartment (ERGIC)** before reaching the cis-Golgi. Cargo receptors typically **cycle** between ER and ERGIC/cis-Golgi: they capture cargo in the ER and are retrieved back to the ER after cargo unloading. (baines2007receptormediatedproteintransport pages 1-2, zhang2023mammaliancargoreceptors pages 3-3)

A canonical, well-defined mammalian cargo receptor complex is **LMAN1–MCFD2**, established as required for efficient secretion of specific soluble glycoproteins such as coagulation factors V and VIII. (baines2007receptormediatedproteintransport pages 1-2, baines2007receptormediatedproteintransport pages 4-6, zhang2023mammaliancargoreceptors pages 4-5)

#### 1.2 Animal L-type lectins (LMAN family)
A foundational review explicitly frames **LMAN1 (ERGIC‑53)** as part of a larger family of related animal L‑type lectins including **LMAN1L**, **LMAN2 (VIP36)**, and **LMAN2L (VIPL)**; some members (LMAN2 and LMAN2L) had been proposed to function in cargo transport. (baines2007receptormediatedproteintransport pages 4-6)

**Interpretation for LMAN1L:** This family context is the strongest direct evidence that LMAN1L should be interpreted within secretory pathway lectin/cargo receptor biology (and not confused with unrelated lectins). (baines2007receptormediatedproteintransport pages 4-6)

### 2) LMAN1L: what is directly supported vs inferred
A structured evidence map is provided below.

| Claim/Topic | Evidence type | Key details | Best supporting source |
|---|---|---|---|
| Gene identity / nomenclature | Direct for LMAN1L | Human target verified as **LMAN1L** (approved name: *lectin, mannose binding 1 like*), Ensembl **ENSG00000140506**; UniProt target in this task is **Q9HAT1** with synonyms including **ERGL**. OpenTargets confirms LMAN1L as a distinct human gene target. (OpenTargets Search: -LMAN1L) | OpenTargets target page / evidence context, PMIDs listed in database evidence; context for ENSG00000140506, accessed via OpenTargets (no DOI; database context) (OpenTargets Search: -LMAN1L) |
| L-type lectin family membership | Direct for LMAN1L | A foundational review explicitly lists **LMAN1L** as a member of the **animal L-type lectin** family, separate from **LMAN1/ERGIC-53**, **LMAN2/VIP36**, and **LMAN2L/VIPL**. (baines2007receptormediatedproteintransport pages 4-6) | Baines & Zhang 2007, *Trends Biochem Sci*; DOI: https://doi.org/10.1016/j.tibs.2007.06.006 (2007) (baines2007receptormediatedproteintransport pages 4-6) |
| Domain architecture / topology | Inference for LMAN1L | Based on its placement in the L-type lectin family and the UniProt/domain annotation supplied in the prompt (lectin legume-like / ConA-like domain), LMAN1L is likely a **type I membrane protein** with a **luminal carbohydrate-recognition domain (CRD)**, stalk/coiled-coil region, transmembrane helix, and short cytosolic tail; this is strongly inferred from the closest paralog LMAN1. (das2012structuralbasisofa pages 25-31, ergicUnknownyearvaijayantidas pages 25-31) | Das 2012 thesis/article on LMAN1 structural basis (no clear journal DOI in retrieved context); summarized structural features of LMAN1 as analog (2012) (das2012structuralbasisofa pages 25-31, ergicUnknownyearvaijayantidas pages 25-31) |
| Trafficking signals / cycling concept | Direct for LMAN1; Inference for LMAN1L | LMAN1 contains a **C-terminal FF motif** for COPII-mediated ER exit and **KK motif** for COPI-mediated retrieval, cycling between **ER, ERGIC, and cis-Golgi**. LMAN1L likely uses analogous early secretory pathway cycling logic if it retains similar motifs/topology. (baines2007receptormediatedproteintransport pages 3-4, baines2007receptormediatedproteintransport pages 2-3, das2012structuralbasisof pages 31-37, das2012structuralbasisofa pages 31-37, zhang2023mammaliancargoreceptors pages 3-3) | Baines & Zhang 2007, *Trends Biochem Sci*; DOI: https://doi.org/10.1016/j.tibs.2007.06.006 (2007) (baines2007receptormediatedproteintransport pages 3-4, baines2007receptormediatedproteintransport pages 2-3) |
| Cargo receptor mechanism (COPII/COPI, pH/Ca2+) | Direct for LMAN1; Inference for LMAN1L | For LMAN1-family cargo receptors, cargo loading occurs in ER and unloading in ERGIC/Golgi; this is influenced by **luminal pH** and **Ca2+** differences. LMAN1 mannose binding is Ca2+-sensitive, and the receptor recycles after cargo release. LMAN1L is therefore plausibly a **Ca2+/pH-sensitive lectin cargo receptor or transporter-like lectin** in the early secretory pathway. (zhang2023mammaliancargoreceptors pages 4-5, zhang2023mammaliancargoreceptors pages 3-3, zhang2023mammaliancargoreceptors pages 5-6) | Zhang et al. 2023, *Biochem Soc Trans*; DOI: https://doi.org/10.1042/bst20220713 (2023) (zhang2023mammaliancargoreceptors pages 4-5, zhang2023mammaliancargoreceptors pages 3-3, zhang2023mammaliancargoreceptors pages 5-6) |
| Structural architecture (cryo-EM 2024 analog) | Direct for LMAN1; Inference for LMAN1L | Full-length **ERGIC-53/LMAN1** was resolved by cryo-EM as a **tetramer** with a four-leaf-clover head, long coiled-coil stalk, and transmembrane domain, in complex with **MCFD2**. This provides the best modern structural analog for inferring LMAN1L overall architecture as an L-type lectin family member, though it is **not** direct LMAN1L evidence. (watanabe2024structureoffulllength media 33178de8) | Watanabe et al. 2024, *Nature Communications*; DOI: https://doi.org/10.1038/s41467-024-46747-1 (2024) (watanabe2024structureoffulllength media 33178de8) |
| Known cargos for LMAN1 as analogs | Direct for LMAN1; Inference for LMAN1L | LMAN1–MCFD2 is a validated cargo receptor for **coagulation factors V and VIII**; other reported cargos/affected proteins include **α1-antitrypsin (A1AT)**, **cathepsin C**, **cathepsin Z**, and additional proposed cargos such as **Mac-2BP**, **GABAARs**, and **MMP-9**. These establish the kind of glycoprotein-trafficking role LMAN1L might have, but **no specific LMAN1L cargo** was retrieved. (baines2007receptormediatedproteintransport pages 3-4, baines2007receptormediatedproteintransport pages 4-6, zhang2023mammaliancargoreceptors pages 4-5) | Baines & Zhang 2007, *Trends Biochem Sci*; DOI: https://doi.org/10.1016/j.tibs.2007.06.006 (2007); Zhang et al. 2023, *Biochem Soc Trans*; DOI: https://doi.org/10.1042/bst20220713 (2023) (baines2007receptormediatedproteintransport pages 3-4, baines2007receptormediatedproteintransport pages 4-6, zhang2023mammaliancargoreceptors pages 4-5) |
| Disease / trait associations for LMAN1L | Database association | OpenTargets links LMAN1L to several complex traits including **hypertension**, **alcohol drinking**, **osteoarthritis**, **hip osteoarthritis**, and **pregnancy-induced hypertension**; these appear to reflect aggregated association evidence rather than mechanism-resolving functional studies, so biological interpretation should be cautious. (OpenTargets Search: -LMAN1L) | OpenTargets disease-target association context for LMAN1L (database evidence; no DOI in retrieved context) (OpenTargets Search: -LMAN1L) |
| Localization | Inference for LMAN1L | No direct localization study for human LMAN1L was retrieved. Because LMAN1 and related L-type lectins operate in the **early secretory pathway**, the strongest current inference is that LMAN1L localizes to **ER/ERGIC/cis-Golgi-associated compartments** rather than being a classic cell-surface lectin. (baines2007receptormediatedproteintransport pages 4-6, ergicUnknownyearvaijayantidas pages 31-37, das2012structuralbasisof pages 31-37, zhang2023mammaliancargoreceptors pages 3-3) | Baines & Zhang 2007, *Trends Biochem Sci*; DOI: https://doi.org/10.1016/j.tibs.2007.06.006 (2007) plus LMAN1 structural/functional analog evidence (baines2007receptormediatedproteintransport pages 4-6, ergicUnknownyearvaijayantidas pages 31-37, das2012structuralbasisof pages 31-37, zhang2023mammaliancargoreceptors pages 3-3) |
| Limitations / knowledge gaps | Direct for LMAN1L | The retrieved corpus contains **very limited direct experimental literature** for human **LMAN1L/Q9HAT1**. No retrieved primary study directly established its cargo spectrum, precise subcellular localization, binding partners, or pathway-specific mechanism. Therefore, most functional annotation currently rests on **family membership plus paralog-based inference**, which must be labeled accordingly. (OpenTargets Search: -LMAN1L, baines2007receptormediatedproteintransport pages 4-6, zhang2023mammaliancargoreceptors pages 4-5) | Constraint from retrieved evidence set; explicit family-only mention in Baines & Zhang 2007 and absence of direct mechanistic LMAN1L studies in retrieved corpus (OpenTargets Search: -LMAN1L, baines2007receptormediatedproteintransport pages 4-6, zhang2023mammaliancargoreceptors pages 4-5) |


*Table: This table separates what is directly supported for human LMAN1L from what is inferred using the best-studied paralog LMAN1/ERGIC-53 and modern cargo receptor biology. It is useful for building a cautious functional annotation while making evidence strength explicit.*

### 3) Molecular function, biological processes, and localization
#### 3.1 Direct evidence for LMAN1L
**Direct mechanistic statements about LMAN1L were not found** in the retrieved full-text set beyond its explicit listing as an L‑type lectin family member. (baines2007receptormediatedproteintransport pages 4-6)

#### 3.2 Likely molecular function (inference from LMAN1/ERGIC-53)
LMAN1 is described as a lectin cargo receptor with features typical of receptors that cycle in the early secretory pathway (transmembrane protein, luminal carbohydrate-recognition domain, and cytosolic motifs that mediate COPII export and COPI retrieval). (baines2007receptormediatedproteintransport pages 3-4, baines2007receptormediatedproteintransport pages 2-3, das2012structuralbasisof pages 31-37, das2012structuralbasisofa pages 31-37)

LMAN1-family cargo receptor behavior is also framed by compartmental chemistry: the ER lumen is relatively neutral with higher Ca2+ compared with the more acidic, lower Ca2+ ERGIC/Golgi, and these gradients can influence cargo loading/unloading. (zhang2023mammaliancargoreceptors pages 3-3)

**Inference for LMAN1L:** Given that LMAN1L is an animal L‑type lectin family member and (per user-provided UniProt context) contains legume/ConA-like lectin domains, the most plausible primary function is **selective binding of specific glycoproteins (likely via high‑mannose-type N‑glycans and/or conformational protein determinants) to promote their ER exit and/or proper trafficking to ERGIC/cis-Golgi**. This inference should be treated as a working hypothesis until direct LMAN1L experimental characterization is available. (baines2007receptormediatedproteintransport pages 4-6, das2012structuralbasisofa pages 25-31, zhang2023mammaliancargoreceptors pages 3-3)

#### 3.3 Likely subcellular localization (inference)
LMAN1 is described as largely localized to the ERGIC at steady state but cycling back to the ER via COPI-dependent retrieval signals, consistent with ER↔ERGIC trafficking. (baines2007receptormediatedproteintransport pages 3-4)

**Inference for LMAN1L:** LMAN1L is therefore most likely an **ER/ERGIC/cis-Golgi-associated cycling membrane lectin** rather than a stable plasma membrane receptor. (baines2007receptormediatedproteintransport pages 4-6, zhang2023mammaliancargoreceptors pages 3-3)

### 4) Recent developments (prioritizing 2023–2024)

| Year | Source | Contribution | Relevance to LMAN1L functional inference |
|---|---|---|---|
| 2007 | Baines & Zhang, *Trends in Biochemical Sciences* (Aug 2007), DOI: https://doi.org/10.1016/j.tibs.2007.06.006 | Foundational review of receptor-mediated protein transport in the early secretory pathway; explicitly identifies **LMAN1L** as a distinct member of the **animal L-type lectin** family alongside LMAN1/ERGIC-53, LMAN2/VIP36, and LMAN2L/VIPL. (baines2007receptormediatedproteintransport pages 4-6) | Provides the key evidence that the target is the correct human family member and should be interpreted within L-type lectin biology rather than confused with LMAN1 or LMAN2 paralogs. (baines2007receptormediatedproteintransport pages 4-6) |
| 2023 | Zhang, Srivastava & Zhang, *Biochemical Society Transactions* (Jun 2023), DOI: https://doi.org/10.1042/bst20220713 | Authoritative recent review of mammalian ER-to-Golgi cargo receptors; synthesizes evidence that **LMAN1** cycles between ER and ERGIC/Golgi, uses glycan and protein interactions for cargo recognition, and is regulated by compartmental **pH/Ca2+** conditions. (zhang2023mammaliancargoreceptors pages 4-5, zhang2023mammaliancargoreceptors pages 3-3, zhang2023mammaliancargoreceptors pages 5-6) | Supplies the strongest recent mechanistic framework for inferring likely **LMAN1L** roles as an early secretory pathway lectin/cargo receptor, while making clear that these are paralog-based inferences rather than direct LMAN1L experiments. (zhang2023mammaliancargoreceptors pages 4-5, zhang2023mammaliancargoreceptors pages 5-6, zhang2023mammaliancargoreceptors pages 3-3) |
| 2024 | Watanabe et al., *Nature Communications* (Mar 2024), DOI: https://doi.org/10.1038/s41467-024-46747-1 | Cryo-EM structure of full-length **ERGIC-53/LMAN1** in complex with **MCFD2**; defines overall architecture as a long stalked tetramer with a clover-like head and transmembrane domain. (watanabe2024structureoffulllength media 33178de8) | Gives the best current structural analog for **LMAN1L** domain organization and supports high-confidence inference that LMAN1L, as an L-type lectin family member, likely shares a comparable secretory-pathway lectin architecture. (watanabe2024structureoffulllength media 33178de8) |


*Table: This table summarizes the key sources used to anchor LMAN1L annotation, highlighting direct family-membership evidence and the most relevant recent mechanistic and structural analogs. It is useful for separating what is known directly about LMAN1L from what is inferred from the best-studied paralog, LMAN1/ERGIC-53.*

#### 4.1 2023: Mechanistic synthesis for mammalian cargo receptors
A 2023 review synthesizes current understanding of mammalian ER-to-Golgi cargo receptors (with emphasis on LMAN1–MCFD2 and SURF4). For LMAN1, it summarizes separable binding for high-mannose glycans and MCFD2, notes physiologically relevant cargoes (FV, FVIII, and α1-antitrypsin) and ER retention when LMAN1/MCFD2 are absent, and highlights how luminal pH/Ca2+ conditions influence cargo loading/unloading. (zhang2023mammaliancargoreceptors pages 4-5, zhang2023mammaliancargoreceptors pages 3-3)

**Relevance to LMAN1L:** This is the most authoritative recent framework for hypothesizing LMAN1L’s possible cargo receptor role and regulatory logic (Ca2+/pH sensitivity), but it does not provide direct LMAN1L data. (zhang2023mammaliancargoreceptors pages 4-5)

#### 4.2 2024: Structural mechanism of ERGIC-53/LMAN1
A 2024 Nature Communications paper reports cryo‑EM structures of full-length ERGIC‑53/LMAN1 in complex with MCFD2, showing a tetrameric organization with a clover-like head and long coiled-coil stalk and proposing mechanisms of cargo capture/release. (watanabe2024structureoffulllength media 33178de8)

The most informative figure panel retrieved is cited here as a structural reference:
(watanabe2024structureoffulllength media 33178de8)

**Relevance to LMAN1L:** LMAN1L likely shares a related overall fold/domain organization as an L‑type lectin family member (inference), making this structure a useful analog for conceptualizing how LMAN1L could present a luminal lectin head connected to the membrane by an extended coiled-coil. (baines2007receptormediatedproteintransport pages 4-6, watanabe2024structureoffulllength media 33178de8)

### 5) Interacting partners/cargo and pathway placement
#### 5.1 What is known for LMAN1 (closest paralog; direct)
LMAN1–MCFD2 is the best-defined mammalian cargo receptor complex; the review describes that it is required for efficient secretion of FV and FVIII and that in the associated inherited disorder plasma FV and FVIII can be reduced to **5–30% of normal**. (baines2007receptormediatedproteintransport pages 3-4)

The same review reports that under chemical cross-linking conditions, an estimated **5–20% of FVIII** is detected in a tertiary complex with LMAN1 and MCFD2, offering direct evidence of receptor–cargo interaction for the LMAN1 pathway. (baines2007receptormediatedproteintransport pages 4-6)

#### 5.2 Implications for LMAN1L (inference)
If LMAN1L acts as a cargo receptor, two nonexclusive mechanisms are plausible by analogy to LMAN1:
1) **Lectin-mediated glycan recognition** (e.g., high-mannose N-glycans) coupled to COPII packaging and COPI retrieval cycling. (baines2007receptormediatedproteintransport pages 3-4, baines2007receptormediatedproteintransport pages 2-3, das2012structuralbasisofa pages 25-31)
2) **Protein–protein interactions** that cooperate with glycan recognition and are modulated by luminal **Ca2+/pH** changes between ER and ERGIC/Golgi to promote release. (zhang2023mammaliancargoreceptors pages 3-3)

However, **no specific LMAN1L cargoes or binding partners** were identified in the retrieved evidence, so cargo assignment for LMAN1L remains an open question in this tool-limited corpus. (baines2007receptormediatedproteintransport pages 4-6)

### 6) Current applications and real-world implementations
Direct translational/industrial applications for LMAN1L were not supported in the retrieved corpus. By analogy, cargo receptors like SURF4 have been suggested as engineering targets to increase recombinant protein secretion; similarly, partial inhibition or modulation of LMAN1 has been discussed as potentially sufficient to modulate FV/FVIII levels in vivo (paralog evidence). (zhang2023mammaliancargoreceptors pages 4-5)

**Inference for LMAN1L:** If LMAN1L proves to be a selective cargo receptor for a therapeutically relevant secreted glycoprotein, it could become a target for (i) secretion engineering in biomanufacturing or (ii) modulation of specific circulating proteins. This is speculative and requires direct evidence. (zhang2023mammaliancargoreceptors pages 4-5)

### 7) Expert synthesis / authoritative opinions
Authoritative reviews emphasize that, despite the enormous diversity of secretory cargo, only a small set of mammalian cargo receptors are well-defined, and receptor-mediated transport requires (i) a cycling transmembrane component, (ii) selective impairment of cargo transport upon deficiency, and (iii) evidence of specific receptor–cargo interaction. (baines2007receptormediatedproteintransport pages 3-4)

**Interpretation for LMAN1L:** Because LMAN1L currently lacks the latter two criteria in the retrieved literature set, the most defensible “expert” position is that LMAN1L is a plausible candidate cargo receptor by homology, but its **specific physiological cargo and mechanism remain insufficiently established** in the accessible corpus. (baines2007receptormediatedproteintransport pages 3-4, baines2007receptormediatedproteintransport pages 4-6)

### 8) Disease associations, statistics, and data
#### 8.1 LMAN1L disease/trait links (database-level)
OpenTargets aggregates evidence connecting LMAN1L to multiple complex traits/diseases, including **hypertension**, **alcohol drinking**, and **osteoarthritis** (including hip OA) and **pregnancy-induced hypertension**. These are association scores/evidence counts and should be treated as hypothesis-generating rather than causal mechanism. (OpenTargets Search: -LMAN1L)

#### 8.2 Quantitative data (from primary/review sources; paralog pathway)
* In combined factor V and VIII deficiency (F5F8D) caused by LMAN1/MCFD2 pathway defects, plasma FV and FVIII levels are reported as **5–30% of normal**. (baines2007receptormediatedproteintransport pages 3-4)
* Under chemical cross-linking, **5–20% of FVIII** is detected in a tertiary complex with LMAN1 and MCFD2. (baines2007receptormediatedproteintransport pages 4-6)

These values provide benchmarks for the magnitude of effect a true cargo receptor can have on secretion and for detectability of receptor–cargo complexes, but they do not specifically implicate LMAN1L. (baines2007receptormediatedproteintransport pages 3-4, baines2007receptormediatedproteintransport pages 4-6)

### 9) Conclusions and prioritized hypotheses for LMAN1L (evidence-aware)
1) **Primary functional hypothesis (inference):** LMAN1L is an early secretory pathway **lectin/cargo receptor-like** protein that binds a subset of glycoprotein clients and supports ER-to-ERGIC/Golgi trafficking in a manner regulated by compartmental Ca2+/pH, analogous to LMAN1/ERGIC‑53. (baines2007receptormediatedproteintransport pages 4-6, zhang2023mammaliancargoreceptors pages 4-5, zhang2023mammaliancargoreceptors pages 3-3)
2) **Localization hypothesis (inference):** LMAN1L most likely resides in **ER/ERGIC/cis-Golgi** compartments and cycles via COPII/COPI logic rather than being primarily cell-surface. (baines2007receptormediatedproteintransport pages 3-4, zhang2023mammaliancargoreceptors pages 3-3)
3) **Human genetics hypothesis (database association):** LMAN1L may influence complex traits (e.g., hypertension, osteoarthritis) through effects on secretion/processing of specific extracellular proteins; this remains unproven and requires gene-to-phenotype mechanistic work. (OpenTargets Search: -LMAN1L)

### References (URLs and publication dates)
* Baines AC, Zhang B. *Receptor-mediated protein transport in the early secretory pathway.* **Aug 2007**. Trends Biochem Sci. DOI/URL: https://doi.org/10.1016/j.tibs.2007.06.006 (baines2007receptormediatedproteintransport pages 3-4, baines2007receptormediatedproteintransport pages 2-3, baines2007receptormediatedproteintransport pages 1-2, baines2007receptormediatedproteintransport pages 4-6)
* Zhang Y, Srivastava V, Zhang B. *Mammalian cargo receptors for endoplasmic reticulum-to-Golgi transport: mechanisms and interactions.* **Jun 2023**. Biochem Soc Trans. DOI/URL: https://doi.org/10.1042/bst20220713 (zhang2023mammaliancargoreceptors pages 4-5, zhang2023mammaliancargoreceptors pages 3-3, zhang2023mammaliancargoreceptors pages 5-6)
* Watanabe S, et al. *Structure of full-length ERGIC-53 in complex with MCFD2 for cargo transport.* **Mar 2024**. Nat Commun. DOI/URL: https://doi.org/10.1038/s41467-024-46747-1 (watanabe2024structureoffulllength media 33178de8)
* OpenTargets association evidence for LMAN1L (ENSG00000140506). Database context with literature links (PMIDs listed in evidence rows). (OpenTargets Search: -LMAN1L)

### Transparency note (scope limitation)
This report is constrained by the retrieved corpus: **direct experimental studies on human LMAN1L/Q9HAT1 were not accessible via the tool searches**, so functional annotation necessarily relies on (i) explicit family membership evidence and (ii) structured inference from LMAN1/ERGIC‑53 and general cargo receptor biology. (baines2007receptormediatedproteintransport pages 4-6, zhang2023mammaliancargoreceptors pages 4-5)

References

1. (OpenTargets Search: -LMAN1L): Open Targets Query (-LMAN1L, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (baines2007receptormediatedproteintransport pages 4-6): Andrea C. Baines and Bin Zhang. Receptor-mediated protein transport in the early secretory pathway. Trends in biochemical sciences, 32 8:381-8, Aug 2007. URL: https://doi.org/10.1016/j.tibs.2007.06.006, doi:10.1016/j.tibs.2007.06.006. This article has 62 citations and is from a domain leading peer-reviewed journal.

3. (zhang2023mammaliancargoreceptors pages 4-5): Yuanbao Zhang, Vishal Srivastava, and Bin Zhang. Mammalian cargo receptors for endoplasmic reticulum-to-golgi transport: mechanisms and interactions. Biochemical Society Transactions, 51:971-981, Jun 2023. URL: https://doi.org/10.1042/bst20220713, doi:10.1042/bst20220713. This article has 23 citations and is from a peer-reviewed journal.

4. (zhang2023mammaliancargoreceptors pages 3-3): Yuanbao Zhang, Vishal Srivastava, and Bin Zhang. Mammalian cargo receptors for endoplasmic reticulum-to-golgi transport: mechanisms and interactions. Biochemical Society Transactions, 51:971-981, Jun 2023. URL: https://doi.org/10.1042/bst20220713, doi:10.1042/bst20220713. This article has 23 citations and is from a peer-reviewed journal.

5. (ergicUnknownyearvaijayantidas pages 31-37): RIN ERGIC. Vaijayanti das. Unknown journal, Unknown year.

6. (das2012structuralbasisofa pages 25-31): V Das. Structural basis of lman1 cargo capture in er & release in ergic. Unknown journal, 2012.

7. (watanabe2024structureoffulllength media 33178de8): Satoshi Watanabe, Yoshiaki Kise, Kento Yonezawa, Mariko Inoue, Nobutaka Shimizu, Osamu Nureki, and Kenji Inaba. Structure of full-length ergic-53 in complex with mcfd2 for cargo transport. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46747-1, doi:10.1038/s41467-024-46747-1. This article has 14 citations and is from a highest quality peer-reviewed journal.

8. (baines2007receptormediatedproteintransport pages 1-2): Andrea C. Baines and Bin Zhang. Receptor-mediated protein transport in the early secretory pathway. Trends in biochemical sciences, 32 8:381-8, Aug 2007. URL: https://doi.org/10.1016/j.tibs.2007.06.006, doi:10.1016/j.tibs.2007.06.006. This article has 62 citations and is from a domain leading peer-reviewed journal.

9. (ergicUnknownyearvaijayantidas pages 25-31): RIN ERGIC. Vaijayanti das. Unknown journal, Unknown year.

10. (baines2007receptormediatedproteintransport pages 3-4): Andrea C. Baines and Bin Zhang. Receptor-mediated protein transport in the early secretory pathway. Trends in biochemical sciences, 32 8:381-8, Aug 2007. URL: https://doi.org/10.1016/j.tibs.2007.06.006, doi:10.1016/j.tibs.2007.06.006. This article has 62 citations and is from a domain leading peer-reviewed journal.

11. (baines2007receptormediatedproteintransport pages 2-3): Andrea C. Baines and Bin Zhang. Receptor-mediated protein transport in the early secretory pathway. Trends in biochemical sciences, 32 8:381-8, Aug 2007. URL: https://doi.org/10.1016/j.tibs.2007.06.006, doi:10.1016/j.tibs.2007.06.006. This article has 62 citations and is from a domain leading peer-reviewed journal.

12. (das2012structuralbasisof pages 31-37): V Das. Structural basis of lman1 cargo capture in er & release in ergic. Unknown journal, 2012.

13. (das2012structuralbasisofa pages 31-37): V Das. Structural basis of lman1 cargo capture in er & release in ergic. Unknown journal, 2012.

14. (zhang2023mammaliancargoreceptors pages 5-6): Yuanbao Zhang, Vishal Srivastava, and Bin Zhang. Mammalian cargo receptors for endoplasmic reticulum-to-golgi transport: mechanisms and interactions. Biochemical Society Transactions, 51:971-981, Jun 2023. URL: https://doi.org/10.1042/bst20220713, doi:10.1042/bst20220713. This article has 23 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](LMAN1L-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](LMAN1L-deep-research-falcon_artifacts/artifact-01.md)
![## Context ID: pqac-00000009 The overall architecture and domain organization of the full-length ERGIC-53 tetramer in complex with MCFD2 is shown in this cryo-E](LMAN1L-deep-research-falcon_artifacts/image-1.png)

## Citations

1. baines2007receptormediatedproteintransport pages 4-6
2. zhang2023mammaliancargoreceptors pages 3-3
3. baines2007receptormediatedproteintransport pages 3-4
4. zhang2023mammaliancargoreceptors pages 4-5
5. das2012structuralbasisofa pages 25-31
6. baines2007receptormediatedproteintransport pages 1-2
7. baines2007receptormediatedproteintransport pages 2-3
8. das2012structuralbasisof pages 31-37
9. das2012structuralbasisofa pages 31-37
10. zhang2023mammaliancargoreceptors pages 5-6
11. https://doi.org/10.1016/j.tibs.2007.06.006
12. https://doi.org/10.1042/bst20220713
13. https://doi.org/10.1038/s41467-024-46747-1
14. https://doi.org/10.1016/j.tibs.2007.06.006,
15. https://doi.org/10.1042/bst20220713,
16. https://doi.org/10.1038/s41467-024-46747-1,