---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-26T18:28:55.824322'
end_time: '2026-07-26T19:13:58.591983'
duration_seconds: 2702.77
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial phosphatidylethanolamine biosynthesis through phosphatidylserine
  module_summary: A reusable two-reaction bacterial module for phosphatidylethanolamine
    biosynthesis from CDP-diacylglycerol. PssA transfers a phosphatidyl group to L-serine
    to form phosphatidylserine, and pyruvoyl-dependent Psd decarboxylates phosphatidylserine
    to phosphatidylethanolamine.
  module_outline: "- Bacterial phosphatidylethanolamine biosynthesis\n  - 1. phosphatidylserine\
    \ formation\n  - PssA-dependent phosphatidylserine formation\n    - Alternative\
    \ versions by enzyme architecture: Bacterial phosphatidylserine synthase architecture\n\
    \      - Class-I peripheral-membrane PssA\n        - Class-I PssA phosphatidylserine\
    \ synthase activity (molecular player: class-I phosphatidylserine synthase family;\
    \ activity or role: CDP-diacylglycerol-serine O-phosphatidyltransferase activity)\n\
    \      - Class-II integral-membrane PssA\n        - Class-II PssA phosphatidylserine\
    \ synthase activity (molecular player: class-II phosphatidylserine synthase family;\
    \ activity or role: CDP-diacylglycerol-serine O-phosphatidyltransferase activity)\n\
    \  - 2. phosphatidylethanolamine formation\n  - Psd-dependent phosphatidylethanolamine\
    \ formation\n    - Psd phosphatidylserine decarboxylase activity (molecular player:\
    \ type-I phosphatidylserine decarboxylase family; activity or role: phosphatidylserine\
    \ decarboxylase activity)"
  module_connections: '- PssA-dependent phosphatidylserine formation feeds into Psd-dependent
    phosphatidylethanolamine formation: PssA supplies phosphatidylserine to Psd.'
  pathway_query: ppu00564
  pathway_id: ppu00564
  pathway_name: Glycerophospholipid metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00564 with 17 primary genes; module
    area: lipid_cell_envelope_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '23'
  candidate_genes: '- PP_0058: PP_0058 | Q88RS1 | 1-acyl-sn-glycerol-3-phosphate acyltransferase
    (primary bucket kegg:ppu00561)

    - plsY: PP_0391 | Q88QU5 | Glycerol-3-phosphate acyltransferase (Acyl-PO4 G3P
    acyltransferase) (Acyl-phosphate--glycerol-3-phosphate acyltransferase) (G3P acyltransferase)
    (GPAT) (EC 2.3.1.275) (Lysophosphatidic acid synthase) (LPA synthase) (EC 2.3.1.275;
    primary bucket kegg:ppu00561)

    - pgpA: PP_0520 | Q88QH3 | Phosphatidylglycerophosphatase A (EC 3.1.3.27) (Phosphatidylglycerolphosphate
    phosphatase A) (EC 3.1.3.27; primary bucket kegg:ppu00564)

    - eutC: PP_0542 | Q88QF2 | Ethanolamine ammonia-lyase small subunit (EAL small
    subunit) (EC 4.3.1.7) (EC 4.3.1.7; primary bucket kegg:ppu00564)

    - eutB: PP_0543 | Q88QF1 | Ethanolamine ammonia-lyase large subunit (EAL large
    subunit) (EC 4.3.1.7) (EC 4.3.1.7; primary bucket kegg:ppu00564)

    - pcs: PP_0731 | Q88PW7 | Phosphatidylcholine synthase (EC 2.7.8.24) (EC 2.7.8.24;
    primary bucket kegg:ppu00564)

    - PP_0892: PP_0892 | Q88PF8 | Phospholipase family protein (primary bucket kegg:ppu00564)

    - glpD: PP_1073 | Q88NY0 | Glycerol-3-phosphate dehydrogenase (EC 1.1.5.3) (EC
    1.1.5.3; primary bucket kegg:ppu00564)

    - plsB: PP_1520 | Q88MQ0 | Glycerol-3-phosphate acyltransferase (GPAT) (EC 2.3.1.15)
    (EC 2.3.1.15; primary bucket kegg:ppu00561)

    - cdsA: PP_1596 | Q88MH5 | Phosphatidate cytidylyltransferase (EC 2.7.7.41) (EC
    2.7.7.41; primary bucket kegg:ppu00564)

    - dgkA-I: PP_1636 | Q88MD7 | Diacylglycerol kinase (EC 2.7.1.107) (EC 2.7.1.107;
    primary bucket kegg:ppu00561)

    - plsC: PP_1844 | Q88LT3 | 1-acyl-sn-glycerol-3-phosphate acyltransferase (EC
    2.3.1.51) (EC 2.3.1.51; primary bucket kegg:ppu00561)

    - ugpQ: PP_2152 | Q88KY7 | Glycerophosphoryl diester phosphodiesterase (EC 3.1.4.46)
    (EC 3.1.4.46; primary bucket kegg:ppu00564)

    - dgkA-II: PP_2973 | Q88IM6 | Diacylglycerol kinase (EC 2.7.1.107) (EC 2.7.1.107;
    primary bucket kegg:ppu00561)

    - clsB: PP_3264 | Q88HT9 | Cardiolipin synthase B (CL synthase) (EC 2.7.8.-) (EC
    2.7.8.-; primary bucket kegg:ppu00564)

    - pssA: PP_3664 | Q88GQ4 | CDP-diacylglycerol--serine O-phosphatidyltransferase
    (EC 2.7.8.8) (EC 2.7.8.8; primary bucket kegg:ppu00564)

    - pgsA: PP_4097 | Q88FJ8 | CDP-diacylglycerol--glycerol-3-phosphate 3-phosphatidyltransferase
    (EC 2.7.8.5) (EC 2.7.8.5; primary bucket kegg:ppu00564)

    - gpsA: PP_4169 | Q88FC9 | Glycerol-3-phosphate dehydrogenase [NAD(P)+] (EC 1.1.1.94)
    (NAD(P)(+)-dependent glycerol-3-phosphate dehydrogenase) (NAD(P)H-dependent dihydroxyacetone-phosphate
    reductase) (EC 1.1.1.94; primary bucket kegg:ppu00564)

    - PP_4677: PP_4677 | Q88DZ1 | CDP-diacylglycerol--serine O-phosphatidyltransferase
    (EC 2.7.8.8) (Phosphatidylserine synthase) (EC 2.7.8.8; primary bucket kegg:ppu00564)

    - psd: PP_4908 | Q88DB9 | Phosphatidylserine decarboxylase proenzyme (EC 4.1.1.65)
    [Cleaved into: Phosphatidylserine decarboxylase alpha chain; Phosphatidylserine
    decarboxylase beta chain] (EC 4.1.1.65; primary bucket kegg:ppu00564)

    - pchP: PP_5130 | Q88CQ0 | Phosphoethanolamine/phosphocholine phosphatase (EC
    3.1.3.75) (EC 3.1.3.75; primary bucket kegg:ppu00564)

    - PP_5276: PP_5276 | Q88CA5 | Phospholipase D family protein (primary bucket kegg:ppu00564)

    - clsA: PP_5364 | Q88C19 | Cardiolipin synthase A (CL synthase) (EC 2.7.8.-) (EC
    2.7.8.-; primary bucket kegg:ppu00564)'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 4
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__bacterial_phosphatidylethanolamine_biosynthesis__ppu00564-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_phosphatidylethanolamine_biosynthesis__ppu00564-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial phosphatidylethanolamine biosynthesis through phosphatidylserine in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00564
- Resolved ID: ppu00564
- Resolved name: Glycerophospholipid metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00564 with 17 primary genes; module area: lipid_cell_envelope_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 23

- PP_0058: PP_0058 | Q88RS1 | 1-acyl-sn-glycerol-3-phosphate acyltransferase (primary bucket kegg:ppu00561)
- plsY: PP_0391 | Q88QU5 | Glycerol-3-phosphate acyltransferase (Acyl-PO4 G3P acyltransferase) (Acyl-phosphate--glycerol-3-phosphate acyltransferase) (G3P acyltransferase) (GPAT) (EC 2.3.1.275) (Lysophosphatidic acid synthase) (LPA synthase) (EC 2.3.1.275; primary bucket kegg:ppu00561)
- pgpA: PP_0520 | Q88QH3 | Phosphatidylglycerophosphatase A (EC 3.1.3.27) (Phosphatidylglycerolphosphate phosphatase A) (EC 3.1.3.27; primary bucket kegg:ppu00564)
- eutC: PP_0542 | Q88QF2 | Ethanolamine ammonia-lyase small subunit (EAL small subunit) (EC 4.3.1.7) (EC 4.3.1.7; primary bucket kegg:ppu00564)
- eutB: PP_0543 | Q88QF1 | Ethanolamine ammonia-lyase large subunit (EAL large subunit) (EC 4.3.1.7) (EC 4.3.1.7; primary bucket kegg:ppu00564)
- pcs: PP_0731 | Q88PW7 | Phosphatidylcholine synthase (EC 2.7.8.24) (EC 2.7.8.24; primary bucket kegg:ppu00564)
- PP_0892: PP_0892 | Q88PF8 | Phospholipase family protein (primary bucket kegg:ppu00564)
- glpD: PP_1073 | Q88NY0 | Glycerol-3-phosphate dehydrogenase (EC 1.1.5.3) (EC 1.1.5.3; primary bucket kegg:ppu00564)
- plsB: PP_1520 | Q88MQ0 | Glycerol-3-phosphate acyltransferase (GPAT) (EC 2.3.1.15) (EC 2.3.1.15; primary bucket kegg:ppu00561)
- cdsA: PP_1596 | Q88MH5 | Phosphatidate cytidylyltransferase (EC 2.7.7.41) (EC 2.7.7.41; primary bucket kegg:ppu00564)
- dgkA-I: PP_1636 | Q88MD7 | Diacylglycerol kinase (EC 2.7.1.107) (EC 2.7.1.107; primary bucket kegg:ppu00561)
- plsC: PP_1844 | Q88LT3 | 1-acyl-sn-glycerol-3-phosphate acyltransferase (EC 2.3.1.51) (EC 2.3.1.51; primary bucket kegg:ppu00561)
- ugpQ: PP_2152 | Q88KY7 | Glycerophosphoryl diester phosphodiesterase (EC 3.1.4.46) (EC 3.1.4.46; primary bucket kegg:ppu00564)
- dgkA-II: PP_2973 | Q88IM6 | Diacylglycerol kinase (EC 2.7.1.107) (EC 2.7.1.107; primary bucket kegg:ppu00561)
- clsB: PP_3264 | Q88HT9 | Cardiolipin synthase B (CL synthase) (EC 2.7.8.-) (EC 2.7.8.-; primary bucket kegg:ppu00564)
- pssA: PP_3664 | Q88GQ4 | CDP-diacylglycerol--serine O-phosphatidyltransferase (EC 2.7.8.8) (EC 2.7.8.8; primary bucket kegg:ppu00564)
- pgsA: PP_4097 | Q88FJ8 | CDP-diacylglycerol--glycerol-3-phosphate 3-phosphatidyltransferase (EC 2.7.8.5) (EC 2.7.8.5; primary bucket kegg:ppu00564)
- gpsA: PP_4169 | Q88FC9 | Glycerol-3-phosphate dehydrogenase [NAD(P)+] (EC 1.1.1.94) (NAD(P)(+)-dependent glycerol-3-phosphate dehydrogenase) (NAD(P)H-dependent dihydroxyacetone-phosphate reductase) (EC 1.1.1.94; primary bucket kegg:ppu00564)
- PP_4677: PP_4677 | Q88DZ1 | CDP-diacylglycerol--serine O-phosphatidyltransferase (EC 2.7.8.8) (Phosphatidylserine synthase) (EC 2.7.8.8; primary bucket kegg:ppu00564)
- psd: PP_4908 | Q88DB9 | Phosphatidylserine decarboxylase proenzyme (EC 4.1.1.65) [Cleaved into: Phosphatidylserine decarboxylase alpha chain; Phosphatidylserine decarboxylase beta chain] (EC 4.1.1.65; primary bucket kegg:ppu00564)
- pchP: PP_5130 | Q88CQ0 | Phosphoethanolamine/phosphocholine phosphatase (EC 3.1.3.75) (EC 3.1.3.75; primary bucket kegg:ppu00564)
- PP_5276: PP_5276 | Q88CA5 | Phospholipase D family protein (primary bucket kegg:ppu00564)
- clsA: PP_5364 | Q88C19 | Cardiolipin synthase A (CL synthase) (EC 2.7.8.-) (EC 2.7.8.-; primary bucket kegg:ppu00564)

## Generic Module Context

### Working Scope

A reusable two-reaction bacterial module for phosphatidylethanolamine biosynthesis from CDP-diacylglycerol. PssA transfers a phosphatidyl group to L-serine to form phosphatidylserine, and pyruvoyl-dependent Psd decarboxylates phosphatidylserine to phosphatidylethanolamine.

### Provisional Biological Outline

- Bacterial phosphatidylethanolamine biosynthesis
  - 1. phosphatidylserine formation
  - PssA-dependent phosphatidylserine formation
    - Alternative versions by enzyme architecture: Bacterial phosphatidylserine synthase architecture
      - Class-I peripheral-membrane PssA
        - Class-I PssA phosphatidylserine synthase activity (molecular player: class-I phosphatidylserine synthase family; activity or role: CDP-diacylglycerol-serine O-phosphatidyltransferase activity)
      - Class-II integral-membrane PssA
        - Class-II PssA phosphatidylserine synthase activity (molecular player: class-II phosphatidylserine synthase family; activity or role: CDP-diacylglycerol-serine O-phosphatidyltransferase activity)
  - 2. phosphatidylethanolamine formation
  - Psd-dependent phosphatidylethanolamine formation
    - Psd phosphatidylserine decarboxylase activity (molecular player: type-I phosphatidylserine decarboxylase family; activity or role: phosphatidylserine decarboxylase activity)

### Known Relationships Among Steps

- PssA-dependent phosphatidylserine formation feeds into Psd-dependent phosphatidylethanolamine formation: PssA supplies phosphatidylserine to Psd.

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

# Module Review: Bacterial Phosphatidylethanolamine Biosynthesis through Phosphatidylserine in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** KEGG ppu00564 "Glycerophospholipid metabolism" (module area: lipid/cell-envelope metabolism)
**Module under review:** Two-reaction bacterial PE-via-PS module — PssA (CDP-diacylglycerol–serine *O*-phosphatidyltransferase, EC 2.7.8.8) → Psd (phosphatidylserine decarboxylase, EC 4.1.1.65)
**Evidence cut-off / access date:** 2026-07. All target-strain molecular evidence is homology-based (electronic, IEA); no direct KT2440 biochemistry exists for these enzymes.

---

## Summary

The canonical bacterial route to phosphatidylethanolamine (PE) proceeds in two enzymatic steps from CDP-diacylglycerol (CDP-DAG): a phosphatidylserine synthase (PssA/Pss, EC 2.7.8.8) condenses CDP-DAG with L-serine to yield phosphatidylserine (PS), and a pyruvoyl-dependent phosphatidylserine decarboxylase (Psd, EC 4.1.1.65) decarboxylates PS to PE. **This module is satisfiable and should be marked COVERED in *P. putida* KT2440.** Both steps are encoded, and PE is a major, actively synthesized membrane phospholipid across the genus ([PMID: 30217149](https://pubmed.ncbi.nlm.nih.gov/30217149/)), consistent with an operative module.

**Step 2 (PS → PE) is unambiguous.** A single high-confidence gene, `psd`/PP_4908 (Q88DB9), carries the specific reaction, the PSD-B "prokaryotic type I" pyruvoyl-zymogen family assignment, and an explicit UniRule pathway annotation ("phosphatidylethanolamine from CDP-diacylglycerol: step 2/2"). There is no paralog ambiguity for this step.

**Step 1 (CDP-DAG + serine → PS) is covered but paralog-ambiguous.** KT2440 encodes **two genuine phosphatidylserine synthases of different structural families**: (i) PP_3664 (Q88GQ4, gene-named `pssA`), a Class-I peripheral-membrane, phospholipase-D (PLD) superfamily enzyme that is a 1:1 KEGG ortholog (K00998) of the biochemically characterized *E. coli* PssA; and (ii) PP_4677 (Q88DZ1), a Class-II integral-membrane CDP-alcohol phosphatidyltransferase that carries the serine-specific InterPro family IPR004533. Both architecture nodes in the generic module ("Class-I peripheral-membrane PssA" and "Class-II integral-membrane PssA") are therefore represented. The remaining open question is not enzyme *identity* but *dominance* — which paralog carries physiological flux — a redundancy/knockout question, not a satisfiability gap. Because most bacteria maintain only one PSS, this dual-paralog situation is itself notable and warrants gene-level review.

The candidate list of 23 genes is dominated by **neighbors of the module, not members of it**. Only 2 of the 23 genes encode the two module reactions. The rest belong to adjacent branches of glycerophospholipid metabolism (CDP-DAG supply, phosphatidylglycerol/cardiolipin, phosphatidylcholine via Pcs, glycerol-3-phosphate supply, lipid turnover), and two (`eutB`/`eutC`) are ethanolamine **catabolism**, unrelated to PE biosynthesis. These should be excluded from the module. `PP_3664`, `PP_4677`, and `psd`/`PP_4908` should be promoted to full `fetch-gene` review.

---

## Key Findings

### F1 — The PE-via-PS module is satisfiable: both enzymatic steps are encoded

Both committed reactions map cleanly onto KT2440 genes by UniProt/InterPro annotation. For Step 1 (PS synthesis, EC 2.7.8.8), PP_4677/Q88DZ1 carries the specific reaction "CDP-1,2-diacyl-sn-glycerol + L-serine = phosphatidyl-L-serine + CMP," the serine-specific InterPro signature IPR004533 (CDP-diacylglycerol–serine *O*-phosphatidyltransferase), Pfam PF01066 (CDP-OH_P_transf), and an integral-membrane topology. For Step 2 (PS decarboxylation, EC 4.1.1.65), PP_4908/Q88DB9 (`psd`) is annotated FUNCTION "Catalyzes the formation of phosphatidylethanolamine from phosphatidylserine," PATHWAY "phosphatidylethanolamine from CDP-diacylglycerol: step 2/2," family "phosphatidylserine decarboxylase, PSD-B subfamily, prokaryotic type I," and is a pyruvoyl zymogen (Pfam PF02666). Both annotations are UniProt evidence level 3 (inferred from homology). This satisfiability is biologically expected: *"The exogenously supplied fatty acids were incorporated into the major bacterial phospholipids phosphatidylethanolamine and phosphatidylglycerol"* ([PMID: 30217149](https://pubmed.ncbi.nlm.nih.gov/30217149/)), confirming PE is a major, actively synthesized phospholipid in *Pseudomonas*.

### F2 — Two genes are annotated as phosphatidylserine synthase, and they belong to different enzyme superfamilies

The paralog ambiguity at Step 1 is real and structural. PP_4677/Q88DZ1 has the explicit EC 2.7.8.8 reaction plus the specific InterPro IPR004533 and PF01066 — an integral-membrane CDP-alcohol phosphatidyltransferase-superfamily enzyme (the *Bacillus*/yeast Class-II PSS architecture). PP_3664/Q88GQ4, which is the gene actually *named* `pssA`, has **no** catalytic reaction annotated (generic keywords only) and belongs to the **phospholipase D (PLD) superfamily** (Pfam PF13091 PLDc_2; InterPro IPR001736, IPR016270 PGS1) — the *E. coli* Class-I PSS architecture. Notably, the gene bearing the `pssA` name is the more weakly reaction-annotated of the two, while the un-named PP_4677 carries the explicit reaction — a classic curation inversion.

### F3 — KEGG orthology resolves identity: PP_3664 is the 1:1 ortholog of the characterized *E. coli* PssA

KEGG orthology assigns PP_3664 to **K00998** together with *E. coli* b2585 (`pssA`) — the biochemically characterized peripheral-membrane, PLD-superfamily (Class-I) phosphatidylserine synthase. PP_4677 is assigned to a different KO, **K17103**, whose members include *S. cerevisiae* CHO1, *B. subtilis* BSU02270 (`pssA`), *P. aeruginosa* PA4693 (`pssA`), and — critically — *P. putida*'s own PP_0731 (`pcs`, phosphatidylcholine synthase). KEGG assigns the cardiolipin synthases `clsA`/`clsB` to a separate KO (K06131), so PP_3664 is **not** a mis-called cardiolipin synthase. This orthology is the single strongest line of evidence that PP_3664 is an operative PSS, and it complements (rather than competes with) the family-level evidence for PP_4677.

### F4 — PP_4677 is serine-specific: it carries an InterPro family that the choline enzyme lacks

The breadth of KO K17103 (which mixes serine- and choline-specific members) initially cast doubt on PP_4677's specificity. The InterPro **family**-level entry IPR004533 resolves it. IPR004533 is named "CDP-diacylglycerol–serine *O*-phosphatidyltransferase" (i.e., serine-specific PSS). PP_4677/Q88DZ1 carries IPR004533 (plus IPR050324, IPR000462, IPR043130, IPR048254). The choline enzyme `pcs`/PP_0731 carries only the generic CDP-alcohol phosphotransferase signatures (IPR000462, IPR043130) plus an MFS transporter domain (IPR036259) and **lacks** IPR004533. Thus, although KEGG lumps PP_4677 and `pcs` in the broad KO K17103, the InterPro family assignment discriminates them: PP_4677 is serine-specific and a genuine second PSS.

### F5 — `pcs` (PP_0731) is a bona fide phosphatidylcholine synthase, reinforcing the PC/PS branch separation

Species-level experimental evidence shows PP_0731's ortholog is a PC synthase, not a PSS. In *P. putida* A ATCC 12633, the `pcs` gene was cloned and a `pcs`-deletion mutant produced no detectable phosphatidylcholine: *"In the pcs-deficient mutant, PC could not be detected, whereas the mutant could be successfully complemented and expressed the enzyme, indicating that PC synthesis occurs exclusively via the PCS pathway in this organism"* ([PMID: 22343357](https://pubmed.ncbi.nlm.nih.gov/22343357/)). The Pcs reaction uses choline, not serine: *"In the PCS pathway, choline is condensed directly with CDP-diacylglyceride to form PC in a reaction catalysed by PCS"* ([PMID: 14663079](https://pubmed.ncbi.nlm.nih.gov/14663079/)); the *P. aeruginosa* Pcs is likewise biochemically characterized ([PMID: 12169604](https://pubmed.ncbi.nlm.nih.gov/12169604/)). Because KEGG co-locates `pcs` and PP_4677 in K17103, `pcs` is the nearest false-positive risk for Step 1 — and IPR004533 is the discriminator that keeps them correctly separated.

### F6 — PP_3664 shows PLD-superfamily GO over-propagation; all target-strain evidence is electronic

PP_3664/Q88GQ4 (442 aa, comparable to *E. coli* PssA ~451 aa) carries three mutually broad GO terms — GO:0003882 (CDP-diacylglycerol–serine *O*-phosphatidyltransferase, from UniProtKB-EC), GO:0008444 (CDP-diacylglycerol–glycerol-3-phosphate 3-phosphatidyltransferase / PGP synthase, from InterPro), and GO:0032049 (cardiolipin biosynthetic process, from InterPro) — reflecting the shared PLD-superfamily signature. This is over-propagation: the KEGG K00998 placement (distinct from cardiolipin K06131) argues the PSS reading is correct and the PGP/cardiolipin terms are superfamily artifacts. By contrast, PP_4677/Q88DZ1 (283 aa) has a cleaner set (GO:0003882 PSS + membrane) and PP_4908/`psd` (287 aa) is clean (GO:0004609 PSD, GO:0006646 PE biosynthesis, from UniProtKB-UniRule). Every GO evidence code is IEA; UniProt protein-existence for all three is level 3 (homology) or 4 (predicted).

### F7 — Most candidate genes are module neighbors, and `eutBC` is unrelated catabolism

Of the 23 candidate genes in the ppu00564 bucket, only 2 define the PE-via-PS module. The rest belong to adjacent branches: CDP-DAG supply (`cdsA`/PP_1596, EC 2.7.7.41); the PG/cardiolipin branch (`pgsA`/PP_4097, `pgpA`/PP_0520, `clsA`/PP_5364, `clsB`/PP_3264); the PC branch (`pcs`/PP_0731); G3P supply (`gpsA`/PP_4169, `glpD`/PP_1073); ppu00561 acyltransferases (`plsB`, `plsY`, `plsC`, `PP_0058`); and lipid recycling/turnover (`dgkA-I/II`, `ugpQ`, `pchP`, `PP_0892`, `PP_5276`). Critically, `eutB`/PP_0543 and `eutC`/PP_0542 (ethanolamine ammonia-lyase, EC 4.3.1.7) are ethanolamine **catabolism**, pulled into the bucket only by the broad KEGG map, and must be excluded from any PE-biosynthesis interpretation.

---

## Mechanistic Model / Interpretation

The two-reaction module in KT2440 is best drawn as:

```
                         CDP-diacylglycerol  (from cdsA / PP_1596)
                                   │
              ┌────────────────────┼────────────────────┐
              │ + L-serine         │ + glycerol-3-P      │ + choline
              ▼                    ▼                     ▼
   ┌──── STEP 1: PssA ────┐    pgsA→pgpA→cls          pcs / PP_0731
   │  EC 2.7.8.8          │    (PG / cardiolipin)     (PC branch)
   │                      │
   │  PP_3664 (Class-I,   │   ← 1:1 ortholog of E. coli PssA (K00998),
   │   PLD superfamily,   │     PLD fold, but blank reaction field +
   │   peripheral)        │     over-propagated PGP/cardiolipin GO
   │                      │
   │  PP_4677 (Class-II,  │   ← serine-specific InterPro IPR004533
   │   CDP-alcohol PTase, │     (absent from pcs); explicit EC 2.7.8.8
   │   integral)          │     reaction; K17103 (broad KO)
   └──────────┬───────────┘
              ▼
        phosphatidyl-L-serine (PS)
              │
   ┌──── STEP 2: Psd ─────┐
   │  EC 4.1.1.65         │   PP_4908 (psd, K01613): pyruvoyl zymogen,
   │  pyruvoyl-dependent  │   PSD-B prokaryotic type I, UniRule
   └──────────┬───────────┘   "PE from CDP-DAG: step 2/2" — CLEAN
              ▼
       phosphatidylethanolamine (PE)  → major Pseudomonas membrane lipid
```

The interpretation is that KT2440 satisfies **both** alternative Step-1 architecture nodes of the generic module simultaneously — an unusual configuration, since most bacteria carry a single PSS class. PP_3664 and PP_4677 are supported by *different, complementary* evidence types: PP_3664 by clean orthology to a characterized enzyme, PP_4677 by a serine-specific protein family and an explicit reaction. This complementarity is reassuring for the *reality* of both enzymes but leaves *primacy* unresolved. Curators should therefore mark Step 1 covered with a **dominance/redundancy flag**, not an identity flag. Step 2 rests on a single clean gene and is high-confidence.

| Feature | PP_3664 (`pssA`) | PP_4677 | psd / PP_4908 |
|---|---|---|---|
| Step | 1 (PS formation) | 1 (PS formation) | 2 (PE formation) |
| Length | 442 aa | 283 aa | 287 aa |
| Architecture | Peripheral (Class I) | Integral (Class II) | Pyruvoyl zymogen |
| Superfamily / fold | PLD (PF13091) | CDP-alcohol PTase (PF01066) | PSD-B type I (PF02666) |
| KEGG KO | K00998 (1:1 *E. coli* PssA) | K17103 (broad; incl. pcs, CHO1) | K01613 |
| Serine-specific IPR004533 | — | **Yes** | n/a |
| Explicit EC reaction in UniProt | No (keywords only) | **Yes** | Yes |
| GO over-propagation | **Yes** (PSS + PGP + cardiolipin) | No | No |
| Curation verdict | Covered candidate | Covered candidate | Covered (high confidence) |

---

## Evidence Base

| PMID | How it supports / challenges the findings |
|---|---|
| [30217149](https://pubmed.ncbi.nlm.nih.gov/30217149/) | *Pseudomonas aeruginosa responds to exogenous PUFAs...* — *"exogenously supplied fatty acids were incorporated into the major bacterial phospholipids phosphatidylethanolamine and phosphatidylglycerol."* Confirms PE is a major, actively synthesized phospholipid, supporting an operative PE module (genus-level; strong relevance). |
| [22343357](https://pubmed.ncbi.nlm.nih.gov/22343357/) | *The phosphatidylcholine synthase of Pseudomonas putida A ATCC 12633...* — direct *P. putida* deletion evidence that `pcs` encodes a functional PC synthase (*"PC could not be detected... PC synthesis occurs exclusively via the PCS pathway"*). Anchors exclusion of `pcs` from the PS/PE module (species-level; strong). |
| [14663079](https://pubmed.ncbi.nlm.nih.gov/14663079/) | *Pathways for phosphatidylcholine biosynthesis in bacteria* — defines the Pcs reaction (*"choline is condensed directly with CDP-diacylglyceride to form PC"*), establishing that Pcs uses a different head group than PssA, supporting branch separation. |
| [12169604](https://pubmed.ncbi.nlm.nih.gov/12169604/) | *Pseudomonas aeruginosa synthesizes phosphatidylcholine by use of the PC synthase pathway* — biochemical characterization of *Pseudomonas* Pcs, reinforcing that PC synthesis is Pcs-dependent and distinct from PS synthesis. |
| [23886927](https://pubmed.ncbi.nlm.nih.gov/23886927/), [21939372](https://pubmed.ncbi.nlm.nih.gov/21939372/), [21866698](https://pubmed.ncbi.nlm.nih.gov/21866698/) | Additional *Pseudomonas* `pcs` genetics reinforcing that PC synthesis is Pcs-dependent (neighbor branch). |
| [25265483](https://pubmed.ncbi.nlm.nih.gov/25265483/) | *Pseudomonas aeruginosa* biofilm lipidome — documents PE as a principal membrane phospholipid, contextualizing the branch architecture. |

**Database evidence (all IEA / homology):** UniProt Q88GQ4 (PP_3664), Q88DZ1 (PP_4677), Q88DB9 (PP_4908/psd), Q88PW7 (PP_0731/pcs). InterPro IPR004533 (serine-specific PSS family), IPR001736/IPR016270 (PLD superfamily), Pfam PF01066, PF13091, PF02666. KEGG orthologs K00998 (Class-I PssA = PP_3664), K17103 (broad Class-II/choline KO = PP_4677 + pcs), K01613 (psd), K06131 (cardiolipin synthase).

---

## Module and GO-Curation Recommendations

| Module element | Recommended status | Rationale |
|---|---|---|
| Step 1 — PS formation (overall) | **covered** | ≥1 credible PssA present |
| Step 1 — Class-I peripheral PssA | **covered (candidate)** → PP_3664 | *E. coli*-type ortholog (K00998) |
| Step 1 — Class-II integral PssA | **covered (candidate)** → PP_4677 | serine-specific IPR004533 (absent from pcs); dominance vs PP_3664 unresolved |
| Step 2 — PE formation (Psd) | **covered** (high confidence) | PP_4908, clean UniRule annotation |
| Module boundaries | **scoping note** (module itself correct) | Exclude eutBC, pcs, PG/CL, precursor and turnover genes; cdsA = input, not a step |

**Boundary verdict:** the generic two-reaction module boundaries are correct in principle; only the local KEGG bucket over-includes neighbors. No change to the module document is needed — only correct gene→step mapping. The generic module's existing "alternative architecture" node (Class-I / Class-II) already accommodates KT2440's dual-paralog situation, so no new module document is required.

**GO-curation requests:** (1) Prune PP_3664 GO:0008444 (PGP synthase) and GO:0032049 (cardiolipin) as PLD-fold over-propagation; retain GO:0003882 (PSS). (2) Add a species note that KT2440 carries both Class-I and Class-II PSS families. (3) No new GO term is necessary — GO:0003882 (PSS) and GO:0004609 (PSD) suffice.

---

## Genes to Promote to Full `fetch-gene` Review

1. **PP_3664 (`pssA`)** — HIGH priority. Confirm as the operative Class-I PSS (K00998 ortholog of characterized *E. coli* PssA); correct the blank reaction field; prune over-propagated PGP/cardiolipin GO.
2. **PP_4677** — HIGH priority. Serine specificity is supported by IPR004533 (absent from `pcs`); confirm as the operative Class-II PSS and resolve dominance/redundancy vs PP_3664. Set the primary annotation and avoid conflation with `pcs` (shared KO K17103).
3. **`psd` / PP_4908** — LOW / optional. Clean; promote only to attach the module-step assertion formally so the module does not rest on a single unreviewed gene.
4. (Reference only) **`pcs` / PP_0731** — ensure it is filed under the PC module, not PE-via-PS; it is the nearest Step-1 false positive.

---

## Limitations and Knowledge Gaps

- **No direct KT2440 experiments** exist for PssA or Psd. Every conclusion for the target strain is homology inference (IEA; protein-existence level 3–4). The strongest experimental evidence in the dossier concerns the *neighboring* PC branch (`pcs`), not the module itself.
- **Paralog dominance is unresolved.** Sequence alone cannot say which of PP_3664/PP_4677 carries PS flux in vivo, whether they are redundant, or whether one is conditional/cryptic.
- **Orthology-vs-family tension.** PP_3664 wins on orthology (K00998) but PP_4677 wins on explicit reaction + serine-specific family (IPR004533). Both are supported, which is reassuring for their reality but leaves primacy open.
- **KEGG KO breadth (K17103)** mixes serine- and choline-specific members, so KO membership alone was insufficient to call PP_4677; the InterPro family (IPR004533) was required to discriminate it from `pcs`.
- **Species transfer:** *E. coli* PssA → PP_3664 is a *strong* functional inference (clear orthology); ATCC 12633/PAO1 Pcs → PP_0731 is *strong* (same species/genus) but concerns the PC neighbor, not PE. No transfer establishes which PSS paralog is dominant in KT2440.

---

## Proposed Follow-up Experiments / Actions

1. **Single and double knockouts** of PP_3664 and PP_4677 in KT2440 with lipidomic (PS/PE) readout — the definitive test of which paralog is functional and whether they are redundant. A viable double-null with abolished PE would falsify both; a viable single-null would rank dominance.
2. **Heterologous complementation** of an *E. coli* `pssA`-null with each KT2440 paralog to confirm PS-synthase activity individually.
3. **Curator resolution of PP_3664 GO** — down-weight GO:0008444 (PGP synthase) and GO:0032049 (cardiolipin) as PLD-superfamily over-propagation; retain GO:0003882 (PSS), consistent with K00998.
4. **Promote PP_3664, PP_4677, and PP_4908** to full `fetch-gene` review; keep `pcs`/PP_0731 flagged as the nearest Step-1 false positive.
5. **Bucket hygiene:** remove `eutB`/`eutC` (ethanolamine catabolism) from any PE-biosynthesis interpretation of ppu00564.
6. **Expression/proteomics check** (RNA-seq or proteomics under standard growth) to see whether one paralog is the constitutively expressed PSS and the other conditionally induced.

---

*Module verdict: **COVERED** with a Step-1 paralog-dominance flag. Step 2 (psd/PP_4908) is high-confidence; Step 1 is covered by two genuine PSS paralogs (Class-I PP_3664, K00998; Class-II PP_4677, IPR004533). All target-strain evidence is homology-based (IEA); no direct KT2440 biochemistry.*


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_phosphatidylethanolamine_biosynthesis__ppu00564-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_phosphatidylethanolamine_biosynthesis__ppu00564-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:30217149
2. PMID:22343357
3. PMID:14663079
4. PMID:12169604