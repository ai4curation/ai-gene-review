---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T06:59:17.223624'
end_time: '2026-07-23T07:50:25.296611'
duration_seconds: 3068.07
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Aerobic phenylacetate catabolism
  module_summary: A reusable aerobic phenylacetyl-CoA pathway that activates phenylacetate,
    epoxidizes the aromatic ring with the multicomponent PaaABCDE system, isomerizes
    and hydrolytically opens the ring, oxidizes the resulting semialdehyde, and processes
    the open-chain CoA ester through a beta-oxidation-like sequence to acetyl-CoA
    and succinyl-CoA. Regulatory and detoxification proteins are outside the required
    reaction chain.
  module_outline: "- Aerobic phenylacetate catabolism\n  - 1. phenylacetate activation\n\
    \  - Phenylacetate activation to phenylacetyl-CoA\n    - Phenylacetate-CoA ligase\
    \ (molecular player: PSEPK canonical PaaK; activity or role: phenylacetate-CoA\
    \ ligase activity)\n  - 2. aromatic-ring epoxidation\n  - Ring 1,2-phenylacetyl-CoA\
    \ epoxidation\n    - PaaABCDE phenylacetyl-CoA epoxidase system (molecular player:\
    \ PaaABCDE phenylacetyl-CoA epoxidase system; activity or role: phenylacetyl-CoA\
    \ 1,2-epoxidase activity)\n  - 3. epoxide isomerization\n  - PaaG epoxide isomerization\n\
    \    - 1,2-epoxyphenylacetyl-CoA isomerase (molecular player: PSEPK canonical\
    \ PaaG)\n  - 4. hydrolytic ring opening and semialdehyde oxidation\n  - Bifunctional\
    \ PaaZ ring opening\n    - 1. oxepin-CoA hydrolysis\n    - Oxepin-CoA hydrolysis\n\
    \      - PaaZ oxepin-CoA hydrolase (molecular player: PSEPK PaaZ hydrolase domain)\n\
    \    - 2. semialdehyde oxidation\n    - PaaZ semialdehyde oxidation\n      - PaaZ\
    \ semialdehyde dehydrogenase (molecular player: PSEPK PaaZ dehydrogenase domain)\n\
    \  - 5. open-chain enoyl-CoA hydration\n  - PaaF open-chain hydration\n    - PaaF\
    \ enoyl-CoA hydratase (molecular player: PSEPK canonical PaaF; activity or role:\
    \ enoyl-CoA hydratase activity)\n  - 6. 3-hydroxyadipyl-CoA oxidation\n  - PaaH\
    \ 3-hydroxyadipyl-CoA oxidation\n    - PaaH 3-hydroxyacyl-CoA dehydrogenase (molecular\
    \ player: PSEPK canonical PaaH; activity or role: (3S)-3-hydroxyacyl-CoA dehydrogenase\
    \ (NAD+) activity)\n  - 7. 3-oxoadipyl-CoA thiolysis\n  - PaaJ 3-oxoadipyl-CoA\
    \ thiolysis\n    - PaaJ 3-oxoadipyl-CoA thiolase (molecular player: PSEPK canonical\
    \ PaaJ; activity or role: 3-oxoadipyl-CoA thiolase activity)"
  module_connections: '- Phenylacetate activation to phenylacetyl-CoA feeds into Ring
    1,2-phenylacetyl-CoA epoxidation: PaaK supplies phenylacetyl-CoA to the epoxidase
    system.

    - Ring 1,2-phenylacetyl-CoA epoxidation feeds into PaaG epoxide isomerization:
    The epoxidase product is rearranged by PaaG.

    - PaaG epoxide isomerization feeds into Bifunctional PaaZ ring opening: PaaG supplies
    the oxepin-CoA intermediate to PaaZ.

    - Bifunctional PaaZ ring opening feeds into PaaF open-chain hydration: PaaZ produces
    the open-chain unsaturated CoA ester.

    - PaaF open-chain hydration feeds into PaaH 3-hydroxyadipyl-CoA oxidation: PaaF
    produces 3-hydroxyadipyl-CoA for PaaH.

    - PaaH 3-hydroxyadipyl-CoA oxidation feeds into PaaJ 3-oxoadipyl-CoA thiolysis:
    PaaH produces 3-oxoadipyl-CoA for PaaJ.

    - Oxepin-CoA hydrolysis feeds into PaaZ semialdehyde oxidation: The hydrolase-domain
    product is oxidized by the dehydrogenase domain.'
  pathway_query: ppu00360
  pathway_id: ppu00360
  pathway_name: Phenylalanine metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00360 with 13 primary genes; module
    area: amino_acid_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '28'
  candidate_genes: '- hisC: PP_0967 | Q88P86 | Histidinol-phosphate aminotransferase
    (EC 2.6.1.9) (Imidazole acetol-phosphate transaminase) (EC 2.6.1.9; primary bucket
    kegg:ppu00401)

    - PP_1791: PP_1791 | Q88LY5 | Aldolase/synthase (primary bucket kegg:ppu00621)

    - tyrB: PP_1972 | Q88LG1 | Aminotransferase (EC 2.6.1.-) (EC 2.6.1.-; primary
    bucket kegg:ppu00401)

    - PP_2217: PP_2217 | Q88KS2 | enoyl-CoA hydratase (EC 4.2.1.17) (EC 4.2.1.17;
    primary bucket kegg:ppu00930)

    - PP_2552: PP_2552 | Q88JU5 | DOPA decarboxylase (EC 4.1.1.28) (EC 4.1.1.28; primary
    bucket kegg:ppu00350)

    - PP_2932: PP_2932 | Q88IR7 | Amidase family protein (primary bucket kegg:ppu00643)

    - paaZ: PP_3270 | Q88HT3 | Oxepin-CoA hydrolase/3-oxo-5,6-dehydrosuberyl-CoA semialdehyde
    dehydrogenase (EC 1.2.1.91, EC 3.3.2.12) (EC 1.2.1.91; 3.3.2.12; primary bucket
    kegg:ppu00360)

    - paaE: PP_3274 | Q88HS9 | Ring 1,2-phenylacetyl-CoA epoxidase, reductase subunit
    (EC 1.14.13.149) (EC 1.14.13.149; primary bucket kegg:ppu00360)

    - paaD: PP_3275 | Q88HS8 | Subunit of phenylacetate degradation enzyme (primary
    bucket kegg:ppu00360)

    - paaC: PP_3276 | Q88HS7 | Ring 1,2-phenylacetyl-CoA epoxidase beta subunit (EC
    1.14.13.149) (EC 1.14.13.149; primary bucket kegg:ppu00360)

    - paaB: PP_3277 | Q88HS6 | Ring 1,2-phenylacetyl-CoA epoxidase regulatory subunit
    (EC 1.14.13.149) (EC 1.14.13.149; primary bucket kegg:ppu00360)

    - paaA: PP_3278 | Q88HS5 | Ring 1,2-phenylacetyl-CoA epoxidase alpha subunit (EC
    1.14.13.149) (EC 1.14.13.149; primary bucket kegg:ppu00360)

    - paaK: PP_3279 | Q88HS4 | Phenylacetate-coenzyme A ligase (EC 6.2.1.30) (Phenylacetyl-CoA
    ligase) (EC 6.2.1.30; primary bucket kegg:ppu00360)

    - paaI: PP_3281 | Q88HS2 | Hydroxyphenylacetyl-CoA thioesterase (primary bucket
    kegg:ppu00360)

    - paaH: PP_3282 | Q88HS1 | 3-hydroxyadipyl-CoA dehydrogenase (EC 1.1.1.35) (EC
    1.1.1.35; primary bucket kegg:ppu00360)

    - paaG: PP_3283 | Q88HS0 | 1,2-epoxyphenylacetyl-CoA isomerase (EC 5.3.3.18) (EC
    5.3.3.18; primary bucket kegg:ppu00360)

    - paaF: PP_3284 | Q88HR9 | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) (EC 4.2.1.17;
    primary bucket kegg:ppu00930)

    - hpd: PP_3433 | Q88HC7 | 4-hydroxyphenylpyruvate dioxygenase (EC 1.13.11.27)
    (EC 1.13.11.27; primary bucket kegg:ppu00130)

    - peaE: PP_3463 | Q88H97 | Phenylacetaldehyde dehydrogenase (EC 1.2.1.39) (EC
    1.2.1.39; primary bucket kegg:ppu00643)

    - amaC: PP_3590 | Q88GX7 | Aminotransferase (EC 2.6.1.-) (EC 2.6.1.-; primary
    bucket kegg:ppu00401)

    - katG: PP_3668 | Q88GQ0 | Catalase-peroxidase (CP) (EC 1.11.1.21) (Peroxidase/catalase)
    (EC 1.11.1.21; primary bucket kegg:ppu00380)

    - PP_3726: PP_3726 | Q88GJ6 | Enoyl-CoA hydratase/isomerase family protein (primary
    bucket kegg:ppu00360)

    - hbd: PP_3755 | Q88GG9 | 3-hydroxybutyryl-CoA dehydrogenase (EC 1.1.1.157) (EC
    1.1.1.157; primary bucket kegg:ppu00360)

    - PP_4311: PP_4311 | Q88EY9 | D-amino acid dehydrogenase 2 small subunit (EC 1.4.99.6)
    (EC 1.4.99.6; primary bucket kegg:ppu00470)

    - dadA1: PP_4434 | Q88EM0 | D-amino acid dehydrogenase 1 (EC 1.4.99.-) (EC 1.4.99.-;
    primary bucket kegg:ppu00470)

    - phhA: PP_4490 | Q88EH3 | Phenylalanine-4-hydroxylase (EC 1.14.16.1) (Phe-4-monooxygenase)
    (EC 1.14.16.1; primary bucket kegg:ppu00360)

    - PP_4983: PP_4983 | Q88D45 | Tryptophan 2-monooxygenase (EC 1.13.12.3) (EC 1.13.12.3;
    primary bucket kegg:ppu00350)

    - dadA2: PP_5270 | Q88CB1 | D-amino acid dehydrogenase 2 (EC 1.4.99.-) (EC 1.4.99.-;
    primary bucket kegg:ppu00470)'
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
  path: PSEPK__phenylacetate_catabolism__ppu00360-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__phenylacetate_catabolism__ppu00360-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Aerobic phenylacetate catabolism in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00360
- Resolved ID: ppu00360
- Resolved name: Phenylalanine metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00360 with 13 primary genes; module area: amino_acid_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 28

- hisC: PP_0967 | Q88P86 | Histidinol-phosphate aminotransferase (EC 2.6.1.9) (Imidazole acetol-phosphate transaminase) (EC 2.6.1.9; primary bucket kegg:ppu00401)
- PP_1791: PP_1791 | Q88LY5 | Aldolase/synthase (primary bucket kegg:ppu00621)
- tyrB: PP_1972 | Q88LG1 | Aminotransferase (EC 2.6.1.-) (EC 2.6.1.-; primary bucket kegg:ppu00401)
- PP_2217: PP_2217 | Q88KS2 | enoyl-CoA hydratase (EC 4.2.1.17) (EC 4.2.1.17; primary bucket kegg:ppu00930)
- PP_2552: PP_2552 | Q88JU5 | DOPA decarboxylase (EC 4.1.1.28) (EC 4.1.1.28; primary bucket kegg:ppu00350)
- PP_2932: PP_2932 | Q88IR7 | Amidase family protein (primary bucket kegg:ppu00643)
- paaZ: PP_3270 | Q88HT3 | Oxepin-CoA hydrolase/3-oxo-5,6-dehydrosuberyl-CoA semialdehyde dehydrogenase (EC 1.2.1.91, EC 3.3.2.12) (EC 1.2.1.91; 3.3.2.12; primary bucket kegg:ppu00360)
- paaE: PP_3274 | Q88HS9 | Ring 1,2-phenylacetyl-CoA epoxidase, reductase subunit (EC 1.14.13.149) (EC 1.14.13.149; primary bucket kegg:ppu00360)
- paaD: PP_3275 | Q88HS8 | Subunit of phenylacetate degradation enzyme (primary bucket kegg:ppu00360)
- paaC: PP_3276 | Q88HS7 | Ring 1,2-phenylacetyl-CoA epoxidase beta subunit (EC 1.14.13.149) (EC 1.14.13.149; primary bucket kegg:ppu00360)
- paaB: PP_3277 | Q88HS6 | Ring 1,2-phenylacetyl-CoA epoxidase regulatory subunit (EC 1.14.13.149) (EC 1.14.13.149; primary bucket kegg:ppu00360)
- paaA: PP_3278 | Q88HS5 | Ring 1,2-phenylacetyl-CoA epoxidase alpha subunit (EC 1.14.13.149) (EC 1.14.13.149; primary bucket kegg:ppu00360)
- paaK: PP_3279 | Q88HS4 | Phenylacetate-coenzyme A ligase (EC 6.2.1.30) (Phenylacetyl-CoA ligase) (EC 6.2.1.30; primary bucket kegg:ppu00360)
- paaI: PP_3281 | Q88HS2 | Hydroxyphenylacetyl-CoA thioesterase (primary bucket kegg:ppu00360)
- paaH: PP_3282 | Q88HS1 | 3-hydroxyadipyl-CoA dehydrogenase (EC 1.1.1.35) (EC 1.1.1.35; primary bucket kegg:ppu00360)
- paaG: PP_3283 | Q88HS0 | 1,2-epoxyphenylacetyl-CoA isomerase (EC 5.3.3.18) (EC 5.3.3.18; primary bucket kegg:ppu00360)
- paaF: PP_3284 | Q88HR9 | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) (EC 4.2.1.17; primary bucket kegg:ppu00930)
- hpd: PP_3433 | Q88HC7 | 4-hydroxyphenylpyruvate dioxygenase (EC 1.13.11.27) (EC 1.13.11.27; primary bucket kegg:ppu00130)
- peaE: PP_3463 | Q88H97 | Phenylacetaldehyde dehydrogenase (EC 1.2.1.39) (EC 1.2.1.39; primary bucket kegg:ppu00643)
- amaC: PP_3590 | Q88GX7 | Aminotransferase (EC 2.6.1.-) (EC 2.6.1.-; primary bucket kegg:ppu00401)
- katG: PP_3668 | Q88GQ0 | Catalase-peroxidase (CP) (EC 1.11.1.21) (Peroxidase/catalase) (EC 1.11.1.21; primary bucket kegg:ppu00380)
- PP_3726: PP_3726 | Q88GJ6 | Enoyl-CoA hydratase/isomerase family protein (primary bucket kegg:ppu00360)
- hbd: PP_3755 | Q88GG9 | 3-hydroxybutyryl-CoA dehydrogenase (EC 1.1.1.157) (EC 1.1.1.157; primary bucket kegg:ppu00360)
- PP_4311: PP_4311 | Q88EY9 | D-amino acid dehydrogenase 2 small subunit (EC 1.4.99.6) (EC 1.4.99.6; primary bucket kegg:ppu00470)
- dadA1: PP_4434 | Q88EM0 | D-amino acid dehydrogenase 1 (EC 1.4.99.-) (EC 1.4.99.-; primary bucket kegg:ppu00470)
- phhA: PP_4490 | Q88EH3 | Phenylalanine-4-hydroxylase (EC 1.14.16.1) (Phe-4-monooxygenase) (EC 1.14.16.1; primary bucket kegg:ppu00360)
- PP_4983: PP_4983 | Q88D45 | Tryptophan 2-monooxygenase (EC 1.13.12.3) (EC 1.13.12.3; primary bucket kegg:ppu00350)
- dadA2: PP_5270 | Q88CB1 | D-amino acid dehydrogenase 2 (EC 1.4.99.-) (EC 1.4.99.-; primary bucket kegg:ppu00470)

## Generic Module Context

### Working Scope

A reusable aerobic phenylacetyl-CoA pathway that activates phenylacetate, epoxidizes the aromatic ring with the multicomponent PaaABCDE system, isomerizes and hydrolytically opens the ring, oxidizes the resulting semialdehyde, and processes the open-chain CoA ester through a beta-oxidation-like sequence to acetyl-CoA and succinyl-CoA. Regulatory and detoxification proteins are outside the required reaction chain.

### Provisional Biological Outline

- Aerobic phenylacetate catabolism
  - 1. phenylacetate activation
  - Phenylacetate activation to phenylacetyl-CoA
    - Phenylacetate-CoA ligase (molecular player: PSEPK canonical PaaK; activity or role: phenylacetate-CoA ligase activity)
  - 2. aromatic-ring epoxidation
  - Ring 1,2-phenylacetyl-CoA epoxidation
    - PaaABCDE phenylacetyl-CoA epoxidase system (molecular player: PaaABCDE phenylacetyl-CoA epoxidase system; activity or role: phenylacetyl-CoA 1,2-epoxidase activity)
  - 3. epoxide isomerization
  - PaaG epoxide isomerization
    - 1,2-epoxyphenylacetyl-CoA isomerase (molecular player: PSEPK canonical PaaG)
  - 4. hydrolytic ring opening and semialdehyde oxidation
  - Bifunctional PaaZ ring opening
    - 1. oxepin-CoA hydrolysis
    - Oxepin-CoA hydrolysis
      - PaaZ oxepin-CoA hydrolase (molecular player: PSEPK PaaZ hydrolase domain)
    - 2. semialdehyde oxidation
    - PaaZ semialdehyde oxidation
      - PaaZ semialdehyde dehydrogenase (molecular player: PSEPK PaaZ dehydrogenase domain)
  - 5. open-chain enoyl-CoA hydration
  - PaaF open-chain hydration
    - PaaF enoyl-CoA hydratase (molecular player: PSEPK canonical PaaF; activity or role: enoyl-CoA hydratase activity)
  - 6. 3-hydroxyadipyl-CoA oxidation
  - PaaH 3-hydroxyadipyl-CoA oxidation
    - PaaH 3-hydroxyacyl-CoA dehydrogenase (molecular player: PSEPK canonical PaaH; activity or role: (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity)
  - 7. 3-oxoadipyl-CoA thiolysis
  - PaaJ 3-oxoadipyl-CoA thiolysis
    - PaaJ 3-oxoadipyl-CoA thiolase (molecular player: PSEPK canonical PaaJ; activity or role: 3-oxoadipyl-CoA thiolase activity)

### Known Relationships Among Steps

- Phenylacetate activation to phenylacetyl-CoA feeds into Ring 1,2-phenylacetyl-CoA epoxidation: PaaK supplies phenylacetyl-CoA to the epoxidase system.
- Ring 1,2-phenylacetyl-CoA epoxidation feeds into PaaG epoxide isomerization: The epoxidase product is rearranged by PaaG.
- PaaG epoxide isomerization feeds into Bifunctional PaaZ ring opening: PaaG supplies the oxepin-CoA intermediate to PaaZ.
- Bifunctional PaaZ ring opening feeds into PaaF open-chain hydration: PaaZ produces the open-chain unsaturated CoA ester.
- PaaF open-chain hydration feeds into PaaH 3-hydroxyadipyl-CoA oxidation: PaaF produces 3-hydroxyadipyl-CoA for PaaH.
- PaaH 3-hydroxyadipyl-CoA oxidation feeds into PaaJ 3-oxoadipyl-CoA thiolysis: PaaH produces 3-oxoadipyl-CoA for PaaJ.
- Oxepin-CoA hydrolysis feeds into PaaZ semialdehyde oxidation: The hydrolase-domain product is oxidized by the dehydrogenase domain.

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

# Species-Aware Module Review: Aerobic Phenylacetate Catabolism in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Module:** Aerobic phenylacetyl-CoA catabolic pathway (generic module `amino_acid_metabolism` / local bucket `kegg:ppu00360`)
**Curation intent:** Manual module satisfiability + gene-annotation review (not a generic pathway essay)

---

## 1. Executive Summary

The aerobic phenylacetyl-CoA (paa) catabolic module is **fully satisfiable** in *P. putida* KT2440. All seven core reaction steps are encoded by a single, non-redundant, co-localized gene cluster spanning **PP_3270–PP_3284** (paaZ, paaABCDE, paaK, paaJ, paaI, paaH, paaG, paaF). The architecture is gene-for-gene homologous to the canonical *E. coli* W `paaZ / paaABCDEFGHIJK` catabolon (Ferrández et al. 1998, PMID 9748275), and the activation step plus operon regulation are **directly validated in KT2440 itself** (Kim et al. 2009, PMID 19406896).

Two curation actions dominate this review:

1. **Add the missing thiolase.** Module step 7 (3-oxoadipyl-CoA thiolysis) has **no candidate** in the local metadata, yet the covering gene clearly exists: **PP_3280 = paaJ, EC 2.3.1.174**, sitting inside the cluster between paaK and paaI. Mark step 7 **covered**, not a gap.
2. **Prune over-propagated candidates.** Only 13 of 28 candidate genes belong to the core chain. The other ~15 are peripheral or over-propagated from the umbrella KEGG *Phenylalanine metabolism* map (ppu00360) and neighboring beta-oxidation / aromatic amino-acid maps.

No lineage-specific alternatives or new GO terms are required; the pathway is the textbook version. The main caveat is that all KT2440 paa proteins are **UniProt TrEMBL (unreviewed)** — EC/subunit calls are automatic annotations anchored by synteny and *E. coli* homology.

---

## 2. Target-Organism Pathway Definition

**What is included (pathway boundary):** activation of free phenylacetate to phenylacetyl-CoA, followed by *aerobic, CoA-dependent, epoxide/oxepin ring cleavage* and a beta-oxidation-like processing of the ring-opened CoA ester down to acetyl-CoA + succinyl-CoA (TCA entry). This is a **non-oxygenolytic-of-the-free-ring** strategy: the ring is epoxidized *while thioesterified to CoA*, distinguishing it from classical ring-hydroxylating dioxygenase routes.

**Neighboring processes to keep OUT of this module:**
- **Phenylalanine → phenylacetate feeder chemistry** (phhA Phe-4-hydroxylase; aromatic aminotransferases; phenylacetaldehyde dehydrogenase peaE). These *supply the substrate* but are not the CoA pathway.
- **Tyrosine/homogentisate catabolism** (hpd, PP_3433). Separate KEGG map ppu00130.
- **β-Ketoadipate / protocatechuate pathway** (pcaF, PP_1377) — shares EC 2.3.1.174 with paaJ but is a different pathway.
- **Generic fatty-acid β-oxidation** (fadA, PP_2217, PP_3726, hbd/PP_3755) — crotonase/thiolase-superfamily paralogs.

**Alternate names / DB definitions:** "phenylacetic acid (PA) degradation", "phenylacetyl-CoA catabolon", "PA-CoA pathway". KEGG module **M00878** (phenylacetate degradation, PA-CoA pathway) is the correct module-level analogue; the local bucket points instead at the broad map **ppu00360 (Phenylalanine metabolism)**, which is why so many peripheral genes were pulled in. **Recommendation: retarget the local bucket from ppu00360 to the paa-specific module (KEGG M00878 / MetaCyc PWY-1341 "phenylacetate degradation I aerobic").**

---

## 3. Expected Step Model → Coverage in KT2440

| # | Module step | Enzyme / EC | KT2440 gene | Status |
|---|-------------|-------------|-------------|--------|
| 1 | Phenylacetate activation | phenylacetate-CoA ligase, EC 6.2.1.30 | **paaK / PP_3279** | **covered** (direct in-strain activity, PMID 19406896) |
| 2 | Ring 1,2-epoxidation | phenylacetyl-CoA epoxidase (multicomponent), EC 1.14.13.149 | **paaA/B/C/D/E / PP_3278/3277/3276/3275/3274** | **covered** |
| 3 | Epoxide isomerization | 1,2-epoxyphenylacetyl-CoA isomerase, EC 5.3.3.18 | **paaG / PP_3283** | **covered** |
| 4a | Oxepin-CoA hydrolysis (ring opening) | oxepin-CoA hydrolase, EC 3.3.2.12 | **paaZ / PP_3270** (hydrolase domain) | **covered** |
| 4b | Semialdehyde oxidation | aldehyde dehydrogenase, EC 1.2.1.91 | **paaZ / PP_3270** (ALDH domain, bifunctional) | **covered** |
| 5 | Open-chain enoyl-CoA hydration | enoyl-CoA hydratase, EC 4.2.1.17 | **paaF / PP_3284** | **covered** |
| 6 | 3-hydroxyadipyl-CoA oxidation | 3-hydroxyacyl-CoA dehydrogenase, EC 1.1.1.35 | **paaH / PP_3282** | **covered** |
| 7 | 3-oxoadipyl-CoA thiolysis | 3-oxoadipyl-CoA thiolase, EC 2.3.1.174 | **paaJ / PP_3280** | **covered — but MISSING from candidate metadata (gap in bucket, not in genome)** |

**Accessory (in cluster, not a required step):** paaI / PP_3281 (thioesterase, EC 3.1.2.-) — proofreading/editing thioesterase that hydrolyzes off-pathway CoA intermediates; keep as cluster context, mark **covered/accessory**, not a core step.

Every required step is present. **Module satisfiability = SATISFIED.**

---

## 4. Candidate Genes and Evidence

### 4A. Core cluster genes (high confidence — all TrEMBL, synteny + *E. coli* homology)

| Gene | Locus | UniProt | Role | Evidence type | Curation note |
|------|-------|---------|------|---------------|---------------|
| paaK | PP_3279 | Q88HS4 | PA-CoA ligase (EC 6.2.1.30) | **Direct KT2440** enzyme activity (PMID 19406896) + homology | Single copy; no auxiliary ligase. Nomenclature caveat: ligase = *paaF* in *Pseudomonas* sp. Y2 (PMID 18544072) — map by EC, not letter |
| paaA | PP_3278 | Q88HS5 | epoxidase α (EC 1.14.13.149) | Homology + synteny | Catalytic diiron oxygenase subunit |
| paaB | PP_3277 | Q88HS6 | epoxidase regulatory/structural | Homology + synteny | 93 aa small subunit |
| paaC | PP_3276 | Q88HS7 | epoxidase β (EC 1.14.13.149) | Homology + synteny | |
| paaD | PP_3275 | Q88HS8 | epoxidase component (Fe-S) | Homology + synteny | No EC in UniProt; "subunit of phenylacetate degradation enzyme" |
| paaE | PP_3274 | Q88HS9 | epoxidase reductase (EC 1.14.13.149) | Homology + synteny | NAD(P)H:ferredoxin-type reductase |
| paaG | PP_3283 | Q88HS0 | epoxide→oxepin isomerase (EC 5.3.3.18) | Homology + synteny | Crotonase superfamily |
| paaZ | PP_3270 | Q88HT3 | **bifunctional** oxepin-CoA hydrolase (EC 3.3.2.12) + ALDH (EC 1.2.1.91) | Homology + synteny | 684 aa two-domain; covers steps 4a & 4b |
| paaF | PP_3284 | Q88HR9 | enoyl-CoA hydratase (EC 4.2.1.17) | Homology + synteny | Cluster copy; paralogs elsewhere (see 5) |
| paaH | PP_3282 | Q88HS1 | 3-hydroxyacyl-CoA DH (EC 1.1.1.35) | Homology + synteny | 505 aa |
| **paaJ** | **PP_3280** | **Q88HS3** | **3-oxoadipyl-CoA thiolase (EC 2.3.1.174)** | Homology + synteny | **Not in candidate list — ADD IT** |
| paaI | PP_3281 | Q88HS2 | editing thioesterase | Homology + synteny | Accessory, not a core step |

### 4B. Peripheral / feeder genes (exclude from core chain)

- **peaE / PP_3463** (phenylacetaldehyde dehydrogenase, EC 1.2.1.39): legitimate **upstream feeder** — oxidizes phenylacetaldehyde (from 2-phenylethylamine / styrene) to phenylacetate, the *substrate* of step 1. Flag as `feeder / peripheral`, not core.
- **phhA / PP_4490** (Phe-4-hydroxylase, EC 1.14.16.1; GO:0006559 L-Phe catabolic process): routes Phe → Tyr; belongs to phenylalanine→tyrosine and downstream tyrosine catabolism. Peripheral.
- **hpd / PP_3433** (4-HPP dioxygenase): tyrosine/homogentisate pathway (ppu00130). Not this module.
- **tyrB / PP_1972, hisC / PP_0967, amaC / PP_3590** (aminotransferases, broad EC 2.6.1.-): broad transaminase over-propagation; not paa.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

**Genuine metadata gap (genome-covered):**
- **Step 7 thiolase paaJ / PP_3280** absent from candidate list. Highest-priority fix. Genome status = covered.

**Paralog ambiguity (resolve by cluster membership + EC, never by EC alone):**
- **Hydratase step (paaF, EC 4.2.1.17):** genome paralogs **PP_2217** and **PP_3726** are generic crotonase-superfamily enzymes (GO:0006635 fatty-acid β-oxidation), NOT cluster-resident. Do **not** assign them to the paa hydration step. `candidate_uncertain` if considered at all; correct assignment is PP_3284.
- **Thiolase step (paaJ, EC 2.3.1.174):** shared with **pcaF-I / PP_1377** (β-ketoadipyl-CoA thiolase of the protocatechuate/β-ketoadipate pathway). Only **PP_3280** belongs to paa.

**Likely over-annotation / noise in the candidate set (from broad ppu00360 map or shared EC):**
- PP_1791 (aldolase/synthase), PP_2552 (DOPA decarboxylase), PP_2932 (amidase), katG (PP_3668, catalase-peroxidase = detox), hbd (PP_3755), PP_4983 (Trp 2-monooxygenase), dadA1/dadA2/PP_4311 (D-amino-acid dehydrogenases, ppu00470). None participate in aerobic phenylacetyl-CoA catabolism.

**Confidence caveat:** every KT2440 paa protein is **TrEMBL (unreviewed)**. EC numbers and subunit roles are automatic annotations; confidence rests on (i) tight cluster synteny, (ii) gene-for-gene homology to experimentally characterized *E. coli* W paa proteins, and (iii) direct KT2440 physiology for the activation step and operon regulation.

---

## 6. Module and GO-Curation Recommendations

**Per-step disposition:**
- Steps 1, 2, 3, 4a, 4b, 5, 6 → **covered**.
- Step 7 (thiolysis) → **covered** after adding PP_3280/paaJ (currently would falsely read as **gap**).
- paaI/PP_3281 → **covered/accessory** (not a required reaction step).

**Module boundary:**
- The generic module boundary is **correct** for this organism (canonical pathway, no lineage-specific rewiring). No `module_needs_revision` on biology grounds.
- **However, the local bucket is mis-targeted:** `kegg:ppu00360` (broad Phenylalanine metabolism) is the reason ~15 spurious candidates appeared. **Recommend re-anchoring to the paa-specific module (KEGG M00878 / MetaCyc PWY-1341).** This is a metadata/bucket fix, not a biological revision.

**GO / new-document needs:**
- No new GO *terms* need to be created — all activities have existing GO/EC coverage (e.g., GO:0010124 phenylacetate catabolic process; EC 1.14.13.149, 5.3.3.18, 3.3.2.12, 1.2.1.91).
- **But GO *annotation* of the cluster is uneven and should be fixed.** A UniProt GO-BP scan shows only paaK, paaA, paaC, paaE, paaG, paaH, paaJ carry `phenylacetate catabolic process`, while **paaZ (PP_3270) has no biological-process GO at all**, and **paaF (PP_3284) is tagged only `fatty acid beta-oxidation`**; paaB (PP_3277), paaD (PP_3275), paaI (PP_3281) also lack it. Request `GO:0010124 phenylacetate catabolic process` annotations for **paaZ, paaF, paaB, paaD, paaI**.
- **Root cause of the dropped thiolase:** paaJ/PP_3280 additionally carries an over-propagated `3,4-dihydroxybenzoate (protocatechuate) catabolic process` GO (from pcaF/PP_1377 paralogy) — this cross-annotation is almost certainly why PP_3280 was bucketed away from ppu00360 and omitted from the candidate list. Review/curate that GO on PP_3280 to prevent recurrence.

**Not-expected-in-taxon:** none — the full pathway is expected and present.

---

## 7. Genes to Promote to Full `fetch-gene` Review

**High priority:**
1. **PP_3280 / paaJ** — add to module as the step-7 thiolase; verify EC 2.3.1.174 and disambiguate from pcaF (PP_1377).
2. **PP_3270 / paaZ** — confirm bifunctional domain architecture (hydrolase EC 3.3.2.12 + ALDH EC 1.2.1.91) so steps 4a/4b are correctly attributed to one gene.

**Medium priority (paralog disambiguation):**
3. **PP_3284 / paaF** vs paralogs **PP_2217**, **PP_3726** — lock the hydration step to the cluster copy.
4. **PP_3275 / paaD** — obtain/confirm functional annotation (no EC in UniProt).

**Low priority (boundary confirmation):** peaE/PP_3463 as a documented feeder; explicit exclusion of phhA, hpd, tyrB, hisC, amaC.

---

## 8. Key References

- **Ferrández et al. 1998**, *J Biol Chem* 273:25974–25986. PMID **9748275**. Defines the *E. coli* W `paaZ / paaABCDEFGHIJK` catabolon, PaaK ligase, PaaABCDE oxygenase, PaaZ third step, PaaFGHIJ β-oxidation-like segment, PaaX regulation. *Homology anchor for KT2440 (strong transfer: gene-for-gene syntenic cluster).*
- **Kim et al. 2009**, *Environ Microbiol / J Bacteriol* work in KT2440. PMID **19406896**. *Direct target-strain evidence:* phenylacetyl-CoA ligase activity, PaaX-repressed paa operon, KDPG-mediated carbon catabolite repression of PAA metabolism.
- **Mohamed et al. 2002**, *J Bacteriol* 184:1953–1963. PMID **12189419**. *Azoarcus evansii* paaYZGHIKABCDE cluster; PA activation to PA-CoA; broad conservation across bacteria. *Related-organism support (moderate transfer).* 
- **del Peso-Santos et al. 2008**, *J Bacteriol*. PMID **18544072**. *Pseudomonas* sp. Y2: PaaX/StyR regulation and paaF-named ligases; documents cross-organism gene-letter inconsistency (ligase called *paaF*). *Nomenclature caveat.*
- Pathway/module resources: KEGG map **ppu00360** (broad, current bucket), KEGG module **M00878** / MetaCyc **PWY-1341** (correct paa-specific target); UniProt proteome **UP000000556**.

---

### Bottom line for curators
Mark the module **SATISFIED**. Make one substantive addition (**PP_3280/paaJ** at step 7), retarget the bucket from the broad ppu00360 map to the paa-specific module, and prune the ~15 peripheral/over-propagated candidates. All KT2440 paa annotations are unreviewed (TrEMBL) but strongly supported by cluster synteny, *E. coli* homology, and direct KT2440 physiology for the activation/regulation steps.


## Artifacts

- [OpenScientist final report](PSEPK__phenylacetate_catabolism__ppu00360-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__phenylacetate_catabolism__ppu00360-deep-research-openscientist_artifacts/final_report.pdf)