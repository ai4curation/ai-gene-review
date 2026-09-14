---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-13T03:35:31.964691'
end_time: '2026-08-13T03:52:21.119421'
duration_seconds: 1009.15
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: phaC
  gene_symbol: phaC-II
  uniprot_accession: Q88D23
  protein_description: 'SubName: Full=Poly(3-hydroxyalkanoate) polymerase 2 {ECO:0000313|EMBL:AAN70571.1};
    EC=2.3.1.- {ECO:0000313|EMBL:AAN70571.1};'
  gene_info: Name=phaC-II {ECO:0000313|EMBL:AAN70571.1}; OrderedLocusNames=PP_5005
    {ECO:0000313|EMBL:AAN70571.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: AB_hydrolase_fold. (IPR029058); PHA/PHB_synthase. (IPR051321);
    PHA_synth_II. (IPR011287); PhaC_N. (IPR010941); PhaC_N (PF07167)
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
citation_count: 11
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: phaC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: phaC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88D23
- **Protein Description:** SubName: Full=Poly(3-hydroxyalkanoate) polymerase 2 {ECO:0000313|EMBL:AAN70571.1}; EC=2.3.1.- {ECO:0000313|EMBL:AAN70571.1};
- **Gene Information:** Name=phaC-II {ECO:0000313|EMBL:AAN70571.1}; OrderedLocusNames=PP_5005 {ECO:0000313|EMBL:AAN70571.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** AB_hydrolase_fold. (IPR029058); PHA/PHB_synthase. (IPR051321); PHA_synth_II. (IPR011287); PhaC_N. (IPR010941); PhaC_N (PF07167)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "phaC-II" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'phaC-II' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **phaC-II** (gene ID: phaC, UniProt: Q88D23) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *phaC-II* (PhaC2, Q88D23, PP_5005) in *Pseudomonas putida* KT2440

**Organism:** *Pseudomonas putida* KT2440 (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950) — proteome PSEPK
**Gene:** *phaC-II* (also *phaC2*); Ordered locus PP_5005
**Protein:** Poly(3-hydroxyalkanoate) polymerase 2 (medium-chain-length PHA synthase 2); EC 2.3.1.-
**UniProt:** Q88D23

## Summary

**phaC-II** (gene product PhaC2; UniProt **Q88D23**; ordered locus **PP_5005**) of *Pseudomonas putida* KT2440 encodes a **Class II medium-chain-length polyhydroxyalkanoate (mcl-PHA) synthase**. Its primary molecular function is that of a **polymerizing acyltransferase** (EC 2.3.1.-) that catalyzes the covalent, processive polymerization of **(R)-3-hydroxyacyl-CoA thioesters — predominantly medium-chain-length substrates of roughly C6–C14 — into the storage polyester mcl-PHA, with the concomitant release of coenzyme A**. This assignment is strongly supported by the protein's domain architecture (PHA_synth_II / IPR011287; PhaC_N / PF07167 / IPR010941; and an α/β-hydrolase fold, IPR029058), by the presence of an intact catalytic lipase-box motif in the primary sequence, and by the broader biochemistry of the PHA synthase family.

The catalytic mechanism proceeds through an **α/β-hydrolase fold** using a **Cys–Asp–His catalytic triad**, in which an active-site cysteine acts as the covalent nucleophile. Direct sequence analysis of Q88D23 (560 residues) locates the canonical lipase-box motif **G294-A-C296-A-G298** (context "NLMG-ACAG-GLT"), positioning the catalytic nucleophile at **Cys296**, with downstream conserved residues (including His480 in an "S-G-H-I-Q" motif) completing the triad by homology. This mirrors the experimentally established covalent nucleophile Cys149 of the *Chromatium vinosum* PHA synthase and the Cys–Asp–His triads resolved in crystal structures of PhaC from *Cupriavidus necator* and *Chromobacterium* sp. USM2.

In terms of localization and biological role, PhaC2 begins as a **soluble cytoplasmic enzyme** and, upon initiating polyester synthesis, becomes an amphipathic protein that self-assembles onto the surface of **intracellular PHA granules (carbonosomes)** — a phospholipid-monolayer-coated inclusion body where the enzyme's activity markedly increases. PhaC2 is one of **two paralogous synthases** (PhaC1 = PP_5003/Q88D25 and PhaC2 = PP_5005/Q88D23, ~55% identical) that flank the intracellular depolymerase **PhaZ (PP_5004)** in the canonical *phaC1-phaZ-phaC2* operon. Physiologically, PhaC2 contributes to **carbon and energy storage under nutrient-limiting conditions**, drawing its (R)-3-hydroxyacyl-CoA monomers from **fatty-acid β-oxidation** and from **de novo fatty-acid synthesis** (via the transacylase PhaG).

---

## Key Findings

### F001 — PhaC2 is a Class II mcl-PHA synthase that polymerizes (R)-3-hydroxyacyl-CoAs

The UniProt record for Q88D23 annotates PP_5005/*phaC-II* as "Poly(3-hydroxyalkanoate) polymerase 2," assigns EC 2.3.1.- (an acyltransferase), and lists the diagnostic domains **PHA_synth_II (IPR011287)**, **PhaC_N (PF07167 / IPR010941)**, and the **α/β-hydrolase fold (IPR029058)**. These annotations place the protein squarely within the polyester (PHA) synthase family. As reviewed by Rehm, "Polyester synthases are the key enzymes of polyester biosynthesis and catalyse the conversion of (R)-hydroxyacyl-CoA thioesters to polyesters with the concomitant release of CoA" ([PMID: 12954080](https://pubmed.ncbi.nlm.nih.gov/12954080/)). The same review notes that "Polyester synthases can been assigned to four classes based on their substrate specificity and subunit composition." Class II synthases — the *Pseudomonas* PhaC1/PhaC2 type — are **single-PhaC-subunit enzymes** that are specific for **medium-chain-length (C6–C14) 3-hydroxyacyl-CoA substrates**, distinguishing them from the short-chain-length-specific Class I and III enzymes.

Crucially, the two *Pseudomonas* paralogs are not merely predicted enzymes: complementation analysis has directly demonstrated that "both mclPHA synthases, PhaC1 and PhaC2, were functional" ([PMID: 24887088](https://pubmed.ncbi.nlm.nih.gov/24887088/)). Together, the domain content, EC assignment, and functional complementation data establish PhaC2 as a genuine, catalytically active Class II mcl-PHA synthase whose product is the storage polyester mcl-PHA.

### F002 — Catalysis proceeds via a covalent active-site cysteine in an α/β-hydrolase fold with a lipase-box triad

The mechanism of PHA synthases is one of the best-characterized features of the family. In the *Chromatium vinosum* PHA synthase, the enzyme "catalyzes the conversion of 3-hydroxybutyryl-CoA (HB-CoA) to polyhydroxybutyrate (PHB) and CoA," and covalent catalysis was demonstrated by trapping a 3-hydroxybutyryl-thioester intermediate: "Sequencing by ion trap mass spectrometry showed that they were identical and that they each contained an altered cysteine (C149)" ([PMID: 9888824](https://pubmed.ncbi.nlm.nih.gov/9888824/)). This identifies a specific active-site cysteine as the covalent catalytic nucleophile.

Despite substantial sequence divergence across the family — "The multiple alignment of the primary structures of these polyester synthases show an overall identity of 8-96% with only eight strictly conserved amino acid residues" ([PMID: 12954080](https://pubmed.ncbi.nlm.nih.gov/12954080/)) — the cysteine nucleophile is retained within a **lipase-box (Gly-X-Cys-X-Gly)** motif. Crystallographic studies of the PhaC catalytic domain from *Cupriavidus necator* and from *Chromobacterium* sp. USM2 revealed an **α/β-hydrolase fold** organized around a **Cys–Asp–His catalytic triad** ([PMID: 28706283](https://pubmed.ncbi.nlm.nih.gov/28706283/); [PMID: 30511262](https://pubmed.ncbi.nlm.nih.gov/30511262/)). Q88D23's IPR029058 (AB_hydrolase_fold) annotation is fully consistent with this architecture, so PhaC2 is expected to use the same nucleophilic acyl-enzyme chemistry.

### F003 — PhaC2 is cytoplasmic and becomes surface-bound to intracellular PHA granules (carbonosomes)

PHA synthases exhibit a characteristic subcellular life cycle. They begin as soluble cytoplasmic proteins: "These soluble enzymes turn into amphipathic enzymes upon covalent catalysis of polyester-chain formation. A self-assembly process is initiated resulting in the formation of insoluble cytoplasmic inclusions with a phospholipid monolayer and covalently attached polyester synthases at the surface" ([PMID: 12954080](https://pubmed.ncbi.nlm.nih.gov/12954080/)). Importantly, the enzyme is more active at the granule surface: "Surface-attached polyester synthases show a marked increase in enzyme activity."

The resulting inclusions are readily visualized. In *P. putida* TISTR 1522, intracellular PHAs "accumulate in granules, about 3-10 granules per cell… white and roundish-shaped with 0.3-0.5-μm diameter," detectable by Nile red staining and transmission electron microscopy ([PMID: 33405009](https://pubmed.ncbi.nlm.nih.gov/33405009/)). These granules are coated with granule-associated proteins (GAPs), including phasins that "play essential roles in granule formation, PHA metabolism," modulate granule number and morphology, and can be exploited as bio-affinity tags ([PMID: 41548774](https://pubmed.ncbi.nlm.nih.gov/41548774/)). Notably, the relative surface abundance of the two synthase paralogs can differ: in one *Pseudomonas* strain, "The analysis of the proteins bound to the PHA granules showed the presence of PhbC and PhaC1, whilst PhaC2 could not be detected" ([PMID: 24887088](https://pubmed.ncbi.nlm.nih.gov/24887088/)), indicating that PhaC2 may be less abundant on granule surfaces than PhaC1 under certain conditions even though both are catalytically competent.

### F004 — *phaC2* lies in the *pha* cluster and functions in carbon/energy storage fed by fatty-acid metabolism

In *Pseudomonas*, the mcl-PHA genes are organized as a compact cluster in which the two synthases flank the depolymerase: a "cluster, phaC1ZC2D, coding for medium chain length PHA production (mclPHA)" ([PMID: 24887088](https://pubmed.ncbi.nlm.nih.gov/24887088/)). The (R)-3-hydroxyacyl-CoA monomers consumed by the synthases are supplied by two converging routes: **β-oxidation of exogenous fatty acids**, and **de novo fatty-acid synthesis**, the latter linked to PHA via the "(R)-3-hydroxydecanol-ACP:CoA transacylase gene phaG (Pp) from Pseudomonas putida" ([PMID: 16496091](https://pubmed.ncbi.nlm.nih.gov/16496091/)).

Physiologically, active mcl-PHA synthesis is coordinated with the machinery that supplies monomers and coats granules: "Active mcl-PHA synthesis by P. putida LS46 was associated with high expression levels of key mcl-PHA biosynthesis genes and/or gene products including monomer-supplying proteins, PHA synthases, and granule-associated proteins" ([PMID: 26544181](https://pubmed.ncbi.nlm.nih.gov/26544181/)). Genetic manipulations confirm this pathway logic. Promoter strengthening upstream of *phaC1* raised the transcription of both *phaC1* and *phaC2* and increased PHA yield ([PMID: 34582907](https://pubmed.ncbi.nlm.nih.gov/34582907/)), while deletion of β-oxidation genes together with *phaZ* increased the content of the dominant monomer ([PMID: 31706817](https://pubmed.ncbi.nlm.nih.gov/31706817/)). Together these place PhaC2 at the polymer-forming terminus of a carbon/energy-storage pathway that is switched on under nutrient limitation with excess carbon.

### F005 — The Q88D23 sequence contains the conserved lipase-box with catalytic Cys296

Direct analysis of the 560-residue Q88D23 sequence locates the canonical PHA-synthase lipase-box motif **G-X-C-X-G as G294-A-C296-A-G298** (sequence context "NLMG-ACAG-GLT"), placing the catalytic nucleophile at **Cys296**. A downstream conserved histidine occurs in an "S-G-H-I-Q" motif at **His480** ("LANSGHIQSII"), consistent with the histidine member of the Cys–Asp–His triad; conserved Asp/His candidates around residues 452–453 and His480 complete the triad by homology. This directly mirrors the experimentally defined nucleophile **Cys149** of *Chromatium vinosum* PhaC ("they each contained an altered cysteine (C149)"; [PMID: 9888824](https://pubmed.ncbi.nlm.nih.gov/9888824/)) and the Cys–Asp–His triad within the α/β-hydrolase fold seen in the PhaC crystal structures ([PMID: 28706283](https://pubmed.ncbi.nlm.nih.gov/28706283/); [PMID: 30511262](https://pubmed.ncbi.nlm.nih.gov/30511262/)). The retention of these residues despite low overall family identity ("only eight strictly conserved amino acid residues"; [PMID: 12954080](https://pubmed.ncbi.nlm.nih.gov/12954080/)) confirms that PhaC2 possesses an intact catalytic apparatus — it is an active synthase, not a degenerate pseudo-enzyme.

### F006 — PhaC2 is a ~55%-identical paralog of PhaC1, with PhaZ between them in the KT2440 locus

The KT2440 genome encodes two adjacent PHA synthases: **PhaC1 = Q88D25 (PP_5003**, "Poly(3-hydroxyalkanoate) polymerase 1," 559 aa) and **PhaC2 = Q88D23 (PP_5005**, "Poly(3-hydroxyalkanoate) polymerase 2," 560 aa). The intervening **PP_5004 is *phaZ*** (the intracellular depolymerase), yielding the canonical **phaC1-phaZ-phaC2** arrangement, independently corroborated by the *phaC1ZC2D* cluster description ([PMID: 24887088](https://pubmed.ncbi.nlm.nih.gov/24887088/)). A global Needleman–Wunsch alignment of the two paralogs computed during this investigation gave **306/557 = 54.9% amino-acid identity**. Both paralogs carry the lipase-box motif at the identical position 294–298 with the catalytic **Cys296** (PhaC1: G294-A-C296-S-G298; PhaC2: G294-A-C296-A-G298). Both single-subunit synthases belong to the same Class II family, consistent with the classification "based on their substrate specificity and subunit composition" ([PMID: 12954080](https://pubmed.ncbi.nlm.nih.gov/12954080/)).

---

## Mechanistic Model / Interpretation

PhaC2 sits at the terminal, polymer-forming step of the mcl-PHA storage pathway of *P. putida* KT2440. The following model synthesizes the findings above.

**Genomic context (the *pha* locus):**

```
   PP_5003        PP_5004        PP_5005
  ┌────────┐    ┌────────┐    ┌────────┐
  │ phaC1  │ →  │  phaZ  │ →  │ phaC2  │  → phaD → phaF/phaI ...
  │ Q88D25 │    │ depoly-│    │ Q88D23 │
  │ 559 aa │    │  merase│    │ 560 aa │
  └────────┘    └────────┘    └────────┘
   synthase 1                  synthase 2
   └──────── ~54.9% identity ─────────┘
   both: lipase box G294-A-C296-A/S-G298 (catalytic Cys296)
```

**Substrate supply and reaction:**

```
  Exogenous fatty acids ──► β-oxidation ─┐
                                          ├──► (R)-3-hydroxyacyl-CoA (C6–C14)
  Carbon (glucose/glycerol) ─► de novo   │            │
       FAS ──► (R)-3-OH-acyl-ACP ─PhaG──►┘            │
                                                       ▼
                              PhaC2 (Cys296 nucleophile, α/β-hydrolase)
                                                       │
                                    ester-bond formation, releases CoA
                                                       ▼
                                  ─[O–CH(R)–CH2–C(=O)]n─  mcl-PHA polyester
```

**Localization / catalytic life cycle:**

```
  Soluble cytoplasmic PhaC2  ──(initiates polyester synthesis)──►
  amphipathic PhaC2  ──(self-assembly)──►
  PHA granule (carbonosome): phospholipid monolayer core,
      PhaC2/PhaC1 + phasins (PhaP1/PhaI) at surface,
      0.3–0.5 µm, 3–10 per cell, higher synthase activity at surface
```

The enzyme is a **single-subunit Class II synthase**. It uses a covalent-catalysis mechanism: the thiol of **Cys296** attacks the thioester carbonyl of an incoming (R)-3-hydroxyacyl-CoA, forming a covalent acyl-enzyme intermediate and releasing CoA; ester-bond formation then extends the growing polyester chain, which remains covalently tethered to the enzyme during processive elongation. The Asp and His of the α/β-hydrolase triad activate the nucleophile and the incoming hydroxyl. Because both KT2440 paralogs retain the identical catalytic box, they are functionally redundant polymerases, which is why complementation shows both are active and why perturbing *phaC1* expression co-modulates *phaC2* and total PHA output.

The two synthases are not identical in behavior, however. Their ~55% divergence and the observation that PhaC2 was undetectable on granules in one strain (while PhaC1 was present) suggest **differential expression, granule-loading, or subtle substrate-preference differences** between the paralogs — a plausible basis for fine-tuning polymer monomer composition. This is consistent with reports that a lower-specificity PhaC2 from a related *Pseudomonas* can incorporate a broader range of monomers (scl + mcl), pointing to paralog-specific substrate tolerance as a tuning knob in the family ([PMID: 16496091](https://pubmed.ncbi.nlm.nih.gov/16496091/)).

**Physiological role:** mcl-PHA is a **carbon and energy reserve** synthesized under nutrient-limiting conditions with carbon excess. PhaC2, together with PhaC1, converts the cell's surplus (R)-3-hydroxyacyl-CoA pool into insoluble polymer that is later mobilized by the intervening depolymerase PhaZ. The tight genomic linkage of synthesis (*phaC1/phaC2*), degradation (*phaZ*), and granule structural/regulatory genes (*phaD/phaF/phaI*) reflects a coordinated storage-and-mobilization module.

### Summary comparison table

| Property | Value / evidence | Support |
|---|---|---|
| Gene / locus | *phaC-II* / PP_5005 | UniProt Q88D23 |
| Protein | Poly(3-hydroxyalkanoate) polymerase 2, 560 aa | UniProt Q88D23 |
| EC / activity | 2.3.1.- polymerizing acyltransferase | UniProt; [12954080](https://pubmed.ncbi.nlm.nih.gov/12954080/) |
| Class | Class II (single subunit, mcl-specific) | [12954080](https://pubmed.ncbi.nlm.nih.gov/12954080/) |
| Substrate | (R)-3-hydroxyacyl-CoA, ~C6–C14 | [12954080](https://pubmed.ncbi.nlm.nih.gov/12954080/) |
| Product | mcl-PHA polyester + CoA | [12954080](https://pubmed.ncbi.nlm.nih.gov/12954080/); [9888824](https://pubmed.ncbi.nlm.nih.gov/9888824/) |
| Catalytic nucleophile | Cys296 (lipase box G294-A-C296-A-G298) | Seq analysis; [9888824](https://pubmed.ncbi.nlm.nih.gov/9888824/) |
| Fold / triad | α/β-hydrolase, Cys–Asp–His | [28706283](https://pubmed.ncbi.nlm.nih.gov/28706283/); [30511262](https://pubmed.ncbi.nlm.nih.gov/30511262/) |
| Localization | Cytoplasm → PHA granule surface | [12954080](https://pubmed.ncbi.nlm.nih.gov/12954080/); [33405009](https://pubmed.ncbi.nlm.nih.gov/33405009/) |
| Paralog | PhaC1 (Q88D25/PP_5003), ~54.9% identity | This work; [24887088](https://pubmed.ncbi.nlm.nih.gov/24887088/) |
| Monomer supply | β-oxidation + de novo FAS (PhaG) | [16496091](https://pubmed.ncbi.nlm.nih.gov/16496091/); [31706817](https://pubmed.ncbi.nlm.nih.gov/31706817/) |
| Physiological role | Carbon/energy storage under nutrient limitation | [26544181](https://pubmed.ncbi.nlm.nih.gov/26544181/) |

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|---|---|---|
| [12954080](https://pubmed.ncbi.nlm.nih.gov/12954080/) | *Polyester synthases: natural catalysts for plastics* | Foundational review: defines the CoA-releasing polymerization reaction, the four-class scheme, the eight strictly conserved residues, and the cytoplasm→granule-surface localization cycle. Underpins F001, F002, F003, F005, F006. |
| [9888824](https://pubmed.ncbi.nlm.nih.gov/9888824/) | *PHA synthase from Chromatium vinosum: Cys149 in covalent catalysis* | Direct MS evidence of a covalent acyl-cysteine intermediate; establishes the catalytic nucleophile paradigm applied to Cys296 of Q88D23. Underpins F002, F005. |
| [28706283](https://pubmed.ncbi.nlm.nih.gov/28706283/) | *Structure of PhaC from Chromobacterium sp. USM2* | Crystal structure showing α/β-hydrolase fold and Cys–Asp–His triad. Underpins F002, F005. |
| [30511262](https://pubmed.ncbi.nlm.nih.gov/30511262/) | *PhaC: functions from a structural perspective* | Confirms the catalytic-domain fold and triad from *C. necator* PhaC. Underpins F002, F005. |
| [24887088](https://pubmed.ncbi.nlm.nih.gov/24887088/) | *High PHB production in P. extremaustralis…* | Complementation shows both PhaC1 and PhaC2 are functional; documents *phaC1ZC2D* operon; notes PhaC2 sometimes undetectable on granules. Underpins F001, F003, F004, F006. |
| [16496091](https://pubmed.ncbi.nlm.nih.gov/16496091/) | *Lower-specificity PhaC2 from P. stutzeri…* | Identifies PhaG transacylase linking de novo FAS to monomer supply; shows paralog substrate breadth. Underpins F004. |
| [26544181](https://pubmed.ncbi.nlm.nih.gov/26544181/) | *Quantitative omics of mcl-PHA in P. putida LS46* | Links synthase expression with monomer-supply and granule proteins in the storage pathway. Underpins F004. |
| [34582907](https://pubmed.ncbi.nlm.nih.gov/34582907/) | *Promoter engineering in P. putida KT2440* | Strengthening *phaC1* promoter raised *phaC2* transcription and PHA yield. Underpins F004. |
| [31706817](https://pubmed.ncbi.nlm.nih.gov/31706817/) | *Metabolic engineering of P. mendocina NK-01* | β-oxidation + *phaZ* deletions increase dominant-monomer content. Underpins F004. |
| [33405009](https://pubmed.ncbi.nlm.nih.gov/33405009/) | *PHA production by P. putida TISTR 1522* | TEM/Nile red visualization of intracellular granules (0.3–0.5 µm, 3–10/cell). Underpins F003. |
| [41548774](https://pubmed.ncbi.nlm.nih.gov/41548774/) | *Phasin–PHA interactions* | Phasins (PhaP1/PhaI) coat granules and modulate number/morphology in KT2440. Underpins F003. |

Overall, the evidence forms a coherent chain: domain/annotation evidence (UniProt) and sequence-motif evidence (Cys296 lipase box) place the protein in the family; family-level biochemistry (covalent Cys catalysis, CoA release) and structural biology (α/β-hydrolase, Cys–Asp–His triad) define the mechanism; and *Pseudomonas*-specific genetics and omics (operon structure, complementation, monomer supply, granule localization) confirm the physiological role.

---

## Limitations and Knowledge Gaps

1. **No direct enzymology on Q88D23 itself.** The catalytic activity, kinetic parameters (kcat, Km), and precise substrate-length preference of the *KT2440* PhaC2 protein have not been measured in the cited literature. The functional assignment rests on domain architecture, conserved-motif analysis, family biochemistry, and complementation of *related* Pseudomonas synthases — strong but inferential evidence.

2. **Triad residues are assigned by homology, not structure.** Cys296 is confidently identified from the lipase box, but the exact identities of the Asp and His triad partners in Q88D23 (candidates around 452–453 and His480) are inferred from alignment, not from a crystal structure of PhaC2. No experimental structure of the KT2440 PhaC2 exists.

3. **PhaC1 vs. PhaC2 division of labor is unresolved.** Although both paralogs are functional and ~55% identical, their relative contributions to polymer yield, monomer composition, and granule loading in KT2440 specifically are not quantified. The single report of PhaC2 being undetectable on granules comes from a different species (*P. extremaustralis*) and cannot be assumed to hold for KT2440.

4. **Substrate-specificity fine structure.** Whether PhaC2 has a broader or narrower monomer range than PhaC1 (analogous to the lower-specificity *P. stutzeri* PhaC2) is not established for KT2440.

5. **Regulation.** The transcriptional/post-translational regulation of *phaC2* specifically (as opposed to co-regulation observed when *phaC1* is manipulated) has not been dissected.

---

## Proposed Follow-up Experiments / Actions

1. **Purify and assay recombinant KT2440 PhaC2.** Express Q88D23 heterologously, and measure in vitro polymerization kinetics against a panel of (R)-3-hydroxyacyl-CoA substrates (C4–C14) to define kcat/Km and confirm the mcl (C6–C14) preference directly.

2. **Site-directed mutagenesis of the triad.** Generate C296A (and candidate Asp/His-Ala mutants) and test for loss of activity, providing direct proof that Cys296 is the nucleophile in PhaC2.

3. **Single- and double-knockout phenotyping in KT2440.** Construct ΔphaC1, ΔphaC2, and ΔphaC1ΔphaC2 strains and quantify PHA yield, granule number/size (TEM), and monomer composition (GC-MS) to resolve the paralogs' division of labor.

4. **Granule proteomics in KT2440.** Isolate PHA granules and perform quantitative proteomics to determine whether PhaC2 is present on granule surfaces in KT2440 and at what stoichiometry relative to PhaC1 and phasins.

5. **Structural determination.** Solve the crystal or cryo-EM structure of the KT2440 PhaC2 catalytic domain to confirm the α/β-hydrolase fold and unambiguously identify the Asp/His triad partners.

6. **Substrate-feeding studies.** Feed defined fatty acids (e.g., octanoate, decanoate, dodecanoate) to paralog-specific mutants to map how each synthase shapes the mcl-PHA monomer distribution.

---

## Consensus Answer

**phaC-II (PhaC2; UniProt Q88D23; locus PP_5005) of *Pseudomonas putida* KT2440 is a Class II medium-chain-length polyhydroxyalkanoate (mcl-PHA) synthase — a polymerizing acyltransferase (EC 2.3.1.-) that condenses (R)-3-hydroxyacyl-CoA thioesters (~C6–C14) into the storage polyester mcl-PHA with release of CoA, using covalent catalysis at an active-site cysteine (Cys296, in an intact G-A-C-A-G lipase box) within an α/β-hydrolase Cys–Asp–His triad.** It is one of two ~55%-identical paralogous synthases (PhaC1 = PP_5003, PhaC2 = PP_5005) flanking the depolymerase PhaZ (PP_5004) in the *phaC1-phaZ-phaC2* operon. The enzyme starts soluble in the cytoplasm and, after initiating synthesis, binds the surface of intracellular PHA granules (carbonosomes), functioning in nutrient-limitation carbon/energy storage supplied by fatty-acid β-oxidation and de novo fatty-acid synthesis (via PhaG).


## Artifacts

- [OpenScientist final report](phaC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](phaC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:12954080
2. PMID:24887088
3. PMID:9888824
4. PMID:28706283
5. PMID:30511262
6. PMID:33405009
7. PMID:41548774
8. PMID:16496091
9. PMID:26544181
10. PMID:34582907
11. PMID:31706817