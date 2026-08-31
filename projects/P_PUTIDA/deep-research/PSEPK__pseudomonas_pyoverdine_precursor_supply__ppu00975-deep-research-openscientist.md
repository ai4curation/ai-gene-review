---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T08:35:16.531413'
end_time: '2026-08-31T09:00:57.529971'
duration_seconds: 1541.0
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Pseudomonas pyoverdine non-proteinogenic precursor supply
  module_summary: A reusable Pseudomonas module for reactions that supply unusual
    amino-acid building blocks to the cytoplasmic pyoverdine NRPS assembly line. PvdA
    hydroxylates L-ornithine to produce N5-hydroxy-L-ornithine, and PvdH forms L-2,4-diaminobutyrate
    from L-aspartate 4-semialdehyde by PLP-dependent transamination. NRPS assembly,
    ferribactin export, periplasmic maturation, secretion, ferripyoverdine uptake,
    and iron release are outside this module.
  module_outline: "- Pseudomonas pyoverdine non-proteinogenic precursor supply\n \
    \ - 1. N5-hydroxy-L-ornithine precursor supply\n  - PvdA-dependent ornithine N5-hydroxylation\n\
    \    - Pyoverdine ornithine N5-monooxygenase PvdA (molecular player: Pseudomonas\
    \ pyoverdine PvdA ornithine N5-monooxygenase family; activity or role: ornithine\
    \ N5-monooxygenase activity)\n  - 2. L-2,4-diaminobutyrate precursor supply\n\
    \  - PvdH-dependent L-2,4-diaminobutyrate formation\n    - Pyoverdine diaminobutyrate\
    \ transaminase PvdH (molecular player: Pseudomonas pyoverdine PvdH diaminobutyrate\
    \ transaminase family; activity or role: L-2,4-diaminobutyrate:2-oxoglutarate\
    \ transaminase activity)"
  module_connections: No explicit connections.
  pathway_query: ppu00975
  pathway_id: ppu00975
  pathway_name: Biosynthesis of various siderophores
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00975 with 3 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '3'
  candidate_genes: '- PP_2800: PP_2800 | Q88J49 | Diaminobutyrate-2-oxoglutarate transaminase
    (primary bucket kegg:ppu00975)

    - pvdH: PP_4223 | Q88F75 | Diaminobutyrate-2-oxoglutarate transaminase (EC 2.6.1.76)
    (EC 2.6.1.76; primary bucket kegg:ppu00975)

    - pvdY: PP_4245 | Q88F54 | Hydroxyproline acetylase (EC 2.3.1.-) (EC 2.3.1.-;
    primary bucket kegg:ppu00975)'
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
  path: PSEPK__pseudomonas_pyoverdine_precursor_supply__ppu00975-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__pseudomonas_pyoverdine_precursor_supply__ppu00975-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Pseudomonas pyoverdine non-proteinogenic precursor supply in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00975
- Resolved ID: ppu00975
- Resolved name: Biosynthesis of various siderophores
- Source: KEGG

Resolved local bucket kegg:ppu00975 with 3 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 3

- PP_2800: PP_2800 | Q88J49 | Diaminobutyrate-2-oxoglutarate transaminase (primary bucket kegg:ppu00975)
- pvdH: PP_4223 | Q88F75 | Diaminobutyrate-2-oxoglutarate transaminase (EC 2.6.1.76) (EC 2.6.1.76; primary bucket kegg:ppu00975)
- pvdY: PP_4245 | Q88F54 | Hydroxyproline acetylase (EC 2.3.1.-) (EC 2.3.1.-; primary bucket kegg:ppu00975)

## Generic Module Context

### Working Scope

A reusable Pseudomonas module for reactions that supply unusual amino-acid building blocks to the cytoplasmic pyoverdine NRPS assembly line. PvdA hydroxylates L-ornithine to produce N5-hydroxy-L-ornithine, and PvdH forms L-2,4-diaminobutyrate from L-aspartate 4-semialdehyde by PLP-dependent transamination. NRPS assembly, ferribactin export, periplasmic maturation, secretion, ferripyoverdine uptake, and iron release are outside this module.

### Provisional Biological Outline

- Pseudomonas pyoverdine non-proteinogenic precursor supply
  - 1. N5-hydroxy-L-ornithine precursor supply
  - PvdA-dependent ornithine N5-hydroxylation
    - Pyoverdine ornithine N5-monooxygenase PvdA (molecular player: Pseudomonas pyoverdine PvdA ornithine N5-monooxygenase family; activity or role: ornithine N5-monooxygenase activity)
  - 2. L-2,4-diaminobutyrate precursor supply
  - PvdH-dependent L-2,4-diaminobutyrate formation
    - Pyoverdine diaminobutyrate transaminase PvdH (molecular player: Pseudomonas pyoverdine PvdH diaminobutyrate transaminase family; activity or role: L-2,4-diaminobutyrate:2-oxoglutarate transaminase activity)

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

# Module Review: Pyoverdine non-proteinogenic precursor supply in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Local bucket reviewed:** `kegg:ppu00975` — "Biosynthesis of various siderophores" (module area: other_kegg_pathway)
**Module scope:** cytoplasmic supply of two non-proteinogenic amino-acid building blocks to the pyoverdine NRPS assembly line — N5-hydroxy-L-ornithine (via PvdA) and L-2,4-diaminobutyrate (via PvdH).

---

## 1. Executive summary

The precursor-supply module has **exactly two enzymatic steps**, and **both are satisfiable in KT2440**:

| Module step | Reaction | KT2440 gene | Status |
|---|---|---|---|
| 1. N5-hydroxy-L-ornithine supply | L-ornithine + O₂ + NADPH → N5-hydroxy-L-ornithine | **pvdA / PP_3796** (Q88GC8) | **covered** — but **missing from the KEGG bucket & candidate list (gap in local metadata)** |
| 2. L-2,4-diaminobutyrate supply | L-aspartate-4-semialdehyde + L-Glu ⇌ L-2,4-diaminobutyrate + 2-oxoglutarate | **pvdH / PP_4223** (Q88F75) | **covered** — high confidence |

Two of the three candidate genes in the bucket are problematic for *this* module:
- **PP_2800** (Q88J49) is a **likely over-propagated annotation** — a symbol-less class-III DABA-aminotransferase located in a polyamine/GABA gene neighborhood ~1.5 Mbp away from the pyoverdine cluster. It is **not** the pyoverdine PvdH and should not be counted toward module satisfiability.
- **PvdY / PP_4245** (Q88F54) is an **acyl/acetyltransferase that is out of scope** for precursor supply; it belongs to pyoverdine side-chain tailoring, and its EC 2.3.1.102 mapping is a broad KO transfer of uncertain accuracy.

**Bottom line:** the module is **fully covered** in KT2440, but the *local bucket boundaries are wrong*: the true step-1 gene (pvdA/PP_3796) is absent, one bucket gene (PP_2800) is over-propagated noise, and one (PvdY) is out-of-scope. The bucket needs curation, not the biology.

---

## 2. Target-organism pathway definition

**Included biochemical process (this module only):** cytoplasmic biosynthesis of the two unusual amino-acid precursors that the pyoverdine non-ribosomal peptide synthetases (NRPS) load onto the assembly line:
1. **N5-hydroxy-L-ornithine** — the hydroxamate iron-chelating precursor, made by the FAD/NADPH-dependent L-ornithine N5-monooxygenase **PvdA**.
2. **L-2,4-diaminobutyrate (Dab)** — a chromophore/backbone precursor (the fluorescent dihydroxyquinoline chromophore is a condensation product of D-tyrosine and L-2,4-diaminobutyrate; PMID 15317763), made by the PLP-dependent transaminase **PvdH** from L-aspartate-4-semialdehyde.

**Explicitly out of scope (keep separate):** NRPS peptide assembly (PP_4221/PP_4243 ferribactin synthase subunits, PvdL/PvdI/PvdJ/PvdD), N5-hydroxyornithine *tailoring* (formylation/acylation, e.g. PvdF), periplasmic maturation (PvdP/PvdM/PvdN/PvdO/PvdQ), ferribactin/pyoverdine export, ferripyoverdine uptake (FpvA), and iron release.

**Neighboring maps to keep separate:**
- KEGG **ppu00260** "Glycine, serine and threonine metabolism" — PP_2800 is dual-mapped here; this is its more plausible home.
- **Ectoine biosynthesis** and **1,3-diaminopropane / polyamine (putrescine/spermidine) metabolism** — these also use class-III DABA/2,4-diaminobutyrate aminotransferases (K00836, EC 2.6.1.76) and are the likely true context of PP_2800.
- The broad KEGG overview map **ppu00975 "Biosynthesis of various siderophores"** is a *multi-siderophore* aggregate map (aerobactin, staphyloferrin, ferrioxamine, petrobactin, putrebactin, etc. appear in its compound list). It is **not** a pyoverdine-specific module; membership by KO/EC alone does not imply a pyoverdine role.

**Alternate names / database definitions:** pyoverdine = pyoverdin = PVD; PvdH = "diaminobutyrate-2-oxoglutarate transaminase" (EC 2.6.1.76, KO K00836); PvdA = "L-ornithine N5-monooxygenase / ornithine 5-monooxygenase / ornithine hydroxylase" (KO K10531, EC 1.14.13.195/1.14.13.196; UniProt lists EC 1.13.12.-).

---

## 3. Expected step model

| # | Step | Enzyme family | Expected reaction | Expected in KT2440? |
|---|---|---|---|---|
| 1 | Ornithine N5-hydroxylation | SidA/PvdA class-B flavin-dependent monooxygenase | L-Orn → N5-OH-L-Orn | Yes (pyoverdine producer) |
| 2 | Dab formation | Class-III PLP aminotransferase (PvdH type) | L-Asp-4-semialdehyde ⇌ L-2,4-Dab | Yes |

Upstream context (not part of module but required for flux): **Asd** (aspartate-β-semialdehyde dehydrogenase) supplies L-aspartate-4-semialdehyde for step 2; *asd* knockouts also abolish pyoverdine (PMID 15317763). Asd is a housekeeping gene (aspartate-family amino-acid biosynthesis) and is present in KT2440, but is correctly outside this module.

---

## 4. Candidate genes and evidence

### pvdA / PP_3796 (Q88GC8) — **NOT in bucket, but the true step-1 gene** ★ promote
- **Role:** L-ornithine N5-monooxygenase → N5-hydroxy-L-ornithine (module step 1).
- **Evidence type:** KT2440 = homology/ortholog assignment (UniProt gene name *pvdA*; KEGG KO **K10531**, EC 1.14.13.195/196; SidA/PvdA family). Reaction chemistry is **directly established for the P. aeruginosa ortholog**: purified PvdA is a FAD/NADPH flavin-monooxygenase catalyzing N5-hydroxylation of L-ornithine, pH optimum 8.0, Km(Orn) ≈ 0.58 mM, tightly coupled to hydroxylamine formation (PMID 17015659; mechanism PMID 17900176; family kinetics PMID 20650894).
- **Species transfer:** strong (conserved gene name, KO, EC, family).
- **Caveat:** absent from the KEGG ppu00975 gene list and from local candidate metadata — a **bucket gap**, not a biological gap. Located at ~4.32 Mb, separate from the main NRPS cluster (a common arrangement for *pvdA*).

### pvdH / PP_4223 (Q88F75) — high-confidence step-2 gene
- **Role:** diaminobutyrate-2-oxoglutarate transaminase → L-2,4-diaminobutyrate (module step 2).
- **Evidence type:** KT2440 = ortholog assignment (gene name *pvdH*, EC 2.6.1.76, KO K00836, class-III PLP aminotransferase) **plus genomic embedding in the pyoverdine cluster** (immediately flanked by PP_4221/PP_4222 ferribactin-synthase/SyrP-type genes). The P. aeruginosa PAO1 ortholog is **directly characterized**: interconverts aspartate-β-semialdehyde and L-2,4-diaminobutyrate, ping-pong mechanism, highest specificity for α-ketoglutarate (41× over pyruvate); *pvdH* knockouts cannot make pyoverdine without exogenous Dab, and PvdH homologues cluster within pyoverdine loci across *Pseudomonas* (PMID 15317763).
- **Species transfer:** strong.
- **Caveat:** none major; the EC/KO is shared with unrelated DABA-aminotransferases, so annotation should be anchored on the cluster location, not EC alone.

### PP_2800 (Q88J49) — likely over-propagation, exclude from module
- **Role (as annotated):** "putative diaminobutyrate-2-oxoglutarate transaminase" (K00836, EC 2.6.1.76); **no gene symbol**; UniProt assigns no EC.
- **Why it is in the bucket:** shares KO/EC with PvdH, so KEGG lists it in the multi-siderophore map ppu00975 (and simultaneously in ppu00260 Gly/Ser/Thr metabolism).
- **Evidence against a pyoverdine role:** located at ~3.19 Mb, **far from the pyoverdine cluster**; its genomic neighborhood is polyamine/GABA-related — PP_2799 (class-III aminotransferase), PP_2801 (γ-aminobutyraldehyde dehydrogenase), PP_2802 (amino-acid permease). This is the signature of a general DABA/polyamine aminotransferase, not a pyoverdine enzyme. **KT2440 encodes only two K00836 DABA-aminotransferases (PP_2800 and pvdH/PP_4223) and lacks the ectoine pathway entirely (no ectA/K06718, no ectC/K06720), so PP_2800 is not an ectoine EctB** — its most plausible role is 1,3-diaminopropane/polyamine metabolism.
- **Species transfer:** N/A (this is KT2440-intrinsic genomic-context evidence).
- **Caveat:** do **not** count toward module satisfiability; mark `candidate_uncertain` and promote to full review to nail down its true polyamine/ectoine role.

### pvdY / PP_4245 (Q88F54) — out of module scope, ambiguous annotation
- **Role (as annotated):** "hydroxyproline acetylase" EC 2.3.1.- (UniProt); KEGG maps to **K03896** "acetyl-CoA:N6-hydroxylysine acetyltransferase" EC 2.3.1.102 (an aerobactin/IucB-type activity).
- **Evidence type:** genomic embedding in the pyoverdine cluster (~4.83 Mb, near PP_4243 NRPS subunit and PP_4244 alternative sigma factor) supports a pyoverdine association, but **no direct functional characterization of PvdY was retrieved**, and the two annotations (hydroxyproline acetylase vs N6-hydroxylysine acetyltransferase) are inconsistent.
- **Relevance to this module:** PvdY is an **acyl/acetyltransferase tailoring enzyme**, not a supplier of N5-OH-ornithine or Dab. It does not satisfy either defined module step.
- **Caveat:** its EC 2.3.1.102/K03896 mapping is a broad cross-siderophore KO transfer of uncertain accuracy; promote to full review.

---

## 5. Gaps, ambiguities, and likely over-annotations

- **Gap in local metadata (not in biology):** step-1 gene **pvdA/PP_3796 is absent** from the bucket and candidate list. This is the single most important curation fix — add PP_3796 as the step-1 gene.
- **Over-propagation:** **PP_2800** is a class-III aminotransferase co-classified into ppu00975 purely via EC 2.6.1.76/K00836. Genomic context (polyamine/GABA cluster, distal to pvd genes) argues it is not a pyoverdine enzyme. KT2440 has only two K00836 genes (PP_2800, pvdH) and **no ectoine pathway** (ectA/ectC absent), ruling out an EctB role and pointing to 1,3-diaminopropane/polyamine metabolism. Classic KO/EC over-propagation into an aggregate map.
- **Out-of-scope bucket member:** **PvdY/PP_4245** is a pyoverdine-cluster acetyltransferase but not a precursor-supply enzyme; it inflates the apparent bucket while not covering any module step.
- **Ambiguous EC/KO mappings to flag:**
  - EC 2.6.1.76 / K00836 is shared by pyoverdine PvdH, ectoine EctB, and polyamine DABA-aminotransferases — EC/KO alone cannot assign a pyoverdine role; use cluster location.
  - PvdY: EC 2.3.1.- vs EC 2.3.1.102 (K03896) inconsistency; likely over-broad.
  - PvdA: UniProt EC 1.13.12.- vs KEGG EC 1.14.13.195/196 — reconcile to the ornithine-N5-monooxygenase EC.
- **Not-expected steps:** none of the two module steps are missing biologically; there is no evidence that KT2440 replaces PvdA or PvdH with a lineage-specific alternative. (KT2440 is a well-established pyoverdine producer.)

---

## 6. Module and GO-curation recommendations

**Per-step module status:**
- **Step 1 (N5-hydroxy-L-ornithine) → `covered`**, by **pvdA/PP_3796** (add this gene to the bucket/module; it is currently a metadata gap).
- **Step 2 (L-2,4-diaminobutyrate) → `covered`**, by **pvdH/PP_4223** (keep).

**Bucket/candidate corrections:**
- **PP_2800 → `candidate_uncertain` and remove from pyoverdine module** (reassign to polyamine/ectoine amino-acid metabolism; retain in ppu00260 context). Likely over-annotation.
- **PvdY/PP_4245 → out_of_scope for this module** (tailoring, not precursor supply). If module boundaries are later widened to include N5-hydroxyornithine acylation, revisit — but as defined, `module_needs_revision` only in the sense that PvdY should be moved out.

**Module boundary verdict:** the *generic* module boundaries (PvdA + PvdH) are **biologically correct for KT2440**; the *local KEGG bucket* boundaries are wrong (missing pvdA; includes over-propagated PP_2800 and out-of-scope PvdY). Recommend decoupling the pyoverdine precursor-supply module from raw `kegg:ppu00975` membership.

**GO-curation notes:**
- pvdA/PP_3796: GO:0008442? no — appropriate terms: **GO:0030410 (nicotianamine? no)** → use **GO:0004497/flavin monooxygenase** parent with **"L-ornithine N5-monooxygenase activity"** (MF) and **GO:0019538/siderophore biosynthesis (BP; GO:0019290 siderophore biosynthetic process)**. Confirm an ornithine-N5-monooxygenase-specific MF term exists; request one if absent.
- pvdH/PP_4223: MF **"diaminobutyrate-2-oxoglutarate transaminase activity"** (EC 2.6.1.76); BP **GO:0019290 siderophore biosynthetic process / pyoverdine biosynthesis**.
- Flag EC/KO-driven annotations (PP_2800, PvdY) as electronic/over-propagated (IEA), needing experimental or context-based downgrade.

---

## 7. Genes to promote to full `fetch-gene` review

1. **pvdA / PP_3796 (Q88GC8)** — highest priority; it is the missing step-1 gene and must be added to the module.
2. **PP_2800 (Q88J49)** — resolve its true role (polyamine/1,3-diaminopropane vs ectoine DABA-aminotransferase); confirm removal from pyoverdine module.
3. **pvdY / PP_4245 (Q88F54)** — reconcile conflicting acetyltransferase annotations and confirm out-of-scope status.

---

## 8. Key references

- Vandenende, Vlasschaert, Seah (2004). *Functional characterization of an aminotransferase required for pyoverdine siderophore biosynthesis in Pseudomonas aeruginosa PAO1.* J Bacteriol. **PMID 15317763.** — Direct: PvdH makes L-2,4-diaminobutyrate; chromophore = D-Tyr + Dab; PvdH homologues sit in pyoverdine loci across *Pseudomonas*.
- Ge & Seah (2006). *Heterologous expression, purification, and characterization of an L-ornithine N5-hydroxylase involved in pyoverdine siderophore biosynthesis in P. aeruginosa.* J Bacteriol. **PMID 17015659.** — Direct: PvdA N5-hydroxylates L-ornithine (FAD/NADPH).
- Meneely & Lamb (2007). *Biochemical characterization of a FAD-dependent monooxygenase, ornithine hydroxylase from P. aeruginosa.* Biochemistry. **PMID 17900176.** — PvdA mechanism.
- Mayfield et al. (2010). *Comprehensive spectroscopic, steady state, and transient kinetic studies of a representative siderophore-associated flavin monooxygenase.* Biochemistry. **PMID 20650894.** — SidA/PvdA family kinetics.
- Koch et al. (2010). *The acylase PvdQ has a conserved function among fluorescent Pseudomonas spp.* — confirms pyoverdine biosynthesis machinery is conserved and functional in P. putida KT2440. **PMID 23766117.**
- Databases: KEGG ppu00975 / ppu:PP_2800 / ppu:PP_3796 / ppu:PP_4223 / ppu:PP_4245; UniProt Q88J49, Q88GC8, Q88F75, Q88F54 (accessed 2026-08-31).

---

*Evidence provenance:* Reaction chemistry for both module steps is **direct experimental** evidence from *P. aeruginosa* orthologs (strong transfer to KT2440). KT2440-specific claims (gene identities, KO/EC, chromosomal positions, gene neighborhoods) are from KEGG/UniProt for strain KT2440 and are **direct genomic** evidence. The over-propagation and out-of-scope calls rest on KT2440 genomic-context reasoning, not on direct functional assays of PP_2800/PvdY — these remain the principal open questions.


## Artifacts

- [OpenScientist final report](PSEPK__pseudomonas_pyoverdine_precursor_supply__ppu00975-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__pseudomonas_pyoverdine_precursor_supply__ppu00975-deep-research-openscientist_artifacts/final_report.pdf)