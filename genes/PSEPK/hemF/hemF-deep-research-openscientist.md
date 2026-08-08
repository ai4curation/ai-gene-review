---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T20:45:18.369303'
end_time: '2026-07-20T20:56:31.545357'
duration_seconds: 673.18
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: hemF
  gene_symbol: hemF
  uniprot_accession: Q88RQ6
  protein_description: 'RecName: Full=Oxygen-dependent coproporphyrinogen-III oxidase
    {ECO:0000255|HAMAP-Rule:MF_00333}; Short=CPO {ECO:0000255|HAMAP-Rule:MF_00333};
    Short=Coprogen oxidase {ECO:0000255|HAMAP-Rule:MF_00333}; Short=Coproporphyrinogenase
    {ECO:0000255|HAMAP-Rule:MF_00333}; EC=1.3.3.3 {ECO:0000255|HAMAP-Rule:MF_00333};'
  gene_info: Name=hemF {ECO:0000255|HAMAP-Rule:MF_00333}; OrderedLocusNames=PP_0073;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the aerobic coproporphyrinogen-III oxidase
  protein_domains: Coprogen_oxidase_aer. (IPR001260); Coprogen_oxidase_aer_sf. (IPR036406);
    Coprogen_oxidase_CS. (IPR018375); Coprogen_oxidas (PF01218)
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
  path: hemF-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: hemF-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88RQ6
- **Protein Description:** RecName: Full=Oxygen-dependent coproporphyrinogen-III oxidase {ECO:0000255|HAMAP-Rule:MF_00333}; Short=CPO {ECO:0000255|HAMAP-Rule:MF_00333}; Short=Coprogen oxidase {ECO:0000255|HAMAP-Rule:MF_00333}; Short=Coproporphyrinogenase {ECO:0000255|HAMAP-Rule:MF_00333}; EC=1.3.3.3 {ECO:0000255|HAMAP-Rule:MF_00333};
- **Gene Information:** Name=hemF {ECO:0000255|HAMAP-Rule:MF_00333}; OrderedLocusNames=PP_0073;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the aerobic coproporphyrinogen-III oxidase
- **Key Domains:** Coprogen_oxidase_aer. (IPR001260); Coprogen_oxidase_aer_sf. (IPR036406); Coprogen_oxidase_CS. (IPR018375); Coprogen_oxidas (PF01218)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "hemF" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'hemF' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **hemF** (gene ID: hemF, UniProt: Q88RQ6) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *hemF* (PP_0073, UniProt Q88RQ6) — Oxygen-dependent Coproporphyrinogen-III Oxidase from *Pseudomonas putida* KT2440

## Summary

The gene **hemF** (ordered locus **PP_0073**; UniProt **Q88RQ6**) of *Pseudomonas putida* KT2440 encodes the **oxygen-dependent coproporphyrinogen-III oxidase** (HemF; also called CPO, coprogen oxidase, coproporphyrinogenase; **EC 1.3.3.3**). This enzyme catalyzes the sixth step — the antepenultimate reaction — of the heme (protoheme IX) biosynthetic pathway: the **O₂-dependent oxidative decarboxylation of coproporphyrinogen III to protoporphyrinogen IX**. Mechanistically, HemF converts the two propionate side chains on pyrrole rings A and B of the tetrapyrrole macrocycle into vinyl groups, releasing two molecules of CO₂ and consuming molecular oxygen as the terminal electron acceptor. The canonical reaction (RHEA:18257) is: *coproporphyrinogen III + O₂ + 2 H⁺ → protoporphyrinogen IX + 2 CO₂ + 2 H₂O*.

The gene identification is **unambiguous and internally consistent**. The gene symbol *hemF*, the organism (*P. putida* KT2440, an aerobic γ-proteobacterium), the EC number, and the protein family (aerobic coproporphyrinogen-III oxidase; Pfam **PF01218**; InterPro **IPR001260 / IPR036406 / IPR018375**) all denote the same well-defined enzyme. Direct inspection of the Q88RQ6 sequence confirms the diagnostic aerobic-CPO family signatures. No cross-gene confusion exists: *hemF* is universally used for the **oxygen-dependent** isoenzyme, distinct from the non-homologous, oxygen-independent radical-SAM enzyme **HemN**.

HemF is a **soluble, cytoplasmic, homodimeric enzyme** that operates without a heme, flavin, or iron-sulfur cofactor (a divalent-metal requirement is predicted by the HAMAP rule but was not observed in the human crystal structure — an unresolved point). It is one of two functionally analogous but structurally unrelated isoenzymes catalyzing the same reaction: HemF is the **O₂-dependent** route used during aerobic growth (the physiological norm for *P. putida*), whereas **HemN** (a radical-SAM [4Fe-4S] enzyme, encoded separately at Q88F35 in KT2440) provides an **oxygen-independent** backup at low oxygen tension. The heme end-product supports the cytochromes, catalases, and peroxidases essential to aerobic respiration and oxidative-stress defense in this metabolically versatile soil bacterium.

---

## Key Findings

### Finding 1 — HemF catalyzes the O₂-dependent oxidative decarboxylation of coproporphyrinogen III to protoporphyrinogen IX

HemF (Q88RQ6) is the **oxygen-dependent isoenzyme** of coproporphyrinogen-III oxidase (EC 1.3.3.3). It acts on the highly reactive, colorless, reduced tetrapyrrole **coproporphyrinogen III**, which bears four propionate and four methyl side chains around its four pyrrole rings. HemF selectively converts **the two propionate substituents on rings A and B into vinyl groups**, releasing two molecules of carbon dioxide and yielding **protoporphyrinogen IX**; the ring C and D propionates are retained. This is the sixth of eight enzymatic steps in heme biosynthesis and prepares the macrocycle for the subsequent oxidation (protoporphyrinogen oxidase) and iron insertion (ferrochelatase, HemH) that complete protoheme IX. The specific substrate is the **III isomer** of coproporphyrinogen.

Classical bacterial genetics established this function definitively. In *Salmonella typhimurium*, mutants defective in **both** *hemN* and *hemF* are heme auxotrophs during aerobic growth and fail to convert the substrate to product ([PMID: 1317844](https://pubmed.ncbi.nlm.nih.gov/1317844/)): *"double mutants are described that are auxotrophic for heme during aerobic growth and fail to convert coproporphyrinogen III to protoporphyrinogen IX. These mutant strains are defective in two genes, hemN and hemF."* The same study showed *"either hemN or hemF is sufficient for aerobic heme synthesis. These phenotypes are consistent with the requirement of a well-characterized class of coproporphyrinogen oxidase for molecular oxygen,"* pinpointing HemF as the **oxygen-requiring** member of the pair. The precise chemistry was defined by mechanistic modeling ([PMID: 18226911](https://pubmed.ncbi.nlm.nih.gov/18226911/)): *"coproporphyrinogen III oxidase catalyzes the conversion of two propionate substituents from the highly reactive substrate coproporphyrinogen III into vinyl substituents, yielding protoporphyrinogen IX."* UniProt/Rhea assigns this as the single step ("step 1/1") of protoporphyrinogen-IX formation from coproporphyrinogen III via the O₂ route.

### Finding 2 — Stepwise, cofactor-independent mechanism proceeding through the harderoporphyrinogen intermediate

The two decarboxylations do not occur simultaneously; they proceed **sequentially** through a monovinyl-monopropionate intermediate, **harderoporphyrinogen** (ring-A propionate first, then ring-B). The reality of this intermediate is demonstrated by the human disease **harderoporphyria**, a variant of hereditary coproporphyria caused by a specific CPO mutation (K404E in current human numbering; historically K304E) that traps the reaction at the intermediate stage, causing massive harderoporphyrin excretion. The mutant enzyme's Michaelis constant is ~**10-fold higher** than wild-type ([PMID: 7757079](https://pubmed.ncbi.nlm.nih.gov/7757079/)): *"this amino acid substitution was responsible for the important decrease in the enzyme activity and for the accumulation of harderoporphyrin. The Michaelis constant of the mutated enzyme was 10-fold higher than normal suggesting that the lysine at position 304 is important for binding the substrate."* An independent clinical study reported Km elevated **15–20-fold** and confirmed that coproporphyrinogen and harderoporphyrinogen are metabolized at the same catalytic center ([PMID: 6886003](https://pubmed.ncbi.nlm.nih.gov/6886003/)).

Remarkably, HemF/CPO achieves oxidative decarboxylation **without any metal ion or organic cofactor** — unusual for an oxidase — as stated in the human CPO structural study ([PMID: 16176984](https://pubmed.ncbi.nlm.nih.gov/16176984/)): *"The mechanism by which CPO catalyzes oxidative decarboxylation, in an extraordinary metal- and cofactor-independent manner, is poorly understood."* Density-functional (DFT) modeling proposed a chemically plausible route ([PMID: 18226911](https://pubmed.ncbi.nlm.nih.gov/18226911/)): *"O(2) addition to the (preferentially deprotonated) pyrrole substrate (yielding a hydroperoxide, which then abstracts a proton from the reactive propionate substituent) is compatible with the observed experimental reaction rate, and that the reaction may then proceed through HO2- elimination, followed by decarboxylation."* Molecular oxygen serves as the immediate electron acceptor, and the reaction passes through a substrate radical/carbanion intermediate, with the deprotonated pyrrole nitrogen key to activating O₂.

### Finding 3 — A soluble homodimer with a novel fold, acting in the bacterial cytoplasm

The three-dimensional architecture of the aerobic CPO family was revealed by the **1.58-Å crystal structure of the human ortholog**, which showed a **previously uncharacterized tertiary fold**: an unusually flat seven-stranded β-sheet sandwiched by α-helices ([PMID: 16176984](https://pubmed.ncbi.nlm.nih.gov/16176984/)): *"we report the crystal structure of human CPO at 1.58-A resolution. The structure reveals a previously uncharacterized tertiary topology comprising an unusually flat seven-stranded beta-sheet sandwiched by alpha-helices."* The enzyme is an **obligate homodimer** (K_D ≈ 5 × 10⁻⁷ M) in which one monomer rotates ~40° relative to the other to form an intersubunit interface adjacent to the two independent catalytic sites: *"In the biologically active dimer (K(D) = 5 x 10(-7) M), one monomer rotates relative to the second by approximately 40 degrees to create an intersubunit interface in close proximity to two independent enzymatic sites."* The structure assigned the active-site residues: *"allows us to assign Ser-244, His-258, Asn-260, Arg-262, Asp-282, and Arg-332 as residues mediating substrate recognition and decarboxylation."*

Regarding **localization**, the eukaryotic aerobic CPO resides in the mitochondrial intermembrane space. Bacteria such as *P. putida* lack mitochondria, so the soluble HemF operates in the **cytoplasm**, consistent with the UniProt cytoplasmic assignment for Q88RQ6 and the soluble, membrane-independent nature of the family. The Coprogen_oxidase_aer domain (PF01218 / IPR001260) present in Q88RQ6 is diagnostic of this cofactor-free enzyme class.

### Finding 4 — Sequence-level evidence confirms Q88RQ6 is a genuine aerobic HemF

Direct examination of the Q88RQ6 sequence provides organism-specific confirmation. The protein is **303 amino acids** long and annotated as cytoplasmic. UniProt/Rhea assigns the exact reaction **RHEA:18257** as the sole step of the "protoporphyrinogen IX from coproporphyrinogen III (O₂ route)" sub-pathway. The sequence carries:

- the **invariant aerobic-CPO family signature GGGFDLTP** at residues 127–134, matching the Coprogen_oxidase_CS signature (IPR018375);
- the conserved catalytic **proton-donor His107** and a cluster of conserved active-site histidines (**His97, His146, His176**) plus substrate-binding residues at positions 93, 109–111, and 259–261;
- a **dimerization region (residues 241–276)**, consistent with the obligate-homodimer architecture;
- only **five cysteines**, **not** arranged in the CxxxCxxC [4Fe-4S] radical-SAM motif of HemN.

The absence of the radical-SAM motif rules out an iron-sulfur identity and confirms HemF as a non-metallo, aerobic oxidase. HemN — not HemF — is *"the established radical SAM enzyme, HemN or oxygen-independent coproporphyrinogen III oxidase from Escherichia coli"* ([PMID: 16218869](https://pubmed.ncbi.nlm.nih.gov/16218869/)).

One annotation discrepancy is noted: **HAMAP rule MF_00333** lists a divalent metal cation cofactor (CHEBI:60240) for aerobic CPO, whereas the human CPO crystal structure explicitly reported the enzyme as **metal-independent** ([PMID: 16176984](https://pubmed.ncbi.nlm.nih.gov/16176984/)). The metal requirement of aerobic CPO therefore remains **debated**; structural evidence favors metal-independence, but a loosely bound divalent cation cannot be fully excluded.

### Finding 5 — *P. putida* KT2440 encodes both isoenzymes (HemF + HemN), giving O₂-dependent and O₂-independent routes

A targeted survey of the *P. putida* KT2440 proteome (NCBI taxid 160488) confirms the genome encodes **both** coproporphyrinogen-oxidase isoenzymes for the same reaction, plus the terminal ferrochelatase:

| Enzyme | UniProt | Gene | Length | O₂ dependence | Cofactor |
|---|---|---|---|---|---|
| Coproporphyrinogen-III oxidase (aerobic) | **Q88RQ6** | **hemF (PP_0073)** | 303 aa | O₂-**dependent** | none (metal debated) |
| Coproporphyrinogen-III oxidase (anaerobic) | Q88F35 | hemN | 460 aa | O₂-**independent** | [4Fe-4S] radical-SAM, SAM |
| Ferrochelatase (terminal step) | Q88PV4 | hemH | 338 aa | — | inserts Fe²⁺ |

This arrangement parallels *E. coli* and *Salmonella*, where **either** *hemN* or *hemF* suffices aerobically while *hemN* is required anaerobically ([PMID: 1317844](https://pubmed.ncbi.nlm.nih.gov/1317844/)). Because *P. putida* is an aerobic soil organism, **HemF is the primary physiological route** for this step, with HemN as an oxygen-independent backup when oxygen tension falls. The same division of labor is documented in the cyanobacterium *Synechocystis* sp. PCC 6803, where HemF is the sole CPO under aerobic conditions and HemN operates under micro-oxic conditions, ensuring *"stable supply of tetrapyrrole pigments under environments where oxygen levels fluctuate greatly"* ([PMID: 20194361](https://pubmed.ncbi.nlm.nih.gov/20194361/)). The E. coli complementation work likewise showed the cloned *hemF* gene *"complemented exclusively under aerobic conditions"* ([PMID: 7768836](https://pubmed.ncbi.nlm.nih.gov/7768836/)).

---

## Mechanistic Model and Interpretation

HemF occupies a defined position in the universal heme biosynthetic pathway:

```
   Uroporphyrinogen III
        │  HemE (UROD)  — 4× decarboxylation
        ▼
   Coproporphyrinogen III  ◄──── SUBSTRATE
        │
        │   ┌─────────────────────────────────────────────┐
        │   │  STEP 6 (this enzyme, EC 1.3.3.3)           │
        │   │  HemF (aerobic, O2-dependent)  ── OR ──      │
        │   │  HemN (anaerobic, radical-SAM, O2-indep.)   │
        │   │                                             │
        │   │  ring-A propionate → vinyl  (−CO2)          │
        │   │        ▼ harderoporphyrinogen (intermediate)│
        │   │  ring-B propionate → vinyl  (−CO2)          │
        │   └─────────────────────────────────────────────┘
        ▼
   Protoporphyrinogen IX  ◄──── PRODUCT
        │  HemG/HemY (protoporphyrinogen oxidase)
        ▼
   Protoporphyrin IX
        │  HemH (ferrochelatase)  — inserts Fe2+
        ▼
   Protoheme IX (heme b)  →  cytochromes, catalases, peroxidases
```

**Reaction catalyzed (RHEA:18257, EC 1.3.3.3):**

```
coproporphyrinogen III + O2 + 2 H+  →  protoporphyrinogen IX + 2 CO2 + 2 H2O
```

The synthesized model is coherent and complete. HemF is a **soluble, cytoplasmic, cofactor-free homodimer** with a novel β-sheet-and-α-helix fold and two active sites at the dimer interface. It selectively oxidatively decarboxylates the ring-A and ring-B propionates of coproporphyrinogen III to vinyl groups in a **two-step, ordered manner** passing through the isolable intermediate harderoporphyrinogen. Catalysis uses molecular O₂ as the electron acceptor, likely via a deprotonated-pyrrole/hydroperoxide route, and requires no organic prosthetic group (with the caveat that HAMAP annotates a divalent metal). This positions HemF as the **aerobic gatekeeper** of the antepenultimate heme step in *P. putida* — functionally interchangeable with, but structurally and mechanistically unrelated to, the radical-SAM enzyme HemN that the same genome also encodes for low-oxygen conditions.

The biological significance is direct: the heme end-product is indispensable for the **cytochromes** (respiratory electron transport), **catalases and peroxidases** (oxidative-stress defense), and other hemoproteins that underpin the aerobic, metabolically versatile lifestyle of *P. putida* KT2440. HemF ensures this supply is maintained efficiently under the oxygenated conditions the organism normally inhabits.

---

## Evidence Base

| PMID | Title (abbreviated) | Role in this report |
|---|---|---|
| [1317844](https://pubmed.ncbi.nlm.nih.gov/1317844/) | *Genes required for heme synthesis in Salmonella — aerobic/anaerobic coproporphyrinogen oxidation* | Genetic proof that hemF/hemN convert coproporphyrinogen III → protoporphyrinogen IX; establishes HemF as the O₂-requiring isoenzyme and hemF/hemN redundancy |
| [18226911](https://pubmed.ncbi.nlm.nih.gov/18226911/) | *Comparative DFT study of the O2-dependent CPO reaction mechanism* | Defines the two-propionate-to-vinyl chemistry; proposes the deprotonated-pyrrole/hydroperoxide O₂ mechanism |
| [16176984](https://pubmed.ncbi.nlm.nih.gov/16176984/) | *Structural basis of hereditary coproporphyria* | 1.58-Å human CPO structure: novel fold, obligate homodimer (K_D 5×10⁻⁷ M), active-site residues, metal-independence |
| [7757079](https://pubmed.ncbi.nlm.nih.gov/7757079/) | *Molecular defect causing harderoporphyria* | K→E substitution traps harderoporphyrinogen intermediate; ~10-fold higher Km identifies a substrate-binding residue |
| [6886003](https://pubmed.ncbi.nlm.nih.gov/6886003/) | *Harderoporphyria: a variant hereditary coproporphyria* | Clinical/biochemical confirmation of the intermediate; 15–20-fold higher Km; single catalytic center for both steps |
| [16218869](https://pubmed.ncbi.nlm.nih.gov/16218869/) | *Structural/functional comparison of HemN to radical SAM enzymes* | Confirms HemN (not HemF) is the radical-SAM/[4Fe-4S] enzyme — supports exclusion of that motif in Q88RQ6 |
| [20194361](https://pubmed.ncbi.nlm.nih.gov/20194361/) | *Functional differentiation of two analogous CPOs in Synechocystis* | HemF as sole aerobic CPO; HemN under micro-oxic conditions — models the division of labor in P. putida |
| [7768836](https://pubmed.ncbi.nlm.nih.gov/7768836/) | *Cloning of E. coli hemN (oxygen-independent CPO)* | Establishes HemF (aerobic, complements only aerobically) vs HemN (oxygen-independent) distinction |
| [398301](https://pubmed.ncbi.nlm.nih.gov/398301/) | *The porphyrias* | Situates CPO within the human heme pathway and disease context |

**How the evidence fits together.** Bacterial genetics ([PMID: 1317844](https://pubmed.ncbi.nlm.nih.gov/1317844/), [PMID: 7768836](https://pubmed.ncbi.nlm.nih.gov/7768836/)) fixes the *function* and the aerobic/anaerobic division of labor; the human structural and disease studies ([PMID: 16176984](https://pubmed.ncbi.nlm.nih.gov/16176984/), [PMID: 7757079](https://pubmed.ncbi.nlm.nih.gov/7757079/), [PMID: 6886003](https://pubmed.ncbi.nlm.nih.gov/6886003/)) supply the *fold, oligomeric state, active-site residues, and reaction intermediate*; the DFT study ([PMID: 18226911](https://pubmed.ncbi.nlm.nih.gov/18226911/)) supplies the *chemical mechanism*; and the radical-SAM literature ([PMID: 16218869](https://pubmed.ncbi.nlm.nih.gov/16218869/)) plus direct sequence inspection of Q88RQ6 confirm that this specific *P. putida* protein belongs to the aerobic, non-iron-sulfur class. The alignment of the conserved GGGFDLTP signature, catalytic His107, and dimerization region within the actual Q88RQ6 sequence provides organism-specific verification.

---

## Limitations and Knowledge Gaps

1. **No direct enzymology on the *P. putida* protein.** The function of Q88RQ6 is assigned by strong homology, conserved sequence signatures, HAMAP rule MF_00333, and the universal biochemistry of the aerobic CPO family — not by direct kinetic characterization of the KT2440 enzyme or a PP_0073 knockout. The assignment is nonetheless high-confidence because the family is deeply conserved and diagnostic signatures are present.

2. **Cofactor ambiguity.** HAMAP annotates a divalent metal cation cofactor, whereas the human crystal structure reported metal- and cofactor-independence. This discrepancy is unresolved for the family and specifically for Q88RQ6.

3. **Structural inference from a eukaryotic ortholog.** The fold, dimer interface, and catalytic-residue assignments derive from the human enzyme; residue numbering and precise contacts in the *P. putida* protein are inferred, not observed.

4. **Localization inferred, not demonstrated.** Cytoplasmic localization follows from the soluble nature of the family and the absence of mitochondria/signal peptides in bacteria, consistent with UniProt — but has not been experimentally verified for PP_0073.

5. **Relative HemF/HemN contribution unstudied in this organism.** The in vivo contributions of HemF versus HemN across the oxygen tensions *P. putida* experiences (rhizosphere, biofilm interiors, aerated culture) have not been directly measured in KT2440.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and assay.** Overexpress and purify PP_0073 (Q88RQ6); assay coproporphyrinogen-III oxidase activity aerobically; determine kcat and Km for coproporphyrinogen III; confirm O₂ dependence and lack of activity under strict anaerobiosis.

2. **Metal-dependence test.** Assay purified HemF ± metal chelators and with defined divalent-metal supplementation, and perform ICP-MS for bound metal, to resolve the HAMAP-vs-structure cofactor discrepancy.

3. **Genetic dissection in KT2440.** Construct ΔhemF, ΔhemN, and ΔhemF ΔhemN mutants; score heme auxotrophy and growth across an oxygen gradient (aerobic → micro-oxic → anaerobic) to confirm the predicted division of labor and any conditional essentiality.

4. **Intermediate trapping.** Engineer an active-site substitution analogous to the human harderoporphyria mutation and test for harderoporphyrin(ogen) accumulation, validating the ordered two-step mechanism in this ortholog.

5. **Structure determination.** Solve the *P. putida* HemF structure (crystallography or cryo-EM) to confirm the fold, dimer interface (residues ~241–276), and active-site geometry, and to settle the metal question.

6. **Expression profiling.** Use RT-qPCR or reporter fusions to measure hemF vs hemN transcription under varying oxygen tension in KT2440, testing whether hemN is induced under low O₂ as in *E. coli* and *Synechocystis*.

---

## Conclusion

The identification is unambiguous and well supported: **hemF / PP_0073 / Q88RQ6 encodes the oxygen-dependent coproporphyrinogen-III oxidase (HemF, CPO; EC 1.3.3.3) of *Pseudomonas putida* KT2440.** It is a soluble, cytoplasmic, cofactor-free homodimer that catalyzes the sixth step of heme biosynthesis — the O₂-dependent oxidative decarboxylation of coproporphyrinogen III to protoporphyrinogen IX via the harderoporphyrinogen intermediate — and serves as the primary aerobic route for this step, complemented by the oxygen-independent radical-SAM enzyme HemN under low-oxygen conditions.


## Artifacts

- [OpenScientist final report](hemF-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](hemF-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:1317844
2. PMID:18226911
3. PMID:7757079
4. PMID:6886003
5. PMID:16176984
6. PMID:16218869
7. PMID:20194361
8. PMID:7768836