---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T14:36:37.450045'
end_time: '2026-07-11T14:57:28.883025'
duration_seconds: 1251.43
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Apolipoprotein N-acyltransferase
  module_summary: A Pseudomonas putida KT2440 UniPathway UPA00666 module for the final
    phospholipid-dependent N-acylation step of bacterial lipoprotein maturation. The
    module is centered on Lnt (PP_4790, UniProtKB:Q88DN4), which transfers an acyl
    chain from a glycerophospholipid to the amino group of the N-terminal cysteine
    of a diacylglyceryl lipoprotein.
  module_outline: "- Apolipoprotein N-acyltransferase\n  - 1. Final N-acylation of\
    \ mature bacterial lipoprotein\n  - Lnt apolipoprotein N-acyltransferase step\n\
    \    - lnt: apolipoprotein N-acyltransferase (molecular player: PSEPK lnt; activity\
    \ or role: N-acyltransferase activity)"
  module_connections: No explicit connections.
  pathway_query: UPA00666
  pathway_id: UPA00666
  pathway_name: UniPathway UPA00666
  pathway_source: UniPathway
  pathway_context: 'Resolved local bucket unipathway:UPA00666 with 1 primary genes;
    module area: unipathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '1'
  candidate_genes: '- lnt: PP_4790 | Q88DN4 | Apolipoprotein N-acyltransferase (ALP
    N-acyltransferase) (EC 2.3.1.269) (EC 2.3.1.269; primary bucket unipathway:UPA00666)'
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
  path: PSEPK__apolipoprotein_n_acyltransferase__upa00666-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__apolipoprotein_n_acyltransferase__upa00666-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Apolipoprotein N-acyltransferase in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: UPA00666
- Resolved ID: UPA00666
- Resolved name: UniPathway UPA00666
- Source: UniPathway

Resolved local bucket unipathway:UPA00666 with 1 primary genes; module area: unipathway.

## Candidate Genes From Local Metadata

Candidate gene count: 1

- lnt: PP_4790 | Q88DN4 | Apolipoprotein N-acyltransferase (ALP N-acyltransferase) (EC 2.3.1.269) (EC 2.3.1.269; primary bucket unipathway:UPA00666)

## Generic Module Context

### Working Scope

A Pseudomonas putida KT2440 UniPathway UPA00666 module for the final phospholipid-dependent N-acylation step of bacterial lipoprotein maturation. The module is centered on Lnt (PP_4790, UniProtKB:Q88DN4), which transfers an acyl chain from a glycerophospholipid to the amino group of the N-terminal cysteine of a diacylglyceryl lipoprotein.

### Provisional Biological Outline

- Apolipoprotein N-acyltransferase
  - 1. Final N-acylation of mature bacterial lipoprotein
  - Lnt apolipoprotein N-acyltransferase step
    - lnt: apolipoprotein N-acyltransferase (molecular player: PSEPK lnt; activity or role: N-acyltransferase activity)

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

# Module/Pathway Review: Apolipoprotein N-acyltransferase (UniPathway UPA00666) in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Module/bucket:** unipathway:UPA00666 — "Protein modification; lipoprotein biosynthesis (N-acyl transfer)"
**Primary gene:** lnt / PP_4790 / UniProtKB **Q88DN4**
**Iteration:** 1 of 3

---

## 1. Executive summary

- UPA00666 is a **single-step module** describing the final, phospholipid-dependent **N-acylation** of the N‑terminal cysteine of a diacylglyceryl-modified apolipoprotein, producing the mature triacylated lipoprotein. It is the third and last enzymatic step of the Lgt→LspA→Lnt lipoprotein maturation pathway.
- In *P. putida* KT2440 the module is **COVERED** by a single, high-confidence gene: **lnt / PP_4790 (Q88DN4)**, annotated as Apolipoprotein N‑acyltransferase, EC 2.3.1.269, inner-membrane, CN‑hydrolase family / apolipoprotein N‑acyltransferase subfamily.
- There is **no paralog ambiguity**: PP_4790 is the *only* PSEPK protein bearing the Lnt-specific InterPro signature (IPR004563) and EC 2.3.1.269. Other CN‑hydrolase (Pfam PF00795) members in the genome are metabolic nitrilases/amidases and are **not** over-annotated as N‑acyltransferases.
- The surrounding machinery is intact — upstream **lgt/PP_5142** and **lspA/PP_0604**, and the downstream **Lol** sorting system (lolA/PP_4003, lolB/PP_0724, lolCDE/PP_2154–2156) — supporting functional coherence.
- Confidence is further upgraded by **catalytic-residue verification**: PP_4790 shares **44% identity** with *E. coli* Lnt over the full length and conserves the **entire catalytic apparatus** — triad Glu267→Glu269, Lys335→Lys329, Cys387→Cys381 (nucleophile), plus accessory residues Glu343→Glu337, Trp237→Trp240, Tyr388→Tyr382, Glu389→Glu383 (this review's alignment).
- Principal caveat: the PSEPK Lnt annotation is **homology-inferred** (UniProt protein existence level 3); there is no direct enzymological or genetic characterization *in P. putida KT2440* itself. Confidence is nonetheless high because the family assignment is specific, the catalytic machinery is fully conserved, and the pathway context is complete.

**Recommendation:** mark the single module step **covered**; no gap, no revision needed. Promote PP_4790 to full `fetch-gene` review only for provenance/essentiality confirmation, not because of annotation doubt.

---

## 2. Target-organism pathway definition

**What the module includes (and only this):** transfer of one acyl chain from a *sn*-1 glycerophospholipid (e.g., phosphatidylethanolamine) to the free α‑amino group of the N‑terminal S‑diacylglyceryl‑cysteine of an apolipoprotein, yielding an amide-linked (N‑acyl) fatty acid and the mature triacylated lipoprotein. UniProt catalytic definition for Q88DN4:

> N-terminal S-1,2-diacyl-sn-glyceryl-L-cysteinyl-[lipoprotein] + a glycerophospholipid → N-acyl-S-1,2-diacyl-sn-glyceryl-L-cysteinyl-[lipoprotein] + a 2-acyl-sn-glycero-3-phospholipid + H⁺  (EC 2.3.1.269)

**Boundaries — keep separate:**
- **Lgt step** (PP_5142; EC 2.4.99.65-type diacylglyceryl transfer) and **LspA step** (PP_0604; signal peptidase II, EC 3.4.23.36). These are the two *upstream* steps of lipoprotein maturation and belong to their own UniPathway steps, not UPA00666.
- **Lol sorting / outer-membrane targeting** (LolABCDE) — a *downstream transport* process, not part of the N‑acyl-transfer biochemistry.
- **General "lipid/phospholipid metabolism" overview maps** — Lnt consumes a phospholipid as acyl donor but is a protein-modification enzyme, not a lipid-biosynthesis enzyme; do not merge into fatty-acid/phospholipid metabolism buckets.
- **Lnt-*like* N‑acyltransferases acting on non-lipoprotein substrates** (e.g., AatD of Enterobacterales, which acylates the anti-aggregation protein Aap; PMID 32845938). These are structural relatives, not part of canonical lipoprotein maturation, and are a known source of mis-transfer of the "Lnt" label — but no such gene is present in PSEPK.

**Alternate names / database mappings:** Lnt; apolipoprotein N‑acyltransferase; "ALP N-acyltransferase"; EC 2.3.1.269; KEGG ppu:PP_4790; eggNOG/COG0815; Pfam PF00795 (CN_hydrolase) + PF20154; InterPro IPR004563 (subfamily-specific), IPR003010, IPR036526, IPR045378; PROSITE PS50263; GO:0016410 (N-acyltransferase activity), GO:0042158 (lipoprotein biosynthetic process), GO:0005886 (plasma membrane).

---

## 3. Expected step model

UPA00666 as scoped is a **one-step module**:

| Step | Reaction | Expected enzyme | PSEPK gene | Status |
|------|----------|-----------------|------------|--------|
| S1 | Apolipoprotein → mature triacylated lipoprotein (N‑acyl transfer) | Lnt (EC 2.3.1.269) | **lnt / PP_4790 (Q88DN4)** | **covered** |

Contextual (out-of-module but confirming) steps of the wider maturation pathway, all present in PSEPK:
- Step −2 (Lgt): **PP_5142 (Q88CN8)**, phosphatidylglycerol–prolipoprotein diacylglyceryl transferase.
- Step −1 (LspA): **PP_0604 (Q88Q91)**, lipoprotein signal peptidase II.
- Downstream (Lol): PP_4003, PP_0724, PP_2154–2156.

No step is "missing but likely present under another name," because the module contains exactly one step and it is directly encoded. No step is "not expected" here.

---

## 4. Candidate genes and evidence

### lnt / PP_4790 / Q88DN4 — HIGH confidence

- **Role:** final N‑acylation step of lipoprotein maturation (EC 2.3.1.269); inner-membrane integral protein, 505 aa.
- **Evidence type:** sequence homology / family assignment (UniProt existence level 3 = "inferred from homology"). Family: **CN hydrolase → apolipoprotein N‑acyltransferase subfamily**; Lnt-specific **InterPro IPR004563**, **PROSITE PS50263**, **COG0815**. UniPathway UPA00666 and pathway comment "Protein modification; lipoprotein biosynthesis (N-acyl transfer)" both attached.
- **Mechanistic anchor (from orthologs, transfer to PSEPK strong):** *E. coli* Lnt proceeds via a covalent **thioester acyl-enzyme intermediate** on an active-site cysteine (Cys387), with a Glu–Lys–Cys catalytic triad (Glu267 required for acyl‑enzyme formation) and a ping-pong mechanism with phospholipid head-group/acyl-chain preference (PMIDs 20000742, 21676878). Structural basis of the reaction has been solved for a bacterial Lnt (PMID 28698362).
- **Catalytic-residue verification (this review, direct sequence evidence for PP_4790):** global BLOSUM62 alignment of Q88DN4 vs *E. coli* Lnt (P23930) gives **44.0% identity over 484 aligned positions**, and every functionally essential *E. coli* residue is conserved in PP_4790 — catalytic triad **Glu267→Glu269, Lys335→Lys329, Cys387→Cys381**; accessory residues **Glu343→Glu337, Trp237→Trp240, Tyr388→Tyr382, Glu389→Glu383** (roles per PMID 20000742). This makes the mechanistic transfer to *P. putida* **strong at residue resolution**, not merely fold-level.
- **Curation caveats:**
  - Annotation is homology-based; there is **no direct P. putida KT2440 biochemistry or knockout**. Returned essentiality/Tn-seq screens (e.g., PMID 33964456, 32826213, 40302248) did not explicitly report PP_4790 status in the abstracts examined.
  - The broad Pfam PF00795 fold is shared with unrelated nitrilases/amidases; rely on the **subfamily-level IPR004563 / EC 2.3.1.269**, not PF00795 alone, when asserting function.
  - EC 2.3.1.269 is highly specific (dedicated to this reaction), so the EC→function mapping here is safe (low over-broad-EC risk).

---

## 5. Gaps, ambiguities, and likely over-annotations

- **No gaps.** The single expected step is encoded.
- **No paralog ambiguity.** Exactly one IPR004563 / EC 2.3.1.269 protein exists in PSEPK (PP_4790). The other eight PF00795 CN‑hydrolase members — e.g., YafV omega-amidase (PP_0859, EC 3.5.1.3), davA (PP_0382), ramA (PP_3846), plus uncharacterized CN‑hydrolase-domain proteins (PP_3019, PP_0896, PP_4463, PP_2005, PP_0939) — are metabolic hydrolases and are **not** mis-labeled as N‑acyltransferases. No pruning needed.
- **Over-annotation risk elsewhere (not in PSEPK):** the AatD-type Lnt-like N‑acyltransferases of Enterobacterales acylate non-lipoprotein substrates (PMID 32845938). Curators should watch for this pattern in *other* genomes but it does not affect *P. putida* KT2440.
- **Essentiality nuance:** in most γ‑proteobacteria with a single Lol pathway (E. coli, Salmonella), *lnt* is **essential** (PMIDs 15513925, 21742870). Exceptions (Francisella, Neisseria) possess modified LolCDE able to sort diacylated lipoproteins and tolerate *lnt* loss (PMID 25755189). *P. putida* KT2440 has a canonical LolCDE (PP_2154–2156), so *lnt* is **predicted essential**; this is an inference, not a direct KT2440 measurement.

---

## 6. Module and GO-curation recommendations

- **Step S1 (N‑acyl transfer):** mark **covered** by PP_4790.
- **Module status:** **satisfiable / complete.** No `gap`, `candidate_uncertain`, `not_expected_in_target_taxon`, or `module_needs_revision` flags warranted.
- **Module boundaries:** the generic single-step scope is **correct** for this organism. Keep Lgt (PP_5142) and LspA (PP_0604) in their own upstream module steps; keep Lol sorting separate.
- **GO terms:** existing assignments (GO:0016410 N‑acyltransferase activity; GO:0042158 lipoprotein biosynthetic process; GO:0005886 plasma membrane) are appropriate. A more specific MF term "apolipoprotein N‑acyltransferase activity" would better match EC 2.3.1.269 if available/desired, but no new GO term request is strictly required.
- **No new module document needed.**

---

## 7. Genes to promote to full review

- **PP_4790 (lnt, Q88DN4):** the functional assignment is now well-supported (specific IPR004563 signature **and** full catalytic-triad conservation verified in this review), so promotion is **optional and low-priority** — useful only for provenance/essentiality confirmation (check KT2440 Tn-seq/CRISPRi essentiality datasets and add experimental-existence evidence if available). This is the only gene in the module.
- No other PSEPK gene needs promotion for this module.

---

## 8. Key references

- Robichon C, et al. (2005) Depletion of Lnt mislocalizes OM lipoproteins in *E. coli*; Lnt essential, 6 TM segments. **PMID 15513925**.
- Buddelmeijer N, Young R (2010) Lnt acts via an extracytoplasmic thioester acyl-enzyme intermediate; Glu–Cys catalytic residues (Cys387, Glu267). **PMID 20000742**.
- Hillmann F, et al. (2011) Kinetics and phospholipid specificity of Lnt; ping-pong mechanism. **PMID 21676878**.
- Narita S, Tokuda H (2011) LolCDE overexpression permits *lnt* deletion — links Lnt to Lol sorting. **PMID 21742870**.
- LoVullo ED, et al. (2015) *lnt* non-essential in *Francisella*/*Neisseria* with modified LolCDE — two classes of Gram-negatives. **PMID 25755189**.
- Noland CL, et al. (2017) Structural insights into lipoprotein N-acylation by Lnt. **PMID 28698362**.
- Nozeret K, et al. (2019) Sensitive fluorescence assay for Lnt activity. **PMID 31685855**.
- Belmont-Monroy L, et al. (2020) AatD, an Lnt-like N‑acyltransferase acting on non-lipoprotein Aap — over-annotation caution. **PMID 32845938**.
- Brülle JK, et al. (2013) Lnt in slow-growing mycobacteria; distribution of Lnt across GC-rich taxa. **PMID 24093492**.
- UniProtKB **Q88DN4** (lnt, PP_4790); KEGG **ppu:PP_4790**; UniPathway **UPA00666**; InterPro **IPR004563**.

---

## 9. Evidence provenance and open questions

**Direct for PSEPK (database/sequence evidence):** gene identity, family/InterPro/EC assignment, genomic presence of the full Lgt/LspA/Lnt + Lol machinery, single-copy status (no paralog), and the 44%-identity residue-level conservation of the catalytic triad in PP_4790 (this review's alignment vs *E. coli* P23930).

**Transferred from other bacteria (homology-based; strength noted):** the two-step ping-pong mechanism, thioester acyl-enzyme intermediate, phospholipid specificity, and essentiality/dispensability logic — all from *E. coli* and other Gram-negatives (strong transfer for mechanism given residue conservation; moderate for essentiality given differing Lol architectures across taxa).

**Open questions / experiments that would close remaining gaps:**
1. **Direct essentiality in KT2440** — targeted literature searches in this review did not surface a KT2440-specific *lnt* essentiality call. A CRISPRi knockdown or attempted markerless deletion (with/without LolCDE overexpression) would confirm the predicted-essential status.
2. **Experimental protein existence** — PP_4790 is currently existence-level 3 (homology); proteomic or activity evidence (e.g., the fluorescence Lnt assay, PMID 31685855) would raise it to experimental.
3. **Lipoprotein acylation state** — MS of a model KT2440 outer-membrane lipoprotein would confirm triacylation (N-acyl transfer actually occurring in vivo).

*No wet-lab characterization of PP_4790 in* P. putida *KT2440 was found in this review; the functional call rests on specific family signatures plus full catalytic-residue conservation, which together constitute strong (but indirect) evidence.*


## Artifacts

- [OpenScientist final report](PSEPK__apolipoprotein_n_acyltransferase__upa00666-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__apolipoprotein_n_acyltransferase__upa00666-deep-research-openscientist_artifacts/final_report.pdf)