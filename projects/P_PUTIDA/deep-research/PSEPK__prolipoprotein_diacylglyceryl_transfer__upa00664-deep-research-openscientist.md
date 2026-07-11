---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T14:26:52.992728'
end_time: '2026-07-11T14:38:05.686962'
duration_seconds: 672.69
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: prolipoprotein diacylglyceryl transfer
  module_summary: A Pseudomonas putida KT2440 UniPathway UPA00664 module for the first
    bacterial lipoprotein-maturation step, in which Lgt transfers a diacylglyceryl
    group from phosphatidylglycerol to the conserved N-terminal cysteine of a prolipoprotein.
    The local UniPathway bucket contains lgt/PP_5142/Q88CN8, a reviewed UniProtKB
    phosphatidylglycerol--prolipoprotein diacylglyceryl transferase entry with EC
    2.5.1.145 and Rhea:RHEA:56712. This module records the Lgt transfer reaction rather
    than the downstream signal-peptide cleavage and N-acylation steps catalyzed by
    LspA and Lnt.
  module_outline: "- prolipoprotein diacylglyceryl transfer\n  - 1. Lgt diacylglyceryl\
    \ transfer to prolipoprotein cysteine\n  - Lgt prolipoprotein diacylglyceryl transfer\n\
    \    - lgt: prolipoprotein diacylglyceryl transferase (molecular player: PSEPK\
    \ lgt; activity or role: phosphatidylglycerol-prolipoprotein diacylglyceryl transferase\
    \ activity)"
  module_connections: No explicit connections.
  pathway_query: UPA00664
  pathway_id: UPA00664
  pathway_name: UniPathway UPA00664
  pathway_source: UniPathway
  pathway_context: 'Resolved local bucket unipathway:UPA00664 with 1 primary genes;
    module area: unipathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '1'
  candidate_genes: '- lgt: PP_5142 | Q88CN8 | Phosphatidylglycerol--prolipoprotein
    diacylglyceryl transferase (EC 2.5.1.145) (EC 2.5.1.145; primary bucket unipathway:UPA00664)'
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
citation_count: 4
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__prolipoprotein_diacylglyceryl_transfer__upa00664-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__prolipoprotein_diacylglyceryl_transfer__upa00664-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

prolipoprotein diacylglyceryl transfer in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: UPA00664
- Resolved ID: UPA00664
- Resolved name: UniPathway UPA00664
- Source: UniPathway

Resolved local bucket unipathway:UPA00664 with 1 primary genes; module area: unipathway.

## Candidate Genes From Local Metadata

Candidate gene count: 1

- lgt: PP_5142 | Q88CN8 | Phosphatidylglycerol--prolipoprotein diacylglyceryl transferase (EC 2.5.1.145) (EC 2.5.1.145; primary bucket unipathway:UPA00664)

## Generic Module Context

### Working Scope

A Pseudomonas putida KT2440 UniPathway UPA00664 module for the first bacterial lipoprotein-maturation step, in which Lgt transfers a diacylglyceryl group from phosphatidylglycerol to the conserved N-terminal cysteine of a prolipoprotein. The local UniPathway bucket contains lgt/PP_5142/Q88CN8, a reviewed UniProtKB phosphatidylglycerol--prolipoprotein diacylglyceryl transferase entry with EC 2.5.1.145 and Rhea:RHEA:56712. This module records the Lgt transfer reaction rather than the downstream signal-peptide cleavage and N-acylation steps catalyzed by LspA and Lnt.

### Provisional Biological Outline

- prolipoprotein diacylglyceryl transfer
  - 1. Lgt diacylglyceryl transfer to prolipoprotein cysteine
  - Lgt prolipoprotein diacylglyceryl transfer
    - lgt: prolipoprotein diacylglyceryl transferase (molecular player: PSEPK lgt; activity or role: phosphatidylglycerol-prolipoprotein diacylglyceryl transferase activity)

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

# Module/Pathway/Taxon Review: Prolipoprotein Diacylglyceryl Transfer (UniPathway UPA00664) in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** UniPathway UPA00664 — "prolipoprotein diacylglyceryl transfer"
**Module area:** unipathway
**Candidate gene count (local metadata):** 1 — lgt/PP_5142/Q88CN8

---

## 1. Executive Summary

The UniPathway UPA00664 module — the first, committed step of bacterial lipoprotein maturation, in which **Lgt (phosphatidylglycerol--prolipoprotein diacylglyceryl transferase, EC 2.5.1.145)** transfers a diacylglyceryl group from phosphatidylglycerol to the conserved N-terminal cysteine of a prolipoprotein — is **COVERED (satisfied)** in *Pseudomonas putida* KT2440 by a single reviewed, single-copy gene: **lgt/PP_5142/Q88CN8**. This is the only bona fide Lgt-family gene in the KT2440 proteome, and its assignment rests on a UniProtKB/Swiss-Prot reviewed entry annotated by HAMAP-Rule MF_01147, carrying the correct EC number (2.5.1.145), Rhea reaction (RHEA:56712), UniPathway (UPA00664), and canonical seven-transmembrane inner-membrane Lgt architecture. Residue-level inspection confirms that Q88CN8 retains the complete set of diagnostic Lgt catalytic sequence motifs, including the essential active-site arginines, making the annotation robust at the sequence level.

The one substantive curation hazard uncovered by this review is **PP_4236/Q88F63**, which superficially resembles a second Lgt because it carries the Lgt GO term (**GO:0008961**) and a Pfam PF01790 (Lgt) domain match. This is an **over-propagated annotation**. PP_4236 is in fact a **DsbE/CcmG-type thiol:disulfide oxidoreductase**: its PF01790 signature is only a partial N-terminal match (residues ~4–100), while its functionally decisive domain is a complete thioredoxin/redoxin fold (residues ~130–269) with an intact active site. PP_4236 must **not** be counted toward UPA00664 satisfiability; doing so would falsely inflate the module to two genes and mis-annotate a redox protein as a lipoprotein-maturation enzyme.

Module boundaries are correct as drawn. The downstream lipoprotein-maturation steps — signal-peptide cleavage by **LspA (PP_0604)** and N-acylation by **Lnt (PP_4790)** — are both encoded in KT2440 but belong to **separate modules**, consistent with UniProt's PATHWAY annotation on Q88CN8 that scopes UPA00664 specifically to the "diacylglyceryl transfer" sub-step. No new module documents or GO term requests are required. The single recommendation for downstream curation is a flag on PP_4236 to correct or qualify its GO:0008961 assignment. Overall confidence in module satisfiability is **high**, with the residual caveat that all evidence is rule-based/homology-derived (protein existence level PE3) rather than derived from KT2440-specific biochemical experiments.

---

## 2. Target-Organism Pathway Definition

### 2.1 What UPA00664 includes

UPA00664 records **exactly one biochemical transformation** — the Lgt-catalyzed diacylglyceryl transfer reaction (Rhea:RHEA:56712):

```
L-cysteinyl-[prolipoprotein]
      + 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol)   [phosphatidylglycerol]
  ─────────────────────────────────────────────────────────────►
S-diacylglyceryl-L-cysteinyl-[prolipoprotein]
      + sn-glycerol-1-phosphate
      + H+
```

This is the **first and committed step** of the Gram-negative lipoprotein biogenesis pathway. The product — a diacylglyceryl-modified prolipoprotein — is the substrate for the subsequent maturation machinery. Because the modification occurs on the invariant "+1" cysteine of the lipobox, Lgt effectively defines which proteins enter the lipoprotein maturation route.

### 2.2 What must be kept separate

The UPA00664 bucket is deliberately narrow. The following **neighboring steps are outside its boundary** and should be curated in their own modules:

| Step | Enzyme | KT2440 gene | EC | Scope |
|------|--------|-------------|----|-------|
| 1. Diacylglyceryl transfer | Lgt | **PP_5142** (Q88CN8) | 2.5.1.145 | **UPA00664 (this module)** |
| 2. Signal-peptide cleavage | LspA (signal peptidase II) | PP_0604 (Q88Q91) | 3.4.23.36 | Separate module |
| 3. N-acylation of the new N-terminal Cys | Lnt (apolipoprotein N-acyltransferase) | PP_4790 (Q88DN4) | 2.3.1.269 | Separate module |

Broad overview maps (e.g., generic "lipoprotein biosynthesis," "membrane lipid metabolism," or KEGG global maps) should not be conflated with UPA00664. The UniProt PATHWAY line on Q88CN8 — "Protein modification; lipoprotein biosynthesis (diacylglyceryl transfer)" — makes the intended narrow scope explicit.

### 2.3 Alternate names / database definitions

- **Gene name:** *lgt* (also historically *umpA*)
- **Enzyme:** phosphatidylglycerol--prolipoprotein diacylglyceryl transferase; prolipoprotein diacylglyceryl transferase; lipoprotein diacylglyceryl transferase
- **EC:** 2.5.1.145
- **Rhea:** RHEA:56712
- **GO (molecular function):** GO:0008961
- **GO (process):** GO:0042158 (lipoprotein biosynthetic process)
- **Family models:** HAMAP MF_01147; InterPro IPR001640; Pfam PF01790; NCBIfam/TIGRFAM TIGR00544; PROSITE PS01311

---

## 3. Expected Step Model

For a Gram-negative proteobacterium such as *P. putida* KT2440, the expected minimal step model for UPA00664 is a **single enzymatic step encoded by a single essential inner-membrane gene**. This expectation is grounded in the established biology of Lgt across Gram-negative bacteria:

- Lgt catalyzes the **first step** in lipoprotein biogenesis ([PMID: 33875545](https://pubmed.ncbi.nlm.nih.gov/33875545/)).
- Lgt is **essential**: deletion of *lgt* is lethal to most Gram-negative bacteria ([PMID: 26729647](https://pubmed.ncbi.nlm.nih.gov/26729647/)).

Consequently, the expected model is:

```
UPA00664  ── single step ──►  Lgt (one gene, essential, inner membrane, 7-TM)
                                   │
                                   └── expected: exactly one bona fide Lgt-family
                                       (PF01790 / TIGR00544 / MF_01147) protein
```

A well-curated KT2440 proteome should therefore contain **exactly one** high-confidence Lgt. Any additional PF01790 hits must be scrutinized for partial/over-propagated annotation rather than accepted as paralogs. This review confirms that expectation is met: one genuine Lgt (PP_5142) plus one false-positive PF01790 protein (PP_4236, a DsbE).

---

## 4. Candidate Genes and Evidence

### 4.1 PP_5142 / Q88CN8 / *lgt* — the bona fide Lgt (COVERED)

**Verdict: covered — high confidence.** This is the correct and sole gene satisfying UPA00664.

| Attribute | Value |
|-----------|-------|
| UniProtKB | Q88CN8, **reviewed (Swiss-Prot)** |
| Gene / locus | *lgt* / PP_5142 |
| Length | 268 aa |
| EC | 2.5.1.145 |
| Reaction | Rhea:RHEA:56712 |
| Pathway | UniPathway UPA00664 |
| Family rule | HAMAP MF_01147 |
| Domain models | InterPro IPR001640; Pfam PF01790; NCBIfam TIGR00544; PROSITE PS01311 |
| Architecture | Canonical 7 transmembrane helices; conserved binding site at residue 139 |
| Localization | Cell inner membrane |
| Protein existence | **PE3 (inferred from homology)** |
| Copy number | Single-copy — only bona fide Lgt in UP000000556 |

**Evidence type:** rule-based/homology (Swiss-Prot + HAMAP), reinforced by residue-level motif analysis. Q88CN8 contains the **complete diagnostic Lgt fingerprint set**:

- **HWYG** motif (position ~20)
- **GRLGY** motif (position ~68), including the catalytically essential **Arg69**
- **GGMSFHGG** motif (position ~94)
- **GAGR-x-GNFIN-x-ELWG** catalytic loop (positions ~136–150)
- **HAMAP-annotated binding-site Arg139**
- Only **2 cysteines** total, consistent with the cysteine-independent Lgt catalytic mechanism

These motifs and conserved arginines correspond to the catalytically critical residues established in the *E. coli* Lgt crystal structure ([PMID: 26729647](https://pubmed.ncbi.nlm.nih.gov/26729647/)), which identified essential arginines (Arg143, Arg239 in *E. coli* numbering) required for diacylglyceryl transfer. The KT2440 protein retains the homologous conserved arginines in the diagnostic GRLGY and binding-site loops.

**Curation caveats:**
- Evidence is **not KT2440-specific experimentally** (PE3). No published biochemical or genetic characterization of *P. putida* KT2440 Lgt was found; function is transferred from the well-studied *E. coli* enzyme and enforced by HAMAP. Given the strong sequence conservation, essentiality, and complete motif retention, this transfer is **strong**.
- No paralog ambiguity for the genuine enzyme — it is single-copy.

### 4.2 PP_4236 / Q88F63 — over-annotated DsbE, NOT a second Lgt (exclude)

**Verdict: over-propagated annotation — must be excluded from UPA00664.**

Although PP_4236 carries the Lgt GO term GO:0008961 and a PF01790 domain hit, it is a **DsbE/CcmG-type thiol:disulfide oxidoreductase**, not a diacylglyceryl transferase.

| Attribute | Value |
|-----------|-------|
| UniProtKB | Q88F63, **unreviewed (TrEMBL)** |
| Locus | PP_4236 |
| Length | 278 aa |
| Submission name | "Thiol:disulfide interchange protein dsbE" |
| Protein existence | **PE4 (predicted)** |
| Domains | Pfam PF01790 (Lgt-like, **partial**) + PF08534 (Redoxin/thioredoxin) |
| InterPro | IPR001640 (Lgt) + IPR013766, IPR017937 (thioredoxin) |
| GO (real function) | GO:0015036 (disulfide oxidoreductase), GO:0017004 (cytochrome complex assembly) |
| GO (over-propagated) | GO:0008961 (Lgt activity), GO:0042158 |

**Domain architecture (decisive evidence):**

```
Q88F63 (278 aa)
  ├─ residues   4–100 : PF01790 / IPR001640 (Lgt) ── PARTIAL N-terminal match only
  └─ residues 130–269 : COMPLETE thioredoxin/redoxin fold
        ├─ CDD cd02966  TlpA_like_family        (138–251)
        ├─ Pfam PF08534 Redoxin                 (132–254)
        ├─ PANTHER PTHR42852 ResA/DsbE subfamily (130–263)
        ├─ PROSITE PS00194 thioredoxin active site (160–178)
        └─ CATH Glutaredoxin/Thioredoxin-like superfamily
```

The functional, complete domain is the **thioredoxin/DsbE fold with an intact active site (PS00194)** — the hallmark of a periplasmic thiol:disulfide oxidoreductase involved in cytochrome *c* maturation. The Lgt (PF01790) signature is only a **partial N-terminal fragment (4–100)** and lacks the full 7-TM Lgt architecture and catalytic loop that the genuine Lgt (Q88CN8) possesses. The GO:0008961 assignment is therefore an **electronic over-propagation** driven by the partial PF01790 match and should not be treated as evidence of Lgt function.

**Curation action:** flag GO:0008961 / GO:0042158 on PP_4236 as likely incorrect (over-propagated); retain the disulfide-oxidoreductase / cytochrome-maturation annotations.

### 4.3 Downstream genes (context only — outside UPA00664)

| Gene | Locus | UniProt | Enzyme | EC | Status |
|------|-------|---------|--------|----|--------|
| *lspA* | PP_0604 | Q88Q91 | Lipoprotein signal peptidase (SPase II) | 3.4.23.36 | Present, single-copy — **separate module** |
| *lnt* | PP_4790 | Q88DN4 | Apolipoprotein N-acyltransferase | 2.3.1.269 | Present, single-copy — **separate module** |

Both are present as single reviewed-family genes, confirming that the full lipoprotein maturation route is intact in KT2440, but they lie **outside** the UPA00664 boundary and should not be folded into this module.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 No true gaps
The single expected step (Lgt diacylglyceryl transfer) is present and well-supported. There is **no missing step** within the UPA00664 boundary. There is no evidence for, or expectation of, a lineage-specific alternative enzyme replacing Lgt in *P. putida* — the enzyme family is universally conserved and essential across Gram-negative proteobacteria.

### 5.2 Principal ambiguity: PP_4236 paralog/over-annotation
The only ambiguity is the false second-Lgt signal from **PP_4236**. This is resolved decisively in favor of a DsbE/CcmG oxidoreductase identity (see §4.2). It is the classic pattern of Pfam-domain over-propagation: a partial shared domain (PF01790) triggers a molecular-function GO term that the protein does not actually perform. Curators should record this explicitly to prevent future re-introduction of PP_4236 as a UPA00664 candidate.

### 5.3 Evidence-level caveat
The genuine Lgt (Q88CN8) is **PE3 (inferred from homology)** — there is **no direct KT2440 experimental characterization**. This is a knowledge gap, not a satisfiability gap: the rule-based and residue-level evidence is strong enough to mark the module covered, but the "direct experimental in target strain" box remains unchecked.

---

## 6. Module and GO-Curation Recommendations

### 6.1 Step status assignments

| Module step | Gene | Recommended status | Rationale |
|-------------|------|--------------------|-----------|
| Lgt diacylglyceryl transfer (UPA00664) | PP_5142 / Q88CN8 | **covered** | Reviewed Swiss-Prot, single-copy, correct EC/Rhea/UniPathway, complete Lgt motif set, canonical 7-TM architecture |
| (spurious second Lgt) | PP_4236 / Q88F63 | **not a candidate — exclude** | DsbE/CcmG oxidoreductase; GO:0008961 over-propagated from partial PF01790 |

**Module-level verdict: COVERED.** The module is satisfiable in *P. putida* KT2440 with a single gene.

### 6.2 Module boundaries
Existing generic module boundaries are **correct** for this organism. UPA00664 is properly scoped to the Lgt step only; LspA (PP_0604) and Lnt (PP_4790) should remain in their own modules. No `module_needs_revision` flag is warranted for boundary reasons.

### 6.3 GO-curation action
- **PP_4236 (Q88F63):** recommend flagging **GO:0008961** (and GO:0042158) as an **over-propagated/incorrect molecular-function annotation**; the accurate annotations are the disulfide-oxidoreductase (GO:0015036) and cytochrome-complex-assembly (GO:0017004) terms. Consider an annotation-quality report to the source database.
- **No new module documents or new GO term requests are needed.** Existing terms and models (MF_01147, IPR001640, PF01790, TIGR00544, GO:0008961) adequately describe the genuine enzyme.

---

## 7. Genes to Promote to Full Review

| Gene | Promote to `fetch-gene`? | Reason |
|------|--------------------------|--------|
| **PP_5142 / Q88CN8 (lgt)** | Optional / low priority | Already reviewed Swiss-Prot with complete evidence; a full review would mainly confirm PE3→experimental status. Promote only if the module requires target-strain experimental validation. |
| **PP_4236 / Q88F63 (dsbE)** | **Yes — recommended** | Needs a full-review pass to formally correct/qualify the over-propagated GO:0008961 Lgt annotation and lock in its DsbE/CcmG identity, preventing recurrence as a false UPA00664 candidate. |

The highest-value curation action is promoting **PP_4236** to full review to fix its annotation, not further validating the already-solid PP_5142.

---

## 8. Mechanistic Model / Interpretation

The KT2440 lipoprotein maturation pathway follows the canonical Gram-negative three-enzyme cascade, of which UPA00664 captures only the first, committed step:

```
 Prolipoprotein (with lipobox, +1 Cys)
            │
            │  ┌─────────────────────────────────────────────┐
   UPA00664 │  │ STEP 1 — Lgt  (PP_5142 / Q88CN8) EC 2.5.1.145 │  ◄── THIS MODULE
   (scope)  │  │  transfers diacylglyceryl from PG to Cys-SH   │
            ▼  └─────────────────────────────────────────────┘
 S-diacylglyceryl-prolipoprotein
            │
            │     STEP 2 — LspA (PP_0604) EC 3.4.23.36   ── separate module
            ▼        cleaves signal peptide
 Apolipoprotein (N-terminal diacylglyceryl-Cys)
            │
            │     STEP 3 — Lnt  (PP_4790) EC 2.3.1.269   ── separate module
            ▼        N-acylates the new N-terminal Cys
 Mature triacylated lipoprotein  ──►  Lol system  ──►  OM/IM sorting
```

The single-copy, essential nature of Lgt makes UPA00664 a "clean" module: one gene, one reaction, no redundancy, no lineage-specific substitution expected. The investigative value of this review lies less in confirming the obvious (PP_5142 is Lgt) and more in **catching the decoy** (PP_4236), which illustrates a general curation principle — a shared Pfam domain and an inherited GO term are insufficient evidence of function when the domain match is partial and a different, complete fold dominates the protein.

---

## 9. Evidence Base

| PMID | Title (abbrev.) | Relevance to this review |
|------|-----------------|--------------------------|
| [26729647](https://pubmed.ncbi.nlm.nih.gov/26729647/) | *Crystal structure of E. coli lipoprotein diacylglyceryl transferase* | Defines the Lgt fold, catalytic arginines, and essentiality; basis for interpreting the conserved motifs/arginines retained in KT2440 Q88CN8. States: "Deletion of the lgt gene is lethal to most Gram-negative bacteria" and identifies "critical residues, including Arg143 and Arg239, that are essential for diacylglyceryl transfer." |
| [33875545](https://pubmed.ncbi.nlm.nih.gov/33875545/) | *Inhibition of E. coli Lipoprotein Diacylglyceryl Transferase...* | Confirms Lgt "catalyzes the first step in the biogenesis of Gram-negative bacterial lipoproteins," matching the UPA00664 diacylglyceryl-transfer step assigned to PP_5142. |
| [35938851](https://pubmed.ncbi.nlm.nih.gov/35938851/) | *A Defect in Lipoprotein Modification by Lgt Leads to Abnormal Morphology and Cell Death in E. coli...* | Supports essentiality and physiological importance of Lgt in proteobacteria, reinforcing the "single essential gene" expectation. |
| [40607986](https://pubmed.ncbi.nlm.nih.gov/40607986/) | *Engineered Membrane Vesicle Production...* (Pseudomonas platform) | Context for lipoprotein biology (e.g., OprI) in the *Pseudomonas* platform; peripheral to the Lgt step but relevant to downstream lipoprotein function. |

**How the evidence maps to findings:**
- Findings F001 (module covered by PP_5142) and F005 (residue-level Lgt confirmation) rest on Swiss-Prot/HAMAP annotation plus the *E. coli* structural/mechanistic literature ([PMID: 26729647](https://pubmed.ncbi.nlm.nih.gov/26729647/), [PMID: 33875545](https://pubmed.ncbi.nlm.nih.gov/33875545/)).
- Findings F002 and F004 (PP_4236 is DsbE, not Lgt) rest on comparative domain-architecture analysis (Pfam/InterPro/CDD/PANTHER/PROSITE), not on the primary literature.
- Finding F003 (LspA/Lnt present but outside UPA00664) rests on proteome-level UniProt annotations.

---

## 10. Limitations and Knowledge Gaps

1. **No target-strain experimental evidence.** Q88CN8 is PE3 (inferred from homology). There is no published biochemical assay, structure, or knockout phenotype for *P. putida* KT2440 Lgt specifically. Function transfer from *E. coli* is strong but not experimentally verified in-strain.
2. **Species transfer.** All mechanistic and essentiality claims derive from *E. coli* studies. Transfer to *P. putida* is well-justified (universal, essential enzyme; complete motif conservation) but should be labeled as **homology-based, strong**, not direct.
3. **PP_4236 identity confidence.** The DsbE reassignment is based on domain architecture and sequence models (TrEMBL, PE4), not experiments. It is highly consistent but not experimentally proven.
4. **Downstream steps not exhaustively validated.** LspA and Lnt were confirmed present at the annotation level but were not the focus of this review and lie outside the module.

---

## 11. Proposed Follow-up Experiments / Actions

**Curation actions (highest priority, no wet-lab needed):**
1. Mark UPA00664 module **COVERED** in KT2440 with PP_5142/Q88CN8 as the sole satisfying gene.
2. **Promote PP_4236/Q88F63 to full `fetch-gene` review** and flag its GO:0008961/GO:0042158 as over-propagated; affirm its DsbE/CcmG (GO:0015036, GO:0017004) identity.
3. Record explicit exclusion note so PP_4236 is not re-suggested as a UPA00664 candidate in future automated passes.
4. Confirm LspA (PP_0604) and Lnt (PP_4790) are curated in their own downstream modules.

**Optional experimental validation (if in-strain evidence is required):**
5. Conditional-depletion or complementation assay of KT2440 *lgt* (PP_5142) to confirm essentiality and diacylglyceryl-transfer activity in-strain, upgrading PE3→experimental.
6. Biochemical/redox assay of PP_4236 to formally confirm thiol:disulfide oxidoreductase (DsbE/CcmG) function and absence of Lgt activity.

---

## 12. Key References

1. Crystal structure of *E. coli* lipoprotein diacylglyceryl transferase. [PMID: 26729647](https://pubmed.ncbi.nlm.nih.gov/26729647/)
2. Inhibition of *E. coli* Lipoprotein Diacylglyceryl Transferase Is Insensitive to Resistance Caused by Deletion of Braun's Lipoprotein. [PMID: 33875545](https://pubmed.ncbi.nlm.nih.gov/33875545/)
3. A Defect in Lipoprotein Modification by Lgt Leads to Abnormal Morphology and Cell Death in *Escherichia coli* That Is Independent of Major Lipoprotein Lpp. [PMID: 35938851](https://pubmed.ncbi.nlm.nih.gov/35938851/)
4. Engineered Membrane Vesicle Production via ... (*Pseudomonas* platform). [PMID: 40607986](https://pubmed.ncbi.nlm.nih.gov/40607986/)

**Primary database entries:** UniProtKB Q88CN8 (lgt/PP_5142, reviewed); UniProtKB Q88F63 (PP_4236, unreviewed); UniPathway UPA00664; Rhea RHEA:56712; HAMAP MF_01147; InterPro IPR001640; Pfam PF01790; NCBIfam TIGR00544; PROSITE PS01311.

---

*Report prepared for manual module satisfiability and gene-annotation curation. Module verdict: **COVERED** by single-copy lgt/PP_5142. Principal curation action: correct the over-propagated Lgt GO term on PP_4236 (a DsbE).*


## Artifacts

- [OpenScientist final report](PSEPK__prolipoprotein_diacylglyceryl_transfer__upa00664-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__prolipoprotein_diacylglyceryl_transfer__upa00664-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:33875545
2. PMID:26729647
3. PMID:35938851
4. PMID:40607986