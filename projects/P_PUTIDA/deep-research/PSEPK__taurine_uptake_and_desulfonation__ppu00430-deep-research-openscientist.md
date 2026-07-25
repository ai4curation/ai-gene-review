---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-25T12:40:15.518962'
end_time: '2026-07-25T12:55:58.306431'
duration_seconds: 942.79
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial taurine uptake and desulfonation
  module_summary: A reusable two-part bacterial module in which the TauABC ATP-binding
    cassette transporter imports extracellular taurine and TauD oxidatively cleaves
    the imported sulfonate to aminoacetaldehyde and sulfite. The module represents
    acquisition of taurine as a sulfur source. Downstream aminoacetaldehyde metabolism,
    sulfite assimilation, sulfur-starvation regulation, and alternative organosulfonate
    transport or cleavage systems are outside the boundary.
  module_outline: "- Bacterial taurine uptake and desulfonation\n  - 1. taurine uptake\n\
    \  - TauABC taurine import\n    - TauABC taurine transporter (molecular player:\
    \ TauABC taurine importer; activity or role: ABC-type taurine transporter transporter\
    \ activity)\n  - 2. taurine desulfonation\n  - TauD taurine dioxygenation\n  \
    \  - Taurine dioxygenase (molecular player: TauD/TfdA-like 2-oxoglutarate-dependent\
    \ dioxygenases; activity or role: taurine dioxygenase activity)"
  module_connections: '- TauABC taurine import feeds into TauD taurine dioxygenation:
    TauABC supplies intracellular taurine to TauD.'
  pathway_query: ppu00430
  pathway_id: ppu00430
  pathway_name: Taurine and hypotaurine metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00430 with 5 primary genes; module
    area: amino_acid_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '5'
  candidate_genes: '- tauD: PP_0230 | Q88RA3 | Alpha-ketoglutarate-dependent taurine
    dioxygenase (EC 1.14.11.17) (EC 1.14.11.17; primary bucket kegg:ppu00430)

    - pta: PP_0774 | Q88PS4 | Phosphate acetyltransferase (EC 2.3.1.8) (Phosphotransacetylase)
    (EC 2.3.1.8; primary bucket kegg:ppu00430)

    - gdhB: PP_2080 | Q88L55 | NAD-specific glutamate dehydrogenase (EC 1.4.1.2) (EC
    1.4.1.2; primary bucket kegg:ppu00430)

    - PP_3535: PP_3535 | Q88H30 | Glutathione hydrolase proenzyme (EC 2.3.2.2) (EC
    3.4.19.13) [Cleaved into: Glutathione hydrolase large chain; Glutathione hydrolase
    small chain] (EC 2.3.2.2; 3.4.19.13; primary bucket kegg:ppu00430)

    - ggt: PP_4659 | Q88E09 | Glutathione hydrolase proenzyme (EC 2.3.2.2) (EC 3.4.19.13)
    [Cleaved into: Glutathione hydrolase large chain; Glutathione hydrolase small
    chain] (EC 2.3.2.2; 3.4.19.13; primary bucket kegg:ppu00430)'
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
  path: PSEPK__taurine_uptake_and_desulfonation__ppu00430-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__taurine_uptake_and_desulfonation__ppu00430-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial taurine uptake and desulfonation in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00430
- Resolved ID: ppu00430
- Resolved name: Taurine and hypotaurine metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00430 with 5 primary genes; module area: amino_acid_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 5

- tauD: PP_0230 | Q88RA3 | Alpha-ketoglutarate-dependent taurine dioxygenase (EC 1.14.11.17) (EC 1.14.11.17; primary bucket kegg:ppu00430)
- pta: PP_0774 | Q88PS4 | Phosphate acetyltransferase (EC 2.3.1.8) (Phosphotransacetylase) (EC 2.3.1.8; primary bucket kegg:ppu00430)
- gdhB: PP_2080 | Q88L55 | NAD-specific glutamate dehydrogenase (EC 1.4.1.2) (EC 1.4.1.2; primary bucket kegg:ppu00430)
- PP_3535: PP_3535 | Q88H30 | Glutathione hydrolase proenzyme (EC 2.3.2.2) (EC 3.4.19.13) [Cleaved into: Glutathione hydrolase large chain; Glutathione hydrolase small chain] (EC 2.3.2.2; 3.4.19.13; primary bucket kegg:ppu00430)
- ggt: PP_4659 | Q88E09 | Glutathione hydrolase proenzyme (EC 2.3.2.2) (EC 3.4.19.13) [Cleaved into: Glutathione hydrolase large chain; Glutathione hydrolase small chain] (EC 2.3.2.2; 3.4.19.13; primary bucket kegg:ppu00430)

## Generic Module Context

### Working Scope

A reusable two-part bacterial module in which the TauABC ATP-binding cassette transporter imports extracellular taurine and TauD oxidatively cleaves the imported sulfonate to aminoacetaldehyde and sulfite. The module represents acquisition of taurine as a sulfur source. Downstream aminoacetaldehyde metabolism, sulfite assimilation, sulfur-starvation regulation, and alternative organosulfonate transport or cleavage systems are outside the boundary.

### Provisional Biological Outline

- Bacterial taurine uptake and desulfonation
  - 1. taurine uptake
  - TauABC taurine import
    - TauABC taurine transporter (molecular player: TauABC taurine importer; activity or role: ABC-type taurine transporter transporter activity)
  - 2. taurine desulfonation
  - TauD taurine dioxygenation
    - Taurine dioxygenase (molecular player: TauD/TfdA-like 2-oxoglutarate-dependent dioxygenases; activity or role: taurine dioxygenase activity)

### Known Relationships Among Steps

- TauABC taurine import feeds into TauD taurine dioxygenation: TauABC supplies intracellular taurine to TauD.

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

# Species-aware Module Review: Bacterial taurine uptake and desulfonation in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxid 160488; proteome UP000000556)
**Module:** TauABC taurine import → TauD taurine desulfonation (KEGG bucket ppu00430, "Taurine and hypotaurine metabolism"; module area amino_acid_metabolism)
**Review completed:** Iteration 5 (6 recorded findings; sources: UniProt UP000000556, KEGG ppu00430, PubMed)

---

## 1. Executive summary

The two-step module — **(1) ABC-transporter import of extracellular taurine and (2) 2-oxoglutarate–dependent oxidative desulfonation of taurine to aminoacetaldehyde + sulfite** — is **fully satisfiable in *P. putida* KT2440**, and both steps map to a single contiguous operon.

- **Step 2 (TauD desulfonation) is COVERED with direct experimental evidence in the exact strain.** PP_0230 (UniProt Q88RA3, TAUD_PSEPK) was purified from KT2440, is an Fe(II)/α-ketoglutarate-dependent taurine dioxygenase (EC 1.14.11.17), and three apo crystal structures were solved (Knauer et al. 2012, PMID 22221834).
- **Step 1 (TauABC import) is COVERED at candidate level.** The transporter genes are **PP_0233 tauA** (periplasmic binding), **PP_0232 tauB** (ATPase), **PP_0231 tauC** (permease) — immediately adjacent to tauD, forming a **tauDCBA operon (PP_0230→PP_0233)**. These genes were **missing from the supplied candidate metadata** and should be added to the module.
- **The candidate list is largely misleading.** Only 1 of the 5 supplied genes (PP_0230/tauD) belongs to the module. The other four (**pta, gdhB, ggt, PP_3535**) are **KEGG broad-map co-members**, not taurine-uptake/desulfonation genes → likely over-propagation for this module boundary.

**Bottom line for curation:** Mark both module steps **covered**; **revise the candidate gene set** (add tauABC PP_0231–0233; drop pta/gdhB/ggt/PP_3535 from the module).

---

## 2. Target-organism pathway definition

**Included (module boundary):** periplasmic capture and ABC-transport of extracellular taurine (2-aminoethanesulfonate) into the cytoplasm, followed by its oxygenolytic C–S cleavage:

> taurine + 2-oxoglutarate + O₂ → aminoacetaldehyde + sulfite + succinate + CO₂

This represents **acquisition of taurine as a sulfur source** (a sulfur-starvation / cys-regulon function), not carbon or nitrogen catabolism.

**Kept separate (neighboring processes, out of boundary):**
- Downstream **aminoacetaldehyde** metabolism and **sulfite assimilation** into cysteine.
- **Sulfur-starvation regulation** (CysB/Cbl-type; AsfR in *P. putida* — Kertesz 2000, PMID 10717312).
- **Alternative organosulfonate systems**: the **ssuEADCBF / SsuABC + SsuD FMNH₂-dependent monooxygenase** route (PP_0236–PP_0240 region here) and the **sctCS** sulfur-compound transporter (PP_0225/0226), which in *P. putida* S-313 handle aromatic/aliphatic sulfonates and sulfate esters (Kahnert et al. 2000, PMID 10781557). These are *parallel* modules, not this one.
- The broad KEGG map ppu00430 also spans **hypotaurine/cysteate/sulfoacetaldehyde** chemistry and **glutathione (γ-glutamyl) reactions** — these belong to other buckets.

**Alternate names / DB definitions:** KEGG bucket "Taurine and hypotaurine metabolism" (ppu00430; GO:0019530). KO for the dioxygenase is **K03119 (tauD)**. Note KEGG labels PP_0230 as *atsK*; UniProt uses *tauD* (synonym *atsK*). "atsK" proper is the *P. putida* S-313 **alkyl-sulfatase** (Müller et al. 2004, PMID 15023059), a paralogous but distinct α-KG dioxygenase — a naming caveat, not a functional reassignment.

---

## 3. Expected step model

| # | Step | Molecular player | Expected activity | Status in KT2440 |
|---|------|------------------|-------------------|------------------|
| 1 | Taurine import | TauABC ABC transporter | ABC-type taurine transporter | **Covered** (PP_0233/0232/0231; homology + operon) |
| 2 | Taurine desulfonation | TauD dioxygenase | taurine dioxygenase (EC 1.14.11.17) | **Covered — direct** (PP_0230, PMID 22221834) |

Known relationship (TauABC supplies intracellular taurine to TauD) is structurally supported: the transporter and dioxygenase are co-transcribed in one operon.

---

## 4. Candidate genes and evidence

### Genuine module gene

| Gene | Locus | UniProt | Role | Evidence | Status |
|------|-------|---------|------|----------|--------|
| tauD | PP_0230 | Q88RA3 (Reviewed) | α-KG–dependent taurine dioxygenase, EC 1.14.11.17; Fe(II), homotetramer | **Direct, target strain**: purified/kinetics + 3 crystal structures (PMID 22221834) | **Covered (Step 2)** |

### Transporter genes — *missing from candidate metadata, should be added*

| Gene | Locus | UniProt | Role | Evidence (UniProt PE / score) | Status |
|------|-------|---------|------|----------|--------|
| tauA | PP_0233 | Q88RA0 | Periplasmic taurine-binding protein | Homology + operon context (TrEMBL, PE3, score 1.0) | **Covered (Step 1), by inference** |
| tauB | PP_0232 | Q88RA1 | Taurine import ATP-binding protein | Homology + operon context (SwissProt, PE3, score 3.0) | **Covered (Step 1), by inference** |
| tauC | PP_0231 | Q88RA2 | Taurine ABC permease | Homology + operon context (TrEMBL, PE3, score 2.0) | **Covered (Step 1), by inference** |
| tauB-I | PP_0209 | Q88RC3 | Paralogous taurine-transporter ATPase | Homology; paralog (TrEMBL, PE4 "Predicted", score 1.0) | candidate_uncertain (accessory) |

**Evidence-tier note:** Only **tauD (PP_0230)** carries protein-level experimental evidence. All three transporter subunits are **PE3 "Inferred from homology"** (tauB-I is PE4 "Predicted"). There is thus **no strain-specific transport assay or expression/proteomics dataset** confirming the import step in KT2440 — it is covered by inference, not by direct experiment. A targeted PubMed search for a KT2440 sulfate-starvation stimulon returned no result.

**Family-signature note (upgrades import confidence above bare homology):** TauA (PP_0233) carries the **dedicated TauA periplasmic-binding InterPro family IPR010068 ("Peri-bd_TauA")**, and TauB (PP_0232) is assigned by **HAMAP rule MF_01714 as "Taurine import ATP-binding protein TauB" (EC 7.6.2.7)**; TauC (PP_0231) has the standard MetI-like ABC permease domain (Pfam PF00528). These are *taurine-specific* signatures, not generic sulfonate-ABC homology, so the operon is confidently a taurine importer. Residual caveat: TauA also carries an SsuA/THI5 co-signature (IPR015168; Pfam PF09084 NMT1), reflecting the known TauA/SsuA overlap — strict substrate exclusivity is not guaranteed without a binding assay.

**Synteny (sulfur-acquisition island).** tauABCD is embedded in a contiguous sulfur-scavenging island, KEGG-annotated across PP_0225–PP_0240:

| Locus | Gene | Product |
|-------|------|---------|
| PP_0225/0226 | sctC/sctS | sulfur-compound ABC transporter (ATPase / permease) |
| PP_0227 | fliY | periplasmic cystine-binding protein |
| PP_0230–0233 | **tauD-tauC-tauB-tauA** | **this module** |
| PP_0236–0240 | ssuE-ssuA-ssuD-ssuC-ssuB | alkanesulfonate/isethionate uptake + FMNH₂-monooxygenase |

This explains the paralog redundancy (PP_0232 tauB / "tauB-II" in-operon vs distal PP_0209 "tauB-I") and reinforces the case for splitting the ssu/sct systems into sibling modules.

### Supplied candidates that are **out-of-module (KEGG map artifacts)**

| Gene | Locus | UniProt | Annotation | Why not in module |
|------|-------|---------|-----------|-------------------|
| pta | PP_0774 | Q88PS4 | Phosphate acetyltransferase, EC 2.3.1.8 | Central acetyl-P/acetyl-CoA metabolism; appears on the map only via C2-sulfonate dissimilation (Xsc/Pta) chemistry, not taurine uptake/TauD |
| gdhB | PP_2080 | Q88L55 | NAD glutamate dehydrogenase, EC 1.4.1.2 | 2-oxoglutarate/glutamate housekeeping; map co-member only |
| ggt | PP_4659 | Q88E09 | γ-glutamyltranspeptidase, EC 2.3.2.2/3.4.19.13 | Glutathione / 5-L-glutamyl-taurine chemistry; not taurine desulfonation |
| PP_3535 | PP_3535 | Q88H30 | Glutathione hydrolase (K00681) | Same as ggt; paralogous over-propagation |

---

## 5. Gaps, ambiguities, and likely over-annotations

- **Candidate-set gap (critical):** the entire transport step was absent from the supplied candidate metadata. tauABC (PP_0231–0233) must be linked to the module. Without them the module would look "half missing" purely due to a metadata omission, not biology.
- **Over-propagation:** 4/5 supplied candidates (pta, gdhB, ggt, PP_3535) are KEGG **pathway-map co-members**, not functional module members. They should be excluded from module satisfiability scoring.
- **Naming ambiguity:** PP_0230 carries synonym *atsK* (KEGG) vs. *tauD* (UniProt). True *atsK* is an alkyl-sulfatase in S-313; here the function is experimentally taurine dioxygenase. Curators should keep the tauD assignment and note the synonym.
- **Paralog ambiguity (transport):** PP_0209 (tauB-I) is a second taurine-transporter ATPase; the ssu operon (PP_0238 ssuD, PP_0239 ssuC) plus a further sulfonate ABC set (Q88GT1/2/3) and MsuD (Q88J84) provide redundant/parallel organosulfonate routes. These can confound automated "which transporter feeds TauD" calls.
- **Paralog check (dioxygenase) — clean:** KT2440 encodes **4 TauD/TfdA-family (Pfam PF02668) proteins**, but **EC 1.14.11.17 is assigned to PP_0230 alone**. The other three — PP_0169 (Q88RG1), PP_4222 (Q88F76, "SyrP-like"), PP_4466 (Q88EJ6) — are uncharacterized 2-oxoglutarate-dependent dioxygenases carrying **no taurine-dioxygenase EC**. So Step 2 has *no* current paralog ambiguity. **Watch-item:** these three should NOT be counted toward the module and are candidates for spurious EC 1.14.11.17 propagation by family-membership pipelines.
- **Direct-vs-inferred transport:** No KT2440-specific taurine *transport assay* was found; the import step rests on annotation + operon synteny + strong genus precedent (S-313 ssu/tau work). Transfer confidence: **strong** (same operon as an experimentally confirmed dioxygenase in the same strain), but not experimentally proven for transport per se.

---

## 6. Module and GO-curation recommendations

| Module step | Recommendation |
|-------------|----------------|
| Step 1 — TauABC import | **covered** (add PP_0233 tauA, PP_0232 tauB, PP_0231 tauC). GO:0015411/ABC-type taurine transport; GO:0015734 taurine transmembrane transport. |
| Step 2 — TauD desulfonation | **covered** (PP_0230; GO:0031419-independent — use taurine dioxygenase GO:0031418 / EC 1.14.11.17). Direct evidence, highest confidence. |
| pta, gdhB, ggt, PP_3535 | **not_in_module / module_needs_revision** — remove from this module's candidate set (KEGG broad-map artifact). |

- **Module boundary is essentially correct for this organism**; the generic TauABC→TauD outline matches KT2440 one-to-one.
- **New module document suggested:** a sibling "SsuABC / SsuD (+MsuD) organosulfonate desulfonation" module to capture the parallel FMNH₂-monooxygenase route (PP_0236–0240, plus sctCS PP_0225/0226 and the distal tauB-I PP_0209), so those genes are not mis-scored against the TauD module.
- No new GO term requests appear necessary; existing taurine transport / taurine dioxygenase terms suffice.

---

## 7. Genes to promote to full `fetch-gene` review

1. **PP_0230 tauD** — anchor gene; promote to confirm EC/GO and lock synonym handling (tauD vs atsK). *Highest priority; direct evidence available.*
2. **PP_0233 tauA / PP_0232 tauB / PP_0231 tauC** — promote as a unit to formally add the transport step and assign transporter GO terms.
3. **PP_0209 tauB-I** — promote to resolve paralog role (dedicated vs shared ABC ATPase).

---

## 8. Key references

- Knauer SH, Hartl-Spiegelhauer O, Schwarzinger S, Hänzelmann P, Dobbek H. *The Fe(II)/α-ketoglutarate-dependent taurine dioxygenases from Pseudomonas putida and Escherichia coli are tetramers.* FEBS J. 2012. **PMID 22221834.** — Direct characterization + structures of TauD from KT2440.
- Kahnert A, Vermeij P, Wietek C, James P, Leisinger T, Kertesz MA. *The ssu locus plays a key role in organosulfur metabolism in Pseudomonas putida S-313.* J Bacteriol. 2000. **PMID 10781557.** — ssuEADCBF (SsuABC transporter + SsuD monooxygenase) organosulfonate route in *P. putida*.
- Kertesz MA. *Riding the sulfur cycle — metabolism of sulfonates and sulfate esters in gram-negative bacteria.* FEMS Microbiol Rev. 2000. **PMID 10717312.** — α-KG–dependent taurine dioxygenase vs FMNH₂-monooxygenase desulfonation; CysB/Cbl/AsfR regulation.
- Müller I, Kahnert A, Pape T, et al. *Crystal structure of the alkylsulfatase AtsK…* J Mol Biol. 2004. **PMID 15023059.** — Clarifies AtsK (alkylsulfatase) vs TauD naming within the α-KG dioxygenase superfamily.
- KEGG pathway ppu00430; UniProt UP000000556 (Q88RA3, Q88RA0–Q88RA2, Q88RC3).

---

### Evidence confidence summary
- **Direct (target strain):** TauD desulfonation (PP_0230).
- **Strong inference (operon synteny + genus precedent):** TauABC import (PP_0231–0233).
- **Refuted as module members:** pta, gdhB, ggt, PP_3535 (KEGG map co-membership only).


## Artifacts

- [OpenScientist final report](PSEPK__taurine_uptake_and_desulfonation__ppu00430-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__taurine_uptake_and_desulfonation__ppu00430-deep-research-openscientist_artifacts/final_report.pdf)