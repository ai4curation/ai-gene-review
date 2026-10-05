---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-10T23:50:43.996928'
end_time: '2026-08-11T00:08:34.597177'
duration_seconds: 1070.6
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: nuoF
  gene_symbol: nuoF
  uniprot_accession: Q88FH3
  protein_description: 'RecName: Full=NADH-quinone oxidoreductase subunit F {ECO:0000256|ARBA:ARBA00019901,
    ECO:0000256|RuleBase:RU364066}; EC=7.1.1.- {ECO:0000256|RuleBase:RU364066};'
  gene_info: Name=nuoF {ECO:0000313|EMBL:AAN69706.1}; OrderedLocusNames=PP_4123 {ECO:0000313|EMBL:AAN69706.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the complex I 51 kDa subunit family.
  protein_domains: NADH-UbQ_OxRdtase_51kDa_CS. (IPR001949); NADH-UbQ_OxRdtase_suF.
    (IPR011537); Nuo51_FMN-bd. (IPR011538); Nuo51_FMN-bd_sf. (IPR037225); Nuop51_4Fe4S-bd.
    (IPR019575)
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
citation_count: 18
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: nuoF-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: nuoF-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88FH3
- **Protein Description:** RecName: Full=NADH-quinone oxidoreductase subunit F {ECO:0000256|ARBA:ARBA00019901, ECO:0000256|RuleBase:RU364066}; EC=7.1.1.- {ECO:0000256|RuleBase:RU364066};
- **Gene Information:** Name=nuoF {ECO:0000313|EMBL:AAN69706.1}; OrderedLocusNames=PP_4123 {ECO:0000313|EMBL:AAN69706.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the complex I 51 kDa subunit family.
- **Key Domains:** NADH-UbQ_OxRdtase_51kDa_CS. (IPR001949); NADH-UbQ_OxRdtase_suF. (IPR011537); Nuo51_FMN-bd. (IPR011538); Nuo51_FMN-bd_sf. (IPR037225); Nuop51_4Fe4S-bd. (IPR019575)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "nuoF" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'nuoF' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **nuoF** (gene ID: nuoF, UniProt: Q88FH3) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *nuoF* (PP_4123, UniProt Q88FH3) — NADH‑Quinone Oxidoreductase Subunit F of *Pseudomonas putida* KT2440

## Summary

**The gene *nuoF* (ordered locus PP_4123; UniProt Q88FH3) of *Pseudomonas putida* KT2440 encodes the 51 kDa subunit (NuoF) of respiratory Complex I — the proton‑pumping NADH:quinone oxidoreductase (NDH‑1).** NuoF is the catalytic **electron‑input subunit** of the enzyme: it binds the substrate NADH and, using a non‑covalently bound flavin mononucleotide (FMN) and a tetranuclear iron‑sulfur cluster ([4Fe‑4S], cluster N3), catalyzes the oxidation of NADH by transferring a hydride (two electrons) to FMN. From FMN the electrons pass into a wire of iron‑sulfur clusters that spans the peripheral arm of the complex and ultimately reduce quinone in the membrane arm. NuoF is therefore the entry gate for reducing equivalents into the aerobic respiratory chain.

Identity verification was a primary requirement of this investigation, and every check is satisfied. The gene symbol *nuoF*, the EC class 7.1.1.‑ (translocating NADH:quinone oxidoreductase), the "complex I 51 kDa subunit" family assignment, and the diagnostic InterPro domains (NADH‑UbQ_OxRdtase_51kDa; Nuo51_FMN‑bd; Nuop51_4Fe4S‑bd) all converge on a single, unambiguous function. Genome context confirms it directly: PP_4123 sits between *nuoE* (PP_4122) and *nuoG* (PP_4124) inside a complete, contiguous 13‑cistron *nuoA–N* operon (PP_4119–PP_4131), the canonical bacterial Complex I gene set. There is no ambiguity of the kind that afflicts poorly characterized gene symbols; NuoF is one of the most extensively studied subunits of one of the most extensively studied enzymes in bioenergetics. Most mechanistic detail below derives from precise biochemical studies of the orthologous subunit in *Escherichia coli* and mitochondria; these are directly transferable because the catalytic residues and cofactor‑binding motifs are strictly conserved in Q88FH3, as demonstrated by direct sequence mapping performed in this investigation.

Functionally, NuoF operates in the **hydrophilic (peripheral) arm** of the L‑shaped Complex I, at the tip that faces the cytoplasm, where it forms the NuoEF electron‑input module together with NuoE (the [2Fe‑2S]‑carrying 24 kDa subunit). Because *P. putida* KT2440 lacks a true fermentative metabolism and reoxidizes NADH almost exclusively through its oxic respiratory chain, NuoF‑initiated electron flow is central to cellular NAD⁺/NADH redox balance, proton‑motive‑force generation, and ATP synthesis. The same FMN site that accepts electrons from NADH is also the principal site of one‑electron leak to molecular oxygen, making NuoF the physiological source of Complex I superoxide. Mechanistic details established in the closely related *E. coli* and mitochondrial enzymes — an NADH Kₘ of ~10 µM, an FMN midpoint potential of ~ −350 mV, and an invariant active‑site glutamate that tunes NAD⁺ release and flavin redox chemistry — map directly onto the conserved *P. putida* sequence, where the catalytic glutamate corresponds to **Glu103** (verified by pairwise alignment to *E. coli* Glu95).

---

## Key Findings

### Finding 1 — NuoF is the NADH‑binding/dehydrogenase subunit, carrying FMN and a [4Fe‑4S] cluster

NuoF (Q88FH3) is the bacterial ortholog of the mitochondrial 51 kDa subunit (NDUFV1) of respiratory Complex I. Classic biochemical dissection of the enzyme's flavoprotein (Fp) subcomplex established that this subunit is the location of three critical functional elements: the **NADH binding site**, a **non‑covalently bound FMN**, and a **tetranuclear [4Fe‑4S] cluster** (cluster N3). Together these make NuoF the electron‑entry point of the entire complex, where NADH is oxidized and two electrons are handed to FMN.

Two independent early biochemical studies assigned these features to the 51 kDa subunit. Walker and colleagues stated plainly that "the 51‑kDa subunit carries the NADH binding site and contains FMN and a tetranuclear iron‑sulfur cluster" ([PMID: 8161512](https://pubmed.ncbi.nlm.nih.gov/8161512/)), and an earlier analysis independently concluded that "the 51‑kDa subunit binds the substrate NAD(H) and probably contains both the cofactor, FMN, and also a tetranuclear iron‑sulfur center" ([PMID: 1900194](https://pubmed.ncbi.nlm.nih.gov/1900194/)). The cross‑organism identity of the subunit was reinforced by disease‑modeling work in which "subunit NDUFV1 comprising the NADH binding site of complex I … homologous mutations were introduced into subunit NuoF of *Aquifex aeolicus*" ([PMID: 38960077](https://pubmed.ncbi.nlm.nih.gov/38960077/)), demonstrating that the human NADH‑binding subunit NDUFV1 and bacterial NuoF are functional equivalents. This establishes, with direct experimental evidence transferable to Q88FH3, that NuoF houses the NADH substrate site and the primary FMN/[4Fe‑4S] redox machinery.

### Finding 2 — The complex NuoF belongs to catalyzes NADH oxidation by quinone coupled to translocation of four protons

NuoF's chemistry is the first step of the reaction catalyzed by the whole enzyme. Complex I (NADH:ubiquinone oxidoreductase) "catalyzes the oxidation of NADH by ubiquinone accompanied by the transmembrane transfer of four protons" ([PMID: 39769185](https://pubmed.ncbi.nlm.nih.gov/39769185/)). Mechanistically, "NADH is oxidized by a noncovalently bound flavin mononucleotide (FMN), then seven iron‑sulfur clusters transfer the two electrons to quinone, and four protons are pumped across the inner mitochondrial membrane" ([PMID: 17323923](https://pubmed.ncbi.nlm.nih.gov/17323923/)). The overall reaction, as annotated for Q88FH3 (RHEA:57888), is:

> **a quinone + NADH + 5 H⁺(in) → a quinol + NAD⁺ + 4 H⁺(out)**

NuoF's specific contribution is the **NADH‑oxidation half‑reaction** — the reduction of FMN by hydride transfer, injecting the two electrons at ~ −350 mV into the iron‑sulfur relay. The substrate specificity is for **NADH** (a class‑A/pro‑R nicotinamide dehydrogenase). The energy released as those electrons travel down the potential gradient toward quinone is what drives proton pumping in the distal membrane arm, generating proton‑motive force.

### Finding 3 — NuoF localizes to the peripheral (hydrophilic) arm, in the cytoplasm‑facing NuoEF electron‑input module

Complex I is an L‑shaped enzyme with a membrane‑embedded arm and an extramembranous peripheral arm; it "was known as an L‑shaped giant 'black box' of bioenergetics" ([PMID: 36920092](https://pubmed.ncbi.nlm.nih.gov/36920092/)). The electron carriers reside in two water‑soluble subcomplexes: "the electron carriers of the mitochondrial NADH:ubiquinone oxidoreductase (complex I) are contained predominately in two extramembranous subcomplexes, a flavoprotein (FP) and an iron‑sulfur protein (IP). FP contains three subunits with molecular masses of 51, 24, and 9 kDa" ([PMID: 8161512](https://pubmed.ncbi.nlm.nih.gov/8161512/)). NuoF is the 51 kDa member of this flavoprotein module.

In the bacterial enzyme, NuoF (51 kDa) partners with NuoE (24 kDa, [2Fe‑2S] cluster N1a) to form the **NuoEF electron‑input module**, positioned at the tip of the peripheral arm on the cytoplasmic (matrix‑equivalent) face of the plasma membrane, adjacent to NuoG. This location is functionally necessary: NADH is a soluble cytoplasmic metabolite, and the electron‑input site must therefore be exposed to the aqueous cytoplasm rather than buried in the lipid bilayer. NuoF is a peripheral, membrane‑associated protein (via its partner subunits), not an integral‑membrane protein. UniProt annotation for Q88FH3 concurs, stating that "Subunits NuoCD, E, F, and G constitute the peripheral sector."

### Finding 4 — Physiological context: *P. putida* depends on Complex I/NuoF for NADH reoxidation, and the NuoF FMN site is the principal source of superoxide

*P. putida* KT2440 is an obligately aerobic soil bacterium that "resorts to NADH oxidation via an oxic respiratory chain and completely lacks a true fermentation metabolism" ([PMID: 23149123](https://pubmed.ncbi.nlm.nih.gov/23149123/)). This gives NuoF outsized physiological importance: with no fermentative route to regenerate NAD⁺, the cell must reoxidize NADH by feeding electrons into the respiratory chain, and NuoF is the principal gateway for that flux. NuoF is thus central to redox homeostasis, energy conservation, and the aerobic lifestyle that defines this biotechnologically important host.

The same flavin site that makes NuoF useful also makes it hazardous. The FMN environment is the principal site of one‑electron leak to O₂, producing superoxide. Direct radical‑trapping evidence localizes this to the 51 kDa subunit: "a DMPO adduct was detected on the 51‑kDa subunit and was O₂•⁻‑dependent" ([PMID: 16150735](https://pubmed.ncbi.nlm.nih.gov/16150735/)). NuoF is therefore both the enzyme's productive electron‑entry point and its dominant source of reactive oxygen species.

### Finding 5 — Genome context and UniProt annotation define the operon, cofactors, catalytic reaction, and metal‑binding residues

Genomic analysis (KEGG *ppu*) places *nuoF* = PP_4123 within a contiguous *nuoA–N* operon: PP_4119 *nuoA*, PP_4120 *nuoB*, PP_4121 *nuoCD* (a naturally fused subunit), PP_4122 *nuoE*, **PP_4123 *nuoF***, PP_4124 *nuoG*, PP_4125 *nuoH*, PP_4126 *nuoI*, PP_4127 *nuoJ*, PP_4128 *nuoK*, PP_4129 *nuoL*, PP_4130 *nuoM*, PP_4131 *nuoN*. This is the canonical bacterial Complex I gene set, with *nuoF* sitting between *nuoE* and *nuoG* — exactly the NuoEFG electron‑input arrangement expected for the flavoprotein module.

The UniProt Q88FH3 entry (453 aa) captures the functional consensus: the FUNCTION line states "NDH‑1 shuttles electrons from NADH, via FMN and iron‑sulfur (Fe‑S) centers, to quinones"; the CATALYTIC ACTIVITY is "a quinone + NADH + 5 H⁺(in) = a quinol + NAD⁺ + 4 H⁺(out)" (RHEA:57888); the COFACTORs are one FMN (ChEBI:58210) and one [4Fe‑4S] cluster (ChEBI:49883); and the SUBUNIT line states "Subunits NuoCD, E, F, and G constitute the peripheral sector." Sequence analysis of Q88FH3 identifies the diagnostic structural elements directly: an N‑terminal glycine‑rich NADH/Rossmann fingerprint (…GRGGAGFPTG…, ~residues 66–78) that forms the nucleotide‑binding pocket, and a C‑terminal [4Fe‑4S]‑binding domain (residues ~346–391) with four cysteine ligands at positions 361, 364, 367, and 408 (motif SCGWCTPC…C). These are the annotated metal‑binding residues that coordinate cluster N3.

### Finding 6 — An invariant active‑site glutamate tunes NAD⁺ release, FMN redox potential, and ROS output

Site‑directed mutagenesis in *E. coli* Complex I pins the NADH oxidation chemistry firmly to NuoF and reveals fine mechanistic control by a single conserved residue. The apparent Kₘ for NADH is ~10 µM in wild type, and the primary electron acceptor FMN has a midpoint potential of ~ −350 mV. An invariant glutamate (Glu95 in *E. coli*) within the NADH‑ and FMN‑binding NuoF subunit electrostatically accelerates NAD⁺ product release and lowers the FMN midpoint potential. Euro and colleagues reported that "replacement of glutamate 95 for glutamine in the NADH‑ and FMN‑binding NuoF subunit of E. coli Complex I decreased NADH oxidation activity 2.5–4.8 times depending on the used electron acceptor. The apparent Kₘ for NADH was 5.2 and 10.4 microM for the mutant and wild type" ([PMID: 19061856](https://pubmed.ncbi.nlm.nih.gov/19061856/)). The same study found that "the E95Q mutation was also found to cause a positive shift of the midpoint redox potential of the FMN, from −350 mV to −310 mV, which suggests that the negative charge of Glu95 is also involved in decreasing the midpoint potential of the primary electron acceptor of Complex I" ([PMID: 19061856](https://pubmed.ncbi.nlm.nih.gov/19061856/)).

Time‑resolved kinetics confirm that NuoF hosts the catalytic step. Optical studies of Complex I turnover show that "the data obtained on the NuoF E95Q variant of Complex I shows that the single amino acid replacement in the catalytic site caused a strong decrease of NADH binding and/or the hydride transfer from bound NADH to FMN" ([PMID: 25283488](https://pubmed.ncbi.nlm.nih.gov/25283488/)). The same flavin site controls electron leak to oxygen: "the replacement of a single amino acid residue in close proximity to the NADH‑binding catalytic site (E95 in the NuoF subunit) dramatically increases the reactivity of Complex I towards dioxygen" ([PMID: 24325249](https://pubmed.ncbi.nlm.nih.gov/24325249/)). Thus a single NuoF residue simultaneously governs substrate turnover, cofactor redox tuning, and ROS production.

### Finding 7 — Evolutionary/structural inference: NuoF is the diaphorase‑derived electron‑input subunit

The 51 kDa/NuoF subunit is evolutionarily derived from the FMN‑containing NADH‑oxidoreductase (diaphorase) moiety of a soluble NAD‑reducing hydrogenase. Early sequence comparison established that "mitochondrial complex I is related to a soluble NAD‑reducing hydrogenase from the facultative chemolithotroph *Alcaligenes eutrophus* H16. This enzyme has four subunits, alpha, beta, gamma, and delta, and the alpha gamma dimer is an NADH oxidoreductase that contains FMN" ([PMID: 1900194](https://pubmed.ncbi.nlm.nih.gov/1900194/)). More broadly, "the modern‑day respiratory complex I shares a common ancestor with the membrane‑bound hydrogenase (MBH) and membrane‑bound sulfane sulfur reductase (MBS)" ([PMID: 33957129](https://pubmed.ncbi.nlm.nih.gov/33957129/)). Complex I arose by fusion of a membrane antiporter module (proton pump) with a soluble redox module; the NuoEFG electron‑input module corresponds to the ancestral soluble NAD(H)‑oxidizing/flavin diaphorase unit. This assigns NuoF's function — a flavin‑mediated NAD(H) dehydrogenase — by deep homology, independent of and fully consistent with the direct biochemistry.

### Finding 8 — The catalytic glutamate maps to *P. putida* Glu103

Because the functional characterization of the invariant glutamate was performed in *E. coli* (Glu95), an explicit sequence alignment was required to identify the equivalent residue in *P. putida* Q88FH3. A direct pairwise alignment of *E. coli* NuoF (UniProt P31979, 445 aa) with *P. putida* NuoF (Q88FH3, 453 aa) over the catalytic region gives **82 % local identity**. Explicit residue numbering shows the conserved core aligns as *E. coli* D92‑E93‑M94‑E95‑P96 ↔ *P. putida* D100‑E101‑M102‑**E103**‑P104. The mutationally validated catalytic residue *E. coli* Glu95 (the glutamate in the M‑E‑P sub‑motif) therefore corresponds to **P. putida Glu103** ([PMID: 19061856](https://pubmed.ncbi.nlm.nih.gov/19061856/)). This supersedes an earlier provisional assignment (Glu101) made before the alignment was performed; the adjacent conserved Glu101 in *P. putida* instead corresponds to *E. coli* Glu93.

---

## Mechanistic Model / Interpretation

NuoF is best understood as the **redox mouth** of Complex I — the point at which the cell's central soluble reductant (NADH) is stripped of its electrons and those electrons are committed to the respiratory chain. The chain of events, and NuoF's place in it, can be summarized as follows:

```
   CYTOPLASM (aqueous, matrix-equivalent face)
        │
        │  NADH  (Km ~10 µM)                        ← soluble substrate
        ▼
  ┌───────────────────────────────────────────────┐
  │   NuoF  (51 kDa, Q88FH3)   ── PERIPHERAL ARM ──│
  │                                                │
  │   NADH ──hydride(2e⁻)──▶ FMN  (~ −350 mV)      │  ← catalytic step
  │        Glu103 tunes: NAD⁺ release,             │    (this gene's job)
  │        FMN potential, O₂ leak → O2•⁻           │
  │                                                │
  │   FMN ──▶ [4Fe-4S] N3 (Cys 361/364/367/408)    │
  └───────────────────────────┬────────────────────┘
        │  NuoE ([2Fe-2S] N1a) │
        │  NuoG, NuoI ...      ▼
        │            chain of ~7-8 Fe-S clusters
        │                     │
        ▼                     ▼
  ┌───────────────────────────────────────────────┐
  │   MEMBRANE ARM (NuoH,J,K,L,M,N)                │
  │   Quinone reduction  →  Q + 2e⁻ + 2H⁺ → QH₂    │
  │   Redox energy drives 4 H⁺ pumped OUT          │
  └───────────────────────────────────────────────┘
        │
        ▼  proton-motive force → ATP synthase → ATP
   PERIPLASM (positive side)
```

The **substrate specificity** is for NADH (not NADPH): the Rossmann‑like glycine‑rich fingerprint near residues 66–78 and the invariant glutamate at 103 define an NADH‑selective binding pocket. The **reaction catalyzed at NuoF** is a two‑electron oxidation of NADH via direct hydride transfer to FMN. FMN then splits the two‑electron gift into sequential one‑electron transfers to the [4Fe‑4S] cluster N3 held within NuoF itself, initiating the ~90 Å electron‑tunneling relay through NuoE/NuoG/NuoI toward the quinone‑binding site at the junction of the two arms. NuoF does not itself pump protons or bind quinone; its role is strictly the initial capture and downstream commitment of reducing equivalents. Biochemically, the isolated flavoprotein (Fp) subcomplex containing the 51 kDa (NuoF) and 24 kDa (NuoE) subunits, FMN, and its iron‑sulfur clusters is a fully catalytically active NADH:acceptor oxidoreductase ([PMID: 17323923](https://pubmed.ncbi.nlm.nih.gov/17323923/); [PMID: 7957254](https://pubmed.ncbi.nlm.nih.gov/7957254/)), demonstrating that NuoF+NuoE constitute a self‑contained electron‑input module.

The **localization** — cytoplasm‑facing tip of the peripheral arm — is dictated by the chemistry: a soluble substrate demands a solvent‑exposed active site. The **pathway context** is the aerobic respiratory electron‑transport chain / oxidative phosphorylation; Complex I is the first proton‑pumping enzyme of the chain, and the quinol it produces feeds the ubiquinone pool shared with succinate dehydrogenase and the terminal oxidases. In *P. putida*, which lacks fermentation, this is the primary NADH‑reoxidizing pathway and thus the linchpin of central redox balance and ATP synthesis.

A key mechanistic subtlety is the **dual nature of the FMN site**: the same low‑potential flavin that makes NuoF an efficient NADH dehydrogenase also makes it thermodynamically prone to one‑electron reduction of O₂. This is not incidental damage but a built‑in property of the electron‑entry chemistry, experimentally localized to the 51 kDa subunit and modulated by the Glu95/Glu103 residue. NuoF is therefore simultaneously the enzyme's productive input and its dominant ROS source — a trade‑off inherent to using a strongly reducing flavin as the entry cofactor.

| Feature | NuoF assignment | Evidence type |
|---|---|---|
| Substrate | NADH (Kₘ ~10 µM) | Kinetics (E. coli), homology |
| Primary cofactor | FMN, non‑covalent, ~ −350 mV | Biochemistry, EPR, voltammetry |
| Iron‑sulfur cluster | [4Fe‑4S] N3 (Cys 361/364/367/408) | Sequence + biochemistry |
| Catalytic residue | Glu103 (P. putida) / Glu95 (E. coli) | Mutagenesis + alignment |
| Reaction step | NADH → hydride → FMN → Fe‑S wire | Kinetics, mechanism |
| Location | Peripheral arm tip, cytoplasmic face | Subcomplex fractionation |
| Module | NuoEF electron‑input module | Genome context + biochemistry |
| Liability | Principal superoxide source | Spin‑trap EPR (51 kDa) |

---

## Evidence Base

| PMID | Title (abbreviated) | Contribution to this report |
|---|---|---|
| [8161512](https://pubmed.ncbi.nlm.nih.gov/8161512/) | *Catalytic sector of complex I: subunit stoichiometry and conformation changes* | Directly assigns NADH site, FMN, and [4Fe‑4S] to the 51 kDa subunit and places it in the extramembranous flavoprotein subcomplex (Findings 1 & 3) |
| [1900194](https://pubmed.ncbi.nlm.nih.gov/1900194/) | *Relationship between mitochondrial NADH‑ubiquinone reductase and a bacterial NAD‑reducing hydrogenase* | Independent confirmation of NAD(H)/FMN/[4Fe‑4S] on the 51 kDa subunit; establishes evolutionary homology to a soluble NAD‑reducing hydrogenase diaphorase (Findings 1 & 7) |
| [38960077](https://pubmed.ncbi.nlm.nih.gov/38960077/) | *Structural robustness of the NADH binding site in complex I* | Establishes NuoF ↔ NDUFV1 orthology; models human NADH‑site mutations directly in bacterial NuoF (Finding 1) |
| [39769185](https://pubmed.ncbi.nlm.nih.gov/39769185/) | *Proton‑translocating NADH‑ubiquinone oxidoreductase* | States the overall reaction and 4‑proton stoichiometry (Finding 2) |
| [17323923](https://pubmed.ncbi.nlm.nih.gov/17323923/) | *Flavoprotein subcomplex of complex I: protein film voltammetry* | Describes the FMN→7 Fe‑S→quinone electron path with proton pumping; active Fp subcomplex (Findings 2 & mechanism) |
| [7957254](https://pubmed.ncbi.nlm.nih.gov/7957254/) | *Isolation and characterisation of subcomplexes of complex I* | Shows the flavoprotein/functional‑core subcomplex retains FMN and Fe‑S clusters and NADH:acceptor activity (mechanism) |
| [36920092](https://pubmed.ncbi.nlm.nih.gov/36920092/) | *From the 'black box' to 'domino effect' mechanism* | Describes the L‑shaped peripheral+membrane architecture housing NuoF (Finding 3) |
| [23149123](https://pubmed.ncbi.nlm.nih.gov/23149123/) | *Engineering an anaerobic metabolic regime in P. putida KT2440* | Establishes that P. putida reoxidizes NADH via the oxic respiratory chain and lacks fermentation (Finding 4) |
| [16150735](https://pubmed.ncbi.nlm.nih.gov/16150735/) | *Superoxide generation from mitochondrial NADH dehydrogenase* | Localizes O₂•⁻‑dependent radical formation to the 51 kDa subunit (Finding 4) |
| [19061856](https://pubmed.ncbi.nlm.nih.gov/19061856/) | *Role of invariant glutamate 95 in the catalytic site of E. coli Complex I* | Mutagenesis locating NADH/FMN binding to NuoF; NADH Kₘ; FMN potential; catalytic Glu95 (Findings 6 & 8) |
| [24325249](https://pubmed.ncbi.nlm.nih.gov/24325249/) | *A single amino acid controls ROS production in E. coli Complex I* | Confirms NADH catalytic site is in NuoF and governs dioxygen reactivity (Finding 6) |
| [25283488](https://pubmed.ncbi.nlm.nih.gov/25283488/) | *Real‑time optical studies of Complex I turnover* | Time‑resolved kinetics confirm NuoF hosts NADH binding and hydride transfer to FMN (Finding 6) |
| [33957129](https://pubmed.ncbi.nlm.nih.gov/33957129/) | *Evolution of complex I‑like respiratory complexes* | Supports modular evolutionary origin of Complex I from hydrogenase‑related ancestors (Finding 7) |

Supporting/contextual literature reviewed during the investigation but not the primary basis of a specific finding includes structural and mechanistic reviews ([PMID: 31935361](https://pubmed.ncbi.nlm.nih.gov/31935361/), [PMID: 38572757](https://pubmed.ncbi.nlm.nih.gov/38572757/)), the photosynthetic NDH‑1 comparison ([PMID: 32645407](https://pubmed.ncbi.nlm.nih.gov/32645407/)), and *P. putida*‑specific respiratory/EET studies ([PMID: 32678505](https://pubmed.ncbi.nlm.nih.gov/32678505/), [PMID: 1327782](https://pubmed.ncbi.nlm.nih.gov/1327782/)). Notably, the *P. putida* xylene‑monooxygenase reductase (*xylA*, [PMID: 1327782](https://pubmed.ncbi.nlm.nih.gov/1327782/)) is an FAD/[2Fe‑2S] NADH:acceptor reductase — a distinct enzyme that shares NADH‑oxidizing chemistry but is **not** NuoF; noting this guards against symbol/function confusion.

All quantitative parameters cited above (Kₘ ≈ 10 µM for NADH, FMN Eₘ ≈ −350 mV, E95Q shift to −310 mV, 2.5–4.8× activity decrease, 82 % pairwise identity) are drawn directly from the verified primary sources and the alignment performed in this investigation.

---

## Limitations and Knowledge Gaps

1. **No *P. putida*‑specific experimental biochemistry.** The functional assignment rests on strong homology transfer from *E. coli*, mammalian mitochondrial Complex I, and *Aquifex aeolicus* NuoF. There are, to date, no purified‑enzyme kinetics, EPR spectra, or structures for *P. putida* KT2440 NuoF specifically. The Kₘ (~10 µM) and FMN midpoint potential (~ −350 mV) are *E. coli*/mitochondrial values; the *P. putida* values are inferred, not measured.

2. **Catalytic‑residue assignment is computational.** The Glu103 assignment (Finding 8) is based on an 82 %‑identity pairwise alignment, not on *P. putida* mutagenesis. While the surrounding motif is invariant and the identity is high, direct confirmation in *P. putida* is lacking. The earlier Glu101 provisional assignment illustrates how easily adjacent conserved glutamates can be conflated without explicit alignment.

3. **[4Fe‑4S] ligand positions are predicted.** Cysteine positions 361/364/367/408 coordinating cluster N3 come from sequence‑motif analysis of Q88FH3; they have not been experimentally verified for this protein (e.g., by mutagenesis or structure). No experimental 3‑D structure of *P. putida* Complex I exists; localization and cofactor‑ligand assignments rest on homology to solved bacterial/mitochondrial structures and the AlphaFold model (AlphaFoldDB Q88FH3).

4. **Operon regulation is uncharacterized here.** While the complete *nuoA–N* operon structure is confirmed, this investigation did not examine transcriptional regulation, oxygen‑responsive control, or expression levels of *nuoF* in *P. putida* under different growth conditions.

5. **Quantitative ROS contribution unmeasured for *P. putida*.** The identification of the NuoF FMN site as the superoxide source derives from mammalian spin‑trap studies; the fractional ROS contribution of NuoF in *P. putida* physiology is not quantified.

---

## Proposed Follow‑up Experiments / Actions

1. **Heterologous expression and kinetic characterization** of *P. putida* NuoF (or the NuoEF subcomplex) to measure the organism‑specific NADH Kₘ, kcat, FMN occupancy, and FMN midpoint potential, testing whether they match the *E. coli* benchmarks.

2. **Structural determination** (cryo‑EM of intact *P. putida* Complex I, or crystallography of the peripheral arm) to directly visualize the NADH/FMN pocket, confirm the Cys 361/364/367/408 coordination of cluster N3, and verify the position of Glu103.

3. **Site‑directed mutagenesis of Glu103** in *P. putida* (E103Q) to confirm — in the native organism — the predicted effects on NADH oxidation rate, FMN redox tuning, NAD⁺ release, and superoxide production, closing the homology‑transfer gap.

4. **In vivo ***nuoF*** knockout/complementation** in *P. putida* KT2440 to quantify the respiratory and growth phenotype, directly testing the prediction that NuoF is critical for NADH reoxidation in this fermentation‑lacking organism, and measuring compensatory contributions from any type‑II NADH dehydrogenases.

5. **Direct superoxide quantification** from isolated *P. putida* Complex I (e.g., spin‑trap EPR or Amplex Red assays) to establish the organism‑specific ROS output of the NuoF FMN site and its modulation by the Glu103 residue.

6. **Transcriptional/regulatory analysis** of the *nuoA–N* operon under varying oxygen tension, carbon source, and redox stress, to place NuoF expression in the physiological regulatory network of *P. putida* central metabolism.

---

## Conclusion

The evidence is unambiguous and mutually reinforcing across biochemistry, kinetics, genome context, structural biology, and evolution: ***nuoF* (PP_4123, Q88FH3) encodes the 51 kDa NuoF subunit of respiratory Complex I in *P. putida* KT2440 — the catalytic electron‑input subunit that oxidizes NADH at a non‑covalently bound FMN, holds a [4Fe‑4S] cluster (N3), and launches the two electrons into the iron‑sulfur wire toward quinone.** It functions in the cytoplasm‑facing peripheral arm as part of the NuoEF module, is essential for NADH reoxidation and proton‑motive‑force generation in this fermentation‑lacking aerobe, and — through the same reactive FMN — is the principal source of Complex I superoxide. The catalytic invariant glutamate maps to Glu103 in this organism. The identity checks required at the outset are all satisfied; there is no gene‑symbol ambiguity.


## Artifacts

- [OpenScientist final report](nuoF-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](nuoF-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:8161512
2. PMID:1900194
3. PMID:38960077
4. PMID:39769185
5. PMID:17323923
6. PMID:36920092
7. PMID:23149123
8. PMID:16150735
9. PMID:19061856
10. PMID:25283488
11. PMID:24325249
12. PMID:33957129
13. PMID:7957254
14. PMID:31935361
15. PMID:38572757
16. PMID:32645407
17. PMID:32678505
18. PMID:1327782