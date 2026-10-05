---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-11T06:45:38.944271'
end_time: '2026-08-11T07:39:55.406894'
duration_seconds: 3256.46
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: alr
  gene_symbol: alr
  uniprot_accession: Q88GJ9
  protein_description: 'RecName: Full=Broad specificity amino-acid racemase {ECO:0000255|HAMAP-Rule:MF_02212,
    ECO:0000305|PubMed:30008699}; EC=5.1.1.10 {ECO:0000255|HAMAP-Rule:MF_02212, ECO:0000269|PubMed:23995642};
    AltName: Full=Broad spectrum racemase {ECO:0000303|PubMed:30008699}; Flags: Precursor;'
  gene_info: Name=alr {ECO:0000303|PubMed:23995642, ECO:0000312|EMBL:AAN69319.1};
    OrderedLocusNames=PP_3722 {ECO:0000312|EMBL:AAN69319.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the alanine racemase family. Bsr subfamily.
  protein_domains: Ala_racemase. (IPR000821); Ala_racemase/Decarboxylase_C. (IPR009006);
    Ala_racemase_C. (IPR011079); Ala_racemase_N. (IPR001608); Ala_racemase_pyridoxalP-BS.
    (IPR020622)
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
  path: alr-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: alr-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88GJ9
- **Protein Description:** RecName: Full=Broad specificity amino-acid racemase {ECO:0000255|HAMAP-Rule:MF_02212, ECO:0000305|PubMed:30008699}; EC=5.1.1.10 {ECO:0000255|HAMAP-Rule:MF_02212, ECO:0000269|PubMed:23995642}; AltName: Full=Broad spectrum racemase {ECO:0000303|PubMed:30008699}; Flags: Precursor;
- **Gene Information:** Name=alr {ECO:0000303|PubMed:23995642, ECO:0000312|EMBL:AAN69319.1}; OrderedLocusNames=PP_3722 {ECO:0000312|EMBL:AAN69319.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the alanine racemase family. Bsr subfamily.
- **Key Domains:** Ala_racemase. (IPR000821); Ala_racemase/Decarboxylase_C. (IPR009006); Ala_racemase_C. (IPR011079); Ala_racemase_N. (IPR001608); Ala_racemase_pyridoxalP-BS. (IPR020622)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "alr" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'alr' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **alr** (gene ID: alr, UniProt: Q88GJ9) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: Alr — Broad-Specificity Amino-Acid Racemase (Q88GJ9, PP_3722) of *Pseudomonas putida* KT2440

## Summary

The gene **alr** (locus tag **PP_3722**; UniProt **Q88GJ9**) of *Pseudomonas putida* strain KT2440 encodes a **pyridoxal-5′-phosphate (PLP)-dependent, broad-specificity amino-acid racemase** (EC 5.1.1.10). Despite its historical name — "alr" for *alanine racemase* — this enzyme is **not** a housekeeping alanine racemase for peptidoglycan biosynthesis. It belongs to the alanine-racemase structural family but to a distinct functional subfamily (the **Bsr / broad-spectrum racemase subfamily**), and its defining biochemical property is that it reversibly interconverts the L- and D-enantiomers of a wide range of α-amino acids while **kinetically preferring the basic amino acids lysine and arginine**. In vitro, the catalytic efficiency (*k*cat/*K*m) toward lysine is roughly three orders of magnitude greater than toward alanine, firmly establishing that alanine is a poor physiological substrate and lysine/arginine are the preferred ones.

The **primary physiological function** of Alr is **catabolic, not biosynthetic**. By generating D-lysine (and D-arginine) from their L-enantiomers, Alr feeds the D-lysine degradation pathway (D-lysine → Δ¹-piperideine-2-carboxylate → L-pipecolate → α-aminoadipate), enabling *P. putida* KT2440 to use L-Lys and L-Arg as sole sources of carbon and nitrogen. This catabolic role is supported by direct experimental evidence: cellular fractionation localizes Alr activity to the **periplasm**; a Δ*alr* knockout is specifically impaired in catabolism of L-Lys and L-Arg; the knockout's peptidoglycan is structurally unchanged (ruling out a cell-wall role); and RNA-seq differential expression between wild-type and Δ*alr* is confined to amino-acid-metabolism genes. The enzyme's specific activity peaks during exponential growth and correlates with accumulation of D-Lys in the medium.

Structurally, Alr adopts the canonical **alanine-racemase fold**: a head-to-tail homodimer in which each protomer contributes an N-terminal (α/β)₈ TIM-barrel and a C-terminal β-stranded domain, with a **two-base active site at the dimer interface**. The catalytic apparatus is the conserved dyad **Lys75** (which forms the internal aldimine with PLP) and **Tyr301** (the second catalytic base from the partner protomer), assisted by **Arg174**, which orients the cofactor. The protein is synthesized as a **precursor with a cleavable N-terminal signal peptide** (residues 1–24) that targets it to the periplasm, and it carries a **disulfide bond (Cys71–Cys97)** consistent with the oxidizing periplasmic environment.

---

## Gene / Protein Identity Verification

Before presenting findings, the identity of the target was verified against the UniProt record and the primary literature. The verification **passes cleanly** — this is not a case of gene-symbol ambiguity.

| Attribute | Expected (UniProt Q88GJ9) | Found in literature | Match |
|---|---|---|---|
| Gene symbol | *alr* | *alr* / "Alr" used in Radkov & Moe 2013, 2018 | ✔ |
| Locus tag | PP_3722 | PP_3722 (KT2440 genome) | ✔ |
| Organism | *P. putida* KT2440 (ATCC 47054 / DSM 6125) | *P. putida* KT2440 | ✔ |
| EC number | 5.1.1.10 | 5.1.1.10 (broad-specificity amino-acid racemase) | ✔ |
| Family | Alanine racemase family, Bsr subfamily | Alanine-racemase fold; broad-spectrum racemase | ✔ |
| Domains | Ala_racemase_N/C, PLP-binding site | Confirmed by sequence inspection | ✔ |

The name "alr" is a misnomer in the sense that the enzyme is not the peptidoglycan alanine racemase; nevertheless, all identifiers (gene symbol, locus tag, organism, accession) are internally consistent, and the primary papers [PMID: 23995642](https://pubmed.ncbi.nlm.nih.gov/23995642/) and [PMID: 30008699](https://pubmed.ncbi.nlm.nih.gov/30008699/) study exactly this protein. Research therefore proceeds with high confidence.

---

## Key Findings

### Finding 1 — Alr is a PLP-dependent broad-specificity amino-acid racemase that kinetically prefers lysine and arginine

Alr catalyzes the general reaction **L-α-amino acid ⇌ D-α-amino acid** (EC 5.1.1.10) using **pyridoxal-5′-phosphate** covalently bound as an internal aldimine to **Lys75**. The direct biochemical characterization by Radkov & Moe ([PMID: 23995642](https://pubmed.ncbi.nlm.nih.gov/23995642/)) demonstrated that the enzyme has genuinely broad substrate specificity, showing measurable racemase activity with **9 of the 19 chiral amino acids** tested. Crucially, activity was **highest with lysine**, and the *k*cat/*K*m values for both L- and D-lysine were **three orders of magnitude greater** than for L- and D-alanine.

The quantitative kinetics make the substrate preference unambiguous:

| Substrate | *k*cat (s⁻¹) | *K*m (mM) | Note |
|---|---|---|---|
| L-Lys | 1681.7 | 8.96 | Preferred substrate; highest *k*cat |
| D-Lys | 274.5 | 0.36 | Tight binding (low *K*m) |
| L-Ala | 7.33 | 12.62 | ~10³-fold lower *k*cat/*K*m than Lys |
| D-Ala | 8.83 | 15.71 | ~10³-fold lower *k*cat/*K*m than Lys |

The very high *k*cat for L-Lys (1681.7 s⁻¹) combined with a millimolar *K*m yields a catalytic efficiency dramatically exceeding that for alanine. Note also that D-Lys has a markedly lower *K*m (0.36 mM), indicating tight binding of the D-enantiomer. This finding establishes the enzyme's identity as a **broad-spectrum racemase with a basic-amino-acid preference**, decisively separating it functionally from a classical biosynthetic alanine racemase.

> *Supporting quote* ([PMID: 23995642](https://pubmed.ncbi.nlm.nih.gov/23995642/)): "The putative biosynthetic alanine racemase Alr showed broad substrate specificity, exhibiting measurable racemase activity with 9 of the 19 chiral amino acids. Among these amino acids, activity was the highest with lysine, and the k(cat)/K(m) values with l- and d-lysine were 3 orders of magnitude greater than the k(cat)/K(m) values with l- and d-alanine."

### Finding 2 — The primary physiological role of Alr is catabolism of basic amino acids, enabling growth on L-Lys and L-Arg

The UniProt FUNCTION annotation (derived from [PMID: 30008699](https://pubmed.ncbi.nlm.nih.gov/30008699/)) states that Alr "plays a primary role in the catabolism of basic amino acid, that allows *P. putida* strain KT2440 to grow on L-Lys and L-Arg as the sole source of carbon and nitrogen, through conversion to their respective D-enantiomers." The **physiologically relevant direction is L → D** for lysine and arginine.

This role fits the established metabolic logic of *P. putida*. The organism catabolizes the **D-stereoisomers** of lysine, phenylalanine, arginine, alanine, and hydroxyproline as sole carbon and nitrogen sources ([PMID: 23995642](https://pubmed.ncbi.nlm.nih.gov/23995642/)). To exploit the far more abundant **L-lysine** available in the environment, the cell must first racemize L-Lys to D-Lys, which is precisely the reaction Alr performs. The downstream **D-lysine catabolic pathway** is well established from classical *Pseudomonas* biochemistry: D-lysine is converted to **Δ¹-piperideine-2-carboxylate** (via D-lysine dehydrogenase/aminotransferase activities, e.g., *amaD*/PP_3596 and *amaC*/PP_3590), then reduced to **L-pipecolate**, and further oxidized toward **α-aminoadipate** ([PMID: 17259313](https://pubmed.ncbi.nlm.nih.gov/17259313/); [PMID: 4359655](https://pubmed.ncbi.nlm.nih.gov/4359655/)).

> *Supporting quotes*:
> — ([PMID: 23995642](https://pubmed.ncbi.nlm.nih.gov/23995642/)): "P. putida KT2440 catabolized the d-stereoisomers of lysine, phenylalanine, arginine, alanine, and hydroxyproline as the sole carbon and nitrogen sources."
> — ([PMID: 17259313](https://pubmed.ncbi.nlm.nih.gov/17259313/)): "l-lysine is racemized to d-lysine, and l-pipecolate and alpha-aminoadipate are the key metabolites."

An important historical nuance: an earlier study ([PMID: 4359655](https://pubmed.ncbi.nlm.nih.gov/4359655/)) using a different *P. putida* strain concluded that a detectable lysine racemase was "not physiologically functional in intact cells at a rate that would permit growth." The modern work on KT2440's Alr resolves this by demonstrating a genuine, growth-supporting catabolic racemase, likely reflecting strain differences and the periplasmic localization of Alr (see Finding 3).

### Finding 3 — Alr is a periplasmic enzyme synthesized with a cleavable N-terminal signal peptide

UniProt Q88GJ9 is a **409-amino-acid precursor** with a **signal peptide spanning residues 1–24** (the sequence begins MPFRRTLLAASLALLITGQAPLYA…, a classic Sec-type signal with a positively charged n-region, hydrophobic h-region, and cleavage site). Cleavage yields the **mature chain (residues 25–409)**. The subcellular location is annotated as **Periplasm** (experimental evidence, ECO:0000269, from [PMID: 30008699](https://pubmed.ncbi.nlm.nih.gov/30008699/); HAMAP rule MF_02212).

A **disulfide bond between Cys71 and Cys97** is present in the mature protein. Disulfide bonds are characteristic of proteins folded in the oxidizing periplasm (they are generally not formed in the reducing cytoplasm), providing an independent structural signature consistent with periplasmic localization. Periplasmic localization is also **mechanistically sensible**: it positions the racemase to act on amino acids as they cross the outer membrane, generating D-enantiomers "at the gate" for subsequent transport and cytoplasmic catabolism, and it explains the observed accumulation of D-Lys in the growth medium.

### Finding 4 — Alr adopts the alanine-racemase fold: a head-to-tail PLP-dependent homodimer with a two-base active site at the dimer interface

The closely homologous broad-specificity racemase (BAR/Bar) from *P. putida* was crystallized ([PMID: 23118975](https://pubmed.ncbi.nlm.nih.gov/23118975/)), revealing "the similar fold of alanine racemase, which is a head-to-tail homodimer with each protomer containing an N-terminal (α/β)₈ barrel and a C-terminal β-stranded domain. The active-site residues are located at the protomer interface … a funnel-like cavity with two catalytic bases, one from each protomer, and the PLP binding site is at the bottom of this cavity."

Q88GJ9 conforms to this architecture. Its catalysis relies on **two catalytic proton-acceptor bases** — Lys75 and the Tyr301-region residue — one contributed by each protomer, so that a functional active site is formed only at the **dimer interface**. PLP is covalently bound to **Lys75** as an N6-(pyridoxal phosphate)lysine internal aldimine. The InterPro domain complement (Ala_racemase_N, IPR001608; Ala_racemase_C, IPR011079; PLP-binding site, IPR020622; plus IPR000821 and IPR009006) matches this two-domain design.

Substrate breadth in this enzyme family is governed by a small number of residues lining the substrate cavity. In the *P. putida* BAR homolog, **two residues on α-helix 10** shape the cavity and control specificity ([PMID: 23118975](https://pubmed.ncbi.nlm.nih.gov/23118975/)), and engineered substitutions at **Y396 and I384** were shown to alter substrate specificity (notably increasing activity toward tryptophan) ([PMID: 17028872](https://pubmed.ncbi.nlm.nih.gov/17028872/)). This explains how a single fold can accommodate the broad range of amino acids that Alr racemizes while retaining a lysine/arginine preference — the enlarged, funnel-like cavity accommodates the long, positively charged side chains of the basic amino acids.

> *Supporting quote* ([PMID: 23118975](https://pubmed.ncbi.nlm.nih.gov/23118975/)): "the similar fold of alanine racemase, which is a head-to-tail homodimer with each protomer containing an N-terminal (α/β)(2)(8) barrel and a C-terminal β-stranded domain. The active-site residues are located at the protomer interface that is a funnel-like cavity with two catalytic bases, one from each protomer, and the PLP binding site is at the bottom of this cavity."

### Finding 5 — Direct experimental evidence (fractionation, knockout, RNA-seq) confirms Alr is a periplasmic racemase dedicated to basic-amino-acid catabolism, not peptidoglycan

The most decisive study is Radkov & Moe 2018 ([PMID: 30008699](https://pubmed.ncbi.nlm.nih.gov/30008699/), *Front. Microbiol.* 9:1343), which combined multiple orthogonal approaches and, in each case, converged on the same conclusion:

1. **Cellular fractionation** localized Alr enzymatic activity to the **periplasm**, matching the predicted signal peptide.
2. **Specific activity was highest during exponential growth** and correlated with **accumulation of D-Lys in the growth medium**, tying enzyme expression to active catabolism.
3. A **Δ*alr* knockout** showed **unchanged stationary-phase peptidoglycan structure**, indicating that Alr's D-amino-acid products are **not incorporated into peptidoglycan** — a direct refutation of a cell-wall biosynthetic role.
4. **RNA-seq** differential expression between wild-type and Δ*alr* was **limited to amino-acid-metabolism genes**, consistent with a narrowly metabolic (not global/pleiotropic) function.
5. The **Δ*alr* strain had limited capacity to catabolize L-Lys and L-Arg** as sole carbon/nitrogen source — a loss-of-function phenotype that pins the catabolic role squarely on Alr.

> *Supporting quotes* ([PMID: 30008699](https://pubmed.ncbi.nlm.nih.gov/30008699/)):
> — "We demonstrate through cellular fractionation that Alr enzymatic activity is found in the periplasm, consistent with its putative periplasm targeting sequence."
> — "The stationary phase peptidoglycan structure did not differ between wild-type and Δalr strains, indicating that products resulting from Alr activity are not incorporated into peptidoglycan under these conditions."
> — "The Δalr strain exhibited a limited capacity for catabolism of l-Lys and l-Arg as the sole source of carbon and nitrogen."
> — "Specific activity of Alr is highest during exponential growth, and this activity corresponds with an increased accumulation of d-Lys in the growth medium."

### Finding 6 — Sequence-level verification of the catalytic residues Lys75/Tyr301 and the PLP-orienting Arg174

Direct inspection of the 409-residue Q88GJ9 sequence confirmed the UniProt-annotated functional residues at their expected positions: **position 75 = Lys** (the PLP internal-aldimine base; sequence context CAVL**K75**ADAYGH), **position 301 = Tyr** (the second catalytic base; context NTVG**Y301**DRTFTL), **position 174 = Arg**, and **position 349 = Met**, with **Cys71/Cys97** forming the disulfide. The **Lys75/Tyr301 pair** is the two-base catalytic dyad homologous to the **Lys39/Tyr265′ dyad of *Bacillus* alanine racemase**, and **Arg174** corresponds to the conserved arginine that hydrogen-bonds to and orients the PLP O3 atom in the homologous *P. putida* Bar structure ([PMID: 23118975](https://pubmed.ncbi.nlm.nih.gov/23118975/)). This provides an independent, sequence-based confirmation of the catalytic machinery inferred from homology.

---

## Mechanistic Model / Interpretation

### The two-base racemization mechanism

Alr uses the classical **PLP-dependent two-base racemization mechanism**. PLP is anchored to Lys75 as an internal aldimine (Schiff base). When an amino-acid substrate enters the funnel-shaped active site, it displaces Lys75 to form an external aldimine. The Cα–H proton is then abstracted from one face by one catalytic base and re-added to the opposite face by the second base, inverting the stereocenter:

```
        L-amino acid                       D-amino acid
             │                                  │
     (Cα–H on re face)                  (Cα–H on si face)
             │                                  │
   Lys75 base ──abstracts H──►  PLP-quinonoid  ◄──re-protonates── Tyr301' base
       (protomer A)          (planar carbanion)       (protomer B)
             \________________ dimer interface ________________/
                        PLP anchored at Lys75 (protomer A)
                        Arg174 orients PLP O3 / phosphate
```

Because the two bases sit on opposite faces of the planar quinonoid intermediate, the reaction is freely reversible and racemizes rather than epimerizes. A notable side reaction of broad-specificity racemases in this family is **nonstereospecific transamination**: the *P. putida* broad-specificity racemase can abstract the C-4′ hydrogen of the coenzyme nonstereospecifically and carry out overall transamination (e.g., between L-ornithine and α-ketoglutarate) as a minor "forced-error" activity ([PMID: 9461589](https://pubmed.ncbi.nlm.nih.gov/9461589/)). This underscores the relatively relaxed active-site geometry that also underlies the broad substrate range.

### Placement in the basic-amino-acid catabolic pathway

The following schematic situates Alr within the physiological pathway that allows *P. putida* KT2440 to grow on L-lysine:

```
   Environment / periplasm                         Cytoplasm
 ┌───────────────────────────┐        ┌────────────────────────────────────┐
 │  L-Lysine                 │        │                                    │
 │      │                    │        │                                    │
 │      ▼  ALR (PP_3722)     │        │                                    │
 │  D-Lysine ────────────────┼──import─► D-lysine dehydrogenase/            │
 │  (accumulates in medium)  │        │  aminotransferase (amaD/amaC)       │
 │                           │        │        │                           │
 │  (L-Arg ⇌ D-Arg likewise) │        │        ▼                           │
 └───────────────────────────┘        │  Δ¹-piperideine-2-carboxylate       │
                                       │        │ (P2C reductase, NADPH)     │
                                       │        ▼                           │
                                       │  L-pipecolate                       │
                                       │        │                           │
                                       │        ▼                           │
                                       │  α-aminoadipate ──► central metab.  │
                                       └────────────────────────────────────┘
```

Alr occupies the **committed entry step** that channels the abundant L-enantiomer into the D-specific degradation branch. Its **periplasmic** placement means racemization occurs before or concurrent with import, consistent with the observed extracellular/periplasmic accumulation of D-Lys. The downstream steps — Δ¹-piperideine-2-carboxylate reductase producing L-pipecolate ([PMID: 6801013](https://pubmed.ncbi.nlm.nih.gov/6801013/)), and the overall D-lysine → L-pipecolate → α-aminoadipate route ([PMID: 17259313](https://pubmed.ncbi.nlm.nih.gov/17259313/); [PMID: 4359655](https://pubmed.ncbi.nlm.nih.gov/4359655/)) — are classical *Pseudomonas* biochemistry.

### Why this is NOT a peptidoglycan enzyme

Two independent lines of evidence exclude a cell-wall role: (1) the Δ*alr* knockout is viable with **normal peptidoglycan** (a true biosynthetic alanine racemase would be essential or cause D-Ala auxotrophy/wall defects); and (2) the enzyme's kinetic preference is for lysine/arginine, with alanine being a ~10³-fold poorer substrate. *P. putida* almost certainly possesses a separate, dedicated biosynthetic D-alanine source for peptidoglycan; Alr is a **catabolic specialist**. This is the central interpretive correction to the misleading "alr/alanine racemase" gene name.

---

## Evidence Base

| PMID | Title (abbrev.) | Relevance | How it supports / challenges findings |
|---|---|---|---|
| [23995642](https://pubmed.ncbi.nlm.nih.gov/23995642/) | *Amino acid racemization in P. putida KT2440* | **Primary** | Biochemical characterization of the exact protein; broad specificity; lysine preference; ~10³-fold higher *k*cat/*K*m for Lys vs Ala. Supports Findings 1 & 2. |
| [30008699](https://pubmed.ncbi.nlm.nih.gov/30008699/) | *A Broad Spectrum Racemase in P. putida* | **Primary** | Fractionation → periplasm; Δ*alr* impaired in Lys/Arg catabolism; unchanged peptidoglycan; RNA-seq confined to amino-acid metabolism; D-Lys accumulation. Supports Findings 2, 3 & 5. |
| [23118975](https://pubmed.ncbi.nlm.nih.gov/23118975/) | *Crystal structures of lysine-preferred racemases* | **Structural (homolog)** | Head-to-tail homodimer, (α/β)₈ barrel + β-domain, interfacial two-base active site, PLP at cavity bottom; specificity residues on α-helix 10. Supports Findings 4 & 6. |
| [17028872](https://pubmed.ncbi.nlm.nih.gov/17028872/) | *Synthesis of DL-Trp by modified BAR* | Structure–function (homolog) | Mutations Y396/I384 alter substrate specificity, showing cavity residues tune breadth. Supports Finding 4. |
| [9461589](https://pubmed.ncbi.nlm.nih.gov/9461589/) | *Nonstereospecific transamination by broad-specificity racemases* | Mechanistic (homolog) | Shows the *P. putida* broad-specificity racemase performs nonstereospecific transamination as a side reaction. Supports mechanistic model. |
| [17259313](https://pubmed.ncbi.nlm.nih.gov/17259313/) | *Initial steps in D-lysine catabolism in P. putida* | Pathway | Establishes L-Lys → D-Lys → L-pipecolate → α-aminoadipate route that consumes Alr's product. Supports Finding 2. |
| [4359655](https://pubmed.ncbi.nlm.nih.gov/4359655/) | *D-lysine catabolic pathway in P. putida* | Pathway (historical) | Defines separate L- and D-lysine pathways; notes a racemase of ambiguous physiological role in an older strain. Contextualizes Finding 2. |
| [6801013](https://pubmed.ncbi.nlm.nih.gov/6801013/) | *Δ¹-piperideine-2-carboxylate reductase of P. putida* | Pathway (downstream) | Characterizes the reductase producing L-pipecolate. Supports pathway model. |
| [24752840](https://pubmed.ncbi.nlm.nih.gov/24752840/) | *Bacterial synthesis of D-amino acids* (review) | Context | Reviews racemase-mediated D-amino-acid synthesis and roles; frames Alr among bacterial racemases. |
| [17486655](https://pubmed.ncbi.nlm.nih.gov/17486655/) | *Model-based characterization of a P. putida racemase* | Biotech (homolog) | Confirms reversible Michaelis-Menten racemization kinetics for a broad-specificity P. putida racemase. |
| [28344038](https://pubmed.ncbi.nlm.nih.gov/28344038/) | *Isoleucine 2-epimerase fold-type I structure* | Comparative | Illustrates an alternative (fold-type I) broad-spectrum racemase; contrasts with Alr's alanine-racemase fold. |

**Weight of evidence:** The functional assignment rests on **two direct primary studies of the exact protein** ([PMID: 23995642](https://pubmed.ncbi.nlm.nih.gov/23995642/) for biochemistry; [PMID: 30008699](https://pubmed.ncbi.nlm.nih.gov/30008699/) for localization, knockout, and physiology), corroborated by structural work on a very close homolog and by decades of *Pseudomonas* lysine-catabolism biochemistry. This is a **strongly supported** annotation.

---

## Limitations and Knowledge Gaps

1. **No crystal structure of Q88GJ9 itself.** The fold and catalytic-residue assignments are inferred from the closely related *P. putida* BAR/lysine-preferred racemase ([PMID: 23118975](https://pubmed.ncbi.nlm.nih.gov/23118975/)) and from sequence-based residue mapping. A direct structure of Alr (ideally PLP- and substrate-bound) would confirm the geometry of the basic-amino-acid-binding cavity.

2. **Full kinetic panel incomplete.** Detailed *k*cat/*K*m values are established for Lys and Ala; arginine and the other seven active substrates are qualitatively "active" but not all fully quantified. The relative ranking of Arg vs Lys, and the physiological importance of the other substrates, remains partly open.

3. **Import/coupling to transport is inferred, not proven.** The model that periplasmic racemization is coupled to a specific D-amino-acid transporter for import into the cytoplasm is mechanistically reasonable but the specific transporter(s) have not been definitively linked to Alr in the reviewed literature.

4. **Regulation is only partly characterized.** Activity peaks in exponential phase and RNA-seq shows amino-acid-metabolism genes respond to *alr* loss, but the transcriptional regulators and inducers controlling *alr* expression were not deeply resolved here.

5. **Strain-dependence.** Older reports ([PMID: 4359655](https://pubmed.ncbi.nlm.nih.gov/4359655/)) described a racemase of little physiological consequence in a different *P. putida* strain, so quantitative catabolic contributions may vary between strains and growth conditions.

6. **Disulfide bond functional role unverified.** The Cys71–Cys97 disulfide is annotated and consistent with periplasmic folding, but its contribution to stability or activity has not been experimentally dissected.

---

## Proposed Follow-up Experiments / Actions

1. **Solve the Alr structure.** Determine a crystal or cryo-EM structure of Q88GJ9 with PLP and, ideally, a lysine/arginine substrate analog, to visualize the residues that select basic side chains and to confirm the Lys75/Tyr301/Arg174 arrangement at the dimer interface.

2. **Complete the substrate kinetic panel.** Measure *k*cat and *K*m for L-/D-Arg and the remaining active substrates under uniform conditions to rank substrate preference quantitatively and test whether Arg rivals Lys.

3. **Identify the D-lysine transporter.** Use transposon or targeted knockouts plus radiolabeled/D-Lys uptake assays to link periplasmic racemization to a specific inner-membrane transporter, closing the gap between D-Lys generation and cytoplasmic catabolism.

4. **Site-directed mutagenesis of catalytic and specificity residues.** Mutate Lys75, Tyr301, Arg174 (catalysis) and cavity-lining residues (specificity, analogous to Y396/I384 in the BAR homolog) to validate mechanism and re-engineer substrate preference.

5. **Dissect regulation.** Map the *alr* promoter and identify inducers (L-Lys, L-Arg, D-Lys?) and regulators via reporter assays and ChIP/RNA-seq to explain the exponential-phase activity peak.

6. **Test the disulfide.** Construct Cys71Ser/Cys97Ser variants and assay periplasmic folding, stability, and activity to determine the disulfide's role.

7. **Confirm metabolic flux.** Use ¹³C/¹⁵N-labeled L-Lys tracing in wild-type vs Δ*alr* to quantitatively confirm flux through the D-Lys → L-pipecolate → α-aminoadipate route.

---

## Conclusion

Alr (PP_3722, Q88GJ9) is a **periplasmic, PLP-dependent broad-specificity amino-acid racemase (EC 5.1.1.10)** of the alanine-racemase fold (Bsr subfamily) that reversibly interconverts L- and D-α-amino acids with a strong **kinetic preference for lysine and arginine** (~10³-fold higher catalytic efficiency for lysine than for alanine). Its **primary, experimentally validated function is catabolic**: by producing D-Lys (and D-Arg) in the periplasm, it feeds the D-lysine/L-pipecolate/α-aminoadipate degradation pathway, enabling *P. putida* KT2440 to grow on L-Lys and L-Arg as sole carbon and nitrogen sources. A Δ*alr* knockout is specifically impaired in this catabolism while retaining normal peptidoglycan, ruling out a cell-wall biosynthetic role and correcting the misleading "alanine racemase" name. Mechanistically, it uses a two-base racemization at a dimer-interface active site built from the catalytic dyad **Lys75/Tyr301** with **Arg174** orienting the PLP cofactor.


## Artifacts

- [OpenScientist final report](alr-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](alr-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:23995642
2. PMID:30008699
3. PMID:17259313
4. PMID:4359655
5. PMID:23118975
6. PMID:17028872
7. PMID:9461589
8. PMID:6801013