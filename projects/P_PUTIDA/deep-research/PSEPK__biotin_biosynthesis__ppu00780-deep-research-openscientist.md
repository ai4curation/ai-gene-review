---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T06:29:48.550254'
end_time: '2026-07-17T06:53:41.174443'
duration_seconds: 1432.62
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: De novo biotin biosynthesis via the BioC-BioH route
  module_summary: Bacterial de novo biotin synthesis in which BioC methylates malonyl-ACP,
    shared fatty-acid-synthase reactions extend the masked intermediate to pimeloyl-ACP
    methyl ester, and BioH removes the methyl group. BioF, BioA, BioD, and BioB then
    assemble the two-ring biotin cofactor. The module models the six pathway-specific
    enzymes; generic fatty-acid elongation machinery is an explicit dependency rather
    than a biotin-specific member, and biotin attachment and BirA-mediated regulation
    are outside the biosynthesis boundary.
  module_outline: "- de novo biotin biosynthesis\n  - 1. malonyl-ACP carboxyl methylation\n\
    \  - Malonyl-ACP to malonyl-ACP methyl ester\n    - BioC malonyl-ACP O-methyltransferase\
    \ (molecular player: BioC malonyl-ACP O-methyltransferase family; activity or\
    \ role: malonyl-ACP O-methyltransferase activity)\n  - 2. pathway-specific ester\
    \ unmasking\n  - Pimeloyl-ACP methyl ester to pimeloyl-ACP\n    - BioH pimeloyl-ACP\
    \ methyl ester esterase (molecular player: BioH pimeloyl-ACP methyl ester esterase\
    \ family; activity or role: pimeloyl-ACP methyl ester esterase activity)\n  -\
    \ 3. 8-amino-7-oxononanoate formation\n  - Pimeloyl-ACP to 8-amino-7-oxononanoate\n\
    \    - BioF 8-amino-7-oxononanoate synthase (molecular player: proteobacterial\
    \ BioF family; activity or role: 8-amino-7-oxononanoate synthase activity)\n \
    \ - 4. 7,8-diaminononanoate formation\n  - 8-amino-7-oxononanoate to 7,8-diaminononanoate\n\
    \    - BioA adenosylmethionine aminotransferase (molecular player: BioA aminotransferase\
    \ family; activity or role: adenosylmethionine-8-amino-7-oxononanoate transaminase\
    \ activity)\n  - 5. dethiobiotin ring closure\n  - 7,8-diaminononanoate to dethiobiotin\n\
    \    - BioD dethiobiotin synthase (molecular player: BioD dethiobiotin synthase\
    \ family; activity or role: dethiobiotin synthase activity)\n  - 6. sulfur insertion\
    \ and biotin formation\n  - Dethiobiotin to biotin\n    - BioB biotin synthase\
    \ (molecular player: BioB radical-SAM biotin synthase family; activity or role:\
    \ biotin synthase activity)"
  module_connections: '- Malonyl-ACP to malonyl-ACP methyl ester precedes Pimeloyl-ACP
    methyl ester to pimeloyl-ACP

    - Pimeloyl-ACP methyl ester to pimeloyl-ACP precedes Pimeloyl-ACP to 8-amino-7-oxononanoate

    - Pimeloyl-ACP to 8-amino-7-oxononanoate precedes 8-amino-7-oxononanoate to 7,8-diaminononanoate

    - 8-amino-7-oxononanoate to 7,8-diaminononanoate precedes 7,8-diaminononanoate
    to dethiobiotin

    - 7,8-diaminononanoate to dethiobiotin precedes Dethiobiotin to biotin'
  pathway_query: ppu00780
  pathway_id: ppu00780
  pathway_name: Biotin metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00780 with 16 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '16'
  candidate_genes: '- bioB: PP_0362 | Q88QX2 | Biotin synthase (EC 2.8.1.6) (EC 2.8.1.6;
    primary bucket kegg:ppu00780)

    - bioF: PP_0363 | Q88QX1 | 8-amino-7-oxononanoate synthase (AONS) (EC 2.3.1.47)
    (7-keto-8-amino-pelargonic acid synthase) (7-KAP synthase) (KAPA synthase) (8-amino-7-ketopelargonate
    synthase) (EC 2.3.1.47; primary bucket kegg:ppu00780)

    - bioH: PP_0364 | Q88QX0 | Pimeloyl-[acp] methyl ester esterase (EC 3.1.1.1, EC
    3.1.1.85) (EC 3.1.1.1; 3.1.1.85; primary bucket kegg:ppu00780)

    - bioC: PP_0365 | Q88QW9 | Malonyl-[acyl-carrier protein] O-methyltransferase
    (Malonyl-ACP O-methyltransferase) (EC 2.1.1.197) (Biotin synthesis protein BioC)
    (EC 2.1.1.197; primary bucket kegg:ppu00780)

    - bioD: PP_0366 | Q88QW8 | ATP-dependent dethiobiotin synthetase BioD (EC 6.3.3.3)
    (DTB synthetase) (DTBS) (Dethiobiotin synthase) (EC 6.3.3.3; primary bucket kegg:ppu00780)

    - birA: PP_0437 | Q88QQ1 | Bifunctional ligase/repressor BirA (Biotin operon repressor)
    (Biotin--[acetyl-CoA-carboxylase] ligase) (EC 6.3.4.15) (Biotin--protein ligase)
    (Biotin-[acetyl-CoA carboxylase] synthetase) (EC 6.3.4.15; primary bucket kegg:ppu00780)

    - PP_0581: PP_0581 | Q88QB3 | 3-oxoacyl-(Acyl-carrier-protein) reductase (primary
    bucket kegg:ppu00780)

    - fabZ: PP_1602 | Q88MG9 | 3-hydroxyacyl-[acyl-carrier-protein] dehydratase FabZ
    (EC 4.2.1.59) ((3R)-hydroxymyristoyl-[acyl-carrier-protein] dehydratase) ((3R)-hydroxymyristoyl-ACP
    dehydrase) (Beta-hydroxyacyl-ACP dehydratase) (EC 4.2.1.59; primary bucket kegg:ppu00780)

    - PP_1852: PP_1852 | Q88LS6 | Enoyl-[acyl-carrier-protein] reductase (NADPH, B-specific)
    (EC 1.3.1.10) (EC 1.3.1.10; primary bucket kegg:ppu00780)

    - fabG: PP_1914 | Q88LL6 | 3-oxoacyl-[acyl-carrier-protein] reductase (EC 1.1.1.100)
    (EC 1.1.1.100; primary bucket kegg:ppu00780)

    - fabF: PP_1916 | Q88LL4 | 3-oxoacyl-[acyl-carrier-protein] synthase 2 (EC 2.3.1.179)
    (EC 2.3.1.179; primary bucket kegg:ppu00780)

    - PP_2540: PP_2540 | Q88JV7 | Oxidoreductase, short-chain dehydrogenase/reductase
    family (primary bucket kegg:ppu00780)

    - PP_2783: PP_2783 | Q88J66 | 2,3-dihydroxy-2,3-dihydro-p-cumate dehydrogenase
    (EC 1.3.1.58) (Biphenyl-2,3-dihydro-2,3-diol dehydrogenase) (EC 1.3.1.58; primary
    bucket kegg:ppu00780)

    - PP_3303: PP_3303 | Q88HQ0 | 3-oxoacyl-[acyl-carrier-protein] synthase 2 (EC
    2.3.1.179) (EC 2.3.1.179; primary bucket kegg:ppu00780)

    - fabB: PP_4175 | Q88FC3 | 3-oxoacyl-[acyl-carrier-protein] synthase 1 (EC 2.3.1.41)
    (3-oxoacyl-[acyl-carrier-protein] synthase I) (Beta-ketoacyl-ACP synthase I) (EC
    2.3.1.41; primary bucket kegg:ppu00780)

    - bioA: PP_4984 | Q88D44 | Adenosylmethionine-8-amino-7-oxononanoate aminotransferase
    (EC 2.6.1.62) (7,8-diamino-pelargonic acid aminotransferase) (DAPA AT) (DAPA aminotransferase)
    (7,8-diaminononanoate synthase) (DANS) (Diaminopelargonic acid synthase) (EC 2.6.1.62;
    primary bucket kegg:ppu00780)'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__biotin_biosynthesis__ppu00780-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__biotin_biosynthesis__ppu00780-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

De novo biotin biosynthesis via the BioC-BioH route in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00780
- Resolved ID: ppu00780
- Resolved name: Biotin metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00780 with 16 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 16

- bioB: PP_0362 | Q88QX2 | Biotin synthase (EC 2.8.1.6) (EC 2.8.1.6; primary bucket kegg:ppu00780)
- bioF: PP_0363 | Q88QX1 | 8-amino-7-oxononanoate synthase (AONS) (EC 2.3.1.47) (7-keto-8-amino-pelargonic acid synthase) (7-KAP synthase) (KAPA synthase) (8-amino-7-ketopelargonate synthase) (EC 2.3.1.47; primary bucket kegg:ppu00780)
- bioH: PP_0364 | Q88QX0 | Pimeloyl-[acp] methyl ester esterase (EC 3.1.1.1, EC 3.1.1.85) (EC 3.1.1.1; 3.1.1.85; primary bucket kegg:ppu00780)
- bioC: PP_0365 | Q88QW9 | Malonyl-[acyl-carrier protein] O-methyltransferase (Malonyl-ACP O-methyltransferase) (EC 2.1.1.197) (Biotin synthesis protein BioC) (EC 2.1.1.197; primary bucket kegg:ppu00780)
- bioD: PP_0366 | Q88QW8 | ATP-dependent dethiobiotin synthetase BioD (EC 6.3.3.3) (DTB synthetase) (DTBS) (Dethiobiotin synthase) (EC 6.3.3.3; primary bucket kegg:ppu00780)
- birA: PP_0437 | Q88QQ1 | Bifunctional ligase/repressor BirA (Biotin operon repressor) (Biotin--[acetyl-CoA-carboxylase] ligase) (EC 6.3.4.15) (Biotin--protein ligase) (Biotin-[acetyl-CoA carboxylase] synthetase) (EC 6.3.4.15; primary bucket kegg:ppu00780)
- PP_0581: PP_0581 | Q88QB3 | 3-oxoacyl-(Acyl-carrier-protein) reductase (primary bucket kegg:ppu00780)
- fabZ: PP_1602 | Q88MG9 | 3-hydroxyacyl-[acyl-carrier-protein] dehydratase FabZ (EC 4.2.1.59) ((3R)-hydroxymyristoyl-[acyl-carrier-protein] dehydratase) ((3R)-hydroxymyristoyl-ACP dehydrase) (Beta-hydroxyacyl-ACP dehydratase) (EC 4.2.1.59; primary bucket kegg:ppu00780)
- PP_1852: PP_1852 | Q88LS6 | Enoyl-[acyl-carrier-protein] reductase (NADPH, B-specific) (EC 1.3.1.10) (EC 1.3.1.10; primary bucket kegg:ppu00780)
- fabG: PP_1914 | Q88LL6 | 3-oxoacyl-[acyl-carrier-protein] reductase (EC 1.1.1.100) (EC 1.1.1.100; primary bucket kegg:ppu00780)
- fabF: PP_1916 | Q88LL4 | 3-oxoacyl-[acyl-carrier-protein] synthase 2 (EC 2.3.1.179) (EC 2.3.1.179; primary bucket kegg:ppu00780)
- PP_2540: PP_2540 | Q88JV7 | Oxidoreductase, short-chain dehydrogenase/reductase family (primary bucket kegg:ppu00780)
- PP_2783: PP_2783 | Q88J66 | 2,3-dihydroxy-2,3-dihydro-p-cumate dehydrogenase (EC 1.3.1.58) (Biphenyl-2,3-dihydro-2,3-diol dehydrogenase) (EC 1.3.1.58; primary bucket kegg:ppu00780)
- PP_3303: PP_3303 | Q88HQ0 | 3-oxoacyl-[acyl-carrier-protein] synthase 2 (EC 2.3.1.179) (EC 2.3.1.179; primary bucket kegg:ppu00780)
- fabB: PP_4175 | Q88FC3 | 3-oxoacyl-[acyl-carrier-protein] synthase 1 (EC 2.3.1.41) (3-oxoacyl-[acyl-carrier-protein] synthase I) (Beta-ketoacyl-ACP synthase I) (EC 2.3.1.41; primary bucket kegg:ppu00780)
- bioA: PP_4984 | Q88D44 | Adenosylmethionine-8-amino-7-oxononanoate aminotransferase (EC 2.6.1.62) (7,8-diamino-pelargonic acid aminotransferase) (DAPA AT) (DAPA aminotransferase) (7,8-diaminononanoate synthase) (DANS) (Diaminopelargonic acid synthase) (EC 2.6.1.62; primary bucket kegg:ppu00780)

## Generic Module Context

### Working Scope

Bacterial de novo biotin synthesis in which BioC methylates malonyl-ACP, shared fatty-acid-synthase reactions extend the masked intermediate to pimeloyl-ACP methyl ester, and BioH removes the methyl group. BioF, BioA, BioD, and BioB then assemble the two-ring biotin cofactor. The module models the six pathway-specific enzymes; generic fatty-acid elongation machinery is an explicit dependency rather than a biotin-specific member, and biotin attachment and BirA-mediated regulation are outside the biosynthesis boundary.

### Provisional Biological Outline

- de novo biotin biosynthesis
  - 1. malonyl-ACP carboxyl methylation
  - Malonyl-ACP to malonyl-ACP methyl ester
    - BioC malonyl-ACP O-methyltransferase (molecular player: BioC malonyl-ACP O-methyltransferase family; activity or role: malonyl-ACP O-methyltransferase activity)
  - 2. pathway-specific ester unmasking
  - Pimeloyl-ACP methyl ester to pimeloyl-ACP
    - BioH pimeloyl-ACP methyl ester esterase (molecular player: BioH pimeloyl-ACP methyl ester esterase family; activity or role: pimeloyl-ACP methyl ester esterase activity)
  - 3. 8-amino-7-oxononanoate formation
  - Pimeloyl-ACP to 8-amino-7-oxononanoate
    - BioF 8-amino-7-oxononanoate synthase (molecular player: proteobacterial BioF family; activity or role: 8-amino-7-oxononanoate synthase activity)
  - 4. 7,8-diaminononanoate formation
  - 8-amino-7-oxononanoate to 7,8-diaminononanoate
    - BioA adenosylmethionine aminotransferase (molecular player: BioA aminotransferase family; activity or role: adenosylmethionine-8-amino-7-oxononanoate transaminase activity)
  - 5. dethiobiotin ring closure
  - 7,8-diaminononanoate to dethiobiotin
    - BioD dethiobiotin synthase (molecular player: BioD dethiobiotin synthase family; activity or role: dethiobiotin synthase activity)
  - 6. sulfur insertion and biotin formation
  - Dethiobiotin to biotin
    - BioB biotin synthase (molecular player: BioB radical-SAM biotin synthase family; activity or role: biotin synthase activity)

### Known Relationships Among Steps

- Malonyl-ACP to malonyl-ACP methyl ester precedes Pimeloyl-ACP methyl ester to pimeloyl-ACP
- Pimeloyl-ACP methyl ester to pimeloyl-ACP precedes Pimeloyl-ACP to 8-amino-7-oxononanoate
- Pimeloyl-ACP to 8-amino-7-oxononanoate precedes 8-amino-7-oxononanoate to 7,8-diaminononanoate
- 8-amino-7-oxononanoate to 7,8-diaminononanoate precedes 7,8-diaminononanoate to dethiobiotin
- 7,8-diaminononanoate to dethiobiotin precedes Dethiobiotin to biotin

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

# Module/Pathway/Taxon Review: De novo biotin biosynthesis via the BioC–BioH route in *Pseudomonas putida* KT2440

**Taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Bucket:** KEGG `ppu00780` "Biotin metabolism"; module area = de novo biotin biosynthesis (BioC–BioH / modified-FAS route)
**Review date:** 2026-07-17 · Evidence: literature + UniProtKB + InterPro/Pfam + KEGG (no experimental data files supplied)

---

## 1. Executive summary

The biotin BioC–BioH module is **fully satisfiable** in *P. putida* KT2440. All six pathway-specific enzymatic steps are encoded by candidate genes, five of them in a single contiguous **`bioBFHCD` operon** (PP_0362–PP_0366) with `bioA` (PP_4984) unlinked. Each of the six core genes carries a **diagnostic, biotin-specific InterPro/Pfam signature** (not merely a propagated gene name), and KEGG assigns all six route-defining KOs (K01012, K00652, K02170, K02169, K01935, K00833). The organism is a predicted **biotin prototroph** using the canonical modified-fatty-acid-synthesis route; the lineage-specific alternatives (BioI/BioW/BioU) are absent and **not expected**.

The chief curation issues are **over-inclusion**, not gaps: 9 of the 16 bucket genes are **generic fatty-acid-synthase (FAS) enzymes** that KEGG pulls into `ppu00780` because the pimelate chain is built by shared FAS chemistry — these are explicit dependencies, not biotin-specific members — and one gene (`PP_2783`, a p-cumate catabolic dehydrogenase) is a **spurious inclusion**. The single genuine biotin-specific gene warranting closer scrutiny is **`bioH` (PP_0364)**: it is the least-conserved step (UniProt PE4/Predicted, no assigned EC in UniProt), though its membership in the dedicated BioH carboxylesterase InterPro family (IPR050228) supports the annotation.

Evidence for KT2440 is **homology/domain/pathway-database based (PE3–4)**; there is no direct biochemical or genetic characterization of the KT2440 bio proteins themselves. The strongest transferable experimental evidence comes from *P. aeruginosa* (operon-encoded BioH; strong transfer within *Pseudomonas*) and from *E. coli* (mechanism of the whole route; strong for conserved steps).

---

## 2. Target-organism pathway definition

**Process included (module boundary):** de novo synthesis of the biotin cofactor from a malonyl-thioester precursor, comprising two conceptual halves:

1. **Pimelate (C7 α,ω-dicarboxylate) moiety synthesis by a "disguised" FAS pathway.** BioC O-methylates the free ω-carboxyl of malonyl-ACP so that the atypical substrate is accepted by the housekeeping FAS elongation enzymes; two elongation cycles yield pimeloyl-ACP methyl ester, which BioH hydrolyzes to pimeloyl-ACP + methanol (Lin, Hanson & Cronan 2010, PMID 20693992; Cronan & Lin 2011, PMID 21435937; Lin & Cronan 2012, PMID 22965231).
2. **Assembly of the fused rings**: BioF (pimeloyl-ACP + L-Ala → 8-amino-7-oxononanoate, KAPA), BioA (KAPA + SAM → 7,8-diaminononanoate, DAPA), BioD (DAPA + CO2/ATP → dethiobiotin), BioB (dethiobiotin + S → biotin).

**Kept separate (neighboring processes / overview maps):**
- **Fatty-acid biosynthesis (KEGG map00061 / fab genes).** The FAS elongation enzymes (FabB/F/G/Z, enoyl-ACP reductase) act on the BioC-masked intermediate but are **not biotin-specific**; they belong to FAS and should be modeled as a dependency, not module members.
- **Biotin activation / protein biotinylation and regulation (BirA).** Per the module scope, biotin–[acetyl-CoA-carboxylase] ligase activity and BirA-mediated transcriptional repression are **outside the biosynthesis boundary**.
- **Aromatic/p-cumate catabolism** (source of the mis-bucketed `PP_2783`).

**Alternate names / database definitions:** MetaCyc "biotin biosynthesis I (BioC-BioH)"; KEGG module **M00123** "Biotin biosynthesis, pimeloyl-ACP/CoA => biotin"; the pimelate-initiation genes `bioC`/`bioH` correspond to KOs **K02169/K02170**. Distinct KEGG routes not used here: **M00573** BioI (P450, K16593), **M00577** BioW (pimeloyl-CoA synthetase, K01906), **M00950** BioU (K25570).

---

## 3. Expected step model and satisfiability

| # | Step (substrate → product) | Enzyme / KO / EC | Candidate gene | Status |
|---|---|---|---|---|
| 1 | malonyl-ACP → malonyl-ACP methyl ester | BioC O-MTase / K02169 / 2.1.1.197 | **bioC PP_0365** | **covered** |
| 2 | pimeloyl-ACP methyl ester → pimeloyl-ACP | BioH esterase / K02170 / 3.1.1.85 | **bioH PP_0364** | **covered** (verify; least-conserved) |
| 3 | pimeloyl-ACP → KAPA (8-amino-7-oxononanoate) | BioF AONS / K00652 / 2.3.1.47 | **bioF PP_0363** | **covered** |
| 4 | KAPA → DAPA (7,8-diaminononanoate) | BioA aminotransferase / K00833 / 2.6.1.62 | **bioA PP_4984** | **covered** |
| 5 | DAPA → dethiobiotin | BioD synthetase / K01935 / 6.3.3.3 | **bioD PP_0366** | **covered** |
| 6 | dethiobiotin → biotin | BioB radical-SAM synthase / K01012 / 2.8.1.6 | **bioB PP_0362** | **covered** |

**Dependency (not a module step):** FAS elongation of the masked intermediate (steps between 1 and 2) — supplied by housekeeping FabB/FabF/FabG/FabZ/enoyl-ACP-reductase + ACP + malonyl-ACP. Present in KT2440 but should be modeled as an external dependency.

**Not expected in this taxon:** BioI (P450) pimelate route, BioW (pimeloyl-CoA) route, BioU route — mark `not_expected_in_target_taxon`.

All six expected steps are encoded → **module = COVERED / satisfiable**.

---

## 4. Candidate genes and evidence

### Core biotin-specific genes (promote/retain)

- **bioC — PP_0365 / Q88QW9.** Malonyl-ACP O-methyltransferase (EC 2.1.1.197, K02169). InterPro IPR011814 **BioC** + IPR050602 Malonyl-ACP_OMT; Pfam Methyltransf_11 (SAM-dependent). UniProt PE3, "Biotin biosynthesis" keyword. Operon position (…H**C**D…). *Evidence:* homology + diagnostic domain. Confidence **high**. Caveat: mechanism proven in *E. coli*/*B. cereus* (PMID 22965231), transfer to KT2440 strong (conserved family).
- **bioH — PP_0364 / Q88QX0.** Pimeloyl-ACP-methyl-ester esterase (EC 3.1.1.85, K02170). InterPro IPR050228 **Carboxylesterase_BioH**, α/β-hydrolase (Pfam Abhydrolase_6). **UniProt PE4 (Predicted), no EC assigned in UniProt, no biotin keyword.** *Evidence:* homology/synteny **plus intact catalytic machinery** — the 243-aa protein has the AB_hydrolase-1 domain (res 5–231), a G-X-S-X-G nucleophile elbow (**GWSLG, Ser68**) and a C-terminal catalytic Asp/His (…GMVE-**D**-SS-**H**-AF…), reproducing the Ser–Asp–His triad of characterized BioH esterases (E. coli / *K. pneumoniae* Ser82–Asp207–His235; PMID 31615653). Confidence **moderate→high**. Caveat: the esterase step is the "wild card" of the pathway — in different bacteria BioH is replaced by non-homologous α/β-hydrolases (BioG/BioJ/BioK/BioV; PMID 28526858). Here it is operon-encoded like *P. aeruginosa* BioH, and the catalytic triad is complete, which supports the call; residual uncertainty is only substrate specificity, best resolved by a ΔbioH complementation test.
- **bioF — PP_0363 / Q88QX1.** 8-amino-7-oxononanoate synthase (EC 2.3.1.47, K00652). InterPro IPR022834 **AONS_Proteobacteria** (matches expected proteobacterial BioF clade); PLP-dependent Aminotran_1_2. PE3, biotin keyword. Confidence **high**.
- **bioA — PP_4984 / Q88D44.** Adenosylmethionine–KAPA aminotransferase (EC 2.6.1.62, K00833). InterPro IPR005815 **BioA**, Aminotran_3 (SAM as amino donor — the standard proteobacterial route). PE3, biotin keyword. Unlinked from the operon (common). Confidence **high**.
- **bioD — PP_0366 / Q88QW8.** ATP-dependent dethiobiotin synthetase (EC 6.3.3.3, K01935). InterPro IPR004472 **DTB_synth_BioD**, P-loop NTPase. PE3, biotin keyword. Confidence **high**.
- **bioB — PP_0362 / Q88QX2.** Biotin synthase (EC 2.8.1.6, K01012). InterPro IPR024177 **Biotin_synthase**, Radical_SAM + BATS domains. PE3, biotin keyword. Confidence **high**. (Requires Fe-S cluster machinery + SAM; sulfur donor debated but housekeeping.)

### Regulatory / boundary gene

- **birA — PP_0437 / Q88QQ1.** Bifunctional biotin-protein ligase / biotin operon repressor (EC 6.3.4.15, K03524). InterPro IPR030855 Bifunct_BirA (BPL_LplA_LipB + HTH_11). Genuine, but **outside the biosynthesis module boundary** (activation + regulation). Retain in bucket for context; do not count toward biosynthesis satisfiability.

### Generic FAS / dependency genes (over-propagated into the bucket)

`fabB` PP_4175 (K.-ACP synthase I, 2.3.1.41), `fabF` PP_1916 & `PP_3303` (KAS-II, 2.3.1.179), `fabG` PP_1914 (KR, 1.1.1.100), `fabZ` PP_1602 (dehydratase, 4.2.1.59), `PP_1852` (enoyl-ACP reductase, 1.3.1.10), `PP_0581` (3-oxoacyl-ACP reductase), `PP_2540` (SDR-family oxidoreductase). **None carries a biotin keyword.** These are housekeeping FAS enzymes that operate on the BioC-masked intermediate. Curation: **dependency / not biotin-specific**; do not treat as module members.

### Spurious inclusion

- **PP_2783 / Q88J66.** 2,3-dihydroxy-2,3-dihydro-p-cumate dehydrogenase (EC 1.3.1.58) — **p-cumate/aromatic catabolism**, no biotin role. Clear over-annotation artifact of the KEGG bucket; **remove** from the biotin module.

---

## 5. Gaps, ambiguities, and likely over-annotations

- **No true gaps.** Every expected step has a candidate gene with a diagnostic domain; pimelate initiation is not a gap because bioC+bioH are present.
- **bioH ambiguity (only real uncertainty).** Least-conserved step; PE4/Predicted; no UniProt EC. Family membership (IPR050228) and operon context support it, but functional confirmation is lacking for KT2440. → `candidate_uncertain`-leaning-`covered`; promote to full review.
- **Broad EC on bioH metadata.** Local metadata lists both EC 3.1.1.1 (generic carboxylesterase) and EC 3.1.1.85 (specific pimeloyl-ACP-methyl-ester esterase). Prefer the **specific** 3.1.1.85 for the module; 3.1.1.1 is over-general and could over-propagate.
- **Paralog notes.** `fabF`/KAS-II activity is represented by two loci (PP_1916, PP_3303) — normal FAS redundancy, irrelevant to biotin-specific curation. Any of several FAS reductases could service the masked intermediate; do not single one out.
- **FAS over-inclusion (9 genes).** Bucket artifact from KEGG map topology; flag as dependency.
- **PP_2783 mis-bucket (1 gene).** Remove.

---

## 6. Module and GO-curation recommendations

**Per-step status:**
- Steps 1–6 (bioC, bioH, bioF, bioA, bioD, bioB): **covered** — with bioH annotated "covered, verify" (moderate confidence).
- FAS elongation between steps 1–2: model as **external dependency** (fatty-acid biosynthesis), not a biotin module step.
- BioI / BioW / BioU alternative routes: **not_expected_in_target_taxon**.

**Module-level:**
- Mark the module **satisfiable/COVERED** for *P. putida* KT2440.
- **module_needs_revision (bucket cleanup):** remove the 9 generic FAS genes and `PP_2783` from the biotin-specific member set; retain them only as an explicit FAS dependency link. Move `birA` to a "regulation/activation" adjunct outside the biosynthesis boundary.
- Generic module boundaries are **appropriate** for this organism (six-enzyme model fits); the KEGG *bucket* is what is inflated, not the module definition.

**GO curation:** no new GO terms required — existing terms suffice: GO:0009102 biotin biosynthetic process; GO:0010340 carboxyl-O-methyltransferase (BioC); GO:0090499 pimeloyl-ACP methyl ester carboxylesterase / GO:0052689 (BioH); GO:0008710 8-amino-7-oxononanoate synthase (BioF); GO:0004015 adenosylmethionine-8-amino-7-oxononanoate transaminase (BioA); GO:0004141 dethiobiotin synthase (BioD); GO:0004076 biotin synthase (BioB). Recommend annotating KT2440 bio genes with evidence code **IEA/ISS** (inferred from sequence/homology), not IDA, since no direct assays exist for this strain.

---

## 7. Genes to promote to full `fetch-gene` review

1. **bioH (PP_0364)** — highest priority. Non-conserved esterase step; PE4/Predicted; UniProt lacks EC. Confirm it is the functional pimeloyl-ACP-methyl-ester esterase (vs. a substitute α/β-hydrolase) and resolve the broad-vs-specific EC. Ideal experiment: complementation of an *E. coli* ΔbioH mutant.
2. **bioC (PP_0365)** — secondary. Confirm malonyl-ACP (not malonyl-CoA) specificity and that no second SAM-MTase confounds annotation.
3. **bioB (PP_0362)** — light-touch. Verify Fe-S/radical-SAM residue conservation and available sulfur-donor context (housekeeping, but worth a domain-completeness check).

bioF, bioA, bioD are high-confidence and need only routine confirmation.

---

## 8. Key references

- Lin S, Hanson RE, Cronan JE. *Biotin synthesis begins by hijacking the fatty acid synthetic pathway.* Nat Chem Biol 2010. **PMID 20693992.** (Defines the BioC-methylation / BioH-demethylation route.)
- Cronan JE, Lin S. *Synthesis of the α,ω-dicarboxylic acid precursor of biotin by the canonical fatty acid biosynthetic pathway.* Curr Opin Chem Biol 2011. **PMID 21435937.** (Pimelate via modified FAS; BioI as the restricted alternative.)
- Lin S, Cronan JE. *The BioC O-methyltransferase catalyzes methyl esterification of malonyl-ACP, an essential step in biotin synthesis.* J Biol Chem 2012. **PMID 22965231.** (BioC substrate = malonyl-ACP.)
- Cao X, Zhu L, Hu Z, Cronan JE. *Expression and Activity of the BioH Esterase of Biotin Synthesis is Independent of Genome Context.* Sci Rep 2017. **PMID 28526858.** (*P. aeruginosa* operon-encoded BioH; esterase "wild-card" plasticity — strongest within-*Pseudomonas* transfer.)
- Wang M et al. *Structural insight into the carboxylesterase BioH from Klebsiella pneumoniae.* 2019. **PMID 31615653.** (BioH catalytic triad / α/β-hydrolase fold.)
- Chow J et al. *The Thaumarchaeon N. gargensis carries functional bioABD genes and a promiscuous ΔbioH-complementing esterase EstN1.* 2018. **PMID 30218044.** (Illustrates esterase substitutability.)
- Zeng J et al. *Pimeloyl-ACP methyl ester esterase…* 2020. **PMID 32117167.**
- Data resources: UniProtKB proteome UP000000556; InterPro/Pfam; KEGG `ppu00780`, modules M00123/M00573/M00577/M00950.

---

### Evidence grade summary
| Claim | Basis | Directness for KT2440 |
|---|---|---|
| Six steps encoded; operon `bioBFHCD` | UniProt loci + KEGG | Direct genomic (strain) |
| Diagnostic family assignments | InterPro/Pfam | Direct sequence (strain) |
| Route = BioC-BioH (not BioI/W/U) | KEGG KO presence/absence | Direct genomic (strain) |
| Mechanism of each step | *E. coli*/*B. cereus* biochemistry | Inferred (strong for conserved steps) |
| bioH is a functional esterase | *P. aeruginosa*/*E. coli* + domain family | Inferred (moderate; verify) |
| Prototrophy | pathway completeness | Inferred (no growth assay cited) |


## Artifacts

- [OpenScientist final report](PSEPK__biotin_biosynthesis__ppu00780-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__biotin_biosynthesis__ppu00780-deep-research-openscientist_artifacts/final_report.pdf)