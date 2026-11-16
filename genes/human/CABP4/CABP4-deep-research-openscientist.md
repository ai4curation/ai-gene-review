---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-14T05:33:50.920622'
end_time: '2026-11-14T05:48:04.185126'
duration_seconds: 853.26
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: CABP4
  gene_symbol: CABP4
  uniprot_accession: P57796
  protein_description: 'RecName: Full=Calcium-binding protein 4; Short=CaBP4;'
  gene_info: Name=CABP4;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: CaBP1/2/4/5. (IPR043582); EF-hand-dom_pair. (IPR011992); EF_Hand_1_Ca_BS.
    (IPR018247); EF_hand_dom. (IPR002048); EF-hand_1 (PF00036)
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
citation_count: 12
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: CABP4-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: CABP4-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P57796
- **Protein Description:** RecName: Full=Calcium-binding protein 4; Short=CaBP4;
- **Gene Information:** Name=CABP4;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** CaBP1/2/4/5. (IPR043582); EF-hand-dom_pair. (IPR011992); EF_Hand_1_Ca_BS. (IPR018247); EF_hand_dom. (IPR002048); EF-hand_1 (PF00036)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CABP4" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CABP4' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CABP4** (gene ID: CABP4, UniProt: P57796) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# CABP4 (Calcium-Binding Protein 4, UniProt P57796): Functional Annotation Report

## Gene/Protein Identity Verification

Before presenting findings, the target identity was confirmed against the provided UniProt record:

| Attribute | Target (UniProt P57796) | Literature match |
|-----------|-------------------------|------------------|
| Protein | Calcium-binding protein 4 (CaBP4) | ✔ Consistent across all primary sources |
| Gene symbol | CABP4 | ✔ |
| Organism | *Homo sapiens* (human); mouse ortholog used for mechanistic/genetic studies | ✔ |
| Domains | EF-hand pair, EF-hand Ca²⁺-binding (IPR002048, IPR011992, IPR018247, PF00036); CaBP1/2/4/5 subfamily (IPR043582) | ✔ Four EF-hands, calmodulin-like CaBP family |

**Verification outcome:** The gene symbol "CABP4" unambiguously matches the human photoreceptor calcium-binding protein 4. The literature is specific and consistent. One potential source of confusion was noted and excluded: *Fasciola gigantica* "tegumental calcium-binding EF-hand protein 4" (rFg-CaBP4; [PMID: 34022913](https://pubmed.ncbi.nlm.nih.gov/34022913/)) is an unrelated parasite protein sharing only a generic "CaBP4" label and the EF-hand fold — it is **not** the human CABP4 and was not used for any functional claim. All functional conclusions below derive from the correct human gene and its mouse ortholog.

---

## Summary

**CABP4 encodes CaBP4, a ~30 kDa calmodulin-like neuronal calcium-binding protein of the CaBP/caldendrin (CABP1–5) family. Its primary, well-established function is to act as a presynaptic calcium sensor and positive regulator of L-type voltage-gated calcium channels — chiefly Cav1.4 (CACNA1F) and, secondarily, Cav1.3 (CACNA1D) — at the ribbon synapse of retinal photoreceptors.** CaBP4 is not an enzyme, transporter, or structural scaffold; it is a signaling/regulatory EF-hand protein that binds its target channel and tunes its gating.

Mechanistically, CaBP4 binds the C-terminal region of the Cav1.4 α1-subunit at the IQ motif and displaces the channel's autoinhibitory "ICDI" (inhibitor of Ca²⁺-dependent inactivation) domain. This shifts voltage-dependent activation of Cav1.4 to more hyperpolarized potentials and dramatically increases channel availability while suppressing calcium-dependent inactivation. The net effect is to keep the channel open under the sustained, graded depolarization that photoreceptors experience in darkness, maintaining the tonic Ca²⁺ influx that drives continuous glutamate release from the photoreceptor synaptic terminal onto second-order ON-bipolar and horizontal cells. CaBP4 therefore governs the very first synapse of the visual pathway.

CaBP4 performs this role intracellularly, on the cytoplasmic face of photoreceptor synaptic terminals in the outer plexiform layer, within a presynaptic protein network that includes the synaptic ribbon protein RIBEYE and the ciliary trafficking chaperone UNC119. Loss of CaBP4 function in humans (recessive loss-of-function mutations) and in knockout mice causes a congenital, non-progressive, cone-dominated synaptic retinal disorder overlapping the incomplete form of congenital stationary night blindness (CSNB2) and Åland eye disease — clinically marked by reduced acuity, nystagmus, photophobia, hyperopia, and a characteristic electronegative electroretinogram. A parallel but functionally minor/redundant role exists in cochlear inner hair cells (modulating Cav1.3), where CaBP4 loss does not cause hearing impairment, underscoring that the retina is the physiologically critical site of action.

---

## Key Findings

### Finding 1 — CaBP4 is a photoreceptor synaptic-terminal Ca²⁺-binding protein that regulates Cav1.4 and is required for the first retinal synapse

The foundational study by Haeseleer et al. ([PMID: 15452577](https://pubmed.ncbi.nlm.nih.gov/15452577/)) established that **"CaBP4 is specifically expressed in photoreceptors, where it is localized to synaptic terminals."** This precise localization places the protein at the photoreceptor-to-bipolar/horizontal cell synapse rather than in the cell body or outer segment, immediately implicating it in synaptic transmission rather than phototransduction.

The same study demonstrated a direct molecular interaction and a biophysical consequence: **"CaBP4 directly associated with the C-terminal domain of the Ca(v)1.4 alpha(1)-subunit and shifted the activation of Ca(v)1.4 to hyperpolarized voltages in transfected cells."** A hyperpolarizing shift in activation means the channel opens at voltages closer to the photoreceptor's dark resting potential — exactly where sustained Ca²⁺ entry is needed to drive tonic transmitter release.

Genetically, *Cabp4⁻/⁻* mice show a thinner outer plexiform layer, ectopic synapses, roughly 100-fold reduced rod bipolar sensitivity, and reduced cone and rod ERG responses — phenocopying incomplete congenital stationary night blindness (CSNB2). A 2025 review ([PMID: 39930196](https://pubmed.ncbi.nlm.nih.gov/39930196/)) consolidates this, stating that **"CaBP4 seems to be the isoform that is most important for the development of structure and function of the photoreceptor to ON bipolar synapse,"** with its absence causing synaptic ribbon immaturity and a structurally thin outer plexiform layer. Together these establish CaBP4's defining role: a channel-regulating Ca²⁺ sensor indispensable for the first retinal synapse.

### Finding 2 — Mechanism: CaBP4 increases Cav1.4 channel availability by relieving ICDI-domain autoinhibition via the IQ motif

Shaltiel et al. ([PMID: 22936811](https://pubmed.ncbi.nlm.nih.gov/22936811/)) defined the molecular mechanism in detail. CaBP4 **"increases Cav1.4 channel availability by relieving the inhibitory effects of the ICDI domain on voltage-dependent Cav1.4 channel gating."** The Cav1.4 C-terminus contains an intrinsic autoinhibitory module — the ICDI (inhibitor of Ca²⁺-dependent inactivation) domain — that folds back and suppresses channel opening. CaBP4 counteracts this.

Using FRET, the authors showed that **"CaBP4 interacts with the IQ motif of Cav1.4 and that it interferes with the binding of the ICDI domain,"** defining a competitive mechanism: CaBP4 occupies the IQ motif, preventing the ICDI domain from docking there and thereby relieving autoinhibition. The functional requirement for the ICDI domain was confirmed because CaBP4's effect was absent in a Cav1.4 mutant lacking the ICDI. Importantly, two disease-associated CaBP4 mutants retained Cav1.4 binding but only partially preserved function, reducing channel availability — a loss-of-function readout that directly links the molecular mechanism to human disease.

### Finding 3 — Human CABP4 mutations cause incomplete CSNB (CSNB2 / Åland-like) with hyperopia; the auditory role is minor/redundant

Clinically, recessive CABP4 mutations are a leading genetic cause of the incomplete form of congenital stationary night blindness. Almutairi et al. ([PMID: 33369259](https://pubmed.ncbi.nlm.nih.gov/33369259/)) reported that **"Recessive mutations in TRPM1 and CABP4 accounted for the majority of cases"** of CSNB in their cohort, and associated CABP4 with hyperopia. Hove et al. ([PMID: 28002560](https://pubmed.ncbi.nlm.nih.gov/28002560/)) identified a novel CABP4 variant within the Åland eye disease / incomplete CSNB (AED/iCSNB) clinical spectrum, which is otherwise dominated by CACNA1F mutations — consistent with CaBP4 and its target channel (Cav1.4/CACNA1F) producing overlapping phenotypes because they operate in the same molecular pathway.

A separate line of work addressed a potential second site of action. Cui et al. ([PMID: 17947313](https://pubmed.ncbi.nlm.nih.gov/17947313/)) showed CaBP4 is expressed in cochlear inner hair cells and modulates Cav1.3 (CACNA1D), but its influence there is weak and redundant: **"Ca(2+)-dependent inactivation is marginally greater in inner hair cells from CaBP4(-/-) than from wild-type mice, yet CaBP4(-/-) mice are not hearing-impaired."** This negative result is informative — it demonstrates that although CaBP4 can tune Cav1.3 feedback in hair cells, the physiologically critical, non-redundant role is in the retina.

### Finding 4 — CaBP4 interacts with the ciliary chaperone UNC119 within the photoreceptor ribbon-synapse network

CaBP4 does not act in isolation. Fehlhaber et al. ([PMID: 37175812](https://pubmed.ncbi.nlm.nih.gov/37175812/)) showed that **"UNC119 can bind to transducin, the synaptic ribbon protein RIBEYE, and the calcium-binding protein CaBP4, suggesting that UNC119 may have a role in synaptic transmission."** This places CaBP4 in a defined presynaptic protein network linking the synaptic ribbon (RIBEYE, which organizes vesicle release sites) and a trafficking chaperone (UNC119), consistent with CaBP4's function at the structured ribbon synapse.

Clinically corroborating the synaptic site of action, a systematic review of the electronegative ERG ([PMID: 42106701](https://pubmed.ncbi.nlm.nih.gov/42106701/)) notes that the electronegative waveform (dark-adapted b:a ratio < 1.0) **"localizes dysfunction to the inner retina or photoreceptor-bipolar synapse"** — precisely the circuit element in which CaBP4 operates. The electrophysiological signature of CaBP4 loss thus maps onto its molecular localization.

### Finding 5 — Molecular architecture: ~30 kDa, four EF-hands (one degenerate), non-myristoylated, basic disordered N-terminus, light-regulated phosphorylation

Sequence and domain analysis of UniProt P57796 (275 aa, 30.4 kDa) shows four EF-hand domains (residues ~129–164, 183–200, 206–241, 243–275). Canonical Ca²⁺-coordinating acidic residues are present in EF-hand 1 (D142/D144/D146/Y148/E153), EF-hand 3 (D219/D221/D223/…/E230) and EF-hand 4 (D256/N258/D260/…/E267), whereas EF-hand 2 (183–200) lacks the canonical Ca²⁺-binding residues and is degenerate/non-canonical — giving approximately three functional Ca²⁺-binding sites, a hallmark of the CaBP/calmodulin-like family.

Two features distinguish CaBP4 from related sensors. First, the N-terminus (residues ~1–112) is intrinsically disordered and strongly basic (net charge ~+8; a basic cluster at residues 38–55, "TRKRSKKERGLRGSRKRT"). Second, the second residue is threonine rather than glycine, so CaBP4 **lacks the N-myristoylation consensus and is non-myristoylated** — unlike several other CaBPs — meaning its membrane/target association depends on other determinants (e.g., the basic N-terminus and the channel interaction itself). A phosphoserine at Ser42 lies within this disordered N-terminus, and UniProt notes that phosphorylation levels change with light conditions and regulate activity, providing a plausible mechanism for light-dependent tuning of CaBP4's channel-modulating activity. UniProt's function annotation is consistent with the experimental literature: CaBP4 is a modulator of CACNA1D (Cav1.3) and CACNA1F (Cav1.4) that suppresses calcium-dependent inactivation and shifts activation to more hyperpolarized voltages, acting in the cytoplasm/presynapse.

### Finding 6 — CABP4 loss-of-function produces a cone-dominated synaptic disorder rather than classic night blindness

Detailed clinical characterization refines the phenotype of CaBP4 deficiency away from "classic" night blindness and toward a cone-dominated presynaptic defect. Khan et al. ([PMID: 23099293](https://pubmed.ncbi.nlm.nih.gov/23099293/)) studied 11 patients from four consanguineous families carrying the same homozygous frameshift (c.81_82insA; p.Pro28Thrfs*4). The paper restates that **"Calcium binding protein 4 (CABP4), [is] specifically located in photoreceptor synaptic terminals."** Strikingly, **"All patients had congenital nystagmus, stable low vision, photophobia and a normal or near-normal fundus appearance. None complained of night blindness when specifically questioned."** Electrophysiology showed an **"electronegative waveform response to scotopic bright flash, near-normal to subnormal rod function, and delayed and/or decreased cone responses"** — an inner-retinal/synaptic signature with prominent cone involvement.

Hauser et al. ([PMID: 39148310](https://pubmed.ncbi.nlm.nih.gov/39148310/)) reinforced this with a further homozygous CABP4 case: stable reduced acuity (20/150), impaired color vision, small-amplitude nystagmus, photophobia without nyctalopia, hyperopia (+7D), and significantly reduced rod and cone ERG responses. The convergent clinical picture — stable (non-progressive), cone-dominated, photophobic, hyperopic, with electronegative ERG and a normal fundus — is exactly what a presynaptic failure at the photoreceptor terminal predicts: the photoreceptors themselves are structurally intact, but signal transfer across the first synapse is impaired. Consistent with this, a cross-IRD survey ([PMID: 28751151](https://pubmed.ncbi.nlm.nih.gov/28751151/)) found CABP4 mutations coincided with the highest degree of **hyperopia** among inherited retinal dystrophies (mean SE +4.81 D).

### Finding 7 — Consolidated annotation

Integrating all six findings: CaBP4 is a presynaptic, calmodulin-like Ca²⁺ sensor that keeps Cav1.4 (and secondarily Cav1.3) channels available to sustain tonic transmitter release at the first retinal synapse. The evidence is convergent across localization ([PMID: 15452577](https://pubmed.ncbi.nlm.nih.gov/15452577/)), direct molecular mechanism ([PMID: 15452577](https://pubmed.ncbi.nlm.nih.gov/15452577/), [PMID: 22936811](https://pubmed.ncbi.nlm.nih.gov/22936811/)), a secondary channel target ([PMID: 17947313](https://pubmed.ncbi.nlm.nih.gov/17947313/)), molecular architecture (UniProt P57796), presynaptic protein interactions ([PMID: 37175812](https://pubmed.ncbi.nlm.nih.gov/37175812/)), and human loss-of-function genetics ([PMID: 23099293](https://pubmed.ncbi.nlm.nih.gov/23099293/), [PMID: 39148310](https://pubmed.ncbi.nlm.nih.gov/39148310/), [PMID: 33369259](https://pubmed.ncbi.nlm.nih.gov/33369259/), [PMID: 39930196](https://pubmed.ncbi.nlm.nih.gov/39930196/)).

---

## Mechanistic Model / Interpretation

### The primary function in one sentence

CaBP4 is a **Ca²⁺-sensing regulatory subunit** of photoreceptor presynaptic L-type Ca²⁺ channels: by binding the Cav1.4 IQ motif it removes the channel's intrinsic brake (the ICDI domain), shifting activation to hyperpolarized voltages and keeping the channel available for the sustained Ca²⁺ influx that powers tonic glutamate release.

### Why this matters physiologically

Photoreceptors are unusual neurons: in darkness they are **depolarized** and release glutamate continuously; light **hyperpolarizes** them and reduces release. Sustained release depends on Cav1.4, an L-type channel specialized for slow/non-inactivating Ca²⁺ entry. Cav1.4's own ICDI domain tends to limit its availability. CaBP4 counteracts this limitation, ensuring enough channels remain available at physiological membrane potentials to maintain the graded, tonic signal that encodes light intensity at the first synapse.

### ASCII schematic of the mechanism

```
   Photoreceptor synaptic terminal (outer plexiform layer, cytoplasmic face)
   ───────────────────────────────────────────────────────────────────────
                         Cav1.4 (CACNA1F) alpha1 C-terminus
                         +-------[ IQ motif ]-------[ ICDI domain ]
                         |            ^                    |
   WITHOUT CaBP4:        |            |   ICDI folds back  |
                         |            +--------------------+  -> autoinhibition
                         |                                    channel availability DOWN
                         v
                    few open channels -> weak/unsustained Ca2+ influx

                         Cav1.4 (CACNA1F) alpha1 C-terminus
                         +-------[ IQ motif ]        [ ICDI displaced ]
   WITH CaBP4:           |            ^
      CaBP4 (EF-hands) --+            |  CaBP4 occupies IQ, blocks ICDI
      (non-myristoylated,            |  -> activation shifts hyperpolarized
       basic disordered N-term,      v  -> Ca2+-dependent inactivation suppressed
       Ser42 light-phospho)     many available channels -> sustained Ca2+ influx
                                      |
                                      v
                           tonic glutamate release at ribbon synapse
                                      |
                                      v
                  ON-bipolar / horizontal cell signaling  (first visual synapse)
```

### Comparative summary of CaBP4's two channel targets

| Target channel | Tissue | Effect of CaBP4 | Physiological importance | Key evidence |
|----------------|--------|-----------------|--------------------------|--------------|
| **Cav1.4 (CACNA1F)** | Retinal photoreceptor terminals | Hyperpolarizing activation shift; relieves ICDI autoinhibition; ↑ availability; suppresses CDI | **Critical, non-redundant** — loss causes retinal disease | [PMID: 15452577](https://pubmed.ncbi.nlm.nih.gov/15452577/), [PMID: 22936811](https://pubmed.ncbi.nlm.nih.gov/22936811/) |
| **Cav1.3 (CACNA1D)** | Cochlear inner hair cells | Weakly suppresses Ca²⁺-dependent inactivation | **Minor/redundant** — knockout mice hear normally | [PMID: 17947313](https://pubmed.ncbi.nlm.nih.gov/17947313/) |

### Localization and pathway placement

- **Where:** Intracellular, cytoplasmic face of **photoreceptor synaptic terminals** in the **outer plexiform layer**; associated with the ribbon-synapse machinery.
- **Protein network:** Interacts with **UNC119** (ciliary chaperone) and is linked to **RIBEYE** (ribbon scaffold), consistent with a role embedded in the presynaptic release apparatus ([PMID: 37175812](https://pubmed.ncbi.nlm.nih.gov/37175812/)).
- **Pathway:** Phototransduction → graded photoreceptor membrane potential → **Cav1.4-mediated Ca²⁺ influx (CaBP4-regulated)** → glutamate release → ON-bipolar/horizontal cell signaling. CaBP4 operates at the Ca²⁺-channel step, not in the phototransduction cascade itself.

### Genotype–phenotype logic

A presynaptic channel-regulator defect predicts: intact photoreceptor structure (normal fundus), impaired signal transfer to bipolar cells (electronegative ERG, reduced b-wave), non-progressive/congenital course, and — because cone terminals are especially dependent on this pathway — a **cone-dominated** phenotype with photophobia and hyperopia. The observed human phenotypes match this prediction precisely, and the overlap with CACNA1F (Cav1.4) disease confirms that CaBP4 and its target channel lie in the same functional pathway.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution | Supports / Challenges |
|------|-----------------|--------------|------------------------|
| [15452577](https://pubmed.ncbi.nlm.nih.gov/15452577/) | *Essential role of Ca²⁺-binding protein 4, a Cav1.4 channel regulator, in photoreceptor synaptic function* | Localization to photoreceptor terminals; direct Cav1.4 C-terminal binding; hyperpolarizing activation shift; knockout retinal phenotype | **Supports** (foundational) |
| [22936811](https://pubmed.ncbi.nlm.nih.gov/22936811/) | *Complex regulation of Cav1.4 by CaBP4* | Defines mechanism: IQ-motif binding displaces ICDI, increasing channel availability; disease mutants are loss-of-function | **Supports** (mechanism) |
| [17947313](https://pubmed.ncbi.nlm.nih.gov/17947313/) | *Ca²⁺-binding proteins tune Ca²⁺-feedback to Cav1.3 in auditory hair cells* | Secondary Cav1.3 target; cochlear role weak/redundant; knockout mice hear normally | **Supports** (defines retina as critical site) |
| [37175812](https://pubmed.ncbi.nlm.nih.gov/37175812/) | *A novel role for UNC119 as an enhancer of synaptic transmission* | CaBP4–UNC119 interaction; links CaBP4 to RIBEYE/ribbon-synapse network | **Supports** (protein network) |
| [23099293](https://pubmed.ncbi.nlm.nih.gov/23099293/) | *Clinical characterisation of the CABP4-related retinal phenotype* | 11-patient series; cone-dominated, non-nyctalopic, electronegative ERG, normal fundus | **Supports** (presynaptic site; refines phenotype) |
| [39148310](https://pubmed.ncbi.nlm.nih.gov/39148310/) | *Novel homozygous nonsense variant* | Additional case: stable low vision, photophobia without nyctalopia, hyperopia, reduced rod+cone ERG | **Supports** |
| [33369259](https://pubmed.ncbi.nlm.nih.gov/33369259/) | *CSNB update, Saudi Arabia* | CABP4 among the majority genetic causes of incomplete CSNB; hyperopia association | **Supports** (genetics) |
| [28002560](https://pubmed.ncbi.nlm.nih.gov/28002560/) | *Åland eye disease / iCSNB in Denmark* | Novel CABP4 variant within the AED/iCSNB spectrum (mostly CACNA1F) | **Supports** (pathway overlap with Cav1.4) |
| [42106701](https://pubmed.ncbi.nlm.nih.gov/42106701/) | *Electronegative ERG systematic review* | Electronegative ERG localizes dysfunction to inner retina/photoreceptor-bipolar synapse | **Supports** (localization via electrophysiology) |
| [39930196](https://pubmed.ncbi.nlm.nih.gov/39930196/) | *CaBP4 is fundamental for retinal structure and function* (2025 review) | CaBP4 is the key isoform for the photoreceptor→ON-bipolar synapse; loss causes ribbon immaturity | **Supports** (synthesis) |
| [28751151](https://pubmed.ncbi.nlm.nih.gov/28751151/) | *Refractive errors in inherited retinal dystrophies* | CABP4 mutations associated with the highest degree of hyperopia among IRDs | **Supports** (refractive phenotype) |
| [34022913](https://pubmed.ncbi.nlm.nih.gov/34022913/) | *Fasciola gigantica tegumental CaBP4* | Unrelated parasite EF-hand protein sharing only the label | **Excluded** (wrong organism/gene) |

---

## Limitations and Knowledge Gaps

1. **Structure of the CaBP4–Cav1.4 complex.** The mechanism (IQ-motif binding, ICDI displacement) is inferred from FRET and functional electrophysiology rather than from a high-resolution structure of CaBP4 bound to the Cav1.4 C-terminus. The exact stoichiometry, the conformation of CaBP4's degenerate EF-hand 2, and which Ca²⁺-binding sites are occupied during channel modulation remain to be defined structurally.

2. **Role of the disordered, basic N-terminus and Ser42 phosphorylation.** The functional consequence of light-dependent Ser42 phosphorylation is annotated but not mechanistically dissected. How phosphorylation alters CaBP4's affinity for Cav1.4 or its membrane association — and the identity of the responsible kinase/phosphatase — is unknown.

3. **Apo- vs. Ca²⁺-bound regulation.** It is not fully resolved to what extent CaBP4 regulates Cav1.4 in a Ca²⁺-dependent versus Ca²⁺-independent (apo) manner at physiological terminal Ca²⁺ concentrations, which matters for understanding how the sensor responds dynamically to light/dark transitions.

4. **Rod vs. cone dependence.** Human phenotypes are cone-dominated, yet mouse knockouts show marked rod bipolar deficits. The cellular basis for the relative cone vulnerability in humans (channel/subunit composition, redundancy with other CaBPs) is not fully explained.

5. **Species and redundancy.** Much mechanistic and genetic data come from mouse; the degree of functional redundancy with other retinal CaBPs (e.g., CaBP5) in humans is incompletely mapped.

6. **Non-myristoylation consequences.** CaBP4 is non-myristoylated, unlike some family members; how it achieves correct subcellular targeting to the synaptic terminal without a myristoyl switch is not directly demonstrated.

---

## Proposed Follow-up Experiments / Actions

1. **Determine the CaBP4–Cav1.4 C-terminal complex structure** by cryo-EM or X-ray crystallography (± Ca²⁺) to visualize how CaBP4 engages the IQ motif and sterically excludes the ICDI domain, and to assign the roles of individual EF-hands.

2. **Dissect Ser42 phosphorylation** using phospho-null (S42A) and phospho-mimetic (S42D/E) CaBP4 variants in electrophysiological assays and in knock-in mice; identify the kinase/phosphatase and test light-dependent regulation in vivo.

3. **Quantify Ca²⁺-dependence** of CaBP4 regulation by combining EF-hand-inactivating mutations with patch-clamp measurements of Cav1.4 availability and CDI across physiological Ca²⁺ ranges.

4. **Map the N-terminal targeting determinants** (basic cluster 38–55) via truncation/charge-neutralization mutants to test their role in synaptic-terminal localization in the absence of myristoylation.

5. **Characterize the CaBP4–UNC119–RIBEYE network** functionally (e.g., proximity labeling, co-IP, and conditional knockouts) to determine whether UNC119 traffics CaBP4 to the ribbon and how disruption affects channel availability and release.

6. **Test gene-augmentation therapy** for CABP4 retinopathy in the knockout model, building on evidence that the disorder is a congenital, non-progressive synaptic defect with structurally intact photoreceptors — a favorable substrate for restoring presynaptic channel regulation.

7. **Clarify the human cone-dominance** by comparing CaBP4 regulation of cone vs. rod Cav1.4/accessory-subunit complexes, to explain why human loss-of-function is cone-predominant and hyperopic.

---

*Report compiled from 7 confirmed findings and 12 reviewed papers over 5 investigation iterations. All functional claims are attributed to the verified human CABP4 (UniProt P57796) and its mouse ortholog; the unrelated Fasciola gigantica "CaBP4" was explicitly excluded.*


## Artifacts

- [OpenScientist final report](CABP4-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](CABP4-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:34022913
2. PMID:15452577
3. PMID:39930196
4. PMID:22936811
5. PMID:33369259
6. PMID:28002560
7. PMID:17947313
8. PMID:37175812
9. PMID:42106701
10. PMID:23099293
11. PMID:39148310
12. PMID:28751151