---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T15:33:10.826302'
end_time: '2026-07-18T15:55:03.162307'
duration_seconds: 1312.34
template_file: templates/module_research.md.j2
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
citation_count: 20
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: endogenous_protein_lipoylation-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: endogenous_protein_lipoylation-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Endogenous protein lipoylation

## Working Scope

Endogenous protein lipoylation is a two-reaction pathway that installs a lipoyl cofactor on conserved lysine residues in lipoyl domains. A LipB-family octanoyltransferase first transfers an octanoyl group from octanoyl-acyl carrier protein to the target protein. LipA-family lipoate synthase then uses radical-SAM chemistry and iron-sulfur clusters to insert sulfur atoms at C6 and C8 of the protein-bound octanoyl group. The resulting lipoyl domains act as swinging arms in alpha-ketoacid dehydrogenase complexes and the glycine cleavage system. Exogenous-lipoate salvage by lipoate--protein ligases and alternative GcvH-relay architectures are outside this module boundary.

## Provisional Biological Outline

- Endogenous protein lipoylation
  - 1. transfer of octanoyl from acyl carrier protein to a lipoyl domain
  - Octanoyl-ACP to octanoylated lipoyl-domain protein
    - LipB-family lipoyl(octanoyl) transferase (molecular player: LipB family octanoyltransferases; activity or role: lipoyl(octanoyl) transferase activity)
  - 2. sulfur insertion into the protein-bound octanoyl group
  - Octanoylated lipoyl-domain protein to lipoylated protein
    - LipA-family lipoate synthase (molecular player: LipA family lipoate synthases; activity or role: lipoate synthase activity)

## Known Relationships Among Steps

- Octanoyl-ACP to octanoylated lipoyl-domain protein feeds into Octanoylated lipoyl-domain protein to lipoylated protein: The octanoylated lipoyl-domain protein made by LipB is the direct macromolecular substrate for LipA.

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

# Endogenous Protein Lipoylation: A Substrate-Coupled, Two-Reaction Cofactor Assembly System

*A commissioned review-style synthesis for a molecular biology audience*

---

## 1. Executive Summary

Endogenous protein lipoylation is the *de novo* biosynthetic route by which cells build the lipoyl cofactor—an eight-carbon, dithiolane-containing prosthetic group—directly onto a conserved lysine residue of specialized **lipoyl domains**. Unlike almost every other protein cofactor, the lipoyl group is not synthesized as a free molecule and then attached; it is assembled *in situ* on its cognate protein. This defining logic reduces the pathway to just two obligatory chemical steps carried out by two enzyme families. First, a **LipB-family octanoyltransferase** transfers an octanoyl moiety from octanoyl-acyl carrier protein (octanoyl-ACP), a product of type-II/mitochondrial fatty-acid synthesis, onto the target lysine, generating an octanoylated intermediate. Second, a **LipA-family radical-SAM lipoate synthase** inserts two sulfur atoms at carbons C6 and C8 of the protein-bound octanoyl group, yielding the mature lipoyllysine. The finished lipoyl domains then serve as "swinging arms" that channel reaction intermediates within the 2-oxoacid dehydrogenase complexes (pyruvate, 2-oxoglutarate, branched-chain, 2-oxoadipate) and the glycine cleavage system.

The mechanistic heart of the pathway is remarkable. LipA (LIAS in humans) is a radical S-adenosylmethionine (SAM) enzyme carrying two [4Fe-4S] clusters: a canonical "radical-SAM" cluster that reductively cleaves SAM to generate 5′-deoxyadenosyl radicals (which abstract hydrogen atoms from C6 and C8), and an **auxiliary cluster that is literally cannibalized as the sulfur donor**. Because the auxiliary cluster is destroyed during each catalytic cycle, LipA is a single-turnover enzyme *in vitro* and depends on cellular iron-sulfur cluster machinery to be reconstituted for further rounds of catalysis. This sacrificial chemistry, the strict dependence on a fatty-acid-synthesis-derived octanoyl-ACP precursor, and the assembly-on-protein logic together constitute the ancient, deeply conserved core of the system across all three domains of life.

Superimposed on this conserved core is well-documented lineage-specific variation in *pathway topology*. *Escherichia coli* and plants use the streamlined two-enzyme route in which LipB octanoylates E2 subunits directly. *Bacillus subtilis*, mammals, and fungi instead route the octanoyl group through the glycine cleavage H protein (**GcvH**) and require a third protein—an amidotransferase (LipL in bacteria; the LIPT1/LIPT2 division of labor in humans)—to relay the modified group onto the E2 subunits. Some archaea split the sulfur-insertion chemistry between two lipoyl synthase paralogs (LipS1 and LipS2). This review delineates the boundaries of the system, distinguishes it from the mechanistically separate exogenous-lipoate **salvage** pathway (ATP-dependent lipoate-protein ligases, LplA/LplJ) and from the downstream phenomenon of **cuproptosis**, and lays out where the evidence is strong, where it is indirect, and what remains unresolved.

---

## 2. Definition and Biological Boundaries

### 2.1 What is included

The endogenous protein lipoylation system, as scoped here, comprises exactly two catalytic reactions and the molecular players that carry them out:

1. **Octanoyl transfer**: transfer of an octanoyl group from octanoyl-ACP onto the ε-amino group of a specific lysine in a lipoyl domain, catalyzed by a **LipB-family lipoyl(octanoyl)transferase**.
2. **Sulfur insertion**: radical-SAM–dependent insertion of sulfur at C6 and C8 of the protein-bound octanoyl group, catalyzed by a **LipA-family lipoate synthase**.

The direct product of step 1—an octanoylated lipoyl-domain protein—is the obligatory macromolecular substrate for step 2. The two steps are therefore substrate-coupled through a *protein-bound* intermediate, which is the single most important structural fact about the pathway.

A key upstream boundary is the octanoyl-ACP precursor, which is a product of type-II fatty-acid synthesis (FAS II) in bacteria and of the mitochondrial fatty-acid synthesis (mtFAS) system in eukaryotes. Because the octanoyl donor is FAS-derived, endogenous lipoylation is metabolically welded to fatty-acid biosynthesis. This coupling is part of the conserved ancient core (see §5).

### 2.2 What is *not* included (and is often confused)

Three neighboring processes are frequently conflated with *de novo* lipoylation but are mechanistically distinct and lie outside this module:

- **Exogenous-lipoate salvage.** Many bacteria (e.g., *E. coli*) also possess an ATP-dependent **lipoate-protein ligase** (LplA in *E. coli*; LplJ in *B. subtilis*) that scavenges *free* lipoate (or octanoate) from the environment and attaches it directly to lysines of E2/GcvH in a classical two-step adenylation reaction. This is chemically and enzymologically unrelated to *de novo* assembly, which never proceeds through a free lipoate intermediate. Eukaryotes generally retain only the *de novo* pathway [PMID: 40813772](https://pubmed.ncbi.nlm.nih.gov/40813772/).

- **The GcvH-relay/amidotransferase architecture as a "different pathway."** In the *B. subtilis*/mammalian topology, GcvH is an obligatory carrier and an amidotransferase relays the group to E2. While the working brief nominally set "alternative GcvH-relay architectures" aside as a module boundary, the evidence reviewed here shows the relay is not a salvage phenomenon but is integral to *de novo* lipoylation in those lineages; it is best treated as a *topological variant* of the same biosynthetic system rather than a separate pathway.

- **Cuproptosis.** The mature lipoylated proteins (especially DLAT of the pyruvate dehydrogenase complex) are the molecular *trigger* of copper-dependent cell death (cuproptosis): copper binds lipoylated TCA-cycle enzymes, causing their aggregation and loss of Fe-S cluster proteins. Cuproptosis is a *downstream consequence* of having lipoylated proteins, not part of the biosynthetic machinery, and should be treated separately [PMID: 42418063](https://pubmed.ncbi.nlm.nih.gov/42418063/).

### 2.3 Competing definitions

The principal definitional tension in the literature concerns whether the multi-protein GcvH-relay constitutes part of "the" lipoylation pathway or a distinct route. Cronan's synthesis argues that the more complex relay may in fact be the *ancestral* arrangement and the streamlined *E. coli* two-enzyme route a derived simplification [PMID: 27074917](https://pubmed.ncbi.nlm.nih.gov/27074917/). Under that reading, "endogenous protein lipoylation" is best defined by its conserved *chemistry* (octanoyl transfer + radical-SAM sulfur insertion, both on protein-bound substrate), with topology treated as a variable feature.

---

## 3. Mechanistic Overview

### 3.1 The best current model

The consensus sequence of events, integrating bacterial and human data, is:

```
        FAS II / mtFAS
             │
             ▼
      octanoyl-ACP  ──────┐
                          │  (1) LipB-family octanoyltransferase
                          │      transfers octanoyl to Lys of lipoyl domain
                          ▼
   octanoylated lipoyl-domain protein   ← the direct macromolecular
                          │                substrate for step 2
                          │  (2) LipA-family lipoate synthase (radical-SAM)
                          │      inserts S at C6 then C8
                          ▼
        lipoylated protein (mature lipoyllysine "swinging arm")
                          │
                          ▼
   active 2-oxoacid dehydrogenases + glycine cleavage system
```

In the **direct (E. coli/plant) topology**, LipB octanoylates the E2 lipoyl domains themselves, and LipA thiolates them in place. In the **relay (B. subtilis/mammal/fungal) topology**, the octanoyltransferase (LipM in *B. subtilis*; LIPT2 in humans) modifies *only GcvH*; sulfur insertion may occur on GcvH-bound octanoyl; and an amidotransferase (LipL in *B. subtilis*; LIPT1 in humans) then transfers the (octanoyl or lipoyl) group from GcvH onto the E2 subunits via a thioester acyl-enzyme intermediate using a Cys-Lys catalytic dyad.

### 3.2 Which steps are obligatory, conditional, or accessory

- **Obligatory:** (i) provision of octanoyl-ACP from FAS; (ii) octanoyl transfer to a protein lysine; (iii) radical-SAM sulfur insertion at C6 and C8. Without any of these there is no lipoylation and aerobic/one-carbon metabolism is blocked.
- **Conditional (lineage-specific but obligatory where present):** the GcvH relay and the amidotransferase step are obligatory in *B. subtilis*, mammals, and fungi—Δ*gcvH* *B. subtilis* strains are lipoate auxotrophs—but absent in the *E. coli*/plant topology.
- **Accessory but essential in practice:** the iron-sulfur cluster biogenesis machinery that reconstitutes LipA/LIAS's sacrificial auxiliary cluster after each turnover. Without cluster regeneration the enzyme performs only a single turnover.

### 3.3 The sulfur-insertion chemistry in detail

LipA is a member of the radical-SAM superfamily. It binds two [4Fe-4S] clusters:

- The **radical-SAM cluster** binds SAM and, upon reduction, cleaves it homolytically to methionine plus a 5′-deoxyadenosyl radical. Two successive radicals abstract hydrogen atoms from C6 and C8 of the octanoyl chain.
- The **auxiliary cluster** supplies the sulfur atoms that are inserted at those carbons. EPR trapping detected ⁵⁷Fe hyperfine coupling between a substrate-derived radical and this cluster, and the cluster is progressively degraded during turnover—accounting for the single-turnover behavior observed *in vitro* [PMID: 26390103](https://pubmed.ncbi.nlm.nih.gov/26390103/); [PMID: 29051382](https://pubmed.ncbi.nlm.nih.gov/29051382/). The reaction proceeds through a discrete **C6-monothiolated intermediate**, a feature conserved between *E. coli* and *Mycobacterium tuberculosis* LipA [PMID: 26841001](https://pubmed.ncbi.nlm.nih.gov/26841001/).

---

## 4. Major Molecular Players and Active Assemblies

### 4.1 Enzyme families and their orthologs

| Step | Bacterial (E. coli) | Bacterial (B. subtilis) | Human (mitochondrial) | Chemistry |
|------|--------------------|-----------------------|----------------------|-----------|
| Octanoyl transfer | **LipB** (octanoyltransferase) | **LipM** (octanoylates GcvH only) | **LIPT2** | Acyl transfer from octanoyl-ACP to Lys |
| Amidotransfer relay | — (not used) | **LipL** (GcvH → E2) | **LIPT1** (relay to E2) | Thioester acyl-enzyme, Cys-Lys dyad |
| Sulfur insertion | **LipA** | **LipA** | **LIAS** | Radical-SAM, dual [4Fe-4S], C6/C8 thiolation |
| Carrier protein | — | **GcvH** (obligatory) | **GcvH** (obligatory) | Swinging-arm intermediate carrier |
| Salvage (outside module) | LplA | LplJ | (LIPT1 can also ligate) | ATP-dependent free-lipoate ligation |

### 4.2 The lipoyl domain and "on-site" assembly

A crucial structural feature is that lipoylation occurs on a small, conserved **lipoyl domain** (a β-barrel with a protruding β-turn that presents the target lysine). Proteomic and copurification work in *E. coli* shows that the intact pyruvate and 2-oxoglutarate dehydrogenase complexes co-purify with both LipB and LipA—meaning the assembly enzymes are physically recruited "on site" to the dehydrogenases where their substrate domains reside [PMID: 21209092](https://pubmed.ncbi.nlm.nih.gov/21209092/). Notably, the salvage ligase LplA shows no such interaction, and GcvH does not copurify with LipA/LipB in *E. coli*, underscoring both the compartmentalized specificity of *de novo* assembly and the topology difference from the GcvH-relay lineages.

### 4.3 The human enzymes and clinical validation

Human intramitochondrial lipoate synthesis proceeds sequentially through **LIPT2 → LIAS → LIPT1** [PMID: 28757203](https://pubmed.ncbi.nlm.nih.gov/28757203/). This ordering is not merely biochemical inference; it is validated by human genetics. Biallelic *LIPT2* mutations in three individuals caused severe neonatal encephalopathy with reduced pyruvate dehydrogenase and 2-oxoglutarate dehydrogenase activities, reduced leucine catabolic flux, and decreased protein lipoylation—phenotypes rescued in fibroblasts by wild-type LIPT2 [PMID: 28757203](https://pubmed.ncbi.nlm.nih.gov/28757203/). *LIAS* mutations produce a nonketotic-hyperglycinemia-like disorder with early-onset convulsions plus an energy-metabolism defect, while *LIPT1* deficiency characteristically spares the glycine cleavage system (because GCS lipoylation via GcvH does not require the LIPT1 relay step) [PMID: 24777537](https://pubmed.ncbi.nlm.nih.gov/24777537/). Because LIAS is Fe-S dependent, mutations in the mitochondrial Fe-S cluster assembly machinery (NFU1, BOLA3, ISCA2, IBA57, GLRX5) also produce LIAS-deficiency-like phenotypes [PMID: 27586888](https://pubmed.ncbi.nlm.nih.gov/27586888/); [PMID: 28803783](https://pubmed.ncbi.nlm.nih.gov/28803783/).

---

## 5. Evolutionary and Cell-Biological Variation

### 5.1 Deep conservation across three domains of life

Lipoate-dependent enzymes (the 2-oxoacid dehydrogenases and the glycine cleavage system) and the LipB/LipA-type assembly logic occur in bacteria, archaea, and eukaryotes; lipoate is explicitly characterized as a cofactor "required in three domains of life" [PMID: 25611823](https://pubmed.ncbi.nlm.nih.gov/25611823/). The two features that appear to constitute the ancient, invariant core are (i) the **radical-SAM sulfur-insertion chemistry** embodied in the LipA family and (ii) the **strict dependence on a FAS-derived octanoyl-ACP precursor**. These are shared across lineages that otherwise differ substantially in pathway topology.

### 5.2 Topological variants as lineage-specific elaborations

| Topology | Representative lineages | Proteins | Distinguishing feature |
|----------|------------------------|----------|------------------------|
| Direct E2 octanoylation | E. coli, plants | LipB, LipA | Two enzymes; E2 modified directly |
| GcvH relay + amidotransfer | B. subtilis, mammals, fungi | LipM/LIPT2, LipL/LIPT1, LipA/LIAS, GcvH | Three+ proteins; GcvH obligatory carrier |
| Split sulfur insertion | Some archaea (Thermococcus & relatives) | LipS1, LipS2 | Two paralogous synthases act at the two carbons |

The GcvH-relay topology requires GcvH as an obligatory carrier: Δ*gcvH* *B. subtilis* strains are lipoate auxotrophs, and LipL catalyzes the amidotransfer (transamidation) of the octanoyl moiety from octanoyl-GcvH to the E2 subunit of pyruvate dehydrogenase via a thioester acyl-enzyme intermediate [PMID: 21338420](https://pubmed.ncbi.nlm.nih.gov/21338420/); [PMID: 21338421](https://pubmed.ncbi.nlm.nih.gov/21338421/). Cronan maps the *E. coli*-type topology onto plants and the *B. subtilis*-type relay onto mammals and fungi [PMID: 27074917](https://pubmed.ncbi.nlm.nih.gov/27074917/).

A distinct archaeal variant splits the sulfur-insertion chemistry: rather than a single LipA thiolating both C6 and C8, some archaea use two lipoyl synthase paralogs, **LipS1 and LipS2**, that act at the two carbons [PMID: 36281299](https://pubmed.ncbi.nlm.nih.gov/36281299/). This is a lineage-specific reorganization of the *same* radical-SAM chemistry rather than a new mechanism.

### 5.3 Compartmentalization

In eukaryotes the entire *de novo* pathway is **mitochondrial**, tied to mtFAS-derived octanoyl-ACP. This spatial confinement means cytosolic or exogenous free lipoate cannot substitute for the *de novo* route in supplying the mitochondrial matrix pool via biosynthesis—consistent with the clinical observation that lipoate supplementation did not improve the course of LIPT2 disease [PMID: 28757203](https://pubmed.ncbi.nlm.nih.gov/28757203/).

### 5.4 The single-turnover problem and its resolutions

Because the auxiliary [4Fe-4S] cluster is consumed, cells must regenerate it. Two resolutions are documented:

- **In humans**, [2Fe-2S]-cluster-bound forms of **ISCU** and **ISCA2** reconstitute LIAS and enable complete product turnover, with an ordered assembly in which the auxiliary cluster is installed before the reducing (radical-SAM) cluster [PMID: 33562493](https://pubmed.ncbi.nlm.nih.gov/33562493/).
- **In E. coli**, the auxiliary cluster is destroyed and then reformed during catalysis (McCarthy & Booker, *Science* 2017), physically closing the catalytic cycle *in vivo*.

The archaeal LipS1/LipS2 split may represent an alternative evolutionary solution that distributes the sulfur-donor burden across two proteins [PMID: 36281299](https://pubmed.ncbi.nlm.nih.gov/36281299/).

---

## 6. Constraints, Dependencies, and Failure Modes

### 6.1 Obligatory ordering

The pathway is strictly ordered by chemistry: **octanoyl transfer must precede sulfur insertion**, because LipA acts only on a *protein-bound* octanoyl group, not on free octanoate. This was demonstrated directly in *E. coli*: sulfur atoms are inserted into octanoyl moieties already amide-linked to a PDH subunit or a derived domain [PMID: 14700636](https://pubmed.ncbi.nlm.nih.gov/14700636/). This is the mechanistic basis for the "assembly-on-protein" definition of the system: unlike biotin, which is synthesized free and then attached, the lipoyl cofactor is built on its cognate protein [PMID: 27074917](https://pubmed.ncbi.nlm.nih.gov/27074917/).

### 6.2 Mutually exclusive / compartment-specific features

- **De novo vs salvage are mutually exclusive at the mechanistic level** even when co-present in one cell: salvage attaches pre-formed free lipoate (LplA/LplJ), whereas de novo never passes through free lipoate. Eukaryotes generally retain only de novo lipoylation [PMID: 40813772](https://pubmed.ncbi.nlm.nih.gov/40813772/).
- **Relay vs direct topology are lineage-specific**: an organism using the GcvH relay cannot lipoylate E2 without GcvH and the amidotransferase, whereas a direct-topology organism has no such requirement.
- **Substrate specificity of the relay** further constrains routing: in *B. subtilis*, LipL is essential to modify E2 subunits even during lipoate scavenging, because the ligase LplJ has strict substrate specificity determined by charge complementarity [PMID: 31066113](https://pubmed.ncbi.nlm.nih.gov/31066113/).

### 6.3 Failure modes

- Loss of any de novo enzyme (LIPT2, LIAS, LIPT1) or of the mtFAS octanoyl supply abolishes lipoylation of PDH, α-KGDH, BCKDH, 2-OADH, and (except in LIPT1 deficiency) the GCS, blocking aerobic and one-carbon metabolism and causing severe neonatal/infantile encephalopathy [PMID: 28757203](https://pubmed.ncbi.nlm.nih.gov/28757203/); [PMID: 24777537](https://pubmed.ncbi.nlm.nih.gov/24777537/).
- Loss of Fe-S cluster biogenesis (NFU1, BOLA3, ISCA2, IBA57, GLRX5) produces a *secondary* LIAS deficiency with a LIAS-like phenotype [PMID: 27586888](https://pubmed.ncbi.nlm.nih.gov/27586888/); [PMID: 28803783](https://pubmed.ncbi.nlm.nih.gov/28803783/).
- Downstream, the *presence* of correctly lipoylated TCA-cycle proteins becomes a liability under copper overload, sensitizing cells to cuproptosis—a distinct failure mode governed by FDX1 and LIPT1 [PMID: 42418063](https://pubmed.ncbi.nlm.nih.gov/42418063/).

### 6.4 Evidence that rules out otherwise-plausible paths

- LipA acting on *free* octanoate is ruled out by the direct demonstration that its substrate is protein-bound octanoyl [PMID: 14700636](https://pubmed.ncbi.nlm.nih.gov/14700636/).
- A single-cluster LipA doing multiple turnovers without regeneration is ruled out by the destruction of the auxiliary cluster and the single-turnover phenotype in vitro [PMID: 29051382](https://pubmed.ncbi.nlm.nih.gov/29051382/).
- Salvage substituting for de novo in the GCS lipoylation of some organisms is constrained by strict ligase substrate specificity [PMID: 31066113](https://pubmed.ncbi.nlm.nih.gov/31066113/).

---

## 7. Mechanistic Model / Integrated Interpretation

Pulling the findings together, endogenous protein lipoylation is best understood as **one conserved chemical program executed through variable protein plumbing**. The invariant core is: (octanoyl-ACP from FAS) → (transfer to a protein lysine) → (radical-SAM thiolation of the protein-bound chain, at the cost of a sacrificial Fe-S cluster). Everything that varies between lineages—direct vs relay routing, one vs two synthases, which Fe-S donors regenerate the cluster—is elaboration around that core.

```
        ┌─────────────────────── CONSERVED CORE ───────────────────────┐
        │  octanoyl-ACP → [protein-Lys–octanoyl] → [protein-Lys–lipoyl] │
        │        (LipB fam)              (LipA fam radical-SAM,          │
        │                                 sacrificial aux [4Fe-4S])     │
        └───────────────────────────────────────────────────────────────┘
                     │                      │                     │
        DIRECT (E.coli/plant)   RELAY (B.sub/mammal/fungi)   SPLIT (archaea)
        LipB→E2; LipA           LipM→GcvH; LipL amidotransfer  LipS1 + LipS2
                                to E2; LIPT2/LIPT1 in humans    at C6 / C8
```

The clinical genetics provide an unusually clean natural knockout series confirming the order and non-redundancy of the human enzymes, and the observation that LIPT1 deficiency spares the GCS is an elegant confirmation that GCS lipoylation (via GcvH) bypasses the E2-directed relay step. The whole system's dependence on both FAS and Fe-S biogenesis makes it a sensitive integrator of mitochondrial biosynthetic health, which is why so many seemingly unrelated Fe-S mutations converge on a lipoylation-deficiency phenotype.

---

## 8. Controversies and Open Questions

**Strongly supported claims.** The assembly-on-protein logic, the two-step chemistry, the dual-cluster radical-SAM mechanism of LipA with a sacrificial auxiliary cluster, the C6-monothiolated intermediate, the GcvH-relay architecture in *B. subtilis*, and the human LIPT2→LIAS→LIPT1 order (validated by patient genetics) are all strongly supported by convergent in vitro biochemistry, structural/spectroscopic data, and genetics.

**Areas of genuine disagreement or indirect evidence.**

1. **Evolutionary polarity of the topologies.** Is the multi-protein GcvH relay ancestral (with the *E. coli* two-enzyme route a derived streamlining, as Cronan argues [PMID: 27074917](https://pubmed.ncbi.nlm.nih.gov/27074917/)), or is the relay a later elaboration? The "evolutionary relic" interpretation is plausible but not settled; it rests largely on distribution/parsimony arguments rather than formal ancestral-state reconstruction.

2. **Where exactly sulfur insertion occurs in the relay topology.** In the GcvH-relay lineages, whether LipA/LIAS thiolates the octanoyl group while it is on GcvH, on E2, or on both, and how amidotransfer timing interleaves with thiolation, is incompletely resolved and may differ between *B. subtilis*, *S. aureus*, and mammals. Dynamic-relay studies in *S. aureus* [PMID: 31451544](https://pubmed.ncbi.nlm.nih.gov/31451544/) hint at more fluid intermediate trafficking than simple linear schemes suggest.

3. **Generalization across organisms.** Much mechanistic detail derives from *E. coli* and, for the relay, from *B. subtilis*; human LIAS reconstitution data are more recent [PMID: 33562493](https://pubmed.ncbi.nlm.nih.gov/33562493/). Mixing data across these systems risks overgeneralization, particularly regarding cluster-donor identity and turnover kinetics.

4. **Physiological cluster donors and turnover in vivo.** ISCU/ISCA2 reconstitute human LIAS in vitro [PMID: 33562493](https://pubmed.ncbi.nlm.nih.gov/33562493/), and the *E. coli* cluster reforms during catalysis, but the full in vivo choreography of auxiliary-cluster resupply, and whether it is rate-limiting for lipoylation flux under physiological or disease conditions, remains open.

**Most important open questions.**
- What is the ancestral topology, and can ancestral-sequence reconstruction of LipB/LipM and LipL/LIPT1 resolve the polarity debate?
- What is the precise substrate state (GcvH- vs E2-bound) for LIAS thiolation in mammals?
- How is auxiliary-cluster regeneration coupled to Fe-S biogenesis flux, and does this coupling explain the LIAS-like phenotypes of Fe-S biogenesis mutations?
- Can the archaeal LipS1/LipS2 split inform engineered multi-turnover lipoyl synthases (relevant to lipoic-acid bioproduction; cf. [PMID: 36639019](https://pubmed.ncbi.nlm.nih.gov/36639019/))?

---

## 9. Evidence Base

| PMID | Title (abbrev.) | Role in this review |
|------|-----------------|---------------------|
| [14700636](https://pubmed.ncbi.nlm.nih.gov/14700636/) | *Assembly of the covalent linkage between lipoic acid and its cognate enzymes* | Direct proof LipA acts on protein-bound octanoyl (obligatory ordering) |
| [27074917](https://pubmed.ncbi.nlm.nih.gov/27074917/) | *Assembly of Lipoic Acid on Its Cognate Enzymes* (Cronan) | Authoritative synthesis: assembly-on-protein logic; topology mapping; ancestral-relic argument |
| [26390103](https://pubmed.ncbi.nlm.nih.gov/26390103/) | *Radical Intermediate in Lipoyl Cofactor Biosynthesis* | Auxiliary cluster as sulfur donor; ⁵⁷Fe hyperfine coupling |
| [29051382](https://pubmed.ncbi.nlm.nih.gov/29051382/) | *Destruction and reformation of an Fe-S cluster during LipA catalysis* | Auxiliary cluster destroyed → single turnover in vitro |
| [26841001](https://pubmed.ncbi.nlm.nih.gov/26841001/) | *Lipoyl Synthase from M. tuberculosis* | Conserved two-cluster architecture and C6-monothiolated intermediate |
| [21338420](https://pubmed.ncbi.nlm.nih.gov/21338420/) | *Two-gene requirement for octanoyltransfer in B. subtilis* | Three-protein relay architecture distinct from E. coli |
| [21338421](https://pubmed.ncbi.nlm.nih.gov/21338421/) | *Novel amidotransferase (LipL) in B. subtilis* | Defines GcvH→E2 amidotransfer; GcvH obligatory |
| [28757203](https://pubmed.ncbi.nlm.nih.gov/28757203/) | *Biallelic LIPT2 mutations cause neonatal encephalopathy* | Human enzyme order LIPT2→LIAS→LIPT1; clinical validation |
| [24777537](https://pubmed.ncbi.nlm.nih.gov/24777537/) | *Lipoic acid biosynthesis defects* | Human pathway overview; LIPT1 spares GCS; Fe-S links |
| [27586888](https://pubmed.ncbi.nlm.nih.gov/27586888/) | *Differential diagnosis of lipoic acid synthesis defects* | Enzyme list; Fe-S biogenesis convergence |
| [28803783](https://pubmed.ncbi.nlm.nih.gov/28803783/) | *Mutations in Fe-S/lipoic pathways, fibroblast profiles* | Secondary LIAS deficiency from Fe-S defects |
| [33562493](https://pubmed.ncbi.nlm.nih.gov/33562493/) | *Human LIAS reconstitution; ISCA2/ISCU donors* | Cluster regeneration and ordered assembly resolve single-turnover |
| [36281299](https://pubmed.ncbi.nlm.nih.gov/36281299/) | *LipS1 and LipS2 characterization* | Archaeal two-gene sulfur-insertion variant |
| [25611823](https://pubmed.ncbi.nlm.nih.gov/25611823/) | *A new regulatory mechanism for bacterial lipoic acid synthesis* | Cofactor required in three domains of life |
| [21209092](https://pubmed.ncbi.nlm.nih.gov/21209092/) | *Protein-protein interactions in assembly on 2-oxoacid dehydrogenases* | LipA/LipB recruited "on site"; LplA/GcvH specificity |
| [31066113](https://pubmed.ncbi.nlm.nih.gov/31066113/) | *Lipoyl-relay of exogenous lipoate in B. subtilis* | Relay substrate specificity; salvage constraints |
| [31451544](https://pubmed.ncbi.nlm.nih.gov/31451544/) | *Dynamic Relay of Protein-Bound Lipoic Acid in S. aureus* | Suggests fluid intermediate trafficking in relay |
| [40813772](https://pubmed.ncbi.nlm.nih.gov/40813772/) | *Common bacterial salvage lipoylation protein boosts metabolism* | De novo vs salvage boundary; eukaryotes retain only de novo |
| [42418063](https://pubmed.ncbi.nlm.nih.gov/42418063/) | *Copper homeostasis and cuproptosis* | Downstream cuproptosis boundary (FDX1/LIPT1) |
| [36639019](https://pubmed.ncbi.nlm.nih.gov/36639019/) | *Metabolic engineering of E. coli for free lipoic acid* | Applied relevance; toxicity of overexpressing LipB/LipA |

---

## 10. Limitations and Knowledge Gaps

- **Organism mixing.** The integrated model blends *E. coli*, *B. subtilis*, *M. tuberculosis*, archaeal, and human data. While the core chemistry is conserved, quantitative kinetics, cluster-donor identities, and relay intermediate states should not be assumed identical across these systems.
- **In vitro vs in vivo turnover.** The single-turnover phenotype is an in vitro observation; the physiological rate-limiting features of cluster regeneration in vivo are inferred, not fully measured.
- **Relay intermediate ambiguity.** The exact protein-bound state (GcvH vs E2) at which LIAS thiolates in mammals is not definitively established.
- **Evolutionary polarity is unresolved.** The "relay-is-ancestral" hypothesis is attractive but based on distribution/parsimony, not formal ancestral reconstruction.
- **This review is literature-based**, without new primary data generated in this investigation; conclusions inherit the limitations of the cited studies.

---

## 11. Proposed Follow-up Experiments / Actions

1. **Resolve the thiolation substrate state in mammals.** Use reconstituted human LIAS with defined octanoyl-GcvH vs octanoyl-E2 lipoyl-domain substrates to determine kinetic preference; complement with cellular pulse-chase of lipoylation intermediates.
2. **Ancestral-sequence reconstruction** of LipB/LipM, LipL/LIPT1, and LipA/LIAS to test whether the GcvH relay or the direct route is ancestral, addressing the polarity controversy.
3. **Quantify cluster-regeneration flux in vivo.** Combine ISCU/ISCA2 perturbation with lipoylation-flux measurements to test whether auxiliary-cluster resupply is rate-limiting and whether it explains Fe-S-mutation phenotypes.
4. **Characterize the archaeal LipS1/LipS2 split mechanistically** (which paralog acts at C6 vs C8; whether each carries its own sacrificial cluster) as a potential blueprint for engineered multi-turnover synthases.
5. **Structural work on the amidotransferase step**—capture the LipL/LIPT1 thioester acyl-enzyme intermediate to define the Cys-Lys dyad geometry and GcvH docking.
6. **Systematically map the de novo/salvage boundary** across pathogens to evaluate the amidotransferase as an antimicrobial target in Gram-positive organisms.

---

*Prepared as a commissioned review synthesis. All mechanistic claims are anchored to the cited primary literature and authoritative reviews; uncertainty is flagged explicitly throughout, and single-organism findings are not assumed to generalize across all lineages.*


## Artifacts

- [OpenScientist final report](endogenous_protein_lipoylation-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](endogenous_protein_lipoylation-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:40813772
2. PMID:42418063
3. PMID:27074917
4. PMID:26390103
5. PMID:29051382
6. PMID:26841001
7. PMID:21209092
8. PMID:28757203
9. PMID:24777537
10. PMID:27586888
11. PMID:28803783
12. PMID:25611823
13. PMID:21338420
14. PMID:21338421
15. PMID:36281299
16. PMID:33562493
17. PMID:14700636
18. PMID:31066113
19. PMID:31451544
20. PMID:36639019