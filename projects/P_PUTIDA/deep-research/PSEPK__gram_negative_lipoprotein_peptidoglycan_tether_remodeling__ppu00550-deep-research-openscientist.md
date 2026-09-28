---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T01:10:05.180341'
end_time: '2026-09-01T01:32:11.901592'
duration_seconds: 1326.72
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Gram-negative lipoprotein-peptidoglycan tether remodeling
  module_summary: A reusable Gram-negative bacterial module for reversible covalent
    attachment of an outer-membrane lipoprotein to peptidoglycan. An ErfK-family L,D-transpeptidase
    transfers a tetrapeptide-stem donor onto the C terminus of a Braun-lipoprotein-like
    substrate, and a YafK/LdtF-family cysteine hydrolase can release the lipoprotein
    by cleaving the resulting amide bond. These reactions remodel the connection between
    the outer membrane and sacculus; they do not represent peptidoglycan glycan polymerization
    or canonical 4-3 peptide crosslinking by penicillin-binding proteins.
  module_outline: "- Gram-negative lipoprotein-peptidoglycan tether remodeling\n \
    \ - 1. outer-membrane lipoprotein anchoring to peptidoglycan\n  - Lipoprotein-peptidoglycan\
    \ tether formation\n    - ErfK-family lipoprotein-anchoring L,D-transpeptidase\
    \ (molecular player: ErfK-family lipoprotein-anchoring L,D-transpeptidases; activity\
    \ or role: peptidoglycan L,D-transpeptidase activity)\n  - 2. lipoprotein-peptidoglycan\
    \ tether release\n  - Lipoprotein-peptidoglycan tether hydrolysis\n    - YafK/LdtF-family\
    \ lipoprotein-tether hydrolase (molecular player: YafK/LdtF-family lipoprotein-tether\
    \ hydrolases; activity or role: peptidoglycan-protein cross-link hydrolase activity)"
  module_connections: '- Lipoprotein-peptidoglycan tether formation feeds into Lipoprotein-peptidoglycan
    tether hydrolysis: The covalent tether formed by the ErfK-family enzyme is the
    substrate for YafK/LdtF-family hydrolysis.'
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
    max_iterations: 5
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
  path: PSEPK__gram_negative_lipoprotein_peptidoglycan_tether_remodeling__ppu00550-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__gram_negative_lipoprotein_peptidoglycan_tether_remodeling__ppu00550-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Gram-negative lipoprotein-peptidoglycan tether remodeling in Pseudomonas putida KT2440

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

A reusable Gram-negative bacterial module for reversible covalent attachment of an outer-membrane lipoprotein to peptidoglycan. An ErfK-family L,D-transpeptidase transfers a tetrapeptide-stem donor onto the C terminus of a Braun-lipoprotein-like substrate, and a YafK/LdtF-family cysteine hydrolase can release the lipoprotein by cleaving the resulting amide bond. These reactions remodel the connection between the outer membrane and sacculus; they do not represent peptidoglycan glycan polymerization or canonical 4-3 peptide crosslinking by penicillin-binding proteins.

### Provisional Biological Outline

- Gram-negative lipoprotein-peptidoglycan tether remodeling
  - 1. outer-membrane lipoprotein anchoring to peptidoglycan
  - Lipoprotein-peptidoglycan tether formation
    - ErfK-family lipoprotein-anchoring L,D-transpeptidase (molecular player: ErfK-family lipoprotein-anchoring L,D-transpeptidases; activity or role: peptidoglycan L,D-transpeptidase activity)
  - 2. lipoprotein-peptidoglycan tether release
  - Lipoprotein-peptidoglycan tether hydrolysis
    - YafK/LdtF-family lipoprotein-tether hydrolase (molecular player: YafK/LdtF-family lipoprotein-tether hydrolases; activity or role: peptidoglycan-protein cross-link hydrolase activity)

### Known Relationships Among Steps

- Lipoprotein-peptidoglycan tether formation feeds into Lipoprotein-peptidoglycan tether hydrolysis: The covalent tether formed by the ErfK-family enzyme is the substrate for YafK/LdtF-family hydrolysis.

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

# Gram-Negative Lipoprotein–Peptidoglycan Tether Remodeling in *Pseudomonas putida* KT2440

**Commissioned Module/Pathway/Taxon Curation Review**

**Taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI:txid160488; proteome UP000000556)
**Local bucket reviewed:** KEGG `ppu00550` "Peptidoglycan biosynthesis" (10 primary genes; module area *lipid_cell_envelope_metabolism*)
**Module under review:** reversible covalent attachment of an outer-membrane lipoprotein to peptidoglycan — tether **formation** (ErfK-family L,D-transpeptidase) + tether **hydrolysis** (YafK/LdtF/DpaA-family hydrolase)

---

## Summary

The single most important curation conclusion of this review is a **scope mismatch between the module and its assigned candidate list**. The commissioned module describes reversible covalent attachment of an outer-membrane (OM) lipoprotein to peptidoglycan (PG): an ErfK/YkuD-family **L,D-transpeptidase** anchors a Braun-lipoprotein-like substrate, and a YafK/LdtF/DpaA-family **cysteine hydrolase** can release it. **None** of the 23 candidate genes drawn from KEGG `ppu00550` encode either activity. All 23 are canonical PG-biosynthesis and cell-division proteins (Mur ligases, penicillin-binding proteins, SEDS glycosyltransferases, D,D-carboxypeptidases, undecaprenyl-phosphate enzymes) that perform glycan polymerization and 4→3 D,D-crosslinking — reactions the module scope explicitly **excludes**. The `ppu00550`→module link is therefore a **boundary error**; the module should be detached and marked `module_needs_revision`.

The module's actual enzymes lie outside the candidate list. KT2440 encodes exactly two proteins carrying the diagnostic YkuD/ErfK L,D-transpeptidase domain (Pfam **PF03734** / InterPro IPR005490): **PP_2320** (Q88KH0) and **PP_1451** (Q88MW7). The **tether-formation step is COVERED**: PP_2320 is a high-confidence ortholog (**78.9% identity over a 303-residue alignment**) of *P. aeruginosa* PA2854, experimentally shown to covalently anchor the OM lipoprotein **OprI** to PG in live cells ([PMID: 42100858](https://pubmed.ncbi.nlm.nih.gov/42100858/)). KT2440 encodes a co-syntenic OprI ortholog, **PP_2322** (Q88KG8, 83 aa, OprI/Braun's-lipoprotein family, Pfam PF11839), only ~2 genes from PP_2320 — an enzyme+substrate cassette conserved from PAO1.

The **tether-hydrolysis (release) step is a GAP / candidate_uncertain**. The reference release enzyme is *E. coli* DpaA/LdtF (P0AA99), a PF03734 murein L,D-endopeptidase that detaches Braun's lipoprotein from PG ([PMID: 33947763](https://pubmed.ncbi.nlm.nih.gov/33947763/)). No KT2440 protein — and, on present evidence, no *Pseudomonas* protein — is a confident DpaA ortholog. The only fold-level fallback is PP_1451, a minimal (184 aa) catalytic-domain-only L,D-transpeptidase whose closest match is *P. aeruginosa* PA3756, not DpaA. Whether release in *Pseudomonas* is carried by a divergent enzyme, by PP_1451 moonlighting, or is simply not part of this organism's biology is the central open question. All conclusions are homology/synteny-based (strong genus transfer for formation; unresolved for release); **no direct KT2440 experiment exists**.

---

## Key Findings

### Finding 1 — The 23 KEGG `ppu00550` candidates are entirely out of module scope (F001)

A proteome-wide scan of UP000000556 for the defining YkuD/ErfK L,D-transpeptidase catalytic domain (Pfam **PF03734** / InterPro **IPR005490**) returns **exactly two proteins — PP_2320 and PP_1451 — neither of which is in the candidate list.** Every one of the 23 supplied candidates is instead a canonical PG-biosynthesis/division protein: cytoplasmic Mur ligases and precursor enzymes (*murA* PP_0964, *murB* PP_1904, *murC* PP_1338, *murD* PP_1335, *murE* PP_1332, *murF* PP_1333, *mraY* PP_1334, *murG* PP_1337, *ddlA* PP_4346, *ddlB* PP_1339); carrier-lipid metabolism (*uppS* PP_1595, *uppP* PP_2862); penicillin-binding proteins performing 4→3 D,D-transpeptidation and glycan polymerization (*ftsI*/PBP3 PP_1331, *mrdA-I* PP_3741, *mrdA-II* PP_4807, *mrcA*/PBP1a PP_5084, *mrcB*/PBP1b PP_4683, *pbpC* PP_0572, *mtgA* PP_5107); SEDS glycosyltransferases (*ftsW* PP_1336, *mrdB*/RodA PP_4806); and D,D-carboxypeptidases (*dacA* PP_4803, *dacB* PP_2098). These share the substrate "peptidoglycan" with the module but no enzymes, no EC classes, and — crucially — not the cysteine-active-site YkuD fold that defines the module. This is the definitive evidence that the candidate list, though a correct enumeration of KEGG "Peptidoglycan biosynthesis," does not represent this module.

### Finding 2 — PP_2320 is the ErfK-family lipoprotein-anchoring L,D-transpeptidase; substrate = OprI/PP_2322 (F002, F005, F006, F007)

PP_2320 (Q88KH0, 325 aa) is the clear ortholog of experimentally validated *P. aeruginosa* PAO1 **PA2854** (Q9HZZ0, 323 aa). Quantitatively, Smith–Waterman over full sequences gives **78.9% identity across a 303-aa alignment** — orthology-grade similarity (calibration: *E. coli* LdtA vs LdtB = 67% over 285 aa). PA2854 was directly shown to be "*the catalyst that performs this transformation between the cell wall and the outer-membrane lipoprotein OprI in live*" *P. aeruginosa* ([PMID: 42100858](https://pubmed.ncbi.nlm.nih.gov/42100858/)). PP_2320 also aligns to the *E. coli* anchoring clade — 50.3% to LdtB/YbiS and 46.7% to LdtA/ErfK over the ~169-aa catalytic region — the very family defined as "*responsible for the attachment of the Braun lipoprotein to murein*" ([PMID: 17369299](https://pubmed.ncbi.nlm.nih.gov/17369299/)). Its 4-mer Jaccard similarity to PA2854 (23.2%) exceeds that to any other *E. coli*/*Pseudomonas* L,D-transpeptidase (≤3.3%), and it shows no homology to DpaA/LdtF (only an 8-aa spurious local alignment).

The substrate is present and co-syntenic. **OprI = PP_2322** (Q88KG8, 83 aa) belongs to the OprI/Braun's-lipoprotein family (Pfam **PF11839**, IPR021793), is a lipid-anchored lipoprotein with a signal peptide, and is a same-length ortholog of PAO1 OprI/PA2853 (P11221). In PAO1, *oprI* is immediately adjacent to the validated anchoring enzyme PA2854; in KT2440 the pairing is conserved — PP_2320 lies ~2 loci from *oprI*/PP_2322, separated only by the uncharacterized PP_2319 and a PP_2321 gap. Conserved enzyme–substrate synteny across two *Pseudomonas* species substantially strengthens transfer of PA2854's validated function to PP_2320.

### Finding 3 — Domain architecture cements PP_2320 in the anchoring clade (F005)

PP_2320 carries a **LysM peptidoglycan-binding domain (IPR018392)** plus the **L,D-transpeptidase catalytic domain (IPR005490, residues 98–233)**, is classified in the "Bacterial L,D-transpeptidase" family **IPR050979**, and has an N-terminal signal peptide — an architecture identical to validated PA2854. Anchoring Ldts (E. coli LdtA/B/C) characteristically carry LysM PG-binding modules, which the release-clade DpaA lacks. This architectural signature independently corroborates the orthology-based assignment of PP_2320 to tether *formation*.

### Finding 4 — The release enzyme (DpaA/LdtF) has no confident KT2440 ortholog (F003, F004, F008)

The *E. coli* Lpp–PG release enzyme is **DpaA/LdtF/YafK = UniProt P0AA99** (246 aa, PF03734), a murein L,D-endopeptidase that "*catalyzes the cleavage of the cross-link between the outer membrane-anchored Braun's lipoprotein (Lpp) and peptidoglycan, detaching Lpp*" and whose title finding is "*DpaA Detaches Braun's Lipoprotein from Peptidoglycan*" ([PMID: 33947763](https://pubmed.ncbi.nlm.nih.gov/33947763/)). Re-running 4-mer Jaccard against the correct DpaA sequence gives PP_1451 = 0.2% and PP_2320 = 0.0% — neither KT2440 YkuD protein groups with DpaA. Notably, **no** PAO1 YkuD protein groups with DpaA either (PA2854/PA3756/PA0732 all ≤0.7%), suggesting the release clade is absent or highly divergent across the genus. Because k-mer/Smith–Waterman metrics are insensitive to divergent homologs, this argues against a *close* ortholog but cannot by itself prove total absence — hence `candidate_uncertain` rather than a hard `not_expected`.

### Finding 5 — PP_1451 is a second, functionally uncertain L,D-transpeptidase (F003, F006)

PP_1451 (Q88MW7, 184 aa) is the only other PF03734 protein in KT2440. It is **minimal** — catalytic domain only, **no LysM**, and not in IPR050979. Its best match is *P. aeruginosa* PA3756 (Q9HXN9, 166 aa) at 67.4% identity over 138 aa — an ortholog of undefined physiological role. It shows negligible similarity to *E. coli* DpaA/LdtF (only a 16-aa spurious alignment), to the anchoring clade, or to the 3→3 crosslinking clade (LdtD/E). It is therefore the only structural candidate for a release activity but is not, on sequence grounds, a DpaA ortholog. It should be flagged `candidate_uncertain` and resolved experimentally.

### Finding 6 — Reduced L,D-transpeptidase complement (F002, F003)

KT2440 encodes only **2** PF03734 proteins versus **3** in *P. aeruginosa* PAO1 (PA2854, PA3756, PA0732) and **6** in *E. coli* K-12. The smaller complement is itself circumstantial support for the release-step gap: *P. putida* appears to have retained anchoring capacity while lacking a dedicated DpaA-clade release enzyme.

---

## Target-Organism Pathway Definition

**Included process (module scope).** Covalent, reversible attachment of the C-terminus of a Braun-lipoprotein-like OM lipoprotein to the *meso*-diaminopimelate (mDAP) position of a PG tetrapeptide stem, catalyzed by an L,D-transpeptidase (acyl acceptor = protein rather than muropeptide), plus the reverse reaction — hydrolysis of that lipoprotein–mDAP amide bond by an LdtF/DpaA hydrolase, releasing the lipoprotein. In *E. coli* the lipoprotein is Braun's lipoprotein (Lpp); **in *Pseudomonas* the functional counterpart is OprI** (OprI/Braun's-lipoprotein family, Pfam PF11839). This is a **lineage-specific substrate substitution** curation must record explicitly.

**Neighboring processes to keep separate.**

- KEGG `ppu00550` **Peptidoglycan biosynthesis** (Mur pathway, glycan polymerization, PBP 4→3 D,D-transpeptidation) — the source of the candidate list; *not* the module.
- Over-broad overview/amino-acid maps cross-listing individual genes (*murE*→ppu00300, *murD*→ppu00470, division maps ppu01501/01502).
- **3→3 L,D-transpeptidation** for PG crosslinking / carbapenem resistance (E. coli LdtD/LdtE) — same superfamily, **different reaction** (muropeptide acceptor).
- **Non-covalent** OM–PG tethering by **Pal/OprL** and by OmpA/β-barrel proteins ([PMID: 33139883](https://pubmed.ncbi.nlm.nih.gov/33139883/)) — parallel mechanisms, not this covalent module.

**Alternate names / database definitions.** L,D-transpeptidase = "Ldt", "YkuD-domain protein", ErfK/YbiS/YcfS (E. coli LdtA/LdtB/LdtC); release enzyme = DpaA = LdtF = YafK. Relevant GO: **GO:0071972** (peptidoglycan L,D-transpeptidase activity); the tether-hydrolase activity is not cleanly represented in GO (see recommendations).

---

## Expected Step Model and Satisfiability

| Module step | Expected enzyme family | Diagnostic domain | KT2440 assignment | Verdict |
|---|---|---|---|---|
| **1. Tether formation** (lipoprotein → PG anchoring) | ErfK/anchoring-clade L,D-transpeptidase | PF03734 + LysM (IPR018392) | **PP_2320** (Q88KH0) acting on **OprI/PP_2322** (Q88KG8) | **covered** (high; strong genus transfer) |
| **2. Tether hydrolysis** (lipoprotein release) | YafK/LdtF/DpaA L,D-endopeptidase | PF03734 (DpaA clade) | No confident ortholog; weak fallback **PP_1451** (Q88MW7) | **candidate_uncertain / gap** (moderate) |

---

## Mechanistic Model / Interpretation

```
        OUTER MEMBRANE
             |
        [ OprI / PP_2322 ]   (Braun-lipoprotein-family lipoprotein, PF11839; 83 aa)
             |  C-terminus
             |
   ==========|=====================================  isopeptide (amide) tether
      STEP 1 |  FORMATION                 STEP 2 | HYDROLYSIS (release)
             v                                   v
   PP_2320 (Q88KH0)                     DpaA/LdtF-type enzyme
   ErfK/anchoring L,D-TPase             (E. coli P0AA99)
   LysM + YkuD catalytic                --> NO confident KT2440 ortholog
   ~79% id to validated PA2854              (PP_1451 minimal Ldt = weak fallback)
             |                                   |
   transfers PG tetrapeptide              cleaves the amide,
   stem donor onto OprI C-term            detaching OprI
             |
        PEPTIDOGLYCAN (meso-DAP of stem peptide)

   Conserved cassette (PAO1 -> KT2440):
     ... oprI (PA2853/PP_2322) -- [gap] -- anchoring Ldt (PA2854/PP_2320) ...

   L,D-transpeptidase (PF03734) census:  E. coli = 6 | P. aeruginosa = 3 | P. putida = 2
```

**Interpretation.** *P. putida* KT2440 possesses a complete, syntenically organized machine for the **forward** (anchoring) reaction, using OprI as its Braun-lipoprotein surrogate. The **reverse** (release) reaction — catalyzed in *E. coli* by DpaA/LdtF — has no clear counterpart. Because the release enzyme belongs to the same PF03734 fold, the reduced YkuD complement of KT2440 (2 vs 6 in *E. coli*) is circumstantial evidence that a dedicated release function may be absent or repurposed in this lineage. Biologically this is plausible: OM tethering via OprI is a constitutive envelope feature, whereas regulated detachment (e.g., for division-site remodeling) may be dispensable or handled by a divergent enzyme in *Pseudomonas*.

---

## Candidate Genes and Evidence (Detail)

### The module's true genes (NOT in the KEGG candidate list)

| Gene | UniProt | Length | Role | Key evidence | Curation status |
|---|---|---|---|---|---|
| **PP_2320** | Q88KH0 | 325 aa | ErfK-family OprI-anchoring L,D-transpeptidase | 78.9% id/303 aa to validated PA2854 (PMID 42100858); 47–50% to E. coli anchoring Ldts (PMID 17369299); LysM+catalytic (IPR050979); syntenic to OprI | **covered** — promote |
| **PP_2322 / OprI** | Q88KG8 | 83 aa | Braun's-lipoprotein-family substrate (acyl acceptor) | PF11839/IPR021793; ortholog of PAO1 OprI (P11221); OprI covalent attachment validated in PAO1 (PMID 42100858) | substrate — promote |
| **PP_1451** | Q88MW7 | 184 aa | Second, uncertain L,D-transpeptidase (release fallback) | Ortholog of PA3756 (67.4%/138 aa); no homology to DpaA/LdtF (≤16 aa); catalytic-only, no LysM | **candidate_uncertain** — promote |

### The 23 KEGG `ppu00550` candidates — assessment (all OUT OF SCOPE)

All 23 are canonical PG-metabolism genes and should be marked **not part of this module**; none carries PF03734.

- **Cytoplasmic Mur/Ddl/carrier steps** (murA–G, mraY, ddlA/B, uppS, uppP): standard, high-confidence PG-precursor biosynthesis; correct EC assignments; over-broad KEGG bucket tags (murE→ppu00300, murD→ppu00470) reflect map cross-listing, not different function.
- **PBP transpeptidases/glycosyltransferases** (ftsI/PBP3; mrdA-I, mrdA-II/PBP2; mrcA/PBP1a; mrcB/PBP1b; pbpC; mtgA; ftsW; mrdB/RodA): perform 4→3 D,D-transpeptidation and glycan polymerization — explicitly excluded by module scope. **mrdA-I/mrdA-II is a genuine PBP2 paralog pair** (annotation consistent, not over-propagation).
- **D,D-carboxypeptidases** (dacA, dacB): PG maturation, EC 3.4.16.4; not module members.
- **Broad EC/GO caveat:** EC 2.4.99.28 (ftsW, mrdB, mtgA, pbpC, mrcA, mrcB) and EC 3.4.16.4 (ftsI, mrdA-I/II, mrcA, dacA) are shared across many PBPs; these broad mappings must not be used to infer L,D-transpeptidase activity.

---

## Gaps, Ambiguities, and Likely Over-Annotations

1. **Release step is the principal gap.** No KT2440 protein is a confident DpaA/LdtF ortholog; the whole *Pseudomonas* genus lacks a close DpaA ortholog by k-mer and Smith–Waterman metrics. Possibilities: (i) genuine lineage loss of a dedicated tether hydrolase; (ii) release by a divergent enzyme (PP_1451 or an uncharacterized peptidase); (iii) the OprI tether is not actively released in *P. putida*. **Mark `candidate_uncertain`, leaning `gap`.**
2. **PP_1451 ambiguity:** could be a minor anchoring Ldt, a 3→3 crosslinker, or a release enzyme — currently unassignable; needs full review.
3. **Candidate-list mismatch (`module_needs_revision` at the bucket level):** binding this module to KEGG `ppu00550` mis-scopes it; the module's genes are not in that KEGG map. A **boundary error to flag**, not a biology gap.
4. **Generic UniProt names:** PP_2320 and PP_1451 are both "L,D-TPase catalytic domain-containing protein" — under-annotated relative to the evidence for PP_2320.
5. **Over-annotation risk:** none of the 23 KEGG genes should be propagated into the tether module on "peptidoglycan" keyword overlap.

---

## Module and GO-Curation Recommendations

| Module step | Recommended status | Evidence basis |
|---|---|---|
| Tether formation (anchoring) | **covered** | PP_2320 (79% to validated PA2854; LysM+catalytic; syntenic to OprI/PP_2322) |
| Tether hydrolysis (release) | **candidate_uncertain → gap** | No confident DpaA ortholog; PP_1451 weak fallback |
| KEGG `ppu00550` → module link | **module_needs_revision** (boundary error) | All 23 candidates canonical PG biosynthesis; no PF03734 |

Concrete actions:

1. **Detach** the module from KEGG bucket `ppu00550`; record the boundary rationale (no shared enzymes/chemistry). Add explicit exclusions: PBP D,D-transpeptidases, Mur ligases, Pal/OprL, OmpA/β-barrel tethers.
2. **Add** PP_2320 + PP_2322 as the tether-formation enzyme+substrate pair. Record OprI (PP_2322) as the **lineage-specific substrate** replacing enterobacterial Lpp.
3. **Register** the release step as `candidate_uncertain`/`gap`, noting PP_1451 as the sole fold-level fallback.
4. **GO annotation:** update PP_2320 to "ErfK-family lipoprotein (OprI)-anchoring L,D-transpeptidase" with **GO:0071972** (peptidoglycan L,D-transpeptidase activity) and an OprI-anchoring biological-process term; evidence code ISS/ISO from PA2854 (PMID 42100858) + IEA domain support.
5. **GO term request likely needed** for the lipoprotein–peptidoglycan tether hydrolase (DpaA) activity: current GO lacks a specific "outer-membrane-lipoprotein–peptidoglycan cross-link hydrolase" term; a dedicated term would support this module step across taxa.
6. **Do not** propagate the module to any of the 23 `ppu00550` genes.

---

## Genes to Promote to Full `fetch-gene` Review

1. **PP_2320 (Q88KH0)** — promote; assign as OprI-anchoring L,D-transpeptidase (highest-value re-annotation).
2. **PP_1451 (Q88MW7)** — promote; resolve whether it is the (divergent) tether-release enzyme, a 3→3 crosslinker, or a minor anchoring Ldt.
3. **PP_2322 (Q88KG8, OprI)** — promote as the module substrate; confirm covalent-attachment status in *P. putida*.
4. *(Lower priority)* **PP_1223 (Pal/OprL)** — confirm it is only a *non-covalent* PG-associated lipoprotein, to keep it out of this module.

---

## Evidence Base

| PMID | Paper (abbrev.) | Role in this review |
|---|---|---|
| [42100858](https://pubmed.ncbi.nlm.nih.gov/42100858/) | *Outer Membrane–Peptidoglycan Anchoring in Pseudomonas* (El-Araby et al. 2026) | **Primary support.** Directly shows PA2854 anchors OprI to PG in live *P. aeruginosa*; validated function transferred to ortholog PP_2320. Verified: "*the gene product of PA2854 is the catalyst that performs this transformation between the cell wall and the outer-membrane lipoprotein OprI in live*." |
| [17369299](https://pubmed.ncbi.nlm.nih.gov/17369299/) | *Identification of the L,D-transpeptidases responsible for attachment of the Braun lipoprotein to E. coli peptidoglycan* (Magnet et al. 2007) | Defines the ErfK/Ldtfm family as the Braun-lipoprotein anchoring enzymes — the family of PP_2320. Verified: "*in Escherichia coli Ldt(fm) homologues are responsible for the attachment of the Braun lipoprotein to murein*." |
| [33947763](https://pubmed.ncbi.nlm.nih.gov/33947763/) | *DpaA Detaches Braun's Lipoprotein from Peptidoglycan* (Winkle et al. 2021) | Defines the release step (DpaA/LdtF, P0AA99) whose ortholog is missing/uncertain in KT2440. |
| [33139883](https://pubmed.ncbi.nlm.nih.gov/33139883/) | *β-Barrel proteins tether the outer membrane in many Gram-negative bacteria* (Sandoz et al. 2021) | Context: alternative/parallel OM–PG tethering mechanisms distinct from this covalent module. |

**How the evidence combines.** The formation step rests on *direct experimental* evidence in the sister species *P. aeruginosa* ([PMID: 42100858](https://pubmed.ncbi.nlm.nih.gov/42100858/)) plus quantitative orthology (78.9% id/303 aa), anchoring-clade domain architecture, and conserved enzyme–substrate synteny — a strong, though not KT2440-direct, transfer. The release step rests only on *absence-of-ortholog* reasoning against the *E. coli* reference DpaA ([PMID: 33947763](https://pubmed.ncbi.nlm.nih.gov/33947763/)), which is weaker (a divergent homolog could evade k-mer/Smith–Waterman detection).

Key database identifiers: PP_2320 Q88KH0, PP_1451 Q88MW7, PP_2322/OprI Q88KG8; PA2854 Q9HZZ0, OprI/PA2853 P11221; E. coli DpaA/LdtF P0AA99. Pfam PF03734, PF11839; InterPro IPR005490, IPR018392, IPR050979, IPR021793.

---

## Limitations and Knowledge Gaps

1. **No direct KT2440 experiment.** Both the anchoring assignment and the release-step gap are computational (orthology, domain architecture, synteny). The strongest experimental anchor is in *P. aeruginosa*, not *P. putida*.
2. **k-mer/Smith–Waterman insensitivity to divergent homologs.** The conclusion that KT2440 lacks a DpaA ortholog could be a false negative if the release enzyme is structurally conserved but sequence-divergent. Profile-HMM and structure-based searches were not exhausted.
3. **PP_1451 function is genuinely unknown.** Its "fallback" status is by elimination, not positive evidence; it could be an anchoring enzyme, a release enzyme, or neither.
4. **OprI-as-covalent-substrate in KT2440 is inferred**, not shown biochemically for this strain; it rests on orthology to PAO1 OprI.
5. **Module GO vocabulary may be incomplete** — a specific lipoprotein–peptidoglycan cross-link hydrolase term may need to be requested.

---

## Proposed Follow-up Experiments / Actions

**Computational (immediate, low cost):**
- Run **profile-HMM (HMMER/InterPro) and structure-based (Foldseek/DALI)** searches for a DpaA-clade protein across the KT2440 proteome and the *Pseudomonas* pangenome, to convert `candidate_uncertain` into a confident `gap` or to recover a divergent release enzyme.
- Build a phylogeny of all *Pseudomonas* PF03734 proteins with *E. coli* LdtA–F as references, to place PP_1451/PA3756 definitively.
- AlphaFold-model PP_2320 and PP_1451; confirm the catalytic Cys and LysM placement in PP_2320.

**Experimental (to resolve gaps):**
- **Detect the covalent OprI–PG species** in KT2440 by muropeptide LC-MS/MS; test dependence on PP_2320 via a clean deletion (Δ*PP_2320*), directly confirming anchoring in the target strain.
- **Test PP_1451** for L,D-endopeptidase / tether-release activity in vitro and via Δ*PP_1451* muropeptide profiling; assess whether OprI release accumulates or is lost.
- **Complementation:** express *E. coli dpaA* in KT2440 to see whether an exogenous release enzyme alters OprI–PG turnover, testing the "release-not-required" hypothesis.

**Curation (now):**
- Detach module from `ppu00550`; add PP_2320 + PP_2322; register release step as `candidate_uncertain`/`gap`; promote PP_2320, PP_1451, PP_2322 to full gene review; flag the OprI-for-Lpp lineage-specific substrate substitution.

---

### Evidence-Type Summary

- **Direct experiment (target strain):** none identified for the module in *P. putida* KT2440.
- **Direct experiment (same genus, strong transfer):** PA2854→OprI anchoring in *P. aeruginosa* ([PMID: 42100858](https://pubmed.ncbi.nlm.nih.gov/42100858/)); OprI orthology.
- **Homology + domain + synteny (target strain):** PP_2320 anchoring assignment; PP_2322 substrate.
- **Inferred negative / gap:** absence of a confident DpaA/LdtF release ortholog in KT2440.


## Artifacts

- [OpenScientist final report](PSEPK__gram_negative_lipoprotein_peptidoglycan_tether_remodeling__ppu00550-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__gram_negative_lipoprotein_peptidoglycan_tether_remodeling__ppu00550-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:42100858
2. PMID:33947763
3. PMID:17369299
4. PMID:33139883