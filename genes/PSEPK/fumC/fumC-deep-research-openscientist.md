---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T17:56:36.632711'
end_time: '2026-07-11T18:08:17.267486'
duration_seconds: 700.63
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: fumC
  gene_symbol: fumC
  uniprot_accession: Q88M20
  protein_description: 'RecName: Full=Fumarate hydratase class II {ECO:0000255|HAMAP-Rule:MF_00743};
    Short=Fumarase C {ECO:0000255|HAMAP-Rule:MF_00743}; EC=4.2.1.2 {ECO:0000255|HAMAP-Rule:MF_00743};
    AltName: Full=Aerobic fumarase {ECO:0000255|HAMAP-Rule:MF_00743}; AltName: Full=Iron-independent
    fumarase {ECO:0000255|HAMAP-Rule:MF_00743};'
  gene_info: Name=fumC {ECO:0000255|HAMAP-Rule:MF_00743}; Synonyms=fumC-2; OrderedLocusNames=PP_1755;
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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: fumC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: fumC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88M20
- **Protein Description:** RecName: Full=Fumarate hydratase class II {ECO:0000255|HAMAP-Rule:MF_00743}; Short=Fumarase C {ECO:0000255|HAMAP-Rule:MF_00743}; EC=4.2.1.2 {ECO:0000255|HAMAP-Rule:MF_00743}; AltName: Full=Aerobic fumarase {ECO:0000255|HAMAP-Rule:MF_00743}; AltName: Full=Iron-independent fumarase {ECO:0000255|HAMAP-Rule:MF_00743};
- **Gene Information:** Name=fumC {ECO:0000255|HAMAP-Rule:MF_00743}; Synonyms=fumC-2; OrderedLocusNames=PP_1755;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the class-II fumarase/aspartase family. Fumarase
- **Key Domains:** Fum_hydII. (IPR005677); Fumarase/histidase_N. (IPR024083); Fumarase_C_C. (IPR018951); Fumarate_lyase_CS. (IPR020557); Fumarate_lyase_fam. (IPR000362)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "fumC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'fumC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **fumC** (gene ID: fumC, UniProt: Q88M20) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *fumC* (Q88M20, PP_1755) — Fumarate Hydratase Class II from *Pseudomonas putida* KT2440

**UniProt accession:** Q88M20 · **Gene:** *fumC* (synonym *fumC-2*) · **Locus:** PP_1755
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / NCIMB 11950 / KT2440)
**EC:** 4.2.1.2 · **Length:** 464 aa · **Family:** class-II fumarase/aspartase superfamily, fumarase subfamily

## Summary

The gene **fumC** (UniProt **Q88M20**; ordered locus **PP_1755**; synonym *fumC-2*) of *Pseudomonas putida* strain KT2440 encodes **fumarate hydratase class II** ("**fumarase C**"; EC 4.2.1.2), a soluble cytoplasmic metabolic enzyme. Its primary and defining function is to catalyze the **reversible, stereospecific hydration/dehydration of fumarate to L-(S)-malate** — the reaction `(S)-malate ⇌ fumarate + H₂O`. This is a canonical step of the **tricarboxylic acid (TCA / Krebs) cycle**, in which fumarate produced by succinate dehydrogenase is hydrated to malate, which is subsequently oxidized to oxaloacetate. The enzyme is annotated by the curated HAMAP rule MF_00743 and belongs to the **class-II fumarase/aspartase superfamily**.

Class II fumarases (the FumC type) are mechanistically and evolutionarily distinct from the class I fumarases (FumA/FumB in *E. coli*). Class II enzymes are **iron-independent** — they contain no [Fe-S] cluster — and are **heat-stable**, whereas class I enzymes rely on a labile [4Fe-4S] cluster for catalysis. This iron-independence underpins the alternative UniProt names **"aerobic fumarase"** and **"iron-independent fumarase"** and reflects a physiological role as an oxidant-resistant, aerobically-favored fumarase. The enzyme functions as a **homotetramer** with 222 symmetry; its active sites are built from residues contributed by three of the four subunits, so the oligomeric assembly is obligatory for catalysis. Catalysis proceeds by general acid/base–catalyzed *anti* (E2-like) addition/elimination of water across the fumarate double bond, an enormously rate-accelerated reaction, with a conserved His/Ser acid-base pair (His186/Ser316 in Q88M20 numbering) at the catalytic center.

The functional assignment for Q88M20 is strongly supported by multiple lines of evidence: (i) curated UniProt/HAMAP annotation specifying the catalytic activity, pathway, subunit structure, and cytoplasmic localization; (ii) **~61% sequence identity** to the biochemically characterized *E. coli* FumC (P05042), far above the threshold for confident function transfer; (iii) **100% conservation** of the class II fumarase signature motif GSSIMPGKVN and of the two annotated catalytic residues; and (iv) structural and mechanistic studies of orthologs (*E. coli* FumC, *M. tuberculosis* Rv1098c). Among the three fumarase isozymes encoded by KT2440, Q88M20 is the **closest ortholog of canonical *E. coli* FumC**, marking it as the principal class II aerobic fumarase of this organism. No literature ambiguity was encountered: the gene symbol, organism, protein family, and domain architecture are all mutually consistent with a class II fumarase.

---

## Key Findings

### Finding 1 — FumC catalyzes the reversible fumarate ⇌ L-malate interconversion (EC 4.2.1.2)

The primary function of Q88M20 (PP_1755) is the stereospecific, reversible hydration of fumarate to **L-(S)-malate**, the canonical fumarate→malate step of the TCA cycle. UniProt annotation, derived from the curated HAMAP rule MF_00743, assigns Q88M20 to the class-II fumarase/aspartase family with **EC 4.2.1.2** and specifies the catalytic activity `(S)-malate = fumarate + H₂O`. The reaction is highly substrate-specific: the class II fumarase family acts on the *trans*-dicarboxylic olefin fumarate and its hydration product (S)-malate, and does not accept the *cis* isomer (maleate) or other dicarboxylates as productive substrates.

This assignment is grounded in direct experimental characterization of the ortholog. Weaver and colleagues, studying *E. coli* fumarase C, state that "*Fumarase C catalyzes the stereospecific interconversion of fumarate to L-malate as part of the metabolic citric acid or Kreb's cycle*" ([PMID: 8909293](https://pubmed.ncbi.nlm.nih.gov/8909293/)). Because Q88M20 shares this family membership and the full catalytic constellation with *E. coli* FumC (see Finding 6), the same reaction and substrate specificity apply.

### Finding 2 — Class II fumarase is iron-independent, heat-stable, and adapted to aerobic/oxidative-stress conditions

The FumC-type (class II) fumarase is biochemically distinguished from the class I enzymes by being **iron-independent and heat-stable**. In *E. coli*, the *fumC* gene product is a heat-stable fumarase that does not require iron for activity — unlike the [Fe-S]-cluster class I enzymes FumA and FumB. Park and Gunsalus report that "*the fumC gene product is a heat-stable fumarase which does not require iron for activity*" ([PMID: 7592392](https://pubmed.ncbi.nlm.nih.gov/7592392/)). This property explains the UniProt alternate names "aerobic fumarase" and "iron-independent fumarase" for Q88M20.

Physiologically, class II FumC functions as an **oxidant-resistant backup** to the iron-dependent fumarases. Because it lacks a solvent-exposed, oxidation-sensitive [Fe-S] cluster, FumC remains active when superoxide or iron limitation would inactivate the class I enzymes. The same study demonstrates regulatory logic consistent with this role: "*Superoxide radicals also caused increased fumC gene expression; fumA expression was unaffected. Both the superoxide control and the iron control of fumC expression required the SoxR regulatory protein*" ([PMID: 7592392](https://pubmed.ncbi.nlm.nih.gov/7592392/)). Thus FumC is induced under oxidative stress and iron limitation, providing continuity of the TCA-cycle fumarate-hydration step under aerobic and oxidative conditions.

### Finding 3 — FumC is a cytoplasmic homotetramer with a shared inter-subunit active site and acid-base catalytic machinery

The class II fumarase/aspartase superfamily forms **222-symmetric homotetramers** in which each subunit adopts a three-domain, largely α-helical fold, with a central bundle of five long helices contributing to a **20-helix core bundle** at the tetramer center. This fold was first defined by the crystal structure of avian δ-crystallin (a "hijacked" argininosuccinate lyase), which "*is distantly related to the class II fumarases, aspartases, adenylosuccinases*" and whose active-site cleft "*is located on the boundary between three subunits of the tetramer*" ([PMID: 7634077](https://pubmed.ncbi.nlm.nih.gov/7634077/)).

In *E. coli* FumC the catalytic "A" site is assembled from side chains contributed by multiple subunits, and a second nearby anion-binding "B" site exists. Weaver and Banaszak describe "*a binding site for anions which is generated by side chains from three of the four subunits within the tetramer*" ([PMID: 8909293](https://pubmed.ncbi.nlm.nih.gov/8909293/)) — meaning the homotetrameric assembly is obligatory for a functional active site. Studies of the essential class II fumarase Rv1098c from *M. tuberculosis* reveal the catalytic dynamics: "*substrate binding promotes the closure of the active site through conformational changes involving the catalytic SS-loop and the C-terminal domain*," and site-directed mutagenesis identifies "*Ser318 as one of the two acid-base catalysts*" ([PMID: 22561013](https://pubmed.ncbi.nlm.nih.gov/22561013/)). The chemistry itself is a general acid/base–catalyzed *anti* (E2-like) addition/elimination of water across the fumarate double bond — an extraordinarily rate-enhanced hydration in which fumarate hydratase decreases the reaction free-energy barrier by ~30 kcal/mol ([PMID: 36595439](https://pubmed.ncbi.nlm.nih.gov/36595439/)).

### Finding 4 — UniProt confirms the single-step TCA reaction, homotetramer, cytoplasmic localization, and catalytic residues

Direct curated annotation of Q88M20 provides a self-consistent functional picture. The protein is **464 amino acids**; its catalytic activity is `(S)-malate = fumarate + H₂O` (EC 4.2.1.2); its pathway assignment is "*Carbohydrate metabolism; tricarboxylic acid cycle; (S)-malate from fumarate: step 1/1*"; its subunit structure is **homotetramer**; its subcellular location is **cytoplasm**; and its similarity is to the "*class-II fumarase/aspartase family, Fumarase subfamily*". The "step 1/1" designation confirms FumC constitutes the sole enzymatic step converting fumarate to (S)-malate in this pathway module.

The annotated catalytic machinery mirrors the characterized *E. coli* FumC: **Active site 186** (proton donor/acceptor) and **Active site 316**, with binding-site residues at positions 96, 127 (site B), 137, 185, 317, 322, and residue 329 flagged as important for catalytic activity. This residue-level correspondence with the experimentally validated *E. coli* enzyme reinforces the confidence of the functional transfer.

### Finding 5 — KT2440 encodes three fumarase isozymes plus fumarase-superfamily paralogs; FumC specificity is set by active-site residues, not fold

*P. putida* KT2440 possesses metabolic redundancy at the fumarate-hydration step. A UniProt proteome survey (organism 160488) returns **two class II fumarases** — the target *fumC*/Q88M20 (PP_1755, 464 aa) and *fumC-I*/Q88PA6 (459 aa) — plus a **class I fumarase** (Q88PF3, 507 aa). The presence of two *fumC* genes is what the "*fumC-2*" synonym for the target reflects.

The genome also encodes several **fumarase-superfamily relatives** that share the tetrameric fumarase/aspartase fold but catalyze entirely different reactions: *argH* (argininosuccinate lyase), *aspA* (aspartate ammonia-lyase, Q88C45), *purB* (adenylosuccinate lyase, Q88FR7), *pcaB* (3-carboxy-cis,cis-muconate cycloisomerase, Q88N37), and *hmgB* (fumarylacetoacetase, Q88E48). Because these superfamily members share the fold yet diverge in catalytic residues, **substrate specificity is determined by the active-site constellation, not the overall fold**. The *P. putida* 3-carboxy-cis,cis-muconate lactonizing enzyme (CMLE) illustrates this directly: "*PpCMLE is a homotetramer and belongs to the fumarase class II superfamily*" ([PMID: 15301541](https://pubmed.ncbi.nlm.nih.gov/15301541/)), yet it catalyzes a cycloisomerization, not fumarate hydration. FumC's fidelity for fumarate/(S)-malate therefore rests on its conserved class II fumarase catalytic residues (the His/Ser acid-base pair and the SS-loop), which distinguish it from the aspartase/lyase members of the same superfamily.

### Finding 6 — Bioinformatic support: 61% identity to characterized *E. coli* FumC with conserved signature and catalytic residues

A global Needleman–Wunsch alignment of Q88M20 (464 aa) against the experimentally characterized *E. coli* FumC (P05042, 467 aa) yields **60.7% identity over 484 aligned positions** (≈63% over full length). This is far above the ~30–40% identity threshold generally considered sufficient for confident transfer of enzyme function. The class II fumarase / fumarate-lyase family signature motif **GSSIMPGKVN** is present and **100% identical** in Q88M20 (residues 315–324), *E. coli* FumC (317–326), and the paralog *fumC-I*/Q88PA6 (312–321). The two UniProt-annotated catalytic residues are conserved: **His186** (within the …GRTH… motif; the proton donor/acceptor) and **Ser316** (the first serine of the GSSIMPGKVN motif, equivalent to the *E. coli*/Rv1098c Ser318 acid-base catalyst). This convergence of high overall identity, an intact family signature, and conserved catalytic residues provides strong bioinformatic confirmation of fumarase function.

### Finding 7 — Q88M20 is the closest ortholog of canonical *E. coli* FumC among KT2440's fumarases

Pairwise global identity comparisons place Q88M20 unambiguously as the principal class II fumarase of KT2440:

| Comparison | Global identity |
|---|---|
| Q88M20 (target) vs *E. coli* FumC (P05042) | **60.7%** |
| *fumC-I* (Q88PA6) vs *E. coli* FumC | 49.2% |
| Q88M20 vs *fumC-I* (Q88PA6) | 50.4% |
| Q88M20 vs KT2440 class I fumarase (Q88PF3) | 28.0% |

Among the three KT2440 fumarases, the target is the **most similar to the biochemically characterized *E. coli* FumC** and only distantly related (28%) to the mechanistically unrelated class I fumarase. This identifies Q88M20 as the organism's principal aerobic class II fumarase, with *fumC-I* serving as a second, more divergent class II paralog.

---

## Mechanistic Model / Interpretation

### The catalyzed reaction and its metabolic context

FumC operates at a specific junction of central carbon metabolism. In the oxidative TCA cycle, it catalyzes:

```
        succinate
           │  (succinate dehydrogenase, Complex II)
           ▼
        FUMARATE  ──────────────►  L-(S)-MALATE  ──────►  oxaloacetate
                    FumC (class II)      │  (malate dehydrogenase)
                    + H₂O                ▼
                    EC 4.2.1.2       to citrate synthase
      (reversible, stereospecific hydration)
```

FumC constitutes the sole enzymatic step for the fumarate→(S)-malate conversion in this pathway module ("step 1/1"). The reaction is freely reversible; its net direction is set by metabolic flux and the concentrations of fumarate and malate.

### Structure–function logic

```
   Class II fumarase (FumC) — homotetramer, 222 symmetry
   ┌───────────────────────────────────────────────┐
   │  4 subunits × 3 α-helical domains each         │
   │  central 20-helix core bundle                  │
   │  Active site A: built from 3 of 4 subunits     │
   │     ─ His186 (proton donor/acceptor)           │
   │     ─ Ser316 (acid-base catalyst; SS-loop)     │
   │     ─ signature motif GSSIMPGKVN (315–324)     │
   │  Site B: second anion-binding site             │
   │  NO [Fe-S] cluster → iron-independent, aerobic │
   └───────────────────────────────────────────────┘
             │
             ▼  general acid/base anti (E2-like) addition of water
        fumarate + H₂O  ⇌  (S)-malate   (ΔΔG‡ ≈ 30 kcal/mol rate enhancement)
```

Three structural features are decisive for function. First, the **obligatory homotetramer**: because the active site is assembled from residues of three different subunits, no monomer or dimer can be catalytically competent. Second, the **conserved acid-base pair (His186/Ser316) and the mobile SS-loop**, which close over the bound substrate and execute the *anti* addition/elimination of water. Third, the **absence of an iron-sulfur cluster**, which distinguishes class II from class I fumarases and confers heat stability and resistance to oxidative/iron-limiting stress.

### Why the class assignment matters physiologically

Class I and class II fumarases are convergent solutions to the same chemical problem but are not homologous. Class I enzymes (e.g., *E. coli* FumA/FumB) use a [4Fe-4S] cluster and are inactivated by superoxide and iron starvation; class II enzymes (FumC) are iron-free and robust under these conditions. This dichotomy is underscored by structural work on parasite fumarases, where inhibitor selectivity for class I FHs "*is due to direct coordination of the inhibitor to the unique Fe of the catalytic [4Fe-4S] cluster … but is absent from class II human FH*" ([PMID: 30645090](https://pubmed.ncbi.nlm.nih.gov/30645090/)). The regulatory data from *E. coli* — SoxR-dependent induction of *fumC* by superoxide and iron limitation — indicate that class II fumarase acts as a **stress-resistant safeguard** for TCA-cycle continuity. In an obligate aerobe like *P. putida* KT2440, which experiences substantial oxidative load during aerobic metabolism and the degradation of aromatic and other compounds, an iron-independent, heat-stable fumarase is a physiologically sensible principal isozyme.

### Distinguishing FumC from its superfamily relatives

The fumarase class II fold is a metabolic "chassis" reused across several reactions (aspartate ammonia-lyase, argininosuccinate lyase, adenylosuccinate lyase, CMLE, δ-crystallin). The aspartase/fumarase superfamily shares "*a monomer that is composed of three domains oriented in an elongated S-shape*" with "*active sites located in clefts between the subunits*" ([PMID: 10800598](https://pubmed.ncbi.nlm.nih.gov/10800598/)). Specificity for fumarate/(S)-malate is not conferred by the fold but by the exact set of active-site residues. Q88M20 carries the fumarase-specific His/Ser catalytic pair and the intact GSSIMPGKVN signature, and its high identity to the validated *E. coli* FumC rules out the possibility that it is an aspartase or lyase misannotated as a fumarase.

---

## Evidence Base

| PMID | Title (abbrev.) | Relevance |
|---|---|---|
| [8909293](https://pubmed.ncbi.nlm.nih.gov/8909293/) | *Crystallographic studies of the catalytic and a second site in fumarase C from E. coli* | **Primary support.** Defines the reaction ("stereospecific interconversion of fumarate to L-malate") and the inter-subunit active site ("side chains from three of the four subunits"). Anchors Findings 1 and 3. |
| [7592392](https://pubmed.ncbi.nlm.nih.gov/7592392/) | *Oxygen, iron, carbon and superoxide control of fumA and fumC genes of E. coli* | **Primary support.** Establishes FumC as heat-stable and iron-independent, and induced by superoxide/iron-limitation via SoxR. Anchors Finding 2. |
| [22561013](https://pubmed.ncbi.nlm.nih.gov/22561013/) | *Conformational changes upon ligand binding in class II fumarase Rv1098c (M. tuberculosis)* | **Primary support.** Provides the catalytic mechanism: SS-loop/C-terminal closure and Ser as an acid-base catalyst. Anchors Finding 3. |
| [36595439](https://pubmed.ncbi.nlm.nih.gov/36595439/) | *Revisiting the Burden Borne by Fumarase: Enzymatic Hydration of an Olefin* | Supports the mechanistic model — ~30 kcal/mol rate enhancement for olefin hydration. Contextualizes Finding 3. |
| [7634077](https://pubmed.ncbi.nlm.nih.gov/7634077/) | *Structure of avian δ-crystallin: a new fold for a superfamily of oligomeric enzymes* | Defines the 222-symmetric tetramer fold and inter-subunit active-site cleft shared across the class II fumarase/aspartase superfamily. Supports Findings 3 and 5. |
| [15301541](https://pubmed.ncbi.nlm.nih.gov/15301541/) | *Crystal structure of 3-carboxy-cis,cis-muconate lactonizing enzyme from P. putida* | Shows *P. putida* encodes catalytically distinct class II superfamily members ("PpCMLE is a homotetramer and belongs to the fumarase class II superfamily"). Supports Finding 5 (specificity from residues, not fold). |
| [10800598](https://pubmed.ncbi.nlm.nih.gov/10800598/) | *L-aspartase: new tricks from an old enzyme* | Describes the shared S-shaped three-domain monomer, tetrameric assembly, and inter-subunit active sites of the aspartase/fumarase superfamily. Contextual support for Findings 3 and 5. |
| [2656658](https://pubmed.ncbi.nlm.nih.gov/2656658/) | *Nucleotide sequence of the FNR-regulated fumB gene of E. coli* | Establishes that class I fumarases share only one short consensus motif (Gly-Ser-Xxx-Ile-Met-...-Lys-Xxx-Asn) with the class II enzyme and are otherwise unrelated iron-containing hydrolyases. Contextualizes class I vs II distinction (Findings 2, 7). |
| [9418241](https://pubmed.ncbi.nlm.nih.gov/9418241/) | *Regulation of fumB gene expression in E. coli* | Confirms the three distinct fumarases (FumA/FumB/FumC) and their aerobic vs anaerobic expression, contextualizing FumC as the aerobic class II enzyme. |
| [30645090](https://pubmed.ncbi.nlm.nih.gov/30645090/) | *Crystal structures of fumarate hydratases from Leishmania major with 2-thiomalate* | Highlights the mechanistic split between class I ([4Fe-4S], class-specific inhibitor coordination) and class II (no Fe cluster, as in human/bacterial FumC), reinforcing the iron-independent nature of FumC. |

**Consistency assessment:** All ten reviewed papers are mutually consistent with the assignment of Q88M20 as a class II fumarase. No literature was found describing a different gene product under the *fumC* symbol that would create ambiguity. The gene symbol (*fumC*), organism (*P. putida* KT2440), protein family (class-II fumarase/aspartase), and InterPro domains (Fum_hydII IPR005677; Fumarase_C_C IPR018951; Fumarate_lyase_CS IPR020557) all align.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of Q88M20 itself.** The functional assignment rests on curated annotation, sequence homology, and structural/mechanistic studies of orthologs (*E. coli* FumC, *M. tuberculosis* Rv1098c). No published kinetic parameters (kcat, Km for fumarate/L-malate), no purified-protein assay, and no crystal structure specific to the *P. putida* KT2440 enzyme were identified. Function is inferred by homology, albeit at high confidence (~61% identity, intact catalytic residues).

2. **Localization is inferred, not experimentally demonstrated.** Cytoplasmic localization is the UniProt/HAMAP annotation and is consistent with the soluble, non-membrane nature of the class II fumarase fold and its TCA-cycle role, but no proteomic or fluorescence-based localization study specific to PP_1755 was found.

3. **Physiological division of labor between the isozymes is uncharacterized in *P. putida*.** KT2440 encodes two class II fumarases (Q88M20 and *fumC-I*/Q88PA6) plus a class I fumarase (Q88PF3). The specific growth conditions under which each is expressed, their relative flux contributions, and any regulatory hierarchy (analogous to the SoxR/ArcA/FNR control in *E. coli*) have not been directly established for *P. putida*.

4. **Regulatory inference is cross-species.** The oxidative-stress/iron-limitation induction and SoxR dependence are documented in *E. coli*. Whether the same regulatory logic governs *P. putida* PP_1755 remains to be verified experimentally.

5. **Substrate-specificity boundaries not directly tested for the *P. putida* enzyme.** Family-level specificity (fumarate/(S)-malate; exclusion of maleate and non-cognate dicarboxylates) is inferred from the conserved active site and from characterized orthologs, not measured for Q88M20.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and steady-state kinetics.** Clone PP_1755, express and purify the His-tagged protein, and measure kcat and Km for fumarate hydration and L-malate dehydration. Confirm stereospecificity ((S)- vs (R)-malate) and test candidate non-substrates (maleate, D-malate, aspartate) to delimit specificity.

2. **Iron-independence and thermostability assays.** Verify absence of [Fe-S] cluster (UV-vis, iron content, EPR) and measure thermal stability, directly confirming the class II designation for the *P. putida* enzyme.

3. **Structural determination.** Solve the crystal or cryo-EM structure of Q88M20 (apo and with malate/inhibitor) to confirm the homotetramer, the inter-subunit active site, and the His186/Ser316 catalytic geometry. Alternatively, validate an AlphaFold model against the *E. coli* FumC template using structural-biology tooling.

4. **Site-directed mutagenesis of predicted catalytic residues.** Mutate His186 and Ser316 (and site-B residues) and measure the loss of activity to experimentally confirm their catalytic roles in the *P. putida* enzyme.

5. **Genetic dissection of isozyme roles.** Construct single and combinatorial deletions of PP_1755, *fumC-I* (Q88PA6), and the class I fumarase (Q88PF3), and assess growth on TCA-cycle-dependent carbon sources under aerobic, oxidative-stress (paraquat), and iron-limited conditions to define each isozyme's physiological niche.

6. **Expression profiling under stress.** Use RT-qPCR or RNA-seq to test whether PP_1755 is induced by superoxide generators and iron chelation, probing whether the *E. coli*-like SoxR/oxidative-stress regulation is conserved in *P. putida*.

---

## Conclusion

The gene *fumC* (Q88M20, PP_1755) of *Pseudomonas putida* KT2440 encodes **fumarate hydratase class II (fumarase C, EC 4.2.1.2)**, a **cytoplasmic, iron-independent, heat-stable homotetramer** that catalyzes the **reversible, stereospecific hydration of fumarate to L-(S)-malate** as the fumarate→malate step of the **TCA cycle**. Its active sites are shared across subunits and employ a conserved His186/Ser316 acid-base pair and a mobile SS-loop to perform general acid/base *anti* addition of water. As a class II enzyme it functions as an aerobic, oxidant-resistant fumarase. The assignment is supported by curated annotation, ~61% identity to the biochemically characterized *E. coli* FumC with 100% conservation of the class II catalytic motif and residues, and by structural/mechanistic studies of orthologs — while acknowledging that no direct biochemical characterization of the *P. putida* enzyme itself has yet been published.


## Artifacts

- [OpenScientist final report](fumC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](fumC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:8909293
2. PMID:7592392
3. PMID:7634077
4. PMID:22561013
5. PMID:36595439
6. PMID:15301541
7. PMID:30645090
8. PMID:10800598