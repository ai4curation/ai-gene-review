---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T17:43:41.044965'
end_time: '2026-07-18T18:02:59.140224'
duration_seconds: 1158.1
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Ubiquinone biosynthesis from chorismate-derived 4-hydroxybenzoate
  module_summary: Species-neutral pathway for de novo biosynthesis of ubiquinone (coenzyme
    Q) from the chorismate-derived aromatic head group 4-hydroxybenzoate and a polyprenyl
    diphosphate side chain. The bacterial pathway begins with UbiC chorismate lyase,
    UbiA polyprenyltransferase, and UbiD-dependent decarboxylation, with UbiX providing
    the prenylated-FMN cofactor required by UbiD-family decarboxylases. Subsequent
    hydroxylation and methylation steps, carried out by UbiH/VisC/Coq7-like monooxygenases
    and UbiG/UbiE methyltransferases, tailor the prenylated aromatic ring to mature
    ubiquinone.
  module_outline: "- Ubiquinone biosynthesis\n  - 1. aromatic head-group synthesis\n\
    \  - 4-hydroxybenzoate formation from chorismate\n    - UbiC: chorismate lyase\
    \ (molecular player: UbiC chorismate lyase family; activity or role: chorismate\
    \ lyase activity)\n  - 2. polyprenyl side-chain attachment\n  - Polyprenylation\
    \ of 4-hydroxybenzoate\n    - UbiA: 4-hydroxybenzoate polyprenyltransferase (molecular\
    \ player: UbiA 4-hydroxybenzoate polyprenyltransferase family; activity or role:\
    \ 4-hydroxybenzoate polyprenyltransferase activity)\n  - 3. UbiD decarboxylation\
    \ and prFMN cofactor supply\n  - prFMN-dependent decarboxylation\n    - UbiX:\
    \ flavin prenyltransferase (molecular player: UbiX flavin prenyltransferase family;\
    \ activity or role: flavin prenyltransferase activity)\n    - UbiD: 4-hydroxy-3-polyprenylbenzoate\
    \ decarboxylase (molecular player: UbiD prFMN-dependent decarboxylase family;\
    \ activity or role: 4-hydroxy-3-polyprenylbenzoate decarboxylase activity)\n \
    \ - 4. aromatic ring hydroxylation\n  - Hydroxylation of prenylated ubiquinone\
    \ intermediates\n    - UbiH/VisC-family: 2-polyprenylphenol 6-hydroxylase (molecular\
    \ player: UbiH/VisC ubiquinone hydroxylase family; activity or role: 2-polyprenylphenol\
    \ 6-hydroxylase activity)\n    - UbiH: 2-octaprenyl-6-methoxyphenol hydroxylase\
    \ (molecular player: UbiH/VisC ubiquinone hydroxylase family; activity or role:\
    \ 2-octaprenyl-6-methoxyphenol hydroxylase activity)\n    - Coq7: 3-demethoxyubiquinol\
    \ 3-hydroxylase (molecular player: Coq7 demethoxyubiquinol hydroxylase family;\
    \ activity or role: 3-demethoxyubiquinol 3-hydroxylase activity)\n  - 5. aromatic\
    \ ring methylation\n  - O- and C-methylation of ubiquinone intermediates\n   \
    \ - UbiG: 2-polyprenyl-6-hydroxyphenol methylase (molecular player: UbiG ubiquinone\
    \ O-methyltransferase family; activity or role: 2-polyprenyl-6-hydroxyphenol methylase\
    \ activity)\n    - UbiE: 2-methoxy-6-polyprenyl-1,4-benzoquinol methyltransferase\
    \ (molecular player: UbiE/Coq5 ubiquinone C-methyltransferase family; activity\
    \ or role: 2-methoxy-6-polyprenyl-1,4-benzoquinol methyltransferase activity)\n\
    \    - UbiG: 3-demethylubiquinol 3-O-methyltransferase (molecular player: UbiG\
    \ ubiquinone O-methyltransferase family; activity or role: 3-demethylubiquinol\
    \ 3-O-methyltransferase activity)"
  module_connections: '- 4-hydroxybenzoate formation from chorismate feeds into Polyprenylation
    of 4-hydroxybenzoate

    - Polyprenylation of 4-hydroxybenzoate feeds into prFMN-dependent decarboxylation

    - UbiX: flavin prenyltransferase feeds into UbiD: 4-hydroxy-3-polyprenylbenzoate
    decarboxylase

    - prFMN-dependent decarboxylation feeds into Hydroxylation of prenylated ubiquinone
    intermediates

    - Hydroxylation of prenylated ubiquinone intermediates feeds into O- and C-methylation
    of ubiquinone intermediates'
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
citation_count: 10
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__ubiquinone_biosynthesis__ppu00130-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__ubiquinone_biosynthesis__ppu00130-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Ubiquinone biosynthesis from chorismate-derived 4-hydroxybenzoate in Pseudomonas putida KT2440

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

Species-neutral pathway for de novo biosynthesis of ubiquinone (coenzyme Q) from the chorismate-derived aromatic head group 4-hydroxybenzoate and a polyprenyl diphosphate side chain. The bacterial pathway begins with UbiC chorismate lyase, UbiA polyprenyltransferase, and UbiD-dependent decarboxylation, with UbiX providing the prenylated-FMN cofactor required by UbiD-family decarboxylases. Subsequent hydroxylation and methylation steps, carried out by UbiH/VisC/Coq7-like monooxygenases and UbiG/UbiE methyltransferases, tailor the prenylated aromatic ring to mature ubiquinone.

### Provisional Biological Outline

- Ubiquinone biosynthesis
  - 1. aromatic head-group synthesis
  - 4-hydroxybenzoate formation from chorismate
    - UbiC: chorismate lyase (molecular player: UbiC chorismate lyase family; activity or role: chorismate lyase activity)
  - 2. polyprenyl side-chain attachment
  - Polyprenylation of 4-hydroxybenzoate
    - UbiA: 4-hydroxybenzoate polyprenyltransferase (molecular player: UbiA 4-hydroxybenzoate polyprenyltransferase family; activity or role: 4-hydroxybenzoate polyprenyltransferase activity)
  - 3. UbiD decarboxylation and prFMN cofactor supply
  - prFMN-dependent decarboxylation
    - UbiX: flavin prenyltransferase (molecular player: UbiX flavin prenyltransferase family; activity or role: flavin prenyltransferase activity)
    - UbiD: 4-hydroxy-3-polyprenylbenzoate decarboxylase (molecular player: UbiD prFMN-dependent decarboxylase family; activity or role: 4-hydroxy-3-polyprenylbenzoate decarboxylase activity)
  - 4. aromatic ring hydroxylation
  - Hydroxylation of prenylated ubiquinone intermediates
    - UbiH/VisC-family: 2-polyprenylphenol 6-hydroxylase (molecular player: UbiH/VisC ubiquinone hydroxylase family; activity or role: 2-polyprenylphenol 6-hydroxylase activity)
    - UbiH: 2-octaprenyl-6-methoxyphenol hydroxylase (molecular player: UbiH/VisC ubiquinone hydroxylase family; activity or role: 2-octaprenyl-6-methoxyphenol hydroxylase activity)
    - Coq7: 3-demethoxyubiquinol 3-hydroxylase (molecular player: Coq7 demethoxyubiquinol hydroxylase family; activity or role: 3-demethoxyubiquinol 3-hydroxylase activity)
  - 5. aromatic ring methylation
  - O- and C-methylation of ubiquinone intermediates
    - UbiG: 2-polyprenyl-6-hydroxyphenol methylase (molecular player: UbiG ubiquinone O-methyltransferase family; activity or role: 2-polyprenyl-6-hydroxyphenol methylase activity)
    - UbiE: 2-methoxy-6-polyprenyl-1,4-benzoquinol methyltransferase (molecular player: UbiE/Coq5 ubiquinone C-methyltransferase family; activity or role: 2-methoxy-6-polyprenyl-1,4-benzoquinol methyltransferase activity)
    - UbiG: 3-demethylubiquinol 3-O-methyltransferase (molecular player: UbiG ubiquinone O-methyltransferase family; activity or role: 3-demethylubiquinol 3-O-methyltransferase activity)

### Known Relationships Among Steps

- 4-hydroxybenzoate formation from chorismate feeds into Polyprenylation of 4-hydroxybenzoate
- Polyprenylation of 4-hydroxybenzoate feeds into prFMN-dependent decarboxylation
- UbiX: flavin prenyltransferase feeds into UbiD: 4-hydroxy-3-polyprenylbenzoate decarboxylase
- prFMN-dependent decarboxylation feeds into Hydroxylation of prenylated ubiquinone intermediates
- Hydroxylation of prenylated ubiquinone intermediates feeds into O- and C-methylation of ubiquinone intermediates

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

# Ubiquinone Biosynthesis from Chorismate-Derived 4-Hydroxybenzoate in *Pseudomonas putida* KT2440

**Commissioned Module/Pathway/Taxon Review — KEGG ppu00130 (cofactors_vitamins_redox)**
Target taxon: *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)

---

## 1. Executive Summary

The de novo ubiquinone (coenzyme Q, in this strain **UQ-9**) biosynthetic pathway from the chorismate-derived aromatic head group **4-hydroxybenzoate (4-HB)** is **fully satisfiable** in *P. putida* KT2440. Every canonical step of the bacterial Ubi pathway maps to a conserved, syntenically plausible gene in the KT2440 proteome: chorismate lyase (**UbiC**, PP_5317), 4-HB polyprenyltransferase (**UbiA**, PP_5318), the prFMN-dependent decarboxylation module (**UbiX**, PP_0548, supplying prenylated-FMN to **UbiD**, PP_5213), the three aerobic ring hydroxylations (**VisC/UbiI**, PP_5197; **UbiH**, PP_5199; and a **Coq7-type** enzyme, PP_0427, substituting for the flavin-dependent UbiF that is absent from this genome), and the two ring methylations (O-methyltransferase **UbiG**, PP_1765; C-methyltransferase **UbiE**, PP_5011). The polyprenyl (nonaprenyl) side chain is supplied by IspB (PP_0687), which lies outside the KEGG map.

Two curation-critical corrections to the supplied metadata are warranted. **First, the candidate list is incomplete**: it omits three accessory/regulatory factors that are present in the proteome and are integral to *Pseudomonas*/proteobacterial UQ biosynthesis — the atypical kinase **UbiB** (PP_5013), and the lipid-binding assembly factors **UbiJ** (PP_5012) and **UbiK** (PP_5235). Notably, *ubiE–ubiJ–ubiB* form a contiguous cluster (PP_5011–PP_5012–PP_5013), strong syntenic support for their functional linkage. **Second, the candidate list is inflated** by five map-boundary artifacts that are not part of de novo UQ biosynthesis from 4-HB: *hpd* (PP_3433, a homogentisate/tyrosine-catabolism dioxygenase belonging to the tocopherol–plastoquinone branch), the acyl-CoA/4-hydroxybenzoyl-CoA thioesterase PP_1218, and three NAD(P)H:quinone oxidoreductases (PP_1644, PP_2789, PP_3720) that *use* quinones rather than *synthesize* them. These arise because KEGG ppu00130 is the lumped map "Ubiquinone **and other terpenoid-quinone** biosynthesis."

The single most important caveat for curators is that **all 14 candidate annotations are homology-inferred (UniProt PE=3)**, with no protein- or transcript-level experimental evidence in KT2440 itself. The pathway is confidently reconstructed by orthology, KEGG KO assignment, and strong transfer from the well-characterized *Escherichia coli* and *Pseudomonas aeruginosa* systems, but not by direct KT2440 biochemistry or genetics. A published genome-wide RB-TnSeq fitness resource for KT2440 offers the fastest route to convert these homology calls into strain-specific functional evidence.

---

## 2. Target-Organism Pathway Definition

**Included process.** This review covers **de novo aerobic biosynthesis of ubiquinone** starting from **chorismate** (via 4-hydroxybenzoate) and a **polyprenyl diphosphate** side chain, through to mature UQ-9. The chemically defined scope is: (i) 4-HB formation from chorismate; (ii) prenylation of 4-HB; (iii) prFMN-dependent decarboxylation (with UbiX supplying the cofactor to UbiD); (iv) three contiguous aromatic-ring hydroxylations; and (v) the O- and C-methylations that decorate the ring. In *P. putida* KT2440 the isoprenoid tail is **nonaprenyl (C45)**, giving UQ-9, consistent with other pseudomonads.

**Neighboring pathways to keep separate.** KEGG map **ppu00130 is deliberately broad** — "Ubiquinone *and other terpenoid-quinone* biosynthesis" — and co-locates enzymes for **menaquinone**, **tocopherol**, **phylloquinone**, and **plastoquinone**. For a KT2440-specific UQ module these must be excluded:
- **Menaquinone (MK)** biosynthesis: not present in KT2440 (proteome searches for *menA* and *menD* return zero hits), consistent with a strict aerobe that respires exclusively via UQ.
- **Tocopherol/plastoquinone branch**: the *hpd* gene (4-hydroxyphenylpyruvate dioxygenase, PP_3433) belongs to **tyrosine catabolism / homogentisate** metabolism, not de novo UQ from 4-HB.
- **Chorismate biosynthesis (shikimate pathway)** upstream and **quinone *utilization*** (respiratory NAD(P)H:quinone oxidoreductases) downstream should be treated as adjacent pathways, not part of this module.

**Alternate names / database definitions.** The pathway is variously called ubiquinone biosynthesis, coenzyme Q biosynthesis, and (in this strain) UQ-9 biosynthesis. Gene-name synonymy that curators must reconcile includes **VisC = UbiI** (the C5/2-methoxy-6-polyprenylphenol hydroxylase; "VisC" is the historical name) and the substitution of a **Coq7-type hydroxylase (EC 1.14.99.60)** for the reaction otherwise assigned to the flavin monooxygenase **UbiF (EC 1.14.13.-)** in *E. coli*.

---

## 3. Expected Step Model

The species-neutral outline maps onto KT2440 genes as follows. The pathway topology (which step feeds which) is preserved; only the enzyme identity at the C6-hydroxylation step differs from the *E. coli* paradigm.

```
Chorismate
   │  UbiC (PP_5317)  chorismate lyase (EC 4.1.3.40)
   ▼
4-Hydroxybenzoate  ───+ nonaprenyl-PP (from IspB / PP_0687, outside map)
   │  UbiA (PP_5318)  4-HB polyprenyltransferase (EC 2.5.1.39)
   ▼
3-nonaprenyl-4-hydroxybenzoate
   │  UbiD (PP_5213)  prFMN-dependent decarboxylase (EC 4.1.1.98)
   │  UbiX (PP_0548)  supplies prenylated-FMN cofactor (EC 2.5.1.129)
   ▼
2-nonaprenylphenol
   │  three CONTIGUOUS aromatic ring hydroxylations (aerobic):
   │    VisC/UbiI (PP_5197)  C5 hydroxylase (EC 1.14.13.240)
   │    UbiH      (PP_5199)  C6 hydroxylase
   │    Coq7-type (PP_0427)  C6/DMQ hydroxylase (EC 1.14.99.60)  ← replaces UbiF
   │  and two methylations:
   │    UbiG (PP_1765)  O-methyltransferase (EC 2.1.1.222 / 2.1.1.64) — acts twice
   │    UbiE (PP_5011)  C-methyltransferase (EC 2.1.1.163/2.1.1.201)
   ▼
Ubiquinone-9 (UQ-9)

Accessory / regulatory (MISSING from candidate metadata, present in proteome):
   UbiB (PP_5013)  atypical kinase / assembly & CoQ distribution
   UbiJ (PP_5012)  SCP2 lipid-binding assembly factor (Ubi metabolon)
   UbiK (PP_5235)  assembly factor (partners UbiJ)
   [ubiE–ubiJ–ubiB are a contiguous cluster: PP_5011–PP_5012–PP_5013]

NOT expected in KT2440 (strict aerobe):
   UbiT / UbiU / UbiV  O2-independent hydroxylation system — ABSENT (0 hits)
   UbiF                flavin C6-hydroxylase — ABSENT genome-wide
   MenA / MenD         menaquinone — ABSENT
```

**Step satisfiability summary table:**

| Expected step | Enzyme family | KT2440 gene | Call |
|---|---|---|---|
| 4-HB from chorismate | UbiC chorismate lyase | PP_5317 (*ubiC*) | **covered** |
| Polyprenylation of 4-HB | UbiA prenyltransferase | PP_5318 (*ubiA*) | **covered** |
| prFMN cofactor supply | UbiX flavin prenyltransferase | PP_0548 (*ubiX*) | **covered** |
| Decarboxylation | UbiD prFMN decarboxylase | PP_5213 (*ubiD*) | **covered** |
| Ring hydroxylation (C5) | UbiI/VisC | PP_5197 (*visC*) | **covered** |
| Ring hydroxylation (C6) | UbiH | PP_5199 (*ubiH*) | **covered** |
| Ring hydroxylation (C6/DMQ) | Coq7-type (replaces UbiF) | PP_0427 (*coq7*) | **covered (lineage substitution)** |
| O-methylation (×2) | UbiG | PP_1765 (*ubiG*) | **covered** |
| C-methylation | UbiE | PP_5011 (*ubiE*) | **covered** |
| Side-chain synthesis | IspB nonaprenyl-PP synthase | PP_0687 | **covered (outside map)** |
| Assembly/regulation | UbiB kinase | PP_5013 (*ubiB*) | **covered — ADD to metadata** |
| Assembly | UbiJ | PP_5012 (*ubiJ*) | **covered — ADD to metadata** |
| Assembly | UbiK | PP_5235 (*ubiK*) | **covered — ADD to metadata** |
| Anaerobic hydroxylation | UbiT/U/V | — | **not_expected_in_target_taxon** |

---

## 4. Candidate Genes and Evidence

All 14 supplied candidates share one over-arching caveat established in **Finding F002**: every UniProt entry carries **proteinExistence = "3: Inferred from homology"**. None is PE=1 (protein-level) or PE=2 (transcript-level). This means the annotations rest on sequence orthology and pathway-database placement, not on KT2440-specific experiments.

### 4.1 High-confidence biosynthetic core (promote all to full review)

**UbiC — PP_5317 (Q88C66), chorismate pyruvate-lyase, EC 4.1.3.40; KO K03181.** Catalyzes the entry reaction, chorismate → 4-HB + pyruvate. KEGG KO and EC are unambiguous. Curation note: UniProt labels it "Probable," reflecting homology-only evidence.

**UbiA — PP_5318 (Q88C65), 4-HB octaprenyltransferase, EC 2.5.1.39; KO K03179.** Prenylates 4-HB with the nonaprenyl tail. Directly adjacent to *ubiC* (PP_5317/PP_5318), a classic proteobacterial arrangement supporting the assignment. High confidence.

**UbiX — PP_0548 (Q88QE6), flavin prenyltransferase, EC 2.5.1.129; KO K03186.** Synthesizes the prenylated-FMN (prFMN) cofactor required by UbiD. Curation caveat: its **primary bucket in the metadata is kegg:ppu00627** (aminobenzoate/other), not ppu00130 — i.e., it is annotated to a different map yet is functionally essential to this pathway. The UbiX–UbiD partnership is one of the best-characterized modules in the field (multiple mechanistic studies; see §8), so transfer to KT2440 is strong.

**UbiD — PP_5213 (Q88CG8), 3-octaprenyl-4-hydroxybenzoate decarboxylase, EC 4.1.1.98; KO K03182.** The prFMN-dependent (de)carboxylase. High confidence. Caveat: the UbiD family is large and functionally diverse (it also includes aromatic-acid decarboxylases such as phenazine-1-carboxylic acid decarboxylase, [PMID: 38176649](https://pubmed.ncbi.nlm.nih.gov/38176649/)); annotation transfer within the family requires the UbiX partner and pathway context, both of which are satisfied here.

**VisC/UbiI — PP_5197 (Q88CI4), FAD/NAD(P)-binding oxidoreductase, EC 1.14.13.240; KO K18800.** The C5 (2-methoxy-6-polyprenylphenol) hydroxylase. "VisC" is the historical name for UbiI. Adjacent to *ubiH* (PP_5197/PP_5199). The UniProt free-text ("Oxidoreductase involved in anaerobic synthesis of ubiquinone") is **misleading** — this is an aerobic hydroxylase; curators should not read "anaerobic" here as evidence for the O2-independent UbiT/U/V system (which is absent).

**UbiH — PP_5199 (Q88CI2), 2-octaprenyl-6-methoxyphenol hydroxylase; KO K03185.** The C6 hydroxylase. High confidence; syntenic with *visC*.

**Coq7-type — PP_0427 (Q88QR1), 3-demethoxyubiquinol 3-hydroxylase / DMQ hydroxylase, EC 1.14.99.60; KO K06134.** This is a **lineage-specific substitution**: KT2440 lacks the flavin monooxygenase UbiF (EC 1.14.13.-; KO K18801 absent genome-wide, Finding F007) and instead uses a **Coq7/COQ7-family di-iron hydroxylase** (the enzyme normally associated with eukaryotic/alphaproteobacterial CoQ synthesis) to accomplish the equivalent C6 hydroxylation. This is a known evolutionary theme: proteobacteria deploy varied enzymes with different regioselectivities to accomplish the three contiguous hydroxylations ([PMID: 27822549](https://pubmed.ncbi.nlm.nih.gov/27822549/)). High curation value — flag as a **non-canonical but real** assignment.

**UbiG — PP_1765 (Q88M10), UQ O-methyltransferase, EC 2.1.1.222 / 2.1.1.64; KO K00568.** Performs **both** O-methylations in the pathway (bifunctional, acts at two steps). High confidence.

**UbiE — PP_5011 (Q88D17), C-methyltransferase, EC 2.1.1.163/2.1.1.201; KO K03183.** The ring C-methyltransferase. High confidence. Caveat: UniProt/HAMAP appends a **generic "menaquinone biosynthesis; menaquinol… step 2/2"** pathway string to UbiE. Because KT2440 has **no menaquinone pathway** (*menA/menD* absent), this menaquinone annotation is an **over-propagated artifact** — UbiE here functions only in UQ biosynthesis. First member of the *ubiE–ubiJ–ubiB* cluster.

### 4.2 Accessory factors present but MISSING from the candidate list (Finding F001)

**UbiB — PP_5013 (A0A140FWS4), "Probable protein kinase UbiB," EC 2.7.-.-; KO K03688; HAMAP MF_00414.** Atypical ABC1/ADCK/UbiB-family kinase required for efficient CoQ biosynthesis and for CoQ distribution across membranes (functionally characterized in *E. coli*, yeast Coq8, human ADCK3/4; [PMID: 34362905](https://pubmed.ncbi.nlm.nih.gov/34362905/), [PMID: 32479562](https://pubmed.ncbi.nlm.nih.gov/32479562/), [PMID: 18319074](https://pubmed.ncbi.nlm.nih.gov/18319074/)). Present in the proteome, contiguous with *ubiJ* and *ubiE*. **Should be added to the module.**

**UbiJ — PP_5012 (Q88D16), UbiJ accessory factor; HAMAP MF_02215.** SCP2 lipid-binding protein that scaffolds the cytosolic Ubi "metabolon" and binds pathway intermediates ([PMID: 36142227](https://pubmed.ncbi.nlm.nih.gov/36142227/)). Directly between *ubiE* and *ubiB*. **Add to the module.** No KEGG KO is assigned (Finding F007), so it is invisible to KO-based reconstruction — a systematic reason it was dropped.

**UbiK — PP_5235 (Q88CE6), UbiK accessory factor; HAMAP MF_02216.** Partners UbiJ in the assembly complex. Present in proteome; no KEGG KO. **Add to the module.**

### 4.3 Map-boundary artifacts — likely NOT part of de novo UQ (Findings F004, F005)

| Gene | ID / accession | Annotation | Why it is an artifact |
|---|---|---|---|
| *hpd* | PP_3433 (Q88HC7) | 4-hydroxyphenylpyruvate dioxygenase, EC 1.13.11.27, KO K00457 | Tyrosine catabolism / homogentisate → tocopherol–plastoquinone branch, **not** UQ from 4-HB |
| PP_1218 | Q88NI9 | acyl-CoA / 4-hydroxybenzoyl-CoA thioesterase, EC 3.1.2.23, KO K01075 | Peripheral hydrolase; not a UQ biosynthetic step |
| PP_1644 | Q88MC9 | WrbA-type NAD(P)H:quinone oxidoreductase, EC 1.6.5.2, KO K03809 | **Uses** quinones (respiration/stress), does not make UQ |
| PP_2789 | Q88J60 | NAD(P)H:quinone oxidoreductase (Qor/MdaB), EC 1.6.5.2, KO K00355 | Quinone-utilizing, not biosynthetic |
| PP_3720 | Q88GK1 | NAD(P)H:quinone oxidoreductase (Qor/MdaB), KO K00355 | Quinone-utilizing, not biosynthetic |

These five inflate the candidate list purely because KEGG ppu00130 is a multi-quinone overview map. They should be excluded from a KT2440-specific de novo UQ module.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

**5.1 The candidate list = raw KEGG ppu00130 membership.** A KEGG REST query (`link/ppu/path:ppu00130`) returns exactly the 14 PP_ IDs supplied (Finding F005). This confirms the metadata was generated by direct map membership, which explains both its omissions (accessory factors *ubiJ/ubiK* have no KO; *ubiB* and *ispB* are not map members) and its inflation (multi-quinone map artifacts).

**5.2 UbiF → Coq7 substitution (Findings F003, F007).** Genome-wide KO checks confirm **no UbiF ortholog** (K18801 absent) and **no UbiI-independent flavin C6-hydroxylase**. The three aerobic hydroxylations are covered by VisC/UbiI, UbiH, and the Coq7-type enzyme. This is consistent with the established evolutionary flexibility of proteobacterial UQ hydroxylases — *"The biosynthesis of UQ requires three hydroxylation reactions on contiguous positions of an aromatic ring"* ([PMID: 27822549](https://pubmed.ncbi.nlm.nih.gov/27822549/)). Curators should record the Coq7 assignment as a **confirmed lineage substitution**, not a gap.

**5.3 Anaerobic UbiT/U/V not expected (Finding F006).** No *ubiT/ubiU/ubiV* genes (0 hits). In denitrifying *P. aeruginosa* PAO1 this O2-independent system is essential for anaerobic UQ-9 synthesis ([PMID: 32409583](https://pubmed.ncbi.nlm.nih.gov/32409583/)); a *P. aeruginosa* genome-scale model (iSD1509) added it because the pathway *"is required for anaerobic growth"* ([PMID: 36765199](https://pubmed.ncbi.nlm.nih.gov/36765199/)). KT2440 is a **strict aerobe lacking a complete denitrification chain**, so this branch should be marked **not_expected_in_target_taxon** rather than a gap. This is a clear case where a generic multi-organism module boundary would be **wrong** for KT2440.

**5.4 Over-propagated annotations to flag.**
- **UbiE menaquinone pathway string** — spurious in KT2440 (no *men* genes).
- **VisC "anaerobic" free-text** — misleading; it is an aerobic hydroxylase.
- **Broad EC/GO on the quinone oxidoreductases** (EC 1.6.5.2, KO K00355/K03809) — these map to respiration/detox, not biosynthesis.

**5.5 Homology-only evidence (Finding F002).** The deepest gap is evidential, not genomic: **all** calls are PE=3. No KT2440 protein-level, transcript-level, or mutant-phenotype data anchor any step in the strain itself.

---

## 6. Module and GO-Curation Recommendations

**Step disposition for the module:**

| Module element | Recommended status |
|---|---|
| UbiC, UbiA, UbiX, UbiD, VisC/UbiI, UbiH, UbiG, UbiE | **covered** (homology-strong) |
| Coq7-type C6 hydroxylation (PP_0427) | **covered** — annotate as lineage substitution for UbiF |
| Nonaprenyl-PP side chain (IspB PP_0687) | **covered** — note it lies outside the KEGG map |
| UbiB (PP_5013), UbiJ (PP_5012), UbiK (PP_5235) | **covered — module_needs_revision to ADD these** |
| *hpd*, PP_1218, PP_1644, PP_2789, PP_3720 | **remove** — map-boundary artifacts, not de novo UQ |
| UbiT/U/V anaerobic hydroxylation | **not_expected_in_target_taxon** |
| UbiF flavin C6-hydroxylase | **not_expected** (absent; role filled by Coq7) |

**Module boundary guidance.** The generic module is broadly correct in topology but must be **species-tailored** for KT2440: (i) exclude menaquinone/tocopherol/plastoquinone members inherited from the lumped KEGG map; (ii) explicitly encode the **Coq7-for-UbiF** substitution as an accepted alternative enzyme; (iii) add the accessory-factor sub-step (UbiB/UbiJ/UbiK); and (iv) mark the anaerobic branch as not expected.

**GO-term / annotation requests.** Because **UbiJ and UbiK lack KEGG KOs**, KO-driven module reconstruction will systematically miss them — a GO/annotation request to ensure these HAMAP-annotated accessory factors (MF_02215/MF_02216) are captured in the module ontology would prevent recurrent under-calling across proteobacteria. No new GO terms appear strictly necessary for the core enzymatic steps, which are well covered by existing EC/GO mappings.

---

## 7. Genes to Promote to Full `fetch-gene` Review

Prioritized for individual review because they are either lineage-specific substitutions, missing from metadata, or carry misleading annotations:

1. **PP_0427 (Coq7-type)** — confirm it, not a UbiF ortholog, performs the C6 hydroxylation; highest novelty/curation value.
2. **PP_5013 (UbiB)**, **PP_5012 (UbiJ)**, **PP_5235 (UbiK)** — add to module; verify identity and synteny (*ubiE–ubiJ–ubiB* cluster).
3. **PP_5197 (VisC/UbiI)** — correct the misleading "anaerobic" free-text; confirm C5-hydroxylase role.
4. **PP_5011 (UbiE)** — strip the spurious menaquinone pathway annotation.
5. **PP_0548 (UbiX)** — reconcile its primary bucket (ppu00627) with its essential UQ role.
6. **PP_5213 (UbiD)** — verify family assignment given the functionally diverse UbiD superfamily.
7. **PP_0687 (IspB)** — confirm as the nonaprenyl-PP source feeding UbiA (outside the KEGG map).

---

## 8. Evidence Base and Key References

**Direct KT2440 evidence:** essentially none at the pathway level — this is the central limitation. The most actionable strain-specific resource is the **RB-TnSeq fitness library** disrupting ~4,778 non-essential genes of KT2440 ([PMID: 33964456](https://pubmed.ncbi.nlm.nih.gov/33964456/)), part of the Deutschbauer/Arkin Fitness Browser (Finding F008). Genes *absent* from such non-essential libraries are inferred essential; core aerobic-respiration UQ genes are expected to be essential or strongly fitness-defective aerobically. A related RB-TnSeq study of *P. putida* carbon metabolism ([PMID: 32826213](https://pubmed.ncbi.nlm.nih.gov/32826213/)) demonstrates the approach is mature for this strain.

**Mechanistic transfer from related systems (strong):**

| Topic | PMID | How it supports the review |
|---|---|---|
| Three contiguous UQ hydroxylations; variable enzymes | [27822549](https://pubmed.ncbi.nlm.nih.gov/27822549/) | Underpins the three-hydroxylation requirement and acceptance of Coq7-type enzymes at these positions |
| O2-independent UbiT/U/V pathway | [32409583](https://pubmed.ncbi.nlm.nih.gov/32409583/) | Defines the anaerobic branch that KT2440 lacks |
| *P. aeruginosa* genome-scale model iSD1509 | [36765199](https://pubmed.ncbi.nlm.nih.gov/36765199/) | Anaerobic UQ-9 pathway "required for anaerobic growth" — not-expected in aerobic KT2440 |
| UbiX–UbiD / prFMN biochemistry | [32951834](https://pubmed.ncbi.nlm.nih.gov/32951834/), [31142738](https://pubmed.ncbi.nlm.nih.gov/31142738/), [28754323](https://pubmed.ncbi.nlm.nih.gov/28754323/), [38176649](https://pubmed.ncbi.nlm.nih.gov/38176649/) | Cofactor chemistry and UbiD family diversity; justify pathway-context requirement for UbiD annotation |
| UbiJ–UbiK assembly factors | [36142227](https://pubmed.ncbi.nlm.nih.gov/36142227/) | Supports adding accessory factors to the module |
| ABC1/ADCK/UbiB kinase family | [34362905](https://pubmed.ncbi.nlm.nih.gov/34362905/), [32479562](https://pubmed.ncbi.nlm.nih.gov/32479562/), [18319074](https://pubmed.ncbi.nlm.nih.gov/18319074/), [24267661](https://pubmed.ncbi.nlm.nih.gov/24267661/) | Supports adding UbiB (PP_5013) as an accessory/regulatory factor |

**Verified supporting quotes.**
- *"The biosynthesis of UQ requires three hydroxylation reactions on contiguous positions of an aromatic ring."* ([PMID: 27822549](https://pubmed.ncbi.nlm.nih.gov/27822549/))
- *"we newly added a recently discovered pathway for ubiquinone-9 biosynthesis which is required for anaerobic growth."* ([PMID: 36765199](https://pubmed.ncbi.nlm.nih.gov/36765199/))

**Database evidence (direct for KT2440 genome content):** UniProt proteome UP000000556 gene-name and proteinExistence queries (Findings F001, F002); KEGG REST map membership and KO/EC assignments (Findings F005, F007). These are authoritative for gene presence/absence and annotation provenance but are themselves homology-based for function.

---

## 9. Limitations and Knowledge Gaps

1. **No direct target-strain functional data.** Every functional call is PE=3 homology inference. Confidence in the *reconstruction* is high; confidence in *strain-specific biochemistry* is homology-grade.
2. **Coq7 substitution is inferred, not demonstrated in KT2440.** The absence of UbiF plus presence of a Coq7 ortholog with the matching EC strongly implies substitution, but the actual C6-hydroxylation activity in KT2440 has not been shown experimentally.
3. **Accessory-factor essentiality unknown in KT2440.** UbiB/UbiJ/UbiK roles are transferred from *E. coli*/yeast/*P. aeruginosa*; their quantitative contribution in KT2440 is untested.
4. **Side-chain length assumed UQ-9.** Consistent with pseudomonads and IspB annotation, but not directly measured here.
5. **KEGG map lumping** forces manual boundary decisions; the five artifact genes and the menaquinone/tocopherol overlap require curator judgment rather than automated exclusion.

---

## 10. Proposed Follow-up Experiments / Actions

**Curation actions (immediate):**
- Revise the module to **add** PP_5013 (UbiB), PP_5012 (UbiJ), PP_5235 (UbiK) and **remove** the five artifacts (PP_3433, PP_1218, PP_1644, PP_2789, PP_3720).
- Record the **Coq7-for-UbiF** substitution and mark **UbiT/U/V** as not_expected_in_target_taxon.
- Correct misleading free-text on VisC ("anaerobic") and the spurious menaquinone pathway string on UbiE.
- File an annotation/GO request so KO-less accessory factors (UbiJ/UbiK) are captured in future reconstructions.

**Experimental / data-mining actions (to close the PE=3 gap):**
- **Mine the KT2440 RB-TnSeq Fitness Browser** ([PMID: 33964456](https://pubmed.ncbi.nlm.nih.gov/33964456/)) for per-gene fitness/essentiality of *ubiA/C/D/X/G/E*, *visC*, *ubiH*, *coq7*, *ubiB/J/K* under aerobic growth — the single fastest path to strain-specific evidence.
- **Targeted deletion + UQ-9 quantification** (LC-MS) for PP_0427 (Coq7) to confirm the UbiF-substitution hypothesis; a Δ*coq7* strain should accumulate demethoxy-UQ.
- **Complementation of an *E. coli ubiF* mutant** with KT2440 *coq7* to demonstrate the C6-hydroxylation activity heterologously.
- **Verify UQ-9 chain length** by mass spectrometry and confirm IspB (PP_0687) as the nonaprenyl-PP source.

---

*Report generated from a 5-iteration autonomous review integrating UniProt (UP000000556), KEGG (ppu00130) REST queries, and 23 literature records. All gene presence/absence claims derive from direct database queries of the KT2440 proteome; all functional roles are homology-inferred unless otherwise stated.*


## Artifacts

- [OpenScientist final report](PSEPK__ubiquinone_biosynthesis__ppu00130-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__ubiquinone_biosynthesis__ppu00130-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:38176649
2. PMID:27822549
3. PMID:34362905
4. PMID:32479562
5. PMID:18319074
6. PMID:36142227
7. PMID:32409583
8. PMID:36765199
9. PMID:33964456
10. PMID:32826213