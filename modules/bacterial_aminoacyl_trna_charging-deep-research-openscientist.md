---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T12:06:21.038705'
end_time: '2026-09-01T12:28:29.331681'
duration_seconds: 1328.29
template_file: templates/module_research.md.j2
template_variables:
  module_title: Bacterial aminoacyl-tRNA charging
  module_summary: Bacterial production of aminoacyl-tRNAs for translation through
    direct aminoacyl-tRNA synthetase reactions. Asparaginyl-tRNA formation is modeled
    as alternative direct AsnRS or indirect non-discriminating AspRS-GatABC routes,
    and glutaminyl-tRNA formation as alternative direct GlnRS or indirect GluRS-GatABC
    routes. The reusable boundary ends when a correctly charged canonical aminoacyl-tRNA
    is formed.
  module_outline: "- bacterial aminoacyl-tRNA charging\n  - 1. direct aminoacyl-tRNA\
    \ synthetase routes\n  - Direct aminoacyl-tRNA synthetase charging\n    - 1. class\
    \ I aminoacyl-tRNA synthetases\n    - Class I direct tRNA charging\n      - Glutamate-tRNA\
    \ ligase family (molecular player: bacterial glutamate-tRNA ligases; activity\
    \ or role: glutamate-tRNA ligase activity)\n      - Arginine-tRNA ligase family\
    \ (molecular player: bacterial arginine-tRNA ligases; activity or role: arginine-tRNA\
    \ ligase activity)\n      - Cysteine-tRNA ligase family (molecular player: bacterial\
    \ cysteine-tRNA ligases; activity or role: cysteine-tRNA ligase activity)\n  \
    \    - Isoleucine-tRNA ligase family (molecular player: bacterial isoleucine-tRNA\
    \ ligases; activity or role: isoleucine-tRNA ligase activity)\n      - Leucine-tRNA\
    \ ligase family (molecular player: bacterial leucine-tRNA ligases; activity or\
    \ role: leucine-tRNA ligase activity)\n      - Methionine-tRNA ligase family (molecular\
    \ player: bacterial methionine-tRNA ligases; activity or role: methionine-tRNA\
    \ ligase activity)\n      - Tryptophan-tRNA ligase family (molecular player: bacterial\
    \ tryptophan-tRNA ligases; activity or role: tryptophan-tRNA ligase activity)\n\
    \      - Tyrosine-tRNA ligase family (molecular player: bacterial tyrosine-tRNA\
    \ ligases; activity or role: tyrosine-tRNA ligase activity)\n      - Valine-tRNA\
    \ ligase family (molecular player: bacterial valine-tRNA ligases; activity or\
    \ role: valine-tRNA ligase activity)\n    - 2. class II aminoacyl-tRNA synthetases\n\
    \    - Class II direct tRNA charging\n      - Serine-tRNA ligase family (molecular\
    \ player: bacterial serine-tRNA ligases; activity or role: serine-tRNA ligase\
    \ activity)\n      - Alanine-tRNA ligase family (molecular player: bacterial alanine-tRNA\
    \ ligases; activity or role: alanine-tRNA ligase activity)\n      - Aspartate-tRNA\
    \ ligase family (molecular player: bacterial non-discriminating aspartate-tRNA\
    \ ligases; activity or role: aspartate-tRNA ligase activity)\n      - Heterotetrameric\
    \ glycine-tRNA ligase (molecular player: bacterial alpha2-beta2 glycyl-tRNA synthetase;\
    \ activity or role: glycine-tRNA ligase activity)\n      - Histidine-tRNA ligase\
    \ family (molecular player: bacterial histidine-tRNA ligases; activity or role:\
    \ histidine-tRNA ligase activity)\n      - Lysine-tRNA ligase family (molecular\
    \ player: bacterial class II lysine-tRNA ligases; activity or role: lysine-tRNA\
    \ ligase activity)\n      - Heterotetrameric phenylalanine-tRNA ligase (molecular\
    \ player: bacterial alpha2-beta2 phenylalanyl-tRNA synthetase; activity or role:\
    \ phenylalanine-tRNA ligase activity)\n      - Proline-tRNA ligase family (molecular\
    \ player: bacterial proline-tRNA ligases; activity or role: proline-tRNA ligase\
    \ activity)\n      - Threonine-tRNA ligase family (molecular player: bacterial\
    \ threonine-tRNA ligases; activity or role: threonine-tRNA ligase activity)\n\
    \  - 2. asparaginyl-tRNA route choice\n  - Asparaginyl-tRNA formation\n    - Alternative\
    \ versions by charging route: Direct and indirect asparaginyl-tRNA routes\n  \
    \    - Direct AsnRS route\n        - Asparagine-tRNA ligase family (molecular\
    \ player: bacterial asparagine-tRNA ligases; activity or role: asparagine-tRNA\
    \ ligase activity)\n      - Indirect AspRS-GatABC route\n        - 1. misacylated\
    \ Asp-tRNA(Asn) formation\n        - Asp-tRNA(Asn) precursor formation\n     \
    \     - Non-discriminating AspRS family (molecular player: non-discriminating\
    \ bacterial aspartate-tRNA ligases; activity or role: aspartate-tRNA ligase activity)\n\
    \        - 2. GatABC-dependent transamidation\n        - Asp-tRNA(Asn) to Asn-tRNA(Asn)\n\
    \          - GatABC aspartyl-tRNA(Asn) amidotransferase (molecular player: bacterial\
    \ GatABC amidotransferase; activity or role: asparaginyl-tRNA synthase (glutamine-hydrolyzing)\
    \ activity)\n  - 3. glutaminyl-tRNA route choice\n  - Glutaminyl-tRNA formation\n\
    \    - Alternative versions by charging route: Direct and indirect glutaminyl-tRNA\
    \ routes\n      - Direct GlnRS route\n        - Glutamine-tRNA ligase family (molecular\
    \ player: bacterial glutamine-tRNA ligases; activity or role: glutamine-tRNA ligase\
    \ activity)\n      - Indirect GluRS-GatABC route\n        - 1. misacylated Glu-tRNA(Gln)\
    \ formation\n        - Glu-tRNA(Gln) precursor formation\n          - Non-discriminating\
    \ GluRS family (molecular player: non-discriminating bacterial glutamate-tRNA\
    \ ligases; activity or role: glutamate-tRNA ligase activity)\n        - 2. GatABC-dependent\
    \ transamidation\n        - Glu-tRNA(Gln) to Gln-tRNA(Gln)\n          - GatABC\
    \ glutamyl-tRNA(Gln) amidotransferase (molecular player: bacterial GatABC amidotransferase;\
    \ activity or role: glutaminyl-tRNA synthase (glutamine-hydrolyzing) activity)"
  module_connections: '- Non-discriminating AspRS family feeds into GatABC aspartyl-tRNA(Asn)
    amidotransferase: Asp-tRNA(Asn) is the immediate GatABC substrate.

    - Non-discriminating GluRS family feeds into GatABC glutamyl-tRNA(Gln) amidotransferase:
    Glu-tRNA(Gln) is the immediate GatABC substrate.'
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
citation_count: 37
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: bacterial_aminoacyl_trna_charging-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: bacterial_aminoacyl_trna_charging-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Bacterial aminoacyl-tRNA charging

## Working Scope

Bacterial production of aminoacyl-tRNAs for translation through direct aminoacyl-tRNA synthetase reactions. Asparaginyl-tRNA formation is modeled as alternative direct AsnRS or indirect non-discriminating AspRS-GatABC routes, and glutaminyl-tRNA formation as alternative direct GlnRS or indirect GluRS-GatABC routes. The reusable boundary ends when a correctly charged canonical aminoacyl-tRNA is formed.

## Provisional Biological Outline

- bacterial aminoacyl-tRNA charging
  - 1. direct aminoacyl-tRNA synthetase routes
  - Direct aminoacyl-tRNA synthetase charging
    - 1. class I aminoacyl-tRNA synthetases
    - Class I direct tRNA charging
      - Glutamate-tRNA ligase family (molecular player: bacterial glutamate-tRNA ligases; activity or role: glutamate-tRNA ligase activity)
      - Arginine-tRNA ligase family (molecular player: bacterial arginine-tRNA ligases; activity or role: arginine-tRNA ligase activity)
      - Cysteine-tRNA ligase family (molecular player: bacterial cysteine-tRNA ligases; activity or role: cysteine-tRNA ligase activity)
      - Isoleucine-tRNA ligase family (molecular player: bacterial isoleucine-tRNA ligases; activity or role: isoleucine-tRNA ligase activity)
      - Leucine-tRNA ligase family (molecular player: bacterial leucine-tRNA ligases; activity or role: leucine-tRNA ligase activity)
      - Methionine-tRNA ligase family (molecular player: bacterial methionine-tRNA ligases; activity or role: methionine-tRNA ligase activity)
      - Tryptophan-tRNA ligase family (molecular player: bacterial tryptophan-tRNA ligases; activity or role: tryptophan-tRNA ligase activity)
      - Tyrosine-tRNA ligase family (molecular player: bacterial tyrosine-tRNA ligases; activity or role: tyrosine-tRNA ligase activity)
      - Valine-tRNA ligase family (molecular player: bacterial valine-tRNA ligases; activity or role: valine-tRNA ligase activity)
    - 2. class II aminoacyl-tRNA synthetases
    - Class II direct tRNA charging
      - Serine-tRNA ligase family (molecular player: bacterial serine-tRNA ligases; activity or role: serine-tRNA ligase activity)
      - Alanine-tRNA ligase family (molecular player: bacterial alanine-tRNA ligases; activity or role: alanine-tRNA ligase activity)
      - Aspartate-tRNA ligase family (molecular player: bacterial non-discriminating aspartate-tRNA ligases; activity or role: aspartate-tRNA ligase activity)
      - Heterotetrameric glycine-tRNA ligase (molecular player: bacterial alpha2-beta2 glycyl-tRNA synthetase; activity or role: glycine-tRNA ligase activity)
      - Histidine-tRNA ligase family (molecular player: bacterial histidine-tRNA ligases; activity or role: histidine-tRNA ligase activity)
      - Lysine-tRNA ligase family (molecular player: bacterial class II lysine-tRNA ligases; activity or role: lysine-tRNA ligase activity)
      - Heterotetrameric phenylalanine-tRNA ligase (molecular player: bacterial alpha2-beta2 phenylalanyl-tRNA synthetase; activity or role: phenylalanine-tRNA ligase activity)
      - Proline-tRNA ligase family (molecular player: bacterial proline-tRNA ligases; activity or role: proline-tRNA ligase activity)
      - Threonine-tRNA ligase family (molecular player: bacterial threonine-tRNA ligases; activity or role: threonine-tRNA ligase activity)
  - 2. asparaginyl-tRNA route choice
  - Asparaginyl-tRNA formation
    - Alternative versions by charging route: Direct and indirect asparaginyl-tRNA routes
      - Direct AsnRS route
        - Asparagine-tRNA ligase family (molecular player: bacterial asparagine-tRNA ligases; activity or role: asparagine-tRNA ligase activity)
      - Indirect AspRS-GatABC route
        - 1. misacylated Asp-tRNA(Asn) formation
        - Asp-tRNA(Asn) precursor formation
          - Non-discriminating AspRS family (molecular player: non-discriminating bacterial aspartate-tRNA ligases; activity or role: aspartate-tRNA ligase activity)
        - 2. GatABC-dependent transamidation
        - Asp-tRNA(Asn) to Asn-tRNA(Asn)
          - GatABC aspartyl-tRNA(Asn) amidotransferase (molecular player: bacterial GatABC amidotransferase; activity or role: asparaginyl-tRNA synthase (glutamine-hydrolyzing) activity)
  - 3. glutaminyl-tRNA route choice
  - Glutaminyl-tRNA formation
    - Alternative versions by charging route: Direct and indirect glutaminyl-tRNA routes
      - Direct GlnRS route
        - Glutamine-tRNA ligase family (molecular player: bacterial glutamine-tRNA ligases; activity or role: glutamine-tRNA ligase activity)
      - Indirect GluRS-GatABC route
        - 1. misacylated Glu-tRNA(Gln) formation
        - Glu-tRNA(Gln) precursor formation
          - Non-discriminating GluRS family (molecular player: non-discriminating bacterial glutamate-tRNA ligases; activity or role: glutamate-tRNA ligase activity)
        - 2. GatABC-dependent transamidation
        - Glu-tRNA(Gln) to Gln-tRNA(Gln)
          - GatABC glutamyl-tRNA(Gln) amidotransferase (molecular player: bacterial GatABC amidotransferase; activity or role: glutaminyl-tRNA synthase (glutamine-hydrolyzing) activity)

## Known Relationships Among Steps

- Non-discriminating AspRS family feeds into GatABC aspartyl-tRNA(Asn) amidotransferase: Asp-tRNA(Asn) is the immediate GatABC substrate.
- Non-discriminating GluRS family feeds into GatABC glutamyl-tRNA(Gln) amidotransferase: Glu-tRNA(Gln) is the immediate GatABC substrate.

## Assignment

Write a rigorous, review-style synthesis suitable for a molecular biology
audience. Treat the topic as a biological system whose boundaries, core
mechanisms, variants, and unresolved points should be made clear to readers who
know the field but are not specialists in this specific process.

The review should be explanatory rather than encyclopedic. Anchor broad claims
in primary literature or authoritative reviews, but keep the focus on how the
system works and how its parts fit together.

## Questions To Address

1. **Scope and boundaries**
   - What exactly is included in this biological system?
   - Which neighboring pathways, organelle processes, complexes, or regulatory
     events are often confused with it but should be treated separately?
   - Are there competing definitions in the literature?

2. **Core mechanism**
   - What is the best current model for the sequence of events?
   - Which steps are obligatory, which are conditional, and which are accessory?
   - What molecular assemblies, enzymes, receptors, adaptors, transporters, or
     structural units carry out each major step?

3. **Variation**
   - How does the system vary across major evolutionary lineages?
   - Are there well-supported differences between cell types, tissues,
     developmental stages, physiological states, or compartments?
   - Where are there alternative routes that achieve a similar outcome by
     different molecular means?

4. **Conservation and origin**
   - What is the deepest plausible evolutionary origin of the system?
   - Which parts appear ancient and conserved, and which appear to be later
     elaborations, replacements, or lineage-specific losses?
   - When a protein family has expanded, which family members are the best
     representatives for understanding the ancestral role?

5. **Physical and biological constraints**
   - What steps must occur in a particular order?
   - Which events are mutually exclusive, compartment-specific, cell-type
     specific, substrate-specific, or stage-specific?
   - What evidence rules out otherwise plausible paths through the system?

6. **Evidence and controversy**
   - Which mechanistic claims are strongly supported by experiments?
   - Where does the literature disagree, rely on indirect evidence, or mix data
     from organisms that may not be comparable?
   - What are the most important open questions?

## Output Format

Use the style and structure of a concise review article:

1. Executive summary
2. Definition and biological boundaries
3. Mechanistic overview
4. Major molecular players and active assemblies
5. Evolutionary and cell-biological variation
6. Constraints, dependencies, and failure modes
7. Controversies and open questions
8. Key references

Include citations for major claims, preferably PMIDs or DOIs. Be explicit about
uncertainty and avoid overgeneralizing from one organism, cell type, or assay
system to all biology.

## Output

# Bacterial Aminoacyl-tRNA Charging: A Mechanistic and Evolutionary Review

*A commissioned review-style synthesis on the production of correctly charged canonical aminoacyl-tRNAs in bacteria, covering direct aminoacyl-tRNA synthetase routes and the indirect transamidation routes to the amide aminoacyl-tRNAs.*

---

## 1. Executive Summary

Bacterial aminoacyl-tRNA (aa-tRNA) charging is the set of reactions that attach each of the 20 canonical amino acids to its cognate tRNA, producing the substrates that elongation factor Tu (EF-Tu) delivers to the ribosome. Two facts organize the entire system. First, the enzymes that do the work — the aminoacyl-tRNA synthetases (aaRS) — are not one family but **two structurally unrelated superfamilies** that arose independently and yet converged on the same chemistry: ATP-dependent activation of an amino acid to an aminoacyl-adenylate, followed by transfer to the 3′-terminal adenosine (A76) of the tRNA. Class I enzymes are built on a Rossmann fold, carry the HIGH and KMSKS motifs, and acylate the 2′-OH of A76; class II enzymes are built on a distinctive antiparallel β-sheet and acylate the 3′-OH [PMID: 2203971](https://pubmed.ncbi.nlm.nih.gov/2203971/), [PMID: 7783225](https://pubmed.ncbi.nlm.nih.gov/7783225/).

Second, and central to the scope of this review, **most bacteria do not possess a complete set of 20 synthetases.** The two amide aminoacyl-tRNAs — Gln-tRNA(Gln) and Asn-tRNA(Asn) — are frequently made not by a direct glutaminyl- or asparaginyl-tRNA synthetase (GlnRS, AsnRS) but by a two-step *indirect* route: a **non-discriminating** aspartyl- or glutamyl-tRNA synthetase (ND-AspRS, ND-GluRS) first mischarges the tRNA with the acidic precursor (Asp or Glu), and the tRNA-dependent amidotransferase **GatCAB** then transamidates the misacylated intermediate to the correct amide, using glutamine, asparagine, or free ammonia as the nitrogen donor and ATP for activation [PMID: 11585842](https://pubmed.ncbi.nlm.nih.gov/11585842/). This indirect route is not a curiosity: it is the **ancestral, pre-LUCA solution** for adding glutamine and asparagine to the genetic code, whereas the direct GlnRS enzyme is a comparatively late, eukaryote-derived innovation that spread to some bacteria by horizontal gene transfer (HGT) [PMID: 38391119](https://pubmed.ncbi.nlm.nih.gov/38391119/), [PMID: 8078941](https://pubmed.ncbi.nlm.nih.gov/8078941/), [PMID: 10486006](https://pubmed.ncbi.nlm.nih.gov/10486006/).

The reusable boundary of this system opens with a free amino acid, ATP, and an uncharged tRNA, and closes when a **correctly charged canonical aa-tRNA** exists — Asp-tRNA(Asn) and Glu-tRNA(Gln) are internal intermediates, not endpoints. Fidelity is enforced at three levels: the operational RNA code that lets a synthetase pick the right tRNA; pre- and post-transfer **editing** (the class I "double-sieve") that destroys near-cognate errors; and, for the indirect route, mechanisms that prevent the misacylated intermediate from leaking to the ribosome — in bacteria, physical **channeling** within a transamidosome, reinforced by kinetic proofreading. This review lays out the boundaries, the mechanism, the molecular players, the evolutionary and lineage-specific variation, the ordering constraints, and the genuine controversies — including the important finding that channeling is *one* fidelity solution, not a universal law.

---

## 2. Definition and Biological Boundaries

### What is included

The system comprises every reaction that yields a correctly charged canonical aa-tRNA in bacteria:

- **Direct charging** of 18 (or up to 20) amino acids by their cognate aaRS: the class I set (GluRS, ArgRS, CysRS, IleRS, LeuRS, MetRS, TrpRS, TyrRS, ValRS — plus GlnRS where present) and the class II set (SerRS, AlaRS, AspRS, GlyRS, HisRS, LysRS, PheRS, ProRS, ThrRS — plus AsnRS where present).
- **Indirect asparaginyl-tRNA formation**: ND-AspRS makes Asp-tRNA(Asn); GatCAB transamidates it to Asn-tRNA(Asn).
- **Indirect glutaminyl-tRNA formation**: ND-GluRS makes Glu-tRNA(Gln); GatCAB transamidates it to Gln-tRNA(Gln).

For asparagine and glutamine, the direct and indirect routes are genuine **alternative versions** that achieve the same endpoint by different molecular means; individual bacteria use one or the other (occasionally both), as detailed in Section 5.

### What is adjacent but out of scope

Several processes share the "misacylate-then-convert" logic or the aa-tRNA product but fall **outside** the boundary of *canonical bacterial charging*:

- **Selenocysteine (Sec) synthesis.** Sec is the 21st amino acid. SerRS charges tRNA(Sec) with serine, and the bacterial selenocysteine synthase **SelA** — a homodecameric, pyridoxal-5′-phosphate (PLP) enzyme — converts Ser-tRNA(Sec) to Sec-tRNA(Sec) [PMID: 18267971](https://pubmed.ncbi.nlm.nih.gov/18267971/), [PMID: 23559248](https://pubmed.ncbi.nlm.nih.gov/23559248/). The product is non-canonical, so the pathway is adjacent, not included.
- **Archaeal indirect cysteine synthesis.** Some methanogenic archaea lacking CysRS make Cys-tRNA(Cys) via SepRS (O-phosphoseryl-tRNA synthetase) and SepCysS on a transsulfursome scaffold [PMID: 25002468](https://pubmed.ncbi.nlm.nih.gov/25002468/). This is an archaeal, not bacterial, solution.
- **Archaeal GatDE.** Archaea use a second, Gln-specific amidotransferase, the heterodimeric GatDE, alongside an Asn-specific GatCAB; bacteria possess only GatCAB, which handles both amides [PMID: 18291416](https://pubmed.ncbi.nlm.nih.gov/18291416/).
- **Organellar charging** (mitochondrial/plastid/apicoplast) frequently reuses bacterial-type indirect machinery but occurs in a compartment with its own tRNA identity elements and is conventionally treated separately.
- **Downstream events** — EF-Tu binding, ribosomal decoding, and post-translational modification — are not part of charging, though EF-Tu selectivity is mechanistically entangled with fidelity (Section 6).

### Competing definitions

The literature does not fully agree on where "aminoacyl-tRNA synthesis" ends. A narrow view counts only the direct aaRS reactions; a broader, genome-informed view — now the mainstream — explicitly includes the indirect transamidation routes as legitimate aa-tRNA synthesis, because in most bacteria they are the *only* way the amide aa-tRNAs are made [PMID: 11732603](https://pubmed.ncbi.nlm.nih.gov/11732603/), [PMID: 11375928](https://pubmed.ncbi.nlm.nih.gov/11375928/). This review adopts the broad definition, consistent with the working scope.

---

## 3. Mechanistic Overview

### 3.1 The universal two-step chemistry

Every aaRS, class I or class II, catalyzes the same two-step reaction:

```
Step 1 (activation):   amino acid + ATP  ->  aminoacyl-AMP + PPi
Step 2 (transfer):     aminoacyl-AMP + tRNA  ->  aminoacyl-tRNA + AMP
```

The transfer step differs in *regiochemistry*: class I enzymes esterify the **2′-OH** of A76, class II the **3′-OH** [PMID: 2203971](https://pubmed.ncbi.nlm.nih.gov/2203971/). (Because the 2′- and 3′-esters interconvert rapidly, the ribosome ultimately uses the 3′-form for all.) This 2′/3′ split is the single most reliable functional signature distinguishing the two classes and correlates tightly with their independent structural origins [PMID: 7783225](https://pubmed.ncbi.nlm.nih.gov/7783225/).

### 3.2 Choosing the right tRNA: the operational RNA code

A synthetase must recognize its cognate tRNA among ~40 species. Recognition rests on **identity elements** — chiefly the discriminator base (N73), the anticodon, and specific acceptor-stem base pairs. The paradigmatic minimalist case is alanine: AlaRS recognizes essentially the single **G3:U70 wobble pair** in the acceptor stem, and a G3→A change abolishes recognition [PMID: 24049072](https://pubmed.ncbi.nlm.nih.gov/24049072/). Acceptor-stem recognition — read through the minor groove by class I enzymes and the major groove by class II — is argued to be the **ancient operational code** that predated anticodon reading [PMID: 31781936](https://pubmed.ncbi.nlm.nih.gov/31781936/).

### 3.3 Correcting errors: editing and the double sieve

Amino acids that are near-isosteric (e.g., valine vs. isoleucine) cannot be discriminated by binding energy alone. Several class I enzymes solve this with a **double-sieve** editing mechanism, defined structurally by the isoleucyl-tRNA synthetase (IleRS): the aminoacylation active site (the Rossmann-fold "coarse" first sieve) activates both Ile and the smaller Val, while a separate β-barrel CP1 editing domain (the "fine" second sieve) hydrolyzes only the mischarged Val product [PMID: 9554847](https://pubmed.ncbi.nlm.nih.gov/9554847/). The two sieves are spatially distinct domains, and the mischarged product is selectively destroyed rather than released.

### 3.4 The indirect amide routes: obligate ordering

For Asn and Gln, when the direct synthetase is absent, the endpoint is reached in a strictly ordered two-step pathway:

```
Asparaginyl-tRNA (indirect):
  tRNA(Asn) + Asp + ATP --ND-AspRS--> Asp-tRNA(Asn)     [misacylation]
  Asp-tRNA(Asn) + Gln/Asn/NH3 + ATP --GatCAB--> Asn-tRNA(Asn)   [transamidation]

Glutaminyl-tRNA (indirect):
  tRNA(Gln) + Glu + ATP --ND-GluRS--> Glu-tRNA(Gln)     [misacylation]
  Glu-tRNA(Gln) + Gln/Asn/NH3 + ATP --GatCAB--> Gln-tRNA(Gln)   [transamidation]
```

The misacylated species (Asp-tRNA(Asn), Glu-tRNA(Gln)) are the **immediate GatCAB substrates** and obligate intermediates — misacylation *must* precede transamidation. GatCAB works by first phosphorylating the α-carboxylate of the tRNA-bound Asp/Glu (kinase activity in the GatB subunit), then amidating the activated intermediate with ammonia generated by hydrolysis of glutamine in the GatA glutaminase site; a molecular ammonia channel connects the two active sites [PMID: 19520089](https://pubmed.ncbi.nlm.nih.gov/19520089/), [PMID: 11585842](https://pubmed.ncbi.nlm.nih.gov/11585842/).

### 3.5 Which steps are obligatory, conditional, accessory

| Step | Status | Notes |
|---|---|---|
| Amino-acid activation to aa-AMP | **Obligatory** | Universal first half-reaction for all 20 |
| Transfer to A76 (2′ class I / 3′ class II) | **Obligatory** | Produces the aa-tRNA |
| Operational-code tRNA selection | **Obligatory** | Sets specificity |
| Editing / double-sieve hydrolysis | **Conditional** | Only for error-prone pairs (Ile/Val, Ala/Ser/Gly, Thr, etc.) |
| ND-synthetase misacylation | **Conditional** | Only when direct GlnRS/AsnRS absent |
| GatCAB transamidation | **Conditional but essential where used** | Obligate second step of the indirect route |
| Transamidosome channeling | **Accessory to fidelity** | One of several ways to protect the intermediate |

---

## 4. Major Molecular Players and Active Assemblies

### 4.1 The two synthetase classes

**Class I (Rossmann fold, HIGH + KMSKS motifs, 2′-OH acylation):** GlnRS, TyrRS, MetRS, GluRS, ArgRS, ValRS, IleRS, LeuRS, TrpRS. Sequence analysis originally partitioned exactly these nine as class I by their two short consensus motifs [PMID: 2203971](https://pubmed.ncbi.nlm.nih.gov/2203971/). The class I fold is the classic nucleotide-binding Rossmann fold shared with dehydrogenases and kinases [PMID: 7783225](https://pubmed.ncbi.nlm.nih.gov/7783225/).

**Class II (antiparallel six-stranded β-sheet, three mutually exclusive motifs, 3′-OH acylation):** SerRS, ThrRS, ProRS, AspRS, AsnRS, LysRS (class II form), HisRS, PheRS-β, AlaRS, GlyRS. The class II fold is not found elsewhere and is built around a six-stranded antiparallel β-sheet [PMID: 7783225](https://pubmed.ncbi.nlm.nih.gov/7783225/).

### 4.2 Quaternary structure is not conserved

Oligomeric state varies widely and is often tied to function. Bacterial **PheRS** is an (αβ)₂ class-IIc heterotetramer with 11 structural domains per αβ protomer [PMID: 21082706](https://pubmed.ncbi.nlm.nih.gov/21082706/); bacterial **GlyRS** is an α₂β₂ heterotetramer. By contrast, the human **mitochondrial PheRS** is an active *monomer* — a chimera of the α catalytic module and the β-subunit anticodon-binding domain — illustrating that multimerization is not a prerequisite for catalysis [PMID: 21082706](https://pubmed.ncbi.nlm.nih.gov/21082706/). This variability means no single quaternary architecture can be taken as representative.

### 4.3 GatCAB: the bacterial amidotransferase

GatCAB is a heterotrimer:
- **GatA** — amidase/glutaminase; hydrolyzes the amide donor (Gln/Asn) to release ammonia.
- **GatB** — the catalytic core; binds the misacylated tRNA, phosphorylates the tRNA-bound Asp/Glu, and amidates it. Contains divalent-metal sites for the two chemical steps and a conserved, often Zn²⁺-stabilized architecture with a water-filled **ammonia channel** running from GatA to GatB [PMID: 19520089](https://pubmed.ncbi.nlm.nih.gov/19520089/).
- **GatC** — small subunit required for GatA folding/stability.

GatCAB accepts glutamine, asparagine, *or* free ammonia as the amide donor, with ATP (or GTP) for the kinase step [PMID: 11585842](https://pubmed.ncbi.nlm.nih.gov/11585842/). Crucially, in a minimal organism such as *Chlamydia trachomatis*, a single GatCAB plus 18 aaRS suffices to make all 20 aa-tRNAs [PMID: 11585842](https://pubmed.ncbi.nlm.nih.gov/11585842/). GatCAB is **essential** in mycobacteria and is a validated, pathogen-selective antibacterial target [PMID: 33072044](https://pubmed.ncbi.nlm.nih.gov/33072044/), [PMID: 26976271](https://pubmed.ncbi.nlm.nih.gov/26976271/).

### 4.4 The transamidosome

In bacteria, ND-AspRS (or ND-GluRS), GatCAB, and tRNA assemble into a **transamidosome** — a ribonucleoprotein particle in which the tRNA acts simultaneously as substrate and structural scaffold, channeling the misacylated intermediate from the synthetase site directly to the GatCAB site. This was established by the crystal structure of the *Thermus thermophilus* Asn-transamidosome [PMID: 20717102](https://pubmed.ncbi.nlm.nih.gov/20717102/) and the ~400-kDa *Pseudomonas aeruginosa* Asn-transamidosome [PMID: 25548166](https://pubmed.ncbi.nlm.nih.gov/25548166/). The bacterial architecture, driven by a bacteria-specific GAD domain of ND-AspRS, is more dynamic than the archaeal-type complex, with faster ND-AspRS turnover.

```
        [ ND-AspRS ]                         [ GatCAB ]
             |  charges Asp onto tRNA(Asn)        |  amidates Asp->Asn
             v                                    v
   tRNA(Asn) --------- Asp-tRNA(Asn) ==channeled==> Asn-tRNA(Asn)
             \______________ transamidosome scaffold ______________/
                        (tRNA is both substrate and scaffold)
```

### 4.5 Kinetic and structural safeguards

Beyond physical channeling, the *Helicobacter pylori* ND-AspRS shows a **dual-kinetic safeguard**: it releases the misacylated Asp-tRNA(Asn) much more slowly than the cognate Asp-tRNA(Asp), giving GatCAB time to bind and transamidate before the dangerous intermediate can escape to EF-Tu and the ribosome [PMID: 22362756](https://pubmed.ncbi.nlm.nih.gov/22362756/).

---

## 5. Evolutionary and Cell-Biological Variation

### 5.1 The indirect route is ancestral; direct GlnRS/AsnRS are later

Phylogeny places the indirect transamidation pathways *before* the archaeal–bacterial split: "life used two-step indirect pathways to synthesize asparagine and glutamine on their cognate tRNAs" before that divergence [PMID: 38391119](https://pubmed.ncbi.nlm.nih.gov/38391119/). Bacterial **GlnRS** has a **eukaryotic origin** and was acquired by HGT [PMID: 8078941](https://pubmed.ncbi.nlm.nih.gov/8078941/); GlnRS is absent from Archaea, and the last common ancestor (cenancestor) is inferred to have used transamidation to make Gln-tRNA(Gln) [PMID: 10486006](https://pubmed.ncbi.nlm.nih.gov/10486006/). Consequently, the *ancestral* representative for understanding amide aa-tRNA formation is the **ND-synthetase + GatCAB** pair, not the direct enzymes.

### 5.2 Discriminating vs. non-discriminating synthetases

Whether AspRS/GluRS charges only its cognate tRNA (discriminating, D-) or also the amide tRNA (non-discriminating, ND-) is set by a small number of residues. For GluRS, the non-discriminating form lacks an anticodon-recognizing arginine (Arg358→Gly366 in *Thermosynechococcus elongatus*), relaxing specificity so it tolerates both the C36 of tRNA(Glu) and the bulkier G36 of tRNA(Gln) [PMID: 16876193](https://pubmed.ncbi.nlm.nih.gov/16876193/). Because ND-synthetases can flood the cell with mischarged tRNA, they are almost always paired with GatCAB, and their intermediates are protected.

### 5.3 Lineage-specific arrangements

- **Minimal set:** *Chlamydia trachomatis* — 18 aaRS + one GatCAB makes all 20 aa-tRNAs [PMID: 11585842](https://pubmed.ncbi.nlm.nih.gov/11585842/).
- **α-proteobacteria:** *Rhizobium meliloti* lacks GlnRS entirely and uses transamidation for Gln-tRNA(Gln), consistent with the mitochondrial ancestry of this subdivision [PMID: 8662929](https://pubmed.ncbi.nlm.nih.gov/8662929/).
- **Second AspRS solution:** *Deinococcus radiodurans*, *Thermus thermophilus*, and others encode a *second*, dedicated ND-AspRS to feed GatCAB while a discriminating AspRS handles tRNA(Asp). *Bdellovibrio bacteriovorus*, by contrast, uses a single ND-AspRS for both, providing a tRNA-dependent biosynthetic route to asparagine [PMID: 25338061](https://pubmed.ncbi.nlm.nih.gov/25338061/).
- **Retained indirect route despite having AsnRS:** *Bacillus subtilis* and *B. halodurans* encode AsnRS yet retain non-discriminating AspRS activity; ~30% of bacteria may carry both routes, and discrimination toward tRNA(Asp) evolved independently multiple times [PMID: 26804570](https://pubmed.ncbi.nlm.nih.gov/26804570/).
- **Duplicated GluRS:** Many bacteria encode GluRS1 (discriminating) and GluRS2 (tRNA(Gln)-specific), a chimeric enzyme whose catalytic and anticodon-binding domains were independently acquired by HGT [PMID: 24521160](https://pubmed.ncbi.nlm.nih.gov/24521160/), [PMID: 14615592](https://pubmed.ncbi.nlm.nih.gov/14615592/).

### 5.4 Bacteria vs. Archaea vs. organelles

Archaea deploy **two** amidotransferases — Gln-specific **GatDE** (heterodimer) and Asn-specific GatCAB — whereas bacteria use only GatCAB for both amides [PMID: 18291416](https://pubmed.ncbi.nlm.nih.gov/18291416/). The *Methanothermobacter thermautotrophicus* GatDE:tRNA(Gln) structure revealed a ~40 Å ammonia channel and, strikingly, tRNA(Gln) recognition by **indirect readout of D-loop shape, independent of the anticodon** — a plausibly ancient, RNA-based mode of adding glutamine to the code [PMID: 16809540](https://pubmed.ncbi.nlm.nih.gov/16809540/). Bacterial and archaeal GatCAB also differ in tRNA recognition: bacterial GatCAB reads the first acceptor-stem base pair and the D-loop, whereas archaeal GatCAB reads the tertiary core [PMID: 19906721](https://pubmed.ncbi.nlm.nih.gov/19906721/). Organelles (plant mitochondria, the *Plasmodium* apicoplast) reuse bacterial-type indirect machinery, sometimes with unique subunit compositions such as a heterodimeric GatAB [PMID: 26318454](https://pubmed.ncbi.nlm.nih.gov/26318454/).

---

## 6. Constraints, Dependencies, and Failure Modes

### 6.1 Mandatory ordering

1. **Activation before transfer.** No aa-tRNA forms without prior aa-AMP.
2. **Misacylation before transamidation.** Asp-tRNA(Asn) and Glu-tRNA(Gln) are obligate precursors; GatCAB cannot act on free amino acid or uncharged tRNA. This is a defining relationship of the pathway: ND-AspRS feeds Asp-tRNA(Asn) to GatCAB, and ND-GluRS feeds Glu-tRNA(Gln) to GatCAB.
3. **Serylation before selenocysteine (adjacent pathway).** SerRS must charge tRNA(Sec) before SelA can convert it — an example of the same ordering logic, outside the canonical boundary.

### 6.2 Mutually exclusive / substrate-specific events

- The direct and indirect amide routes are **alternative** endpoints-by-different-means; within a given tRNA/amino-acid pair an organism generally commits to one.
- Class I 2′-OH vs. class II 3′-OH acylation is a fixed, family-specific property.
- ND-synthetases are dangerous precisely because they relax anticodon discrimination; their use *requires* a downstream corrector (GatCAB) and a safeguard against release.

### 6.3 Fidelity safeguards and how they can fail

Fidelity is defended redundantly:
- **Editing (double sieve)** removes near-cognate mischarging within a single synthetase [PMID: 9554847](https://pubmed.ncbi.nlm.nih.gov/9554847/).
- **Channeling** in the transamidosome hides the misacylated intermediate from EF-Tu [PMID: 20717102](https://pubmed.ncbi.nlm.nih.gov/20717102/).
- **Kinetic proofreading** (slow release of the mischarged intermediate) supplements channeling [PMID: 22362756](https://pubmed.ncbi.nlm.nih.gov/22362756/).

**Tunable failure as a feature.** GatCAB is not merely essential; it is a *modulator of specific translational fidelity* [PMID: 27564922](https://pubmed.ncbi.nlm.nih.gov/27564922/). Clinically relevant mycobacterial GatCAB mutations alter fidelity, and controlled Glu→Gln / Asp→Asn mistranslation can confer phenotypic antibiotic (e.g., rifampicin) tolerance [PMID: 34225495](https://pubmed.ncbi.nlm.nih.gov/34225495/). Thus the indirect route is simultaneously an accuracy device and a controlled source of adaptive mistranslation.

### 6.4 Drug-target vulnerability

Because bacteria lacking direct GlnRS/AsnRS depend wholly on ND-synthetases + GatCAB — enzymes absent from the human cytoplasm — these steps are attractive, pathogen-selective targets. Cyclic-peptide inhibitors of *H. pylori* GatCAB have been identified [PMID: 26976271](https://pubmed.ncbi.nlm.nih.gov/26976271/). The direct aaRS active sites are also validated targets: **mupirocin** (pseudomonic acid), the only clinically approved aaRS inhibitor, occupies the isoleucyl-adenylate pocket of bacterial IleRS, and resistance arises via active-site signature-motif mutations [PMID: 37679387](https://pubmed.ncbi.nlm.nih.gov/37679387/), [PMID: 38246751](https://pubmed.ncbi.nlm.nih.gov/38246751/).

---

## 7. Controversies and Open Questions

### 7.1 Is channeling universal? No.

The most important nuance uncovered in this review is that **substrate channeling is one fidelity solution among several, not a universal rule.** Bacterial transamidosomes physically channel the intermediate [PMID: 20717102](https://pubmed.ncbi.nlm.nih.gov/20717102/), [PMID: 22362756](https://pubmed.ncbi.nlm.nih.gov/22362756/). Yet transient-kinetic analysis of the *archaeal* ND-GluRS/GatDE system shows two-step Gln-tRNA(Gln) synthesis proceeds **without channeling and without a stable GluRS–GatDE binary complex**; accuracy is instead maintained by rapid GatDE processing of the intermediate plus preferential EF-Tu binding to the cognate product [PMID: 21726564](https://pubmed.ncbi.nlm.nih.gov/21726564/). Care is therefore needed not to generalize the elegant bacterial transamidosome mechanism to all indirect pathways. (Note that the archaeal ND-GluRS–GatDE complex, where it does form, does not require tRNA to assemble, unlike the bacterial complex — another point of divergence [PMID: 20457752](https://pubmed.ncbi.nlm.nih.gov/20457752/).)

### 7.2 Origin and spread of GlnRS

The eukaryotic-HGT origin of bacterial GlnRS is well supported [PMID: 8078941](https://pubmed.ncbi.nlm.nih.gov/8078941/), but the fine-grained history is convoluted: bacterial GlnRS appears to have arrived both by HGT from eukarya and by intra-bacterial HGT, GlnRS is more widespread than once thought, and some genomes retain GlnRS pseudogenes indicating failed acquisitions [PMID: 24521160](https://pubmed.ncbi.nlm.nih.gov/24521160/). The chimeric nature of GluRS2 further complicates simple narratives.

### 7.3 Best ancestral representative

For reconstructing the ancestral amide-charging role, the **ND-synthetase + GatCAB** module and, for tRNA recognition, the anticodon-*independent* D-loop readout seen in GatDE [PMID: 16809540](https://pubmed.ncbi.nlm.nih.gov/16809540/) are more informative than the derived, anticodon-reading direct enzymes. Which extant enzyme best proxies the last common ancestor remains debated and depends on the phylogenetic method.

### 7.4 Organisms mixed in the literature

A recurring hazard is over-generalization across domains and compartments. Bacterial GatCAB, archaeal GatDE, apicoplast GatAB, and organellar systems differ in subunit composition, tRNA recognition (first base pair and D-loop in bacteria vs. tertiary core in archaea [PMID: 19906721](https://pubmed.ncbi.nlm.nih.gov/19906721/)), and channeling behavior. Claims transferred between these systems should be treated with caution.

### 7.5 Key open questions

1. What determines, mechanistically and evolutionarily, whether a given bacterium keeps the indirect route, the direct route, or both?
2. How general is transamidosome channeling across bacterial phyla, and are there bacterial lineages that (like archaea) forgo it?
3. How is the fidelity-modulating, adaptive-mistranslation activity of GatCAB regulated physiologically, and can it be therapeutically exploited or blocked?
4. Can pathogen-selective inhibitors of ND-synthetases or GatCAB be advanced to clinically useful antibacterials?

---

## 8. Mechanistic Model — Synthesis

```
                    BACTERIAL AMINOACYL-tRNA CHARGING
                    =================================

 DIRECT ROUTES (18-20 amino acids)
 ---------------------------------
   Class I aaRS (Rossmann fold; HIGH/KMSKS; 2'-OH)
     GluRS ArgRS CysRS IleRS LeuRS MetRS TrpRS TyrRS ValRS  (+GlnRS*)
   Class II aaRS (antiparallel beta-sheet; 3'-OH)
     SerRS AlaRS AspRS GlyRS HisRS LysRS PheRS ProRS ThrRS  (+AsnRS*)

     aa + ATP -> aa-AMP -> aa-tRNA          [+ editing for Ile/Val, Ala, Thr...]

 INDIRECT AMIDE ROUTES (ancestral; used by most bacteria lacking GlnRS/AsnRS)
 ---------------------------------------------------------------------------
   Asn:  tRNA(Asn) --ND-AspRS--> Asp-tRNA(Asn) --GatCAB--> Asn-tRNA(Asn)
   Gln:  tRNA(Gln) --ND-GluRS--> Glu-tRNA(Gln) --GatCAB--> Gln-tRNA(Gln)
         (intermediates channeled in transamidosome + slow-release kinetics)

 BOUNDARY: opens at (amino acid + ATP + uncharged tRNA)
           closes at correctly charged CANONICAL aa-tRNA
           Asp-tRNA(Asn), Glu-tRNA(Gln) = internal intermediates, NOT endpoints

 OUT OF SCOPE: Sec (SerRS+SelA), archaeal Cys (SepRS/SepCysS),
               archaeal GatDE, organellar systems, EF-Tu/ribosome
   * GlnRS/AsnRS present only in some bacteria (often eukaryote-derived HGT)
```

The unifying logic: two independently invented enzyme superfamilies converged on identical two-step chemistry; specificity is set by an operational RNA code; fidelity is defended by editing and, for the ancestral amide routes, by protecting a deliberately mischarged intermediate until a dedicated amidotransferase corrects it. The direct amide synthetases are evolutionary latecomers layered onto this ancient scaffold.

---

## 9. Limitations and Knowledge Gaps

- **Genome-inferred route assignments** (e.g., "~30% of bacteria may carry both Asn routes" [PMID: 26804570](https://pubmed.ncbi.nlm.nih.gov/26804570/)) rest partly on sequence prediction; the discrimination status of many AspRS/GluRS enzymes has not been biochemically verified.
- **Channeling generality is uncertain.** Direct kinetic tests exist for only a handful of organisms; the bacterial-vs-archaeal contrast ([PMID: 20717102](https://pubmed.ncbi.nlm.nih.gov/20717102/) vs. [PMID: 21726564](https://pubmed.ncbi.nlm.nih.gov/21726564/)) warns against extrapolation.
- **Cross-organism mixing.** Much mechanistic detail comes from thermophiles (*Thermus*, *Aquifex*) and model pathogens (*H. pylori*, mycobacteria); physiological regulation in diverse bacteria is under-sampled.
- **This review is literature-synthetic**, not based on new experimental or primary sequence-dataset analysis; all conclusions inherit the uncertainties of the cited primary work.
- **Quantitative flux** through direct vs. indirect routes in organisms that possess both is largely unknown.

---

## 10. Proposed Follow-up Analyses and Experiments

1. **Comparative genomics of route choice.** Systematically classify AspRS/GluRS as discriminating vs. non-discriminating across sequenced bacteria and correlate with presence/absence of GlnRS, AsnRS, and GatCAB — to quantify how often each route (and dual routes) occurs and in which lineages.
2. **Transamidosome assembly survey.** Test in vitro whether transamidosomes form and channel in phylogenetically diverse bacteria (beyond *Thermus*/*Pseudomonas*) using transient kinetics, to map the boundary of the channeling paradigm.
3. **Fidelity-tuning under stress.** Quantify Glu→Gln / Asp→Asn mistranslation as a function of GatCAB level/mutation and antibiotic exposure, connecting adaptive mistranslation [PMID: 34225495](https://pubmed.ncbi.nlm.nih.gov/34225495/) to phenotypic tolerance.
4. **Inhibitor development.** Advance GatCAB and ND-synthetase inhibitors (building on cyclic-peptide leads [PMID: 26976271](https://pubmed.ncbi.nlm.nih.gov/26976271/)) with selectivity counter-screens against human cytoplasmic aaRS.
5. **Ancestral-state reconstruction** of GatB/GatE and GluRS/GlnRS to test which extant enzyme best represents the LUCA-era amide-charging module.

---

## 11. Key References

| PMID | Contribution to this review |
|---|---|
| [2203971](https://pubmed.ncbi.nlm.nih.gov/2203971/) | Defines the two aaRS classes by mutually exclusive motifs; 2′/3′-OH functional split |
| [7783225](https://pubmed.ncbi.nlm.nih.gov/7783225/) | Class I Rossmann fold vs. class II antiparallel β-sheet |
| [11585842](https://pubmed.ncbi.nlm.nih.gov/11585842/) | Single GatCAB makes both amide aa-tRNAs; amide donors and nucleotide use (*Chlamydia*) |
| [38391119](https://pubmed.ncbi.nlm.nih.gov/38391119/) | Indirect amide routes predate the archaeal–bacterial split |
| [8078941](https://pubmed.ncbi.nlm.nih.gov/8078941/) | Bacterial GlnRS is eukaryote-derived, acquired by HGT |
| [10486006](https://pubmed.ncbi.nlm.nih.gov/10486006/) | Cenancestor used transamidation for Gln-tRNA(Gln) |
| [16876193](https://pubmed.ncbi.nlm.nih.gov/16876193/) | Structural basis of non-discriminating GluRS (Arg→Gly) |
| [9554847](https://pubmed.ncbi.nlm.nih.gov/9554847/) | Double-sieve editing in IleRS |
| [20717102](https://pubmed.ncbi.nlm.nih.gov/20717102/) | Transamidosome structure and channeling (*T. thermophilus*) |
| [25548166](https://pubmed.ncbi.nlm.nih.gov/25548166/) | ~400-kDa *P. aeruginosa* Asn-transamidosome; bacterial-type architecture |
| [22362756](https://pubmed.ncbi.nlm.nih.gov/22362756/) | Dual-kinetic slow-release safeguard (*H. pylori* ND-AspRS) |
| [19520089](https://pubmed.ncbi.nlm.nih.gov/19520089/) | GatCAB catalytic mechanism; ammonia channel; metal sites (*Aquifex*) |
| [18291416](https://pubmed.ncbi.nlm.nih.gov/18291416/) | Bacteria use only GatCAB; archaea also use GatDE |
| [16809540](https://pubmed.ncbi.nlm.nih.gov/16809540/) | GatDE ammonia channel; anticodon-independent D-loop readout |
| [20457752](https://pubmed.ncbi.nlm.nih.gov/20457752/) | Archaeal ND-GluRS–GatDE transamidosome affinity |
| [21726564](https://pubmed.ncbi.nlm.nih.gov/21726564/) | Archaeal two-step charging **without** channeling |
| [24049072](https://pubmed.ncbi.nlm.nih.gov/24049072/) | G3:U70 single-pair operational code for alanine |
| [31781936](https://pubmed.ncbi.nlm.nih.gov/31781936/) | Acceptor-stem operational code as ancient recognition mode |
| [21082706](https://pubmed.ncbi.nlm.nih.gov/21082706/) | Heterotetrameric bacterial PheRS structure |
| [26804570](https://pubmed.ncbi.nlm.nih.gov/26804570/) | Retained indirect Asn route in *Bacillus*; independent evolution of AspRS discrimination |
| [25338061](https://pubmed.ncbi.nlm.nih.gov/25338061/) | Single ND-AspRS route in *Bdellovibrio* |
| [24521160](https://pubmed.ncbi.nlm.nih.gov/24521160/) | Convoluted GlxRS evolution; GluRS2 chimera; GlnRS pseudogenes |
| [14615592](https://pubmed.ncbi.nlm.nih.gov/14615592/) | Duplicated GluRS with complementary tRNA specificities |
| [27564922](https://pubmed.ncbi.nlm.nih.gov/27564922/) | GatCAB modulates specific translational fidelity |
| [34225495](https://pubmed.ncbi.nlm.nih.gov/34225495/) | Clinically relevant GatCAB mutations; fidelity/tolerance link |
| [33072044](https://pubmed.ncbi.nlm.nih.gov/33072044/) | Essential indirect pathway in mycobacteria |
| [26976271](https://pubmed.ncbi.nlm.nih.gov/26976271/) | GatCAB essential; cyclic-peptide inhibitors |
| [37679387](https://pubmed.ncbi.nlm.nih.gov/37679387/) | Mupirocin targets IleRS; resistance via motif mutation |
| [38246751](https://pubmed.ncbi.nlm.nih.gov/38246751/) | Structural basis of IleRS substrate/antibiotic recognition |
| [23559248](https://pubmed.ncbi.nlm.nih.gov/23559248/) | Bacterial SelA decamer; distinct from archaeal SepSecS |
| [25002468](https://pubmed.ncbi.nlm.nih.gov/25002468/) | Archaeal indirect Cys pathway (SepRS/SepCysS) |
| [18267971](https://pubmed.ncbi.nlm.nih.gov/18267971/) | SerRS-initiated indirect Sec route |
| [11732603](https://pubmed.ncbi.nlm.nih.gov/11732603/) | Genome-era view of non-canonical aa-tRNA synthesis |

---

*Prepared as a commissioned review-style synthesis. Confidence is highest for the two-class architecture, the two-step chemistry, the essentiality and mechanism of GatCAB, and the ancestral status of the indirect amide routes; it is lower for genome-predicted route assignments and for the generality of transamidosome channeling across bacterial phyla, where the literature mixes data from bacteria, archaea, and organelles that may not be directly comparable.*


## Artifacts

- [OpenScientist final report](bacterial_aminoacyl_trna_charging-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](bacterial_aminoacyl_trna_charging-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:2203971
2. PMID:7783225
3. PMID:11585842
4. PMID:38391119
5. PMID:8078941
6. PMID:10486006
7. PMID:18267971
8. PMID:23559248
9. PMID:25002468
10. PMID:18291416
11. PMID:11732603
12. PMID:11375928
13. PMID:24049072
14. PMID:31781936
15. PMID:9554847
16. PMID:19520089
17. PMID:21082706
18. PMID:33072044
19. PMID:26976271
20. PMID:20717102
21. PMID:25548166
22. PMID:22362756
23. PMID:16876193
24. PMID:8662929
25. PMID:25338061
26. PMID:26804570
27. PMID:24521160
28. PMID:14615592
29. PMID:16809540
30. PMID:19906721
31. PMID:26318454
32. PMID:27564922
33. PMID:34225495
34. PMID:37679387
35. PMID:38246751
36. PMID:21726564
37. PMID:20457752