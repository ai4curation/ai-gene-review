---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T16:19:41.839956'
end_time: '2026-07-11T16:36:03.180361'
duration_seconds: 981.34
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: metB
  gene_symbol: metB
  uniprot_accession: Q88Q39
  protein_description: 'SubName: Full=Cystathionine gamma-synthase {ECO:0000313|EMBL:AAN66284.1};'
  gene_info: Name=metB {ECO:0000313|EMBL:AAN66284.1}; OrderedLocusNames=PP_0659 {ECO:0000313|EMBL:AAN66284.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the trans-sulfuration enzymes family.
  protein_domains: Cys/Met-Metab_PyrdxlP-dep_enz. (IPR000277); Cys_met_metab_PP. (IPR054542);
    PyrdxlP-dep_Trfase. (IPR015424); PyrdxlP-dep_Trfase_major. (IPR015421); PyrdxlP-dep_Trfase_small.
    (IPR015422)
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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: metB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: metB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88Q39
- **Protein Description:** SubName: Full=Cystathionine gamma-synthase {ECO:0000313|EMBL:AAN66284.1};
- **Gene Information:** Name=metB {ECO:0000313|EMBL:AAN66284.1}; OrderedLocusNames=PP_0659 {ECO:0000313|EMBL:AAN66284.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the trans-sulfuration enzymes family.
- **Key Domains:** Cys/Met-Metab_PyrdxlP-dep_enz. (IPR000277); Cys_met_metab_PP. (IPR054542); PyrdxlP-dep_Trfase. (IPR015424); PyrdxlP-dep_Trfase_major. (IPR015421); PyrdxlP-dep_Trfase_small. (IPR015422)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "metB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'metB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **metB** (gene ID: metB, UniProt: Q88Q39) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# metB (PP_0659, Q88Q39): Cystathionine γ-Synthase of *Pseudomonas putida* KT2440

## Summary

The gene **metB** (ordered locus **PP_0659**; UniProt **Q88Q39**) of *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) encodes **cystathionine γ-synthase (CGS)**, a pyridoxal-5′-phosphate (PLP)-dependent enzyme of the **trans-sulfuration enzyme family** (EC 2.5.1.48; KEGG orthology K01739). Gene identity, protein description, organism, and the diagnostic InterPro/Pfam domains all agree: the protein is a *bona fide* MetB cystathionine γ-synthase, and its symbol, family and domain complement match the biochemically characterized enzyme with no evidence of gene-symbol ambiguity. The verification checks required by the research brief are therefore satisfied.

The primary function of the enzyme is to catalyze the **first committed, methionine-specific step of *de novo* methionine biosynthesis**: a PLP-dependent **γ-replacement reaction** in which the acyl group of an *O*-acyl-L-homoserine is displaced by the thiol of **L-cysteine** to form **L-cystathionine**. In *Pseudomonas*, homoserine is activated as its *O*-succinyl ester by MetA, so the physiological substrates of P. putida MetB are **O-succinyl-L-homoserine and L-cysteine**, yielding L-cystathionine plus succinate. The product cystathionine is subsequently cleaved by cystathionine β-lyase (MetC) to homocysteine, which is methylated to methionine. This trans-sulfuration branch operates in parallel with a direct-sulfhydrylation route (MetZ) that also exists in *Pseudomonas*.

Mechanistically and structurally, MetB is a **cytoplasmic homotetramer** (α4) in which PLP is covalently anchored to an active-site lysine via a Schiff-base internal aldimine — position **Lys216** in Q88Q39. Catalysis proceeds through a shared PLP-bound quinonoid/aminocrotonate (pyridoxamine-vinylglyoxylate) intermediate that partitions between the productive γ-replacement and a slower competing γ-elimination side reaction. Substrate specificity toward *O*-succinyl- versus *O*-acetyl-homoserine is dictated by the conformation of the β10–β11 active-site loop. All of these features are established for orthologous, biochemically and crystallographically characterized CGS enzymes from *E. coli*, *C. glutamicum*, and plants, and the domain architecture of Q88Q39 is fully consistent with them.

---

## Key Findings

### F001 — metB is cystathionine γ-synthase, the first committed step of bacterial trans-sulfuration

Q88Q39/PP_0659 is annotated as cystathionine γ-synthase (MetB) and belongs to the trans-sulfuration / Cys-Met-metabolism PLP-dependent enzyme family (InterPro **IPR000277**, **IPR054542**). The defining reaction of this enzyme class is a PLP-dependent **γ-replacement**: the acyl group of an *O*-acyl-L-homoserine is displaced by the thiol of L-cysteine to form L-cystathionine, constituting the **first step of the bacterial trans-sulfuration pathway** and the first reaction unique to methionine biosynthesis.

This assignment is grounded in biochemically characterized orthologs. In *E. coli* CGS, the catalytic efficiency for the succinyl-homoserine substrate is high (k_cat/K_m for L-OSHS ≈ 9.8 × 10⁴ M⁻¹ s⁻¹; [PMID: 14503880](https://pubmed.ncbi.nlm.nih.gov/14503880/)), confirming that *O*-succinyl-L-homoserine is a kinetically competent physiological substrate. The *C. glutamicum* study explicitly states that "*Cystathionine γ-synthase (MetB) condenses O-acetyl-l-homoserine (OAHS) or O-succinyl-l-homoserine (OSHS) with cysteine to produce cystathionine*" ([PMID: 28675039](https://pubmed.ncbi.nlm.nih.gov/28675039/)), and the *E. coli* mechanistic study defines the reaction as one "*in which the succinyl group of an O-succinyl-L-homoserine (L-OSHS) is displaced by the thiol of L-cysteine to form L-cystathionine, in the first step of the bacterial transsulfuration pathway*" ([PMID: 14503880](https://pubmed.ncbi.nlm.nih.gov/14503880/)).

**Reaction catalyzed:**

```
O-succinyl-L-homoserine  +  L-cysteine  --(PLP)-->  L-cystathionine  +  succinate
```

### F002 — MetB is a PLP-dependent homotetramer with a Lys–PLP Schiff base; specificity set by the β10–β11 loop

The 1.5 Å structure of *E. coli* CGS shows an **α4 tetramer** with subunits related by non-crystallographic 222 symmetry, performing PLP-dependent γ-replacement of *O*-succinyl-L-homoserine and L-cysteine to yield L-cystathionine — described as the only known PLP-dependent replacement reaction at Cγ ([PMID: 9843488](https://pubmed.ncbi.nlm.nih.gov/9843488/)): "*The transsulfuration enzyme cystathionine gamma-synthase (CGS) catalyses the pyridoxal 5′-phosphate (PLP)-dependent gamma-replacement of O-succinyl-L-homoserine and L-cysteine, yielding L-cystathionine*" and "*The enzyme crystallizes as an alpha4 tetramer with the subunits related by non-crystallographic 222 symmetry.*"

In *C. glutamicum* MetB (1.5 Å), PLP is covalently bound to the active-site lysine via a Schiff base in a deep cavity ([PMID: 28675039](https://pubmed.ncbi.nlm.nih.gov/28675039/)): "*The pyridoxal phosphate cofactor is covalently bound to Lys204 via a Schiff base linkage in the deep cavity.*" The equivalent catalytic lysine in Q88Q39 is **Lys216** (see F004). Structural comparison further identifies the **β10–β11 connecting loop** as the determinant of acyl-group specificity: "*we propose that the conformation of the β10-β11 connecting loops determines the size and shape of the acetyl- or succinyl-group binding site and ultimately determines the substrate specificity of MetBs toward OAHS or OSHS*" ([PMID: 28675039](https://pubmed.ncbi.nlm.nih.gov/28675039/)). Q88Q39 carries the diagnostic PLP-dependent transferase domains **IPR015421/IPR015422/IPR015424** and the Cys/Met-metabolism PLP-enzyme signature **IPR000277**, consistent with this fold and mechanism.

### F003 — Catalysis proceeds via a PLP quinonoid/aminocrotonate intermediate with a competing γ-elimination side reaction

Stopped-flow spectroscopy of *E. coli* CGS provided "*direct evidence for a pyridoxamine derivative of vinylglyoxylate as a key intermediate in pyridoxal phosphate dependent gamma-elimination and gamma-replacement reactions*" ([PMID: 2405904](https://pubmed.ncbi.nlm.nih.gov/2405904/)). This intermediate is the partitioning point common to both the productive γ-replacement (with L-cysteine) and the competing **γ-elimination** side reaction, in which "*L-OSHS is hydrolyzed to succinate, NH₃, and alpha-ketobutyrate*" ([PMID: 14503880](https://pubmed.ncbi.nlm.nih.gov/14503880/)). The elimination reaction is roughly 70-fold slower than replacement (k_cat/K_m ≈ 1350 M⁻¹ s⁻¹), and the enzyme follows an **ordered mechanism** — "*The mechanism of Escherichia coli CGS (eCGS) is ordered with L-OSHS associating before L-Cys*" ([PMID: 14503880](https://pubmed.ncbi.nlm.nih.gov/14503880/)) — becoming ping-pong at low cysteine, with a bell-shaped pH profile (optimum ≈ 7.4–7.8).

### F004 — EC 2.5.1.48 / K01739 in methionine biosynthesis module M00017; PLP bound at Lys216

KEGG assigns **ppu:PP_0659** to orthology **K01739** (cystathionine γ-synthase, **EC 2.5.1.48**), pathway **ppu00270** (Cysteine and methionine metabolism), and module **ppu_M00017** (Methionine biosynthesis: aspartate ⇒ homoserine ⇒ methionine). UniProt **Q88Q39** (423 aa) records a single modified residue, **N6-(pyridoxal phosphate)lysine at position 216**, matching Pfam **PF01053** (Cys/Met metabolism PLP-dependent enzyme) and eggNOG **COG0626** (cystathionine β-lyase/γ-synthase). A C-terminal coiled-coil (residues ~383–410) is also annotated, consistent with the oligomerization/tetramer-interface features of this family.

### F005 — *Pseudomonas* activates homoserine as its O-succinyl ester, so P. putida MetB uses O-succinyl-L-homoserine

In *Pseudomonas aeruginosa*, the first committed methionine step is catalyzed by an *O*-succinylhomoserine synthase, the product of *metA*: "*The first step is catalysed by an O-succinylhomoserine synthase, the product of the metA gene*" ([PMID: 7704274](https://pubmed.ncbi.nlm.nih.gov/7704274/)). *Pseudomonas* is described as "*the only organism so far described that uses O-succinylhomoserine as substrate for a direct sulfhydrylation*" (via MetZ), and importantly "*the two transsulfuration pathways between cysteine and homocysteine, with cystathionine as an intermediate, probably exist in parallel in this organism*" ([PMID: 7704274](https://pubmed.ncbi.nlm.nih.gov/7704274/)). Because *P. putida* KT2440 is a close congener with the same metA/metB/metC gene set, its MetB (PP_0659) condenses **O-succinyl-L-homoserine with L-cysteine** as its physiological reaction, and the resulting cystathionine feeds the trans-sulfuration route that runs alongside the direct MetZ sulfhydrylation.

---

## Mechanistic Model / Interpretation

MetB (PP_0659) sits at the branch point where **sulfur (from cysteine) is committed to methionine**. The de novo methionine pathway in *Pseudomonas* can be summarized as:

```
   L-aspartate
        │  (aspartokinase, ASADH, homoserine dehydrogenase)
        ▼
   L-homoserine
        │  MetA  (+ succinyl-CoA)
        ▼
   O-succinyl-L-homoserine  ───────────────┐
        │                                    │
        │  MetB (CGS, PP_0659)   + L-Cys     │  MetZ (direct sulfhydrylation)
        │                                    │  + HS⁻ (bisulfide)
        ▼                                    ▼
   L-cystathionine  + succinate         L-homocysteine
        │  MetC (cystathionine β-lyase)      │
        ▼                                    │
   L-homocysteine  + pyruvate + NH3          │
        │◄───────────────────────────────────┘
        │  MetE/MetH  (+ CH3 from methyl-THF / methyl-cobalamin)
        ▼
   L-methionine ──► SAM (S-adenosylmethionine)
```

**The catalytic cycle** at the PLP center proceeds as follows. The resting enzyme holds PLP as an internal aldimine (Schiff base) with the active-site lysine (Lys216 in Q88Q39). *O*-succinyl-L-homoserine binds first and forms an external aldimine; Cα-proton abstraction and β,γ-elimination of the succinyl group generate a PLP-bound **aminocrotonate / pyridoxamine-vinylglyoxylate quinonoid intermediate** ([PMID: 2405904](https://pubmed.ncbi.nlm.nih.gov/2405904/)). This electrophilic intermediate is then attacked by the thiol of L-cysteine at Cγ (γ-replacement), producing L-cystathionine. When cysteine is scarce, water instead intercepts the intermediate, giving the **γ-elimination** products succinate, ammonia, and α-ketobutyrate ([PMID: 14503880](https://pubmed.ncbi.nlm.nih.gov/14503880/)). The shared intermediate explains why the same active site catalyzes two chemistries whose relative flux depends on cysteine availability.

**Substrate specificity** is a structural property of the acyl-binding subsite. The β10–β11 connecting loop molds a pocket sized for either an acetyl or a succinyl group ([PMID: 28675039](https://pubmed.ncbi.nlm.nih.gov/28675039/)). Because *Pseudomonas* MetA produces the succinyl ester ([PMID: 7704274](https://pubmed.ncbi.nlm.nih.gov/7704274/)), P. putida MetB is expected to be tuned to *O*-succinyl-L-homoserine, in contrast to the *O*-acetyl-homoserine used by many other bacteria and the *O*-phosphohomoserine used by plants.

**Localization.** MetB is a soluble **cytoplasmic** enzyme. It has no signal peptide or transmembrane segment; amino-acid biosynthesis, PLP chemistry, and the availability of cytosolic cysteine and succinyl-homoserine all place its activity in the cytoplasm.

| Property | Value / Assignment | Source |
|---|---|---|
| Gene / locus | metB / PP_0659 | UniProt Q88Q39 |
| Enzyme | Cystathionine γ-synthase | F001 |
| EC number | 2.5.1.48 | KEGG (F004) |
| KEGG orthology | K01739 | KEGG (F004) |
| Pathway / module | ppu00270 / M00017 | KEGG (F004) |
| Cofactor | Pyridoxal-5′-phosphate (PLP) | F002/F004 |
| Catalytic residue | Lys216 (Schiff-base) | UniProt (F004) |
| Quaternary structure | Homotetramer (α4) | [PMID: 9843488](https://pubmed.ncbi.nlm.nih.gov/9843488/) |
| Physiological substrates | O-succinyl-L-homoserine + L-cysteine | F001/F005 |
| Products | L-cystathionine + succinate | F001 |
| Side reaction | γ-elimination → succinate + NH₃ + α-ketobutyrate | [PMID: 14503880](https://pubmed.ncbi.nlm.nih.gov/14503880/) |
| Length | 423 aa | UniProt Q88Q39 |
| Localization | Cytoplasm | Inference from function |

### Substrate specificity across orthologs

| Organism / enzyme | Homoserine ester substrate | Second substrate | Catalytic Lys | Reference |
|---|---|---|---|---|
| *E. coli* CGS | O-succinyl-L-homoserine | L-cysteine | — | [PMID: 9843488](https://pubmed.ncbi.nlm.nih.gov/9843488/), [PMID: 14503880](https://pubmed.ncbi.nlm.nih.gov/14503880/) |
| *C. glutamicum* MetB | O-acetyl or O-succinyl-L-homoserine | L-cysteine | Lys204 | [PMID: 28675039](https://pubmed.ncbi.nlm.nih.gov/28675039/) |
| *N. tabacum* CGS (plant) | O-phosphohomoserine | L-cysteine | — | [PMID: 10438597](https://pubmed.ncbi.nlm.nih.gov/10438597/), [PMID: 10595588](https://pubmed.ncbi.nlm.nih.gov/10595588/) |
| *A. thaliana* CGS (plant) | O-phosphohomoserine | L-cysteine | Lys379 | [PMID: 9531508](https://pubmed.ncbi.nlm.nih.gov/9531508/) |
| *P. putida* MetB (PP_0659) | O-succinyl-L-homoserine (inferred) | L-cysteine | Lys216 | This report (F004/F005) |

---

## Evidence Base

The functional assignment for Q88Q39 rests principally on **strong homology to biochemically and structurally characterized CGS enzymes**, combined with genome-context and database annotations. No study has yet characterized the *P. putida* PP_0659 protein directly; the conclusions are inferences from close orthologs, which is appropriate given the high sequence and domain conservation of this enzyme family.

| PMID | Title (abbrev.) | How it supports the findings |
|---|---|---|
| [14503880](https://pubmed.ncbi.nlm.nih.gov/14503880/) | *E. coli CGS does not obey ping-pong kinetics; continuous assays* | Defines the γ-replacement reaction and substrate (L-OSHS + L-Cys → cystathionine); documents the competing γ-elimination and ordered kinetic mechanism; provides catalytic efficiencies (F001, F003). |
| [9843488](https://pubmed.ncbi.nlm.nih.gov/9843488/) | *Crystal structure of E. coli CGS at 1.5 Å* | Establishes the PLP-dependent γ-replacement mechanism and the homotetrameric (α4) quaternary structure (F002). |
| [28675039](https://pubmed.ncbi.nlm.nih.gov/28675039/) | *Structural insights into substrate specificity of C. glutamicum CGS* | Confirms MetB substrate/product identity; localizes catalytic PLP–Lys Schiff base; identifies the β10–β11 loop as the OAHS/OSHS specificity determinant (F001, F002). |
| [2405904](https://pubmed.ncbi.nlm.nih.gov/2405904/) | *Reaction mechanism of E. coli CGS* | Direct spectroscopic evidence for the pyridoxamine-vinylglyoxylate intermediate shared by γ-replacement and γ-elimination (F003). |
| [7704274](https://pubmed.ncbi.nlm.nih.gov/7704274/) | *Direct sulfhydrylation pathway in P. aeruginosa* | Shows *Pseudomonas* activates homoserine as the O-succinyl ester (MetA) and runs trans-sulfuration (cystathionine) in parallel with direct sulfhydrylation (MetZ), fixing the physiological substrate of P. putida MetB (F005). |
| [9531508](https://pubmed.ncbi.nlm.nih.gov/9531508/) | *A. thaliana CGS characterization* | Homotetramer, one PLP per subunit at an active-site lysine, ping-pong mechanism, very weak γ-elimination — cross-kingdom confirmation of family properties. |
| [10438597](https://pubmed.ncbi.nlm.nih.gov/10438597/) / [10595588](https://pubmed.ncbi.nlm.nih.gov/10595588/) | *N. tabacum CGS structure & biochemistry* | Illustrate how distal-group binding (phosphate vs acyl) tunes substrate specificity — the same principle underlying bacterial OSHS/OAHS selection. |

Two notes on citation quality: the [PMID: 2405904](https://pubmed.ncbi.nlm.nih.gov/2405904/) snippet was flagged as a title-derived match rather than an abstract-verified quote, but it accurately reflects the paper's established finding. The plant CGS papers use O-phosphohomoserine and therefore support the *mechanistic and structural* family properties rather than the exact *Pseudomonas* substrate.

---

## Limitations and Knowledge Gaps

1. **No direct characterization of PP_0659.** All conclusions are inferences from orthologs (*E. coli*, *C. glutamicum*, plants). The *P. putida* enzyme has not been purified, kinetically assayed, or crystallized. Kinetic constants (K_m, k_cat) and the exact γ-replacement/γ-elimination partition ratio for the KT2440 protein are unknown.

2. **Substrate specificity is inferred, not measured.** The assignment of *O*-succinyl-L-homoserine as the physiological substrate rests on the *P. aeruginosa* MetA study ([PMID: 7704274](https://pubmed.ncbi.nlm.nih.gov/7704274/)) and general *Pseudomonas* biology. Whether P. putida MetB can also accept *O*-acetyl-homoserine (as *C. glutamicum* MetB does) has not been tested experimentally.

3. **Catalytic-residue mapping.** Lys216 as the PLP Schiff-base lysine comes from UniProt sequence-based annotation, not from a P. putida structure; its identity should be confirmed structurally or by mutagenesis.

4. **Pathway redundancy and regulation.** The relative flux through the MetB (trans-sulfuration) versus MetZ (direct sulfhydrylation) routes in *P. putida* under different sulfur/cysteine conditions is not quantified, nor is transcriptional regulation (e.g., MetR/MetJ-type control) established for this specific organism.

5. **Localization is inferred.** Cytoplasmic localization is deduced from function and the absence of targeting signals rather than demonstrated experimentally in P. putida.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and enzyme assay.** Clone PP_0659, express in *E. coli*, purify, and confirm PLP content (spectral A₃₄₀/A₄₂₀). Measure γ-replacement kinetics with *O*-succinyl-L-homoserine + L-cysteine and compare against *O*-acetyl-L-homoserine to define substrate preference directly.

2. **γ-elimination partitioning.** Quantify the competing γ-elimination (succinate, NH₃, α-ketobutyrate production) using the continuous assays described for *E. coli* CGS ([PMID: 14503880](https://pubmed.ncbi.nlm.nih.gov/14503880/)) to establish the replacement:elimination ratio for the P. putida enzyme.

3. **Structure determination.** Solve the crystal or cryo-EM structure of PP_0659 (apo and PLP-bound) to confirm the homotetramer, the Lys216 Schiff base, and the β10–β11 loop geometry that predicts succinyl-ester specificity.

4. **Genetic validation.** Construct a ΔmetB (PP_0659) deletion in KT2440 and test for methionine auxotrophy; complement with wild-type and active-site (K216A) variants to confirm the catalytic residue.

5. **Pathway flux and regulation.** Use isotope tracing or metabolomics under varied sulfur/cysteine conditions to determine the in vivo balance between the MetB (cystathionine) and MetZ (direct sulfhydrylation) branches, and profile transcriptional regulation of the met regulon in P. putida.

6. **AlphaFold structural inference.** In the absence of an experimental structure, an AlphaFold model of Q88Q39 can be used to validate the predicted PLP-binding pocket, tetramer interface, and the acyl-binding β10–β11 loop, providing structural support ahead of wet-lab work.

---

## Conclusion

The gene symbol **metB** is **not ambiguous** for this target: gene name, protein description, organism, family, and domain complement all consistently identify Q88Q39/PP_0659 as **cystathionine γ-synthase** of *P. putida* KT2440. The enzyme is a cytoplasmic, PLP-dependent, homotetrameric trans-sulfuration enzyme (EC 2.5.1.48; K01739) that catalyzes the **first committed step of methionine biosynthesis** — the γ-replacement of *O*-succinyl-L-homoserine with L-cysteine to give L-cystathionine plus succinate — within cysteine/methionine metabolism (pathway ppu00270, module M00017). Its catalytic PLP is anchored at Lys216, catalysis proceeds through a pyridoxamine-vinylglyoxylate intermediate that also drives a minor γ-elimination side reaction, and its physiological substrate is set by *Pseudomonas*' use of the succinyl-homoserine ester. These assignments are strongly supported by biochemistry and crystallography of close orthologs but await direct experimental confirmation for the P. putida protein itself.


## Artifacts

- [OpenScientist final report](metB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](metB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:14503880
2. PMID:28675039
3. PMID:9843488
4. PMID:2405904
5. PMID:7704274
6. PMID:10438597
7. PMID:10595588
8. PMID:9531508