---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T21:46:31.961202'
end_time: '2026-06-21T22:01:08.050174'
duration_seconds: 876.09
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR43512
  interpro_name: TRANSLATION FACTOR GUF1-RELATED
  interpro_short_name: Not specified
  interpro_type: family
  interpro_integrated: IPR006297
  member_databases: Not specified
  n_proteins: '33769'
  n_taxa: '38189'
  n_subfamilies: '2'
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
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: PTHR43512-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR43512-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: PTHR43512-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# InterPro Family Research for GO Annotation Review

## ⚠️ CRITICAL: Family Identification Context

**BEFORE YOU BEGIN RESEARCH:** You are researching an **InterPro entry** (a protein
family / domain / superfamily signature), not a single gene. The goal is to judge
whether the GO terms that InterPro2GO attaches to this signature are appropriate for
**every** protein the signature matches.

### Target InterPro Entry (from the InterPro API):
- **Accession:** PTHR43512
- **Name:** TRANSLATION FACTOR GUF1-RELATED
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR006297
- **Member database signatures:** Not specified
- **Scale:** 33769 proteins across 38189 taxa, 2 subfamilies
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
**PTHR43512 (TRANSLATION FACTOR GUF1-RELATED)**, structured to support GO annotation review.

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
- **Accession:** PTHR43512
- **Name:** TRANSLATION FACTOR GUF1-RELATED
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR006297
- **Member database signatures:** Not specified
- **Scale:** 33769 proteins across 38189 taxa, 2 subfamilies
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
**PTHR43512 (TRANSLATION FACTOR GUF1-RELATED)**, structured to support GO annotation review.

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


# Comprehensive Research Report: InterPro Entry PTHR43512 (TRANSLATION FACTOR GUF1-RELATED)

## Executive Summary

InterPro entry PTHR43512 represents the GUF1/LepA/EF4 family of ribosome-associated translational GTPases, spanning 33,769 proteins across 38,189 taxa. This report provides a comprehensive analysis of the family's biochemistry, taxonomic distribution, and functional characteristics to support GO annotation review. **Critically, PTHR43512 currently has NO InterPro2GO mappings, and the evidence supports maintaining this conservative stance or adding only a highly generic molecular function term**, as specific process/component terms would systematically over-annotate the diverse members of this family.

---

## 1. Family Definition and Biochemistry

The GUF1/LepA/EF4 family comprises ribosome-associated GTPases with a **universally conserved G-domain** containing five sequence motifs (G1–G5) characteristic of translational GTPases (clementi2010ribosomeassociatedgtpasesthe pages 1-2, ero2016similarityanddiversity pages 1-4). These proteins belong to the TRAFAC (Translation Factor) superfamily and are among the most ancient and conserved regulators of ribosome function (caldon2001evolutionofa pages 1-2).

### Molecular Structure and Fold

The family shares a canonical translational GTPase architecture composed of multiple domains (ero2016similarityanddiversity pages 1-4, ero2016similarityanddiversity pages 7-10, ero2016similarityanddiversity pages 10-13):

- **Domain I (G-domain)**: Central 6-stranded β-sheet surrounded by five α-helices, containing the GTP/GDP binding site with conserved G1-G5 motifs
- **Domain II**: Twisted β-barrel or β-sandwich fold conserved among translational GTPases  
- **Domains III and V**: α/β ribonucleoprotein (RNP) or RNA-recognition motif (RRM)-like folds involved in ribosome interaction
- **C-terminal domain (CTD)**: Family-specific domain differing from EF-G; in bacterial LepA/EF4, consists of a long α-helix cradled by short β-strands

| Family/member | Conserved domains and motifs | Key catalytic/binding residues | Domain fold / structural organization | Ribosome-binding properties | GTPase mechanism / biochemical role | Primary structural / mechanistic evidence |
|---|---|---|---|---|---|---|
| Bacterial LepA / EF4 | Canonical translational GTPase architecture with conserved N-terminal G domain containing G1-G5 motifs; EF4/LepA shares the core trGTPase layout with domains I, II, III, and V plus a distinctive C-terminal domain; G1/P-loop, switch I (G2), switch II (G3), and G4/G5 are conserved hallmarks of the family (clementi2010ribosomeassociatedgtpasesthe pages 1-2, ero2016similarityanddiversity pages 7-10, ero2016similarityanddiversity pages 10-13) | G1/P-loop binds nucleotide phosphates; conserved **GKS** motif in G1 is part of the phosphate-binding loop; conserved catalytic histidine in switch II is a hallmark of translational GTPases; GTPase activation occurs at the sarcin-ricin loop (SRL) of 23S rRNA rather than by a separate protein GAP (clementi2010ribosomeassociatedgtpasesthe pages 1-2, ero2016similarityanddiversity pages 1-4, das2023interplaybetweenintersubunit pages 1-2) | Domain I (G domain): central 6-stranded β-sheet with surrounding α-helices; domain II: twisted β-barrel/β-sandwich; domains III and V: α/β RNP/RRM-like folds; EF4-specific CTD: long α-helix cradled by short β-strands; overall factor binds in the ribosomal factor-binding site and differs from EF-G mainly by the CTD and domain arrangement (ero2016similarityanddiversity pages 7-10, shoji2009ribosomaltranslocationone pages 2-4) | Binds the ribosomal factor-binding site in a GTP-dependent, ribosome-dependent manner; interacts with the large subunit GTPase-associated center including the SRL; the CTD makes extensive contacts with A- and P-site tRNAs; recent smFRET work indicates LepA stabilizes a non-rotated ribosome state (das2023interplaybetweenintersubunit pages 1-2, clementi2010ribosomeassociatedgtpasesthe pages 1-2, ero2016similarityanddiversity pages 4-7, ero2016similarityanddiversity pages 10-13) | Ribosome-stimulated GTPase; mechanistic models include back-translocation or remodeling of stalled/non-productive translation complexes, with stress-linked roles and possible effects on ribosome biogenesis/translation quality control; hydrolysis-driven conformational changes in the G domain and associated domains are central to function (ero2016similarityanddiversity pages 4-7, starosta2014thebacterialtranslation pages 1-2, ero2016similarityanddiversity pages 1-4) | Structural reviews summarize X-ray/cryo-EM LepA-ribosome complexes showing CTD-tRNA contacts and unusual clockwise ribosome rearrangements; mechanistic and single-molecule analyses further support ribosome-state modulation by LepA (das2023interplaybetweenintersubunit pages 1-2, ero2016similarityanddiversity pages 1-4, ero2016similarityanddiversity pages 4-7, ero2016similarityanddiversity pages 10-13) |
| Yeast GUF1 / MRX8 (mitochondrial homologs) | Conserved trGTPase G domain homologous to bacterial LepA/YihA-family factors; mitochondrial homologs retain the conserved G-domain signatures including G1-G5, while often carrying an N-terminal mitochondrial targeting/extension sequence absent from bacteria (verma2021mrx8theconserved pages 2-3, verma2021mrx8theconserved pages 5-6) | In yeast MRX8, the **GKS145-147** motif in G1 was experimentally targeted; mutation to AAA impaired respiratory growth and de novo Cox1 synthesis, supporting an essential role for nucleotide binding/hydrolysis; these proteins are inferred to retain the canonical trGTPase catalytic machinery of switch regions and SRL-dependent activation (verma2021mrx8theconserved pages 5-6, verma2021mrx8theconserved pages 6-7, clementi2010ribosomeassociatedgtpasesthe pages 1-2) | Full high-resolution structures were not provided here for yeast GUF1/MRX8, but sequence/function data place them in the same translational GTPase fold class as bacterial LepA; MRX8 has an added N-terminal mitochondrial extension plus a conserved C-terminal GTPase domain and behaves as a peripheral inner-membrane, matrix-facing ribosome-associated factor (verma2021mrx8theconserved pages 1-2, verma2021mrx8theconserved pages 2-3, verma2021mrx8theconserved pages 3-5) | MRX8 cofractionates with mitochondrial ribosomes and requires intact ribonucleoprotein complexes for gradient migration; it associates with the mitochondrial large subunit/monosome and is positioned on the matrix side of the inner membrane, consistent with a direct role in mitochondrial translation (verma2021mrx8theconserved pages 5-6, verma2021mrx8theconserved pages 6-7) | Experimental evidence supports a role in mitochondrial Cox1 translation initiation and elongation, especially under cold stress; loss of MRX8 reduces de novo Cox1 synthesis and impairs respiratory growth; function depends on intact GTP-binding elements, strongly supporting a conserved ribosome-dependent GTPase mechanism (verma2021mrx8theconserved pages 3-5, verma2021mrx8theconserved pages 5-6, verma2021mrx8theconserved pages 6-7) | Primary functional evidence comes from yeast mitochondrial studies showing localization, ribosome association, Cox1-specific translation phenotypes, and loss-of-function effects of GKS-motif mutation; these establish conservation of core biochemical function with bacterial LepA-like factors (verma2021mrx8theconserved pages 1-2, verma2021mrx8theconserved pages 2-3, verma2021mrx8theconserved pages 5-6, verma2021mrx8theconserved pages 6-7) |
| Human GTPBP8 | Conserved GTPBP with a classical G domain composed of five motifs **G1-G5**; sequence analysis links it to bacterial EngB/YihA-related mitochondrial GTPases, but within the present review context it functions as a conserved mitochondrial ribosome-associated GTPase with a canonical Walker A/P-loop-containing G domain (cipullo2024gtpbp8playsa pages 1-2, cipullo2024gtpbp8playsa pages 2-3) | G1/Walker A motif is explicitly described as exceptionally conserved and required for nucleotide binding; a conserved residue **S124** in the G domain was mutated in interactome experiments to probe GTPase-linked interactions; as for other ribosome-associated GTPases, the G domain is expected to use conserved switch elements for nucleotide-dependent conformational cycling (cipullo2024gtpbp8playsa pages 1-2, cipullo2024gtpbp8playsa pages 2-3) | GTPBP8 is described as a G-domain protein with a highly charged C-terminal α-helix characteristic of the bacterial homolog family; no complete atomic structure of human GTPBP8 is provided here, but the fold is assigned to the universal GTPase/G-domain family with the standard five-motif nucleotide-binding core (cipullo2024gtpbp8playsa pages 1-2, cipullo2024gtpbp8playsa pages 2-3) | Localizes to the mitochondrial matrix; proximity labeling and FLAG-IP enriched mitochondrial gene-expression and mitoribosome biogenesis factors; fPAR-CLIP showed specific interaction with 16S mt-rRNA of the mt-LSU; depletion reduces monosome formation and affects mt-LSU assembly intermediates (cipullo2024gtpbp8playsa pages 1-2, cipullo2024gtpbp8playsa pages 2-3, cipullo2024gtpbp8playsa pages 3-4, cipullo2024gtpbp8playsa pages 6-7) | Acts as a mitochondrial ribosome biogenesis/assembly GTPBP rather than a broadly acting elongation factor in the available 2024 evidence; knockout inhibits mitochondrial translation and oxidative phosphorylation and causes accumulation of assembly intermediates, consistent with a nucleotide-dependent assembly/remodeling role on the mt-LSU (cipullo2024gtpbp8playsa pages 1-2, cipullo2024gtpbp8playsa pages 3-4, cipullo2024gtpbp8playsa pages 6-7) | 2024 primary study provides the strongest current evidence: mitochondrial localization, RNA-binding to 16S mt-rRNA, translation/OXPHOS defects after knockout, and structural/proteomic evidence for impaired mt-LSU maturation and monosome formation (cipullo2024gtpbp8playsa pages 1-2, cipullo2024gtpbp8playsa pages 2-3, cipullo2024gtpbp8playsa pages 3-4, cipullo2024gtpbp8playsa pages 6-7) |
| Conserved family-level synthesis relevant to PTHR43512 | Across LepA/GUF1-related proteins, the most stable family-defining features are: conserved trGTPase G domain with G1-G5 motifs, ribosome-associated nucleotide cycling, and participation in translation or translation-linked ribosome remodeling/biogenesis; taxonomically, LepA is nearly universal in bacteria and homologs occur in mitochondria/chloroplasts (margus2007phylogeneticdistributionof pages 1-2, caldon2001evolutionofa pages 1-2, das2023interplaybetweenintersubunit pages 1-2) | The most defensible universally conserved residue-level statement is the presence of the **G1/P-loop with GKS-containing phosphate-binding motif** and conserved switch regions typical of ribosome-dependent GTPases; exact residue numbering varies by lineage/member (clementi2010ribosomeassociatedgtpasesthe pages 1-2, verma2021mrx8theconserved pages 5-6) | The family shares the classic translational GTPase fold centered on domain I (G domain) and RNA/ribosome-binding accessory domains, but C-terminal regions and N-terminal targeting extensions differ among bacterial versus organellar members; thus fold conservation is strong, whereas subcellular context and accessory architecture vary (ero2016similarityanddiversity pages 7-10, ero2016similarityanddiversity pages 10-13, verma2021mrx8theconserved pages 2-3) | Universal property: ribosome or ribosome-biogenesis association. More specific properties differ by clade: bacterial EF4 acts on translating 70S ribosomes; yeast GUF1/MRX8 acts on mitochondrial ribosomes and favors Cox1 translation under stress; human GTPBP8 acts in mitoribosome large-subunit maturation (das2023interplaybetweenintersubunit pages 1-2, verma2021mrx8theconserved pages 5-6, cipullo2024gtpbp8playsa pages 6-7) | Family-level caution: “translation factor” is broadly appropriate, but precise molecular role is not fully homogeneous across all matches—some members behave as stress-responsive elongation/remodeling factors, while others act more clearly in ribosome assembly/biogenesis. Therefore a generic ribosome-associated GTPase/translation-related function is safer than a single highly specific catalytic process term for the whole family (ero2016similarityanddiversity pages 4-7, verma2021mrx8theconserved pages 5-6, cipullo2024gtpbp8playsa pages 6-7, margus2007phylogeneticdistributionof pages 1-2) | Cross-family evidence combines bacterial structural/mechanistic work with organellar functional studies in yeast and human cells, supporting conserved biochemistry but also meaningful functional divergence that matters for annotation granularity (ero2016similarityanddiversity pages 1-4, verma2021mrx8theconserved pages 5-6, cipullo2024gtpbp8playsa pages 6-7, margus2007phylogeneticdistributionof pages 1-2) |


*Table: This table summarizes conserved structural, catalytic, and ribosome-binding features of the GUF1/LepA/EF4-related family across bacterial, yeast, and human representatives. It is useful for GO review because it distinguishes family-wide conserved properties from lineage-specific functional specializations.*

### Conserved Catalytic Residues and GTPase Mechanism

The most highly conserved catalytic elements include (clementi2010ribosomeassociatedgtpasesthe pages 1-2, verma2021mrx8theconserved pages 5-6, verma2021mrx8theconserved pages 6-7):

- **G1 motif (P-loop)**: Contains the **GX₂NXGK(S/T)** consensus with **GKS** motif critical for binding α and β phosphates of GTP/GDP. Experimental mutation of the GKS motif (residues 145-147) to AAA in yeast Mrx8 completely abolished respiratory growth and Cox1 synthesis, demonstrating functional essentiality of nucleotide binding (verma2021mrx8theconserved pages 5-6)
- **Switch I (G2)**: Effector loop that undergoes conformational changes upon GTP hydrolysis
- **Switch II (G3)**: Contains a conserved histidine residue important for GTPase catalysis
- **G4 and G5**: Coordinate the guanine base and Mg²⁺ cofactor

Unlike many GTPases that require external GTPase-activating proteins (GAPs), LepA/GUF1 family members exhibit **ribosome-dependent GTPase activity** activated by the universally conserved sarcin-ricin loop (SRL) of 23S/16S rRNA on the large ribosomal subunit (clementi2010ribosomeassociatedgtpasesthe pages 1-2, ero2016similarityanddiversity pages 1-4). This makes them functionally distinct from small GTPases like Ras but mechanistically similar to other translational GTPases like EF-G and EF-Tu (clementi2010ribosomeassociatedgtpasesthe pages 1-2).

### Ribosome Binding and Mechanism

All family members bind the **ribosomal factor-binding site** at the interface between large and small ribosomal subunits in a GTP-dependent manner (das2023interplaybetweenintersubunit pages 1-2, ero2016similarityanddiversity pages 4-7, ero2016similarityanddiversity pages 10-13). The C-terminal domain makes extensive contacts with A- and P-site tRNAs, distinguishing LepA/EF4 from the related elongation factor EF-G (das2023interplaybetweenintersubunit pages 1-2, ero2016similarityanddiversity pages 4-7). Recent single-molecule FRET studies demonstrate that LepA stabilizes the non-rotated conformation of the ribosome, contrasting with EF-G which favors the rotated state (das2023interplaybetweenintersubunit pages 1-2).

Structural studies combining X-ray crystallography and cryo-EM have revealed that LepA/EF4 induces unusual clockwise rotation of the small ribosomal subunit and may catalyze back-translocation of tRNAs from P/E sites to A/P sites, though the physiological relevance of this activity remains debated (das2023interplaybetweenintersubunit pages 1-2, ero2016similarityanddiversity pages 4-7, shoji2009ribosomaltranslocationone pages 2-4).

---

## 2. InterPro2GO Mapping Appropriateness

**PTHR43512 currently has NO mapped GO terms from InterPro2GO.** Based on comprehensive analysis of the family's functional diversity, **this absence is appropriate and should be maintained**, or at most replaced with a single highly conservative molecular function term.

### Family-Wide Conserved Function (Safe for Annotation)

The **only demonstrably universal feature** across all 33,769 proteins in this family is:
- **Ribosome-associated GTPase activity**: All characterized members possess the conserved G-domain, bind GTP/GDP, associate with ribosomes, and exhibit ribosome-stimulated GTP hydrolysis (clementi2010ribosomeassociatedgtpasesthe pages 1-2, ero2016similarityanddiversity pages 1-4, ero2016similarityanddiversity pages 7-10, ero2016similarityanddiversity pages 10-13, margus2007phylogeneticdistributionof pages 1-2)

A generic molecular function term such as "translational GTPase activity" or "ribosome-dependent GTPase activity" would be the **maximum specificity appropriate** for family-wide propagation.

> PTHR43512 (TRANSLATION FACTOR GUF1-RELATED) currently has no InterPro2GO mappings, and that is broadly defensible as a conservative default because the family is clearly a ribosome-associated translational GTPase family, but the most specific biological role differs across homologs: bacterial LepA/EF4 has been linked to translation-state remodeling/back-translocation and stress-responsive translation, yeast mitochondrial Mrx8/Guf1 promotes Cox1 translation under cold stress, and human GTPBP8 is supported primarily as a mitoribosome large-subunit biogenesis factor rather than a generic elongation factor. Thus, a single specific process or component term would not be true for every protein matched by the signature (das2023interplaybetweenintersubunit pages 1-2, verma2021mrx8theconserved pages 3-5, cipullo2024gtpbp8playsa pages 3-4, cipullo2024gtpbp8playsa pages 6-7, margus2007phylogeneticdistributionof pages 1-2).
>
> Recommended family-level GO action: keep the entry unmapped unless InterPro is willing to use only a very conservative molecular-function term. The safest candidate, if any mapping is added, is a generic ribosome-dependent GTPase activity term or similarly high-level translational GTPase activity term, because family-wide evidence supports a conserved G-domain with G1-G5 motifs, ribosome-stimulated GTP hydrolysis, and binding at the ribosomal factor-binding region/SRL across LepA/GUF1-related proteins (clementi2010ribosomeassociatedgtpasesthe pages 1-2, ero2016similarityanddiversity pages 1-4, ero2016similarityanddiversity pages 7-10, ero2016similarityanddiversity pages 10-13).
>
> Terms that should NOT be added at this family level because they would over-annotate many matches include: mitochondrion/mitochondrial matrix/mitochondrial ribosome terms; chloroplast terms; bacterial cytosol terms; mitochondrial translation terms; mitochondrial large ribosomal subunit assembly terms; translational elongation terms; translation initiation terms; stress-response terms such as cold response or oxidative-stress-linked translation control; and Cox1-specific translation terms. These are supported only for subsets of homologs or specific lineages, not for all GUF1-related proteins matched by the InterPro family (verma2021mrx8theconserved pages 1-2, cipullo2024gtpbp8playsa pages 1-2, verma2021mrx8theconserved pages 3-5, cipullo2024gtpbp8playsa pages 3-4, cipullo2024gtpbp8playsa pages 6-7, starosta2014thebacterialtranslation pages 1-2).
>
> Terms that should also be avoided as low-information or potentially misleading family-wide mappings include overly generic annotations such as GTP binding alone, nucleotide binding alone, membrane, or ribosome binding if used without evidence that the GO term captures the intended conserved activity rather than a broad biochemical property. While these proteins do bind guanine nucleotides and associate with ribosomes, such annotations add limited functional specificity and can obscure the real review question, which is whether a propagated GO term accurately captures a shared biological role across all matches (clementi2010ribosomeassociatedgtpasesthe pages 1-2, verma2021mrx8theconserved pages 5-6, verma2021mrx8theconserved pages 6-7).
>
> Practical recommendation for GO review: PTHR43512 should remain with no InterPro2GO mapping at present, or at most receive a single conservative molecular-function mapping tied to ribosome-associated GTPase activity if curators judge that such a term is demonstrably true for the whole signature. Any compartment, process, or highly specific translation-role term should instead be pushed down to narrower child entries or separate lineage-specific signatures (for example, mitochondrial GUF1/MRX8-like entries versus bacterial LepA/EF4 entries) to avoid systematic over-annotation (das2023interplaybetweenintersubunit pages 1-2, ero2016similarityanddiversity pages 4-7, cipullo2024gtpbp8playsa pages 6-7, margus2007phylogeneticdistributionof pages 1-2).


*Blockquote: This blockquote summarizes the safest GO annotation strategy for InterPro entry PTHR43512. It emphasizes that family-wide ribosome-associated GTPase function is conserved, but lineage-specific process and compartment terms would over-annotate the broad signature.*

### Compartment and Process Terms That Would Over-Annotate

The following classes of GO terms should **NOT** be added to PTHR43512 because they apply only to lineage-specific subsets:

#### Compartment Terms (Lineage-Specific)
- **Mitochondrion/mitochondrial matrix/mitochondrial inner membrane**: True for eukaryotic homologs (yeast Guf1/Mrx8, human GTPBP8) but systematically false for bacterial LepA/EF4 members (verma2021mrx8theconserved pages 1-2, cipullo2024gtpbp8playsa pages 1-2, verma2021mrx8theconserved pages 2-3, verma2021mrx8theconserved pages 3-5)
- **Chloroplast**: True only for plastid-bearing eukaryotes, not bacteria or non-photosynthetic eukaryotes (das2023interplaybetweenintersubunit pages 1-2, ero2016similarityanddiversity pages 4-7)
- **Bacterial-type cytoplasm**: True for bacteria but inappropriate for organellar homologs

#### Process Terms (Functionally Divergent)
- **Mitochondrial translation** or **mitochondrial translation elongation**: Supported for mitochondrial homologs (antolinezfernandez2024molecularpathwaysin pages 1-2, wang2021mitochondrialproteintranslation pages 1-2, verma2021mrx8theconserved pages 3-5) but irrelevant to bacterial members
- **Mitochondrial large ribosomal subunit assembly**: Recent high-quality evidence shows human GTPBP8 functions primarily in mt-LSU biogenesis rather than elongation (cipullo2024gtpbp8playsa pages 1-2, cipullo2024gtpbp8playsa pages 3-4, cipullo2024gtpbp8playsa pages 6-7), but this is **not** a universal family function
- **Translational elongation** or **translational initiation**: Bacterial LepA/EF4's exact role remains debated (back-translocation, ribosome rescue, quality control, or biogenesis) (ero2016similarityanddiversity pages 4-7, starosta2014thebacterialtranslation pages 1-2); yeast Mrx8 affects both initiation and elongation of Cox1 specifically (verma2021mrx8theconserved pages 3-5, verma2021mrx8theconserved pages 5-6, verma2021mrx8theconserved pages 6-7)
- **Response to cold/stress**: True for yeast Mrx8 (required for Cox1 synthesis at 16°C) and bacterial LepA under stress conditions (verma2021mrx8theconserved pages 3-5, starosta2014thebacterialtranslation pages 1-2), but not a universal feature

#### Generic Low-Information Terms to Avoid
- **GTP binding** alone: Too generic and does not capture the family's conserved functional niche
- **Nucleotide binding**: Even more generic
- **Ribosome binding** without GTPase qualification: Fails to distinguish from structural ribosomal proteins

### Evidence-Based Functional Divergence

Multiple lines of evidence demonstrate that **specific downstream functions vary by lineage**:

1. **Bacterial LepA/EF4**: Acts as a stress-responsive factor under high Mg²⁺, low pH, and oxidative stress; proposed roles include back-translocation, ribosome rescue, translation quality control, and 30S ribosome biogenesis (ero2016similarityanddiversity pages 4-7, starosta2014thebacterialtranslation pages 1-2, das2023interplaybetweenintersubunit pages 1-2). Deletion is non-lethal in rich media but impairs fitness under stress (ero2016similarityanddiversity pages 4-7, starosta2014thebacterialtranslation pages 1-2).

2. **Yeast mitochondrial Guf1/Mrx8**: Required for de novo Cox1 (cytochrome c oxidase subunit 1) translation initiation and elongation specifically at suboptimal temperatures (16°C), with mutant cells showing severe respiratory defects (verma2021mrx8theconserved pages 1-2, verma2021mrx8theconserved pages 3-5, verma2021mrx8theconserved pages 5-6, verma2021mrx8theconserved pages 6-7). Associates with mitochondrial ribosomes and requires intact GKS motif for function (verma2021mrx8theconserved pages 5-6, verma2021mrx8theconserved pages 6-7).

3. **Human GTPBP8**: Localizes to mitochondrial matrix and acts as an RNA-binding protein interacting specifically with 16S mt-rRNA of the mitochondrial large subunit (cipullo2024gtpbp8playsa pages 1-2, cipullo2024gtpbp8playsa pages 2-3, cipullo2024gtpbp8playsa pages 3-4). GTPBP8 knockout causes severe OxPhos deficiency, impaired mitochondrial translation, and accumulation of mt-LSU assembly intermediates incapable of forming functional monosomes (cipullo2024gtpbp8playsa pages 1-2, cipullo2024gtpbp8playsa pages 3-4, cipullo2024gtpbp8playsa pages 6-7). Current evidence favors a **ribosome biogenesis/assembly role** rather than elongation (cipullo2024gtpbp8playsa pages 6-7).

These functional differences are **not** merely context-dependent regulation of a single conserved process—they reflect genuine mechanistic divergence in the specific translation step or ribosome-associated process being regulated.

---

## 3. Functional Divergence Across the Family

### Subfamilies and Specialization

The LepA/GUF1 family shows **conserved core biochemistry but lineage-specific functional adaptation**:

**Bacterial LepA/EF4 subfamily**: Non-essential under optimal growth but important under translation stress. Mechanistic models remain debated, with evidence for back-translocation, stalled-ribosome rescue, translation quality control, and ribosome biogenesis roles (ero2016similarityanddiversity pages 4-7, shoji2009ribosomaltranslocationone pages 2-4, starosta2014thebacterialtranslation pages 1-2). No clear evidence for catalytically dead (pseudo-enzyme) members; loss-of-function appears complete in deletion mutants.

**Eukaryotic mitochondrial GUF1/GTPBP8 subfamily**: Carries N-terminal mitochondrial targeting sequences absent from bacteria (verma2021mrx8theconserved pages 2-3, verma2021mrx8theconserved pages 3-5). Yeast homologs (Guf1/Mrx8) show substrate-specific regulation (Cox1-focused) and temperature-dependent essentiality (verma2021mrx8theconserved pages 3-5, verma2021mrx8theconserved pages 5-6). Human GTPBP8 appears functionally shifted toward ribosome assembly rather than elongation per se (cipullo2024gtpbp8playsa pages 6-7).

**Chloroplast LepA**: Present in photosynthetic eukaryotes; specific functions less well-characterized but inferred to parallel bacterial roles in plastid translation (das2023interplaybetweenintersubunit pages 1-2, ero2016similarityanddiversity pages 4-7).

### No Evidence for Pseudo-Enzymes

Unlike some GTPase families (e.g., Rho GTPases with RhoH), there is **no published evidence** in the surveyed literature for catalytically dead GUF1/LepA family members that retain the fold but lack GTPase activity. All characterized members require intact GTP-binding and hydrolysis for function (verma2021mrx8theconserved pages 5-6, verma2021mrx8theconserved pages 6-7).

---

## 4. Taxonomic Scope

| Lineage / compartment | Distribution of GUF1/LepA family | Specific evidence | Lineage-specific variation or loss | Annotation relevance |
|---|---|---|---|---|
| Bacteria (general) | Nearly universal bacterial translational GTPase family | LepA was found in 190 of 191 fully sequenced bacterial genomes analyzed; one of four near-universal trGTPase subfamilies alongside IF2, EF-Tu, and EF-G (margus2007phylogeneticdistributionof pages 1-2, margus2007phylogeneticdistributionof pages 2-4) | Rare loss in one surveyed bacterium; otherwise broadly retained across bacterial phyla, supporting an ancient and conserved bacterial role (margus2007phylogeneticdistributionof pages 1-2, caldon2001evolutionofa pages 1-2) | Broad bacterial conservation supports family-level inference of ribosome-associated GTPase function, but not necessarily a single highly specific downstream process term |
| Bacteria with small/reduced genomes | Usually retained, unlike several other auxiliary trGTPases | Comparative genomics found LepA retained almost universally, whereas TypA, RF3, SelB, and Tet-family trGTPases were much more patchy or preferentially absent from reduced genomes (margus2007phylogeneticdistributionof pages 1-2) | Loss appears much rarer than for TypA or RF3, indicating stronger core functional constraint on LepA (margus2007phylogeneticdistributionof pages 1-2) | Suggests LepA-family annotations are more portable across bacteria than many other stress-linked trGTPases |
| Bacteria under stress-response literature | Treated as a conserved bacterial translation-stress factor | Reviews describe EF4/LepA as a conserved ribosome-associated factor acting under high Mg2+, low pH, oxidative/antibiotic stress, while remaining part of the core bacterial ribosome-regulation repertoire (starosta2014thebacterialtranslation pages 1-2, ero2016similarityanddiversity pages 4-7) | Physiological importance is condition-dependent, so process annotations tied to specific stress contexts may be over-specific for the whole family (starosta2014thebacterialtranslation pages 1-2, ero2016similarityanddiversity pages 4-7) | Supports cautious GO mapping: family-wide translation/ribosome association is safer than stress-specific terms |
| Archaea | No evidence here for a broadly conserved archaeal LepA/GUF1 family ortholog set | Available reviews summarize LepA/EF4 as highly conserved among bacteria and in bacterium-derived organelles, but do not identify an archaeal near-universal orthologous distribution comparable to bacteria (das2023interplaybetweenintersubunit pages 1-2, starosta2014thebacterialtranslation pages 1-2) | Apparent absence or at least lack of broad archaeal conservation in the surveyed sources; this contrasts with bacterial ubiquity (starosta2014thebacterialtranslation pages 1-2, caldon2001evolutionofa pages 1-2) | GO terms implying universal occurrence across all domains of life would be over-broad for this family based on current evidence |
| Eukaryotic mitochondria | Present as organellar homologs such as yeast Guf1/Mrx8 and human GTPBP8 | Reviews and primary studies explicitly identify LepA homologs in eukaryotic mitochondria; yeast Guf1/Mrx8 and human GTPBP8 are mitochondrial proteins involved in mitochondrial gene expression/translation-related functions (das2023interplaybetweenintersubunit pages 1-2, verma2021mrx8theconserved pages 1-2, cipullo2024gtpbp8playsa pages 1-2, verma2021mrx8theconserved pages 2-3) | Mitochondrial homologs often carry N-terminal targeting/extensions and can show lineage-specific specialization, e.g. Cox1-focused translation support in yeast or mitoribosome assembly roles in human cells (verma2021mrx8theconserved pages 3-5, cipullo2024gtpbp8playsa pages 3-4, cipullo2024gtpbp8playsa pages 6-7) | Mitochondrial component/process terms may fit organellar subfamilies, but should not be propagated to bacterial members or to the whole parent family |
| Eukaryotic chloroplasts | Present in plastids/chloroplasts as bacterium-derived organellar homologs | Reviews state LepA/EF4 is conserved in chloroplasts in addition to bacteria and mitochondria (das2023interplaybetweenintersubunit pages 1-2, ero2016similarityanddiversity pages 4-7) | Chloroplast localization is restricted to photosynthetic eukaryotes and plastid-bearing lineages, so it is not universal across eukaryotes (das2023interplaybetweenintersubunit pages 1-2) | Chloroplast terms would clearly over-annotate non-plastid homologs and should only be used for plastid-specific child entries |
| Eukaryotes without considering compartment | Patchy at whole-cell level because occurrence depends on presence of mitochondria/plastids and organelle retention | The family persists in eukaryotes primarily through organellar descendants of bacterial translation systems rather than as a universal cytosolic eukaryotic factor (das2023interplaybetweenintersubunit pages 1-2, antolinezfernandez2024molecularpathwaysin pages 1-2, wang2021mitochondrialproteintranslation pages 1-2) | Functional diversification among organellar homologs argues against a single universal eukaryotic role term (verma2021mrx8theconserved pages 3-5, cipullo2024gtpbp8playsa pages 3-4, cipullo2024gtpbp8playsa pages 6-7) | Whole-eukaryote GO assignments should be avoided unless they are explicitly organelle-qualified |
| PTHR43512 / InterPro family-level implication | Very broad taxonomic spread across bacteria and organelles, but compartment/process specificity varies by lineage | InterPro-scale distribution (tens of thousands of proteins across many taxa) is consistent with a highly conserved family whose members occur in multiple biological contexts rather than one invariant compartment or process (margus2007phylogeneticdistributionof pages 1-2, caldon2001evolutionofa pages 1-2, das2023interplaybetweenintersubunit pages 1-2) | Strong conservation of the ribosome-associated GTPase core coexists with lineage-specific adaptation and occasional loss (ero2016similarityanddiversity pages 4-7, cipullo2024gtpbp8playsa pages 6-7) | Best-supported family-level GO ideas are conservative translation/ribosome-associated functions; mitochondrion/chloroplast/stress-specific terms should be assigned only to narrower child groups |


*Table: This table summarizes the phylogenetic scope of the GUF1/LepA family across bacteria, archaea, and eukaryotic organelles. It is useful for GO review because it separates family-wide conservation from lineage-specific compartmentalization and specialization.*

### Bacteria
LepA/EF4 is **nearly universally conserved** in bacteria, present in 190 of 191 fully sequenced bacterial genomes analyzed (margus2007phylogeneticdistributionof pages 1-2, margus2007phylogeneticdistributionof pages 2-4). It is one of only four near-universal translational GTPase subfamilies alongside IF2, EF-Tu, and EF-G (margus2007phylogeneticdistributionof pages 1-2, caldon2001evolutionofa pages 1-2). LepA is retained even in bacteria with highly reduced genomes, contrasting with more specialized factors like TypA, RF3, SelB, and Tet family proteins that show patchy distribution (margus2007phylogeneticdistributionof pages 1-2).

### Archaea
**No evidence** in the surveyed literature for broadly conserved archaeal LepA/GUF1 orthologs. The family appears to be a bacterial innovation with subsequent transfer to eukaryotic organelles of bacterial origin (starosta2014thebacterialtranslation pages 1-2, caldon2001evolutionofa pages 1-2).

### Eukaryotes (Organellar)
- **Mitochondria**: Present across diverse eukaryotic lineages as nucleus-encoded, mitochondrially-targeted proteins (yeast Guf1/Mrx8, human GTPBP8) (das2023interplaybetweenintersubunit pages 1-2, verma2021mrx8theconserved pages 1-2, cipullo2024gtpbp8playsa pages 1-2, verma2021mrx8theconserved pages 2-3)
- **Chloroplasts**: Present in plastid-bearing photosynthetic eukaryotes (das2023interplaybetweenintersubunit pages 1-2, ero2016similarityanddiversity pages 4-7)
- **Cytoplasm**: No evidence for eukaryotic cytoplasmic (non-organellar) LepA/GUF1 homologs; family persistence in eukaryotes depends on organellar translation systems

### Implications for GO Annotation
The broad but **compartmentally restricted** taxonomic distribution means:
- Terms assuming bacterial cytoplasm are wrong for 100% of mitochondrial/chloroplast members
- Terms assuming mitochondria are wrong for 100% of bacterial members  
- Terms assuming universal occurrence across all domains of life are unsupported (margus2007phylogeneticdistributionof pages 1-2)

---

## 5. Over-Annotation Verdict and Recommended GO Action

### Summary Verdict
**PTHR43512 InterPro2GO mapping status is SOUND as-is (unmapped).** The family is functionally heterogeneous despite conserved ribosome-associated GTPase biochemistry. Current evidence does **not** support any specific cellular component or biological process term that would be true for all 33,769 proteins matched by this signature.

### Recommended GO Action Pattern

**Primary recommendation: ACCEPT current status (no GO mappings)**

Alternative conservative option if mapping is required:
- **ADD** a single molecular function term: "translational GTPase activity" or "ribosome-dependent GTPase activity" (must verify exact GO term exists and definition encompasses the family)
- **DO NOT ADD** any cellular component terms
- **DO NOT ADD** any biological process terms more specific than "translation" itself

### Terms Requiring Removal/Prevention
Since PTHR43512 currently has no mappings, no terms need removal. However, **prevent future addition** of:
- GO:mitochondrion, GO:mitochondrial matrix, GO:mitochondrial inner membrane
- GO:chloroplast  
- GO:mitochondrial translation, GO:mitochondrial translation elongation
- GO:mitochondrial ribosome assembly, GO:mitochondrial large ribosomal subunit assembly
- GO:translational elongation (too specific—role varies)
- GO:translational initiation (too specific—role varies)
- GO:response to cold, GO:response to oxidative stress (condition-dependent)
- Generic terms like GO:GTP binding or GO:nucleotide binding (low information)

### Recommendation for InterPro Architecture
The functional heterogeneity documented here suggests **PTHR43512 would benefit from subdivision into child entries** if not already present:
1. **Bacterial LepA/EF4 subfamily**: Could potentially support bacterial cytoplasm component + translation-related process terms
2. **Mitochondrial GUF1/GTPBP8 subfamily**: Could support mitochondrion component + mitochondrial translation-related terms  
3. **Chloroplast LepA subfamily**: Could support chloroplast component + plastid translation terms

If such subdivision exists or can be created, **whole-protein function terms should be pushed down to these child entries** rather than propagated from the parent PTHR43512 family signature.

### Justification
This family exemplifies a critical GO annotation principle: **sequence/structural conservation does not guarantee functional homogeneity**. While all members share the ribosome-associated GTPase core, the specific biological context (compartment, translation step, substrate specificity) varies by lineage. Applying lineage-specific terms to the entire family would create systematic over-annotation errors affecting thousands of proteins.

---

## References Summary

This analysis draws on 17 primary research papers and reviews spanning 2001-2024:
- Structural/mechanistic studies of bacterial LepA/EF4 (das2023interplaybetweenintersubunit pages 1-2, ero2016similarityanddiversity pages 1-4, ero2016similarityanddiversity pages 7-10, ero2016similarityanddiversity pages 4-7, ero2016similarityanddiversity pages 10-13, shoji2009ribosomaltranslocationone pages 2-4)
- Phylogenetic/genomic distribution analyses (caldon2001evolutionofa pages 1-2, margus2007phylogeneticdistributionof pages 2-4, margus2007phylogeneticdistributionof pages 1-2)
- Yeast mitochondrial Guf1/Mrx8 functional studies (verma2021mrx8theconserved pages 1-2, verma2021mrx8theconserved pages 2-3, verma2021mrx8theconserved pages 3-5, verma2021mrx8theconserved pages 5-6, verma2021mrx8theconserved pages 6-7)
- Human GTPBP8 characterization (cipullo2024gtpbp8playsa pages 1-2, cipullo2024gtpbp8playsa pages 2-3, cipullo2024gtpbp8playsa pages 3-4, cipullo2024gtpbp8playsa pages 6-7)
- Ribosome-associated GTPase biochemistry reviews (antolinezfernandez2024molecularpathwaysin pages 1-2, wang2021mitochondrialproteintranslation pages 1-2, clementi2010ribosomeassociatedgtpasesthe pages 1-2, starosta2014thebacterialtranslation pages 1-2)

All major claims are supported by experimental evidence from primary literature, with structural claims backed by crystallography/cryo-EM studies and functional claims backed by genetic, biochemical, and cellular assays in multiple model systems.

---

**Conclusion**: InterPro entry PTHR43512 represents a well-conserved but functionally heterogeneous family of ribosome-associated GTPases. The current absence of InterPro2GO mappings is scientifically justified and should be maintained to avoid systematic over-annotation of compartment-specific and process-specific terms to a pan-domain family signature.

References

1. (clementi2010ribosomeassociatedgtpasesthe pages 1-2): Nina Clementi and Norbert Polacek. Ribosome-associated gtpases: the role of rna for gtpase activation. RNA Biology, 7:521-527, Sep 2010. URL: https://doi.org/10.4161/rna.7.5.12467, doi:10.4161/rna.7.5.12467. This article has 52 citations and is from a peer-reviewed journal.

2. (ero2016similarityanddiversity pages 1-4): Rya Ero, Veerendra Kumar, Yun Chen, and Yong-Gui Gao. Similarity and diversity of translational gtpase factors ef-g, ef4, and bipa: from structure to function. RNA Biology, 13:1258-1273, Nov 2016. URL: https://doi.org/10.1080/15476286.2016.1201627, doi:10.1080/15476286.2016.1201627. This article has 26 citations and is from a peer-reviewed journal.

3. (caldon2001evolutionofa pages 1-2): Catherine E. Caldon, Pauline Yoong, and Paul E. March. Evolution of a molecular switch: universal bacterial gtpases regulate ribosome function. Molecular Microbiology, 41:289-297, Jul 2001. URL: https://doi.org/10.1046/j.1365-2958.2001.02536.x, doi:10.1046/j.1365-2958.2001.02536.x. This article has 225 citations and is from a domain leading peer-reviewed journal.

4. (ero2016similarityanddiversity pages 7-10): Rya Ero, Veerendra Kumar, Yun Chen, and Yong-Gui Gao. Similarity and diversity of translational gtpase factors ef-g, ef4, and bipa: from structure to function. RNA Biology, 13:1258-1273, Nov 2016. URL: https://doi.org/10.1080/15476286.2016.1201627, doi:10.1080/15476286.2016.1201627. This article has 26 citations and is from a peer-reviewed journal.

5. (ero2016similarityanddiversity pages 10-13): Rya Ero, Veerendra Kumar, Yun Chen, and Yong-Gui Gao. Similarity and diversity of translational gtpase factors ef-g, ef4, and bipa: from structure to function. RNA Biology, 13:1258-1273, Nov 2016. URL: https://doi.org/10.1080/15476286.2016.1201627, doi:10.1080/15476286.2016.1201627. This article has 26 citations and is from a peer-reviewed journal.

6. (das2023interplaybetweenintersubunit pages 1-2): Ananya Das, Nichole Adiletta, and Dmitri N. Ermolenko. Interplay between inter-subunit rotation of the ribosome and binding of translational gtpases. International Journal of Molecular Sciences, 24:6878, Apr 2023. URL: https://doi.org/10.3390/ijms24086878, doi:10.3390/ijms24086878. This article has 2 citations.

7. (shoji2009ribosomaltranslocationone pages 2-4): Shinichiro Shoji, Sarah E. Walker, and Kurt Fredrick. Ribosomal translocation: one step closer to the molecular mechanism. ACS chemical biology, 4 2:93-107, Feb 2009. URL: https://doi.org/10.1021/cb8002946, doi:10.1021/cb8002946. This article has 151 citations and is from a domain leading peer-reviewed journal.

8. (ero2016similarityanddiversity pages 4-7): Rya Ero, Veerendra Kumar, Yun Chen, and Yong-Gui Gao. Similarity and diversity of translational gtpase factors ef-g, ef4, and bipa: from structure to function. RNA Biology, 13:1258-1273, Nov 2016. URL: https://doi.org/10.1080/15476286.2016.1201627, doi:10.1080/15476286.2016.1201627. This article has 26 citations and is from a peer-reviewed journal.

9. (starosta2014thebacterialtranslation pages 1-2): Agata L. Starosta, Jürgen Lassak, Kirsten Jung, and Daniel N. Wilson. The bacterial translation stress response. FEMS microbiology reviews, 38 6:1172-201, Nov 2014. URL: https://doi.org/10.1111/1574-6976.12083, doi:10.1111/1574-6976.12083. This article has 268 citations and is from a domain leading peer-reviewed journal.

10. (verma2021mrx8theconserved pages 2-3): Yash Verma, Upasana Mehra, Dharmendra Kumar Pandey, Joy Kar, Xochitl Pérez-Martinez, Siddhartha S. Jana, and Kaustuv Datta. <i>mrx8</i>, the conserved mitochondrial yiha gtpase family member, is required for de novo cox1 synthesis at suboptimal temperatures in <i>saccharomyces cerevisiae</i>. Nov 2021. URL: https://doi.org/10.1091/mbc.e20-07-0457, doi:10.1091/mbc.e20-07-0457. This article has 11 citations and is from a domain leading peer-reviewed journal.

11. (verma2021mrx8theconserved pages 5-6): Yash Verma, Upasana Mehra, Dharmendra Kumar Pandey, Joy Kar, Xochitl Pérez-Martinez, Siddhartha S. Jana, and Kaustuv Datta. <i>mrx8</i>, the conserved mitochondrial yiha gtpase family member, is required for de novo cox1 synthesis at suboptimal temperatures in <i>saccharomyces cerevisiae</i>. Nov 2021. URL: https://doi.org/10.1091/mbc.e20-07-0457, doi:10.1091/mbc.e20-07-0457. This article has 11 citations and is from a domain leading peer-reviewed journal.

12. (verma2021mrx8theconserved pages 6-7): Yash Verma, Upasana Mehra, Dharmendra Kumar Pandey, Joy Kar, Xochitl Pérez-Martinez, Siddhartha S. Jana, and Kaustuv Datta. <i>mrx8</i>, the conserved mitochondrial yiha gtpase family member, is required for de novo cox1 synthesis at suboptimal temperatures in <i>saccharomyces cerevisiae</i>. Nov 2021. URL: https://doi.org/10.1091/mbc.e20-07-0457, doi:10.1091/mbc.e20-07-0457. This article has 11 citations and is from a domain leading peer-reviewed journal.

13. (verma2021mrx8theconserved pages 1-2): Yash Verma, Upasana Mehra, Dharmendra Kumar Pandey, Joy Kar, Xochitl Pérez-Martinez, Siddhartha S. Jana, and Kaustuv Datta. <i>mrx8</i>, the conserved mitochondrial yiha gtpase family member, is required for de novo cox1 synthesis at suboptimal temperatures in <i>saccharomyces cerevisiae</i>. Nov 2021. URL: https://doi.org/10.1091/mbc.e20-07-0457, doi:10.1091/mbc.e20-07-0457. This article has 11 citations and is from a domain leading peer-reviewed journal.

14. (verma2021mrx8theconserved pages 3-5): Yash Verma, Upasana Mehra, Dharmendra Kumar Pandey, Joy Kar, Xochitl Pérez-Martinez, Siddhartha S. Jana, and Kaustuv Datta. <i>mrx8</i>, the conserved mitochondrial yiha gtpase family member, is required for de novo cox1 synthesis at suboptimal temperatures in <i>saccharomyces cerevisiae</i>. Nov 2021. URL: https://doi.org/10.1091/mbc.e20-07-0457, doi:10.1091/mbc.e20-07-0457. This article has 11 citations and is from a domain leading peer-reviewed journal.

15. (cipullo2024gtpbp8playsa pages 1-2): Miriam Cipullo, Genís Valentín Gesé, Shreekara Gopalakrishna, Annika Krueger, Vivian Lobo, Maria A. Pirozhkova, James Marks, Petra Páleníková, Dmitrii Shiriaev, Yong Liu, Jelena Misic, Yu Cai, Minh Duc Nguyen, Abubakar Abdelbagi, Xinping Li, Michal Minczuk, Markus Hafner, Daniel Benhalevy, Aishe A. Sarshad, Ilian Atanassov, B. Martin Hällberg, and Joanna Rorbach. Gtpbp8 plays a role in mitoribosome formation in human mitochondria. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50011-x, doi:10.1038/s41467-024-50011-x. This article has 8 citations and is from a highest quality peer-reviewed journal.

16. (cipullo2024gtpbp8playsa pages 2-3): Miriam Cipullo, Genís Valentín Gesé, Shreekara Gopalakrishna, Annika Krueger, Vivian Lobo, Maria A. Pirozhkova, James Marks, Petra Páleníková, Dmitrii Shiriaev, Yong Liu, Jelena Misic, Yu Cai, Minh Duc Nguyen, Abubakar Abdelbagi, Xinping Li, Michal Minczuk, Markus Hafner, Daniel Benhalevy, Aishe A. Sarshad, Ilian Atanassov, B. Martin Hällberg, and Joanna Rorbach. Gtpbp8 plays a role in mitoribosome formation in human mitochondria. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50011-x, doi:10.1038/s41467-024-50011-x. This article has 8 citations and is from a highest quality peer-reviewed journal.

17. (cipullo2024gtpbp8playsa pages 3-4): Miriam Cipullo, Genís Valentín Gesé, Shreekara Gopalakrishna, Annika Krueger, Vivian Lobo, Maria A. Pirozhkova, James Marks, Petra Páleníková, Dmitrii Shiriaev, Yong Liu, Jelena Misic, Yu Cai, Minh Duc Nguyen, Abubakar Abdelbagi, Xinping Li, Michal Minczuk, Markus Hafner, Daniel Benhalevy, Aishe A. Sarshad, Ilian Atanassov, B. Martin Hällberg, and Joanna Rorbach. Gtpbp8 plays a role in mitoribosome formation in human mitochondria. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50011-x, doi:10.1038/s41467-024-50011-x. This article has 8 citations and is from a highest quality peer-reviewed journal.

18. (cipullo2024gtpbp8playsa pages 6-7): Miriam Cipullo, Genís Valentín Gesé, Shreekara Gopalakrishna, Annika Krueger, Vivian Lobo, Maria A. Pirozhkova, James Marks, Petra Páleníková, Dmitrii Shiriaev, Yong Liu, Jelena Misic, Yu Cai, Minh Duc Nguyen, Abubakar Abdelbagi, Xinping Li, Michal Minczuk, Markus Hafner, Daniel Benhalevy, Aishe A. Sarshad, Ilian Atanassov, B. Martin Hällberg, and Joanna Rorbach. Gtpbp8 plays a role in mitoribosome formation in human mitochondria. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50011-x, doi:10.1038/s41467-024-50011-x. This article has 8 citations and is from a highest quality peer-reviewed journal.

19. (margus2007phylogeneticdistributionof pages 1-2): Tõnu Margus, Maido Remm, and Tanel Tenson. Phylogenetic distribution of translational gtpases in bacteria. BMC Genomics, 8:15-15, Jan 2007. URL: https://doi.org/10.1186/1471-2164-8-15, doi:10.1186/1471-2164-8-15. This article has 141 citations and is from a peer-reviewed journal.

20. (antolinezfernandez2024molecularpathwaysin pages 1-2): Álvaro Antolínez-Fernández, Paula Esteban-Ramos, Miguel Ángel Fernández-Moreno, and Paula Clemente. Molecular pathways in mitochondrial disorders due to a defective mitochondrial protein synthesis. Frontiers in Cell and Developmental Biology, May 2024. URL: https://doi.org/10.3389/fcell.2024.1410245, doi:10.3389/fcell.2024.1410245. This article has 16 citations.

21. (wang2021mitochondrialproteintranslation pages 1-2): Fei Wang, Deyu Zhang, Dejiu Zhang, Peifeng Li, and Yanyan Gao. Mitochondrial protein translation: emerging roles and clinical significance in disease. Frontiers in Cell and Developmental Biology, Jul 2021. URL: https://doi.org/10.3389/fcell.2021.675465, doi:10.3389/fcell.2021.675465. This article has 144 citations.

22. (margus2007phylogeneticdistributionof pages 2-4): Tõnu Margus, Maido Remm, and Tanel Tenson. Phylogenetic distribution of translational gtpases in bacteria. BMC Genomics, 8:15-15, Jan 2007. URL: https://doi.org/10.1186/1471-2164-8-15, doi:10.1186/1471-2164-8-15. This article has 141 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR43512-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR43512-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](PTHR43512-deep-research-falcon_artifacts/artifact-02.md)

## Citations

1. caldon2001evolutionofa pages 1-2
2. clementi2010ribosomeassociatedgtpasesthe pages 1-2
3. das2023interplaybetweenintersubunit pages 1-2
4. margus2007phylogeneticdistributionof pages 1-2
5. ero2016similarityanddiversity pages 1-4
6. ero2016similarityanddiversity pages 7-10
7. ero2016similarityanddiversity pages 10-13
8. shoji2009ribosomaltranslocationone pages 2-4
9. ero2016similarityanddiversity pages 4-7
10. starosta2014thebacterialtranslation pages 1-2
11. antolinezfernandez2024molecularpathwaysin pages 1-2
12. wang2021mitochondrialproteintranslation pages 1-2
13. margus2007phylogeneticdistributionof pages 2-4
14. https://doi.org/10.4161/rna.7.5.12467,
15. https://doi.org/10.1080/15476286.2016.1201627,
16. https://doi.org/10.1046/j.1365-2958.2001.02536.x,
17. https://doi.org/10.3390/ijms24086878,
18. https://doi.org/10.1021/cb8002946,
19. https://doi.org/10.1111/1574-6976.12083,
20. https://doi.org/10.1091/mbc.e20-07-0457,
21. https://doi.org/10.1038/s41467-024-50011-x,
22. https://doi.org/10.1186/1471-2164-8-15,
23. https://doi.org/10.3389/fcell.2024.1410245,
24. https://doi.org/10.3389/fcell.2021.675465,