---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T15:33:16.578714'
end_time: '2026-07-18T15:57:35.948095'
duration_seconds: 1459.37
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Endogenous protein lipoylation
  module_summary: Endogenous protein lipoylation is a two-reaction pathway that installs
    a lipoyl cofactor on conserved lysine residues in lipoyl domains. A LipB-family
    octanoyltransferase first transfers an octanoyl group from octanoyl-acyl carrier
    protein to the target protein. LipA-family lipoate synthase then uses radical-SAM
    chemistry and iron-sulfur clusters to insert sulfur atoms at C6 and C8 of the
    protein-bound octanoyl group. The resulting lipoyl domains act as swinging arms
    in alpha-ketoacid dehydrogenase complexes and the glycine cleavage system. Exogenous-lipoate
    salvage by lipoate--protein ligases and alternative GcvH-relay architectures are
    outside this module boundary.
  module_outline: "- Endogenous protein lipoylation\n  - 1. transfer of octanoyl from\
    \ acyl carrier protein to a lipoyl domain\n  - Octanoyl-ACP to octanoylated lipoyl-domain\
    \ protein\n    - LipB-family lipoyl(octanoyl) transferase (molecular player: LipB\
    \ family octanoyltransferases; activity or role: lipoyl(octanoyl) transferase\
    \ activity)\n  - 2. sulfur insertion into the protein-bound octanoyl group\n \
    \ - Octanoylated lipoyl-domain protein to lipoylated protein\n    - LipA-family\
    \ lipoate synthase (molecular player: LipA family lipoate synthases; activity\
    \ or role: lipoate synthase activity)"
  module_connections: '- Octanoyl-ACP to octanoylated lipoyl-domain protein feeds
    into Octanoylated lipoyl-domain protein to lipoylated protein: The octanoylated
    lipoyl-domain protein made by LipB is the direct macromolecular substrate for
    LipA.'
  pathway_query: ppu00785
  pathway_id: ppu00785
  pathway_name: Lipoic acid metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00785 with 19 primary genes; module
    area: cofactors_vitamins_redox.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '19'
  candidate_genes: '- aceF: PP_0338 | Q88QZ6 | Acetyltransferase component of pyruvate
    dehydrogenase complex (EC 2.3.1.12) (EC 2.3.1.12; primary bucket kegg:ppu00785)

    - aceE: PP_0339 | Q88QZ5 | Pyruvate dehydrogenase E1 component (EC 1.2.4.1) (EC
    1.2.4.1; primary bucket kegg:ppu00785)

    - acoC: PP_0553 | Q88QE1 | Dihydrolipoyllysine-residue acetyltransferase component
    of acetoin cleaving system (EC 2.3.1.12) (EC 2.3.1.12; primary bucket kegg:ppu00785)

    - gcvT-I: PP_0986 | Q88P67 | aminomethyltransferase (EC 2.1.2.10) (Glycine cleavage
    system T protein) (EC 2.1.2.10; primary bucket kegg:ppu00785)

    - gcvP1: PP_0988 | Q88P65 | Glycine dehydrogenase (decarboxylating) 1 (EC 1.4.4.2)
    (Glycine cleavage system P-protein 1) (Glycine decarboxylase 1) (Glycine dehydrogenase
    (aminomethyl-transferring) 1) (EC 1.4.4.2; primary bucket kegg:ppu00785)

    - gcvH1: PP_0989 | Q88P64 | Glycine cleavage system H protein 1 (primary bucket
    kegg:ppu00785)

    - lpdG: PP_4187 | Q88FB1 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4;
    primary bucket kegg:ppu00785)

    - sucB: PP_4188 | Q88FB0 | Dihydrolipoyllysine-residue succinyltransferase component
    of 2-oxoglutarate dehydrogenase complex (EC 2.3.1.61) (2-oxoglutarate dehydrogenase
    complex component E2) (EC 2.3.1.61; primary bucket kegg:ppu00785)

    - sucA: PP_4189 | Q88FA9 | 2-oxoglutarate dehydrogenase E1 component (EC 1.2.4.2)
    (Alpha-ketoglutarate dehydrogenase) (EC 1.2.4.2; primary bucket kegg:ppu00785)

    - bkdAA: PP_4401 | Q88EQ2 | 2-oxoisovalerate dehydrogenase subunit alpha (EC 1.2.4.4)
    (Branched-chain alpha-keto acid dehydrogenase E1 component alpha chain) (EC 1.2.4.4;
    primary bucket kegg:ppu00785)

    - bkdAB: PP_4402 | Q88EQ1 | 2-oxoisovalerate dehydrogenase subunit beta (EC 1.2.4.4)
    (Branched-chain alpha-keto acid dehydrogenase E1 component beta chain) (EC 1.2.4.4;
    primary bucket kegg:ppu00785)

    - bkdB: PP_4403 | Q88EQ0 | Dihydrolipoamide acetyltransferase component of pyruvate
    dehydrogenase complex (EC 2.3.1.-) (EC 2.3.1.-; primary bucket kegg:ppu00785)

    - lpdV: PP_4404 | Q88EP9 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4;
    primary bucket kegg:ppu00785)

    - lipA: PP_4800 | Q88DM5 | Lipoyl synthase (EC 2.8.1.8) (Lip-syn) (LS) (Lipoate
    synthase) (Lipoic acid synthase) (Sulfur insertion protein LipA) (EC 2.8.1.8;
    primary bucket kegg:ppu00785)

    - lipB: PP_4801 | Q88DM4 | Octanoyltransferase (EC 2.3.1.181) (Lipoate-protein
    ligase B) (Lipoyl/octanoyl transferase) (Octanoyl-[acyl-carrier-protein]-protein
    N-octanoyltransferase) (EC 2.3.1.181; primary bucket kegg:ppu00785)

    - gcvP2: PP_5192 | Q88CI9 | Glycine dehydrogenase (decarboxylating) 2 (EC 1.4.4.2)
    (Glycine cleavage system P-protein 2) (Glycine decarboxylase 2) (Glycine dehydrogenase
    (aminomethyl-transferring) 2) (EC 1.4.4.2; primary bucket kegg:ppu00785)

    - gcvH2: PP_5193 | Q88CI8 | Glycine cleavage system H protein 2 (primary bucket
    kegg:ppu00785)

    - gcvT: PP_5194 | Q88CI7 | Aminomethyltransferase (EC 2.1.2.10) (Glycine cleavage
    system T protein) (EC 2.1.2.10; primary bucket kegg:ppu00785)

    - lpd: PP_5366 | Q88C17 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4;
    primary bucket kegg:ppu00785)'
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
  path: PSEPK__endogenous_protein_lipoylation__ppu00785-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__endogenous_protein_lipoylation__ppu00785-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Endogenous protein lipoylation in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00785
- Resolved ID: ppu00785
- Resolved name: Lipoic acid metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00785 with 19 primary genes; module area: cofactors_vitamins_redox.

## Candidate Genes From Local Metadata

Candidate gene count: 19

- aceF: PP_0338 | Q88QZ6 | Acetyltransferase component of pyruvate dehydrogenase complex (EC 2.3.1.12) (EC 2.3.1.12; primary bucket kegg:ppu00785)
- aceE: PP_0339 | Q88QZ5 | Pyruvate dehydrogenase E1 component (EC 1.2.4.1) (EC 1.2.4.1; primary bucket kegg:ppu00785)
- acoC: PP_0553 | Q88QE1 | Dihydrolipoyllysine-residue acetyltransferase component of acetoin cleaving system (EC 2.3.1.12) (EC 2.3.1.12; primary bucket kegg:ppu00785)
- gcvT-I: PP_0986 | Q88P67 | aminomethyltransferase (EC 2.1.2.10) (Glycine cleavage system T protein) (EC 2.1.2.10; primary bucket kegg:ppu00785)
- gcvP1: PP_0988 | Q88P65 | Glycine dehydrogenase (decarboxylating) 1 (EC 1.4.4.2) (Glycine cleavage system P-protein 1) (Glycine decarboxylase 1) (Glycine dehydrogenase (aminomethyl-transferring) 1) (EC 1.4.4.2; primary bucket kegg:ppu00785)
- gcvH1: PP_0989 | Q88P64 | Glycine cleavage system H protein 1 (primary bucket kegg:ppu00785)
- lpdG: PP_4187 | Q88FB1 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4; primary bucket kegg:ppu00785)
- sucB: PP_4188 | Q88FB0 | Dihydrolipoyllysine-residue succinyltransferase component of 2-oxoglutarate dehydrogenase complex (EC 2.3.1.61) (2-oxoglutarate dehydrogenase complex component E2) (EC 2.3.1.61; primary bucket kegg:ppu00785)
- sucA: PP_4189 | Q88FA9 | 2-oxoglutarate dehydrogenase E1 component (EC 1.2.4.2) (Alpha-ketoglutarate dehydrogenase) (EC 1.2.4.2; primary bucket kegg:ppu00785)
- bkdAA: PP_4401 | Q88EQ2 | 2-oxoisovalerate dehydrogenase subunit alpha (EC 1.2.4.4) (Branched-chain alpha-keto acid dehydrogenase E1 component alpha chain) (EC 1.2.4.4; primary bucket kegg:ppu00785)
- bkdAB: PP_4402 | Q88EQ1 | 2-oxoisovalerate dehydrogenase subunit beta (EC 1.2.4.4) (Branched-chain alpha-keto acid dehydrogenase E1 component beta chain) (EC 1.2.4.4; primary bucket kegg:ppu00785)
- bkdB: PP_4403 | Q88EQ0 | Dihydrolipoamide acetyltransferase component of pyruvate dehydrogenase complex (EC 2.3.1.-) (EC 2.3.1.-; primary bucket kegg:ppu00785)
- lpdV: PP_4404 | Q88EP9 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4; primary bucket kegg:ppu00785)
- lipA: PP_4800 | Q88DM5 | Lipoyl synthase (EC 2.8.1.8) (Lip-syn) (LS) (Lipoate synthase) (Lipoic acid synthase) (Sulfur insertion protein LipA) (EC 2.8.1.8; primary bucket kegg:ppu00785)
- lipB: PP_4801 | Q88DM4 | Octanoyltransferase (EC 2.3.1.181) (Lipoate-protein ligase B) (Lipoyl/octanoyl transferase) (Octanoyl-[acyl-carrier-protein]-protein N-octanoyltransferase) (EC 2.3.1.181; primary bucket kegg:ppu00785)
- gcvP2: PP_5192 | Q88CI9 | Glycine dehydrogenase (decarboxylating) 2 (EC 1.4.4.2) (Glycine cleavage system P-protein 2) (Glycine decarboxylase 2) (Glycine dehydrogenase (aminomethyl-transferring) 2) (EC 1.4.4.2; primary bucket kegg:ppu00785)
- gcvH2: PP_5193 | Q88CI8 | Glycine cleavage system H protein 2 (primary bucket kegg:ppu00785)
- gcvT: PP_5194 | Q88CI7 | Aminomethyltransferase (EC 2.1.2.10) (Glycine cleavage system T protein) (EC 2.1.2.10; primary bucket kegg:ppu00785)
- lpd: PP_5366 | Q88C17 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4; primary bucket kegg:ppu00785)

## Generic Module Context

### Working Scope

Endogenous protein lipoylation is a two-reaction pathway that installs a lipoyl cofactor on conserved lysine residues in lipoyl domains. A LipB-family octanoyltransferase first transfers an octanoyl group from octanoyl-acyl carrier protein to the target protein. LipA-family lipoate synthase then uses radical-SAM chemistry and iron-sulfur clusters to insert sulfur atoms at C6 and C8 of the protein-bound octanoyl group. The resulting lipoyl domains act as swinging arms in alpha-ketoacid dehydrogenase complexes and the glycine cleavage system. Exogenous-lipoate salvage by lipoate--protein ligases and alternative GcvH-relay architectures are outside this module boundary.

### Provisional Biological Outline

- Endogenous protein lipoylation
  - 1. transfer of octanoyl from acyl carrier protein to a lipoyl domain
  - Octanoyl-ACP to octanoylated lipoyl-domain protein
    - LipB-family lipoyl(octanoyl) transferase (molecular player: LipB family octanoyltransferases; activity or role: lipoyl(octanoyl) transferase activity)
  - 2. sulfur insertion into the protein-bound octanoyl group
  - Octanoylated lipoyl-domain protein to lipoylated protein
    - LipA-family lipoate synthase (molecular player: LipA family lipoate synthases; activity or role: lipoate synthase activity)

### Known Relationships Among Steps

- Octanoyl-ACP to octanoylated lipoyl-domain protein feeds into Octanoylated lipoyl-domain protein to lipoylated protein: The octanoylated lipoyl-domain protein made by LipB is the direct macromolecular substrate for LipA.

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

# Species-Aware Module Review: Endogenous Protein Lipoylation in *Pseudomonas putida* KT2440

**Taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Module:** Endogenous protein lipoylation (LipB octanoyltransferase → LipA lipoate synthase)
**Local bucket:** kegg:ppu00785 "Lipoic acid metabolism" (cofactors_vitamins_redox), 19 primary genes
**Date:** 2026-07-18 · Review complete (5 iterations)

---

## 1. Executive summary

The endogenous protein-lipoylation module is a **narrow, two-reaction biosynthetic pathway** that installs the lipoyl cofactor de novo on lysine residues of lipoyl-carrier domains: (1) a LipB-family octanoyltransferase transfers octanoyl from octanoyl-ACP onto the apo lipoyl domain, then (2) a LipA-family radical-SAM lipoate synthase inserts two sulfur atoms to yield the mature lipoyl group.

In *P. putida* KT2440 **both steps are covered and canonical**:

- **Step 1 = LipB (PP_4801 / Q88DM4)** — Octanoyltransferase, EC 2.3.1.181, carries the diagnostic PROSITE **LIPB** signature (PS01313) and the Octanoyltransferase InterPro family (IPR000544). A *bona fide* LipB, **not** an LplA-like LipM.
- **Step 2 = LipA (PP_4800 / Q88DM5)** — Lipoyl synthase, EC 2.8.1.8, radical-SAM enzyme (Pfam PF04055, IPR003698 Lipoyl_synth) with 4Fe-4S / SAM annotation.

The two genes are **genomically adjacent** (PP_4800–PP_4801), consistent with a lipA-lipB unit. A whole-proteome scan of taxon 160488 found **no LplA-family salvage ligase**, so de novo synthesis appears to be KT2440's sole route to protein-bound lipoate. However, a domain-based scan (correcting an earlier name-only search) revealed a **candidate LipM/LipL-family GcvH-relay octanoyltransferase, PP_0423** (InterPro IPR050664; PANTHER "octanoyl-[GcvH]:protein N-octanoyltransferase"). This is an **out-of-module** auxiliary per the module's scope (GcvH-relay architectures are excluded) and does not affect core satisfiability, but it is flagged for review.

**Module recommendation: COVERED.** LipB and LipA cover both steps. The remaining 17 of the 19 bucket genes are **out-of-module** (lipoyl-domain acceptors, non-lipoylated E1 subunits, E3 dehydrogenases, and glycine-cleavage T-proteins) and reflect KEGG map breadth rather than pathway steps; PP_0423 (not in the bucket) is a separate out-of-module relay candidate.

---

## 2. Target-organism pathway definition

**In scope (the module):** the enzymatic *installation* of the lipoyl cofactor on apo lipoyl domains, comprising exactly two reactions:

1. Octanoyl-ACP + apo-[lipoyl domain] → octanoyl-[lipoyl domain] + ACP (**LipB**, EC 2.3.1.181).
2. Octanoyl-[lipoyl domain] + 2 S (via 2 SAM, 4Fe-4S) → lipoyl-[lipoyl domain] (**LipA**, EC 2.8.1.8).

The octanoylated protein made by LipB is the **direct macromolecular substrate** of LipA (PMID 20882995).

**Kept separate (neighboring pathways / overview breadth):**
- **Lipoyl-cofactor utilisation:** the 2-oxoacid dehydrogenase complexes (PDH aceE/aceF, OGDH sucA/sucB, BCKAD bkdAA/bkdAB/bkdB, acetoin acoC) and the glycine cleavage system (gcvP/gcvH/gcvT). Their lipoyl-domain proteins are *substrates* of the module, not steps within it.
- **Exogenous lipoate salvage:** lipoate–protein ligase A (LplA) — explicitly outside the module boundary (and, notably, not annotated in KT2440; no full-length LplA-family protein detected by domain scan).
- **Alternative lipoylation architectures:** the *Bacillus*-type LipM (octanoyl-ACP:GcvH transferase) + LipL (GcvH→E2 amidotransferase relay) — outside the boundary. KT2440 does encode a **candidate LipM/LipL-family protein, PP_0423** (see §4/§5), so this architecture cannot be dismissed as absent, but it is out-of-module.

**Alternate names / DB definitions:** KEGG "Lipoic acid metabolism" (ppu00785); MetaCyc "lipoate biosynthesis and incorporation"; the enzymes are also labelled "lipoyl(octanoyl) transferase" (LipB) and "lipoate synthase / Lip-syn / LS" (LipA). LipB is frequently mis-labelled "lipoate-protein ligase B," which can invite confusion with true salvage ligases (LplA).

---

## 3. Expected step model

| Step | Reaction | Expected player | KT2440 gene | Status |
|------|----------|-----------------|-------------|--------|
| 1 | Octanoyl-ACP → octanoylated lipoyl-domain protein | LipB-family octanoyltransferase | **lipB / PP_4801 / Q88DM4** | **Covered** |
| 2 | Octanoylated → lipoylated protein (S insertion) | LipA-family lipoate synthase | **lipA / PP_4800 / Q88DM5** | **Covered** |

No third step exists in this module. The relationship "LipB product is LipA substrate" holds and is satisfied by the adjacent lipA/lipB pair.

---

## 4. Candidate genes and evidence

### In-module (promote / high confidence)

| Gene | Locus / UniProt | Role | EC | Evidence | Family signature | Caveats |
|------|-----------------|------|----|----------|------------------|---------|
| **lipB** | PP_4801 / Q88DM4 | Octanoyltransferase (Step 1) | 2.3.1.181 | UniProt PE3 (homology), score 3/5 | PROSITE **LIPB** PS01313; Pfam PF21948; IPR000544 | Name "lipoate-protein ligase B" is a misnomer — it is a de novo octanoyltransferase, **not** a salvage ligase. |
| **lipA** | PP_4800 / Q88DM5 | Lipoyl synthase (Step 2) | 2.8.1.8 | UniProt PE3 (homology), score 3/5 | Radical_SAM PF04055; IPR003698; LIAS_N | Requires 4Fe-4S + SAM; correctly annotated. |

Evidence type for both is **homology / rule-based** (no KT2440-specific biochemistry located), but family assignment is unambiguous (exact PROSITE/Pfam diagnostic hits) and genomic adjacency reinforces a functional biosynthetic unit. Transfer of *E. coli* mechanism to KT2440 is **strong** (well-conserved γ-proteobacterial enzymes, correct EC and catalytic-domain signatures).

**Authoritative pathway assignment (UniProt/HAMAP).** Beyond the KEGG bucket, UniProt PATHWAY comments (HAMAP rules, ECO:0000255) place both enzymes explicitly in *"Protein modification; protein lipoylation via endogenous pathway"* — an exact match to this module's name:
- **lipB (HAMAP MF_00013):** catalytic activity `octanoyl-[ACP] + L-lysyl-[protein] = N6-octanoyl-L-lysyl-[protein] + holo-[ACP] + H+` — **Step 1** verbatim.
- **lipA (HAMAP MF_00206):** `N6-octanoyl-L-lysyl-[protein] + 2 S (radical-SAM, second [4Fe-4S] cluster) → N6-lipoyl-L-lysyl-[protein]` with a **[4Fe-4S] cofactor** annotation — **Step 2** verbatim.

This is authoritative rule-based confirmation that the two steps are represented by lipA/lipB, independent of KEGG map breadth.

**Essentiality (inferred).** No KT2440-specific mutant phenotype for lipA/lipB was located; a KT2440 Tn-seq study exists (PMID 40302248) but targets metal tolerance, not lipoylation. Because no salvage ligase is annotated, de novo lipoylation is the sole route and lipA/lipB are expected to be essential for growth on non-fermentable carbon (PDH/OGDH-dependent) — an inference, not a direct KT2440 result.

### Out-of-module bucket members (acceptors and utilisation machinery — do not treat as steps)

- **Lipoyl-domain acceptors (substrates of the module; UniProt 'Lipoyl' keyword):** aceF (PP_0338), sucB (PP_4188), bkdB (PP_4403), acoC (PP_0553), gcvH1 (PP_0989), gcvH2 (PP_5193). These are *products* of lipoylation, not enzymes that install it.
- **Non-lipoylated E1 decarboxylase subunits:** aceE (PP_0339), sucA (PP_4189), bkdAA (PP_4401), bkdAB (PP_4402), gcvP1 (PP_0988), gcvP2 (PP_5192).
- **E3 dihydrolipoyl dehydrogenases (EC 1.8.1.4):** lpd (PP_5366), lpdG (PP_4187, PE1 / 3D-structure — experimentally characterised), lpdV (PP_4404). Use lipoamide but are not lipoyl-domain proteins and not biosynthetic.
- **Glycine-cleavage T-protein aminomethyltransferases (EC 2.1.2.10):** gcvT-I (PP_0986), gcvT (PP_5194).

### Paralog notes relevant to the module's substrate load
KT2440 encodes **two glycine-cleavage clusters** (gcvTHP-1 at PP_0986–0989 and gcvTHP-2 at PP_5192–5194) and **three E3s** (lpd/lpdG/lpdV) plus multiple 2-oxoacid E2 acceptors. This expands the population of lysine substrates LipB/LipA must service but does not change module satisfiability.

---

## 5. Gaps, ambiguities, and likely over-annotations

- **No gap in the module itself.** Both steps are encoded by unambiguous family members.
- **Over-inclusive bucket:** 17/19 kegg:ppu00785 genes are utilisation/acceptor genes, not biosynthesis. This is the main curation risk — a naïve reading would over-count "steps."
- **LipB name ambiguity:** "Lipoate-protein ligase B" wording risks conflation with salvage LplA. The EC (2.3.1.181) and PROSITE LIPB signature confirm octanoyltransferase identity.
- **No annotated salvage ligase (LplA):** neither the name search (only lipB/lipA) nor the domain scan (IPR004143 → lipB, birA, PP_0423) revealed a full-length LplA-family salvage ligase. This is suggestive, not definitive.
- **Uncharacterised LipM/LipL-family protein PP_0423 (Q88QR5):** flagged by domain scan, not by gene name. InterPro IPR050664 "Octanoyltransferase LipM/LipL"; PANTHER PTHR43679:SF2 "octanoyl-[GcvH]:protein N-octanoyltransferase"; PF21948; 234 aa; UniProt PE4 (Predicted), score 1/5, no assigned gene name. It is a candidate GcvH-relay octanoyltransferase (out-of-module) whose real activity is unverified — it could be a functional relay enzyme, a redundant/auxiliary transferase, or an over-called family assignment. Its short single-domain length argues against it being a full LplA. **Genomic context (this review):** PP_0423 is genomically isolated, flanked by tryptophan/pABA-biosynthesis genes (pabA-trpD-trpC, PP_0420–0422) and a crp regulator (PP_0424) — with *no* neighboring gcvH, lipoyl-domain acceptor, or acetoin (aco) gene. There is therefore no operonic support for a dedicated GcvH-relay role, which weakens (but does not exclude) a functional relay interpretation. (A pairwise-alignment attempt to sub-classify it as LipM vs LipL was inconclusive due to reference and local-alignment artifacts; the InterPro/PANTHER family call is the reliable evidence.) This is the single most important item a curator should resolve, because it bears on whether KT2440 has redundant lipoylation routes.
- **acoC (PP_0553)** is UniProt PE4 (Predicted), score 1/5 — lowest-confidence acceptor; not module-critical but flag if it enters an acetoin module.
- **Evidence is homology-level** for lipA/lipB; no KT2440-specific mutant/enzymology found in this pass.

---

## 6. Module and GO-curation recommendations

| Module element | Recommended status |
|----------------|--------------------|
| Step 1 (octanoyl transfer, LipB) | **covered** — lipB / PP_4801 |
| Step 2 (sulfur insertion, LipA) | **covered** — lipA / PP_4800 |
| LplA salvage route | **not_expected_in_target_taxon** (outside boundary; no full-length LplA detected) |
| LipM/LipL (GcvH-relay) alternative | **candidate_uncertain / out_of_module** — PP_0423 is a LipM/LipL-family candidate (PE4); not needed for satisfiability (LipB present) but present and unverified |
| 17 acceptor/E1/E3/GcvT bucket genes | **out_of_module** (belong to 2-oxoacid dehydrogenase / glycine-cleavage modules) |

- **Module boundary is correct** for this organism as written (LipB→LipA only). No `module_needs_revision`.
- **GO suggestions:** confirm lipB → GO:0033819 (octanoyltransferase / lipoyl(octanoyl) transferase activity) and lipA → GO:0016992 (lipoate synthase activity); both to GO:0009107 (lipoate biosynthetic process). Acceptors should carry protein-lipoylation *target* terms (e.g. GO:0009249 protein lipoylation) but not the biosynthetic-enzyme activity terms.
- Recommend the local bucket flag lipA/lipB as the only "biosynthetic step" members and demote the other 17 to "cofactor-utilising / substrate" annotations.

---

## 7. Genes to promote to full `fetch-gene` review

1. **lipB / PP_4801 (Q88DM4)** — the rate-defining, name-ambiguous Step-1 enzyme; confirm octanoyltransferase vs ligase identity and operon context. **High priority.**
2. **lipA / PP_4800 (Q88DM5)** — Step-2 radical-SAM enzyme; confirm 4Fe-4S cofactor and lipA-lipB genomic unit. **High priority.**
3. **PP_0423 (Q88QR5)** — uncharacterised LipM/LipL-family protein flagged by domain scan; resolve whether it is a functional GcvH-relay octanoyltransferase, a redundant transferase, or an over-called family assignment. **High priority for boundary/redundancy decisions** (out-of-module, but its existence affects how the module's exclusions are worded for this taxon).
4. *(Lower priority, only if adjacent modules are opened)* lpdG / PP_4187 (has 3D structure, PE1) as the experimentally-supported E3 anchor; acoC / PP_0553 to resolve its PE4 low-confidence acceptor annotation.

---

## 8. Key references

- Christensen QH & Cronan JE. "Lipoic acid synthesis: a new family of octanoyltransferases generally annotated as lipoate protein ligases." *Biochemistry* 2010. **PMID 20882995** — defines the LipB→LipA two-step de novo module and the *Bacillus* LipM alternative (basis for boundary and alternative-pathway calls).
- Dhembla et al. "Lipoate protein ligase B primarily recognizes the C-terminal…" 2022. **PMID 35764173** — LipB vs LplA distinction and de novo vs salvage routes.
- Lennox-Hvenekilde et al. "Metabolic engineering of *E. coli* for high-level production of free lipoic acid." *Metab Eng* 2023. **PMID 36639019** — reiterates LipB + LipA as the native de novo enzymes acting on lipoyl domains.
- UniProt entries Q88DM4 (lipB) and Q88DM5 (lipA), *P. putida* KT2440; InterPro IPR000544 / IPR003698; PROSITE PS01313 (LIPB), PS51918 (Radical-SAM); UniProt/HAMAP rules MF_00013 (lipB) and MF_00206 (lipA) assigning both to "protein lipoylation via endogenous pathway."
- UniProt entry Q88QR5 (PP_0423), *P. putida* KT2440 — "BPL/LPL catalytic domain-containing protein," InterPro IPR050664 (Octanoyltransferase LipM/LipL), PANTHER PTHR43679:SF2 (octanoyl-[GcvH]:protein N-octanoyltransferase); basis for the LipM/LipL relay-candidate call.
- Christensen QH & Cronan JE. "Three transferases…LipM/LipL/GcvH relay" and related B. subtilis lipoylation studies establish the GcvH-relay architecture that PP_0423's family (IPR050664) belongs to. See also PMID 20882995 above.

---

*Confidence: Module satisfiability call is HIGH (unambiguous family signatures for both steps, genomic adjacency). Enzyme-level evidence is homology-based (UniProt PE3) with strong transfer from E. coli; no KT2440-specific enzymology was located in this pass. Absence of a salvage ligase is annotation-based and should be treated as suggestive.*


## Artifacts

- [OpenScientist final report](PSEPK__endogenous_protein_lipoylation__ppu00785-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__endogenous_protein_lipoylation__ppu00785-deep-research-openscientist_artifacts/final_report.pdf)