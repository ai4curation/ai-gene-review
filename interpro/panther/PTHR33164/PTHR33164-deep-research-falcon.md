---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T21:45:32.162165'
end_time: '2026-06-21T21:57:41.335052'
duration_seconds: 729.17
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR33164
  interpro_name: TRANSCRIPTIONAL REGULATOR, MARR FAMILY
  interpro_short_name: Not specified
  interpro_type: family
  interpro_integrated: IPR039422
  member_databases: Not specified
  n_proteins: '171881'
  n_taxa: '24294'
  n_subfamilies: '26'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: Not specified in InterPro
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 24
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR33164-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR33164-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# InterPro Family Research for GO Annotation Review

## ⚠️ CRITICAL: Family Identification Context

**BEFORE YOU BEGIN RESEARCH:** You are researching an **InterPro entry** (a protein
family / domain / superfamily signature), not a single gene. The goal is to judge
whether the GO terms that InterPro2GO attaches to this signature are appropriate for
**every** protein the signature matches.

### Target InterPro Entry (from the InterPro API):
- **Accession:** PTHR33164
- **Name:** TRANSCRIPTIONAL REGULATOR, MARR FAMILY
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR039422
- **Member database signatures:** Not specified
- **Scale:** 171881 proteins across 24294 taxa, 26 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** Not specified in InterPro

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR33164 (TRANSCRIPTIONAL REGULATOR, MARR FAMILY)**, structured to support GO annotation review.

Prioritize authoritative reviews and primary literature; you may supplement with
database annotations, but treat those as potentially outdated or over-broad.

Address each of the following:

1. **Family definition and biochemistry.** What does this family/domain do
   mechanistically? What fold is it? What are the conserved catalytic or binding
   residues? Cite primary/structural literature for all claims.

2. **InterPro2GO mapping appropriateness.** For **each** GO term currently mapped to
   this entry (listed above), state whether it is true for *every* protein the signature
   matches. Flag terms that are: (a) only true for a subfamily; (b) whole-protein
   functions attached to a domain/superfamily signature; (c) so generic (e.g. "ATP
   binding", "metal ion binding", "membrane") that they carry little information; or
   (d) process/component terms that leak into taxa where the pathway/compartment is
   absent. Where a more specific GO term would be correct, name it.

3. **Functional divergence across the family.** Are there subfamilies with divergent or
   even opposite functions (neo-functionalization)? Are there catalytically dead
   (pseudo-enzyme) members that retain the fold but lost activity? Identify the
   subfamilies and what distinguishes them.

4. **Taxonomic scope.** In which clades does this signature occur, and does any mapped
   process/component term hold across all of them?

5. **Over-annotation verdict.** Summarize whether InterPro2GO for this entry is sound,
   partially over-broad, or over-annotating, and give the recommended GO action pattern
   (ACCEPT / MODIFY-to-specific / KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED / REMOVE)
   for genes matching it. Note any recommendation for InterPro itself (e.g. demote a
   whole-protein term on a domain entry, or move it to a child entry).

Include experimental evidence where possible, and clearly distinguish experimental
findings from inference based on structure, evolution, or bioinformatics.


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

# InterPro Family Research for GO Annotation Review

## ⚠️ CRITICAL: Family Identification Context

**BEFORE YOU BEGIN RESEARCH:** You are researching an **InterPro entry** (a protein
family / domain / superfamily signature), not a single gene. The goal is to judge
whether the GO terms that InterPro2GO attaches to this signature are appropriate for
**every** protein the signature matches.

### Target InterPro Entry (from the InterPro API):
- **Accession:** PTHR33164
- **Name:** TRANSCRIPTIONAL REGULATOR, MARR FAMILY
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR039422
- **Member database signatures:** Not specified
- **Scale:** 171881 proteins across 24294 taxa, 26 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** Not specified in InterPro

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR33164 (TRANSCRIPTIONAL REGULATOR, MARR FAMILY)**, structured to support GO annotation review.

Prioritize authoritative reviews and primary literature; you may supplement with
database annotations, but treat those as potentially outdated or over-broad.

Address each of the following:

1. **Family definition and biochemistry.** What does this family/domain do
   mechanistically? What fold is it? What are the conserved catalytic or binding
   residues? Cite primary/structural literature for all claims.

2. **InterPro2GO mapping appropriateness.** For **each** GO term currently mapped to
   this entry (listed above), state whether it is true for *every* protein the signature
   matches. Flag terms that are: (a) only true for a subfamily; (b) whole-protein
   functions attached to a domain/superfamily signature; (c) so generic (e.g. "ATP
   binding", "metal ion binding", "membrane") that they carry little information; or
   (d) process/component terms that leak into taxa where the pathway/compartment is
   absent. Where a more specific GO term would be correct, name it.

3. **Functional divergence across the family.** Are there subfamilies with divergent or
   even opposite functions (neo-functionalization)? Are there catalytically dead
   (pseudo-enzyme) members that retain the fold but lost activity? Identify the
   subfamilies and what distinguishes them.

4. **Taxonomic scope.** In which clades does this signature occur, and does any mapped
   process/component term hold across all of them?

5. **Over-annotation verdict.** Summarize whether InterPro2GO for this entry is sound,
   partially over-broad, or over-annotating, and give the recommended GO action pattern
   (ACCEPT / MODIFY-to-specific / KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED / REMOVE)
   for genes matching it. Note any recommendation for InterPro itself (e.g. demote a
   whole-protein term on a domain entry, or move it to a child entry).

Include experimental evidence where possible, and clearly distinguish experimental
findings from inference based on structure, evolution, or bioinformatics.


# Comprehensive Research Report: InterPro Entry PTHR33164 (TRANSCRIPTIONAL REGULATOR, MARR FAMILY)

## Executive Summary

PTHR33164 represents the MarR (Multiple Antibiotic Resistance Regulator) family of bacterial and archaeal transcription factors, encompassing 171,881 proteins across 24,294 taxa with 26 subfamilies. This report evaluates whether Gene Ontology (GO) annotations should be attached to this InterPro entry. **Verdict: The current absence of InterPro2GO mappings for PTHR33164 is APPROPRIATE.** The extreme functional heterogeneity across subfamilies makes family-wide biological process annotations systematically over-annotating. Only universal molecular function terms should be considered, and most specific annotations should be moved to subfamily-level entries.

---

## 1. Family Definition and Biochemistry

### 1.1 Protein Fold and Structural Architecture

MarR family proteins are homodimeric transcription factors characterized by a conserved winged helix-turn-helix (wHTH) DNA-binding domain coupled with a dimerization/ligand-binding region (beggs2020marrfamilyproteins pages 1-2, nazaret2023marrfamilytranscriptional pages 1-2, beggs2020marrfamilyproteins pages 2-4). The structural organization comprises:

**Core Architecture:**
- **Dimerization domain**: Formed primarily by long intersecting α-helices (typically α1 and α6) that mediate homodimer assembly (beggs2020marrfamilyproteins pages 1-2, beggs2020marrfamilyproteins pages 2-4)
- **DNA-binding domain**: The wHTH motif consists of a three-helix bundle plus a β-hairpin "wing"; the α4 recognition helix inserts into the major groove of DNA, while the β-stranded wing contacts the minor groove (song2024structuralbasisof pages 1-2, nazaret2023marrfamilytranscriptional pages 1-2, beggs2020marrfamilyproteins pages 2-4)
- **Ligand-binding pocket**: Located at the intersubunit interface between the dimerization domain and wHTH domain, formed by residues from multiple N- and C-terminal helices (beggs2020marrfamilyproteins pages 2-4, nazaret2023marrfamilytranscriptional pages 4-6)

**Structural Evidence:**
Crystal structures of multiple MarR family members demonstrate this conserved architecture, including *E. coli* MarR, MexR from *Pseudomonas aeruginosa*, and UrtR subfamily members PecS, MftR, and HucR (song2024structuralbasisof pages 1-2, beggs2020marrfamilyproteins pages 2-4). The wHTH fold is present in approximately 73-84% of MarR-family DNA-binding domains across prokaryotes (lemmens2019transcriptionregulatorsin pages 1-2).

### 1.2 DNA Recognition Mechanism

MarR proteins bind palindromic operator sequences, typically 16-20 bp in length, through sequence-specific contacts (nazaret2023marrfamilytranscriptional pages 1-2, beggs2020marrfamilyproteins pages 2-4):

- **Recognition helix (α4)** establishes base-specific contacts in the major groove
- **β-wing** stabilizes binding through minor groove interactions
- Some family members bind longer sequences (e.g., *Dickeya dadantii* MfbR binds 48 bp sites), suggesting co-factor involvement (nazaret2023marrfamilytranscriptional pages 1-2)

Experimental evidence from DNA-bound crystal structures confirms symmetric DNA binding by MarR dimers, with each subunit contributing one wHTH module to operator recognition (song2024structuralbasisof pages 1-2, beggs2020marrfamilyproteins pages 2-4).

### 1.3 Conserved Functional Residues

**No universally conserved catalytic residues exist** because MarR proteins are regulatory, not enzymatic (nazaret2023marrfamilytranscriptional pages 1-2, nazaret2023marrfamilytranscriptional pages 4-6). Instead, subfamily-specific residues mediate ligand or signal sensing:

- **Redox-sensing subfamilies (OhrR, MarR/DUF24)**: Conserve reactive cysteine residues for oxidative signal detection. *B. subtilis* OhrR has C15 (1-Cys type); *X. campestris* OhrR has C22 and C127 (2-Cys type) that form intersubunit disulfide bonds (nazaret2023marrfamilytranscriptional pages 4-6)
- **UrtR subfamily**: Unique N-terminal α-helix contributes to uric acid recognition and dimerization, a feature absent in canonical MarR proteins (song2024structuralbasisof pages 1-2, song2024structuralbasisof pages 2-3)
- **Aromatic compound sensors**: No specific catalytic residues; ligand pockets accommodate CoA thioesters of hydroxycinnamic acids (nazaret2023marrfamilytranscriptional pages 6-7)

### 1.4 Allosteric Regulation Mechanism

Ligand binding triggers conformational changes that modulate DNA affinity (beggs2020marrfamilyproteins pages 1-2, beggs2020marrfamilyproteins pages 2-4, nazaret2023marrfamilytranscriptional pages 4-6):

**Canonical MarR mechanism**: Global repositioning of wHTH domains reduces operator affinity. For example, copper(II) oxidizes cysteines in *E. coli* MarR, promoting disulfide-linked tetramerization that sequesters DNA-recognition helices (beggs2020marrfamilyproteins pages 1-2, beggs2020marrfamilyproteins pages 2-4).

**UrtR subfamily mechanism**: Exhibits a unique **local allosteric mechanism**—uric acid binding induces conformational changes specifically in the major groove-binding core of the wHTH, generating a DNA-incompatible structure without large-scale domain movements typical of other MarR proteins (song2024structuralbasisof pages 1-2).

**Redox-sensing mechanisms**: 
- OhrR 1-Cys: Sulfenylation followed by mixed disulfide formation with bacillithiol disrupts DNA binding (nazaret2023marrfamilytranscriptional pages 4-6)
- OhrR 2-Cys: Intersubunit disulfide bond rotates wHTH modules (nazaret2023marrfamilytranscriptional pages 4-6)
- MarR/DUF24: S-alkylation by quinones reduces distance between wHTH helices, impairing DNA contacts (nazaret2023marrfamilytranscriptional pages 4-6)

---

| Feature | Canonical MarR family proteins | UrtR subfamily (MarR-derived) | Experimental evidence sources |
|---|---|---|---|
| Core architecture | Homodimeric transcription factors with a winged helix-turn-helix (wHTH) DNA-binding domain plus a dimerization/effector-binding region formed by N- and C-terminal helices; often described as having α1/α6 dimerization helices flanking the DNA-binding core (beggs2020marrfamilyproteins pages 1-2, nazaret2023marrfamilytranscriptional pages 1-2, beggs2020marrfamilyproteins pages 2-4) | Retains the MarR-like homodimeric organization with a dimerization domain and wHTH DNA-binding domain, but is distinguished by a unique N-terminal α-helix/extension that contributes to both dimerization and uric-acid recognition (song2024structuralbasisof pages 1-2, song2024structuralbasisof pages 2-3) | Crystal structures and comparative structural analyses of MarR-family proteins and UrtR proteins (beggs2020marrfamilyproteins pages 1-2, song2024structuralbasisof pages 1-2, nazaret2023marrfamilytranscriptional pages 1-2, beggs2020marrfamilyproteins pages 2-4) |
| Conserved secondary-structure logic | Typical MarR proteins contain a compact helical scaffold and a wHTH module with the recognition helix and β-wing; dimerization is mediated primarily by long intersecting helices, while the wing contributes to DNA contacts (nazaret2023marrfamilytranscriptional pages 1-2, lemmens2019transcriptionregulatorsin pages 1-2, beggs2020marrfamilyproteins pages 2-4) | UrtR proteins preserve the wHTH + dimerization framework but add the N-terminal helix as a subfamily-specific structural feature absent from canonical MarR proteins (song2024structuralbasisof pages 1-2, song2024structuralbasisof pages 2-3) | Structural review and UrtR crystal structures (song2024structuralbasisof pages 1-2, nazaret2023marrfamilytranscriptional pages 1-2, lemmens2019transcriptionregulatorsin pages 1-2) |
| DNA-binding domain and recognition helix | DNA-binding uses the wHTH domain; the recognition helix is typically α4, inserted into the major groove of B-DNA, while the β-wing commonly contacts the minor groove (beggs2020marrfamilyproteins pages 1-2, nazaret2023marrfamilytranscriptional pages 1-2, beggs2020marrfamilyproteins pages 2-4) | UrtR uses the same overall logic: the α4 recognition helix binds the major groove and the β-stranded wing binds the minor groove in operator DNA complexes (song2024structuralbasisof pages 1-2) | DNA-bound structural models and family reviews (beggs2020marrfamilyproteins pages 1-2, song2024structuralbasisof pages 1-2, beggs2020marrfamilyproteins pages 2-4) |
| DNA sequence specificity | Usually binds palindromic operator sequences, commonly ~16–20 bp; some members bind longer or more degenerate sites depending on subfamily and regulon architecture (nazaret2023marrfamilytranscriptional pages 1-2, beggs2020marrfamilyproteins pages 2-4) | Also binds operator DNA specifically, but target sequences are subfamily/regulon specific; UrtR proteins repress cognate promoters in the absence of uric acid and release upon ligand binding (song2024structuralbasisof pages 1-2, nazaret2023marrfamilytranscriptional pages 6-7) | Biochemical and structural studies plus comparative reviews (song2024structuralbasisof pages 1-2, nazaret2023marrfamilytranscriptional pages 1-2, nazaret2023marrfamilytranscriptional pages 6-7) |
| Ligand-binding pocket location | In canonical MarR proteins, ligand/effector-binding pockets are typically formed by residues from several N- and C-terminal helices and lie at or near the intersubunit region adjacent to the DNA-binding lobes; pocket chemistry varies strongly by subfamily (phenolics, antibiotics, metals, oxidants, aromatic-CoA thioesters, etc.) (beggs2020marrfamilyproteins pages 1-2, nazaret2023marrfamilytranscriptional pages 1-2, beggs2020marrfamilyproteins pages 2-4, nazaret2023marrfamilytranscriptional pages 4-6, nazaret2023marrfamilytranscriptional pages 6-7) | UrtR binds uric acid in an intersubunit pocket positioned between the dimerization domain and the wHTH domain; the unique N-terminal helix contributes to ligand recognition, making this pocket mechanistically distinctive within the MarR superfamily (song2024structuralbasisof pages 1-2) | Crystal structures and mutational analyses of canonical MarR-family members and UrtR proteins (song2024structuralbasisof pages 1-2, beggs2020marrfamilyproteins pages 2-4, nazaret2023marrfamilytranscriptional pages 4-6, nazaret2023marrfamilytranscriptional pages 6-7) |
| Ligand/signal diversity | Highly variable across subfamilies: salicylate and other phenolics, antibiotics/drug-like molecules, copper, organic hydroperoxides, reactive electrophiles, quinones, p-coumaroyl-CoA/feruloyl-CoA, and other niche-specific metabolites or redox signals (beggs2020marrfamilyproteins pages 1-2, nazaret2023marrfamilytranscriptional pages 1-2, beggs2020marrfamilyproteins pages 2-4, nazaret2023marrfamilytranscriptional pages 4-6, nazaret2023marrfamilytranscriptional pages 6-7) | Specialized primarily for uric acid sensing; some UrtR-family studies also examine xanthine-related purine binding, but uric acid is the defining physiological signal (song2024structuralbasisof pages 1-2, nazaret2023marrfamilytranscriptional pages 6-7) | Functional/genetic studies and reviews of specific MarR branches (song2024structuralbasisof pages 1-2, nazaret2023marrfamilytranscriptional pages 1-2, nazaret2023marrfamilytranscriptional pages 4-6, nazaret2023marrfamilytranscriptional pages 6-7) |
| Allosteric mechanism of regulation | General rule: effector binding or redox chemistry changes the dimer conformation and reduces operator affinity. In many canonical MarR proteins, this involves global repositioning of the wHTH domains; in redox-sensing branches, cysteine oxidation can trigger disulfides, tetramerization, or S-alkylation that disrupt productive DNA-binding geometry (beggs2020marrfamilyproteins pages 1-2, beggs2020marrfamilyproteins pages 2-4, nazaret2023marrfamilytranscriptional pages 4-6) | UrtR uses a more local allosteric mechanism: uric-acid binding remodels the major-groove-binding core element of the wHTH into a DNA-incompatible state, rather than relying primarily on the broader global shifts typical of many canonical MarR proteins (song2024structuralbasisof pages 1-2) | UrtR structural study explicitly contrasts its mechanism with other MarR proteins; canonical examples from structural/review literature (song2024structuralbasisof pages 1-2, beggs2020marrfamilyproteins pages 2-4, nazaret2023marrfamilytranscriptional pages 4-6) |
| Conserved reactive residues | No single catalytic residue is universally conserved across the whole family because function is regulatory rather than enzymatic; instead, different subfamilies conserve distinct ligand- or redox-sensing residues, especially cysteines in OhrR/DUF24-like branches (nazaret2023marrfamilytranscriptional pages 1-2, nazaret2023marrfamilytranscriptional pages 4-6, nazaret2023marrfamilytranscriptional pages 6-7) | UrtR proteins share distinct sequence conservation patterns in the N-terminal extension and remaining regions that are not found in canonical MarR proteins, consistent with uric-acid specialization (song2024structuralbasisof pages 1-2, song2024structuralbasisof pages 2-3) | Comparative sequence/structure analysis and subfamily-specific biochemistry (song2024structuralbasisof pages 1-2, nazaret2023marrfamilytranscriptional pages 4-6, nazaret2023marrfamilytranscriptional pages 6-7) |
| Biochemical consequence of ligand binding | Usually derepression of target genes after loss of high-affinity DNA binding; however, some family members can activate transcription or behave as dual regulators depending on promoter context and regulon wiring (nazaret2023marrfamilytranscriptional pages 1-2, beggs2020marrfamilyproteins pages 2-4, nazaret2023marrfamilytranscriptional pages 6-7) | In the absence of uric acid, UrtR represses target promoters; uric acid binding promotes dissociation from promoter DNA and transcriptional activation/derepression of virulence, oxidative-stress, or metabolic genes depending on the organism (song2024structuralbasisof pages 1-2, nazaret2023marrfamilytranscriptional pages 6-7) | Genetic, biochemical, and structural studies (song2024structuralbasisof pages 1-2, beggs2020marrfamilyproteins pages 2-4, nazaret2023marrfamilytranscriptional pages 6-7) |
| Functional implication for annotation | Structural conservation supports a broad family-level inference of sequence-specific DNA-binding transcription regulator function, but ligand specificity and regulated biological process are highly subfamily-specific and should not be generalized across the full family (nwokocha2024regulationofbacterial pages 1-2, nazaret2023marrfamilytranscriptional pages 1-2, gupta2019marrfamilytranscription pages 1-2, nazaret2023marrfamilytranscriptional pages 6-7) | UrtR-specific features justify narrower child/subfamily annotations related to uric-acid-responsive transcriptional regulation rather than projecting these properties onto all MarR proteins (song2024structuralbasisof pages 1-2, nazaret2023marrfamilytranscriptional pages 6-7) | Comparative family/subfamily reviews and structural evidence (nwokocha2024regulationofbacterial pages 1-2, song2024structuralbasisof pages 1-2, nazaret2023marrfamilytranscriptional pages 1-2, nazaret2023marrfamilytranscriptional pages 6-7) |


*Table: This table compares conserved structural and biochemical features of canonical MarR proteins with the UrtR subfamily. It highlights which properties are family-wide versus subfamily-specific, which is useful for GO annotation review.*

---

## 2. InterPro2GO Mapping Appropriateness

**Current status**: PTHR33164 has **no InterPro2GO mappings**.

### 2.1 Assessment of Potential GO Terms

Given the functional diversity documented in the literature, potential GO annotations would include:

**Molecular Function:**
- **DNA-binding transcription factor activity (GO:0003700)**: TRUE for all members—this is the universal biochemical function (beggs2020marrfamilyproteins pages 1-2, song2024structuralbasisof pages 1-2, nazaret2023marrfamilytranscriptional pages 1-2, beggs2020marrfamilyproteins pages 2-4)
- **Sequence-specific DNA binding (GO:0043565)**: TRUE for all members—palindromic operator recognition is conserved (song2024structuralbasisof pages 1-2, nazaret2023marrfamilytranscriptional pages 1-2, beggs2020marrfamilyproteins pages 2-4)
- **Small molecule binding**: TRUE but highly subfamily-specific—phenolics, antibiotics, metals, organic hydroperoxides, aromatic-CoA thioesters, uric acid, etc. (beggs2020marrfamilyproteins pages 1-2, song2024structuralbasisof pages 1-2, beggs2020marrfamilyproteins pages 2-4, nazaret2023marrfamilytranscriptional pages 4-6, nazaret2023marrfamilytranscriptional pages 6-7)

**Biological Process (subfamily-specific, NOT universal):**
- **Response to antibiotic (GO:0046677)**: Only true for antibiotic resistance subfamilies (MarR, MprA, MexR, FarR) (beggs2020marrfamilyproteins pages 1-2, beggs2020marrfamilyproteins pages 2-4, wojcicki2021transcriptionalregulationof pages 2-5)
- **Response to oxidative stress (GO:0006979)**: Only true for OhrR and MarR/DUF24 redox-sensing subfamilies (nazaret2023marrfamilytranscriptional pages 4-6, nazaret2023marrfamilytranscriptional pages 6-7)
- **Aromatic compound metabolic process**: Only true for HcaR, CouR, FerR subfamilies regulating catabolism (nazaret2023marrfamilytranscriptional pages 6-7)
- **Pathogenesis/virulence**: Only true for pathogen-specific subfamilies like PecS, MftR, SlyA (nwokocha2024regulationofbacterial pages 1-2, nazaret2023marrfamilytranscriptional pages 6-7)
- **Biofilm formation**: Only documented for BifR (nazaret2023marrfamilytranscriptional pages 4-6, nazaret2023marrfamilytranscriptional pages 6-7)

**Cellular Component:**
- **Cytoplasm/nucleoid**: TRUE for all members as prokaryotic DNA-binding TFs localize to the cytoplasm/nucleoid region (inferred from function, not experimentally validated for all members)

### 2.2 Over-Annotation Flags

**(a) Subfamily-specific functions projected family-wide**: Any biological process term (antibiotic resistance, oxidative stress response, virulence, aromatic catabolism) applied to PTHR33164 would **systematically over-annotate** proteins from subfamilies with different functions. For example:
- Applying "response to antibiotic" would incorrectly annotate OhrR proteins (which sense organic hydroperoxides)
- Applying "aromatic compound catabolic process" would incorrectly annotate MarR proteins (which regulate multidrug efflux)

**(b) Whole-protein functions on a family entry**: PTHR33164 is a **family**-level entry, not a domain. Family entries can support whole-protein function terms, but only if functionally homogeneous. MarR family exhibits **extreme functional divergence** through neo-functionalization, making family-wide process terms inappropriate (nazaret2023marrfamilytranscriptional pages 1-2, gupta2019marrfamilytranscription pages 1-2, nazaret2023marrfamilytranscriptional pages 6-7).

**(c) Generic terms with low information content**: Terms like "metal ion binding" or "small molecule binding" are too generic given that different subfamilies bind chemically unrelated ligands with distinct physiological consequences (beggs2020marrfamilyproteins pages 2-4, nazaret2023marrfamilytranscriptional pages 4-6, nazaret2023marrfamilytranscriptional pages 6-7).

**(d) Taxon-inappropriate annotations**: 
- Virulence-related terms are only relevant in pathogenic bacteria, not in environmental or archaeal species (nwokocha2024regulationofbacterial pages 1-2, gupta2019marrfamilytranscription pages 1-2, nazaret2023marrfamilytranscriptional pages 6-7)
- Plant-interaction processes (aromatic compound degradation from plant exudates) are irrelevant in clinical pathogens (nazaret2023marrfamilytranscriptional pages 6-7)
- Multidrug efflux regulation is clinically relevant but not universally present across free-living soil bacteria

### 2.3 Recommended GO Actions

**For PTHR33164 (family level):**
- **ACCEPT** current state (no mappings) as most appropriate
- **IF annotations are required**: Limit to universal molecular functions only:
  - DNA-binding transcription factor activity (GO:0003700)
  - Sequence-specific DNA binding (GO:0043565)
- **AVOID** all biological process and cellular component terms at this level

**For specific GO annotations:**
- **MOVE** to subfamily-level InterPro entries (e.g., separate child entries for UrtR, OhrR, PecS, canonical MarR-antibiotic subfamilies)
- **MARK_AS_CONDITIONAL** if process terms must be added, clearly noting they apply only to specific subfamilies

---

| Subfamily Name | Representative Members | Ligand/Signal Sensed | Primary Function/Regulon | Mechanism of Sensing | Taxonomic Distribution | Key Citations |
|---|---|---|---|---|---|---|
| UrtR | PecS (*Pectobacterium atrosepticum*), MftR (*Burkholderia thailandensis*), HucR (*Deinococcus radiodurans*) | Uric acid; in some members also xanthine-related purine signals | Coordinates virulence, oxidative-stress protection, urate metabolism, and secondary metabolism; typically represses target promoters until uric acid accumulates | Effector binds an intersubunit pocket between dimerization domain and wHTH domain; UrtR proteins have a distinctive N-terminal helix contributing to dimerization and uric-acid recognition; ligand binding causes a local allosteric change that makes the DNA-binding conformation incompatible with operator binding | Broad bacterial distribution; reported across Pseudomonadota, Cyanobacteria, Actinomycetota, and Bacillota | (song2024structuralbasisof pages 1-2, song2024structuralbasisof pages 2-3, nazaret2023marrfamilytranscriptional pages 6-7) |
| OhrR | OhrR (*Bacillus subtilis*), OhrR (*Xanthomonas campestris*) | Organic hydroperoxides (ROOH); oxidative stress | Controls oxidative-stress defense genes, especially *ohr* and related peroxide-resistance regulons | Redox sensing through one or two reactive cysteines: 1-Cys OhrR forms mixed disulfides with low-molecular-weight thiols after sulfenylation; 2-Cys OhrR forms intersubunit disulfides that rotate/reposition the wHTH and disrupt DNA binding | Widespread in bacteria, including Firmicutes and phytopathogenic Pseudomonadota/Xanthomonadales | (nazaret2023marrfamilytranscriptional pages 4-6, nazaret2023marrfamilytranscriptional pages 6-7) |
| MarR/DUF24 redox-sensing branch | YodB (*Bacillus subtilis*), CatR, HypR, MhqR | Reactive electrophile species, quinones, diamide, NaOCl, other redox-active compounds | Regulates detoxification, quinone/electrophile response, nitric-oxide reduction and catechol-degradation-associated genes, and related stress regulons | Reactive cysteines undergo disulfide formation or S-alkylation depending on the electrophile/oxidant, producing conformational changes in DNA-recognition helices and reduced operator binding | Common in bacteria adapted to oxidative/electrophile stress, including soil and plant-associated taxa | (nazaret2023marrfamilytranscriptional pages 4-6, nazaret2023marrfamilytranscriptional pages 6-7) |
| Canonical MarR antibiotic/stress repressors | MarR (*Escherichia coli*), MprA/EmrR (*E. coli*), MexR (*Pseudomonas aeruginosa*), FarR (*Neisseria gonorrhoeae*) | Phenolics (e.g. salicylate), antibiotics/drug-like molecules, copper(II), anti-repressor peptides in some systems | Controls multidrug resistance networks and efflux pumps, including *marRAB*, *emrRAB*, *mexAB-oprM* and related loci; can also affect virulence-associated traits | Small molecules or redox signals alter dimer conformation and lower DNA affinity; in *E. coli* MarR, Cu(II)-dependent oxidation of cysteine promotes disulfide-linked tetramerization; MexR is additionally controlled by anti-repressor ArmR | Especially abundant in Gram-negative bacteria, including Enterobacteriaceae, *Pseudomonas*, and *Neisseria*; MarR family broadly distributed in bacteria and archaea | (beggs2020marrfamilyproteins pages 1-2, beggs2020marrfamilyproteins pages 2-4, chubiz2023themarsox pages 1-2) |
| PecS branch | PecS (*Dickeya dadantii*), PecS (*Pectobacterium atrosepticum*) | Uric acid in some species; also H2O2, organic hydroperoxides, pH, and species-specific host/environmental signals | Represses the conserved *pecS-pecM* intergenic region and modulates broader virulence/fness regulons, including plant-cell-wall-degrading enzymes and oxidative-stress-related functions | DNA binding to the shared *pecS-pecM* region is conserved, but binding mode, ligand preference, and regulon breadth differ by species; in urate-responsive members, sensing follows the UrtR-like allosteric mechanism | Plant-pathogenic bacteria, especially soft-rot Enterobacterales such as *Dickeya* and *Pectobacterium* | (nwokocha2024regulationofbacterial pages 1-2, song2024structuralbasisof pages 1-2, nazaret2023marrfamilytranscriptional pages 6-7) |
| Aromatic-compound catabolism regulators | HcaR (*Agrobacterium fabrum*), HcaR (*Acinetobacter* sp. ADP1), CouR (*Rhodopseudomonas palustris*), FerR, DesR | Hydroxycinnamoyl-CoA or related aromatic-CoA thioesters (e.g. p-coumaroyl-CoA, feruloyl-CoA), vanillate/syringate for some branches | Represses aromatic-compound degradation pathways, enabling detoxification and use of plant-derived phenylpropanoids as carbon sources | Direct binding of pathway intermediates or CoA thioesters relieves DNA binding and derepresses catabolic operons | Common in plant-associated and soil bacteria using phenylpropanoid-rich niches | (nazaret2023marrfamilytranscriptional pages 6-7, nazaret2023marrfamilytranscriptional pages 1-2) |
| BifR-like copper/redox regulators | BifR (*Burkholderia thailandensis*) | Copper; membrane/redox stress | Regulates biofilm-associated genes and stress adaptation | Oxidation promotes tetramer formation, but unlike canonical MarR this can increase repression, producing a “super-repressor” state | Reported in *Burkholderia* and related environmental/pathogenic Proteobacteria | (nazaret2023marrfamilytranscriptional pages 4-6, nazaret2023marrfamilytranscriptional pages 6-7, gupta2019marrfamilytranscription pages 1-2) |
| TctR/SlyA-like virulence regulators within MarR family | TctR (*Burkholderia* spp.), SlyA (*Dickeya* spp.) | Often not clearly defined; likely niche-specific environmental/host cues | Controls virulence-associated genes, including secretion systems or plant-cell-wall-degrading functions, with some members acting as activators or dual regulators rather than simple repressors | Family-conserved wHTH scaffold retained, but regulon wiring and transcriptional output have diverged; activation/repression depends on promoter context and network integration | Distributed among diverse pathogens and symbionts; especially notable in plant- and host-associated Proteobacteria | (nazaret2023marrfamilytranscriptional pages 6-7, gupta2019marrfamilytranscription pages 1-2, nazaret2023marrfamilytranscriptional pages 1-2) |


*Table: This table summarizes experimentally characterized MarR-family subfamilies, their sensed signals, regulons, sensing mechanisms, and phylogenetic spread. It is useful for judging which functions are conserved across the family versus restricted to specific subfamilies.*

---

## 3. Functional Divergence Across the Family

### 3.1 Major Subfamilies and Neo-Functionalization

The MarR family exhibits extensive **neo-functionalization**, with subfamilies evolving distinct ligand specificities and regulatory targets while retaining the conserved wHTH scaffold (nwokocha2024regulationofbacterial pages 1-2, nazaret2023marrfamilytranscriptional pages 1-2, gupta2019marrfamilytranscription pages 1-2, nazaret2023marrfamilytranscriptional pages 6-7):

**UrtR subfamily (uric acid-responsive)**: Specialized for sensing uric acid, a signal of host environment in pathogens. Regulates virulence (PecS in *Dickeya*, MftR in *Burkholderia*), oxidative stress defense, and urate catabolism (HucR in *Deinococcus*). Distinguished by unique N-terminal α-helix (song2024structuralbasisof pages 1-2, nazaret2023marrfamilytranscriptional pages 6-7).

**OhrR subfamily (organic hydroperoxide sensors)**: Divided into 1-Cys (e.g., *B. subtilis* OhrR) and 2-Cys (e.g., *X. campestris* OhrR) types. Regulate oxidative stress response genes through cysteine-based redox sensing (nazaret2023marrfamilytranscriptional pages 4-6, nazaret2023marrfamilytranscriptional pages 6-7).

**MarR/DUF24 subfamily (reactive electrophile sensors)**: Respond to quinones, diamides, aldehydes through cysteine S-alkylation or disulfide formation. Examples: *B. subtilis* YodB, CatR, MhqR (nazaret2023marrfamilytranscriptional pages 4-6, nazaret2023marrfamilytranscriptional pages 6-7).

**Canonical antibiotic resistance regulators**: Sense antibiotics, phenolics, or metals. *E. coli* MarR/MprA, *P. aeruginosa* MexR, *N. gonorrhoeae* FarR regulate multidrug efflux pumps (beggs2020marrfamilyproteins pages 1-2, beggs2020marrfamilyproteins pages 2-4, wojcicki2021transcriptionalregulationof pages 2-5).

**PecS subfamily**: Global virulence regulators in plant pathogens (*Dickeya*, *Pectobacterium*). Regulate plant cell wall-degrading enzymes, type II secretion, and oxidative stress genes. Binding mode and regulon vary by species despite conserved *pecS-pecM* architecture (nwokocha2024regulationofbacterial pages 1-2, nazaret2023marrfamilytranscriptional pages 6-7).

**Aromatic compound catabolism regulators**: HcaR, CouR, FerR sense hydroxycinnamic acid-CoA thioesters from plant-derived phenylpropanoids. Enable utilization of aromatic compounds as carbon sources in rhizosphere bacteria (nazaret2023marrfamilytranscriptional pages 6-7).

**BifR (copper-responsive biofilm regulator)**: Unique "super-repressor" mechanism—oxidation promotes tetramerization that *increases* rather than decreases repression (nazaret2023marrfamilytranscriptional pages 4-6, nazaret2023marrfamilytranscriptional pages 6-7).

### 3.2 Regulatory Mode Divergence

MarR family members display functional plasticity in transcriptional output (nazaret2023marrfamilytranscriptional pages 1-2, nazaret2023marrfamilytranscriptional pages 6-7):

- **Repressors** (most common): Bind operator DNA in absence of ligand, release upon signal detection
- **Activators**: Some members (e.g., certain PecS orthologs, WggR in *Sinorhizobium*) activate transcription (nazaret2023marrfamilytranscriptional pages 6-7)
- **Dual regulators**: Same protein can repress some promoters and activate others depending on promoter architecture and regulatory network context (nazaret2023marrfamilytranscriptional pages 6-7)

### 3.3 Catalytically Dead or Pseudo-Enzyme Members?

**No catalytically dead members identified.** MarR proteins are regulatory transcription factors, not enzymes, so the concept of "catalytically dead" is not applicable. However, functional divergence manifests as:

- **Loss of ligand responsiveness**: Some orthologs may have lost ancestral ligand-binding capacity
- **Regulatory rewiring**: Orthologous regulators control disparate gene sets in different species due to promoter evolution (nwokocha2024regulationofbacterial pages 1-2, gupta2019marrfamilytranscription pages 1-2)

### 3.4 Distinguishing Features of Subfamilies

Subfamilies are distinguished by:
1. **Ligand/signal specificity** (chemical nature of sensed molecule)
2. **Sensing mechanism** (redox chemistry vs. direct ligand binding vs. protein-protein interactions)
3. **Regulon composition** (which genes are regulated)
4. **Taxonomic distribution** (some subfamilies restricted to specific bacterial lineages)
5. **Structural features** (e.g., UrtR N-terminal helix, number of reactive cysteines in redox sensors)

---

## 4. Taxonomic Scope

### 4.1 Distribution Across Prokaryotic Clades

**Bacteria** (primary domain of MarR family):
- **Pseudomonadota (Proteobacteria)**: Abundant in *Escherichia*, *Pseudomonas*, *Burkholderia*, *Neisseria*, *Xanthomonas*, *Dickeya*, *Pectobacterium*, *Agrobacterium* (beggs2020marrfamilyproteins pages 1-2, nwokocha2024regulationofbacterial pages 1-2, gupta2019marrfamilytranscription pages 1-2, beggs2020marrfamilyproteins pages 2-4, nazaret2023marrfamilytranscriptional pages 6-7)
- **Firmicutes (Bacillota)**: Well-represented in *Bacillus*, *Staphylococcus*, *Streptomyces* (nazaret2023marrfamilytranscriptional pages 4-6, nazaret2023marrfamilytranscriptional pages 6-7)
- **Actinomycetota (Actinobacteria)**: Present in *Mycobacterium*, *Corynebacterium*, *Streptomyces* (nazaret2023marrfamilytranscriptional pages 6-7)
- **Cyanobacteria**: UrtR subfamily documented (song2024structuralbasisof pages 1-2)
- **Other phyla**: MarR proteins identified in most bacterial phyla (floresbautista2020decipheringthefunctional pages 1-2, perezrueda2018abundancediversityand pages 1-2)

**Archaea** (less abundant but present):
- Identified in Euryarchaeota and Crenarchaeota lineages (lemmens2019transcriptionregulatorsin pages 1-2)
- Lower abundance than in bacteria; archaeal MarR proteins show sequence divergence from bacterial orthologs (lemmens2019transcriptionregulatorsin pages 1-2)

**Genome-scale distributions**:
- Present in >12,000 bacterial and archaeal genomes (nazaret2023marrfamilytranscriptional pages 1-2)
- PTHR33164 encompasses 171,881 proteins across 24,294 taxa
- Abundance correlates with genome size and lifestyle: **free-living bacteria encode more MarR proteins** than intracellular/obligate pathogenic species (floresbautista2020decipheringthefunctional pages 1-2, perezrueda2018abundancediversityand pages 1-2)
- **Absent from eukaryotes** (lemmens2019transcriptionregulatorsin pages 1-2)

### 4.2 Taxonomic Compatibility of Mapped Terms

**No single biological process term applies universally across all taxa containing MarR family proteins:**

- **Antibiotic resistance**: Relevant in clinical pathogens and resistant environmental bacteria, but not in archaea or most soil bacteria without antibiotic exposure (beggs2020marrfamilyproteins pages 2-4, wojcicki2021transcriptionalregulationof pages 2-5)
- **Plant interactions**: Relevant only in plant-associated bacteria (rhizosphere, phytopathogens, symbionts), not in human pathogens or archaea (nazaret2023marrfamilytranscriptional pages 1-2, nazaret2023marrfamilytranscriptional pages 6-7)
- **Virulence**: Only applicable to pathogenic species, not to free-living environmental bacteria or archaea (nwokocha2024regulationofbacterial pages 1-2, gupta2019marrfamilytranscription pages 1-2, nazaret2023marrfamilytranscriptional pages 6-7)
- **Oxidative stress response**: Broad but not universal—some subfamilies sense other signals (aromatics, antibiotics, uric acid) (nazaret2023marrfamilytranscriptional pages 4-6, nazaret2023marrfamilytranscriptional pages 6-7)

**Conclusion**: The extreme taxonomic and ecological breadth (24,294 taxa spanning environmental, pathogenic, symbiotic, and archaeal lifestyles) precludes application of any single process term to PTHR33164.

---

## 5. Over-Annotation Verdict and Recommendations

### 5.1 Summary Verdict

**The absence of InterPro2GO mappings for PTHR33164 is APPROPRIATE and should be maintained.**

**Rationale:**
1. **PTHR33164 is a FAMILY-level entry** with 26 subfamilies, each exhibiting distinct ligand specificity, sensing mechanisms, and regulatory targets
2. **Extreme functional heterogeneity**: Subfamilies have undergone neo-functionalization for antibiotic resistance, aromatic catabolism, virulence, oxidative stress, biofilm formation, and other processes—**none of which are universal**
3. **Context-dependent regulation**: Same subfamily members can be repressors or activators depending on species and promoter architecture
4. **Taxonomic incompatibility**: Spans 24,294 taxa from clinical pathogens to soil bacteria to archaea, where process annotations (virulence, plant interactions, antibiotic resistance) leak into inappropriate contexts
5. **Entry type permits whole-protein terms**, but functional diversity is so extreme that no biological process applies to all 171,881 proteins

### 5.2 Recommended GO Action Pattern

**For PTHR33164 (current state):**
- **ACCEPT** (maintain no InterPro2GO mappings)

**IF annotations are required at family level:**
- **MODIFY-to-specific**: Restrict to universal molecular functions only
  - DNA-binding transcription factor activity (GO:0003700)
  - Sequence-specific DNA binding (GO:0043565)
- **AVOID** all biological process terms (response to antibiotic, oxidative stress, aromatic metabolism, virulence, biofilm formation)
- **AVOID** generic molecular function terms with low information (small molecule binding, metal ion binding)

**Preferred alternative approach:**
- **MOVE annotations to subfamily-level InterPro entries**:
  - Create/identify child entries for UrtR, OhrR, canonical MarR-antibiotic, PecS, aromatic catabolism subfamilies
  - Apply subfamily-specific biological process terms to these child entries
  - Document subfamily diagnostic features (N-terminal helix in UrtR, reactive cysteines in redox sensors)

**IF process terms must be added to PTHR33164:**
- **MARK_AS_CONDITIONAL** with clear documentation that terms apply only to specific subfamilies
- **KEEP_AS_NON_CORE** to indicate annotations are low-confidence at family level

### 5.3 Recommendations for InterPro

1. **Maintain current annotation-free status** for PTHR33164
2. **Develop subfamily-level entries** within the PANTHER hierarchy or linked InterPro entries for:
   - UrtR (uric acid-responsive virulence/metabolism regulators)
   - OhrR (organic hydroperoxide sensors)
   - MarR/DUF24 (reactive electrophile sensors)
   - Canonical MarR (antibiotic resistance/efflux regulators)
   - PecS (plant pathogen virulence regulators)
   - Aromatic catabolism regulators (HcaR-like)
3. **Document subfamily diagnostic features** in InterPro descriptions to guide manual curation
4. **Cross-reference** to experimentally characterized members in each subfamily for evidence-based annotation

### 5.4 Scientific Justification

The MarR family exemplifies a **conserved structural scaffold supporting extreme functional plasticity**. While the wHTH DNA-binding mechanism is universal (justifying molecular function annotations), the regulatory targets, sensed signals, and biological outcomes are subfamily-specific products of evolution in diverse ecological niches (nwokocha2024regulationofbacterial pages 1-2, nazaret2023marrfamilytranscriptional pages 1-2, gupta2019marrfamilytranscription pages 1-2, nazaret2023marrfamilytranscriptional pages 6-7). Projecting any single biological process term onto this family would systematically misannotate the majority of its members.

**Experimental support**: All characterized MarR subfamilies show:
- Conserved DNA-binding via wHTH (structural evidence) (song2024structuralbasisof pages 1-2, beggs2020marrfamilyproteins pages 2-4)
- Subfamily-specific ligand pockets and regulons (genetic/biochemical evidence) (beggs2020marrfamilyproteins pages 2-4, nazaret2023marrfamilytranscriptional pages 4-6, nazaret2023marrfamilytranscriptional pages 6-7)
- Independent evolution of regulatory networks even among orthologs (comparative genomics) (nwokocha2024regulationofbacterial pages 1-2, gupta2019marrfamilytranscription pages 1-2, nazaret2023marrfamilytranscriptional pages 6-7)

This body of evidence conclusively demonstrates that **functional annotations must be subfamily-specific rather than family-wide** to avoid over-annotation.

---

## References

All citations in this report use context IDs () corresponding to the evidence gathered from peer-reviewed literature published 2015-2025, with prioritization of 2020-2024 sources as requested. Key review articles include Beggs et al. 2020 (beggs2020marrfamilyproteins pages 1-2), Song et al. 2024 (song2024structuralbasisof pages 1-2), Nazaret et al. 2023 (nazaret2023marrfamilytranscriptional pages 1-2), Nwokocha et al. 2024 (nwokocha2024regulationofbacterial pages 1-2), and Gupta et al. 2019 (gupta2019marrfamilytranscription pages 1-2) for subfamily-specific characterization.

References

1. (beggs2020marrfamilyproteins pages 1-2): Grace A. Beggs, Richard G. Brennan, and Mehreen Arshad. Marr family proteins are important regulators of clinically relevant antibiotic resistance. Protein Science, 29:647-653, Nov 2020. URL: https://doi.org/10.1002/pro.3769, doi:10.1002/pro.3769. This article has 84 citations and is from a peer-reviewed journal.

2. (nazaret2023marrfamilytranscriptional pages 1-2): Fanny Nazaret, Geneviève Alloing, Karine Mandon, and Pierre Frendo. Marr family transcriptional regulators and their roles in plant-interacting bacteria. Microorganisms, 11:1936, Jul 2023. URL: https://doi.org/10.3390/microorganisms11081936, doi:10.3390/microorganisms11081936. This article has 15 citations.

3. (beggs2020marrfamilyproteins pages 2-4): Grace A. Beggs, Richard G. Brennan, and Mehreen Arshad. Marr family proteins are important regulators of clinically relevant antibiotic resistance. Protein Science, 29:647-653, Nov 2020. URL: https://doi.org/10.1002/pro.3769, doi:10.1002/pro.3769. This article has 84 citations and is from a peer-reviewed journal.

4. (song2024structuralbasisof pages 1-2): Wan Seok Song, Dong Uk Ki, Hye Yeon Cho, Oh Hyun Kwon, Hongbaek Cho, and Sung-il Yoon. Structural basis of transcriptional regulation by urtr in response to uric acid. Nucleic Acids Research, 52:13192-13205, Nov 2024. URL: https://doi.org/10.1093/nar/gkae922, doi:10.1093/nar/gkae922. This article has 13 citations and is from a highest quality peer-reviewed journal.

5. (nazaret2023marrfamilytranscriptional pages 4-6): Fanny Nazaret, Geneviève Alloing, Karine Mandon, and Pierre Frendo. Marr family transcriptional regulators and their roles in plant-interacting bacteria. Microorganisms, 11:1936, Jul 2023. URL: https://doi.org/10.3390/microorganisms11081936, doi:10.3390/microorganisms11081936. This article has 15 citations.

6. (lemmens2019transcriptionregulatorsin pages 1-2): Liesbeth Lemmens, Hassan Ramadan Maklad, Indra Bervoets, and Eveline Peeters. Transcription regulators in archaea: homologies and differences with bacterial regulators. Journal of Molecular Biology, 431:4132-4146, Sep 2019. URL: https://doi.org/10.1016/j.jmb.2019.05.045, doi:10.1016/j.jmb.2019.05.045. This article has 65 citations and is from a domain leading peer-reviewed journal.

7. (song2024structuralbasisof pages 2-3): Wan Seok Song, Dong Uk Ki, Hye Yeon Cho, Oh Hyun Kwon, Hongbaek Cho, and Sung-il Yoon. Structural basis of transcriptional regulation by urtr in response to uric acid. Nucleic Acids Research, 52:13192-13205, Nov 2024. URL: https://doi.org/10.1093/nar/gkae922, doi:10.1093/nar/gkae922. This article has 13 citations and is from a highest quality peer-reviewed journal.

8. (nazaret2023marrfamilytranscriptional pages 6-7): Fanny Nazaret, Geneviève Alloing, Karine Mandon, and Pierre Frendo. Marr family transcriptional regulators and their roles in plant-interacting bacteria. Microorganisms, 11:1936, Jul 2023. URL: https://doi.org/10.3390/microorganisms11081936, doi:10.3390/microorganisms11081936. This article has 15 citations.

9. (nwokocha2024regulationofbacterial pages 1-2): George C. Nwokocha, Arpita Ghosh, and Anne Grove. Regulation of bacterial virulence genes by pecs family transcription factors. Journal of Bacteriology, Oct 2024. URL: https://doi.org/10.1128/jb.00302-24, doi:10.1128/jb.00302-24. This article has 5 citations and is from a peer-reviewed journal.

10. (gupta2019marrfamilytranscription pages 1-2): Ashish Gupta, Anuja Pande, Afsana Sabrin, Sudarshan S. Thapa, Brennan W. Gioe, and Anne Grove. Marr family transcription factors from <i>burkholderia</i> species: hidden clues to control of virulence-associated genes. Microbiology and Molecular Biology Reviews, Feb 2019. URL: https://doi.org/10.1128/mmbr.00039-18, doi:10.1128/mmbr.00039-18. This article has 45 citations and is from a domain leading peer-reviewed journal.

11. (wojcicki2021transcriptionalregulationof pages 2-5): Michał Wójcicki, Olga Świder, Kamila J. Daniluk, Paulina Średnicka, Monika Akimowicz, Marek Ł. Roszko, Barbara Sokołowska, and Edyta Juszczuk-Kubiak. Transcriptional regulation of the multiple resistance mechanisms in salmonella—a review. Pathogens, 10:801, Jun 2021. URL: https://doi.org/10.3390/pathogens10070801, doi:10.3390/pathogens10070801. This article has 40 citations.

12. (chubiz2023themarsox pages 1-2): Lon M. Chubiz. The mar, sox, and rob systems. EcoSal Plus, Dec 2023. URL: https://doi.org/10.1128/ecosalplus.esp-0010-2022, doi:10.1128/ecosalplus.esp-0010-2022. This article has 16 citations.

13. (floresbautista2020decipheringthefunctional pages 1-2): Emanuel Flores-Bautista, Rafael Hernandez-Guerrero, Alejandro Huerta-Saquero, Silvia Tenorio-Salgado, Nancy Rivera-Gomez, Alba Romero, Jose Antonio Ibarra, and Ernesto Perez-Rueda. Deciphering the functional diversity of dna-binding transcription factors in bacteria and archaea organisms. PLoS ONE, 15:e0237135, Aug 2020. URL: https://doi.org/10.1371/journal.pone.0237135, doi:10.1371/journal.pone.0237135. This article has 26 citations and is from a peer-reviewed journal.

14. (perezrueda2018abundancediversityand pages 1-2): Ernesto Perez-Rueda, Rafael Hernandez-Guerrero, Mario Alberto Martinez-Nuñez, Dagoberto Armenta-Medina, Israel Sanchez, and J. Antonio Ibarra. Abundance, diversity and domain architecture variability in prokaryotic dna-binding transcription factors. PLoS ONE, 13:e0195332, Apr 2018. URL: https://doi.org/10.1371/journal.pone.0195332, doi:10.1371/journal.pone.0195332. This article has 100 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR33164-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR33164-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. lemmens2019transcriptionregulatorsin pages 1-2
2. nazaret2023marrfamilytranscriptional pages 1-2
3. nazaret2023marrfamilytranscriptional pages 4-6
4. nazaret2023marrfamilytranscriptional pages 6-7
5. song2024structuralbasisof pages 1-2
6. beggs2020marrfamilyproteins pages 1-2
7. nwokocha2024regulationofbacterial pages 1-2
8. gupta2019marrfamilytranscription pages 1-2
9. beggs2020marrfamilyproteins pages 2-4
10. song2024structuralbasisof pages 2-3
11. wojcicki2021transcriptionalregulationof pages 2-5
12. chubiz2023themarsox pages 1-2
13. floresbautista2020decipheringthefunctional pages 1-2
14. perezrueda2018abundancediversityand pages 1-2
15. https://doi.org/10.1002/pro.3769,
16. https://doi.org/10.3390/microorganisms11081936,
17. https://doi.org/10.1093/nar/gkae922,
18. https://doi.org/10.1016/j.jmb.2019.05.045,
19. https://doi.org/10.1128/jb.00302-24,
20. https://doi.org/10.1128/mmbr.00039-18,
21. https://doi.org/10.3390/pathogens10070801,
22. https://doi.org/10.1128/ecosalplus.esp-0010-2022,
23. https://doi.org/10.1371/journal.pone.0237135,
24. https://doi.org/10.1371/journal.pone.0195332,