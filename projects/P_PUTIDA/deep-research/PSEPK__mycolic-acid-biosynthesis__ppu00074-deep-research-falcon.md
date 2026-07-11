---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-06T23:15:33.171583'
end_time: '2026-07-06T23:32:07.240185'
duration_seconds: 994.07
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: mycolic acid biosynthesis
  module_summary: No module YAML was resolved; use the pathway and taxon context.
  module_outline: No module YAML outline available.
  module_connections: No module YAML connections available.
  pathway_query: ppu00074
  pathway_id: ppu00074
  pathway_name: Mycolic acid biosynthesis
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00074 with 2 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '2'
  candidate_genes: '- PP_1183: PP_1183 | Q88NM4 | Enterobactin synthase component
    D (4''-phosphopantetheinyl transferase EntD) (Enterochelin synthase D) (primary
    bucket kegg:ppu00074)

    - fabD: PP_1913 | Q88LL7 | Malonyl CoA-acyl carrier protein transacylase (EC 2.3.1.39)
    (EC 2.3.1.39; primary bucket kegg:ppu00074)'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 21
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PSEPK__mycolic-acid-biosynthesis__ppu00074-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PSEPK__mycolic-acid-biosynthesis__ppu00074-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

mycolic acid biosynthesis in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00074
- Resolved ID: ppu00074
- Resolved name: Mycolic acid biosynthesis
- Source: KEGG

Resolved local bucket kegg:ppu00074 with 2 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 2

- PP_1183: PP_1183 | Q88NM4 | Enterobactin synthase component D (4'-phosphopantetheinyl transferase EntD) (Enterochelin synthase D) (primary bucket kegg:ppu00074)
- fabD: PP_1913 | Q88LL7 | Malonyl CoA-acyl carrier protein transacylase (EC 2.3.1.39) (EC 2.3.1.39; primary bucket kegg:ppu00074)

## Generic Module Context

### Working Scope

No module YAML was resolved; use the pathway and taxon context.

### Provisional Biological Outline

No module YAML outline available.

### Known Relationships Among Steps

No module YAML connections available.

## Assignment

Write a species-aware review of this module/pathway in the target organism. The
goal is not a generic pathway essay; the goal is to support manual module
satisfiability and gene annotation curation.

Treat the candidate gene list as a starting point, not ground truth. Use the
literature and authoritative resources to decide whether each expected pathway
step is present, absent, ambiguous, replaced by a lineage-specific alternative,
or represented by a likely over-propagated annotation.

Prioritize direct evidence from the target species/strain. When using evidence
from related organisms, state the organism and explain whether transfer to the
target taxon is strong, weak, or uncertain. Distinguish *Pseudomonas putida*
KT2440 evidence from broader *Pseudomonas* or generic bacterial evidence.

## Questions To Address

1. **Pathway boundaries**
   - What exact biochemical or cellular process is included?
   - Which neighboring pathways or broad overview maps should be kept separate?
   - Are there alternate names or database-specific definitions for this pathway?

2. **Satisfiability in the target taxon**
   - Which expected steps are encoded by candidate genes?
   - Which steps are missing from the metadata but likely present under a
     different gene name, paralog, or enzyme family?
   - Which steps are probably not expected in this organism?

3. **Candidate gene assessment**
   - For each high-confidence gene, summarize the likely role, evidence type,
     and any curation-relevant caveats.
   - Identify paralog ambiguity, broad EC/GO mappings, and likely annotation
     over-propagation.
   - Note genes that should be promoted to full `fetch-gene` review.

4. **Module implications**
   - What module steps should be marked covered, candidate_uncertain, gap,
     not_expected_in_target_taxon, or module_needs_revision?
   - Are existing generic module boundaries wrong for this organism?
   - Are new module documents or GO term requests likely needed?

5. **Evidence and open questions**
   - Which conclusions are supported by direct experiments?
   - Which are inferred from homology, pathway databases, or neighboring genes?
   - What experiments or expert questions would resolve the important gaps?

## Output Format

Use concise review sections:

1. Executive summary
2. Target-organism pathway definition
3. Expected step model
4. Candidate genes and evidence
5. Gaps, ambiguities, and likely over-annotations
6. Module and GO-curation recommendations
7. Genes to promote to full review
8. Key references

Include citations for major claims, preferably PMIDs or DOIs. Be explicit about
uncertainty, species transfer, and whether evidence is direct for the target
organism.

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

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

mycolic acid biosynthesis in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00074
- Resolved ID: ppu00074
- Resolved name: Mycolic acid biosynthesis
- Source: KEGG

Resolved local bucket kegg:ppu00074 with 2 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 2

- PP_1183: PP_1183 | Q88NM4 | Enterobactin synthase component D (4'-phosphopantetheinyl transferase EntD) (Enterochelin synthase D) (primary bucket kegg:ppu00074)
- fabD: PP_1913 | Q88LL7 | Malonyl CoA-acyl carrier protein transacylase (EC 2.3.1.39) (EC 2.3.1.39; primary bucket kegg:ppu00074)

## Generic Module Context

### Working Scope

No module YAML was resolved; use the pathway and taxon context.

### Provisional Biological Outline

No module YAML outline available.

### Known Relationships Among Steps

No module YAML connections available.

## Assignment

Write a species-aware review of this module/pathway in the target organism. The
goal is not a generic pathway essay; the goal is to support manual module
satisfiability and gene annotation curation.

Treat the candidate gene list as a starting point, not ground truth. Use the
literature and authoritative resources to decide whether each expected pathway
step is present, absent, ambiguous, replaced by a lineage-specific alternative,
or represented by a likely over-propagated annotation.

Prioritize direct evidence from the target species/strain. When using evidence
from related organisms, state the organism and explain whether transfer to the
target taxon is strong, weak, or uncertain. Distinguish *Pseudomonas putida*
KT2440 evidence from broader *Pseudomonas* or generic bacterial evidence.

## Questions To Address

1. **Pathway boundaries**
   - What exact biochemical or cellular process is included?
   - Which neighboring pathways or broad overview maps should be kept separate?
   - Are there alternate names or database-specific definitions for this pathway?

2. **Satisfiability in the target taxon**
   - Which expected steps are encoded by candidate genes?
   - Which steps are missing from the metadata but likely present under a
     different gene name, paralog, or enzyme family?
   - Which steps are probably not expected in this organism?

3. **Candidate gene assessment**
   - For each high-confidence gene, summarize the likely role, evidence type,
     and any curation-relevant caveats.
   - Identify paralog ambiguity, broad EC/GO mappings, and likely annotation
     over-propagation.
   - Note genes that should be promoted to full `fetch-gene` review.

4. **Module implications**
   - What module steps should be marked covered, candidate_uncertain, gap,
     not_expected_in_target_taxon, or module_needs_revision?
   - Are existing generic module boundaries wrong for this organism?
   - Are new module documents or GO term requests likely needed?

5. **Evidence and open questions**
   - Which conclusions are supported by direct experiments?
   - Which are inferred from homology, pathway databases, or neighboring genes?
   - What experiments or expert questions would resolve the important gaps?

## Output Format

Use concise review sections:

1. Executive summary
2. Target-organism pathway definition
3. Expected step model
4. Candidate genes and evidence
5. Gaps, ambiguities, and likely over-annotations
6. Module and GO-curation recommendations
7. Genes to promote to full review
8. Key references

Include citations for major claims, preferably PMIDs or DOIs. Be explicit about
uncertainty, species transfer, and whether evidence is direct for the target
organism.

# Mycolic Acid Biosynthesis (KEGG ppu00074) in *Pseudomonas putida* KT2440: Species-Aware Pathway Review

---

## 1. Executive Summary

**The KEGG pathway ppu00074 ("Mycolic acid biosynthesis") is not a biologically meaningful pathway in *Pseudomonas putida* KT2440 and should be treated as an annotation artifact.** Mycolic acids are α-alkyl, β-hydroxy long-chain fatty acids produced exclusively by members of the order Corynebacteriales (phylum Actinobacteria), including *Mycobacterium*, *Corynebacterium*, *Nocardia*, *Rhodococcus*, *Gordonia*, *Tsukamurella*, *Dietzia*, and *Segniliparus* (marrakchi2014mycolicacidsstructures pages 1-2, marrakchi2014mycolicacidsstructures pages 2-3). *P. putida* KT2440 is a Gram-negative Gammaproteobacterium (NCBI taxon 160488) with a standard Gram-negative cell envelope comprising an inner membrane, thin peptidoglycan layer, and an outer membrane containing lipopolysaccharide (LPS)—fundamentally different from the mycolyl-arabinogalactan-peptidoglycan (mAGP) complex of mycolic acid-producing organisms (dover2004comparativecellwall pages 2-4). *P. putida* KT2440 does not produce mycolic acids, and there is no biological, biochemical, or genomic evidence to suggest otherwise.

The two candidate genes (PP_1183/EntD and PP_1913/FabD) are mapped to this pathway solely because they share EC numbers or protein family membership with enzymes that participate in general fatty acid biosynthesis steps also utilized by mycobacteria upstream of mycolic acid-specific reactions. Both genes have well-characterized, non-mycolic-acid functions in *P. putida*: FabD operates in type II fatty acid synthesis (FAS-II) and EntD is a phosphopantetheinyl transferase for NRPS-based siderophore biosynthesis. **All module steps should be marked `not_expected_in_target_taxon`, and the pathway should be flagged for removal from the *P. putida* KT2440 KEGG organism-specific pathway listing or clearly annotated as an over-propagation artifact.**

---

## 2. Target-Organism Pathway Definition

### 2.1 What is Mycolic Acid Biosynthesis?

Mycolic acids are very long-chain (C60–C90 in mycobacteria, C22–C36 in corynebacteria) α-alkyl, β-hydroxy fatty acids that constitute a distinctive lipid component of the cell envelope of Corynebacteriales (marrakchi2014mycolicacidsstructures pages 2-3, dover2004comparativecellwall pages 2-4). Their biosynthesis requires a complex, multi-step enzymatic pathway that includes:

1. **FAS-I**: A eukaryotic-like multifunctional fatty acid synthase producing C16–C18 and C24–C26 acyl-CoA precursors (the α-branch) (marrakchi2014mycolicacidsstructures pages 2-3, dover2004comparativecellwall pages 14-15).
2. **FAS-II**: A dissociated (type II) fatty acid synthase system that elongates FAS-I products to C48–C62 meromycolate chains via iterative two-carbon additions using specialized enzymes KasA, KasB, MabA, InhA, HadAB/HadBC, and MtFabD (marrakchi2014mycolicacidsstructures pages 8-9, marrakchi2014mycolicacidsstructures pages 4-6).
3. **Meromycolate modification**: SAM-dependent methyltransferases (CmaA1, CmaA2, PcaA, MmaA2, MmaA4/Hma) introduce cyclopropane rings, methyl branches, methoxy groups, and keto groups (marrakchi2014mycolicacidsstructures pages 7-8, dover2004comparativecellwall pages 15-16).
4. **Claisen condensation**: The polyketide synthase Pks13 catalyzes the final condensation of the activated meromycolate chain (via FadD32) with the carboxylated α-branch (via AccD4) to form the characteristic mycolic acid β-ketoester (marrakchi2014mycolicacidsstructures pages 8-9).
5. **Post-condensation processing**: Reduction by CmrA and transfer to cell wall arabinogalactan or trehalose carriers by the Ag85 complex, with transport via MmpL3 (dover2004comparativecellwall pages 16-18).

### 2.2 Pathway Boundaries and Neighboring Pathways

The KEGG map00074 encompasses both upstream fatty acid synthesis steps shared with general metabolism (map00061, Fatty acid biosynthesis) and downstream mycolic acid-specific steps. The critical distinction is that FabD and PPTases participate in **general fatty acid biosynthesis** (KEGG map00061) and **secondary metabolism**, respectively, not in mycolic acid-specific chemistry. For *P. putida* KT2440, these genes should be mapped exclusively to:
- **map00061** (Fatty acid biosynthesis) for FabD
- **map01053** (Biosynthesis of siderophore group nonribosomal peptides) or related NRPS pathways for EntD

### 2.3 Alternate Names

KEGG pathway 00074 is also referenced as "Mycolic acid biosynthesis" in MetaCyc (as part of superpathway of mycolate biosynthesis) and BRENDA. It is sometimes called "mycolate biosynthesis" or "cell wall mycolic acid pathway."

---

## 3. Expected Step Model

The following table maps all canonical mycolic acid biosynthesis steps against the *P. putida* KT2440 genome and establishes that essentially every mycolic acid-specific step is absent:

| Pathway Step | Key Enzyme(s) in Mycobacteria | EC Number(s) | Present in *P. putida* KT2440? | Status |
|---|---|---|---|---|
| Malonyl-CoA formation | AccABCD / acyl-CoA carboxylase components | EC 6.4.1.2, EC 6.4.1.3 | Yes, but as general fatty acid biosynthesis precursor supply rather than mycolate-specific metabolism (marrakchi2014mycolicacidsstructures pages 3-4, mezzina2021engineeringnativeand pages 13-16) | covered_for_general_FAS_only; not_expected_in_target_taxon for mycolic acid pathway |
| Malonyl-CoA:ACP transacylase | MtFabD / FabD | EC 2.3.1.39 | Yes; PP_1913/fabD is a general FAS-II malonyl-CoA:ACP transacylase, not evidence of mycolate synthesis (mezzina2021engineeringnativeand pages 13-16, marrakchi2014mycolicacidsstructures pages 8-9, marrakchi2014mycolicacidsstructures pages 4-6) | covered_for_general_FAS_only; not_expected_in_target_taxon for mycolic acid pathway |
| FAS-I de novo synthesis | Fas | EC 2.3.1.85 | No; *P. putida* uses discrete FAS-II enzymes rather than mycobacterial FAS-I (marrakchi2014mycolicacidsstructures pages 2-3, mezzina2021engineeringnativeand pages 13-16) | not_expected_in_target_taxon |
| FAS-II meromycolate elongation core | KasA, KasB, MabA, InhA, HadABC | EC 2.3.1.41; EC 1.1.1.100; EC 1.3.1.9; EC 4.2.1.- | No orthologous mycolate-system core detected; *P. putida* has non-orthologous FabB/FabF/FabA/FabZ for general FAS-II, not KasA/KasB meromycolate elongation (marrakchi2014mycolicacidsstructures pages 8-9, marrakchi2014mycolicacidsstructures pages 4-6, mezzina2021engineeringnativeand pages 13-16, guo2024diversityinfatty pages 2-4) | not_expected_in_target_taxon |
| FAS-I to FAS-II bridge | mtFabH | EC 2.3.1.180 | No mycobacterial-type bridge enzyme expected; *P. putida* initiation differs and can rely on FabB/FabH-family FAS-II initiation only (marrakchi2014mycolicacidsstructures pages 8-9, dover2004comparativecellwall pages 14-15, guo2024diversityinfatty pages 2-4) | not_expected_in_target_taxon |
| Meromycolate chain modification - cyclopropanation | CmaA1, CmaA2, PcaA, MmaA2 | EC 2.1.1.- | No; these are mycolic-acid modification enzymes of Corynebacteriales (marrakchi2014mycolicacidsstructures pages 7-8, dover2004comparativecellwall pages 15-16) | not_expected_in_target_taxon |
| Meromycolate modification - methoxylation/keto groups | MmaA4 / Hma | EC 2.1.1.- / oxygenation-associated | No; no mycolate oxygenation machinery expected in *P. putida* (marrakchi2014mycolicacidsstructures pages 7-8) | not_expected_in_target_taxon |
| Meromycolate activation | FadD32 | EC 6.2.1.- | No; required for activation of meromycolate prior to condensation in mycobacteria (marrakchi2014mycolicacidsstructures pages 8-9) | not_expected_in_target_taxon |
| Alpha-branch carboxylation | AccD4-containing acyl-CoA carboxylase | EC 6.4.1.- | No mycolate-specific AccD4 function expected; generic carboxylases in *P. putida* do not imply this step (marrakchi2014mycolicacidsstructures pages 8-9, marrakchi2014mycolicacidsstructures pages 3-4) | not_expected_in_target_taxon |
| Claisen condensation | Pks13 | EC 2.3.1.- | No; hallmark mycolic acid condensase absent and not expected outside Corynebacteriales (marrakchi2014mycolicacidsstructures pages 8-9, marrakchi2014mycolicacidsstructures pages 7-8) | not_expected_in_target_taxon |
| Mycolate reduction | CmrA | EC 1.1.1.- | No evidence in *P. putida*; downstream of Pks13 and therefore not expected when the pathway core is absent (marrakchi2014mycolicacidsstructures pages 8-9) | not_expected_in_target_taxon |
| Mycolate transfer to cell wall | Ag85 complex, MmpL3 | EC 2.3.1.- / transporter | No; *P. putida* has a Gram-negative outer membrane with LPS rather than a mycolyl-arabinogalactan cell wall (dover2004comparativecellwall pages 2-4, dover2004comparativecellwall pages 14-15, mezzina2021engineeringnativeand pages 13-16) | not_expected_in_target_taxon |
| PPTase activation of Pks13 | PptT | EC 2.7.8.- | No mycolate-specific PPTase expected; PP_1183/EntD is an NRPS/siderophore PPTase and does not support mycolate synthesis (kim2018distributionandfunctional pages 2-3) | not_expected_in_target_taxon |


*Table: This table maps canonical mycolic acid biosynthesis steps from mycobacteria onto *Pseudomonas putida* KT2440. It shows that only generic fatty acid precursor steps are present, while all mycolic acid-specific steps are absent and should be treated as not expected in this taxon.*

In summary, only two generic upstream steps (malonyl-CoA formation and malonyl-CoA:ACP transacylation) have homologs in *P. putida*, but these function exclusively in general fatty acid biosynthesis and are not evidence of mycolic acid pathway activity (mezzina2021engineeringnativeand pages 13-16).

---

## 4. Candidate Genes and Evidence

The two candidate genes mapped to ppu00074 are assessed below:

| Gene/Locus Tag | UniProt | Annotated Function | True Biological Role in *P. putida* KT2440 | Evidence Type | Mycolic Acid Relevance | Assessment/Recommendation |
|---|---|---|---|---|---|---|
| PP_1183 (*entD*) | Q88NM4 | Enterobactin synthase component D; 4'-phosphopantetheinyl transferase | Sfp/EntD-type PPTase for activating carrier proteins in NRPS-dependent siderophore biosynthesis; not part of fatty acid synthesis and no evidence for mycolic-acid-related chemistry in *P. putida* KT2440 (kim2018distributionandfunctional pages 2-3) | Functional inference from PPTase family specificity and siderophore-associated EntD role; pathway-context inference for *Pseudomonas* secondary metabolism (kim2018distributionandfunctional pages 2-3) | None in target taxon; *P. putida* lacks mycolic acid pathway and mycolate-specific acceptor enzymes such as Pks13/PptT (marrakchi2014mycolicacidsstructures pages 1-2, marrakchi2014mycolicacidsstructures pages 8-9) | Likely over-propagated KEGG assignment; keep as PPTase/siderophore-related annotation, not as mycolic acid biosynthesis gene |
| PP_1913 (*fabD*) | Q88LL7 | Malonyl-CoA-acyl carrier protein transacylase (EC 2.3.1.39) | Core FAS-II enzyme that converts malonyl-CoA to malonyl-ACP for general fatty acid biosynthesis in *P. putida* KT2440 (mezzina2021engineeringnativeand pages 13-16) | Strong pathway inference from reviewed *P. putida* FAS-II biochemistry; shared enzymatic role with bacterial fatty acid synthesis broadly (mezzina2021engineeringnativeand pages 13-16) | Indirect/shared only: mycobacteria also use FabD/MtFabD in FAS-II supplying meromycolate elongation, but *P. putida* lacks downstream mycolate-specific machinery and does not produce mycolic acids (marrakchi2014mycolicacidsstructures pages 8-9, marrakchi2014mycolicacidsstructures pages 4-6, marrakchi2014mycolicacidsstructures pages 1-2) | Valid fatty-acid-biosynthesis annotation, but mycolic-acid mapping is an over-propagated/shared-EC artifact; do not treat as evidence that ppu00074 is satisfiable in the target taxon |


*Table: This table evaluates the two KEGG-mapped candidate genes for ppu00074 in *P. putida* KT2440 and shows that both are better explained by general fatty acid or siderophore metabolism, not mycolic acid biosynthesis. It is useful for deciding that the pathway assignment is likely a database over-propagation artifact.*

### 4.1 PP_1913 / FabD (Q88LL7) — Malonyl-CoA:ACP Transacylase (EC 2.3.1.39)

**True function in *P. putida* KT2440:** FabD catalyzes the transfer of the malonyl group from malonyl-CoA to the acyl carrier protein (ACP), producing malonyl-ACP, which is the essential substrate for all FAS-II condensation reactions (mezzina2021engineeringnativeand pages 13-16). This is a core, essential enzyme for *de novo* fatty acid biosynthesis in virtually all bacteria. In *P. putida* KT2440, FabD feeds malonyl-ACP into condensation reactions catalyzed by FabB (the primary initiation enzyme in Pseudomonads) and FabF for chain elongation (mezzina2021engineeringnativeand pages 13-16, guo2024diversityinfatty pages 2-4, guo2024diversityinfatty pages 1-2). The fatty acid products are incorporated into phospholipids, LPS, rhamnolipids (when heterologously expressed), and polyhydroxyalkanoates (mezzina2021engineeringnativeand pages 13-16).

**Why it appears in ppu00074:** In mycobacteria, the orthologous enzyme MtFabD also provides malonyl-ACP to the FAS-II system, but in that organism FAS-II feeds into meromycolate chain elongation (marrakchi2014mycolicacidsstructures pages 8-9, marrakchi2014mycolicacidsstructures pages 4-6). KEGG maps FabD to map00074 because it shares the same EC number (2.3.1.39), but the downstream pathway context is entirely different in *P. putida*.

**Evidence type:** Strong — direct experimental evidence from *P. putida* fatty acid biosynthesis studies (mezzina2021engineeringnativeand pages 13-16, guo2024diversityinfatty pages 2-4).

**Assessment:** Valid fatty acid biosynthesis gene. The mycolic acid pathway mapping is an over-propagation artifact based on shared EC number.

### 4.2 PP_1183 / EntD (Q88NM4) — 4'-Phosphopantetheinyl Transferase

**True function in *P. putida* KT2440:** PP_1183 encodes an EntD-family phosphopantetheinyl transferase (PPTase). EntD-type PPTases belong to the Sfp/EntD superfamily and activate carrier protein domains in nonribosomal peptide synthetases (NRPSs) by transferring a phosphopantetheine moiety from coenzyme A to a conserved serine residue (kim2018distributionandfunctional pages 2-3). In *E. coli*, EntD specifically activates EntF for enterobactin (siderophore) biosynthesis. *P. putida* KT2440 does not synthesize enterobactin but does produce pyoverdine and other siderophores; PP_1183 is annotated as an EntD homolog and is most likely involved in NRPS-dependent secondary metabolite biosynthesis (kim2018distributionandfunctional pages 2-3).

**Why it appears in ppu00074:** In mycobacteria, a related PPTase (PptT) activates the type I polyketide synthase Pks13, which catalyzes the final Claisen condensation in mycolic acid biosynthesis (marrakchi2014mycolicacidsstructures pages 8-9). KEGG maps PPTases to map00074 based on shared protein family (PF01648), but PP_1183/EntD has no functional relationship to Pks13 or mycolic acid biosynthesis.

**Evidence type:** Moderate — functional assignment is inferred from protein family classification and homology to *E. coli* EntD (kim2018distributionandfunctional pages 2-3). Direct biochemical characterization of PP_1183 in *P. putida* KT2440 has not been identified in the literature.

**Assessment:** Likely valid siderophore/NRPS-associated PPTase. The mycolic acid pathway mapping is a clear over-propagation artifact.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 Over-Propagation Assessment

The assignment of ppu00074 to *P. putida* KT2440 is a textbook example of **annotation over-propagation through shared EC numbers and protein family membership**. The KEGG automated orthology assignment system maps genes to pathway maps based on KO (KEGG Orthology) assignments, which in this case capture enzymes that participate in upstream fatty acid biosynthesis shared between general bacterial metabolism and the mycolic acid pathway of Corynebacteriales. Because the KEGG pathway map00074 includes early FAS-II steps as part of the mycolic acid biosynthesis route, any organism with FabD and/or PPTases may be spuriously mapped to this pathway.

### 5.2 Taxonomic Mismatch

Mycolic acids have never been detected in any Pseudomonas species or any member of the Proteobacteria phylum. They are restricted to the order Corynebacteriales within the phylum Actinobacteria, where they serve as essential structural components of the mycolyl-arabinogalactan-peptidoglycan (mAGP) cell wall complex (marrakchi2014mycolicacidsstructures pages 1-2, dover2004comparativecellwall pages 2-4, marrakchi2014mycolicacidsstructures pages 2-3). *P. putida* KT2440 has a fundamentally different cell envelope architecture: a Gram-negative outer membrane with LPS, which is structurally and biosynthetically unrelated to the mycolic acid-based permeability barrier of Corynebacteriales.

### 5.3 Missing Mycolic Acid-Specific Genes

The *P. putida* KT2440 genome (6.18 Mb) lacks all of the following mycolic acid-specific genes/enzyme families:
- **FAS-I** (*fas*): Multifunctional fatty acid synthase producing C24–C26 α-branch precursors
- **KasA/KasB**: Specialized β-ketoacyl-ACP synthases for meromycolate elongation
- **HadAB/HadBC**: β-Hydroxyacyl-ACP dehydratases specific to meromycolate synthesis
- **MtFabH**: FAS-I → FAS-II bridging enzyme
- **FadD32**: Acyl-AMP ligase for meromycolate activation
- **AccD4**: Acyl-CoA carboxylase subunit for α-branch carboxylation
- **Pks13**: Polyketide synthase condensase for the Claisen condensation
- **PptT**: PPTase activating Pks13
- **CmrA**: Mycolate ketoreductase
- **CmaA1/CmaA2/PcaA/MmaA2/MmaA4**: SAM-dependent methyltransferases for meromycolate modification
- **Ag85 complex**: Mycolyltransferases
- **MmpL3**: Trehalose monomycolate transporter

### 5.4 What *P. putida* KT2440 Actually Has

*P. putida* KT2440 possesses a well-characterized canonical bacterial FAS-II system for general fatty acid biosynthesis, including AccABCD, FabD, FabH1/FabH2 (though non-essential due to FabB initiation), FabB, FabF, FabG, FabA, FabZ, and FabI (mezzina2021engineeringnativeand pages 13-16, guo2024diversityinfatty pages 2-4, guo2024diversityinfatty pages 1-2, guo2024diversityinfatty pages 6-8). Notably, *P. putida* exhibits a distinctive FAS initiation mechanism: FabB (β-ketoacyl-ACP synthase I) serves as the primary initiation enzyme through malonyl-ACP decarboxylation, unlike *E. coli* where FabH (KAS III) is essential for initiation (guo2024diversityinfatty pages 2-4, guo2024diversityinfatty pages 1-2, guo2024diversityinfatty pages 6-8, guo2024diversityinfatty pages 4-6). This is a feature unique to Pseudomonads and unrelated to mycolic acid biosynthesis.

---

## 6. Module and GO-Curation Recommendations

### 6.1 Module Step Status Recommendations

| Step | Recommended Status |
|---|---|
| All mycolic acid-specific steps (FAS-I, KasA/KasB elongation, meromycolate modification, FadD32, AccD4, Pks13, CmrA, Ag85, MmpL3, PptT) | `not_expected_in_target_taxon` |
| FabD (malonyl-CoA:ACP transacylase) | `not_expected_in_target_taxon` for mycolic acid context; belongs in FAS-II/map00061 |
| EntD (PPTase) | `not_expected_in_target_taxon` for mycolic acid context; belongs in siderophore/NRPS pathways |

### 6.2 Pathway-Level Recommendation

**The entire KEGG ppu00074 pathway should be marked as `not_expected_in_target_taxon` for *P. putida* KT2440.** This is not a case of partial pathway presence or gap-filling—the organism fundamentally does not perform this biochemistry. The pathway assignment arises from automated KO mapping of shared upstream enzymes and should be suppressed or flagged in curated databases.

### 6.3 GO Term Recommendations

- PP_1913/FabD should retain GO annotations for fatty acid biosynthetic process (GO:0006633) and malonyl-CoA:ACP transacylase activity (GO:0004314). Any GO annotations linking it to mycolic acid biosynthetic process should be removed.
- PP_1183/EntD should retain GO annotations for 4'-phosphopantetheinyl transferase activity (GO:0008897) and siderophore biosynthetic process (GO:0019290). It should not carry mycolic acid-related GO terms.

### 6.4 Module Document Needs

No new module document is needed for mycolic acid biosynthesis in *P. putida*. If a generic "mycolic acid biosynthesis" module exists, it should include a taxonomic scope restriction to Corynebacteriales (or more broadly, the mycolata taxon within Actinobacteria) to prevent spurious assignments to Proteobacteria and other phyla.

---

## 7. Genes to Promote to Full Review

**Neither candidate gene requires promotion to a full fetch-gene review for the purpose of mycolic acid biosynthesis,** as this pathway is not operative in the target organism. However:

- **PP_1913/FabD** merits inclusion in any review of the fatty acid biosynthesis module (map00061) for *P. putida* KT2440, where it plays an essential and well-characterized role (mezzina2021engineeringnativeand pages 13-16).
- **PP_1183/EntD** could be promoted for review in the context of siderophore/NRPS biosynthesis pathways in *P. putida* KT2440, particularly to clarify its specific substrate(s) among the multiple NRPS systems in this organism (kim2018distributionandfunctional pages 2-3). Its precise biochemical role in *P. putida* (as opposed to *E. coli*) has not been directly characterized experimentally.

---

## 8. Key References

1. **Marrakchi H, Lanéelle MA, Daffé M.** Mycolic acids: structures, biosynthesis, and beyond. *Chemistry & Biology.* 2014;21(1):67–85. doi:10.1016/j.chembiol.2013.11.011. — Comprehensive review of mycolic acid structures and biosynthesis; establishes taxonomic restriction to Corynebacteriales (marrakchi2014mycolicacidsstructures pages 1-2, marrakchi2014mycolicacidsstructures pages 2-3, marrakchi2014mycolicacidsstructures pages 8-9, marrakchi2014mycolicacidsstructures pages 4-6, marrakchi2014mycolicacidsstructures pages 7-8, marrakchi2014mycolicacidsstructures pages 3-4).

2. **Dover LG, Cerdeño-Tárraga AM, Pallen MJ, Parkhill J, Besra GS.** Comparative cell wall core biosynthesis in the mycolated pathogens, *Mycobacterium tuberculosis* and *Corynebacterium diphtheriae*. *FEMS Microbiology Reviews.* 2004;28(2):225–250. doi:10.1016/j.femsre.2003.10.001. — Defines mAGP complex architecture and mycolic acid biosynthesis enzymes in mycolated organisms (dover2004comparativecellwall pages 15-16, dover2004comparativecellwall pages 2-4, dover2004comparativecellwall pages 14-15, dover2004comparativecellwall pages 16-18).

3. **Mezzina MP, Manoli MT, Prieto MA, Nikel PI.** Engineering native and synthetic pathways in *Pseudomonas putida* for the production of tailored polyhydroxyalkanoates. *Biotechnology Journal.* 2021;16(3):e2000165. doi:10.1002/biot.202000165. — Describes FAS-II pathway in *P. putida* including FabD function (mezzina2021engineeringnativeand pages 13-16).

4. **Guo Q, Zhong C, Dong H, Cronan JE, Wang H.** Diversity in fatty acid elongation enzymes: The FabB long-chain β-ketoacyl-ACP synthase I initiates fatty acid synthesis in *Pseudomonas putida* F1. *Journal of Biological Chemistry.* 2024;300(2):105600. doi:10.1016/j.jbc.2023.105600. — Demonstrates unique FabB-mediated FAS initiation in *P. putida* (guo2024diversityinfatty pages 2-4, guo2024diversityinfatty pages 1-2, guo2024diversityinfatty pages 6-8, guo2024diversityinfatty pages 4-6).

5. **Kim JH, Komatsu M, Shin-ya K, Omura S, Ikeda H.** Distribution and functional analysis of the phosphopantetheinyl transferase superfamily in Actinomycetales microorganisms. *PNAS.* 2018;115(26):6828–6833. doi:10.1073/pnas.1800715115. — Classifies PPTase families including EntD and establishes its NRPS/siderophore role (kim2018distributionandfunctional pages 2-3).

6. **Valencia LE, Incha MR, Schmidt M, et al.** Engineering *Pseudomonas putida* KT2440 for chain length tailored free fatty acid and oleochemical production. *Communications Biology.* 2022;5:1–13. doi:10.1038/s42003-022-04336-2. — Demonstrates fatty acid metabolism engineering in *P. putida* KT2440 without any mycolic acid involvement.

7. **North EJ, Jackson M, Lee RE.** New approaches to target the mycolic acid biosynthesis pathway for the development of tuberculosis therapeutics. *Current Pharmaceutical Design.* 2014;20(27):4357–4378. doi:10.2174/1381612819666131118203641. — Comprehensive overview of mycolic acid-specific enzymes as drug targets.

---

## Summary of Conclusions

| Question | Conclusion | Confidence |
|---|---|---|
| Does *P. putida* KT2440 produce mycolic acids? | **No** — phylogenetically impossible | Very high |
| Is KEGG ppu00074 biologically meaningful? | **No** — artifact of shared upstream EC numbers | Very high |
| Is PP_1913/FabD involved in mycolic acid biosynthesis? | **No** — general FAS-II enzyme only | High |
| Is PP_1183/EntD involved in mycolic acid biosynthesis? | **No** — NRPS/siderophore PPTase | High |
| Should any steps be marked as covered? | **No** — entire pathway is `not_expected_in_target_taxon` | Very high |
| Are there hidden mycolic acid genes? | **No** — no lineage-specific alternatives exist in Proteobacteria | Very high |

This pathway assignment represents a well-understood class of database annotation artifact where automated orthology mapping propagates pathway membership based on shared upstream enzymatic steps without accounting for the phylogenetic restriction of the pathway endpoint (mycolic acid production) to a distant taxonomic lineage.

References

1. (marrakchi2014mycolicacidsstructures pages 1-2): Hedia Marrakchi, Marie-Antoinette Lanéelle, and Mamadou Daffé. Mycolic acids: structures, biosynthesis, and beyond. Chemistry & biology, 21 1:67-85, Jan 2014. URL: https://doi.org/10.1016/j.chembiol.2013.11.011, doi:10.1016/j.chembiol.2013.11.011. This article has 848 citations.

2. (marrakchi2014mycolicacidsstructures pages 2-3): Hedia Marrakchi, Marie-Antoinette Lanéelle, and Mamadou Daffé. Mycolic acids: structures, biosynthesis, and beyond. Chemistry & biology, 21 1:67-85, Jan 2014. URL: https://doi.org/10.1016/j.chembiol.2013.11.011, doi:10.1016/j.chembiol.2013.11.011. This article has 848 citations.

3. (dover2004comparativecellwall pages 2-4): Lynn G. Dover, Ana M. Cerdeño-Tárraga, Mark J. Pallen, Julian Parkhill, and Gurdyal S. Besra. Comparative cell wall core biosynthesis in the mycolated pathogens, mycobacterium tuberculosis and corynebacterium diphtheriae. FEMS microbiology reviews, 28 2:225-50, May 2004. URL: https://doi.org/10.1016/j.femsre.2003.10.001, doi:10.1016/j.femsre.2003.10.001. This article has 170 citations and is from a domain leading peer-reviewed journal.

4. (dover2004comparativecellwall pages 14-15): Lynn G. Dover, Ana M. Cerdeño-Tárraga, Mark J. Pallen, Julian Parkhill, and Gurdyal S. Besra. Comparative cell wall core biosynthesis in the mycolated pathogens, mycobacterium tuberculosis and corynebacterium diphtheriae. FEMS microbiology reviews, 28 2:225-50, May 2004. URL: https://doi.org/10.1016/j.femsre.2003.10.001, doi:10.1016/j.femsre.2003.10.001. This article has 170 citations and is from a domain leading peer-reviewed journal.

5. (marrakchi2014mycolicacidsstructures pages 8-9): Hedia Marrakchi, Marie-Antoinette Lanéelle, and Mamadou Daffé. Mycolic acids: structures, biosynthesis, and beyond. Chemistry & biology, 21 1:67-85, Jan 2014. URL: https://doi.org/10.1016/j.chembiol.2013.11.011, doi:10.1016/j.chembiol.2013.11.011. This article has 848 citations.

6. (marrakchi2014mycolicacidsstructures pages 4-6): Hedia Marrakchi, Marie-Antoinette Lanéelle, and Mamadou Daffé. Mycolic acids: structures, biosynthesis, and beyond. Chemistry & biology, 21 1:67-85, Jan 2014. URL: https://doi.org/10.1016/j.chembiol.2013.11.011, doi:10.1016/j.chembiol.2013.11.011. This article has 848 citations.

7. (marrakchi2014mycolicacidsstructures pages 7-8): Hedia Marrakchi, Marie-Antoinette Lanéelle, and Mamadou Daffé. Mycolic acids: structures, biosynthesis, and beyond. Chemistry & biology, 21 1:67-85, Jan 2014. URL: https://doi.org/10.1016/j.chembiol.2013.11.011, doi:10.1016/j.chembiol.2013.11.011. This article has 848 citations.

8. (dover2004comparativecellwall pages 15-16): Lynn G. Dover, Ana M. Cerdeño-Tárraga, Mark J. Pallen, Julian Parkhill, and Gurdyal S. Besra. Comparative cell wall core biosynthesis in the mycolated pathogens, mycobacterium tuberculosis and corynebacterium diphtheriae. FEMS microbiology reviews, 28 2:225-50, May 2004. URL: https://doi.org/10.1016/j.femsre.2003.10.001, doi:10.1016/j.femsre.2003.10.001. This article has 170 citations and is from a domain leading peer-reviewed journal.

9. (dover2004comparativecellwall pages 16-18): Lynn G. Dover, Ana M. Cerdeño-Tárraga, Mark J. Pallen, Julian Parkhill, and Gurdyal S. Besra. Comparative cell wall core biosynthesis in the mycolated pathogens, mycobacterium tuberculosis and corynebacterium diphtheriae. FEMS microbiology reviews, 28 2:225-50, May 2004. URL: https://doi.org/10.1016/j.femsre.2003.10.001, doi:10.1016/j.femsre.2003.10.001. This article has 170 citations and is from a domain leading peer-reviewed journal.

10. (marrakchi2014mycolicacidsstructures pages 3-4): Hedia Marrakchi, Marie-Antoinette Lanéelle, and Mamadou Daffé. Mycolic acids: structures, biosynthesis, and beyond. Chemistry & biology, 21 1:67-85, Jan 2014. URL: https://doi.org/10.1016/j.chembiol.2013.11.011, doi:10.1016/j.chembiol.2013.11.011. This article has 848 citations.

11. (mezzina2021engineeringnativeand pages 13-16): Mariela P. Mezzina, María Tsampika Manoli, M. Auxiliadora Prieto, and Pablo I. Nikel. Engineering native and synthetic pathways in <i>pseudomonas putida</i> for the production of tailored polyhydroxyalkanoates. Biotechnology Journal, Nov 2021. URL: https://doi.org/10.1002/biot.202000165, doi:10.1002/biot.202000165. This article has 150 citations and is from a peer-reviewed journal.

12. (guo2024diversityinfatty pages 2-4): Qiaoqiao Guo, Canyao Zhong, Huijuan Dong, John E. Cronan, and Haihong Wang. Diversity in fatty acid elongation enzymes: the fabb long-chain β-ketoacyl-acp synthase i initiates fatty acid synthesis in pseudomonas putida f1. The Journal of Biological Chemistry, 300:105600, Feb 2024. URL: https://doi.org/10.1016/j.jbc.2023.105600, doi:10.1016/j.jbc.2023.105600. This article has 10 citations.

13. (kim2018distributionandfunctional pages 2-3): Jeong Ho Kim, Mamoru Komatsu, Kazuo Shin-ya, Satoshi Omura, and Haruo Ikeda. Distribution and functional analysis of the phosphopantetheinyl transferase superfamily in actinomycetales microorganisms. Proceedings of the National Academy of Sciences of the United States of America, 115:6828-6833, Jun 2018. URL: https://doi.org/10.1073/pnas.1800715115, doi:10.1073/pnas.1800715115. This article has 59 citations and is from a highest quality peer-reviewed journal.

14. (guo2024diversityinfatty pages 1-2): Qiaoqiao Guo, Canyao Zhong, Huijuan Dong, John E. Cronan, and Haihong Wang. Diversity in fatty acid elongation enzymes: the fabb long-chain β-ketoacyl-acp synthase i initiates fatty acid synthesis in pseudomonas putida f1. The Journal of Biological Chemistry, 300:105600, Feb 2024. URL: https://doi.org/10.1016/j.jbc.2023.105600, doi:10.1016/j.jbc.2023.105600. This article has 10 citations.

15. (guo2024diversityinfatty pages 6-8): Qiaoqiao Guo, Canyao Zhong, Huijuan Dong, John E. Cronan, and Haihong Wang. Diversity in fatty acid elongation enzymes: the fabb long-chain β-ketoacyl-acp synthase i initiates fatty acid synthesis in pseudomonas putida f1. The Journal of Biological Chemistry, 300:105600, Feb 2024. URL: https://doi.org/10.1016/j.jbc.2023.105600, doi:10.1016/j.jbc.2023.105600. This article has 10 citations.

16. (guo2024diversityinfatty pages 4-6): Qiaoqiao Guo, Canyao Zhong, Huijuan Dong, John E. Cronan, and Haihong Wang. Diversity in fatty acid elongation enzymes: the fabb long-chain β-ketoacyl-acp synthase i initiates fatty acid synthesis in pseudomonas putida f1. The Journal of Biological Chemistry, 300:105600, Feb 2024. URL: https://doi.org/10.1016/j.jbc.2023.105600, doi:10.1016/j.jbc.2023.105600. This article has 10 citations.

## Artifacts

- [Edison artifact artifact-00](PSEPK__mycolic-acid-biosynthesis__ppu00074-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PSEPK__mycolic-acid-biosynthesis__ppu00074-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. dover2004comparativecellwall pages 2-4
2. marrakchi2014mycolicacidsstructures pages 8-9
3. dover2004comparativecellwall pages 16-18
4. marrakchi2014mycolicacidsstructures pages 7-8
5. kim2018distributionandfunctional pages 2-3
6. mezzina2021engineeringnativeand pages 13-16
7. marrakchi2014mycolicacidsstructures pages 1-2
8. marrakchi2014mycolicacidsstructures pages 2-3
9. dover2004comparativecellwall pages 14-15
10. marrakchi2014mycolicacidsstructures pages 4-6
11. dover2004comparativecellwall pages 15-16
12. marrakchi2014mycolicacidsstructures pages 3-4
13. guo2024diversityinfatty pages 2-4
14. guo2024diversityinfatty pages 1-2
15. guo2024diversityinfatty pages 6-8
16. guo2024diversityinfatty pages 4-6
17. https://doi.org/10.1016/j.chembiol.2013.11.011,
18. https://doi.org/10.1016/j.femsre.2003.10.001,
19. https://doi.org/10.1002/biot.202000165,
20. https://doi.org/10.1016/j.jbc.2023.105600,
21. https://doi.org/10.1073/pnas.1800715115,