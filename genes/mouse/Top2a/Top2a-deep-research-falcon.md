---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-30T20:02:36.317706'
end_time: '2026-05-30T20:09:37.892740'
duration_seconds: 421.58
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: mouse
  gene_id: Top2a
  gene_symbol: Top2a
  uniprot_accession: Q01320
  protein_description: 'RecName: Full=DNA topoisomerase 2-alpha; EC=5.6.2.2 {ECO:0000255|PROSITE-ProRule:PRU00995,
    ECO:0000269|PubMed:1331984}; AltName: Full=DNA topoisomerase II, alpha isozyme;'
  gene_info: Name=Top2a; Synonyms=Top-2, Top2;
  organism_full: Mus musculus (Mouse).
  protein_family: Belongs to the type II topoisomerase family. .
  protein_domains: DNA_Topoisomerase_II. (IPR050634); DTHCT. (IPR012542); HATPase_C_sf.
    (IPR036890); Ribosomal_Su5_D2-typ_SF. (IPR020568); Ribsml_uS5_D2-typ_fold_subgr.
    (IPR014721)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 24
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Top2a-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q01320
- **Protein Description:** RecName: Full=DNA topoisomerase 2-alpha; EC=5.6.2.2 {ECO:0000255|PROSITE-ProRule:PRU00995, ECO:0000269|PubMed:1331984}; AltName: Full=DNA topoisomerase II, alpha isozyme;
- **Gene Information:** Name=Top2a; Synonyms=Top-2, Top2;
- **Organism (full):** Mus musculus (Mouse).
- **Protein Family:** Belongs to the type II topoisomerase family. .
- **Key Domains:** DNA_Topoisomerase_II. (IPR050634); DTHCT. (IPR012542); HATPase_C_sf. (IPR036890); Ribosomal_Su5_D2-typ_SF. (IPR020568); Ribsml_uS5_D2-typ_fold_subgr. (IPR014721)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Top2a" matches the protein description above**
2. **Verify the organism is correct:** Mus musculus (Mouse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Top2a' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Top2a** (gene ID: Top2a, UniProt: Q01320) in mouse.

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
- **UniProt Accession:** Q01320
- **Protein Description:** RecName: Full=DNA topoisomerase 2-alpha; EC=5.6.2.2 {ECO:0000255|PROSITE-ProRule:PRU00995, ECO:0000269|PubMed:1331984}; AltName: Full=DNA topoisomerase II, alpha isozyme;
- **Gene Information:** Name=Top2a; Synonyms=Top-2, Top2;
- **Organism (full):** Mus musculus (Mouse).
- **Protein Family:** Belongs to the type II topoisomerase family. .
- **Key Domains:** DNA_Topoisomerase_II. (IPR050634); DTHCT. (IPR012542); HATPase_C_sf. (IPR036890); Ribosomal_Su5_D2-typ_SF. (IPR020568); Ribsml_uS5_D2-typ_fold_subgr. (IPR014721)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Top2a" matches the protein description above**
2. **Verify the organism is correct:** Mus musculus (Mouse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Top2a' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Top2a** (gene ID: Top2a, UniProt: Q01320) in mouse.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Research report: Mouse **Top2a** (UniProt **Q01320**) — DNA topoisomerase 2-alpha (EC 5.6.2.2)

## 0) Target verification (critical identity check)
The UniProt accession **Q01320** corresponds to **Mus musculus** **Top2a**, annotated as **DNA topoisomerase II alpha** (type IIA topoisomerase family). The literature summarized here consistently describes **TOP2A/Top2α** as an ATP-dependent **homodimeric type II topoisomerase** that cleaves and religates **double-stranded DNA** during strand passage, and it highlights the canonical **ATPase + DNA cleavage core + C-terminal regulatory region** architecture expected for a type IIA topoisomerase; this matches the UniProt-provided identity and avoids confusion with TOP2B (benoit2025investigatingthemitotic pages 21-25, fenelon2026therolesof pages 5-7).

## 1) Key concepts and definitions (current understanding)

### 1.1 What TOP2A is (definition)
**Top2a/TOP2A** is an **ATP-dependent type IIA DNA topoisomerase** that resolves topological stress by creating a **transient, enzyme-linked double-strand break** in one DNA duplex (the “gate” segment) and transporting a second duplex (the “transport” segment) through the break before **re-ligating** the DNA. This activity changes DNA topology and enables both **relaxation of supercoils** and **decatenation** (unlinking) of interlinked DNA duplexes (benoit2025investigatingthemitotic pages 21-25, fenelon2026therolesof pages 5-7).

### 1.2 Reaction catalyzed and substrate specificity (functional annotation focus)
Functionally, TOP2A’s substrate is **double-stranded DNA** in topologically constrained forms encountered in vivo: **supercoiled DNA** produced by replication/transcription and **catenated sister chromatids** produced by DNA replication. Its central physiological outputs are (i) **relaxation of supercoiling** and (ii) **decatenation** required for chromosome segregation (benoit2025investigatingthemitotic pages 21-25, fenelon2026therolesof pages 5-7).

### 1.3 Mechanistic “two-gate” model and druggable steps
The catalytic cycle is commonly described in terms of gates: an **ATPase/N-gate** (ATP binding/hydrolysis controls dimer closure), a **DNA-gate** where cleavage/religation occurs, and a **C-gate** that allows release after transport. Distinct inhibitor classes trap different intermediates: **topoisomerase II poisons** (e.g., etoposide) stabilize cleavage complexes, whereas **catalytic inhibitors** (e.g., ICRF-193) inhibit strand passage/decatenation by trapping a clamp-like state (benoit2025investigatingthemitotic pages 21-25).

## 2) Protein architecture (domains) and structure-function relationships

### 2.1 Domain organization (high-level)
Across eukaryotic TOP2A proteins (including mouse Top2a), evidence supports a modular architecture with:
- **N-terminal ATPase domain** (HATPase-like fold),
- a **central catalytic core** that binds and cleaves DNA (including **TOPRIM** and “Tower”/cleavage-associated elements), and
- a **C-terminal domain (CTD)** that is regulatory and contributes to chromatin recruitment and isoform-specific functions in vivo (liu2024structuralinsightsinto pages 11-12, ardawatia2025lysinerichregionslocated pages 1-5).

### 2.2 Recent structural insight (2024): assembly of the cleavage–religation center
A 2024 structural study of **human Top2α/Top2β catalytic cores** (highly conserved with mouse Top2a) provides mechanistic detail for how DNA binding drives assembly of the **DNA cleavage–religation center**. It identifies a previously undocumented, **strictly conserved TOPRIM-helix arginine–DNA backbone interaction** (human Top2α **R661**) that is required for function (mutation abolished activity in functional assays) and notes that nearby lysine modification (SUMOylation) can interfere with this contact and reduce decatenation (Liu et al., **2024-07**, *Nucleic Acids Research*, https://doi.org/10.1093/nar/gkae657) (liu2024structuralinsightsinto pages 11-12).

## 3) Cellular localization and cell-cycle regulation (mouse-focused where possible)

### 3.1 Subcellular localization in mouse cells
In mouse NIH3T3 fibroblasts, Top2α is **chromatin-associated** and described as **enriched at heterochromatin**. Importantly, **catalytic inhibition** with **ICRF-193** (a catalytic Top2 inhibitor) increases Top2α chromatin association and retention (including under high-salt extraction conditions) and reduces its mobility by FRAP, consistent with inhibitor-induced trapping on chromatin rather than free diffusion (Amoiridis et al., **2024-08**, *Nature Communications*, preprint DOI: https://doi.org/10.1101/2023.08.01.551420) (amoiridis2024inhibitionoftopoisomerase pages 17-22).

### 3.2 Cell-cycle regulation
TOP2A expression is tightly linked to proliferation: it is low in quiescent cells, increases through **S phase**, and peaks during **G2/M**, consistent with its specialized role in managing DNA topology during replication completion and mitosis (fenelon2026therolesof pages 5-7). This cell-cycle coupling aligns with its essential role in **decatenation** prior to and during chromosome segregation (benoit2025investigatingthemitotic pages 21-25, fenelon2026therolesof pages 5-7).

## 4) Biological roles and pathways

### 4.1 DNA replication completion, sister chromatid decatenation, and the decatenation checkpoint
During DNA replication, daughter duplexes become intertwined (catenated). TOP2A decatenation is required to enable sister chromatid individualization and faithful segregation, and catalytic inhibition can activate a **decatenation checkpoint**/G2 arrest phenotype in cell-based contexts (benoit2025investigatingthemitotic pages 21-25, amoiridis2024inhibitionoftopoisomerase pages 54-57).

### 4.2 Mitotic chromosome architecture and segregation
Multiple lines of evidence support that TOP2A is a major mitotic chromosome-associated factor with key roles in chromosome structure and segregation. In mitotic contexts, depletion/inhibition phenotypes include defective chromosome compaction/maintenance, chromosome bridges, and segregation failure (benoit2025investigatingthemitotic pages 25-28, benoit2025investigatingthemitotic pages 115-118). A major model is that TOP2A’s enzymatic decatenation is required for segregation, with additional evidence (in some systems) for a **structural maintenance contribution** to the integrity of condensed chromatids (benoit2025investigatingthemitotic pages 115-118).

## 5) Mouse genetics and phenotypes (in vivo requirement)
A frequently cited mammalian genetic result is that **mouse Top2a null embryos are lethal very early**, with arrest reported **as early as the 4–8 cell stage**, supporting an essential requirement during cleavage-stage development (Sapetto-Rebow et al., **2011-11**, *BMC Developmental Biology*, https://doi.org/10.1186/1471-213x-11-71; also summarized in later reviews) (fenelon2026therolesof pages 5-7).

*Note:* In the evidence available here, this embryonic-lethality statement is obtained from authoritative secondary sources rather than the original mouse knockout primary paper; it is nevertheless widely repeated and consistent with Top2a’s essential replication/segregation function (fenelon2026therolesof pages 5-7).

## 6) Recent developments (prioritizing 2023–2024)

### 6.1 2024 mechanistic advance in mouse cells: TOP2 catalytic inhibition destabilizes heterochromatin/repeats
Amoiridis et al. (2024) investigated how **catalytic inhibition** of Top2 affects heterochromatin and repetitive elements and developed multiple assays in mouse cells. The study reports that Top2α becomes more tightly chromatin-associated under ICRF-193, and it uses mechanistic tools (including a dominant-negative **Top2α Y805F** catalytic mutant) to show that **Top2α catalytic activity is required** for specific DNA-damage responses at heterochromatin under inhibitory conditions (amoiridis2024inhibitionoftopoisomerase pages 17-22).

**Recent statistics/data and implementation details from this work include:**
- END-seq performed on **15 million NIH3T3 (mouse) cells** and mapped to the **mm9** mouse genome, with repetitive-element quantification retaining multi-mapped reads and differential analysis using **DESeq2** normalization (amoiridis2024inhibitionoftopoisomerase pages 54-57).
- A Top2 cleavage-complex isolation workflow was applied to NIH3T3 with **ICRF-193 (5 μM, 4 h)** or **etoposide (50 μM, 30 min)** as perturbations (amoiridis2024inhibitionoftopoisomerase pages 54-57).

These data provide concrete, recent evidence that Top2a activity is important for heterochromatin/repeat integrity and that Top2 catalytic inhibitors can “trap” Top2α on chromatin in mouse cells (amoiridis2024inhibitionoftopoisomerase pages 54-57, amoiridis2024inhibitionoftopoisomerase pages 17-22).

### 6.2 2024 structural advance (human Top2α core; conserved relevance to mouse)
The 2024 *Nucleic Acids Research* study provides near-term structural insight into how the catalytic core assembles around DNA and identifies conserved protein–DNA contacts within the TOPRIM region that are critical for catalysis, informing residue-level functional annotation for vertebrate Top2a orthologs (https://doi.org/10.1093/nar/gkae657) (liu2024structuralinsightsinto pages 11-12).

## 7) Current applications and real-world implementations

### 7.1 TOP2A as a therapeutic target (oncology)
Type II topoisomerases are major anticancer drug targets; therapeutic strategies include **TOP2 poisons** that stabilize TOP2–DNA cleavage complexes (increasing protein-linked DNA breaks) and **catalytic inhibitors** that block strand passage/decatenation. A 2023 review emphasizes leveraging TOP2 inhibitors in **synthetic lethality**-based combinations (e.g., co-targeting DNA damage response pathways) to improve efficacy and overcome resistance (Matias-Barrios & Dong, **2023-01**, *Pharmaceuticals*, https://doi.org/10.3390/ph16010094) (fenelon2026therolesof pages 5-7).

### 7.2 Experimental implementations in mammalian systems (including mouse cells)
Catalytic inhibitors such as **ICRF-193** and poisons such as **etoposide** are used as mechanistic probes to distinguish decatenation defects from cleavage-complex–associated DNA damage. In mouse NIH3T3 cells, ICRF-193 was used at **5 μM for 4 h** to induce a trapped chromatin-associated state of Top2α and interrogate heterochromatin/repeat phenotypes, whereas etoposide was used at **50 μM for 30 min** in cleavage-complex isolation workflows (amoiridis2024inhibitionoftopoisomerase pages 54-57, amoiridis2024inhibitionoftopoisomerase pages 17-22).

## 8) Expert synthesis and interpretive analysis (authoritative perspective)
Across the current evidence set, a coherent functional model emerges: **Top2a is an essential nuclear enzyme that uses ATP-driven strand passage to remove DNA supercoils and, critically, to decatenate replicated sister chromatids**, thereby enabling correct chromosome condensation/individualization and segregation. The newest (2024) mouse-cell work extends this classical mitotic/replication role into chromatin-context specificity by demonstrating strong dependence of **heterochromatin and repetitive DNA integrity** on Top2 catalytic activity and showing that catalytic inhibition can selectively trap Top2α on chromatin and induce repeat-associated defects (amoiridis2024inhibitionoftopoisomerase pages 17-22, amoiridis2024inhibitionoftopoisomerase pages 54-57). In parallel, new structural work identifies highly conserved catalytic contacts that can be mapped onto the mouse protein for residue-level annotation, providing a mechanistic basis for how specific mutations or post-translational modifications could alter decatenation and genome stability (liu2024structuralinsightsinto pages 11-12).

## 9) Evidence summary table
The following table consolidates key functional annotation points, recent advances, and applications with linked sources and DOIs.

| Category | Key points | Evidence/Source | URL/DOI | Notes |
|---|---|---|---|---|
| Enzymatic activity | ATP-dependent type IIA topoisomerase that transiently cleaves both strands of a DNA duplex and passes a second duplex through the break to change DNA topology; resolves supercoils and DNA catenanes generated during replication and mitosis (benoit2025investigatingthemitotic pages 21-25, fenelon2026therolesof pages 5-7) | Benoit 2025 thesis excerpt; Fenelon & Madabhushi 2026 *IJMS* | https://doi.org/10.3390/ijms27031552 | Core biochemical function is broadly conserved across eukaryotic TOP2A; directly matches UniProt Q01320 family assignment. |
| Mechanism | Catalytic cycle uses N-gate ATPase, DNA-gate cleavage/religation center, and C-gate; DNA binding induces conformational rearrangements that assemble the cleavage–religation center, including TOPRIM-mediated metal coordination (benoit2025investigatingthemitotic pages 21-25, liu2024structuralinsightsinto pages 11-12) | Benoit 2025 thesis excerpt; Liu 2024 *Nucleic Acids Research* | https://doi.org/10.1093/nar/gkae657 | Structural/mechanistic details are from human Top2α core structures but are highly relevant to mouse Top2a because of strong conservation within type IIA topoisomerases. |
| Domains | Domain architecture includes N-terminal ATPase/HATPase fold, central catalytic DNA cleavage core with TOPRIM/Tower elements, and a regulatory C-terminal domain (CTD); CTD is important in vivo for chromatin recruitment and isoform-specific regulation (liu2024structuralinsightsinto pages 11-12, ardawatia2025lysinerichregionslocated pages 1-5) | Liu 2024 *Nucleic Acids Research*; Ardawatia 2025 *bioRxiv* | https://doi.org/10.1093/nar/gkae657; https://doi.org/10.1101/2025.01.29.635480 | Consistent with UniProt/Pfam-style assignment of ATPase, DNA topoisomerase II catalytic, and CTD regulatory regions. Ardawatia is preprint evidence. |
| Localization | Top2α is nuclear/chromatin-associated and becomes tightly chromosome associated during mitosis; in mouse NIH3T3 cells it is enriched at heterochromatin and shows increased chromatin trapping after ICRF-193 treatment (amoiridis2024inhibitionoftopoisomerase pages 17-22, fenelon2026therolesof pages 18-19) | Amoiridis 2024 *Nature Communications*; Fenelon & Madabhushi 2026 *IJMS* | https://doi.org/10.1101/2023.08.01.551420; https://doi.org/10.3390/ijms27031552 | Mouse-cell evidence is direct for chromatin/heterochromatin association. Nucleolar localization is supported mainly by non-mouse CTD literature summarized in review/preprint contexts, so confidence for mouse-specific nucleolar localization is lower. |
| Cell-cycle regulation | Expression is proliferation dependent: low in quiescent cells, rises in S phase, and peaks in G2/M; Top2a activity contributes to the decatenation/G2 checkpoint and mitotic entry (fenelon2026therolesof pages 5-7, amoiridis2024inhibitionoftopoisomerase pages 54-57) | Fenelon & Madabhushi 2026 *IJMS*; Amoiridis 2024 *Nature Communications* | https://doi.org/10.3390/ijms27031552; https://doi.org/10.1101/2023.08.01.551420 | Review cites classic NIH3T3/mouse developmental expression studies; direct 2024 work supports G2-linked catalytic requirement. |
| Biological roles | Essential for relieving replication-associated topological stress, decatenating sister chromatids, supporting chromosome condensation/individualization, and enabling faithful chromosome segregation; catalytic inhibition or acute depletion causes chromosome decompaction, bridges, and failed segregation (benoit2025investigatingthemitotic pages 25-28, benoit2025investigatingthemitotic pages 115-118) | Benoit 2025 thesis excerpt; Nielsen 2020 *PNAS* | https://doi.org/10.1073/pnas.2001760117 | Strong functional consensus across vertebrate systems; mouse relevance supported by conservation and by mouse-cell inhibitor studies. |
| Mouse genetics | Mouse Top2a knockout is embryonic lethal as early as the 4–8 cell stage, indicating an essential requirement in early cleavage-stage development (fenelon2026therolesof pages 5-7) | Sapetto-Rebow 2011 *BMC Developmental Biology* (citing mouse knockout result); Fenelon & Madabhushi 2026 *IJMS* | https://doi.org/10.1186/1471-213x-11-71; https://doi.org/10.3390/ijms27031552 | The embryonic-lethality statement is well repeated in secondary sources available here; direct primary knockout paper was not recovered in context, so this row relies on authoritative secondary citation. |
| Recent 2023-2024 developments | 2024 work showed catalytic inhibition destabilizes heterochromatin/repetitive DNA and promotes interlinks between clustered repeats in mouse cells; 2024 structural study identified a conserved TOPRIM arginine-DNA contact and clarified assembly of the DNA cleavage–religation center (amoiridis2024inhibitionoftopoisomerase pages 17-22, liu2024structuralinsightsinto pages 11-12) | Amoiridis 2024 *Nature Communications*; Liu 2024 *Nucleic Acids Research* | https://doi.org/10.1101/2023.08.01.551420; https://doi.org/10.1093/nar/gkae657 | Best recent mechanistic advances in provided context. The structural study is human, but directly informs conserved Top2a function. |
| Applications/drugs | TOP2A is a major anticancer target; poisons such as etoposide stabilize cleavage complexes, whereas catalytic inhibitors such as ICRF-193 block strand passage/decatenation and are widely used to probe checkpoint and chromosome-segregation functions (benoit2025investigatingthemitotic pages 21-25, fenelon2026therolesof pages 5-7) | Benoit 2025 thesis excerpt; Matias-Barrios & Dong 2023 *Pharmaceuticals* | https://doi.org/10.3390/ph16010094 | Application evidence is mainly human oncology/general TOP2 literature, but it is directly relevant to mouse functional studies because the same inhibitor classes are used experimentally in mouse cells. |


*Table: This table summarizes the functional annotation of Mus musculus Top2a (UniProt Q01320), including enzymatic function, regulation, localization, mouse genetics, and recent mechanistic advances. It is useful as a concise evidence map linking core biology to experimental and therapeutic relevance.*

## 10) Key references (with dates and URLs)
- Liu K-T, Chen S-F, Chan N-L. **2024-07**. *Nucleic Acids Research*. “Structural insights into the assembly of type IIA topoisomerase DNA cleavage-religation center.” https://doi.org/10.1093/nar/gkae657 (liu2024structuralinsightsinto pages 11-12)
- Amoiridis M, Meaburn K, Verigos J, et al. **2024-08**. *Nature Communications* (as indexed; preprint DOI). “Inhibition of topoisomerase 2 catalytic activity impacts the integrity of heterochromatin and repetitive DNA and leads to interlinks between clustered repeats.” https://doi.org/10.1101/2023.08.01.551420 (amoiridis2024inhibitionoftopoisomerase pages 17-22, amoiridis2024inhibitionoftopoisomerase pages 54-57)
- Matias‑Barrios VM, Dong X. **2023-01**. *Pharmaceuticals*. “The implication of topoisomerase II inhibitors in synthetic lethality for cancer therapy.” https://doi.org/10.3390/ph16010094 (fenelon2026therolesof pages 5-7)
- Sapetto‑Rebow B, McLoughlin SC, O’Shea LC, et al. **2011-11**. *BMC Developmental Biology*. “Maternal topoisomerase II alpha…”. https://doi.org/10.1186/1471-213x-11-71 (mouse Top2a embryonic lethality cited) (fenelon2026therolesof pages 5-7)



References

1. (benoit2025investigatingthemitotic pages 21-25): J Benoit. Investigating the mitotic roles of topoisomerase 2 alpha and topoisomerase 2 beta-binding protein 1 in the maintenance of chromosome structure and genome …. Unknown journal, 2025.

2. (fenelon2026therolesof pages 5-7): Kelli D. Fenelon and Ram Madabhushi. The roles of topoisomerases in transcriptional regulation. International Journal of Molecular Sciences, 27:1552, Feb 2026. URL: https://doi.org/10.3390/ijms27031552, doi:10.3390/ijms27031552. This article has 1 citations.

3. (liu2024structuralinsightsinto pages 11-12): Ko-Ting Liu, Shin-Fu Chen, and Nei-Li Chan. Structural insights into the assembly of type iia topoisomerase dna cleavage-religation center. Nucleic Acids Research, 52:9788-9802, Jul 2024. URL: https://doi.org/10.1093/nar/gkae657, doi:10.1093/nar/gkae657. This article has 3 citations and is from a highest quality peer-reviewed journal.

4. (ardawatia2025lysinerichregionslocated pages 1-5): Vandana V. Ardawatia, Rhîan G. Jacobsen, Diana C. Turcu, Sandra Ninzima, Niclas P. Decker, Amanda J. Edson, and Aurélia E. Lewis. Lysine-rich regions located in the c-terminal domain of dna topoisomerase 2-alpha act as polyphosphoinositide interaction sites and nucleolar localisation signals. bioRxiv, Jan 2025. URL: https://doi.org/10.1101/2025.01.29.635480, doi:10.1101/2025.01.29.635480. This article has 0 citations.

5. (amoiridis2024inhibitionoftopoisomerase pages 17-22): Michalis Amoiridis, Karen Meaburn, John Verigos, William H Gittens, Tao Ye, Matthew J Neale, and Evi Soutoglou. Inhibition of topoisomerase 2 catalytic activity impacts the integrity of heterochromatin and repetitive dna and leads to interlinks between clustered repeats. Nature Communications, Aug 2024. URL: https://doi.org/10.1101/2023.08.01.551420, doi:10.1101/2023.08.01.551420. This article has 21 citations and is from a highest quality peer-reviewed journal.

6. (amoiridis2024inhibitionoftopoisomerase pages 54-57): Michalis Amoiridis, Karen Meaburn, John Verigos, William H Gittens, Tao Ye, Matthew J Neale, and Evi Soutoglou. Inhibition of topoisomerase 2 catalytic activity impacts the integrity of heterochromatin and repetitive dna and leads to interlinks between clustered repeats. Nature Communications, Aug 2024. URL: https://doi.org/10.1101/2023.08.01.551420, doi:10.1101/2023.08.01.551420. This article has 21 citations and is from a highest quality peer-reviewed journal.

7. (benoit2025investigatingthemitotic pages 25-28): J Benoit. Investigating the mitotic roles of topoisomerase 2 alpha and topoisomerase 2 beta-binding protein 1 in the maintenance of chromosome structure and genome …. Unknown journal, 2025.

8. (benoit2025investigatingthemitotic pages 115-118): J Benoit. Investigating the mitotic roles of topoisomerase 2 alpha and topoisomerase 2 beta-binding protein 1 in the maintenance of chromosome structure and genome …. Unknown journal, 2025.

9. (fenelon2026therolesof pages 18-19): Kelli D. Fenelon and Ram Madabhushi. The roles of topoisomerases in transcriptional regulation. International Journal of Molecular Sciences, 27:1552, Feb 2026. URL: https://doi.org/10.3390/ijms27031552, doi:10.3390/ijms27031552. This article has 1 citations.

## Artifacts

- [Edison artifact artifact-00](Top2a-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. benoit2025investigatingthemitotic pages 21-25
2. liu2024structuralinsightsinto pages 11-12
3. amoiridis2024inhibitionoftopoisomerase pages 17-22
4. fenelon2026therolesof pages 5-7
5. benoit2025investigatingthemitotic pages 115-118
6. amoiridis2024inhibitionoftopoisomerase pages 54-57
7. ardawatia2025lysinerichregionslocated pages 1-5
8. benoit2025investigatingthemitotic pages 25-28
9. fenelon2026therolesof pages 18-19
10. https://doi.org/10.1093/nar/gkae657
11. https://doi.org/10.1101/2023.08.01.551420
12. https://doi.org/10.1186/1471-213x-11-71;
13. https://doi.org/10.3390/ph16010094
14. https://doi.org/10.3390/ijms27031552
15. https://doi.org/10.1093/nar/gkae657;
16. https://doi.org/10.1101/2025.01.29.635480
17. https://doi.org/10.1101/2023.08.01.551420;
18. https://doi.org/10.3390/ijms27031552;
19. https://doi.org/10.1073/pnas.2001760117
20. https://doi.org/10.1186/1471-213x-11-71
21. https://doi.org/10.3390/ijms27031552,
22. https://doi.org/10.1093/nar/gkae657,
23. https://doi.org/10.1101/2025.01.29.635480,
24. https://doi.org/10.1101/2023.08.01.551420,