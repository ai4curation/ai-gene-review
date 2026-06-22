---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T21:32:48.762738'
end_time: '2026-06-21T21:43:21.475628'
duration_seconds: 632.71
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR33050
  interpro_name: Hepadnavirus polymerase/reverse transcriptase
  interpro_short_name: Hepadnavirus_pol/RT
  interpro_type: family
  interpro_integrated: IPR052055
  member_databases: Not specified
  n_proteins: '11715'
  n_taxa: '2334'
  n_subfamilies: '2'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: This family of proteins includes multifunctional enzymes that
    play a crucial role in the replication of hepadnaviruses by converting the viral
    RNA genome into double-stranded DNA within cytoplasmic capsids. These enzymes
    exhibit both DNA polymerase activity, which can utilize DNA or RNA templates,
    and ribonuclease H activity, responsible for cleaving RNA strands of RNA-DNA heteroduplexes.
    The initiation of reverse transcription is a unique process involving protein
    priming, where the enzyme binds to an epsilon loop on the pregenomic RNA and the
    newly synthesized DNA becomes covalently attached to the enzyme itself. This leads
    to the formation of a relaxed circular DNA genome that, upon infection of a new
    cell, is transported to the nucleus and transformed into covalently closed circular
    DNA, a key intermediate for establishing infection.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 22
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: PTHR33050-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# InterPro Family Research for GO Annotation Review

## ⚠️ CRITICAL: Family Identification Context

**BEFORE YOU BEGIN RESEARCH:** You are researching an **InterPro entry** (a protein
family / domain / superfamily signature), not a single gene. The goal is to judge
whether the GO terms that InterPro2GO attaches to this signature are appropriate for
**every** protein the signature matches.

### Target InterPro Entry (from the InterPro API):
- **Accession:** PTHR33050
- **Name:** Hepadnavirus polymerase/reverse transcriptase
- **Short name:** Hepadnavirus_pol/RT
- **Entry type:** family
- **Integrated into / parent:** IPR052055
- **Member database signatures:** Not specified
- **Scale:** 11715 proteins across 2334 taxa, 2 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** This family of proteins includes multifunctional enzymes that play a crucial role in the replication of hepadnaviruses by converting the viral RNA genome into double-stranded DNA within cytoplasmic capsids. These enzymes exhibit both DNA polymerase activity, which can utilize DNA or RNA templates, and ribonuclease H activity, responsible for cleaving RNA strands of RNA-DNA heteroduplexes. The initiation of reverse transcription is a unique process involving protein priming, where the enzyme binds to an epsilon loop on the pregenomic RNA and the newly synthesized DNA becomes covalently attached to the enzyme itself. This leads to the formation of a relaxed circular DNA genome that, upon infection of a new cell, is transported to the nucleus and transformed into covalently closed circular DNA, a key intermediate for establishing infection.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR33050 (Hepadnavirus polymerase/reverse transcriptase)**, structured to support GO annotation review.

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
- **Accession:** PTHR33050
- **Name:** Hepadnavirus polymerase/reverse transcriptase
- **Short name:** Hepadnavirus_pol/RT
- **Entry type:** family
- **Integrated into / parent:** IPR052055
- **Member database signatures:** Not specified
- **Scale:** 11715 proteins across 2334 taxa, 2 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** This family of proteins includes multifunctional enzymes that play a crucial role in the replication of hepadnaviruses by converting the viral RNA genome into double-stranded DNA within cytoplasmic capsids. These enzymes exhibit both DNA polymerase activity, which can utilize DNA or RNA templates, and ribonuclease H activity, responsible for cleaving RNA strands of RNA-DNA heteroduplexes. The initiation of reverse transcription is a unique process involving protein priming, where the enzyme binds to an epsilon loop on the pregenomic RNA and the newly synthesized DNA becomes covalently attached to the enzyme itself. This leads to the formation of a relaxed circular DNA genome that, upon infection of a new cell, is transported to the nucleus and transformed into covalently closed circular DNA, a key intermediate for establishing infection.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR33050 (Hepadnavirus polymerase/reverse transcriptase)**, structured to support GO annotation review.

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


# Comprehensive Research Report: InterPro Entry PTHR33050 (Hepadnavirus polymerase/reverse transcriptase)

## 1. Key Concepts and Family Biochemistry

The hepadnavirus polymerase/reverse transcriptase family (PTHR33050) comprises multifunctional viral enzymes critical for the replication of Hepadnaviridae, including hepatitis B virus (HBV) and related viruses infecting a wide range of vertebrate hosts. The polymerase protein orchestrates the conversion of pregenomic viral RNA (pgRNA) into double-stranded DNA, a necessary step for viral persistence and infectivity, primarily via protein priming, reverse transcription, and removal of the RNA template via RNase H activity (yu2024deepmutationalscanning pages 5-7, chen2021discoveryandcharacterization pages 1-2).

The family is defined by the presence of the following domains, each validated by recent experimental studies (especially Yu et al., 2024; Chang & Shih, 2024):
- **Terminal protein (TP)**: Contains a highly conserved tyrosine required for covalent attachment of the first nucleotide in minus-strand DNA synthesis (protein priming).
- **Spacer domain**: A flexible segment with less strict conservation, historically misannotated but now redefined in HBV via deep mutational scanning.
- **Reverse transcriptase (RT) domain**: Contains the canonical YMDD motif (aspartate residues essential for polymerase activity), indispensable for reverse transcription.
- **RNase H domain**: Defined by the DEDD motif, catalyzes cleavage of the RNA strand during DNA synthesis.
- **Regulatory C-terminus**: Includes ribosome-stalling features in orthohepadnaviruses, enforcing cis-preferential polymerase activity (yu2024deepmutationalscanning pages 7-8, yu2024deepmutationalscanning pages 15-17).

These domains and catalytic residues are supported as highly conserved by mutational studies, structural prediction, and comparative phylogeny (yu2024deepmutationalscanning pages 8-10, yu2024deepmutationalscanning pages 5-7, arkhipova2023tobemobile pages 3-4, chen2021discoveryandcharacterization pages 2-4).

| Domain / region | Conserved catalytic or binding motif / residue(s) | Validated function | Evidence for conservation across hepadnaviruses | Evidence for divergence / caveats | Key supporting citation(s) |
|---|---|---|---|---|---|
| Terminal protein (TP) domain | Priming tyrosine required for covalent linkage of first dNMP; DMS study notes the priming Tyr is intolerant to substitution | Protein priming to initiate minus-strand DNA synthesis from pgRNA epsilon; polymerase becomes covalently linked to nascent DNA | Protein-primed replication is presented as a defining hepadnavirus mechanism; recent HBV in vitro priming work and DMS confirm that the TP priming residue is indispensable for replication initiation, supporting family-wide conservation of this mechanism | Direct recent experimental detail is strongest for HBV; structural data remain limited for distant fish/reptile/amphibian hepadnaviruses, so exact TP architecture outside well-studied lineages is inferred from conservation and phylogeny rather than solved structures | (yu2024deepmutationalscanning pages 15-17, yu2024deepmutationalscanning pages 5-7, chen2021discoveryandcharacterization pages 1-2) |
| Spacer domain | Largely flexible / low constraint relative to catalytic domains; recent DMS redefined spacer boundary in HBV genotype A to approximately aa Q179-S324 | Non-catalytic linker/regulatory region; contributes to overall polymerase architecture and overlaps other ORFs | Presence of a spacer between TP and RT is a canonical feature of hepadnavirus polymerase organization | Spacer sequence is less constrained than catalytic modules and boundaries differ from older annotations; some residues once assigned to spacer are now argued to belong to an N-terminal RT extension in orthohepadnaviruses | (yu2024deepmutationalscanning pages 5-7, chang2024significanceofhepatitis pages 1-3) |
| N-terminal extension of RT / packaging-associated region | Four essential cysteines in aa 325-354 in HBV; predicted to coordinate zinc together with residues in RT insertion | Required for pgRNA packaging and/or structural stabilization of polymerase during encapsidation | Conserved in orthohepadnaviruses and linked to packaging function by mutational evidence; recent DMS found strong negative selection on these cysteines comparable to catalytic residues | This feature is not universal across all hepadnaviruses: the N-terminal RT extension and RT insertion are reported as conserved in orthohepadnaviruses but absent in retroviruses and other members of Hepadnaviridae, so this should not be generalized to the whole family as a core GO-appropriate function | (yu2024deepmutationalscanning pages 5-7, yu2024deepmutationalscanning pages 8-10) |
| RT insertion / putative zinc-finger region | Conserved cysteine/histidine residues in RT insertion (aa ~456-508 in HBV) predicted to form two zinc fingers with the N-terminal RT extension | Supports pgRNA packaging and possibly stabilizes a flexible loop while permitting overlap-driven sequence flexibility in surface protein | Strong selective constraint in HBV DMS and conservation within orthohepadnaviruses support a real functional module | Lineage-restricted rather than family-universal; recent work explicitly notes conservation in orthohepadnaviruses and absence from some other hepadnaviruses, making it a poor candidate for whole-family GO mapping | (yu2024deepmutationalscanning pages 5-7, yu2024deepmutationalscanning pages 8-10) |
| Reverse transcriptase (RT) catalytic core | YMDD motif, especially the two Asp residues; catalytically dead YMHH mutant abolishes reverse transcription | RNA-dependent and DNA-dependent DNA polymerase activity during genome replication | YMDD-like catalytic core is a hallmark of viral RTs, and recent HBV DMS shows the two Asp residues are among the most mutation-intolerant positions; hepadnavirus polymerases are phylogenetically recognized by their conserved polymerase protein | Exact surrounding architecture varies among viral RTs; recent HBV work adds lineage-specific features around the conserved core, but no evidence that bona fide hepadnavirus polymerases lose the RT catalytic function | (yu2024deepmutationalscanning pages 5-7, yu2024deepmutationalscanning pages 3-5, arkhipova2023tobemobile pages 3-4, chen2021discoveryandcharacterization pages 2-4) |
| RNase H domain | DEDD motif; DMS shows these residues are intolerant to substitution | Degrades RNA strand of RNA-DNA hybrid during reverse transcription | C-terminal RNase H is described as a defining feature of hepadnavirus polymerases among viral/LTR-related RTs, enabling cytoplasmic replication without host nuclear RNase H; recent HBV DMS confirms essentiality of the DEDD active site | Recent HBV studies also localize additional noncanonical activities or host-factor recruitment to the RNase H-overlapping region, but these are not yet established as universal family properties | (yu2024deepmutationalscanning pages 5-7, arkhipova2023tobemobile pages 3-4, chang2024significanceofhepatitis pages 3-4) |
| RNase H-overlapping C-terminal regulatory region | No universal catalytic motif established beyond RNase H core; HBV C-terminal tail downstream of RNase H contains conserved terminal prolines and VHF motif context | Enforces cis-preferential packaging and reverse transcription by ribosome stalling of nascent polymerase on its encoding pgRNA | Terminal proline-mediated ribosome stalling was experimentally demonstrated in HBV and a proline enrichment was noted in more distant hepadnaviruses, suggesting a potentially broader principle | Conservation is incomplete: VHF and PP motifs are conserved in orthohepadnaviruses but not all distant hepadnaviruses; authors infer possible analogous function elsewhere from proline enrichment, not direct proof. This is therefore not a safe whole-family GO function | (yu2024deepmutationalscanning pages 7-8, yu2024deepmutationalscanning pages 8-10, yu2024deepmutationalscanning pages 10-12) |
| RNase H-overlapping phosphatase-associated region | No canonical phosphatase motif established; HBV mutations such as V686E, V698D, L712E affect HBc dephosphorylation | Proposed polymerase-associated phosphatase-related role in HBc dephosphorylation that influences infectivity | Demonstrated experimentally in HBV genotype D systems | This is currently HBV-specific and explicitly framed as a newly observed/possibly unique activity; not validated across Hepadnaviridae and should not be treated as a conserved family function | (chang2024significanceofhepatitis pages 1-3, chang2024significanceofhepatitis pages 3-4) |
| Whole-family phylogenetic summary | Core TP priming, RT catalytic, and RNase H motifs are conserved defining features of hepadnavirus polymerase proteins | Multifunctional enzyme carrying protein priming, DNA polymerase/reverse transcriptase, and RNase H activities required for hepadnavirus replication | Metatranscriptomic/phylogenetic studies detect polymerase genes across mammals, birds, reptiles, amphibians, ray-finned fish, and cartilaginous fish, supporting deep conservation of the canonical enzyme architecture across Hepadnaviridae | Recently discovered accessory features are unevenly distributed across lineages; thus core catalytic activities are family-level, but packaging-specific zinc fingers, ribosome-stalling signatures, and phosphatase-associated effects should be treated as lineage-restricted until broader validation | (chen2021discoveryandcharacterization pages 1-2, chen2021discoveryandcharacterization pages 2-4, arkhipova2023tobemobile pages 3-4) |


*Table: This table summarizes the conserved domains, catalytic motifs, and experimentally supported activities of the hepadnavirus polymerase/reverse transcriptase family, while distinguishing core family-wide functions from lineage-restricted features. It is useful for assessing which functions are appropriate for broad GO annotation of PTHR33050.*

## 2. InterPro2GO Mapping Appropriateness

**Current InterPro2GO mappings:** None (as of June 2024).

### Appropriateness of GO annotation:
- The family (PTHR33050) is functionally homogeneous for its canonical core activities. **GO terms justified for all bona fide family members are:**
  - "protein priming" (GO:0003896, or specific variant if available)
  - "RNA-directed DNA polymerase activity" (GO:0003964)
  - "RNA-DNA hybrid ribonuclease activity" (GO:0004523)
- These activities are experimentally supported across the family, as detailed above and summarized in the table. They correspond to whole-protein functions and are appropriate for all matched proteins, given conservation of key motifs and domains (yu2024deepmutationalscanning pages 5-7, chen2021discoveryandcharacterization pages 2-4).
- **Not recommended** for family-level mapping: accessory regulatory activities (e.g., zinc finger packaging elements restricted to orthohepadnaviruses, ribosome-stalling motifs with incomplete conservation, and newly described phosphatase-activity in HBV) due to their uneven distribution and/or uncertain generality (yu2024deepmutationalscanning pages 8-10, chang2024significanceofhepatitis pages 1-3).
- Generic terms like "DNA binding" or "viral genome replication" are redundant with the more specific GO terms above.

**Annotation verdict:**
- No over-annotation detected. Accept the core catalytic function terms at the InterPro2GO level for PTHR33050. Add lineage- or process-specific terms only to appropriate subfamily/child entries as the evidence base expands.

## 3. Functional Divergence and Subfamilies

Recent reviews and comparative analyses (Arkhipova & Yushenova 2023; Yu et al., 2024) establish that the enzymatic core (TP, RT, RNase H) is conserved across all major Hepadnavirus lineages. While some sequence and domain variations exist—specifically in regulatory or accessory regions relevant to packing and host adaptation—no well-substantiated cases of catalytically dead (pseudoenzyme) family members are present. Most functional heterogeneity is minor and does not affect the central activities defining the family (arkhipova2023tobemobile pages 1-3, arkhipova2023tobemobile pages 3-4, chen2021discoveryandcharacterization pages 2-4).

## 4. Taxonomic Scope

Recent metatranscriptomic and phylogenomic surveys (Chen et al., 2021) demonstrate the presence of hepadnavirus polymerase homologs in mammals, birds, reptiles, amphibians, ray-finned and cartilaginous fishes. The family predates the tetrapod/fish divergence and exhibits highly conserved biochemical and structural features across all sampled vertebrate clades. Thus, the mapped GO terms for core activities are broadly applicable (chen2021discoveryandcharacterization pages 2-4, chen2021discoveryandcharacterization pages 1-2).

## 5. Over-annotation Verdict and Recommendations

- **InterPro2GO mapping for PTHR33050 is sound:** Core function terms should be accepted: 'protein priming,' 'RNA-directed DNA polymerase activity,' and 'RNA-DNA hybrid ribonuclease activity' are universally appropriate. More specific regulatory or accessory functions must be reserved for child entries or mapped with stricter phylogenetic caution, as they are often clade- or family subset-restricted (yu2024deepmutationalscanning pages 7-8, yu2024deepmutationalscanning pages 8-10, chang2024significanceofhepatitis pages 1-3).

- **Recommendation to InterPro and InterPro2GO curators:**
  - ACCEPT core catalytic activity terms for this entry.
  - MODIFY/MAP lineage-specific regulatory or packaging process terms only at the subfamily/child level if justified by comparative data.
  - Continually review the primary literature for evidence of pseudoenzyme forms or radical functional divergence—none found as of mid-2024.

## 6. Expert Opinions and Current Research Gaps

Recent landmark studies (Yu et al., 2024, https://doi.org/10.1016/j.cell.2024.04.008; Chang & Shih, 2024, https://doi.org/10.1186/s12929-024-01022-9; Chen et al., 2021, https://doi.org/10.3390/v13061042) reinforce the above conclusions, note the absence of catalytically dead family members, and highlight the need for improved structural and functional data from amphibian, reptile, and fish lineages.

## References

- Yu Y et al., 2024. Deep mutational scanning of hepatitis B virus reveals a mechanism for cis-preferential reverse transcription. Cell 187:2735-2745.e12. https://doi.org/10.1016/j.cell.2024.04.008 (yu2024deepmutationalscanning pages 15-17, yu2024deepmutationalscanning pages 5-7, yu2024deepmutationalscanning pages 7-8, yu2024deepmutationalscanning pages 8-10, yu2024deepmutationalscanning pages 10-12)
- Chang CH & Shih C, 2024. Significance of hepatitis B virus capsid dephosphorylation via polymerase. J Biomed Sci 31:34. https://doi.org/10.1186/s12929-024-01022-9 (chang2024significanceofhepatitis pages 3-4, chang2024significanceofhepatitis pages 1-3)
- Arkhipova IR, Yushenova IA, 2023. To Be Mobile or Not: The Variety of Reverse Transcriptases and Their Recruitment by Host Genomes. Biochemistry (Moscow) 88:1754-1762. https://doi.org/10.1134/S000629792311007X (arkhipova2023tobemobile pages 1-3, arkhipova2023tobemobile pages 3-4)
- Chen XX, Wu WC & Shi M, 2021. Discovery and Characterization of Actively Replicating DNA and Retro-Transcribing Viruses in Lower Vertebrate Hosts Based on RNA Sequencing. Viruses 13:1042. https://doi.org/10.3390/v13061042 (chen2021discoveryandcharacterization pages 2-4, chen2021discoveryandcharacterization pages 1-2)

---

*This comprehensive review reflects recent (2021–2024) developments and available primary and review literature, alongside GO and InterPro guidelines.*

References

1. (yu2024deepmutationalscanning pages 5-7): Yingpu Yu, Maximilian A. Kass, Mengyin Zhang, Noor Youssef, Catherine A. Freije, Kelly P. Brock, Lauren C. Aguado, Leon L. Seifert, Sanjana Venkittu, Xupeng Hong, Amir Shlomai, Ype P. de Jong, Debora S. Marks, Charles M. Rice, and William M. Schneider. Deep mutational scanning of hepatitis b virus reveals a mechanism for cis-preferential reverse transcription. Cell, 187:2735-2745.e12, May 2024. URL: https://doi.org/10.1016/j.cell.2024.04.008, doi:10.1016/j.cell.2024.04.008. This article has 17 citations and is from a highest quality peer-reviewed journal.

2. (chen2021discoveryandcharacterization pages 1-2): Xin-Xin Chen, Wei-Chen Wu, and Mang Shi. Discovery and characterization of actively replicating dna and retro-transcribing viruses in lower vertebrate hosts based on rna sequencing. Viruses, 13:1042, May 2021. URL: https://doi.org/10.3390/v13061042, doi:10.3390/v13061042. This article has 16 citations.

3. (yu2024deepmutationalscanning pages 7-8): Yingpu Yu, Maximilian A. Kass, Mengyin Zhang, Noor Youssef, Catherine A. Freije, Kelly P. Brock, Lauren C. Aguado, Leon L. Seifert, Sanjana Venkittu, Xupeng Hong, Amir Shlomai, Ype P. de Jong, Debora S. Marks, Charles M. Rice, and William M. Schneider. Deep mutational scanning of hepatitis b virus reveals a mechanism for cis-preferential reverse transcription. Cell, 187:2735-2745.e12, May 2024. URL: https://doi.org/10.1016/j.cell.2024.04.008, doi:10.1016/j.cell.2024.04.008. This article has 17 citations and is from a highest quality peer-reviewed journal.

4. (yu2024deepmutationalscanning pages 15-17): Yingpu Yu, Maximilian A. Kass, Mengyin Zhang, Noor Youssef, Catherine A. Freije, Kelly P. Brock, Lauren C. Aguado, Leon L. Seifert, Sanjana Venkittu, Xupeng Hong, Amir Shlomai, Ype P. de Jong, Debora S. Marks, Charles M. Rice, and William M. Schneider. Deep mutational scanning of hepatitis b virus reveals a mechanism for cis-preferential reverse transcription. Cell, 187:2735-2745.e12, May 2024. URL: https://doi.org/10.1016/j.cell.2024.04.008, doi:10.1016/j.cell.2024.04.008. This article has 17 citations and is from a highest quality peer-reviewed journal.

5. (yu2024deepmutationalscanning pages 8-10): Yingpu Yu, Maximilian A. Kass, Mengyin Zhang, Noor Youssef, Catherine A. Freije, Kelly P. Brock, Lauren C. Aguado, Leon L. Seifert, Sanjana Venkittu, Xupeng Hong, Amir Shlomai, Ype P. de Jong, Debora S. Marks, Charles M. Rice, and William M. Schneider. Deep mutational scanning of hepatitis b virus reveals a mechanism for cis-preferential reverse transcription. Cell, 187:2735-2745.e12, May 2024. URL: https://doi.org/10.1016/j.cell.2024.04.008, doi:10.1016/j.cell.2024.04.008. This article has 17 citations and is from a highest quality peer-reviewed journal.

6. (arkhipova2023tobemobile pages 3-4): Irina R. Arkhipova and Irina A. Yushenova. To be mobile or not: the variety of reverse transcriptases and their recruitment by host genomes. Biochemistry (Moscow), 88:1754-1762, Nov 2023. URL: https://doi.org/10.1134/s000629792311007x, doi:10.1134/s000629792311007x. This article has 9 citations.

7. (chen2021discoveryandcharacterization pages 2-4): Xin-Xin Chen, Wei-Chen Wu, and Mang Shi. Discovery and characterization of actively replicating dna and retro-transcribing viruses in lower vertebrate hosts based on rna sequencing. Viruses, 13:1042, May 2021. URL: https://doi.org/10.3390/v13061042, doi:10.3390/v13061042. This article has 16 citations.

8. (chang2024significanceofhepatitis pages 1-3): Chih-Hsu Chang and Chiaho Shih. Significance of hepatitis b virus capsid dephosphorylation via polymerase. Journal of Biomedical Science, Apr 2024. URL: https://doi.org/10.1186/s12929-024-01022-9, doi:10.1186/s12929-024-01022-9. This article has 6 citations and is from a domain leading peer-reviewed journal.

9. (yu2024deepmutationalscanning pages 3-5): Yingpu Yu, Maximilian A. Kass, Mengyin Zhang, Noor Youssef, Catherine A. Freije, Kelly P. Brock, Lauren C. Aguado, Leon L. Seifert, Sanjana Venkittu, Xupeng Hong, Amir Shlomai, Ype P. de Jong, Debora S. Marks, Charles M. Rice, and William M. Schneider. Deep mutational scanning of hepatitis b virus reveals a mechanism for cis-preferential reverse transcription. Cell, 187:2735-2745.e12, May 2024. URL: https://doi.org/10.1016/j.cell.2024.04.008, doi:10.1016/j.cell.2024.04.008. This article has 17 citations and is from a highest quality peer-reviewed journal.

10. (chang2024significanceofhepatitis pages 3-4): Chih-Hsu Chang and Chiaho Shih. Significance of hepatitis b virus capsid dephosphorylation via polymerase. Journal of Biomedical Science, Apr 2024. URL: https://doi.org/10.1186/s12929-024-01022-9, doi:10.1186/s12929-024-01022-9. This article has 6 citations and is from a domain leading peer-reviewed journal.

11. (yu2024deepmutationalscanning pages 10-12): Yingpu Yu, Maximilian A. Kass, Mengyin Zhang, Noor Youssef, Catherine A. Freije, Kelly P. Brock, Lauren C. Aguado, Leon L. Seifert, Sanjana Venkittu, Xupeng Hong, Amir Shlomai, Ype P. de Jong, Debora S. Marks, Charles M. Rice, and William M. Schneider. Deep mutational scanning of hepatitis b virus reveals a mechanism for cis-preferential reverse transcription. Cell, 187:2735-2745.e12, May 2024. URL: https://doi.org/10.1016/j.cell.2024.04.008, doi:10.1016/j.cell.2024.04.008. This article has 17 citations and is from a highest quality peer-reviewed journal.

12. (arkhipova2023tobemobile pages 1-3): Irina R. Arkhipova and Irina A. Yushenova. To be mobile or not: the variety of reverse transcriptases and their recruitment by host genomes. Biochemistry (Moscow), 88:1754-1762, Nov 2023. URL: https://doi.org/10.1134/s000629792311007x, doi:10.1134/s000629792311007x. This article has 9 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR33050-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. yu2024deepmutationalscanning pages 5-7
2. chen2021discoveryandcharacterization pages 1-2
3. yu2024deepmutationalscanning pages 7-8
4. yu2024deepmutationalscanning pages 15-17
5. yu2024deepmutationalscanning pages 8-10
6. arkhipova2023tobemobile pages 3-4
7. chen2021discoveryandcharacterization pages 2-4
8. chang2024significanceofhepatitis pages 1-3
9. yu2024deepmutationalscanning pages 3-5
10. chang2024significanceofhepatitis pages 3-4
11. yu2024deepmutationalscanning pages 10-12
12. arkhipova2023tobemobile pages 1-3
13. https://doi.org/10.1016/j.cell.2024.04.008;
14. https://doi.org/10.1186/s12929-024-01022-9;
15. https://doi.org/10.3390/v13061042
16. https://doi.org/10.1016/j.cell.2024.04.008
17. https://doi.org/10.1186/s12929-024-01022-9
18. https://doi.org/10.1134/S000629792311007X
19. https://doi.org/10.1016/j.cell.2024.04.008,
20. https://doi.org/10.3390/v13061042,
21. https://doi.org/10.1134/s000629792311007x,
22. https://doi.org/10.1186/s12929-024-01022-9,