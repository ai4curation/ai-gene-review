---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T13:27:22.298656'
end_time: '2026-07-11T13:39:35.916427'
duration_seconds: 733.62
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: miaE
  gene_symbol: miaE
  uniprot_accession: Q88KV1
  protein_description: 'RecName: Full=tRNA 2-(methylsulfanyl)-N(6)-isopentenyladenosine(37)
    hydroxylase {ECO:0000305}; EC=1.14.99.69 {ECO:0000269|PubMed:32785618}; AltName:
    Full=2-methylthio-N6-isopentenyladenosine(37)-tRNA monooxygenase {ECO:0000250|UniProtKB:Q08015};
    AltName: Full=tRNA-(ms[2]io[6]A37)-hydroxylase {ECO:0000250|UniProtKB:Q08015};'
  gene_info: Name=miaE {ECO:0000303|PubMed:32785618}; OrderedLocusNames=PP_2188 {ECO:0000312|EMBL:AAN67801.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the MiaE family. .
  protein_domains: Ferritin-like. (IPR012347); Ferritin-like_SF. (IPR009078); tRNA-Hydrxlase_MiaE.
    (IPR010386); MiaE (PF06175)
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
citation_count: 10
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: miaE-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: miaE-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88KV1
- **Protein Description:** RecName: Full=tRNA 2-(methylsulfanyl)-N(6)-isopentenyladenosine(37) hydroxylase {ECO:0000305}; EC=1.14.99.69 {ECO:0000269|PubMed:32785618}; AltName: Full=2-methylthio-N6-isopentenyladenosine(37)-tRNA monooxygenase {ECO:0000250|UniProtKB:Q08015}; AltName: Full=tRNA-(ms[2]io[6]A37)-hydroxylase {ECO:0000250|UniProtKB:Q08015};
- **Gene Information:** Name=miaE {ECO:0000303|PubMed:32785618}; OrderedLocusNames=PP_2188 {ECO:0000312|EMBL:AAN67801.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the MiaE family. .
- **Key Domains:** Ferritin-like. (IPR012347); Ferritin-like_SF. (IPR009078); tRNA-Hydrxlase_MiaE. (IPR010386); MiaE (PF06175)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "miaE" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'miaE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **miaE** (gene ID: miaE, UniProt: Q88KV1) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: **miaE** (PP_2188 / UniProt Q88KV1) in *Pseudomonas putida* KT2440

## Summary

**MiaE (gene *miaE*, ordered locus PP_2188, UniProt Q88KV1) of *Pseudomonas putida* KT2440 is a soluble, cytoplasmic non-heme carboxylate-bridged diiron monooxygenase that catalyzes the final step of a three-enzyme tRNA anticodon-loop modification pathway.** Its defined reaction (EC 1.14.99.69) is the O₂- and reductant-dependent, E-stereospecific allylic hydroxylation of the terminal isopentenyl carbon (C4) of 2-methylthio-N⁶-isopentenyladenosine at position 37 (ms²i⁶A37) in tRNA, generating 2-methylthio-N⁶-(4-hydroxyisopentenyl)adenosine (ms²io⁶A37, also historically called "2-methylthio-*cis*-ribozeatin"). This identity is directly and unambiguously established for the *P. putida* PP_2188 protein by combined in vivo, in vitro, and X-ray crystallographic characterization [PMID: 32785618](https://pubmed.ncbi.nlm.nih.gov/32785618/), fully consistent with the UniProt annotation of Q88KV1 in the target organism. The gene symbol, organism, protein family (MiaE family), and domain architecture (Ferritin-like superfamily; Pfam MiaE, PF06175) all cross-validate. **This report therefore proceeds with confidence that the correct gene/protein was studied.**

The enzyme sits at the end of the biosynthetic sequence **MiaA → MiaB → MiaE**: the isopentenyltransferase MiaA installs the N⁶-isopentenyl group (i⁶A37), the radical-SAM methylthiotransferase MiaB adds a 2-methylthio group (ms²i⁶A37), and MiaE hydroxylates the isoprenoid tail to yield ms²io⁶A37. MiaE is structurally a member of the ferritin-like diiron monooxygenase class whose active site resembles that of the soluble methane monooxygenase hydroxylase, making it the first (and still nearly unique) example of a diiron monooxygenase that hydroxylates a biological macromolecule rather than a small molecule. In *P. putida*, the diiron center is coordinated by six residues within a four-α-helix bundle, and a krypton-defined hydrophobic tunnel channels O₂ to the metal cluster. Catalysis in vitro requires an electron-transport chain (ferredoxin + ferredoxin reductase + NADPH), and the enzyme recognizes the intact tRNA anticodon stem-loop, which enhances catalytic efficiency roughly 6000-fold over free nucleoside substrate.

Biologically, position-37 hypermodifications of this type stabilize the anticodon loop and tune decoding efficiency and fidelity for tRNAs that read codons beginning with U. In *Salmonella typhimurium* (the historical model for this enzyme), loss of the hydroxylation step specifically prevents aerobic growth on the citric-acid-cycle dicarboxylic acids succinate, fumarate, and malate — a phenotype that traces to the tRNA modification state itself, not to a separate metabolic function of MiaE. The gene is taxonomically restricted (absent from *E. coli*), consistent with the absence of ms²io⁶A in species lacking *miaE*.

---

## Gene/Protein Identity Verification

The target is **MiaE**, tRNA 2-(methylsulfanyl)-N⁶-isopentenyladenosine(37) hydroxylase (EC 1.14.99.69), encoded by ordered locus **PP_2188** in *Pseudomonas putida* KT2440 (UniProt **Q88KV1**), MiaE family, ferritin-like/PF06175 domain. All identity checks are satisfied:

- **Gene symbol matches protein description.** The dedicated *P. putida* study explicitly states that *"the putative pp-2188 gene encodes a MiaE enzyme"* [PMID: 32785618](https://pubmed.ncbi.nlm.nih.gov/32785618/), directly linking the PP_2188 locus to MiaE function.
- **Organism is correct.** The primary experimental characterization was performed on the *Pseudomonas putida* protein itself (not merely inferred from an ortholog).
- **Protein family/domains align.** The crystal structure confirms the ferritin-like four-α-helix-bundle diiron fold predicted by InterPro/Pfam (PF06175, IPR010386).

There is **no ambiguity** and no conflation with a same-symbol gene in another organism. The literature for *miaE* is specific and internally consistent across *P. putida* and *S. typhimurium* orthologs.

---

## Key Findings

### Finding 1 — MiaE catalyzes O₂-dependent allylic hydroxylation of ms²i⁶A37 to ms²io⁶A37 in tRNA

The primary, defining function of MiaE is established at the level of the specific *P. putida* protein. Direct in vivo, in vitro, and X-ray structural characterization demonstrated that the putative PP_2188 gene encodes a functional MiaE enzyme [PMID: 32785618](https://pubmed.ncbi.nlm.nih.gov/32785618/). The reaction it catalyzes is described precisely: *"MiaE (2-methylthio-N6-isopentenyl-adenosine37-tRNA monooxygenase) is a unique non-heme diiron enzyme that catalyzes the O2-dependent post-transcriptional allylic hydroxylation of a hypermodified nucleotide 2-methylthio-N6-isopentenyl-adenosine (ms2i6A37) at position 37 of selected tRNA molecules to produce 2-methylthio-N6-4-hydroxyisopentenyl-adenosine (ms2io6A37)."* The same paper confirms the target's identity: *"The investigation demonstrates that the putative pp-2188 gene encodes a MiaE enzyme."*

The reaction carries EC number **1.14.99.69**. The formal transformation (from UniProtKB Q88KV1) is:

> 2-methylsulfanyl-N⁶-dimethylallyladenosine(37) in tRNA + AH₂ + O₂ → N⁶-[(2E)-4-hydroxy-3-methylbut-2-en-1-yl]-2-(methylsulfanyl)adenosine(37) in tRNA + A + H₂O

Quantitative steady-state kinetics have been measured on an anticodon-stem-loop substrate. MiaE-catalyzed hydroxylation of the i⁶A-containing anticodon stem-loop of tRNA^Trp *"follows Michaelis-Menten saturation kinetics with kcat, KM, and V/K determined to be 0.10 ± 0.01 s⁻¹, 9.1 ± 1.5 μM, and ∼11000 M⁻¹ s⁻¹, respectively"* [PMID: 25453905](https://pubmed.ncbi.nlm.nih.gov/25453905/). These are physiologically relevant parameters: a modest turnover number (~0.1 s⁻¹) typical of a diiron monooxygenase acting on a large macromolecular substrate, with micromolar affinity for the folded anticodon stem-loop.

### Finding 2 — MiaE is a non-heme carboxylate-bridged diiron monooxygenase with a ferritin-like four-helix-bundle fold

MiaE belongs to the ferritin-like superfamily of carboxylate-bridged diiron enzymes. Spectroscopic characterization (UV-vis, EPR, HYSCORE, Mössbauer) of the *S. typhimurium* enzyme established that *"the MiaE enzyme contains a nonheme dinuclear iron cluster, similar to that found in the hydroxylase component of methane monooxygenase. This is the first example of an enzyme from this important class of diiron monooxygenases to be involved in the hydroxylation of a biological macromolecule"* [PMID: 17679698](https://pubmed.ncbi.nlm.nih.gov/17679698/). This places MiaE alongside soluble methane monooxygenase (sMMO), ribonucleotide reductase R2, and Δ9-desaturase in the diiron-carboxylate structural class, but sets it apart functionally because its substrate is a modified nucleotide embedded in a tRNA rather than a small molecule.

The crystal structure of the *P. putida* enzyme confirmed the fold at atomic resolution: *"The structure shows that Pp-MiaE consists of a catalytic diiron(III) domain with a four alpha-helix bundle fold"* [PMID: 32785618](https://pubmed.ncbi.nlm.nih.gov/32785618/). The same study defined how dioxygen reaches the buried metal cluster: *"krypton-pressurized Pp-MiaE experiments, revealed the presence of defined O2 site along a conserved hydrophobic tunnel leading to the diiron active center."* This hydrophobic O₂ delivery channel is a hallmark of diiron monooxygenases and explains the enzyme's strict O₂ dependence. The InterPro/Pfam annotations for Q88KV1 (Ferritin-like, IPR012347/IPR009078; tRNA-Hydroxylase MiaE, IPR010386; Pfam PF06175) are fully corroborated by this experimental structure.

### Finding 3 — Substrate specificity: E-stereoselective C4 hydroxylation with tRNA anticodon-loop recognition driving a ~6000-fold rate enhancement

MiaE's chemistry is highly regio- and stereo-selective. Using peroxide-shunt assays with a series of nucleoside surrogates, the enzyme hydroxylated only the terminal carbon of the isopentenyl group with defined stereochemistry: *"regardless of the substrate (i(6)A, Cl(2)i(6)A, and ms(2)i(6)A) used in peroxide-shunt assays, hydroxylation of the terminal isopentenyl-C4-position was observed with >97% E-stereoselectivity. No other nonspecific hydroxylation products were observed in enzymatic assays"* [PMID: 23906247](https://pubmed.ncbi.nlm.nih.gov/23906247/). The enzyme tolerates variation at the 2-position of the adenine (with or without methylthio/dichloro substituents) but rigidly directs oxidation to the allylic C4 of the prenyl tail, producing the E-configured 4-hydroxy product.

Although MiaE can chemically hydroxylate free nucleosides via the peroxide shunt, its physiological substrate is the folded tRNA anticodon stem-loop, and recognition of that structure is what makes the enzyme efficient. Comparing free nucleoside to an anticodon-stem-loop (ACSL-Trp) substrate revealed that *"an ∼6000-fold increase in enzymatic efficiency is imparted by ACSL(Trp)-MiaE interactions"* [PMID: 25453905](https://pubmed.ncbi.nlm.nih.gov/25453905/). Structural docking and site-directed mutagenesis of the *P. putida* enzyme localized the determinants of this recognition: the study, *"combined with site directed mutagenesis and in vivo activity shed light on the importance of an additional linker region for substrate tRNA recognition"* [PMID: 32785618](https://pubmed.ncbi.nlm.nih.gov/32785618/). Thus MiaE's substrate specificity operates at two levels: exquisite chemical regioselectivity for the isopentenyl C4, and macromolecular selectivity for the anticodon stem-loop presenting ms²i⁶A37.

### Finding 4 — Localization, electron-transport partners, and pathway context

MiaE is a soluble cytoplasmic tRNA-modifying enzyme that performs the last of three sequential modifications at position 37. The pathway was defined as: *"the enzymes that introduce the respective modifications (prenyltransferase MiaA, methylthiotransferase MiaB, and hydroxylase MiaE) have been identified"* [PMID: 17910062](https://pubmed.ncbi.nlm.nih.gov/17910062/). MiaA (a dimethylallyltransferase) installs i⁶A37; MiaB (a radical-SAM methylthiotransferase) converts it to ms²i⁶A37; MiaE (this enzyme) hydroxylates the prenyl tail to give ms²io⁶A37.

As a diiron monooxygenase, MiaE requires external reducing equivalents to regenerate the reduced diiron(II) state and activate O₂. In vitro reconstitution demonstrated the electron-supply system: the assay used *"recombinant ferredoxin (Fd) and ferredoxin reductase (FdR) to provide a catalytic electron transport chain (ETC) using NADPH as the sole electron source"* [PMID: 25453905](https://pubmed.ncbi.nlm.nih.gov/25453905/). This ferredoxin/ferredoxin-reductase/NADPH chain represents the physiological route by which cellular reducing power is delivered to the enzyme.

The modification's target location on the tRNA anchors its functional role: the base *"is present in position 37 (adjacent to and 3' of the anticodon) of tRNAs that read codons beginning with U"* [PMID: 9620964](https://pubmed.ncbi.nlm.nih.gov/9620964/). Position 37 immediately 3′ of the anticodon is a canonical hotspot for hypermodifications that stabilize codon–anticodon pairing.

### Finding 5 — Physiological role: modification status governs aerobic growth on TCA-cycle dicarboxylic acids; the gene is taxonomically restricted

In the *Salmonella* model, the specific consequence of losing MiaE activity is a defined growth phenotype. *"Mutants (miaE) of S. typhimurium in which ms2i6A hydroxylation is blocked are unable to grow aerobically on the dicarboxylic acids of the citric acid cycle"* [PMID: 9620964](https://pubmed.ncbi.nlm.nih.gov/9620964/). Importantly, the determinant is the tRNA modification state itself, not a separate moonlighting activity of the protein: *"S. typhimurium senses the hydroxylation status of the isopentenyl group of the tRNA and will grow on succinate, fumarate, or malate only if the isopentenyl group is hydroxylated."* Uptake of the dicarboxylates and the TCA/respiratory enzymes remain functional in the mutant, so the growth block is a translation-level effect propagated by the altered anticodon modification.

The gene is not universally distributed. *"Southern blot analysis showed that the miaE gene is absent in E. coli, a finding consistent with the absence of the hydroxylated derivative of ms2i6A in this species"* [PMID: 8253666](https://pubmed.ncbi.nlm.nih.gov/8253666/). The presence of *miaE* in *P. putida* and *Salmonella* but its absence in *E. coli* mirrors the phylogenetic distribution of the ms²io⁶A37 modification and underscores that this hydroxylation is a lineage-specific elaboration of the more widely conserved ms²i⁶A37.

### Finding 6 — Residue-level diiron coordination and structural data for *P. putida* MiaE (Q88KV1)

At the residue level, UniProtKB Q88KV1 (entry name MIAE_PSEPK) describes a **205-amino-acid** protein whose cofactor is iron. The diiron center is coordinated by **six residues at positions 38, 69, 72, 122, 151, and 154**, arranged as the two carboxylate/His clusters characteristic of the ferritin-like E-X-X-H diiron motif embedded in the four-helix bundle. This ligand set is the structural basis for the spectroscopic and crystallographic observations in Findings 2–3.

Experimental structures are available. The Protein Data Bank contains **PDB 2ITB** (2.05 Å) and the structures **6ZMA / 6ZMB / 6ZMC** (1.70–2.50 Å) reported in the *P. putida* study [PMID: 32785618](https://pubmed.ncbi.nlm.nih.gov/32785618/), plus an AlphaFold model. UniProt lists the biological assembly as a **homodimer** (the crystals contain two chains), whereas the isolated *Salmonella* enzyme was reported as a **monomer** [PMID: 17679698](https://pubmed.ncbi.nlm.nih.gov/17679698/) — a minor discrepancy likely reflecting species differences or crystallization conditions rather than a functional divergence.

### Finding 7 — Translational rationale: A37 isopentenyl-type modifications stabilize the anticodon loop and support decoding efficiency and fidelity

The reason cells invest in hydroxylating ms²i⁶A37 traces to the general role of position-37 isoprenoid modifications in translation. Biophysical work showed that these modifications structurally reinforce the anticodon arm: *"UV melting and differential scanning calorimetry indicate that the modifications stabilize the stem and may enhance base stacking in the loop"* [PMID: 21782828](https://pubmed.ncbi.nlm.nih.gov/21782828/). By enhancing stacking and (with Mg²⁺) promoting the canonical U-turn fold, the modification pre-organizes the anticodon loop for accurate codon reading.

Functionally, the i⁶A37 modification tunes decoding in a codon-specific manner: *"i6A37 promotes decoding activity generally and increases fidelity at cognate codons while decreasing fidelity at noncognate codons"* [PMID: 23716598](https://pubmed.ncbi.nlm.nih.gov/23716598/). Loss of the modification degrades translational accuracy. Consistent with this, combined loss of the position-34 queuosine and position-37 ms²i⁶A modifications has severe consequences: *"Simultaneous absence of Q34 and ms2i6A37 increases +1 frameshifting at tyrosine codons and promotes protein aggregation, indicating impaired tRNATyr function"* [PMID: 42391044](https://pubmed.ncbi.nlm.nih.gov/42391044/). The MiaE-installed hydroxyl group is the final fine-tuning of this modification, adjusting the chemical properties of the isoprenoid tail on tRNAs decoding U-starting codons.

---

## Mechanistic Model / Interpretation

MiaE is best understood as the **terminal tailoring enzyme** of a stepwise anticodon-loop hypermodification pathway that converts a plain adenosine at position 37 into the highly elaborated ms²io⁶A37. The pathway and MiaE's place in it can be summarized as follows:

```
   tRNA(A37)                 tRNA(i6A37)              tRNA(ms2i6A37)            tRNA(ms2io6A37)
       │                         │                         │                         │
       │  MiaA                   │  MiaB                   │  MiaE (PP_2188)         │
       │  prenyltransferase      │  radical-SAM            │  diiron monooxygenase   │
       │  (DMAPP donor)          │  methylthiotransferase  │  EC 1.14.99.69          │
       ▼                         ▼                         ▼                         ▼
   adenosine ────────►  N6-isopentenyl ──────►  2-methylthio-N6-  ──────►  2-methylthio-N6-
                         adenosine                isopentenyladenosine      (4-OH-isopentenyl)adenosine
                                                                            = "2-methylthio-cis-ribozeatin"

  MiaE half-reaction:   ms2i6A37-tRNA + O2 + AH2  ──►  ms2io6A37-tRNA + H2O + A
  Electron supply:      NADPH ─► ferredoxin reductase (FdR) ─► ferredoxin (Fd) ─► MiaE diiron center
  O2 delivery:          via a conserved hydrophobic tunnel to the buried diiron(III) cluster
```

**Chemical logic.** MiaE is a carboxylate-bridged diiron monooxygenase whose active-site chemistry parallels sMMO: a reduced diiron(II) center binds and activates O₂ to form a high-valent oxidant that inserts oxygen into a C–H bond. Here the target is the allylic C4 of the isopentenyl tail. The reaction's strict >97% E-stereoselectivity for the terminal carbon (Finding 3) reflects precise positioning of the prenyl group over the metal-oxo species, while the requirement for external electrons (Fd/FdR/NADPH; Finding 4) reflects the need to re-reduce the diiron center each catalytic cycle. The buried nature of the diiron site necessitates the hydrophobic O₂ tunnel identified by krypton pressurization (Finding 2).

**Macromolecular recognition.** Unlike its small-molecule diiron relatives, MiaE must dock a folded RNA. The ~6000-fold catalytic-efficiency gain conferred by the anticodon stem-loop (Finding 3) shows that the enzyme's productive substrate is the tRNA, not the free nucleoside; a linker region flanking the catalytic domain mediates tRNA recognition. This coupling of a classic diiron oxygenase fold to a tRNA-binding module is what makes MiaE the first-described diiron monooxygenase acting on a biological macromolecule.

**Physiological output.** The purpose of the modification is translational. Position-37 modifications stabilize the anticodon loop and improve decoding fidelity/efficiency for U-starting codons (Findings 5, 7). In *Salmonella*, the hydroxylation state is read out as a specific requirement for aerobic growth on TCA-cycle dicarboxylates — a phenotype that is a downstream consequence of altered translation, not a separate function of the protein. By extension, in *P. putida* KT2440 — a metabolically versatile soil bacterium — MiaE is expected to fine-tune translation of transcripts enriched in the relevant U-starting codons, with the modification's presence tracking the organism's aerobic physiology.

### Comparative summary of the two best-characterized MiaE orthologs

| Property | *P. putida* MiaE (PP_2188, Q88KV1) — **target** | *S. typhimurium* MiaE |
|---|---|---|
| Reaction | ms²i⁶A37 → ms²io⁶A37, O₂-dependent | Same |
| EC / class | 1.14.99.69, non-heme diiron monooxygenase | Non-heme diiron monooxygenase |
| Structural evidence | X-ray (PDB 2ITB; 6ZMA/B/C), O₂ tunnel defined | Spectroscopy (UV-vis, EPR, HYSCORE, Mössbauer) |
| Fold | Ferritin-like four-α-helix bundle; diiron(III) | Dinuclear Fe cluster ~ sMMO hydroxylase |
| Oligomeric state | Homodimer (crystal) | Monomer (isolated) |
| Electron donors | Fd + FdR + NADPH (in vitro) | Diiron center; reductant-dependent |
| Phenotype studied | tRNA recognition (mutagenesis, in vivo activity) | Aerobic growth on succinate/fumarate/malate |
| Length / Fe ligands | 205 aa; residues 38/69/72/122/151/154 | — |

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution to this annotation |
|---|---|---|
| [32785618](https://pubmed.ncbi.nlm.nih.gov/32785618/) | *Structural, biochemical and functional analyses of MiaE from P. putida* | **Primary source for the target protein.** Confirms PP_2188 encodes MiaE; defines reaction; solves crystal structure (four-helix bundle, diiron(III)); identifies O₂ tunnel and tRNA-recognition linker. |
| [25453905](https://pubmed.ncbi.nlm.nih.gov/25453905/) | *Steady-state kinetics and spectroscopy of MiaE-tRNA interactions* | Provides kcat/KM/(V/K); demonstrates ~6000-fold efficiency gain from anticodon stem-loop; identifies Fd/FdR/NADPH electron-transport chain. |
| [23906247](https://pubmed.ncbi.nlm.nih.gov/23906247/) | *Peroxide-shunt substrate specificity of MiaE* | Establishes >97% E-selective hydroxylation at isopentenyl C4; no nonspecific products; substrate tolerance at the 2-position. |
| [17679698](https://pubmed.ncbi.nlm.nih.gov/17679698/) | *MiaE is a nonheme diiron monooxygenase* | Defines the dinuclear iron cluster (sMMO-like); first diiron monooxygenase acting on a macromolecule; reports monomeric *Salmonella* enzyme. |
| [17910062](https://pubmed.ncbi.nlm.nih.gov/17910062/) | *Structural bioinformatics of the ms²io⁶A37 pathway* | Defines the MiaA → MiaB → MiaE pathway and MiaE's role as the hydroxylase step. |
| [9620964](https://pubmed.ncbi.nlm.nih.gov/9620964/) | *ms²io⁶A37 regulates growth on citric-acid-cycle intermediates* | Position/codon context (pos. 37, U-starting codons); links hydroxylation state to aerobic growth on succinate/fumarate/malate. |
| [8253666](https://pubmed.ncbi.nlm.nih.gov/8253666/) | *Isolation of miaE and mutant characterization* | Original gene isolation; documents taxonomic restriction (absent in *E. coli*). |
| [21782828](https://pubmed.ncbi.nlm.nih.gov/21782828/) | *Conformation effects of base modification on anticodon stem-loop* | Biophysical evidence that i⁶A37-type modifications stabilize the stem and enhance loop stacking. |
| [23716598](https://pubmed.ncbi.nlm.nih.gov/23716598/) | *Lack of i⁶A37 alters mRNA decoding (fission yeast)* | Establishes decoding-efficiency/fidelity role of the position-37 modification. |
| [42391044](https://pubmed.ncbi.nlm.nih.gov/42391044/) | *Defective Q and i⁶A/ms²i⁶A cause frameshifting and aggregation* | Links loss of ms²i⁶A37 to +1 frameshifting and proteostasis defects. |

The evidence base is notably **convergent**: independent structural (X-ray, spectroscopy), enzymological (steady-state kinetics, peroxide-shunt regiochemistry), genetic (mutant phenotypes, gene isolation), and biophysical (tRNA conformation) lines all point to the same coherent function. No paper in the reviewed set contradicts the assigned function. The only minor internal tension is the oligomeric state (homodimer in *P. putida* crystals vs. monomer for isolated *Salmonella* enzyme), which does not affect the functional assignment.

---

## Limitations and Knowledge Gaps

1. **Species transfer of the growth phenotype.** The specific aerobic-growth-on-dicarboxylates phenotype is documented in *S. typhimurium* [PMID: 9620964](https://pubmed.ncbi.nlm.nih.gov/9620964/), not in *P. putida* KT2440. Whether *P. putida* exhibits an equivalent metabolic phenotype upon *miaE* deletion has not been directly demonstrated in the reviewed literature. The core enzymatic function, however, is directly established for the *P. putida* protein itself.

2. **In vivo electron donors in *P. putida*.** The Fd/FdR/NADPH chain was reconstituted in vitro [PMID: 25453905](https://pubmed.ncbi.nlm.nih.gov/25453905/). The identity of the specific physiological ferredoxin(s) and reductase(s) partnering MiaE inside *P. putida* cells is not pinned down.

3. **Full tRNA substrate repertoire.** MiaE acts on tRNAs reading U-starting codons, but a complete, quantitative census of which *P. putida* tRNA isoacceptors carry ms²io⁶A37 (and to what stoichiometry) is not established in the reviewed set.

4. **Catalytic intermediate.** While the diiron center and sMMO-like character are established, the exact nature of the high-valent oxidizing intermediate and the detailed C–H activation mechanism for the allylic hydroxylation have not been trapped/characterized here.

5. **Regulation.** How *miaE* expression and MiaE activity respond to oxygen tension, growth phase, or carbon source in *P. putida* is unaddressed.

6. **Oligomeric-state discrepancy.** The functional significance (if any) of the homodimer-vs-monomer difference between species remains unresolved.

---

## Proposed Follow-up Experiments / Actions

1. **Targeted *P. putida* KT2440 Δ*miaE* phenotyping.** Construct a clean PP_2188 deletion and (a) confirm loss of ms²io⁶A37 by LC-MS/MS of bulk tRNA, and (b) test aerobic growth on succinate, fumarate, and malate versus glucose to determine whether the *Salmonella* metabolic phenotype is conserved.

2. **Map the in vivo electron-transport partners.** Use co-purification / bacterial two-hybrid / crosslinking to identify the endogenous ferredoxin and ferredoxin-reductase that supply electrons to MiaE in *P. putida*, then reconstitute activity with the native partners.

3. **tRNA-ome modification survey.** Perform isoacceptor-resolved mass spectrometry (or modification-sensitive sequencing) to enumerate which *P. putida* tRNAs carry ms²io⁶A37 and quantify modification stoichiometry, testing the "U-starting codon" specificity directly in this organism.

4. **Mechanistic trapping.** Apply rapid-freeze-quench Mössbauer/EPR with O₂ to capture the reactive diiron-oxygen intermediate and define the oxidant responsible for allylic C4 hydroxylation.

5. **Structure of the enzyme–tRNA complex.** Pursue a cryo-EM or co-crystal structure of MiaE bound to a full-length tRNA (or extended anticodon stem-loop) to visualize the linker-mediated recognition that drives the ~6000-fold efficiency gain and to rationalize the mutagenesis data.

6. **Codon-usage / translational-fidelity readout.** In *P. putida*, use reporter assays or ribosome profiling in wild-type vs. Δ*miaE* to test whether decoding efficiency/fidelity at U-starting codons is measurably altered, connecting the modification to translation as predicted from the yeast/*Salmonella* literature.

---

## Conclusion

The identity check requested in the research brief is satisfied without ambiguity: gene symbol (*miaE*), organism (*P. putida* KT2440), locus (PP_2188), UniProt accession (Q88KV1), protein family (MiaE), and domain architecture (ferritin-like diiron; Pfam PF06175) are mutually consistent and are backed by a dedicated experimental study of this exact protein [PMID: 32785618](https://pubmed.ncbi.nlm.nih.gov/32785618/). **MiaE is a soluble, cytoplasmic non-heme diiron monooxygenase (EC 1.14.99.69) that performs the terminal, O₂- and reductant-dependent, E-stereospecific allylic hydroxylation of ms²i⁶A37 to ms²io⁶A37 in the anticodon loops of tRNAs reading U-starting codons, thereby completing the MiaA→MiaB→MiaE modification pathway and fine-tuning translational decoding.**


## Artifacts

- [OpenScientist final report](miaE-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](miaE-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:32785618
2. PMID:25453905
3. PMID:17679698
4. PMID:23906247
5. PMID:17910062
6. PMID:9620964
7. PMID:8253666
8. PMID:21782828
9. PMID:23716598
10. PMID:42391044