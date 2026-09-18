---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T06:14:28.881490'
end_time: '2026-08-31T07:13:16.966711'
duration_seconds: 3528.09
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pedH
  gene_symbol: pedH
  uniprot_accession: Q88JH0
  protein_description: 'RecName: Full=Quinoprotein alcohol dehydrogenase PedH {ECO:0000305|PubMed:28655819,
    ECO:0000305|Ref.3}; EC=1.1.2.- {ECO:0000305|PubMed:28655819, ECO:0000305|Ref.3};
    AltName: Full=Lanthanide-dependent pyrroloquinoline quinone-dependent alcohol
    dehydrogenase {ECO:0000303|PubMed:28655819}; Short=Lanthanide-dependent PQQ-ADH
    {ECO:0000303|PubMed:28655819}; Flags: Precursor;'
  gene_info: Name=pedH {ECO:0000303|PubMed:28655819, ECO:0000303|Ref.3}; Synonyms=qedH-II
    {ECO:0000312|EMBL:AAN68287.1}; OrderedLocusNames=PP_2679 {ECO:0000312|EMBL:AAN68287.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the bacterial PQQ dehydrogenase family.
  protein_domains: ADHI. (IPR034119); PQQ_b-propeller_rpt. (IPR018391); PQQ_MeOH/EtOH_DH.
    (IPR017512); PQQ_rpt_dom. (IPR002372); Quinoprotein_ADH-like_sf. (IPR011047)
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
citation_count: 6
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pedH-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pedH-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88JH0
- **Protein Description:** RecName: Full=Quinoprotein alcohol dehydrogenase PedH {ECO:0000305|PubMed:28655819, ECO:0000305|Ref.3}; EC=1.1.2.- {ECO:0000305|PubMed:28655819, ECO:0000305|Ref.3}; AltName: Full=Lanthanide-dependent pyrroloquinoline quinone-dependent alcohol dehydrogenase {ECO:0000303|PubMed:28655819}; Short=Lanthanide-dependent PQQ-ADH {ECO:0000303|PubMed:28655819}; Flags: Precursor;
- **Gene Information:** Name=pedH {ECO:0000303|PubMed:28655819, ECO:0000303|Ref.3}; Synonyms=qedH-II {ECO:0000312|EMBL:AAN68287.1}; OrderedLocusNames=PP_2679 {ECO:0000312|EMBL:AAN68287.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the bacterial PQQ dehydrogenase family.
- **Key Domains:** ADHI. (IPR034119); PQQ_b-propeller_rpt. (IPR018391); PQQ_MeOH/EtOH_DH. (IPR017512); PQQ_rpt_dom. (IPR002372); Quinoprotein_ADH-like_sf. (IPR011047)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pedH" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pedH' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pedH** (gene ID: pedH, UniProt: Q88JH0) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *pedH* (Q88JH0, PP_2679) in *Pseudomonas putida* KT2440

## Summary

**PedH is a periplasmic, lanthanide-dependent, pyrroloquinoline-quinone (PQQ) alcohol dehydrogenase (EC 1.1.2.–) that oxidizes a broad range of alcohols and aldehydes.** Encoded by the gene *pedH* (synonym *qedH-II*; ordered locus PP_2679) in *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950), the protein Q88JH0 belongs to the bacterial PQQ dehydrogenase family and carries the diagnostic domain architecture of a quinoprotein alcohol dehydrogenase: an eight-bladed PQQ β-propeller (IPR018391, IPR002372, IPR011047) with the ADH type-I signature (IPR034119) and the methanol/ethanol PQQ-DH fold (IPR017512). Its defining biochemical feature is that it uses a bimetallic catalytic cofactor consisting of PQQ plus a **lanthanide (rare-earth) ion (Ln³⁺)**, in contrast to the classical Ca²⁺-dependent quinoprotein dehydrogenases. PedH was the first lanthanide-dependent PQQ-ADH characterized in a **non-methylotrophic** bacterium, extending lanthanide biochemistry — previously known mainly from methanotroph/methylotroph XoxF methanol dehydrogenases — into the broad metabolic repertoire of a soil pseudomonad.

Beyond its catalytic activity, PedH plays a **dual role** as a sensory/regulatory module. It participates in a "rare-earth-element (REE) switch" in which the cell inversely regulates the two isoenzymes PedE (Ca²⁺-dependent, PP_2674) and PedH (Ln³⁺-dependent, PP_2679) according to lanthanide availability. This switch is highly sensitive, responding to as little as 1–10 nM lanthanum, an ecologically relevant concentration for soils and the rhizosphere. The molecular machinery of the switch centers on the PedS2/PedR2 two-component system (PP_2671/PP_2672): in the absence of lanthanides, sensor kinase PedS2 phosphorylates the LuxR-type response regulator PedR2, which activates *pedE* and represses *pedH*; the presence of La³⁺ reduces PedS2 kinase activity, lowering phospho-PedR2, thereby de-repressing *pedH* and reducing *pedE*.

Physiologically, the PedE/PedH system enables efficient periplasmic oxidation of **volatile organic compounds (VOCs)** — a range of linear and aromatic alcohols and aldehydes — for detoxification and catabolism, and it initiates a **novel accessory route for glycerol utilization** that operates in parallel with the canonical glpFKRD pathway. Detailed biochemical and computational studies show PedH is active only with the **early lanthanides (La³⁺ through Gd³⁺)**, with a bell-shaped activity profile across the series that peaks at Nd³⁺, and that its metal-ion preference is tunable by active-site mutations that change the coordination number. Together, these properties make *P. putida* PedE/PedH a leading model system for lanthanide biology outside methylotrophy, with emerging applications in rare-earth-element recovery and whole-cell biosensing.

---

## Gene/Protein Identity Verification

Before presenting findings, the target identity was verified against the UniProt record and the primary literature. **All checks pass**, and the literature retrieved corresponds specifically to this protein and organism:

| Attribute | UniProt (Q88JH0) | Confirmed in literature |
|---|---|---|
| Gene symbol | *pedH* (syn. *qedH-II*) | *pedH* / PP_2679 ([PMID: 28655819](https://pubmed.ncbi.nlm.nih.gov/28655819/)) |
| Locus tag | PP_2679 | PP_2679 ([PMID: 28655819](https://pubmed.ncbi.nlm.nih.gov/28655819/)) |
| Organism | *P. putida* KT2440 | *P. putida* KT2440 ([PMID: 30158283](https://pubmed.ncbi.nlm.nih.gov/30158283/)) |
| Protein family | Bacterial PQQ dehydrogenase | PQQ-dependent alcohol dehydrogenase ([PMID: 28655819](https://pubmed.ncbi.nlm.nih.gov/28655819/)) |
| Cofactor | Ln³⁺ + PQQ (implied by name) | Ln³⁺/PQQ cofactor complex ([PMID: 40031112](https://pubmed.ncbi.nlm.nih.gov/40031112/)) |
| EC | 1.1.2.– | Quinoprotein, cytochrome acceptor ([PMID: 28655819](https://pubmed.ncbi.nlm.nih.gov/28655819/)) |

The gene symbol *pedH* is **unambiguous** for this protein in the context of *P. putida*, and the literature is directly on-target. No conflicting literature for a different gene of the same symbol was encountered.

---

## Key Findings

### Finding 1 — PedH is a lanthanide-dependent periplasmic PQQ alcohol dehydrogenase

The foundational characterization of PedH comes from Wehrmann et al. (2017, *mBio*) [PMID: 28655819](https://pubmed.ncbi.nlm.nih.gov/28655819/), who purified the enzyme and demonstrated its activity in vitro. PedH (PP_2679) oxidizes a **broad range of substrates** — linear and aromatic primary and secondary alcohols, as well as aldehydes — but does so **only in the presence of lanthanide ions**, specifically La³⁺, Ce³⁺, Pr³⁺, Sm³⁺, or Nd³⁺. In the authors' words, "*PedH (PP_2679) exhibits enzyme activity on a range of substrates similar to that of its Ca2+-dependent counterpart PedE (PP_2674), including linear and aromatic primary and secondary alcohols, as well as aldehydes, but only in the presence of lanthanide ions, including La3+, Ce3+, Pr3+, Sm3+, or Nd3+.*" This makes PedH the counterpart of the Ca²⁺-dependent isoenzyme **PedE (PP_2674)**, with which it shares a similar substrate range but differs fundamentally in the metal used for catalysis.

The reaction catalyzed is the two-electron oxidation of an alcohol (or aldehyde) to the corresponding aldehyde (or carboxylic acid), coupled to reduction of the PQQ cofactor, which is re-oxidized by a downstream electron acceptor (a cytochrome), consistent with the assigned classification **EC 1.1.2.–** (quinoprotein alcohol dehydrogenase using a cytochrome as acceptor):

```
R–CH2OH  +  acceptor(ox)  --[PedH: PQQ·Ln3+]-->  R–CHO  +  acceptor(red) + 2H+
```

The localization of PedH is **periplasmic**. The Wehrmann et al. study frames the enzyme within a class of systems that many Gram-negative bacteria have evolved: "*many Gram-negative bacteria have evolved periplasmic oxidation systems based on pyrroloquinoline quinone-dependent alcohol dehydrogenases (PQQ-ADHs) that are often functionally redundant.*" The precursor form of Q88JH0 carries an N-terminal signal peptide (indicated by the "Flags: Precursor" annotation) that directs export to the periplasm, where the mature enzyme performs oxidation of its substrates using the periplasmically supplied PQQ cofactor. PedH is therefore the **first lanthanide-dependent PQQ-ADH described in a non-methylotrophic bacterium**.

### Finding 2 — PedH has a dual catalytic and sensory/regulatory role in the lanthanide switch

A striking property established by Wehrmann et al. (2017) is that PedH is not only an enzyme but also part of a **regulatory sensing system**. The authors report that "*PedH not only has a catalytic function but is also involved in the transcriptional regulation of pedE and pedH, most likely acting as a sensory module.*" The regulatory network is remarkably sensitive, responding to lanthanum concentrations as low as **1–10 nM** — a range that is ecologically meaningful given the trace abundance of bioavailable rare-earth elements in natural soils.

The consequence of this sensing is an inverse, mutually exclusive expression pattern of the two isoenzymes: PedE and PedH are **inversely regulated** depending on Ln³⁺ availability, producing what is now called the **"rare-earth-element (REE) switch."** When lanthanides are scarce, the cell expresses the Ca²⁺-dependent PedE; when lanthanides are available, it switches to the Ln³⁺-dependent PedH.

The molecular mechanism of this switch was elucidated by Wehrmann et al. (2018, *mSphere*) [PMID: 30158283](https://pubmed.ncbi.nlm.nih.gov/30158283/). The central control element is the **PedS2/PedR2 two-component system (PP_2671/PP_2672)**: "*the PedS2/PedR2 (PP_2671/PP_2672) two-component system (TCS) plays a central role in the observed REE-mediated switch of PQQ-EDHs.*" Mechanistically, "*the sensor histidine kinase PedS2 phosphorylates its cognate LuxR-type response regulator PedR2, which in turn not only activates pedE gene transcription but is also involved in repression of pedH.*" In the absence of La³⁺, PedS2 is an active kinase, phospho-PedR2 accumulates, *pedE* is switched on and *pedH* is repressed. When La³⁺ is present, PedS2 kinase activity falls, phospho-PedR2 declines, *pedE* transcription drops and *pedH* repression is relieved (with additional positive input onto *pedH* from a still-unidentified module). This wiring explains the reciprocal expression that defines the REE switch.

```
   ── No lanthanide (La3+ low) ──          ── Lanthanide present (La3+ high) ──

   PedS2 (kinase ON)                        PedS2 (kinase activity reduced)
        │ phosphorylates                          │ less phosphotransfer
        ▼                                          ▼
   PedR2~P (high)                            PedR2~P (low)
        │ activates pedE                          │ derepresses pedH
        │ represses  pedH                         │ (+ unknown activator)
        ▼                                          ▼
   PedE expressed  ──►  Ca2+-ADH active      PedH expressed ──► Ln3+-ADH active
```

### Finding 3 — The PedE/PedH system enables growth on volatile alcohols and a novel glycerol route

The physiological importance of the PQQ-dependent oxidation system was established by Wehrmann et al. (2017), who showed that the combined activity of PedE and PedH is **crucial for efficient growth** of *P. putida* KT2440 on a variety of volatile alcohols. The general metabolic rationale is that "*the oxidation of alcohols and aldehydes is crucial for detoxification and efficient catabolism of various volatile organic compounds (VOCs).*" In the periplasm, these enzymes convert potentially toxic alcohols and aldehydes into carboxylic acids that can be imported and channeled into central metabolism, serving both a protective (detoxification) and a nutritional (catabolic) function.

A more specific and unexpected physiological role was uncovered by Wehrmann et al. (2020, *mBio*) [PMID: 32345644](https://pubmed.ncbi.nlm.nih.gov/32345644/) using comparative proteomics and mutant analysis. This study demonstrated that PedE/PedH activity **initiates a novel accessory route for glycerol metabolism**. In this route, glycerol is oxidized (via glyceraldehyde) to glycerate, which is then phosphorylated by the glycerate kinase GarK (likely to glycerate-2-phosphate) and channeled into central carbon metabolism. This periplasmic-oxidation route operates **in parallel** with the canonical cytoplasmic glpFKRD pathway and confers a growth advantage in the form of an **earlier onset of growth**. The study confirmed that "*the two pyrroloquinoline quinone-dependent alcohol dehydrogenases (PQQ-ADHs) PedE and PedH are inversely regulated in response to REE availability,*" and further showed that **La³⁺ availability strongly affects growth on glycerol**, tying the regulatory switch directly to a concrete metabolic phenotype.

```
Glycerol ──[PedE/PedH, periplasmic oxidation]──► glyceraldehyde ──► glycerate
                                                                         │ GarK (glycerate kinase)
                                                                         ▼
                                                              glycerate-2-phosphate ──► central metabolism
   (parallel to the canonical cytoplasmic glpFKRD pathway; gives earlier growth onset)
```

### Finding 4 — Metal preference: early lanthanides, bell-shaped activity peaking at Nd³⁺

The metal specificity of PedH was dissected in fine detail by Wang et al. (2025, *Colloids and Surfaces B*) [PMID: 40031112](https://pubmed.ncbi.nlm.nih.gov/40031112/) using purified enzyme, mutational analysis, and density functional theory (DFT). This work confirmed the general principle that "*Lanthanide (Ln) elements form a cofactor complex with pyrroloquinoline quinone (PQQ) in bacterial alcohol dehydrogenases,*" and established several quantitative structure–activity relationships:

- Only the **early lanthanides (La³⁺ through Gd³⁺)** support high Ln³⁺-ADH activity; the later (heavier, smaller-radius) lanthanides do not.
- Across the lanthanide series, PedH activity follows a **bell-shaped trend**, with **Nd³⁺ giving the highest activity** — consistent with an optimum ionic radius that balances Lewis acidity against steric/coordination constraints in the active site.
- **Active-site mutations that alter the number of coordinating ligands shift the enzyme's metal-ion preference**, demonstrating that coordination number is a tunable determinant of which lanthanide is optimal.
- DFT analysis indicated that the **HOMO–LUMO gap, substrate interaction energy, and metal-ion binding distances** govern catalytic activity, providing a physical-chemical explanation linking coordination number and ionic radius to performance.

This establishes a mechanistic model in which the lanthanide ion functions as a Lewis-acid catalyst that polarizes the PQQ/substrate system, and in which the geometry of the metal-binding pocket selects for a specific subset of the lanthanide series.

| Metal parameter | Observation | Source |
|---|---|---|
| Active series | Early lanthanides La³⁺–Gd³⁺ only | [PMID: 40031112](https://pubmed.ncbi.nlm.nih.gov/40031112/) |
| Peak activity | Nd³⁺ (bell-shaped trend) | [PMID: 40031112](https://pubmed.ncbi.nlm.nih.gov/40031112/) |
| Active in vitro | La³⁺, Ce³⁺, Pr³⁺, Nd³⁺, Sm³⁺ | [PMID: 28655819](https://pubmed.ncbi.nlm.nih.gov/28655819/) |
| Tunability | Coordination-number mutations shift preference | [PMID: 40031112](https://pubmed.ncbi.nlm.nih.gov/40031112/) |
| Governing factors | HOMO–LUMO gap, substrate interaction energy, M–ligand distances | [PMID: 40031112](https://pubmed.ncbi.nlm.nih.gov/40031112/) |

### Finding 5 — PedH extends lanthanide-dependent PQQ metabolism beyond methylotrophs

PedH occupies an important place in the broader field of lanthanide biology. As reviewed by Daumann (2022, perspective) [PMID: 36167440](https://pubmed.ncbi.nlm.nih.gov/36167440/), the recognition that lanthanides serve as catalytic cofactors began with methanol dehydrogenases: "*After the first demonstration of a lanthanide in the active site of the XoxF-type pyrroloquinoline quinone methanol dehydrogenases, follow-up studies showed the same for other pyrroloquinoline quinone-containing enzymes.*" PedH is a central example of these "other PQQ-containing enzymes," and its characterization in *P. putida* extended lanthanide-dependent catalysis from the narrow world of methanotrophs and methylotrophs into a versatile, non-methylotrophic soil bacterium.

The significance of this expansion is echoed in the methylotrophy field. Chistoserdova & Kalyuzhnaya (2018, *Trends in Microbiology*) [PMID: 29471983](https://pubmed.ncbi.nlm.nih.gov/29471983/) note that "*we discuss the significance of the recent discovery of lanthanide-dependent alcohol dehydrogenases for understanding both the occurrence and the distribution of methylotrophy functions among bacteria.*" PedH thereby serves as a model for how lanthanides act not only as catalytic cofactors but also as **regulatory signals** that modulate gene expression and metal handling, with translational interest in rare-earth-element recovery/biomining and lanthanide biosensing.

---

## Mechanistic Model / Interpretation

PedH can be understood as a two-in-one device: a **periplasmic redox enzyme** and a **lanthanide-responsive regulatory input**, both built on the same PQQ-quinoprotein scaffold.

**As an enzyme:** PedH is exported to the periplasm as a precursor, folds into an eight-bladed β-propeller (the canonical PQQ-ADH fold, IPR011047), and assembles a bimetallic active site comprising **PQQ + an early lanthanide ion**. The Ln³⁺ ion replaces the Ca²⁺ used by the sister enzyme PedE and, because lanthanides are stronger Lewis acids, it can support catalysis with distinct kinetic and specificity characteristics. Substrate alcohols/aldehydes are oxidized at the PQQ cofactor, the reduced PQQ is re-oxidized by a dedicated cytochrome, and the electrons enter the periplasmic respiratory chain (EC 1.1.2.–). The result is periplasmic conversion of volatile alcohols/aldehydes into acids for detoxification and catabolism — including the accessory glycerol → glycerate → glycerate-2-phosphate route feeding central metabolism.

**As a sensor/switch:** The cell needs to deploy the correct isoenzyme for the available metal. This decision is executed by the **PedS2/PedR2 two-component system**, with PedH itself contributing sensory input. The presence of nanomolar La³⁺ shifts the balance from PedE (Ca²⁺) to PedH (Ln³⁺). This "REE switch" is one of the clearest examples of lanthanides acting as bona fide **signaling ions** in bacteria.

```
                     ┌─────────────────────────────────────────────┐
                     │         Lanthanide availability (La3+)        │
                     └───────────────┬─────────────────────────────┘
                                     │  sensed by PedS2/PedR2 TCS (+ PedH sensory input)
                    low La3+  ◄───────┴────────►  high La3+
                       │                              │
              PedR2~P high                     PedR2~P low
              pedE ON / pedH OFF               pedH ON / pedE OFF
                       │                              │
                       ▼                              ▼
             PedE (Ca2+ + PQQ)              PedH (Ln3+ + PQQ)  ← this protein, Q88JH0
                       │                              │
                       └──────────┬───────────────────┘
                                  ▼
                 Periplasmic oxidation of alcohols/aldehydes (VOCs)
                 + accessory glycerol oxidation route
                                  ▼
                    Detoxification + catabolism / growth
```

Within the lanthanide series, the enzyme is selective for the early (larger-radius) members, with a coordination-geometry-determined optimum at Nd³⁺. This selectivity is not fixed: engineering the number of metal-coordinating residues re-tunes the preferred lanthanide, which is both mechanistically informative and biotechnologically useful for building lanthanide-selective biosensors and biosorbents.

---

## Evidence Base

| PMID | Study (year, journal) | Contribution to this annotation |
|---|---|---|
| [28655819](https://pubmed.ncbi.nlm.nih.gov/28655819/) | Wehrmann et al. 2017, *mBio* — *Functional Role of Lanthanides in Enzymatic Activity and Transcriptional Regulation of PQQ-ADHs in P. putida* | Primary characterization: purified PedH oxidizes broad alcohol/aldehyde range only with Ln³⁺; counterpart to Ca²⁺-dependent PedE; periplasmic PQQ-ADH system; dual catalytic + sensory role; 1–10 nM La sensitivity; first Ln-dependent PQQ-ADH in a non-methylotroph. **Supports Findings 1, 2, 3.** |
| [30158283](https://pubmed.ncbi.nlm.nih.gov/30158283/) | Wehrmann et al. 2018, *mSphere* — *The PedS2/PedR2 Two-Component System Is Crucial for the REE Switch* | Molecular mechanism of the switch: PedS2 kinase phosphorylates LuxR-type PedR2; PedR2~P activates *pedE* and represses *pedH*. **Supports Finding 2.** |
| [32345644](https://pubmed.ncbi.nlm.nih.gov/32345644/) | Wehrmann et al. 2020, *mBio* — *The Cellular Response to Lanthanum … Novel Route for Glycerol Metabolism* | Proteomics + mutants: PedE/PedH initiate an accessory glycerol-oxidation route (via GarK) parallel to glpFKRD; La³⁺ strongly affects glycerol growth; confirms inverse REE regulation. **Supports Finding 3.** |
| [40031112](https://pubmed.ncbi.nlm.nih.gov/40031112/) | Wang et al. 2025, *Colloids Surf. B* — *Coordination number and ionic radius … mutational studies and DFT* | Metal-preference profiling: active only with early lanthanides La–Gd, bell-shaped activity peaking at Nd³⁺; coordination-number mutations shift preference; DFT rationalizes activity. **Supports Finding 4.** |
| [36167440](https://pubmed.ncbi.nlm.nih.gov/36167440/) | Daumann 2022 — *A perspective on the role of lanthanides in biology* | Places PedH within the broader class of Ln-utilizing PQQ enzymes discovered after XoxF; regulatory + applied context. **Supports Finding 5.** |
| [29471983](https://pubmed.ncbi.nlm.nih.gov/29471983/) | Chistoserdova & Kalyuzhnaya 2018, *Trends in Microbiology* — *Current Trends in Methylotrophy* | Field significance of Ln-dependent alcohol dehydrogenases for the distribution of methylotrophy functions. **Supports Finding 5.** |

The evidence base is coherent and mutually reinforcing. The 2017 primary study anchors enzyme identity, cofactor requirement, localization, and the dual role; the 2018 study supplies the regulatory mechanism; the 2020 study supplies a concrete metabolic phenotype; the 2025 study supplies quantitative metal-specificity and structural rationale; and the two reviews situate PedH in the wider field. No retrieved study contradicts the annotation.

---

## Limitations and Knowledge Gaps

1. **No experimentally determined 3D structure for PedH specifically** was identified in the retrieved literature. The domain architecture (IPR011047, IPR018391, IPR017512) and DFT modeling ([PMID: 40031112](https://pubmed.ncbi.nlm.nih.gov/40031112/)) strongly imply the eight-bladed β-propeller PQQ-ADH fold and a defined lanthanide-coordination sphere, but atomic-resolution confirmation of the PedH active site and its bound lanthanide would strengthen the mechanistic model.

2. **Kinetic parameters are incompletely catalogued here.** While the substrate range (linear/aromatic primary and secondary alcohols, aldehydes) and the active lanthanide set are established, quantitative kcat/Km values for individual substrate–metal combinations were not extracted in this investigation and would refine the substrate-specificity picture.

3. **The identity of the electron acceptor/cytochrome** partner that re-oxidizes PedH's PQQ in vivo, and the exact routing of electrons into the respiratory chain, were not resolved in the retrieved sources. The EC 1.1.2.– classification implies a cytochrome acceptor but the specific partner remains to be pinned down for PedH.

4. **The "unknown module" activating *pedH*.** The 2018 mechanism explains repression of *pedH* by PedR2~P but invokes an additional, unidentified activator of *pedH* under high-lanthanide conditions. The identity of this factor is an open question.

5. **Physiological lanthanide uptake and delivery.** How lanthanides are acquired, transported across the outer membrane, and delivered to periplasmic PedH (e.g., via lanthanophores/TonB-dependent uptake) is not covered by the retrieved literature and is an important gap for the complete pathway.

6. **This report is literature-based** (six papers). No new sequence, structural, or omics analyses were performed in this investigation; conclusions rest on the cited experimental and computational studies.

---

## Proposed Follow-up Experiments / Actions

1. **Solve the PedH structure with bound lanthanide** (X-ray crystallography or cryo-EM) to visualize the PQQ/Ln³⁺ active site and directly test the coordination-number model that explains the Nd³⁺ optimum.

2. **Measure full kinetic profiles** (kcat, Km, kcat/Km) for a substrate panel (methanol, ethanol, higher/aromatic alcohols, glyceraldehyde, aldehydes) crossed with each early lanthanide, to quantify substrate × metal specificity.

3. **Identify the cognate cytochrome/electron acceptor** for PedH via co-purification, cross-linking, or genetic dissection, and map the periplasmic respiratory route.

4. **Find the unknown *pedH* activator** through transcription-factor pull-downs on the *pedH* promoter, transposon screens, or ChIP-seq under high-lanthanide conditions.

5. **Dissect lanthanide uptake/delivery**: test for lanthanophores and TonB-dependent transporters, and determine how Ln³⁺ reaches periplasmic PedH.

6. **Engineer metal selectivity** by systematic active-site coordination-number mutagenesis (building on [PMID: 40031112](https://pubmed.ncbi.nlm.nih.gov/40031112/)) to create PedH variants selective for target rare-earth elements — enabling REE-recovery biosorbents and whole-cell lanthanide biosensors.

7. **In situ / rhizosphere validation**: test the REE switch and glycerol route under environmentally realistic nanomolar lanthanide conditions to confirm ecological relevance.

---

## Conclusion

PedH (Q88JH0 / PP_2679) of *Pseudomonas putida* KT2440 is a **periplasmic, lanthanide(Ln³⁺)-dependent PQQ alcohol dehydrogenase (EC 1.1.2.–)** that oxidizes a broad range of linear and aromatic primary and secondary alcohols and aldehydes, using a PQQ–early-lanthanide cofactor (active with La³⁺–Gd³⁺, peak at Nd³⁺). It is the lanthanide-utilizing isoenzyme of the Ca²⁺-dependent PedE and, beyond catalysis, functions as a **lanthanide sensor** that, with the PedS2/PedR2 two-component system, drives the inverse **rare-earth-element switch** between *pedE* and *pedH*. Physiologically it supports detoxification/catabolism of volatile alcohols and initiates an accessory glycerol-oxidation route, establishing *P. putida* PedE/PedH as a landmark model for lanthanide biology outside methylotrophy.


## Artifacts

- [OpenScientist final report](pedH-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pedH-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:28655819
2. PMID:30158283
3. PMID:40031112
4. PMID:32345644
5. PMID:36167440
6. PMID:29471983