---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-06T23:55:50.151786'
end_time: '2026-07-07T00:25:05.728510'
duration_seconds: 1755.58
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Ubiquinone biosynthesis
  module_summary: 'A taxon-neutral bacterial ubiquinone biosynthesis module covering
    formation of the benzoquinone head group and its polyprenylated membrane-associated
    intermediates from chorismate-derived 4-hydroxybenzoate. The strict pathway begins
    with UbiC production of 4-hydroxybenzoate, UbiA prenylation, UbiD decarboxylation
    supported by the UbiX-derived prenyl-FMN cofactor, and a series of hydroxylation
    and methylation steps carried out by UbiH-family monooxygenases, Coq7, UbiE, and
    UbiG. KEGG ppu00130 is broader than this strict module: it also includes other
    terpenoid-quinone or side-map entries such as generic NAD(P)H quinone oxidoreductases,
    homogentisate formation, and acyl-CoA thioesterase-like proteins that should not
    by themselves satisfy ubiquinone biosynthesis.'
  module_outline: "- Ubiquinone biosynthesis\n  - 1. 4-hydroxybenzoate precursor formation\n\
    \  - Chorismate to 4-hydroxybenzoate\n    - UbiC chorismate lyase (molecular player:\
    \ PSEPK ubiC; activity or role: chorismate lyase activity)\n  - 2. polyprenyl\
    \ side-chain attachment\n  - 4-hydroxybenzoate polyprenylation\n    - UbiA 4-hydroxybenzoate\
    \ polyprenyltransferase (molecular player: PSEPK ubiA; activity or role: 4-hydroxybenzoate\
    \ polyprenyltransferase activity)\n  - 3. prenyl-FMN cofactor supply for UbiD\n\
    \  - Prenyl-FMN cofactor synthesis\n    - UbiX flavin prenyltransferase (molecular\
    \ player: PSEPK ubiX; activity or role: flavin prenyltransferase activity)\n \
    \ - 4. polyprenyl-hydroxybenzoate decarboxylation\n  - 4-hydroxy-3-polyprenylbenzoate\
    \ decarboxylation\n    - UbiD 4-hydroxy-3-polyprenylbenzoate decarboxylase (molecular\
    \ player: PSEPK ubiD; activity or role: 4-hydroxy-3-polyprenylbenzoate decarboxylase\
    \ activity)\n  - 5. first aromatic hydroxylation\n  - 2-polyprenylphenol hydroxylation\n\
    \    - VisC-like 2-polyprenylphenol 6-hydroxylase (molecular player: PSEPK visC;\
    \ activity or role: 2-polyprenylphenol 6-hydroxylase activity)\n  - 6. first O-methylation\n\
    \  - Polyprenyldihydroxybenzene O-methylation\n    - UbiG 2-polyprenyl-6-hydroxyphenol\
    \ methylase (molecular player: PSEPK ubiG; activity or role: 2-polyprenyl-6-hydroxyphenol\
    \ methylase activity)\n  - 7. second aromatic hydroxylation\n  - 2-octaprenyl-6-methoxyphenol\
    \ hydroxylation\n    - UbiH 2-octaprenyl-6-methoxyphenol hydroxylase (molecular\
    \ player: PSEPK ubiH; activity or role: 2-octaprenyl-6-methoxyphenol hydroxylase\
    \ activity)\n  - 8. C-methylation of the quinol ring\n  - UbiE C-methylation\n\
    \    - UbiE 2-methoxy-6-polyprenyl-1,4-benzoquinol methyltransferase (molecular\
    \ player: PSEPK ubiE; activity or role: 2-methoxy-6-polyprenyl-1,4-benzoquinol\
    \ methyltransferase activity)\n  - 9. demethoxyubiquinol hydroxylation\n  - 3-demethoxyubiquinol\
    \ hydroxylation\n    - Coq7 3-demethoxyubiquinol hydroxylase (molecular player:\
    \ PSEPK coq7; activity or role: 3-demethoxyubiquinol 3-hydroxylase activity)\n\
    \  - 10. terminal O-methylation\n  - Demethylubiquinol O-methylation\n    - UbiG\
    \ 3-demethylubiquinol 3-O-methyltransferase (molecular player: PSEPK ubiG; activity\
    \ or role: 3-demethylubiquinol 3-O-methyltransferase activity)"
  module_connections: No explicit connections.
  pathway_query: ppu00130
  pathway_id: ppu00130
  pathway_name: Ubiquinone and other terpenoid-quinone biosynthesis
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00130 with 13 primary genes; module
    area: cofactors_vitamins_redox.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '14'
  candidate_genes: '- coq7: PP_0427 | Q88QR1 | 3-demethoxyubiquinol 3-hydroxylase
    (DMQ hydroxylase) (EC 1.14.99.60) (2-nonaprenyl-3-methyl-6-methoxy-1,4-benzoquinol
    hydroxylase) (EC 1.14.99.60; primary bucket kegg:ppu00130)

    - ubiX: PP_0548 | Q88QE6 | Flavin prenyltransferase UbiX (EC 2.5.1.129) (EC 2.5.1.129;
    primary bucket kegg:ppu00627)

    - PP_1218: PP_1218 | Q88NI9 | Acyl-CoA thioesterase (EC 3.1.2.-) (EC 3.1.2.-;
    primary bucket kegg:ppu00130)

    - PP_1644: PP_1644 | Q88MC9 | NAD(P)H dehydrogenase (Quinone) (EC 1.6.5.2) (EC
    1.6.5.2; primary bucket kegg:ppu00130)

    - ubiG: PP_1765 | Q88M10 | Ubiquinone biosynthesis O-methyltransferase (2-polyprenyl-6-hydroxyphenol
    methylase) (EC 2.1.1.222) (3-demethylubiquinone 3-O-methyltransferase) (EC 2.1.1.64)
    (EC 2.1.1.222; 2.1.1.64; primary bucket kegg:ppu00130)

    - PP_2789: PP_2789 | Q88J60 | Oxidoreductase (primary bucket kegg:ppu00130)

    - hpd: PP_3433 | Q88HC7 | 4-hydroxyphenylpyruvate dioxygenase (EC 1.13.11.27)
    (EC 1.13.11.27; primary bucket kegg:ppu00130)

    - PP_3720: PP_3720 | Q88GK1 | NAD(P)H quinone oxidoreductase (primary bucket kegg:ppu00130)

    - ubiE: PP_5011 | Q88D17 | Ubiquinone/menaquinone biosynthesis C-methyltransferase
    UbiE (EC 2.1.1.163) (EC 2.1.1.201) (2-methoxy-6-polyprenyl-1,4-benzoquinol methylase)
    (Demethylmenaquinone methyltransferase) (EC 2.1.1.163; 2.1.1.201; primary bucket
    kegg:ppu00130)

    - visC: PP_5197 | Q88CI4 | Oxidoreductase involved in anerobic synthesis of ubiquinone,
    FAD/NAD(P)-binding domain (primary bucket kegg:ppu00130)

    - ubiH: PP_5199 | Q88CI2 | 2-octaprenyl-6-methoxyphenyl hydroxylase (primary bucket
    kegg:ppu00130)

    - ubiD: PP_5213 | Q88CG8 | 3-octaprenyl-4-hydroxybenzoate carboxy-lyase (EC 4.1.1.98)
    (Polyprenyl p-hydroxybenzoate decarboxylase) (EC 4.1.1.98; primary bucket kegg:ppu00130)

    - ubiC: PP_5317 | Q88C66 | Probable chorismate pyruvate-lyase (CL) (CPL) (EC 4.1.3.40)
    (EC 4.1.3.40; primary bucket kegg:ppu00130)

    - ubiA: PP_5318 | Q88C65 | 4-hydroxybenzoate octaprenyltransferase (EC 2.5.1.39)
    (4-HB polyprenyltransferase) (EC 2.5.1.39; primary bucket kegg:ppu00130)'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 32
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PSEPK__ubiquinone_biosynthesis__ppu00130-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PSEPK__ubiquinone_biosynthesis__ppu00130-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Ubiquinone biosynthesis in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00130
- Resolved ID: ppu00130
- Resolved name: Ubiquinone and other terpenoid-quinone biosynthesis
- Source: KEGG

Resolved local bucket kegg:ppu00130 with 13 primary genes; module area: cofactors_vitamins_redox.

## Candidate Genes From Local Metadata

Candidate gene count: 14

- coq7: PP_0427 | Q88QR1 | 3-demethoxyubiquinol 3-hydroxylase (DMQ hydroxylase) (EC 1.14.99.60) (2-nonaprenyl-3-methyl-6-methoxy-1,4-benzoquinol hydroxylase) (EC 1.14.99.60; primary bucket kegg:ppu00130)
- ubiX: PP_0548 | Q88QE6 | Flavin prenyltransferase UbiX (EC 2.5.1.129) (EC 2.5.1.129; primary bucket kegg:ppu00627)
- PP_1218: PP_1218 | Q88NI9 | Acyl-CoA thioesterase (EC 3.1.2.-) (EC 3.1.2.-; primary bucket kegg:ppu00130)
- PP_1644: PP_1644 | Q88MC9 | NAD(P)H dehydrogenase (Quinone) (EC 1.6.5.2) (EC 1.6.5.2; primary bucket kegg:ppu00130)
- ubiG: PP_1765 | Q88M10 | Ubiquinone biosynthesis O-methyltransferase (2-polyprenyl-6-hydroxyphenol methylase) (EC 2.1.1.222) (3-demethylubiquinone 3-O-methyltransferase) (EC 2.1.1.64) (EC 2.1.1.222; 2.1.1.64; primary bucket kegg:ppu00130)
- PP_2789: PP_2789 | Q88J60 | Oxidoreductase (primary bucket kegg:ppu00130)
- hpd: PP_3433 | Q88HC7 | 4-hydroxyphenylpyruvate dioxygenase (EC 1.13.11.27) (EC 1.13.11.27; primary bucket kegg:ppu00130)
- PP_3720: PP_3720 | Q88GK1 | NAD(P)H quinone oxidoreductase (primary bucket kegg:ppu00130)
- ubiE: PP_5011 | Q88D17 | Ubiquinone/menaquinone biosynthesis C-methyltransferase UbiE (EC 2.1.1.163) (EC 2.1.1.201) (2-methoxy-6-polyprenyl-1,4-benzoquinol methylase) (Demethylmenaquinone methyltransferase) (EC 2.1.1.163; 2.1.1.201; primary bucket kegg:ppu00130)
- visC: PP_5197 | Q88CI4 | Oxidoreductase involved in anerobic synthesis of ubiquinone, FAD/NAD(P)-binding domain (primary bucket kegg:ppu00130)
- ubiH: PP_5199 | Q88CI2 | 2-octaprenyl-6-methoxyphenyl hydroxylase (primary bucket kegg:ppu00130)
- ubiD: PP_5213 | Q88CG8 | 3-octaprenyl-4-hydroxybenzoate carboxy-lyase (EC 4.1.1.98) (Polyprenyl p-hydroxybenzoate decarboxylase) (EC 4.1.1.98; primary bucket kegg:ppu00130)
- ubiC: PP_5317 | Q88C66 | Probable chorismate pyruvate-lyase (CL) (CPL) (EC 4.1.3.40) (EC 4.1.3.40; primary bucket kegg:ppu00130)
- ubiA: PP_5318 | Q88C65 | 4-hydroxybenzoate octaprenyltransferase (EC 2.5.1.39) (4-HB polyprenyltransferase) (EC 2.5.1.39; primary bucket kegg:ppu00130)

## Generic Module Context

### Working Scope

A taxon-neutral bacterial ubiquinone biosynthesis module covering formation of the benzoquinone head group and its polyprenylated membrane-associated intermediates from chorismate-derived 4-hydroxybenzoate. The strict pathway begins with UbiC production of 4-hydroxybenzoate, UbiA prenylation, UbiD decarboxylation supported by the UbiX-derived prenyl-FMN cofactor, and a series of hydroxylation and methylation steps carried out by UbiH-family monooxygenases, Coq7, UbiE, and UbiG. KEGG ppu00130 is broader than this strict module: it also includes other terpenoid-quinone or side-map entries such as generic NAD(P)H quinone oxidoreductases, homogentisate formation, and acyl-CoA thioesterase-like proteins that should not by themselves satisfy ubiquinone biosynthesis.

### Provisional Biological Outline

- Ubiquinone biosynthesis
  - 1. 4-hydroxybenzoate precursor formation
  - Chorismate to 4-hydroxybenzoate
    - UbiC chorismate lyase (molecular player: PSEPK ubiC; activity or role: chorismate lyase activity)
  - 2. polyprenyl side-chain attachment
  - 4-hydroxybenzoate polyprenylation
    - UbiA 4-hydroxybenzoate polyprenyltransferase (molecular player: PSEPK ubiA; activity or role: 4-hydroxybenzoate polyprenyltransferase activity)
  - 3. prenyl-FMN cofactor supply for UbiD
  - Prenyl-FMN cofactor synthesis
    - UbiX flavin prenyltransferase (molecular player: PSEPK ubiX; activity or role: flavin prenyltransferase activity)
  - 4. polyprenyl-hydroxybenzoate decarboxylation
  - 4-hydroxy-3-polyprenylbenzoate decarboxylation
    - UbiD 4-hydroxy-3-polyprenylbenzoate decarboxylase (molecular player: PSEPK ubiD; activity or role: 4-hydroxy-3-polyprenylbenzoate decarboxylase activity)
  - 5. first aromatic hydroxylation
  - 2-polyprenylphenol hydroxylation
    - VisC-like 2-polyprenylphenol 6-hydroxylase (molecular player: PSEPK visC; activity or role: 2-polyprenylphenol 6-hydroxylase activity)
  - 6. first O-methylation
  - Polyprenyldihydroxybenzene O-methylation
    - UbiG 2-polyprenyl-6-hydroxyphenol methylase (molecular player: PSEPK ubiG; activity or role: 2-polyprenyl-6-hydroxyphenol methylase activity)
  - 7. second aromatic hydroxylation
  - 2-octaprenyl-6-methoxyphenol hydroxylation
    - UbiH 2-octaprenyl-6-methoxyphenol hydroxylase (molecular player: PSEPK ubiH; activity or role: 2-octaprenyl-6-methoxyphenol hydroxylase activity)
  - 8. C-methylation of the quinol ring
  - UbiE C-methylation
    - UbiE 2-methoxy-6-polyprenyl-1,4-benzoquinol methyltransferase (molecular player: PSEPK ubiE; activity or role: 2-methoxy-6-polyprenyl-1,4-benzoquinol methyltransferase activity)
  - 9. demethoxyubiquinol hydroxylation
  - 3-demethoxyubiquinol hydroxylation
    - Coq7 3-demethoxyubiquinol hydroxylase (molecular player: PSEPK coq7; activity or role: 3-demethoxyubiquinol 3-hydroxylase activity)
  - 10. terminal O-methylation
  - Demethylubiquinol O-methylation
    - UbiG 3-demethylubiquinol 3-O-methyltransferase (molecular player: PSEPK ubiG; activity or role: 3-demethylubiquinol 3-O-methyltransferase activity)

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

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Ubiquinone biosynthesis in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00130
- Resolved ID: ppu00130
- Resolved name: Ubiquinone and other terpenoid-quinone biosynthesis
- Source: KEGG

Resolved local bucket kegg:ppu00130 with 13 primary genes; module area: cofactors_vitamins_redox.

## Candidate Genes From Local Metadata

Candidate gene count: 14

- coq7: PP_0427 | Q88QR1 | 3-demethoxyubiquinol 3-hydroxylase (DMQ hydroxylase) (EC 1.14.99.60) (2-nonaprenyl-3-methyl-6-methoxy-1,4-benzoquinol hydroxylase) (EC 1.14.99.60; primary bucket kegg:ppu00130)
- ubiX: PP_0548 | Q88QE6 | Flavin prenyltransferase UbiX (EC 2.5.1.129) (EC 2.5.1.129; primary bucket kegg:ppu00627)
- PP_1218: PP_1218 | Q88NI9 | Acyl-CoA thioesterase (EC 3.1.2.-) (EC 3.1.2.-; primary bucket kegg:ppu00130)
- PP_1644: PP_1644 | Q88MC9 | NAD(P)H dehydrogenase (Quinone) (EC 1.6.5.2) (EC 1.6.5.2; primary bucket kegg:ppu00130)
- ubiG: PP_1765 | Q88M10 | Ubiquinone biosynthesis O-methyltransferase (2-polyprenyl-6-hydroxyphenol methylase) (EC 2.1.1.222) (3-demethylubiquinone 3-O-methyltransferase) (EC 2.1.1.64) (EC 2.1.1.222; 2.1.1.64; primary bucket kegg:ppu00130)
- PP_2789: PP_2789 | Q88J60 | Oxidoreductase (primary bucket kegg:ppu00130)
- hpd: PP_3433 | Q88HC7 | 4-hydroxyphenylpyruvate dioxygenase (EC 1.13.11.27) (EC 1.13.11.27; primary bucket kegg:ppu00130)
- PP_3720: PP_3720 | Q88GK1 | NAD(P)H quinone oxidoreductase (primary bucket kegg:ppu00130)
- ubiE: PP_5011 | Q88D17 | Ubiquinone/menaquinone biosynthesis C-methyltransferase UbiE (EC 2.1.1.163) (EC 2.1.1.201) (2-methoxy-6-polyprenyl-1,4-benzoquinol methylase) (Demethylmenaquinone methyltransferase) (EC 2.1.1.163; 2.1.1.201; primary bucket kegg:ppu00130)
- visC: PP_5197 | Q88CI4 | Oxidoreductase involved in anerobic synthesis of ubiquinone, FAD/NAD(P)-binding domain (primary bucket kegg:ppu00130)
- ubiH: PP_5199 | Q88CI2 | 2-octaprenyl-6-methoxyphenyl hydroxylase (primary bucket kegg:ppu00130)
- ubiD: PP_5213 | Q88CG8 | 3-octaprenyl-4-hydroxybenzoate carboxy-lyase (EC 4.1.1.98) (Polyprenyl p-hydroxybenzoate decarboxylase) (EC 4.1.1.98; primary bucket kegg:ppu00130)
- ubiC: PP_5317 | Q88C66 | Probable chorismate pyruvate-lyase (CL) (CPL) (EC 4.1.3.40) (EC 4.1.3.40; primary bucket kegg:ppu00130)
- ubiA: PP_5318 | Q88C65 | 4-hydroxybenzoate octaprenyltransferase (EC 2.5.1.39) (4-HB polyprenyltransferase) (EC 2.5.1.39; primary bucket kegg:ppu00130)

## Generic Module Context

### Working Scope

A taxon-neutral bacterial ubiquinone biosynthesis module covering formation of the benzoquinone head group and its polyprenylated membrane-associated intermediates from chorismate-derived 4-hydroxybenzoate. The strict pathway begins with UbiC production of 4-hydroxybenzoate, UbiA prenylation, UbiD decarboxylation supported by the UbiX-derived prenyl-FMN cofactor, and a series of hydroxylation and methylation steps carried out by UbiH-family monooxygenases, Coq7, UbiE, and UbiG. KEGG ppu00130 is broader than this strict module: it also includes other terpenoid-quinone or side-map entries such as generic NAD(P)H quinone oxidoreductases, homogentisate formation, and acyl-CoA thioesterase-like proteins that should not by themselves satisfy ubiquinone biosynthesis.

### Provisional Biological Outline

- Ubiquinone biosynthesis
  - 1. 4-hydroxybenzoate precursor formation
  - Chorismate to 4-hydroxybenzoate
    - UbiC chorismate lyase (molecular player: PSEPK ubiC; activity or role: chorismate lyase activity)
  - 2. polyprenyl side-chain attachment
  - 4-hydroxybenzoate polyprenylation
    - UbiA 4-hydroxybenzoate polyprenyltransferase (molecular player: PSEPK ubiA; activity or role: 4-hydroxybenzoate polyprenyltransferase activity)
  - 3. prenyl-FMN cofactor supply for UbiD
  - Prenyl-FMN cofactor synthesis
    - UbiX flavin prenyltransferase (molecular player: PSEPK ubiX; activity or role: flavin prenyltransferase activity)
  - 4. polyprenyl-hydroxybenzoate decarboxylation
  - 4-hydroxy-3-polyprenylbenzoate decarboxylation
    - UbiD 4-hydroxy-3-polyprenylbenzoate decarboxylase (molecular player: PSEPK ubiD; activity or role: 4-hydroxy-3-polyprenylbenzoate decarboxylase activity)
  - 5. first aromatic hydroxylation
  - 2-polyprenylphenol hydroxylation
    - VisC-like 2-polyprenylphenol 6-hydroxylase (molecular player: PSEPK visC; activity or role: 2-polyprenylphenol 6-hydroxylase activity)
  - 6. first O-methylation
  - Polyprenyldihydroxybenzene O-methylation
    - UbiG 2-polyprenyl-6-hydroxyphenol methylase (molecular player: PSEPK ubiG; activity or role: 2-polyprenyl-6-hydroxyphenol methylase activity)
  - 7. second aromatic hydroxylation
  - 2-octaprenyl-6-methoxyphenol hydroxylation
    - UbiH 2-octaprenyl-6-methoxyphenol hydroxylase (molecular player: PSEPK ubiH; activity or role: 2-octaprenyl-6-methoxyphenol hydroxylase activity)
  - 8. C-methylation of the quinol ring
  - UbiE C-methylation
    - UbiE 2-methoxy-6-polyprenyl-1,4-benzoquinol methyltransferase (molecular player: PSEPK ubiE; activity or role: 2-methoxy-6-polyprenyl-1,4-benzoquinol methyltransferase activity)
  - 9. demethoxyubiquinol hydroxylation
  - 3-demethoxyubiquinol hydroxylation
    - Coq7 3-demethoxyubiquinol hydroxylase (molecular player: PSEPK coq7; activity or role: 3-demethoxyubiquinol 3-hydroxylase activity)
  - 10. terminal O-methylation
  - Demethylubiquinol O-methylation
    - UbiG 3-demethylubiquinol 3-O-methyltransferase (molecular player: PSEPK ubiG; activity or role: 3-demethylubiquinol 3-O-methyltransferase activity)

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

# Ubiquinone Biosynthesis in *Pseudomonas putida* KT2440: A Species-Aware Module Review

## 1. Executive Summary

This review assesses the ubiquinone (UQ, coenzyme Q) biosynthetic pathway in *Pseudomonas putida* KT2440 (NCBI taxon 160488, proteome UP000000556) as defined by KEGG map ppu00130 ("Ubiquinone and other terpenoid-quinone biosynthesis"). *P. putida* KT2440 is an obligately aerobic Gammaproteobacterium that produces UQ-9 (ubiquinone with a nonaprenyl side chain), which serves as its primary membrane-embedded electron and proton shuttle in respiratory metabolism. The 14 candidate genes retrieved from KEGG metadata were evaluated against the current literature on bacterial UQ biosynthesis, with particular reference to recent comparative genomics (Kazemzadeh et al., 2023) and studies in the related species *P. aeruginosa* (Vo et al., 2020).

**Key findings:** Eight of the ten expected core biosynthetic steps are covered by high-confidence candidate genes (ubiC, ubiA, ubiX, ubiD, ubiH, ubiG, ubiE, coq7). Three important genes are absent from the candidate list but are expected to be present in the KT2440 genome: **UbiI** (C5-hydroxylase), **UbiB** (accessory kinase-like ATPase), and **UbiJ** (lipid-binding accessory factor). One candidate (VisC/PP_5197) has uncertain function. Five genes (hpd, PP_1218, PP_1644, PP_2789, PP_3720) are over-propagated KEGG map inclusions that do not participate in the strict UQ biosynthetic module. No direct biochemical experiments on UQ pathway enzymes have been reported specifically for KT2440; assignments rely on strong homology, comparative genomics, and pathway conservation within Pseudomonadota.

## 2. Target-Organism Pathway Definition

### 2.1 Biochemical Process

Ubiquinone biosynthesis encompasses the assembly of the benzoquinone head group from chorismate-derived 4-hydroxybenzoate (4-HB), attachment of a polyprenyl side chain (nonaprenyl in *Pseudomonas*), and sequential ring modifications including three hydroxylations (at C1, C5, and C6), two O-methylations, one C-methylation, and one decarboxylation (pierrel2022recentadvancesin pages 3-4, pierrel2022recentadvancesin pages 1-3). In *P. putida* KT2440, the product is UQ-9, consistent with the genus-wide predominance of Q-9 ubiquinones in *Pseudomonas*.

### 2.2 Pathway Boundaries

The strict UQ biosynthetic module begins with UbiC-catalyzed production of 4-HB from chorismate and ends with the terminal O-methylation yielding mature ubiquinone. The following neighboring pathways should be kept **separate**:

- **Chorismate/shikimate pathway** (upstream precursor supply)
- **Isoprenoid/MEP pathway** (polyprenyl diphosphate supply via IspB)
- **Homogentisate pathway** (aromatic amino acid catabolism, involving Hpd)
- **Menaquinone biosynthesis** (although UbiE participates in both)
- **Quinone redox utilization** (NAD(P)H:quinone oxidoreductases are quinone-consuming, not biosynthetic)
- **Tocopherol/plastoquinone pathways** (not expected in *Pseudomonas*)

KEGG map ppu00130 is substantially broader than the strict UQ biosynthesis module, encompassing terpenoid-quinone overview entries, homogentisate-related reactions, and generic quinone oxidoreductases (ariasbarrau2004thehomogentisatepathway pages 8-10, ariasbarrau2004thehomogentisatepathway pages 1-2).

### 2.3 Alternate Names and Database Definitions

The pathway is variously referred to as: Coenzyme Q biosynthesis, CoQ biosynthesis, ubiquinone biosynthesis. KEGG module M00117 ("Ubiquinone biosynthesis, prokaryotes") provides a narrower, more appropriate definition than ppu00130. MetaCyc pathway PWY-6708 ("Ubiquinol-9 biosynthesis") is the closest species-specific match.

## 3. Expected Step Model

The canonical aerobic UQ biosynthesis pathway in Gammaproteobacteria involves approximately 10 enzymatic steps plus accessory factors. Based on comparative genomics of UQ-hydroxylase diversification, *P. putida* KT2440 is expected to use the **UbiH/UbiI/Coq7** hydroxylase combination, which is characteristic of many Beta- and Gammaproteobacteria outside the Enterobacterales/Vibrionales clade that uses UbiH/UbiI/UbiF (kazemzadeh2023diversificationofubiquinone pages 8-9, kazemzadeh2023diversificationofubiquinone pages 2-3, kazemzadeh2023diversificationofubiquinone pages 1-2, kazemzadeh2023diversificationofubiquinone pages 9-11).

The following table maps each expected pathway step to candidate genes and curation status:

| Step Number | Reaction Description | Expected Enzyme(s) | Assigned KT2440 Gene(s) | Step Status | Notes on Evidence Quality |
|---|---|---|---|---|---|
| 1 | Chorismate → 4-hydroxybenzoate (4-HB) | UbiC chorismate lyase | **ubiC / PP_5317 / Q88C66** | covered | Canonical bacterial entry step to ubiquinone head-group biosynthesis; assignment in KT2440 is strong by homology and pathway logic, but direct biochemical evidence in KT2440 was not found (pierrel2022recentadvancesin pages 3-4, pierrel2022recentadvancesin pages 1-3, rodrigo2023roleofthe pages 1-5, fernandezdelrio2021coenzymeqbiosynthesis pages 7-9) |
| 2 | 4-HB → 3-polyprenyl-4-HB | UbiA 4-HB polyprenyltransferase | **ubiA / PP_5318 / Q88C65** | covered | Strong assignment; PP_5318 was specifically reported as upregulated during KT2440 resuscitation, linking the target strain to UQ demand, although enzymatic confirmation remains indirect (lopezlara2020influenceofrehydration pages 6-7, lopezlara2020influenceofrehydration pages 1-2, pierrel2022recentadvancesin pages 3-4, rodrigo2023roleofthe pages 1-5) |
| 3 | Prenyl-FMN cofactor synthesis for decarboxylation | UbiX flavin prenyltransferase | **ubiX / PP_0548 / Q88QE6** | covered | Canonical source of the prFMN cofactor needed by UbiD-family decarboxylases; inferred by strong conserved pathway architecture rather than target-strain experiment (pierrel2022recentadvancesin pages 3-4, pierrel2022recentadvancesin pages 4-5, rodrigo2023roleofthe pages 1-5) |
| 4 | Decarboxylation of polyprenyl-4-HB intermediate | UbiD decarboxylase | **ubiD / PP_5213 / Q88CG8** | covered | Conserved core step of bacterial UQ synthesis; assignment is strong from homology and pathway conservation, but no direct KT2440 mutant/biochemical evidence was located (pierrel2022recentadvancesin pages 3-4, pierrel2022recentadvancesin pages 4-5, rodrigo2023roleofthe pages 1-5) |
| 5 | C1-hydroxylation of prenylated phenolic intermediate | UbiH | **ubiH / PP_5199 / Q88CI2** | covered | Comparative genomics across Pseudomonadota supports a **UbiH/UbiI/Coq7** hydroxylase set in many Beta/Gamma-proteobacteria; transfer to KT2440 is strong but still comparative, not direct (kazemzadeh2023diversificationofubiquinone pages 8-9, kazemzadeh2023diversificationofubiquinone pages 2-3, pierrel2022recentadvancesin pages 3-4, vo2020theo2independentpathway pages 1-2, vo2020theo2independentpathway pages 7-8) |
| 6 | First O-methylation | UbiG O-methyltransferase | **ubiG / PP_1765 / Q88M10** | covered | UbiG is the canonical bifunctional O-methyltransferase in bacterial UQ pathways; step placement as the first O-methylation is pathway-consistent but not directly validated in KT2440 (staiano2023biosynthesisdeficiencyand pages 4-5, pierrel2022recentadvancesin pages 3-4) |
| 7 | C5-hydroxylation | UbiI | **No candidate in provided list** | gap | Important missing core hydroxylase from the candidate set. Comparative genomics predicts that a **UbiI-family** enzyme should exist in KT2440 if it follows the common Pseudomonas/Gammaproteobacterial **UbiH/UbiI/Coq7** pattern; this should trigger a genome re-check / fetch-gene search (kazemzadeh2023diversificationofubiquinone pages 8-9, kazemzadeh2023diversificationofubiquinone pages 2-3, pierrel2022recentadvancesin pages 3-4, vo2020theo2independentpathway pages 1-2, vo2020theo2independentpathway pages 7-8) |
| 8 | C-methylation of quinol ring | UbiE C-methyltransferase | **ubiE / PP_5011 / Q88D17** | covered | Canonical bacterial UQ C-methyltransferase; assignment is strong by conservation and enzyme family function, though direct KT2440 validation was not found (staiano2023biosynthesisdeficiencyand pages 4-5, pierrel2022recentadvancesin pages 3-4) |
| 9 | C6-hydroxylation | Coq7 or UbiF-family hydroxylase | **coq7 / PP_0427 / Q88QR1** | covered | Strong comparative assignment. In **P. aeruginosa**, Coq7 replaces UbiF for the aerobic C6-hydroxylation step, making transfer to KT2440 plausible and relatively strong within Pseudomonas (vo2020theo2independentpathway pages 7-8, kazemzadeh2023diversificationofubiquinone pages 8-9, vo2020theo2independentpathway pages 1-2) |
| 10 | Terminal O-methylation | UbiG O-methyltransferase | **ubiG / PP_1765 / Q88M10** | covered | Same gene likely catalyzes the second O-methylation as in other bacterial UQ pathways; assignment is strong at family level, indirect in KT2440 (staiano2023biosynthesisdeficiencyand pages 4-5, pierrel2022recentadvancesin pages 3-4) |
| 11 | Accessory membrane-associated UQ-biosynthesis factor | UbiB kinase-like/ATPase accessory protein | **No candidate in provided list** | gap | UbiB is broadly involved in bacterial UQ synthesis, likely facilitating membrane intermediate handling; absence from the candidate set suggests metadata incompleteness rather than true biological absence (vo2020theo2independentpathway pages 1-2, vo2020theo2independentpathway pages 1-1, staiano2023biosynthesisdeficiencyand pages 4-5, rodrigo2023roleofthe pages 1-5) |
| 12 | Lipid-binding/accessory scaffold factor | UbiJ | **No candidate in provided list** | gap | UbiJ is part of the canonical bacterial UQ accessory ensemble in related species including P. aeruginosa; missing from the candidate list likely reflects bucket incompleteness, not strong evidence of true absence (vo2020theo2independentpathway pages 1-2) |
| 13 | Putative anaerobic/alternative UQ-related factor | VisC-like oxidoreductase | **visC / PP_5197 / Q88CI4** | candidate_uncertain | Annotation suggests involvement in anaerobic UQ synthesis, but direct evidence in KT2440 is lacking and mapping to the established **UbiT/UbiU/UbiV** anaerobic system is unresolved. Should not be used to satisfy a core aerobic hydroxylation step without further review (vo2020theo2independentpathway pages 8-9, vo2020theo2independentpathway pages 7-8, ariascartin2023roleofthe pages 1-2, vo2020theo2independentpathway pages 3-4, vo2020theo2independentpathway pages 5-7) |


*Table: This table maps each expected ubiquinone biosynthesis step in Pseudomonas putida KT2440 to candidate genes and module-curation status. It highlights strong core assignments, likely metadata omissions such as UbiI/UbiB/UbiJ, and the unresolved status of VisC as a possible anaerobic-related factor.*

## 4. Candidate Genes and Evidence

### 4.1 Detailed Gene Assessment

| Gene Name | Locus Tag | UniProt | Proposed Pathway Role | Evidence Type | Confidence Level | Assessment for Module Curation | Key Notes/Caveats |
|---|---|---|---|---|---|---|---|
| ubiC | PP_5317 | Q88C66 | Chorismate lyase; forms 4-hydroxybenzoate head-group precursor | Homology from general bacterial CoQ pathway; KEGG annotation only in KT2440 | High | covered | UbiC is the canonical bacterial enzyme for chorismate → 4-HB, the standard entry step into UQ biosynthesis; no direct KT2440 biochemical test found, but assignment is strong (pierrel2022recentadvancesin pages 3-4, pierrel2022recentadvancesin pages 1-3, rodrigo2023roleofthe pages 1-5, fernandezdelrio2021coenzymeqbiosynthesis pages 7-9) |
| ubiA | PP_5318 | Q88C65 | 4-hydroxybenzoate polyprenyltransferase; attaches polyprenyl tail to 4-HB | Direct transcript evidence in KT2440 plus homology/review support | High | covered | PP_5318/ubiA was specifically reported as upregulated during KT2440 rehydration/resuscitation, linking it to UQ biosynthetic demand in the target strain; enzymatic role is canonical in bacteria (lopezlara2020influenceofrehydration pages 6-7, lopezlara2020influenceofrehydration pages 1-2, pierrel2022recentadvancesin pages 3-4, rodrigo2023roleofthe pages 1-5) |
| ubiX | PP_0548 | Q88QE6 | Flavin prenyltransferase producing prFMN cofactor for UbiD | Homology from general bacterial CoQ pathway; KEGG annotation only in KT2440 | High | covered | UbiX supplies the prenylated FMN cofactor required by UbiD-family decarboxylases; strong pathway logic but no direct KT2440 experiment found (pierrel2022recentadvancesin pages 3-4, pierrel2022recentadvancesin pages 4-5, rodrigo2023roleofthe pages 1-5) |
| ubiD | PP_5213 | Q88CG8 | 4-hydroxy-3-polyprenylbenzoate decarboxylase in UQ pathway | Homology from general bacterial CoQ pathway; KEGG annotation only in KT2440 | High | covered | UbiD acts with UbiX/prFMN in the conserved decarboxylation step after prenylation; role is canonical though direct KT2440 validation is lacking (pierrel2022recentadvancesin pages 3-4, pierrel2022recentadvancesin pages 4-5, rodrigo2023roleofthe pages 1-5) |
| ubiH | PP_5199 | Q88CI2 | UQ aromatic-ring hydroxylase, most likely C1-hydroxylase in the aerobic pathway | Homology from related species and comparative genomics | High | covered | Hydroxylase assignment is supported by broad proteobacterial patterns; Gammaproteobacteria including Pseudomonas commonly use UbiH/UbiI/Coq7 rather than UbiF for the three hydroxylations (vo2020theo2independentpathway pages 7-8, kazemzadeh2023diversificationofubiquinone pages 8-9, kazemzadeh2023diversificationofubiquinone pages 2-3, pierrel2022recentadvancesin pages 3-4, kazemzadeh2023diversificationofubiquinone pages 1-2, vo2020theo2independentpathway pages 1-2) |
| visC | PP_5197 | Q88CI4 | Proposed O2-independent/anaerobic UQ hydroxylation factor; likely analogous to anaerobic UQ pathway components rather than classic aerobic hydroxylase | KEGG/database annotation plus weak comparative inference | Medium | candidate_uncertain | Direct evidence for PP_5197 in KT2440 is lacking. Annotation as “oxidoreductase involved in anaerobic synthesis of ubiquinone” is plausible but unresolved; should not be used alone to satisfy an aerobic hydroxylation step. Relationship to established UbiUVT anaerobic systems remains unclear from available evidence (vo2020theo2independentpathway pages 8-9, vo2020theo2independentpathway pages 7-8, ariascartin2023roleofthe pages 1-2, vo2020theo2independentpathway pages 3-4, vo2020theo2independentpathway pages 5-7) |
| ubiG | PP_1765 | Q88M10 | Bifunctional O-methyltransferase for two O-methylation steps in UQ biosynthesis | Homology from general bacterial CoQ pathway; KEGG annotation only in KT2440 | High | covered | UbiG is the canonical bifunctional O-methyltransferase for the 5-O/6-O methylation reactions in bacterial UQ pathways; no direct KT2440 assay found (staiano2023biosynthesisdeficiencyand pages 4-5, rodrigo2023roleofthe pages 1-5, pierrel2022recentadvancesin pages 3-4) |
| ubiE | PP_5011 | Q88D17 | C-methyltransferase for C2 methylation of the UQ ring | Homology from general bacterial CoQ pathway; KEGG annotation only in KT2440 | High | covered | UbiE is the canonical C-methyltransferase in UQ biosynthesis and also participates in menaquinone-related chemistry in some bacteria; assignment is strong (staiano2023biosynthesisdeficiencyand pages 4-5, rodrigo2023roleofthe pages 1-5, pierrel2022recentadvancesin pages 3-4) |
| coq7 | PP_0427 | Q88QR1 | Diiron UQ hydroxylase; likely C6-hydroxylase replacing UbiF | Homology from related species and comparative genomics | High | covered | In P. aeruginosa, Coq7 functionally replaces UbiF in aerobic UQ biosynthesis; comparative genomics indicates many Beta/Gamma-proteobacteria, including Pseudomonas-lineage taxa, use UbiH/UbiI/Coq7 combinations (vo2020theo2independentpathway pages 7-8, kazemzadeh2023diversificationofubiquinone pages 8-9, kazemzadeh2023diversificationofubiquinone pages 2-3, pierrel2022recentadvancesin pages 3-4, kazemzadeh2023diversificationofubiquinone pages 1-2, vo2020theo2independentpathway pages 1-2) |
| hpd | PP_3433 | Q88HC7 | 4-hydroxyphenylpyruvate dioxygenase of the homogentisate pathway; aromatic amino acid catabolism | Direct experiment in Pseudomonas putida (species-level, catabolic pathway studies) | Over-annotation | not_expected_in_pathway | Strong literature shows hpd is for Tyr/Phe degradation to homogentisate, not for the strict UQ pathway. Its inclusion under KEGG ppu00130 reflects map breadth and precursor/catabolic neighborhood, not core UQ synthesis (ariasbarrau2004thehomogentisatepathway pages 8-10, ariasbarrau2004thehomogentisatepathway pages 1-2, verhoef2010comparativetranscriptomicsand pages 8-9, ariasbarrau2004thehomogentisatepathway pages 15-16) |
| PP_1218 | PP_1218 | Q88NI9 | Acyl-CoA thioesterase; no specific strict UQ biosynthetic role established | KEGG/database annotation only | Low | over-propagated | No evidence retrieved linking this thioesterase directly to conserved UQ biosynthetic chemistry; likely a broad map inclusion or nearby redox/lipid metabolism entry rather than a required module component (pierrel2022recentadvancesin pages 3-4, pierrel2022recentadvancesin pages 1-3) |
| PP_1644 | PP_1644 | Q88MC9 | NAD(P)H dehydrogenase (quinone); quinone redox metabolism, not synthesis | KEGG/database annotation only | Low | over-propagated | Quinone reductases/dehydrogenases interact with ubiquinone as electron carriers but are not part of head-group/tail assembly or ring-modification steps of biosynthesis; should be excluded from strict module satisfiability (lopezlara2020influenceofrehydration pages 6-7, lopezlara2020influenceofrehydration pages 1-2) |
| PP_2789 | PP_2789 | Q88J60 | Generic oxidoreductase; no defined step in canonical UQ pathway | KEGG/database annotation only | Low | over-propagated | No direct evidence for a role in UQ biosynthesis; likely over-propagated from broad KEGG map membership and should not count toward pathway completion (pierrel2022recentadvancesin pages 3-4, pierrel2022recentadvancesin pages 1-3) |
| PP_3720 | PP_3720 | Q88GK1 | NAD(P)H quinone oxidoreductase; quinone redox handling rather than UQ biosynthesis | KEGG/database annotation only | Low | over-propagated | As with PP_1644, this is best interpreted as a quinone-utilizing/redox enzyme, not a biosynthetic step enzyme. Keep separate from the strict UQ module (lopezlara2020influenceofrehydration pages 6-7, lopezlara2020influenceofrehydration pages 1-2) |


*Table: This table evaluates all 14 candidate genes associated with KEGG ppu00130 in Pseudomonas putida KT2440, separating high-confidence core ubiquinone biosynthesis genes from ambiguous anaerobic candidates and likely over-propagated annotations. It is useful for manual module satisfiability and annotation curation because it maps each candidate to evidence type, confidence, and a concrete curation decision.*

### 4.2 High-Confidence Core Pathway Genes

**ubiC (PP_5317, Q88C66):** Chorismate pyruvate-lyase catalyzing the one-step conversion of chorismate to 4-hydroxybenzoate. This is the canonical bacterial entry point to UQ head-group biosynthesis (pierrel2022recentadvancesin pages 3-4, pierrel2022recentadvancesin pages 1-3, fernandezdelrio2021coenzymeqbiosynthesis pages 7-9). The *P. putida* ubiC gene has also been exploited in metabolic engineering contexts for 4-HB production in related *Pseudomonas* species (pierrel2022recentadvancesin pages 4-5). **Evidence type:** Strong homology; no direct KT2440 biochemical assay.

**ubiA (PP_5318, Q88C65):** 4-Hydroxybenzoate octaprenyltransferase attaching the polyprenyl side chain. This is the only candidate gene with **direct transcriptomic evidence** in KT2440: López-Lara et al. (2020) reported upregulation of PP_5318/ubiA during rehydration-triggered resuscitation from a viable-but-nonculturable state, linking phenylalanine/tyrosine catabolism to UQ biosynthetic demand (lopezlara2020influenceofrehydration pages 6-7, lopezlara2020influenceofrehydration pages 1-2). **Evidence type:** Direct transcript evidence in KT2440.

**ubiX (PP_0548, Q88QE6):** Flavin prenyltransferase producing the prenylated FMN (prFMN) cofactor required by UbiD-family decarboxylases. The UbiX/UbiD system is well conserved across bacteria (pierrel2022recentadvancesin pages 3-4, pierrel2022recentadvancesin pages 4-5, rodrigo2023roleofthe pages 1-5). Note that PP_0548 is assigned a primary KEGG bucket of ppu00627, not ppu00130, reflecting the cofactor's dual role. **Evidence type:** Strong homology.

**ubiD (PP_5213, Q88CG8):** Polyprenyl-4-hydroxybenzoate decarboxylase utilizing the prFMN cofactor from UbiX. In E. coli, UbiD and UbiX co-migrate as a ~700 kDa complex (pierrel2022recentadvancesin pages 4-5). The UbiD enzyme family has been structurally characterized (Bailey et al., 2019) and the 1,3-dipolar cycloaddition mechanism with prFMN is well established (pierrel2022recentadvancesin pages 3-4, rodrigo2023roleofthe pages 1-5). **Evidence type:** Strong homology.

**ubiH (PP_5199, Q88CI2):** Flavin-dependent monooxygenase catalyzing C1-hydroxylation of 2-polyprenylphenol. Comparative genomics across 2,373 Pseudomonadota genomes confirms that UbiH is one of the most widely distributed UQ-hydroxylases outside Alphaproteobacteria (kazemzadeh2023diversificationofubiquinone pages 8-9, kazemzadeh2023diversificationofubiquinone pages 2-3, kazemzadeh2023diversificationofubiquinone pages 1-2). In *P. aeruginosa*, UbiH is confirmed as part of the aerobic hydroxylase triad (vo2020theo2independentpathway pages 7-8, vo2020theo2independentpathway pages 1-2). Transfer to *P. putida* KT2440 is **strong**. **Evidence type:** Strong comparative genomics within *Pseudomonas*.

**ubiG (PP_1765, Q88M10):** Bifunctional SAM-dependent O-methyltransferase catalyzing both 2-polyprenyl-6-hydroxyphenol methylation (early step) and 3-demethylubiquinol O-methylation (terminal step). UbiG (Coq3 in yeast) performs two O-methylation reactions using S-adenosyl-L-methionine as cofactor (staiano2023biosynthesisdeficiencyand pages 4-5, pierrel2022recentadvancesin pages 3-4). **Evidence type:** Strong homology.

**ubiE (PP_5011, Q88D17):** SAM-dependent C-methyltransferase catalyzing C2-methylation of the benzoquinol ring. UbiE also participates in menaquinone biosynthesis in bacteria, demonstrating pathway crosstalk (staiano2023biosynthesisdeficiencyand pages 4-5, pierrel2022recentadvancesin pages 3-4). **Evidence type:** Strong homology.

**coq7 (PP_0427, Q88QR1):** Diiron hydroxylase catalyzing C6-hydroxylation, functionally replacing UbiF. This is a critical lineage-specific feature: while E. coli uses the flavin monooxygenase UbiF for C6-hydroxylation, *P. aeruginosa* and many other Gammaproteobacteria outside Enterobacterales use the diiron enzyme Coq7 instead (vo2020theo2independentpathway pages 7-8, vo2020theo2independentpathway pages 1-2). Kazemzadeh et al. (2023) demonstrated that Coq7 orthologs from diverse proteobacterial classes possess C6-hydroxylase activity, with some showing weak additional C5-hydroxylase activity (kazemzadeh2023diversificationofubiquinone pages 3-6). The presence of Coq7 rather than UbiF in KT2440 is consistent with the Pseudomonadales-wide pattern. **Evidence type:** Strong comparative genomics; direct functional evidence from ortholog testing.

### 4.3 Uncertain Candidate

**visC (PP_5197, Q88CI4):** Annotated as an "oxidoreductase involved in anaerobic synthesis of ubiquinone" with a FAD/NAD(P)-binding domain. The annotation is suggestive but problematic. *P. putida* KT2440 is an obligate aerobe that lacks the denitrification capacity of *P. aeruginosa*. In *P. aeruginosa*, the anaerobic UQ pathway involves UbiT/UbiU/UbiV proteins (PA3911–PA3913), which are iron-sulfur cluster-containing enzymes that perform O2-independent hydroxylation (vo2020theo2independentpathway pages 8-9, vo2020theo2independentpathway pages 7-8, vo2020theo2independentpathway pages 1-1, vo2020theo2independentpathway pages 3-4). Whether PP_5197 is a true ortholog of any of these anaerobic components, or whether it serves a distinct aerobic role, remains unresolved. Its genomic proximity to ubiH (PP_5199) is notable but does not clarify function. **Recommendation:** Mark as `candidate_uncertain`; do not use to satisfy any core aerobic hydroxylation step.

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 Missing Core Pathway Genes

**UbiI (C5-hydroxylase):** This is the most significant gap in the candidate list. Comparative genomics strongly predicts that *P. putida* KT2440, as a member of the Gammaproteobacteria using the UbiH/UbiI/Coq7 hydroxylase combination, should encode a UbiI ortholog for C5-hydroxylation (kazemzadeh2023diversificationofubiquinone pages 8-9, kazemzadeh2023diversificationofubiquinone pages 2-3, kazemzadeh2023diversificationofubiquinone pages 1-2, kazemzadeh2023diversificationofubiquinone pages 9-11). In E. coli, UbiI performs the C5-hydroxylation step; in *P. aeruginosa*, UbiI is part of the confirmed aerobic hydroxylase set (vo2020theo2independentpathway pages 1-2, vo2020theo2independentpathway pages 7-8). The absence of UbiI from the 14-gene candidate list likely reflects an annotation gap in the KEGG ppu00130 bucket rather than genuine biological absence. **Action needed:** Genome search for UbiI ortholog.

**UbiB (accessory kinase-like ATPase):** UbiB is an atypical kinase-like protein with ATPase activity that is broadly involved in UQ biosynthesis across bacteria. Its proposed role is to extract quinone head intermediates from the membrane to facilitate enzymatic modification (staiano2023biosynthesisdeficiencyand pages 4-5, rodrigo2023roleofthe pages 1-5). In *P. aeruginosa*, UbiB is listed among the UQ biosynthetic proteins (vo2020theo2independentpathway pages 1-2, vo2020theo2independentpathway pages 1-1). Its absence from the KT2440 candidate list is likely a metadata gap. **Action needed:** Genome search for UbiB ortholog.

**UbiJ (lipid-binding accessory):** UbiJ is a lipid-binding protein that participates in the UQ biosynthetic multiprotein complex in E. coli and is present in *P. aeruginosa* (vo2020theo2independentpathway pages 1-2). Its absence from the candidate list likely reflects KEGG bucket scope rather than biological absence. **Action needed:** Genome search for UbiJ ortholog.

### 5.2 Over-Propagated Annotations

Five of the 14 candidates are not part of the strict UQ biosynthetic pathway and should be excluded from module satisfiability assessment:

**hpd (PP_3433, Q88HC7):** 4-Hydroxyphenylpyruvate dioxygenase is firmly established as part of the **homogentisate catabolic pathway** for L-phenylalanine and L-tyrosine degradation in *P. putida*, not UQ biosynthesis. Arias-Barrau et al. (2004) demonstrated that *hpd* mutants cannot grow on Phe/Tyr as sole carbon source but retain normal central metabolism (ariasbarrau2004thehomogentisatepathway pages 8-10, ariasbarrau2004thehomogentisatepathway pages 1-2). The gene is part of the hmgABC/hpd catabolic cassette (ariasbarrau2004thehomogentisatepathway pages 15-16). Its presence in KEGG ppu00130 reflects the broad "terpenoid-quinone" scope of the map, which includes tocopherol/plastoquinone precursor steps sharing the homogentisate intermediate; these are not relevant to *Pseudomonas* ubiquinone biosynthesis.

**PP_1644 (Q88MC9) and PP_3720 (Q88GK1):** Both encode NAD(P)H:quinone oxidoreductases. These enzymes **utilize** ubiquinone as a substrate/cofactor in redox reactions but do not catalyze any step in UQ ring assembly or modification. They are quinone-consuming enzymes, not biosynthetic pathway members.

**PP_1218 (Q88NI9):** Acyl-CoA thioesterase with no established connection to any conserved UQ biosynthetic step. Likely included in the KEGG map due to broad terpenoid-quinone metabolism scope.

**PP_2789 (Q88J60):** Generic oxidoreductase with no defined role in the canonical UQ pathway.

## 6. Module and GO-Curation Recommendations

### 6.1 Step Coverage Summary

| Status | Steps |
|--------|-------|
| **Covered** (8/10) | Steps 1–6, 8–10 (UbiC, UbiA, UbiX, UbiD, UbiH, UbiG×2, UbiE, Coq7) |
| **Gap** (1/10) | Step 7: C5-hydroxylation (UbiI missing from candidate list) |
| **Candidate_uncertain** (1) | VisC (PP_5197): unclear aerobic vs. anaerobic role |
| **Not_expected_in_pathway** (5) | hpd, PP_1218, PP_1644, PP_2789, PP_3720 |

### 6.2 Module Boundary Recommendations

- The generic KEGG map ppu00130 is too broad for strict UQ module satisfiability. A narrower module definition (analogous to KEGG M00117) should be used.
- The module should explicitly include UbiI, UbiB, and UbiJ as expected components, pending genome-level confirmation.
- Coq7 should be explicitly recognized as the C6-hydroxylase in *Pseudomonas*, replacing UbiF in the module definition for this taxon.
- VisC should be flagged for separate evaluation as a potential anaerobic pathway component, distinct from the core aerobic module.

### 6.3 Hydroxylase Diversification Context

Recent work by Kazemzadeh et al. (2023) analyzing 2,373 Pseudomonadota genomes and 5,044 UQ-flavin monooxygenase (FMO) sequences revealed that UQ hydroxylases diversified via at least three duplication events with neofunctionalization and subfunctionalization, producing six FMO subfamilies (UbiH, UbiI, UbiF, UbiL, UbiM, UbiN) plus the non-FMO diiron enzyme Coq7 (kazemzadeh2023diversificationofubiquinone pages 8-9, kazemzadeh2023diversificationofubiquinone pages 2-3, kazemzadeh2023diversificationofubiquinone pages 1-2, kazemzadeh2023diversificationofubiquinone pages 9-11). The ancestral repertoire consisted of a UbiL-like enzyme (C1/C5 activity) and Coq7 (C6 activity). In the lineage leading to Beta/Gammaproteobacteria, UbiL duplicated and subfunctionalized into UbiH (C1) and UbiI (C5), with UbiI later duplicating to give UbiF in Enterobacterales (kazemzadeh2023diversificationofubiquinone pages 9-11). This evolutionary framework strongly predicts the UbiH/UbiI/Coq7 combination in *P. putida*.

## 7. Genes to Promote to Full Review

The following genes warrant full `fetch-gene` review:

1. **UbiI ortholog (not in current candidate list):** Genome search needed to identify the C5-hydroxylase. This is the most critical gap for module completion.
2. **UbiB ortholog (not in current candidate list):** Search needed for the accessory kinase-like protein.
3. **UbiJ ortholog (not in current candidate list):** Search needed for the lipid-binding accessory factor.
4. **visC (PP_5197):** Full review needed to clarify whether this is an anaerobic UQ pathway component, an aerobic accessory, or a mis-annotated gene. Comparison with the UbiT/UbiU/UbiV system characterized in *P. aeruginosa* (vo2020theo2independentpathway pages 8-9, vo2020theo2independentpathway pages 7-8) and E. coli (ariascartin2023roleofthe pages 1-2, ariascartin2023roleofthe pages 17-20) should be performed.
5. **coq7 (PP_0427):** Promote for detailed review to confirm C6-hydroxylase assignment and assess any additional C5-hydroxylase activity, as some Coq7 orthologs show weak promiscuous activity (kazemzadeh2023diversificationofubiquinone pages 3-6).

## 8. Key References

1. **Kazemzadeh K, Pelosi L, et al.** (2023) "Diversification of Ubiquinone Biosynthesis via Gene Duplications, Transfers, Losses, and Parallel Evolution." *Mol Biol Evol* 40(10). DOI: 10.1093/molbev/msad219 (kazemzadeh2023diversificationofubiquinone pages 8-9, kazemzadeh2023diversificationofubiquinone pages 2-3, kazemzadeh2023diversificationofubiquinone pages 12-13, kazemzadeh2023diversificationofubiquinone pages 1-2, kazemzadeh2023diversificationofubiquinone pages 9-11, kazemzadeh2023diversificationofubiquinone pages 3-6, kazemzadeh2023diversificationofubiquinone pages 6-8)

2. **Vo CD, Michaud J, et al.** (2020) "The O2-independent pathway of ubiquinone biosynthesis is essential for denitrification in *Pseudomonas aeruginosa*." *J Biol Chem* 295:9021–9032. DOI: 10.1074/jbc.RA120.013748 (vo2020theo2independentpathway pages 7-8, vo2020theo2independentpathway pages 8-9, vo2020theo2independentpathway pages 1-1, vo2020theo2independentpathway pages 1-2, vo2020theo2independentpathway pages 3-4, vo2020theo2independentpathway pages 5-7)

3. **Arias-Cartin R, Kazemzadeh Ferizhendi K, et al.** (2023) "Role of the *Escherichia coli* ubiquinone-synthesizing UbiUVT pathway in adaptation to changing respiratory conditions." *mBio* 14(3). DOI: 10.1128/mbio.03298-22 (ariascartin2023roleofthe pages 1-2, ariascartin2023roleofthe pages 17-20, rodrigo2023roleofthe pages 1-5)

4. **Pierrel F, Burgardt A, et al.** (2022) "Recent advances in the metabolic pathways and microbial production of coenzyme Q." *World J Microbiol Biotechnol* 38(4). DOI: 10.1007/s11274-022-03242-3 (pierrel2022recentadvancesin pages 3-4, pierrel2022recentadvancesin pages 4-5, pierrel2022recentadvancesin pages 1-3)

5. **Staiano C, García-Corzo L, et al.** (2023) "Biosynthesis, Deficiency, and Supplementation of Coenzyme Q." *Antioxidants* 12:1469. DOI: 10.3390/antiox12071469 (staiano2023biosynthesisdeficiencyand pages 4-5)

6. **López-Lara LI, Pazos-Rojas LA, et al.** (2020) "Influence of rehydration on transcriptome during resuscitation of desiccated *Pseudomonas putida* KT2440." *Ann Microbiol* 70(1). DOI: 10.1186/s13213-020-01596-3 (lopezlara2020influenceofrehydration pages 6-7, lopezlara2020influenceofrehydration pages 1-2)

7. **Arias-Barrau E, Olivera ER, et al.** (2004) "The Homogentisate Pathway: a Central Catabolic Pathway Involved in the Degradation of L-Phenylalanine, L-Tyrosine, and 3-Hydroxyphenylacetate in *Pseudomonas putida*." *J Bacteriol* 186:5062–5077. DOI: 10.1128/JB.186.15.5062-5077.2004 (ariasbarrau2004thehomogentisatepathway pages 8-10, ariasbarrau2004thehomogentisatepathway pages 1-2, ariasbarrau2004thehomogentisatepathway pages 15-16)

8. **Fernández-del-Río L, Clarke CF** (2021) "Coenzyme Q Biosynthesis: An Update on the Origins of the Benzenoid Ring and Discovery of New Ring Precursors." *Metabolites* 11:385. DOI: 10.3390/metabo11060385 (fernandezdelrio2021coenzymeqbiosynthesis pages 5-7, fernandezdelrio2021coenzymeqbiosynthesis pages 7-9)

9. **Bailey SS, Payne KAP, et al.** (2019) "Enzymatic control of cycloadduct conformation ensures reversible 1,3-dipolar cycloaddition in a prFMN-dependent decarboxylase." *Nat Chem* 11:1049–1057. DOI: 10.1038/s41557-019-0324-8

10. **Verhoef S, Ballerstedt H, et al.** (2010) "Comparative transcriptomics and proteomics of p-hydroxybenzoate producing *Pseudomonas putida* S12." *Appl Microbiol Biotechnol* 87:679–690. DOI: 10.1007/s00253-010-2626-z (verhoef2010comparativetranscriptomicsand pages 8-9)


References

1. (pierrel2022recentadvancesin pages 3-4): Fabien Pierrel, Arthur Burgardt, Jin-Ho Lee, Ludovic Pelosi, and Volker F. Wendisch. Recent advances in the metabolic pathways and microbial production of coenzyme q. World Journal of Microbiology & Biotechnology, Feb 2022. URL: https://doi.org/10.1007/s11274-022-03242-3, doi:10.1007/s11274-022-03242-3. This article has 31 citations and is from a peer-reviewed journal.

2. (pierrel2022recentadvancesin pages 1-3): Fabien Pierrel, Arthur Burgardt, Jin-Ho Lee, Ludovic Pelosi, and Volker F. Wendisch. Recent advances in the metabolic pathways and microbial production of coenzyme q. World Journal of Microbiology & Biotechnology, Feb 2022. URL: https://doi.org/10.1007/s11274-022-03242-3, doi:10.1007/s11274-022-03242-3. This article has 31 citations and is from a peer-reviewed journal.

3. (ariasbarrau2004thehomogentisatepathway pages 8-10): Elsa Arias-Barrau, Elías R. Olivera, José M. Luengo, Cristina Fernández, Beatriz Galán, José L. García, Eduardo Díaz, and Baltasar Miñambres. The homogentisate pathway: a central catabolic pathway involved in the degradation of l-phenylalanine, l-tyrosine, and 3-hydroxyphenylacetate in pseudomonas putida. Journal of Bacteriology, 186:5062-5077, Aug 2004. URL: https://doi.org/10.1128/jb.186.15.5062-5077.2004, doi:10.1128/jb.186.15.5062-5077.2004. This article has 320 citations and is from a peer-reviewed journal.

4. (ariasbarrau2004thehomogentisatepathway pages 1-2): Elsa Arias-Barrau, Elías R. Olivera, José M. Luengo, Cristina Fernández, Beatriz Galán, José L. García, Eduardo Díaz, and Baltasar Miñambres. The homogentisate pathway: a central catabolic pathway involved in the degradation of l-phenylalanine, l-tyrosine, and 3-hydroxyphenylacetate in pseudomonas putida. Journal of Bacteriology, 186:5062-5077, Aug 2004. URL: https://doi.org/10.1128/jb.186.15.5062-5077.2004, doi:10.1128/jb.186.15.5062-5077.2004. This article has 320 citations and is from a peer-reviewed journal.

5. (kazemzadeh2023diversificationofubiquinone pages 8-9): Katayoun Kazemzadeh, Ludovic Pelosi, Clothilde Chenal, Sophie-Carole Chobert, Mahmoud Hajj Chehade, Margaux Jullien, Laura Flandrin, William Schmitt, Qiqi He, Emma Bouvet, Manon Jarzynka, Nelle Varoquaux, Ivan Junier, Fabien Pierrel, and Sophie S Abby. Diversification of ubiquinone biosynthesis via gene duplications, transfers, losses, and parallel evolution. Molecular Biology and Evolution, Oct 2023. URL: https://doi.org/10.1093/molbev/msad219, doi:10.1093/molbev/msad219. This article has 12 citations and is from a highest quality peer-reviewed journal.

6. (kazemzadeh2023diversificationofubiquinone pages 2-3): Katayoun Kazemzadeh, Ludovic Pelosi, Clothilde Chenal, Sophie-Carole Chobert, Mahmoud Hajj Chehade, Margaux Jullien, Laura Flandrin, William Schmitt, Qiqi He, Emma Bouvet, Manon Jarzynka, Nelle Varoquaux, Ivan Junier, Fabien Pierrel, and Sophie S Abby. Diversification of ubiquinone biosynthesis via gene duplications, transfers, losses, and parallel evolution. Molecular Biology and Evolution, Oct 2023. URL: https://doi.org/10.1093/molbev/msad219, doi:10.1093/molbev/msad219. This article has 12 citations and is from a highest quality peer-reviewed journal.

7. (kazemzadeh2023diversificationofubiquinone pages 1-2): Katayoun Kazemzadeh, Ludovic Pelosi, Clothilde Chenal, Sophie-Carole Chobert, Mahmoud Hajj Chehade, Margaux Jullien, Laura Flandrin, William Schmitt, Qiqi He, Emma Bouvet, Manon Jarzynka, Nelle Varoquaux, Ivan Junier, Fabien Pierrel, and Sophie S Abby. Diversification of ubiquinone biosynthesis via gene duplications, transfers, losses, and parallel evolution. Molecular Biology and Evolution, Oct 2023. URL: https://doi.org/10.1093/molbev/msad219, doi:10.1093/molbev/msad219. This article has 12 citations and is from a highest quality peer-reviewed journal.

8. (kazemzadeh2023diversificationofubiquinone pages 9-11): Katayoun Kazemzadeh, Ludovic Pelosi, Clothilde Chenal, Sophie-Carole Chobert, Mahmoud Hajj Chehade, Margaux Jullien, Laura Flandrin, William Schmitt, Qiqi He, Emma Bouvet, Manon Jarzynka, Nelle Varoquaux, Ivan Junier, Fabien Pierrel, and Sophie S Abby. Diversification of ubiquinone biosynthesis via gene duplications, transfers, losses, and parallel evolution. Molecular Biology and Evolution, Oct 2023. URL: https://doi.org/10.1093/molbev/msad219, doi:10.1093/molbev/msad219. This article has 12 citations and is from a highest quality peer-reviewed journal.

9. (rodrigo2023roleofthe pages 1-5): Arias-Cartin Rodrigo, Kazemzadeh Ferizhendi Katayoun, Séchet Emmanuel, Pelosi Ludovic, Loeuillet Corinne, Pierrel Fabien, Barras Frédéric, and Bouveret Emmanuelle. Role of the escherichia coli ubiquinone-synthesizing ubiuvt pathway in adaptation to changing respiratory conditions. bioRxiv, Mar 2023. URL: https://doi.org/10.1101/2023.03.15.532739, doi:10.1101/2023.03.15.532739. This article has 2 citations.

10. (fernandezdelrio2021coenzymeqbiosynthesis pages 7-9): Lucía Fernández-del-Río and Catherine F. Clarke. Coenzyme q biosynthesis: an update on the origins of the benzenoid ring and discovery of new ring precursors. Metabolites, 11:385, Jun 2021. URL: https://doi.org/10.3390/metabo11060385, doi:10.3390/metabo11060385. This article has 56 citations.

11. (lopezlara2020influenceofrehydration pages 6-7): Lilia I. López-Lara, Laura A. Pazos-Rojas, Lesther E. López-Cruz, Yolanda E. Morales-García, Verónica Quintero-Hernández, Jesús de la Torre, Pieter van Dillewijn, Jesús Muñoz-Rojas, and Antonino Baez. Influence of rehydration on transcriptome during resuscitation of desiccated pseudomonas putida kt2440. Annals of Microbiology, Sep 2020. URL: https://doi.org/10.1186/s13213-020-01596-3, doi:10.1186/s13213-020-01596-3. This article has 16 citations and is from a peer-reviewed journal.

12. (lopezlara2020influenceofrehydration pages 1-2): Lilia I. López-Lara, Laura A. Pazos-Rojas, Lesther E. López-Cruz, Yolanda E. Morales-García, Verónica Quintero-Hernández, Jesús de la Torre, Pieter van Dillewijn, Jesús Muñoz-Rojas, and Antonino Baez. Influence of rehydration on transcriptome during resuscitation of desiccated pseudomonas putida kt2440. Annals of Microbiology, Sep 2020. URL: https://doi.org/10.1186/s13213-020-01596-3, doi:10.1186/s13213-020-01596-3. This article has 16 citations and is from a peer-reviewed journal.

13. (pierrel2022recentadvancesin pages 4-5): Fabien Pierrel, Arthur Burgardt, Jin-Ho Lee, Ludovic Pelosi, and Volker F. Wendisch. Recent advances in the metabolic pathways and microbial production of coenzyme q. World Journal of Microbiology & Biotechnology, Feb 2022. URL: https://doi.org/10.1007/s11274-022-03242-3, doi:10.1007/s11274-022-03242-3. This article has 31 citations and is from a peer-reviewed journal.

14. (vo2020theo2independentpathway pages 1-2): Chau-Duy-Tam Vo, Julie Michaud, Sylvie Elsen, Bruno Faivre, Emmanuelle Bouveret, Frédéric Barras, Marc Fontecave, Fabien Pierrel, Murielle Lombard, and Ludovic Pelosi. The o2-independent pathway of ubiquinone biosynthesis is essential for denitrification in pseudomonas aeruginosa. Jul 2020. URL: https://doi.org/10.1074/jbc.ra120.013748, doi:10.1074/jbc.ra120.013748. This article has 37 citations and is from a domain leading peer-reviewed journal.

15. (vo2020theo2independentpathway pages 7-8): Chau-Duy-Tam Vo, Julie Michaud, Sylvie Elsen, Bruno Faivre, Emmanuelle Bouveret, Frédéric Barras, Marc Fontecave, Fabien Pierrel, Murielle Lombard, and Ludovic Pelosi. The o2-independent pathway of ubiquinone biosynthesis is essential for denitrification in pseudomonas aeruginosa. Jul 2020. URL: https://doi.org/10.1074/jbc.ra120.013748, doi:10.1074/jbc.ra120.013748. This article has 37 citations and is from a domain leading peer-reviewed journal.

16. (staiano2023biosynthesisdeficiencyand pages 4-5): Carmine Staiano, Laura García-Corzo, David Mantle, Nadia Turton, Lauren E. Millichap, Gloria Brea-Calvo, and Iain Hargreaves. Biosynthesis, deficiency, and supplementation of coenzyme q. Antioxidants, 12:1469, Jul 2023. URL: https://doi.org/10.3390/antiox12071469, doi:10.3390/antiox12071469. This article has 25 citations.

17. (vo2020theo2independentpathway pages 1-1): Chau-Duy-Tam Vo, Julie Michaud, Sylvie Elsen, Bruno Faivre, Emmanuelle Bouveret, Frédéric Barras, Marc Fontecave, Fabien Pierrel, Murielle Lombard, and Ludovic Pelosi. The o2-independent pathway of ubiquinone biosynthesis is essential for denitrification in pseudomonas aeruginosa. Jul 2020. URL: https://doi.org/10.1074/jbc.ra120.013748, doi:10.1074/jbc.ra120.013748. This article has 37 citations and is from a domain leading peer-reviewed journal.

18. (vo2020theo2independentpathway pages 8-9): Chau-Duy-Tam Vo, Julie Michaud, Sylvie Elsen, Bruno Faivre, Emmanuelle Bouveret, Frédéric Barras, Marc Fontecave, Fabien Pierrel, Murielle Lombard, and Ludovic Pelosi. The o2-independent pathway of ubiquinone biosynthesis is essential for denitrification in pseudomonas aeruginosa. Jul 2020. URL: https://doi.org/10.1074/jbc.ra120.013748, doi:10.1074/jbc.ra120.013748. This article has 37 citations and is from a domain leading peer-reviewed journal.

19. (ariascartin2023roleofthe pages 1-2): Rodrigo Arias-Cartin, Katayoun Kazemzadeh Ferizhendi, Emmanuel Séchet, Ludovic Pelosi, Corinne Loeuillet, Fabien Pierrel, Frédéric Barras, and Emmanuelle Bouveret. Role of the escherichia coli ubiquinone-synthesizing ubiuvt pathway in adaptation to changing respiratory conditions. mBio, Jun 2023. URL: https://doi.org/10.1128/mbio.03298-22, doi:10.1128/mbio.03298-22. This article has 18 citations and is from a domain leading peer-reviewed journal.

20. (vo2020theo2independentpathway pages 3-4): Chau-Duy-Tam Vo, Julie Michaud, Sylvie Elsen, Bruno Faivre, Emmanuelle Bouveret, Frédéric Barras, Marc Fontecave, Fabien Pierrel, Murielle Lombard, and Ludovic Pelosi. The o2-independent pathway of ubiquinone biosynthesis is essential for denitrification in pseudomonas aeruginosa. Jul 2020. URL: https://doi.org/10.1074/jbc.ra120.013748, doi:10.1074/jbc.ra120.013748. This article has 37 citations and is from a domain leading peer-reviewed journal.

21. (vo2020theo2independentpathway pages 5-7): Chau-Duy-Tam Vo, Julie Michaud, Sylvie Elsen, Bruno Faivre, Emmanuelle Bouveret, Frédéric Barras, Marc Fontecave, Fabien Pierrel, Murielle Lombard, and Ludovic Pelosi. The o2-independent pathway of ubiquinone biosynthesis is essential for denitrification in pseudomonas aeruginosa. Jul 2020. URL: https://doi.org/10.1074/jbc.ra120.013748, doi:10.1074/jbc.ra120.013748. This article has 37 citations and is from a domain leading peer-reviewed journal.

22. (verhoef2010comparativetranscriptomicsand pages 8-9): Suzanne Verhoef, Hendrik Ballerstedt, Rita J. M. Volkers, Johannes H. de Winde, and Harald J. Ruijssenaars. Comparative transcriptomics and proteomics of p-hydroxybenzoate producing pseudomonas putida s12: novel responses and implications for strain improvement. Applied Microbiology and Biotechnology, 87:679-690, May 2010. URL: https://doi.org/10.1007/s00253-010-2626-z, doi:10.1007/s00253-010-2626-z. This article has 92 citations and is from a domain leading peer-reviewed journal.

23. (ariasbarrau2004thehomogentisatepathway pages 15-16): Elsa Arias-Barrau, Elías R. Olivera, José M. Luengo, Cristina Fernández, Beatriz Galán, José L. García, Eduardo Díaz, and Baltasar Miñambres. The homogentisate pathway: a central catabolic pathway involved in the degradation of l-phenylalanine, l-tyrosine, and 3-hydroxyphenylacetate in pseudomonas putida. Journal of Bacteriology, 186:5062-5077, Aug 2004. URL: https://doi.org/10.1128/jb.186.15.5062-5077.2004, doi:10.1128/jb.186.15.5062-5077.2004. This article has 320 citations and is from a peer-reviewed journal.

24. (kazemzadeh2023diversificationofubiquinone pages 3-6): Katayoun Kazemzadeh, Ludovic Pelosi, Clothilde Chenal, Sophie-Carole Chobert, Mahmoud Hajj Chehade, Margaux Jullien, Laura Flandrin, William Schmitt, Qiqi He, Emma Bouvet, Manon Jarzynka, Nelle Varoquaux, Ivan Junier, Fabien Pierrel, and Sophie S Abby. Diversification of ubiquinone biosynthesis via gene duplications, transfers, losses, and parallel evolution. Molecular Biology and Evolution, Oct 2023. URL: https://doi.org/10.1093/molbev/msad219, doi:10.1093/molbev/msad219. This article has 12 citations and is from a highest quality peer-reviewed journal.

25. (ariascartin2023roleofthe pages 17-20): Rodrigo Arias-Cartin, Katayoun Kazemzadeh Ferizhendi, Emmanuel Séchet, Ludovic Pelosi, Corinne Loeuillet, Fabien Pierrel, Frédéric Barras, and Emmanuelle Bouveret. Role of the escherichia coli ubiquinone-synthesizing ubiuvt pathway in adaptation to changing respiratory conditions. mBio, Jun 2023. URL: https://doi.org/10.1128/mbio.03298-22, doi:10.1128/mbio.03298-22. This article has 18 citations and is from a domain leading peer-reviewed journal.

26. (kazemzadeh2023diversificationofubiquinone pages 12-13): Katayoun Kazemzadeh, Ludovic Pelosi, Clothilde Chenal, Sophie-Carole Chobert, Mahmoud Hajj Chehade, Margaux Jullien, Laura Flandrin, William Schmitt, Qiqi He, Emma Bouvet, Manon Jarzynka, Nelle Varoquaux, Ivan Junier, Fabien Pierrel, and Sophie S Abby. Diversification of ubiquinone biosynthesis via gene duplications, transfers, losses, and parallel evolution. Molecular Biology and Evolution, Oct 2023. URL: https://doi.org/10.1093/molbev/msad219, doi:10.1093/molbev/msad219. This article has 12 citations and is from a highest quality peer-reviewed journal.

27. (kazemzadeh2023diversificationofubiquinone pages 6-8): Katayoun Kazemzadeh, Ludovic Pelosi, Clothilde Chenal, Sophie-Carole Chobert, Mahmoud Hajj Chehade, Margaux Jullien, Laura Flandrin, William Schmitt, Qiqi He, Emma Bouvet, Manon Jarzynka, Nelle Varoquaux, Ivan Junier, Fabien Pierrel, and Sophie S Abby. Diversification of ubiquinone biosynthesis via gene duplications, transfers, losses, and parallel evolution. Molecular Biology and Evolution, Oct 2023. URL: https://doi.org/10.1093/molbev/msad219, doi:10.1093/molbev/msad219. This article has 12 citations and is from a highest quality peer-reviewed journal.

28. (fernandezdelrio2021coenzymeqbiosynthesis pages 5-7): Lucía Fernández-del-Río and Catherine F. Clarke. Coenzyme q biosynthesis: an update on the origins of the benzenoid ring and discovery of new ring precursors. Metabolites, 11:385, Jun 2021. URL: https://doi.org/10.3390/metabo11060385, doi:10.3390/metabo11060385. This article has 56 citations.

## Artifacts

- [Edison artifact artifact-00](PSEPK__ubiquinone_biosynthesis__ppu00130-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PSEPK__ubiquinone_biosynthesis__ppu00130-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. pierrel2022recentadvancesin pages 4-5
2. kazemzadeh2023diversificationofubiquinone pages 3-6
3. ariasbarrau2004thehomogentisatepathway pages 15-16
4. kazemzadeh2023diversificationofubiquinone pages 9-11
5. staiano2023biosynthesisdeficiencyand pages 4-5
6. verhoef2010comparativetranscriptomicsand pages 8-9
7. pierrel2022recentadvancesin pages 3-4
8. pierrel2022recentadvancesin pages 1-3
9. ariasbarrau2004thehomogentisatepathway pages 8-10
10. ariasbarrau2004thehomogentisatepathway pages 1-2
11. kazemzadeh2023diversificationofubiquinone pages 8-9
12. kazemzadeh2023diversificationofubiquinone pages 2-3
13. kazemzadeh2023diversificationofubiquinone pages 1-2
14. rodrigo2023roleofthe pages 1-5
15. fernandezdelrio2021coenzymeqbiosynthesis pages 7-9
16. lopezlara2020influenceofrehydration pages 6-7
17. lopezlara2020influenceofrehydration pages 1-2
18. ariascartin2023roleofthe pages 1-2
19. ariascartin2023roleofthe pages 17-20
20. kazemzadeh2023diversificationofubiquinone pages 12-13
21. kazemzadeh2023diversificationofubiquinone pages 6-8
22. fernandezdelrio2021coenzymeqbiosynthesis pages 5-7
23. https://doi.org/10.1007/s11274-022-03242-3,
24. https://doi.org/10.1128/jb.186.15.5062-5077.2004,
25. https://doi.org/10.1093/molbev/msad219,
26. https://doi.org/10.1101/2023.03.15.532739,
27. https://doi.org/10.3390/metabo11060385,
28. https://doi.org/10.1186/s13213-020-01596-3,
29. https://doi.org/10.1074/jbc.ra120.013748,
30. https://doi.org/10.3390/antiox12071469,
31. https://doi.org/10.1128/mbio.03298-22,
32. https://doi.org/10.1007/s00253-010-2626-z,