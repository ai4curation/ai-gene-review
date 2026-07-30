---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ACTL7A
affinage_run_date: 2026-06-09T22:02:40
uniprot_accession: Q9Y615
self_evaluation_pairwise: win
faith_pct: 83.33333333333333
n_discoveries: 14
citation_count: 14
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ACTL7A (human)

## Current model (mechanistic narrative)

ACTL7A is a testis-enriched actin-like protein essential for acrosome biogenesis and sperm head shaping during spermiogenesis [PMID:36734600]. It localizes dynamically to the nucleus and subacrosomal space of developing spermatids and later to postacrosomal regions, where it drives formation of subacrosomal filamentous actin and anchors the acrosome to the nucleus via the acroplaxome; its loss abolishes subacrosomal F-actin, causes abnormal acrosomal granule migration, and produces peeling, detached acrosomes [PMID:36734600]. ACTL7A operates within a perinuclear theca cytoskeletal network, co-immunoprecipitating with the zona-pellucida-binding protein ZPBP and being stabilized by FNDC8, whose depletion destabilizes ACTL7A and disrupts head morphogenesis [PMID:35921706, PMID:41169243]. Disruption of the acrosome-acroplaxome-manchette complex upon ACTL7A loss yields small-headed sperm, accompanied by dysregulation of the PI3K/AKT/mTOR/autophagy axis and PDLIM1 accumulation that impairs manchette development [PMID:37667331]. A central downstream consequence of ACTL7A dysfunction is mislocalization, reduced expression, or co-discharge of the sperm-borne oocyte activation factor PLCζ (PLCZ1), which abolishes oocyte calcium oscillations and causes total fertilization failure [PMID:32923619, PMID:35863052]. Loss-of-function and missense mutations in ACTL7A cause male infertility through acrosomal and perinuclear theca ultrastructural defects and oocyte activation deficiency, a phenotype rescuable by artificial oocyte activation [PMID:32923619, PMID:34727571].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0008092 cytoskeletal protein binding, GO:0005198 structural molecule activity
- **localization:** GO:0005634 nucleus, GO:0005856 cytoskeleton
- **pathway (Reactome):** R-HSA-1474165 Reproduction
- **partners:** ZPBP, FNDC8, CCIN, ACTRT1, ACTRT2, ARPM1
- **complexes:** acroplaxome, perinuclear theca cytoskeletal network, acrosome-acroplaxome-manchette complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1999 | Medium | ACTL7A encodes a 435-amino-acid actin-like protein (predicted MW 48.6 kDa) expressed in multiple adult tissues, with the gene located intronless on chromosome 9q31 in a head-to-head orientation with ACTL7B on a common 8-kb HindIII fragment. | PMID:10373328 | Genomics |
| 2012 | Medium | ACTL7A expression is upregulated via the PKA pathway and undergoes relocalization (remodeling) during the early period of capacitation in mouse spermatozoa, indicating it is an essential component of sperm capacitation. | PMID:23211711 | Fertility and sterility |
| 2012 | Medium | Anti-ACTL7A antibodies cause sperm agglutination and reduce fertilizing capacity of mouse spermatozoa in vitro; active immunization of mice with ACTL7A protein significantly reduces fertility, establishing ACTL7A as a target antigen in immunologic infertility. | PMID:22386842 | Fertility and sterility |
| 2020 | High | A homozygous missense mutation in ACTL7A causes acrosomal ultrastructural defects in sperm and leads to reduced expression and abnormal localization of PLCζ in sperm, resulting in failure of oocyte activation and early embryonic arrest. Artificial oocyte activation rescues the fertilization defect. | PMID:32923619 | Science advances |
| 2021 | Medium | Compound heterozygous loss-of-function variants in ACTL7A cause ultrastructural defects in the acrosome and perinuclear theca, and significantly reduce expression of both ACTL7A protein and PLCζ in sperm, leading to oocyte activation deficiency and total fertilization failure. | PMID:34727571 | Human reproduction |
| 2022 | Medium | In Actl7a knockout mice, sperm show malformed acrosomes, altered localization of zona pellucida binding protein ZPBP, and reduced calcium oscillations in oocytes due to abnormal localization and expression of PLCZ1; ACTL7A and ZPBP co-immunoprecipitate, forming a complex potentially involved in acrosomal formation. | PMID:35921706 | Biochemical and biophysical research communications |
| 2022 | High | A pathogenic variant in ACTL7A (p.Gly402Ser) causes mutant ACTL7A to fail to attach to the acroplaxome and be discharged via cytoplasmic droplets, resulting in absence of ACTL7A from epididymal sperm, acrosome detachment from the nuclear membrane (bubble-shaped acrosomes), and PLCζ co-discharge leading to total fertilization failure. Immunoprecipitation-mass spectrometry identified interacting proteins involved in acrosome assembly and actin filament organization. | PMID:35863052 | Molecular human reproduction |
| 2022 | Medium | A homozygous missense mutation p.D75A in ACTL7A causes protein degradation in sperm, irregular perinuclear theca and acrosomal ultrastructural defects, and abnormal localization and reduced expression of PLCZ1; 3D structural modeling shows loss of a hydrogen bond with Ser170 and transformation of an α-helix to random coil. | PMID:36574082 | Molecular genetics and genomics |
| 2023 | High | ACTL7A is dynamically localized within the nucleus and subacrosomal space of developing spermatids, and later associates with postacrosomal regions. Actl7a knockout mice show complete loss of subacrosomal filamentous actin (F-actin) structures, abnormal acrosomal granule migration, and peeling acrosomes during spermatid elongation, establishing ACTL7A as required for subacrosomal F-actin formation and acrosomal anchoring via the acroplaxome. | PMID:36734600 | Molecular human reproduction |
| 2023 | Medium | Loss of ACTL7A disrupts the acrosome-acroplaxome-manchette complex, causing small head sperm. Proteomic analysis of Actl7a-KO testes reveals enrichment of differentially expressed proteins in the PI3K/AKT/mTOR pathway; autophagy inhibition via PI3K/AKT/mTOR activation leads to PDLIM1 accumulation, impairing manchette development and sperm head shaping. | PMID:37667331 | Reproductive biology and endocrinology |
| 2023 | Medium | ACTL7A variants affecting the actin domain cause absent ACTL7A protein in spermatozoa and near-absent PLCζ1, along with attenuated and unevenly distributed acrosomal PNA signals, indicating acrosome dysfunction and oocyte activation failure. | PMID:37991128 | Andrology |
| 2024 | Low | In the absence of ACTL7A (or ACTL7B), intranuclear localization of HDAC1 and HDAC3 is lost in spermatids, implicating ACTL7A in nuclear HDAC association and epigenetic regulation during spermiogenesis. In silico modeling predicts ACTL7A can bind to HSA domains of INO80 and SWI/SNF nucleosome remodeler family members in a manner analogous to nuclear actin and ACTL6A, suggesting ARP subunit swapping in chromatin regulatory complexes. | PMID:38464253 | bioRxiv |
| 2025 | Medium | FNDC8 interacts with ACTL7A (and CCIN) in the perinuclear theca during spermiogenesis; depletion of FNDC8 destabilizes ACTL7A protein levels, establishing ACTL7A as part of a protein complex within the perinuclear theca that maintains structural integrity for sperm head morphogenesis. | PMID:41169243 | Zoological research |
| 2025 | Low | ACTL7A co-immunoprecipitates with the perinuclear theca proteins ACTRT1, ACTRT2, and ARPM1, and with the sperm surface protein ZPBP, placing ACTL7A within a cytoskeletal network in the perinuclear theca that connects the acrosome and nucleus. | PMID:bio_10.1101_2025.03.27.645694 | bioRxiv |

## Citations

- PMID:10373328
- PMID:22386842
- PMID:23211711
- PMID:32923619
- PMID:34727571
- PMID:35863052
- PMID:35921706
- PMID:36574082
- PMID:36734600
- PMID:37667331
- PMID:37991128
- PMID:38464253
- PMID:41169243
- PMID:bio_10.1101_2025.03.27.645694
