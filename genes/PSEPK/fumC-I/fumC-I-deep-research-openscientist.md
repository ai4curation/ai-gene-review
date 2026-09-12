---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T17:50:31.185772'
end_time: '2026-07-11T18:03:12.673305'
duration_seconds: 761.49
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: fumC-I
  gene_symbol: fumC-I
  uniprot_accession: Q88PA6
  protein_description: 'RecName: Full=Fumarate hydratase class II {ECO:0000256|HAMAP-Rule:MF_00743};
    Short=Fumarase C {ECO:0000256|HAMAP-Rule:MF_00743}; EC=4.2.1.2 {ECO:0000256|HAMAP-Rule:MF_00743};
    AltName: Full=Aerobic fumarase {ECO:0000256|HAMAP-Rule:MF_00743}; AltName: Full=Iron-independent
    fumarase {ECO:0000256|HAMAP-Rule:MF_00743};'
  gene_info: Name=fumC-I {ECO:0000313|EMBL:AAN66569.1}; Synonyms=fumC {ECO:0000256|HAMAP-Rule:MF_00743};
    OrderedLocusNames=PP_0944 {ECO:0000313|EMBL:AAN66569.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the class-II fumarase/aspartase family. Fumarase
  protein_domains: Fum_hydII. (IPR005677); Fumarase/histidase_N. (IPR024083); Fumarase_C_C.
    (IPR018951); Fumarate_lyase_CS. (IPR020557); Fumarate_lyase_fam. (IPR000362)
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
citation_count: 15
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: fumC-I-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: fumC-I-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88PA6
- **Protein Description:** RecName: Full=Fumarate hydratase class II {ECO:0000256|HAMAP-Rule:MF_00743}; Short=Fumarase C {ECO:0000256|HAMAP-Rule:MF_00743}; EC=4.2.1.2 {ECO:0000256|HAMAP-Rule:MF_00743}; AltName: Full=Aerobic fumarase {ECO:0000256|HAMAP-Rule:MF_00743}; AltName: Full=Iron-independent fumarase {ECO:0000256|HAMAP-Rule:MF_00743};
- **Gene Information:** Name=fumC-I {ECO:0000313|EMBL:AAN66569.1}; Synonyms=fumC {ECO:0000256|HAMAP-Rule:MF_00743}; OrderedLocusNames=PP_0944 {ECO:0000313|EMBL:AAN66569.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the class-II fumarase/aspartase family. Fumarase
- **Key Domains:** Fum_hydII. (IPR005677); Fumarase/histidase_N. (IPR024083); Fumarase_C_C. (IPR018951); Fumarate_lyase_CS. (IPR020557); Fumarate_lyase_fam. (IPR000362)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "fumC-I" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'fumC-I' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **fumC-I** (gene ID: fumC-I, UniProt: Q88PA6) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: fumC-I (PP_0944, UniProt Q88PA6)

## Class II Fumarate Hydratase (Fumarase C) of *Pseudomonas putida* KT2440

---

## Summary

**fumC-I** (ordered locus **PP_0944**; UniProt accession **Q88PA6**) of *Pseudomonas putida* strain ATCC 47054 / DSM 6125 / KT2440 encodes a **class II fumarate hydratase (fumarase C, EC 4.2.1.2)**. Its primary and, on all available evidence, sole biochemical function is to catalyze the **reversible, stereospecific hydration of fumarate to L-(S)-malate** — the penultimate step of the tricarboxylic acid (TCA) cycle. The enzyme has narrow substrate specificity for the four-carbon dicarboxylates fumarate and L-malate and does not require a metal cofactor, distinguishing it mechanistically and structurally from the class I (iron–sulfur) fumarases. This identification is fully consistent with the target's UniProt annotation, its membership in the class-II fumarase/aspartase family (InterPro domains Fum_hydII IPR005677, Fumarate_lyase_fam IPR000362, Fumarate_lyase_CS IPR020557), and the presence of the diagnostic catalytic residues and "SS-loop" signature in the Q88PA6 sequence.

Mechanistically, fumC-I is predicted to assemble as a **soluble cytoplasmic homotetramer** that uses a **water-assisted general acid–base (E1cb-type carbanion) mechanism**. By homology to the extensively characterized *Escherichia coli* FumC (~46–59% identity across the class II family), the catalytic base corresponds to a histidine at the active "A-site" (UniProt active site residue ~183, structurally equivalent to *E. coli* FumC His188), with a permanent active-site water molecule and a separate allosteric dicarboxylate "B-site." Because the class II enzyme lacks the oxygen-labile [4Fe-4S] cluster of class I fumarases, it is the **oxidation-resistant "aerobic fumarase"** that sustains TCA-cycle flux under aerobic and oxidative-stress conditions — highly relevant for an obligate aerobe such as *P. putida* KT2440. In *E. coli*, *fumC* is a canonical member of the **SoxRS superoxide-stress regulon**, induced by superoxide and iron limitation.

A distinctive genomic feature of *P. putida* KT2440 is that **fumC-I is one of two paralogous class II fumarases** (the other being Q88M20/fumC), and the genome additionally encodes a **structurally unrelated class I fumarase** (Q88PF3). This provides functional redundancy for an essential metabolic step and mirrors the multi-fumarase arrangement of *E. coli* (FumA/FumB class I; FumC class II). All conclusions here rest on strong bioinformatic and sequence evidence for Q88PA6 combined with detailed biochemical, crystallographic, and mutagenesis data from well-characterized orthologs; no fumC-I-specific enzymatic study exists in the current literature, which is a stated limitation.

---

## Gene and Protein Identity Verification

Before presenting findings, the mandatory identity check was completed and **passes**:

| Attribute | UniProt (Q88PA6) | Literature/Bioinformatic finding | Match |
|---|---|---|---|
| Gene symbol | fumC-I (syn. fumC) | Class II fumarase symbol conserved across taxa | ✔ |
| Protein | Fumarate hydratase class II, EC 4.2.1.2 | Reaction fumarate ⇌ L-malate confirmed in family | ✔ |
| Organism | *P. putida* KT2440 | Proteome query confirms PP_0944 in KT2440 | ✔ |
| Family | Class-II fumarase/aspartase | SS-loop + catalytic residues present in sequence | ✔ |
| Domains | Fum_hydII, Fumarate_lyase | Diagnostic motifs identified in Q88PA6 | ✔ |

The gene symbol, organism, family, and domain architecture are internally consistent. Literature for class II fumarases (chiefly the *E. coli* FumC ortholog) is directly applicable by homology. **The research proceeds on the correct protein.**

---

## Key Findings

### F001 — fumC-I is a class II fumarate hydratase catalyzing reversible fumarate ⇌ L-malate interconversion

The core functional assignment is robust. UniProt Q88PA6 annotates PP_0944/fumC-I as "Fumarate hydratase class II, Fumarase C, EC 4.2.1.2," placing it in the class-II fumarase/aspartase family with the characteristic domains Fum_hydII (IPR005677) and Fumarate_lyase_fam (IPR000362). The defining biochemistry of this enzyme family was established in the homologous *E. coli* system, where fumarases "catalyze the interconversion of fumarate to L-malate in the tricarboxylic acid cycle" ([PMID: 11133938](https://pubmed.ncbi.nlm.nih.gov/11133938/)). The class assignment is equally well grounded: "Class II contains fumarase C and porcine fumarase, which have amino acid sequences 60% identical to each other" ([PMID: 1329945](https://pubmed.ncbi.nlm.nih.gov/1329945/)), a family that is deeply conserved — *E. coli* FumC is "homologous to eukaryotic fumarases" and shows "∼58% identity and ∼74% similarity to the yeast Fum1" ([PMID: 23462316](https://pubmed.ncbi.nlm.nih.gov/23462316/)).

The reaction catalyzed is therefore:

```
              fumarate  +  H2O   ⇌   (S)-malate  (= L-malate)
              (trans-butenedioate)      EC 4.2.1.2 ; Rhea:12460
```

Substrate specificity is narrow: class II fumarases act on the C4 dicarboxylates fumarate and L-malate and are stereospecific, producing exclusively the L-(S) enantiomer of malate via *anti* addition of water across the double bond. The reaction is a formidable catalytic feat — fumarate hydratase "decreases the free energy of the catalyzed reaction by 30 kcal mol⁻¹" relative to the uncatalyzed olefin hydration ([PMID: 36595439](https://pubmed.ncbi.nlm.nih.gov/36595439/)), underscoring the sophistication of the active-site chemistry.

### F002 — Catalytic mechanism: homotetrameric enzyme with a His general base and water-mediated acid–base catalysis

The catalytic mechanism of class II fumarase is one of the best-characterized among lyases, thanks to crystallographic and site-directed mutagenesis studies of the *E. coli* FumC ortholog. Two distinct dicarboxylate-binding sites exist: the catalytic **A-site** (the true active site) and a separate allosteric **B-site**. Mutagenesis decisively identified the catalytic residue: "H188N at the A-site resulted in a large decrease in specific activity, while the H129N mutation at the B-site had essentially no effect... we conclude that the A-site is indeed the active site, and a dual role for H188 as a potential catalytic base is proposed" ([PMID: 9098893](https://pubmed.ncbi.nlm.nih.gov/9098893/)).

The crystal structure of free *E. coli* FumC further revealed that catalysis depends on "the use of water as a permanent member of the active site and the use of an imidazole–imidazolium conversion to control access at the allosteric B site" ([PMID: 16204892](https://pubmed.ncbi.nlm.nih.gov/16204892/)). This places the enzyme firmly within the **fumarate-lyase superfamily**, whose members share an E1cb-type carbanion acid–base mechanism: "this homology extends to functionally related enzymes such as the class II fumarases, the argininosuccinate and adenylosuccinate lyases" ([PMID: 10800598](https://pubmed.ncbi.nlm.nih.gov/10800598/)). The shared Fumarate_lyase signature (IPR020557) present in Q88PA6 reflects this common mechanistic architecture, which is also used by aspartase.

The enzyme functions as a **homotetramer**, with each of the four active sites assembled from residues contributed by three of the four subunits — including the mobile "SS-loop" that reaches into a neighboring subunit (see F004). This quaternary structure is obligatory for activity.

### F003 — FumC is the aerobic, oxidation-resistant fumarase; cytoplasmic; operates in the oxidative TCA cycle

A key physiological property distinguishes class II FumC from the class I fumarases: **resistance to oxidative inactivation**. In *E. coli*, elevated oxygen "caused inactivation of FumA and FumB activities by the high oxidized state, but FumC activity" is retained ([PMID: 11133938](https://pubmed.ncbi.nlm.nih.gov/11133938/)). This resistance arises because the class II enzyme is **cofactor-free (iron-independent)** and lacks the oxygen-labile [4Fe-4S] cluster that class I fumarases require for catalysis ([PMID: 1329945](https://pubmed.ncbi.nlm.nih.gov/1329945/); [PMID: 30645090](https://pubmed.ncbi.nlm.nih.gov/30645090/)). The UniProt names "Aerobic fumarase" and "Iron-independent fumarase" for Q88PA6 directly reflect this property.

This is functionally important for *P. putida* KT2440, an **obligate aerobe** with a fully operational, tightly regulated TCA cycle as part of central carbon metabolism ([PMID: 24951791](https://pubmed.ncbi.nlm.nih.gov/24951791/)). Under aerobic growth, the oxidation-resistant fumarase reliably converts fumarate to L-malate to keep the oxidative cycle turning.

Regarding localization, fumarase is a **soluble enzyme**. In eukaryotes it "is dual localized to the cytosol and mitochondria" ([PMID: 23462316](https://pubmed.ncbi.nlm.nih.gov/23462316/)); in bacteria such as *P. putida*, which lack organelles, the enzyme resides in the **cytoplasm**, where the soluble TCA-cycle enzymes operate. This is corroborated by UniProt's subcellular-location annotation (see F004).

### F004 — Sequence-level confirmation: Q88PA6 carries the diagnostic SS-loop, catalytic residues, and canonical TCA annotation

Direct inspection of the target sequence confirms the homology-based inferences. The **459-amino-acid, ~48.5-kDa** Q88PA6 protein contains the hallmark class II fumarase/aspartase catalytic **"SS-loop" motif GSSIMPGKVN beginning at residue 312** — the conserved segment that swings into the neighboring subunit's active site in the homotetramer and is essential for catalysis. UniProt annotates:

- **Active site residue 183** — "Proton donor/acceptor" (structurally equivalent to *E. coli* FumC His188, the catalytic base defined by mutagenesis; [PMID: 9098893](https://pubmed.ncbi.nlm.nih.gov/9098893/)).
- **A second active site at residue 313** — within the SS-loop.
- **A "site B" binding residue at 124** — the allosteric dicarboxylate B-site defined crystallographically ([PMID: 16204892](https://pubmed.ncbi.nlm.nih.gov/16204892/)).
- **Residue 326** — "Important for catalytic activity."

UniProt records the exact reaction "(S)-malate = fumarate + H₂O" (Rhea:12460, EC 4.2.1.2), the pathway "tricarboxylic acid cycle; (S)-malate from fumarate: step 1/1," the keyword "Cytoplasm," and a **cytoplasmic subcellular location**. The correspondence between the target's annotated active-site residues and the experimentally validated *E. coli* residues gives high confidence that Q88PA6 is a bona fide, catalytically competent class II fumarase performing the canonical single TCA-cycle step.

| Q88PA6 feature | Residue/position | *E. coli* FumC equivalent | Evidence |
|---|---|---|---|
| Catalytic base (proton donor/acceptor) | 183 | His188 (A-site) | Mutagenesis [PMID: 9098893] |
| SS-loop catalytic motif | GSSIMPGKVN @ 312; active site @ 313 | Conserved SS-loop | Structure [PMID: 16204892] |
| Allosteric B-site binding | 124 | B-site (His129 region) | Structure [PMID: 16204892] |
| Additional catalytic residue | 326 | — | UniProt annotation |
| Reaction | (S)-malate ⇌ fumarate + H₂O | identical | Rhea:12460 / EC 4.2.1.2 |
| Localization | Cytoplasm | Cytoplasm | UniProt |

### F005 — FumC belongs to the SoxRS superoxide-stress regulon; induced by oxidative stress and iron limitation

Beyond its metabolic role, the *E. coli fumC* ortholog is a **canonical member of the SoxRS oxidative-stress regulon**, providing a regulatory rationale for the "aerobic/oxidation-resistant" phenotype. The SoxS activator binds the *fumC* promoter directly: MalE-SoxS "protected from DNase I attack 22–27 bp segments immediately adjacent to or overlapping the −35 hexamers of the zwf, sodA, nfo, micF, and fumC promoters" ([PMID: 7891555](https://pubmed.ncbi.nlm.nih.gov/7891555/)). Promoter–GFP fusion studies confirm superoxide-driven induction, listing "the sodA, fumC, zwf, acnA, acrAB, and soxS genes from the SoxRS regulon... which respond to the superoxide anion" ([PMID: 15672380](https://pubmed.ncbi.nlm.nih.gov/15672380/); [PMID: 12889026](https://pubmed.ncbi.nlm.nih.gov/12889026/)).

*fumC* is additionally induced by **iron deprivation** in a soxR-dependent manner: "SoxR completely inhibited the migration of a DNA fragment containing the promoter region of fumC, in gel-shift experiments" ([PMID: 11470373](https://pubmed.ncbi.nlm.nih.gov/11470373/)). Under strong superoxide stress, FumC protein/activity rises together with glucose-6-phosphate dehydrogenase — the cell deploys "such as glucose-6-phosphate dehydrogenase (Zwf) and fumarase (FumC)" as part of its antioxidant/metabolic-remodeling response ([PMID: 17309444](https://pubmed.ncbi.nlm.nih.gov/17309444/)).

The physiological logic is coherent: when superoxide inactivates the [4Fe-4S] class I fumarases (and aconitase), the cell upregulates the cofactor-free FumC to preserve TCA flux, and iron limitation similarly favors the iron-independent enzyme. Whether *P. putida* KT2440 regulates fumC-I through an orthologous SoxR/SoxS circuit remains to be established experimentally, but the promoter-level regulation is well documented in *E. coli*.

### F006 — fumC-I is one of two class II fumarase paralogs in *P. putida* KT2440, alongside an unrelated class I fumarase

A UniProt proteome query for *P. putida* KT2440 (organism_id 160488) returns **three fumarate hydratases**, revealing a redundant and mixed-class complement:

| Protein | Gene | Length | Class | Locus |
|---|---|---|---|---|
| **Q88PA6** (target) | **fumC-I** | 459 aa | Class II | **PP_0944** |
| Q88M20 | fumC | 464 aa | Class II | — |
| Q88PF3 | — | 507 aa | Class I | — |

Global Needleman–Wunsch alignments (match +1 / mismatch −1 / gap −2; identities conservatively estimated) quantify the relationships:

| Pair | Identity | Interpretation |
|---|---|---|
| fumC-I vs class II paralog Q88M20 | 48.6% (228/469) | Two distinct class II paralogs |
| fumC-I vs *E. coli* FumC (P05042) | 46.2% (217/470) | Clear class II ortholog |
| Q88M20 vs *E. coli* FumC | 59.4% (278/468) | Strong class II conservation |
| **fumC-I vs class I fumarase Q88PF3** | **23.6% (123/521)** | Structurally unrelated (different class) |

The ~60% class II identity between *E. coli* FumC and its homologs matches the canonical figure "Class II contains fumarase C and porcine fumarase... 60% identical" ([PMID: 1329945](https://pubmed.ncbi.nlm.nih.gov/1329945/)). The very low identity (23.6%) between fumC-I and the class I enzyme Q88PF3 confirms that these belong to two evolutionarily and mechanistically distinct enzyme families that converged on the same reaction — precisely the arrangement seen in *E. coli* (class I FumA/FumB vs class II FumC). This paralogy provides **functional redundancy** for an essential TCA-cycle step and likely enables the cell to maintain fumarase activity across varying oxygen tension, iron availability, and oxidative-stress conditions.

---

## Mechanistic Model and Interpretation

Integrating the six findings produces a coherent picture of fumC-I as the **cofactor-free, oxidation-resistant fumarase of the *P. putida* KT2440 TCA cycle**:

```
   CENTRAL CARBON METABOLISM — TCA CYCLE (oxidative direction)

     ... → succinate → [SDH] → FUMARATE ──────────────┐
                                                       │
                                          fumC-I (Q88PA6, PP_0944)
                                     class II fumarase, EC 4.2.1.2
                                     cytoplasm • homotetramer • no metal
                                     His183 base + active-site H2O
                                                       │
                                                       ▼
                            (S)-MALATE ──[MDH]──→ oxaloacetate → ...

   PROTEIN ARCHITECTURE                    REGULATORY CONTEXT (from E. coli ortholog)
   ┌───────────────────────────┐          ┌───────────────────────────────────────┐
   │ Homotetramer (4 subunits) │          │  Superoxide (O2•-)  ↑   Iron limitation │
   │ 4 active sites, each built │          │        │                    │          │
   │ from 3 subunits            │          │      SoxR → SoxS ───► fumC promoter    │
   │ SS-loop GSSIMPGKVN@312     │          │        (binds -35 region)              │
   │ reaches into neighbor      │          │              │                         │
   │ A-site: His183 (catalytic) │          │              ▼                         │
   │ B-site: allosteric (res124)│          │   ↑ FumC (iron-independent, O2-stable) │
   │ permanent active-site water│          │   maintains TCA flux when [4Fe-4S]     │
   └───────────────────────────┘          │   class I fumarases are inactivated    │
                                           └───────────────────────────────────────┘

   GENOMIC REDUNDANCY in P. putida KT2440
   ┌──────────────────────────────────────────────────────────────────┐
   │ Class II:  fumC-I (Q88PA6, PP_0944)  ── 48.6% id ──  fumC (Q88M20) │
   │ Class I:   Q88PF3  (only 23.6% id to fumC-I; [4Fe-4S], O2-labile)  │
   └──────────────────────────────────────────────────────────────────┘
```

**Primary function.** fumC-I catalyzes the reversible, stereospecific hydration of fumarate to L-(S)-malate (EC 4.2.1.2) — a single, well-defined TCA-cycle step with narrow C4-dicarboxylate substrate specificity.

**Location.** The enzyme acts in the **cytoplasm** as a soluble homotetramer; bacteria lack the mitochondrial compartment to which eukaryotic fumarases are additionally targeted.

**Mechanism.** Catalysis proceeds by a general acid–base (E1cb carbanion) mechanism shared across the fumarate-lyase superfamily, using a histidine base (residue ~183) and a permanent active-site water, without any metal or [4Fe-4S] cofactor.

**Pathway and physiology.** fumC-I operates in the oxidative TCA cycle of central carbon metabolism. Its cofactor-free, oxidation-resistant nature makes it the "aerobic fumarase" that keeps the cycle running under high oxygen and oxidative stress — the conditions under which the *E. coli* ortholog is transcriptionally induced via the SoxRS regulon and by iron limitation. In *P. putida* KT2440 this role is buffered by paralogy: a second class II fumarase (Q88M20) and a class I enzyme (Q88PF3) provide redundancy across metabolic and stress regimes.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports / challenges the findings |
|---|---|---|
| [11133938](https://pubmed.ncbi.nlm.nih.gov/11133938/) | *O₂- and growth-rate-dependent regulation of E. coli fumarases* | Defines the fumarate ⇌ L-malate reaction (F001); shows FumC uniquely retains activity under high O₂ (F003). Primary ortholog physiology. |
| [1329945](https://pubmed.ncbi.nlm.nih.gov/1329945/) | *Fumarase A: iron–sulfur cluster enzyme* | Establishes class I vs class II distinction; "class II... 60% identical" quantifies family conservation (F001, F006); class I needs [4Fe-4S] (F003). |
| [23462316](https://pubmed.ncbi.nlm.nih.gov/23462316/) | *Evolving dual targeting of a prokaryotic protein in yeast* | Confirms FumC homology to eukaryotic fumarases; documents cytosol/mitochondria dual localization → cytoplasmic in bacteria (F001, F003). |
| [9098893](https://pubmed.ncbi.nlm.nih.gov/9098893/) | *Mutations distinguishing active site from nearby dicarboxylate site* | Identifies His188 A-site catalytic base by mutagenesis; anchors the F002 mechanism and the F004 residue-183 assignment. |
| [16204892](https://pubmed.ncbi.nlm.nih.gov/16204892/) | *Structure of free fumarase C from E. coli* | Crystal structure: permanent active-site water, allosteric B-site (F002, F004). |
| [10800598](https://pubmed.ncbi.nlm.nih.gov/10800598/) | *L-aspartase: new tricks from an old enzyme* | Places class II fumarase in the fumarate-lyase superfamily using a carbanion acid–base mechanism (F002). |
| [24951791](https://pubmed.ncbi.nlm.nih.gov/24951791/) | *Central carbon metabolism of P. putida KT2440* | Establishes the operational TCA cycle in the target organism where fumarase acts (F003). |
| [7891555](https://pubmed.ncbi.nlm.nih.gov/7891555/) | *MalE-SoxS fusion; control sites of superoxide-inducible genes* | Direct DNase-I footprint of SoxS on the fumC promoter — places fumC in SoxRS regulon (F005). |
| [11470373](https://pubmed.ncbi.nlm.nih.gov/11470373/) | *Differential activities of SoxR under iron deprivation* | Gel-shift shows SoxR binds fumC promoter; iron-deprivation induction (F005). |
| [17309444](https://pubmed.ncbi.nlm.nih.gov/17309444/) | *Polyamine protection vs superoxide* | FumC protein/activity rises with Zwf under strong superoxide stress (F005). |
| [15672380](https://pubmed.ncbi.nlm.nih.gov/15672380/) | *Oxidative stress regulons via GFP* | fumC listed among SoxRS superoxide-responsive genes (F005). |
| [12889026](https://pubmed.ncbi.nlm.nih.gov/12889026/) | *Oxidative-stress response genes in aerobic fermentations* | Confirms fumC among SoxRS regulon genes; quantifies induction kinetics (F005). |
| [30645090](https://pubmed.ncbi.nlm.nih.gov/30645090/) | *Class I fumarate hydratase structures from Leishmania* | Class I FH uniquely uses the [4Fe-4S] cluster absent from class II — supports the iron-independent nature of FumC (F003). |
| [36595439](https://pubmed.ncbi.nlm.nih.gov/36595439/) | *Revisiting the burden borne by fumarase* | Quantifies the catalytic challenge (30 kcal mol⁻¹) of olefin hydration (F001 context). |
| [7557464](https://pubmed.ncbi.nlm.nih.gov/7557464/) | *fumR class II fumarase in Rhizopus oryzae* | Independent example of a class II fumarase (~494 aa, 50 kDa) — corroborates size/class of the family. |

**Note on evidence provenance.** No enzymatic, structural, or genetic study specific to *P. putida* fumC-I (Q88PA6) exists in the reviewed literature. Every mechanistic and regulatory claim derives from (i) direct bioinformatic analysis of the Q88PA6 sequence and UniProt annotation, and (ii) transfer of knowledge from well-characterized orthologs, chiefly *E. coli* FumC (46% identical) and the broader class II family. The high sequence identity and conservation of catalytic residues make this inference strong, but it remains inference.

---

## Limitations and Knowledge Gaps

1. **No target-specific experimental data.** There is no published kinetic characterization (kcat, Km for fumarate/L-malate), crystal structure, or knockout phenotype for *P. putida* fumC-I itself. All functional detail is inferred from orthologs.
2. **Paralog division of labor is unknown.** *P. putida* KT2440 has two class II fumarases (fumC-I/Q88PA6 and Q88M20) plus a class I enzyme (Q88PF3). Their relative expression, condition-dependence, and whether fumC-I or the paralog carries the dominant flux under standard growth are not established.
3. **Regulation is extrapolated.** The SoxRS induction and iron-limitation response are documented for *E. coli fumC*. It is not confirmed that fumC-I is under an orthologous regulatory circuit in *P. putida*, which has its own oxidative-stress regulators.
4. **Localization is annotation-based.** Cytoplasmic localization is inferred from UniProt and family behavior, not from a *P. putida*-specific proteomic or fractionation study.
5. **Substrate specificity assumed narrow.** Class II fumarases are highly specific for fumarate/L-malate, but the target has not been screened for possible promiscuous activities (e.g., the enol/keto-oxaloacetate isomerization seen in class I FumA; [PMID: 8422384](https://pubmed.ncbi.nlm.nih.gov/8422384/)).

---

## Proposed Follow-up Experiments and Actions

1. **Recombinant enzyme kinetics.** Overexpress and purify Q88PA6 (His-tagged) from *E. coli*; measure steady-state kinetics for fumarate hydration and L-malate dehydration, confirm metal-independence (no activity loss with chelators; no [4Fe-4S] EPR signal), and verify stereospecificity for L-(S)-malate.
2. **Structural determination.** Solve the crystal or cryo-EM structure of the homotetramer to confirm the His183 A-site, the SS-loop (GSSIMPGKVN@312) reaching into the neighboring subunit, the allosteric B-site, and the conserved active-site water.
3. **Genetic dissection of paralogy.** Construct single (ΔfumC-I, ΔQ88M20, ΔQ88PF3) and combinatorial deletions in *P. putida* KT2440; assay growth on TCA-dependent carbon sources and quantify fumarase activity to define each paralog's contribution and any conditional essentiality.
4. **Oxidative-stress regulation.** Use RT-qPCR / RNA-seq and promoter-reporter fusions to test whether fumC-I is induced by superoxide generators (paraquat) or iron limitation, and identify the responsible regulator(s) in *P. putida*.
5. **Oxidation-resistance validation.** Compare residual activity of purified fumC-I versus the class I paralog Q88PF3 after controlled oxygen/superoxide exposure to confirm the "aerobic/oxidation-resistant" phenotype at the protein level.
6. **Substrate-specificity screen.** Test the purified enzyme against related dicarboxylates and for possible side reactions to bound the specificity claim.

---

## Conclusion

fumC-I (PP_0944, UniProt Q88PA6) of *Pseudomonas putida* KT2440 is a **class II fumarate hydratase (fumarase C, EC 4.2.1.2)** that catalyzes the reversible, stereospecific hydration of **fumarate to L-(S)-malate** — the fumarase step of the TCA cycle — with narrow specificity for C4 dicarboxylates. It is a **cytoplasmic, iron-independent (cofactor-free) homotetramer** using a water-assisted general acid–base mechanism (catalytic base at residue ~183, equivalent to *E. coli* FumC His188, plus the conserved SS-loop), making it the **oxidation-resistant "aerobic" fumarase** that sustains TCA flux when oxygen-labile [4Fe-4S] class I fumarases are inactivated. In *P. putida* it is one of two class II paralogs (with Q88M20) alongside an unrelated class I enzyme (Q88PF3), providing redundancy for this essential metabolic step. The identification is strongly supported by sequence/domain evidence for Q88PA6 and by detailed biochemical, crystallographic, and mutagenesis data on close orthologs, though no fumC-I-specific experimental study yet exists.


## Artifacts

- [OpenScientist final report](fumC-I-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](fumC-I-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:11133938
2. PMID:1329945
3. PMID:23462316
4. PMID:36595439
5. PMID:9098893
6. PMID:16204892
7. PMID:10800598
8. PMID:30645090
9. PMID:24951791
10. PMID:7891555
11. PMID:15672380
12. PMID:12889026
13. PMID:11470373
14. PMID:17309444
15. PMID:8422384