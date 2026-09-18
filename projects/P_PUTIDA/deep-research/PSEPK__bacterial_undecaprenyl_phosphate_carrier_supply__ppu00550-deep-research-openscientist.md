---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T02:02:23.330062'
end_time: '2026-09-01T02:12:58.773394'
duration_seconds: 635.44
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial undecaprenyl-phosphate carrier supply
  module_summary: A reusable bacterial module that supplies the C55 polyprenyl-phosphate
    lipid carrier used for cell-envelope glycan assembly. UppS first elongates farnesyl
    diphosphate with eight isopentenyl diphosphates to form undecaprenyl diphosphate.
    An integral-membrane undecaprenyl-diphosphatase then removes one phosphate to
    generate undecaprenyl phosphate. The carrier supports multiple pathways, including
    peptidoglycan and lipopolysaccharide synthesis; transfer of pathway-specific sugars
    onto the carrier and downstream glycan polymerization are outside this module.
  module_outline: "- Bacterial undecaprenyl-phosphate carrier supply\n  - 1. undecaprenyl-diphosphate\
    \ synthesis\n  - Undecaprenyl-diphosphate synthesis\n    - UppS undecaprenyl-diphosphate\
    \ synthase (molecular player: bacterial UppS undecaprenyl-diphosphate synthases;\
    \ activity or role: ditrans,polycis-undecaprenyl-diphosphate synthase activity)\n\
    \  - 2. undecaprenyl-phosphate formation\n  - Undecaprenyl-phosphate formation\n\
    \    - UppP/BacA undecaprenyl-diphosphatase (molecular player: UppP/BacA undecaprenyl-diphosphatases;\
    \ activity or role: undecaprenyl-diphosphatase activity)"
  module_connections: '- Undecaprenyl-diphosphate synthesis feeds into Undecaprenyl-phosphate
    formation: UppS-derived C55-PP is the substrate for carrier-activating dephosphorylation.'
  pathway_query: ppu00550
  pathway_id: ppu00550
  pathway_name: Peptidoglycan biosynthesis
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00550 with 10 primary genes; module
    area: lipid_cell_envelope_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '23'
  candidate_genes: '- pbpC: PP_0572 | Q88QC2 | peptidoglycan glycosyltransferase (EC
    2.4.99.28) (EC 2.4.99.28; primary bucket kegg:ppu00550)

    - murA: PP_0964 | Q88P88 | UDP-N-acetylglucosamine 1-carboxyvinyltransferase (EC
    2.5.1.7) (Enoylpyruvate transferase) (UDP-N-acetylglucosamine enolpyruvyl transferase)
    (EPT) (EC 2.5.1.7; primary bucket kegg:ppu00550)

    - ftsI: PP_1331 | Q88N82 | Peptidoglycan D,D-transpeptidase FtsI (EC 3.4.16.4)
    (Penicillin-binding protein 3) (PBP-3) (EC 3.4.16.4; primary bucket kegg:ppu01501)

    - murE: PP_1332 | Q88N81 | UDP-N-acetylmuramoyl-L-alanyl-D-glutamate--2,6-diaminopimelate
    ligase (EC 6.3.2.13) (Meso-A2pm-adding enzyme) (Meso-diaminopimelate-adding enzyme)
    (UDP-MurNAc-L-Ala-D-Glu:meso-diaminopimelate ligase) (UDP-MurNAc-tripeptide synthetase)
    (UDP-N-acetylmuramyl-tripeptide synthetase) (EC 6.3.2.13; primary bucket kegg:ppu00300)

    - murF: PP_1333 | Q88N80 | UDP-N-acetylmuramoyl-tripeptide--D-alanyl-D-alanine
    ligase (EC 6.3.2.10) (D-alanyl-D-alanine-adding enzyme) (EC 6.3.2.10; primary
    bucket kegg:ppu01502)

    - mraY: PP_1334 | Q88N79 | Phospho-N-acetylmuramoyl-pentapeptide-transferase (EC
    2.7.8.13) (UDP-MurNAc-pentapeptide phosphotransferase) (EC 2.7.8.13; primary bucket
    kegg:ppu01502)

    - murD: PP_1335 | Q88N78 | UDP-N-acetylmuramoylalanine--D-glutamate ligase (EC
    6.3.2.9) (D-glutamic acid-adding enzyme) (UDP-N-acetylmuramoyl-L-alanyl-D-glutamate
    synthetase) (EC 6.3.2.9; primary bucket kegg:ppu00470)

    - ftsW: PP_1336 | Q88N77 | Probable peptidoglycan glycosyltransferase FtsW (PGT)
    (EC 2.4.99.28) (Cell division protein FtsW) (Cell wall polymerase) (Peptidoglycan
    polymerase) (PG polymerase) (EC 2.4.99.28; primary bucket kegg:ppu00550)

    - murG: PP_1337 | Q88N76 | UDP-N-acetylglucosamine--N-acetylmuramyl-(pentapeptide)
    pyrophosphoryl-undecaprenol N-acetylglucosamine transferase (EC 2.4.1.227) (Undecaprenyl-PP-MurNAc-pentapeptide-UDPGlcNAc
    GlcNAc transferase) (EC 2.4.1.227; primary bucket kegg:ppu01502)

    - murC: PP_1338 | Q88N75 | UDP-N-acetylmuramate--L-alanine ligase (EC 6.3.2.8)
    (UDP-N-acetylmuramoyl-L-alanine synthetase) (EC 6.3.2.8; primary bucket kegg:ppu00550)

    - ddlB: PP_1339 | Q88N74 | D-alanine--D-alanine ligase B (EC 6.3.2.4) (D-Ala-D-Ala
    ligase B) (D-alanylalanine synthetase B) (EC 6.3.2.4; primary bucket kegg:ppu01502)

    - uppS: PP_1595 | Q88MH6 | Ditrans,polycis-undecaprenyl-diphosphate synthase ((2E,6E)-farnesyl-diphosphate
    specific) (EC 2.5.1.31) (Ditrans,polycis-undecaprenylcistransferase) (Undecaprenyl
    diphosphate synthase) (UDS) (Undecaprenyl pyrophosphate synthase) (UPP synthase)
    (EC 2.5.1.31; primary bucket kegg:ppu00900)

    - murB: PP_1904 | Q88LM5 | UDP-N-acetylenolpyruvoylglucosamine reductase (EC 1.3.1.98)
    (UDP-N-acetylmuramate dehydrogenase) (EC 1.3.1.98; primary bucket kegg:ppu00550)

    - dacB: PP_2098 | Q88L37 | D-alanyl-D-alanine carboxypeptidase (primary bucket
    kegg:ppu00550)

    - uppP: PP_2862 | Q88IY7 | Undecaprenyl-diphosphatase (EC 3.6.1.27) (Bacitracin
    resistance protein) (Undecaprenyl pyrophosphate phosphatase) (EC 3.6.1.27; primary
    bucket kegg:ppu00552)

    - mrdA-I: PP_3741 | Q88GI2 | Peptidoglycan D,D-transpeptidase MrdA (EC 3.4.16.4)
    (Penicillin-binding protein 2) (PBP-2) (EC 3.4.16.4; primary bucket kegg:ppu01501)

    - ddlA: PP_4346 | Q88EV6 | D-alanine--D-alanine ligase A (EC 6.3.2.4) (D-Ala-D-Ala
    ligase A) (D-alanylalanine synthetase A) (EC 6.3.2.4; primary bucket kegg:ppu01502)

    - mrcB: PP_4683 | Q88DY5 | Penicillin-binding protein 1B (PBP-1b) (PBP1b) (Murein
    polymerase) (primary bucket kegg:ppu00550)

    - dacA: PP_4803 | Q88DM2 | serine-type D-Ala-D-Ala carboxypeptidase (EC 3.4.16.4)
    (EC 3.4.16.4; primary bucket kegg:ppu00550)

    - mrdB: PP_4806 | Q88DL9 | Peptidoglycan glycosyltransferase MrdB (PGT) (EC 2.4.99.28)
    (Cell elongation protein RodA) (Cell wall polymerase) (Peptidoglycan polymerase)
    (PG polymerase) (EC 2.4.99.28; primary bucket kegg:ppu00550)

    - mrdA-II: PP_4807 | Q88DL8 | Peptidoglycan D,D-transpeptidase MrdA (EC 3.4.16.4)
    (Penicillin-binding protein 2) (PBP-2) (EC 3.4.16.4; primary bucket kegg:ppu01501)

    - mrcA: PP_5084 | Q88CU6 | Penicillin-binding protein 1A (EC 2.4.99.28) (EC 3.4.16.4)
    (EC 2.4.99.28; 3.4.16.4; primary bucket kegg:ppu01501)

    - mtgA: PP_5107 | Q88CS3 | Biosynthetic peptidoglycan transglycosylase (EC 2.4.99.28)
    (Glycan polymerase) (Peptidoglycan glycosyltransferase MtgA) (PGT) (EC 2.4.99.28;
    primary bucket kegg:ppu00550)'
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
  path: PSEPK__bacterial_undecaprenyl_phosphate_carrier_supply__ppu00550-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_undecaprenyl_phosphate_carrier_supply__ppu00550-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial undecaprenyl-phosphate carrier supply in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00550
- Resolved ID: ppu00550
- Resolved name: Peptidoglycan biosynthesis
- Source: KEGG

Resolved local bucket kegg:ppu00550 with 10 primary genes; module area: lipid_cell_envelope_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 23

- pbpC: PP_0572 | Q88QC2 | peptidoglycan glycosyltransferase (EC 2.4.99.28) (EC 2.4.99.28; primary bucket kegg:ppu00550)
- murA: PP_0964 | Q88P88 | UDP-N-acetylglucosamine 1-carboxyvinyltransferase (EC 2.5.1.7) (Enoylpyruvate transferase) (UDP-N-acetylglucosamine enolpyruvyl transferase) (EPT) (EC 2.5.1.7; primary bucket kegg:ppu00550)
- ftsI: PP_1331 | Q88N82 | Peptidoglycan D,D-transpeptidase FtsI (EC 3.4.16.4) (Penicillin-binding protein 3) (PBP-3) (EC 3.4.16.4; primary bucket kegg:ppu01501)
- murE: PP_1332 | Q88N81 | UDP-N-acetylmuramoyl-L-alanyl-D-glutamate--2,6-diaminopimelate ligase (EC 6.3.2.13) (Meso-A2pm-adding enzyme) (Meso-diaminopimelate-adding enzyme) (UDP-MurNAc-L-Ala-D-Glu:meso-diaminopimelate ligase) (UDP-MurNAc-tripeptide synthetase) (UDP-N-acetylmuramyl-tripeptide synthetase) (EC 6.3.2.13; primary bucket kegg:ppu00300)
- murF: PP_1333 | Q88N80 | UDP-N-acetylmuramoyl-tripeptide--D-alanyl-D-alanine ligase (EC 6.3.2.10) (D-alanyl-D-alanine-adding enzyme) (EC 6.3.2.10; primary bucket kegg:ppu01502)
- mraY: PP_1334 | Q88N79 | Phospho-N-acetylmuramoyl-pentapeptide-transferase (EC 2.7.8.13) (UDP-MurNAc-pentapeptide phosphotransferase) (EC 2.7.8.13; primary bucket kegg:ppu01502)
- murD: PP_1335 | Q88N78 | UDP-N-acetylmuramoylalanine--D-glutamate ligase (EC 6.3.2.9) (D-glutamic acid-adding enzyme) (UDP-N-acetylmuramoyl-L-alanyl-D-glutamate synthetase) (EC 6.3.2.9; primary bucket kegg:ppu00470)
- ftsW: PP_1336 | Q88N77 | Probable peptidoglycan glycosyltransferase FtsW (PGT) (EC 2.4.99.28) (Cell division protein FtsW) (Cell wall polymerase) (Peptidoglycan polymerase) (PG polymerase) (EC 2.4.99.28; primary bucket kegg:ppu00550)
- murG: PP_1337 | Q88N76 | UDP-N-acetylglucosamine--N-acetylmuramyl-(pentapeptide) pyrophosphoryl-undecaprenol N-acetylglucosamine transferase (EC 2.4.1.227) (Undecaprenyl-PP-MurNAc-pentapeptide-UDPGlcNAc GlcNAc transferase) (EC 2.4.1.227; primary bucket kegg:ppu01502)
- murC: PP_1338 | Q88N75 | UDP-N-acetylmuramate--L-alanine ligase (EC 6.3.2.8) (UDP-N-acetylmuramoyl-L-alanine synthetase) (EC 6.3.2.8; primary bucket kegg:ppu00550)
- ddlB: PP_1339 | Q88N74 | D-alanine--D-alanine ligase B (EC 6.3.2.4) (D-Ala-D-Ala ligase B) (D-alanylalanine synthetase B) (EC 6.3.2.4; primary bucket kegg:ppu01502)
- uppS: PP_1595 | Q88MH6 | Ditrans,polycis-undecaprenyl-diphosphate synthase ((2E,6E)-farnesyl-diphosphate specific) (EC 2.5.1.31) (Ditrans,polycis-undecaprenylcistransferase) (Undecaprenyl diphosphate synthase) (UDS) (Undecaprenyl pyrophosphate synthase) (UPP synthase) (EC 2.5.1.31; primary bucket kegg:ppu00900)
- murB: PP_1904 | Q88LM5 | UDP-N-acetylenolpyruvoylglucosamine reductase (EC 1.3.1.98) (UDP-N-acetylmuramate dehydrogenase) (EC 1.3.1.98; primary bucket kegg:ppu00550)
- dacB: PP_2098 | Q88L37 | D-alanyl-D-alanine carboxypeptidase (primary bucket kegg:ppu00550)
- uppP: PP_2862 | Q88IY7 | Undecaprenyl-diphosphatase (EC 3.6.1.27) (Bacitracin resistance protein) (Undecaprenyl pyrophosphate phosphatase) (EC 3.6.1.27; primary bucket kegg:ppu00552)
- mrdA-I: PP_3741 | Q88GI2 | Peptidoglycan D,D-transpeptidase MrdA (EC 3.4.16.4) (Penicillin-binding protein 2) (PBP-2) (EC 3.4.16.4; primary bucket kegg:ppu01501)
- ddlA: PP_4346 | Q88EV6 | D-alanine--D-alanine ligase A (EC 6.3.2.4) (D-Ala-D-Ala ligase A) (D-alanylalanine synthetase A) (EC 6.3.2.4; primary bucket kegg:ppu01502)
- mrcB: PP_4683 | Q88DY5 | Penicillin-binding protein 1B (PBP-1b) (PBP1b) (Murein polymerase) (primary bucket kegg:ppu00550)
- dacA: PP_4803 | Q88DM2 | serine-type D-Ala-D-Ala carboxypeptidase (EC 3.4.16.4) (EC 3.4.16.4; primary bucket kegg:ppu00550)
- mrdB: PP_4806 | Q88DL9 | Peptidoglycan glycosyltransferase MrdB (PGT) (EC 2.4.99.28) (Cell elongation protein RodA) (Cell wall polymerase) (Peptidoglycan polymerase) (PG polymerase) (EC 2.4.99.28; primary bucket kegg:ppu00550)
- mrdA-II: PP_4807 | Q88DL8 | Peptidoglycan D,D-transpeptidase MrdA (EC 3.4.16.4) (Penicillin-binding protein 2) (PBP-2) (EC 3.4.16.4; primary bucket kegg:ppu01501)
- mrcA: PP_5084 | Q88CU6 | Penicillin-binding protein 1A (EC 2.4.99.28) (EC 3.4.16.4) (EC 2.4.99.28; 3.4.16.4; primary bucket kegg:ppu01501)
- mtgA: PP_5107 | Q88CS3 | Biosynthetic peptidoglycan transglycosylase (EC 2.4.99.28) (Glycan polymerase) (Peptidoglycan glycosyltransferase MtgA) (PGT) (EC 2.4.99.28; primary bucket kegg:ppu00550)

## Generic Module Context

### Working Scope

A reusable bacterial module that supplies the C55 polyprenyl-phosphate lipid carrier used for cell-envelope glycan assembly. UppS first elongates farnesyl diphosphate with eight isopentenyl diphosphates to form undecaprenyl diphosphate. An integral-membrane undecaprenyl-diphosphatase then removes one phosphate to generate undecaprenyl phosphate. The carrier supports multiple pathways, including peptidoglycan and lipopolysaccharide synthesis; transfer of pathway-specific sugars onto the carrier and downstream glycan polymerization are outside this module.

### Provisional Biological Outline

- Bacterial undecaprenyl-phosphate carrier supply
  - 1. undecaprenyl-diphosphate synthesis
  - Undecaprenyl-diphosphate synthesis
    - UppS undecaprenyl-diphosphate synthase (molecular player: bacterial UppS undecaprenyl-diphosphate synthases; activity or role: ditrans,polycis-undecaprenyl-diphosphate synthase activity)
  - 2. undecaprenyl-phosphate formation
  - Undecaprenyl-phosphate formation
    - UppP/BacA undecaprenyl-diphosphatase (molecular player: UppP/BacA undecaprenyl-diphosphatases; activity or role: undecaprenyl-diphosphatase activity)

### Known Relationships Among Steps

- Undecaprenyl-diphosphate synthesis feeds into Undecaprenyl-phosphate formation: UppS-derived C55-PP is the substrate for carrier-activating dephosphorylation.

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

# Module Review: Bacterial Undecaprenyl-Phosphate Carrier Supply in *Pseudomonas putida* KT2440

**Taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Module:** Bacterial undecaprenyl-phosphate (C55-P) carrier supply
**Source bucket queried:** KEGG ppu00550 (Peptidoglycan biosynthesis)
**Module area:** lipid / cell-envelope metabolism
**Date:** 2026-09-01

---

## 1. Executive summary

The generic two-step module — (1) UppS synthesis of undecaprenyl-diphosphate (C55-PP) and (2) UppP/BacA dephosphorylation to undecaprenyl-phosphate (C55-P) — is **satisfiable** in *P. putida* KT2440. Both steps are represented by reviewed (Swiss-Prot) orthologs: **uppS / PP_1595 (Q88MH6, EC 2.5.1.31)** and **uppP / bacA / PP_2862 (Q88IY7, EC 3.6.1.27)**. All KT2440 evidence is **homology-inferred** (both entries: protein existence "Inferred from homology", annotation score 3.0/5); there is no direct biochemical or genetic characterization in this strain.

Two curation-relevant nuances dominate this review:

1. **Boundary/over-collection problem.** Only 2 of the 23 candidate genes actually belong to this module. The candidate list is essentially the full peptidoglycan-biosynthesis bucket (ppu00550) plus adjacent PBP/cell-division genes. The other 21 genes are cytoplasmic Mur-ligase precursor synthesis, C55-P *consumers* (mraY, murG), or periplasmic glycan polymerases/transpeptidases — all explicitly outside the carrier-supply scope.
2. **Asymmetric redundancy.** Step 1 is **single-copy and non-redundant** (UppS is the only cis-prenyltransferase in the genome → expected essential). Step 2 is **functionally redundant**: beyond uppP (BacA family), KT2440 encodes three PAP2-family phosphatases (PP_0251, PP_0900, PP_4813) that belong to the same family (Pfam PF01569) as *E. coli*'s accessory C55-PP phosphatases PgpB/YbjG/LpxT. uppP is therefore probably individually dispensable.

**Recommended module calls:** Step 1 → **covered** (high confidence). Step 2 → **covered** (primary, uppP) with an attached **candidate_uncertain** note for accessory PAP2 redundancy. Module boundaries need tightening (**module_needs_revision** at the level of the bucket→module mapping, not the biology).

---

## 2. Target-organism pathway definition

**Included process (this module).** Supply of the reusable C55 polyprenyl-phosphate lipid carrier for cell-envelope glycan assembly, comprising exactly two reactions:

- **C55-PP synthesis:** *trans,trans*-farnesyl-diphosphate (FPP) + 8 isopentenyl-diphosphate (IPP) → ditrans,octacis-undecaprenyl-diphosphate (C55-PP) + 8 PPi (EC 2.5.1.31; cytoplasmic-facing cis-prenyltransferase).
- **C55-P formation:** C55-PP + H2O → C55-P + Pi (EC 3.6.1.27; integral-membrane pyrophosphatase). This activity acts on both *de novo* C55-PP (from UppS) and *recycled* C55-PP released on the periplasmic face after each round of glycan transfer.

**Explicitly excluded (kept in neighboring pathways):**
- **Upstream:** IPP/DMAPP and FPP supply — FPP is made by IspA (PP_0528, EC 2.5.1.1/2.5.1.10). This is terpenoid-backbone/isoprenoid metabolism (KEGG ppu00900 / MEP pathway), not this module.
- **Downstream / carrier consumers:** MraY (PP_1334, EC 2.7.8.13; C55-P → lipid I) and MurG (PP_1337, EC 2.4.1.227; lipid I → lipid II) *use* C55-P but perform pathway-specific sugar transfer and are outside scope. Likewise all PG polymerases/transpeptidases (ftsW, mrdB/rodA, ftsI, mrdA-I/II, mrcA/mrcB, pbpC, mtgA) and carboxypeptidases (dacA, dacB), and the cytoplasmic Mur ligases (murA–F, ddlA/B).
- **Overview maps to keep separate:** KEGG global/overview maps ppu01100 (metabolic pathways), ppu01110 (biosynthesis of secondary metabolites); and the PG super-pathway maps ppu01501/ppu01502 (β-lactam resistance / peptidoglycan). Note uppP is bucketed by KEGG under **ppu00552** (not ppu00550), reflecting its carrier-recycling role.

**Alternate names / database definitions.** UppS = undecaprenyl pyrophosphate synthase / di-*trans*,poly-*cis*-undecaprenyl-diphosphate synthase / cis-IPPS (Pfam PF01255, "UPP synthase family"; MetaCyc UDP synthase). UppP = BacA / Upk / undecaprenyl pyrophosphate phosphatase / "bacitracin resistance protein" (Pfam PF02673, InterPro IPR003824). The carrier itself is variously "undecaprenyl phosphate", "bactoprenol phosphate", "C55-P", or "lipid carrier".

---

## 3. Expected step model

| Step | Reaction (EC) | Expected player | KT2440 status |
|------|---------------|-----------------|----------------|
| 1. Undecaprenyl-diphosphate synthesis | FPP + 8 IPP → C55-PP (2.5.1.31) | UppS cis-prenyltransferase | **covered** — uppS/PP_1595 (single-copy, non-redundant) |
| 2. Undecaprenyl-phosphate formation | C55-PP → C55-P + Pi (3.6.1.27) | UppP/BacA + PAP2 accessory phosphatases | **covered (primary)** uppP/PP_2862; **candidate_uncertain** accessory PP_0251/PP_0900/PP_4813 |

No additional obligatory steps exist in the generic module. There is no expectation of a lineage-specific replacement for the *synthesis* step in a Gram-negative γ-proteobacterium such as *P. putida*; the UppS cis-prenyltransferase family is universal in bacteria.

---

## 4. Candidate genes and evidence

### High-confidence, in-scope

**uppS — PP_1595 — Q88MH6 — EC 2.5.1.31 (Step 1).**
- **Role:** sole cis-prenyltransferase producing C55-PP. Pfam PF01255; InterPro IPR001441/IPR018520/IPR036424 ("UPP synthase family"). GO:0008834 (di-trans,poly-cis-undecaprenyl-diphosphate synthase activity), GO:0016094 (polyprenol biosynthesis), GO:0000287 (Mg2+), GO:0071555 (cell-wall organization).
- **Evidence type:** ortholog assignment, reviewed Swiss-Prot; protein existence "inferred from homology" (no direct KT2440 assay). Strong homology transfer from well-characterized bacterial UppS (structural/enzymological work in *E. coli*, *S. pneumoniae*, *S. aureus*: PMIDs 24827744, 25287857, 34473495).
- **Caveats:** KEGG places uppS in ppu00900 (terpenoid backbone), which is why it is not among the ppu00550 "primary" genes; this is a bucket artifact, not a functional discrepancy. Single-copy → **expected essential** (universal essentiality of UppS; validated antibiotic target). No isozyme backup exists in the genome.

**uppP / bacA / upk — PP_2862 — Q88IY7 — EC 3.6.1.27 (Step 2).**
- **Role:** primary (BacA-family) undecaprenyl-pyrophosphate phosphatase. Pfam PF02673; InterPro IPR003824 ("UppP family"). GO:0050380 (undecaprenyl-diphosphatase activity), GO:0046677 (response to antibiotic), GO:0005886 (plasma membrane).
- **Evidence type:** ortholog assignment, reviewed Swiss-Prot; "inferred from homology". The "bacitracin resistance protein" name reflects the well-established link between C55-PP phosphatase level and bacitracin resistance (bacitracin sequesters C55-PP).
- **Caveats:** the single-gene annotation **under-represents the true biology of the step** — in *E. coli* BacA supplies only ~75% of membrane C55-PP phosphatase activity and a *bacA* deletion is viable (PMID 15778224). uppP alone is therefore probably **not essential** in KT2440.

### Accessory / redundancy candidates (in-scope for Step 2, currently unannotated for it)

| Gene | Acc | Family | Note |
|------|-----|--------|------|
| PP_0251 | Q88R82 | PAP2 (PF01569 / IPR000326) + haloperoxidase domain | candidate accessory C55-PP phosphatase |
| PP_0900 | Q88PF0 | PAP2 (PF01569 / IPR000326) | candidate accessory C55-PP phosphatase |
| PP_4813 | Q88DL2 | PAP2 (PF01569) fused to DedA (PF09335) | candidate; DedA fusion suggests membrane/lipid role |

These share the exact family (PF01569) of *E. coli* PgpB/YbjG/LpxT, which provide the remaining ~25% of C55-PP phosphatase activity; only *bacA*+*ybjG*+*pgpB* triple inactivation is lethal (PMID 15778224; Manat et al. 2015, PMID 26560897). Transfer to *P. putida* is **family-level (moderate)**, not orthology- or function-level. Their *primary* physiological substrate (phosphatidylglycerol-phosphate, lipid A 1-phosphate, or C55-PP) is unresolved.

### Out-of-scope candidates (correct annotations, wrong module)
- **C55-P consumers:** mraY/PP_1334, murG/PP_1337 (belong to lipid-linked PG precursor assembly).
- **Cytoplasmic precursor synthesis:** murA/PP_0964, murB/PP_1904, murC/PP_1338, murD/PP_1335, murE/PP_1332, murF/PP_1333, ddlA/PP_4346, ddlB/PP_1339.
- **PG polymerization/crosslinking/hydrolysis:** ftsW/PP_1336, mrdB/PP_4806, ftsI/PP_1331, mrdA-I/PP_3741, mrdA-II/PP_4807, mrcA/PP_5084, mrcB/PP_4683, pbpC/PP_0572, mtgA/PP_5107, dacA/PP_4803, dacB/PP_2098.

None of these should be attached to the carrier-supply module.

---

## 5. Gaps, ambiguities, and likely over-annotations

- **Over-collection (primary issue).** The bucket→module mapping pulls the entire ppu00550 PG-biosynthesis set into a module whose true membership is 2 genes. This is a **module_needs_revision** at the mapping level.
- **Step-2 under-annotation.** Only uppP carries GO:0050380. The genome's PAP2 paralogs are candidate accessory phosphatases but lack the C55-PP-phosphatase annotation. This is the opposite risk to over-propagation: a real, redundant activity is likely **under-captured**.
- **PAP2 over-generalization risk.** Conversely, do **not** blanket-assign GO:0050380 to PP_0251/PP_0900/PP_4813 without phylogenetic/experimental support — PAP2 enzymes are promiscuous and many act primarily on glycerophospholipids or LPS, not C55-PP. Broad EC/GO transfer here would be a new over-propagation.
- **EC/GO breadth on PBPs.** Several out-of-scope PBPs carry broad EC 2.4.99.28 / 3.4.16.4 mappings (e.g., mrcA with both), but these are irrelevant to this module.
- **No direct KT2440 evidence.** Both in-scope genes are homology-inferred. No strain-specific essentiality dataset was retrievable in this review to confirm UppS essentiality or uppP dispensability in KT2440 specifically.

---

## 6. Module and GO-curation recommendations

**Module step calls:**
- **Step 1 (undecaprenyl-diphosphate synthesis): `covered`** — uppS/PP_1595, high confidence, single-copy, expected essential.
- **Step 2 (undecaprenyl-phosphate formation): `covered`** via uppP/PP_2862, with an attached **`candidate_uncertain`** annotation recording probable accessory redundancy from PP_0251/PP_0900/PP_4813 and the resulting likelihood that uppP is individually non-essential.
- **Module boundary: `module_needs_revision`** — restrict membership to UppS + UppP/PAP2 and explicitly exclude C55-P consumers (mraY, murG) and PG polymerases. Add an explicit note that FPP supply (IspA/ppu00900) is the upstream boundary and glycan transfer is the downstream boundary.

**GO / annotation actions:**
- Consider a curator-reviewed GO:0050380 (undecaprenyl-diphosphatase activity) annotation with an appropriate "inferred from sequence/structural similarity" evidence code for the best-supported PAP2 paralog(s), *after* orthology analysis — do not auto-propagate.
- Keep uppP's KEGG bucket (ppu00552) note; the ppu00552 vs ppu00550 split reflects synthesis vs recycling and is informative, not an error.
- No new GO *term* requests appear necessary — existing terms (GO:0008834, GO:0016094, GO:0050380) cover both steps. A new **module document** narrowing the reusable carrier-supply module is warranted.

---

## 7. Genes to promote to full `fetch-gene` review

1. **uppS / PP_1595 (Q88MH6)** — confirm essentiality call and structural/active-site conservation; anchor gene of Step 1.
2. **uppP / PP_2862 (Q88IY7)** — confirm BacA-family active-site residues (Glu/Ser/Arg; PMID 26560897) and dispensability expectation; anchor gene of Step 2.
3. **PP_0251 (Q88R82), PP_0900 (Q88PF0), PP_4813 (Q88DL2)** — PAP2-family paralogs; promote for reciprocal-best-hit/phylogenetic assignment vs *E. coli* PgpB/YbjG/LpxT and substrate-specificity assessment before any C55-PP-phosphatase annotation.

---

## 8. Key references

- El Ghachi M, Derbise A, Bouhss A, Mengin-Lecreulx D. *Identification of multiple genes encoding membrane proteins with undecaprenyl pyrophosphate phosphatase (UppP) activity in Escherichia coli.* J Biol Chem. 2005. **PMID 15778224.** (BacA supplies most, not all, C55-PP phosphatase activity; *bacA* viable; *bacA+ybjG+pgpB* lethal.)
- Manat G, El Ghachi M, Auger R, et al. *Membrane Topology and Biochemical Characterization of the E. coli BacA Undecaprenyl-Pyrophosphate Phosphatase.* 2015. **PMID 26560897.** (BacA ≈75% of activity; PAP2 family = PgpB/YbjG/LpxT; catalytic residues.)
- Sinko W, Wang Y, Zhu W, et al. *Undecaprenyl diphosphate synthase inhibitors: antibacterial drug leads.* J Med Chem. 2014. **PMID 24827744.** (UppS essential for lipid I/II and PG; drug target.)
- Danley DE, Baima ET, Mansour M, et al. *Discovery and structural characterization of an allosteric inhibitor of bacterial cis-prenyltransferase.* 2015. **PMID 25287857.** ("UPPs is an essential enzyme in a key bacterial cell wall synthesis pathway.")
- Workman SD, Day J, Farha MA, et al. *Structural Insights into the Inhibition of Undecaprenyl Pyrophosphate Synthase from Gram-Positive Bacteria.* 2021. **PMID 34473495.**
- UniProtKB (organism 160488): Q88MH6 (uppS/PP_1595), Q88IY7 (uppP/PP_2862), Q88R82/Q88PF0/Q88DL2 (PAP2 paralogs) — accessed 2026-09-01.

---

### Evidence-strength summary

| Claim | Basis | Strength for KT2440 |
|-------|-------|---------------------|
| uppS/PP_1595 makes C55-PP | UniProt ortholog + universal UppS biology | Strong (homology); direct assay absent |
| uppS single-copy/essential | genome prenyltransferase census + general UppS essentiality | Strong inference; not strain-verified |
| uppP/PP_2862 is primary C55-PP phosphatase | UniProt ortholog (BacA family) | Strong (homology) |
| uppP individually non-essential (redundancy) | *E. coli* genetics (PMID 15778224) + KT2440 PAP2 paralogs present | Moderate (family transfer) |
| PP_0251/0900/4813 act on C55-PP | PF01569 family match to PgpB/YbjG/LpxT | Weak–moderate; needs orthology/experiment |


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_undecaprenyl_phosphate_carrier_supply__ppu00550-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_undecaprenyl_phosphate_carrier_supply__ppu00550-deep-research-openscientist_artifacts/final_report.pdf)