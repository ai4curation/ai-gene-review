---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T15:21:31.878228'
end_time: '2026-07-11T15:30:40.685406'
duration_seconds: 548.81
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Osmoregulated periplasmic glucan biosynthesis
  module_summary: A Pseudomonas putida KT2440 UniPathway UPA00637 module for biosynthesis
    of osmoregulated periplasmic glucans by the OpgH inner-membrane glucosyltransferase
    and the OpgG periplasmic glucan biosynthesis protein.
  module_outline: "- Osmoregulated periplasmic glucan biosynthesis\n  - 1. Inner-membrane\
    \ OPG glucosyltransferase\n  - OpgH glucosyltransferase step\n    - opgH: OPG\
    \ glucosyltransferase (molecular player: PSEPK opgH; activity or role: glucosyltransferase\
    \ activity)\n  - 2. Periplasmic OPG biosynthesis protein\n  - OpgG periplasmic\
    \ glucan biosynthesis step\n    - opgG: periplasmic OPG biosynthesis factor (molecular\
    \ player: PSEPK opgG; activity or role: carbohydrate binding)"
  module_connections: No explicit connections.
  pathway_query: UPA00637
  pathway_id: UPA00637
  pathway_name: UniPathway UPA00637
  pathway_source: UniPathway
  pathway_context: 'Resolved local bucket unipathway:UPA00637 with 2 primary genes;
    module area: unipathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '2'
  candidate_genes: '- opgH: PP_5025 | Q88D04 | Glucans biosynthesis glucosyltransferase
    H (EC 2.4.1.-) (EC 2.4.1.-; primary bucket unipathway:UPA00637)

    - opgG: PP_5026 | Q88D03 | Glucans biosynthesis protein G (primary bucket unipathway:UPA00637)'
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
  path: PSEPK__osmoregulated_periplasmic_glucan_biosynthesis__upa00637-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__osmoregulated_periplasmic_glucan_biosynthesis__upa00637-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Osmoregulated periplasmic glucan biosynthesis in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: UPA00637
- Resolved ID: UPA00637
- Resolved name: UniPathway UPA00637
- Source: UniPathway

Resolved local bucket unipathway:UPA00637 with 2 primary genes; module area: unipathway.

## Candidate Genes From Local Metadata

Candidate gene count: 2

- opgH: PP_5025 | Q88D04 | Glucans biosynthesis glucosyltransferase H (EC 2.4.1.-) (EC 2.4.1.-; primary bucket unipathway:UPA00637)
- opgG: PP_5026 | Q88D03 | Glucans biosynthesis protein G (primary bucket unipathway:UPA00637)

## Generic Module Context

### Working Scope

A Pseudomonas putida KT2440 UniPathway UPA00637 module for biosynthesis of osmoregulated periplasmic glucans by the OpgH inner-membrane glucosyltransferase and the OpgG periplasmic glucan biosynthesis protein.

### Provisional Biological Outline

- Osmoregulated periplasmic glucan biosynthesis
  - 1. Inner-membrane OPG glucosyltransferase
  - OpgH glucosyltransferase step
    - opgH: OPG glucosyltransferase (molecular player: PSEPK opgH; activity or role: glucosyltransferase activity)
  - 2. Periplasmic OPG biosynthesis protein
  - OpgG periplasmic glucan biosynthesis step
    - opgG: periplasmic OPG biosynthesis factor (molecular player: PSEPK opgG; activity or role: carbohydrate binding)

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

# Module Review: Osmoregulated Periplasmic Glucan Biosynthesis (UniPathway UPA00637) in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Module/bucket:** unipathway:UPA00637 — "Glycan metabolism; osmoregulated periplasmic glucan (OPG) biosynthesis"
**Candidate genes:** opgH (PP_5025 / Q88D04), opgG (PP_5026 / Q88D03)

---

## 1. Executive summary

- The core **OPG backbone-synthesis module (UPA00637) is satisfiable and should be marked COVERED** in KT2440. Both defining genes are present, adjacent, and correctly annotated: **opgH (PP_5025, inner-membrane GT2 glucosyltransferase)** and **opgG (PP_5026, periplasmic OpgG/MdoG-family maturation protein)**.
- Evidence for KT2440 itself is **homology-based (UniProt protein existence level 3, "inferred from homology")**, but transfer is **strong** because the direct orthologs in the close congener *P. aeruginosa* (opgGH, PA5077/PA5078) are experimentally shown to make linear β-1,2 glucan (Lequette et al. 2007, PMID 17906125), and opgG/opgH are the most conserved, functionally validated OPG genes across proteobacteria.
- **No accessory OPG genes** (opgB/mdoB phosphoglycerophosphotransferase, opgC/mdoC succinyltransferase, opgD glucan hydrolase, or the non-homologous ndvB) are annotated in the KT2440 proteome. These are **decoration/tailoring steps outside the UPA00637 backbone bucket** and should be treated as `not_expected_in_target_taxon` **for this module** (their true presence is a separate question — see §5).
- Curation risks are limited to **broad EC/GO breadth on OpgH** (bare `EC 2.4.1.-`, generic GT2 Pfam) and an **unannotated moonlighting FtsZ/cell-size role** documented for *E. coli* OpgH.

---

## 2. Target-organism pathway definition

**Process included (UPA00637):** Synthesis of the **glucose backbone of osmoregulated periplasmic glucans (OPGs)** — cytoplasmic-facing polymerization of UDP-glucose-derived glucosyl units by the inner-membrane glucosyltransferase **OpgH**, coupled to **OpgG**-dependent periplasmic maturation/assembly of the β-1,2-linked (with β-1,6 branch) glucan. OPGs accumulate in the periplasm in response to **low medium osmolarity** and are envelope homeostasis molecules.

**Alternate names / database definitions (keep consistent):**
- OPGs = historically **"membrane-derived oligosaccharides (MDOs)"**; *E. coli* genes **mdoG/mdoH = opgG/opgH**.
- UniPathway UPA00637 ≡ backbone synthesis only.

**Neighboring pathways/maps to keep SEPARATE:**
- **OPG substitution/decoration** (glycerophosphotransferase OpgB, succinyltransferase OpgC) — modifies but does not build the backbone.
- **Periplasmic glucan tailoring/hydrolysis** (OpgD) — controls chain length.
- **Cyclic β-1,2 glucan synthesis via NdvB/ChvB** (Rhizobiales/*Agrobacterium*) — a **non-homologous, alternative OPG route**; not the opgGH route.
- **Glycogen / α-1,4-glucan metabolism** (KT2440 glgB/PP_4058, glgE/PP_4060, glgP/PP_5041, glgA/glgC) — cytoplasmic storage glucan, unrelated to periplasmic OPGs. Do **not** merge these into UPA00637 despite the shared "glucan" keyword.
- Broad "starch and sucrose metabolism" / KEGG overview maps — keep out of the module.

---

## 3. Expected step model

| Step | Enzyme/player | Role | Expected in KT2440? |
|------|---------------|------|---------------------|
| 1. Backbone polymerization | **OpgH** (inner-membrane GT2) | Glucosyltransferase; polymerizes β-1,2 glucan backbone from UDP-glucose | **Yes — covered** (PP_5025) |
| 2. Periplasmic maturation/assembly | **OpgG** (periplasmic) | Backbone maturation / branching-associated periplasmic factor; carbohydrate binding | **Yes — covered** (PP_5026) |
| (accessory) Glycerophosphotransferase | OpgB/MdoB | sn-1-P-glycerol substitution | Not in module scope; not annotated |
| (accessory) Succinyltransferase | OpgC/MdoC | Succinyl substitution (seen in *P. aeruginosa* OPGs) | Not in module scope; not annotated (open question) |
| (accessory) Glucan hydrolase | OpgD | Chain-length control | Not in module scope; not annotated |

Both required backbone steps are encoded. Accessory steps are **not part of UPA00637** and their absence does not reduce module satisfiability.

---

## 4. Candidate genes and evidence

### opgH — PP_5025 / Q88D04 (high confidence; COVERS step 1)
- **Annotation:** Glucans biosynthesis glucosyltransferase H; 857 aa; **Cell inner membrane** (multi-TM); UniPathway UPA00637.
- **Family evidence:** InterPro **IPR023725 (Glucans_biosynth_gluTrFase_H, OpgH-specific)**, IPR050321 (Glycosyltr_2/OpgH_subfam), generic GT2 IPR001173/Pfam PF00535; **COG2943**. The OpgH-specific InterPro + COG + pathway context make the subfamily call reliable despite the generic GT2 core.
- **Function transfer:** Strong. Orthologous *P. aeruginosa* opgH (PA5077) participates in experimentally verified linear β-1,2 glucan synthesis (PMID 17906125); mdoH/opgH mutants abolish OPGs in *E. coli*, Erwinia, Salmonella, Shigella, Rhodobacter (PMIDs 11325942, 19118363, 20062978, 12027885).
- **Curation caveats:** (i) EC is only `2.4.1.-` (no leaf EC) and the generic GT2 Pfam/GO are **over-propagation-prone** — rely on the OpgH-subfamily anchor. (ii) *E. coli* OpgH **moonlights** as a UDP-glucose-dependent, nutrient-sensing FtsZ antagonist controlling cell size (Hill et al. 2013, PMID 23935518); this second function is **not annotated** in KT2440.

### opgG — PP_5026 / Q88D03 (high confidence; COVERS step 2)
- **Annotation:** Glucans biosynthesis protein G; 559 aa; **Periplasm** with cleaved signal peptide; UniPathway UPA00637.
- **Family evidence:** **OpgD/OpgG family**; Pfam **PF04349 (MdoG)**, InterPro IPR023704 (MdoG_OpgG), IPR007444 (MdoG_C), galactose-mutarotase-like + Ig/E-set folds; **COG3131**.
- **Function transfer:** Strong (same experimental basis as opgH; opgG mutants abolish OPGs).
- **Curation caveats:** OpgG and OpgD are **paralogs of the same family** (PF04349); automated pipelines can mis-split OpgG vs OpgD. **Verified: KT2440 has exactly one PF04349 member (PP_5026), i.e. no separate OpgD**, so the periplasmic role is assigned to **OpgG with no paralog ambiguity** in this genome. GO carbohydrate-binding term is appropriate; avoid asserting a specific hydrolase activity absent OpgD-type evidence.

**GT2-breadth check:** OpgH (PP_5025) is **1 of 7 GT2/PF00535 proteins** in KT2440 (others: PP_3256, PP_1792, PP_1793, PP_3137, PP_3135, PP_0034), but **only PP_5025 carries the OpgH-specific InterPro IPR023725** — concretely confirming that the shared GT2 Pfam/GO is over-propagation-prone and that the specific OpgH call depends on the subfamily/UniPathway anchor.

**Operon context (verified):** PP_5025/PP_5026 are consecutive, matching the conserved **opgHG (opgGH) operon** organization (as in *P. aeruginosa* PA5077/PA5078). The locus is a **standalone two-gene unit**: upstream neighbors are an amino-acid ABC-transport cluster (PP_5023 GlnP permease, PP_5024 solute-binding protein 3 family), downstream are unrelated genes (PP_5027 D-aminoacyl-tRNA deacylase, PP_5028 proline iminopeptidase). **No adjacent opgB/opgC/opgD** acyl-/glycerophosphotransferase — no genomic evidence for a co-localized OPG-decoration sub-module.

---

## 5. Gaps, ambiguities, and likely over-annotations

- **Backbone module: no gaps.** Both required steps covered by high-confidence genes.
- **Accessory tailoring genes absent from annotation:** No opgB, opgC, opgD, or ndvB found in a proteome-wide search of taxon 160488. *P. aeruginosa* OPGs carry succinyl substituents, so an **opgC-like succinyltransferase could plausibly exist** but be unannotated/divergent — a genuine open question, though **outside UPA00637**. Mark accessory steps `not_expected_in_target_taxon` for this module while noting the opgC uncertainty for a possible substitution sub-module.
- **Over-annotation risk on OpgH:** bare `EC 2.4.1.-` and generic GT2 GO terms; keep the specific OpgH-subfamily/UniPathway anchoring.
- **Do not conflate glycogen genes** (glgB/E/P/A/C) with OPG biosynthesis; shared "glucan" wording is the main false-merge risk.
- **Evidence class:** All KT2440 assignments are homology-inferred (PE3); there is **no direct KT2440 experimental OPG characterization** in the retrieved literature.

---

## 6. Module and GO-curation recommendations

| Module step | Recommendation |
|-------------|----------------|
| OpgH glucosyltransferase step | **covered** (PP_5025) |
| OpgG periplasmic maturation step | **covered** (PP_5026) |
| Overall UPA00637 backbone module | **SATISFIED / covered** in KT2440 |
| OPG succinylation (opgC) | `not_expected_in_target_taxon` for UPA00637; flag as `candidate_uncertain` if a substitution sub-module is defined |
| OPG glycerophosphate (opgB), chain-length (opgD) | `not_expected_in_target_taxon` for this backbone module |

- **Module boundaries are appropriate** for KT2440 as a backbone-only (OpgH + OpgG) module; no revision needed. Keep decoration/hydrolysis and cyclic-glucan (ndvB) routes as separate modules.
- **GO:** OpgH — retain glucosyltransferase activity + OPG biosynthetic process + inner membrane; consider (only if experimentally supported in Pseudomonas) an added division/FtsZ-regulation term. OpgG — carbohydrate binding + OPG biosynthetic process + periplasm; avoid a specific hydrolase term. No new GO term requests appear necessary for the core module.

---

## 7. Genes to promote to full `fetch-gene` review

1. **opgH / PP_5025 (Q88D04)** — promote. Reasons: broad `EC 2.4.1.-`, generic GT2 GO breadth, and a documented moonlighting FtsZ/cell-size function worth curating or explicitly excluding for KT2440.
2. **opgG / PP_5026 (Q88D03)** — promote (lower priority). Confirm OpgG-vs-OpgD family assignment is unambiguous (single PF04349 member) and that carbohydrate-binding/periplasmic annotation is correctly scoped.

---

## 8. Key references

- Bohin JP. 2000. Osmoregulated periplasmic glucans in Proteobacteria. **PMID 10779706** (review; OPG families, osmoregulation, pleiotropic mutant phenotypes).
- Lequette Y, Rollet E, Delangle A, Greenberg EP, Bohin JP. 2007. Linear osmoregulated periplasmic glucans are encoded by the opgGH locus of *Pseudomonas aeruginosa*. **PMID 17906125** (direct Pseudomonas evidence: β-1,2 backbone, β-1,6 branches, succinyl substitution, osmotic repression, biofilm role).
- Hill NS, Buske PJ, Shi Y, Levin PA. 2013. A moonlighting enzyme links *E. coli* cell size with central metabolism. **PMID 23935518** (OpgH as UDP-glucose-dependent FtsZ antagonist / cell-size regulator).
- Page F et al. 2001. OPG synthesis required for *Erwinia chrysanthemi* pathogenicity. **PMID 11325942** (opgGH ≡ mdoGH; mutants abolish OPGs).
- Bhagwat AA et al. 2009. OPGs of *Salmonella* Typhimurium required for virulence. **PMID 19118363** (bicistronic opgGH operon).
- Liu D et al. 2010. OPG gene family of *Shigella flexneri*. **PMID 20062978** (opgGH + accessory opgB/C/D operon structure).
- Cogez V et al. 2002. opgGIH/opgC operon in *Rhodobacter sphaeroides*. **PMID 12027885** (backbone vs succinylation genetics).
- UniProt Q88D04 (opgH/PP_5025) and Q88D03 (opgG/PP_5026); UniPathway UPA00637; InterPro IPR023725, IPR023704, Pfam PF00535/PF04349.


## Artifacts

- [OpenScientist final report](PSEPK__osmoregulated_periplasmic_glucan_biosynthesis__upa00637-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__osmoregulated_periplasmic_glucan_biosynthesis__upa00637-deep-research-openscientist_artifacts/final_report.pdf)