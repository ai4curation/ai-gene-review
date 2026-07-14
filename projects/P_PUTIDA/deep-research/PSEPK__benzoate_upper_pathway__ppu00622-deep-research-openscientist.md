---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-13T11:33:07.385362'
end_time: '2026-07-13T11:58:37.330326'
duration_seconds: 1529.95
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Benzoate upper degradation pathway
  module_summary: A reusable bacterial aromatic-catabolism module for the upper benzoate
    degradation route that converts benzoate to catechol. The pathway begins with
    a multicomponent benzoate 1,2-dioxygenase system, represented here by BenA-like
    large oxygenase, BenB-like small oxygenase, and BenC-like reductase roles, and
    is followed by a BenD-like cis-diol dehydrogenase. Pseudomonas putida KT2440 benA/benB/benC/benD
    provide the local PSEPK exemplars for this module, but the module boundary is
    the conserved benzoate-to-catechol pathway segment rather than a PSEPK-specific
    locus definition.
  module_outline: "- Benzoate to catechol upper pathway\n  - 1. benzoate dioxygenation\
    \ to a cis-dihydrodiol\n  - BenABC benzoate dioxygenation\n    - Benzoate 1,2-dioxygenase\
    \ large oxygenase subunit (molecular player: benzoate 1,2-dioxygenase large subunit\
    \ family; activity or role: benzoate 1,2-dioxygenase activity)\n    - Benzoate\
    \ 1,2-dioxygenase small oxygenase subunit (molecular player: benzoate 1,2-dioxygenase\
    \ small subunit family; activity or role: contributes to benzoate 1,2-dioxygenase\
    \ activity)\n    - Benzoate dioxygenase reductase/electron-transfer component\
    \ (molecular player: BenC-like FAD/NAD-binding reductase family; activity or role:\
    \ ferredoxin-NAD+ reductase activity)\n  - 2. cis-dihydrodiol dehydrogenation\
    \ to catechol\n  - BenD cis-diol dehydrogenation\n    - Benzoate cis-dihydrodiol\
    \ dehydrogenase (molecular player: BenD dehydrogenase family; activity or role:\
    \ 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase activity)"
  module_connections: '- BenABC benzoate dioxygenation precedes BenD cis-diol dehydrogenation:
    The cis-dihydrodiol produced by BenABC is the substrate for BenD.'
  pathway_query: ppu00622
  pathway_id: ppu00622
  pathway_name: Xylene degradation
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00622 with 4 primary genes; module
    area: aromatic_and_xenobiotic_catabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '6'
  candidate_genes: '- PP_1791: PP_1791 | Q88LY5 | Aldolase/synthase (primary bucket
    kegg:ppu00621)

    - PP_2504: PP_2504 | Q88JY9 | 2-hydroxymuconate tautomerase (EC 5.3.2.6) (4-oxalocrotonate
    tautomerase) (EC 5.3.2.6; primary bucket kegg:ppu00621)

    - benA: PP_3161 | Q88I40 | Benzoate 1,2-dioxygenase subunit alpha (EC 1.14.12.10)
    (EC 1.14.12.10; primary bucket kegg:ppu00622)

    - benB: PP_3162 | Q88I39 | Benzoate 1,2-dioxygenase subunit beta (EC 1.14.12.10)
    (EC 1.14.12.10; primary bucket kegg:ppu00622)

    - benC: PP_3163 | Q88I38 | Benzoate 1,2-dioxygenase electron transfer component
    (EC 1.14.12.10, EC 1.18.1.3) (EC 1.14.12.10; 1.18.1.3; primary bucket kegg:ppu00622)

    - benD: PP_3164 | Q88I37 | 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase
    (EC 1.3.1.25) (EC 1.3.1.25; primary bucket kegg:ppu00622)'
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
citation_count: 6
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__benzoate_upper_pathway__ppu00622-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__benzoate_upper_pathway__ppu00622-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Benzoate upper degradation pathway in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00622
- Resolved ID: ppu00622
- Resolved name: Xylene degradation
- Source: KEGG

Resolved local bucket kegg:ppu00622 with 4 primary genes; module area: aromatic_and_xenobiotic_catabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 6

- PP_1791: PP_1791 | Q88LY5 | Aldolase/synthase (primary bucket kegg:ppu00621)
- PP_2504: PP_2504 | Q88JY9 | 2-hydroxymuconate tautomerase (EC 5.3.2.6) (4-oxalocrotonate tautomerase) (EC 5.3.2.6; primary bucket kegg:ppu00621)
- benA: PP_3161 | Q88I40 | Benzoate 1,2-dioxygenase subunit alpha (EC 1.14.12.10) (EC 1.14.12.10; primary bucket kegg:ppu00622)
- benB: PP_3162 | Q88I39 | Benzoate 1,2-dioxygenase subunit beta (EC 1.14.12.10) (EC 1.14.12.10; primary bucket kegg:ppu00622)
- benC: PP_3163 | Q88I38 | Benzoate 1,2-dioxygenase electron transfer component (EC 1.14.12.10, EC 1.18.1.3) (EC 1.14.12.10; 1.18.1.3; primary bucket kegg:ppu00622)
- benD: PP_3164 | Q88I37 | 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase (EC 1.3.1.25) (EC 1.3.1.25; primary bucket kegg:ppu00622)

## Generic Module Context

### Working Scope

A reusable bacterial aromatic-catabolism module for the upper benzoate degradation route that converts benzoate to catechol. The pathway begins with a multicomponent benzoate 1,2-dioxygenase system, represented here by BenA-like large oxygenase, BenB-like small oxygenase, and BenC-like reductase roles, and is followed by a BenD-like cis-diol dehydrogenase. Pseudomonas putida KT2440 benA/benB/benC/benD provide the local PSEPK exemplars for this module, but the module boundary is the conserved benzoate-to-catechol pathway segment rather than a PSEPK-specific locus definition.

### Provisional Biological Outline

- Benzoate to catechol upper pathway
  - 1. benzoate dioxygenation to a cis-dihydrodiol
  - BenABC benzoate dioxygenation
    - Benzoate 1,2-dioxygenase large oxygenase subunit (molecular player: benzoate 1,2-dioxygenase large subunit family; activity or role: benzoate 1,2-dioxygenase activity)
    - Benzoate 1,2-dioxygenase small oxygenase subunit (molecular player: benzoate 1,2-dioxygenase small subunit family; activity or role: contributes to benzoate 1,2-dioxygenase activity)
    - Benzoate dioxygenase reductase/electron-transfer component (molecular player: BenC-like FAD/NAD-binding reductase family; activity or role: ferredoxin-NAD+ reductase activity)
  - 2. cis-dihydrodiol dehydrogenation to catechol
  - BenD cis-diol dehydrogenation
    - Benzoate cis-dihydrodiol dehydrogenase (molecular player: BenD dehydrogenase family; activity or role: 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase activity)

### Known Relationships Among Steps

- BenABC benzoate dioxygenation precedes BenD cis-diol dehydrogenation: The cis-dihydrodiol produced by BenABC is the substrate for BenD.

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

# Module/Pathway/Taxon Review: Benzoate Upper Degradation Pathway in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (organism code PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket (commissioned):** KEGG `ppu00622` — resolved name "Xylene degradation"
**Module area:** aromatic_and_xenobiotic_catabolism
**Working module:** benzoate → catechol upper degradation route (BenABC dioxygenation + BenD cis-diol dehydrogenation)

---

## 1. Executive Summary

The benzoate upper-degradation module — conversion of benzoate to catechol — is **fully satisfiable** in *Pseudomonas putida* KT2440. All four expected enzymatic roles are encoded by a single contiguous chromosomal operon: **benA (PP_3161), benB (PP_3162), benC (PP_3163), and benD (PP_3164)**. These map cleanly to KEGG orthologs K05549 (benA, benzoate 1,2-dioxygenase α subunit, EC 1.14.12.10), K05550 (benB, β subunit), K05784 (benC, reductase/electron-transfer component, EC 1.18.1.-), and K05783 (benD, 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase, EC 1.3.1.25). Both defined module steps — (1) BenABC multicomponent benzoate 1,2-dioxygenation to the cis-1,2-dihydrodiol, and (2) BenD dehydrogenation/decarboxylation to catechol — are covered by high-confidence candidates with **no gaps and no module-internal paralog ambiguity** (all four subunits are single-copy).

The single most important curation correction concerns the commissioned bucket label. KEGG `ppu00622` is titled "Xylene degradation," but this is a **map artifact for KT2440**. KT2440 is a plasmid-free derivative of *P. putida* mt-2 that lacks the pWW0/TOL plasmid and therefore lacks the *xyl* meta-cleavage genes that define genuine xylene/toluene catabolism. In KT2440, benzoate is instead funneled through the **chromosomal ortho (β-ketoadipate) pathway**: benABCD produce catechol, which is immediately committed by CatA catechol 1,2-dioxygenase (PP_3166) within the same gene cluster. The ben genes natively belong to KEGG `ppu00362` (Benzoate degradation). The bucket should be relabeled accordingly, and genuine xylene/TOL meta-pathway steps should be marked *not_expected_in_target_taxon*.

The module is not merely a homology prediction. Direct in-strain proteomics (Kim et al. 2006, [PMID: 16470664](https://pubmed.ncbi.nlm.nih.gov/16470664/)) show that **BenA, BenD, and CatA proteins are benzoate-induced in KT2440**, elevating the module from "predicted" to "experimentally expressed" in the target strain. Two of the six commissioned candidate genes — **PP_1791 (K01666, 4-hydroxy-2-oxovalerate aldolase) and PP_2504 (K01821, 4-oxalocrotonate tautomerase)** — are meta-cleavage *lower*-pathway enzymes that were over-propagated into this bucket purely through shared EC/overview-map membership. They act downstream of ring cleavage, are chromosomally distant from benABCD, and cluster with no other meta-pathway genes. They should be **removed** from this module's candidate list.

---

## 2. Target-Organism Pathway Definition

### What the module includes

The module covers the **peripheral (upper) benzoate catabolic segment** that converts benzoate to catechol in two enzymatic steps:

1. **Benzoate 1,2-dioxygenation** — the three-component benzoate 1,2-dioxygenase (BenABC) incorporates both atoms of molecular O₂ into benzoate, yielding **benzoate cis-1,2-dihydrodiol (1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate)**. This is a class of Rieske non-heme iron oxygenases in which BenA (large/α, catalytic) and BenB (small/β) form the terminal oxygenase, and BenC is the FAD/NAD(P)H-dependent reductase/electron-transfer component that supplies reducing equivalents.
2. **cis-Diol dehydrogenation/decarboxylation** — BenD, an NAD⁺-dependent dehydrogenase, oxidizes and spontaneously decarboxylates the cis-dihydrodiol to give **catechol** plus CO₂ and NADH.

### Neighboring pathways to keep separate

- **Catechol ring cleavage and the β-ketoadipate pathway (`ppu00362` lower segment):** Catechol is the *product* boundary of this module. Its ortho cleavage by CatA (PP_3166) begins a distinct downstream module and should not be merged into the upper pathway.
- **Xylene/toluene (TOL) meta pathway (`ppu00622` genuine content):** In organisms carrying pWW0 (e.g., *P. putida* mt-2), toluene/xylene are oxidized to (methyl)benzoates by *xyl* upper-pathway genes, and (methyl)catechols are cleaved by *meta* (2,3-dioxygenase) enzymes. **KT2440 lacks this plasmid entirely.** The commissioned "xylene degradation" label therefore does not reflect a functional xylene pathway in the target strain.
- **Meta-cleavage lower pathway (2-oxopent-4-enoate branch):** Enzymes such as 4-oxalocrotonate tautomerase and 4-hydroxy-2-oxovalerate aldolase (the two spurious candidates) belong to this branch, downstream of *meta* ring cleavage, and are not part of the benzoate upper module.

### Alternate names and database definitions

| Database | Identifier | Name | Relevance to KT2440 |
|---|---|---|---|
| KEGG | ppu00622 | Xylene degradation | **Mislabeled for KT2440** — no pWW0 plasmid; artifact of EC/map propagation |
| KEGG | ppu00362 | Benzoate degradation | **Correct native map** for benABCD |
| KEGG | ppu00621 | Dioxin degradation | Where PP_1791/PP_2504 primary buckets sit (over-propagated) |
| Enzyme | EC 1.14.12.10 | Benzoate/toluate 1,2-dioxygenase | benA/benB catalytic activity |
| Enzyme | EC 1.3.1.25 | 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase | benD activity |

---

## 3. Expected Step Model

```
                    O2   NAD(P)H (via BenC reductase)
                     \        |
  benzoate ───────────[ BenA + BenB oxygenase ]──────────►  benzoate cis-1,2-dihydrodiol
   (PP_3161 benA α, catalytic Rieske center)                (1,6-dihydroxycyclohexa-2,4-
   (PP_3162 benB β)                                          diene-1-carboxylate)
   (PP_3163 benC reductase, [2Fe-2S]/FAD)
                                                                     |
                                                                     | NAD+  (BenD)
                                                                     ▼
                                              catechol  +  CO2  +  NADH
                                              (PP_3164 benD dehydrogenase)
                                                                     |
                                                                     ▼   [ downstream module boundary ]
                                              CatA (PP_3166) → cis,cis-muconate → β-ketoadipate → TCA
```

| Step | Role | Expected player | KT2440 candidate | KEGG KO | Status |
|---|---|---|---|---|---|
| 1a | Benzoate 1,2-dioxygenase large/α subunit | Rieske oxygenase catalytic subunit | **benA / PP_3161** | K05549 | **Covered** |
| 1b | Benzoate 1,2-dioxygenase small/β subunit | Oxygenase β subunit | **benB / PP_3162** | K05550 | **Covered** |
| 1c | Reductase / electron-transfer component | FAD/NAD, [2Fe-2S] reductase | **benC / PP_3163** | K05784 | **Covered** |
| 2 | cis-Dihydrodiol dehydrogenase | NAD⁺ dehydrogenase | **benD / PP_3164** | K05783 | **Covered** |

Genomic context (chromosomal locus ~3,581,930–3,585,749 bp): **benR (PP_3159, AraC/XylS activator)** — *benABCD (PP_3161–3164)* — **benK (PP_3165, MFS transporter)** — **catA (PP_3166, catechol 1,2-dioxygenase)**. This intact operon organization is itself strong contextual evidence that all four steps are functionally coupled and channel benzoate into the ortho route.

---

## 4. Candidate Genes and Evidence

### High-confidence module genes (retain)

**benA — PP_3161 (Q88I40).** Benzoate 1,2-dioxygenase α (large) subunit, EC 1.14.12.10, KEGG K05549. Single-copy (K05549 → only PP_3161). UniProt protein existence PE3 (inferred from homology). Directly supported by KT2440 proteomics: BenA is benzoate-induced ([PMID: 16470664](https://pubmed.ncbi.nlm.nih.gov/16470664/)). **Curation caveat:** the EC 1.14.12.10 assignment is shared with *toluate* 1,2-dioxygenase (xylXYZ of the TOL system); the enzyme has documented activity on both benzoate and 3-methylbenzoate. This benzoate-vs-toluate substrate ambiguity is worth noting but does not affect module satisfiability, since benzoate is the physiological substrate in KT2440.

**benB — PP_3162 (Q88I39).** Benzoate 1,2-dioxygenase β (small) subunit, EC 1.14.12.10, KEGG K05550. Single-copy. UniProt PE3. Same benzoate/toluate EC ambiguity as benA.

**benC — PP_3163 (Q88I38).** Benzoate dioxygenase reductase/electron-transfer component, EC 1.14.12.10 / 1.18.1.3, KEGG K05784. Single-copy. **UniProt PE4 (predicted) — the lowest evidence tier among the four ben genes;** annotated with a [2Fe-2S] cluster cofactor. This is the weakest-evidence candidate and the priority for full gene-level review.

**benD — PP_3164 (Q88I37).** 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase, EC 1.3.1.25, KEGG K05783. Single-copy. UniProt PE3. Directly supported by KT2440 proteomics: BenD is benzoate-induced ([PMID: 16470664](https://pubmed.ncbi.nlm.nih.gov/16470664/)).

### Candidates to remove (over-propagated)

**PP_1791 (Q88LY5).** Annotated "Aldolase/synthase"; KEGG K01666 = 4-hydroxy-2-oxovalerate aldolase (EC 4.1.3.39). Natively mapped to `ppu00360` (phenylalanine metabolism). It acts on 4-hydroxy-2-oxovalerate — a *meta*-cleavage lower-pathway intermediate, downstream of catechol ring cleavage — not on benzoate or its dihydrodiol. Located ~2.0 Mb from benABCD. Its genomic neighborhood is a sugar/glycan region (glycosyltransferases PP_1792/1793, acylneuraminate cytidylyltransferase PP_1790, HAD hydrolase PP_1789) with **no** other meta-pathway genes. Multi-mapping into `ppu00622` is purely EC-driven overview-map propagation.

**PP_2504 (Q88JY9).** 2-hydroxymuconate/4-oxalocrotonate tautomerase, EC 5.3.2.6; KEGG K01821. Acts on 2-hydroxymuconate, a *meta*-cleavage intermediate. Located ~2.85 Mb from benABCD. Flanked by a phage integrase (PP_2501), a LysR regulator (PP_2502), a 3-oxoacyl-ACP reductase (PP_2503), and a GGDEF/GAF protein (PP_2505) — an isolated EC-mapped singleton with no meta-cleavage operon context.

### Summary table

| Gene | Locus | UniProt | KO | Evidence type | Verdict |
|---|---|---|---|---|---|
| benA | PP_3161 | Q88I40 (PE3) | K05549 | Homology + proteomic induction (in-strain) | **Retain — covered** |
| benB | PP_3162 | Q88I39 (PE3) | K05550 | Homology + operon context | **Retain — covered** |
| benC | PP_3163 | Q88I38 (PE4) | K05784 | Homology (predicted); weakest tier | **Retain — promote to full review** |
| benD | PP_3164 | Q88I37 (PE3) | K05783 | Homology + proteomic induction (in-strain) | **Retain — covered** |
| PP_1791 | PP_1791 | Q88LY5 | K01666 | EC-map propagation only | **Remove — meta lower pathway** |
| PP_2504 | PP_2504 | Q88JY9 | K01821 | EC-map propagation only | **Remove — meta lower pathway** |

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

**No module-internal gaps.** Both expected steps are covered, and all four subunits are single-copy (K05549→PP_3161; K05550→PP_3162; K05784→PP_3163; K05783→PP_3164), so there is no paralog ambiguity *within* the module. Redundancy in the surrounding system is entirely downstream or peripheral: KT2440 carries **two catechol 1,2-dioxygenases** — catA-II (PP_3166, in the ben cluster) and catA-I (PP_3713, adjacent to catB muconate cycloisomerase PP_3715) — and **multiple benzoate transporters** (benK PP_3165; benE-family PP_2035, PP_1820, PP_3167). These do not affect upper-pathway satisfiability but are relevant when scoping the adjacent ring-cleavage and transport modules. No anthranilate 1,2-dioxygenase (antABC) is annotated by name in KT2440.

**Bucket label is wrong for this taxon.** The commissioned `ppu00622` "Xylene degradation" label does not describe a functional pathway in KT2440. The strain is plasmid-free (no pWW0/TOL), so the *xyl* meta upper- and meta-cleavage genes that constitute genuine xylene degradation are simply absent. Pérez-Pantoja et al. 2015 ([PMID: 24588992](https://pubmed.ncbi.nlm.nih.gov/24588992/)) describe the two mutually exclusive routes explicitly: "one meta pathway encoded by xyl genes of the pWW0 plasmid and mastered by the Pm promoter and XylS, and one chromosomally encoded ortho pathway initiated by Pben and the BenR protein." KT2440 has only the latter.

**EC-based over-annotation is the dominant artifact.** PP_1791 and PP_2504 illustrate a classic overview-map propagation failure: both are multi-mapped to `ppu00360/00362/00621/00622/01220/01100/01120` solely because their EC numbers appear on multiple aromatic-degradation maps, despite acting only on ring-cleavage lower-pathway intermediates and clustering with no relevant operon.

**Benzoate-vs-toluate EC ambiguity.** benA/benB carry EC 1.14.12.10, which covers both benzoate and toluate 1,2-dioxygenase activities. In organisms with the TOL plasmid these are distinct enzymes (chromosomal BenABC vs. plasmid XylXYZ); in KT2440 only the chromosomal benzoate enzyme exists, so the ambiguity is nominal but should be flagged during gene-level curation.

**In-strain biochemistry is indirect for the enzymology itself.** All four ben annotations are homology-inferred (PE3/PE4), and direct enzyme kinetics come from related systems — *Acinetobacter* benABCDE ([PMID: 18781356](https://pubmed.ncbi.nlm.nih.gov/18781356/)) and the *P. putida* mt-2 TOL toluate dioxygenase. KT2440-specific functional support rests on the intact operon, robust growth on benzoate, regulatory studies (BenR/Crc), and the proteomic induction data — strong but not a purified-enzyme demonstration in KT2440.

---

## 6. Module and GO-Curation Recommendations

| Module step | Recommended status | Rationale |
|---|---|---|
| BenABC benzoate dioxygenation | **covered** | benA/benB/benC single-copy K05549/K05550/K05784; BenA benzoate-induced in KT2440 |
| BenD cis-diol dehydrogenation | **covered** | benD single-copy K05783; BenD benzoate-induced in KT2440 |
| Xylene/TOL meta upper & meta-cleavage steps | **not_expected_in_target_taxon** | KT2440 is plasmid-free (no pWW0); *xyl* genes absent |

**Bucket action:** Relabel the local bucket from KEGG `ppu00622` "Xylene degradation" to `ppu00362` "Benzoate degradation" (benzoate→catechol upper segment). The "xylene" framing is a map artifact for this strain and should not drive module scoping.

**Candidate-list revision:** Remove **PP_1791 (K01666)** and **PP_2504 (K01821)** as isolated EC-mapped singletons belonging to the meta-cleavage lower pathway, not the benzoate upper module.

**Module boundary:** The generic benzoate→catechol boundary is **correct** for KT2440 and requires no revision. The downstream boundary (catechol → CatA ortho cleavage) is appropriate; keep the β-ketoadipate lower pathway as a separate module.

**GO terms:** **No new GO term requests are needed.** Existing terms adequately cover the roles: benzoate 1,2-dioxygenase activity (GO:0018619), ferredoxin-NAD⁺ reductase activity for BenC, and 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase activity for BenD.

---

## 7. Genes to Promote to Full Review

Priority order for `fetch-gene` promotion:

1. **benC / PP_3163** — highest priority. UniProt PE4 (predicted) is the lowest evidence tier among the four; the reductase/electron-transfer role and [2Fe-2S] cofactor annotation warrant direct verification.
2. **benA / PP_3161 and benB / PP_3162** — next. Confirm benzoate (vs. toluate) substrate assignment and resolve the shared EC 1.14.12.10 mapping.
3. **benD / PP_3164** — lower priority; PE3 with proteomic support, but full review would confirm the dehydrogenation/decarboxylation stoichiometry.

PP_1791 and PP_2504 should **not** be promoted within this module; if reviewed at all, they belong to meta-cleavage lower-pathway curation.

---

## 8. Mechanistic Model and Interpretation

The picture that emerges across five iterations is coherent and internally consistent. KT2440 handles benzoate through a **single, tightly organized chromosomal cassette** that both encodes and regulates the entire upper pathway plus the committed first step of ring cleavage:

```
  benR ──(activates on benzoate)──► Pben ──► [ benA benB benC benD | benK | catA ]
  PP_3159                                       3161  3162  3163  3164   3165   3166
   AraC/XylS                                    └── benzoate → catechol ──┘  transport  ortho cleavage
```

BenR, an AraC/XylS-family activator, senses benzoate and turns on the *ben* operon; the encoded BenABC dioxygenase and BenD dehydrogenase convert benzoate to catechol; BenK imports substrate; and CatA immediately commits catechol to *cis,cis*-muconate and the β-ketoadipate pathway feeding the TCA cycle. Kim et al.'s proteomic detection of BenA, BenD, and CatA co-induction by benzoate ([PMID: 16470664](https://pubmed.ncbi.nlm.nih.gov/16470664/)) confirms this cassette is expressed as a functional unit in vivo, and Jiménez et al.'s genome-wide map ([PMID: 12534466](https://pubmed.ncbi.nlm.nih.gov/12534466/)) places the *ben* peripheral pathway feeding the catechol branch of the β-ketoadipate pathway. Notably, the β-ketoadipate lower-pathway enzymes PcaF and PcaD were co-induced by benzoate, p-hydroxybenzoate, and vanillin — showing convergence of multiple peripheral routes into a common β-ketoadipate funnel.

The regulatory layer reinforces the ortho-only interpretation. The translational repressor **Crc** imposes catabolite repression on benR and on the first *ben* structural genes ([PMID: 22925411](https://pubmed.ncbi.nlm.nih.gov/22925411/)), and BenR's promoter architecture distinguishes benzoate from 3-methylbenzoate signaling ([PMID: 22588473](https://pubmed.ncbi.nlm.nih.gov/22588473/)). In mt-2 (pWW0⁺) strains, BenR and the plasmid XylS activator cross-talk to route toluene-derived benzoate correctly and avoid metabolic conflict ([PMID: 24588992](https://pubmed.ncbi.nlm.nih.gov/24588992/)) — but that cross-talk requires the plasmid that KT2440 lacks, which is exactly why KT2440's route is ortho-only and the "xylene" bucket is inapplicable.

The over-propagation of PP_1791 and PP_2504 is the mirror image of this cohesion: these genes are physically and functionally *outside* the cassette (2.0–2.85 Mb away, embedded in unrelated glycan and mobile-element neighborhoods) and enter the bucket only through EC-number map overlaps. Their exclusion sharpens the module to exactly the four genes that biology supports.

---

## 9. Evidence Base

| PMID | Title (abbrev.) | How it supports/challenges the review |
|---|---|---|
| [16470664](https://pubmed.ncbi.nlm.nih.gov/16470664/) | *Aromatic catabolic pathways in KT2440 by proteomics (2-DE/MS + ICAT)* | **Direct in-strain support.** "Benzoate dioxygenase (BenA, BenD) and catechol 1,2-dioxygenase (CatA) were induced by benzoate" — confirms the upper module is expressed and benzoate-inducible in KT2440. |
| [12534466](https://pubmed.ncbi.nlm.nih.gov/12534466/) | *Genomic analysis of aromatic catabolic pathways from KT2440* | Authoritative genome-wide map: the chromosomal *ben* peripheral pathway for benzoate feeds the β-ketoadipate pathway. Quote: "the genes encoding the peripheral pathways for the catabolism of p-hydroxybenzoate (pob), benzoate (ben), quinate (qui)." |
| [24588992](https://pubmed.ncbi.nlm.nih.gov/24588992/) | *Differential response of Pben to BenR and XylS in mt-2* | Establishes that the benzoate ortho route (BenR/Pben) is chromosomal and distinct from the plasmid-borne *xyl*/meta (xylene) pathway — the basis for relabeling ppu00622. |
| [18781356](https://pubmed.ncbi.nlm.nih.gov/18781356/) | *benABCDE cluster in Acinetobacter calcoaceticus PHEA-2* | Related-organism biochemical/genetic characterization of the benABCDE operon converting benzoate to catechol; supports the enzymatic model (transfer strength: moderate — different genus, same operon logic). |
| [22925411](https://pubmed.ncbi.nlm.nih.gov/22925411/) | *Crc controls benzoate and alkane catabolic pathways* | Regulatory context: Crc represses benR and the first ben structural genes in *P. putida*. |
| [22588473](https://pubmed.ncbi.nlm.nih.gov/22588473/) | *Broadening signal specificity of BenR-controlled Pb promoter* | BenR of KT2440 (AraC/XylS) activates Pb in response to benzoate/3-methylbenzoate — confirms benzoate as physiological inducer in the target strain. |
| [27046069](https://pubmed.ncbi.nlm.nih.gov/27046069/) | *Cross-talk between ortho-cleavage and TOL pathways in mt-2* | Illustrates ortho/meta cross-talk that requires pWW0 — absent in KT2440. |

**Evidence hierarchy for the module:**
- *Direct experimental (KT2440):* proteomic induction of BenA/BenD/CatA; robust growth on benzoate; BenR/Crc regulation.
- *Genomic/contextual (KT2440):* intact benR–benABCD–benK–catA operon; single-copy subunits; native KEGG mapping to ppu00362.
- *Homology transfer (related organisms):* purified-enzyme biochemistry from *Acinetobacter* benABCDE and mt-2 toluate dioxygenase.

---

## 10. Limitations and Knowledge Gaps

1. **No purified-enzyme kinetics in KT2440.** All four ben annotations are homology-inferred (PE3/PE4). Direct biochemical demonstration of benzoate 1,2-dioxygenase and cis-diol dehydrogenase activity in KT2440 protein has not been reported; kinetics derive from related systems.
2. **benC is the weakest link.** UniProt PE4 (predicted) status and its role as the electron-transfer component make it the least-verified subunit.
3. **Benzoate/toluate EC ambiguity** (EC 1.14.12.10) is unresolved at the annotation level for benA/benB, though physiologically benzoate is the substrate.
4. **Proteomic evidence covers BenA and BenD but not BenB or BenC directly** — these two subunits are supported by operon context and homology rather than in-strain detection.
5. **Transferred evidence caveat:** *Acinetobacter* benABCDE data are cross-genus; transfer to KT2440 is moderate (conserved operon architecture) but not definitive at the residue level.

---

## 11. Proposed Follow-up Actions

1. **Promote benC/PP_3163 to full `fetch-gene` review** (highest priority) to verify the reductase/electron-transfer assignment and [2Fe-2S] cofactor annotation; follow with benA/benB (resolve benzoate-vs-toluate EC) and benD.
2. **Execute the bucket relabel:** change local bucket from `ppu00622` "Xylene degradation" to `ppu00362` "Benzoate degradation"; mark xylene/TOL meta steps *not_expected_in_target_taxon*.
3. **Remove PP_1791 and PP_2504** from the benzoate upper module candidate list; reassign to meta-cleavage lower-pathway curation if needed.
4. **Confirm module status as fully covered** with no gaps; no new GO term requests required.
5. **Optional experimental resolution:** targeted proteomics/RNA-seq to confirm BenB and BenC induction in KT2440, and (if resources allow) heterologous expression + activity assay of BenABC and BenD to obtain direct KT2440 enzyme kinetics and settle the benzoate/toluate substrate question.

---

### Final curation verdict

The benzoate→catechol upper module is **fully satisfiable and experimentally supported** in *P. putida* KT2440 via the single-copy operon **benABCD (PP_3161–PP_3164)**. The commissioned bucket label "Xylene degradation" is a map artifact for this plasmid-free strain and should be corrected to Benzoate degradation; two candidates (PP_1791, PP_2504) are over-propagated meta-cleavage enzymes to be removed; and benC merits promotion to full gene-level review as the lowest-evidence subunit.


## Artifacts

- [OpenScientist final report](PSEPK__benzoate_upper_pathway__ppu00622-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__benzoate_upper_pathway__ppu00622-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:16470664
2. PMID:24588992
3. PMID:18781356
4. PMID:12534466
5. PMID:22925411
6. PMID:22588473