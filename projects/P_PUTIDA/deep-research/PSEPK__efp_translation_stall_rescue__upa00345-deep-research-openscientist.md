---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T12:30:26.323661'
end_time: '2026-07-11T12:59:56.047015'
duration_seconds: 1769.72
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: EF-P translation stall rescue
  module_summary: A Pseudomonas putida KT2440 UniPathway UPA00345 module for elongation
    factor P-dependent stimulation of peptide-bond formation and rescue of stalled
    cytosolic ribosomes. The module is centered on efp (PP_1858, UniProtKB:Q88LS0).
    EarP-dependent Arg32 rhamnosylation and dTDP-L-rhamnose supply are activation
    context for pseudomonad EF-P, but they are not members of the single-gene UPA00345
    pathway bucket.
  module_outline: "- EF-P translation stall rescue\n  - 1. EF-P-dependent rescue of\
    \ stalled translation elongation\n  - EF-P stalled-ribosome rescue\n    - efp:\
    \ elongation factor P (molecular player: PSEPK efp; activity or role: translation\
    \ elongation factor activity)"
  module_connections: No explicit connections.
  pathway_query: UPA00345
  pathway_id: UPA00345
  pathway_name: UniPathway UPA00345
  pathway_source: UniPathway
  pathway_context: 'Resolved local bucket unipathway:UPA00345 with 1 primary genes;
    module area: unipathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '1'
  candidate_genes: '- efp: PP_1858 | Q88LS0 | Elongation factor P (EF-P) (primary
    bucket unipathway:UPA00345)'
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
  path: PSEPK__efp_translation_stall_rescue__upa00345-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__efp_translation_stall_rescue__upa00345-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

EF-P translation stall rescue in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: UPA00345
- Resolved ID: UPA00345
- Resolved name: UniPathway UPA00345
- Source: UniPathway

Resolved local bucket unipathway:UPA00345 with 1 primary genes; module area: unipathway.

## Candidate Genes From Local Metadata

Candidate gene count: 1

- efp: PP_1858 | Q88LS0 | Elongation factor P (EF-P) (primary bucket unipathway:UPA00345)

## Generic Module Context

### Working Scope

A Pseudomonas putida KT2440 UniPathway UPA00345 module for elongation factor P-dependent stimulation of peptide-bond formation and rescue of stalled cytosolic ribosomes. The module is centered on efp (PP_1858, UniProtKB:Q88LS0). EarP-dependent Arg32 rhamnosylation and dTDP-L-rhamnose supply are activation context for pseudomonad EF-P, but they are not members of the single-gene UPA00345 pathway bucket.

### Provisional Biological Outline

- EF-P translation stall rescue
  - 1. EF-P-dependent rescue of stalled translation elongation
  - EF-P stalled-ribosome rescue
    - efp: elongation factor P (molecular player: PSEPK efp; activity or role: translation elongation factor activity)

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

# Species-Aware Module Review: EF-P Translation Stall Rescue in *Pseudomonas putida* KT2440 (UniPathway UPA00345)

**Target:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Bucket:** unipathway:UPA00345 — EF-P-dependent stimulation of peptide-bond formation / rescue of stalled cytosolic ribosomes
**Anchor gene:** efp = PP_1858 = UniProtKB **Q88LS0** (EFP_PSEPK)
**Review completed:** Iteration 3 of 3 (final)

---

## 1. Executive summary

The single-gene UPA00345 module for *P. putida* KT2440 is **SATISFIED and COVERED** by the sole candidate gene **efp (PP_1858, Q88LS0)**. This is a canonical, universally conserved translation elongation factor P that rescues ribosomes stalled at polyproline (and related) motifs by stabilizing P-site peptidyl-tRNA and promoting peptide-bond formation. Evidence is **direct for the target strain** at the sequence/annotation level (reviewed SwissProt entry, HAMAP MF_00141, Arg32 rhamnosylation feature) and mechanistically strong from genus-level and structural studies.

KT2440 EF-P uses the **pseudomonad activation strategy: Arg32 rhamnosylation by EarP** (PP_1857, immediately adjacent), using **dTDP-L-rhamnose** supplied by the complete *rml/rfb* nucleotide-sugar cluster (PP_1782–1785; RmlA–D). These activation genes are **real and present** but are correctly **outside the UPA00345 bucket**; they belong to separate glycosyltransferase / nucleotide-sugar modules. The *E. coli*-style EpmA/EpmB/EpmC β-lysylation route is **not expected** in this organism (EF-P carries Arg, not Lys, at position 32). KT2440 has **no EfpL/YeiP paralog**, so there is no paralog ambiguity and the single-gene module scope is correct.

---

## 2. Target-organism pathway definition

- **Process included:** EF-P-dependent stimulation of peptidyl transferase activity to rescue elongating 70S ribosomes stalled at consecutive prolines (PPP/PPG and related XPP/PPX motifs). EF-P binds between the P- and E-sites, contacts the CCA end of P-site tRNA, and enforces a nascent-chain geometry compatible with peptide-bond formation (PMID 29100052).
- **Keep separate (neighboring processes, NOT this bucket):**
  - **EarP-catalyzed EF-P Arg-rhamnosylation** (post-translational activation; a glycosyltransferase reaction) — separate module/GO.
  - **dTDP-L-rhamnose biosynthesis** (*rmlABCD* / *rfbABCD*; nucleotide-sugar metabolism, also feeds LPS O-antigen) — separate module.
  - **General polypeptide elongation** (UniProt PATHWAY "Protein biosynthesis; polypeptide chain elongation") — the broad overview map; UPA00345 is the specialized stall-rescue sub-process, not general elongation.
  - **Ribosome rescue by tmRNA/ArfA/ArfB** (rescue of *truncated-mRNA*-stalled ribosomes) — a mechanistically distinct rescue system; do not merge.
- **Alternate names / database definitions:** EF-P (efp); eukaryotic/archaeal functional analog eIF5A/aIF5A ("EF5"); UniProt keyword "Elongation factor"; HAMAP rule MF_00141; the modified-arginine subfamily is the "PGKGP/Arg32" type of EF-P.

---

## 3. Expected step model

UPA00345 is a **single-step** bucket in the metadata, and that matches the biology for KT2440:

| Step | Description | Expected gene | Status in KT2440 |
|------|-------------|---------------|------------------|
| S1 | EF-P-dependent rescue of polyproline-stalled ribosomes / stimulation of peptide-bond formation | efp | **Covered** (PP_1858 / Q88LS0) |

Activation context (adjacent modules, listed for curator awareness, **not** UPA00345 steps):

| Context step | Gene(s) in KT2440 | Note |
|--------------|-------------------|------|
| EF-P Arg32 rhamnosylation | earP / PP_1857 (Q88LS1) | Adjacent to efp; experimental EC 2.4.1.- rhamnosyltransferase |
| dTDP-L-rhamnose supply | Complete Rml cluster PP_1782–1785: rmlA/rfbA (PP_1783), rmlB/rffG (PP_1785), rmlC/rfbC (PP_1782), rmlD/rfbD (PP_1784) | Nucleotide-sugar / O-antigen module; supplies EarP substrate |

---

## 4. Candidate genes and evidence

### efp — PP_1858 — Q88LS0 (EFP_PSEPK) — **high confidence, COVERED**
- **Role:** Elongation factor P; rescues polyproline-stalled ribosomes and stimulates peptide-bond synthesis on 70S ribosomes (UniProt FUNCTION; HAMAP MF_00141).
- **Evidence type:** Direct SwissProt annotation for strain KT2440; 189 aa; "Belongs to the elongation factor P family." Sequence position 32 = **Arg**, carrying UniProt feature **"Glycosylation 32..32 N-alpha-linked (Rha) arginine"** and PTM note "arginine rhamnosylation is required for EF-P function and rescue of polyproline stalled ribosomes." Function is HAMAP-rule/homology inferred; the PTM/site is supported by genus-level experiments (PMID 25686373, 28951478).
- **Curation caveats:** None that undermine the assignment. It is the **only** EF-P-family protein in the KT2440 proteome (no over-propagation risk, no paralog to disambiguate). GO/pathway mappings are specific and appropriate.

### earP — PP_1857 — Q88LS1 (EARP_PSEPK) — activation context (out of bucket)
- **Role:** Protein-arginine rhamnosyltransferase; transfers rhamnose onto EF-P Arg32 (required for EF-P activity). Experimental support ECO:0000269 (PMID 28951478).
- **Curation caveat:** UniProt FUNCTION text says the target is **"'Lys-32'"** — this is a **residue mislabel**; the modified residue is **Arg32** (efp position 32 = R; feature = arginine glycosylation). Flag for UniProt correction. Do **not** place earP inside UPA00345.

---

## 5. Gaps, ambiguities, and likely over-annotations

- **No gap** in the UPA00345 core: the single expected step is present with a specific, reviewed gene.
- **Not expected in target taxon:** the *E. coli* EF-P β-lysylation activation genes **epmA (poxA/genX), epmB (yjeK), epmC**. A UniProt proteome search of taxon 160488 returned **zero** hits for any of these (genomic absence, not just inference). KT2440 EF-P has **Arg** (not Lys) at the modification site (loop G31-**R32**-N33) and uses the EarP route instead. Any epmA/B/C annotation transferred to KT2440 should be treated as **not_expected / mis-transfer**.
- **Activation substrate fully supplied:** the complete dTDP-L-rhamnose cluster **PP_1782–1785** (RmlA/RmlB/RmlC/RmlD) is present, so EarP's sugar-nucleotide donor is genomically guaranteed.
- **Paralog ambiguity:** none. Unlike *E. coli* (which has EfpL/YeiP, PMID 39622818), KT2440 encodes a single EF-P. No risk of splitting the assignment between paralogs.
- **Over-annotation to watch:** broad "translation elongation factor activity" / GO:0003746 could be applied loosely; for UPA00345 the specific, evidenced function (polyproline stall rescue) is what matters and is well supported here.
- **Boundary correctness:** the generic module boundary (single efp gene, with EarP/rhamnose flagged as activation context, not members) is **correct** for this organism; no revision needed.

---

## 6. Module and GO-curation recommendations

- **S1 (EF-P stall rescue): mark COVERED** — efp / PP_1858 / Q88LS0.
- **Module scope: keep single-gene**; do **not** fold earP or the dTDP-L-rhamnose (*rml/rfb*) genes into UPA00345. Represent EarP activation and rhamnose supply as **separate linked modules** if cross-references are desired.
- **not_expected_in_target_taxon:** EpmA/EpmB/EpmC (β-lysine) activation route.
- **module_needs_revision:** No.
- **New GO term / document requests:** None required for UPA00345 itself. Optionally request/verify a curated cross-reference linking EF-P (GO:0043022/GO:0003746, ribosome-associated stall rescue) to the EarP rhamnosylation activation module, and file a **UniProt correction** for the Q88LS1 "Lys-32" → "Arg-32" residue text.

---

## 7. Genes to promote to full review

1. **efp (PP_1858, Q88LS0)** — promote to full `fetch-gene` review as the module anchor (highest priority; the covered step).
2. **earP (PP_1857, Q88LS1)** — optional secondary promotion as the obligate activation partner (adjacent gene, experimental evidence, contains the annotation typo to fix). Not a UPA00345 member but essential to interpret EF-P functionality in this taxon.

---

## 8. Key references

- Lassak J. *et al.* (2015) *Arginine-rhamnosylation as new strategy to activate translation elongation factor P.* **Nat Chem Biol** — PMID **25686373** (corrigendum PMID 25785429). EarP + dTDP-L-rhamnose; occurs in *Pseudomonas*.
- Krafczyk R. *et al.* (2017) *Structural Basis for EarP-Mediated Arginine Glycosylation of EF-P.* — PMID **28951478**. Rhamnosylation on Arg32; cited by KT2440 UniProt entries.
- Huter P. *et al.* (2017) *Structural Basis for Polyproline-Mediated Ribosome Stalling and Rescue by EF-P.* — PMID **29100052**. Mechanism of stall rescue.
- Yanagisawa T. *et al.* (2016) *N. meningitidis EF-P and its active-site Arg are essential…* — PMID **26840407**. EF-P/Arg-modification dispensable in *P. aeruginosa*/*S. oneidensis*.
- Lassak J., Wilson D.N., Jung K. (2016) *Stall no more at polyproline stretches…* (review) — PMID **26416626**.
- Sieber A. *et al.* (2024) *EF-P and its paralog EfpL (YeiP)…* — PMID **39622818**. EfpL/YeiP paralog (absent in KT2440).
- UniProtKB: **Q88LS0** (EFP_PSEPK), **Q88LS1** (EARP_PSEPK); HAMAP rule MF_00141.

---

### Evidence provenance summary
- **Direct for KT2440:** UniProt reviewed annotations (efp Q88LS0, earP Q88LS1), efp Arg32 sequence (loop G31-R32-N33) + rhamnosylation feature, gene adjacency PP_1857/PP_1858, complete *rml* cluster PP_1782–1785, and genomic **absence** of epmA/B/C.
- **Genus/strong transfer (*P. aeruginosa*, *Pseudomonas*):** EarP rhamnosylation chemistry, requirement for EF-P function, non-essentiality.
- **Homology/rule-based:** core EF-P peptide-bond-formation function (HAMAP MF_00141).
- **Open questions:** direct experimental demonstration of polyproline-stall rescue specifically in KT2440 (vs. *P. aeruginosa*) is lacking; whether EF-P/EarP loss produces a measurable fitness/proteome phenotype in KT2440's saprophytic lifestyle is untested; correct the UniProt Q88LS1 "Lys-32" text to "Arg-32". (The *rmlB* locus is now confirmed as rffG/PP_1785.)


## Artifacts

- [OpenScientist final report](PSEPK__efp_translation_stall_rescue__upa00345-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__efp_translation_stall_rescue__upa00345-deep-research-openscientist_artifacts/final_report.pdf)