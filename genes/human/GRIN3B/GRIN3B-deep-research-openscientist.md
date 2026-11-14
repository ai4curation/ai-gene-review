---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-14T20:26:17.879382'
end_time: '2026-11-14T20:38:32.339125'
duration_seconds: 734.46
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: GRIN3B
  gene_symbol: GRIN3B
  uniprot_accession: O60391
  protein_description: 'RecName: Full=Glutamate receptor ionotropic, NMDA 3B {ECO:0000305};
    Short=GluN3B; AltName: Full=N-methyl-D-aspartate receptor subtype 3B; Short=NMDAR3B;
    Short=NR3B {ECO:0000303|PubMed:11735224}; Flags: Precursor;'
  gene_info: Name=GRIN3B {ECO:0000312|HGNC:HGNC:16768};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the glutamate-gated ion channel (TC 1.A.10.1)
  protein_domains: Glu/Gly-bd. (IPR019594); Iono_Glu_rcpt_met. (IPR001508); Ionotropic_Glu_rcpt.
    (IPR015683); Iontro_rcpt_C. (IPR001320); Peripla_BP_I. (IPR028082)
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
citation_count: 16
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: GRIN3B-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: GRIN3B-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** O60391
- **Protein Description:** RecName: Full=Glutamate receptor ionotropic, NMDA 3B {ECO:0000305}; Short=GluN3B; AltName: Full=N-methyl-D-aspartate receptor subtype 3B; Short=NMDAR3B; Short=NR3B {ECO:0000303|PubMed:11735224}; Flags: Precursor;
- **Gene Information:** Name=GRIN3B {ECO:0000312|HGNC:HGNC:16768};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the glutamate-gated ion channel (TC 1.A.10.1)
- **Key Domains:** Glu/Gly-bd. (IPR019594); Iono_Glu_rcpt_met. (IPR001508); Ionotropic_Glu_rcpt. (IPR015683); Iontro_rcpt_C. (IPR001320); Peripla_BP_I. (IPR028082)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GRIN3B" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GRIN3B' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GRIN3B** (gene ID: GRIN3B, UniProt: O60391) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# GRIN3B / GluN3B (NR3B): Functional Annotation Report

**UniProt:** O60391 | **Gene:** GRIN3B (HGNC:16768) | **Organism:** *Homo sapiens* | **Protein family:** Glutamate-gated ion channel (TC 1.A.10.1)

---

## Summary

**GRIN3B encodes GluN3B (also called NR3B or NMDAR3B), a glycine-/D-serine–binding, non-pore-forming modulatory subunit of the N-methyl-D-aspartate (NMDA) subfamily of ionotropic glutamate receptors.** The gene symbol, organism, protein family, and domain architecture all match the UniProt target: molecular cloning identified a 1003-amino-acid protein with a signal peptide, four membrane-associated regions, a conserved glutamate-receptor ligand-binding pocket, and highest sequence similarity (51%) to its paralog GluN3A ([PMID: 11717388](https://pubmed.ncbi.nlm.nih.gov/11717388/); [PMID: 12008020](https://pubmed.ncbi.nlm.nih.gov/12008020/)). The literature is specific and consistent for this exact protein, so no ambiguity or mis-identification problem arises.

The primary function of GluN3B is not to act as an independent ligand-gated channel — it cannot form functional receptors on its own — but to **co-assemble with the obligatory GluN1 subunit (and optionally GluN2) at the neuronal plasma membrane, where it reshapes the ion-conduction properties of the resulting receptor.** GluN3B operates in two modes. (i) Within conventional GluN1/GluN2 NMDA receptors it acts as a **dominant / dominant-negative modulatory subunit**, suppressing glutamate-evoked current, reducing Ca²⁺ permeability, and lowering Mg²⁺ block — an activity proposed to protect motoneurons from glutamate excitotoxicity. (ii) In the absence of GluN2, GluN1/GluN3B diheteromers form unconventional **excitatory glycine receptors** that are activated by glycine alone, are insensitive to glutamate/NMDA, are paradoxically inhibited by D-serine, and are relatively Ca²⁺-impermeable and resistant to Mg²⁺, MK-801, memantine, and competitive antagonists.

GluN3B carries out its function **post-synaptically at the plasma membrane of glutamatergic/glycinergic neurons**, most prominently in **somatic motoneurons of the brainstem and spinal cord**, where it becomes the dominant regulatory NMDAR subunit during early postnatal development (a NR2→NR3B switchover) and contributes to dendrite morphogenesis and motor behavior. In humans the gene is highly polymorphic and bears a common, globally distributed null allele (homozygous in ~10% of European-Americans) that is tolerated and shows **no association with amyotrophic lateral sclerosis (ALS)**, whereas a frameshift variant degrading the glycine-binding domain has been linked to psychotic disorders/schizophrenia.

---

## Gene / Protein Identity Verification

Before describing function, the mandatory identity check was performed and **passed on all counts**:

| Verification criterion | Result |
|---|---|
| Gene symbol "GRIN3B" matches protein description | ✔ Cloned NR3B is the glutamate-receptor NMDA type-3B subunit ([PMID: 11717388](https://pubmed.ncbi.nlm.nih.gov/11717388/)) |
| Organism is *Homo sapiens* | ✔ Human cloning and genetics studies ([PMID: 11717388](https://pubmed.ncbi.nlm.nih.gov/11717388/); [PMID: 17687115](https://pubmed.ncbi.nlm.nih.gov/17687115/)) |
| Protein family/domains align with literature | ✔ Glutamate-receptor family, signal peptide, 4 membrane regions, conserved ligand-binding pocket ([PMID: 11717388](https://pubmed.ncbi.nlm.nih.gov/11717388/)) |
| No confusion with a different same-symbol gene | ✔ Literature is uniformly about the NMDA receptor subunit |

The gene symbol is **not** ambiguous for this target. A rich, specific primary literature exists for human GluN3B and its rodent orthologs, so the report proceeds on firm ground.

---

## Key Findings

### 1. GluN3B is a glycine-binding modulatory subunit of the NMDA receptor family (F001)

Molecular cloning by Nishi and colleagues identified NR3B as a 1003-amino-acid protein (encoded by ≥9 exons) belonging to the glutamate-receptor family. It shares its highest sequence similarity (51%) with the NR3A subunit — hence its name — and displays the canonical architecture of an ionotropic glutamate receptor: a signal peptide, four membrane-associated regions, and a conserved ligand-binding pocket ([PMID: 11717388](https://pubmed.ncbi.nlm.nih.gov/11717388/)). It is one of the two GluN3 subunits (GluN3A and GluN3B), which were the last NMDA receptor subunits to be cloned, roughly 15 years after the rest of the family ([PMID: 22240240](https://pubmed.ncbi.nlm.nih.gov/22240240/)).

> *"This protein showed the highest similarity (51%) to the NR3A subunit of the NMDA receptor and therefore was termed NR3B. NR3B has a structure typical of glutamate receptor family members with a signal peptide and four membrane-associated regions. Amino acids forming a ligand-binding pocket are conserved."* — [PMID: 11717388](https://pubmed.ncbi.nlm.nih.gov/11717388/)

This finding anchors the molecular identity: GluN3B is a bona fide member of the glutamate-gated ion channel family (TC 1.A.10.1), consistent with the UniProt domains (Glu/Gly-binding IPR019594; ionotropic glutamate receptor domains IPR001508, IPR015683, IPR001320; periplasmic binding protein-like fold IPR028082).

### 2. GluN3B acts as a dominant-negative subunit, suppressing GluN1/GluN2 current and reducing Ca²⁺ permeability (F002, F011)

The defining functional property of GluN3B emerged directly from its first heterologous characterization. When co-expressed with NR1 and NR2A in heterologous cells, NR3B suppressed glutamate-induced current in a manner similar to NR3A, establishing that NR3-class subunits act as **dominant-negative subunits** within the NMDA receptor complex ([PMID: 11717388](https://pubmed.ncbi.nlm.nih.gov/11717388/)).

> *"When coexpressed with NR1 and NR2A in heterologous cells, NR3B suppressed glutamate-induced current similarly to NR3A. Thus members of the NR3 class of NMDA receptors act as dominant-negative subunits in the NMDA receptor complex."* — [PMID: 11717388](https://pubmed.ncbi.nlm.nih.gov/11717388/)

This was independently confirmed by Matsuda et al., who cloned NR3B (1003 aa, most closely related to NR3A, with conserved ligand-binding domain, channel pore, and gate) and demonstrated by co-immunoprecipitation that NR3B forms complexes with NR1a and NR2A. Critically, **NR3B expressed alone did not reconstitute functional NMDA receptors**, but its co-expression reduced the Ca²⁺ permeability of glutamate-induced currents in NR1a/NR2A-expressing cells ([PMID: 12008020](https://pubmed.ncbi.nlm.nih.gov/12008020/)).

> *"coexpression of NR3B reduced the Ca(2+) permeability of glutamate-induced currents in cells expressing NR1a and NR2A. These results indicate that NR3B is a dominant modulatory subunit that can modify the function of NMDA receptors."* — [PMID: 12008020](https://pubmed.ncbi.nlm.nih.gov/12008020/)

The reduction of Ca²⁺ permeability is a general property of NR3 subunits ([PMID: 18425811](https://pubmed.ncbi.nlm.nih.gov/18425811/)). Functionally, this translates into protection against Ca²⁺-mediated toxicity: co-expression of NR3A and NR3B inhibited NMDA-evoked rises in intracellular and mitochondrial Ca²⁺ and reduced cell death in HEK293 cells ([PMID: 20813147](https://pubmed.ncbi.nlm.nih.gov/20813147/)).

### 3. GluN1/GluN3 assemble into excitatory glycine receptors activated solely by glycine (F003, F007, F008)

In the absence of GluN2, GluN3 subunits assemble with GluN1 into **excitatory glycine receptors** ([PMID: 22240240](https://pubmed.ncbi.nlm.nih.gov/22240240/)). The seminal demonstration came from Chatterton et al., who cloned NR3B and showed that co-expression with NR1 in *Xenopus* oocytes yields receptors that are **unaffected by glutamate or NMDA and are inhibited by D-serine** — a striking inversion of conventional NMDAR pharmacology, where D-serine is a co-agonist. These NR1/NR3 channels form **relatively Ca²⁺-impermeable cation channels resistant to Mg²⁺, MK-801, memantine, and competitive antagonists** ([PMID: 11823786](https://pubmed.ncbi.nlm.nih.gov/11823786/)).

> *"NR3A or NR3B co-assembles with NR1 to form excitatory glycine receptors that are unaffected by glutamate or NMDA, and inhibited by D-serine... NR1/NR3A or -3B receptors form relatively Ca2+-impermeable cation channels that are resistant to Mg2+, MK-801, memantine and competitive antagonists."* — [PMID: 11823786](https://pubmed.ncbi.nlm.nih.gov/11823786/)

Pharmacological dissection by Smothers & Woodward confirmed the distinctive profile in HEK293 cells: glycine-activated NR1/NR3A/NR3B receptors were not stimulated by glutamate or kainate and were resistant to Mg²⁺ block and to D-APV, ifenprodil, memantine, and MK-801. D-serine partially activated them, 5,7-dichlorokynurenic acid inhibited them, and the glycine-site ligands 7-chlorokynurenic acid and the partial agonist HA-966 potentiated glycine-stimulated currents; ethanol and toluene produced modest (~10–21%) inhibition ([PMID: 17502428](https://pubmed.ncbi.nlm.nih.gov/17502428/)).

> *"These glycine-activated receptors were not stimulated by glutamate or kainic acid and were resistant to magnesium block."* — [PMID: 17502428](https://pubmed.ncbi.nlm.nih.gov/17502428/)

Recent reviews and cryo-EM structural work reinforce this model for the GluN3 family: unlike conventional GluN1-N2 receptors that require both glycine and glutamate, GluN1-N3 receptors are activated solely by glycine, display faster desensitization and reduced Ca²⁺ permeability, and gate via GluN3-dependent conformational changes ([PMID: 40235311](https://pubmed.ncbi.nlm.nih.gov/40235311/); [PMID: 42665662](https://pubmed.ncbi.nlm.nih.gov/42665662/)).

### 4. Crystallography defines a unique glycine-/D-serine-binding ligand-binding domain (F006)

The structural basis of ligand recognition was established by Yao et al. Using ligand-binding assays, X-ray crystallography, and all-atom molecular dynamics simulations, they showed that the ligand-binding domains (LBDs) of both NR3A and NR3B **bind glycine and D-serine** — the candidate neurotransmitters/co-agonists for NR3-containing receptors. The NR3 LBDs adopt a degree of domain closure similar to the NR1 LBD but possess a **unique loop 1 structure distinct from all other glutamate receptor ion channels**, along with distinct hydrogen-bonding and solvent networks, and they fail to undergo the partial-agonist (ACPC) rearrangement seen in NR1 ([PMID: 18636091](https://pubmed.ncbi.nlm.nih.gov/18636091/)).

> *"we investigate mechanisms underlying the binding by NR3A and NR3B of glycine and D-serine... The ligand binding domains of both NR3 subunits adopt a similar extent of domain closure as found in the corresponding NR1 complexes, but have a unique loop 1 structure distinct from that in all other glutamate receptor ion channels."* — [PMID: 18636091](https://pubmed.ncbi.nlm.nih.gov/18636091/)

This provides direct, atomic-resolution evidence that GluN3B is a **glycine-binding** subunit, consistent with the UniProt Glu/Gly-binding domain annotation (IPR019594) and explaining the glycine-gated behavior of GluN1/GluN3B receptors.

### 5. Fixed triheteromeric stoichiometry and trafficking control (F009)

Single-molecule fluorescence colocalization studies by Ulbrich & Isacoff revealed assembly rules. In *Xenopus* oocytes, NR1, NR2, and NR3 follow an "exclusion rule" yielding separate NR1/NR2 and NR1/NR3 receptor populations. However, co-expression of NR1, NR3A, and NR3B produces **triheteromeric receptors with a fixed stoichiometry of two NR1 subunits plus one NR3A and one NR3B**; at least part of this stoichiometric regulation is enforced by **internal (intracellular) retention** ([PMID: 18779583](https://pubmed.ncbi.nlm.nih.gov/18779583/)).

> *"coexpression of NR1, NR3A, and NR3B yields triheteromeric receptors with a fixed stoichiometry of two NR1 subunits with one NR3A and one NR3B. At least part of this regulation of subunit stoichiometry appears to be caused by internal retention."* — [PMID: 18779583](https://pubmed.ncbi.nlm.nih.gov/18779583/)

This establishes that GluN3B's surface expression and incorporation are tightly quality-controlled, and that it can occupy a specific, non-interchangeable position within mixed GluN3A/GluN3B receptors.

### 6. Localization: a plasma-membrane subunit enriched in somatic motoneurons with developmental switchover (F004, F011)

GluN3B is a plasma-membrane NMDAR subunit with a distinctive expression footprint. Its mRNA is concentrated in **somatic motoneurons of the brainstem and spinal cord**, with high levels in pons, midbrain, medulla, and spinal cord and low levels in forebrain and cerebellum ([PMID: 11717388](https://pubmed.ncbi.nlm.nih.gov/11717388/); [PMID: 12008020](https://pubmed.ncbi.nlm.nih.gov/12008020/)).

> *"NR3B shows very restricted expression in somatic motoneurons of the brainstem and spinal cord."* — [PMID: 11717388](https://pubmed.ncbi.nlm.nih.gov/11717388/)

Developmentally, NR3B mRNA first appears in mouse motoneurons at P10–P14 and peaks by P21/adulthood, reciprocal to the declining NR2A subunit — defining a **NR2→NR3B switchover** in early postnatal motoneurons ([PMID: 15813953](https://pubmed.ncbi.nlm.nih.gov/15813953/)). Unlike NR3A, which declines after the second postnatal week, NR3B remains constant into adulthood ([PMID: 12008020](https://pubmed.ncbi.nlm.nih.gov/12008020/)). At the protein level, immunolabeling shows broader distribution — hippocampus, cerebral cortex, striatum (caudoputamen, nucleus accumbens), cerebellum, and spinal motoneurons — co-distributing with the obligatory NR1 subunit ([PMID: 18425811](https://pubmed.ncbi.nlm.nih.gov/18425811/)).

> *"the major regulatory subunit of NMDA receptors is likely to switch from NR2 to NR3B in somatic motoneurons during the early postnatal period"* — [PMID: 15813953](https://pubmed.ncbi.nlm.nih.gov/15813953/)

### 7. Physiological roles and human genetics (F005, F010)

GluN3B shapes neuronal structure and behavior. Over-expression of NR3B in cultured rat spinal motor neurons increased dendritic arbor length and complexity and the number of dendritic filopodia, implicating it in **dendrite morphogenesis** ([PMID: 18541382](https://pubmed.ncbi.nlm.nih.gov/18541382/)). NR3B-knockout mice are viable and fertile but display impaired motor learning/coordination and altered social behavior ([PMID: 17880385](https://pubmed.ncbi.nlm.nih.gov/17880385/)).

In humans, GRIN3B is highly polymorphic. Niemann et al. found that **~10% of the normal European-American population lacks NR3B** due to homozygous occurrence of a null allele ([PMID: 17880385](https://pubmed.ncbi.nlm.nih.gov/17880385/)). Sequencing the 3.1 kb coding region in familial and sporadic ALS and controls identified 32 SNPs plus a 4-bp insertion (insCGTT) that truncates the protein near its amino terminus, creating a null allele with global frequency 0–0.38; **no variants were found that cause or modify ALS** ([PMID: 17687115](https://pubmed.ncbi.nlm.nih.gov/17687115/)). This same study restates the mechanistic rationale: NR3B reduces the receptor's Ca²⁺-permeability and overall current and may thereby protect motoneurons against glutamate-mediated excitotoxicity.

> *"NR3B reduces the Ca(2+)-permeability as well as the overall current of the receptor response and may thereby protect motoneurons against glutamate-mediated excitotoxicity."* — [PMID: 17687115](https://pubmed.ncbi.nlm.nih.gov/17687115/)

By contrast, a frameshift variant (rs10666583) that **degrades the S1/S2 glycine-binding domain** and alters channel-pore permeability segregated with psychotic disorders in a family and was enriched in psychosis patients, linking GluN3B glycine-binding to schizophrenia risk ([PMID: 28132660](https://pubmed.ncbi.nlm.nih.gov/28132660/)).

> *"The amino acid shift degrades the S1/S2 glycine binding domain of the dominant modulatory GluN3B subunit of the NMDA receptor, which subsequently affects the permeability of the channel pore"* — [PMID: 28132660](https://pubmed.ncbi.nlm.nih.gov/28132660/)

---

## Mechanistic Model / Interpretation

GluN3B is best understood as a **conditional modulator of excitatory ion flux** whose effect depends on its assembly partners. It is not an autonomous channel; it requires the obligatory GluN1 subunit, and its physiology bifurcates according to whether GluN2 is present.

```
                         GRIN3B → GluN3B (NR3B) protein
                                   │
                 (cannot form functional channel alone;
                  ER/intracellular retention gates surface delivery)
                                   │
            ┌──────────────────────┴──────────────────────┐
            │                                              │
   WITH GluN1 + GluN2                              WITH GluN1 ONLY
   (triheteromer)                                  (diheteromer)
            │                                              │
  Dominant / dominant-negative                 Excitatory GLYCINE receptor
  modulatory subunit:                          - activated by glycine ALONE
   - suppresses glutamate current              - glutamate / NMDA INSENSITIVE
   - ↓ Ca²⁺ permeability                        - INHIBITED by D-serine
   - ↓ Mg²⁺ block                               - Ca²⁺-impermeable
   - limits excitotoxic Ca²⁺ influx            - Mg²⁺ / MK-801 / memantine resistant
            │                                              │
            └──────────────────────┬──────────────────────┘
                                   │
                  Ligand recognized: GLYCINE and D-SERINE
                  via a structurally unique S1/S2 LBD
                  (NR1-like domain closure, unique loop 1)
                                   │
         Post-synaptic plasma membrane of neurons; enriched in
         brainstem/spinal SOMATIC MOTONEURONS (NR2→NR3B switchover),
         plus hippocampus, cortex, striatum, cerebellum
```

**Where it acts:** GluN3B functions at the **post-synaptic plasma membrane** of central neurons in glutamatergic (and, in the diheteromeric mode, glycinergic) signaling. Its most prominent and functionally characterized niche is the **somatic motoneuron**, where it becomes the dominant regulatory subunit after the first two postnatal weeks.

**What it does mechanistically:** Through its glycine-/D-serine-binding S1/S2 LBD, GluN3B is recruited into NMDAR complexes where it tunes the biophysics of the pore. In GluN1/GluN2 receptors it dampens the signature high-Ca²⁺-permeability, Mg²⁺-sensitive conductance of conventional NMDARs, which is consistent with a proposed **neuroprotective, anti-excitotoxic** role in motoneurons (a cell type highly vulnerable to glutamate toxicity). In GluN1-only receptors it converts the complex into a cation channel driven by glycine rather than glutamate, opening a non-canonical excitatory pathway whose physiological ligand and native prevalence remain areas of active research.

**Pathway context:** GluN3B sits within glutamatergic excitatory synaptic transmission, acting as a **rheostat on NMDAR-mediated Ca²⁺ signaling** rather than as a primary charge carrier. This places it upstream of the Ca²⁺-dependent signaling cascades (synaptic plasticity, excitotoxic cell-death pathways) that conventional NMDARs trigger — it attenuates them. Its fixed triheteromeric stoichiometry with GluN3A and its intracellular-retention-based trafficking indicate that cells tightly regulate how much GluN3B reaches the surface, giving it a gatekeeping influence over NMDAR signaling strength.

### Comparison of receptor modes

| Property | GluN1/GluN2 (conventional) | GluN1/GluN2/GluN3B (triheteromer) | GluN1/GluN3B (diheteromer) |
|---|---|---|---|
| Primary agonist(s) | Glutamate + glycine/D-serine | Glutamate + glycine (attenuated) | **Glycine alone** |
| Glutamate sensitivity | Required | Required (reduced current) | **Insensitive** |
| Effect of D-serine | Co-agonist (potentiates) | Co-agonist | **Inhibits** |
| Ca²⁺ permeability | High | Reduced | Low / impermeable |
| Mg²⁺ block | Strong | Reduced | Resistant |
| MK-801 / memantine | Blocked | — | Resistant |
| Role of GluN3B | — | Dominant-negative modulator | Core pore-forming partner |

---

## Evidence Base

| PMID | Paper (abbreviated) | Contribution |
|---|---|---|
| [11717388](https://pubmed.ncbi.nlm.nih.gov/11717388/) | *Motoneuron-specific expression of NR3B... dominant-negative manner* (Nishi et al. 2001) | Molecular cloning; identity (1003 aa, 51% to NR3A); dominant-negative function; motoneuron localization |
| [12008020](https://pubmed.ncbi.nlm.nih.gov/12008020/) | *Cloning and characterization of NR3B: a dominant subunit that reduces calcium permeability* (Matsuda et al. 2002) | Independent cloning; Ca²⁺-permeability reduction; cannot form channels alone; co-IP with NR1a/NR2A; brainstem/spinal expression |
| [11823786](https://pubmed.ncbi.nlm.nih.gov/11823786/) | *Excitatory glycine receptors containing the NR3 family* (Chatterton et al. 2002, *Nature*) | Primary discovery of GluN1/GluN3 excitatory glycine receptors; glutamate-insensitive, D-serine-inhibited biophysics; motoneuron predominance |
| [18636091](https://pubmed.ncbi.nlm.nih.gov/18636091/) | *Molecular mechanism of ligand recognition by NR3 subtype* (Yao et al. 2008) | Crystallography: glycine/D-serine binding; unique loop 1 LBD structure |
| [17502428](https://pubmed.ncbi.nlm.nih.gov/17502428/) | *Pharmacological characterization of glycine-activated NR1/NR3 currents* (Smothers & Woodward 2007) | Antagonist-resistance profile; glycine-site pharmacology |
| [18779583](https://pubmed.ncbi.nlm.nih.gov/18779583/) | *Rules of engagement for NMDA receptor subunits* (Ulbrich & Isacoff 2008) | Fixed 2:1:1 triheteromer stoichiometry; intracellular retention |
| [15813953](https://pubmed.ncbi.nlm.nih.gov/15813953/) | *NR2 to NR3B subunit switchover...* (Fukaya et al. 2005) | Developmental NR2→NR3B switch in motoneurons |
| [18425811](https://pubmed.ncbi.nlm.nih.gov/18425811/) | *Immunolocalization of NR3B...* (Wee et al. 2008) | Broader CNS protein distribution; co-localization with NR1; Ca²⁺-permeability reduction |
| [18541382](https://pubmed.ncbi.nlm.nih.gov/18541382/) | *NR3B regulates dendrite morphogenesis* (Prithviraj & Inglis 2008) | Dendritic arbor/filopodia role |
| [17880385](https://pubmed.ncbi.nlm.nih.gov/17880385/) | *Genetic ablation of NR3B in mouse* (Niemann et al. 2007) | KO phenotypes; common human null allele (~10%) |
| [17687115](https://pubmed.ncbi.nlm.nih.gov/17687115/) | *Motoneuron-specific NR3B: no association with ALS* (Niemann et al. 2008) | Polymorphism survey; ALS-negative genetics; anti-excitotoxic rationale |
| [28132660](https://pubmed.ncbi.nlm.nih.gov/28132660/) | *GRIN3B missense mutation as inherited schizophrenia risk* (Hornig et al. 2017) | Glycine-binding-domain frameshift linked to psychosis |
| [20813147](https://pubmed.ncbi.nlm.nih.gov/20813147/) | *Requirement of both NR3A and NR3B for dominant-negative Ca²⁺ effects* (Fukumori et al. 2010) | GluN3B limits NMDAR Ca²⁺ entry and excitotoxic death |
| [22240240](https://pubmed.ncbi.nlm.nih.gov/22240240/) | *GluN3-containing NMDA receptors: not just one-trick ponies* (Pachernegg et al. 2012) | Review: GluN3 identity, excitatory glycine receptor concept |
| [40235311](https://pubmed.ncbi.nlm.nih.gov/40235311/) | *The GluN3-containing NMDA receptors* (Xiong et al. 2025) | Modern review: glycine-only activation, desensitization, low Ca²⁺ |
| [42665662](https://pubmed.ncbi.nlm.nih.gov/42665662/) | *Structural/mechanistic insights into GluN1-GluN3A* (Kim et al. 2026) | Cryo-EM gating mechanism (GluN3A paralog, informs family) |

**Consistency:** Two independent cloning papers ([PMID: 11717388](https://pubmed.ncbi.nlm.nih.gov/11717388/); [PMID: 12008020](https://pubmed.ncbi.nlm.nih.gov/12008020/)) converge on the dominant/dominant-negative, Ca²⁺-permeability-reducing modulatory role, and the excitatory-glycine-receptor property is supported by a *Nature* primary study ([PMID: 11823786](https://pubmed.ncbi.nlm.nih.gov/11823786/)) and independent pharmacology ([PMID: 17502428](https://pubmed.ncbi.nlm.nih.gov/17502428/)). Structural ([PMID: 18636091](https://pubmed.ncbi.nlm.nih.gov/18636091/)), localization ([PMID: 15813953](https://pubmed.ncbi.nlm.nih.gov/15813953/); [PMID: 18425811](https://pubmed.ncbi.nlm.nih.gov/18425811/)), and genetic ([PMID: 17687115](https://pubmed.ncbi.nlm.nih.gov/17687115/); [PMID: 28132660](https://pubmed.ncbi.nlm.nih.gov/28132660/)) lines all reinforce rather than contradict the model.

---

## Limitations and Knowledge Gaps

1. **Heterologous vs. native physiology.** Much of the biophysical and pharmacological characterization (dominant-negative current suppression, Ca²⁺-impermeable glycine channels) was obtained in *Xenopus* oocytes and HEK293 cells. The prevalence, stoichiometry, and functional contribution of **native GluN3B-containing receptors in human neurons remains under-defined**. Recent work on the GluN3A paralog even indicates native receptors may be diheteromeric ([PMID: 42665662](https://pubmed.ncbi.nlm.nih.gov/42665662/)), raising questions about which native assemblies GluN3B actually joins.

2. **GluN3B-specific structural data.** The atomic structural evidence for glycine/D-serine binding covers the isolated NR3A/NR3B LBDs ([PMID: 18636091](https://pubmed.ncbi.nlm.nih.gov/18636091/)), and recent full-length cryo-EM gating studies are on **GluN3A**, not GluN3B specifically ([PMID: 42665662](https://pubmed.ncbi.nlm.nih.gov/42665662/)). A full-length GluN3B structure is not yet in the reviewed record.

3. **Endogenous ligand and physiological trigger.** Whether glycine, D-serine, or another agonist drives GluN1/GluN3B receptors *in vivo*, and under what circumstances these diheteromers are physiologically engaged, is not resolved.

4. **Tolerated null allele paradox.** ~10% of some human populations are homozygous null for GRIN3B with no overt disease ([PMID: 17880385](https://pubmed.ncbi.nlm.nih.gov/17880385/)), which complicates assigning an essential, non-redundant function and suggests substantial redundancy or compensatory mechanisms.

5. **Disease associations are modest/single-study.** The schizophrenia link rests largely on one family-based/enriched-cohort study ([PMID: 28132660](https://pubmed.ncbi.nlm.nih.gov/28132660/)) and warrants replication; the ALS association is clearly negative ([PMID: 17687115](https://pubmed.ncbi.nlm.nih.gov/17687115/)).

6. **Species extrapolation.** Many localization/developmental data are from mouse and rat; human-specific expression timing and distribution are less completely mapped.

---

## Proposed Follow-up Experiments / Actions

1. **Native receptor isolation in human/primate motoneurons.** Use single-molecule pull-down (SiMPull) and proteomics to determine the actual stoichiometry and partner composition of GluN3B-containing receptors in native tissue, extending the approach used for GluN3A ([PMID: 42665662](https://pubmed.ncbi.nlm.nih.gov/42665662/)).

2. **Full-length cryo-EM of GluN1/GluN3B.** Solve antagonist-, glycine-, and D-serine-bound states of the GluN1/GluN3B diheteromer to confirm whether the GluN3A gating model transfers to GluN3B and to visualize the unique loop 1 in a full-length context.

3. **Conditional, motoneuron-specific manipulation.** Generate cell-type-specific GRIN3B knock-in/knock-out and the S1/S2 frameshift allele in mice to test the anti-excitotoxic hypothesis directly (e.g., vulnerability to glutamate/ischemic challenge and ALS-model crosses).

4. **Human iPSC-derived motoneurons.** Compare Ca²⁺ handling, excitotoxic resistance, and dendritic morphology between GRIN3B-null and wild-type human iPSC motoneurons to test the neuroprotective and morphogenic roles in a human system.

5. **Replication of the schizophrenia association.** Large-cohort genetic replication and functional electrophysiology of the rs10666583 glycine-binding-domain variant to confirm or refute causality ([PMID: 28132660](https://pubmed.ncbi.nlm.nih.gov/28132660/)).

6. **Pharmacological probes.** Exploit emerging GluN1/GluN3-selective positive allosteric modulators (e.g., UCM-A86, CGP-78608) to probe native GluN3B function and therapeutic potential in motoneuron protection.

---

## Conclusion

GRIN3B encodes GluN3B (NR3B), a glycine-/D-serine-binding, non-pore-forming **modulatory subunit** of the NMDA receptor family that cannot function alone and must co-assemble with the obligatory GluN1 subunit at the neuronal plasma membrane. Its primary biochemical function is to **tune excitatory ion flux**: as a dominant-negative subunit in GluN1/GluN2 receptors it suppresses glutamate-evoked current, lowers Ca²⁺ permeability, and reduces Mg²⁺ block (limiting excitotoxic Ca²⁺ influx), while with GluN1 alone it forms unconventional **excitatory glycine receptors** that are glutamate-insensitive, D-serine-inhibited, Ca²⁺-impermeable, and resistant to classical NMDAR blockers. It acts post-synaptically in central glutamatergic/glycinergic signaling, is most prominently expressed in brainstem and spinal **somatic motoneurons** (where it becomes the dominant regulatory subunit via a postnatal NR2→NR3B switchover and shapes dendrite morphogenesis), and its common human null allele is tolerated and ALS-neutral, whereas a glycine-binding-domain frameshift variant is linked to schizophrenia.


## Artifacts

- [OpenScientist final report](GRIN3B-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](GRIN3B-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:11717388
2. PMID:12008020
3. PMID:17687115
4. PMID:22240240
5. PMID:18425811
6. PMID:20813147
7. PMID:11823786
8. PMID:17502428
9. PMID:40235311
10. PMID:42665662
11. PMID:18636091
12. PMID:18779583
13. PMID:15813953
14. PMID:18541382
15. PMID:17880385
16. PMID:28132660