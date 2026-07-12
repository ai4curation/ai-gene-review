---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T16:19:41.793372'
end_time: '2026-07-11T16:50:48.359791'
duration_seconds: 1866.57
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: metZ
  gene_symbol: metZ
  uniprot_accession: Q88LD4
  protein_description: 'RecName: Full=O-succinylhomoserine sulfhydrylase {ECO:0000256|HAMAP-Rule:MF_02056};
    Short=OSH sulfhydrylase {ECO:0000256|HAMAP-Rule:MF_02056}; Short=OSHS sulfhydrylase
    {ECO:0000256|HAMAP-Rule:MF_02056}; EC=2.5.1.- {ECO:0000256|HAMAP-Rule:MF_02056};'
  gene_info: Name=metZ {ECO:0000256|HAMAP-Rule:MF_02056, ECO:0000313|EMBL:AAN67615.1};
    OrderedLocusNames=PP_2001 {ECO:0000313|EMBL:AAN67615.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the trans-sulfuration enzymes family. MetZ
  protein_domains: Cys/Met-Metab_PyrdxlP-dep_enz. (IPR000277); Cys_met_metab_PP. (IPR054542);
    O-succ-hSer_sulfhydrylase. (IPR006234); PyrdxlP-dep_Trfase. (IPR015424); PyrdxlP-dep_Trfase_major.
    (IPR015421)
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
citation_count: 10
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: metZ-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: metZ-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88LD4
- **Protein Description:** RecName: Full=O-succinylhomoserine sulfhydrylase {ECO:0000256|HAMAP-Rule:MF_02056}; Short=OSH sulfhydrylase {ECO:0000256|HAMAP-Rule:MF_02056}; Short=OSHS sulfhydrylase {ECO:0000256|HAMAP-Rule:MF_02056}; EC=2.5.1.- {ECO:0000256|HAMAP-Rule:MF_02056};
- **Gene Information:** Name=metZ {ECO:0000256|HAMAP-Rule:MF_02056, ECO:0000313|EMBL:AAN67615.1}; OrderedLocusNames=PP_2001 {ECO:0000313|EMBL:AAN67615.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the trans-sulfuration enzymes family. MetZ
- **Key Domains:** Cys/Met-Metab_PyrdxlP-dep_enz. (IPR000277); Cys_met_metab_PP. (IPR054542); O-succ-hSer_sulfhydrylase. (IPR006234); PyrdxlP-dep_Trfase. (IPR015424); PyrdxlP-dep_Trfase_major. (IPR015421)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "metZ" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'metZ' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **metZ** (gene ID: metZ, UniProt: Q88LD4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: metZ (O-Succinylhomoserine Sulfhydrylase) in *Pseudomonas putida* KT2440

**UniProt Accession:** Q88LD4 | **Gene:** metZ | **Ordered Locus:** PP_2001
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440) — PSEPK
**EC:** 2.5.1.- | **Enzyme family:** Cys/Met-metabolism PLP-dependent, trans-sulfuration (γ-family), MetZ subfamily

---

## Gene/Protein Identity Verification

The target is **metZ** (ordered locus **PP_2001**; UniProt **Q88LD4**) of *Pseudomonas putida* KT2440, annotated as **O-succinylhomoserine (OSH) sulfhydrylase** (EC 2.5.1.-), a member of the trans-sulfuration (Cys/Met-metabolism, PLP-dependent) enzyme family, MetZ subgroup. The literature is **fully consistent** with this identity. The gene symbol *metZ* in *Pseudomonas* denotes exactly this enzyme: it was originally defined in *Pseudomonas aeruginosa* as the O-succinylhomoserine sulfhydrylase performing direct sulfhydrylation in methionine biosynthesis [PMID: 7704274](https://pubmed.ncbi.nlm.nih.gov/7704274/), and direct sulfhydrylation of O-succinylhomoserine was experimentally demonstrated in *Pseudomonas putida* itself [PMID: 10482527](https://pubmed.ncbi.nlm.nih.gov/10482527/). The organism, gene symbol, protein family (trans-sulfuration/MetZ), and PLP-dependent Cys/Met domains all align. **No gene-symbol ambiguity was encountered.**

---

## Summary

The gene **metZ** (PP_2001, UniProt **Q88LD4**) of *Pseudomonas putida* KT2440 encodes **O-succinylhomoserine sulfhydrylase (OSHS)**, a soluble, cytoplasmic, pyridoxal-5′-phosphate (PLP)-dependent enzyme that catalyzes the second, sulfur-incorporating step of *de novo* **L-methionine biosynthesis**. The enzyme performs **direct sulfhydrylation**: it condenses **O-succinyl-L-homoserine** with **inorganic sulfide (HS⁻)** to yield **L-homocysteine** and **succinate**, bypassing the cystathionine intermediate used by the alternative transsulfuration pathway. This is a distinctive reaction because *Pseudomonas* is the primary described case of an organism that uses the *succinyl* (rather than acetyl) ester of homoserine for direct sulfhydrylation.

Three convergent lines of evidence establish this function. First, the founding characterization of *metZ* in the sibling species *P. aeruginosa* directly demonstrated that this gene encodes the enzyme performing the second step of methionine biosynthesis by direct sulfhydrylation of O-succinylhomoserine [PMID: 7704274](https://pubmed.ncbi.nlm.nih.gov/7704274/). Second, direct experimental study of sulfur metabolism in *P. putida* itself confirmed that this organism uses direct sulfhydrylation of O-succinylhomoserine as its **primary** methionine-biosynthetic route, with the transsulfuration enzymes expressed only at low, cysteine-inducible levels [PMID: 10482527](https://pubmed.ncbi.nlm.nih.gov/10482527/). Third, loss-of-function genetics in the orthologous system of *Rhizobium etli* showed that a *metZ* mutant lacks detectable O-succinylhomoserine sulfhydrylase activity and becomes a methionine auxotroph, and that the gene functionally complements a *P. aeruginosa metZ* mutant [PMID: 9885190](https://pubmed.ncbi.nlm.nih.gov/9885190/).

At the mechanistic level, metZ belongs to the γ-subclass of the Cys/Met-metabolism PLP fold — the same fold shared by cystathionine γ-lyase, methionine γ-lyase, and O-acetylhomoserine sulfhydrylase (MetY). Catalysis proceeds through a covalent **PLP–lysine Schiff base (internal aldimine)** that activates the homoserine-ester substrate for γ-replacement, and the enzyme's preference for the bulkier **succinyl** leaving group is encoded by the conformation of an active-site acyl-binding loop (the β10–β11 connecting-loop region). The enzyme functions in the **cytoplasm** as a soluble homotetramer, consistent with its family. Together these data yield a confident, mechanistically detailed annotation for a protein that has not itself been the subject of a dedicated structural or kinetic study, but whose function is tightly constrained by orthology, pathway context, and family biochemistry.

---

## Key Findings

### Finding 1 — metZ encodes O-succinylhomoserine sulfhydrylase, catalyzing the second step of methionine biosynthesis by direct sulfhydrylation

The primary function of metZ is to catalyze the **incorporation of sulfur** into the carbon skeleton of methionine. In the methionine-biosynthetic pathway, L-homoserine is first activated at its γ-hydroxyl by an acyltransferase — in *Pseudomonas*, **MetA (O-succinylhomoserine synthase)** — to produce **O-succinyl-L-homoserine**. The metZ product then catalyzes the second step:

> **O-succinyl-L-homoserine + HS⁻ → L-homocysteine + succinate** (EC 2.5.1.-)

This is a **direct sulfhydrylation** reaction: inorganic sulfide is incorporated in a single step, in contrast to the transsulfuration route in which cysteine sulfur is transferred via a cystathionine intermediate. The founding study of *metZ* in *P. aeruginosa* stated explicitly that "the second step is achieved by direct sulfhydrylation, involving the enzyme encoded by a metZ gene that we have identified and sequenced," and further noted that "*Pseudomonas* appears to be the only organism so far described that uses O-succinylhomoserine as substrate for a direct sulfhydrylation" [PMID: 7704274](https://pubmed.ncbi.nlm.nih.gov/7704274/). This latter point is the defining substrate-specificity feature of MetZ: most direct-sulfhydrylation organisms (e.g., *Corynebacterium*, *Leptospira*) use the **acetyl** ester via an O-acetylhomoserine sulfhydrylase (MetY), whereas *Pseudomonas* MetZ acts on the **succinyl** ester.

Genetic loss-of-function evidence anchors the enzymatic assignment. In the orthologous *R. etli* system, a *metZ* mutant "showed undetectable levels of O-succinylhomoserine sulfhydrylase activity," was a methionine auxotroph, and the cloned *R. etli metZ* gene complemented a *P. aeruginosa metZ* mutant [PMID: 9885190](https://pubmed.ncbi.nlm.nih.gov/9885190/). This directly links the *metZ* gene product to the biochemical activity and to the physiological requirement for methionine.

Because *P. putida* PP_2001 is a syntenic *Pseudomonas* ortholog of the characterized *P. aeruginosa metZ*, carries the HAMAP MetZ rule signature (MF_02056), and possesses the diagnostic InterPro domains (IPR006234, O-succinylhomoserine sulfhydrylase; IPR000277, Cys/Met-metabolism PLP-dependent enzyme), the enzymatic function transfers with high confidence.

### Finding 2 — Direct sulfhydrylation of O-succinylhomoserine is the *primary* methionine route in *P. putida*

Beyond identifying the enzyme, the biological importance of metZ is that it drives the **principal** route to homocysteine (and hence methionine) in *P. putida*. Vermeij & Kertesz directly examined assimilative sulfur metabolism in *P. putida* S-313 (and *P. aeruginosa* PAO1) and found that "both these organisms used direct sulfhydrylation of O-succinylhomoserine for the synthesis of methionine" [PMID: 10482527](https://pubmed.ncbi.nlm.nih.gov/10482527/). Critically, the same study showed that the alternative transsulfuration enzymes — cystathionine γ-synthase and cystathionine β-lyase — "were expressed at low levels in both pseudomonads but were strongly upregulated during growth with cysteine as the sole sulfur source." This establishes a clear hierarchy: **direct sulfhydrylation (metZ) is the default, primary pathway**, while transsulfuration serves as a minor, condition-specific (cysteine-inducible) alternative. *P. putida* also lacks a reverse transsulfuration (cystathionine γ-lyase) pathway, further concentrating homocysteine biosynthesis through the metZ-dependent direct route.

This physiological context matters for annotation quality: it distinguishes metZ from a redundant or auxiliary activity and identifies it as the committed sulfur-fixing enzyme of methionine biosynthesis under standard (sulfate/sulfide) growth conditions. Loss of metZ activity produces **methionine auxotrophy** in orthologous systems (*R. etli*, *P. aeruginosa* mutants), confirming its essential role for methionine prototrophy when methionine/homocysteine are not supplied exogenously.

### Finding 3 — metZ is a soluble cytoplasmic PLP-dependent enzyme of the Cys/Met-metabolism γ-family

metZ belongs to the **trans-sulfuration enzymes family (MetZ subfamily)** and contains the **Cys/Met-metabolism pyridoxal-phosphate-dependent enzyme domain** (InterPro IPR000277), together with the fold-type I PLP transferase domains (IPR015421, IPR015424). Enzymes of this family are **soluble cytoplasmic** proteins that carry out sulfur-amino-acid metabolism in the cytosol; there is no signal peptide, transmembrane segment, or export signal implied by the family or by the sequence annotation, so the enzyme performs its function **inside the cell, in the cytoplasm**. Its substrates (O-succinylhomoserine, sulfide) and product (homocysteine) are all cytoplasmic metabolites.

The structural classification is supported by the crystal structure of the homologous **O-acetylhomoserine sulfhydrylase (MetY)** from *Wolinella succinogenes*, a "pyridoxal 5′-phosphate (PLP) dependent sulfide-utilizing enzyme" [PMID: 21931214](https://pubmed.ncbi.nlm.nih.gov/21931214/). That work reported that "MetY has the same fold as cystathionine γ-lyase and methionine γ-lyase," placing the sulfhydrylases firmly in the **γ-elimination/replacement subclass** of PLP enzymes. These enzymes are typically homotetramers with the PLP cofactor bound at each active site. By homology, metZ is expected to adopt the same fold and quaternary organization and to operate as a cytoplasmic PLP-dependent γ-replacement catalyst.

### Finding 4 — Substrate specificity for the succinyl ester is set by active-site loop architecture; catalysis uses a PLP–lysine Schiff base

Two mechanistic features complete the functional picture. First, **catalysis**: in the Cys/Met γ-family, the PLP cofactor is covalently anchored to a conserved active-site lysine through a **Schiff base (internal aldimine)**. In *Corynebacterium glutamicum* cystathionine γ-synthase (MetB), "the pyridoxal phosphate cofactor is covalently bound to Lys204 via a Schiff base linkage in the deep cavity" [PMID: 28675039](https://pubmed.ncbi.nlm.nih.gov/28675039/). The incoming amino-acid substrate transaldiminates with this internal aldimine to form an external aldimine, after which γ-proton abstraction and elimination of the acyl leaving group generate a reactive PLP-bound intermediate that is attacked by the sulfur nucleophile — here, sulfide — to yield homocysteine. metZ possesses the corresponding conserved catalytic lysine and PLP-binding residues (HAMAP rule MF_02056 defines the PLP-binding lysine).

Second, **substrate discrimination**: the same structural work established that "the conformation of the β10–β11 connecting loops determines the size and shape of the acetyl- or succinyl-group binding site and ultimately determines the substrate specificity of MetBs toward OAHS or OSHS" [PMID: 28675039](https://pubmed.ncbi.nlm.nih.gov/28675039/). This provides the structural rationale for why MetZ prefers the bulkier **O-succinylhomoserine** substrate: its acyl-binding pocket is shaped to accommodate the four-carbon succinyl leaving group. Quantitative support that γ-family enzymes bind and turn over O-succinylhomoserine comes from *Helicobacter pylori* cystathionine γ-synthase, for which "the K(m) and k(cat)/K(m) values against the substrate O-succinyl-L-homoserine (L-OSHS) were 3.02 mM" [PMID: 17981822](https://pubmed.ncbi.nlm.nih.gov/17981822/), confirming millimolar-range affinity for the succinyl ester in this enzyme class.

---

## Mechanistic Model / Interpretation

### Pathway placement

metZ operates at the **sulfur-incorporation branch point** of methionine biosynthesis in *P. putida*:

```
  L-aspartate
      │  (aspartokinase, ASD, homoserine dehydrogenase)
      ▼
  L-homoserine
      │  MetA (homoserine O-succinyltransferase)
      │  + succinyl-CoA
      ▼
  O-succinyl-L-homoserine ─────────────────────────────┐
      │                                                 │
      │  ★ MetZ (PP_2001)  ← THIS ENZYME                │ (minor, cysteine-inducible
      │  + HS⁻ (inorganic sulfide)                      │  transsulfuration branch:
      │  → succinate                                    │  cystathionine γ-synthase
      ▼   DIRECT SULFHYDRYLATION (primary route)         │  + L-cysteine → cystathionine
  L-homocysteine  ◄─────────────────────────────────────┘  → cystathionine β-lyase → homocysteine
      │  MetH / MetE (methionine synthase)
      │  + N5-methyl-THF
      ▼
  L-methionine
      │  MetK (SAM synthetase)
      ▼
  S-adenosylmethionine (SAM)
```

### Reaction catalyzed

| Feature | Value |
|---|---|
| **Substrate 1** | O-succinyl-L-homoserine |
| **Substrate 2** | Inorganic sulfide (HS⁻ / S²⁻) |
| **Product 1** | L-homocysteine |
| **Product 2** | Succinate |
| **Cofactor** | Pyridoxal-5′-phosphate (PLP) |
| **Reaction class** | γ-replacement (direct sulfhydrylation) |
| **EC** | 2.5.1.- (transferase; sulfhydrylase) |
| **Distinctive specificity** | Succinyl ester (vs. acetyl in MetY-type enzymes) |
| **Localization** | Cytoplasm (soluble homotetramer, by homology) |

### Catalytic cycle (γ-replacement)

```
 PLP–Lys (internal aldimine)
        │  + O-succinyl-L-homoserine
        ▼
 External aldimine (substrate–PLP)
        │  γ-proton abstraction
        ▼
 α,β/γ-unsaturated PLP intermediate  ──►  succinate released
        │  nucleophilic addition of HS⁻ at Cγ
        ▼
 L-homocysteine–PLP external aldimine
        │  transaldimination with Lys
        ▼
 PLP–Lys (regenerated) + L-homocysteine
```

### Interpretation

MetZ is best understood as *Pseudomonas*'s specialized, committed enzyme for **fixing inorganic sulfur into the methionine skeleton**. Its succinyl-ester specificity is the biochemical signature that separates the MetZ subfamily from the more widespread MetY (acetyl) sulfhydrylases and from the cystathionine γ-synthases (which use the same succinyl ester in *E. coli* but partner it with cysteine rather than sulfide). Comparative-genomics work suggests these enzymes share a common ancestor with broad homoserine-ester and sulfur-source promiscuity that later specialized — MetZ retaining the succinyl-substrate/direct-sulfhydrylation phenotype in *Pseudomonas* and related Proteobacteria. In *P. putida* specifically, the dominance of metZ over transsulfuration means that this single enzyme carries the bulk of *de novo* homocysteine flux, making it functionally essential for methionine prototrophy in the absence of exogenous methionine.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [7704274](https://pubmed.ncbi.nlm.nih.gov/7704274/) | *A direct sulfhydrylation pathway is used for Met biosynthesis in P. aeruginosa* | **Primary** — defines metZ as the O-succinylhomoserine sulfhydrylase performing step 2; establishes succinyl-substrate specificity unique to *Pseudomonas*. Supports Findings 1, 2. |
| [9885190](https://pubmed.ncbi.nlm.nih.gov/9885190/) | *The R. etli metZ gene is essential for Met biosynthesis and nodulation* | **Primary/genetic** — metZ mutant lacks OSHS activity and is a Met auxotroph; cross-complements a P. aeruginosa metZ mutant. Supports Finding 1. |
| [10482527](https://pubmed.ncbi.nlm.nih.gov/10482527/) | *Pathways of assimilative sulfur metabolism in P. putida* | **Primary (in-organism)** — shows *P. putida* uses direct sulfhydrylation of OSH as primary Met route; transsulfuration low/cysteine-inducible. Supports Finding 2. |
| [21931214](https://pubmed.ncbi.nlm.nih.gov/21931214/) | *Novel sulfur transfer by O-acetylhomoserine sulfhydrylase, W. succinogenes* | **Structural (homolog)** — PLP-dependent sulfide-utilizing enzyme; same fold as cystathionine γ-lyase/methionine γ-lyase. Supports Finding 3. |
| [28675039](https://pubmed.ncbi.nlm.nih.gov/28675039/) | *Structural insights into substrate specificity of C. glutamicum CGS* | **Structural (family)** — PLP–Lys204 Schiff base; β10–β11 loop sets acetyl vs succinyl specificity. Supports Finding 4. |
| [17981822](https://pubmed.ncbi.nlm.nih.gov/17981822/) | *Cystathionine γ-synthase from H. pylori* | **Kinetic (family)** — Km(OSHS) = 3.02 mM, quantifying succinyl-ester turnover in this enzyme class. Supports Finding 4. |
| [12832650](https://pubmed.ncbi.nlm.nih.gov/12832650/) | *In vivo substrates of CGS and OAH sulfhydrylase* | **Context** — multisubstrate promiscuity and evolutionary origins of homoserine-ester sulfhydrylases. Supports Findings 1, 4. |
| [11844756](https://pubmed.ncbi.nlm.nih.gov/11844756/) | *C. glutamicum uses both transsulfuration and direct sulfhydrylation* | **Context** — metY (OAH sulfhydrylase) as the direct-sulfhydrylation paradigm; parallel-pathway logic. Supports Finding 2. |
| [12845493](https://pubmed.ncbi.nlm.nih.gov/12845493/) | *Met biosynthesis and regulation in C. glutamicum* | **Context** — direct sulfhydrylation vs. transsulfuration distinction and regulation. Supports Finding 2. |
| [15581575](https://pubmed.ncbi.nlm.nih.gov/15581575/) | *Enzymology of cystathionine biosynthesis (review)* | **Review** — control of reaction/substrate specificity in PLP γ-family enzymes. Supports Finding 4. |

### How the evidence fits together

The assignment for Q88LD4 is **inferred by strong orthology plus in-organism physiology**, not by a dedicated study of the PP_2001 protein itself. The *P. aeruginosa metZ* characterization [PMID: 7704274] provides the direct gene→enzyme→reaction link within the same genus; the *P. putida* sulfur-metabolism study [PMID: 10482527] confirms that *P. putida* actually runs this pathway as its primary route; the *R. etli* genetics [PMID: 9885190] supplies orthogonal loss-of-function proof of the enzyme identity. The structural and kinetic papers from related γ-family enzymes [PMID: 21931214, 28675039, 17981822] supply the mechanistic and specificity detail (PLP–Lys Schiff base, γ-replacement chemistry, succinyl-loop specificity, cytoplasmic soluble fold) that could not be obtained from *P. putida* MetZ directly. No paper in the reviewed set contradicts the annotation.

### Supported and refuted hypotheses

| Hypothesis | Status | Basis |
|---|---|---|
| metZ (Q88LD4) is O-succinylhomoserine sulfhydrylase | **Supported** | PMID 7704274, 9885190; UniProt/InterPro family |
| It catalyzes OSH + sulfide → homocysteine + succinate (direct sulfhydrylation, 2nd Met step) | **Supported** | PMID 7704274 |
| Direct sulfhydrylation of OSH is the primary Met route in *P. putida* | **Supported** | PMID 10482527 (S-313 strain) |
| Enzyme is PLP-dependent, γ-subclass, tetrameric, cytoplasmic | **Supported (by homology)** | PMID 21931214, 28675039 |
| *P. putida* uses O-acetylhomoserine (not succinyl) for sulfhydrylation | **Refuted** | PMID 7704274, 10482527: substrate is O-succinylhomoserine |
| Methionine synthesis in *P. putida* relies mainly on transsulfuration/cystathionine | **Refuted** | PMID 10482527: transsulfuration low/inducible; no reverse transsulfuration |

---

## Limitations and Knowledge Gaps

1. **No dedicated study of PP_2001/Q88LD4 itself.** All enzymatic evidence is by orthology (*P. aeruginosa* metZ, *R. etli* metZ, *P. putida* strain S-313) and family inference. The specific KT2440 protein has not, in the reviewed literature, been purified, crystallized, or kinetically characterized. Its Km, kcat, and substrate/sulfur-donor preferences are predicted, not measured.

2. **Sulfur donor identity in vivo.** Direct sulfhydrylation formally uses HS⁻/sulfide, but some γ-family enzymes accept alternative thiols. The exact physiological sulfur nucleophile used by *P. putida* MetZ across growth conditions has not been resolved here.

3. **Structural specificity residues not mapped in MetZ.** The β10–β11 acyl-binding loop determinant is documented for CGS/MetY-type enzymes; the corresponding residues in *P. putida* MetZ have not been individually verified by mutagenesis or structure. No experimental 3D structure of a *Pseudomonas* OSH-specific MetZ was found.

4. **Regulation.** Methionine-mediated repression and sulfur-source control are documented in other organisms (e.g., *C. glutamicum*, and induction by sulfate/thiosulfate in *R. etli*), but the precise regulators of PP_2001 (e.g., CysB/sulfate regulon, MetR-type control) were not established for *P. putida* in the reviewed set.

5. **Localization is inferred.** Cytoplasmic localization is by family analogy and absence of export signals, not by experimental fractionation of *P. putida* MetZ.

6. **Essentiality.** Methionine auxotrophy upon loss is demonstrated in orthologs (*R. etli*) and implied by pathway dominance in *P. putida*, but a clean *P. putida* KT2440 ΔPP_2001 phenotype was not directly cited here.

7. **Possible secondary activity.** Some family members show cystathionine γ-synthase-like promiscuity [PMID: 12832650]; whether MetZ has any secondary activity is untested.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant enzymology.** Overexpress and purify *P. putida* KT2440 MetZ (His-tag), confirm PLP content (A₄₂₀ spectrum), and measure steady-state kinetics for O-succinyl-L-homoserine + sulfide → homocysteine + succinate. Directly compare Km/kcat for O-succinyl- vs O-acetyl-homoserine to quantify the succinyl preference.

2. **Sulfur-donor panel.** Assay the purified enzyme with Na₂S, cysteine, methanethiol, and thiosulfate to define the physiological nucleophile and any promiscuity.

3. **Targeted genetics.** Construct a *P. putida* KT2440 ΔPP_2001 mutant and test for methionine auxotrophy on minimal sulfate/sulfide medium; complement with wild-type and catalytic-lysine (Schiff-base) point mutants to confirm the active-site residue.

4. **Structure determination / AlphaFold validation.** Solve or model the MetZ structure and map the β10–β11 acyl-binding loop; use it to design point mutations that switch succinyl↔acetyl specificity, testing the loop-architecture hypothesis directly in MetZ.

5. **Regulation.** Measure metZ (PP_2001) transcript/protein levels across sulfur sources (sulfate, cysteine, methionine) and identify the transcriptional regulator, to establish whether, as in *C. glutamicum*, methionine represses the direct-sulfhydrylation route.

6. **Flux confirmation.** Use ³⁴S/³⁵S labeling to demonstrate direct incorporation of inorganic sulfide into homocysteine via MetZ in vivo, and quantify the metZ vs. transsulfuration flux split under standard growth.

---

## References

- Foglino M, et al. (1995) A direct sulfhydrylation pathway is used for methionine biosynthesis in *Pseudomonas aeruginosa*. [PMID: 7704274](https://pubmed.ncbi.nlm.nih.gov/7704274/)
- Vermeij P, Kertesz MA (1999) Pathways of assimilative sulfur metabolism in *Pseudomonas putida*. [PMID: 10482527](https://pubmed.ncbi.nlm.nih.gov/10482527/)
- Taté R, et al. (1999) The *Rhizobium etli* metZ gene is essential for methionine biosynthesis and nodulation of *Phaseolus vulgaris*. [PMID: 9885190](https://pubmed.ncbi.nlm.nih.gov/9885190/)
- Tran TH, et al. (2011) A novel mechanism of sulfur transfer catalyzed by O-acetylhomoserine sulfhydrylase in *Wolinella succinogenes*. [PMID: 21931214](https://pubmed.ncbi.nlm.nih.gov/21931214/)
- Sagong HY, Kim KJ (2017) Structural insights into substrate specificity of cystathionine γ-synthase from *Corynebacterium glutamicum*. [PMID: 28675039](https://pubmed.ncbi.nlm.nih.gov/28675039/)
- Kong Y, et al. (2008) Enzymatic characterization and inhibitor discovery of a new cystathionine γ-synthase from *Helicobacter pylori*. [PMID: 17981822](https://pubmed.ncbi.nlm.nih.gov/17981822/)
- Hacham Y, et al. (2003) In vivo analysis of various substrates utilized by cystathionine γ-synthase and O-acetylhomoserine sulfhydrylase in methionine biosynthesis. [PMID: 12832650](https://pubmed.ncbi.nlm.nih.gov/12832650/)
- Hwang BJ, et al. (2002) *Corynebacterium glutamicum* utilizes both transsulfuration and direct sulfhydrylation pathways for methionine biosynthesis. [PMID: 11844756](https://pubmed.ncbi.nlm.nih.gov/11844756/)
- Lee HS, Hwang BJ (2003) Methionine biosynthesis and its regulation in *Corynebacterium glutamicum*. [PMID: 12845493](https://pubmed.ncbi.nlm.nih.gov/12845493/)
- Aitken SM, Kirsch JF (2005) The enzymology of cystathionine biosynthesis. [PMID: 15581575](https://pubmed.ncbi.nlm.nih.gov/15581575/)


## Artifacts

- [OpenScientist final report](metZ-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](metZ-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:7704274
2. PMID:10482527
3. PMID:9885190
4. PMID:21931214
5. PMID:28675039
6. PMID:17981822
7. PMID:12832650
8. PMID:11844756
9. PMID:12845493
10. PMID:15581575