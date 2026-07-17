---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T07:08:53.573897'
end_time: '2026-07-17T07:45:31.920880'
duration_seconds: 2198.35
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: L-valine, L-leucine, and L-isoleucine biosynthesis
  module_summary: Microbial biosynthesis of the three branched-chain amino acids.
    L-isoleucine synthesis begins with threonine deamination to 2-oxobutanoate. The
    IlvI-IlvH acetohydroxy-acid synthase, IlvC ketol-acid reductoisomerase, and IlvD
    dihydroxy-acid dehydratase then form a shared catalytic trunk that processes either
    the valine precursor derived from two pyruvate molecules or the isoleucine precursor
    derived from pyruvate plus 2-oxobutanoate. The valine intermediate 2-oxoisovalerate
    also enters a three-reaction LeuA/LeuC-LeuD/LeuB extension branch. IlvE performs
    the terminal transamination for all three products. The module requires each biochemical
    step but allows any validated member of the biosynthetic threonine-deaminase family
    to satisfy the entry reaction.
  module_outline: "- branched-chain amino acid biosynthesis\n  - 1. isoleucine-branch\
    \ 2-oxobutanoate supply\n  - L-threonine to 2-oxobutanoate\n    - Biosynthetic\
    \ threonine deaminase (molecular player: full-length biosynthetic threonine deaminase\
    \ family; activity or role: threonine deaminase activity)\n  - 2. acetohydroxy-acid\
    \ formation\n  - Acetohydroxy-acid synthase complex\n    - IlvI acetohydroxy-acid\
    \ synthase catalytic subunit (molecular player: biosynthetic acetohydroxy-acid\
    \ synthase large subunit; activity or role: acetolactate synthase activity)\n\
    \    - IlvH acetohydroxy-acid synthase regulatory subunit (molecular player: biosynthetic\
    \ acetohydroxy-acid synthase small subunit; activity or role: acetolactate synthase\
    \ regulator activity)\n  - 3. acetohydroxy-acid reduction and rearrangement\n\
    \  - Acetohydroxy acids to dihydroxy acids\n    - IlvC ketol-acid reductoisomerase\
    \ (molecular player: type I ketol-acid reductoisomerase family; activity or role:\
    \ ketol-acid reductoisomerase activity)\n  - 4. branched-chain 2-oxoacid formation\n\
    \  - Dihydroxy acids to branched-chain 2-oxoacids\n    - IlvD dihydroxy-acid dehydratase\
    \ (molecular player: biosynthetic dihydroxy-acid dehydratase family; activity\
    \ or role: dihydroxy-acid dehydratase activity)\n  - 5. leucine-specific carbon-chain\
    \ extension\n  - 2-Oxoisovalerate to 2-oxoisocaproate\n    - 1. committed leucine-branch\
    \ condensation\n    - 2-Oxoisovalerate to 2-isopropylmalate\n      - LeuA 2-isopropylmalate\
    \ synthase (molecular player: LeuA 2-isopropylmalate synthase family; activity\
    \ or role: 2-isopropylmalate synthase activity)\n    - 2. isopropylmalate isomerization\n\
    \    - 2-Isopropylmalate to 3-isopropylmalate\n      - LeuC 3-isopropylmalate\
    \ dehydratase large subunit (molecular player: 3-isopropylmalate dehydratase large\
    \ subunit family; activity or role: 3-isopropylmalate dehydratase activity)\n\
    \      - LeuD 3-isopropylmalate dehydratase small subunit (molecular player: 3-isopropylmalate\
    \ dehydratase small subunit family; activity or role: 3-isopropylmalate dehydratase\
    \ activity)\n    - 3. leucine-branch 2-oxoacid formation\n    - 3-Isopropylmalate\
    \ to 2-oxoisocaproate\n      - LeuB 3-isopropylmalate dehydrogenase (molecular\
    \ player: 3-isopropylmalate dehydrogenase family; activity or role: 3-isopropylmalate\
    \ dehydrogenase activity)\n  - 6. terminal transamination of all three branches\n\
    \  - Branched-chain 2-oxoacids to L-valine, L-leucine, and L-isoleucine\n    -\
    \ IlvE branched-chain amino-acid aminotransferase (molecular player: IlvE branched-chain\
    \ amino-acid aminotransferase family; activity or role: branched-chain-amino-acid:2-oxoglutarate\
    \ transaminase activity)"
  module_connections: '- L-threonine to 2-oxobutanoate precedes Acetohydroxy-acid
    synthase complex

    - Acetohydroxy-acid synthase complex precedes Acetohydroxy acids to dihydroxy
    acids

    - Acetohydroxy acids to dihydroxy acids precedes Dihydroxy acids to branched-chain
    2-oxoacids

    - Dihydroxy acids to branched-chain 2-oxoacids precedes 2-Oxoisovalerate to 2-oxoisocaproate

    - Dihydroxy acids to branched-chain 2-oxoacids precedes Branched-chain 2-oxoacids
    to L-valine, L-leucine, and L-isoleucine

    - 2-Oxoisovalerate to 2-oxoisocaproate precedes Branched-chain 2-oxoacids to L-valine,
    L-leucine, and L-isoleucine

    - 2-Oxoisovalerate to 2-isopropylmalate precedes 2-Isopropylmalate to 3-isopropylmalate

    - 2-Isopropylmalate to 3-isopropylmalate precedes 3-Isopropylmalate to 2-oxoisocaproate'
  pathway_query: ppu00290
  pathway_id: ppu00290
  pathway_name: Valine, leucine and isoleucine biosynthesis
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00290 with 11 primary genes; module
    area: amino_acid_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '18'
  candidate_genes: '- leuA: PP_1025 | Q88P28 | 2-isopropylmalate synthase (EC 2.3.3.13)
    (Alpha-IPM synthase) (Alpha-isopropylmalate synthase) (EC 2.3.3.13; primary bucket
    kegg:ppu00290)

    - PP_1157: PP_1157 | Q877U6 | Acetolactate synthase (primary bucket kegg:ppu00660)

    - PP_1394: PP_1394 | Q88N22 | Acetolactate synthase, large subunit (primary bucket
    kegg:ppu00660)

    - alaA: PP_1872 | Q88LQ7 | Glutamate-pyruvate aminotransferase AlaA (EC 2.6.1.2)
    (EC 2.6.1.2; primary bucket kegg:ppu00290)

    - leuC: PP_1985 | Q88LE8 | 3-isopropylmalate dehydratase large subunit (EC 4.2.1.33)
    (Alpha-IPM isomerase) (IPMI) (Isopropylmalate isomerase) (EC 4.2.1.33; primary
    bucket kegg:ppu00660)

    - leuD: PP_1986 | Q88LE7 | 3-isopropylmalate dehydratase small subunit (EC 4.2.1.33)
    (Alpha-IPM isomerase) (IPMI) (Isopropylmalate isomerase) (EC 4.2.1.33; primary
    bucket kegg:ppu00660)

    - leuB: PP_1988 | Q88LE5 | 3-isopropylmalate dehydrogenase (EC 1.1.1.85) (3-IPM-DH)
    (Beta-IPM dehydrogenase) (IMDH) (EC 1.1.1.85; primary bucket kegg:ppu00660)

    - PP_2930: PP_2930 | Q88IR9 | L-serine ammonia-lyase (EC 4.3.1.17) (EC 4.3.1.17;
    primary bucket kegg:ppu00290)

    - PP_3191: PP_3191 | Q88I11 | Threonine ammonia-lyase / dehydratase (EC 4.3.1.19)
    (EC 4.3.1.19; primary bucket kegg:ppu00290)

    - ilvA-I: PP_3446 | Q88HB4 | L-threonine dehydratase (EC 4.3.1.19) (Threonine
    deaminase) (EC 4.3.1.19; primary bucket kegg:ppu00290)

    - ilvE: PP_3511 | Q88H54 | Branched-chain-amino-acid aminotransferase (EC 2.6.1.42)
    (EC 2.6.1.42; primary bucket kegg:ppu00290)

    - PP_4430: PP_4430 | Q88EM4 | Threonine dehydratase (EC 4.3.1.19) (EC 4.3.1.19;
    primary bucket kegg:ppu00290)

    - ldh: PP_4617 | Q88E51 | Leucine dehydrogenase (EC 1.4.1.9) (EC 1.4.1.9; primary
    bucket kegg:ppu00290)

    - ilvC: PP_4678 | Q88DZ0 | Ketol-acid reductoisomerase (NADP(+)) (KARI) (EC 1.1.1.86)
    (Acetohydroxy-acid isomeroreductase) (AHIR) (Alpha-keto-beta-hydroxylacyl reductoisomerase)
    (Ketol-acid reductoisomerase type 1) (Ketol-acid reductoisomerase type I) (EC
    1.1.1.86; primary bucket kegg:ppu00290)

    - ilvH: PP_4679 | Q88DY9 | Acetolactate synthase small subunit (AHAS) (ALS) (EC
    2.2.1.6) (Acetohydroxy-acid synthase small subunit) (EC 2.2.1.6; primary bucket
    kegg:ppu00660)

    - ilvI: PP_4680 | Q88DY8 | Acetolactate synthase (EC 2.2.1.6) (EC 2.2.1.6; primary
    bucket kegg:ppu00660)

    - ilvD: PP_5128 | Q88CQ2 | Dihydroxy-acid dehydratase (DAD) (EC 4.2.1.9) (EC 4.2.1.9;
    primary bucket kegg:ppu00290)

    - ilvA-II: PP_5149 | Q88CN1 | L-threonine dehydratase (EC 4.3.1.19) (Threonine
    deaminase) (EC 4.3.1.19; primary bucket kegg:ppu00290)'
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
  path: PSEPK__branched_chain_amino_acid_biosynthesis__ppu00290-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__branched_chain_amino_acid_biosynthesis__ppu00290-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

L-valine, L-leucine, and L-isoleucine biosynthesis in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00290
- Resolved ID: ppu00290
- Resolved name: Valine, leucine and isoleucine biosynthesis
- Source: KEGG

Resolved local bucket kegg:ppu00290 with 11 primary genes; module area: amino_acid_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 18

- leuA: PP_1025 | Q88P28 | 2-isopropylmalate synthase (EC 2.3.3.13) (Alpha-IPM synthase) (Alpha-isopropylmalate synthase) (EC 2.3.3.13; primary bucket kegg:ppu00290)
- PP_1157: PP_1157 | Q877U6 | Acetolactate synthase (primary bucket kegg:ppu00660)
- PP_1394: PP_1394 | Q88N22 | Acetolactate synthase, large subunit (primary bucket kegg:ppu00660)
- alaA: PP_1872 | Q88LQ7 | Glutamate-pyruvate aminotransferase AlaA (EC 2.6.1.2) (EC 2.6.1.2; primary bucket kegg:ppu00290)
- leuC: PP_1985 | Q88LE8 | 3-isopropylmalate dehydratase large subunit (EC 4.2.1.33) (Alpha-IPM isomerase) (IPMI) (Isopropylmalate isomerase) (EC 4.2.1.33; primary bucket kegg:ppu00660)
- leuD: PP_1986 | Q88LE7 | 3-isopropylmalate dehydratase small subunit (EC 4.2.1.33) (Alpha-IPM isomerase) (IPMI) (Isopropylmalate isomerase) (EC 4.2.1.33; primary bucket kegg:ppu00660)
- leuB: PP_1988 | Q88LE5 | 3-isopropylmalate dehydrogenase (EC 1.1.1.85) (3-IPM-DH) (Beta-IPM dehydrogenase) (IMDH) (EC 1.1.1.85; primary bucket kegg:ppu00660)
- PP_2930: PP_2930 | Q88IR9 | L-serine ammonia-lyase (EC 4.3.1.17) (EC 4.3.1.17; primary bucket kegg:ppu00290)
- PP_3191: PP_3191 | Q88I11 | Threonine ammonia-lyase / dehydratase (EC 4.3.1.19) (EC 4.3.1.19; primary bucket kegg:ppu00290)
- ilvA-I: PP_3446 | Q88HB4 | L-threonine dehydratase (EC 4.3.1.19) (Threonine deaminase) (EC 4.3.1.19; primary bucket kegg:ppu00290)
- ilvE: PP_3511 | Q88H54 | Branched-chain-amino-acid aminotransferase (EC 2.6.1.42) (EC 2.6.1.42; primary bucket kegg:ppu00290)
- PP_4430: PP_4430 | Q88EM4 | Threonine dehydratase (EC 4.3.1.19) (EC 4.3.1.19; primary bucket kegg:ppu00290)
- ldh: PP_4617 | Q88E51 | Leucine dehydrogenase (EC 1.4.1.9) (EC 1.4.1.9; primary bucket kegg:ppu00290)
- ilvC: PP_4678 | Q88DZ0 | Ketol-acid reductoisomerase (NADP(+)) (KARI) (EC 1.1.1.86) (Acetohydroxy-acid isomeroreductase) (AHIR) (Alpha-keto-beta-hydroxylacyl reductoisomerase) (Ketol-acid reductoisomerase type 1) (Ketol-acid reductoisomerase type I) (EC 1.1.1.86; primary bucket kegg:ppu00290)
- ilvH: PP_4679 | Q88DY9 | Acetolactate synthase small subunit (AHAS) (ALS) (EC 2.2.1.6) (Acetohydroxy-acid synthase small subunit) (EC 2.2.1.6; primary bucket kegg:ppu00660)
- ilvI: PP_4680 | Q88DY8 | Acetolactate synthase (EC 2.2.1.6) (EC 2.2.1.6; primary bucket kegg:ppu00660)
- ilvD: PP_5128 | Q88CQ2 | Dihydroxy-acid dehydratase (DAD) (EC 4.2.1.9) (EC 4.2.1.9; primary bucket kegg:ppu00290)
- ilvA-II: PP_5149 | Q88CN1 | L-threonine dehydratase (EC 4.3.1.19) (Threonine deaminase) (EC 4.3.1.19; primary bucket kegg:ppu00290)

## Generic Module Context

### Working Scope

Microbial biosynthesis of the three branched-chain amino acids. L-isoleucine synthesis begins with threonine deamination to 2-oxobutanoate. The IlvI-IlvH acetohydroxy-acid synthase, IlvC ketol-acid reductoisomerase, and IlvD dihydroxy-acid dehydratase then form a shared catalytic trunk that processes either the valine precursor derived from two pyruvate molecules or the isoleucine precursor derived from pyruvate plus 2-oxobutanoate. The valine intermediate 2-oxoisovalerate also enters a three-reaction LeuA/LeuC-LeuD/LeuB extension branch. IlvE performs the terminal transamination for all three products. The module requires each biochemical step but allows any validated member of the biosynthetic threonine-deaminase family to satisfy the entry reaction.

### Provisional Biological Outline

- branched-chain amino acid biosynthesis
  - 1. isoleucine-branch 2-oxobutanoate supply
  - L-threonine to 2-oxobutanoate
    - Biosynthetic threonine deaminase (molecular player: full-length biosynthetic threonine deaminase family; activity or role: threonine deaminase activity)
  - 2. acetohydroxy-acid formation
  - Acetohydroxy-acid synthase complex
    - IlvI acetohydroxy-acid synthase catalytic subunit (molecular player: biosynthetic acetohydroxy-acid synthase large subunit; activity or role: acetolactate synthase activity)
    - IlvH acetohydroxy-acid synthase regulatory subunit (molecular player: biosynthetic acetohydroxy-acid synthase small subunit; activity or role: acetolactate synthase regulator activity)
  - 3. acetohydroxy-acid reduction and rearrangement
  - Acetohydroxy acids to dihydroxy acids
    - IlvC ketol-acid reductoisomerase (molecular player: type I ketol-acid reductoisomerase family; activity or role: ketol-acid reductoisomerase activity)
  - 4. branched-chain 2-oxoacid formation
  - Dihydroxy acids to branched-chain 2-oxoacids
    - IlvD dihydroxy-acid dehydratase (molecular player: biosynthetic dihydroxy-acid dehydratase family; activity or role: dihydroxy-acid dehydratase activity)
  - 5. leucine-specific carbon-chain extension
  - 2-Oxoisovalerate to 2-oxoisocaproate
    - 1. committed leucine-branch condensation
    - 2-Oxoisovalerate to 2-isopropylmalate
      - LeuA 2-isopropylmalate synthase (molecular player: LeuA 2-isopropylmalate synthase family; activity or role: 2-isopropylmalate synthase activity)
    - 2. isopropylmalate isomerization
    - 2-Isopropylmalate to 3-isopropylmalate
      - LeuC 3-isopropylmalate dehydratase large subunit (molecular player: 3-isopropylmalate dehydratase large subunit family; activity or role: 3-isopropylmalate dehydratase activity)
      - LeuD 3-isopropylmalate dehydratase small subunit (molecular player: 3-isopropylmalate dehydratase small subunit family; activity or role: 3-isopropylmalate dehydratase activity)
    - 3. leucine-branch 2-oxoacid formation
    - 3-Isopropylmalate to 2-oxoisocaproate
      - LeuB 3-isopropylmalate dehydrogenase (molecular player: 3-isopropylmalate dehydrogenase family; activity or role: 3-isopropylmalate dehydrogenase activity)
  - 6. terminal transamination of all three branches
  - Branched-chain 2-oxoacids to L-valine, L-leucine, and L-isoleucine
    - IlvE branched-chain amino-acid aminotransferase (molecular player: IlvE branched-chain amino-acid aminotransferase family; activity or role: branched-chain-amino-acid:2-oxoglutarate transaminase activity)

### Known Relationships Among Steps

- L-threonine to 2-oxobutanoate precedes Acetohydroxy-acid synthase complex
- Acetohydroxy-acid synthase complex precedes Acetohydroxy acids to dihydroxy acids
- Acetohydroxy acids to dihydroxy acids precedes Dihydroxy acids to branched-chain 2-oxoacids
- Dihydroxy acids to branched-chain 2-oxoacids precedes 2-Oxoisovalerate to 2-oxoisocaproate
- Dihydroxy acids to branched-chain 2-oxoacids precedes Branched-chain 2-oxoacids to L-valine, L-leucine, and L-isoleucine
- 2-Oxoisovalerate to 2-oxoisocaproate precedes Branched-chain 2-oxoacids to L-valine, L-leucine, and L-isoleucine
- 2-Oxoisovalerate to 2-isopropylmalate precedes 2-Isopropylmalate to 3-isopropylmalate
- 2-Isopropylmalate to 3-isopropylmalate precedes 3-Isopropylmalate to 2-oxoisocaproate

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

# Module/Pathway Review: L-Valine, L-Leucine and L-Isoleucine Biosynthesis (KEGG ppu00290) in *Pseudomonas putida* KT2440

**Taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** KEGG ppu00290 "Valine, leucine and isoleucine biosynthesis"
**Scope of evidence:** UniProtKB (2026), KEGG (2026), and PubMed literature. All KT2440 ilv/leu proteins are UniProt evidence level PE=3 ("inferred from homology"); no target-strain enzymology exists for individual proteins. The strongest direct KT2440 evidence is a genome-wide auxotrophy screen (PMID 20158506).

---

## 1. Executive summary

The BCAA-biosynthesis module is **fully satisfiable** in *P. putida* KT2440: every one of the six canonical mechanistic steps has at least one strong, orthology-supported candidate, and de-novo amino-acid biosynthesis is experimentally required for growth on glucose minimal medium in this strain (PMID 20158506). The catalytic trunk (`ilvIH` → `ilvC` → `ilvD`), the leucine extension branch (`leuA` → `leuCD` → `leuB`), and the terminal transaminase (`ilvE`) are unambiguous. The only genuinely ambiguous step is the isoleucine-entry threonine deamination, which is served by **two redundant biosynthetic paralogs** (`ilvA-I`/PP_3446 and `ilvA-II`/PP_5149).

The candidate list, however, needs curation. It (a) appears to "omit **PP_3365**," but this is a locus-level artifact — PP_3365 and the listed **PP_1157** encode an **identical** AHAS large-subunit protein (single UniProt entry **Q877U6**, two ordered-locus names), so no distinct enzyme is missing; (b) contains **four over-propagated members** that are not part of BCAA biosynthesis — `alaA` (alanine), `ldh` (glutamate-dehydrogenase-like / BCAA *degradation*), and the short ACT-less dehydratases PP_3191 and PP_4430 (catabolic threonine/serine dehydratases), plus `PP_2930`/sdaA (serine ammonia-lyase); and (c) carries **incorrect primary-bucket labels** for `leuBCD` and `ilvHI` (tagged ppu00660, a KEGG map-overlap artifact — they are canonical ppu00290 genes). No lineage-specific citramalate (`cimA`) bypass exists, so threonine deamination is the sole isoleucine entry.

---

## 2. Target-organism pathway definition

**Included biochemistry (ppu00290):** conversion of pyruvate (and, for isoleucine, threonine-derived 2-oxobutanoate) to the three proteinogenic branched-chain amino acids via:
1. L-threonine → 2-oxobutanoate (threonine deaminase; isoleucine branch only)
2. 2× pyruvate → (S)-2-acetolactate, and pyruvate + 2-oxobutanoate → (S)-2-aceto-2-hydroxybutanoate (AHAS)
3. acetohydroxy acids → 2,3-dihydroxy acids (ketol-acid reductoisomerase)
4. 2,3-dihydroxy acids → branched 2-oxoacids (dihydroxy-acid dehydratase)
5. leucine-only extension: 2-oxoisovalerate → 2-isopropylmalate → 3-isopropylmalate → 2-oxoisocaproate (LeuA/LeuCD/LeuB)
6. transamination of all three 2-oxoacids → L-Val/L-Leu/L-Ile (BCAT, IlvE)

**Neighboring maps to keep separate:**
- **ppu00280** "Valine, leucine and isoleucine *degradation*" — catabolism; shares `ilvE` (reversible transaminase) and contains `ldh` (PP_4617).
- **ppu00660** "C5-branched dibasic acid metabolism" and **ppu00650** "Butanoate metabolism" — overlap on the *reaction* level (acetolactate, isopropylmalate), which is why `ilvHI`, `leuBCD`, and the catabolic acetolactate synthases co-map there. Map overlap ≠ separate biological function.
- **ppu00260** "Glycine, serine and threonine metabolism" — where KEGG also lists all four K01754 threonine dehydratases and `sdaA`.
- **ppu00250 / ppu00270** (Ala/Asp/Glu; Cys/Met) — source of the `alaA` and `sdaA` over-annotations.

**Alternate names / DB definitions:** KEGG modules **M00019** (Val/Ile biosynthesis, pyruvate ⇒ valine / 2-oxobutanoate ⇒ isoleucine) and **M00432** (leucine biosynthesis) / **M00570** (isoleucine biosynthesis, threonine ⇒ 2-oxobutanoate ⇒ isoleucine). UniProt uses per-product "L-valine / L-leucine / L-isoleucine biosynthesis" pathway strings. BioCyc/MetaCyc splits the same chemistry into ILEUSYN-PWY, VALSYN-PWY, LEUSYN-PWY.

---

## 3. Expected step model and satisfiability calls

| # | Step (enzyme / EC) | KT2440 gene(s) | Call |
|---|--------------------|----------------|------|
| 1 | L-Thr → 2-oxobutanoate — threonine deaminase (4.3.1.19) | **ilvA-I PP_3446**, **ilvA-II PP_5149** | **covered** (redundant paralogs) |
| 2 | AHAS (2.2.1.6) | **ilvI PP_4680** + **ilvH PP_4679** | **covered** |
| 3 | Ketol-acid reductoisomerase (1.1.1.86) | **ilvC PP_4678** | **covered** |
| 4 | Dihydroxy-acid dehydratase (4.2.1.9) | **ilvD PP_5128** | **covered** |
| 5a | 2-isopropylmalate synthase (2.3.3.13) | **leuA PP_1025** | **covered** |
| 5b | Isopropylmalate isomerase (4.2.1.33) | **leuC PP_1985** + **leuD PP_1986** | **covered** |
| 5c | 3-isopropylmalate dehydrogenase (1.1.1.85) | **leuB PP_1988** | **covered** |
| 6 | Branched-chain aminotransferase (2.6.1.42) | **ilvE PP_3511** | **covered** |

**All six steps covered.** No gaps and no `not_expected_in_target_taxon` steps: KT2440 is a BCAA prototroph.

---

## 4. Candidate genes and evidence

**High-confidence biosynthetic members (promote/keep as covered):**
- **ilvI (PP_4680, Q88DY8)** + **ilvH (PP_4679, Q88DY9)** — anabolic AHAS; UniRule pathway "L-valine/L-isoleucine biosynthesis step 1"; ilvH carries the ACT valine-feedback domain. Organised in the **ilvIH-ilvC operon (PP_4678-4680)** — the strongest operon evidence in this module.
- **ilvC (PP_4678, Q88DZ0)** — type-I KARI, EC 1.1.1.86; detailed catalytic FUNCTION annotation.
- **ilvD (PP_5128, Q88CQ2)** — dihydroxy-acid dehydratase, EC 4.2.1.9.
- **leuA (PP_1025, Q88P28)** — 2-isopropylmalate synthase; UniProt "L-leucine biosynthesis step 1/4". Genomic orphan.
- **leuC (PP_1985)/leuD (PP_1986)** — isopropylmalate isomerase large/small subunits, clustered.
- **leuB (PP_1988, Q88LE5)** — 3-isopropylmalate dehydrogenase.
- **ilvE (PP_3511, Q88H54)** — BCAT; UniProt assigns it to all three L-Val/L-Leu/L-Ile pathways; also appears in the ppu00280 degradation map because the transamination is reversible (expected, not an error). Single-copy — no paralog backup, so functionally pivotal.
- **ilvA-I (PP_3446, Q88HB4)** and **ilvA-II (PP_5149, Q88CN1)** — both ~500–530 aa with two C-terminal **ACT-like regulatory domains**, UniProt-named "L-threonine dehydratase" with the isoleucine-biosynthesis pathway. Both are genomic orphans. Redundant biosynthetic paralogs.

**Copy-number check (KEGG ortholog counts in KT2440):** the trunk/branch enzymes are all single-copy — ilvE/BCAT (K00826, PP_3511), leuA (K01649, PP_1025), leuB (K00052, PP_1988), leuCD (K01703, PP_1985), ilvD (K01687, PP_5128), ilvC (K00053, PP_4678) — so there is no paralog ambiguity at these steps; ilvE in particular has no backup and is functionally pivotal. Critically, the **AHAS small (regulatory) subunit is also single-copy** (K01653, ilvH/PP_4679): since the other three K01652 large subunits (Q877U6=PP_1157/PP_3365; PP_1394) have no cognate small subunit, only ilvI can assemble the anabolic, valine-feedback-regulated AHAS holoenzyme — independent support that ilvIH is the sole biosynthetic AHAS and the other large subunits are catabolic/independent acetolactate synthases.

**Evidence type for all of the above:** homology / UniRule + KEGG orthology + (for ilvIH-ilvC, leuCD) operon context. Direct enzymology is *not* available for any KT2440 protein; whole-module function is supported in vivo by auxotrophy on minimal medium (PMID 20158506).

---

## 5. Gaps, ambiguities, and likely over-annotations

**Paralog ambiguity (candidate_uncertain, needs experimental disambiguation):**
- **ilvA-I vs ilvA-II** — which paralog carries the physiological biosynthetic load (and whether one is isoleucine-feedback-regulated while the other is not) is unresolved. Redundancy explains why neither would necessarily show an auxotrophic phenotype when singly disrupted.
- **AHAS large-subunit paralogs** — besides anabolic `ilvI`, KT2440 encodes additional K01652 large subunits. Crucially, **PP_1157 and PP_3365 are two loci encoding an identical 547-aa protein** (single UniProt entry **Q877U6**; confirmed by KEGG DBLINKS and UniProt `orderedLocusNames`), so the apparent "missing PP_3365" is a duplicate gene copy, not a new enzyme. The distinct paralogs are therefore Q877U6 (PP_1157/PP_3365) and **PP_1394 (Q88N22)**. Neither has a UniProt BCAA-pathway assignment or an adjacent small regulatory subunit, and both map primarily to ppu00660/00650. Sequence classification (3-mer cosine vs characterized references) shows **ilvI/PP_4680 is unambiguously the anabolic AHAS** (top match to *E. coli* anabolic IlvI, 0.43, vs ≤0.26 for all others), while Q877U6 and PP_1394 are divergent from all anabolic references (0.16–0.22) → most likely **catabolic acetolactate synthases** (acetoin/2,3-butanediol), candidate_uncertain, leaning not-in-biosynthesis-module.

**Likely over-propagation (should NOT be biosynthetic-module members):**
- **PP_3191 (Q88I11, 350 aa)** and **PP_4430 (Q88EM4, 330 aa)** — ACT-less, UniProt-unnamed PALP-fold proteins auto-mapped to K01754/EC 4.3.1.19. The ~330 aa length matches catabolic threonine dehydratase (E. coli TdcB ≈328 aa); genomic neighbours are amino-acid-catabolism genes (ornithine cyclodeaminase, GntR/D-Arg regulators). Broad EC 4.3.1.19 mapping, not biosynthetic evidence.
- **PP_2930 (Q88IR9)** — L-serine ammonia-lyase (sdaA, EC 4.3.1.17); serine, not threonine/BCAA. Over-annotation into ppu00290.
- **alaA (PP_1872, Q88LQ7, EC 2.6.1.2)** — glutamate-pyruvate aminotransferase, UniProt pathway "L-alanine biosynthesis". Not BCAA. Over-propagation (transaminase EC overlap).
- **ldh (PP_4617, Q88E51, EC 1.4.1.9)** — annotated "leucine dehydrogenase," but UniProt domain is Glu/Phe/Leu/Val/Trp-dehydrogenase and FUNCTION is glutamate oxidative deamination; KEGG places it in ppu00280 **degradation**. Even if it can reductively aminate 2-oxoisocaproate, the canonical biosynthetic terminal step is IlvE transamination — treat as catabolic/alternative, not a core biosynthetic member.

**Metadata bucket errors (module_needs_revision):**
- `leuC/leuD/leuB` (PP_1985/86/88) and `ilvH/ilvI` (PP_4679/80) are labeled *primary bucket kegg:ppu00660*. They are canonical ppu00290 biosynthetic genes; the 00660 tag is a KEGG map-overlap artifact and should be corrected to primary ppu00290.

---

## 6. Module and GO-curation recommendations

- **Mark covered:** steps 1–6 (see §3). The module is satisfiable; KT2440 is a BCAA prototroph.
- **candidate_uncertain:** `ilvA-I`/`ilvA-II` (which is dominant); `PP_3365`, `PP_1157`, `PP_1394` (AHAS-family paralogs of uncertain anabolic role); `ldh` (catabolic vs alternative aminating route).
- **Remove from biosynthesis module (over-annotation):** `alaA` (PP_1872), `PP_2930` (sdaA), and the short catabolic dehydratases `PP_3191`, `PP_4430`. `ldh` (PP_4617) belongs primarily to ppu00280.
- **module_needs_revision:**
  - Document **PP_3365** as a duplicate locus of PP_1157 (identical protein, UniProt Q877U6) — this reconciles the KEGG 19-gene vs metadata 18-gene count without adding a new enzyme. Both loci should be marked candidate_uncertain (catabolic-ALS-leaning), consistently bucketed.
  - Re-bucket `leuBCD` and `ilvHI` to primary **ppu00290**.
  - Record that `ilvE` co-membership in ppu00280 is expected (reversible transaminase), not an error.
- **Module boundaries:** the generic outline is essentially correct for KT2440. One refinement — the outline's "any validated member of the biosynthetic threonine-deaminase family satisfies the entry" should specify **ACT-domain-containing, full-length** (~500 aa) deaminases, to exclude the short catabolic K01754 hits.
- **GO curation:** no new GO terms required; existing terms suffice — GO:0009097 (isoleucine biosynthesis), GO:0009099 (valine biosynthesis), GO:0009098 (leucine biosynthesis), GO:0003984 (AHAS), GO:0004160 (DHAD), GO:0004084 (BCAT), GO:0004794 (L-threonine ammonia-lyase). Recommend GO annotations be restricted to the covered members above and *withheld* from the over-propagated candidates.

---

## 7. Genes to promote to full `fetch-gene` review

1. **ilvA-I (PP_3446)** and **ilvA-II (PP_5149)** — resolve which is the principal biosynthetic threonine deaminase and its feedback regulation (paralog redundancy).
2. **Q877U6 (PP_1157 = PP_3365 duplicate loci)** and **PP_1394** — determine anabolic vs catabolic (acetoin/butanediol) AHAS role; confirm the two loci are truly identical copies.
3. **ldh (PP_4617)** — confirm glutamate-dehydrogenase-like vs true leucine-dehydrogenase function and biosynthetic relevance.
4. **PP_1157 / PP_1394** — classify as catabolic acetolactate synthases (acetoin/butanediol) vs redundant AHAS.
5. (Lower priority) **PP_3191 / PP_4430** — confirm catabolic threonine/serine dehydratase assignment to justify removal from the biosynthesis module.

---

## 8. Evidence summary and open questions

- **Direct (target strain):** genome-wide minimal-medium auxotrophy screen shows amino-acid biosynthesis genes are conditionally essential in KT2440 (Molina-Henares et al. 2010, PMID 20158506) — establishes the module is functional and required in vivo, but does not resolve individual paralogs.
- **Homology / database inference:** all per-gene step assignments (UniProt UniRule PE=3, KEGG KO). Strong for the single-copy trunk/branch enzymes; weaker where multiple paralogs share a KO (K01754 deaminases; K01652 AHAS large subunits).
- **Species transfer:** the biosynthetic-vs-catabolic threonine-deaminase distinction (ACT-domain, length) is a robust, sequence-intrinsic criterion (E. coli IlvA vs TdcB) that transfers strongly. AHAS-isozyme physiology in other *Pseudomonas* (e.g., *P. aeruginosa* ilvBN/ilvIH) is a weaker transfer and should not be assumed identical in KT2440.
- **Open questions / resolving experiments:** (i) single vs double `ilvA-I/ilvA-II` knockouts on minimal medium ± isoleucine to test redundancy; (ii) does `PP_3365`/`ilvI` deletion cause valine/isoleucine auxotrophy (anabolic AHAS test)?; (iii) enzymatic assay or RB-TnSeq fitness (cf. PMID 38323821) to confirm PP_1157/PP_1394 are acetoin-pathway ALS; (iv) verify `ldh` (PP_4617) directionality in vivo.

---

## Key references
- Molina-Henares AJ, et al. (2010) *Identification of conditionally essential genes for growth of Pseudomonas putida KT2440 on minimal medium…* Environ Microbiol. **PMID 20158506**. — direct KT2440 auxotrophy evidence.
- Borchert AJ, et al. (2024) *Machine learning analysis of RB-TnSeq fitness data predicts functional gene modules in [P. putida].* **PMID 38323821**. — functional-genomics resource to disambiguate paralogs.
- Borchert AJ & Downs DM (2018) *Analyses of variants of the Ser/Thr dehydratase IlvA…2-aminoacrylate metabolism.* **PMID 30327426**. — biosynthetic IlvA (EC 4.3.1.19) mechanism/context.
- UniProtKB entries: Q88DY8 (ilvI), Q88DY9 (ilvH), Q88DZ0 (ilvC), Q88CQ2 (ilvD), Q88P28 (leuA), Q88LE8/Q88LE7/Q88LE5 (leuC/D/B), Q88H54 (ilvE), Q88HB4/Q88CN1 (ilvA-I/ilvA-II).
- KEGG pathways ppu00290 / ppu00280 / ppu00660 / ppu00260; modules M00019, M00432, M00570.

*Caveat: no per-protein enzymology exists for KT2440 BCAA-biosynthesis enzymes; all gene-level calls are homology/orthology-based, with whole-module function corroborated in vivo by minimal-medium auxotrophy.*


## Artifacts

- [OpenScientist final report](PSEPK__branched_chain_amino_acid_biosynthesis__ppu00290-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__branched_chain_amino_acid_biosynthesis__ppu00290-deep-research-openscientist_artifacts/final_report.pdf)