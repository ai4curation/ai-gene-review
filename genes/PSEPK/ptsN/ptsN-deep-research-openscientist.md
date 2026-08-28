---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-11T02:37:41.265248'
end_time: '2026-08-11T02:57:31.380928'
duration_seconds: 1190.12
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ptsN
  gene_symbol: ptsN
  uniprot_accession: Q88PA0
  protein_description: 'SubName: Full=Phosphotransferase system enzyme IIA, regulation
    of potassium transport {ECO:0000313|EMBL:AAN66575.1};'
  gene_info: Name=ptsN {ECO:0000313|EMBL:AAN66575.1}; OrderedLocusNames=PP_0950 {ECO:0000313|EMBL:AAN66575.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: PTrfase/Anion_transptr. (IPR016152); PTS_EIIA_type-2_dom. (IPR002178);
    PTS_Nitro_regul. (IPR006320); PTS_SugarTrans_NitroReg. (IPR051541); PTS_EIIA_2
    (PF00359)
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
citation_count: 11
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ptsN-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ptsN-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88PA0
- **Protein Description:** SubName: Full=Phosphotransferase system enzyme IIA, regulation of potassium transport {ECO:0000313|EMBL:AAN66575.1};
- **Gene Information:** Name=ptsN {ECO:0000313|EMBL:AAN66575.1}; OrderedLocusNames=PP_0950 {ECO:0000313|EMBL:AAN66575.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** PTrfase/Anion_transptr. (IPR016152); PTS_EIIA_type-2_dom. (IPR002178); PTS_Nitro_regul. (IPR006320); PTS_SugarTrans_NitroReg. (IPR051541); PTS_EIIA_2 (PF00359)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ptsN" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ptsN' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ptsN** (gene ID: ptsN, UniProt: Q88PA0) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *ptsN* (EIIA^Ntr^, PP_0950, UniProt Q88PA0) in *Pseudomonas putida* KT2440

## Summary

The gene **ptsN** (ordered locus **PP_0950**; UniProt accession **Q88PA0**) of *Pseudomonas putida* KT2440 encodes **EIIA^Ntr^**, the terminal phosphoacceptor of the **nitrogen-related phosphotransferase system (PTS^Ntr^)**. Despite its "phosphotransferase system enzyme IIA" annotation and its homology to the sugar-transporting EIIA proteins of the classical carbohydrate PTS, PtsN is **not a transporter and does not catalyze sugar uptake or a metabolic reaction**. Instead, it is a soluble, cytoplasmic, **phosphorylation-state-dependent protein–protein interaction module** — a regulatory adaptor — that couples the cell's carbon/nitrogen/energy status to a small set of specific downstream targets. This identity is unambiguous: the PTS^Ntr^ in *P. putida* KT2440 is explicitly "not related to sugar transport but believed to rule the metabolic balance of carbon vs. nitrogen," and the PTS^Ntr^ as a class "lacks membrane-bound components and functions exclusively in a regulatory capacity" ([PMID: 21236318](https://pubmed.ncbi.nlm.nih.gov/21236318/); [PMID: 25701731](https://pubmed.ncbi.nlm.nih.gov/25701731/)).

Mechanistically, PtsN sits at the bottom of a dedicated phosphorelay. In vivo in KT2440, phosphoryl groups flow **PEP → EI^Ntr^ (PtsP) → NPr (PtsO) → EIIA^Ntr^ (PtsN)**, landing on a conserved active-site histidine (**His68**, embedded in an H-C-R motif that matches solved IIA^Ntr^ structures and the *E. coli* IIA^Ntr^ fold, PDB 1A6J) ([PMID: 18296519](https://pubmed.ncbi.nlm.nih.gov/18296519/); [PMID: 16092953](https://pubmed.ncbi.nlm.nih.gov/16092953/)). The phosphorylation state of PtsN acts as a switch: the phosphorylated form (PtsN∼P) and the unphosphorylated form each engage distinct partners with distinct functional consequences. The two best-defined primary functions of *P. putida* PtsN are (1) **regulation of potassium transport**, achieved by direct binding to the membrane sensor kinase **KdpD** of the KdpD/KdpE two-component system, thereby controlling transcription of the *kdpFABC* high-affinity K⁺ pump; and (2) **inhibition of the pyruvate dehydrogenase complex (PDH, E1 subunit AceE)** by the unphosphorylated form, positioning PtsN at the carbon/nitrogen metabolic node.

Functionally, PtsN carries out its work **in the cytoplasm and at the cytoplasmic face of the inner membrane**, where it toggles between activating/repressing signal-transduction complexes (KdpD, and by homology PhoR) and directly modulating a central metabolic enzyme (PDH) and a K⁺ transporter (TrkA, established in *E. coli*). It is a hub that integrates PTS-derived metabolic signals — including cross-talk from the fructose PTS — into potassium homeostasis, phosphate signaling, and carbon flux control.

---

## Key Findings

### Finding 1 — PtsN is EIIA^Ntr^, the terminal cytoplasmic phosphoacceptor of the PTS^Ntr^

The domain architecture of Q88PA0 unambiguously identifies it as an **EIIA of the mannitol/fructose (type-2) class dedicated to nitrogen regulation**: it carries the Pfam PF00359 (PTS_EIIA_2) domain and the InterPro signatures IPR002178 (PTS_EIIA_type-2) and IPR006320 (PTS_Nitro_regul). Unlike the sugar-transporting arms of the classical carbohydrate PTS, the PTS^Ntr^ **has no membrane-bound EIIB/EIIC components and transports no sugars** — it is a purely regulatory phosphorelay. As stated for the family, "most Proteobacteria possess the so-called nitrogen PTS (PTS^Ntr^) that transfers a phosphate group from phosphoenolpyruvate (PEP) over enzyme I^Ntr^ (EI^Ntr^) and NPr to enzyme IIA^Ntr^ (EIIA^Ntr^). The PTS^Ntr^ lacks membrane-bound components and functions exclusively in a regulatory capacity" ([PMID: 25701731](https://pubmed.ncbi.nlm.nih.gov/25701731/)). In the exact target organism, the system is described as "a variant of the phosphoenolpyruvate-carbohydrate phosphotransferase system (PTS^Ntr^), which is not related to sugar transport but believed to rule the metabolic balance of carbon vs. nitrogen" ([PMID: 21236318](https://pubmed.ncbi.nlm.nih.gov/21236318/)). PtsN is the **last (terminal) component** of this relay, and therefore the effector that hands the metabolic signal off to downstream targets.

### Finding 2 — PtsN represses the *kdpFABC* K⁺ transporter via direct interaction with the sensor kinase KdpD

A genome-wide survey of PtsN-regulated genes in *P. putida* KT2440 found that **the *kdpFABC* operon** — encoding the high-affinity, ATP-dependent K⁺ transporter — was **the transcriptional target most strongly affected** by PtsN. PtsN represses *kdpFp* promoter activity, and this repression is "mainly PtsN∼P," i.e. attributable to the **phosphorylated form**, and is dependent on the external K⁺ concentration. Crucially, the mechanism is direct: "Bacterial two-hybrid assays demonstrated that *kdpFp* regulation is implemented through direct interaction of the PtsN protein with the sensor kinase KdpD" ([PMID: 26224366](https://pubmed.ncbi.nlm.nih.gov/26224366/)). Both non-phospho and phospho-mimetic PtsN variants were capable of binding KdpD, indicating that binding is constitutive but the functional output is phospho-tuned. This finding establishes potassium transport control as a **primary, experimentally proven function of PtsN in the target organism**, executed by physical contact with a membrane-embedded histidine kinase. The conservation of this logic is supported by an independent proteobacterial system: in *Rhizobium leguminosarum* the PTS^Ntr^ "also regulates K⁺ homeostasis by transcriptional activation of the high-affinity ATP-dependent K⁺ transporter KdpABC ... [via] direct interaction of a two-component sensor regulator pair KdpDE with unphosphorylated EIIA^Ntr^" ([PMID: 22340847](https://pubmed.ncbi.nlm.nih.gov/22340847/)). Note the sign of the regulation differs between organisms (activation in *Rhizobium* vs. repression by PtsN∼P in *P. putida*), which points to species-specific tuning of a conserved mechanism.

### Finding 3 — Unphosphorylated PtsN binds and inhibits pyruvate dehydrogenase (AceE) at the C/N node

Using **co-immunoprecipitation of epitope-tagged PtsN from *P. putida* KT2440 soluble extracts followed by mass spectrometry**, the **E1 subunit of the pyruvate dehydrogenase complex (the *aceE* gene product)** was identified as a major interaction partner of EIIA^Ntr^: "The E1 subunit of the pyruvate dehydrogenase (PDH) complex, the product of the *aceE* gene, was identified as a major interaction partner of EIIA^Ntr^" ([PMID: 21236318](https://pubmed.ncbi.nlm.nih.gov/21236318/)). Enzyme-activity assays in isogenic *ptsN*⁺/*ptsN*⁻ strains, together with analysis of phospho-mimetic variants, established the functional consequence and the responsible species: "EIIA^Ntr^ down-regulates PDH activity. Both genetic and biochemical evidence revealed that the **non-phosphorylated form of PtsN** is the protein species that inhibits PDH" ([PMID: 21236318](https://pubmed.ncbi.nlm.nih.gov/21236318/)). Fluorescent-fusion confocal microscopy showed cytoplasmic co-localization of PtsN and AceE. This is a mechanistically precise, direct-interaction finding placing PtsN at the **pyruvate → acetyl-CoA junction** — the entry point of carbon into the TCA cycle — and demonstrates that PtsN's outputs are not limited to signal-transduction cascades but include direct enzymatic modulation. Importantly, the phospho-state dependence is **opposite** to that of the *kdpFABC*/KdpD output (unphosphorylated PtsN inhibits PDH; phosphorylated PtsN∼P represses *kdpFABC*), which is the hallmark of a bifunctional switch that partitions signals by phosphorylation state.

### Finding 4 — Structural and bioinformatic evidence for the EIIA type-2 fold and a His68 phospho-acceptor

The 154-residue Q88PA0 sequence contains the **diagnostic EIIA type-2 (mannitol-family) active-site loop**, …FGNGIAIP-**H68**-C-**R70**-LEG…, placing a histidine (His68) immediately adjacent to an arginine (Arg70). This is the **canonical His(phospho-acceptor)/Arg(phosphate-coordinating) pair** of nitrogen-regulatory IIA proteins. The arrangement mirrors experimentally determined IIA^Ntr^ structures: in the *Neisseria meningitidis* IIA^Ntr^ crystal structure, "the position of the phosphoryl acceptor histidine residue (H67) is conserved. The orientation of an adjacent arginine residue (R69) suggests that it may also be involved in coordinating the phosphate group," and that structure was solved by molecular replacement from *E. coli* IIA^Ntr^ (PDB 1A6J), sharing the mannitol-family EIIA fold and an HPr/NPr-like docking surface ([PMID: 16092953](https://pubmed.ncbi.nlm.nih.gov/16092953/)). The Pfam/InterPro assignments (PF00359; IPR002178; IPR006320) independently place Q88PA0 in this family. Together this provides **structural rationale for the biochemistry**: His68 is the residue whose phosphorylation state toggles PtsN's downstream interactions, and the conserved Arg70 stabilizes the phosphoryl group during transfer from NPr.

### Finding 5 — In vivo phosphoryl flow is PEP → PtsP → PtsO → PtsN, with cross-talk from the fructose PTS (FruB)

*P. putida* KT2440 encodes only **five PTS proteins**: FruA/FruB (the fructose uptake system) and the sugar-independent regulatory branch PtsP (EI^Ntr^), PtsO (NPr), and PtsN (EIIA^Ntr^). By monitoring the **in vivo phosphorylation state of EIIA^Ntr^** across genetic backgrounds and carbon sources, PEP was shown to be the phosphoryl donor and the main route established: "the source of phosphate available to the system is PEP and that the primary flow of phosphate through the N/C-sensing PTS proceeds from PEP to EI^Ntr^ to NPr to EIIA^Ntr^" ([PMID: 18296519](https://pubmed.ncbi.nlm.nih.gov/18296519/)). The same study revealed **cross-talk from the fructose PTS**: "in the presence of fructose, unlike in the presence of succinate, EIIA^Ntr^ can be phosphorylated in a *ptsP* strain but not in a *ptsP fruB* double mutant. This result revealed that the fructose transport system has the ability to cross talk in vivo with the N-related PTS branch" ([PMID: 18296519](https://pubmed.ncbi.nlm.nih.gov/18296519/)). This means PtsN's phosphorylation state — and therefore its regulatory output — integrates not only the PEP/pyruvate ratio (a proxy for glycolytic flux and C/N balance) but also the presence of a specific PTS sugar (fructose) via FruB. The phosphorylation state of PtsN is thus a genuine metabolic sensor input.

### Finding 6 — EIIA^Ntr^ is a phospho-state-dependent accessory regulator of membrane sensor kinases (KdpD, PhoR) and the K⁺ transporter TrkA

The mechanistic paradigm for the family — worked out in *E. coli*, to which *P. putida* PtsN belongs by sequence and fold — shows EIIA^Ntr^ acting as a **modular accessory regulator of two-component signaling and of a K⁺ transporter**, with the phosphorylation state selecting the target and outcome:

- **TrkA (low-affinity K⁺ transporter):** dephosphorylated EIIA^Ntr^ "interacts with and regulates the *Escherichia coli* K⁺ transporter TrkA" ([PMID: 17289841](https://pubmed.ncbi.nlm.nih.gov/17289841/)).
- **KdpD (sensor kinase):** "IIA^Ntr^ interacts with sensor kinase KdpD and stimulates kinase activity, resulting in increased levels of phosphorylated response regulator KdpE. The data suggest that exclusively dephosphorylated IIA^Ntr^ binds and activates KdpD" ([PMID: 19400808](https://pubmed.ncbi.nlm.nih.gov/19400808/)).
- **PhoR (phosphate-sensing kinase):** "EIIA^Ntr^ is an accessory protein that modulates the activities of two distinct sensor kinases, KdpD and PhoR, in *E. coli*" ([PMID: 22812494](https://pubmed.ncbi.nlm.nih.gov/22812494/)), increasing phospho-PhoB and modulating the *pho* regulon.

Because the carbon source controls the PTS phosphorylation state (e.g., glucose drives dephospho-EIIA^Ntr^), K⁺ uptake and phosphate signaling are thereby **linked to carbon metabolism** ([PMID: 19400808](https://pubmed.ncbi.nlm.nih.gov/19400808/)). In *P. putida* specifically, the direct KdpD interaction is experimentally confirmed ([PMID: 26224366](https://pubmed.ncbi.nlm.nih.gov/26224366/)), with the caveat that the reported net effect there is *repression* of *kdpFABC* by PtsN∼P — species-specific tuning of a conserved accessory-regulator role.

### Finding 7 — Broader (pleiotropic) regulatory footprint that clarifies the precise role

Across proteobacteria, EIIA^Ntr^ has been implicated in "potassium homeostasis, phosphate starvation, nitrogen metabolism, carbon metabolism, regulation of ABC transporters and poly-β-hydroxybutyrate accumulation" ([PMID: 25701731](https://pubmed.ncbi.nlm.nih.gov/25701731/)). In *E. coli*, EIIA^Ntr^ "controls sigma factor selectivity by regulating the intracellular K⁺ level" ([PMID: 21143318](https://pubmed.ncbi.nlm.nih.gov/21143318/)) — a direct downstream consequence of its K⁺-transport control, linking PtsN to the σ⁷⁰/σ^S^ balance of global transcription. In *P. putida*, EIIA^Ntr^ participates in glucose-mediated downregulation of the *Pu* promoter of the TOL (m-xylene) catabolic operon, and the PTS^Ntr^ inhibits conjugative uptake of IncP-9 plasmids. These are not independent "primary functions" so much as **manifestations of the same core mechanism** — a phospho-state switch that sets intracellular K⁺ and gates specific signal-transduction and metabolic complexes — propagating into transcriptional and physiological outputs.

---

## Mechanistic Model / Interpretation

PtsN is best understood as a **cytoplasmic phospho-switch adaptor**. Its single covalent modification (phosphorylation of His68) is written by the upstream relay and read out as a change in which partners it engages and how.

### The phosphorelay (signal input)

```
      PEP  ─────►  EI^Ntr (PtsP)  ─────►  NPr (PtsO)  ─────►  EIIA^Ntr (PtsN, His68)
   (glycolytic                                                        │
    intermediate)                                                     │  phospho-state = SIGNAL
                                                                      ▼
   fructose ──► FruB (fructose PTS) ─── cross-talk ──►  PtsN∼P  ⇄  PtsN
                                                        (His68~P)   (His68)
```

The phosphorylation state of PtsN reflects the **PEP:pyruvate ratio** (and thus glycolytic flux / C:N balance) plus a specific input from **fructose** via FruB cross-talk ([PMID: 18296519](https://pubmed.ncbi.nlm.nih.gov/18296519/)).

### The outputs (signal readout) — a bifunctional switch

| PtsN species | Target | Location | Functional consequence | Evidence |
|---|---|---|---|---|
| **PtsN∼P** (phospho, His68~P) | KdpD sensor kinase | inner membrane (cytoplasmic face) | Represses *kdpFABC* K⁺ pump transcription in *P. putida* (K⁺-dependent) | [PMID: 26224366](https://pubmed.ncbi.nlm.nih.gov/26224366/) |
| **PtsN** (dephospho) | AceE (PDH E1) | cytoplasm | Inhibits pyruvate dehydrogenase activity | [PMID: 21236318](https://pubmed.ncbi.nlm.nih.gov/21236318/) |
| **PtsN** (dephospho) | TrkA K⁺ transporter | inner membrane | Inhibits low-affinity K⁺ uptake (*E. coli* paradigm) | [PMID: 17289841](https://pubmed.ncbi.nlm.nih.gov/17289841/) |
| **PtsN** (dephospho) | KdpD sensor kinase | inner membrane | Stimulates KdpD → phospho-KdpE → activates *kdpFABC* (*E. coli* paradigm) | [PMID: 19400808](https://pubmed.ncbi.nlm.nih.gov/19400808/) |
| **PtsN** | PhoR sensor kinase | inner membrane | Modulates phosphate-starvation *pho* regulon (*E. coli*) | [PMID: 22812494](https://pubmed.ncbi.nlm.nih.gov/22812494/) |

Two coherent principles emerge:

1. **Location:** PtsN is soluble and cytoplasmic, but its most important actions occur **at the cytoplasmic face of the inner membrane**, where it docks onto integral membrane histidine kinases (KdpD, PhoR) and a membrane K⁺ transporter (TrkA), plus one soluble cytoplasmic metabolic enzyme (PDH/AceE).

2. **Logic:** The switch is **antagonistically wired by phospho-state**. Dephospho-PtsN (favored under carbon-replete, high-glycolytic-flux conditions) inhibits PDH and, in the paradigm organism, engages the K⁺/phosphate kinases; phospho-PtsN (favored under carbon limitation) releases these. In *P. putida* the *kdpFABC* output is repressed by PtsN∼P, an organism-specific inversion of sign relative to *E. coli*/*Rhizobium*, but the underlying mechanism — direct binding to KdpD — is conserved. The net physiological effect is to **coordinate K⁺ uptake, phosphate signaling, and carbon entry into the TCA cycle with the cell's PEP-reported energy/carbon status**, which further propagates (via intracellular K⁺) to σ-factor selectivity and global transcription ([PMID: 21143318](https://pubmed.ncbi.nlm.nih.gov/21143318/)).

### Primary function statement

- **Enzyme/transporter?** No. PtsN catalyzes no metabolic reaction and transports no substrate. The only chemistry it participates in is reversible **His-phosphotransfer** at His68, received from NPr (PtsO).
- **Adaptor/signaling role?** Yes — this is the primary function. PtsN is a **phosphorylation-controlled protein–protein interaction module** that gates the activities of membrane sensor kinases (KdpD, PhoR), a K⁺ transporter (TrkA), and the pyruvate dehydrogenase complex (AceE).
- **Pathway:** It is the terminal effector of the **PTS^Ntr^** (nitrogen-related PTS), integrating carbon/nitrogen/energy status and feeding into potassium homeostasis, phosphate-starvation signaling, and central carbon flux.

---

## Evidence Base

| PMID | Title (abbrev.) | Organism | How it supports the annotation |
|---|---|---|---|
| [21236318](https://pubmed.ncbi.nlm.nih.gov/21236318/) | *EIIA^Ntr^ interplay with pyruvate dehydrogenase* | *P. putida* KT2440 | **Primary target-organism evidence**: PTS^Ntr^ is non-sugar, C/N-balancing; identifies AceE as direct partner; unphospho-PtsN inhibits PDH |
| [26224366](https://pubmed.ncbi.nlm.nih.gov/26224366/) | *PtsN interplay with sensor kinase KdpD* | *P. putida* | **Primary target-organism evidence**: PtsN∼P represses *kdpFABC* via direct KdpD binding (two-hybrid) |
| [18296519](https://pubmed.ncbi.nlm.nih.gov/18296519/) | *Cross-talk between N-related and fructose PTS branches* | *P. putida* | In vivo phospho-flow PEP→PtsP→PtsO→PtsN; FruB cross-talk |
| [25701731](https://pubmed.ncbi.nlm.nih.gov/25701731/) | *Dephospho-NPr in envelope stress response* | *E. coli* / review context | Defines PTS^Ntr^ relay order; PtsN is terminal, membrane-free, regulatory; lists EIIA^Ntr^ target processes |
| [16092953](https://pubmed.ncbi.nlm.nih.gov/16092953/) | *Crystal structure of IIA^Ntr^ from N. meningitidis* | *N. meningitidis* | Structural basis: conserved His phospho-acceptor + adjacent Arg; mannitol-family fold; PDB 1A6J template |
| [17289841](https://pubmed.ncbi.nlm.nih.gov/17289841/) | *EIIA^Ntr^ regulates TrkA* | *E. coli* | Dephospho-EIIA^Ntr^ binds/inhibits TrkA K⁺ transporter |
| [19400808](https://pubmed.ncbi.nlm.nih.gov/19400808/) | *IIA^Ntr^ stimulates KdpD kinase* | *E. coli* | Dephospho-IIA^Ntr^ stimulates KdpD→KdpE→*kdpFABC*; links K⁺ to carbon |
| [22812494](https://pubmed.ncbi.nlm.nih.gov/22812494/) | *EIIA^Ntr^ modulates PhoR* | *E. coli* | EIIA^Ntr^ as accessory regulator of two sensor kinases (KdpD, PhoR) |
| [22340847](https://pubmed.ncbi.nlm.nih.gov/22340847/) | *PTS^Ntr^ regulates ABC transporters* | *R. leguminosarum* | Independent proteobacterial confirmation: EIIA^Ntr^–KdpDE controls KdpABC |
| [21143318](https://pubmed.ncbi.nlm.nih.gov/21143318/) | *Potassium mediates σ-factor selectivity* | *E. coli* | Downstream: EIIA^Ntr^ K⁺ control sets σ⁷⁰/σ^S^ balance |
| [18421563](https://pubmed.ncbi.nlm.nih.gov/18421563/) | *Solution structure of NPr* | *E. coli* | Upstream partner (NPr) structure; His16 phosphotransfer to IIA^Ntr^ |

**Convergence of evidence.** The two most authoritative, precise studies are direct target-organism biochemistry: the PtsN–AceE co-IP/MS and PDH assays ([PMID: 21236318](https://pubmed.ncbi.nlm.nih.gov/21236318/)) and the PtsN–KdpD two-hybrid/promoter analysis ([PMID: 26224366](https://pubmed.ncbi.nlm.nih.gov/26224366/)). These are reinforced by in vivo phospho-state mapping in the same organism ([PMID: 18296519](https://pubmed.ncbi.nlm.nih.gov/18296519/)), by structural data defining the His/Arg active site ([PMID: 16092953](https://pubmed.ncbi.nlm.nih.gov/16092953/)), and by an extensive *E. coli* mechanistic literature that establishes the accessory-regulator paradigm for the whole family ([PMID: 17289841](https://pubmed.ncbi.nlm.nih.gov/17289841/); [PMID: 19400808](https://pubmed.ncbi.nlm.nih.gov/19400808/); [PMID: 22812494](https://pubmed.ncbi.nlm.nih.gov/22812494/)).

**Identity verification (mandatory check passed).** The gene symbol *ptsN*, the "Phosphotransferase system enzyme IIA, regulation of potassium transport" description, the organism *P. putida* KT2440, and the domains (PF00359, IPR002178, IPR006320) all align precisely with the EIIA^Ntr^/PTS^Ntr^ literature above, including studies performed **directly in KT2440**. There is no ambiguity or organism mix-up: this is the correct gene, and the "regulation of potassium transport" phrase in the UniProt description is corroborated by primary experimental work in the same strain ([PMID: 26224366](https://pubmed.ncbi.nlm.nih.gov/26224366/)).

---

## Limitations and Knowledge Gaps

1. **Sign of *kdpFABC* regulation differs across species.** In *P. putida*, PtsN∼P *represses* *kdpFABC* ([PMID: 26224366](https://pubmed.ncbi.nlm.nih.gov/26224366/)), whereas in *E. coli* the dephospho form *stimulates* KdpD to *activate* *kdpFABC* ([PMID: 19400808](https://pubmed.ncbi.nlm.nih.gov/19400808/)), and in *Rhizobium* unphospho-EIIA^Ntr^ activates KdpABC ([PMID: 22340847](https://pubmed.ncbi.nlm.nih.gov/22340847/)). The molecular basis for this inversion in *P. putida* — and whether it reflects different KdpD conformational coupling or additional factors — is not resolved. A modeling study even predicts an additional, unidentified integrative controller in the KT2440 K⁺-uptake circuit ([PMID: 26159078](https://pubmed.ncbi.nlm.nih.gov/26159078/)).

2. **PhoR/TrkA interactions in *P. putida* are inferred, not proven.** The PhoR and TrkA regulatory roles are established in *E. coli*; their direct occurrence in *P. putida* KT2440 is a reasonable homology-based inference but has not, in the reviewed literature, been demonstrated in the target organism.

3. **His68 is predicted, not experimentally mutated here.** The His68 phospho-acceptor assignment rests on sequence/structure homology to solved IIA^Ntr^ structures ([PMID: 16092953](https://pubmed.ncbi.nlm.nih.gov/16092953/)). A site-directed H68A/H68E mutagenesis series in KT2440 tying phospho-state to each output would close this gap directly.

4. **Structural data are for orthologs, not Q88PA0 itself.** No experimental structure of *P. putida* PtsN (Q88PA0) is cited; the fold is inferred from *N. meningitidis* IIA^Ntr^ and *E. coli* IIA^Ntr^ (PDB 1A6J).

5. **Quantitative interaction parameters are lacking.** Binding affinities (K_d) of PtsN∼P vs. PtsN for KdpD and AceE, and the stoichiometry/kinetics of the switch, are not established, limiting a fully quantitative model of the bifunctional switch.

6. **Pleiotropy vs. primary role.** Effects on the TOL *Pu* promoter, IncP-9 plasmid conjugation, PHB accumulation, and σ-factor selectivity are documented but are largely downstream consequences; disentangling which are direct PtsN contacts vs. indirect (K⁺-mediated) is incomplete.

---

## Proposed Follow-up Experiments / Actions

1. **Direct His68 phospho-switch dissection in KT2440.** Construct chromosomal *ptsN* point mutants (H68A non-phosphorylatable; H68E/D phospho-mimetic) and measure, in isogenic backgrounds: (a) *kdpFp* promoter activity vs. external K⁺; (b) PDH specific activity; (c) growth on fructose vs. succinate vs. glucose. This directly ties His68 phosphorylation to each output.

2. **Quantitative interactomics.** Purify Q88PA0 and phospho-mimetic variants; measure K_d and stoichiometry against the KdpD cytoplasmic domain and AceE by ITC/SPR/BLI. Test whether PtsN∼P and PtsN differ in affinity (predicting the switch mechanism) rather than merely in downstream effect.

3. **Test PhoR and TrkA regulation in *P. putida*.** Use bacterial two-hybrid and *phoA*/*pho*-regulon reporters, plus K⁺-uptake assays, to determine whether the *E. coli* PhoR and TrkA interactions are conserved in KT2440 or whether *P. putida* rewires these outputs.

4. **Resolve the *kdpFABC* sign inversion.** Reconstitute KdpD/KdpE phosphotransfer in vitro with *P. putida* components ± PtsN/PtsN∼P to determine whether *P. putida* PtsN∼P inhibits KdpD autokinase (opposite of *E. coli*), and search for the predicted additional integrative controller ([PMID: 26159078](https://pubmed.ncbi.nlm.nih.gov/26159078/)).

5. **Experimental structure of Q88PA0.** Solve the crystal or cryo-EM/NMR structure of *P. putida* PtsN, ideally in complex with the KdpD cytoplasmic domain and/or AceE, to define the docking surfaces and validate the His68/Arg70 active site.

6. **Systems-level phospho-flux mapping.** Combine in vivo phospho-state measurement of PtsN with metabolomics (PEP:pyruvate) across carbon sources to build a quantitative model of how metabolic state sets PtsN phospho-occupancy and, in turn, K⁺ uptake and PDH flux.

---

## Conclusion

*ptsN* / PP_0950 / Q88PA0 encodes **EIIA^Ntr^**, the terminal, soluble, cytoplasmic phosphoacceptor of the sugar-independent **PTS^Ntr^** of *Pseudomonas putida* KT2440. It is **not an enzyme or transporter** but a **phosphorylation-state-controlled protein–protein adaptor** whose His68 phospho-status — set by the PEP → PtsP → PtsO → PtsN relay with fructose/FruB cross-talk — toggles direct interactions with specific targets. Its best-defined primary functions in the target organism are **regulation of potassium transport** (PtsN∼P directly binds the sensor kinase KdpD to control the *kdpFABC* K⁺ pump) and **inhibition of pyruvate dehydrogenase** (unphosphorylated PtsN binds and down-regulates AceE), with an accessory-regulator role over membrane sensor kinases (KdpD, PhoR) and the TrkA K⁺ transporter established across proteobacteria. It thereby coordinates potassium and phosphate homeostasis with central carbon flux, acting in the cytoplasm and at the cytoplasmic face of the inner membrane.


## Artifacts

- [OpenScientist final report](ptsN-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ptsN-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:21236318
2. PMID:25701731
3. PMID:18296519
4. PMID:16092953
5. PMID:26224366
6. PMID:22340847
7. PMID:17289841
8. PMID:19400808
9. PMID:22812494
10. PMID:21143318
11. PMID:26159078