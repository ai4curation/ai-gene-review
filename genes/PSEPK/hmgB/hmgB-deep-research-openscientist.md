---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T12:57:56.450270'
end_time: '2026-07-23T13:20:44.457449'
duration_seconds: 1368.01
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: hmgB
  gene_symbol: hmgB
  uniprot_accession: Q88E48
  protein_description: 'RecName: Full=fumarylacetoacetase {ECO:0000256|ARBA:ARBA00012094};
    EC=3.7.1.2 {ECO:0000256|ARBA:ARBA00012094};'
  gene_info: Name=hmgB {ECO:0000313|EMBL:AAN70193.1}; OrderedLocusNames=PP_4620 {ECO:0000313|EMBL:AAN70193.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the hydratase/decarboxylase family.
  protein_domains: Fumarylacetoacetase. (IPR005959); Fumarylacetoacetase-like_C. (IPR011234);
    Fumarylacetoacetase_C_sf. (IPR036663); Fumarylacetoacetase_N. (IPR015377); Fumarylacetoacetase_N_sf.
    (IPR036462)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 6
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: hmgB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: hmgB-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88E48
- **Protein Description:** RecName: Full=fumarylacetoacetase {ECO:0000256|ARBA:ARBA00012094}; EC=3.7.1.2 {ECO:0000256|ARBA:ARBA00012094};
- **Gene Information:** Name=hmgB {ECO:0000313|EMBL:AAN70193.1}; OrderedLocusNames=PP_4620 {ECO:0000313|EMBL:AAN70193.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the hydratase/decarboxylase family.
- **Key Domains:** Fumarylacetoacetase. (IPR005959); Fumarylacetoacetase-like_C. (IPR011234); Fumarylacetoacetase_C_sf. (IPR036663); Fumarylacetoacetase_N. (IPR015377); Fumarylacetoacetase_N_sf. (IPR036462)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "hmgB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'hmgB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **hmgB** (gene ID: hmgB, UniProt: Q88E48) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *hmgB* (Q88E48 / PP_4620) in *Pseudomonas putida* KT2440

**Target gene:** *hmgB*
**UniProt accession:** Q88E48
**Ordered locus name:** PP_4620
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440) (PSEPK)
**EC number:** 3.7.1.2
**Protein family:** Fumarylacetoacetate hydrolase (FAH) / hydratase–decarboxylase superfamily

---

## Summary

The gene *hmgB* of *Pseudomonas putida* KT2440 (UniProt **Q88E48**, ordered locus **PP_4620**) encodes **fumarylacetoacetate hydrolase** (also called fumarylacetoacetase, **FAH; EC 3.7.1.2**). This enzyme catalyzes the **terminal, committed step of the homogentisate central catabolic pathway**: the hydrolytic cleavage of a carbon–carbon bond in **4-fumarylacetoacetate** to yield **fumarate** and **acetoacetate**. Both products feed directly into central carbon metabolism — fumarate enters the tricarboxylic acid (TCA) cycle, and acetoacetate is activated and consumed as an acetyl-CoA source — so HmgB is the metabolic node at which the carbon skeleton of aromatic substrates is finally delivered into the cell's core energy and biosynthetic economy. This identity is fully consistent with the UniProt annotation (fumarylacetoacetase, EC 3.7.1.2; hydratase/decarboxylase family; FAH N- and C-terminal domains IPR005959/IPR011234/IPR015377) and is directly supported by experimental characterization of the *P. putida* homogentisate pathway.

Mechanistically, HmgB belongs to the FAH superfamily of **metal-dependent carbon–carbon bond hydrolases** — a distinctive and comparatively rare enzyme chemistry. FAH-family structures define a novel α/β metalloenzyme fold in which a divalent cation (Ca²⁺ or Mg²⁺) is octahedrally coordinated in the active site adjacent to a **Glu–His catalytic dyad**. Catalysis proceeds through a **Glu–His–water catalytic triad** that activates a water molecule for nucleophilic attack, generating a **tetrahedral alkoxy transition-state intermediate** stabilized within an oxyanion hole. This mechanism, together with the defining HxxE / Hxx…xxE sequence motifs, is conserved across the whole FAH family, so HmgB's catalytic machinery can be inferred with high confidence from the well-resolved crystal structures of human and bacterial FAH orthologues, even though HmgB itself has not been crystallized.

In its physiological context, *hmgB* is part of the **hmgABC gene cluster** — a single transcriptional unit encoding homogentisate dioxygenase (HmgA), fumarylacetoacetate hydrolase (HmgB), and maleylacetoacetate isomerase (HmgC). This operon constitutes the **convergent central route** of aromatic catabolism in *P. putida*, funneling homogentisate derived from **L-phenylalanine, L-tyrosine, and 3-hydroxyphenylacetate** into fumarate and acetoacetate. Expression of *hmgABC* is controlled by the IclR-type transcriptional repressor **HmgR**, with **homogentisate** acting as the inducer molecule. The enzyme functions in the **cytoplasm** as a soluble, divalent-metal-dependent hydrolase. Importantly, this bacterial "hmgB" must **not** be confused with the unrelated eukaryotic **HMGB** high-mobility-group chromatin/DNA-binding proteins (HMGB1/2); the two share only a superficial symbol resemblance and have no functional, structural, or evolutionary relationship. The gene symbol, UniProt description, organism, and domain architecture all corroborate the assignment made here.

---

## Key Findings

### Finding 1 — HmgB is the fumarylacetoacetate hydrolase of the homogentisate central catabolic pathway

The core identity of the gene product is firmly established. In *P. putida*, the *hmgABC* genes encode three enzymes that together constitute the central (post-ring-cleavage) catabolic pathway for homogentisate: **homogentisate dioxygenase (HmgA)**, **fumarylacetoacetate hydrolase (HmgB)**, and **maleylacetoacetate isomerase (HmgC)**. HmgB catalyzes the last of these three steps, hydrolyzing fumarylacetoacetate to fumarate plus acetoacetate, corresponding to **EC 3.7.1.2**.

This assignment comes directly from the experimental characterization of the pathway by Arias-Barrau and colleagues, who state that "homogentisate is then catabolized by a central catabolic pathway that involves three enzymes, homogentisate dioxygenase (HmgA), fumarylacetoacetate hydrolase (HmgB), and maleylacetoacetate isomerase (HmgC), finally yielding fumarate and acetoacetate" ([PMID: 15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/)). This directly assigns to HmgB the function of fumarylacetoacetate hydrolase within the *P. putida* homogentisate pathway and identifies the reaction products. The UniProt annotation (fumarylacetoacetase; EC 3.7.1.2; hydratase/decarboxylase family; FAH N- and C-terminal InterPro domains IPR005959, IPR011234, IPR015377) is fully concordant with this experimentally grounded assignment.

### Finding 2 — HmgB catalyzes hydrolytic C–C bond cleavage of fumarylacetoacetate to fumarate + acetoacetate

The reaction catalyzed is chemically distinctive. Fumarylacetoacetate hydrolase performs the **hydrolytic cleavage of a carbon–carbon bond** — a rare enzymatic reaction. In the canonical (mammalian) tyrosine/phenylalanine degradation context, this is "the final step of tyrosine and phenylalanine catabolism, the hydrolytic cleavage of a carbon-carbon bond in fumarylacetoacetate, to yield fumarate and acetoacetate" ([PMID: 10508789](https://pubmed.ncbi.nlm.nih.gov/10508789/)). The same chemistry applies to the bacterial enzyme HmgB.

What makes the FAH family notable is that it "represents the first structure of a hydrolase that acts specifically on carbon-carbon bonds" ([PMID: 10508789](https://pubmed.ncbi.nlm.nih.gov/10508789/)). Most hydrolases cleave C–N, C–O, or C–S bonds (peptidases, esterases, glycosidases); enzymes that hydrolyze C–C bonds are uncommon, and FAH defines a class specialized for this task. Structural studies of the product complex show **fumarate binding near the active-site entrance** and **acetoacetate binding to an octahedrally coordinated metal ion**, delineating the two-product architecture of the reaction. Substrate specificity in the FAH superfamily is driven by the electrophilic β-keto/oxo carbon adjacent to the scissile bond, with the divalent metal ion polarizing the carbonyl and positioning the substrate for nucleophilic water attack. The physiological substrate of HmgB, 4-fumarylacetoacetate, is a β-diketo acid produced by the immediately upstream isomerase HmgC.

### Finding 3 — HmgB employs a metal-dependent Glu–His–water catalytic triad, oxyanion hole, and tetrahedral intermediate

The catalytic machinery of the FAH fold is well characterized structurally, and these features are conserved across the family to which HmgB belongs. FAH-family active sites contain a **divalent metal ion** (Ca²⁺ or Mg²⁺) that is **octahedrally coordinated** and positioned next to a **Glu–His catalytic dyad**. Catalysis proceeds via a **Glu–His–water catalytic triad**: the glutamate orients and deprotonates the histidine, which in turn acts as a general base to activate the metal-bound water molecule for nucleophilic attack on the electrophilic carbon of the substrate. The original FAH structure describes "acetoacetate binding to an octahedrally coordinated calcium ion located in close proximity to a Glu-His dyad… FAH also defines a new class of metalloenzymes characterized by a unique alpha/beta fold. A mechanism involving a Glu-His-water catalytic triad is suggested" ([PMID: 10508789](https://pubmed.ncbi.nlm.nih.gov/10508789/)).

Inhibitor-complex studies further validate the mechanism. A phosphorus-based transition-state mimic bound to FAH "reveals a Mg(2+) bound in the enzyme's active site, [and] supports the proposed formation of a tetrahedral alkoxy transition state intermediate during the FAH catalyzed reaction" ([PMID: 11154690](https://pubmed.ncbi.nlm.nih.gov/11154690/)). This confirms both the Mg²⁺ cofactor and the tetrahedral geometry of the reaction's high-energy intermediate, which is stabilized by a charged oxyanion hole. Slow-onset, tight-binding phosphinate mimics of the tetrahedral intermediate (CEHPOBA and COPHPAA) inhibit FAH with nanomolar potency (K_i = 41 nM and 12 nM, respectively), providing kinetic and structural evidence that the reaction passes through a tetrahedral intermediate resembling these compounds ([PMID: 17064256](https://pubmed.ncbi.nlm.nih.gov/17064256/)).

Crucially, the generality of this mechanism to the entire FAH family — and therefore to HmgB — was established by structural studies of Cg1458, which showed that "this catalytic triad is common among FAH family proteins that catalyse the cleavage of the C-C bond of the substrate. Two sequence motifs, HxxE and Hxx…xxE have been identified as the basis for this mechanism" ([PMID: 23046410](https://pubmed.ncbi.nlm.nih.gov/23046410/)). Because HmgB carries the FAH fold and these defining motifs, its catalytic triad and metal-dependent mechanism can be inferred with high confidence.

### Finding 4 — HmgB operates in a convergent central pathway (Phe / Tyr / 3-HPA), encoded by the HmgR-repressed hmgABC operon

*hmgB* does not act in isolation; it is embedded in a well-defined regulatory and metabolic architecture. The *hmgABC* genes "appear to form a single transcriptional unit," and regulation is exerted by an adjacent, divergently transcribed regulator: "gel retardation assays and lacZ translational fusion experiments have shown that hmgR encodes a specific repressor that controls the inducible expression of the divergently transcribed hmgABC catabolic genes, and homogentisate is the inducer molecule" ([PMID: 15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/)). HmgR is an **IclR-type transcriptional repressor** that binds a palindromic operator in the *Phmg* promoter region; **homogentisate**, the pathway's entry metabolite, relieves this repression and induces expression of the catabolic genes, including *hmgB*. This substrate-driven induction ensures that HmgB is produced only when its pathway substrate is available.

The pathway's role is that of a **convergent central (or "lower") route**. Multiple upstream peripheral pathways generate homogentisate, which is then processed by the shared HmgABC enzymes. As shown in studies of 3-hydroxyphenylacetate assimilation, HmgABC constitutes "a central route (convergent route), which catalyzes the transformation of the Hmg generated from 3-OH-PhAc, l-Phe, and l-Tyr into fumarate and acetoacetate (HmgABC)" ([PMID: 15866873](https://pubmed.ncbi.nlm.nih.gov/15866873/)). Thus HmgB is the final funnel through which the carbon of at least three aromatic substrates — L-phenylalanine, L-tyrosine, and 3-hydroxyphenylacetate — is delivered into central metabolism. Homogentisate uptake and pathway operation are also supported by an associated ABC-transporter system (HmgDEFGHI) in *P. putida*. Physiologically, this enables the organism to use aromatic amino acids and aromatic acids as carbon and energy sources.

---

## Mechanistic Model / Interpretation

### Position of HmgB in aromatic catabolism

HmgB catalyzes the last of three reactions in the homogentisate central pathway. The overall flow of carbon can be summarized as follows:

```
 Peripheral (upstream) routes                Central (convergent) route: hmgABC
 ────────────────────────────                ───────────────────────────────────

 L-Phenylalanine ─► L-Tyrosine ─┐
                                 │
 3-Hydroxyphenylacetate ────────┼──►  HOMOGENTISATE
                                        │
                                        │  HmgA (homogentisate 1,2-dioxygenase)
                                        │     ring cleavage, + O2
                                        ▼
                                   Maleylacetoacetate
                                        │
                                        │  HmgC (maleylacetoacetate isomerase)
                                        │     cis→trans isomerization (GSH-dependent)
                                        ▼
                                   Fumarylacetoacetate
                                        │
                                        │  ►► HmgB (fumarylacetoacetate hydrolase, EC 3.7.1.2) ◄◄
                                        │     hydrolytic C–C bond cleavage + H2O
                                        ▼
                        ┌───────────────┴───────────────┐
                        ▼                                ▼
                    FUMARATE                        ACETOACETATE
                 (→ TCA cycle)              (→ acetoacetyl-CoA → 2 acetyl-CoA)
```

HmgB sits at the exit of the aromatic-degradation funnel. By splitting fumarylacetoacetate into two central metabolites, it converts an aromatic ring–derived carbon skeleton into TCA-cycle and acetyl-CoA precursors, completing the assimilation of aromatic carbon.

### Catalytic mechanism (inferred from FAH-family structures)

```
        Glu ──(H-bond)── His ──(general base)──► activates H2O
                                                    │
                                                    ▼ nucleophilic attack
   Fumarylacetoacetate  ──►  [ tetrahedral alkoxy intermediate ]  ──►  Fumarate + Acetoacetate
        (C–C scissile bond)         stabilized by oxyanion hole
                    │
             Mg2+/Ca2+ (octahedral) polarizes carbonyl, orients substrate
```

The divalent metal ion (Mg²⁺ or Ca²⁺) is octahedrally coordinated by conserved carboxylate residues and a water molecule, and it electrostatically polarizes the substrate's carbonyl group. The His of the Glu–His dyad deprotonates the metal-bound water, generating a hydroxide nucleophile that attacks the electrophilic carbon adjacent to the scissile C–C bond, producing a **tetrahedral alkoxy intermediate**. Collapse of this intermediate cleaves the C–C bond, releasing fumarate and acetoacetate. This model is supported directly by product-complex, Mg²⁺-complex, and transition-state-mimic inhibitor structures across the FAH family.

### Comparison across the FAH superfamily

The FAH fold is a versatile scaffold reused by evolution for diverse metal-dependent reactions on β-keto/oxo-acid substrates. This context supports the confidence of the HmgB annotation:

| Enzyme (organism) | Reaction / EC | Metal | Catalytic role | PMID |
|---|---|---|---|---|
| **HmgB / FAH (P. putida, human)** | Fumarylacetoacetate → fumarate + acetoacetate (EC 3.7.1.2) | Ca²⁺/Mg²⁺ | C–C bond hydrolase | [10508789](https://pubmed.ncbi.nlm.nih.gov/10508789/), [15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/) |
| KdaD (S. solfataricus) | 2-keto-3-deoxy-D-arabinonate dehydratase | Mg²⁺/Ca²⁺ | Base-catalyzed dehydration | [18448118](https://pubmed.ncbi.nlm.nih.gov/18448118/) |
| LRA6 (bacteria) | 2,4-diketo-3-deoxy-L-rhamnonate → pyruvate + L-lactate | divalent | C–C bond hydrolase | [36563174](https://pubmed.ncbi.nlm.nih.gov/36563174/) |
| Cg1458 (Corynebacterium) | FAH-family hydrolase | divalent | Glu–His–water triad; HxxE / Hxx…xxE motifs | [23046410](https://pubmed.ncbi.nlm.nih.gov/23046410/) |

The shared fold, shared metal dependence, and shared Glu–His–water triad across these enzymes provide strong evolutionary and structural corroboration for HmgB's assigned reaction and mechanism.

### Localization

HmgB is a **soluble cytoplasmic enzyme**. There is no signal peptide or membrane-spanning region implied by the FAH fold, and its substrate (fumarylacetoacetate) is an intracellular intermediate produced by the upstream cytoplasmic enzymes HmgA and HmgC. FAH-family members are routinely purified as soluble cytosolic proteins for crystallography. The enzyme therefore carries out its function in the **cytoplasm**, where the entire homogentisate central pathway operates and where its products enter central metabolism.

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the findings |
|---|---|---|
| [15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/) | *The homogentisate pathway… in Pseudomonas putida* | **Primary, organism-specific.** Directly names HmgB as fumarylacetoacetate hydrolase; establishes products (fumarate + acetoacetate), operon structure (single transcriptional unit), and HmgR/homogentisate regulation. Anchors Findings 1 and 4. |
| [15866873](https://pubmed.ncbi.nlm.nih.gov/15866873/) | *A two-component hydroxylase… 3-hydroxyphenyl acetate in P. putida* | Establishes HmgABC as the convergent central route converting homogentisate from 3-OH-PhAc, L-Phe, and L-Tyr into fumarate + acetoacetate. Supports Finding 4 (pathway convergence). |
| [10508789](https://pubmed.ncbi.nlm.nih.gov/10508789/) | *Crystal structure and mechanism of a carbon-carbon bond hydrolase* | **Foundational mechanism paper.** Defines the exact reaction, the C–C bond hydrolase chemistry, the novel α/β metalloenzyme fold, the octahedral metal + Glu–His dyad, and the Glu–His–water triad. Supports Findings 2 and 3. |
| [11154690](https://pubmed.ncbi.nlm.nih.gov/11154690/) | *…FAH with a bound phosphorus-based inhibitor* | Confirms Mg²⁺ cofactor and the tetrahedral alkoxy transition-state intermediate. Supports Finding 3. *(Study of orthologous FAH, applied to HmgB by family inference.)* |
| [17064256](https://pubmed.ncbi.nlm.nih.gov/17064256/) | *Slow-onset inhibition of FAH by phosphinate mimics…* | Nanomolar transition-state-mimic inhibitors (K_i = 12–41 nM) provide kinetic + structural evidence for the tetrahedral intermediate. Corroborates Finding 3. |
| [23046410](https://pubmed.ncbi.nlm.nih.gov/23046410/) | *Crystal structures of Cg1458… common catalytic mechanism for the FAH family* | Generalizes the Glu–His–water triad and defining HxxE / Hxx…xxE motifs to the whole FAH family, licensing inference to HmgB. Supports Finding 3. |
| [18448118](https://pubmed.ncbi.nlm.nih.gov/18448118/) | *Novel 2-keto-3-deoxy-D-arabinonate dehydratase… FAH superfamily* | Comparative structural context; shows the shared FAH fold and octahedral metal coordination across the superfamily. Supports the mechanistic model. |
| [36563174](https://pubmed.ncbi.nlm.nih.gov/36563174/) | *Crystal structure of L-2,4-diketo-3-deoxyrhamnonate hydrolase…* | Another FAH-superfamily C–C bond hydrolase; reinforces the family's metal-dependent hydrolase chemistry. Supports the mechanistic model. |

**Evidence strength.** The organism-specific functional and regulatory claims (Findings 1 and 4) rest on direct experimental characterization in *P. putida* ([PMID: 15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/), [PMID: 15866873](https://pubmed.ncbi.nlm.nih.gov/15866873/)). The detailed catalytic mechanism (Finding 3) is derived from high-resolution crystal structures of orthologous/homologous FAH-family enzymes rather than from HmgB itself; because HmgB carries the diagnostic FAH fold and sequence motifs, this inference is well justified but is structural/evolutionary rather than direct.

---

## Supported and Refuted Hypotheses

| Hypothesis | Status | Basis |
|---|---|---|
| hmgB = fumarylacetoacetate hydrolase (EC 3.7.1.2) | **Supported** | Experimental operon characterization ([PMID: 15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/)); UniProt family/domains |
| Reaction = hydrolytic C–C cleavage of fumarylacetoacetate → fumarate + acetoacetate | **Supported** | FAH structural/biochemical studies ([PMID: 10508789](https://pubmed.ncbi.nlm.nih.gov/10508789/)) |
| Mechanism = metal-dependent Glu–His–water triad, oxyanion hole, tetrahedral intermediate | **Supported (by homology)** | [PMID: 10508789](https://pubmed.ncbi.nlm.nih.gov/10508789/), [11154690](https://pubmed.ncbi.nlm.nih.gov/11154690/), [23046410](https://pubmed.ncbi.nlm.nih.gov/23046410/) |
| Terminal step of homogentisate pathway converging Phe/Tyr/3-OH-PhAc catabolism | **Supported** | [PMID: 15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/), [15866873](https://pubmed.ncbi.nlm.nih.gov/15866873/) |
| Cytoplasmic localization | **Supported (inference)** | Soluble FAH-family enzymes; intracellular substrate/products |
| hmgB = eukaryotic HMGB chromatin protein | **Refuted** | Different family, EC, organism; no relationship |

---

## Limitations and Knowledge Gaps

1. **No direct structural or enzymological study of HmgB itself.** The catalytic residues, metal identity (Ca²⁺ vs Mg²⁺), kinetic parameters (k_cat, K_m), and substrate specificity of the *P. putida* PP_4620 protein have not been experimentally determined. All mechanistic detail is transferred from human FAH and other FAH-family enzymes by homology. A crystal structure or biochemical assay of purified HmgB would confirm the specifics.

2. **Substrate specificity boundaries are inferred.** While HmgB is assigned fumarylacetoacetate as its physiological substrate, the FAH superfamily is functionally diverse (dehydratases, other C–C hydrolases). Direct assay would be needed to rule out promiscuous activities and to establish quantitative substrate preference.

3. **Metal cofactor identity in vivo.** Structural studies variously report Ca²⁺ or Mg²⁺ in FAH active sites. The physiologically relevant metal for HmgB in *P. putida* is not established.

4. **Regulatory fine structure.** Although HmgR-mediated repression and homogentisate induction are established, the precise operator architecture, affinity constants, and any additional layers of regulation (e.g., global carbon regulation, cross-talk with peripheral pathway regulators) for PP_4620 specifically remain incompletely mapped.

5. **Localization is inferred, not measured.** Cytoplasmic localization is deduced from the fold (no signal peptide/TM region) and the intracellular nature of the substrate, but has not been experimentally verified for HmgB by fractionation or imaging.

6. **Strain provenance of primary data.** Much of the genetic/biochemical characterization was performed in *P. putida* systems that are orthologous and identically annotated to KT2440 PP_4620, but strain-specific confirmation (e.g., a PP_4620 knockout growth phenotype on tyrosine) would be ideal.

7. **Quantitative flux contribution and knockout phenotype.** The relative contribution of HmgB flux to overall aromatic-carbon assimilation, and phenotypes of an *hmgB* knockout (e.g., accumulation of the potentially cytotoxic intermediate fumarylacetoacetate, analogous to hereditary tyrosinaemia type 1 in humans), have not been characterized here.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and enzymatic assay.** Clone and express PP_4620, purify the protein, and measure fumarylacetoacetate hydrolase activity (k_cat, K_m) with fumarylacetoacetate. Include the transition-state-mimic inhibitors CEHPOBA/COPHPAA as active-site probes to confirm mechanism.

2. **Metal-dependence assay.** Test activity as a function of divalent cations (Ca²⁺, Mg²⁺, Mn²⁺, chelators such as EDTA) to establish the physiological cofactor.

3. **Structural determination.** Solve the crystal structure (or an AlphaFold model validated against family structures) of HmgB, ideally with a bound product or transition-state mimic, to directly confirm the Glu–His–water triad, octahedral metal site, and oxyanion hole; compare against human FAH ([PMID: 10508789](https://pubmed.ncbi.nlm.nih.gov/10508789/)) and Cg1458 ([PMID: 23046410](https://pubmed.ncbi.nlm.nih.gov/23046410/)).

4. **Active-site residue mapping.** Map the conserved HxxE / Hxx…xxE motifs onto the Q88E48 sequence to pinpoint the specific Glu/His of the catalytic triad; validate by site-directed mutagenesis.

5. **Gene knockout / complementation.** Construct a Δ*hmgB* mutant in *P. putida* KT2440 and assess growth on L-Phe, L-Tyr, and 3-hydroxyphenylacetate as sole carbon sources; test for accumulation of fumarylacetoacetate/maleylacetoacetate and any associated toxicity, with complementation to confirm causality.

6. **Regulatory validation.** Map the HmgR operator and confirm homogentisate induction of *hmgB* using reporter fusions and electrophoretic mobility shift assays; quantify induction kinetics.

7. **Localization confirmation.** Fractionate *P. putida* lysates or use a fluorescent fusion to confirm cytoplasmic localization of HmgB.

8. **Comparative genomics.** Confirm operon synteny (*hmgABC*, *hmgR*, and the associated HmgDEFGHI transporter) across *Pseudomonas* species to strengthen the pathway model and detect any strain-specific variation.

---

## Conclusion

The gene symbol *hmgB* is unambiguously correct for this target: it matches the UniProt description (fumarylacetoacetase, EC 3.7.1.2), the organism (*P. putida* KT2440), and the FAH-fold domain architecture, and the primary literature on the *P. putida* homogentisate pathway describes precisely this protein. **HmgB (Q88E48 / PP_4620) is fumarylacetoacetate hydrolase**, a soluble cytoplasmic, divalent-metal-dependent enzyme that catalyzes the hydrolytic cleavage of a carbon–carbon bond in fumarylacetoacetate to yield fumarate and acetoacetate. It performs the terminal, committed step of the homogentisate central catabolic pathway (HmgABC) — the convergent route by which *P. putida* degrades L-phenylalanine, L-tyrosine, and 3-hydroxyphenylacetate — channeling aromatic carbon into central metabolism. Its catalytic mechanism (FAH-fold metalloenzyme, Glu–His–water triad, tetrahedral intermediate, oxyanion hole) is confidently inferred from well-characterized FAH-family structures, and its expression is controlled by the IclR-type repressor HmgR with homogentisate as inducer.


## Artifacts

- [OpenScientist final report](hmgB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](hmgB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:15262943
2. PMID:10508789
3. PMID:11154690
4. PMID:17064256
5. PMID:23046410
6. PMID:15866873