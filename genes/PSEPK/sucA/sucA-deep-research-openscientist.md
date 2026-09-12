---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T18:43:57.572393'
end_time: '2026-07-11T19:00:14.064423'
duration_seconds: 976.49
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: sucA
  gene_symbol: sucA
  uniprot_accession: Q88FA9
  protein_description: 'RecName: Full=2-oxoglutarate dehydrogenase E1 component {ECO:0000256|ARBA:ARBA00013321};
    EC=1.2.4.2 {ECO:0000256|ARBA:ARBA00012280}; AltName: Full=Alpha-ketoglutarate
    dehydrogenase {ECO:0000256|ARBA:ARBA00030680};'
  gene_info: Name=sucA {ECO:0000313|EMBL:AAN69770.1}; OrderedLocusNames=PP_4189 {ECO:0000313|EMBL:AAN69770.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the alpha-ketoglutarate dehydrogenase family.
  protein_domains: 2-oxogl_dehyd_N. (IPR032106); 2oxoglutarate_DH_E1. (IPR011603);
    DH_E1. (IPR001017); KGD_C_sf. (IPR042179); ODO-1/KGD_C. (IPR031717)
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
  path: sucA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: sucA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88FA9
- **Protein Description:** RecName: Full=2-oxoglutarate dehydrogenase E1 component {ECO:0000256|ARBA:ARBA00013321}; EC=1.2.4.2 {ECO:0000256|ARBA:ARBA00012280}; AltName: Full=Alpha-ketoglutarate dehydrogenase {ECO:0000256|ARBA:ARBA00030680};
- **Gene Information:** Name=sucA {ECO:0000313|EMBL:AAN69770.1}; OrderedLocusNames=PP_4189 {ECO:0000313|EMBL:AAN69770.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the alpha-ketoglutarate dehydrogenase family.
- **Key Domains:** 2-oxogl_dehyd_N. (IPR032106); 2oxoglutarate_DH_E1. (IPR011603); DH_E1. (IPR001017); KGD_C_sf. (IPR042179); ODO-1/KGD_C. (IPR031717)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "sucA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'sucA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **sucA** (gene ID: sucA, UniProt: Q88FA9) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *sucA* (Q88FA9 / PP_4189) in *Pseudomonas putida* KT2440

**Gene:** *sucA* · **UniProt:** Q88FA9 · **Locus:** PP_4189 · **Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440) · **EC:** 1.2.4.2

---

## Summary

*sucA* (Q88FA9, ordered locus PP_4189) encodes the **E1o component (2-oxoglutarate dehydrogenase, EC 1.2.4.2)** of the **2-oxoglutarate dehydrogenase complex (OGDHc / α-ketoglutarate dehydrogenase complex, KGDHc)** in *Pseudomonas putida* KT2440. Its gene product is a **thiamine-diphosphate (ThDP)-dependent oxidoreductase** that catalyzes the **first, committed and rate-limiting step of the fourth reaction of the tricarboxylic acid (TCA) cycle**: the oxidative decarboxylation of 2-oxoglutarate (α-ketoglutarate). The enzyme decarboxylates its C5 keto-acid substrate to yield a covalent succinyl-ThDP enamine intermediate and CO₂, then transfers the succinyl moiety by reductive succinylation onto the lipoyl "swinging arm" of the E2 core (SucB). Together with E2 (dihydrolipoyl succinyltransferase, SucB) and E3 (dihydrolipoyl dehydrogenase, LpdG), the overall multienzyme complex converts 2-oxoglutarate + CoA + NAD⁺ → succinyl-CoA + CO₂ + NADH. This positions SucA at a pivotal **carbon/nitrogen and redox/energy node**, partitioning flux between respiratory ATP generation and biosynthetic precursor (glutamate/succinyl-CoA) supply.

The identity assignment is robust and passes all mandatory verification checks. The gene symbol *sucA* is the canonical bacterial designation for the E1o subunit; the UniProt description, EC number (1.2.4.2), protein family (alpha-ketoglutarate dehydrogenase), and InterPro domain architecture (2-oxogl_dehyd_N, 2oxoglutarate_DH_E1, DH_E1, KGD_C) all converge on this function. In *P. putida* KT2440's own genome, PP_4189 sits in a contiguous, co-oriented `sdhA–sdhB–sucA–sucB–lpdG` gene cluster that encodes all three OGDHc subunits (E1/E2/E3) side by side, exactly as expected for this operonic module of the TCA cycle.

Because no direct enzymology exists for the *P. putida* protein itself, its precise mechanism and substrate specificity are inferred with high confidence from its closest biochemically and structurally characterized ortholog, *Escherichia coli* SucA (65.6% amino-acid identity over the full-length single-chain α/β-fused polypeptide). The catalytically and regulatorily important residues — the active-site histidine cluster (E. coli His260/His298/His729 → P. putida His266/His304/His737) and the Thr405→Thr411 regulatory AMPylation site — are conserved, licensing functional transfer. The enzyme operates in the **bacterial cytoplasm** as a soluble, high-molecular-weight multienzyme assembly.

---

## Gene/Protein Identity Verification

**Verified — identity is unambiguous.** All four mandatory checks pass:

1. **Symbol matches function.** *sucA* is the canonical bacterial gene name for the E1o (2-oxoglutarate dehydrogenase) subunit; this matches the UniProt RecName "2-oxoglutarate dehydrogenase E1 component."
2. **Organism confirmed.** The target is *Pseudomonas putida* KT2440, and PP_4189 is confirmed as *sucA* within KT2440's own genome (KEGG organism `ppu`).
3. **Family/domains align.** The alpha-ketoglutarate dehydrogenase family and InterPro domains (2oxoglutarate_DH_E1 / DH_E1 / KGD_C) match the literature on E1o enzymes.
4. **No same-symbol confusion.** The well-characterized *E. coli* SucA used for functional transfer is a genuine 65.6%-identical ortholog — not an unrelated gene sharing the symbol.

---

## Key Findings

### F001 — SucA is the ThDP-dependent E1o decarboxylase (EC 1.2.4.2)

UniProt Q88FA9 is annotated as **RecName: 2-oxoglutarate dehydrogenase E1 component, EC 1.2.4.2**, in the alpha-ketoglutarate dehydrogenase family, with defining InterPro domains IPR011603 (2oxoglutarate_DH_E1), IPR001017 (DH_E1), and IPR031717 (KGD C-terminal). The gene symbol *sucA* is the canonical bacterial name for this E1 subunit. The bacterial E1o homolog is a thiamine-diphosphate–dependent enzyme that catalyzes the **first, rate-limiting step of the OGDH complex reaction**.

This is directly supported by the *E. coli* structural work of Frank et al.: *"The thiamine-dependent E1o component (EC 1.2.4.2) of the 2-oxoglutarate dehydrogenase complex catalyses a rate-limiting step of the tricarboxylic acid cycle (TCA) of aerobically respiring organisms"* ([PMID: 17367808](https://pubmed.ncbi.nlm.nih.gov/17367808/)). This single sentence anchors the enzyme identity, the cofactor (thiamine diphosphate), the EC number (1.2.4.2), and the physiological role as the rate-limiting E1 step that *sucA* performs.

### F002 — SucA acts within a multienzyme OGDH complex using lipoyl-arm substrate channeling

SucA does not act in isolation. It is the E1 catalytic subunit of the OGDH/KGDH complex, which consists of multiple copies of three catalytic subunits: **E1 (SucA, 2-oxoglutarate dehydrogenase, EC 1.2.4.2)**, **E2 (SucB, dihydrolipoyl succinyltransferase, EC 2.3.1.61)** forming the structural core, and **E3 (LpdG, dihydrolipoamide dehydrogenase, EC 1.8.1.4)**. E1 decarboxylates the substrate and passes the succinyl group to lipoyl moieties tethered on the E2 core via a flexible "swinging arm."

Kinetic and computer-model analysis of the *E. coli* complex demonstrates that this channeling is highly interconnected: *"More than one lipoyl moiety services each E1 subunit (alpha-ketoglutarate dehydrogenase, EC 1.2.4.2), and an extensive lipoyl-lipoyl interaction network for exchange of electrons and possibly acyl groups must also be present"* ([PMID: 6403946](https://pubmed.ncbi.nlm.nih.gov/6403946/)). The three-subunit architecture is confirmed independently: *"The complex consists of multiple copies of three catalytic subunits: α-ketoglutarate dehydrogenase (E1), dihydrolipoamide succinyltransferase (E2) and dihydrolipoamide dehydrogenase (E3)"* ([PMID: 36256893](https://pubmed.ncbi.nlm.nih.gov/36256893/)). SucA is thus the point-of-entry catalyst in a nanomachine that couples decarboxylation, acyl transfer, and NADH generation through substrate channeling.

### F003 — Structure defines substrate specificity (His/Ser cluster) and allosteric control (oxaloacetate, AMP)

The 2.6 Å crystal structure of *E. coli* E1o reveals the ThDP-binding fold and an **α₂β₂-like architecture in which the α and β subunits are fused into a single polypeptide** — consistent with Q88FA9 being a single ~933–943-residue chain rather than two separate subunits. As Frank et al. state, *"the alpha and beta subunits are fused as a single polypeptide"* ([PMID: 17367808](https://pubmed.ncbi.nlm.nih.gov/17367808/)).

The same structure identifies the determinants of substrate specificity and regulation: *"The active site pocket contains a group of three histidine residues and one serine that appear to confer substrate specificity and the capacity to accommodate the TCA metabolite oxaloacetate. Oxaloacetate inhibits E1o activity at physiological concentrations"* ([PMID: 17367808](https://pubmed.ncbi.nlm.nih.gov/17367808/)). Additionally, an AMP molecule is specifically recognized in a pocket linking the enzyme's domains, providing a second layer of allosteric/energy-state control. These features are the molecular basis both for 2-oxoglutarate selectivity and for feedback sensing of TCA metabolite pools.

### F004 — Genomic and transcriptional coupling to the succinate-branch TCA genes

In *E. coli*, *sucA* lies in the **suc operon** together with the E2o (*sucB*) and succinyl-CoA synthetase (*sucCD*) genes, within the larger *gltA*–*sdhCDAB*–*sucABCD* citric-acid-cycle gene cluster. As reported: *"the suc operon, which also encodes the dehydrogenase (Elo; sucA) and succinyltransferase (E2o; sucB) components of the 2-oxoglutarate dehydrogenase complex"* ([PMID: 3543212](https://pubmed.ncbi.nlm.nih.gov/3543212/)). The *sucABCD* genes are coordinately regulated, being controlled largely from the upstream *sdhC* promoter with negative control under anaerobiosis by ArcA and Fnr: *"The sucABCD genes of Escherichia coli encode subunits for two enzymes of the tricarboxylic acid (TCA) cycle, alpha-ketoglutarate dehydrogenase (sucAB) and succinyl coenzyme A synthetase (sucCD)"* ([PMID: 9209026](https://pubmed.ncbi.nlm.nih.gov/9209026/)).

The functional consequence of losing this activity is demonstrable: *"disruption of the sucA or sucB gene (encoding subunits of the 2-oxoglutarate dehydrogenase complex) notably decreased HHP survival"* ([PMID: 30497599](https://pubmed.ncbi.nlm.nih.gov/30497599/)), establishing that SucA's OGDHc function has a measurable physiological phenotype. In *P. putida* KT2440, the citric acid cycle is a component of tightly regulated central carbon metabolism, and *sucA* corresponds to locus PP_4189.

### F005 — P. putida SucA is a close ortholog of biochemically characterized E. coli SucA (65.6% identity)

A pairwise global alignment (Needleman-Wunsch, +2/−1/−1) of the full-length UniProt sequences shows *P. putida* KT2440 SucA (Q88FA9, **943 aa**) and *E. coli* K-12 SucA (P0AFG3 / ODO1_ECOLI, **933 aa**) share **588 identical residues over 896 aligned columns = 65.6% amino-acid identity**. Both are annotated "2-oxoglutarate dehydrogenase E1 component," and both are single long polypeptides with α-like and β-like domains fused — matching the E1o architecture solved crystallographically in *E. coli*: *"the alpha and beta subunits are fused as a single polypeptide"* ([PMID: 17367808](https://pubmed.ncbi.nlm.nih.gov/17367808/)). This high sequence identity across the full length, spanning the ThDP-binding and catalytic regions, provides a strong, rigorous justification for transferring the *E. coli* mechanism, substrate specificity, and structure to the *P. putida* ortholog.

### F006 — Substrate specificity for 2-oxoglutarate (C5), distinct from the 2-oxoadipate E1a paralog

The enzyme is specifically dedicated to **2-oxoglutarate**, the C5 substrate of the TCA cycle's fourth step, and is functionally distinct from the paralogous 2-oxoadipate dehydrogenase E1a (DHTKD1). The reaction *"catalyzes the fourth step of the tricarboxylic acid (TCA) cycle and links carbohydrate, fatty acid and amino acid metabolism to the aerobic production of ATP"* ([PMID: 41722662](https://pubmed.ncbi.nlm.nih.gov/41722662/)), converting α-ketoglutarate to succinyl-CoA with NADH generation.

Substrate specificity within the E1 family is enzyme-specific and can be quantified: the human 2-oxoadipate dehydrogenase E1a shows *"an approximately 49-fold preference in catalytic efficiency for OA over OG, indicating that hE1a is specific to the 2-oxoadipate dehydrogenase complex"* ([PMID: 29191460](https://pubmed.ncbi.nlm.nih.gov/29191460/)). By contrast, the canonical E1o (*sucA*-type) is the **2-oxoglutarate-specific** component that recruits the shared E2o/E3 machinery. This ~49-fold catalytic-efficiency discrimination in the paralog underscores that E1 substrate selection is precise, and confirms SucA's dedicated role as the 2-oxoglutarate (not 2-oxoadipate) enzyme.

### F007 — In P. putida KT2440, PP_4189 sits in a contiguous sdhAB–sucA–sucB–lpdG cluster

KEGG genome annotation (organism `ppu`) places five co-oriented genes contiguously on the complement strand of the *P. putida* KT2440 chromosome:

| Locus | Gene | Product | KEGG Orthology | EC | Coordinates |
|-------|------|---------|----------------|-----|-------------|
| PP_4191 | *sdhA* | Succinate dehydrogenase flavoprotein | K00239 | 1.3.5.1 | 4,736,597–4,738,369 |
| PP_4190 | *sdhB* | SDH iron-sulfur subunit | K00240 | 1.3.5.1 | 4,735,881–4,736,585 |
| **PP_4189** | ***sucA*** | **2-oxoglutarate dehydrogenase E1** | **K00164** | **1.2.4.2** | **4,732,803–4,735,634** |
| PP_4188 | *sucB* | 2-oxoglutarate dehydrogenase E2 (dihydrolipoyl succinyltransferase) | K00658 | 2.3.1.61 | 4,731,537–4,732,760 |
| PP_4187 | *lpdG* | Dihydrolipoyl dehydrogenase E3 | K00382 | 1.8.1.4 | 4,730,007–4,731,443 |

Intergenic gaps are small (~40–95 bp), consistent with an operon. KEGG assigns PP_4189 to **Citrate cycle (ppu00020)**, **Lipoic acid metabolism (ppu00785)**, **2-Oxocarboxylic acid metabolism (ppu01210)**, and **Carbon metabolism (ppu01200)**, and to modules **M00009 (TCA cycle)** and **M00011 (2-oxoglutarate ⇒ oxaloacetate, second oxidation)**. This confirms — in *P. putida*'s own genome, not merely by analogy — that all three OGDHc catalytic subunits (E1/E2/E3) are encoded side by side, physically clustering the machinery SucA works within.

### F008 — Catalytic and regulatory residues are conserved in P. putida SucA

Alignment mapping of *E. coli* SucA (P0AFG3) onto *P. putida* SucA (Q88FA9) shows uniformly high domain-wise identity — the N-terminal region (res 1–350) is 64.0% identical and the central+C-terminal catalytic region (351–933) is 66.5% identical — with 71% of all *E. coli* histidines conserved as His. Crucially, the histidines corresponding to the *E. coli* E1o active-site region are conserved: **E. coli His260/His298/His729 → P. putida His266/His304/His737**. This maps the specificity-conferring active-site cluster identified crystallographically — *"The active site pocket contains a group of three histidine residues and one serine that appear to confer substrate specificity and the capacity to accommodate the TCA metabolite oxaloacetate"* ([PMID: 17367808](https://pubmed.ncbi.nlm.nih.gov/17367808/)) — directly onto the *P. putida* sequence.

In addition, the UniProt-annotated regulatory modification site of *E. coli* SucA, **Thr405 (O-AMP-threonine, AMPylated by the YdiU/SelO protein AMPylase)**, aligns to a conserved threonine (**Thr411**) in *P. putida* SucA. This indicates conservation not only of catalysis but also of a post-translational regulatory mechanism, suggesting SucA activity in *P. putida* may likewise be modulated by AMPylation under stress conditions.

---

## Mechanistic Model / Interpretation

### The reaction and its place in the cycle

SucA catalyzes the entry step of the OGDHc-catalyzed overall reaction:

```
  2-oxoglutarate + CoA-SH + NAD+  ──►  succinyl-CoA + CO2 + NADH + H+
  (α-ketoglutarate, C5)                (C4-acyl-CoA)
```

The complex partitions this into three sequential, channeled half-reactions across the three subunits:

```
  ┌────────────────────────── OGDH COMPLEX (soluble, cytoplasm) ──────────────────────────┐
  │                                                                                        │
  │  E1o = SucA (PP_4189)          E2o = SucB (PP_4188)          E3 = LpdG (PP_4187)        │
  │  ThDP-dependent                lipoyl-bearing core           FAD + NAD+                 │
  │  ───────────────               ──────────────────           ──────────────             │
  │                                                                                        │
  │  2-oxoglutarate                                                                        │
  │       │ (1) decarboxylation                                                            │
  │       ▼   ThDP → succinyl-ThDP  + CO2                                                   │
  │  [succinyl-ThDP enamine]                                                                │
  │       │ (2) reductive succinylation                                                    │
  │       └──────────────►  lipoyl-S-succinyl (E2)                                          │
  │                              │ (3) transfer to CoA                                      │
  │                              └──────────►  succinyl-CoA                                 │
  │                         dihydrolipoyl (E2)                                              │
  │                              │ (4) reoxidation                                          │
  │                              └──────────►  E3: FADH2 → NADH                             │
  │                                                                                        │
  └────────────────────────────────────────────────────────────────────────────────────┘
                   Step 4 of the TCA cycle · rate-limiting · irreversible
```

**Step 1 (SucA/E1o):** ThDP attacks the C2 keto-carbon of 2-oxoglutarate; decarboxylation releases CO₂ and generates a resonance-stabilized succinyl-ThDP enamine (carbanion) intermediate. The three-histidine + serine active-site cluster (P. putida His266/His304/His737) orients and stabilizes the C5 dicarboxylate substrate — the structural basis for selecting 2-oxoglutarate over other 2-oxo acids such as 2-oxoadipate (the DHTKD1/E1a substrate). This is the committed, rate-limiting, essentially irreversible step.

**Step 2 (SucA→SucB):** The succinyl group is transferred by reductive succinylation onto the oxidized lipoamide arm of E2, reducing the disulfide. The flexible lipoyl "swinging arm" then visits the E2 acyltransferase site.

**Step 3 (SucB/E2o):** The succinyl group is transferred from dihydrolipoamide to CoA, releasing **succinyl-CoA** — a high-energy thioester used downstream by succinyl-CoA synthetase for substrate-level phosphorylation.

**Step 4 (LpdG/E3):** The reduced dihydrolipoamide is reoxidized by E3 (FAD), regenerating oxidized lipoamide and reducing NAD⁺ to **NADH**, which feeds oxidative phosphorylation.

### Regulation and metabolic significance

SucA sits at a **triple control point**:

1. **Rate-limiting kinetics** — the E1o step gates overall flux through the second half of the TCA cycle.
2. **Allosteric feedback** — the active site can accommodate and be inhibited by oxaloacetate at physiological concentrations, and an AMP-binding pocket senses energy charge, coupling activity to the cell's metabolic state (from F003).
3. **Post-translational modification** — the conserved Thr411 AMPylation site (F008) implies regulation by the YdiU/SelO AMPylase, a stress-responsive mechanism.

Metabolically, 2-oxoglutarate is the principal **carbon/nitrogen crossroads**: it is the acceptor of ammonia in glutamate/glutamine synthesis and the exit point for amino-acid-derived carbon into the TCA cycle. By controlling the drain of 2-oxoglutarate toward succinyl-CoA, SucA partitions flux between **(a) respiratory energy generation** (NADH → oxidative phosphorylation; succinyl-CoA → substrate-level phosphorylation) and **(b) biosynthetic precursor supply** (retaining 2-oxoglutarate for nitrogen assimilation and glutamate-family amino acids). In *P. putida* KT2440, whose central carbon metabolism is noted for tight, largely post-transcriptional/metabolic regulation ([PMID: 24951791](https://pubmed.ncbi.nlm.nih.gov/24951791/)), this node is especially important for balancing the organism's versatile catabolic lifestyle with biosynthesis.

### Localization

The OGDHc, including SucA, is a **soluble cytoplasmic multienzyme complex** in bacteria (the analog of the mitochondrial-matrix complex in eukaryotes). There are no signal peptides, transmembrane segments, or secretion signals in the annotation; the enzyme carries out its function in the cytosol, where it associates non-covalently around the E2 core.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|------|-----------------|---------------------|
| [17367808](https://pubmed.ncbi.nlm.nih.gov/17367808/) | *Crystal structure of the E1 component of the E. coli 2-oxoglutarate dehydrogenase complex* | **Primary structural evidence.** Establishes EC 1.2.4.2, ThDP dependence, rate-limiting role, single-chain α/β fusion, active-site His/Ser cluster, oxaloacetate inhibition, and AMP-binding pocket. Underpins F001, F003, F005, F008. |
| [6403946](https://pubmed.ncbi.nlm.nih.gov/6403946/) | *Multiple random coupling in the α-ketoglutarate dehydrogenase complex of E. coli* | Documents lipoyl-arm servicing of the E1 subunit and lipoyl-lipoyl channeling network. Supports F002. |
| [36256893](https://pubmed.ncbi.nlm.nih.gov/36256893/) | *Influence of 5-FU on the α-KGDH complex* | Confirms canonical three-subunit (E1/E2/E3) architecture. Supports F002. |
| [3543212](https://pubmed.ncbi.nlm.nih.gov/3543212/) | *Cloning and expression of succinyl-CoA synthetase genes of E. coli* | Defines the *suc* operon context (sucA/sucB with sucCD). Supports F004. |
| [9209026](https://pubmed.ncbi.nlm.nih.gov/9209026/) | *Aerobic regulation of the sucABCD genes of E. coli* | Establishes sucAB = α-ketoglutarate dehydrogenase and ArcA/Fnr/sdhC-promoter regulation. Supports F004. |
| [30497599](https://pubmed.ncbi.nlm.nih.gov/30497599/) | *Novel genes in high-hydrostatic-pressure resistance of E. coli* | Genetic phenotype of sucA/sucB disruption. Supports F004. |
| [41722662](https://pubmed.ncbi.nlm.nih.gov/41722662/) | *Alpha-ketoglutarate dehydrogenase: more than just a TCA cycle enzyme* | States 4th-TCA-step reaction and metabolic integration. Supports F006. |
| [29191460](https://pubmed.ncbi.nlm.nih.gov/29191460/) | *2-oxoadipate and 2-oxoglutarate dehydrogenase complexes share E2 and E3* | Quantifies E1a's ~49× preference for 2-oxoadipate, distinguishing it from 2-oxoglutarate-specific E1o. Supports F006 (substrate specificity by contrast). |
| [24951791](https://pubmed.ncbi.nlm.nih.gov/24951791/) | *Functional structure of central carbon metabolism in P. putida KT2440* | Places the TCA cycle within tightly regulated central metabolism of the target organism. Context for F004/F007. |
| [35530286](https://pubmed.ncbi.nlm.nih.gov/35530286/) | *Targeting 2-oxoglutarate dehydrogenase for cancer treatment* | Reviews OGDHc as a redox sensor and αKG/glutaminolysis intersection (mechanistic context, eukaryotic). |

Additional reviewed literature (PMIDs 28579060, 27986918, 20228444, 11368334, 6341609, 25184115, 40609475, 39299525, 1730230) provides supporting context on E3 deficiency, complex reengineering, random steady-state channeling models, the E1 ping-pong mechanism, KGDC quaternary heterogeneity, and ROS generation — reinforcing the general mechanistic model of 2-oxo-acid dehydrogenase complexes within which SucA functions.

**Direct experimental evidence** exists for the *E. coli* ortholog (crystal structure, kinetics, operon regulation, knockout phenotypes). **Inference from evolution/structure** (65.6% identity, conserved active-site and regulatory residues) transfers this to *P. putida*. **Bioinformatic/genomic evidence** (KEGG operon annotation) confirms the complete complex is encoded in *P. putida* itself.

---

## Limitations and Knowledge Gaps

1. **No direct enzymology of PP_4189.** There is no published biochemical characterization (purified enzyme, kinetics, K_m, k_cat, crystal structure) of the *P. putida* KT2440 SucA protein specifically. All mechanistic and substrate-specificity claims rest on orthology transfer from *E. coli* (65.6% identity) and the broader alpha-ketoglutarate dehydrogenase family.

2. **Substrate specificity is inferred, not measured, for the target.** While the active-site His cluster is conserved, the possibility of a broadened or altered substrate range (e.g., partial activity toward other 2-oxo acids) has not been experimentally excluded in *P. putida*.

3. **Regulation is largely extrapolated.** Oxaloacetate inhibition, AMP binding, and Thr411 AMPylation are established or predicted from *E. coli*/UniProt annotation. Their operation and physiological relevance in *P. putida* KT2440 (which relies heavily on post-transcriptional/metabolic regulation, [PMID: 24951791](https://pubmed.ncbi.nlm.nih.gov/24951791/)) remain to be tested.

4. **Complex stoichiometry and quaternary structure** in *P. putida* are unknown; the E. coli complex itself may be structurally heterogeneous ([PMID: 6341609](https://pubmed.ncbi.nlm.nih.gov/6341609/)), so precise E1:E2:E3 ratios in *P. putida* are unconfirmed.

5. **Operon transcription is inferred from gene contiguity and small intergenic gaps**; the actual transcriptional unit boundaries, promoters, and regulators for the *P. putida sdhAB–sucAB–lpdG* cluster have not been experimentally mapped.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and kinetic characterization.** Clone PP_4189 (± PP_4188/PP_4187), purify, and reconstitute the OGDHc in vitro. Measure K_m and k_cat for 2-oxoglutarate and, as controls, 2-oxoadipate and pyruvate to directly confirm substrate specificity and quantify discrimination — mirroring the DHTKD1/E1a comparison ([PMID: 29191460](https://pubmed.ncbi.nlm.nih.gov/29191460/)).

2. **Structural determination.** Solve the crystal or cryo-EM structure of *P. putida* SucA (or the whole complex) to verify the predicted single-chain α/β fold and the His266/His304/His737 active-site geometry, and to test oxaloacetate/AMP binding pockets predicted from the *E. coli* structure ([PMID: 17367808](https://pubmed.ncbi.nlm.nih.gov/17367808/)).

3. **Gene knockout / conditional depletion.** Construct a PP_4189 deletion or knockdown in KT2440 and characterize growth on TCA-cycle-dependent carbon sources, glutamate/nitrogen handling, redox balance, and stress survival (e.g., analogous to the HHP phenotype in *E. coli*, [PMID: 30497599](https://pubmed.ncbi.nlm.nih.gov/30497599/)).

4. **Test AMPylation regulation.** Verify whether Thr411 is AMPylated in vivo by the *P. putida* YdiU/SelO homolog and whether this modulates activity under nutrient/stress transitions — a targeted test of the conserved regulatory site (F008).

5. **Operon mapping.** Use RT-PCR/RNA-seq and promoter-reporter fusions to define the transcriptional unit(s) spanning `sdhAB–sucAB–lpdG` and identify regulators (e.g., anaerobiosis/oxygen control analogous to ArcA/Fnr in *E. coli*, [PMID: 9209026](https://pubmed.ncbi.nlm.nih.gov/9209026/)).

6. **Metabolic flux analysis.** Use ¹³C-labeling in KT2440 to quantify flux partitioning at the 2-oxoglutarate node between respiratory oxidation (via SucA) and nitrogen assimilation/biosynthesis, directly probing SucA's role as the carbon/nitrogen branch-point gate.


## Artifacts

- [OpenScientist final report](sucA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](sucA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:17367808
2. PMID:6403946
3. PMID:36256893
4. PMID:3543212
5. PMID:9209026
6. PMID:30497599
7. PMID:41722662
8. PMID:29191460
9. PMID:24951791
10. PMID:6341609