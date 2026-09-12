---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T16:19:41.792911'
end_time: '2026-07-11T16:42:38.001372'
duration_seconds: 1376.21
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: metH
  gene_symbol: metH
  uniprot_accession: Q88KB5
  protein_description: 'RecName: Full=Methionine synthase {ECO:0000256|ARBA:ARBA00013998,
    ECO:0000256|NCBIfam:TIGR02082}; EC=2.1.1.13 {ECO:0000256|ARBA:ARBA00012032, ECO:0000256|NCBIfam:TIGR02082};
    AltName: Full=5-methyltetrahydrofolate--homocysteine methyltransferase {ECO:0000256|ARBA:ARBA00031040,
    ECO:0000256|PIRNR:PIRNR000381};'
  gene_info: Name=metH {ECO:0000313|EMBL:AAN67988.1}; OrderedLocusNames=PP_2375 {ECO:0000313|EMBL:AAN67988.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the vitamin-B12 dependent methionine synthase
  protein_domains: Cbl-bd_cap. (IPR003759); Cobalamin-bd. (IPR006158); Cobalamin-bd_sf.
    (IPR036724); Dihydropteroate_synth-like_sf. (IPR011005); HCY_dom. (IPR003726)
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
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: metH-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: metH-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88KB5
- **Protein Description:** RecName: Full=Methionine synthase {ECO:0000256|ARBA:ARBA00013998, ECO:0000256|NCBIfam:TIGR02082}; EC=2.1.1.13 {ECO:0000256|ARBA:ARBA00012032, ECO:0000256|NCBIfam:TIGR02082}; AltName: Full=5-methyltetrahydrofolate--homocysteine methyltransferase {ECO:0000256|ARBA:ARBA00031040, ECO:0000256|PIRNR:PIRNR000381};
- **Gene Information:** Name=metH {ECO:0000313|EMBL:AAN67988.1}; OrderedLocusNames=PP_2375 {ECO:0000313|EMBL:AAN67988.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the vitamin-B12 dependent methionine synthase
- **Key Domains:** Cbl-bd_cap. (IPR003759); Cobalamin-bd. (IPR006158); Cobalamin-bd_sf. (IPR036724); Dihydropteroate_synth-like_sf. (IPR011005); HCY_dom. (IPR003726)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "metH" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'metH' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **metH** (gene ID: metH, UniProt: Q88KB5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *metH* (Q88KB5) — Cobalamin-Dependent Methionine Synthase of *Pseudomonas putida* KT2440

**Target:** metH / PP_2375, UniProt **Q88KB5**
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440), taxon "PSEPK"
**Assigned function:** Cobalamin (vitamin B12)-dependent methionine synthase; 5-methyltetrahydrofolate–homocysteine methyltransferase; **EC 2.1.1.13**

## Summary

The gene **metH** (ordered locus **PP_2375**; UniProt **Q88KB5**) of *Pseudomonas putida* strain KT2440 encodes the **cobalamin (vitamin B12)-dependent methionine synthase** (EC 2.1.1.13), also known as **5-methyltetrahydrofolate–homocysteine methyltransferase**. Its primary and defining function is to catalyze the **terminal step of de novo L-methionine biosynthesis**: transfer of a methyl group from **N5-methyltetrahydrofolate (CH3-THF)** to **L-homocysteine**, producing **L-methionine and tetrahydrofolate (THF)**. This single reaction sits at the junction of two central metabolic cycles — the folate/one-carbon cycle (which regenerates THF for one-carbon metabolism) and the methionine/S-adenosylmethionine (SAM) cycle (which supplies the universal methyl donor for cellular methylation). The gene product is a large, soluble, **cytoplasmic** protein.

The functional assignment rests on multiple, mutually reinforcing lines of evidence. Q88KB5 carries the complete four-module domain architecture diagnostic of the MetH family (a Zn-binding homocysteine domain, a folate-binding domain, a cobalamin-binding module with cap, and a C-terminal AdoMet-binding reactivation domain), and it is **67.6% identical over its full length** to the extensively biochemically and structurally characterized *Escherichia coli* MetH. Critically, **every experimentally validated catalytic residue** of *E. coli* MetH — the three zinc-ligating cysteines, the His-Asp-Ser cobalamin lower-axial triad, and the reactivation-domain tyrosine — is conserved at the aligned position in Q88KB5, establishing that the *P. putida* enzyme is catalytically complete and mechanistically equivalent.

Mechanistically, MetH uses an enzyme-bound cobalamin as an **intermediate methyl carrier** that cycles between methylcobalamin and cob(I)alamin during turnover, with an active-site **Zn2+** ion activating the homocysteine thiol and a **His-on/His-off** cobalt coordination switch driving major domain rearrangements between catalytic conformations. Because the highly reactive cob(I)alamin intermediate is occasionally oxidized to inactive cob(II)alamin (roughly once per ~2,000 turnovers), the enzyme requires periodic **reductive reactivation** using an electron from reduced flavodoxin and a methyl group from S-adenosylmethionine. Notably, KT2440 also encodes a cobalamin-**independent** MetE-family methionine synthase and cobalamin-biosynthesis/salvage genes, indicating that MetH is likely **conditionally rather than absolutely essential** in this organism.

---

## Key Findings

### F001 — Q88KB5 is a cobalamin-dependent methionine synthase catalyzing the terminal step of methionine biosynthesis (EC 2.1.1.13)

The core functional identity of Q88KB5 is firmly established by convergent database annotation and domain analysis. UniProt Q88KB5 is annotated by two independent orthology-based resources — **TIGRFAM TIGR02082** and **PIRSF PIRNR000381** — as methionine synthase / 5-methyltetrahydrofolate–homocysteine methyltransferase, EC 2.1.1.13. Its InterPro domain complement precisely matches the modular architecture of the biochemically characterized enzyme: the **HCY domain (IPR003726)** provides the zinc/homocysteine-binding site; the **dihydropteroate-synthase-like TIM-barrel superfamily fold (IPR011005)** provides the folate/pterin-binding module; and the paired **cobalamin-binding domain (IPR006158)** plus **Cbl-binding cap (IPR003759)** form the B12-binding module.

Functionally, the enzyme transfers a methyl group from N5-methyltetrahydrofolate to homocysteine, producing methionine plus tetrahydrofolate, using a zinc ion to activate the thiol of homocysteine. This mechanism is established for the MetH family and directly supported by computational and structural work: *"Cobalamin-dependent methionine synthase (MetH) is an important metalloenzyme responsible for the biosynthesis of methionine. It catalyzes methyl transfer from N(5)-methyl-tetrahydrofolate to homocysteine (Hcy) by using a zinc ion to activate the Hcy substrate"* ([PMID: 21837727](https://pubmed.ncbi.nlm.nih.gov/21837727/)). This defines both the catalyzed reaction and the substrate specificity: the enzyme is specific for **N5-methyltetrahydrofolate** as the methyl donor and **L-homocysteine** as the methyl acceptor.

### F002 — MetH is a large (~136 kDa) modular enzyme built from four domains that reorganize between distinct catalytic conformations

The MetH family enzyme is a large multimodular protein. In *E. coli*, MetH is a **136-kDa** enzyme carrying a cobalamin chromophore, built from four modules: (1) a homocysteine(Zn)-binding domain, (2) a methyltetrahydrofolate-binding domain, (3) a cobalamin-binding module with an accompanying cap, and (4) a C-terminal S-adenosylmethionine (AdoMet)-binding reactivation domain. Because the single cobalamin cofactor must react with three different substrates located in different modules, the enzyme cannot adopt one static conformation; instead it undergoes major domain rearrangements to bring the cobalamin into productive contact with each partner in turn.

As the primary literature states: *"Cobalamin-dependent methionine synthase (MetH) is a 136-kDa multimodular enzyme with a cobalamin chromophore; the color of the cobalamin reflects the conformation of the protein. The enzyme contains four modules and catalyzes three different methyl transfer reactions that require different arrangements of these modules"* ([PMID: 12832615](https://pubmed.ncbi.nlm.nih.gov/12832615/)). The cobalamin's color reports the conformational state, revealing an ensemble of interconverting conformers whose distribution is shifted by substrate and product binding. This architecture is directly relevant to Q88KB5, which at **1,235 amino acids** is co-linear with the *E. coli* enzyme and preserves the same four-module organization (see F005).

### F003 — Catalysis proceeds via a methylcobalamin/cob(I)alamin cycle with His-on/His-off cobalt coordination switching

During each turnover, the cobalamin prosthetic group alternates between two states. Homocysteine demethylates methylcobalamin, producing methionine and highly reactive cob(I)alamin; cob(I)alamin is then remethylated by CH3-THF to regenerate methylcobalamin. The methyl transfer from methylcobalamin to homocysteine is the key catalytic step of the productive cycle: *"The prosthetic group alternates between methylcobalamin and cob(I)alamin during catalysis as homocysteine is converted to methionine using a methyl group derived from methyltetrahydrofolate"* ([PMID: 17924667](https://pubmed.ncbi.nlm.nih.gov/17924667/)).

On the folate side, the methyl group cannot be transferred from CH3-THF unless the folate is first chemically activated. The favored mechanism is **protonation at N5** of the tetrahydropterin ring prior to methyl transfer: *"Activation of CH(3)-H(4)folate by protonation prior to transfer of the methyl group has been the favored mechanism"* ([PMID: 11076529](https://pubmed.ncbi.nlm.nih.gov/11076529/)). This protonation raises the leaving-group ability of the folate nitrogen and enables the methyl to be captured by the super-nucleophilic cob(I)alamin. The imidazole of the conserved histidine (His759 in *E. coli*; His761 in Q88KB5) coordinates the cobalt in a **His-on** state and dissociates in a **His-off** state; the His-off state is associated with the reactivation conformation, and the cobalt coordination and trans-ligand influence govern the conformational equilibrium and the affinity for flavodoxin.

### F004 — Occasional cofactor oxidation requires reductive reactivation using reduced flavodoxin and AdoMet

Because the cobalamin serves as both acceptor and donor of the methyl group, the reactive cob(I)alamin intermediate is intrinsically vulnerable to oxidation. Approximately **once every ~2,000 catalytic cycles**, the cofactor is oxidized to catalytically dead **cob(II)alamin** and must be rescued. Rescue is not spontaneous: it requires uptake of **one electron from reduced flavodoxin** together with a **methyl group from S-adenosyl-L-methionine (AdoMet)**, a reaction carried out by the C-terminal reactivation module: *"The cobalamin cofactor, which serves as both acceptor and donor of the methyl group, is oxidized once every approximately 2,000 catalytic cycles and must be reactivated by the uptake of an electron from reduced flavodoxin and a methyl group from S-adenosyl-L-methionine (AdoMet)"* ([PMID: 19846791](https://pubmed.ncbi.nlm.nih.gov/19846791/)).

Structural work illuminates how the enzyme accomplishes the thermodynamically challenging Co(II)→Co(I) reduction: it lowers the reduction potential by elongating the cobalt-axial ligand bond so that the cobalt becomes effectively four-coordinate, with a conserved tyrosine (Tyr1139 in *E. coli*; Tyr1143 in Q88KB5) stabilizing this state. In some organisms (e.g., *Thermotoga maritima*), the reactivation function is even supplied *in trans* by a separate protein (TM0269; [PMID: 17656578](https://pubmed.ncbi.nlm.nih.gov/17656578/)), underscoring the modular, semi-autonomous nature of the reactivation domain that Q88KB5 encodes as its C-terminus.

### F005 — Q88KB5 is a full-length ortholog of *E. coli* MetH (67.6% identity) with all catalytic residues conserved

The strongest species-specific evidence comes from direct sequence comparison. A global Needleman-Wunsch alignment of Q88KB5 (*P. putida* KT2440 MetH, 1,235 aa) against *E. coli* MetH (UniProt P13009, 1,227 aa) yields **68.0% identity over 1,220 aligned positions (67.6% over the full *E. coli* length)**, with only ~22 gap columns. This demonstrates a co-linear four-module architecture with no domain gain or loss — true one-to-one orthology rather than a distant or truncated homolog.

Most importantly, every experimentally characterized catalytic residue of *E. coli* MetH is identically conserved at the aligned position in Q88KB5:

| Functional role | *E. coli* MetH (P13009) | Q88KB5 (*P. putida*) |
|---|---|---|
| Homocysteine-domain Zn2+ ligand | Cys247 | Cys250 |
| Homocysteine-domain Zn2+ ligand | Cys310 | Cys313 |
| Homocysteine-domain Zn2+ ligand | Cys311 | Cys314 |
| Cobalamin lower-axial His | His759 | His761 |
| Cobalamin triad Asp | Asp757 | Asp759 |
| Cobalamin triad Ser | Ser810 | Ser812 |
| Reactivation-domain Tyr | Tyr1139 | Tyr1143 |

The complete conservation of the Zn-thiolate cluster (which activates homocysteine), the His-Asp-Ser triad (which controls cobalt coordination and conformational switching), and the reactivation tyrosine (which stabilizes the four-coordinate cob(II)alamin during reductive reactivation) establishes that Q88KB5 is catalytically complete and mechanistically equivalent to the reference enzyme. Sequences were retrieved from the UniProt REST API (2026-07).

### F006 — *P. putida* KT2440 encodes both MetH (B12-dependent) and a MetE-family (B12-independent) methionine synthase, plus cobalamin-biosynthesis genes

Genomic context clarifies the physiological role and essentiality of MetH. A UniProt proteome query (organism_id 160488) shows that in addition to *metH*/Q88KB5 (PP_2375, 1,235 aa, EC 2.1.1.13), KT2440 carries a *metE* gene, **Q88JF1 (PP_2698)**, annotated as 5-methyltetrahydropteroyltriglutamate–homocysteine methyltransferase — the **cobalamin-independent methionine synthase** family (EC 2.1.1.14) — as well as a second MetE-family protein, **Q88E31 (PP_4637)**. The genome also encodes cobalamin/corrinoid biosynthesis and salvage functions (e.g., *cbiD*/PP_4831, cobalt-precorrin-5B C1-methyltransferase; *cysG*/*cobA-2*/PP_3999, siroheme/precorrin synthase) and the downstream methionine-utilizing enzyme *metK*/PP_4967 (S-adenosylmethionine synthase, EC 2.5.1.6).

The presence of both a B12-dependent (MetH) and a B12-independent (MetE) methionine synthase means the two enzymes are functionally redundant for methionine synthesis but differ in cofactor requirement. MetH is faster and more efficient but requires cobalamin; MetE is B12-independent but catalytically slower. This dual-route arrangement strongly implies that MetH is **conditionally essential** — preferred when cobalamin is available, but dispensable when MetE can supply methionine. This mirrors the MetH/MetE relationship in other organisms, where cobalamin availability governs which enzyme is used: in the alga *Chlamydomonas reinhardtii*, cobalamin-producing bacteria enable MetH-mediated methionine synthesis under conditions where MetE fails ([PMID: 23486253](https://pubmed.ncbi.nlm.nih.gov/23486253/)).

### F007 — Q88KB5 is a soluble cytoplasmic protein with no signal peptide or transmembrane segments, carrying the canonical B12-binding DxHxxG motif

Sequence-based localization analysis places Q88KB5 firmly in the **cytoplasm**, consistent with its role in central intracellular biosynthesis. Kyte-Doolittle hydropathy analysis (window 19) yields a maximum windowed hydropathy of only **1.51**, with **zero** windows exceeding the ~1.6 threshold indicative of a transmembrane helix — the protein has no predicted transmembrane segments. The N-terminus (MSDRSARLQALQNALKER...) is hydrophilic (maximum hydropathy in the first 30 residues = 0.36) and lacks the hydrophobic n/h-region of a secretion signal peptide, so the protein is not secreted or membrane-targeted. The overall charged-residue fraction (D/E/K/R) of **24.7%** is typical of soluble cytoplasmic proteins.

The analysis also confirms the diagnostic cofactor-binding signature: the cobalamin lower-axial ligand His761 sits within the sequence context `...KGDVHDIGKN...`, matching the canonical **DxHxxG "base-off/His-on"** B12-binding motif (Asp-x-His...Gly) shared by cobalamin-dependent enzymes. This motif is the structural hallmark that allows the histidine to displace the cobalamin's own dimethylbenzimidazole tail and coordinate the cobalt from below the corrin ring — the essential feature underlying the His-on/His-off switching described in F003.

---

## Mechanistic Model / Interpretation

Q88KB5 (MetH) is best understood as the **methyl-transfer nexus that couples two central metabolic cycles** in the *P. putida* cytoplasm. The following diagram summarizes its catalytic cycle and its integration into one-carbon metabolism:

```
        FOLATE / ONE-CARBON CYCLE                METHIONINE / SAM CYCLE
       ┌────────────────────────┐              ┌────────────────────────┐
       │                        │              │                        │
   CH3-THF ──(N5 protonation)──►│              │◄── L-Homocysteine      │
       │                        ▼              ▼        (thiol,          │
       │              ┌───────────────────────────┐     Zn2+-activated)  │
       │              │        MetH (Q88KB5)       │                     │
       │              │  ┌──────────────────────┐  │                     │
       │              │  │  Enzyme-bound         │  │                     │
       │   remethylate│  │  COBALAMIN carrier    │  │ demethylate         │
       │   cob(I)     │  │  MeCbl  <──►  Cob(I)  │  │ MeCbl               │
       │              │  └──────────────────────┘  │                     │
       │              └───────────────────────────┘                     │
       ▼                        │              │                        ▼
      THF ─────────────────────►│              │◄──── L-Methionine ──► SAM (via MetK)
   (returns to one-carbon pool) │              │      (methyl acceptor)  │
                                └──────────────┘                        
                        Reaction: CH3-THF + L-Hcy → THF + L-Met

   REACTIVATION (once per ~2,000 turnovers, when cob(I) → cob(II)):
       cob(II)alamin + e⁻ (reduced flavodoxin) + CH3 (AdoMet)  → MeCbl
       (C-terminal reactivation domain; Tyr1143 stabilizes 4-coordinate Co)
```

The enzyme's four modules act as a **molecular assembly line for a single mobile cofactor**. The cobalamin, tethered in the B12-binding module, is swung sequentially into contact with (1) the folate-binding module to accept a methyl group from protonated CH3-THF (yielding methylcobalamin and THF), (2) the homocysteine-binding module to donate that methyl to Zn2+-activated homocysteine (yielding methionine and cob(I)alamin), and, when repair is needed, (3) the reactivation module to receive an electron from flavodoxin and a methyl from AdoMet. The His-on/His-off switch of His761 and the trans-influence of the axial ligand act as the conformational "gearbox" partitioning the enzyme among these arrangements (F003, F007).

Physiologically, MetH performs the **committed, terminal step of methionine biosynthesis**, regenerating THF (which re-enters the one-carbon pool for nucleotide and amino-acid synthesis) and producing methionine (which is converted by MetK/PP_4967 to SAM, the cell's universal methyl donor). The genomic co-occurrence of a B12-independent MetE backup (Q88JF1) and cobalamin-biosynthesis genes (F006) means *P. putida* has flexible, cofactor-conditional control over this node: when B12 is available, the efficient MetH route operates; when B12 is scarce, MetE can substitute. This makes MetH **conditionally essential** rather than absolutely required for viability.

**Localization:** All evidence — absence of transmembrane helices or a signal peptide, high charged-residue content, and requirement for soluble partners (flavodoxin, AdoMet, folate, homocysteine) — places MetH's activity in the **cytoplasm** (F007), where the folate and methionine cycles operate.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|---|---|---|
| [21837727](https://pubmed.ncbi.nlm.nih.gov/21837727/) | *Zinc-homocysteine binding in MetH... QM/MM studies* | Establishes the catalyzed reaction (CH3-THF → Hcy) and Zn2+-based thiol activation defining MetH function (F001). |
| [12832615](https://pubmed.ncbi.nlm.nih.gov/12832615/) | *Factors modulating conformational equilibria in MetH* | Documents the ~136 kDa size, four-module architecture, and cobalamin-reported conformational cycling (F002). |
| [17924667](https://pubmed.ncbi.nlm.nih.gov/17924667/) | *Ligand trans influence governs conformation in MetH* | Describes the methylcobalamin/cob(I)alamin catalytic cycle carrying the methyl between folate and homocysteine (F003). |
| [11076529](https://pubmed.ncbi.nlm.nih.gov/11076529/) | *Protonation state of methyltetrahydrofolate in MetH* | Supports N5-protonation activation of CH3-THF before methyl transfer (F003). |
| [19846791](https://pubmed.ncbi.nlm.nih.gov/19846791/) | *Insights into the reactivation of MetH* | States the reactivation requirement: reduced flavodoxin (electron) + AdoMet (methyl) regenerate active methylcobalamin (F004). |
| [23486253](https://pubmed.ncbi.nlm.nih.gov/23486253/) | *Chlamydomonas thermal tolerance via B12-producing bacteria* | Illustrates the MetH/MetE cofactor-conditional relationship relevant to essentiality (F006). |
| [18332423](https://pubmed.ncbi.nlm.nih.gov/18332423/) | *Disulfide-stabilized conformer reveals role of His ligand* | Structural basis for His-on/His-off switching of the cobalamin axial ligand (F003). |
| [17656578](https://pubmed.ncbi.nlm.nih.gov/17656578/) | *Reactivation of T. maritima MetH requires TM0269* | Demonstrates the modular, sometimes *trans*-acting reactivation domain (F004). |
| [21417249](https://pubmed.ncbi.nlm.nih.gov/21417249/) | *Two-step methyl cation transfer mechanism in MetH* | Mechanistic detail on methyl-Co(cobalamin) intermediate formation (F003). |

Supporting database evidence (not primary literature) includes UniProt/InterPro/TIGRFAM/PIRSF annotations for Q88KB5 (F001), the UniProt REST sequence alignment against *E. coli* P13009 (F005), the UniProt proteome query for KT2440 (organism_id 160488) identifying *metE* and cobalamin-biosynthesis genes (F006), and the in-house Kyte-Doolittle hydropathy/motif analysis of the Q88KB5 sequence (F007).

**Note on the literature landscape:** No primary experimental studies of the *P. putida* KT2440 MetH enzyme specifically were identified; the functional assignment relies on (a) authoritative structural/biochemical/computational studies of the closely related, extensively characterized *E. coli* MetH and (b) sequence-, domain-, and genome-context analyses specific to Q88KB5. Because Q88KB5 is a full-length ortholog with 67.6% identity and complete conservation of all catalytic residues, transfer of the *E. coli* mechanism to the *P. putida* enzyme is very well supported. Importantly, the gene symbol *metH* is **not ambiguous** here — it unambiguously corresponds to the cobalamin-dependent methionine synthase, and all literature and domain evidence align with the UniProt-provided identity.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of Q88KB5.** All enzymatic, structural, and mechanistic claims are inferred from orthology to *E. coli* MetH (and related family members). There is no published in vitro assay, crystal structure, or kinetic measurement of the *P. putida* KT2440 protein itself. The inference is strong (full-length orthology, all catalytic residues conserved) but remains inference.

2. **Essentiality is inferred, not measured.** The conclusion that MetH is *conditionally* essential rests on the genomic presence of a MetE-family backup (Q88JF1/PP_2698, plus PP_4637) and cobalamin-biosynthesis genes. No gene-knockout or transposon-fitness data specific to *metH*/PP_2375 in KT2440 were reviewed to confirm whether MetH loss is tolerated under standard growth or only under B12-replete conditions.

3. **Cofactor supply and regulation unexamined.** Whether *P. putida* KT2440 synthesizes sufficient cobalamin de novo to support MetH under all conditions, and how *metH* versus *metE* expression is regulated (e.g., by B12-riboswitches or methionine availability), was not established from primary data.

4. **Reactivation partners not confirmed in *P. putida*.** The identity of the physiological reductant (flavodoxin vs. flavodoxin/ferredoxin homologs) for MetH reactivation in KT2440 was inferred from the *E. coli* paradigm, not verified in this organism.

5. **Localization is computational.** Cytoplasmic localization is predicted from sequence (no signal peptide, no TM segments) rather than demonstrated experimentally.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and enzyme assay.** Clone and overexpress PP_2375, purify the protein, and measure methionine synthase activity (CH3-THF + homocysteine → methionine + THF) with and without added cobalamin to directly confirm B12 dependence and kinetic parameters (Km for CH3-THF and homocysteine, kcat).

2. **Genetic essentiality test.** Construct a clean *metH* deletion in KT2440 and assay growth on minimal medium ± methionine, ± cobalamin, and in a *metH metE* double mutant, to experimentally define conditional essentiality and MetH/MetE redundancy.

3. **Regulatory analysis.** Use RT-qPCR/RNA-seq to test whether *metH* and *metE* expression respond reciprocally to cobalamin and methionine availability, and search the upstream regions for B12-riboswitch elements.

4. **Reactivation partner identification.** Identify and test candidate flavodoxin/ferredoxin-reductase partners from the KT2440 genome for their ability to reductively reactivate purified MetH in the presence of AdoMet.

5. **Structural confirmation.** Determine an experimental or high-confidence predicted (AlphaFold) structure of Q88KB5 and verify the geometry of the Zn-thiolate site (Cys250/Cys313/Cys314), the cobalamin His-Asp-Ser triad (His761/Asp759/Ser812), and the reactivation Tyr1143 relative to the *E. coli* template.

---

*Report generated from a 3-iteration autonomous investigation: 7 confirmed findings, 24 papers reviewed. Functional assignment: cobalamin-dependent methionine synthase (EC 2.1.1.13), high confidence.*


## Artifacts

- [OpenScientist final report](metH-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](metH-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:21837727
2. PMID:12832615
3. PMID:17924667
4. PMID:11076529
5. PMID:19846791
6. PMID:17656578
7. PMID:23486253