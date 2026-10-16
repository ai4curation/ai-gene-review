---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T16:43:34.776788'
end_time: '2026-08-31T16:59:15.002745'
duration_seconds: 940.23
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: flgG
  gene_symbol: flgG
  uniprot_accession: Q88ER8
  protein_description: 'RecName: Full=Flagellar basal-body rod protein FlgG {ECO:0000256|ARBA:ARBA00017948,
    ECO:0000256|NCBIfam:TIGR02488}; AltName: Full=Distal rod protein {ECO:0000256|ARBA:ARBA00032912,
    ECO:0000256|RuleBase:RU362116};'
  gene_info: Name=flgG {ECO:0000313|EMBL:AAN69963.1}; OrderedLocusNames=PP_4385 {ECO:0000313|EMBL:AAN69963.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the flagella basal body rod proteins family.
  protein_domains: Flag_bb_rod_N. (IPR001444); Flagellar_basal_body_rod_CS. (IPR019776);
    Flagellar_FlgE/F/G. (IPR020013); Flg_bb/hook_C_dom. (IPR010930); FlgE/F/G-like.
    (IPR037925)
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
citation_count: 12
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: flgG-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: flgG-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88ER8
- **Protein Description:** RecName: Full=Flagellar basal-body rod protein FlgG {ECO:0000256|ARBA:ARBA00017948, ECO:0000256|NCBIfam:TIGR02488}; AltName: Full=Distal rod protein {ECO:0000256|ARBA:ARBA00032912, ECO:0000256|RuleBase:RU362116};
- **Gene Information:** Name=flgG {ECO:0000313|EMBL:AAN69963.1}; OrderedLocusNames=PP_4385 {ECO:0000313|EMBL:AAN69963.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the flagella basal body rod proteins family.
- **Key Domains:** Flag_bb_rod_N. (IPR001444); Flagellar_basal_body_rod_CS. (IPR019776); Flagellar_FlgE/F/G. (IPR020013); Flg_bb/hook_C_dom. (IPR010930); FlgE/F/G-like. (IPR037925)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "flgG" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'flgG' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **flgG** (gene ID: flgG, UniProt: Q88ER8) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: FlgG (Q88ER8, PP_4385) — Flagellar Basal-Body Distal Rod Protein of *Pseudomonas putida* KT2440

**Target:** FlgG (gene *flgG*; ordered locus **PP_4385**) — UniProt **Q88ER8**
**Organism:** *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125), PSEPK
**Protein family:** Flagellar basal-body rod protein family (FlgB/FlgC/FlgF/FlgG)

## Summary

**FlgG (UniProt Q88ER8; locus PP_4385) is the distal rod protein of the flagellar basal body in *Pseudomonas putida* KT2440.** It is a non-enzymatic, structural axial protein. Roughly 26 copies of FlgG polymerize head-to-tail into the distal segment of the rigid, helical **rod**, which functions as a molecular **drive shaft**: it mechanically transmits torque generated by the membrane-embedded flagellar motor outward across the cell envelope to the extracellular **hook** and **filament**, thereby powering swimming motility. FlgG does not catalyze any reaction, transport any substrate, or transduce a chemical signal; its "substrate" is mechanical rotation, and its role is purely architectural within the flagellar rotary nanomachine.

FlgG occupies a defined position in the cell envelope. The distal rod it forms sits in the **periplasm**, encircled by the **P ring** (embedded in the peptidoglycan layer) and the **L ring** (embedded in the outer membrane), lying immediately proximal to the **rod–hook junction**. Because it is an external axial component with no cleavable Sec signal peptide, FlgG is exported unfolded through the central channel of the growing structure by the dedicated **flagellar type III secretion system (fT3SS)** and self-assembles at the distal tip of the proximal rod. Beyond its static structural role, FlgG carries an intrinsic **molecular ruler** function: it sets the length of the distal rod, and gain-of-function *flgG\** alleles that produce abnormally elongated, filamentous rods also prematurely trigger the fT3SS **substrate-specificity switch** from rod/hook-type (early) to filament-type (late) export.

This annotation for the *P. putida* protein rests on two complementary lines of evidence. First, decades of detailed structural, genetic, and biochemical work on the orthologous FlgG proteins of *Salmonella*, *Bacillus subtilis*, and *Caulobacter crescentus* establish the distal-rod function of the family. Second, sequence analysis performed in this investigation confirms that Q88ER8 is a bona fide, high-confidence FlgG ortholog (56.8 % identity to *Salmonella* FlgG, gap-free, with conserved axial-protein termini) and is specifically the **distal-rod (FlgG-type)** protein rather than the proximal-rod (FlgF-type) paralog (~57 % identity to FlgG vs. only ~31 % to FlgF). In *P. putida* KT2440, *flgG* is embedded in the large polar-flagellar gene cluster (PP4329–PP4397) and is expressed under the master regulator **FleQ** acting through **σ⁵⁴ (σN)** promoters.

---

## Key Findings

### Finding 1 — FlgG is the distal rod protein of the flagellar basal body, a drive-shaft component surrounded by the L and P rings

The bacterial flagellum is a rotary nanomachine assembled from a basal body (embedded in the cell envelope), a hook (a universal joint), and a long helical filament (the propeller). Within the basal body, the **rod** is a rigid axial structure that spans the periplasm and connects the cytoplasmic-membrane-associated motor to the extracellular hook. The rod is built from four structurally related proteins — **FlgB, FlgC, FlgF, and FlgG** — that share strong sequence similarity near their N- and C-termini, hallmarks of the flagellar axial-protein family ([PMID: 2129540](https://pubmed.ncbi.nlm.nih.gov/2129540/)).

Among these four, FlgG occupies the **distal** portion of the rod — the outermost segment, positioned precisely in the region girdled by the **L ring** (outer membrane) and **P ring** (peptidoglycan), immediately before the rod–hook junction. As the classic study by Homma and colleagues put it, *"FlgG is known to lie within the distal portion of the rod, in the region where it is surrounded by the L and P rings, just before the rod-hook junction"* ([PMID: 2129540](https://pubmed.ncbi.nlm.nih.gov/2129540/)). The functional significance of the rod is mechanical: it is *"the rod, which is believed to transmit motor rotation to the filament"* ([PMID: 2129540](https://pubmed.ncbi.nlm.nih.gov/2129540/)). In other words, FlgG helps form the **drive shaft** that couples the torque-generating motor to the propeller.

That the *P. putida* protein Q88ER8 (PP_4385) belongs to this family is confirmed by its domain architecture: it carries the flagellar basal-body rod N-terminal domain (Flag_bb_rod_N, IPR001444), the flagellar basal-body rod conserved site (IPR019776), and the FlgE/F/G-like fold (IPR037925 / IPR020013). These are the diagnostic signatures of the basal-body rod protein family, placing FlgG firmly within it.

### Finding 2 — FlgG assembles as ~26 subunits forming the distal rod, exported by the flagellar T3SS without a cleavable signal peptide

Quantitative stoichiometric analysis of the isolated *Salmonella* hook-basal-body complex revealed a striking asymmetry between the distal and proximal rod proteins. The distal rod protein **FlgG is present at approximately 26 subunits**, whereas the proximal rod proteins FlgB, FlgC, and FlgF are present at only ~6 subunits each — roughly one helical turn apiece. As reported: *"The distal rod protein (FlgG) is present at approximately 26 subunits, while the proximal rod proteins (FlgB, FlgC and FlgF) are present at only approximately six subunits each"* ([PMID: 2181149](https://pubmed.ncbi.nlm.nih.gov/2181149/)). This means FlgG contributes the bulk of the rod's length: the proximal rod is a short adaptor, while the distal rod (FlgG) forms the long, load-bearing shaft that traverses the periplasmic space.

Despite building an external, periplasmic structure, none of the rod proteins is exported by the general secretory (Sec) pathway. As established, *"none of the four rod proteins contains a consensus signal sequence for the primary export pathway"* ([PMID: 2129540](https://pubmed.ncbi.nlm.nih.gov/2129540/)). Instead, FlgG and the other axial proteins are translocated in an unfolded state through the **central channel** of the nascent flagellum by the **flagellar type III secretion system (fT3SS)**, where they then fold and self-assemble at the distal growing tip. This mode of export is a defining feature of all flagellar axial proteins and distinguishes the rod proteins from the ring proteins (e.g., the L-ring protein FlgH), which *do* carry cleavable Sec signal sequences. The fT3SS mechanism — in which *"each axial protein is translocated via the fT3SS across the cytoplasmic membrane, diffuses down the central channel of the growing flagellar structure and assembles at the distal end"* — has been characterized in detail ([PMID: 35602071](https://pubmed.ncbi.nlm.nih.gov/35602071/)).

### Finding 3 — FlgG completes the rod during ordered basal-body assembly and is homologous to the hook protein FlgE

Flagellar assembly is strictly ordered and proceeds from the inside out. The proximal rod (FlgB/FlgC/FlgF) is laid down first, followed by the **distal rod (FlgG)**. Completion of the rod is an obligatory prerequisite for the subsequent steps: loading of the **FlgD hook cap** and then polymerization of the **FlgE hook**. Genetic evidence pins FlgG to this checkpoint. The scaffolding/cap protein FlgD is detectable in the basal bodies of many flagellar mutants, but it is **absent** from *flgB, flgD, flgG, and flgJ* mutant basal bodies — i.e., *"not at all in those from flgB, flgD, flgG, and flgJ mutants"* ([PMID: 8157595](https://pubmed.ncbi.nlm.nih.gov/8157595/)). Because a *flgG* mutant cannot complete the rod, FlgD cannot load and hook assembly cannot begin. This places FlgG at a defined, early position in the assembly hierarchy.

Consistent with FlgG bridging the rod to the hook at the rod–hook junction, sequence comparisons show that the hook protein **FlgE most strongly resembles the distal rod protein FlgG** (and the proximal hook-associated protein HAP1/FlgK): *"Hook protein most strongly resembled the distal rod protein (FlgG) and the proximal HAP (HAP1)"* ([PMID: 2193164](https://pubmed.ncbi.nlm.nih.gov/2193164/)). This structural kinship reflects the shared coiled-coil axial architecture of the rod and hook and explains why FlgG can form a seamless mechanical junction with the hook. A modern review of the hook protein FlgE explicitly discusses the *"similarities and differences between FlgE (hook) and FlgG (distal rod)"*, underscoring that these two proteins are the closely related building blocks flanking the rod–hook junction ([PMID: 36941455](https://pubmed.ncbi.nlm.nih.gov/36941455/)).

### Finding 4 — FlgG governs distal-rod length and, via gain-of-function *flgG\** mutants, triggers the type III secretion specificity switch

Beyond its static structural role, FlgG carries an intrinsic length-control ("molecular ruler") function for the distal rod. Distal-rod **gain-of-function** mutants — *flgG\** — produce *"filamentous rod structures"* instead of the normal fixed-length rod ([PMID: 19376867](https://pubmed.ncbi.nlm.nih.gov/19376867/)). This demonstrates that FlgG itself encodes information that terminates rod elongation at the correct length; when that control is disrupted, the rod grows abnormally long and filamentous.

Critically, these same *flgG\** mutations (like mutations in *flk*) cause **premature switching** of the flagellar type III secretion system, whereby *"the flagellar type III secretion system switches from secreting rod/hook-type to filament-type substrates"* ([PMID: 19376867](https://pubmed.ncbi.nlm.nih.gov/19376867/)). Normally, this substrate-specificity switch occurs only after the hook reaches its proper length; the export machinery then stops secreting rod/hook-type substrates (FlgB, FlgC, FlgF, FlgG, FlgE, FlgD) and begins secreting filament-type substrates (FliC/flagellin and the hook-associated proteins). The finding that FlgG status feeds into this switch ties the distal rod directly into the regulation of flagellar export order. In *flgG\** strains, deletion of *flgE* or *flgD* allowed filaments to grow directly on the elongated rod — further evidence that the switch had been thrown prematurely. Notably, the premature switch still required the hook-length control protein **FliK** and the rod-cap protein **FlgJ**, showing that FlgG acts within — not independently of — the established length-control/switching circuitry.

### Finding 5 — In *P. putida* KT2440, *flgG* (PP_4385) lies within the polar flagellar gene cluster under FleQ/σ⁵⁴ control

*Pseudomonas putida* KT2440 assembles **polar flagella**, and the genes for their biogenesis are organized in a single large chromosomal cluster spanning **PP4329–PP4397** ([PMID: 30338358](https://pubmed.ncbi.nlm.nih.gov/30338358/)). The target gene *flgG* (PP_4385) maps within this cluster, alongside the other structural, export, and regulatory genes of the flagellar system.

Expression of the cluster is governed by the master flagellar regulator **FleQ**. Deletion of *fleQ* — *"the gene encoding FleQ, the primary regulator of flagellar synthesis"* — yields non-motile, flagella-deficient cells ([PMID: 39570920](https://pubmed.ncbi.nlm.nih.gov/39570920/)). FleQ activates **σ⁵⁴ (σN)-dependent** flagellar promoters; in *P. putida*, the flagellar export-gate operon (*flhA–flhF–fleN–fliA*) is driven from σN-dependent promoters that are *activated by the flagellar regulator FleQ and negatively regulated by FleN* ([PMID: 30889223](https://pubmed.ncbi.nlm.nih.gov/30889223/)). Together with the antiactivator FleN and the second messenger **c-di-GMP**, FleQ coordinates the trade-off between flagellar motility and biofilm/adhesion programs. Thus, *flgG* is expressed as part of the FleQ/σ⁵⁴ regulon, and its product is exported by the same fT3SS export gate (e.g., FlhA) that translocates all other axial proteins.

### Finding 6 — Q88ER8 is a high-confidence FlgG ortholog (56.8 % identity to *Salmonella* FlgG)

To confirm the identity of the *P. putida* target directly, a Needleman–Wunsch global alignment was performed between Q88ER8 (261 aa) and the functionally characterized *Salmonella* Typhimurium FlgG (P0A1J3 / FLGG_SALTY, 260 aa). The alignment yielded **147/259 identical positions = 56.8 % identity, 70.3 % similarity**, with only 3 gaps across a 262-column alignment. This identity is far above the ~30 % "twilight zone" of homology detection, and the near-absence of insertions/deletions indicates identical domain architecture and chain length. Conservation is concentrated in the N- and C-terminal coiled-coil (D0) segments that build the axial core, and the target retains the diagnostic C-terminal axial-protein signature (`EELVNMI(T)TQRAYE(M)NSK...DQML`). This same conserved-terminus principle underlies cross-species FlgG identification: the *Caulobacter crescentus* FlgG homolog was recognized because *"the N and C termini of the Salmonella typhimurium flagellar axial proteins... share a high degree of sequence identity with the FlgF and FlgG rod proteins"* even in this distantly related organism ([PMID: 1474584](https://pubmed.ncbi.nlm.nih.gov/1474584/)). The chain length (~261 aa) is also consistent with FlgG and clearly distinct from the much larger (~403-aa) hook protein FlgE.

### Finding 7 — Q88ER8 is specifically a distal-rod (FlgG-type) protein, not a proximal-rod (FlgF-type) protein

Because the four rod paralogs (FlgB/FlgC/FlgF/FlgG) share a common fold, an ortholog assignment must discriminate between subtypes. Global alignments resolved this cleanly: the *P. putida* target is **56.8 % identical to *Salmonella* FlgG** (distal rod) but only **31.4 % identical to *Salmonella* FlgF** (proximal rod, P16323). For calibration, *Salmonella* FlgG itself is only 31.7 % identical to *Salmonella* FlgF — i.e., ~31 % represents the baseline family-level similarity between distinct rod paralogs. The target's markedly higher, gap-free match to FlgG (57 %) versus the family-baseline match to FlgF (31 %) assigns Q88ER8 **unambiguously to the FlgG (distal-rod) subtype**. This distinction matters functionally because the distal and proximal rod proteins are not interchangeable: FlgG forms the long, ~26-subunit load-bearing shaft, whereas FlgF is a short ~6-subunit proximal adaptor ([PMID: 2181149](https://pubmed.ncbi.nlm.nih.gov/2181149/)). Both *Bacillus subtilis* and *Caulobacter* comparative genomics reinforce this canonical FlgF-then-FlgG (proximal-then-distal) rod organization across diverse bacteria ([PMID: 1905667](https://pubmed.ncbi.nlm.nih.gov/1905667/); [PMID: 1474584](https://pubmed.ncbi.nlm.nih.gov/1474584/)).

---

## Mechanistic Model / Interpretation

FlgG's function is best understood by placing it within the architecture and assembly sequence of the flagellar basal body. The following schematic (based on the canonical *Salmonella* model, which applies to the *P. putida* ortholog) locates FlgG in the cell envelope:

```
   EXTRACELLULAR
        │  Filament (FliC)         ← propeller
        │  ────────────
        │  Hook (FlgE)             ← universal joint
   ═════╪═════  Outer membrane ─── L ring (FlgH)
        │  ┌── DISTAL ROD (FlgG, ~26 subunits)   ← FlgG: distal drive shaft
   ─────┼──┤    Peptidoglycan ──── P ring (FlgI)
        │  └── PROXIMAL ROD (FlgB/FlgC/FlgF, ~6 each)
   ═════╪═════  Inner membrane ─── MS ring (FliF)
        │  C ring (FliG/M/N) + fT3SS export gate + motor
   CYTOPLASM
```

**Structural role (primary function).** FlgG is a purely structural axial protein — not an enzyme, transporter, or signaling molecule. Its "substrate" is mechanical torque. Roughly 26 FlgG subunits polymerize into the distal rod, a rigid helical shaft whose job is to transmit the rotation generated by the cytoplasmic motor (stator–rotor interactions at the C ring) across the periplasm to the hook and filament ([PMID: 2129540](https://pubmed.ncbi.nlm.nih.gov/2129540/); [PMID: 2181149](https://pubmed.ncbi.nlm.nih.gov/2181149/)). The distal rod must be rigid to transmit torque without buckling, and it passes through the bushing formed by the P and L rings, which allow it to rotate freely against the peptidoglycan and outer membrane.

**Localization.** FlgG functions in the **periplasm**, specifically in the distal-rod zone enclosed by the P ring (peptidoglycan) and L ring (outer membrane), just proximal to the rod–hook junction ([PMID: 2129540](https://pubmed.ncbi.nlm.nih.gov/2129540/)). It reaches this location by fT3SS-mediated export through the central channel, folding and assembling only at the distal tip.

**Assembly logic and length control.** FlgG is the last-built rod component. Its assembly completes the rod and licenses the next steps — FlgD cap loading and FlgE hook polymerization ([PMID: 8157595](https://pubmed.ncbi.nlm.nih.gov/8157595/)). FlgG also acts as a molecular ruler that terminates rod growth at a defined length; disruption of this control (*flgG\**) yields elongated filamentous rods ([PMID: 19376867](https://pubmed.ncbi.nlm.nih.gov/19376867/)).

**Coupling to export regulation.** The distal rod is a node in the fT3SS substrate-specificity switch. *flgG\** mutations prematurely flip the export machine from rod/hook-type to filament-type secretion — but only in cooperation with FliK and FlgJ ([PMID: 19376867](https://pubmed.ncbi.nlm.nih.gov/19376867/)). This connects the physical completion of the rod to the temporal program of flagellar gene product export.

The following table summarizes how FlgG contrasts with its family members:

| Protein | Role | Location | Copies per flagellum | Export route |
|---|---|---|---|---|
| FlgB | Proximal rod | Periplasm (inner) | ~6 | fT3SS |
| FlgC | Proximal rod | Periplasm (inner) | ~6 | fT3SS |
| FlgF | Proximal rod | Periplasm (inner) | ~6 | fT3SS |
| **FlgG** | **Distal rod (drive shaft)** | **Periplasm, within L/P rings** | **~26** | **fT3SS** |
| FlgE | Hook | Extracellular | ~120 | fT3SS |

**Regulatory context in *P. putida*.** In KT2440, *flgG* (PP_4385) is transcribed as part of the polar-flagellar cluster (PP4329–PP4397) under the FleQ/σ⁵⁴ regulatory hierarchy, which integrates c-di-GMP signaling to balance motility against biofilm formation ([PMID: 30338358](https://pubmed.ncbi.nlm.nih.gov/30338358/); [PMID: 39570920](https://pubmed.ncbi.nlm.nih.gov/39570920/); [PMID: 30889223](https://pubmed.ncbi.nlm.nih.gov/30889223/)).

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|---|---|---|
| [2129540](https://pubmed.ncbi.nlm.nih.gov/2129540/) | *FlgB, FlgC, FlgF and FlgG: a family of structurally related basal-body rod proteins (Salmonella)* | Defines the four-protein rod family; localizes FlgG to the distal rod within the L/P rings; states the drive-shaft function; notes rod proteins lack Sec signal peptides. Foundational for Findings 1 & 2. |
| [2181149](https://pubmed.ncbi.nlm.nih.gov/2181149/) | *Stoichiometric analysis of the flagellar hook-basal-body complex* | Provides measured subunit counts: FlgG ~26 vs. FlgB/C/F ~6. Core evidence for Finding 2 and the distal/proximal distinction (Finding 7). |
| [8157595](https://pubmed.ncbi.nlm.nih.gov/8157595/) | *FlgD is a scaffolding protein needed for hook assembly* | Shows FlgD is absent in *flgG* mutant basal bodies — rod completion by FlgG is prerequisite for hook assembly. Supports Finding 3. |
| [2193164](https://pubmed.ncbi.nlm.nih.gov/2193164/) | *Flagellar hook and hook-associated proteins* | Establishes that hook protein FlgE most closely resembles FlgG, consistent with the rod–hook junction. Supports Finding 3. |
| [19376867](https://pubmed.ncbi.nlm.nih.gov/19376867/) | *Mutations affecting the T3SS specificity switch (flk, flgG, flhA, flhE)* | Shows *flgG\** gain-of-function alleles produce filamentous rods and prematurely trigger the rod/hook→filament secretion switch. Core evidence for Finding 4. |
| [36941455](https://pubmed.ncbi.nlm.nih.gov/36941455/) | *Structure and function of the flagellar hook FlgE (review)* | Modern review contrasting FlgE (hook) with FlgG (distal rod), reinforcing their close structural relationship. Supports Finding 3. |
| [1474584](https://pubmed.ncbi.nlm.nih.gov/1474584/) | *Caulobacter basal-body rod/ring genes* | Independent ortholog: identifies FlgF (proximal) and FlgG (distal) rod proteins via conserved termini; σ⁵⁴ regulation. Supports Findings 6 & 7 and the regulatory model. |
| [1905667](https://pubmed.ncbi.nlm.nih.gov/1905667/) | *Bacillus subtilis flgB, flgC, flgG, fliE, fliF sequences* | Confirms FlgB/FlgC/FlgG are conserved rod components across Gram-positive bacteria. Supports Findings 1 & 7. |
| [30338358](https://pubmed.ncbi.nlm.nih.gov/30338358/) | *Deletion of flagella/pili genes in P. putida* | Defines the P. putida flagellar gene cluster PP4329–PP4397 containing flgG (PP_4385). Supports Finding 5. |
| [39570920](https://pubmed.ncbi.nlm.nih.gov/39570920/) | *fleQ deficiency in P. putida* | Identifies FleQ as the master regulator of P. putida flagellar synthesis; ΔfleQ is non-motile. Supports Finding 5. |
| [30889223](https://pubmed.ncbi.nlm.nih.gov/30889223/) | *flhF and fleN in P. putida* | Shows P. putida flagellar promoters are σN-dependent, FleQ-activated, FleN/c-di-GMP-modulated. Supports Finding 5. |
| [35602071](https://pubmed.ncbi.nlm.nih.gov/35602071/) | *Flagellar ATPase complex for assembly* | Describes fT3SS export of axial proteins across the membrane and diffusion to the distal tip — the mechanism by which FlgG is exported. Supports Finding 2. |
| [30250776](https://pubmed.ncbi.nlm.nih.gov/30250776/) | *Energy transduction in flagellar T3 protein export* | Details fT3SS-driven axial protein export, the pathway for FlgG translocation. Supports Finding 2. |

Both direct sequence evidence (Findings 6 & 7, generated in this investigation) and the extensive ortholog literature converge on the same conclusion. No paper reviewed contradicts the distal-rod assignment; the *P. putida*-specific literature ([PMID: 30338358](https://pubmed.ncbi.nlm.nih.gov/30338358/), [39570920](https://pubmed.ncbi.nlm.nih.gov/39570920/), [30889223](https://pubmed.ncbi.nlm.nih.gov/30889223/)) situates *flgG* in the correct genomic and regulatory context but does not itself dissect FlgG structure — hence the reliance on well-characterized orthologs, justified by the strong, gap-free sequence conservation.

---

## Limitations and Knowledge Gaps

1. **No *P. putida*-specific structural or mutational study of FlgG.** The functional annotation is transferred from *Salmonella*, *Bacillus*, and *Caulobacter* orthologs. While the 56.8 % identity and conserved axial termini make this transfer highly reliable, no experiment has directly demonstrated the distal-rod localization, ~26-subunit stoichiometry, or drive-shaft function of the *P. putida* protein itself.

2. **Stoichiometry and length values are from *Salmonella*.** The ~26-subunit count and rod dimensions may differ modestly in *P. putida*, whose polar flagellum and cell-envelope architecture differ from *Salmonella*'s peritrichous system. Species-specific differences in basal-body organization have been noted (e.g., in *B. subtilis*, [PMID: 1905667](https://pubmed.ncbi.nlm.nih.gov/1905667/)).

3. **The length-control / secretion-switch role (*flgG\**) has not been tested in *P. putida*.** Whether FlgG contributes to the substrate-specificity switch identically in *P. putida* — which uses a distinct FleQ/σ⁵⁴/c-di-GMP regulatory layer and FlhF/FleN for polar placement — remains an inference.

4. **No high-resolution structure of Q88ER8.** An experimental or AlphaFold structure of the *P. putida* FlgG was not analyzed in this investigation; the D0 coiled-coil core architecture is inferred from homology and domain signatures rather than a solved model.

5. **Interaction partners not experimentally mapped in *P. putida*.** The predicted contacts with FlgF (proximal rod), FlgE (hook), and the P/L rings (FlgI/FlgH) are based on the *Salmonella* model.

---

## Proposed Follow-up Experiments / Actions

1. **Targeted mutagenesis in *P. putida* KT2440.** Construct a clean *flgG* (PP_4385) deletion and test for loss of swimming motility (soft-agar assay) and loss of assembled flagella (electron microscopy / immunostaining). Complement in *trans* to confirm specificity. This would directly validate the essential structural role.

2. **Cryo-EM of the *P. putida* basal body.** Purify hook-basal-body complexes and determine the distal-rod position and FlgG subunit count, testing whether the ~26-subunit *Salmonella* stoichiometry holds for a polar flagellum.

3. **Construct and characterize *P. putida flgG\** gain-of-function alleles** analogous to the *Salmonella* mutants ([PMID: 19376867](https://pubmed.ncbi.nlm.nih.gov/19376867/)) to test whether distal-rod length control and the fT3SS substrate-specificity switch are conserved in the FleQ/σ⁵⁴/c-di-GMP regulatory context.

4. **AlphaFold / AlphaFold-Multimer modeling** of Q88ER8 alone and in complex with *P. putida* FlgF and FlgE to confirm the D0 coiled-coil drive-shaft architecture and the rod–rod and rod–hook junction interfaces in silico.

5. **Transcriptional confirmation.** Map the *flgG* promoter/operon structure within PP4329–PP4397 and verify FleQ/σ⁵⁴ dependence directly (e.g., reporter fusions in wild-type vs. Δ*fleQ*), extending the operon analysis of [PMID: 30889223](https://pubmed.ncbi.nlm.nih.gov/30889223/).

6. **Motility–biofilm trade-off.** Given the FleQ/c-di-GMP node coupling motility and adhesion, quantify how *flgG* loss reshapes the motility–biofilm balance in *P. putida*, relevant to its use as an industrial/environmental chassis.

---

## Conclusion

The gene symbol *flgG* is **not** ambiguous for this target: sequence, domain, genomic-context, and regulatory evidence all consistently identify Q88ER8 (PP_4385) as the genuine **distal flagellar basal-body rod protein FlgG** of *Pseudomonas putida* KT2440. It is a non-enzymatic structural protein that polymerizes (~26 copies) into the distal rod — the rigid periplasmic drive shaft enclosed by the P and L rings — which transmits motor torque to the hook and filament to power swimming motility. It is exported by the flagellar type III secretion system, completes the rod during ordered basal-body assembly, sets distal-rod length, and thereby contributes to the checkpoint that switches flagellar protein export from rod/hook-type to filament-type substrates. In *P. putida*, it is encoded in the polar-flagellar cluster (PP4329–PP4397) under FleQ/σ⁵⁴ control.


## Artifacts

- [OpenScientist final report](flgG-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](flgG-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:2129540
2. PMID:2181149
3. PMID:35602071
4. PMID:8157595
5. PMID:2193164
6. PMID:36941455
7. PMID:19376867
8. PMID:30338358
9. PMID:39570920
10. PMID:30889223
11. PMID:1474584
12. PMID:1905667