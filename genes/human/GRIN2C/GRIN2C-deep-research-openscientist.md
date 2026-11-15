---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-14T20:26:30.790414'
end_time: '2026-11-14T21:01:05.270235'
duration_seconds: 2074.48
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: GRIN2C
  gene_symbol: GRIN2C
  uniprot_accession: Q14957
  protein_description: 'RecName: Full=Glutamate receptor ionotropic, NMDA 2C {ECO:0000305};
    Short=GluN2C {ECO:0000250|UniProtKB:Q00961}; AltName: Full=Glutamate [NMDA] receptor
    subunit epsilon-3 {ECO:0000250|UniProtKB:Q01098}; AltName: Full=N-methyl D-aspartate
    receptor subtype 2C; Short=NMDAR2C {ECO:0000250|UniProtKB:Q00961}; Short=NR2C
    {ECO:0000303|PubMed:9037519}; Flags: Precursor;'
  gene_info: Name=GRIN2C {ECO:0000312|HGNC:HGNC:4587}; Synonyms=NMDAR2C;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the glutamate-gated ion channel (TC 1.A.10.1)
  protein_domains: ANF_lig-bd_rcpt. (IPR001828); Glu/Gly-bd. (IPR019594); Iono_Glu_rcpt_met.
    (IPR001508); Ionotropic_Glu_rcpt. (IPR015683); Iontro_rcpt_C. (IPR001320)
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
citation_count: 21
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: GRIN2C-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: GRIN2C-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q14957
- **Protein Description:** RecName: Full=Glutamate receptor ionotropic, NMDA 2C {ECO:0000305}; Short=GluN2C {ECO:0000250|UniProtKB:Q00961}; AltName: Full=Glutamate [NMDA] receptor subunit epsilon-3 {ECO:0000250|UniProtKB:Q01098}; AltName: Full=N-methyl D-aspartate receptor subtype 2C; Short=NMDAR2C {ECO:0000250|UniProtKB:Q00961}; Short=NR2C {ECO:0000303|PubMed:9037519}; Flags: Precursor;
- **Gene Information:** Name=GRIN2C {ECO:0000312|HGNC:HGNC:4587}; Synonyms=NMDAR2C;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the glutamate-gated ion channel (TC 1.A.10.1)
- **Key Domains:** ANF_lig-bd_rcpt. (IPR001828); Glu/Gly-bd. (IPR019594); Iono_Glu_rcpt_met. (IPR001508); Ionotropic_Glu_rcpt. (IPR015683); Iontro_rcpt_C. (IPR001320)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GRIN2C" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GRIN2C' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GRIN2C** (gene ID: GRIN2C, UniProt: Q14957) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# GRIN2C / GluN2C (UniProt Q14957): Functional Annotation Report

**Gene:** GRIN2C (HGNC:4587) · **Protein:** Glutamate receptor ionotropic, NMDA 2C (GluN2C / NR2C / NMDAR2C / glutamate [NMDA] receptor subunit epsilon-3) · **Organism:** *Homo sapiens* · **UniProt:** Q14957 · **Family:** Glutamate-gated ion channel (TC 1.A.10.1)

---

## Summary

GRIN2C encodes **GluN2C** (historically NR2C), one of four GluN2 subunits (A–D) of the **N-methyl-D-aspartate receptor (NMDAR)**, the glutamate-gated, Ca²⁺-permeable ionotropic glutamate receptor that mediates the slow component of excitatory neurotransmission in the central nervous system. GluN2C is **not an enzyme or a classical transporter**; it is a **ligand-gated cation channel subunit**. Specifically, it is the **glutamate-binding** subunit that co-assembles with two obligatory **glycine/D-serine-binding GluN1 subunits** and (usually) a second GluN2 subunit to form a heterotetrameric channel. Its "substrate" is the agonist glutamate (bound by its ligand-binding domain), and the channel it helps form conducts Na⁺, K⁺, and—critically—Ca²⁺ across the plasma membrane upon coincident agonist binding and membrane depolarization. This identity is firmly established by cryo-EM structures of human GluN1-2C, GluN1-2A-2C, and GluN1-2D receptors ([PMID: 36309015](https://pubmed.ncbi.nlm.nih.gov/36309015/)).

The **primary functional contribution** of GluN2C is to confer a **distinct biophysical and pharmacological identity** on the receptors into which it is incorporated. GluN2C-containing NMDARs display **low sensitivity to voltage-dependent Mg²⁺ block, low single-channel conductance, high open probability, and slow deactivation kinetics**. These properties make GluN2C-containing receptors well-suited for **tonic conductance and temporal summation** of synaptic input, in contrast to the fast, high-conductance, strongly Mg²⁺-blocked GluN2A-containing receptors. GluN2C is most strongly **enriched in cerebellar granule cells**, where it developmentally replaces GluN2B and assembles predominantly into **triheteromeric GluN1/GluN2A/GluN2C** receptors, with additional functional roles in thalamocortical sensory relay neurons, the auditory midbrain (inferior colliculus), white-matter myelin/oligodendrocytes, and cortical astrocytes.

Mechanistically, GluN2C operates at **postsynaptic (and specialized peri-axonal/myelinic) membranes**. Its Ca²⁺ influx couples to downstream **neuronal nitric oxide synthase (nNOS)/nitric oxide (NO)** signaling in granule cells, and its intracellular **C-terminal domain functions as a signaling and trafficking hub**—phosphorylated by Akt/PKB at Ser1096, bound by 14-3-3ε, and linked to pro-survival trafficking. At the circuit level GluN2C sets the **cortical excitatory–inhibitory (E/I) balance** and shapes **neuronal gamma oscillations**, connecting it to NMDAR-hypofunction models of schizophrenia and other neuropsychiatric conditions. The gene symbol and organism were verified: GRIN2C/GluN2C in *Homo sapiens* matches the glutamate-gated ion channel family and the ligand-binding/ion-channel domain architecture given in UniProt, and all retrieved literature concerns this NMDAR subunit.

---

## Key Findings

### F001 — GluN2C is a glutamate-binding regulatory subunit of the ionotropic NMDA receptor

GluN2C is a subunit of the NMDAR, which is a **glycine- and glutamate-gated ion channel existing as a heterotetramer** composed of two obligatory GluN1 subunits and two GluN2 (A–D) and/or GluN3 (A–B) subunits. Within this assembly, GluN1 subunits bind the co-agonist glycine/D-serine, while GluN2 subunits—including GluN2C—bind the principal agonist **glutamate**. Cryo-EM structures of human GluN1-2C, GluN1-2A-2C, and GluN1-2D receptors directly resolve GluN2C as a glutamate-gated subunit forming part of a cation channel, and show that "the GluN2C and GluN2D subunits form ion channels with distinct properties and spatio-temporal expression patterns" ([PMID: 36309015](https://pubmed.ncbi.nlm.nih.gov/36309015/)).

The gating mechanism is now understood at the structural level. Activation and competitive inhibition "occur by controlling the tension of the linker between the ligand-binding domain and the transmembrane ion channel of the GluN2 subunit" ([PMID: 32610085](https://pubmed.ncbi.nlm.nih.gov/32610085/)). In other words, agonist binding closes the bilobed ligand-binding domain (LBD) around glutamate, and the resulting conformational change pulls on the LBD-to-transmembrane linker, applying tension that opens the ion-conducting pore. This establishes the **core molecular function** of the protein: GluN2C is the glutamate sensor whose LBD closure is mechanically transduced into pore opening, gating a cation channel permeable to Na⁺, K⁺, and Ca²⁺.

### F002 — Distinctive biophysics: low Mg²⁺ sensitivity, low conductance, slow deactivation

The defining functional signature of GluN2C-containing receptors is a set of biophysical properties that set them apart from GluN2A/2B-containing receptors. GluN2C/D-containing NMDARs are **relatively insensitive to the voltage-dependent Mg²⁺ block** that normally silences NMDARs at resting membrane potential ([PMID: 39240253](https://pubmed.ncbi.nlm.nih.gov/39240253/); [PMID: 31110197](https://pubmed.ncbi.nlm.nih.gov/31110197/)). This means GluN2C-containing receptors can pass current even near resting potential, enabling a **tonic, non-coincidence-dependent conductance** and enhanced temporal summation of inputs.

Single-channel analysis of triheteromeric GluN1/GluN2A/GluN2C receptors shows **three conductance levels** and bursting behavior similar to GluN1/GluN2A, but with a **single-channel open time and open probability reminiscent of GluN1/GluN2C**, and a **deactivation time course intermediate** between GluN1/GluN2A and GluN1/GluN2C receptors ([PMID: 30056832](https://pubmed.ncbi.nlm.nih.gov/30056832/)). Thus GluN2C lowers unitary conductance and slows the receptor's deactivation (prolonging the response to a glutamate transient). Collectively these properties—low Mg²⁺ block, low conductance, slow deactivation—represent the **primary biophysical function** that GluN2C contributes to any receptor in which it is incorporated.

| Property | GluN2A-type | GluN2C-containing |
|---|---|---|
| Voltage-dependent Mg²⁺ block | Strong | Weak (low sensitivity) |
| Single-channel conductance | High (main ~50 pS) | Low / multiple sublevels |
| Open probability | Variable | High (long bursts, low open time) |
| Deactivation kinetics | Fast | Slow / prolonged |
| Functional consequence | Coincidence detection | Tonic conductance, temporal summation |

### F003 — Enrichment in cerebellar granule cells and triheteromeric assembly

GluN2C has a highly restricted expression pattern, with its **strongest enrichment in cerebellar granule cells** ([PMID: 41223665](https://pubmed.ncbi.nlm.nih.gov/41223665/)). Importantly, in these neurons GluN2C does not form simple diheteromeric GluN1/GluN2C receptors; instead, the **predominant native NMDARs are triheteromeric GluN1/GluN2A/GluN2C receptors**. Co-expression of GluN2A "occludes cell surface expression of diheteromeric GluN1/GluN2C receptors," so the triheteromer is the dominant receptor population at the granule-cell surface ([PMID: 30056832](https://pubmed.ncbi.nlm.nih.gov/30056832/)).

This assembly is developmentally regulated. During cerebellar maturation, a **subunit switch from NR2B (GluN2B) to NR2C (GluN2C)** occurs in granule cells, and this switch is driven by NMDA/AMPA-receptor-dependent neuronal activity ([PMID: 18685090](https://pubmed.ncbi.nlm.nih.gov/18685090/)). The developmental switch converts granule-cell NMDARs from the fast, Mg²⁺-sensitive GluN2B profile to the slow, Mg²⁺-insensitive GluN2C profile, matching the receptor's kinetics to the needs of the mature cerebellar circuit. (Notably, this switch is independent of neuregulin/ErbB signaling in vivo — [PMID: 19244516](https://pubmed.ncbi.nlm.nih.gov/19244516/).)

### F004 — The C-terminal domain is a signaling hub: Akt-Ser1096 phosphorylation, 14-3-3 binding, pro-survival trafficking, and nNOS/NO coupling

Beyond its channel-forming role, GluN2C has a functionally important intracellular C-terminal tail. **PKB/Akt directly phosphorylates NR2C (GluN2C) on serine 1096 (S1096)**, and **14-3-3ε binds NR2C in an S1096-phosphorylation-dependent manner**. Both growth-factor stimulation and NMDAR activity drive a robust increase in S1096 phosphorylation and a corresponding increase in **surface expression of cerebellar NMDARs**. Critically, "NR2C expression, unlike NR2A and NR2B, supports neuronal survival" ([PMID: 19477150](https://pubmed.ncbi.nlm.nih.gov/19477150/)). This identifies a specific **pro-survival trafficking pathway**: growth factor → Akt → S1096 phosphorylation → 14-3-3ε binding → increased GluN2C surface delivery → neuronal survival, distinguishing GluN2C from the other GluN2 subunits.

Downstream of channel activity, GluN2C couples to nitric oxide signaling. In cultured cerebellar granule cells, "a GluN2C agonist increased nNOS and NO, whereas a GluN2C inhibitor decreased both; selective blockade of nNOS abolished the GluN2C-agonist-evoked rise in NO" ([PMID: 41223665](https://pubmed.ncbi.nlm.nih.gov/41223665/)). Because NMDARs are highly Ca²⁺-permeable and nNOS is Ca²⁺/calmodulin-activated, this links GluN2C-mediated Ca²⁺ influx to the **nNOS → NO** second-messenger pathway in granule cells—one of the concrete biochemical pathways in which GluN2C functions.

### F005 — Extra-cerebellar roles: myelin/peri-axonal compartment, auditory midbrain, and thalamocortical sensory inputs

Although most enriched in cerebellum, GluN2C (together with GluN2D) operates in several other compartments, consistent with broad but specialized extra-cerebellar roles. In **white-matter myelin**, "ischemic conditions trigger activation of myelinic NMDA receptors incorporating GluN2C/D subunits following release of axonal vesicular glutamate into the peri-axonal space under the myelin sheath," and a GluN2C/D-selective negative allosteric modulator shields myelin from ischemic injury ([PMID: 29531223](https://pubmed.ncbi.nlm.nih.gov/29531223/)). This places GluN2C-containing receptors in a **non-synaptic, peri-axonal membrane compartment** where they contribute to white-matter excitotoxicity.

In the **auditory midbrain**, "GluN2C/D-containing NMDA receptors enhance temporal summation and increase sound-evoked and spontaneous firing in the inferior colliculus," a direct functional consequence of their low Mg²⁺ sensitivity ([PMID: 39240253](https://pubmed.ncbi.nlm.nih.gov/39240253/)). In **thalamocortical neurons**, GluN2C shows input-specific localization, being "more abundant at sensory inputs" than at corticothalamic inputs ([PMID: 40123534](https://pubmed.ncbi.nlm.nih.gov/40123534/)). These findings demonstrate that GluN2C's slow, tonic biophysical signature is deployed where temporal integration of input is functionally advantageous.

### F006 — GluN2C creates a pharmacologically distinct, selectively druggable NMDAR subtype

Incorporation of GluN2C produces a receptor with a unique pharmacological profile that is exploitable for subtype-selective drugs. The pan-positive allosteric modulator (PAM) EU1622-240 "enhances the function of all GluN2 subunit-containing NMDARs ... with the strongest effects on GluN2C- and GluN2D-containing NMDARs" ([PMID: 41054222](https://pubmed.ncbi.nlm.nih.gov/41054222/)). The GluN2C/D-selective PAM **(+)-EU1180-453** "potentiates triheteromeric NMDARs containing at least one GluN2C or GluN2D subunit" and "increases glutamate efficacy for GluN2C/GluN2D-containing NMDARs both by prolonging the deactivation time and by potentiating the peak response amplitude" ([PMID: 40560934](https://pubmed.ncbi.nlm.nih.gov/40560934/); [PMID: 39574703](https://pubmed.ncbi.nlm.nih.gov/39574703/)).

The structural basis for GluN2C selectivity was resolved by cryo-EM, which revealed "unique inter-subunit and domain arrangements of the GluN2C NMDARs, which contribute to functional regulation and formation of the PAM binding pocket and is distinct from GluN2D NMDARs" ([PMID: 36309015](https://pubmed.ncbi.nlm.nih.gov/36309015/)). This explains how GluN2C-selective positive modulators such as PYD-106 bind a pocket uniquely formed by the GluN2C subunit arrangement. Negative allosteric modulators also show graded, subtype-dependent maximal inhibition across GluN2A/2B/2C/2D (e.g., UBP792: 52%/70%/87%/89% maximal inhibition respectively — [PMID: 34610288](https://pubmed.ncbi.nlm.nih.gov/34610288/)), and a GluN2C/D-selective NAM protects myelin from ischemia ([PMID: 29531223](https://pubmed.ncbi.nlm.nih.gov/29531223/)). Together these define GluN2C as a **distinct and tractable drug target**.

### F007 — GluN2C dictates subtype-specific gating/conformational behavior; its functional domains are evolutionarily conserved

Single-molecule FRET experiments show that the variable GluN2 subunit (including GluN2C), paired with an identical GluN1, exerts a "strong, subtype-specific influence on GluN1 conformational rearrangements" across apo, partially liganded, and fully liganded states ([PMID: 39154344](https://pubmed.ncbi.nlm.nih.gov/39154344/); [PMID: 38370786](https://pubmed.ncbi.nlm.nih.gov/38370786/)). This provides the **conformational basis for the divergent activity, desensitization, and agonist potency** of GluN2C-containing receptors—i.e., GluN2C does not merely passively occupy a slot but actively dictates the gating conformations of the whole receptor.

Cross-species conservation analysis reinforces which regions carry the core function. In human NMDAR subunits, "the transmembrane domain is most highly conserved, followed by the ligand-binding domain, which maintains conservation of amino acids that participate in the binding of ligands. The N-terminal domain is less well conserved" ([PMID: 41233739](https://pubmed.ncbi.nlm.nih.gov/41233739/) / [PMID: 40766232](https://pubmed.ncbi.nlm.nih.gov/40766232/)). The C-terminal domain is the least conserved overall, but **functional motifs within it—phosphorylation, palmitoylation, ubiquitylation sites and protein-binding motifs—are better conserved**. This evolutionary evidence independently corroborates that the **ligand-binding and channel domains** (the glutamate sensor and pore) are the most functionally constrained parts of GluN2C, consistent with the UniProt domain annotation (ANF_lig-bd_rcpt, Glu/Gly-bd, Iono_Glu_rcpt).

### F008 — GluN2C regulates cortical E/I balance, oscillations, cognition; expressed in astrocytes as well as neurons

At the circuit level, loss of GluN2C shifts the cortical balance of excitation and inhibition. GluN2C-knockout medial prefrontal cortex (mPFC) pyramidal neurons show **reduced mEPSC frequency and dendritic spine density** alongside **higher mIPSC frequency and more perisomatic GAD67 puncta**, indicating a shift toward greater inhibition ([PMID: 27922130](https://pubmed.ncbi.nlm.nih.gov/27922130/)). GluN2C-KO and heterozygous mice show **exaggerated MK-801-induced oscillations** and deficits in cognition and sensorimotor gating, and lower GluN2C expression has been reported in schizophrenia postmortem brain—linking GluN2C to NMDAR-hypofunction models of neuropsychiatric disease.

GluN2C and GluN2D have **opposing roles in modulating neuronal oscillations**. A proposed model places "NMDARs containing GluN2C in astrocytes and GluN2D in interneurons" to "detect local cortical excitatory synaptic activity and provide ... bidirectional feedback," with basal low-gamma oscillatory power elevated in GluN2C-KO mice ([PMID: 31786200](https://pubmed.ncbi.nlm.nih.gov/31786200/)). This finding documents a **non-neuronal (astrocytic) site of GluN2C action** in addition to its neuronal roles, broadening the cellular localization where the gene product carries out its function.

---

## Mechanistic Model / Interpretation

The findings converge on a coherent model of GluN2C as a **tuning subunit** that reprograms NMDAR biophysics, trafficking, and downstream signaling in a cell-type- and compartment-specific manner.

**1. Molecular level — the glutamate-gated channel.**

```
   Glycine / D-serine          Glutamate
        │                         │
     [GluN1 LBD]   +    [GluN2C LBD]   ──► clamshell closure
        │                         │
        └──── LBD–TMD linker tension ────┘
                     │
              Pore (M1–M3, re-entrant M2 loop)
                     │
           Ca²⁺ / Na⁺ influx, K⁺ efflux
```
GluN2C binds glutamate; GluN1 binds glycine/D-serine. Dual agonist binding closes both LBDs, and the tension transmitted through the LBD–transmembrane linker opens the cation pore (F001). GluN2C sets the pore's low conductance, confers weak Mg²⁺ block, and slows deactivation (F002), and it dictates the GluN1 conformational trajectory that underlies these properties (F007).

**2. Cellular level — trafficking and downstream signaling.**

```
  Growth factor / NMDAR activity
            │
          Akt/PKB ──► GluN2C-Ser1096-P ──► 14-3-3ε binding
            │                                   │
            └────────► ↑ surface GluN2C ◄───────┘
                          │
            Ca²⁺ influx ──► nNOS (Ca²⁺/CaM) ──► NO
                          │
                   Neuronal survival
```
The GluN2C C-terminal tail is a signaling node: Akt-mediated S1096 phosphorylation recruits 14-3-3ε and promotes surface delivery and survival (F004), while channel-mediated Ca²⁺ influx drives nNOS/NO production (F004).

**3. Circuit / anatomical level — where GluN2C acts.**

| Location | Assembly / cell type | Functional role | Evidence |
|---|---|---|---|
| Cerebellar granule cells | GluN1/GluN2A/GluN2C triheteromer (post NR2B→NR2C switch) | Slow, tonic NMDAR signaling; nNOS/NO | F003, F004 |
| Thalamocortical neurons | GluN2C at sensory inputs | Input-specific temporal integration | F005 |
| Inferior colliculus (auditory midbrain) | GluN2C/D | Temporal summation, ↑ firing | F005 |
| Myelin / peri-axonal space | GluN2C/D myelinic NMDARs | White-matter (patho)physiology, ischemic injury | F005 |
| Cortical astrocytes | GluN2C | Detect excitatory activity, oscillatory feedback | F008 |
| Prefrontal cortex (network) | GluN2C (loss) | Sets E/I balance, gamma oscillations, cognition | F008 |

**Unifying interpretation.** The single biophysical theme—**low Mg²⁺ block + low conductance + slow deactivation**—explains GluN2C's deployment across all these sites: wherever the circuit needs **tonic, temporally-integrating, non-coincidence-dependent** NMDAR conductance rather than fast coincidence detection, GluN2C is incorporated. Its unique subunit arrangement additionally creates a **selective allosteric pocket** (F006), and its C-terminal tail adds a **trafficking/survival signaling layer** (F004) absent from GluN2A/2B. This makes GluN2C simultaneously a biophysical tuner, a signaling scaffold, and a druggable subtype marker.

---

## Evidence Base

| PMID | Title (abbrev.) | Supports | Role |
|---|---|---|---|
| [36309015](https://pubmed.ncbi.nlm.nih.gov/36309015/) | Structural insights into GluN1-2C/2A-2C/2D NMDARs | F001, F006 | Cryo-EM: GluN2C as glutamate-gated subunit; unique PAM pocket |
| [32610085](https://pubmed.ncbi.nlm.nih.gov/32610085/) | Structural basis of functional transitions in NMDARs | F001 | Gating via LBD–TMD linker tension |
| [39240253](https://pubmed.ncbi.nlm.nih.gov/39240253/) | GluN2C/D NMDARs in inferior colliculus | F002, F005 | Low Mg²⁺; temporal summation in auditory midbrain |
| [30056832](https://pubmed.ncbi.nlm.nih.gov/30056832/) | Triheteromeric GluN1/2A/2C in granule cells | F002, F003 | Single-channel properties; dominant native assembly |
| [41223665](https://pubmed.ncbi.nlm.nih.gov/41223665/) | Cerebellar GluN2C and sleep deprivation | F003, F004 | Granule-cell enrichment; nNOS/NO coupling |
| [18685090](https://pubmed.ncbi.nlm.nih.gov/18685090/) | NR2B/NR2C regulation in granule cells | F003 | Activity-driven NR2B→NR2C switch |
| [19477150](https://pubmed.ncbi.nlm.nih.gov/19477150/) | Akt phosphorylation of NR2C | F004 | S1096 phosphorylation, 14-3-3ε, survival |
| [29531223](https://pubmed.ncbi.nlm.nih.gov/29531223/) | Vesicular glutamate and myelin damage | F005, F006 | Myelinic GluN2C/D; NAM protection |
| [40123534](https://pubmed.ncbi.nlm.nih.gov/40123534/) | Input-specific GluN2 in thalamocortical neurons | F005 | GluN2C at sensory inputs |
| [41054222](https://pubmed.ncbi.nlm.nih.gov/41054222/) | NMDAR PAM EU1622-240 | F006 | Strongest potentiation of GluN2C/D |
| [40560934](https://pubmed.ncbi.nlm.nih.gov/40560934/) | (+)-EU1180-453 GluN2C/D PAM | F006 | Prolongs deactivation, ↑ peak amplitude |
| [34610288](https://pubmed.ncbi.nlm.nih.gov/34610288/) | UBP792 NAM | F006 | Graded subtype-selective inhibition |
| [39154344](https://pubmed.ncbi.nlm.nih.gov/39154344/) | Subtype-specific conformational landscape | F007 | GluN2 dictates GluN1 conformation |
| [38370786](https://pubmed.ncbi.nlm.nih.gov/38370786/) | Conformational basis of allosteric control | F007 | Subtype-specific gating determinants |
| [40766232](https://pubmed.ncbi.nlm.nih.gov/40766232/) | Conservation of NMDAR subunits in zebrafish | F007 | TMD/LBD most conserved; CTD motifs conserved |
| [27922130](https://pubmed.ncbi.nlm.nih.gov/27922130/) | GluN2C controls cortical E/I balance | F008 | KO: E/I shift, oscillations, cognition |
| [31786200](https://pubmed.ncbi.nlm.nih.gov/31786200/) | GluN2C/GluN2D opposing roles in oscillations | F008 | Astrocytic GluN2C; oscillatory feedback |

**Gene identity confirmation.** All retrieved literature concerns the NMDAR subunit GluN2C/NR2C in mammalian (human/rodent) nervous tissue, matching the UniProt record (Q14957; GRIN2C; glutamate-gated ion channel family; ligand-binding and ionotropic glutamate receptor domains). No conflicting gene with the same symbol was encountered. The identity verification is therefore satisfied.

---

## Limitations and Knowledge Gaps

- **Species of evidence.** Much mechanistic detail (knockout phenotypes, single-channel recordings, Akt/S1096 phosphorylation, nNOS coupling) derives from **rodent** systems or heterologous expression. While NMDAR subunits are highly conserved between human and rodent/zebrafish (F007), direct human experimental data are comparatively sparse.
- **Human disease variants.** Compared to GRIN1/GRIN2A/GRIN2B/GRIN2D, GRIN2C-specific human pathogenic-variant literature is **limited** (confirmed sparse during iteration 4). GRIN2C is less frequently implicated in monogenic neurodevelopmental disorders than its paralogs, so genotype–phenotype inference is weaker.
- **Triheteromer complexity.** Native receptors are predominantly triheteromeric (GluN1/GluN2A/GluN2C), making it experimentally difficult to isolate "pure" GluN2C contributions; many biophysical/pharmacological statements derive from mixed or heterologous diheteromeric contexts.
- **Astrocytic GluN2C** rests on a proposed model ([PMID: 31786200](https://pubmed.ncbi.nlm.nih.gov/31786200/)) and would benefit from independent confirmation of functional astrocytic NMDAR currents with defined GluN2C dependence.
- **Direct CTD interactome.** Beyond 14-3-3ε and Akt, the full GluN2C C-terminal protein-interaction network (PSD scaffolds, kinases) is less characterized than for GluN2A/2B.

---

## Proposed Follow-up Experiments / Actions

1. **Human-neuron validation.** Use GRIN2C-tagged human iPSC-derived cerebellar granule-like neurons or cerebellar organoids to confirm the NR2B→NR2C developmental switch, triheteromeric assembly, and low-Mg²⁺/slow-deactivation biophysics in a human context.
2. **S1096 signaling in situ.** Generate a phospho-S1096-specific antibody and a knock-in S1096A mouse to test, in vivo, whether Akt/14-3-3ε-dependent trafficking is required for GluN2C surface expression and granule-cell survival.
3. **Astrocytic GluN2C.** Combine cell-type-specific conditional GRIN2C deletion (astrocyte vs. neuron) with gamma-oscillation recordings to dissect the proposed astrocytic feedback model (F008).
4. **Subtype-selective pharmacology.** Co-crystallize/cryo-EM the GluN2C-unique PAM pocket with PYD-106-class and EU1180/EU1622-class modulators to enable structure-guided design of truly GluN2C-selective (vs. GluN2C/D) ligands.
5. **nNOS/NO pathway mapping.** Quantify the GluN2C-Ca²⁺→nNOS→NO axis with genetically encoded Ca²⁺/NO sensors in granule cells, testing whether GluN2C's low conductance nonetheless delivers sufficient Ca²⁺ for nNOS activation via spatial coupling.
6. **Myelinic receptors.** Test GluN2C/D-selective NAMs in human white-matter ischemia models to assess translational neuroprotective potential (F005).
7. **Variant functional screening.** Systematically express rare human GRIN2C missense variants in vitro with electrophysiology to populate the currently sparse genotype–function map and determine gain- vs. loss-of-function directionality.

---

*Report compiled from 8 confirmed findings and 37 reviewed papers over 5 investigation iterations. Gene/protein identity verified: GRIN2C → GluN2C (NR2C), UniProt Q14957, Homo sapiens, glutamate-gated ion channel (NMDA receptor) subunit.*


## Artifacts

- [OpenScientist final report](GRIN2C-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](GRIN2C-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:36309015
2. PMID:32610085
3. PMID:39240253
4. PMID:31110197
5. PMID:30056832
6. PMID:41223665
7. PMID:18685090
8. PMID:19244516
9. PMID:19477150
10. PMID:29531223
11. PMID:40123534
12. PMID:41054222
13. PMID:40560934
14. PMID:39574703
15. PMID:34610288
16. PMID:39154344
17. PMID:38370786
18. PMID:41233739
19. PMID:40766232
20. PMID:27922130
21. PMID:31786200