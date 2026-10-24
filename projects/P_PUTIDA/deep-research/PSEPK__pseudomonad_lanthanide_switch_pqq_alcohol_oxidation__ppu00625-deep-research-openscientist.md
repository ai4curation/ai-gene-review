---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T06:18:00.390004'
end_time: '2026-08-31T06:41:41.730933'
duration_seconds: 1421.34
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Pseudomonad lanthanide-switch PQQ alcohol oxidation
  module_summary: A reusable pseudomonad module coupling PedS2/PedR2 two-component
    signaling to metal-conditioned periplasmic alcohol oxidation. In the absence of
    usable lanthanides, phosphorylated PedR2 favors expression of the calcium-dependent
    PQQ alcohol dehydrogenase PedE. Lanthanide availability shifts the system toward
    the lanthanide-dependent paralog PedH. Both enzymes oxidize diverse alcohols in
    the periplasm and pass electrons to cytochrome c. PQQ biosynthesis, downstream
    aldehyde metabolism, and lanthanide uptake are adjacent systems and are outside
    this module.
  module_outline: "- Pseudomonad lanthanide-switch PQQ alcohol oxidation\n  - 1. lanthanide-responsive\
    \ PedS2 sensor signaling\n  - PedS2 sensor-kinase signaling\n    - PedS2 phosphorelay\
    \ sensor kinase (molecular player: pseudomonad PedS2 sensor-kinase family; activity\
    \ or role: phosphorelay sensor kinase activity)\n  - 2. PedR2 transcriptional\
    \ switch output\n  - PedR2-dependent transcriptional control\n    - PedR2 phosphorelay\
    \ response regulator (molecular player: pseudomonad PedR2 response-regulator family;\
    \ activity or role: phosphorelay response regulator activity)\n  - 3. metal-conditioned\
    \ periplasmic PQQ alcohol oxidation\n  - Alternative PedE/PedH alcohol oxidation\n\
    \    - Alternative versions by catalytic metal availability: Ped alcohol-dehydrogenase\
    \ metal variants\n      - Calcium-dependent PedE alcohol oxidation\n        -\
    \ Calcium-dependent PQQ alcohol dehydrogenase PedE (molecular player: calcium-dependent\
    \ PedE-type PQQ alcohol dehydrogenase family; activity or role: alcohol dehydrogenase\
    \ (cytochrome c) activity)\n      - Lanthanide-dependent PedH alcohol oxidation\n\
    \        - Lanthanide-dependent PQQ alcohol dehydrogenase PedH (molecular player:\
    \ lanthanide-dependent PedH-type PQQ alcohol dehydrogenase family; activity or\
    \ role: alcohol dehydrogenase (cytochrome c) activity)"
  module_connections: '- PedS2 sensor-kinase signaling promotes PedR2-dependent transcriptional
    control: PedS2-dependent phosphorylation activates PedR2 output in the lanthanide-free
    state.

    - PedR2-dependent transcriptional control promotes Calcium-dependent PedE alcohol
    oxidation: Phosphorylated PedR2 promotes the calcium-dependent PedE branch.

    - PedR2-dependent transcriptional control inhibits Lanthanide-dependent PedH alcohol
    oxidation: PedR2 contributes to repression of the PedH branch without lanthanides.'
  pathway_query: ppu00625
  pathway_id: ppu00625
  pathway_name: Chloroalkane and chloroalkene degradation
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00625 with 3 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '5'
  candidate_genes: '- fdhA: PP_0328 | Q88R06 | Formaldehyde dehydrogenase (EC 1.2.1.46)
    (EC 1.2.1.46; primary bucket kegg:ppu00625)

    - frmA: PP_1616 | Q88MF5 | S-(hydroxymethyl)glutathione dehydrogenase (EC 1.1.1.1)
    (EC 1.1.1.284) (Alcohol dehydrogenase class-3) (Alcohol dehydrogenase class-III)
    (Glutathione-dependent formaldehyde dehydrogenase) (EC 1.1.1.1; 1.1.1.284; primary
    bucket kegg:ppu00626)

    - pedE: PP_2674 | Q88JH5 | Quinoprotein alcohol dehydrogenase PedE (EC 1.1.2.8)
    (Ca(2+)-dependent pyrroloquinoline quinone-dependent alcohol dehydrogenase) (Ca(2+)-dependent
    PQQ-ADH) (EC 1.1.2.8; primary bucket kegg:ppu00625)

    - pedH: PP_2679 | Q88JH0 | Quinoprotein alcohol dehydrogenase PedH (EC 1.1.2.-)
    (Lanthanide-dependent pyrroloquinoline quinone-dependent alcohol dehydrogenase)
    (Lanthanide-dependent PQQ-ADH) (EC 1.1.2.-; primary bucket kegg:ppu00625)

    - adhP: PP_3839 | Q88G86 | Short-chain alcohol dehydrogenase (EC 1.1.1.-, EC 1.1.1.1)
    (EC 1.1.1.-; 1.1.1.1; primary bucket kegg:ppu00626)'
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
citation_count: 2
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__pseudomonad_lanthanide_switch_pqq_alcohol_oxidation__ppu00625-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__pseudomonad_lanthanide_switch_pqq_alcohol_oxidation__ppu00625-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Pseudomonad lanthanide-switch PQQ alcohol oxidation in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00625
- Resolved ID: ppu00625
- Resolved name: Chloroalkane and chloroalkene degradation
- Source: KEGG

Resolved local bucket kegg:ppu00625 with 3 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 5

- fdhA: PP_0328 | Q88R06 | Formaldehyde dehydrogenase (EC 1.2.1.46) (EC 1.2.1.46; primary bucket kegg:ppu00625)
- frmA: PP_1616 | Q88MF5 | S-(hydroxymethyl)glutathione dehydrogenase (EC 1.1.1.1) (EC 1.1.1.284) (Alcohol dehydrogenase class-3) (Alcohol dehydrogenase class-III) (Glutathione-dependent formaldehyde dehydrogenase) (EC 1.1.1.1; 1.1.1.284; primary bucket kegg:ppu00626)
- pedE: PP_2674 | Q88JH5 | Quinoprotein alcohol dehydrogenase PedE (EC 1.1.2.8) (Ca(2+)-dependent pyrroloquinoline quinone-dependent alcohol dehydrogenase) (Ca(2+)-dependent PQQ-ADH) (EC 1.1.2.8; primary bucket kegg:ppu00625)
- pedH: PP_2679 | Q88JH0 | Quinoprotein alcohol dehydrogenase PedH (EC 1.1.2.-) (Lanthanide-dependent pyrroloquinoline quinone-dependent alcohol dehydrogenase) (Lanthanide-dependent PQQ-ADH) (EC 1.1.2.-; primary bucket kegg:ppu00625)
- adhP: PP_3839 | Q88G86 | Short-chain alcohol dehydrogenase (EC 1.1.1.-, EC 1.1.1.1) (EC 1.1.1.-; 1.1.1.1; primary bucket kegg:ppu00626)

## Generic Module Context

### Working Scope

A reusable pseudomonad module coupling PedS2/PedR2 two-component signaling to metal-conditioned periplasmic alcohol oxidation. In the absence of usable lanthanides, phosphorylated PedR2 favors expression of the calcium-dependent PQQ alcohol dehydrogenase PedE. Lanthanide availability shifts the system toward the lanthanide-dependent paralog PedH. Both enzymes oxidize diverse alcohols in the periplasm and pass electrons to cytochrome c. PQQ biosynthesis, downstream aldehyde metabolism, and lanthanide uptake are adjacent systems and are outside this module.

### Provisional Biological Outline

- Pseudomonad lanthanide-switch PQQ alcohol oxidation
  - 1. lanthanide-responsive PedS2 sensor signaling
  - PedS2 sensor-kinase signaling
    - PedS2 phosphorelay sensor kinase (molecular player: pseudomonad PedS2 sensor-kinase family; activity or role: phosphorelay sensor kinase activity)
  - 2. PedR2 transcriptional switch output
  - PedR2-dependent transcriptional control
    - PedR2 phosphorelay response regulator (molecular player: pseudomonad PedR2 response-regulator family; activity or role: phosphorelay response regulator activity)
  - 3. metal-conditioned periplasmic PQQ alcohol oxidation
  - Alternative PedE/PedH alcohol oxidation
    - Alternative versions by catalytic metal availability: Ped alcohol-dehydrogenase metal variants
      - Calcium-dependent PedE alcohol oxidation
        - Calcium-dependent PQQ alcohol dehydrogenase PedE (molecular player: calcium-dependent PedE-type PQQ alcohol dehydrogenase family; activity or role: alcohol dehydrogenase (cytochrome c) activity)
      - Lanthanide-dependent PedH alcohol oxidation
        - Lanthanide-dependent PQQ alcohol dehydrogenase PedH (molecular player: lanthanide-dependent PedH-type PQQ alcohol dehydrogenase family; activity or role: alcohol dehydrogenase (cytochrome c) activity)

### Known Relationships Among Steps

- PedS2 sensor-kinase signaling promotes PedR2-dependent transcriptional control: PedS2-dependent phosphorylation activates PedR2 output in the lanthanide-free state.
- PedR2-dependent transcriptional control promotes Calcium-dependent PedE alcohol oxidation: Phosphorylated PedR2 promotes the calcium-dependent PedE branch.
- PedR2-dependent transcriptional control inhibits Lanthanide-dependent PedH alcohol oxidation: PedR2 contributes to repression of the PedH branch without lanthanides.

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

# Commissioned Module/Pathway/Taxon Review: Pseudomonad Lanthanide-Switch PQQ Alcohol Oxidation in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Seeding pathway bucket:** KEGG `ppu00625` — "Chloroalkane and chloroalkene degradation"
**Module area:** other_kegg_pathway
**Candidate genes seeded from local metadata:** fdhA (PP_0328), frmA (PP_1616), pedE (PP_2674), pedH (PP_2679), adhP (PP_3839)

---

## 1. Executive Summary

The lanthanide-switch PQQ (pyrroloquinoline-quinone) alcohol-oxidation module is a **real and directly experimentally validated system in *P. putida* KT2440**, and it is one of the best-characterized rare-earth-element (REE) switches in any bacterium. Its **catalytic core is well covered by the candidate list**: `pedE` (PP_2674), the calcium-dependent PQQ alcohol dehydrogenase, and `pedH` (PP_2679), the lanthanide-dependent paralog, are both experimentally purified and biochemically characterized enzymes from this exact strain. These two enzymes define the periplasmic alcohol-oxidation step of the module.

However, the **regulatory core of the module — the PedS2/PedR2 two-component system (PP_2671/PP_2672) — is completely missing from the seeded candidate gene list.** This is a *metadata gap, not a biological gap*: the two-component system is experimentally proven in KT2440 to be the master switch that reciprocally controls `pedE` and `pedH` expression in response to nanomolar lanthanide concentrations. UniProt annotates PP_2672 under the gene name `exaE` ("Transcriptional activator protein ExaE"), which is the same protein as PedR2 — a naming synonymy that curators must reconcile. Both PP_2671 (PedS2 sensor histidine kinase) and PP_2672 (PedR2/ExaE response regulator) should be **added to the module and promoted to full gene review.**

Two further curation-critical conclusions emerge. First, the **KEGG seeding bucket `ppu00625` (chloroalkane/chloroalkene degradation) is a mismatch**: it is a generic, EC-number-based overview map into which PedE, PedH and formaldehyde dehydrogenase fall only because they share broad alcohol/aldehyde-dehydrogenase EC classes. There is no experimental evidence linking PedE/PedH to chloroalkane catabolism in this organism. Second, **three of the five candidate genes — fdhA (PP_0328), frmA (PP_1616), and adhP (PP_3839) — are out of module scope**; they represent downstream aldehyde/formaldehyde detoxification or cytoplasmic NAD-dependent alcohol metabolism, not the periplasmic PQQ oxidation core, and are likely over-propagated into the bucket by shared EC numbers. A nearby second two-component system (AgmR, PP_2665) is the principal paralog-ambiguity hazard for the regulatory step and must be distinguished from PedR2/ExaE.

---

## 2. Target-Organism Pathway Definition

### What this module *is*

The module is a **reusable pseudomonad regulatory-catalytic unit** coupling metal-sensing two-component signaling to metal-conditioned periplasmic alcohol oxidation. In *P. putida* KT2440 it comprises three functional steps:

1. **Lanthanide-responsive sensor signaling** — the sensor histidine kinase PedS2 (PP_2671) modulates its autophosphorylation/phosphotransfer activity according to lanthanide availability.
2. **Transcriptional switch output** — the LuxR/GerE-type response regulator PedR2 (PP_2672, = ExaE) receives the phosphoryl signal and reciprocally controls the two dehydrogenase genes.
3. **Metal-conditioned periplasmic PQQ alcohol oxidation** — two redundant periplasmic PQQ-dependent alcohol dehydrogenases, the Ca²⁺-dependent PedE (PP_2674) and the Ln³⁺-dependent PedH (PP_2679), oxidize diverse alcohols and aldehydes and pass electrons to cytochrome c.

The physiological logic is a mutually exclusive enzyme switch: in the **absence of usable lanthanides**, phospho-PedR2 activates `pedE` and represses `pedH`; when **lanthanides are available** (down to 1–10 nM La³⁺), PedS2 kinase activity falls, phospho-PedR2 drops, `pedE` expression decreases, and `pedH` is de-repressed and (via an additional, still-unidentified regulatory input) activated.

### Neighboring pathways to keep separate

- **PQQ biosynthesis** (e.g., pqqD2, PP_2681) — supplies the PQQ cofactor but is a distinct adjacent system.
- **Lanthanide uptake / handling** — the transport and storage machinery for REEs is upstream and out of scope.
- **Downstream aldehyde metabolism** — periplasmic/cytoplasmic aldehyde dehydrogenases (e.g., aldB-II, PP_2680; fdhA, PP_0328) and formaldehyde detoxification (frmA, PP_1616) act *after* the alcohol-oxidation step and are outside the module.
- **Cytoplasmic NAD(H)-dependent alcohol metabolism** (adhP, PP_3839) — a mechanistically unrelated, non-PQQ, non-periplasmic activity.
- **KEGG overview maps** — `ppu00625` (chloroalkane/chloroalkene degradation) and `ppu00626` (related degradation buckets) are broad EC-based maps and should not be treated as this module.

### Alternate names / database definitions

- **PedR2 = ExaE** (UniProt gene name for PP_2672). The `exa` nomenclature derives from the *ethanol oxidation* (Exa) system of *Pseudomonas aeruginosa*; curators should treat `pedR2` and `exaE` as synonyms for PP_2672 in KT2440.
- **PedE** is also referenced as **QedH-I** and **PedH** as **QedH-II** in some UniProt/annotation contexts.
- EC assignments: PedE = **EC 1.1.2.8** (alcohol dehydrogenase, cytochrome c); PedH = **EC 1.1.2.-** (partial/incomplete EC, reflecting its lanthanide-dependent activity).

---

## 3. Expected Step Model

| # | Module step | Expected molecular player | KT2440 gene / locus | Status in candidate metadata |
|---|-------------|---------------------------|---------------------|------------------------------|
| 1 | Lanthanide-responsive sensor signaling | PedS2 phosphorelay sensor kinase | PedS2 / PP_2671 | **MISSING** (metadata gap) |
| 2 | Transcriptional switch output | PedR2/ExaE response regulator (LuxR/GerE-type) | PedR2 = ExaE / PP_2672 | **MISSING** (metadata gap) |
| 3a | Ca²⁺-dependent periplasmic PQQ alcohol oxidation | Ca²⁺-PQQ alcohol dehydrogenase | PedE / PP_2674 | **COVERED** |
| 3b | Ln³⁺-dependent periplasmic PQQ alcohol oxidation | Ln³⁺-PQQ alcohol dehydrogenase | PedH / PP_2679 | **COVERED** |

Steps 3a and 3b are **alternative versions by catalytic-metal availability** (a single "metered" alcohol-oxidation node with two mutually exclusive enzyme realizations), not two independent obligatory steps.

The three remaining seeded candidates map to *adjacent* steps that are explicitly outside the module scope:

| Seeded gene | Locus | Annotation | Where it actually belongs |
|-------------|-------|------------|---------------------------|
| fdhA | PP_0328 | Formaldehyde dehydrogenase (EC 1.2.1.46) | Downstream aldehyde metabolism |
| frmA | PP_1616 | S-(hydroxymethyl)glutathione / glutathione-dependent formaldehyde dehydrogenase, class-III ADH (EC 1.1.1.1 / 1.1.1.284) | Formaldehyde detoxification (ppu00626) |
| adhP | PP_3839 | Short-chain / NAD(H)-dependent cytoplasmic alcohol dehydrogenase (EC 1.1.1.- / 1.1.1.1) | Cytoplasmic alcohol metabolism (ppu00626) |

---

## 4. Candidate Genes and Evidence

### 4.1 pedE (PP_2674) — Ca²⁺-dependent PQQ alcohol dehydrogenase — **COVERED, high confidence**

PedE is a periplasmic, PQQ-dependent, calcium-dependent alcohol dehydrogenase (EC 1.1.2.8) that is directly, experimentally characterized in *P. putida* KT2440. Purified-enzyme biochemistry [PMID: 28655819](https://pubmed.ncbi.nlm.nih.gov/28655819/) shows PedE and its lanthanide-dependent counterpart PedH have similar broad substrate ranges spanning linear and aromatic primary and secondary alcohols as well as aldehydes. PedE is the enzyme favored in the absence of usable lanthanides. Evidence type: **direct, target-strain purified-enzyme and reporter-fusion data.** Curation caveat: the EC 1.1.2.8 and generic alcohol-dehydrogenase mappings are what pull PedE into unrelated KEGG overview maps such as `ppu00625`; the locus-tag-level identity to the lanthanide-switch module is unambiguous and should be preserved.

### 4.2 pedH (PP_2679) — Ln³⁺-dependent PQQ alcohol dehydrogenase — **COVERED, high confidence**

PedH (PP_2679) is the lanthanide-dependent paralog. The key experimental result is that PedH exhibits enzyme activity on a range of substrates similar to PedE — *including linear and aromatic primary and secondary alcohols, as well as aldehydes* — **but only in the presence of lanthanide ions** (La³⁺, Ce³⁺, Pr³⁺, Sm³⁺, Nd³⁺) [PMID: 28655819](https://pubmed.ncbi.nlm.nih.gov/28655819/). The regulatory network responds to lanthanide concentrations as low as 1–10 nM La³⁺, and the two enzymes are inversely regulated. The PQQ-oxidation system as a whole is crucial for efficient growth on volatile alcohols. Evidence type: **direct, target-strain.** Curation caveat: PedH carries an *incomplete* EC number (1.1.2.-), reflecting that its lanthanide-dependent catalysis was formalized more recently; broad GO/EC mappings should not be used to relocate it out of the module.

### 4.3 PedS2 (PP_2671) and PedR2/ExaE (PP_2672) — regulatory core — **MISSING from metadata, must be added, high confidence they belong**

The seeded candidate list (PP_0328, PP_1616, PP_2674, PP_2679, PP_3839) does **not** contain PP_2671 or PP_2672, yet these two genes constitute the entire signaling half of the module. In KT2440, adaptive-evolution experiments, site-specific mutations, reporter fusions, and complementation demonstrate that the **PedS2/PedR2 (PP_2671/PP_2672) two-component system drives the REE switch** [PMID: 30158283](https://pubmed.ncbi.nlm.nih.gov/30158283/). Mechanistically: in the absence of La³⁺, sensor histidine kinase PedS2 phosphorylates its cognate LuxR-type response regulator PedR2, which activates `pedE` transcription and represses `pedH`; La³⁺ lowers PedS2 kinase activity, reducing phospho-PedR2, decreasing `pedE`, and de-repressing `pedH`.

A crucial caveat for module-relationship curation is that PedR2 is **not the sole regulator of `pedH`**: the same study documents that transcriptional *activation* of `pedH` requires "a yet unknown regulatory module" [PMID: 30158283](https://pubmed.ncbi.nlm.nih.gov/30158283/). Thus PedR2's documented role is repression of `pedH` and activation of `pedE`; full positive control of `pedH` involves an additional, unidentified input.

UniProt annotates PP_2672 under the gene name **`exaE`** ("Transcriptional activator protein ExaE", a LuxR/GerE-type regulator). Curators must recognize `exaE` = `pedR2` = PP_2672 as one protein. This synonymy is the single most important reconciliation needed to make the module satisfiable in the target taxon.

### 4.4 fdhA (PP_0328), frmA (PP_1616), adhP (PP_3839) — **out of module scope, likely over-propagated**

- **fdhA (PP_0328)** — formaldehyde dehydrogenase (EC 1.2.1.46). Acts on aldehydes/formaldehyde and belongs to downstream aldehyde metabolism, explicitly outside the periplasmic-alcohol-oxidation module scope.
- **frmA (PP_1616)** — glutathione-dependent S-(hydroxymethyl)glutathione / formaldehyde dehydrogenase, class-III ADH (EC 1.1.1.284 / 1.1.1.1); its primary bucket is `ppu00626`. It is a formaldehyde-detoxification enzyme, not a periplasmic PQQ enzyme.
- **adhP (PP_3839)** — short-chain / NAD(H)-dependent cytoplasmic alcohol dehydrogenase (EC 1.1.1.1); primary bucket `ppu00626`. It is neither a PQQ enzyme nor periplasmic.

None of these three is among the two PQQ-ADHs (PedE/PedH) that define the module, and the target-strain literature attributes periplasmic VOC (volatile-organic-compound) oxidation exclusively to PedE and PedH [PMID: 28655819](https://pubmed.ncbi.nlm.nih.gov/28655819/), [PMID: 30158283](https://pubmed.ncbi.nlm.nih.gov/30158283/). They enter the bucket through shared, broad alcohol/aldehyde-dehydrogenase EC classes — a textbook signature of annotation over-propagation.

### 4.5 Locus architecture confirms the cluster (UniProt, proteome UP000000556)

Inspection of the PP_2662–PP_2683 region in UniProt (organism 160488) confirms a coherent gene cluster and identifies the electron-acceptor and cofactor neighbors that flank the catalytic core:

| Locus | UniProt gene / annotation | Module relevance |
|-------|---------------------------|------------------|
| PP_2671 | histidine kinase (EC 2.7.13.3) | **PedS2 — sensor kinase (step 1)** |
| PP_2672 | `exaE`, Transcriptional activator ExaE | **PedR2 — response regulator (step 2)** |
| PP_2674 | `pedE` (qedH-I, EC 1.1.2.8) | **Ca²⁺-PQQ-ADH (step 3a)** |
| PP_2675 | Cytochrome c-type protein | Candidate electron acceptor (adjacent) |
| PP_2679 | `pedH` (qedH-II, EC 1.1.2.-) | **Ln³⁺-PQQ-ADH (step 3b)** |
| PP_2680 | `aldB-II`, aldehyde dehydrogenase (EC 1.2.1.3) | Downstream aldehyde step (adjacent) |
| PP_2681 | `pqqD2` | PQQ biosynthesis (adjacent) |
| PP_2664 / PP_2665 | sensor histidine kinase / `agmR`, DNA-binding response regulator | **Second TCS — paralog-ambiguity hazard** |
| PP_2682 / PP_2683 | `yiaY` iron-ADH / `yiaZ` (third TCS) | Adjacent, out of scope |

This architecture is decisive: the sensor/regulator pair (PP_2671/PP_2672) sits immediately adjacent to the catalytic pair (PP_2674/PP_2679), with cytochrome c (PP_2675), PQQ biosynthesis (PP_2681), and downstream aldehyde-DH (PP_2680) genes co-localized — exactly what is expected for a physically clustered lanthanide-switch operon.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 Metadata gap (regulatory core absent)

The most consequential problem is that **steps 1 and 2 of the module have no representative in the candidate list**. PedS2 (PP_2671) and PedR2/ExaE (PP_2672) are experimentally validated in KT2440 but were not seeded. Without them the module appears "half-satisfiable" purely as an artifact of metadata seeding.

### 5.2 Naming synonymy (PedR2 = ExaE)

PP_2672 is annotated as `exaE` in UniProt but referred to as `pedR2` in the mechanistic literature. Curation systems keyed on gene symbol will miss the match unless the synonym is recorded.

### 5.3 Paralog-ambiguity hazard (AgmR, second TCS)

A **second two-component system (sensor kinase PP_2664 / response regulator AgmR, PP_2665)** lies within the same locus. AgmR is a DNA-binding response regulator that can be confused with PedR2/ExaE during automated annotation transfer. There is also a third TCS (`yiaZ`, PP_2683). Any homology-based assignment of "the response regulator of the ped cluster" must specifically resolve to PP_2672, not PP_2665 or PP_2683. This is the principal mis-assignment risk in the module.

### 5.4 Incomplete `pedH` positive regulation

PedR2 accounts for `pedE` activation and `pedH` repression, but full `pedH` *activation* requires an additional, unidentified regulatory module [PMID: 30158283](https://pubmed.ncbi.nlm.nih.gov/30158283/). The "PedR2 inhibits PedH branch" relationship in the generic module is correct, but the generic module's implicit assumption that PedR2 is the complete regulator of the switch is an oversimplification.

### 5.5 Over-propagated / out-of-scope candidates

fdhA (PP_0328), frmA (PP_1616), and adhP (PP_3839) are pulled into the bucket by broad EC classes and should be flagged as adjacent, not covered.

### 5.6 Wrong seeding bucket

KEGG `ppu00625` ("Chloroalkane and chloroalkene degradation") is a generic overview map. PedE, PedH, and fdhA appear there only via shared EC numbers (1.1.2.x alcohol dehydrogenase; 1.2.1.46 formaldehyde/aldehyde dehydrogenase). No experimental evidence links PedE/PedH to chloroalkane/chloroalkene catabolism in KT2440. The bucket should not be treated as equivalent to this module.

---

## 6. Module and GO-Curation Recommendations

### Per-step status recommendations

| Module step | KT2440 gene(s) | Recommended status | Rationale |
|-------------|----------------|--------------------|-----------|
| 1. PedS2 sensor signaling | PP_2671 | **covered → but ADD to module** | Validated in KT2440; missing from seed. |
| 2. PedR2 transcriptional output | PP_2672 (=ExaE) | **covered → but ADD to module** | Validated in KT2440; missing from seed; record `exaE` synonym. |
| 3a. Ca²⁺-PedE oxidation | PP_2674 | **covered** | Direct purified-enzyme evidence. |
| 3b. Ln³⁺-PedH oxidation | PP_2679 | **covered** | Direct purified-enzyme evidence. |
| (adjacent) downstream aldehyde/formaldehyde | PP_0328, PP_1616 | **not_expected_in_target_taxon (out of module scope)** | Downstream, EC-driven over-propagation. |
| (adjacent) cytoplasmic NAD-ADH | PP_3839 | **not_expected_in_target_taxon (out of module scope)** | Non-PQQ, non-periplasmic. |

### Module-boundary and revision recommendations

1. **module_needs_revision (metadata):** Add PP_2671 (PedS2) and PP_2672 (PedR2/ExaE) as the step-1 and step-2 players. The current seed omits the entire regulatory half.
2. **Fix the bucket mapping:** Detach the module from KEGG `ppu00625`. The lanthanide-switch module is a distinct regulatory/physiological system, not a chloroalkane-degradation submap.
3. **Record synonymy:** Add `exaE` (UniProt) ↔ `pedR2` (literature) ↔ PP_2672 as an explicit alias so symbol-keyed curation resolves correctly.
4. **Flag paralog hazard:** Annotate that PP_2665 (AgmR) and PP_2683 (yiaZ) are *distinct* response regulators in the same locus and must not be confused with PedR2/ExaE.
5. **Relationship refinement:** Keep "PedR2 activates PedE / represses PedH," but annotate that full `pedH` positive activation requires an additional, still-unknown regulatory input (do not model PedR2 as the sole `pedH` controller).

### GO-curation considerations

- PedE/PedH: **alcohol dehydrogenase (cytochrome c) activity** (EC 1.1.2.8-type), plus periplasmic localization. PedH additionally warrants a lanthanide/metal-ion-dependency qualifier.
- PedS2: **phosphorelay sensor kinase activity** (GO:0000155).
- PedR2/ExaE: **phosphorelay response regulator activity** (GO:0000156) and **DNA-binding transcription factor activity** (LuxR/GerE-type).
- No new GO *term* requests appear strictly necessary, but a lanthanide-dependency evidence qualifier for PedH would improve fidelity. A dedicated **module document** for "pseudomonad lanthanide-switch PQQ alcohol oxidation" (distinct from KEGG overview maps) is warranted.

---

## 7. Genes to Promote to Full Review (`fetch-gene`)

| Priority | Gene | Locus | Reason to promote |
|----------|------|-------|-------------------|
| 1 | **pedS2** | PP_2671 | Step-1 regulatory core; missing from seed; validated in KT2440. |
| 2 | **pedR2 / exaE** | PP_2672 | Step-2 regulatory core; missing from seed; naming synonymy must be resolved. |
| 3 | **pedE** | PP_2674 | Catalytic core; confirm EC 1.1.2.8 and Ca²⁺-dependence annotations. |
| 4 | **pedH** | PP_2679 | Catalytic core; resolve incomplete EC 1.1.2.- and add lanthanide-dependency qualifier. |
| (secondary) | agmR | PP_2665 | Not part of module, but should be reviewed to disambiguate from PedR2. |

fdhA (PP_0328), frmA (PP_1616), and adhP (PP_3839) do **not** need promotion for this module; they should simply be marked out of scope.

---

## 8. Evidence Base

| PMID | Title (abbrev.) | Role in this review | Evidence strength for KT2440 |
|------|-----------------|---------------------|------------------------------|
| [30158283](https://pubmed.ncbi.nlm.nih.gov/30158283/) | *The PedS2/PedR2 Two-Component System Is Crucial for the Rare Earth Element Switch in P. putida KT2440* | Establishes the regulatory core (PP_2671/PP_2672), reciprocal control of pedE/pedH, and the "yet unknown" additional pedH activator | **Direct, target-strain** (adaptive evolution, site mutations, reporter fusions, complementation) |
| [28655819](https://pubmed.ncbi.nlm.nih.gov/28655819/) | *Functional Role of Lanthanides in Enzymatic Activity and Transcriptional Regulation of PQQ-Dependent Alcohol Dehydrogenases* | Establishes PedE (PP_2674) and PedH (PP_2679) identities, metal dependence, and shared broad substrate range | **Direct, target-strain** (purified-enzyme biochemistry, reporter assays) |
| [32345644](https://pubmed.ncbi.nlm.nih.gov/32345644/) | *The Cellular Response to Lanthanum Is Substrate Specific and Reveals a Novel Route for Glycerol Metabolism in P. putida KT2440* | Context for lanthanum physiology and substrate-specific responses in the target strain | **Direct, target-strain** (physiology) |

Key verbatim support:

- PedE/PedH identities and metal dependence: *"PedH (PP_2679) exhibits enzyme activity on a range of substrates similar to that of its Ca²⁺-dependent counterpart PedE (PP_2674), including linear and aromatic primary and secondary alcohols, as well as aldehydes, but only in the presence of lanthanide ions, including La³⁺, Ce³⁺, Pr³⁺, Sm³⁺, or Nd³⁺"* — [PMID: 28655819](https://pubmed.ncbi.nlm.nih.gov/28655819/).
- Regulatory core loci: *"the PedS2/PedR2 (PP_2671/PP_2672) two-component system (TCS)"* — [PMID: 30158283](https://pubmed.ncbi.nlm.nih.gov/30158283/).
- Incomplete regulation of pedH: *"the transcriptional activation of the pedH gene by a yet unknown regulatory module"* — [PMID: 30158283](https://pubmed.ncbi.nlm.nih.gov/30158283/).

Locus architecture (PedR2 = ExaE = PP_2672; second TCS AgmR = PP_2665; cytochrome c PP_2675; pqqD2 PP_2681; aldB-II PP_2680) is drawn from UniProt proteome UP000000556 (organism 160488).

---

## 9. Mechanistic Model / Interpretation

```
 Lanthanide status                Signaling core                 Catalytic output
 -----------------                --------------                 ----------------

 No usable La3+ ──▶ PedS2 (PP_2671) ──phosphorylates──▶ PedR2 (PP_2672 = ExaE)
                    sensor kinase                       response regulator
                                                              │
                                        ┌─────────────────────┴─────────────────────┐
                                        │ activates                     represses    │
                                        ▼                                            ▼
                              pedE (PP_2674)                              pedH (PP_2679)
                              Ca2+-PQQ-ADH  ──▶ oxidizes alcohols ──▶ cyt c (PP_2675)
                              [ACTIVE branch]                          [OFF]

 La3+ available (>=1-10 nM) ──▶ PedS2 kinase activity DROPS ──▶ phospho-PedR2 DROPS
                                        │
                                        ▼
                     pedE DOWN, pedH DE-REPRESSED (+ unknown activator) ──▶
                              pedH (PP_2679) Ln3+-PQQ-ADH ──▶ oxidizes alcohols ──▶ cyt c
                              [ACTIVE branch]

 Adjacent / OUT OF MODULE SCOPE:
   PQQ biosynthesis (pqqD2, PP_2681) ─ cofactor supply
   Downstream aldehyde DH (aldB-II PP_2680; fdhA PP_0328; frmA PP_1616)
   Cytoplasmic NAD-ADH (adhP PP_3839)
   Second/third TCS (agmR PP_2665; yiaZ PP_2683)  ◀ paralog-ambiguity hazard
```

The model is a bistable, metal-metered enzyme switch. The candidate list captures only the two catalytic endpoints; the sensor/regulator that *is* the switch must be added for the module to be biologically satisfiable. The redundancy of PedE and PedH — same broad substrate spectrum, different catalytic metal — is the defining feature that makes this a "switch" rather than two independent pathways: the cell chooses which enzyme to express based on lanthanide availability, but the periplasmic alcohol-oxidation output to cytochrome c is functionally equivalent either way.

---

## 10. Limitations and Knowledge Gaps

1. **Additional pedH activator unidentified.** Full positive control of `pedH` requires a regulatory input beyond PedR2 that has not been molecularly identified [PMID: 30158283](https://pubmed.ncbi.nlm.nih.gov/30158283/). The module cannot yet fully enumerate step-2 players.
2. **Electron-acceptor assignment is inferential.** PP_2675 (cytochrome c-type) is a strong candidate periplasmic electron acceptor by co-localization and annotation, but its direct coupling to PedE/PedH in KT2440 is inferred, not experimentally pinned in the reviewed literature.
3. **This review relied on UniProt/KEGG annotations plus three primary papers.** A broader literature sweep (e.g., structural studies of PedH lanthanide coordination, cross-strain PedS2/PedR2 comparisons) was not exhaustively performed.
4. **AgmR's role vs. PedR2** was not experimentally dissected here; the disambiguation recommendation is based on locus architecture and annotation, not functional data in KT2440.
5. **No experimental link tested** between PedE/PedH and the seeded KEGG chloroalkane bucket; the mismatch conclusion is an absence-of-evidence argument grounded in the mechanistic literature.

---

## 11. Proposed Follow-up Experiments / Curation Actions

1. **Add PP_2671 (PedS2) and PP_2672 (PedR2/ExaE) to the module** and promote both to full `fetch-gene` review (highest priority curation action).
2. **Record the `exaE` ↔ `pedR2` ↔ PP_2672 synonymy** in the module/gene metadata.
3. **Detach the module from KEGG `ppu00625`;** create or link a dedicated "lanthanide-switch PQQ alcohol oxidation" module document.
4. **Mark fdhA (PP_0328), frmA (PP_1616), adhP (PP_3839) as out-of-scope/adjacent**, with a note that they were over-propagated via broad EC classes.
5. **Flag AgmR (PP_2665) and yiaZ (PP_2683)** as distinct response regulators to prevent mis-assignment to step 2.
6. **Add a lanthanide-dependency qualifier to PedH (PP_2679)** and resolve its incomplete EC (1.1.2.-).
7. **Expert/experimental question:** identify the additional `pedH` activator and confirm PP_2675 cytochrome c as the physiological electron acceptor — both would close the remaining mechanistic gaps in the module.

---

*Prepared for manual module satisfiability and gene-annotation curation. Evidence is direct for* P. putida *KT2440 unless otherwise noted; locus architecture is from UniProt proteome UP000000556.*


## Artifacts

- [OpenScientist final report](PSEPK__pseudomonad_lanthanide_switch_pqq_alcohol_oxidation__ppu00625-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__pseudomonad_lanthanide_switch_pqq_alcohol_oxidation__ppu00625-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:28655819
2. PMID:30158283