---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T12:11:07.407361'
end_time: '2026-07-11T12:20:17.501091'
duration_seconds: 550.09
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: mcl-PHA monomer supply from de novo fatty-acid synthesis
  module_summary: A Pseudomonas putida KT2440 UniPathway UPA00212 module for the PhaG
    bridge from de novo fatty-acid synthesis to medium-chain-length polyhydroxyalkanoate
    (mcl-PHA) biosynthesis. PhaG supplies (R)-3-hydroxyacyl-CoA monomers from ACP-bound
    fatty-acid-synthesis intermediates for downstream PHA synthases. This module records
    the monomer supply connection rather than the PhaC polymerization step or the
    alternative beta-oxidation/PhaJ monomer-supply routes.
  module_outline: "- mcl-PHA monomer supply from de novo fatty-acid synthesis\n  -\
    \ 1. PhaG bridge from FAS intermediates to mcl-PHA monomers\n  - PhaG FAS-to-mcl-PHA\
    \ monomer supply\n    - phaG: 3-hydroxyacyl-ACP:CoA transacylase (molecular player:\
    \ PSEPK phaG; activity or role: acyltransferase activity)"
  module_connections: No explicit connections.
  pathway_query: UPA00212
  pathway_id: UPA00212
  pathway_name: UniPathway UPA00212
  pathway_source: UniPathway
  pathway_context: 'Resolved local bucket unipathway:UPA00212 with 1 primary genes;
    module area: unipathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '1'
  candidate_genes: '- phaG: PP_1408 | O85207 | (R)-3-hydroxydecanoyl-ACP:CoA transacylase
    (EC 2.4.1.-) (3-hydroxyacyl-CoA-acyl carrier protein transferase) (EC 2.4.1.-;
    primary bucket unipathway:UPA00212)'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__mcl_pha_monomer_supply_from_fas__upa00212-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__mcl_pha_monomer_supply_from_fas__upa00212-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

mcl-PHA monomer supply from de novo fatty-acid synthesis in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: UPA00212
- Resolved ID: UPA00212
- Resolved name: UniPathway UPA00212
- Source: UniPathway

Resolved local bucket unipathway:UPA00212 with 1 primary genes; module area: unipathway.

## Candidate Genes From Local Metadata

Candidate gene count: 1

- phaG: PP_1408 | O85207 | (R)-3-hydroxydecanoyl-ACP:CoA transacylase (EC 2.4.1.-) (3-hydroxyacyl-CoA-acyl carrier protein transferase) (EC 2.4.1.-; primary bucket unipathway:UPA00212)

## Generic Module Context

### Working Scope

A Pseudomonas putida KT2440 UniPathway UPA00212 module for the PhaG bridge from de novo fatty-acid synthesis to medium-chain-length polyhydroxyalkanoate (mcl-PHA) biosynthesis. PhaG supplies (R)-3-hydroxyacyl-CoA monomers from ACP-bound fatty-acid-synthesis intermediates for downstream PHA synthases. This module records the monomer supply connection rather than the PhaC polymerization step or the alternative beta-oxidation/PhaJ monomer-supply routes.

### Provisional Biological Outline

- mcl-PHA monomer supply from de novo fatty-acid synthesis
  - 1. PhaG bridge from FAS intermediates to mcl-PHA monomers
  - PhaG FAS-to-mcl-PHA monomer supply
    - phaG: 3-hydroxyacyl-ACP:CoA transacylase (molecular player: PSEPK phaG; activity or role: acyltransferase activity)

### Known Relationships Among Steps

No explicit connections.

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

# Species-Aware Module Review: mcl-PHA monomer supply from de novo fatty-acid synthesis in *Pseudomonas putida* KT2440 (UniPathway UPA00212)

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Module bucket:** unipathway:UPA00212 — PhaG bridge from de novo fatty-acid synthesis (FAS) to medium-chain-length polyhydroxyalkanoate (mcl-PHA) monomers
**Candidate gene(s):** phaG — PP_1408 | O85207 | annotated as (R)-3-hydroxydecanoyl-ACP:CoA transacylase (EC 2.4.1.-)

**Database cross-check (UniProt REST, Iteration 2).** O85207 is a **reviewed Swiss-Prot** entry: gene `phaG`, locus `PP_1408`, organism *P. putida* KT2440 (taxon 160488), name "(R)-3-hydroxydecanoyl-ACP:CoA transacylase", EC 2.4.1.-, mapped to **UniPathway UPA00212**, KEGG `ppu:PP_1408`, BioCyc `G1G01-1499-MONOMER`. Its FUNCTION field records only the 1998 in-vitro transacylase assay and does **not** incorporate the 2012 thioesterase revision — the legacy annotation is entrenched at the Swiss-Prot level and inherited downstream. The candidate 3HA-CoA ligase `PP_0763` = **Q88PT5**, **TrEMBL (unreviewed)**, submission name "Medium-chain-fatty-acid CoA ligase", **no EC number** and no curated 3-hydroxy specificity.

---

## 1. Executive summary

- The single candidate gene, **phaG (PP_1408 / O85207)**, is a **genuine, experimentally characterized enzyme of the target strain** *P. putida* KT2440. It is the historically defined "metabolic link" between de novo fatty-acid synthesis and mcl-PHA biosynthesis (Rehm et al. 1998, PMID 9727022). This module step is **covered** by direct target-organism evidence.
- **Curation-critical caveat:** the metadata annotation "3-hydroxyacyl-ACP:**CoA transacylase** (EC 2.4.1.-, acyltransferase GO)" reflects the **original 1998 model, which has since been biochemically revised**. Current evidence (Wang et al., *Appl. Environ. Microbiol.* 2012, 78:519–527; corroborated by PMID 25732207, PMID 30799088) indicates **PhaG functions as a (R)-3-hydroxyacyl-ACP thioesterase** (EC 3.1.2.-), releasing **free (R)-3-hydroxy fatty acids** rather than directly forming an acyl-CoA.
- Consequently, **complete monomer supply to a CoA thioester (the substrate of PhaC) requires a second enzyme: a (R)-3-hydroxyacyl-CoA ligase, encoded in KT2440 by PP_0763** (EC 6.2.1.-). This gene is **absent from the module metadata** but is mechanistically required and present in the target genome.
- **Recommendation:** mark the PhaG step **covered (with a revised-activity note)**; flag the module as **module_needs_revision** because a required 3HA-CoA ligase step (PP_0763) is missing; treat the EC 2.4.1.- / acyltransferase GO mapping as a **likely over-propagated legacy annotation**.

---

## 2. Target-organism pathway definition

**Included process.** The channelling of intermediates of **de novo fatty-acid biosynthesis** (ACP-bound (R)-3-hydroxyacyl groups, principally C8–C12) toward **mcl-PHA monomer supply**. In *P. putida* KT2440 this is the route used when cells grow on **structurally unrelated carbon sources** (gluconate, glucose, sugars, styrene-derived acetyl-CoA), typically under **nitrogen/nutrient limitation**, when no exogenous fatty acids are available.

Mechanistically (revised model):
1. FAS produces **(R)-3-hydroxyacyl-ACP**.
2. **PhaG** removes the 3-hydroxyacyl group from ACP — now understood as a **thioesterase**, yielding **free (R)-3-hydroxy fatty acid**.
3. A **(R)-3-hydroxyacyl-CoA ligase (PP_0763)** activates the free acid to **(R)-3-hydroxyacyl-CoA**.
4. (Downstream, **outside this module**) **PhaC1/PhaC2 synthases** polymerize the CoA monomers into mcl-PHA.

**Neighboring processes to keep separate.**
- **PhaC polymerization** (PP_5003 phaC1 / PP_5005 phaC2) — the terminal step; correctly excluded from UPA00212.
- **β-oxidation-fed monomer supply via PhaJ** (R-specific enoyl-CoA hydratase) — the alternative route used when growing **on fatty acids**; a distinct monomer-supply module, correctly excluded.
- **Fatty-acid de novo synthesis proper** (fab genes) and **rhamnolipid synthesis (RhlA/RhlG)**, which compete for the same 3-hydroxyacyl-ACP pool — overview/neighboring maps, not part of this bucket.

**Alternate names / database definitions.** phaG gene product is variously annotated as "(R)-3-hydroxydecanoyl-ACP:CoA transacylase," "3-hydroxyacyl-ACP-CoA transferase," or "3-hydroxyacyl-ACP thioesterase" (PhaG). EC has historically been left as **2.4.1.-** (glycosyl/acyl transferase placeholder); the revised activity better fits a **thioesterase (EC 3.1.2.-)**.

---

## 3. Expected step model

| # | Expected step | Enzyme / activity | Gene in KT2440 | Status |
|---|---------------|-------------------|----------------|--------|
| 1 | FAS supplies (R)-3-hydroxyacyl-ACP | fatty-acid synthase (fab) | fabB/fabF/fabG etc. | Upstream context (not in module) |
| 2 | Release of 3-hydroxyacyl group from ACP | **PhaG** — 3-hydroxyacyl-ACP thioesterase (revised) / historically ACP:CoA transacylase | **phaG / PP_1408** | **Covered (activity revised)** |
| 3 | Activation of free (R)-3-hydroxy fatty acid to CoA thioester | (R)-3-hydroxyacyl-CoA ligase (EC 6.2.1.-) | **PP_0763** | **Gap in metadata / likely present** |
| 4 | Polymerization of 3HA-CoA to mcl-PHA | PHA synthase | phaC1/phaC2 | Out of scope (downstream) |

---

## 4. Candidate genes and evidence

### phaG — PP_1408 | O85207 — HIGH CONFIDENCE (identity), REVISED ACTIVITY

- **Likely role:** Removes the (R)-3-hydroxyacyl moiety from FAS-derived acyl-ACP to feed mcl-PHA monomer supply.
- **Evidence type — direct, target strain (strong):** Cloned from *P. putida* KT2440 by phenotypic complementation of PHA-deficient mutants; 295-aa / 33,876 Da protein; 44% identity to RhlA; transcriptionally induced on gluconate; heterologous expression conferred PHA synthesis from gluconate in a non-producer (*P. oleovorans*). Purified enzyme showed 3-hydroxyacyl-CoA↔ACP acyl-transfer activity in vitro (Rehm et al. 1998, PMID 9727022).
- **Pathway-role confirmation (strong):** Five PHA-negative KT2440 Tn5 mutants were all complemented by phaG → PhaG is the **only** FAS→PHA link in *P. putida* (Rehm, Mitsky, Steinbüchel 2001, PMID 11425728).
- **Curation-relevant caveats:**
  1. **Activity revised** from transacylase to **thioesterase** (Wang et al. 2012, via PMID 25732207). The metadata EC 2.4.1.- and "acyltransferase activity" GO are **legacy/over-propagated**; the enzyme does not by itself yield acyl-CoA.
  2. **PhaG alone is insufficient** for CoA-monomer supply/PHA in heterologous hosts unless a 3HA-CoA ligase is co-supplied — repeatedly observed in *E. coli* engineering (PMID 25732207, PMID 30799088). This is the practical signature of the thioesterase mechanism.
  3. Homolog (>99% identity) in *P. putida* CA-3 shows the same nitrogen-limitation-dependent expression (PMID 16085828); PhaG(Pa) in *P. aeruginosa* is a functional ortholog (PMID 10713430) — good genus-level transfer, but KT2440 has its own direct evidence, so transfer is not needed here.

### PP_0763 — (R)-3-hydroxyacyl-CoA ligase (UniProt Q88PT5) — NOT IN METADATA, SHOULD BE ADDED

- **Likely role:** ATP-dependent ligase activating free (R)-3-hydroxy fatty acid → (R)-3-hydroxyacyl-CoA, completing monomer supply for PhaC.
- **Evidence type — direct, target strain (moderate–strong):** PP_0763 gene product from *P. putida* KT2440 shown to have (R)-3HA-CoA ligase activity (Wang et al. 2012, cited in PMID 25732207); a *P. aeruginosa* paralog (PA3924) provides the same activity and outperforms PP_0763 in a recombinant system (PMID 25732207).
- **Database status (curation-relevant):** UniProt **Q88PT5**, **TrEMBL/unreviewed**, named "Medium-chain-fatty-acid CoA ligase", **no EC number assigned**, no explicit 3-hydroxyacyl specificity in the record — under-curated relative to the experimental evidence.
- **Curation note:** Should be **promoted to full fetch-gene review** and added as a required step if the module is intended to represent supply of **CoA** monomers (PhaC substrate). If the module is deliberately scoped only to "release from ACP," PP_0763 belongs to an adjacent activation step.

---

## 5. Gaps, ambiguities, and likely over-annotations

- **Over-annotation (likely):** phaG EC **2.4.1.-** ("transacylase"/acyltransferase). This is the 1998 interpretation; the 2012 biochemistry favors **thioesterase (EC 3.1.2.-)**. GO "acyltransferase activity" is correspondingly questionable; a hydrolase/thioesterase GO term may be more accurate. Flag for GO-curation review.
- **Metadata gap:** the **3HA-CoA ligase step (PP_0763)** required to reach the PhaC substrate is missing. Without it the module cannot, on its own, deliver a CoA-thioester monomer — a satisfiability gap for the "monomer supply" intent.
- **Ambiguity / paralogy:** whether a single dedicated 3HA-CoA ligase or several acyl-CoA synthetases (broad EC 6.2.1.-) fulfil step 3 in KT2440 is not fully resolved; acyl-CoA ligase families are large and prone to broad EC mapping and cross-annotation.
- **Boundary correctness:** the module correctly excludes PhaC and the β-oxidation/PhaJ route. The FAS-route boundary itself is well supported (PhaG is the sole FAS→PHA link).

---

## 6. Module and GO-curation recommendations

| Item | Recommendation |
|------|----------------|
| PhaG / PP_1408 step | **covered** — but attach a note that the true activity is **3-hydroxyacyl-ACP thioesterase**, not ACP:CoA transacylase. |
| EC / GO mapping for phaG | **module_needs_revision / GO request** — replace/augment EC 2.4.1.- with EC 3.1.2.- (thioesterase); re-evaluate "acyltransferase activity" GO vs. a thioesterase/hydrolase term. |
| 3HA-CoA ligase step (PP_0763) | **gap** in current metadata — add as a required activation step (EC 6.2.1.-) for CoA-monomer supply, or explicitly document that the module stops at ACP release. |
| Module boundary vs. PhaC and β-oxidation/PhaJ | **keep separate** — current scoping is correct. |
| Overall module satisfiability | **candidate_uncertain / module_needs_revision** — the sole listed step is present, but the module as written mis-states the enzyme's activity and omits a mechanistically required ligase step. |

No step should be marked `not_expected_in_target_taxon`: both PhaG and a 3HA-CoA ligase are present and functional in KT2440.

---

## 7. Genes to promote to full review

1. **phaG / PP_1408 (O85207)** — promote to full `fetch-gene` review to correct the activity/EC/GO annotation (transacylase → thioesterase).
2. **PP_0763** — promote to full `fetch-gene` review; candidate (R)-3-hydroxyacyl-CoA ligase that should likely be added to the module. Check for additional acyl-CoA synthetase paralogs that could share this role.

---

## 8. Key references

- Rehm BHA, Krüger N, Steinbüchel A. (1998) A new metabolic link between fatty acid de novo synthesis and PHA synthesis. The phaG gene from *Pseudomonas putida* KT2440 encodes a 3-hydroxyacyl-ACP–CoA transferase. *J Biol Chem* 273:24044–24051. **PMID 9727022** — original characterization in the target strain.
- Rehm BHA, Mitsky TA, Steinbüchel A. (2001) Establishment of the transacylase (PhaG)-mediated pathway for PHA biosynthesis in *E. coli*; PhaG is the only FAS→PHA link in *P. putida*. *Appl Environ Microbiol* 67:3102–3109. **PMID 11425728** — module boundary support.
- Hoffmann N, Steinbüchel A, Rehm BHA. (2000) The *P. aeruginosa* phaG gene product. *FEMS Microbiol Lett* 184:253–259. **PMID 10713430** — genus ortholog.
- Hokamura A, et al. (2015) Biosynthesis of P(3HB-co-3HA) by recombinant *E. coli* from glucose. *J Biosci Bioeng* — states PhaG "actually functions as a 3-hydroxyacyl-ACP thioesterase" and PP0763 has 3HA-CoA ligase activity (citing Wang et al. 2012). **PMID 25732207** — activity revision + PP_0763.
- Goto S, et al. (2019) LA-based polymers containing mcl-3HA in recombinant *E. coli*. Uses "(R)-3-hydroxyacyl-ACP thioesterase (PhaG)" plus "(R)-3-hydroxyacyl-CoA ligase." **PMID 30799088** — corroborates two-enzyme monomer supply.
- O'Leary ND, et al. (2005) PHA from styrene in *P. putida* CA-3; nitrogen-limitation-dependent phaG expression, >99% identity to KT2440. **PMID 16085828**.
- Wang Q, et al. (2012) *Appl Environ Microbiol* 78:519–527 — primary source for PhaG thioesterase activity and PP_0763 3HA-CoA ligase (cited secondarily; recommend direct retrieval during full gene review).

---

### Evidence status & confidence (curation quick-reference)

| Claim | Confidence | Evidence type |
|-------|-----------|---------------|
| PP_1408 = phaG = O85207 = the FAS→PHA enzyme in KT2440 | **High** | Direct, target strain (PMID 9727022) + UniProt Swiss-Prot cross-check |
| PhaG is the sole FAS→PHA link in *P. putida* | **High** | Direct genetics, target species (PMID 11425728) |
| PhaG's true activity is thioesterase, not transacylase | **Moderate–High** | Primary source Wang et al. 2012 (AEM 78:519–527), cited secondarily by two independent groups (PMID 25732207, 30799088); no dissenting reports found |
| PP_0763 (Q88PT5) supplies 3HA-CoA ligase activity | **Moderate** | Target strain, reported via secondary citation; UniProt entry unreviewed, no EC |
| EC 2.4.1.- / acyltransferase GO is over-propagated legacy | **High** | Confirmed entrenched in Swiss-Prot O85207; contradicted by thioesterase mechanism |

*Note:* The pivotal Wang et al. 2012 paper (*Appl. Environ. Microbiol.* 78:519–527) is cited here through two independent secondary sources; direct retrieval of the primary article is recommended during the full `fetch-gene` review of phaG and PP_0763 to confirm the exact assayed activities and EC assignments.

### Uncertainty & species-transfer statement
The core annotations (PhaG identity, role as sole FAS→PHA link, revised thioesterase activity, PP_0763 ligase activity) are **direct for *P. putida* KT2440**. Ortholog evidence from *P. aeruginosa* / *P.* sp. 61-3 is supportive but not required for the target-strain conclusions. The main open experimental question is the precise in vivo enzyme(s) and EC/GO term for the ACP-release and CoA-activation steps in KT2440, best resolved by direct review of Wang et al. 2012 and biochemical/structural data for PP_1408 and PP_0763.


## Artifacts

- [OpenScientist final report](PSEPK__mcl_pha_monomer_supply_from_fas__upa00212-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__mcl_pha_monomer_supply_from_fas__upa00212-deep-research-openscientist_artifacts/final_report.pdf)