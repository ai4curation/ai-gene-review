---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-26T18:28:47.837797'
end_time: '2026-07-26T19:41:36.687226'
duration_seconds: 4368.85
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial choline uptake and glycine betaine biosynthesis
  module_summary: A reusable bacterial module for choline uptake followed by its two-step
    oxidation to the compatible solute glycine betaine. A BetT-family transporter
    imports choline, FAD-dependent BetA oxidizes choline to betaine aldehyde, and
    NAD-dependent BetB oxidizes the aldehyde to glycine betaine.
  module_outline: "- Bacterial choline uptake and glycine betaine biosynthesis\n \
    \ - 1. choline uptake\n  - BetT-dependent choline uptake\n    - BetT choline transporter\
    \ activity (molecular player: BetT-family choline transporter; activity or role:\
    \ choline transmembrane transporter activity)\n  - 2. choline oxidation\n  - BetA-dependent\
    \ betaine aldehyde formation\n    - BetA choline dehydrogenase activity (molecular\
    \ player: FAD-dependent BetA family; activity or role: choline dehydrogenase activity)\n\
    \  - 3. glycine betaine formation\n  - BetB-dependent glycine betaine formation\n\
    \    - BetB betaine-aldehyde dehydrogenase activity (molecular player: BetB aldehyde\
    \ dehydrogenase family; activity or role: betaine-aldehyde dehydrogenase (NAD+)\
    \ activity)"
  module_connections: '- BetT-dependent choline uptake feeds into BetA-dependent betaine
    aldehyde formation: BetT supplies intracellular choline to BetA.

    - BetA-dependent betaine aldehyde formation feeds into BetB-dependent glycine
    betaine formation: BetA supplies betaine aldehyde to BetB.'
  pathway_query: UPA00529
  pathway_id: UPA00529
  pathway_name: UniPathway UPA00529
  pathway_source: UniPathway
  pathway_context: 'Resolved local bucket unipathway:UPA00529 with 1 primary genes;
    module area: unipathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '1'
  candidate_genes: '- betI: PP_5719 | A0A140FWS5 | HTH-type transcriptional regulator
    BetI (primary bucket unipathway:UPA00529)'
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
citation_count: 5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__bacterial_choline_to_glycine_betaine_biosynthesis__upa00529-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_choline_to_glycine_betaine_biosynthesis__upa00529-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial choline uptake and glycine betaine biosynthesis in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: UPA00529
- Resolved ID: UPA00529
- Resolved name: UniPathway UPA00529
- Source: UniPathway

Resolved local bucket unipathway:UPA00529 with 1 primary genes; module area: unipathway.

## Candidate Genes From Local Metadata

Candidate gene count: 1

- betI: PP_5719 | A0A140FWS5 | HTH-type transcriptional regulator BetI (primary bucket unipathway:UPA00529)

## Generic Module Context

### Working Scope

A reusable bacterial module for choline uptake followed by its two-step oxidation to the compatible solute glycine betaine. A BetT-family transporter imports choline, FAD-dependent BetA oxidizes choline to betaine aldehyde, and NAD-dependent BetB oxidizes the aldehyde to glycine betaine.

### Provisional Biological Outline

- Bacterial choline uptake and glycine betaine biosynthesis
  - 1. choline uptake
  - BetT-dependent choline uptake
    - BetT choline transporter activity (molecular player: BetT-family choline transporter; activity or role: choline transmembrane transporter activity)
  - 2. choline oxidation
  - BetA-dependent betaine aldehyde formation
    - BetA choline dehydrogenase activity (molecular player: FAD-dependent BetA family; activity or role: choline dehydrogenase activity)
  - 3. glycine betaine formation
  - BetB-dependent glycine betaine formation
    - BetB betaine-aldehyde dehydrogenase activity (molecular player: BetB aldehyde dehydrogenase family; activity or role: betaine-aldehyde dehydrogenase (NAD+) activity)

### Known Relationships Among Steps

- BetT-dependent choline uptake feeds into BetA-dependent betaine aldehyde formation: BetT supplies intracellular choline to BetA.
- BetA-dependent betaine aldehyde formation feeds into BetB-dependent glycine betaine formation: BetA supplies betaine aldehyde to BetB.

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

# Species-Aware Module Review: Choline uptake and glycine betaine biosynthesis (UPA00529) in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Module / bucket:** unipathway:UPA00529 — "Amine and polyamine biosynthesis; betaine biosynthesis via choline pathway"
**Commissioned candidate genes:** betI / PP_5719 (regulator only)

---

## 1. Executive summary

The choline → betaine-aldehyde → glycine-betaine module is **fully satisfiable** in *P. putida* KT2440. All three functional steps are encoded by direct, high-confidence orthologs that sit in a single genomic cluster at ~5.77 Mb, together with the cognate regulator:

- **Choline uptake:** BetT-I / **PP_5061** (BCCT-family choline transporter), assigned by decisive genomic context (co-clustered with *betBA*); two BCCT paralogs (PP_0229, PP_3957) belong to unrelated operons and are excluded.
- **Choline → betaine aldehyde:** BetA / **PP_5064** (choline dehydrogenase, EC 1.1.99.1; HAMAP MF_00750; **77.7%** identity to *E. coli* BetA).
- **Betaine aldehyde → glycine betaine:** BetB / **PP_5063** (betaine-aldehyde dehydrogenase, EC 1.2.1.8; HAMAP MF_00804; **77.1%** identity to *E. coli* BetB).
- **Regulation:** BetI / **PP_5719** (TetR/HTH choline-responsive repressor), physically within the cluster between *betT-I* and *betB*.

The single most important curation issue is that the **local metadata bucket captured only the regulator (betI), not the catalytic core.** The enzymes that actually carry the UniPathway annotation (betA/PP_5064, betB/PP_5063) and the transporter (betT-I/PP_5061) were absent from the candidate list. The module should be marked **covered**, but the bucket **needs revision** to add and promote the catalytic genes.

Direct genetic evidence in KT2440 (Galvão et al. 2006, PMID 17116241) confirms *betBA* are required for choline→glycine-betaine conversion and osmotolerance, and — importantly — that the neighboring *betC* (choline-*O*-sulphate) function is **uncoupled from osmoprotection** and should be kept out of this module.

---

## 2. Target-organism pathway definition

**Included process:** transmembrane import of exogenous choline, followed by its two-step oxidation to the compatible solute glycine betaine:

```
choline (out) --BetT--> choline (in) --BetA(EC 1.1.99.1)--> betaine aldehyde --BetB(EC 1.2.1.8)--> glycine betaine
```

This is the canonical bacterial "betaine biosynthesis via choline pathway" (UniPathway **UPA00529**; equivalent to MetaCyc *choline degradation I* / KEGG map00260 betaine node). Glycine betaine then acts as an osmoprotectant (accumulated under high salt) and, in *P. putida*, also as a carbon/nitrogen source.

**Neighboring pathways to keep separate:**
- **Choline-*O*-sulphate utilization** (BetC / PP_0077 choline-sulfatase, EC 3.1.6.6, + ABC transporter/LysR regulator at PP_0076–0077). Galvão 2006 shows this is genetically distant from *betBA* and functionally dedicated to COS catabolism, **not** osmoprotection.
- **Direct glycine-betaine/quaternary-amine transport** (ProU/OpuA-type ABC importers, ProP): these supply betaine without synthesis and belong to an osmolyte-transport module, not the biosynthetic one.
- **Downstream glycine betaine catabolism** (demethylation to dimethylglycine) is a separate degradation pathway.

**Alternate names / DB definitions:** *bet* regulon; choline oxidation pathway; UniProt pathway string "Amine and polyamine biosynthesis; betaine biosynthesis via choline pathway"; MetaCyc PWY-... choline degradation.

---

## 3. Expected step model

| Step | Function (GO/EC) | Expected player | KT2440 status |
|------|------------------|-----------------|---------------|
| 1. Choline uptake | choline transmembrane transporter (GO:0015220) | BetT-family (BCCT) | **Covered** — BetT-I/PP_5061 (cluster); paralogs PP_0229, PP_3957 |
| 2. Choline oxidation | choline dehydrogenase (EC 1.1.99.1) | FAD/GMC BetA | **Covered** — BetA/PP_5064 (cluster); paralog PP_0056 |
| 3. Betaine aldehyde oxidation | betaine-aldehyde dehydrogenase, NAD+ (EC 1.2.1.8) | BetB (ALDH) | **Covered** — BetB/PP_5063 (cluster) |
| (Regulation) | TetR repressor, choline-responsive | BetI | Present — BetI/PP_5719 (cluster) |

---

## 4. Candidate genes and evidence

**Genomic layout (KEGG coordinates, ~5.77 Mb) — the *bet* cluster:**

```
PP_5061 betT-I  5,770,959–5,772,962 (–)   choline transporter (BCCT)
PP_5719 betI    5,773,438–5,774,094 (+)   TetR repressor
PP_5063 betB    5,774,134–5,775,606 (+)   betaine-aldehyde dehydrogenase
PP_5064 betA    5,775,684–5,777,381 (+)   choline dehydrogenase
```

> **Curation note on locus tags:** despite its high number, **PP_5719 (betI) physically lies between betT-I and betB** — it is the cognate, adjacent regulator of the *betBA* operon. The layout recapitulates the canonical *E. coli* *bet* regulon, where *betI* and three structural genes *betT* (choline porter), *betA* (choline dehydrogenase) and *betB* (betaine-aldehyde dehydrogenase) are controlled by two **divergent promoters** driving *betT* vs *betIBA*, with **BetI acting as a choline-responsive repressor of both** (Lamark et al. 1996, PMID 8626294; gene order established by Andresen et al. 1988, PMID 3065456). In KT2440 *betT-I*/PP_5061 is on the **reverse strand** while *betI-betB-betA* are on the **forward strand** — exactly the divergent arrangement expected. Species transfer of this regulon model to KT2440 is **strong**. The high locus tag on betI is a re-annotation artifact, not evidence of a distal/unrelated gene.

**Orthology quantification (global-alignment % identity to *E. coli* K-12 reference):**

| KT2440 protein | vs *E. coli* ortholog | Paralog vs same ref | Verdict |
|----------------|----------------------|---------------------|---------|
| BetA / PP_5064 | **77.7%** vs EcBetA (P17444) | PP_0056 = 40.5% | PP_5064 = true ortholog; PP_0056 distant paralog |
| BetB / PP_5063 | **77.1%** vs EcBetB (P17445) | PP_0708 = 40.7% | PP_5063 = true ortholog; PP_0708 distant paralog |
| BetT-I / PP_5061 | 43.4% vs EcBetT (P0ABC9) | PP_0229 = 46.2%; PP_3957 = 46.5% | No strong sequence ortholog; PP_5061 chosen on **genomic context**, transporter step ambiguous |

> Interpretation: the two catalytic steps are backed by unambiguous ~77% orthologs, so PP_5064 and PP_5063 are safe module representatives and PP_0056/PP_0708 are correctly demoted to candidate_uncertain. The three BCCT transporters are all only ~43–46% identical to *E. coli* BetT (and 45–51% to each other), so **step 1 cannot be resolved by sequence alone** — PP_5061 is preferred only because it co-clusters with *betIBA*; PP_0229/PP_3957 remain plausible choline importers.

| Gene | Accession | Role | Evidence type | Curation caveat |
|------|-----------|------|---------------|-----------------|
| **betA / PP_5064** | Q88CW6 | Choline dehydrogenase (step 2) | UniProt HAMAP MF_00750; RHEA:17433/15305; **direct KT2440 mutant phenotype** (Galvão 2006) | Dual EC (1.1.99.1 **+** 1.2.1.8) is **genuine bifunctionality** — BetA oxidizes both choline and betaine aldehyde (Cánovas 2000, PMID 10708384), not an annotation error; BetB remains the dedicated NAD+-BADH. **Promote.** |
| **betB / PP_5063** | Q88CW7 | Betaine-aldehyde dehydrogenase (step 3) | UniProt HAMAP MF_00804; RHEA:15305; direct KT2440 phenotype (Galvão 2006) | High-confidence ortholog in cluster. **Promote.** |
| **betT-I / PP_5061** | Q88CW9 | Choline transporter (step 1) | Cluster position, BCCT family; BetT is the osmoregulated choline importer (cryo-EM mechanism, Yang 2024, PMID 39141726) | No EC/GO in UniProt; transport not directly assayed in KT2440. **Promote as best transporter candidate.** |
| **betI / PP_5719** | A0A140FWS5 | Choline-responsive TetR repressor | HAMAP MF_00768; cluster position | Regulatory, **not** a catalytic step; should not itself "satisfy" any enzymatic module step. |

---

## 5. Gaps, ambiguities, and likely over-annotations

- **No true gaps.** All three enzymatic/transport steps have strong candidates; the module is not missing any step in KT2440.
- **Transporter paralog ambiguity — resolved by genomic context:** three BCCT choline/betaine transporters exist, but their operonic contexts differ decisively (KEGG neighbor analysis):
  - **BetT-I/PP_5061** — directly flanked by *betB*/PP_5063 and *betA*/PP_5064 → **the module choline importer** (step 1, covered).
  - **BetT-II/PP_0229** — embedded among sulfur-assimilation genes (sulfur-compound ABC transporter PP_0226, cystine-binding PP_0227, sulfonate dioxygenase PP_0230, taurine ABC transporter PP_0231–0232) → unrelated physiology → **candidate_uncertain, not the module transporter**.
  - **BetT-III(BetTC)/PP_3957** — next to NhaA Na⁺/H⁺ antiporter (PP_3958), a chloride channel (PP_3959) and its own TetR regulator (PP_3960) → a standalone osmoregulated transporter → **candidate_uncertain, not the module transporter**.
  Additional ABC importers (cbcVWX/PP_0294–0296, betX/PP_1741, opuA/PP_2774, yehWXYZ/PP_0868–0871, proP/PP_2914, PP_0076 betaine-binding) mostly transport betaine/carnitine rather than feed choline oxidation → not module step 1.
- **Choline-dehydrogenase paralog:** **BetA-I / PP_0056** (Q88RS3, EC 1.1.99.1, 550 aa) is a second choline dehydrogenase outside the cluster; likely accessory or over-propagated for this module → **candidate_uncertain**.
- **BADH-family over-count:** PP_0708 is annotated "betaine-aldehyde dehydrogenase" without EC, and >10 other ALDH-family paralogs exist. Only **BetB/PP_5063** carries the pathway/HAMAP evidence → others are **likely over-annotations** for this step.
- **BetA dual EC (1.1.99.1 + 1.2.1.8):** NOT an over-annotation — BetA-family flavoenzymes genuinely oxidize both choline and betaine aldehyde (Cánovas 2000, PMID 10708384). The dedicated NAD+-dependent step 3, however, is BetB's role; retain both enzymes.
- **BetC/PP_0077 (choline-sulfatase):** a distinct pathway (choline-*O*-sulphate → choline + sulfate). **Keep out of UPA00529.** Direct KT2440 evidence: it is downregulated at high salt and dispensable for osmoprotection (Galvão 2006).

---

## 6. Module and GO-curation recommendations

| Module step | Recommended status | Representative gene |
|-------------|--------------------|--------------------|
| Choline uptake | **covered** — BetT-I/PP_5061 assigned by decisive genomic context (co-clustered with betBA); paralogs PP_0229/PP_3957 excluded (sulfur- and ion-stress operons) | betT-I / PP_5061 |
| Choline → betaine aldehyde | **covered** | betA / PP_5064 |
| Betaine aldehyde → glycine betaine | **covered** | betB / PP_5063 |
| (Regulation) | present, non-catalytic | betI / PP_5719 |

- **module_needs_revision (metadata):** the bucket must be expanded from betI-only to include betA/PP_5064, betB/PP_5063, betT-I/PP_5061. Recording only the regulator would falsely imply the pathway is regulator-defined.
- **Generic module boundaries:** correct for KT2440 — keep the three-step scope; explicitly **exclude** choline-*O*-sulphate (betC) and betaine ABC-import as separate modules.
- **GO curation:** BetT-I/PP_5061 lacks a GO transporter term in UniProt — a **GO annotation (choline transmembrane transporter activity, GO:0015220) request** is warranted based on family + cluster context. Flag the BetA dual-EC for review.
- No new module document is required; the existing generic outline maps cleanly onto the KT2440 cluster.

---

## 7. Genes to promote to full `fetch-gene` review

1. **betA / PP_5064** (Q88CW6) — choline dehydrogenase; resolve dual-EC caveat.
2. **betB / PP_5063** (Q88CW7) — betaine-aldehyde dehydrogenase; high-confidence step 3.
3. **betT-I / PP_5061** (Q88CW9) — primary choline uptake candidate; needs transport-evidence review.
4. (Context) **betI / PP_5719** — confirm regulator, keep as regulatory annotation only.
5. (Disambiguation) **PP_0056, PP_0229, PP_3957, PP_0708** — review to confirm they are paralogs/other-context, not module representatives.

---

## 8. Key references

- Galvão TC, de Lorenzo V, Cánovas D. (2006) *Uncoupling of choline-O-sulphate utilization from osmoprotection in Pseudomonas putida.* Mol Microbiol. **PMID: 17116241.** — Direct KT2440 evidence that *betBA* convert choline to glycine betaine and confer osmotolerance, and that *betC* (COS) is separate from osmoprotection.
- Lamark T, Røkenes TP, McDougall J, Strøm AR. (1996) *The complex bet promoters of Escherichia coli: regulation by oxygen (ArcA), choline (BetI), and osmotic stress.* J Bacteriol. **PMID: 8626294.** — Defines the *betI*/*betT*/*betA*/*betB* regulon and BetI as a choline-responsive repressor of divergent promoters (model transferred to KT2440).
- Andresen PA et al. (1988) *Molecular cloning, physical mapping and expression of the bet genes... of Escherichia coli.* Mol Microbiol. **PMID: 3065456.** — Original definition of *betA/betB/betT* activities and gene order.
- Cánovas D et al. (2000) *Genes for the synthesis of the osmoprotectant glycine betaine from choline in Halomonas elongata DSM 3043.* **PMID: 10708384.** — *betIBA* operon; evidence that BetA oxidizes both choline and betaine aldehyde (supports BetA/PP_5064 dual EC).
- Yang et al. (2024) *Structure and mechanism of the osmoregulated choline transporter BetT.* **PMID: 39141726.** — Cryo-EM mechanism confirming BetT as the osmoregulated choline importer feeding betaine synthesis.
- UniProt Knowledgebase entries: Q88CW6 (BetA/PP_5064), Q88CW7 (BetB/PP_5063), Q88CW9 (BetT-I/PP_5061), A0A140FWS5 (BetI/PP_5719); HAMAP rules MF_00750, MF_00804, MF_00768.
- KEGG GENES (ppu) locus records for PP_5061–5065 and PP_5719 (genomic coordinates / operon layout).

---

### Uncertainty & species-transfer notes
- Steps 2–3 (betA/betB) are **direct experimental** for KT2440 (mutant phenotypes, Galvão 2006).
- Step 1 (betT-I) is **inferred from family + cluster position**; transport not directly assayed in KT2440 — transfer confidence moderate–strong.
- Paralog assignments and the BetA dual-EC rest on homology/annotation and warrant expert confirmation.


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_choline_to_glycine_betaine_biosynthesis__upa00529-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_choline_to_glycine_betaine_biosynthesis__upa00529-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:17116241
2. PMID:8626294
3. PMID:3065456
4. PMID:10708384
5. PMID:39141726