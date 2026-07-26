---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-15T16:46:54.475582'
end_time: '2026-07-15T16:57:07.151027'
duration_seconds: 612.68
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_0416
  gene_symbol: PP_0416
  uniprot_accession: Q88QS2
  protein_description: 'RecName: Full=Phosphoglycolate phosphatase {ECO:0000255|HAMAP-Rule:MF_00495};
    Short=PGP {ECO:0000255|HAMAP-Rule:MF_00495}; Short=PGPase {ECO:0000255|HAMAP-Rule:MF_00495};
    EC=3.1.3.18 {ECO:0000255|HAMAP-Rule:MF_00495};'
  gene_info: OrderedLocusNames=PP_0416;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the HAD-like hydrolase superfamily.
  protein_domains: HAD-like_hydrolase_sf. (IPR050155); HAD-like_sf. (IPR036412); HAD-SF_hydro_IA.
    (IPR006439); HAD-SF_hydro_IIIA. (IPR006549); HAD_2. (IPR041492)
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
citation_count: 16
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_0416-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_0416-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QS2
- **Protein Description:** RecName: Full=Phosphoglycolate phosphatase {ECO:0000255|HAMAP-Rule:MF_00495}; Short=PGP {ECO:0000255|HAMAP-Rule:MF_00495}; Short=PGPase {ECO:0000255|HAMAP-Rule:MF_00495}; EC=3.1.3.18 {ECO:0000255|HAMAP-Rule:MF_00495};
- **Gene Information:** OrderedLocusNames=PP_0416;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the HAD-like hydrolase superfamily.
- **Key Domains:** HAD-like_hydrolase_sf. (IPR050155); HAD-like_sf. (IPR036412); HAD-SF_hydro_IA. (IPR006439); HAD-SF_hydro_IIIA. (IPR006549); HAD_2. (IPR041492)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_0416" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_0416' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_0416** (gene ID: PP_0416, UniProt: Q88QS2) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PP_0416 (Q88QS2) — Phosphoglycolate Phosphatase of *Pseudomonas putida* KT2440

**Gene:** PP_0416 (OrderedLocusName) · **Protein:** Phosphoglycolate phosphatase (PGP / PGPase)
**Organism:** *Pseudomonas putida* KT2440 (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950)
**EC:** 3.1.3.18 · **Family:** HAD-like hydrolase superfamily (HAMAP rule MF_00495)

## Summary

**PP_0416** of *Pseudomonas putida* KT2440 (UniProt **Q88QS2**) encodes **phosphoglycolate phosphatase (PGP / PGPase; EC 3.1.3.18)**, a soluble cytoplasmic enzyme belonging to the **haloacid dehalogenase (HAD)-like hydrolase superfamily**. Its primary function is to catalyze the **Mg²⁺-dependent hydrolysis of 2-phosphoglycolate to glycolate and inorganic phosphate**. The enzyme is highly specific for its 2-phosphoglycolate substrate, a hallmark of a dedicated metabolite-repair (proofreading) phosphatase rather than a broad-spectrum hydrolase. This functional assignment is supported by direct orthology to the biochemically characterized *Escherichia coli* enzyme Gph, by conserved InterPro domain signatures (HAD-SF hydrolase subfamilies IA and IIIA), and by the presence of an intact, canonical HAD catalytic tetrad in the Q88QS2 protein sequence.

Mechanistically, PP_0416 operates through the conserved HAD chemistry: an active-site **aspartate nucleophile (Asp19)** attacks the substrate phosphorus to form a covalent **phospho-aspartyl intermediate**, which is then hydrolyzed with the assistance of a second aspartate (Asp21) acting as a general acid/base, all coordinated by a catalytic **Mg²⁺** ion. The four diagnostic HAD sequence motifs are all identifiable in Q88QS2 — Motif I (DLDGT, beginning at residue 19), Motif II (conserved Ser/Thr), Motif III (conserved Lys near residue 123), and Motif IV (the Mg²⁺-binding GDxxxD, present as GDSRSD at residue 181) — confirming a fully assembled Rossmann-fold catalytic core with a small cap domain that provides substrate specificity.

Physiologically, the enzyme performs **metabolic repair / salvage**: it clears the small, potentially inhibitory phosphorylated byproduct 2-phosphoglycolate that arises intracellularly (most notably during the repair of 3′-phosphoglycolate DNA ends produced by oxidative and radiomimetic DNA damage) and recovers the carbon skeleton as **glycolate**. In *P. putida*, glycolate is a defined node of two-carbon (C2) metabolism that is oxidized by glycolate oxidase (the *glcDEF* operon) to glyoxylate and assimilated through the glyoxylate carboligase (*gcl*) pathway into central carbon metabolism. The enzyme thus links genome maintenance and metabolite-damage control to central metabolism, and it does so in the cytoplasm.

---

## Key Findings

### Finding 1 — PP_0416 is a phosphoglycolate phosphatase catalyzing 2-phosphoglycolate → glycolate + Pi

The core functional identity of PP_0416 is that of **phosphoglycolate phosphatase (EC 3.1.3.18)**. UniProt Q88QS2 assigns this activity via the curated HAMAP family rule **MF_00495**, which defines the bacterial PGP/PGPase family. The most informative experimental support comes from the well-characterized bacterial ortholog, *E. coli* **Gph**, which was purified and shown to be **highly specific for 2-phosphoglycolate** with good catalytic efficiency (k_cat/K_m). Critically, this efficiency is high enough to permit turnover of the substrate even at the low intracellular concentrations at which 2-phosphoglycolate is typically present ([PMID: 13129953](https://pubmed.ncbi.nlm.nih.gov/13129953/)).

The reaction catalyzed is:

```
2-phosphoglycolate  +  H2O   ──[PGP, Mg2+]──►   glycolate  +  Pi
```

The narrow substrate range distinguishes PP_0416 from the many promiscuous sugar-phosphate phosphatases of the HAD superfamily; it is a purpose-built enzyme for a single small metabolite. The verbatim experimental basis is: *"The enzyme was highly specific for 2-phosphoglycolate and showed good catalytic efficiency (k(cat)/K(m)), which enabled the conversion of this substrate even at low intracellular concentrations."* ([PMID: 13129953](https://pubmed.ncbi.nlm.nih.gov/13129953/)).

### Finding 2 — Catalytic mechanism: Mg²⁺-dependent phospho-aspartyl transfer within the HAD superfamily

Q88QS2 belongs to the **HAD-like hydrolase superfamily**, as indicated by its InterPro assignments: HAD-like hydrolase superfamily (IPR050155), HAD-like superfamily fold (IPR036412), and the HAD-SF hydrolase subfamily IA (IPR006439) and subfamily IIIA (IPR006549) signatures, plus the HAD_2 domain (IPR041492). HAD phosphatases share a **Rossmann-like α/β fold** and a defining active-site **DxDx(V/T)** motif, and they operate through a conserved two-step chemistry: an aspartate nucleophile attacks the phosphoryl group to form a covalent phospho-aspartate intermediate, which is subsequently hydrolyzed — all in a **magnesium-dependent** reaction ([PMID: 22607316](https://pubmed.ncbi.nlm.nih.gov/22607316/)). A conserved pair of aspartates coordinates the catalytic Mg²⁺, and a Ser/Thr assists in phosphate binding, with the mechanism proceeding through the phospho-aspartate intermediate ([PMID: 10191250](https://pubmed.ncbi.nlm.nih.gov/10191250/)).

The defining mechanistic statement is: *"HAD phosphatases employ an aspartate residue as a nucleophile in a magnesium-dependent phosphoaspartyl transferase reaction."* ([PMID: 22607316](https://pubmed.ncbi.nlm.nih.gov/22607316/)), and the intermediate is supported by *"a mechanism comprising a phosphoaspartate intermediate is postulated"* ([PMID: 10191250](https://pubmed.ncbi.nlm.nih.gov/10191250/)).

### Finding 3 — Sequence-level confirmation of the HAD catalytic tetrad

Direct inspection of the 272-residue Q88QS2 sequence confirms an intact, canonical HAD active site — the strongest structure/sequence-based evidence that this protein is a functional phosphatase rather than a pseudoenzyme:

| HAD motif | Consensus | Location in Q88QS2 | Catalytic role |
|-----------|-----------|--------------------|----------------|
| Motif I | DxDx(T/V) | **DLDGT**, residue 19 | Asp19 = nucleophile (forms phospho-aspartyl intermediate); Asp21 = general acid/base |
| Motif II | conserved Ser/Thr | Ser/Thr | Stabilizes/orients the transferred phosphoryl group |
| Motif III | conserved Lys | Lys near residue 123 (…ITNK123…) | Neutralizes negative charge of the transition state |
| Motif IV | GDxxxD | **GDSRSD**, residue 181 (Asp182/Asp186) | Coordinates the catalytic Mg²⁺ ion |

The protein length (~272 aa) and the Rossmann-fold core plus a small α/β cap domain are fully consistent with a **class I HAD phosphatase** (InterPro IPR006439). The active-site signature DxDx(V/T) that identifies HAD family members ([PMID: 22607316](https://pubmed.ncbi.nlm.nih.gov/22607316/)) is present as **DLDGT at position 19**. The completeness of all four motifs (Finding 7) rules out the possibility that PP_0416 is a degenerate family member lacking activity.

### Finding 4 — Physiological role: salvage / metabolic repair of 2-phosphoglycolate

The physiological rationale for PP_0416 is **metabolite repair**. 2-Phosphoglycolate is not a biosynthetic intermediate but a byproduct that must be cleared. In *E. coli*, *gph* is a **constitutively expressed housekeeping gene** whose product dissimilates the intracellular 2-phosphoglycolate generated during **DNA repair of 3′-phosphoglycolate ends** — for example, the strand-break ends produced by the radiomimetic agent bleomycin. A *gph*-deficient mutant behaves differently from the parental strain, directly linking 2-phosphoglycolate formation to glycolate production that is then incorporated into general metabolism ([PMID: 13129953](https://pubmed.ncbi.nlm.nih.gov/13129953/)). Consistent with a DNA-repair-linked role, Gph shows **increased physical interaction with GAPDH upon bleomycin challenge** ([PMID: 23195894](https://pubmed.ncbi.nlm.nih.gov/23195894/)).

The salvage function is stated explicitly: *"We thus provide evidence for a salvage function of 2-phosphoglycolate phosphatase in the metabolism of a two-carbon compound generated by the cellular DNA repair machinery."* ([PMID: 13129953](https://pubmed.ncbi.nlm.nih.gov/13129953/)). The source of substrate is captured by: *"This enzyme is involved in the metabolism of 2-phosphoglycolate formed in the DNA repair of 3'-phosphoglycolate ends generated by bleomycin damage."* ([PMID: 23195894](https://pubmed.ncbi.nlm.nih.gov/23195894/)).

### Finding 5 — Downstream pathway in *P. putida*: glycolate → glyoxylate → central metabolism

The product of the PGP reaction, **glycolate**, is not a dead end in *P. putida* KT2440 — it is a defined C2 metabolic node. *P. putida* metabolizes glycolate via **glycolate oxidase (the *glcDEF* operon)** to **glyoxylate**, which is then assimilated through the **glyoxylate carboligase (*gcl*) operon pathway** (*gcl, hyi, glxR, ttuD, pykF*) into central carbon metabolism ([PMID: 29885475](https://pubmed.ncbi.nlm.nih.gov/29885475/); [PMID: 31166064](https://pubmed.ncbi.nlm.nih.gov/31166064/)). Glycolate is a documented toxic-intermediate bottleneck in the organism's C2 metabolism (arising, for example, from ethylene glycol / glycolaldehyde catabolism), and relieving that bottleneck by overexpressing *glcDEF* supports growth ([PMID: 29885475](https://pubmed.ncbi.nlm.nih.gov/29885475/)).

Supporting quotes: *"It is metabolized by aerobic microbial processes via the highly toxic intermediates glycolaldehyde and glycolate through C2 metabolic pathways."* and *"the additional overexpression of the glycolate oxidase (glcDEF) operon removes the glycolate bottleneck"* ([PMID: 29885475](https://pubmed.ncbi.nlm.nih.gov/29885475/)). This establishes the metabolic fate of the glycolate produced by PP_0416 and situates the enzyme at the interface between damage control and central metabolism.

### Finding 6 — Subcellular localization: soluble cytoplasmic enzyme

PP_0416 is a **cytoplasmic (cytosolic) protein**. The Q88QS2 sequence begins **MSGFEQLFPGT…** and carries the HAD Motif I (DLDGT) starting at residue 19; there is **no N-terminal cleavable Sec/Tat signal peptide and no membrane-spanning leader**, indicating the protein is not secreted or membrane-embedded. This matches the experimentally characterized ortholog: *E. coli* Gph is a constitutively expressed cytoplasmic housekeeping enzyme that acts on intracellular 2-phosphoglycolate ([PMID: 13129953](https://pubmed.ncbi.nlm.nih.gov/13129953/)), and its interaction partner GAPDH is likewise a cytosolic enzyme ([PMID: 23195894](https://pubmed.ncbi.nlm.nih.gov/23195894/)). The localization is consistent with the substrate's origin (intracellular DNA repair and metabolic processes) and its downstream consumption by cytoplasmic C2-metabolism enzymes.

The verbatim basis is: *"We showed that this housekeeping enzyme is involved in the dissimilation of the intracellular 2-phosphoglycolate formed in the DNA repair of 3'-phosphoglycolate ends."* ([PMID: 13129953](https://pubmed.ncbi.nlm.nih.gov/13129953/)).

### Finding 7 — Complete catalytic tetrad + "metabolic proofreading" character

All four HAD catalytic motifs are present and correctly spaced in Q88QS2 (see the table in Finding 3), demonstrating a fully functional active site. Phosphoglycolate phosphatase has been explicitly characterized as a **metabolic proofreading enzyme essential for cellular function** ([PMID: 30700551](https://pubmed.ncbi.nlm.nih.gov/30700551/); correction [PMID: 31676556](https://pubmed.ncbi.nlm.nih.gov/31676556/)). The **narrow, high specificity** of the bacterial enzyme for 2-phosphoglycolate ([PMID: 13129953](https://pubmed.ncbi.nlm.nih.gov/13129953/)) is precisely the signature of a dedicated metabolite-repair phosphatase whose role is to clear a small, potentially inhibitory phosphorylated byproduct before it can accumulate. The mechanistic match is anchored by *"HAD phosphatases employ an aspartate residue as a nucleophile in a magnesium-dependent phosphoaspartyl transferase reaction."* ([PMID: 22607316](https://pubmed.ncbi.nlm.nih.gov/22607316/)).

---

## Mechanistic Model / Interpretation

The findings converge on a single, coherent model in which PP_0416 acts as a cytoplasmic "cleanup" phosphatase bridging genome maintenance and central carbon metabolism.

```
   DNA damage (oxidative / bleomycin)
   3'-phosphoglycolate DNA ends
              │  (DNA end-processing / repair)
              ▼
      2-PHOSPHOGLYCOLATE  ◄── small, potentially inhibitory phosphorylated byproduct
              │
              │   PP_0416 / Q88QS2  (phosphoglycolate phosphatase, EC 3.1.3.18)
              │   HAD mechanism: Asp19 nucleophile → phospho-Asp intermediate → hydrolysis
              │   Mg2+-dependent (Motif IV GDSRSD-181); high specificity
              ▼
        GLYCOLATE  +  Pi
              │
              │   glycolate oxidase  (glcDEF operon)
              ▼
         GLYOXYLATE
              │
              │   glyoxylate carboligase pathway (gcl, hyi, glxR, ttuD, pykF)
              ▼
      CENTRAL CARBON METABOLISM
```

**Enzyme class and chemistry.** PP_0416 is a class I HAD-superfamily phosphatase. The Rossmann-fold core houses the catalytic tetrad, while a small cap domain confers the strict specificity for 2-phosphoglycolate. Catalysis proceeds by nucleophilic attack of Asp19 on the substrate phosphorus, forming a phospho-aspartyl intermediate that is resolved by a water molecule activated by Asp21, with Mg²⁺ (coordinated by the Motif IV aspartates) stabilizing the transition state and the Motif III lysine neutralizing developing negative charge.

**Why the enzyme exists (proofreading logic).** 2-Phosphoglycolate is a "damage" metabolite — a phosphorylated two-carbon species that is not part of any productive biosynthetic route and can interfere with metabolism if allowed to accumulate. Dedicated, high-specificity removal is the defining feature of metabolite-repair (proofreading) enzymes. The constitutive, housekeeping expression of the ortholog and the high catalytic efficiency at low substrate concentration both fit a system that must keep a damage metabolite at trace levels at all times.

**Localization–function coherence.** The absence of any signal/anchor sequence places the enzyme in the cytoplasm, exactly where its substrate is generated (DNA repair) and where its product is consumed. This spatial coherence — substrate source, enzyme, and product-consuming pathway all cytoplasmic — reinforces the functional assignment.

**Organism-specific context.** Unlike photosynthetic organisms, where PGP (e.g., plant PGLP1) is the committed entry step of the photorespiratory C2 cycle, *P. putida* is a non-photosynthetic soil bacterium. Here PGP's role is metabolite repair/salvage rather than photorespiration, but the downstream biochemistry (glycolate → glyoxylate → assimilation) is conserved in principle and is well documented in *P. putida* KT2440 through its native *glcDEF* and *gcl* pathways.

---

## Evidence Base

| PMID | Title / focus | How it supports the annotation |
|------|---------------|--------------------------------|
| [13129953](https://pubmed.ncbi.nlm.nih.gov/13129953/) | *Role of 2-phosphoglycolate phosphatase of E. coli in metabolism of the 2-phosphoglycolate formed in DNA repair* | Primary biochemical characterization of the bacterial ortholog (Gph): high specificity for 2-phosphoglycolate, good k_cat/K_m, constitutive housekeeping expression, cytoplasmic salvage of a DNA-repair-derived C2 compound. Grounds Findings 1, 4, 6, 7. |
| [22607316](https://pubmed.ncbi.nlm.nih.gov/22607316/) | *Human HAD phosphatases: structure, mechanism, and roles in health and disease* | Defines the HAD superfamily fold and DxDx(V/T) active-site signature and the Asp-nucleophile, Mg²⁺-dependent phospho-aspartyl transfer mechanism. Grounds Findings 2, 3, 7. |
| [10191250](https://pubmed.ncbi.nlm.nih.gov/10191250/) | *Identification of the Mg²⁺-binding site in HAD superfamily members by similarity to CheY* | Establishes the Mg²⁺-coordinating aspartate pair and the postulated phospho-aspartate intermediate. Grounds Finding 2. |
| [23195894](https://pubmed.ncbi.nlm.nih.gov/23195894/) | *Protein interaction studies point to new functions for E. coli GAPDH* | Shows Gph–GAPDH interaction strengthened by bleomycin, tying PGP to DNA-repair-associated processes and to cytosolic metabolism. Grounds Findings 4, 6. |
| [29885475](https://pubmed.ncbi.nlm.nih.gov/29885475/) | *Engineering P. putida KT2440 for efficient ethylene glycol utilization* | Documents glycolate as a toxic C2 node and glycolate oxidase (glcDEF) as its consuming enzyme in *P. putida*. Grounds Finding 5 (downstream fate of glycolate). |
| [31166064](https://pubmed.ncbi.nlm.nih.gov/31166064/) | *Laboratory evolution reveals the metabolic and regulatory basis of ethylene glycol metabolism by P. putida KT2440* | Details the glyoxylate carboligase pathway and its regulation in *P. putida*, into which glyoxylate (from glycolate) is assimilated. Grounds Finding 5. |
| [30700551](https://pubmed.ncbi.nlm.nih.gov/30700551/) / [31676556](https://pubmed.ncbi.nlm.nih.gov/31676556/) | *Phosphoglycolate phosphatase is a metabolic proofreading enzyme essential for cellular function* (+ correction) | Frames PGP as a metabolic-proofreading enzyme, the conceptual basis for Finding 7. |
| [15952775](https://pubmed.ncbi.nlm.nih.gov/15952775/) | *HAD subclass IIB sugar phosphatase BT4131* | Comparative structural analysis showing how high-specificity phosphoglycolate phosphatase uses a single substrate-specificity loop with three polar residues for the glycolate leaving group (vs. lax sugar-phosphatases). Supports the specificity rationale for Findings 1 and 7. |

**Supporting / contextual literature (eukaryotic PGLP).** A cluster of plant/algal studies characterize photorespiratory PGLP1 (e.g., rice [PMID: 35083835](https://pubmed.ncbi.nlm.nih.gov/35083835/); wheat [PMID: 34981152](https://pubmed.ncbi.nlm.nih.gov/34981152/); Arabidopsis guard-cell [PMID: 41889139](https://pubmed.ncbi.nlm.nih.gov/41889139/); thermotolerance [PMID: 38409783](https://pubmed.ncbi.nlm.nih.gov/38409783/)), assay methods ([PMID: 38861076](https://pubmed.ncbi.nlm.nih.gov/38861076/); [PMID: 38861075](https://pubmed.ncbi.nlm.nih.gov/38861075/)), and archaeal 2-PG salvage ([PMID: 38593075](https://pubmed.ncbi.nlm.nih.gov/38593075/)). These confirm the conserved 2-PG → glycolate reaction across domains of life but describe the photorespiratory/CBB-cycle context, which is **not** the context of the non-photosynthetic *P. putida* enzyme. They are corroborative for the reaction chemistry but should not be over-interpreted as evidence for a photorespiratory role in PP_0416.

---

## Verification of Gene/Protein Identity

The mandatory identity checks are satisfied:

1. **Gene symbol vs. description:** The ordered-locus name **PP_0416** maps to UniProt **Q88QS2**, annotated as phosphoglycolate phosphatase (EC 3.1.3.18) — consistent throughout.
2. **Organism:** *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950), confirmed as the source organism; downstream-pathway evidence (Finding 5) is drawn from this exact strain.
3. **Family/domain alignment:** The HAD-like hydrolase superfamily assignment and the DxDx(T/V) / GDxxxD motifs found in the sequence match the family and the biochemically established PGP mechanism.
4. **No cross-organism symbol confusion:** The bacterial-ortholog evidence (*E. coli* Gph) and the *P. putida*-specific downstream pathway are internally consistent; there is no conflation with an unrelated gene bearing a similar symbol.

The literature specific to the *P. putida* enzyme itself is limited (no dedicated primary study of PP_0416 was found), so the functional assignment rests on **orthology to biochemically characterized bacterial PGP**, **conserved catalytic-motif analysis of the Q88QS2 sequence**, and **organism-specific evidence for the downstream glycolate pathway** — a well-supported inference rather than a direct in vitro characterization of Q88QS2.

---

## Limitations and Knowledge Gaps

- **No direct experimental characterization of Q88QS2.** All enzymatic claims (specificity, kinetics, mechanism) are inferred from the *E. coli* Gph ortholog and from sequence-motif analysis. The specific k_cat, K_m, pH optimum, and metal preference of the *P. putida* enzyme have not been measured.
- **No experimental structure.** The catalytic-tetrad assignment is sequence-based (motif identification). An experimental crystal structure or a validated AlphaFold model with the substrate/Mg²⁺ modeled would confirm active-site geometry and the specificity loop.
- **In vivo substrate flux unquantified.** The magnitude of 2-phosphoglycolate flux through PP_0416 in *P. putida* under normal versus DNA-damage conditions is unknown; the DNA-repair link is established in *E. coli*, not directly in *P. putida*.
- **Genomic context / regulation not analyzed here.** Whether PP_0416 is constitutively expressed (as in *E. coli*) or induced under oxidative/genotoxic stress in *P. putida* has not been verified. Its operonic neighbors and any co-regulated genes were not examined.
- **Possible minor substrate promiscuity.** While the ortholog is highly specific, some HAD phosphatases exhibit low-level activity on related small phosphomonoesters; this has not been ruled out for Q88QS2.
- **Alternative 2-PG sources.** Beyond DNA repair, other cellular sources of 2-phosphoglycolate in a non-photosynthetic bacterium (e.g., side reactions) are not well defined and could modulate the enzyme's physiological importance.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzyme kinetics.** Clone PP_0416, purify the His-tagged protein, and measure activity toward 2-phosphoglycolate (and a panel of related phosphomonoesters) using the coupled glycolate-oxidase assay ([PMID: 38861076](https://pubmed.ncbi.nlm.nih.gov/38861076/)) or NMR glycolate detection ([PMID: 38861075](https://pubmed.ncbi.nlm.nih.gov/38861075/)). Determine k_cat, K_m, Mg²⁺ dependence, and substrate specificity.
2. **Active-site mutagenesis.** Generate D19A (nucleophile) and D21A (acid/base) variants and Motif IV GDSRSD Asp mutants; confirm loss of activity to validate the predicted catalytic tetrad.
3. **Structural determination.** Solve a crystal structure (or validate an AlphaFold model with Phenix) with Mg²⁺ and a substrate analog bound to confirm the Rossmann-fold + cap architecture and map the substrate-specificity loop (cf. [PMID: 15952775](https://pubmed.ncbi.nlm.nih.gov/15952775/)).
4. **Gene deletion phenotyping.** Construct a ΔPP_0416 mutant in *P. putida* KT2440 and test for 2-phosphoglycolate accumulation, sensitivity to genotoxic/oxidative agents (e.g., bleomycin, H₂O₂), and growth on C2 substrates that route through glycolate.
5. **Expression/regulation analysis.** Use RT-qPCR or RNA-seq to determine baseline expression and induction under DNA-damage and oxidative stress; examine genomic context for co-regulated repair/metabolism genes.
6. **Metabolic flux link.** Combine ΔPP_0416 with glycolate-pathway reporters or ¹³C tracing to confirm that PGP-derived glycolate feeds the glcDEF → glyoxylate → gcl route into central metabolism in vivo ([PMID: 29885475](https://pubmed.ncbi.nlm.nih.gov/29885475/); [PMID: 31166064](https://pubmed.ncbi.nlm.nih.gov/31166064/)).

---

## Conclusion

PP_0416 (Q88QS2) is, with high confidence, the **phosphoglycolate phosphatase** of *Pseudomonas putida* KT2440: a **soluble cytoplasmic HAD-superfamily hydrolase** that catalyzes the **Mg²⁺-dependent, phospho-aspartyl-mediated dephosphorylation of 2-phosphoglycolate to glycolate and inorganic phosphate**, with high substrate specificity. It functions as a **metabolite-proofreading / salvage enzyme**, clearing the 2-phosphoglycolate generated during DNA 3′-phosphoglycolate-end repair and recovering the carbon as glycolate, which feeds the organism's native **glycolate oxidase (glcDEF) → glyoxylate → glyoxylate-carboligase** pathway into central metabolism. The assignment is anchored by orthology to the biochemically characterized *E. coli* Gph, by conserved HAD catalytic-motif analysis of the Q88QS2 sequence, and by organism-specific evidence for the downstream glycolate pathway, though direct in vitro characterization of the *P. putida* enzyme itself remains to be performed.


## Artifacts

- [OpenScientist final report](PP_0416-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_0416-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:13129953
2. PMID:22607316
3. PMID:10191250
4. PMID:23195894
5. PMID:29885475
6. PMID:31166064
7. PMID:30700551
8. PMID:31676556
9. PMID:35083835
10. PMID:34981152
11. PMID:41889139
12. PMID:38409783
13. PMID:38861076
14. PMID:38861075
15. PMID:38593075
16. PMID:15952775