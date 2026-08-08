---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-16T10:53:31.138078'
end_time: '2026-07-16T11:09:46.527775'
duration_seconds: 975.39
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: dTDP-L-rhamnose biosynthesis
  module_summary: Species-neutral bacterial module for synthesis of the activated
    sugar dTDP-L-rhamnose from alpha-D-glucose 1-phosphate. The pathway proceeds through
    dTDP-glucose formation, dTDP-glucose 4,6-dehydration, dTDP-4-dehydrorhamnose 3,5-epimerization,
    and final NADPH-dependent reduction to dTDP-L-rhamnose. The module represents
    the soluble nucleotide-sugar supply pathway and treats downstream O-antigen, LPS,
    and specialized-polysaccharide assembly reactions as consumers, not as part of
    the biosynthetic module itself.
  module_outline: "- dTDP-L-rhamnose biosynthesis\n  - 1. dTDP-glucose formation\n\
    \  - Glucose-1-phosphate thymidylyltransferase\n    - rfbA: glucose-1-phosphate\
    \ thymidylyltransferase (molecular player: glucose-1-phosphate thymidylyltransferase\
    \ family; activity or role: glucose-1-phosphate thymidylyltransferase activity)\n\
    \  - 2. dTDP-glucose dehydration\n  - dTDP-glucose 4,6-dehydratase\n    - rffG:\
    \ dTDP-glucose 4,6-dehydratase (molecular player: dTDP-glucose 4,6-dehydratase\
    \ family; activity or role: dTDP-glucose 4,6-dehydratase activity)\n  - 3. 3,5-epimerization\n\
    \  - dTDP-4-dehydrorhamnose 3,5-epimerase\n    - rmlC: dTDP-4-dehydrorhamnose\
    \ 3,5-epimerase (molecular player: dTDP-4-dehydrorhamnose 3,5-epimerase family;\
    \ activity or role: dTDP-4-dehydrorhamnose 3,5-epimerase activity)\n    - rfbC:\
    \ dTDP-4-dehydrorhamnose 3,5-epimerase (molecular player: dTDP-4-dehydrorhamnose\
    \ 3,5-epimerase family; activity or role: dTDP-4-dehydrorhamnose 3,5-epimerase\
    \ activity)\n  - 4. final reduction to dTDP-L-rhamnose\n  - dTDP-4-dehydrorhamnose\
    \ reductase\n    - rfbD: dTDP-4-dehydrorhamnose reductase (molecular player: dTDP-4-dehydrorhamnose\
    \ reductase family; activity or role: dTDP-4-dehydrorhamnose reductase activity)\n\
    \    - PP_0500: dTDP-4-dehydrorhamnose reductase (molecular player: dTDP-4-dehydrorhamnose\
    \ reductase family; activity or role: dTDP-4-dehydrorhamnose reductase activity)"
  module_connections: '- Glucose-1-phosphate thymidylyltransferase feeds into dTDP-glucose
    4,6-dehydratase: RfbA supplies dTDP-glucose for RffG dehydration.

    - dTDP-glucose 4,6-dehydratase feeds into dTDP-4-dehydrorhamnose 3,5-epimerase:
    RffG supplies the deoxy-keto dTDP-sugar for RmlC/RfbC.

    - dTDP-4-dehydrorhamnose 3,5-epimerase feeds into dTDP-4-dehydrorhamnose reductase:
    The epimerase step supplies dTDP-4-dehydro-beta-L-rhamnose.'
  pathway_query: ppu00523
  pathway_id: ppu00523
  pathway_name: Polyketide sugar unit biosynthesis
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00523 with 4 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '6'
  candidate_genes: '- rmlC: PP_0265 | Q88R69 | dTDP-4-dehydrorhamnose 3,5-epimerase
    (EC 5.1.3.13) (Thymidine diphospho-4-keto-rhamnose 3,5-epimerase) (EC 5.1.3.13;
    primary bucket kegg:ppu00523)

    - PP_0500: PP_0500 | Q88QJ2 | dTDP-4-dehydrorhamnose reductase (EC 1.1.1.133)
    (EC 1.1.1.133; primary bucket kegg:ppu00523)

    - rfbC: PP_1782 | Q88LZ4 | dTDP-4-dehydrorhamnose 3,5-epimerase (EC 5.1.3.13)
    (Thymidine diphospho-4-keto-rhamnose 3,5-epimerase) (EC 5.1.3.13; primary bucket
    kegg:ppu00523)

    - rfbA: PP_1783 | Q88LZ3 | Glucose-1-phosphate thymidylyltransferase (EC 2.7.7.24)
    (EC 2.7.7.24; primary bucket kegg:ppu00525)

    - rfbD: PP_1784 | Q88LZ2 | dTDP-4-dehydrorhamnose reductase (EC 1.1.1.133) (EC
    1.1.1.133; primary bucket kegg:ppu00523)

    - rffG: PP_1785 | Q88LZ1 | dTDP-glucose 4,6-dehydratase (EC 4.2.1.46) (EC 4.2.1.46;
    primary bucket kegg:ppu00525)'
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__dtdp_l_rhamnose_biosynthesis__ppu00523-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__dtdp_l_rhamnose_biosynthesis__ppu00523-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

dTDP-L-rhamnose biosynthesis in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00523
- Resolved ID: ppu00523
- Resolved name: Polyketide sugar unit biosynthesis
- Source: KEGG

Resolved local bucket kegg:ppu00523 with 4 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 6

- rmlC: PP_0265 | Q88R69 | dTDP-4-dehydrorhamnose 3,5-epimerase (EC 5.1.3.13) (Thymidine diphospho-4-keto-rhamnose 3,5-epimerase) (EC 5.1.3.13; primary bucket kegg:ppu00523)
- PP_0500: PP_0500 | Q88QJ2 | dTDP-4-dehydrorhamnose reductase (EC 1.1.1.133) (EC 1.1.1.133; primary bucket kegg:ppu00523)
- rfbC: PP_1782 | Q88LZ4 | dTDP-4-dehydrorhamnose 3,5-epimerase (EC 5.1.3.13) (Thymidine diphospho-4-keto-rhamnose 3,5-epimerase) (EC 5.1.3.13; primary bucket kegg:ppu00523)
- rfbA: PP_1783 | Q88LZ3 | Glucose-1-phosphate thymidylyltransferase (EC 2.7.7.24) (EC 2.7.7.24; primary bucket kegg:ppu00525)
- rfbD: PP_1784 | Q88LZ2 | dTDP-4-dehydrorhamnose reductase (EC 1.1.1.133) (EC 1.1.1.133; primary bucket kegg:ppu00523)
- rffG: PP_1785 | Q88LZ1 | dTDP-glucose 4,6-dehydratase (EC 4.2.1.46) (EC 4.2.1.46; primary bucket kegg:ppu00525)

## Generic Module Context

### Working Scope

Species-neutral bacterial module for synthesis of the activated sugar dTDP-L-rhamnose from alpha-D-glucose 1-phosphate. The pathway proceeds through dTDP-glucose formation, dTDP-glucose 4,6-dehydration, dTDP-4-dehydrorhamnose 3,5-epimerization, and final NADPH-dependent reduction to dTDP-L-rhamnose. The module represents the soluble nucleotide-sugar supply pathway and treats downstream O-antigen, LPS, and specialized-polysaccharide assembly reactions as consumers, not as part of the biosynthetic module itself.

### Provisional Biological Outline

- dTDP-L-rhamnose biosynthesis
  - 1. dTDP-glucose formation
  - Glucose-1-phosphate thymidylyltransferase
    - rfbA: glucose-1-phosphate thymidylyltransferase (molecular player: glucose-1-phosphate thymidylyltransferase family; activity or role: glucose-1-phosphate thymidylyltransferase activity)
  - 2. dTDP-glucose dehydration
  - dTDP-glucose 4,6-dehydratase
    - rffG: dTDP-glucose 4,6-dehydratase (molecular player: dTDP-glucose 4,6-dehydratase family; activity or role: dTDP-glucose 4,6-dehydratase activity)
  - 3. 3,5-epimerization
  - dTDP-4-dehydrorhamnose 3,5-epimerase
    - rmlC: dTDP-4-dehydrorhamnose 3,5-epimerase (molecular player: dTDP-4-dehydrorhamnose 3,5-epimerase family; activity or role: dTDP-4-dehydrorhamnose 3,5-epimerase activity)
    - rfbC: dTDP-4-dehydrorhamnose 3,5-epimerase (molecular player: dTDP-4-dehydrorhamnose 3,5-epimerase family; activity or role: dTDP-4-dehydrorhamnose 3,5-epimerase activity)
  - 4. final reduction to dTDP-L-rhamnose
  - dTDP-4-dehydrorhamnose reductase
    - rfbD: dTDP-4-dehydrorhamnose reductase (molecular player: dTDP-4-dehydrorhamnose reductase family; activity or role: dTDP-4-dehydrorhamnose reductase activity)
    - PP_0500: dTDP-4-dehydrorhamnose reductase (molecular player: dTDP-4-dehydrorhamnose reductase family; activity or role: dTDP-4-dehydrorhamnose reductase activity)

### Known Relationships Among Steps

- Glucose-1-phosphate thymidylyltransferase feeds into dTDP-glucose 4,6-dehydratase: RfbA supplies dTDP-glucose for RffG dehydration.
- dTDP-glucose 4,6-dehydratase feeds into dTDP-4-dehydrorhamnose 3,5-epimerase: RffG supplies the deoxy-keto dTDP-sugar for RmlC/RfbC.
- dTDP-4-dehydrorhamnose 3,5-epimerase feeds into dTDP-4-dehydrorhamnose reductase: The epimerase step supplies dTDP-4-dehydro-beta-L-rhamnose.

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

# Species-Aware Module Review: dTDP-L-rhamnose Biosynthesis in *Pseudomonas putida* KT2440

**Taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Commissioned bucket:** KEGG ppu00523 "Polyketide sugar unit biosynthesis" (module area: other_kegg_pathway)
**True module:** dTDP-L-rhamnose biosynthesis (soluble nucleotide-sugar supply, α-D-glucose-1-phosphate → dTDP-L-rhamnose)
**Evidence tier throughout:** All KT2440 genes are UniProt Protein-Existence level **PE3 "Inferred from homology"**; no direct KT2440 enzymology exists. Functional transfer rests on strong homology to experimentally characterized *P. aeruginosa* and generic bacterial Rml enzymes.

---

## 1. Executive summary

The dTDP-L-rhamnose module is **fully satisfiable** in *P. putida* KT2440. All four canonical enzymatic steps are encoded by a single **contiguous *rmlBDAC*-type operon, PP_1785–PP_1782** (minus strand): `rffG(rmlB) – rfbD(rmlD) – rfbA(rmlA) – rfbC(rmlC)`. Each gene carries the correct family-specific InterPro/Pfam signature and the correct EC, and the operon layout is syntenic with the experimentally validated *P. aeruginosa* *rmlBDAC* cluster (PMID 11065359).

Two of the six candidate genes are **operon-external paralogs** that inflate the apparent step count: a second epimerase **PP_0265 (*rmlC*)** and a second reductase **PP_0500**. PP_0265 is a domain-confirmed, close (66.5% id) genuine RmlC. PP_0500 is a **divergent (39.7% id), genomically isolated** RmlD-family member (GenBank "…reductase-*related* protein") whose *physiological* substrate/role is unresolved.

The commissioned bucket **ppu00523 is a KEGG multi-mapping artifact**, not a real KT2440 polyketide pathway; the same shared nucleotide-sugar enzymes also map to ppu00521/00525/00520/00541. The generic module boundary (four soluble steps; LPS/O-antigen as consumers) is **correct for KT2440** and needs no revision.

**Bottom line for curation:** mark all four steps `covered` on the operon set; annotate PP_0265 as a confirmed redundant paralog; mark PP_0500 `candidate_uncertain` and promote it to full `fetch-gene` review.

---

## 2. Target-organism pathway definition

**Process included (soluble module):** the four-reaction conversion of α-D-glucose-1-phosphate into the activated deoxy-sugar donor dTDP-β-L-rhamnose:

1. **dTDP-glucose formation** — glucose-1-phosphate thymidylyltransferase, **EC 2.7.7.24** (dTTP + α-D-glucose-1-P → dTDP-α-D-glucose + PPi).
2. **4,6-dehydration** — dTDP-glucose 4,6-dehydratase, **EC 4.2.1.46** (→ dTDP-4-dehydro-6-deoxy-α-D-glucose; NAD⁺-dependent, internal redox).
3. **3,5-epimerization** — dTDP-4-dehydrorhamnose 3,5-epimerase, **EC 5.1.3.13** (→ dTDP-4-dehydro-β-L-rhamnose).
4. **Final reduction** — dTDP-4-dehydrorhamnose reductase, **EC 1.1.1.133** (NADPH-dependent → dTDP-β-L-rhamnose).

**Neighboring processes to keep separate (consumers, NOT part of the module):** downstream L-rhamnosyl transfer into LPS core/O-antigen and other glycans. In *Pseudomonas*, L-rhamnose is a documented component of the LPS core (the attachment receptor for A-band/B-band O antigen) and of O-antigen polysaccharides (*P. aeruginosa* evidence; PMID 11065359). **Note a species caveat:** rhamnolipid surfactant biosynthesis, a well-known L-rhamnose sink in *P. aeruginosa*, is **not** an established feature of *P. putida* KT2440 — do not assume it as a sink here.

**Alternate names / database definitions:**
- Gene symbols: *rmlA/rfbA* (=*rffH* variants), *rmlB/rffG*, *rmlC/rfbC*, *rmlD/rfbD*. KT2440 uses mixed *rfb*/*rff*/*rml* symbols.
- The pathway is captured as MetaCyc "dTDP-L-rhamnose biosynthesis I" and UniProt "Carbohydrate biosynthesis; dTDP-L-rhamnose biosynthesis."
- KEGG has **no dedicated dTDP-L-rhamnose map**; the enzymes appear inside ppu00521 (Streptomycin), ppu00523 (Polyketide sugar unit), ppu00525 (Acarbose/validamycin), ppu00520 (Amino/nucleotide sugar metabolism), ppu00541, and global maps 01100/01110/01250. **ppu00523 should be treated as a label, not the pathway.**

---

## 3. Expected step model (with target-taxon status)

| Step | Reaction (EC) | Expected gene family | KT2440 gene(s) | Status |
|------|---------------|----------------------|----------------|--------|
| 1 | Glc-1-P thymidylylation (2.7.7.24) | RmlA / G1P-thymidylyltransferase | **PP_1783 / rfbA** | **covered** |
| 2 | dTDP-glucose 4,6-dehydration (4.2.1.46) | RmlB / dTDP-glucose dehydratase | **PP_1785 / rffG** | **covered** |
| 3 | 3,5-epimerization (5.1.3.13) | RmlC epimerase | **PP_1782 / rfbC** (+ paralog **PP_0265 / rmlC**) | **covered** (one redundant paralog) |
| 4 | NADPH reduction (1.1.1.133) | RmlD reductase | **PP_1784 / rfbD** (+ paralog **PP_0500**) | **covered** (one uncertain paralog) |

No step is missing; no step is "not expected." The pathway is complete on the single operon PP_1782–PP_1785.

---

## 4. Candidate genes and evidence

**Operon PP_1782–PP_1785 (minus strand; syntenic *rmlBDAC*):**

- **PP_1783 / rfbA (Q88LZ3) — glucose-1-P thymidylyltransferase, EC 2.7.7.24 (Step 1).** InterPro IPR005907 (G1P_thy_trans_s), Pfam PF00483, PANTHER PTHR43532:SF1; Mg²⁺/nucleotidyltransferase keywords. UniProt catalytic-activity and dual pathway annotation (LPS O-antigen; dTDP-L-rhamnose). Evidence: homology (PE3). **Confident RmlA.** Caveat: KEGG "primary bucket" ppu00525 is a multi-mapping artifact — it is a core member of the rhamnose module.
- **PP_1785 / rffG (Q88LZ1) — dTDP-glucose 4,6-dehydratase, EC 4.2.1.46 (Step 2).** InterPro IPR005888 (dTDP_Gluc_deHydtase), Pfam PF16363, NAD-binding. Named "dTDP-glucose 4,6-dehydratase 2" in GenBank. Evidence: homology (PE3). **Confident RmlB.** Same ppu00525 multi-map caveat.
- **PP_1782 / rfbC (Q88LZ4) — dTDP-4-dehydrorhamnose 3,5-epimerase, EC 5.1.3.13 (Step 3).** InterPro IPR000888 (RmlC-like cupin), Pfam PF00908, PANTHER PTHR21047:SF2. Evidence: homology (PE3). **Confident RmlC**, and the operon-resident (physiologically committed) epimerase.
- **PP_1784 / rfbD (Q88LZ2) — dTDP-4-dehydrorhamnose reductase, EC 1.1.1.133 (Step 4).** InterPro IPR005913 (dTDP_dehydrorham_reduct) + IPR029903 (RmlD-like-bd), Pfam PF04321, NADP. Evidence: homology (PE3). **Confident RmlD**, operon-resident committed reductase.

**Operon-external paralogs:**

- **PP_0265 / rmlC (Q88R69) — EC 5.1.3.13, ~319.8 kb.** Identical domain architecture to PP_1782 (IPR000888/PF00908/PTHR21047:SF2); **66.5% aa identity** to PP_1782. **A genuine second RmlC epimerase.** Genomic neighbors are unrelated (ADP-sugar pyrophosphorylase, siderophore receptor, sensor kinases) — not in a deoxy-sugar cluster; likely a redundant/spare epimerase or one channeled to another dTDP-4-keto-6-deoxy-hexose.
- **PP_0500 (Q88QJ2) — EC 1.1.1.133, ~589.9 kb.** Carries the diagnostic RmlD-family signature (IPR005913/PF04321), so the reductase family assignment is **domain-supported**; however it is only **39.7% identical** to the operon RmlD (PP_1784) — barely above background — has **no gene symbol**, GenBank name "dTDP-4-rhamnose reductase-**related** protein," UniProt annotation score 2.0, and sits beside a pseudogene (PP_0499) and a lone NAD-epimerase (PP_0501) with **no cognate RmlA/RmlB partner**. **Genuine RmlD-family, but physiological substrate/role uncertain.**

**Broad/spurious mappings noted:** Both reductases inherit a wrong PANTHER *subfamily* tag PTHR10491:SF4 "methionine adenosyltransferase 2 subunit beta" (a PANTHER SF mis-grouping artifact; the family PTHR10491 = dTDP-4-dehydrorhamnose reductase is correct). Do not propagate the SF4 label.

---

## 5. Gaps, ambiguities, and likely over-annotations

- **No true pathway gap.** All four steps are covered by the operon.
- **Paralog ambiguity (Step 3 and Step 4).** Two epimerases and two reductases. The operon copies (PP_1782, PP_1784) are the committed enzymes; PP_0265 and PP_0500 are extra copies. Curatorially, steps should not be double-counted.
- **PP_0500 is the key uncertainty.** Domain signature supports EC 1.1.1.133, but low identity + orphan location + "related protein" naming leave open whether it (a) is a redundant dTDP-L-rhamnose reductase, or (b) reduces a different dTDP-4-keto-6-deoxy-sugar. This is the most likely locus of over-precise EC transfer.
- **KEGG bucket over-interpretation.** ppu00523 "Polyketide sugar unit biosynthesis" does **not** imply KT2440 makes polyketide sugars, streptomycin, acarbose, or validamycin (ppu00521/00525) — these are shared-enzyme labels. Treat ppu00523 as a boundary artifact.
- **Evidence ceiling.** Every conclusion for KT2440 is homology-based (PE3). No target-strain knockout, complementation, or enzymology exists.

---

## 6. Module and GO-curation recommendations

**Per-step module status:**
- Step 1 (EC 2.7.7.24) → **covered** by PP_1783/rfbA.
- Step 2 (EC 4.2.1.46) → **covered** by PP_1785/rffG.
- Step 3 (EC 5.1.3.13) → **covered** by PP_1782/rfbC; annotate **PP_0265** as a confirmed redundant paralog (secondary, not step-satisfying on its own).
- Step 4 (EC 1.1.1.133) → **covered** by PP_1784/rfbD; annotate **PP_0500** as **candidate_uncertain** paralog.

**Module boundaries:** the generic four-step module (α-D-glucose-1-P → dTDP-L-rhamnose; LPS/O-antigen as consumers) is **correct for KT2440 — no revision needed** (`module_needs_revision = No`). Fold rfbA/rffG into this module regardless of their ppu00525 KEGG tag.

**Bucket handling:** reassign the working bucket from KEGG ppu00523 to the MetaCyc/UniProt "dTDP-L-rhamnose biosynthesis" definition, or explicitly annotate ppu00523 as a shared-enzyme label.

**GO curation:** existing GO/EC assignments (GO:0008830 dTDP-4-dehydrorhamnose 3,5-epimerase; GO:0008831 dTDP-4-dehydrorhamnose reductase; GO:0008879 glucose-1-phosphate thymidylyltransferase; GO:0008460 dTDP-glucose 4,6-dehydratase) are appropriate for the operon genes. **No new GO term request is needed.** For PP_0500, prefer the family-level term with an IEA/ISS evidence code and a curator note on substrate uncertainty rather than an over-specific assertion.

---

## 7. Genes to promote to full `fetch-gene` review

1. **PP_0500 (highest priority)** — divergent, orphan RmlD-family paralog; resolve whether it is a redundant dTDP-L-rhamnose reductase or a reductase for a different dTDP-4-keto-6-deoxy-sugar. Check catalytic residues, cofactor (NADPH vs NADH), operonic context of neighbor PP_0501, and any phenotype data.
2. **PP_0265** — confirm second RmlC and clarify why KT2440 retains two epimerases (redundancy vs distinct sugar route); moderate priority.
3. (Optional) **PP_1782–PP_1785 operon** — a single consolidated fetch-gene review to attach the operon/synteny evidence and mark the four steps covered.

---

## 8. Key references

- **Rahim R, Burrows LL, Monteiro MA, Perry MB, Lam JS.** Involvement of the *rml* locus in core oligosaccharide and O polysaccharide assembly in *Pseudomonas aeruginosa*. *Microbiology* 2000. **PMID 11065359.** — Characterizes the *rmlBDAC* operon making dTDP-L-Rha; L-Rha is the LPS-core receptor for O-antigen attachment. *Species transfer to KT2440: strong (same genus, syntenic operon), but still homology-level for KT2440.*
- **Dong C, et al. (Naismith group).** RmlC epimerase mechanism via an unusual twist-boat intermediate. *(2007).* **PMID 17046787.** — Mechanism/validated drug target for the EC 5.1.3.13 step. *Generic bacterial evidence.*
- **Christendat D, et al.** Crystal structure of dTDP-4-keto-6-deoxy-hexulose 3,5-epimerase (RmlC). *(2000).* **PMID 10827167.** — Structural basis and conserved active site of RmlC. *Generic bacterial evidence.*
- **UniProt** entries Q88LZ3 (rfbA), Q88LZ1 (rffG), Q88LZ4 (rfbC), Q88LZ2 (rfbD), Q88R69 (rmlC/PP_0265), Q88QJ2 (PP_0500) — annotations, EC, InterPro/Pfam, PE3 evidence tier.
- **KEGG** ppu:PP_0265/PP_0500/PP_1782-1785 — genomic coordinates, operon synteny, and multi-map pathway memberships (ppu00521/00523/00525/00520/00541).
- **InterPro/Pfam** families: IPR005907/PF00483 (RmlA), IPR005888/PF16363 (RmlB), IPR000888/PF00908 (RmlC), IPR005913/PF04321 (RmlD).

---

### Evidence provenance summary
- **Direct KT2440 experiment:** none identified.
- **Homology/synteny (strong):** operon completeness and step assignments, transferred from *P. aeruginosa* *rmlBDAC* + universal Rml family signatures.
- **Database/computational:** EC, InterPro/Pfam domains, genomic coordinates, pairwise identities (Needleman-Wunsch computed here).
- **Open questions for experts:** (1) in-vivo substrate/role of PP_0500; (2) reason for retained duplicate epimerase PP_0265; (3) the physiological L-rhamnose sink(s) in KT2440 (LPS core/O-antigen assumed; rhamnolipid unconfirmed).


## Artifacts

- [OpenScientist final report](PSEPK__dtdp_l_rhamnose_biosynthesis__ppu00523-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__dtdp_l_rhamnose_biosynthesis__ppu00523-deep-research-openscientist_artifacts/final_report.pdf)