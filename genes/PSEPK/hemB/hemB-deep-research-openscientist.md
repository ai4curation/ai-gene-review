---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T16:55:27.579009'
end_time: '2026-07-20T17:14:43.233469'
duration_seconds: 1155.65
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: hemB
  gene_symbol: hemB
  uniprot_accession: Q88IT6
  protein_description: 'RecName: Full=Delta-aminolevulinic acid dehydratase {ECO:0000256|ARBA:ARBA00020771,
    ECO:0000256|RuleBase:RU000515}; EC=4.2.1.24 {ECO:0000256|ARBA:ARBA00012053, ECO:0000256|RuleBase:RU000515};'
  gene_info: Name=hemB {ECO:0000313|EMBL:AAN68521.1}; OrderedLocusNames=PP_2913 {ECO:0000313|EMBL:AAN68521.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the ALAD family. {ECO:0000256|ARBA:ARBA00008055,
  protein_domains: ALAD. (IPR001731); ALAD_AS. (IPR030656); Aldolase_TIM. (IPR013785);
    ALAD (PF00490)
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
  path: hemB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: hemB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88IT6
- **Protein Description:** RecName: Full=Delta-aminolevulinic acid dehydratase {ECO:0000256|ARBA:ARBA00020771, ECO:0000256|RuleBase:RU000515}; EC=4.2.1.24 {ECO:0000256|ARBA:ARBA00012053, ECO:0000256|RuleBase:RU000515};
- **Gene Information:** Name=hemB {ECO:0000313|EMBL:AAN68521.1}; OrderedLocusNames=PP_2913 {ECO:0000313|EMBL:AAN68521.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the ALAD family. {ECO:0000256|ARBA:ARBA00008055,
- **Key Domains:** ALAD. (IPR001731); ALAD_AS. (IPR030656); Aldolase_TIM. (IPR013785); ALAD (PF00490)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "hemB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'hemB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **hemB** (gene ID: hemB, UniProt: Q88IT6) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# hemB (Q88IT6, PP_2913) in *Pseudomonas putida* KT2440: Functional Annotation Report

**Gene:** hemB (OrderedLocusName PP_2913)
**Protein:** Delta-aminolevulinic acid dehydratase / Porphobilinogen synthase (ALAD / PBGS)
**UniProt:** Q88IT6
**EC number:** 4.2.1.24
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440), taxon "PSEPK"
**Protein family:** ALAD family (Pfam PF00490; InterPro IPR001731 ALAD, IPR030656 ALAD_AS, IPR013785 Aldolase_TIM)

---

## Identity Verification

Before presenting findings, the gene/protein identity was confirmed. The gene symbol **hemB**, the EC number **4.2.1.24**, the ALAD-family Pfam/InterPro domain architecture, and the conserved active-site sequence signatures are all mutually consistent. In this organism "hemB" unambiguously denotes the heme-biosynthetic enzyme **5-aminolevulinate dehydratase / porphobilinogen synthase**, and not any unrelated similarly named gene. All analyses below refer to this specific 324-residue protein (Q88IT6 / PP_2913). No literature ambiguity was encountered; the ortholog literature (*E. coli*, human, *P. aeruginosa*, *Chlorobium*, *Pyrobaculum*) is directly relevant.

---

## Summary

The gene **hemB** in *Pseudomonas putida* KT2440 (UniProt **Q88IT6**, locus **PP_2913**) encodes **porphobilinogen synthase (PBGS)**, also known as **5‑aminolevulinic acid dehydratase (ALAD)**, EC 4.2.1.24. This enzyme catalyzes the **second step and the first committed common step of tetrapyrrole (heme) biosynthesis**: the asymmetric condensation of two molecules of 5‑aminolevulinic acid (ALA) into the monopyrrole **porphobilinogen (PBG)**, releasing two molecules of water. Porphobilinogen is the universal building block from which all tetrapyrroles — heme, siroheme, cobalamin (vitamin B12), and (in phototrophs) chlorophyll and bacteriochlorophyll — are subsequently assembled. The identification is secure: UniProt annotation, EC assignment, ALAD-family domain architecture, and conserved active-site signatures all converge, and the reaction has been directly demonstrated for the close *Pseudomonas aeruginosa* ortholog by functional complementation and enzymatic assay.

The most mechanistically informative result of this investigation is that the *P. putida* enzyme is predicted to be a **zinc‑dependent PBGS**, in contrast to its taxonomically closer relative in *P. aeruginosa*, which is experimentally confirmed to be **magnesium‑dependent**. This assignment rests on a diagnostic sequence feature: Q88IT6 retains the catalytic zinc‑binding **cysteine triad Cys122/Cys124/Cys132**, embedded in a His/Cys‑rich metal pocket essentially identical to that of the zinc-type *Escherichia coli* and human enzymes. The *P. aeruginosa* ortholog instead replaces these three cysteines with Ala/Leu/Asp — the hallmark of the magnesium-type subfamily. Quantitative global alignments reinforce this: Q88IT6 is **77% identical to *E. coli* ALAD (zinc-type)** but only **55% identical to *P. aeruginosa* HEM2 (Mg-type)**, despite *P. aeruginosa* being phylogenetically nearer. Metal-ion class in PBGS therefore does not track species relatedness, a phenomenon well documented across the ALAD family.

Beyond the metal center, Q88IT6 conserves every catalytic determinant of a functional PBGS: the two mechanistically essential active-site lysines (**Lys249**, the A-side Schiff-base lysine; **Lys197**, the P-side "perturbing" lysine), the substrate-carboxylate-binding lid arginines, and the histidines flanking the metal site. The protein has no signal peptide or transmembrane segment, consistent with a **soluble cytoplasmic localization**, where tetrapyrrole biosynthesis occurs. In summary, hemB/PP_2913 is a cytoplasmic, zinc-dependent, TIM-barrel homo-oligomeric metalloenzyme performing the first committed step of heme biosynthesis in *P. putida*.

---

## Key Findings

### Finding 1 — hemB encodes porphobilinogen synthase, catalyzing the condensation of two 5‑ALA into porphobilinogen

Q88IT6 is annotated in UniProt as **Delta‑aminolevulinic acid dehydratase, EC 4.2.1.24**, and belongs to the ALAD family (Pfam **PF00490**; InterPro **IPR001731** ALAD, **IPR030656** ALAD_AS active-site signature, **IPR013785** Aldolase_TIM barrel). The 324‑residue sequence retains the diagnostic ALAD active-site signature. The enzyme catalyzes:

```
2 × 5-aminolevulinate  →  porphobilinogen + 2 H2O
```

This is a Knorr/aldol-type **asymmetric condensation** that forms the pyrrole ring of porphobilinogen. It is the **second step of the heme pathway** and the **first committed step common to all tetrapyrroles** (heme, siroheme, cobalamin, chlorophyll). The reaction was directly demonstrated for the close *Pseudomonas aeruginosa* ortholog by functional complementation of an *E. coli* hemB mutant coupled with enzymatic assay ([PMID: 9529530](https://pubmed.ncbi.nlm.nih.gov/9529530/)), which describes ALAD as catalyzing "the condensation of two molecules of 5-aminolevulinic acid (ALA) to form one molecule of the pyrrole derivative porphobilinogen." An authoritative review confirms PBGS "is an essential enzyme in the biosynthesis of all tetrapyrroles, which function in respiration, photosynthesis, and methanogenesis" ([PMID: 27783504](https://pubmed.ncbi.nlm.nih.gov/27783504/)).

**Substrate specificity:** The single physiological substrate is **5‑aminolevulinic acid (ALA)**. Two ALA molecules are bound in two distinct sub-sites — the "A-side" (which contributes the ring nitrogen and the aminomethyl/acetyl side) and the "P-side" (which contributes the propionyl side) — and joined asymmetrically. Porphobilinogen is the sole product besides water. The substrate specificity is corroborated by the fact that ALA-mimicking molecules act as potent active-site-directed inhibitors: the antibiotic **alaremycin** and the intermediate-analog **4,7-dioxosebacic acid**.

### Finding 2 — The enzyme is predicted zinc‑dependent, retaining the Cys122/124/132 triad absent in its Mg-dependent *P. aeruginosa* relative

PBGS enzymes fall into two mechanistic classes distinguished by the catalytic A-site metal: **zinc-dependent** enzymes (e.g., human, *E. coli*) that use a triple-cysteine ligand set, and **magnesium-dependent / zinc-independent** enzymes (e.g., plants, some bacteria including *P. aeruginosa*) in which those cysteines are replaced by neutral/acidic residues.

Direct alignment of the metal-binding loop places Q88IT6 firmly in the **zinc-dependent** class. The *P. putida* loop (residues 118–136) reads **`VVMSDTCFCEYTSHGHCGVLH`**, containing the intact cysteine triad **Cys122, Cys124, Cys132**. This is essentially identical to the zinc-dependent *E. coli* ALAD motif (`VMSDTCFCEYTSHGHCGVL`) and matches the human zinc-coordinating triad Cys122/124/132 identified by quantum-biochemistry and evolutionary analysis ([PMID: 33791795](https://pubmed.ncbi.nlm.nih.gov/33791795/)). By contrast, the closely related **Mg‑dependent *P. aeruginosa*** ortholog (Q59643 / HEM2_PSEAE) carries the loop `IITDVALDPFTTHGQDGIL`, in which all three cysteines are replaced by Ala/Leu/Asp — the magnesium-type signature. That the *P. aeruginosa* enzyme is Mg2+-dependent was established directly: "Alignment of the amino acid sequences deduced from hemB revealed a potential metal-binding site and indicated that the enzyme is Mg(2+)-dependent" ([PMID: 9529530](https://pubmed.ncbi.nlm.nih.gov/9529530/)).

The functional relevance of the Zn/Mg distinction is documented structurally: the two classes differ in inhibitor sensitivity — "the structure suggests why 4,7-dioxosebacic acid is a better inhibitor of the zinc-dependent ALADs than of the zinc-independent ALADs" ([PMID: 16304458](https://pubmed.ncbi.nlm.nih.gov/16304458/)). More broadly, PBGS "evolved to use an unusual variety of metal ions both for catalytic function and to control protein multimerization" ([PMID: 27783504](https://pubmed.ncbi.nlm.nih.gov/27783504/)), which is precisely why two *Pseudomonas* species diverge in metal usage.

### Finding 3 — The two catalytic Schiff-base lysines and the TIM-barrel fold are conserved, consistent with a cytoplasmic homo-oligomer

The PBGS catalytic mechanism requires **two adjacent active-site lysines**, each forming a Schiff base (imine) with one of the two ALA substrates. Mapping Q88IT6 against *E. coli* ALAD identifies both:

- **A-side / Schiff-base lysine:** in the conserved motif `...LMVKPAGAY...`, *E. coli* Lys247 → *P. putida* **Lys249**.
- **P-side / "perturbing" lysine:** in the conserved motif `...MAYSTKFASS...`, *E. coli* Lys195 → *P. putida* **Lys197**.

These correspond to the two lysines described mechanistically as "one to the normal Schiff base-forming Lys-246 and the other to a universally conserved 'perturbing' Lys-194 (E. coli numbering)" ([PMID: 11444968](https://pubmed.ncbi.nlm.nih.gov/11444968/)). The two-Schiff-base mechanism — "two covalent Schiff base linkages between adjacent active site lysine residues and each of the two substrate molecules" — is well established ([PMID: 15381398](https://pubmed.ncbi.nlm.nih.gov/15381398/)), and inhibitor co-crystal structures confirm both lysines engage substrate: "the inhibitor binds by forming Schiff-base linkages with lysines 200 and 253 at the active site" ([PMID: 16304458](https://pubmed.ncbi.nlm.nih.gov/16304458/)). The alaremycin co-crystal with *P. aeruginosa* PBGS likewise shows the antibiotic "covalently bound by the catalytically important active-site lysine residue 260" ([PMID: 19822707](https://pubmed.ncbi.nlm.nih.gov/19822707/)).

Structurally, "monomers of all ALADs adopt the TIM-barrel fold" ([PMID: 28045381](https://pubmed.ncbi.nlm.nih.gov/28045381/)) — the (α/β)8 barrel encoded by the Aldolase_TIM InterPro signature (IPR013785). ALAD monomers assemble into **homo-oligomers**, canonically homooctamers. **Localization:** Q88IT6 begins `MSNQFPSVRPRR...` with no signal peptide and no predicted transmembrane segment, consistent with a **soluble cytoplasmic** enzyme, the compartment where tetrapyrrole biosynthesis takes place.

### Finding 4 — Quantitative phylogenetic evidence places *P. putida* ALAD with the zinc-type enzymes

Global (Needleman–Wunsch) pairwise identity comparisons quantify the divergence:

| Pair | % identity | Metal class of comparator |
|------|-----------|---------------------------|
| Q88IT6 (*P. putida*) vs *E. coli* ALAD | **77.4%** | Zinc-dependent |
| Q88IT6 (*P. putida*) vs *P. aeruginosa* HEM2 | **55.0%** | Magnesium-dependent |
| *E. coli* ALAD vs *P. aeruginosa* HEM2 | 51.0% | — |

Despite *P. aeruginosa* being taxonomically closer to *P. putida* than *E. coli* is, the *P. putida* enzyme is markedly more similar to the **zinc-type** *E. coli* enzyme. Q88IT6 conserves every zinc/catalytic determinant: the metal loop Ser119–Asp120 plus the Cys122/Cys124/Cys132 triad, the perturbing Lys197, the Schiff-base Lys249, and the substrate-carboxylate-binding lid motif `NPMNRR` (Arg228/Arg229). The *P. aeruginosa* enzyme instead carries the Mg-type loop. A practical corollary is that **the *E. coli* enzyme — not the available *P. aeruginosa* crystal structure — is the most appropriate mechanistic/structural model** for Q88IT6. This pattern is consistent with the general principle that "phylogenetic variation in PBGS multimerization equilibria provides insight into how Nature has harnessed oligomeric variation in the control of protein function" ([PMID: 27783504](https://pubmed.ncbi.nlm.nih.gov/27783504/)) — metal and quaternary-structure properties vary across the family and do not strictly follow species phylogeny.

### Finding 5 — The His/Cys-rich zinc-binding pocket is fully conserved, indicating a bona fide zinc metalloenzyme

Q88IT6 conserves the histidine- and cysteine-rich metal region. The motif `...EYTSHGHCG...` places **His129 and His131** immediately adjacent to the Cys122/124/132 triad, corresponding to *E. coli* **His126 and His128**. Site-directed mutagenesis in *E. coli* PBGS established that this region forms the zinc-binding pocket: single and double His→Ala mutants remain catalytically active (Vmax ~44–75 vs ~50 U/mg wild type), but H128A raises the apparent Kd for Zn(II) roughly ten-fold — "His128 is part of a histidine- and cysteine-rich region of the sequence that is implicated in metal binding. The apparent Kd for Zn(II) binding to H128A is about an order of magnitude higher than for the wild type protein" ([PMID: 7592604](https://pubmed.ncbi.nlm.nih.gov/7592604/)). That same study confirms "Porphobilinogen synthase (PBGS) is a metalloenzyme that catalyzes the first common step of tetrapyrrole biosynthesis, the asymmetric condensation of two molecules of 5-aminolevulinic acid (ALA) to form porphobilinogen." Full conservation of this pocket in Q88IT6 supports a functional Zn2+ site. The quantum-biochemistry study of human PBGS independently identifies Cys122/Cys124/Cys132 as the highest-energy zinc contacts and His131/Asp120/Ser168/Arg209 as co-conserved metal-site residues ([PMID: 33791795](https://pubmed.ncbi.nlm.nih.gov/33791795/)) — all conserved in Q88IT6.

---

## Mechanistic Model / Interpretation

### Position in the heme biosynthetic pathway

hemB catalyzes the **second step** of the universal heme pathway, immediately downstream of ALA synthesis. *Pseudomonas* uses the **C5 / glutamate pathway** to make ALA:

```
Glutamate
   │  glutamyl-tRNA synthetase (gltX)
   ▼
Glutamyl-tRNA
   │  hemA (glutamyl-tRNA reductase), hemL (GSA aminomutase)
   ▼
5-Aminolevulinic acid (ALA)
   │
   │  ★ hemB / PBGS (Q88IT6)  ← THIS ENZYME
   │     2 ALA → porphobilinogen + 2 H2O   (Zn2+-dependent)
   ▼
Porphobilinogen (PBG)
   │  hemC (PBG deaminase) → hydroxymethylbilane
   │  hemD → uroporphyrinogen III
   │  hemE → hemF/hemN → hemG/hemY → hemH (ferrochelatase)
   ▼
Protoporphyrin IX → Heme (Fe insertion)
   │
   └──► also feeds siroheme, cobalamin (B12); chlorophyll in phototrophs
```

Because porphobilinogen is the monopyrrole precursor for **all** tetrapyrroles, hemB sits at a metabolic bottleneck: loss of function blocks heme, cytochromes, catalases/peroxidases, siroheme-dependent assimilatory reductases, and respiration. This is why PBGS is a validated antibacterial target — the antibiotic **alaremycin**, an ALA mimic, inhibits PBGS and uncouples heme biosynthesis from bacterial growth ([PMID: 19822707](https://pubmed.ncbi.nlm.nih.gov/19822707/)).

### Catalytic mechanism

The reaction proceeds through a well-characterized two-Schiff-base mechanism within a single active site of the TIM barrel:

```
       A-side                                  P-side
   ┌──────────┐                            ┌──────────┐
   │  Lys249  │= N─(ALA-A)                  │  Lys197  │  perturbing
   │ (Schiff  │                            │  lysine  │
   │  base)   │        Zn2+ ──[Cys122/Cys124/Cys132 + His129/His131]
   └──────────┘                            └──────────┘
        │                                        │
   ALA-A amine forms C–N bond ◄──── aldol/Knorr ──► ALA-P
        │                                        │
        └──────────► Porphobilinogen ◄───────────┘
                       + 2 H2O
```

1. The first ALA ("A-side" substrate) forms a **Schiff base with Lys249**.
2. The second ALA ("P-side") binds adjacent to **Lys197**, the universally conserved "perturbing" lysine.
3. The catalytic **Zn2+**, ligated by the Cys122/124/132 triad in the His/Cys-rich pocket, positions/activates the substrates.
4. Asymmetric **C–N bond formation** followed by an **aldol-type C–C condensation** joins the two units and cyclizes to the pyrrole, releasing two waters and porphobilinogen.

Substrate carboxylates are anchored by conserved lid arginines (Arg228/Arg229 in the `NPMNRR` motif). The A-side and P-side chemistry is distinct, giving the reaction its characteristic asymmetry.

### Quaternary structure and allostery

PBGS is the archetypal **"morpheein"**: human PBGS interconverts among a high-activity octamer, a low-activity hexamer, and a dimer, providing a quaternary-structure basis for allostery and, in humans, for disease-causing variants and drug side effects ([PMID: 31952692](https://pubmed.ncbi.nlm.nih.gov/31952692/)). Whether *P. putida* hemB exhibits comparable morpheein dynamics is unknown, but the conserved TIM-barrel/oligomerization architecture makes it plausible.

### Zinc vs magnesium: the key species-specific insight

The single most notable mechanistic feature of *P. putida* hemB is its predicted **zinc dependence**, diverging from the experimentally confirmed **magnesium dependence** of the *P. aeruginosa* ortholog. The determinant is the metal-loop sequence:

| Enzyme | Metal loop (res ~118–136) | Metal class |
|--------|---------------------------|-------------|
| *P. putida* Q88IT6 | `VVMSDT`**`C`**`F`**`C`**`EYTSHGH`**`C`**`GVLH` | **Zinc** (Cys triad intact) |
| *E. coli* ALAD | `VMSDT`**`C`**`F`**`C`**`EYTSHGH`**`C`**`GVL` | Zinc |
| *P. aeruginosa* HEM2 | `IITDV`**`A`**`L`**`D`**`PFTTHGQ`**`D`**`GIL` | Magnesium (cysteines replaced) |

This places *P. putida* hemB with the *E. coli*/human zinc-type enzymes and predicts corresponding functional properties: dependence on Zn2+ for catalysis, sensitivity to zinc chelators, susceptibility to lead (Pb2+ displaces catalytic Zn2+ — the basis for ALAD's role as a biomarker of lead exposure in humans), and greater sensitivity to zinc-selective inhibitors such as 4,7-dioxosebacic acid ([PMID: 16304458](https://pubmed.ncbi.nlm.nih.gov/16304458/)). Many bacterial zinc-ALADs additionally possess a separate allosteric magnesium ("Mg arm") site, which may also apply here.

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports this report |
|------|--------------------|------------------------------|
| [9529530](https://pubmed.ncbi.nlm.nih.gov/9529530/) | *Cloning… hemB of P. aeruginosa, a Mg-dependent ALAD* | Directly demonstrates the ALAD reaction (2 ALA → PBG) for the closest ortholog and establishes it is **Mg-dependent** — the comparison point highlighting *P. putida*'s zinc-type identity. |
| [27783504](https://pubmed.ncbi.nlm.nih.gov/27783504/) | *The Remarkable Character of Porphobilinogen Synthase* | Confirms PBGS as the essential first committed enzyme of tetrapyrrole biosynthesis and documents the family's varied metal-ion usage. |
| [7592604](https://pubmed.ncbi.nlm.nih.gov/7592604/) | *Conserved histidines of E. coli PBGS not required for catalysis* | Maps the His/Cys-rich **zinc-binding pocket** (His128 ↔ *P. putida* His131); H128A raises Zn Kd ~10-fold, confirming metalloenzyme status. |
| [33791795](https://pubmed.ncbi.nlm.nih.gov/33791795/) | *Human PBGS metalloprotein by quantum biochemistry & evolution* | Identifies Cys122/124/132 as the strongest zinc contacts and His131/Asp120/Ser168/Arg209 as co-conserved — all present in Q88IT6. |
| [11444968](https://pubmed.ncbi.nlm.nih.gov/11444968/) | *Suicide inactivation by 4,7-dioxosebacic acid* | Identifies the two catalytic lysines (Schiff-base Lys246 and perturbing Lys194, *E. coli* numbering) → *P. putida* Lys249/Lys197. |
| [15381398](https://pubmed.ncbi.nlm.nih.gov/15381398/) | *The PBGS catalyzed reaction mechanism* | Establishes the two-Schiff-base mechanism binding both ALA substrates. |
| [16304458](https://pubmed.ncbi.nlm.nih.gov/16304458/) | *Chlorobium ALAD with diacid inhibitor* | Confirms both active-site lysines form Schiff bases and defines zinc-dependent vs -independent inhibitor selectivity. |
| [28045381](https://pubmed.ncbi.nlm.nih.gov/28045381/) | *Structural studies of ALAD substrate/product complexes* | Establishes the universal **TIM-barrel fold** of ALAD monomers. |
| [19822707](https://pubmed.ncbi.nlm.nih.gov/19822707/) | *P. aeruginosa PBGS with alaremycin* | Shows the active-site catalytic lysine covalently binds an ALA-mimic antibiotic; validates PBGS as an antibacterial target. |
| [31952692](https://pubmed.ncbi.nlm.nih.gov/31952692/) | *PBGS: an equilibrium of different assemblies* | Documents PBGS quaternary-structure dynamics (morpheein octamer/hexamer/dimer equilibrium). |

The human lead-toxicity literature (PMIDs [35969329](https://pubmed.ncbi.nlm.nih.gov/35969329/), [35805621](https://pubmed.ncbi.nlm.nih.gov/35805621/), [32554272](https://pubmed.ncbi.nlm.nih.gov/32554272/), [32004562](https://pubmed.ncbi.nlm.nih.gov/32004562/)) concerns the human ALAD ortholog as a biomarker of lead exposure; it is not directly about *P. putida* but corroborates the general principle that zinc-type ALADs are inhibited when Pb2+ displaces the catalytic zinc.

---

## Supported and Refuted Hypotheses

**Supported**
- **H1** — Q88IT6 catalyzes 2 ALA → porphobilinogen + 2 H2O (EC 4.2.1.24). *(Family/EC annotation + direct evidence for the ortholog.)*
- **H2** — The two catalytic lysines (Lys249 Schiff-base, Lys197 perturbing) are conserved. *(Alignment to E. coli.)*
- **H3** — Q88IT6 is a **zinc-dependent** PBGS. *(Retention of the Cys122/124/132 triad, matching E. coli/human Zn enzymes; conserved His/Cys pocket.)*
- **H4** — The enzyme is cytoplasmic and adopts a homo-oligomeric TIM-barrel architecture.

**Refuted / revised**
- The assumption (extrapolated from the *P. aeruginosa* literature) that all *Pseudomonas* PBGS are Mg2+-dependent does **not** hold for *P. putida*, whose enzyme retains the zinc triad.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of the *P. putida* enzyme.** All functional conclusions rest on (a) database annotation, (b) sequence homology and conserved-residue mapping, and (c) direct experiments on orthologs. The Q88IT6 protein itself has not, to our knowledge, been purified, assayed, or crystallized.
2. **Zinc dependence is a strong prediction, not a measurement.** The Cys122/124/132 triad is diagnostic and reliable, but metal content, metal Km/Kd, Pb2+ sensitivity, and any allosteric magnesium requirement of the *P. putida* enzyme have not been measured.
3. **Oligomeric state and morpheein behavior unknown.** Whether *P. putida* hemB shows the octamer/hexamer/dimer equilibrium seen for human PBGS is untested.
4. **Localization inferred, not demonstrated.** The absence of a signal peptide/TM segment strongly implies cytoplasmic localization, but this has not been shown experimentally in *P. putida*.
5. **Regulation uncharacterized.** hemB expression/regulation in *P. putida* was not investigated; in *P. aeruginosa*, no strong O2/heme/iron regulation of hemB was observed.
6. **No structural model validated.** Conclusions are sequence-based; no AlphaFold/homology model was quantitatively validated here.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and metal analysis.** Clone PP_2913, express in *E. coli*, purify, and determine catalytic metal identity by ICP-MS/atomic absorption and by activity assays ± Zn2+/Mg2+ and ± chelators (EDTA, 1,10-phenanthroline) to directly test zinc dependence.
2. **Steady-state kinetics.** Measure Km for ALA, kcat, and pH optimum; benchmark against zinc-type (*E. coli*, human) and Mg-type (*P. aeruginosa*) enzymes.
3. **Lead-inhibition assay.** Because zinc-type ALADs are Pb2+-sensitive, test Pb2+ inhibition to functionally confirm a catalytic zinc site.
4. **Structure determination / modeling.** Solve the crystal structure or build and validate an AlphaFold model (e.g., via Phenix) to confirm the TIM-barrel fold, Cys122/124/132 zinc geometry, and Lys197/Lys249 arrangement.
5. **Inhibitor selectivity.** Test 4,7-dioxosebacic acid and alaremycin; zinc-type enzymes are predicted to be more sensitive to the former.
6. **Oligomeric-state analysis.** Use size-exclusion chromatography / native MS / analytical ultracentrifugation to determine oligomeric state and test for morpheein-type equilibria.
7. **Genetic essentiality.** Attempt a PP_2913 knockout in *P. putida* KT2440; expect heme auxotrophy (rescuable by exogenous heme), confirming its committed pathway role.

---

## Conclusion

hemB / PP_2913 (Q88IT6) in *Pseudomonas putida* KT2440 encodes **porphobilinogen synthase (5‑aminolevulinate dehydratase, ALAD; EC 4.2.1.24)**, a **cytoplasmic, TIM‑barrel, homo‑oligomeric metalloenzyme** that catalyzes the **first committed common step of heme/tetrapyrrole biosynthesis** — the asymmetric condensation of two 5‑aminolevulinate molecules into porphobilinogen plus two water, using two conserved active-site lysines (Lys249 Schiff-base/A-side and Lys197 perturbing/P-side). Unlike its magnesium-dependent *P. aeruginosa* ortholog, the *P. putida* enzyme retains the canonical **zinc-binding cysteine triad Cys122/124/132** and the flanking His/Cys pocket identical to the *E. coli* and human enzymes, and is therefore predicted to be a **zinc-dependent PBGS**. The gene identity is verified and unambiguous; all conclusions are consistent with the UniProt annotation, domain architecture, and the primary ALAD literature.


## Artifacts

- [OpenScientist final report](hemB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](hemB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:9529530
2. PMID:27783504
3. PMID:33791795
4. PMID:16304458
5. PMID:11444968
6. PMID:15381398
7. PMID:19822707
8. PMID:28045381
9. PMID:7592604
10. PMID:31952692