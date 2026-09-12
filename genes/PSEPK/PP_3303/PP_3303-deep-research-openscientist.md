---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T09:10:03.845349'
end_time: '2026-07-23T09:29:45.887853'
duration_seconds: 1182.04
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_3303
  gene_symbol: PP_3303
  uniprot_accession: Q88HQ0
  protein_description: 'RecName: Full=3-oxoacyl-[acyl-carrier-protein] synthase 2
    {ECO:0000256|ARBA:ARBA00014657, ECO:0000256|PIRNR:PIRNR000447}; EC=2.3.1.179 {ECO:0000256|ARBA:ARBA00012356,
    ECO:0000256|PIRNR:PIRNR000447};'
  gene_info: OrderedLocusNames=PP_3303 {ECO:0000313|EMBL:AAN68910.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the thiolase-like superfamily. Beta-ketoacyl-ACP
  protein_domains: 3-oxoacyl-ACP_synth-2. (IPR017568); Beta-ketoacyl_synthase. (IPR000794);
    Ketoacyl_synth_AS. (IPR018201); Ketoacyl_synth_C. (IPR014031); Ketoacyl_synth_N.
    (IPR014030)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_3303-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_3303-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88HQ0
- **Protein Description:** RecName: Full=3-oxoacyl-[acyl-carrier-protein] synthase 2 {ECO:0000256|ARBA:ARBA00014657, ECO:0000256|PIRNR:PIRNR000447}; EC=2.3.1.179 {ECO:0000256|ARBA:ARBA00012356, ECO:0000256|PIRNR:PIRNR000447};
- **Gene Information:** OrderedLocusNames=PP_3303 {ECO:0000313|EMBL:AAN68910.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the thiolase-like superfamily. Beta-ketoacyl-ACP
- **Key Domains:** 3-oxoacyl-ACP_synth-2. (IPR017568); Beta-ketoacyl_synthase. (IPR000794); Ketoacyl_synth_AS. (IPR018201); Ketoacyl_synth_C. (IPR014031); Ketoacyl_synth_N. (IPR014030)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_3303" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_3303' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_3303** (gene ID: PP_3303, UniProt: Q88HQ0) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PP_3303 (Q88HQ0) — β-Ketoacyl-[ACP] Synthase II (KAS II / FabF)

**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440), PSEPK
**Gene / locus:** PP_3303 · **UniProt:** Q88HQ0 · **Length:** 437 aa · **EC:** 2.3.1.179
**Family:** Thiolase-like superfamily; β-ketoacyl-ACP synthase I/II (KAS). Domains: Beta-ketoacyl_synthase (IPR000794), Ketoacyl_synth_N (IPR014030), Ketoacyl_synth_C (IPR014031), 3-oxoacyl-ACP_synth-2 (IPR017568), Ketoacyl_synth_AS (IPR018201).

---

## 1. Summary (Answer to the Research Question)

PP_3303 encodes **β-ketoacyl-[acyl-carrier-protein] synthase II (KAS II, the FabF condensing enzyme; EC 2.3.1.179)**, a soluble **cytoplasmic** enzyme of the dissociated **type II fatty acid synthase (FAS-II)**. Its primary function is to catalyze the **carbon–carbon bond-forming, decarboxylative Claisen condensation** that elongates a growing fatty acyl chain by two carbons in each turn of the FAS-II elongation cycle: it transfers the acyl group from **acyl-ACP** onto an active-site cysteine and condenses it with a **malonyl-ACP** extender unit to yield a **3-oxoacyl-ACP** (β-ketoacyl-ACP), releasing holo-ACP and CO₂. Its diagnostic, curated substrate reaction is the elongation of **palmitoleoyl-ACP (C16:1 cis-9)** to the **β-keto precursor of cis-vaccenoyl-ACP (C18:1 cis-11)**, identifying it as the KAS II isoform responsible for **cis-vaccenic acid** production and hence for the **temperature-dependent tuning of membrane fatty-acid (homeoviscous) composition**.

---

## 2. Verified Identity

The target was cross-checked against the supplied UniProt record and confirmed unambiguous:

| Attribute | Value (confirmed) |
|---|---|
| Protein name | 3-oxoacyl-[ACP] synthase 2 (KAS II / FabF) |
| EC number | 2.3.1.179 (KAS II) — distinct from EC 2.3.1.41 (KAS I/FabB) and EC 2.3.1.180 (KAS III/FabH) |
| Length | 437 residues |
| N-terminal thiolase motif | `...IVVTGTGVVSPLGC...` (conserved KAS Cys-cap region) |
| Curated reaction (specific) | (9Z)-hexadecenoyl-[ACP] + malonyl-[ACP] + H⁺ = 3-oxo-(11Z)-octadecenoyl-[ACP] + holo-[ACP] + CO₂ |
| Curated reaction (general) | acyl-[ACP] + malonyl-[ACP] + H⁺ = 3-oxoacyl-[ACP] + holo-[ACP] + CO₂ |
| Pathway | Lipid metabolism; fatty acid biosynthesis |

Because the annotated reaction and EC number are the **hallmark KAS II activity** (elongation of long, including C16:1, acyl-ACP; production of the cis-vaccenate precursor), there is no gene-symbol ambiguity: this is genuinely a bacterial FabF/KAS II from *P. putida* KT2440.

**Sequence-level confirmation of the catalytic apparatus (this work):** Direct inspection of the 437-aa sequence recovers all diagnostic elongating-KAS motifs — the N-terminal thiolase signature **TGTGVVSPLGC** (res. 20–30), the nucleophilic **Cys184** in the acyl-cysteine motif `APVTAC184AAGV`, the first catalytic histidine **His325** in the `NAH325ATST` motif, and the second catalytic histidine **His361** in the strictly conserved elongation signature `KSATGH361LLGAAG` (KSxxGHxxG). This reconstitutes the canonical **Cys-His-His triad** (cf. *E. coli* FabF Cys163/His303/His340), giving direct sequence evidence — not merely orthology — that PP_3303 is a catalytically competent KAS II.

**Phylogenetic placement (this work):** Global pairwise-identity comparison places PP_3303 firmly in the **FabF/KAS II clade**: it is most similar to *E. coli* FabF/KAS II (48.7%) and to the KT2440 housekeeping fabF PP_1916 (49.8%), clearly less similar to KAS I/FabB (*E. coli* 41.7%; KT2440 PP_4175 39.7%), and least similar to KAS III/FabH (29.1%). This independently corroborates the EC 2.3.1.179 assignment and **excludes** a FabB (KAS I) or FabH (KAS III) identity. The ~50% identity to PP_1916 indicates the two are anciently diverged KAS-II paralogs rather than recent duplicates.

### 2a. Paralog census and genomic context (important caveat)

A UniProt census of *P. putida* KT2440 FAS-II condensing enzymes shows PP_3303 is **one of several KAS-family paralogs**:

| Locus | UniProt | Annotation | Note |
|---|---|---|---|
| PP_4175 | Q88FC3 | FabB / KAS I (EC 2.3.1.41) | unsaturated FA initiation |
| **PP_1916** | Q88LL4 | **FabF / KAS II (EC 2.3.1.179)** | **housekeeping fabF, in fab cluster beside fabG (PP_1914)** |
| **PP_3303** | **Q88HQ0** | **KAS II (EC 2.3.1.179)** | **this study; standalone paralog** |
| PP_2780 | Q88J69 | KAS-II-like | accessory paralog |
| PP_2778 | Q88J71 | KAS-II-like | accessory paralog |

Critically, PP_3303 is **not** located in the core fatty-acid biosynthesis operon. Its genomic neighborhood (PP_3300–PP_3305) is an **efflux/stress-response island**: a TetR-family transcriptional regulator (PP_3300), RND efflux transporter + membrane-fusion components (PP_3301/PP_3302), a Bcr/CflA-family efflux transporter (PP_3304), and a TerC-family membrane protein (PP_3305). The canonical housekeeping elongation synthase is instead **PP_1916 (fabF)**, co-clustered with **fabG (PP_1914)**. This indicates that while PP_3303's **molecular function is unambiguously KAS II condensation**, its **in vivo physiological deployment may be accessory or condition/stress-responsive** rather than the primary housekeeping elongation role — a distinction that should temper direct transfer of *E. coli* fabF phenotypes to PP_3303.

---

## 3. Primary Function — The Reaction Catalyzed

FAS-II synthesizes fatty acids on the small acyl carrier protein (ACP) through iterative two-carbon elongation cycles (condensation → ketoreduction → dehydration → enoyl reduction). PP_3303 performs the **committed condensation (C–C bond-forming) step** of the cycle [PMID 39175097]. KAS enzymes catalyze a **decarboxylative Claisen condensation** by a **two-step ping-pong mechanism**: (1) the acyl donor acylates the active-site cysteine (acyl-enzyme intermediate); (2) malonyl-ACP is decarboxylated to a carbanion/enolate that attacks the acyl-enzyme, forming the new C–C bond and yielding β-ketoacyl-ACP [PMID 22017312]. The **elongating** synthases KAS I (FabB) and KAS II (FabF) use an **acyl-ACP** donor (in contrast to the priming KAS III/FabH, which uses acyl-CoA) [PMID 22017312].

---

## 4. Substrate Specificity

The curated Q88HQ0 reaction — **palmitoleoyl-ACP (C16:1Δ9) + malonyl-ACP → 3-oxo-cis-vaccenoyl-ACP (C18:1Δ11) + CO₂** — is the defining KAS II activity. Biochemically, **FabF/KAS II efficiently elongates saturated C14 and unsaturated C16:1 acyl-ACP substrates**, whereas the paralogous **KAS I (FabB) has reduced activity beyond C12** [PMID 36048156]. This chain-length preference places PP_3303 at the **terminal, long-chain elongation steps** of FAS-II and makes it the enzyme that produces **cis-vaccenic acid (C18:1 cis-11)**, the principal long-chain monounsaturated fatty acid of enterobacterial and pseudomonad membranes. Recent structural work shows FabF achieves substrate selectivity through hydrophobic cavities and "front/middle/back door" gating residues that stabilize specific acyl chain lengths [PMID 39175097], with mobile active-site loops enforcing an ordered "gating" mechanism [PMID 32265440].

---

## 5. Catalytic Mechanism & Active Site

PP_3303 adopts the **thiolase fold** and employs a conserved **Cys-His-His catalytic triad** [PMID 11286890]. Detailed mutagenesis of a KAS II (*S. pneumoniae* FabF) assigns the roles [PMID 16618705]:
- **Nucleophilic active-site cysteine** — required for acyl-enzyme formation and overall condensation (UniProt annotates the KAS active-site residue on Q88HQ0).
- **Two histidines with distinct electronic states** — one (His337 in Sp numbering) stabilizes the malonyl thioester oxyanion in the transition state; the other (His303) deprotonates a structured active-site water to drive decarboxylation and bicarbonate release.
- **A conserved lysine** controls the histidine electronic state; a **gatekeeper phenylalanine (Phe396)** enforces ordered substrate addition.

Quantum-chemical analysis of *E. coli* FabF corroborates that conserved **Lys and His residues facilitate proton transfer during C–C bond formation** [PMID 39175097]. The catalytic cysteine's reactivity is directly demonstrated by the antibiotic **cerulenin**, which is **covalently bonded to the active-site cysteine** [PMID 10037680]; FabF is likewise the target of platensimycin-class antibacterials [PMID 18336284], underscoring both the mechanism and druggability of this enzyme class.

---

## 6. Subcellular Localization

As a component of the **soluble, dissociated FAS-II system**, PP_3303 operates in the **cytoplasm**, acting on substrates tethered to the phosphopantetheine arm of ACP. Its β-ketoacyl-ACP products are processed by the downstream cytosolic tailoring enzymes (FabG, FabA/FabZ, FabI) and ultimately channelled into **membrane phospholipid** biosynthesis at the inner membrane. There is no signal peptide or membrane-spanning domain in the sequence, consistent with a cytoplasmic assignment.

---

## 7. Pathway Context & Physiological Role

**Pathway:** Bacterial type II fatty acid biosynthesis (FAS-II) → membrane phospholipid acyl chains. PP_3303 is the elongation condensing enzyme that governs production of long-chain (C18) unsaturated fatty acids.

**Homeoviscous / thermal regulation:** Classic *E. coli* genetics established that **fabF-null mutants lack both cis-vaccenic acid synthesis and thermal regulation**, and that **synthase II (FabF) is "the sole enzyme regulating the temperature-dependent composition of the membrane phospholipid acyl chains"** [PMID 6337151]. At lower temperatures FabF activity increases the proportion of the longer C18:1 (cis-vaccenate) chain, maintaining membrane fluidity — a role directly attributable to PP_3303's substrate preference.

**Relevance to *P. putida* physiology:** In the solvent-tolerant *P. putida* lineage, the very unsaturated fatty acid produced by FabF (**cis-vaccenate**) is the substrate for the periplasmic **cis/trans isomerase (Cti)**, which converts cis- to trans-unsaturated fatty acids as the principal **short-term adaptation to organic solvents**, complemented by longer-term cardiolipin changes [PMID 17564601]. Adaptive remodeling of membrane fatty-acid and phospholipid composition is a well-documented solvent-tolerance mechanism in *P. putida* and related pseudomonads [PMID 12142492, PMID 11030576]. Thus PP_3303 supplies the biosynthetic precursor pool that underlies both **temperature** and **solvent-stress** membrane adaptation in this biotechnologically important organism.

---

## 8. Supported vs. Refuted Hypotheses

| Hypothesis | Status | Basis |
|---|---|---|
| PP_3303 is a KAS II/FabF condensing enzyme (EC 2.3.1.179) | **Supported** | UniProt curated EC/reaction; domain architecture [PMID 22017312, 39175097] |
| It elongates palmitoleoyl-ACP → cis-vaccenate precursor (long-chain specificity) | **Supported** | Curated reaction; FabF C14/C16:1 preference [PMID 36048156] |
| Uses Cys-His-His triad, ping-pong Claisen condensation | **Supported** | [PMID 16618705, 11286890, 39175097, 10037680] |
| Cytoplasmic FAS-II enzyme | **Supported** | Type II FAS biology; no signal/TM segment |
| Governs temperature-dependent membrane fatty-acid composition | **Supported (by orthology)** | *E. coli* fabF genetics [PMID 6337151] |
| It is KAS I (FabB, EC 2.3.1.41) or KAS III (FabH) | **Refuted** | EC 2.3.1.179 and the C16:1→C18:1 reaction are KAS II-specific |
| Catalytic Cys-His-His triad intact in the actual Q88HQ0 sequence | **Supported** | Cys184/His325/His361 + KSATGH & thiolase motifs (this work) |
| PP_3303 is the sole/housekeeping fabF of KT2440 | **Refuted / qualified** | Housekeeping fabF is PP_1916 (in fabG cluster); PP_3303 is a standalone paralog in an efflux/stress island (this work) |
| PP_3303 belongs to KAS II (FabF) clade, not KAS I/III | **Supported** | Global identity: 48.7% EcFabF, 41.7% EcFabB, 29.1% EcFabH (this work) |

---

## 9. Limitations & Future Directions

- Direct **biochemical or genetic characterization of PP_3303 specifically in *P. putida* KT2440 is not available in the literature**; functional assignment rests on the curated UniProt reaction, direct sequence verification of the catalytic triad, and strong orthology to extensively characterized *E. coli*, *S. pneumoniae*, and *Synechocystis* KAS II enzymes. The catalytic identity is robust; the *in vivo* physiological role is inference-by-homology.
- **PP_3303 is a paralog, not the housekeeping fabF.** KT2440 encodes a dedicated fabF (PP_1916, in the fabG cluster), a FabB/KAS I (PP_4175), and two further KAS-II-like genes (PP_2778/PP_2780). PP_3303 sits in an efflux/stress genomic island. The **division of labor, relative flux, expression conditions, and possible functional redundancy** among these paralogs have not been experimentally dissected, so the cis-vaccenate/thermal-regulation role (established for the single *E. coli* fabF) may in KT2440 be carried primarily by PP_1916, with PP_3303 accessory or condition-specific.
- Future work: paralog-resolved knockouts (ΔPP_3303 vs ΔPP_1916, and double mutants) with temperature/solvent-shift lipidomics; RNA-seq to define the condition-dependence of PP_3303 (given its efflux-island context and adjacent TetR regulator); enzyme kinetics on defined acyl-ACP substrates; structural determination to confirm the gating residues.

---

## References (PMIDs)
- 39175097 — FabF catalyzes C–C bond formation; bimodal specificity; catalytic Lys/His (2024)
- 36048156 — FabB/FabF substrate selectivity; FabF elongates C14/C16:1 (2022)
- 32265440 — Gating mechanism of elongating β-ketoacyl-ACP synthases (2020)
- 22017312 — Substrate recognition by β-ketoacyl-ACP synthases; ping-pong/Claisen (2011)
- 16618705 — Active-site residues (Cys/His/His/Lys/Phe) of KAS II FabF mechanism (2006)
- 11286890 — KAS I structure; Cys-His-His triad shared by KAS II (2001)
- 11152607 — KAS II crystal structure (Synechocystis), condensing-enzyme classification (2001)
- 10037680 — Cerulenin covalently bound to active-site cysteine of KAS (1999)
- 18336284 — Platensimycin targets FabF/FabB (2008)
- 6337151 — FabF/synthase II is the sole thermal regulator of membrane acyl-chain composition (1983)
- 17564601 — cis/trans isomerase and cardiolipin in *P. putida* membrane adaptation (2007)
- 12142492 — Mechanisms of solvent tolerance in Gram-negative bacteria (2002)
- 11030576 — Phospholipid compositional changes in pseudomonads with toluene (2000)


## Artifacts

- [OpenScientist final report](PP_3303-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_3303-deep-research-openscientist_artifacts/final_report.pdf)