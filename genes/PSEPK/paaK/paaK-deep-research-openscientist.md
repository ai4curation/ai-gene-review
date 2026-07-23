---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T11:18:29.981778'
end_time: '2026-07-23T11:38:43.012361'
duration_seconds: 1213.03
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: paaK
  gene_symbol: paaK
  uniprot_accession: Q88HS4
  protein_description: 'RecName: Full=Phenylacetate-coenzyme A ligase {ECO:0000256|ARBA:ARBA00068695,
    ECO:0000256|PIRNR:PIRNR006444}; EC=6.2.1.30 {ECO:0000256|ARBA:ARBA00066629, ECO:0000256|PIRNR:PIRNR006444};
    AltName: Full=Phenylacetyl-CoA ligase {ECO:0000256|ARBA:ARBA00075111, ECO:0000256|PIRNR:PIRNR006444};'
  gene_info: Name=paaK {ECO:0000313|EMBL:AAN68886.1}; OrderedLocusNames=PP_3279 {ECO:0000313|EMBL:AAN68886.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the phenylacetyl-CoA ligase family.
  protein_domains: Adenylate-forming_Reductase. (IPR051414); AMP-bd_C_sf. (IPR045851);
    AMP-dep_Lig_C. (IPR028154); AMP-dep_synth/lig_dom. (IPR000873); ANL_N_sf. (IPR042099)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
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
  path: paaK-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: paaK-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88HS4
- **Protein Description:** RecName: Full=Phenylacetate-coenzyme A ligase {ECO:0000256|ARBA:ARBA00068695, ECO:0000256|PIRNR:PIRNR006444}; EC=6.2.1.30 {ECO:0000256|ARBA:ARBA00066629, ECO:0000256|PIRNR:PIRNR006444}; AltName: Full=Phenylacetyl-CoA ligase {ECO:0000256|ARBA:ARBA00075111, ECO:0000256|PIRNR:PIRNR006444};
- **Gene Information:** Name=paaK {ECO:0000313|EMBL:AAN68886.1}; OrderedLocusNames=PP_3279 {ECO:0000313|EMBL:AAN68886.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the phenylacetyl-CoA ligase family.
- **Key Domains:** Adenylate-forming_Reductase. (IPR051414); AMP-bd_C_sf. (IPR045851); AMP-dep_Lig_C. (IPR028154); AMP-dep_synth/lig_dom. (IPR000873); ANL_N_sf. (IPR042099)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "paaK" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'paaK' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **paaK** (gene ID: paaK, UniProt: Q88HS4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: paaK (PP_3279, UniProt Q88HS4)
## Phenylacetate–Coenzyme A Ligase of *Pseudomonas putida* KT2440

---

## 1. Summary (Answer to the Research Question)

**paaK** (ordered locus **PP_3279**; UniProt **Q88HS4**) of *Pseudomonas putida* KT2440 encodes **phenylacetate–coenzyme A ligase (phenylacetyl-CoA ligase, EC 6.2.1.30)**, an ATP-dependent (AMP-forming) acyl-CoA synthetase of the **ANL/adenylate-forming (AMP-dependent synthetase/ligase) superfamily**. It catalyzes the **first, committed step of the aerobic phenylacetate (PA) catabolic pathway**, activating the chemically inert aromatic carboxylic acid phenylacetate to its coenzyme A thioester:

> **phenylacetate + ATP + CoA → phenylacetyl-CoA (PA-CoA) + AMP + PPi** (Mg²⁺-dependent)

The enzyme is a **cytoplasmic**, soluble ~48-kDa monomer that acts on intracellular phenylacetate. Its product, phenylacetyl-CoA, is the **central convergent intermediate** (the "phenylacetyl-CoA catabolon") into which many peripheral aromatic pathways (phenylalanine, 2-phenylethylamine, styrene, *n*-phenylalkanoic acids, environmental aromatics) funnel; PA-CoA is then processed by a distinct ring-epoxidizing/CoA-dependent route to acetyl-CoA and succinyl-CoA for entry into central metabolism. PA-CoA is also the physiological inducer of the pathway.

The gene identity is **unambiguous and fully consistent with the UniProt annotation**: symbol *paaK*, EC 6.2.1.30, phenylacetyl-CoA ligase family, AMP-dependent synthetase/ligase domains (IPR000873, IPR028154, IPR045851, IPR042099), in *P. putida* KT2440.

---

## 2. Gene/Protein Identity Verification

| Attribute | UniProt Q88HS4 | Literature consistency |
|---|---|---|
| Symbol | *paaK* (also *pha* nomenclature in KT2440; *pcl* in *P. putida* U) | ✔ consistent; *paaK* is the standard PA-CoA ligase symbol (E. coli, Thermus, Burkholderia) |
| EC number | 6.2.1.30 | ✔ matches purified enzyme reaction |
| Family | Phenylacetyl-CoA ligase family / ANL superfamily | ✔ AMP-forming acyl-CoA synthetase fold |
| Organism | *P. putida* KT2440 | ✔ genome study PMID 12534466 maps the *pha* cluster |
| Reaction | PA + ATP + CoA → PA-CoA + AMP + PPi | ✔ PMID 2324116, 18414813 |

**Conclusion:** This is the correct, well-characterized gene. No ambiguity; the symbol, EC number, family, domains, and organism are mutually consistent with an extensive primary literature. (Note: the KT2440 phenylacetate cluster was originally annotated with *pha* gene names by Jiménez et al. 2002 [PMID 12534466]; the community-standard *paa*/*paaK* nomenclature, used by UniProt, is equivalent.)

---

## 3. Primary Molecular Function — The Catalyzed Reaction

### 3.1 Reaction and mechanism
PaaK is an **AMP-forming ligase** of the ANL (Acyl-CoA synthetase / NRPS adenylation / Luciferase) superfamily. Like all members, it works by a **two-step, adenylate-forming mechanism**:
1. **Adenylation:** phenylacetate + ATP → phenylacetyl-adenylate (PA-AMP) + PPi.
2. **Thioesterification:** PA-AMP + CoA → phenylacetyl-CoA + AMP.

The domain architecture reported for Q88HS4 — a large N-terminal adenylation domain (ANL_N; IPR042099) plus a small mobile C-terminal domain (AMP-binding C; IPR045851/IPR028154) — is the structural hallmark of this superfamily, in which the C-terminal domain rotates (~140°) between an "adenylation" and a "thioester-forming" conformation ("domain alternation") to catalyze the two half-reactions.

### 3.2 Direct biochemical evidence (purified enzyme)
The enzyme was first purified to homogeneity (513-fold) from *Pseudomonas putida* and biochemically characterized (Martínez-Blanco et al. 1990, **PMID 2324116**):
- **Reaction requirements:** ATP, CoA, phenylacetate, and Mg²⁺ (as MgCl₂).
- **Size:** single ~**48 ± 1 kDa** polypeptide (monomer) by SDS-PAGE.
- **Optimum:** pH 8.2, 30 °C.
- **Apparent Kₘ:** ATP 9.7 mM, CoA 1.0 mM, phenylacetate 16.5 mM.
- **Inhibition:** by Cu²⁺, Zn²⁺, Hg²⁺ and by thiol-reactive reagents (N-ethylmaleimide, DTNB, p-chloromercuribenzoate) — indicating a functionally important cysteine/thiol.

A sensitive coupled fluorometric assay (adenylate kinase / pyruvate kinase / lactate dehydrogenase, monitoring NADH) confirmed the AMP-forming stoichiometry (Rodríguez-Aparicio et al. 1991, **PMID 2009287**).

The homologous PaaK from *Thermus thermophilus* provided a clean in-vitro demonstration of the exact reaction and higher substrate affinities:
- **PA + CoA + MgATP → PA-CoA + AMP + MgPPi**, Vmax 24 µmol/min/mg, Kₘ ATP 6 µM, CoA 30 µM, PA 50 µM (Erb et al. 2008, **PMID 18414813**).

### 3.3 Gene cloning confirms function
The gene encoding this enzyme (*pcl* in *P. putida* U, ortholog of KT2440 *paaK*) was cloned by Tn5 mutagenesis and shown to encode the 48-kDa PA-CoA ligase; heterologous expression in *E. coli* conferred PA-CoA ligase activity and the ability to grow on phenylacetate as sole carbon source (Miñambres et al. 1996, **PMID 8969218**). In *E. coli* W, *paaK* was identified within the *paaABCDEFGHIJK* catabolic operon as the gene "coding for a phenylacetyl-CoA ligase that catalyzes the activation of PA to phenylacetyl-CoA" (Ferrández et al. 1998, **PMID 9748275**).

---

## 4. Substrate Specificity

PaaK is **highly specific for unsubstituted phenylacetate**:
- The purified *P. putida* enzyme **does not use** 3-hydroxy-, 4-hydroxy-, or 3,4-dihydroxyphenylacetate as substrates, and shows a specificity **distinct from other acyl-CoA-activating enzymes**; hydroxy-/methyl-phenylacetyl derivatives and short/long-chain fatty acids (>C5), acetate, butyrate and succinate neither serve as substrates nor induce the enzyme (Martínez-Blanco et al. 1990, **PMID 2324116**).
- *T. thermophilus* PaaK is **highly specific toward phenylacetate**, with only low activity on 4-hydroxyphenylacetate (Erb et al. 2008, **PMID 18414813**).

Comparative structural/kinetic work in *Burkholderia cenocepacia* (which carries two ligases, PaaK1 and PaaK2) rationalizes this specificity: the specific enzyme has a compact binding pocket, whereas the more promiscuous PaaK1 has a **larger binding pocket** that can accommodate hydroxylated PA derivatives (3-OHPA, 4-OHPA) (Imolorhe & Cardona 2011, **PMID 22919580**). *P. putida* KT2440's PaaK corresponds to the strict phenylacetate-specific type.

**Interpretation:** Narrow specificity ensures PaaK channels only genuine phenylacetate — the hub metabolite of the catabolon — into the CoA-dependent pathway, avoiding wasteful activation of related aromatics that belong to other routes.

---

## 5. Subcellular Localization / Where It Acts

- PaaK is a **soluble, cytoplasmic** enzyme. It is a monomeric globular protein with no signal peptide, membrane-spanning region, or secretion signal; the purified protein behaves as a soluble 48-kDa species (**PMID 2324116**).
- It acts on the **intracellular pool of phenylacetate**. Phenylacetate first enters the cell via a dedicated, energy-dependent **phenylacetic acid transport system (PATS)** (active transport, Kₘ ≈ 13 µM, driven by the membrane energization/electron-transport state), after which cytoplasmic PaaK activates it (Schleissner et al. 1994, **PMID 8002592**).

Thus the enzyme performs its catalytic function **in the cytoplasm**, at the interface between substrate uptake and downstream CoA-dependent ring processing.

---

## 6. Pathway Context and Biological Process

### 6.1 The phenylacetyl-CoA "catabolon"
PaaK is the **committed entry enzyme** of the aerobic phenylacetate degradation pathway — a **CoA-dependent "hybrid" pathway** that is fundamentally different from classical aerobic aromatic catabolism (which uses ring-hydroxylating dioxygenases on free aromatic acids). This pathway operates in ~16% of sequenced bacteria, including *E. coli* and *P. putida* (Teufel et al. 2010, **PMID 20660314**).

In KT2440, genomic analysis identified the **phenylacetate (*pha*/*paa*) pathway** as one of four central aromatic catabolic routes (alongside the protocatechuate and catechol β-ketoadipate branches and the homogentisate pathway) (Jiménez et al. 2002, **PMID 12534466**). Multiple **peripheral (upper) pathways converge on phenylacetyl-CoA**, making PaaK the funnel point for:
- **L-phenylalanine** (via phenylpyruvate/phenylacetaldehyde → phenylacetate),
- **2-phenylethylamine** (via the *mao*/amine oxidase route),
- **styrene** (via the *sty* upper pathway, PMID 11959447),
- **n-phenylalkanoic acids** and other environmental aromatics/pollutants.

### 6.2 Steps downstream of PaaK (fate of the product PA-CoA)
Once PaaK forms phenylacetyl-CoA, the ring is attacked while activated as a thioester (Teufel et al. 2010, **PMID 20660314**; 2011, **PMID 21296885**; 2012, **PMID 22398448**):
1. **PaaABC(E)** — a multicomponent, **di-iron monooxygenase/epoxidase** — converts PA-CoA to **ring-1,2-epoxyphenylacetyl-CoA** (and can deoxygenate it back, an intrinsic detox mechanism).
2. The epoxide isomerizes to a seven-membered O-heterocyclic enol ether, **oxepin-CoA**.
3. **PaaZ** (bifunctional (R)-enoyl-CoA hydratase + NADP⁺ aldehyde dehydrogenase) hydrolytically cleaves the ring to **3-oxo-5,6-dehydrosuberyl-CoA**.
4. **β-oxidation–like steps** (PaaFGHIJ homologs) degrade this to **acetyl-CoA and succinyl-CoA**, which enter the **TCA cycle**.

### 6.3 Regulation
- The product **PA-CoA is the true physiological inducer** of the pathway: it antagonizes the **PaaX** transcriptional repressor, de-repressing the catabolic operon (Ferrández et al. 1998, **PMID 9748275**). This places PaaK's product at the center of pathway induction.
- In KT2440, phenylacetate metabolism is under **carbon catabolite repression (CCR)** by glucose/gluconate, acting at the transcriptional level. The intracellular signal is **2-keto-3-deoxy-6-phosphogluconate (KDPG)**: an *edd* mutant (no KDPG) shows high phenylacetyl-CoA ligase activity even in glucose+PAA (CCR abolished), whereas wild type is repressed (Kim et al. 2009, **PMID 19406896**). PA-CoA ligase activity and *paaK* transcription track pathway induction across conditions (O'Leary et al. 2002, **PMID 11959447**; Kim et al. 2007, **PMID 18156794**).

### 6.4 Biotechnological/physiological relevance
Because PaaK generates phenylacetyl-CoA, expressing the *P. putida* ligase gene in *Penicillium chrysogenum* increased the pool of this direct precursor and **boosted benzylpenicillin (penicillin G) biosynthesis ~1.8–2.2-fold** (Miñambres et al. 1996, **PMID 8969218**) — direct evidence that the enzyme's product is phenylacetyl-CoA and that PaaK is the rate-relevant activating step.

---

## 7. Supported and Refuted Hypotheses

**Supported:**
- H1: PP_3279/paaK encodes phenylacetate-CoA ligase (EC 6.2.1.30). ✔ (multiple biochemical + genetic lines).
- H2: The enzyme catalyzes PA + ATP + CoA → PA-CoA + AMP + PPi, Mg²⁺-dependent, AMP-forming. ✔
- H3: It is strictly specific for unsubstituted phenylacetate. ✔
- H4: It is cytoplasmic and acts on imported phenylacetate. ✔
- H5: It is the committed first step of the CoA-dependent catabolon converging on PA-CoA → acetyl-CoA + succinyl-CoA. ✔
- H6: It is induced by phenylacetate and subject to KDPG-mediated CCR. ✔

**Refuted / Not supported:**
- That PaaK acts on hydroxylated phenylacetates (3-/4-OH-PA) in *P. putida* — **refuted** for the specific enzyme (no activity; PMID 2324116).
- That the aromatic ring is opened on the free acid by a dioxygenase (classical model) — **refuted**; ring processing occurs on the CoA thioester via epoxidation (PMID 20660314).

---

## 8. Limitations and Future Directions

1. **Direct structural data** for the *P. putida* KT2440 PaaK (Q88HS4) itself have not been reported; mechanistic/structural inferences draw on homologs (*Thermus*, *Burkholderia*, *E. coli*) and the ANL superfamily. An experimental crystal/cryo-EM structure of the KT2440 enzyme with PA-AMP/CoA would confirm active-site residues and the domain-alternation mechanism.
2. Most **quantitative kinetics** derive from *P. putida* U and thermophilic/other homologs; strain-KT2440-specific kinetic constants and any second paralog should be verified from the KT2440 genome.
3. In-vivo flux control by PaaK versus the transporter (PATS) and the downstream oxygenase under different carbon regimes merits systems-level study.

---

## 9. Key References
- Martínez-Blanco et al. 1990, *J. Biol. Chem.* — purification/characterization of PA-CoA ligase (PMID **2324116**).
- Rodríguez-Aparicio et al. 1991 — sensitive assay confirming AMP-forming reaction (PMID **2009287**).
- Schleissner et al. 1994 — phenylacetate active transport system (PMID **8002592**).
- Miñambres et al. 1996 — cloning of *pcl*/paaK; penicillin precursor boost (PMID **8969218**).
- Ferrández et al. 1998 — *paa* cluster, paaK function, PA-CoA as inducer (PMID **9748275**).
- Jiménez et al. 2002 — KT2440 aromatic catabolism genomics; *pha* pathway (PMID **12534466**).
- O'Leary et al. 2002 — *paaK* transcription linked to styrene/PA growth (PMID **11959447**).
- Erb et al. 2008 — recombinant PaaK reaction and kinetics (PMID **18414813**).
- Kim et al. 2009 — KDPG-mediated CCR of PA metabolism/ligase (PMID **19406896**).
- Teufel et al. 2010 — elucidation of the CoA-dependent phenylalanine/phenylacetate pathway (PMID **20660314**); 2011 (PMID **21296885**); 2012 (PMID **22398448**).
- Imolorhe & Cardona 2011 — two PaaK ligases, binding-pocket/specificity (PMID **22919580**).


## Artifacts

- [OpenScientist final report](paaK-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](paaK-deep-research-openscientist_artifacts/final_report.pdf)