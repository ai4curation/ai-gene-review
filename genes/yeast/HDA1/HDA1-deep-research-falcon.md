---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-13T03:37:59.933905'
end_time: '2026-05-13T03:53:15.800895'
duration_seconds: 915.87
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

GO annotation research for Saccharomyces cerevisiae HDA1 (UniProt P53973). Focus on GO evidence for core functions: class II zinc-dependent histone deacetylase activity with hydrolytic mechanism, HDA1/HDA2/HDA3 histone deacetylase complex membership, nuclear/chromatin localization, chromatin binding if directly supported, deacetylation of histones H2B/H3/H4 if supported, epigenetic regulation of gene expression, chromatin organization, negative regulation of RNA polymerase II transcription/repression. Evaluate non-core or questionable annotations: cytoplasm, positive regulation of macromolecule biosynthetic process, generic hydrolase, protein binding/identical protein binding, chromosome segregation/centromere roles, positive regulation of transcription, response to heat/HSF1 if any. Include PMID/DOI citations and keep under 1200 words.

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

GO annotation research for Saccharomyces cerevisiae HDA1 (UniProt P53973). Focus on GO evidence for core functions: class II zinc-dependent histone deacetylase activity with hydrolytic mechanism, HDA1/HDA2/HDA3 histone deacetylase complex membership, nuclear/chromatin localization, chromatin binding if directly supported, deacetylation of histones H2B/H3/H4 if supported, epigenetic regulation of gene expression, chromatin organization, negative regulation of RNA polymerase II transcription/repression. Evaluate non-core or questionable annotations: cytoplasm, positive regulation of macromolecule biosynthetic process, generic hydrolase, protein binding/identical protein binding, chromosome segregation/centromere roles, positive regulation of transcription, response to heat/HSF1 if any. Include PMID/DOI citations and keep under 1200 words.

## GO-annotation evidence report: *Saccharomyces cerevisiae* HDA1 (UniProt P53973)

### Executive summary (current understanding)
Hda1 is a class II, Zn2+-dependent lysine deacetylase (histone deacetylase) that functions primarily as the catalytic core of the Hda1C complex with Hda2 and Hda3, acting on chromatin in the nucleus to tune histone acetylation and thereby repress or dampen RNA polymerase II (Pol II)–dependent transcription at specific promoters and across broader chromosomal domains. Strong experimental evidence supports chromatin association, histone-tail deacetylation (H2B/H3 and context-dependent H4), and transcriptional repression. Several broad or non-core GO annotations (e.g., cytoplasmic localization; generic hydrolase; positive regulation of transcription/biosynthesis) are weakly supported or likely reflect indirect effects.

### 1) Key concepts and definitions (GO-relevant)
**Class II zinc-dependent histone deacetylase activity (MF).** Hda1 belongs to the Zn2+-dependent Rpd3/Hda1 deacetylase family; mechanistically, these enzymes catalyze hydrolysis of the ε-N-acetyl-lysine amide bond, typically via a Zn2+-activated water and conserved acid/base relay (general HDAC mechanism described for Hda1 family members). Structural/biochemical work on yeast Hda1 and its C-terminal Arb2 domain supports this family placement and a hydrolytic deacetylation mechanism. (shen2016structuralandhistone pages 1-2)

**Hda1C complex (CC).** Hda1 functions in a multi-subunit histone deacetylase complex with Hda2 and Hda3, where Hda2/Hda3 are required for full Hda1 activity and targeting. (wu2001hda2andhda3 pages 1-2)

**Chromatin targeting and transcriptional repression (BP).** Hda1C is recruited to promoters (often via corepressors such as Tup1) to deacetylate promoter-proximal nucleosomes and repress transcription, and it can also operate over extended domains (e.g., subtelomeric regions) that exhibit low transcriptional output. (wu2001tup1utilizeshistone pages 1-2, robyr2002microarraydeacetylationmaps pages 1-2, robyr2002microarraydeacetylationmaps pages 5-7)

### 2) Recent developments and latest research (prioritizing 2023–2024)
A limitation of this tool run is that it retrieved **one 2023 Hda1C-relevant primary source** but **no 2024 *S. cerevisiae* Hda1 primary paper** directly addressing Hda1 core molecular functions.

**2023 functional evidence (starvation/stress-linked repression).** A 2023 study examining acetylation regulators in chronological ageing/stationary-phase contexts reports that deleting **HDA1/HDA2/HDA3** enhances expression of heat-shock protein (HSP) reporters under starvation and interprets this as the Hda1 HDAC complex negatively influencing starvation-induced HSP expression; it also links Hda1 (with Gcn5) to changes in global H3K9 acetylation in stationary-phase transition. This supports a **repressive role for Hda1C** in stress-associated transcriptional programs and is consistent with GO BP terms related to negative regulation of transcription and chromatin-based regulation. Publication date: Sep 2023; URL: https://doi.org/10.17863/cam.101661. (zhang2023thesaccharomycescerevisiae pages 1-5)

**Most informative recent mechanistic primary evidence (2019).** The most detailed modern chromatin-targeting/substrate evidence in the retrieved set is a 2019 Nature Communications study showing **Hda1C binds hyperactive genes** and mediates **H4-specific deacetylation within coding regions**, likely through an Arb2–Pol II interaction. Publication date: Sep 2019; URL: https://doi.org/10.1038/s41467-019-12077-w. (ha2019transcriptiondependenttargetingof pages 4-5, ha2019transcriptiondependenttargetingof media f27f6bb5)

### 3) Current applications and real-world implementations
Although Hda1 GO annotations are primarily basic-science oriented, there are real-world implementations in:

**Genome-wide functional annotation and chromatin regulatory network models.** Hda1 is frequently used as a node in yeast epigenetic regulatory maps, including promoter/domain deacetylation landscapes and subtelomeric chromatin-domain analyses that connect histone acetylation states to environmental-response gene sets. These studies underpin systems biology models of chromatin regulation and transcriptional repression. (robyr2002microarraydeacetylationmaps pages 1-2, robyr2002microarraydeacetylationmaps pages 5-7)

**Biotechnology strain engineering (conceptual relevance).** Because Hda1 influences transcriptional states of stress/alternative-carbon utilization genes (e.g., in subtelomeric HAST domains), HDA1 perturbation is a potential strategy in yeast strain engineering where tuning chromatin repression can alter expression programs (e.g., stress-response or metabolic flexibility). This inference is grounded in the observed enrichment of stress/alternative carbon genes in Hda1-regulated domains. (robyr2002microarraydeacetylationmaps pages 5-7, robyr2002microarraydeacetylationmaps pages 3-5)

### 4) Evidence for core GO functions (with analysis)

#### A. MF: class II zinc-dependent histone deacetylase activity (hydrolytic mechanism)
- **Family/mechanism support.** Structural characterization of Hda1’s Arb2 domain places Hda1 as a class II HDAC within the Zn2+-dependent Rpd3/Hda1 family and describes the Zn2+-linked hydrolytic mechanism at the family level. (shen2016structuralandhistone pages 1-2)
- **Functional biochemistry.** Biochemical reconstitution/characterization describes the yeast class II Hda1 complex as **trichostatin A (TSA) sensitive**, consistent with canonical Zn2+-dependent HDAC pharmacology. (lee2009structuralandfunctional pages 1-3)

*GO interpretation:* Strong support for “histone deacetylase activity (Zn2+-dependent)” and hydrolytic deacetylation, with the caveat that the snippets emphasize family mechanism rather than metal-dependence assays on Hda1 specifically. (shen2016structuralandhistone pages 1-2, lee2009structuralandfunctional pages 1-3)

#### B. CC: Hda1/Hda2/Hda3 histone deacetylase complex membership
- **Physical association and requirement for activity.** Hda2 and Hda3 physically interact with Hda1 and are essential for Hda1 deacetylase activity; disruption of any subunit disrupts activity in vitro and in vivo. (wu2001hda2andhda3 pages 1-2)
- **Architecture.** Structural/functional studies describe Hda1C organization (Hda1 dimer plus Hda2/Hda3 modules) and non-sequence-specific DNA binding by Hda2/Hda3 N-termini, consistent with chromatin targeting functions. (lee2009structuralandfunctional pages 1-3)

*GO interpretation:* Strong support for “Hda1C complex” cellular component annotation. (wu2001hda2andhda3 pages 1-2, lee2009structuralandfunctional pages 1-3)

#### C. CC: nuclear/chromatin localization; chromatin binding
- **Direct chromatin occupancy.** ChIP-qPCR/ChIP-seq shows Hda1 occupancy at promoters and coding regions of highly transcribed genes, consistent with nuclear localization and chromatin association. (ha2019transcriptiondependenttargetingof pages 4-5, ha2019transcriptiondependenttargetingof media f27f6bb5)
- **Direct binding capacity (domains).** The Hda1 Arb2 domain binds histone dimers/tetramers in vitro; Hda2/Hda3 N-termini bind DNA in vitro. Together, these provide direct mechanistic support for chromatin binding/association of the complex. (shen2016structuralandhistone pages 1-2, lee2009structuralandfunctional pages 1-3)

*GO interpretation:* Supported for “chromatin” association and potentially “chromatin binding,” with best evidence being a combination of ChIP-based occupancy and in vitro binding by Arb2/DNA-binding modules. (ha2019transcriptiondependenttargetingof pages 4-5, shen2016structuralandhistone pages 1-2)

#### D. MF: deacetylation of histones H2B/H3/H4
- **H2B and H3 at repressed promoters (Tup1-dependent).** Tup1 recruits Hda1 to deacetylate histones **H3 and H2B** at promoter-adjacent nucleosomes (e.g., ENA1), supporting histone-substrate specificity and a repression mechanism. (wu2001tup1utilizeshistone pages 1-2, robyr2002microarraydeacetylationmaps pages 1-2)
- **Genome-wide histone-site effects.** Genome-scale deacetylation maps identify Hda1-affected acetylation sites including **H3K9, H3K18 and H2BK16**, frequently in promoter/intergenic regions and in subtelomeric domains. (robyr2002microarraydeacetylationmaps pages 3-5, robyr2002microarraydeacetylationmaps pages 5-7)
- **H4 in coding regions of hyperactive genes (context-dependent).** Modern spike-in normalized ChIP-seq/ChIP-qPCR demonstrates Hda1C-dependent **H4 deacetylation within coding regions** of highly transcribed genes. (ha2019transcriptiondependenttargetingof pages 4-5, ha2019transcriptiondependenttargetingof media 7a4ee2a4)

*GO interpretation:* Strong support for H2B/H3 deacetylation, and strong evidence for H4 deacetylation in a transcription-coupled, gene-body context. (wu2001tup1utilizeshistone pages 1-2, ha2019transcriptiondependenttargetingof pages 4-5)

#### E. BP: epigenetic regulation of gene expression; chromatin organization
- **Domain-scale chromatin regulation.** Hda1 regulates extended subtelomeric “HAST” domains (multiple chromosome ends; kb-scale regions) enriched for lowly expressed genes involved in stress and alternative carbon utilization, supporting chromatin-organization and epigenetic-regulation annotations. (robyr2002microarraydeacetylationmaps pages 5-7)
- **Local and global deacetylation landscapes.** At PHO5 and adjacent ORFs, deletion of HDA1 increases acetylation across a multi-kb region, consistent with domain-wide chromatin regulation influencing basal transcriptional states. (vogelauer2000globalhistoneacetylation pages 1-2)

#### F. BP: negative regulation of RNA polymerase II transcription / repression
- **Direct repression mechanism via Tup1.** Tup1 utilizes Hda1 to deacetylate promoter-proximal nucleosomes, producing localized chromatin states consistent with transcriptional repression. (wu2001tup1utilizeshistone pages 1-2)
- **Genome-wide repression-biased signature.** Hda1-affected regions overlap with Tup1-regulated promoters and correlate with repressed subtelomeric gene sets. (robyr2002microarraydeacetylationmaps pages 5-7, robyr2002microarraydeacetylationmaps pages 1-2)

### 5) Evaluation of non-core or questionable annotations

**Cytoplasm (CC): likely weak/incorrect for Hda1 itself.** In the retrieved evidence, cytosolic relocalization is described for **Hda2/Hda3 under hypoxia**, not for Hda1; core functional data place Hda1C on chromatin. (peterson2019functionalcharacterizationof pages 75-79, ha2019transcriptiondependenttargetingof pages 4-5)

**Positive regulation of macromolecule biosynthetic process / positive regulation of transcription (BP): generally not supported as core.** The dominant evidence supports repression/dampening via deacetylation. Genome-wide data do note rare loci with paradoxical expression changes in hda1 mutants, but these are more consistent with indirect effects or pathway interactions than direct activation. (robyr2002microarraydeacetylationmaps pages 3-5, wu2001tup1utilizeshistone pages 1-2)

**Generic hydrolase activity (MF): overly broad.** Evidence supports a specific lysine deacetylase/HDAC activity rather than a generic hydrolase term. (shen2016structuralandhistone pages 1-2)

**Protein binding / identical protein binding (MF): partially supported but nonspecific.** Hda1 self-interaction (dimerization) and interactions with Hda2/Hda3 and Tup1 support these broad terms, but they add little beyond specific complex membership annotations. (wu2001hda2andhda3 pages 1-2, peterson2019functionalcharacterizationof pages 71-75)

**Chromosome segregation / centromere roles (BP/CC): context-dependent and possibly driven by Hda3.** Genetic suppressor analysis and ChIP-PCR show association of tagged Hda1/Hda2/Hda3 with centromeric DNA, but the strongest chromosome-segregation phenotype (e.g., markedly elevated chromosome loss) is attributed to **Hda3** and complex integrity. Thus, annotating Hda1 to “chromosome segregation” may be defensible only with careful qualifiers (complex-level effect; context-specific), rather than as a core function. (kanta2006suppressoranalysisof pages 11-12, kanta2006suppressoranalysisof pages 8-11)

**Response to heat / HSF1 (BP): limited direct evidence.** A 2023 study links Hda1C to repression of starvation-induced HSP reporter expression, which could motivate a “stress response” annotation, but the retrieved evidence does not directly support an HSF1-specific mechanism for Hda1. (zhang2023thesaccharomycescerevisiae pages 1-5, peterson2019functionalcharacterizationof pages 71-75)

### 6) Key data/statistics from the cited studies
- **Subtelomeric HAST domains:** Robyr et al. report Hda1-dependent subtelomeric domains across **22 chromosome ends**, spanning roughly **4–34 kb**, and containing **149 genes** with very low steady-state expression in rich media. (robyr2002microarraydeacetylationmaps pages 5-7)
- **Promoter targeting scope:** Robyr et al. report most promoters are predominantly affected by one deacetylase (Hda1 vs Rpd3), with partial overlap and Hda1 acting largely at intergenic/promoter regions. (robyr2002microarraydeacetylationmaps pages 3-5)
- **Chromosome-loss phenotype (Hda3):** Kanta et al. report ~**100-fold** higher chromosome loss rate in an **hda3Δ/hda3Δ** mutant, emphasizing that segregation defects are most clearly supported for Hda3 among Hda subunits in that study. (kanta2006suppressoranalysisof pages 11-12)

### Visual evidence
ChIP-seq and ChIP-qPCR panels directly illustrating Hda1C occupancy at hyperactive genes and increased H4 acetylation in **hda1Δ** cells are shown in Ha et al. 2019 (Figures 2–3). (ha2019transcriptiondependenttargetingof media f27f6bb5, ha2019transcriptiondependenttargetingof media 7a4ee2a4)

### Summary table
| GO aspect | Specific claim/term | Key experimental evidence | Best supporting paper | DOI URL | Citation id(s) |
|---|---|---|---|---|---|
| MF | Class II Zn2+-dependent histone deacetylase activity (hydrolytic mechanism) | Structural/mechanistic analysis places Hda1 in the Zn2+-dependent Rpd3/Hda1 family; TSA-sensitive HDAC complex reconstituted | Lee, 2009, J Mol Biol | https://doi.org/10.1016/j.jmb.2009.06.059 | (lee2009structuralandfunctional pages 1-3, shen2016structuralandhistone pages 1-2) |
| CC | Member of Hda1/Hda2/Hda3 histone deacetylase complex | CoIP/GST pull-downs and genetic disruption show Hda2/Hda3 interact with and are essential for Hda1 activity | Wu, 2001, PNAS | https://doi.org/10.1073/pnas.081560698 | (wu2001hda2andhda3 pages 1-2) |
| CC | Nuclear/chromatin localization | ChIP-qPCR/ChIP-seq show Hda1 occupancy at coding regions of active genes and promoters | Ha, 2019, Nat Commun | https://doi.org/10.1038/s41467-019-12077-w | (ha2019transcriptiondependenttargetingof pages 4-5, ha2019transcriptiondependenttargetingof media f27f6bb5) |
| CC | Chromatin binding directly supported | Arb2 domain binds histones/nucleosomes in vitro; Hda2/Hda3 N-termini bind DNA | Shen, 2016, Sci Rep | https://doi.org/10.1038/srep33905 | (shen2016structuralandhistone pages 1-2, lee2009structuralandfunctional pages 1-3) |
| MF | Deacetylates histone H2B | Promoter-proximal H2B hyperacetylation in hda1 mutants; localized deacetylation at ENA1 | Wu, 2001, Mol Cell | https://doi.org/10.1016/S1097-2765(01)00160-5 | (wu2001tup1utilizeshistone pages 1-2) |
| MF | Deacetylates histone H3 | H3/H2B-specific promoter deacetylation and genome-wide H3 site effects (H3K9/H3K18) | Wu, 2001, Mol Cell | https://doi.org/10.1016/S1097-2765(01)00160-5 | (wu2001tup1utilizeshistone pages 1-2, robyr2002microarraydeacetylationmaps pages 3-5) |
| MF | Deacetylates histone H4 | Spike-in ChIP-seq shows increased H4 acetylation in hda1Δ at hyperactive genes | Ha, 2019, Nat Commun | https://doi.org/10.1038/s41467-019-12077-w | (ha2019transcriptiondependenttargetingof pages 4-5, ha2019transcriptiondependenttargetingof pages 1-2) |
| BP | Epigenetic regulation of gene expression | Histone deacetylation at promoters/coding regions delays induction and fine-tunes expression | Ha, 2019, Nat Commun | https://doi.org/10.1038/s41467-019-12077-w | (ha2019transcriptiondependenttargetingof pages 1-2) |
| BP | Chromatin organization / subtelomeric domain regulation | Genome-wide deacetylation maps define HAST subtelomeric domains with low-expression genes | Robyr, 2002, Cell | https://doi.org/10.1016/S0092-8674(02)00746-8 | (robyr2002microarraydeacetylationmaps pages 5-7, robyr2002microarraydeacetylationmaps pages 1-2) |
| BP | Negative regulation of RNA polymerase II transcription / repression | Tup1 recruits Hda1 for localized histone deacetylation and repression at ENA1 and other genes | Wu, 2001, Mol Cell | https://doi.org/10.1016/S1097-2765(01)00160-5 | (wu2001tup1utilizeshistone pages 1-2) |
| questionable | Cytoplasm localization | No direct evidence for Hda1; cytosolic relocalization reported for Hda2/Hda3 under hypoxia, not Hda1 | Peterson summary, 2019 | n/a | (peterson2019functionalcharacterizationof pages 75-79) |
| questionable | Positive regulation of macromolecule biosynthetic process | Insufficient direct support for Hda1 itself; stronger evidence is repression/dampening of transcription | Ha, 2019, Nat Commun | https://doi.org/10.1038/s41467-019-12077-w | (ha2019transcriptiondependenttargetingof pages 1-2) |
| questionable | Generic hydrolase activity | Too broad; evidence is specific for histone lysine deacetylase/HDAC activity rather than generic hydrolase | Shen, 2016, Sci Rep | https://doi.org/10.1038/srep33905 | (shen2016structuralandhistone pages 1-2) |
| questionable | Protein binding / identical protein binding | Some support for Hda1 self-interaction and partner binding, but broad GO terms are less informative than complex membership | Wu, 2001, PNAS | https://doi.org/10.1073/pnas.081560698 | (wu2001hda2andhda3 pages 1-2) |
| questionable | Chromosome segregation / centromere role | Genetic and centromeric DNA association evidence exists, but appears non-core/conditional and Hda3 may drive specificity | Kanta, 2006, Genetics | https://doi.org/10.1534/genetics.105.050559 | (kanta2006suppressoranalysisof pages 1-2) |
| questionable | Positive regulation of transcription | Limited/indirect cases from genome-wide data; core literature supports repression far more strongly | Robyr, 2002, Cell | https://doi.org/10.1016/S0092-8674(02)00746-8 | (robyr2002microarraydeacetylationmaps pages 3-5) |
| questionable | Response to heat / HSF1 | 2023 study links Hda1C to starvation-induced HSP reporter repression, but no direct HSF1-specific GO evidence in gathered core papers | Zhang, 2023, thesis/article | https://doi.org/10.17863/cam.101661 | (zhang2023thesaccharomycescerevisiae pages 1-5) |


*Table: This table maps the main requested GO annotation areas for S. cerevisiae HDA1 (P53973) to the strongest experimental evidence found in the gathered literature. It highlights well-supported core annotations and flags weaker or non-core claims that have limited or indirect support.*

### Concluding expert synthesis
Across classic (2000–2002) genome-wide and promoter-focused studies and later mechanistic/structural work (2009–2019), the most robust GO-supported model for Hda1 is: **a nuclear chromatin-associated, Zn2+-dependent histone deacetylase that functions as the catalytic subunit of Hda1C (Hda1/Hda2/Hda3) to deacetylate histones (H2B/H3 and context-dependent H4) and thereby repress or dampen transcription, including at subtelomeric domains and corepressor-bound promoters.** (wu2001tup1utilizeshistone pages 1-2, robyr2002microarraydeacetylationmaps pages 3-5, ha2019transcriptiondependenttargetingof pages 4-5)

Claims that Hda1 is cytoplasmic, broadly activates transcription/biosynthesis, or has central roles in chromosome segregation should be treated as **weak/conditional** unless supported by more direct Hda1-specific localization/functional assays; where segregation phenotypes are observed, evidence points to **Hda3** as the strongest driver within the complex. (peterson2019functionalcharacterizationof pages 75-79, kanta2006suppressoranalysisof pages 11-12)

References

1. (shen2016structuralandhistone pages 1-2): Hui Shen, Yuwei Zhu, Chongyuan Wang, Hui Yan, Maikun Teng, and Xu Li. Structural and histone binding ability characterization of the arb2 domain of a histone deacetylase hda1 from saccharomyces cerevisiae. Scientific Reports, Sep 2016. URL: https://doi.org/10.1038/srep33905, doi:10.1038/srep33905. This article has 18 citations and is from a peer-reviewed journal.

2. (wu2001hda2andhda3 pages 1-2): Jiansheng Wu, Andrew A. Carmen, Ryuji Kobayashi, Noriyuki Suka, and Michael Grunstein. Hda2 and hda3 are related proteins that interact with and are essential for the activity of the yeast histone deacetylase hda1. Proceedings of the National Academy of Sciences of the United States of America, 98:4391-4396, Apr 2001. URL: https://doi.org/10.1073/pnas.081560698, doi:10.1073/pnas.081560698. This article has 89 citations and is from a highest quality peer-reviewed journal.

3. (wu2001tup1utilizeshistone pages 1-2): Jiansheng Wu, Noriyuki Suka, Marian Carlson, and Michael Grunstein. Tup1 utilizes histone h3/h2b-specific hda1 deacetylase to repress gene activity in yeast. Molecular cell, 7 1:117-26, Jan 2001. URL: https://doi.org/10.1016/s1097-2765(01)00160-5, doi:10.1016/s1097-2765(01)00160-5. This article has 303 citations and is from a highest quality peer-reviewed journal.

4. (robyr2002microarraydeacetylationmaps pages 1-2): Daniel Robyr, Yuko Suka, Ioannis Xenarios, Siavash K. Kurdistani, Amy Wang, Noriyuki Suka, and Michael Grunstein. Microarray deacetylation maps determine genome-wide functions for yeast histone deacetylases. Cell, 109:437-446, May 2002. URL: https://doi.org/10.1016/s0092-8674(02)00746-8, doi:10.1016/s0092-8674(02)00746-8. This article has 603 citations and is from a highest quality peer-reviewed journal.

5. (robyr2002microarraydeacetylationmaps pages 5-7): Daniel Robyr, Yuko Suka, Ioannis Xenarios, Siavash K. Kurdistani, Amy Wang, Noriyuki Suka, and Michael Grunstein. Microarray deacetylation maps determine genome-wide functions for yeast histone deacetylases. Cell, 109:437-446, May 2002. URL: https://doi.org/10.1016/s0092-8674(02)00746-8, doi:10.1016/s0092-8674(02)00746-8. This article has 603 citations and is from a highest quality peer-reviewed journal.

6. (zhang2023thesaccharomycescerevisiae pages 1-5): Nianshu Zhang. The saccharomyces cerevisiae acetyltransferase gcn5 exerts antagonistic pleiotropic effects on chronological ageing. JournalArticle, Sep 2023. URL: https://doi.org/10.17863/cam.101661, doi:10.17863/cam.101661. This article has 0 citations.

7. (ha2019transcriptiondependenttargetingof pages 4-5): So Dam Ha, Seokjin Ham, Min Young Kim, Ji Hyun Kim, Insoon Jang, Bo Bae Lee, Min Kyung Lee, Jin-Taek Hwang, Tae-Young Roh, and TaeSoo Kim. Transcription-dependent targeting of hda1c to hyperactive genes mediates h4-specific deacetylation in yeast. Nature Communications, Sep 2019. URL: https://doi.org/10.1038/s41467-019-12077-w, doi:10.1038/s41467-019-12077-w. This article has 28 citations and is from a highest quality peer-reviewed journal.

8. (ha2019transcriptiondependenttargetingof media f27f6bb5): So Dam Ha, Seokjin Ham, Min Young Kim, Ji Hyun Kim, Insoon Jang, Bo Bae Lee, Min Kyung Lee, Jin-Taek Hwang, Tae-Young Roh, and TaeSoo Kim. Transcription-dependent targeting of hda1c to hyperactive genes mediates h4-specific deacetylation in yeast. Nature Communications, Sep 2019. URL: https://doi.org/10.1038/s41467-019-12077-w, doi:10.1038/s41467-019-12077-w. This article has 28 citations and is from a highest quality peer-reviewed journal.

9. (robyr2002microarraydeacetylationmaps pages 3-5): Daniel Robyr, Yuko Suka, Ioannis Xenarios, Siavash K. Kurdistani, Amy Wang, Noriyuki Suka, and Michael Grunstein. Microarray deacetylation maps determine genome-wide functions for yeast histone deacetylases. Cell, 109:437-446, May 2002. URL: https://doi.org/10.1016/s0092-8674(02)00746-8, doi:10.1016/s0092-8674(02)00746-8. This article has 603 citations and is from a highest quality peer-reviewed journal.

10. (lee2009structuralandfunctional pages 1-3): Jung-Hoon Lee, Klaus Maskos, and Robert Huber. Structural and functional studies of the yeast class ii hda1 histone deacetylase complex. Journal of molecular biology, 391 4:744-57, Aug 2009. URL: https://doi.org/10.1016/j.jmb.2009.06.059, doi:10.1016/j.jmb.2009.06.059. This article has 33 citations and is from a domain leading peer-reviewed journal.

11. (ha2019transcriptiondependenttargetingof media 7a4ee2a4): So Dam Ha, Seokjin Ham, Min Young Kim, Ji Hyun Kim, Insoon Jang, Bo Bae Lee, Min Kyung Lee, Jin-Taek Hwang, Tae-Young Roh, and TaeSoo Kim. Transcription-dependent targeting of hda1c to hyperactive genes mediates h4-specific deacetylation in yeast. Nature Communications, Sep 2019. URL: https://doi.org/10.1038/s41467-019-12077-w, doi:10.1038/s41467-019-12077-w. This article has 28 citations and is from a highest quality peer-reviewed journal.

12. (vogelauer2000globalhistoneacetylation pages 1-2): Maria Vogelauer, Jiansheng Wu, Noriyuki Suka, and Michael Grunstein. Global histone acetylation and deacetylation in yeast. Nature, 408:495-498, Nov 2000. URL: https://doi.org/10.1038/35044127, doi:10.1038/35044127. This article has 596 citations and is from a highest quality peer-reviewed journal.

13. (peterson2019functionalcharacterizationof pages 75-79): MR Peterson. Functional characterization of histone deacetylase 2 and histone deacetylase 3 in candida albicans. Unknown journal, 2019.

14. (peterson2019functionalcharacterizationof pages 71-75): MR Peterson. Functional characterization of histone deacetylase 2 and histone deacetylase 3 in candida albicans. Unknown journal, 2019.

15. (kanta2006suppressoranalysisof pages 11-12): Hasna Kanta, Lisa Laprade, Abeer Almutairi, and Inés Pinto. Suppressor analysis of a histone defect identifies a new function for the hda1 complex in chromosome segregation. Genetics, 173:435-450, May 2006. URL: https://doi.org/10.1534/genetics.105.050559, doi:10.1534/genetics.105.050559. This article has 15 citations and is from a domain leading peer-reviewed journal.

16. (kanta2006suppressoranalysisof pages 8-11): Hasna Kanta, Lisa Laprade, Abeer Almutairi, and Inés Pinto. Suppressor analysis of a histone defect identifies a new function for the hda1 complex in chromosome segregation. Genetics, 173:435-450, May 2006. URL: https://doi.org/10.1534/genetics.105.050559, doi:10.1534/genetics.105.050559. This article has 15 citations and is from a domain leading peer-reviewed journal.

17. (ha2019transcriptiondependenttargetingof pages 1-2): So Dam Ha, Seokjin Ham, Min Young Kim, Ji Hyun Kim, Insoon Jang, Bo Bae Lee, Min Kyung Lee, Jin-Taek Hwang, Tae-Young Roh, and TaeSoo Kim. Transcription-dependent targeting of hda1c to hyperactive genes mediates h4-specific deacetylation in yeast. Nature Communications, Sep 2019. URL: https://doi.org/10.1038/s41467-019-12077-w, doi:10.1038/s41467-019-12077-w. This article has 28 citations and is from a highest quality peer-reviewed journal.

18. (kanta2006suppressoranalysisof pages 1-2): Hasna Kanta, Lisa Laprade, Abeer Almutairi, and Inés Pinto. Suppressor analysis of a histone defect identifies a new function for the hda1 complex in chromosome segregation. Genetics, 173:435-450, May 2006. URL: https://doi.org/10.1534/genetics.105.050559, doi:10.1534/genetics.105.050559. This article has 15 citations and is from a domain leading peer-reviewed journal.

## Citations

1. shen2016structuralandhistone pages 1-2
2. zhang2023thesaccharomycescerevisiae pages 1-5
3. lee2009structuralandfunctional pages 1-3
4. robyr2002microarraydeacetylationmaps pages 5-7
5. vogelauer2000globalhistoneacetylation pages 1-2
6. robyr2002microarraydeacetylationmaps pages 3-5
7. kanta2006suppressoranalysisof pages 11-12
8. ha2019transcriptiondependenttargetingof pages 1-2
9. peterson2019functionalcharacterizationof pages 75-79
10. kanta2006suppressoranalysisof pages 1-2
11. robyr2002microarraydeacetylationmaps pages 1-2
12. ha2019transcriptiondependenttargetingof pages 4-5
13. peterson2019functionalcharacterizationof pages 71-75
14. kanta2006suppressoranalysisof pages 8-11
15. https://doi.org/10.17863/cam.101661.
16. https://doi.org/10.1038/s41467-019-12077-w.
17. https://doi.org/10.1016/j.jmb.2009.06.059
18. https://doi.org/10.1073/pnas.081560698
19. https://doi.org/10.1038/s41467-019-12077-w
20. https://doi.org/10.1038/srep33905
21. https://doi.org/10.1016/S1097-2765(01
22. https://doi.org/10.1016/S0092-8674(02
23. https://doi.org/10.1534/genetics.105.050559
24. https://doi.org/10.17863/cam.101661
25. https://doi.org/10.1038/srep33905,
26. https://doi.org/10.1073/pnas.081560698,
27. https://doi.org/10.1016/s1097-2765(01
28. https://doi.org/10.1016/s0092-8674(02
29. https://doi.org/10.17863/cam.101661,
30. https://doi.org/10.1038/s41467-019-12077-w,
31. https://doi.org/10.1016/j.jmb.2009.06.059,
32. https://doi.org/10.1038/35044127,
33. https://doi.org/10.1534/genetics.105.050559,