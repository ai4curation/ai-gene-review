---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T18:51:53.332659'
end_time: '2026-07-20T19:54:06.771988'
duration_seconds: 3733.44
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pqqC
  gene_symbol: pqqC
  uniprot_accession: Q88QV6
  protein_description: 'RecName: Full=Pyrroloquinoline-quinone synthase {ECO:0000255|HAMAP-Rule:MF_00654};
    EC=1.3.3.11 {ECO:0000255|HAMAP-Rule:MF_00654}; AltName: Full=Coenzyme PQQ synthesis
    protein C {ECO:0000255|HAMAP-Rule:MF_00654}; AltName: Full=Pyrroloquinoline quinone
    biosynthesis protein C {ECO:0000255|HAMAP-Rule:MF_00654};'
  gene_info: Name=pqqC {ECO:0000255|HAMAP-Rule:MF_00654}; OrderedLocusNames=PP_0378;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the PqqC family. {ECO:0000255|HAMAP-
  protein_domains: Haem_Oase-like_multi-hlx. (IPR016084); PqqC. (IPR011845); PqqC-like.
    (IPR039068); Thiaminase-2/PQQC. (IPR004305); TENA_THI-4 (PF03070)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 2
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pqqC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pqqC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QV6
- **Protein Description:** RecName: Full=Pyrroloquinoline-quinone synthase {ECO:0000255|HAMAP-Rule:MF_00654}; EC=1.3.3.11 {ECO:0000255|HAMAP-Rule:MF_00654}; AltName: Full=Coenzyme PQQ synthesis protein C {ECO:0000255|HAMAP-Rule:MF_00654}; AltName: Full=Pyrroloquinoline quinone biosynthesis protein C {ECO:0000255|HAMAP-Rule:MF_00654};
- **Gene Information:** Name=pqqC {ECO:0000255|HAMAP-Rule:MF_00654}; OrderedLocusNames=PP_0378;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the PqqC family. {ECO:0000255|HAMAP-
- **Key Domains:** Haem_Oase-like_multi-hlx. (IPR016084); PqqC. (IPR011845); PqqC-like. (IPR039068); Thiaminase-2/PQQC. (IPR004305); TENA_THI-4 (PF03070)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pqqC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pqqC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pqqC** (gene ID: pqqC, UniProt: Q88QV6) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *pqqC* (Q88QV6) — Pyrroloquinoline-Quinone Synthase in *Pseudomonas putida* KT2440

**Gene:** *pqqC* (Ordered locus PP_0378) · **UniProt:** Q88QV6 · **Organism:** *Pseudomonas putida* strain ATCC 47054 / DSM 6125 / KT2440 (PSEPK) · **EC:** 1.3.3.11
**Family / domains:** PqqC family; Haem-oxygenase-like multi-helical fold (IPR016084); PqqC (IPR011845); PqqC-like (IPR039068); Thiaminase-2/PQQC, TENA_THI-4 (PF03070)

---

## Summary

**PqqC (UniProt Q88QV6; ordered locus PP_0378) is pyrroloquinoline-quinone synthase (EC 1.3.3.11), the terminal enzyme of pyrroloquinoline quinone (PQQ) biosynthesis in *Pseudomonas putida* KT2440.** Its primary and defining catalytic function is to convert the biosynthetic intermediate 3a-(2-amino-2-carboxyethyl)-4,5-dioxo-4,5,6,7,8,9-hexahydroquinoline-7,9-dicarboxylic acid (abbreviated **AHQQ**) into the mature redox cofactor **PQQ**. This single enzymatic step combines an intramolecular **ring cyclization** with an **eight-electron, eight-proton oxidation**, and it is the last of five reactions that build PQQ from the glutamate and tyrosine residues embedded in the ribosomally synthesized precursor peptide PqqA ([PMID: 15148379](https://pubmed.ncbi.nlm.nih.gov/15148379/); [PMID: 18371220](https://pubmed.ncbi.nlm.nih.gov/18371220/); [PMID: 31427437](https://pubmed.ncbi.nlm.nih.gov/31427437/)).

Mechanistically, PqqC is remarkable because it is a **cofactor-less, metal-free oxidase**. Unlike the overwhelming majority of oxidases and oxygenases, it carries no flavin, no metal ion, and no other redox-active organic cofactor. Instead it transfers redox equivalents directly to molecular oxygen (O₂), releasing hydrogen peroxide (H₂O₂) as a co-product. Structurally, PqqC is a compact, soluble **seven-helix bundle** belonging to the heme-oxygenase-like all-α fold; it scaffolds a strongly positively charged active-site cavity that closes over the substrate through a large induced-fit conformational change ([PMID: 15148379](https://pubmed.ncbi.nlm.nih.gov/15148379/)).

Physiologically, PqqC does not act on any central-metabolic substrate itself; rather, its **sole product, PQQ, is the essential cofactor of periplasmic quinoprotein dehydrogenases.** In *P. putida* the most prominent client is PQQ-dependent glucose dehydrogenase (Gcd), which oxidizes glucose to gluconate in the periplasm as the oxidative branch of glucose catabolism. PqqC is therefore a **cytoplasmic biosynthetic enzyme whose output is exported to the periplasm** to enable extracytoplasmic redox chemistry — coupling cofactor biosynthesis inside the cell to nutrient oxidation outside the inner membrane ([PMID: 23392768](https://pubmed.ncbi.nlm.nih.gov/23392768/); [PMID: 7540821](https://pubmed.ncbi.nlm.nih.gov/7540821/); [PMID: 18371220](https://pubmed.ncbi.nlm.nih.gov/18371220/)).

**Identity is unambiguous.** The gene symbol *pqqC*, the protein description (pyrroloquinoline-quinone synthase / coenzyme PQQ synthesis protein C), EC 1.3.3.11, the PqqC family, and the domain complement (IPR016084; IPR011845/IPR039068; PF03070) are all fully consistent with the primary literature reviewed here — a definitive crystallographic study and two independent structural/mechanistic reviews all describe PqqC as the terminal PQQ-biosynthesis catalyst. This is a correctly identified gene. (Note: many recent PubMed hits use *pqqC* merely as a **soil-metagenomic marker gene** for phosphate-mobilizing bacteria; those studies concern ecology, not enzyme mechanism, and are peripheral to this annotation.)

---

## Key Findings

### Finding 1 — PqqC catalyzes the final step of PQQ biosynthesis: ring cyclization plus eight-electron oxidation of AHQQ to PQQ (EC 1.3.3.11)

The defining function of PqqC was established biochemically and structurally by Magnusson and colleagues, who crystallized both the apo-enzyme and its complex with the product PQQ and determined the stoichiometry of oxygen consumption and peroxide production ([PMID: 15148379](https://pubmed.ncbi.nlm.nih.gov/15148379/)). They report explicitly that "**PqqC, the protein encoded by pqqC, catalyzes the final step in the pathway in a reaction that involves ring cyclization and eight-electron oxidation of 3a-(2-amino-2-carboxyethyl)-4,5-dioxo-4,5,6,7,8,9-hexahydroquinoline-7,9-dicarboxylic-acid to PQQ.**" This single statement identifies the substrate (AHQQ), the product (PQQ), and the chemical transformation (intramolecular cyclization combined with an eight-electron oxidation). The overall reaction can be written:

> **AHQQ + O₂ → PQQ + H₂O₂** (net: ring closure + eight-electron/eight-proton oxidation)

This assignment is independently corroborated by two review-level sources. Puehringer, Metlitzky and Schwarzenbacher, in their structural reappraisal of the PQQ pathway, state directly that "**the last cyclization and oxidation steps are catalysed by PqqC**" ([PMID: 18371220](https://pubmed.ncbi.nlm.nih.gov/18371220/)). Independently, Martins and colleagues, describing the pathway from the perspective of the PqqA-derived RiPP framework, characterize PqqC as an "**eight-electron, eight-proton oxidase**" that completes the pathway alongside the radical-SAM enzyme PqqE, the peptide chaperone PqqD, and the dual hydroxylase PqqB ([PMID: 31427437](https://pubmed.ncbi.nlm.nih.gov/31427437/)). The convergence of a crystallographic primary study and two independent reviews on the same reaction assignment makes this the most secure conclusion of the report. The EC classification 1.3.3.11 (an oxidoreductase acting on the CH–CH group of donors with O₂ as acceptor) is fully consistent with this O₂-dependent oxidative ring-closure chemistry.

The substrate specificity is narrow: PqqC acts on the single dedicated pathway intermediate **AHQQ**, and its product is the tricyclic *ortho*-quinone cofactor **PQQ**. There is no evidence of promiscuous activity on other cellular metabolites.

### Finding 2 — PqqC is a cofactor-less, metal-free oxidase that uses molecular O₂ and produces H₂O₂

PqqC belongs to a small and mechanistically fascinating group of enzymes that perform multi-electron oxidations **without any redox-active cofactor.** Magnusson et al. determined the stoichiometry of H₂O₂ formation and O₂ uptake and concluded that "**PqqC is unusual in that it transfers redox equivalents to molecular oxygen without the assistance of a redox active metal or cofactor**" ([PMID: 15148379](https://pubmed.ncbi.nlm.nih.gov/15148379/)). This is striking: an eight-electron oxidation of an organic substrate is normally the province of flavin- or metal-dependent enzymes, yet PqqC accomplishes it using only protein side chains and the intrinsic redox chemistry of its quinonoid substrate.

The same study proposed a mechanistic sequence to explain how this is possible: "**We propose a reaction sequence that involves base-catalyzed cyclization and a series of quinone-quinol tautomerizations that are followed by cycles of O₂/H₂O₂-mediated oxidations.**" In this model an active-site base first catalyzes the intramolecular cyclization that closes the pyrrole ring; the substrate then cycles through quinone/quinol tautomeric states, each of which can be re-oxidized by molecular oxygen, with H₂O₂ released at each oxidation cycle. Extra electron density observed adjacent to **Arg179** and to the **C5 position of PQQ** in the crystal structure was modeled as bound O₂/H₂O₂, defining a discrete oxygen-binding subsite within the active pocket. In effect, the substrate itself serves as the transient "cofactor," its quinone/quinol chemistry providing the redox machinery that flavins or metals supply in other enzymes.

The stoichiometric production of H₂O₂ is a mechanistic signature of this class of chemistry, and it has physiological implications: PqqC activity generates a reactive oxygen species coupled to PQQ synthesis, which the cell must manage.

### Finding 3 — PqqC is a soluble seven-helix-bundle protein with a positively charged active site that closes on substrate/product

The crystal structures of PqqC and the PqqC–PQQ complex reveal the enzyme's architecture ([PMID: 15148379](https://pubmed.ncbi.nlm.nih.gov/15148379/)). The authors report that "**the PqqC structure(s) reveals a compact seven-helix bundle that provides the scaffold for a positively charged active site cavity. Product binding induces a large conformational change, which results in the active site recruitment of amino acid side chains proposed to play key roles in the catalytic mechanism.**"

Three features are worth emphasizing. First, the **all-α seven-helix bundle** places PqqC in the heme-oxygenase-like fold superfamily — consistent with the InterPro/Pfam domain annotations for Q88QV6 (Haem_Oase-like multi-hlx IPR016084; PqqC IPR011845/IPR039068; Thiaminase-2/PQQC family, Pfam PF03070 TENA_THI-4). Notably, PqqC adopts a heme-oxygenase-*like* scaffold but binds **no heme and no metal**, reinforcing Finding 2. Second, the **positively charged active-site cavity** is well suited to bind the multiply carboxylated, anionic substrate AHQQ and product PQQ, both of which carry several carboxylate groups. Third, the **induced-fit closure** upon ligand binding — a large conformational change that recruits catalytic residues such as Arg179 into the active site — indicates that catalysis proceeds within a sequestered, solvent-shielded pocket. This sequestration is important both for orienting the substrate for cyclization and for containing the reactive quinonoid/oxygen intermediates during the multistep oxidation.

The absence of a signal peptide or membrane-spanning segment, together with the compact soluble fold, is consistent with PqqC functioning as a **soluble cytoplasmic enzyme.** This localization is mechanistically appropriate: PQQ biosynthesis assembles the cofactor in the cytoplasm from the ribosomal PqqA peptide, after which the mature cofactor is exported to the periplasm where its client dehydrogenases reside (Finding 4).

### Finding 4 — PqqC's product PQQ is the cofactor of periplasmic quinoprotein glucose dehydrogenase, driving glucose→gluconate oxidation

PqqC has no standalone physiological role apart from producing PQQ; its biological significance is entirely mediated by the downstream use of that cofactor. In *P. putida* and other fluorescent pseudomonads, glucose is catabolized by **two parallel routes**: a periplasmic oxidative pathway and a cytoplasmic phosphorylative pathway. Ponraj and colleagues state that "**fluorescent pseudomonads catabolize glucose simultaneously by two different pathways, namely, the oxidative pathway in periplasm and the phosphorylative pathway in cytoplasm**" ([PMID: 23392768](https://pubmed.ncbi.nlm.nih.gov/23392768/)). The periplasmic oxidative branch depends on **PQQ-dependent quinoprotein glucose dehydrogenase (Gcd)**, and disruption of *gcd* or of PQQ biosynthesis (e.g., *pqqF*) impairs periplasmic gluconic acid production — directly linking PQQ availability to this physiology.

The mechanistic role of PQQ as the glucose dehydrogenase cofactor is well documented across gram-negative bacteria. Babu-Khan et al., studying mineral phosphate solubilization, describe "**periplasmic oxidation of glucose to gluconic acid via the quinoprotein glucose dehydrogenase (GDH)**" ([PMID: 7540821](https://pubmed.ncbi.nlm.nih.gov/7540821/)). Apo-GDH is catalytically inert; it becomes an active holo-enzyme only upon binding PQQ. The gluconic acid produced by this periplasmic oxidation acidifies the extracellular environment and, in soil bacteria, solubilizes mineral phosphate — which is precisely why *pqqC* is widely used as a functional marker gene for phosphorus-mobilizing bacteria in soil-ecology studies ([PMID: 37528183](https://pubmed.ncbi.nlm.nih.gov/37528183/); [PMID: 41274639](https://pubmed.ncbi.nlm.nih.gov/41274639/)). Importantly, that ecological marker role reflects the **downstream** action of PqqC's product, not a direct catalytic role of PqqC in phosphate mobilization.

Puehringer et al. summarize the general downstream role, noting that PQQ is "**a bacterial redox active cofactor for numerous alcohol and aldose dehydrogenases**" ([PMID: 18371220](https://pubmed.ncbi.nlm.nih.gov/18371220/)). Thus PqqC sits at the head of a supply chain: cytoplasmic PQQ synthesis → periplasmic export → holo-enzyme assembly of Gcd (and other quinoproteins) → periplasmic substrate oxidation.

### Finding 5 — PqqC performs the final cyclization/oxidation in a five-reaction pathway that builds PQQ from the Glu and Tyr of PqqA

PqqC is the last enzyme in an operon-encoded biosynthetic route. The structural review by Puehringer, Metlitzky and Schwarzenbacher establishes the RiPP origin of the cofactor: "**PQQ is derived from the two amino acids glutamate and tyrosine encoded in the precursor peptide PqqA**" ([PMID: 18371220](https://pubmed.ncbi.nlm.nih.gov/18371220/)). Five enzymatic reactions convert these two amino acids into the tricyclic *o*-quinone cofactor, and, as quoted above, "**the last cyclization and oxidation steps are catalysed by PqqC.**" The review also notes that the *pqqA–F* genes reside together in a single **PQQ operon**.

The upstream steps involve the other *pqq* operon products: **PqqA** (the precursor peptide donating Glu and Tyr), **PqqE** (a radical-SAM enzyme forming the first carbon–carbon crosslink between the Glu and Tyr side chains), **PqqD** (a peptide chaperone that presents PqqA to PqqE), **PqqB** (a hydroxylase implicated in hydroxylation/tailoring of the developing quinoline), and **PqqF** (a protease involved in liberating the modified residues from the peptide). Martins et al. concisely capture the modular logic — "**radical SAM activity (PqqE), aided by a peptide chaperone (PqqD), a dual hydroxylase (PqqB), and an eight-electron, eight-proton oxidase (PqqC)**" ([PMID: 31427437](https://pubmed.ncbi.nlm.nih.gov/31427437/)). PqqC receives the penultimate intermediate AHQQ and performs the final ring closure and oxidation to yield mature PQQ, with no downstream enzymatic tailoring required.

---

## Mechanistic Model / Interpretation

### The PQQ biosynthetic pathway (cytoplasm)

```
  PqqA (ribosomal precursor peptide)
   │   supplies conserved Glu + Tyr
   ▼
  PqqE (radical SAM) + PqqD (peptide chaperone)
   │   forms C–C crosslink between Glu and Tyr side chains
   ▼
  PqqB (hydroxylase) / PqqF (protease)
   │   hydroxylation, cleavage, tailoring
   ▼
  AHQQ  ── the substrate of PqqC ──┐
                                    │
                                    ▼
        ┌───────────────────────────────────────────────┐
        │  PqqC  (Q88QV6, PP_0378)  EC 1.3.3.11          │
        │  - ring cyclization                            │
        │  - 8-electron / 8-proton oxidation             │
        │  - cofactor-less, metal-free                   │
        │  - uses O2, releases H2O2                       │
        │  - 7-helix bundle, positively charged site     │
        └───────────────────────────────────────────────┘
                                    │
                                    ▼
                            PQQ (mature cofactor)
```

### From cytoplasmic synthesis to periplasmic function

```
  CYTOPLASM                       |  PERIPLASM
  -----------------------------   |  ------------------------------------
  PqqA →...→ AHQQ                 |
        │                         |
     [ PqqC ] ──► PQQ ────────────┼──► PQQ binds apo-Gcd → holo-Gcd
     (soluble, cofactor-less)     |          │
                                  |          ▼
                                  |    Glucose ──► Gluconate + 2 e- + 2 H+
                                  |          │
                                  |          ▼
                                  |    electrons → respiratory chain
                                  |    gluconate → further metabolism /
                                  |                mineral-P solubilization
  ═════════════ cytoplasmic (inner) membrane ═════════════
```

### Interpretation

Three conceptual points unify the findings:

1. **PqqC is a "chemistry-first" enzyme.** It performs one of the most demanding reactions in cofactor biosynthesis — an eight-electron oxidation coupled to ring closure — using nothing but protein side chains, the substrate's own quinonoid redox chemistry, and molecular oxygen. It is a textbook example of a cofactor-independent oxidase, which explains the intense structural and mechanistic interest it has attracted.

2. **The enzyme's product is its purpose.** PqqC has no metabolic role beyond making PQQ. All of its physiological importance is *transitive*, flowing through the client quinoproteins (chiefly glucose dehydrogenase) that require PQQ to function. This is why *pqqC* loss-of-function phenocopies loss of periplasmic glucose oxidation, and why *pqqC* serves as an ecological marker for gluconate-producing, phosphate-solubilizing bacteria.

3. **Localization is compartment-bridging.** PqqC works in the cytoplasm (soluble, no signal peptide), but its product operates in the periplasm. The pathway therefore spans the cell envelope: synthesis inside, export across the inner membrane, and holo-enzyme assembly plus catalysis outside. This spatial separation is a defining feature of PQQ physiology in *P. putida*.

### Summary table of the enzyme's properties

| Property | Value | Evidence |
|---|---|---|
| Gene / locus | *pqqC* / PP_0378 | UniProt Q88QV6 |
| Enzyme name | Pyrroloquinoline-quinone synthase | UniProt; [PMID: 18371220](https://pubmed.ncbi.nlm.nih.gov/18371220/) |
| EC number | 1.3.3.11 | UniProt |
| Reaction | AHQQ → PQQ (cyclization + 8e⁻ oxidation) | [PMID: 15148379](https://pubmed.ncbi.nlm.nih.gov/15148379/) |
| Cofactor requirement | None (metal-free, cofactor-less) | [PMID: 15148379](https://pubmed.ncbi.nlm.nih.gov/15148379/) |
| Co-substrate | O₂ | [PMID: 15148379](https://pubmed.ncbi.nlm.nih.gov/15148379/) |
| Byproduct | H₂O₂ | [PMID: 15148379](https://pubmed.ncbi.nlm.nih.gov/15148379/) |
| Fold | Seven-helix bundle (heme-oxygenase-like all-α) | [PMID: 15148379](https://pubmed.ncbi.nlm.nih.gov/15148379/) |
| Active site | Positively charged; induced-fit closure | [PMID: 15148379](https://pubmed.ncbi.nlm.nih.gov/15148379/) |
| Localization | Soluble, cytoplasmic | Structure/annotation inference |
| Product function | Cofactor of periplasmic quinoprotein dehydrogenases (Gcd) | [PMID: 23392768](https://pubmed.ncbi.nlm.nih.gov/23392768/); [PMID: 7540821](https://pubmed.ncbi.nlm.nih.gov/7540821/) |
| Pathway position | Terminal enzyme (5th of 5 reactions) | [PMID: 18371220](https://pubmed.ncbi.nlm.nih.gov/18371220/); [PMID: 31427437](https://pubmed.ncbi.nlm.nih.gov/31427437/) |

---

## Evidence Base

| PMID | Title (abbreviated) | Type | Role in this report |
|---|---|---|---|
| [15148379](https://pubmed.ncbi.nlm.nih.gov/15148379/) | *Quinone biogenesis: Structure and mechanism of PqqC, the final catalyst in the production of pyrroloquinoline quinone* | Primary (crystallography + biochemistry) | **Cornerstone.** Defines the reaction (AHQQ→PQQ), cofactor-less/metal-free O₂ chemistry, H₂O₂ byproduct, seven-helix fold, induced-fit active site. Supports Findings 1, 2, 3. |
| [18371220](https://pubmed.ncbi.nlm.nih.gov/18371220/) | *The pyrroloquinoline quinone biosynthesis pathway revisited: a structural approach* | Review (structural) | Assigns the terminal cyclization/oxidation to PqqC; establishes RiPP origin from Glu+Tyr of PqqA; confirms PQQ as cofactor of alcohol/aldose dehydrogenases; operon organization. Supports Findings 1, 4, 5. |
| [31427437](https://pubmed.ncbi.nlm.nih.gov/31427437/) | *A two-component protease in [PQQ biosynthesis]* | Primary/Review | Independently characterizes PqqC as the eight-electron/eight-proton oxidase and situates it among PqqB/D/E. Supports Findings 1, 5. |
| [23392768](https://pubmed.ncbi.nlm.nih.gov/23392768/) | *Influence of periplasmic oxidation of glucose on pyoverdine synthesis in Pseudomonas putida S11* | Primary | Establishes the periplasmic PQQ-dependent oxidative glucose pathway in *P. putida*; links PQQ/Gcd to gluconate. Supports Finding 4. |
| [7540821](https://pubmed.ncbi.nlm.nih.gov/7540821/) | *Cloning of a mineral phosphate-solubilizing gene from Pseudomonas cepacia* | Primary | Identifies PQQ-dependent GDH as the periplasmic enzyme oxidizing glucose to gluconic acid. Supports Finding 4. |
| [24350630](https://pubmed.ncbi.nlm.nih.gov/24350630/) | *Intrigues and intricacies of the biosynthetic pathways for the enzymatic quinocofactors: PQQ, TTQ, CTQ, TPQ, LTQ* | Review | Broader context on quinocofactor biosynthesis (abstract unavailable; used for context only). |
| [37528183](https://pubmed.ncbi.nlm.nih.gov/37528183/) | *Long-Term Organic Fertilization ... pqqC- and phoD-Harboring Bacterial Communities* | Primary (ecology) | Documents *pqqC* as a functional marker for phosphorus-mobilizing bacteria — an ecological consequence of gluconate production. Contextual support for Finding 4. |
| [41274639](https://pubmed.ncbi.nlm.nih.gov/41274639/) | *Carbon-phosphorus coupling in reddish paddy fields ... pqqC-harboring bacteria as a driver* | Primary (ecology) | Reinforces the ecological role of *pqqC*-harboring bacteria in phosphorus mobilization. Contextual support for Finding 4. |

**Consistency of the evidence.** The core enzymatic assignment is supported by a convergence of independent evidence types: a direct crystallographic and biochemical study of the enzyme itself ([PMID: 15148379](https://pubmed.ncbi.nlm.nih.gov/15148379/)) and two independent structural/mechanistic reviews ([PMID: 18371220](https://pubmed.ncbi.nlm.nih.gov/18371220/); [PMID: 31427437](https://pubmed.ncbi.nlm.nih.gov/31427437/)). The downstream physiological role of PQQ is supported by functional/genetic studies in *P. putida* and related organisms ([PMID: 23392768](https://pubmed.ncbi.nlm.nih.gov/23392768/); [PMID: 7540821](https://pubmed.ncbi.nlm.nih.gov/7540821/)). No source reviewed contradicts the annotation.

---

## Supported vs. Refuted Hypotheses

- **Supported:** PqqC is the terminal PQQ-biosynthetic enzyme (pyrroloquinoline-quinone synthase, EC 1.3.3.11) performing ring cyclization + eight-electron oxidation of AHQQ; it is a cofactor-less, cytoplasmic seven-helix-bundle oxidase that uses O₂ and produces H₂O₂; its product PQQ functions in the periplasm as a quinoprotein dehydrogenase cofactor.
- **Refuted / excluded:** PqqC is **not** a metal- or flavin/heme-dependent oxidase; it is **not** the direct phosphate-solubilizing or glucose-oxidizing enzyme (that is PQQ-dependent Gcd). Its appearance as a "phosphorus-cycling" marker gene reflects its product's downstream role, not a direct catalytic role in P mobilization.

---

## Limitations and Knowledge Gaps

1. **Species of the definitive structural study.** The landmark crystallographic and mechanistic work on PqqC ([PMID: 15148379](https://pubmed.ncbi.nlm.nih.gov/15148379/)) was performed on an orthologous PqqC (e.g., from *Klebsiella pneumoniae*), not directly on the *P. putida* KT2440 protein (Q88QV6). However, HAMAP-rule assignment (MF_00654), high sequence conservation, identical domain architecture, and the operon-encoded, functionally interchangeable nature of the pathway make transfer of function robust. Direct characterization of the KT2440 enzyme would remove residual uncertainty.

2. **Localization is inferred, not directly measured here.** The assignment of PqqC to the soluble cytoplasm rests on the absence of a signal peptide/transmembrane segment and on the logic of the pathway, rather than on a fractionation experiment for Q88QV6. This is a well-supported inference but not a measured localization.

3. **Mechanistic details remain a proposal.** The base-catalyzed cyclization / quinone–quinol tautomerization / O₂-H₂O₂ cycling mechanism is explicitly framed as a proposal ([PMID: 15148379](https://pubmed.ncbi.nlm.nih.gov/15148379/)). The exact order of electron-transfer steps, the identity of the catalytic base, and the precise role of individual residues (e.g., Arg179) in the *P. putida* enzyme are not fully resolved.

4. **PQQ export machinery is not defined.** The model requires PQQ to move from cytoplasm to periplasm, but the transporter(s) mediating PQQ export in *P. putida* were not identified in the reviewed literature. This is a genuine open question.

5. **Upstream intermediate assignments are review-level.** The exact chemical structures and enzyme assignments for some intermediate steps (particularly PqqB's hydroxylation and any spontaneous vs. enzyme-catalyzed steps) continue to be refined in the literature.

6. **Quantitative kinetics for Q88QV6 are absent.** No Km, kcat, or O₂-affinity values specific to the KT2440 enzyme were located; kinetic parameters would strengthen quantitative modeling of PQQ supply.

---

## Proposed Follow-up Experiments / Actions

1. **Directly characterize KT2440 PqqC (Q88QV6).** Express and purify the enzyme, confirm the absence of bound metals/cofactors (ICP-MS, UV-vis), and measure steady-state kinetics (Km for AHQQ, kcat, O₂ dependence) plus H₂O₂ stoichiometry to verify the cofactor-less oxidase mechanism in this specific ortholog.

2. **Solve the KT2440 PqqC structure (or validate a model).** Determine the crystal or cryo-EM structure, or validate an AlphaFold model, to confirm the seven-helix bundle fold and the positively charged, induced-fit active site, and to map catalytic residues (e.g., the Arg179 equivalent) for site-directed mutagenesis.

3. **Genetic validation in KT2440.** Construct a clean *pqqC* deletion and test for (a) loss of PQQ production, (b) loss of periplasmic glucose→gluconate oxidation, and (c) chemical complementation by exogenous PQQ, closing the loop between PqqC and Gcd function.

4. **Localization assay.** Perform subcellular fractionation or fluorescent-fusion imaging to confirm cytoplasmic localization of PqqC and periplasmic assembly of holo-Gcd.

5. **Identify the PQQ exporter.** Use transposon or CRISPRi screens for mutants that accumulate cytoplasmic PQQ but lack periplasmic quinoprotein activity, to pinpoint the export pathway.

6. **Mechanistic dissection.** Trap and characterize reaction intermediates (stopped-flow spectroscopy, ¹⁸O₂ labeling to trace oxygen into H₂O₂ vs. product) to test the proposed quinone–quinol tautomerization / O₂-cycling mechanism directly.

7. **Applied context.** Given the role of *pqqC*/PQQ in gluconate-driven mineral-phosphate solubilization ([PMID: 37528183](https://pubmed.ncbi.nlm.nih.gov/37528183/); [PMID: 41274639](https://pubmed.ncbi.nlm.nih.gov/41274639/)), test whether overexpression of the *pqq* operon in KT2440 enhances gluconate output and phosphate solubilization for potential biofertilizer applications.

---

## Conclusion

PqqC (Q88QV6, PP_0378) is unambiguously **pyrroloquinoline-quinone synthase (EC 1.3.3.11)**, the terminal enzyme of PQQ biosynthesis. It catalyzes the ring cyclization and eight-electron/eight-proton oxidation of the intermediate AHQQ to yield the mature redox cofactor PQQ, doing so as a remarkable **cofactor-less, metal-free oxidase** that uses molecular O₂ and releases H₂O₂. It is a soluble cytoplasmic seven-helix-bundle protein with a positively charged, induced-fit active site. Its physiological importance is entirely transitive: the PQQ it produces is exported to the periplasm, where it serves as the essential cofactor of quinoprotein dehydrogenases — chiefly glucose dehydrogenase (Gcd) — driving *P. putida*'s periplasmic oxidation of glucose to gluconate. This function bridges cytoplasmic cofactor biosynthesis and periplasmic nutrient oxidation, and it underlies the ecological role of *pqqC*-harboring bacteria in gluconate-mediated mineral-phosphate solubilization.

---

### References
- Magnusson OT, Toyama H, Saeki M, Rojas A, Reed JC, Liddington RC, Klinman JP, Schwarzenbacher R. *Quinone biogenesis: structure and mechanism of PqqC, the final catalyst in the production of pyrroloquinoline quinone.* PNAS 2004. **[PMID: 15148379](https://pubmed.ncbi.nlm.nih.gov/15148379/)**
- Martins AM, et al. *A two-component protease with high activity toward the peptide precursor of the redox cofactor pyrroloquinoline quinone.* J Biol Chem 2019. **[PMID: 31427437](https://pubmed.ncbi.nlm.nih.gov/31427437/)**
- Ponraj P, Shankar M, Ilakkiam D, Rajendhran J, Gunasekaran P. *Influence of periplasmic oxidation of glucose on pyoverdine synthesis in Pseudomonas putida S11.* 2013. **[PMID: 23392768](https://pubmed.ncbi.nlm.nih.gov/23392768/)**
- Babu-Khan S, Yeo TC, Martin WL, Duron MR, Rogers RD, Goldstein AH. *Cloning of a mineral phosphate-solubilizing gene from Pseudomonas cepacia.* Appl Environ Microbiol 1995. **[PMID: 7540821](https://pubmed.ncbi.nlm.nih.gov/7540821/)**
- Puehringer S, Metlitzky M, Schwarzenbacher R. *The pyrroloquinoline quinone biosynthesis pathway revisited: a structural approach.* BMC Biochem 2008. **[PMID: 18371220](https://pubmed.ncbi.nlm.nih.gov/18371220/)**
- Klinman JP, Bonnot F. *Intrigues and intricacies of the biosynthetic pathways for the enzymatic quinocofactors: PQQ, TTQ, CTQ, TPQ, and LTQ.* Chem Rev 2014. **[PMID: 24350630](https://pubmed.ncbi.nlm.nih.gov/24350630/)**


## Artifacts

- [OpenScientist final report](pqqC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pqqC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:15148379
2. PMID:18371220
3. PMID:31427437
4. PMID:23392768
5. PMID:7540821
6. PMID:37528183
7. PMID:41274639
8. PMID:24350630