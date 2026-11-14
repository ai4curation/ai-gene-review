---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-14T20:26:17.882501'
end_time: '2026-11-14T20:37:02.224492'
duration_seconds: 644.34
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: GRIN3A
  gene_symbol: GRIN3A
  uniprot_accession: Q8TCU5
  protein_description: 'RecName: Full=Glutamate receptor ionotropic, NMDA 3A {ECO:0000305};
    Short=GluN3A {ECO:0000250|UniProtKB:Q9R1M7}; AltName: Full=N-methyl-D-aspartate
    receptor subtype 3A; Short=NMDAR3A; Short=NR3A {ECO:0000303|PubMed:11735224};
    AltName: Full=NMDAR-L {ECO:0000250|UniProtKB:Q9R1M7}; Flags: Precursor;'
  gene_info: Name=GRIN3A {ECO:0000312|HGNC:HGNC:16767}; Synonyms=KIAA1973;
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
citation_count: 15
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: GRIN3A-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: GRIN3A-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q8TCU5
- **Protein Description:** RecName: Full=Glutamate receptor ionotropic, NMDA 3A {ECO:0000305}; Short=GluN3A {ECO:0000250|UniProtKB:Q9R1M7}; AltName: Full=N-methyl-D-aspartate receptor subtype 3A; Short=NMDAR3A; Short=NR3A {ECO:0000303|PubMed:11735224}; AltName: Full=NMDAR-L {ECO:0000250|UniProtKB:Q9R1M7}; Flags: Precursor;
- **Gene Information:** Name=GRIN3A {ECO:0000312|HGNC:HGNC:16767}; Synonyms=KIAA1973;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the glutamate-gated ion channel (TC 1.A.10.1)
- **Key Domains:** ANF_lig-bd_rcpt. (IPR001828); Glu/Gly-bd. (IPR019594); Iono_Glu_rcpt_met. (IPR001508); Ionotropic_Glu_rcpt. (IPR015683); Iontro_rcpt_C. (IPR001320)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GRIN3A" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GRIN3A' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GRIN3A** (gene ID: GRIN3A, UniProt: Q8TCU5) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# GRIN3A (GluN3A / NR3A): Functional Annotation Report

**Gene:** GRIN3A (HGNC:16767; synonym KIAA1973)
**Protein:** Glutamate receptor ionotropic, NMDA 3A (GluN3A / NMDAR3A / NR3A / NMDAR-L)
**UniProt:** Q8TCU5
**Organism:** *Homo sapiens* (Human)
**Family:** Glutamate-gated ion channel superfamily (TC 1.A.10.1)
**Key domains:** ANF/ligand-binding receptor (IPR001828); Glu/Gly-binding (IPR019594); Ionotropic glutamate receptor, metazoa (IPR001508); Ionotropic glutamate receptor (IPR015683); Ionotropic receptor C-terminal (IPR001320)

---

## Identity Verification

The gene symbol **GRIN3A** unambiguously matches the UniProt target Q8TCU5. All retrieved literature concerns the same human/mammalian protein: the NMDA receptor subunit GluN3A (also called NR3A or NMDAR3A). The protein family (glutamate-gated ion channel) and its diagnostic domains (ANF/ligand-binding, Glu/Gly-binding, ionotropic glutamate receptor channel and C-terminal domains) are consistent across the primary literature, cryo-EM structural studies, and database annotations. No conflicting gene with the same symbol was encountered. The research below therefore describes the correct target with high confidence.

---

## Summary

**GRIN3A encodes GluN3A (NR3A), a non-conventional, glycine/D-serine–binding — not glutamate-binding — subunit of the NMDA-type ionotropic glutamate receptor.** Its defining molecular property is that, unlike the GluN2 subunits that bind glutamate, GluN3A binds the co-agonist glycine (and D-serine) at its extracellular ligand-binding domain. This single difference reconfigures the receptors it joins. When GluN3A is incorporated into conventional GluN1/GluN2 NMDARs, it acts as a dominant-negative "molecular brake," reducing single-channel conductance, lowering Ca²⁺ permeability, and reducing Mg²⁺ sensitivity. When GluN3A assembles with GluN1 alone, the resulting GluN1/GluN3A diheteromer is a glutamate-independent **excitatory glycine receptor** — a channel gated by glycine binding to GluN3A rather than by glutamate.

**The primary biological role of GluN3A is developmental: it times the maturation of excitatory synapses and drives dendritic spine pruning during the early postnatal period, when its expression peaks.** GluN3A operates at the neuronal postsynaptic membrane. Its intracellular C-terminal tail is the hub of this function: it binds the postsynaptic scaffold GIT1, thereby suppressing the GIT1/βPIX→Rac1→PAK actin-signaling pathway that would otherwise promote spine growth and stabilization. This inhibitory action is activity-dependent, restricting GluN3A's negative effect to under-used synapses, which are then eliminated. The amount of GluN3A on the cell surface is further tuned by clathrin/AP2-mediated endocytosis through a C-terminal YWL motif, regulated by Src-family tyrosine phosphorylation and the adaptor PACSIN1.

**GluN3A is normally down-regulated as the brain matures, permitting synapse strengthening and the acquisition of adult plasticity.** Loss of GluN3A enhances NMDA responses, increases spine density, and augments hippocampal long-term potentiation (LTP) via a CaMKII-dependent mechanism; it also increases vulnerability to ischemic excitotoxicity, revealing a neuroprotective role in adults. Conversely, mis-timed reactivation of GluN3A is mechanistically linked to schizophrenia, autism, addiction, neurodegenerative disease, and stroke. Recent single-molecule and cryo-EM studies (2026) establish the native GluN1-GluN3A receptor as a diheteromer gated solely through GluN3A conformational changes, and define its allosteric pharmacology.

---

## Key Findings

### 1. GluN3A is an inhibitory / dominant-negative NMDAR subunit (F001)

GluN3A assembles with the obligatory GluN1 subunit and glutamate-binding GluN2 subunits to form NMDA receptors, but its incorporation suppresses the receptor's cardinal biophysical features. Das et al. (1998, *Nature*) showed by co-immunoprecipitation that NR3A (GluN3A) physically associates with NR1 and NR2 in cerebrocortical extracts, and by single-channel recording in *Xenopus* oocytes that adding NR3A to NR1+NR2 produces a **smaller unitary conductance** [PMID: 9620802](https://pubmed.ncbi.nlm.nih.gov/9620802/). Chowdhury et al. (2013) further established that GluN3A "endows NMDAR channels with low calcium permeability and reduced magnesium sensitivity compared with NMDARs comprising only GluN1 and GluN2 subunits" [PMID: 23447623](https://pubmed.ncbi.nlm.nih.gov/23447623/).

The net effect is that GluN3A behaves as a **dominant-negative modulator**: the two hallmark properties that make NMDARs coincidence detectors and sources of synaptic Ca²⁺ — high Ca²⁺ permeability and voltage-dependent Mg²⁺ block — are both attenuated. Consistently, genetic knockout of GluN3A enhances NMDA-evoked currents.

### 2. GluN3A is a molecular brake on synapse maturation and a driver of spine pruning (F002)

The principal developmental function of GluN3A is to restrain the maturation of excitatory synapses and to promote the elimination of dendritic spines. Das et al. (1998) found that genetic knockout of NR3A "results in enhanced NMDA responses and increased dendritic spines in early postnatal cerebrocortical neurons," showing that GluN3A normally limits spine formation [PMID: 9620802](https://pubmed.ncbi.nlm.nih.gov/9620802/). Gain-of-function experiments confirmed the direction of effect: Kehoe et al. (2014) demonstrated that "overexpressing GluN3A reduced spine density over time, increased spine elimination, and decreased spine stability" [PMID: 25009255](https://pubmed.ncbi.nlm.nih.gov/25009255/).

An authoritative review (Pérez-Otaño et al., 2016) frames this role in circuit terms: GluN3-containing NMDARs "seem to have important roles in delaying synapse maturation until the arrival of sensory experience and in targeting non-used synapses for pruning" [PMID: 27558536](https://pubmed.ncbi.nlm.nih.gov/27558536/). GluN3A thus functions as a developmental gate — holding synapses in an immature, plastic state until experience selects which connections to keep.

### 3. GluN1/GluN3A assemblies are glutamate-independent excitatory glycine receptors (F003)

Because GluN3A binds glycine rather than glutamate, GluN1/GluN3A receptors are gated by glycine alone. Mesic et al. (2016) showed that "NMDA receptors composed of glycine-binding GluN1 and GluN3 subunits function as excitatory glycine receptors," and defined the mechanism: "Binding of glycine to the high-affinity GluN3 subunits triggers channel opening, whereas glycine binding to the low-affinity GluN1 subunits causes an auto-inhibition of the maximal glycine-inducible receptor current" [PMID: 26777280](https://pubmed.ncbi.nlm.nih.gov/26777280/). The GluN3A N-terminal domain determines agonist efficacy, which is why GluN1-selective antagonists can potentiate the response (by relieving GluN1-mediated auto-inhibition).

This is a striking exception within the NMDAR family: a channel that requires no glutamate and is activated by an amino acid (glycine) usually associated with inhibitory neurotransmission. Triheteromeric GluN1/GluN2/GluN3A receptors also exist at specific cortical inputs, blending features of glutamate-activated and glycine-activated receptors (Pilli & Kumar, 2012) [PMID: 22814002](https://pubmed.ncbi.nlm.nih.gov/22814002/).

### 4. Surface expression is controlled by AP2/clathrin endocytosis via a YWL motif (F004)

GluN3A surface levels are dynamically regulated by endocytosis. Chowdhury et al. (2013) defined "a novel endocytic motif (YWL), which is located within the cytoplasmic C-terminal tail of GluN3A and mediates its binding to the clathrin adaptor AP2" [PMID: 23447623](https://pubmed.ncbi.nlm.nih.gov/23447623/). Mutating the motif to alanine inhibits internalization and accumulates surface GluN3A, whereas phosphorylation of the motif's tyrosine by **Src-family kinases** promotes internalization: "the tyrosine residue is phosphorylated by Src family kinases, and that Src-activation limits surface GluN3A expression" [PMID: 23447623](https://pubmed.ncbi.nlm.nih.gov/23447623/).

A second adaptor, PACSIN1, is required for endogenous GluN3A endocytosis; silencing PACSIN1 blocks GluN3A internalization and enhances spine pruning, mimicking GluN3A overexpression (Kehoe et al., 2014) [PMID: 25009255](https://pubmed.ncbi.nlm.nih.gov/25009255/). Trafficking is therefore the master switch that converts GluN3A abundance into functional output at the synapse.

### 5. GluN3A constrains adult LTP, is neuroprotective, and is disease-linked (F005, F007)

GluN3A expression peaks neonatally and declines in adulthood. This developmental profile matters: when GluN3A is removed, adult plasticity is unleashed. Mohamad et al. (2013) found that "Hippocampal slices from juvenile and adult GluN3A KO mice showed greater long-term potentiation (LTP) compared with WT slices. GluN3A deletion resulted in increased expression of Ca²⁺/calmodulin-dependent kinase II (CaMKII)," with CaMKII inhibition abolishing the enhanced LTP [PMID: 23006484](https://pubmed.ncbi.nlm.nih.gov/23006484/). GluN3A thus restrains LTP via a CaMKII-dependent mechanism, and its KO also alters locomotion, pain perception, and learning/memory.

In adults, residual GluN3A is neuroprotective. Lee et al. (2015) showed that after focal cerebral ischemia "the infarction volume... was significantly larger in GluN3A KO mice compared with WT mice" [PMID: 25652449](https://pubmed.ncbi.nlm.nih.gov/25652449/) — consistent with GluN3A dampening Ca²⁺-driven excitotoxicity. The flip side is disease risk from mis-timed expression: GluN3A-containing NMDARs "regulate synapse pruning and excitotoxicity, and are associated with schizophrenia, autism and stroke" (Kim et al., 2026) [PMID: 42665662](https://pubmed.ncbi.nlm.nih.gov/42665662/), and "reactivation of GluN3A expression at inappropriate ages may underlie maladaptive synaptic rearrangements observed in addiction, neurodegenerative diseases and other major brain disorders" [PMID: 27558536](https://pubmed.ncbi.nlm.nih.gov/27558536/).

### 6. Cryo-EM defines GluN1-GluN3A as a glycine-gated diheteromer (F006)

Structural biology has now resolved the native architecture and gating mechanism. Kim et al. (2026, Gouaux lab) used single-molecule pull-down to show that "native GluN3A-containing receptors are diheteromeric assemblies," and solved cryo-EM structures in antagonist-bound, preactive, active, and desensitized states [PMID: 42665662](https://pubmed.ncbi.nlm.nih.gov/42665662/). The key mechanistic result: "glycine activates the receptor solely via GluN3A-dependent conformational changes, opening the gate with two-fold symmetry," followed by a roughly four-fold symmetric desensitized state. The GluN1-selective antagonist CGP-78608 restricts GluN3A rotation, blocking desensitization and potentiating activity — a structural rationale for allosteric control. A companion study reported the native architecture, allosteric modulation, and gating mechanism of these glycine-dependent receptors [PMID: 42039402](https://pubmed.ncbi.nlm.nih.gov/42039402/).

### 7. GluN3A binds glycine/D-serine at the co-agonist site, not glutamate (F008)

GluN3A's ligand specificity is a defining, evolutionarily conserved feature. Stroebel, Mony & Paoletti (2021) note that "five out of the eighteen vertebrate iGluR subunits do not bind glutamate but glycine... This is the case of GluN1, GluN3A, GluN3B, GluD1 and GluD2 subunits, all also binding the D amino acid d-serine" [PMID: 34058193](https://pubmed.ncbi.nlm.nih.gov/34058193/). On conventional GluN1/GluN2 NMDARs, glycine/D-serine is a mandatory co-agonist; on unconventional GluN1/GluN3 NMDARs, "glycine acts as the sole agonist directly triggering opening of excitatory glycinergic channels recently shown to be physiologically relevant" [PMID: 34058193](https://pubmed.ncbi.nlm.nih.gov/34058193/). This matches the UniProt Q8TCU5 domain annotation (ANF/ligand-binding IPR001828; Glu/Gly-binding IPR019594). The development of a GluN3-selective positive allosteric modulator, UCM-A86, confirms GluN1/GluN3 receptors have distinct roles in neuronal development and synapse maturation (Benton et al., 2026) [PMID: 41740201](https://pubmed.ncbi.nlm.nih.gov/41740201/).

### 8. Membrane topology and the intracellular C-terminal tail (F009)

GluN3A is an integral postsynaptic membrane protein with extracellular ligand-binding domains and an intracellular C-terminal tail that governs its trafficking and signaling. Tahiri, Corti & Duarte (2025) describe that NMDAR subunits including GluN3A "share a similar structure and membrane topology, with an intracellular C-terminus tail responsible for the interaction with proteins important for the trafficking of the receptors, and to control their surface distribution and signalling activity" [PMID: 40029461](https://pubmed.ncbi.nlm.nih.gov/40029461/). This tail carries most of the post-translational modification sites: "These modifications, including phosphorylation, ubiquitination, and palmitoylation, regulate interactions with intracellular proteins" [PMID: 40029461](https://pubmed.ncbi.nlm.nih.gov/40029461/). The extracellular domains are additionally essential for ER processing/assembly of NMDARs (Horak et al., 2021) [PMID: 33796003](https://pubmed.ncbi.nlm.nih.gov/33796003/). The YWL endocytic motif characterized in finding 4 lies within this same cytoplasmic C-terminal tail.

### 9. GluN3A inhibits spine maturation through the GIT1/βPIX/Rac1/PAK pathway (F010)

The molecular mechanism linking GluN3A to spine pruning was defined by Fiuza, González-González & Pérez-Otaño (2013, *J. Cell Biol.*). "GluN3A binds G protein-coupled receptor kinase-interacting protein (GIT1), a postsynaptic scaffold that assembles actin regulatory complexes, including the Rac1 guanine nucleotide exchange factor βPIX, to promote Rac1 activation in spines. Binding to GluN3A limits the synaptic localization of GIT1 and its ability to complex βPIX, leading to decreased Rac1 activation and reduced spine density and size" [PMID: 24297929](https://pubmed.ncbi.nlm.nih.gov/24297929/). Deleting GluN3A has the opposite effect — it favors GIT1/βPIX complex formation and increases activation of Rac1 and its effector PAK (p21-activated kinase).

Critically, "binding of GluN3A to GIT1 is regulated by synaptic activity, a response that might restrict the negative regulatory effects of GluN3A on actin signaling to inactive synapses" [PMID: 24297929](https://pubmed.ncbi.nlm.nih.gov/24297929/). This provides the mechanistic basis for selective pruning of under-used synapses: active synapses release GluN3A's grip on GIT1, allowing Rac1-driven spine growth, while inactive synapses remain braked and are eliminated.

---

## Mechanistic Model / Interpretation

GluN3A is best understood as a **developmental timer and synapse-selection device** rather than a conventional neurotransmitter receptor. Its unusual ligand specificity (glycine/D-serine, not glutamate) and its dominant-negative biophysics converge on one outcome: suppression of the Ca²⁺-dependent signaling that normally strengthens and stabilizes excitatory synapses. Its intracellular tail then couples this receptor-level inhibition to the actin cytoskeleton via GIT1.

### Two receptor assemblies, two functions

| Assembly | Ligand / gating | Biophysics | Functional consequence |
|---|---|---|---|
| **GluN1/GluN2/GluN3A** (triheteromer) | Glutamate (GluN2) + glycine (GluN1/GluN3A) | ↓ unitary conductance, ↓ Ca²⁺ permeability, ↓ Mg²⁺ block | Dominant-negative brake on conventional NMDAR signaling |
| **GluN1/GluN3A** (diheteromer) | Glycine alone (sole agonist at GluN3A) | Excitatory glycinergic current; low Ca²⁺ | Glutamate-independent excitatory glycine receptor |

### Signaling pathway for spine pruning

```
   Inactive synapse                          Active synapse
   ----------------                          --------------
   GluN3A ── binds ──► GIT1                   synaptic activity
        (sequesters scaffold)                 releases GIT1 from GluN3A
            │                                       │
            ▼                                       ▼
   GIT1 cannot complex βPIX              GIT1 + βPIX complex forms
            │                                       │
            ▼                                       ▼
   ↓ Rac1-GTP  ──►  ↓ PAK                 ↑ Rac1-GTP ──► ↑ PAK
            │                                       │
            ▼                                       ▼
   ↓ actin polymerization                 ↑ actin polymerization
   spine shrinks / pruned                 spine grows / stabilized
```

### Trafficking control sets the dose

```
 Surface GluN3A  ◄── recycling ───┐
      │                           │
      │ YWL motif binds AP2       │
      │ (Src phosphorylates Tyr;  │
      │  PACSIN1 required)        │
      ▼                           │
 clathrin-mediated endocytosis ───┘
      │
      ▼
 ↓ Surface GluN3A  →  less braking  →  synapse matures
```

### Developmental trajectory

GluN3A expression is high neonatally and declines with maturation. During the peak window, GluN3A keeps nascent synapses immature and plastic, allowing sensory experience to select which connections persist; non-used synapses are pruned via the GIT1/Rac1 pathway. As GluN3A is removed (by transcriptional down-regulation and endocytosis), the brake lifts: Ca²⁺-permeable GluN2-NMDARs dominate, CaMKII signaling rises, LTP matures, and synapses stabilize. Pathological **re-expression** of GluN3A in the adult re-imposes the brake at the wrong time, producing maladaptive synapse loss implicated in schizophrenia, autism, addiction, neurodegeneration, and (through altered excitotoxicity thresholds) stroke outcomes.

---

## Evidence Base

| PMID | Study (year) | Contribution | Supports |
|---|---|---|---|
| [9620802](https://pubmed.ncbi.nlm.nih.gov/9620802/) | Das et al., *Nature* (1998) | NR3A co-IPs with NR1/NR2; ↓ unitary conductance; KO ↑ NMDA responses & spines | F001, F002 |
| [23447623](https://pubmed.ncbi.nlm.nih.gov/23447623/) | Chowdhury et al. (2013) | Low Ca²⁺/Mg²⁺ properties; YWL/AP2 endocytosis; Src regulation | F001, F004, F009 |
| [25009255](https://pubmed.ncbi.nlm.nih.gov/25009255/) | Kehoe et al. (2014) | GluN3A overexpression drives spine pruning; PACSIN1 required | F002, F004 |
| [27558536](https://pubmed.ncbi.nlm.nih.gov/27558536/) | Pérez-Otaño et al., review (2016) | Synapse-maturation delay, pruning of non-used synapses; disease reactivation | F002, F005, F007 |
| [26777280](https://pubmed.ncbi.nlm.nih.gov/26777280/) | Mesic et al. (2016) | GluN1/GluN3 = excitatory glycine receptors; GluN3 high-affinity activation | F003 |
| [22814002](https://pubmed.ncbi.nlm.nih.gov/22814002/) | Pilli & Kumar (2012) | Triheteromeric GluN1/GluN2/GluN3A at specific cortical inputs | F003 |
| [23006484](https://pubmed.ncbi.nlm.nih.gov/23006484/) | Mohamad et al. (2013) | KO ↑ LTP via CaMKII; behavioral roles | F005 |
| [25652449](https://pubmed.ncbi.nlm.nih.gov/25652449/) | Lee et al. (2015) | KO ↑ infarct volume → GluN3A neuroprotective | F005 |
| [42665662](https://pubmed.ncbi.nlm.nih.gov/42665662/) | Kim et al. (2026) | Native diheteromer; glycine gates solely via GluN3A; allosteric modulation; disease links | F006, F007 |
| [42039402](https://pubmed.ncbi.nlm.nih.gov/42039402/) | (2026) | Native architecture, allosteric modulation, gating of glycine-dependent NMDARs | F006 |
| [34058193](https://pubmed.ncbi.nlm.nih.gov/34058193/) | Stroebel, Mony & Paoletti, review (2021) | GluN3A binds glycine/D-serine, not glutamate; glycinergic channels physiological | F008 |
| [41740201](https://pubmed.ncbi.nlm.nih.gov/41740201/) | Benton et al. (2026) | UCM-A86 selective PAM confirms distinct GluN1/GluN3 roles | F008 |
| [40029461](https://pubmed.ncbi.nlm.nih.gov/40029461/) | Tahiri, Corti & Duarte, review (2025) | Membrane topology; C-tail PTMs control trafficking/signaling | F009 |
| [33796003](https://pubmed.ncbi.nlm.nih.gov/33796003/) | Horak et al. (2021) | Extracellular domains essential for ER processing/assembly | F009 |
| [24297929](https://pubmed.ncbi.nlm.nih.gov/24297929/) | Fiuza, González-González & Pérez-Otaño, *JCB* (2013) | GluN3A→GIT1 sequestration→↓βPIX/Rac1/PAK; activity-dependent | F010 |

The evidence base is strong and internally consistent. Loss-of-function (KO) and gain-of-function (overexpression) experiments point in opposite directions as expected, and the structural (cryo-EM), biochemical (co-IP, pull-down), electrophysiological (single-channel, oocyte, slice LTP), and cell-biological (spine imaging, endocytosis assays) lines of evidence converge on the same model. The 2026 cryo-EM work directly confirms the long-inferred mechanism that glycine gates the receptor through GluN3A.

---

## Localization Summary

- **Primary site of function:** neuronal **postsynaptic membrane** of excitatory synapses (dendritic spines), predominantly in forebrain/cortex and hippocampus.
- **Topology:** integral membrane protein with a large extracellular N-terminal and ligand-binding region, a transmembrane ion-channel domain, and an **intracellular C-terminal tail** that mediates trafficking and signaling (GIT1 binding, AP2 endocytosis, PTM sites).
- **Subcellular dynamics:** cycles between the surface and intracellular compartments via clathrin/AP2 endocytosis (YWL motif); assembly and ER export depend on the extracellular domains.
- **Temporal:** surface/expression levels peak during early postnatal development and decline with maturation.

---

## Limitations and Knowledge Gaps

1. **Species of evidence.** Much mechanistic data (KO mice, oocyte and slice electrophysiology, spine imaging) derives from rodent models. The human protein (Q8TCU5) is highly conserved and the cryo-EM/pharmacology work increasingly uses human or human-like constructs, but direct human cell-physiology data remain comparatively sparse.
2. **Triheteromer stoichiometry and prevalence.** The abundance, exact stoichiometry (one vs. two GluN3A copies), and regional distribution of native GluN1/GluN2/GluN3A triheteromers versus GluN1/GluN3A diheteromers in the human brain are incompletely quantified.
3. **In vivo glycinergic signaling.** The physiological triggers and circuits in which GluN1/GluN3A excitatory glycine receptors fire endogenously — including the source of activating glycine/D-serine and its regulation — are still being mapped.
4. **Disease causality.** Associations with schizophrenia, autism, addiction, neurodegeneration, and stroke are mechanistically plausible and partly genetic, but causal human genetic variants in GRIN3A with defined molecular consequences are less established than for GRIN2A/GRIN2B.
5. **PTM-specific roles.** While phosphorylation, ubiquitination, and palmitoylation of the C-tail are documented as a class, the site-specific functional consequences for GluN3A trafficking and GIT1 engagement are not fully resolved.
6. **D-serine vs. glycine.** The relative contributions of glycine and D-serine as endogenous agonists at native GluN3A receptors, and their spatiotemporal availability, remain to be clarified.

---

## Proposed Follow-up Experiments / Actions

1. **Quantify native stoichiometry in human tissue.** Apply single-molecule pull-down (as in Kim et al., 2026) to human post-mortem cortex/hippocampus to measure the ratio of GluN1/GluN3A diheteromers to GluN1/GluN2/GluN3A triheteromers across development.
2. **Define endogenous glycinergic currents in vivo.** Use GluN3-selective tools (positive allosteric modulator UCM-A86; GluN1-selective antagonist CGP-78608) to isolate and characterize GluN1/GluN3A-mediated currents in defined circuits, identifying the source and regulation of the activating agonist.
3. **Dissect the GIT1 interaction interface.** Map the GluN3A C-tail residues that bind GIT1 and generate separation-of-function mutants that disrupt GIT1 binding without affecting channel gating or endocytosis, to isolate the spine-pruning signal from the biophysical brake.
4. **Site-specific PTM mapping.** Use quantitative proteomics to define developmental changes in GluN3A C-tail phosphorylation/ubiquitination/palmitoylation and test their causal roles in trafficking and GIT1 engagement.
5. **Human disease modeling.** Introduce GRIN3A variants (and controlled re-expression) into human iPSC-derived neurons/organoids to test whether mis-timed GluN3A drives measurable spine loss and circuit dysfunction relevant to schizophrenia/autism.
6. **Therapeutic window for stroke.** Given GluN3A's neuroprotective role against excitotoxicity, test whether transient, acute enhancement of GluN3A function or GluN3A-receptor activity reduces infarct volume in adult models without impairing plasticity.

---

## Conclusion

GRIN3A encodes **GluN3A**, a glycine/D-serine–binding (not glutamate-binding) NMDA receptor subunit that functions at the neuronal postsynaptic membrane as an **inhibitory developmental brake**. By reducing NMDAR conductance, Ca²⁺ permeability, and Mg²⁺ block in GluN1/GluN2/GluN3A triheteromers — and by forming glutamate-independent excitatory glycine receptors as GluN1/GluN3A diheteromers — GluN3A times excitatory synapse maturation and drives activity-dependent spine pruning, chiefly by sequestering the GIT1 scaffold to suppress βPIX→Rac1→PAK actin signaling. Its surface level is set by AP2/Src/PACSIN1-mediated endocytosis, and its developmentally programmed removal permits synapse strengthening and adult plasticity, whereas mis-timed GluN3A expression is linked to schizophrenia, autism, addiction, neurodegeneration, and stroke.


## Artifacts

- [OpenScientist final report](GRIN3A-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](GRIN3A-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:9620802
2. PMID:23447623
3. PMID:25009255
4. PMID:27558536
5. PMID:26777280
6. PMID:22814002
7. PMID:23006484
8. PMID:25652449
9. PMID:42665662
10. PMID:42039402
11. PMID:34058193
12. PMID:41740201
13. PMID:40029461
14. PMID:33796003
15. PMID:24297929