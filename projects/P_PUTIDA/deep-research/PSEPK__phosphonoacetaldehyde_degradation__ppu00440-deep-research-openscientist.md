---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-16T10:44:20.994889'
end_time: '2026-07-16T11:57:34.728646'
duration_seconds: 4393.73
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: 2-aminoethylphosphonate degradation through phosphonoacetaldehyde
  module_summary: Species-neutral bacterial module for the PhnW/PhnX route of 2-aminoethylphosphonate
    degradation. PhnW first transaminates 2-aminoethylphosphonate with pyruvate to
    generate phosphonoacetaldehyde and L-alanine. PhnX then hydrolyzes phosphonoacetaldehyde,
    cleaving the carbon- phosphorus bond to yield acetaldehyde and inorganic phosphate.
    The module excludes unrelated C-P lyase systems and phosphonatase-family enzymes
    whose characterized substrates are not phosphonoacetaldehyde.
  module_outline: "- 2-aminoethylphosphonate degradation through phosphonoacetaldehyde\n\
    \  - 1. AEP transamination to phosphonoacetaldehyde\n  - PhnW AEP transamination\n\
    \    - phnW: 2-aminoethylphosphonate--pyruvate transaminase (molecular player:\
    \ PhnW AEP transaminase family; activity or role: 2-aminoethylphosphonate:pyruvate\
    \ transaminase activity)\n  - 2. C-P bond cleavage and phosphate release\n  -\
    \ PhnX phosphonoacetaldehyde hydrolysis\n    - phnX: phosphonoacetaldehyde hydrolase\
    \ (molecular player: PhnX phosphonatase family; activity or role: phosphonoacetaldehyde\
    \ hydrolase activity)"
  module_connections: '- PhnW AEP transamination feeds into PhnX phosphonoacetaldehyde
    hydrolysis: PhnW produces phosphonoacetaldehyde, which is the PhnX substrate.'
  pathway_query: ppu00440
  pathway_id: ppu00440
  pathway_name: Phosphonate and phosphinate metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00440 with 2 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '2'
  candidate_genes: '- phnX: PP_2208 | Q88KT1 | Phosphonoacetaldehyde hydrolase (Phosphonatase)
    (EC 3.11.1.1) (Phosphonoacetaldehyde phosphonohydrolase) (EC 3.11.1.1; primary
    bucket kegg:ppu00440)

    - phnW: PP_2209 | Q88KT0 | 2-aminoethylphosphonate--pyruvate transaminase (EC
    2.6.1.37) (2-aminoethylphosphonate aminotransferase) (AEP transaminase) (AEPT)
    (EC 2.6.1.37; primary bucket kegg:ppu00440)'
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
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__phosphonoacetaldehyde_degradation__ppu00440-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__phosphonoacetaldehyde_degradation__ppu00440-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

2-aminoethylphosphonate degradation through phosphonoacetaldehyde in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00440
- Resolved ID: ppu00440
- Resolved name: Phosphonate and phosphinate metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00440 with 2 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 2

- phnX: PP_2208 | Q88KT1 | Phosphonoacetaldehyde hydrolase (Phosphonatase) (EC 3.11.1.1) (Phosphonoacetaldehyde phosphonohydrolase) (EC 3.11.1.1; primary bucket kegg:ppu00440)
- phnW: PP_2209 | Q88KT0 | 2-aminoethylphosphonate--pyruvate transaminase (EC 2.6.1.37) (2-aminoethylphosphonate aminotransferase) (AEP transaminase) (AEPT) (EC 2.6.1.37; primary bucket kegg:ppu00440)

## Generic Module Context

### Working Scope

Species-neutral bacterial module for the PhnW/PhnX route of 2-aminoethylphosphonate degradation. PhnW first transaminates 2-aminoethylphosphonate with pyruvate to generate phosphonoacetaldehyde and L-alanine. PhnX then hydrolyzes phosphonoacetaldehyde, cleaving the carbon- phosphorus bond to yield acetaldehyde and inorganic phosphate. The module excludes unrelated C-P lyase systems and phosphonatase-family enzymes whose characterized substrates are not phosphonoacetaldehyde.

### Provisional Biological Outline

- 2-aminoethylphosphonate degradation through phosphonoacetaldehyde
  - 1. AEP transamination to phosphonoacetaldehyde
  - PhnW AEP transamination
    - phnW: 2-aminoethylphosphonate--pyruvate transaminase (molecular player: PhnW AEP transaminase family; activity or role: 2-aminoethylphosphonate:pyruvate transaminase activity)
  - 2. C-P bond cleavage and phosphate release
  - PhnX phosphonoacetaldehyde hydrolysis
    - phnX: phosphonoacetaldehyde hydrolase (molecular player: PhnX phosphonatase family; activity or role: phosphonoacetaldehyde hydrolase activity)

### Known Relationships Among Steps

- PhnW AEP transamination feeds into PhnX phosphonoacetaldehyde hydrolysis: PhnW produces phosphonoacetaldehyde, which is the PhnX substrate.

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

# Module Review: 2-Aminoethylphosphonate Degradation via Phosphonoacetaldehyde in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target pathway/bucket:** KEGG ppu00440 — Phosphonate and phosphinate metabolism (local bucket `kegg:ppu00440`)
**Module scope:** PhnW/PhnX route of 2-aminoethylphosphonate (AEP) degradation to acetaldehyde + inorganic phosphate

---

## 1. Executive Summary

Both enzymatic steps of the PhnW/PhnX 2-aminoethylphosphonate (AEP) degradation route are **present and should be marked COVERED** in *P. putida* KT2440. The two candidate genes supplied in the local metadata are correct and complete for the two-enzyme module: **phnW = PP_2209** (UniProt Q88KT0; EC 2.6.1.37; KEGG ortholog K03430) encodes the 2-aminoethylphosphonate:pyruvate transaminase that converts AEP + pyruvate into phosphonoacetaldehyde + L-alanine, and **phnX = PP_2208** (UniProt Q88KT1; EC 3.11.1.1; KEGG ortholog K05306) encodes the phosphonoacetaldehyde hydrolase (phosphonatase) that cleaves the carbon–phosphorus bond of phosphonoacetaldehyde to yield acetaldehyde and inorganic phosphate. The product of the first reaction is the substrate of the second, so the two genes together constitute a self-contained, linearly ordered catabolic module.

The gene assignments are clean and unambiguous. Genome-wide KEGG ortholog and EC scans confirm that both `phnW` and `phnX` are **single-copy** in KT2440 — K05306/EC 3.11.1.1 maps to exactly one gene (PP_2208) and K03430/EC 2.6.1.37 maps to exactly one gene (PP_2209) — so there is no paralog ambiguity and no evidence of annotation over-propagation. Both proteins carry **substrate-specific TIGRFAM/InterPro signatures** (PhnX: IPR006323 PhnX family; PhnW: IPR012703/TIGR02326 "NH2EtPonate_pyrv_transaminase"), meaning the annotations reflect the specific AEP-degrading reactions rather than generic HAD-hydrolase or class-V aminotransferase fold assignments. The two genes lie **immediately adjacent on the minus strand** as a tight `phnW→phnX` operon (34 bp intergenic gap), with a **divergently transcribed LysR-family regulator (PP_2210, candidate AepR)** upstream — the canonical architecture of a substrate-inducible catabolic operon. The competing broad-substrate **C–P lyase system (phnGHIJK) is entirely absent** from the genome, which correctly justifies its exclusion from the module boundary for this organism.

Direct biochemical evidence for KT2440 itself does not exist in the literature (UniProt evidence level 3, "inferred from homology"), but the transfer of function is strongly supported by **species-level enzyme-activity data in other *P. putida* strains**: strain NG2 was shown to possess both AEP:pyruvate aminotransferase and phosphonatase activities, inducible by AEP; and strain BIRD-1 was shown to catabolize AEP as a C, N, or P source through the PhnWX system under the control of a substrate-specific LysR regulator named AepR located upstream of phnWX — exactly mirroring the KT2440 gene arrangement. The only genuine gap is a **dedicated AEP-specific transporter**, which is not encoded in the recognizable phnSTUV form and lies outside the two-enzyme module scope. No module-boundary revisions are required, and no new GO terms are needed; both catalytic genes are recommended for promotion to full `fetch-gene` review to formally lock in the direct catalytic and genomic-context evidence.

---

## 2. Target-Organism Pathway Definition

### What the module includes

The module covers the **two-enzyme, linear catabolic route** by which 2-aminoethylphosphonate (AEP; ciliatine) is degraded to central-metabolism intermediates in *P. putida* KT2440:

1. **AEP transamination** (PhnW, EC 2.6.1.37): AEP + pyruvate → phosphonoacetaldehyde + L-alanine. A PLP-dependent class-V aminotransferase reaction that transfers the amino group of AEP to pyruvate, unmasking the aldehyde required for the subsequent C–P bond cleavage.
2. **Phosphonoacetaldehyde hydrolysis / C–P bond cleavage** (PhnX, EC 3.11.1.1): phosphonoacetaldehyde + H₂O → acetaldehyde + inorganic phosphate. A HAD-superfamily hydrolase that uses a Schiff-base mechanism (via a catalytic lysine) to hydrolytically cleave the phosphorus–carbon bond.

The acetaldehyde and released phosphate feed into central carbon metabolism and the cellular phosphate pool, respectively; L-alanine returns to amino-acid metabolism. The module therefore lets KT2440 exploit AEP as a source of carbon, nitrogen, and/or phosphorus.

### What must be kept separate (pathway boundaries)

- **C–P lyase system (phnGHIJK / phnK; KEGG K06163–K06166, K05781):** a mechanistically distinct, broad-substrate radical route for phosphonate degradation. It is **absent** in KT2440 and must not be conflated with the PhnWX substrate-specific route.
- **General phosphonate/phosphite ABC transporter (phnCDE, PP_0825–PP_0827):** present in the genome but an uptake system, not part of the two-enzyme catabolic module. It should be scoped out.
- **Other HAD-superfamily phosphatases and other class-V aminotransferases:** share folds with PhnX and PhnW but act on different substrates. The substrate-specific TIGRFAMs distinguish the true module members from these fold relatives.
- **KEGG overview map ppu00440 ("Phosphonate and phosphinate metabolism")** is a broad bucket that also nominally contains PEP-mutase/phosphonopyruvate biosynthetic steps and C–P lyase reactions; only the PhnW/PhnX sub-route is in scope here.

### Alternate names / database definitions

- **AEP** = 2-aminoethylphosphonate = 2-aminoethylphosphonic acid = (2-aminoethyl)phosphonate = ciliatine; abbreviated **2AEP** in some literature.
- **PhnW** = 2-aminoethylphosphonate—pyruvate transaminase = AEP transaminase (AEPT) = 2-aminoethylphosphonate aminotransferase.
- **PhnX** = phosphonoacetaldehyde hydrolase = phosphonatase = phosphonoacetaldehyde phosphonohydrolase.
- KEGG orthologs: **K03430 (phnW)**, **K05306 (phnX)**. EC numbers: **2.6.1.37 (phnW)**, **3.11.1.1 (phnX)**.

---

## 3. Expected Step Model

```
   2-aminoethylphosphonate (AEP)
            |
            |   [Step 1]  PhnW  (PP_2209 / Q88KT0)
            |   EC 2.6.1.37, K03430, class-V PLP aminotransferase
            |   AEP + pyruvate  -->  phosphonoacetaldehyde + L-alanine
            v
     phosphonoacetaldehyde (PAA)
            |
            |   [Step 2]  PhnX  (PP_2208 / Q88KT1)
            |   EC 3.11.1.1, K05306, HAD-superfamily hydrolase (Schiff-base)
            |   PAA + H2O  -->  acetaldehyde + Pi   (C-P bond cleavage)
            v
     acetaldehyde  +  inorganic phosphate
       (central C metabolism)   (cellular Pi pool)

  Regulation:  PP_2210 (LysR-family, candidate AepR), divergent, upstream of phnW
  Excluded:    C-P lyase phnGHIJK  = ABSENT in KT2440
  Out of scope: general phosphonate ABC transporter phnCDE (PP_0825-0827)
```

| Step | Reaction | Enzyme | Gene (locus) | UniProt | EC / KO | Module call |
|------|----------|--------|--------------|---------|---------|-------------|
| 1 | AEP + pyruvate → phosphonoacetaldehyde + L-alanine | PhnW (AEP:pyruvate transaminase) | PP_2209 | Q88KT0 | 2.6.1.37 / K03430 | **COVERED** |
| 2 | phosphonoacetaldehyde + H₂O → acetaldehyde + Pi | PhnX (phosphonatase) | PP_2208 | Q88KT1 | 3.11.1.1 / K05306 | **COVERED** |
| (Reg.) | Substrate induction of phnWX | AepR (LysR-type regulator) | PP_2210 | — | — | Context (candidate) |
| (Alt.) | Broad-substrate C–P lyase | PhnGHIJK | — | — | K06163–K06166, K05781 | **not_expected_in_target_taxon** |
| (Transport) | AEP uptake | dedicated AEP transporter | — | — | phnSTUV absent | **gap (out of module scope)** |

---

## 4. Candidate Genes and Evidence

### 4.1 phnW — PP_2209 (Q88KT0), 2-aminoethylphosphonate:pyruvate transaminase

**Likely role.** PhnW catalyzes the first committed step of AEP catabolism, transaminating AEP with pyruvate to give phosphonoacetaldehyde and L-alanine (EC 2.6.1.37; KEGG K03430). The 368-aa protein belongs to the **class-V PLP-dependent aminotransferase family** (Pfam PF00266 / Aminotran_5 fold, IPR000192).

**Evidence type.** Homology-based for KT2440 (UniProt evidence level 3; annotation score 2.0), reinforced by three strong lines of context:
- **Substrate-specific signatures:** InterPro annotations include the specific **IPR012703 "NH2EtPonate_pyrv_transaminase" (TIGR02326)** and **IPR024169 "SP_NH2Trfase/AEP_transaminase"**, in addition to the generic Aminotran_5 fold. This narrows the assignment to the AEP:pyruvate reaction rather than a generic class-V aminotransferase.
- **Single-copy:** K03430 and EC 2.6.1.37 each map to exactly one KT2440 gene (PP_2209) — no paralog ambiguity.
- **Genomic context:** encoded immediately upstream of and co-transcribed with phnX (see 4.3), and species-level activity data confirm AEP:pyruvate aminotransferase activity in *P. putida* (see 4.4).

**Curation caveats.** No KT2440-strain-specific biochemistry exists; the direct experimental support is at the species level (strains NG2, BIRD-1). The generic Aminotran_5 fold is shared with many transaminases, so annotation confidence rests on the substrate-specific TIGRFAM plus operon context, both of which are present here.

### 4.2 phnX — PP_2208 (Q88KT1), phosphonoacetaldehyde hydrolase (phosphonatase)

**Likely role.** PhnX cleaves the C–P bond of phosphonoacetaldehyde hydrolytically, producing acetaldehyde and inorganic phosphate (EC 3.11.1.1; KEGG K05306). The 275-aa protein is a member of the **HAD-like hydrolase superfamily / PhnX family**, uses Mg²⁺ as cofactor, and operates by a Schiff-base mechanism.

**Evidence type.** Homology-based for KT2440 (UniProt evidence level 3; annotation score 3.0), supported by:
- **Substrate-specific signature:** **IPR006323 (PhnX family)** — a phosphonatase-specific TIGRFAM, not merely the broad HAD fold.
- **Conserved catalytic residues:** the KT2440 sequence retains the HAD motif-I aspartate (Asp near residue 15, "DWAGT" motif), the **Schiff-base-forming Lys56** and the **catalytic His59** ("WDHI" motif). These correspond to the experimentally validated *Bacillus cereus* / *Salmonella typhimurium* phosphonatase catalytic pair (Lys53/His56) and the conserved active-site aspartate that mediates phosphoryl transfer.
- **Single-copy:** K05306 and EC 3.11.1.1 each map to exactly one KT2440 gene (PP_2208).
- **Genomic context:** immediately downstream of phnW in a tight operon.

**Curation caveats.** As for PhnW, direct biochemistry is at the *P. putida* species level, not the KT2440 strain. However, the combination of the phosphonatase-specific TIGRFAM, fully conserved Schiff-base catalytic machinery, and operon linkage to phnW makes the assignment high-confidence.

### 4.3 Genomic architecture — the phnWX operon and PP_2210 (AepR)

KEGG genomic coordinates place both genes on the **minus strand**: `phnW = PP_2209` complement(2,515,421..2,516,527) and `phnX = PP_2208` complement(2,514,559..2,515,386), separated by only a **34-bp intergenic region** and transcribed in the biochemical order phnW→phnX. Immediately upstream, on the **plus strand**, lies **PP_2210** (2,516,640..2,517,503), a **LysR-family transcriptional regulator** in the canonical divergent orientation relative to its target operon. This architecture — a divergent LysR regulator controlling an adjacent catabolic operon — is the textbook layout for a substrate-inducible degradation system and matches the experimentally characterized **AepR** regulator of *P. putida* BIRD-1.

### 4.4 Species-level functional support (transfer to KT2440)

Two *P. putida* strains provide direct enzymatic/physiological evidence that the PhnWX route is functional and AEP-inducible:

- **Strain NG2** [PMID: 9841125]: contains both **AEP:pyruvate aminotransferase (PhnW)** and **phosphonoacetaldehyde hydrolase/phosphonatase (PhnX)** activities, inducible by AEP and independent of phosphate status (substrate-inducible, pho-independent).
- **Strain BIRD-1** [PMID: 35229442]: uses 2AEP as a source of C, N, or P via the **PhnWX transaminase-phosphonatase system**, dual-regulated by global stress regulators (CbrAB/NtrBC/PhoBR) plus a **substrate-specific LysR regulator AepR** upstream of phnWX.

**Transfer strength:** Strong at the species level. Both strains are *P. putida*, both possess the identical two-enzyme system in the same genomic arrangement, and KT2440's genes are orthologous single-copy loci with substrate-specific signatures. The transfer is therefore rated **strong** for functional presence, though **KT2440-strain-specific biochemistry remains to be demonstrated**.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

**No over-annotation detected.** The over-propagation safety check (KEGG EC→gene links in KT2440) found that EC 3.11.1.1 maps to exactly one gene (PP_2208) and EC 2.6.1.37 maps to exactly one gene (PP_2209). No additional genome genes carry the module ECs, and the KO scans (K05306, K03430) are likewise single-copy. There is thus **no paralog ambiguity** and **no evidence that the module ECs have been over-propagated** to unrelated loci.

**C–P lyase route absent (correctly excluded).** The broad-substrate C–P lyase system is entirely missing: K06163/phnG, K06164/phnH, K06165/phnI, K06166/phnJ, and K05781/phnK all return no KT2440 genes. This confirms that KT2440 relies on the specific PhnWX route and that the module boundary — excluding C-P lyase — is correct for this organism. The alternative route should be marked **not_expected_in_target_taxon**.

**Transporter gap (out of module scope).** Dedicated AEP ABC-transporter components (phnSTUV: K09994, K11081–K11084) are absent from KT2440. A **general phosphonate ABC transporter is present** — phnC (PP_0825, K02041) and phnD (PP_0826/PP_0827, K02042) — but this is a broad-specificity uptake system, not a dedicated AEP transporter and not part of the two-enzyme catabolic module. How AEP enters the KT2440 cell is therefore a genuine open question, but it is **outside the scope** of the PhnW/PhnX module and should be logged as a separate transport gap rather than a module failure.

**Regulator not in the candidate list.** PP_2210 (candidate AepR) is functionally relevant context but was not among the two supplied candidate genes. It is not a catalytic step of the module, so it need not be a module member, but it is worth recording as the likely substrate-specific regulator.

**Residual uncertainty.** All KT2440-level conclusions are homology- and genomic-context-based (UniProt evidence level 3). There is no KT2440-strain biochemical or genetic knockout study confirming the AEP growth phenotype or enzyme activities; the direct evidence is at the species level (NG2, BIRD-1).

---

## 6. Module and GO-Curation Recommendations

| Module element | Recommended status | Rationale |
|----------------|--------------------|-----------|
| Step 1 — PhnW AEP transamination (PP_2209) | **covered** | Single-copy K03430/EC 2.6.1.37; substrate-specific TIGRFAM IPR012703; operon context; species-level activity evidence |
| Step 2 — PhnX phosphonoacetaldehyde hydrolysis (PP_2208) | **covered** | Single-copy K05306/EC 3.11.1.1; PhnX-family TIGRFAM IPR006323; conserved Schiff-base Lys56/His59 + HAD-Asp; operon context |
| C–P lyase alternative route | **not_expected_in_target_taxon** | phnGHIJK/phnK all absent from genome |
| Dedicated AEP transporter | **gap (out of module scope)** | phnSTUV absent; only general phosphonate ABC transporter present |
| Module boundaries | **no revision needed** | Two-enzyme scope correctly excludes C-P lyase and non-PAA phosphonatases |

- **Module satisfiability:** The module is **fully satisfiable** in KT2440. Both catalytic steps are covered by high-confidence, single-copy, substrate-specifically annotated genes.
- **Module boundaries:** Correct as written. The exclusion of C-P lyase systems and non-phosphonoacetaldehyde phosphonatases is appropriate; KT2440 confirms this by lacking the C-P lyase genes entirely.
- **GO terms:** No new GO term requests appear necessary. The relevant activities already have precise GO/EC mappings: 2-aminoethylphosphonate—pyruvate transaminase activity (EC 2.6.1.37) and phosphonoacetaldehyde hydrolase activity (EC 3.11.1.1). Existing annotations should be retained with evidence codes reflecting homology (ISS/IEA) rather than direct assay (IDA) for KT2440.
- **New module documents:** None required for the two-enzyme module. Optionally, a separate note could track the AEP-uptake transport gap.

---

## 7. Genes to Promote to Full Review

Both catalytic genes should be **promoted to full `fetch-gene` review** to formally consolidate the direct catalytic-residue and genomic-context evidence:

1. **phnX / PP_2208 (Q88KT1)** — confirm the phosphonatase-specific TIGRFAM (IPR006323), the conserved Schiff-base Lys56 / catalytic His59 / HAD motif-I Asp, Mg²⁺ dependence, and single-copy status. Highest-confidence module member.
2. **phnW / PP_2209 (Q88KT0)** — confirm the AEP:pyruvate transaminase-specific TIGRFAM (IPR012703/TIGR02326), class-V PLP fold, and single-copy status.

**Optional context promotion:** **PP_2210** (candidate AepR, LysR-family regulator) could be reviewed to formalize its role as the substrate-specific regulator of the phnWX operon, by analogy to *P. putida* BIRD-1 AepR — though it is regulatory context, not a catalytic module step.

---

## 8. Mechanistic Model and Interpretation

The KT2440 module is a compact, self-contained catabolic cassette. PhnW performs the chemically enabling first step: AEP's amino group is chemically inert to direct C–P cleavage, so PhnW first transaminates it (using pyruvate as the amino acceptor and generating L-alanine) to unmask the aldehyde and produce **phosphonoacetaldehyde**. This aldehyde is precisely the substrate that PhnX requires: PhnX forms a **Schiff base** between its active-site lysine (Lys56 in KT2440, homologous to Lys53 of the *B. cereus* enzyme) and the aldehyde carbonyl, which electronically activates the adjacent C–P bond for hydrolytic cleavage, releasing acetaldehyde and inorganic phosphate. The catalytic His59 and the HAD-superfamily aspartate complete the proton-transfer and phosphoryl-handling machinery. The strict substrate–product coupling (PhnW's product is PhnX's only substrate) explains why the two genes are almost always found together in a tight operon across bacteria, and KT2440 conforms to this pattern with a 34-bp intergenic gap and shared minus-strand orientation.

The divergent LysR regulator (PP_2210 / AepR) sits upstream and, by analogy to BIRD-1, provides substrate-specific induction: the operon is switched on when AEP is available, layered on top of global C/N/P starvation regulators. This regulatory logic is consistent with the NG2 observation that the enzymes are AEP-inducible and phosphate-independent, i.e., KT2440 likely uses AEP opportunistically as a carbon/nitrogen source, not only under phosphate limitation.

The absence of the C-P lyase system is mechanistically informative: KT2440 does not carry the broad-substrate radical machinery for cleaving unactivated phosphonates, so its phosphonate catabolism is channeled specifically through the aldehyde-activated PhnWX route. This is why the module boundary correctly excludes C-P lyase for this organism.

---

## 9. Evidence Base

| PMID | Title (abbrev.) | How it supports the review |
|------|-----------------|----------------------------|
| [PMID: 33830741](https://pubmed.ncbi.nlm.nih.gov/33830741/) | *Discovery of a New, Recurrent Enzyme in Bacterial Phosphonate Degradation* | States the exact two-step route: "the aminotransferase PhnW initially converts AEP into phosphonoacetaldehyde (PAA), which is then cleaved by the hydrolase PhnX to yield acetaldehyde and phosphate" — defines the module PP_2209/PP_2208 encode |
| [PMID: 35229442](https://pubmed.ncbi.nlm.nih.gov/35229442/) | *2-Aminoethylphosphonate utilization in Pseudomonas putida BIRD-1 is controlled by multiple master regulators* | Direct *P. putida* evidence: 2AEP used as C/N/P source via PhnWX; identifies "a LysR-type regulator, termed AepR, upstream of the 2AEP transaminase-phosphonatase system (PhnWX)" — matches divergent PP_2210 |
| [PMID: 9841125](https://pubmed.ncbi.nlm.nih.gov/9841125/) | *Phosphate starvation-independent 2-aminoethylphosphonic acid biodegradation in Pseudomonas putida NG2* | Direct *P. putida* strain evidence: both AEP:pyruvate aminotransferase and phosphonoacetaldehyde hydrolase (phosphonatase) activities present and AEP-inducible |
| [PMID: 10956028](https://pubmed.ncbi.nlm.nih.gov/10956028/) | *Crystal structure of Bacillus cereus phosphonoacetaldehyde hydrolase* | Defines the catalytic Schiff-base Lys53 and Mg(II)-binding core conserved in KT2440 PhnX (Lys56/His59, Mg²⁺) |
| [PMID: 14670958](https://pubmed.ncbi.nlm.nih.gov/14670958/) | *X-ray/mutagenesis of Schiff-base formation in phosphonatase* | Establishes His-56 and Met-49 as catalytic residues in the Schiff-base mechanism; supports assignment of conserved KT2440 PhnX catalytic residues |
| [PMID: 9649311](https://pubmed.ncbi.nlm.nih.gov/9649311/) | *Mechanism of phosphonoacetaldehyde hydrolase from gene sequence & mutagenesis* | Places phosphonatase in a novel HAD-family with a conserved active-site aspartate in covalent catalysis; underpins the HAD-motif-I Asp signature in KT2440 PhnX |
| [PMID: 8605214](https://pubmed.ncbi.nlm.nih.gov/8605214/) | *Phosphoenolpyruvate mutase catalysis* | Context for phosphonate C-P chemistry; phosphonoacetaldehyde hydrolase used as a coupling enzyme, illustrating PhnX substrate specificity |

**Direct vs. inferred:**
- **Direct experimental (for the enzymes/mechanism):** the phosphonatase Schiff-base mechanism and catalytic residues (PMIDs 10956028, 14670958, 9649311) are direct biochemistry, but on *B. cereus*/*S. typhimurium* enzymes, transferred to KT2440 by sequence conservation.
- **Direct at *P. putida* species level:** PhnW/PhnX enzyme activities and AEP induction (NG2, PMID 9841125) and PhnWX-mediated 2AEP utilization + AepR regulation (BIRD-1, PMID 35229442).
- **Inferred for KT2440 strain:** all gene-level calls are homology- and genomic-context-based (UniProt evidence level 3; KEGG orthology; InterPro/TIGRFAM signatures; operon coordinates). No KT2440-strain knockout or enzyme assay exists.

---

## 10. Limitations and Knowledge Gaps

1. **No KT2440-strain-specific biochemistry.** All conclusions for KT2440 rest on homology, KEGG orthology, InterPro/TIGRFAM signatures, and genomic context. Direct enzyme assays and growth phenotypes are available only for other *P. putida* strains (NG2, BIRD-1). Transfer is strong but not experimentally confirmed in KT2440.
2. **AEP uptake mechanism unresolved.** KT2440 lacks recognizable dedicated AEP transporter genes (phnSTUV). Whether the general phosphonate ABC transporter (phnCDE, PP_0825–PP_0827) or another system imports AEP is unknown. This transport gap is outside the two-enzyme module but affects whether the pathway is physiologically usable.
3. **Regulator assignment provisional.** PP_2210 is a strong candidate AepR by homology and divergent position, but its direct regulation of phnWX in KT2440 has not been demonstrated experimentally.
4. **Downstream fate of acetaldehyde/alanine not analyzed.** The module ends at acetaldehyde + Pi + L-alanine; integration into central metabolism was not investigated here.

---

## 11. Proposed Follow-up Experiments / Actions

**Curation actions (immediate):**
- Mark Step 1 (PhnW, PP_2209) and Step 2 (PhnX, PP_2208) as **COVERED**.
- Mark the C-P lyase alternative as **not_expected_in_target_taxon**.
- Log the dedicated AEP transporter as a **gap outside module scope**.
- Promote **PP_2208** and **PP_2209** to full `fetch-gene` review; optionally review **PP_2210** as regulatory context.
- Retain existing GO/EC annotations with homology-appropriate evidence codes; no new GO terms required.

**Experimental (to resolve KT2440-level gaps):**
1. **Growth phenotyping:** test KT2440 growth on AEP as sole C, N, and/or P source; construct ΔphnW and ΔphnX knockouts to confirm each gene is required.
2. **Enzyme assays:** heterologously express PP_2208 and PP_2209 and measure phosphonatase (EC 3.11.1.1) and AEP:pyruvate transaminase (EC 2.6.1.37) activities directly.
3. **Transporter identification:** transcriptomics/transposon screens under AEP growth to identify the AEP uptake system; test whether phnCDE (PP_0825–0827) contributes.
4. **Regulator validation:** ΔPP_2210 mutant + reporter assays to confirm AepR-dependent, AEP-inducible expression of phnWX.
5. **Catalytic-residue confirmation:** site-directed mutagenesis of KT2440 PhnX Lys56/His59 to verify the Schiff-base mechanism inferred from homology.

---

### Bottom line for curators

The PhnW/PhnX 2-aminoethylphosphonate degradation module is **fully satisfiable and COVERED** in *P. putida* KT2440 by two clean, single-copy, substrate-specifically annotated genes (PP_2209 = phnW; PP_2208 = phnX) arranged in a tight operon with a divergent LysR regulator. Module boundaries are correct, no over-annotation is present, the C-P lyase alternative is correctly excluded (absent from the genome), and the only genuine gap — a dedicated AEP transporter — lies outside the two-enzyme module scope.


## Artifacts

- [OpenScientist final report](PSEPK__phosphonoacetaldehyde_degradation__ppu00440-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__phosphonoacetaldehyde_degradation__ppu00440-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:9841125
2. PMID:35229442
3. PMID:33830741
4. PMID:10956028
5. PMID:14670958
6. PMID:9649311
7. PMID:8605214